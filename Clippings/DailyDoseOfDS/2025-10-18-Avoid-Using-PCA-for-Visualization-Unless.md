---
title: "Avoid Using PCA for Visualization Unless..."
source: "https://mail.google.com/mail/u/0/#inbox/199f91f3eaa6509e"
author:
  - "[[DailyDoseOfDS]]"
published: 2025-10-18
created: 2026-07-30
description: "分析将 PCA 用于高维数据 2D 可视化时的陷阱，并介绍如何通过累计解释方差（CEV）图检验可视化有效性。"
tags:
  - clippings
---

# 除非满足此条件，否则避免使用 PCA 进行可视化（Avoid Using PCA for Visualization Unless...）

主成分分析（PCA）本质上是一种线性**降维技术（Dimensionality Reduction）**。然而在实际工程中，开发者常直接提取 PCA 的前两个主成分（PC1 和 PC2）来生成 2D 散点图以可视化高维数据。这种做法存在巨大的误导隐患。

![PCA 高维数据降维与可视化示意](https://embed.filekitcdn.com/e/k7YHPN24SoxyM8nGKZnDxa/iqc5YCYR8ZZkd5Ck9ypZXs/email)

### PCA 2D 可视化的内在缺陷

在应用 PCA 之后，每一个新特征主成分（PC1, PC2, ..., PC-N）仅捕捉原始数据总方差的一小部分：
- 例如：PC1 解释了 40% 的方差；
- PC2 解释了 25% 的方差。

如果仅取前两个主成分做 2D 可视化，意味着**丢弃了剩下的 35% 的数据方差信息**。只有当前两个主成分能够捕获数据绝大部分方差（如 80%-90%+）时，2D 散点图才能真实反映原始高维空间的结构。而在现实高维数据集中，这种情况极其罕见。

### 检验方案：绘制累计解释方差图（CEV Plot）

在将 PCA 用于可视化之前，必须通过**累计解释方差图（Cumulative Explained Variance Plot, CEV）**进行验证。

![绘制 Cumulative Explained Variance 曲线](https://embed.filekitcdn.com/e/k7YHPN24SoxyM8nGKZnDxa/gsRttUdcyutEe5Qwb36jY5/email)

在 `scikit-learn` 中，可以通过 `pca.explained_variance_ratio_` 计算方差比例：

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

pca = PCA().fit(X)
cum_explained_variance = np.cumsum(pca.explained_variance_ratio_)

plt.plot(cum_explained_variance)
plt.xlabel("Number of Components")
plt.ylabel("Cumulative Explained Variance")
plt.show()
```

#### 判读标准：

1. **误导性曲线（不推荐使用 PCA 可视化）**：前两个主成分累计解释方差极低（如下图）。此时生成的 2D 图严重失真，无法代表高维结构。

![误导性的低累计方差曲线](https://embed.filekitcdn.com/e/k7YHPN24SoxyM8nGKZnDxa/naLCbohgQZTgA4s3iDoYL7/email)

2. **有效曲线（可安全使用 PCA 可视化）**：前两个主成分累计解释方差接近 100%（如下图）。

![高累计方差安全曲线](https://embed.filekitcdn.com/e/k7YHPN24SoxyM8nGKZnDxa/kgAKGCyjKou2mT4cXeEZSb/email)

![降维维度选型与 CEV 关系](https://embed.filekitcdn.com/e/k7YHPN24SoxyM8nGKZnDxa/nCANandQLfKiLjySpHaSNo/email)

对于高维数据的可视化展示，推荐优先使用专为数据可视化设计的非线性降维算法，如 **t-SNE** 或 **UMAP**。
