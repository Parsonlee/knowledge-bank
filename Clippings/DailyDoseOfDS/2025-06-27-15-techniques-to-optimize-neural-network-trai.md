---
title: "优化神经网络训练的 15 种技巧"
source: "https://mail.google.com/mail/u/0/#inbox/197b30868d3ba958"
author:
  - "[[DailyDoseOfDS]]"
published: 2025-06-27
created: 2026-07-30
description: "汇总神经网络训练的 15 项优化建议，涵盖优化器、混合精度、多 GPU、检查点、数据加载等。"
tags:
  - clippings
---

# 优化神经网络训练的 15 种技巧

邮件用一张速览图回顾了 15 种训练优化方法。一些基础做法包括：使用高效优化器（如 AdamW、Adam）；使用 GPU/TPU 等硬件加速器；以及在条件允许时尽可能增大 batch size。

邮件进一步解释了以下方法：

4. **搜索空间很大时使用贝叶斯优化**：根据先前超参数配置的结果作出更有信息量的下一步选择，丢弃非最优配置，从而更快收敛。邮件中的结果图显示，贝叶斯优化（绿色柱）迭代次数和耗时最少，同时找到 F1 分数最佳的配置。
5. **混合精度训练**：在可行处（例如卷积和矩阵乘法）使用较低精度的 `float16`，同时保留 `float32`。
6. **使用 He 或 Xavier 初始化**：通常有助于更快收敛。
7. **使用多 GPU 训练**：可采用模型并行、数据并行、流水线并行或张量并行。
8. **大模型可使用 DeepSpeed、FSDP、YaFSDP 等技术**。
9. **在数据加载中始终使用 `DistributedDataParallel` 而非 `DataParallel`**，即使没有使用分布式训练也是如此。
10. **使用 activation checkpointing 优化内存**：不保存所有中间激活，而是保存其中一部分，并在需要时重算其余部分，可显著降低内存需求；邮件称，内存使用量可降至原内存消耗 `M` 的平方根量级，但会因重算增加运行时间。
11. **对整数数据在传输到 GPU 后再归一化**：以图像像素为例，若在传输前归一化，需要传输 32 位浮点数；若传输后归一化，则传输 8 位整数，所占内存更少。
12. **梯度累积**：在内存约束下通常需使用较小 batch size；梯度累积可在不显式增大 batch size 的情况下，逻辑上增大 batch size。邮件也提示其改善有时可能有限。
13. **直接在 GPU 上创建张量**：`torch.rand(2, 2, device = ...)` 会直接在 GPU 创建张量；`torch.rand(2,2).cuda()` 则先在 CPU 创建、再传输到 GPU，速度较慢。
14–15. **在 `DataLoader` 中设置 `max_workers` 和 `pin_memory`**：训练第一个 mini-batch 时，CPU 可以将第二个 mini-batch 传到 GPU，以减少 GPU 在完成当前 batch 后等待数据的时间。

邮件说明这并非穷尽列表，并邀请读者补充其他技巧。

- [含实现的完整文章](https://www.dailydoseofds.com/15-ways-to-optimize-neural-network-training-with-implementation/)
