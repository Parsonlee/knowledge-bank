---
type: source
tags:
- RAG
- RAG/chunking
summary: 文本切分系列第4篇，介绍 Level 4 基于向量模型的语义切分，通过计算句子间向量差异决定切分点，并比较四种阈值控制方法。
sources:
- raw/RAG文本切分的第四个层次，基于向量模型的语义切分.md
created: '2026-06-29'
updated: '2026-07-01'
confidence: high
---
# RAG文本切分_语义切分

> 来源：哎呀AIYA 微信公众号《RAG文本切分的第四个层次，基于向量模型的语义切分》
> URL：https://mp.weixin.qq.com/s/gUyFlIzToUT-fcs8t67j1Q
> tags: RAG, RAG/chunking
> Cubox 高亮：2 处（见下方 [重点/高亮]）

## [重点/高亮]

1. **语义切分器工作原理**：确定何时分隔句子，通过查找任意两个句子之间的向量差异来完成。当该差异超过某个阈值时，它们将被拆分。
2. **梯度方法**：距离的梯度与百分位数方法一起用于分割块。当块彼此高度相关或特定于某个领域时非常有用。想法是在梯度数组上应用异常检测，使分布变得更宽，易于识别高度语义数据中的边界。

## 摘要

文本切分系列第 4 篇。介绍 Level 4 语义切分（Semantic Splitting），基于向量模型计算句子间语义差异来决定切分点。使用 LangChain 的 SemanticChunker 实现，并介绍四种阈值控制方法。

## 核心内容

### 语义切分原理
- 通过查找任意两个句子之间的**向量差异**来确定切分点
- 当差异超过某个阈值时进行拆分
- 需要指定嵌入模型（如 OpenAIEmbeddings 或自定义模型）

### LangChain 实现
- `SemanticChunker(OpenAIEmbeddings())` — langchain_experimental 包
- `text_splitter.create_documents([text])` 完成切分

### 四种阈值控制方法（breakpoint_threshold_type）

1. **百分比（percentile）**：默认方式。计算句子之间所有差异，拆分大于 X 百分位数的差异。结果约 26 块。
2. **标准差（standard_deviation）**：拆分大于 X 个标准差的差值。结果约 4 块（粒度更粗）。
3. **四分位距（interquartile）**：使用四分位数距离分割。结果约 25 块。
4. **梯度（gradient）**：距离的梯度与百分位数方法结合。适用于块彼此高度相关或特定领域的场景。在梯度数组上应用异常检测，使分布更宽，易于识别高度语义数据中的边界。结果约 26 块。

## 关联

- 概念：[[概念_文本切分五层级]]、[[概念_语义切分]]、[[概念_Embedding与向量检索]]
- 实体：[[实体_LangChain]]
- 系列上一篇：[[RAG文本切分_JSON文档切分]]
