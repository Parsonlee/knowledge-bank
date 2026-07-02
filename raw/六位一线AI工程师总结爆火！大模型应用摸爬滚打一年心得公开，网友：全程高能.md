---
id: "7196553461914143318"
cubox_url: https://cubox.pro/web/card/7196553461914143318
url: https://mp.weixin.qq.com/s/LwNFfwiHCED9AjB2su0C-g
tags:
  - AI-Agent/coding
---
# 六位一线AI工程师总结爆火！大模型应用摸爬滚打一年心得公开，网友：全程高能

提示词、RAG、微调、评估与监测……全讲了

[Read in Cubox](https://cubox.pro/web/card/7196553461914143318)  
[Read Original](https://mp.weixin.qq.com/s/LwNFfwiHCED9AjB2su0C-g)  

---


---

## 📖 正文全文

# 六位一线AI工程师总结爆火！大模型应用摸爬滚打一年心得公开，网友：全程高能

[mp.weixin.qq.com](https://mp.weixin.qq.com/s/LwNFfwiHCED9AjB2su0C-g)关注前沿科技 量子位

##### 梦晨 西风 发自 凹非寺
量子位 \| 公众号 QbitAI

**六**位**一**线AI工程师和创业者，把在**大模型应用开发上摸爬滚打一整年的心得**，全！分！享！了！

（奇怪的六一儿童节大礼包出现了）

这篇干货长文，一时间成为开发者社区热议的话题。

![](https://image.cubox.pro/cardImg/4w9lpo33oscgpllvp3y0ioi85onbryfkz7lsn2xja4vj6jyo59?imageMogr2/quality/90/ignore-error/1)

有网友评价为，大模型领域少有的**"有操作性"**的实用见解，非常值得一读。

![](https://image.cubox.pro/cardImg/29mrkhwfjib2sri34nru7p54xb7p37xyzmlp3wdufvprvapeyf?imageMogr2/quality/90/ignore-error/1)

这6位作者来自不同背景，比如有大厂工程师，也有独立开发者，还有咨询顾问。

但他们的共同之处，是过去一年里一直在大模型之上构建真实应用程序，而不只是炫酷的Demo演示，他们认为：
> **现在正是非机器学习工程师或科学家，也能把AI构建到产品中的时候。**

在他们的一系列分享中，网友热议的亮点包括但不限于：

-何时用长上下文、何时RAG、何时微调模型

* 多样化输出不止提高温度，改变提示词中示例的顺序也影响结果

* 长上下文不会让RAG过时

* "实习生测试"：如果大学生能根据提示词完成任务，说明比较完善了

* 每个大模型都有自己的偏好，Claude更喜欢XML格式，GPT系列更喜欢Markdown和JSON

* 如果靠提示词已完成了90%的任务，微调可能就不值得投资

* 大模型当裁判评估结果可能起作用，但不是万能的  
  ......

总之，无论是大厂工程师、创业者还是参加个人开发者，都值得一看。

## 全程高能干货分享

提示词、RAG和微调都是改善大模型输出结果的有效方法。

但是何时该用何种方法，还没有定论。

作者们认为，需要根据具体的应用场景、任务需求、成本效益和性能目标来做出决策：

* **建议在开发新应用程序时从提示词开始**

* **需要大模型掌握新知识时优先使用RAG**

* **当需要针对特定任务优化时再考虑微调**

最后，他们还重点讨论了对大模型应用的评估和监测，认为是应该贯穿开发全流程的重要环节。

#### 提示词篇

很多开发者都陷入了一个误区：以为设计一个**涵盖一切的"终极提示词"**就能完美解决问题。

就像过去软件开发中也有希望一个类或函数可以完成所有事情的误区。

实际情况**恰恰相反**，随着需求的复杂化，这样的Prompt会越来越臃肿，性能反而每况愈下。

![](https://image.cubox.pro/cardImg/1zulkmdj6u8tganfvyg0w9it23hq0iyt81nldiymj2i4p0m5xt?imageMogr2/quality/90/ignore-error/1)

那么正确的做法是什么呢？提示词也应该**像代码一样保持简洁**，以**会议记录总结场景**来说，可以分解为以下步骤：

* 将关键决策、待办事项和执行者提取为结构化格式

* 检查提取的详细信息与原始会议记录的一致性

* 从结构化详情生成简明摘要

![](https://image.cubox.pro/cardImg/2u42kqfrk1ax29kq97tcig0fqwajud4vmtka8hyr1jcwjiytie?imageMogr2/quality/90/ignore-error/1)

通过拆分，每个提示词都简单、突出重点且易于理解，更重要的是接下来可以单独迭代和评估每个提示词。

比如思维链鼓励AI在最终回答之前写下思维过程，除了"一步一步思考"之外，还可以用一些技巧显著降低幻觉。

还以会议记录总结场景为例，迭代后的提示词示例为：

    - 首先，在草稿中列出关键决策、待办事项和相关执行者。
    - 然后，检查草稿中的细节是否与文字记录相符。
    - 最后，根据要点合成简洁的总结。

![](https://image.cubox.pro/cardImg/2l3c5u0nk01gfwiwthii0vx1k9q08kdlyu6z5ljsye4x0vf77h?imageMogr2/quality/90/ignore-error/1)

在提示词方面，作者们还提出了更多具体经验。

对于给大模型提供示例的上下文学习：

* 提示词中的**示例数量**追求**≥5**（也不要害怕用上几十个）。太少会让模型过度遵循特定示例、损害泛化能力。

* **示例应该反映预期的输入分布**。比如做电影剧情总结，示例中不同类型电影的比例大致应与实践中期望看到的相同。

* **不一定需要提供完整的输入-输出对**。在许多情况下，只有输出的示例就足够了。

* 如果所用的大模型支持工具调用，则**示例也应包含希望AI使用的工具**。

对于结构化输入输出：

* **优化上下文结构**，让模型更容易理解和处理。单纯打包一堆文件人类看着头疼，AI看着也费劲。

* 只保留必要信息，**像雕刻艺术家一样剔除冗余、自相矛盾和格式化错误**。

* 每个大模型都有自己的偏好，**Claude更喜欢xml格式**，**GPT系列更喜欢Markdown和JSON**。

比如给Claude的提示词，甚至可以用xml tag来预填充输出模板。

![](https://image.cubox.pro/cardImg/3ktqcj5su0rehrum121th0b1r5t3c31t33b01a7ynblgyoveof?imageMogr2/quality/90/ignore-error/1)

#### RAG（检索增强生成）篇

**不要忘记关键词搜索**

基于Embedding的RAG演示很多，让人们容易忘记信息检索领域数十年来积累的经验。

作者认为**向量检索无疑是强大的工具，但不是全部**。虽然擅长捕获高级语义相似性，但它们可能难以处理更具体的关键字，比如人名、首字母缩略词或者ID。

不要忘记传统的关键词匹配（如BM25算法），在大多数情况下，混合关键字匹配和向量搜索效果最好：
> 先匹配最明显的关键词，再对同义词、上位概念和拼写错误做向量查询，以及多模态向量查询。

**![](https://image.cubox.pro/cardImg/4zao3hp5r284s8v56o2icf3yctr04fdbrfk0d4lar6h25io3ky?imageMogr2/quality/90/ignore-error/1)**

**RAG输出的质量取决于检索文档的质量**

具体来说，检索文档的质量又取决于几个因素。

第一个也是最明显的指标是**相关性**。与传统推荐系统一样，检索到的项目的排名对大模型输出产生重大影响，要衡量这种影响，可以试试打乱顺序并观察大模型行为变化。

第二个是**信息密度**。如果两份文档同样相关，应该选择更简洁、无关细节更少的那个。

最后是**信息的详细程度**，附加的详细信息可以帮助大模型更好地理解。

![](https://image.cubox.pro/cardImg/2fpwd2x4sjtymywbv77aijo6x3eqeypcqpv8o5hvkdvmjsn3bw?imageMogr2/quality/90/ignore-error/1)

**优先RAG，而不是对新知识微调**

RAG和微调都可让大模型掌握新知识并提高特定任务的性能。那么，应该优先选择哪一个呢？

微软一篇论文比较RAG与无监督微调（又叫持续预训练），发现**对于新知识RAG性能始终优于微调**。

![](https://image.cubox.pro/cardImg/4y89imfps6329o5ntx2ew4y2wfhghmxu34xt6vq5s57vbw4jv6?imageMogr2/quality/90/ignore-error/1)**△** arxiv.org/abs/2312.05934

除了改进性能之外，**RAG容易更新而且成本更低**。如果知识库中发现错误，RAG方法只需简单删除有问题的文档即可。

RAG还可以给文档权限提供更细粒度的控制，确保每个用户只能访问自己有权限的文档，不会泄露信息。

**长上下文不会让RAG过时**

首先，即使上下文窗口达到一千万tokens，仍然需要一种方法来选择要输入模型的信息。

其次，除了简单大海捞针评估之外，**还没有看到令人信服的数据**表明模型可以在如此大的上下文进行有效的推理。

**如果没有良好的检索和排名，干扰因素可能淹没模型**，甚至可能用完全不相关的信息填满了上下文窗口。

最后还有成本问题，ransformer的推理成本随上下文长度二次增长，过度依赖长上下文可能不划算。

![](https://image.cubox.pro/cardImg/x4b0t48u9tpx4h3l5vfww4m9vfuepte3ss0t3r70upq6z9bha?imageMogr2/quality/90/ignore-error/1)

#### 微调篇

**当最巧妙的提示词设计也无法完成一些任务时，可能就需要考虑微调了**。

虽然微调可能是有效的，但它会带来巨大的成本。必须注释微调数据、执行微调和评估模型，并最终自行部署模型。因此，请考虑较高的前期成本是否值得。

作者们的经验是：

* 如果提示词已完成了**90%**的任务，那么微调可能不值得投资。

* 如果确定要微调，可以考虑**合成数据或开源数据集**，降低人工收集注释数据的成本。

#### Agent与工作流

最成功的Agent开发者可能也是工程师团队的管理者，因为**给AI制定计划的过程和管理初级员工的方式类似**。

我们给人类新手明确的目标和具体的计划，而不是模糊的开放式指示，对Agent也应该这样做。

**优先考虑确定性工作流程**

Agent被期待动态对用户请求做反应，但随着执行步数增加，失败的可能性指数增加，并且从错误中恢复的机会很小。

一种有前途的方法是使用Agent系统来生成确定性计划，然后以结构化、可重复的方式执行这些计划，好处包括：

* 生成的计划可以作为提示词中的少数样本，或微调数据。

* 使系统更加容易测试和调试，失败可以追溯到计划中的具体步骤。

* 生成的计划可以表示为有向无环图 (DAG)，相对于静态提示词，它更容易理解和适应新情况。

![](https://image.cubox.pro/cardImg/1yvnmx05f2gf6nh51zmd3uypsvt43avsemo8ihrldfe86jgr0t?imageMogr2/quality/90/ignore-error/1)

**多样化输出不止提高温度**

如果任务需要输出的多样性，比如根据用户之前购买过的产品推荐新产品，简单增加大模型的温度参数可能会产生问题。

如果温度太高，可能会生成不存在的产品，甚至输出乱码。

其他增加输出多样性的方法包括：

最简单的是**调整提示词内的元素顺序**，打乱用户历史购买记录的顺序，就可能产生显著差异。

还可以**在上下文中保留前几轮的输出**，并要求大模型避免重复最近推荐过的产品。

另一个策略是**改变提示词的措辞**，比如"选择用户喜欢经常使用的产品"和"选择用户可能会推荐给朋友的产品"。

![](https://image.cubox.pro/cardImg/56za9enk9frea9bhuz5k33pv47o8s4j26s0mn69ufm80kdab6u?imageMogr2/quality/90/ignore-error/1)

#### 评估与监测

大模型的输入和输出是任意文本，要完成的任务是多种多样的。尽管如此，严格且深思熟虑的评估仍至关重要。

**从真实的输入/输出样本中创建基于断言的单元测试**

作者建议创建由生产中的输入和输出样本组成的单元测试，并基于至少3个指标测试。

3个指标是实践中总结出来的，更少可能表明任务没有充分定义，或过于开放。

这些单元测试应该由工作流的任何更改触发，无论是编辑提示词、通过RAG添加新上下文还是其他修改。

![](https://image.cubox.pro/cardImg/402d4fcd0d29fjk1imkh3of8qy02w1ccet5gay9umiqnft52oi?imageMogr2/quality/90/ignore-error/1)

**大模型当裁判可能起作用，但不是万能的**

作者认为，让最强大的模型当裁判、给其他模型的输出打分，用于**定性比较优劣可能有用** ，但**具体输赢的幅度就没什么参考价值了**。

* 不要让大模型在量表上对单个输出进行评分，而是**提供两个选项，要求选择更好的一个**，这往往会带来更稳定的结果。

* 提供的选项顺序可能会影响结果，为了缓解这种情况，请将每个成对比较进行两次，每次**交换顺序**。

* 在某些情况下，两种选择可能同样好。因此**允许大模型宣布平局**，这样就不会武断地选一个胜者。

* 使用思维链：要求大模型在**给出最终偏好之前解释其决定**，可以提高评估的可靠性，还可以让更小的模型获得与大模型类似的结果。  
  （这部分流程通常处于并行批处理模式，思维链带来的额外延迟并不造成问题。）

* 大模型往往偏向于较长的回答，为减少这种情况，请确保成对的回答长度相似。

![](https://image.cubox.pro/cardImg/343zjtez2di1rfhnv9pt7lxp1ng9iv3zus3zrkwgmxvtj81we1?imageMogr2/quality/90/ignore-error/1)

**"实习生测试"**

如果将提示词（包括上下文）作为一项任务，交给相关专业的普通大学生，他们能成功吗？需要多长时间？

如果大学生都做不到，就该考虑如何给大模型提供更丰富的上下文资料了。

如果根本无法通过改进上下文来解决这个问题，那么这就是对当代大模型来说太难的任务。

如果大学生能做到，但需要一段时间。可以尝试降低任务的复杂性。分解任务，或某些方面是否可以更加模板化。

如果大学生能做到，而且很快，但大模型不行。那么就该深入研究大模型反馈的数据了。尝试找到失败的模式，让模型在输出之前或之后解释自己。

![](https://image.cubox.pro/cardImg/1nvpez9d2s64zo2qml5h5h24g70wfs3sum5p951c2y575106m5?imageMogr2/quality/90/ignore-error/1)

**过分强调某些指标可能影响整体**

著名的古德哈特定律表示，**"当一项指标成为目标时，它就不再是一项好指标"**。

比如针对长上下文的**"大海捞针"测试**最早是网友提出的，迅速成为行业通用方法之后，就**很容易针对性优化、刷榜**。

更好的指标可能正是复杂的实际任务，比如"给定一个小时的会议记录，大模型能否总结出关键决策、待办事项和相关负责人"。

这项任务更切合实际，**超越了死记硬背的范畴**，还考虑到了解析复杂讨论、识别相关信息和归纳总结的能力。

在总结中强调事实一致性可能会导致摘要不那么具体（因此不太可能与事实不一致），也可能不那么相关。

反之，如果强调写作风格和口才，则可能导致更多花哨的话术，从而造成与事实不符的情况。

![](https://image.cubox.pro/cardImg/1tk8y24rfakpb2oy7leokzquyt5in9js09ga7daq85qf47354k?imageMogr2/quality/90/ignore-error/1)

**LLMs甚至会在不应该返回输出时返回输出**

大模型经常会在不应该生成输出的情况下生成输出。可能是无害但无意义的输出，也可能是更严重有害输出。

例如，当被要求从文档中提取特定属性或元数据时，大模型可能会自信地返回不存在的结果。可以尝试让大模型回答"不适用"或"不知道"，但也并非万无一失。

虽然谨慎的提示工程可以在一定程度上起作用，但还应辅之以强大的"护栏"机制，以检测和过滤/重新生成不受欢迎的输出。

例如，OpenAI提供了一个内容过滤API，可识别不安全的响应，如仇恨言论、自残或性内容。同样，还有许多用于检测个人身份信息 (PII) 的软件包。这样做的好处之一是，"护栏"在很大程度上与场景无关，因此可广泛应用于特定语言的所有输出。

此外，通过精确检索，如果没有相关文档，系统也可以确定地回答 "我不知道"。

在实际应用中，最好持续记录输入和输出，以便进行调试和监控。

![](https://image.cubox.pro/cardImg/404v0t9boz2njoe19to9vz2h9xbknwj83o3550gmh5huqoqdoc?imageMogr2/quality/90/ignore-error/1)

**幻觉很难彻底解决**

与安全问题不同，幻觉可能**很难被发现**。

根据作者们从大模型供应商那里了解到的情况，要**将幻觉率降低到2%以下是非常困难的**，即使是在摘要等简单任务中也是如此。

为了解决这个问题，可以将提示工程（生成的上游）和事实不一致护栏（生成的下游）结合起来。

对于提示词工程，思维链等技术可以让大模型在最终返回输出之前解释其推理，从而帮助减少幻觉。然后，可以应用事实不一致护栏来评估摘要的事实性，并过滤或重新生成。

![](https://image.cubox.pro/cardImg/12yj44o0lmtpw26w9se4q10hsyhaenkoh0oh8xt9s3vzhp8oo3?imageMogr2/quality/90/ignore-error/1)

## 技术篇结束，还有运营、战略篇

对于这篇精彩的实战经验分享，沃顿商学院教授Ethan Molick推荐并感慨：
> 这篇文章显示了从传统软件角度来看，使用大模型是多么奇怪，以及人们还有多少东西需要学习。

![](https://image.cubox.pro/cardImg/ck0t4h4ccxus1vutcr4dmpwzcl742v0a7ia1bmqhaexxk6e45?imageMogr2/quality/90/ignore-error/1)

事实上这只是六位作者完整分享的三分之一：战术篇。

第二部分运营篇也刚刚发布，围绕数据、模型、产品、团队发展四个话题展开分享。

![](https://image.cubox.pro/cardImg/3sorhvdfm628be2urymfsig1iqnwrx3jvtkg0c4fzlvpb35b48?imageMogr2/quality/90/ignore-error/1)

接下来还有最后一部分战略篇，也是狠狠期待了。

最后，不妨再来认识一下六位作者。

**Eugene Yan**

![](https://image.cubox.pro/cardImg/gz28adx6lviysz4ykig3pdp983sp5vgp709oaql0q5a1cvgyo?imageMogr2/quality/90/ignore-error/1)

他目前是亚马逊高级应用科学家，负责构建服务全球数百万客户的推荐系统，并应用大语言模型来更好地服务客户。

此前，他曾在Lazada（被阿里巴巴收购）和一家健康科技初创公司领导机器学习团队。他在eugeneyan.com和ApplyingML.com上撰写并发表关于机器学习、推荐系统、大语言模型及工程方面的文章和演讲。

**Bryan Bischof**

![](https://image.cubox.pro/cardImg/2v9d5v2hd1rn1f6i5mlciyn0wp3avk3lkt0gjk3cpm41bhtktc?imageMogr2/quality/90/ignore-error/1)

Bryan Bischof是Hex的AI负责人，领导工程师团队开发了Magic------数据科学和分析助手。

他在数据领域有丰富的工作经验，曾创建了Blue Bottle Coffee、Weights and Biases的数据团队，领导了Stitch Fix的多个项目，还曾与O'Reilly合写了"Building Production Recommendation Systems"一书，并在罗格斯大学教授数据科学和分析课程。他拥有纯数学博士学位。

**Charles Frye**

![](https://image.cubox.pro/cardImg/nkefppqu2a0nrhacurqcri0cc2l1w6qjryt2w8ik013r2f120?imageMogr2/quality/90/ignore-error/1)

Charles Frye在加州伯克利获得了神经网络优化方面的博士学位。

他通过在Weights and Biases、Full Stack Deep Learning和Modal的教育和咨询工作，教授了数千人从线性代数基础到GPU奥秘以及构建可行商业模式的整个AI应用开发过程。

**Hamel Husain**

![](https://image.cubox.pro/cardImg/k7v0gvvtbgpo4dx224384lx6gfa2ehi6sumeyvjqw0va6znrx?imageMogr2/quality/90/ignore-error/1)

Hamel Husain是一位拥有超过25年经验的机器学习工程师。

他曾就职于Airbnb和GitHub等，参与了OpenAI用于代码理解的早期大语言模型研究，还领导许多受欢迎的开源机器学习工具。Hamel目前是一名帮助公司将LLM投入运营加速其AI产品开发的独立顾问。

**Jason Liu**

![](https://image.cubox.pro/cardImg/42cnhwptzpukboqq1eljerp24i50wl2tbdmffyo6g2d3z2ejb2?imageMogr2/quality/90/ignore-error/1)

Jason Liu是一位知名的机器学习顾问，在个性化算法、搜索优化、合成数据生成和MLOps系统方面拥有技术专长。

他曾在Stitchfix创建了一个处理每日3.5亿次请求的推荐框架和可观测性工具，还曾在Meta、纽约大学以及Limitless AI和Trunk Tools等初创公司担任重要角色。

**Shreya Shankar**

![](https://image.cubox.pro/cardImg/3vj58hb7vzg4xlbpeax6cpx9bivjgvk45pyb5sj2m1pykuejn4?imageMogr2/quality/90/ignore-error/1)

Shreya Shankar是加州伯克利计算机科学博士生和机器学习工程师。

她曾是两家初创公司的首席机器学习工程师，从零开始构建AI产品。她的工作重点是通过以人为中心的方法解决生产级机器学习系统中的数据挑战，研究成果发表在VLDB、SIGMOD、CIDR和CSCW等顶级数据管理和人机交互会议上。

另外，作者们还计划举办一场线上直播（北京时间6月21日上午），就大模型产品开发展开更多分享，感兴趣的朋友可以报名了。

![](https://image.cubox.pro/cardImg/4mvimfawvlj2swp1nfcmj3rcfe1qbvmpaazqha09l5t6vdnx62?imageMogr2/quality/90/ignore-error/1)

阅读原文  
https://www.oreilly.com/radar/what-we-learned-from-a-year-of-building-with-llms-part-i/  
https://www.oreilly.com/radar/what-we-learned-from-a-year-of-building-with-llms-part-ii/

线上直播活动：  
https://lu.ma/e8huz3s6

参考链接：  
\[1\]https://news.ycombinator.com/item?id=40508390


--- **完** ---


**量子位年度AI主题策划**正在征集中！

欢迎投稿专题**一千零一个AI应** **用** ，**365行AI落地方案**

或与我们分享你在**寻找的AI产品** ，或发现的**AI新动向**


![](https://image.cubox.pro/cardImg/4yz4kh8xzgzj2l7ui4hxg8wep8p8aqwtmdxkdp25nknhmq9j0?imageMogr2/quality/90/ignore-error/1)

**点这里👇关注我，记得标星哦～**


**一键三连「分享」、「点赞」和「在看」**

**科技前沿进展日日相见 \~**


![](https://image.cubox.pro/cardImg/2149p49yqv93hnyypojpe8et7iveq86vjiu2zittex8zd4ovl9?imageMogr2/quality/90/ignore-error/1)

[Read in Cubox](https://cubox.pro/web/card/7196553461914143318)
