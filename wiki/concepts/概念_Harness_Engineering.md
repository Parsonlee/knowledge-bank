---
type: concept
tags:
- AI-Agent/harness
- AI-Agent/coding
summary: 围绕基础大模型构建的宿主与编排系统（Harness Engineering），负责编排执行、思考规划、工具行动、上下文感知管理、产物存储与评估。
sources:
- wiki/sources/OpenAI前VP_Lilian_Weng_AI自我改进的近路不是改权重.md
created: '2026-07-22'
updated: '2026-07-22'
---

# 概念：Harness Engineering

## 定义

**Harness Engineering（外壳工程 / 宿主工程）** 是围绕基础模型（Raw Model）构建的那套系统工程。它编排 Agent 的执行逻辑，决定模型如何思考规划、调用工具行动、感知管理上下文、存储中间产物以及评估输出结果。

Lilian Weng 提出了一个类比：**Harness 之于大模型，如同操作系统之于硬件**——封装复杂底层逻辑，保持接口规范简洁。

## Harness 的三大设计模式

1. **工作流自动化（Workflow Automation）**：目标导向的计划-执行-观察-改进循环，驱动模型自主分析运行轨迹与失败原因。
2. **文件系统即持久记忆（Filesystem as Persistent Memory）**：避开受限的上下文窗口，将实验日志、代码 diff、错误追踪落盘为物理文件，利用 shell/bash 标准接口进行读写。
3. **子代理与后台任务（Sub-agents & Background Tasks）**：主代理派生子代理进行并行任务分工，配套显式的进程管理（启动、查看日志、取消、合并结果）。

## 编码智能体标准工具箱

一个完备的编码 Harness 包含：文件系统工具（glob/grep/read/write/edit）、shell/git、MCP 协议组件、搜索与浏览器、后台任务与子代理委托。

## 代表实践

- [[entities/实体_Claude_Code|Claude Code]]：Anthropic CLI 编码智能体，高度集成了 Harness 工程哲学。
- [[entities/实体_Codex|Codex]]：OpenAI 编码智能体系统。

## 来源与参考

- [[OpenAI前VP_Lilian_Weng_AI自我改进的近路不是改权重]]
- [[concepts/概念_RSI递归自我改进]]
- [[concepts/概念_Harness优化阶梯]]
