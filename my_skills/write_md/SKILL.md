---
name: write_md
description: Markdown readability and visual formatting. Load when the user asks to improve readability, format a document, add visual boxes, or make a Markdown page scannable. Handles language, structure, and a renderer-aware presentation layer.
---

## Output Contract

- 先说结论，再给必要依据和下一步。
- 默认短句和常用词；术语只在更准确时用，首次出现直接解释。
- 内部状态、流程和检查表默认不展示；只有影响决定或用户明确要求时才展开。
- 外部事实、论文结论和数字附来源；不确定的直接写"尚未验证"或"我推测"，不给每句话机械加 fact/speculation 标签。
- 一段能说清就不用表格；独立要点用列表；只有横向比较才用表格。
- 不写套话、廉价肯定、重复总结和固定收尾。

# write_md — Readable Markdown

## 1. Language Layer

- **Anti-jargon**: if a term can be deleted without changing meaning, delete it.
- **One sentence, one meaning**: break stacked abstractions.
- **Concrete verbs over abstract nouns**: "the model drops recall" beats "performance degradation is observed."
- **Explain on first use**: every concept introduced must be explainable in plain language.
- **Say it straight**: every paragraph's first sentence carries the point; rewrite headings that are abstract nouns into statements; never wrap internal process names (gate, readiness, handoff, lifecycle) in front of the reader — say what is confirmed, what is missing, what happens next.
- **Precision exception**: in manuscripts, necessary technical terms stay — explain the meaning in plain words first, then give the exact term.

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
- Propose cleanup (delete/merge) only when concrete stale or duplicate content is found — not as a fixed sign-off.
