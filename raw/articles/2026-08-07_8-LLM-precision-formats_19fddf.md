---
title: 8 LLM precision formats
source_key: dailydoseofds
email_subject: '[Hands-on] Build Semantic Search Inside Your Database Without an Embedding
  Pipeline'
email_sender: Daily Dose of DS <avi@dailydoseofds.com>
email_date: Fri, 07 Aug 2026 20:42:13 +0000
email_id: 19fddf64edb10546
article_id: 19fddf64edb10546:1
published: '2026-08-07'
tags:
- LLM/inference
- LLM/training
- Infra/gpu
---

#  8 LLM precision formats 

- **原邮件主题**: [Hands-on] Build Semantic Search Inside Your Database Without an Embedding Pipeline
- **发送人**: Daily Dose of DS <avi@dailydoseofds.com>
- **日期**: Fri, 07 Aug 2026 20:42:13 +0000
- **ID**: 19fddf64edb10546

---

## [**8 LLM precision formats**](<https://www.dailydoseofds.com/p/5-llm-quantization-techniques/>)

A 12GB consumer GPU cannot hold a 7B model in FP32, which needs 28GB just for the weights.

But running `ollama run llama3` on that card works anyway.

The reason is that Ollama does not ship weights in FP32.

Instead, it pulls a Q4_K_M GGUF by default, which averages around 4.8 bits per weight and puts a 7B model near 4.1GB.

