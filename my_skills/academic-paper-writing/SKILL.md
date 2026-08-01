---
name: academic-paper-writing
description: Top-tier CS/AI/Robotics manuscript writing taste. Triggers on drafting, revising, or polishing academic papers in computer vision, machine learning, robotics, image processing, and related fields.
---

## Output Contract

- 先说结论，再给必要依据和下一步。
- 默认短句和常用词；术语只在更准确时用，首次出现直接解释。
- 内部状态、流程和检查表默认不展示；只有影响决定或用户明确要求时才展开。
- 外部事实、论文结论和数字附来源；不确定的直接写"尚未验证"或"我推测"，不给每句话机械加 fact/speculation 标签。
- 一段能说清就不用表格；独立要点用列表；只有横向比较才用表格。
- 不写套话、廉价肯定、重复总结和固定收尾。

# Academic Writing — Evidence-Bound Manuscripts

## Core Premise

A strong paper is built on audited evidence, clear claims, and a structure that lets the reader follow the reasoning. Prose may clarify but cannot strengthen claims beyond the evidence.

## Narrative Arc

1. **Opening**: Identify the precise gap. Avoid generic statements. Anchor on the strongest credible work that still falls short; then cite the closest recent direct work. Never pad the gap with weak papers.
2. **Insight**: State the re-framing in one crisp sentence. If you cannot, the paper is not yet focused.
3. **Method**: Show the idea before the equations. Figures should communicate the core mechanism in 30 seconds.
4. **Experiments**: Build from evidence:
   - One dense table with the main result.
   - An ablation that isolates the claimed reason for improvement, without universal thresholds.
   - A generalization check on an unseen setting or dataset.
   - A limitation figure showing where the method fails.
5. **Ending**: Return to the opening gap, summarize what the evidence shows, and state the remaining boundary honestly.

## The Voice

- Write for a brilliant colleague from an adjacent subfield.
- Avoid hype words: "novel", "first", "significantly" (without effect size and uncertainty), "obviously", "clearly", "state-of-the-art".
- Prefer verbs that describe mechanism: "enables", "reveals", "decouples", "bridges".
- Alternate sentence length. Active voice for contributions; passive for established facts, rarely.
- Define every symbol at first use. Reference every equation and figure in the text.
- Avoid AI-flavored punctuation: em dashes and colons abused as dramatic pivots.

## Evidence Ceiling and Traceability

Draft claims only from promoted implementations and retained evidence records. Every quantitative claim must trace to an experiment ID and a retained artifact (figure, table, or log manifest). Do not select attractive runs from experiment branches.

Required reporting: effect size, uncertainty interval, and practical significance. Do not rely on p-values or single thresholds like `<1%`, `90% of gain`, or `sharp peak`.

## Figures and Tables

- Figures are arguments, not decoration. Show flow and mechanism, not just layout.
- Delegate figure production and visual validation to `result_visualization`; the paper skill decides narrative placement and caption argument.
- Consistent iconography across all figures.
- Error maps and distributions beat single scalars when heterogeneity matters.
- Colorblind-safe palettes; grayscale readability is a discipline.
- Tables: no vertical lines, aligned decimals, best result in bold, include parameters and cost metrics.
- Captions are self-contained and define abbreviations.

## Ablations and Sensitivity

- Test the hard thing: remove or replace the claimed essential component. Report the effect size and uncertainty; do not require a fixed drop threshold.
- Include a replacement ablation: compare against the simplest baseline addressing the same problem.
- Main comparisons must include the strongest credible method, not only weak direct competitors that are easy to beat.
- Hyperparameter sensitivity: report the range and whether the effect is stable or brittle, without relying on a `sharp peak` narrative.

## Citation Ethics

Before citing, delegate retrieval, verification (year, claim), and capture to `.kilo/knowledge/papers/` to `knowledge_keeper`. A citation is a promise; do not make it lightly.

Before drafting, read the direction's anchor set and minimum quality bar, and answer: whose problem definition do we follow, whose experimental/theoretical standard do we follow, who is the closest competitor, and do our results actually clear that bar. If the last answer is no, the problem is unfinished research, not writing.

In Related Work, synthesize by idea, not chronology. Do not treat all related papers as equals — anchor papers, direct competitors, and background get different weight. When criticizing, be surgical: describe the assumption that restricts applicability, not a dismissive summary.

## The Reviewer's Mind

- **5-minute test**: problem, insight, main result — clear from the title, abstract, and first figure.
- **Surprise test**: figures and tables tell a coherent story without the text.
- **Objection test**: list every objection; preempt or acknowledge each as a limitation.
- **Title test**: accessible to a non-specialist without being vague. Under 100 characters, no jargon, no abbreviations.

## Limitations and Reproducibility

State limitations with the same precision as successes. Include a failure-case figure and explain why the failure occurs. Report framework, hardware, training time, batch size, optimizer, schedule, augmentation, loss, seeds, dataset size/splits/preprocessing, and metric definitions. Hidden tricks are reproducibility failures, not cleverness.

## Manuscript Storage

Store active manuscripts in the direction's `manuscript/` directory or an external repository linked from the direction overview. Generated manuscripts are exempt from the 150-line operational document budget.

## Final Polish

Read aloud. Listen for clunk, echo, drift, hype, math orphans, and figure orphans. Fix them. Then fix them again.
