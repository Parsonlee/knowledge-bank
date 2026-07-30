---
title: "RAG & Fine-tuning, explained visually"
source: "https://mail.google.com/mail/u/0/#inbox/19b5c7637722a2ba"
author:
  - "[[DailyDoseOfDS]]"
published: 2025-12-26
created: 2026-07-30
description: "通过直观对比分析 RAG（检索增强生成）与 Fine-tuning（微调）在知识获取、模型行为定制、成本与时效性方面的技术选型路径。"
tags:
  - clippings
---

# 图解 RAG 与微调（RAG & Fine-tuning, explained visually）

如果你正在构建真实的大语言模型（LLM）应用，几乎很少能直接将预训练模型开箱即用而不做任何调整。

开发者通常将 RAG（检索增强生成）和微调（Fine-tuning）视为可互换的选项，但实际上并非如此。

RAG 和微调解决的是根本不同的问题。一个控制模型在运行时（Runtime）**知道什么**，另一个则改变模型默认的**行为方式**。

下图清晰拆解了两者区别：

![RAG 与微调对比原理图](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa087ec4e-141a-477e-87fb-58cd5f07dfd0_960x995.gif)

---

### RAG 的工作原理

参考图解的上半部分。

RAG 作用于推理阶段（Inference time）。当用户发送查询时，检索器（Retriever）会在你的知识库（PDF、向量数据库、API、文档）中进行搜索，提取相关的上下文，并将该上下文与查询一起传递给 LLM。在此过程中，**模型的权重从未改变**。你实际上是在运行时为 LLM 提供了一张“开卷考试参考纸”。

---

### 微调的工作原理

微调则截然不同。参考图解的下半部分。

微调发生在离线训练阶段（部署之前）。你在特定领域的训练数据集上对模型进行训练，**模型的权重会发生真实更新**。模型从此具备了不同的默认行为方式。

微调的目的在于改变模型的行为表现：包括其语气、词汇、回答结构或特定的推理模式。

![RAG 与微调技术选型决策矩阵](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6856e33e-5983-4a03-a344-9135ea6f5b50_2400x1317.png)

---

### 选型思考：如何选择？

两个关键问题决定了你的技术路径：

1. **你的任务需要多少外部知识？**
2. **你需要多大程度的行为定制？**

* 如果你需要模型引用特定的文档、产品目录或任何频繁更新的信息，这主要属于 **RAG** 的范畴。
* 如果你需要模型采用企业内部特定术语、匹配特定写作风格或遵循特定领域的推理范式，这主要属于 **微调** 的范畴。

例如，LLM 可能难以总结公司内部会议记录，因为发言者使用了模型从未见过的内部术语。微调可以完美解决这一问题。

话虽如此，在实际生产系统中，你往往需要结合使用两者。例如，客服机器人可能需要从文档中检索答案（RAG），同时以符合品牌声调的语气做出回应（微调）。

---

### 核心结论

* **RAG** $ightarrow$ 模型应该知道什么？（What should the model know?）
* **微调** $ightarrow$ 模型应该如何表现？（How should the model behave?）

它们不是竞争关系，而是 LLM 架构栈中互补的两个层级。
