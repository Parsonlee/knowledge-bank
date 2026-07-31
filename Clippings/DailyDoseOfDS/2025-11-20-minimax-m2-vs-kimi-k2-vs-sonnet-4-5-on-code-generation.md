---
title: "MiniMax-M2 vs. Kimi-K2 vs. Sonnet 4.5 on code generation"
source: "https://mail.google.com/mail/u/0/#inbox/19aa2d674dcfaef6"
author:
  - "[[DailyDoseOfDS]]"
published: 2025-11-20
created: 2026-07-30
description: "基于实测评估开源大模型 MiniMax-M2、Kimi-K2 与 Claude Sonnet 4.5 在代码生成任务上的表现对比。"
tags:
  - clippings
---

# 代码生成评测：MiniMax-M2 vs. Kimi-K2 vs. Sonnet 4.5（MiniMax-M2 vs. Kimi-K2 vs. Sonnet 4.5 on code generation）

在当前的大语言模型演进中，开源/开放权重模型正在以惊人的速度追赶闭源商业模型，并在诸多具体工程场景中展现出同等乃至超越的实力。

![代码生成能力评测对比与排行榜](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_lossy/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F470ae846-8147-44c7-90d7-d1eabd46f6a6_1066x1140.gif)

![Opik 评测得分对比图解](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F38822747-31ee-435c-8b7f-484b8cf6a52b_2820x1500.png)

### 评测细节与测试结果

为了评估各模型在实际代码生成任务上的真实水平，团队使用 CometML 开源的 **Opik** 框架进行了严格基准测试，从**代码正确性（Correctness）**、**可读性（Readability）**及**最佳实践规范（Best Practices）**三大维度展开评估：

* **MiniMax-M2 得分**：
* **Claude Sonnet 4.5 得分**：

（注：得分为百分制转换后的相对标度，得分越高代表综合代码质量越佳）

这一测试结果不仅表明顶级开源模型在专业代码生成任务上已经具备与顶尖商业模型打平甚至实现超越的实力，更意味着企业在部署推理服务时能够显著降低 API 成本开销与自研数据泄露风险。
