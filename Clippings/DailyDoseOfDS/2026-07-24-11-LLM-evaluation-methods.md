---
title: "11 LLM evaluation methods"
source: "https://mail.google.com/mail/u/0/#inbox/19f962933027e3e6"
author:
  - "[[DailyDoseOfDS]]"
published: 2026-07-24
created: 2026-07-30
description: "全面梳理大语言模型评估的 11 种核心方法，从字符串重叠、语义嵌入到 LLM-as-a-Judge、评测陪审团、DAG 决策树及轨迹安全门禁全景覆盖。"
tags:
  - clippings
---

# 大语言模型（LLM）评估的 11 种核心方法（11 LLM evaluation methods）

大模型可能会回答出一个完全正确但 BLEU 得分接近于零的答案。这凸显了 LLM 评估的复杂性。本文全面梳理生产环境中使用的 11 种核心评估范式：

![11 种 LLM 评估方法分类全景图](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6222b4ea-4c55-460f-90e6-ee328a9dc3d4_1456x561.png)
*图 1：11 种 LLM 评估方法分类全景*

---

### 11 种评估方法深度拆解

#### 1. Exact Match（完全匹配）
最基础的匹配方式，检查模型输出与标准答案是否逐字完全一致。适用于结构化 JSON、数字回答或选项选择。

#### 2. Lexical Overlap（词法重叠：BLEU / ROUGE）
通过 $n$-gram 重叠度衡量生成文本与参考文本的相似程度。对于开放式问答效果较差，但常用于机器翻译和文本摘要基线。

#### 3. Embedding Distance（语义嵌入距离）
使用 Embedding 模型将生成文本与参考文本映射为向量，计算余弦相似度（Cosine Similarity）。能捕捉语义相关性而非字面匹配。

#### 4. Task-Specific Classifiers（任务专用分类器）
训练专门的小型分类模型（如 BERT）来检查生成的响应是否满足特定属性（如情绪分类、意图分类、格式合规性等）。

#### 5. Pairwise Ranking（成对排序）
将两个模型的输出同时提交给评估器，判别哪一个输出更好。常用于 RLHF 偏好数据采集与胜率（Win Rate）评估。

#### 6. Single LLM Judge（单模型裁判）
使用 GPT-4 等强模型作为裁判，依据预设的 Scoring Rubric 给生成结果打分。

#### 7. LLM Jury（LLM 评测陪审团）
单一 LLM 裁判存在固有的同族模型偏好（Self-preference bias）。陪审团机制通过引入不同模型家族（如 Claude + GPT + Gemini）进行投票平均，有效抵消单模型偏置。

#### 8. DAG Rubric（有向无环图评分树）
将评分规则设计为 DAG 决策树，每个节点询问一个明确的问题并进行路由分叉。保证具有硬性约束（如格式、法律免责声明）的评分具有确定性。

#### 9. Trajectory Accuracy（轨迹精确度）
评估 Agent 的全套思维链（CoT）、工具调用序列与观察路径。重点检查 Agent 是否通过错误的路径侥幸得到了正确答案。

#### 10. Multi-turn Eval（多轮对话评估）
将整个多轮对话视为评估单元，考核角色一致性、跨轮次记忆保持与长对话逻辑连贯性。

#### 11. Safety & Guardrail Eval（安全与防护门禁评估）
并行运行偏见、毒性（Toxicity）与 PII 隐私泄露分类器。该项评估应作为系统的硬性门禁（Gatekeeper），而非折算进平均分中。

上述评估指标大部分已在开源 LLM 评估与可观测平台 [Comet Opik](https://github.com/comet-ml/opik) 中开箱即用。
