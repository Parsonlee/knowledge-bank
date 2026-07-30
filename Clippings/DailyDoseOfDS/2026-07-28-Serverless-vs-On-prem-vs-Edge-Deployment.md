---
title: "无服务器、私有部署与边缘部署：模型部署方式对比"
source: "https://mail.google.com/mail/u/0/#inbox/19faa9c1ec5cf9ba"
author:
  - "[[DailyDoseOfDS]]"
published: 2026-07-28
created: 2026-07-30
description: "对比 Serverless、On-prem 与 Edge 三种模型部署方式的成本、冷启动、隐私和资源利用率，并介绍多模型共享 GPU 的推理服务问题。"
tags:
  - clippings
---

# 无服务器、私有部署与边缘部署：模型部署方式对比（Serverless vs on-prem vs edge deployment）

![原邮件配图](https://embed.filekitcdn.com/e/k7YHPN24SoxyM8nGKZnDxa/4cFcSe3hu3p5r8UdHtC7dZ/email)

Serverless、on-prem 和 edge deployment，是对“模型究竟在哪里运行”这一问题的三种不同回答；每一种都会让你付出不同的代价。

下图展示了这三种方式：

- **Serverless（无服务器）**：你把模型交给服务提供商。只有请求到达时，提供商才会启动机器；请求间隙容器会关闭，因此空闲时无需付费。但权重也会随容器卸载，下一次调用必须将数 GB 的权重重新拉回内存，响应前的等待时间可累积到 90 秒。位于搜索链路中间的 reranker 无法花这么久来唤醒，因此你不得不保持实例预热，最终又回到了为闲置 GPU 付费的状态。
- **On-premise（私有部署）**：你自行租用或拥有 GPU，并让服务器在自己的网络内持续运行。没有数据离开你的基础设施；因为推理引擎已持有权重，也没有冷启动；你支付的是固定小时费率而非按 token 计费。不过，无论是否有流量，显卡都会持续运行。
- **Edge（边缘部署）**：模型通过一个轻量本地运行时，在用户自己的设备、NPU 或 CPU 上运行。模型必须被缩小以适配设备，因此可以离线工作，且任何数据都不会离开硬件；但它通常只能完成一个狭窄任务，而不能承载完整流水线。

真正严肃的团队通常会落到私有部署，而它只有在多个模型共享同一张卡时才划算。

现实中，这很少发生：vLLM 会在启动时预分配 90% 的 GPU，忽略同一 GPU 上的其他 vLLM 实例；而 HuggingFace TEI（Text Embeddings Inference）每个进程只接收一个 `model-id`。两者都不知道彼此的存在。

于是，四个小模型最终跑在四张不同的卡上。你原本改用小模型是为了省钱，现在却要租用四张 GPU 来运行本可装进一张卡的工作负载。

私有部署中，推理服务引擎决定了私有部署到底是真的便宜，还是只是以另一种方式昂贵。

约束并不在显卡本身。缺失的是一个能容纳所有模型、并随流量变化在模型间调度内存的服务器，而不是四台各自确信自己拥有整张 GPU 的服务器。

> [!info] 项目推广
> 邮件将 [Superlinked Inference Engine（SIE）](https://github.com/superlinked/sie)作为针对上述问题的开源项目进行介绍。

[Superlinked Inference Engine（SIE）](https://github.com/superlinked/sie)被设计为填补这一位置：一台服务器处理 embedding、reranking、信息提取与生成；某个请求第一次需要模型时加载它；内存不足时则卸载最久未使用的模型。

- GitHub 仓库：[https://github.com/superlinked/sie](https://github.com/superlinked/sie)
- 邮件还提醒读者不要忘记给项目点星标 🌟。
- [关于 SIE 是什么以及如何开始使用的详细解析](https://www.dailydoseofds.com/p/why-small-models-alone-dont-reduce-inference-costs/)
