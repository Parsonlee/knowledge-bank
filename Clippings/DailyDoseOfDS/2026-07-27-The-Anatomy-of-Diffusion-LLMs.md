title: "Diffusion LLM（扩散语言模型）结构与原理剖析" date: 2026-07-27 author: "Avi Chawla & Akshay Pachaar" source: "https://mail.google.com/mail/u/0/#inbox/19fa5754b2a0ee28" type: clipping
Diffusion LLM（扩散语言模型）结构与原理剖析
目前所有的生产级大语言模型（GPT-4、Claude、Gemini、LLaMA 等）都采用自回归（Autoregressive）方式逐字生成文本：从左到右，一次生成一个 Token。


这种方式的痛点在于受限于内存带宽（Memory-bandwidth bound）：每生成一个 Token，都需要将全部模型权重从 GPU 显存载入计算，而 GPU 本身擅长的是高算力密度的并行计算。
扩散语言模型的全新路径
Diffusion LLM（扩散 LLM）采取了截然不同的解法：


* 从一个完全被 Mask（掩码）遮盖的序列开始；
* 在每一步使用双向 Self-Attention 迭代地并行解掩码（Unmask）；
* 将推理计算从内存带宽限制转变为算力限制（Compute-bound），完美契合现代 GPU 的硬件优势。
技术关键进展
1. Block Diffusion (BD3-LM)：在 LM1B 上与自回归模型的 Perplexity 差距缩小至 0.5 点以内。
2. LLaDA (8B)：在 MMLU 上赶平 LLaMA 3，在 TruthfulQA 和 HumanEval 上实现超越。
3. Dream 7B：已实现通过 SGLang 在生产环境中进行 Serving 推送。


随着模型规模放大，从 Forward Masking 过程到 ELBO 目标函数，再到 Block 级别的 KV Cache 优化，理解 Diffusion LLM 的底层数学原理与工程实现正变得越来越重要。