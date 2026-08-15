---
name: result_analysis
description: Evidence interpretation, baseline-expected-actual comparison, mechanism diagnosis, and statistical verdicts. Load when the user asks to analyze results, interpret data, decide whether to kill/pivot/continue a direction, or evaluate numeric evidence. Locates which causal link failed, enforces convergence accounting, and delegates chart generation to result_visualization.
requires: research_manager
---

## Output Contract

- 先说结论，再给必要依据和下一步。
- 默认短句和常用词；术语只在更准确时用，首次出现直接解释。
- 内部状态、流程和检查表默认不展示；只有影响决定或用户明确要求时才展开。
- 外部事实、论文结论和数字附来源；不确定的直接写"尚未验证"或"我推测"，不给每句话机械加 fact/speculation 标签。
- 一段能说清就不用表格；独立要点用列表；只有横向比较才用表格。
- 不写套话、廉价肯定、重复总结和固定收尾。

# Result Analysis — Locate the Broken Link, Converge the Ledger

`result_analysis` owns statistical analysis and evidence verdicts. It does not generate visual artifacts, mutate research state, or commit/merge.

## 0. Separate Value from Verdict

- **Experiment value**: `informative` | `reusable` | `none`
- **Direction verdict**: `inconclusive` | `continue` | `pivot` | `falsified` | `validated`

`inconclusive` is valid when evidence is inadequate; do not force a false verdict.

Progress means: an explanation eliminated, a key uncertainty reduced, a causal link located, or a decision boundary clarified. **More observations, more phenomena, or more new ideas are not progress by themselves.** An experiment that raises five questions but closes the core hypothesis is convergent; one that produces many observations but changes no judgment is not.

## 1. Adequacy Check

Before interpreting any data, answer:

1. What claim can this experiment support, challenge, or discriminate?
2. What metric or control would falsify or weaken that claim?
3. Does the evaluation setup satisfy (1) and (2)?

If not, fix the evaluation first. Do not draw conclusions from weak evidence.

## 2. Pre-Registered Expectation

Before inspecting actual outcomes, recover the experiment-time record of: baseline metric and uncertainty; expected metric range; expected mechanism, causal link, and observable intermediate signals; alternative explanations and the measurements intended to distinguish them; the **main contradiction** the run targets.

If these were not recorded before the run, mark the expectation as post hoc and lower the evidential weight of any apparent confirmation. Do not rewrite the expected result to fit the actual result.

## 3. Evidence Audit (Fact Layer)

Strip away interpretation. List facts with numbers and units. De-fuzzify vague words like "significant" by demanding a quantitative definition.

Audit: observational unit and design (paired / repeated / independent); missingness, dependence, sampling, run-to-run randomness; descriptive statistics before inference; controls drawn from the anchor set rather than weak competitors, with protocol comparability justified; sample size relative to the claim; intermediate measurements relevant to the mechanism, not only the final score.

## 4. Baseline / Expected / Actual Analysis

For every primary metric and important diagnostic, make the three-way comparison explicit:

| Quantity | Baseline | Expected | Actual | Deviation | Interpretation |
|---|---:|---:|---:|---:|---|

Then **locate which link of the registered causal chain failed**, in order:

| Link | Question | Action if broken |
|---|---|---|
| Experiment validity | Did implementation, data, or evaluation make the run invalid? | Fix the experiment; do not update the hypothesis |
| Intervention | Did change A actually produce the predicted intermediate signal? | Redesign or fix A, not the theory |
| Mechanism | The signal appeared — did it translate to the target capability? | Revise the mechanism hypothesis |
| Goal | Does the metric change correspond to the real research goal? | Fix the evaluation or the question |
| Value | Even if true, is the effect large enough to support the claim? | Continue, downgrade, or stop |

Only the first link permits prioritizing local engineering fixes. All other links route back to the main hypothesis. **Do not replace the main contradiction with a local anomaly** (an odd layer, a failing subgroup, an unstable loss term) unless evidence shows it explains the primary deviation or blocks the core chain. Otherwise it goes to the parking lot.

## 5. Statistical Analysis

Choose tests or models from the design, not a fixed recipe. Report: estimates and effect sizes; uncertainty intervals; assumptions and checks; multiple-comparison handling where applicable; practical vs. statistical significance.

Avoid universal thresholds like `≥3 seeds` or variance rules; calibrate checks to the actual randomness source, design, effect size, and controls.

## 6. Competing Hypotheses and Convergence Ledger

Propose at most 2–3 mutually exclusive hypotheses with mechanism and falsification condition — never an open-ended list. Then produce the convergence ledger:

| Item | Before run | After run |
|---|---|---|
| Primary hypothesis | ... | supported / weakened / untested |
| Active explanations | N | fewer, or justify why not |
| Dominant uncertainty | ... | resolved; new dominant one is ... |
| Main contradiction | ... | updated to ... |
| Parked new questions | ... | recorded, not auto-activated |
| Next decision | unknown | continue / pivot / stop / invalid |

Rules: the next experiment must shrink the explanation set, not the component count; new ideas default to the parking lot and only interrupt the main line if they invalidate the current question or change the decision; two consecutive rounds without reducing a decision-relevant uncertainty → stop the sequence and re-review the question itself; no "tweak and see" iterations without a named mechanism update.

## 7. Failure Diagnosis and Next Experiment

When actual results miss the expected range, produce a failure table:

| Candidate explanation | Supporting evidence | Contradicting evidence | Confidence | Discriminating next test |
|---|---|---|---|---|

Do not write "the direction does not work" from a surface metric alone. A useful next experiment targets the highest-impact unresolved explanation, alters one discriminating factor, and states the new expected mechanism and result before running. If no plausible explanation is cheaply testable or no mechanism-level prediction survives, recommend stopping or pivoting with the evidence boundary stated plainly.

## 8. Verdict and Recommendation

Output: `retain`/`discard` recommendation for the run; checkpoint recommendation; next discriminating experiment (if `continue` or `inconclusive`); lifecycle recommendation (`no-change`, `archive-as-*`, `promote`).

Hand the verdict to `experiment_manager` or `research_manager`; never write directly to `archive/`, move `project/` state, commit, or merge. Supply the evidence and statistics sections of each run report and the final direction report; distinguish facts, estimates, uncertainty, interpretation, and verdict.

## 9. Mandatory Visual Audit

For every run report and final report, run a visual-needs audit before writing — skipping the audit is not allowed, though its outcome may be "text suffices":

| Information type | Default encoding |
|---|---|
| Method/module structure | architecture or flow diagram |
| Where the implementation chain still relies on speculation | risk-chain diagram |
| Difference vs. closest work | alignment matrix or structural contrast |
| Multi-group numeric comparison | dot plot / distribution / small multiples |
| Baseline–expected–actual | interval comparison chart |
| How runs changed judgments over time | timeline or decision trajectory |
| Where failures occur | failure-case panel or mechanism diagnostic |
| Two or three trivial numbers | compact table, no forced chart |

Record in the report: figure candidates considered, selected, and rejected with reasons. Hand each selected figure to `result_visualization` with: purpose, source data/version, observational unit, variables, grouping/faceting, summary operation, valid uncertainty representation, target claim, artifact class. Do not alter the statistical claim in the handoff.

## Output Constraints

- No cheap affirmations. No unexamined causal claims.
- Distinguish fact, inference, speculation, and excluded evidence.
- File writes only after user confirmation.
- Propose cleanup only on concrete stale or duplicate content.
