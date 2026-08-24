---
type: "entity"
tags: ["AI-Agent/tool-calling", "RAG/chunking"]
summary: "专注于为 LLM 和 AI Agent 提取干净 Markdown 数据的开源数据管道团队，代表产品包括网页抓取转 Markdown 服务与本地多格式文档解析工具 anydoc。"
sources: ["wiki/sources/Firecrawl 新工具开源，anydoc，将各种输入转换为md.md"]
updated: "2026-08-20"
---

# 实体：Firecrawl

## 简介
**Firecrawl** 是专注于构建 AI-first 数据输入基础设施的开源团队与产品。其核心使命是将互联网与本地的各种非结构化/半结构化输入，转换为适合大语言模型（LLM）训练、RAG 检索增强生成与 AI Agent 上下文消费的干净、结构化 Markdown 数据。

## 核心产品矩阵与定位

1. **Firecrawl Web 爬取与转换引擎**：
   - 解决网页 DOM 结构复杂、动态 JS 渲染与反爬等问题，将网页一键清洗为干净的 Markdown，广泛用于 Agent Web 浏览工具与企业级 RAG 知识抓取。
2. **anydoc 本地多格式文档转换工具**：
   - 补齐本地多格式文件解析短板。采用纯 Rust 实现与中间稿（IR）两阶段解析架构，支持 Office、PDF、EPUB 等 14 种格式超快速转换。
3. **AI 数据管道底座定位**：
   - 旨在成为 AI 时代的“ffmpeg 数据预处理基础设施”，占据从网页端（Web）到本地文件（Local Documents）两大核心数据输入入口。

## 关联页面
- **核心项目**：[[entities/实体_anydoc|anydoc]]
- **同类数据管道**：[[entities/实体_Jina_AI|Jina AI]]
- **应用场景**：[[concepts/概念_文档结构切分|文档结构切分]]、[[concepts/概念_Agent_Skills元工具架构|Agent Skills 元工具架构]]、[[concepts/概念_RAG基础流程|RAG 基础流程]]
- **支撑来源**：[[sources/Firecrawl 新工具开源，anydoc，将各种输入转换为md|Firecrawl 新工具开源，anydoc，将各种输入转换为md]]
