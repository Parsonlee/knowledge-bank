---
type: entity
tags:
- AI-Agent/tools
- RAG
summary: 业界主流的大模型应用流水线与 RAG 链式编排框架。
sources:
- raw/12 RAG 痛点和拟议解决方案.md
- raw/AI 代理的上下文工程：LangChain 和 Manas - Notebook....md
- raw/FastAPI 架构指南：用这份模版打造可扩展又安全的系统（附实战经验）.md
- raw/How we built our multi-agent research system.md
- raw/Human In the Loop竟然可以是个MCP_.md
- raw/Jina AI创业复盘：AI团队的Scaling Law是什么.md
- raw/Prompt Engineering, Finetune, RAG？：OpenA....md
- raw/RAG从入门到精通系列1：基础RAG.md
- raw/RAG从入门到精通系列4：Query Construction（查询构造）.md
- raw/RAG从入门到精通系列5：Indexing（索引）.md
- raw/RAG从入门到精通系列6：Retrieval（检索）.md
- raw/RAG文本切分LV3：轻松定制Markdown切分.md
- raw/RAG文本切分五个层次3：不同文档切分之JSON(实战).md
- raw/RAG文本切分的五个层次1：字符切分基础(实战).md
- raw/RAG文本切分的五个层次2：递归字符分割(实战).md
- raw/RAG文本切分的五个层次2：递归字符切分的token优化(实战).md
- raw/RAG文本切分的第四个层次，基于向量模型的语义切分.md
- raw/RAG高级优化：检索后处理模块成竹在胸.md
- raw/RAG高级优化：检索策略探讨Fusion, HyDE安排上(含代码).md
- raw/一文读懂向量数据库，原理到应用全解析！.md
- raw/也许当前最好的「上下文工程」讲解_LangChain联合Manus季逸超最新分享....md
- raw/大模型算法岗，面试百问百答.md
- raw/探索提升RAG系统问答质量的技术路线.md
- raw/浅谈上下文工程｜从 Claude Code 、Manus 和 Kiro 看提示工....md
- raw/用 RAGAS 精准定位 RAG 系统短板.md
- wiki/sources/AI_Agent与AI_Workflow的区别和深度解析.md
- wiki/sources/Agent系统开发经验.md
- wiki/sources/Context_Engineering_LangChain_Manus_NotebookLM.md
- wiki/sources/Jina_AI创业复盘.md
- wiki/sources/Manus创始人手把手拆解上下文工程.md
- wiki/sources/RAGAS评估RAG系统.md
- wiki/sources/RAG_12痛点与解决方案.md
- wiki/sources/RAG基础_索引检索生成.md
- wiki/sources/RAG技巧与底层代码剖析.md
- wiki/sources/RAG文本切分_JSON文档切分.md
- wiki/sources/RAG文本切分_Markdown切分.md
- wiki/sources/RAG文本切分_token优化.md
- wiki/sources/RAG文本切分_字符切分.md
- wiki/sources/RAG文本切分_语义切分.md
- wiki/sources/RAG文本切分_递归字符切分.md
- wiki/sources/RAG查询构造_Query_Construction.md
- wiki/sources/RAG查询翻译_Query_Translation.md
- wiki/sources/RAG检索_Retrieval入门到精通.md
- wiki/sources/RAG索引进阶_Indexing.md
- wiki/sources/RAG路由_Routing.md
- wiki/sources/RAG高级优化_query转换之路.md
- wiki/sources/RAG高级优化_检索后处理.md
- wiki/sources/RAG高级优化_检索策略Fusion_HyDE.md
- wiki/sources/RAG高级优化_问题生成检索增强.md
- wiki/sources/也许当前最好的上下文工程讲解_LangChain联合Manus.md
- wiki/sources/从提示员到系统架构师：Loop Engineering 的范式跃迁.md
- wiki/sources/向量数据库原理与应用全解析.md
- wiki/sources/浅谈上下文工程_Claude_Code_Manus_Kiro.md
created: '2026-06-29'
updated: '2026-07-01'
confidence: medium
---

> [!note] 说明
> 注：全文围绕 LangChain 用法展开但未系统介绍框架本身，故标 medium。

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

## 关联

- 相关概念：[[概念_RAG基础流程]]、[[概念_RAG_Routing]]、[[概念_Query_Construction]]、[[概念_文本切分五层级]]
- 来源：[[RAG基础_索引检索生成]]、[[RAG查询翻译_Query_Translation]]、[[RAG路由_Routing]]、[[RAG查询构造_Query_Construction]]、[[RAG索引进阶_Indexing]]、[[RAG文本切分_字符切分]]、[[RAG文本切分_递归字符切分]]、[[RAG文本切分_token优化]]、[[RAG文本切分_JSON文档切分]]、[[RAG文本切分_语义切分]]、[[RAG_12痛点与解决方案]]
