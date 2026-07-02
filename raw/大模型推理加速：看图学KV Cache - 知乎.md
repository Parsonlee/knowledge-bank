---
id: "7295077168185344557"
cubox_url: https://cubox.pro/web/card/7295077168185344557
url: https://zhuanlan.zhihu.com/p/662498827
tags:
  - LLM/inference/kv-cache
---
# 大模型推理加速：看图学KV Cache - 知乎

KV Cache是Transformer标配的推理加速功能，transformer官方use_cache这个参数默认是True，但是它 只能用于Decoder架构的模型，这是因为Decoder有Causal Mask，在推理的时候前面已经生成的字符不需要与后面的字符…

[Read in Cubox](https://cubox.pro/web/card/7295077168185344557)  
[Read Original](https://zhuanlan.zhihu.com/p/662498827)  

---


---

\## 📖 正文全文

# 大模型推理加速：看图学KV Cache

[zhuanlan.zhihu.com](https://zhuanlan.zhihu.com/p/662498827)看图学双一流计算机硕士｜前百度资深算法工程师｜多年互联网大厂经验关注

[KV Cache](https://zhida.zhihu.com/search?content_id=235350632&content_type=Article&match_order=1&q=KV+Cache&zhida_source=entity)是[Transformer](https://zhida.zhihu.com/search?content_id=235350632&content_type=Article&match_order=1&q=Transformer&zhida_source=entity)标配的推理加速功能，transformer官方use_cache这个参数默认是True，但是它**只能用于[Decoder架构](https://zhida.zhihu.com/search?content_id=235350632&content_type=Article&match_order=1&q=Decoder%E6%9E%B6%E6%9E%84&zhida_source=entity)的模型** ，这是因为Decoder有[Causal Mask](https://zhida.zhihu.com/search?content_id=235350632&content_type=Article&match_order=1&q=Causal+Mask&zhida_source=entity)，在推理的时候前面已经生成的字符不需要与后面的字符产生attention，从而使得前面已经计算的K和V可以缓存起来。

我们先看一下不使用KV Cache的推理过程。假设模型最终生成了"遥遥领先"4个字。

当模型生成第一个"遥"字时，input="\<s\>", "\<s\>"是起始字符。[Attention](https://zhida.zhihu.com/search?content_id=235350632&content_type=Article&match_order=1&q=Attention&zhida_source=entity)的计算如下：
![](https://image.cubox.pro/cardImg/3bxqxfxlho67ux1uhzra0kvtu0qa8w65y3s9374fje73bxzkh3.jpg?imageMogr2/quality/90/ignore-error/1)

为了看上去方便，我们**暂时忽略scale项** <math xmlns="http://www.w3.org/1998/Math/MathML"> d </math>\\sqrt{d}， 但是要注意这个scale面试时经常考。

如上图所示，最终Attention的计算公式如下，（softmaxed 表示已经按行进行了softmax）:

<math display="block" xmlns="http://www.w3.org/1998/Math/MathML"> A t t 1 ( Q , K , V ) = softmax ( Q 1 K 1 T ) V 1 → = softmaxed ( Q 1 K 1 T ) V 1 → </math>{\\color{orange}{Att_1}}(Q, K, V) = \\text{softmax}({\\color{orange}{Q_1}} K_1\^T) \\vec{V_1} = \\text{softmaxed}({\\color{orange}{Q_1}} K_1\^T) \\vec{V_1} \\\\

当模型生成第二个"遥"字时，input="\<s\>遥", Attention的计算如下：
![](https://image.cubox.pro/cardImg/5y360ctjgtaig6pidzdxgwf9cd39a7jqraly3gn6o7mhw89zhm.jpg?imageMogr2/quality/90/ignore-error/1)

当 <math xmlns="http://www.w3.org/1998/Math/MathML"> Q K T </math>QK\^T 变为矩阵时，softmax 会针对 **行**进行计算。写详细一点如下，softmaxed 表示已经按行进行了softmax。
![](https://image.cubox.pro/cardImg/2sz74zbqvzbrl1axmx8ee1uaak71b906djxviogoo7vramzy05.jpg?imageMogr2/quality/90/ignore-error/1)

假设 <math xmlns="http://www.w3.org/1998/Math/MathML"> A t t 1 ( Q , K , V ) </math>{\\color{orange}{Att_1}}(Q, K, V) 表示 Attention 的第一行， <math xmlns="http://www.w3.org/1998/Math/MathML"> A t t 2 ( Q , K , V ) </math>{\\color{orange}{Att_2}}(Q, K, V) 表示 Attention 的第二行，则根据上面推导，

其计算公式为：

<math display="block" xmlns="http://www.w3.org/1998/Math/MathML"> A t t 1 ( Q , K , V ) = softmaxed ( Q 1 K 1 T ) V 1 → A t t 2 ( Q , K , V ) = softmaxed ( Q 2 K 1 T ) V 1 → + softmaxed ( Q 2 K 2 T ) V 2 → </math> \\begin{aligned} {\\color{orange}{Att_1}}(Q, K, V) \&= \\text{softmaxed}({\\color{orange}{Q_1}} K_1\^T) \\vec{V_1} \\\\ {\\color{red}{Att_2}}(Q, K, V) \&= \\text{softmaxed}({\\color{red}{Q_2}} K_1\^T) \\vec{V_1} + \\text{softmaxed}({\\color{red}{Q_2}} K_2\^T) \\vec{V_2 } \\end{aligned} \\\\

你会发现，由于 <math xmlns="http://www.w3.org/1998/Math/MathML"> Q 1 K 2 T </math>Q_1 K_2\^T 这个值会mask掉，

* <math xmlns="http://www.w3.org/1998/Math/MathML"> Q 1 </math>Q_1**在第二步参与的计算与第一步是一样的，而且第二步生成的** <math xmlns="http://www.w3.org/1998/Math/MathML"> V 1 </math>V_1**也仅仅依赖于** <math xmlns="http://www.w3.org/1998/Math/MathML"> Q 1 </math>Q_1**，与** <math xmlns="http://www.w3.org/1998/Math/MathML"> Q 2 </math>Q_2**毫无关系。**
* <math xmlns="http://www.w3.org/1998/Math/MathML"> V 2 </math>V_2**的计算也仅仅依赖于** <math xmlns="http://www.w3.org/1998/Math/MathML"> Q 2 </math>Q_2**，与** <math xmlns="http://www.w3.org/1998/Math/MathML"> Q 1 </math>Q_1**毫无关系。**

当模型生成第三个"领"字时，input="\<s\>遥遥"Attention的计算如下：
![](https://image.cubox.pro/cardImg/308x7knsrc92ityoo32xwgs1bvk6hr7ljjdmcks6ryesaa2vz0.jpg?imageMogr2/quality/90/ignore-error/1)

详细的推导参考第二步，其计算公式为：

<math display="block" xmlns="http://www.w3.org/1998/Math/MathML"> A t t 1 ( Q , K , V ) = softmaxed ( Q 1 K 1 T ) V 1 → A t t 2 ( Q , K , V ) = softmaxed ( Q 2 K 1 T ) V 1 → + softmaxed ( Q 2 K 2 T ) V 2 → A t t 3 ( Q , K , V ) = softmaxed ( Q 3 K 1 T ) V 1 → + softmaxed ( Q 3 K 2 T ) V 2 → + softmaxed ( Q 3 K 3 T ) V 3 → </math> \\begin{aligned} {\\color{orange}{Att_1}}(Q, K, V) \&= \\text{softmaxed}({\\color{orange}{Q_1}} K_1\^T) \\vec{V_1} \\\\ {\\color{red}{Att_2}}(Q, K, V) \&= \\text{softmaxed}({\\color{red}{Q_2}} K_1\^T) \\vec{V_1} + \\text{softmaxed}({\\color{red}{Q_2}} K_2\^T) \\vec{V_2 } \\\\ {\\color{purple}{Att_3}}(Q, K, V) \&= \\text{softmaxed}({\\color{purple}{Q_3}} K_1\^T) \\vec{V_1} + \\text{softmaxed}({\\color{purple}{Q_3}} K_2\^T) \\vec{V_2 } + \\text{softmaxed}({\\color{purple}{Q_3}} K_3\^T) \\vec{V_3 } \\end{aligned} \\\\

同样的， <math xmlns="http://www.w3.org/1998/Math/MathML"> A t t k </math>Att_k 只与 <math xmlns="http://www.w3.org/1998/Math/MathML"> Q k </math>Q_k 有关。

当模型生成第四个"先"字时，input="\<s\>遥遥领"Attention的计算如下：
![](https://image.cubox.pro/cardImg/5vd00bg2imsnj1zzud3470i68gtm0horo1c1m1xhx4c4j1q87o.jpg?imageMogr2/quality/90/ignore-error/1)

<math display="block" xmlns="http://www.w3.org/1998/Math/MathML"> A t t 1 ( Q , K , V ) = softmaxed ( Q 1 K 1 T ) V 1 → A t t 2 ( Q , K , V ) = softmaxed ( Q 2 K 1 T ) V 1 → + softmaxed ( Q 2 K 2 T ) V 2 → A t t 3 ( Q , K , V ) = softmaxed ( Q 3 K 1 T ) V 1 → + softmaxed ( Q 3 K 2 T ) V 2 → + softmaxed ( Q 3 K 3 T ) V 3 → A t t 4 ( Q , K , V ) = softmaxed ( Q 4 K 1 T ) V 1 → + softmaxed ( Q 4 K 2 T ) V 2 → + softmaxed ( Q 4 K 3 T ) V 3 → + softmaxed ( Q 4 K 4 T ) V 4 → </math> \\begin{aligned} {\\color{orange}{Att_1}}(Q, K, V) \&= \\text{softmaxed}({\\color{orange}{Q_1}} K_1\^T) \\vec{V_1} \\\\ {\\color{red}{Att_2}}(Q, K, V) \&= \\text{softmaxed}({\\color{red}{Q_2}} K_1\^T) \\vec{V_1} + \\text{softmaxed}({\\color{red}{Q_2}} K_2\^T) \\vec{V_2 } \\\\ {\\color{purple}{Att_3}}(Q, K, V) \&= \\text{softmaxed}({\\color{purple}{Q_3}} K_1\^T) \\vec{V_1} + \\text{softmaxed}({\\color{purple}{Q_3}} K_2\^T) \\vec{V_2 } + \\text{softmaxed}({\\color{purple}{Q_3}} K_3\^T) \\vec{V_3 } \\\\ {\\color{brown}{Att_4}}(Q, K, V) \&= \\text{softmaxed}({\\color{brown}{Q_4}} K_1\^T) \\vec{V_1} + \\text{softmaxed}({\\color{brown}{Q_4}} K_2\^T) \\vec{V_2 } + \\text{softmaxed}({\\color{brown}{Q_4}} K_3\^T) \\vec{V_3 } + \\text{softmaxed}({\\color{brown}{Q_4}} K_4\^T) \\vec{V_4 } \\end{aligned} \\\\

和之前类似，不再赘述。

看上面图和公式，我们可以得出结论：

1. **当前计算方式存在大量冗余计算。**
2. <math xmlns="http://www.w3.org/1998/Math/MathML"> A t t k </math>Att_k**只与** <math xmlns="http://www.w3.org/1998/Math/MathML"> Q k </math>Q_k**有关。**
3. **推理第** <math xmlns="http://www.w3.org/1998/Math/MathML"> x k </math>x_k**个字符的时候只需要输入字符** <math xmlns="http://www.w3.org/1998/Math/MathML"> x k − 1 </math>x_{k-1}**即可。**

我们每一步其实之需要根据 <math xmlns="http://www.w3.org/1998/Math/MathML"> Q k </math>Q_k 计算 <math xmlns="http://www.w3.org/1998/Math/MathML"> A t t k </math>Att_k 就可以，之前已经计算的Attention完全不需要重新计算。但是 <math xmlns="http://www.w3.org/1998/Math/MathML"> K </math>K 和 <math xmlns="http://www.w3.org/1998/Math/MathML"> V </math>V 是全程参与计算的，所以这里我们需要把每一步的 <math xmlns="http://www.w3.org/1998/Math/MathML"> K , V </math>K,V 缓存起来。所以说叫KV Cache好像有点不太对，因为KV本来就需要全程计算，可能叫增量KV计算会更好理解。

下面4张图展示了使用KV Cache和不使用的对比。
![](https://image.cubox.pro/cardImg/3qtt3rb1pdi9g6w7ldpc5w7f4togkistdkobowistgz7vgqef8.jpg?imageMogr2/quality/90/ignore-error/1)

下面是gpt里面KV Cache的实现。其实明白了原理后代码实现简单的不得了,就是concat操作而已。

[https://github.com/huggingface/transformers/blob/main/src/transformers/models/gpt2/modeling_gpt2.py\#L318C1-L331C97](https://link.zhihu.com/?target=https%3A//github.com/huggingface/transformers/blob/main/src/transformers/models/gpt2/modeling_gpt2.py%23L318C1-L331C97)

    if layer_past is not None:
            past_key, past_value = layer_past
            key = torch.cat((past_key, key), dim=-2)
            value = torch.cat((past_value, value), dim=-2)
        
        if use_cache is True:
            present = (key, value)
        else:
            present = None
        
        if self.reorder_and_upcast_attn:
            attn_output, attn_weights = self._upcast_and_reordered_attn(query, key, value, attention_mask, head_mask)
        else:
            attn_output, attn_weights = self._attn(query, key, value, attention_mask, head_mask)

最后需要注意当**sequence特别长的时候，KV Cache其实还是个Memory刺客**。

比如batch_size=32, head=32, layer=32, dim_size=4096, seq_length=2048, float32类型，则需要占用的显存为（感谢网友指正） 2 \* 32 \* 4096 \* 2048 \* 32 \* 4 / 1024/1024/1024 /1024 = 64G。

\## 历史相关文章

[想学习大语言模型(LLM)，应该从哪个开源模型开始？854 赞同 · 13 评论回答![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fpic3.zhimg.com%2Fv2-aa5a09c120d69427d5a858fa3d66364a_180x120.jpg&valid=false)](https://www.zhihu.com/question/608820310/answer/3091336166)

[大模型开源SFT训练数据整理46 赞同 · 8 评论文章![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fpicx.zhimg.com%2Fv2-50744c0efe7c34962900546c42200f17_ipico.jpg&valid=false)](https://zhuanlan.zhihu.com/p/634322783)

[国内大模型测评现状169 赞同 · 13 评论文章![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fpic2.zhimg.com%2Fv2-91016fe3847c0d340c81162aa62c6c49_ipico.jpg&valid=false)](https://zhuanlan.zhihu.com/p/660201722)

[大模型参数量和占的显存怎么换算？306 赞同 · 11 评论回答![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fpic4.zhimg.com%2Fv2-e7135a8cf787d44b797c0c9ab7f04f41_180x120.jpg&valid=false)](https://www.zhihu.com/question/612046818/answer/3117938195)

[如何评价超越Llama的Falcon模型？208 赞同 · 11 评论回答![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fpic3.zhimg.com%2Fv2-21bd1e25a25f79350fd6acf3cfb10cd6_180x120.jpg&valid=false)](https://www.zhihu.com/question/605021170/answer/3060877755)

[ChatGPT平替模型：LLaMA（附下载地址，平民玩家和伸手党的福音！）97 赞同 · 44 评论文章![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fpic2.zhimg.com%2Fv2-7d2c5789a96efe78795134449a21b90d_ipico.jpg&valid=false)](https://zhuanlan.zhihu.com/p/614118339)

[为什么大模型输入输出往往只有2K, 4K token?48 赞同 · 4 评论回答![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fpic1.zhimg.com%2Fv2-913c3b71221bca23ac239a2599da6a46_ipico.jpg&valid=false)](https://www.zhihu.com/question/606514058/answer/3104085523)

[Read in Cubox](https://cubox.pro/web/card/7295077168185344557)
