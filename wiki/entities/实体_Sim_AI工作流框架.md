---
type: entity
tags:
- AI-Agent/coding
- AI-Agent/UI
- Skill/python
summary: Sim 是用于快速构建 AI Agent 工作流的轻量级可视化框架，支持实时执行、ReactFlow 拖拽界面、Ollama 本地模型、多种部署方式及外部工具连接。
sources:
- wiki/sources/2026-08-01_Build-a-stock-market-research-Agentic-workflow_19fbed_part2.md
updated: 2026-08-04
---

# 实体定义
**Sim** 是一个开源的轻量级、AI-native 可视化智能体工作流（Agentic Flow）拖拽式构建框架。它基于 ReactFlow 开发，旨在帮助开发者在数分钟内构建、调试和部署 AI 智能体工作流。

---

# 核心特征
- **可视化节点编排**：利用 ReactFlow 提供直观的拖拽式（Drag-and-Drop）节点图界面，使智能体流的拓扑结构一目了然。
- **实时工作流执行**：支持实时的节点执行与状态追踪，方便开发者在设计时进行即时调试。
- **本地模型联动**：支持通过 Ollama 接入并运行本地大语言模型，确保了数据的隐私安全性。
- **强大的集成生态**：可以轻松连接各种外部 API、数据库和工具。
- **对标 n8n 的优势**：
  - **更直观的交互**：界面专为 AI 智能体设计，结构更加紧凑清晰。
  - **AI 伴写（Copilot）**：内置更强大的 Copilot 辅助系统，能大幅提升复杂工作流的构建效率。
  - **AI 原生（AI-native）**：在节点状态流转和逻辑判断上，原生支持智能体自主循环与交互。

---

# 典型应用：股票研究 Agent
在实际应用中，Sim 常被用于快速搭建特定领域的 AI 助手，例如构建一个**股票市场研究 Agent**：
- **数据接入**：利用 Alpha-Vantage MCP（Model Context Protocol）接口接入实时且权威的股票市场数据。
- **流程编排**：在 Sim 中通过 ReactFlow 节点图将“数据查询”、“语义分析”、“报告生成”等步骤串联起来。
- **本地部署**：支持 Docker 容器化技术，将 Sim 及其依赖组件一键打包部署在本地环境中。
- **多端触达**：工作流构建完成后，能够快速与 Telegram Bot 等通讯工具联动，实现随时随地的指令式交互与报告推送。
