title: 为什么单纯使用小模型无法降低推理成本：SIE 共享 GPU 架构 source: https://mail.google.com/mail/u/0/#inbox/19f6784a03ed6e1e author:


* "[[DailyDoseOfDS]]" published: 2026-07-15 created: 2026-07-28 description: 拆分大模型为多个小模型（OCR、Embedding、Rerank、LLM）后，传统工具强制“一卡一模型”导致 GPU 严重空闲；剖析 SIE 推理引擎的 GPU 共享解法。 tags:
* clippings


________________


为什么单纯使用小模型无法降低推理成本：SIE 共享 GPU 架构
在生产环境中，团队倾向于将复杂的 AI 流水线拆解为多个专用小模型（如文本解析、Embedding 向量化、Cross-encoder 重排、实体提取和安全审核），以替代昂贵的前沿大模型。


然而，使用更便宜的模型并不等于使用更便宜的系统。
传统部署的卡顿根源：工具链割裂
GPU 租赁是按墙上时钟时间（Wall-clock time）按小时计费的。若将 4 个小模型部署在 4 张 GPU 上，总账单就是 4 张卡的租金和。


理论上一张 24GB 显存的 NVIDIA L4 完全能放下这 4 个小模型，但传统工具（如 vLLM 默认占 90% 显存、TEI 仅支持单模型）强制“一卡一模型/一进程一卡”。若在一张卡上强行开 4 个服务进程，因缺乏全局显存协调，任意模型的激活值（Activation）突发增长都会导致整张显卡 Out-Of-Memory (OOM)。


常见的避坑尝试：


1. 托管 API：随用量线性增长，无法私有化部署且存在数据隐私隐患；
2. Serverless GPU：冷启动（Cold Start）拉取数 GB 权重需耗时数秒，无法满足 Reranker 等实时链路。
解决方案：Superlinked Inference Engine (SIE)
开源推理引擎 SIE 打破了“单模型独占 GPU”的假设：


* 单 API 统一管理：一个服务同时暴露 encode、score、extract 和 generate 四种接口；
* 按计算成本动态 Batching：按请求长度归类填充，避免按全局最大长度 Padding 造成的算力浪费；
* 模型 LRU 加载与驱逐：类似于浏览器 Cache，根据流量动态在 GPU 显存中加载/卸载模型；
* 全局队列网关：网关层统一接收请求并调度到共享 Worker 线程，实现多模型高密并行，直接降低 75% 硬件账单。