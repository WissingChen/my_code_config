---
name: write_md
description: Markdown readability, visual planning, and report HTML rendering. Load for any long research report (two passes: visual planning before figures, final readability after), when the user asks to improve readability or format a document, or when a report needs a self-contained HTML reading version. Handles language, structure, and a renderer-aware presentation layer. Horizontal slide decks belong to slide_deck.
requires: research_manager
---

## Output Contract

- 先说结论，再给必要依据和下一步。
- 默认短句和常用词；术语只在更准确时用，首次出现直接解释。
- 内部状态、流程和检查表默认不展示；只有影响决定或用户明确要求时才展开。
- 外部事实、论文结论和数字附来源；不确定的直接写"尚未验证"或"我推测"，不给每句话机械加事实/猜测标签。
- 一段能说清就不用表格；独立要点用列表；只有横向比较才用表格。
- 不写套话、廉价肯定、重复总结和固定收尾。
- 禁用黑话和自造词（赋能、闭环、抓手、对齐、链路、落地、打磨等），直接说具体那件事。
- 写文件前先经用户确认。
- 只在发现具体的过时或重复内容时才提议清理，不作为固定收尾动作。

# write_md — 让 Markdown 好读，让图有规划

## 1. 语言层

本节的改写前后实例：`references/rewrite-examples.md`。

- **反术语**：一个词删掉不改变意思，就删。
- **一句一个意思**：堆叠的抽象拆开。
- **具体动词优先于抽象名词**："模型召回掉了"好过"观察到性能退化"。
- **首次出现就解释**：引入的每个概念都要能用大白话解释。
- **直说**：每段第一句带观点；是抽象名词的标题改写成陈述句；内部流程名（评审、通过与否、交接、生命周期）不许糊到读者脸上——直接说什么确认了、什么缺、下一步是什么。

**精度例外**：论文手稿里必要的技术术语保留——先用大白话解释意思，再给准确术语。手稿的起草和论证结构本身归 `academic-paper-writing`；在手稿上 `write_md` 只套用这一层语言规则。

## 2. 结构层

- **结论先行**：第一段就给出观点。
- **关键数字加粗**：扫读的人要一眼看到决定性数字。
- **30 秒扫读测试**：疲惫的读者 30 秒内必须抓到要点。
- **图文节奏**：长文档不许整屏文字墙，用表格、图、提示块打断。每个非文字元素必须携带信息——短文档或一目了然的文档不许硬塞图。

## 3. 报告要过两遍

每份长报告 `write_md` 过两遍——绝不只在结尾过一遍：

1. **配图规划（图还不存在时）**：读草稿结构，找出图/表比文字更能说清的位置，产出该报告**唯一的一份**配图规划：位置、用途、主张、产物类别，并汇总 `result_analysis` §9 从证据角度提出的候选图；每张候选记录选中/拒绝及原因，每行一条：`| 候选图 | 选中/拒绝 | 原因 |`。规划交给 `experiment_manager` 验收，由它委托 `result_visualization`。这一遍打破"得先有图 write_md 才能动"的死锁。
2. **最终可读性（图已嵌入后）**：结论先行、术语一致、图表引用、图注位置、30 秒扫读路径，并按 `experiment_manager` §4a 的标准逐张验收被引用的图。不许改动统计结论、证据判定和去留决定。

## 4. 呈现层

提示块预算：**每篇 ≤3 个**。一个块不改变读者第一眼看到什么，就别用。选元素：并列比较用表格；有出处的引述用引用块；只有必须改变读者第一注视点时才用提示块（警告、决定、关键数字）。

按渲染器选格式（默认目标：VS Code / Typora / Obsidian 本地阅读）：

- **本地渲染器**：内联样式的原生 HTML 块渲染正常，默认选它。
- **GitHub**：内联样式会被剥掉；只有文档会在那边看时，退回纯 Markdown、引用块或 alert（`> [!NOTE]`）。
- **论文手稿**：默认不用 UI 式提示块。

```html
<!-- 本地渲染器默认用；GitHub 目标时去掉 -->
<div style="background:#3498db1a; border-left:4px solid #3498db; padding:8px 12px; margin:8px 0;">...</div>
```

## 5. 语义色板

一个颜色一个意思。色板只维护在 `result_visualization/plotting-reference.md` §3，这里不重复定义。

## 6. 图表分工

标准流程图、时序图、架构图、数据图由 `result_visualization` 制作。`write_md` 负责需要判断（§3 第一遍）和整合：位置、引用、图注上下文。

## 7. 报告渲染成 HTML

区别于 `slide_deck`（横向翻页演示）。用户要报告的可读 HTML 版时，从最终 `REPORT.md` 和保留的图生成一个自包含的滚动 HTML 文件：

- 自包含：内联 CSS，无 CDN、无外部字体；图片默认 base64 嵌入。最小骨架：`references/report-skeleton.html`。
- 自动目录带小节锚点；顶部放结论先行的摘要块。
- 图带图注嵌入、点击放大；Mermaid 预渲染或换成内联 SVG，保证离线可用。
- 打印友好：浏览器打印出干净文档。
- 内容变了从源文件重新生成；绝不手维护一份平行的 HTML。
- 默认路径：报告旁边，或 `.kilo/reports/YYYY-MM-DD-<slug>-report.html`。

默认不把短的或一次性的文档转 HTML：快速讨论留在 Markdown；完整方向报告出 Markdown + HTML；正式演示给 `slide_deck`；手稿留 Markdown/LaTeX 配 PDF/SVG 图。

## 8. 全局约束

- 不要装饰性格式。
- 除非需要强调，否则不把普通表格换成带框表格。

## References

| 文件 | 何时加载 |
|---|---|
| `references/rewrite-examples.md` | 应用 §1–§2 语言/结构规则时 |
| `references/report-skeleton.html` | 渲染报告 HTML 版时（§7） |
