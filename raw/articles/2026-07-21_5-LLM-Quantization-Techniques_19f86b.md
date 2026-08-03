# 5 LLM Quantization Techniques

- **原邮件主题**: 5 LLM Quantization Techniques
- **发送人**: Daily Dose of DS <avi@dailydoseofds.com>
- **日期**: Tue, 21 Jul 2026 22:13:47 +0000
- **ID**: 19f86be0631f8e2c

---

## [**5 LLM Quantization Techniques**](<https://fff97757.click.kit-mail3.com/27uprpxd03foh8mg2dvs3hgr6675gsghgmk33/owhkhqhw26ld34tvhr/aHR0cHM6Ly93d3cuZGFpbHlkb3Nlb2Zkcy5jb20vcXVhbnRpemF0aW9uLW9wdGltaXplLW1sLW1vZGVscy10by1ydW4tdGhlbS1vbi10aW55LWhhcmR3YXJlLw==>)

A 70B parameter model in FP16 requires 140GB of memory for weights alone.

That exceeds any single GPU available today:

  * An H100 carries 80GB
  * An RTX 4090 carries 24GB

So serving the model in half precision means multi-GPU setups and tensor parallelism before the first token is generated.

![](https://substackcdn.com/image/fetch/$s_!mcn3!,w_1456,c_limit,f_auto,q_auto:good,fl_lossy/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F437225d5-c382-4f8e-9ea3-88bb9b0e78b5_1554x274.gif)   
---  
  
Quantization reduces this footprint by storing weights in lower bits.

The standard scheme maps each weight from FP16 onto a small integer grid: compute the dynamic range of the tensor, divide it into `2^b` levels (16 levels at 4-bit), round each weight to the nearest level, and store a scale factor to dequantize during inference.

![](https://substackcdn.com/image/fetch/$s_!BYVx!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6090d643-2b7b-40be-a391-abd20cbf8d99_2899x991.png)   
---  
  
At 4-bit, the weight memory drops 4x. The 140GB model fits in 35GB, within the range of a single 40GB or 48GB card.

That said, if rounding were lossless in practice, one method would suffice, and the diagram below would have had one row:

![](https://substackcdn.com/image/fetch/$s_!jdZa!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F82be21c1-7649-4d25-8e4b-b900dda507c0_1350x1200.jpeg)   
---  
  
But it has five because weights and activations in large transformers are not uniformly important.

The `LLM.int8()` paper quantified this. Beyond roughly 6.7B parameters, every transformer layer develops a handful of hidden dimensions carrying values 20x to 100x larger than the rest.

These dimensions make up about 0.1% of the model’s features, but zeroing them out nearly destroys the model’s ability to predict text.

![](https://substackcdn.com/image/fetch/$s_!MCnt!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb306f134-0557-4da8-a23d-ad979dd5306c_4707x1105.png)   
---  
  
These outliers are also what break naive rounding. The quantization grid spans the range of the tensor, so a single activation of magnitude 60 among values near 1 inflates the scale factor and collapses the remaining values into a few levels, destroying their precision.

![](https://substackcdn.com/image/fetch/$s_!Cq7M!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc7d5a73e-26e0-4bf9-b48c-48b841ff5b65_1200x896.jpeg)   
---  
  
Each method in the visual shown earlier solves this saliency problem differently.

1) `RTN` (round to nearest) does not handle it at all. It applies the scale-and-round procedure directly with no calibration data, which makes it the cheapest baseline and the weakest at low bit widths, where accumulated rounding error is unrecoverable.

![](https://substackcdn.com/image/fetch/$s_!gLDQ!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F1615326b-b912-4c5d-86f3-a89d727141dc_1338x216.png)   
---  
  
2) `GPTQ` corrects rounding damage as it happens. It quantizes the weights of a layer a few at a time, measures how much error the rounding just introduced, and nudges the not-yet-quantized weights to cancel out that error before moving on.

![](https://substackcdn.com/image/fetch/$s_!Ewpo!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F62adc36e-0ca4-4f04-a661-04f1ae9a1ef0_1338x214.png)   
---  
  
The adjustment is not uniform. GPTQ uses statistics from calibration data to work out which remaining weights can absorb the error with the least effect on the layer’s output, which is what separates it from blind rounding.

This runs fast enough to matter in practice. A 175B model quantizes to 4-bit in around four GPU hours. The known weakness is that fitting the calibration data this closely can tune the model to it, and the AWQ authors showed this hurts accuracy on inputs that look different from the calibration set.

3) `AWQ` protects the important weights before rounding instead of repairing damage afterward. It runs calibration samples through the model and watches which weights get multiplied by the largest incoming values, because a rounding error on those weights gets amplified the most in the layer’s output.

![](https://substackcdn.com/image/fetch/$s_!c6nX!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F8dcb2c2d-36cb-429d-b4ec-dc6d6e35837f_1338x214.png)   
---  
  
Only around 1% of weight channels turn out to matter this much. Rather than storing them at higher precision, AWQ multiplies them by a scaling factor before rounding, so they spread across more levels of the grid and lose less detail, and the math is rearranged so a matching inverse scale elsewhere keeps the layer’s output unchanged.

Every weight still ends up in plain INT4, with no special-case handling at inference time. AWQ also depends far less on which calibration samples were used than GPTQ does, which is a big part of why it became the standard choice in serving engines like vLLM.

4) `LLM.int8()` isolates the outliers instead of fighting them. When the model is loaded, it finds the dimensions carrying extreme values and splits every matrix multiplication into two:

![](https://substackcdn.com/image/fetch/$s_!tej0!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F741c84cf-d58e-4d07-9700-50467aa67772_1338x214.png)   
---  
  
  * The outliers run in full FP16
  * The other 99.9% of values run in INT8, and the two results are added back together.

Nothing needs to be computed ahead of time. That is why it is also available as the `load_in_8bit` flag in `bitsandbytes`.

The cost is speed. Splitting and merging every matrix multiplication is slower than running one optimized 4-bit kernel, so this path is common for local development and QLoRA fine-tuning, not for serving traffic at scale.

5) `QAT` modifies training rather than the quantization procedure. During a short fine-tuning run, every forward pass rounds the weights to INT4 before using them, so the model experiences the exact damage that quantization will cause, and its predictions are scored under that damage.

![](https://substackcdn.com/image/fetch/$s_!mfLX!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F22678dba-f5c8-458b-95c1-fb07f317ed48_1338x231.png)   
---  
  
The weight updates still happen in full precision behind the scenes, since rounding itself cannot be trained through directly. Over the fine-tuning run, the weights drift toward values that keep the loss low even after rounding, so when the real quantization is applied at the end, there is almost nothing left to break.

Google produced its Gemma 3 QAT checkpoints with roughly 5,000 fine-tuning steps guided by the original model’s outputs, and the int4 versions hold close to full-precision quality at about 3x lower memory.

* * *

All five methods described above produce the same artifact, i.e., a model at a fraction of its trained precision.

They differ in where the outlier problem gets addressed, at rounding time, after rounding, before rounding, at inference, or during training itself.

To dive deeper, we have already written a full [**deep dive on Quantization**](<https://fff97757.click.kit-mail3.com/27uprpxd03foh8mg2dvs3hgr6675gsghgmk33/owhkhqhw26ld34tvhr/aHR0cHM6Ly93d3cuZGFpbHlkb3Nlb2Zkcy5jb20vcXVhbnRpemF0aW9uLW9wdGltaXplLW1sLW1vZGVscy10by1ydW4tdGhlbS1vbi10aW55LWhhcmR3YXJlLw==>), specifically, which covers several of these methods with their simplified mathematics.

![](https://substackcdn.com/image/fetch/$s_!fatV!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F9c860c15-3e43-4403-9344-dccf0b0e3988_1004x442.png)   
---  
  
[**Learn how Quantization lets us run LLMs on tiny hardware here →**](<https://fff97757.click.kit-mail3.com/27uprpxd03foh8mg2dvs3hgr6675gsghgmk33/owhkhqhw26ld34tvhr/aHR0cHM6Ly93d3cuZGFpbHlkb3Nlb2Zkcy5jb20vcXVhbnRpemF0aW9uLW9wdGltaXplLW1sLW1vZGVscy10by1ydW4tdGhlbS1vbi10aW55LWhhcmR3YXJlLw==>)
