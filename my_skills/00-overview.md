---
title: "技能组总览 — Research Skill Family"
last_updated: "2026-08-15"
---

# 技能组总览

> Related: [research_manager](research_manager/SKILL.md), [research_progress](research_progress/SKILL.md), [knowledge_keeper](knowledge_keeper/SKILL.md), [experiment_manager](experiment_manager/SKILL.md), [result_analysis](result_analysis/SKILL.md), [result_visualization](result_visualization/SKILL.md), [write_md](write_md/SKILL.md), [academic-paper-writing](academic-paper-writing/SKILL.md), [slide_deck](slide_deck/SKILL.md)

## 0. 一句话定位

9 个技能覆盖研究全生命周期：收敛想法、管理知识、执行实验、解析证据、可视化、表达文档、成稿论文、生成展示页。总原则：**先落地现实，再决定验证什么；每个实验必须收敛一个决策相关的不确定性。**

## 1. 技能清单

| 技能 | 角色 | 触发词 |
|------|------|--------|
| `research_manager` | 目录与研究状态、真相层级 | "初始化项目"、"归档"、"建文档" |
| `research_progress` | 方向收敛：价值→相关工作现实→实现闭环→决策型验证 | "有个想法"、"这个方向怎么样" |
| `knowledge_keeper` | 知识检索、论文质量判断（含实现级事实）与落库 | "查文献"、"这篇论文讲什么"、"存到知识库" |
| `experiment_manager` | 实验执行、主矛盾约束、视觉验收与报告组装 | "开始实验"、"跑第 N 次"、"关闭方向" |
| `result_analysis` | 统计分析、因果链定位、收敛账本 | "分析数据"、"Kill/Pivot/Continue" |
| `result_visualization` | 数据图表 + 论证图（实现链/对齐/风险/决策） | "画图/plot"、"流程图"、"出图" |
| `write_md` | 视觉规划 + 可读性两次调用、报告 HTML 渲染 | "排版"、"美化文档"、"出 HTML 报告" |
| `academic-paper-writing` | 论文写作 | "写论文"、"润色"、"改 Introduction" |
| `slide_deck` | HTML 展示页（代替 PPT，仅横向翻页） | "做个展示"、"slides"、"代替 PPT" |

## 2. 标准生命周期

| 状态 | 位置 | 所有者 | 转换事件 |
|---|---|---|---|
| Evaluating | `proposal/NN-slug/` | `research_progress` 推荐 | 现实审查通过或失败 |
| Blocked | `proposal/NN-slug/` | `research_progress` 标记 | 数据/接口/代码/资源事实未查清；禁止实验设计 |
| Ready | `proposal/NN-slug/` | `research_manager` 记录 | 用户 GO 开始实验 |
| Active | `project/NN-slug/` on `exp/NN-slug` | `experiment_manager` 执行 | 继续、转向、证伪、验证 |
| Rejected/Falsified/Validated/Superseded/Abandoned | `archive/YYYY-MM-DD-NN-slug/` | `research_manager` 应用 | 最终报告为主交付物 |

实验循环：每次 `ENN` 绑定**一个主假设 + 当前主矛盾**，跑完先形成图文 `ENN-experiment-report.md`（含收敛账本），通过价值门后再 checkpoint。连续两轮未缩小决策相关不确定性 → 停止实验序列，退回 `research_progress` 重新界定问题。关闭方向时综合为一份图文并茂的 `REPORT.md`。需要汇报时由 `research_manager` 生成带日期的状态快照至 `.kilo/reports/YYYY-MM-DD-status.md`，永不手工维护，相邻快照可直接 diff。

## 3. 真相层级与上下文纪律

文档冲突时的优先级：`AGENTS.md`（下游项目根，你维护的过程政策，Agent 只读；模板见仓库根 `AGENTS_template.md`）→ `global.md`（当前目标与指针）→ 方向 `00-overview.md`（当前状态，含主矛盾与停放区）→ 已登记实验计划（冻结预期）→ 运行报告（观测证据）→ 文献笔记（外部证据）→ 生成的状态快照（一次性视图）。

会话开始只读 `global.md` 和目标方向的 `00-overview.md`，按需跟随链接；不整树加载 `.kilo/`。方向 overview 只记当前状态，历史留在运行报告；新想法默认进停放区，不自动激活。

## 4. 交叉引用矩阵

| 被引 →<br>引用 ↓ | manager | progress | keeper | experiment | analysis | visualization | write_md | academic | slides |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| research_manager | — | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| research_progress | ✓ | — | handoff | handoff | — | ✓(论证图) | — | — | — |
| knowledge_keeper | ✓ | — | — | — | — | — | — | — | — |
| experiment_manager | ✓ | ✓ | — | — | ✓ | ✓ | ✓(两次) | — | — |
| result_analysis | ✓ | — | ✓ | — | — | handoff | — | — | — |
| result_visualization | ✓ | — | ✓ | ✓ | — | — | — | ✓ | — |
| write_md | — | — | ✓ | — | — | handoff | — | ✓ | — |
| academic-paper-writing | ✓(citation) | — | — | — | ✓ | — | — | — | — |
| slide_deck | ✓ | — | — | — | handoff | handoff | — | — | — |

