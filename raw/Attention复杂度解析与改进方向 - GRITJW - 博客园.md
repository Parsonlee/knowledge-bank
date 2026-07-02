---
id: "7370784196572219988"
cubox_url: https://cubox.pro/web/card/7370784196572219988
url: https://www.cnblogs.com/GlenTt/p/19109565
tags:
  - DeepLearning

---
# Attention复杂度解析与改进方向 - GRITJW - 博客园

Attention复杂度解析与改进方向 摘要/引言 在大规模语言模型（LLM）浪潮中，扩展模型上下文窗口长度被认为是提升模型能力和应用范围的关键方向。然而，现代Transformer结构中的自注意力机制，其时间和空间复杂度均为二次方级（\(O(N^2)\)），成为限制序列长度扩展的根本瓶颈。有研究指

[Read in Cubox](https://cubox.pro/web/card/7370784196572219988)  
[Read Original](https://www.cnblogs.com/GlenTt/p/19109565)  

---


---

\## 📖 正文全文

# Attention复杂度解析与改进方向

[www.cnblogs.com](https://www.cnblogs.com/GlenTt/p/19109565)GRITJW 粉丝 - 4 关注 - 0

\## 摘要/引言

在大规模语言模型（LLM）浪潮中，扩展模型上下文窗口长度被认为是提升模型能力和应用范围的关键方向。然而，现代Transformer结构中的自注意力机制，其时间和空间复杂度均为二次方级（ <math xmlns="http://www.w3.org/1998/Math/MathML"> O ( N 2 ) </math>），成为限制序列长度扩展的根本瓶颈。有研究指出，注意力机制对序列长度的时间和空间复杂度均为二次方，导致计算量和内存需求随序列长度迅速增长，尤其在处理长文本时表现出显著的性能瓶颈。此外，由于GPU计算速度远超内存带宽，注意力计算往往受到高带宽显存（HBM）访问的限制。本文将从理论层面系统分析标准自注意力的时间和空间复杂度来源，探讨其内存I/O瓶颈，并重点介绍以FlashAttention为代表的I/O感知（I/O-aware）优化技术如何通过重构计算流程突破瓶颈。最后，我们还简要介绍其他高效注意力机制（如Hyena、线性注意力、S2-Attention）的基本思想，为读者提供全面视角。

\## 标准自注意力机制的复杂度瓶颈

Transformer中的自注意力核心计算公式为：


<math display="block" xmlns="http://www.w3.org/1998/Math/MathML"> A t t e n t i o n ( Q , K , V ) = s o f t m a x ( Q K T d k ) V , </math>

其中输入序列长度为 <math xmlns="http://www.w3.org/1998/Math/MathML"> N </math>，每个词元的表示维度为 <math xmlns="http://www.w3.org/1998/Math/MathML"> d </math>， <math xmlns="http://www.w3.org/1998/Math/MathML"> Q , K , V </math> 是通过线性变换得到的查询、键、值矩阵。

1. **时间复杂度 ( <math xmlns="http://www.w3.org/1998/Math/MathML"> O ( N 2 ⋅ d ) </math>)**   
   时间复杂度主要由乘加运算（浮点运算次数)（FLOPs）数量决定，可分解为四个主要步骤：

   * **Q,K,V生成** ：输入矩阵 <math xmlns="http://www.w3.org/1998/Math/MathML"> X ∈ R N × d </math> 与三个权重矩阵相乘得到 <math xmlns="http://www.w3.org/1998/Math/MathML"> Q , K , V </math>，总体复杂度为 <math xmlns="http://www.w3.org/1998/Math/MathML"> O ( N d 2 ) </math>（每个 <math xmlns="http://www.w3.org/1998/Math/MathML"> Q , K , V </math> 各一次共 <math xmlns="http://www.w3.org/1998/Math/MathML"> 3 N d 2 </math>）。
   * **注意力得分计算** ：计算 <math xmlns="http://www.w3.org/1998/Math/MathML"> S = Q K T </math>，这是大小为 <math xmlns="http://www.w3.org/1998/Math/MathML"> N × d </math> 的 <math xmlns="http://www.w3.org/1998/Math/MathML"> Q </math> 与 <math xmlns="http://www.w3.org/1998/Math/MathML"> d × N </math> 的 <math xmlns="http://www.w3.org/1998/Math/MathML"> K </math> 矩阵乘法，结果为 <math xmlns="http://www.w3.org/1998/Math/MathML"> N × N </math> 的得分矩阵，计算量为 <math xmlns="http://www.w3.org/1998/Math/MathML"> O ( N 2 d ) </math>，是时间复杂度的主导项。
   * **Softmax归一化** ：对 <math xmlns="http://www.w3.org/1998/Math/MathML"> N × N </math> 的得分矩阵 <math xmlns="http://www.w3.org/1998/Math/MathML"> S </math> 按行执行 Softmax，每行需要遍历 <math xmlns="http://www.w3.org/1998/Math/MathML"> N </math> 个元素并归一化，共 <math xmlns="http://www.w3.org/1998/Math/MathML"> N </math> 行，总复杂度 <math xmlns="http://www.w3.org/1998/Math/MathML"> O ( N 2 ) </math>。
   * **加权求和** ：将归一化后的注意力矩阵 <math xmlns="http://www.w3.org/1998/Math/MathML"> P </math>（ <math xmlns="http://www.w3.org/1998/Math/MathML"> N × N </math>）与 <math xmlns="http://www.w3.org/1998/Math/MathML"> V </math>（ <math xmlns="http://www.w3.org/1998/Math/MathML"> N × d </math>）相乘，得到输出矩阵，复杂度为 <math xmlns="http://www.w3.org/1998/Math/MathML"> O ( N 2 d ) </math>。

   综合来看，高阶项为 <math xmlns="http://www.w3.org/1998/Math/MathML"> O ( N 2 d ) </math>。当序列长度 <math xmlns="http://www.w3.org/1998/Math/MathML"> N </math> 远大于表示维度 <math xmlns="http://www.w3.org/1998/Math/MathML"> d </math> 时（LLM 中常见情形）， <math xmlns="http://www.w3.org/1998/Math/MathML"> N 2 </math> 项主导了计算量，计算负载随 <math xmlns="http://www.w3.org/1998/Math/MathML"> N </math> 二次增长。正如文献所述，自注意力的二次复杂度是其性能瓶颈的根源。
2. **空间复杂度 ( <math xmlns="http://www.w3.org/1998/Math/MathML"> O ( N 2 ) </math>)**   
   空间复杂度主要由计算中需要存储的中间矩阵大小决定。在前向传播时，必须显式生成大小为 <math xmlns="http://www.w3.org/1998/Math/MathML"> N × N </math> 的注意力得分矩阵 <math xmlns="http://www.w3.org/1998/Math/MathML"> S </math> 和 Softmax 输出矩阵 <math xmlns="http://www.w3.org/1998/Math/MathML"> P </math>。在反向传播时，为计算梯度需要复用这些中间结果，因此 <math xmlns="http://www.w3.org/1998/Math/MathML"> S </math> 或 <math xmlns="http://www.w3.org/1998/Math/MathML"> P </math> 必须持续保留在显存中直到梯度计算结束。这意味着注意力机制至少需要额外 <math xmlns="http://www.w3.org/1998/Math/MathML"> O ( N 2 ) </math> 的内存存储量。比如，若 <math xmlns="http://www.w3.org/1998/Math/MathML"> N = 65536 </math>，则一个 <math xmlns="http://www.w3.org/1998/Math/MathML"> 65536 × 65536 </math> 的半精度（FP16）矩阵就占用超过 8GB 显存（ <math xmlns="http://www.w3.org/1998/Math/MathML"> 65536 2 × 2 </math> 字节），这对于主流GPU显存来说是难以承受的。因此，随着序列长度的增加，Attention的内存需求也会呈二次方增长。

3. **真正的性能瓶颈：内存I/O**   
   随着硬件的发展，GPU上的计算单元（ALU）性能提升迅速，但内存带宽的增长相对滞后。Attention操作计算密集但同时极度依赖对大矩阵的读写。标准实现中，注意力计算依次执行：

   * 将 <math xmlns="http://www.w3.org/1998/Math/MathML"> Q K T </math> 计算结果 <math xmlns="http://www.w3.org/1998/Math/MathML"> S </math>（ <math xmlns="http://www.w3.org/1998/Math/MathML"> N × N </math>）写入全局显存（HBM）；
   * 读取整个 <math xmlns="http://www.w3.org/1998/Math/MathML"> S </math> 矩阵计算 Softmax 后的 <math xmlns="http://www.w3.org/1998/Math/MathML"> P </math>（ <math xmlns="http://www.w3.org/1998/Math/MathML"> N × N </math>），并将 <math xmlns="http://www.w3.org/1998/Math/MathML"> P </math> 写回 HBM；
   * 最后读取 <math xmlns="http://www.w3.org/1998/Math/MathML"> P </math> 和 <math xmlns="http://www.w3.org/1998/Math/MathML"> V </math> 进行加权求和。

   这一系列大规模的"写入-读出"往返操作使得GPU计算核心常常空闲等待数据传输，导致算力利用率低下。简言之，注意力计算往往受限于内存带宽，而非原始算力。正因为如此，许多工作强调Attention的核心瓶颈是 内存I/O 而非纯计算量。

\## 破局者：FlashAttention 的 I/O 感知优化

FlashAttention 由 Tri Dao 等人在2022年提出，其核心理念是通过算法重组与硬件协同设计，最大限度减少全局显存访问，从而解放GPU计算资源，实现Attention加速。FlashAttention 主要技术要点包括：

* **核融合（Kernel Fusion）与避免显存物化** ：FlashAttention 将Attention前向和后向的所有操作融合到一个 CUDA Kernel 中，目标是不在全局显存中显式生成大小为 <math xmlns="http://www.w3.org/1998/Math/MathML"> N × N </math> 的中间矩阵。所有计算在片上高速缓存（SRAM）中完成，最终只将输出矩阵（ <math xmlns="http://www.w3.org/1998/Math/MathML"> N × d </math>）写回全局内存。Tri Dao等人总结道，FlashAttention 通过分块（tiling）和重计算，将注意力的空间复杂度从二次方降至线性，使得中间矩阵无需物化；由于不往慢速显存读写 <math xmlns="http://www.w3.org/1998/Math/MathML"> N × N </math> 矩阵，内存访问量大幅降低，整体计算速度提升了2--4倍。

* **分块计算（Tiling）** ：FlashAttention 将输入 <math xmlns="http://www.w3.org/1998/Math/MathML"> Q , K , V </math> 按序列长度 <math xmlns="http://www.w3.org/1998/Math/MathML"> N </math> 分块。算法在外层循环中依次加载 <math xmlns="http://www.w3.org/1998/Math/MathML"> K , V </math> 的一个块到SRAM，在内层循环中加载对应的 <math xmlns="http://www.w3.org/1998/Math/MathML"> Q </math> 块。对每对块执行矩阵乘积和Softmax操作并立即累加结果。这种"分块"策略保证同时在SRAM中只存在小块数据，避免生成完整的 <math xmlns="http://www.w3.org/1998/Math/MathML"> ( N , N ) </math> 矩阵。如资料所述："FlashAttention 通过切分输入为更小的块并逐步计算注意力，从而减少在相对较慢的GPU全局内存中生成大注意力矩阵的需求；同时利用片上缓存减少不同层级内存间的数据读写。"

* **在线Softmax（Online Softmax）** ：分块计算带来一个挑战：标准Softmax需要对整行进行归一化。FlashAttention 利用一种在线归一化算法，在处理每个 <math xmlns="http://www.w3.org/1998/Math/MathML"> K </math> 块时维护当前行的最大值和归一化累积值。在加载下一个块时，根据新的最大值和累积和实时更新归一化因子，从而无需访问完整的得分行即能得到正确的Softmax结果。也就是说，Softmax 操作被拆解并融合在分块流程中，同样无需将整个矩阵写入显存。

上述技术的综合效果是：前向和反向过程在片上缓存内完成中间计算，仅将最终输出写回全局内存，使Attention从内存密集型转为计算密集型，从而充分发挥现代GPU的计算潜力。FlashAttention 的原始论文和实现表明，此策略无需任何近似，在保持精度的前提下可获得数倍加速。

\## 持续进化：从 FlashAttention-1 到 FlashAttention-3

\#\## FlashAttention-1 的成就与局限

FlashAttention-1验证了I/O感知设计的巨大潜力，实现了在多个基准任务上对比传统实现的显著加速。然而，其对新硬件特性的利用还不充分。例如，Tri Dao等人指出，FlashAttention-2 在NVIDIA Hopper架构（如H100）上仅能达到大约35%的理论峰值TFLOPs利用率，意味着GPU资源仍有大量空闲可挖掘。

\#\## FlashAttention-2 的优化

针对这些不足，研究团队在FlashAttention-2中进行了深度工程优化。通过更合理的线程块布局和工作划分，充分利用多头注意力中的并行性，以及更均衡地安排矩阵乘法和非乘法操作，提高了硬件利用率。例如，通过调整算法以在序列维度进行分片，并降低线程间同步开销，FlashAttention-2在A100（Ampere）GPU上FP16前向可以达到约70%的理论性能，而在H100（Hopper）GPU上将同样计算的吞吐率从原来的350 TFLOPs提升到了约540--570 TFLOPs。这些优化使得FlashAttention-2在保持精度的同时，比初代实现快近一倍，接近硬件性能极限。

\#\## FlashAttention-3 的突破

2024年，Tri Dao 等人进一步提出 FlashAttention-3，将计算重心推向硬件新特性和异步执行。FlashAttention-3 利用Hopper GPU的Warpgroup矩阵乘加（WGMMA）、张量内存加速器（TMA）和低精度FP8指令，通过以下技术实现性能飞跃：

* **异步重叠（Asynchrony）**：FlashAttention-3 在Warp粒度上并行计算矩阵乘法（GEMM）与Softmax。具体而言，采用"乒乓调度"（Ping-Pong Scheduling）和Warp组内流水线，在一个Warp组执行GEMM时，另一个Warp组执行Softmax。这样，当Tensor核忙于矩阵运算时，多功能单元可以并行计算指数函数，大幅减少了特殊函数（如指数）的低吞吐成为瓶颈的影响。实测显示，此策略将FP16前向计算吞吐从约570 TFLOPs提升至620 TFLOPs，再通过Warp组内流水线提升到640--660 TFLOPs。

* **FP8低精度**：Hopper架构支持FP8数值格式，能将Tensor核吞吐提升到接近2倍（H100上FP8峰值1978 TFLOPs vs FP16的989 TFLOPs）。FlashAttention-3在低精度下采用"非相干处理"（incoherent processing）技术，即对查询和键乘以随机正交矩阵以抑制异常值，从而显著降低量化误差。结合FP8计算，FlashAttention-3实现了最高接近1.2 PFLOPs的峰值吞吐，同时相比直接量化的FP8注意力，误差降低了2.6倍。

综合异步执行和低精度优化，FlashAttention-3在H100上用FP16精度相比前代实现达到了1.5--2.0倍的加速（性能高达740 TFLOPs，占H100理论峰值的75%）。对于LLM训练和推理，这意味着可以高效使用更长的上下文（数十万乃至百万级令牌），而无需额外的近似或精度损失。FlashAttention-3的开源实现和相应论文已经正式发布，进一步巩固了该系列在工业界处理长上下文的核心地位。

\## 其他高效注意力机制简介

除了FlashAttention系列，多种方法也在探索突破注意力复杂度的途径：

* **Hyena层（Hyena Hierarchy）** ：由 Hazy Research 提出的 Hyena 层是一种基于长卷积的注意力替代方案，具有子二次时间复杂度。Hyena通过隐式的长卷积核来捕捉全局依赖，不显式构造 <math xmlns="http://www.w3.org/1998/Math/MathML"> N × N </math> 矩阵。文献指出，Hyena实现了与注意力同等质量的建模能力，在超长序列上表现尤为突出：在序列长度达到10万时，Hyena的速度是高度优化的FlashAttention的100倍；而在较短序列（如4K）下，它的速度略慢于闪存注意力。这表明Hyena在极端长上下文任务中具有潜力，但其效果依赖于卷积滤波参数化等设计。

* **线性注意力（Linear Attention）** ：此类方法通过近似Softmax或设计核函数，使得注意力计算复杂度降为线性。典型代表如 Performer（Choromanski et al., 2020）使用随机特征（Random Fourier Features）将Softmax内核线性化，将时间和空间复杂度从 <math xmlns="http://www.w3.org/1998/Math/MathML"> O ( N 2 ) </math> 降为 <math xmlns="http://www.w3.org/1998/Math/MathML"> O ( N ) </math>。换言之，随机特征方法（RFA）能以线性时间近似原始注意力，但通常以一定偏差为代价。相关研究提出了改进方案（如线性随机注意力LARA等），以在效率和精度间取得平衡。这类方法无须存储完整的注意力矩阵，但在精度和可扩展性上需要仔细设计。

* **S2-Attention**：这是一种"硬件感知的上下文分片"技术，旨在加速稀疏注意力计算。S2-Attention库允许为每个注意头和上下文范围自定义稀疏模式，并在低级别实现专门优化。在这种方案中，不同头只关注全局上下文的不同子集（通过跨头分片），同时采用混合稠密/稀疏策略来兼顾效率与性能。最新工作表明，S2-Attention在长上下文（如128K长度）场景下相对于FlashAttention-2实现了多倍加速------报告指出其在128K长度下比FlashAttention-2快8.79倍、15.87倍乃至25.3倍；在7B参数模型的推理中也可达到约4.5倍的速度提升。重要的是，这些稀疏策略在保持近似全注意力性能的同时，通过上下文分片和并行化显著减少了内存I/O瓶颈。

上述方法各有侧重：Hyena通过结构化卷积达到亚二次复杂度，线性注意力通过核近似线性化注意力矩阵，而S2-Attention等稀疏技术通过分片和专用内核减少IO成本。它们与FlashAttention属于不同思路：FlashAttention着眼于完全保留原始注意力结果的前提下优化IO，而其他方法则通过近似、稀疏或替代机制降低理论复杂度。

\## 总结

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fimg2024.cnblogs.com%2Fblog%2F3670197%2F202509%2F3670197-20250924175645219-246188031.png&valid=false)

传统自注意力机制的二次复杂度不仅意味着计算量的爆炸增长，更带来了对显存带宽的极大挑战。在长序列条件下，这种"计算-内存齐头并进"的增长使得标准注意力成为效率瓶颈。FlashAttention系列技术提供了一个优雅的解决方案：它们并不改变模型结构或近似注意力矩阵，而是通过算法与硬件的协同设计------采用分块计算、内存复用和Kernel融合等策略------彻底消除了中间 <math xmlns="http://www.w3.org/1998/Math/MathML"> N × N </math> 矩阵的全局写入和读取。这样，注意力计算从内存密集型转变为计算密集型，显著提升了GPU利用率。最新的FlashAttention-3进一步利用Hopper GPU的新指令和异步调度，将实际性能利用率推至75%以上。这些进步已成为长上下文LLM训练和推理的行业标准，推动了上下文长度从最初的2-4K一路提升到数十万甚至百万级别。

[Read in Cubox](https://cubox.pro/web/card/7370784196572219988)
