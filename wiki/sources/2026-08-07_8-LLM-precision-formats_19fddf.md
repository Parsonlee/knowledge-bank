---
type: "source"
tags: ["LLM/inference", "LLM/training", "Infra/gpu"]
summary: "梳理 FP32、TF32、BF16、FP16、FP8、INT8、INT4 与 NF4 八类 LLM 数值格式，以及它们在训练和推理中的显存、范围、精度与速度权衡。"
sources: ["raw/articles/2026-08-07_8-LLM-precision-formats_19fddf.md"]
updated: "2026-08-10"
---

# 八种 LLM 精度格式

## 来源信息

- 标题：8 LLM precision formats
- 作者：Avi Chawla / Daily Dose of Data Science
- 日期：2026-08-07
- URL：https://www.dailydoseofds.com/p/5-llm-quantization-techniques/

## 核心要点

- [原文陈述] 低于 FP32 的格式都在数值细节与显存之间取舍。以 7B 模型为例，文章称 FP32 权重约需 28GB；Ollama 默认的 Q4_K_M GGUF 平均约 4.8 bit/权重，使其约为 4.1GB。
- [原文陈述] FP32 有 8 位指数和 23 位尾数；TF32 保留 FP32 的 8 位指数、采用 10 位尾数，且仅在 Tensor Core 的乘法过程中使用，因此不会降低权重存储的显存占用。
- [原文陈述] BF16 保留 FP32 的指数范围但仅有 7 位尾数，适合预训练；FP16 为 5 位指数、10 位尾数，表示范围较小，训练中需依赖 loss scaling 处理溢出风险。
- [原文陈述] FP8 的 E4M3 与 E5M2 分别更适合权重/激活和梯度；由于数值范围更窄，按张量或按块的缩放因子成为必要条件。
- [原文陈述] INT8 按校准范围将权重映射至 256 个等距等级；INT4 只有 16 个等级，GPTQ 通过逐权重处理并补偿后续权重误差，AWQ 则放大高信号通道，二者都依赖校准数据。
- [原文陈述] NF4 也是 16 个等级，但按接近零中心高斯分布的预训练权重非均匀布置；在 [[概念_LoRA与QLoRA显存]] 中，冻结基座以 NF4 存储、LoRA 适配器以 BF16 训练，计算时仍会反量化到 BF16。

## 关联实体与概念

- [[概念_量化]]：INT8、INT4、NF4 等低位宽表示的共同框架。
- [[概念_混合精度训练]]：FP32、BF16、FP16 与低精度计算在训练中的协同。
- [[概念_LoRA与QLoRA显存]]：NF4 与 BF16 在 QLoRA 中的具体组合。
- [[实体_vLLM]]：文中将其作为采用 4-bit 格式的常见推理生态之一。

> 📎 **物理文献**：[[raw/articles/2026-08-07_8-LLM-precision-formats_19fddf.md]]
