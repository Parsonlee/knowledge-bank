---
id: "7215970289979491622"
cubox_url: https://cubox.pro/web/card/7215970289979491622
url: https://www.ithome.com/0/781/633.htm
tags:
  - LLM/hallucination
---
# OpenAI 翁荔提出大模型「外在幻觉」：万字 blog 详解抵抗办法、产幻原因和检测方式 - IT之家

大模型幻觉还分内在、外在了 ——OpenAI 科学家翁荔最新 Blog，提出 LLM 外在幻觉（extrinsic hallucination）。

[Read in Cubox](https://cubox.pro/web/card/7215970289979491622)  
[Read Original](https://www.ithome.com/0/781/633.htm)  

---

\## Annotations  

> LLM 学习带有新知识的微调示例，要比学习与模型预先存在的知识一致的示例，学得更慢；一旦学习了这些带有新知识的示例，模型产生幻觉的倾向就会增加。  

[Link️](https://cubox.pro/web/annotations/cards/7215970289979491622?highlight=7215970290130488927)  

> 回顾一组提升 LLM 响应真实性的方法，这些方法包括从外部知识库检索、特殊的采样方法、对齐微调。在这里暂不讨论一些通过神经元编辑来减少幻觉的可解释性方法。  

[Link️](https://cubox.pro/web/annotations/cards/7215970289979491622?highlight=7215972833942306978)


---

\## 📖 正文全文

# OpenAI 翁荔提出大模型「外在幻觉」：万字 blog 详解抵抗办法、产幻原因和检测方式

[www.ithome.com](https://www.ithome.com/0/781/633.htm)

大模型幻觉还分内在、外在了 ------OpenAI 科学家翁荔最新 Blog，提出 **LLM 外在** **幻觉**（extrinsic hallucination）。

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fimg.ithome.com%2Fnewsuploadfiles%2F2024%2F7%2Ffbba6a82-526d-4c82-bc52-7ac3e78f49ba.png&valid=false "OpenAI 翁荔提出大模型「外在幻觉」：万字 blog 详解抵抗办法、产幻原因和检测方式")

有别于代指模型生成与现实不符、虚构、不一致或者毫无意义的内容，翁荔将 LLM"幻觉"问题具体化为**模型** **输出内容是虚构的** **，** **并且不基于所提供的上下文或世界知识**。

由此，幻觉有两种类型：

* 上下文内幻觉：模型**输出应该与上下文中的源内容一致**（出现上下文内幻觉时，输出与源内容不一致）。

* 外在幻觉：模型输出应该基于预训练数据集。然而，考虑到预训练数据集的规模，检索并识别每次生成的冲突成本过高。如果将预训练数据集看作是**世界知识** 的象征，那么本质上是试图确保模型输出是事实性的并可以通过外部世界知识进行验证。同样重要的是，**当模型不了解某个事实时，它应该明确表示不知道**。

![](https://image.cubox.pro/cardImg/jppz0v5k3yw5u0c766ru5y568hg1sgv5l50qiwcxuyc0r7rdt.png?imageMogr2/quality/90/ignore-error/1 "OpenAI 翁荔提出大模型「外在幻觉」：万字 blog 详解抵抗办法、产幻原因和检测方式")

之前，翁荔还提出过 Agent 公式：Agent = 大模型 + 记忆 + 主动规划 + 工具使用，被一些网友称为是"看到的有关 Agent 的最好的文章"。

![](https://image.cubox.pro/cardImg/19l4j6j318sxs7fdgoi2awkqclmhaktiqqi3wxng5b3ew6ixgs.png?imageMogr2/quality/90/ignore-error/1 "OpenAI 翁荔提出大模型「外在幻觉」：万字 blog 详解抵抗办法、产幻原因和检测方式")

![](https://image.cubox.pro/cardImg/5eju25klzboybhdbjx0ndum3woxsa9bqpegm8crq49sz6y4a4f.png?imageMogr2/quality/90/ignore-error/1 "OpenAI 翁荔提出大模型「外在幻觉」：万字 blog 详解抵抗办法、产幻原因和检测方式")

而这次关于大模型幻觉的这篇 Blog，同样"重工"，文章超长，足足 24 篇参考文献：

![](https://image.cubox.pro/cardImg/5w3tutmlwgn9dxcnl3e58z2r4li883306jlbigeuclrpql3jkx.webp?imageMogr2/quality/90/format/gif/ignore-error/1 "OpenAI 翁荔提出大模型「外在幻觉」：万字 blog 详解抵抗办法、产幻原因和检测方式")

翁荔重点关注外在幻觉，讨论了三个问题：产生幻觉的原因是什么？幻觉检测，抵抗幻觉的方法。

![](https://image.cubox.pro/cardImg/4bb9jhfttdm8zi3yho6i8r3gz6ykdg2l3ktwck8yrfzusglitn.png?imageMogr2/quality/90/ignore-error/1 "OpenAI 翁荔提出大模型「外在幻觉」：万字 blog 详解抵抗办法、产幻原因和检测方式")

量子位在不改变原意的情况下，对原文进行了编译整理，已获原作者授权翻译转载。

原文在这里：

https://lilianweng.github.io/posts/2024-07-07-hallucination/

\## 产生幻觉的原因是什么？

考虑到一个标准的可部署 LLM 需要经过预训练和微调来进行对齐和改进，所以原因分析从这两个阶段入手。

\#\## 预训练数据问题

预训练数据集旨在代表所有可获得的书面形式的世界知识，因此体量巨大。

从公共互联网爬取数据是最常见的选择，但这就导致可能会出现一些过时、缺失或错误的信息。由于模型可能仅仅通过最大化对数似然来错误地记忆这些信息，所以模型可能会犯错误。

\#\## 微调新知识

通过监督微调（SFT）和人类反馈强化学习（RLHF）来微调预训练 LLM 是提高模型某些能力（例如指令跟踪）的常用技术。微调阶段难免引入新知识。

而微调通常消耗的计算资源较少，**通过小规模的微调模型是否能可靠地学习新知识还有待商榷**。

Gekhman 等人在今年的一项研究中讨论了一个问题：用新知识进行 LLM 微调是否会促使幻觉现象的发生。

他们发现：LLM 学习带有新知识的微调示例，要比学习与模型预先存在的知识一致的示例，学得更慢；一旦学习了这些带有新知识的示例，模型产生幻觉的倾向就会增加。

具体来说，给定一个封闭式问答数据集（即 EntityQuestions）𝐷=(𝑞，𝑎)，将𝑃~Correct~(𝑞，𝑎；𝑀，𝑇) 定义为模型 M 准确生成正确答案的可能性的估计，当使用随机示例和一定的解码温度𝑇来提示时，问题𝑞的正确答案是𝑎。

他们根据𝑃~Correct~(𝑞，𝑎；𝑀，𝑇) 不同条件将示例分为 4 个类别：Known 组（包括三个子组：HighlyKnown、MaybeKnown、WeakKnown）、Unknown 组。

![](https://image.cubox.pro/cardImg/48kh75itzulkrm40cy2u3fwvwtvtdizfh6nm0a4mn2mpyutfbk.png?imageMogr2/quality/90/ignore-error/1 "OpenAI 翁荔提出大模型「外在幻觉」：万字 blog 详解抵抗办法、产幻原因和检测方式")

实验中的一些有趣观察，其中验证集（dev set）的准确率被视为幻觉的象征性指标：

* Unknown 拟合速度明显比 Known 慢得多；

* 当 LLM 拟合了大多数 Known 训练示例，但只拟合了少数 Unknown 示例时，可以获得最佳表现；

* **当大多数 Unknown 示例被学习后，模型开始产生幻觉**。

![](https://image.cubox.pro/cardImg/56fnurllib462ymsla21rxp4ugf7qjeksjxeop57zg8grfwt5v.png?imageMogr2/quality/90/ignore-error/1 "OpenAI 翁荔提出大模型「外在幻觉」：万字 blog 详解抵抗办法、产幻原因和检测方式")

这些来自 Gekhman 等人的研究结果，指出了使用监督微调来更新 LLM 知识的风险。

\## 幻觉检测

\#\## 检索增强评估

为量化模型的幻觉现象，Lee 等人 2022 年引入了一个新的基准数据集 **FactualityPrompt**，该数据集包含了事实性和非事实性的提示，使用维基百科文档或句子作为事实性的基础知识库。

维基百科文档是来自 FEVER 数据集的已知真实信息，而句子则是通过 tf-idf 或基于句子嵌入的相似度选择的。

![](https://image.cubox.pro/cardImg/5jwm8ey1s93819kwr27xr9yi75zh8jf7plunf5ky53wwoimc4g.png?imageMogr2/quality/90/ignore-error/1 "OpenAI 翁荔提出大模型「外在幻觉」：万字 blog 详解抵抗办法、产幻原因和检测方式")

在给定模型续写和配对的维基百科文本的情况下，考虑了两种评估幻觉的指标：**幻觉命名实体** （NE）**错误率** 、**蕴含比率**（Entailment ratios）。

较高的 NE 错误率和较低的蕴含比率表明事实性较高，研究发现这两个指标都与人类注释相关，较大模型在此基准上表现更佳。

此外，Min 等人 2023 提出了 **FActScore**，将长文生成分解成多个原子事实，并根据维基百科等知识库单独验证每个事实。然后可以测量每个模型生成的知识来源支持的句子的比率（精度），FActScore 是一组提示中模型生成的平均精度。

该论文在人物传记生成任务上试验了多种事实性验证方式，发现**使用检索比无上下文 LLM 具有更好的一致** **性**。在检索增强方法中，最佳估计器的选择取决于模型。

* 无上下文 LLM：直接使用"True or False？"提示 LLM，无需附加上下文

* 检索 → LLM：以从知识来源检索的𝑘相关段落作为上下文进行提示

* 非参数概率 (NP)：通过掩码 LM 计算原子事实中标记的平均似然度，并用其进行预测

* 检索 → LLM+NP：两种方法的集成

关于模型幻觉行为的一些有趣的观察：

* 在传记生成任务中，越稀有的实体的错误率越高

* 在生成内容中较晚提及的事实的错误率也较高

* 使用检索来为模型生成提供基础可以显著帮助减少幻觉现象

Wei 等人 2024 年还提出了一种评估 LLM 长篇事实性的方法，名为 **SAFE**（Search-Augmented Factuality Evaluator）。

与 FActScore 相比，主要区别在于 SAFE 使用语言模型作为 Agent，**通过多步骤过程迭代地发出谷歌搜索查询**，并推理搜索结果是支持还是不支持该事实。

在每一步中，Agent 基于待检查的事实以及之前获得的搜索结果生成搜索查询。经过若干步骤后，模型进行推理以确定该事实是否得到搜索结果的支持。

根据实验，**尽管 SAFE 方法的成本比人类注释低 20 倍，但其效果却优于人类注释**：与人类的一致率为 72%，在意见不一致时胜过人类的比率为 76%。

![](https://image.cubox.pro/cardImg/402suhtir3d3m85co36xph5rcx0kumyz3vybewhb71bg0tv7z8.png?imageMogr2/quality/90/ignore-error/1 "OpenAI 翁荔提出大模型「外在幻觉」：万字 blog 详解抵抗办法、产幻原因和检测方式")

SAFE 评估指标是 F1@K。对于长篇事实性的模型响应，理想情况下应同时达到精确度和召回率，因为响应应同时满足：

* **事实性的**：通过精确度衡量，即整个响应中被支持的事实占所有事实的百分比。

* **长篇** **的**：通过召回率衡量，即提供的事实占应出现在响应中的所有相关事实的百分比。因此，要考虑最多支持的事实数量𝐾。

给定模型响应𝑦，指标 F1@K 定义为：

![](https://image.cubox.pro/cardImg/402suhtir3d3m85co36xph5rcx0kumyz3vybewhb71bg0tv7z8.png?imageMogr2/quality/90/ignore-error/1 "OpenAI 翁荔提出大模型「外在幻觉」：万字 blog 详解抵抗办法、产幻原因和检测方式")

![](https://image.cubox.pro/cardImg/402suhtir3d3m85co36xph5rcx0kumyz3vybewhb71bg0tv7z8.png?imageMogr2/quality/90/ignore-error/1 "OpenAI 翁荔提出大模型「外在幻觉」：万字 blog 详解抵抗办法、产幻原因和检测方式")

另外，Chern 等人 2023 年提出了遵循标准的事实核查工作流程 **FacTool**。它旨在检测包括基于知识的问答、代码生成、解决数学问题以及科学文献审查等多种任务中的事实错误。步骤包括：

* 声明提取：通过提示 LLM 提取所有可验证的声明。

* 查询生成：将每个声明转换为适合外部工具的一系列查询，例如搜索引擎查询、单元测试用例、代码片段和论文标题。

* 工具查询与证据收集：查询外部工具，如搜索引擎、代码解释器、谷歌学术，并获取返回结果。

* 一致性验证：根据外部工具提供的证据支持程度，为每个声明分配一个二进制的事实性标签。

![](https://image.cubox.pro/cardImg/402suhtir3d3m85co36xph5rcx0kumyz3vybewhb71bg0tv7z8.png?imageMogr2/quality/90/ignore-error/1 "OpenAI 翁荔提出大模型「外在幻觉」：万字 blog 详解抵抗办法、产幻原因和检测方式")

\#\## 基于采样的检测

Manakul 等人 2023 年提出了依赖于对来自黑盒 LLM 的多个样本进行一致性检查 ------**SelfCheckGPT**，以识别事实性错误。

考虑到灰盒事实核查测量需要访问 LLM 的 token 级别的 logprob，SelfCheckGPT **仅需使用不依赖外部知识库的样本，因此黑盒访问就足够了**，无需外部知识库。

该方法使用不同的指标来衡量模型响应与其它随机模型样本之间的一致性，包括 BERTScore、NLI、提示（询问是 / 否）等。在对 GPT-3 生成的 WikiBio 段落进行实验检测时，使用提示的 SelfCheckGPT 似乎表现最佳。

![](https://image.cubox.pro/cardImg/402suhtir3d3m85co36xph5rcx0kumyz3vybewhb71bg0tv7z8.png?imageMogr2/quality/90/ignore-error/1 "OpenAI 翁荔提出大模型「外在幻觉」：万字 blog 详解抵抗办法、产幻原因和检测方式")

校准未知知识

让模型对无法回答或未知问题生成答案可能会引发幻觉。**TruthfulQA** （Lin 等人，2021 年）和 **SelfAware**（Yin 等人，2023 年）是两个基准测试，用以衡量模型在这类情况下生成真实回应的能力，前者是为了强调人类的错误而对抗性构建的，后者包含了因其性质而无法回答的问题。

面对这些问题时，**模型应该拒绝回答或提供相关信息**。

在 TruthfulQA 中，测试问题是根据人类常见的误解或错误对抗性地设计的。这个基准包含了覆盖健康、法律、金融和政治等 38 个话题的 817 个问题。

在进行测试时，最佳 LLM 的准确率为 58%，而人类可以达到 94%。研究团队发现，**由于常见的误解，较大的模型不太真实** **，但这种趋势并未在其它标准** （非对抗性）**事实基准中显示出来**。

以下是 GPT-3 在 TruthfulQA 上的错误答案示例：

![](https://image.cubox.pro/cardImg/402suhtir3d3m85co36xph5rcx0kumyz3vybewhb71bg0tv7z8.png?imageMogr2/quality/90/ignore-error/1 "OpenAI 翁荔提出大模型「外在幻觉」：万字 blog 详解抵抗办法、产幻原因和检测方式")

Yin 等人 2023 年研究了 **SelfAware** 的概念，指的是语言模型是否知道它们知道什么或不知道什么。

SelfAware 包含了五个类别中的 1032 个无法回答的问题和 2337 个可回答的问题。无法回答的问题来源于在线论坛并附有人类注释，可回答的问题来源于 SQuAD、HotpotQA 和 TriviaQA。

一个问题可能因为各种原因而无法回答，例如没有科学共识、对未来的想象、完全主观、可能产生多种回应的哲学原因等。

研究将区分可回答和不可回答的问题视为二元分类任务，并使用 F1 分数或准确率来评估模型的表现，实验表明更大的模型在这项任务上表现得更好。

![](https://image.cubox.pro/cardImg/402suhtir3d3m85co36xph5rcx0kumyz3vybewhb71bg0tv7z8.png?imageMogr2/quality/90/ignore-error/1 "OpenAI 翁荔提出大模型「外在幻觉」：万字 blog 详解抵抗办法、产幻原因和检测方式")

评估模型对未知知识的认知程度的另一种方式是测量模型输出的不确定性。当一个问题介于已知和未知之间时，模型应表现出正确的置信度。

Kadavath 等人 2022 年的实验表明，在具有可见字母答案选项的多种多**选题**格式（MMLU、TruthfulQA、QuALITY、LogiQA）中，LLM 在估计答案正确性的概率上表现得很好，这意味着预测的概率与该答案为真的频率一致。

RLHF 微调使模型校准效果较差，但较高的采样温度会带来更好的校准结果。

![](https://image.cubox.pro/cardImg/402suhtir3d3m85co36xph5rcx0kumyz3vybewhb71bg0tv7z8.png?imageMogr2/quality/90/ignore-error/1 "OpenAI 翁荔提出大模型「外在幻觉」：万字 blog 详解抵抗办法、产幻原因和检测方式")

Lin 等人 2022 年提出了 **CalibratedMath** 任务套件。CalibrateMath 是一套以编程方式生成的数学问题，具有不同的难度级别，用以测试模型输出概率的校准程度。

对于每个问题，模型必须提供一个数值答案及其对该答案的置信度。考虑了三种类型的概率：

* 用文字表述的数字或词（例如"最低"，"低"，"中等"，"高"，"最高"），如"置信度：60% / 中等"。

* 答案 token 的归一化对数概率。注意，微调实验中没有使用这种参数。

* 在原始答案之后的间接"True / False"标记的 Logprob。实验侧重于校准在任务难度或内容的分布变化下的泛化程度。每个微调数据点是一个问题、模型的答案（可能是错误的）和校准的置信度。在两种情况下，文字表述的概率都能很好地泛化，而所有设置在乘除任务转换上表现良好。在模型预测置信度方面，Few-shot 比微调模型弱。包含更多示例很有帮助，50-shot 几乎与微调版本一样好。

![](https://image.cubox.pro/cardImg/402suhtir3d3m85co36xph5rcx0kumyz3vybewhb71bg0tv7z8.png?imageMogr2/quality/90/ignore-error/1 "OpenAI 翁荔提出大模型「外在幻觉」：万字 blog 详解抵抗办法、产幻原因和检测方式")

\#\## 间接查询

Agrawal 等人 2023 年专门研究了 LLM 生成中出现的幻觉引用案例，包括虚构的书籍、文章和论文标题。他们使用两种基于一致性的方法来检测幻觉，即直接查询与间接查询。这两种方法在 T\>0 时多次运行检查，并验证一致性。

![](https://image.cubox.pro/cardImg/402suhtir3d3m85co36xph5rcx0kumyz3vybewhb71bg0tv7z8.png?imageMogr2/quality/90/ignore-error/1 "OpenAI 翁荔提出大模型「外在幻觉」：万字 blog 详解抵抗办法、产幻原因和检测方式")

直接查询要求模型判断生成的参考资料是否存在，间接查询则要求提供辅助细节，如**参考资料的作者是谁**。

假设是，对于一个幻觉参考资料，多次生成同一作者的一致性要小于直接查询多次回应显示参考资料存在的可能性。

实验表明，**间接查询方法效果更好，更大的模型能力更强，且幻觉现象更少**。

\## 抵抗幻觉的方法

接下来，回顾一组提升 LLM 响应真实性的方法，这些方法包括从外部知识库检索、特殊的采样方法、对齐微调。在这里暂不讨论一些通过神经元编辑来减少幻觉的可解释性方法。

\#\## RAG → 编辑与归因

RAG（检索增强生成）是一种非常常见的提供基础信息的方法，即检索相关文档，然后利用额外的相关文档作为上下文进行生成。

**RARR**（Retrofit Attribution using Research and Revision）是 Gao 等人 2022 年提出的一个框架，通过编辑归因使 LLM 能够追溯地支持对外部证据的归因。

给定一个模型生成的文本𝑥，RARR 分两步处理，输出一个修订后的文本 𝑦和一个归因报告𝐴：

**1、** **研究阶段：查找相关文档作为证据。**

首先使用查询生成模型（通过少样本提示，𝑥→𝑞~1~,...,𝑞~𝑁~ ）构建一组搜索查询 𝑞~1~,...,𝑞~𝑁~来验证每个句子的各个方面。

运行 Google 搜索，每个查询𝐾=5 个结果𝑞~𝑖~。

利用预训练的查询-文档相关性模型来分配相关性分数，并且每个查询𝑞~𝑖~仅保留一个最相关的𝐽=1 文档 𝑒~𝑖1~,...,𝑒~𝑖𝐽~。

**2、修订阶段：编辑输出以纠正不受证据支持的内容，同时尽可能保留原始内容。**初始化修订后的文本𝑦=𝑥。

根据 (𝑞~𝑖~,𝑒~𝑖𝐽~) ，协议模型（通过 few-shot 提示 + CoT，(𝑦，𝑞，𝑒)→ 0,1 ）检查证据𝑒~𝑖~是否与当前修订后的文本不一致。

仅当检测到不一致时，编辑模型（通过少数提示 + CoT，(𝑦，𝑞，𝑒)→ new 𝑦 ）输出新版本的𝑦 ，旨在与证据同时最小限度地改变𝑦 。

最后只有有限数量的𝑀=5 证据进入归因报告𝐴。

![](https://image.cubox.pro/cardImg/402suhtir3d3m85co36xph5rcx0kumyz3vybewhb71bg0tv7z8.png?imageMogr2/quality/90/ignore-error/1 "OpenAI 翁荔提出大模型「外在幻觉」：万字 blog 详解抵抗办法、产幻原因和检测方式")

在评估修订后的文本𝑦时，归因和保留都很重要。

归因使用 AIS（归因于已识别来源）分数来衡量𝑦中有多少可归因于𝐴。可以收集人工注释或使用 NLI 模型来近似自动 AIS 评分。

保留是指𝑦保留𝑥原始文本的程度，以 Previntent×PrevLev 衡量，其中 Previntent 需要人工注释，而 PrevLev 基于字符级 Levenshtein 编辑距离。与两个基线相比，RARR 会带来更好的平衡结果，特别是在保留指标方面。

与使用搜索 + 编辑的 RARR 类似，Mishra 等人 2024 提出的 **FAVA**（Factuality Verification with Augmented Knowledge）也会检索相关文档，然后编辑模型输出以避免幻觉错误。FAVA 模型由一个检索器和一个编辑器组成。

给定提示𝑥和模型输出𝑦，检索最相关的文档：

![](https://image.cubox.pro/cardImg/402suhtir3d3m85co36xph5rcx0kumyz3vybewhb71bg0tv7z8.png?imageMogr2/quality/90/ignore-error/1 "OpenAI 翁荔提出大模型「外在幻觉」：万字 blog 详解抵抗办法、产幻原因和检测方式")

编辑器生成增强输出：

![](https://image.cubox.pro/cardImg/402suhtir3d3m85co36xph5rcx0kumyz3vybewhb71bg0tv7z8.png?imageMogr2/quality/90/ignore-error/1 "OpenAI 翁荔提出大模型「外在幻觉」：万字 blog 详解抵抗办法、产幻原因和检测方式")

RARR 不需要训练，但是 FAVA 中的编辑器模型𝑀~edit~ 需要微调。通过更详细地分类不同类型的幻觉错误，可以为编辑模型生成合成训练数据，方法是在模型生成中插入随机错误。

每个示例都是一个三元组 (𝑐，𝑦，𝑦^∗^) ，其中𝑐是作为黄金上下文的原始维基百科段落，𝑦是带错误的 LM 输出，而𝑦^∗^是带有错误标签和正确编辑的输出。

![](https://image.cubox.pro/cardImg/402suhtir3d3m85co36xph5rcx0kumyz3vybewhb71bg0tv7z8.png?imageMogr2/quality/90/ignore-error/1 "OpenAI 翁荔提出大模型「外在幻觉」：万字 blog 详解抵抗办法、产幻原因和检测方式")

He 等人 2022 年提出的 **RR**（Rethinking with retrieval）方法同样依赖于检索相关的外部知识，但不涉及额外的编辑。

RR 的检索不是利用搜索查询生成模型，而是基于分解的 CoT 提示。

给定输入提示𝑄，RR 使用 CoT 提示在温度 \> 0 时生成多个推理路径𝑅~1~,...,𝑅~𝑁~ ，其中每个𝑅~𝑖~推理路径包含一个解释𝐸~𝑖~（即推理部分），然后是预测𝑃~𝑖~（即实际模型输出）。检索外部知识𝐾~1~,...,𝐾~𝑀~来支持每个解释。然后，根据检索到的知识𝐾~1~,...,𝐾~𝑀~ 的契合程度选择最忠实的答案。

**知识检** **索**：RR 的实验应用稀疏检索 BM25 对维基百科进行搜索，然后通过预训练的 MPNet 模型提供的嵌入余弦相似度进行重新排序。

**忠实度评分**：每个推理路径的忠实度通过蕴含得分、矛盾得分和 MPNet 相似度的组合来估计。蕴含得分和矛盾得分均由预训练的 NLI 模型提供。

![](https://image.cubox.pro/cardImg/402suhtir3d3m85co36xph5rcx0kumyz3vybewhb71bg0tv7z8.png?imageMogr2/quality/90/ignore-error/1 "OpenAI 翁荔提出大模型「外在幻觉」：万字 blog 详解抵抗办法、产幻原因和检测方式")

**S** **elf-RAG**（Asai 等人，2024）通过端到端训练一个语言模型，使其学会通过输出任务结果和间歇性的特殊反思标记来反思自身的生成。

研究团队通过提示 GPT-4 创建了一个用于评判模型和生成模型的监督数据集，然后将其蒸馏到一个内部模型中，以降低推理成本。

![](https://image.cubox.pro/cardImg/402suhtir3d3m85co36xph5rcx0kumyz3vybewhb71bg0tv7z8.png?imageMogr2/quality/90/ignore-error/1 "OpenAI 翁荔提出大模型「外在幻觉」：万字 blog 详解抵抗办法、产幻原因和检测方式")

给定输入提示𝑥，生成的输出𝑦有多个部分（例如，一个段是一个句子）。反思标记总共有四种类型，一种用于检索，三种用于评价：

* Retrieve：决定是否并行运行检索来获取一组文档；输出值：{yes, no, continue}。

* IsRel：判断提示𝑥与检索到的文档𝑑是否相关；输出值：{relevant, irrelevant}。

* IsSup：判断𝑑是否支持输出文本𝑦；输出值：{fully supported, partially supported, no support}。

* IsUse：判断输出文本𝑦是否对𝑥有用；输出值：{5, 4, 3, 2, 1}。

Self-RAG 一次生成一段𝑦~𝑡~。根据给定的𝑥和前面的生成𝑦\<𝑡 ，模型对 Retrieve token 进行解码：

如果 Retrieve==no，直接生成𝑦~𝑡~；

如果 Retrieve==yes，模型并行检索多个段落，并使用 IsRel token 检查检索到的文档是否相关。如果相关，生成𝑦~𝑡~并使用其它评价 token 来评分、排名并选择多个输出中的最佳结果。

\#\## 动作链

在没有外部检索知识的基础上，可以设计一个**利用模型本身进行验证和修订**的过程，以减少幻觉。

Dhuliawala 等人 2023 年提出了一种基于动作链进行规划和执行验证的方法，名为 **Chain-of-Verification**（CoVe）。CoVe 包括四个核心步骤：

* **基线响** **应**：模型生成一个初始响应草稿，称为"baseline"。

* **规划验证**：基于这个原始生成，模型设计非模板化的验证问题进行事实核查；可以通过少量示例提示（回答，验证问题）来实现。

* **执行验证**：模型独立回答这些问题。有几种设置变体：

1）联合：与步骤 2 结合，其中 few-shot 示例结构为（响应，验证问题，验证答案）；缺点是原始响应在上下文中，模型可能会重复类似的幻觉。

2）两步法：将验证规划和执行步骤分开，如不影响原始响应。

3）分解：分别回答每个验证问题。例如，如果长篇基本生成结果产生多个验证问题，将逐一回答每个问题。

4）分解 + 修订：在分解验证执行后添加一个"交叉检查"步骤，根据基线响应和验证问题及答案进行条件限制，检测不一致性。

* **最终输出**：生成最终的、精练的输出。如果发现任何不一致，则在此步骤中将修改输出。

CoVe 之所以这样设计，是因为使用长篇验证链生成可能会导致重复幻觉，因为初始的幻觉响应仍在上下文中，并且在新生成过程中可以被关注，而**单独回答每个验证问题被发现比长篇生成能带来更好的结果**。

![](https://image.cubox.pro/cardImg/402suhtir3d3m85co36xph5rcx0kumyz3vybewhb71bg0tv7z8.png?imageMogr2/quality/90/ignore-error/1 "OpenAI 翁荔提出大模型「外在幻觉」：万字 blog 详解抵抗办法、产幻原因和检测方式")

以下是来自 CoVe 实验的一些有趣观察：

* 指令调整和 CoT 并未减少幻觉。

* 分解和两步法的 CoVe 提高了性能，并且对不一致性检测的进一步明确推理也有所帮助（"分解 + 修订"方法）。

* 简短形式的验证问题比长形式问题，得到的回答更准确。

* 自由格式的 LLM 生成的验证问题比启发式问题（例如，X 是否回答了问题？）更好，需要开放式生成的问题比"是 / 否"问题更好。

此外，Sun 等人 2023 年提出了 **RECITE** 的方法，依赖于复述作为中间步骤，以提高模型生成的事实正确性并减少幻觉。

其动机是将 Transformer 的记忆作为信息检索模型来使用。在 RECITE 的复述与回答方案中，首先要求 LLM 复述相关信息，然后生成输出。

具体来说，可以使用 few-shot 的上下文提示来教导模型进行复述，然后基于复述来生成答案。此外，它还可以与自我一致性的集成方法结合，这种方法使用多个样本，并且可以扩展以支持多跳问答。

![](https://image.cubox.pro/cardImg/402suhtir3d3m85co36xph5rcx0kumyz3vybewhb71bg0tv7z8.png?imageMogr2/quality/90/ignore-error/1 "OpenAI 翁荔提出大模型「外在幻觉」：万字 blog 详解抵抗办法、产幻原因和检测方式")

生成的复述与基于 BM25 的检索模型相当，但两者在使用真实段落时都存在差距。根据研究团队进行的错误分析，大约 7-10% 的问题虽然复述正确，但无法生成正确的答案；大约 12% 的问题复述不正确，但仍然可以正确回答。

\#\## 抽样方法

Lee 等人 2022 年发现，在 FactualityPrompt 基准测试中，核采样（top-𝑝采样）的表现不如贪婪采样，尽管核采样增加了额外的随机性，实现了更好的多样性和较少的重复。

因此，他们提出了基于假设的事实核采样算法，**该假设认为采样的随机性对句子后半部分的事实性的影响大于句子开头** 。事实核采样旨在动态调整每个句子中采样词汇的概率𝑝。对于一个句子中的第𝑡个 token，有𝑝~𝑡~=max(𝜔，𝑝⋅𝜆^𝑡−1^)，其中𝜔用于防止采样回退到损害生成质量和多样性的贪婪采样。

![](https://image.cubox.pro/cardImg/402suhtir3d3m85co36xph5rcx0kumyz3vybewhb71bg0tv7z8.png?imageMogr2/quality/90/ignore-error/1 "OpenAI 翁荔提出大模型「外在幻觉」：万字 blog 详解抵抗办法、产幻原因和检测方式")

Li 等人 2023 年提出 **Inference-Time Intervention**（ITI），通过在每层上对激活进行线性探测，以区分真实与虚假的输出，研究了某些注意力头与事实性是否更相关。

他们发现，对于许多注意力头来说，探测器的表现不比随机选择更好，而有些则表现出很强的性能。在识别出一组在真实性线性探测准确性高的稀疏注意力头后，ITI 在推理时会将 top 𝐾选定的注意力头的激活沿着"真实"方向进行调整。

![](https://image.cubox.pro/cardImg/402suhtir3d3m85co36xph5rcx0kumyz3vybewhb71bg0tv7z8.png?imageMogr2/quality/90/ignore-error/1 "OpenAI 翁荔提出大模型「外在幻觉」：万字 blog 详解抵抗办法、产幻原因和检测方式")

针对事实性的微调

Lee 等人 2022 年提出了两个事实增强训练的想法：

* 引入 TopicPrefix 以更好地了解事实：在该文档的每个句子前添加主题（即维基百科文档标题）。

* 将句子完成损失作为训练目标：更新训练损失以便聚焦于句子的后半部分，假设句子的后半部分包含更多的事实知识。实现非常简单，决定一个枢轴点𝑡，并且第𝑡 token 之前的所有 token 都应用零掩码。在他们的实验中，最佳的枢轴点𝑡被选择为 0.5x 句子长度。

Lin 等人 2024 年提出进行关注事实性的 SFT+RLHF 对齐训练，命名为 **FLAME**。

* SFT 阶段（Factuality-aware SFT）：目标是生成比模型自身生成更具事实性的训练数据（通过 FActScore 衡量）。

* RLHF 阶段（Factuality-aware DPO）：测试了两种方法，方法 1 表现不佳，方法 2 表现还可以，可能是因为方法 1 试图在没有足够训练的情况下将新知识蒸馏到模型中。

前文也有提到过，有一些证据表明，微调新知识可能会导致幻觉，而 RAG 的监督包含了 LLM 未知的信息。

方法 1：使用 RAG 数据样本作为正样本，原始模型生成作为负样本作为 RM 数据。

方法 2：使用 FActScore 作为事实性的奖励信号。

![](https://image.cubox.pro/cardImg/402suhtir3d3m85co36xph5rcx0kumyz3vybewhb71bg0tv7z8.png?imageMogr2/quality/90/ignore-error/1 "OpenAI 翁荔提出大模型「外在幻觉」：万字 blog 详解抵抗办法、产幻原因和检测方式")

为了避免在对齐训练期间意外将未知知识蒸馏到模型中，他们建议使用模型生成的响应来构建 SFT / DPO 数据集。

![](https://image.cubox.pro/cardImg/402suhtir3d3m85co36xph5rcx0kumyz3vybewhb71bg0tv7z8.png?imageMogr2/quality/90/ignore-error/1 "OpenAI 翁荔提出大模型「外在幻觉」：万字 blog 详解抵抗办法、产幻原因和检测方式")

Tian\&Mitchell 等人 2024 年提出的 **Factuality tuning** 同样依赖于微调语言模型以提高事实性。他们试验了不同的方法来估计每个模型样本中原子声明的真实性，然后运行 DPO。

![](https://image.cubox.pro/cardImg/402suhtir3d3m85co36xph5rcx0kumyz3vybewhb71bg0tv7z8.png?imageMogr2/quality/90/ignore-error/1 "OpenAI 翁荔提出大模型「外在幻觉」：万字 blog 详解抵抗办法、产幻原因和检测方式")

事实性调整过程：

1、给定提示集的模型完成示例对（例如"Write a bio of Yo-Yo Ma"）

2、根据两种无需人工干涉的方法对其进行真实性标注：

基于参考：检查外部知识库是否支持模型声明，类似于上述基于检索的幻觉评估部分。(a) 提取一系列原子声明；(b) 查找维基百科参考；(c) 使用一个微调过的小型 NLI 模型来检查参考文本是否支持原子声明。

不基于参考的：使用模型自身的置信度作为其真实性的象征，类似于间接查询方法。(a) 将每个声明转换成相应的问题 / 需要仔细改写以确保问题明确；使用 few-shot 提示；(b) 从模型中多次采样以回答该问题；(c) 计算聚合分数 / 使用字符串匹配或询问 GPT 判断两个答案是否语义等价。

3、通过从模型生成多个样本并根据真实性分数分配偏好，构建一个训练数据集。然后在这个数据集上使用 DPO 对模型进行微调。

![](https://image.cubox.pro/cardImg/402suhtir3d3m85co36xph5rcx0kumyz3vybewhb71bg0tv7z8.png?imageMogr2/quality/90/ignore-error/1 "OpenAI 翁荔提出大模型「外在幻觉」：万字 blog 详解抵抗办法、产幻原因和检测方式")

\#\## 针对归因的微调

在生成依赖于搜索结果的模型输出时，赋予归因是减少幻觉的一个好方法。有一系列工作旨在训练 LLM 更好地利用检索到的内容并分配高质量的归因。

Nakano 等人 2022 年提出 **WebGPT**，将用于文档检索的 Web 搜索与微调的 GPT 模型相结合，旨在回答长篇问题以减少幻觉并提高事实精度。

该模型与基于文本的 Web 浏览器中的互联网搜索进行交互，并学会引用网页来回答问题。当模型正在浏览时，它可以采取的一种行动是引用当前页面的摘录。执行此操作时，会记录页面标题、域名和摘录，以便稍后作为参考使用。**WebGPT 的核心是使用参考资料帮助人们判断事实正确性**。

该模型首先在人类使用 Web 浏览环境回答问题的演示上进行监督微调，以进行行为克隆。

收集同一问题的两个模型生成的答案（每个答案都有自己的参考集）之间的比较数据，其中答案会根据其事实精度、连贯性和整体有用性进行评判。奖励模型用于 RL 训练和 best-of-n 拒绝采样。相比之下，RL 效果有限，并且当使用拒绝抽样时，效果更有限。

![](https://image.cubox.pro/cardImg/402suhtir3d3m85co36xph5rcx0kumyz3vybewhb71bg0tv7z8.png?imageMogr2/quality/90/ignore-error/1 "OpenAI 翁荔提出大模型「外在幻觉」：万字 blog 详解抵抗办法、产幻原因和检测方式")

Menick 等人 2022 年提出 **GopherCite**，在使用搜索引擎创建支持材料和教模型提供参考资料方面与 WebGPT 非常相似。两者都对引导进行监督微调，并且都应用 RLHF 训练。

与依赖人类演示进行行为克隆的 WebGPT 不同的是，GopherCite **通过 few-shot 提示生成演示**，并且每次生成都使用相关文档的上下文填充，然后使用奖励模型来评分哪些是最好的。

![](https://image.cubox.pro/cardImg/402suhtir3d3m85co36xph5rcx0kumyz3vybewhb71bg0tv7z8.png?imageMogr2/quality/90/ignore-error/1 "OpenAI 翁荔提出大模型「外在幻觉」：万字 blog 详解抵抗办法、产幻原因和检测方式")

为避免低质量响应的另一个技巧将模型配置为拒绝使用预设答案"I don't know"进行回答，该答案由全局 RM 阈值决定，称为选择性预测（selective prediction）。

RL 实证结果与 WebGPT 类似，即 RL 只带来有限的改进，或者当与拒绝抽样结合使用时不带来改进。

![](https://image.cubox.pro/cardImg/402suhtir3d3m85co36xph5rcx0kumyz3vybewhb71bg0tv7z8.png?imageMogr2/quality/90/ignore-error/1 "OpenAI 翁荔提出大模型「外在幻觉」：万字 blog 详解抵抗办法、产幻原因和检测方式")

\## 翁荔是谁？

翁荔是 OpenAI 华人科学家、ChatGPT 的贡献者之一，北大毕业。

![](https://image.cubox.pro/cardImg/402suhtir3d3m85co36xph5rcx0kumyz3vybewhb71bg0tv7z8.png?imageMogr2/quality/90/ignore-error/1 "OpenAI 翁荔提出大模型「外在幻觉」：万字 blog 详解抵抗办法、产幻原因和检测方式")

她是 OpenAI 人工智能应用研究的负责人，2018 年加入 OpenAI，在 GPT-4 项目中主要参与预训练、强化学习 \& 对齐、模型安全等方面的工作。

在 OpenAI 去年底成立的安全顾问团队中，她领导安全系统团队（Safety Systems），解决减少现有模型如 ChatGPT 滥用等问题。

本文来自微信公众号：[量子位（ID：QbitAI）](https://mp.weixin.qq.com/s/1RF_TEDHg1HoIr00ubreeA)，作者：西风

广告声明：文内含有的对外跳转链接（包括不限于超链接、二维码、口令等形式），用于传递更多信息，节省甄选时间，结果仅供参考，IT之家所有文章均包含本声明。

[Read in Cubox](https://cubox.pro/web/card/7215970289979491622)
