---
title: 15 techniques to optimize neural network training
source_key: dailydoseofds
email_subject: ​15 Techniques to Optimize Neural Network Training​
email_sender: Daily Dose of DS <avi@dailydoseofds.com>
email_date: Fri, 27 Jun 2025 20:16:02 +0000
email_id: 197b30868d3ba958
article_id: 197b30868d3ba958:1
published: '2025-06-27'
tags:
- DeepLearning
- Skill/data-analysis
- LLM/training
---

# 15 techniques to optimize neural network training

- **原邮件主题**: ​15 Techniques to Optimize Neural Network Training​
- **发送人**: Daily Dose of DS <avi@dailydoseofds.com>
- **日期**: Fri, 27 Jun 2025 20:16:02 +0000
- **ID**: 197b30868d3ba958

---

## [**15 techniques to optimize neural network training**](<https://www.dailydoseofds.com/15-ways-to-optimize-neural-network-training-with-implementation/>)

Here are 15 ways we could recall in 2 minutes to optimize neural network training:

![](https://substackcdn.com/image/fetch/$s_!9eAt!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F9e7c9435-9466-4216-b41e-82da94afedc5_952x1074.gif)   
---  
  
Some of them are pretty basic and obvious, like:

  * Use efficient optimizers: AdamW, Adam, etc.
  * Utilize hardware accelerators (GPUs/TPUs).
  * Max out the batch size.

Here are other methods with more context:

**On a side note,**[**we implemented all these techniques here →**](<https://www.dailydoseofds.com/15-ways-to-optimize-neural-network-training-with-implementation/>)

**#4) Use Bayesian Optimization if the hyperparameter search space is big:**

  * Take informed steps using the results of previous hyperparameter configs.
  * This lets it discard non-optimal configs, and the model converges faster.
  * As shown in the results below, Bayesian optimization (green bar) takes the least number of iterations, consumes the lowest time, and still finds the configuration with the best F1 score:

![](https://substackcdn.com/image/fetch/$s_!U1sv!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ffe4a1480-59ad-410e-8a2b-c23e3b807f65_1000x689.png)   
---  
  
**#5) Use mixed precision training:**

![](https://substackcdn.com/image/fetch/$s_!fREY!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7752bd3d-c43c-4e44-a461-cdeac12d4054_792x832.gif)   
---  
  
  * Use lower precision `float16` (wherever feasible, like in convolutions and matrix multiplications) along with `float32`.
  * List of some models trained using mixed precision (indicating popularity):

![](https://substackcdn.com/image/fetch/$s_!oVRJ!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7223e89a-d0ac-4199-bd44-59f226acdaa5_898x432.png)   
---  
  
#6) Use He or Xavier initialization for faster convergence (usually helps).

#7) Utilize multi-GPU training through Model/Data/Pipeline/Tensor parallelism.

#8) For large models, use techniques like DeepSpeed, FSDP, YaFSDP, etc.

#9) Always use `DistributedDataParallel`, not `DataParallel` in your data loaders, even if you are not using distributed training.

#10) Use activation checkpointing to optimize memory (run-time will go up).

![](https://substackcdn.com/image/fetch/$s_!A1rv!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F794aeb73-182b-425b-ac49-19df9b07d714_1200x1496.png)   
---  
  
  * We don’t need to store all the intermediate activations in memory. Instead, storing a few of them and recomputing the rest when needed can significantly reduce the memory requirement.
  * This can reduce memory usage by a factor of `sqrt(M)`, where `M` is the memory consumed without activation checkpointing.
  * But due to recomputations, it increases run-time.

#11) Normalize data after transferring to GPU (for integer data, like pixels):

![](https://substackcdn.com/image/fetch/$s_!cDwO!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4a57e18d-4760-4f7e-b94f-2cb92460c3cc_1456x727.png)   
---  
  
  * Consider image data, which has pixels (8-bit integer values).
  * Normalizing it before transferring to the GPU would mean we need to transfer 32-bit floats.
  * But normalizing after transfer means 8-bit integers are transferred, consuming less memory.

#12) Use gradient accumulation (may have marginal improvement at times).

![](https://substackcdn.com/image/fetch/$s_!vSoI!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F8216dfa4-6c42-4875-b56d-830b61cf5f88_2120x688.png)   
---  
  
  * Under memory constraints, it is always recommended to train the neural network with a small batch size.
  * Despite that, there’s a technique called **gradient accumulation** , which lets us (logically) increase batch size without explicitly increasing the batch size.

**#13)**`torch.rand(2, 2, device = ...)` creates a tensor directly on the `GPU`. But `torch.rand(2,2).cuda()` first creates on the CPU, then transfers to the GPU, which is slow. The speedup is evident from the image below:

![](https://substackcdn.com/image/fetch/$s_!Auf6!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0a9cfbab-b599-43a6-ab38-4c15450f4525_1456x690.png)   
---  
  
# 14-15) Set `max_workers` and `pin_memory` in DataLoader.

  * The typical neural network training procedure is as follows:

![](https://substackcdn.com/image/fetch/$s_!IkdX!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe437cb84-f778-46d5-a010-5e254cff7d5f_1740x676.png)   
---  
  
  * As shown above, when the GPU is working, the CPU is idle, and when the CPU is working, the GPU is idle.
  * But here’s what we can do to optimize this:

![](https://substackcdn.com/image/fetch/$s_!isJ5!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F00a246a7-bcd3-4fb6-91f2-8e0bf76e56f7_1916x676.png)   
---  
  
  * When the model is being trained on the 1st mini-batch, the CPU can transfer the 2nd mini-batch to the GPU.
  * This ensures that the GPU does not have to wait for the next mini-batch of data as soon as it completes processing an existing mini-batch.
  * While the CPU may remain idle, this process ensures that the GPU (which is the actual accelerator for our model training) always has data to work with.

Of course, the above is not an all-encompassing list.

👉 Over to you: Can you add more techniques?

****[**We implemented all these techniques here →**](<https://www.dailydoseofds.com/15-ways-to-optimize-neural-network-training-with-implementation/>)
