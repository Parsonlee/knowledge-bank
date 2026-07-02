---
id: "7249425525721008430"
cubox_url: https://cubox.pro/web/card/7249425525721008430
url: https://mp.weixin.qq.com/s/gUyFlIzToUT-fcs8t67j1Q
tags:
  - RAG
  - RAG/chunking
---
# RAG文本切分的第四个层次，基于向量模型的语义切分

本篇文章开始，我们将介绍第四层级的内容语义切分；​本篇文章将介绍基于向量模型的语义切分。

[Read in Cubox](https://cubox.pro/web/card/7249425525721008430)  
[Read Original](https://mp.weixin.qq.com/s/gUyFlIzToUT-fcs8t67j1Q)  

---

\## Annotations  

> 这个 切分器 的工作原理是确定何时分隔句子。这是通过查找任意两个句子之间的向量差异来完成的。当该差异超过某个阈值时，它们将被拆分。  

[Link️](https://cubox.pro/web/annotations/cards/7249425525721008430?highlight=7249425525771340594)  

> 梯度
>
> 在这种方法中，距离的梯度与百分位数方法一起用于分割块。当块彼此高度相关或特定于某个领域时，此方法非常有用。这个想法是在梯度数组上应用异常检测，使分布变得更宽，并且易于识别高度语义数据中的边界。  

[Link️](https://cubox.pro/web/annotations/cards/7249425525721008430?highlight=7249426110423762162)


---

\## 📖 正文全文

# RAG文本切分的第四个层次，基于向量模型的语义切分

[mp.weixin.qq.com](https://mp.weixin.qq.com/s/gUyFlIzToUT-fcs8t67j1Q)哎呀AIYA 哎呀AIYA


之前的文章提到，我们将文本切分划分为五个层级，并介绍了前三个层级的实现和一些基础知识。本篇文章开始，我们将介绍第四层级的内容语义切分；本篇文章将介绍基于向量模型的语义切分。

文本切分五个层级：

* **Level 1: [Character Splitting](http://mp.weixin.qq.com/s?__biz=Mzk0NTcyNTMzNw==&mid=2247483951&idx=1&sn=61c25be0edab945c7b34980ec7dd98de&chksm=c31048d9f467c1cf1f4323b52a568af63f0086359385f77a8464b1b717ea65ee18ebd181d6f4&scene=21\#wechat_redirect)** - 简单的字符长度切分

* **Level 2: [Recursive Character Text Splitting](http://mp.weixin.qq.com/s?__biz=Mzk0NTcyNTMzNw==&mid=2247483959&idx=1&sn=8805bfc48c02cc396042eed5ad5f440a&chksm=c31048c1f467c1d734fba7253411119c5b65b39319cb5bb73681f6dd4ceb2b4d822d2d0bc9c3&scene=21\#wechat_redirect)** - 通过分隔符切分，然后递归合并

* **Level 3: [Document Specific Splitting](http://mp.weixin.qq.com/s?__biz=Mzk0NTcyNTMzNw==&mid=2247483975&idx=1&sn=c2de67cc8dcb53986ccfaed03547bab6&chksm=c31048b1f467c1a77ad27d3e8c6b549844f927a3523a0b385e2bde82c01a3886cf34103b5fdb&scene=21\#wechat_redirect)** - 针对不同文档格式切分 (PDF, Python, Markdown)

* **Level 4: Semantic Splitting** - 语义切分

* **Level 5: Agentic Splitting**-使用代理实现自动切分

这个 切分器 的工作原理是确定何时分隔句子。这是通过查找任意两个句子之间的向量差异来完成的。当该差异超过某个阈值时，它们将被拆分。后面演示它是怎么实现的：

搭建语义切分流程

**数据加载**

* 
* 
* 

    # This is a long document we can split up.with open("state_of_the_union.txt") as f:    state_of_the_union = f.read()


**创建拆分器**

要实例化 SemanticChunker，我们必须指定一个嵌入模型。下面我们将使用 OpenAIEmbeddings，也可以使用[自己的模型](http://mp.weixin.qq.com/s?__biz=Mzk0NTcyNTMzNw==&mid=2247483767&idx=1&sn=17c63b3aa0ed6545d57a76bcec61b3f3&chksm=c3104b81f467c297a859c3e62510417d3c6419057fab3de3c26f518c69884ed7a8f316a22e6f&scene=21\#wechat_redirect)。

* 
* 
* 
* 

    from langchain_experimental.text_splitter import SemanticChunkerfrom langchain_openai.embeddings import OpenAIEmbeddings
    text_splitter = SemanticChunker(OpenAIEmbeddings())


**拆分文本**

* 
* 

    docs = text_splitter.create_documents([state_of_the_union])print(docs[0].page_content)


这样我们就完成了基于向量的语义切分；下面介绍其参数控制：

切分的几种形式

在切分的过程中，我们怎么控制切分的粒度？有几种方法可以确定该阈值是什么？这些方法可以由kwarg的breakpoint_threshold_type控制。


**百分比**

默认的拆分方式是基于百分位数。在这种方法中，计算句子之间的所有差异，然后拆分任何大于 X 百分位数的差异。


* 
* 
* 
* 
* 

    text_splitter = SemanticChunker(             OpenAIEmbeddings(),             breakpoint_threshold_type="percentile")docs = text_splitter.create_documents([state_of_the_union])print(docs[0].page_content)


* 

    print(len(docs))


* 

    # 26


**标准差**

在此方法中，任何大于 X 个标准差的差值都将被拆分。


* 
* 
* 
* 
* 

    text_splitter = SemanticChunker(             OpenAIEmbeddings(),             breakpoint_threshold_type="standard_deviation")docs = text_splitter.create_documents([state_of_the_union])print(docs[0].page_content)


* 

    print(len(docs))


* 

    # 4


**四分位距**

在这种方法中，四分位数距离用于分割块。


* 
* 
* 
* 
* 

    text_splitter = SemanticChunker(           OpenAIEmbeddings(),           breakpoint_threshold_type="interquartile")docs = text_splitter.create_documents([state_of_the_union])print(docs[0].page_content)


* 

    print(len(docs))


* 

    # 25


**梯度**

在这种方法中，距离的梯度与百分位数方法一起用于分割块。当块彼此高度相关或特定于某个领域时，此方法非常有用。这个想法是在梯度数组上应用异常检测，使分布变得更宽，并且易于识别高度语义数据中的边界。


* 
* 
* 
* 
* 

    text_splitter = SemanticChunker(             OpenAIEmbeddings(),             breakpoint_threshold_type="gradient")docs = text_splitter.create_documents([state_of_the_union])print(docs[0].page_content)


* 

    print(len(docs))


* 

    26


以上介绍了langchain基于向量的语义切分实现，后续将介绍具体的算法实现和其它语义切分方式，敬请期待。

如果对内容有什么疑问和建议可以私信和留言，也可以添加我加入大模型交流群，一起讨论大模型在创作、RAG和agent中的应用。  

好了，这就是我今天想分享的内容。如果你对大模型应用感兴趣，别忘了点赞、关注噢\~


往期推荐


[RAG数据集自动构造探索, 附PROMPT](http://mp.weixin.qq.com/s?__biz=Mzk0NTcyNTMzNw==&mid=2247484090&idx=1&sn=61361b4553028f4e584f88793ea861ee&chksm=c310484cf467c15af6030f899f3c3e44f96ce511a2d49fe0e2d18dbab0bf77293e2b174bb000&scene=21\#wechat_redirect)  


[支持大模型流式输出的JSON提取工具](http://mp.weixin.qq.com/s?__biz=Mzk0NTcyNTMzNw==&mid=2247483821&idx=1&sn=6f34d91291fbcab03a79142eaa3ed56f&chksm=c3104b5bf467c24d7c4184784831d2cab8ce97f47cfc86d40da172650e67dba9a0860a7411b0&scene=21\#wechat_redirect)  


[高级 RAG实战：召回更好的片段Query扩展](http://mp.weixin.qq.com/s?__biz=Mzk0NTcyNTMzNw==&mid=2247484014&idx=1&sn=c50328bcf4e970150d36a0435ba8c72d&chksm=c3104898f467c18e5effdbc5b82ddc12f6bdb3848871a353605f1702c1639c8a7a2327da923e&scene=21\#wechat_redirect)

[RAG：Langchain中使用自己的LLM大模型](http://mp.weixin.qq.com/s?__biz=Mzk0NTcyNTMzNw==&mid=2247483750&idx=1&sn=776d59a1d9b95ceda8e7d99a94014c20&chksm=c3104b90f467c28643c5d49cfb8c960cb51e9f4a48e368fec0bea9a7c7cc2089f246b65a2804&scene=21\#wechat_redirect)

[Read in Cubox](https://cubox.pro/web/card/7249425525721008430)
