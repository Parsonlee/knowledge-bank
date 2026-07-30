---
title: "How to use kNNs for imbalanced datasets"
source: "https://mail.google.com/mail/u/0/#inbox/19acc373a89bc8c4"
author:
  - "[[DailyDoseOfDS]]"
published: 2025-11-28
created: 2026-07-30
description: "探讨如何通过距离加权 kNN 与动态调整 k 值优化不平衡数据集下的 kNN 分类性能。"
tags:
  - clippings
---

# 如何在不平衡数据集上高效使用 kNN（How to use kNNs for imbalanced datasets）

在 K-近邻（kNN）算法中，超参数 $ 的选择对预测结果至关重要，而在类别不平衡（Imbalanced Datasets）场景下，传统的 kNN 往往表现欠佳。

![二维数据集与测试样本示意图](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F872e7be0-cee5-43b1-8746-e4f8b48add43_1672x864.png)

![标准 kNN 在 k=7 下的投票流程](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F2b360269-f208-4d82-a539-625cd8deda17_1456x699.png)

### 传统 kNN 在不平衡数据下的缺陷

如上图所示，当 =7$ 时，测试点寻找最近的 7 个邻居进行多数投票（Majority Voting）。在不平衡数据集中，由于多数类样本在数据空间中占据主导地位，测试点附近的 7 个邻居很可能绝大多数都是多数类样本，即便该测试点距离少数类样本非常接近。这会导致模型强烈偏向多数类，严重误判少数类。

![多数类占优导致误判示意图](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa60b3e8e-ece3-4bc1-a6c5-7c6f4791023a_1456x708.png)

为了解决这一难题，可以采用以下两种改进方案：

### 解决方案 1：使用距离加权 kNN（Distance-weighted kNN）

![距离加权 kNN 权重计算公式](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ffdb2357e-8717-421f-9b50-24dfa43a3b74_1456x708.png)

距离加权 kNN 不再对所有邻居一视同仁，而是根据邻居与测试点之间的距离计算权重 $：
15624w = rac{1}{d} \quad 	ext{或} \quad w = rac{1}{d^2}15624

![距离较近的少数类获得更高投票权重](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F9924e4f5-7a87-488a-b255-c9b92bfe591d_1432x654.png)

![加权投票计算结果示意图](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F99785e04-cdce-4ead-a333-d0423794db31_1432x654.png)

距离越近的样本获得的投票权重越大。因此，即便 7 个邻居中有 4 个多数类和 3 个少数类，由于 3 个少数类距离更近，它们的总加权权重也会超过远距离的多数类，从而正确预测为少数类。

### 解决方案 2：动态更新超参数 k（Dynamically update k）

第二种策略是根据数据集的偏斜比例动态调整邻居数量 $。

![计算不平衡比例计算公式](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F33ac222e-129e-423e-b7a7-c7f64947b722_989x498.png)

![计算动态邻居数 k' 公式](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7c2ed832-98fd-4d97-883a-094bb75719f1_1456x592.png)

![动态缩减邻居窗口范围图解](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F1a0214c7-85de-480f-8d02-6e8cd1c1eec9_2840x700.png)

![仅在前 k' 个邻居中执行多数投票](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc70e7336-f577-4644-913c-0ab093c6f94a_347x105.png)

**操作逻辑：**
1. 首先计算少数类与多数类的数量比例（Imbalance Ratio）。
2. 根据此比例计算缩减后的局部邻居窗口 '$。
3. 仅在前 '$ 个最近邻居中执行多数投票。

其内在逻辑在于：如果少数类样本确实出现在局部区域内，由于该区域离少数类很近，在更小的邻居窗口 '$ 范围中，少数类更容易占据多数地位，从而避免被更外围的多数类洪水淹没。
