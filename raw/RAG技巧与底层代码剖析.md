---
id: "7331951337749351963"
cubox_url: https://cubox.pro/web/card/7331951337749351963
url: https://mp.weixin.qq.com/s/oX6JZS_INj9M8Ntkh4Jp9Q
tags:
  - RAG

---
# RAG技巧与底层代码剖析

1. naive RAG
2. 基于语义的分块（百分位法、标准差法、四分位距法）
3. 上下文检索增强
4. 添加“块标题”（Contextual Chunk Headers，CCH）
5. 基于问题生成的RAG
6. Query改写
7. 重排序
8. 用于增强 RAG 的相关段落提取（Relevant Segment Extraction，RSE）
9. 上下文压缩技术：提升 RAG 系统效率
10. 反馈机制（Feedback Loop）

[Read in Cubox](https://cubox.pro/web/card/7331951337749351963)  
[Read Original](https://mp.weixin.qq.com/s/oX6JZS_INj9M8Ntkh4Jp9Q)  

---


---

\## 📖 正文全文

# RAG技巧与底层代码剖析

[mp.weixin.qq.com](https://mp.weixin.qq.com/s/oX6JZS_INj9M8Ntkh4Jp9Q)子茹 阿里云开发者

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_jpg%2FEkgpOcjaJwjxN3eZFpTO7lE1PnrwFvUjPSTbibVcicpUIG4Sf9hgBkTLpKVHl5BFo0Wp7dVA0mkmqwxXLnpwL1rg%2F640%3Fwx_fmt%3Djpeg%26tp%3Dwebp%26wxfrom%3D5%26wx_lazy%3D1&valid=false)

导读

【用Python基础库从零手撕RAG内核】你是否还在用现成框架调包实现RAG？本文带你撕开技术黑箱，仅用numpy等Python基础库构建RAG系统，从零手撕RAG内核！从文本划分、向量化、相似度检索到生成优化，逐行代码解剖检索增强生成的核心逻辑，更深度解析9大实战技巧：从智能分块策略到动态上下文压缩，助你突破回答质量瓶颈。拒绝做调参工具人，这次彻底掌握RAG的底层基因！

相信大家都对 RAG（Retrieval-Augmented Generation，检索增强生成）并不陌生。在实际应用中，很多人会借助像 LangChain 或 FAISS 这样的框架来实现 RAG 功能。但如果我们从零开始手动实现一个 RAG 系统，你是否尝试过？

为了帮助大家从底层更好地理解 RAG 的工作原理，本文将带你一步步实现一个简易版本的 RAG 系统。在这个过程中，我们不会使用任何复杂的框架，而是仅依赖大家熟悉的 Python 标准库和常用科学计算库，如 numpy。

一、从0开始：简易RAG实现

\## 在构建更复杂的 RAG 架构之前，我们先从最基础的版本入手。整个流程可以分为以下几个关键步骤：

1.数据导入：加载并预处理原始文本数据，为后续处理做好准备。

2.文本分块：将长文本分割成较小的段落或句子，以提高检索效率和相关性。

3.创建 Embedding：使用嵌入模型将文本块转换为向量表示，便于进行语义层面的比较与匹配。

4.语义搜索：根据用户输入的查询内容，在已有向量库中检索出最相关的文本块。

5.响应生成：基于检索到的相关内容，结合语言模型生成最终的回答输出。


**设置环境**


首先，我们需要导入必要的库：

    import osimport numpy as npimport jsonimport fitzimport dashscopefrom openai import OpenAI
    os.environ['DASHSCOPE_API_KEY'] = "your dashscope api key"


**从PDF文件中提取文本**


首先我们需要一个文本数据源。在这篇文章中，我们使用PyMuPDF库从PDF文件中提取文本，这里定义一个函数来从PDF中提取文本：

    def extract_text_from_pdf(pdf_path):    # 打开PDF文件    document = fitz.open(pdf_path)    all_text = ""  # 初始化一个空字符串存储提取出的文本
        # 遍历PDF中的每一页    for page_num in range(document.page_count):        page = document[page_num]  # 获取页面        text = page.get_text("text")  # 从页面提取文本        all_text += text  # 将提取出的文本追加到all_text字符串
        return all_text  # 返回提取出的文本


**对提取出的文本进行分块**


有了提取出的文本后，我们将它分成较小的、有重叠的块，以提高检索准确性。

    def chunk_text(text_input, chunk_size, overlap_size):    text_chunks = []  # 初始化一个列表存储文本块
        # 循环遍历文本，步长为(chunk_size - overlap_size)    for i in range(0, len(text_input), chunk_size - overlap_size):        text_chunks.append(text_input[i:i + chunk_size])  # 追加从i到i+chunk_size的文本块到text_chunks列表
        return text_chunks  # 返回文本块列表


**设置OpenAI API客户端**


初始化OpenAI客户端用于生成嵌入和响应。

    client = OpenAI(    api_key=os.getenv("DASHSCOPE_API_KEY"),  # 如果您没有配置环境变量，请在此处用您的API Key进行替换    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1"  # 百炼服务的base_url)


**提取并分块PDF文件中的文本**


现在，我们加载PDF，提取文本，并将其分割成块。

    # 定义PDF文件路径pdf_path = "knowledge_base/智能编码助手通义灵码.pdf"
    # 从PDF文件中提取文本extracted_text = extract_text_from_pdf(pdf_path)
    # 将提取出的文本分割成1000字符大小的块，重叠部分为100字符text_chunks = chunk_text(extracted_text, 1000, 100)
    # 打印创建的文本块数量print("文本块数量:", len(text_chunks))
    # 打印第一个文本块print("\n第一个文本块:")print(text_chunks[0])


    文本块数量: 5
    第一个文本块:什么是智能编码助手通义灵码 智能编码助手通义灵码（简称为通义灵码），是由阿里云提供的智能编码辅助工具，提供代码智能生成、智能问答、多文件修改、编程智能体等能力，为开发者带来高效、流畅的编码体验，引领 AI 原生研发新范式。同时，我们为企业客户提供了企业标准版、专属版，具备企业级场景自定义、私域知识增强等能力，助力企业研发智能化升级。 核心能力 代码补全 Code Completion 经过海量优秀开源代码数据训练，可根据当前代码文件及跨文件的上下文，为您生成行级/函数级代码、单元测试、代码优化建议等。沉浸式编码心流，秒级生成速度，让您更专注在技术设计，高效完成编码工作。 智能问答 Ask Mode 智能问答模式拥有海量研发文档、产品文档、通用研发知识等，并结合工程级感知能力，为开发者解决编码过程中遇到的研发问题，协助开发者进行代码问题修复、调试或运行错误的排查等。 文件编辑 Edit Mode 文件编辑模式具备多文件代码修改的能力，当开发者需要精准地修改代码文件时，能够结合需求描述和当前工程环境进行多文件修改，并且可以进行多次迭代、代码审查，帮助开发者高效可控地完成代码修改任务。 智能体 Agent Mode 智能体模式具备自主决策、环境感知、工具使用等能力，可以根据开发者的编码诉求，使用工程检索、文件编辑、终端等工具，可以端到端完成编码任务。同时，支持开发者配置 MCP 工具，编码更加贴合开发者工作流程。 产品优势 • 多种会话模式：一次会话流中同时支持问答模式、文件编辑模式、智能体模式，开发者可以针对不同场景和问题难度自由切换模式，实现工作效率最大化。 • 工程自动感知：根据开发者的任务描述，可自动感知工程框架、技术栈、所需代码文件、错误信息等工程内信息，无需手动添加工程上下文，任务描述更轻松，代码补全更加贴合当前代码库的业务场景。 • 工程级变更：可根据开发者的任务描述，自主进行任务拆解和工程内多个代码文件修改，同时可通过多次对话进行逐步迭代或快照回滚，与通义灵码协同完成编码任务。 • 记忆感知：支持基于大模型的自主记忆能力，在开发者与通义灵码的对话过程，通义灵码会逐步形成针对开发者个人、工程、问题等相关的丰富记忆，越用越懂您。 • 多种企业版方案，灵活选择：提供企业标准版、企业


**创建文本块的嵌入向量**


嵌入向量将文本转换为数值向量，允许高效地进行相似度搜索。这里用了阿里云的embedding模型"text-embedding-v3"。

    # 创建文本块的嵌入向量def create_embeddings(texts, model="text-embedding-v3"):    """    输入一组文本（字符串或列表），返回对应的嵌入向量列表    """    ifisinstance(texts, str):        texts = [texts]  # 确保输入为列表形式
        completion = client.embeddings.create(        model=model,        input=texts,        encoding_format="float"    )        # 将响应转换为 dict 并提取所有 embedding    data = json.loads(completion.model_dump_json())    embeddings = [item["embedding"] for item in data["data"]]    return embeddings


**执行语义搜索**


我们通过计算余弦相似度来找到与用户查询最相关的文本块。

    from sklearn.metrics.pairwise import cosine_similarity
    # 语义搜索函数def semantic_search(query, text_chunks, embeddings=None, k=2):    """    在 text_chunks 中找出与 query 最相关的 top-k 文本块        参数：        query: 查询语句        text_chunks: 候选文本块列表        embeddings: 对应的嵌入向量列表（如果已提前计算）        k: 返回最相关的结果数量            返回：        top_k_chunks: 最相关的 top-k 文本块    """    if embeddings is None:        embeddings = create_embeddings(text_chunks)  # 如果没有提供，则自动生成    else:        assert len(embeddings) == len(text_chunks), "embeddings 和 text_chunks 必须长度一致"
        query_embedding = create_embeddings(query)[0]  # 获取查询的嵌入
        # 计算相似度    similarity_scores = []    for i, chunk_embedding in enumerate(embeddings):        score = cosine_similarity([query_embedding], [chunk_embedding])[0][0]        similarity_scores.append((i, score))
        # 排序并取 top-k    similarity_scores.sort(key=lambda x: x[1], reverse=True)    top_indices = [index for index, _ in similarity_scores[:k]]    return [text_chunks[index] for index in top_indices]


最后，执行查询操作，并打印结果。

    # 执行语义搜索query = '通义灵码的智能体能力是什么？'top_chunks = semantic_search(query, text_chunks, k=2)
    # 输出结果print("Query:", query)for i, chunk in enumerate(top_chunks):    print(f"Context {i + 1}:\n{chunk}\n=====================================")


    Query: 通义灵码的智能体能力是什么？Context 1:什么是智能编码助手通义灵码 智能编码助手通义灵码（简称为通义灵码），是由阿里云提供的智能编码辅助工具，提供代码智能生成、智能问答、多文件修改、编程智能体等能力，为开发者带来高效、流畅的编码体验，引领 AI 原生研发新范式。同时，我们为企业客户提供了企业标准版、专属版，具备企业级场景自定义、私域知识增强等能力，助力企业研发智能化升级。 核心能力 代码补全 Code Completion 经过海量优秀开源代码数据训练，可根据当前代码文件及跨文件的上下文，为您生成行级/函数级代码、单元测试、代码优化建议等。沉浸式编码心流，秒级生成速度，让您更专注在技术设计，高效完成编码工作。 智能问答 Ask Mode 智能问答模式拥有海量研发文档、产品文档、通用研发知识等，并结合工程级感知能力，为开发者解决编码过程中遇到的研发问题，协助开发者进行代码问题修复、调试或运行错误的排查等。 文件编辑 Edit Mode 文件编辑模式具备多文件代码修改的能力，当开发者需要精准地修改代码文件时，能够结合需求描述和当前工程环境进行多文件修改，并且可以进行多次迭代、代码审查，帮助开发者高效可控地完成代码修改任务。 智能体 Agent Mode 智能体模式具备自主决策、环境感知、工具使用等能力，可以根据开发者的编码诉求，使用工程检索、文件编辑、终端等工具，可以端到端完成编码任务。同时，支持开发者配置 MCP 工具，编码更加贴合开发者工作流程。 产品优势 • 多种会话模式：一次会话流中同时支持问答模式、文件编辑模式、智能体模式，开发者可以针对不同场景和问题难度自由切换模式，实现工作效率最大化。 • 工程自动感知：根据开发者的任务描述，可自动感知工程框架、技术栈、所需代码文件、错误信息等工程内信息，无需手动添加工程上下文，任务描述更轻松，代码补全更加贴合当前代码库的业务场景。 • 工程级变更：可根据开发者的任务描述，自主进行任务拆解和工程内多个代码文件修改，同时可通过多次对话进行逐步迭代或快照回滚，与通义灵码协同完成编码任务。 • 记忆感知：支持基于大模型的自主记忆能力，在开发者与通义灵码的对话过程，通义灵码会逐步形成针对开发者个人、工程、问题等相关的丰富记忆，越用越懂您。 • 多种企业版方案，灵活选择：提供企业标准版、企业=====================================Context 2:感知：支持基于大模型的自主记忆能力，在开发者与通义灵码的对话过程，通义灵码会逐步形成针对开发者个人、工程、问题等相关的丰富记忆，越用越懂您。 • 多种企业版方案，灵活选择：提供企业标准版、企业专属版等多种面向企业客户的方案，并提供企业个性化方案，可灵活选择，加速企业内智能研发的规模化落地。 功能介绍 行间代码补全 • 行级/函数级实时续写：根据当前语法和跨文件的代码上下文，自动感知当前工程，实时生成行、函数级代码； • 注释生成代码：通过注释描述您想要的功能，可直接在编辑器区生成代码，编码心流不间断。 智能问答 • 研发问题问答：遇到编码疑问、技术难题时，一键唤起通义灵码，无需离开 IDE 客户端，即可快速获得答案和解决思路。 • 工程问答：通过问答即可快速结合当前仓库进行工程理解、代码查询等，同时可以通过自然语言描述需求，结合当前工程生成简单需求或缺陷的整体修复建议和建议代码。 • 图片多模态问答：支持选择、拖拽或粘贴将图片添加为上下文，自动分析图片内容，并根据需求描述生成代码建议或问题修复建议等。 • 企业知识库问答：借助企业知识和数据进行问答，快速构建企业研发知识问答助手，提升团队的工作效率和协作能力。 文件编辑 • 工程级变更：可根据开发者的任务描述，进行工程内多个代码文件修改，同时可通过多次对话进行逐步迭代或快照回滚，开发者与通义灵码协同逐步完成编码任务。 • 精确编辑：在开发者提供的上下文范围内完成代码文件修改，不会做出超出开发者预期的修改。 • 快速执行：严格遵循开发者的任务描述和提供的上下文，进行代码文件修改，无需进行额外的复杂任务计划，相比智能体模式完成任务更加迅速。 • 工具使用：拥有文件读取、工程内语义检索、文件编辑等代码修改相关工具使用能力，可帮助开发者快速完成代码修改。 编程智能体 • 工程级变更：可根据开发者的任务描述，自主进行任务拆解和工程内多个代码文件修改，同时可通过多次对话进行逐步迭代或快照回滚，与通义灵码协同完成编码任务。 • 工程自动感知：根据开发者的任务描述，可自动感知工程框架、技术栈、所需代码文件、错误信息等工程内信息，无需手动添加工程上下文，任务描述更轻松。 • 工具使用：可自主使用十多种内置编程工具，例如读写文件、代=====================================


**基于检索块生成响应**


    # 初始化 DashScope 客户端（使用阿里云通义千问）client = OpenAI(    api_key=os.getenv("DASHSCOPE_API_KEY"),  # 确保提前设置好环境变量    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1")
    # 设置系统提示SYSTEM_PROMPT = (    "你是一个 AI 助手，必须严格根据提供的上下文内容进行回答。"    "如果无法从提供的上下文中直接得出答案，请回复：'我无法根据现有信息回答这个问题。'")
    def generate_response(system_prompt, user_message, model="qwen-max"):    """    使用 DashScope 的通义千问模型生成基于上下文的回答。
        参数：        system_prompt (str): 控制 AI 行为的系统指令        user_message (str): 用户输入的问题及上下文        model (str): 使用的模型名称，默认为 qwen-plus
        返回：        str: 模型生成的回答内容    """    response = client.chat.completions.create(        model=model,        temperature=0.0,  # 温度设为0，保证输出确定性        max_tokens=512,   # 可按需调整最大输出长度        messages=[            {"role": "system", "content": system_prompt},            {"role": "user", "content": user_message}        ]    )        return response.choices[0].message.content.strip()
    # 示例 top_chunks（假设这是 semantic_search 返回的结果）top_chunks = [    "通义灵码是一个基于 AI 的智能编程助手。",    "文件编辑能力包括自动补全、错误修复和代码重构等功能。"]
    query = "通义灵码的智能体能力是什么？"
    # 构建用户 prompt（包含上下文 + 问题）user_prompt = "\n".join([f"上下文 {i + 1}:\n{chunk}"for i, chunk in enumerate(top_chunks)])user_prompt += f"\n\n问题：{query}"
    # 生成 AI 回答answer = generate_response(SYSTEM_PROMPT, user_prompt)
    # 输出结果print("AI 回答：")print(answer)


     AI 回答：通义灵码的智能体能力包括以下几个方面：
    - **自主决策**：能够根据开发者的编码需求自主进行任务拆解。- **环境感知**：可以自动感知工程框架、技术栈、所需代码文件、错误信息等工程内信息，无需手动添加工程上下文。- **工具使用**：能自主使用十多种内置编程工具，如读写文件、代码编辑等。- **端到端完成编码任务**：基于开发者的需求，利用工程检索、文件编辑、终端等多种工具来实现从开始到结束的完整编码任务。- **支持配置 MCP 工具**：使得编码过程更加贴合开发者的个人工作流程。


**评估回答**


    # 定义评估系统的提示词evaluate_system_prompt = (    "你是一个智能评估系统，负责评估 AI 助手的回答质量。"    "如果 AI 助手的回答与真实答案非常接近，请打 1 分；"    "如果回答错误或与真实答案不相关，请打 0 分；"    "如果回答部分符合真实答案，请打 0.5 分。"    "请直接输出评分结果：0、0.5 或 1。")\#构建评估 prompt 并获取评分evaluation_prompt = f"""用户问题: {query}AI 回答:{answer}真实答案: {ideal_answer}请根据以下标准进行评分：- 如果 AI 回答与真实答案非常接近 → 输出 1- 如果回答错误或不相关 → 输出 0- 如果部分匹配 → 输出 0.5"""evaluation_result = generate_response(evaluate_system_prompt, evaluation_prompt)
    # Step 5: 输出最终评分print("AI 回答评分：", evaluation_result)


    AI 回答评分： 1


二、基于语义的文本分块

在 RAG中，文本分块（Text Chunking）是一个至关重要的环节。其核心作用是将一大段连续文本划分为多个具有语义完整性的较小段落，从而提升信息检索的准确性和整体效果。

传统的分块方式通常采用固定长度的切分策略，例如每500个字符或每若干句子进行一次分割。这种方法虽然实现简单，但在实际应用中容易割裂完整的语义单元，导致后续的信息检索与理解受到影响。

相比之下，一种更智能的分块方法是语义分块（Semantic Chunking）。它不再依据字数或句数进行机械划分，而是通过分析句子之间的内容相似性来判断合适的切分位置。当检测到前后句子在语义上出现明显差异时，就在该位置断开，形成一个新的语义段落。


**切分点的判定方法**


为了找到合适的语义切分点，我们可以借助以下几种常见的统计方法：

1.百分位法（Percentile）找出所有相邻句子之间语义相似度差异的"第 X 百分位数"，并在那些差异值超过该阈值的位置进行切分。

2.标准差法（Standard Deviation）当句子间的语义相似度下降幅度超过平均值减去 X 倍标准差时，在该位置进行切分。

3.四分位距法（IQR, Interquartile Range）利用上下四分位数之差（Q3 - Q1）来识别变化较大的位置，并将其作为潜在的切分点。


**实际应用示例**


在本次实践中，我们采用的是\*\*百分位法（Percentile）\*\*来进行语义分块，并在一个样本文本上测试其分块效果。


**创建句子级别的 Embedding**


首先，将一段原始文本按句子为单位进行初步切分，然后为每一个句子生成对应的向量表示（Embedding），以便后续计算句子之间的语义相似性。

    # 初始化客户端client = OpenAI(    api_key=os.getenv("DASHSCOPE_API_KEY"),  # 如果您没有配置环境变量，请在此处用您的API Key进行替换    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1"  # 百炼服务的base_url)
    # 创建文本块的嵌入向量def create_embeddings(texts, model="text-embedding-v3"):    """    输入一组文本（字符串或列表），返回对应的嵌入向量列表    """    if isinstance(texts, str):        texts = [texts]  # 确保输入为列表形式
        completion = client.embeddings.create(        model=model,        input=text_chunks,        encoding_format="float"    )        # 将响应转换为 dict 并提取所有 embedding    data = json.loads(completion.model_dump_json())    embeddings = [item["embedding"] for item in data["data"]]    return embeddings

    # 将文本按句号进行初步切分为句子sentences = extracted_text.split("。")# 去除空字符串和前后空格sentences = [sentence.strip() for sentence in sentences if sentence.strip()]
    # 批量生成所有句子的嵌入向量（推荐做法）embeddings = create_embeddings(sentences)
    print(f"成功生成 {len(embeddings)} 个句子的嵌入向量。")


成功生成 5 个句子的嵌入向量。


**计算相似度差异**


我们通过计算连续句子之间的余弦相似度（Cosine Similarity），来衡量它们在语义上的接近程度。

    import numpy as npfrom sklearn.metrics.pairwise import cosine_similarity
    def cosine_similarity(vec1, vec2):    """    计算两个向量之间的余弦相似度。
        参数:    vec1(np.ndarray): 第一向量。    vec2(np.ndarray): 第二向量。
        返回:    float: 余弦相似度。        异常:    ValueError: 如果输入向量不是一维数组或形状不匹配。    """    if vec1.ndim != 1or vec2.ndim != 1:        raise ValueError("输入向量必须是一维数组")    if vec1.shape[0] != vec2.shape[0]:        raise ValueError("输入向量必须具有相同的维度")
        return np.dot(vec1, vec2) / (np.linalg.norm(vec1) * np.linalg.norm(vec2))
    # 使用sklearn的cosine_similarity函数计算连续句子之间的相似度similarities = [cosine_similarity(embeddings[i].reshape(1, -1), embeddings[i + 1].reshape(1, -1))[0][0] for i in range(len(embeddings) - 1)]


**实现语义分块**


我们实现了三种不同的方法来识别文本中的切分点（Breakpoints），也就是判断在哪些位置将一段文字切分为多个有意义的段落。

这些方法的核心思想是：基于句子之间的语义相似度变化来决定切分位置。当检测到连续句子之间的语义差异较大时，就认为此处是一个潜在的段落分界点。

    def compute_breakpoints(similarity_scores, method="percentile", threshold=90):    """    根据相似度下降点计算分段断点。
        参数:    similarity_scores(List[float]): 句子之间的相似度列表。    method(str): 阈值计算方法，可选 'percentile', 'standard_deviation', 或 'interquartile'。    threshold(float): 阈值（用于百分位数或标准差法）。
        返回:    List[int]: 应该进行分割的索引位置。    """    # 根据选择的方法确定阈值    if method == "percentile":        # 计算指定百分位数的相似度值作为阈值        threshold_value = np.percentile(similarity_scores, threshold)    elif method == "standard_deviation":        # 计算均值和标准差，并通过减去X个标准差确定阈值        mean = np.mean(similarity_scores)        std_dev = np.std(similarity_scores)        threshold_value = mean - (threshold * std_dev)    elif method == "interquartile":        # 使用四分位距（IQR）规则确定异常值阈值        q1, q3 = np.percentile(similarity_scores, [25, 75])        iqr = q3 - q1        threshold_value = q1 - 1.5 * iqr    else:        # 如果方法无效则抛出错误        raise ValueError("无效方法。请选择 'percentile'、'standard_deviation' 或 'interquartile'。")
        # 找出相似度低于阈值的位置，即分段断点    return [i for i, score in enumerate(similarity_scores) if score < threshold_value]
    # 使用 percentile 方法并设置阈值为 90% 百分位数计算断点breakpoints = compute_breakpoints(similarity_scores=similarities, method="percentile", threshold=90)


**将文本切分为语义块**


接下来我们根据计算出的切分点（Breakpoints），将文本按照其语义内容进行划分。在上一步中，我们已经通过分析句子之间的语义相似度变化，识别出了一些潜在的切分位置。现在，我们将依据这些位置，把原始文本分割为多个具有清晰语义边界的段落，也称为"语义块（Semantic Chunks）"。

    def split_into_chunks(sentence_list, break_indices):    """    将句子列表根据断点索引划分为语义段落。
        参数:    sentence_list(List[str]): 句子列表。    break_indices(List[int]): 表示需要分段的位置索引列表。
        返回:    List[str]: 划分后的语义段落列表。    """    semantic_chunks = []  # 存储划分后的段落    current_start_index = 0  # 当前段起始索引
        # 遍历每个断点以创建段落    for bp in break_indices:        # 将当前段从起始索引连接到断点位置，并添加句号结束        semantic_chunks.append(". ".join(sentence_list[current_start_index:bp + 1]) + ".")        current_start_index = bp + 1  # 更新起始索引为下一个句子
        # 添加最后一个段落（剩余句子）    semantic_chunks.append(". ".join(sentence_list[current_start_index:]))
        return semantic_chunks  # 返回语义段落列表
    # 使用 split_into_chunks 函数生成段落text_chunks = split_into_chunks(sentence_list=sentences, break_indices=breakpoints)
    # 打印生成的段落数量print(f"生成的语义段落数量: {len(text_chunks)}")
    # 打印第一个段落以验证结果print("\n第一个语义段落:")print(text_chunks[0])


    生成的语义段落数量: 4
    第一个语义段落:什么是智能编码助手通义灵码 智能编码助手通义灵码（简称为通义灵码），是由阿里云提供的智能编码辅助工具，提供代码智能生成、智能问答、多文件修改、编程智能体等能力，为开发者带来高效、流畅的编码体验，引领 AI 原生研发新范式. 同时，我们为企业客户提供了企业标准版、专属版，具备企业级场景自定义、私域知识增强等能力，助力企业研发智能化升级.


**为语义块创建嵌入向量**


在完成文本的语义切分之后，接下来我们要为每一个语义块（Semantic Chunk）生成嵌入向量（Embedding），以便于后续的检索和使用。

    # 创建文本块的嵌入向量def create_embeddings(texts, model="text-embedding-v3"):    """    输入一组文本（字符串或列表），返回对应的嵌入向量列表    """    ifisinstance(texts, str):        texts = [texts]  # 确保输入为列表形式
        completion = client.embeddings.create(        model=model,        input=text_chunks,        encoding_format="float"    )        # 将响应转换为 dict 并提取所有 embedding    data = json.loads(completion.model_dump_json())    embeddings = [item["embedding"] for item in data["data"]]    return embeddings


**进行语义搜索**


我们使用余弦相似度（Cosine Similarity） 来检索与查询内容最相关的语义块（Chunks）。

    from sklearn.metrics.pairwise import cosine_similarity
    # 语义搜索函数def semantic_search(query, text_chunks, embeddings=None, k=2):    """    在 text_chunks 中找出与 query 最相关的 top-k 文本块        参数：        query: 查询语句        text_chunks: 候选文本块列表        embeddings: 对应的嵌入向量列表（如果已提前计算）        k: 返回最相关的结果数量            返回：        top_k_chunks: 最相关的 top-k 文本块    """    if embeddings is None:        embeddings = create_embeddings(text_chunks)  # 如果没有提供，则自动生成    else:        assert len(embeddings) == len(text_chunks), "embeddings 和 text_chunks 必须长度一致"
        query_embedding = create_embeddings(query)[0]  # 获取查询的嵌入
        # 计算相似度    similarity_scores = []    for i, chunk_embedding in enumerate(embeddings):        score = cosine_similarity([query_embedding], [chunk_embedding])[0][0]        similarity_scores.append((i, score))
        # 排序并取 top-k    similarity_scores.sort(key=lambda x: x[1], reverse=True)    top_indices = [index for index, _ in similarity_scores[:k]]    return [text_chunks[index] for index in top_indices]


    # 执行语义搜索query = '什么是智能编码助手通义灵码？'top_chunks = semantic_search(query, text_chunks, k=2)
    # 输出结果print("Query:", query)for i, chunk in enumerate(top_chunks):    print(f"Context {i + 1}:\n{chunk}\n=====================================")


    Query: 什么是智能编码助手通义灵码 Context 1:什么是智能编码助手通义灵码 智能编码助手通义灵码（简称为通义灵码），是由阿里云提供的智能编码辅助工具，提供代码智能生成、智能问答、多文件修改、编程智能体等能力，为开发者带来高效、流畅的编码体验，引领 AI 原生研发新范式. 同时，我们为企业客户提供了企业标准版、专属版，具备企业级场景自定义、私域知识增强等能力，助力企业研发智能化升级.=====================================Context 2:核心能力 代码补全 Code Completion 经过海量优秀开源代码数据训练，可根据当前代码文件及跨文件的上下文，为您生成行级/函数级代码、单元测试、代码优化建议等.=====================================


**基于检索到的文本块生成响应**


在完成语义搜索并找到与用户查询最相关的文本块（Chunks）之后，下一步是基于这些检索结果生成回答。

    import osfrom openai import OpenAI
    # 初始化 DashScope 客户端（使用阿里云通义千问）client = OpenAI(    api_key=os.getenv("DASHSCOPE_API_KEY"),  # 确保提前设置好环境变量    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1")
    # 设置系统提示（中文版）SYSTEM_PROMPT = (    "你是一个 AI 助手，必须严格根据提供的上下文内容进行回答。"    "如果无法从提供的上下文中直接得出答案，请回复：'我无法根据现有信息回答这个问题。'")
    def generate_response(system_prompt, user_message, model="qwen-max"):    """    使用 DashScope 的通义千问模型生成基于上下文的回答。
        参数：        system_prompt (str): 控制 AI 行为的系统指令        user_message (str): 用户输入的问题及上下文        model (str): 使用的模型名称，默认为 qwen-plus
        返回：        str: 模型生成的回答内容    """    response = client.chat.completions.create(        model=model,        temperature=0.0,  # 温度设为0，保证输出确定性        max_tokens=512,   # 可按需调整最大输出长度        messages=[            {"role": "system", "content": system_prompt},            {"role": "user", "content": user_message}        ]    )        return response.choices[0].message.content.strip()


三、在 RAG 中引入"上下文增强检索"

传统的方法存在一个明显的问题：它只返回一个个孤立的文本块，这些文本块之间缺乏上下文联系，有时会导致 AI 获取的信息不完整，从而出现回答错误或内容不全面的情况。

为了解决这个问题，我们提出了一种新的方法，叫做 "上下文增强检索"（Context-Enriched Retrieval）。 它的核心思想是： 不只是找出一个最相关的文本块，而是同时返回它的前一个和后一个文本块，帮助 AI 更好地理解上下文，从而生成更准确、更完整的回答。

整个流程主要包括以下几个步骤：

1.数据导入（Data Ingestion）从 PDF 文件中提取原始文字内容。

2.带上下文的分块（Chunking with Overlapping Context）将大段文字划分为多个小块，但每个文本块与前后内容有一定的重叠。 👉 这样做的目的是确保即使某句话被切分到两个文本块之间，在其中一个块中也能看到完整的上下文。

3.创建嵌入向量（Embedding Creation）将每个文本块转换为一组数字表示（称为"嵌入向量"），便于后续进行相似度计算。 👉 可以理解为给每个文本块打上"语义标签"，这样就能快速找到语义相近的内容。

4.上下文感知的检索（Context-Aware Retrieval）当用户提问时，系统不仅会找到最相关的那个文本块，还会一并返回其前后的文本块。 👉 这样 AI 在回答问题时能获得更丰富的背景信息，避免断章取义。

5.生成回答（Response Generation）使用大语言模型（如 Llama、ChatGLM 等），基于包含上下文的检索结果生成自然、准确的回答。 👉 就像你在考试时可以翻书找答案，而且还能看到那一页的前后内容，自然就能答得更准确。

6.评估效果（Evaluation）最后，我们会对 AI 的回答进行评估，判断是否因引入上下文而提升了回答的准确性与完整性。 👉 比如可以通过人工评分，或者让另一个 AI 来评估回答的质量。


**实现上下文感知的语义搜索**


在原有的语义搜索基础上进行了改进：在检索过程中，不仅返回最相关的文本块，还同时返回其相邻的前后文本块，从而提供更完整、更有上下文支持的信息。

    def context_enriched_search(search_query, chunked_texts, chunk_embeddings, top_k=1, context_window_size=1):    """    在搜索时不仅返回最相关的段落，还包含它前后的上下文段落，以提供更丰富的背景信息。
        参数:        search_query(str): 用户的查询语句。        chunked_texts(List[str]): 文本被切分后的段落列表。        chunk_embeddings(List[dict]): 每个文本段落对应的向量表示（通常是从 embedding 模型得到的）。        top_k(int): 要检索的相关段落数量（这里只用 top 1 来找中心段落）。        context_window_size(int): 要包含的上下文段落数量（前后各取几个）。
        返回:        List[str]: 包含最相关段落及其上下文的文本段落列表。    """
        # 第一步：将用户的问题转换为一个向量（embedding），用于和文本段落做相似度比较    query_embedding = create_embeddings(search_query).data[0].embedding
        similarity_list = []  # 用于存储每个段落与问题的相似度分数和其索引
        # 第二步：遍历所有段落的向量，计算它们与问题向量之间的余弦相似度    for i, chunk_embedding in enumerate(chunk_embeddings):        # 使用 cosine_similarity 函数计算相似度（越接近1越相似）        similarity_score = cosine_similarity(np.array(query_embedding), np.array(chunk_embedding.embedding))        # 把该段落的索引和相似度保存下来，如：(0, 0.75)        similarity_list.append((i, similarity_score))
        # 第三步：根据相似度对所有段落进行排序，从高到低排列    similarity_list.sort(key=lambda x: x[1], reverse=True)
        # 第四步：获取最相关的那个段落的索引（即排在第一位的段落）    most_relevant_index = similarity_list[0][0]  # 如：第3个段落
        # 第五步：确定要提取的上下文范围（包括当前段落 + 前后 context_window_size 个段落）    start_index = max(0, most_relevant_index - context_window_size)  # 防止超出开头    end_index = min(len(chunked_texts), most_relevant_index + context_window_size + 1)  # 防止超出结尾
        # 第六步：返回包含上下文的段落列表    return [chunked_texts[i] for i in range(start_index, end_index)]


四、添加"块标题"（Contextual Chunk Headers，CCH）

RAG 通过在生成回答之前从外部知识库中检索相关信息，从而提升语言模型的事实准确性。然而，在传统的文本分块方法中，往往会丢失重要的上下文信息，导致检索效果不佳，甚至使模型生成脱离上下文的回答。

为了解决这个问题，我们引入了一种改进方法：上下文块标题（Contextual Chunk Headers, 简称 CCH）。 这个方法的核心思想是： 在将文本分成小块（chunk）时，将该段内容所属的高级上下文信息（如文档标题、章节标题等）一并加到每个文本块的开头，然后再进行嵌入和检索。 这样做可以让每个文本块都带有其背景信息，帮助模型更好地理解它属于哪个部分，从而提高检索的相关性，并避免模型基于断章取义的内容生成错误答案。


**本方法中的步骤如下：**


1.数据导入（Data Ingestion）加载并预处理原始文本数据。

2.带上下文标题的分块（Chunking with Contextual Headers）自动识别文档中的章节标题，并将这些标题加到对应段落的前面，形成带有上下文的文本块。👉 例如：

    # 第三章：人工智能的基本技术人工智能的核心方法包括机器学习、深度学习和自然语言处理...


3.创建嵌入向量（Embedding Creation）将这些带有上下文信息的文本块转换成数字形式（即嵌入向量），以便后续进行语义搜索。

4.语义搜索（Semantic Search）当用户提出问题时，系统会基于这些增强后的文本块，找到最相关的内容。

5.生成回答（Response Generation）使用大语言模型（如 Llama、ChatGLM 等）基于检索结果生成自然、准确的回答。

6.评估效果（Evaluation）通过评分系统对 AI 的回答进行评估，检查加入上下文标题后是否提升了回答的准确性和相关性。

*** ** * ** ***


**使用上下文标题对文本进行分块**


为了提升信息检索的效果，我们使用大语言模型（LLM）为每一个文本块自动生成一个描述性的标题（Header），并将其加在该文本块的前面。

    def generate_chunk_header(text_chunk, model_name="qwen-max"):    """    使用大语言模型（LLM）为给定文本段落生成一个标题/摘要。
        参数:        text_chunk(str): 需要生成标题的文本段落。        model_name(str): 用于生成标题的语言模型名称，默认为 "qwen-max"。
        返回:        str: 由模型生成的标题或摘要内容。    """
        # 定义系统提示词，指导 AI 的行为    header_system_prompt = "请为以下文本生成一个简洁且具有信息量的标题。"
        # 调用 LLM 模型生成基于系统提示词和输入文本的响应    llm_response = client.chat.completions.create(        model=model_name,        temperature=0,        messages=[            {"role": "system", "content": header_system_prompt},            {"role": "user", "content": text_chunk}        ]    )
        # 提取并返回模型生成的内容，去除前后多余的空白字符    return llm_response.choices[0].message.content.strip()


    def chunk_text_with_headers(input_text, chunk_size, overlap_size):    """    将输入文本分割为较小的段落并为每个段落生成标题。
        参数:        input_text(str): 需要分割的完整文本。        chunk_size(int): 每个段落的大小（字符数）。        overlap_size(int): 相邻段落之间的重叠字符数。
        返回:        List[dict]: 包含 'header' 和 'text' 键的字典列表，分别表示段落的标题和内容。    """        text_chunks = []  # 初始化一个空列表，用于存储带有标题的文本段落
        # 使用指定的段落大小和重叠长度遍历文本    for start_index in range(0, len(input_text), chunk_size - overlap_size):        current_chunk = input_text[start_index:start_index + chunk_size]  # 提取当前段落        chunk_header = generate_chunk_header(current_chunk)  # 使用大语言模型生成段落标题        text_chunks.append({"header": chunk_header, "text": current_chunk})  # 将标题和段落内容一起添加到列表中
        return text_chunks  # 返回包含标题和内容的段落列表


**为标题和正文创建embedding向量**


为了提升信息检索的准确性，我们不仅对正文内容生成Embedding，同时也对每个文本块前面的标题（Header）生成嵌入向量。

    # 为每个文本块生成嵌入向量chunk_embeddings = []  # 初始化一个空列表，用于存储带有标题、文本及其嵌入向量的字典
    # 遍历每个文本块并生成嵌入向量（带进度条）for current_chunk in tqdm(text_chunks, desc="生成嵌入向量"):    # 获取当前文本块的文本内容，并生成其嵌入向量    text_embedding = create_embeddings(current_chunk["text"])        # 获取当前文本块的标题，并生成其嵌入向量    header_embedding = create_embeddings(current_chunk["header"])        # 将当前文本块的标题、文本及其对应的嵌入向量存入列表中    chunk_embeddings.append({        "header": current_chunk["header"],        "text": current_chunk["text"],        "embedding": text_embedding,        "header_embedding": header_embedding    })


**语义检索**


    import numpy as np
    def _calculate_similarity(query_vec, chunk_vec):    """    计算查询向量与块向量之间的余弦相似度。        参数:    query_vec (np.array): 查询的嵌入向量。    chunk_vec (np.array): 文本块的嵌入向量。        返回:    float: 余弦相似度。    """    return cosine_similarity(np.array(query_vec), np.array(chunk_vec))
    def semantic_search(query, chunks, top_k=5):    """    根据查询语义搜索最相关的文本块。        参数:    query (str): 用户输入的查询语句。    chunks (List[dict]): 包含嵌入向量的文本块列表。    top_k (int): 需要返回的最相关结果的数量。        返回:    List[dict]: 最相关的前top_k个文本块。    """    # 生成查询语句的向量表示    query_vector = create_embeddings(query)
        # 初始化一个列表用于存储每个文本块及其相似度    chunk_similarity_pairs = []
        # 遍历每个文本块并计算相似度    for chunk in chunks:        text_vector = chunk["embedding"]     # 获取文本内容的嵌入向量        header_vector = chunk["header_embedding"]  # 获取标题的嵌入向量
            # 分别计算查询与文本、标题的相似度，并取平均        similarity_text = _calculate_similarity(query_vector, text_vector)        similarity_header = _calculate_similarity(query_vector, header_vector)        avg_similarity = (similarity_text + similarity_header) / 2
            # 存储文本块及其平均相似度        chunk_similarity_pairs.append((chunk, avg_similarity))
        # 按照相似度从高到低排序    chunk_similarity_pairs.sort(key=lambda pair: pair[1], reverse=True)
        # 返回最相关的 top-k 个文本块    return [pair[0] forpair in chunk_similarity_pairs[:top_k]]


五、基于问题生成的RAG

本节通过在文档处理阶段引入问题生成（Question Generation），对文档内容进行增强。

我们为每个文本块生成相关的提问，从而提升信息检索的效果，最终帮助语言模型生成更准确、更相关的回答。

这种方法的核心思想是： 在传统的 RAG（Retrieval-Augmented Generation）中，我们通常只将文本块嵌入后存入向量库。而在这一改进方法中，我们还为每个文本块自动生成一些相关的问题，并将这些问题也进行嵌入。这样，在用户提问时，系统可以更好地理解哪些文本块与问题最相关，从而提高检索效果和回答质量。

实现步骤如下：

1.数据导入（Data Ingestion）从 PDF 文件中提取原始文本内容。

2.文本分块（Chunking）将大段文字切分成小块，便于后续处理。 👉 每个块通常包含 200\~300 字左右的内容。

3.问题生成（Question Generation）使用大语言模型（LLM），为每个文本块自动生成几个与该段内容相关的问题。 👉 例如，输入一段关于"机器学习"的内容，输出可能是：

* "什么是机器学习？"

<!-- -->

* "机器学习有哪些常见算法？"

<!-- -->

* "机器学习和人工智能有什么关系？"

4.创建嵌入向量（Embedding Creation）对每个文本块及其对应的问题分别生成嵌入向量（即转化为数字表示），以便进行语义匹配。

5.构建向量数据库（Vector Store Creation）使用 NumPy 构建一个简单的向量数据库，用来存储所有文本块和问题的嵌入向量。

6.语义搜索（Semantic Search）当用户提出问题时，系统会先查找与其问题最相似的生成问题（generated questions），然后找到对应的文本块作为上下文。

7.生成回答（Response Generation）基于检索到的相关文本块，让语言模型生成自然、准确的回答。

8.评估效果（Evaluation）最后，我们会对生成的回答进行评分，评估这种增强型 RAG 是否提升了回答的质量和准确性。


**为文本块生成问题**


为每一个文本块自动生成一些相关问题------也就是那些可以通过这段文字找到答案的问题。

    import re
    def _extract_questions_from_response(response_text):    """    从模型返回的文本中提取出以问号结尾的问题。
        参数:    response_text (str): 模型返回的原始文本。
        返回:    List[str]: 清洗后的有效问题列表。    """    questions = []    for line in response_text.split('\n'):        cleaned_line = line.strip()  # 去除前后空格        if cleaned_line:            # 去除可能存在的编号前缀（如 "1.", "2)", "•", "-" 等）            cleaned_line = re.sub(r'^[\d\-\•\*]+\s*[\.\\)]?\s*', '', cleaned_line)            # 判断是否含有问号（中英文都支持）            if '?' in cleaned_line or '？' in cleaned_line:                # 统一转为英文问号结尾                question = cleaned_line.rstrip('?').rstrip('？') + '?'                questions.append(question)    return questions

    def generate_questions(text, question_count=5, model="qwen-max"):    """    根据提供的文本块生成可回答的问题。
        参数:    text (str): 需要生成问题的文本内容。    question_count (int): 需要生成的问题数量。    model (str): 用于生成问题的语言模型名称。
        返回:    List[str]: 生成的问题列表。    """    # 系统指令：定义 AI 的行为准则    system_instruction = "你是一个擅长从文本中生成相关问题的专家。请仅使用提供的文本创建简洁的问题，关注关键信息和概念。"
        # 用户请求模板：提供具体任务和格式要求    user_request = f"""    请基于以下文本生成 {question_count} 个不同的问题，这些问题必须能通过该文本来回答：
        {text}
        请以数字编号列表的形式输出问题，不要添加其他内容。    """
        # 调用大模型 API 生成问题    response = client.chat.completions.create(        model=model,        temperature=0.7,        messages=[            {"role": "system", "content": system_instruction},            {"role": "user", "content": user_request}        ]    )
        # 提取原始响应内容并去除前后空格    raw_questions_text = response.choices[0].message.content.strip()
        # 使用辅助函数提取并过滤有效问题    filtered_questions = _extract_questions_from_response(raw_questions_text)
        return filtered_questions


**构建一个简单的向量存储库**


我们将使用 NumPy 来实现一个简单的向量存储（Vector Store）。

    import numpy as npfrom typing import List, Dict, Optional

    classSimpleVectorStore:    """    简单的基于 NumPy 的向量存储实现。    """
        def __init__(self):        """        初始化向量数据库，包含向量、文本和元数据列表。        """        self.vectors: List[np.ndarray] = []   # 存储向量        self.texts: List[str] = []            # 存储原始文本        self.metadata_list: List[Dict] = []    # 存储元信息        def add_item(self, text: str, vector: List[float], metadata: Optional[Dict] = None):        """        向向量库中添加一个条目。
            参数:        text (str): 原始文本内容。        vector (List[float]): 向量嵌入表示。        metadata (Dict, optional): 可选的元数据信息。        """        self.vectors.append(np.array(vector))        self.texts.append(text)        self.metadata_list.append(metadata or {})        def similarity_search(self, query_vector: List[float], top_k: int = 5) -> List[Dict]:        """        根据查询向量在向量库中查找最相似的 top_k 条记录。
            参数:        query_vector (List[float]): 查询向量。        top_k (int): 返回的结果数量。
            返回:        List[Dict]: 包含相似文本、元数据和相似度得分的字典列表。        """        ifnot self.vectors:            return []                # 将查询向量转换为 numpy 数组        query_array = np.array(query_vector)                # 计算每个向量与查询向量的余弦相似度        similarities = []        for idx, vector in enumerate(self.vectors):            similarity = np.dot(query_array, vector) / (                np.linalg.norm(query_array) * np.linalg.norm(vector)            )            similarities.append((idx, similarity))                # 按照相似度降序排序        similarities.sort(key=lambda x: x[1], reverse=True)                # 构建结果返回        results = []        for i in range(min(top_k, len(similarities))):            idx, score = similarities[i]            results.append({                "text": self.texts[idx],                "metadata": self.metadata_list[idx],                "similarity_score": float(score)            })                return results


**使用问题增强来处理文档**


现在，我们将前面的所有步骤整合在一起，对文档进行完整处理：包括为文本块生成相关问题、创建embedding，并构建一个增强型的向量存储库（Augmented Vector Store）。

    def process_document(pdf_path, chunk_size=1000, chunk_overlap=200, questions_per_chunk=5):    """    对文档进行处理并生成问题增强。
        参数:    pdf_path(str): PDF 文件路径。    chunk_size(int): 每个文本块的字符数。    chunk_overlap(int): 文本块之间的重叠字符数。    questions_per_chunk(int): 每个文本块生成的问题数量。
        返回:    Tuple[List[str], SimpleVectorStore]: 处理后的文本块和向量存储。    """    print("从PDF中提取文本...")    extracted_text = extract_text_from_pdf(pdf_path)
        print("分割文本为块...")    text_chunks = chunk_text(extracted_text, chunk_size, chunk_overlap)    print(f"共创建 {len(text_chunks)} 个文本块")
        vector_store = SimpleVectorStore()
        print("处理每个文本块并生成相关问题...")    for idx, chunk in enumerate(tqdm(text_chunks, desc="正在处理文本块")):        # 为当前文本块生成嵌入        chunk_embedding_response = create_embeddings(chunk)        chunk_embedding = chunk_embedding_response.data[0].embedding
            # 将文本块添加到向量库中        vector_store.add_item(            text=chunk,            vectors=chunk_embedding,            metadata={"type": "chunk", "index": idx}        )
            # 为当前文本块生成多个问题        questions = generate_questions(chunk, num_questions=questions_per_chunk)
            # 为每个问题生成嵌入，并加入向量库        for q_idx, question in enumerate(questions):            question_embedding_response = create_embeddings(question)            question_embedding = question_embedding_response.data[0].embedding
                # 将问题添加到向量库            vector_store.add_item(                text=question,                vectors=question_embedding,                metadata={"type": "question", "chunk_index": idx, "original_chunk": chunk}            )
        return text_chunks, vector_store


**提取与处理文档**


    # 定义PDF文件路径pdf_file_path = "knowledge_base/智能编码助手通义灵码.pdf"
    # 处理文档（提取文本、生成块、创建问题、构建向量库）text_chunks, vector_store = process_document(    pdf_file_path,    chunk_size=1000,    chunk_overlap=100,    questions_per_chunk=3)
    # 输出向量库中的条目数量print(f"向量库包含 {len(vector_store.texts)} 个条目")


**在增强型向量库上进行查询**


    import json
    search_query = '通义灵码是由哪家公司的智能编码辅助工具?'
    # 使用语义搜索查找相关内容search_results = semantic_search(search_query, vector_store, k=5)
    print("查询内容:", search_query)print("\n搜索结果:")
    # 按类型分类结果document_chunks = []matched_questions = []
    for result in search_results:    if result["metadata"]["type"] == "chunk":        document_chunks.append(result)    else:        matched_questions.append(result)
    # 打印文档片段print("\n相关文档片段:")for index, result in enumerate(document_chunks):    print(f"上下文 {index + 1} (相似度: {result['similarity']:.4f}):")    print(result["text"][:300] + "...")    print("=====================================")
    # 打印匹配的问题print("\n匹配的问题:")for index, result in enumerate(matched_questions):    print(f"问题 {index + 1} (相似度: {result['similarity']:.4f}):")    print(result["text"])    chunk_index = result["metadata"]["chunk_index"]    print(f"来自片段 {chunk_index}")    print("=====================================")


    查询内容: 通义灵码是由哪家公司的智能编码辅助工具?
    匹配的问题:问题 1 (相似度: 0.9770):通义灵码是由哪家公司提供的智能编码辅助工具，它主要提供哪些能力?来自片段 0=====================================问题 2 (相似度: 0.8629):除了个人开发者外，通义灵码还为企业提供了哪些版本及特色服务?来自片段 0=====================================问题 3 (相似度: 0.8108):通义灵码提供了哪几种企业版方案供客户选择?来自片段 1=====================================问题 4 (相似度: 0.8078):通义灵码的代码补全功能是如何工作的，它能够为开发者生成什么样的代码建议?来自片段 0=====================================


六、Query改写

本节实现了三种查询转换（Query Transformation），以提升检索增强生成（RAG）系统的信息检索效果。

核心目标：

通过修改或扩展用户的原始查询，帮助系统更准确地理解用户意图，并从向量库中找到更相关的信息。


**三大查询转换技巧**


\#\#\## 1. 查询重写（Query Rewriting）

将用户的问题变得更具体、更详细，从而提高检索的精准度。

🔹 示例：

* 用户原问题："AI 是什么？"

<!-- -->

* 重写后的问题："人工智能的定义及其核心技术有哪些？"

✅ 提升点：让搜索更精确，避免过于宽泛的结果。

*** ** * ** ***

\#\#\## 2. 回退提问（Step-back Prompting）

生成一个更广泛、更高层次的问题，用于获取更多背景信息，帮助系统更好地理解上下文。

🔹 示例：

* 用户原问题："深度学习在医疗领域有哪些应用？"

<!-- -->

* 回退问题："人工智能在医疗行业的应用有哪些？"

✅ 提升点：有助于找到与问题相关但不直接匹配的重要背景知识。

*** ** * ** ***

\#\#\## 3. 子查询拆解（Sub-query Decomposition）

将一个复杂的问题拆分成多个更简单的小问题，分别进行检索，最后综合所有结果，提供更全面的回答。

🔹 示例：

* 用户原问题："比较机器学习和深度学习的优缺点及应用场景。"

<!-- -->

* 拆解为：

<!-- -->

* "什么是机器学习？"

* "什么是深度学习？"

* "机器学习有哪些优缺点？"

* "深度学习有哪些优缺点？"

* "它们各自适用于哪些场景？"

✅ 提升点：确保覆盖问题的所有方面，避免遗漏关键信息。


**实现查询转换技术**


1.查询重写（Query Rewriting）

在很多情况下，用户提出的问题可能比较模糊或简短，例如：

"AI 是什么？"

这种提问虽然明确，但不够具体，系统在向量库中搜索时可能会返回过于宽泛或不相关的结果。

查询重写的作用就是根据原始问题的意图，生成一个更清晰、更详细的版本，帮助系统找到更相关的信息。

    def rewrite_query(original_query, model="qwen-max"):    """    重写用户查询，使其更具体和详细，以提高检索效果。        参数:        original_query(str): 用户原始查询语句        model(str): 用于改写的模型名称            返回:        str: 经过优化的查询语句    """    # 系统提示词：指导AI助手行为    system_prompt = "你是一个擅长优化搜索查询的AI助手。你的任务是将用户的查询语句改写得更加具体、详细，并有助于获取相关的信息。"
        # 用户提示词：提供需要重写的原始查询    user_prompt = f"""    请将以下查询语句进行改写，使其更加具体并包含有助于精准检索的相关术语和概念。
        原始查询: {original_query}
        改写后的查询:    """
        # 使用指定模型生成改写结果    response = client.chat.completions.create(        model=model,        temperature=0.0,  # 温度设为0，确保输出稳定        messages=[            {"role": "system", "content": system_prompt},            {"role": "user", "content": user_prompt}        ]    )
        # 返回改写后的查询内容，并去除首尾空格    return response.choices[0].message.content.strip()


2. 回退提问（Step-back Prompting）

目标是生成更宽泛、更高层次的问题，用于检索与用户问题相关的背景信息。

*** ** * ** ***


**什么是"回退提问"？**


在很多情况下，用户提出的问题可能非常具体，例如：

"深度学习在医疗影像诊断中的应用有哪些？"

这个问题虽然明确，但太聚焦，可能导致系统只检索到非常局部的信息，而忽略了重要的上下文背景。

"回退提问"的思路是：  

先"后退一步"，提出一个更广泛的问题，比如：

"人工智能在医疗行业中的应用有哪些？"

这样可以让系统先获取一些整体背景知识，帮助更好地理解当前问题所处的语境，从而提升最终回答的准确性和完整性。

    def generate_step_back_query(original_query, model="qwen-max"):    """    生成一个更通用的"后退一步"查询，以获取更广泛的上下文信息。        参数:        original_query(str): 用户原始查询语句        model(str): 用于生成查询的模型名称            返回:        str: 更宽泛的背景查询语句    """    # 系统提示词：指导AI助手行为    system_prompt = "你是一个擅长搜索策略的AI助手。你的任务是将具体查询扩展为更通用的形式，以获取相关的背景信息。"
        # 用户提示词：提供需要泛化的原始查询    user_prompt = f"""    请根据以下具体查询生成一个更宽泛、更具概括性的版本，以便获取有用的背景知识。
        原始查询: {original_query}
        后退一步的查询:    """
        # 使用指定模型生成更宽泛的查询语句    response = client.chat.completions.create(        model=model,        temperature=0.1,  # 温度略高一点，增加多样性        messages=[            {"role": "system", "content": system_prompt},            {"role": "user", "content": user_prompt}        ]    )
        # 返回生成的查询内容，并去除首尾空格    return response.choices[0].message.content.strip()


3. 子查询拆解（Sub-query Decomposition）

目标是将复杂的用户问题拆分成多个更简单、更具体的子问题，从而实现更全面的信息检索。

*** ** * ** ***


**什么是子查询拆解？**


当用户提出一个比较复杂或包含多个部分的问题时，例如：

"请比较机器学习和深度学习的原理、优缺点以及应用场景。"

如果直接用这个问题去搜索，系统可能很难找到完全匹配的内容，导致信息不全或回答不够准确。

子查询拆解的思路是：  

把这个问题拆成几个更小、更容易处理的部分，分别进行检索，最后综合所有结果来生成完整回答。

示例说明：

    def decompose_query(original_query, num_subqueries=4, model="qwen-max"):    """    将复杂查询拆解为更简单的子查询。
        参数:        original_query(str): 原始的复杂查询内容        num_subqueries(int): 要生成的子查询数量        model(str): 用于分解查询的模型名称
        返回:        List[str]: 拆分后的子查询列表    """    # 系统提示词：指导AI助手的行为逻辑    system_prompt = "你是一个擅长分解复杂问题的AI助手。你的任务是将复杂的查询分解成多个简单的问题，这些子问题的答案共同构成原始问题的答案。"
        # 用户提示词：提供需要分解的原始查询    user_prompt = f"""    将以下复杂查询分解为 {num_subqueries} 个更简单的子查询。每个子查询应关注原始问题的不同方面。
        原始查询: {original_query}
        请按如下格式输出结果：    1. [第一个子查询]    2. [第二个子查询]    ...    """
        # 使用指定模型生成子查询    response = client.chat.completions.create(        model=model,        temperature=0.2,  # 温度略高一点，增加多样性        messages=[            {"role": "system", "content": system_prompt},            {"role": "user", "content": user_prompt}        ]    )
        # 提取并处理响应内容    content = response.choices[0].message.content.strip()
        # 按行分割响应内容    lines = content.split("\n")    sub_queries = []
        # 解析每一行，提取编号后的子查询    for line in lines:        if line.strip() and any(line.strip().startswith(f"{i}.") for i in range(1, 10)):            query = line.strip()            query = query[query.find(".") + 1:].strip()  # 去除序号部分，保留实际内容            sub_queries.append(query)
        return sub_queries


七、重排序（Reranking）

重排序是在初步检索结果的基础上进行的第二轮筛选与优化步骤，目的是确保最终用于生成回答的内容是最相关、最准确的部分。

在传统的语义搜索中，我们通常使用向量相似度（如余弦相似度）来找到最相关的文本块。但这种"初步检索"并不总是完美的，有时会返回一些看似相关但实际上不匹配的内容。

重排序的作用就是：

✅ 在初步检索结果中进一步筛选；

✅ 使用更精确的相关性评分模型对内容重新打分；

✅ 按照实际相关性重新排序；

✅ 只保留最相关的文档用于后续的回答生成。


**重排序的核心流程**


\#\#\## 1. 初步检索（Initial Retrieval）

* 使用基础的语义相似度搜索（如向量匹配）快速获取一批候选文本块；

<!-- -->

* 这一步速度快，但准确性有限。

\#\#\## 2. 文档评分（Document Scoring）

* 对每个检索到的文档进行更深入的相关性评估；

<!-- -->

* 可以使用专门的重排序模型（如 BERT reranker、ColBERT、Cross-Encoder 等），根据用户查询和文档内容之间的语义关系打分；

<!-- -->

* 相比简单的向量匹配，这种方式能更好地理解"句子层面"的相关性。

\#\#\## 3. 重新排序（Reordering）

* 根据评分结果对所有候选文档进行重新排序；

<!-- -->

* 最相关的排在最前面，最不相关的被靠后或剔除。

\#\#\## 4. 内容选择（Selection）

* 只选取排名靠前的几个文档作为上下文提供给语言模型；

<!-- -->

* 避免引入噪音信息，提高回答的准确性和可靠性。


**举个例子：**


假设用户问："深度学习有哪些主要应用？"

初步检索可能返回以下三个段落：

1."深度学习广泛应用于图像识别和自然语言处理。"

2."机器学习可以分为监督学习和无监督学习两种方式。"

3."卷积神经网络是一种常用于图像分类的深度学习模型。"

通过重排序，我们可以判断：

* 第1条高度相关 ✅

<!-- -->

* 第2条不太相关 ❌

<!-- -->

* 第3条部分相关 ✅

于是我们只保留第1条和第3条作为上下文，用来生成最终答案。


**基于大模型的重排序**


    def rerank_with_llm(query, search_results, top_n=3, model="qwen-max"):    """    使用LLM对搜索结果进行重新排序。    参数:        query(str): 用户查询语句。        search_results(List[Dict]): 初始搜索结果列表，每个元素包含文档文本、元数据和相似度分数。        top_n(int): 重新排序后返回的文档数量。        model(str): 用于评分的LLM模型名称。    返回:        List[Dict]: 按相关性评分排序后的文档列表。    """    print(f"正在对 {len(search_results)} 个文档进行重新排序...")    scored_results = []  # 存储带有相关性评分的结果    # 定义系统提示词，指导LLM如何评分    system_prompt = """你是一个评估文档与搜索查询相关性的专家。你的任务是根据文档回答给定查询的相关程度，在0到10之间对文档进行评分。评分指南：- 0-2分：文档完全不相关- 3-5分：文档有一些相关信息，但不能直接回答查询- 6-8分：文档相关且能部分回答查询- 9-10分：文档高度相关且能直接回答查询请只输出一个整数分数（0到10）作为评分，不要包含其他内容。"""    # 遍历每个搜索结果    for idx, result in enumerate(search_results):        if idx % 5 == 0:            print(f"正在评分第 {idx + 1}/{len(search_results)} 个文档...")        # 构建用户提示词，输入查询和文档内容        user_prompt = f"""查询: {query}文档内容:{result['text']}请根据上述查询对该文档的相关性进行评分（0-10）:"""        # 调用LLM接口获取评分        response = client.chat.completions.create(            model=model,            temperature=0,            messages=[                {"role": "system", "content": system_prompt},                {"role": "user", "content": user_prompt}            ]        )        # 提取评分结果        score_text = response.choices[0].message.content.strip()        # 使用正则表达式提取数字评分        score_match = re.search(r'\b(10|[0-9])\b', score_text)        if score_match:            relevance_score = float(score_match.group(1))        else:            # 如果无法提取评分，则使用相似度得分作为备选方案            print(f"警告：无法从响应中提取评分: '{score_text}'，改用相似度评分")            relevance_score = result["similarity"] * 10        # 将评分结果添加到列表中        scored_results.append({            "text": result["text"],            "metadata": result["metadata"],            "similarity": result["similarity"],            "relevance_score": relevance_score        })    # 根据相关性评分对结果进行降序排序    reranked_results = sorted(scored_results, key=lambda x: x["relevance_score"], reverse=True)    # 返回前top_n个结果    return reranked_results[:top_n]


**基于关键词的重排序**


    def rerank_with_keywords(query, doc_results, top_n=3):    """    一个基于关键词匹配和位置的简单重排序方法。    Args:        query(str): 用户查询的问题        doc_results(List[Dict]): 初始搜索结果，每个字典包含文本和其他元数据        top_n(int): 重排序后要返回的结果数量，默认是前3个    Returns:        List[Dict]: 按相关性重新排序后的结果，只保留前 top_n 个    """    def extract_keywords(text):        """从文本中提取关键词"""        return [word.lower()for word in text.split()iflen(word) > 3]    # 从用户问题中提取重要关键词    keywords = extract_keywords(query)    ranked_docs = []  # 创建一个列表来存储评分后的文档    for doc_result in doc_results:        document_text = doc_result["text"].lower()  # 将文档文本转换为小写，方便后续比较        # 基础分从向量相似度开始，乘以0.5表示它不是唯一决定因素        base_score = doc_result["similarity"] * 0.5        # 初始化关键词得分        keyword_score = 0        for keyword in keywords:            if keyword in document_text:                # 如果找到了某个关键词，则加0.1分                keyword_score += 0.1                # 如果关键词出现在文档前1/4的位置，说明更可能直接回答问题，再加0.1分                first_position = document_text.find(keyword)                if first_position < len(document_text) / 4:  # 在前四分之一的位置                    keyword_score += 0.1                # 根据关键词出现的次数加分，但最多只能加到0.2分                frequency = document_text.count(keyword)                keyword_score += min(0.05 * frequency, 0.2)  # 最多加0.2分        # 计算最终得分：基础分加上关键词得分        final_score = base_score + keyword_score        # 将这条文档及其相关信息和得分存入列表        ranked_docs.append({            "text": doc_result["text"],            "metadata": doc_result["metadata"],            "similarity": doc_result["similarity"],            "relevance_score": final_score        })    # 对所有文档按照最终的相关性得分进行降序排列    reranked_docs = sorted(ranked_docs, key=lambda x: x["relevance_score"], reverse=True)    # 返回前 top_n 条最高得分的文档    return reranked_docs[:top_n]


**带有重排序的完整 RAG 流程**


到目前为止，我们已经实现了 RAG流程中的核心模块，包括：

* 文档处理（Document Processing）

<!-- -->

* 问答生成（Question Answering）

<!-- -->

* 结果重排序（Reranking）

现在，我们将这些模块整合在一起，构建一个完整的 RAG 系统流程。  

    def rag_with_reranking(query, vector_store, reranking_method="llm", top_n=3, model="qwen-max"):    """    完整的 RAG 管道，包含重新排序。        参数:        query(str): 用户查询语句        vector_store(SimpleVectorStore): 向量数据库        reranking_method(str): 重排序方法 ('llm' 或 'keywords')        top_n(int): 重排序后返回的结果数量        model(str): 用于生成回答的模型            返回:        Dict: 包含查询、上下文和回答的结果字典    """    # 创建查询嵌入向量    query_embedding = create_embeddings(query)        # 初始检索（获取比需要的更多的结果用于后续重排序）    initial_results = vector_store.similarity_search(query_embedding, k=10)        # 应用重排序    if reranking_method == "llm":        reranked_results = rerank_with_llm(query, initial_results, top_n=top_n)    elif reranking_method == "keywords":        reranked_results = rerank_with_keywords(query, initial_results, top_n=top_n)    else:        # 不进行重排序，直接使用初始检索结果的前 top_n 条        reranked_results = initial_results[:top_n]        # 合并重排序后的上下文    context = "\n\n===\n\n".join([result["text"] for result in reranked_results])        # 根据上下文生成回答    response = generate_response(query, context, model)        return {        "query": query,        "reranking_method": reranking_method,        "initial_results": initial_results[:top_n],        "reranked_results": reranked_results,        "context": context,        "response": response    }


八、用于增强 RAG 的相关段落提取

（Relevant Segment Extraction，RSE）

不同于传统的做法------仅仅检索出多个孤立的文本块， 我们的目标是：识别并重建连续的文本片段，从而为语言模型提供更完整、更有逻辑性的上下文信息。

核心理念：

在文档中，与用户问题相关的文本块往往集中出现在同一区域或连续段落中。 如果我们能够识别这些相关文本块之间的联系，并将它们按顺序组织成一个连贯的整体段落，就能显著提升语言模型对上下文的理解能力。

为什么使用 RSE？

传统 RAG 的问题：

* 检索结果由多个不相连的文本块组成；

<!-- -->

* 块之间可能缺少过渡和背景信息；

<!-- -->

* 导致语言模型理解困难，甚至出现断章取义的情况。

而 RSE 的优势在于： ✅ 将相关文本块组合成连续段落； ✅ 保留原文结构和语义连贯性； ✅ 提供更自然、完整的上下文给语言模型； ✅ 提高最终回答的准确性和流畅度。

RSE 的实现步骤：

1.初步检索  

使用语义搜索从向量库中找出与用户问题最相关的若干文本块。

2.位置排序  

如果原始文档中的文本块有编号或位置信息（如页码、段落顺序），我们可以根据这些信息对检索结果进行重新排序。

3.聚类分析  

分析哪些文本块在原文中彼此靠近且语义相近，将它们归为一组，形成"相关段落簇"。

4.段落重建  

将属于同一个簇的文本块拼接在一起，形成一个完整的上下文段落。必要时还可以加入相邻的前后内容，以增强上下文连贯性。

5.输入语言模型  

将重建后的连续段落作为上下文，提供给大语言模型（LLM）生成最终回答。

示例说明：

假设用户问："深度学习有哪些应用？"

传统 RAG 可能返回以下三个孤立的文本块：

1."深度学习广泛应用于图像识别。"

2."它还被用于语音识别和自然语言处理。"

3."在自动驾驶领域也有重要应用。"

而通过 RSE，我们可以将这三个块按原文顺序拼接成一段：

"深度学习广泛应用于图像识别。它还被用于语音识别和自然语言处理，在自动驾驶领域也有重要应用。"

这样，语言模型就能更好地理解整体含义，而不是分别处理几个独立的句子。


**创建一个简单的向量数据库**


    import numpy as npclassSimpleVectorStore:    """    一个使用 NumPy 的轻量级向量存储实现。    """    def __init__(self, dimension=1536):        """        初始化向量存储。        参数:            dimension (int): 嵌入向量的维度        """        self.dimension = dimension        self.vectors = []  # 存储向量数据        self.documents = []  # 存储文档内容        self.metadata_list = []  # 存储元数据    def add_documents(self, documents, vectors=None, metadata_list=None):        """        向向量存储中添加文档。        参数:            documents (List[str]): 文档分块列表            vectors (List[List[float]], 可选): 嵌入向量列表            metadata_list (List[Dict], 可选): 元数据字典列表        """        if vectors is None:            vectors = [None] * len(documents)        if metadata_list is None:            metadata_list = [{} for _ in range(len(documents))]        for doc, vec, metadata in zip(documents, vectors, metadata_list):            self.documents.append(doc)            self.vectors.append(vec)            self.metadata_list.append(metadata)    def search(self, query_vector, top_k=5):        """        搜索最相似的文档。        参数:            query_vector (List[float]): 查询嵌入向量            top_k (int): 返回的结果数量        返回:            List[Dict]: 包含文档、相似度分数和元数据的结果列表        """        ifnot self.vectors ornot self.documents:            return []        # 将查询向量转换为 NumPy 数组        query_array = np.array(query_vector)        # 计算相似度        similarities = []        for index, vector in enumerate(self.vectors):            ifvector is not None:                # 计算余弦相似度                similarity = np.dot(query_array, vector) / (                    np.linalg.norm(query_array) * np.linalg.norm(vector)                )                similarities.append((index, similarity))        # 根据相似度排序（降序）        similarities.sort(key=lambda x: x[1], reverse=True)        # 获取 top-k 结果        results = []        for index, score in similarities[:top_k]:            results.append({                "document": self.documents[index],                "score": float(score),                "metadata": self.metadata_list[index]            })        return results


**使用 RSE 处理文档**


现在，我们来实现相关段落提取（Relevant Segment Extraction, RSE） 的核心功能。

🧠 打个比方

想象你在图书馆找一本书，管理员给你列出了几十本可能相关的书。

你开始一本一本地看，发现有些确实讲你想知道的内容，有些只是标题看起来相关，内容根本不搭。

于是你给每本书打分：

* 内容很相关的：90 分

<!-- -->

* 有点关系的：60 分

<!-- -->

* 完全没关系的：扣掉 20 分 → 得 40 分甚至负分

最后你只挑了高分的那几本来读。

这个函数就是做这件事 ------ 挑最有用的信息。

    from typing import List, Dict, Tuple
    def process_document(pdf_path: str, chunk_size: int = 800) -> Tuple[List[str], SimpleVectorStore, Dict]:    """    处理文档以便与 RSE（检索增强生成）一起使用。        参数:        pdf_path(str): PDF 文档的路径        chunk_size(int): 每个文本块的大小（字符数）            返回:        Tuple[List[str], SimpleVectorStore, Dict]: 包含文本块列表、向量存储实例和文档信息的元组    """    print("从文档中提取文本...")    # 从 PDF 文件中提取文本内容    document_text = extract_text_from_pdf(pdf_path)        print("将文本分割为非重叠片段...")    # 将提取的文本分割为非重叠的文本块    text_chunks = chunk_text(document_text, chunk_size=chunk_size, overlap=0)    print(f"共创建了 {len(text_chunks)} 个文本块")        print("为文本块生成嵌入向量...")    # 为每个文本块生成嵌入向量    chunk_embeddings = create_embeddings(text_chunks)        # 创建一个 SimpleVectorStore 实例用于存储向量数据    vector_store = SimpleVectorStore()        # 添加带有元数据的文档（包含文本块索引，用于后续重建）    metadata_list = [{"chunk_index": index, "source": pdf_path} for index in range(len(text_chunks))]    vector_store.add_documents(text_chunks, chunk_embeddings, metadata_list)        # 记录原始文档结构以供后续拼接使用    document_info = {        "chunks": text_chunks,        "source": pdf_path,    }        return text_chunks, vector_store, document_info


✅ 总结一下

这个函数干了这么几件事：

1.把用户的问题转成向量；

2.去向量库里找哪些文本块和这个问题最像；

3.给每个文本块打分，越相关的得分越高；

4.给不相关的文本块扣分（惩罚），让它们更容易被忽略；

5.返回一个列表，告诉系统："这些 chunk 哪些重要，哪些不重要。"


**RSE 核心算法：计算文本块价值并找出最佳段落**


在我们已经具备了文档处理功能以及为每个文本块生成嵌入向量的能力之后，现在可以开始实现 RSE（相关段落提取）的核心算法。

    def calculate_chunk_values(query: str, chunks: List[str], vector_store, irrelevant_chunk_penalty: float = 0.2) -> List[float]:    """    计算每个文档切片的价值值（value），结合其相关性得分和位置信息。
        参数:        query(str): 用户输入的查询文本        chunks(List[str]): 文档被切分后的文本块列表        vector_store: 向量数据库，包含文档块的向量表示        irrelevant_chunk_penalty(float): 对无关文档块施加的惩罚值，默认是0.2            返回:        List[float]: 每个文档块对应的价值值列表（浮点数）    """
        # 将用户查询转换成嵌入向量以进行语义匹配    query_embedding = create_embeddings([query])[0]
        # 获取所有文本块数量并搜索相似度结果    total_chunks = len(chunks)    search_results = vector_store.search(query_embedding, top_k=total_chunks)
        # 构建 chunk_index 到相关性得分的映射字典    relevance_scores = {        result["metadata"]["chunk_index"]: result["score"]        for result in search_results    }
        # 根据相关性得分计算价值值，并应用不相关块的惩罚机制    chunk_values = []    for i in range(total_chunks):        score = relevance_scores.get(i, 0.0)        value = score - irrelevant_chunk_penalty        chunk_values.append(value)
        return chunk_values


🎯 举个生活化的例子

想象你在看一本书的目录，每章前面有个"重要性评分"，你想：

1.挑几章读一读；

2.每一章最多读 20 节；

3.总共不超过 30 节；

4.每一段内容必须有价值（评分大于 0.2）；

那你就会从头开始试："从第3节开始读5节怎么样？"、"从第10节开始读3节呢？"...... 最后选出几段你觉得"最有意思、最值得读"的内容。


**在 RAG 中重建并使用段落**


    def reconstruct_segments(document_chunks: List[str], best_segment_indices: List[Tuple[int, int]]) -> List[Dict]:    """    根据最佳切片索引重建文本段落。        参数:        document_chunks(List[str]): 原始文档的所有文本块        best_segment_indices(List[Tuple[int, int]]): 最佳段落的起始和结束索引列表            返回:        List[Dict]: 包含重建段落及其范围的字典列表    """    reconstructed_segments = []
        for start_idx, end_idx in best_segment_indices:        segment_text = " ".join(document_chunks[start_idx:end_idx])        reconstructed_segments.append({            "text": segment_text,            "segment_range": (start_idx, end_idx),        })
        return reconstructed_segments


    def format_segments_for_context(segments: List[Dict]) -> str:    """    将文本段落格式化为语言模型可用的上下文字符串。        参数:        segments(List[Dict]): 包含段落文本和索引范围的字典列表            返回:        str: 格式化的上下文文本    """    context_lines = []
        for index, segment in enumerate(segments):        header = f"SEGMENT {index + 1} (Chunks {segment['segment_range'][0]}-{segment['segment_range'][1] - 1}):"        context_lines.append(header)        context_lines.append(segment["text"])        context_lines.append("-" * 80)
        return"\n\n".join(context_lines)


**举个例子**


假设输入的是这两个段落：

    segments = [    {        "segment_range": [2, 5],        "text": "人工智能是计算机科学的一个分支，旨在让机器模拟人类智能行为。"    },    {        "segment_range": [7, 9],        "text": "深度学习是一种特殊的机器学习方法，特别擅长处理图像和语音数据。"    }]


那么输出会是这样的：

    SEGMENT 1 (Chunks 2-4):人工智能是计算机科学的一个分支，旨在让机器模拟人类智能行为。--------------------------------------------------------------------------------
    SEGMENT 2 (Chunks 7-8):深度学习是一种特殊的机器学习方法，特别擅长处理图像和语音数据。--------------------------------------------------------------------------------


完整的pipeline

    def rag_with_rse(pdf_path: str, query: str, chunk_size: int = 800, penalty: float = 0.2) -> Dict:    """    完整的 RAG 流程，使用相关段落提取（RSE）策略筛选最有用的文档内容。        参数:        pdf_path(str): PDF 文档路径        query(str): 用户查询        chunk_size(int): 文本切片大小        penalty(float): 不相关切片的惩罚系数            返回:        Dict: 包含查询、选中的段落以及生成回答的结果字典    """    print("\n=== 开始执行基于相关段落提取的 RAG 流程 ===")    print(f"查询内容: {query}")
        # 步骤 1：处理文档并生成向量存储    text_chunks, vector_store, doc_info = process_document(pdf_path, chunk_size)
        # 步骤 2：计算每个文本块的相关性得分与价值值    print("\n正在计算文本块相关性得分与价值值...")    chunk_values = calculate_chunk_values(query, text_chunks, vector_store, penalty)
        # 步骤 3：根据价值值选择最优段落    best_segments, scores = find_best_segments(        chunk_values=chunk_values,        max_segment_length=20,        total_max_length=30,        min_segment_value=0.2    )
        # 步骤 4：重建最佳段落    print("\n正在重建最佳文本段落...")    selected_segments = reconstruct_segments(text_chunks, best_segments)
        # 步骤 5：格式化上下文供大模型使用    formatted_context = format_segments_for_context(selected_segments)
        # 步骤 6：调用大模型生成最终回复    response = generate_response(query, formatted_context)
        # 整理输出结果    result = {        "query": query,        "segments": selected_segments,        "response": response    }
        print("\n=== 最终回复如下 ===")    print(response)
        return result


九、上下文压缩技术：提升 RAG 系统效率

我们将对检索到的文本块进行过滤与压缩，只保留其中最相关的内容，从而：

✅ 减少噪声信息；

✅ 提高语言模型回答的准确性和相关性；

✅ 更高效地利用有限的上下文窗口（context window）。


**问题背景**


在使用 RAG 系统进行文档检索时，我们通常会得到一些包含混合内容的文本块：

* 有些句子与用户的问题相关；

<!-- -->

* 有些句子则完全无关或只是背景介绍。

例如：

"人工智能是计算机科学的一个分支。它旨在让机器模拟人类智能行为。许多AI系统依赖于大数据进行训练。深度学习是一种特殊的机器学习方法。"

如果用户的问题是："什么是人工智能？" 那么只有第一句是最相关的，其余内容虽然正确，但和当前问题无关。


**上下文压缩的目标**


我们要做的是：

✅ 移除不相关的句子或段落；

✅ 仅保留与用户查询高度相关的信息；

✅ 最大化上下文窗口中的"有用信息密度"。

这样可以让语言模型更专注于关键内容，避免被无关信息干扰，从而提高最终回答的质量。


**实现思路**


我们将从零开始实现一个简单的上下文压缩流程，主要包括以下步骤：

\#\#\## 1. 逐句分析相关性

将每个文本块拆分为句子，并使用语义模型（如 BERT、Sentence-BERT 等）计算每句话与用户查询之间的相关性得分。

🔹 示例：

    scores = [model.similarity(query_embedding, sentence_embedding) for sentence in sentences]


\#\#\## 2. 设定阈值或选择 Top-K 句子

我们可以选择两种策略之一来筛选句子：

✅ 保留得分高于某个阈值的句子；

✅ 或者保留得分最高的前 K 个句子。

\#\#\## 3. 重建压缩后的上下文

将筛选后的句子按原始顺序重新组合成一个新的、更紧凑的上下文段落。


**示例演示**


原始文本块：

"人工智能是计算机科学的一个分支。它旨在让机器模拟人类智能行为。许多AI系统依赖于大数据进行训练。深度学习是一种特殊的机器学习方法。"

用户问题：

"什么是人工智能？"

经过压缩后保留的内容：

"人工智能是计算机科学的一个分支。它旨在让机器模拟人类智能行为。"


**实现上下文压缩**


这是方法的核心部分。我们将使用一个大语言模型来过滤和压缩检索到的内容，从而保留与用户问题最相关的信息。

    def compress_chunk(chunk: str, query: str, compression_type: str = "selective", model: str = "qwen-max") -> Tuple[str, float]:    """    压缩检索到的文本块，仅保留与查询相关的部分。    参数:        chunk(str): 需要压缩的文本块        query(str): 用户查询        compression_type(str): 压缩方式 ("selective", "summary", 或 "extraction")        model(str): 使用的 LLM 模型名称    返回:        Tuple[str, float]: 压缩后的文本块 和 压缩比例（百分比）    """    # 根据不同压缩类型构建系统提示词    if compression_type == "selective":        system_prompt = """你是一个信息筛选专家。        你的任务是分析文档片段并提取**直接与用户查询相关**的句子或段落。删除所有不相关的内容。        输出要求：        1. 只包含有助于回答问题的文本        2. 保留相关句子的原始措辞（不要改写）        3. 维持原文顺序        4. 包含所有相关内容，即使看起来重复        5. 排除任何与问题无关的文本        请以纯文本格式输出，不要添加额外说明。"""        elif compression_type == "summary":        system_prompt = """你是一个摘要专家。        你的任务是对给定的文档片段进行简洁总结，只聚焦于与用户查询有关的信息。        输出要求：        1. 简洁但涵盖所有与问题相关的内容        2. 专注于与查询相关的信息        3. 忽略不相关细节        4. 用中立、客观的语气撰写        请以纯文本格式输出，不要添加额外说明。"""        else:  # extraction        system_prompt = """你是一个信息抽取专家。        你的任务是从文档片段中提取**确切包含相关信息的句子**来回答用户的查询。        输出要求：        1. 仅包含原文中的相关句子        2. 保持原句不变（不要修改）        3. 只包含与问题直接相关的句子        4. 每个句子之间用换行分隔        5. 不添加任何评论或其他内容        请以纯文本格式输出，不要添加额外说明。"""    # 构建用户提示    user_prompt = f"""        查询：{query}        文档片段：        {chunk}        提取与该查询相关的内容。    """    # 调用大模型 API 进行压缩处理    response = client.chat.completions.create(        model=model,        messages=[            {"role": "system", "content": system_prompt},            {"role": "user", "content": user_prompt}        ],        temperature=0    )    # 获取压缩后的内容    compressed_content = response.choices[0].message.content.strip()    # 计算压缩比例    original_length = len(chunk)    compressed_length = len(compressed_content)    compression_ratio = (original_length - compressed_length) / original_length * 100
        return compressed_content, compression_ratio


完整pipeline

    def rag_with_compression(pdf_path: str, query: str, k: int = 10, compression_type: str = "selective", model: str = "qwen-max") -> Dict:    """    完整的 RAG 流程，使用上下文压缩策略减少输入长度。
        参数:        pdf_path(str): PDF 文件路径        query(str): 用户查询        k(int): 初始检索的文本块数量        compression_type(str): 压缩方法        model(str): 使用的大模型名称
        返回:        Dict: 包含查询、压缩前后内容、响应等结果的字典    """
        print("\n=== 上下文压缩 RAG 流程开始 ===")    print(f"查询内容: {query}")    print(f"压缩类型: {compression_type}")
        # 加载文档并创建向量存储    vector_store = process_document(pdf_path)
        # 创建查询嵌入    query_embedding = create_embeddings(query)
        # 检索最相关的前 k 个文本块    print(f"正在检索前 {k} 个相关文本块...")    results = vector_store.similarity_search(query_embedding, k=k)    retrieved_chunks = [result["text"] for result in results]
        # 对每个文本块进行压缩    compressed_results = batch_compress_chunks(retrieved_chunks, query, compression_type, model)    compressed_chunks = [result[0] for result in compressed_results]    compression_ratios = [result[1] for result in compressed_results]
        # 过滤空内容    valid_compressed_data = [(chunk, ratio) for chunk, ratio in zip(compressed_chunks, compression_ratios) if chunk.strip()]
        ifnot valid_compressed_data:        # 所有压缩后为空时回退原始文本块        print("警告：所有文本块被压缩为空。将使用原始文本块。")        valid_compressed_data = [(chunk, 0.0) for chunk in retrieved_chunks]    else:        compressed_chunks, compression_ratios = zip(*valid_compressed_data)
        # 构建上下文    context = "\n\n---\n\n".join(compressed_chunks)
        # 生成最终回复    print("基于压缩后的文本块生成回复...")    response = generate_response(query, context, model)
        # 返回结果    result = {        "query": query,        "original_chunks": retrieved_chunks,        "compressed_chunks": compressed_chunks,        "compression_ratios": compression_ratios,        "context_length_reduction": f"{sum(compression_ratios) / len(compression_ratios):.2f}%",        "response": response    }
        print("\n=== 最终回复 ===")    print(response)
        return result    


十、RAG 中的反馈机制（Feedback Loop）

在本节中，我将实现一个带有反馈机制的 RAG 系统，它能够随着时间推移不断自我优化。 通过收集并整合用户的反馈信息，它可以：

✅ 学习哪些回答是有效的，哪些需要改进；

✅ 持续提升检索结果的相关性和回答质量；

✅ 在每一次交互中变得"更聪明"。


**传统 RAG 系统的局限性**


传统的 RAG 系统是静态的：

它们仅基于向量相似度来检索信息，不会从用户反馈中学习。

这意味着：

* 如果返回了不准确或不相关的答案，系统不会自动修正；

<!-- -->

* 即使同样的问题被多次提出，系统也不会"记住"之前更好的回答。


**带有反馈机制的 RAG 的优势**


我们构建的是一个动态、自适应的 RAG 系统，它具备以下能力：

✅ 记忆功能：记住哪些文档曾提供过有用的信息，哪些没有；

✅ 动态调整评分：根据历史反馈更新文档的相关性得分；

✅ 知识积累：将成功的问答对加入知识库，供未来查询使用；

✅ 持续进化：每次与用户的互动都是一次学习机会，系统会越用越准、越用越好。


**反馈机制的核心流程**


1.用户提问

* 用户输入一个问题，并得到一个由 RAG 系统生成的回答。

2.获取用户反馈

* 用户可以通过评分、点赞/踩、或者直接评论等方式提供反馈；

<!-- -->

* 示例：

<!-- -->

* "这个回答很有帮助 ✅"

* "这个回答不够详细 ❌"

* "请补充更多细节 📝"

3.记录反馈数据

* 将用户问题、原始回答、反馈内容等信息存储下来，形成反馈日志。

4.分析与学习

* 使用模型分析哪些文档和段落产生了高质量的回答；

* 调整这些文档在未来的检索权重；

* 将高质量问答对加入知识库，用于增强未来的语义理解。

5.优化下一次回答

* 下次遇到类似问题时，系统能更快、更准确地找到最佳答案。


**示例演示**


🔹 用户第一次提问：

"什么是机器学习？"

系统回答：

"机器学习是一种人工智能技术，让计算机通过数据学习规律。"

用户反馈：

"不错，但可以更详细。"

🔹 第二次有人问类似问题：

"机器学习的基本原理是什么？"

系统结合之前的反馈，返回更详细的回答：

"机器学习是一种人工智能技术，它通过训练数据让计算机自动学习模式和规律。常见的方法包括监督学习、无监督学习和强化学习。"


**构建简单向量数据库**


    from typing import List, Dict, Optional, Tuple, Callableimport numpy as np

    classSimpleVectorStore:    """    基于 NumPy 的简易向量数据库实现。
        该类提供内存中的向量存储与检索系统，支持使用余弦相似度进行基本的相似性搜索。    """
        def __init__(self):        """        初始化向量数据库，包含三个并行列表：        - vectors: 存储嵌入向量（NumPy 数组）        - texts: 存储原始文本块        - metadata: 存储每个文本块的元数据        """        self.vectors: List[np.ndarray] = []  # 嵌入向量列表        self.texts: List[str] = []           # 文本内容列表        self.metadata: List[Dict] = []       # 元数据列表
        def add_item(self, text: str, embedding: List[float], metadata: Optional[Dict] = None) -> None:        """        添加一个条目到向量数据库中。
            参数:            text (str): 需要存储的文本内容            embedding (List[float]): 表示该文本的嵌入向量            metadata (Dict, optional): 可选的元数据字典        """        self.vectors.append(np.array(embedding))        self.texts.append(text)        self.metadata.append(metadata or {})
        def similarity_search(        self,        query_embedding: List[float],        k: int = 5,        filter_func: Optional[Callable[[Dict], bool]] = None    ) -> List[Dict]:        """        使用余弦相似度查找与查询向量最相似的条目。
            参数:            query_embedding (List[float]): 查询向量            k (int): 返回结果的数量            filter_func (Callable, optional): 过滤函数，用于基于元数据筛选结果
            返回:            List[Dict]: 包含文本、元数据和相关性评分的结果列表        """        ifnot self.vectors:            return []
            query_vector = np.array(query_embedding)        similarities = []
            for i, vector in enumerate(self.vectors):            if filter_func andnot filter_func(self.metadata[i]):                continue
                similarity = np.dot(query_vector, vector) / (                np.linalg.norm(query_vector) * np.linalg.norm(vector)            )            similarities.append((i, similarity))
            similarities.sort(key=lambda x: x[1], reverse=True)
            results = []        for i in range(min(k, len(similarities))):            idx, score = similarities[i]            results.append({                "text": self.texts[idx],                "metadata": self.metadata[idx],                "similarity": score,                "relevance_score": self.metadata[idx].get("relevance_score", score)            })
            return results


**反馈系统功能模块**


现在，我们将实现核心的反馈系统组件。

    def get_user_feedback(query: str, response: str, relevance: int, quality: int, comments: str = "") -> Dict:    """    将用户反馈格式化为字典。
        参数:        query(str): 用户的问题        response(str): 系统的回答        relevance(int): 相关性评分（1-5）        quality(int): 回答质量评分（1-5）        comments(str): 可选评论
        返回:        Dict: 格式化的反馈字典    """    return{        "query": query,        "response": response,        "relevance": int(relevance),        "quality": int(quality),        "comments": comments,        "timestamp": datetime.now().isoformat()    }


    def store_feedback(feedback: Dict, feedback_file: str = "feedback_data.json") -> None:    """    将反馈数据保存到 JSON 文件中。
        参数:        feedback(Dict): 反馈数据        feedback_file(str): 文件路径    """    with open(feedback_file, "a") as f:        json.dump(feedback, f)        f.write("\n")


    def load_feedback_data(feedback_file: str = "feedback_data.json") -> List[Dict]:    """    从文件中加载反馈数据。
        参数:        feedback_file(str): 文件路径
        返回:        List[Dict]: 反馈数据列表    """    feedback_data = []    try:        with open(feedback_file, "r") as f:            for line in f:                if line.strip():                    feedback_data.append(json.loads(line.strip()))    except FileNotFoundError:        print("未找到反馈文件。将使用空反馈开始。")
        return feedback_data


带有反馈意识的文档处理

    def process_document(pdf_path: str, chunk_size: int = 1000, chunk_overlap: int = 200) -> Tuple[List[str], SimpleVectorStore]:    """    处理文档以进行 RAG 流程。
        步骤：    1. 提取 PDF 中的文本    2. 切分文本    3. 创建嵌入    4. 存储到向量数据库
        参数:        pdf_path(str): PDF 文件路径        chunk_size(int): 每个切片大小        chunk_overlap(int): 切片之间的重叠字符数
        返回:        Tuple[List[str], SimpleVectorStore]: 文本切片和向量数据库    """    print("正在从 PDF 提取文本...")    extracted_text = extract_text_from_pdf(pdf_path)
        print("正在切分文本...")    chunks = chunk_text(extracted_text, chunk_size, chunk_overlap)    print(f"生成了 {len(chunks)} 个文本切片")
        print("正在为切片创建嵌入...")    chunk_embeddings = create_embeddings(chunks)
        store = SimpleVectorStore()
        for i, (chunk, embedding) in enumerate(zip(chunks, chunk_embeddings)):        store.add_item(            text=chunk,            embedding=embedding,            metadata={                "index": i,                "source": pdf_path,                "relevance_score": 1.0,                "feedback_count": 0            }        )
        print(f"已添加 {len(chunks)} 个切片到向量数据库")    return chunks, store


    def assess_feedback_relevance(query: str, doc_text: str, feedback: dict) -> bool:    """    使用语言模型（LLM）来判断一段过去的用户反馈是否与当前查询和文档内容相关。        这个函数用于决定哪些历史反馈应该影响当前的检索结果排序或生成结果。        参数:        query(str): 当前用户的查询问题        doc_text(str): 正在评估的文档内容（即要检索的文本块）        feedback(Dict): 之前保存的用户反馈数据，包含 'query' 和 'response' 字段            返回:        bool: 如果该反馈与当前查询和文档相关，返回 True；否则返回 False    """
        # 系统提示词：告诉AI它只能判断反馈是否相关，不能做其他事情    system_prompt = """你是一个判断反馈是否相关的专家。请只回答"yes"或"no"，不要提供任何解释或其他内容。"""
        # 用户提示词：构建输入上下文，包括当前查询、过去的问题、文档内容片段和之前的回答    user_prompt = f"""    当前查询：{query}    过去收到反馈的问题：{feedback['query']}    文档内容：{doc_text[:500]}... [截断]    过去收到反馈的回答：{feedback['response'][:500]}... [截断]
        这条历史反馈是否与当前查询和文档内容相关？请回答 yes 或 no。    """
        # 调用 LLM 模型 API 获取判断结果    response = client.chat.completions.create(        model="qwen-max",  # 使用的模型名称        messages=[            {"role": "system", "content": system_prompt},  # 系统指令（已翻译成中文）            {"role": "user", "content": user_prompt}       # 用户输入内容        ],        temperature=0  # 设置为0以确保输出确定性    )
        # 提取模型响应并处理    answer = response.choices[0].message.content.strip().lower()
        # 判断是否包含 "yes"    return'yes' in answer


    def adjust_relevance_scores(query: str, results: List[Dict], feedback_data: List[Dict]) -> List[Dict]:    """    根据历史反馈调整检索结果的相关性评分。
        参数:        query(str): 当前查询        results(List[Dict]): 检索结果        feedback_data(List[Dict]): 历史反馈数据
        返回:        List[Dict]: 调整后的结果    """    ifnot feedback_data:        return results
        print("正在根据反馈历史调整相关性评分...")
        for i, result in enumerate(results):        document_text = result["text"]        relevant_feedback = []
            for fb in feedback_data:            if assess_feedback_relevance(query, document_text, fb):                relevant_feedback.append(fb)
            if relevant_feedback:            avg_relevance = sum(f['relevance'] for f in relevant_feedback) / len(relevant_feedback)            modifier = 0.5 + (avg_relevance / 5.0)            original_score = result["similarity"]            adjusted_score = original_score * modifier
                result.update({                "original_similarity": original_score,                "similarity": adjusted_score,                "relevance_score": adjusted_score,                "feedback_applied": True,                "feedback_count": len(relevant_feedback)            })
                print(f"  文档 {i+1}: 评分从 {original_score:.4f} 调整至 {adjusted_score:.4f}，基于 {len(relevant_feedback)} 条反馈")
        results.sort(key=lambda x: x["similarity"], reverse=True)    return results


    def rag_with_feedback_loop(    query: str,    vector_store: SimpleVectorStore,    feedback_data: List[Dict],    k: int = 5,    model: str = "qwen-amax") -> Dict:    """    执行带反馈机制的完整 RAG 流程。
        参数:        query(str): 用户查询        vector_store(SimpleVectorStore): 向量数据库        feedback_data(List[Dict]): 历史反馈数据        k(int): 检索数量        model(str): LLM 模型
        返回:        Dict: 包含查询、检索文档和响应的结果    """    print(f"\n=== 正在处理带反馈的 RAG 查询 ===")    print(f"查询: {query}")
        query_embedding = create_embeddings(query)    results = vector_store.similarity_search(query_embedding, k=k)    adjusted_results = adjust_relevance_scores(query, results, feedback_data)
        retrieved_texts = [result["text"] for result in adjusted_results]    context = "\n\n---\n\n".join(retrieved_texts)
        print("正在生成回复...")    response = generate_response(query, context, model)
        return {        "query": query,        "retrieved_documents": adjusted_results,        "response": response    }


利用反馈微调索引

    def fine_tune_index(    current_store: SimpleVectorStore,    chunks: List[str],    feedback_data: List[Dict]) -> SimpleVectorStore:    """    使用高质量反馈微调向量数据库。
        参数:        current_store(SimpleVectorStore): 当前数据库        chunks(List[str]): 原始文本切片        feedback_data(List[Dict]): 历史反馈数据
        返回:        SimpleVectorStore: 微调后的数据库    """    print("正在使用高质量反馈微调索引...")
        good_feedback = [fb for fb in feedback_data if fb['relevance'] >= 4and fb['quality'] >= 4]
        ifnot good_feedback:        print("未找到高质量反馈。")        return current_store
        new_store = SimpleVectorStore()
        for i in range(len(current_store.texts)):        new_store.add_item(            text=current_store.texts[i],            embedding=current_store.vectors[i],            metadata=current_store.metadata[i].copy()        )
        for feedback in good_feedback:        enhanced_text = f"Question: {feedback['query']}\nAnswer: {feedback['response']}"        embedding = create_embeddings(enhanced_text)
            new_store.add_item(            text=enhanced_text,            embedding=embedding,            metadata={                "type": "feedback_enhanced",                "query": feedback["query"],                "relevance_score": 1.2,                "feedback_count": 1,                "original_feedback": feedback            }        )
            print(f"已添加反馈内容: {feedback['query'][:50]}...")
        print(f"微调后索引包含 {len(new_store.texts)} 项 (原始: {len(chunks)})")    return new_store


完整工作流程：从初始设置到反馈收集

    def full_rag_workflow(    pdf_path: str,    query: str,    feedback_data: Optional[List[Dict]] = None,    feedback_file: str = "feedback_data.json",    fine_tune: bool = False) -> Dict:    """    完整的 RAG 工作流，集成反馈机制。
        参数:        pdf_path(str): PDF 文件路径        query(str): 用户查询        feedback_data(Optional[List[Dict]]): 历史反馈数据        feedback_file(str): 反馈文件路径        fine_tune(bool): 是否启用索引微调
        返回:        Dict: 包含响应和检索信息的结果    """    if feedback_data is None:        feedback_data = load_feedback_data(feedback_file)        print(f"从 {feedback_file} 加载了 {len(feedback_data)} 条反馈")
        chunks, vector_store = process_document(pdf_path)
        if fine_tune and feedback_data:        vector_store = fine_tune_index(vector_store, chunks, feedback_data)
        result = rag_with_feedback_loop(query, vector_store, feedback_data)
        print("\n=== 是否愿意对本次回复提供反馈？ ===")    print("评分相关性 (1-5):")    relevance = input()
        print("评分质量 (1-5):")    quality = input()
        print("任何评论？（可跳过）")    comments = input()
        feedback = get_user_feedback(        query=query,        response=result["response"],        relevance=int(relevance),        quality=int(quality),        comments=comments    )
        store_feedback(feedback, feedback_file)    print("感谢您的反馈！")
        return result


参考文献：

1.Searching for Best Practices in Retrieval-Augmented Generation https://arxiv.org/abs/2407.01219

2.A Comprehensive Survey of Retrieval-Augmented Generation (RAG): Evolution, Current Landscape and Future Directions https://arxiv.org/abs/2410.12837

3.《Advanced RAG Techniques》Yugank .Amanhttps://medium.com/@yugank.aman/advanced-rag-techniques-0c283aacf5ba

4.https://github.com/FareedKhan-dev/all-rag-techniques

5.https://github.com/NirDiamant/RAG_Techniques


**在 App 上搭建开箱即用的 AI 助手**


企业在移动应用中集成 AI 功能时往往面临开发周期长、技术复杂度高等问题，本方案基于多端低代码开发平台和大模型服务平台，通过构建非侵入式 Copilot 助理，提供意图识别、知识问答等智能服务，实现应用快速、无缝智能化升级，助力企业高效创新。

点击阅读原文查看详情。


[Read in Cubox](https://cubox.pro/web/card/7331951337749351963)
