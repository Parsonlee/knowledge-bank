---
type: concept
tags:
  - AI-Agent/skill
---

# 概念：Agentic 设计模式分类

## 定义

Agentic 设计模式（Agentic Design Patterns）是构建智能体（Agent）系统时可复用的架构方案，覆盖从任务分解、智能路由到多智能体协作的全链路设计选择。

## 分类体系（Antonio Gulli《Agentic Design Patterns》）

### 核心模式（Core Patterns）

| 模式 | 核心思想 |
|------|---------|
| **提示链（Prompt Chaining）** | 将复杂任务分解为串联处理流水线，每步单独迭代测试 |
| **路由（Routing）** | 根据任务类型/输入内容动态选择最佳处理路径 |
| **并行化（Parallelization）** | 同时执行多个独立子任务，提升效率 |
| **反思（Reflection）** | 生成→自我评估→迭代改进的反馈循环 |
| **工具使用（Tool Use）** | 集成外部工具/API，扩展 Agent 能力边界 |
| **规划（Planning）** | 多步骤计划制定与执行，分解复杂目标 |
| **多智能体协作（Multi-Agent）** | orchestrator 分配任务，worker 并行执行 |

### 高级模式（Advanced Patterns）

- **记忆管理（Memory Management）**：短期/长期记忆维持上下文连续性
- **学习与适应（Learning & Adaptation）**：从经验中持续优化行为
- **目标设定与监控（Goal Setting & Monitoring）**：动态目标管理与进展追踪

### 集成模式（Integration Patterns）

- **异常处理与恢复**：优雅错误处理，保证系统稳定性
- **人机协作（HITL）**：融合人类判断与 AI 执行能力
- **知识检索（RAG）**：检索增强生成结合外部知识库

### 生产模式（Production Patterns）

- **Agent 间通信（A2A）**：智能体通信协议
- **资源感知优化**：平衡性能与成本
- **护栏/安全模式（Guardrails）**：防止不当行为
- **评估与监控**：量化 Agent 表现
- **探索与发现**：自主发现新解决方案

## 最重要的实践原则

1. **优先确定性工作流**：Agent 生成 DAG 计划→结构化执行，失败可追溯到具体步骤
2. **提示链 vs 单一 Prompt**：复杂任务应拆分，每个 Prompt 简单、突出、可单独迭代
3. **反思模式降低幻觉**：生成前先推理，生成后自检

## 关联概念

- [[概念_orchestrator-worker模式]]
- [[概念_多智能体协调]]
- [[概念_Agent感知记忆推理三能力]]
- [[概念_Agent三层记忆体系]]
- [[概念_HITL_MCP]]
- [[概念_RAG基础流程]]

## 来源

- [[Agentic_Design_Patterns_中文翻译版]]
