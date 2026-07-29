title: 大语言模型（LLM）生成控制：7 种核心 Generation Parameters source: https://mail.google.com/mail/u/0/#inbox/19ec7f0bdd27389b author:


* "[[DailyDoseOfDS]]" published: 2026-06-14 created: 2026-07-28 description: 梳理控制大模型输出的核心参数：Max tokens、Temperature、Top-k、Top-p (Nucleus Sampling)、Frequency/Presence Penalty 与 Stop sequences。 tags:
* clippings


________________


大语言模型（LLM）生成控制：7 种核心 Generation Parameters
精准调节推理参数是控制大模型输出确定性与多样性的基础：


1. Max Tokens：设置单次生成的最大 Token 数量硬性上限。
2. Temperature（温度）：缩放 Logits 概率分布。趋近于 0 时生成极度确定，较高时提升多样性。
3. Top-k Sampling：仅在概率最高的前 $k$ 个 Token 集中进行采样。
4. Top-p Sampling (Nucleus Sampling)：动态选择累计概率达到 $p$（如 0.9）的最少 Token 集合。
5. Frequency Penalty（频率惩罚）：根据 Token 在已生成文本中出现的绝对频率进行扣分，有效惩罚重复词。
6. Presence Penalty（存在惩罚）：只要 Token 在已生成文本中出现过即施加固定惩罚，鼓励模型引入新话题。
7. Stop Sequences：遇到指定 Token 序列（如 \n\n 或 }）时立即截断并停止生成。