# Research Skill Family Refactor Plan

## Goal

Unify the research skill family around one lifecycle contract, separate research-state ownership from experiment execution and result visualization, and prevent exploratory code and generated outputs from accumulating on the main branch.

## Fixed Decisions

- Keep the existing four research directories: `proposal/`, `project/`, `archive/`, and `knowledge/`.
- Add `experiment_manager` instead of expanding `research_manager` into Git and artifact operations.
- Restore visualization as an independent `result_visualization` skill; keep statistical inference in `result_analysis` and visual encoding in `result_visualization`.
- Treat one research direction as one stable `NN-slug/` directory and one direction-level `exp/NN-slug` branch.
- A direction remains in `proposal/` after the three research gates until the user explicitly starts experiments.
- Creating the experiment branch is the promotion event from proposal to active project.
- Judge each experiment by information or reuse value, not by whether the metric improved.
- Never merge an experiment branch directly.
- Every completed experiment produces a self-contained illustrated run report before its value is judged.
- Every closed direction produces a synthesized illustrated final report as its primary research deliverable.
- A falsified direction returns the final report and its minimal evidence assets to the base branch, but no exploratory implementation.
- A validated direction returns the final report, minimal evidence assets, effective implementation, tests, and minimal configuration through a clean promotion branch.
- Large outputs stay outside Git; Git stores only a manifest with URI, checksum, purpose, and retention policy.
- Classify every visual artifact as `diagnostic`, `evidence`, or `explanatory`; only the latter two are candidates for durable retention.
- Git commits, branch deletion, merges, and other lifecycle mutations still require explicit user authorization.

## Canonical Lifecycle

| State | Location | Owner | Transition |
|---|---|---|---|
| Evaluating | `proposal/NN-slug/` | `research_progress` recommends | Pass or fail the three gates |
| Ready | `proposal/NN-slug/` | `research_manager` records | Explicit user GO starts experiments |
| Active | `project/NN-slug/` on `exp/NN-slug` | `experiment_manager` operates | Continue, pivot, falsify, or validate |
| Rejected | `archive/YYYY-MM-DD-NN-slug/` | `research_manager` applies | Proposal fails before experiments |
| Falsified | `archive/YYYY-MM-DD-NN-slug/` | `research_manager` applies | Registered prediction is reliably contradicted |
| Validated | promoted code plus archived evidence | `experiment_manager` promotes; manager records | Promotion criteria are met |
| Superseded | archived old direction plus new proposal | manager applies | Core question or hypothesis changes |
| Abandoned | archive with non-scientific stop reason | manager applies | Resource or priority stop |

`research_manager` owns directory and research-state transitions. `research_progress` recommends admission. `result_analysis` owns statistical analysis and recommends evidence/direction verdicts. `result_visualization` owns charts, evidence tables, and diagrams without strengthening the underlying claim. `experiment_manager` executes the authorized Git and artifact workflow. Writing skills never change scientific state.

## File Changes

### 1. Add `my_skills/experiment_manager/SKILL.md`

Define a direction-level experiment workflow:

1. **Open**
   - Require a ready proposal with hypothesis, falsifiable prediction, kill criteria, promotion criteria, minimum viable experiment, controls, and output-retention policy.
   - Record `base_branch`, `base_commit`, direction ID, branch name, and worktree path.
   - Create `exp/NN-slug`; recommend a dedicated worktree so untracked outputs cannot leak across branches.
   - Move the direction from `proposal/` to `project/` only within the experiment branch.

