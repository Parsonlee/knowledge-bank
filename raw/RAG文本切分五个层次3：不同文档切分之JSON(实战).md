---
id: "7246426759866875976"
cubox_url: https://cubox.pro/web/card/7246426759866875976
url: https://mp.weixin.qq.com/s?__biz=Mzk0NTcyNTMzNw==&mid=2247483975&idx=1&sn=c2de67cc8dcb53986ccfaed03547bab6&chksm=c31048b1f467c1a77ad27d3e8c6b549844f927a3523a0b385e2bde82c01a3886cf34103b5fdb&cur_album_id=3583314836786053132&scene=189
tags:
  - RAG
  - RAG/chunking
---
# RAG文本切分五个层次3：不同文档切分之JSON(实战)

前面文章提到，我们将文本切分划分为五个层级，并介绍了前两个层级的实现和一些基础知识。

[Read in Cubox](https://cubox.pro/web/card/7246426759866875976)  
[Read Original](https://mp.weixin.qq.com/s?__biz=Mzk0NTcyNTMzNw==&mid=2247483975&idx=1&sn=c2de67cc8dcb53986ccfaed03547bab6&chksm=c31048b1f467c1a77ad27d3e8c6b549844f927a3523a0b385e2bde82c01a3886cf34103b5fdb&cur_album_id=3583314836786053132&scene=189)  

---


---

\## 📖 正文全文

# RAG文本切分五个层次3：不同文档切分之JSON(实战)

[mp.weixin.qq.com](https://mp.weixin.qq.com/s?__biz=Mzk0NTcyNTMzNw==&mid=2247483975&idx=1&sn=c2de67cc8dcb53986ccfaed03547bab6&chksm=c31048b1f467c1a77ad27d3e8c6b549844f927a3523a0b385e2bde82c01a3886cf34103b5fdb&cur_album_id=3583314836786053132&scene=189)哎呀AIYA 哎呀AIYA


前面文章提到，我们将文本切分划分为五个层级，并介绍了前两个层级的实现和一些基础知识。本篇文章开始，我们将介绍第三个层级的内容，基于文档结构的切分，这个级别是关于让我们的分块策略适合不同的数据格式。

文本切分五个层级：

* **Level 1: [Character Splitting](http://mp.weixin.qq.com/s?__biz=Mzk0NTcyNTMzNw==&mid=2247483951&idx=1&sn=61c25be0edab945c7b34980ec7dd98de&chksm=c31048d9f467c1cf1f4323b52a568af63f0086359385f77a8464b1b717ea65ee18ebd181d6f4&scene=21\#wechat_redirect)** - 简单的字符长度切分

* **Level 2: [Recursive Character Text Splitting](http://mp.weixin.qq.com/s?__biz=Mzk0NTcyNTMzNw==&mid=2247483959&idx=1&sn=8805bfc48c02cc396042eed5ad5f440a&chksm=c31048c1f467c1d734fba7253411119c5b65b39319cb5bb73681f6dd4ceb2b4d822d2d0bc9c3&scene=21\#wechat_redirect)** - 通过分隔符切分，然后递归合并

* **Level 3: Document Specific Splitting** - 针对不同文档格式切分 (PDF, Python, Markdown)

* **Level 4: Semantic Splitting** - 语义切分

* **Level 5: Agentic Splitting**-使用代理实现自动切分

我们在日常数据处理中，不仅仅有txt数据，还包含一些存在结构的数据，例如json、markdown、代码(例如py)、PDF等。今天让我们看看如何处理JSON数据，后续将挑重点介绍。

langchain实现

**切分逻辑**

首先遍历json数据深度，然后构建更小的json块。试图保持嵌套json对象的完整，但在需要的时候会将它们分开，以保持块的大小在min_chunk_size和max_chunk_size之间。

如果值不是一个嵌套的json，而是一个非常大的字符串，那么字符串将不会被分割。如果您需要对块大小进行硬性限制，请考虑在这些块上使用递归文本分配器来组合它。拆分列表有一个可选的预处理步骤，首先将它们转换为json (dict)，然后拆分它们。

**加载测试数据**

* 
* 
* 
* 
* 

    import requestsfrom pprint import pprint
    # This is a large nested json object and will be loaded as a python dictjson_data = requests.get("https://api.smith.langchain.com/openapi.json").json()


![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2Fr8c4hf2wliabAPMiaAiaNJaZRIApME0EhbTQSgkrCeGxznicROKLsBIXYFfOaoQ2QgvvRBib8PTE12LP6IODJRcElEQ%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26tp%3Dwebp%26wxfrom%3D5%26wx_lazy%3D1%26wx_co%3D1&valid=false)

加载后的json_data是一个很大的json文件，我们看看怎么切分它：  


**定义切分器**

* 
* 
* 
* 

    from langchain_text_splitters import RecursiveJsonSplitter
    splitter = RecursiveJsonSplitter(max_chunk_size=300)# 还可以设置min_chunk_size


**切分文档**

* 

    json_chunks = splitter.split_json(json_data=json_data)


可以看出按最内层进行了分割，paths的每一条，被分割成了多条。

**列表切分**

当json里面有一个大列表时，按上述方法会完整保留，这样就会导致片段的长度超长。怎么解决这个问题呢？我们可以指定convert_lists=True来预处理json，将列表内容转换为index:item作为key:val对的字典:

* 

    json_chunks = splitter.split_json(json_data=json_data, convert_lists=True)


可以看到，在存在列表的位置，将列表转化为了dict，key为元素所在的位置。langchain中的实现，我们介绍到这，下面看看llama-index是怎么处理的：  

llama-index实现

\#\## **定义切分器**


* 
* 
* 
* 
* 

    import jsonfrom llama_index.core.node_parser import JSONNodeParserfrom llama_index.core import Document
    parser = JSONNodeParser()


**切分文档**

* 
* 
* 

    nodes = parser.get_nodes_from_documents(  [Document(text=json.dumps(json_data))]  )


可以看出，llama_index将json切分成了一个个小块。我们可以进一步做切分处理。

JSON的切分就讲到着，大家感觉是不是很有用呢？下篇文章我们将继续分享。

如果对内容有什么疑问和建议可以私信和留言，也可以添加我加入大模型交流群，一起讨论大模型在创作、RAG和agent中的应用。  

好了，这就是我今天想分享的内容。如果你对大模型应用感兴趣，别忘了点赞、关注噢\~


往期推荐


[RAG文本切分的五个层次1：字符切分基础(实战)](http://mp.weixin.qq.com/s?__biz=Mzk0NTcyNTMzNw==&mid=2247483951&idx=1&sn=61c25be0edab945c7b34980ec7dd98de&chksm=c31048d9f467c1cf1f4323b52a568af63f0086359385f77a8464b1b717ea65ee18ebd181d6f4&scene=21\#wechat_redirect)

[](https://mp.weixin.qq.com/s?__biz=MzI0MjYwNTUyMw==&mid=2247484227&idx=1&sn=57de0d20b27be9a273f6418875360fa3&chksm=e9788fffde0f06e930d951763f03e52b8cf392b164ea00b5b0a1112e6572fe9bfebc53933195&scene=21\#wechat_redirect)[RAG文本切分的五个层次2：递归字符分割(实战)](http://mp.weixin.qq.com/s?__biz=Mzk0NTcyNTMzNw==&mid=2247483959&idx=1&sn=8805bfc48c02cc396042eed5ad5f440a&chksm=c31048c1f467c1d734fba7253411119c5b65b39319cb5bb73681f6dd4ceb2b4d822d2d0bc9c3&scene=21\#wechat_redirect)  


[支持大模型流式输出的JSON提取工具](http://mp.weixin.qq.com/s?__biz=Mzk0NTcyNTMzNw==&mid=2247483821&idx=1&sn=6f34d91291fbcab03a79142eaa3ed56f&chksm=c3104b5bf467c24d7c4184784831d2cab8ce97f47cfc86d40da172650e67dba9a0860a7411b0&scene=21\#wechat_redirect)

[一文读懂token到底是什么鬼，消耗那么多钱？](http://mp.weixin.qq.com/s?__biz=Mzk0NTcyNTMzNw==&mid=2247483676&idx=1&sn=34ff4199b3506d29bd2ceb38adc11093&chksm=c3104beaf467c2fc6406daecf514cd9ecc0e1ae5fff6007b370ff1ae1224484796967b48cd6f&scene=21\#wechat_redirect)

[Read in Cubox](https://cubox.pro/web/card/7246426759866875976)
