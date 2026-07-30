---
title: "The Anatomy of an Agent Harness"
source: "https://mail.google.com/mail/u/0/#inbox/19d64a1fd91e185f"
author:
  - "[[DailyDoseOfDS]]"
published: 2026-04-06
created: 2026-07-30
description: "深入解析 Agent Harness（智能体套件/外骨骼）的架构设计，探讨包含编排循环、工具集成、内存与上下文管理等 11 个关键生产级组件。"
tags:
  - clippings
---
# Agent Harness 的剖析（The Anatomy of an Agent Harness）

![Agent Harness 概览](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F74c4de9a-7d99-47df-a835-b8eb8f69fef7_1216x912.png)

一个简单的 ReAct 循环、几个工具以及精心编写的系统提示词（System Prompt），在 Demo 演示阶段往往表现惊艳。

然而，一旦实际任务需要执行 10 个步骤以上，整个系统就会迅速走向崩溃：模型会忘记三步前做过什么、工具调用静默失败、上下文窗口充斥着垃圾信息。

**核心问题不在于模型本身，而在于模型周围的所有配套设施。**

LangChain 证明了这一点：在保持底层 LLM 模型与权重完全不变的情况下，仅通过重新设计封装 LLM 的基础设施，他们在 TerminalBench 2.0 榜单上的排名就从 30 名开外飙升至第 5 名。另一个研究项目通过让 LLM 自动优化基础设施本身，达到了 76.4% 的通过率，甚至超越了人类精心编写的手工系统。

这套包覆在模型外围的基础设施，如今拥有了一个正式的工程学名称：**Agent Harness（智能体套件/外骨骼）**。

---

## 什么是 Agent Harness？

“Agent Harness” 一词在 2026 年初被正式形式化定义，但其核心概念早已存在。

简单来说，**Harness 是包裹在 LLM 外围的完整软件基础设施**，包含编排循环（Orchestration Loop）、工具集、内存/记忆系统、上下文管理、状态持久化、错误处理以及安全护栏（Guardrails）。

Anthropic 在 Claude Code 的官方文档中给出了简洁的总结：其 SDK 本质上就是“驱动 Claude Code 运行的 Agent Harness”。

LangChain 的 Vivek Trivedy 提出了一句经典公式：
> **“如果你不是模型本身，那你就是 Harness。”**

用另一种视角来看，“Agent（智能体）” 是系统涌现出的行为特征（即用户与之交互的具备目标导向、工具使用与自我修正能力的实体）；而 **Harness 则是产生该行为的工程机械**。当有人说“我构建了一个 Agent”时，实际含义是他构建了一套 Harness 并将其接入了某个基础模型。

![操作系统比喻](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7a3a9d5f-ef89-47c0-9b87-4dd0a192be15_985x494.png)

Beren Millidge 在 2023 年的文章中给出了极其精准的比喻：
* **原生 LLM（Raw LLM）** 相当于没有 RAM、没有硬盘、没有 I/O 的裸 CPU；
* **上下文窗口（Context Window）** 充当 RAM（速度极快但容量受限）；
* **外部数据库（External DBs）** 充当硬盘存储（容量巨大但相对较慢）；
* **工具集成（Tools Integrations）** 相当于设备驱动程序（Device Drivers）。

而 **Harness 则是整套系统的操作系统（Operating System）**。

---

## 围绕模型的三个工程层次

在现代 AI 系统中，存在三个环环相扣的工程层次：

1. **Prompt Engineering（提示词工程）**：精心打造模型接收到的静态与动态指令；
2. **Context Engineering（上下文工程）**：根据当前步骤，动态检索、剪裁并组装最佳的上下文信息；
3. **Harness Engineering（套件工程）**：控制状态机流转、执行自我修正闭环、持久化历史会话以及统筹子智能体协作。

![11个核心组件](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F933d530a-d817-4e19-9180-8bade83ef57e_1357x706.png)

---

## 生产级 Harness 的 11 个核心组件

一个健壮的生产级 Agent Harness 通常由以下 11 个模块协同构成：

![Orchestration Loop](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F1b2a255e-8439-4212-acea-ff62939cc62a_680x379.png)

### 1. 编排循环（Orchestration Loop）
负责控制 Agent 的生命周期，决定何时向模型发起 Request、何时解析 Tool Call、何时返回控制权给用户或终止执行。

### 2. 工具集成（Tools）
提供标准化 Schema 定义与安全执行环境，包括本地 Shell 命令、API 调用以及 MCP (Model Context Protocol) 插件注册。

![Memory and Context](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F66a7c9d3-c90e-4ae8-9501-07f59dedd3d2_680x407.png)

### 3. 记忆系统（Memory）
区分工作记忆（Working Memory）与长期记忆（Long-term Memory），实现跨 Session 的状态持久化与经验积累。

### 4. 上下文管理（Context Management）
实施 Token 预算控制、历史消息截断、自动摘要生成与懒加载机制，确保上下文窗口不被噪声淹没。

### 5. 提示词构建（Prompt Construction）
将系统指令、环境感知、可用工具列表、动态记忆与交互历史实时合成为最终送入 LLM 的 Payload。

### 6. 输出解析（Output Parsing）
处理模型返回的非结构化文本，强类型校验 JSON / Structured Outputs，并在解析失败时触发重试。

### 7. 状态管理（State Management）
维持严格的状态机（State Machine），保证断点续传（Checkpointing）、回滚（Time-traveling）与并发一致性。

### 8. 错误处理（Error Handling）
针对 API 超时、网络抖动、幻觉工具参数等异常制定优雅退避与自修复路径。

![Verification Loops](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F2ac4f24e-259e-4837-a547-a696f9eed8a0_680x367.png)

### 9. 护栏与安全（Guardrails and Safety）
在工具执行前后实施权限审批（Human-in-the-loop）、敏感数据脱敏与危险操作阻断。

### 10. 验证闭环（Verification Loops）
引入确定性验证（如 Linter、单元测试、编译器）与推理性验证（LLM-as-a-judge），在错误累积前拦截异常。

![Subagent Orchestration](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd95eb7bc-15be-4f0f-9501-06f74856f593_680x381.png)

### 11. 子智能体编排（Subagent Orchestration）
主 Agent 将复杂子任务委托（Delegate）给专精的 Subagent，并在隔离的上下文中并行执行后归并结果。

---

## 演进流程与脚手架隐喻

![Step-by-step walkthrough](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F59a97baa-7dff-424d-89cc-e2829660ecf4_680x370.png)

![Scaffolding Metaphor](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff25b53b2-7a60-44bb-b622-f18b87f1d1bd_680x379.png)

Harness 就像建筑工程中的脚手架。当基础模型（LLM）能力提升时，部分原本属于 Harness 的显示规划与控制逻辑会被模型内部内化（例如 Anthropic 随着新版本发布逐步移除了 Claude Code Harness 中的显式规划步骤）。但 Harness 本身绝不会消失——即使最强大的模型也需要外围基础设施来管理其物理边界、工具执行与状态校验。

---

## 结论：Harness 即产品

![Harness is the Product](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F63894e2b-ad10-47a4-8de4-36e3be7a88fd_680x380.png)

在基座模型趋同的背景下，两款使用相同模型的 AI 产品，其最终表现可能天差地别，决定性差异正是 Harness 的工程水平。

下次当你的 AI Agent 执行失败时，先不要急于指责模型不够聪明，试着审视并重构你的 Agent Harness。
