---
type: entity
tags:
  - AI-Agent/multi-agent
summary: "Anthropic 多智能体研究系统，Claude Research 功能的底层架构，orchestrator-worker 模式实现"
created: "2026-06-29"
updated: "2026-06-29"
---

# 实体_Anthropic_Research系统

Anthropic 为 Claude 构建的多智能体研究功能（Claude Research），支持跨 Web、Google Workspace 和各类集成进行复杂任务研究。

## 架构组件

- **LeadResearcher**：主智能体，使用 Claude Opus 4，负责规划、任务分解、汇总
- **Subagents**：子智能体，使用 Claude Sonnet 4，并行执行具体搜索任务
- **CitationAgent**：专职处理引用，定位具体引用位置
- **Memory**：外部持久化存储，保存研究计划（防上下文超限丢失）

## 关键数据

- 多智能体 vs 单智能体 Claude Opus 4：提升 **90.2%**
- 并行化后复杂查询研究时间缩短最高 **90%**
- token 消耗约为 chat 的 15×

## 开发团队

Jeremy Hadfield, Barry Zhang, Kenneth Lien, Florian Scholz, Jeremy Fox, Daniel Ford 及 Anthropic Apps 工程团队

## 开源资源

- Cookbook 提示词示例：https://github.com/anthropics/anthropic-cookbook/tree/main/patterns/agents/prompts

## 相关概念

- [[概念_orchestrator-worker模式]]
- [[概念_多智能体协调]]
- [[概念_Agent思考工具]]

## 来源

- [[Anthropic多智能体研究系统构建]]
