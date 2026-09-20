# 技能组改进收件箱

`skill_rsi` 的待审提议池。每条提议经用户批准后落地，落地或拒绝后标记状态但不删除。

格式见 `skill_rsi/SKILL.md` §2。

## 2026-08-31 首批（本次大重构的遗留项）

来源: 2026-08-31 全组重构
证据: review 时发现 frontmatter 英文 description 与中文正文词汇脱节；00-overview 矩阵部分单元格语义未逐格验证；卫生检查靠手工
建议: 已当场修复（description 词汇统一、矩阵修正、新增 check_skills.sh）
类型: 卫生检查
影响面: 全部技能
状态: 已落地 2026-08-31

## 2026-09-04 新增 plain_talk 技能 + 全组契约加两条

来源: 用户直接要求
证据: 用户反馈：黑话和长篇大论消耗注意力；agent 优化某个环节时跑偏、舍本逐末，车轱辘话掩盖主线
建议: 新建 `plain_talk/SKILL.md`（黑话替换表、发前自检，只管输出风格）；11 个 SKILL.md 的 Output Contract 同步加"禁黑话"一条；CLAUDE.md 加每次会话必加载 plain_talk；00-overview.md 索引更新。问题2（守主线）第一次误改 10 个技能，已按用户要求全部撤回，等用户指定实际跑偏的技能后再改
类型: 新技能 + 改正文
影响面: 全部技能（仅契约一条）、CLAUDE.md、00-overview.md
状态: 已落地 2026-09-04；问题2 于 2026-09-05 落地：只改 `research_progress`，新增"主线任务"一节（主线一句话写进 todo 首条并保持，除非用户要求改）

## 2026-09-05 TODO 归属调整 + 技能组冗余清理

来源: 用户 review 技能组后逐条确认
证据: 用户裁定 TODO 归 research_manager 创建维护、research_progress 只读；审查发现矩阵旧名 gardener、委托表两处维护、收尾规则散落 5 处、深度规则讲三遍、小节编号 2.5/6.5
建议: `research_manager` §3 定义 TODO.md 三层树（主线→阶段→方案）为项目进展唯一来源；`research_progress` 主线任务节改为只读 TODO.md；两条通用收尾规则上收进 Output Contract（11 处同步）；overview 矩阵列名 gardener→skill_rsi；research_manager §9 委托表改为指向 overview §5；knowledge_keeper §6 删重复的深度规则、research_progress §3 改为指向 keeper §8；academic-paper-writing 2.5→3 起顺移、slide_deck 6.5→7、7→8
类型: 改正文 + 卫生检查
影响面: 全部技能、00-overview.md
状态: 已落地 2026-09-05

## 2026-09-05 TODO 成为会话入口 + README 同步

来源: 用户直接要求
证据: 用户裁定会话先读 TODO.md、由 TODO 指向方向文件；README 过时（9 技能、无 TODO、契约少三条、global.md 行数矛盾）
建议: `research_manager` §3 TODO 带方向文件链接、§8 开场顺序改为 AGENTS.md→TODO.md→跟链接；overview §3 同步；README 全面更新（11 技能、TODO 入口、契约补三条、文件清单补 skill_rsi/plain_talk）
类型: 改正文
影响面: research_manager、00-overview.md、README.md
状态: 已落地 2026-09-05

## 2026-09-05 单一事实源修复（四处重复维护）

来源: 用户要求全组审查"多个产物维护一件事"
证据: 审查发现：生命周期状态表在 overview §2 和 research_manager §1 各一份；实验价值/方向判定定义在 result_analysis §0 和 experiment_manager §2 各一份；"报告需要哪些图"由 result_analysis §9 和 write_md §3 第一遍各自规划；图渲染验收标准写在三个技能里
建议: 状态表只留 research_manager §1，overview §2 改指针；价值/判定定义收进 result_analysis §0（experiment_manager §2 只留动作）；配图规划合并为 write_md §3 第一遍维护的唯一一份（result_analysis §9 候选汇入、experiment_manager §4a 验收它）；渲染验收标准只留 experiment_manager §4a，result_visualization §3 和 write_md §3 第二遍改为指向
类型: 改正文
影响面: 00-overview.md、result_analysis、experiment_manager、write_md、result_visualization、README.md（价值表和报告生产流程同步改指针）
状态: 已落地 2026-09-05（用户当场批准；check_skills.sh 全过）

