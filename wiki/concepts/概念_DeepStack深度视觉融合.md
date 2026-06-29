---
type: concept
tags:
  - LLM/arch/VLM
summary: "DeepStack：Qwen3-VL 的多层次视觉特征注入技术，从 ViT 多个中间层提取特征，注入 LLM 解码器前几层，实现深度视觉-语言融合"
created: "2026-06-29"
updated: "2026-06-29"
---

# 概念：DeepStack 深度视觉融合

DeepStack 是 Qwen3-VL 的核心架构创新，将传统的"视觉信息一次性注入 LLM 输入层"升级为"多层次持续注入"。

## 原理

```
ViT 编码器
 ├── 第8层特征  ──→ 注入 LLM Block 1
 ├── 第16层特征 ──→ 注入 LLM Block 3
 └── 第24层特征 ──→ 注入 LLM Block ...
```

传统 MLLM：ViT 最后一层 → 连接器 → LLM 输入层（仅一次）
DeepStack：ViT 多个中间层 → 注入 LLM 不同深度的浅层（持续多次）

## 设计理论依据

- LLM 的浅层更适合处理视觉信息（有实验数据支撑）
- 信息层次匹配：LLM 浅层（基础特征）匹配 ViT 中间层（相对不抽象的视觉特征）

## Qwen3-VL 的优化实现

相比原始 DeepStack 论文，Qwen3-VL 更高效：
- **无需额外处理高分辨率图像**：直接从处理标准输入的同一个 Vision Tower 中提取指定中间层（如第8、16、24层）特征
- 代码实现：新增 `deepstack_merger_list` 模块
- 核心操作：**原地加法（in-place addition）**，计算开销极小

## 与其他方案对比

| 方案 | 融合方式 | 代表模型 |
|------|---------|---------|
| 简单拼接 | 输入端一次性 | LLaVA 1.0/1.5 |
| AnyRes | 输入端多分辨率 | LLaVA-OneVision |
| DeepStack | 内部多层注入（深度） | Qwen3-VL |
| 多专家融合 | 内部多专家并行（广度） | MouSi |

## 参见

- [[概念_MLLM三位一体架构]]
- [[概念_AnyRes高分辨率处理]]
- [[从LLaVA到Qwen3-VL_多模态架构演进]]
- [[实体_Qwen3-VL]]
