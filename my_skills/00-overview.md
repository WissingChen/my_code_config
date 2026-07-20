---
title: "技能组总览 — Research Skill Family"
last_updated: "2026-07-20"
---

# 技能组总览

> Related: [research_manager](research_manager/SKILL.md), [research_progress](research_progress/SKILL.md), [experiment_manager](experiment_manager/SKILL.md), [result_analysis](result_analysis/SKILL.md), [result_visualization](result_visualization/SKILL.md), [write_md](write_md/SKILL.md), [academic-paper-writing](academic-paper-writing/SKILL.md)

## 0. 一句话定位

7 个技能覆盖研究全生命周期：收敛想法、执行实验、解析证据、可视化、表达文档、成稿论文。

## 1. 技能清单

| 技能 | 角色 | 触发词 |
|------|------|--------|
| `research_manager` | 目录与研究状态 | "初始化项目"、"归档"、"建文档" |
| `research_progress` | 方向收敛与三门 | "有个想法"、"这个方向怎么样"、"查文献" |
| `experiment_manager` | 实验执行与报告组装 | "开始实验"、"跑第 N 次"、"关闭方向" |
| `result_analysis` | 统计分析与证据判断 | "分析数据"、"Kill/Pivot/Continue" |
| `result_visualization` | 图表与流程图 | "画图/plot"、"流程图"、"出图" |
| `write_md` | 可读性排版 | "排版"、"美化文档"、"加盒子" |
| `academic-paper-writing` | 论文写作 | "写论文"、"润色"、"改 Introduction" |

## 2. 标准生命周期

| 状态 | 位置 | 所有者 | 转换事件 |
|---|---|---|---|
| Evaluating | `proposal/NN-slug/` | `research_progress` 推荐 | 通过或失败三门 |
| Ready | `proposal/NN-slug/` | `research_manager` 记录 | 用户 GO 开始实验 |
| Active | `project/NN-slug/` on `exp/NN-slug` | `experiment_manager` 执行 | 继续、转向、证伪、验证 |
| Rejected/Falsified/Validated/Superseded/Abandoned | `archive/YYYY-MM-DD-NN-slug/` | `research_manager` 应用 | 最终报告为主交付物 |

实验循环：每次 `ENN` 跑完先形成 `ENN-experiment-report.md`，通过价值门后再决定是否 checkpoint。关闭方向时综合为一份图文并茂的 `REPORT.md`。

## 3. 交叉引用矩阵

| 被引 →<br>引用 ↓ | manager | progress | experiment | analysis | visualization | write_md | academic |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| research_manager | — | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| research_progress | ✓ | — | handoff | — | — | — | — |
| experiment_manager | ✓ | ✓ | — | ✓ | ✓ | ✓ | — |
| result_analysis | ✓ | — | ✓ | — | handoff | — | — |
| result_visualization | ✓ | — | ✓ | ✓ | — | — | ✓ |
| write_md | — | — | ✓ | — | — | — | ✓ |
| academic-paper-writing | ✓(citation) | — | — | — | ✓ | — | — |

## 4. 委托指南

| 请求领域 | 加载技能 |
|----------|----------|
| 课题收敛、研究想法论证 | `research_progress` |
| 开始/管理/关闭实验、生成报告 | `experiment_manager` |
| 统计推断、证据判断 | `result_analysis` |
| 数据图表、流程图、论文配图 | `result_visualization` |
| 文档排版、报告可读性 | `write_md` |
| 论文写作、稿件打磨 | `academic-paper-writing` |

## 5. 设计原则

1. **Manager owns research state**: 目录移动、归档、状态转换只能由 `research_manager` 或它委托的 `experiment_manager` 执行。
2. **Experiment value, not success, determines checkpoints**: 价值为 `informative` 或 `reusable` 才 checkpoint；`none` 只记录排除原因。
3. **Experiment branches are never merged directly**: 失败方向只返回最终报告包；成功方向通过干净的 `promote/NN-slug` 分支进入主线。

可视化边界：

- `result_analysis` 决定数字支持什么、不支持什么；
- `result_visualization` 决定如何无失真地编码这些数字；
- `experiment_manager` 决定是否保留该产物。

按需叠加：基础层 + 1–2 个技能即可。图只在显著改善解释时才绘制。
