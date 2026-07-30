---
title: "Another MCP moment by Anthropic?"
source: "https://mail.google.com/mail/u/0/#inbox/19a274be34a3e99c"
author:
  - "[[DailyDoseOfDS]]"
published: 2025-10-27
created: 2026-07-30
description: "深入解析 Anthropic 推出的 Claude Skills 机制，探讨其作为 Agent SOP 规范对 AI 遗忘问题的解决方案。"
tags:
  - clippings
---

# Anthropic 的又一个 MCP 时刻？（Another MCP moment by Anthropic?）

在推出 MCP（Model Context Protocol）协议之后，Anthropic 再次发布了全新的 **Claude Skills** 机制。这极有可能成为 AI Agent 发展历程中的又一个里程碑时刻。

![Claude Skills 架构与工作机制](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F91bd546c-2a6d-437b-ac3f-21d863c449e1_1980x1530.png)

### 核心痛点：Agent 的长期遗忘与流程混乱

在实际开发 Agent 时，业界长期面临一个普遍但鲜少被彻底解决的问题：**Agent 在长任务执行过程中极易遗忘上下文与标准化流程（SOP）**。当任务变得复杂或跨越多个步骤时，模型经常脱轨，无法按照预期的约束规范执行。

### Claude Skills 的核心理念

Claude Skills 将技能定义为 **Agent 的标准作业程序（SOPs for agents）**：

- **概念定位**：Skills 为 Agent 提供了模版化、高复用的操作规范，明确了特定任务的输入、处理逻辑与输出标准；
- **对比分析**：
  - **Skills vs. MCP**：MCP 侧重于连接外部数据源与工具的通信协议，而 Skills 侧重于内部任务执行的 SOP 标准流程；
  - **Skills vs. Projects / Subagents**：Skills 是模块化的能力单元，可被不同 Project 或 Subagent 灵活加载与复用；
- **自建技能扩展**：开发者可以根据业务场景灵活构建自定义技能，赋予 Agent 确定性强、可重复性高的专业能力。
