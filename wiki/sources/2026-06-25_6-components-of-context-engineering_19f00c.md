---
type: source
tags:
- AI-Agent/context-engineering
summary: 探讨上下文工程（Context Engineering）的 6 个核心组件，包括提示词技术、查询增强、长期记忆、短期记忆、知识库检索以及工具与智能体，并指出上下文工程是决定AI应用质量的75%的关键部分。
sources:
- raw/articles/2026-06-25_6-components-of-context-engineering_19f00c.md
updated: '2026-08-04'
---

# 来源：6 components of context engineering

## 来源信息
- **主题**：The AI Engineering Master Stack for 2026!
- **作者**：Daily Dose of DS (avi@dailydoseofds.com)
- **日期**：2026-06-25
- **原始文献**：[[raw/articles/2026-06-25_6-components-of-context-engineering_19f00c.md]]

## 核心要点
1. **AI 资产决定比例（75%法则）**：决定 AI 应用输出质量的要素中，模型选择占 15%，Prompt 占 10%，而其余的上下文工程外围系统（检索、记忆、工具与查询处理等）占 75%。
2. **上下文工程（Context Engineering）定义**：核心在于将恰当的信息，在最合适的时间以正确的格式提供给模型。
3. **六大核心组件**：
   - **提示词技术**：包括 Few-shot 模式识别和 Chain-of-Thought（CoT）推理链。
   - **查询增强**：对用户模糊的 query 进行改写（Rewriting）、扩展（Expansion）、分解（Decomposition）或使用智能体动态重塑（Query Agents）。
   - **长期记忆**：通过向量数据库（语义检索）与图数据库（实体与关系），支持情景（Episodic）、语义（Semantic/事实）和程序性（Procedural/用户习惯）记忆，引入 Zep Graphiti。
   - **短期记忆**：对话历史管理，避免因塞入过多噪声而导致模型表现下降，涉及 compaction 摘要策略。
   - **知识库检索**：涵盖 Pre-Retrieval（切块与元数据保存）、Retrieval（混合检索与重排）和 Augmentation（上下文格式化与排歧）三层机制，引入 Airweave。
   - **工具与智能体**：单/多 Agent 协作；基于 MCP（Model Context Protocol）协议将传统的 $N \times M$ 对接简化为 $N + M$ 对接。

## 关键引文
> "Model selection: 15% | Prompt: 10% | Everything else (retrieval, memory, tools, query handling): 75%"
> "Context engineering is the art of getting the right information to the model at the right time in the right format."

## 联动概念
- [[concepts/概念_上下文工程|概念：上下文工程]]

---
> 📎 **物理文献**：[[raw/articles/2026-06-25_6-components-of-context-engineering_19f00c.md]]
