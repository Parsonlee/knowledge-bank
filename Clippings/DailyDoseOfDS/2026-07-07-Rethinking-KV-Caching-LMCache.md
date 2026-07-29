title: 重新思考生产环境中的 KV Cache 管理：LMCache 架构 source: https://mail.google.com/mail/u/0/#inbox/19f3d7ecdb9a83ee author:

"[[DailyDoseOfDS]]" published: 2026-07-07 created: 2026-07-28 description: 斯坦福团队研究显示 Agent 62% 的 Token 为重复上下文；解耦式 KV Cache 框架 LMCache 将缓存管理移出推理引擎，实现 14x 首 Token 延迟缩短。 tags:

clippings

# 重新思考生产环境中的 KV Cache 管理：LMCache 架构

斯坦福大学研究表明：在 AI Agent 每次调用中，约 62% 的 Token 属于重复传入的上下文（如系统 Prompt、工具定义和文档）。这导致即使单 Token 价格下降，Agent 系统的总体账单依然飙升。

## 传统 Prefix Caching 的局限

传统的 Prompt Caching 要求缓存前缀必须是严格字节级匹配（Byte-for-byte prefix）。一旦多文档顺序改变、新增对话历史或变更前缀，缓存即彻底失效（Cache Miss）。

## LMCache 的解耦设计与 CacheBlend

开源项目 LMCache 将 KV Cache 管理从推理引擎进程中彻底解耦出来，作为独立进程运行：

零资源抢占：Cache I/O 与 GPU 矩阵计算并行，消除 20% 的引擎内耗。

跨 GPU 零拷贝共享：通过共享显存使多张 GPU 直接读写同一缓存区域。

CacheBlend 技术（EuroSys 2025 获奖论文）：针对 RAG 多文档组合场景，仅选择性重计算跨文档边界连接处少数 Token 的 KV，其余直接复用独立 Cache，使多文档查询速度提升 2-4 倍。

在 H200 GPU 与 Qwen3-235B 模型测试中，LMCache 实现了 14x 的首 Token 延迟（TTFT）缩短 与 4x 解码加速。
