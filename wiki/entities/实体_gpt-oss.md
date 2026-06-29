---
type: entity
tags:
  - LLM/arch/MoE
---

# 实体：gpt-oss

OpenAI 于 2025 年 8 月发布的首批开放权重模型（自 GPT-2 2019 年以来），Apache 2.0 许可证。来源：[[从GPT-2到gpt-oss_OpenAI开放模型进化之路]]

## 基本信息

- 模型：gpt-oss-20b 和 gpt-oss-120b
- 类型：推理模型（Reasoning Model），仅解码器 Transformer + MoE
- 许可证：Apache 2.0（可用于商业产品和蒸馏其他模型）
- 训练计算量：210 万 H100 GPU 小时（含 SFT + RL）
- 发布时间：2025 年 8 月

## 架构规格

| 规格 | gpt-oss-20b | gpt-oss-120b |
|------|-------------|--------------|
| Transformer 层 | 24 | 更多 |
| 嵌入维度 | 2880 | 2880 |
| 专家数量 | 32 | 更多 |
| 每 token 激活专家 | 4 | 4 |
| 注意力 | 交替 GQA + 滑动窗口（128 token） | 同左 |
| 位置编码 | RoPE | RoPE |
| 归一化 | RMSNorm | RMSNorm |
| 激活函数 | SwiGLU | SwiGLU |

## 量化与硬件要求

- MXFP4 量化版本：120b 可在单块 80GB H100 运行；20b 可在 16GB RTX 50 系列运行
- bfloat16 版本：20b 需 48GB，120b 需 240GB
- Mac Mini 上通过 ollama 运行 20b 约占 13.5GB 内存

## 特性

- 可通过系统提示词控制推理工作量（低/中/高），灵活平衡成本与准确率
- 注意力层含可学习 per-head bias logits 作为 attention sinks
- 模型卡注明幻觉倾向相对较高（训练过于侧重数学/代码推理任务）

## 关联

- [[概念_gpt-oss架构特征]] — 架构分析
- [[实体_Sebastian_Raschka]] — 技术博客分析作者
- [[概念_MoE混合专家]] — 核心架构组件
