---
title: "Agent memory and state are not the same thing!"
source: "https://mail.google.com/mail/u/0/#inbox/19fa5754b2a0ee28"
author:
  - "[[DailyDoseOfDS]]"
published: 2026-07-27
created: 2026-07-30
description: "辨析 Agent 系统中状态（State）与记忆（Memory）的技术差异，阐述通过检查点实现中断恢复以及按 Agent 划分记忆作用域的架构设计。"
tags:
  - clippings
---

# Agent 的记忆与状态并不是一回事！（Agent memory and state are not the same thing!）

如果一个 Agent 忘记了它已经学到的东西，那是**记忆（Memory）**出了问题；如果它在执行任务的中途忘记了自己处于什么位置并被迫从头开始，那是**状态（State）**出了问题。

我们曾经在任务中途终止过一个 Agent 以测试其他功能，结果它重新启动时就像之前的执行过程完全没有发生过一样。就在那一刻，我们忽然意识到：我们一直以来都把这两个完全不同的问题混为一谈了。

---

### 一、 状态（State）与当前运行紧密绑定

状态决定了 Agent 在当前单次运行中正在处理什么任务，以及它已经发现了哪些信息。

除非有机制显式将其记录下来，否则这些状态数据在进程崩溃后将彻底消失。

解决方案是在每个已完成步骤之后添加一个**检查点（Checkpoint）**，用以记录 Agent 的最新进度。这样一来，一旦进程异常中断，系统就可以从该精确节点继续执行，而不是彻底从头开始。

---

### 二、 记忆（Memory）是完全不同的概念

记忆是指跨越多次运行依然存在、值得永久保留的事实、经验与关键结论。

起初，我们为所有 Agent 配置了同一个全局共享记忆，并以为这就足够了。然而很快我们发现，Agent 开始读取其他 Agent 的发现并将其误认为是自己的结论。

这就是为什么必须使用 `memory = memory.scope("/agent")` 为每个 Agent 独立划分**记忆作用域（Memory Scope）**的原因。

---

### 三、 拆分状态与记忆后的架构落地

一旦将状态与记忆解耦，整个 Agent 系统的工作流就变得非常清晰且易于推演。

![解耦状态与记忆后的 Agent 基础 Harness 架构](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F106d2285-d15a-448a-a41a-8af78537eca3_1199x654.png)
*图 1：解耦状态与记忆后的 Agent 基础 Harness 架构*

![基于检查点的任务恢复与分支分叉](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F05413595-9081-4608-b60c-74fd3c4f90e0_1199x654.png)
*图 2：基于检查点的任务恢复与分支分叉*

以下是构建任何 Agent 的标准 Harness 基础要点：
* 将记忆与状态视作两个独立的问题分别处理；
* 当发现不应跨 Agent 共享时，对记忆实施独立作用域隔离（Scope）；
* 在每个子任务完成后实时写入检查点；
* 支持从上一个检查点无缝恢复被中断的运行；
* 支持将检查点分叉（Fork）至新分支，无需重复执行之前的繁重工作。

这是构建任何 Agent 的 Harness Baseline。对于通用工作流而言它已足够强大；但对于代码 Agent 及超长运行系统，还需要叠加更多的工程层级。

我们基于 [CrewAI](https://github.com/crewAIInc/crewAI)（100% 开源框架）编写的实战指南完整演示了规划（Planning）、Agent 循环、子 Agent 协作、沙盒隔离、记忆与检查点机制。
