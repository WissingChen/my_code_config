---
name: slide_deck
description: Self-contained HTML slide decks as a PPT replacement. Load when the user asks to present the project (or a subset such as motivation, contributions, methods, experiment results) as a horizontal-paging HTML file.
requires: research_manager
---

## Output Contract

- Label every claim as **fact** (with source) or **speculation** (explicitly marked, e.g. `[speculation]`). Never state speculation as fact — this is a hard red line.
- Plain language: conclusion first; explain any jargon in one short sentence on first use; no filler phrases or padding; prefer tables or lists when they aid scanning.

# Slide Deck — HTML Instead of PPT

`slide_deck` generates one self-contained HTML file with horizontal paging. It does not create content: every claim and figure comes from existing research artifacts.

## 1. Scope

- Full deck sections: motivation → contributions → methods → experiment results → conclusion / next steps.
- Partial deck: generate only the sections the user names. State in the reply which sections are included and which artifacts they draw from.

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
- Slide titles are assertions, not topics ("X reduces error by 40%", not "Results").
- Figure slides carry a caption with uncertainty semantics. Figures are embedded as base64 by default so the file stays portable; relative-path linking only when the user asks for a small file.
- Print-friendly: `@media print` renders each slide as one landscape page, so browser print-to-PDF replaces a PPT handout.

## 4. Visual Style Methodology

Style is guided by principles, not a fixed theme; the user iterates on rendered output over time.

- Centralize every style decision as CSS custom properties in one `:root` block (colors, fonts, spacing, slide padding). This is the user-tuning layer: style changes are one-place edits, never scattered inline styles.
- Hierarchy comes from size, weight, and space. Color is reserved for meaning: at most one accent, plus semantic colors only when the content itself carries status.
- Consistency beats any specific choice: the same element type looks the same on every slide.
- Every visual element must earn its pixels; remove decoration that carries no information.
- Start minimal. Add styling only in response to a concrete readability problem observed in the rendered deck.
- Keep two change layers separate: content changes regenerate from source artifacts; style changes edit the `:root` tokens. Iterating on one must never disturb the other.

## 5. Output Discipline

- Default path: `.kilo/reports/YYYY-MM-DD-deck.html` or a user-specified path. Generated artifact: regenerate from sources instead of hand-editing.
- Before generating, show the slide outline (one line per slide) and get user confirmation.
- The deck ends with a sources slide listing every artifact used.
