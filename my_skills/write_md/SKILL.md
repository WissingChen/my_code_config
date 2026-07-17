---
name: write_md
description: Markdown readability and visual formatting. Load when the user asks to improve readability, format a document, add visual boxes, or make a Markdown page scannable. Handles language, structure, and a tight presentation layer.
---

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

## 3. Presentation Layer

Box budget: **≤3 per document**. If a box does not change what the reader sees first, do not use it.

Templates to use:

- **Info** box: background, context.
- **Warning** box: risks, critical caveats.
- **Data Table** box: metrics, parameters, comparisons.

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

## 5. Diagrams

Standard flowcharts, sequence diagrams, and architecture diagrams are handled by `result_analysis` (Mermaid + matplotlib). `write_md` only supplies HTML boxes for free-layout visual emphasis.

## 6. Global Constraints

- No decorative formatting.
- Never replace a plain table with a boxed table unless emphasis is needed.
- End each formatting session by proposing what to delete or merge.
