---
title: "Phases of ML Modeling"
source: "https://mail.google.com/mail/u/0/#inbox/19c102bf0ed3e544"
author:
  - "[[DailyDoseOfDS]]"
published: 2026-01-30
created: 2026-07-30
description: "解析机器学习建模的四个演进阶段：从启发式规则基线，到最简 ML 模型，再到模型优化与复杂深度学习模型，降低系统风险。"
tags:
  - clippings
---
# 机器学习建模的四个阶段（Phases of ML Modeling）

大多数机器学习系统并不会直接跳到深度学习，而是遵循渐进演化的阶段。

一种实用的思考方式是将这一过程拆分为多个阶段，从最简单的解决方案开始，仅在必要时才增加复杂度。因为不必要的复杂度等于低实用性。

![ML 建模阶段概述图](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F33dc6716-4847-43bc-aa16-72de11bcb06b_797x267.png)

分阶段方法可以降低风险，提高可调试性，并且非常契合 MLOps 的最佳实践。

下面让我们走过 ML 模型开发的各个阶段：

## 阶段 1：在 ML 之前（启发式规则）

如果是第一次解决某个问题，请抵制一上来就构建模型的冲动。先从非 ML 基线开始：规则、启发式策略或简单的确定性算法。

例如，在电影推荐系统中，阶段 1 的解决方案可以简单到向每位用户推荐 Top-10 最受欢迎的电影。

虽然这听起来很天真，但此类启发式规则往往出奇地强强。这些基线构建快速、易于理解，并确立了最低性能门槛。如果复杂的 ML 模型打败不了简单启发式规则，那说明流程存在问题或 ML 根本没有带来价值。

![阶段 1 启发式规则映射](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F9158da26-a336-4cc6-ad30-777b80fb8294_1024x505.png)

## 阶段 2：最简 ML 模型

一旦启发式基线建立（或确定规则不够用），下一步仍然不是深度模型，而是**最简单可行的 ML 模型**。

想想逻辑回归、浅层决策树、k 近邻（kNN）或简单线性模型。这些模型易于训练、解释和部署。

本阶段的目标不是追求巅峰准确率，而是回答基础问题：
* 能否基于历史数据训练并得到合理的预测？
* 特征是否有效？
* 模型泛化性能是否优于启发式规则？

这也是验证端到端 ML 流水线（数据接入、特征提取、训练、评估、服务）的关键阶段。

![阶段 2 最简 ML 模型验证](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F15940d4d-0f8c-4bee-b280-09e04b27f5f6_1024x504.png)

## 阶段 3：优化简单模型

基础模型工作后，在不改变模型族的前提下，往往还有巨大的性能提升空间。阶段 3 致力于从现有方法中榨取尽可能多的价值：

常见杠杆包括：
* **特征工程**：创建更好的输入数据表达；
* **超参数调优**：系统地搜索更好的配置；
* **扩充数据**：扩大数据集或提高数据质量。

这一阶段的投资回报率（ROI）往往最高。

![阶段 3 模型优化循环图](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb4a6eb4b-9e63-4790-9af1-93a82f66fa1d_1511x782.png)

## 阶段 4：复杂模型

只有当简单方法被彻底穷尽后，才应当转向 fundamentally 更加复杂的模型（如深度神经网络、Transformer 或大规模预训练架构）。

![阶段 4 复杂深度模型演进](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe52e4e5f-0806-4e2d-97f3-bed894de2c88_1257x617.png)

复杂模型带来了高表达能力，但也带来了高工程成本。进入阶段 4 的决策应当由证据驱动。在每个阶段，前一阶段的最佳模型都将成为新的基线。
