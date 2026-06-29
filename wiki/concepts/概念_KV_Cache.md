---
type: concept
tags: ["LLM/inference"]
summary: "Transformer 推理时缓存已计算的 Key 和 Value 矩阵以避免重复计算，是推理显存的主要消耗项"
sources: ["Cubox/[LLM]大模型显存计算公式与优化 - 知乎-2025-05-06.md"]
created: "2026-06-26"
updated: "2026-06-26"
confidence: high
---

# KV Cache

## 定义

KV Cache（Key-Value Cache）是 Transformer 模型在自回归推理过程中，将已计算的注意力层 Key 和 Value 张量缓存在显存中的技术。每生成一个新 token 时，只需计算当前 token 的 Q/K/V 并与缓存拼接，避免对所有历史 token 重复计算。

## 显存计算公式

```
KV Cache 显存 = 2 × batch_size × seq_len × num_layers × hidden_size × dtype_bytes
```

- `2`：Key 和 Value 各一份
- `batch_size`：并发请求数
- `seq_len`：已生成的序列长度（随生成逐步增长）
- `num_layers`：Transformer 层数
- `hidden_size`：隐藏层维度
- `dtype_bytes`：数据类型字节数（FP16 = 2，FP32 = 4）

## 为什么是瓶颈

- KV Cache 随序列长度线性增长，长文本场景下可能超过模型参数本身的显存占用
- 多用户并发时 batch_size 放大，显存需求成倍增加
- 制约了最大可服务的上下文长度和并发数

## 优化方法

- **量化**：将 KV Cache 从 FP16 量化到 INT8/INT4，减半或减至 1/4
- **分页管理**：如 vLLM 的 PagedAttention，按页分配避免碎片浪费
- **MQA / GQA**：Multi-Query Attention / Grouped-Query Attention 减少 K/V head 数
- **滑动窗口**：限制有效上下文长度（如 Mistral 的 sliding window attention）

## 关联

- [[概念_显存估算公式|显存估算公式]]
- [[概念_模型并行|模型并行]]
- 来源：[[大模型显存计算与优化]]
