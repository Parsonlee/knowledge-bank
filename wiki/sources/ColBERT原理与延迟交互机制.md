---
type: source
tags:
  - RAG/embedding
  - RAG
summary: "ColBERT 原理与延迟交互（Late Interaction）机制——多向量表示、MaxSim 计算流程，及其与稠密向量（Sentence-BERT）的对比与 BGE-M3 实验"
sources:
  - title: "ColBERT原理、延迟交互机制与稠密向量的对比分析"
    url: https://mp.weixin.qq.com/s?__biz=MzkwNjcxNTc2Ng==&mid=2247485657&idx=1&sn=30bc94da15598a7373aedf9fc33a02a9&scene=21&poc_token=HJoD1mijgUYBup2PQ7CK-tfueFdYxEMkDLGaRe1_
    cubox_id: "7371088986099419215"
created: 2026-06-26
updated: 2026-06-26
confidence: high
---

# ColBERT原理与延迟交互机制

## 三种向量表示方法

- **稠密向量（Dense Vector）**：低维，由 [[BERT]] / [[Sentence-BERT]] 将整个句子编码为单个向量。
- **稀疏向量（Sparse Vector）**：高维，由 [[BM25]] / TF-IDF 产生。
- **多向量（Multi-Vector）**：每段文本对应一组向量，每个 token 拥有自己的向量，[[ColBERT]] 是其代表。

## ColBERT 核心

- 构建于 [[BERT]] 之上，为每个 token 生成独立的上下文嵌入（contextual embedding），而非每句一个向量。
- 对查询 Q 产生向量集 {q1, …, qn}；对文档 D 产生向量集 {d1, …, dm}。
- 维度通常为 1024，来自 BERT 输出 + 线性投影（linear projection）。

## 延迟交互机制（Late Interaction）

- 查询与文档**独立编码**。
- 随后对每个查询向量 qi，在所有文档向量 dj 中找到点积最大值（max dot product）。
- 将所有最大值（max score）求和，作为最终相关性得分。

这一逐 token 取最大再求和的过程即 [[MaxSim]] 计算方式。

## 与稠密向量的对比

| 维度 | 稠密向量（[[Sentence-BERT]]） | ColBERT（多向量） |
|------|------------------------------|--------------------|
| 表示 | 单个向量 | 多向量（每 token 一个） |
| 相似度复杂度 | O(1) | O(n·m)（可用矩阵运算优化） |
| 粒度 | 句级 | token 级（更细） |

## BGE-M3 实验

使用 `BGEM3FlagModel`：

- 查询："What is BGE M3?"（8 个 token）
- 文档："Definition of BM25"（7 个 token）

| 指标 | 数值 |
|------|------|
| 原始得分（raw score） | 3.8145 |
| 归一化得分 | 0.4768 |
| 官方 colbert_score | 0.4768 |
| 稠密余弦相似度 | 0.4103 |

ColBERT 因逐 token 选取最大相似度而给出更高的相似度。相关模型见 [[BGE-M3]]。

## 关键结论

- 归一化（normalization）对可解释性至关重要。
- 多向量比单个稠密向量能捕捉更细的粒度。

## 相关概念

- [[ColBERTv2残差压缩演进]]
- [[Late Interaction]]
- [[MaxSim]]
