#!/usr/bin/env python3
"""Render a Markdown report to an A4 PDF via headless Chromium.

Pipeline: Markdown -> self-contained HTML (inline CSS, base64 images, mermaid
rendered by the browser) -> chromium --headless --print-to-pdf.

Why headless Chromium: it is the only local engine that executes JavaScript, so
live ```mermaid blocks render (Prince, Calibre ebook-convert and WeasyPrint do
not run JS). Page size comes from the CSS @page rule, so A4 is global per
stylesheet, not per file.

Usage:
    python build_pdf.py REPORT.md [-o REPORT.pdf] [--css report_pdf.css]
                                  [--title "..."] [--keep-html] [--timeout 15000]

Notes / limits:
    * Chromium must be able to read the temp HTML and write the temp PDF, so
      both live under $HOME (snap Chromium is confined and cannot use /tmp or
      other mounts). The final PDF is copied to the requested output path, which
      may be anywhere the caller can write.
    * Mermaid is inlined from a local mermaid.min.js when one is found (e.g. the
      Markdown Preview Enhanced extension); otherwise it loads from the CDN.
"""
import argparse
import base64
import mimetypes
import os
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

CHROMIUM_CANDIDATES = (
    "chromium", "chromium-browser", "google-chrome",
    "google-chrome-stable", "chrome",
)
MERMAID_CDN = "https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.min.js"
MERMAID_LOCAL_GLOBS = (
    ".vscode-server/extensions/*markdown-preview-enhanced*/crossnote/dependencies/mermaid/mermaid.min.js",
    ".vscode/extensions/*markdown-preview-enhanced*/crossnote/dependencies/mermaid/mermaid.min.js",
    ".local/share/code-server/extensions/*markdown-preview-enhanced*/crossnote/dependencies/mermaid/mermaid.min.js",
)
DEFAULT_CSS = Path(__file__).with_name("report_pdf.css")


def find_chromium():
    for name in CHROMIUM_CANDIDATES:
        path = shutil.which(name)
        if path:
            return path
    raise SystemExit(
        "no Chromium/Chrome found on PATH (tried: %s)" % ", ".join(CHROMIUM_CANDIDATES)
    )


def find_mermaid_js():
    home = Path.home()
    for pattern in MERMAID_LOCAL_GLOBS:
        for path in sorted(home.glob(pattern)):
            if path.is_file():
                return path
    return None


def strip_front_matter(text):
    if text.startswith("---"):
        end = text.find("\n---", 3)
        if end != -1:
            return text[end + 4:].lstrip("\n")
    return text


def build_html(md_text, css_text, title, mermaid_src):
    return f"""<!DOCTYPE html>
<html lang="zh">
<head>
<meta charset="utf-8">
<title>{title}</title>
<style>
{css_text}
</style>
<script src="{mermaid_src}"></script>
<script>
try {{ mermaid.initialize({{ startOnLoad: true }}); }}
catch (e) {{ console.error(e); }}
</script>
</head>
<body>
{md_text}
</body>
</html>
"""


def render_markdown(md_text):
    from markdown_it import MarkdownIt

    md = MarkdownIt("gfm-like", {"html": True, "linkify": False, "typographer": False})

    # Pull ```mermaid fences out before markdown rendering; the browser renders
    # them after the HTML loads. Placeholders use a token markdown never touches.
    mermaid_blocks = []

    def stash(match):
        mermaid_blocks.append(match.group(1))
        return f"\n@@MERMAID_{len(mermaid_blocks) - 1}@@\n"

    md_text = re.sub(r"```mermaid[ \t]*\n(.*?)```", stash, md_text, flags=re.S)
    html = md.render(md_text)
    for i, block in enumerate(mermaid_blocks):
        html = html.replace(
            f"<p>@@MERMAID_{i}@@</p>",
            f'<pre class="mermaid">{block.strip()}</pre>',
        )
    return html


def embed_images(html, base_dir):
    def repl(match):
        src = match.group(1)
        if src.startswith(("http://", "https://", "data:")):
            return match.group(0)
        path = (base_dir / src).resolve()
        if not path.is_file():
            print(f"warn: image not found: {src}", file=sys.stderr)
            return match.group(0)
        mime = mimetypes.guess_type(path.name)[0] or "application/octet-stream"
        data = base64.b64encode(path.read_bytes()).decode("ascii")
        return match.group(0).replace(f'"{src}"', f'"data:{mime};base64,{data}"')

    return re.sub(r'<img[^>]+src="([^"]+)"', repl, html)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("input", type=Path)
    ap.add_argument("-o", "--output", type=Path)
    ap.add_argument("--css", type=Path, default=None)
    ap.add_argument("--title", default=None)
    ap.add_argument("--keep-html", action="store_true")
    ap.add_argument("--timeout", type=int, default=15000, help="virtual-time-budget ms")
    args = ap.parse_args()

    src = args.input.resolve()
    if not src.is_file():
        raise SystemExit(f"input not found: {src}")
    out = (args.output or src.with_suffix(".pdf")).resolve()
    css_path = (args.css or DEFAULT_CSS).resolve()
    css_text = css_path.read_text(encoding="utf-8")

    raw = src.read_text(encoding="utf-8")
    title = args.title or src.stem.replace("-", " ")
    m = re.search(r"^#\s+(.+)$", raw, flags=re.M)
    if m:
        title = m.group(1).strip()

    html = embed_images(render_markdown(strip_front_matter(raw)), src.parent)

    # Chromium (snap) can only read/write paths under $HOME; use a plain dir.
    work = Path.home() / "pdf_export_tmp"
    work.mkdir(parents=True, exist_ok=True)
    tmp = Path(tempfile.mkdtemp(prefix="build_", dir=work))

    mermaid_path = find_mermaid_js()
    if mermaid_path is not None:
        shutil.copyfile(mermaid_path, tmp / "mermaid.min.js")
        mermaid_src = "mermaid.min.js"
    else:
        mermaid_src = MERMAID_CDN

    page = build_html(html, css_text, title, mermaid_src)
    html_file = tmp / "doc.html"
    pdf_file = tmp / "doc.pdf"
    html_file.write_text(page, encoding="utf-8")

    chrom = find_chromium()
    cmd = [
        chrom, "--headless", "--no-sandbox", "--disable-gpu",
        f"--virtual-time-budget={args.timeout}",
        "--no-pdf-header-footer", "--hide-scrollbars",
        f"--print-to-pdf={pdf_file}", str(html_file),
    ]
    print("$ " + " ".join(cmd))
    proc = subprocess.run(cmd, capture_output=True, text=True)
    if not pdf_file.is_file() or pdf_file.stat().st_size == 0:
        tail = "\n".join(
            line for line in (proc.stdout + proc.stderr).splitlines()
            if "AppArmor" not in line and "dbus" not in line.lower()
        )[-800:]
        raise SystemExit(f"chromium did not produce a PDF\n{tail}")

    out.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(pdf_file, out)
    size_kb = out.stat().st_size / 1024
    print(f"wrote {out} ({size_kb:.0f} KB)")

    if args.keep_html:
        kept = out.with_suffix(".html")
        shutil.copyfile(html_file, kept)
        print(f"kept {kept}")
    shutil.rmtree(tmp, ignore_errors=True)


if __name__ == "__main__":
    main()
