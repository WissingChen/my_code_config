---
name: pdf_export
description: Render a finished Markdown report to an A4 PDF directly with headless Chromium, without the editor's export menu. Load when the user asks to export or generate a PDF from Markdown or an HTML report, or when a plugin PDF export came out the wrong page size or lost the mermaid diagram. Reading HTML reports belong to write_report; slide PDFs to slide_deck.
requires: write_report
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

# PDF Export — 直接把 Markdown 导成 A4 PDF

用本机 headless Chromium 生成 PDF，不经过 Markdown Preview Enhanced 的导出菜单。

## 1. 为什么自建这条路径

插件四种出 PDF 的方式都有坑，实测过：

- 只有 **Chrome (Puppeteer)** 会执行 JavaScript，mermaid 流程图才出得来；**PDF (prince)** 和 **eBook (Calibre)** 都不跑 JS，流程图丢失。
- **没有全局 A4**：Puppeteer 的 `format`、Calibre 的 `paper-size` 只能写进每个文件的 front-matter；把 `@page { size: A4 }` 放进全局 CSS 对 Puppeteer 无效（它默认 Letter 且不读 CSS 尺寸）。

本技能用一个脚本固定三件事：A4 写在全局 CSS 里、mermaid 交给真浏览器渲染、图片 base64 内嵌。调用一次出 PDF，不改 markdown 头部。

## 2. 工具链

- **headless Chromium**（`--print-to-pdf`）：认 `@page size`、跑 JS。本机 `/snap/bin/chromium` 已验证。
- snap 版 Chromium 受 AppArmor 限制，只能读写 `$HOME` 下的路径。脚本把中间 HTML/PDF 放 `~/pdf_export_tmp/`，成功后把 PDF 复制到目标路径（目标可在任何可写位置）。
- mermaid 优先用本地 `mermaid.min.js`（Markdown Preview Enhanced 扩展自带），找不到再走 CDN。

## 3. 用法

```bash
P=/data0/chenweixing/tools/miniconda3/envs/wsi/bin/python
$P ~/my_code_config/my_skills/pdf_export/references/build_pdf.py REPORT.md -o REPORT.pdf
```

| 参数 | 作用 |
|---|---|
| `input` | 输入 Markdown；相对路径图片按文件所在目录解析并 base64 内嵌 |
| `-o/--output` | 输出 PDF，默认与输入同名 `.pdf` |
| `--css` | 换样式表，默认 `references/report_pdf.css` |
| `--title` | 覆盖 PDF 标题，默认取第一个 `# 标题` |
| `--keep-html` | 同时保留中间 HTML（调试用） |
| `--timeout` | mermaid 渲染等待毫秒数，默认 15000；图多/复杂时调大 |

顶部的 YAML front-matter 会被自动去掉，所以带或不带都能直接导。

## 4. 出完必须验证

脚本只保证"生成了文件"，页数/版面要自己看一眼：

```bash
pdfinfo REPORT.pdf | grep -i pages          # 或 gs 数页
pdftoppm -png -r 90 -f 1 -l 2 REPORT.pdf /tmp/p   # 头两页转 PNG
```

打开 PNG 确认：**纸张是 A4**（MediaBox 约 595×842 pt）、**mermaid 流程图有内容**、**嵌入的图不空白**。任一项缺失就别交付。

## 5. 边界

- 只做 PDF。阅读用的自包含 HTML 报告归 `write_report` §7；横向翻页 deck 归 `slide_deck`。
- 不创造内容：输入是已定稿的 Markdown，图由 `result_visualization` 产出，统计结论由 `result_analysis` 负责。
- 改纸张/字号/表格样式改 `references/report_pdf.css`，这是全局的，不需要动任何 markdown 文件。

## References

| 文件 | 何时加载 |
|---|---|
| `references/build_pdf.py` | 每次导出都跑 |
| `references/report_pdf.css` | 调整纸张尺寸、字体、表格与分页规则时 |
