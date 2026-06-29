---
type: concept
tags:
  - LLM/arch/Mamba
created: "2026-06-29"
updated: "2026-06-29"
confidence: medium
---

# State Swapping

Mamba 特有的推理范式：预先对专业数据集运行推理生成压缩 state，推理时直接注入，无需 few-shot 例子或微调。

## 原理

Mamba 的隐状态是对历史信息的压缩表示。可以：
1. 对专业语料（如物理教材 + 100 道例题）做一次前向推理，得到 state
2. 将该 state 保存并分发
3. 推理时直接将此 state 注入模型，再问短问题

## 优势

- 无需 backprop（与 fine-tuning 不同）
- 无需 few-shot 例子（与 in-context learning 不同）
- State 可无限复用，零推理成本
- 类似 LoRA 插件，可"下载"特定领域 state

## 对比传统方式

| 方式 | 成本 | 效果 |
|------|------|------|
| Few-shot prompting | 每次推理都消耗 token | 中 |
| Fine-tuning | 需要 GPU 训练 | 高 |
| RAG | 每次检索 | 中 |
| State Swapping | 一次生成，无限复用 | 中高 |

## 局限

目前仍是理论设想（Kola Ayonrinde 的观点），实际产品化尚未成熟。confidence: medium

## 来源

- [[Mamba_Explained_Kola_Ayonrinde]]
