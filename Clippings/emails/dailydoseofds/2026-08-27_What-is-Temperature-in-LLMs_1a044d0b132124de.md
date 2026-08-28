---
title: " What is Temperature in LLMs? "
source_key: "dailydoseofds"
email_subject: "KV vs Prefix vs Prompt vs Semantic Caching"
email_sender: "Daily Dose of DS <avi@dailydoseofds.com>"
email_date: "Thu, 27 Aug 2026 20:02:01 +0000"
email_id: "1a044d0b132124de"
article_id: "1a044d0b132124de:3"
published: "2026-08-27"
tags: []
---

#  What is Temperature in LLMs? 

- **邮件来源**: dailydoseofds
- **原邮件主题**: KV vs Prefix vs Prompt vs Semantic Caching
- **发送人**: Daily Dose of DS <avi@dailydoseofds.com>
- **日期**: Thu, 27 Aug 2026 20:02:01 +0000
- **邮件 ID**: 1a044d0b132124de
- **文章 ID**: 1a044d0b132124de:3

---

## [**What is Temperature in LLMs?**](<https://www.dailydoseofds.com/ai-agents-crash-course-part-1-with-implementation/>)

A low temperature value produces identical responses from the LLM (shown below):

![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4bda7594-c672-4066-81ec-e90a90c1cc97_1888x1156.png)   
---  
  
But a high temperate value produces gibberish.

![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F9587829f-23b1-42aa-ba01-4f3e8cd514e2_1888x1156.png)   
---  
  
What exactly is `temperature` in LLMs?

Let’s understand this today!

* * *

Traditional classification models use softmax to generate the final prediction from logits over all classes. In LLMs, the output layer spans the entire vocabulary.

![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe66aabe8-e450-46fe-be20-03d0f70b76a2_3060x1272.png)   
---  
  
The difference is that a traditional classification model predicts the class with the highest softmax score, which makes it deterministic.

But LLMs **sample** the prediction from these softmax probabilities:

![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb8a85e64-921c-4861-9c76-037318f12839_3180x1272.png)   
---  
  
Thus, even though “`Token 1`” has the highest probability of being selected (`0.86`), it may not be chosen as the next token since we are sampling.

Temperature introduces the following tweak in the softmax function, which, in turn, influences the sampling process:

![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe97a4d18-56ea-430e-a2a4-a584ab7d7900_2640x619.png)   
---  
  
1) If the temperature is low, the probabilities look more like a max value instead of a “soft-max” value.

![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F54e30662-3e50-43ef-8197-09cadbd29ee3_2036x1072.png)   
---  
  
  * This means the sampling process will almost certainly choose the token with the highest probability.
  * This makes the generation process look greedy and (almost) deterministic.

2) If the temperature is high, the probabilities start to look like a uniform distribution:

![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F175ce847-c7f0-4fdb-baf7-560894b5bd49_2036x1072.png)   
---  
  
  * This means the sampling process may select any token.
  * This makes the generation process random and heavily stochastic.

A quick note: In practice, the model can generate different outputs even if `temperature=0`. This is because there are still several other sources of randomness, such as race conditions in multithreaded code.

Here are some best practices for using temperature:

  * Set a low temperature value to generate predictable responses.
  * Set a high temperature value to generate more random and creative responses.
  * An extremely high temperature value rarely has any real utility, as we saw at the top.

And this explains the objective behind temperature in LLMs.

This visual explains 6 more LLM generation parameters with usage:

![](https://embed.filekitcdn.com/e/k7YHPN24SoxyM8nGKZnDxa/eB93eY66SjsgmADvtC6124/email)   
---  
  
👉 Over to you: How do you determine an ideal value of temperature?
