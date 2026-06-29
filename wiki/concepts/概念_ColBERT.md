# 概念_ColBERT

> tags: RAG, RAG/retrieval
> confidence: high

## 定义

ColBERT（Contextualized Late Interaction over BERT）是一种基于细粒度 token 级嵌入相似性计算的检索方法。相比将整篇文档/块压缩成单一向量，ColBERT 对每个 token 进行嵌入，实现更精细的匹配。

## 步骤与原理

1. **Token 级别相似度计算**：对查询和文档中的每个 token 分别计算上下文嵌入
2. **最大池化（MaxSim）操作**：对查询中每个 token，取其与文档中所有 token 的最大相似度
3. **选择最相关文档**：基于 MaxSim 得分排序选取

## 为什么有效

- **关注细粒度匹配**：即使查询中只有部分 token 能匹配，这些匹配也能显著影响最终得分
- **兼顾上下文信息**：token 嵌入是基于上下文生成的（BERT），捕捉更丰富语义
- **鲁棒性**：不依赖严格字面匹配，能处理词法变体、同义词、句子结构变化

## 开源实现

- GitHub: https://github.com/stanford-futuredata/ColBERT

## 关联

- 相关概念：[[概念_Embedding与向量检索]]、[[概念_RAPTOR索引]]、[[概念_Multi-representation_Indexing]]、[[概念_Dense_Embedding]]
- 实体：[[实体_ColBERT]]
- 来源：[[RAG索引进阶_Indexing]]、[[从BM25到Multi-Vector_6种Embedding演进路线]]
