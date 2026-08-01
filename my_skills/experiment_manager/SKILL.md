---
name: experiment_manager
description: Direction-level experiment execution and artifact workflow. Load when a user starts, runs, checkpoints, or closes experiments. Delegates evidence interpretation to result_analysis and visualization to result_visualization; owns branch/worktree lifecycle, run reports, output hygiene, and promotion.
requires: research_manager
---

## Output Contract

- 先说结论，再给必要依据和下一步。
- 默认短句和常用词；术语只在更准确时用，首次出现直接解释。
- 内部状态、流程和检查表默认不展示；只有影响决定或用户明确要求时才展开。
- 外部事实、论文结论和数字附来源；不确定的直接写"尚未验证"或"我推测"，不给每句话机械加 fact/speculation 标签。
- 一段能说清就不用表格；独立要点用列表；只有横向比较才用表格。
- 不写套话、廉价肯定、重复总结和固定收尾。

# Experiment Manager

`experiment_manager` operates the experiment branch, assembles reports, and enforces output hygiene. It does not interpret evidence or render visuals.

Git commits, branch deletion, merges, and other lifecycle mutations require explicit user authorization.

## 1. Open a Direction

Require a ready proposal containing: question, hypothesis, falsifiable prediction, kill criteria, promotion criteria, minimum viable experiment, controls, output-retention policy, anchor set, and minimum quality bar (including the strong baselines that must be compared against).

Record: `base_branch`, `base_commit`, direction ID, branch name (`exp/NN-slug`), and worktree path. Create the branch; prefer a dedicated worktree so untracked outputs cannot leak across branches. Move the direction from `proposal/` to `project/` only within the experiment branch.

## 2. Run Loop

Give each run an `ENN` ID. Change one controlled factor where feasible.

Delegate evidence interpretation to `result_analysis` and visuals to `result_visualization`. Before the value gate, produce one illustrated `ENN-experiment-report.md` (schema in §4).

Classify value separately from direction outcome:

| Experiment value | Meaning | Action |
|---|---|---|
| `informative` | Materially updates hypothesis or next decision | Atomic checkpoint |
| `reusable` | Yields direction-independent verified asset | Atomic checkpoint |
| `none` | Invalid, redundant, or decision-neutral | Record exclusion; clean outputs |

For `none`, do not commit the run report. Record its ID and reason in the direction report's excluded-runs table, remove only its outputs, and restore to the latest valuable checkpoint using non-destructive, user-authorized Git operations.

## 3. Output Hygiene

Maintain a retention whitelist from the first run. Allow in Git: small decision tables, minimal configurations, analysis scripts, and final figures. Exclude: checkpoints, caches, dataset copies, full logs, prediction dumps, temporary figures, intermediate features, and reproducible bulk outputs.

Valuable large artifacts live externally. Track in a manifest: `uri`, `checksum`, `producer_commit`, `retention_reason`, and expiry/review date. Clean disposable outputs after every run; never rely on branch deletion to remove committed large objects.

## 4. Run Report Schema

Every completed `ENN` run produces `ENN-experiment-report.md` containing:

- Question and experiment ID
- Base commit and controlled change
- Setup, data, controls, and reproducibility parameters
- Data-quality and adequacy audit
- Key results table
- Selected diagnostic/evidence charts with captions
- Statistical analysis and uncertainty
- Fact / inference / speculation
- Experiment value: `informative` | `reusable` | `none`
- Direction verdict and next action
- Retain/discard manifest

The report is the input to the value gate. Informative/reusable reports enter an atomic checkpoint.

## 5. Close as Falsified

Synthesize valuable run reports into one illustrated `REPORT.md` containing:

- Executive conclusion
- Original question, hypothesis, and decision thresholds
- Experiment map and traceability table
- Methods and evaluation design
- Results with selected tables and figures
- Statistical analysis
- Competing explanations and failure analysis
- Excluded/invalid runs and reasons
- Final verdict and evidence boundary
- Revised belief, reusable findings, and limitations
- Code/artifact provenance and retention status
- Replacement path

Report bundle: `REPORT.md`, `SUMMARY.md` pointer, `figures/` (selected evidence figures only), `data/` (compact source tables only), `scripts/` (minimal plotting source when required for reproducibility). Remove duplicate previews, diagnostics, intermediate renderings, and exploratory implementation.

Before finalizing, verify: every headline conclusion points to a table, figure, or explicit numeric result; every retained visual is referenced in the text with uncertainty semantics; the report distinguishes facts, inference, speculation, and excluded evidence; provenance points to base and experiment commits that survive branch deletion.

Apply only the final report bundle plus index transition to the recorded base branch; do not merge or cherry-pick exploratory code. When authorized, delete the experiment branch/worktree and disposable external artifacts.

## 6. Close as Validated

Create `promote/NN-slug` from the target base. Synthesize the same illustrated final report with promotion criteria, validated scope, key evidence, limitations, and traceability to retained experiment IDs. The report must state, in plain terms: what we achieved relative to the anchor set, where we still fall short of the minimum quality bar, and what level of claim the current results can support. Selectively apply only effective implementation, required tests, minimal configuration, and the report bundle. Exclude superseded variants, debug helpers, temporary scripts, exploratory abstractions, and intermediate outputs. Review the promotion diff independently; merge the promotion branch, never `exp/NN-slug` directly. Close the experiment branch/worktree after promotion is verified.

## 7. Pivot

Archive the old core hypothesis as `superseded` and create a new proposal ID when the research question changes materially. Do not silently mutate project history.

## 8. Extract Reusable Fixes

Promote direction-independent bug fixes through a separate clean fix branch with tests, even if the research direction is later falsified.

## 9. Report Assembly and Cross-Skill Contracts

| Report component | Owner |
|---|---|
| Run metadata, provenance, retain/discard manifest, branch traceability | `experiment_manager` |
| Adequacy audit, statistics, interpretation, experiment value, direction verdict | `result_analysis` |
| Tables, charts, qualitative panels, process diagrams, visual validation | `result_visualization` |
| Final Markdown hierarchy and renderer-aware readability pass | `write_md` |
| State transition, archive index, `SUMMARY.md` pointer | `research_manager` |

Standard outputs: `Proposal readiness: rejected | evaluating | ready`; `Experiment value: informative | reusable | none`; `Direction verdict: inconclusive | continue | pivot | falsified | validated`; `Lifecycle recommendation: no-change | activate | archive-as-* | promote`; `Visual artifact class: diagnostic | evidence | explanatory`; `Visual retention: discard-after-run | retain-with-checkpoint | retain-with-final-record`.

`experiment_manager` orchestrates report assembly and verifies all required sections before checkpointing or closing. No skill may silently rewrite another skill's scientific judgment.
