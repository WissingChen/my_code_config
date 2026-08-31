# Rewrite Examples — write_md §1–§2 Companion

Reference-only: before/after pairs for the language and structure rules. Each pair shows the rule applied, not just stated.

## Language Layer (§1)

**Anti-jargon — delete what carries no meaning**

- Before: "我们对模型进行了系统性的性能退化分析。"
- After: "我们分析了模型在哪些样本上掉点。"

**Concrete verbs over abstract nouns**

- Before: "在对照子集上观察到了准确率的下降现象。"
- After: "对照子集的准确率掉了 2.6 个点。"

**Explain on first use / say it straight**

- Before: "本文采用 conformal prediction 框架对预测区间进行校准。"
- After: "我们用 conformal prediction（一种给出覆盖率保证的区间构造方法）校准预测区间。"

## Structure Layer (§2)

**Conclusion first — first paragraph carries the point**

- Before: "近年来，视频理解取得了长足进展。与此同时，评测协议问题逐渐受到关注。本节介绍我们的实验设置……（第三段才出现结果）"
- After: "修正项在受控协议下提升 6.6 个点，但在无偏差题目上掉 2.6 个点。下面给出实验设置与证据。"

**30-second scan test — key numbers bold, heading states the point**

- Before: heading "实验结果"；正文 "……最终在修正子集上取得了 67.8% 的准确率，相比基线的 61.2% 有所提升。"
- After: heading "修正项在受控协议下有效，在对照子集过修正"；正文 "**67.8% vs 61.2%**（三次运行，范围为观测区间）。"

**Figure-text rhythm — break walls, but only with information-carrying elements**

- Before: 连续五段文字描述三轮实验的数值变化。
- After: 一张 baseline–expected–actual 区间图 + 两段文字：一段说哪条链成立，一段说哪条断裂。（图承载比较，文字承载解释。）
