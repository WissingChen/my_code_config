---
name: research_manager
description: Research project skeleton and file lifecycle. Load when initializing a `.kilo/` project, migrating or archiving documents, or deciding where to put a new research note. Defines the four-directory layout (proposal/project/archive/knowledge), two-digit numeric prefixes, the global.md index layer, archive SUMMARY.md rules, and final REPORT.md requirements.
---

## Output Contract

- 先说结论，再给必要依据和下一步。
- 默认短句和常用词；术语只在更准确时用，首次出现直接解释。
- 内部状态、流程和检查表默认不展示；只有影响决定或用户明确要求时才展开。
- 外部事实、论文结论和数字附来源；不确定的直接写"尚未验证"或"我推测"，不给每句话机械加 fact/speculation 标签。
- 一段能说清就不用表格；独立要点用列表；只有横向比较才用表格。
- 不写套话、廉价肯定、重复总结和固定收尾。

# Research Project Manager

Lightweight skeleton: four directories, numeric ordering, and a pointer layer. `research_manager` owns directory moves, archive naming, and state transitions. It does not run experiments or generate artifacts.

## 1. Directory Layout and Canonical States

```
.kilo/
├── global.md          # pure index (→ progress + TODO.md); no goals or rules
├── TODO.md            # project backlog; single source, links to module TODOs
├── proposal/          # evaluating or ready directions
├── project/           # active directions on an experiment branch
├── archive/           # rejected, falsified, validated, superseded, abandoned
├── reports/           # generated dated status snapshots
└── knowledge/         # external references (knowledge notes)
```

| State | Location | Owner | Entry/Exit |
|---|---|---|---|
| Evaluating | `proposal/NN-slug/` | `research_progress` recommends | Reality gates pass or fail |
| Blocked | `proposal/NN-slug/` | `research_progress` flags | Data, interface, code, or resource facts unverified; no experiment design while blocked |
| Ready | `proposal/NN-slug/` | `research_manager` records | User GO starts experiments |
| Active | `project/NN-slug/` on `exp/NN-slug` | `experiment_manager` operates | Continue, pivot, falsify, or validate |
| Rejected/Falsified/Validated/Superseded/Abandoned | `archive/YYYY-MM-DD-NN-slug/` | `research_manager` applies | Final report is primary deliverable |

## 2. Naming

- Direction unit: `NN-slug/` (two-digit prefix, lowercase hyphenated). Preserve the ID across moves.
- Exceptions: `global.md`, `TODO.md`, `00-overview.md`, `SUMMARY.md`, `REPORT.md`, and dated archive directories do not use `NN-slug`.
- Archive entries: `YYYY-MM-DD-NN-slug/`.
- Knowledge notes: `author-year-title.md` or `source-year-topic.md`; the knowledge query log is `knowledge/papers/00-query-log.md` (owned by `knowledge_keeper`).

## 3. global.md and TODO.md (Index + Backlog)

`global.md` is a pure index, agent-maintained. Keep it ≤60 lines:

- Directory index (proposal, project, archive, knowledge, external index)
- Pointer to `TODO.md` and current project progress

No goals, rules, or explanations here — those are owner-written in `AGENTS.md` (see §4).

`TODO.md` (same directory) holds the project backlog. It links to module-level
TODOs (e.g. `tto_pp/TODO.md`) instead of duplicating them. Keep it ≤150 lines.

## 4. Overviews and Source-of-Truth Hierarchy

Truth precedence when documents conflict: `AGENTS.md` (owner-written goal and process policy) → `global.md` (index/pointers) → direction `00-overview.md` (current state) → registered experiment plan (frozen expectations) → run reports (observed evidence) → knowledge notes (external evidence) → generated status reports (disposable views, never authoritative).

- **Direction-level**: every `proposal/NN-slug/` and `project/NN-slug/` keeps a `00-overview.md` as the entry point. It records **current state only** — status, main question, primary hypothesis, main contradiction, current evidence, dominant uncertainty, next decision, parked questions (idea parking lot; parked items never auto-activate), superseded assumptions. History lives in run reports, not appended here.
- **Collection-level**: create or update a directory's `00-overview.md` only after it holds more than five entries.
- `AGENTS.md` at the project root is hand-written by the project owner; agents are strictly read-only. It stores the project goal, non-goals, success criteria, toolchain/compiler, key constraints, and decision policy — never experiment results, paper notes, or evolving discussion. The most an agent may do is copy `AGENTS_template.md` to the project root as `AGENTS.md` on request; everything after that is owner-maintained.

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
- Plan: each evaluating/blocked/ready direction with state and one-liner (from `proposal/NN-slug/00-overview.md`)
- Active progress: per active direction, latest `ENN` verdict and distance to kill/promotion criteria — data delegated from `experiment_manager` (run reports live on `exp/NN-slug` branches)
- Closed this period: outcomes and lessons (from `archive/*/SUMMARY.md`)
- Next steps and risks: backlog (`TODO.md`) plus judgment

Every claim must trace to an existing source. Generated reports are exempt from line budgets.

## 7. Budgets and Cleanup

Hard limits apply to human-maintained operational research documents:

- `global.md` ≤60 lines; `TODO.md` ≤150 lines
- Any single operational `SKILL.md` or direction document ≤150 lines

Exempt: manuscripts, generated reports/data, code, bibliographies, and indivisible tables.

Propose archive/delete/merge only when concrete stale content is found. Preserve raw scientific evidence unless its retention policy allows deletion.

## 8. Read Discipline

At the start of a session, read `AGENTS.md` (if present), `global.md`, `TODO.md`, and the target direction's `00-overview.md`. Follow only links relevant to the current task. Do not load the entire `.kilo/` tree.

## 9. Skill Delegation

| Request | Load |
|---|---|
| Generate a status report or progress briefing | `research_manager` (§6) |
| Converge a research idea | `research_progress` |
| Search literature or capture to the knowledge base | `knowledge_keeper` |
| Start/monitor/close experiments | `experiment_manager` |
| Analyze experimental evidence | `result_analysis` |
| Produce charts or diagrams | `result_visualization` |
| Format Markdown, plan report visuals, or render a report HTML version | `write_md` |
| Write or polish a paper | `academic-paper-writing` |
| Create an HTML slide deck or presentation | `slide_deck` |

Long-report tasks auto-compose: `experiment_manager` orchestrates `result_analysis` (evidence + visual audit) → `write_md` (visual planning) → `result_visualization` (production) → `experiment_manager` (embed + render-verify) → `write_md` (final readability).
