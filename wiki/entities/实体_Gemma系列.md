---
type: entity
tags:
- LLM/arch
summary: Google DeepMind 研发的 Gemma 系列开源大语言模型家族，涵盖 Gemma 1、Gemma 2、Gemma 3 以及端侧优化的 Gemma 3n。
sources:
- wiki/sources/2025年七大顶流大模型架构.md
- wiki/sources/HuggingFace手把手训练大模型实战指南.md
- wiki/sources/从DeepSeek-V3到Kimi_K2_八种现代LLM架构大比较.md
updated: '2026-08-26'
---

# 实体：Gemma 系列（Gemma Family）

## 概述

**Gemma 系列** 是由 Google DeepMind 研发并开源的轻量级开放大语言模型家族。该系列基于构建 Gemini 模型的相同研究与技术基础打造，涵盖 1B / 4B / 12B / 27B 等多种规模规格，并在性能与计算效率之间取得了优异平衡。

---

## 核心架构创新（Gemma 3 为例）

1. **混合局部滑动窗口注意力（Sliding Window Attention）**：
   - 采用全局注意力与局部滑动窗口注意力的周期性交替设计（全局 : 局部 = 1 : 5）。
   - 局部窗口收敛至 1024（相较于 Gemma 2 的 4096 进一步缩窄），在极大降低超长上下文推理 KV Cache 显存开销的同时，保持了高质量的语义建模能力。
2. **Pre+Post Norm 双层 RMSNorm**：
   - 在每个 Attention 与 FFN 计算块的前后各挂载一层 RMSNorm 归一化层，兼具了 Pre-Norm 的深层网络训练稳定性与 Post-Norm 的强表征能力。
3. **分组查询注意力（GQA）**：
   - 全系标配 GQA，加速推理解码并降低显存带宽压力。

---

## 端侧优化（Gemma 3n 移动端）

- **逐层流式嵌入（Per-Layer Embedding, PLE）**：特定 Token 层嵌入可从 CPU 内存或 SSD 按需流式传输，显著削减移动设备常驻显存。
- **MatFormer 弹性架构**：允许单一大模型动态切片为更小尺寸的独立子模型，适应多变设备算力。

---

## 相关概念与文献

- [[wiki/concepts/概念_滑动窗口注意力|概念_滑动窗口注意力]]
- [[wiki/sources/2025年七大顶流大模型架构|2025年七大顶流大模型架构]]
- [[wiki/sources/从DeepSeek-V3到Kimi_K2_八种现代LLM架构大比较|从DeepSeek-V3到Kimi_K2_八种现代LLM架构大比较]]
- [[wiki/sources/HuggingFace手把手训练大模型实战指南|HuggingFace手把手训练大模型实战指南]]
