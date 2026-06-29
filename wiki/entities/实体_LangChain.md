# 实体_LangChain

> tags: RAG
> confidence: medium

## 简介

LangChain 是构建 LLM/RAG 应用的框架，贯穿本 RAG 系列全部 5 篇文章的实现。与 LlamaIndex 同类，负责将检索和生成过程链（Chain）在一起。

## 全文涉及能力

- **文档加载**：有超过 160 种不同的文档加载器，可从许多来源抓取数据
- **链（Chain）**：将检索和生成过程串联，简化 RAG 管道构建
- **PromptTemplate**：将问题和知识片段组成 Prompt String
- **结构化输出**：`with_structured_output` 将模型生成结果格式化为结构化数据（JSON/字典），用于 Logical Routing 和 Query Construction
- **检索器（retriever）**：基于 Vector Store 构建
- **InMemoryByteStore**：Multi-representation 中存储原始文档
- **文本切分器**：CharacterTextSplitter、RecursiveCharacterTextSplitter、RecursiveJsonSplitter、SentenceTransformersTokenTextSplitter、SemanticChunker 等
- **Token 集成**：支持 tiktoken（OpenAI）、HuggingFace tokenizer、SentenceTransformers 切分

## 相关平台

- **LangSmith**：构建生产级 LLM 应用的平台，可跟踪 LLM 调用、监控和评估应用

> 注：全文围绕 LangChain 用法展开但未系统介绍框架本身，故标 medium。

## 关联

- 相关概念：[[概念_RAG基础流程]]、[[概念_RAG_Routing]]、[[概念_Query_Construction]]、[[概念_文本切分五层级]]
- 来源：[[RAG基础_索引检索生成]]、[[RAG查询翻译_Query_Translation]]、[[RAG路由_Routing]]、[[RAG查询构造_Query_Construction]]、[[RAG索引进阶_Indexing]]、[[RAG文本切分_字符切分]]、[[RAG文本切分_递归字符切分]]、[[RAG文本切分_token优化]]、[[RAG文本切分_JSON文档切分]]、[[RAG文本切分_语义切分]]、[[RAG_12痛点与解决方案]]
