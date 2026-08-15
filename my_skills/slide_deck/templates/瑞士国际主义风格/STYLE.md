# 瑞士国际主义风格（Swiss International Style）

瑞士国际主义平面设计风格的全 deck 模板：模块化网格 + 无衬线极细巨字 + 单一强调色 + 等宽大写标签 + 发丝线/点阵装饰。直角、无阴影、无渐变，克制至极。

- 来源实例：`https://mo65jg3kga2my.ok.kimi.link/`（NSFC 博士生专项申请汇报 deck，15 页）
- 基准实例：本目录 `template.html`（自包含可渲染，4 页覆盖核心组件）
- 设计系统渊源：IBM Carbon（2x Grid 间距模数、Motion tokens、role-based 文本色）+ 瑞士排印传统

## 风格 DNA（识别特征）

1. **网格至上**：12 列模块化网格（`.grid-12` + `.span-*`）；所有间距取 Carbon 2x Grid 8px 模数 token（`--sp-3:8px` … `--sp-13:160px`），杜绝自由取值。
2. **双极排印**：Expressive 巨字（vw/vh 驱动，`font-weight:200–250`，`letter-spacing:-.02~-.05em`，字号越大字重越轻）× Productive 小字（固定 px 的 `.t-*` token：mono 大写标签 14px / 正文 16–18px）。中间字重（500–600）只给标题强调。
3. **单一 accent**：整页只有纸面灰白（`#fafaf8`）、近黑（`#0a0a0a`）、三档灰、**一个**强调色（可换主题：IKB 克莱因蓝或深绿 `#17673A`）。第二彩色绝不出现。
4. **等宽字体做元信息**：所有 kicker / 页眉 / 页码 / 图注用 mono + 大写 + `letter-spacing:.14–.24em` + 低透明度。
5. **发丝线与点阵装饰**：1px 分隔线（`opacity:.18–.25`）、radial-gradient 点阵、135° 斜杠 hatch；装饰 opacity 不超过 `.62`。
6. **直角纯色块**：卡片/色块一律 `border-radius:0`（最多 3px）、无阴影；页面变体仅四种——paper / grey / dark(ink) / accent。
7. **页面骨架固定**：顶部 `.chrome-min`（左章节名 · 右页码）→ 中间内容 → 底部 `.t-meta` 一句话 takeaway（常以 → 开头）。

## 色板与文本角色

```css
--paper:#fafaf8;  --ink:#0a0a0a;
--grey-1:#f0f0ee;  --grey-2:#d4d4d2;  --grey-3:#737373;
--accent:#17673A;            /* 深绿（此实例）；换主题只改 accent 一族 */
/* 备选主题：IKB 克莱因蓝 --accent:#002FA7（暗底提亮版另配） */
--accent-on:#ffffff;  --accent-bright:#3FA06B;   /* 暗底高亮提亮版 */
```

文本不用 opacity 叠灰，用 Carbon role token：`--text-primary/secondary/helper/placeholder`、`--border-subtle:#e0e0e0`、`--border-strong:#a3a3a3`。

## 字体

- `--sans`: Inter → Helvetica Neue → Arial → system-ui；中文 `--sans-zh`: PingFang SC / 思源黑体 / 微软雅黑。
- `--mono`: JetBrains Mono → IBM Plex Mono → SF Mono → Consolas。
- 模板默认不引外部字体（自包含原则）；如需完全还原可加 CDN：Inter(200–900) + JetBrains Mono(300–600) + Noto Sans SC(200–900)。
- **Windows 坑**：微软雅黑无 200 字重，巨字会糊成粗黑——用 `body.is-win` 把所有 200 补偿为 300（template.html 已含检测脚本与补偿 CSS）。
- 巨字尺寸用 `min(vw, vh)` 双约束（如 `font-size:min(6.4vw,11.2vh)`），保证 16:9 之外的视口不溢出。

## 页面骨架（canvas 模式，每页即满屏卡片）

```html
<section class="slide[ grey|dark|accent|split]">
  <div class="canvas-card">
    <div class="chrome-min"><div class="l">02 · 章节名 SECTION</div><div class="r">02 / 15</div></div>
    <div style="flex:1;display:grid;grid-template-rows:auto 1fr auto;gap:2.4vh;min-height:0">
      <div>  <!-- header: .t-meta kicker + 巨字 h2 -->  </div>
      <div>  <!-- body: 组件区 -->  </div>
      <div class="t-meta">→ 本页一句话结论</div>
    </div>
  </div>
</section>
```

- `.canvas-card` padding：`5.6vh 5vw 4.4vh`；`.chrome-min` 与内容间距 `--sp-9`(48px)。
- 底部内容不低于 `--nav-safe-bottom:8vh`（给分页圆点留安全区）。

## 组件清单（template.html 全部含实现）

