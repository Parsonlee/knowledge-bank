---
title: "Cyclical feature encoding in machine learning"
source: "https://mail.google.com/mail/u/0/#inbox/19dbca56ab454b95"
author:
  - "[[DailyDoseOfDS]]"
published: 2026-04-23
created: 2026-07-30
description: "探讨机器学习中周期性特征（如一天中的小时、星期、季节、风向）的传统线性编码局限，并详解基于正弦与余弦三角函数映射的周期编码原理与应用场景。"
tags:
  - clippings
---
# 机器学习中的周期性特征编码（Cyclical feature encoding in machine learning）

在典型的机器学习数据集中，特征通常分为：
- **数值型特征（Numerical Features）**：如年龄、收入、交易金额等。
- **类别型特征（Categorical Features）**：如 T 恤尺码、收入等级、年龄段等。

然而，还存在一类非常特殊的特征——**周期性特征（Cyclical Features）**。

例如一天中的“小时”（0 点到 23 点）。一个理想的特征转换系统需要满足以下两个关键属性：
1. **首尾相邻性**：“23 点”与下一个周期“0 点”在物理时间上是紧密相邻的。
2. **距离一致性**：“0 点”到“1 点”的距离，必须与“23 点”到“0 点”的距离完全一致。

### 传统线性编码的局限

然而，标准的线性数值表示法（0, 1, 2, ..., 23）无法满足上述任何一个属性：
- 在数值大小上，23 与 0 相距甚远（差值为 23）。
- 距离一致性也被打破。

### 三角函数周期编码原理

编码此类特征最常用的高效技巧之一是使用三角函数，具体来说即**正弦（Sine）与余弦（Cosine）**函数。

三角函数天然具有周期性、有界性，且对所有实数均有定义。

以将“一天中的小时”（0-23）映射为周期特征为例，中心角（$2\pi$ 弧度）代表完整的 24 小时：

$$x_{\sin} = \sin\left(rac{2\pi \cdot 	ext{hour}}{24}ight)$$

$$x_{\cos} = \cos\left(rac{2\pi \cdot 	ext{hour}}{24}ight)$$

通过正弦和余弦的双维度联合编码，特征被均匀分布在一个二维单位圆周上：

![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6d438665-cb86-407b-8141-cfa2263928af_1200x928.png)

如图所示，经过三角编码后：
- “23 点”与“0 点”在二维空间中的欧氏距离与“0 点”到“1 点”的距离完全相同。
- 两个数学属性被完美满足。

如果特征是“星期几”（Day of the Week），则只需将中心角 $2\pi$ 替换对应 7 天进行缩放即可。

### 广泛的应用场景

相同的周期特征编码思想可以扩展到数据集中常见的各类周期性维度：
- **风向（Wind Direction）**：N（北）、NE（东北）、E（东）、SE（东南）、S（南）、SW（西南）、W（西）、NW（西北），随后循环回到 N。
- **月相（Phases of the Moon）**：新月、上弦月、满月、下弦月，构成周期性类别。
- **季节（Seasons）**：春、夏、秋、冬，具有按年重复的周期模式。

通过这种特征工程处理，机器学习模型能够以符合自然规律的方式更容易地捕捉和利用周期模式。
