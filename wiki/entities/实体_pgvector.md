---
type: entity
tags:
- RAG/retrieval
- Skill/python
summary: PostgreSQL 的开源向量检索扩展插件，支持原生 SQL 向量查询与事务复用。
sources:
- wiki/sources/2026程序员必读的向量数据库原理与选型指南.md
updated: '2026-07-22'
---

# 实体：pgvector

## 简介

**pgvector** 是开源的关系型数据库 PostgreSQL 的向量检索扩展插件。它允许开发者直接在 PostgreSQL 中存储高维向量并进行相似度搜索（如 L2 距离、余弦相似度、内积）。

## 核心特性

- **SQL 原生支持**：使用标准 SQL 表达式（如 `ORDER BY embedding <-> '[...]' LIMIT 5`）完成向量相似度检索。
- **复用 PG 生态**：完美复用 PostgreSQL 的 ACID 事务、行级权限控制、备份恢复与原有关系型数据表。
- **索引支持**：支持 HNSW 和 IVF_FLAT 索引。

## 适用场景

- **实用主义者首选**：团队已有 PostgreSQL 基础设施，且向量数据量在百万级以下（< 100 万），选型 ROI 最高。

## 关联

- 相关概念：[[concepts/概念_向量数据库]]、[[concepts/概念_标量过滤]]
- 来源：[[2026程序员必读的向量数据库原理与选型指南]]