| 组件 | 类 | 要点 |
|---|---|---|
| 页眉 | `.chrome-min` | mono 大写，左章节右页码 |
| Kicker | `.t-meta` / `.kicker` | `.kicker` 自带 24px 引导短横 |
| 巨字标题 | inline `font-weight:200; font-size:min(…vw,…vh)` 或 `.h-hero/.h-xl/.h-md` | 中文用 `-zh` 变体，行高 .92–1.12 |
| KPI 行 | `.kpi-row-4 > .kpi-cell`（lbl/nb/note） | 顶 1px 线 + 单元格左竖线，首个去线 |
| 大数字 | `.kpi-hero/.kpi-big/.kpi-thin/.num-mega` | 800 或 200 两极，`font-feature-settings:"tnum"` |
| 流程 | `.pipeline[data-cols] > .step(.accent-top)` | 顶 2px 边 + mono 编号，当前步 3px accent |
| 数据卡 | `.stat-card(.accent-top/.thin)` | 顶边 2px，无盒无阴影 |
| 色块 | `.accent-block/.ink-block/.grey-block`、`.card-fill/.card-ink/.card-accent` | 每页最多一个 accent 块 |
| 时间线 | `.timeline-v / .timeline-h` | 8px 实心圆点 + 4px 虚线轴，accent 标当前 |
| 柱状图 | `.bar-chart / .h-bar-chart / .v-bar-chart` | 扁平几何，ink 为默认色，accent 只给焦点行 |
| 对仗 | `.duo-compare`（1fr 1px 1fr 中缝竖线） | 对比页专用，accent 只给其中一栏 |
| 半屏 | `.split-half > .half.b-ink/.b-accent` | statement/封面/封底 |
| 子卡 | `.sub-grid-3-2 > .sub-card` | grey-1 底、radius 3px、右上 mono 角标 |
| 层块 | `.stack-row > .stack-block.b-accent/.b-grey/.b-ink` | 三层架构拼图 |
| KPI 塔 | `.bar-towers > .bar-tower`（.h-1…h-4 控高） | 默认浅描边，只有焦点塔 .b-accent |
| 引用 | `.callout(.ink)` | 左 3px accent 边 |
| 高亮 | `.mark` / `.underline-accent` | 文内强调 |
| 装饰 | `.rule(.thick/.accent)`、`.dots* / .dot-mat / .ring-mat / .hatch`、`.geo-dot/.geo-square/.geo-line` | 全部 currentColor + 低 opacity |
| 动态背景 | `canvas.ascii-bg` | 深色区粒子呼吸场，插首位即启动 |
| 图标 | `.ico/.ico-md/.ico-lg` stroke 1.4–1.8 | 线性 SVG，禁止填充色块图标 |
| 图片 | `.frame-img.r-*` + `.img-cap` | 直角无阴影，mono 图注 |

## 动效层

- **ASCII 点阵呼吸场（已内置）**：封面/封底深色区（accent / ink）的动态粒子背景。用法：在 `.canvas-card` 或 `.half` 内**首位**插入 `<canvas class="ascii-bg" aria-hidden="true">`，模板底部 IIFE 自动扫描启动。纯 canvas 2D 无依赖；sin/cos 噪声场驱动字符调色板 `   ...:::---+++***◦◦••▢▣` 显隐，`mix-blend-mode:screen` 在深色底上发亮；离屏 slide 自动降帧 1/4。
- **WebGL 漂移网格背景（未收录）**：源站在非 canvas 模式下还有一层全屏 WebGL 细网格 + 鼠标 accent 微光背景，canvas 模式下源站自身也将其移除。需要时从源站 `bootGL` 脚本提取。
- **入场编排（可选）**：源站用 Motion One + `data-animate="recipe"` 字典；模板默认静态即完整。需要动画时用 :root 里的 Carbon Motion tokens：productive `.2,0,.38,.9` / expressive `.4,.14,.3,1`，时长 70–700ms。
- 翻页过渡：`#deck{transition:transform .9s cubic-bezier(.77,0,.175,1)}`。

## QA 坑点记录

- 巨字必须 `min(vw,vh)` 双约束 + `line-height≤1.12`，否则 16:9 截图时超出安全区。
- 中文巨字字重 200 在 Windows 失效 → `is-win` 补偿 300（已内置）。
- 一页一个 accent 焦点：出现第二处 accent 块/ accent 柱即破坏风格。
- mono 标签永远大写 + 宽字距；中文与 mono 混排时中文留在 sans。
- `.step` / `.stat-card` 的顶边是**信息**（当前/重点用 3px accent，其余 2px currentColor 或 1px grey），不要加底色盒。
- 装饰点阵 opacity ≤.62，永不在正文正下方铺装饰。
- 响应式降级 `@media(max-width:900px)` 已内置（巨字放大、grid-12 降 6 列、pipeline 降 2 列）。
- 页码、章节名写在 `.chrome-min`，不另起页眉组件；底部 takeaway 用 `.t-meta` 一行写完。
