---
title: "7 categorical data encoding techniques"
source: "https://mail.google.com/mail/u/0/#inbox/19ae0c67c504face"
author:
  - "[[DailyDoseOfDS]]"
published: 2025-12-02
created: 2026-07-30
description: "详细拆解机器学习中常见的 7 种类别数据编码技术及其适用场景与维度对比。"
tags:
  - clippings
---

# 7 种类别数据编码技术（7 categorical data encoding techniques）

在机器学习模型中，处理类别特征（Categorical Features）是数据预处理的关键环节。本文总结了 7 种最常用的类别数据编码技术：

![7 种类别特征编码技术图解](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F06ca2110-d4af-4327-a2c5-a224efe77323_1174x1126.gif)

### 1. 独热编码（One-hot encoding）
* 每个类别用一个由 0 和 1 组成的二元向量表示。
* 每个类别对应一个独立的二元特征，同一时间有且仅有一个特征为“Hot”（置为 1）。
* 生成的特征数量 = 唯一类别标签的数量。

### 2. 哑变量编码（Dummy encoding）
* 与独热编码原理基本一致，但在编码后随机丢弃其中一个二元特征。
* 这样做的目的是为了消除多重共线性，避免陷入“哑变量陷阱”（Dummy variable trap）。
* 生成的特征数量 = 唯一类别标签数量 - 1。

### 3. 效果编码（Effect encoding）
* 与哑变量编码类似，但多了一步处理：将全为 0 的那一行修改为全 -1。
* 这样可以确保生成的二元特征不仅能表达特定类别的存在与否，还能刻画基准类别与无类别之间的对比效果。
* 生成的特征数量 = 唯一类别标签数量 - 1。

### 4. 标签编码（Label encoding）
* 为每个类别指派一个唯一的整数标签。
* 标签编码会在类别间引入隐式的顺序关系（例如 0 < 1 < 2），这在无序类别数据中可能引发非预期的模型偏置。
* 生成的特征数量 = 1。

### 5. 序号编码（Ordinal encoding）
* 与标签编码类似，为每个类别指派一个唯一的整数值。
* 不同之处在于，指派的数值具有明确且有意义的先后顺序（如：低=0、中=1、高=2）。
* 生成的特征数量 = 1。

### 6. 计数编码（Count encoding / Frequency encoding）
* 也称为频率编码。
* 根据每个类别在数据集中出现的频次/计数进行编码。
* 直接将类别替换为其对应的出现次数，而不是替换成抽象数值或二元向量。
* 生成的特征数量 = 1。

### 7. 二进制编码（Binary encoding）
* 结合了序号编码与独热编码的优势。
* 首先将类别转换为序号整数，然后再将该整数转换为二进制代码。
* 最后将二进制代码的每一位拆分为独立的二元特征。
* 非常适合处理高基数（High-cardinality）类别特征，相比独热编码能够极大地降低特征维度（从 $ 维降低至 $\log_2(N)$ 维）。
* 生成的特征数量 = $\log_2(N)$。

在实际工程中，你可以使用开源 Python 库  来轻松试用上述及更多高级编码技术。
