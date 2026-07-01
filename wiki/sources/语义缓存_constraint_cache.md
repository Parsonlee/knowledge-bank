---
type: source
tags:
- LLM/inference
summary: constraint-cache：通过确定性语义规范化将相似查询映射为同一缓存键，实现 99.9% 缓存命中率和毫秒级响应
sources:
- Cubox/让本地大模型不再重复推理的缓存技巧-2025-11-04.md
created: '2026-06-29'
updated: '2026-07-01'
confidence: high
---
## 来源信息

- 标题：让本地大模型不再重复推理的缓存技巧
- URL：https://mp.weixin.qq.com/s/quJt33cOZhK0B38nnfWflQ
- 项目：https://github.com/BitUnwiseOperator/constraint-cache

## 核心要点

- 问题：传统缓存对"怎么退款"和"如何申请退货"视为不同查询，每次重新推理
- 核心思路：**确定性规范化算法**——提取查询中的实体和动作，组合成标准化意图标识符
  - "cancel my order #12345" → "cancel_order"
  - "I want to cancel #67890" → "cancel_order"（相同键值）
  - "how do I cancel" → "cancel_order"（相同键值）
- 缓存的是**通用指令**（如"如何取消订单：访问账户>订单>点击取消"），而非具体订单信息，既安全又实用
- 实测（27,000条客服对话）：首次查询正常推理，后续相似查询直接返回缓存；最终达到 **99.9% 缓存命中率**，成本降低 99.9%，响应时间从几秒 → 1毫秒
- 技术底层：基于 Redis 标准缓存
- 强调"确定性"：相同查询总是得到相同结果，避免随机性响应，适合生产环境
- 适用场景：客服机器人、知识库问答等重复查询多的场景

## 关联

- [[概念_语义缓存]] — 语义相似查询归一化缓存
- [[概念_KV_Cache]] — 模型内部的 KV 推理缓存（与本文应用层缓存互补）
- [[概念_推测解码]] — 另一类推理加速方向
