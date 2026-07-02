---
id: "7382731199472471519"
cubox_url: https://cubox.pro/web/card/7382731199472471519
url: https://mp.weixin.qq.com/s/Vg0HUgIgOujLBClDXSDslQ
tags:
  - LLM
  - LLM/training/post-train
  - LLM/training/RL
  - LLM/training
---
# 后训练认知：SFT vs RL—关于记忆和遗忘机制

模型能否记得更牢，不取决于算法聪不聪明，而在于它学的是“谁的数据”。

[Read in Cubox](https://cubox.pro/web/card/7382731199472471519)  
[Read Original](https://mp.weixin.qq.com/s/Vg0HUgIgOujLBClDXSDslQ)  

---


---

\## 📖 正文全文

# RL记得更牢，SFT更健忘？普林斯顿陈丹琦团队改写后训练认知

[mp.weixin.qq.com](https://mp.weixin.qq.com/s/Vg0HUgIgOujLBClDXSDslQ)让你更懂AI的 PaperWeekly


![](https://image.cubox.pro/cardImg/1zns7unpm68lafvvmsq8jghd75oetxzvtj6yodpgv4uvbmzdmr?imageMogr2/quality/90/ignore-error/1)

\## 同样的后训练，RL 让模型更稳，SFT 却更健忘。普林斯顿陈丹琦团队发现，遗忘的根源不在算法，而在数据分布与模型行为之间的错位。


随着大模型规模的不断扩大，后训练（post-training）已成为影响模型最终表现的关键阶段。它让模型更符合人类偏好，但也带来了一个顽固的副作用------**遗忘** 。模型在交流上更自然，却往往在推理与知识任务上表现下滑。

这种现象被研究者称为 *alignment tax* ：对齐越彻底，记忆越脆弱。在各种后训练方法中，监督微调（SFT）和强化学习（RL）是两条最常见的路线。SFT 依赖高质量标注数据，稳定可靠；RL 则通过奖励优化生成策略，更具适应性。

从理论直觉看，SFT 被认为更稳健，而 RL 的目标更激进，似乎更容易遗忘。然而近年的实际结果却反其道而行------**RL 在长周期训练后反而保留了更多原有能力** 。  

这一现象引起了普林斯顿陈丹琦团队的兴趣。他们提出了一个核心问题：

"当 RL 和 SFT 在相同条件下训练时，是什么让它们的'记忆保留'出现系统差异？"

为回答这个问题，研究团队设计了严格的对照实验，并建立理论模型来分析遗忘的根源。他们最终发现，问题并非源自算法形式，而是源自**数据分布与模型行为之间的错位** 。

这项研究不仅比较了两种后训练范式的差异，更揭示了**记忆保留背后的机制** 。接下来的部分，将从理论与实证两条线展开，解释为何 RL 能"学得更久，也记得更牢"。

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2FVBcD02jFhgkg3QnfRB9IY0wfeNX3M0RwXOJ7TamMoBmST8PdMmXx45Ctka5EfEp8MicmpibpxWXWqEcMLO4xonBg%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26tp%3Dwebp%26wxfrom%3D5%26wx_lazy%3D1%23imgIndex%3D1&valid=false)

论文标题：

Retaining by Doing: The Role of On-Policy Data in Mitigating Forgetting

论文链接：

https://arxiv.org/pdf/2510.18874

![](https://image.cubox.pro/cardImg/5nlfzlrm0qzqfqcizjn9esqqwcdyk2e5lq3fw86lrd4c9evwh2?imageMogr2/quality/90/format/gif/ignore-error/1)

研究背景

在语言模型的发展过程中，"对齐"早已成为标准流程。模型从海量无监督语料中学习语言结构，但要真正理解人类意图，还需要经历后训练阶段：通过 SFT 或 RLHF，让模型输出符合人类期望。

然而，对齐带来的副作用同样显著------**灾难性遗忘（catastrophic forgetting）** 。模型在新任务上表现更好，却在旧任务上出现性能滑坡。

为系统研究这种现象，普林斯顿陈丹琦团队选择了两种最具代表性的后训练方法------**SFT 与 RL** ，并在 **Llama-3** 与 **Qwen-2.5** 系列模型上，以相同算力与数据预算进行对照训练，覆盖三类典型任务：指令遵循、通识推理、算术推理。

这项研究的目标，不是评判哪种方法更强，而是探究更深层的机制：

当模型在学习新目标时，它的旧知识为何会流失？又是什么让某些方法能让模型在学习中保留记忆？

正是在这一问题的驱动下，论文构建了从理论到实证的完整分析路径------逐步揭示出：**记忆的保持，与算法无关，与数据分布息息相关。**

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2FPsho9dm7oDGhKg9nnSz5qQrwKvXibt3wuhfgUpIfdPSqH8YjjHbCUiaaKsMA36bIMsMtGNKoBcus5py06M0fvx3A%2F640%3Fwx_fmt%3Dpng%26tp%3Dwebp%26wxfrom%3D5%26wx_lazy%3D1%23imgIndex%3D4&valid=false)

从两种 KL 到"记忆保留"的关键机制

在大语言模型（LLM）的后训练阶段，我们通常使用两类主流方法：SFT（监督微调）和RL（强化学习）。表面上，它们只是优化目标不同；但在作者看来，这两种方法的核心差别，其实在于它们如何处理模型的"记忆"。

2.1 从 KL 出发：两种截然不同的学习方向

SFT 与 RL 的关系，可以统一在同一个数学框架下。前者最小化的是正向 KL 散度（forward KL），意味着模型要"覆盖"目标分布的全部区域；后者最小化的是反向 KL 散度（reverse KL），则倾向"选择"目标分布中最可能的那部分。

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2FVBcD02jFhgkg3QnfRB9IY0wfeNX3M0Rwaiaoqy5IicicMQcQMxoAmbgia1UicFicDfo1ca4BBGlIicCcmliaarlChqRZBw%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26tp%3Dwebp%26wxfrom%3D5%26wx_lazy%3D1%23imgIndex%3D4&valid=false)

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2FVBcD02jFhgkg3QnfRB9IY0wfeNX3M0RwfB3PH5XqbD6Spm2xibO2IZcd8rDkBug7pB7vWzS4sjvSU9MOZ0XGEkg%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26tp%3Dwebp%26wxfrom%3D5%26wx_lazy%3D1%23imgIndex%3D5&valid=false)

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2FVBcD02jFhgkg3QnfRB9IY0wfeNX3M0RwLDXdSiaM8CHjMPUpdxa6RibWCv82XAIJmIyPYL1SibnibmiboXSTLzP1ZdQ%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26tp%3Dwebp%26wxfrom%3D5%26wx_lazy%3D1%23imgIndex%3D6&valid=false)

