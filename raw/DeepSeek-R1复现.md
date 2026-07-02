---
id: "7283144999426853848"
cubox_url: https://cubox.pro/web/card/7283144999426853848
url: https://mp.weixin.qq.com/s/_yrzvSzzE6g3qBzVEk1q-Q
tags:
  - LLM
  - LLM/reasoning
---
# DeepSeek-R1复现



[Read in Cubox](https://cubox.pro/web/card/7283144999426853848)  
[Read Original](https://mp.weixin.qq.com/s/_yrzvSzzE6g3qBzVEk1q-Q)  

---


---

\## 📖 正文全文

# 全球掀DeepSeek复现狂潮！硅谷巨头神话崩塌，30刀见证啊哈时刻

[mp.weixin.qq.com](https://mp.weixin.qq.com/s/_yrzvSzzE6g3qBzVEk1q-Q)玩转VS Code

\#\## ![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_jpg%2FUicQ7HgWiaUb2ibG9LcmbDlGA50zQV4udMhBg1oTyUMR1UFDlxRdsX4ib9PsWbyjibR4oiaKKhdlRKmP7Mzo31ms1nyQ%2F640%3Fwx_fmt%3Djpeg%26from%3Dappmsg)

\#\## *** ** * ** ***
**新智元报道**


编辑：编辑部 HYZ

\#\#\#\## **【新智元导读】** 就在刚刚，网上已经出现了一波复现DeepSeek的狂潮。UC伯克利、港科大、HuggingFace等纷纷成功复现，只用强化学习，没有监督微调，30美元就能见证「啊哈时刻」！全球AI大模型，或许正在进入下一分水岭。


这些天，硅谷彻底处于中国公司带来的大地震余波中。

全美都在恐慌：是否全球人工智能的中心已经转移到了中国？

就在这当口，全球复现DeepSeek的一波狂潮也来了。

诚如LeCun所言：「这一次，正是开源对闭源的胜利！」

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2FUicQ7HgWiaUb2ibG9LcmbDlGA50zQV4udMhIzJmK5YZjy5KWdtP0wZu2F6wSRDcGrAzwluGPTZtYbpKgWiaQvLTJuQ%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg)
>
> 在没有顶级芯片的情况下，以极低成本芯片训出突破性模型的DeepSeek，或将威胁到美国的AI霸权。
>
> 大模型比拼的不再是动辄千万亿美元的算力战。
>
> OpenAI、Meta、谷歌这些大公司引以为傲的技术优势和高估值将会瓦解，英伟达的股价将开始动摇。

种种这些观点和讨论，让人不禁怀疑：数百亿美元支出，对这个行业真的必要吗？甚至有人说，中国量化基金的一群天才，将导致纳斯达克崩盘。

从此，大模型时代很可能会进入一个分水岭：超强性能的模型不再独属于算力巨头，而是属于每个人。

30美金，就能看到「啊哈」时刻


来自UC伯克利博士生潘家怡和另两位研究人员，在CountDown游戏中复现了DeepSeek R1-Zero。

他们表示，结果相当出色！

实验中，团队验证了通过强化学习RL，3B的基础语言模型也能够自我验证和搜索。

更令人兴奋的是，成本不到30美金（约217元），就可以亲眼见证「啊哈」时刻。

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2FUicQ7HgWiaUb2ibG9LcmbDlGA50zQV4udMhpscAiahHZYEvDBp7OmQz5AYym7EiapKXgF3J04Ric15fURVAS6biavBL0A%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg)

这个项目叫做TinyZero，采用了R1-Zero算法------给定一个基础语言模型、提示和真实奖励信号，运行强化学习。

然后，团队将其应用在CountDown游戏中（这是一个玩家使用基础算术运算，将数字组合以达到目标数字的游戏）。

模型从最初的简单输出开始，逐步进化出自我纠正和搜索的策略。

在以下示例中，模型提出了解决方案，自我验证，并反复纠正，直到解决问题为止。

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2FUicQ7HgWiaUb2ibG9LcmbDlGA50zQV4udMhOqmkpC6DFaxa7oLdtjZLfPT1b3jN53wDhBeGAl3gibaRiblNpRKJibGnw%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg)

在消融实验中，研究人员运行了Qwen-2.5-Base（0.5B、1.5B、3B、7B四种参数规模）。

结果发现，0.5B模型仅仅是猜测一个解决方案然后停止。而从1.5B开始，模型学会了搜索、自我验证和修正其解决方案，从而能够获得更高的分数。

