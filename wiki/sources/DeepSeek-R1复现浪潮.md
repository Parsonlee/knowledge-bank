---
type: source
tags:
- LLM/reasoning
- LLM/training/RL
summary: 全球 UC伯克利/港科大/HuggingFace 等团队以极低成本成功复现 DeepSeek-R1-Zero，验证纯 RL 涌现推理能力
sources:
- raw/DeepSeek-R1复现.md
created: '2026-06-29'
updated: '2026-07-01'
confidence: high
---
## 来源信息

- **标题**：全球掀DeepSeek复现狂潮！硅谷巨头神话崩塌，30刀见证啊哈时刻
- **作者**：新智元编辑部
- **URL**：https://mp.weixin.qq.com/s/_yrzvSzzE6g3qBzVEk1q-Q

## 核心要点

- **TinyZero**（UC伯克利潘家怡等）：在 CountDown 游戏任务上复现 R1-Zero，3B 基础模型纯 RL，成本不到 30 美元，验证了自我验证和搜索能力的涌现
  - 0.5B 模型只猜解不验证；1.5B 起可学会搜索、自我验证和修正
  - 额外 SFT 并非必须，印证了 R1-Zero 设计决策
  - PPO/GRPO/PRIME 等不同 RL 算法均能涌现长 CoT，具体算法不关键
  - 推理行为与任务强相关：CountDown 任务学搜索验证，乘法任务学分布律分解
- **SimpleRL**（港科大何俊贤团队）：仅用 8K MATH 数据在 Qwen2.5-Math-7B 基础模型上做纯 PPO，无 SFT 无奖励模型
  - AIME 33.3%、AMC 62.5%、MATH 77.2%，超越 Qwen2.5-Math-7B-Instruct
  - 媲美使用 50 倍数据的 PRIME 和 rStar-MATH
  - 第 44 步出现「顿悟时刻」，自我反思自发出现
  - 训练动态：输出长度先减（消除代码模式）后增（自我反思涌现）
  - SimpleRL（Long CoT SFT 冷启动 + RL）比 SimpleRL-Zero（纯 RL）平均提升 6.9 个百分点
- **Open R1**（HuggingFace）：官宣复刻全套 pipeline，三步骤：R1-Distill 复现 → R1-Zero 纯 RL 复现 → 多阶段训练
- LeCun 评价："这一次，正是开源对闭源的胜利"

## 关联

- [[概念_GRPO强化学习]] — GRPO 算法
- [[概念_RLVR]] — 可验证奖励 RL
- [[实体_DeepSeek-R1]] — 被复现的原始模型
- [[实体_TinyZero]] — UC伯克利复现项目
- [[实体_SimpleRL]] — 港科大复现项目
- [[实体_Open_R1]] — HuggingFace 复现项目
- [[DeepSeek-R1工作原理]] — 原始论文解读

---
> 📎 **物理文献**：[[raw/DeepSeek-R1复现.md]]
