title: Paged Attention：解决大模型推理 KV Cache 内存瓶颈 source: https://mail.google.com/mail/u/0/#inbox/19f721c214ca5038 author:

"[[DailyDoseOfDS]]" published: 2026-07-17 created: 2026-07-28 description: 借用操作系统虚拟内存分页思想，Paged Attention 将 KV Cache 切分为固定大小块，解决内存碎片化与连续空间预分配浪费，提高 2-4x 吞吐量。 tags:

clippings

# Paged Attention：解决大模型推理 KV Cache 内存瓶颈

在大模型大规模 Serving 部署时，显存往往先于计算力成为瓶颈。传统 KV Cache 实现为每个请求预分配大块连续显存（例如预留 2048 个 Token 空间），但实际平均生成仅 200 Token，导致 70%~80% 的显存因碎片化与过度预留而被浪费。

## Paged Attention 的核心设计

Paged Attention 借鉴了操作系统中的**虚拟内存分页（Virtual Paging Memory）**机制：

块级分配（Block-level Allocation）：将 KV Cache 切分为固定大小的物理块（通常为 16 个 Token 一块），块在 GPU 显存中无需连续。

页表映射（Block Table）：每个请求维护一个页表，将逻辑 Token 索引动态映射到离散的物理显存块上。

共享 Prefix 缓存：多个共享相同 System Prompt 的请求可直接复用同一物理显存块，直到输出分叉时才写时复制（Copy-on-Write）。

凭借该机制，vLLM、TensorRT-LLM 和 SGLang 实现了 2-4 倍的系统吞吐量提升，并将显存浪费降至近乎为零。