## 2026-09-06 research_progress 加"会话内主线锚定"

来源: 用户直接要求
证据: 用户反馈：research_progress 要牢记主线，不要把注意力全部放在局部任务中，不要顺着当前局部子任务跑偏。现有"主线任务"一节只规定开场读 TODO、支线提一句，缺少会话进行中被子任务拖走的约束
建议: 在 `research_progress/SKILL.md` "主线任务"一节加三条：(1) 每个子任务动手前一句话说清它服务主线的哪个判断，说不出就不做；(2) 子任务完成后回答"它推进了主线的哪个判断"，答不上等于跑偏，停下汇报；(3) 子任务不许再嵌套展开子任务，确有必要先回到主线重新确认
类型: 改正文
影响面: research_progress
状态: 已落地 2026-09-06（用户批准后落地；"主线任务"节加三条会话内锚定）

## 2026-09-06 experiment_manager 加"上下文卫生"

来源: 用户直接要求
证据: 用户反馈：experiment_manager 要管理整个项目的上下文；不是全部文档和内容都重要，关键不是信息多少而是信息干净，这是 harness 的关键。现有技能管分支和产物，但没有规定活跃上下文里放什么、清什么
建议: 在 `experiment_manager/SKILL.md` §2 运行循环后加一小节：活跃上下文只放四样——主线一句话、当前最主要矛盾、当前运行的冻结预期、最新收敛记录；历史运行细节、被排除的假设、旧日志只留文件指针不进上下文；`00-overview.md` 是当前状态文件，每次运行后改写而不是追加；一条信息留在活跃上下文的标准是"删掉它会改变下一步决定"，答不上就清出去
类型: 改正文
影响面: experiment_manager
状态: 已落地 2026-09-06（用户批准后落地；§2 末尾加"上下文卫生"段）

## 2026-09-06 research_manager 补全文件模板

来源: 用户直接要求
证据: 用户指出 research_manager 应提供完整参考模板、每个文件都有指导；检查发现 AGENTS_template.md 在仓库根而技能引用的是"仓库根"，对下游项目是悬空路径，且没有任何文件模板
建议: 新建 `research_manager/references/templates.md`（global.md、TODO.md、方向 00-overview.md、SUMMARY.md、状态快照五份模板，REPORT.md/experiment-plan.md 只留指针）；`AGENTS_template.md` 从仓库根移入 `research_manager/references/` 并修正其 Context Discipline 与 §8 一致；SKILL.md 和 00-overview.md 的引用路径同步修正；SKILL.md 文末加 References 索引
类型: 新reference + 改正文
影响面: research_manager、00-overview.md
状态: 已落地 2026-09-06（用户当场批准，含移动模板到技能下的指示）

## 2026-09-06 check_skills.sh 查不出悬空路径引用

来源: 本次修复 AGENTS_template.md 时发现
证据: SKILL.md 和 00-overview.md 引用"仓库根 AGENTS_template.md"对下游项目是悬空路径，但 check_skills.sh 第 3 项"references 链接完整"报 ok——只查了特定链接格式，没查正文里提到的文件路径是否真实存在
建议: 给 check_skills.sh 加一项：扫描 SKILL.md/overview 正文中以反引号标注、带 `/` 的相对路径，验证文件存在
类型: 卫生检查
影响面: check_skills.sh
状态: 待审

## 2026-09-18 iclr_write 并入 academic-paper-writing

