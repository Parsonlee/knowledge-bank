# 概念_HyDE

> tags: RAG, RAG/query
> confidence: high

## 定义

HyDE（Hypothetical Document Embedding，假设文档嵌入）是一种 Query Translation 方法，核心思想是通过生成"假设文档"，将查询从抽象的自然语言问题转化为检索系统能高效处理的表示。特别适用于复杂问题处理。

## 流程

1. **输入问题**：用户输入自然语言问题
2. **生成假设文档**：用生成模型（如 GPT）生成一个可能的回答（假设答案），提供强语义上下文，即使可能并不完全正确
3. **检索相关文档**：将假设文档嵌入向量空间或提取关键词作为检索输入
4. **生成最终答案**：结合检索文档和原始问题生成回答

## 关联

- 相关概念：[[概念_Query_Translation]]
- 来源：[[RAG查询翻译_Query_Translation]]