2. **Run loop**
   - Give each run an `ENN` ID and change one controlled factor where feasible.
   - Delegate evidence interpretation to `result_analysis`.
   - Generate one illustrated `ENN-experiment-report.md` before the value gate. The report combines setup, key tables/charts, statistical analysis, interpretation, limitations, and the run decision instead of leaving these as scattered outputs.
   - Classify experiment value separately from direction outcome:
     - `informative`: materially updates a hypothesis or next decision;
     - `reusable`: yields a direction-independent verified engineering asset;
     - `none`: invalid, redundant, or decision-neutral.
   - Commit only informative or reusable experiments, using one atomic checkpoint containing minimal code/configuration, the run report, and its selected evidence assets.
   - For `none`, do not commit the run report or outputs as a standalone checkpoint. Record its ID and exclusion reason in the direction report's excluded-runs table, then remove only outputs created by that run and restore to the latest valuable checkpoint using non-destructive, user-authorized Git operations.

3. **Output hygiene**
   - Maintain a retention whitelist from the first run rather than cleaning only at final archive time.
   - Allow small decision-relevant tables, minimal configurations, analysis scripts, and final figures in Git.
   - Exclude checkpoints, caches, dataset copies, full logs, prediction dumps, temporary figures, intermediate features, and reproducible bulk outputs.
   - Store valuable large artifacts externally and track `uri`, `checksum`, `producer_commit`, `retention_reason`, and expiry/review date in a manifest.
   - Clean disposable outputs after every run; never rely on branch deletion to remove committed large Git objects.

4. **Close as falsified**
   - Synthesize the valuable run reports into one illustrated final `REPORT.md` containing hypothesis, kill criterion, experiment map, statistical evidence, key charts/tables, failure diagnosis, conclusion, revised belief, limitations, base commit, and replacement path.
   - Preserve a minimal report bundle: `REPORT.md`, selected evidence figures, compact source tables, and report-specific plotting source when required for reproducibility. Remove duplicate previews, diagnostics, intermediate renderings, and exploratory implementation.
   - Represent invalid/redundant runs in a compact excluded-runs table with reason; do not silently omit them or retain their full artifacts.
   - Apply only the final report bundle plus summary/index transition back to the recorded base branch; do not merge or cherry-pick exploratory model/method implementation.
   - Close and, when authorized, delete the experiment branch/worktree and disposable external artifacts.

5. **Close as validated**
   - Create `promote/NN-slug` from the current target branch.
   - Synthesize the direction into the same illustrated final report used for falsified directions, with promotion criteria, validated scope, key evidence, limitations, and traceability to retained experiment IDs.
   - Selectively reconstruct or apply only the effective implementation, required tests, minimal configuration, final report, and minimal report assets.
   - Exclude superseded variants, debug helpers, temporary scripts, exploratory abstractions, and intermediate outputs.
   - Review the promotion diff independently; merge the promotion branch, never `exp/NN-slug` directly.
   - Close the experiment branch/worktree after promotion is verified.

6. **Extract reusable fixes**
   - Promote direction-independent bug fixes through a separate clean fix branch with tests, even if the research direction is later falsified.

Keep the skill procedural and compact. Put the experiment-record and artifact-manifest schemas in one small reference file only if `SKILL.md` would otherwise exceed the document budget.

### 2. Refactor `my_skills/research_manager/SKILL.md`

- Replace vague directory comments with the canonical state meanings.
- Define `NN-slug/` as the stable direction unit; preserve its ID across moves.
- State naming precedence and exceptions for `global.md`, `00-overview.md`, `SUMMARY.md`, literature notes, and dated archive directories.
- Separate mandatory direction-level `00-overview.md` from optional collection-level overviews created after more than five entries.
- Replace the fixed “project only” archive rule with rejected, falsified, validated/completed, superseded, and abandoned outcomes. Closed active directions require an illustrated `REPORT.md`; keep `SUMMARY.md` only as a short outcome/index pointer rather than duplicating the report.
- Make manager the sole owner of directory moves, archive naming, `SUMMARY.md`, and `global.md` pointer updates.
- Add delegation to `experiment_manager` for experiment startup, Git operations, promotion, branch closure, and output cleanup.
- Narrow the 150-line budget to human-maintained operational research documents; exempt manuscripts, generated reports/data, code, bibliographies, and indivisible tables.
- Clarify read discipline: read the pointer layer and target direction overview first, then only the files linked for the current task.
- Centralize cleanup policy: propose archive/delete/merge only when concrete stale content is found; preserve raw scientific evidence unless its retention policy allows deletion.

