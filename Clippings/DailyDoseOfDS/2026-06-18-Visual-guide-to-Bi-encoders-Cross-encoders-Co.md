---
title: "Visual guide to Bi-encoders, Cross-encoders & ColBERT."
source: "https://mail.google.com/mail/u/0/#inbox/19edcc2a8ec8a790"
author:
  - "[[DailyDoseOfDS]]"
published: 2026-06-18
created: 2026-07-30
description: "直观对比文本对相似度计算的三大核心架构：Bi-encoders、Cross-encoders 与 ColBERT（晚期交互机制）。"
tags:
  - clippings
---
# Bi-encoder、Cross-encoder 与 ColBERT 架构直观指南（Visual guide to Bi-encoders, Cross-encoders & ColBERT.）

在自然语言处理（NLP）、信息检索（IR）与 RAG 文本匹配系统中，计算句对/文档相似度（Sentence Pair Similarity）是最核心的底层需求。本文直观对比三种最为主流的架构：

---

## 1. 双编码器（Bi-encoders）

![Bi-encoder 架构原理图解](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F94b1deaa-33c4-4030-9323-2f6051e040f8_934x1084.gif)

* **原理**：将 Query 与 Document 分别独立传入两个（或共享权重的）编码器中，各自生成固定维度的向量表示 $\mathbf{u}$ 和 $\mathbf{v}$。随后通过余弦相似度或点积计算得分：
  $$	ext{Score} = \cos(\mathbf{u}, \mathbf{v})$$
* **优点**：可以预先将海量文档编码并建立向量索引（如 FAISS/Milvus），检索速度极快 ($O(1)$ 查找)。
* **缺点**：编码过程中 Query 与 Document 没有任何 Token 级别的交互，跨语义表达能力受限。

---

## 2. 交叉编码器（Cross-encoders）

![Cross-encoder 架构原理图解](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F8f5ba20b-725d-44ad-9902-b0cb88d05f78_933x333.gif)

* **原理**：将 Query 与 Document 拼接为单个序列 `[CLS] Query [SEP] Document` 输入 Transformer 模型中，允许每个 Token 之间在所有注意力层中进行完全的自注意力（Self-attention）交叉计算。
* **优点**：准确率极高，能够捕捉微小的语义差异与上下文匹配关系。
* **缺点**：计算复杂度高，无法预先计算向量，仅能用于重排序（Reranking）阶段。

---

## 3. 晚期交互模型（ColBERT / Late Interaction）

![ColBERT 晚期交互架构图解](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa564dd5e-a21f-4b30-9323-2f6051e040f8_933x342.gif)

![ColBERT MaxSim 匹配图解](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fcfff0681-bc0f-416e-89b7-436e21f8c52e_933x348.gif)

* **原理**：结合了前两者的优势。Query 和 Document 分别独立编码生成 **多向量序列（Multi-vector sequence）**。在最终打分阶段，通过 MaxSim 算子计算局部注意力相似度：
  $$	ext{Score}(Q, D) = \sum_{i \in |Q|} \max_{j \in |D|} \left( \mathbf{E}_{q_i} \cdot \mathbf{E}_{d_j}^T ight)$$
* **优势**：既保持了预编码索引的快速检索能力，又获得了接近 Cross-encoder 的 Token 级丰富匹配精度。
