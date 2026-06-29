# RAG高级优化：基于问题生成的文档检索增强

> 来源：哎呀AIYA 公众号
> URL：https://mp.weixin.qq.com/s?__biz=Mzk0NTcyNTMzNw==&mid=2247484125&idx=1&sn=0490793590a7061bf0593749f1a58474
> tags: RAG, RAG/query
> Cubox 高亮：1 处（问题丰富文本片段提高检索准确性）

## 摘要

[重点/高亮] 通过用相关问题丰富文本片段，显著提高识别文档中包含用户查询答案的最相关部分的准确性。

本文介绍一种文本增强技术，利用 LLM 额外生成问题来改进向量数据库中的文档检索。通过生成并合并与每个文本片段相关的问题，增强标准检索过程，增加找到相关文档的可能性。

## 核心内容

### 实现步骤

1. **文档解析和文本分块**：处理 PDF 文档并划分为可管理的文本片段
2. **问题增强**：使用 LLM 在文档级别或片段级别生成相关问题
3. **向量存储创建**：使用向量模型计算嵌入，创建 FAISS 向量存储
4. **检索和答案生成**：使用 FAISS 查找最相关文档，根据上下文生成答案

### 问题生成级别

- **DOCUMENT_LEVEL**：在整个文档级别生成问题
- **FRAGMENT_LEVEL**：在单个文本片段级别生成问题

### 处理流程

1. 全文按 `DOCUMENT_MAX_TOKENS` 切分为多个 text_document
2. 每个 text_document 按 `FRAGMENT_MAX_TOKENS` 切分为 text_fragment
3. 对每个 fragment 或 document 调用 LLM 生成问题列表
4. 原始片段与生成的问题共同存入 FAISS（metadata 区分 ORIGINAL/AUGMENTED）
5. 检索时问题与原始片段均参与匹配，返回对应的原始文档

### 关键代码逻辑

- `generate_questions(text)` 使用 gpt-4o-mini 根据文本上下文生成至少 N 个问题
- Prompt 要求问题可直接从上下文回答，不含答案或标题
- 去重过滤后存入 Document（page_content=问题，metadata 指向原文）
- 检索器返回 k=1 最相关的 FAISS 文档

### 注意事项

- 使用大模型 API 生成问题会产生成本
- 问题数量由 `QUESTIONS_PER_DOCUMENT` 参数控制

## 关联

- 概念：[[概念_问题生成检索增强]]、[[概念_Embedding与向量检索]]
- 实体：[[实体_LangChain]]
- 同系列：[[RAG高级优化_检索策略Fusion_HyDE]]、[[RAG高级优化_query转换之路]]、[[RAG高级优化_检索后处理]]
