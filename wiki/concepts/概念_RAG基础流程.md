# 概念_RAG基础流程

> tags: RAG
> confidence: high

## 定义

RAG（Retrieval Augmented Generation，检索增强生成）是一种将 LLM 与外部数据源（私有数据或最新数据）连接的通用方法，允许 LLM 使用外部数据生成输出。解决 LLM 训练数据不含任务相关数据或非最新数据的问题。

## 三步流程

1. **Indexing（索引）**：对外部文档建立索引
2. **Retrieval（检索）**：根据用户问题检索相关文档
3. **Generation（生成）**：将问题 + 相关文档输入 LLM 生成最终答案

## 关联

- 相关概念：[[概念_Embedding与向量检索]]、[[概念_向量数据库]]
- 进阶技巧：[[概念_Query_Translation]]、[[概念_RAG_Routing]]、[[概念_Query_Construction]]、[[概念_Multi-representation_Indexing]]
- 来源：[[RAG基础_索引检索生成]]
