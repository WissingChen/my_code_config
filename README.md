# Research Skill Family 使用指南

一套覆盖科研全生命周期的 9 技能组，位于 `my_skills/`。核心理念：**先收敛再动手，价值而非成败决定 checkpoint，实验分支永不直接合并，最终交付物永远是一份图文并茂、证据可追溯的 REPORT.md**。

## 技能清单

| 技能 | 职责 | 触发词示例 |
|------|------|-----------|
| `research_manager` | 目录结构、状态转换、归档、**状态汇报** | "初始化项目"、"归档"、"汇报一下进展" |
| `research_progress` | 想法收敛（三门评估） | "我有个想法"、"这个方向值得做吗" |
| `knowledge_keeper` | 文献检索与知识库落库 | "查一下相关文献"、"这篇论文讲什么" |
| `experiment_manager` | 实验分支生命周期、运行报告、产物卫生 | "开始实验"、"跑第 3 次"、"关闭这个方向" |
| `result_analysis` | 统计分析与证据判断 | "分析一下这批数据"、"该 kill 还是 continue" |
| `result_visualization` | 图表、流程图、论文配图 | "画个图"、"出一张流程图" |
| `write_md` | Markdown 排版与可读性 | "美化一下这份文档" |
| `academic-paper-writing` | 论文写作与润色 | "写 Introduction"、"润色这一段" |
| `slide_deck` | HTML 展示页（代替 PPT） | "做个展示"、"生成 slides"、"代替 PPT" |

技能按需加载：基础层 + 1–2 个相关技能即可，不必全部启用。

## 目录约定（`.kilo/`）

```
.kilo/
├── global.md      # 全局指针层（≤80 行）：目标、四目录索引、backlog
├── proposal/      # 评估中/就绪的方向：proposal/NN-slug/
├── project/       # 进行中的方向（只存在于 exp/NN-slug 实验分支上）
├── archive/       # 已关闭方向：archive/YYYY-MM-DD-NN-slug/
├── reports/       # 生成的状态快照：YYYY-MM-DD-status.md
└── knowledge/     # 文献笔记 + 查询日志
```

## 典型流程

### 1. 提出并收敛一个想法

```
你："我有个想法：用 X 方法解决 Y 问题，值得做吗？"
```

`research_progress` 执行三门评估：

1. **问题值得讨论吗**——挑战提问框架，问错了会直接指出
2. **空白真实吗**——委托 `knowledge_keeper` 检索（本地优先、结果必落库），基于证据判断
3. **就绪度**——提案需包含：问题、文献空白、假设、可证伪预测、kill 准则、晋升准则、最小可行实验、对照、可行性、产物保留计划

产出：`ready` / `evaluating` / `rejected`，就绪提案写入 `proposal/NN-slug/experiment-plan.md`。

### 2. 开始实验

```
你："GO，开始做这个方向。"
```

`experiment_manager` 创建 `exp/NN-slug` 分支（优先独立 worktree），在实验分支上把方向从 `proposal/` 移到 `project/`。**主分支上方向仍在 proposal/ 中**——失败时探索性代码随分支丢弃，不污染主线。

### 3. 实验循环

每次运行编号 `ENN`，流程固定：

1. 尽量只改一个受控因子
2. `result_analysis` 解读证据，`result_visualization` 出图
3. 产出图文 `ENN-experiment-report.md`
4. 过**价值门**：

| 价值 | 含义 | 动作 |
|------|------|------|
| `informative` | 实质更新假设或决策 | 原子 checkpoint |
| `reusable` | 产出方向无关的可复用资产 | 原子 checkpoint |
| `none` | 无效/冗余/决策中性 | 不提交，记录排除原因并清理输出 |

### 4. 关闭方向

- **证伪**：综合所有有价值运行报告为 `REPORT.md`，只把报告包应用回主分支 `archive/`，不合并探索性代码
- **验证**：从目标 base 建干净的 `promote/NN-slug` 分支，只挑有效实现 + 测试 + 最小配置 + 报告包，合并 promote 分支（**永远不直接合并 exp 分支**）
- **转向（pivot）**：旧假设归档为 `superseded`，新建 proposal ID，不静默改写历史

### 5. 状态汇报

```
你："帮我整理一份项目进展汇报。"
```

`research_manager` 生成 `.kilo/reports/YYYY-MM-DD-status.md`，包含：

- 本期结论（≤3 行）
- 当前规划（各 evaluating/ready 方向状态）
- 进行中进展（最新 ENN 判定、距 kill/晋升准则的距离——数据从实验分支上的运行报告拉取）
- 本期关闭方向及教训
- 下期计划与风险

快照是**生成物，永不手工维护**；相邻两份直接 diff 即可回答"和上次比有什么变化"。

### 6. 生成展示页（HTML 代替 PPT）

```
你："把这个项目做成一个 HTML 展示页，要有动机、贡献、方法、实验结果。"
你："只展示方法和实验结果两部分。"
```

`slide_deck` 生成单个自包含 HTML 文件（默认 `.kilo/reports/YYYY-MM-DD-deck.html`）：

- **横板翻页**：`←`/`→` 方向键 + 屏幕按钮，带页码 `n / N`
- **自包含**：CSS/JS 全部内联，无 CDN 无框架；图片默认 base64 嵌入，单文件拷走即可放映
- **可打印**：浏览器打印即每页一张幻灯片，导出 PDF 代替 PPT 讲义
- **内容可追溯**：每个带数字的幻灯片页脚标注来源工件（experiment-plan、REPORT.md、ENN 报告），结尾附来源清单页；新图表委托 `result_visualization`，统计结论委托 `result_analysis`——展示页不创造内容，只重编码已批准的证据
- 生成前先给出幻灯片大纲供确认；底层工件更新后重新生成而非手改
- **风格可持续调整**：所有样式集中在文件顶部一处 `:root` CSS 变量块中，改样式只动这一处；风格按方法论迭代（层次来自对比、颜色只表义、一致性优先、无信息装饰必删），不锁死固定主题

## 输出契约（所有技能共同遵守）

- 每个论断标注为 **fact**（附来源）或 **speculation**（显式标记如 `[speculation]`）——把推测说成事实是红线
- 直白表达：结论先行；术语首次出现用一句话解释；不写填充句；优先表格和列表

## 关键边界

- **Git 变更需显式授权**：commit、删分支、合并都要你确认
- **产物白名单制**：Git 只收小决策表、最小配置、分析脚本、最终图；checkpoint、缓存、数据副本、完整日志一律排除，大产物走外部 manifest 追踪
- **文献只经 `knowledge_keeper`**：检索一次必落库，禁止重复检索和编造引用
- **状态转换所有权唯一**：目录移动、归档只由 `research_manager`（或其委托的 `experiment_manager`）执行
- **任何技能不得静默改写另一技能的科学判断**

## 文件位置

```
my_skills/
├── 00-overview.md            # 技能组总览（先读这个）
├── research_manager/SKILL.md
├── research_progress/SKILL.md
├── knowledge_keeper/SKILL.md
├── experiment_manager/SKILL.md
├── result_analysis/SKILL.md
├── result_visualization/SKILL.md
├── write_md/SKILL.md
├── academic-paper-writing/SKILL.md
└── slide_deck/SKILL.md
```
