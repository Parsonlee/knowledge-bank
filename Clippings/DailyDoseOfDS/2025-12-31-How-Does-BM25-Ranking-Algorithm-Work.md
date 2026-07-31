---
title: "How does BM25 ranking algorithm work?"
source: "https://mail.google.com/mail/u/0/#inbox/19b71b8454693ea2"
author:
  - "[[DailyDoseOfDS]]"
published: 2025-12-31
created: 2026-07-30
description: "深入解析 BM25 检索算法的核心三问（逆文档频率、词频饱和度度量与文档长度归一化）及其在 RAG 混合检索中的工程优势。"
tags:
  - clippings
---

# BM25 排序算法工作原理（How does BM25 ranking algorithm work?）

在信息检索与 RAG（检索增强生成）系统中，有一个经典算法至今依然占据核心地位——它就是 **BM25（Best Matching 25）**。

![BM25 算法核心公式与组成拆解](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4d71335e-5177-4228-87bf-dde550e55e79_1936x1200.png)

让我们来拆解究竟是什么赋予了它如此强大的性能。

假设你正在机器学习论文库中搜索“`transformer attention mechanism`”（Transformer 注意力机制）。

BM25 算法主要提出了三个极其简单而关键的问题：

### 1. “这个词有多罕见？”（How rare is this word?）
几乎每篇论文都会包含“`the`”和“`is`”，这使得这些高频常见词在检索中毫无价值。然而“`transformer`”是一个非常具体且信息量极高的词。BM25 会提升罕见词的权重，并忽略常见噪声词。
$$
ightarrow 	ext{这对应公式中的逆文档频率 } 	ext{IDF}(q_i)$$

### 2. “它在文档中出现了多少次？”（How many times does it appear?）
如果“`attention`”在论文中出现了 10 次，这是一个强相关的信号。但是出现 10 次与出现 100 次之间的相关度差异并不大。BM25 引入了词频的**边际递减效应（Diminishing Returns）**。
$$
ightarrow 	ext{这对应结合参数 } k_1 	ext{ 来控制饱和度的 } f(q_i, D)$$

### 3. “这份文档是否异常长？”（Is this document unusually long?）
一篇 50 页的论文自然会比一篇 5 页的论文包含更多关键字。BM25 对文档长度进行归一化拉平，从而避免长文档仅靠字数优势拉高评分。
$$
ightarrow 	ext{这对应受参数 } b 	ext{ 控制的文档长度缩放项 } rac{|D|}{	ext{avgdl}}$$

![BM25 核心三问逻辑总结](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fdb25056d-1348-4811-98ea-84192ae1d976_1936x1200.png)

总体而言，BM25 围绕这三个核心问题展开构建，并且**完全不需要神经网络计算**。

---

### 为什么 BM25 在现代化 RAG 中依然不可替代？

BM25 极其擅长**精准关键字匹配（Exact Keyword Matching）**，而这正是向量嵌入（Embeddings / Vector Search）经常面临困难的地方。

当你的语料库包含特定领域的专业术语、型号代码或未在向量模型预训练数据中出现的词汇时，BM25 的优势尤为突出。

例如：如果用户搜索错误代码“`error code 5012`”，向量检索可能会返回语义相似但编号完全不对的故障文档；而 BM25 则能精准定位到包含该具体代码的条目。

这也正是**混合检索（Hybrid Search）**诞生的原因。

当今最顶尖的 RAG 系统会将 BM25 稀疏检索与向量密集检索相结合。你可以同时兼得两者的优势：既拥有向量模型的语义理解能力，又具备 BM25 的精确关键字匹配能力。

因此，在为每个搜索问题投掷 GPU 算力之前，不妨优先考虑 BM25——它可能已经能解决你的问题，或者在与语义检索结合时让系统的综合效果更上一层楼。
