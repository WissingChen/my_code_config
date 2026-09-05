---
name: research_manager
description: Research project skeleton and file lifecycle. Load when initializing a `.kilo/` project, migrating or archiving documents, or deciding where to put a new research note. Defines the four-directory layout (proposal/project/archive/knowledge), two-digit numeric prefixes, the global.md index layer, archive SUMMARY.md rules, and final REPORT.md requirements. It does not run experiments (experiment_manager) or judge whether an idea is worth pursuing (research_progress).
---

## Output Contract

- 先说结论，再给必要依据和下一步。
- 默认短句和常用词；术语只在更准确时用，首次出现直接解释。
- 内部状态、流程和检查表默认不展示；只有影响决定或用户明确要求时才展开。
- 外部事实、论文结论和数字附来源；不确定的直接写"尚未验证"或"我推测"，不给每句话机械加事实/猜测标签。
- 一段能说清就不用表格；独立要点用列表；只有横向比较才用表格。
- 不写套话、廉价肯定、重复总结和固定收尾。
- 禁用黑话和自造词（赋能、闭环、抓手、对齐、链路、落地、打磨等），直接说具体那件事。
- 写文件前先经用户确认。
- 只在发现具体的过时或重复内容时才提议清理，不作为固定收尾动作。

# Research Manager — 管目录、状态和归档

轻量骨架：四个目录、数字编号、一层索引。`research_manager` 负责目录搬动、归档命名、状态流转。不跑实验，不产出内容。

## 1. 目录结构和状态

```
.kilo/
├── global.md          # 纯索引（→ 进度 + TODO.md）；不写目标和规则
├── TODO.md            # 项目进展唯一来源；三层树（主线→阶段→方案）
├── proposal/          # 评估中、卡住、已通过还没开工的方向
├── project/           # 正在实验分支上跑的方向
├── archive/           # 已结束的方向
├── reports/           # 生成的带日期状态快照
└── knowledge/         # 外部资料（知识笔记）
```

| 状态 | 位置 | 谁负责 | 进出条件 |
|---|---|---|---|
| 评估中 | `proposal/NN-slug/` | `research_progress` 建议 | 现实检查过或不过 |
| 卡住 | `proposal/NN-slug/` | `research_progress` 标记 | 数据、接口、代码或资源没查清；卡住期间不做实验设计 |
| 通过 | `proposal/NN-slug/` | `research_manager` 记录 | 用户说 GO 才开实验 |
| 进行中 | `project/NN-slug/`（在 `exp/NN-slug` 分支上） | `experiment_manager` 操作 | 继续、转向、证伪或验证通过 |
| 否决 / 证伪 / 验证通过 / 被取代 / 放弃 | `archive/YYYY-MM-DD-NN-slug/` | `research_manager` 执行 | 终版报告是主要交付物 |

## 2. 命名

- 方向单位：`NN-slug/`（两位数字前缀，小写连字符）。搬动时 ID 不变。
- 例外：`global.md`、`TODO.md`、`00-overview.md`、`SUMMARY.md`、`REPORT.md` 和带日期的归档目录不用 `NN-slug`。
- 归档目录：`YYYY-MM-DD-NN-slug/`。
- 知识笔记：`作者-年份-标题.md` 或 `来源-年份-主题.md`；检索日志是 `knowledge/papers/00-query-log.md`（归 `knowledge_keeper` 管）。

## 3. global.md 和 TODO.md（索引 + 待办）

`global.md` 是纯索引，由 agent 维护，≤60 行：

- 目录索引（proposal、project、archive、knowledge、外部索引）
- 指向 `TODO.md` 和当前项目进度的指针

这里不写目标、规则、解释——那些由项目所有者写在 `AGENTS.md`（见 §4）。

`TODO.md`（同目录）是项目进展的唯一来源，由 `research_manager` 创建和维护，其他技能只读。三层树：

1. 主线：一句话中心问题（锁定，只有用户能改）
2. 大阶段：来自 proposal 的确定阶段（如 SFR / TTO / RL），proposal 状态变化时才更新
3. 实现方案：每个阶段的当前做法（不确定），随实验证据增删换，每次改动在回复里说明原因

