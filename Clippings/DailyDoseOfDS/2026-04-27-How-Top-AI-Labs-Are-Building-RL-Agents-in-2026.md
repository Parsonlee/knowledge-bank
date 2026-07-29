title: 顶尖 AI 实验室 2026 年如何构建强化学习 Agent：从 RLVR、GRPO 到 RULER source: https://mail.google.com/mail/u/0/#inbox/19dd11ff55feb3f6 author:


* "[[DailyDoseOfDS]]" published: 2026-04-27 created: 2026-07-28 description: 全面解析 2026 年强化学习 Agent 的演进路线：从 PPO 的 4 模型架构到 DeepSeek-R1 的 RLVR+GRPO，再到 OpenPipe RULER 通用 LLM-as-Judge 相对排名奖励机制。 tags:
* clippings


________________


顶尖 AI 实验室 2026 年如何构建强化学习 Agent：从 RLVR、GRPO 到 RULER
强化学习在 LLM 领域经历了三次重大架构演进：
1. PPO 与传统 RLHF（4 模型时代）
早期的 InstructGPT / ChatGPT 依赖人类偏好排序，训练难度高，且需要在显存中同时维持 4 个全尺寸大模型：


* Policy（被训练的模型）
* Reference Policy（冻结的基准模型，用于 KL 散度正则化）
* Reward Model（拟合人类偏好的奖励模型）
* Critic / Value Model（评价当前状态预期收益的价值模型）
2. DeepSeek R1 与 RLVR + GRPO（2 模型时代）
2025 年初，DeepSeek R1 引入 RLVR（可验证奖励强化学习） 与 GRPO（组相对策略优化）：


* 去除了 Critic 模型：在同一 Prompt 下采样 16 条回复，直接利用组内均值和标准差归一化计算 Advantage。
* 去除了 Reward Model：数学问题用已知答案匹配，代码用编译器运行结果（0 或 1 奖励）。
* 成果：仅需 Policy 和 Reference 模型，DeepSeek R1-Zero 在 AIME 数学竞赛上从 15.6% 跃升至 77.9%。
3. 泛化 Agent 工作流的挑战与 RULER 解决方案
RLVR 在数学和代码等可客观验证的领域表现优异，但面对 RAG、客服、文档摘要等主观或多维度的 Agent 任务时，无法通过简单的字符串匹配得出二进制 Reward。
OpenPipe 的 RULER (Relative Universal LLM-as-a-Judge Evaluator and Ranker)
为了解决自定义 Python 奖励函数极易写错且脆弱的问题，RULER 提出了 LLM 相对排名机制：


1. 相对评分优于绝对评分：LLM 很难打出校准精准的绝对分，但在同一 Prompt 下对比 4-8 条轨迹并按质量排序非常准确。
2. 直接对接 GRPO：GRPO 本身就只需要组内相对排名。RULER 将系统 Prompt 作为评判标准，直接输出 0~1 的相对梯度得分。
3. 无需编写规则代码：修改系统 Prompt 后，RULER 的评判标准会自动自适应调整，无需重写任何 Reward 函数。