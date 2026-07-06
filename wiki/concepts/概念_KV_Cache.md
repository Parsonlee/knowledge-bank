---
type: concept
tags:
- Infra/AI
- LLM/inference
summary: KV Cache 缓存 LLM 推理中 X@W_K 和 X@W_V 的已计算结果，空间换时间，避免自回归逐 token 生成时对历史 token
  的重复计算。几乎所有 LLM 推理框架（如 vLLM）均已支持。
sources:
- raw/2025年七大顶流大模型架构.md
- raw/Mamba Explained _ Kola Ayonrinde.md
- raw/Mamba2_ SSM和Transformer的大一统 - 知乎.md
- raw/MiniMax和Kimi为了“注意力”，隔空交手.md
- raw/一文讲明白大模型显存占用（只考虑单卡） - 知乎.md
- raw/入局AI Infra：程序员必须了解的AI系统设计与挑战知识.md
- raw/大模型推理加速：看图学KV Cache - 知乎.md
- raw/大模型算法岗，面试百问百答.md
- wiki/sources/2025年七大顶流大模型架构.md
- wiki/sources/DeepSeek_MLA矩阵吸收原理.md
- wiki/sources/KV_Cache原理图解.md
- wiki/sources/LLM面试50题_MIT_CSAIL.md
- wiki/sources/MCP遇上代码执行.md
- wiki/sources/Mamba_Explained_Kola_Ayonrinde.md
- wiki/sources/Manus创始人手把手拆解上下文工程.md
- wiki/sources/MiniMax_vs_Kimi_注意力路线之争.md
- wiki/sources/Transformer大模型3D可视化_NanoGPT.md
- wiki/sources/从DeepSeek-V3到Kimi_K2_八种现代LLM架构大比较.md
- wiki/sources/入局AI_Infra系统设计与挑战.md
- wiki/sources/大模型显存占用单卡分析.md
- wiki/sources/大模型显存计算公式与优化.md
- wiki/sources/推测解码Speculative_Decoding综述.md
created: '2026-06-29'
updated: '2026-06-29'
confidence: high
---


# 概念：KV Cache

## 定义

KV Cache 是 LLM 推理优化的核心机制。LLM 自回归生成时，每次推理都需将之前生成过的 token 重新输入模型计算 Key 和 Value，复杂度为 O(N²) 存在大量重复计算。KV Cache 将已计算的 K/V 矩阵缓存，后续只需计算新增 token 的 K/V 并拼接，以空间换时间减少计算量。

## 原理

- LLM 模型结构（因果注意力）使得历史 token 的 K/V 计算结果不变
- 缓存 X@W_K 和 X@W_V 的结果上半部分（历史 token 部分）
- 每步仅需计算当前新 token 的 K/V，与缓存拼接后执行注意力计算

## 适用条件

- **仅适用于 Decoder 架构**（有 Causal Mask）
- Encoder 的 K/V 不可缓存，因为输入会整体变化

## 显存代价

$$\text{KV Cache} = 2 \times L \times H \times D \times S \times B \times \text{bytes}$$

示例：batch=32, head=32, layer=32, dim=4096, seq=2048, float32 → **约 64GB**

## 优化方向

| 方案 | 原理 |
|------|------|
| GQA/MQA | 减少头数，共享 K/V |
| MLA | 低秩压缩 K/V |
| Linear Attention | 无需 KV Cache |
| 量化 | K/V 低精度存储 |
| 滑动窗口 | 仅保留近邻 K/V |

## 关联

- [[入局AI_Infra系统设计与挑战]]（来源）
- [[KV_Cache原理图解]]（详细图解来源）
- [[概念_MLA低秩KV压缩]]
- [[MiniMax_vs_Kimi_注意力路线之争]]
- [[实体_vLLM]]
- [[概念_自注意力复杂度]]