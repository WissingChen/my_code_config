---
name: result_analysis
description: Evidence interpretation, experimental-data analysis, and statistical verdicts. Load when the user asks to analyze results, interpret data, decide whether to kill/pivot/continue a direction, or evaluate numeric evidence. Delegates chart generation to result_visualization.
requires: research_manager
---

## Output Contract

- 先说结论，再给必要依据和下一步。
- 默认短句和常用词；术语只在更准确时用，首次出现直接解释。
- 内部状态、流程和检查表默认不展示；只有影响决定或用户明确要求时才展开。
- 外部事实、论文结论和数字附来源；不确定的直接写"尚未验证"或"我推测"，不给每句话机械加 fact/speculation 标签。
- 一段能说清就不用表格；独立要点用列表；只有横向比较才用表格。
- 不写套话、廉价肯定、重复总结和固定收尾。

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
- Controls and baselines: are they drawn from the strongest credible work (the anchor set), or only from weak competitors that are easy to beat? Is the evaluation protocol comparable to the anchor's; if not, is the difference justified?
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
- Propose cleanup (archive/delete/merge) only when concrete stale or duplicate content is found — not as a fixed sign-off.
