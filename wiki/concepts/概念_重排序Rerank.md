# 概念_重排序Rerank

> tags: RAG, RAG/retrieval
> confidence: high

## 定义

重排序（Rerank）是检索后对候选文档按与查询的相关性进行精细排序的环节，传统方式为单塔模型输出相关性 logit 分数。

## 传统 Rerank

- 单塔架构：`[CLS] Query [SEP] Document` 拼接后输入模型
- 最后一层 linear 输出相关性 logit 分数

## Qwen3 Reranker 新范式（LLM 化）

- 将排序任务转化为二元分类问题（yes/no）
- 用 system prompt 设定角色，规定答案只能是 yes/no
- 输入采用类聊天模板：
  - System：判断规则
  - User：`<Instruct>` + `<Query>` + `<Document>`
  - Assistant：让模型生成 yes/no 判断
- 评分公式：`score = P("yes") / (P("yes") + P("no"))`，取值 0~1
- 通过"LLM 化"/"对话化"充分释放基础模型的理解和推理能力
- 支持自定义 Instruct，实现细粒度任务控制

## LLM Reranker 与分层蒸馏（优图）

- 传统 Reranker（BERT/RoBERTa，110M~400M，512 token）→ LLM Reranker（8k+ token，理解能力更强）
- 分层知识蒸馏：约束多个 Transformer 层输出一致，支持层级输出能力（详见 [[概念_分层知识蒸馏]]）

## 关联

- 相关概念：[[概念_检索后处理]]、[[概念_Instruct_Embedding]]、[[概念_LLM重排序]]、[[概念_分层知识蒸馏]]
- 实体：[[实体_Qwen3_Embedding]]、[[实体_Cohere_Rerank]]
- 来源：[[为什么用Qwen3_embedding和rerank]]、[[RAG_12痛点与解决方案]]、[[RAG挑战赛冠军方案]]、[[提升RAG问答质量的技术路线]]、[[优图RAG技术详解]]
