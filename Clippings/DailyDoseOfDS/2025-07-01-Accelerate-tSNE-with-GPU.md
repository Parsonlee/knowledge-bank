---
title: "用 GPU 加速 t-SNE"
source: "https://mail.google.com/mail/u/0/#inbox/197c7ace7fc9ab0e"
author:
  - "[[DailyDoseOfDS]]"
published: 2025-07-01
created: 2026-07-30
description: "t-SNE 的运行时间与数据点数量呈二次关系；tSNE-CUDA 是其 CUDA 优化实现，邮件称其相对 sklearn 可快 33 倍，在 CIFAR-10 训练集上可快 700 倍。"
tags:
  - clippings
---

# 用 GPU 加速 t-SNE

t-SNE 的运行时间与数据点数量呈二次关系。因此，在 sklearn 实现中，数据超过 **4 万个点** 时，t-SNE 会变得难以使用。

`tSNE-CUDA` 是 t-SNE 算法的 CUDA 优化版本，能相较标准 sklearn 实现带来显著加速；邮件图示称 GPU 加速实现快 **33 倍**。

![tSNE-CUDA 与 sklearn 的速度对比](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fcfd54fc7-3bcd-425e-b94c-41ff70069116_2184x908.png)

该实现仅支持 `n_components=2`，即只能投影到二维。作者无意支持更多维度，因为这会要求对代码作重大改动；邮件作者认为这影响不大，因为 t-SNE 在 **99%** 的使用场景中就是用于生成二维投影。

作者的基准测试显示，在 CIFAR-10 训练集（5 万张图像）上，`tSNE-CUDA` 比 sklearn 快 **700 倍**。

![tSNE-CUDA 基准测试结果](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F27a8b2e7-23cd-4454-b1bf-1f9b62033c4f_3280x1532.png)

延伸阅读：

- [用 GPU 加速其他机器学习算法](https://www.dailydoseofds.com/sklearn-models-are-not-deployment-friendly-supercharge-them-with-gpus-first/)；
- [从零推导并实现 t-SNE 算法](https://www.dailydoseofds.com/formulating-and-implementing-the-t-sne-algorithm-from-scratch/)。
