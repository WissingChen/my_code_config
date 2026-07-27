---
name: write_md
description: Markdown readability and visual formatting. Load when the user asks to improve readability, format a document, add visual boxes, or make a Markdown page scannable. Handles language, structure, and a renderer-aware presentation layer.
---

## Output Contract

- Label every claim as **fact** (with source) or **speculation** (explicitly marked, e.g. `[speculation]`). Never state speculation as fact — this is a hard red line.
- Plain language: conclusion first; explain any jargon in one short sentence on first use; no filler phrases or padding; prefer tables or lists when they aid scanning.

# write_md — Readable Markdown

## 1. Language Layer

- **Anti-jargon**: if a term can be deleted without changing meaning, delete it.
- **One sentence, one meaning**: break stacked abstractions.
- **Concrete verbs over abstract nouns**: "the model drops recall" beats "performance degradation is observed."
- **Explain on first use**: every concept introduced must be explainable in plain language.

## 2. Structure Layer

- **Conclusion first**: the first paragraph states the point.
- **Key numbers bold**: readers scanning should see the decisive numbers.
- **30-second scan test**: a tired reader must grasp the gist in 30 seconds.
- **Figure-text rhythm**: long documents must not contain a full-screen wall of text; break it with tables, diagrams, or boxes. Every non-text element must carry information — no forced visuals in short or self-evident documents.

## 3. Presentation Layer

Box budget: **≤3 per document**. If a box does not change what the reader sees first, do not use it.

Renderer-aware formatting (default target: local reading in VS Code / Typora / Obsidian):

- **Local renderers**: raw HTML boxes with inline styles render correctly; this is the default choice.
- **GitHub**: inline styles are stripped; fall back to plain Markdown, blockquotes, or alerts (`> [!NOTE]`) only when the document will be viewed there.
- **Manuscripts**: no UI-style boxes by default.

```html
<!-- Default for local renderers; strip for GitHub targets -->
<div style="background:#3498db1a; border-left:4px solid #3498db; padding:8px 12px; margin:8px 0;">...</div>
```

## 4. Semantic Color Palette

One color, one meaning:

| Role | Color |
|------|-------|
| Info | `#3498db` |
| Success | `#27ae60` |
| Emphasis | `#9b59b6` |
| Caution | `#e67e22` |
| Danger | `#e74c3c` |
| Neutral | `#7f8c8d` |
| Framework | `#2c3e50` |

## 5. Diagrams and Figures

Standard flowcharts, sequence diagrams, architecture diagrams, and data figures are produced by `result_visualization`. `write_md` owns need judgment and integration: during a readability pass, identify positions where a diagram or table communicates better than prose, decide placement, callouts, and caption context, then delegate production to `result_visualization`.

## 6. Final Report Readability Pass

After scientific content and visuals are fixed, apply a final pass: conclusion-first structure, consistent terminology, figure/table callouts, caption placement, and a 30-second scan path. Do not alter statistical claims, evidence verdicts, or retention decisions.

## 7. Global Constraints

- No decorative formatting.
- Never replace a plain table with a boxed table unless emphasis is needed.
- File writes only after user confirmation.
- End each formatting session by proposing what to delete or merge.
