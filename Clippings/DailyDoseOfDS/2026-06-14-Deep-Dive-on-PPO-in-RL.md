title: "强化学习中的近端策略优化（PPO）算法深度剖析" source: "https://mail.google.com/mail/u/0/#inbox/19ec7f0bdd27389b" author:


* "[[DailyDoseOfDS]]" published: "2026-06-14" created: "2026-07-28" description: "详细拆解大模型对齐与 RLHF 的基石算法 PPO，涵盖信任域限制、Clipped Surrogate 目标函数以及从零实现的完整逻辑。" tags:
* clippings


________________


强化学习中的近端策略优化（PPO）算法深度剖析
PPO（Proximal Policy Optimization）是现代 LLM 对齐与 RLHF 的奠基算法。ChatGPT 的 RLHF 正是构建在 PPO 之上，后续出现的 DPO、GRPO 等算法均为针对 PPO 的改进或替代方案。
PPO 的核心要点：
* 为什么策略更新过大导致崩溃：缺乏约束的梯度更新容易让 Policy 跌入无法恢复的低劣区域。
* 信任域（Trust Region）与 Clipped Objective：通过截断（Clipping）目标函数限制新旧策略的比率，确保更新平滑安全。
* KL 散度惩罚：在 LLM 对齐中引入 KL 惩罚，防止模型偏离初始预训练模型的分布。
* 从零实现与训练诊断：使用 PyTorch 在 LunarLander 环境中训练，并监控不健康训练状态的诊断指标。