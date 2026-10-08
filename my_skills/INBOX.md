# 技能组改进收件箱

`skill_rsi` 的待审提议池。每条提议经用户批准后落地，落地或拒绝后标记状态但不删除。

格式见 `skill_rsi/SKILL.md` §2。顺序：最新在前（新提议插到文件头部）。

## 2026-10-08 research_progress 形式大于内容

来源: 用户审查技能组（2026-10-08 全组审阅）
证据: 用户指出 research_progress "形式大于内容"。审查发现三套重叠的不确定性记账装置：§1 四标签（想法/假设/预期/证据）、§4 箭头状态（已验证/有依据/猜测/不知道）、§5 猜想清单打分，都在管同一件事但没说清关系；"主线任务"节 7 条是三次补丁堆出来的纪律条款；§9 把六项输出写成每次必填的章节格式，不管讨论深浅
建议: 三套装置合并——猜想清单为唯一账本，箭头状态和四标签说明是它的投影而不是独立系统；§9 六项从"必须输出的章节"降为"必须能回答的问题"；主线节压缩；保留真正有内容的 §2 三种死法、§5 优先级打分、§6 决策驱动实验
类型: 改正文
影响面: research_progress
状态: 已落地 2026-10-08（主线节 7 条压到 4 条；§1 加"账本只有一本"说明；§9 六项降为必答问题；委托画链图改硬条件）

## 2026-10-08 术语统一：元目录/工作区 + research_manager 加清理和迁移能力

来源: 用户直接要求
证据: 用户规定以后 `.kilo` 文件夹统称"元目录"、整个项目文件夹统称"工作区"；research_manager 只有管理归档指导，没有清理能力，且清理前必须先出报告、用户确认后才执行；还需要把旧版元目录升级到新版的功能
建议: (1) 全组术语扫荡：prose 里用"元目录/工作区"，字面路径 `.kilo/` 不动；波及 research_manager、research_progress、knowledge_keeper、experiment_manager、result_analysis、write_md、00-overview.md、README.md、AGENTS_template.md。(2) research_manager 加"清理"节：两阶段——先出清理报告（候选 + 原因 + 拟处置：归档/删/合并/留），用户逐项确认后才执行；删除需逐项明确批准；原始科学证据不删（沿用 §7 定义）。(3) 加"元目录迁移"节：元目录引入版本标记（global.md frontmatter 或 VERSION 文件），references/meta-migrations.md 记录各版结构差异和迁移步骤，迁移同样报告先行、只加不删
类型: 改正文 + 新reference
影响面: research_manager 为主；术语波及全组
状态: 已落地 2026-10-08（§1 加术语定义；新增 §8 清理（报告先行、逐项确认）和 §9 元目录版本与迁移；新建 references/meta-migrations.md；templates.md 的 global.md 模板加 meta_version；术语扫到 knowledge_keeper、AGENTS_template、00-overview、README）

## 2026-10-08 result_visualization 调用不顺的根因与修法

来源: 用户审查 + 本次根因分析
证据: 用户说 result_visualization "需要强调才知道要用"。根因：技能的触发面只有 frontmatter 的 name+description（系统提示里只有这两项），现在的 description 是英文长句，对中文触发词（"画图/可视化"）匹配弱；委托链规则写在 00-overview.md §5（不是技能、会话中不会加载）和各委托方正文里，委托条件是软判断（"在图能暴露文字藏住的缺口时委托"），容易被跳过。Anthropic 官方博客也指出 name/description 是唯一触发面、要按实际触发情况迭代
建议: description 改中英混合触发词；委托方技能（experiment_manager、result_analysis、research_progress、write_md）把软条件改硬（"有数值比较就必须委托"）；报告自动叠加链从 00-overview 复制一行到每会话必读处（CLAUDE.md 或下游 AGENTS.md）
类型: 改正文
影响面: result_visualization、experiment_manager、result_analysis、research_progress、write_md、CLAUDE.md
状态: 已落地 2026-10-08（result_visualization/write_report/research_progress 的 description 加中文触发词；experiment_manager §2、result_analysis §9、research_progress §4 委托改硬条件；CLAUDE.md 加报告自动串联段）

