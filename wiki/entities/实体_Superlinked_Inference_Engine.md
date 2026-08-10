---
type: "entity"
tags: ["Infra/AI", "LLM/inference"]
summary: "Superlinked Inference Engine（SIE）是面向多模型流水线的开源推理服务引擎，以统一 API、共享 GPU 池和按需模型加载协调异构模型服务。"
sources: ["wiki/sources/2026-08-05_How-to-serve-5-models-on-one-GPU_19fd38.md"]
updated: "2026-08-10"
---

# 实体：Superlinked Inference Engine

## 简介

Superlinked Inference Engine（SIE）是 Superlinked 的开源推理服务引擎。根据 2026-08-05 的来源，它将嵌入、重排序、文档解析、信息抽取、视觉和生成模型置于统一服务层，以协调共享 GPU 基础设施上的多模型流水线。

## 功能与机制

- 通过 `extract`、`score`、`generate` 三类原语提供统一调用接口。
- 按请求加载模型，在显存受限时按最近最少使用策略腾出空间。
- 通过共享队列与按预估计算成本分批，让调度层获得跨模型负载视图。
- 提供 gateway 与 worker 层，并以模型目录提供服务配置；来源称其当时目录覆盖 112 个模型。

## 关联

- [[实体_vLLM]]：单模型运行时与多模型协调服务层的对照。
- [[概念_连续批处理]]：请求调度与批处理的相关机制。

## 来源

- [[wiki/sources/2026-08-05_How-to-serve-5-models-on-one-GPU_19fd38]]
