---
type: entity
tags:
  - DeepLearning
summary: "深度学习中常用的自适应梯度下降优化器，兼顾 Momentum 与 RMSProp 优点。"
created: "2026-06-29"
updated: "2026-07-01"
confidence: high
---

## 简介

Adam（Adaptive Moment Estimation）是深度学习中常用的梯度下降优化器，同时兼顾 Momentum 和 RMSProp 的优点，近年来是深度学习问题的常用选择。

## 核心要点

- 公式：
  - sum_of_gradient = previous * beta1 + gradient * (1-beta1)【Momentum 一阶矩】
  - sum_of_gradient_squared = previous * beta2 + gradient² * (1-beta2)【RMSProp 二阶矩】
  - delta = -learning_rate * sum_of_gradient / sqrt(sum_of_gradient_squared)
- 默认超参：beta1=0.9（一阶矩衰减率），beta2=0.999（二阶矩衰减率）
- 速度来源：动量提供速度 + RMSProp 提供适应不同方向梯度的能力
- 实验表现：在有两座小山阻挡的地形中，Adam 是唯一能找到全局极小值的方法（动量越过局部极小值 + 二阶矩调整侧向移动）

## 相关概念

- [[概念_梯度下降优化器]]

## 来源

- [[梯度下降优化器可视化解释]]

