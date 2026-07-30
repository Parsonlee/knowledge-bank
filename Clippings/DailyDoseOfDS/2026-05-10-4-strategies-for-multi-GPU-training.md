---
title: "4 strategies for multi-GPU training."
source: "https://mail.google.com/mail/u/0/#inbox/19e13d76eb927af3"
author:
  - "[[DailyDoseOfDS]]"
published: 2026-05-10
created: 2026-07-30
description: "深度拆解多 GPU 模型训练的 4 种主流并行策略：模型并行、张量并行、数据并行与流水线并行。"
tags:
  - clippings
---

# 多 GPU 训练的 4 种并行策略（4 strategies for multi-GPU training.）

默认情况下，深度学习框架即使在拥有多个 GPU 的机器上也只会利用单个 GPU 进行训练。

为了加速训练过程，理想的做法是将训练工作负载合理切分并分布到多个 GPU 上。

下图直观展现了多 GPU 训练的四种常见策略：

![多 GPU 训练 4 种策略全景图](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa02acc26-b1bf-48df-93e4-672d790a77ff_1022x1138.gif)

让我们逐一详细剖析这四种策略：

---

### #1) 模型并行（Model parallelism）

在模型并行中，模型的不同网络层被划分并放置在不同的 GPU 上。数据按顺序通过各个 GPU 依次进行前向与反向传播。

![模型并行示意图](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4dce0267-f065-41d0-8d61-2ef1bf297cf9_1554x274.gif)

---

### #2) 张量并行（Tensor parallelism）

张量并行是在单个网络层内部（如大型 Linear 层或 Self-Attention 矩阵）按行或按列拆分权重矩阵，将其分布到多个 GPU 上并行计算。

![张量并行示意图](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F437225d5-c382-4f8e-9ea3-88bb9b0e78b5_1554x274.gif)

各个 GPU 分别完成矩阵乘法切片后，通过 All-Reduce 操作汇总同步结果：

![张量并行通信与矩阵切片细节](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fcfdae765-ee44-49e5-a16b-ff8df6cb4e51_2884x1139.png)

---

### #3) 数据并行（Data parallelism）

在数据并行中，每个 GPU 上都复制一份完整的模型副本。训练 Batch 被均匀切分发送到各个 GPU，每个 GPU 独立计算其 Batch 切片的梯度，最后通过 All-Reduce 同步归约梯度并统一更新权重：

![数据并行示意图](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc9119718-64d0-4bbf-af57-fc44a22757fb_1550x524.gif)

---

### #4) 流水线并行（Pipeline parallelism）

流水线并行结合了模型并行与微批次（Micro-batching）技术。它将网络层切分为不同的阶段（Stages）放置在不同 GPU 上，并将数据切分成微批次在 GPU 间流动，大大减少了传统模型并行中 GPU 的等待空闲时间（Bubble）：

![流水线并行示意图](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc1a8d3db-8e56-4990-8871-9e125fcee3e9_944x348.gif)

👉 互动讨论：在你的实际训练生产中，还使用过哪些其他多 GPU 并行优化策略？
