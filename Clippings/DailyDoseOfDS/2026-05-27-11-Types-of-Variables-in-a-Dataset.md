---
title: "11 types of variables in a dataset."
source: "https://mail.google.com/mail/u/0/#inbox/19e6b1b1a122a14a"
author:
  - "[[DailyDoseOfDS]]"
published: 2026-05-27
created: 2026-07-30
description: "全面解析表格数据集中常见的 11 种变量类型，包括自变量/因变量、混淆变量、控制变量、潜在变量、交互变量、平稳/非平稳变量、滞后变量与目标泄漏变量。"
tags:
  - clippings
---

# 数据集中的 11 种变量类型（11 types of variables in a dataset.）

在任何表格数据集（Tabular Dataset）中，我们通常习惯将各列简单归类为**特征（Feature）**或**目标（Target）**。

然而在实际的数据科学与机器学习工程中，我们可以发现并定义出更丰富细致的变量类型，如下图所示：

![数据集中的 11 种变量类型概览](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F030349a9-a413-40d7-a304-36f154c93ec4_1724x676.png)

今天就让我们来全面梳理与理解这 11 种变量类型！

---

### #1-2) 自变量与因变量（Independent and Dependent variables）

- **自变量（Independent variables）**：作为模型输入以预测结果的特征。它们也被称为预测变量（Predictors）、特征（Features）或解释变量（Explanatory variables）。
- **因变量（Dependent variable）**：被预测的目标结果。它也被称为目标变量（Target）、响应变量（Response）或输出变量（Output variable）。

![自变量与因变量示意图](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd1782c63-bd12-4dc3-a78f-29043378288b_1720x696.png)

---

### #3-4) 混淆变量与相关变量（Confounding and Correlated variables）

**混淆变量（Confounding variables）**通常出现在因果推断（Causal Inference）的研究中。

它们往往不是我们主要关注的变量，但如果处理不当，会导致极其诡异的伪关联（Spurious Associations）。

假设我们想测量“冰淇淋销量”对“空调销量”的影响，这两者在统计数据上高度正相关：

![冰淇淋销量与空调销量的强相关性](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F49e31e3c-d9e9-484a-be90-a20646b289dd_1664x688.png)

然而，这里存在一个**混淆变量——气温（Temperature）**，它同时影响着冰淇淋销量与空调销量：

![气温作为混淆变量影响两者](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F9da17703-973f-4987-b451-92a6e76ed65c_1904x676.png)

要研究真正的因果效应，就必须对混淆因素（气温）进行控制或调整。否则，分析结果将会产生严重的误导。正是由于混淆变量的存在，数据科学中才常说：**“相关性并不意味着因果关系（Correlation does not imply causation）。”**

---

### #5) 控制变量（Control variables）

在前述例子中，我们必须确保气温得到控制（Keep Controlled），从而能够准确测量冰淇淋销量对空调销量的真实影响：

![控制变量示意图](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fee226325-30cb-48ae-84b5-00abe1e9af41_1996x676.png)

一旦被控制，气温就变成了**控制变量**。控制变量虽然不是研究的核心重点，但考虑它们至关重要，这能保证我们要测量的效应不会受到其他潜在因素的偏差干扰或混淆。

---

### #6) 潜在变量（Latent variables）

**潜在变量（Latent variables）**是指无法直接观测到、但可以通过其他可观测变量推断出来的变量。

例如在聚类分析（Clustering）中，数据并没有真实的显式标签——这个隐含的类别就是潜在变量。

![潜在变量示意图](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe6dd05f0-e18f-4cd3-a54a-09a23fabb19f_1700x700.png)

在从零实现高斯混合模型（GMM）等算法时，潜在变量也发挥着核心作用。

---

### #7) 交互变量（Interaction variables）

交互变量用于测量两个或多个变量之间的**交互效应（Interaction effect）**，常用于回归分析中。

例如，假设有两个分类变量：
- 人口密度（Population density）→ 高、中、低（独热编码 One-hot encoded）。
- 收入水平（Income levels）→ 高、中、低（独热编码 One-hot encoded）。

![交互变量构造示意图](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F030349a9-a413-40d7-a304-36f154c93ec4_1724x676.png)

将它们相乘可以产生 9 个交互变量。研究这些交互变量往往能带来更深入的业务洞察。

---

### #8-9) 平稳与非平稳变量（Stationary and Non-Stationary variables）

- **平稳变量（Stationary variables）**：其统计属性（如均值、方差）**不会随着时间发生改变**的变量。
- **非平稳变量（Non-Stationary variables）**：统计属性随时间发生变化的变量。

![平稳与非平稳变量示意图](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4cacb56f-4600-4b70-9db4-87a8397b4401_2012x800.png)

在统计学习中保持平稳性至关重要，因为大多数模型都假设样本是独立同分布（i.i.d.）的。这就是为什么不建议直接使用非平稳特征的原始值（如股票绝对价格），而是建议将其定义为相对变化率（Relative changes）。

---

### #10) 滞后变量（Lagged variables）

**滞后变量（Lagged variable）**代表给定变量在先前时间点的值：

![滞后变量示意图](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F443c07c5-da56-4caa-9818-410d989313a4_1852x676.png)

例如，在预测下个月的销售额时，我们可以将上个月的销售额作为滞后变量引入。

常见滞后特征包括：
- 网站流量的 7 天滞后项，用于预测当前流量。
- 股票价格的 30 天滞后项，用于预测下个月的收盘价。

---

### #11) 目标泄漏变量（Leaky variables）

**泄漏变量（Leaky variables）**提供了在真实预测阶段**无法获取的未来或目标信息**。

这会导致模型在训练期间表现出过于乐观的超高性能，但在新数据上泛化能力极差。

例如，创建向前看（Forward-lag）的未来的滞后特征就会直接引入泄漏变量：

![目标泄漏变量示意图](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe0d3a730-ede6-416f-83e4-5b33d45f4ffe_1852x676.png)

思考一下：你在日常业务中还遇到过哪些其他变量类型？
