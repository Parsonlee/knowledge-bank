---
title: Agent Loop使用语义早停比max_iterations硬截断节省38% Token 且质量不降
source: https://mp.weixin.qq.com/s/QUhztozEmydtvUDUXK8jsA
author:
  - "[[南七技校]]"
published:
created: 2026-06-29
description: Loop engineering之语义早停法
tags:
  - AI-Agent/loop-engineering
---
南七技校 AgenticHub *2026年6月29日 08:46*

大家好！我是南七技校1111，专注 AI Agent 落地与模型前沿。校友评论区集合。

“你写了一个 Writer→Critic 循环。Writer 起草答案，Critic 审阅给反馈，Writer 修改——来回几轮，质量越来越好。然后你设了一个 `max_iterations=6` ，跑满就停。”

**问题在哪？**

简单的问题，第 1 轮就出好答案了，但循环硬跑到第 6 轮——白白烧了 5 轮 token。难的问题，6 轮还没写完，循环一刀切断了——答案半成品就交出去了。最要命的是：第 4、5、6 轮输出本质上说的是同一件事，但计数器看不见——它只数迭代序号，不看内容。

Sahil Shrivastava 在 6 月 25 日提交到 arXiv 的单人论文里，把这个问题概括成一句话：

> "The stopping decision is made on the iteration index, never on what was actually written."  
> 终止决策基于迭代序号，从来不看实际写了什么。

他提出的方案叫语义早停（Semantic Early-Stopping）：不看迭代次数，看答案还在不在变。

\## ① 两个信号 + 四级级联：语义早停怎么判断"该停了"

语义早停的核心是两条信号通路，一条免费，一条付费。

