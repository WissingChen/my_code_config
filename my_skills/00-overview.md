---
title: "技能组总览 — Research Skill Family"
last_updated: "2026-07-04"
status: "🟢 Stable"
---

# 技能组总览

> Related: [research_manager](research_manager/SKILL.md), [research_progress](research_progress/SKILL.md), [result_analysis](result_analysis/SKILL.md), [research_visualize](research_visualize/SKILL.md), [write_md](write_md/SKILL.md), [academic-paper-writing](write_paper/SKILL.md)

---

## 0. 一句话定位

**6 个技能覆盖研究全生命周期：从想法收敛到论文成稿，每个环节有专门的 Agent 角色驱动。**

---

## 1. 技能全景图

```
                         ┌──────────────────────────────────────┐
                         │         research_manager             │
                         │   目录体系 · 生命周期 · 委托指南      │
                         └────┬──────┬──────┬──────┬────────────┘
                              │      │      │      │
              ┌───────────────┘      │      │      └──────────────┐
              ▼                      ▼      ▼                      ▼
   ┌──────────────────┐   ┌──────────────┐  ┌──────────────┐  ┌──────────────┐
   │research_progress │   │result_analysis│  │  write_md    │  │ write_paper  │
   │   课题收敛       │──▶│   证据解析    │  │ 文档视觉呈现  │  │  论文写作审美 │
   │   (五步协议)     │   │   (五步协议)  │  │ (HTML盒子+    │  │  (语感+图表+  │
   └──────────────────┘   └──────┬───────┘  │  语义调色板)   │  │   引用伦理)   │
                                 │          └──────────────┘  └──────────────┘
                                 │ handoff: 可视化建议              ▲
                                 ▼                                 │
                        ┌──────────────────┐                       │
                        │research_visualize│───────────────────────┘
                        │   统计绘图 + 图表 │  生成论文级 PDF 矢量图
                        │ matplotlib/seaborn│
                        │  Mermaid + HTML   │
                        └──────────────────┘
```

<div style="border-left:4px solid #3498db;padding:12px 16px;margin:12px 0;background:#ebf5fb;border-radius:0 8px 8px 0;">
<div style="color:#3498db;font-weight:bold;margin-bottom:4px;">技能加载规则</div>
加载 <code>research_manager</code> 即可获得目录体系和委托指南。其他 5 个技能<b>按需叠加</b>，不要求全部加载。典型场景通常加载 2-3 个技能组合即可覆盖。
</div>

---

## 2. 技能清单

| 技能 | 角色 | 核心能力 | 依赖 | 触发词 |
|------|------|---------|------|--------|
| `research_manager` | 基础层 | `.kilo/` 目录体系、proposal→project→archive 生命周期、命名约定、00-overview.md、global.md | — | "初始化项目"、"归档"、"建文档" |
| `research_progress` | 课题收敛顾问 | 五步收敛协议：问题解构→类型分类→Gap分析文献搜索→致命质疑≥2→风险扫描 | research_manager | "有个想法"、"这个方向怎么样" |
| `result_analysis` | 证据解析顾问 | 五步解析协议：证据审计→竞争假设→置信度更新→闭环实验设计→结论裁决 | research_manager | "实验结果出来了"、"分析一下数据" |
| `research_visualize` | 可视化工具 | Mode 1: matplotlib/seaborn 统计绘图 / Mode 2: Mermaid 流程图+架构图 | research_manager | "画图"、"画架构图"、"plot" |
| `write_md` | 文档排版 | HTML div 语义盒子(8种)+架构图+语义调色板(7色) | — | "排版"、"美化文档"、"加盒子" |
| `academic-paper-writing` | 论文写作 | 叙事弧线、语感打磨、图表审美、消融实验规范、引用伦理、审稿人心理 | — | "写论文"、"改写 Introduction"、"润色" |

---

## 3. 标准工作流

### 3.1 完整研究链路（6 技能全流程）

