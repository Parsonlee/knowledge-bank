# 概念_Dense_Embedding

> tags: RAG, RAG/embedding
> confidence: high

## 定义

Dense Embedding（语义级稠密向量）将文本编码为低维全非零向量，捕捉语义信息。

## 特点

- 典型模型：text-embedding-3-large、BGE、E5-mistral
- 向量形态：256~1536 维，全部非零
- 相似度计算：余弦距离
- 优点：捕捉同义、上下位、跨语言语义
- 痛点：需要 GPU/CPU 推理，单条 10~100ms；维度越低信息越"挤"，需折中精度与存储

## 适用场景

- 通用语义搜索首选，用户用"人话"提问时显威力
- 案例：SaaS 客服 FAQ 检索，TOP1 命中率从关键词的 62% 提升到 89%
- 实践建议：先用 Dense 打 baseline，再决定是否需要更复杂方案

## 关联

- 相关概念：[[概念_Embedding与向量检索]]、[[概念_Sparse_Embedding]]、[[概念_Quantized_Embedding]]、[[概念_Matryoshka表示学习]]
- 来源：[[从BM25到Multi-Vector_6种Embedding演进路线]]
