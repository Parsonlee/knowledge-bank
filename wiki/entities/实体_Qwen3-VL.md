---
type: entity
tags:
  - LLM/arch/VLM
summary: "阿里巴巴 Qwen 团队的深度融合多模态大模型，核心创新为 DeepStack 多层视觉特征注入 + MoE + MRoPE-Interleave，支持超高分辨率图像和视频"
created: "2026-06-29"
updated: "2026-06-29"
---

# 实体：Qwen3-VL

## 基本信息

- **机构**：阿里巴巴 Qwen 团队
- **类型**：多模态大语言模型
- **开源**：是

## 核心架构创新

### DeepStack
- ViT 多个中间层（第 8、16、24 层）提取特征
- 精准注入 LLM 解码器前几层（原地加法实现）
- 代码模块：`deepstack_merger_list` + `_deepstack_process`

### MoE 语言模型
- 语言模型升级为 `Qwen3VLMoeTextModel`（含 `Qwen3VLMoeTextSparseMoeBlock`）

### MRoPE-Interleave
- 交错 t/h/w 三维频率的多维旋转位置编码
- 增强视频时空感知

### 文本时间戳对齐
- 视频帧与精确时间戳文本（如 `<0.8 seconds>`）在输入端绑定

## 与 Qwen2.5-VL 的代码差异

| 组件 | Qwen2.5-VL | Qwen3-VL |
|------|-----------|---------|
| 视觉融合 | 输入端拼接 | DeepStack 多层注入 |
| 语言模型 | Dense | MoE |
| 位置编码 | MRoPE | MRoPE-Interleave |

## 参见

- [[从LLaVA到Qwen3-VL_多模态架构演进]]
- [[概念_DeepStack深度视觉融合]]
- [[概念_MLLM三位一体架构]]
- [[实体_LLaVA]]
