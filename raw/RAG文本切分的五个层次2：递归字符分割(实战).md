---
id: "7246424724572471957"
cubox_url: https://cubox.pro/web/card/7246424724572471957
url: https://mp.weixin.qq.com/s?__biz=Mzk0NTcyNTMzNw==&mid=2247483959&idx=1&sn=8805bfc48c02cc396042eed5ad5f440a&chksm=c31048c1f467c1d734fba7253411119c5b65b39319cb5bb73681f6dd4ceb2b4d822d2d0bc9c3&cur_album_id=3583314836786053132&scene=189
tags:
  - RAG
  - RAG/chunking
---
# RAG文本切分的五个层次2：递归字符分割(实战)

我们来介绍第二个层级Recursive Character Text Splitting，这个切分器是日常实践中通常会采用的，是最直观也有效的方案，也是其它高级方案的基础。

[Read in Cubox](https://cubox.pro/web/card/7246424724572471957)  
[Read Original](https://mp.weixin.qq.com/s?__biz=Mzk0NTcyNTMzNw==&mid=2247483959&idx=1&sn=8805bfc48c02cc396042eed5ad5f440a&chksm=c31048c1f467c1d734fba7253411119c5b65b39319cb5bb73681f6dd4ceb2b4d822d2d0bc9c3&cur_album_id=3583314836786053132&scene=189)  

---


---

\## 📖 正文全文

# RAG文本切分的五个层次2：递归字符分割(实战)

[mp.weixin.qq.com](https://mp.weixin.qq.com/s?__biz=Mzk0NTcyNTMzNw==&mid=2247483959&idx=1&sn=8805bfc48c02cc396042eed5ad5f440a&chksm=c31048c1f467c1d734fba7253411119c5b65b39319cb5bb73681f6dd4ceb2b4d822d2d0bc9c3&cur_album_id=3583314836786053132&scene=189)哎呀AIYA 哎呀AIYA


上篇文章提到，我们将文本切分划分为五个层级，并介绍了第一个层级的实现和一些基础知识。今天我们来介绍第二个层级Recursive Character Text Splitting，这个切分器是日常实践中通常会采用的，是最直观也有效的方案，也是其它高级方案的基础。

文本切分五个层级：

* **Level 1: [Character Splitting](http://mp.weixin.qq.com/s?__biz=Mzk0NTcyNTMzNw==&mid=2247483951&idx=1&sn=61c25be0edab945c7b34980ec7dd98de&chksm=c31048d9f467c1cf1f4323b52a568af63f0086359385f77a8464b1b717ea65ee18ebd181d6f4&scene=21\#wechat_redirect)** - 简单的字符长度切分

* **Level 2: Recursive Character Text Splitting** - 通过分隔符切分，然后递归合并

* **Level 3: Document Specific Splitting** - 针对不同文档格式切分 (PDF, Python, Markdown)

* **Level 4: Semantic Splitting** - 语义切分

* **Level 5: Agentic Splitting**-使用代理实现自动切分

为什么需要Recursive Character Text Splitting

按字符长度切分的问题在于，根本没有考虑到文档的结构。只是按固定数量的字符分割，这样很容易造成文档被随意切分开了，导致最后的效果不好。  
递归字符文本分割器可以帮助解决这个问题。有了它，切分的过程可描述为：我们先指定一系列分隔符，这些分隔符用于分割文档，然后将分割好的小块合并，达到指定的长度。

它是切分器中最基础的做法，也是快速搭建应用流程的首选。如果在不知道选择哪个切分器的时候，这是一个不错的选择。

我们看看在langchain中的默认分隔符\["\\n\\n", "\\n", " ", ""\]：

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2Fr8c4hf2wliaYElo6jY6YzYH3rI6amXrd615dibRPHOuoicTdVOLBJDE6Vtk4yGspGCJteB4ULzhSqmDIqNTSvUEhA%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26tp%3Dwebp%26wxfrom%3D5%26wx_lazy%3D1%26wx_co%3D1&valid=false)

看看下面例子，在一般情况下，我们希望的切分情况，如何能实现它？

* 
* 
* 
* 
* 
* 
* 

    text = """One of the most important things I didn't understand about the world when I was a child is the degree to which the returns for performance are superlinear.
    Teachers and coaches implicitly told us the returns were linear. "You get out," I heard a thousand times, "what you put in." They meant well, but this is rarely true. If your product is only half as good as your competitor's, you don't get half as many customers. You get no customers, and you go out of business.
    It's obviously true that the returns for performance are superlinear in business. Some think this is a flaw of capitalism, and that if we changed the rules it would stop being true. But superlinear returns for performance are a feature of the world, not an artifact of rules we've invented. We see the same pattern in fame, power, military victories, knowledge, and even benefit to humanity. In all of these, the rich get richer. [1]"""


可以很直观地将它切分成三个段落：  

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2Fr8c4hf2wliaYElo6jY6YzYH3rI6amXrd6SgfkeT1ZtZCUVs0vLZZe2nC7ckEJJW1Qp9DtRStJFgskfpcXttmIJA%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26tp%3Dwebp%26wxfrom%3D5%26wx_lazy%3D1%26wx_co%3D1&valid=false)

如何实现

\#\## **加载依赖方法**


* 

    from langchain.text_splitter import RecursiveCharacterTextSplitter


**构建切分器**

* 
* 
* 
* 

    text_splitter = RecursiveCharacterTextSplitter(chunk_size=65, chunk_overlap=0)text_splitter.create_documents([text])# chunk_size 每个片段的字符数# chunk_overlap 片段之间的重叠字符数


总共生成了16段，从结果上看，虽然没有再将单词切开了，但感觉切的还是太零碎了：  

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2Fr8c4hf2wliaYElo6jY6YzYH3rI6amXrd6XSRkm110iaFoAtttJvY1LHwEibOTO0WBxygjXggJ09rHwmWkqFu4JOnQ%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26tp%3Dwebp%26wxfrom%3D5%26wx_lazy%3D1%26wx_co%3D1&valid=false)

注意，现在有很多块以"."结尾。这是因为这些是句子的结尾，但又没有把"."添加到分隔符中，所以比较多。我也不知道为什么" "是分隔符，"."不是默认分隔符，有知道的可以私信我，哈哈。

拆分器首先寻找\\n\\n(段落断行)，一旦段落被分割，它就会查看块的大小，如果一个块太大，它就会被下一个分隔符分割。如果该块仍然太大，那么它将移动到下一个，依此类推。

**更大的chunk_size**

对英文来说65个字符也太小了，我们放大chunk_size看看效果。

* 
* 

    text_splitter = RecursiveCharacterTextSplitter(chunk_size=450, chunk_overlap=0)text_splitter.create_documents([text])


总共生成3段，这就是我们预期的切分效果。  

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2Fr8c4hf2wliaYElo6jY6YzYH3rI6amXrd625LJ8iavlqMWP1tibhWoZCrdS7Aov8o4YrtOYhgB8Eo2qBMUdqkvnurA%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26tp%3Dwebp%26wxfrom%3D5%26wx_lazy%3D1%26wx_co%3D1&valid=false)

