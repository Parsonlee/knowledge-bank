# 北京大学发布LLMs（预训练+微调）数据管理全流程综述

[mp.weixin.qq.com](https://mp.weixin.qq.com/s/AFooqkOIpLaMJY8v23Ze8w)谢年年 夕小瑶科技说


![图片](https://image.cubox.pro/cardImg/2023121916411888967/75516.jpg?imageMogr2/quality/90/ignore-error/1)

夕小瑶科技说 原创  
作者 \| 谢年年、python**数据一直以来都是大语言模型（LLMs）构建的基石。LLMs强大的能力在很大程度上依赖于在大量数据上的自我监督预训练。** 并且，通过进一步在指令数据集上进行有监督微调，可以进一步提高LLMs遵循指令和完成各种各样下游任务的能力。

然而，现有的许多知名LLMs并没有详细公布或深度总结其在训练全阶段所使用的数据情况，以及如何进行数据去重、过滤等数据管理过程。

**近日，来自北京大学的学者发布了LLMs训练数据管理全流程综述，分别从预训练与有监督微调两个阶段详细总结了包括数据规模、数据质量、领域组成以及数据管理系统等方面的研究。**

**论文标题** :  
Data Management For Large Language Models: A Survey

**论文链接** :  
https://arxiv.org/pdf/2312.01700.pdf
![图片](https://image.cubox.pro/cardImg/2023121916411987167/91993.jpg?imageMogr2/quality/90/ignore-error/1)

## 预训练阶段

### 1. 数据规模

模型规模与训练数据集规模之间符合缩放定律，即当模型大小和训练计算预算没有瓶颈限制时，模型性能与训练数据集规模呈幂律关系。只要同时扩大模型大小和训练数据集规模，模型性能可以提高，但如果其中一个固定而另一个增加，就会遇到过拟合问题。因此，**在更多的计算预算下，模型大小和数据集规模应以大致相同的速度扩大**。

但是随着模型规模的不断增加，高质量训练数据总有一天会耗尽，因此研究者开始关注重复数据的利用。\[1\]发现在精心选择的重复数据上训练可以超过在随机选择的新数据上训练的模型的效果，而在随机选择的重复数据上训练则大打则扣，这表明了智能选择重复数据是应对数据枯竭的一条有效思路。

### 2. 数据质量

高质量的数据在机器学习任务的训练中至关重要。在LLM的预训练中需要采取一些系列技术保证数据质量。

1.
   **去重**：去重可以减模型记忆问题、避免训练-测试重叠并提高训练效率。常用N-gram相似性与MinHash技术来检测重复的训练数据集。
2.
   **质量过滤**：公共数据集中通常包含质量低的数据，妨碍模型训练，一般采用分类器、手工启发式算法或者根据困惑度等标准进行阈值过滤。另外需要注意过滤的阈值设定，\[2\]表明对于类似GPT的LLM，在广泛任务上过滤可能会导致性能下降。
3.
   **毒性过滤**：毒性是指可能让某人离开讨论的粗鲁、无礼或不合理的语言内容。与质量过滤类似，毒性过滤多采用启发式和基于规则的过滤方法以及N-gram分类器。过渡毒性过滤也会降低模型的泛化能力和毒性识别能力，增加有毒内容生成的风险。
4.
   **社会偏见**：预训练的LLM可以捕捉到大量训练文本中包含的社会偏见。现有的过滤器还不足以解决该问题，现有研究多是通过实验证明了LLMs包含大量偏见，对如何缓解社会偏见的工作还比较少。
5.
   **数据多样性**：在构建数据集时尽量保证数据类型来源以及内容的多样性。\[3\]提出了一种新颖的修剪方法，通过将数据集表示为包含困难分数的无向图，并采用正向和反向消息传递策略来选择一个既包含多样性又包含困难区域的核心集。

### 3. 数据组合

公开可用的预训练数据集通常是从多个来源和领域收集的数据混合而成的。以常用的预训练集Pile为例，它包含了来自Common Crawl、Wikipedia、书籍以及医学、学术、编码和数学、法律和社交资源等多个领域的网络文档。那么，这种混合数据会对模型的性能产生影响吗？实验结果表明，高质量（如书籍）和高多样性（如网络）的数据领域对模型的性能有广泛的帮助，即使这些数据与具体的下游任务不是完全相关。因此，在构建预训练数据集时，应该囊括尽可能多的可靠数据来源。

### 4.数据管理系统

本文介绍了两个数据管理系统。DataJuicer\[4\]有50多个灵活的数据管理操作符和专用工具，可以生成多样化的数据配方。这个系统非常适合零代码数据处理、低代码定制和现成数据处理组件。它还支持在数据配方和LLM的多个开发阶段上进行及时反馈循环。Oasis\[5\]是一个预训练数据整理和评估系统，包括交互式模块化规则过滤模块、去偏的神经质量过滤模块、自适应文档去重模块和整体数据评估模块。

## 有监督微调阶段

本文还总结了LLM在有监督微调中对数据规模、数据质量（包括指示质量、多样性、复杂性和提示设计）以及任务组成的研究。

### 1.数据规模

对于数据规模的研究分为两个流派，一是侧重于减少指令数据以提高训练数据，如LIMA\[6\]精心筛选了1000个高质量样本微调模型并获得了不错的效果。

另一个主张扩大指令数据的数量，但很多研究表明数据量的大小对模型能力的影响因任务和模型规模而异，比如\[7\]认为扩大指令数据可以改善部分任务，但对数学和思维链等任务没有明显提升。而\[8\]则认为模型的一般能力在约1000个样本后提升缓慢，而数学推理和代码生成则随数据量增加稳步提升。因此，应根据具体任务和能力选择合适的数据量和调整方法。

### 2. 数据质量

1.
   **指令的质量**:指令数据的质量是提高模型性能最重要的因素之一。因此，\[9\]使用困惑度作为指标，从开源模型生成的候选指令池中选择最合适的指令。\[10\]利用语言模型本身为增强指令分配质量得分，并通过迭代改进模型预测结果。

2.
   **指令的多样性**：在常见的开放式有监督微调数据集中，规模越大，多样性越强，而性能更好。因此为了更好地评估SFT数据集的指令多样性，\[11\]提出使用ChatGPT作为开放式细粒度标注器，将指令多样性量化为整个标签集的独特标签覆盖率。

3.
   **指令复杂度**:\[12\]证明增加复杂性可以带来持续的性能改进。而且，这种改进并不是由于令牌数量的增加，因此\[13，14\]采用增加推理、添加约束、逐层演化、加深和加重代码和表格输入等操作逐步重写指令增加指令复杂度

4.
   **提示设计**:目前的指令设计主要有两种方式：人类启发式设计和LLMs合成。但不同的指令选择可能会对模型性能产生显著影响。目前，哪种指令更好尚未得到充分探索。

### 3.任务组合

多任务微调可以进一步提高LLMs对未知任务的泛化性能。除了任务数量的扩展外，不同指令基准的混合比例和任务平衡对于有效的指令微调也至关重要。不同于将多个任务组合在一起，\[15,16\]表明，在单个任务数据上微调的专家LLM可以胜过在多个任务上微调的LLM。

## 挑战与未来方向

### 1.需要更全面和细致的理解

虽然人们已经做了很多工作来理解数据管理对不同训练阶段的影响，但目前的研究仍不全面。此外，不同的技术可能会有不同的优点和缺点，需要根据具体情况进行选择和平衡。例如，在质量和过滤效果之间需要进行权衡，去毒化和去偏见后所得到的效果是相互矛盾的，少量高质量数据的微调和数据扩展之间也无法两全。

### 2. 通用数据管理框架

虽然已经有了Data-Juicer和Oasis这样的数据管理系统，可以帮助组合LLM预训练阶段或SFT阶段的各种数据配方，但研究者仍然需要花费精力寻找合适的数据集。因此，需要一个构建更简单、更方便、更通用的数据管理系统，帮助人们更容易地找到和使用合适的数据集。

### 3. 幻觉问题

虽然LLM很强大，但幻觉在所难免，甚至会产生严重的后果。减轻幻觉主要可以从两个方面入手，一是提取高质量数据的预训练语料库；二是在有监督微调阶段，人工筛选的高质量指令数据和自动选择的高质量指令数据。这是我们在训练大模型时不可忽视的部分。

### 4.社会偏见和公平性

虽然LLM的社会偏见与公平性已经被广泛探索了，但是离理想的LLM还存在较大差距，未来仍然有很多值得探索的问题，例如如何减轻预训练数据集中的潜在偏见，有监督微调数据集中的偏见存在，以及是否可以通过有监督微调减少社会偏见等。

### 5.多模态数据管理

随着LLM被应用到更多的领域，构建多模态数据集变得越来越重要。目前的多模态LLM通常通过手动设计指令或者GPT辅助生成指令等方式构建指令调优数据集。因此多模态数据管理也是一个未来的研究方向，包括如何扩展数据、如何控制数据质量以及如何平衡不同任务等等。

## 结论

本文对LLM训练中的数据管理进行全面概述，分别讨论了LLM的预训练和有监督的微调阶段，并总结了目前关于每个阶段的数据数量、数据质量和领域/任务组成的研究成果，能够帮助从业者更好地理解和应用LLM训练的数据管理，为LLM未来的发展提供一些新的启示。

![图片](https://image.cubox.pro/cardImg/2023121916411985728/75749.jpg?imageMogr2/quality/90/ignore-error/1)![图片](https://image.cubox.pro/cardImg/2023121916411933692/57660.jpg?imageMogr2/quality/90/ignore-error/1)![图片](https://image.cubox.pro/cardImg/2023121916411966203/86687.jpg?imageMogr2/quality/90/ignore-error/1)


#### 参考资料


\[1\]Kushal Tirumala, Daniel Simig,Armen Aghajanyan,and Ari SMorcos. 2023. D4: Improving llm pretraining via document deduplication and diversification.arXiv preprint arXiv:2308.12284.  
\[2\] Kushal Tirumala, Daniel Simig, Armen Aghajanyan, and Ari S Morcos. 2023. D4: Improving llm pretraining via document de-duplication and diversification. arXiv preprint arXiv:2308.12284.  
\[3\] D2 pruning: Message passing for balancing diversity and difficulty in data pruning. arXiv preprint arXiv:2310.07931.  
\[4\] Data-juicer: A one-stop data processing system for large language models. arXiv preprint arXiv:2309.02033.  
\[5\] Oasis: Data curation and assessment system for pretraining of large language models. arXiv preprint arXiv:2311.12537.  
\[6\]Lima: Less is more for alignment. arXiv preprint arXiv:2305.11206.  
\[7\]Exploring the impact of instruction data scaling on large language models: An empirical study on real-world use cases. arXiv preprint arXiv:2303.14742.  
\[8\]How abilities in large language models are affected by supervised fine-tuning data composition. arXiv preprint arXiv:2310.05492.  
\[9\]Harnessing the power of david against goliath: Exploring instruction data generation without using closed-source models. arXiv:2308.12711.  
\[10\] Self-alignment with instruction backtranslation. arXiv preprint arXiv:2308.06259.  
\[11\] #instag: Instruction tagging for analyzing supervised fine-tuning of large language models\[12\] Chatbridge: Bridging modalities withlarge language model as a language catalyst.  
\[13\] Wizardlm: Empowering large language models to follow complex instructions. arXiv preprint arXiv:2304.12244.  
\[15\] Exploring the benefits of training expert language models over instruction tuning.  
\[16\] Maybe only 0.5% data is needed: Apreliminary exploration of low training data instruction tuning

[Read in Cubox](https://cubox.pro/web/card/7136381194786049041)
