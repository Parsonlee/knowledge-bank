# 概念_RAG反馈机制

> tags: RAG
> confidence: high

## 定义

RAG 反馈机制（Feedback Loop）是一种使 RAG 系统从静态变为动态自适应的策略。通过收集用户反馈，持续优化检索结果的相关性和回答质量。

## 核心能力

- **记忆功能**：记住哪些文档提供过有用信息
- **动态调整评分**：根据历史反馈更新文档相关性得分
- **知识积累**：将高质量 QA 对加入知识库
- **持续进化**：每次交互都是学习机会

## 实现流程

1. 用户提问，系统生成回答
2. 获取用户反馈（相关性 1-5、质量 1-5、评论）
3. 存储反馈数据（JSON 日志）
4. 下次查询时：
   - assess_feedback_relevance：LLM 判断历史反馈是否与当前查询相关
   - adjust_relevance_scores：相关反馈的平均评分作为 modifier 调整检索评分
5. 索引微调（fine_tune_index）：高质量 QA 对（relevance>=4, quality>=4）回注向量库，relevance_score=1.2 加权

## 评分调整公式

- modifier = 0.5 + (avg_relevance / 5.0)
- adjusted_score = original_score * modifier
- 反馈好(relevance=5) → modifier=1.5, 提升排名
- 反馈差(relevance=1) → modifier=0.7, 降低排名

## 关联

- 相关概念：[[概念_RAG基础流程]]、[[概念_检索后处理]]、[[概念_Adaptive-RAG]]
- 来源：[[RAG技巧与底层代码剖析]]