## 2026-10-08 write_md 改名 write_report + 可读性强化

来源: 用户直接要求
证据: 用户要求 write_md 改名 write_report；调用仍不顺（根因同上一条）；产出堆砌细节与数据，要再提醒才改。用户要求：数据默认用图表展示、图表默认取信息密度最高的形式（不罗列表格和裸折线）、只有关键数字才放正文、用色块划分段落/区域功能方便快速定位。注意 §2"数值报告默认配图"和 result_visualization §1"现象优先/高密度"已在 2026-09-20 加过但仍不生效——根因是 write_md 经常根本没被加载（触发问题），不是规则缺失
建议: (1) 目录和 frontmatter 改名 write_md→write_report，同步 00-overview、experiment_manager §9、result_analysis §9、research_progress、README。(2) 新增规则：数据默认图表化；图表按信息密度排序选形式（合成图/热图/排序点图优先）；只有改变决定的关键数字进正文。(3) §4 区分"提示块"（警示、限量 ≤3）和"区块色带"（导航用、按语义色板固定配色、不计入提示块预算），并给色带的最小 HTML 样例
类型: 改正文
影响面: write_md（改名波及 00-overview、experiment_manager、result_analysis、research_progress、README）
状态: 已落地 2026-10-08（目录改名 write_report，12 处引用同步；§2 加"数据默认进图、正文只留关键数字""图按信息密度选形式"两条；§4 加区块色带（与提示块分开、固定配色、附 HTML 样例））

## 2026-10-08 plain_talk 加"克制"条款

来源: 用户直接要求
证据: 用户反馈 plain_talk 还不够：要克制、直白、直观、降低阅读门槛；不要罗列无关紧要的细节、不要过度防御、不要黑话包装。现技能管"怎么说"（黑话表、结构自检），缺"说多少"：无默认长度上限、无列举上限、无禁防御性内容的条款
建议: 加三条：默认 ≤3 句、用户说"详细说"才展开；列举只列会改变决定的项、默认 ≤5 条；禁防御性内容（不预先声明限制、不解释动机，除非影响决定）
类型: 改正文
影响面: plain_talk（Output Contract 若同步加条款则波及全部 12 处）
状态: 已落地 2026-10-08（新增 §3 克制：默认 ≤3 句、列举 ≤5 条且只列改变决定的项、禁防御性内容。Output Contract 未同步——plain_talk 每会话必加载，契约不动以免 12 处 churn）

## 2026-10-08 GitHub 技能生态检查结论

来源: 用户要求检查 GitHub 相关技能是否有更新、能否优化本技能组
证据: anthropics/skills 近一个月提交几乎全是 claude-api 技能更新（模型名录、Managed Agents 文档），与研究技能组无关；docx/pdf/pptx/xlsx 文档技能不相关；agentskills.io 规范页三次请求超时，规范是否有新字段未验证；Anthropic 官方博客的技能编写建议（渐进式披露、按触发情况迭代 description、从失败使用中沉淀）本组已通过 references/ 分层和 skill_rsi 覆盖
建议: 无可直接引入的更新；唯一可借鉴点是"description 按实际触发情况迭代"，已并入上两条提议。本次仅记录，不改文件
类型: 卫生检查
影响面: 无
状态: 已落地 2026-10-08（无文件改动，仅记录结论）

## 2026-09-30 新增 pdf_export 技能（绕过插件直接导 PDF）

