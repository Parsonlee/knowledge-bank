---
type: concept
tags:
  - CV/arch
summary: adaLN-Zero 是 DiT 中表现最优的条件注入方式——用时间步/类标签回归出归一化的缩放/移位参数及额外的缩放系数 α，初始化 α=0 使每个 Block 起始为恒等映射。
sources:
  - "wiki/sources/DiT_扩散模型与Transformer.md"
created: "2026-06-26"
updated: "2026-06-26"
confidence: high
---

# 概念：adaLN-Zero Block

## 定义

Adaptive Layer Norm (adaLN) 遵循 GAN 中的自适应归一化层，不直接学习缩放/移位参数 γ、β，而是用噪声时间步 t 和类标签 c 回归得到。adaLN-Zero 在此基础上额外回归缩放系数 α，并初始化 MLP 使 α 全为 0，从而使 DiT Block 初始化为恒等函数（Identity Function）。

## 要点

- 灵感来自：有监督学习中对每个 Block 第一个 BN 缩放因子做 Zero-Initialization 可加速大规模训练
- 在 DiT-XL/2 实验中：adaLN-Zero（118.6 GFLOPs）取得最低 FID，且计算最高效
- 400K 迭代时 adaLN-Zero 的 FID 几乎是 In-Context 的一半，说明条件策略严重影响模型质量
- 初始化为恒等映射的性能大大优于普通 adaLN，DiT 后续实验一直采用 adaLN-Zero

## 关联

- [[DiT_扩散模型与Transformer]]（来源）
