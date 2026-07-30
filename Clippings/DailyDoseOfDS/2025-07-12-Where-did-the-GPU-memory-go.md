---
title: "GPU 显存都去哪了？"
source: "https://mail.google.com/mail/u/0/#inbox/1980063d889e559c"
author:
  - "[[DailyDoseOfDS]]"
published: 2025-07-12
created: 2026-07-30
description: "以 GPT-2 XL 为例拆解训练显存：模型参数、梯度与 Adam 状态约占 24GB，激活值经 checkpointing 后仍需约 8–9GB，另有碎片化等开销。"
tags:
  - clippings
---

# GPU 显存都去哪了？

GPT-2 XL 有 15 亿个参数；其参数以 16 位精度存储时约占 **3GB**。但在单张 32GB GPU 上，训练这样一个“3GB 模型”依然已相当勉强。

![GPT-2 XL 的训练设置](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3da036e0-1aa8-40d0-a886-b39f1ae64c7f_1860x704.png)

设置为：优化器 Adam、batch size 32、48 个 Transformer 层、序列长度 1000。下面计算显存构成。

## 1. 优化器状态、梯度与参数

混合精度训练会同时使用较低精度的 `float16` 和 `float32`。若模型有 $\Phi$ 个参数：

- 权重占用 $2\Phi$ 字节；
- 梯度占用 $2\Phi$ 字节；
- 为有效计算，反向传播结束时的更新以 32 位进行，模型参数还需 $4\Phi$ 字节；
- Adam 为更新保存两个 32 位状态：动量 $4\Phi$ 字节、梯度方差再占 $4\Phi$ 字节。

其中 2 和 4 分别表示每个参数在 16 位与 32 位精度下占用的字节数。合计为 $16\Phi$，对 GPT-2 XL 约为 **24GB**。

![Adam 更新规则示意](https://embed.filekitcdn.com/e/k7YHPN24SoxyM8nGKZnDxa/BNwnDA18MXkAcMr8btFdG/email)

## 2. 激活值

邮件给出 GPT-2 每个 Transformer block 的激活值计算，并将其累加至所有 block。代入 GPT-2 XL 的参数后，约得到 **300 亿个激活值**；每个激活值为 16 位，因此需要约 **60GB** 显存。

![Transformer block 激活值计算](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F89819588-72a5-4ae4-b430-09c7f7b74d20_3222x450.jpeg)

使用[激活检查点](https://www.dailydoseofds.com/15-ways-to-optimize-neural-network-training-with-implementation/)可将激活值显存降至约 **8–9GB**，代价是运行时间增加 **25–30%**。至此总显存消耗已接近 **32–35GB**。

## 3. 其他开销

内存碎片化会在已分配块之间产生未使用的间隙，使得即使总剩余内存足够，也可能无法获得连续块来满足新的分配请求。约 **5–15%** 的显存可能因碎片化而未被有效利用。

## 结论

这说明训练约 3GB 的 GPT-2 模型也几乎需要 **36GB** GPU 显存。模型再增加一层，显存需求就可能额外增加数 GB；多 GPU 训练因此很关键。可进一步阅读[多 GPU 模型训练入门](https://www.dailydoseofds.com/a-beginner-friendly-guide-to-multi-gpu-model-training/)以及[从零实现大规模并行 CUDA 程序](https://www.dailydoseofds.com/implementing-massively-parallelized-cuda-programs-from-scratch-using-cuda-programming/)。
