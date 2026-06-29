# 概念_Embedding与向量检索

> tags: RAG, RAG/embedding
> confidence: high

## 定义

将文本表示（Text Representation）转成数值表示（Numerical Representation），以便通过相似度（如余弦相似度）衡量相关性。

## 文本转数值的方法

- **Statistical（基于统计学）**
- **Machine Learned（基于机器学习）** — 目前最常用

机器学习方法将文本转成固定长度、可捕获语义的 Embedding Vector（嵌入向量）。

## Embedding Model 的限制

- 开源模型如 BAAI 系列
- Context Window（上下文窗口）有限，一般 512~8192 token
- 因此需将文档切分为 Split 满足上下文窗口限制

## 检索原理

根据问题的 Embedding Vector，按某种距离/相似度衡量方法找出最相似的 k 个 Split 的语义向量。

## 关联

- 相关概念：[[概念_RAG基础流程]]、[[概念_向量数据库]]、[[概念_ColBERT]]、[[概念_语义切分]]、[[概念_词向量]]、[[概念_BERT各向异性]]、[[概念_Sentence-BERT]]、[[概念_SimCSE]]、[[概念_Dense_Embedding]]、[[概念_Sparse_Embedding]]、[[概念_Matryoshka表示学习]]、[[概念_Instruct_Embedding]]
- 来源：[[RAG基础_索引检索生成]]、[[RAG文本切分_语义切分]]、[[一文详尽之Embedding]]、[[从BM25到Multi-Vector_6种Embedding演进路线]]、[[MRL_俄罗斯套娃表示学习]]、[[为什么用Qwen3_embedding和rerank]]
