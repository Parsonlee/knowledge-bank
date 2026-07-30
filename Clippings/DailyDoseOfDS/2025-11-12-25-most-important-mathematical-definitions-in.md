---
title: "25 most important mathematical definitions in DS"
source: "https://mail.google.com/mail/u/0/#inbox/19a79cbb943dd0f0"
author:
  - "[[DailyDoseOfDS]]"
published: 2025-11-12
created: 2026-07-30
description: "精炼总结数据科学与机器学习实践中最关键的 25 个核心数学概念与公式定义全景图。"
tags:
  - clippings
---

# 数据科学中最重要的 25 个数学定义（25 most important mathematical definitions in DS）

数学是数据科学与机器学习的基石。建立对底层核心数学概念的深刻直觉，能够帮助开发者更好地理解算法机制、调试模型瓶颈以及设计创新的架构。

![数据科学中最重要的 25 个数学概念全景图](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa4ae2974-664e-489e-9504-8421700ccb76_1456x2059.png)

以下是数据科学实践中最为核心的部分数学概念拆解：

### 1. Softmax 函数
Softmax 函数用于将一个实值向量转化为概率分布，使其所有元素的和为 1。在多分类任务与 Transformer 的 Attention 权重计算中扮演重要角色：

$$	ext{Softmax}(z_i) = rac{e^{z_i}}{\sum_{j=1}^{K} e^{z_j}}$$

![Softmax 与 Cross-Entropy 示意图](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc58b127c-09d5-49fb-8946-30372f97ff47_1220x708.png)

### 2. 交叉熵损失（Cross-Entropy Loss）
交叉熵衡量了预测概率分布与真实分布之间的差异，是分类模型中最常用的损失函数。

### 3. 基尼不纯度（Gini Impurity）
衡量从集合中随机选择的元素被错误标记的概率。基尼不纯度常用于决策树分类算法（如 CART）以及 t-SNE 的分割计算。

### 4. 特征向量与特征值（Eigenvectors and Eigenvalues）
在矩阵线性变换下方向保持不变的非零向量称为特征向量，其缩放比例称为特征值。它们是主成分分析（PCA）等降维算法的核心。

### 5. $R^2$ 判定系数（R-squared）
$R^2$ 是衡量回归模型解释因变量变异程度的统计指标，其取值范围通常在 $0$ 到 $1$ 之间。

![R-squared 公式与概念示意图](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fde593f44-3ee1-48e5-b7b6-3a2006e2d705_1356x676.png)

### 6. KL 散度（Kullback-Leibler Divergence）
KL 散度用于评估使用一个概率分布来近似另一个真实概率分布时的信息损失量，广泛用于 VAE（变分自编码器）、t-SNE 以及 RLHF 训练中。

### 7. 奇异值分解（SVD）
SVD 是一种将任意矩阵分解为三个特定矩阵相乘的因子分解技术（$A = U \Sigma V^T$），是降维、去噪、推荐系统和数据压缩的基础工具。

### 8. 拉格朗日乘子法（Lagrange Multipliers）
拉格朗日乘子法是求解带约束条件的极值问题的经典数学工具。例如在目标函数 $f(x)$ 满足约束条件 $g(x)=0$ 时构造拉格朗日函数求解，在 SVM 和 PCA 的推导中至关重要。

![SVD 与拉格朗日乘子法结构图解](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F363104d2-e8f4-45e7-8a5f-4d1e4e75983b_1708x684.png)
