---
title: "Context engineering for Agents"
source: "https://mail.google.com/mail/u/0/#inbox/199785061541447a"
author:
  - "[[DailyDoseOfDS]]"
published: 2025-09-23
created: 2026-07-30
description: "系统阐述上下文工程（Context Engineering）的概念、核心定义、4 个基本阶段（写入、读取、压缩、隔离）及其与特征工程的类比。"
tags:
  - clippings
---
# Agent 的上下文工程（Context engineering for Agents）

上下文工程越来越重要，但许多人仍然难以真正理解它的具体含义。

简单来说，**上下文工程（Context Engineering）是一门艺术与科学，旨在将正确的信息、以正确的格式、在正确的时间提供给你的 LLM**。

![Andrej Karpathy 对上下文工程的评价](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd3c57039-25e1-400e-aaae-9bff25f2ce8b_1200x1349.png)

要理解上下文工程，首先需要理解上下文的含义。

如今的 Agent 已经演变为远超越聊天机器人的存在。

下图总结了 Agent 正常运行所需的 6 种上下文类型：

![Agent 所需的 6 种上下文类型](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa5baedfc-1c6a-4446-84a2-bcf269d402d1_1200x983.png)

* 指令（Instructions）
* 示例（Examples）
* 知识（Knowledge）
* 记忆（Memory）
* 工具（Tools）
* 护栏（Guardrails）

这表明仅仅对其进行“Prompt 提示”是不够的，你必须对输入（上下文）进行工程化设计。

思考模型：
* 如果 LLM 是 CPU。
* 那么上下文窗口就是 RAM。

![LLM 与 Context Window 类比为 CPU 与 RAM](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7e7bae65-5e25-412c-b612-b8e4d7b70733_1700x1153.png)

---

## 上下文工程的 4 个核心阶段

上下文工程可以拆解为 4 个基本阶段：

![上下文工程的 4 个阶段](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F69186a3b-68d8-4aa7-9e71-3b9dc67bf2b9_1338x964.gif)

### 1. 写入上下文（Writing Context）
将上下文保存到上下文窗口外部，以帮助 Agent 完成任务。

![写入上下文机制](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F56019299-003f-4d6e-a0c3-415095a0f9ca_1200x290.png)

可以将其写入：
* 长期记忆（跨会话持久化）
* 短期记忆（会话内持久化）
* 状态对象（State Object）

### 2. 读取上下文（Reading Context）
将上下文拉取到上下文窗口中，以帮助 Agent 执行任务。

![读取上下文机制](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff19053e8-c69c-486a-a5bc-484ca40d8ef8_1200x286.png)

上下文可从以下位置拉取：
* 工具
* 记忆系统
* 知识库（文档、向量数据库）

### 3. 压缩上下文（Compressing Context）
仅保留任务所需的 Token。

![压缩上下文机制](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F14562048-09f3-4a24-94a5-fce76f3bb58c_1200x286.png)

检索到的上下文可能包含重复或冗余信息（例如多轮工具调用），导致额外的 Token 消耗与成本上升。上下文摘要（Summarization）在此能发挥关键作用。

### 4. 隔离上下文（Isolating Context）
将上下文拆分，以协助 Agent 更好地执行任务。

![隔离上下文机制](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F52ba59c8-4291-4116-ad91-a750639ca218_1200x286.png)

常见隔离手段：
* 使用多个 Agent（或子 Agent），每个拥有独立上下文
* 使用沙箱环境（Sandbox）存储与执行代码
* 使用状态对象（State Object）控制作用域

---

就像在传统机器学习中构建特征（Feature Engineering）以使模型生效一样——移除对输出没有贡献的特征、注意高度相关特征未必有帮助——在 LLM 领域也需要工程化设计上下文，使模型更准确地响应。
