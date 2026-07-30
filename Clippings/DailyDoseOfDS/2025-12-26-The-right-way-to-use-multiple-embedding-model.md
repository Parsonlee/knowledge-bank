---
title: "The right way to use multiple embedding models"
source: "https://mail.google.com/mail/u/0/#inbox/19b5c7637722a2ba"
author:
  - "[[DailyDoseOfDS]]"
published: 2025-12-26
created: 2026-07-30
description: "阐明为什么不能直接对不同嵌入模型生成的同维向量进行距离计算或相似度比对，并介绍拼接（Concatenation）等正确的组合表达范式。"
tags:
  - clippings
---

# 组合使用多个嵌入模型的正确姿势（The right way to use multiple embedding models）

假设在你的整个机器学习流水线中有两个不同的模型（或子网络）。两者都将输入数据转换为相同维度（例如 200 维）的向量表示/嵌入（Embedding）。

![两个网络生成相同维度的嵌入](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F036bba45-0180-4d7f-917b-82c8d1b15800_1192x1393.gif)

这些可能用于生成嵌入的预训练模型（如 BERT、XLNet 等），或者任何嵌入网络。

在这里，许多人会很自然地尝试让它们直接相互作用，例如：
* 比较这些向量表示
* 计算它们的欧氏距离（Euclidean distance）
* 计算它们的余弦相似度（Cosine similarity）等

其背后的理由是：既然这些嵌入具有相同的维度，它们就可以无缝地相互计算。

然而，**这种假设是完全错误的，你绝不应该这样做**。

---

### 为什么不能直接比较？

这是因为尽管这些嵌入具有相同的长度（或维度），但它们**并不在同一个向量空间内**（out of space）。

不在同一个空间内意味着它们的坐标轴没有对齐。

为了简化理解，假设两种嵌入都在 3 维空间中：

![坐标轴不一致示意图](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Face496b0-36ba-438d-a118-4463604f9d06_2343x1008.png)

假设它们的 Z 轴是对齐的，但第一个模型的 X 轴和 Y 轴与第二个模型的 X 轴和 Y 轴之间存在一定的夹角。

当然，两个嵌入都具有相同的维度：3 维。但你能直接对它们进行比较计算吗？

不能。

同样地，直接比较上述两个不同网络生成的嵌入，本质上隐含假设了所有坐标轴都是完美对齐的。由于坐标轴在空间中有无限种旋转朝向的可能性，这种假设在现实中极不可能成立。

因此，除非向量是由同一个网络生成，或者是通过显式对齐训练的不同网络生成的，否则这些向量表示**绝对无法直接比较**。

---

### 正确的解决方法：拼接（Concatenation）

相反，向量拼接（Concatenation）是利用多种嵌入更好的方式：

![嵌入向量拼接示意图](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F1fa6ed52-ba08-40f8-9776-04b57c791dbb_2405x760.png)

拼接的一大优势在于，即使两个嵌入模型的向量维度不一致，它也能完美工作。
