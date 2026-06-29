---
type: source
tags:
  - AI-Agent/coding
summary: "阿里云团队在 DevOps 系统中构建 Coding 驱动的"自我编程" Agent：基于 Py4j 的 Code+泛化调用机制、仿脑区功能分区架构、Segment 上下文工程、三层记忆体系（感知/短期/长期）的完整工程实践。"
sources:
  - "Cubox/从代码生成到自主决策：打造一个Coding驱动的\"自我编程\"Agent-2025-11-18.md"
created: "2026-06-29"
updated: "2026-06-29"
confidence: high
---

## 来源信息

- 作者：残风、栀七、荀易、辉酱（阿里云开发者）
- 原文：微信公众号 阿里云开发者
- Cubox ID：7390355593191490622

## 核心要点

### 核心创新：Coding 驱动（Code + 泛化调用）

传统 Agent 使用 JSON + 函数组装调用工具，本文方案改为：**LLM 直接生成 Python 代码来控制 Agent 行为**，通过 Py4j 实现 Python 回调 Java 代码的泛化调用。

优势：
- 工具调用不再只能"下一步"，而是拥有**分支、循环等复杂控制逻辑**
- 数据确定性：字符串运算、数字运算、时间运算等 Python 原生能力
- 自我控制：Agent 可检查自身已发起的任务、查询掌握的技能

技术架构：
- 后端：Spring Boot + Spring AI + Spring AI Alibaba
- 代码执行：Java 调用本地 Python 进程（Python Executor）+ Py4j 泛化回调
- 模型分工：Qwen3-Turbo（翻译/数据提取，低延迟）/ Qwen3-Coder（思考/动态代码生成）/ 按需 Qwen/DeepSeek（通用场景）
- 工具：MCP 协议补充业务能力；A2A 协议实现多 Agent 架构

### FIM 格式（Fill-In-Middle）

基于论文《Efficient Training of Language Models to Fill in the Middle》，代码生成使用：
```
<|fim_prefix|> 前缀代码 <|fim_suffix|> 后缀代码 <|fim_middle|>（LLM 续写）
```
优势：上下文感知（同时理解前后缀语义）、精准填充中间片段、逻辑连贯。

### 仿脑区功能分区架构

每个工具箱设计为 Python Class，工具为函数，不同描述/属性映射为 Python 定义。

Agent 被设计为线程，包含五大功能区（Area）：

| 功能区 | 职责 |
|--------|------|
| 感知区 | 接收外部信息，解析用户主语言、模糊化、场景分析、附件数据 |
| 认知区（IntentPlanner） | 接收感知解析数据，生成 Segment 并提交 Python 执行；复杂任务移交运动区 |
| 运动区（TaskExecutor） | 高级认知区，承担复杂任务，内部循环逐轮执行计划，每轮评估进度 |
| 表达区 | 向外传递信息（用户消息/卡片/事件），文本不过度总结 |
| 自我评估区（SelfTaskCheck） | IntentPlanner/TaskExecutor 完成后评估任务完成情况，失败则重新触发 |

运动区（TaskExecutor）每轮 Segments 格式：
```
Round N Segments: [历史所有Segments, ThoughtN, PlanN, CmdN, EvaluationN, NextGoalN]
```

### Segment 上下文工程

Segment 采用 `[Segment]: [Content]` 结构，通过组合不同 Segment 形成 Prompt，实现 CoT 推理。

**System Prompt 结构**（配置化 + 动态化）：平台介绍 / 角色定义 / 工作机制 / 输入格式说明 / 输出格式要求 / 可用工具（Python Class 描述）/ 重要原则 / 补充增强知识 / 历史经验（知识库检索召回）

**User Prompt 结构**：Segment 序列（User → Context → Thought → Command → Evaluation → NextGoal → ...）

**系统工具**（Agent 自我控制）：检查已发起的任务、查询掌握的技能、主动休眠、主动与用户对话、深度思考、解析数据。

### 三层记忆体系

基于 Atkinson-Shiffrin Memory Model：

**感知记忆（Sensory Memory）**：
- 标签页维度，最短期记忆
- 通过悬浮球捕捉页面/URL 环境感知
- 用于答疑场景：Agent 能"看到"用户当前页面，提前预输入上下文

**短期记忆（Short-term Memory）**：
- Session 维度，基于 ES 存储
- 统一 Segment 格式，三类消息：段落记忆消息（InferenceSegment + execId + parentExecId）/ 实体记忆消息（工具调用结果、用户关键信息）/ 基础消息
- 流程：用户对话 → 产生 Segment → 存储 → 下轮检索 → 提供上下文

**长期记忆（Long-term Memory）**：
- 知识点（短知识）：一句话配置化知识指引，如"重新部署是流水线概念，重启是诺曼底运维概念"
- 历史会话摘要、用户画像（角色/技能标签/工作习惯）
- 代码执行经验：经人工审核 + 大模型投票机制录入经验图谱（规划中）

## 关联

- [[概念_Agent感知记忆推理三能力]]
- [[概念_orchestrator-worker模式]]
- [[概念_MCP协议]]
- [[概念_上下文工程]]
- [[概念_Context_Rot]]