来源: 用户直接要求
证据: WorldAgent-Benchmark 项目内的 `paper/skill/iclr_write/` 是单项目技能，内容为 ICLR 基准论文模板（章节骨架、摘要七句式、反 AI 腔清单、5 篇模板论文句式库），属于 academic-paper-writing 的场景差异，应进技能库复用。同次使用中用户两条纠正一并并入：成稿 prose 禁用冒号/分号/破折号（原规则只是"两个以上重写"）；"判官"类拟人化隐喻禁用
建议: 新建 `academic-paper-writing/references/scenario-iclr-benchmark.md`（场景文件，含升级后的反 AI 腔清单第 1、7 条）；模板来源论文库移为 `references/iclr-benchmark-papers.md`；SKILL.md References 表加两行；项目内技能目录删除，ch_v1.md 模板指针改指全局技能
类型: 新reference + 改正文
影响面: academic-paper-writing、WorldAgent-Benchmark 项目
状态: 已落地 2026-09-18（用户当场指示；check_skills.sh 全过）

## 2026-09-18 国自然示意图禁止纯文字框，必须配细节丰富的图标

来源: result_visualization（phd_funding 项目摘要示意图）
证据: 第一版用纯几何图形+文字堆叠，用户两次纠正："全是字"、"参考这种样式"（给出插画级参考图：机械臂、档案夹、放大镜清单等多部件图标，深青/青/橙配色，正箭头深青、回流橙色）
建议: plotting-reference.md §4 后加小节：基金/项目示意图必须配插画级图标，三个来源（matplotlib 多部件矢量组合 / 网络检索素材内联 / 生图模型输出），附 fig11_abstract.py 为参考实现
类型: 改正文
影响面: result_visualization
状态: 已落地 2026-09-18（用户当场指示"更新技能"）；同日用户纠正归属——国自然示意图归 slide_deck 国自然基金风格模板，该小节已从 result_visualization 撤除，内容并入 `slide_deck/templates/国自然基金风格/STYLE.md` §5 图标段与 §6 QA 坑点

## 2026-09-20 数据结果报告缺统计图（write_md 没把配图变成硬要求）

来源: write_md（WorldAgent-Benchmark 模式 B 报告更新）
证据: 更新 mode_b/report.md 时全文只有表格没有一张统计图，用户纠正"你得补上相关统计图，参考 mode a 的方式""写报告都不喜欢创建合理的统计图以更直观的方式可视化数据特点"。write_md §2 只写了"不许硬塞图"的防御面，没有"数值报告默认配图"的要求，§3 配图规划在实践中被整体跳过
建议: write_md/SKILL.md §2 加硬规则：含跨组比较/分布/趋势的数值报告默认配统计图，纯表格按缺件处理；§3 第一遍标为必做，候选图绑定要凸显的现象，给出最小图集模式（总览合成图 + 差异热图 + 排序比较图）
类型: 改正文
影响面: write_md
状态: 已落地 2026-09-20（用户当场指示"先更新我提及的两个技能"）

## 2026-09-20 结果图信息密度低、凸显不出现象（result_visualization）

来源: result_visualization（同一场景）
证据: 用户指出"提及到画图但是又只会画折线图，信息密度太小""没够直观与美观，凸显不出现象，这个是结果可视化的技能的不足"；模式 A 的 plot_compare.py 曾把四张折线图重做成三张高密度图（总览合成/差异热图/组件热图），这个教训没有沉淀进技能
建议: result_visualization/SKILL.md §1 表补"矩阵比较、报告级总览、配对下降"三类形式，加"折线只用于有序变量趋势"限制和"现象优先"设计规则；plotting-reference.md §1 同步补行，新增现象优先设计条目（按效应排序、参考线、直接标注差距与离群、对比组高饱和其余压灰、热图 cell 带数值、多面板合成）与报告图三件套模式
类型: 改正文
影响面: result_visualization、plotting-reference.md
状态: 已落地 2026-09-20（用户当场指示）