[**We covered several different LLM quantization techniques here →**](<https://www.dailydoseofds.com/p/5-llm-quantization-techniques/>)

Every format below FP32 is doing the same thing, i.e., trading numeric detail for memory.

The visual below explains 8 such LLM precision formats:

![](https://substackcdn.com/image/fetch/$s_!rEf9!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fdaeb6e53-c360-40f6-9cb3-5b338f7a4538_1988x1975.png)   
---  
  
Before we dive into them, some background:

A floating-point number splits its bits three ways.

One sign bit, then exponent bits that decide how large or small a value can get, then mantissa bits that decide how finely values can be told apart inside that range.

![](https://substackcdn.com/image/fetch/$s_!M3xm!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F82edbd28-b067-46f7-83a2-23c4f1ae33cb_1200x896.jpeg)   
---  
  
  * Cutting exponent bits causes overflow, where large values saturate, and training blows up.
  * Cutting mantissa bits causes rounding error, where nearby values collapse into the same number and the error accumulates.

Different formats focus on different sides.

**1) FP32 has 8 exponent bits and 23 mantissa bits, reaching about 3.4e38.**

![](https://substackcdn.com/image/fetch/$s_!iGNN!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fdc52fa81-3dff-4284-b3a1-b13417d431a5_1376x526.jpeg)   
---  
  
Four bytes per parameter is expensive, but optimizer states and master weights still use FP32 even in low-precision training runs, because the gradient updates are small enough that FP16 storage might round them away entirely.

**2) TF32 is 19 bits, made of FP32’s 8 exponent bits and FP16’s 10 mantissa bits.**

![](https://substackcdn.com/image/fetch/$s_!MYjq!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fdbc44dc3-7c07-4333-ae24-87c19f482f04_1376x686.jpeg)   
---  
  
It only exists inside the tensor core, so weights are loaded and stored as FP32, and memory usage does not drop at all.

PyTorch enables it on Ampere and later without any code change, and this small change results in roughly 3x faster matmuls in exchange for 13 fewer mantissa bits during the multiplication process.

**3) BF16 keeps FP32’s 8 exponent bits and cuts the mantissa to 7.**

![](https://substackcdn.com/image/fetch/$s_!GldY!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe178da4f-eca6-4740-811e-10d6e208275b_1376x607.jpeg)   
---  
  
An identical range means casting down from FP32 only rounds and never overflows, which is why it has become the pre-training default.

**4) FP16 splits the same 16 bits the other way, 5 exponent bits and 10 mantissa bits.**

![](https://substackcdn.com/image/fetch/$s_!ZjSV!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb4741ec8-e0a5-45ef-bd41-97be8a63c496_1376x611.jpeg)   
---  
  
It resolves values eight times more finely than BF16 but is limited to just 65504, so gradients above that become infinity, and training needs loss scaling to survive.

It is also the only 16-bit option on V100 and T4 class hardware, which predate BF16.

_An RL fine-tuning paper from late 2025 found BF16’s rounding error accumulates across autoregressive sampling until the training and inference engines assign different probabilities to the same tokens, and that moving the whole pipeline to FP16 removed the divergence._

**5) FP8 has two layouts:**

![](https://substackcdn.com/image/fetch/$s_!q0y8!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc7cfe03a-6a96-40ed-8032-ce8bd598e4c2_1376x703.jpeg)   
---  
  
  * E4M3 reaches 448 and is ideal for weights and activations
  * E5M2 reaches 57344 and is ideal for gradients, which span more orders of magnitude.

Throughput-wise, this is about 2x faster BF16, but since the range is narrow, scaling factors per tensor or per block are no longer optional.

**6) INT8 has no floating point.**

![](https://substackcdn.com/image/fetch/$s_!Ghsi!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5d145767-08f0-4316-bad8-5d8d8477aa5f_1376x768.jpeg)   
---  
  
Weights map onto 256 evenly spaced integer levels between a calibrated minimum and maximum, which puts a 7B model in about 7GB with under 1% quality loss on many models.

Yes, even spacing is indeed a weakness, since a few outlier activations stretch the range and waste levels on values almost nothing uses.

![](https://substackcdn.com/image/fetch/$s_!taT9!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fcbf7e1c4-8f78-4860-bb5c-06e312076af7_1376x528.jpeg)   
---  
  
**7) INT4 gives each weight 16 possible values:**

![](https://substackcdn.com/image/fetch/$s_!wAhc!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5f5c2004-a671-4267-9180-84c94a4430e6_1376x633.webp)   
---  
  
To compare, INT8 can take 256 values, so the gaps between allowed values are sixteen times wider, and every weight moves further when it snaps to the nearest one.

Rounding to the nearest value keeps that individual move as small as possible. But a layer multiplies thousands of weights against the input and adds the results, so the error that shows up in the output is the sum of thousands of these moves.

Rounding cannot see that sum. It treats every weight as equally important, when in practice, only some of them meaningfully change the output.

GPTQ works around this by quantizing a block one weight at a time and adjusting the weights not yet done to cancel the error already made.

![](https://substackcdn.com/image/fetch/$s_!C6Uk!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0241eca1-c5fc-4c1d-b390-719689ab7b4d_1338x214.png)   
---  
  
AWQ finds the channels carrying the most signal and scales them up before quantizing, spending more of the 16 values where it counts.

![](https://substackcdn.com/image/fetch/$s_!j2nS!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Faced23a2-78bc-42fa-b130-e4240528bb32_1338x214.png)   
---  
  
Both need calibration data, a few hundred real inputs, since that is the only way to tell which weights matter.

**8) NF4 also uses 16 levels but spaces them unevenly, with bin edges placed along a normal distribution because pretrained weights sit close to a zero-centered Gaussian.**

![](https://substackcdn.com/image/fetch/$s_!X5uQ!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F47e75904-01a9-4941-aa94-7cf41883c749_1376x548.jpeg)   
---  
  
It exists for QLoRA, where the base model stays frozen in 4 bits, and [**LoRA**](<https://www.dailydoseofds.com/implementing-lora-from-scratch-for-fine-tuning-llms/>) adapters train in BF16 on top, which puts 65B fine-tuning on one 48GB GPU at 16-bit task quality.

The weights get dequantized back to BF16 for the actual matmul, so it saves memory without adding speed.

As a result, quality degrades far less on larger models, so a 70B at 4-bit generally beats a 13B at 16-bit for the same memory.

And the sharp drop is between 3-bit and 4-bit, not between 4-bit and 8-bit, which is why 4-bit ended up as the default everywhere from Ollama to vLLM.

To dive deeper, we have already written a full [**deep dive on Quantization**](<https://www.dailydoseofds.com/quantization-optimize-ml-models-to-run-them-on-tiny-hardware/>), specifically, which covers several of these methods with their simplified mathematics.

![](https://substackcdn.com/image/fetch/$s_!fatV!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F9c860c15-3e43-4403-9344-dccf0b0e3988_1004x442.png)   
---  
  
[**Learn how Quantization optimizes LLMs to run them on tiny hardware →**](<https://www.dailydoseofds.com/quantization-optimize-ml-models-to-run-them-on-tiny-hardware/>)
