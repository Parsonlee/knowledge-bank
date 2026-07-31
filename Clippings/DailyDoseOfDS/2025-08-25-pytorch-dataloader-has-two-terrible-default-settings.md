---
title: "PyTorch Dataloader 有两个糟糕的默认设置（PyTorch Dataloader has two terrible default settings.）"
source: "https://mail.google.com/mail/u/0/#inbox/198e2e9234d8b09f"
author:
  - "[[DailyDoseOfDS]]"
published: 2025-08-25
created: 2026-07-30
description: "讲解如何通过更改 PyTorch DataLoader 的默认设置（使用 pin_memory 和 non_blocking）来重叠 CPU 和 GPU 的计算，从而加速模型训练。"
tags:
  - clippings
---

# PyTorch Dataloader 有两个糟糕的默认设置（PyTorch Dataloader has two terrible default settings.）

考虑下面显示的 PyTorch 模型训练循环：

* 第 5 行将数据从 CPU 传输到 GPU。
* 数据传输后，一切都在 GPU 上执行，即第 7-15 行。

这意味着当 GPU 工作时，CPU 处于空闲状态；而当 CPU 工作时，GPU 处于空闲状态，如下所示：

理想情况下，你可以在 GPU 对批次 1 进行模型训练时，同时传输批次 2。

在 PyTorch 中实现这一点非常简单。

首先，在定义 DataLoader 对象时设置 pin_memory=True 和 num_workers。

接下来，在训练循环的数据传输步骤中，指定 non_blocking=True：

完成！

这是在 MNIST 数据集上的速度比较：

* 在正常设置下，模型在 5 个 epoch 上训练需要 43 秒。

* 但在使用更新的设置后，相同的模型只需 9 秒即可完成训练：

当然，这并不是加速模型训练的唯一技术。

我们在这里介绍了优化模型训练的 15 种技术（包含代码） →
