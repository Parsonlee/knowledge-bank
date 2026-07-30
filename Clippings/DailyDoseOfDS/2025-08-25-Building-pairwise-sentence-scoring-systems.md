---
title: "构建句对评分系统"
source: "https://mail.google.com/mail/u/0/#inbox/198e2e9234d8b09f"
author:
  - "[[DailyDoseOfDS]]"
published: 2025-08-25
created: 2026-07-30
description: "说明句子、段落或文档两两评分是 RAG、问答、信息检索和重复内容检测等 NLP 系统的基础模块，并给出延伸学习资源。"
tags:
  - clippings
---

# 构建句对评分系统

![句对评分系统示意图](https://substack-post-media.s3.amazonaws.com/public/images/6878b8fa-5e74-45a1-9a89-5aab92889126_2366x990.gif)

现实中的 NLP 系统会显式或隐式地依赖上下文相似度。句对（也可扩展至段落对、文档对）评分正是许多应用的基础构件。

## 典型应用

- **RAG**：RAG 系统严重依赖句对评分来检索相关上下文；评分的粒度可随数据切块方式而变化，检索到的上下文随后交给 LLM 生成。这也是“RAG 有 80% 是检索、20% 是生成”这一说法的原因：大部分效果取决于能否检索到正确上下文。
- **问答系统**：许多问答系统会隐式评估问题与候选答案之间的相似度。
- **信息检索（IR）**：对查询—文档对进行评分，并据此为给定查询排序最合适的文档。
- **重复内容检测**：判断两个句子或问题是否表达相同含义。这类需求常见于 Stack Overflow、Medium、Quora 等社区平台；例如 Quora 会在阅读某问题的回答时展示相关问题。

依赖句对评分的任务还可以继续列举，但核心在于：它是许多 NLP 应用不可缺少的基础能力。

## 学习建议

若要构建这类系统，需要理解相应技能与当前先进方法。邮件推荐的两部分系列以面向初学者的方式覆盖背景、传统方法的挑战、合适的方法与实现：

1. [第一部分：用于句对相似度评分的双编码器与交叉编码器](https://www.dailydoseofds.com/bi-encoders-and-cross-encoders-for-sentence-pair-similarity-scoring-part-1/)
2. [第二部分：AugSBERT——双编码器 + 交叉编码器用于句对相似度评分](https://www.dailydoseofds.com/augsbert-bi-encoders-cross-encoders-for-sentence-pair-similarity-scoring-part-2/)

如果此前没有接触过这类系统，也无需担心；上述系列旨在从必要的上下文开始讲解。