来源: 用户直接要求
证据: 用 Markdown Preview Enhanced 导 PDF 时，eBook(Calibre) 与 PDF(prince) 都不执行 JS，mermaid 流程图丢失；页面尺寸也无全局设置（Puppeteer 的 format、Calibre 的 paper-size 只能写每个文件的 front-matter，@page 全局 CSS 对 Puppeteer 无效）。用户要求改成技能直接生成。
建议: 新建 `pdf_export/`：脚本 `build_pdf.py` 用 headless Chromium `--print-to-pdf` 出 A4（`@page` 写在全局 `report_pdf.css`），mermaid 由浏览器渲染，图片 base64 内嵌；SKILL.md 含输出契约与渲染验证步骤。00-overview 与 README 计数 11→12、索引更新。
类型: 新技能
影响面: 全组计数（11→12 处契约同步不变，仅计数文案）、00-overview.md、README.md
状态: 已落地 2026-09-30（check_skills.sh 通过；在 `2026-09-30-gyn-data-processing.md` 上验证：5 页、A4、mermaid 与内嵌图正常）

## 2026-09-23 改动前后必须跑读数回归（policy_cesh prompt 改版引入 cf 归零）

来源: WorldAgent-Benchmark policy_cesh.py 优化轮
证据: 为省 tokens 改了决策 prompt 结构（brief 移出、观察换精简段），只验证了"tokens 降、结局不变"，没有复跑五项演绎读数。下一局 cf 从 0.414 归零——模型开始模仿新 prompt 的结构回填字段，cf 答题行为被改坏。且 lint 只查格式不查"有题未答"，坏输出合法通过。事后根因排查花了整整一轮（离线重放服务端时序才定位）。
建议: 拉取 AGENTS_template.md 到项目根目录作为 AGENTS.md，并在 Experiment Discipline 加两条：改动触及 prompt/模型接口时前后各跑读数对照；校验规则与协议强约束一一对应。同时该次教训的具体技术修复（lint 拒绝空 cf 答案、cf_questions 位置修正）已在项目代码落地。
类型: 改正文
影响面: 项目根 AGENTS.md（含模板本身是否同步，待用户定夺）
状态: 已落地 2026-09-23（用户指示拉模板到项目根并加条目；模板文件本身未改，是否回灌模板待定）

## 2026-09-23 CESH 会话流程偏好：先讨论定方案再动手、单折单模型、单局结论分级

来源: CESH/DESIGN.md 全周期会话（WorldAgent-Benchmark 项目）
证据: 本次会话中用户多次纠正与确认：(1) "我们先讨论，不要执行"——方案必须讨论清楚、用户说"可以试试"才动手；(2) "我都说了全部用deepseek-flash……不要给我自作主张"——模型/配置不得照抄文件现状，必须与用户确认；(3) "以后都跑单折就行……只用deepseek-flash，只跑一折"——实验协议以用户指令为准，覆盖文档旧协议（多折均值）；(4) "叽里咕噜说什么，给我说人话"——结论必须直白，机制层与效果层分开说（"解决了"="机制上成立且有证据" vs "效果未证"="病没出现药没机会显效"）；(5) 被测的是演绎不是通关——判定标准是"每分演绎读数花多少 tokens"，不是结局/步数
建议: 这类偏好是会话级+项目级的执行纪律，核心三条——先讨论后执行（方案经用户确认才落代码）、用户明示的配置/协议覆盖文件现状且改动要报告、结论按"机制已证/效果待证/纯噪声"分级不下超量结论——已由 plain_talk SKILL 覆盖大部分；项目协议部分（单折、单模型）属于 CESH/DESIGN.md §5 已落地。为避免技能膨胀，本条仅作记录供审查：若用户认为需要，可在 plain_talk 加一节"执行类任务的对话节奏"（讨论→确认→执行→汇报，每步等指令）
类型: 新reference（待用户定夺是否需要）
影响面: plain_talk（可选）、research_manager、全局 CLAUDE.md
状态: 已落地 2026-09-23（部分）——AGENTS_template.md Experiment Discipline 加两条（配置以所有者指定为准、单局结果分级），全局 CLAUDE.md §6 加"配置以用户指令为准"；plain_talk 对话节奏一节经用户审查后不加（现有规则已覆盖，避免膨胀）

