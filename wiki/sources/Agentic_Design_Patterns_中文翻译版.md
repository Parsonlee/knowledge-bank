---
type: source
tags:
  - AI-Agent/skill
summary: "《Agentic Design Patterns》中文翻译项目：Antonio Gulli 著，424页，涵盖21种 Agent 设计模式的完整实践指南"
sources:
  - "Cubox/《Agentic Design Patterns》中文翻译版-2025-10-29.md"
created: "2026-06-29"
updated: "2026-06-29"
confidence: high
---

## 来源信息

- 原文：GitHub 项目 ginobefun/agentic-design-patterns-cn
- 原始链接：https://github.com/ginobefun/agentic-design-patterns-cn
- 原书作者：Antonio Gulli（Springer 出版，版税捐赠救助儿童会）
- 原书链接：https://www.amazon.com/Agentic-Design-Patterns-Hands-Intelligent/dp/3032014018/

## 核心要点

### 书籍概览

全书 424 页，中英双语对照翻译，分四大部分：

**第一部分：核心设计模式（103页，7章）**
1. 提示链（Prompt Chaining）——分而治之，任务分解为处理流水线
2. 路由（Routing）——根据情境选择最佳行动路径
3. 并行化（Parallelization）——同时执行多个独立任务
4. 反思（Reflection）——通过反馈循环自我评估迭代改进
5. 工具使用（Tool Use）——集成外部工具与 API 扩展能力
6. 规划（Planning）——多步骤计划制定与执行
7. 多智能体协作（Multi-Agent Collaboration）——协同工作架构

**第二部分：高级设计模式（61页，4章）**
- 记忆管理、学习与适应、模型上下文协议（MCP）、目标设定与监控

**第三部分：集成设计模式（34页，3章）**
- 异常处理与恢复、人机协作（HITL）、知识检索（RAG）

**第四部分：生产设计模式（114页，7章）**
- Agent 间通信（A2A）、资源感知优化、推理技术、护栏/安全模式、评估与监控、优先级排序、探索与发现

**附录（74页）**
- 高级提示技术、框架概览、AgentSpace 实践、推理引擎内幕、编程 Agent 等

### 核心概念

- **渐进式披露**：只展示足够决策的信息，按需加载更多细节
- **提示链**：复杂任务分解为串联处理流水线，每步可单独迭代测试
- **反思模式**：生成→自评估→改进的迭代循环
- **多智能体协作**：orchestrator 分解任务，worker 并行执行

### 代码示例

配套 `codes/` 目录，支持 LangChain/LangGraph，兼容 OpenAI API 及 OpenRouter，每章有 Google Colab 链接。

### 翻译规范

- 中文内容黄色高亮（`<mark>文本</mark>`）
- 双语对照，重要术语保留英文+括号注中文
- CC BY-NC 4.0 开源，禁止商业使用

## 关键引文

（本文为项目介绍页，核心内容为目录结构，无单独高亮）

## 关联

- [[概念_Agent开发范式三级进化]]
- [[概念_orchestrator-worker模式]]
- [[概念_多智能体协调]]
- [[概念_Agent感知记忆推理三能力]]
- [[概念_MCP协议]]
- [[概念_HITL_MCP]]
- [[概念_RAG基础流程]]
- [[概念_思维链CoT高级方法]]