▲ 图1. Forward KL vs Reverse KL 的核心差异

前者像是"尽量包住所有山峰"，后者则专注"爬到最高的那座峰"，即"mode-covering" 与 "mode-seeking"的形象写照。

按照以往直觉，反向 KL 的 RL 会"舍弃旧模式"，似乎更容易遗忘。然而，当研究者在真实 LLM 分布上做实验时，却发现了完全相反的现象。

2.2 小模型推演：为什么现实中 RL 反而更"记得住"


为了理解这种反转，研究团队设计了一个极简的混合分布实验，把"旧任务"与"新任务"分别建模成两座概率峰：

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2FVBcD02jFhgkg3QnfRB9IY0wfeNX3M0RwnjMnm3D5JUB1VAnqxHWmHonoCTIa5QdWbo64HRibHAFRZbPvl330gyA%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26tp%3Dwebp%26wxfrom%3D5%26wx_lazy%3D1%23imgIndex%3D7&valid=false)


训练的目标是，让模型分布 在学习新任务时，尽可能保留旧峰的质量。研究者通过定义重叠度（overlap area）来度量这种"记忆保留"：

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2FVBcD02jFhgkg3QnfRB9IY0wfeNX3M0Rw87Wicd3MiadShiby93OPJHzd8cOF0CjO9icjWyWu9EYRGgovYuDVdC474A%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26tp%3Dwebp%26wxfrom%3D5%26wx_lazy%3D1%23imgIndex%3D8&valid=false)


