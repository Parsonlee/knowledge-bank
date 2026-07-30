---
title: "PyTorch DataLoader 有两个糟糕的默认设置"
source: "https://mail.google.com/mail/u/0/#inbox/19664020d007efe2"
author:
  - "[[DailyDoseOfDS]]"
published: 2025-04-23
created: 2026-07-30
description: "通过启用 pin_memory、配置 num_workers，并在传输时使用 non_blocking，减少 CPU 与 GPU 互相等待。"
tags:
  - clippings
---

# PyTorch DataLoader 有两个糟糕的默认设置

在所示的 PyTorch 训练循环中，第 5 行把数据从 CPU 传输到 GPU，之后第 7–15 行都在 GPU 上执行。这意味着 GPU 工作时 CPU 空闲，CPU 工作时 GPU 空闲。

理想情况是：GPU 用批次 1 训练模型时，CPU 同时传输批次 2。邮件给出的做法是：

1. 定义 `DataLoader` 时设置 `pin_memory=True`，并配置 `num_workers`。
2. 在训练循环的数据传输步骤中指定 `non_blocking=True`。

这样可以让数据传输与 GPU 训练重叠执行。

在 MNIST 上的对比中，普通设置训练 5 个 epoch 需要 43 秒；更新设置后，同一模型需要 9 秒。

这并不是加速模型训练的唯一方法。邮件还链接到一篇包含实现的[神经网络训练优化 15 种方法](https://www.dailydoseofds.com/15-ways-to-optimize-neural-network-training-with-implementation/)。
