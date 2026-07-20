---
name: result_visualization
description: Charts, evidence tables, process diagrams, and figure validation for research reports. Load when the user asks to plot data, draw diagrams, or produce publication-ready figures. Delegates statistical analysis and verdicts to result_analysis.
requires: research_manager
---

# Result Visualization — Encode Evidence Without Distortion

`result_visualization` owns visual encoding and figure production. It does not invent uncertainty, run hypothesis tests, or issue direction verdicts.

## 1. Data Charts and Evidence Tables

Accept raw/tabular data or a handoff from `result_analysis`. Validate: data shape, observational unit, aggregation, missing values, and available uncertainty.

Select form from the analytical question:

| Question | Form |
|---|---|
| Distribution | histogram, density, box, violin, strip |
| Paired change | paired points/lines, slope graph |
| Trend over steps | line with explicit uncertainty unit |
| Comparison | dot plot, small multiples, bar only when few categories |
| Relationship | scatter, heatmap, contour |
| Calibration | reliability diagram, residual plot |
| Sensitivity/ablation | ordered dot/bar, interaction plot |

Prefer showing distributions or raw points; do not hide heterogeneity behind aggregate bars. Use compact tables when the data are trivial or a chart adds no information. Do not invent error bars, CIs, significance markers, missing values, or sample sizes.

## 2. Process and Architecture Diagrams

Handle Mermaid flowcharts, state diagrams, sequence diagrams, architecture diagrams, ER diagrams, and timelines without invoking statistical analysis. Require: purpose, entities/states, relationships/transitions, and target renderer. Split diagrams that exceed a readable node/edge budget. Use Mermaid for standard semantics; when Mermaid cannot express the layout, use self-contained inline SVG: reuse the semantic color palette, no external font or script dependencies, and label the artifact class. Do not use draw.io or other plugin-dependent formats.

## 3. Figure Production and Validation

Generate reproducible source plus minimum outputs: PDF/SVG for vector use, PNG only when a preview or raster target is actually needed. Check axis labels and units, scale and baseline, legend, ordering, uncertainty semantics, colorblind/grayscale readability, font availability, clipping, and caption self-containment.

Reject misleading defaults: unlabelled truncated axes, dual axes without strong justification, 3D decoration, rainbow maps, pie charts as the default comparison, and significance decoration unsupported by the analysis. Treat script/source and rendered outputs sharing one prefix as one artifact bundle.

## 4. Artifact Lifecycle

| Class | Purpose | Default retention |
|---|---|---|
| `diagnostic` | Debugging, data-quality checks, exploratory inspection | Do not commit; clean after the run |
| `evidence` | Supports an experiment-value or direction verdict | Retain with a valuable run report; select minimum for final report |
| `explanatory` | Communicates a stable process, architecture, or manuscript claim | Retain only for a current promoted system or claim |

Label every generated artifact with its class and hand the retention recommendation to `experiment_manager`. A polished figure is not automatically valuable evidence. Both validated and falsified directions may retain selected visuals when they materially support the final report; report assets are curated evidence, not a dump of all generated figures.

## 5. Handoff from result_analysis

Accept a request containing: purpose/question, source data and version, observational unit and study design, variables/groups/facets/ordering, summary/transformation, valid uncertainty representation, claim or comparison, target medium and renderer, artifact class and retention recommendation. Produce the visual; do not alter the statistical claim.

For implementation guidance, see `plotting-reference.md`.
