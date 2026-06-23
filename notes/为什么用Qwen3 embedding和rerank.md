# 为什么用Qwen3 embedding和rerank

[mp.weixin.qq.com](https://mp.weixin.qq.com/s/hmJ1H9gTBmHV_dOGM7UeWg)周博洋 熵减AI


![](https://image.cubox.pro/cardImg/4yzoy4h64vg8ywi4qmhlh9swdut2hc3enalgwpxexh3eh0n599?imageMogr2/quality/90/ignore-error/1)

排名是真的挺好，开源闭源现在都是第一了，这个事embeddiing的，rerank应该也是第一，甚至4B的基本也除了8B以外就是它第一。

它和普通的比如原来的我们常用的BGE之类的有啥区别？

传统的embedding都是基于bert来弄模型，一般也就encoder only，bert原来也就是干分类器的，给一句话到它，它给你进行embedding了，这里考虑到有些同学可以不理解整套流程，我就稍微说细点一般来讲用3层法就很好理解：

**第一层：词元嵌入（Token Embedding）------"查字典"阶段**

"一个token一个token地进行embedding"，这是最基础的，也是第一步。

1. 分词（Tokenization）：模型拿到一句话，例如 "The cat sat on the mat"，会先把它切分为一个个"词元"（Token）：\["the", "cat", "sat", "on", "the", "mat"\]

2. 查字典（Token Embedding）：模型内部有一个庞大的"字典"（Embedding Layer），存着每个词元对应的初始向量。模型会根据分词的结果，依次查出每个token的初始向量。举例："the" -\> \[0.1, 0.5, 0.2, ...\]"cat" -\> \[0.8, 0.1, 0.9, ...\]......这一层得到的向量**是上下文无关的** 。举个经典例子，无论"bank"出现在"river bank"（河岸）还是"investment bank"（投资银行）里，在这一层查出的向量都是一样的。两个bank在这个向量化的时候没啥区别，但是我们知道语义完全是两个东西

**第二层：上下文感知（Contextualization）------Transformer就上了**

传统模型（比如Word2Vec）和现代的Transformer模型（比如BERT、Qwen）就在这里拉开了差距。

在拿到第一步得到的所有初始向量后，模型不会直接用它们，而是把这一串向量送入Transformer核心结构（多层自注意力机制，搞一遍QKV），进行"深加工"。

你可以把它想象成：这些独立的单词向量都进入了一个"会议室"。在这里，"cat"这个向量会和"sat""mat"等其他向量充分"沟通和讨论"（自注意力机制）。经过多轮（多层）讨论，每个单词向量都吸收了整句话的上下文信息，最终全部更新（这块看不懂可以看我以前的transformer算法文章）。

在这一步之后，比如"bank"在"river bank"和在"investment bank"中的最终向量就不再相同，而是根据上下文有了不同的含义。但要注意：此时我们依然得到了一个**词元序列对应一个向量** ，即一句话还是对应一串向量，每个词元一个。

**第三层：句子嵌入（Sentence Embedding）------从"一串"到"一个"**

接下来，有些任务（比如语义搜索、相似度比对等）需要用一个向量来代表整个句子，而不是一串向量。这时就需要一个**聚合或池化（Pooling）** 的策略，把第二层产出的那一串上下文感知向量，浓缩成一个能够代表整句话的整体向量。

这块BGE代表的bert派和qwen3代表的LLM派就有区别了

这正是 \[CLS\] 和 \[EOS\] 发挥作用的地方！

**传统BERT模型（\[CLS\]策略）**

BERT会在输入的最前面加一个特殊的 \[CLS\]（Classification）标记。在经过Transformer的"深加工"后，BERT会特别训练模型，使得这一最终的 \[CLS\] 标记向量能够代表整句话的含义。

因此，我们只需要从最后一层输出中，把 \[CLS\] 对应的向量单独拿出来，就可以用作整句话的句子嵌入。其他词元的向量在这个任务中可以忽略。这个CLS可以挂在整个句子的最前面

\[CLS\] 句子A \[SEP\] 句子B \[SEP\]

bert pooling完了的结果是由这个CLS位为代表，最终的句子（任意长的chunk）得到的一个定长的向量，也就是**[CLS]标记最终的隐藏状态向量** 。这个**定长的向量** 就是该文本块的嵌入表示，也正是我们存入向量库用于后续检索的那个向量。

**Qwen3模型（\[EOS\]策略）**

Qwen3的原理与BERT类似，不过由于其结构是单向的，因为LLM是casul LLM，它看不到你前面的东西啊，所以它选择在输入序列的末尾加一个 \[EOS\]（End of Sequence）标记。

也就这么点区别，因为看不见前面，所以选择最后整个语义被压缩到最后一个speical token，这里用的是EOS，然后最后这个EOS token所代表的hidden state 等驾于CLS

当然同样，Qwen3也会特别训练模型，确保 \[EOS\] 标记的最终向量能够代表整句话的含义。

因此，我们只需取 \[EOS\] 的那个向量，就得到了所需的句子嵌入。

看起来似乎没那么特别大的差别吗？那它为什么效果能好出来10几个百分点呢？

1- 模型够大，只要你把BGE做的dimension变大，它其实也能变好的，因为维度大了，隐空间可表示的表征自然就丰富，难训，但是训好了，泛化性和能力都要更好

2- 基础模型太强，Qwen3的语音本身的理解那不是bert能比的了的（在我看这才是核心），早它之前其实也有那拿mistral来训类似的套路的，效果也不错，可是mistral和qwen系列还是没法比的

3- 训练方法

前两个阶段都是对比学习，3阶段加一个slerp

1）合成数剧上用qwen32来刷的，刷了很多，有逻辑的数据，那以前BGE上的只能上社区搜，这块差了不少，无论质量还是数量。他们总共创造了约**1.5亿** 对用于弱监督训练的文本对，有人说LLM的语义能力应该可以啊，嗨搞什么弱监督pretrain啊，这不是你的最终任务是这种成对的吗，所以拿这个刷一刷，原始pretrain数据集里对这种的任务没有特定的针对datasets，相当于补充一下

2）多样性，研发人员在生成数据时，精确地定义和控制各种维度，例如**任务类型、语言、文本长度和难度** 等。论文的附录中详细介绍了一个精巧的两阶段生成流程，在生成检索数据时，会先为文档配置一个"角色（Character）"，然后从这个角色的视角出发生成查询，极大地提升了数据的多样性和真实感。

3） 合成加人工在FT，这阶段还有包含约700万对人工标注数据和1200万对高质量合成数据来刷FT

4- Slerp这个基本不太会有人特别用，但是论文说用Slerp来融合多个step的checkpoint面对不同的下游任务效果都很好，我觉得看看就可以了，这个不用太当真。

刚才说它底子好，数据又多是主要原因，其实还有一个原因也很重要，但是估计大多数人不一定用，比如我粘这张图的MTEB的bench leadboard就没考虑进来，全是zero shot的，也就是我们普通玩的双塔

问题--\> embedding 得向量和 docuemnt embedding得向量一比，哪几个topk更好，就选出他们index对英的chunk

这是普通玩法，当然qwen3这个普通玩法我们看着在天梯上就很能打

可是它其实是有新玩法的，就是instruct

它示例代码是这样的：

    from sentence_transformers import SentenceTransformer
    # Load the modelmodel = SentenceTransformer("Qwen/Qwen3-Embedding-0.6B")queries = [    "What is the capital of China?",    "Explain gravity",]documents = [    "The capital of China is Beijing.",    "Gravity is a force that attracts two bodies towards each other...",]# Encode the queries and documents. Note that queries benefit from using a promptquery_embeddings = model.encode(queries, prompt_name="query")document_embeddings = model.encode(documents)


先看一个用sentence-transformer引导的简单的案例，就是比2个query和2个document的距离么

这个看着特别容易，但是其实有点玄机，玄机在这

query_embeddings = model.encode(queries, prompt_name="query")

正常我们认为encode一个问题的时候就是把query给encode了，对吧，但是它这个多来一个尾巴，就是这个 prompt_name="query"

这个是什么呢？

这个就是instruct，玩LLM的对这个就没什么可陌生的了，最早的chatGPT就有3个输入对吧

system的

instruct的

user的

system的对应全局role的或者什么其他的设定，instruct对应本次的，user就是正常说话的，只不过现在被改的基本也就偶尔用用system，instruct基本消失于江湖了，全是user的

但是qwen3把这个捡了起来。

它是做什么的呢？

首先如果默认写了prompt_name='query'如上一段代码，那么背后的意义就是相当于开个默认的instruct='Given a web search query, retrieve relevant passages that answer the query'

而每次跟着用户的问题一起进入双塔中的问题塔进行encoder的除了用户的问题，还有这个instruct，相当于给你的查询加了控制

有人说看这个instruct也没什么意义啊，基本不都是为了query吗？那系统本身带的默认的却是就是给retrive用的

可是还很多场景，你可以给它改了，比如我举几个能想到又好理解的例子：

例子一：FAQ知识库中的"相似问题"匹配

场景：

假设你有一个包含1000个标准问答对（FAQ）的知识库。用户提出了一个口语化的问题，你不希望直接从那些冗长的答案中查找，而是希望先找到与用户问题最相似的"标准问题"，再把相应的标准答案返回给用户。

挑战：

这里的关键任务不再是"问题→答案"的检索，而是"问题→问题"的相似度匹配。

自定义指令：

Instruct: For the given user question, find the most similar question from the FAQ list.

中文示例："为以下用户问题，在FAQ列表中匹配最相似的标准问法。"

这个指令告诉模型，无需关注答案内容，而是聚焦于两个问题在语义上的等价性。相比通用的retrieve指令，这样更精准，能有效避免用户问题因为某个关键词（如"价格"）而误匹配到不相关的答案。

例子二："相关推荐"或"发现更多"功能

场景：

用户正在阅读一篇新闻报道或浏览一个商品详情页，你希望在页面下方为其推荐"相似文章"或"相似商品"。

挑战：

"相似"有多种维度：是主题相似？风格或调性相似？还是同样提到了某个人物或产品？

自定义指令与示例

主题推荐：

Instruct: Find other articles with a similar topic.

中文示例："寻找主题相似的其他文章。"

风格推荐：

Instruct: Find other documents written in a similar narrative style.

中文示例："寻找写作风格相似的其他文档。"

意义：

你可以用同一套文档向量，通过在查询时动态传入不同指令，为用户提供多维度的推荐。比如让用户自己选择"更关心主题"还是"喜欢这个作者的风格"，实现更个性化的推荐功能。

例子三：代码库中的功能性搜索（论文提到的强项）

场景：

开发者希望在代码库中寻找能够"异步写入文件"的函数。

挑战：

代码搜索和自然语言搜索不同。直搜"异步写入文件"未必有效，因为不同开发者可能用不同的变量名或注释。

自定义指令：

Instruct: Find code snippets that perform a similar function.

中文示例："寻找能够实现相似功能的代码片段。"

这个指令能引导模型超越表面词汇差异，理解代码的实际逻辑和功能。这也是Qwen3 Embedding在代码检索表现突出的原因之一。开发者还可以更具体地定制指令，比如："Find usage examples for the 'torch.nn.Module' class"。

例子四：细粒度的评论分析

场景：

身为产品经理，你希望从大量用户评论中，找到所有提到"电池续航差"的负面评价。

挑战：

直接搜"电池"会返回所有正负评论，普通语义搜索也难区分评论的情感倾向。

自定义指令：

Instruct: From the product reviews, retrieve passages that express a negative sentiment about battery life.

中文示例："从产品评论中，检索关于'电池续航'的负面评价段落。"

这不就少挨几句骂么。。。

综上，这个我认为是有用，但是现有大部分rag系统本身不支持这个（我自己玩的BY_RAG也为了这个能力再改），所以还是有一定工作量和产品设计怎么能根据具体的任务来灵活的设置instruct，新玩法出来了，但是老工具还是需要改进来fit它的能力。

最后花少许时间讲讲qwen-rerank

它这个也和传统的rerank不一样，传统的单塔rerank一般是最后一层liner输出个logit，但是它是用system prompt来让rerank模型生成yes\|no，然后输出yes的概率得分，（score = P("yes") / (P("yes") + P("no"))包括为了兼容这块你最好还要做padding的左移，总之现有的代码你想用，是要进行变更的

除了对rerank分数的判定不一样，传统rerank是使用简单的[CLS]Query[SEP]Document拼接方式，然后进里面去查相关性，它不是，它的套路是template

Qwen3 Reranker 的设计采用了结构化、类似对话的上下文输入方式，最大程度发挥了大语言模型的理解和推理能力。

根据论文，输入格式遵循类聊天模板，主要包含以下几个部分：

第1部分

1. **系统指令（System Prompt）**   
   首先，系统级指令为模型设定角色和任务规则。这个指令会告诉模型："根据提供的查询和指令来判断文档是否满足要求"，并明确规定"答案只能是'yes'或'no'"。这样，排序任务就被直接转化为一个二元分类问题。

2. **用户信息（User Block）**   
   在 user 块中，结构化地提供三项核心信息：

   * <Instruct>
     : 用户自定义、用于指导模型排序的具体指令
   * <Query>
     : 用户原始查询
   * <Document>
     : 待判断相关性的候选文档
3. **助手提示（Assistant Prompt）**   
   最后，输入以一个 assistant 提示结尾，让模型去"思考"并生成最终的判断。

看起来这样

    <|im_start|>systemJudge whether the Document meets the requirements based on the Query and theInstruct provided. Note that the answer can only be "yes" or "no".<|im_end|><|im_start|>user<Instruct>: {用户自定义的指令}<Query>: {用户的查询}<Document>: {候选文档}<|im_end|><|im_start|>assistant


第2部分：进入Qwen3模型（"判官"审阅案卷）

这个精心构建、结构化好的"案卷"文本会被完整送入Qwen3基础模型。

Qwen3本身就是一个强大的大语言模型（虽然小，但是应付embedding够用），拥有0.6B、4B、8B等多种规模，具备强大的文本理解能力、长上下文处理（32K序列长度）、以及出色的指令跟随能力。

与传统模型类似，Qwen3会对指令、查询和文档中的所有词元进行深度、端到端的自注意力计算，实现信息的充分交互。

第3部分：输出判决（计算"yes"的概率）

Qwen3 Reranker在输出机制上和传统模型有着显著区别。它不依赖额外的分类头输出抽象分数，而是直接通过预测答案"yes"或"no"的概率，作为相关性判断的依据。

具体做法是：模型的主要任务是预测 assistant 后最可能出现的词元，即"yes"或"no"，并计算它们各自的概率。最终的相关性分数通过如下公式归一化得到：

score = P("yes") / (P("yes") + P("no"))

该分数的取值范围在0到1之间，直观代表了文档与查询在当前指令下的相关程度。分数越高，说明"yes"的置信度越高，即文档越符合用户需求。

**Qwen3 Reranker通过将排序任务"LLM化"**或** "对话化"，充分释放了其强大基础模型的潜力，使其不再是一个简单的打分工具，而是一个能够理解复杂指令、进行深度推理的智能"判官"，这就是完全两个故事了，所以性能和纯rank打分器也不一样**

**训练就不说了，没啥特殊的，刷数据**

我自己的RAG肯定是率先都支持了，现在在做和DR集成，做好了，就开源，做不好我也不着急发![](https://image.cubox.pro/cardImg/4p7x51ppstos8s5608p89kzoin361bvcgb2qq7x3ojyofqjwl7.png?imageMogr2/quality/90/ignore-error/1)

![](https://image.cubox.pro/cardImg/4qima9zuzr0392xw5mlycpsw2fosllyplwijj28kqixjieevl5?imageMogr2/quality/90/ignore-error/1)

![](https://image.cubox.pro/cardImg/2htst3l6e6ontpppaszjwnhyan3hms43e9resnhu26kvmgmvri?imageMogr2/quality/90/ignore-error/1)

[Read in Cubox](https://cubox.pro/web/card/7337179436820728245)
