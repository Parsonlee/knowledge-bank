# 实体_LlamaIndex

> tags: RAG
> confidence: medium

## 简介

LlamaIndex 是构建 LLM/RAG 应用的框架，与 LangChain 同类。在文本切分系列中用于演示文档加载与切分。

## 全文涉及能力

- **文档加载**：`SimpleDirectoryReader(input_files=[...]).load_data()` 加载本地文档
- **文本切分**：`SentenceSplitter(chunk_size, chunk_overlap)` 字符级切分
- **JSON 切分**：`JSONNodeParser()` 处理 JSON 结构数据
- **Node 体系**：切分结果为 nodes，包含文本信息及元数据

> 注：全文仅作为 LangChain 对比方案简要演示，未深入介绍框架本身，故标 medium。

## 关联

- 相关概念：[[概念_文本切分五层级]]、[[概念_字符切分]]、[[概念_文档结构切分]]
- 来源：[[RAG文本切分_字符切分]]、[[RAG文本切分_token优化]]、[[RAG文本切分_JSON文档切分]]
