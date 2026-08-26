---
title: 4 LLM text generation strategies
source_key: dailydoseofds
email_subject: Rethinking KV Caching For Production Inference
email_sender: Daily Dose of DS <avi@dailydoseofds.com>
email_date: Tue, 07 Jul 2026 16:52:26 +0000
email_id: 19f3d7ecdb9a83ee
article_id: 19f3d7ecdb9a83ee:1
published: '2026-07-07'
tags:
- LLM/arch
- LLM/inference
- DeepLearning
---

# 4 LLM text generation strategies

- **原邮件主题**: Rethinking KV Caching For Production Inference
- **发送人**: Daily Dose of DS <avi@dailydoseofds.com>
- **日期**: Tue, 07 Jul 2026 16:52:26 +0000
- **ID**: 19f3d7ecdb9a83ee

---

## **4 LLM text generation strategies**

Every time you prompt an LLM, it doesn’t “know” the whole sentence in advance. Instead, it predicts the next token step by step.

But here’s the catch: predicting probabilities is not enough. We still need a strategy to pick which token to use at each step.

And different strategies lead to very different styles of output.

Here are the 4 most common strategies for text generation:

![](https://substackcdn.com/image/fetch/$s_!I8rU!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F92fa50e4-d4cd-4b35-b371-647cd97303f0_1790x1396.png)   
---  
  
#### Approach 1: Greedy strategy

The naive approach greedily chooses the word with the highest probability from the probability vector, and autoregresses. This is often not ideal since it leads to repetitive sentences.

#### Approach 2: Multinomial sampling strategy

Instead of always picking the top token, we can sample from the probability distribution available in the probability vector.

![](https://substackcdn.com/image/fetch/$s_!DsVw!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ffd4fa2d4-6175-4d98-8fd3-034efec31de4_1456x582.png)   
---  
  
The temperature parameter controls the randomness in the generation ([**covered in detail here**](<https://fff97757.click.kit-mail3.com/4zuwmw6lz0hehp4vkn4txh690orn2h5h6ng99/kkhmh6hn0w6dgmslh7/aHR0cHM6Ly93d3cuZGFpbHlkb3Nlb2Zkcy5jb20vcC93aGF0LWlzLXRlbXBlcmF0dXJlLWluLWxsbXMv>)).

#### Approach 3: Beam search

Both approach 1 and approach 2 have a problem. They only focus on the most immediate token to be generated. Ideally, we care about maximizing the probability of the whole sequence, not just the next token.

![](https://substackcdn.com/image/fetch/$s_!1RH5!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc506c53e-e6d7-4195-9a8c-3cf376742642_1860x270.png)   
---  
  
  * To maximize this product, you’d need to know future conditionals (what comes after each candidate).
  * But when decoding, we only know probabilities for the next step, not the downstream continuation.

Beam search tries to approximate the true global maximization:

![](https://substackcdn.com/image/fetch/$s_!eA68!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F52fe0893-0918-4d23-8554-223f301e03ca_2942x577.png)   
---  
  
  * At each step, it expands the top k partial sequences (the beam).
  * Some beams may have started with less probable tokens initially, but lead to much higher-probability completions.
  * By keeping alternatives alive, beam search explores more of the probability tree.

This is widely used in tasks like machine translation, where correctness matters more than creativity.

#### Approach 4: Contrastive search

![](https://substackcdn.com/image/fetch/$s_!GMd9!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F513e95ba-7ab6-4c06-ad8c-c63537e0917e_2942x585.png)   
---  
  
This is a newer method that balances fluency with diversity.

Essentially, it penalizes repetitive continuations by checking how similar a candidate token is to what’s already been generated to have more diversity in the output.

  * At each step, the model considers candidate tokens.
  * Applies a penalty if the token is too similar to what’s already been generated.
  * Selects the token that balances probability and diversity.

This way, it also prevents “stuck in a loop” problems while keeping coherence high.

It’s especially effective for longer generations like stories, where repetition can easily creep in.

👉 Over to you: Which decoding strategy have you found most effective in your projects?
