---
title: "Prompt, context, harness & loop engineering."
source: "https://mail.google.com/mail/u/0/#inbox/19f29f70428b228f"
author:
  - "[[DailyDoseOfDS]]"
published: 2026-07-03
created: 2026-07-30
description: "深入剖析 Agent 系统构建的四大工程层级：Prompt Engineering、Context Engineering、Harness Engineering 与 Loop Engineering 的分层演进与协同架构。"
tags:
  - clippings
---
# Prompt、Context、Harness 与 Loop 工程详解（Prompt, context, harness & loop engineering.）

在智能体（Agent）系统的核心逻辑中，一个 Agent 本质上就是一个 `while` 循环：

* 模型开始运行；
* 模型发起工具调用请求（Tool Call）；
* 工具执行结果返回并更新上下文（Context）；
* 模型再次运行，直到不再发起工具调用并给出最终结果。

早在 2022-2023 年，ReAct 架构就描述了这种循环形式，如今几乎所有 Agent 框架都采用了类似的实现逻辑。然而，在这个基础循环之外，包裹着四大关键工程层级：

1. **Prompt Engineering（提示词工程）**
2. **Context Engineering（上下文工程）**
3. **Harness Engineering（测试套件与外围工程）**
4. **Loop Engineering（循环工程）**

每一层都逐级包裹上一层，模型处于最核心位置。它们之间并不相互竞争，而是各自向外放大一个视角层级。

---

## 1. Prompt Engineering（提示词工程）

![Prompt Engineering 原理](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fac4ffdb4-a6e6-42d0-bda8-d3f34c488883_1300x1080.jpeg)

Prompt Engineering 定义了模型在**单次调用**中所看到的输入，通常由角色（Role）、指令（Instructions）、示例（Examples）和输出格式（Output Format）组成。

提示词工程的技巧在于改变模型因接收到的词句而进行的内部计算与推理过程：
* **思维链（Chain-of-Thought）**：引导模型在给出最终答案前分步骤推导；
* **少样本示例（Few-shot examples）**：明确界定输出格式与边界情况；
* **结构化输出（JSON Schema / XML 标签）**：确保输出可以被代码稳健解析；
* **自一致性（Self-consistency）**：对多条推理链进行采样并采取多数表决。

---

## 2. Context Engineering（上下文工程）

![Context Engineering 架构图](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb03483bf-8b3d-432e-acf6-43176e9ae06a_1080x1080.gif)

上下文工程涉及模型在**单轮对话/执行**中所看到的所有信息，不仅包括 Prompt，还包括用户查询、检索到的文档、记忆、历史对话轮次以及先前步骤的工具输出。

由于上下文窗口是有限的且极易填满，上下文工程的核心工作是评估与排序输入，裁剪所有无法提供价值的冗余信息：
* **检索与重排序（Reranking）**：仅检索与查询最相关的文本块，并进行二次重排序；
* **关键信息位置优化**：避免将关键事实放置在上下文中间（解决 "Lost in the Middle" 精度下降问题）；
* **历史修剪与总结**：汇总旧对话轮次、剔除过期输出，并将大块数据下沉转移到外部文件。

---

## 3. Harness Engineering（测试套件与外围工程）

![Harness Engineering 结构解构](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd913227d-857c-4771-a345-170b32bfa3bf_1200x1200.png)

Harness Engineering 是包裹在模型外围的代码框架，用于定义可用工具、解析模型调用、处理失败重试，并将工作分发路由给子 Agent（例如一个负责检索、另一个负责编写代码）。

验证器（Verifier）随后通过运行测试、校验 Schema 等方式对结果做出评估评分。
如果说 Prompt 和 Context 工程着重于**确保单次调用的准确**，那么 Harness 工程则包含在真实生产系统中运行该调用所需的**所有外围支撑环境**。

---

## 4. Loop Engineering（循环工程）

![Loop Engineering 整体控制流图解](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb52d8006-5880-450c-8414-37ac67bb877f_2400x1650.jpeg)

在常见的开发模式中，开发者手动管理外层循环（即编写提示词、读取 Agent 轮次、编写下一个提示词并重复执行，同时捕捉错误）。

Loop Engineering 层将这项控制权交还给 Agent 本身。Agent 可以在定时器或事件触发下启动，并连续运行多轮操作而无需人工中间干预。

![Loop 停止条件示意](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F286632a3-be0e-45ba-bfa2-dfdaa275d090_793x944.gif)

循环本身默认不知道何时完成。Agent 可能会在测试依然失败的情况下汇报“已完成”并停止。因此，停止逻辑不能依赖 Agent 的单方面声明，必须来自**确定性的真实信号**：
* **轮次与 Token 限制**：设定上限以拦截卡死的运行；
* **无进展检测器（No-progress Detector）**：捕捉重复无效的工具调用；
* **完成度校验（Completion Check）**：通过独立模型或确定性测试来验证目标达成。

![四层工程演进关系示意](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F25a87b56-cedd-4938-9363-5c76e09c1b72_1244x676.png)

到了 Loop Engineering 这一层，开发者是在对**整个运行全生命周期**进行工程化：从编写单次提示词转移到预先设定目标与停止条件，并允许 Agent 自动探索运行。
