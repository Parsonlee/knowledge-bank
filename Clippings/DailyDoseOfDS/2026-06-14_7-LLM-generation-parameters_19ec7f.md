# 7 LLM generation parameters

- **原邮件主题**: Deep dive on proximal policy optimization (PPO) in RL
- **发送人**: Daily Dose of DS <avi@dailydoseofds.com>
- **日期**: Sun, 14 Jun 2026 21:01:42 +0000
- **ID**: 19ec7f0bdd27389b

---

## [**7 LLM generation parameters**](<https://fff97757.click.kit-mail3.com/e5unmnq5evf7hl3gdznf8h85kn4x6slhvzgnn/x0hph6he6mwkqkt5hl/aHR0cHM6Ly93d3cuZGFpbHlkb3Nlb2Zkcy5jb20vbGxtb3BzLWNyYXNoLWNvdXJzZS1wYXJ0LTEv>)

Every generation from an LLM is shaped by parameters under the hood.

Knowing how to tune is important so that you can produce sharp and more controlled outputs.

Here are the 7 levers that matter most:

![](https://embed.filekitcdn.com/e/k7YHPN24SoxyM8nGKZnDxa/fKGxvZdMD4UmMaHrKMUfzb/email)   
---  
  
**1) Max tokens**

![](https://substackcdn.com/image/fetch/$s_!ZtYY!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff1b0886c-470c-4009-958e-be3856f63c9d_890x156.gif)   
---  
  
  * This is a hard cap on how many tokens the model can generate in one response.
  * Too low → truncated outputs; too high → could lead to wasted compute.

**2) Temperature (**[**covered in detail here**](<https://fff97757.click.kit-mail3.com/e5unmnq5evf7hl3gdznf8h85kn4x6slhvzgnn/6qheh8hlg47x9ziohk/aHR0cHM6Ly93d3cuZGFpbHlkb3Nlb2Zkcy5jb20vcC93aGF0LWlzLXRlbXBlcmF0dXJlLWluLWxsbXMv>)**):**

![](https://substackcdn.com/image/fetch/$s_!4hF3!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff8c6e298-d4c5-4a39-b844-45d14ef7e13c_890x172.gif)   
---  
  
  * Governs randomness. Low temperature (~0) makes the model deterministic.
  * Higher temperature (0.7–1.0) boosts creativity, diversity, but also noise.
  * Use case: lower for QA/chatbots, higher for brainstorming/creative tasks.

**3) Top-k:**

![](https://substackcdn.com/image/fetch/$s_!MDQM!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F2de42ee9-8f69-4efa-a4f8-78f5c507326c_890x172.gif)   
---  
  
  * The default way to generate the next token is to sample from all tokens, proportional to their probability.
  * This parameter restricts sampling to the top _k_ most probable tokens.
  * Example: k=5 → model only considers 5 most likely next tokens during sampling.
  * Helps enforce focus, but overly small `k` may give repetitive outputs.

**4) Top-p (nucleus sampling):**

![](https://substackcdn.com/image/fetch/$s_!cFFQ!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe8daaad1-f582-4a86-ba4e-ab91f6ae8773_890x172.gif)   
---  
  
  * Instead of picking from all tokens or top `k` tokens, model samples from a probability mass up to _p_.
  * Example: top_p=0.9 → only the smallest set of tokens covering 90% probability are considered.
  * More adaptive than `top_k`, useful when balancing coherence with diversity.

**5) Frequency penalty:**

![](https://substackcdn.com/image/fetch/$s_!HJaK!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7a903393-cb94-47a8-a604-d6f79a64341f_890x152.gif)   
---  
  
  * Reduces likelihood of reusing tokens that have already appeared frequently.
  * Positive values discourage repetition, negative values exaggerate it.
  * Useful for summarization (avoid redundancy) or poetry (intentional repetition).

**6) Presence penalty**

![](https://substackcdn.com/image/fetch/$s_!7qFI!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F758936be-8183-4598-aed3-ad5195450310_890x152.gif)   
---  
  
  * Encourages the model to bring in new tokens not yet seen in the text.
  * Higher values push for novelty, lower values make the model stick to known patterns.
  * Handy for exploratory generation where diversity of ideas is valued.

**7) Stop sequences**

![](https://substackcdn.com/image/fetch/$s_!k2aP!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F85ba8849-3eda-4328-aee4-52bf1dc73509_890x152.gif)   
---  
  
  * Custom list of tokens that immediately halt generation.
  * Critical in structured outputs (e.g., JSON), preventing spillover text.
  * Let's you enforce strict response boundaries without heavy prompt engineering.

👉 Over to you: What other LLM generation params have we missed?
