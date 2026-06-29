# 实体_rank_bm25

> tags: RAG, RAG/retrieval
> confidence: medium

## 简介

`rank_bm25` 是一个 Python 库，提供 BM25 排名算法的实现。在 RAG 融合检索场景中用于关键字匹配检索，与向量检索互补。

## 核心 API

- `BM25Okapi(tokenized_docs)`：基于分词后的文档集建立 BM25 索引
- `bm25.get_scores(query_tokens)`：返回查询与每篇文档的 BM25 相关性得分

## 使用方式

```python
from rank_bm25 import BM25Okapi
tokenized_docs = [doc.page_content.split() for doc in documents]
bm25 = BM25Okapi(tokenized_docs)
scores = bm25.get_scores(query.split())
```

## 关联

- 相关概念：[[概念_BM25]]、[[概念_Fusion_Retrieval]]
- 来源：[[RAG高级优化_检索策略Fusion_HyDE]]
