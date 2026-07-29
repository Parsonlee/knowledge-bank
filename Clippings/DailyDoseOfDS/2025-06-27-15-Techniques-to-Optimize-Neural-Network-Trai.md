---
title: ​15 Techniques to Optimize Neural Network Training​
source: https://mail.google.com/mail/u/0/#inbox/197b30868d3ba958
author:
  - "[[DailyDoseOfDS]]"
published: 2025-06-27
created: 2026-07-29
description: DailyDoseOfDS 通讯深度解析：包含 ​15 Techniques to Optimize Neural Network Training​ 的原理剖析与工程实践。
tags:
  - clippings
---

# ​15 Techniques to Optimize Neural Network Training​

## 1. 核心要点解析

本期内容重点涵盖：
- **​15 Techniques to Optimize Neural Network Training​**

## 2. 深度拆解与正文翻译

​Industry ML guides (
https://click.convertkit-mail2.com/qdu393wq7es7h46z493ulh870qkkkb4h8po66/owhkhqhwle5d7oiv/aHR0cHM6Ly93d3cuZGFpbHlkb3Nlb2Zkcy5jb20vbWVtYmVyc2hpcC8=
)​

----------------------
In today's newsletter:
----------------------

* The ultimate Python framework for multimodal AI
* ​15 techniques to optimize neural network training​
* Fine-tuning, Transfer, Multitask & Federated Learning,
explained visually.

Reading time: 3 minutes.

TODAY'S ISSUE

multimodal AI
-------------

-----------------------------------------------------------------
​The ultimate Python framework for multimodal AI (
https://click.convertkit-mail2.com/qdu393wq7es7h46z493ulh870qkkkb4h8po66/z2hghnherz0x80cp/aHR0cHM6Ly9naXRodWIuY29tL3BpeGVsdGFibGUvcGl4ZWx0YWJsZQ==
)​
-----------------------------------------------------------------

(
https://click.convertkit-mail2.com/qdu393wq7es7h46z493ulh870qkkkb4h8po66/z2hghnherz0x80cp/aHR0cHM6Ly9naXRodWIuY29tL3BpeGVsdGFibGUvcGl4ZWx0YWJsZQ==
)​
Data pipelines eat 90% of AI development time. They take weeks to
deploy but can break in minutes when requirements change.

And it gets even worse when your data is multimodal.

​Pixeltable (
https://click.convertkit-mail2.com/qdu393wq7es7h46z493ulh870qkkkb4h8po66/z2hghnherz0x80cp/aHR0cHM6Ly9naXRodWIuY29tL3BpeGVsdGFibGUvcGl4ZWx0YWJsZQ==
) is a framework that handles the entire multimodal pipeline
(images, videos, audio, docs & structured data), from data
storage to model execution.

It seamlessly manages images, videos, text, and tabular data—all
in one place.

Fully open-source.

-->​Pixeltable GitHub repo (
https://click.convertkit-mail2.com/qdu393wq7es7h46z493ulh870qkkkb4h8po66/z2hghnherz0x80cp/aHR0cHM6Ly9naXRodWIuY29tL3BpeGVsdGFibGUvcGl4ZWx0YWJsZQ==
)
​Pixeltable GitHub repo (
https://github.com/pixeltable/pixeltable )​GitHub repo → (
https://click.convertkit-mail2.com/qdu393wq7es7h46z493ulh870qkkkb4h8po66/z2hghnherz0x80cp/aHR0cHM6Ly9naXRodWIuY29tL3BpeGVsdGFibGUvcGl4ZWx0YWJsZQ==
) (don’t forget to star)

deep learning
-------------

-----------------------------------------------------------------
​15 techniques to optimize neural network training (
https://click.convertkit-mail2.com/qdu393wq7es7h46z493ulh870qkkkb4h8po66/p8heh9h45e8olriq/aHR0cHM6Ly93d3cuZGFpbHlkb3Nlb2Zkcy5jb20vMTUtd2F5cy10by1vcHRpbWl6ZS1uZXVyYWwtbmV0d29yay10cmFpbmluZy13aXRoLWltcGxlbWVudGF0aW9uLw==
)​
-----------------------------------------------------------------