## 2026-09-20 结果图信息密度低、凸显不出现象（result_visualization）

来源: result_visualization（同一场景）
证据: 用户指出"提及到画图但是又只会画折线图，信息密度太小""没够直观与美观，凸显不出现象，这个是结果可视化的技能的不足"；模式 A 的 plot_compare.py 曾把四张折线图重做成三张高密度图（总览合成/差异热图/组件热图），这个教训没有沉淀进技能
建议: result_visualization/SKILL.md §1 表补"矩阵比较、报告级总览、配对下降"三类形式，加"折线只用于有序变量趋势"限制和"现象优先"设计规则；plotting-reference.md §1 同步补行，新增现象优先设计条目（按效应排序、参考线、直接标注差距与离群、对比组高饱和其余压灰、热图 cell 带数值、多面板合成）与报告图三件套模式
类型: 改正文
影响面: result_visualization、plotting-reference.md
状态: 已落地 2026-09-20（用户当场指示）

## 2026-09-20 数据结果报告缺统计图（write_md 没把配图变成硬要求）

来源: write_md（WorldAgent-Benchmark 模式 B 报告更新）
证据: 更新 mode_b/report.md 时全文只有表格没有一张统计图，用户纠正"你得补上相关统计图，参考 mode a 的方式""写报告都不喜欢创建合理的统计图以更直观的方式可视化数据特点"。write_md §2 只写了"不许硬塞图"的防御面，没有"数值报告默认配图"的要求，§3 配图规划在实践中被整体跳过
建议: write_md/SKILL.md §2 加硬规则：含跨组比较/分布/趋势的数值报告默认配统计图，纯表格按缺件处理；§3 第一遍标为必做，候选图绑定要凸显的现象，给出最小图集模式（总览合成图 + 差异热图 + 排序比较图）
类型: 改正文
影响面: write_md
状态: 已落地 2026-09-20（用户当场指示"先更新我提及的两个技能"）

## 2026-09-18 国自然示意图禁止纯文字框，必须配细节丰富的图标

来源: result_visualization（phd_funding 项目摘要示意图）
证据: 第一版用纯几何图形+文字堆叠，用户两次纠正："全是字"、"参考这种样式"（给出插画级参考图：机械臂、档案夹、放大镜清单等多部件图标，深青/青/橙配色，正箭头深青、回流橙色）
建议: plotting-reference.md §4 后加小节：基金/项目示意图必须配插画级图标，三个来源（matplotlib 多部件矢量组合 / 网络检索素材内联 / 生图模型输出），附 fig11_abstract.py 为参考实现
类型: 改正文
影响面: result_visualization
状态: 已落地 2026-09-18（用户当场指示"更新技能"）；同日用户纠正归属——国自然示意图归 slide_deck 国自然基金风格模板，该小节已从 result_visualization 撤除，内容并入 `slide_deck/templates/国自然基金风格/STYLE.md` §5 图标段与 §6 QA 坑点

## 2026-09-18 iclr_write 并入 academic-paper-writing

来源: 用户直接要求
证据: WorldAgent-Benchmark 项目内的 `paper/skill/iclr_write/` 是单项目技能，内容为 ICLR 基准论文模板（章节骨架、摘要七句式、反 AI 腔清单、5 篇模板论文句式库），属于 academic-paper-writing 的场景差异，应进技能库复用。同次使用中用户两条纠正一并并入：成稿 prose 禁用冒号/分号/破折号（原规则只是"两个以上重写"）；"判官"类拟人化隐喻禁用
建议: 新建 `academic-paper-writing/references/scenario-iclr-benchmark.md`（场景文件，含升级后的反 AI 腔清单第 1、7 条）；模板来源论文库移为 `references/iclr-benchmark-papers.md`；SKILL.md References 表加两行；项目内技能目录删除，ch_v1.md 模板指针改指全局技能
类型: 新reference + 改正文
影响面: academic-paper-writing、WorldAgent-Benchmark 项目
状态: 已落地 2026-09-18（用户当场指示；check_skills.sh 全过）

