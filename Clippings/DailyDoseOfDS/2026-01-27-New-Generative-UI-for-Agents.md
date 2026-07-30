---
title: "[New] Generative UI for Agents"
source: "https://mail.google.com/mail/u/0/#inbox/19c010d600302f25"
author:
  - "[[DailyDoseOfDS]]"
published: 2026-01-27
created: 2026-07-30
description: "深度解析 Cursor、Claude 等顶尖 AI 应用的核心架构 Generative UI，阐述其三大演进范式与 CopilotKit 开源技术栈落地方案。"
tags:
  - clippings
---

# [新趋势] 面向 Agent 的生成式 UI（[New] Generative UI for Agents）

Cursor、Claude、Lovable 等顶尖 AI 产品有着一个鲜少被公开讨论的共同核心技术——**生成式 UI（Generative UI）**。

如果你正在构建 AI 应用，这无疑是当今必须掌握的最关键架构设计范式。

## 1. 为什么传统的 Chat 界面不再适用？

目前大多数 AI 应用依然沿用传统对话范式：用户输入文本，系统返回文本。这种模式对于基础的 Q&A 问答足够有效。

但现代 AI Agent 需要执行复杂工作流、调用外部工具、管理上下文状态，并在关键节点暂停等待人类决策。纯文本 Chat 界面根本无法承载这些复杂交互。

上述领头产品早已意识到这一点：**Agent 不应仅参与对话，更应该直接参与界面渲染**。

例如：
* 天气工具应当返回一个精心设计的天气卡片，而非一段纯文本。
* 敏感操作必须弹出交互式确认对话框并等待点击。

需要强调的是，**Generative UI 并不是指大模型实时生成原始 HTML 代码**，也不是更高级的 Markdown 聊天框，更不是用 AI 替代整个前端。

它的实际工作逻辑更加实用：开发者预先构建好常用交互组件（如进度条、对话框、数据表格、图表），在运行时由 Agent 挑选最合适的组件并填充数据，前端直接进行标准化渲染。

![图 1：Generative UI 核心架构与交互模式图解](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa5781b79-8952-4fd8-ae92-3bd57e629595_1341x576.png)
*说明：图 1：Generative UI 核心架构与交互模式图解*

## 2. Generative UI 的三大范式

目前业界涌现出三种主要实现范式：

1. **静态范式（Static）**：Agent 将数据填充至预定义组件中，提供最高的控制力与UI一致性。
2. **声明式范式（Declarative）**：Agent 从组件注册表中组装 UI，兼具灵活性与可预测性。
3. **开放式范式（Open-ended）**：Agent 返回完全开放的内容（如 iframe 或 raw HTML），提供最大灵活性但控制力较低。

![图 2：Generative UI 组件选择与数据填充流水线](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F82570727-8291-4343-9117-baf8c3276b98_2466x819.png)
*说明：图 2：Generative UI 组件选择与数据填充流水线*

## 3. 实时双向通信协议与开源生态

组件本身还不够，Agent 需要主动推送状态更新并接收用户操作反馈，这需要实时的双向通信。

目前涌现出了三大核心规范：
* **A2UI 与 MCP Apps**：定义 Agent 意图与渲染内容。
* **AG-UI**：处理 Agent 与前端之间的实时状态同步。
* **应用控制层**：掌控外观表现与交互行为。

解耦这些分层使得架构极为灵活：你可以在不修改前端代码的前提下更换 Agent 框架，也可以在不重写 Agent 逻辑的情况下升级 UI 组件。

![图 3：CopilotKit 开源栈与 AG-UI / A2UI 协议继承解耦设计](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fadccb247-53ed-400c-9e13-e1e63ad5e578_1882x663.png)
*说明：图 3：CopilotKit 开源栈与 AG-UI / A2UI 协议继承解耦设计*

**CopilotKit** 已经为 React 开源了完整的 Generative UI 技术栈，开箱即用支持 LangGraph、CrewAI、Mastra 等主流 Agent 框架，并原生支持 AG-UI、A2UI 及 MCP Apps 协议。
