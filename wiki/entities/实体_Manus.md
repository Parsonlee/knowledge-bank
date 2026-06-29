---
type: entity
tags:
  - AI-Agent/context-engineering
created: "2026-06-29"
updated: "2026-06-29"
---

# 实体：Manus

## 基本信息

- 类型：通用 AI Agent 产品
- 联合创始人：Peak Ji 季逸超
- 发布：2025年3月
- 特点：运行在VM沙盒中，典型任务约50次工具调用，输入/输出 token 比约100:1

## 架构特点

- 基于上下文工程而非微调，与底层模型保持正交
- 分层行动空间：函数调用 / 沙盒工具集 / 软件包与API 三层
- KV缓存优化：前缀稳定、追加式上下文、显式缓存断点
- 工具掩码（非移除）：上下文感知状态机 + logits掩码
- 文件系统作为外化记忆
- todo.md 复述注意力机制
- 保留错误路径作为负面样本

## 演进历史

- 已四次重构Agent框架（"随机梯度下降"式探索）
- MCP发布后从紧凑静态行动空间转变为可无限扩展系统
- 每次重构后发现最大飞跃来自简化而非增加复杂层

## 出现文章

- [[Context_Engineering_LangChain_Manus_NotebookLM]]
- [[Manus创始人手把手拆解上下文工程]]
- [[也许当前最好的上下文工程讲解_LangChain联合Manus]]
- [[浅谈上下文工程_Claude_Code_Manus_Kiro]]
