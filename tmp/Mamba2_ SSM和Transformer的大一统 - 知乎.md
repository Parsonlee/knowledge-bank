# Mamba2: SSM和Transformer的大一统

[zhuanlan.zhihu.com](https://zhuanlan.zhihu.com/p/705138777)HongzhuzhuOptimistic Pessimist关注她

目录

收起

Introduction

SSD Model

The Linear (SSM) Mode

The Attention Mode: Structured Attention

SSM与Attention的联系

State Space Duality（状态空间对偶）

Efficiency: the SSM and Attention Modes

SSD Algorithm：Block Matrix Decomposition

SSD Algorithm: Chunking and State Passing

Code

Computation Cost

Mamba2 Architecture

Block Design

Multihead Patterns for Sequence Transformations

System and Scaling Optimizations

Tensor Parallel（张量并行）

Sequence Parallel（序列并行）

Variable Length（可变长度）

References:

## Introduction

最近Mamba-2被ICML接收，实现了状态空间模型和[注意力机制](https://zhida.zhihu.com/search?content_id=244828514&content_type=Article&match_order=1&q=%E6%B3%A8%E6%84%8F%E5%8A%9B%E6%9C%BA%E5%88%B6&zhida_source=entity)的大一统，不仅拥有较强的模型表现，还实现了性能的8倍优化。我最近正好在研读这方面的工作，认真学习了一下技术报告和原文，这里就做一些记录。原文真的太长了，所以本文力求提取核心思想，有错误之处，请大家帮忙指出和改正。但是原文真的非常值得一读！从理论基础到算法设计，到模型结构的设计，到系统性能优化，真的是十分全面和系统，值得反复品味和学习。

**Mamba解决的问题：**

Transformer类模型是当下LLM主流的模型结构，有着良好的并行性能和模型效果，但是也存在着一些缺点：训练过程，计算复杂度随着序列长度二次增加；推理过程，需要大量的memory来缓存kv cache。

**Mamba1：**通过改进模型结构，提出了状态空间模型（SSM），训练时通过高效的算法降低了计算复杂度为线性；推理时生成每个token计算和显存是常量（在初始化SSM states之后），不随序列长度而变化。

**Mamba-2的改进：** 提出了状态空间对偶（SSD）框架，连接了状态空间模型、[结构化矩阵](https://zhida.zhihu.com/search?content_id=244828514&content_type=Article&match_order=1&q=%E7%BB%93%E6%9E%84%E5%8C%96%E7%9F%A9%E9%98%B5&zhida_source=entity)和注意力机制。SSD可以从三个方面来理解：SSD Model是一个 DNN 模型层，可以用来组合以构建模型；SSD Framework是一个分析框架，可以分析各种生成式模型特点；SSD algorithm是更加适合GPU计算的高效算法，比 SSM 有更高的计算效率。最后，基于SSD还可以进行系统层面的优化，充分利用针对Transformers开发的优化，例如张量并行，序列并行，可变长序列的训练和推理等。

**Mamba效果：**

Nvidia做了更多的验证，分为两个方面（参考[An Empirical Study of Mamba-based Language Models](https://link.zhihu.com/?target=https%3A//arxiv.org/pdf/2406.07887)）：

**纯基于SSM的模型：**通过比较8b参数量的Mamba，Mamba-2和Transformers结构的模型，在3.5T token长度上进行训练，结果发现纯基于SSM结构的模型在很多任务上可以匹敌或者超过Transformers结构的模型；但是在特定任务上比如strong copying，in-context learning和long-context reasoning上表现略差。

**混合模型（Mamba-2-Hybrid）：**8B参数，包含43% Mamba-2, 7% self-attention, 50% MLP层，改模型在所有12个标准任务上超过了8b的Transformer模型，推理过程得到了8倍的提速。长文本任务上，在16K，32K，128K任务中，Hybrid模型可以达到和Transformer模型相当或超过的水平。

## SSD Model

### The Linear (SSM) Mode

**Structured State Space Models （结构化状态空间模型，SSM）：**

<math display="block" xmlns="http://www.w3.org/1998/Math/MathML"> h t = A h t − 1 + B x t y t = C T h t </math>\\begin{aligned} h_t \& ={A} h_{t-1}+{B} x_t \\\\ y_t \& =C\^{T} h_t \\end{aligned} \\\\

本质是定义了一个映射 <math xmlns="http://www.w3.org/1998/Math/MathML"> x ∈ R T → y ∈ R T </math>x \\in \\mathbb{R}\^{\\mathrm{T}} \\rightarrow y \\in \\mathbb{R}\^{\\mathrm{T}} ， <math xmlns="http://www.w3.org/1998/Math/MathML"> x t , y t </math>x_t,y_t 都是标量，中间隐藏状态 <math xmlns="http://www.w3.org/1998/Math/MathML"> h t </math>h_t 是 <math xmlns="http://www.w3.org/1998/Math/MathML"> N </math>N 维向量。参数 <math xmlns="http://www.w3.org/1998/Math/MathML"> A ∈ R ( T , N , N ) , B ∈ R ( T , N ) , C ∈ R ( T , N ) </math>A \\in \\mathbb{R}\^{(\\mathrm{T}, \\mathrm{N}, \\mathrm{N})}, B \\in \\mathbb{R}\^{(\\mathrm{T}, \\mathrm{N})} \\text {, } C \\in \\mathbb{R}\^{(\\mathrm{T}, \\mathrm{N})} 。

**为什么是结构化SSM？**

**结构化矩阵的定义：**

一般矩阵 <math xmlns="http://www.w3.org/1998/Math/MathML"> M ∈ R ( T , T ) </math>M \\in \\mathbb{R}\^{(\\mathrm{T}, \\mathrm{T})} 需要 <math xmlns="http://www.w3.org/1998/Math/MathML"> T 2 </math>T\^{2} 个参数来表示，并且需要 <math xmlns="http://www.w3.org/1998/Math/MathML"> O ( T 2 ) </math>O(T\^{2}) 时间来执行矩阵-向量乘法等基本操作。结构化矩阵是指：

* 通过压缩表示可以为以二次（理想情况下线性）参数表示的矩阵，且
* 可以通过对这种压缩表示进行直接操作来实现快速算法（最重要的是矩阵乘法）。

控制时间动态的矩阵 A 必须是结构化的，常见的结构化矩阵是稀疏矩阵和低秩矩阵。这些具有特定形式的矩阵才能在深度神经网络中高效地计算这种序列到序列的转换。

注意：文章中SSM就指代结构化SSM。

**离散化：**

以上的状态表示是连续的，而在实际的系统中状态通常是通过采样来获取的，因此需要进行离散化处理。Mamba2 paper 为了简化，就不单独为离散的矩阵设置单独的符号表示了。所以在本文中，我们就直接认为A，B已经做好了离散化处理。也就是说， <math xmlns="http://www.w3.org/1998/Math/MathML"> ( A , B ) </math>(A, B) 是通过参数 <math xmlns="http://www.w3.org/1998/Math/MathML"> ( A ¯ , B ¯ ) </math>(\\overline{A} ,\\overline{B}) 以及step size <math xmlns="http://www.w3.org/1998/Math/MathML"> Δ </math>\\Delta 生成的。连续的参数 <math xmlns="http://www.w3.org/1998/Math/MathML"> ( Δ , A ¯ , B ¯ ) </math>(\\Delta,\\overline{A} ,\\overline{B}) 通过公式 <math xmlns="http://www.w3.org/1998/Math/MathML"> A = f A ( Δ , A ¯ ) </math>A=f_{A}(\\Delta,\\overline{A}) 和 <math xmlns="http://www.w3.org/1998/Math/MathML"> B = f B ( Δ , B ¯ ) </math>B=f_{B}(\\Delta,\\overline{B}) 转成离散参数 <math xmlns="http://www.w3.org/1998/Math/MathML"> ( A , B ) </math>(A, B)，其中 <math xmlns="http://www.w3.org/1998/Math/MathML"> ( f A , f B ) </math>(f_{A},f_{B}) 为离散准则。

**离散化步长的说明：** 对于连续信号保持一个特定值的时间可以由一个可学习的参数表示，称为步长 <math xmlns="http://www.w3.org/1998/Math/MathML"> Δ </math>\\Delta 。根据连续信号和步长采样，就可以得到离散输出。
![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fpic3.zhimg.com%2Fv2-d900d9d725122139f7de6d477e7840f8_1440w.jpg&valid=false)

离散化处理的方法：Zero-order hold
![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fpic1.zhimg.com%2Fv2-bc8c9a00492fbda420a5134ff4d03bb8_1440w.jpg&valid=false)

**选择性状态空间模型（selective state space model）**

为什么要用selective SSM？这部分主要是Mamba1解决的问题， 我们简要说明一下：

[Structured State Space for Sequence Modeling](https://link.zhihu.com/?target=https%3A//arxiv.org/abs/2111.00396) (S4)：

<math display="block" xmlns="http://www.w3.org/1998/Math/MathML"> h t = A h t − 1 + B x t y t = C ⊤ h t </math>\\begin{aligned} h_t \& =A h_{t-1}+B x_t \\\\ y_t \& =C\^{\\top} h_t \\end{aligned}\\\\

* 也就是线性时不变SSM，可以表达为卷积形式和循环形式；卷积形式可以实现并行，输出 <math xmlns="http://www.w3.org/1998/Math/MathML"> y t </math>y_{t} 不依赖于 <math xmlns="http://www.w3.org/1998/Math/MathML"> y t − 1 </math>y_{t-1} 只取决于卷积核和输入 <math xmlns="http://www.w3.org/1998/Math/MathML"> x t </math>x_{t}。
* 卷积形式可以用来训练，我们已经拥有了全部的输入token，实现并行计算；循环形式可以用来推理，对每个生成的token，它的只需要考虑之前的隐藏状态和当前的输入即可，计算量和内存占用量都是常量。

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fpicx.zhimg.com%2Fv2-b06d9e01cf50b9f255bdfe06538156d1_1440w.jpg&valid=false)

S4 的局限：

* 系统的行为由状态变量的演化和外部控制信号的影响决定。状态变量是系统的内部表示，可以捕获系统的动态特性，通过 <math xmlns="http://www.w3.org/1998/Math/MathML"> A </math>A 来控制；外部控制信号的影响通过 <math xmlns="http://www.w3.org/1998/Math/MathML"> B </math>B 来控制；系统的状态转化为最终的输出通过矩阵 <math xmlns="http://www.w3.org/1998/Math/MathML"> C </math>C 来控制。
* LTI表示SSM参数A、B和C对于所有时间步长都是固定的。无论给SSM的序列是什么，可学习的参数 <math xmlns="http://www.w3.org/1998/Math/MathML"> A , B , C </math>A,B,C 的值随着新token的传入都保持不变。这样就得到了一个不感知内容的静态表示。
* 从循环表示来看，SSM的循环表示创建了一个非常有效的小状态，它压缩了整个历史信息，并不是有效的从内容中选择关键的信息，所以与不压缩历史(注意力矩阵)的Transformer模型相比，它的功能要弱得多。
* 从卷积表示来看，全局卷积可以是感知世界，也就是说可以解决vanilla copying task的问题，但是无法解决selective copying task的问题，因为它缺乏了内容的感知。

如何感知内容呢？

就是让参数变成input-depedent，矩阵 A（HiPPO 矩阵）保持不变，但 Δ、B 和 C 现在成为输入的函数。下图展示了二者选择机制的差异。
![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fpic4.zhimg.com%2Fv2-21431e3a99c0f161529ad7e0c82eed49_1440w.jpg&valid=false)
SSM vs. Selective SSM

B: batch size; L: sequence length; D：input vector size；N：hidden state size；
![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fpic2.zhimg.com%2Fv2-32baa40958651ba7b80f6b5ff7a581d1_1440w.jpg&valid=false)
![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fpic2.zhimg.com%2Fv2-114732f0ddec6ec7ff33e0c48f2f9397_1440w.jpg&valid=false)

* 对于每个输入标记，有不同的B和C矩阵，这解决了内容感知问题，这里矩阵A保持不变，因为希望状态本身保持静态，但影响它的方式(通过B和C)是动态的。
* 也就是说它们一起选择性地选择将什么保留在隐藏状态中，什么需要忽略，这都是由输入确定的。
* 较小的步长\\Delta导致忽略特定的单词，而是更多地使用之前的上下文，而较大的步长\\Delta则更多地关注输入单词而不是上下文:

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fpic2.zhimg.com%2Fv2-30c2e946ade0bf73cd38339596e199a5_1440w.jpg&valid=false)

Mamba2的表示中， A，B，C 都是随着时间变化的：\\begin{aligned} h_t \& =A_t h_{t-1}+B_t x_t \\\\ y_t \& =C_t\^{\\top} h_t \\end{aligned}\\\\

为什么这里 A 也变成随时间变化的了？连续信号 A 是常量，但是离散化处理的步长参数 \\Delta 是时变的，也就是输入依赖的，所以由于离散化处理的原因，A 也看成是时变的。

然后我们回到Mamba2，都在selective SSM的场景下进行讨论。

**SSM 的一般形式表示**

上述SSM的公式表示都是 x \\in \\mathbb{R}\^{\\mathrm{T}} 情况，如果 x\\in (T,P) ,也就是P个channel，我们可以对每个channel独立地使用相同的SSM。对于维度 (T,P) ，其中T是序列/时间长度；P是head dimension。目前我们主要考虑single head的场景，multi-head 可以完全通过相互独立的single head 的来实现。

进一步地，SSM的一般形式表示：Y\^{(\\mathrm{T}, \\mathrm{P})}=\\operatorname{SSM}\\left(A\^{(\\mathrm{T}, \\ldots)}, B\^{(\\mathrm{T}, \\mathrm{N})}, C\^{(\\mathrm{T}, \\mathrm{N})}\\right)\\left(X\^{(\\mathrm{T}, \\mathrm{P})}\\right)\\\\其中 A 的结构会影响其参数形状

* ... = (N,N) 适用于常规（非结构化）SSM
* ... = (N) 适用于对角线 SSM
* ... = () 用于标量 SSM（即 SSD）

另外，N是state dimension；P是head dimension。

**SSM的矩阵变换（卷积形式）**

SSM表示为矩阵变换的形式：

Y=\\operatorname{SSM}(A, B, C)(X)=M X\\\\

循环形式：

\\begin{aligned} \& y_0=C_{0}\^{T}B_{0}x_{0} \\\\ \& y_1=C_{1}\^{T}A_{1}B_{0}x_{0}+C_{1}\^{T}B_{1}x_{1} \\\\ \& y_2=C_{2}\^{T}A_{2}A_{1}B_{0}x_{0}+C_{2}\^{T}A_{2}B_{1}x_{1}+C_{2}\^{T}B_{2}x_{2} \\\\ \& \\quad \\vdots \\quad \\vdots \\end{aligned}\\\\

简而言之，由 h_0=B_0x_0 ，

\\begin{aligned} h_t \& =A_t \\ldots A_1 B_0 x_0+A_t \\ldots A_2 B_1 x_1+\\cdots+A_t A_{t-1} B_{t-2} x_{t-2}+A_t B_{t-1} x_{t-1}+B_t x_t \\\\ \& =\\sum_{s=0}\^t A_{t: s}\^{\\times} B_s x_s . \\end{aligned}\\\\

则y_t=\\sum_{s=0}\^t C_t\^{\\top} A_{t: s}\^{\\times} B_s x_s\\\\

对应上面的矩阵表示，M展开为矩阵形式，即\\left\[\\begin{array}{ccccl} C_0\^{\\top} B_0 \& \& \& \& \\\\ C_1\^{\\top} A_1 B_0 \& C_1\^{\\top} B_1 \& \& \& \\\\ C_2\^{\\top} A_2 A_1 B_0 \& C_2\^{\\top} A_2 B_1 \& C_2\^{\\top} B_2 \& \& \\\\ \\vdots \& \\vdots \& \\ddots \& \\ddots \& \\\\ C_{\\mathrm{T}}\^{\\top} A_{\\mathrm{T}-1} \\ldots A_1 B_0 \& C_{\\mathrm{T}}\^{\\top} A_{\\mathrm{T}-1} \\ldots A_2 B_1 \& \\ldots \& C_{\\mathrm{T}}\^{\\top} A_{\\mathrm{T}-1} B_{\\mathrm{T}-2} \& C_{\\mathrm{T}}\^{\\top} B_{\\mathrm{T}-1} \\end{array}\\right\]\\\\这种类型的矩阵实际上有一个名字：它被称为半可分离矩阵 (**semiseparable matrix**)， 半可分离矩阵的另一种表征是它们的结构秩属性，它表示包含在下三角形部分的每个子矩阵都是低秩的。

总结而言， M 是下三角矩阵，即 i\<j 时， M_{ij}=0 ，否则M_{i j}=C_i\^{\\top} A_{i: j}\^{\\times} B_j:=C_i\^{\\top} A_i \\ldots A_{j+1} B_j\\\\
![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fpica.zhimg.com%2Fv2-fcc3db4d009945bbb491e62e3d2b2060_1440w.jpg&valid=false)
状态空间模型是半可分离矩阵变换

### The Attention Mode: Structured Attention

Transformers 的Attention机制本质上也是一个映射操作：

\\left(Q\^{(\\mathrm{T}, \\mathrm{N})}, K\^{(\\mathrm{S}, \\mathrm{N})}, V\^{(\\mathrm{S}, \\mathrm{P})}\\right) \\mapsto Y\^{(\\mathrm{T}, \\mathrm{P})}\\\\其中 P=N , 是head dimension；一般情况下，V的head dimension P可以与QK的head dimension N不相等。T是目标序列的长度，S是源序列的长度。 对应了Q length和KV length不相等的场景。通知在self-attention里 S=T 。

具体来说，Attention计算就是可以表示为：

Y=softmax(QK\^\\top)\\cdot V \\\\

当序列长度T增长并且特征维度N较小时，那么注意力成本可以从二次降低到线性。此时可以线性化注意力：Y=Q\\cdot (K\^\\top V) \\\\

**[线性注意力](https://zhida.zhihu.com/search?content_id=244828514&content_type=Article&match_order=1&q=%E7%BA%BF%E6%80%A7%E6%B3%A8%E6%84%8F%E5%8A%9B&zhida_source=entity)的因果掩码 (Causal) Linear Attention：**

对于有因果掩码，也就是causal mask的线性注意力，可以表示为如下形式：

Y=(L\\circ QK\^{T})V\\\\

其中\\circ表示element-wise 乘，L为 mask 矩阵：L=\\left\[\\begin{array}{ccc} 1 \& \& \\\\ \\vdots \& \\ddots \& \\\\ 1 \& \\ldots \& 1 \\end{array}\\right\]\\\\

对于这种掩码操作，有如下等价操作y=Q\\cdot\\operatorname{cumsum}(K\^{T}V)\\\\

**关于causal linear attention从二次到线性的证明（** Tensor Contraction Proof）**：**

使用tensor contractionor [einsum](https://link.zhihu.com/?target=https%3A//numpy.org/doc/stable/reference/generated/numpy.einsum.html) notation来表示 Y=(L\\circ QK\^{T})V ，也就是二次形式的结构化掩码矩阵：

G=contract(TN,SN\\rightarrow TS)(Q,K)\\\\M=contract(TS,TS\\rightarrow TS)(G,L)\\\\Y=contract(TS,SP\\rightarrow TP)(M,V)\\\\

我们将其重写为 four-way contraction（四阶张量缩约）：

y=contract(TN,SN,SP,TS\\rightarrow TP)(Q,K,V,L)\\\\

**\[定义\]** ：**结构化掩码矩阵（Structured masked attention, SMA)**：四阶张量缩约（four-way tensor contraction），其中使用的注意力掩码mask是一个结构化矩阵。

我们也可以通过其他的contraction顺序来得到相同的结果。我们用 V,K,L,Q 替换 Q,K,V,L ，也就是变成线性形式的结构化掩码矩阵。

Z=contract(SP,SN\\rightarrow SPN)(V,K)\\\\H=contract(TS,SPN\\rightarrow TPN)(L,Z)\\\\Y=contract(TN,TPN\\rightarrow TP)(Q,H)\\\\

也就是说，SMA有着二次和线性两种形式。

### **SSM与Attention的联系**

1. **从SSM到Attention**

回到 SSM 的 M 矩阵，当 A_t 是标量时，有M_{i j}=C_i\^{\\top} A_{i: j}\^{\\times} B_j=A_{i: j}\^{\\times} \\cdot\\left(C_i\^{\\top} B_j\\right)\\\\此时 M 矩阵可以改写为M=L \\circ C B\^{\\top} \\in \\mathbb{R}\^{(\\mathrm{T}, \\mathrm{T})}\\\\这样将一维输入映射到一维输出的序列变换 x \\in \\mathbb{R}\^{\\mathrm{T}} \\rightarrow y \\in \\mathbb{R}\^{\\mathrm{T}} 表示为 y=Mx 。用SSM形式表示就是 y=Mx=(L \\circ C B\^{\\top} )X ；用Attention形式表示就是 y=Mx=(L \\circ Q K\^{\\top} )V

这样当我们做一个转换 (C,B,X)↦(Q,K,V) ，SSM和线性注意力机制完全等价！

**2.从Attention到SSM：**

对于结构化掩码注意力，掩码矩阵为：

L=\\left\[\\begin{array}{ccccl} 1 \& \& \& \& \\\\ a_{1} \& 1 \& \& \& \\\\ a_{2}a_{1} \& a_{2} \& 1 \& \& \\\\ \\vdots \& \\vdots \& \\ddots \& \\ddots \& \\\\ a_{T-1}...a_{1} \& a_{T-1}...a_{2} \& a_{T-1} \& 1 \\end{array}\\right\]\\\\**\[定义\]** ：这种形式的矩阵为**1-SS (1-semiseparable）**半可分离矩阵 。半可分离矩阵的另一种表征是它们的结构秩属性，它表示包含在下三角形部分的每个子矩阵都是低秩的。

假设 a_{t}=1 ，L就会变成全1的下三角掩码矩阵。所以causal mask是L的特殊形式。

那么这个掩码矩阵怎么表示为SSM呢？考虑如下循环表示：

\\begin{aligned} \& y_0=x_0 \\\\ \& y_1=a_1 x_0+a_1 \\\\ \& y_2=a_2 a_1 x_0+a_2 x_1+x_2=a_2 y_1+x_2 \\\\ \& \\quad \\vdots \\quad \\vdots \\end{aligned}\\\\这个形式和SSM的循环形式表示完全一致！而这种关系可以使用矩阵形式表示y=Lx，L就是我们上面定义的掩码矩阵。

考虑一个更为简单的case方便理解：

y=\\left\[\\begin{array}{ccc} 1 \& \& \\\\ \\vdots \& \\ddots \& \\\\ 1 \& \\ldots \& 1 \\end{array}\\right\]x\\Leftrightarrow y_{0}=x_{0}; y_{t}=y_{t-1}+x_{t}\\\\

## State Space Duality（状态空间对偶）

对偶性是指状态空间方程（ A_t 是标量）和线性注意力的掩码表示本质上是同一个模型。二者之间的等价关系可以对应为：
![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fpica.zhimg.com%2Fv2-664c1cdd05355c2e20a04cb5b4775cee_1440w.jpg&valid=false)

这样我们就可以把 SSD 写成抽象的映射表示，即\\left(A\^{(T)},B\^{(\\mathrm{T}, \\mathrm{N})}, C\^{(\\mathrm{T}, \\mathrm{N})}, X\^{(\\mathrm{T}, \\mathrm{P})}\\right) \\mapsto Y\^{(\\mathrm{T}, \\mathrm{P})}\\\\ 其中T是sequence length，P是head dimension，N是state size，A是一个标量结构化矩阵。
![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fpic4.zhimg.com%2Fv2-90e226a7134a4e09f0391f56cfa73c9b_1440w.jpg&valid=false)

所以无论是结构化矩阵的mask L，还是序列转换矩阵M，本质上都是统一的。

SSD使用统一的理论将 SSM 和 Attention 联系了起来，其交集的部分即 SSD 模型，在该理论下 Linear Attention 和 [RetNet](https://zhida.zhihu.com/search?content_id=244828514&content_type=Article&match_order=1&q=RetNet&zhida_source=entity) 只是其一种特殊形式。
![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fpic4.zhimg.com%2Fv2-c8ce83bd4d36a87fdd9dc9b1b8022941_1440w.jpg&valid=false)

## Efficiency: the SSM and Attention Modes

SSD Mode在训练和推理上都实现了适配GPU的优化。推理上，状态空间模型（SSM）的递归模式非常适合高效的自回归推理；训练上，SSD相比于Attention降低了计算复杂度，可以更加高效的训练（也可以高效推理），相比于SSM，SSD实现了并行计算和矩阵运算（通过矩阵乘使得序列长度为 T 时的二次复杂度降低到线性），充分利用GPU的算力。

### SSD Algorithm：Block Matrix Decomposition

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fpicx.zhimg.com%2Fv2-310f8ede0662b98952e25dc42dbf0e2d_1440w.jpg&valid=false)

这里是通过矩阵分解的视角理解SSD。对于某个块大小 Q，我们将矩阵 M 划分为一个 T/Q × T/Q 的子矩阵网格，每个子矩阵大小为 Q×Q。比如上图T=9，将其分解为Q=3的块。注意，由半分离矩阵的定义性质，非对角块是低秩的。

1. (橙色) 每个对角块是一个小的半可分离矩阵，可以通过SSD的二次形式，也就是类似Attention的方式来计算矩阵乘；不同的块之间可以并行计算；
2. (绿色) 只有T/Q 个不同的block，大部分的block都是share的（可以看到第一列的两个block是一样的）。可以通过batched matmul来计算；
3. (黄色) 黄色部分自己形成了一个1-SS矩阵，这部分计算等同于SSM scan；
4. (蓝色) 和绿色部分类似，可以通过batched matmul来计算。

### SSD Algorithm: Chunking and State Passing

这里就是通过状态传递的视角来理解SSD。我们把序列分成size为Q的blocks/chunks，这里的chunk就会有不同的状态：

1. **Intra-chunk outputs**: 计算每个chunk的局部输出：假设初始状态是0，计算其输出状态；
2. **Chunk states**: 计算出每个chunk的最终状态；
3. **Pass states**: 通过parallel或者sequential scan等方法计算所有chunk的递归状态，也就是考虑了之前时间点所有状态的最终状态；
4. **Output states**: 对每个chunk，给定初始状态（step3 得到的），计算对从初始状态对输出的贡献。

### Code

我们来看一下最小版本的实现代码：[AI_analysis/mamba2_ssd.ipynb at main · ifromeast/AI_analysis (github.com)](https://link.zhihu.com/?target=https%3A//github.com/ifromeast/AI_analysis/blob/main/mamba2_ssd.ipynb)

**Part 0：segsum计算1-SS矩阵**

    def segsum(x):
        """More stable segment sum calculation."""
        T = x.size(-1)
        x = repeat(x, "... d -> ... d e", e=T)
        mask = torch.tril(torch.ones(T, T, device=x.device, dtype=bool), diagonal=-1)
        x = x.masked_fill(~mask, 0)
        x_segsum = torch.cumsum(x, dim=-2)
        mask = torch.tril(torch.ones(T, T, device=x.device, dtype=bool), diagonal=0)
        x_segsum = x_segsum.masked_fill(~mask, -torch.inf)
        return x_segsum

在1-SS矩阵中，每个元素是其实是累乘的：

a_{i: j}\^{\\times}=a_{i}\\times \\cdot\\cdot\\cdot \\times a_{j-1}= \\frac{a_{i: T}\^{\\times}}{a_{j: T}\^{\\times}} \\\\

这种乘积的表示形式会带来严重的数值问题，例如 a_{t}\\approx0.9，当句子长度T非常长的时候，比如0.9的上千次方，数值会很小。

* 解决方案：segsum操作

由于所有的 a_{t}\>0 ，我们可以通过log运算，把乘法转成加法操作。对于每一段 segment\[i:j\] ，都可以通过segment sum（segsum）这个primitive来实现，类似于前缀和cumsum。

我们还需要通过exp重新回到累乘的形式：

a_{i: j}\^{\\times}=exp(loga_{i}+ \\cdot\\cdot\\cdot + loga_{j-1})= ((loga)_{i:T}\^{+}-(loga)_{j:T}\^{+})\\\\

* 从unstable到stable实现：

初始unstable的实现，在cumsum部分的处理是这样的：

    x_cumsum = torch.cumsum(x, dim=-1)
    x_segsum = x_cumsum[..., :, None] - x_cumsum[..., None, :]

由于SSM对数值十分敏感，这个操作需要做减法操作，这就会引入[Catastrophic_cancellation](https://link.zhihu.com/?target=https%3A//en.wikipedia.org/wiki/Catastrophic_cancellation)问题，简单来说，两个大的数值十分接近，相对差值很小；但是他们减去同一个数后，变成小的数值了，相对差值就变大了。

所以改进成了无减法的版本：

    x = repeat(x, "... d -> ... d e", e=T)
    mask = torch.tril(torch.ones(T, T, device=x.device, dtype=bool), diagonal=-1)
    x = x.masked_fill(~mask, 0)
    x_segsum = torch.cumsum(x, dim=-2)

根据作者的介绍，这个细节非常重要，如果是unstable版本的实现，可能用fp32训练刚开始没多久就出现了nan。

**Part 1：计算intra-chunk/对角线chunk的输出（橙色块）**

就和计算 y=(L \\circ Q K\^{\\top} )V 一致，这里对应是 y=(L \\circ C B\^{\\top} )X ， L 就是1-SS矩阵，通过segsum(A)直接得到。

     # 1. Compute the output for each intra-chunk (diagonal blocks)
    L = torch.exp(segsum(A))
    Y_diag  = torch.einsum("bclhn,bcshn,bhcls,bcshp->bclhp", C, B, L, X)  ## orange

接下来的部分要结合公式理解，也就是非对角块M_{j:j',i':i} 的分解如下：M_{j:j',i':i}=\\left\[\\begin{array}{ccc} C_j\^{\\top} A_{j: i\^{\\prime}}\^{\\times} B_{i\^{\\prime}} \& \\ldots \& C_j\^{\\top} A_{j: i-1}\^{\\times} B_{i-1} \\\\ \\vdots \& \& \\vdots \\\\ C_{j\^{\\prime}-1}\^{\\top} A_{j\^{\\prime}-1: i\^{\\prime}}\^{\\times} B_{i\^{\\prime}} \& \\ldots \& C_{j\^{\\prime}-1}\^{\\top} A_{j\^{\\prime}-1: i-1}\^{\\times} B_{i-1} \\end{array}\\right\]=\\left\[\\begin{array}{c} C_j\^{\\top} A_{j: j}\^{\\times} \\\\ \\vdots \\\\ C_{j\^{\\prime}-1}\^{\\top} A_{j\^{\\prime}-1: j}\^{\\times} \\end{array}\\right\] A_{j: i-1}\^{\\times}\\left\[\\begin{array}{lll} A_{i-1: i\^{\\prime}}\^{\\times} B_{i\^{\\prime}} \& \\cdots \& A_{i-1: i-1}\^{\\times} B_{i-1} \\end{array}\\right\]\\\\其中 j'\>j\\geq i\>i'。

**Part 2: 计算intra-rank的状态矩阵（绿色块，右因子）**

这里主要关注的就是A，通过减法操作对应得到decay_states= \[A_{i-1:i\^{'}}\^{\\times} \\cdot\\cdot\\cdot A_{i-1:i-1\^{'}}\^{\\times}\]

    # 2. Compute the state for each intra-chunk
    # (right term of low-rank factorization of off-diagonal blocks; B terms)
    decay_states = torch.exp((A_cumsum[:, :, :, -1:] - A_cumsum))
    states = torch.einsum("bclhn,bhcl,bclhp->bchpn", B, decay_states, X)  ## green

**Part 3：计算inter-rank SSM递归states（黄色块，中心因子）**

decay_chunk就是黄色部分的A A_{j: i-1}\^{\\times}

    # 3. Compute the inter-chunk SSM recurrence; produces correct SSM states at chunk boundaries
    # (middle term of factorization of off-diag blocks; A terms)
    if initial_states is None:
        initial_states = torch.zeros_like(states[:, :1])
    states = torch.cat([initial_states, states], dim=1)
    decay_chunk = torch.exp(segsum(F.pad(A_cumsum[:, :, :, -1], (1, 0))))
    new_states = torch.einsum("bhzc,bchpn->bzhpn", decay_chunk, states)  ## yellow
    states, final_state = new_states[:, :-1], new_states[:, -1]

**Part 4：计算从递归states到输出（蓝色块，左因子）**

    # 4. Compute state -> output conversion per chunk
    # (left term of low-rank factorization of off-diagonal blocks; C terms)
    state_decay_out = torch.exp(A_cumsum)
    Y_off = torch.einsum('bclhn,bchpn,bhcl->bclhp', C, states, state_decay_out)

**Part5: 对角线+非对角线拼接得到最终结果**

    # Add output of intra-chunk and inter-chunk terms (diagonal and off-diagonal blocks)
    Y = rearrange(Y_diag+Y_off, "b c l h p -> b (c l) h p")

### Computation Cost

我们将符号 BMM(B, M, N, K) 定义为一个批量矩阵乘法 contract(MK, KN → MN)，其中批次（batch）维度为 B。从这个符号我们可以推断出计算的三个方面的效率：

* 计算成本：总共 O(BMNK) FLOPs。
* 内存成本：总共 O(B(MK+KN+MN)) 空间。
* 并行化：较大的 M、N、K 项可以利用现代加速器上的专门矩阵乘法单元。

**中心块**。二次 SMA 计算的成本包括三个步骤：

* 计算核矩阵 C\^{T}B，其成本为 BMM(T/Q, Q, Q, N)。
* 乘以掩码矩阵，这是一个形状为 (T/Q, Q, Q) 的张量的逐元素操作。
* 乘以X值，其成本为 BMM(T/Q, Q, P, N)。

**低秩块：右因子。**这一步是一次矩阵乘法，成本为 BMM(T/Q, N, P, Q)。

**低秩块：中心因子**。这一步是一个标量 SSM 扫描（或 1-SS 乘法），长度为 T/Q，独立通道为 (N, P)。这个扫描的工作量为 TNP/Q，与其他因素相比可以忽略不计。

需要注意的是，由于分块将序列长度从 T 减小到 T/Q，这个扫描的成本比纯 SSM 扫描（例如 Mamba 的选择扫描）小了 Q 倍。因此我们可以观察到，在大多数问题长度上，其他算法可能更有效，或者更容易实现而不会显著减慢速度。例如，通过 1-SS 矩阵乘法的朴素实现成本为 BMM(1, T/Q, NP, T/Q)，这比朴素的递归/扫描实现更容易，并且可能比其更有效。

**低秩块：左因子**。这一步是一次矩阵乘法，成本为 BMM(T/Q, Q, P, N)。

**总成本**。如果我们设置 N=P=Q（换句话说，状态维度、头维度和块长度相等），那么上述所有 BMM 项都变成了 BMM(T/N, N, N, N)。其计算特性是：

* 总 FLOP 数量为 O(TN\^{2})。
* 总内存为 O(TN)。
* 工作主要由形状为 (N,N) 的矩阵乘法组成。

**与纯SSM和Attention的比较：**
![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fpic4.zhimg.com%2Fv2-44ecdf1c4e1c10407b9a1ac20576b043_1440w.jpg&valid=false)

## Mamba2 Architecture

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fpic4.zhimg.com%2Fv2-e49a7a7870ea6f1ae36392a2cbc39f15_1440w.jpg&valid=false)

### Block Design

**并行参数投影**

Mamba-1 受 SSM 为中心的观点启发，其中选择性 SSM 层被视为从 X\\rightarrow Y的映射。SSM 参数 A, B, C 被视为附属参数，并且是 SSM 输入 X 的函数。因此，定义 (A, B, C) 的线性投影发生在创建X之后，从左侧的sequential mamba block可以看出，(A, B, C) 在在SSM之前还有一个参数投影。

在 Mamba-2 中，SSD 层被视为从 A,X,B,C\\rightarrow Y 的映射。因此，可以通过单个投影并行产生 A,X, B,C 。这类似于标准注意力架构，其中 X,B,C 对应于并行创建的 Q,K,V投影。从右侧图可以看出，只需要最开始的投影即可，SSM之前不需要额外的投影了。

带来的好处：采用并行投影以获得 SSM 的 A,B,C,X输入减少了参数，并且我们可以通过Megatron的sharding pattern实现张量并行。

**额外的归一化**

作者发现较大模型容易出现不稳定，所以通过在块的最后输出投影之前添加一个额外的归一化层（例如 LayerNorm，GroupNorm 或 RMSNorm）来缓解这一问题。

### Multihead Patterns for Sequence Transformations

这里我理解是说，SSD不仅可以表达经典transformers attention的各种形式（MHA，MQA），同时还延伸出了更多的表达（MVA）。

参数定义：

* T : sequence length
* H：head number
* D=d_{model}：model dimension/hidden dimension
* N：state size，QK head dimension
* P：head dimension，V head dimension；Mamba2中通常选则64或128

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fpic1.zhimg.com%2Fv2-77c971694e03834d279e7368f0d2f466_1440w.jpg&valid=false)

Attention分类：

1. **多头选择性状态空间模型（Multihead SSM (MHS)）/多头注意力（Multihead Attention (MHA) Pattern）**

公式（17）：head dim P 可以被模型维度 D 整除，得到head的数目 H=D/P 。

**2. 多收缩状态空间模型（MCS）（Multi-contract SSM (MCS)）/多查询注意（MQA）模式（Multi-query Attention (MQA) Pattern）**

公式（18）：MQA也可以定义为等效的SSM版本。Attention mode，H个头的 Q 共享 (K,V) 的单个头；SSM mode， C 共享 (B,X) 个头。

公式（19）：类似地，也可以定义多key注意力或多扩展SSM（MES）的模式，Attention mode，H个头的 K 共享 (V,Q) 单个头，SSM mode， B 共享 (X,C) 的单个头。

**3. 多输入 SSM（MIS）（Multi-input SSM (MIS)）/ Multi-value Attention (MVA) Pattern（多值注意（MVA）模式）**

公式（20）：SSM的自然选择， X 视为SSM的主要输入，所以需要多个头，有 H个， B 和 C 视为跨输入通道共享的参数，只有一个头。

4. 此外，Mama-2 也可以扩展到GQA的形式，也就是分组查询注意力，在SSM模式中称为分组输入SSM（grouped-input SSM (GIS)），或者分组值注意（grouped-value attention (GVA)）。

从Attention的角度重新看Mamba：

* 头维度 P=1：每个通道都有独立的 SSM 动态 A 。
* 多输入 SSM（MIS）或多值注意（MVA）头结构： B,C 矩阵（对应于注意力对偶的 K,Q ）在输入 X 的所有通道之间共享（对应于注意力中的 V）。

## System and Scaling Optimizations

### Tensor Parallel（张量并行）

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fpic1.zhimg.com%2Fv2-ac210ee8dc9a2a13156fae1b78abff94_1440w.jpg&valid=false)
Mamba和Mamba-2的张量并行

**Mamba：2次allreduce**

假设我们想要沿着 2 个 GPU 分割计算。将输入投影矩阵 W\^{(x)} W\^{(z)} 分割成两个大小为 d\\times ed/2 的分区，然后每个 GPU 将持有 x_{c} 大小的一半： L\\times ed/2。然而，我们注意到由于 \\Delta, B,C 是关于x_{c}的函数，所以在计算 \\Delta, B,C 之前，我们需要在 GPU 之间进行额外的 all-reduce，以获取完整的x_{c}。之后，两个 GPU 可以并行计算 SSM，因为它们在d上 是独立的。最后，我们可以将输出投影矩阵 W\^{(o)}分割成两个大小为 ed/2\\times d 的分区，并在最后进行 all-reduce。
![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fpic1.zhimg.com%2Fv2-84db9a7541cb47be9c8faf83d8d4a9dc_1440w.jpg&valid=false)

Mamba-2：1次allreduce

通过投影直接从 u 获取\\Delta, B,C，而不是从 x_{c} 获取，我们只需要对投影矩阵进行切分。这意味着在不同的 GPU 上有不同的\\Delta, B,C集合，这相当于在更大的 "逻辑 GPU" 上有几个group的\\Delta, B,C。此外，在每个块内使用 GroupNorm，组数可被 TP degree整除，以便 TP 组内的 GPU 在块内不进行通信。这样只需要在块结束时候进行一次allreduce即可。
![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fpica.zhimg.com%2Fv2-773ea4997aa58da4532aa81b4325f392_1440w.jpg&valid=false)

### Sequence Parallel（序列并行）

序列并行是沿着序列长度把输入和激活分配到不同的GPU上计算，主要有两种技术：

* 序列并行（Sequence parallelism，SP）用于残差和归一化操作：使用的方法是Korthikanti et al等人提出并且在Megtron-LM中已经支持的方法：将 TP 中的 all-reduce 分解为 reduce-scatter 和 all-gather。注意在同一 TP 组中所有 GPU上，残差和归一化操作在在相同输入上重复执行；SP 沿着序列长度维度切分激活值，主要执行流程是：reduce-scatter，残差和归一化，然后 all-gather。Mamba-2 架构使用相同的残差和归一化结构，因此 SP 直接使用该方法无需修改。
* 序列并行/上下文并行（context parallelism，CP）：用于token-mixing操作（注意力或 SSM））。目前主流的技术例如Ring-attention等。该类方法将查询和键分割成块，但每个查询块都需要与键块交互，导致通信带宽与worker数量的平方成正比。对于 SSM，可以一种简单的方式分割序列：每个worker获取一个初始状态，根据其输入计算 SSM，返回最终状态，并将该最终状态传递给下一个工作人员。这样通信带宽与worker数量成线性关系。这种分解与 SSD 算法中的块分解完全相同，将其分割成块/块（blocks / chunks）。如下图所示：

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fpic4.zhimg.com%2Fv2-843bbeb822502c85eb64504d5e847d99_1440w.jpg&valid=false)
Mamba-2序列并行

### Variable Length（可变长度）

预训练通常对批处理使用相同的序列长度，但在微调或推断过程中，模型可能需要处理不同长度的不同输入序列。最简单的处理方式是将批次中的所有序列右填充到最大长度，但如果序列长度差异很大，效率会比较差。对于 Transformer，已经有一系列技术避免填充并保证GPU 之间负载平衡，或者可以将多个序列pack到同一batch中，此时需要注意调整注意力掩码。

对于 SSMs，特别是 Mamba，文章通过将整个batch视为一个长序列来处理可变序列长度，并避免在各个序列之间传递状态。这相当于把一个序列终止处的token t 简单地设置 A_{t}=0，从而不将信息传递给属于另一个序列的token t+1。

## References:

[Transformers are SSMs: Generalized Models and Efficient Algorithms Through Structured State Space Duality](https://link.zhihu.com/?target=https%3A//arxiv.org/pdf/2405.21060)

[state-spaces/mamba: Mamba SSM architecture (github.com)](https://link.zhihu.com/?target=https%3A//github.com/state-spaces/mamba)

[State Space Duality (Mamba-2) Part I - The Model \| Goomba Lab](https://link.zhihu.com/?target=https%3A//goombalab.github.io/blog/2024/mamba2-part1-model/%23the-mamba-2-architecture)

[State Space Duality (Mamba-2) Part II - The Theory \| Goomba Lab](https://link.zhihu.com/?target=https%3A//goombalab.github.io/blog/2024/mamba2-part2-theory/%23going-beyond-the-ssd-layer-2)

[State Space Duality (Mamba-2) Part III - The Algorithm \| Goomba Lab](https://link.zhihu.com/?target=https%3A//goombalab.github.io/blog/2024/mamba2-part3-algorithm/)

[State Space Duality (Mamba-2) Part IV - The Systems \| Goomba Lab](https://link.zhihu.com/?target=https%3A//goombalab.github.io/blog/2024/mamba2-part4-systems/)

[Mamba: The Easy Way (jackcook.com)](https://link.zhihu.com/?target=https%3A//jackcook.com/2024/02/23/mamba.html)

[Mamba: The Hard Way (srush.github.io)](https://link.zhihu.com/?target=https%3A//srush.github.io/annotated-mamba/hard.html)

[https://newsletter.maartengrootendorst.com/p/a-visual-guide-to-mamba-and-state](https://link.zhihu.com/?target=https%3A//newsletter.maartengrootendorst.com/p/a-visual-guide-to-mamba-and-state)

[Megatron-LM/examples/mamba at ssm · NVIDIA/Megatron-LM (github.com)](https://link.zhihu.com/?target=https%3A//github.com/NVIDIA/Megatron-LM/tree/ssm/examples/mamba)

[An Empirical Study of Mamba-based Language Models](https://link.zhihu.com/?target=https%3A//arxiv.org/pdf/2406.07887)

[LLM（廿五）：从控制系统到语言模型 ------ Mamba 的前世今生 - 知乎 (zhihu.com)](https://zhuanlan.zhihu.com/p/680833040?)

[LLM（ 廿八）：解读 Mamba 2，兼谈 LLM 的统一理论 - 知乎 (zhihu.com)](https://zhuanlan.zhihu.com/p/701860743)

[Read in Cubox](https://cubox.pro/web/card/7339910235936523629)