![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2FVBcD02jFhgkg3QnfRB9IY0wfeNX3M0Rw6zOCVCADuOIwwmxE8HnnFpLyls0ZA7qvzKyAqYv00Ugg42aK2tVscA%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26tp%3Dwebp%26wxfrom%3D5%26wx_lazy%3D1%23imgIndex%3D9&valid=false)

▲ 图2. 单峰分布：SFT 稍占优势

在简单任务下，SFT 的 forward KL 确实能同时提升新峰并维持旧峰。

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2FVBcD02jFhgkg3QnfRB9IY0wfeNX3M0Rw8302sm2d96WjfBrYvl4LPUwCnibsbCE3GtsSDbBBvT3dCsic3icJ6ayvw%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26tp%3Dwebp%26wxfrom%3D5%26wx_lazy%3D1%23imgIndex%3D10&valid=false)

▲ 图3. 多峰分布：RL 反超

当任务复杂、输出多样时，SFT 的 forward KL 为了"覆盖"新目标，会拉扯概率质量，使旧峰衰减明显；反之，RL 的 reverse KL 直接"平移新峰"贴近目标，而不动旧峰。  

这意味着，真正让模型忘记旧任务的，不是 KL 的方向，而是数据分布是否一致。SFT 在离线静态数据（off-policy）上训练，始终面对过去；RL 在模型当前策略（on-policy）下采样，始终面向当下。

作者团队由此给出核心洞见------遗忘不是算法的问题，而是分布错位的问题。

2.3 消融分析：关键不在正则，而在 on-policy

为了进一步验证这一点，作者在 RL 目标中系统地移除了各个组成部分：去掉 KL 正则项（），去掉优势估计（REINFORCE 替代 GRPO），结果发现------模型的抗遗忘性能几乎不变。

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2FVBcD02jFhgkg3QnfRB9IY0wfeNX3M0Rwza1ktO2SsNzhPQZtz10OAVRHhuHbAbHQgLWW2ichibD2EQdgiaumMWduw%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26tp%3Dwebp%26wxfrom%3D5%26wx_lazy%3D1%23imgIndex%3D11&valid=false)

▲ 图4. 去掉 KL 正则，RL 依然保持低遗忘

上图对比了 GRPO 在 β = 0（无正则）与 β = 0.05 （有正则）下的表现。除 Llama 系列在 IFEval 任务上略有差异外，两者在 gain-drop 平衡上几乎一致，说明 KL 正则并非关键因素。

换言之，无论是否添加 KL 正则，只要训练数据来自 on-policy 分布，模型都能稳定保留旧知识。后续实验进一步表明，这种稳定性并不依赖特定算法成分，而主要源于 on-policy 采样机制本身。

这一发现，直接改写了过去"反向 KL 导致遗忘"的主流理解。

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2FPsho9dm7oDGhKg9nnSz5qQrwKvXibt3wukOjHSmSsEuRCB0fJu69CtdNgLnvFPDUCgeicOppBKuDvniaD3q8XWQ0Q%2F640%3Fwx_fmt%3Dpng%26tp%3Dwebp%26wxfrom%3D5%26wx_lazy%3D1%23imgIndex%3D9&valid=false)

实验结果

方法上的直觉得到了大规模实证的支持。作者在 Llama-3 与 Qwen-2.5 系列模型上，对比了 SFT、Self-SFT、REINFORCE 与 GRPO 四种方案，覆盖三个典型任务：IFEval（指令）、MMLU（通识）、Countdown（算术）。

在每个任务中，他们分别记录目标任务的提升（Gain）与非目标任务的下降（Drop）。

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2FVBcD02jFhgkg3QnfRB9IY0wfeNX3M0Rw5ZBwaNyIg67IwIaJSJj7xgYWMfB3ialurgqYx5GJ6G15sAJxDXgb7TA%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26tp%3Dwebp%26wxfrom%3D5%26wx_lazy%3D1%23imgIndex%3D13&valid=false)

▲ 图5. RL 在多数任务上表现更稳

