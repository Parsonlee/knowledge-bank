---
type: source
tags:
- RAG/embedding
summary: HuggingFace 俄罗斯套娃嵌入模型概述——MRL 训练原理、Sentence Transformers 实现、截断使用方法与性能实验
sources:
- raw/俄罗斯套娃 (Matryoshka) 嵌入模型概述 - HuggingFace ....md
created: 2026-06-26
updated: '2026-07-01'
confidence: high
---
# Matryoshka嵌入模型概述_HuggingFace

## 核心内容

### 嵌入基础

- 嵌入是复杂数字对象（文本、图像、音频等）的数值表示
- 嵌入模型总是产生相同固定大小的嵌入
- 通过计算嵌入的相似性来衡量对象相似性
- 应用领域：推荐系统、信息检索、零样本学习、异常检测、相似性搜索、聚类、分类等

### 俄罗斯套娃嵌入动机

- 新的 SOTA 嵌入模型输出维度越来越高，提高性能但牺牲下游任务效率
- Kusupati 等人（2022）提出即使嵌入尺寸合理缩小也不会在性能上遭受太大损失的模型
- 核心设计：将更重要的信息存储在早期维度中，不太重要的信息存储在后面的维度中

### 使用场景

1. **筛选和重新排序**：先用缩小的嵌入高效"筛选"，再用完整维度处理剩余嵌入
2. **权衡**：根据所需的存储成本、处理速度和性能来扩展嵌入解决方案

### 训练方法（Sentence Transformers）

- 一个训练步骤产生嵌入后，使用损失函数确定多种不同维度下的嵌入质量（如 768/512/256/128/64）
- 各维度损失值加在一起得到最终损失值
- 使用 `MatryoshkaLoss` 包裹基础损失函数（如 `CoSENTLoss`）
- 通过 `matryoshka_dims` 指定截断维度，`matryoshka_weight` 指定权重
- 训练时间不会显著增加

### 推理使用

- 加载模型后正常 encode，然后对嵌入做切片截断：`embeddings[..., :matryoshka_dim]`
- 截断后如果原嵌入已归一化，需要重新归一化
- 获取较小嵌入的速度与获取较大嵌入的速度一样快（推理不加速，下游任务加速）

### 实验结果

- 在 STSBenchmark 测试集上，俄罗斯套娃模型在所有维度上都达到比标准模型更高的 Spearman 相似度
- 嵌入大小只有 8.3% 时，俄罗斯套娃模型保持 98.37% 的性能，远高于标准模型的 96.46%
- 结论：截断嵌入可显著加快下游任务速度、显著节省存储空间而不显著影响性能

### 代表模型

- tomaarsen/mpnet-base-nli-matryoshka
- nomic-ai/nomic-embed-text-v1.5（Nomic 推荐截断前做 Layer Normalization）

## 关联

- 相关概念：[[概念_Matryoshka表示学习]]、[[概念_Embedding与向量检索]]
- 实体：[[实体_Sentence_Transformers]]
- 参考论文：Kusupati et al. (2022). Matryoshka representation learning. NeurIPS 35. https://arxiv.org/abs/2205.13147
