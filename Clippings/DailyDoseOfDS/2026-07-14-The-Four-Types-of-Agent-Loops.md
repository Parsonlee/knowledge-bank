---
title: "The four types of agent loops"
source: "https://mail.google.com/mail/u/0/#inbox/19f6174c7b5adc67"
author:
  - "[[DailyDoseOfDS]]"
published: 2026-07-14
created: 2026-07-30
description: "系统化拆解 Agent 循环工程（Loop Engineering）的四种核心模式：对话轮次驱动、目标评价驱动、时间定时驱动与主动事件驱动，帮助开发者根据任务特性选择最佳控制流结构。"
tags:
  - clippings
---

# Agent 循环工程的四种核心架构（The four types of agent loops）

“循环工程”（Loop Engineering）经常被人们当作单一的技术概念来讨论，但它实际上是**四种不同架构结构之间的选择**，每种结构适应于不同类型的任务。

循环工程的核心是设计控制与引导 Agent 的系统，而不是人工一步一步手控。

该系统始终需要回答两个基本问题：
1. **是什么触发了一次运行？**
2. **由谁来判断工作已经完成？**

在人工手动的会话中，人类在每一步都回答了这两个问题。而每一种循环类型，都是将更多的此类职责交由系统自动化处理。

![Agent 四种循环模式对比总览](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6296b4b4-3f8c-4d3e-b193-24b456d14b03_960x922.gif)

---

### 一、 轮次驱动型循环（Turn-based loops）

**触发机制**：由用户输入的 Prompt 触发。

![轮次驱动型循环架构图](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F03f8a20d-3be6-4667-b9b1-528e817e4ca6_1188x308.png)

Agent 在单个 Turn 内部收集上下文、执行动作并检查自己的工作。随后由人类审查输出结果，并编写下一个 Prompt。

* **适用场景**：当需求尚不明确、且每一次的输出都会改变下一个 Prompt 的提问方向时使用。

---

### 二、 目标驱动型循环（Goal-based loops）

**触发机制**：由携带成功标准与预算控制的 `/goal` 指令触发（例如：“将首页 Lighthouse 得分提升至 90，最多尝试 5 次”）。

![目标驱动型循环架构图](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fbc34a00c-adcd-4197-941b-56457404e9e3_1187x236.png)

当 Agent 尝试停止时，一个评估器模型（Evaluator Model）会检查目标是否达成。若未达成，则将其打回继续工作。

* **适用场景**：当最终输出结果是可量化测量的，但具体实现路径不需要人类干预时使用。

---

### 三、 时间驱动型循环（Time-based loops）

**触发机制**：由系统时钟（Clock）定时触发。

![时间驱动型循环架构图](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fedda4aa4-0acd-44b6-831a-6e875f9b76a9_1187x228.png)

时间间隔触发后，Agent 运行固定的 Prompt（如“检查 PR 并修复 CI”），然后等待下一个周期。`/loop` 命令在本地运行，而 `/schedule` 会将其移至云端以在断网/关机后继续生存。

* **适用场景**：用于重复性工作，其任务内容预先已知，仅仅是执行时间定期重复。

---

### 四、 主动事件驱动型循环（Proactive loops）

**触发机制**：由外部事件或排程触发，全程无人类在场。

![主动事件驱动型循环架构图](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F67dc6ddc-7ee4-4a4d-b96d-73b7b1d5943f_1187x275.png)

后台进程监控通道，当有需要处理的事件时自动派生工作流。该工作流包含分诊 Agent（Triage）、修复 Agent（Fix）以及在任务关闭前进行对抗性评审的审查者（Reviewer）。

* **适用场景**：用于常驻责任体系，无法预知会有什么事件进来，只确定一定会发生。

---

### 五、 选型映射总结

每种循环类型相较前一种都交出了更多的工作控制权：
* **Turn-based** 将触发与评价双重职责均保留给人类；
* **Goal-based** 实现了评价检查的自动化；
* **Time-based** 实现了触发周期的自动化；
* **Proactive** 则将两者全部自动化，并在运行时动态决定工作流形状。

因此，技术选型的问题不是哪种循环最先进，而是你的任务属于**探索性（Exploratory）**、**可测量（Measurable）**、**周期性（Recurring）**还是**常驻型（Standing）**。放手交出的控制权越多，你需要手动监控的工作量就越少。
