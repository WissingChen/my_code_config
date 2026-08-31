---
name: skill_rsi
description: Skill-family self-improvement inbox. Load when using any skill reveals friction, a user correction worth persisting, a missing scenario or reference, or a cross-skill inconsistency. Records improvement proposals and applies them only after user review. Never silently edits skills.
requires: research_manager
---

## Output Contract

- 先说结论，再给必要依据和下一步。
- 默认短句和常用词；术语只在更准确时用，首次出现直接解释。
- 内部状态、流程和检查表默认不展示；只有影响决定或用户明确要求时才展开。
- 外部事实、论文结论和数字附来源；不确定的直接写"尚未验证"或"我推测"，不给每句话机械加事实/猜测标签。
- 一段能说清就不用表格；独立要点用列表；只有横向比较才用表格。
- 不写套话、廉价肯定、重复总结和固定收尾。

# Skill RSI — 技能组在用中长大

让每个技能在使用中暴露的问题变成技能组的改进，而不是消失在对话里。**改动必须先提出来、用户检查后才落地；绝不顺手改技能文件。**

## 1. 什么时候记录

使用中遇到以下情况，先记一条改进提议，再继续手头的活：

- 用户纠正了说法、黑话、流程——这次的纠正大概率下次还适用；
- 某条规则被绕过，或被证明是形式主义；
- 缺一个场景或 reference（新的写作场景、新的失败模式、新的工具链）；
- 发现跨技能不一致、悬空引用、词汇漂移；
- 同一类手工修复做了两次以上——说明该沉淀成规则或自动检查。

## 2. 提议格式

追加到 `my_skills/INBOX.md`，一条一个块：

```
## <YYYY-MM-DD> <标题>
来源: <哪个技能 / 哪次使用>
证据: <发生了什么，用户说了什么>
建议: <改哪个文件哪一节，或新建什么 reference>
类型: 新reference | 改正文 | 新技能 | 卫生检查
影响面: <波及哪些技能或文件>
状态: 待审
```

## 3. 告知与落地

- 记录后**立刻告知**用户：当前有几条待审提议、各是什么。不在会话里默默攒着。
- 用户批准后才可以改技能文件。改动时同步核对：Output Contract 各处逐字一致、references 链接有效、SKILL.md ≤150 行、00-overview 和 README 是否受影响。改完跑 `my_skills/check_skills.sh`。
- 落地后把那条标 `已落地 + 日期`；被拒绝的标 `已拒绝 + 原因`。拒绝记录不删——防止下次又提同一条。

## 4. 什么值得记

- 会重复出现的才记；只适用于当前对话这一次的不记。
- 拿不准就记，让用户在审查时扔掉——漏记的代价比多记大。
- 不记研究项目本身的产物和决定，那是 `research_manager` 及各研究技能的事。

## 5. 边界

- 不重排技能间委托关系的语义，不删规则，只提议。
- 改任何技能文件前必须拿到用户对这条提议的明确批准；"顺手优化"等于没批准。
- 写文件前先经用户确认（INBOX.md 的追加除外——追加本身就是被告知的行为，但追加内容要在回复里同步展示）。