![图片](https://mmbiz.qpic.cn/mmbiz_png/Cic4GFNZLlxph4zgQv5Y88I4XHbZSKTqCIn1yyFCynAzRyiaowlVZYQ9CicuibcxVsrJiapIic8bnSg6XThyFfwiar1jrhbJI3ItxxlzcFW5nvyjao/640?wx_fmt=png&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1\#imgIndex=0)

**几何信号 dₜ——免费。** ==每轮把 Writer 的输出用本地 sentence embedding 模型（论文用的是 sentence-transformers）转成向量，算相邻两轮的余弦距离：dₜ = 1 − cos(eₜ, eₜ₋₁)。当连续 k 轮 dₜ < ε（默认 0.06），说明答案在语义上已经收敛——再跑下去是 churn，不是 improvement。这个信号完全本地计算，不调任何 API，零成本。==

**质量信号 ISₜ——付费。** 用 RAGAS 四维指标（faithfulness / answer relevancy / context precision / context recall）加权求和，每轮调一次 LLM judge 打分。保证"收敛"不等于"收敛到一个烂答案"。

这两个信号按优先级组成四级终止级联：

1. 1\. Critic 显式批准 → 停
2. 2\. 连续 k 轮 dₜ < ε → 语义收敛，停
3. 3\. IS 不再提升（ΔIS ≤ 0）→ 质量到顶，停
4. 4\. t ≥ T\_max → 无条件 failsafe（保证终止，有机器验证的定理）

文章给了一个真实轨迹示例。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/Cic4GFNZLlxpicDbibGKNd2pfk3mc54jO7ZNz0IMS4uOdz13QIdF02kzZo7iaic4u4WJ3jpGy7LhibhSheYs5rf0wiaicmGqcHZ3mRGpmwMQI5z80Xo/640?wx_fmt=png&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1\#imgIndex=1)

问题是"Cypress 和 Ajuga 是否同属？"第 1 轮 IS=0.54，第 2 轮语义距离 d₂=0.144（大变化），第 3 轮 d₃=0.027（首次跌破 ε=0.06），第 4 轮 d₄=0.007（连续两轮 < ε）→ SHP 在第 4 轮触发 entropy 停。而 max\_iterations baseline 会跑满 6 轮——多烧了 2 轮完全没用的 token。

如果你现在把 `max_iterations=6` 换成连续 2 轮余弦距离 < 0.06 就停，embedding 本地跑 sentence-transformers 免费，预期省 30-40% token。论文测试集上实测省了 38%。

文章还有一个值得尊重的细节：作者坦承早期版本声称这是 Banach 收缩——有唯一不动点、保证收敛。但拿不出 Lipschitz 界。现在的版本诚实降级：只证明确定性终止（Theorem 1，机器验证），收敛性降为经验猜想（Conjecture 1）。这种"我证不了就不声称"的态度，在 LLM 论文里不多见。

\## ② 省 38% Token 质量不降，但加了质量信号反而更贵

文章在 HotpotQA distractor setting 上做了实验。Writer/Critic/Judge 都用 llama-3.1-8b-instruct，20 题开发集调参，60 题测试集冻结只报结果。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/Cic4GFNZLlxo0ttAAruuA1wV0DiavffehgvmSrmyofYwySmXoFK3XQutztYpDb9TNYypMwqopWehyicuBxQvk4UtjbGtNLhZbBnK54apKtXCek/640?wx_fmt=png&from=appmsg&watermark=1\#imgIndex=2)

评估方法本身就是一个贡献。每个问题只生成一次完整轨迹到 T\_max，所有停止策略在同一轨迹上回放——严格配对对比，消除生成随机性。judge 调用全部缓存，同一个草稿不重复打分。

测试集 60 题的结果：

![图片](https://mmbiz.qpic.cn/mmbiz_png/Cic4GFNZLlxr72TOor2kDAic3yaKpUmSFtB8wh9otbOaVA5abFmJLzOiakzNNDNLNtnsf8Cpn4YXmIW5IC1VeW8WRVNrdFSXWrcQumCS0ibuDKQ/640?wx_fmt=png&from=appmsg&watermark=1\#imgIndex=3)

三个反直觉发现：

**第一，judge-free 语义早停是最优性价比。** entropy\_only 只靠免费几何信号，省 38% token，质量与 baseline 统计无差异（p=0.81）。你不需要调任何 LLM judge 就能拿到这个收益。

**第二，加了质量信号反而血亏。** full SHP 每轮调 judge 算 IS，虽然只跑 2.4 轮就停，但 token 消耗反而比 baseline 多了 129%。judge 成本吃掉了所有节省。这是全文最反直觉的结论：你以为加质量信号会让决策更聪明，实际上它让成本爆炸。

**第三，oracle 把问题重构了。** oracle 事后选最优轮，IS 比 baseline 高 0.115（p≈4×10⁻¹¹），但 token 多烧 170%。它揭示了一个更深刻的问题："何时停"很简单——语义收敛就停，省 38% 零成本。"选哪轮最好"才是真正的开放难题——oracle 的天花板说明还有巨大的优化空间，但实时判断哪轮最优目前没有好办法。

如果你有办法事后评估质量（比如人工标注 20 条小样本），可以跑满 T\_max 然后事后选最优轮——IS 能提升 0.115。但实时场景下，老老实实用 judge-free 语义早停，省 38% token 是最优解。

\## ③ 语义距离确实在收敛——但没那么干净

文章还分析了 300 个逐轮距离的分布。均值 0.040，中位数 0.022，80% 低于 ε=0.06。距离平均递减（p=1.3×10⁻³）——收敛是真实的。

![图片](https://mmbiz.qpic.cn/mmbiz_png/Cic4GFNZLlxpWFKb4dEIE6w5cLwLuibGkicFcqcpaCyuZEXVCjgXgYu2DSewVbT746qHPibrmUm4K4ZRyk60eoms4pibibZLKC7tpibRxgQic7lgy8o/640?wx_fmt=png&from=appmsg&watermark=1\#imgIndex=4)

但只有约 5% 的轨迹严格单调递减。大部分轨迹的距离是"震荡下降"——这轮近一点、下轮远一点、整体趋势向下。这正是为什么需要 patience 窗口（k=2）：容忍逐轮噪声，不被单次幸运的 sub-ε 触发误停。

这个发现对工程落地很重要：别指望语义距离像梯度下降一样单调收敛。设一个合理的 ε（0.06 是个好起点）和 patience（2-3 轮），接受噪声，整体趋势向下就够了。

\## ④ 你现在就能用的一个优化

如果你在用 Writer→Critic 或类似的 Agent 循环，把 `max_iterations` 换成语义早停只需要三步：

1. 1\. 加一个本地 embedding 模型（sentence-transformers 随便选一个轻量的），每轮算余弦距离
2. 2\. 设 ε=0.06，k=2——连续 2 轮距离低于阈值就停
3. 3\. 保留 T\_max 作为 failsafe（比如 10），但正常情况不会触发

预期省 30-40% token，质量不降。embedding 本地跑，零 API 成本。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/Cic4GFNZLlxql5ZwQQ7zcW2WNVtuicuzJMjWCc1oclwYmGFhj5wrS05LnQPiao1aZIcEicjv9RB9NictLfnNqp8IVjF7dCAQjZvdg7bnwWnO6ILc/640?wx_fmt=png&from=appmsg&watermark=1\#imgIndex=5)

**别加质量信号。** full SHP 的教训很明确——每轮调 LLM judge 的成本远超节省。除非你的 judge 是本地小模型且延迟可忽略，否则 judge-free 就是最优性价比。

但是文章的局限性也要说清楚：目前只在短答案 QA（HotpotQA）上验证。长文本生成（代码、文章）中草稿逐轮累积内容，语义距离可能不会快速收敛——需要进一步验证。但代码和论文数据全部开源（github.com/SahilShrivastava-Dev/semantic-halting-problem），你可以直接拿自己的任务跑一遍。

---

语义早停把一个"工程直觉"——答案不变了就停——做成了有理论保证、有实验验证、有开源代码的完整方案。38% token 节省 + 质量持平，对任何跑 Agent 循环的开发者都是直接可用的优化。

oracle 的存在提醒我们：真正的难题不是"何时停"，而是"哪轮最好"。如果你能找到低成本的事后质量评估方法，oracle 的 +0.115 IS 天花板就在那里等着你。

---

\## 参考资料

1. 1\. https://arxiv.org/abs/2606.27009
2. 2\. https://github.com/SahilShrivastava-Dev/semantic-halting-problem

**微信扫一扫赞赏作者**

闪记

复制 LaTeX 公式