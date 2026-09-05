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
