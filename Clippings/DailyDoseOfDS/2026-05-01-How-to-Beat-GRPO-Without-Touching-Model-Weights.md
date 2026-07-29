title: 无需修改模型权重：通过自然语言反思超越 GRPO (GEPA 算法详解) source: https://mail.google.com/mail/u/0/#inbox/19de58fc0d126e4b author:

"[[DailyDoseOfDS]]" published: 2026-05-01 created: 2026-07-28 description: 深入解析 GEPA 算法：将 5,000 Token 的采样轨迹喂给反思 LLM 迭代优化 Prompt，在复合 AI 系统上以 10-50 倍更少的计算量取得超越 GRPO 的效果。 tags:

clippings

# 无需修改模型权重：通过自然语言反思超越 GRPO (GEPA 算法详解)

在强化学习（RL）中，GRPO 需要数万次 Rollout 才能收敛。每次 Rollout 都会产生包含推理步骤、工具调用与自我修正的 5,000 Token 丰富轨迹，但 GRPO 却将这些丰富信息压缩成单一的标量 Reward 参与反向传播，丢弃了数千 Bit 的结构化诊断信号。

## GEPA（Generative Execution-guided Prompt Adaptation）核心思想

GEPA（发表于 ICLR 2026，现已成为 DSPy 的一级优化器）提出了全新的替代方案：不更新模型权重，而是直接让反思 LLM 阅读完整 Rollout 轨迹。

### 6 步优化算法循环

帕累托采样 (Pareto Sampling)：从提示词种群中挑选候选 Prompt（保留在至少一个子任务上表现最佳的 Prompt，避免陷入局部最优）。

选择变异模块：轮询选择复合系统中的某个模块（如 Multi-hop QA 中的检索词编写器）。

小批量采样：抽取 3 个训练样本。

运行 Rollout 并收集反馈：收集自然语言反馈函数 $\mu_f$ 返回的诊断信息（如缺失的实体、编译器报错等）。

自然语言反思 (Reflect)：将轨迹与诊断反馈喂给反思 LLM，生成新 Prompt。

接受/拒绝：重新运行测试，若性能提升则保留新 Prompt，否则丢弃。

## GEPA vs GRPO 对比
