---
type: concept
tags:
  - CV/arch
summary: Patchify 是 ViT/DiT 的第一步——将图像（或 latent）切分为 patch 并经线性嵌入变为 token 序列；patch size p 决定 token 数量与计算量。
sources:
  - "wiki/sources/DiT_扩散模型与Transformer.md"
created: "2026-06-26"
updated: "2026-06-26"
confidence: high
---

# 概念：Patchify

## 定义

DiT 第 1 步与 ViT 一致：把输入（在 DiT 中是 latent z）切分为 patch，经 Linear Embedding 变为多个 d 维 token，并加上基于 ViT 的 sine-cosine 频率位置编码。

## 要点

- token 数量 T 由 patch 大小 p 决定，满足 T = (I/p)^2
- patch 大小 p 越小，token 数 T 越大；p 减半使 T 变为 4 倍，计算量也变为 4 倍
- p 对 GFLOPs 有显著影响，但对参数量影响很小
- DiT 设计空间使用 p ∈ {2, 4, 8}

## 关联

- [[DiT_扩散模型与Transformer]]（来源）
- [[概念_Vision_Transformer]]