实心柱表示目标任务 Gain，斜线阴影柱表示非目标任务 Drop。在多数模型与数据集上，RL（GRPO）在提升目标任务的同时，非目标任务的下降更小。  

换句话说，RL 不仅能"学会新东西"，还能"记得住旧东西"。相比之下，SFT 往往在高增益的同时付出较大的遗忘代价。

3.1 学习率的"记忆代价"

研究者还观察到一个极具工程意义的现象：在 SFT 训练中，学习率（LR）与遗忘呈现典型跷跷板关系。

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2FVBcD02jFhgkg3QnfRB9IY0wfeNX3M0RwcH1iavFu9TGCIxL3BWO48ib2ExQS8O48rhA64mX5eofWo5VmQnZdvlxw%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26tp%3Dwebp%26wxfrom%3D5%26wx_lazy%3D1%23imgIndex%3D14&valid=false)

▲ 图6. SFT 学习率越高，遗忘越重

高 LR 能迅速提高 IFEval 指标，却导致 MMLU、Countdown 显著下降；降低 LR 虽能缓解遗忘，但目标任务几乎停滞不前。这进一步印证了方法部分的小模型结论：SFT 的问题不是学习率选不好，而是它始终在"过时的数据"上更新。

3.2 定量结果：RL 的遗忘几乎为零

论文在表 1 中列出了不同方法在三个任务上的定量结果：SFT 通常会出现明显的性能下降（Drop≈-3\~-7），而 REINFORCE 与 GRPO 的 Drop 几乎为 0，甚至在部分任务中呈现轻微正增益。

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2FVBcD02jFhgkg3QnfRB9IY0wfeNX3M0RwGrg4oDWhvkbfsHql3iaR7ggeemKYZjyTQt9iaIeCrhlxWBCXAfLV69vA%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26tp%3Dwebp%26wxfrom%3D5%26wx_lazy%3D1%23imgIndex%3D15&valid=false)

▲ 表1. 不同方法在三任务上的性能对比

RL 在所有任务上都展现出稳定的"无遗忘"特性，SFT 则存在明显退化。

3.3 让 SFT 学会"像 RL 一样学习"

论文最后探讨了一个务实问题：既然 RL 的稳定性来自 on-policy 数据，能否让 SFT 模拟这种"动态更新"机制？

于是作者提出了两种方案：Iterative-SFT（每个 epoch 用当前模型重新生成训练样本）与 RL-to-SFT（先用 RL 采样，再用这些数据做 SFT）。

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2FVBcD02jFhgkg3QnfRB9IY0wfeNX3M0RwOnjwsdrOpoT8QoiaRC6sSQwrha2IavqkSXyXxuhPJga6t7kV9iaKnuwQ%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26tp%3Dwebp%26wxfrom%3D5%26wx_lazy%3D1%23imgIndex%3D16&valid=false)

▲ 图7. Iterative-SFT 成功复现 RL 的抗遗忘特性

图中比较了 Qwen 2.5 1.5B 与 7B 模型在 IFEval 与 MMLU 任务上的三种 SFT 变体：Iterative-SFT、Self-SFT 与传统 SFT。

结果显示，Iterative-SFT 的目标任务表现与 RL (GRPO) 相当，非目标任务的性能下降也显著减轻，证明使用近似 on-policy 数据即可复现 RL 的抗遗忘特性。