## 2026-09-06 check_skills.sh 查不出悬空路径引用

来源: 本次修复 AGENTS_template.md 时发现
证据: SKILL.md 和 00-overview.md 引用"仓库根 AGENTS_template.md"对下游项目是悬空路径，但 check_skills.sh 第 3 项"references 链接完整"报 ok——只查了特定链接格式，没查正文里提到的文件路径是否真实存在
建议: 给 check_skills.sh 加一项：扫描 SKILL.md/overview 正文中以反引号标注、带 `/` 的相对路径，验证文件存在
类型: 卫生检查
影响面: check_skills.sh
状态: 已落地 2026-10-08（新增第 4 项：反引号包裹、含 / 的相对路径做存在性检查；跳过模板占位符和目录约定式写法）

## 2026-09-06 research_manager 补全文件模板

来源: 用户直接要求
证据: 用户指出 research_manager 应提供完整参考模板、每个文件都有指导；检查发现 AGENTS_template.md 在仓库根而技能引用的是"仓库根"，对下游项目是悬空路径，且没有任何文件模板
建议: 新建 `research_manager/references/templates.md`（global.md、TODO.md、方向 00-overview.md、SUMMARY.md、状态快照五份模板，REPORT.md/experiment-plan.md 只留指针）；`AGENTS_template.md` 从仓库根移入 `research_manager/references/` 并修正其 Context Discipline 与 §8 一致；SKILL.md 和 00-overview.md 的引用路径同步修正；SKILL.md 文末加 References 索引
类型: 新reference + 改正文
影响面: research_manager、00-overview.md
状态: 已落地 2026-09-06（用户当场批准，含移动模板到技能下的指示）

## 2026-09-06 experiment_manager 加"上下文卫生"

来源: 用户直接要求
证据: 用户反馈：experiment_manager 要管理整个项目的上下文；不是全部文档和内容都重要，关键不是信息多少而是信息干净，这是 harness 的关键。现有技能管分支和产物，但没有规定活跃上下文里放什么、清什么
建议: 在 `experiment_manager/SKILL.md` §2 运行循环后加一小节：活跃上下文只放四样——主线一句话、当前最主要矛盾、当前运行的冻结预期、最新收敛记录；历史运行细节、被排除的假设、旧日志只留文件指针不进上下文；`00-overview.md` 是当前状态文件，每次运行后改写而不是追加；一条信息留在活跃上下文的标准是"删掉它会改变下一步决定"，答不上就清出去
类型: 改正文
影响面: experiment_manager
状态: 已落地 2026-09-06（用户批准后落地；§2 末尾加"上下文卫生"段）

## 2026-09-06 research_progress 加"会话内主线锚定"

来源: 用户直接要求
证据: 用户反馈：research_progress 要牢记主线，不要把注意力全部放在局部任务中，不要顺着当前局部子任务跑偏。现有"主线任务"一节只规定开场读 TODO、支线提一句，缺少会话进行中被子任务拖走的约束
建议: 在 `research_progress/SKILL.md` "主线任务"一节加三条：(1) 每个子任务动手前一句话说清它服务主线的哪个判断，说不出就不做；(2) 子任务完成后回答"它推进了主线的哪个判断"，答不上等于跑偏，停下汇报；(3) 子任务不许再嵌套展开子任务，确有必要先回到主线重新确认
类型: 改正文
影响面: research_progress
状态: 已落地 2026-09-06（用户批准后落地；"主线任务"节加三条会话内锚定）

## 2026-09-05 TODO 成为会话入口 + README 同步

