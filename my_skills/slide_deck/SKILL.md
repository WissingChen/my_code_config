---
name: slide_deck
description: Self-contained HTML slide decks as a PPT replacement. Load when the user asks to present the project (or a subset such as motivation, contributions, methods, experiment results) as a horizontal-paging HTML file.
requires: research_manager
---

## Output Contract

- 先说结论，再给必要依据和下一步。
- 默认短句和常用词；术语只在更准确时用，首次出现直接解释。
- 内部状态、流程和检查表默认不展示；只有影响决定或用户明确要求时才展开。
- 外部事实、论文结论和数字附来源；不确定的直接写"尚未验证"或"我推测"，不给每句话机械加 fact/speculation 标签。
- 一段能说清就不用表格；独立要点用列表；只有横向比较才用表格。
- 不写套话、廉价肯定、重复总结和固定收尾。

# Slide Deck — HTML Instead of PPT

`slide_deck` generates one self-contained HTML file with horizontal paging. It does not create content: every claim and figure comes from existing research artifacts.

## 1. Scope

- Full deck sections: motivation → contributions → methods → experiment results → conclusion / next steps.
- Partial deck: generate only the sections the user names. State in the reply which sections are included and which artifacts they draw from.
- Boundary: this skill produces horizontal presentation decks only. Scrolling self-contained HTML **report** rendering belongs to `write_md` (§7); do not stretch a deck into a report or vice versa.

## 2. Content Sourcing

| Section | Primary sources |
|---|---|
| Motivation | `proposal/NN-slug/experiment-plan.md`, direction `00-overview.md` |
| Contributions | final `REPORT.md`, promotion summary, status snapshots |
| Methods | `REPORT.md` methods, `ENN-experiment-report.md` setup and controls |
| Experiment results | `REPORT.md` results, retained evidence figures, key results tables |

- Every slide carrying a number or claim cites its source artifact in a small footer. Never invent numbers.
- New charts are delegated to `result_visualization`; statistical claims to `result_analysis`. `slide_deck` only re-encodes approved content into slides.

## 3. Technical Spec

- Single `.html` file: inline CSS and JS; no CDN, frameworks, or external fonts.
- Horizontal paging: `←`/`→` arrow keys, clickable prev/next controls, slide counter `n / N`.
- 16:9 slides, base font ≥24px; one idea per slide.
- Slide titles are assertions, not topics ("X reduces error by 40%", not "Results"). But never upgrade a trend into a causal or certain claim for punchiness — when evidence is thin, the title keeps the hedge.
- Figure slides carry a caption with uncertainty semantics. Figures are embedded as base64 by default so the file stays portable; relative-path linking only when the user asks for a small file.
- Print-friendly: `@media print` renders each slide as one landscape page, so browser print-to-PDF replaces a PPT handout.
- Layout rule: **boxes hug their content; whitespace lives outside boxes.** Never stretch a card to full height with `flex:1` when its content is short — that traps dead space inside the border and reads as "empty". Make the row fit (`flex:0 0 auto`) and center the content block vertically in the slide, so remaining space distributes evenly outside the boxes.

## 4. Scraping Figures from Papers (Related Work)

When the deck needs teaser/pipeline figures from papers:

1. **arXiv HTML first**: `https://arxiv.org/html/<id>/x1.png` is the teaser in most recent papers; `x2.png` is usually the pipeline figure. Confirm by fetching the HTML page and checking the `<img>` tags when unsure.
2. **PDF fallback**: some papers have no HTML version, or the HTML version's figures failed to extract (check for missing/empty `src`). Then: `curl -O https://arxiv.org/pdf/<id>`, render with `pdftoppm -png -f N -l N -r 150 paper.pdf page`, and crop the figure region with PIL.
3. **Verify every download**: run `file *.png` and open dimensions — arXiv can return an HTML error page with a 200 status. A ~8 KB "PNG" is an error page, not a figure.
4. **Optimize before base64 embedding**: resize to ≤1100 px wide, save as JPEG q≈82. Raw arXiv PNGs (up to 10 MB) would make the deck file balloon; optimized figures keep a 15–20 slide deck at 1–2 MB.
5. Credit each figure in the slide footer (`arXiv <id> Fig.N, HTML/PDF`) and in the sources slide.

## 5. Visual QA Loop (Mandatory)

Never deliver a deck without rendering and inspecting **every** slide.

1. Screenshot each slide with headless Chromium: `chromium --headless --no-sandbox --screenshot=out.png --window-size=1600,900 file.html` (jump to slide N by temporarily replacing the initial `go(0)` call in a copied file).
2. Snap Chromium (Ubuntu default) can only read/write the home directory — copy the deck to `~` for preview and write screenshots there.
3. Batch screenshot loops occasionally produce stale or wrong-slide captures; any suspicious shot must be re-taken individually before believing it.
4. Defect checklist per slide:
   - boxes with large internal dead space (see §3 layout rule);
   - SVG text overlapping shapes or clipped at the `viewBox` edge;
   - code blocks and wide tables overflowing horizontally or colliding with the footer;
   - text clipped at slide edges.
5. Global font changes (e.g. uniform ×1.18 scaling of all `font-size` values) are a legitimate iteration step, but every table, code block, and footer must be re-checked afterwards — they are the first to overflow.

## 6. Visual Style Methodology

Style is guided by principles, not a fixed theme; the user iterates on rendered output over time.

- Centralize every style decision as CSS custom properties in one `:root` block (colors, fonts, spacing, slide padding). This is the user-tuning layer: style changes are one-place edits, never scattered inline styles.
- Hierarchy comes from size, weight, and space. Color is reserved for meaning: at most one accent, plus semantic colors only when the content itself carries status.
- Consistency beats any specific choice: the same element type looks the same on every slide.
- Every visual element must earn its pixels; remove decoration that carries no information.
- Start minimal. Add styling only in response to a concrete readability problem observed in the rendered deck.
- Keep two change layers separate: content changes regenerate from source artifacts; style changes edit the `:root` tokens. Iterating on one must never disturb the other.

## 6.5 风格模板库（templates/）

用户命名保存的风格模板放在 `templates/<风格名>/`，索引与维护规则见 `templates/README.md`。

- 用户点名某个已保存风格时：先读该模板的 `STYLE.md`，按其风格 DNA 与组件词汇**参考风格**，按内容拓扑从模式库选择或组合布局；`template.html` 只是一种模式的实例，不凭记忆重写样式、不硬套骨架。
- 用户要求保存新风格时：从已通过视觉 QA 的 slide 提取 CSS tokens 与组件骨架，新建 `templates/<风格名>/STYLE.md` + `template.html`，在 `templates/README.md` 登记，并对 `template.html` 做一次截图 QA。
- 风格的后续修订回写到模板文件（单一事实源），套用页面只替换内容、不改模板 token。
- 当前模板：**国自然基金风格**（技术路线插图视觉语言：面板/色彩/箭头语法 + 5 种布局模式）、**瑞士国际主义风格**（整套 deck 视觉体系：网格 + 极细巨字 + 单一 accent）。索引见 `templates/README.md`。

## 7. Output Discipline

- Default path: `.kilo/reports/YYYY-MM-DD-deck.html` or a user-specified path. Generated artifact: regenerate from sources instead of hand-editing.
- Before generating, show the slide outline (one line per slide) and get user confirmation.
- The deck ends with a sources slide listing every artifact used.
