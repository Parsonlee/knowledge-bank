title: 大语言模型（LLM）文本生成的 4 种解码策略 source: https://mail.google.com/mail/u/0/#inbox/19f3d7ecdb9a83ee author:

"[[DailyDoseOfDS]]" published: 2026-07-07 created: 2026-07-28 description: 总结大模型逐 Token 生成时的 4 种主流解码策略：Greedy Search、Multinomial Sampling、Beam Search 和 Contrastive Search。 tags:

clippings

# 大语言模型（LLM）文本生成的 4 种解码策略

大模型在生成回复时是逐 Token 预测概率分布的，如何从概率向量中选择目标 Token 决定了输出的风格与质量。

## 4 种核心解码策略

Greedy Strategy（贪心搜索）：每一步直接选择概率最高的 Token。简单但容易产生重复循环。

Multinomial Sampling（多项式采样）：按概率分布随机采样，配合 Temperature（温度）控制随机性，提升回复多样性。

Beam Search（束搜索）：在每一步保留前 $k$ 个高概率候选序列（Beam），全局寻找序列累计概率最大化。常用于机器翻译等追求准确性的任务。

Contrastive Search（对比搜索）：在选择 Candidate 时加上惩罚项——若候选 Token 与已生成文本过分相似则降权，兼顾流畅度与多样性，非常适合小说与长文创作。
