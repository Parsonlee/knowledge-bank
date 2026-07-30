---
title: "无标签场景下的聚类评估（Clustering evaluation without labels）"
source: "https://mail.google.com/mail/u/0/#inbox/1995434d669b06de"
author:
  - "[[DailyDoseOfDS]]"
published: 2025-09-16
created: 2026-07-30
description: "介绍无真实标签时评估聚类质量的三种内在指标：轮廓系数、Calinski-Harabasz 指数与 DBCV。"
tags:
  - clippings
---

# 无标签场景下的聚类评估（Clustering evaluation without labels）

在没有真实标签时，聚类质量通常难以评估，因此需要依赖内在度量（intrinsic measures）。以下是邮件列出的三种常用指标。

## 1. 轮廓系数（Silhouette Coefficient）

若一个点到同簇所有其他点的平均距离较小，而到另一簇的距离较大，说明这些簇分离良好、结果较为可靠。

对每个数据点：

* $A$：该点到本簇其他所有点的平均距离；
* $B$：该点到最近簇中所有点的平均距离；
* $score = \frac{B-A}{\max(B,A)}$。

对所有点的分数取平均，即得到整体聚类分数。当 $B \gg A$ 时，$score \approx 1$，表示簇的分离度好。比较不同质心数 $k$ 下的分数，可找出最有希望的聚类结果。

## 2. Calinski-Harabasz 指数

轮廓系数的运行时间会随数据点总数呈二次增长。Calinski-Harabasz（CH）指数具有相似直觉，但计算更快。

* $A$：各簇中心到数据集中心的平方距离之和；
* $B$：所有数据点到其所属簇中心的平方距离之和；
* 指标按 $\frac{A}{B}$（另加缩放因子）计算。

当 $A \gg B$ 时，分数远大于 1，表明聚类分离得较好。

## 3. DBCV（Density-Based Clustering Validation）

轮廓系数和 CH 指数通常更偏好团状（3D 中为球形）簇；对密度聚类使用它们可能导致误导。DBCV 针对这一点计算：

* 簇内密度；
* 簇与簇之间的密度重叠。

簇内密度高、簇间密度重叠低，代表较好的聚类结果。邮件中的对比指出：KMeans 的结果在密度结构上较差，但其轮廓系数仍可能高于密度聚类；使用 DBCV 时，KMeans 得分较低、密度聚类得分较高，更符合该场景的实际质量。

延伸阅读：邮件还链接了 [Calinski-Harabasz 指数的 scikit-learn 文档](https://scikit-learn.org/stable/modules/clustering.html#calinski-harabasz-index)、[DBCV 实现](https://github.com/christopherjenness/DBCV)、[高斯混合模型（GMM）](https://www.dailydoseofds.com/gaussian-mixture-models-gmm/) 与 [DBSCAN++](https://www.dailydoseofds.com/dbscan-the-faster-and-scalable-alternative-to-dbscan-clustering/)。
