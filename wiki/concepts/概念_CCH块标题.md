# 概念_CCH块标题

> tags: RAG, RAG/chunking
> confidence: high

## 定义

上下文块标题（Contextual Chunk Headers, CCH）是一种 RAG 分块增强方法：在将文本分块时，为每个 chunk 生成描述性标题并拼接到块开头，然后对"标题+正文"进行联合 Embedding 和检索。

## 解决的问题

- 传统分块丢失重要上下文信息（该段属于哪个章节/主题）
- 导致检索效果不佳，模型可能基于断章取义的内容生成错误答案

## 实现方式

1. 文本分块（固定长度或语义分块）
2. 用 LLM 为每个 chunk 生成简洁标题（generate_chunk_header）
3. 分别对标题和正文生成 Embedding
4. 检索时计算 query 与标题相似度 + query 与正文相似度，取平均作为最终得分

## 效果

- 每个文本块都携带高层上下文信息
- 标题提供主题定位，正文提供细节
- 联合评分同时考虑宏观相关性和微观相关性

## 关联

- 相关概念：[[概念_文本切分五层级]]、[[概念_Markdown标题切分]]、[[概念_Multi-representation_Indexing]]
- 来源：[[RAG技巧与底层代码剖析]]
