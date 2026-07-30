---
title: "通过内存锁页加速模型训练"
source: "https://mail.google.com/mail/u/0/#inbox/196ac3a283f20357"
author:
  - "[[DailyDoseOfDS]]"
published: 2025-05-07
created: 2026-07-30
description: "介绍 PyTorch 中利用 pin_memory 和 non_blocking 异步传输 CPU 数据与 GPU 训练重叠的方法，以及其速度收益与内存代价。"
tags:
  - clippings
---

# 通过内存锁页加速模型训练

如果经常用 GPU 加速训练，原文介绍了一种只需改动两处配置即可加速训练的技术：**内存锁页（memory pinning）**。

在常见的 PyTorch 训练流程中，数据先从 CPU 传到 GPU，随后训练在 GPU 上执行。这意味着 GPU 工作时 CPU 可能空闲，而 CPU 工作时 GPU 又可能空闲。

优化的思路是让两者重叠：当模型在第一个 mini-batch 上训练时，CPU 可以把第二个 mini-batch 传到 GPU。这样，GPU 处理完当前 batch 后不必等待下一个 batch；CPU 可能仍会空闲，但实际加速器 GPU 尽量不空闲。

原文将这种做法称为内存锁页：它通过让训练流程中的 CPU 到 GPU 数据传输异步化来加速传输。在 PyTorch 中可按以下两步启用：

1. 定义 `DataLoader` 时设置 `pin_memory=True`，并指定 `num_workers`；
2. 在训练步骤把数据传到 GPU 时设置 `non_blocking=True`。

原文展示的一个简单神经网络示例中，未使用内存锁页时，训练 5 个 epoch 需要 43 秒；使用后，同一模型训练时间少于 10 秒。

## 注意事项

若多个张量被分配到锁页内存，会占用相当一部分 RAM，影响其他操作可用的内存。因此应始终对代码进行性能分析，跟踪内存消耗。若张量较小，CPU 到 GPU 的传输本来耗时不多，内存锁页的效果也会很小。

> 原文还链接了多 GPU 训练指南、15 种神经网络训练优化方法，以及从零开始学习 CUDA 编程的文章。
