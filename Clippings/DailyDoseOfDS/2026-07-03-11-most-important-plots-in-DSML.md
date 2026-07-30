---
title: "11 most important plots in DS/ML."
source: "https://mail.google.com/mail/u/0/#inbox/19f29f70428b228f"
author:
  - "[[DailyDoseOfDS]]"
published: 2026-07-03
created: 2026-07-30
description: "全面总结数据科学与机器学习领域最核心的 11 种可视化图表及其在模型评估、解释性与特征工程中的关键应用。"
tags:
  - clippings
---
# 数据科学与机器学习中最核心的 11 种可视化图表（11 most important plots in DS/ML.）

在数据科学（DS）与机器学习（ML）实践中，可视化图表对于模型诊断、特征选择和结果解释至关重要。本文整理了 11 种必须掌握的关键图表及其核心应用场景。

![数据科学 11 种核心图表全景图](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7d9a3c85-2d42-4453-9dad-20ae24da3994_1208x776.png)
*说明：数据科学 11 种核心图表全景指南*

---

## 1) KS 曲线（KS Plot / Kolmogorov-Smirnov Curve）

![KS Plot 图解](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F474c275c-114a-4e25-a35a-d87199b799b8_1200x716.png)

* **作用**：评估二分类模型对正负样本的区分能力（Separation Power）。
* **解读**：KS 统计量表示累积正样本曲线与累积负样本曲线之间的最大垂直距离。KS 值越高，模型的区分能力越强（常见于风控信用评分卡评估）。

---

## 2) SHAP 摘要图（SHAP Plot）

![SHAP Plot 图解](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe1827901-140d-440e-ad1a-399bfab36e0f_1448x676.png)

* **作用**：展示特征对模型预测结果的贡献度与影响方向。
* **解读**：结合特征重要性（纵轴按影响排序）与特征取值高低（颜色深浅），直观呈现每个特征是正向推高还是负向拉低预测值。

---

## 3) ROC 曲线（ROC Curve）

![ROC Curve 图解](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0725182f-9dbd-41ca-880e-7d789abc8bc5_1272x704.png)

* **作用**：衡量分类模型在不同决策阈值下的综合表现。
* **解读**：横轴为假正率（FPR），纵轴为真正率（TPR）。曲线下包围的面积（AUC）越大，模型的整体分类性能越好。

---

## 4) 精确率-召回率曲线（Precision-Recall Curve / PR Curve）

![Precision-Recall Curve 图解](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa79c8fc6-4092-403b-aba9-a5b6b38e04d8_1468x688.png)

* **作用**：在极度不平衡数据集（Imbalanced Datasets）中评估模型性能。
* **解读**：对比精确率（Precision）与召回率（Recall）之间的权衡，在正样本极少时比 ROC 曲线更具针对性。

---

## 5) QQ 图（Quantile-Quantile Plot / QQ Plot）

![QQ Plot 图解](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fccf1a5ed-bdbd-4543-a993-7f27f5ace198_1336x688.png)

* **作用**：检验数据分布是否符合某种理论分布（如正态分布）。
* **解读**：若数据点紧密贴合 45 度对角线，则说明实际分布与目标理论分布高度吻合。

---

## 6) 累积解释方差图（Cumulative Explained Variance Plot - PCA）

![Cumulative Explained Variance Plot 图解](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ffd0676d3-17cc-40eb-8928-b3f0a8f931f2_1456x1380.png)

* **作用**：帮助确定主成分分析（PCA）降维时的最佳主成分保留数量。
* **解读**：展示前 $k$ 个主成分对原始数据总方差的累积解释比例（例如达到 90% 或 95% 所需的维数）。

---

## 7) 肘部法则曲线（Elbow Curve）

![Elbow Curve 图解](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc1dd132d-25f8-4091-854d-2d5eb6e5381d_1308x676.png)

* **作用**：辅助确定 K-means 聚类算法中的最佳簇数量（Cluster Count $K$）。
* **解读**：随着 $K$ 增加，簇内平方和（WCSS）逐渐降低，曲线拐折处的“肘部”点通常对应最佳聚类数。

---

## 8) 轮廓系数曲线（Silhouette Curve）

![Silhouette Curve 图解](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc0437d11-f1b1-4ef2-ac24-05522e472593_1496x676.png)

* **作用**：当肘部法则不够清晰时，替代或补充用于聚类质量评估。
* **解读**：衡量样本在同簇内的紧密程度与异簇间的分离程度，轮廓系数越接近 1 说明聚类效果越好。

---

## 9) 基尼不纯度与熵对比图（Gini-Impurity and Entropy）

![Gini-Impurity and Entropy 图解](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F727cfc1e-bb11-4961-8938-176bbe8f6bfa_1276x676.png)

* **作用**：度量决策树节点分裂时的不纯度（Impurity）与混乱程度。
* **解读**：展示在不同节点类别比例下，基尼系数与信息熵的曲率差异及其对树生长决策的影响。

---

## 10) 偏差-方差权衡图（Bias-Variance Tradeoff）

* **作用**：指导机器学习模型复杂度的选择，防止欠拟合与过拟合。
* **解读**：随着模型复杂度增加，偏差（Bias）降低而方差（Variance）上升，总误差曲线的最低点代表最优模型复杂度。

---

## 11) 部分依赖图（Partial Dependency Plots / PDP）

* **作用**：展示一个或两个特征与预测目标之间的边际效应关系。
* **解读**：1-way PDP 呈现单一特征对目标的影响轨迹，2-way PDP 呈现特征交互项对目标的作用。
