# The anatomy of diffusion LLMs

- **原邮件主题**: Graph Engineering Clearly Explained
- **发送人**: Daily Dose of DS <avi@dailydoseofds.com>
- **日期**: Mon, 27 Jul 2026 21:22:34 +0000
- **ID**: 19fa5754b2a0ee28

---

## [**The anatomy of diffusion LLMs**](<https://fff97757.click.kit-mail3.com/27uprpxd03foh8m2lvrf3hgrqednzbghgmk33/reh8hohmg5r5q8f2h6/aHR0cHM6Ly93d3cuZGFpbHlkb3Nlb2Zkcy5jb20vZGlmZnVzaW9uLW1vZGVscy1wYXJ0LTEv>)  
  
We recently published a deep dive that covers one of the most important architectural shifts happening in language modeling right now: diffusion LLMs.

[**Read the full Part 1 deep dive here →**](<https://fff97757.click.kit-mail3.com/27uprpxd03foh8m2lvrf3hgrqednzbghgmk33/reh8hohmg5r5q8f2h6/aHR0cHM6Ly93d3cuZGFpbHlkb3Nlb2Zkcy5jb20vZGlmZnVzaW9uLW1vZGVscy1wYXJ0LTEv>)

[**Read the full Part 2 deep dive here →**](<https://fff97757.click.kit-mail3.com/27uprpxd03foh8m2lvrf3hgrqednzbghgmk33/08hwh9h23757d0blh5/aHR0cHM6Ly93d3cuZGFpbHlkb3Nlb2Zkcy5jb20vZGlmZnVzaW9uLW1vZGVscy1wYXJ0LTI=>)

![](https://substackcdn.com/image/fetch/$s_!g9CL!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F09768bd8-8e5e-43da-802b-85ebdef29965_1257x633.png)   
---  
  
It builds a complete understanding from first principles:

  * how autoregressive generation is structurally memory-bandwidth bound)
  * why Gaussian noise can’t work on discrete tokens
  * how masked diffusion solves this with an ELBO-derived training objective
  * the math behind the forward and reverse processes
  * unmasking strategies
  * block diffusion for KV cache compatibility
  * a detailed engineering comparison between the two paradigms.
  * the training techniques that scaled dLLMs from 8B to 100B parameters (including converting pre-trained autoregressive models like LLaMA into diffusion models via attention mask annealing)
  * the inference acceleration stack (block-wise KV caching with Fast-dLLM, confidence-aware parallel decoding, token editing with LLaDA 2.1),
  * production serving with SGLang
  * hands-on code for running Dream 7B and serving LLaDA 2.0, 
  * and a decision framework for when dLLMs actually make sense over autoregressive models.

[**Read the full Part 1 deep dive here →**](<https://fff97757.click.kit-mail3.com/27uprpxd03foh8m2lvrf3hgrqednzbghgmk33/reh8hohmg5r5q8f2h6/aHR0cHM6Ly93d3cuZGFpbHlkb3Nlb2Zkcy5jb20vZGlmZnVzaW9uLW1vZGVscy1wYXJ0LTEv>)

[**Read the full Part 2 deep dive here →**](<https://fff97757.click.kit-mail3.com/27uprpxd03foh8m2lvrf3hgrqednzbghgmk33/08hwh9h23757d0blh5/aHR0cHM6Ly93d3cuZGFpbHlkb3Nlb2Zkcy5jb20vZGlmZnVzaW9uLW1vZGVscy1wYXJ0LTI=>)

* * *

# **Why care?**

Every production LLM today, GPT-4, Claude, Gemini, LLaMA, generates text the same way: one token at a time, left to right.

![](https://substackcdn.com/image/fetch/$s_!OWAB!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff9afd2f9-892b-4640-8a57-4da5d4ca6bcd_807x400.png)   
---  
  
Each token requires loading the full model weights through GPU memory, performing a tiny computation, and then loading all the weights again for the next token. On an A100, this means roughly 1 FLOP per byte of data moved, while the GPU is designed for 100+ FLOPs per byte.

![](https://substackcdn.com/image/fetch/$s_!2Lbi!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3585f1a2-20c1-4b93-b76f-860e253af000_1069x427.png)   
---  
  
[**Diffusion LLMs**](<https://fff97757.click.kit-mail3.com/27uprpxd03foh8m2lvrf3hgrqednzbghgmk33/reh8hohmg5r5q8f2h6/aHR0cHM6Ly93d3cuZGFpbHlkb3Nlb2Zkcy5jb20vZGlmZnVzaW9uLW1vZGVscy1wYXJ0LTEv>) take a completely different approach. They start with a fully masked sequence and iteratively unmask all tokens in parallel, using bidirectional attention at every step. This shifts inference from memory-bandwidth bound to compute-bound, which is exactly where modern GPUs are efficient.

The results are catching up fast. Block diffusion (BD3-LM) is within 0.5 perplexity points of autoregressive on LM1B. LLaDA at 8B parameters matches LLaMA 3 on MMLU and exceeds it on TruthfulQA and HumanEval. And models like Dream 7B are already being served in production with SGLang.

Understanding how it works at a mathematical level, from the forward masking process to the ELBO objective to block-level KV caching, is going to be increasingly valuable as these models scale.

[**You can read Part 1 here →**](<https://fff97757.click.kit-mail3.com/27uprpxd03foh8m2lvrf3hgrqednzbghgmk33/reh8hohmg5r5q8f2h6/aHR0cHM6Ly93d3cuZGFpbHlkb3Nlb2Zkcy5jb20vZGlmZnVzaW9uLW1vZGVscy1wYXJ0LTEv>)

[**You can read Part 2 here →**](<https://fff97757.click.kit-mail3.com/27uprpxd03foh8m2lvrf3hgrqednzbghgmk33/08hwh9h23757d0blh5/aHR0cHM6Ly93d3cuZGFpbHlkb3Nlb2Zkcy5jb20vZGlmZnVzaW9uLW1vZGVscy1wYXJ0LTI=>)

👉 Over to you: Do you think the future of LLM generation is pure diffusion, pure autoregressive, or some hybrid of the two?