来源: 用户直接要求
证据: 用户裁定会话先读 TODO.md、由 TODO 指向方向文件；README 过时（9 技能、无 TODO、契约少三条、global.md 行数矛盾）
建议: `research_manager` §3 定义 TODO.md 三层树（主线→阶段→方案）为项目进展唯一来源；`research_progress` 主线任务节改为只读 TODO.md；两条通用收尾规则上收进 Output Contract（11 处同步）；overview 矩阵列名 gardener→skill_rsi；research_manager §9 委托表改为指向 overview §5；knowledge_keeper §6 删重复的深度规则、research_progress §3 改为指向 keeper §8；academic-paper-writing 2.5→3 起顺移、slide_deck 6.5→7、7→8
类型: 改正文
影响面: 全部技能、00-overview.md
状态: 已落地 2026-09-05

## 2026-09-05 单一事实源修复（四处重复维护）

来源: 用户要求全组审查"多个产物维护一件事"
证据: 审查发现：生命周期状态表在 overview §2 和 research_manager §1 各一份；实验价值/方向判定定义在 result_analysis §0 和 experiment_manager §2 各一份；"报告需要哪些图"由 result_analysis §9 和 write_md §3 各自规划；图渲染验收标准写在三个技能里
建议: 状态表只留 research_manager §1，overview §2 改指针；价值/判定定义收进 result_analysis §0（experiment_manager §2 只留动作）；配图规划合并为 write_md §3 第一遍维护的唯一一份（result_analysis §9 候选汇入、experiment_manager §4a 验收它）；渲染验收标准只留 experiment_manager §4a，result_visualization §3 和 write_md §3 第二遍改为指向
类型: 改正文
影响面: 00-overview.md、result_analysis、experiment_manager、write_md、result_visualization、README.md（价值表和报告生产流程同步改指针）
状态: 已落地 2026-09-05（用户当场批准；check_skills.sh 全过）

## 2026-09-05 TODO 归属调整 + 技能组冗余清理

来源: 用户 review 技能组后逐条确认
证据: 用户裁定 TODO 归 research_manager 创建维护、research_progress 只读；审查发现矩阵旧名 gardener、委托表两处维护、收尾规则散落 5 处、深度规则讲三遍、小节编号 2.5/6.5
建议: `research_manager` §3 定义 TODO.md 三层树（主线→阶段→方案）为项目进展唯一来源；`research_progress` 主线任务节改为只读 TODO.md；两条通用收尾规则上收进 Output Contract（11 处同步）；overview 矩阵列名 gardener→skill_rsi；research_manager §9 委托表改为指向 overview §5；knowledge_keeper §6 删重复的深度规则、research_progress §3 改为指向 keeper §8；academic-paper-writing 2.5→3 起顺移、slide_deck 6.5→7、7→8
类型: 改正文 + 卫生检查
影响面: 全部技能、00-overview.md
状态: 已落地 2026-09-05

## 2026-09-04 新增 plain_talk 技能 + 全组契约加两条

来源: 用户直接要求
证据: 用户反馈：黑话和长篇大论消耗注意力；agent 优化某个环节时跑偏、舍本逐末，车轱辘话掩盖主线
建议: 新建 `plain_talk/SKILL.md`（黑话替换表、发前自检，只管输出风格）；11 个 SKILL.md 的 Output Contract 同步加"禁黑话"一条；CLAUDE.md 加每次会话必加载 plain_talk；00-overview.md 索引更新。问题2（守主线）第一次误改 10 个技能，已按用户要求全部撤回，等用户指定实际跑偏的技能后再改
类型: 新技能 + 改正文
影响面: 全部技能（仅契约一条）、CLAUDE.md、00-overview.md
状态: 已落地 2026-09-04；问题2 于 2026-09-05 落地：只改 `research_progress`，新增"主线任务"一节（主线一句话写进 todo 首条并保持，除非用户要求改）

## 2026-08-31 首批（本次大重构的遗留项）

来源: 2026-08-31 全组重构
证据: review 时发现 frontmatter 英文 description 与中文正文词汇脱节；00-overview 矩阵部分单元格语义未逐格验证；卫生检查靠手工
建议: 已当场修复（description 词汇统一、矩阵修正、新增 check_skills.sh）
类型: 卫生检查
影响面: 全部技能
状态: 已落地 2026-08-31
