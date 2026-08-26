---
type: concept
tags:
- RAG/retrieval
- AI-Agent/coding
summary: REFRAG 是 Meta AI 提出的一种在向量层面进行压缩与过滤的 RAG 检索优化框架，能够显著提高首字生成时间（TTFT），并减少冗余 token
  开销。
sources:
- wiki/sources/2026-03-24_RAG-vs-MetaAI's-REFRAG_19d21b.md
updated: 2026-08-04
---

# 概念: REFRAG (RAG 压缩与过滤)

## 1. 传统 RAG 的开销痛点
在传统的检索增强生成（RAG）管道中，当用户提出查询时，系统会将查询向量化，检索向量数据库并召回最相似的若干个文本块（Chunks），然后将这些召回的全部文本直接拼接到 LLM 的提示词上下文中。
这种经典模式存在以下缺陷：
- **Token 浪费**：检索出的 Chunks 中通常包含大量冗余、不相关或者对回答无用的文本，导致 LLM 需要处理远超必要的 tokens。
- **延迟高（TTFT）**：由于上下文过长，LLM 预填充（Prefill）阶段耗时增加，首字时间（Time-to-First-Token）严重恶化。
- **运行成本昂贵**：API 计费或推理算力与输入的 token 数量成正比，大量无用信息造成了严重的计算资源浪费。

## 2. REFRAG 架构及其四大机制
为了解决上述问题，Meta AI 提出了 **REFRAG**。它在向量层面（Vector level）对上下文进行压缩和过滤，主要包括以下四大核心机制：

1. **块压缩 (Chunk Compression)**：
   不同于传统的以多个 token 向量表示一个文本块的做法，REFRAG 将每个 Chunk 编码为一个单一的压缩嵌入向量（Single compressed embedding），从而使得整个 Chunk 的信息能够在极小的空间内被表征。
2. **强化学习相关性策略 (Relevance Policy)**：
   引入一个基于强化学习（RL）训练的轻量级策略网络。该策略网络评估这些压缩的单向量，快速识别相关性最高的文本块并进行过滤，剔除掉冗余或无关的文本块。
3. **选择性展开 (Selective Expansion)**：
   只有经过强化学习策略筛选并判定为高相关的文本块，才会被重新展开为原本的多 token 细粒度嵌入（Token-level representation），其余被拒绝的块则保持压缩状态。
4. **混合拼接机制 (Hybrid Concatenation)**：
   最后，REFRAG 将以下三部分进行拼接，作为最终输入发送给 LLM 解码器：
   - 原始查询（Query）的 token 级别表示
   - 被选中的高相关 Chunks 的 token 级别表示
   - 被拒绝的 Chunks 的压缩单向量表示（用于保留全局背景信息，但仅占用极少 token 资源）

## 3. 性能收益与优势
根据 Meta AI 论文的研究数据，REFRAG 在保持相同准确率的情况下实现了以下指标的突破：
- **TTFT 提速**：首字时间（Time-to-First-Token）相较于经典模式提升了 **30.85x**，比之前的 SOTA 模型快了 3.75x。
- **Token 消耗减少**：相比 LLaMA 模型，在 16 个 RAG 基准测试中仅使用了 **2 到 4 倍更少的 decoder tokens**。
- **更宽的上下文**：支持高达 **16x 宽度的上下文窗口**。
- **无精度损失**：在问答、摘要、多轮对话等各类 RAG 任务中，精度完全没有下降。

---
> 📎 **来源摘要**：[[wiki/sources/2026-03-24_RAG-vs-MetaAI's-REFRAG_19d21b.md]]
