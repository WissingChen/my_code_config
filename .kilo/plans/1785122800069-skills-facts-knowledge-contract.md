# 技能组完善计划：事实红线 + 知识管理技能 + 直白表达

## 目标

1. 所有技能输出遵守事实红线：区分事实/推测，推测必须显式标注，禁止基于猜测作确定性回复。
2. 新增独立技能 `knowledge_keeper`：论文/资料检索先查本地、结果必落库、记录查询日志，避免重复检索触发 API 封禁。
3. 所有技能的回复与文档遵守直白表达规则：结论先行、术语必解释、禁套话。

## 已确认的决策

- 知识库位置：**仅项目级** `.kilo/knowledge/papers/`（沿用 research_manager 现有结构）。
- 全局规则落点：**每个 SKILL.md 内嵌同一份「输出契约」块**（agent 只加载单个技能，00-overview 不作依赖）。
- 新技能边界：**独立技能 + 委托**。research_progress Gate 2 的检索动作改为委托给 knowledge_keeper。

## 任务清单

### 1. 起草「输出契约」块（所有技能共用，约 6 行，英文，与现有技能风格一致）

内容要点：

- Label every claim as **fact** (with source) or **speculation** (explicitly marked, e.g. `[speculation]`). Never state speculation as fact — this is a hard red line.
- Plain language: conclusion first; explain any jargon in one short sentence on first use; no filler phrases or padding; prefer tables/lists over prose when it aids scanning.

### 2. 将输出契约嵌入 7 个现有 SKILL.md

在每个技能开头（frontmatter 之后、正文第一节之前）插入同一契约块：

- `research_manager/SKILL.md`
- `research_progress/SKILL.md`
- `experiment_manager/SKILL.md`
- `result_analysis/SKILL.md`
- `result_visualization/SKILL.md`
- `write_md/SKILL.md`
- `academic-paper-writing/SKILL.md`

注意 research_progress 第 6 节已有 "Distinguish fact / inference / speculation"，合并去重，以契约为准。

### 3. 新建 `knowledge_keeper/SKILL.md`（≤150 行，遵守 research_manager 预算）

frontmatter：

- name: `knowledge_keeper`
- description 触发词：检索论文/资料、查文献、"这篇论文讲什么"、保存/总结到知识库。

正文协议（核心流程）：

1. **本地优先**：任何 API/web 检索前，先 grep `.kilo/knowledge/papers/` 并查 `00-query-log.md`。命中则直接复用并注明来源为本地缓存。
2. **查询日志**：`knowledge/papers/00-query-log.md` 记录每次 API 查询：日期、查询词、数据源（arXiv/Semantic Scholar）、结果数、产出的笔记文件。相同/高度相似查询在 **7 天内** 不重复调 API，直接引用日志中的旧结果并标注检索日期。
3. **落库义务**：任何被实际使用（引用进回复/文档）的论文必须当场存为笔记 `author-year-title.md`，按 arXiv ID/DOI 去重；禁止"只检索不落库"。
4. **笔记模板**（最小字段）：标题/作者/年份/链接、一段话讲清结论与证据强度、与本项目哪个方向相关、关键可复用点（方法/数据集/结论）。禁止堆砌摘要原文。
5. **索引**：`knowledge/papers/00-overview.md` 在超过 5 篇后建立/更新（沿用 research_manager 第 4 节规则）。
6. 遵守输出契约；文件写入前需用户确认（与 research_progress 第 8 节一致）。

### 4. 修改 `research_progress/SKILL.md` Gate 2

- 检索动作改为：加载/委托 `knowledge_keeper` 执行本地检索 + API 查询 + 落库。
- research_progress 自身只保留 gap 判断逻辑（直接相关工作是否存在、差异分析）。
- 删除其中与 knowledge_keeper 重复的落库描述，改为指针引用。

### 5. 更新交叉引用

- `00-overview.md`：技能清单表加 `knowledge_keeper` 行；交叉引用矩阵加一行/一列；委托指南加"查论文/资料检索"条目；设计原则加一条"检索必落库"。
- `research_manager/SKILL.md` 第 8 节委托表加 `knowledge_keeper` 行；knowledge 命名规则处补充查询日志文件。

## 验证

1. 契约文本在 8 个 SKILL.md 中逐字一致（diff 检查）。
2. knowledge_keeper/SKILL.md ≤150 行；触发词能覆盖"查文献/总结论文/存知识库"场景。
3. 模拟场景走查：用户问"查一下 X 方向的文献"→ knowledge_keeper 先查日志和本地 → 无命中才调 API → 结果落库 + 写日志。
4. 模拟场景：7 天内重复同一查询 → 不调 API，复用日志结果。
5. research_progress Gate 2 中不再含具体检索/落库步骤，仅有委托指针。

## 风险与注意

- 契约块冗余是有意为之（保证单技能加载时生效）；后续修改契约需同步 8 处，计划完成后在 00-overview 设计原则中注明这一点。
- 7 天去重窗口为推荐默认值，写入技能时标注可按需调整。
- 不改动任何技能的核心业务逻辑，仅加契约块和委托指针（符合最小改动原则）。
