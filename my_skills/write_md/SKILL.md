---
name: write_md
description: Markdown document readability enhancement guide. Uses inline HTML div boxes (Info/Claim/Concept/Step/Caution/Warning/Data Table/Code Example) + architecture diagrams + semantic color palette to achieve structured, scannable technical documents in pure Markdown renderers. Orthogonal to research_manager: write_md handles visual presentation, research_manager handles directory workflow. Use when writing or refactoring any Markdown document.
---

# Markdown Document Readability Enhancement Guide
> General conventions applicable to any Markdown document. Achieves structured, scannable documents in pure Markdown renderers via inline HTML div boxes + semantic color palette + architecture diagrams. **File structure, writing principles (one-sentence positioning, numbers-first, design rationale, etc.), and detail granularity: see [research_manager](research_manager).**

## 0. 职责边界

write_md 负责**视觉呈现层**（how——HTML 盒子、调色板、架构图）。**内容组织规范**（YAML frontmatter、导航栏、一句话定位、数字优先、设计理由、详略分级）见 [research_manager](research_manager) §4。两个技能正交但互补——写文档时通常需同时加载两者以覆盖完整的 what + how。

### Applicability: When to Use HTML Boxes vs Plain Markdown

### Use HTML boxes when
- The document is intended for **collaboration or review** — boxes provide fast-scan anchors
- It contains **multiple information types** that need visual distinction (e.g., claims vs warnings vs data)
- It exceeds 200 lines — boxes serve as visual signposts
- The target renderer **supports inline HTML** (GitHub README, GitLab Wiki, VS Code preview, Notion import, Typora, etc.)

### Plain Markdown is sufficient when
- Short documents (<100 lines) with a single information type — plain Markdown is cleaner
- The target platform **does not support inline HTML** (some chat tools, legacy wikis, plain-text readers)
- Temporary notes / drafts — add boxes later when migrating to formal documentation

## 1. Semantic Color Palette
Assign colors by semantic role; keep consistent across the project (or across documents):

| Semantic Role | Primary | Background | Typical Use |
|--------------|---------|------------|-------------|
| Title / Framework | `#2c3e50` | `#f8f9fa` | Architecture diagram title bar, core framework, document header |
| Info / Notes | `#3498db` | `#ebf5fb` | Supplementary notes, background information, external references |
| Success / Positive | `#27ae60` | `#eafaf1` | Success path, best practices, positive conclusions |
| Emphasis / Core | `#9b59b6` | `#f5eef8` | Core modules, critical flows, key content |
| Caution / Attention | `#e67e22` | `#fef9e7` | Considerations, constraints, pending decisions |
| Danger / Warning | `#e74c3c` | `#fdf2e9` | Failure modes, risks, prohibited actions |
| Auxiliary / Secondary | `#7f8c8d` | `#fafafa` | Arrows, secondary information, metadata, paths |

> Map semantic roles as needed per project, but keep "one color, one meaning."

## 2. Box Templates

### 2.1 Info Box
For supplementary notes, background information, external references, etc.:
```html
<div style="border-left:4px solid #3498db;padding:12px 16px;margin:12px 0;background:#ebf5fb;border-radius:0 8px 8px 0;">
<div style="color:#3498db;font-weight:bold;margin-bottom:4px;">Note</div>
Supplementary information or background context.
</div>
```

### 2.2 Claim Box
Dark left border, for listing key points, conclusions, or arguments:
```html
<div style="border-left:4px solid #2c3e50;padding:12px 16px;margin:12px 0;background:#f8f9fa;border-radius:0 8px 8px 0;">
1. Point one
2. Point two
</div>
```

### 2.3 Concept Box
Wrapper around a complete concept, with embedded info list and design rationale:
```html
<div style="border:1px solid #7f8c8d;border-radius:8px;padding:16px;margin:12px 0;background:#fff;">
<h3 style="margin:0 0 8px 0;font-size:1.17em;">Concept Title</h3>
<p>Body paragraph...</p>
<div style="background:#ebf5fb;padding:12px;border-radius:6px;margin:8px 0;">
Embedded info list
</div>
<p><strong>Design Rationale</strong>: explain why this choice was made.</p>
</div>
```

### 2.4 Step Box
Left border + bold colored title + monospace pseudocode, for flows/algorithms:
```html
<div style="border-left:4px solid #9b59b6;padding:8px 14px;margin:10px 0;background:#fafafa;border-radius:0 6px 6px 0;">
<div style="font-weight:bold;color:#9b59b6;margin-bottom:4px;">Step N: Title</div>
<div style="font-size:13px;font-family:monospace;line-height:1.8;">
Pseudocode / command / data flow
</div>
</div>
```