| 阶段 | 加载技能 | 做什么 | 产出 |
|------|---------|--------|------|
| 1. 课题收敛 | research_manager + research_progress | 五步协议收敛想法，文献搜索 | `proposal/01-problem-definition.md` 等 |
| 2. 实验设计 | research_progress | 可证伪预测，里程碑规划 | `proposal/04-milestones.md`（含假设表） |
| 3. 跑实验 | （用户自行执行） | 训练、评估、采集数据 | `project/` 下实验数据和报告 |
| 4. 结果分析 | research_manager + result_analysis | 五步协议解析证据，裁决假设 | `project/NN-experiment-analysis-*.md` |
| 5. 可视化 | research_manager + research_visualize | 从分析结论生成图表、架构图 | `project/` 下 PDF/PNG/Mermaid 文件 |
| 6. 论文撰写 | academic-paper-writing | 写作审美驱动，引用归档 | 论文草稿，引用归档到 `knowledge/papers/` |

### 3.2 最小链路（仅分析实验）

```
research_manager → result_analysis → research_visualize
```

### 3.3 文档写作链路

```
research_manager → write_md（排版）→ academic-paper-writing（论文写作审美）
```

---

## 4. 交叉引用完整性

所有 6 个技能之间通过 Handoff 协议、跨技能引用段和 research_manager 委托指南形成有向连通图，无断链。

| 被引 →<br>引用 ↓ | manager | progress | analysis | visualize | write_md | academic-paper-writing |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| research_manager | — | ✓ | ✓ | ✓ | ✓ | ✓ |
| research_progress | ✓ | — | ✓(handoff) | ✓(full chain) | — | ✓(chain) |
| result_analysis | ✓ | ✓(handoff) | — | ✓(handoff) | — | — |
| research_visualize | ✓ | ✓(via analysis) | ✓ | — | ✓ | ✓ |
| write_md | ✓ | — | — | ✓ | — | — |
| academic-paper-writing | ✓(citation) | — | — | — | — | — |

<div style="border-left:4px solid #9b59b6;padding:12px 16px;margin:12px 0;background:#f5eef8;border-radius:0 8px 8px 0;">
<div style="color:#9b59b6;font-weight:bold;margin-bottom:4px;">委托指南（来自 research_manager §6）</div>
<table style="width:100%;border-collapse:collapse;">
<thead>
<tr style="border-bottom:2px solid #9b59b6;">
<th style="padding:8px;text-align:left;">请求领域</th>
<th style="padding:8px;text-align:left;">加载技能</th>
</tr>
</thead>
<tbody>
<tr style="border-bottom:1px solid #ddd;"><td style="padding:8px;">课题收敛、研究想法论证</td><td style="padding:8px;"><code>research_progress</code></td></tr>
<tr style="border-bottom:1px solid #ddd;"><td style="padding:8px;">实验结果分析、假设检验</td><td style="padding:8px;"><code>result_analysis</code></td></tr>
<tr style="border-bottom:1px solid #ddd;"><td style="padding:8px;">统计绘图、流程图绘制</td><td style="padding:8px;"><code>research_visualize</code></td></tr>
<tr style="border-bottom:1px solid #ddd;"><td style="padding:8px;">文档排版、视觉呈现</td><td style="padding:8px;"><code>write_md</code></td></tr>
<tr><td style="padding:8px;">论文写作、稿件打磨</td><td style="padding:8px;"><code>academic-paper-writing</code></td></tr>
</tbody>
</table>
</div>

---

## 5. research 链路 vs writing 链路

```
research 链路（纵向，按阶段推进）:
  research_progress ──▶ result_analysis ──▶ research_visualize
     课题收敛              证据解析              可视化

writing 链路（横向，按需加载）:
  write_md（文档排版）+ academic-paper-writing（论文审美）── 随时叠加到任何阶段
```

两条链路通过 `research_manager` 的目录体系和委托指南统一调度，分歧仅在加载时机。

---

## 6. 设计原则

| 原则 | 体现 |
|------|------|
| **单一职责** | 每个技能只做一件事：收敛、分析、画图、排版、写作 |
| **Handoff 驱动** | 技能间通过明确的数据格式传递（假设表、可视化建议段） |
| **按需叠加** | 不强制加载全部 6 个技能，基础层 + 2-3 个按需技能即可 |
| **基础层统一** | research_manager 提供目录体系、命名约定、委托指南 |
| **写作为审美，不做工具** | academic-paper-writing 只讲写作品味，不嵌入工具引用 |
| **正交互补** | research_visualize + write_md 各有侧重，互不替代 |
