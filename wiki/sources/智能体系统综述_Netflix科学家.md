---
type: source
tags:
- AI-Agent
- LLM/reasoning
summary: Netflix 高级研究科学家 Cameron R. Wolfe 的 AI Agent 系统综述，从底层语言模型出发，拆解规划、记忆、推理与工具调用的完整核心架构。
sources:
- raw/「智能体」，系统综述.md
created: '2026-07-02'
updated: '2026-07-02'
confidence: high
---
# 智能体系统综述

## 来源信息
- 物理文件：[[raw/「智能体」，系统综述.md]]
- 作者：Cameron R. Wolfe (Netflix 高级研究科学家)

## 核心要点
1. **从聊天到自主决策的跃迁**：大语言模型（LLM）不仅是对话生成引擎，更是智能体（Agent）的大脑，能够进行多步推理与决策。
2. **关键架构三要素**：规划（Planning，含反思机制反思链 [[概念_Self-RAG]] 与分解能力）、记忆体系（短期提示词记忆与长期 RAG 记忆库）、工具使用（自然语言转 API 调用）。
3. **推理与反馈闭环**：结合环境反馈不断纠偏，避免单次闭环推理导致的雪崩效应。

## 关联概念与实体
- [[概念_智能体能力金字塔]]
- [[概念_RAG基础流程]]
- [[概念_接地气Groundedness]]

---
> 📎 **物理文献**：[[raw/「智能体」，系统综述.md]]
