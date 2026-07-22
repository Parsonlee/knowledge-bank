---
type: entity
tags:
- RAG/retrieval
- Skill/python
summary: 开源轻量级嵌入式向量数据库，极简 Python 安装，适合本地 PoC 与 Demo 快速验证。
sources:
- wiki/sources/2026程序员必读的向量数据库原理与选型指南.md
- wiki/sources/向量数据库原理与应用全解析.md
created: '2026-07-22'
updated: '2026-07-22'
---

# 实体：Chroma

## 简介

**Chroma**（ChromaDB）是一款开源的 AI 原生嵌入式向量数据库。它旨在简化 AI 应用的构建，提供极简的 Python/TypeScript API。

## 核心特性

- **极简部署**：单行 `pip install chromadb` 即可快速运行，支持嵌入式模式与 Docker 容器。
- **开箱即用**：与 LangChain、LlamaIndex 开箱即用整合，成为原型开发的首选。

## 选型考量

- **适用场景**：适合本地脚本跑 Demo、概念验证 (PoC) 和轻量级应用（数据量百万以下）。
- **局限性**：不建议直接用于高并发、大规模生产环境。

## 关联

- 相关概念：[[concepts/概念_向量数据库]]
- 来源：[[2026程序员必读的向量数据库原理与选型指南]]、[[向量数据库原理与应用全解析]]
