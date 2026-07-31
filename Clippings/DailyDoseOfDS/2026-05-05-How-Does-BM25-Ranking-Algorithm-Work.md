---
title: "How Does BM25 Ranking Algorithm Work?"
source: "https://mail.google.com/mail/u/0/#inbox/19dfa25648e2f2cb"
author:
  - "[[DailyDoseOfDS]]"
published: 2026-05-05
created: 2026-07-30
description: "深度拆解经典信息检索算法 BM25，解析词频饱和度（Term Frequency Saturation）与文档长度归一化（Document Length Normalization）的数学原理。"
tags:
  - clippings
---

# BM25 排序算法的工作原理（How Does BM25 Ranking Algorithm Work?）

在现代信息检索（IR）与混合检索 RAG（Dense Vector + Sparse Retrieval）架构中，**BM25 (Best Matching 25)** 依然是最稳健、效果最好的稀疏检索算法。

## 1. 传统 TF-IDF 的局限性

传统 TF-IDF 存在两大主要痛点：
1. **词频得分线性开销**：在 TF-IDF 中，某关键词在文档中出现 100 次的得分是出现 10 次的 10 倍，导致高词频文档得分虚高。
2. **缺乏文档长度惩罚**：较长的文档天然更有可能匹配到更多查询词，从而导致检索得分不公平地偏向长文本。

![图 1：TF-IDF 与 BM25 词频得分饱和度曲线对比](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4d71335e-5177-4228-87bf-dde550e55e79_1936x1200.png)
*说明：图 1：TF-IDF 与 BM25 词频得分饱和度曲线对比*

## 2. BM25 的两大核心改进

1. **词频饱和度（Term Frequency Saturation）**：引入超参数 $k_1$，使词频得分随出现次数呈非线性递增，当词频达到一定阈值后得分渐进饱和。
2. **文档长度归一化（Document Length Normalization）**：引入超参数 $b$，结合文档实际长度 $|D|$ 与语料库平均文档长度 $\text{avgdl}$，对长文档的匹配得分进行适当惩罚。

![图 2：BM25 文档长度归一化惩罚机制示意图](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fdb25056d-1348-4811-98ea-84192ae1d976_1936x1200.png)
*说明：图 2：BM25 文档长度归一化惩罚机制示意图*

## 3. 数学公式与超参数建议

对于查询 $Q$ 与文档 $D$，BM25 计算公式为：

$$\text{Score}(D, Q) = \sum_{i=1}^{n} \text{IDF}(q_i) \cdot \frac{f(q_i, D) \cdot (k_1 + 1)}{f(q_i, D) + k_1 \cdot \left(1 - b + b \cdot \frac{|D|}{\text{avgdl}}\right)}$$

其中：
* $f(q_i, D)$ 为查询词 $q_i$ 在文档 $D$ 中的词频。
* $\text{IDF}(q_i) = \ln \left( \frac{N - n(q_i) + 0.5}{n(q_i) + 0.5} + 1 \right)$，其中 $N$ 为文档总数，$n(q_i)$ 为包含词 $q_i$ 的文档数。
* **$k_1$ 参数**：通常在 $[1.2, 2.0]$ 之间，用于控制词频饱和的速度。
* **$b$ 参数**：通常设置为 $0.75$，用于控制文档长度惩罚的强度（$b=1$ 为完全惩罚，$b=0$ 为不惩罚）。

![图 3：BM25 参数 k1 与 b 的实际工程调优指南](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F94db5384-8d85-4f58-b4c3-9f8c61de6c8f_993x809.png)
*说明：图 3：BM25 参数 k1 与 b 的实际工程调优指南*
