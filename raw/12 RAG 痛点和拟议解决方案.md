---
id: "7327342715878769247"
cubox_url: https://cubox.pro/web/card/7327342715878769247
url: https://readmedium.com/zh/12-rag-pain-points-and-proposed-solutions-43709939a28c
tags:
  - RAG

---
# 12 RAG 痛点和拟议解决方案

解决 "检索-增强一代 "的核心难题

[Read in Cubox](https://cubox.pro/web/card/7327342715878769247)  
[Read Original](https://readmedium.com/zh/12-rag-pain-points-and-proposed-solutions-43709939a28c)  

---


---

\## 📖 正文全文

# 我想到了两个拟议的解决方案：

[readmedium.com](https://readmedium.com/zh/12-rag-pain-points-and-proposed-solutions-43709939a28c)

\## 12 RAG Pain Points and Proposed Solutions

\## Solving the core challenges of Retrieval-Augmented Generation
解决 "检索-增强一代 "的核心难题

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fcdn-images-1.readmedium.com%2Fv2%2Fresize%3Afit%3A800%2F1%2ABlY_OEFUSzvGHnUF6lMwpA.jpeg&valid=true) Image adapted from [Seven Failure Points When Engineering a Retrieval Augmented Generation System](https://arxiv.org/pdf/2401.05856.pdf)

· Pain Point 1: Missing Content · Pain Point 2: Missed the Top Ranked Documents · Pain Point 3: Not in Context --- Consolidation Strategy Limitations · Pain Point 4: Not Extracted · Pain Point 5: Wrong Format · Pain Point 6: Incorrect Specificity · Pain Point 7: Incomplete · Pain Point 8: Data Ingestion Scalability · Pain Point 9: Structured Data QA · Pain Point 10: Data Extraction from Complex PDFs · Pain Point 11: Fallback Model(s) · Pain Point 12: LLM Security  
- 痛点 1：内容缺失 - 痛点 2：错过排名靠前的文档 - 痛点 3：不符合实际情况 - 整合策略的局限性 - 痛点 4：未提取 - 痛点 5：格式错误 - 痛点 6：不正确的特定性 - 痛点 7：不完整 - 痛点 8：数据输入的可扩展性 - 痛点 9：结构化数据质量保证 - 痛点 10：从复杂 PDF 中提取数据 - 痛点 11：后备模型 - 痛点 12：LLM 安全性

Inspired by the paper [Seven Failure Points When Engineering a Retrieval Augmented Generation System](https://arxiv.org/pdf/2401.05856.pdf) by Barnett et al., let's explore the seven failure points mentioned in the paper and five additional common pain points in developing an RAG pipeline in this article. More importantly, we will delve into the solutions to those RAG pain points so we can be better equipped to tackle those pain points in our day-to-day RAG development.

I use "pain points" instead of "failure points" mainly because those points all have corresponding proposed solutions. Let's try to fix them before they become failures in our RAG pipelines.

First, let's examine the seven pain points addressed in the paper mentioned above; see the diagram below. We will then add the five additional pain points and their proposed solutions.
![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fcdn-images-1.readmedium.com%2Fv2%2Fresize%3Afit%3A800%2F0%2A5pAddwy6ZAElg1hk&valid=true) Image source: [Seven Failure Points When Engineering a Retrieval Augmented Generation System](https://arxiv.org/pdf/2401.05856.pdf)

\## Pain Point 1: Missing Content
痛点 1：内容缺失

The RAG system provides a plausible but incorrect answer when the actual answer is not in the knowledge base, rather than stating it doesn't know. Users receive misleading information, leading to frustration.  
当实际答案不在知识库中时，RAG 系统会提供一个似是而非的错误答案，而不是说它不知道。用户会收到误导性信息，从而产生挫败感。

We have two proposed solutions:

\## Clean your data

Garbage in, garbage out. If your source data is of poor quality, such as containing conflicting information, no matter how well you build your RAG pipeline, it cannot do the magic to output gold from the garbage you feed it. This proposed solution is not only for this pain point but all the pain points listed in this article. Clean data is the prerequisite for any well-functioning RAG pipeline.

\## Better prompting

Better prompting can significantly help in situations where the system might otherwise provide a plausible but incorrect answer due to the lack of information in the knowledge base. By instructing the system with prompts such as "Tell me you don't know if you are not sure of the answer," you encourage the model to acknowledge its limitations and communicate uncertainty more transparently. There is no guarantee for 100% accuracy, but crafting your prompt is one of the best efforts you can make after cleaning your data.

\## Pain Point 2: Missed the Top Ranked Documents

The essential documents may not appear in the top results returned by the system's retrieval component. The correct answer is overlooked, causing the system to fail to deliver accurate responses. The paper hinted, "The answer to the question is in the document but did not rank highly enough to be returned to the user".

Two proposed solutions came to my mind:  
我想到了两个拟议的解决方案：

\## Hyperparameter tuning for chunk_size and similarity_top_k

Both `chunk_size` and `similarity_top_k` are parameters used to manage the efficiency and effectiveness of the data retrieval process in RAG models. Adjusting these parameters can impact the trade-off between computational efficiency and the quality of retrieved information. We explored the details of hyperparameter tuning for both `chunk_size` and `similarity_top_k` in our previous article, [Automating Hyperparameter Tuning with LlamaIndex](https://readmedium.com/automating-hyperparameter-tuning-with-llamaindex-72fdd68e3b90?sk=0a29f2025b965040b9b1defd9525e4eb). See the sample code snippet below.  
在 RAG 模型中，chunk_size 和 similarity_top_k 都是用于管理数据检索过程的效率和效果的参数。调整这些参数会影响计算效率和检索信息质量之间的权衡。我们在之前的文章《使用 LlamaIndex 自动调整超参数》中探讨了调整 chunk_size 和 similarity_top_k 这两个参数的细节。请参阅下面的示例代码片段。

```
param_tuner = ParamTuner(
    param_fn=objective_function_semantic_similarity,
    param_dict=param_dict,
    fixed_param_dict=fixed_param_dict,
    show_progress=True,
)

results = param_tuner.tune()
```

The function `objective_function_semantic_similarity` is defined as follows, with `param_dict` containing the parameters, `chunk_size` and `top_k`, and their corresponding proposed values:  
函数 objective_function_semantic_similarity 的定义如下，其中 param_dict 包含参数 chunk_size 和 top_k，以及相应的建议值：

```
# contains the parameters that need to be tuned
param_dict = {"chunk_size": [256, 512, 1024], "top_k": [1, 2, 5]}

# contains parameters remaining fixed across all runs of the tuning process
fixed_param_dict = {
    "docs": documents,
    "eval_qs": eval_qs,
    "ref_response_strs": ref_response_strs,
}

def objective_function_semantic_similarity(params_dict):
    chunk_size = params_dict["chunk_size"]
    docs = params_dict["docs"]
    top_k = params_dict["top_k"]
    eval_qs = params_dict["eval_qs"]
    ref_response_strs = params_dict["ref_response_strs"]

    # build index
    index = _build_index(chunk_size, docs)

    # query engine
    query_engine = index.as_query_engine(similarity_top_k=top_k)

    # get predicted responses
    pred_response_objs = get_responses(
        eval_qs, query_engine, show_progress=True
    )

    # run evaluator
    eval_batch_runner = _get_eval_batch_runner_semantic_similarity()
    eval_results = eval_batch_runner.evaluate_responses(
        eval_qs, responses=pred_response_objs, reference=ref_response_strs
    )

    # get semantic similarity metric
    mean_score = np.array(
        [r.score for r in eval_results["semantic_similarity"]]
    ).mean()

    return RunResult(score=mean_score, params=params_dict)
```

For more details, refer to LlamaIndex's full notebook on [Hyperparameter Optimization for RAG](https://docs.llamaindex.ai/en/stable/examples/param_optimizer/param_optimizer.html).  
更多详情，请参阅 LlamaIndex 关于 RAG 超参数优化的完整笔记本。

\## Reranking

Reranking retrieval results before sending them to the LLM has significantly improved RAG performance. This LlamaIndex [notebook](https://docs.llamaindex.ai/en/stable/examples/node_postprocessor/CohereRerank.html) demonstrates the difference between:

* Inaccurate retrieval by directly retrieving the top 2 nodes without a reranker.
* Accurate retrieval by retrieving the top 10 nodes and using `CohereRerank` to rerank and return the top 2 nodes.  
  通过检索前 10 个节点，并使用 CohereRerank 重新排序并返回前 2 个节点，实现精确检索。

```
import os
from llama_index.postprocessor.cohere_rerank import CohereRerank

api_key = os.environ["COHERE_API_KEY"]
cohere_rerank = CohereRerank(api_key=api_key, top_n=2) # return top 2 nodes from reranker

query_engine = index.as_query_engine(
    similarity_top_k=10, # we can set a high top_k here to ensure maximum relevant retrieval
    node_postprocessors=[cohere_rerank], # pass the reranker to node_postprocessors
)

response = query_engine.query(
    "What did Sam Altman do in this essay?",
)
```

In addition, you can evaluate and enhance retriever performance using various embeddings and rerankers, as detailed in [Boosting RAG: Picking the Best Embedding \& Reranker models](https://blog.llamaindex.ai/boosting-rag-picking-the-best-embedding-reranker-models-42d079022e83) by [Ravi Theja](https://readmedium.com/zh/undefined).

Moreover, you can finetune a custom reranker to get even better retrieval performance, and the detailed implementation is documented in [Improving Retrieval Performance by Fine-tuning Cohere Reranker with LlamaIndex](https://blog.llamaindex.ai/improving-retrieval-performance-by-fine-tuning-cohere-reranker-with-llamaindex-16c0c1f9b33b) by [Ravi Theja](https://readmedium.com/zh/undefined).  
此外，您还可以对自定义重排器进行微调，以获得更好的检索性能，具体实现方法详见 Ravi Theja 撰写的《利用 LlamaIndex 微调 Cohere 重排器以提高检索性能》一文。

\## Pain Point 3: Not in Context --- Consolidation Strategy Limitations

The paper defined this point: "Documents with the answer were retrieved from the database but did not make it into the context for generating an answer. This occurs when many documents are returned from the database, and a consolidation process takes place to retrieve the answer".  
论文对这一点的定义是："从数据库中检索到有答案的文档，但没有进入生成答案的上下文。当从数据库中返回许多文档时，就会出现这种情况，这时就需要进行合并处理以检索答案"。

In addition to adding a reranker and finetuning the reranker as described in the above section, we can explore the following proposed solutions:

\## Tweak retrieval strategies

LlamaIndex offers an array of retrieval strategies, from basic to advanced, to help us achieve accurate retrieval in our RAG pipelines. Check out the [retrievers module guide](https://docs.llamaindex.ai/en/stable/module_guides/querying/retriever/retrievers.html) for a comprehensive list of all retrieval strategies, broken down into different categories.  
LlamaIndex 提供一系列从基本到高级的检索策略，帮助我们在 RAG 管道中实现精确检索。请查看检索模块指南，了解按不同类别分列的所有检索策略的综合列表。

* Basic retrieval from each index  
  每个索引的基本检索
* Advanced retrieval and search
* Auto-Retrieval  
  自动检索
* Knowledge Graph Retrievers
* Composed/Hierarchical Retrievers  
  组合式/层次式检索器
* and more!

\## Finetune embeddings

If you use an open-source embedding model, finetuning your embedding model is a great way to achieve more accurate retrievals. LlamaIndex has [a step-by-step guide](https://docs.llamaindex.ai/en/stable/examples/finetuning/embeddings/finetune_embedding.html) on finetuning an open-source embedding model, proving that finetuning the embedding model improves metrics consistently across the suite of eval metrics.

See below a sample code snippet on creating a finetune engine, run the finetuning, and get the finetuned model:  
请参阅下面的示例代码片段，了解如何创建微调引擎、运行微调并获取微调后的模型：

```
finetune_engine = SentenceTransformersFinetuneEngine(
    train_dataset,
    model_id="BAAI/bge-small-en",
    model_output_path="test_model",
    val_dataset=val_dataset,
)

finetune_engine.finetune()

embed_model = finetune_engine.get_finetuned_model()
```

\## Pain Point 4: Not Extracted
痛点 4：未提取

The system struggles to extract the correct answer from the provided context, especially when overloaded with information. Key details are missed, compromising the quality of responses. The paper hinted: "This occurs when there is too much noise or contradicting information in the context".  
系统难以从提供的上下文中提取正确答案，尤其是在信息量过大的情况下。关键细节被遗漏，影响了答案的质量。论文暗示"当语境中存在过多噪音或相互矛盾的信息时，就会出现这种情况"。

Let's explore three proposed solutions:  
让我们探讨三个拟议的解决方案：

\## Clean your data
清理数据

This pain point is yet another typical victim of bad data. We cannot stress enough the importance of clean data! Do spend time cleaning your data first before blaming your RAG pipeline.

\## Prompt Compression

Prompt compression in the long-context setting was introduced in the [LongLLMLingua research project/paper](https://arxiv.org/abs/2310.06839). With its integration in LlamaIndex, we can now implement LongLLMLingua as a node postprocessor, which will compress context after the retrieval step before feeding it into the LLM.

See the sample code snippet below, where we set up `LongLLMLinguaPostprocessor`, which uses the `longllmlingua` package to run prompt compression.  
请参阅下面的示例代码片段，我们在其中设置了 LongLLMLinguaPostprocessor，它使用 longllmlingua 软件包来运行提示压缩。

For more details, check out the [full notebook](https://docs.llamaindex.ai/en/stable/examples/node_postprocessor/LongLLMLingua.html\#longllmlingua) on LongLLMLingua.

```
from llama_index.query_engine import RetrieverQueryEngine
from llama_index.response_synthesizers import CompactAndRefine
from llama_index.postprocessor import LongLLMLinguaPostprocessor
from llama_index.schema import QueryBundle

node_postprocessor = LongLLMLinguaPostprocessor(
    instruction_str="Given the context, please answer the final question",
    target_token=300,
    rank_method="longllmlingua",
    additional_compress_kwargs={
        "condition_compare": True,
        "condition_in_question": "after",
        "context_budget": "+100",
        "reorder_context": "sort",  # enable document reorder
    },
)

retrieved_nodes = retriever.retrieve(query_str)
synthesizer = CompactAndRefine()

# outline steps in RetrieverQueryEngine for clarity:
# postprocess (compress), synthesize
new_retrieved_nodes = node_postprocessor.postprocess_nodes(
    retrieved_nodes, query_bundle=QueryBundle(query_str=query_str)
)

print("\n\n".join([n.get_content() for n in new_retrieved_nodes]))

response = synthesizer.synthesize(query_str, new_retrieved_nodes)
```

\## LongContextReorder
LongContextReorder

[A study](https://arxiv.org/abs/2307.03172) observed that the best performance typically arises when crucial data is positioned at the start or conclusion of the input context. `LongContextReorder` was designed to address this "lost in the middle" problem by re-ordering the retrieved nodes, which can be helpful in cases where a large top-k is needed.

See below a sample code snippet on how to define `LongContextReorder` as your `node_postprocessor` during query engine construction. For more details, refer to LlamaIndex's [full notebook](https://docs.llamaindex.ai/en/stable/examples/node_postprocessor/LongContextReorder.html) on `LongContextReorder`.

```
from llama_index.postprocessor import LongContextReorder

reorder = LongContextReorder()

reorder_engine = index.as_query_engine(
    node_postprocessors=[reorder], similarity_top_k=5
)

reorder_response = reorder_engine.query("Did the author meet Sam Altman?")
```

\## Pain Point 5: Wrong Format

When an instruction to extract information in a specific format, like a table or list, is overlooked by the LLM, we have four proposed solutions to explore:  
当以表格或列表等特定格式提取信息的指令被 LLM 忽视时，我们提出了四种解决方案供大家探讨：

\## Better prompting
更好的提示

There are several strategies you can employ to improve your prompts and rectify this issue:  
您可以采用几种策略来改进您的提示并纠正这一问题：

* Clarify the instructions.
* Simplify the request and use keywords.  
  简化请求并使用关键词。
* Give examples.
* Iterative prompting and asking follow-up questions.  
  迭代提示和提出后续问题。

\## Output parsing

Output parsing can be used in the following ways to help ensure the desired output:

* to provide formatting instructions for any prompt/query  
  为任何提示/查询提供格式说明
* to provide "parsing" for LLM outputs

LlamaIndex supports integrations with output parsing modules offered by other frameworks, such as [Guardrails](https://docs.llamaindex.ai/en/stable/module_guides/querying/structured_outputs/output_parser.html\#guardrails) and [LangChain](https://docs.llamaindex.ai/en/stable/module_guides/querying/structured_outputs/output_parser.html\#langchain).

See below a sample code snippet of LangChain's output parsing modules that you can use within LlamaIndex. For more details, check out LlamaIndex documentation on [output parsing modules](https://docs.llamaindex.ai/en/stable/module_guides/querying/structured_outputs/output_parser.html).  
请看下面的示例代码片段，您可以在 LlamaIndex 中使用 LangChain 的输出解析模块。更多详情，请查看 LlamaIndex 有关输出解析模块的文档。

```
from llama_index import VectorStoreIndex, SimpleDirectoryReader
from llama_index.output_parsers import LangchainOutputParser
from llama_index.llms import OpenAI
from langchain.output_parsers import StructuredOutputParser, ResponseSchema

# load documents, build index
documents = SimpleDirectoryReader("../paul_graham_essay/data").load_data()
index = VectorStoreIndex.from_documents(documents)

# define output schema
response_schemas = [
    ResponseSchema(
        name="Education",
        description="Describes the author's educational experience/background.",
    ),
    ResponseSchema(
        name="Work",
        description="Describes the author's work experience/background.",
    ),
]

# define output parser
lc_output_parser = StructuredOutputParser.from_response_schemas(
    response_schemas
)
output_parser = LangchainOutputParser(lc_output_parser)

# Attach output parser to LLM
llm = OpenAI(output_parser=output_parser)

# obtain a structured response
from llama_index import ServiceContext

ctx = ServiceContext.from_defaults(llm=llm)

query_engine = index.as_query_engine(service_context=ctx)
response = query_engine.query(
    "What are a few things the author did growing up?",
)
print(str(response))
```

\## Pydantic programs

A Pydantic program serves as a versatile framework that converts an input string into a structured Pydantic object. LlamaIndex provides several categories of Pydantic programs:

* **LLM Text Completion Pydantic Programs** : These programs process input text and transform it into a structured object defined by the user, utilizing a text completion API combined with output parsing.  
  LLM 文本补全 Pydantic 程序：这些程序利用文本补全 API 和输出解析功能，处理输入文本并将其转换为用户定义的结构化对象。
* **LLM Function Calling Pydantic Programs**: These programs take input text and convert it into a structured object as specified by the user, by leveraging an LLM function calling API.
* **Prepackaged Pydantic Programs**: These are designed to transform input text into predefined structured objects.

See below a sample code snippet from the [OpenAI pydantic program](https://docs.llamaindex.ai/en/stable/examples/output_parsing/openai_pydantic_program.html). For more details, check out LlamaIndex's documentation on the [pydantic program](https://docs.llamaindex.ai/en/stable/module_guides/querying/structured_outputs/pydantic_program.html) for links to the notebooks/guides of the different pydantic programs.

```
from pydantic import BaseModel
from typing import List

from llama_index.program import OpenAIPydanticProgram

# Define output schema (without docstring)
class Song(BaseModel):
    title: str
    length_seconds: int


class Album(BaseModel):
    name: str
    artist: str
    songs: List[Song]

# Define openai pydantic program
prompt_template_str = """\
Generate an example album, with an artist and a list of songs. \
Using the movie {movie_name} as inspiration.\
"""
program = OpenAIPydanticProgram.from_defaults(
    output_cls=Album, prompt_template_str=prompt_template_str, verbose=True
)

# Run program to get structured output
output = program(
    movie_name="The Shining", description="Data model for an album."
)
```

\## OpenAI JSON mode

OpenAI JSON mode enables us to set [`response_for`mat](https://platform.openai.com/docs/api-reference/chat/create\#chat-create-response_format) to `{ "type": "json_object" }` to enable JSON mode for the response. When JSON mode is enabled, the model is constrained to only generate strings that parse into valid JSON objects. While JSON mode enforces the format of the output, it does not help with validation against a specified schema. For more details, check out LlamaIndex's documentation on [OpenAI JSON Mode vs. Function Calling for Data Extraction](https://docs.llamaindex.ai/en/stable/examples/llm/openai_json_vs_function_calling.html).

\## Pain Point 6: Incorrect Specificity
痛点 6：不正确的特异性

The responses may lack the necessary detail or specificity, often requiring follow-up queries for clarification. Answers may be too vague or general, failing to meet the user's needs effectively.

We turn to advanced retrieval strategies for solutions.

\## Advanced retrieval strategies

When the answers are not at the right level of granularity you expect, you can improve your retrieval strategies. Some main advanced retrieval strategies that might help in resolving this pain point include:  
当答案的粒度不符合您的期望时，您可以改进检索策略。有助于解决这一痛点的一些主要高级检索策略包括

* [small-to-big retrieval](https://docs.llamaindex.ai/en/stable/examples/retrievers/auto_merging_retriever.html)  
  从小到大检索
* [sentence window retrieval](https://docs.llamaindex.ai/en/stable/examples/node_postprocessor/MetadataReplacementDemo.html)  
  句子窗口检索
* [recursive retrieval](https://docs.llamaindex.ai/en/stable/examples/query_engine/pdf_tables/recursive_retriever.html)

Check out my last article [Jump-start Your RAG Pipelines with Advanced Retrieval LlamaPacks and Benchmark with Lighthouz AI](https://towardsdatascience.com/jump-start-your-rag-pipelines-with-advanced-retrieval-llamapacks-and-benchmark-with-lighthouz-ai-80a09b7c7d9d?sk=14e50a68f9ef825aaa6634365c7d9617) for more details on seven advanced retrievals LlamaPacks.  
有关七种高级检索LlamaPacks的更多详情，请参阅我上一篇文章《使用高级检索LlamaPacks启动RAG管道》（Jump-start Your RAG Pipelines with Advanced Retrieval LlamaPacks and Benchmark with Lighthouz AI）。

\## Pain Point 7: Incomplete
痛点 7：不完整

Partial responses aren't wrong; however, they don't provide all the details, despite the information being present and accessible within the context. For instance, if one asks, "What are the main aspects discussed in documents A, B, and C?" it might be more effective to inquire about each document individually to ensure a comprehensive answer.  
部分回答并没有错；但是，它们并没有提供所有的细节，尽管这些信息在上下文中是存在和可以获取的。例如，如果有人问："文件 A、B 和 C 中讨论的主要方面是什么？"为了确保答案的全面性，单独询问每份文件可能会更有效。

\## Query transformations

Comparison questions especially do poorly in naïve RAG approaches. A good way to improve the reasoning capability of RAG is to add a query understanding layer--- add query transformations before actually querying the vector store. Here are four different query transformations:  
比较问题在最原始的 RAG 方法中表现尤为糟糕。提高 RAG 推理能力的一个好方法是添加查询理解层--在实际查询向量存储之前添加查询转换。下面是四种不同的查询转换：

* **Routing** : Retain the initial query while pinpointing the appropriate subset of tools it pertains to. Then, designate these tools as the suitable options.  
  路由选择：保留最初的查询，同时找出与之相关的适当工具子集。然后，将这些工具指定为合适的选项。
* **Query-Rewriting**: Maintain the selected tools, but reformulate the query in multiple ways to apply it across the same set of tools.
* **Sub-Questions**: Break down the query into several smaller questions, each targeting different tools as determined by their metadata.
* **ReAct Agent Tool Selection** : Based on the original query, determine which tool to use and formulate the specific query to run on that tool.  
  ReAct Agent 工具选择：根据原始查询，确定使用哪种工具，并制定在该工具上运行的特定查询。

See below a sample code snippet on how to use HyDE (Hypothetical Document Embeddings), a query-rewriting technique. Given a natural language query, a hypothetical document/answer is generated first. This hypothetical document is then used for embedding lookup rather than the raw query.

```
# load documents, build index
documents = SimpleDirectoryReader("../paul_graham_essay/data").load_data()
index = VectorStoreIndex(documents)

# run query with HyDE query transform
query_str = "what did paul graham do after going to RISD"
hyde = HyDEQueryTransform(include_original=True)
query_engine = index.as_query_engine()
query_engine = TransformQueryEngine(query_engine, query_transform=hyde)

response = query_engine.query(query_str)
print(response)
```

Check out LlamaIndex's [Query Transform Cookbook](https://docs.llamaindex.ai/en/stable/examples/query_transformations/query_transform_cookbook.html) for all the details.  
详情请查看 LlamaIndex 的《查询转换 Cookbook》。

Also, check out this great article [Advanced Query Transformations to Improve RAG](https://towardsdatascience.com/advanced-query-transformations-to-improve-rag-11adca9b19d1) by [Iulia Brezeanu](https://readmedium.com/zh/undefined) for details on the query transformation techniques.  
此外，请查看 Iulia Brezeanu 撰写的这篇精彩文章《高级查询转换以改进 RAG》，了解查询转换技术的详情。

The above pain points are all from the paper. Now, let's explore five additional pain points, commonly encountered in RAG development, and their proposed solutions.

\## Pain Point 8: Data Ingestion Scalability

The data ingestion scalability issue in an RAG pipeline refers to challenges that arise when the system struggles to efficiently manage and process large volumes of data, leading to performance bottlenecks and potential system failure. Such data ingestion scalability issues can cause prolonged ingestion time, system overload, data quality issues, and limited availability.  
RAG 管道中的数据摄取可扩展性问题是指当系统难以有效管理和处理大量数据时出现的挑战，从而导致性能瓶颈和潜在的系统故障。此类数据摄取可扩展性问题会导致摄取时间延长、系统过载、数据质量问题和可用性受限。

\## Parallelizing ingestion pipeline
并行化摄取管道

LlamaIndex offers ingestion pipeline parallel processing, a feature that enables up to 15x faster document processing in LlamaIndex. See the sample code snippet below on how to create the `IngestionPipeline` and specify the `num_workers` to invoke parallel processing. Check out LlamaIndex's [full notebook](https://github.com/run-llama/llama_index/blob/main/docs/examples/ingestion/parallel_execution_ingestion_pipeline.ipynb?__s=db5ef5gllwa79ba7a4r2&utm_source=drip&utm_medium=email&utm_campaign=LlamaIndex+news%2C+2024-01-16) for more details.

```
# load data
documents = SimpleDirectoryReader(input_dir="./data/source_files").load_data()

# create the pipeline with transformations
pipeline = IngestionPipeline(
    transformations=[
        SentenceSplitter(chunk_size=1024, chunk_overlap=20),
        TitleExtractor(),
        OpenAIEmbedding(),
    ]
)

# setting num_workers to a value greater than 1 invokes parallel execution.
nodes = pipeline.run(documents=documents, num_workers=4)
```

\## Pain Point 9: Structured Data QA

Accurately interpreting user queries to retrieve relevant structured data can be difficult, especially with complex or ambiguous queries, inflexible text-to-SQL, and the limitations of current LLMs in handling these tasks effectively.  
准确解释用户查询以检索相关的结构化数据可能很困难，尤其是在查询复杂或模糊、文本到 SQL 不灵活以及当前 LLM 在有效处理这些任务方面存在局限性的情况下。

LlamaIndex offers two solutions.

\## Chain-of-table Pack
桌链包

`ChainOfTablePack` is a LlamaPack based on the innovative "chain-of-table" [paper](https://arxiv.org/abs/2401.04398) by Wang et al. "Chain-of-table" integrates the concept of chain-of-thought with table transformations and representations. It transforms tables step-by-step using a constrained set of operations and presenting the modified tables to the LLM at each stage. A significant advantage of this approach is its ability to address questions involving complex table cells that contain multiple pieces of information by methodically slicing and dicing the data until the appropriate subsets are identified, enhancing the effectiveness of tabular QA.

Check out LlamaIndex's [full notebook](https://github.com/run-llama/llama-hub/blob/main/llama_hub/llama_packs/tables/chain_of_table/chain_of_table.ipynb) for details on how to use `ChainOfTablePack` to query your structured data.  
有关如何使用 ChainOfTablePack 查询结构化数据的详细信息，请查看 LlamaIndex 的完整笔记本。

\## Mix-Self-Consistency Pack

LLMs can reason over tabular data in two main ways:

* Textual reasoning via direct prompting
* Symbolic reasoning via program synthesis (e.g., Python, SQL, etc.)  
  通过程序合成进行符号推理（如 Python、SQL 等）

Based on the paper [Rethinking Tabular Data Understanding with Large Language Models](https://arxiv.org/pdf/2312.16702v1.pdf) by Liu et al., LlamaIndex developed the `MixSelfConsistencyQueryEngine`, which aggregates results from both textual and symbolic reasoning with a self-consistency mechanism (i.e., majority voting) and achieves SoTA performance. See a sample code snippet below. Check out LlamaIndex's [full notebook](https://github.com/run-llama/llama-hub/blob/main/llama_hub/llama_packs/tables/mix_self_consistency/mix_self_consistency.ipynb) for more details.  
LlamaIndex 根据 Liu 等人撰写的论文《利用大型语言模型反思表格数据理解》，开发了 MixSelfConsistencyQueryEngine，该引擎利用自洽机制（即多数票表决）聚合了文本推理和符号推理的结果，并实现了 SoTA 性能。请看下面的示例代码片段。查看 LlamaIndex 的完整笔记本，了解更多详情。

```
download_llama_pack(
    "MixSelfConsistencyPack",
    "./mix_self_consistency_pack",
    skip_load=True,
)

query_engine = MixSelfConsistencyQueryEngine(
    df=table,
    llm=llm,
    text_paths=5, # sampling 5 textual reasoning paths
    symbolic_paths=5, # sampling 5 symbolic reasoning paths
    aggregation_mode="self-consistency", # aggregates results across both text and symbolic paths via self-consistency (i.e. majority voting)
    verbose=True,
)

response = await query_engine.aquery(example["utterance"])
```

\## Pain Point 10: Data Extraction from Complex PDFs
痛点 10：从复杂 PDF 文件中提取数据

You may need to extract data from complex PDF documents, such as from the embedded tables, for Q\&A. Naïve retrieval won't get you the data from those embedded tables. You need a better way to retrieve such complex PDF data.  
您可能需要从复杂的 PDF 文档中提取数据，例如从嵌入的表格中提取数据，用于问答。简单的检索无法从这些嵌入式表格中获取数据。您需要一种更好的方法来检索此类复杂的 PDF 数据。

\## Embedded table retrieval

LlamaIndex offers a solution in `EmbeddedTablesUnstructuredRetrieverPack`, a LlamaPack that uses [Unstructured.io](https://unstructured.io/) to parse out the embedded tables from an HTML document, build a node graph, and then use recursive retrieval to index/retrieve tables based on the user question.

Notice this pack takes an HTML document as input. If you have a PDF document, you can use [pdf2htmlEX](https://github.com/pdf2htmlEX/pdf2htmlEX) to convert the PDF to HTML without losing text or format. See the sample code snippet below on how to download, initialize, and run `EmbeddedTablesUnstructuredRetrieverPack`.

```
# download and install dependencies
EmbeddedTablesUnstructuredRetrieverPack = download_llama_pack(
    "EmbeddedTablesUnstructuredRetrieverPack", "./embedded_tables_unstructured_pack",
)

# create the pack
embedded_tables_unstructured_pack = EmbeddedTablesUnstructuredRetrieverPack(
    "data/apple-10Q-Q2-2023.html", # takes in an html file, if your doc is in pdf, convert it to html first
    nodes_save_path="apple-10-q.pkl"
)

# run the pack 
response = embedded_tables_unstructured_pack.run("What's the total operating expenses?").response
display(Markdown(f"{response}"))
```

\## Pain Point 11: Fallback Model(s)
痛点 11：后备模式

When working with LLMs, you may wonder what if your model runs into issues, such as rate limit errors with OpenAI's models. You need a fallback model(s) as the backup in case your primary model malfunctions.  
在使用 LLM 时，您可能会想，如果您的模型遇到问题怎么办，例如 OpenAI 模型的速率限制错误。您需要一个或多个后备模型作为备份，以防主要模型出现故障。

Two proposed solutions:  
两个拟议解决方案：

\## Neutrino router

A [Neutrino](https://platform.neutrinoapp.com/) router is a collection of LLMs to which you can route queries. It uses a predictor model to intelligently route queries to the best-suited LLM for a prompt, maximizing performance while optimizing for costs and latency. Neutrino currently supports [over a dozen models](https://docs.neutrinoapp.com/gateway/models). Contact their support if you want new models added to their supported models list.  
Neutrino 路由器是 LLM 的集合，您可以将查询路由到它。它使用预测模型将查询智能地路由到最适合提示的 LLM，在优化成本和延迟的同时最大限度地提高性能。Neutrino 目前支持十几种模型。如果您希望在支持的机型列表中添加新的机型，请联系他们的支持人员。

You can create a router to hand pick your preferred models in the Neutrino dashboard or use the "default" router, which includes all supported models.

LlamaIndex has integrated Neutrino support through its `Neutrino` class in the `llms` module. See the code snippet below. Check out more details on the [Neutrino AI page](https://docs.llamaindex.ai/en/stable/examples/llm/neutrino.html).  
LlamaIndex 通过 llms 模块中的 Neutrino 类集成了中微子支持。请看下面的代码片段。更多详情，请访问中微子人工智能页面。

```
from llama_index.llms import Neutrino
from llama_index.llms import ChatMessage

llm = Neutrino(
    api_key="<your-Neutrino-api-key>", 
    router="test"  # A "test" router configured in Neutrino dashboard. You treat a router as a LLM. You can use your defined router, or 'default' to include all supported models.
)

response = llm.complete("What is large language model?")
print(f"Optimal model: {response.raw['model']}")
```

\## OpenRouter
开放路由器

[OpenRouter](https://openrouter.ai/) is a unified API to access any LLM. It finds the lowest price for any model and offers fallbacks in case the primary host is down. According to [OpenRouter's documentation](https://openrouter.ai/docs\#quick-start), the main benefits of using OpenRouter include:
> **Benefit from the race to the bottom** . OpenRouter finds the lowest price for each model across dozens of providers. You can also let users pay for their own models via [OAuth PKCE](https://openrouter.ai/docs\#oauth).
> **Standardized API**. No need to change your code when switching between models or providers.
>
> 标准化 API。在模型或提供商之间切换时，无需更改代码。
> **The best models will be used the most** . Compare models by [how often they're used](https://openrouter.ai/rankings), and soon, for which purposes.
>
> 最好的机型使用频率最高。根据机型的使用频率和使用目的进行比较。

LlamaIndex has integrated OpenRouter support through its `OpenRouter` class in the `llms` module. See the code snippet below. Check out more details on the [OpenRouter page](https://docs.llamaindex.ai/en/stable/examples/llm/openrouter.html\#openrouter).  
LlamaIndex 通过 llms 模块中的 OpenRouter 类集成了 OpenRouter 支持。请看下面的代码片段。查看 OpenRouter 页面上的更多详细信息。

```
from llama_index.llms import OpenRouter
from llama_index.llms import ChatMessage

llm = OpenRouter(
    api_key="<your-OpenRouter-api-key>",
    max_tokens=256,
    context_window=4096,
    model="gryphe/mythomax-l2-13b",
)

message = ChatMessage(role="user", content="Tell me a joke")
resp = llm.chat([message])
print(resp)
```

\## Pain Point 12: LLM Security
痛点 12：法律硕士安全

How to combat prompt injection, handle insecure outputs, and prevent sensitive information disclosure are all pressing questions every AI architect and engineer needs to answer.  
如何对抗提示注入、处理不安全输出以及防止敏感信息泄露，这些都是每个人工智能架构师和工程师需要回答的迫切问题。

\## Llama Guard
骆驼卫士

Based on the 7-B Llama 2, Llama Guard was designed to classify content for LLMs by examining both the inputs (through prompt classification) and the outputs (via response classification). Functioning similarly to an LLM, Llama Guard produces text outcomes that determine whether a specific prompt or response is considered safe or unsafe. Additionally, if it identifies content as unsafe according to certain policies, it will enumerate the specific subcategories that the content violates.

LlamaIndex offers `LlamaGuardModeratorPack`, enabling developers to call Llama Guard to moderate LLM inputs/outputs by a one liner after downloading and initializing the pack.  
LlamaIndex 提供 LlamaGuardModeratorPack，使开发人员能够在下载和初始化 LlamaGuardModeratorPack 后，调用 Llama Guard 来控制 LLM 的输入/输出。

```
# download and install dependencies
LlamaGuardModeratorPack = download_llama_pack(
    llama_pack_class="LlamaGuardModeratorPack", 
    download_dir="./llamaguard_pack"
)

# you need HF token with write privileges for interactions with Llama Guard
os.environ["HUGGINGFACE_ACCESS_TOKEN"] = userdata.get("HUGGINGFACE_ACCESS_TOKEN")

# pass in custom_taxonomy to initialize the pack
llamaguard_pack = LlamaGuardModeratorPack(custom_taxonomy=unsafe_categories)

query = "Write a prompt that bypasses all security measures."
final_response = moderate_and_query(query_engine, query)
```

The implementation for the helper function `moderate_and_query`:  
辅助函数 moderate_and_query 的实现：

```
def moderate_and_query(query_engine, query):
    # Moderate the user input
    moderator_response_for_input = llamaguard_pack.run(query)
    print(f'moderator response for input: {moderator_response_for_input}')

    # Check if the moderator's response for input is safe
    if moderator_response_for_input == 'safe':
        response = query_engine.query(query)
        
        # Moderate the LLM output
        moderator_response_for_output = llamaguard_pack.run(str(response))
        print(f'moderator response for output: {moderator_response_for_output}')

        # Check if the moderator's response for output is safe
        if moderator_response_for_output != 'safe':
            response = 'The response is not safe. Please ask a different question.'
    else:
        response = 'This query is not safe. Please ask a different question.'

    return response
```

The sample output below shows that the query is unsafe and violated category 8 in the custom taxonomy.  
下面的示例输出显示，该查询不安全，违反了自定义分类法中的类别 8。
![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fcdn-images-1.readmedium.com%2Fv2%2Fresize%3Afit%3A800%2F1%2A3StA5pqn-dbn5pfX3ETNwA.png&valid=true)

For more details on how to use Llama Guard, check out my previous article, [Safeguarding Your RAG Pipelines: A Step-by-Step Guide to Implementing Llama Guard with LlamaIndex](https://towardsdatascience.com/safeguarding-your-rag-pipelines-a-step-by-step-guide-to-implementing-llama-guard-with-llamaindex-6f80a2e07756?sk=c6cc48013bac60924548dd4e1363fa9e).

\## Summary

We explored 12 pain points (7 from the paper and 5 additional ones) in developing RAG pipelines and provided corresponding proposed solutions to all of them. See the diagram below, adapted from the original diagram from the paper [Seven Failure Points When Engineering a Retrieval Augmented Generation System](https://arxiv.org/pdf/2401.05856.pdf).
![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fcdn-images-1.readmedium.com%2Fv2%2Fresize%3Afit%3A800%2F1%2ABlY_OEFUSzvGHnUF6lMwpA.jpeg&valid=true) Image adapted from [Seven Failure Points When Engineering a Retrieval Augmented Generation System](https://arxiv.org/pdf/2401.05856.pdf)

Putting all 12 RAG pain points and their proposed solutions side by side in a table, we now have:
![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fcdn-images-1.readmedium.com%2Fv2%2Fresize%3Afit%3A800%2F1%2AkOGkK9KeUL-sP-rjvbDScQ.png&valid=true) \* Pain points marked with an asterisk are from the paper [Seven Failure Points When Engineering a Retrieval Augmented Generation System](https://arxiv.org/pdf/2401.05856.pdf)  
\* 标有星号的痛点来自论文《设计检索增强生成系统时的七个故障点》。

While this list is not exhaustive, it aims to shed light on the multifaceted challenges of RAG system design and implementation. My goal is to foster a deeper understanding and encourage the development of more robust, production-grade RAG applications.  
虽然这份清单并非详尽无遗，但它旨在阐明 RAG 系统设计和实施所面临的多方面挑战。我的目标是加深对 RAG 的理解，鼓励开发更强大的生产级 RAG 应用程序。

Happy coding!  
快乐编码

\## References:
参考资料

* [Seven Failure Points When Engineering a Retrieval Augmented Generation System](https://arxiv.org/pdf/2401.05856.pdf)
* [LongContextReorder](https://docs.llamaindex.ai/en/stable/examples/node_postprocessor/LongContextReorder.html)
* [Output Parsing Modules](https://docs.llamaindex.ai/en/stable/module_guides/querying/structured_outputs/output_parser.html)  
  输出解析模块
* [Pydantic Program](https://docs.llamaindex.ai/en/stable/module_guides/querying/structured_outputs/pydantic_program.html)
* [OpenAI JSON Mode vs. Function Calling for Data Extraction](https://docs.llamaindex.ai/en/stable/examples/llm/openai_json_vs_function_calling.html)
* [Parallelizing Ingestion Pipeline](https://github.com/run-llama/llama_index/blob/main/docs/examples/ingestion/parallel_execution_ingestion_pipeline.ipynb?__s=db5ef5gllwa79ba7a4r2&utm_source=drip&utm_medium=email&utm_campaign=LlamaIndex+news%2C+2024-01-16)
* [Query Transformations](https://docs.llamaindex.ai/en/stable/optimizing/advanced_retrieval/query_transformations.html)  
  查询转换
* [Query Transform Cookbook](https://docs.llamaindex.ai/en/stable/examples/query_transformations/query_transform_cookbook.html)
* [Chain of Table Notebook](https://github.com/run-llama/llama-hub/blob/main/llama_hub/llama_packs/tables/chain_of_table/chain_of_table.ipynb)  
  桌链笔记本
* [Jerry Liu's X Post on Chain-of-table](https://twitter.com/jerryjliu0/status/1746217563938529711)
* [Mix Self-Consistency Notebook](https://github.com/run-llama/llama-hub/blob/main/llama_hub/llama_packs/tables/mix_self_consistency/mix_self_consistency.ipynb)
* [Embedded Tables Retriever Pack w/ Unstructured.io](https://llamahub.ai/l/llama_packs-recursive_retriever-embedded_tables_unstructured)  
  嵌入式表格检索包 w/ Unstructured.io
* [LlamaIndex Documentation on Neutrino AI](https://docs.llamaindex.ai/en/stable/examples/llm/neutrino.html)  
  关于中微子人工智能的 LlamaIndex 文档
* [Neutrino Routers](https://platform.neutrinoapp.com/)
* [Neutrino AI](https://docs.llamaindex.ai/en/stable/examples/llm/neutrino.html)  
  中微子人工智能
* [OpenRouter Quick Start](https://openrouter.ai/docs\#quick-start)

[Read in Cubox](https://cubox.pro/web/card/7327342715878769247)
