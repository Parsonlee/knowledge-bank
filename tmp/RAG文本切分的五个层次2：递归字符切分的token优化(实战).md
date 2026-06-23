# RAG文本切分的五个层次2：递归字符切分的token优化(实战)

[mp.weixin.qq.com](https://mp.weixin.qq.com/s?__biz=Mzk0NTcyNTMzNw==&mid=2247483966&idx=1&sn=4895eeba3d51d02f83e2b96067eb9227&chksm=c31048c8f467c1dea75e0dbfb6dcd2652bb410753fa1f92140e7aca1ec33ff50d64fba445bc6&cur_album_id=3583314836786053132&scene=189)哎呀AIYA 哎呀AIYA


前面文章提到，我们将文本切分划分为五个层级，并介绍了第前两个层级的实现和一些基础知识。前面两种方案实现在统计长度的时候都是按字符(一个英文字母或中文汉字)计算的，这显然和大模型处理文本时存在差异；大模型在处理文本时，是按照[token](http://mp.weixin.qq.com/s?__biz=Mzk0NTcyNTMzNw==&mid=2247483676&idx=1&sn=34ff4199b3506d29bd2ceb38adc11093&chksm=c3104beaf467c2fc6406daecf514cd9ecc0e1ae5fff6007b370ff1ae1224484796967b48cd6f&scene=21#wechat_redirect)进行输入的，今天来介绍如何在切分时融入token切分。  

文本切分五个层级：

* **Level 1: [Character Splitting](http://mp.weixin.qq.com/s?__biz=Mzk0NTcyNTMzNw==&mid=2247483951&idx=1&sn=61c25be0edab945c7b34980ec7dd98de&chksm=c31048d9f467c1cf1f4323b52a568af63f0086359385f77a8464b1b717ea65ee18ebd181d6f4&scene=21#wechat_redirect)** - 简单的字符长度切分

* **Level 2: [Recursive Character Text Splitting](http://mp.weixin.qq.com/s?__biz=Mzk0NTcyNTMzNw==&mid=2247483959&idx=1&sn=8805bfc48c02cc396042eed5ad5f440a&chksm=c31048c1f467c1d734fba7253411119c5b65b39319cb5bb73681f6dd4ceb2b4d822d2d0bc9c3&scene=21#wechat_redirect)** - 通过分隔符切分，然后递归合并

* **Level 3: Document Specific Splitting** - 针对不同文档格式切分 (PDF, Python, Markdown)

* **Level 4: Semantic Splitting** - 语义切分

* **Level 5: Agentic Splitting**-使用代理实现自动切分

为什么要融入token

### 语言模型，不管是大语言模型，还是向量模型、重排模型等等，都是有长度限制的，我们在切分文档时使用token的个数进行切分，有以下好处：

*

  ### 保证切分后的文本片段不超过模型最大长度；

*

  ### 保证文本片段送入模型的token数相当，并行节约资源；

*

  ### 可以有效预估送入大模型的片段长度，便于系统内资源调整。

如何融入  

### 我们以下面的文本为例子：


* 
* 
* 

    text = """8月12日，中国乒乓球界的一则趣闻在网络上持续发酵，引发了广泛关注和热议。在巴黎奥运会期间的一次采访环节中，中国乒乓球队的绝对主力马龙在接受媒体采访时，其队友王楚钦与樊振东在镜头后的轻松"划水"画面被捕捉并上传至网络，迅速走红。这一幕不仅展现了国乒队员之间轻松愉快的氛围，也意外成为了公众茶余饭后的谈资。
    面对这一突如其来的"网红"事件，马龙在随后的一次做客节目中，以他特有的幽默与谦逊方式进行了回应。马龙笑称："看来今后王楚钦、樊振东的摸鱼机会不多了，其实他们两位的表达能力远胜于我，只是平时在训练场上太过勤快，以至于在这方面偶尔犯起了'懒'。""""


**OpenAI模型**

我们可以很容易的通过tiktoken在切分器中融入token切分工具：

**CharacterTextSplitter**

* 
* 
* 
* 
* 
* 

    from langchain_text_splitters import CharacterTextSplitter
    text_splitter = CharacterTextSplitter.from_tiktoken_encoder(    encoding_name="cl100k_base", chunk_size=50, chunk_overlap=0)texts = text_splitter.split_text(text)


**RecursiveCharacterTextSplitter**

* 
* 
* 
* 
* 
* 
* 
* 

    from langchain_text_splitters import RecursiveCharacterTextSplitter
    text_splitter = RecursiveCharacterTextSplitter.from_tiktoken_encoder(    model_name="gpt-4",    chunk_size=50,    chunk_overlap=0,)texts = text_splitter.split_text(text)


![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2Fr8c4hf2wliab0PF53GxaNn96XhLax91vmml5HkJXeruDtgKRic1yDPkUQewyTCibsviakD6roFYuWJXCcW8uBpCo8g%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26tp%3Dwebp%26wxfrom%3D5%26wx_lazy%3D1%26wx_co%3D1&valid=false)

* 
* 

    len(texts[0])# 39


第一行的字符长度才39，说明OpenAI在切中文字符时，一个汉字是好几个token，这玩意对中文来说可真坑啊，贵。

**SentenceTransformers类方法**

我们也可以使用SentenceTransformers进行切分，我们以bge-m3为例：  

* 
* 
* 
* 

    from langchain_text_splitters import SentenceTransformersTokenTextSplittersplitter = SentenceTransformersTokenTextSplitter(  tokens_per_chunk=50, chunk_overlap=0, model_name="./bge-m3")pprint(splitter.split_text(text))


![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2Fr8c4hf2wliab0PF53GxaNn96XhLax91vm7gxZsyK5z1PtcicPq4KmDJIOl0b0ibF2ibTo4eEoESeM1AwAMhYj0jKWg%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26tp%3Dwebp%26wxfrom%3D5%26wx_lazy%3D1%26wx_co%3D1&valid=false)

* 
* 

    len(texts[0])# 77


这些对中文支持比较好的模型，转化为token后，中文的压缩比例显著提升了。  

还有很多其它的切分工具，例如NLTKTextSplitter，SpacyTextSplitter，大家可以去进一步探索。

如何加载自己的工具

### 当我们使用自己的向量模型时，我们需要在切分的时候也使用自己的模型，那么可以使用下面的方法：


* 
* 
* 
* 
* 
* 
* 
* 
* 
* 
* 
* 
* 

    from transformers import AutoTokenizer
    # 定义tokenizertokenizer = AutoTokenizer.from_pretrained("./bge-m3")
    from langchain_text_splitters import RecursiveCharacterTextSplitter
    # 定义切分器text_splitter = RecursiveCharacterTextSplitter.from_huggingface_tokenizer(    tokenizer, chunk_size=50, chunk_overlap=0,     separators=["\n\n", "\n", "。"], keep_separator=False)texts = text_splitter.split_text(text)


![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2Fr8c4hf2wliab0PF53GxaNn96XhLax91vmHjUDowiaZ2pib0icicx1rBj2NTmOiaOOsaU3O3vmyryzgBXFaIrWlA4P8FQ%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26tp%3Dwebp%26wxfrom%3D5%26wx_lazy%3D1%26wx_co%3D1&valid=false)

大家是不是全学会了呢，字符级别的切分，我们就介绍到这里啦，下篇文章我们将介绍文档级别的切分方式。  

如果对内容有什么疑问和建议可以私信和留言，也可以添加我加入大模型交流群，一起讨论大模型在创作、RAG和agent中的应用。  

好了，这就是我今天想分享的内容。如果你对大模型应用感兴趣，别忘了点赞、关注噢\~


往期推荐


[RAG文本切分的五个层次1：字符切分基础(实战)](http://mp.weixin.qq.com/s?__biz=Mzk0NTcyNTMzNw==&mid=2247483951&idx=1&sn=61c25be0edab945c7b34980ec7dd98de&chksm=c31048d9f467c1cf1f4323b52a568af63f0086359385f77a8464b1b717ea65ee18ebd181d6f4&scene=21#wechat_redirect)

[](https://mp.weixin.qq.com/s?__biz=MzI0MjYwNTUyMw==&mid=2247484227&idx=1&sn=57de0d20b27be9a273f6418875360fa3&chksm=e9788fffde0f06e930d951763f03e52b8cf392b164ea00b5b0a1112e6572fe9bfebc53933195&scene=21#wechat_redirect)[RAG文本切分的五个层次2：递归字符分割(实战)](http://mp.weixin.qq.com/s?__biz=Mzk0NTcyNTMzNw==&mid=2247483959&idx=1&sn=8805bfc48c02cc396042eed5ad5f440a&chksm=c31048c1f467c1d734fba7253411119c5b65b39319cb5bb73681f6dd4ceb2b4d822d2d0bc9c3&scene=21#wechat_redirect)  


[支持大模型流式输出的JSON提取工具](http://mp.weixin.qq.com/s?__biz=Mzk0NTcyNTMzNw==&mid=2247483821&idx=1&sn=6f34d91291fbcab03a79142eaa3ed56f&chksm=c3104b5bf467c24d7c4184784831d2cab8ce97f47cfc86d40da172650e67dba9a0860a7411b0&scene=21#wechat_redirect)

[一文读懂token到底是什么鬼，消耗那么多钱？](http://mp.weixin.qq.com/s?__biz=Mzk0NTcyNTMzNw==&mid=2247483676&idx=1&sn=34ff4199b3506d29bd2ceb38adc11093&chksm=c3104beaf467c2fc6406daecf514cd9ecc0e1ae5fff6007b370ff1ae1224484796967b48cd6f&scene=21#wechat_redirect)

[Read in Cubox](https://cubox.pro/web/card/7246425924340549464)
