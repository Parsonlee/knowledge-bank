---
title: "Recursive language models."
source: "https://mail.google.com/mail/u/0/#inbox/19ef7234678feae5"
author:
  - "[[DailyDoseOfDS]]"
published: 2026-06-24
created: 2026-07-30
description: "深入探讨递归语言模型（Recursive Language Models, RLM）的架构原理：通过分治递归分解复杂任务与无限上下文处理。"
tags:
  - clippings
---
# 递归语言模型详解（Recursive language models.）

当大语言模型面对极度复杂的任务或海量上下文时，单次推导往往会导致注意力分散或超出窗口上限。**递归语言模型（Recursive Language Models, RLM）** 提出了一种分治思想的递归解决范式。

---

## 1. 递归拆解与子任务分发架构

![递归语言模型核心原理图解](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4ae6613e-4904-4676-b5e0-e7262c73b838_1277x1142.gif)

RLM 的核心机制包括：
1. **递归分解（Recursive Decomposition）**：模型评估输入任务，若过于复杂，则将其拆解为若干独立子任务；
2. **子 Agent/模型实例化（Sub-instance Invocation）**：派生新的 LLM 实例（基准情况 Base Case）去解决简单子问题；
3. **递归归并与结果汇总（Recursive Aggregation）**：向上返回子问题的推导结果并由父节点汇总。

---

## 2. 递归调用的核心算法流程

![递归分治处理全景图解](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fccef5110-cc7d-4c56-8735-980b18f831a5_1024x559.png)

![递归终止条件与 Base Case](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F2d2fcc85-d620-462f-afa4-72b7f48788c3_1024x559.png)

![上下文隔离与变量传递图解](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F909152f2-f0bf-49fc-8714-e789a1782a61_1024x559.png)

![海量长文本递归摘要处理](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe4654329-c430-4830-941f-8ef1c634753f_3816x1400.png)

这种递归架构彻底突破了传统单一提示词处理超大文档或超长推导链条时的注意力退化问题，为处理超大规模任务提供了天然扩展能力。
