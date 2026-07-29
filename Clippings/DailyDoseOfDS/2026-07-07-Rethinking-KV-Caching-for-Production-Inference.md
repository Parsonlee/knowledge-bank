title: 重构生产环境推理中的 KV 缓存：LMCache 解耦架构 source: https://mail.google.com/mail/u/0/#inbox/19f3d7ecdb9a83ee author:


* "[[DailyDoseOfDS]]" published: 2026-07-07 created: 2026-07-28 description: 斯坦福研究表明 Agent 请求中 62% 为重复上下文；解耦缓存管理与推理计算的开源架构 LMCache 实现首字延迟降低 14 倍，配合 CacheBlend 解决多文档 RAG 缓存失效问题。 tags:
* clippings


________________


重构生产环境推理中的 KV 缓存：LMCache 解耦架构
斯坦福研究表明，在 AI Agent 的推理预算中，约 62% 的 Token 是重复的系统 Prompt、工具定义和文档。随着 Agent 步数增多，单任务 Token 消耗达到了普通 Chatbot 的 5~30 倍。
前缀缓存（Prefix Caching）的局限
虽然 Prompt Caching 能减少重复前缀开销，但存在严格的前缀匹配门槛：


* 多文档 RAG：同时引用文档 A 和 B 时，单独缓存的 A/B KV 状态失效；
* 文档顺序调整：相同文档改变排列顺序即导致 Cache Miss；
* 多轮对话增长：前缀后的任何微小改动都会使后续缓存失效。


此外，传统 KV Cache 管理运行在推理引擎进程内部，I/O 操作与矩阵计算抢占资源，像 TurboQuant 这类压缩算法反而会导致 20%+ 的推理变慢。
LMCache 解耦架构
开源项目 LMCache 将缓存管理移出推理引擎，作为独立进程运行：


1. 无资源争用：缓存 I/O（GPU/CPU/SSD 间传输）与 GPU 矩阵计算完全分离；
2. 跨 GPU 零拷贝共享：多 GPU 可直接读写共享内存区域；
3. 多层级并行加载：同时检索 GPU、内存、本地 SSD 及远程存储并并行流式传输。


实测在 H200 上运行 Qwen3-235B（50 并发），LMCache 实现了 14 倍的首字延迟（TTFT）加速 和 4 倍解码加速。
CacheBlend：解决多文档组合缓存
获得 EuroSys 2025 最佳论文的 CacheBlend 算法进一步发现：Transformer 中绝大多数 Token 仅与局部上下文相关。针对多文档 RAG 场景，CacheBlend 仅选择性重算跨文档边界的极少数 Token，复用独立缓存，使多文档查询速度提升 2-4 倍。