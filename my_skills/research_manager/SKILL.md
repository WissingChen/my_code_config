---
name: research_manager
description: Research project skeleton and file lifecycle. Load when initializing a `.kilo/` project, migrating or archiving documents, or deciding where to put a new research note. Defines the four-directory layout (proposal/project/archive/knowledge), two-digit numeric prefixes, the global.md pointer layer, archive SUMMARY.md rules, and final REPORT.md requirements.
---

## Output Contract

- Label every claim as **fact** (with source) or **speculation** (explicitly marked, e.g. `[speculation]`). Never state speculation as fact — this is a hard red line.
- Plain language: conclusion first; explain any jargon in one short sentence on first use; no filler phrases or padding; prefer tables or lists when they aid scanning.

# Research Project Manager

Lightweight skeleton: four directories, numeric ordering, and a pointer layer. `research_manager` owns directory moves, archive naming, and state transitions. It does not run experiments or generate artifacts.

## 1. Directory Layout and Canonical States

```
.kilo/
├── global.md          # pointer layer only
├── proposal/          # evaluating or ready directions
├── project/           # active directions on an experiment branch
├── archive/           # rejected, falsified, validated, superseded, abandoned
├── reports/           # generated dated status snapshots
└── knowledge/         # external references (knowledge notes)
```

| State | Location | Owner | Entry/Exit |
|---|---|---|---|
| Evaluating | `proposal/NN-slug/` | `research_progress` recommends | Pass or fail the three gates |
| Ready | `proposal/NN-slug/` | `research_manager` records | User GO starts experiments |
| Active | `project/NN-slug/` on `exp/NN-slug` | `experiment_manager` operates | Continue, pivot, falsify, or validate |
| Rejected/Falsified/Validated/Superseded/Abandoned | `archive/YYYY-MM-DD-NN-slug/` | `research_manager` applies | Final report is primary deliverable |

## 2. Naming

- Direction unit: `NN-slug/` (two-digit prefix, lowercase hyphenated). Preserve the ID across moves.
- Exceptions: `global.md`, `00-overview.md`, `SUMMARY.md`, `REPORT.md`, and dated archive directories do not use `NN-slug`.
- Archive entries: `YYYY-MM-DD-NN-slug/`.
- Knowledge notes: `author-year-title.md` or `source-year-topic.md`; the knowledge query log is `knowledge/papers/00-query-log.md` (owned by `knowledge_keeper`).

## 3. global.md (Pointer Layer)

Index only. Keep it ≤80 lines:

- Goal / non-goals / success criteria
- Directory index (proposal, project, archive, knowledge, external index)
- Backlog

## 4. Overviews

- **Direction-level**: every `proposal/NN-slug/` and `project/NN-slug/` keeps a `00-overview.md` as the entry point.
- **Collection-level**: create or update a directory's `00-overview.md` only after it holds more than five entries.

## 5. Archive Rules and Final Report

Close a direction only through `experiment_manager` or explicit user authorization. A closed active direction must leave a self-contained illustrated `REPORT.md` as its primary deliverable.

`SUMMARY.md` is a short outcome/index pointer only; do not duplicate the report.

Archive outcomes:

- **rejected**: failed before experiments
- **falsified**: registered prediction reliably contradicted
- **validated**: promoted; archived evidence retained
- **superseded**: core question or hypothesis changed materially
- **abandoned**: non-scientific stop reason (resource, priority, etc.)

## 6. Status Reports

On request ("汇报", "status report"), generate a dated snapshot at `.kilo/reports/YYYY-MM-DD-status.md`. Status documents are generated, never hand-maintained; consecutive snapshots are diffed to show change.

Required sections:

- Headline: ≤3 lines synthesizing the period
- Plan: each evaluating/ready direction with state and one-liner (from `proposal/NN-slug/00-overview.md`)
- Active progress: per active direction, latest `ENN` verdict and distance to kill/promotion criteria — data delegated from `experiment_manager` (run reports live on `exp/NN-slug` branches)
- Closed this period: outcomes and lessons (from `archive/*/SUMMARY.md`)
- Next steps and risks: backlog (`global.md`) plus judgment

Every claim must trace to an existing source. Generated reports are exempt from line budgets.

## 7. Budgets and Cleanup

Hard limits apply to human-maintained operational research documents:

- `global.md` ≤80 lines
- Any single operational `SKILL.md` or direction document ≤150 lines

Exempt: manuscripts, generated reports/data, code, bibliographies, and indivisible tables.

Propose archive/delete/merge only when concrete stale content is found. Preserve raw scientific evidence unless its retention policy allows deletion.

## 8. Read Discipline

At the start of a session, read `global.md` and the target direction's `00-overview.md`. Follow only links relevant to the current task. Do not load the entire `.kilo/` tree.

## 9. Skill Delegation

| Request | Load |
|---|---|
| Generate a status report or progress briefing | `research_manager` (§6) |
| Converge a research idea | `research_progress` |
| Search literature or capture to the knowledge base | `knowledge_keeper` |
| Start/monitor/close experiments | `experiment_manager` |
| Analyze experimental evidence | `result_analysis` |
| Produce charts or diagrams | `result_visualization` |
| Format or present Markdown | `write_md` |
| Write or polish a paper | `academic-paper-writing` |
| Create an HTML slide deck or presentation | `slide_deck` |
