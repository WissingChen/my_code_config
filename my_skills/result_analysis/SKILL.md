---
name: result_analysis
description: Evidence interpretation, experimental-data analysis, and plotting. Load when the user asks to analyze results, interpret data, decide whether to kill/pivot/continue a direction, or produce plots/charts/diagrams from numeric data.
requires: research_manager
---

# Result Analysis — Interpret Evidence, Decide Direction

## Step 0: Adequacy Check

Before interpreting any data, answer:

1. What claim can this experiment actually prove?
2. What metric or control would falsify that claim?
3. Does the evaluation setup satisfy (1) and (2)?

If not, fix the evaluation first. Do not draw conclusions from weak evidence.

## Step 1: Evidence Audit (Fact Layer)

Strip away interpretation. List undeniable facts with numbers and units. De-fuzzify vague words like "significant" or "clear trend" by demanding a quantitative definition.

Statistics checklist (apply before treating any number as evidence):

- **Seeds**: results must be mean ± std over ≥3 seeds. A single run is an anecdote, not evidence.
- **Difference vs. variance**: a claimed improvement must exceed run-to-run variance. If variance is unknown, that is missing evidence — say so.
- **Sample size**: if n is too small for the claim (e.g. evaluating on a handful of examples), flag it; do not compute or imply significance.
- **Missing baseline or control**: stop here and request it, per Step 0.

## Step 2: Competing Hypotheses

Propose at least two mutually exclusive hypotheses (H1, H2, ...). Each needs:

- Mechanism explanation
- Falsification condition

Distinguish **fact / inference / speculation**.

## Step 3: Confidence Update

| Hypothesis | Prior | Evidence | Posterior | Missing Information |
|------------|-------|----------|-----------|---------------------|
| H1 | ... | +/- ... | ... | ... |

## Step 4: Verdict

Choose one:

- **Kill**: direction falsified → write falsified SUMMARY to `archive/` (see research_manager).
- **Pivot**: keep assets, change the core hypothesis or question.
- **Continue**: run the next experiment with the highest discriminating power. State which two hypotheses it distinguishes.

## Step 5: Patch-Trap Guard

If two consecutive rounds only patch small issues and never touch the core hypothesis, force a direction-level verdict before a third patch.

Tracking: record `patch_round: N` in the analysis file's Verdict section. Increment N on every iteration that only patches small issues; reset to 0 when the core hypothesis changes. At N=2, the next verdict must be direction-level (Kill / Pivot / Continue) — no third patch.

## Step 6: Mandatory Visualization

When numeric data exists, the conclusion must include a generated chart — unless the data is trivial (≤3 numbers, or a chart would not change the conclusion; use a plain table then). Never produce a chart that adds no information over the numbers themselves.

- matplotlib / seaborn
- Colorblind-safe palette
- PDF vector output, error bars, axis labels with units
- Architecture / flow diagrams: Mermaid

For detailed plotting guidance, load `plotting-reference.md`.

## Output Constraints

- No cheap affirmations.
- No unexamined causal claims.
- File writes only after user confirmation.
- End each session by proposing what to archive, delete, or merge.
