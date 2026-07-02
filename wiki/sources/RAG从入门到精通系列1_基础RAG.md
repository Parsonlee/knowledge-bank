---
type: source
tags:
- RAG
summary: 系统梳理基础检索增强生成（Naive RAG）标准管线的核心技术流程与基础概念，从文档切分、向量嵌入到召回生成进行全链路概括。
sources:
- raw/RAG从入门到精通系列1：基础RAG.md
created: '2026-07-02'
updated: '2026-07-02'
confidence: high
---
# RAG从入门到精通系列1_基础RAG

## 来源信息
- 物理文件：[[raw/RAG从入门到精通系列1：基础RAG.md]]

## 核心要点
1. **基础 RAG 三阶段架构**：文档索引（Indexing：切块 Chunking + 嵌入 Embedding）、向量检索（Retrieval：相似度匹配 Top-K）、最终生成（Generation：提示词增强注入 LLM）。
2. **典型瓶颈与挑战**：基础 RAG 容易受到切片语境断裂、相似度匹配不准（语意差异）及生成幻觉等因素限制。
3. **向高级 RAG 演进指引**：明确了后续引入重排序（Rerank）、混合检索与查询改写的优化方向。

## 关联概念与实体
- [[概念_RAG基础流程]]
- [[概念_Embedding与向量检索]]
- [[概念_重排序Rerank]]

---
> 📎 **物理文献**：[[raw/RAG从入门到精通系列1：基础RAG.md]]
