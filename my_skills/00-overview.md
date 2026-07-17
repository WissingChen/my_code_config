---
title: "技能组总览 — Research Skill Family"
last_updated: "2026-07-18"
---

# 技能组总览

> Related: [research_manager](research_manager/SKILL.md), [research_progress](research_progress/SKILL.md), [result_analysis](result_analysis/SKILL.md), [write_md](write_md/SKILL.md), [academic-paper-writing](academic-paper-writing/SKILL.md)

## 0. 一句话定位

5 个技能覆盖研究全生命周期：收敛想法、解析证据、表达文档、成稿论文。

## 1. 技能清单

| 技能 | 角色 | 触发词 |
|------|------|--------|
| `research_manager` | 骨架与目录 | "初始化项目"、"归档"、"建文档" |
| `research_progress` | 方向收敛 | "有个想法"、"这个方向怎么样"、"查文献" |
| `result_analysis` | 证据解析 + 出图 | "分析数据"、"画图/plot"、"Kill/Pivot/Continue" |
| `write_md` | 可读性排版 | "排版"、"美化文档"、"加盒子" |
| `academic-paper-writing` | 论文写作 | "写论文"、"润色"、"改 Introduction" |

## 2. 标准工作流

| 阶段 | 加载技能 | 产出 |
|------|----------|------|
| 1. 课题收敛 | `research_manager` + `research_progress` | `proposal/` 文档 |
| 2. 实验设计 | `research_progress` | `proposal/04-milestones.md` 含假设表 |
| 3. 跑实验 | 用户自行执行 | `project/` 下数据 |
| 4. 结果分析 | `research_manager` + `result_analysis` | 分析报告 + 图表 |
| 5. 论文撰写 | `academic-paper-writing` | 论文草稿 |

## 3. 交叉引用矩阵

| 被引 →<br>引用 ↓ | manager | progress | analysis | write_md | academic-paper-writing |
|:---:|:---:|:---:|:---:|:---:|:---:|
| research_manager | — | ✓ | ✓ | ✓ | ✓ |
| research_progress | ✓ | — | ✓(handoff) | — | — |
| result_analysis | ✓ | — | — | — | — |
| write_md | — | — | ✓ | — | — |
| academic-paper-writing | ✓(citation) | — | — | — | — |

## 4. 委托指南

| 请求领域 | 加载技能 |
|----------|----------|
| 课题收敛、研究想法论证 | `research_progress` |
| 实验结果分析、假设检验 | `result_analysis` |
| 统计绘图、流程图绘制 | `result_analysis` |
| 文档排版、视觉呈现 | `write_md` |
| 论文写作、稿件打磨 | `academic-paper-writing` |

## 5. 设计原则

- **骨架轻**：`research_manager` 只定义目录和硬预算。
- **先证伪**：`research_progress` 和 `result_analysis` 都强调 kill criteria。
- **分析必须出图**：`result_analysis` 承担原 visualize 的绘图职责。
- **按需叠加**：基础层 + 1–2 个技能即可。
