---
name: research_manager
description: Research project management guidelines—must be followed for any document creation, update, or archival. Standardizes .kilo/ directory structure, global.md as the single source of truth, the proposal/project/archive/knowledge four-directory system, naming conventions, status labels, archival rules, and collaboration workflows to ensure research projects remain clear, traceable, and context-preserving from ideation through implementation, experimentation, and archival. Use for new project initialization, document organization, file migration/archival, and document iteration.
---

# Project Management

> A set of management guidelines for research projects. Through standardized directory structure, documentation conventions, and workflow rules, these guidelines ensure that project ideation, implementation, experimentation, and archival are well-organized, traceable, and never lose context.

---

## 1. Initialization Principles

When starting a new project, establish the skeleton in the following order:

1. **Create directories**: Under the project root, create `.kilo/` with four subdirectories—`proposal/`, `project/`, `archive/`, `knowledge/`—and a `global.md` file.
2. **Establish external index**: If the project root already contains implementation files not managed by `.kilo/`, create mappings in global.md's "External Index" section. **Never forcibly migrate** existing files—avoid breaking existing build paths.
3. **Populate global context**: `global.md` is the project's single source of truth. At initialization, it must include: project goals, non-goals, success criteria, directory index, naming conventions, decision log, and change log.

---

## 2. Directory Structure Specification

### 2.1 Top-Level Directories: proposal / project / archive / knowledge

The three lifecycle directories follow: **Ideation → Implementation → Retirement**. `knowledge/` sits alongside as a non-lifecycle reference layer for external knowledge (papers, technical reports, related repositories).

```
.kilo/
├── global.md             # Single source of truth
├── proposal/             # Ideation layer: not yet scheduled for development
├── project/              # Implementation layer: in progress or completed
├── archive/              # Retirement layer: deprecated/replaced/falsified
└── knowledge/            # Knowledge layer: external references (papers, repos, reports)
```

### 2.2 Naming Iron Rule

All files and directories must use a **two-digit numeric prefix** to maintain lexicographic order as reading order. Names like `untitled.md`, `temp.md`, `new.md` are forbidden.

---

### 2.3 Subdirectory Overview Principle

**Every subdirectory under proposal/, project/, and archive/ must contain a `00-overview.md` (archive top level uses `00-overview.md`, individual archive entries use `SUMMARY.md`).**

The core purpose of this principle is to **offload global.md**: global.md serves only as a pointer layer, with detailed information pushed down into subdirectory overviews.

```
.kilo/
├── global.md              ← Pointer layer: index + decision log + change log
├── proposal/
│   ├── 00-overview.md     ← Proposal landscape
│   ├── 03-solution-candidates/
│   │   └── 00-overview.md ← Candidate comparison summary
│   └── ...
├── project/
│   ├── 00-overview.md     ← Implementation landscape
│   ├── 01-module-a/
│   │   └── 00-overview.md ← Module A: responsibilities, interfaces, dependencies, status
│   ├── 02-module-b/
│   │   └── 00-overview.md
│   └── ...
└── archive/
    ├── 00-overview.md     ← Archive registry table (lists all entries with reasons)
    └── 2026-07-04-xxx/
        └── SUMMARY.md     ← Detailed summary for a single entry
knowledge/
    ├── 00-overview.md     ← Knowledge index (key info for quick retrieval)
    ├── papers/
    │   └── 00-overview.md ← Paper summaries
    ├── reports/
    │   └── 00-overview.md ← Technical report summaries
    └── repos/
        └── 00-overview.md ← Related repo summaries
```

**Each subdirectory `00-overview.md` should contain**:
- The directory's responsibility/positioning (one sentence)
- File listing with their purposes (table)
- Current status (overall)
- Dependencies (which directories/modules it relates to)
- Key entry points (which file newcomers should read first)

**Forbid global.md from bloating into a content repository**—global.md's directory index needs only a single-line reference; all details point to subdirectory overviews.

---

### 2.4 proposal/ (Ideation Layer)

Stores only content **not yet scheduled for development**. Once implementation begins, the content must be migrated to `project/` and global.md updated accordingly.

Standard structure (adjustable as needed; not all must be created):
- `00-overview.md` — Project landscape: goals, non-goals, success criteria
- `01-problem-definition.md` — Problem definition, inputs/outputs, boundary conditions
- `02-literature-review.md` — Survey of related techniques/papers/solutions
- `03-solution-candidates/` — Candidate solution comparison (one file per candidate)
- `04-milestones.md` — Phased breakdown, acceptance criteria, dependencies
- `05-risks.md` — Technical risks, fallback strategies, pending decisions

---

### 2.5 project/ (Implementation Layer)

