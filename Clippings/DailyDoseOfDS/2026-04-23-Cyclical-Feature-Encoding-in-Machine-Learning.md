title: 机器学习中的周期性特征编码（Cyclical Feature Encoding） source: https://mail.google.com/mail/u/0/#inbox/19dbca56ab454b95 author:

"[[DailyDoseOfDS]]" published: 2026-04-23 created: 2026-07-28 description: 为什么简单线性数值编码会破坏时间（小时、星期、月份）与风向等周期性特征？详细讲解利用 Sine 和 Cosine 三角函数进行周期特征转换的数学原理。 tags:

clippings

# 机器学习中的周期性特征编码（Cyclical Feature Encoding）

在处理时间（一天中的小时 0-23、星期几 1-7、月份 1-12）、风向（N, NE, E...）、季节等周期特征时，直接使用线性数值（如 0 到 23）会导致严重的信息丢失。

## 线性编码的问题

理想的周期特征表达必须满足：

连续循环：23 点与 0 点在物理时间上只差 1 小时，但数值上相差 23。

等距性：0 到 1 的距离必须与 23 到 0 的距离严格相等。

线性表示显然违背了这两点，会误导基于距离的算法（如 KNN、SVM、神经网络）甚至树模型。

## 三角函数编码（Sine & Cosine）

将周期映射到单位圆（$2\pi$）：

$$x_{\sin} = \sin\left(\frac{2\pi \times \text{value}}{\text{period}}\right)$$ $$x_{\cos} = \cos\left(\frac{2\pi \times \text{value}}{\text{period}}\right)$$

对于小时特征（period = 24）：

23 点转换为 $(\sin(23\pi/12), \cos(23\pi/12))$，在二维平面上与 0 点的 $(\sin(0), \cos(0)) = (0, 1)$ 完美相邻且距离相等。

必须同时保留 Sine 和 Cosine 两个特征，因为单一三角函数会导致两个不同的点拥有相同的函数值。
