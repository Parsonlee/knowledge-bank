---
tags:
- RAG
- RAG/query
confidence: high
type: concept
summary: RAG Fusion 是一种在生成阶段融合检索结果的策略，关注如何从多个检索到的文档中综合信息生成高质量回答。过程与 Multi-Query 相似，但对检索到的多篇文档进行筛选过滤之后再输入
  LLM。
created: '2026-07-06'
updated: '2026-07-06'
sources:
- raw/RAG从入门到精通系列2：Query Translation（查询翻译）.md
- raw/RAG从入门到精通系列6：Retrieval（检索）.md
- raw/探索提升RAG系统问答质量的技术路线.md
- wiki/sources/DMQR-RAG_多样查询改写.md
- wiki/sources/ES企业AI搜索实践.md
- wiki/sources/RAG查询翻译_Query_Translation.md
- wiki/sources/RAG检索_Retrieval入门到精通.md
- wiki/sources/RAG高级优化_检索策略Fusion_HyDE.md
- wiki/sources/提升RAG问答质量的技术路线.md
---

# 概念_RAG_Fusion


## 定义

RAG Fusion 是一种在生成阶段融合检索结果的策略，关注如何从多个检索到的文档中综合信息生成高质量回答。过程与 Multi-Query 相似，但对检索到的多篇文档进行筛选过滤之后再输入 LLM。

## 流程

1. 根据原始问题生成多个（文中为 4 个）相关问题
2. 分别检索
3. 使用 **Reciprocal Rank Fusion (RRF)** 对检索结果排序过滤
4. 组成最终 RAG 管道

## 与 Multi-Query 区别

- Multi-Query：检索阶段生成多查询，去重合并
- RAG Fusion：对检索结果用 RRF 筛选过滤后再输入 LLM

## 关联

- 相关概念：[[概念_Query_Translation]]、[[概念_Reciprocal_Rank_Fusion]]、[[概念_DMQR-RAG]]
- 来源：[[RAG查询翻译_Query_Translation]]、[[DMQR-RAG_多样查询改写]]、[[提升RAG问答质量的技术路线]]