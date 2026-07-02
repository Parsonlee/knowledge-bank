---
id: "7154617028760832099"
cubox_url: https://cubox.pro/web/card/7154617028760832099
url: https://mp.weixin.qq.com/s/syCREjY7YIg8LIsDzj6EPQ
tags:
  - Recommendation

---
# 即插即用、简单有效的大语言模型推荐算法！港大联合百度推出RLMRec

本文提出了一种名为 RLMRec 的模型无关框架，利用大型语言模型（LLMs）来改善推荐算法的表征学习。

[Read in Cubox](https://cubox.pro/web/card/7154617028760832099)  
[Read Original](https://mp.weixin.qq.com/s/syCREjY7YIg8LIsDzj6EPQ)  

---


---

\## 📖 正文全文

# 即插即用、简单有效的大语言模型推荐算法！港大联合百度推出RLMRec

[mp.weixin.qq.com](https://mp.weixin.qq.com/s/syCREjY7YIg8LIsDzj6EPQ)让你更懂AI的 PaperWeekly

![图片](https://image.cubox.pro/cardImg/2024020719472869277/74727.jpg?imageMogr2/quality/90/ignore-error/1)

![图片](https://image.cubox.pro/cardImg/2024020719472925901/70403.jpg?imageMogr2/quality/90/ignore-error/1)

**论文链接：**

https://arxiv.org/abs/2310.15950

**论文代码：**

https://github.com/HKUDS/RLMRec

**实验室主页：**

https://sites.google.com/view/chaoh/group-join-us?authuser=0

![图片](https://image.cubox.pro/cardImg/2024020719472946672/22510.jpg?imageMogr2/quality/90/ignore-error/1)

**TLDR**

本文从互信息最大化的理论角度出发，通过引入文本信号以优化推荐算法的表征学习中存在的噪音，并且设计一套高效且无偏的基于大语言模型的用户/商品画像生成流程以提供优质的文本信号，最终通过基于对比式学习和生成式学习两套范式实现了互信息最大化的目标，在不同的任务场景下体现出了优势。

![图片](https://image.cubox.pro/cardImg/2024020719472922105/77405.jpg?imageMogr2/quality/90/ignore-error/1)

**从有噪的表征学习说起**

推荐系统已经成为互联网的一种基本服务，其通过学习用户历史交互行为中的偏好，向用户推荐个性化的商品。目前，基于图神经网络（Graph Neural Networks）的协同过滤算法在推荐领域体现出了巨大的优势。

一般来说，在协同过滤（Collaborative Filtering, CF）的场景下，我们拥有用户集合 U 和商品集合 I，以及他们之间的交互，那么如果我们将每一个用户和商品分别视为节点，并且将他们之间的交互记录视为边，就能够构造一个用户商品交互图（User-Item Interaction Graph）。

接着基于图神经网络的层层信息传递和聚合，我们可以最终得到每一个用户和商品节点基于图结构所学习到的表征，由于该表征包含了协同过滤的信息，因此我们可以称之为**协同过滤特征表示**（CF-side Representation）。

![图片](https://image.cubox.pro/cardImg/2024020719472977629/78469.jpg?imageMogr2/quality/90/ignore-error/1)

然而不可避免地，在用户和商品的交互图中存在着许多噪音（例如用户的误点击行为，用户购买过某商品之后发现并不喜欢等等情况），因此图上的某些边（交互）并不一定是正向的，即不能体现用户真正的购物偏好。

但是在模型优化的过程中，这些交互边任然会被视为是正样本，通过 BPR 损失对模型的参数进行优化，从而相关有噪的信息就被嵌入到图网络模型所学习到的表征中，因此最终变成了有噪的表征学习过程。

![图片](https://image.cubox.pro/cardImg/2024020719472954784/63862.jpg?imageMogr2/quality/90/ignore-error/1)

**引入文本信号从理论上优化表征**

如果没有额外的信息，仅仅依靠于用户-商品的交互图，想要挖掘出这些噪音边并且去掉是比较困难的，因此，我们考虑引入别的信号，即文本信号。

<br />

在这里我们首先对**协同过滤特征表示**（CF-side Representation）进行剖析，既然它是有噪声影响的，同时又是有益于推荐的，那么其实在该特征中存在着两种成分：（i）一部分是有益的于推荐的成分，其蕴含了用户/商品的交互行为的偏好；（ii）另一部分是包含噪音的成分，这是我们想去除的。

那么接下来我们考虑，如果存在着另一种模态的特征表示，它其中同样也蕴含着有益于推荐的成分，接着我们极大化两种特征表示中共存的部分（即交集），就可以压缩原本存在的噪音的部分，从而实现对表征学习的优化。

<br />

什么样的模态能够直白的表示出用户和商品的交互偏好呢？很显然，我们可以直接通过文本的形式将其体现出来，例如我们可以以**文本的形式**直接描述某个用户喜欢什么类型的商品。

我们需要将自然语言的文本转换成嵌入的形式（Sentence-to-Embedding），我们称之为语义特征表示（Semantic Representation），在编码的过程中，其不可避免的也会将一些我们不想要的信息嵌入进去，例如语言本身的语法等等内容，因此我们考虑文本模态的特征也有包含一部分的噪音。因此，上述完整的流程，可以形象化的体现为如下形式：

![图片](https://image.cubox.pro/cardImg/2024020719472931321/96136.jpg?imageMogr2/quality/90/ignore-error/1)

我们通过一定的理论推导，假设所有文本模态的特征表示都是预先获得好且固定不变的，那么上述的优化过程等同于：**最大化两种模态特征表示的互信息**（Mutual Infomation）。

<br />

接着，由于特征都是通过神经网络编码而得，因此我们无法直接准确的计算互信息，转而进一步推导，我们获得了基于 InfoNCE 的互信息变分下届（Variational Lower Bound），并且通过最大化互信息变分下届的方式实现对互信息的优化。

![图片](https://image.cubox.pro/cardImg/2024020719473074049/21699.jpg?imageMogr2/quality/90/ignore-error/1)

在该优化公式中，存在一个我们称之为 critic function 的函数 ，其基于两种模态特征的输入，并且输出一个实数来体现其相似度。到此为止，我们已经获得了一个基本的蓝图，需要引入额外的模态，并且实现户信息的最大化优化。从实践的角度来说，存在有两个呆解决的挑战：（i）如何获得高质量的用户/商品文本表征？（ii）如何有效的实现 critic function 的计算？我们将继续进行讲解。

![图片](https://image.cubox.pro/cardImg/2024020719473089827/18523.jpg?imageMogr2/quality/90/ignore-error/1)

**基于大语言模型的文本表征获取**

首先我们想获得高质量的文本表征（Semantic Representation），我们先需要有高质量的文本，也就是用户和商品的画像，由于他们需要能够体现出其在推荐场景下的交互偏好，因此我们考虑该画像中应该要体现以下信息：（i）**用户画像**：体现出该用户喜欢什么类别的商品（ii）**商品画像**：体现出该商品会吸引什么样的用户群体。

然而，由于推荐数据的原始数据集中，并不一定直接拥有这样的文本描述，转而是大量原始的文本内容（例如用户反馈，商品标签等信息），同时也可能存在有许多噪音（例如用户反馈中存在有大量的噪音文本）。

因此，在这一步为了能够高效的获取上述画像，我们需要使用大语言模型（Large Language Models）的文本理解能力，同时也需要设计出一套合理的画像生成流程，以实现无偏的画像生成，描述出用户和商品真正的交互偏好。

基于此，我们设计了一套先商品后用户（Item-to-User）的生成流程以适配不同数据集所拥有的原始文本信息，从顺序上的角度来说，我们先生成所有商品的画像，然后再生成所有用户的画像。由于我们需要基于大语言模型进行画像的推理，因此这一步的核心要义就是如何去构建 Prompts，并且在其中包含足够的信息，以供语言模型准确的抓住用户和商品的交互行为，实现无偏的推理。

![图片](https://image.cubox.pro/cardImg/2024020719473093499/22998.jpg?imageMogr2/quality/90/ignore-error/1)

首先，对于**商品画像的生成（Item Profile Generation）**，我们考虑两种情况，第一种是在数据集中存在有对该商品的描述，例如在 Amazon-book 数据集中，就存在有对书本的原始描述，如果是该情况，则直接将原始描述用于构建 Prompts。

<br />

第二种情况就是在数据集中存在有对商品的属性标签以及用户反馈，例如在 Yelp 数据集中就有用户反馈信息和 POI 的基本标签，那么基于此我们认为也足够用于语言模型进行无偏地推理商品画像。其次，对于**用户画像的生成（User Profile Generation）**，我们考虑基于该用户购买过的商品以及其对该商品留下的反馈来构建 Prompts。

由于我们已经在之前生成了所以商品的画像，因此此处我们就可以配合商品画像以及用户对该商品的反馈以提供足够的信息，由于用户对商品的反馈中体现出了用户是否真的喜欢该商品，因此其蕴含的信息是十分充分且直接的。

值得指出的是，上述提供的流程在实现画像生成的时候每个用户和商品都是独立生成的，因此可以实现并行生成以提高效率，同时我们也使用了思维链的思想构建 Instruction，让语言模型在推理的过程中同时给出理由，以提高最终获得的画像质量。关于具体生成的 Instruction 的设计可以参考原文和开源代码中提供的例子。

![图片](https://image.cubox.pro/cardImg/2024020719473072266/41023.jpg?imageMogr2/quality/90/ignore-error/1)

完成了上述的画像生成过程，我们就实现了为用户-商品交互图上的每一个节点提供了高质量的文本描述（Text Description），这也同时实现了文本标注图（Text-attributed Graph, TAG）的构建。

接着，我们就可以利用文本编码器（Embedder）将一段文本转换成特征表示，我们通过实验发现，越优异的文本编码器对后续算法的性能帮助越大，因此此处我们使用了OpenAI 提供了 text-embedding-ada-002 作为编码器。

![图片](https://image.cubox.pro/cardImg/2024020719473069811/53754.jpg?imageMogr2/quality/90/ignore-error/1)

**互信息最大化**

通过上述的过程我们已经实现了第一个目标，即文本模态特征表示（Semantic Representation）的获取，接下来我们就要实现对于 critic function 的建模，以实现最终对互信息的优化。此处我们考虑了如下两种实现方式。

第一种是对比式对齐建模（Contrastive Alignment, RLMRec-Con），我们通过多层线性感知机将文本表征进行降纬，使其和协同过滤表征具有同一个维度，接着利用余弦相似度配合指数函数计算函数值。形象上来说，对比式对齐实现了两个模态特征的双向对齐。

![图片](https://image.cubox.pro/cardImg/2024020719473076677/34002.jpg?imageMogr2/quality/90/ignore-error/1)

第二种是生成式**对齐建模**（Generative Alignment, RLMRec-Gen），此处我们首先随机选择图上节点，将其初始特征替换成 \[MASK\] token，接着利用多层线性感知机将该节点的协同过滤表征进行放大至于文本模态一个维度，并且同样利用余弦相似度配合指数函数计算函数值。形象上来说，生成式对齐符合 Mask-autoencoding 的思想，实现了从协同过滤模态向文本模态的单向重构。

![图片](https://image.cubox.pro/cardImg/2024020719473159507/77803.jpg?imageMogr2/quality/90/ignore-error/1)

最后，由于我们的互信息最大化是一个额外的优化目标，因此我们所提出的算法是一个**模型无关**（model-agnostic）的框架，我们称之为 RLMRec，其可以无缝嵌入到任何以表征学习（Representation Learning）为基础的协同过滤推荐算法中。

![图片](https://image.cubox.pro/cardImg/2024020719473111583/19029.jpg?imageMogr2/quality/90/ignore-error/1)

![图片](https://image.cubox.pro/cardImg/2024020719473143573/49702.jpg?imageMogr2/quality/90/ignore-error/1)

**实验效果**

我们在协同过滤的数据集（Amazon-book，Yelp，Steam）上面进行了测试，并且将我们的框架和现有的最先进的基于图神经网络的推荐算法（GCCF, LightGCN, SGL, SimGCL, DCCF, AutoCF）进行了组合，均提升了现有推荐算法的性能，并且效果的提升具有显著性。

![图片](https://image.cubox.pro/cardImg/2024020719473181472/54328.jpg?imageMogr2/quality/90/ignore-error/1)

接着，我们对文本模态表征执行了消融试验，使用了不同的文本编码器构造了不同质量的模态表征，通过试验发现越好的表征对模型性能的提升越大，同时我们通过随机打乱（Shuffle）文本表征的顺序构造了一个错误对齐的绝对噪声情况，其性能下降最明显，由此进一步证明了越好的文本模态表征对模型性能的帮助越大，也与我们的理论结论相符合。

![图片](https://image.cubox.pro/cardImg/2024020719473184099/79750.jpg?imageMogr2/quality/90/ignore-error/1)

其次，我们执行了噪声试验，通过在原始数据上加入一定比例的随机噪声（加入随机交互边），然后验证对比式对齐（RLMRec-Con），生成式对齐（RLMRec-Gen）以及原始模型在上面的性能。

通过试验我们发现，RLMRec-Con 和 RLMRec-Gen 在任意噪声情况下都能过对原始模型有一定的性能提升，体现了其抵抗噪声的效果。同时，基于对比式对齐的方式在噪声比例越大时，性能下降的比例越小，因此其抵抗噪声的影响是最强的。

![图片](https://image.cubox.pro/cardImg/2024020719473157008/22137.jpg?imageMogr2/quality/90/ignore-error/1)

最后，我们探索了所提出的算法是否能为与预训练（Pre-training）任务提供帮助，我们将 Yelp 数据集按照年份划分成预训练数据和新数据，并且使用不同的方式（RLMRec-Con、RLMRec-Gen、Backbone）在预训练数据上进行表征学习，并且用于初始化在新数据集上面的 Backbone 算法的初始参数，通过 fine-tuning 之后验证结果。

通过结果我们发现：首先 RLMRec 对预训练性能有提升，其次，基于生成式对齐的方式获得的参数更好，由此可见生成式对齐可以有效避免对原始数据的过度拟合，更加适用于预训练任务。

![图片](https://image.cubox.pro/cardImg/2024020719473298447/72565.jpg?imageMogr2/quality/90/ignore-error/1)

在**落地实践**方面，我们在公司的搜索业务场景上利用了 RLMRec 的文本生成和对齐范式，并且对业务模型进行了优化，有效的提升了当前业务模型的性能，并且完成了上线。

![图片](https://image.cubox.pro/cardImg/2024020719473218819/80567.jpg?imageMogr2/quality/90/ignore-error/1)

**结语**

本文提出了一种名为 RLMRec 的模型无关框架，利用大型语言模型（LLMs）来改善推荐算法的表征学习。我们介绍了一种高效且无偏的用户和商品画像生成范式。RLMRec 利用对比和生成式对齐技术将协同过滤侧的特征表示与文本语义特征表示进行对齐，有效地减少特征噪声。

该框架结合了通用推荐系统和 LLMs 的优势，拥有有效的理论保证，并在真实世界数据集上进行了广泛评估。我们将来的研究重点将集中在通过提供更深入的解释来推进基于 LLMs 的推理结果在推荐系统中的应用。

**更多阅读**


[![图片](https://image.cubox.pro/cardImg/2024020719473272116/68488.jpg?imageMogr2/quality/90/ignore-error/1)](https://mp.weixin.qq.com/s?__biz=MzIwMTc4ODE0Mw==&mid=2247651348&idx=1&sn=f675292dc2382fe406cf9a083bc43fe8&chksm=96e44f94a193c682bc73542ebedce862752720146bf6d392a1f338a84064c1d31ffe179cd1b0&scene=21\#wechat_redirect)

[![图片](https://image.cubox.pro/cardImg/2024020719473217270/93134.jpg?imageMogr2/quality/90/ignore-error/1)](https://mp.weixin.qq.com/s?__biz=MzIwMTc4ODE0Mw==&mid=2247641053&idx=2&sn=7aed340d17b677d9bdf72d86f34f3310&chksm=96e4785da193f14bb080397ca23661bc8649a56e4e5ed92fe77f80947db10fa2bf68afe1b2de&scene=21\#wechat_redirect)

[![图片](https://image.cubox.pro/cardImg/2024020719473238905/56481.jpg?imageMogr2/quality/90/ignore-error/1)](https://mp.weixin.qq.com/s?__biz=MzIwMTc4ODE0Mw==&mid=2247640870&idx=2&sn=5431c403cc8d6727bb3a000af26a92bd&chksm=96e478a6a193f1b02fb9b5c97d454c0cd80074c6f392068b39f1d0f3dfec41bd70e8aaf20b67&scene=21\#wechat_redirect)


![图片](https://image.cubox.pro/cardImg/2024020719473357920/23522.jpg?imageMogr2/quality/90/ignore-error/1)

**\#投 稿通 道\#**


**让你的文字被更多人看到**


如何才能让更多的优质内容以更短路径到达读者群体，缩短读者寻找优质内容的成本呢？**答案就是：你不认识的人。**

总有一些你不认识的人，知道你想知道的东西。PaperWeekly 或许可以成为一座桥梁，促使不同背景、不同方向的学者和学术灵感相互碰撞，迸发出更多的可能性。

PaperWeekly 鼓励高校实验室或个人，在我们的平台上分享各类优质内容，可以是**最新论文解读** ，也可以是**学术热点剖析** 、**科研心得** 或**竞赛经验讲解**等。我们的目的只有一个，让知识真正流动起来。

📝**稿件基本要求：**

• 文章确系个人**原创作品**，未曾在公开渠道发表，如为其他平台已发表或待发表的文章，请明确标注

• 稿件建议以**markdown**格式撰写，文中配图以附件形式发送，要求图片清晰，无版权问题

• PaperWeekly 尊重原作者署名权，并将为每篇被采纳的原创首发稿件，提供**业内具有竞争力稿酬**，具体依据文章阅读量和文章质量阶梯制结算

📬**投稿通道：**

• 投稿邮箱：hr@paperweekly.site

• 来稿请备注即时联系方式（微信），以便我们在稿件选用的第一时间联系作者

• 您也可以直接添加小编微信（**pwbot02**）快速投稿，备注：姓名-投稿

![图片](https://image.cubox.pro/cardImg/2024020719473314345/91712.jpg?imageMogr2/quality/90/ignore-error/1)

**△长按添加PaperWeekly小编**


🔍

现在，在**「知乎」**也能找到我们了

进入知乎首页搜索**「PaperWeekly」**

点击**「关注」**订阅我们的专栏吧

·

·


![](https://image.cubox.pro/cardImg/2024020719473345913/72712.jpg?imageMogr2/quality/90/ignore-error/1)


·

![图片](https://image.cubox.pro/cardImg/2024020719473377691/76732.jpg?imageMogr2/quality/90/ignore-error/1)

[Read in Cubox](https://cubox.pro/web/card/7154617028760832099)
