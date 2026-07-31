---
title: "Introduction to Quantile Regression"
source: "https://mail.google.com/mail/u/0/#inbox/19f962933027e3e6"
author:
  - "[[DailyDoseOfDS]]"
published: 2026-07-24
created: 2026-07-30
description: "深入讲解分位数回归（Quantile Regression）的数学原理与代码实现，分析其如何超越传统均值回归，提供完整的条件分布与不确定性预测。"
tags:
  - clippings
---

# 分位数回归（Quantile Regression）通俗导论（Introduction to Quantile Regression）

普通的最小二乘法回归（OLS）只能给出条件均值（Conditional Mean）的点预测，在遇到异方差数据、偏态分布或极值风险建模时存在显著不足。

**分位数回归（Quantile Regression）** 允许我们预测响应变量在给定输入下的任意分位数（如第 10、第 50 或第 90 分位数），从而提供完整的数据分布预测。

![传统均值回归 vs 分位数回归预测区间对比](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb5f39202-dae5-45cd-b1b1-2f4516939eec_1456x894.png)
*图 1：均值点预测与分位数区间预测示意*

---

### 一、 核心数学原理：Pinball 损失函数

分位数回归通过优化 **Pinball Loss（或称 Check Loss）** 来估计第 $q$ 个分位数 $	au$：

$$\mathcal{L}_{	au}(y, \hat{y}) = \max \left( 	au (y - \hat{y}), (	au - 1)(y - \hat{y}) 
ight)$$

* 当 $	au = 0.5$ 时，Pinball Loss 退化为平均绝对误差（MAE），预测中位数；
* 当 $	au = 0.9$ 时，对高估（Overestimation）惩罚较轻，对低估（Underestimation）施加较重惩罚，从而拟合第 90 分位数。

---

### 二、 从零开始的 Python 实现

使用 PyTorch 实现 Pinball 损失函数并进行分位数回归训练代码如下：

```python
import torch
import torch.nn as nn

class PinballLoss(nn.Module):
    def __init__(self, quantile: float = 0.5):
        super().__init__()
        self.quantile = quantile

    def forward(self, y_pred: torch.Tensor, y_true: torch.Tensor) -> torch.Tensor:
        errors = y_true - y_pred
        loss = torch.max(
            self.quantile * errors,
            (self.quantile - 1.0) * errors
        )
        return torch.mean(loss)

# 实例化第 10、50、90 分位数损失函数
loss_q10 = PinballLoss(quantile=0.10)
loss_q50 = PinballLoss(quantile=0.50)
loss_q90 = PinballLoss(quantile=0.90)
```

分位数回归广泛应用于金融风险评估（Value at Risk）、供应链库存需求上下界预测以及医疗健康预测区间设定中。
