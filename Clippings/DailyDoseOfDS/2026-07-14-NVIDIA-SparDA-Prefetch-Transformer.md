title: 英伟达与麻省理工 SparDA 预取 Transformer 架构 source: https://mail.google.com/mail/u/0/#inbox/19f6174c7b5adc67 author:


* "[[DailyDoseOfDS]]" published: 2026-07-14 created: 2026-07-28 description: NVIDIA 与 MIT 提出 SparDA 架构，在 Q、K、V 外新增 Forecast 预测投影，实现 CPU 到 GPU 的 KV Block 提前并行拉取，解码速度提升 1.7 倍。 tags:
* clippings


________________


英伟达与麻省理工 SparDA 预取 Transformer 架构
NVIDIA 与 MIT 联合发表的 SparDA 论文提出了一种全新的 Transformer 变体，通过极小的架构改动实现了解码速度 1.7 倍提升，长文本推理准确率提升 6.5 分。
传统稀疏注意力（Sparse Attention）的瓶颈
在 100K+ 超长上下文推理中，完整的 KV Cache 无法全部容纳在 GPU 显存中，必须 Offload 到 CPU RAM。


1. 传输停顿：当前层需要根据查询向量 $Q$ 挑选 Top-K 块，但 $Q$ 只有在当前层运行时才生成，导致 GPU 必须停顿等待 KV Block 从 CPU 拷贝回 GPU 显存；
2. 选择开销：传统选择器需将每个 Query Head 与候选块逐一计算得分并取 Softmax，计算量随上下文呈指数级增长。
SparDA 的解耦设计：四投影架构
SparDA 在每个 Attention 层中增加第 4 个投影：$Q, K, V$ 以及 Forecast（预测）。


* 第 $L$ 层的 Forecast 能够在当前层计算的同时，预判第 $L+1$ 层需要的 KV 块；
* 运行时在独立的 CUDA Stream 上提前将第 $L+1$ 层所需的 KV 块从 CPU 内存异步 Fetch 到 GPU 显存，使内存拷贝与 GPU 计算重叠（Overlap）；
* Forecast 无需多头布局，每个 GQA 组仅需 1 个 Forecast Head，完全跳过了 Softmax 步骤。
性能表现
Forecast 投影仅增加 0.41% 参数（8B 模型增加 33.5M 参数），在 MiniCPM4.1-8B 和 NOSA-8B 上 Prefill 加速 1.25x，Decode 加速 1.7x；在 CPU Offload 模式下解码吞吐量提升高达 5.3 倍。