---
type: concept
tags:
  - Skill/knowledge-bank
  - AI-Agent/coding
---

# 概念：LLM Wiki 范式

## 定义

**LLM Wiki** 是由 [[实体_Andrej_Karpathy]] 提出的一种全新知识管理范式，旨在颠覆传统 RAG（检索增强生成）“临时抱佛脚”的模式，强调**在知识摄入（Ingest）阶段即完成信息的结构化与编译**。

## 与传统 RAG 的深度对比

| 维度 | 传统 RAG | LLM Wiki |
|------|----------|----------|
| **核心思维** | “我有一堆文档，AI 现场帮我搜” | “AI 平时帮我编译好知识库，我随时用” |
| **处理时机** | **查询时（Query-time）** 临时检索与拼接 | **摄入时（Ingestion-time）** 预先结构化与关联 |
| **知识复利** | **无积累**：每次查询从零开始，搜完即散 | **高复利（Compounding）**：新知识在图谱中交叉引用与补充 |
| **存储形态** | 向量数据库（高维度，人类不可读） | 纯 Markdown（零基建依赖，[[实体_Obsidian]] 可读与图谱可视化） |
| **冲突处理** | 检索到矛盾碎片易引发幻觉或逻辑断裂 | 在 Ingest 阶段主动发现、标注矛盾与维护一致性 |

## 三层经典架构（Karpathy 比喻）

1. **底层原始资料（Raw Sources）**：由笔记、剪藏、PDF 构成的只读层，保持绝对原貌。
2. **中间层维基（Wiki Layer - 代码库）**：AI 提取要点、编写词条、建立概念间双向引用的结构化网络。
3. **顶层规则配置（Schema Layer）**：如 `CLAUDE.md` 与 [[概念_系统提示词四层架构]]，指导 AI 理解知识体系 structure、格式与处理 SOP。

> **核心名言**：**"Obsidian 是 IDE，LLM 是程序员，Wiki 是代码库。"** AI 不是搜索引擎，而是知识库管理员。

## 来源与参考

- [[Claude Code与Obsidian飞书知识库搭建实践]]
- [[概念_RAG与LLM_Wiki对比]]