他们认为，在这个过程，基础模型的是性能的关键。

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2FUicQ7HgWiaUb2ibG9LcmbDlGA50zQV4udMhRBSvpiaBnHibPiciaBeMiaicsxpYkQO0gQYccldrkVs5SibqqvuLicFicmJRkfg%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg)

他们还验证了，额外的指令微调（SFT）并非是必要的，这也印证了R1-Zero的设计决策。

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2FUicQ7HgWiaUb2ibG9LcmbDlGA50zQV4udMhPjhOUItbkgneARjpy1wToqlF1gWnCuuZxLRFrWBTmZS9WYibbLXdSLg%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg)

这是首个验证LLM推理能力的实现可以纯粹通过RL，无需监督微调的开源研究

基础模型和指令模型两者区别：

*
  指令模型运行速度快，但最终表现与基础模型相当
* 指令输出的模型更具结构性和可读性


![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2FUicQ7HgWiaUb2ibG9LcmbDlGA50zQV4udMh4a2ge2S3NmwWPWQVjpQibYicEh4oMJibiaMs38HD9yPC4TpmYSwkfA4Anw%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg)

此外，他们还发现，具体的RL算法并不重要。PPO、GRPO、PRIME这些算法中，长思维链（Long CoT）都能够涌现，且带来不错的性能表现。

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2FUicQ7HgWiaUb2ibG9LcmbDlGA50zQV4udMhibibBn04FooQOXYmEdImHhibBfVALsPkUA0elIyrRTm7ra8ar6QQZKpkw%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg)

而且，模型在推理行为中非常依赖于具体的任务：

*
  对于Countdow任务，模型学习进行搜索和自我验证
* 对于数字乘法任务，模型反而学习使用分布规则分解问题，并逐步解决


![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2FUicQ7HgWiaUb2ibG9LcmbDlGA50zQV4udMhUpFsbDMRKVoRvFaJGl5wMMvH4XiceeOQuOB9VYia0qOlXyHNBfpC8s5Q%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg)

苹果机器学习科学家Yizhe Zhang对此表示，太酷了，小到1.5B的模型，也能通过RL涌现出自我验证的能力。

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2FUicQ7HgWiaUb2ibG9LcmbDlGA50zQV4udMhY5J7iaGqUIuScDRkM5NEttugHGwsSXejwmiaiadZhDCPbIBMoeRWVdCnQ%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg)

7B模型复刻，结果令人惊讶


港科大助理教授何俊贤的团队（共同一作黄裕振、Weihao Zeng），只用了8K个样本，就在7B模型上复刻出了DeepSeek-R1-Zero和DeepSeek-R1的训练。

结果令人惊喜------模型在复杂的数学推理上取得了十分强劲结果。

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2FUicQ7HgWiaUb2ibG9LcmbDlGA50zQV4udMhle8kblHAlUno2JCZIqsTX0Zbts0VMI84JIlAT3ibV1mbvBticoqSSiaAA%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg)

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2FUicQ7HgWiaUb2ibG9LcmbDlGA50zQV4udMhPAz6JZG1Tl85ohk7F1lbjjWicIIPeclwek46rhPichtxK3BfibqZAt3zQ%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg)

项目地址：https://github.com/hkust-nlp/simpleRL-reason

他们以Qwen2.5-Math-7B（基础模型）为起点，直接对其进行强化学习。

整个过程中，没有进行监督微调（SFT），也没有使用奖励模型。

最终，模型在AIME基准上实现了33.3%的准确率，在AMC上为62.5%，在MATH上为77.2%。

这一表现不仅超越了Qwen2.5-Math-7B-Instruct，并且还可以和使用超过50倍数据量和更复杂组件的PRIME和rStar-MATH相媲美！

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2FUicQ7HgWiaUb2ibG9LcmbDlGA50zQV4udMhric90V3GL6ShPyuAxwVEPTF0deXoW7buuvN3MnJdzfIl5kypiasecjgw%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg)

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2FUicQ7HgWiaUb2ibG9LcmbDlGA50zQV4udMhYUVLEDibsfGS6qJLq0NCYMxtYI7l2Nt3mic1a4xabw5rtzuFLWice7p3Q%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg)

其中，Qwen2.5-7B-SimpleRL-Zero是在Qwen2.5-Math-7B基础模型上仅使用纯PPO方法训练的，仅采用了MATH数据集中的8K样本。

Qwen2.5-7B-SimpleRL则首先通过Long CoT监督微调（SFT）作为冷启动，然后再进行强化学习。

