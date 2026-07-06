---
tags:
- RAG
confidence: medium
type: concept
summary: Self-RAG（Self-Reflective RAG，自我反思 RAG）是一种让 LLM 生成初步答案后进行自我检查，并决定是否需要额外检索或调整答案结构的
  RAG 生成策略。
created: '2026-07-06'
updated: '2026-07-06'
sources:
- raw/OpenAI 翁荔提出大模型「外在幻觉」：万字 blog 详解抵抗办法、产幻原因....md
- raw/RAG从入门到精通系列6：Retrieval（检索）.md
- raw/探索提升RAG系统问答质量的技术路线.md
- wiki/sources/LLM_32种消除幻觉技术综述.md
- wiki/sources/RAG检索_Retrieval入门到精通.md
- wiki/sources/提升RAG问答质量的技术路线.md
- wiki/sources/翁荔_LLM外在幻觉_原因检测抵抗.md
---

# 概念_Self-RAG


## 定义

Self-RAG（Self-Reflective RAG，自我反思 RAG）是一种让 LLM 生成初步答案后进行自我检查，并决定是否需要额外检索或调整答案结构的 RAG 生成策略。

## 工作原理

- LLM 生成初步答案
- 对答案进行自我反思检查（引入额外"自我检查"步骤）
- 决定是否需要额外检索或调整答案结构
- 更高效地评估和改进检索和生成结果
- 论文：https://arxiv.org/abs/2310.11511

## 优势

- 提高生成的连贯性和合理性
- 适用于开放领域问答，提高 LLM 的"自我意识"

## 实现参考

- LangGraph 工作流实现 Self-RAG

## 关联

- 相关概念：[[概念_CRAG]]、[[概念_Adaptive-RAG]]、[[概念_RAG基础流程]]、[[概念_重排序Rerank]]
- 来源：[[提升RAG问答质量的技术路线]]、[[RAG检索_Retrieval入门到精通]]

> 注：本页 confidence 为 medium，全文仅概要介绍未展开算法细节。