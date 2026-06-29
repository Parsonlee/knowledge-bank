---
type: concept
tags:
  - LLM/arch/MoE
  - LLM/arch
---

# 概念：gpt-oss 架构特征

OpenAI gpt-oss-20b/120b 的关键架构设计，相比 GPT-2 的 7 项进化与和 Qwen3 的对比。来源：[[从GPT-2到gpt-oss_OpenAI开放模型进化之路]]

## 相比 GPT-2 的 7 项架构进化

| 变化 | 原因 |
|------|------|
| 去除 Dropout | LLM 单轮训练，每 token 只见一次，过拟合风险极低 |
| RoPE 取代绝对位置嵌入 | 旋转编码更适合外推，随 LLaMA 广泛采用 |
| SwiGLU 取代 GELU | 3个FC替代2个，参数更少（8.39M→3.15M），乘法交互提升表达力 |
| MoE 取代单前向模块 | 稀疏激活，增加容量同时保持推理高效 |
| GQA 取代 MHA | 共享 K/V 头，降低参数量和 KV Cache 内存带宽 |
| 交替滑动窗口注意力 | 每隔一层用 128-token 窗口局部 GQA，大幅降低内存 |
| RMSNorm 取代 LayerNorm | 省去均值计算，减少 GPU 通信开销 |

## gpt-oss vs Qwen3：宽度与深度权衡

- **gpt-oss-20b**：24 层，嵌入维度 2880（更宽）
- **Qwen3-30B-A3B**：48 层，嵌入维度 2048（更深）

宽模型优势：推理吞吐量更高（更高并行度），但内存占用更大。Gemma 2 消融研究表明同等参数下宽模型略优（52.0 vs 50.8）。

## 专家设计：少量大专家 vs 大量小专家

- gpt-oss-20b：32 个专家，每 token 激活 4 个
- Qwen3-30B-A3B：128 个专家，每 token 激活 8 个

近期趋势（DeepSeekMoE 等）倾向大量小专家。gpt-oss 少专家可能是 20B 规模的副产物，120B 版本已增加专家数量。两者均无共享专家（不同于 DeepSeek）。

## 注意力 Sinks

可学习的 per-head bias logits，附加到注意力分数中，稳定长上下文注意力。不修改 token 化输入，是对传统序列开头"始终关注 token"的实现变体。

## MXFP4 量化

对 MoE 专家权重使用 MXFP4 量化，使 120B 模型可在单块 80GB H100 运行，20B 可在 16GB RTX 50 系列运行。

## 关联

- [[概念_MoE混合专家]] — gpt-oss 的 MoE 专家层
- [[概念_滑动窗口注意力]] — 交替 128-token 局部 GQA
- [[概念_RoPE位置编码]] — 取代绝对位置嵌入
- [[实体_gpt-oss]] — 具体模型实体
