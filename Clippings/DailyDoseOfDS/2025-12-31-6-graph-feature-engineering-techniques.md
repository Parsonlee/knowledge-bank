---
title: "6 graph feature engineering techniques"
source: "https://mail.google.com/mail/u/0/#inbox/19b71b8454693ea2"
author:
  - "[[DailyDoseOfDS]]"
published: 2025-12-31
created: 2026-07-30
description: "详解在图机器学习（Graph ML）中基于节点度数与中心性度量的 6 种经典图特征提取技术。"
tags:
  - clippings
---

# 6 种图特征工程技术（6 graph feature engineering techniques）

在图机器学习（Graph ML）或传统机器学习模型处理图数据时，必须通过图特征工程（Graph Feature Engineering）将节点与边转化为数值特征向量。

本文解析 6 种最常用且效果显著的节点级特征提取技术：

![图 1：图特征工程示例数据集与图网络结构说明](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7cc469f9-8d3a-4df5-92da-bce46019c2f1_1456x937.png)
*说明：图 1：图特征工程示例数据集与图网络结构说明*

![图 2：图结构与其对应的邻接矩阵（Adjacency Matrix）表示](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe0f3bb60-07e4-4fd9-8fdf-fffe64399970_1456x796.png)
*说明：图 2：图结构与其对应的邻接矩阵（Adjacency Matrix）表示*

## 1-3) 节点度数特征（Node Degree Features）

![图 3：节点度数特征提取示意图](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe8803b31-8b39-4127-9eeb-5604b4a2a6b9_1456x1002.png)
*说明：图 3：节点度数特征提取示意图*

1. **入度（In-degree）**：指向该节点的有向边数量。在社交网络中代表被关注数，在论文网络中代表被引用数。
2. **出度（Out-degree）**：从该节点发出的有向边数量。在社交网络中代表关注人数，在交易网络中代表转账频次。
3. **总度数（Total Degree）**：入度与出度的总和，代表节点的综合连接活跃度。

![图 4：入度、出度与总度数具体计算图解](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5204166b-67d3-446a-a6d2-167543883138_1456x538.png)
*说明：图 4：入度、出度与总度数具体计算图解*

## 4-6) 节点中心性特征（Node Centrality Features）

![图 5：节点中心性指标概览](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fac01f0f6-5ad7-4766-9ab0-f07c26a08d48_1456x923.png)
*说明：图 5：节点中心性指标概览*

4. **度中心性（Degree Centrality）**：归一化的节点度数，反映节点在图中的局部重要性。
5. **特征向量中心性（Eigenvector Centrality）**：不仅考虑度数，还考虑邻居节点的质量——连接到高重要性节点的节点会获得更高得分（PageRank 算法的核心逻辑）。
6. **介数中心性（Betweenness Centrality）**：计算全图所有节点对的最短路径中经过该节点的比例，识别网络中的“交通枢纽”与关键桥梁节点。

![图 6：特征向量中心性与 PageRank 传递示意图](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fbe9c1e46-3be6-4177-a3bb-a94ff8497e65_634x424.png)
*说明：图 6：特征向量中心性与 PageRank 传递示意图*

![图 7：介数中心性与最短路径计算图解](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F616779a3-1c57-4baa-87fe-30e66592ea9c_634x424.png)
*说明：图 7：介数中心性与最短路径计算图解*

![图 8：接近中心性（Closeness Centrality）计算图解](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F2d19ada6-7ba4-4273-8781-1140e8dbd549_634x424.png)
*说明：图 8：接近中心性（Closeness Centrality）计算图解*
