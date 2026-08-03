---
type: source
tags:
  - sentence-similarity
  - bi-encoder
  - cross-encoder
  - colbert
  - nlp
summary: 介绍了双编码器（Bi-encoders）、交叉编码器（Cross-encoders）与 ColBERT 架构在成对句子评分系统中的工作机制、优劣势，并重点阐述了 ColBERT 如何通过延迟交互（Late Interaction）平衡检索吞吐与精准度。
sources:
  - raw/articles/2026-06-18_Visual-guide-to-Bi-encoders,-Cross-encoders-&-ColBERT_19edcc.md
updated: 2026-08-04
---

# Visual guide to Bi-encoders, Cross-encoders & ColBERT (Source 摘要)

## 来源信息
- **标题**: Visual guide to Bi-encoders, Cross-encoders & ColBERT
- **发送人**: Daily Dose of DS
- **日期**: 2026-06-18
- **原始文章**: [[raw/articles/2026-06-18_Visual-guide-to-Bi-encoders,-Cross-encoders-&-ColBERT_19edcc.md]]

## 核心要点
- **成对句子评分机制 (Pairwise Sentence Scoring)**：是许多实际 NLP 系统（如 RAG、问答匹配、去重等）的基石。
- **交叉编码器 (Cross-encoders)**：将 Query 和 Document 拼接输入，利用全注意力机制。语义表达非常强，但无法离线预计算，检索无法扩展。
- **双编码器 (Bi-encoders)**：分别独立对 Query 和 Document 编码，通过计算 `[CLS]` 的余弦相似度打分。支持文档向量离线计算，检索扩展性强，但在特征提取中丢失了细粒度的词词间关联。
- **ColBERT 架构**：通过延迟交互（Late Interaction）机制将两者的优势结合。既允许离线预计算词级向量，又能通过 MaxSim 算子对 Query 和 Document 间的词级向量进行高效交叉匹配，从而达到逼近交叉编码器的精度。

## 关键引文
- "But we lose all the interaction and simply “hope” that the entire information about the query and the document is well summarized in the `[CLS]` token."
- "ColBERT brings together the power of cross-encoders and the scalability of bi-encoders."

## 联动概念
- [[wiki/concepts/概念_双编码器与交叉编码器.md|概念_双编码器与交叉编码器]]

> 📎 **物理文献**：[[raw/articles/2026-06-18_Visual-guide-to-Bi-encoders,-Cross-encoders-&-ColBERT_19edcc.md]]
