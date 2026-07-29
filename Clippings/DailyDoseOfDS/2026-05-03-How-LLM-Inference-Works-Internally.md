title: 大语言模型（LLM）内部推理工作原理：Prefill 与 Decode 阶段详解 source: https://mail.google.com/mail/u/0/#inbox/19deeeb458239986 author:


* "[[DailyDoseOfDS]]" published: 2026-05-03 created: 2026-07-28 description: 深入解析 LLM 推理的两个计算阶段：Compute-bound 的 Prefill 阶段（首 Token 延迟 TTFT）与 Memory-bound 的 Decode 阶段（Token 间延迟 ITL），以及 KV Cache 架构演进。 tags:
* clippings


________________


大语言模型（LLM）内部推理工作原理：Prefill 与 Decode 阶段详解
每次调用 LLM 的 generate() 函数时，GPU 上都会运行两个截然不同的计算阶段：
1. Prefill（预填充阶段）：算力受限 (Compute-bound)
* 任务：并行处理输入的 Prompt 所有 Token，计算 Q、K、V 矩阵并运行 Self-attention。
* 特点：充分利用 GPU 的算力矩阵乘法单元（Tensor Cores），算力利用率高。
* 关键指标：首 Token 延迟（Time to First Token, TTFT）。
* 产物：填充 KV Cache，将每个 Transformer 层的 K 和 V 张量保存在 GPU 显存中供后续复用。
2. Decode（解码阶段）：显存带宽受限 (Memory-bound)
* 任务：逐个生成输出 Token。每一步仅计算当前新 Token 的 Q、K、V，并关注历史所有 Token 的 cached K/V。
* 特点：单步计算量极小（向量与矩阵乘法），但每生成一个 Token 都需要将庞大的模型权重和整个 KV Cache 从 HBM（高带宽显存）重新加载一遍，导致 GPU 算力闲置，瓶颈在于显存带宽。
* 关键指标：Token 间延迟（Inter-Token Latency, ITL）。
KV Cache 的成本与架构演进
KV Cache 避免了每生成一个 Token 都要对全序列重新计算 Attention 的二次方复杂度问题，将推理加速 5 倍以上。但其体积随序列长度线性增长：


* 对于 13B 模型，每个 Token 消耗约 1MB 显存。4K 上下文仅 KV Cache 就占用 4GB 显存。
* 前沿解决方案：除了 INT8/INT4 缓存量化和 PagedAttention（vLLM 内存分页管理）外，DeepSeek-V4 等架构通过 Compressed Sparse Attention (CSA) 与 Heavily Compressed Attention (HCA) 从结构上重构 Attention，使 1M 上下文下的 KV Cache 减少 90%。