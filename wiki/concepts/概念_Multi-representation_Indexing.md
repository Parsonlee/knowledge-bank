# 概念_Multi-representation_Indexing

> tags: RAG, RAG/chunking
> confidence: high

## 定义

Multi-representation Indexing 通过结合多种表示（文档摘要、块或完整内容），在检索和生成过程中取得最佳效果。使用不同层次和粒度的表示（简洁的摘要与详细的文档）弥补单一表示可能存在的不足。

## Proposition Indexing（具体实现）

1. 使用 LLM 对原始文本生成摘要（Summary）
2. 对摘要进行嵌入处理保存到 Vector Store；原始文本保存到 Doc Store
3. 原始文档和摘要通过 doc_id 关联
4. 检索时根据问题嵌入匹配摘要，返回原始文本

## 特点

- 对长上下文 LLM 更友好
- 弥补块大小和块数量参数难以设置的问题

## 关联

- 相关概念：[[概念_RAPTOR索引]]、[[概念_RAG基础流程]]、[[概念_Embedding与向量检索]]
- 来源：[[RAG索引进阶_Indexing]]