### 2.5 Caution Box
For considerations, constraints, or known issues:
```html
<div style="border-left:4px solid #e67e22;padding:12px 16px;margin:12px 0;background:#fef9e7;border-radius:0 8px 8px 0;">
<div style="color:#e67e22;font-weight:bold;margin-bottom:4px;">Caution</div>
Considerations, constraints, or known issues.
</div>
```

### 2.6 Warning Box
For high-risk items, prohibited actions, or critical issues:
```html
<div style="border-left:4px solid #e74c3c;padding:12px 16px;margin:12px 0;background:#fdf2e9;border-radius:0 8px 8px 0;">
<div style="color:#e74c3c;font-weight:bold;margin-bottom:4px;">Warning</div>
High-risk items, prohibited actions, or critical caveats.
</div>
```

### 2.7 Data Table Box
Narrow left border wrapping an HTML table, for parameters/specs/metrics. Since Markdown tables inside HTML `<div>` blocks are typically not parsed by renderers, use native HTML `<table>` inside data table boxes:
```html
<div style="border-left:3px solid #9b59b6;padding:8px 12px;margin:8px 0;background:#fafafa;">
<table style="width:100%;border-collapse:collapse;">
<thead>
<tr style="border-bottom:2px solid #9b59b6;">
<th style="padding:8px;text-align:left;">Column A</th>
<th style="padding:8px;text-align:left;">Column B</th>
</tr>
</thead>
<tbody>
<tr style="border-bottom:1px solid #ddd;">
<td style="padding:8px;">Value</td>
<td style="padding:8px;">Value</td>
</tr>
</tbody>
</table>
</div>
```
> If the colored border is not needed, use a plain Markdown table directly.

### 2.8 Code Example Box
Code block with a file-path header bar, for presenting key code snippets:
```html
<div style="border:1px solid #7f8c8d;border-radius:8px;overflow:hidden;margin:12px 0;">
<div style="background:#f8f9fa;padding:8px 14px;font-family:monospace;font-size:13px;color:#7f8c8d;">src/example.py</div>
<div style="padding:12px;background:#fafafa;">
<pre style="margin:0;"><code>def example():
    return "hello"</code></pre>
</div>
</div>
```

## 3. Architecture Diagram
Use nested HTML divs to simulate flowcharts: outer wrapper with title bar, inner modules as colored-bordered boxes, arrows as centered `↓` (vertical) or `→` (horizontal):
```html
<div style="border:2px solid #2c3e50;border-radius:10px;overflow:hidden;margin:16px 0;">
<div style="background:#2c3e50;color:#fff;padding:10px 16px;font-weight:bold;">Architecture Title</div>
<div style="padding:12px;">
<div style="border:2px solid #3498db;border-radius:8px;padding:10px 14px;margin:8px 0;background:#ebf5fb;">
<div style="color:#3498db;font-weight:bold;margin-bottom:6px;">Module Name</div>
<div style="font-size:13px;font-family:monospace;line-height:1.8;">Module content / data flow</div>
</div>
<div style="text-align:center;font-size:18px;color:#7f8c8d;margin:4px 0;">↓</div>
<div style="border:2px solid #27ae60;border-radius:8px;padding:10px 14px;margin:8px 0;background:#eafaf1;">
<div style="color:#27ae60;font-weight:bold;margin-bottom:6px;">Next Module</div>
<div style="font-size:13px;font-family:monospace;line-height:1.8;">Content</div>
</div>
</div>
</div>
```

> **Mermaid 标准图**: 流程图、时序图、类图、状态图、ER 图、甘特图等标准图类型使用 [research_visualize](research_visualize) 的 Mermaid 模式，共享本节的语义调色板。HTML div 盒子仅用于需要自由布局和颜色语义的非标准视觉化内容。

## 4. Table Enhancement
For tables that need visual emphasis, wrap them in a Data Table Box (§2.7). For plain Markdown tables:
- Use column alignment syntax `|:---|:---:|---:|` to make alignment explicit
- Separate header from body with `|---|`, keeping column counts consistent
- Consider using a list instead for single-column tables

## 5. Box Selection Guide
Recommended box combinations by document type. Limit to no more than 3 types per document:

| Document Type | Recommended Boxes | Pairing Notes |
|--------------|-------------------|---------------|
| Technical Proposal | Claim Box + Concept Box + Architecture Diagram + Data Table Box | Claim box for arguments, concept box for solution details, data table box for parameters |
| Plan / Roadmap | Step Box + Info Box | Step box for phases, info box for background |
| Report / Analysis | Info Box + Data Table Box + Caution Box | Data table box for metrics, info box for background, caution box for risks |
| README | Claim Box + Code Example Box | Claim box for features, code box for usage |
| Notes / Records | Info Box + Step Box | Light use; avoid architecture diagrams |
| Risk / Issue Doc | Warning Box + Claim Box | Warning box for risk levels, claim box for mitigation strategies |
