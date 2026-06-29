# 概念_Contextual_Compression

> tags: RAG, RAG/retrieval
> confidence: high

## 定义

上下文压缩（Contextual Compression）是一种检索后处理方法。本质上利用 LLM 判断检索之后的文档与用户 query 的相关性，只返回相关度最高的 k 个文档（或文档中的相关片段），过滤掉无关内容。

## 作用

- 减少送入大模型的无关上下文，降低噪声
- 节省 token 成本
- 提高生成回答的聚焦度和准确性

## 实现

LangChain：
- `ContextualCompressionRetriever`：包装基础检索器
- `LLMChainExtractor`：用 LLM 从召回文档中提取相关内容
- 结构：`base_retriever` 召回 → `base_compressor` 用 LLM 压缩过滤

## 关联

- 相关概念：[[概念_检索后处理]]、[[概念_Long-text_Reorder]]
- 来源：[[RAG高级优化_检索后处理]]
