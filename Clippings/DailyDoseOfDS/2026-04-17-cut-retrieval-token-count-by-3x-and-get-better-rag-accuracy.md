---
title: "Cut retrieval token count by 3X and get better RAG accuracy too"
source: "https://mail.google.com/mail/u/0/#inbox/19d9d1a7d44f86a9"
author:
  - "[[DailyDoseOfDS]]"
published: 2026-04-17
created: 2026-07-30
description: "介绍如何通过 Blockify 智能分块与语义去重技术，在检索阶段降低 3 倍 Token 消耗，同时消除冗余信息干扰以提升 RAG 系统回答准确率。"
tags:
  - clippings
---
# 降低 3 倍检索 Token 消耗并同时提升 RAG 准确率（Cut retrieval token count by 3X and get better RAG accuracy too）

大多数 RAG（检索增强生成）系统的成本优化都集中在模型层——例如选用更小的模型、减少调用次数以及采用批处理。

然而，**检索得到的 Payload（载荷）本身却极少被系统性评估和优化**。

一个典型的 RAG 架构通常在每次查询时检索 5 个文档 Chunk（分块），每个 Chunk 大约包含 300 Token。这意味着在大语言模型（LLM）输出单字之前，仅输入端就已消耗了 **1,500 个 Input Token**。在规模化运行下，这一开销会成倍复合增加。

比成本更严重的问题是**准确率下降**。企业级文档往往会在不同版本的多个文件中复述相同的事实：

![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fea92b433-d922-4872-89e4-a1edb6fd6ff8_1200x1109.png)

当检索到的多个 Chunk 包含同一事实的微小差异或冗余描述时，输入上下文不仅被无意义地塞满，大模型在推理过程中也极易受到冗余信息的干扰误导。

### 解决方案：Blockify 智能分块与去重

为解决这一难题，可通过在索引与检索阶段引入智能 Blockify 机制：
1. **打破固定窗口分割**：不再依赖固定 Token 长度的粗暴硬切割，而是识别文档的结构化语义 Block。
2. **语义层面去重与压缩**：在向量组装阶段自动识别并合并不同文件中的重复事实与冗余段落。

通过 Blockify 处理：
- **检索 Token 数降低 3 倍**：上下文 Payload 显著瘦身，大幅削减 API 账单与 Prompt 延迟。
- **准确率显著提升**：消除了矛盾与冗余信息的干扰，使 LLM 能精准聚焦于核心事实上下文。
