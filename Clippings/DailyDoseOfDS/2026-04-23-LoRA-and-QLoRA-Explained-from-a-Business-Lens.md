title: 从商业与工程角度看 LoRA 与 QLoRA 大模型微调技术 source: https://mail.google.com/mail/u/0/#inbox/19dbca56ab454b95 author:


* "[[DailyDoseOfDS]]" published: 2026-04-23 created: 2026-07-28 description: 为什么 OpenAI 无法为每个用户维护一份 175B 的 GPT-3？从计算存储成本、多租户热插拔等商业视角深度解析 LoRA/QLoRA 的低秩分解原理。 tags:
* clippings


________________


从商业与工程角度看 LoRA 与 QLoRA 大模型微调技术
全参数微调一个 175B 参数的 GPT-3，仅 FP16 权重就需要 350GB 显存。


如果 OpenAI 为 10 万个微调用户各维护一份全量模型，将需要 3,500 万 GB 的存储空间，且无法在内存中常驻所有模型。
LoRA（Low-Rank Adaptation）的商业与技术解法
LoRA 冻结原始权重矩阵 $W (d \times d)$，引入两个低秩矩阵 $A (d \times r)$ 和 $B (r \times d)$，其中 $r \ll d$（通常 $r=8$）。
优势：
1. 显存与存储剧降：每个用户的 LoRA 适配器权重仅约 20-25 MB。
2. 多租户热插拔：OpenAI / 部署服务只需在 GPU 中常驻一份基座模型，在收到请求时将轻量级 LoRA 矩阵与基座权重实时相加（$\Delta W = B \times A$），即可瞬间切换不同用户的定制模型。
3. QLoRA 进一步压缩：通过 NF4（NormalFloat4）数据类型量化基座模型，配合双重量化（Double Quantization）与分页优化器（Paged Optimizers），使得单张消费级 GPU 即可完成 70B 模型的微调。