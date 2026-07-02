---
id: "7338895617151729795"
cubox_url: https://cubox.pro/web/card/7338895617151729795
url: https://mp.weixin.qq.com/s/TmANwuqCawcq1Zr3vfNgFg
tags:
  - LLM/training
---
# 一文详细了解：大模型三大缩放定律（Scaling Law）

大模型三大Scaling Law

[Read in Cubox](https://cubox.pro/web/card/7338895617151729795)  
[Read Original](https://mp.weixin.qq.com/s/TmANwuqCawcq1Zr3vfNgFg)  

---

\## Annotations  

> 「后训练技术能够进一步提升模型针对特定应用的适应性与相关性」。  

[Link️](https://cubox.pro/web/annotations/cards/7338895617151729795?highlight=7338895617378222826)  

> 推理阶段Scaling Law(https://arxiv.org/abs/2504.02495)（Long Thinking）发生在推理过程中。「强调通过动态调整奖励机制来提升模型的推理能力，而非传统的通过增加模型参数或训练数据。」  

[Link️](https://cubox.pro/web/annotations/cards/7338895617151729795?highlight=7338904244633733997)


---

\## 📖 正文全文

# 一文详细了解：大模型三大缩放定律（Scaling Law）

[mp.weixin.qq.com](https://mp.weixin.qq.com/s/TmANwuqCawcq1Zr3vfNgFg)ShuYini AINLPer


**点击下方****"****AINLPer****"**，添加关注

更多干货，第一时间送达


更多精彩内容-\>[专注大模型、Agent、RAG等前沿分享！](https://mp.weixin.qq.com/s?__biz=MzUzOTgwNDMzOQ==&mid=2247502960&idx=1&sn=e938491c6253a6525ab37a9238111059&scene=21&token=646435429&lang=zh_CN\#wechat_redirect)

\## 引言

就像自然界中存在的经验法则，例如"物体上升必定下落"或"给物体施加作用力必定伴随反作用力"；在大模型方面也存在这么一个经验法则：更多的算力、数据以及模型参数也会得到优秀的模型。

然而，随着AI技术的发展，已经出现了三条不同的法则来描述不同方式下计算资源的应用如何影响模型性能。它们分别是**「预训练Scaling法则（Pretraining Scaling Law）」** 、**「后训练Scaling法则（Post-Training Scaling Law）和推理阶段Scaling法则（Test-Time Scaling Law，又称Long Thinking）」** 。这三条法则共同反映了AI在不断丰富的复杂应用场景中，如何采用不同技术方式使用额外计算资源以提升表现。本文将详细介绍大模型的三大Scaling法则。![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2F1BQYN3xneiabCy7LaPO9RbKgwMWVOHV1hOicicf2iaREiaEv261ibia3DhSU1kcCxOgOricJA88kXibibnvDD70AZCU8hibicQ%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26tp%3Dwebp%26wxfrom%3D5%26wx_lazy%3D1&valid=false)

\## 预训练Scaling Law

预训练Scaling Law(https://arxiv.org/abs/2203.15556)是AI发展的基础法则。**「它证明了通过扩大训练数据集规模、增加模型参数数量和计算资源，可以实现模型性能的提升」** 。数据、模型规模、计算能力这三要素彼此密不可分。

根据预训练Scaling法则，当更大的模型被更多的数据喂养时，整体性能会提升。正是预训练Scaling原则促成了超大模型的诞生，同时也推动了模型架构方面的重大创新，包括十亿甚至万亿参数规模的Transformer模型、专家混合模型（Mixture of Experts）以及新的分布式训练技术。

然而，为了实现这一点需要大量算力，只有强大的加速计算资源才能来承担更大的训练任务。这就是美国限制AI芯片的主要原因。当前预训练Scaling法则的意义仍在持续，人们正在不断生产日益增长的多模态数据，这些文本、图像、音频、视频及传感器数据将用于训练更强大的AI模型。![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_jpg%2F1BQYN3xneiabCy7LaPO9RbKgwMWVOHV1hjBG5fBceYajoh4jvQl5b8VSydXp6nxSyiacKcZlCniaqWWAKpAZvbZ9g%2F640%3Fwx_fmt%3Djpeg%26from%3Dappmsg%26tp%3Dwebp%26wxfrom%3D5%26wx_lazy%3D1&valid=false)图中展示的Mixture of Experts是当前AI训练中流行的模型架构。

\## 后训练Scaling

并非每个人都能对预训练基础大模型（Foundation Model），因为它需要大量的计算资源、专业人才和数据集。但一旦某个组织完成了基础模型的预训练并公开发布，它就降低了AI应用的门槛。通过后训练技术可以让人们对基础大模型进行调优并实现模型定制化。流行的开源模型往往衍生出数百甚至上千个不同版本，覆盖各种领域。

**「后训练技术能够进一步提升模型针对特定应用的适应性与相关性」** 。若将预训练比作送AI模型"上学"学习基础技能，那么后训练就是"职场培训"，使模型胜任具体工作。比如，一个LLM可以通过后训练应对情感分析、翻译等任务，或者掌握特定领域（如医疗、法律）的专业术语。

后训练Scaling法则(https://arxiv.org/abs/2410.12119)认为，通过微调、剪枝、量化、蒸馏、强化学习和合成数据增强等技术，**「可以进一步提升预训练模型的计算效率、准确率或领域适应性」** ：

*
  **「微调（Fine-tuning）」** ：使用额外训练数据，将AI模型调整到特定领域或应用。可采用公司内部数据集，或输入/输出样例对。

*
  **「蒸馏（Distillation）」** ：采用一对AI模型：一个复杂"教师"模型与一个轻量"学生"模型。最常见的是离线蒸馏，学生模型学习模仿教师模型的输出。

*
  **「强化学习（Reinforcement Learning, RL）」** ：基于奖励机制训练大模型，使其在特定任务中做出最优决策。RLHF（人类反馈强化学习）通过用户"点赞"反馈正向强化模型表现。RLAIF（AI反馈强化学习）则由AI模型提供反馈，提升后训练效率。

*
  **「Best-of-n采样」** ：生成多个模型输出，选择根据奖励模型评分最高的结果。无需修改模型参数，即可提升输出质量，是微调与强化学习的替代方案。

*
  **「搜索方法（Search Methods）」** ：探索各种潜在决策路径后再选择最终输出，可反复改进模型回答。

为支持后训练，开发者还可使用合成数据扩充微调数据集。AI生成数据能帮助模型更好地处理原训练数据中缺失或极少出现的特殊案例。

\## 推理Scaling Law？

LLM能够对输入Prompt迅速作答，这种方式比较适合简单问题，但若面对复杂问题效果并不是很好。而复杂问题的解答需要LLM在作答前进行充分的思考推理。这与人类思考过程类似------若被问"2加2是多少"，人们能立即回答；但若临时被要求制定提升公司利润10%的商业计划，则往往要思考多个选项，分步骤作答。

推理阶段Scaling Law(https://arxiv.org/abs/2504.02495)（Long Thinking）发生在推理过程中。**「强调通过动态调整奖励机制来提升模型的推理能力，而非传统的通过增加模型参数或训练数据。」**

与传统模型一次性快速生成答案不同，采用该技术的模型在推理时投入更多计算资源，推演多个可能答案，最终选出最佳方案。例如，生成复杂定制代码时，AI推理过程可能耗时数分钟甚至数小时------面对复杂问题时所需计算量可能是传统LLM单次推理的数十倍，否则几乎不可能一次生成正确答案。

这一推理能力让模型能探索不同问题解决方案，分解复杂需求，并在推理过程中向用户展示"解题步骤"。**「研究发现，当AI模型面对需要多步推理与规划的开放式问题时，推理阶段Scaling显著提升了回答质量。」**

推理阶段的计算方法包括：

*
  **「多次采样与并行采样」** ：通过多次采样生成不同的原则集和相应的批评，然后投票选出最终的奖励。更大规模的采样可以更准确地判断具有更高多样性的原则，并以更细的粒度输出奖励。

*
  **「自我原则批评调整（SPCT）」** ：包含拒绝式微调（作为冷启动阶段）和基于规则的在线强化学习，通过不断优化生成的准则和评论，增强泛化型奖励生成能力，促使奖励模型在推理阶段展现良好扩展能力。

*
  **「元奖励模型（Meta Reward Model）」** ：引入多层级奖励评估体系，统一处理单响应、多响应及对比评分的多样化场景，进一步提升推理效果。

其中，Best-of-n采样等后训练方法也可用于推理阶段优化输出，使之更符合人类偏好或其他目标。

\## 推理Scaling如何赋能AI推理？

**「推理阶段计算能力的提升，使AI能够针对复杂、开放式问题给出更合理、更有帮助、更准确的答案。这一能力对自主Agentic AI应用中的多步骤推理任务至关重要」** 。各行业也能借此提升效率与生产力，为用户提供强大的助理以加速工作进程。

在医疗领域，模型可以借助推理阶段Scaling分析海量数据，预测疾病进展，以及基于新药分子结构推测潜在并发症，或筛选匹配患者疾病特征的临床试验，并展示不同方案的优缺点。

在**「金融领域」** ，与传统机器学习模型相比，推理模型能捕捉数据间的复杂关联（如因果关系），更精准地预测客户违约概率。例如，通过分析客户历史行为与外部经济指标的关联，模型可动态调整风险评分，降低人工审核成本。

在零售与供应链物流领域，推理阶段Scaling有助于解决短期运营问题及长期战略目标所需的复杂决策。推理技术可帮助企业预测并评估多种情境，降低风险，应对扩展挑战------提升需求预测精度、优化供应链路径、改进符合可持续发展目标的采购决策。

当前AI推理模型正迅速演进。已经出现了很多推理大模型，尤其是今年年初的DeepSeek R1，可谓引爆全球，当然相关推理模型也有：OpenAI的o1、Google DeepMind的Gemini 2.0 Flash Thinking、Qwen的Qwen3推理模型等。

\## 推荐阅读

\[1\][新手必看！强化学习入门指南](https://mp.weixin.qq.com/s?__biz=MzUzOTgwNDMzOQ==&mid=2247504066&idx=1&sn=04c09ebe3b719de39d9337c1157c8a30&scene=21\#wechat_redirect)

\[2\][大模型(LLM)推理优化技术总结（非常详细）](https://mp.weixin.qq.com/s?__biz=MzUzOTgwNDMzOQ==&mid=2247504051&idx=1&sn=d736cc5c5aac64f7caff9772ef50e592&scene=21\#wechat_redirect)  

\[3\][大模型推理基准测试及评估指标](https://mp.weixin.qq.com/s?__biz=MzUzOTgwNDMzOQ==&mid=2247504028&idx=1&sn=1db360ad57565663c6890ecd47e4a71f&scene=21\#wechat_redirect)！

\[4\][多智能体（Multi-Agent）开发必读指南！](https://mp.weixin.qq.com/s?__biz=MzUzOTgwNDMzOQ==&mid=2247503999&idx=2&sn=740478d62d653e0e63c1ee1cc898da62&scene=21\#wechat_redirect)

\[5\][Agent下一阶段：可自我进化的AI-Agent](https://mp.weixin.qq.com/s?__biz=MzUzOTgwNDMzOQ==&mid=2247503947&idx=1&sn=dc9a235a15c2c960d8e6e11937488240&scene=21\#wechat_redirect)

\[6\][众所周知！大模型应用构建面临的 6大误区](https://mp.weixin.qq.com/s?__biz=MzUzOTgwNDMzOQ==&mid=2247503909&idx=1&sn=834f85e705eaa9d49775ba7d95773468&scene=21\#wechat_redirect)

欢迎投稿或寻求报道，联系：ainlperbot


**「资料整理不易，点个** ****再看******、** **赞****吧**」****

[Read in Cubox](https://cubox.pro/web/card/7338895617151729795)