**仅仅使用字符个数作为小块内的切分依据，似乎不是一个好的方案；相同语义下，中英文、数字等字符个数差别太大了。下篇文章我们将介绍如何优化小块内的切分和计数方案。**   

如果对内容有什么疑问和建议可以私信和留言，也可以添加我加入大模型交流群，一起讨论大模型在创作、RAG和agent中的应用。  

好了，这就是我今天想分享的内容。如果你对大模型应用感兴趣，别忘了点赞、关注噢\~


往期推荐


[RAG文本切分的五个层次1：字符切分基础(实战)](http://mp.weixin.qq.com/s?__biz=Mzk0NTcyNTMzNw==&mid=2247483951&idx=1&sn=61c25be0edab945c7b34980ec7dd98de&chksm=c31048d9f467c1cf1f4323b52a568af63f0086359385f77a8464b1b717ea65ee18ebd181d6f4&scene=21\#wechat_redirect)  


[](https://mp.weixin.qq.com/s?__biz=MzI0MjYwNTUyMw==&mid=2247484227&idx=1&sn=57de0d20b27be9a273f6418875360fa3&chksm=e9788fffde0f06e930d951763f03e52b8cf392b164ea00b5b0a1112e6572fe9bfebc53933195&scene=21\#wechat_redirect)[一款约束大模型结构化输出的开源工具，后处理不存在了提速又提质！(实战)](http://mp.weixin.qq.com/s?__biz=Mzk0NTcyNTMzNw==&mid=2247483887&idx=1&sn=1304cc26fe5269d402207d0acedca368&chksm=c3104b19f467c20fb59e80bffbc8b24dfee79494017a94a6aa8a3cbf019f707557c7979dbc40&scene=21\#wechat_redirect)  


[支持大模型流式输出的JSON提取工具](http://mp.weixin.qq.com/s?__biz=Mzk0NTcyNTMzNw==&mid=2247483821&idx=1&sn=6f34d91291fbcab03a79142eaa3ed56f&chksm=c3104b5bf467c24d7c4184784831d2cab8ce97f47cfc86d40da172650e67dba9a0860a7411b0&scene=21\#wechat_redirect)

[一文读懂token到底是什么鬼，消耗那么多钱？](http://mp.weixin.qq.com/s?__biz=Mzk0NTcyNTMzNw==&mid=2247483676&idx=1&sn=34ff4199b3506d29bd2ceb38adc11093&chksm=c3104beaf467c2fc6406daecf514cd9ecc0e1ae5fff6007b370ff1ae1224484796967b48cd6f&scene=21\#wechat_redirect)

[Read in Cubox](https://cubox.pro/web/card/7246424724572471957)