### 3. Refactor `my_skills/research_progress/SKILL.md`

- Keep the three gates, but return `rejected`, `evaluating`, or `ready`; do not move directories or start experiments.
- Replace fixed `proposal/04-milestones.md` with a direction-relative hypothesis/experiment-plan path.
- Define readiness as: question, scoped literature gap, hypothesis, falsifiable prediction, kill criterion, promotion criterion, minimum viable experiment, controls, feasibility, and artifact-retention plan.
- Record literature query date, source, terms, filters, nearest work, and uncovered sources.
- Replace absolute “no directly relevant work found” with a scoped statement tied to recorded searches.
- Call saved literature items “knowledge notes,” not archived papers.
- Hand ready proposals to `experiment_manager`, not directly to `result_analysis`.

### 4. Refactor `my_skills/result_analysis/SKILL.md`

- Separate `Experiment value` (`informative`, `reusable`, `none`) from `Direction verdict` (`inconclusive`, `continue`, `pivot`, `falsified`, `validated`).
- Add `inconclusive` so inadequate evidence does not force a false Kill/Pivot/Continue decision.
- Replace “what can this prove” with what the experiment can support, challenge, or discriminate.
- Replace universal seed and variance thresholds with checks appropriate to the actual randomness source, design, effect size, uncertainty interval, controls, sample size, and practical significance.
- Make statistical analysis an explicit responsibility:
  - identify the observational unit and paired/repeated/independent design;
  - audit missingness, dependence, sampling and run-to-run randomness;
  - report descriptive statistics before inference;
  - choose tests or models from the design rather than from a fixed recipe;
  - report estimates, effect sizes, uncertainty intervals, assumptions, and multiple-comparison handling where applicable;
  - distinguish statistical detectability from practical or scientific importance.
- Use qualitative confidence before/after unless a formal Bayesian model supports numeric priors/posteriors.
- Output explicit `retain`, `discard`, checkpoint recommendation, next discriminating experiment, and lifecycle recommendation.
- Supply the evidence/statistics sections of each run report and the final direction report; distinguish facts, estimates, uncertainty, interpretation, and verdict.
- Never write directly to `archive/`, move project state, commit, or merge; hand recommendations to manager/experiment manager.
- Produce a visualization handoff only when a chart or evidence table adds information beyond a compact textual result. The handoff must state purpose, source data, observational unit, variables, grouping/faceting, summary operation, valid uncertainty representation, target claim, and artifact class.
- Delegate chart generation to `result_visualization`; do not mix plotting implementation into the evidence verdict workflow.

### 5. Add `my_skills/result_visualization/SKILL.md`

Give visualization its own trigger and three modes:

1. **Data chart and evidence table**
   - Accept raw/tabular data or a handoff from `result_analysis`.
   - Validate data shape, observational unit, aggregation, missing values, and available uncertainty before plotting.
   - Select the visual form from the analytical question: distributions, paired changes, trends, comparisons, relationships, calibration, sensitivity, or ablations.
   - Allow descriptive transformations required to draw the chart, but delegate hypothesis tests, inferential models, and scientific verdicts to `result_analysis`.
   - Prefer showing distributions/raw points when feasible; do not hide heterogeneity behind aggregate bars.
   - Do not invent error bars, confidence intervals, significance markers, missing values, or sample sizes.
   - Use compact tables instead of charts when the data are trivial or a figure adds no information.

2. **Process and architecture diagrams**
   - Handle Mermaid flowcharts, state diagrams, sequence diagrams, architecture diagrams, ER diagrams, and timelines without invoking statistical analysis.
   - Require a clear purpose, entities/states, relationships/transitions, and target renderer.
   - Keep one diagram focused; split diagrams that exceed a readable node/edge budget.
   - Use Mermaid for standard semantics; use another repository-supported source format only when Mermaid cannot express the required layout.

