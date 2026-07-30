---
title: "An intuitive guide to non-linearity of ReLU."
source: "https://mail.google.com/mail/u/0/#inbox/19ea91777352c092"
author:
  - "[[DailyDoseOfDS]]"
published: 2026-06-08
created: 2026-07-30
description: "直观图解 ReLU 激活函数的非线性特性：拆解神经元输出、拼接分段线性函数以及拟合任意非线性曲线的数学原理。"
tags:
  - clippings
---

# 直观理解 ReLU 激活函数的非线性（An intuitive guide to non-linearity of ReLU.）

ReLU（Rectified Linear Unit，修正线性单元）的定义非常简单：
$$\text{ReLU}(z) = \max(0, z)$$

从表面上看，它对于 $z > 0$ 只是一个简单的线性映射 $y=z$，而对于 $z \le 0$ 则直接截断为 $0$。那么，为什么这种极其简单的“分段线性”函数，能够赋予神经网络表达极其复杂的复杂非线性关系的能力？

![ReLU 几何图示 1](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F8abbe940-eb44-42f0-8509-ceb5e581522e_522x82.png)

![ReLU 拟合复杂非线性函数动图](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3de8b850-a1bf-44ae-b089-392c4e567c42_1704x988.gif)

![ReLU 数学公式表达](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F51fd87ae-5184-4335-9234-b9f5089c2670_641x122.png)

---

### 神经元输出的解构（Breaking down a neuron’s output）

在一个神经网络层中，单个神经元的计算可以拆解为四个步骤：

![单个神经元输出拆解](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0fa9de50-4dfa-43a9-9806-f87c9a519746_1000x488.png)

1. **接收输入**：来自前一层的输入向量 $(x_1, x_2, \dots, x_n)$；
2. **权重加权**：与对应的权重参数 $(w_1, w_2, \dots, w_n)$ 进行逐元素相乘；
3. **叠加偏置**：加入偏置项 $b$（每个神经元拥有独立的偏置参数）；
4. **ReLU 激活**：将生成的 $z = \mathbf{w}^T \mathbf{x} + b$ 传入 $\text{ReLU}(z)$ 得到神经元最终的输出激活值。

![线性组合与偏置加权](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fffb448d8-0027-47bb-be66-cede15deec50_1000x346.png)

![ReLU 截断零点变化](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd6f0e22a-8434-49c1-b5ab-9283a2bad9bc_1000x391.png)

![不同偏置下的 ReLU 偏移](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa323bb08-0368-49d7-bb19-59d2b73633e4_579x290.png)

---

### 绘制 Dummy ReLU 单元（Plotting dummy ReLU units）

由于单元素 ReLU 在 $z=0$ 处引入了一个“拐折点”，当多个包含不同权重 $w_i$ 与偏置 $b_i$ 的神经元在后续网络层进行加权组合时：

![绘制 Dummy ReLU 单元曲线](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F141beb46-2264-41ba-b178-8a1b14acdbfc_1020x500.png)

![多单元分段拼接](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F8ce4378b-7574-4443-8371-c7462c3c5aa7_888x395.png)

![折线叠加拟合非线性](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fbdb31bf3-dbe5-4701-9981-fdeefaa75165_1020x527.png)

![加权求和后的复杂折线](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F1f80a189-6cd7-407c-a83f-adf1463dca80_731x249.png)

每个神经元负责在特定输入区间内产生一个转折。将成百上千个这样在不同位置转折的分段直线叠加在一起，就能拼出一个高度复杂的**分段线性决策边界（Piecewise Linear Function）**。

---

### $y = x^2$ 拟合实验（X-squared Demo）

我们可以直观地看到：使用几个简单的 ReLU 神经元，就能以分段折线的方式高精度拟合平滑的抛物线 $y = x^2$：

![拟合二次函数 y = x^2 效果图 1](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe728d665-103c-4dcb-a27d-db4c752fb570_1000x447.png)

![拟合二次函数 y = x^2 效果图 2](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc57784a9-d4e7-489c-aafd-4cb67e041bae_1000x505.png)

![拟合二次函数 y = x^2 效果图 3](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fefcd20fb-ea9a-4d6a-a5ce-761a41d208f1_1000x505.png)

![拟合二次函数 y = x^2 效果图 4](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F36c5cfb7-8465-415c-bf64-fc46bc2c9895_1456x1229.png)

![拟合二次函数 y = x^2 效果图 5](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F9bff9550-28cd-468d-8cd8-5864d9dfcd3f_1456x548.png)

当网络中的神经元数量无限增加时，分段直线的微元段无限缩小，从而能够以任意精度逼近任何连续的非线性函数。这正是通用近似定理（Universal Approximation Theorem）的数学精髓。
