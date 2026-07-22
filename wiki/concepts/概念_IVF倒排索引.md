---
type: concept
tags:
- RAG/embedding
- RAG/retrieval
summary: 基于聚类空间划分的倒排文件向量索引算法（Inverted File Index），通过簇中心分组大幅缩小检索范围与内存占用。
sources:
- wiki/sources/2026程序员必读的向量数据库原理与选型指南.md
created: '2026-07-22'
updated: '2026-07-22'
---

# 概念：IVF倒排索引 (Inverted File Index)

## 定义

**IVF（Inverted File Index，倒排文件索引）** 是向量检索中最经典的[[concepts/概念_近似最近邻搜索|ANN 算法]]之一。它利用 K-Means 聚类将高维向量空间划分为多个 Voronoi 区域（簇）。

## 工作原理

1. **聚类训练**：使用 K-Means 将全量向量聚类为 $N$ 个质心（Centroids），建立倒排列表。
2. **倒排挂载**：每个向量按最近距离归属于某一个质心，挂载在该质心的倒排列表中。
3. **查询加速**：检索时，先计算查询向量与 $N$ 个质心的距离，选出最近的 $nprobe$ 个质心，仅在这些质心对应的倒排列表中进行详细距离计算。

## 优缺点与应用

- **优点**：内存消耗相比 [[entities/实体_HNSW|HNSW]] 小很多，结合 PQ（乘积量化，IVF_PQ）可以大幅压缩数据体积，极度适合超大规模向量检索。
- **缺点**：召回率略低于 HNSW，依赖高质量的聚类训练。
- **代表组件**：[[entities/实体_Faiss|Faiss]]、[[entities/实体_Milvus|Milvus]]、[[entities/实体_pgvector|pgvector]]（IVF_FLAT）。

## 关联

- 相关概念：[[concepts/概念_向量数据库]]、[[concepts/概念_近似最近邻搜索]]、[[concepts/概念_向量索引方法]]、[[concepts/概念_向量量化]]
- 实体：[[entities/实体_Milvus]]、[[entities/实体_pgvector|pgvector]]、[[entities/实体_Faiss]]
- 来源：[[2026程序员必读的向量数据库原理与选型指南]]
