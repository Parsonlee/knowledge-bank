# 4 strategies for multi-GPU training

- **原邮件主题**: Component-level Evals for LLM apps
- **发送人**: Daily Dose of DS <avi@dailydoseofds.com>
- **日期**: Mon, 30 Jun 2025 20:04:18 +0000
- **ID**: 197c270c599ab371

---

## [**4 strategies for multi-GPU training**](<https://www.dailydoseofds.com/a-beginner-friendly-guide-to-multi-gpu-model-training/>)

By default, deep learning models only utilize a single GPU for training, even if multiple GPUs are available.

An ideal way to train models is to distribute the training workload across multiple GPUs.

The graphic below depicts four common strategies for multi-GPU training:

![](https://substackcdn.com/image/fetch/$s_!quT_!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa02acc26-b1bf-48df-93e4-672d790a77ff_1022x1138.gif)   
---  
  
We covered multi-GPU training in detail with implementation here: [**A Beginner-friendly Guide to Multi-GPU Model Training**](<https://www.dailydoseofds.com/a-beginner-friendly-guide-to-multi-gpu-model-training/>).

Let’s discuss these four strategies below:

# **#1) Model parallelism**

![](https://substackcdn.com/image/fetch/$s_!n0_R!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4dce0267-f065-41d0-8d61-2ef1bf297cf9_1554x274.gif)   
---  
  
  * Different parts (or layers) of the model are placed on different GPUs.
  * Useful for huge models that do not fit on a single GPU.
  * However, model parallelism also introduces severe bottlenecks as it requires data flow between GPUs when activations from one GPU are transferred to another GPU.

# **#2) Tensor parallelism**

![](https://substackcdn.com/image/fetch/$s_!mcn3!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F437225d5-c382-4f8e-9ea3-88bb9b0e78b5_1554x274.gif)   
---  
  
  * Distributes and processes individual tensor operations across multiple devices or processors.
  * It is based on the idea that a large tensor operation, such as matrix multiplication, can be divided into smaller tensor operations, and each smaller operation can be executed on a separate device or processor.

![](https://substackcdn.com/image/fetch/$s_!SmeN!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fcfdae765-ee44-49e5-a16b-ff8df6cb4e51_2884x1139.png)   
---  
  
  * Such parallelization strategies are inherently built into standard implementations of PyTorch and other deep learning frameworks, but they become much more pronounced in a distributed setting.

# **#3) Data parallelism**

![](https://substackcdn.com/image/fetch/$s_!rn8q!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc9119718-64d0-4bbf-af57-fc44a22757fb_1550x524.gif)   
---  
  
  * Replicate the model across all GPUs.
  * Divide the available data into smaller batches, and each batch is processed by a separate GPU.
  * The updates (or gradients) from each GPU are then aggregated and used to update the model parameters on every GPU.

# **#4) Pipeline parallelism**

![](https://substackcdn.com/image/fetch/$s_!EGqs!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc1a8d3db-8e56-4990-8871-9e125fcee3e9_944x348.gif)   
---  
  
  * This is often considered a combination of data parallelism and model parallelism.
  * So the issue with standard model parallelism is that 1st GPU remains idle when data is being propagated through layers available in 2nd GPU:

![](https://substackcdn.com/image/fetch/$s_!n0_R!,w_1456,c_limit,f_auto,q_auto:good,fl_lossy/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4dce0267-f065-41d0-8d61-2ef1bf297cf9_1554x274.gif)   
---  
  
  * Pipeline parallelism addresses this by loading the next micro-batch of data once the 1st GPU has finished the computations on the 1st micro-batch and transferred activations to layers available in the 2nd GPU. The process looks like this:
    * 1st micro-batch passes through the layers on 1st GPU.
    * 2nd GPU receives activations on 1st micro-batch from 1st GPU.
    * While the 2nd GPU passes the data through the layers, another micro-batch is loaded on the 1st GPU.
    * And the process continues.
  * GPU utilization drastically improves this way. This is evident from the animation below where multi-GPUs are being utilized at the same timestamp (look at t=1, t=2, t=5, and t=6):

![](https://substackcdn.com/image/fetch/$s_!EGqs!,w_1456,c_limit,f_auto,q_auto:good,fl_lossy/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc1a8d3db-8e56-4990-8871-9e125fcee3e9_944x348.gif)   
---  
  
* * *

Those were four common strategies for multi-GPU training.

To get into more details about multi-GPU training and implementation, read this article: [**A Beginner-friendly Guide to Multi-GPU Model Training**](<https://www.dailydoseofds.com/a-beginner-friendly-guide-to-multi-gpu-model-training/>).

Also, we covered [](<https://www.dailydoseofds.com/15-ways-to-optimize-neural-network-training-with-implementation/>)[**15 ways to optimize neural network training here (with implementation) →**](<https://www.dailydoseofds.com/15-ways-to-optimize-neural-network-training-with-implementation/>)
