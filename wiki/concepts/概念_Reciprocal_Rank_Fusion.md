# 概念_Reciprocal_Rank_Fusion

> tags: RAG, RAG/retrieval
> confidence: high

## 定义

互易秩融合（Reciprocal Rank Fusion, RRF）是一种排序融合算法，将多个排序结果合并为一个综合排序。核心思想是对每个文档在各排序中的排名取倒数并累加，排名靠前的文档获得更高分数。

## 公式

对文档 d 在多个排序 R₁, R₂, ... 中的综合得分：

```
score(d) = Σ 1 / (k + rank_i(d) + 1)
```

- k：平滑常数，默认 60
- rank_i(d)：文档 d 在第 i 个排序中的排名（从 0 开始）

## 特点

- 无需归一化各检索方法的原始分数
- 对排名前列的文档给予更大权重
- 平滑常数 k 避免排名第一的文档权重过大
- 适用于合并来自不同检索系统/不同查询的结果

## 应用场景

- RAG-Fusion：多个查询变体的检索结果用 RRF 融合
- 混合检索：向量 + 关键字检索结果融合

## 关联

- 相关概念：[[概念_RAG_Fusion]]、[[概念_Fusion_Retrieval]]
- 来源：[[RAG高级优化_检索策略Fusion_HyDE]]
