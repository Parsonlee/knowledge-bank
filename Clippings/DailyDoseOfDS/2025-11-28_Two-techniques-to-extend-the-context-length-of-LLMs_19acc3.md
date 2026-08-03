# Two techniques to extend the context length of LLMs

- **原邮件主题**: How to Use kNNs for Imbalanced Datasets
- **发送人**: Daily Dose of DS <avi@dailydoseofds.com>
- **日期**: Fri, 28 Nov 2025 20:46:01 +0000
- **ID**: 19acc373a89bc8c4

---

## [**Two techniques to extend the context length of LLMs**](<https://www.dailydoseofds.com/implementing-massively-parallelized-cuda-programs-from-scratch-using-cuda-programming/>)

Consider this:

  * GPT-3.5-turbo had a context window of 4,096 tokens.
  * Later, GPT-4 took that to 8,192 tokens.
  * Claude 2 reached 100,000 tokens.
  * Llama 3.1 → 128,000 tokens.
  * Gemini → 1M+ tokens.

We have been making great progress in extending the context window of LLMs.

Today, let's understand some techniques that help us unlock this.

* * *

# **What's the challenge?**

In a traditional transformer, a model processing 4,096 tokens requires **64 times more computation** (quadratic growth) than one handling 512 tokens due to the attention mechanism.

![](https://embed.filekitcdn.com/e/k7YHPN24SoxyM8nGKZnDxa/pHwM2WdNJ6C9G6JUF5hsCK/email)   
---  
  
Thus, having a longer context window isn't just as easy as increasing the size of the matrices, if you will.

But at least we have narrowed down the bottleneck.

If we can optimize this quadratic complexity, we have optimized the network.

_A quick note: This bottleneck was already known way back in 2017 when transformers were introduced. Since GPT-3, most LLMs have utilized non-quadratic approaches for attention computation._

* * *

# **1) Approximate attention using Sparse Attention**

Instead of computing attention scores between all pairs of tokens, sparse attention limits that to a subset of tokens, which will reduce the computations.

There are two common ways:

  * Use local attention, where tokens attend only to their neighbors.
  * Let the model learn which tokens to focus on.

![](https://embed.filekitcdn.com/e/k7YHPN24SoxyM8nGKZnDxa/eh7aTinGW8ZApFrgLeTWJz/email)   
---  
  
As you may have guessed, there's a trade-off between computational complexity and performance.

# **2) Flash Attention**

This is a fast and memory-efficient method that retains the exactness of traditional attention mechanisms.

![](https://embed.filekitcdn.com/e/k7YHPN24SoxyM8nGKZnDxa/91rxVM5Hee7GJCgKNDqcYX/email)   
---  
  
The whole idea revolves around optimizing the data movement within GPU memory. Here are some background details and how it works.

In a GPU:

  * A **thread** is the smallest unit of execution.
  * A group of threads is called a **block**.

![](https://substackcdn.com/image/fetch/$s_!h50G!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F469f5487-0d4c-42b3-870f-64036ab5a8f6_2217x798.jpeg)   
---  
  
Also:

![](https://substackcdn.com/image/fetch/$s_!XClj!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F24561a7c-904d-429d-8f36-a781c9bb6134_2134x1080.jpeg)   
---  
  
  * A block executes the same kernel (function, to simplify) and its threads cooperate by sharing a fast memory block called SRAM.
  * Also, all blocks together can access a shared global memory block in the GPU called HBM.

A note about SRAM and HBM:

  * SRAM is scarce but extremely fast.
  * HBM is much more abundant but slow (typically 8-15x slower).

The quadratic attention and typical optimizations involve plenty of movement of large matrices between SRAM and HBM:

![](https://substackcdn.com/image/fetch/$s_!H9IM!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F8775aa17-0917-4789-928e-027dcf135fa0_2409x420.jpeg)   
---  
  
  * First, the product of query (Q) and key (K) is distributed to threads, computed, and brought back to HBM.
  * Next, the above result is again distributed to threads to compute the softmax of the product and brought back to HBM once it is done.

Flash attention reduces the repeated movements by utilizing SRAM to cache the intermediate results.

This way, redundant movements are reduced, and typically, this offers a speedup of up to 7.6x over standard attention methods.

Also, it scales linearly with sequence length, which is also great.

* * *

While reducing the computational complexity is crucial, **this is not sufficient**.

See, using the above optimization, we have made it practically feasible to pass longer contexts without drastically increasing the computation cost.

However, the model must know how to comprehend longer contexts and the relative position of tokens.

That is why selecting the right positional embeddings is crucial.

![](https://embed.filekitcdn.com/e/k7YHPN24SoxyM8nGKZnDxa/uesVqT76BbRZYGf1k3Hwuo/email)   
---  
  
Rotary positional embeddings (RoPE) usually work the best since they preserve both the relative position and the relation.

If you want to learn more about RoPE, let us know. We can cover it in another issue.

In the meantime, if you want to get into the internals of CUDA GPU programming and understand the internals of GPU, how it works, and learn how CUDA programs are built, we covered it here: [](<https://www.dailydoseofds.com/implementing-massively-parallelized-cuda-programs-from-scratch-using-cuda-programming/>)[**Implementing (Massively) Parallelized CUDA Programs From Scratch Using CUDA Programming**](<https://www.dailydoseofds.com/implementing-massively-parallelized-cuda-programs-from-scratch-using-cuda-programming/>).
