---
id: "7271069011834571080"
cubox_url: https://cubox.pro/web/card/7271069011834571080
url: https://mp.weixin.qq.com/s/PQF8Ka5UPYxpnEASTUSs5w
tags:
  - RAG
  - RAG/query
---
# ICLR2025盲审论文DMQR-RAG：多样查询改写，查询P@5提升了14.46%，超过RAG-Fusion

论文解析

[Read in Cubox](https://cubox.pro/web/card/7271069011834571080)  
[Read Original](https://mp.weixin.qq.com/s/PQF8Ka5UPYxpnEASTUSs5w)  

---

## Annotations  

> 改写策略
> 为了提升检索文档的多样性，同时考虑到用户查询可能存在的信息噪音或冗余问题，本文提出四种改写策略：
>
> 信息等同：改写的目标是消除用户查询中的噪音并精炼查询。具体实现为通用查询改写（GQR）和关键词提取改写（KWR），分别通过保留原始查询中的关键信息或直接提取关键词来提升检索精度。
>
> 信息扩展：通过整合LLMs的先验知识生成伪答案，使查询扩展更多信息；该策略被称为伪答案改写（PAR）。
>
> 信息缩减：当查询包含过多细节时，对其进行核心内容提取以简化查询并突出重点，定义为核心内容提取（CCE）。  

[Link️](https://cubox.pro/web/annotations/cards/7271069011834571080?highlight=7271069011884901992)


---

## 📖 正文全文

# ICLR2025盲审论文DMQR-RAG：多样查询改写，查询P@5提升了14.46%，超过RAG-Fusion

[mp.weixin.qq.com](https://mp.weixin.qq.com/s/PQF8Ka5UPYxpnEASTUSs5w)cathy 机器人的脑电波


![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2F5icXlzGAkUYRpOSguVf2icj2XojGOxSPBL9xMiaQGlovqZgKnJ3X5K22vjH9vNAothC5leP5y0oWNfq0ib5icB8MXFQ%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26tp%3Dwebp%26wxfrom%3D5%26wx_lazy%3D1%26wx_co%3D1&valid=false)

论文： https://arxiv.org/abs/2411.13154


## 摘要

大型语言模型（LLMs）常面临静态知识和幻觉问题，这削弱了其可靠性。检索增强生成（RAG）通过融入外部信息，缓解了这些问题。然而，用户的查询通常包含噪音和意图偏差，必须通过查询改写来提升检索文档的相关性。

本文提出了DMQR-RAG，一种旨在提升RAG中文档检索和最终响应性能的多样化多查询改写框架。具体而言，研究了含有不同信息量的查询如何检索多样化的文档，并提出了四种改写策略，这些策略在不同信息层面上操作，从而改进基线方法的性能。

此外，还提出了一种自适应策略选择方法，该方法在尽量减少改写数量的情况下优化了整体性能。通过在学术和工业领域的大量实验验证，这些方法表现出显著的优越性。

## 方法

首先介绍了传统RAG工作流程，并提出了一个标准化设置以探索改写策略对性能的影响。在此基础上，提出了DMQR-RAG框架以及自适应改写选择方法。

## RAG流程中的多查询改写标准化设置

给定用户查询 ( q )，传统的RAG流程首先通过查询改写产生 ( q' )。随后，检索器搜索相关文档 ( D )，这些文档经过重新排名后成为 ( D' )。接着，选取前 ( K ) 个文档，与原始查询 ( q ) 一起输入LLM，生成最终响应 ( A )。其具体流程如下：

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2F5icXlzGAkUYRpOSguVf2icj2XojGOxSPBLjoAQmCQN24OicnD27l7pJKpHicoaxuKiaqrtDmxOcrtUcJ3hzupYibiaDEw%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26tp%3Dwebp%26wxfrom%3D5%26wx_lazy%3D1%26wx_co%3D1&valid=false)

为了评估改写模块的效果，而不受复杂RAG管道中其他可变因素的干扰，本文提出标准化设置，将检索器和重排模块统一为主流方法，例如使用Bing搜索引擎作为检索器以确保数据的时效性，以及采用广泛应用的BAAI-BGE重排器。

## 多样化多查询改写框架

鉴于LLMs在自然语言理解方面的先进能力，多数用于查询改写。但当前方法往往生成单一改写结果，缺乏多样性，限制了改进潜力。本文设计的有效多查询改写应满足以下信息准则：每个改写结果都应多样化，提供其他改写中未包含的独特信息，从而最大化检索相关文档的覆盖率。

### 改写策略

为了提升检索文档的多样性，同时考虑到用户查询可能存在的信息噪音或冗余问题，本文提出四种改写策略：

1. **信息等同** ：改写的目标是消除用户查询中的噪音并精炼查询。具体实现为**通用查询改写（GQR）** 和**关键词提取改写（KWR）** ，分别通过保留原始查询中的关键信息或直接提取关键词来提升检索精度。

2. **信息扩展** ：通过整合LLMs的先验知识生成伪答案，使查询扩展更多信息；该策略被称为**伪答案改写（PAR）** 。

3. **信息缩减** ：当查询包含过多细节时，对其进行核心内容提取以简化查询并突出重点，定义为**核心内容提取（CCE）** 。

上述策略形成了一个动态扩展的策略池：

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2F5icXlzGAkUYRpOSguVf2icj2XojGOxSPBLjRsCuoR1ibX3hiaj7eMmpIoljhCG2R3zXia7L2VguCFu85zKoAEiaBqHmA%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26tp%3Dwebp%26wxfrom%3D5%26wx_lazy%3D1%26wx_co%3D1&valid=false)

可根据具体需求灵活引入新策略，如跨跳查询的子查询改写，以及结合训练性方法提升效果。

自适应策略选择

虽然多查询重写可以增强检索的多样性，但对每个查询应用固定策略集并不是最优的。因此，至关重要的是根据每个特定查询动态选择重写策略，生成最符合原始意图的多个重写查询。

我们通过轻量级提示和few shoot实现这种选择方法。具体来说，我们将重写策略池 RS 中的策略描述纳入大型语言模型（LLMs）的提示中作为上下文信息。这些描述概述了适用的查询类型和每种策略的作用，使 LLMs 能够全面了解所有可用的重写策略。为了在具有挑战性的情况下增强策略选择，我们还采用了few shoot方法，通过向 LLMs 提供多个示例，帮助它们为困难的查询选择合适的重写策略。参考prompt如下所示


    ### Instruction ###You will receive a user's question that requires retrieving relevant contentthrough internet search to provide an answer. There are now the following{N} rewriting methods, {RS name list}. Based on the characteristics of thequery, please select some of the rewriting methods to rewrite the question.### {RSi name} ###{RSi description}. . .### Guidelines ###{RSi name}: {RSi usage guideline}. . .### Output Format ###Each output line should list the selected rewriting method, starting with itsname followed by the rewritten result.The final line should explain the selection rationale for these methods and theexclusion of others, beginning with "reason: ".### Example ###Question: {example query}Output:{RSj name}: {Rewriting result based on RSj }{RSk name}: {Rewriting result based on RSk}reason: {the rationale for selecting these methods over others}Begin! Only output the final result without any additional content. Do notgenerate any other unrelated content.Question: {query}Output:


## 实验与评估

通过将自适应策略选择方法嵌入上述改写框架中，本文采用轻量化提示及小样本学习实现。具体来说，基于查询类型动态选择适合的策略，为每个查询生成最优改写结果。同时，根据工业界和学术界的实际应用场景，通过全面实验验证了该框架的有效性。

实验设置

进行了实验，使用三个具有代表性的开放域问答数据集：

1. **AmbigNQ：用于解决自然问题中固有的歧义性；**
2. **HotpotQA：包含需要多跳推理的复杂性问题，使用验证集进行评估；**
3. **FreshQA：动态基准测试数据集，涵盖多种问题类型，并需最新世界知识来提供准确答案。**

此外，还在工业数据集上进行了实验。

### 评价指标

采用了检索和端到端响应的相关指标进行评估：

*
  检索性能：利用 GPT-4 评估检索文档的Top-5命中率（H@5）和精度（P@5）。
*
  端到端性能：对于 HotpotQA 和 AmbigNQ 数据集，计算 EM 和 F1 分数；对于 FreshQA，利用 GPT-4 对响应进行评分并计算准确率（Acc）。

## 基线方法

采用以下方法作为基线：

1. **提示式方法** :

   *
     LLM Rewrite（重写），通过提示结合大语言模型生成通用检索重写。
   *
     Hyde，通过生成伪文档嵌入目标文档语义后进行检索。
2. **微调方法** :

   *
     Rewrite-Retrieve-Read (RRR)，使用检索后模型响应的准确性作为奖励信号，微调T5模型。
   *
     RQ-RAG，构建跨多查询的检索数据集。

此外，还进行了原始查询直接检索（Original Query Retrieval，OQR）的比较。

### 实现细节

实验基于 PyTorch，使用了多个LLM的改写任务，展示 DMQR-RAG 框架在 Llama3-8B、Qwen2-7B 和 GPT-4 等模型上的适用性。生成多种改写后，检索和回答生成基于 Bing 检索器，并使用 BGE 模型作为重新排名器。Top-5重新排名的文档作为附加上下文提供给响应模型（GPT-4）。

## 实验结果

### 基线比较

实验结果显示，所提方法在大多数场景下表现优于其他方法。

1. **原始查询的有效性** ：在某些场景，基线方法（如 RRR、Hyde 等）表现不如 OQR。这证明了原始查询在某些情况下能够准确表达用户意图，为检索和端到端响应提供宝贵的上下文。这一发现也验证了将原始查询与改写版本结合的策略池设计的合理性。

2. **多查询改写优于单查询改写** ：在所有数据集上，DMQR-RAG 在文档检索方面表现优越。特别是在 FreshQA 上，比最佳基线 P@5 提升了 14.46%。对于复杂多跳问题（如 HotpotQA），P@5 提升了约 8%。在端到端响应方面，DMQR-RAG 在 AmbigNQ 数据集上超越了 Hyde，实现了 EM 和 F1 分数分别提升 1.30% 和 3.74%。对于 FreshQA 数据集，准确率比 Rewrite 提高了 5.84%。

3. **超越 RAG-Fusion** ：与 RAG-Fusion 方法相比，DMQR-RAG 通过基于信息的多查询改写展示了更加优异的性能，在 AmbigNQ 数据集的 P@5 上有约 10% 的提升。

### 泛化性测试

实验测试了 DMQR-RAG 是否适用于其他LLMs，特别是比 GPT-4 更小的模型。测试结果显示，在 Llama3-8B 和 Qwen2-7B 模型上也能有效运行，显示了方法的通用性和适用性。

### 消融研究

研究每种改写方法的贡献，结果显示：

1. **PAR 方法贡献最大** ：通过 P@5 的平均减少1.34%，表明伪答案与其他改写方法显著不同，扩展了可用信息，从而增强了检索多样性。

2. **GQR 方法对相对明确的查询贡献较小** ：尽管如此，其在含噪或不清晰的用户查询场景中仍然有显著作用。

3. **无需对所有方法一视同仁** ：在 FreshQA 数据集上，删除任何方法可能提高特定指标，如 H@5 和 Acc。这表明应动态选择适合每个查询的改写方法以减少噪声并提升性能。

### 自适应改写选择评估

采用了自适应改写选择方法，在 FreshQA 数据集上测试了 Llama3-8B 和 GPT-4 的改写器。

1. **改写数量减少** ：动态选择后，平均改写次数从4次减少至约2.48次，呈高斯分布，这验证了方法的有效性。

2. **检索和回答性能提升** ：动态选择可有效减少检索到的噪声文档，提高相关文档的比例。此外，性能提升在 Llama3-8B 上更为显著，其准确率提高了 2.17%，而 GPT-4 为 0.66%。

### 工业应用

在实际应用场景中使用 DMQR-RAG，根据15,000,000名在线用户的查询进行了测试。实验表明：

1.
   检索性能显著提升：H@5 平均提升 2.0%，P@5 提升 10.0%。
2.
   端到端响应的正确性和相关性指标有所改善。

### 案例分析

通过复杂和简短查询的案例进行分析：

1. **复杂查询** ：RRR 尽管删除了无关信息，但生成的查询仍过于复杂；而 KWR 和 CCE 策略显著简化了查询，同时保留了核心信息，从而有效检索到相关文档。

2.
   简短查询：PAR生成的伪答案与真实答案语义对齐，成功提升检索效果。

## 结论

本文介绍了多样化多查询改写框架（DMQR-RAG），旨在通过提升文档多样性和覆盖率改进检索增强生成（RAG）的性能。设计了基于信息层次的四种改写策略，确保改写后的查询具有多样性并提供独特的见解。此外，本文还提出了一种自适应改写选择方法，该方法利用轻量化提示和少样本学习实现动态策略选择。

在学术和工业数据集上的评估表明，多查询改写通常优于单一查询改写，而DMQR-RAG在多数场景下超过了传统RAG-Fusion方法。消融研究和案例分析进一步证明了基于查询特性的改写策略选择的重要性，验证了所提方法的有效性。

未来研究方向包括：优化自适应改写选择方法，扩展改写策略池的范围，以创造出更加丰富的策略集合，从而进一步提升检索和生成能力。


[Read in Cubox](https://cubox.pro/web/card/7271069011834571080)