## 5. 委托指南

| 请求领域 | 加载技能 |
|----------|----------|
| 项目状态汇报、进展快照 | `research_manager` |
| 课题收敛、研究想法论证 | `research_progress` |
| 论文/资料检索、知识库落库 | `knowledge_keeper` |
| 开始/管理/关闭实验、生成报告 | `experiment_manager` |
| 统计推断、证据判断 | `result_analysis` |
| 数据图表、流程图、论文配图 | `result_visualization` |
| 文档排版、报告可读性、报告 HTML 版 | `write_md` |
| 论文写作、稿件打磨 | `academic-paper-writing` |
| 项目展示、HTML 幻灯片 | `slide_deck` |

报告任务自动叠加：`experiment_manager` + `result_analysis` + `write_md`（视觉规划）+ `result_visualization` + `write_md`（最终检查），不需要用户逐个触发。

## 6. 设计原则

1. **Manager owns research state**: 目录移动、归档、状态转换只能由 `research_manager` 或它委托的 `experiment_manager` 执行。
1. **Search once, capture always**: 外部检索由 `knowledge_keeper` 执行，本地优先、结果必落库、查询留日志，禁止重复检索。
1. **Quality over relevance**: 检索产出不是相关性列表。`knowledge_keeper` 对每篇被依赖的论文给出角色（anchor/competitor/adjacent/background）、质量（strong/usable/weak）和阅读深度；会议等级、作者、引用只是辅助信号，不能代替全文判断。最近直接工作必须返回实现级事实（数据、目标、代码、算力、失败边界）。判断规则集中在 `knowledge_keeper/paper-quality.md`。
1. **Direct work ≠ dead direction**: 有人做过同题不自动否定课题——看它是高质量完整解决（真冲突）还是占坑但做得差（设下限不设上限）。但"别人做得差"本身不是贡献，必须说清我们多带来什么。
1. **Reality gates before experiment design**: 提案 ready 必须先过价值、相关工作现实、实现闭环三道审查，再存在一项会改变决策的验证。核心实现链上连续两个 `assumed/unknown` 环节 → 状态 `blocked`，禁止进入实验设计。锚点集与最低质量线仍为 ready 的必要条件。
1. **Baseline → expectation → actual is the analysis loop**: 新方案必须在实验前写明相对 baseline 的预期结果、机制假设和可观测中间信号；实验后先定位哪条因果边成立或断裂（实验有效性→干预→机制→目标→价值），再解释偏差。表面指标变差不能直接证明方向无效，也不能据此进行没有新机制假设的 v2/v3 迭代。
1. **Convergence accounting every run**: 每轮实验必须缩小活跃解释集或更新主矛盾；新发现默认进停放区；局部异常只有能解释主要偏差时才能升级为主问题。信息增加 ≠ 进展，判断改变才是进展。
1. **Visual audit is mandatory, figure count is not**: 每份长报告必须执行视觉需求审计（可以考虑后选择纯文本并记录理由），被选中图必须实际产出、嵌入并渲染验证。图的数量不是质量指标。
1. **Output contract is duplicated by design**: 直白表达契约逐字内嵌在每个 SKILL.md 中（agent 只加载单个技能，共 9 个）；修改契约必须同步全部 9 处。
1. **Experiment value, not success, determines checkpoints**: 价值为 `informative` 或 `reusable` 才 checkpoint；`none` 只记录排除原因。
1. **Experiment branches are never merged directly**: 失败方向只返回最终报告包；成功方向通过干净的 `promote/NN-slug` 分支进入主线。

两条硬规则：

- **没有通过现实实现链审查，不进入实验设计。**
- **没有完成视觉需求审计和渲染验证，不宣布长报告完成。**

内部流程名不进入面向用户的正文：

| 内部词 | 对用户的说法 |
|---|---|
| gate / readiness | 这一关确认什么 / 能不能开始做 |
| promotion criterion | 做到什么程度算成功 |
| kill criterion | 出现什么结果就停 |
| artifact / checkpoint | 结果文件 / 保留这次实验 |
| handoff / lifecycle | 交给谁处理 / 当前状态 |
| main contradiction | 当前最关键的分歧点 |
| parking lot | 先记下来的新想法 |

可视化边界：

- `result_analysis` 决定数字支持什么、不支持什么；
- `result_visualization` 决定如何无失真地编码这些数字（含课题论证图）；
- `experiment_manager` 决定是否保留该产物并验收其嵌入。

按需叠加：基础层 + 1–2 个技能即可。图只在显著改善解释时才绘制，但"是否需要图"的判断必须显式做出并记录。
