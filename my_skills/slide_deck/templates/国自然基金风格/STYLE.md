# 国自然基金风格（NSFC Pipeline Style）

机制流程图 / 预期方案 pipeline 页风格。视觉原型：基金申请书中常见的"多栏机制图"——分栏面板 + 彩色标题栏 + 编号步骤流 + 粗箭头 + 闭环横幅。

- 来源实例：`room2manip/slides/index.html` slide 12「任务—环境—本体协同的具身交互行为生成」（2026-08-13 通过视觉 QA）
- 基准实例：本目录 `template.html`（自包含可渲染，复制即用）

## 风格 DNA（识别特征，缺一就不像）

1. **三栏横向结构**：绿色「输入单元」面板 → 橙色块状箭头 → 藏青标题栏「引擎」面板 → 橙色块状箭头 → 白底「归因/输出」面板。
2. **藏青实心标题栏**（`#1f3a63` 白粗字 21px）+ 浅蓝副条件栏（`#dce7f6`，写"共同条件：…"）。
3. **编号步骤流**：蓝色实心编号圆圈 + 浅蓝底（`#eaf2fb`）蓝边步骤框；S 形回流——上排 ①→②→③，右侧 ↓，下排 ⑤←④，左侧 ↑ 回 ①；竖向连接符用橙色并带小标签（如「失配经验」「闭环再生」）。
4. **竖排色块标签**：归因/分类条目左侧 44px 色块，白色竖排粗字（`writing-mode: vertical-rl`），三类配色固定为 藏青 / 中蓝 / 灰。
5. **橙色块状箭头**连接面板（SVG 多边形，非文字箭头），下方配橙色小标签（≤4 字）。
6. **胶囊横幅**收尾：白底蓝边圆角 999px，句式「以X检验…，以Y驱动…」，关键词分别上蓝色和橙色。
7. **全部图标手绘 SVG**：`viewBox="0 0 24 24"`、`fill="none"`、`stroke="currentColor"`、`stroke-width="1.8"`、round caps/joins；不用 emoji、不用位图。

## 色板（CSS tokens）

```css
--fig-navy: #1f3a63;        /* 标题栏、归因色块1、强调文字 */
--fig-blue: #2e6fb7;        /* 编号圆圈、步骤边框、归因色块2 */
--fig-blue-soft: #eaf2fb;   /* 步骤框底色 */
--fig-blue-line: #c2d6ee;   /* 引擎面板边框 */
--fig-green: #5f9e46;       /* 输入单元图标、虚线条边框 */
--fig-green-deep: #3f6f2f;  /* 输入单元标题 */
--fig-green-soft: #eff7e7;  /* 输入单元底色 */
--fig-green-line: #c2dfae;  /* 输入单元边框 */
--fig-orange: #e8833a;      /* 块状箭头、回路连接符、标签 */
--fig-gray: #59637a;        /* 归因色块3 */
```

副条件栏底色 `#dce7f6`；归因面板边框 `#c9cfdb`。依赖宿主 deck 的基础 token：`--ink`、`--muted`、`--line`。

## 布局数值

- 三栏 flex：左栏 300px / 右栏 348px / 箭头栏 62px / gap 12px；引擎栏 `flex:1` 自适应。
- 引擎内步骤流：CSS grid `1fr 30px 1fr 30px 1fr`，行 gap 10px、列 gap 4px；步骤框跨格用显式 `grid-column/grid-row` 放置（上排 1/3/5 列，下排 ⑤ 在 1 列、④ 在 5 列，横向回流箭头跨 2/5 列）。
- 字号层级：标题栏 21px/800 → 步骤标题 18.5px → 输入卡标题 19px → 副栏 16.5px → 正文 14.5–15px → 小标签 12.5–13.5px → 横幅 19px。
- 步骤框内部：`hd`（编号圆圈 26px + 标题）+ `bd`（32px 图标 + ≤3 行正文）。
- 归因条目：色块 44px + 衬线公式（STIX/Times，16.5px）+ 说明 14.5px；底部三色输出签 `flex:1` 均分。

## 组件骨架

全部见 `template.html`：`.syn`（总容器）→ `.syn-inputs` / `.syn-engine` / `.syn-attr` 三栏 + `.syn-arrow` 箭头栏 + `.syn-banner` 横幅。复制时连同 `:root` 中的 `--fig-*` token 一起搬运。

## 图标库（template.html 中已有实现，可直接复用）

clipboard（任务）、floorplan（环境）、robot-arm（本体）、overlap-circles（实例化）、shield-check（检验）、trajectory（行为生成）、split-node（归因）、refresh（再生成）、database（记忆/写回）、layers（输入单元标题）、block-arrow（橙色块状箭头，viewBox 60×40）。

## QA 坑点记录（实测踩过）

- 箭头栏标签 **≤4 字**（15px 下 62px 栏宽），5 字必换行——用「三元组」而非「三元组输入」。
- 步骤内小签（`.syn-mini`）每签 ≤3 字，`font-size:12.5px` + `white-space:nowrap`，否则换行。
- 副条件栏 / 归因副标题一句话写完，避免带括号的长注释（会折行成两行）。
- 步骤正文 ≤22 字（约 3 行 @153px 宽）：grid 行高由该行最高步骤框决定，一个框 5 行会拖累同排其他框出现内部死区。
- 归因面板公式用衬线字体与正文区分；下标用 `<sub>`。
- 横幅 `align-self:center` + `flex:0 0 auto`，不要拉伸整行。