3. **Figure production and validation**
   - Generate reproducible source plus the minimum required outputs: PDF/SVG for durable vector use, PNG only when a preview or raster target is actually needed.
   - Check axis labels and units, scale and baseline choices, legend, ordering, uncertainty semantics, colorblind/grayscale readability, font availability, clipping, and caption self-containment.
   - Reject misleading defaults: unlabelled truncated axes, dual axes without strong justification, 3D decoration, rainbow maps, pie charts as the default comparison, and significance decoration unsupported by the analysis.
   - Treat script/source and rendered outputs sharing one prefix as one artifact bundle.

Define visual artifact lifecycle:

| Class | Purpose | Default retention |
|---|---|---|
| `diagnostic` | Debugging, data-quality checks, exploratory inspection | Do not commit; clean after the run |
| `evidence` | Supports an experiment-value or direction verdict | Retain with a valuable run report; select the minimum needed for the final report |
| `explanatory` | Communicates a stable process, architecture, or manuscript claim | Retain only for a current promoted system or claim |

The skill must label every generated artifact with its class and hand the retention recommendation to `experiment_manager`. A visually polished figure is not automatically valuable evidence. Both validated and falsified directions may retain selected visuals when they materially support the final report; report assets are curated evidence, not a dump of all generated figures.

### 6. Move and revise the plotting reference

- Move `my_skills/result_analysis/plotting-reference.md` to `my_skills/result_visualization/plotting-reference.md` so implementation guidance follows its owner.
- Expand chart selection beyond generic library calls to match data design: paired points/lines, distributions, uncertainty intervals, small multiples, calibration and sensitivity plots.
- Remove pie charts as the default composition recommendation.
- Warn that seaborn confidence intervals require suitable raw observations and an appropriate resampling unit; do not synthesize uncertainty from aggregate rows or pseudo-replicates.
- Detect available fonts instead of assuming `SimHei`.
- Save into the active direction or user-specified location, not unconditionally under `project/`.
- Treat script/PDF/PNG sharing one prefix as one artifact bundle.
- Update a direction overview for retained figures; never register disposable diagnostics. Update a collection overview only when that overview exists.
- Require the plotting source to record input path/version and relevant transformation so retained figures are reproducible.
- Produce report-ready captions that state the comparison, observational unit, uncertainty semantics, and takeaway without overstating the analysis.

### 7. Align `my_skills/write_md/SKILL.md`

- Keep it presentation-only; remove research-file archive/merge advice.
- Make formatting renderer-aware:
  - GitHub: plain Markdown, blockquotes, or supported alerts;
  - raw HTML boxes only when the target renderer permits inline styles and nested content;
  - manuscripts: no UI-style boxes by default.
- Delegate charts and standard diagrams to `result_visualization`; keep `write_md` responsible only for document language, hierarchy, and renderer-aware presentation.
- Apply a final report readability pass after scientific content and visuals are fixed: conclusion-first structure, consistent terminology, figure/table callouts, caption placement, and a 30-second scan path. Do not alter statistical claims or retention decisions.

### 8. Align `my_skills/academic-paper-writing/SKILL.md`

- Add an evidence ceiling: prose may clarify but cannot strengthen claims beyond audited evidence.
- Remove universal `<1%`, `90% of gain`, sharp-peak, and p-value-only rules; require domain-appropriate effect size and uncertainty.
- Draft claims only from promoted implementations and retained evidence records, not by selecting attractive runs from experiment branches.
- Require traceability from manuscript result claims to experiment IDs and retained artifacts.
- Delegate paper figure production and visual checks to `result_visualization`; the paper skill decides narrative placement and caption argument, not statistical encoding.
- Keep narrative guidance, but remove language encouraging drama or inevitability when evidence is ambiguous.
- Declare manuscript storage: active direction `manuscript/` or an external repository linked from the direction overview.