![](https://image.cubox.pro/cardImg/dgar9t53wlkxwoxr8jtl9e995nidmu3vwglau1xwxuyzv06mn?imageMogr2/quality/90/format/gif/ignore-error/1)

总结：遗忘的本质，是分布错位

从这项研究可以看出，语言模型的"记忆"并非由算法复杂度决定，而与它学习的方式密切相关。当模型持续在自己生成的数据上训练，它会自然维持能力的连贯；而当训练与行为脱节，遗忘就悄然发生。

这让"后训练"问题有了新的视角：对齐并非一定伴随代价，关键是让模型在理解中学习、在行动中巩固。这项工作提醒我们，强化学习的优势或许并不在于奖励信号，而在于它提供了一种更贴近模型自身的学习节奏。

对于未来的大模型训练而言，这可能意味着一个更朴素却深远的启示------模型的稳定记忆，不靠冻结参数，而靠它是否真正"参与了自己的学习过程"。

**更多阅读**


[![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2FPsho9dm7oDEIjnsdmcibpmUEicctXJn2BO0AX9JO5sZtCf1IKh4muZWVicnR8KckNrMmKBkBuBNntZibvZTrGiao2XQ%2F640%3Fwx_fmt%3Dpng%26tp%3Dwebp%26wxfrom%3D5%26wx_lazy%3D1%23imgIndex%3D19&valid=false)](https://mp.weixin.qq.com/s?__biz=MzIwMTc4ODE0Mw==&mid=2247709834&idx=1&sn=2986fb95731ad97b3c473dad0bec0ad1&scene=21\#wechat_redirect)

[![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2FPsho9dm7oDEIjnsdmcibpmUEicctXJn2BOVsB1OYIuQmdU7keLGuNgux2icx0ArbgggzyeTkYtMibUovJEbvUlLDsg%2F640%3Fwx_fmt%3Dpng%26tp%3Dwebp%26wxfrom%3D5%26wx_lazy%3D1%23imgIndex%3D20&valid=false)](https://mp.weixin.qq.com/s?__biz=MzIwMTc4ODE0Mw==&mid=2247709503&idx=3&sn=eede2987d8a2ac7125285ebfb7aa9d1f&scene=21\#wechat_redirect)

[![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2FPsho9dm7oDEIjnsdmcibpmUEicctXJn2BOsVNDKsAwGqXKE7pFZiahRYZnNpfysfibauP3xnnxJMcxcniaSS4cWEO2g%2F640%3Fwx_fmt%3Dpng%26tp%3Dwebp%26wxfrom%3D5%26wx_lazy%3D1%23imgIndex%3D21&valid=false)](https://mp.weixin.qq.com/s?__biz=MzIwMTc4ODE0Mw==&mid=2247709412&idx=2&sn=b9fd526b87e266001c746686cb9c2078&scene=21\#wechat_redirect)


![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_gif%2FPsho9dm7oDHHMXQ2IicFvJwssWxgWhKuK7ulQVyw7gPTxZia00vCxia2vzhRH6pGq8t1FN1zY48ibULAEZpic41k6eg%2F640%3Fwx_fmt%3Dgif%26tp%3Dwebp%26wxfrom%3D5%26wx_lazy%3D1%23imgIndex%3D22&valid=false)

**\#投 稿 通 道\#**


**让你的文字被更多人看到**


如何才能让更多的优质内容以更短路径到达读者群体，缩短读者寻找优质内容的成本呢？**答案就是：你不认识的人。**

总有一些你不认识的人，知道你想知道的东西。PaperWeekly 或许可以成为一座桥梁，促使不同背景、不同方向的学者和学术灵感相互碰撞，迸发出更多的可能性。

PaperWeekly 鼓励高校实验室或个人，在我们的平台上分享各类优质内容，可以是**最新论文解读** ，也可以是**学术热点剖析** 、**科研心得** 或**竞赛经验讲解** 等。我们的目的只有一个，让知识真正流动起来。

📝 **稿件基本要求：**

• 文章确系个人**原创作品** ，未曾在公开渠道发表，如为其他平台已发表或待发表的文章，请明确标注

• 稿件建议以 **markdown** 格式撰写，文中配图以附件形式发送，要求图片清晰，无版权问题

• PaperWeekly 尊重原作者署名权，并将为每篇被采纳的原创首发稿件，提供**业内具有竞争力稿酬** ，具体依据文章阅读量和文章质量阶梯制结算

📬 **投稿通道：**

• 投稿邮箱：hr@paperweekly.site

• 来稿请备注即时联系方式（微信），以便我们在稿件选用的第一时间联系作者

• 您也可以直接添加小编微信（**pwbot02** ）快速投稿，备注：姓名-投稿

**△长按添加PaperWeekly小编**


🔍

现在，在**「知乎」** 也能找到我们了

进入知乎首页搜索**「PaperWeekly」**

点击**「关注」** 订阅我们的专栏吧

·


[Read in Cubox](https://cubox.pro/web/card/7382731199472471519)
