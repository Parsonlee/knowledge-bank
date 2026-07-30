---
title: "AI Agent 的 6 类上下文"
source: "https://mail.google.com/mail/u/0/#inbox/199f3a89f1a116c9"
author:
  - "[[DailyDoseOfDS]]"
published: 2025-10-17
created: 2026-07-30
description: "邮件将 Agent 的上下文拆为指令、示例、知识、记忆、工具及工具结果六层，强调完整上下文比单一提示词更能决定长程 Agent 的可靠性。"
tags:
  - clippings
---

# AI Agent 的 6 类上下文

邮件的中心观点是：合适的上下文能让能力较弱的 LLM 工作起来；反过来，再先进的模型也无法弥补上下文缺失。生产级 LLM 应用需要的不是一条指令，而是一套定义推理、记忆和决策循环的结构。因而，先进 Agent 架构把上下文当作多维设计层，而非提示词中的一行文本。

## 六个层次

1. **指令（Instructions）**：规定 Agent 是谁、为何行动及如何行动，例如角色（PM、研究员、编程助手）、目标／预期结果、步骤、语气、输出格式与约束。
2. **示例（Examples）**：展示正确与错误的样子，可包含行为演示、结构化样例和反模式。邮件认为模型从模式中学习通常优于只接收文字规则。
3. **知识（Knowledge）**：提供业务流程、API、数据模型与工作流等领域信息，把文本预测连接到实际决策。
4. **记忆（Memory）**：使 Agent 跨会话保持连续性；短期记忆可包括当前推理步骤和聊天历史，长期记忆则包括事实、公司知识与用户偏好。
5. **工具（Tools）**：令 Agent 能超越语言而执行现实操作。每项工具应具备参数、输入和示例；工具设计会影响外部 API 的使用质量。
6. **工具结果（Tool Results）**：把调用结果重新提供给模型，以支持自我纠错、适应和动态决策。

邮件认为这六层共同构成“上下文感知”的 Agent；Claude Code、现实中的 Agent 与记忆工具已采用相同方向。对长程、多步骤任务而言，上下文工程正成为核心能力。

文中还链接了一个涵盖 Agent 基础、工具与结构化输出、Flows、多人／多 Crew 项目、护栏、异步、回调、人类参与、多模态、记忆、ReAct、规划和多 Agent 模式的 [Agentic systems 系列课程](https://www.dailydoseofds.com/ai-agents-crash-course-part-1-with-implementation/)。