### 9. Rewrite `my_skills/00-overview.md`

- List all seven skills and their single responsibilities.
- Replace the linear pipeline with the canonical lifecycle and experiment loop.
- Update the delegation and cross-reference matrices for `experiment_manager` and `result_visualization`.
- Replace hard-coded `proposal/04-milestones.md` paths.
- Change “analysis must produce a plot” to “plot when it materially improves interpretation.”
- Add three governing rules:
  1. Manager owns research state.
  2. Experiment value, not success, determines checkpoints.
  3. Experiment branches are never merged directly.
- Document the visualization boundary: analysis determines what the numbers support; visualization determines how to encode it without distortion; experiment management determines whether the artifact is retained.
- Update `last_updated` with the implementation date.

## Cross-Skill Contracts

Standardize these outputs so skills can hand off without duplicating authority:

```text
Proposal readiness: rejected | evaluating | ready
Experiment value: informative | reusable | none
Direction verdict: inconclusive | continue | pivot | falsified | validated
Lifecycle recommendation: no-change | activate | archive-as-* | promote
Lifecycle execution: research_manager / experiment_manager only
Visual artifact class: diagnostic | evidence | explanatory
Visual retention: discard-after-run | retain-with-checkpoint | retain-with-final-record
```

Standardize the analysis-to-visualization handoff:

```text
Purpose/question
Source data and version
Observational unit and study design
Variables, groups, facets, and ordering
Summary/transformation
Uncertainty representation supported by the data
Claim or comparison the visual may communicate
Target medium and renderer
Artifact class and retention recommendation
```

## Canonical Experiment Reports

Use reporting at two levels without preserving every exploratory artifact permanently.

Report assembly is a cross-skill contract rather than a new catch-all responsibility:

| Report component | Owner |
|---|---|
| Run metadata, provenance, retain/discard manifest, branch traceability | `experiment_manager` |
| Adequacy audit, statistics, interpretation, experiment value, direction verdict | `result_analysis` |
| Tables, charts, qualitative panels, process diagrams, visual validation | `result_visualization` |
| Final Markdown hierarchy and renderer-aware readability pass | `write_md` |
| State transition, archive index, `SUMMARY.md` pointer | `research_manager` |

`experiment_manager` orchestrates assembly and verifies that all required sections exist before checkpointing or closing a direction. No skill may silently rewrite another skill's scientific judgment.

### Run report

Every completed `ENN` run first produces `ENN-experiment-report.md` on the experiment branch:

```text
Question and experiment ID
Base commit and controlled change
Setup, data, controls, and reproducibility parameters
Data-quality and adequacy audit
Key results table
Selected diagnostic/evidence charts with captions
Statistical analysis and uncertainty
Fact / inference / speculation
Experiment value: informative | reusable | none
Direction verdict and next action
Retain/discard manifest
```

The report is the input to the value gate. Informative/reusable reports enter an atomic checkpoint. A `none` report is not retained as a standalone artifact, but its ID and exclusion rationale must appear in the final report.

### Final direction report

On `falsified`, `validated`, `superseded`, or `abandoned`, synthesize one reader-facing `REPORT.md` rather than merely moving or splitting files:

```text
Executive conclusion
Original question, hypothesis, and decision thresholds
Experiment map and traceability table
Methods and evaluation design
Results with selected tables and figures
Statistical analysis
Competing explanations and failure analysis
Excluded/invalid runs and reasons
Final verdict and evidence boundary
Revised belief, reusable findings, and limitations
Code/artifact provenance and retention status
Replacement path or promoted implementation
```

The report must be visually informative, not decorative. Prefer a small set of decisive charts, tables, qualitative examples, and Mermaid process diagrams. Each visual must answer a named question and have a self-contained caption. The report bundle may include:

```text
REPORT.md
SUMMARY.md                 # short status/index pointer
figures/                   # selected report figures only
data/                      # compact source tables only
scripts/                   # minimal report plotting source only
```

