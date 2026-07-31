---
title: "[Hands-on] Scale ML models to billions of parameters"
source: "https://mail.google.com/mail/u/0/#inbox/1995434d669b06de"
author:
  - "[[DailyDoseOfDS]]"
published: 2025-09-16
created: 2026-07-30
description: "介绍如何使用 Lightning Fabric 仅需对原生 PyTorch 代码进行 4 处微调，即可轻松扩展模型至百亿参数规模并支持分布式训练。"
tags:
  - clippings
---
# 【实战】将 ML 模型扩展至数十亿参数规模（[Hands-on] Scale ML models to billions of parameters）

PyTorch 提供了极高的灵活性与控制力，但同时也带来了大量的样板代码（Boilerplate Code）。

PyTorch Lightning 能大幅减少样板代码，并允许通过直接指定参数来使用分布式训练功能（如 DDP、FSDP、DeepSpeed、混合精度训练等）。然而在编写手动训练循环时，它的灵活性略逊于纯 PyTorch。

近期，**Lightning Fabric** 结合了 PyTorch 的灵活性与 PyTorch Lightning 的分布式训练能力：

![PyTorch、PyTorch Lightning 与 Lightning Fabric 对比](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fef5b62bb-9ee7-4954-82a2-ae916aaf3090_1456x460.png)

你只需对现有的 PyTorch 代码进行 **4 处微小修改**，即可轻松将其扩展至百亿参数规模的顶级模型/LLM：

![使用 Lightning Fabric 修改代码的 4 个步骤](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4476f20d-f16d-4751-ac12-7aad91e65f50_1456x462.png)

1. **创建并启动 Fabric 对象**：
   在创建 Fabric 对象时，可以指定加速器类型、设备数量、并行策略以及浮点精度等。

2. **配置模型、优化器和数据加载器**：
   让 Fabric 完成这些训练组件的配置。

3. **移除所有 `.to()` 和 `.cuda()` 调用**：
   Fabric 会自动处理设备分配与数据迁移。

4. **替换反向传播**：
   将 `loss.backward()` 替换为 `fabric.backward(loss)`。

![Lightning Fabric 代码修改细节示意图](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F78cc2226-f90b-4213-ac61-16f00799a1ec_1456x521.png)

通过这 4 个简单步骤，你可以：
* 轻松在 CPU、GPU（Apple Silicon、CUDA 等）、TPU、多 GPU 或多节点训练之间切换。
* 开箱即用使用最先进的分布式训练策略（DDP、FSDP、DeepSpeed）及混合精度。

此外，也可以借助 Fabric 构建自定义 Trainer，用于训练检查点、日志记录等功能。参见 [Lightning Fabric 文档](https://lightning.ai/docs/fabric/stable/)。
