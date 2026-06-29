---
type: entity
tags:
  - AI-Agent/memory
---

# 实体：MemGPT

**MemGPT**（Memory GPT）是论文《MemGPT: Towards LLMs as Operating Systems》（arXiv:2310.08560）提出的 LLM 记忆管理系统，由 Letta AI 开发。

## 核心思想

将传统操作系统的分层内存管理（物理内存 + 磁盘分页）映射到 LLM 记忆管理，使 LLM 在固定上下文窗口内实现近乎无限的长期记忆。

## 架构

- **LLM 处理器**：固定上下文长度的 LLM，配备分层内存系统和函数集合
- **主上下文（上下文窗口）**：系统指令 + 工作上下文 + FIFO 队列
- **外部上下文**：归档数据库 + 召回数据库
- **函数执行器**：解释 LLM 输出中的函数调用
- **`request_heartbeat=True`**：LLM 输出中的特殊参数，可链接多步检索

## 工作方式

1. LLM 通过函数调用在主上下文与外部上下文之间移动数据
2. 信息超出主上下文时自动归档
3. 需要时通过函数调用检索并 page in 相关记忆
4. 支持多步检索（函数链）

## 公司

Letta AI（原 MemGPT 团队），专注于构建有记忆能力的 AI 智能体平台。

## 参考来源

- [[Agent记忆模块前沿研究简述]]
- [[概念_AI_Agent记忆策略]]
