# 模板来源：5 篇 ICLR 论文的骨架与句式

拉取日期：2026-09-17。来源均为 arXiv abs 页 + HTML 全文。用途：写 ICLR 论文时对照真实例子的结构和句式，不凭记忆。

---

## 1. AgentBench（arXiv:2308.03688，ICLR 2024，agent 基准）

**章节骨架**：1 Introduction → 2 LLM-as-Agent 定义 → 3 基准组成（3.1/3.2/3.3 按 Code/Game/Web 三类环境）→ 4 评测（Setup / Main Results / Analysis）→ 5 Related Work → 6 Conclusion → 附录 A–J。

**引言 5 段**：大背景（agent 是 AI 核心概念）→ 技术机会（GPT-4 与对齐训练）→ 缺口（缺系统基准，已有环境动作封闭、单环境、门槛高）→ 提出 AgentBench（8 环境 3 类，测 29 模型）→ 失败诊断与建议，收束到贡献列表。

**贡献**："In summary, our contributions are:" + 3 条 bullet，每条 2–3 句，动词开头。

**摘要句式**（约 170 词）：
1. `The potential of X has been widely acknowledged. Thus, there is an urgent need to quantitatively evaluate X ...`（背景+必要性）
2. `We present <Name>, a multi-dimensional benchmark that consists of 8 distinct environments to assess ...`（提出物+规模）
3. `Our extensive test over 29 ... shows that, while ..., there is a significant disparity ...`（规模+对比发现）
4. `We identify the typical reasons of failures ..., showing that ...`（失败诊断）
5. `And different from existing assumptions, ...`（反直觉发现）
6. `Datasets, environments, and an integrated evaluation package ... are released at <URL>.`（发布声明）

**局限**：无独立节，细节全进附录。

---

## 2. WebArena（arXiv:2307.13854，ICLR 2024，环境基准）

**章节骨架**：1 Introduction → 2 环境（控制方式/站点选择/观察空间/动作空间）→ 3 任务集（收集/标注）→ 4 Baseline agents → 5 Results + Analysis → 6 Related Work → 7 Conclusion → 附录 A。

**引言 5 段**：背景+两条标准（真实、可复现）→ 缺口（现有环境过度简化，逐条列四个缺陷）→ 提出 WebArena（Figure 1 总览，4 个全功能站点+工具+知识库，Docker+gym API 保复现）→ 812 个长程任务、评功能正确性 → 结果（GPT-4 14.41% vs 人类 78.24%）。

**贡献**：无列表，摊在叙述里。

**摘要句式**（约 185 词）：背景 `With advances in X, there is now potential for ...` → 缺口 `However, current X ... leading to a disconnect ...` → 提出物 `we build an environment ... that is highly <A> and <B>` → 具体化 `we focus on ..., and create ... from four common domains` → benchmark `we release a set of benchmark tasks focusing on evaluating the functional correctness` → 结果对照 `our best GPT-4-based agent only achieves 14.41%, significantly lower than the human performance of 78.24%` → 意义 `WebArena can be used to measure such progress`。

**复现性是主线**：不是独立节，写进核心属性（Docker、自托管、状态重置）。

---

## 3. SOTOPIA（arXiv:2310.11667，ICLR 2024，社会智能评测）

**章节骨架**：1 Introduction → 2 环境（task space / episodes）→ 3 SOTOPIA-EVAL 评估框架（单列一节）→ 4 Research questions 与实验设置（单列一节）→ 5–7 三组实验各一节 → 8 Related work → 9 Conclusion → 附录 A–H（附录 B = limitations & future directions，含伦理）。

**引言 7 段**：大背景+具体例子（"分享毯子"）→ 缺口 → 提出环境 → 规模（90 场景 × 40 角色）→ 评估框架（多维度、双评委）→ 结果预告 → "Our contributions are as follows" 字母编号 (A)–(D)。

**摘要句式**（约 165 词）：人性背景 → `Yet, X's abilities in this realm remain elusive.` → `We present <Name>, an open-ended environment to ... and evaluate ...` → 环境内能力 → `We simulate ... and evaluate ... with a holistic evaluation framework called <Eval>` → 发现+难例子集（SOTOPIA-hard）→ 人类对照 → `demonstrate <Name>'s promise as a general platform for ...`。

**值得抄的设计**：难例子集命名（<Name>-hard）；评估框架单独命名（<Name>-EVAL）；局限+伦理放附录 B。

---

## 4. GameNGen（arXiv:2408.14837，ICLR 2025，系统类对照）

**章节骨架**：1 Introduction → 2 Interactive World Simulation（形式化）→ 3 方法（数据/训练/推理）→ 4 实验设置 → 5 Results（质量/消融）→ 6 Related Work → 7 Discussion（Summary / Limitations 三条编号 / Future Work）→ Broader Impact（含 Societal impact + Reproducibility）。

**引言 6 段**：背景（游戏=手写规则 game loop）→ 技术机会与差异（扩散≠交互模拟）→ 缺口+问句（"Can a neural model ...?"）→ 回答 yes → 贡献散文（"Our key contribution is a demonstration ..." + 内联 (1)(2)(3) 三个技术点）→ 更广意义+坦承未解。

**摘要句式**（约 175 词）：`We present <Name>, the first <X> that also enables ...` → 训练对象 → 性能数字（20 FPS 单 TPU、PSNR 29.4 "comparable to lossy JPEG"）→ 人类评测数字（"only slightly better than random chance ... even after 5 minutes"）→ 方法两阶段 → 技术收益。

**值得抄的写法**：数字配生活化类比（PSNR 29.4 ≈ 有损 JPEG）；问句开缺口；Limitations 三条编号写在 Discussion。

---

## 5. The Illusion of Diminishing Returns（arXiv:2509.09677，ICLR 2026，测量类）

**章节骨架**：1 Introduction → 2 Formulation（指标定义：Step/Turn/Task Accuracy）→ 3 Experiments（按三个研究问题分节）→ 4 Related Work → 5 Conclusion（末段即 Limitations）→ 附录 A–J。

**引言 5 段**：核心问句+经济动机 → 重新解读争论（解耦 planning 与 execution）→ 受控设置做法 → **三个发现用加粗小标题各自成段**（finding-first 写法，无贡献列表）→ 收尾连回大命题。

**摘要句式**（约 230 词，最长）：问句开题 → 反转主论点 `short-task benchmarks may give an illusion of ...` → 重新归因 `failures ... arise from execution, rather than ...` → 方法 `we propose isolating ..., by explicitly providing ...` → 发现链 `First, we find ... We then observe ... curiously, ... But, we find ...` → 收束 `Overall, ... we hope to reconcile ...`。

**值得抄的写法**：问句开题；发现链用 First/Then/But 连接；局限并入结论末段，不单列。

---

## 跨论文共同纪律

- Related Work 全部在结果之后、结论之前。
- 摘要全部单段、160–230 词、无引用无公式；数字集中在结果句。
- 人类对照或强 baseline 对照是摘要标配（WebArena 14.41% vs 78.24%；SOTOPIA GPT-4 vs 人类；GameNGen 人类分辨≈随机）。
- 贡献 3–4 条，不超过；形式三选一（bullet / 字母编号 / 散文+内联编号）。
- 环境/任务节开头给形式定义（POMDP、⟨S,A,O,T⟩、task space）。
- 局限必须有，位置灵活（Discussion 段、结论末段、附录节）。
