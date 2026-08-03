---
type: source
tags:
  - sentence-similarity
  - bi-encoder
  - cross-encoder
  - nlp
summary: 探讨了成对句子评分（Pairwise Sentence Scoring）作为现实世界中 RAG 检索、问答系统、信息检索、去重引擎等应用的基础定位，引入了双编码器和交叉编码器等核心 SOTA 方法。
sources:
  - raw/articles/2025-08-25_Building-pairwise-sentence-scoring-systems_198e2e.md
updated: 2026-08-03
---

# Building pairwise sentence scoring systems (Source 摘要)

## 来源信息
- **主题**: 4 Layers of Agentic AI Systems (Daily Dose of DS)
- **发送人**: Daily Dose of DS \<avi@dailydoseofds.com\>
- **日期**: 2025-08-25
- **物理原始文件**: [[raw/articles/2025-08-25_Building-pairwise-sentence-scoring-systems_198e2e.md]]

## 核心要点
- **NLP 系统的基础**：现实中的许多 NLP 系统（如 RAG、问答、信息检索、重复检测等）都隐式或显式地依赖于上下文相似度评估（即成对句子评分 Pairwise Sentence Scoring）。
- **RAG 的检索核心**：RAG 严重依赖成对句子评分来检索相关上下文。正所谓“RAG 是 80% 的检索和 20% 的生成”，检索质量决定了整个系统的效果。
- **典型应用场景**：
  - **问答系统**：评估问题与潜在答案之间的相似性。
  - **信息检索 (IR)**：根据查询与文档对的评分对文档进行排序。
  - **重复项检测**：在 Quora、Stackoverflow 等社区平台中，判断两个问题或句子是否表达相同的含义。
- **SOTA 架构方向**：需要理解双编码器（Bi-encoders）、交叉编码器（Cross-encoders）以及结合两者的 AugSBERT 架构。

## 关联概念/实体
- 概念: [[wiki/concepts/概念_双编码器与交叉编码器|双编码器与交叉编码器]]

## 关键引文
- "A RAG system heavily relies on pairwise sentence scoring ... to retrieve relevant context ... That is why RAG is considered 80% retrieval and 20% generation."
- "...pairwise sentence (paragraphs, documents, etc.) scoring is a fundamental building block in several NLP applications."

---
> 📎 **物理文献**：[[raw/articles/2025-08-25_Building-pairwise-sentence-scoring-systems_198e2e.md]]
