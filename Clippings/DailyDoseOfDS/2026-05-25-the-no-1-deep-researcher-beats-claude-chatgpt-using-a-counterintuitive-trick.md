---
title: "The No. 1 deep researcher beats Claude/ChatGPT using a counterintuitive trick."
source: "https://mail.google.com/mail/u/0/#inbox/19e60c170373504b"
author:
  - "[[DailyDoseOfDS]]"
published: 2026-05-25
created: 2026-07-30
description: "深度拆解在 DeepResearch Bench 上排名第一的开源深度研究 Agent 架构，剖析为什么剥离协调者 Agent 的搜索工具权限能大幅提升研究质量。"
tags:
  - clippings
---

# 排名第一的深度研究 Agent 击败 Claude 和 ChatGPT 的反直觉秘诀（The No. 1 deep researcher beats Claude/ChatGPT using a counterintuitive trick.）

在 DeepResearch Bench 上排名第一的深度研究（Deep Research）系统使用了一个 Claude 和 ChatGPT 都没有采用的技巧。

我们深入分析了其背后的开源架构。

令人吃惊且非常反直觉的一点是：**负责运行整个研究策略的协调者 Agent（Orchestrator Agent），竟然完全没有搜索工具权限！**

它无法查询网页，也无法打开任何 URL。

![协调者 Agent 剥离搜索权限](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F1b7ff836-7e3d-43a1-a119-65f4173b3a47_1152x780.jpeg)

乍一看这似乎是完全错误的逻辑。因为几乎所有其他的深度研究系统，都会赋予其协调者 Agent 丰富而强大的能力。

然而：
↳ 研发该系统的研究团队（Onyx 团队）观察到，如果赋予协调者搜索能力，会导致模型将大量的上下文和计算周期浪费在低质量的检索上。

绝大多数 Orchestrator 在拥有搜索和检索工具的同时，还拥有分发（Dispatch）任务的能力。一旦 Orchestrator 拥有了搜索能力：

![常规 Orchestrator 容易陷入自行搜索与生成浅层报告的陷阱](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ffbebf198-13d0-4790-a867-49a98829de5e_1579x798.png)

它往往不再去仔细拆解复杂问题，而是开始亲自回答问题。它抓取几个初步结果，跳过深入的任务解构，直接根据最先找到的内容生成一份浮于表面的报告。

**剥离 Orchestrator 的搜索权限，能强迫它专注撰写自我完备、逻辑严密的任务简报（Task Briefs），并分发给底层的研究 Agent。**

此外，研究人员还将系统架构严格限定在**两层深度（Two levels deep）**。因为当信息在多级 Agent 之间层层传递时，每一层传递都会带来不可避免的微小扭曲与信息衰减。

这两个关键限制嵌入在一个更大的三阶段管线中（如下图所示）：

![Onyx 三阶段深度研究管线架构](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0965ce02-193a-4ec2-bb7c-ff2c2ab85b23_1210x1160.jpeg)

目前这一模式在 DeepResearch Bench 上高居榜首。完整代码已在 GitHub 上开源（Onyx 仓库）。

👉 互动讨论：你目前首选的深度研究（Deep Researcher）工具是哪一个？
