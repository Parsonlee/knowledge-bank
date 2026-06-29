# 概念_Markdown标题切分

> tags: RAG, RAG/chunking
> confidence: high

## 定义

Markdown 标题切分是文本切分 Level 3（文档结构切分）针对 Markdown 格式的具体实现。利用 Markdown 文件按标题组织的结构特点，在特定标题组中创建块，使共同上下文的文本放在一起。

## 实现（LangChain MarkdownHeaderTextSplitter）

### 指定要拆分的标题
```python
headers_to_split_on = [
    ("#", "Header 1"),
    ("##", "Header 2"),
    ("###", "Header 3"),
]
markdown_splitter = MarkdownHeaderTextSplitter(headers_to_split_on)
md_header_splits = markdown_splitter.split_text(markdown_document)
```
切分后内容按标题分组，标题层级信息存入每个 Document 的 metadata。

### 关键参数

- **strip_headers**：默认 True 剥离被分割的标头；`strip_headers=False` 将标题保留到内容中
- **return_each_line**：默认 False 按标题聚合行；`return_each_line=True` 使一行成为一条独立 Document

### 限制块大小

在每个 Markdown 标题组中再应用 `RecursiveCharacterTextSplitter`（如 chunk_size=250, chunk_overlap=30）进一步控制块大小，实现两级切分。

安装：`pip install langchain-text-splitters`

## 关联

- 上层概念：[[概念_文档结构切分]]、[[概念_文本切分五层级]]
- 相关概念：[[概念_递归字符切分]]、[[概念_Chunk_Size与Overlap]]
- 来源：[[RAG文本切分_Markdown切分]]
