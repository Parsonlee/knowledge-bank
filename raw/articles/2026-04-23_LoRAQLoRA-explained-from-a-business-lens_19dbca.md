# LoRA/QLoRA explained from a business lens

- **原邮件主题**: Top AI Labs Share an Agent Memory Trick Most Miss
- **发送人**: Daily Dose of DS <avi@dailydoseofds.com>
- **日期**: Thu, 23 Apr 2026 23:20:49 +0000
- **ID**: 19dbca56ab454b95

---

## [**LoRA/QLoRA explained from a business lens**](<https://fff97757.click.kit-mail3.com/38u030zrokckh2geol4urh4m798r9i7h64xll/kkhmh6hnvldgngul/aHR0cHM6Ly93d3cuZGFpbHlkb3Nlb2Zkcy5jb20vaW1wbGVtZW50aW5nLWxvcmEtZnJvbS1zY3JhdGNoLWZvci1maW5lLXR1bmluZy1sbG1zLw==>)

Consider the size difference between BERT-large and GPT-3:

![](https://embed.filekitcdn.com/e/k7YHPN24SoxyM8nGKZnDxa/cRYXi2HMRuFC547DMre8ec/email) GPT-4 (not shown here) is 10x bigger than GPT-3.  
---  
  
We have fine-tuned BERT-large several times on a single GPU using traditional fine-tuning:

![](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F9764beac-a786-4305-9a47-ec050b0ebef6_1060x308.gif)   
---  
  
But this is impossible with GPT-3, which has 175B parameters. That's 350GB of memory just to store model weights under float16 precision.

This means that if OpenAI used traditional fine-tuning within its fine-tuning API, it would have to maintain one model copy per user:

  * If 10 users fine-tuned GPT-3 → they need **3500 GB** to store model weights.
  * If 1000 users fine-tuned GPT-3 → they need **350k GB** to store model weights.
  * If 100k users fine-tuned GPT-3 → they need **35 million** GB to store model weights.

![](https://embed.filekitcdn.com/e/k7YHPN24SoxyM8nGKZnDxa/5EZ6B115sYJBfg4VCeYcWu/email)   
---  
  
And the problems don't end there:

  * OpenAI bills solely based on usage. What if someone fine-tunes the model for fun or learning purposes but never uses it?
  * Since a request can come anytime, should they always keep the fine-tuned model loaded in memory? Wouldn't that waste resources since several models may never be used?

[**LoRA**](<https://fff97757.click.kit-mail3.com/38u030zrokckh2geol4urh4m798r9i7h64xll/kkhmh6hnvldgngul/aHR0cHM6Ly93d3cuZGFpbHlkb3Nlb2Zkcy5jb20vaW1wbGVtZW50aW5nLWxvcmEtZnJvbS1zY3JhdGNoLWZvci1maW5lLXR1bmluZy1sbG1zLw==>)**(+**[**QLoRA and other variants**](<https://fff97757.click.kit-mail3.com/38u030zrokckh2geol4urh4m798r9i7h64xll/58hvh7hg2mvpgvc6/aHR0cHM6Ly93d3cuZGFpbHlkb3Nlb2Zkcy5jb20vdW5kZXJzdGFuZGluZy1sb3JhLWRlcml2ZWQtdGVjaG5pcXVlcy1mb3Itb3B0aW1hbC1sbG0tZmluZS10dW5pbmcv>)**) neatly solved this critical business problem.**

The core idea revolves around training a few parameters compared to the base model.

![](https://embed.filekitcdn.com/e/k7YHPN24SoxyM8nGKZnDxa/fN4DhcCeqnD8d79bW2NcHp/email)   
---  
  
For instance, if the original model has a weight matrix `W` (shape `d*d`), one can define the corresponding LoRA matrices `A` (`d*r`) and `B` (`r*d`).

↳ where `r<<<<d` (typically, `r` is a single-digit number).

During fine-tuning, freeze the weight matrix `W` and update the weights of the LoRA matrices.

During inference, the product of the LoRA matrices results in a matrix of the same shape as `W`. So one can obtain the output as follows:

![](https://embed.filekitcdn.com/e/k7YHPN24SoxyM8nGKZnDxa/nYkD1sojMLv4b4CoE18mLH/email)   
---  
  
This way, every user gets their LoRA matrices, and OpenAI can maintain just one global/common model.

![](https://embed.filekitcdn.com/e/k7YHPN24SoxyM8nGKZnDxa/2HtzbT1knmGEDhWA1eLrXd/email)   
---  
  
Another good thing is that LoRA matrices usually do not require more than 20-25 MB of memory per user. This is immensely smaller than what we get from traditional fine-tuning.

Lastly, this also solves the other two problems we mentioned earlier:

  * If someone fine-tunes the model just for fun or learning purposes but never uses it, it's okay; LoRA matrices are still manageable.
  * Loading small LoRA matrices from disk isn't tedious either. These small matrices can be offloaded if not used for a while and reloaded when needed.

[**We implemented LoRA for fine-tuning LLMs from scratch here →**](<https://fff97757.click.kit-mail3.com/38u030zrokckh2geol4urh4m798r9i7h64xll/kkhmh6hnvldgngul/aHR0cHM6Ly93d3cuZGFpbHlkb3Nlb2Zkcy5jb20vaW1wbGVtZW50aW5nLWxvcmEtZnJvbS1zY3JhdGNoLWZvci1maW5lLXR1bmluZy1sbG1zLw==>)

[**LoRA has several efficient variants. We covered them here →**](<https://fff97757.click.kit-mail3.com/38u030zrokckh2geol4urh4m798r9i7h64xll/58hvh7hg2mvpgvc6/aHR0cHM6Ly93d3cuZGFpbHlkb3Nlb2Zkcy5jb20vdW5kZXJzdGFuZGluZy1sb3JhLWRlcml2ZWQtdGVjaG5pcXVlcy1mb3Itb3B0aW1hbC1sbG0tZmluZS10dW5pbmcv>)

![](https://embed.filekitcdn.com/e/k7YHPN24SoxyM8nGKZnDxa/8FLBc1XK7kojjCjq9HD8G3/email)   
---  
  
Moreover, if you want to develop expertise in “business ML,” we have discussed several other topics (with implementations) that align with it:

Here are some of them:

  * [**Quantization: Optimize ML Models to Run Them on Tiny Hardware**](<https://fff97757.click.kit-mail3.com/38u030zrokckh2geol4urh4m798r9i7h64xll/25h2hoh3w2vr38i3/aHR0cHM6Ly93d3cuZGFpbHlkb3Nlb2Zkcy5jb20vcXVhbnRpemF0aW9uLW9wdGltaXplLW1sLW1vZGVscy10by1ydW4tdGhlbS1vbi10aW55LWhhcmR3YXJlLw==>).
  * [**Conformal Predictions: Build Confidence in Your Model's Predictions**](<https://fff97757.click.kit-mail3.com/38u030zrokckh2geol4urh4m798r9i7h64xll/qvh8h7hdpr7gdvil/aHR0cHM6Ly93d3cuZGFpbHlkb3Nlb2Zkcy5jb20vY29uZm9ybWFsLXByZWRpY3Rpb25zLWJ1aWxkLWNvbmZpZGVuY2UtaW4teW91ci1tbC1tb2RlbHMtcHJlZGljdGlvbnMv>).
  * [**A Practical Guide to Scaling ML Model Training**](<https://fff97757.click.kit-mail3.com/38u030zrokckh2geol4urh4m798r9i7h64xll/g3hnh5hmw3d7mosr/aHR0cHM6Ly93d3cuZGFpbHlkb3Nlb2Zkcy5jb20vaG93LXRvLXNjYWxlLW1vZGVsLXRyYWluaW5nLw==>).
  * [**5 Ways to Test ML Models in Production (Implementation Included)**](<https://fff97757.click.kit-mail3.com/38u030zrokckh2geol4urh4m798r9i7h64xll/9qhzhnhdrpqkdlt9/aHR0cHM6Ly93d3cuZGFpbHlkb3Nlb2Zkcy5jb20vNS1tdXN0LWtub3ctd2F5cy10by10ZXN0LW1sLW1vZGVscy1pbi1wcm9kdWN0aW9uLWltcGxlbWVudGF0aW9uLWluY2x1ZGVkLw==>).
  * [**Federated Learning: Build Privacy-Preserving ML Models**](<https://fff97757.click.kit-mail3.com/38u030zrokckh2geol4urh4m798r9i7h64xll/3ohphkh3g7o63dsr/aHR0cHM6Ly93d3cuZGFpbHlkb3Nlb2Zkcy5jb20vZmVkZXJhdGVkLWxlYXJuaW5nLWEtY3JpdGljYWwtc3RlcC10b3dhcmRzLXByaXZhY3ktcHJlc2VydmluZy1tYWNoaW5lLWxlYXJuaW5nLw==>).
  * [**Model Compression: A Step Towards Efficient Machine Learning**](<https://fff97757.click.kit-mail3.com/38u030zrokckh2geol4urh4m798r9i7h64xll/n2hohvhv038wvnh6/aHR0cHM6Ly93d3cuZGFpbHlkb3Nlb2Zkcy5jb20vbW9kZWwtY29tcHJlc3Npb24tYS1jcml0aWNhbC1zdGVwLXRvd2FyZHMtZWZmaWNpZW50LW1hY2hpbmUtbGVhcm5pbmcv>).

