---
id: "7311397260774870486"
cubox_url: https://cubox.pro/web/card/7311397260774870486
url: https://zhuanlan.zhihu.com/p/1888290264377976190
tags:
  - LLM/arch/attention
---
# deepseek MLA 矩阵吸收浅谈 - 知乎

一个小例子在开始之前，我们先看一个小例子 a = torch.randn(1000, 500, 1000, device=&#39;cuda&#39;) b = torch.randn(1000, 1000, 2000, device=&#39;cuda&#39;) t1 = time.time() c = a @ b # c shape(1000,50…

[Read in Cubox](https://cubox.pro/web/card/7311397260774870486)  
[Read Original](https://zhuanlan.zhihu.com/p/1888290264377976190)  

---


---

## 📖 正文全文

# deepseek MLA 矩阵吸收浅谈

[zhuanlan.zhihu.com](https://zhuanlan.zhihu.com/p/1888290264377976190)大猫咪与小狮子从初识到五境之上，无它，但手熟尔。关注

目录

收起

一个小例子

MLA计算流程

Q矩阵的处理

KV矩阵处理

编码部分计算注意力权重

拆分KV升维矩阵

K升维矩阵的吸收

注意力分数计算

V升维矩阵的吸收和最终注意力分数

小总结

## 一个小例子

在开始之前，我们先看一个小例子

    a = torch.randn(1000, 500, 1000, device='cuda')
    b = torch.randn(1000, 1000, 2000, device='cuda')
    t1 = time.time()
    c = a @ b  # c shape(1000,500,2000)
    t2 = time.time()
    print("t2-t1:{}".format(t2 - t1))

本机笔记本 4080 上

t2-t1:0.47059178352355957

继续对比：

    d = torch.randn(1000, 500, 1000, device='cuda')
    e = torch.randn(1, 1000, 2000, device='cuda')
    t2 = time.time()
    f = d @ e  # f shape(1000,500,2000)
    t3 = time.time()
    print(" t3-t2:{}".format(t3 - t2))

t3-t2:0.11941194534301758

相比两块代码，第二块代码进行相乘的时候发生了张量的广播，但它的计算耗时却远低于前者，其本质原因是在于计算时，张量广播降低了内存的访问。

有了这个背景，我们再研究[MLA矩阵吸收](https://zhida.zhihu.com/search?content_id=255609228&content_type=Article&match_order=1&q=MLA%E7%9F%A9%E9%98%B5%E5%90%B8%E6%94%B6&zhida_source=entity)怎么优化性能的

接下来， 我们假设当前查询Q矩阵的shape为：\[B:2, S:1, C:7168\]，KV矩阵为：\[B:2, S:12, C:7168\]，其本质是模拟自回归模型推理的过程。

图中符号对应的图例：

B: Batch_size  
S: 序列长度  
C: 分类数  
H: 多头数  
N: 不用[位置编码](https://zhida.zhihu.com/search?content_id=255609228&content_type=Article&match_order=1&q=%E4%BD%8D%E7%BD%AE%E7%BC%96%E7%A0%81&zhida_source=entity)部分  
R: 旋转位置编码部分  
L: Low rank 数

## MLA计算流程

所有流程参考与[deepseek](https://zhida.zhihu.com/search?content_id=255609228&content_type=Article&match_order=1&q=deepseek&zhida_source=entity)代码，MLA参考这张图，由于网上有很多关于该图的说明，以及公式的推导过程，所以，在本文中不再进行MLA解释和公式推导。
![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fpica.zhimg.com%2Fv2-5c9ec87b329e320a4ce936ef7f7b3740_1440w.jpg&valid=false)

### Q矩阵的处理

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fpica.zhimg.com%2Fv2-ca25c78484afb66f5f46f4af34f39358_1440w.jpg&valid=false)

首先将输入的查询Q进行低秩投影，然后再升维，最后拆分为需要进行位置编码的部分q_rope， 和无需位置编码的部分q_nope。

### KV矩阵处理

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fpica.zhimg.com%2Fv2-9e53ab0aa41d61fdbef880277cc1d026_1440w.jpg&valid=false)

KV先进行降秩投影，注意，对比与Q矩阵，KV并未进行升维，得到k_rope需要进行位置编码的部分和compressed_kv，至于升维矩阵，将在后面通过矩阵吸收处理。

### 编码部分计算注意力权重

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fpica.zhimg.com%2Fv2-f6ea989e6886151db21cea15ebcfda62_1440w.jpg&valid=false)

对于Q的编码部分和K的编码部分，进行完位置编码之后，即可计算该部分的注意力权重，注意，此处q_rope编码的时候，应提供该词的具体位置，而不是使用S=1。另外，此处也是体现了矩阵吸收的地方，观察k_rope，其头的维度为1， 也就是此处的注意力权重计算为广播计算，**使用了"小例子"优化逻辑**。 假如我们在KV矩阵处理的时候，进行了升维度操纵，那么这儿的k_rope的头就是H=16，它的性能将低于当前H=1情况。

### 拆分KV升维矩阵

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fpic3.zhimg.com%2Fv2-ea94e1bbce62a8060470259be9f09182_1440w.jpg&valid=false)

KV的升维矩阵是由nn.Linear创建的，它的in_features= 512, out_features = 头信息（K的nope部分 + V的nope部分） = 16\*(128+128)=4096。此处值得注意的是，KV的升维矩阵是多头的，也就是说，MLA矩阵吸收既继承了[MQA](https://zhida.zhihu.com/search?content_id=255609228&content_type=Article&match_order=1&q=MQA&zhida_source=entity)的优势，同时又极大的降低了信息的损失。

此处的操作是将升维矩阵拆分成k_up（K的升维矩阵）和v_up（V的升维矩阵），k_up和v_up在后面将会被吸收。

### K升维矩阵的吸收

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fpic4.zhimg.com%2Fv2-ef08db149d9be2e4c167e69c945f6aad_1440w.jpg&valid=false)

此处可以看见， q_nope @ k_up 即将k_up吸收如q_nope中，此处q_nope和k_up都包含多头信息。

### 注意力分数计算

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fpicx.zhimg.com%2Fv2-4b76df9a85b4a75b2c3f3903421fe3e7_1440w.jpg&valid=false)

此处将吸收了k_up的q_nope与compressed_kv进行注意力计算，值得注意的是：这儿的compressed_kv并没有包含头信息，**也就是用到了我们"小例子"所提到的优化逻辑。**之后再将编码位置的注意力权重和未编码部分的注意力权重进行相加，得到最终的注意力权重，再根据注意力计算的公式进行缩放点积和softmax。

另外还有值得注意的一个点，在于注意力权重和compressed_kv进行相乘的时候，同样compressed_kv也是没有头信息的，**也即是会用到我们"小例子"的优化逻辑。**

至此，我们可以看到有三个位置用到"小例子"优化逻辑：

**注意力权重1：Q的位置编码 @ K的位置编码\^T**

**注意力权重2：Q的非位置编码部分 @ compressed_kv\^T**

**注意力分数计算： 注意力权重 @ compressed_kv**

这也就是MLA矩阵吸收所带来的好处，它在注意力计算的时候，对K 和V 的计算都不包含头信息在内。考虑到deepseek的多头数是128，所以此项优化给deepseek带来巨大的收益。

### V升维矩阵的吸收和最终注意力分数

接下来，我们要对V的升维矩阵进行吸收
![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fpica.zhimg.com%2Fv2-75d1ea66e9331eb4f17c616d736e531e_1440w.jpg&valid=false)

至此，使用注意力分数 @v_up\^T即可吸收V的升维矩阵v_up， 最后在将头信息进行合并，再用nn.Linear投影出最终的注意力分数，至此，MLA注意力计算结束。

## 小总结

1. MLA既继承了MQA的优势，同时又极大的保留了信息的表达。
2. 矩阵吸收带来的优化是在注意力计算的时候，K和V不包含头信息，以至于计算的时候减少了内存的访问。
3. 文章中每一张流程图都是一个独立的实现，代码实现可以按每张图的流程进行。与deepseek官方提供的相比，提高了代码可读性。

附上MLA计算全部流程图：
![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fpic3.zhimg.com%2Fv2-10d31686f8f45923d3913b2069c0cbae_1440w.jpg&valid=false)

声明： 转载注明出处

[Read in Cubox](https://cubox.pro/web/card/7311397260774870486)
