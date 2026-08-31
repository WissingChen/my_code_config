---
name: slide_deck
description: Self-contained HTML slide decks as a PPT replacement. Load when the user asks to present the project (or a subset such as motivation, contributions, methods, experiment results) as a horizontal-paging HTML file. Scrolling HTML report rendering belongs to write_md.
requires: research_manager
---

## Output Contract

- 先说结论，再给必要依据和下一步。
- 默认短句和常用词；术语只在更准确时用，首次出现直接解释。
- 内部状态、流程和检查表默认不展示；只有影响决定或用户明确要求时才展开。
- 外部事实、论文结论和数字附来源；不确定的直接写"尚未验证"或"我推测"，不给每句话机械加事实/猜测标签。
- 一段能说清就不用表格；独立要点用列表；只有横向比较才用表格。
- 不写套话、廉价肯定、重复总结和固定收尾。

# Slide Deck — 用 HTML 代替 PPT

生成一个自包含、横向翻页的 HTML 文件。不创造内容：每个声明和每张图都来自已有的研究产物。

## 1. 适用范围

- 完整 deck 的小节：动机 → 贡献 → 方法 → 实验结果 → 结论/下一步。
- 部分 deck：只生成用户点名的小节。回复里说清包含了哪些小节、各取自哪些产物。
- 边界：本技能只做横向演示 deck。滚动式自包含 HTML **报告**归 `write_md`（§7）；不许把 deck 拉成报告，也不许反过来。

## 2. 内容从哪来

| 小节 | 主要来源 |
|---|---|
| 动机 | `proposal/NN-slug/experiment-plan.md`、方向 `00-overview.md` |
| 贡献 | 终版 `REPORT.md`、转正摘要、状态快照 |
| 方法 | `REPORT.md` 方法部分、`ENN-experiment-report.md` 的设置和对照 |
| 实验结果 | `REPORT.md` 结果部分、保留的证据图、关键结果表 |

- 每张带数字或声明的 slide 在页脚小字注明来源产物。绝不编数字。
- 新图委托 `result_visualization`；统计结论委托 `result_analysis`。`slide_deck` 只把已批准的内容重新编码成 slide。

## 3. 技术规格

- 单个 `.html` 文件：内联 CSS 和 JS；无 CDN、无框架、无外部字体。
- 横向翻页：`←`/`→` 方向键、可点的前后控制、页码 `n / N`。
- 16:9，正文字号 ≥24px；一页一个观点。
- 标题是断言，不是话题（"X 把错误率降了 40%"，不是"实验结果"）。但不许为了有力把趋势升级成因果或确定的声明——证据薄的时候标题保留限定词。
- 图页带图注，写清不确定度含义。图默认 base64 嵌入保持可携带；用户明确要求小文件时才用相对路径外链。
- 打印友好：`@media print` 把每页 slide 渲染成一页横版，浏览器打印成 PDF 即代替 PPT 讲义。
- 大 deck（>20 页）：分块生成和做视觉检查（动机/方法/结果），再拼装；拼装后重新验证页码、导航点、打印版式——溢出和编号 bug 都出在分块接缝处。
- 布局规则：**盒子贴着内容长，空白留在盒子外。** 内容短时不许用 `flex:1` 把卡片拉满高——那把死空间关进了边框里，看着就是"空"。行高自适应（`flex:0 0 auto`），内容块在 slide 里垂直居中，剩余空间均匀留在盒子外面。

## 4. 从论文里抓图（相关工作用）

deck 需要论文的 teaser/pipeline 图时：

