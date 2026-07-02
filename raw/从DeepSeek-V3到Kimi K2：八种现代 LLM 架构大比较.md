---
id: "7351871331060679617"
cubox_url: https://cubox.pro/web/card/7351871331060679617
url: https://mp.weixin.qq.com/s?__biz=MzIyNjM2MzQyNg==&mid=2247709807&idx=1&sn=a142fa7e5e509b9404b3c40ad44d7167&poc_token=HI-OjGijjge9eMarfDD_p7klpkVdMqh5X7NC-F9w
tags:
  - LLM/arch/MoE
---
# 从DeepSeek-V3到Kimi K2：八种现代 LLM 架构大比较



[Read in Cubox](https://cubox.pro/web/card/7351871331060679617)  
[Read Original](https://mp.weixin.qq.com/s?__biz=MzIyNjM2MzQyNg==&mid=2247709807&idx=1&sn=a142fa7e5e509b9404b3c40ad44d7167&poc_token=HI-OjGijjge9eMarfDD_p7klpkVdMqh5X7NC-F9w)  

---


---

## 📖 正文全文

# 从DeepSeek-V3到Kimi K2：八种现代 LLM 架构大比较

[mp.weixin.qq.com](https://mp.weixin.qq.com/s?__biz=MzIyNjM2MzQyNg==&mid=2247709807&idx=1&sn=a142fa7e5e509b9404b3c40ad44d7167&poc_token=HI-OjGijjge9eMarfDD_p7klpkVdMqh5X7NC-F9w)Datawhale


Datawhale干货

**作者：Sebastian Raschka**


> 编译：PaperAgent

距离最初的 GPT 架构问世，已经过去了七年。乍看之下，回溯到 GPT-2（2019 年），再展望 DeepSeek-V3 和 Llama 4（2024-2025 年），人们或许会惊讶于这些模型在结构上竟依然如此相似。

当然，位置嵌入已经从绝对位置编码演变为旋转位置编码（RoPE），多头注意力机制已基本被分组查询注意力机制所取代，更高效的 SwiGLU 激活函数也取代了 GELU 等传统激活函数。但在这些细微的改进背后，我们是真正看到了突破性的变化，还是仅仅在对相同的架构基础进行打磨？

<br />

架构示意图：DeepSeek V3/R1、OLMo 2、Gemma 3、Mistral Small 3.1、Llama 4、Qwen3、SmolLM3和Kimi 2

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2FvI9nYe94fsFuNPibFzrKDibDZJ8xJyh6jmCiazbkREqR6qWqwTibYuInNnxTMaIWD7EtP9w1LkblrVWuvxlHibucuHQ%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26randomid%3D0y3mkty3%26tp%3Dwebp%26wxfrom%3D5%26wx_lazy%3D1&valid=false)

原文地址：https://sebastianraschka.com/blog/2025/the-big-llm-architecture-comparison.html


## 一、DeepSeek V3/R1
DeepSeek V3 中引入的两种关键架构技术，这些技术提高了其计算效率，并使其有别于许多其他 LLM：多头潜在注意力（MLA）、混合专家（MoE）：
1.1 多头潜在注意力（MLA）
MLA旨在解决传统多头注意力（MHA）在大规模模型中内存占用过高的问题。与分组查询注意力（GQA）相比，MLA通过压缩键和值张量来进一步减少内存使用。
MHA 与 GQA 的比较。此处，组大小为 2，其中两个查询共享一个键值对。
![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2FvI9nYe94fsFuNPibFzrKDibDZJ8xJyh6jm2tuLHmvLVRvoclHFfsOOBIDdQibaX9PKiba8X2meZoo4LgDCXt4chaqA%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26randomid%3D4eub9bvv%26tp%3Dwebp%26wxfrom%3D5%26wx_lazy%3D1&valid=false)
在MLA中，键和值张量在存储到KV缓存之前会被压缩到一个低维空间。在推理时，这些压缩的张量会被重新投影回原始大小。这种设计虽然增加了额外的矩阵乘法操作，但显著降低了内存占用。
MLA（用于 DeepSeek V3 和 R1）与常规 MHA 的比较。
![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2FvI9nYe94fsFuNPibFzrKDibDZJ8xJyh6jm50sWLa5vN5W7sx3K9veO40REfQXqTp42BchYZVBAF1ibKszg9xB2Oicw%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26randomid%3Dwut0j1hq%26tp%3Dwebp%26wxfrom%3D5%26wx_lazy%3D1&valid=false)
1.2 混合专家（MoE）
MoE将传统的前馈模块替换为多个专家层，每个专家层也是一个前馈模块。在推理时，一个路由器会选择一小部分专家进行激活。例如，DeepSeek V3有256个专家，但每次推理仅激活9个专家（1个共享专家和8个由路由器选择的专家）。
V3/R1 中的混合专家 (MoE) 模块（右）与具有标准前馈块的 LLM（左）的比较图。
![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2FvI9nYe94fsFuNPibFzrKDibDZJ8xJyh6jmN8JRWePiaRL1L0HUCDxdAHU9E9shlBIsk8mlM5qMpnGlribcmE0VBQXg%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26randomid%3Dhiixys26%26tp%3Dwebp%26wxfrom%3D5%26wx_lazy%3D1&valid=false)
## 二、OLMo 2
2.1 归一化层放置
OLMo 2采用后归一化（Post-Norm）策略，与大多数LLM采用的前归一化（Pre-Norm）不同。这种设计旨在提高训练稳定性。
在OLMo 2中，归一化层被放置在注意力模块和前馈模块之后，而不是之前。这种设计与原始Transformer架构中的Post-LN类似，但使用了RMSNorm而非LayerNorm。
Post-Norm、Pre-Norm和OLMo 2的Post-Norm变体的对比图。
![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2FvI9nYe94fsFuNPibFzrKDibDZJ8xJyh6jmOiboWTPLxfBBPUa59XynSkAkVbic1tticwwJhL2QcGlwNNb506b0Hn9Mw%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26randomid%3Djg1932j3%26tp%3Dwebp%26wxfrom%3D5%26wx_lazy%3D1&valid=false)
研究表明，后归一化有助于训练稳定性，尤其是在不使用精心设计的学习率预热策略时。OLMo 2的训练损失曲线表明，这种设计在训练过程中表现更为稳定。
Pre-Norm（如GPT-2、Llama 3和许多其他模型中使用的）与OLMo 2的Post-Norm变体的训练稳定性对比图。
![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2FvI9nYe94fsFuNPibFzrKDibDZJ8xJyh6jm1sJNRH3C0JPjNtOD8ycXFfXtGiaVzPuHIKvGx3oiahNJibxibUic7YJFUeQ%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26randomid%3Dcx06n9qt%26tp%3Dwebp%26wxfrom%3D5%26wx_lazy%3D1&valid=false)
2.2 QK-Norm
QK-Norm是在多头注意力模块中引入的额外RMSNorm层，应用于查询（q）和键（k）之前。这种设计有助于在应用RoPE之前对输入进行归一化，从而减少训练过程中的数值不稳定。
class GroupedQueryAttention(nn.Module): def __init__( self, d_in, num_heads, num_kv_groups, head_dim=None, qk_norm=False, dtype=None ): # ... if qk_norm: self.q_norm = RMSNorm(head_dim, eps=1e-6) self.k_norm = RMSNorm(head_dim, eps=1e-6) else: self.q_norm = self.k_norm = None def forward(self, x, mask, cos, sin): b, num_tokens, _ = x.shape # Apply projections queries = self.W_query(x) keys = self.W_key(x) values = self.W_value(x) # ... # Optional normalization if self.q_norm: queries = self.q_norm(queries) if self.k_norm: keys = self.k_norm(keys) # Apply RoPE queries = apply_rope(queries, cos, sin) keys = apply_rope(keys, cos, sin) # Expand K and V to match number of heads keys = keys.repeat_interleave(self.group_size, dim=1) values = values.repeat_interleave(self.group_size, dim=1) # Attention attn_scores = queries @ keys.transpose(2, 3) # ...
OLMo 2 和 Llama 3；可以看出，除了 OLMo 2 仍然使用传统的 MHA 而非 GQA 之外，它们的架构在其他方面相对相似。
Llama 3 和 OLMo 2 的架构比较。
![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2FvI9nYe94fsFuNPibFzrKDibDZJ8xJyh6jmqTBF5pLFoz7MvozQkm1KIOqtlsNhribLnBmI2FVb3CUsyBzck1UYhAw%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26randomid%3Dgrknla1v%26tp%3Dwebp%26wxfrom%3D5%26wx_lazy%3D1&valid=false)
## 三、Gemma 3
3.1 滑动窗口注意力
滑动窗口注意力旨在减少KV缓存的内存需求，同时保持模型的性能。这种设计特别适用于需要处理长序列的任务。
通过滑动窗口注意力实现的KV缓存内存节省。
![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2FvI9nYe94fsFuNPibFzrKDibDZJ8xJyh6jmqIA3BEz6nic56jczDKIfS9iaYk8zibGiaDeIILEsx52Vv59iamzI9YSE17g%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26randomid%3Dr5gbk25x%26tp%3Dwebp%26wxfrom%3D5%26wx_lazy%3D1&valid=false)
滑动窗口注意力限制了每个查询位置的上下文范围，使其仅关注局部窗口内的内容。与传统的全局注意力机制相比，这种设计显著减少了KV缓存的内存占用。例如，Gemma 3将滑动窗口大小从Gemma 2的4096减少到1024，并调整了全局与局部注意力的比例。
常规注意力（左）和滑动窗口注意力（右）的对比图。
![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2FvI9nYe94fsFuNPibFzrKDibDZJ8xJyh6jmticvHynYibcCYLDtoL2SpZgVSkURYTbc9Zy4kAdH0PnV3VhSa1O5PTUA%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26randomid%3Djd36sxsx%26tp%3Dwebp%26wxfrom%3D5%26wx_lazy%3D1&valid=false)
研究表明，滑动窗口注意力对模型的建模性能影响极小，但在内存使用上带来了显著的优化。这种设计使得Gemma 3在处理长序列时更加高效。
常规注意力（左）和滑动窗口注意力（右）的对比图。
![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2FvI9nYe94fsFuNPibFzrKDibDZJ8xJyh6jmGrQ00giaP7ODictRc1faNRkg0djcsI58rkB7VyNuOgaxBZafsUpMWLTw%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26randomid%3Dqwbrtox6%26tp%3Dwebp%26wxfrom%3D5%26wx_lazy%3D1&valid=false)
3.2 归一化层放置
Gemma 3在注意力模块和前馈模块前后都放置了RMSNorm层。这种设计结合了前归一化和后归一化的优点，既保持了训练稳定性，又提高了推理效率。
OLMo 2和Gemma 3的架构对比图；注意Gemma 3中额外的归一化层。
![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2FvI9nYe94fsFuNPibFzrKDibDZJ8xJyh6jmAcwdgm04L5Cj0uszQmnnLnfhqVJ4iag98joQwF34OuRiblicxAoFZZxbw%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26randomid%3D7e3md9s9%26tp%3Dwebp%26wxfrom%3D5%26wx_lazy%3D1&valid=false)
## ## 四、Mistral Small 3.1
Mistral Small 3.1通过自定义分词器、缩小KV缓存和减少层数来优化模型。此外，它放弃了滑动窗口注意力，转而使用更高效的FlashAttention技术。
这些优化使得Mistral Small 3.1在推理延迟上优于Gemma 3，同时保持了较高的性能。这种设计特别适合需要快速推理的应用场景。
OLMo 2和Gemma 3的架构对比图；注意Gemma 3中额外的归一化层。
![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2FvI9nYe94fsFuNPibFzrKDibDZJ8xJyh6jmVibUVE4vG84UL2cBnSEVRiaJLXrHLP6xHRGwqr1cJiaicttkK0fsWuYodA%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26randomid%3D7s1xwrh4%26tp%3Dwebp%26wxfrom%3D5%26wx_lazy%3D1&valid=false)
## ## 五、Llama 4
Llama 4采用了与DeepSeek V3类似的架构，但在某些细节上进行了优化，以提高模型的性能和效率。
DeepSeek V3（6710亿参数）和Llama 4 Maverick（4000亿参数）的架构对比图。
![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2FvI9nYe94fsFuNPibFzrKDibDZJ8xJyh6jmibBZ5wtFWLpwtpA79vIA5cXbiaj04QsWOzib3luaiaAvEx304kytbLXXzQ%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26randomid%3Dd3bi7r3m%26tp%3Dwebp%26wxfrom%3D5%26wx_lazy%3D1&valid=false)
Llama 4使用了分组查询注意力（GQA）而非多头潜在注意力（MLA），并且在MoE模块中使用了更少但更大的专家。此外，Llama 4在每个Transformer块中交替使用MoE模块和密集模块。
六、Qwen3
6.1 密集模型
Qwen3 0.6B和Llama 3 1B的架构对比图
![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2FvI9nYe94fsFuNPibFzrKDibDZJ8xJyh6jmvbayvJSNv788zXgedKqz4K7xtm5iaUqMZDbFYHF0FcrNwVBTHiavtx0g%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26randomid%3D1kgpm0g1%26tp%3Dwebp%26wxfrom%3D5%26wx_lazy%3D1&valid=false)
Qwen3的密集模型采用了较深的架构（更多Transformer块），具有更多的层，而 Llama 3 是一种更宽的架构，具有更多的注意力头。Qwen3 的内存占用较小，但生成速度较慢。
6.2 MoE模型
DeepSeek-V3 和 Qwen3 235B-A22B 的架构比较。
![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2FvI9nYe94fsFuNPibFzrKDibDZJ8xJyh6jmOYzlUcLlF2FVMXS0eMHBTWW1ppNrbyfySHn3T6vph8jVs7Qnyte9ibg%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26randomid%3Dvdni5i2b%26tp%3Dwebp%26wxfrom%3D5%26wx_lazy%3D1&valid=false)
Qwen3的MoE模型采用了与DeepSeek V3类似的架构，但在某些细节上有所不同，例如不使用共享专家。这种设计使得模型在训练时能够学习更多知识，而在推理时保持高效。
<br />
七、SmolLM3
SmolLM3 架构看起来相当标准。不过，最有趣的一点或许是它使用了 NoPE（无位置嵌入）。
Qwen3 4B 和 SmolLM3 3B 的架构比较。
![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2FvI9nYe94fsFuNPibFzrKDibDZJ8xJyh6jmicXypNHAM9WN0QIlfLAqsdn60kwTBs89LM28W2iciaXAlrLFicpmibfObcQ%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26randomid%3D042z4tnv%26tp%3Dwebp%26wxfrom%3D5%26wx_lazy%3D1&valid=false)
7.1 无位置嵌入（NoPE）
NoPE不使用任何位置嵌入（绝对位置嵌入或旋转位置嵌入），而是依赖因果注意力掩码来保持序列的自回归顺序。这种设计使得模型在训练过程中能够学习到隐式的位置信息。
绝对位置嵌入示例
![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2FvI9nYe94fsFuNPibFzrKDibDZJ8xJyh6jmqY9vkUjRfQf6H9XgFIFxwicvfA9rm1JCyTsZic8vfovRjDoK8wvuNKKQ%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26randomid%3Djvhe3u6b%26tp%3Dwebp%26wxfrom%3D5%26wx_lazy%3D1&valid=false)
研究表明，NoPE在长度泛化方面表现更好，即在处理更长序列时性能下降较少。这种设计使得SmolLM3在处理长序列任务时表现优异。
![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2FvI9nYe94fsFuNPibFzrKDibDZJ8xJyh6jms0BZCad9SNd86J0j9wa7jkV7Q0xzrfianhrg3n2RJ8cp1rCpRwVYpkw%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26randomid%3Dc5o34i6j%26tp%3Dwebp%26wxfrom%3D5%26wx_lazy%3D1&valid=false)
## 八、Kimi K2
Kimi K2采用了DeepSeek V3的架构，并进行了扩展。它使用了Muon优化器而非AdamW，这可能是其训练损失曲线表现优异的原因之一。此外，Kimi K2在MoE模块中使用了更多的专家，在MLA模块中使用了更少的头。
DeepSeek V3 和 Kimi K2 的架构比较。
![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2FvI9nYe94fsFuNPibFzrKDibDZJ8xJyh6jm8Q2Xxk3Q5tE3eoU7Gd6YjV4do255OEhF8B0L3naaviaib3J2OpJqmgOw%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26randomid%3Dp2u8e03z%26tp%3Dwebp%26wxfrom%3D5%26wx_lazy%3D1&valid=false)
这些设计使得Kimi 2在训练过程中表现优异，训练损失曲线平滑且下降迅速。这可能有助于该模型跃居上述基准测试的榜首。
![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2FvI9nYe94fsFuNPibFzrKDibDZJ8xJyh6jmEltM3jZ9yjBsjZZTs4MA8BOVlzPsWtZqGjTPoRr4eZhibQicw7Pc7n0w%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26randomid%3D7lbnw0nt%26tp%3Dwebp%26wxfrom%3D5%26wx_lazy%3D1&valid=false)
![](https://image.cubox.pro/cardImg/61reu91pogkc13rbbu3r49z5ps0vrjwj6mj7t5o1r73q6kryme?imageMogr2/quality/90/format/gif/ignore-error/1)**一起"**点****赞"****三连** ↓**

[Read in Cubox](https://cubox.pro/web/card/7351871331060679617)
