# 生命周期走查 — research_manager 填法实例

演示一个方向走完状态机，以及五种结局各长什么样。ID 和内容是虚构的。

## 主线路径：评估中 → 通过 → 进行中

1. **评估中**：`research_progress` 评估想法；建目录 `proposal/03-spatial-eval/`，含 `00-overview.md`（状态：评估中）和 `experiment-plan.md`。
2. **卡住（可选）**：查实现时发现帧采样代码拿不到 → 提案的 `00-overview.md` 状态改为卡住，记一行带日期的说明：缺哪个事实。不搬目录——卡住就留在 `proposal/`。
3. **通过**：事实查清，一项能改变决定的验证被论证清楚 → `research_manager` 把状态改为通过，等用户 GO。仍在 `proposal/`。
4. **进行中**：用户 GO → `experiment_manager` 报分支名给用户确认后创建 `exp/03-spatial-eval` + worktree，**只在该分支内**把目录挪到 `project/03-spatial-eval/`。`NN-slug` 这个 ID 搬动后不变；`global.md` 索引更新。

## 五种结局（archive/YYYY-MM-DD-NN-slug/）

- **否决**：没离开过 `proposal/`——价值检查发现没有真实价值。`research_manager` 直接归档提案目录；`experiment-plan.md` 里的评审记录就是最终文档，不要求 `REPORT.md`。
- **证伪**：跑了 E01–E04，事先登记的预期被稳定推翻。`experiment_manager` 合成 `REPORT.md`；报告包合回 base 分支；方向归档，`SUMMARY.md` 指向 `REPORT.md`。
- **验证通过**：达到做成标准。`promote/03-spatial-eval` 合入；证据保留；归档时 `REPORT.md` 写明验证过的适用范围和声明级别。
- **被取代**：跑到一半核心问题变了（修正项 → 协议重设计）。旧假设归档为被取代；新问题开**新的**提案编号；不改写历史。
- **放弃**：E02 时 GPU 预算被撤。非科学原因停下。方向在进行中，主要交付物仍是一份 `REPORT.md`（可以短），写明停止原因和停止时刻的证据边界；`SUMMARY.md` 指向它。运行报告原样保留。

## 走查中可见的通用规则

- 目录搬动和状态流转由 `research_manager`（或其委托下的 `experiment_manager`）执行——不动手乱挪。
- ID `03-spatial-eval` 全程不变；变的只有父目录和（归档时的）日期前缀。
- 每种结局恰好留一个主要交付物：没进过实验的方向留评审记录（否决/卡住），其余留 `REPORT.md`（证伪/验证通过/被取代/放弃）。
