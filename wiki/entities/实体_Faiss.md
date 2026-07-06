---
type: entity
tags:
- RAG/retrieval
summary: Meta AI 开源的高效海量向量相似度检索与聚类计算库。
sources:
- raw/FastAPI 架构指南：用这份模版打造可扩展又安全的系统（附实战经验）.md
- raw/RAG 挑战赛冠军方案解析：从数据解析到多路由器检索的工程实践，推荐阅读！.md
- raw/RAG之延迟交互与残差压缩：从ColBERT到ColBERTv2的演进及其应用.md
- raw/RAG高级优化：基于问题生成的文档检索增强.md
- raw/RAG：ColBERT原理、延迟交互机制与稠密向量的对比分析.md
- raw/一文读懂向量数据库，原理到应用全解析！.md
- raw/从BM25到Multi-Vector：6种Embedding演进路线.md
- raw/美团搜索中查询改写技术的探索与实践 - 美团技术团队.md
- wiki/sources/ColBERTv2残差压缩演进.md
- wiki/sources/RAG技巧与底层代码剖析.md
- wiki/sources/RAG挑战赛冠军方案.md
- wiki/sources/RAG高级优化_问题生成检索增强.md
- wiki/sources/向量数据库原理与应用全解析.md
- wiki/sources/美团搜索查询改写实践.md
created: '2026-06-29'
updated: '2026-07-01'
confidence: high
---

## 简介

Faiss（Facebook AI Similarity Search）是由 Facebook AI Research 开源的向量相似检索库（C++ 实现）。更像库/工具包而非完整数据库。

## 特点

- 提供丰富的索引算法（Flat、IVF、HNSW、PQ 等）实现和优化
- 支持 GPU 加速，单机环境追求极致性能
- 支持多种距离度量（L2、IP、余弦等）
- 优势：查询速度快、算法灵活，常作为其他向量库的底层引擎或基准
- 局限：不含分布式存储、持久化、权限控制等数据库功能；不直接支持过滤和复杂查询，需应用层配合
- 适合嵌入式使用或搭建自定义向量服务，即装即用门槛较高
- ColBERT 用 FAISS 索引存储文档向量

## 关联

- 相关概念：[[概念_向量索引方法]]、[[概念_近似最近邻搜索]]、[[概念_向量数据库]]、[[概念_向量量化]]
- 实体：[[实体_HNSW]]、[[实体_ColBERT]]
- 来源：[[向量数据库原理与应用全解析]]、[[ColBERTv2残差压缩演进]]、[[RAG挑战赛冠军方案]]、[[美团搜索查询改写实践]]
