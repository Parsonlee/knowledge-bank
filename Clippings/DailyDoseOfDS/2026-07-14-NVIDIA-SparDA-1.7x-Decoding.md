title: NVIDIA SparDA：通过预测机制将 Transformer 解码速度提升 1.7x source: https://mail.google.com/mail/u/0/#inbox/19f6174c7b5adc67 author:


* "[[DailyDoseOfDS]]" published: 2026-07-14 created: 2026-07-28 description: NVIDIA 与 MIT 提出 SparDA 架构，在每层 Attention 中增加第四个 Forecast 投影，预判下一层所需 KV 块并在 CUDA 流中预取，实现 1.7x 解码加速。 tags:
* clippings


________________


NVIDIA SparDA：通过预测机制将 Transformer 解码速度提升 1.7x
在长上下文推理中，稀疏注意力（Sparse Attention）虽能筛选重要 KV 块，但面临两大瓶颈：


1. CPU 到 GPU 的传输停顿：100K+ 上下文下 KV Cache 需卸载至 CPU RAM，每层计算前必须同步拉取，导致 GPU 频繁空转等待。
2. 选择计算本身昂贵：需要用当前层的 Query 向量计算所有 Candidate 块得分。
SparDA 架构的创新
NVIDIA 与 MIT 提出的 SparDA 为每个 Attention 层增加了第四个投影头——Forecast（预测头）：


* 解耦预取：第 $L$ 层的 Forecast 向量提前预判第 $L+1$ 层所需的 KV 块。
* 异步 Overlap：当第 $L$ 层在 GPU 上计算时，系统已在独立 CUDA 流中将第 $L+1$ 层所需的 KV 块从 CPU 内存预取至 GPU，彻底掩盖传输延迟。
性能表现
在 8B 模型上，Forecast 参数仅增加 0.41%（33.5M），使 Prefill 速度提升 1.25x，解码速度提升 1.7x，并在长文本推理基准测试中获得 +6.5 分 的准确率提升。