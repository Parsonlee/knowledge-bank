---
title: "The ideal loss function to handle class imbalance."
source: "https://mail.google.com/mail/u/0/#inbox/19d11dddb3bc89bd"
author:
  - "[[DailyDoseOfDS]]"
published: 2026-03-21
created: 2026-07-30
description: "详细推导与对比二分类交叉熵（BCE）与 Focal Loss 损失函数，解析 Focal Loss 如何通过调制因子与逆类频率权重解决极度类别不平衡问题。"
tags:
  - clippings
---

# 解决类别不平衡的理想损失函数（The ideal loss function to handle class imbalance.）

在机器学习与深度学习分类任务中，二分类交叉熵（Binary Cross-Entropy, BCE）是默认的标准损失函数。然而，当面临严重类别不平衡（Class Imbalance，例如 99:1 或 90:10）的场景时，BCE 损失函数的缺陷便暴露无遗。

本文将深度拆解为何 BCE 会在极端不平衡数据下失效，以及 **Focal Loss** 如何成为解决此类问题的理想损失函数。

---

### 一、 BCE 损失函数的局限性

标准的二分类交叉熵损失定义如下：

$$	ext{BCE}(p, y) = -y \log(p) - (1-y) \log(1-p)$$

为了推导上的简洁性，我们定义 $p_t$ 如下：

$$p_t = egin{cases} p & 	ext{若 } y=1 \ 1-p & 	ext{若 } y=0 \end{cases}$$

于是，交叉熵损失可以简化重写为：

$$	ext{CE}(p_t) = -\log(p_t)$$

BCE 的核心局限在于：**它对所有样本一视同仁。** 即使模型对简单样本（Easy Examples，如 $p_t = 0.9$）已经非常自信，这些样本产生的微小损失叠加起来，依然会在数量庞大的主导类中主导梯度更新，导致模型忽视稀有的困难样本（Hard Examples）。

---

### 二、 Focal Loss 的数学机制

为了解决这个问题，Focal Loss 引入了一个动态调制因子（Modulating Factor） $(1 - p_t)^\gamma$：

$$	ext{FL}(p_t) = -(1 - p_t)^\gamma \log(p_t)$$

其中 $\gamma \ge 0$ 为可调超参数（Focusing Parameter）。

![BCE 损失与不同 Gamma 取值下 Focal Loss 的曲线对比](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa98da6f2-4c1f-49af-84c9-02459e342e97_2360x944.png)
*图 1：BCE 损失与不同 Gamma 取值下 Focal Loss 的曲线对比*

![Gamma 增加对高置信度样本损失衰减的抑制效果](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa3ead0b3-4f62-4ad5-9f1f-5480548ca414_420x116.png)
*图 2：Gamma 增加对高置信度样本损失衰减的抑制效果*

从曲线上可以清晰看出：
- 当 $p_t 	o 1$（模型对预测高度自信的简单样本）时，$(1 - p_t)^\gamma 	o 0$，该样本对总损失的贡献被极大地抑制。
- 当 $p_t$ 较小（困难样本）时，调制因子接近 1，损失几乎不受影响。

![Focal Loss 在对称分类下的数学形式](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F78592f1a-d050-4083-b960-e30e761918ad_2728x676.png)
*图 3：Focal Loss 在对称分类下的数学形式*

进一步地，为了同时平衡正负样本的类频率不均衡，引入平衡因子 $lpha_t$（通常设为类频率的倒数）：

![结合 Alpha 平衡因子后的完整 Focal Loss 公式](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F11ec5bda-003f-4791-a408-a0a60bcd32c5_2392x1184.png)
*图 4：结合 Alpha 平衡因子后的完整 Focal Loss 公式*

完整公式如下：

$$	ext{FL}(p_t) = -lpha_t (1 - p_t)^\gamma \log(p_t)$$

![结合降权因子与逆类频率加权的最终损失表达式](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F30427305-e2e0-4983-9649-319dfea0c32d_2376x1328.png)
*图 5：结合降权因子与逆类频率加权的最终损失表达式*

---

### 三、 90:10 不平衡数据集上的实证对比

在 90:10 的极端不平衡数据集上，分别使用 BCE 损失与 Focal Loss 训练神经网络，结果对比显著：

![BCE 损失在不平衡数据集上的决策边界与预测偏置](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6336706d-201f-44a7-a042-9d137e16344d_2320x1256.png)
*图 6：BCE 损失在不平衡数据集上的决策边界与预测偏置*

![Focal Loss 在不平衡数据集上的决策边界与预测结果](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F30495e42-1f54-4227-a42b-b1cead75c1d5_2632x952.png)
*图 7：Focal Loss 在不平衡数据集上的决策边界与预测结果*

![BCE vs Focal Loss 训练神经网络决策区域对比图](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F36dbaeb9-5757-4a25-ad3a-7bee1da31219_2856x676.png)
*图 8：BCE vs Focal Loss 训练神经网络决策区域对比图*

![BCE 模型偏向多数类 vs Focal Loss 聚焦少数类的效果对比](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7f8c159c-2a1d-4b8d-be26-eb6d275f5a3d_2416x1152.png)
*图 9：BCE 模型偏向多数类 vs Focal Loss 聚焦少数类的效果对比*

![针对类别不平衡的拓展 ML 模型增强技术索引](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4a0ad295-b095-429d-b147-92340340490f_1424x752.png)
*图 10：针对类别不平衡的拓展 ML 模型增强技术索引*

- **BCE 模型**（左）：由于绝大多数样本都是多数类，模型完全倾向于预测多数类，牺牲了少数类的召回率。
- **Focal Loss 模型**（右）：动态抑制了简单多数类的梯度，迫使模型关注少数类的特征形态，获得了更高的 F1-score 与整体拟合质量。
