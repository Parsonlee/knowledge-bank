# 概念_Query_Translation

> tags: RAG, RAG/query
> confidence: high

## 定义

Query Translation（查询翻译）是 RAG 高阶技巧，针对用户 Query 模糊或复杂导致检索不准的问题（"Garbage in, Garbage out"），通过改写/优化/分解原始查询提升检索和生成效果。

## 方法分类

### Re-written（改写）
对原始查询语义重写，保持核心意思不变，调整语言表述。
- **Multi-Query**：生成多个不同表述的查询，分别检索后去重合并，获得更全面的文档集合
- **RAG Fusion**：见 [[概念_RAG_Fusion]]

### Decomposition（分解）
将复杂问题拆解为多个独立子问题（sub-question）：
- **逻辑分解**：基于"且""或"等逻辑关系
- **多跳分解**：跨越多个知识领域逐步深入
- 流程一（递归求解）：前一子问题答案结合下一子问题检索文档
- 流程二（并行汇总）：分别回答后集中汇总

### Step-back Question
当问题太具体时退一步问更广泛、概括的问题，获取更大上下文。需提供 few-shot example。提高召回率和上下文覆盖率。

### HyDE
见 [[概念_HyDE]]

## 关联

- 相关概念：[[概念_RAG_Fusion]]、[[概念_HyDE]]、[[概念_RAG基础流程]]
- 来源：[[RAG查询翻译_Query_Translation]]
