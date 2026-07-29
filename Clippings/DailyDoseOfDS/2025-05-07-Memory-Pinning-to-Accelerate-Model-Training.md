---
title: Memory Pinning to Accelerate Model Training
source: https://mail.google.com/mail/u/0/#inbox/196ac3a283f20357
author:
  - "[[DailyDoseOfDS]]"
published: 2025-05-07
created: 2026-07-29
description: DailyDoseOfDS 通讯深度解析：包含 Memory Pinning to Accelerate Model Training 的原理剖析与工程实践。
tags:
  - clippings
---

# Memory Pinning to Accelerate Model Training

## 1. 核心要点解析

本期内容重点涵盖：
- **Memory Pinning to Accelerate Model Training**

## 2. 深度拆解与正文翻译

​

----------------------
In today's newsletter:
----------------------

* A web browser for your AI.
* Memory Pinning to accelerate model training.
* [Hands-on] ​Multimodal RAG with DeepSeek Janus​.​

Reading time: 3 minutes.

TODAY'S ISSUE

Together with browserbase
-------------------------

-----------------------------------------------------------------
​A web browser for your AI (
https://click.convertkit-mail2.com/4zuwmw6lz0hehpqxvrobxh64mvm77h5/x0hph6hezrog7rt5/aHR0cHM6Ly9kdWIuc2gvYmIx
)​
-----------------------------------------------------------------

Browserbase powers web browsing capabilities for AI agents and
applications.

If you’re building automations that need to interact with
websites, fill out forms, or replicate users’ actions,
Browserbase manages that infrastructure so you don’t have to
maintain your fleet of headless browsers.

(
https://click.convertkit-mail2.com/4zuwmw6lz0hehpqxvrobxh64mvm77h5/6qheh8hlwkzq25bo/aHR0cHM6Ly9zdGFnZWgubGluay9jb21w
)​
With the excitement of Open AI's new Computer Using Agent API,
Browserbase has built an open-source version of this toolkit—CUA
Browser (
https://click.convertkit-mail2.com/4zuwmw6lz0hehpqxvrobxh64mvm77h5/6qheh8hlwkzq25bo/aHR0cHM6Ly9zdGFnZWgubGluay9jb21w
), for you to try out yourself.

-->Try CUA Browser (
https://click.convertkit-mail2.com/4zuwmw6lz0hehpqxvrobxh64mvm77h5/6qheh8hlwkzq25bo/aHR0cHM6Ly9zdGFnZWgubGluay9jb21w
)
Try CUA Browser ( https://stageh.link/comp )Supercharge your CUA
with Browserbase's reliable, scalable browser infrastructure, and
sign up for free (
https://click.convertkit-mail2.com/4zuwmw6lz0hehpqxvrobxh64mvm77h5/kkhmh6hnedr79efl/aHR0cHM6Ly9zdGFnZWgubGluay9zaWdudXA=
).

TODAY's Daily dose of data science
----------------------------------

-------------------------------------------
Memory Pinning to accelerate model training
-------------------------------------------

If you regularly use GPUs to accelerate model training, let us
show you a simple technique to accelerate model training…

…by changing just two lines of code.

Let’s begin!

Here’s how we typically train a neural network using PyTorch:

​
* Line 5 transfers the data to the GPU from the CPU.
* Everything executes on the GPU after the data transfer, i.e.,
lines 7-15.

This means:

​
* When the GPU is working, the CPU is idle,
* And when the CPU is working, the GPU is idle.

This can be optimized as follows:

* When the model is being trained on the 1st mini-batch, the CPU
can transfer the 2nd mini-batch to the GPU.
* This ensures that the GPU does not have to wait for the next
mini-batch as soon as it has processed the current mini-batch.

Thus, the resource utilization chart should look like:

​
While the CPU may remain idle, this ensures that the GPU (which
is the actual accelerator) is never idle.

This is known as memory pinning, and it is used to speed up the
data transfer from the CPU to the GPU by making the training
workflow asynchronous.

Enabling this is quite simple in PyTorch.

1) First, when defining the DataLoader object, set
pin_memory=True and specify num_workers.

