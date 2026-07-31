---
title: "ANN search using inverted file index."
source: "https://mail.google.com/mail/u/0/#inbox/19a274be34a3e99c"
author:
  - "[[DailyDoseOfDS]]"
published: 2025-10-27
created: 2026-07-30
description: "详细拆解向量数据库中基于倒排文件索引（IVF）的近似最近邻（ANN）搜索算法原理与时间复杂度推导。"
tags:
  - clippings
---

# 使用倒排文件索引的近似最近邻（ANN）搜索（ANN search using inverted file index.）

在海量向量数据检索中，传统的精确 **kNN（k-Nearest Neighbors）** 算法需要将查询向量与数据库中的每一个向量进行穷举距离计算，在数据量达到数百万或数亿级别时，查询延迟将不可接受。

![kNN 穷举搜索与 ANN 近似搜索对比](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F71e5cfd4-7661-4426-9e57-a6115654b5b3_1140x454.gif)

为了解决这一性能瓶颈，**近似最近邻（Approximate Nearest Neighbor, ANN）** 搜索算法通过建立索引来缩减搜索空间。其中，**倒排文件索引（Inverted File Index, IVF）** 是一种最简单、最直观的索引技术。

![倒排文件索引 (IVF) 核心架构图](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4efa275d-c8ee-4332-8648-f69a70fe6d68_1504x884.png)

---

### IVF 索引构建步骤

建索引过程主要分为以下阶段：

1. **聚类划分（Partitioning）**：使用 K-Means 等算法对输入的训练向量数据进行聚类划分，得到 $K$ 个聚类中心（Centroids）。

![聚类划分步骤](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fefcd3013-5d0d-4862-a6a5-f487ae34bbce_2184x676.png)

2. **向量关联（Association）**：将每个数据点关联到距离其最近的唯一一个聚类中心分区中。

![向量点关联分区](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fbcbfb865-09ee-41d8-891f-e003ddac6d77_2048x684.png)

3. **映射表构建（Map Building）**：维护一个倒排哈希映射表（Inverted Map），保存每个聚类中心 ID 及其所属的所有向量数据点集合。

![倒排映射表构造](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F1485046c-35b6-434b-8afc-4af53c35e69e_1728x796.png)

---

### IVF 查询阶段

当发起向量查询时，检索分为两步进行：

1. **查找最近聚类中心**：计算查询向量与所有 $K$ 个聚类中心的距离，找出最近的中心。

![步骤 1：查找最近聚类中心](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3aa59990-088f-4954-9547-2267c3931230_1700x756.png)

2. **局部精确查找**：仅在目标聚类中心包含的数据点集合中，计算查询向量与这些点的最近邻。

![步骤 2：在目标分区中精确查找](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F1c8b11cc-047f-4103-98f3-c806cb658050_1820x716.png)

---

### 时间复杂度对比推导

假设：
- 数据总量为 $N$ 个向量；
- 每个向量的维度为 $D$；
- 创建了 $K$ 个聚类分区；
- 假设每个分区均匀分布有 $N/K$ 个数据点。

#### 1. 精确 kNN 搜索复杂度
查询向量需要与所有 $N$ 个向量计算距离：

$$	ext{Complexity}_{	ext{kNN}} = O(N \cdot D)$$

#### 2. IVF 近似搜索复杂度
- 第一步：与 $K$ 个聚类中心做匹配，复杂度为 $O(K \cdot D)$；
- 第二步：在最近分区内的 $N/K$ 个向量中查找最近邻，复杂度为 $O(rac{N}{K} \cdot D)$。

总时间复杂度为：

$$	ext{Complexity}_{	ext{IVF}} = O\left(K \cdot D + rac{N}{K} \cdot D
ight)$$

![IVF 时间复杂度计算公式](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fae4e0e08-91d4-4050-ad96-07a3e6236d1b_325x114.png)

#### 实际性能量化：
当 $N = 10,000,000$ (1000 万)，$K = 100$ 时：
- **kNN 复杂度** 正比于 $10,000,000$；
- **IVF 复杂度** 正比于 $100 + rac{10,000,000}{100} = 100,100$。

检索效率提升了近 **100 倍**！

---

### 准确率权衡（Accuracy Trade-offs）

近似最近邻（ANN）并非 100% 完美。如果某些数据点在空间上距离查询点非常近，但碰巧划归到了相邻的其他分区中，它们就会被 IVF 遗漏：

![分区边界处数据遗漏权衡](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F36119d6b-8644-4f97-b824-8f110e20c749_1808x744.png)

在生产实践中，为了获得极低延迟，我们通常主动接受这种微小的召回率（Recall）损失。