Stores only content **that has begun or completed implementation**. The boundary with proposal is: when code/scripts/config files are first created or modified, the corresponding documentation must enter `project/`.

**project/ internal structure is not prescriptive**—organize by subsystem, module, scenario, or any other dimension. Constraints:
- All files and directories must have a two-digit numeric prefix
- Every subdirectory must contain a `00-overview.md` (see §2.3)
- Files without a numeric prefix are forbidden (except `README.md`, though `00-README.md` is recommended)

Common organizational patterns:
- By functional layer: `00-meta/`, `01-architecture/`, `02-modules/`, `03-experiments/`
- By subsystem: `00-agent/`, `01-hal/`, `02-bridge/`
- By scenario: `00-game/`, `01-simulation/`, `02-real-robot/`

---

### 2.6 archive/ (Retirement Layer)

Stores **deprecated, replaced, or falsified** complete projects/modules/experiments. The boundary with project is: the content is no longer referenced by any active code or experiments.

**Storage granularity**: Preserve the original directory structure from project/, prepend a `YYYY-MM-DD-` timestamp prefix, and move the entire directory tree as a unit.

```
archive/
├── 00-overview.md         # Archive registry table (lists every entry with reasons)
├── 2026-07-04-03-experiments-baseline-v1/
│   ├── SUMMARY.md
│   └── ... (complete original project/ directory structure)
└── 2026-05-12-02-modules-old-parser/
    ├── SUMMARY.md
    └── ...
```

**`00-overview.md`**: The living map of archive. A single table listing all archived entries: name, archive date, reason (replaced/falsified), replacement path, and summary link. New members can quickly locate historical lessons by reading this table alone.

**Every archive entry must come with a `SUMMARY.md`** containing the following fixed fields:

```markdown
---
title: "[archive entry name]"
date: "YYYY-MM-DD"
reason: "[replaced] or [falsified]"
---

## Archival Reason
[One sentence explaining why this was retired]

## Original Hypothesis (required for falsified)
[We believed X to be true]

## Experiment & Observation (required for falsified)
[What experiments were conducted, what data was observed]

## Revised Belief (required for falsified)
[We now believe Y, supported by evidence Z]

## Replacement
[Path to replacement in project/, or "no replacement"]
```

**Replaced vs. Falsified**:

| Type | Archival Reason | SUMMARY.md Focus | Value |
|------|----------------|------------------|-------|
| **Replaced** | Implementation upgraded; old version no longer runs | Replacement path | Historical reference |
| **Falsified** | Core hypothesis proven wrong by experiment | Hypothesis / Experiment / Revised belief | **Prevents repeating mistakes** |

---

### 2.7 knowledge/ (Knowledge Layer)

Stores **external knowledge references** that inform project decisions: academic papers, technical reports, related open-source repositories, benchmarks, datasets, etc. This layer is not part of the lifecycle—it serves as a reference base that feeds into proposal ideation and project implementation.

```
knowledge/
├── 00-overview.md         # Knowledge index: key info for quick retrieval
├── papers/                # Academic paper summaries
│   ├── 00-overview.md     # Paper index with one-line takeaways
│   └── author-year-title.md
├── reports/               # Technical reports, whitepapers
│   ├── 00-overview.md
│   └── org-year-title.md
└── repos/                 # Related code repositories
    ├── 00-overview.md
    └── org-repo-name.md
```

**Internal structure is not prescriptive**—organize by type (papers/reports/repos), topic, or any other dimension. Constraints:
- All files and directories must have a two-digit numeric prefix
- The top-level `knowledge/00-overview.md` is mandatory—it serves as the **quick retrieval index**
- Each subdirectory must contain its own `00-overview.md`

**`knowledge/00-overview.md`** — the quick retrieval index. A living table that allows anyone to quickly find relevant external knowledge:

| Entry | Type | Key Insight | Link |
|-------|------|-------------|------|
| GAN Paper | paper | Generative adversarial networks for image synthesis | papers/00-overview.md |
| XYZ Benchmark | repo | Standard evaluation suite for task X | repos/xyz-benchmark.md |

**Per-entry files** (e.g., `author-year-title.md` for papers, `org-repo-name.md` for repos) should capture:
- **One-line takeaway**: The single most important insight
- **Relevance**: Why this matters to our project
- **Key details**: Method, results, limitations (papers); architecture, setup, compatibility (repos)
- **Link**: URL/DOI to the original source
- **Status**: Read / To-read / Applied / Outdated

**跨技能引用**: `write_paper` 在论文撰写阶段引用文献时应归档到 `knowledge/papers/`，遵循本节的命名和格式约定。`result_analysis` 如需搜索文献排除竞争假设，参考 `research_progress` Step 3 的文献搜索子流程，结果同样归档到 `knowledge/papers/`。`research_visualize` 生成的统计图表和 Mermaid 源文件保存到 `project/` 对应子目录，遵循本文档的命名约定和 00-overview.md 更新规则。

