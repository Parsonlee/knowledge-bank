title: 强化学习深度剖析：PPO 算法详解与代码实现 source: https://mail.google.com/mail/u/0/#inbox/19ec7f0bdd27389b author:


* "[[DailyDoseOfDS]]" published: 2026-06-14 created: 2026-07-28 description: 详解 ChatGPT 对齐基石 PPO（Proximal Policy Optimization）算法，涵盖 Trust Region 置信域、Clipped Loss 目标函数与 PyTorch 实现。 tags:
* clippings


________________


强化学习深度剖析：PPO 算法详解与代码实现
PPO（Proximal Policy Optimization）是大模型 RLHF 对齐以及机器人控制中最核心的强化学习算法。DPO 与 GRPO 均是以 PPO 为基准改良而来的。
PPO 的核心原理
1. 防止策略崩溃（Irreversible Collapse）：传统的 Policy Gradient 在更新步长过大时容易导致策略彻底失效。
2. Clipped Surrogate Objective（裁剪代理目标）：通过限制新旧策略概率比率 $\frac{\pi_\theta(a|s)}{\pi_{\theta_{old}}(a|s)}$ 在 $[1-\epsilon, 1+\epsilon]$ 之间，确保更新幅度在安全的置信域（Trust Region）内。
3. KL 散度惩罚：在 LLM 场景中，加入与冻结 Reference Model 的 KL 散度惩罚，防止模型生成退化。