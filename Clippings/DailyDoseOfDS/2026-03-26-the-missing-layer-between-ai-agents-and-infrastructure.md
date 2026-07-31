---
title: "AI Agent 与基础设施之间缺失的一层（The missing layer between AI agents and infrastructure.）"
source: "https://mail.google.com/mail/u/0/#inbox/19d2bbc9492d99c6"
author:
  - "[[DailyDoseOfDS]]"
published: 2026-03-26
created: 2026-07-30
description: "Teleport 推出了开源的 Agentic Identity Framework，为 AI Agent 提供加密身份、动态访问控制和使用审计，以解决自动系统带来的安全挑战。"
tags:
  - clippings
---

# AI Agent 与基础设施之间缺失的一层（The missing layer between AI agents and infrastructure.）

大多数身份验证模型是为人类和静态自动化设计的。

AI Agent 打破了这些假设，因为它们会持续行动、独立做出决策，并以机器的速度访问基础设施。

因此，要控制访问权限、追踪行为，或者知道哪个 Agent 对什么负责，变得几乎不可能。

Teleport 的 Agentic Identity Framework（Agent 身份框架）是一个开源的、标准驱动的架构，用于在整个基础设施中安全地部署 AI Agent。

它赋予每个 Agent 自己的加密身份，在运行时强制执行访问控制而不是依赖静态权限，自动发现影子 Agent 和未管理的 MCP 服务器，并在系统自主运行时保持完整的行为归因。

该框架还提供了对 LLM 使用的控制，包括速率限制、预算和安全护栏（guardrails）。