---

## 3. global.md Specification (Pointer Layer, Not a Content Repository)

**global.md is an index, not a detail repository.** Detailed arguments, architecture diagrams, and experimental data all sink down into subdirectory `00-overview.md` files. global.md retains only at-a-glance summaries + links to deeper documents.

`global.md` must contain the following seven fixed sections, and **must be updated synchronously** whenever proposal, project, or archive is modified:

### 3.1 Project Overview
- **Goal**: One-sentence description
- **Non-goals**: What is explicitly not in scope (prevent scope creep)
- **Success Criteria**: Verifiable metrics or deliverables

### 3.2 Directory Index (Living Map)
Maintained as five tables: proposal, project, archive, knowledge, and external index.

| Area | Table Columns | Description |
|------|--------------|-------------|
| proposal | File, Status, Owner, Notes | Records maturity of ideation documents |
| project | File/Dir, Status, Corresponding Code Path, Notes | Records implementation-to-code mappings |
| archive | Entry, Archival Reason, Replacement, Notes | Records retired content and its lessons |
| knowledge | Entry, Type, Key Insight, Status | Records external references for quick retrieval |
| External Index | Path, Role, Linked .kilo Doc | Records files outside .kilo/ and their associations |

### 3.3 Standards & Constraints
- Language version, code style, test coverage requirements
- Registration rules for new dependencies
- Document naming conventions

### 3.4 Naming Conventions
- Documents: `two-digit prefix + lowercase-hyphenated` (e.g., `01-problem-definition.md`)
- Experiment folders: `YYYY-MM-DD-short-description`
- Archive entries: `YYYY-MM-DD-original-directory-name`
- Knowledge entries: `author-year-title.md` for papers, `org-repo-name.md` for repos, `org-year-title.md` for reports
- Code: module names snake_case, class names PascalCase

### 3.5 Decision Log (Reverse Chronological)
Records "why we chose A over B" to prevent project amnesia. Includes a conclusion column pointing to archive SUMMARY.md for details.

| Date | Decision | Rationale | Alternatives | Conclusion |
|------|----------|-----------|--------------|------------|
| YYYY-MM-DD | Specific decision | Why | Rejected options | ✅ Valid / ❌ Falsified → see archive/xxx/SUMMARY.md |

**Falsified decisions**: Conclusion column shows `❌` + a link to the corresponding archive SUMMARY.md. Do not expand details in this table.

### 3.6 Change Log (Reverse Chronological)
Records "what moved from where to where" to prevent broken links. Write SUMMARY.md synchronously when archiving.

| Date | Operation | File | Reason |
|------|-----------|------|--------|
| YYYY-MM-DD | Migration/Archive/Creation | Path | Why |

### 3.7 Backlog
Use a concise list to record directions that are confirmed but not yet scheduled. Do not expand arguments here—arguments belong in proposal/.

---

## 4. 内容组织规范（Content Organization）

> 本章定义文档的**内容组织规范**（what——写什么、什么粒度）。
> **视觉呈现规范**（how——HTML 盒子、调色板、架构图）见 [write_md](write_md)。写文档时需同时参考两者以覆盖从结构到呈现的完整规范。

### 4.1 File Structure Iron Rule

Every Markdown file within `.kilo/` must contain three parts:
1. **YAML Frontmatter**: Must include at minimum `title`, `last_updated`, `status`
2. **Navigation bar**: A blockquote at the top listing related document links, e.g., `> Related: [filename](filename.md), Previous: [...]`
3. **Body**: Hierarchical headings, using tables, lists, and code blocks to organize content

### 4.2 Structured Writing Principles

1. **One-sentence positioning**: Begin each section with 1-2 sentences stating the core thesis, then elaborate. Never substitute vague paragraphs for conclusions.
2. **Numbers first**: Whenever parameters, dimensions, durations, or thresholds are involved, list specific values in tables. Avoid vague descriptors like "faster" or "larger".
3. **Design rationale**: Every key design choice must be followed by a `**Design rationale**:` paragraph explaining why. Never present what without why.
4. **Code as documentation**: Use pseudocode or Python to express flows and data structures, rather than pure prose paragraphs.
5. **Cross-references**: Use `[filename](filename.md)` links for related documents, concentrated in the top navigation bar. Never describe the same information in multiple places.
6. **Citation numbering**: Use `[N]` format for literature references, pointing to a separate reference file.

### 4.3 Detail Granularity

Information density is determined by the document's position in the project lifecycle:

