---
title: "Breathing KMeans vs KMeans"
source: "https://mail.google.com/mail/u/0/#inbox/19d2bbc9492d99c6"
author:
  - "[[DailyDoseOfDS]]"
published: 2026-03-26
created: 2026-07-30
description: "详细介绍呼吸 K-均值算法（Breathing K-Means）如何通过动态吸气（增加质心）与呼气（删除无效质心）机制克服经典 K-Means 对初始质心敏感和容易陷入局部最优的问题。"
tags:
  - clippings
---
# Breathing KMeans 与 KMeans 算法对比（Breathing KMeans vs KMeans）

![Breathing KMeans 示意图](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F029b775a-2e7c-413f-b9f6-a1e03b588359_1456x1028.png)

在无监督学习（Unsupervised Learning）领域，**K-Means 聚类算法** 是应用最广的基础算法之一。然而，传统 K-Means 存在一个致命缺陷：**对初始质心位置高度敏感，极其容易陷入局部极小值（Local Minima）**。

即使采用 K-Means++ 进行初始化改善，面对复杂分布的数据集时，依然经常无法收敛至全局最优。

为了解决这一问题，研究人员提出了 **Breathing K-Means（呼吸 K-均值）算法**。该算法通过模仿生物的“吸气”与“呼气”过程，在迭代过程中动态调整质心数量，从而有效跳出局部极小值陷阱。

---

## Breathing K-Means 核心工作原理

Breathing K-Means 的核心思想是：**临时增加质心以探测更有利的簇空间（吸气），随后删除冗余或低效的质心（呼气），最终保持目标 $k$ 值不变。**

具体分为以下 5 个步骤：

### Step 1: 运行初始 K-Means
在数据集上运行标准的 K-Means，得到初始的 $k$ 个聚类质心。

### Step 2: 吸气阶段（Breathe-in Step）
向当前系统中**引入 $m$ 个新质心**（总质心数暂时变为 $k + m$）。新质心通常放置在误差平方和（SSE）最大、分布最松散的簇区域内，强行打破现有的僵化边界。

### Step 3: 呼气阶段（Breathe-out Step）
重新运行 K-Means 收敛后，评估所有 $k + m$ 个质心。根据质心对总 SSE 减少量的贡献，**移除表现最差的 $m$ 个质心**（质心数恢复为 $k$）。

### Step 4: 递减 $m$ 参数
将步长参数 $m$ 进行适当递减（如 $m = m - 1$）。

### Step 5: 循环迭代
重复执行 Step 2 到 Step 4，直到 $m = 0$ 为止。

---

## 算法对比总结

| 维度 | 标准 K-Means | Breathing K-Means |
| :--- | :--- | :--- |
| **初始点敏感度** | 极高，容易收敛到次优解 | 低，具备自我纠错能力 |
| **质心调整机制** | 质心数量固定不变 | 动态增加与删除质心试探最优解 |
| **收敛质量** | 易陷入 Local Minima | 更大概率逼近 Global Optima |
| **计算复杂度** | 较低 | 略高（多次内部迭代） |
