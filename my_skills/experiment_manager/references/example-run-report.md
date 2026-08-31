# Example Run Report — experiment_manager §4 Schema Filled

Reference-only: a complete instance of `ENN-experiment-report.md` per `experiment_manager` §4, including the §4a visual acceptance record. Direction and numbers are fictional.

---

# E03-experiment-report

- **Question**: 偏差修正项能否从中间层表征估计并提升协议一致性？
- **Experiment ID**: E03  **Main contradiction**: 探针信号存在（E01）但完整评测未复现提升——分歧在"修正项失效"还是"评测协议淹没了修正效果"
- **Base commit**: `a41c9e2`  **Controlled change**: 仅评测管线接入修正项；模型、数据、采样与 E02 逐字节一致

## Setup, data, controls, reproducibility

- Data: VSI-Bench 子集 1000 题（E01 注册划分）；seed 17/18/19 三次独立运行。
- Controls: 未修正子集 500 题（区分"修正有效"与"题目变简单"）；baseline = E02 冻结产物。
- Framework/hardware: torch 2.4, 1×A100, 推理 3.1h/run；配置 `configs/e03.yaml`（已提交）。

## Data-quality and adequacy audit

- 观测单位：题目；独立运行间无共享采样。缺失率 0.4%（4 题渲染失败，已记录并从分母剔除）。
- 充分性三问：实验可区分"修正失效"vs"协议淹没"（对照子集）；会削弱声明的指标 = 对照子集准确率变化；当前评测满足两者。

## Baseline / expected / actual

| Metric | Baseline (E02) | Expected (pre-registered) | Actual | Deviation | Interpretation |
|---|---:|---:|---:|---:|---|
| 修正子集准确率 | 61.2 ± 1.1 | 66–70 | 67.8 ± 0.9 | 在预期内 | 修正项在受控协议下有效 |
| 对照子集准确率 | 61.0 ± 1.2 | 不变 (60–62) | 58.4 ± 1.3 | **低于预期** | 协议外题目被修正项拖累 |

## Mechanism prediction vs observed signals

预测：中间层探针 AUC 高 → 修正项激活率与误差下降正相关。观测：激活率 0.71，激活样本误差下降 12pp，未激活样本上升 3pp → **干预→机制环成立；机制→目标环在对照子集断裂**（修正项对无偏差题目产生过修正）。

## Selected figures

- `03-plot-bea-accuracy.pdf`（evidence）: baseline–expected–actual 区间对比，观测单位=题目，误差棒为三次运行的观测范围（非 CI）。
- `04-diagram-correction-path.svg`（explanatory）: 修正项介入点与断裂环标注。

## Statistical analysis

配对 bootstrap（题目级重采样，10000 次）：修正子集 +6.6pp [4.9, 8.3]；对照子集 −2.6pp [−4.4, −0.8]。多重比较：两个预设主指标，Bonferroni 校正后结论不变。实用显著性：修正子集效应超过 5pp 决策阈值，对照子集负效应构成新约束。

## Deviation and failure-mechanism analysis

对照子集低于预期。候选解释：

| Candidate | Supporting | Contradicting | Confidence | Discriminating next test |
|---|---|---|---|---|
| 修正项对无偏差题目过修正 | 未激活样本误差上升 | 未激活样本仅 +3pp，不足以解释全部 | medium | E04：修正项加置信门限 |
| 对照子集难度漂移 | 无 | baseline 复算一致 | low | — |

## 收敛记录

| 项 | 运行前 | 运行后 |
|---|---|---|
| 主要假设 | 修正项有效 | 有依据（限受控协议） |
| 活着的解释 | 3 | 2（排除"协议淹没"） |
| 最大不确定性 | 协议是否淹没修正 | 已解决；新的主导不确定：过修正边界 |
| 主要矛盾 | 修正失效 vs 协议淹没 | 更新为：修正项的选择性不足 |
| 暂存的问题 | 0 | 1（门限形式，不自动激活） |
| 下一步决定 | 未知 | 继续（E04 判别测试） |

## 事实 / 推断 / 猜测

- 事实：上表全部数字，来自 `logs/e03/*.jsonl`（清单见下）。
- 推断：过修正是对照子集下降的主因（两个独立信号一致）。
- 猜测：置信门限能同时保住修正子集收益——未经检验。

## Experiment value / verdict / next action

- **实验价值: 有信息**（排除一个解释，更新主矛盾）。
- 方向判定: 继续。下一步：E04 置信门限判别测试，预期已登记于方向计划。

## Visual manifest and retain/discard manifest

- Retain: `03-plot-bea-accuracy.{py,pdf,png}`, `04-diagram-correction-path.svg`（evidence/explanatory）。
- Discard: 中间渲染 12 张诊断图（diagnostic，已清理）；大型 logits dump 未入库，manifest 记录外部 URI + checksum。

## §4a Visual acceptance record

- Visual audit (from `result_analysis` §9): candidates 3 — BEA 区间图（selected）、修正路径图（selected）、逐题散点（rejected: 2000 点无增量信息，表已足够）。
- 两张选中图均由 `result_visualization` 产出，bundle 完整（.py/.pdf/.png）。
- Markdown 引用链接已解析；Chromium 截图检查通过，无破图。
- Caption 均含对比、观测单位、不确定性语义、结论。无整屏文字墙。
