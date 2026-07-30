---
title: "Train classical ML models on large datasets."
source: "https://mail.google.com/mail/u/0/#inbox/19dfa25648e2f2cb"
author:
  - "[[DailyDoseOfDS]]"
published: 2026-05-05
created: 2026-07-30
description: "通过随机贴片（Random Patches）算法在无需将全量数据加载入内存的情况下，对超大规模表格数据训练随机森林等经典 ML 模型。"
tags:
  - clippings
---

# 在大数据集上训练传统机器学习模型（Train classical ML models on large datasets.）

在 Scikit-learn 中，支持批次 API（Batch API，如 `partial_fit`）的实现列表非常有限：

![支持 Batch API 的 sklearn 算法列表](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5c4bcebd-86bc-4a50-a537-606480518a85_1080x1080.png)

这非常令人担忧，因为在企业业务场景中，数据形式主要以表格数据（Tabular Data）为主。

经典机器学习算法（如基于树的集成方法 Tree-based Ensemble Methods）频繁被用于建模。

然而，这些模型的典型实现并不“大语言数据友好（Big-data-friendly）”，因为它们要求将整个数据集一次性加载到内存中。

针对这一瓶颈，有两种解决思路：
1. 第一种思路是使用 Spark MLlib 等大数据计算框架来进行模型训练。
2. 第二种思路是使用**随机贴片算法（Random Patches）**。

---

### 随机贴片算法（Random Patches）

*注意：该方法仅适用于集成学习（Ensemble Setting）环境。因此，你需要训练多个子模型。*

其核心思想是抽取随机数据贴片（同时随机采样行和列），并在每个数据贴片（Data Patch）上训练一个决策树模型。

![Random Patches 随机数据贴片采样示意图](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc7040e7e-d523-4936-bab4-c2cb984e3693_1210x801.png)

![Random Patches 训练随机森林图解](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F366c02db-f5e4-4d23-97a7-0842b61b3fbb_2752x939.jpeg)

通过随机生成不同的数据贴片并重复此步骤多次，最终构建出完整的随机森林模型。

在相关学术论文（参见论文第 174 页和 178 页）中，对 13 个经典数据集进行了测试实验：

![不同数据集上的性能测试对比图表](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F91621f82-b337-4b67-809e-628db6db2774_2268x676.jpeg)
*从左至右依次为：Cifar10, mnist3v8, mnist4v9, mnist, isolet, arcene, breast2, madelon, marti, reged, second, this, 以及 sido。*

实验结果表明：
- 在绝大多数场景下，Random Patches 方法的性能优于传统随机森林（Traditional Random Forest）。
- 在其余场景中，两者的性能表现仅存在极微小的边际差异。

这就是我们如何在不将数据全部装入内存的情况下，在大规模数据集上高效训练随机森林模型的方法。

---

### 为什么它能奏效？

该方法的内在机制与 **Bagging（自助采样聚合）** 的方差降低（Variance Reduction）原理如出一辙。

简单来说，当每个基决策树具备高度多样性（Diversity）且相互解耦时，对其预测结果进行平均能够极大程度削减整体模型的方差（Variance），从而在不损失偏差（Bias）的情况下取得极佳的泛化效果。