For falsified directions, this report bundle is the only experiment-specific material returned to the base branch. For validated directions, it is promoted alongside the clean effective implementation and tests. In both cases, raw logs, checkpoints, duplicate formats, temporary diagnostics, and discarded implementations remain excluded.

Before finalizing a report, verify:

- every headline conclusion points to a table, figure, or explicit numeric result;
- every retained visual is referenced in the text and carries source and uncertainty semantics;
- the report distinguishes facts, inference, speculation, and excluded evidence;
- readers can understand the outcome without access to the deleted experiment branch;
- the minimal report bundle renders correctly in the declared target renderer;
- report provenance points to the relevant base and experiment commits even after branch deletion.

For a pivot, archive the old core hypothesis as `superseded` and create a new proposal ID when the research question changes materially. Do not silently mutate project history.

## Validation

### Static checks

- Confirm all seven skill frontmatters, links, `requires`, delegation tables, and overview references resolve.
- Search for stale fixed paths such as `proposal/04-milestones.md` and direct archive writes from analysis skills.
- Search for contradictory definitions of proposal/project, mandatory plotting, visualization ownership, file-write confirmation, and per-session cleanup.
- Verify operational skill documents remain within the revised line budget or use one linked reference file.
- Inspect the final diff to ensure only research skill family files and the new skill are changed.

### Scenario walkthroughs

1. A proposal fails the literature gap gate: archive as rejected without creating an experiment branch.
2. A ready proposal receives explicit GO: create one direction branch/worktree and make the direction active there.
3. A run is invalid due to a code bug: no experiment checkpoint; clean only its outputs and rerun.
4. A negative result rules out a key mechanism: mark informative and preserve one atomic experiment checkpoint.
5. Evidence is inadequate: return inconclusive, not Kill/Pivot/Continue by force.
6. A direction is falsified: base branch receives one illustrated final report bundle and index changes; no exploratory implementation appears in its diff.
7. A direction is validated: promotion diff contains only effective implementation, tests, minimal configuration, and the illustrated final report bundle.
8. A reusable evaluator bug fix emerges from a failed direction: promote it independently with a test.
9. A large checkpoint is valuable: Git contains only its manifest, while closure applies its retention policy.
10. A user requests statistical analysis without a figure: `result_analysis` completes the evidence audit and inference without forcing visualization.
11. A user requests a chart from aggregate means without uncertainty inputs: visualization refuses to fabricate error bars and records the limitation.
12. A user requests only an architecture diagram: `result_visualization` handles it without statistics or a direction verdict.
13. Exploratory plots expose a data bug: classify them as diagnostic, preserve the resulting bug finding in the run/final reports, and clean the plots after the run.
14. An ablation figure supports a valuable negative result: retain it with the valuable run report and select it for the illustrated falsification report when it remains decisive.
15. Several invalid runs exist: the final report lists their IDs and exclusion reasons without retaining their code, logs, or figures.

## Success Criteria

- `proposal/` and `project/` have one operational boundary: explicit experiment startup.
- Every state transition has one owner and no subskill directly mutates another owner's state.
- Failed exploration cannot enter the base branch except as a curated illustrated report bundle with compact scientific evidence.
- Successful exploration reaches the base branch only through a clean, reviewable promotion diff containing the effective implementation and final report bundle.
- Invalid or decision-neutral runs do not become permanent commits.
- Large and disposable outputs are controlled per run rather than accumulated until archive time.
- Statistical claims are produced by evidence analysis, while visual artifacts cannot invent or strengthen those claims.
- Diagnostic figures are removed per run; retained figures have a reproducible source, explicit evidence/explanatory purpose, and one retention owner.
- Every completed run is evaluated through a report, and every closed direction leaves one self-contained illustrated final report rather than a fragmented archive.
- Negative results remain discoverable without retaining dead implementations.
- The overview, skill bodies, and references describe the same lifecycle and terminology.
