# MiniMax和Kimi为了"注意力"，隔空交手

[mp.weixin.qq.com](https://mp.weixin.qq.com/s?__biz=MzkyNjU2ODM2NQ==&mid=2247619925&idx=1&sn=375f3d4c9dfae099424769ecd31c9ddf&poc_token=HLFJEWmjOjKhclaNoe8QweFOQ3k4Rfpj1MU8HpYN)周一笑 硅星人Pro


![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2FjopKOlhibRBKahrJg67568mZd8ntKfPJ3N7LMCoA9qQHlhiacQNARo4mPljOzPw2FHfoQjFk8v7iaT0iczNqNa3kTQ%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26tp%3Dwebp%26wxfrom%3D5%26wx_lazy%3D1%23imgIndex%3D0&valid=false)

作者*｜* 周一笑  
邮箱*｜* zhouyixiao@pingwest.com

10月29日，月之暗面研究员周昕宇（Zhou Xinyu）在X上转发了MiniMax M2 Tech Blog的推文，并评论道："Minimax don't worry, Kimi got your back 😘"。不仅如此，他还在知乎的同一篇博文下留下了同样的评论，这种带有调侃意味的公开"示好"，既像挑逗，也像挑衅。
![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2FjopKOlhibRBKahrJg67568mZd8ntKfPJ34BjgcXRicYuSIS5E0ZpZGeQeeIfaybucHSTSJOX1Xyfv2YPDAa6Ow5w%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26tp%3Dwebp%26wxfrom%3D5%26wx_lazy%3D1%23imgIndex%3D1&valid=false)

在M2发布两天后，MiniMax的预训练负责人孙浩海（Haohai Sun）在知乎和X发布了一篇技术博客，罕见地坦诚地说明了团队为什么放弃efficient attention，"为什么不做linear/sparse attention"？"一直在做，但是在工业系统里真的打过Full Attention还有些距离"

周昕宇的评论显然有所指，但"got your back"究竟是什么意思？答案在24小时后揭晓。10月30日，月之暗面发布了Kimi Linear，一个48B参数的混合注意力模型，声称在长上下文任务中KV Cache减少75%，吞吐量提升6倍。

技术报告的Abstract写道："for the first time, outperforms full attention under fair comparisons across various scenarios"（首次在公平对比下全面超越全注意力）。

从MiniMax M2发布到Kimi Linear发布，恰好72小时。这种技术路线扽差异是大模型行业在效率与性能之间的路线探索，争论仍未尘埃落定。


1

**MiniMax M2：回归Full Attention**

MiniMax此前的M1 Lightning采用Softmax + MoE的混合式架构，支持百万级上下文。到了M2，MiniMax选择了回归Full Attention。

M2的定位是Agent和代码生成，强调"大巧若拙"的产品哲学。在价格上，M2仅为Claude Sonnet 4.5的8%（每百万Token输入0.3美元），推理速度快近2倍（TPS约100）。MiniMax在官方发布文章中表示，这是通过"高效的激活参数设计"实现的"智能、速度与成本的最佳平衡"。
![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2FjopKOlhibRBKahrJg67568mZd8ntKfPJ3weNFRYlFrmc0nReoliapBibRXqVfo32H7EYA2p55c56Yda3R29FLnia5g%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26tp%3Dwebp%26wxfrom%3D5%26wx_lazy%3D1%23imgIndex%3D2&valid=false)

《为什么M2是Full Attention》这篇文章在知乎和X都获得了不少好评。X上的评论者认为这是"难得的工程视角分享"，"对行业非常有价值"。一位名为@TensorTemplar的评论者说："难得见到如此详尽公开分享模型架构的整体工程视角。关于稀疏注意力尾部风险的论述非常精彩！在复杂多轮使用场景中尚未证明其等效性前，我暂不愿称之为'高效'。"
![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2FjopKOlhibRBKahrJg67568mZd8ntKfPJ3mL7eshOssrpicunjichl5rkq5z4ibJSkXddPrOlYZGGVaj7MJnzXUA7bg%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26tp%3Dwebp%26wxfrom%3D5%26wx_lazy%3D1%23imgIndex%3D3&valid=false)

Haohai详细阐述了三个核心困难。第一个是工程链路复杂性爆炸。用他的话说，"需要同时满足code/math、agent、多模态、Long CoT、RL、低精度运算、缓存、speculative decoding等众多场景"。翻译成人话就是，现代大模型不只是做一件事，而是要同时支持十几种不同的应用场景。每增加一种efficient attention机制，就要在所有这些场景下验证，工程复杂度呈指数级增长。

第二个困难是评测体系局限。"小规模实验的结论无法外推，复杂多跳推理任务的缺陷只在大规模时暴露。"在小模型上测试效果好，不代表在大模型上也好。很多问题只有在训练到一定规模时才会暴露，但那时候已经投入了大量资源，来不及调整。Haohai在评论区补充说，复杂多跳推理任务可以参考KorBench、BBEH等榜单，以及BBH里的dyck language任务。

有评论者问"你们是否尝试过其他线性注意力变体，比如门控Delta Net或Mamba2？"Haohai回复："GDN混合模型表现尚可，Mamba2 \< Mamba2 + qknorm ≈ GDN。但与全注意力模型相比，这些模型在推理密集型基准测试（如BBH）中表现相对较弱。"MiniMax在实际测试中发现了问题。

第三个困难是基建不完善。"Linear Attention的训练是访存bound，推理需要解决低精度存储、Prefix Cache、投机解码等问题。"即使理论上linear attention更快，但实际工程中需要解决很多基础设施问题。训练时内存带宽成为瓶颈，推理时需要支持各种优化技术，这些都还没有成熟的解决方案。

这篇博客的评论区也透露了一些重要信息。一位名为silicon的开发者评论道："我自己都开发了近百种Transformer变体了，但'验证新变体是否先进'所花的时间远远大于开发算法的时间"。Benchmark困境不只是MiniMax的问题，而是整个行业的痛点。

另一个问题是关于成本和时延的澄清。当有网友问"Agent场景下Full Attention会成为瓶颈吗"时，Haohai回答是："GPU的进步非常快，对Full Attention来说目前只有成本问题，没有时延问题。"也就是说核心矛盾不是速度慢，而是成本高。MiniMax的策略是等待GPU进步解决成本问题，同时通过工程优化（如"高效的激活参数设计"）来平衡性能和成本。


1

**月暗的"挑逗"和Kimi Linear的发布**

Zhou Xinyu是月之暗面的研究员，也是MoBA（Mixture of Block Attention）论文的核心作者之一，他的"挑逗"背后藏着一个大招。10月30日晚，月之暗面发布了Kimi Linear，一个48B总参数、3B激活参数的MoE模型，训练数据达5.7T tokens，支持1M tokens的上下文长度。模型权重、代码和技术报告全部开源。从M2发布到Kimi Linear发布，72小时。

Kimi Linear有三个值得注意的点。

第一个是Kimi Delta Attention (KDA)。KDA基于Gated DeltaNet，引入了fine-grained gating机制。具体来说，它从scalar gate（标量门控）升级到channel-wise gate（通道级门控），让每个特征维度都有独立的遗忘因子。用人话说，就像给模型装了更精细的"记忆开关"。传统的门控机制是一个总开关，要么全记住，要么全忘记。而KDA可以针对不同类型的信息分别控制记忆强度，比如对代码语法记得牢一点，对临时变量忘得快一点。这个改进带来了显著的性能提升，相比标准DPLR实现，KDA的计算效率提升了约100%。

第二个是3:1的混合比例。Kimi Linear采用了Hybrid架构，将KDA（线性注意力）和MLA（Multi-head Latent Attention）混合使用。MLA是DeepSeek在V2/V3中使用的技术，通过将注意力输入压缩成低维潜在向量，然后在需要计算注意力时映射回高维空间，显著减少了内存需求。关键问题是混合的比例应该是多少？Kimi团队通过系统性的ablation study找到了答案：3:1，也就是每3层KDA配1层MLA。

实验结果显示，3:1是平衡性能和效率的最佳点。纯MLA（0:1）的validation PPL是5.77，3:1是5.65，1:1是5.66，7:1是5.70，15:1是5.82。太多全注意力（1:1）浪费资源，太少（7:1、15:1）影响性能。

Kimi Linear 模型架构示意图。该模型由一系列堆叠的模块组成，每个模块包含一个 token 混合层（token mixing layer），其后接一个 MoE 通道混合层（channel-mixing layer）。

第三个是No Position Encoding (NoPE)。Kimi Linear的MLA层不使用位置编码（如RoPE），所有的位置信息完全由KDA层负责。这个设计带来三个好处：推理效率更高（MLA可以转换为更高效的MQA）、训练更简单（避免了RoPE参数调整）、长上下文泛化更好。

Kimi Linear的性能数据很亮眼。技术报告显示，Kimi Linear"显著减少了高达75%的KV cache需求"，这意味着内存占用降低4倍，直接降低了部署成本。在1M tokens的长上下文场景中，Kimi Linear的解码吞吐量比MLA（全注意力）快6.3倍。具体数据是TPOT（Time Per Output Token）从11.48ms降到1.84ms。

在RULER基准测试（128k context）上，Kimi Linear达到84.3的性能，同时速度是MLA的3.98倍。技术报告称这是"Pareto-optimal"，性能和速度都是最优，没有trade-off。

Kimi团队用1.4T tokens的训练验证了scaling law。MLA的Loss是2.3092 × C\^(-0.0536)，Kimi Linear是2.2879 × C\^(-0.0527)。技术报告总结："Kimi Linear achieves ∼ 1.16× computational efficiency"。大规模训练中，Kimi Linear仍然优于Full Attention。

为了验证理论正确性，Kimi团队在三个合成任务上测试了KDA：Palindrome（回文任务）、MQAR（多查询关联回忆）、Stack（栈追踪）。KDA在所有任务上都达到100%准确率，而GDN和Mamba2在长序列上失败。这些任务测试的正是复杂多跳推理能力。

这也是Linear attention首次在公平对比下全面超越Full Attention。不是特定任务，而是"across various scenarios"（各种场景），包括short-context、long-context、RL scaling。

Kimi Linear的工程化成熟度还体现在vLLM集成上。vLLM是UC Berkeley开发的开源LLM推理框架，是全球最主流的推理引擎之一。Kimi Delta Attention（KDA）算子已被vLLM官方整合进主代码库。这意味着vLLM用户只要升级到最新版本，就可以直接使用Kimi的注意力实现。


1

**MiniMax向左，Kimi向右**

MiniMax和Kimi的选择，代表了两种不同的技术路线。整个行业也都在探索，DeepSeek用MLA 改造/压缩KV-cache，Mistral引入滑动窗口稀疏模式，OpenAI与Anthropic的具体注意力实现未公开，业内普遍认为其以Full Attention的工程化加速为主。

不同选择反映了效率与性能的不同权衡。MiniMax选择Full Attention，核心逻辑是等待GPU进步解决成本问题，同时通过工程优化来平衡性能和成本。Full Attention是经过多年验证的技术，不需要担心在某些场景下的隐藏弱点。

Kimi选择KDA + MLA，核心逻辑是主动优化架构降低成本，系统性解决工程化问题。这种选择的优势是效率更高、成本更低、长期可能竞争力更强，但也面临更大的工程挑战，需要在多个场景下验证稳定性。Kimi Linear的发布证明，至少在月之暗面的技术体系中，他们找到了可能的解决方案。

两种选择都有其合理性。MiniMax的策略是时间换空间，赌GPU进步会解决成本问题。Kimi的策略是空间换时间，通过技术创新主动降低成本。哪种路线更好？目前还没有定论。

不过，这种不同路线的探索和公开的技术讨论，对整个行业都是一件好事。它让外界看到了大模型技术演进的真实图景，没有正确答案，而是多条路径的并行探索。MiniMax和Kimi的坦诚和创新，都在推动行业进步。

但在技术探讨之外，两家公司在实际层面的竞争也不容忽视。月之暗面和MiniMax都定位于中国头部通用大模型，在长上下文、代码/Agent、开源推理生态等方面同场竞跑。技术路线的选择不仅关乎技术本身，也关乎资本市场的认可和长期竞争力。

这是Full Attention和Efficient Attention两种技术路线的较量，也是MiniMax和Kimi两家公司的角力，两件事情都会持续下去。这场关于Attention机制的技术之争，本身也成了一场"注意力之争"。

**[](https://mp.weixin.qq.com/s?__biz=MzkyNjU2ODM2NQ==&mid=2247618902&idx=1&sn=7e9f8a5662155b89e5b4c8b51602a59d&scene=21#wechat_redirect)[](https://mp.weixin.qq.com/s?__biz=MzkyNjU2ODM2NQ==&mid=2247619248&idx=1&sn=6d38650c1d2bf02a68c6aa2d125f4be0&scene=21#wechat_redirect)[](https://mp.weixin.qq.com/s?__biz=MzkyNjU2ODM2NQ==&mid=2247619911&idx=1&sn=3ab03dd0e3a8ff7a0628f93c7783d55a&scene=21#wechat_redirect)[](https://mp.weixin.qq.com/s?__biz=MzkyNjU2ODM2NQ==&mid=2247619824&idx=1&sn=86a6231ed3b91532e32c7a2ae3535dbc&scene=21#wechat_redirect)
[](https://mp.weixin.qq.com/s?__biz=MzkyNjU2ODM2NQ==&mid=2247618885&idx=1&sn=7b3d9ce6ecadb22bb07261a291520297&scene=21#wechat_redirect)[](https://mp.weixin.qq.com/s?__biz=MzkyNjU2ODM2NQ==&mid=2247619752&idx=1&sn=fa54a3a1d4c6c84af52eb3a489e0d3a6&scene=21#wechat_redirect)
**点个**"爱心"** ，再走吧****

[Read in Cubox](https://cubox.pro/web/card/7387381961167212077)