1. **arXiv HTML 版优先**：多数近期论文 `https://arxiv.org/html/<id>/x1.png` 就是 teaser，`x2.png` 通常是 pipeline 图。拿不准就抓 HTML 页面看 `<img>` 标签确认。
2. **PDF 兜底**：有些论文没有 HTML 版，或 HTML 版图没抽出来（检查 `src` 是否缺失/为空）。这时：`curl -O https://arxiv.org/pdf/<id>`，用 `pdftoppm -png -f N -l N -r 150 paper.pdf page` 渲染对应页，用 PIL 裁出图区。
3. **每个下载都验证**：跑 `file *.png` 并看尺寸——arXiv 可能拿 200 状态码返回 HTML 错误页。一个 8 KB 的"PNG"是错误页，不是图。
4. **base64 嵌入前先优化**：缩到 ≤1100 px 宽，存 JPEG q≈82。arXiv 原始 PNG（可达 10 MB）会把 deck 撑爆；优化后 15–20 页的 deck 保持 1–2 MB。
5. 每张图在 slide 页脚和来源页署名（`arXiv <id> Fig.N, HTML/PDF`）。
6. **非 arXiv 来源**：会议提供公开 PDF 直链就走 `pdftoppm` 路线。只能摸到摘要页（付费墙或无全文）时，不抓预览缩略图——委托 `result_visualization` 重画一张简化示意图，署名"redrawn after <引用>"。

## 5. 视觉检查循环（强制）

不渲染、不逐页检查的 deck 不许交付。

1. 无头 Chromium 逐页截图：`chromium --headless --no-sandbox --screenshot=out.png --window-size=1600,900 file.html`（跳转到第 N 页：复制一份文件，临时改掉开头的 `go(0)` 调用）。
2. Snap 版 Chromium（Ubuntu 默认）只能读写 home 目录——把 deck 拷到 `~` 预览，截图也写到那。
3. 批量截图循环偶尔会产出过期或错页的截图；可疑的图必须单独重拍再采信。
4. 每页缺陷清单：
   - 盒子里大片死空间（见 §3 布局规则）；
   - SVG 文字压到图形上或在 `viewBox` 边缘被裁；
   - 代码块和宽表格横向溢出或撞到页脚；
   - 文字在页面边缘被裁。
5. 全局字号调整（比如所有 `font-size` 统一 ×1.18）是合法的迭代步骤，但之后每个表格、代码块、页脚都必须重查——它们最先溢出。

## 6. 风格方法论

风格由原则指导，不固定主题；用户在渲染产物上逐步迭代。

- 所有风格决定集中成 `:root` 一个块里的 CSS 变量（颜色、字体、间距、页面边距）。这是用户调参层：改风格是一处改动，绝不是散落的内联样式。
- 层次来自字号、字重和留白。颜色留给含义：最多一个强调色，内容本身带状态时才用语义色。
- 一致性压过任何具体选择：同类元素在每页长得一样。
- 每个视觉元素都要值回它占的像素；不带信息的装饰删掉。
- 从极简开始。只在渲染产物里看到具体的可读性问题时才加样式。
- 两层改动分开：内容变了从源产物重新生成；风格变了改 `:root` 变量。迭代一层绝不许动另一层。

## 6.5 风格模板库（templates/）

用户命名保存的风格模板放在 `templates/<风格名>/`，索引与维护规则见 `templates/README.md`。

- 用户点名某个已保存风格时：先读该模板的 `STYLE.md`，按其风格 DNA 与组件词汇**参考风格**，按内容拓扑从模式库选择或组合布局；`template.html` 只是一种模式的实例，不凭记忆重写样式、不硬套骨架。
- 用户要求保存新风格时：从已通过视觉检查的 slide 提取 CSS tokens 与组件骨架，新建 `templates/<风格名>/STYLE.md` + `template.html`，在 `templates/README.md` 登记，并对 `template.html` 做一次截图检查。
- 风格的后续修订回写到模板文件（单一事实源），套用页面只替换内容、不改模板 token。
- 当前模板：**国自然基金风格**（技术路线插图视觉语言：面板/色彩/箭头语法 + 5 种布局模式）、**瑞士国际主义风格**（整套 deck 视觉体系：网格 + 极细巨字 + 单一 accent）。索引见 `templates/README.md`。

## 7. 输出规矩

- 默认路径：`.kilo/reports/YYYY-MM-DD-deck.html` 或用户指定路径。生成物：从源文件重新生成，不手改。
- 生成前先给 slide 大纲（每页一行），用户确认后再做。
- deck 以来源页结尾，列出用过的每个产物。
