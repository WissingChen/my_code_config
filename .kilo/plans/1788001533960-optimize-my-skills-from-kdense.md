# 参考 K-Dense scientific-agent-skills 优化 my_skills 技能组

## 背景与已确认决策

- 调研基础：本仓库 `my_skills/`（9 技能，平均 108 行，规则密度高、几乎无 worked example）vs `.kilo/knowledge/repo/scientific-agent-skills/`（22 个相关技能，平均 293 行，强项是示例/模板/反模式清单/门禁判据）。
- **路线**：两阶段——Pass 1 全组格式对齐，Pass 2 逐技能补内容。
- **行数**：严格执行既有 ≤150 行/SKILL.md 预算；新增内容一律进 `references/`，正文在使用点内联指向（K-Dense progressive disclosure 模式）。
- **不引入** scripts/ 校验 CLI；重复内容（语义色板）改用单一事实源 + 指向解决。Output Contract 九处重复是刻意设计，不动。
- **Pass 2 范围**：全部 9 技能，顺序 = research_progress → experiment_manager → result_analysis → result_visualization → research_manager → knowledge_keeper → write_md → slide_deck → academic-paper-writing。

## 约束

- 保持现有风格：frontmatter 英文 description 含 "Load when…" 触发；正文机制英文、Output Contract 中文逐字一致；`## N.` 编号小节 + `§N` 跨节引用。
- 保留非标准 frontmatter 字段 `requires`；**不**新增 license/metadata/compatibility 等 K-Dense 分发字段（个人配置仓库无分发需求）。
- 只补文档与示例，不改变技能间委托关系的语义。
- 每个 SKILL.md 修改后仍 ≤150 行；超了就把细节下沉 references/。

## Pass 1：格式对齐（先做，一次完成）

1. **academic-paper-writing frontmatter 补齐**：description 改为 "Load when…" 触发句式 + 负向路由；加 `requires: research_manager`（与其他 7 个一致）。
2. **academic-paper-writing 章节编号化**：命名小节改为 `## 1.`–`## N.`，使 §N 引用体系可用。
3. **修正 00-overview.md 交叉引用矩阵**：knowledge_keeper 行补 research_progress（其 §7 引用 Gate 2）；write_md 行的 academic 标注与实际正文对齐（二选一：正文补互指，或矩阵删标注——倾向正文补互指，见 Pass 2 第 9 项）。
4. **语义色板单一事实源**：色板只保留在 `result_visualization/plotting-reference.md`；`result_visualization/SKILL.md` 与 `write_md/SKILL.md §4` 的内联色板替换为指向该文件的一行引用。
5. **description 负向路由补全**：检查 9 个 description 是否都有"不做什么/边界场景找谁"（K-Dense 新式四要素：功能边界/触发词/兄弟路由/否定边界），缺的补上；research_manager §9 委托表为权威路由表。

## Pass 2：内容补缺（按序执行，每技能独立可验）

### 1. research_progress（借鉴 hypothesis-generation、scientific-brainstorming、what-if-oracle）
- 新增 `references/gate-walkthrough.md`：一个方向完整过四门 Gate 的 worked example（含六项默认输出实例 + A/B/ambiguous→动作映射实例）。
- 正文补：Force Tier 划分判据（"小问题 vs 研究方向"）；Gate1 停止条件的优先规则；投机账本三项（投机度/影响/验证成本）的 1–3 标度定义。
- 借鉴 hypothesis-generation 的"对象区分表"形式，把 idea/assumption/prediction/evidence 标签定义钉成表。

### 2. experiment_manager（借鉴 pptx-posters hard gates、peer-review intake gate）
- 新增 `references/example-run-report.md`：一份完整运行报告实例（含 §4 schema 填充 + §4a 视觉审计记录实例）。
- §4a "open or screenshot-check" 具体化：直接引用 slide_deck §5 的 chromium 截图命令。
- ready proposal 15+ 项清单补"缺项降级路径"（缺哪些项 → blocked，缺哪些项 → 退回补写）。
- informative vs none 价值分类补 2–3 个边界示例。

### 3. result_analysis（借鉴 statistical-analysis、exploratory-data-analysis）
- 新增 `references/causal-chain-diagnosis.md`：因果链后四环（干预/机制/目标/价值）断裂的判别决策树 + 失败诊断表填写实例。
- §5 统计指导补一张"问题类型 → 分析思路"决策表（只写方法论路由，不绑定具体库）。
- §9 视觉审计补记录模板（候选/选中/拒绝三列表格）。
- 充分性检查三问补失败后的处理路径。

### 4. result_visualization（借鉴 scientific-visualization）
- `plotting-reference.md` 补：完整 handoff payload 示例（10 项字段填充实例）；大样本降采样、多图拼接规范。
- 借鉴其 Final review checklist 形式，把产物验收改成可勾选清单。

### 5. research_manager（借鉴 venue-templates currency rule）
- 新增 `references/lifecycle-trace.md`：一个方向从 Evaluating → Ready → Active → 归档（5 种结局各一段）的完整走查。
- 正文补：rejected/blocked 方向（未进实验）的归档责任人与路径；stale/duplicate 的判定判据；行数超限的处理流程。

### 6. knowledge_keeper（借鉴 paper-lookup、citation-management）
- 补：无 arXiv ID/DOI 论文的去重规则；Semantic Scholar/OpenAlex 限流/失败的降级路径（"fail visible, not plausible"——验证响应形状而非状态码）。
- 新增 `references/impl-facts-template.md`：实现级事实采集模板（衔接 §7 字段清单与笔记模板）。

### 7. write_md（借鉴 statistical-analysis APA 模板形态）
- 新增 `references/rewrite-examples.md`：语言层/结构层规则的 before/after 改写示例（反术语、30 秒扫读各 2–3 组）。
- 补：box vs 表格/引用的选用判据；§7 最小 HTML 报告骨架模板（放 references/）。

### 8. slide_deck（借鉴 latex-posters 硬限制表思路）
- §4 抓图协议补非 arXiv 场景（无 HTML 版会议的 PDF 直链/仅摘要页）处理路径。
- 补：20+ 页大 deck 的分块生成与检查指导；瑞士模板 593 行 HTML 加组件定位注释（改 template.html 注释，不加正文行数）。

### 9. academic-paper-writing（借鉴 scientific-writing 声明-证据绑定）
- 补：四个 reviewer 测试的应用示例（一个虚构段落走查）。
- 补：来自文献的定量声明追溯规则——必须链接 knowledge_keeper 笔记 ID（实验产物追溯规则的文献侧对应）。
- 与 write_md 补互指（稿件排版边界）。

### 收尾
- 更新 `00-overview.md`：交叉引用矩阵、设计原则中补 "references/ 渐进披露" 约定（SKILL.md ≤150 行、详细示例/模板下沉、使用点内联指向、文末 References 索引）。

## 验证（每个技能改完即做）

1. `wc -l` 确认 SKILL.md ≤150 行。
2. 确认 Output Contract 段落与改动前逐字一致。
3. 确认新增 references/ 文件在正文至少一处被指向；正文指向的路径全部存在。
4. description 触发条件仍与实际内容一致（改动机制后回读 frontmatter）。
5. 全部完成后重读 00-overview.md 交叉引用矩阵，确认与 9 个正文一致。

## 明确不做

- 不引入 scripts/、校验 CLI、license/metadata/compatibility frontmatter 字段。
- 不照搬 K-Dense 与特定 Python 库/API 绑定的内容（matplotlib、parallel.ai 等用法）。
- 不改变 Output Contract 九处重复的刻意设计。
- 不调整技能间委托关系语义，只补文档、示例、判据。
