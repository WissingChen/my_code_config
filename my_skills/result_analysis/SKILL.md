---
name: result_analysis
description: Evidence interpretation, experimental-data analysis, and statistical verdicts. Load when the user asks to analyze results, interpret data, decide whether to kill/pivot/continue a direction, or evaluate numeric evidence. Delegates chart generation to result_visualization.
requires: research_manager
---

## Output Contract

- Label every claim as **fact** (with source) or **speculation** (explicitly marked, e.g. `[speculation]`). Never state speculation as fact — this is a hard red line.
- Plain language: conclusion first; explain any jargon in one short sentence on first use; no filler phrases or padding; prefer tables or lists when they aid scanning.

# Result Analysis — Interpret Evidence, Recommend Direction

`result_analysis` owns statistical analysis and evidence verdicts. It does not generate visual artifacts, mutate research state, or commit/merge.

## 0. Separate Value from Verdict

- **Experiment value**: `informative` | `reusable` | `none`
- **Direction verdict**: `inconclusive` | `continue` | `pivot` | `falsified` | `validated`

`inconclusive` is valid when evidence is inadequate; do not force a false verdict.

## 1. Adequacy Check

Before interpreting any data, answer:

1. What claim can this experiment support, challenge, or discriminate?
2. What metric or control would falsify or weaken that claim?
3. Does the evaluation setup satisfy (1) and (2)?

If not, fix the evaluation first. Do not draw conclusions from weak evidence.

## 2. Evidence Audit (Fact Layer)

Strip away interpretation. List facts with numbers and units. De-fuzzify vague words like "significant" by demanding a quantitative definition.

Audit:

- Observational unit and design (paired / repeated / independent)
- Missingness, dependence, sampling, and run-to-run randomness
- Descriptive statistics before inference
- Controls and baselines
- Sample size relative to the claim

## 3. Statistical Analysis

Choose tests or models from the design, not a fixed recipe. Report:

- Estimates and effect sizes
- Uncertainty intervals
- Assumptions and checks
- Multiple-comparison handling where applicable
- Practical vs. statistical significance

Avoid universal thresholds like `≥3 seeds` or variance rules; calibrate checks to the actual randomness source, design, effect size, and controls.

## 4. Competing Hypotheses and Confidence

Propose at least two mutually exclusive hypotheses with mechanism and falsification condition. Use qualitative confidence before/after unless a formal Bayesian model supports numeric priors/posteriors.

| Hypothesis | Confidence before | Evidence impact | Confidence after | Missing information |
|---|---|---|---|---|
| H1 | ... | +/- ... | ... | ... |

## 5. Verdict and Recommendation

Output:

- `retain` / `discard` recommendation for the run
- Checkpoint recommendation
- Next discriminating experiment (if `continue` or `inconclusive`)
- Lifecycle recommendation (`no-change`, `archive-as-*`, `promote`) for the manager/experiment manager

Hand the verdict to `experiment_manager` or `research_manager`; never write directly to `archive/`, move `project/` state, commit, or merge.

Supply the evidence and statistics sections of each run report and the final direction report; distinguish facts, estimates, uncertainty, interpretation, and verdict.

## 6. Visualization Handoff

Request a chart or evidence table only when it adds information beyond a compact textual result. The handoff must state: purpose, source data/version, observational unit, variables, grouping/faceting, summary operation, valid uncertainty representation, target claim, and artifact class. Then delegate generation to `result_visualization`.

## Output Constraints

- No cheap affirmations.
- No unexamined causal claims.
- Distinguish fact, inference, speculation, and excluded evidence.
- File writes only after user confirmation.
- End each session by proposing what to archive, delete, or merge.
