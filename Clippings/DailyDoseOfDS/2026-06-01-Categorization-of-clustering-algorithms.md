---
title: "Categorization of clustering algorithms."
source: "https://mail.google.com/mail/u/0/#inbox/19e84f32570b4582"
author:
  - "[[DailyDoseOfDS]]"
published: 2026-06-01
created: 2026-07-30
description: "聚类算法的系统化分类指南：基于划分、层次、基于密度（DBSCAN/HDBSCAN）、基于模型与基于网格的聚类算法特性对比。"
tags:
  - clippings
---

# 聚类算法分类全景指南（Categorization of clustering algorithms.）

聚类（Clustering）是无监督机器学习中最基础且核心的任务之一。根据数据划分方式、空间拓扑与假设模型的不同，主流聚类算法可划分为以下 5 大核心类别：

### 1. 基于划分的聚类（Partitioning-based Clustering）

* **典型算法**：K-Means, K-Medoids (PAM);
* **特点**：将包含 $N$ 个对象的数据集划分为 $K$ 个预先指定的簇，通过迭代优化样本到簇中心的平方误差；
* **局限**：必须预先指定 $K$ 值，且难以识别非凸形状（Non-convex）的几何簇。

---

### 2. 层次聚类（Hierarchical Clustering）

* **典型算法**：AGNES（自底向上凝聚）, DIANA（自顶向下分裂）;
* **特点**：构建树状层次结构（Dendrogram），无需预先指定簇数量；
* **局限**：合并或分裂决策不可逆，计算复杂度较高（通常为 $O(N^2)$ 或 $O(N^3)$）。

---

### 3. 基于密度的聚类（Density-based Clustering）

* **DBSCAN**：通过检测样本密度的连通性划分簇，能够自动发现任意复杂形状的簇并过滤噪点。但处理高维数据或密度分布不均的数据时性能较差，且计算复杂度较高。
* **HDBSCAN**：是 DBSCAN 的层次化延伸与升级版算法。它克服了 DBSCAN 必须全局统一密度阈值（$\text{eps}$）的局限，具备更出色的拓展性与更快的运行效率，能够自动处理多重密度梯度的聚类场景。

---

### 4. 基于模型的聚类（Model-based Clustering）

* **典型算法**：GMM（高斯混合模型，Gaussian Mixture Model）;
* **特点**：假设数据由若干底层概率分布组合生成，通过 EM 算法估算参数，提供软聚类（Soft Assignment）概率分布。

---

### 5. 基于网格的聚类（Grid-based Clustering）

* **典型算法**：STING, CLIQUE;
* **特点**：将数据空间划分为有限个网格单元，所有聚类操作直接在网格上展开，计算速度与数据量脱钩，极具扩展性。
