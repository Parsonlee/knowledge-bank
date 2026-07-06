---
type: concept
tags:
- LLM/training/post-train
created: '2026-06-29'
updated: '2026-06-29'
summary: 对 LLM 进行对齐训练（SFT/RLHF）后，模型在原有推理与知识任务上出现性能下降的代价，也称灾难性遗忘在对齐场景下的具体表现。
sources:
- raw/万字解构“幻觉陷阱”：大模型犯的错，会摧毁互联网吗？丨 AGI 之路 04 期 ....md
- raw/后训练认知：SFT vs RL—关于记忆和遗忘机制.md
- wiki/sources/后训练认知_SFT_vs_RL_记忆与遗忘机制.md
---


# 概念：Alignment Tax（对齐税）

## 定义

对 LLM 进行对齐训练（SFT/RLHF）后，模型在原有推理与知识任务上出现性能下降的代价，也称灾难性遗忘在对齐场景下的具体表现。

## 核心观点

- 对齐越彻底，记忆越脆弱
- 不是不可避免的——研究表明 RL（on-policy）训练可以大幅消除这一代价
- 代价来源于**数据分布错位**，而非对齐目标本身

## 关联

- [[概念_灾难性遗忘]]
- [[概念_on-policy与off-policy数据]]
- [[后训练认知_SFT_vs_RL_记忆与遗忘机制]]