| Level | Applicable Context | Requirements |
|-------|-------------------|--------------|
| **Rich** | Core design docs (architecture, methodology, problem definition) | Full argument + architecture description + design rationale + code examples |
| **Moderate** | Evaluation / experiment / test docs | Table-driven + key step descriptions; minimize complex architecture diagrams |
| **Concise** | Planning / timeline / reference / extension docs | Concise tables + bullet points; retain frontmatter and navigation bar |

Principle: The closer to "what we are doing now," the more detailed. The closer to "what we might do later," the more concise.

---

## 5. Workflow Rules

### 5.1 Single-Point-of-Write Principle

Any piece of information should exist as the authoritative version in only **one** place. If `project/02-modules/model/` describes the model structure, do not duplicate it in `proposal/`. In proposal, replace with a link: `See [project/02-modules/model/README.md](project/02-modules/model/README.md)`.

### 5.2 Status Labels

Every document/directory must display its status at the top:

- **proposal documents**: `🟡 Draft`, `🟢 Final`, `🔴 Stale`
- **project documents**: `🟡 WIP`, `🟢 Stable`, `🔴 Deprecated`

### 5.3 proposal → project Trigger Conditions

Content may only be migrated from `proposal/` to `project/` when all of the following checks pass:

| Check | Verification Standard |
|-------|----------------------|
| Implementation plan | Decomposed to module level with clear interface definitions |
| Acceptance criteria | Verifiable metrics or deliverables, documented in experiment report.md |
| Dependencies ready | Data, environment, permissions, external APIs are available |

**Migration actions**:
1. Physically move files or create corresponding directories
2. Record in global.md's Change Log
3. Update the original proposal document status to `🔴 Migrated` and add a link pointing to the new location

### 5.4 project → archive Trigger Conditions

- Code has been refactored and the old version no longer runs
- Experiment has been superseded by a new experiment and conclusions are recorded
- **Core hypothesis has been experimentally falsified** (the most important category)
- Configuration/scripts have expired

**Archival actions**:
1. Under `archive/`, create a `YYYY-MM-DD-original-directory-name` directory
2. Move the entire directory structure from project/ as a whole (do not split; preserve context)
3. **Create `SUMMARY.md`**: Fill out using the §2.6 template; for falsified entries, focus on hypothesis/experiment/revised belief
4. Record the retirement reason in global.md's Change Log
5. Update the conclusion column of the corresponding decision in global.md's Decision Log (for falsified: fill `❌` + link)
6. If interface changes are involved, annotate the replacement document with "Compatibility break: original interface see archive/..."

### 5.5 Prohibited Actions

- Forbidden to write implementation details beyond pseudocode in `proposal/`
- Forbidden to store unvalidated "ideas" in `project/` (ideas go back to proposal)
- Forbidden to directly delete any file or document that has ever existed (must go through archive)
- Forbidden to skip `SUMMARY.md` when archiving (discarding lessons learned is the greatest waste)
- Forbidden to create files without a numeric prefix (except `README.md`, though `00-README.md` is recommended)
- Forbidden to let global.md bloat into a content repository (details must sink into subdirectory overviews)
- Forbidden to create subdirectories lacking a `00-overview.md`

---

## 6. Collaboration Mode with Users

When the user raises a new requirement, respond in the following order:

1. **Locate**: Is this proposal-level ideation or project-level implementation?
2. **Record**: Create/update documents in the appropriate directory, following naming conventions (two-digit prefix)
3. **Link**: Update the index and status in `global.md`; add navigation bars at the top of documents pointing to related files
4. **Confirm**: Briefly describe the placement and current status to the user; ask the user to confirm acceptance criteria when necessary

**Special rule**: If the user says "just note it down, we'll do it later," you **must** place it in `proposal/` with `Status: 🟡 Draft` and register it in global.md's Backlog.

**技能委托指南**: 当用户请求落入特定领域时，加载对应技能（加载 research_manager 即可获得目录体系，其他技能按需叠加）：
| 请求领域 | 加载技能 |
|---------|---------|
| 课题收敛、研究想法论证 | `research_progress` |
| 实验结果分析、假设检验 | `result_analysis` |
| 统计绘图、流程图绘制 | `research_visualize` |
| 文档排版、视觉呈现 | `write_md` |
| 论文写作、稿件打磨 | `write_paper` |

---

## 7. Success Criteria

The signs that these guidelines are effective:

- Fewer unnecessary changes in diffs
- Fewer rewrites due to overcomplication
- Clarifying questions emerge before implementation rather than after mistakes
- New members can understand the project's current state within 5 minutes by reading `global.md` and the directory index
- Project history (why A was chosen over B, what moved where) is fully traceable through the Decision Log and Change Log
- Falsified hypotheses are never repeated by the same person or different people
