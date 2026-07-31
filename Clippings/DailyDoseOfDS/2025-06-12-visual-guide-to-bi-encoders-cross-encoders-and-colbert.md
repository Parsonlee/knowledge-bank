---
title: "Bi-encoder、Cross-encoder 与 ColBERT 可视化指南"
source: "https://mail.google.com/mail/u/0/#inbox/197658945bda228b"
author:
  - "[[DailyDoseOfDS]]"
published: 2025-06-12
created: 2026-07-30
description: "介绍 NLP 成对文本评分中的 Cross-encoder、Bi-encoder 和 ColBERT：三者分别在语义表达能力、离线索引可扩展性与 token 级延迟交互之间权衡。"
tags:
  - clippings
---

# Bi-encoder、Cross-encoder 与 ColBERT 可视化指南

许多真实 NLP 系统都会以某种形式依赖成对句子（或上下文）的评分，例如 [RAG 系统](https://www.dailydoseofds.com/a-crash-course-on-building-rag-systems-part-1-with-implementations/)、问答系统和重复文本检测系统。邮件用可视化内容呈现了业界处理此问题的三种常见方法。

作者还提供了相关实现文章：[用于句对相似度评分的 Bi-encoder 与 Cross-encoder](https://www.dailydoseofds.com/bi-encoders-and-cross-encoders-for-sentence-pair-similarity-scoring-part-1/)、[用于句对相似度评分的 AugSBERT](https://www.dailydoseofds.com/augsbert-bi-encoders-cross-encoders-for-sentence-pair-similarity-scoring-part-2/) 以及[深入理解 ColBERT 与 ColBERTv2 以改进 RAG 系统（含实现）](https://www.dailydoseofds.com/a-crash-course-on-building-rag-systems-part-8-with-implementation/)。

## 1. Cross-encoder

Cross-encoder 在概念上是最强大的方法之一：

- 将查询文本与文档文本拼接；
- 使用 BERT 类编码器进行编码；
- 对 `[CLS]` token 表示施加变换（一个 dense layer），得到相似度分数。

模型会同时关注两份上下文，因此生成的语义表示极具表达力。但它无法扩展：如果有 10 亿篇文档，为了判定某个查询最相关的文档，就必须进行 10 亿次前向传播。

## 2. Bi-encoder

Bi-encoder 分别编码查询和文档，并计算查询 `[CLS]` token 与文档 `[CLS]` token 之间的余弦相似度。

由于文档嵌入可离线计算，它具有很高的可扩展性；但也失去了所有交互，只能“希望”查询和文档的全部信息都已被 `[CLS]` token 良好地概括。

## 3. ColBERT

ColBERT 将 Cross-encoder 的能力与 Bi-encoder 的可扩展性结合起来：

- 分别编码查询和文档；
- 计算一个延迟交互矩阵，其中包含所有查询 token 与所有文档 token 之间的相似度分数（点积）；
- 对每个查询 token，取其在全部文档 token 上的最大分数；
- 将这些最大分数求和，得到匹配分数。

它的优点是：像 Bi-encoder 一样，文档嵌入可离线计算，因而高度可扩展；像 Cross-encoder 一样，它保留了查询 token 与文档 token 的跨交互，这种机制称为**延迟交互（late interaction）**。

作者最后询问读者：ColBERT 还有哪些优势？
