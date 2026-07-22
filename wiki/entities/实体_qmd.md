---
type: entity
tags:
- Skill/knowledge-bank
- RAG/retrieval
summary: 基于 Rust 编写的本地 Markdown 搜索引擎，支持全文检索、语义搜索与混合搜索。
sources:
- wiki/sources/Karpathy推文引发的LLM_Wiki知识库搭建实践.md
created: '2026-07-22'
updated: '2026-07-22'
---

# 实体：qmd

## 简介

**qmd** 是一款使用 Rust 编写的轻量级本地 Markdown 搜索引擎。

## 核心功能与作用

- **三种搜索模式**：同时支持关键词全文检索（BM25）、向量语义搜索与多路[[concepts/概念_混合检索|混合搜索]]。
- **解决 Wiki 规模膨胀瓶颈**：当 LLM Wiki 知识库拓展至 300+ 页面时，全量索引文件 `index.md` 单词上下文开销庞大（15K+ token），qmd 可作为高效的本地前置检索引擎，精准提供候选上下文。

## 关联

- 相关概念：[[concepts/概念_LLM_Wiki范式]]、[[concepts/概念_混合检索]]
- 来源：[[Karpathy推文引发的LLM_Wiki知识库搭建实践]]
