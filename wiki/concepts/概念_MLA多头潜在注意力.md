---
type: concept
tags:
  - LLM/arch
created: "2026-06-29"
updated: "2026-06-29"
---

# 概念_MLA多头潜在注意力

MLA（Multi-Head Latent Attention，多头潜在注意力）是 DeepSeek-V2 首次引入的注意力变体，用于减少 KV Cache 内存占用，同时保持或提升建模性能。

## 核心思想

与 GQA 通过共享 K/V 头减少内存不同，MLA 将 K 和 V 张量压缩到低维潜在空间，然后存储压缩后的张量：

- 推理时，压缩的 K/V 表示会被投影回原始尺寸再使用
- 额外增加一次矩阵乘法，但 KV Cache 内存显著降低
- 训练时 Q 也压缩，推理时 Q 不压缩

## 与其他注意力方案对比

| 方案 | KV Cache 大小 | 建模性能 | 复杂度 |
|------|--------------|----------|--------|
| MHA | 最大 | 基准 | 低 |
| GQA | 中等（共享 K/V 头） | 略低于 MHA | 低 |
| MLA | 最小（压缩 K/V） | 优于 MHA | 中等 |

来源：DeepSeek-V2 消融研究。

## 应用模型

- DeepSeek-V2、DeepSeek-V3、DeepSeek-R1
- Kimi K2（基于 DeepSeek-V3 架构扩展）

## 相关来源

- [[从DeepSeek-V3到Kimi_K2_八种现代LLM架构大比较]]
- [[2025年七大顶流大模型架构]]

## 关联概念

- [[概念_自注意力复杂度]] — 注意力机制的基础复杂度分析
- [[概念_KV_Cache]] — KV Cache 原理
- [[概念_MoE混合专家]] — DeepSeek-V3 另一核心组件
- [[实体_DeepSeek-V3]] — MLA 应用模型
