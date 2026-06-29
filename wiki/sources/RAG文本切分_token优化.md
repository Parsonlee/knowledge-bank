---
type: source
tags:
  - RAG
  - RAG/chunking
summary: 文本切分系列第2.5篇，介绍在递归字符切分中融入 token 计数的优化方法，对比 tiktoken、SentenceTransformers 和自定义 tokenizer 三种方案。
sources:
  - "Cubox/RAG文本切分的五个层次2：递归字符切分的token优化.md"
created: "2026-06-29"
updated: "2026-06-29"
confidence: high
---

# RAG文本切分_token优化

> 来源：哎呀AIYA 微信公众号《RAG文本切分的五个层次2：递归字符切分的token优化(实战)》
> URL：https://mp.weixin.qq.com/s?__biz=Mzk0NTcyNTMzNw==&mid=2247483966&idx=1&sn=4895eeba3d51d02f83e2b96067eb9227
> tags: RAG, RAG/chunking
> Cubox 高亮：无

## 摘要

文本切分系列第 2.5 篇（Level 2 token 优化）。前两种方案按字符（一个英文字母或中文汉字）计算长度，与大模型按 token 处理文本存在差异。本篇介绍如何在切分时融入 token 计数。

## 核心内容

### 为什么融入 token
- 语言模型（LLM、向量模型、重排模型）都有长度限制
- 使用 token 个数切分的好处：
  1. 保证切分后文本片段不超过模型最大长度
  2. 保证送入模型的 token 数相当，并行节约资源
  3. 有效预估送入大模型的片段长度，便于系统内资源调整

### OpenAI 模型（tiktoken）
- `CharacterTextSplitter.from_tiktoken_encoder(encoding_name="cl100k_base", chunk_size=50, chunk_overlap=0)`
- `RecursiveCharacterTextSplitter.from_tiktoken_encoder(model_name="gpt-4", chunk_size=50, chunk_overlap=0)`
- 发现：OpenAI tokenizer 对中文切分时一个汉字消耗多个 token，成本较高

### SentenceTransformers 方法
- `SentenceTransformersTokenTextSplitter(tokens_per_chunk=50, chunk_overlap=0, model_name="./bge-m3")`
- 对中文支持好的模型，token 压缩比例显著提升（如 bge-m3 每 token 对应更多中文字符）

### 加载自己的 tokenizer
- 使用 `AutoTokenizer.from_pretrained("./bge-m3")` 定义 tokenizer
- `RecursiveCharacterTextSplitter.from_huggingface_tokenizer(tokenizer, chunk_size=50, chunk_overlap=0, separators=["\n\n", "\n", "。"], keep_separator=False)`
- 可自定义分隔符配合自己的向量模型

### 其它切分工具
- NLTKTextSplitter、SpacyTextSplitter 等

## 关联

- 概念：[[概念_文本切分五层级]]、[[概念_递归字符切分]]、[[概念_Token切分优化]]
- 实体：[[实体_LangChain]]、[[实体_LlamaIndex]]
- 系列上一篇：[[RAG文本切分_递归字符切分]]
- 系列下一篇：[[RAG文本切分_JSON文档切分]]
