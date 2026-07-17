---
name: research_manager
description: Research project skeleton and file lifecycle. Load when initializing a `.kilo/` project, migrating or archiving documents, or deciding where to put a new research note. Defines the four-directory layout (proposal/project/archive/knowledge), two-digit numeric prefixes, the global.md pointer layer, and archive SUMMARY.md rules.
---

# Research Project Manager

Lightweight skeleton: four directories, numeric ordering, and a pointer layer.

## 1. Directory Layout

Create `.kilo/` with four subdirectories:

```
.kilo/
├── global.md          # pointer layer only
├── proposal/          # not yet scheduled
├── project/           # being implemented
├── archive/           # deprecated / falsified
└── knowledge/         # external references
```

## 2. Naming

- Files and directories: `NN-lowercase-hyphenated` (two-digit prefix).
- Archive entries: `YYYY-MM-DD-original-directory-name`.
- Knowledge papers: `author-year-title.md`.

## 3. global.md (Pointer Layer)

`global.md` is an index, not a content dump. Keep it **≤80 lines**. Sections:

- Goal / Non-goals / Success criteria
- Directory index (proposal, project, archive, knowledge, external index)
- Backlog

Decision Log and Change Log are no longer required.

## 4. Overviews

A subdirectory only needs `00-overview.md` when it contains **more than 5 files**. The overview is a living map: responsibility, file list, key entry points.

## 5. Archive Rules

Move retired content from `project/` as a whole. Each entry needs a `SUMMARY.md`.

For **falsified** entries, `SUMMARY.md` must include:

- Original hypothesis
- Experiment and observation
- Revised belief
- Replacement path (or "none")

For **replaced** entries, only the replacement path is required.

## 6. Budgets and Cleanup

Hard limits:

- `global.md` ≤80 lines
- Any single document ≤150 lines

If a document exceeds the limit, compress or split it on the spot. Do not let it grow.

At the end of each session, propose: "what should be archived, deleted, or merged?" Wait for user confirmation before acting.

## 7. Read Discipline

At the start of a session, read only `global.md` and the `00-overview.md` of the directory you are working in. Do not load the entire `.kilo/` tree.

## 8. Content Rules

Two rules survive from the old content guide:

- **One-sentence positioning**: every section starts with its core claim.
- **Numbers first**: parameters, thresholds, durations go in tables with concrete values.

YAML frontmatter and status labels are optional for new documents. Old documents do not need retrofitting.

## 9. Skill Delegation

| Request | Load |
|---------|------|
| Converge a research idea | `research_progress` |
| Analyze experimental data | `result_analysis` |
| Plot data or draw diagrams | `result_analysis` |
| Format / present Markdown | `write_md` |
| Write or polish a paper | `academic-paper-writing` |
