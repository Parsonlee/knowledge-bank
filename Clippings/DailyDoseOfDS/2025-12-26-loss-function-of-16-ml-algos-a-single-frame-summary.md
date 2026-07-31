---
title: "Loss Function of 16 ML Algos"
source: "https://mail.google.com/mail/u/0/#inbox/19b5c7637722a2ba"
author:
  - "[[DailyDoseOfDS]]"
published: 2025-12-26
created: 2026-07-30
description: "一图全览 16 种常用机器学习算法的核心损失函数配置，涵盖线性回归、逻辑回归、SVM、决策树、Adaboost 及神经网络等。"
tags:
  - clippings
---

# 16 种机器学习算法的损失函数全景总结（Loss Function of 16 ML Algos）

损失函数（Loss function）是机器学习算法的核心组成部分。深入理解哪些损失函数最适合特定的机器学习算法，对于模型训练与调优至关重要。

下图总结了各种经典 ML 算法中最常用的损失函数：

![16 种 ML 算法损失函数全景图](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fcb8005a7-8f4e-483e-995e-ab9f47c8cb84_2820x1020.png)

---

### 各算法损失函数明细

1. **线性回归（Linear Regression）**：
   * 均方误差（Mean Squared Error, MSE）。根据实际情况，可结合或不结合正则化项（L1/L2）。

2. **逻辑回归（Logistic Regression）**：
   * 交叉熵损失（Cross-Entropy Loss）或对数损失（Log Loss），可带正则化。

3. **决策树与随机森林（Decision Tree & Random Forest）**：
   * 分类任务：基尼不纯度（Gini Impurity）或信息增益（Information Gain）。
   * 回归任务：均方误差（MSE）。

4. **支持向量机（SVM）**：
   * 合页损失（Hinge Loss）。它对错误预测以及置信度不足的正确预测均施加惩罚，最适合构建最大间隔分类器。

5. **K-近邻算法（kNN）**：
   * **无损失函数**。kNN 是一种非参数懒惰学习算法（Lazy learning），它直接存储训练实例，并在预测时计算测试样本与 $k$ 个最近邻的距离。

6. **朴素贝叶斯（Naive Bayes）**：
   * **无损失函数**。它基于贝叶斯定理进行条件概率估计，不通过梯度下降求解损失函数。

7. **神经网络（Neural Networks）**：
   * 回归任务：均方误差（MSE）。
   * 分类任务：交叉熵损失（Cross-Entropy Loss）。

8. **AdaBoost**：
   * 指数损失函数（Exponential Loss）。AdaBoost 是一种集成学习算法，在每次迭代中提高上一轮被错分样本的权重，训练新的弱分类器以最小化加权指数损失。

9. **其他 Boosting 算法（Gradient Boosting / XGBoost 等）**：
   * 回归任务：均方误差（MSE）或 Huber 损失。
   * 分类任务：交叉熵损失（Cross-Entropy Loss）。