在这两种方法中，团队都只使用了相同的8K MATH样本，仅此而已。

大概在第44步的时候，「啊哈时刻」出现了！模型的响应中，出现了自我反思。

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2FUicQ7HgWiaUb2ibG9LcmbDlGA50zQV4udMh9PMvibfHZoW3SWMnDtsT1laibsxQCUIuINPjRl1VSfoNRhFwwG1uZRxg%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg)

并且，在这个过程中，模型还显现了更长的CoT推理能力和自我反思能力。

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2FUicQ7HgWiaUb2ibG9LcmbDlGA50zQV4udMh1iaUk60xWGEHFiaicUrFhdvRDEDxTl2ZpKu1Qhsia7MjuwS0S2icpDiag3dA%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg)

在博客中，研究者详细剖析了实验设置，以及在这个强化学习训练过程中所观察到的现象，例如长链式思考（CoT）和自我反思机制的自发形成。

与DeepSeek R1类似，研究者的强化学习方案极其简单，没有使用奖励模型或MCTS（蒙特卡洛树搜索）类技术。

他们使用的是PPO算法，并采用基于规则的奖励函数，根据生成输出的格式和正确性分配奖励：

*
  如果输出以指定格式提供最终答案且正确，获得+1的奖励
*
  如果输出提供最终答案但不正确，奖励设为-0.5
* 如果输出未能提供最终答案，奖励设为-1


该实现基于OpenRLHF。初步试验表明，这个奖励函数有助于策略模型快速收敛，产生符合期望格式的输出。

\#\## **第一部分：SimpleRL-Zero（从头开始的强化学习）**


接下来，研究者为我们分享了训练过程动态分析和一些有趣的涌现模式。

\#\#\## **训练过程动态分析**


如下所示，所有基准测试的准确率在训练过程中都在稳步提高，而输出长度则呈现先减少后逐渐增加的趋势。

经过进一步调查，研究者发现，Qwen2.5-Math-7B基础模型在初始阶段倾向于生成大量代码，这可能源于模型原始训练数据的分布特征。

输出长度的首次下降，是因为强化学习训练逐渐消除了这种代码生成模式，转而学会使用自然语言进行推理。

随后，生成长度开始再次增加，此时出现了自我反思机制。

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2FUicQ7HgWiaUb2ibG9LcmbDlGA50zQV4udMhyTblCv4aZkzcZIjRARiaeBiaRv28icnvxxTQjx034PgRUVls75RjKZleQ%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg)

训练奖励和输出长度

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2FUicQ7HgWiaUb2ibG9LcmbDlGA50zQV4udMhxyPwI6unqUCDZd3lG6nvGBKOd4OFLgz4C4dyJKcrJ7CPMiaDbEnp0Kg%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg)

基准测试准确率（pass@1）和输出长度


\#\#\## **自我反思机制的涌现**


在训练到第 40 步左右时，研究者观察到：模型开始形成自我反思模式，这正是DeepSeek-R1论文中所描述的「aha moment」（顿悟时刻）。

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2FUicQ7HgWiaUb2ibG9LcmbDlGA50zQV4udMhCicmzjhDSn9CONUh2z1nnq9vjVBRkib6fDIBWC3ErPx36toPS5lV6UNQ%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg)

\#\## **第二部分：SimpleRL（基于模仿预热的强化学习）**


如前所述，研究者在进行强化学习之前，先进行了long CoT SFT预热，使用了8,000个从QwQ-32B-Preview中提取的MATH示例响应作为SFT数据集。

这种冷启动的潜在优势在于：模型在开始强化学习时已具备long CoT思维模式和自我反思能力，从而可能在强化学习阶段实现更快更好的学习效果。

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2FUicQ7HgWiaUb2ibG9LcmbDlGA50zQV4udMhULK32arYgl3lCvzYfRsdHVfczPqStcic395KtSGUlhOyo6VE0OSQn2Q%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg)

与RL训练前的模型（Qwen2.5-Math-7B-Base + 8K QwQ知识蒸馏版本）相比，Qwen2.5-7B-SimpleRL的平均性能显著提升了6.9个百分点。

此外，Qwen2.5-7B-SimpleRL不仅持续优于Eurus-2-7B-PRIME，还在5个基准测试中的3个上超越了Qwen2.5-7B-SimpleRL-Zero。

\#\## **训练过程分析**

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2FUicQ7HgWiaUb2ibG9LcmbDlGA50zQV4udMhwEic3xic8YtvuAp3Y3Q0n3hhmnmic334aBCkkxyYOQWWN7qNbGMDjQB5g%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg)

