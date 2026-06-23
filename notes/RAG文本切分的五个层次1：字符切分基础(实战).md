# RAG文本切分的五个层次1：字符切分基础(实战)

[mp.weixin.qq.com](https://mp.weixin.qq.com/s/SnfhuQyRmjQxDP3n5n3Upw)哎呀AIYA 哎呀AIYA


在大模型应用中，时常会出现由于知识库参考内容过多或者长期记忆的内容过长，导致输入模型的成本过高或者超出模型的承载长度。该怎么办呢？

提高语言模型应用程序性能的最有效策略之一是将大数据分成较小的部分。后面的一系列分享将介绍文本切分的一些概念、方法和实战；会涉及很多内容，但如果你能坚持到最后，保证你会对分块理论有一个扎实的掌握。

我们将文本切分定义为五个层级：

* **Level 1: Character Splitting** - 简单的字符长度切分

* **Level 2: Recursive Character Text Splitting** - 通过分隔符切分，然后递归合并

* **Level 3: Document Specific Splitting** - 针对不同文档格式切分 (PDF, Python, Markdown)

* **Level 4: Semantic Splitting** - 语义切分

* **Level 5: Agentic Splitting**-使用代理实现自动切分

本篇文章将介绍字符切分的概念和实现。虽然简单，但有助于我们理解一些参数和整体概念。

字符切分概念

字符分割是分割文本的最基本形式。它是简单地将文本分成n个字符大小的块的过程，而不考虑其内容或形式。

不建议在任何应用程序中使用这种方法，但它是我们理解基础知识的一个很好的起点。

* 优点:简单容易

* 缺点:非常死板，没有考虑到文本的结构

**两个小概念:**

**Chunk Size**(块大小)-块中包含的字符数量。50、100、10万等等。

**Chunk Overlap** (块重叠)-为了避免重要信息被切开成多个部分，希望有连续块重叠，overlap就是重叠块的大小。

下面看个例子，来看看字符切分逻辑：  

* 
* 
* 
* 
* 
* 
* 
* 
* 

    text = "2024年一季度公司实现营业收入24.56亿元（-12.60%），实现归母净利润19.54亿元（-3.70%），扣非后归母净利润19.37亿元（+2.38%），基本每股收益0.12元，（-3.36%）。"
    chunks = []chunk_size = 35
    for i in range(0, len(text), chunk_size):    chunk = text[i:i + chunk_size]  # 每隔35是一个块    chunks.append(chunk)print(chunks)


在实际工程使用中，我们都不是孤立的切分文本，而是对文档进行切分，下面我们使用langchain和llama_index来演示这个过程。  

LangChain实现

### **导入模块：**


* 

    from langchain.text_splitter import CharacterTextSplitter


**切分文档**

上面text内容按35个字符被切分成多个片段了：  


* 
* 
* 

    text_splitter = CharacterTextSplitter(chunk_size=35, chunk_overlap=0, separator='', strip_whitespace=False)print(text_splitter.split_text(text))


**加入overlap**

通过加入overlap，我们可以发现下面的：%），实现，母净利润1 在两个片段中出现了。

* 
* 
* 
* 

    text_splitter = CharacterTextSplitter(chunk_size=35, chunk_overlap=5, separator='', strip_whitespace=False)st = text_splitter.split_text(text)pprint(st)


**加入separator**

先利用separator将文档切分成小块，再使用长度对小块进行切割：

* 
* 
* 

    text_splitter = CharacterTextSplitter(chunk_size=35, chunk_overlap=0, separator='，', strip_whitespace=False)print(text_splitter.split_text(text))


LLama-Index实现

### **加载依赖模块**


* 
* 

    from llama_index.core.text_splitter import SentenceSplitterfrom llama_index.core import SimpleDirectoryReader


**构建切分器**

* 
* 
* 
* 

    splitter = SentenceSplitter(    chunk_size=200,    chunk_overlap=15,)


**加载文档**

* 
* 
* 

    documents = SimpleDirectoryReader(    input_files=["./test.txt"]).load_data()


**切分文档**

* 

    nodes = splitter.get_nodes_from_documents(documents)


nodes里面不仅包含了切分的文本信息，也包含了很多额外的相关内容。可以去探索...  

至此，你已经学会了字符切分的全部概念和实战，让我们下篇继续吧。

如果对内容有什么疑问和建议可以私信和留言，也可以添加我加入大模型交流群，一起讨论大模型在创作、RAG和agent中的应用。

好了，这就是我今天想分享的内容。如果你对大模型应用感兴趣，别忘了点赞、关注噢\~


往期推荐


[RAG：Langchain中使用自己的LLM大模型](http://mp.weixin.qq.com/s?__biz=Mzk0NTcyNTMzNw==&mid=2247483750&idx=1&sn=776d59a1d9b95ceda8e7d99a94014c20&chksm=c3104b90f467c28643c5d49cfb8c960cb51e9f4a48e368fec0bea9a7c7cc2089f246b65a2804&scene=21#wechat_redirect)


[](https://mp.weixin.qq.com/s?__biz=MzI0MjYwNTUyMw==&mid=2247484227&idx=1&sn=57de0d20b27be9a273f6418875360fa3&chksm=e9788fffde0f06e930d951763f03e52b8cf392b164ea00b5b0a1112e6572fe9bfebc53933195&scene=21#wechat_redirect)[一款约束大模型结构化输出的开源工具，后处理不存在了提速又提质！(实战)](http://mp.weixin.qq.com/s?__biz=Mzk0NTcyNTMzNw==&mid=2247483887&idx=1&sn=1304cc26fe5269d402207d0acedca368&chksm=c3104b19f467c20fb59e80bffbc8b24dfee79494017a94a6aa8a3cbf019f707557c7979dbc40&scene=21#wechat_redirect)  


[支持大模型流式输出的JSON提取工具](http://mp.weixin.qq.com/s?__biz=Mzk0NTcyNTMzNw==&mid=2247483821&idx=1&sn=6f34d91291fbcab03a79142eaa3ed56f&chksm=c3104b5bf467c24d7c4184784831d2cab8ce97f47cfc86d40da172650e67dba9a0860a7411b0&scene=21#wechat_redirect)

[一文读懂token到底是什么鬼，消耗那么多钱？](http://mp.weixin.qq.com/s?__biz=Mzk0NTcyNTMzNw==&mid=2247483676&idx=1&sn=34ff4199b3506d29bd2ceb38adc11093&chksm=c3104beaf467c2fc6406daecf514cd9ecc0e1ae5fff6007b370ff1ae1224484796967b48cd6f&scene=21#wechat_redirect)

[Read in Cubox](https://cubox.pro/web/card/7246422148867165245)
