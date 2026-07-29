title: 多 GPU 模型训练的 4 种核心策略 source: https://mail.google.com/mail/u/0/#inbox/19e13d76eb927af3 author:

"[[DailyDoseOfDS]]" published: 2026-05-10 created: 2026-07-28 description: 对比模型并行、张量并行、流水线并行与数据并行 4 种分布式深度学习训练策略的技术细节与适用场景。 tags:

clippings

# 多 GPU 模型训练的 4 种核心策略

当单张 GPU 显存无法容纳大模型训练时，需要将计算分发至多卡：

模型并行（Model Parallelism）：将模型不同层分配到不同 GPU，解决单卡装不下的问题。

张量并行（Tensor Parallelism）：将单层矩阵乘法切分到多个 GPU 上并行计算（如 Megatron-LM）。

流水线并行（Pipeline Parallelism）：按层切分并按 Micro-batch 流水线交替计算，减少 GPU 空闲等待（Bubble）。

数据并行（Data Parallelism / DDP / ZeRO）：每张卡复制完整模型，切分 Batch 数据，最后同步梯度。
