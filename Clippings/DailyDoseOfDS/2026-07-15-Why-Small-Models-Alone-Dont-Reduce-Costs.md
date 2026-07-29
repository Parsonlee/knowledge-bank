title: 为什么仅凭小模型（SLM）无法降低推理成本？ source: https://mail.google.com/mail/u/0/#inbox/19f6784a03ed6e1e author:

"[[DailyDoseOfDS]]" published: 2026-07-15 created: 2026-07-28 description: 剖析将大模型切分为多个专用小模型后，传统 Serving 框架强制一模型占用一 GPU 导致的显存闲置浪费，以及开源推理引擎 SIE 的多模型共享 GPU 解决方案。 tags:

clippings

# 为什么仅凭小模型（SLM）无法降低推理成本？

在生产环境中，团队越来越倾向于用精简的微调小模型（SLM）来替换昂贵的大模型，以处理文档解析、向量 Embedding、重排序（Reranking）和字段提取等重复任务。

然而，便宜的模型并不等于便宜的系统。GPU 租用是按墙上时钟（Wall-clock Time）按小时计费的，而不是按 FLOPs 计费。

如果一个管道包含 4 个小模型，但在现有框架（如 vLLM 或 TEI）下每个进程强制独占单张 GPU，那么系统的总硬件账单反而会增加 4 倍。

## 传统 Serving 框架的瓶颈

单进程独占：vLLM 和 TEI 均基于“一个模型独占一张 GPU”的假设构建。若在一张 GPU 上强行开启 4 个独立 Server 进程，无法进行跨进程显存协调与优先级调度。

预分配浪费：vLLM 启动时默认按 --gpu-memory-utilization 0.9 预留显存，多个进程极易引发 OOM（内存溢出）。

## 开源解决方案：Superlinked Inference Engine (SIE)

Superlinked Inference Engine（SIE）提供了一个能在单张 GPU 上协同运行多种不同架构模型（Embedding、Reranking、OCR、Extraction、Generation）的单一 Server 框架：

单一 API 统一入口：用 encode、score、extract 和 generate 覆盖 Agent 链条的全部模型需求。

基于 Compute 的 Batch 组装：按计算成本对不同长度请求动态打包，减少 Padding 填充损耗。

LRU 动态加载与淘汰：根据实时流量热度动态加载/换出模型，彻底消除闲置 GPU 显存占用。
