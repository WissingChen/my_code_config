---
name: experiment_manager
description: Direction-level experiment execution, expectation tracking, and artifact workflow. Load when a user starts, runs, checkpoints, or closes experiments. Requires a registered main contradiction per run, enforces convergence accounting, assembles reports with verified visuals, and owns branch/worktree lifecycle, output hygiene, and promotion.
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

Require a ready proposal containing: question, hypothesis, falsifiable prediction, mechanism hypothesis with observable intermediate signals, baseline result and uncertainty, expected result range, kill criteria, promotion criteria, minimum viable experiment, controls, output-retention policy, anchor set, minimum quality bar (including the strong baselines that must be compared against), **the direction's current main contradiction, and a speculation ledger**. Expected results and mechanisms must be recorded before running the experiment; do not infer the prediction after seeing the result.

Record: `base_branch`, `base_commit`, direction ID, branch name (`exp/NN-slug`), and worktree path. Create the branch; prefer a dedicated worktree so untracked outputs cannot leak across branches. Move the direction from `proposal/` to `project/` only within the experiment branch.

## 2. Run Loop

Give each run an `ENN` ID. Each run must bind **one primary hypothesis and the current main contradiction**. Change one controlled factor where feasible. Before execution, freeze: baseline, expected result range, expected intermediate signals, the causal chain connecting intervention to outcome, and the outcome→action branches (result A/B/ambiguous each map to a named action).

Reject a run request that states no decision it would change, or that tunes peripheral details while the core implementation chain remains unclosed. New ideas surfacing mid-loop go to the direction's parking-lot list; they never auto-activate.

Delegate evidence interpretation to `result_analysis` and visuals to `result_visualization`. Before the value gate, produce one illustrated `ENN-experiment-report.md` (schema in §4). **A long report is not complete until the visual audit was executed and every selected figure was produced, embedded, and render-verified** (§4a).

Classify value separately from direction outcome:

| Experiment value | Meaning | Action |
|---|---|---|
| `informative` | Materially updates hypothesis or next decision | Atomic checkpoint |
| `reusable` | Yields direction-independent verified asset | Atomic checkpoint |
| `none` | Invalid, redundant, or decision-neutral | Record exclusion; clean outputs |

For `none`, do not commit the run report. Record its ID and reason in the direction report's excluded-runs table, remove only its outputs, and restore to the latest valuable checkpoint using non-destructive, user-authorized Git operations.

After each run, carry the convergence ledger (from `result_analysis` §6) into the direction `00-overview.md`: active explanations, dominant uncertainty, main contradiction, parked questions, next decision. If two consecutive runs fail to reduce a decision-relevant uncertainty, halt the run sequence and send the direction back to `research_progress` for re-scoping.

## 3. Output Hygiene

Maintain a retention whitelist from the first run. Allow in Git: small decision tables, minimal configurations, analysis scripts, and final figures. Exclude: checkpoints, caches, dataset copies, full logs, prediction dumps, temporary figures, intermediate features, and reproducible bulk outputs.

Valuable large artifacts live externally. Track in a manifest: `uri`, `checksum`, `producer_commit`, `retention_reason`, and expiry/review date. Clean disposable outputs after every run; never rely on branch deletion to remove committed large objects.

## 4. Run Report Schema

Every completed `ENN` run produces `ENN-experiment-report.md` containing:

- Question, experiment ID, and the main contradiction targeted
- Base commit and controlled change
- Setup, data, controls, and reproducibility parameters
- Data-quality and adequacy audit
- Baseline / expected / actual results table, with uncertainty and the pre-registered expectation for every primary metric
- Mechanism prediction versus observed intermediate signals, and which causal link held or broke
- Selected diagnostic/evidence charts with captions
- Statistical analysis and uncertainty
- Deviation and failure-mechanism analysis: for every missed expectation, enumerate plausible causes, evidence for and against each, and the next discriminating test
- Convergence ledger (before/after) and parked-questions list
- Fact / inference / speculation
- Experiment value: `informative` | `reusable` | `none`
- Direction verdict and next action
- Visual manifest and retain/discard manifest

## 4a. Visual Acceptance Checklist

Before a run or final report counts as complete:

- The visual audit (from `result_analysis` §9) is recorded: candidates considered, selected, rejected with reasons.
- Every selected figure was actually delegated to and produced by `result_visualization` — data charts keep reproducible `.py` source, vector `.svg/.pdf`, and `.png` preview as one artifact bundle.
- Markdown actually references each figure file; links resolve; the figure renders (open or screenshot-check, no broken paths).
- Captions state comparison, observational unit, uncertainty semantics, and takeaway.
- No full-screen text walls in long reports; when no figure was selected, the reason "text/table is more accurate" is on record.

## 5. Close as Falsified

Synthesize valuable run reports into one illustrated `REPORT.md` containing: executive conclusion; original question, hypothesis, decision thresholds, and main contradiction; experiment map and traceability table; methods and evaluation design; results with selected tables and figures; statistical analysis; integrated baseline / expected / actual comparison and mechanism-based failure analysis; competing explanations and failure analysis; excluded/invalid runs and reasons; final verdict and evidence boundary; revised belief, reusable findings, and limitations; code/artifact provenance and retention status; replacement path.

Report bundle: `REPORT.md`, `SUMMARY.md` pointer, `figures/` (selected evidence figures only), `data/` (compact source tables only), `scripts/` (minimal plotting source when required for reproducibility). Remove duplicate previews, diagnostics, intermediate renderings, and exploratory implementation.

Before finalizing, verify: every headline conclusion points to a table, figure, or explicit numeric result; every retained visual is referenced in the text with uncertainty semantics; the report distinguishes facts, inference, speculation, and excluded evidence; the §4a visual checklist passed; provenance points to base and experiment commits that survive branch deletion.

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
| Run metadata, provenance, manifests, visual acceptance check, branch traceability | `experiment_manager` |
| Adequacy audit, statistics, causal-link diagnosis, convergence ledger, experiment value, direction verdict | `result_analysis` |
| Tables, charts, qualitative panels, process/risk/decision diagrams, visual validation | `result_visualization` |
| Visual placement plan (pre-figure pass) and final Markdown readability pass | `write_md` |
| State transition, archive index, `SUMMARY.md` pointer | `research_manager` |

Standard outputs: `Proposal readiness: rejected | blocked | evaluating | ready`; `Experiment value: informative | reusable | none`; `Direction verdict: inconclusive | continue | pivot | falsified | validated`; `Lifecycle recommendation: no-change | activate | archive-as-* | promote`; `Visual artifact class: diagnostic | evidence | explanatory`; `Visual retention: discard-after-run | retain-with-checkpoint | retain-with-final-record`.

`experiment_manager` orchestrates report assembly and verifies all required sections before checkpointing or closing. No skill may silently rewrite another skill's scientific judgment.
