---
type: concept
tags:
  - LLM/training/post-train
  - DeepLearning
created: "2026-06-29"
updated: "2026-06-29"
---

# 概念：Forward KL 与 Reverse KL

## 定义

- **Forward KL**（正向 KL 散度）：KL(目标分布 || 模型分布），最小化时模型要"覆盖"目标分布的全部区域，即 **mode-covering**
- **Reverse KL**（反向 KL 散度）：KL(模型分布 || 目标分布），最小化时模型倾向"选择"目标分布中最可能的部分，即 **mode-seeking**

## 在 SFT 与 RL 中的对应

- **SFT** 最小化 Forward KL：尽量覆盖所有目标分布区域（"包住所有山峰"）
- **RL** 最小化 Reverse KL：专注目标分布中最可能的部分（"爬到最高峰"）

## 对遗忘的影响

- 直觉上认为 RL（reverse KL）更激进、更容易遗忘旧模式
- 但在真实 LLM 实验中，多峰分布场景下：SFT 的 forward KL 为覆盖新目标而拉扯旧峰质量，RL 的 reverse KL 直接平移新峰而不动旧峰
- **结论：KL 方向并非遗忘的决定性因素，on-policy 数据分布才是关键**

## 关联

- [[后训练认知_SFT_vs_RL_记忆与遗忘机制]]
- [[概念_灾难性遗忘]]
- [[概念_on-policy与off-policy数据]]
