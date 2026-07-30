---
title: "Why small models alone don't reduce inference costs"
source: "https://mail.google.com/mail/u/0/#inbox/19f6784a03ed6e1e"
author:
  - "[[DailyDoseOfDS]]"
published: 2026-07-15
created: 2026-07-30
description: "阐述为何仅依赖小型专用模型（Small Models）无法从根本上降低 LLM 推理成本。分析显存预留、硬件闲置与多模型部署瓶颈，并介绍开源单引擎推理架构 SIE（Superlinked Inference Engine）的共享 GPU 与自适应加载机制。"
tags:
  - clippings
---

# 为什么仅靠小模型无法降低推理成本（Why small models alone don't reduce inference costs）

在 AI 系统设计中，使用小型专用模型（Small, Specialized Models）处理特定任务已成为广泛共识。它们在受控任务上准确率足够高，同时能保证数据留在本地私有环境中。

**但是，仅仅换用小模型本身并不能降低推理成本。**

它只是将计费方式从“按 Token 付费”转变成了“按租用的 GPU 显卡付费”。如果你为每一个小模型都单独分配一块 GPU，绝大多数硬件在大部分时间内都会处于**闲置状态**，而你依然需要为其买单。

只有当多个模型能够**共享 GPU** 时，成本节省才会真正显现。而这需要一个能够同时运行所有这些模型的统一引擎，因为一旦你用不同的工具去服务每个模型，每个模型就又会独占一块 GPU。

本文将深入探讨开源推理引擎 **SIE（Superlinked Inference Engine）** 如何通过统一架构解决这一瓶颈。

---

### 一、 传统小模型部署的显存与计算浪费

在传统的推理引擎（如标准 vLLM 或 Triton）中，部署多模型流水线面临两大浪费：

1. **显存预留但闲置（Reserved-but-idle）**：多个公共 vLLM 的 issue 表明，模型在加载时会预留显卡约 80% 的显存，但在嵌入（Embedding）等任务期间，实际显存利用率经常低于 40%。
2. **批处理中的填充浪费（Padding Overhead）**：即使在满载批处理内部，不同请求的长度各异。简单的做法是将短请求填充（Pad）到与最长请求一致，从而浪费大量 GPU 算力处理无意义的 Padding。

---

### 二、 SIE 引擎的核心解决机制

开源项目 **SIE** 实现了一种全新的共享推理架构，允许在一个共享集群上运行 Agent 所需的各种不同模型，让 GPU 保持繁忙而非闲置：

![基于流量的自适应模型加载与淘汰策略](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fce46d84f-77f6-4bad-af03-4dedb6a6f9c1_2485x1191.jpeg)

* **按计算成本做 Batching**：SIE 根据请求的计算开销进行分组，仅填充至该 Batch 内的最长项，而非全局最大值，几乎零算力浪费。
* **全局共享队列**：网关（Gateway）将所有请求发布到单个共享队列中，各 Worker 从该 Pool 中拉取任务并在触碰 GPU 前组装成完整的 Batch。
* **自适应加载与淘汰（Load & Eviction）**：模型在首次收到请求时才加载到 GPU 显存中，当显存不足时自动淘汰最久未使用（LRU）的模型，类似于浏览器缓存机制。

![开箱即用的预调优模型配置](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fbb25d1fa-a42d-435a-9f65-e6ad52a24a50_1902x1428.png)

* **开箱即用的最佳配置**：不同于 vLLM 需手动调优 Batch 大小、显存比例与精度，SIE 目录中的 85+ 个模型均自带生产验证过的配置文件，按名称引用即可自动以最优参数加载。

---

### 三、 生产级端到端流水线代码实现

下面展示在一个 SIE 单服务器上同时运行包含 4 种不同模型架构（Embedding、Cross-Encoder Reranker、NER Extraction 和 Generative Output）的完整检索与推理流水线：

#### 1. 启动与初始化客户端

```bash
# 启动 SIE 服务器（以端口 8080 为例）
sie serve --port 8080
```

```python
from sie import SIEClient

# 实例化客户端，后续所有模型调用均走此单端点
client = SIEClient(base_url="http://localhost:8080")
```

#### 2. 执行向量嵌入 (Encode)

将输入文本列表转换为密集向量：

```python
passages = [
    "Invoice line #4021 for server hardware",
    "Payment terms: Net 30 days via wire transfer",
    "Cafeteria menu for Wednesday: Tacos and Salad"
]

# 调用 encode 接口生成 dense vector
encode_res = client.encode(
    model="bge-small-en-v1.5",
    inputs=passages
)
print("嵌入结果向量维度:", len(encode_res[0]["dense"]))
```

#### 3. 执行交叉编码重排序 (Score / Rerank)

使用 Cross-Encoder 同时读取 Query 与各段落并计算相关性得分：

```python
query = "What are the payment conditions?"
scores = client.score(
    model="bge-reranker-large",
    query=query,
    documents=passages
)

# 返回按相关性降序排列的结果
top_passage = scores[0]["document"]
print("最佳匹配段落:", top_passage)
```

#### 4. 执行命名实体提取 (Extract)

利用抽取模型识别特定字段 span：

```python
extraction = client.extract(
    model="gliner-bi-edge",
    text=top_passage,
    schema=["payment_term", "due_date"]
)
print("提取实体字段:", extraction)
```

#### 5. 执行生成式回答 (Generate)

最终将 Top 匹配上下文喂给生成式模型生成回答（底层由 SGLang 驱动 GPU 路线）：

```python
response = client.generate(
    model="Qwen2.5-Coder-7B-Instruct",
    prompt=f"Based on context: {top_passage}, answer the query: {query}"
)
print("生成最终回答:", response.text)
```

---

### 四、 总结与工程考量

包含 4 种模型家族、4 种输出类型的完整流水线，均在单个 SIE 进程和单个客户端下高效完成。

切换到小模型并不自然意味着推理变便宜；只有当多个小模型能够**共享 GPU 算力集群**并消除闲置开销时，成本优势才会彻底兑现。

开源项目 SIE (github.com/superlinked/sie) 提供了这一开箱即用的解决方案，并与 Chroma、Qdrant、Weaviate、LanceDB 等标准检索栈深度集成。
