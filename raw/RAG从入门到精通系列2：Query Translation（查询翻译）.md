---
id: "7281569961389065093"
cubox_url: https://cubox.pro/web/card/7281569961389065093
url: https://mp.weixin.qq.com/s/8aUzRjpO5ve0C5ndhgI6ng
tags:
  - RAG
  - RAG/query
---
# RAG从入门到精通系列2：Query Translation（查询翻译）

Multi-query: 生成多个类似query；
RAG fusion: 针对检索到的doc进行过滤；
decomposition: 分解，递归求解
step-back: 生成一个更概括性的问题，检索更大的信息回答问题

[Read in Cubox](https://cubox.pro/web/card/7281569961389065093)  
[Read Original](https://mp.weixin.qq.com/s/8aUzRjpO5ve0C5ndhgI6ng)  

---


---

## 📖 正文全文

# RAG从入门到精通系列2：Query Translation（查询翻译）

[mp.weixin.qq.com](https://mp.weixin.qq.com/s/8aUzRjpO5ve0C5ndhgI6ng)南七无名式 PyTorch研习社


LLM（Large Language Model，大型语言模型）是一个功能强大的新平台，但它们并不总是使用与我们的任务相关的数据或者是最新的数据进行训练。

RAG（Retrieval Augmented Generation，检索增强生成）是一种将 LLM 与外部数据源（例如私有数据或最新数据）连接的通用方法。它允许 LLM 使用外部数据来生成其输出。

要想真正掌握 RAG，我们需要学习下图所示的技术（技巧）：

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2FSaeK9tW7Bu8bchx6XOFHAkoCAVrOh1N5MycECIYib1InAKy7T6ibI91aWzkGOToGVIaFmnJp8NUkRTfcX3PA3Wlw%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26tp%3Dwebp%26wxfrom%3D5%26wx_lazy%3D1%26wx_co%3D1&valid=false)

在《[RAG从入门到精通系列1：基础RAG](https://mp.weixin.qq.com/s?__biz=MzI2ODUyMTQyNA==&mid=2247495255&idx=1&sn=562e184d49d101f7be545b412a236e46&scene=21#wechat_redirect)》一文我已经介绍了基础的 RAG 部分：**Indexing** （索引）、**Retrieval** （检索）和 **Generation** （生成）。

在机器学习领域有一句经典的话：Garbage in，Garbage out

这句话也是适合于 RAG，因为我们现在检索的原理就是根据用户的 Query（也就是 Question）的语义去检索相关的文档。  

但是我们不能指望所有的用户都能清楚地描述自己的 Query，如果用户写了一句模棱两可的 Query 或者是一个复杂的 Query，那么检索到的文档也将是模棱两可或者难以准确检索，进而导致 LLM 的回答就不准确：

在这篇文章中我将介绍 RAG 的高阶技巧：**Query Translation**（查询翻译）：

更具体地，我们将学习 Re-written（改写）、Step-back question（优化问题）和 sub-question（分解问题）这三种 Query Translation 方法，进而提升检索和生成的效果。


**Re-written**


Re-written 是指对原始查询进行语义重写，保持核心意思不变，但调整语言表述，使得问题更易被知识库或检索系统处理。

我们将原始 Question 改写成三种表述方式 Q1、Q2 和 Q3，然后分别检索与这三种问题相关的文档：

**应用场景**：

* 原始问题语言模糊或表述不清。

* 需要通过不同的表述来优化检索匹配。

**示例**：

* 原始问题：*"Python 的用法？"*

* Re-written：*"Python 编程语言的常见使用场景是什么？"*

* 效果：改写后的问题更具体，更容易检索到高质量答案。

**常见方法**：

1. **Multi-Query**：在检索阶段针对同一个问题生成多个不同的查询，通过这些查询去检索知识库，以获得更全面或相关的文档集合。

2. **RAG Fusion**：一种在生成阶段融合检索结果的策略。它关注的是如何从多个检索到的文档中综合信息，以生成高质量的回答。

**优点**：

* 增强了检索系统对问题的理解能力。

* 提高了检索结果的相关性。

**挑战**：

* 如何保持改写问题与原始问题的语义一致性。

* 避免引入偏差或歧义。

**1. Multi-Query**

首先我们准备一个 Prompt，让 LLM 将原始问题转写成 5 个不同表述方式的问题：

接下来就是分别检索与这 5 个问题相关的文档，并把这些文档去重之后组织在一起：

最后我们将上述拆分问题的链和检索链串起来形成最终的 RAG 管道，我们还引入了新的 Prompt：

**2. RAG Fusion**

这个过程与 Multi-Query 很相似，但是对检索到的多篇文档进行筛选过滤之后再输入 LLM：  

我们先写一个 Prompt：根据原始问题生成 4 个相关的问题：

这里我将实现一个简单的 Reciprocal Rank Fusion (RRF) 检索过滤方法：

最终的 RAG 管道：


**Decomposition**


也就是 sub-question，是将复杂的问题拆解为多个独立的子问题，每个子问题可以单独处理。最终通过聚合子问题的答案来生成完整的回答。

**应用场景**：

* 多跳问题（需要跨多个知识点回答）。

* 包含逻辑操作或条件限制的问题。

**示例**：

* 原始问题：*"诺贝尔奖得主中，谁既是科学家又是文学家？"*

* Sub-question：

  1. "诺贝尔奖得主中有哪些科学家？"

  2. "诺贝尔奖得主中有哪些文学家？"

  3. "有哪些人既是科学家又是文学家？"

* 效果：通过独立回答每个子问题，最终整合得到准确的答案。

**方法**：

* **逻辑分解**：基于问题中的逻辑关系（如"且"、"或"）。

* **多跳分解**：根据问题需要跨越的知识领域，逐步深入。

**优点**：

* 减少了问题的复杂性，提高了检索和生成的准确率。

* 提供了更清晰的推理过程，便于调试和分析。

**挑战**：

* 分解的子问题可能存在相互依赖关系，需要设计合理的顺序。

* 子问题答案的整合可能存在冲突或不一致。

**Sub-question 流程一**  

类似于"递归求解"：用前一个子问题答案结合下一个子问题检索到的文档来生成下一个子问题的答案。

首先，设定 Prompt：

然后就是完整的 RAG 管道：  

**Sub-question 流程二**

先得到每个子问题的答案，然后集中汇总得到最终答案。

分别获得每个子问题的答案：

汇总答案：


**Step-back Question**


在检索和回答过程中，当系统意识到当前的问题太具体或难以直接回答时，退一步改问一个更广泛、更概括性的问题，从而获取更大的上下文信息。

**应用场景**：

* 当前查询太具体，无法直接匹配知识库内容。

* 检索结果中没有足够的信息来回答原始问题。

**示例**：

* 原始问题：*"爱因斯坦在 1921 年诺贝尔奖颁奖仪式上的具体演讲内容是什么？"*

* Step-back Question：*"爱因斯坦为什么获得 1921 年诺贝尔奖？"*

* 效果：通过回答更概括的问题，间接获取相关的上下文信息，为后续回答具体问题提供支持。

**优点**：

* 提高了检索的召回率和上下文覆盖率。

* 适用于数据稀疏或回答难度较高的场景。

**挑战**：

* 如何自动判断何时需要"退一步"？

* 退回的问题是否仍能与原始问题保持语义相关性。

我们首先需要提供 few-shot example 给 LLM，使 LLM 知道如何修改原始问题：

效果如下：

完整的 RAG 管道：


**HyDE**


HyDE（Hypothetical Document Embedding） 是一种用于 Query Translation 的创新方法，特别适用于 RAG 系统中的复杂问题处理。HyDE 的核心思想是通过生成"假设文档"（Hypothetical Document），将查询从抽象的自然语言问题转化为检索系统能够高效处理的表示。

以下是 HyDE 的典型流程：

1. **输入问题**：用户输入一个自然语言问题，如：

   * *"哪个国家首次成功发射了人造卫星？"*

2. **生成假设文档**：

   * *"第一个成功发射人造卫星的国家是苏联，他们在 1957 年发射了 Sputnik 1。"*

   <!-- -->

   * 使用语言模型（如 GPT）生成一个可能的回答，假设内容可能是：

   * 这一步提供了一个强语义上下文的假设答案，即使生成的假设答案可能并不完全正确。

3. **检索相关文档**：

   * 将生成的假设文档嵌入向量空间或提取关键词，作为检索系统的输入，搜索知识库中与其最相关的文档。

4. **生成最终答案**：

   * 将检索到的文档和原始问题结合，通过生成模型生成最终的回答。

HyDE 的做法是：

1. **生成假设文档**：使用生成模型（如 GPT）对输入问题生成一个假设答案，作为问题可能的语义扩展。

2. **检索相关文档** ：将生成的假设文档作为输入，通过嵌入匹配或关键词匹配的方式，检索知识库中的相关文档。

3. **整合检索结果** ：结合原始查询和检索到的相关文档，生成最终的回答。


**Prompt 的威力**


不管是 Re-written、Decomposition 还是 Step-back Question，这些都借助了强大的 Prompt。

也许你的英文不太好，而我们的资料库又都是英文，所以我可以建一个翻译 Chain：将用户的中文问题先翻译成英文。

然后再要求 LLM 用中文回答问题：  


**GitHub 链接：**

https://github.com/realyinchen/RAG/blob/main/02_Query_Translation.ipynb  

文章来源：PyTorch研习社


[Read in Cubox](https://cubox.pro/web/card/7281569961389065093)
