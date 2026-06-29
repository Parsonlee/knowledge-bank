# RAG文本切分_JSON文档切分

> 来源：哎呀AIYA 微信公众号《RAG文本切分五个层次3：不同文档切分之JSON(实战)》
> URL：https://mp.weixin.qq.com/s?__biz=Mzk0NTcyNTMzNw==&mid=2247483975&idx=1&sn=c2de67cc8dcb53986ccfaed03547bab6
> tags: RAG, RAG/chunking
> Cubox 高亮：无

## 摘要

文本切分系列第 3 篇。介绍 Level 3 基于文档结构的切分中 JSON 数据的切分方法。日常数据不仅有 txt，还包含 JSON、Markdown、代码、PDF 等结构化数据，需要适配不同格式的切分策略。

## 核心内容

### JSON 切分逻辑
- 遍历 JSON 数据深度，构建更小的 JSON 块
- 尽量保持嵌套 JSON 对象完整，但在需要时会拆分以保持块大小在 min_chunk_size 和 max_chunk_size 之间
- 如果值不是嵌套 JSON 而是大字符串，字符串不会被分割（需要硬性限制时可组合递归文本分割器）

### LangChain 实现
- `RecursiveJsonSplitter(max_chunk_size=300)`，可设 `min_chunk_size`
- `splitter.split_json(json_data=json_data)` 按最内层进行分割
- **列表切分问题**：大列表会被完整保留导致片段超长
- **解决方案**：`convert_lists=True` 预处理，将列表内容转换为 `index:item` 作为 key:val 字典

### LLama-Index 实现
- `JSONNodeParser()` + `Document(text=json.dumps(json_data))`
- `parser.get_nodes_from_documents([...])` 将 JSON 切分成小块
- 可进一步做切分处理

## 关联

- 概念：[[概念_文本切分五层级]]、[[概念_文档结构切分]]
- 实体：[[实体_LangChain]]、[[实体_LlamaIndex]]
- 系列上一篇：[[RAG文本切分_token优化]]
- 系列下一篇：[[RAG文本切分_语义切分]]
