# LLM学习笔记：最好的学习方法是带着问题去寻找答案

[mp.weixin.qq.com](https://mp.weixin.qq.com/s?__biz=MjM5ODYwMjI2MA==&mid=2649793418&idx=1&sn=42bdb5161cea0cb2df6fb40872ec295e&subscene=0)腾讯程序员 腾讯技术工程


![](https://image.cubox.pro/cardImg/4l1pmr142p23gusjdlsdq6do8kcw8yjysd4cfz4imzvhwzw3yo?imageMogr2/quality/90/ignore-error/1)

作者：huaxing
> 知其然，然后知其所以然。本文主要是对学习赛博活佛Andrej Karpathy 7个小时教学视频的总结和拓展阅读笔记，推荐去看原视频，很精彩，链接在文末。从最常用的聊天应用过程分析开始，引入对话过程原理浅析，再到LLM训练过程；再结合当前主流的应用形式，在得知最新用法的同时，加深对LLM的理解；再谈谈AI的最新重大进展MCP；以及作为JAVAer，在Java领域有哪些前沿能力去整合LLM。

最后再罗列一下再公司内部一些AI平台、工具。最好的学习方法是带着问题去寻找答案，以费曼学习法为标准，产出可教学的资料。本文是个人所学梳理和所想记录，作为AI的小白，个人知识有限，难免有所错误、疏漏，请及时纠偏、不吝赐教，感谢。
1 大模型聊天过程分析

我打开AI聊天窗口[https://chat.deepseek.com](https://chat.deepseek.com/)，发送我的Query：
![](https://image.cubox.pro/cardImg/1lc0rvb8t4fqyhw6kqjbf535teb7kaje8c4rjllmk3fx8utsw6?imageMogr2/quality/90/format/gif/ignore-error/1)

#### 1.1 流程浅析

当我们开始一个LLM聊天对话，输入问题时，实际上大模型托管服务有内置的上下文信息，在我们输入信息，按下发送按钮时，大模型收到的是内置上下文 + 系统服务Prompt + 用户输入信息。
![](https://image.cubox.pro/cardImg/2dgggrr5gymif61jiiu7af0kezfc7486g5c42dt15fey9vxi2b?imageMogr2/quality/90/format/gif/ignore-error/1)

大模型经过神经网络的概率统计（权重拟合)得到下一个要说的词，通过流式响应逐个词丢回会话窗口，用户就能看到大模型"正在打字"和我们聊天。"打字"的速度就是大模型响应的速度，通常看描述LLM性能的一个指标N token/s。
![](https://image.cubox.pro/cardImg/3286gnge4lgurys9kbhtx97i0q7uedhi9dpnt5iyebkn0c5qf?imageMogr2/quality/90/format/gif/ignore-error/1)

#### 1.2 原理浅析

![](https://image.cubox.pro/cardImg/51p23101x6gqf79okd434zhycuwxw3smlcs80ozfncuunulshc?imageMogr2/quality/90/format/gif/ignore-error/1)

本质就是从输入的 tokens 推测下一个 token 的出现概率，将可能性较高的作为输出token，再将得到的token添加到输入中，直到满足结束条件（上下文长度限制、结束符以较高概率出现、用户定义的停止条件、概率阈值与采样策略、模型架构的隐式结束符）。所以LLM本质上是一个具有统计概率的知识记忆模糊的知识回顾系统，也可简称概率性复读机。那么这个回顾系统是怎么实现的呢，"zip文件"怎么得来的？构建一个现代的LLM三个步骤：\*\*预训练、后训练（SFT）和强化学习（RL\\RLHF)\*\*。

#### 1.3 预训练

在预训练过程中，需要有原始数据和验证数据，所以通常可以将数据集分为两份，例如90%用于训练，10%用于验证（具体比例可能因任务调整）。

##### 1.3.1 数据集

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2Fj3gficicyOvattV3Cy7muORnkSUx9P3EBPwSbv6JMOBOwKibNicWiay3Ouye4nqCDeibc2CHeys8mnQuJc45h85OSiaRg%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26tp%3Dwebp%26wxfrom%3D5%26wx_lazy%3D1&valid=false)

图片来源[huggingface.co/space...](https://huggingface.co/spaces/HuggingFaceFW/blogpost-fineweb-v1)

数据集生成流程：

1.
   列举主流网站的URL

2.
   有害网站URL过滤，垃圾站点、成人内容等

3.
   从URL网站响应的富文本提取文字内容

4.
   文本语言过滤，如仅针保留英文或者中文内容，在huggingface上数据集语言分布前5如下图：
   ![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2Fj3gficicyOvattV3Cy7muORnkSUx9P3EBPujwSDWKuzxawia7cQg9b8Z0dkvZyU2GVUtxc06NwKyHIpAutrSFNICA%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26tp%3Dwebp%26wxfrom%3D5%26wx_lazy%3D1&valid=false)
5.
   Gopher 过滤，去除无意义、低信息量或有害内容（如垃圾文本、暴力、偏见等）

6.
   MinHash 去重，用于快速检测并移除数据集中的重复或近似重复的文本片段（如文档、段落或句子）。其核心目的是减少数据冗余，避免模型因重复数据过拟合或偏向高频内容，同时节省计算资源。

7.
   C4 过滤，C4（Colossal Clean Crawled Corpus） 数据集进行清洗和筛选的步骤，旨在从原始网页文本中提取高质量、多样化的语料，同时去除噪声、重复和低效内容。

8.
   Custom Filters（自定义过滤器）目标是针对通用过滤方法（如MinHash去重、C4/Gopher过滤）无法覆盖的领域特殊性问题，进行更精细化的数据质量控制。

9.
   PII Removal（个人身份信息移除） 是指从原始数据中识别并删除或匿名化 个人身份信息（Personally Identifiable Information, PII） 的关键步骤，旨在保护用户隐私、遵守数据保护法规（如GDPR、CCPA），并降低模型泄露敏感信息的风险。

预训练数据集示例：
![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2Fj3gficicyOvattV3Cy7muORnkSUx9P3EBPEnRgkfNZcKwKpsyF08O4JWICosMflHOXOYRPgZRQmJp9yATPo1ZDCQ%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26tp%3Dwebp%26wxfrom%3D5%26wx_lazy%3D1&valid=false)

##### 1.3.2 Tokenization

[tiktokenizer.vercel....](https://tiktokenizer.vercel.app/) 上可以看到模型token可能是不一样的，这里举例OpenAI的对话示例:
![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2Fj3gficicyOvattV3Cy7muORnkSUx9P3EBPUjbibyx7tBCe8aAUh5C2aUJWI3kibwQuxdib9cIgthWSH4Ber5cyiazlibg%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26tp%3Dwebp%26wxfrom%3D5%26wx_lazy%3D1&valid=false)

可以看到OpenAI对数据结构化了，定义了对话角色，增加了\<\|im_start\|\>、\<\|im_sep\|\>、\<\|im_end\|\>这样的标识符用于分割对话，这些标识符都对饮一个token，"You are a helpful assistant"的tokens序列是"3575, 553, 261, 10297, 29186"。

Tokenization（分词/令牌化）是将输入文本拆分为模型可处理的离散单元（Token）的过程，即将文本数据表示为token的一维序列。它是自然语言处理（NLP）中的关键步骤，直接影响模型对文本的理解能力和效率。

数据集的原始文本数据量非常大，如著名的FineWeb数据集就有15万亿个token，总共44TB大小，需要高效拆分文本窗口，在能表达混合多种语言、复杂字符表达等情况，但不丢失语义。分词实际上就是一层映射包装，过粗、过细的分词都不利于训练和模型性能表现，分词过细（如字符级、字节级别、比特级别）导致长序列，计算开销大，分词过粗（如单词级）则词汇表爆炸，内存占用高。

采用BPE（Byte-Pair Encoding，如GPT）、WordPiece（如BERT）或SentencePiece，将文本转化为子词（subword）单元。BPE算法（Byte-Pair Encoding）：平衡词汇表大小与序列长度。

原始文本：
![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2Fj3gficicyOvattV3Cy7muORnkSUx9P3EBPn1a7oXdRV95AMwIibeUZL93WYhzhSqf51FSN3mpudu3TnZJibU5K5Dtw%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26tp%3Dwebp%26wxfrom%3D5%26wx_lazy%3D1&valid=false)

原始字节
![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2Fj3gficicyOvattV3Cy7muORnkSUx9P3EBPDBayvKjNZt3gVhTNfAiaGSziav0mZa0Vq4KgHZJtoAHNdQx7goe7oX5Q%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26tp%3Dwebp%26wxfrom%3D5%26wx_lazy%3D1&valid=false)

tokenization：
![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2Fj3gficicyOvattV3Cy7muORnkSUx9P3EBPtticeVnOcr5TkZpy9u2wUCvFGia9wGQt47BVbEtPDD30cYqyB16ynpXQ%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26tp%3Dwebp%26wxfrom%3D5%26wx_lazy%3D1&valid=false)

对话过程中输入的token越多，越分散注意力，降低模型准确性和性能，节约成本。不丢失信息的情况，越短越好，性能成本都会提升。所以，聊不同的主题应该单独开会话窗口。

##### 1.3.3 词汇表

在tokenization过程中，我们发现，在44TB的文本内容里，很多词一起出现的概率较高，如图中49305后面出现17，那么就可以将49305与17合并成4930517，作为一个新的token，重复如此。最后，再将所有词汇压缩到最小映射表，重新编号token，这样就得到了一份可以还原44TB内容的词汇表。如GPT-4词汇表是100277个。主流大语言模型的词汇表大小如下（按数值从小到大排序）：

1.
   **原版LLaMA** 词汇表大小为 **32,000** （32K），但中文token较少（仅几百个）。
2.
   **中文LLaMA/Alpaca** 通过合并中文tokenizer后，词汇表扩展至 **49,953** （约50K）。
3.
   **优化后的实验模型**
   *
     部分研究将词汇表从32K扩展至 **43,000** （43K），显著提升下游任务性能。
   *
     理论预测的Llama2-70B最优词表大小为 **216,000** （216K），但尚未实际部署。
4.
   **多语言模型（如XLM-R、Bloom）** 词汇表普遍较大，约 **250,000** （250K）。

##### 1.3.4 数据分片

将大规模训练数据集划分为多个逻辑或物理片段（Shard）的技术，目的是实现高效的数据并行处理和分布式训练。

数据分片的核心作用：

1.
   **解决内存与存储限制** ：单个节点无法加载全部数据，分片后每个节点仅处理部分数据。
2.
   **并行加速训练** ：不同分片由不同计算设备并行处理（如GPU），缩短训练时间。
3.
   **容错性** ：单个分片损坏或失败时，只需重新处理该分片，而非整个数据集。

我们知道数据集是一张表，所以数据分片的方式方法和传统结构化数据分片类似，但这里要结合训练过程的实际情况做调整，数据分片常见方法：

1.
   静态分片，预先规划好分片，每个GPU固定处理指定分片，优点实现简单，缺点是实际训练过程中可能导致GPU负载不平衡，因为数据集中的每一行长度是不同的，所以会导致数据倾斜。
2.
   动态分片，训练过程中动态分配数据（如通过中央调度器或分布式文件系统），优点：自动平衡负载，适应数据异构性。缺点：实现复杂，需额外协调开销（如Apache Spark或Ray框架）。
3.
   分片与数据管道的结合，流水线加载：当一个GPU处理当前分片时，异步预加载下一个分片（隐藏I/O延迟）；格式优化：分片常存储为高效二进制格式（如TFRecord、HDF5），加速读取。

##### 1.3.5 模型架构选择

当前主流LLM通常是采用Transformer结构，包含自主力(Self-Attention)和多头注意力(Multi-Head Attention)的注意力层、前馈神经网络(FFN)，注意力层+FFN等模块组成一层，需要确定模型的层数和参数量。

**主流架构** ：Transformer（基于自注意力机制），常见变体：

*
  **Decoder-only** （GPT系列）：适合生成任务，单向注意力掩码。
*
  **Encoder-decoder** （T5、BART）：适合翻译等序列到序列任务。

**规模参数** ：

*
  层数（L）：12-100+（如GPT-3 davinci版本包含96层）
*
  隐藏层维度（d_model）：768-12,288
*
  注意力头数（h）：12-128

**Transformer结构** ：

*
  **自注意力机制** ：计算输入序列中每个位置的关联权重（如多头注意力）。
*
  **前馈网络（FFN）** ：每个注意力层后接非线性变换。
*
  **层数与参数量** ：例如，GPT-3有1750亿参数，包含96层Transformer块。

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2Fj3gficicyOvattV3Cy7muORnkSUx9P3EBPBicQpcwfhRkOm0DLyCD8r3AYEQh2jqibQO2YZNZfGP7y9xyAPe3qhMEA%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26tp%3Dwebp%26wxfrom%3D5%26wx_lazy%3D1&valid=false)

##### 1.3.6 训练任务设计、执行和优化

##### 预训练任务设计

**自监督学习** ：无需人工标注，通过文本自身生成监督信号。

*
  **因果语言建模（CLM）** ：预测下一个Token，目标函数：
  ![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2Fj3gficicyOvattV3Cy7muORnkSUx9P3EBPDONoztuqW3E03VqOyuRIjDsOfnHibGBSAibSBsZ8WawZVADOw1bfHUIg%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26tp%3Dwebp%26wxfrom%3D5%26wx_lazy%3D1&valid=false)
*
  **掩码语言建模（MLM）** ：随机遮盖部分Token并预测（如BERT），遮盖比例通常15%。

*
  **混合目标** ：如UniLM结合双向和单向预测。

##### 训练执行

###### 训练过程

分布式训练，并行策略执行、通信优化，每一轮训练（单步训练）流程包括：

1.
   数据加载与预处理，可以是分布式数据加载，或动态批次构建。
2.
   前向传播（含激活重计算）
3.
   反向传播
4.
   梯度同步（数据并行）
5.
   参数更新（含梯度裁剪）

Transformer结构的训练通常需要经过上万轮的训练，即上万个训练步数，训练时会充分利用GPU并行的特性，在分布式训练中并行，包括数据并行、模型并行、张量并行、流水线并行，且总GPU数 = 数据并行度 × 模型并行度。

**数据并行（Data Parallelism）** ：将批次（Batch）划分为多个子批次（Sub-batch），分配到不同GPU上并行处理。**模型并行（Model Parallelism）** ：

*
  **张量并行（Tensor Parallelism）** ：将单个矩阵运算拆分到多GPU（如Megatron-LM）。
*
  **流水线并行（Pipeline Parallelism）** ：将模型层拆分到多GPU（如GPipe）。

举例GPT-3的预训练情况，加深直观理解：

*
  参数量：1750亿
*
  训练数据：约3000亿token
*
  训练步数：约94000步（批量大小3.2M tokens/步，3000亿/3.2M 约等于94000）
*
  耗时：数周（使用数千张A100 GPU）
*
  上下文大小：原始上下文长度是2048 Tokens，硬件显存和注意力计算复杂度的权衡结果，Transformer的自注意力机制计算复杂度为 O(n2)（n为序列长度），导致显存和计算成本随序列长度急剧增长。

这里批量大小和上下文大小的关系是：序列数=批次大小/上下文长度=3.2\*10\^6/2048≈1562 个序列/步，批次大小是并行训练的序列数量，而上下文长度是单个序列的长度。这里对tokenization后的数据集进行切分为一个个小块（chunk），这个chunk的大小就是上下文窗口长度（context window），chunk的大小是序列长度，批次大小是同时处理的chunk数量，训练批次总token数是两者的乘积。

###### 单轮训练结果

在预训练的阶段，每一轮预训练训练的结果是得到一个基础模型（Base Model），这个模型可以预测每一个输入序列tokens的下一个token，可能每个词汇token都会有一个概率，这里是统计性和概率性的结果，是对训练数据集的回放。
![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2Fj3gficicyOvattV3Cy7muORnkSUx9P3EBP0KKKnY3M73dWfuxoWyCYLUU7IdiaQxKnR6nUrfVA4P8j3LbajsibRZjQ%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26tp%3Dwebp%26wxfrom%3D5%26wx_lazy%3D1&valid=false)

上图得到的next token ID 是19348(" Direction")，但是我们期望的是3962（" Post"）概率更高一些。所以，在完成一轮训练后，我们会用测试数据集进行测试，计算Lost函数，并将拟合偏离反馈到神经网络的参数调整上，这样下一轮训练后，token ID 3962（" Post"）的概率就会更高一些。
![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2Fj3gficicyOvattV3Cy7muORnkSUx9P3EBPSf4hqianoaQZSOvnT2nqUicSuqxLEwekFj6ebITyD83pCpxPCNPqKdaw%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26tp%3Dwebp%26wxfrom%3D5%26wx_lazy%3D1&valid=false)

整个训练的过程，我们逐步调整参数权重，这种权重的参数有上亿个，如DeepSeek R1满血版参数量是671B(6710亿)个，GPT-3 的参数量是 1750 亿，GPT4的参数量1.8 万亿左右，这是很大的参数量。所以，我们可以理解为神经网络实际上是一个非常巨大的数学表达式，我们预训练后得到的就是这样一个或者一群这样的函数表达式。
![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2Fj3gficicyOvattV3Cy7muORnkSUx9P3EBPBc3D9SD283ibMkCDEXTNQp8z4Pl03XqsUIbUGrjAyTic61CLHx0oB56A%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26tp%3Dwebp%26wxfrom%3D5%26wx_lazy%3D1&valid=false)

这样一个超巨大的数学表达式展开式什么样的呢？这里有一个大模型可视化网址[bbycroft.net/llm](https://bbycroft.net/llm) ，可以看到一个85584个参数的神经网络，这里详细讲解了通过预训练后得到的排序神经网络，在处理一个排序任务的时候整个过程，推荐大家去做拓展阅读。这里面还有GPT-2、GPT-3的神经网络可视化，可以直观感受到不同规格参数的神经网络。
![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2Fj3gficicyOvattV3Cy7muORnkSUx9P3EBPPGJRrteicIrI3pTGn3q62QsNBukvS9yWJTKeBoCtQl3ULFyhKw5snzQ%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26tp%3Dwebp%26wxfrom%3D5%26wx_lazy%3D1&valid=false)

循环训练以上单步训练外，还需要引入优化，保证训练结果。

##### 训练优化

包括软件技术优化和硬件技术优化。

**软件技术优化：**

*
  **混合精度训练** ：
  *
    **FP16/FP8存储** ：参数和梯度用低精度保存，减少显存占用，DeepSeek 的优化之一就是FP8化，并且开源了他们FP8的项目[DeepGEMM](https://github.com/deepseek-ai/DeepGEMM)，提升效果是很明显的。![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2Fj3gficicyOvattV3Cy7muORnkSUx9P3EBPiaibo9ViaTToYMRhxuMT4H16cg3Yb9WT1xkfLGd1hXiaQQXFfpvFfQokkg%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26tp%3Dwebp%26wxfrom%3D5%26wx_lazy%3D1&valid=false)
  *
    **Loss Scaling** ：对损失值放大以防止梯度下溢。
*
  **激活检查点（Activation Checkpointing）** ：
  *
    仅保存关键层的激活值，其余在反向传播时重新计算，显存减少30%-50%。
*
  **内核融合（Kernel Fusion）** ：
  *
    将多个CUDA操作合并为单一内核（如将LayerNorm + Dropout融合）。

**硬件技术优化**

1.
   **显存管理**
   1.
      **显存池（Memory Pool）** ：预分配显存块，避免碎片化。
   2.
      **页锁定内存（Pinned Memory）** ：加速主机到设备的数据传输。
2.
   **计算加速**
   1.
      **FlashAttention** ：优化注意力计算显存占用，支持更长的上下文（如32K）。
   2.
      **稀疏计算（Sparsity）** ：对MoE（Mixture of Experts）模型的专家路由动态分配计算资源。

##### 1.3.7 预训练产物

![](https://image.cubox.pro/cardImg/51p23101x6gqf79okd434zhycuwxw3smlcs80ozfncuunulshc?imageMogr2/quality/90/format/gif/ignore-error/1)

至此，我们得到了一个基础模型（Base Model）,可以看做是一个互联网词汇模拟器，它能够模仿数据集的知识，蹦出概率较高的下一个token，这些token组成的知识是模糊的、具有统计性质的。就像是将数据集的只是内化存储到了神经网络之上，知识可以被拟合回放。但是它还不能成为一个有用的助手，它的回答可能是不可读，甚至有害的，这时候给他问题他也许只会给出更多问题或者做简单背诵。还需要进到后训练才能做出正确相应，成为一个有个性的助手。

#### 1.4 后训练

进一步优化模型性能、对齐人类意图或适应特定任务的阶段。这一阶段的关键在于让模型从"通用知识库"转变为"可控、安全、可用的工具"。

后训练是LLM从"知识存储"到"实用工具"的关键过渡。通过这一过程，模型不仅学会生成流畅文本，还能在安全性、可控性和任务适应性上达到实际应用标准。例如，ChatGPT的后训练阶段（包括SFT和RLHF）使其能够理解复杂指令并生成符合伦理的回答，而未经后训练的原始GPT模型可能输出有害或无意义内容。

这一过程需要大量高质量数据、计算资源和多学科协作（如语言学、伦理学、计算机科学），是当前LLM研发的核心挑战之一。

##### 1.4.1 监督微调**（Supervised Fine-Tuning, SFT）**

我们在用的聊天型LLM是对话模式的，
![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2Fj3gficicyOvattV3Cy7muORnkSUx9P3EBP6218ibxuXvyXvwaJZHIRPBzlKmrU6VdssfBV4iaTkIygibSaWOI1TzA7A%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26tp%3Dwebp%26wxfrom%3D5%26wx_lazy%3D1&valid=false)

对话示例 通过人工标注的高质量数据，调整模型的输出风格、格式和内容，使其更符合实际需求。

**数据集：** 是一组对话列表，是通过人工创建的高质量对话。

**方法** ：使用问答对、指令-响应数据（例如：用户指令+理想回答）进行微调，对模型进行"隐式编程"，进一步调整了权重，模型会逐渐建立从自然语言指令到目标响应的隐式映射函数，通过梯度下降在参数空间中寻找指令对齐的最优解。

**效果** ：提升模型对指令的理解和响应质量，减少无意义或重复输出。

数据集的构造，早期OpenAI是在upwork（一个自由职业平台）和scaleAI（一个标注平台）发布问题任务，由网友完成回答并提交，形成数十万的条基础数据集。
![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2Fj3gficicyOvattV3Cy7muORnkSUx9P3EBPn8nFL9pkUTPrwNqYwHUN6yppGUib4gtV4JHQqpPe0tIMdp9ncj9ydTg%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26tp%3Dwebp%26wxfrom%3D5%26wx_lazy%3D1&valid=false)

OpenAI在2022年的一个论文《Training language models to follow instructions with human feedback》 如今，大量标注工作由大语言模型辅助完成（例如，人类更多是进行编辑而非从头撰写），甚至有些标注完全是合成生成的，如著名的[UltraChat](https://github.com/thunlp/UltraChat)：

gif

nvidia公开的一份代码SFT数据集示例如下图：
![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2Fj3gficicyOvattV3Cy7muORnkSUx9P3EBPdzZJgIApaAGCwfialWmpW1oHxicH5BAP8bXomewzHUhAjIpibhgViaYk7Q%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26tp%3Dwebp%26wxfrom%3D5%26wx_lazy%3D1&valid=false)

huggingface上的后训练数据集 Models need tokens to think，问答是否更好，也会考虑模型本身的特性，那些能让回答逐步计算和迭代的回答更好，跳跃性、单步计算量的回答是没那么好。比如下图右边的答案更好，因为他是逐步推导和计算，在最后给出的答案，而左边在一开始就做了全部计算，这对模型本身的计算消耗是更大。
![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2Fj3gficicyOvattV3Cy7muORnkSUx9P3EBPicQ5JbichX4KlLCQiadrrtQCBMHm5e2NfNVKicQb92nvce9KhNE1otguRQ%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26tp%3Dwebp%26wxfrom%3D5%26wx_lazy%3D1&valid=false)

##### 1.4.2 奖励模型（Reward Modeling）

*
  **目的** ：训练一个能够评估生成内容质量的奖励模型（Reward Model），为后续强化学习提供反馈信号。
*
  **方法** ：
  *
    数据集，收集人类对模型输出的排序数据（例如：让标注者对多个回答按质量排序），在huggingface上公开的一些数据集会附上评分。
  *
    训练奖励模型，使其能够预测人类对回答的偏好（如回答A比回答B更好，B比C更好，则A是winning_response，C是losing_response）。
  *
    数据格式，三元组（Prompt, 优质回答, 劣质回答），或四元组（Prompt, 回答A, 回答B, 偏好标签。
  *
    关键点，奖励模型通常是另一个小型神经网络，学习人类的偏好标准。
  *
    模型架构设计，通常基于预训练语言模型（如BERT、GPT）改造，移除最后一层并添加标量输出层，即输出标量分数，表示回答的质量。
  *
    损失函数，基于对比学习，常用Bradley-Terry模型计算偏好概率，L=−log(σ(r(q,w)−r(q,l))) ，其中r(q, w)和r(q, l)分别是对优质回答和劣质回答的预测分数，σ为Sigmoid函数。
  *
    验证与迭代，一致性：对相似质量的回答评分差异小，区分度：能捕捉回答间的细微质量差距，对齐度：预测分数与人工标注偏好高度相关（如Kendall Tau系数）。

##### 1.4.3 领域适应（Domain Adaptation）

**目的** ：解决**源域** （训练数据）与**目标域** （测试数据）分布不一致的问题，使模型在目标域上保持高性能，适应特定领域知识（如医疗、法律、金融、代码生成）。

**方法** ：

*
  在领域相关数据上继续预训练（持续预训练）。
*
  使用领域指令数据进行监督微调。

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2Fj3gficicyOvattV3Cy7muORnkSUx9P3EBPUsU6Z3LnFgxy2g7vUTYsF1ibXIIbtNvoOoojlXSblnUgaGQQKo43ZEA%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26tp%3Dwebp%26wxfrom%3D5%26wx_lazy%3D1&valid=false)

##### 1.4.4 模型存在的问题

1、幻觉和解决办法
![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2Fj3gficicyOvattV3Cy7muORnkSUx9P3EBPQOtugKPEh2MjLOo8agkXZItetw1HFX48iaaeV99sY94uTT7iaDqBP6nA%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26tp%3Dwebp%26wxfrom%3D5%26wx_lazy%3D1&valid=false) 企业微信截图_05db3b26-91f3-4523-99b7-4de36a915e6a

2、长记忆和解决办法

发生场景：对话上下文非常长时，如上传了文件、多轮对话、跨模态任务融合等

技术原因：上下文窗口硬性限制、信息稀释与注意力衰减、模型无状态和存储机制缺失、计算资源和效率的矛盾（需要分布式计算）

解决办法：外部存储结合（向量数据库）、显示记忆和分层存储（高频知识内化到模型参数、中频KV向量存储、低频动态检索）等方法
![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2Fj3gficicyOvattV3Cy7muORnkSUx9P3EBP764g7hK0Bibwc7cKqHmayuDeKFJWL1q0DLV9YF4X5MQxv0xx2ia8UmBA%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26tp%3Dwebp%26wxfrom%3D5%26wx_lazy%3D1&valid=false)

3、数学计算能力 经典问题：
![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2Fj3gficicyOvattV3Cy7muORnkSUx9P3EBPkx1OwpThuzVKiaq2pK2ibFpQcvYUhMxYnSiaVyMIFbktNpG1f9o4Trgtg%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26tp%3Dwebp%26wxfrom%3D5%26wx_lazy%3D1&valid=false)

进行大数乘法的时候，通过心算，得出近似的错误答案：
![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2Fj3gficicyOvattV3Cy7muORnkSUx9P3EBPZeEzRYibfkcGlr6n1wiaDm2lsdZrDice6NaVZwPUyfM9e1q5TyjHxFBVQ%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26tp%3Dwebp%26wxfrom%3D5%26wx_lazy%3D1&valid=false)

DeepSeek R1思考了很久，最终通过心算计算正确，应该是借助MoE分配给了数学专家神经网络完成了正确的推算。
![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2Fj3gficicyOvattV3Cy7muORnkSUx9P3EBPG0kcYScJsEpCGnbgoeN2YAsHqGUFVANvqMNmUKLHNUVRSAic6xG4M0g%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26tp%3Dwebp%26wxfrom%3D5%26wx_lazy%3D1&valid=false) ![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2Fj3gficicyOvattV3Cy7muORnkSUx9P3EBPEN1Og3IDQJX95xu2ITp1dWZejXXQTiaHsX30WuUlz2deP7jElCYjIxg%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26tp%3Dwebp%26wxfrom%3D5%26wx_lazy%3D1&valid=false)

4、模型直接使用工具

模型本身还不具备注解调用工具的能力，目前都是在模型输出后给到应用层来完成工具调用。

5、Tokenization的副作用
![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2Fj3gficicyOvattV3Cy7muORnkSUx9P3EBPQeUcM3CWd8Ejodmg62DPZbQSgbiad52MkHxOJN1xPDKoWDP1s8BfWBg%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26tp%3Dwebp%26wxfrom%3D5%26wx_lazy%3D1&valid=false) ![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2Fj3gficicyOvattV3Cy7muORnkSUx9P3EBPkRgw9GzCCGostsyUTAzCgPN373kZk1YPpKHEnVtxaj8hiarR11jXUDw%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26tp%3Dwebp%26wxfrom%3D5%26wx_lazy%3D1&valid=false)

#### 1.5 强化学习（RL）

通常认为RL是属于后训练的一部分，但Andrej Karpathy认为RL和SFT、RLHF是有本质区别的。RLHF在不可验证的领域进行学习，通过持续采样、评分和策略更新逐步对齐人类偏好，在完成训练后做重复训练是没有收益的；而RL是可以不断重复对模型进行改进，获得复利的，如增加推理轮次获得更深度的思考结果。而RL从后训练中拿出来是因为RL有广阔的前景，RL是推理模型构建的必要，也是模型走向AGI的关键。
![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2Fj3gficicyOvattV3Cy7muORnkSUx9P3EBPhib2zUIWOajQGF3rS3HxKKXKFSTHSyT4hZvta12NfNXnmYLd6PI9PFw%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26tp%3Dwebp%26wxfrom%3D5%26wx_lazy%3D1&valid=false)

早在DeepMind的AlphaGo就在用，但是是在封闭的环境内，是明确游戏规则的，在开放化话题中表现不佳，如何提升在开放环、开放话题的表现一直是业界难题。RL是当前业界前沿的技术话题，DeepSeek是第一个公开讨论实现方法并开源了实现成果、开源实现工具和实现框架的，所以我主要是阅读[DeepSeek_R1.pdf](https://github.com/deepseek-ai/DeepSeek-R1/blob/main/DeepSeek_R1.pdf)来理解RL。论文中提出了一种用强化学习"教会"大模型自主推理的方法。他们先训练了一个完全靠自我摸索成长的模型（DeepSeek-R1-Zero），发现它虽然聪明但"说话混乱"；于是改进出一个结合少量示例教学和多阶段训练的升级版（DeepSeek-R1)，最终达到接近顶尖闭源模型的水平。团队还成功将大模型的能力"压缩"到小模型上，让手机等设备也能运行高性能推理模型。这项工作为AI自主学习和知识迁移提供了新思路，并开源了全部成果供社区使用。

##### 1.5.1 训练方法

1、通过纯强化学习（无需监督微调）训练，直接从基础模型（DeepSeek-V3-Base）开始，使用GRPO（Group Relative Policy Optimization）算法优化，通过分组奖励估计替代传统批评模型，降低训练成本。奖励模型结合准确性奖励（基于规则验证结果）和格式奖励（强制结构化输出）。模型在训练中自然涌现出自我验证、反思、生成长思维链（CoT）等能力，在数学（如AIME 2024）、编程等任务上表现优异（pass@1达71%），但存在可读性差和语言混合问题。

2、为解决DeepSeek-R1-Zero的缺陷，引入冷启动数据（人工设计数千条高质量长思维链可读模板示例）初始化模型，随后进行两阶段强化学习（优化推理能力与人类偏好对齐）和两阶段SFT（融合推理与非推理任务数据）。最终性能与OpenAI的o1-1217模型相当，在AIME 2024上pass@1达79.8%，数学任务（MATH-500）准确率达97.3%。

3、将DeepSeek-R1的推理能力迁移到小规模密集模型（1.5B至70B参数的模型），即直接使用DeepSeek-R1生成的80万条数据微调小模型，无需额外强化学习。例如，蒸馏后的14B模型在AIME 2024上超越QwQ-32B-Preview，32B和70B模型在推理基准上刷新记录。

示例：国人开源，基于满血DeepSeek-R1生成，可用于蒸馏的中文数据集 [huggingface.co/datas...](https://huggingface.co/datasets/Congliu/Chinese-DeepSeek-R1-Distill-data-110k)

##### 1.5.2 思维链（CoT，chain-of-thought）

在解决复杂问题时生成的一种**结构化推理过程，** 它要求模型不仅输出最终答案，还需详细展示解题的中间步骤（如逻辑推导、公式计算、假设验证等），从而提升推理的透明性和准确性。示例：

    <think>  1. 设方程 √(a−√(a+x)) = x，首先平方两边得到 a−√(a+x) = x²；  
    2. 进一步整理得 √(a+x) = a−x²，再次平方后化简为四次方程；    
    3. 发现中间步骤可能有误，重新检查并修正推导逻辑...</think>
    <answer>
    .....最终答案是...... 
    </answer>

主要作用：1、提升准确性，在数学（AIME 2024）、编程（Codeforces）等任务中，CoT帮助模型分解复杂问题，减少计算错误。

2、增强可解释性，CoT使模型的思考过程可视化，便于用户理解其决策逻辑，尤其在教育、科研等需透明推理的场景中价值显著。

3、支持长上下文推理，模型通过生成数百至数千个推理标记（Token），逐步解决需多步推导的问题（如证明题或代码调试）。

示例：
![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2Fj3gficicyOvattV3Cy7muORnkSUx9P3EBPl7M2qjlNBRj6Ae0gvzhU5Pmtyb36pa9o0yTMRWtppNvf4DBoGuQaGQ%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26tp%3Dwebp%26wxfrom%3D5%26wx_lazy%3D1&valid=false)

##### 1.5.3 Aha moment

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2Fj3gficicyOvattV3Cy7muORnkSUx9P3EBPqAKOZfibqnCe85Uqt1LcYadefC0I6qzap5giaEtpErKdctVcnF0KHddw%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26tp%3Dwebp%26wxfrom%3D5%26wx_lazy%3D1&valid=false)

在强化学习（RL）过程中，DeepSeek - R1 - Zero 在训练集上的平均回复长度。DeepSeek - R1 - Zero 自然而然地学会了花费更多思考时间来解决推理任务。
![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2Fj3gficicyOvattV3Cy7muORnkSUx9P3EBPicVgMKmlDELEHwSYXUrMg89mO7DMNUXa3fOuoyibj7snxmx8CSjsI57w%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26tp%3Dwebp%26wxfrom%3D5%26wx_lazy%3D1&valid=false)

DeepSeek - R1 - Zero 一个中间版本的有趣 "顿悟时刻"。该模型学会了以拟人化的口吻重新思考。这对我们来说也是一个顿悟时刻，让我们见证了强化学习的力量与美妙之处。

#### 1.6 原理总结

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2Fj3gficicyOvattV3Cy7muORnkSUx9P3EBPXOfLo1ZQljSMoskhQBuib50klC84uqO8gviaYy9RUXLnecnqXcjgNr6g%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26tp%3Dwebp%26wxfrom%3D5%26wx_lazy%3D1&valid=false)

图片来源 [zeropointlabs.ai/lla...](https://zeropointlabs.ai/llama-3-1-405b-metas-most-capable-llm/)

输入文本tokens，token向量化，自注意、多头注意，前馈神经网络，循环自注意、多头注意，前馈神经网络，输出文本token，自回归解码，追加到输入tokens，循环上述过程。展开一些就是下面的过程：
![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2Fj3gficicyOvattV3Cy7muORnkSUx9P3EBPBicQpcwfhRkOm0DLyCD8r3AYEQh2jqibQO2YZNZfGP7y9xyAPe3qhMEA%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26tp%3Dwebp%26wxfrom%3D5%26wx_lazy%3D1&valid=false)

再展开可以看大模型可视化 [bbycroft.net/llm](https://bbycroft.net/llm)
![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2Fj3gficicyOvattV3Cy7muORnkSUx9P3EBP3QyAKufCJPfp83KhnshACVqVO1LsBHtVupGFX2rJ0IsBWgJ1XSGKYg%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26tp%3Dwebp%26wxfrom%3D5%26wx_lazy%3D1&valid=false)

### 2 市面上主流特性和应用

#### 2.1 文件上传

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2Fj3gficicyOvattV3Cy7muORnkSUx9P3EBPbPqYMic7InGUib2D7zpicMHp9qVtNGicUelN4wHWLutcJQq6wX15b40BUw%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26tp%3Dwebp%26wxfrom%3D5%26wx_lazy%3D1&valid=false)

##### 流程浅析

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2Fj3gficicyOvattV3Cy7muORnkSUx9P3EBPPqC7R9sAib7eyKh3NUCMDCCaEGA8WGRCdUR9MlmwpstBqIkSr7bQMnQ%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26tp%3Dwebp%26wxfrom%3D5%26wx_lazy%3D1&valid=false)

1、解析文件，拿到文本序列（也有模型方案支持理解图片、表格等），将文本切分一个个小块，组成一个很长的块序列。

2、文件内容token化，把用户输入文本拼在一起，作为输入。

3、经过神经网络这个超大函数，输出丢出token。

4、循环第三步，直到结束符出现。

#### 2.2 网络搜索

解决最新知识缺失问题。
![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2Fj3gficicyOvattV3Cy7muORnkSUx9P3EBPGmU9ScZWbEOHQkdteeqQJ7HqZOicHjYjGdkXtPYoRXeBHlVxF2frC4g%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26tp%3Dwebp%26wxfrom%3D5%26wx_lazy%3D1&valid=false)

##### 搜索流程浅析

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2Fj3gficicyOvattV3Cy7muORnkSUx9P3EBPu2hjvbuGLrOqTsm8VicSZ8icric16lejzWWBOwqWgpOg6WrTDx6I0yicCw%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26tp%3Dwebp%26wxfrom%3D5%26wx_lazy%3D1&valid=false)

1、将用户输入做总结，特别是在经过多轮对话后，关注点分散、关键词不易捕捉的情况。

2、调用搜索引擎，每个AI聊天应用的实现情况不一样，调用特定的搜索引擎，如ChatGPT是Bing，DeepSeek是博查。

3、对搜索结果列表中内容进行阅读和解析。

4、对搜索结果进行相关度排序，选出前N；Rerank模型，对初步检索结果重新排序，提升相关性（如Cohere Reranker、Cross-Encoder）。

5、将前N篇文章作为参考内容，标识草考内容与用户Query一起传给LLM。

6、大模型返回结果。

![](https://image.cubox.pro/cardImg/1ggqme7i2k70kkmd0jd7wrl4yt9sd06oqlduo3voycqgh5kphf?imageMogr2/quality/90/ignore-error/1)


![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2Fj3gficicyOvasVeMDmWoZ2zyN8iaSc6XWYj5q5PQEOc5ibURPb03vnRibrxC3UR8xzdyATfiawTYRV2vJvBnAIcE1FeQ%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26tp%3Dwebp%26wxfrom%3D5%26wx_lazy%3D1&valid=false)

[Read in Cubox](https://cubox.pro/web/card/7323977750799190022)