训练奖励和输出长度

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2FUicQ7HgWiaUb2ibG9LcmbDlGA50zQV4udMhdwa83IicmnJXUNmuCicwaEp8djtfo0T36ibIPgAAs90Ezkqz4vZcHxXkQ%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg)

基准测试准确率（pass@1）和输出长度

Qwen2.5-SimpleRL的训练动态表现与Qwen2.5-SimpleRL-Zero相似。

有趣的是，尽管研究者先进行了long CoT SFT，但在强化学习初期仍然观察到输出长度减少的现象。

他们推测，这可能是因为从QwQ提取的推理模式不适合小型策略模型，或超出了其能力范围。

因此，模型选择放弃这种模式，转而自主发展新的长链式推理方式。

最后，研究者用达芬奇的一句话，对这项研究做了总结------

简约，便是最终极的精致。

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2FUicQ7HgWiaUb2ibG9LcmbDlGA50zQV4udMhJBo5yU7XlFzGbsST8Cjl8Sf8TTk21qu5sUbQEYJmdkM1pM2lArUVlw%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg)

完全开源复刻，HuggingFace下场了


甚至，就连全球最大开源平台HuggingFace团队，今天官宣复刻DeepSeek R1所有pipeline。

复刻完成后，所有的训练数据、训练脚本等等，将全部开源。

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2FUicQ7HgWiaUb2ibG9LcmbDlGA50zQV4udMhdzibd96kYpc7768MmkORNfz856MjZU6eaeWognUXzEBLRkfkgxw5KDg%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg)

这个项目叫做Open R1，当前还在进行中。发布到一天，星标冲破1.9k，斩获142个fork。

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2FUicQ7HgWiaUb2ibG9LcmbDlGA50zQV4udMhPxoCdGIKoXs3pgzn92OoxrEItBzr7FCd6fYp8aYJLF4o9mV367DZvA%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg)

项目地址：https://github.com/huggingface/open-r1

研究团队以DeepSeek-R1技术报告为指导，将整个复刻过程划分为三个关键步骤。

*
  **步骤 1：** 通过从DeepSeek-R1蒸馏高质量语料库，复现R1-Distill模型。
*
  **步骤 2：** 复现DeepSeek用于创建R1-Zero的纯强化学习（RL）流程。这可能需要为数学、推理和代码任务策划新的大规模数据集。
* **步骤 3：** 展示我们如何通过多阶段训练，从基础模型发展到经过RL调优的模型。


![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2FUicQ7HgWiaUb2ibG9LcmbDlGA50zQV4udMhIBp1sSIoxxDoicmna9AgYOaXuILLR0xjwuufG6cSmYI8yLJwCNeq3MQ%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg)

从斯坦福到MIT，R1成为首选


一个副业项目，让全世界科技大厂为之惶恐。

DeepSeek这波成功，也成为业界的神话，网友最新截图显示，这款应用已经在APP Store「效率」应用榜单中挤进前三。

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2FUicQ7HgWiaUb2ibG9LcmbDlGA50zQV4udMhE2ozhjQyyB6TNtlMMsnx6GLsraVemCUWdQhMiabibnumvSHJQakWaZNA%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg)

在Hugging Face中，R1下载量直接登顶，另外3个模型也霸占着热榜。

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2FUicQ7HgWiaUb2ibG9LcmbDlGA50zQV4udMhLSQrQlySXRo6ibxPUuRu1Vwlf4BjeOeNPQrxqJbWQ38qjLlibnQzZ3uw%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg)

a16z合伙人Anjney Midha称，一夜之间，从斯坦福到MIT，DeepSeek R1已经成为美国顶尖高校研究人员「首选模型」。

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2FUicQ7HgWiaUb2ibG9LcmbDlGA50zQV4udMh1d4oO3Rbob3CYehkyFdVrJX8dDQl57KUibVo0qjhIL5s7xsqe7icjbaA%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg)

还有研究人员表示，DeepSeek基本上取代了我用ChatGPT的需求。

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2FUicQ7HgWiaUb2ibG9LcmbDlGA50zQV4udMhrLO1BJ1oBkLzHAQKYAJ0f9AcWQmC6rXM96JFXTw4LLFXGCA5xk9eDQ%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg)

中国AI，这一次真的震撼了世界。

参考资料：

https://x.com/junxian_he/status/1883183099787571519

https://x.com/jiayi_pirate/status/1882839370505621655

[Read in Cubox](https://cubox.pro/web/card/7283144999426853848)
