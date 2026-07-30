---
title: "11 most important DS Plots"
source: "https://mail.google.com/mail/u/0/#inbox/19b7766d2c7e9ffc"
author:
  - "[[DailyDoseOfDS]]"
published: 2026-01-01
created: 2026-07-30
description: "全面解析机器学习与数据科学中 11 种最关键的诊断与评估图表，涵盖 KS 图、SHAP 图、ROC 曲线、PR 曲线、QQ 图等。"
tags:
  - clippings
---

# 数据科学中最重要的 11 种核心图表（11 most important DS Plots）

在数据科学与机器学习建模的全生命周期中，可视化图表是发现数据模式、诊断模型缺陷以及评估预测性能的最有效工具。

本文深度拆解数据科学家必须熟练掌握的 11 种核心评估图表：

![图 1：11 种核心数据科学图表全景动图概览](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F286632a3-be0e-45ba-bfa2-dfdaa275d090_793x944.gif)
*说明：图 1：11 种核心数据科学图表全景动图概览*

## 1. KS 图（Kolmogorov-Smirnov Plot）
评估二分类模型对正负样本的区分区分度，通过测量正负样本累积分布函数（CDF）之间的最大垂直距离度量模型区分能力。

![图 2：KS 曲线示意图](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F25a87b56-cedd-4938-9363-5c76e09c1b72_1244x676.png)
*说明：图 2：KS 曲线示意图*

## 2. SHAP 图（SHAP Value Plot）
全局与局部可解释性工具，基于博弈论 Shapley 值清晰展示每个特征对模型预测结果贡献的大小与作用方向。

![图 3：SHAP 特征重要性与影响分布图](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7d9a3c85-2d42-4453-9dad-20ae24da3994_1208x776.png)
*说明：图 3：SHAP 特征重要性与影响分布图*

## 3. ROC 曲线（Receiver Operating Characteristic Curve）
绘制真正率（TPR）与假正率（FPR）在不同判定阈值下的变化曲线，AUC 面积综合度量二分类模型的排序能力。

![图 4：ROC 曲线与 AUC 说明](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F474c275c-114a-4e25-a35a-d87199b799b8_1200x716.png)
*说明：图 4：ROC 曲线与 AUC 说明*

## 4. Precision-Recall 曲线（PR 曲线）
类别不平衡数据集下的最佳评估图表，直观展示精确率（Precision）与召回率（Recall）之间的权衡关系。

![图 5：PR 曲线示意图](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe1827901-140d-440e-ad1a-399bfab36e0f_1448x676.png)
*说明：图 5：PR 曲线示意图*

## 5. QQ 图（Quantile-Quantile Plot）
检验样本数据的残差或特征分位数与理论正态分布分位数是否吻合的分位数对照图。

![图 6：QQ 正态分布检验图](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0725182f-9dbd-41ca-880e-7d789abc8bc5_1272x704.png)
*说明：图 6：QQ 正态分布检验图*

## 6. 累积解释方差图（Cumulative Explained Variance Plot）
在主成分分析（PCA）降维时，帮助确定保留多少个主成分才能覆盖大部分原始信息方差。

![图 7：PCA 累积解释方差图](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa79c8fc6-4092-403b-aba9-a5b6b38e04d8_1468x688.png)
*说明：图 7：PCA 累积解释方差图*

## 7. 肘部法则曲线（Elbow Curve Plot）
K-Means 聚类中依据簇内离差平方和（WCSS）的拐点确定最佳聚类簇数 $K$ 的经典诊断图。

![图 8：K-Means 肘部法则图](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fccf1a5ed-bdbd-4543-a993-7f27f5ace198_1336x688.png)
*说明：图 8：K-Means 肘部法则图*

## 8. 轮廓系数曲线（Silhouette Curve Plot）
衡量聚类结果中样本在簇内的紧密程度与簇间的分离程度，辅助选择优质聚类参数。

![图 9：轮廓系数得分分布图](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ffd0676d3-17cc-40eb-8928-b3f0a8f931f2_1456x1380.png)
*说明：图 9：轮廓系数得分分布图*

## 9. 基尼不纯度与熵基准图（Gini-Impurity and Entropy）
决策树分类算法选择最优节点分裂属性时，基尼系数与信息熵的理论曲线对比。

![图 10：基尼不纯度与熵特征选择曲线](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc1dd132d-25f8-4091-854d-2d5eb6e5381d_1308x676.png)
*说明：图 10：基尼不纯度与熵特征选择曲线*

## 10. 偏差-方差权衡图（Bias-Variance Tradeoff）
揭示模型复杂度与泛化误差之间的关系，指导识别欠拟合（High Bias）与过拟合（High Variance）。

![图 11：偏差-方差权衡关系分析图](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc0437d11-f1b1-4ef2-ac24-05522e472593_1496x676.png)
*说明：图 11：偏差-方差权衡关系分析图*

## 11. 局部依赖图（Partial Dependency Plots - PDP）
展示一个或两个特定输入特征对模型边际预测输出的影响趋势。

![图 12：局部依赖图（PDP）示意图](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F727cfc1e-bb11-4961-8938-176bbe8f6bfa_1276x676.png)
*说明：图 12：局部依赖图（PDP）示意图*
