---
title: "大语言模型技术面试题：如何筛选值得复盘的 Agent 轨迹"
source: "https://mail.google.com/mail/u/0/#inbox/19faa9c1ec5cf9ba"
author:
  - "[[DailyDoseOfDS]]"
published: 2026-07-28
created: 2026-07-30
description: "在禁止使用 LLM 评估的条件下，介绍用确定性行为、执行与环境信号从 8 万条生产 Agent 轨迹中筛选最值得人工复盘样本的方法。"
tags:
  - clippings
---

# 大语言模型技术面试题：如何筛选值得复盘的 Agent 轨迹（Technical LLM interview question!）

![原邮件配图](https://embed.filekitcdn.com/e/k7YHPN24SoxyM8nGKZnDxa/rebNqDFnniHnJpNUpKsorU/email)

你拥有来自生产环境的 80,000 条 Agent 轨迹。现在需要找出其中最值得审查的 100 条，以便改进你的 Agent。

不允许使用 LLM 来评估轨迹。你会怎么做？

让我们看看几种方法。

最简单的起点是随机抽样：随机挑选 100 条轨迹进行审查。

![原邮件配图](https://embed.filekitcdn.com/e/k7YHPN24SoxyM8nGKZnDxa/krBWhu2kjr6CKDi15JRfPp/email)

但绝大多数生产 Agent 都能正常处理常规请求，因此这种方法会浪费很大一部分标注预算。

另一种方法是筛选更长的对话，因为用户消息达到 10 条以上通常意味着更高的复杂度。

不过，长对话会严重偏向彻底失败的案例。你能找出显而易见的故障，却会错过那些“技术上完成了任务”、但仍暗藏细微问题的对话。

DigitalOcean 的一篇[近期论文](https://arxiv.org/pdf/2604.00356)提出了一种新方法。

![原邮件配图](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F348b55cc-2e33-45b0-8a80-f31681a7ce21_1061x1015.png)

它使用确定性规则，直接从轨迹数据中计算轻量级行为信号。

这些信号分为三组：

1. **交互信号**
   - 用户重新表述请求或纠正 Agent，意味着存在错位（misalignment）。
   - Agent 重复自身内容，意味着停滞（stagnation）。
   - 用户放弃使用 Agent，意味着脱离（disengagement）。
   - 用户确认某件事已成功，意味着满意（satisfaction）。

   所有这些信号都可通过归一化短语匹配和相似度检查检测出来。

2. **执行信号**
   - 某次工具调用未推动任务前进，是失败信号。
   - 以完全相同或持续漂移的输入重复调用，表明发生了循环。

   这些信号可以直接从执行日志中提取。

3. **环境信号**

   例如速率限制、上下文溢出和 API 错误。

   这些信号有助于诊断，但不应用于训练，因为它们反映的是系统约束，而非 Agent 的决策。

![原邮件配图](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc1908fc0-67d9-4c76-9b4a-ad7f2f9d6019_1108x552.png)

系统会根据各类信号是否触发为每条轨迹打分，再抽样出信号得分最高的轨迹进行审查。

在 τ-bench 上，作者比较了三种方法在 100 条轨迹上的效果：

- 随机抽样的信息性命中率为 54%。
- 基于长度的启发式方法达到 74%。
- 基于信号的抽样达到 82%。

这意味着，每审查 5 条轨迹，大约有 4 条确实有助于改进 Agent。

事实上，即使在 Agent 已正确完成任务的对话中，信号抽样仍在 66.7% 的案例中识别出有价值的模式；随机抽样的比例则为 41.3%。

这些细微问题包括：策略违规、低效的工具使用，以及不会导致任务失败、但仍会影响优化效果的不必要步骤。

整个框架无需任何 LLM 开销，可以作为生产流水线中的常驻组件运行。

如果想实际体验这种方法，基于信号的方案已经集成到 [Plano](https://github.com/katanemo/plano) 中。Plano 是一个开源的 AI 原生代理，集路由、编排、护栏与可观测性于一体。

![原邮件配图](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F97164b14-e9ff-4676-9b9a-31e325a91d6e_1456x902.png)

- [Plano GitHub 仓库](https://github.com/katanemo/plano)
- [arXiv 论文](https://arxiv.org/pdf/2604.00356)

👉 留给你的问题：你会采用什么方法解决这个问题？
