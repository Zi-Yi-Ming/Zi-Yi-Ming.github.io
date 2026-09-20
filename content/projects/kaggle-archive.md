---
title: "Kaggle Archive"
date: 2026-09-04
weight: 25
description: "Kaggle 竞赛实验与研究归档：把竞赛里的数据处理、特征/建模实验与复盘沉淀成可回看、可复用的记录。"
tech: ["Kaggle", "Python", "ML"]
status: "研究归档 · 持续更新"
github: "https://github.com/Zi-Yi-Ming/kaggle-archive"
---

Kaggle 竞赛实验与研究归档：把做过的竞赛题、实验脚本和复盘按仓库沉淀下来，方便回看与复用。

定位是研究归档，不是封装好的软件产品——重点是过程记录本身：数据怎么处理、特征与建模实验怎么做的、哪些思路有效、哪些踩了坑。实验结论与代码一并保留，作为后续竞赛和研究的参考。

## 收录范围

仓库已归档 10 个无奖牌或已完赛的比赛，每个比赛一个目录，统一四段式复盘：**Result（Metric / Best Score / Key Finding）→ 结果记录 → 深度复盘（失败实验档案）→ 方法论经验**。活跃奖牌赛（kaggriculture / rsna_knee）赛期内不公开，赛后归档。

## 精选案例

- **Titanic — 对照线思维**：891 行小样本，本地 CV 0.83 与公开榜 ~0.76 脱节后，学会「分数必须与规则对照线（性别基线）在相同折上比较」，最终胜出的是 4 特征的最简模型
- **Store Sales — 提交正确性**：lag/rolling 特征 +0.04 进头部区间，但两次「本地完全看不出来」的灾难分（提交 id 错位 -3.50、测试滞后特征 NaN 塌陷 -1.76）证明——提交正确性与模型质量是两件事
- **Smartphone Addiction (S6E8) — OOF 混合**：69 万行合成表格，单模型调参到顶后，真正的收益来自 74 模型异构集成 + 拼接社区公开 OOF 库（rank 归一化解决 log-odds 量纲陷阱），公开榜 0.97033

完整学习路径（Baselines → 特征工程 → 时序 → CV → NLP → 赛制博弈）与全部比赛档案见 [GitHub 仓库](https://github.com/Zi-Yi-Ming/kaggle-archive)。
