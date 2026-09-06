# 文件模板

`research_manager` 管的每个文件一份模板。骨架里 `<尖括号>` 是待填内容，填写指导写在每节开头；实例化时把指导忘掉，只留内容。

不归本技能管的文件只留指针：`experiment-plan.md` → `research_progress` §9；`ENN-experiment-report.md` 和 `REPORT.md` → `experiment_manager` §4–5；知识笔记 → `knowledge_keeper`。

## 1. 项目根 AGENTS.md

模板是独立文件 `references/AGENTS_template.md`。复制为项目根 `AGENTS.md`，由项目所有者填写维护，agent 严格只读。

## 2. .kilo/global.md（≤60 行）

纯索引：只放目录和指针。不写目标、规则、解释——那些归项目根 `AGENTS.md`。

```markdown
# 项目索引

## 方向
- 评估中: [NN-slug](proposal/NN-slug/00-overview.md)
- 进行中: [NN-slug](project/NN-slug/00-overview.md)
- 已归档: archive/（按 YYYY-MM-DD-NN-slug 目录）

## 进展
- TODO: [TODO.md](TODO.md)
- 最新状态快照: [reports/YYYY-MM-DD-status.md](reports/YYYY-MM-DD-status.md)

## 知识库
- [knowledge/](knowledge/)（查询日志: knowledge/papers/00-query-log.md）
```

## 3. .kilo/TODO.md（≤150 行）

项目进展唯一来源，三层树：主线（锁定，只有用户能改）→ 大阶段（来自 proposal，状态变化才更新）→ 实现方案（随实验证据增删换，每次改动在回复里说明原因）。只放链接，不复制方向文件的内容。

```markdown
# TODO

- 主线：<一句话中心问题>
  - S1 <阶段名> → [方向概览](project/NN-slug/00-overview.md)
    - 当前方案：<现阶段做法>
  - S2 <阶段名> → [方向概览](proposal/NN-slug/00-overview.md)
    - 当前方案：<现阶段做法>
```

## 4. 方向 00-overview.md（≤150 行，proposal/project 通用）

只记**当前状态**，改写不追加；历史留在运行报告里。某节确实没有内容就写"无"，不许填套话。

```markdown
# NN-slug 方向概览

- 状态: 评估中 | 卡住 | 通过 | 进行中
- 主要问题: <一句话>
- 主要假设: <当前核心假设>
- 主要矛盾: <当前最阻塞决策的矛盾>
- 当前证据: <链接到运行报告/实验计划 + 一句话>
- 最大不确定性: <当前排序第一的不确定性>
- 下一步决定: <做什么、由什么结果触发>
- 暂存的问题: <新想法，不自动激活>
- 被推翻的假设: <假设 → 推翻它的证据链接>
```

## 5. archive/YYYY-MM-DD-NN-slug/SUMMARY.md

短指针，不复制报告内容。

```markdown
# NN-slug 归档摘要

- 结局: 否决 | 证伪 | 验证通过 | 被取代 | 放弃
- 一句话结论: <结论>
- 终版文档: [REPORT.md](REPORT.md)（没进过实验的方向指向 experiment-plan.md）
- 教训: <1-3 条>
```

## 6. .kilo/reports/YYYY-MM-DD-status.md

只生成、不手维护；每个说法都要能指到已存在的来源。生成的快照不受行数预算限制。

```markdown
# YYYY-MM-DD 状态快照

## 头条
<≤3 行概括本期>

## 在评方向
- NN-slug: <状态 + 一句话，来自 proposal/NN-slug/00-overview.md>

## 进行中的进展
- NN-slug: <最近一次 ENN 的判定、离停手/做成标准的距离>

## 本期结束的方向
- NN-slug: <结局 + 教训，来自 archive/*/SUMMARY.md>

## 下一步和风险
- <待办（TODO.md）加判断>
```