方向状态一有变化（阶段推进、方案更换、主线调整）就更新。主线和大阶段后面带指向方向文件的链接（如 `project/03-physcene3d/00-overview.md`），有就指，没有不指；也可链接模块级 TODO（如 `tto_pp/TODO.md`），不复制内容。≤150 行。

## 4. 概览文件和谁说了算

文件打架时的优先级：`AGENTS.md`（所有者写的目标和流程约定）→ `global.md`（索引/指针）→ 方向 `00-overview.md`（当前状态）→ 登记的实验计划（冻结的预期）→ 运行报告（观测证据）→ 知识笔记（外部证据）→ 生成的状态报告（一次性视图，永远不算数）。

- **方向级**：每个 `proposal/NN-slug/` 和 `project/NN-slug/` 都有一个 `00-overview.md` 当入口。只记**当前状态**——状态、主要问题、主要假设、主要矛盾、当前证据、最大不确定性、下一步决定、暂存的问题（不自动激活）、被推翻的假设。历史写在运行报告里，不往这里追加。
- **集合级**：一个目录超过五个条目后，才建或更新它的 `00-overview.md`。
- 项目根的 `AGENTS.md` 由项目所有者手写，agent 严格只读。内容是项目目标、不做什么、成功标准、工具链、关键约束、决策约定——绝不放实验结果、论文笔记、进行中的讨论。agent 最多在被要求时把 `AGENTS_template.md` 复制为项目根的 `AGENTS.md`，之后全归所有者维护。

## 5. 归档规则和终版报告

结束一个方向只能经 `experiment_manager` 或用户明确授权。结束一个进行中的方向，必须留下一份自足的带图 `REPORT.md` 作为主要交付物。

`SUMMARY.md` 只是短的结果/索引指针，不复制报告内容。

五种结局：

- **否决**：没进实验就失败
- **证伪**：登记过的预期被稳定推翻
- **验证通过**：已转正，证据保留
- **被取代**：核心问题或假设实质改变
- **放弃**：非科学原因（资源、优先级等）

没进过实验的否决/卡住方向由 `research_manager` 直接归档——没有实验分支，提案里的评审记录（`experiment-plan.md`）就是最终文档，不要求 `REPORT.md`。五种结局的完整走查：`references/lifecycle-trace.md`。

## 6. 状态汇报

被请求时（"汇报"、"status report"）生成带日期的快照 `.kilo/reports/YYYY-MM-DD-status.md`。状态文档只生成、不手维护；相邻快照做 diff 展示变化。

必备内容：

- 头条：≤3 行概括本期
- 在评方向：每个评估中/卡住/通过的方向，状态加一句话（来自 `proposal/NN-slug/00-overview.md`）
- 进行中的进展：每个方向最近一次 `ENN` 的判定、离停手/做成标准的距离——数据由 `experiment_manager` 提供（运行报告在 `exp/NN-slug` 分支上）
- 本期结束的方向：结局和教训（来自 `archive/*/SUMMARY.md`）
- 下一步和风险：待办（`TODO.md`）加判断

每个说法都要能指到已存在的来源。生成的报告不受行数预算限制。

## 7. 行数预算和清理

人维护的运营文档有硬上限：

- `global.md` ≤60 行；`TODO.md` ≤150 行
- 任何单个运营用 SKILL.md 或方向文档 ≤150 行

豁免：论文手稿、生成的报告/数据、代码、参考文献列表、拆不开的表格。

超预算时：把细节拆到旁边的引用文件，使用点留一行指针；不许靠悄悄删规则来压缩。

只在发现具体的过时或重复内容时才提议归档/删除/合并。过时：描述的状态已不再成立、且被更高优先级的文件取代。重复：同一事实在两个文件里维护——保留归口技能负责的那份，另一份换成指针。原始科学证据保留，除非它的保留规则允许删。

## 8. 读文件的规矩

会话开始时先读 `AGENTS.md`（有的话）和 `TODO.md`，再顺着 TODO 里的链接读对应方向的文件。`global.md` 只是索引备查。不整树加载 `.kilo/`。

## 9. 找哪个技能

请求领域 → 技能 的对照表、长报告任务的串联顺序，单一事实源在技能组总览 `my_skills/00-overview.md` §5，这里不复制。
