---
title: "将任意 ML 模型、RAG 或 Agent 部署为 MCP 服务器"
source: "https://mail.google.com/mail/u/0/#inbox/198fc6ca70584770"
author:
  - "[[DailyDoseOfDS]]"
published: 2025-08-30
created: 2026-07-30
description: "介绍 LitServe 的 /mcp/ 端点：将模型、RAG 或 Agent 以 MCP 服务器形式提供给 Claude Desktop、Cursor 等兼容客户端。"
tags:
  - clippings
---

# 将任意 ML 模型、RAG 或 Agent 部署为 MCP 服务器

要让 AI 模型同时服务 Slack 机器人和客服面板等不同应用，通常需要为每个场景单独编写集成代码。本文以 [LitServe](https://github.com/Lightning-AI/LitServe) 说明如何借助 MCP 简化这件事。

LitServe 是基于 FastAPI 构建的开源 AI 模型服务引擎。它集成了专用的 `/mcp/` 端点，因此任意 AI 模型、RAG 或 Agent 都可以被 MCP 兼容客户端（例如 Claude Desktop 或 Cursor）调用。

邮件将服务端代码的职责划分如下：

- `InputRequest` 类定义输入 schema；
- `setup` 方法定义 ML 模型；此处可以放置待部署的 Agent、RAG 等任意对象；
- `decode_request` 准备输入；
- `predict` 执行推理逻辑并产生输出；
- `encode_response` 返回响应；
- 主程序保护块启动启用 MCP 的 LitServe API。

运行 `python server.py` 后，模型即可作为 MCP 服务器提供服务；随后在 Claude Desktop 中添加相应配置并重启应用，即可与该模型交互。

![邮件中的 LitServe / MCP 示例配图](https://embed.filekitcdn.com/e/k7YHPN24SoxyM8nGKZnDxa/rNciaixq823mo9bLJ3sQgg)

## 作者列出的 LitServe 特点

- 相比原生 FastAPI 快 2 倍；
- 可服务 LLM、视觉、音频和多模态模型；
- 可在一个文件中组合 Agent、RAG 与管道；
- 可以加入自定义逻辑，并完全掌控推理过程。

详细说明见 [LitServe MCP 文档](https://lightning.ai/docs/litserve/features/mcp)。

## 延伸阅读

邮件还回顾了 MCP 速成课程的主题：主机—客户端—服务器模型、能力与传输机制、函数调用与 MCP 的差异、自定义本地客户端、工具/资源/提示词工作流、采样、测试与安全、沙箱，以及与 LangGraph、LlamaIndex、CrewAI、PydanticAI 的集成。

## 广告 / 推广

邮件推广 Daily Dose of Data Science 会员资源，并在末尾提供面向超过 75 万 AI 从业者的广告投放服务；这些信息不属于 LitServe 或 MCP 部署的技术说明。
