# RAG文本切分LV3：轻松定制Markdown切分

[mp.weixin.qq.com](https://mp.weixin.qq.com/s?__biz=Mzk0NTcyNTMzNw==&mid=2247484120&idx=1&sn=51fdd215151fe9be2d0ab8290eed6a1e&chksm=c310482ef467c13880ca7633fafbac9bedb57c318a7629ce08d27ea7609baa3e42c7ab70992a&cur_album_id=3583314836786053132&scene=189)哎呀AIYA 哎呀AIYA

上篇文章我们介绍了借助LLM和OCR将文档转换成markdown的方法：[颠覆传统OCR轻松搞定复杂PDF的工具](http://mp.weixin.qq.com/s?__biz=Mzk0NTcyNTMzNw==&mid=2247484116&idx=1&sn=bcc36c86009e0f4811d6b1e0ed5f6de7&chksm=c3104822f467c13463c036ebdda23b93eb68fc7ed1b6679f2c22297582bd5c7453e230566716&scene=21#wechat_redirect)。本篇文章将介绍如何对markdown进行有效切分。

之前介绍了文本切分五个层级，本文方法是第三个层次：

* **Level 1: [Character Splitting](http://mp.weixin.qq.com/s?__biz=Mzk0NTcyNTMzNw==&mid=2247483951&idx=1&sn=61c25be0edab945c7b34980ec7dd98de&chksm=c31048d9f467c1cf1f4323b52a568af63f0086359385f77a8464b1b717ea65ee18ebd181d6f4&scene=21#wechat_redirect)** - 简单的字符长度切分

* **Level 2: [Recursive Character Text Splitting](http://mp.weixin.qq.com/s?__biz=Mzk0NTcyNTMzNw==&mid=2247483959&idx=1&sn=8805bfc48c02cc396042eed5ad5f440a&chksm=c31048c1f467c1d734fba7253411119c5b65b39319cb5bb73681f6dd4ceb2b4d822d2d0bc9c3&scene=21#wechat_redirect)** - 通过分隔符切分，然后递归合并

* **Level 3: [Document Specific Splitting](http://mp.weixin.qq.com/s?__biz=Mzk0NTcyNTMzNw==&mid=2247483975&idx=1&sn=c2de67cc8dcb53986ccfaed03547bab6&chksm=c31048b1f467c1a77ad27d3e8c6b549844f927a3523a0b385e2bde82c01a3886cf34103b5fdb&scene=21#wechat_redirect)** - 针对不同文档格式切分 (PDF, Python, Markdown)

* **Level 4: [Semantic Splitting](http://mp.weixin.qq.com/s?__biz=Mzk0NTcyNTMzNw==&mid=2247484106&idx=1&sn=e731d2e0cf52ccdd685eab32dfeaa131&chksm=c310483cf467c12a5d5c85ce3c66ec4d1379bff786ed802fd6c954a8972458021998a4367d8a&scene=21#wechat_redirect)** - 语义切分

* **Level 5: Agentic Splitting**-使用代理实现自动切分

基本概念和环境

分块通常旨在将具有共同上下文的文本放在一起。考虑到这一点，我们可能希望特别尊重文档本身的结构。例如，markdown 文件按标题组织。在特定标题组中创建块是一种直观的想法。为了解决这一挑战，我们可以使用MarkdownHeaderTextSplitter。这将按指定的一组标题拆分 markdown 文件。

本文用到的安装包如下：  

* 

    pip install langchain-text-splitters


切分实现

### 我们可以指定要拆分的标题headers_to_split_on，切分之后内容按标题分组 ：


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

    markdown_document = "# Foo\n\n    ## Bar\n\nHi this is Jim\n\nHi this is Joe\n\n ### Boo \n\n Hi this is Lance \n\n ## Baz\n\n Hi this is Molly"
    headers_to_split_on = [    ("#", "Header 1"),    ("##", "Header 2"),    ("###", "Header 3"),]
    markdown_splitter = MarkdownHeaderTextSplitter(  headers_to_split_on)md_header_splits = markdown_splitter.split_text(  markdown_document)print(md_header_splits)


结果如下：

* 
* 
* 

    [Document(page_content='Hi this is Jim  \nHi this is Joe', metadata={'Header 1': 'Foo', 'Header 2': 'Bar'}), Document(page_content='Hi this is Lance', metadata={'Header 1': 'Foo', 'Header 2': 'Bar', 'Header 3': 'Boo'}), Document(page_content='Hi this is Molly', metadata={'Header 1': 'Foo', 'Header 2': 'Baz'})]


默认情况下，MarkdownHeaderTextSplitter从输出块的内容中剥离被分割的标头。可以通过设置strip_headers = False来禁用此功能。

* 
* 
* 
* 
* 
* 

    markdown_splitter = MarkdownHeaderTextSplitter(    headers_to_split_on,     strip_headers=False)md_header_splits = markdown_splitter.split_text(  markdown_document)print(md_header_splits)


可以看到，标题添加到内容中了

* 
* 
* 

    [Document(page_content='# Foo  \n## Bar  \nHi this is Jim  \nHi this is Joe', metadata={'Header 1': 'Foo', 'Header 2': 'Bar'}), Document(page_content='### Boo  \nHi this is Lance', metadata={'Header 1': 'Foo', 'Header 2': 'Bar', 'Header 3': 'Boo'}), Document(page_content='## Baz  \nHi this is Molly', metadata={'Header 1': 'Foo', 'Header 2': 'Baz'})]


**如何将 Markdown 行返回为单独的文档**

默认情况下，MarkdownHeaderTextSplitter根据headers_to_split_on中指定的标题聚合行。我们可以通过指定return_each_line来禁用此功能，使得一行就是一条内容：

* 
* 
* 
* 
* 
* 

    markdown_splitter = MarkdownHeaderTextSplitter(    headers_to_split_on,    return_each_line=True,)md_header_splits = markdown_splitter.split_text(markdown_document)print(md_header_splits)


* 
* 
* 
* 

    [Document(page_content='Hi this is Jim', metadata={'Header 1': 'Foo', 'Header 2': 'Bar'}), Document(page_content='Hi this is Joe', metadata={'Header 1': 'Foo', 'Header 2': 'Bar'}), Document(page_content='Hi this is Lance', metadata={'Header 1': 'Foo', 'Header 2': 'Bar', 'Header 3': 'Boo'}), Document(page_content='Hi this is Molly', metadata={'Header 1': 'Foo', 'Header 2': 'Baz'})]


**如何限制块大小：**

然后，我们可以在每个 markdown 组中应用任何我们想要的文本分割器，例如RecursiveCharacterTextSplitter，它允许进一步控制块大小。

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

    markdown_document = "# Intro \n\n    ## History \n\n Markdown[9] is a lightweight markup language for creating formatted text using a plain-text editor. John Gruber created Markdown in 2004 as a markup language that is appealing to human readers in its source code form.[9] \n\n Markdown is widely used in blogging, instant messaging, online forums, collaborative software, documentation pages, and readme files. \n\n ## Rise and divergence \n\n As Markdown popularity grew rapidly, many Markdown implementations appeared, driven mostly by the need for \n\n additional features such as tables, footnotes, definition lists,[note 1] and Markdown inside HTML blocks. \n\n #### Standardization \n\n From 2012, a group of people, including Jeff Atwood and John MacFarlane, launched what Atwood characterised as a standardisation effort. \n\n ## Implementations \n\n Implementations of Markdown are available for over a dozen programming languages."
    headers_to_split_on = [    ("#", "Header 1"),    ("##", "Header 2"),]
    # MD splitsmarkdown_splitter = MarkdownHeaderTextSplitter(    headers_to_split_on=headers_to_split_on, strip_headers=False)md_header_splits = markdown_splitter.split_text(markdown_document)
    # Char-level splitsfrom langchain_text_splitters import RecursiveCharacterTextSplitter
    chunk_size = 250chunk_overlap = 30text_splitter = RecursiveCharacterTextSplitter(    chunk_size=chunk_size, chunk_overlap=chunk_overlap)
    # Splitsplits = text_splitter.split_documents(md_header_splits)splits


如果对内容有什么疑问和建议可以私信和留言，也可以添加我加入大模型交流群，一起讨论大模型在创作、RAG和agent中的应用。  

好了，这就是我今天想分享的内容。如果你对大模型应用感兴趣，别忘了点赞、关注噢\~


往期推荐


[RAG数据集自动构造探索, 附PROMPT](http://mp.weixin.qq.com/s?__biz=Mzk0NTcyNTMzNw==&mid=2247484090&idx=1&sn=61361b4553028f4e584f88793ea861ee&chksm=c310484cf467c15af6030f899f3c3e44f96ce511a2d49fe0e2d18dbab0bf77293e2b174bb000&scene=21#wechat_redirect)  


[支持大模型流式输出的JSON提取工具](http://mp.weixin.qq.com/s?__biz=Mzk0NTcyNTMzNw==&mid=2247483821&idx=1&sn=6f34d91291fbcab03a79142eaa3ed56f&chksm=c3104b5bf467c24d7c4184784831d2cab8ce97f47cfc86d40da172650e67dba9a0860a7411b0&scene=21#wechat_redirect)  


[高级 RAG实战：召回更好的片段Query扩展](http://mp.weixin.qq.com/s?__biz=Mzk0NTcyNTMzNw==&mid=2247484014&idx=1&sn=c50328bcf4e970150d36a0435ba8c72d&chksm=c3104898f467c18e5effdbc5b82ddc12f6bdb3848871a353605f1702c1639c8a7a2327da923e&scene=21#wechat_redirect)

[颠覆传统OCR轻松搞定复杂PDF的工具](http://mp.weixin.qq.com/s?__biz=Mzk0NTcyNTMzNw==&mid=2247484116&idx=1&sn=bcc36c86009e0f4811d6b1e0ed5f6de7&chksm=c3104822f467c13463c036ebdda23b93eb68fc7ed1b6679f2c22297582bd5c7453e230566716&scene=21#wechat_redirect)

[Read in Cubox](https://cubox.pro/web/card/7249426213075158351)