​
2) During the data transfer step in the training step, specify
non_blocking=True, as depicted below:

​
Done!

The speedup with a simple neural network is depicted below:

* Without memory pinning, the model takes 43 seconds to train on
5 epochs.

​
* But with memory pinning, the same model trains in less than 10
seconds:

​
That said, remember that if several tensors are allocated to the
pinned memory, it will block a substantial portion of RAM.

This impacts the memory available to other operations. Thus,
always profile your code to track the memory consumption.

Also, if the tensors are small, memory pinning has a negligible
effect since the data transfer from the CPU to the GPU does not
take that time anyway:

​
👉 Over to you: What are some other ways to optimize model
training?

One way is multi-GPU training, which we covered here: A
Beginner-friendly Guide to Multi-GPU Model Training (
https://click.convertkit-mail2.com/4zuwmw6lz0hehpqxvrobxh64mvm77h5/58hvh7hg0vqe9oc6/aHR0cHM6Ly93d3cuZGFpbHlkb3Nlb2Zkcy5jb20vYS1iZWdpbm5lci1mcmllbmRseS1ndWlkZS10by1tdWx0aS1ncHUtbW9kZWwtdHJhaW5pbmcv
).

And here are 15 more ways to optimize neural network training: 15
Ways to Optimize Neural Network Training (With Implementation) (
https://click.convertkit-mail2.com/4zuwmw6lz0hehpqxvrobxh64mvm77h5/25h2hoh3gv65oec3/aHR0cHM6Ly93d3cuZGFpbHlkb3Nlb2Zkcy5jb20vMTUtd2F5cy10by1vcHRpbWl6ZS1uZXVyYWwtbmV0d29yay10cmFpbmluZy13aXRoLWltcGxlbWVudGF0aW9uLw==
).

Lastly, here’s an article that teaches CUDA programming from
scratch, which will help you understand the underlying details of
CUDA and how it works: Implementing (Massively) Parallelized CUDA
Programs From Scratch Using CUDA Programming (
https://click.convertkit-mail2.com/4zuwmw6lz0hehpqxvrobxh64mvm77h5/qvh8h7hdv7zx66cl/aHR0cHM6Ly93d3cuZGFpbHlkb3Nlb2Zkcy5jb20vaW1wbGVtZW50aW5nLW1hc3NpdmVseS1wYXJhbGxlbGl6ZWQtY3VkYS1wcm9ncmFtcy1mcm9tLXNjcmF0Y2gtdXNpbmctY3VkYS1wcm9ncmFtbWluZy8=
).

In case you missed it
---------------------

-----------------------------------------------------------------
​MultiModal RAG with DeepSeek Janus (
https://click.convertkit-mail2.com/4zuwmw6lz0hehpqxvrobxh64mvm77h5/g3hnh5hmndrvzebr/aHR0cHM6Ly93d3cuZGFpbHlkb3Nlb2Zkcy5jb20vcC9tdWx0aW1vZGFsLXJhZy11c2luZy1kZWVwc2Vla3MtamFudXMv
)​
-----------------------------------------------------------------

After DeepSeek-R1, DeepSeek also dropped more open-weight
multimodal models—Janus, Janus-Pro, and Janus-Flow.

They can understand images and generate images from text input.

Moreover, they beat OpenAI's DALL-E 3 and Stable Diffusion in
GenEval and DPG-Bench benchmarks.

Recently, we did a hands-on demo of building a multimodal RAG
with Janus-Pro on a complex document shown below:

​
​Read the detail

## 3. 工程落地与实践指南

1. **架构实践**：遵循模块化与低偶合设计原则，保障服务高可用。
2. **性能基准**：结合上下文剪枝与向量重排序技术提升延迟表现。
3. **运维与安全**：持续监控模型采样行为与安全防护。
