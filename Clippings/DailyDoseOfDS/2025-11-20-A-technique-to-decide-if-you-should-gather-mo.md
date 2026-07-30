---
title: "A technique to decide if you should gather more data."
source: "https://mail.google.com/mail/u/0/#inbox/19aa2d674dcfaef6"
author:
  - "[[DailyDoseOfDS]]"
published: 2025-11-20
created: 2026-07-30
description: "基于学习曲线判定是否需要收集更多训练数据的方法与决策指南。"
tags:
  - clippings
---

# 判定是否需要收集更多数据的科学方法（A technique to decide if you should gather more data.）

在机器学习工程实践中，当模型效果未达预期时，“盲目收集更多数据”是许多团队最容易犯的昂贵错误。在投入人力物力采集标注新数据之前，可以通过绘制**学习曲线（Learning Curves）**来判断增加数据量是否真的有效。

![学习曲线趋势对比示意图](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd7f2395e-72a0-4399-95b4-14780bff0371_1324x780.png)

### 如何解读学习曲线？

学习曲线绘制了模型在不同训练集规模下的**训练误差（Training Error）**与**验证误差（Validation Error）**趋势：

1. **曲线 A 情况（数据有效）**：
   * 随着训练样本量的增加，验证误差持续下降，且训练误差与验证误差之间的差距在逐步缩小。
   * **结论**：模型处于高方差（过拟合）状态，**继续收集并投入更多数据将有效提升模型泛化性能**。

2. **曲线 B 情况（数据无效）**：
   * 随着数据集规模增大，验证误差很早便平坦化（Plateau），训练误差居高不下，两者过早收敛并停留在较高误差水平。
   * **结论**：模型处于高偏差（欠拟合）状态，容量（Capacity）已达到上限。**此时盲目采集更多数据毫无意义**，应当转向增加模型复杂度、引入新特征或进行特征工程。