Here are 15 ways we could recall in 2 minutes to optimize neural
network training:

​
Some of them are pretty basic and obvious, like:

* Use efficient optimizers: AdamW, Adam, etc.
* Utilize hardware accelerators (GPUs/TPUs).
* Max out the batch size.

Here are other methods with more context:

On a side note, we implemented all these techniques here → (
https://click.convertkit-mail2.com/qdu393wq7es7h46z493ulh870qkkkb4h8po66/p8heh9h45e8olriq/aHR0cHM6Ly93d3cuZGFpbHlkb3Nlb2Zkcy5jb20vMTUtd2F5cy10by1vcHRpbWl6ZS1uZXVyYWwtbmV0d29yay10cmFpbmluZy13aXRoLWltcGxlbWVudGF0aW9uLw==
)​
#4) Use Bayesian Optimization if the hyperparameter search space
is big:

* Take informed steps using the results of previous
hyperparameter configs.
* This lets it discard non-optimal configs, and the model
converges faster.
* As shown in the results below, Bayesian optimization (green
bar) takes the least number of iterations, consumes the lowest
time, and still finds the configuration with the best F1 score:

​
#5) Use mixed precision training:

​
* Use lower precision float16 (wherever feasible, like in
convolutions and matrix multiplications) along with float32.
* List of some models trained using mixed precision (indicating
popularity):

​
#6) Use He or Xavier initialization for faster convergence
(usually helps).

#7) Utilize multi-GPU training through Model/Data/Pipeline/Tensor
parallelism.

#8) For large models, use techniques like DeepSpeed, FSDP,
YaFSDP, etc.

#9) Always use DistributedDataParallel, not DataParallel in your
data loaders, even if you are not using distributed training.

#10) Use activation checkpointing to optimize memory (run-time
will go up).

​
* We don’t need to store all the intermediate activations in
memory. Instead, storing a few of them and recomputing the rest
when needed can significantly reduce the memory requirement.
* This can reduce memory usage by a factor of sqrt(M), where M is
the memory consumed without activation checkpointing.
* But due to recomputations, it increases run-time.

#11) Normalize data after transferring to GPU (for integer data,
like pixels):

​
* Consider image data, which has pixels (8-bit integer values).
* Normalizing it before transferring to the GPU would mean we
need to transfer 32-bit floats.
* But normalizing after transfer means 8-bit integers are
transferred, consuming less memory.

#12) Use gradient accumulation (may have marginal improvement at
times).

​
* Under memory constraints, it is always recommended to train the
neural network with a small batch size.
* Despite that, there’s a technique called gradient accumulation,
which lets us (logically) increase batch size without explicitly
increasing the batch size.

#13) torch.rand(2, 2, device = ...) creates a tensor directly on
the GPU. But torch.rand(2,2).cuda() first creates on the CPU,
then transfers to the GPU, which is slow. The speedup is evident
from the image below:

​
#14-15) Set max_workers and pin_memory in DataLoader.

* The typical neural network training procedure is as follows:

​
* As shown above, when the GPU is working, the CPU is idle, and
when the CPU is working, the GPU is idle.
* But here’s what we can do to optimize this:

​
* When the model is being trained on the 1st mini-batch, the CPU
can transfer the 2nd mini-batch to the GPU.
* This ensures that the GPU does not have to wait for the next
mini-batch of data as soon

## 3. 工程落地与实践指南

1. **架构实践**：遵循模块化与低偶合设计原则，保障服务高可用。
2. **性能基准**：结合上下文剪枝与向量重排序技术提升延迟表现。
3. **运维与安全**：持续监控模型采样行为与安全防护。
