---
id: "7131285711155627032"
cubox_url: https://cubox.pro/web/card/7131285711155627032
url: https://mp.weixin.qq.com/s/UtNLpJc0SlIowuHGbJ8SRg
tags:
  - LLM
---
# 矩阵模拟！Transformer大模型3D可视化，GPT-3、Nano-GPT每一层清晰可见



[Read in Cubox](https://cubox.pro/web/card/7131285711155627032)  
[Read Original](https://mp.weixin.qq.com/s/UtNLpJc0SlIowuHGbJ8SRg)  

---


---

\## 📖 正文全文

# 矩阵模拟！Transformer大模型3D可视化，GPT-3、Nano-GPT每一层清晰可见

[mp.weixin.qq.com](https://mp.weixin.qq.com/s/UtNLpJc0SlIowuHGbJ8SRg)新智元 新智元

\#\## ![图片](https://image.cubox.pro/cardImg/2023120418464533825/52737.jpg?imageMogr2/quality/90/ignore-error/1)

\#\## *** ** * ** ***
**新智元报道**


编辑：桃子 好困

\#\#\#\## **【新智元导读】** Transformer大模型工作原理究竟是什么样的？一位软件工程师打开了大模型的矩阵世界。


黑客帝国中，「矩阵模拟」的世界或许真的存在。  

![图片](https://image.cubox.pro/cardImg/2023120418464539500/35775.jpg?imageMogr2/quality/90/ignore-error/1)

模拟人类神经元，不断进化的Transformer模型，一直以来都深不可测。

许多科学家都试着打开这个黑盒，看看究竟是如何工作的。

而现在，大模型的矩阵世界，真的被打开了！

一位软件工程师Brendan Bycroft制作了一个「大模型工作原理3D可视化」网站霸榜HN，效果非常震撼，让你秒懂LLM工作原理。

![图片](https://image.cubox.pro/cardImg/2023120418464599501/21855.jpg?imageMogr2/quality/90/ignore-error/1)

1750亿参数的GPT-3，模型层足足有8列，密密麻麻没遍布了整个屏幕。

![图片](https://image.cubox.pro/cardImg/2023120418464580372/91614.jpg?imageMogr2/quality/90/ignore-error/1)

GPT-2模型不同参数版本的架构可视化，差异巨大。如下是有150亿参数GPT-2（XL），以及有1.24亿参数GPT-2（Small）。

![图片](https://image.cubox.pro/cardImg/2023120418464697817/22540.jpg?imageMogr2/quality/90/ignore-error/1)

![图片](https://image.cubox.pro/cardImg/2023120418464616867/82751.jpg?imageMogr2/quality/90/ignore-error/1)

这个3D模型可视化还展示了，大模型生成内容的每一步。

这里，Bycroft主要分解了OpenAI科学家Andrej Karpathy打造的轻量级的GPT模型------NanoGPT，参数量为85000。

![图片](https://image.cubox.pro/cardImg/2023120418464765608/72409.jpg?imageMogr2/quality/90/ignore-error/1)

地址：https://bbycroft.net/llm

看过这个可视化图，你就可以了解ChatGPT的大脑。

![图片](https://image.cubox.pro/cardImg/2023120418464798352/90398.jpg?imageMogr2/quality/90/ignore-error/1)

从GPT-2（Small）到GPT-3的参数规模的跨越，让人叹为观止。

![图片](https://image.cubox.pro/cardImg/2023120418464763905/11501.jpg?imageMogr2/quality/90/ignore-error/1)

Bycroft称，这个指南侧重于模型的推理，而非训练，只是机器学习中的一小部分。在具体例子中，模型的权重已经预训练完成，使用推理过程来生成输出。

当然了，这个可视化网站也是收到了Karpathy在PyTorch中创建的minGPT，以及YouTube视频系列「Neural Networks: Zero to Hero」的启发。

接下来，一起深入来了解，Transformer模型每一层。

介绍

为了方便进行演示，Brendan Bycroft给NanoGPT布置了一个非常简单的任务：
> 获取一个由六个字母组成的序列：C B A B B C，并按字母顺序排序，即「ABBBCC」。

![图片](https://image.cubox.pro/cardImg/2023120418464835784/95012.jpg?imageMogr2/quality/90/ignore-error/1)

我们将每一个字母称为token，模型的不同token集合构成了它的词汇表：

![图片](https://image.cubox.pro/cardImg/2023120418464875874/88272.jpg?imageMogr2/quality/90/ignore-error/1)

这个表中，每个token都被分配了一个数字，它是token index。现在我们可以将这一系列数字输入到模型中：「2 1 0 1 1 2」

![图片](https://image.cubox.pro/cardImg/2023120418464878566/90464.jpg?imageMogr2/quality/90/ignore-error/1)

在3D视图中，每个绿色单元格表示一个正在处理的数字，每个蓝色单元格表示权重。

![图片](https://image.cubox.pro/cardImg/2023120418464848126/57796.jpg?imageMogr2/quality/90/ignore-error/1)

序列中的每个数字首先被转换为一个48元素向量，这就是所谓的「嵌入」（embedding）。

![图片](https://image.cubox.pro/cardImg/2023120418464931808/15558.jpg?imageMogr2/quality/90/ignore-error/1)

然后，「嵌入」被输入模型，传递通过一系列Transformer层，最后到达底层。

![图片](https://image.cubox.pro/cardImg/2023120418464978288/90008.jpg?imageMogr2/quality/90/ignore-error/1)

那么输出是什么呢？

对序列中下一个token的预测。因此，在序列中第6个token处，得到了下一个token将是「A」、「B」或「C」的概率。

在这种情况下，模型非常确定会是「A」。

现在，我们可以将这一预测反馈到模型的顶层，并重复整个过程。

嵌入

我们之前看到过，如何使用一个简单的查找表（lookup table）将token映射为一串整数。

这些整数，即标记token index，是我们在模型中第一次，也是唯一一次看到的整数。从这里开始，我们将使用浮点数（十进制数）进行运算。

以第4个token（index 3）为例，看看是如何被用来生成输入嵌入的第4列向量的。

![图片](https://image.cubox.pro/cardImg/2023120418464959533/50539.jpg?imageMogr2/quality/90/ignore-error/1)

我们使用token index（在本例中为B = 1）来选择左侧token嵌入矩阵的第二列。请注意，我们在这里使用的是从0开始的index，因此第一列位于index 0处。

这将产生一个大小为C=48的列向量，我们将其描述为「token嵌入」（token embedding）。

![图片](https://image.cubox.pro/cardImg/2023120418465011539/41033.jpg?imageMogr2/quality/90/ignore-error/1)

由于我们主要查看的是位于第4个位置的 （t = 3） token B，因此我们将采用「位置嵌入矩阵」的第4列。

这也会产生一个大小为C=48的列向量，我们将其描述为位置嵌入（position embedding）。

![图片](https://image.cubox.pro/cardImg/2023120418465088833/67279.jpg?imageMogr2/quality/90/ignore-error/1)

请注意，这两个位置和token嵌入都是在训练期间学习的（由蓝色表示）。

现在我们有了这两个列向量，我们只需将它们相加即可生成另一个大小为C=48的列向量。

![图片](https://image.cubox.pro/cardImg/2023120418465040410/72317.jpg?imageMogr2/quality/90/ignore-error/1)

现在，我们对输入序列中的所有token运行相同的过程，创建一组包含token值及其位置的向量。

![图片](https://image.cubox.pro/cardImg/2023120418465063351/83604.jpg?imageMogr2/quality/90/ignore-error/1)

（随意停在输入嵌入矩阵上的单个单元格上，可以查看计算及其来源。）

我们看到，对输入序列中的所有token运行此过程，会产生一个大小为TxC的矩阵。

T代表时间，也就是说，你可以将序列中稍后的token看作是时间上稍后的token。C代表通道（channel），但也称为「特征」或「维度」或「嵌入大小」。

这个矩阵，我们称之为「输入嵌入」（input embedding），并通过模型向下传递。

在本指南中，我们将看到由T列（每列长度为 C）组成的矩阵集合。

![图片](https://image.cubox.pro/cardImg/2023120418465150194/69196.jpg?imageMogr2/quality/90/ignore-error/1)

Layer Norm

上一节的「输入嵌入」矩阵是第一个Transformer模块的输入。

Transformer模块的第一步是对该矩阵进行「层归一化」（Layer Norm）处理。这是对矩阵每列的值分别进行归一化的操作。

![图片](https://image.cubox.pro/cardImg/2023120418465168350/26145.jpg?imageMogr2/quality/90/ignore-error/1)

归一化是深度神经网络训练中的一个重要步骤，它有助于提高模型在训练过程中的稳定性。

我们可以分别看待每一列，所以现在先关注第4列（t=3）。

![图片](https://image.cubox.pro/cardImg/2023120418465174342/73883.jpg?imageMogr2/quality/90/ignore-error/1)

我们的目标是使该列的平均值等于0，标准偏差等于1。为此，我们要找出该列的这两个量（平均值 (μ) 和标准偏差 (σ)），然后减去平均值，再除以标准偏差。

![图片](https://image.cubox.pro/cardImg/2023120418465152456/31496.jpg?imageMogr2/quality/90/ignore-error/1)

这里我们使用E\[x\]表示平均值，Var\[x\]表示方差（长度为C的列）。方差就是标准差的平方。ε项

![图片](https://image.cubox.pro/cardImg/2023120418465240404/17888.jpg?imageMogr2/quality/90/ignore-error/1)

是为了防止除以零。

我们在聚合层中计算并存储这些值，因为我们要将它们应用于列中的所有值。

最后，在得到归一化值后，我们将列中的每个元素乘以学习权重 (γ)，然后加上偏置 (β)，最终得到归一化值。

![图片](https://image.cubox.pro/cardImg/2023120418465217267/75348.jpg?imageMogr2/quality/90/ignore-error/1)

我们在「输入嵌入」矩阵的每一列上执行这一归一化操作，得到的结果就是归一化后的「输入嵌入」，并将其传递给自注意力层。

![图片](https://image.cubox.pro/cardImg/2023120418465213543/15002.jpg?imageMogr2/quality/90/ignore-error/1)

自注意力

自注意力层或许是Transformer和GPT的核心。在这一阶段，「输入嵌入」矩阵中的各列相互「对话」。到目前为止，在所有其他阶段，各列都是独立存在的。

自注意力层由几个头组成，我们现在只关注其中一个。

![图片](https://image.cubox.pro/cardImg/2023120418465256613/13506.jpg?imageMogr2/quality/90/ignore-error/1)

第一步是从归一化输入嵌入矩阵的C列中为每一列生成三个向量。这些向量分别是Q、K和V向量：

Q：查询向量

K：键向量

V：值向量

要生成这些向量中的一个，我们要执行矩阵-向量乘法，并加上偏置。

每个输出单元都是输入向量的线性组合。例如，对于Q向量，这是用Q权重矩阵的一行和输入矩阵的一列之间的点积来完成的。

![图片](https://image.cubox.pro/cardImg/2023120418465372649/89579.jpg?imageMogr2/quality/90/ignore-error/1)

我们会经常看到的点乘运算非常简单：我们将第一个向量中的每个元素与第二个向量中的相应元素配对，将这对元素相乘，然后将结果相加。

![图片](https://image.cubox.pro/cardImg/2023120418465385165/23256.jpg?imageMogr2/quality/90/ignore-error/1)

这是一种确保每个输出元素都能受到输入向量中所有元素影响的通用而简单的方法（这种影响由权重决定）。因此，它经常出现在神经网络中。

我们对Q、K、V向量中的每个输出单元重复这一操作：

![图片](https://image.cubox.pro/cardImg/2023120418465335558/39147.jpg?imageMogr2/quality/90/ignore-error/1)

我们该如何处理Q、K和V向量呢？命名给了我们一个提示：「key」和「value」让人联想到软件中的字典，

键（key）映射到值（value）。然后「query」就是我们用于查找值的东西。

![图片](https://image.cubox.pro/cardImg/2023120418465473782/33737.jpg?imageMogr2/quality/90/ignore-error/1)

在自注意力的情况下，我们返回的不再是单个词条，而是词条的加权组合。

为了找到这个加权，我们在Q向量和K向量之间进行点乘。我们将加权归一化，最后用它与相应的V向量相乘，再将它们相加。

![图片](https://image.cubox.pro/cardImg/2023120418465423379/46322.jpg?imageMogr2/quality/90/ignore-error/1)

举个更具体的例子，让我们看看第6列（t=5），我们将从这一列开始查询：

![图片](https://image.cubox.pro/cardImg/2023120418465476772/82439.jpg?imageMogr2/quality/90/ignore-error/1)

我们查找的 {K, V} 项是过去的6列，Q值是当前时间。

我们首先计算当前列（t=5）的Q向量与之前各列的K向量之间的点积。然后将其存储在注意力矩阵的相应行（t=5）中。

![图片](https://image.cubox.pro/cardImg/2023120418465448548/75720.jpg?imageMogr2/quality/90/ignore-error/1)

这些点积是衡量两个向量相似度的一种方法。如果它们非常相似，点积就会很大。如果两个向量非常不同，点积就会很小或为负。

只将query向量与过去的key向量进行运算，使得它成为因果自注意力。也就是说，token无法「预见未来」。

另一个要素是，在求出点积后，我们要除以sqrt(A)，其中A是Q/K/V向量的长度。进行这种缩放是为了防止大值在下一步的归一化（softmax）中占主导地位。

我们将跳过softmax操作（稍后解释），只需说明每一行的归一化总和为1即可。

![图片](https://image.cubox.pro/cardImg/2023120418465595584/35775.jpg?imageMogr2/quality/90/ignore-error/1)

最后，我们就可以得出这一列（t=5）的输出向量。我们查看归一化自注意力矩阵的（t=5）行，并将每个元素与其他列的相应V向量相乘。

![图片](https://image.cubox.pro/cardImg/2023120418465580792/43243.jpg?imageMogr2/quality/90/ignore-error/1)

然后，我们可以将这些向量相加，得出输出向量。因此，输出向量将以高分列的V向量为主。

现在我们知道了这个过程，让我们对所有列进行运行。

![图片](https://image.cubox.pro/cardImg/2023120418465514897/59322.jpg?imageMogr2/quality/90/ignore-error/1)

这就是自注意力层中的一个头的处理过程。

所以自注意力的主要目标是，每个列向量希望从其他列向量中找到相关信息，提取它们的值，方法是将其查询向量与其他列向量的键值进行比较。但有一个附加限制，即它只能查找过去的信息。

投影

在自我注意力过程之后，我们会从每个头得到一个输出。这些输出是受Q和K向量影响而适当混合的V向量。

要合并每个头的输出向量，我们只需将它们堆叠在一起即可。因此，在时间t=4时，我们将从3个长度为A=16的向量叠加到1个长度为C=48的向量。

![图片](https://image.cubox.pro/cardImg/2023120418465545142/35953.jpg?imageMogr2/quality/90/ignore-error/1)

值得注意的是，在GPT中，头（A=16）内向量的长度等于 C/num_heads。这确保了当我们将它们重新堆叠在一起时，能得到原来的长度C。

在此基础上，我们进行投影，得到该层的输出。这是一个简单的矩阵-向量乘法，以每列为单位，并加上偏置。

![图片](https://image.cubox.pro/cardImg/2023120418465697568/25512.jpg?imageMogr2/quality/90/ignore-error/1)

现在，我们得到了自注意力层的输出结果。

我们不会直接将这一输出传递到下一阶段，而是将其按元素顺序添加到输入嵌入中。绿色垂直箭头表示的这一过程被称为残差连接（residual connection）或残差路径（residual pathway）。

![图片](https://image.cubox.pro/cardImg/2023120418465669184/39533.jpg?imageMogr2/quality/90/ignore-error/1)

与「层归一化」一样，残差路径对于实现深度神经网络的有效学习非常重要。

有了自注意力的结果，我们就可以将其传递到Transformer的下一个部分：前馈神经网络。

MLP

在自注意力层之后，Transformer模块的下半部分是MLP（多层感知器）。虽然有点拗口，但在这里它是一个有两层的简单神经网络。

与自注意力一样，在向量进入MLP之前，我们要进行层归一化处理。

在MLP中，我们将每个长度为C=48的列向量（独立地）进行以下处理：

1. 添加偏置的线性变换，转换为长度为4\*C的向量。

2. 一个GELU激活函数（按元素计算）

3. 进行线性变换并添加偏置，返回长度为C的向量

让我们追踪其中一个向量：

![图片](https://image.cubox.pro/cardImg/2023120418465670958/94709.jpg?imageMogr2/quality/90/ignore-error/1)

我们首先进行带偏置的矩阵-向量乘法运算，将向量扩展为长度为4\*C 的矩阵。（请注意，输出矩阵在这里进行了转置，这纯粹是为了更加形象化）

![图片](https://image.cubox.pro/cardImg/2023120418465782330/49588.jpg?imageMogr2/quality/90/ignore-error/1)

接下来，我们对向量的每个元素应用GELU激活函数。

这是任何神经网络的关键部分，我们要在模型中引入一些非线性。使用的特定函数GELU看起来很像ReLU函数（计算公式为max(0,x)），但它有一条平滑的曲线，而不是一个尖角。

![图片](https://image.cubox.pro/cardImg/2023120418465782413/26011.jpg?imageMogr2/quality/90/ignore-error/1)

![图片](https://image.cubox.pro/cardImg/2023120418465764039/37911.jpg?imageMogr2/quality/90/ignore-error/1)

然后，我们通过另一个带偏置的矩阵-向量乘法，将向量投影回长度C。

![图片](https://image.cubox.pro/cardImg/2023120418465770411/24721.jpg?imageMogr2/quality/90/ignore-error/1)

与自注意力+投影部分一样，我们将MLP的结果按元素顺序添加到输入中。

![图片](https://image.cubox.pro/cardImg/2023120418465713700/13798.jpg?imageMogr2/quality/90/ignore-error/1)

现在，我们可以对输入内容中的所有列重复这一过程。

![图片](https://image.cubox.pro/cardImg/2023120418465893164/83220.jpg?imageMogr2/quality/90/ignore-error/1)

至此，MLP 完成。现在我们有了Transformer模块的输出，可以将其传递给下一个模块了。

Transformer

这就是一个完整的Transformer模块！

它们构成了任何GPT模型的主体，并且会重复多次，一个块的输出会输入到下一个块，继续残差路径。

与深度学习中常见的情况一样，很难说清楚这些层中的每一层在做什么，但我们有一些大致的想法：前面的层往往侧重于学习较低层次的特征和模式，而后面的层则学习识别和理解较高层次的抽象概念和关系。

在自然语言处理中，底层可能学习语法、句法和简单的词汇关联，而高层可能捕捉更复杂的语义关系、话语结构和上下文相关的含义。

![图片](https://image.cubox.pro/cardImg/2023120418465882195/33526.jpg?imageMogr2/quality/90/ignore-error/1)

\## Softmax

softmax运算不仅是自注意力机制的一部分，如前文所述，它还会出现在模型的最后阶段。

概括来说，softmax的目的是将向量中的值归一化，使它们加起来等于1.0。但这并不是简单地将各值除以总和那么简单。相反，每个输入值都会先被求指数。
> a = exp(x_1)

这样处理的效果是让所有值变为正数。一旦得到了一个指数化的值向量，就可以将每个值除以所有值的总和，从而确保所有值的和为1.0。由于所有指数化的值都是正的，那么最终的值将介于0.0和1.0之间，也就是为原始值提供了一个概率分布。

softmax的过程就是这样：简单地对值进行指数化处理，然后除以它们的总和。

不过，这里有一个小麻烦。

如果输入值很大，那么指数化后的值也会很大。这时，就将面临一个大数除以另一个大的数的情况，进而导致浮点运算出现问题。

softmax运算有一个有用的特性：如果向所有输入值添加一个常数，最终结果将保持不变。因此，可以在输入向量中找到最大值，并从所有值中减去这个它，这样可以确保最大值变为0.0，从而保持softmax运算的数值稳定。

在自注意力层，每个softmax运算的输入向量是自注意力矩阵的一行（但只到对角线为止）。

与「层归一化」类似，有一个中间步骤来存储一些聚合值来提高处理效率。

对于每一行，需要记录该行的最大值和经过移位与指数化处理后的值的总和。然后，为了得到相应的输出行，可以执行一系列操作：减去最大值，进行指数化处理，再除以总和。

那么，为什么叫「softmax」呢？

这个运算的「hard」版本，称为argmax，简单地找到最大值，将其设为1.0，其他所有值设为0.0。相比之下，softmax运算是一种更「soft」的版本。

由于涉及指数运算，softmax运算会突出最大值，并将其推向1.0，同时还保持了对所有输入值的概率分布。这样的处理方式不仅能捕获到最可能的选项，还能捕获到其他选择的相对可能性，实现了更细微的表示。

![图片](https://image.cubox.pro/cardImg/2023120418465818308/50756.jpg?imageMogr2/quality/90/ignore-error/1)

输出

最后一个Transformer块的输出，首先会经过层归一化，然后再进行线性变换（矩阵乘法），不过这次没有加入偏置项。

![图片](https://image.cubox.pro/cardImg/2023120418465854032/88175.jpg?imageMogr2/quality/90/ignore-error/1)

最后的transformation会将每个列向量的长度从C变为nvocab。因此，实际上是在为每一列的词汇库中的每个词产生一个得分------logits。

「logits」这个术语源自「log-odds」，也就是每个token的对数几率。之所以会使用「Log」（对数），是因为接下来应用的softmax会进行指数转换，从而把这些得分变成「几率」或者说概率。

为了把这些得分转化为更加直观的概率值，需要先通过softmax来进行处理。现在，每一列都得到了模型对词汇表中每个词所分配的概率。

在这个特定的模型中，它已经有效地学会了所有关于如何排序三个字母的问题的答案，因此给出的概率值，也很大概率会倾向于正确答案。

在对模型进行时间步进时，需要利用最后一列的概率值来决定下一个要添加到序列中的token。举个例子，如果已经向模型输入了6个token，那么就会用第6列的输出概率来决策。

这一列输出的是一系列概率值，因此必须从中选择一个作为序列的下一个元素。这需要通过「从分布中采样」来实现。也就是说，会根据概率值的权重随机选择一个token。例如，一个概率为0.9的token有90%的概率被选中。

当然，还有其他选择方法，比如始终选择概率最高的token。

此外，还可以通过使用温度参数来控制分布的「平滑度」。较高的温度会让分布更均匀，而较低的温度则会让分布更集中于概率最高的token。

在应用softmax之前，先用温度除以logits（线性变换的输出）。由于softmax中的指数化对较大的数值影响较大，因此将所有数字拉近会减少这种影响。

![图片](https://image.cubox.pro/cardImg/2023120418465875716/85494.jpg?imageMogr2/quality/90/ignore-error/1)

网友惊掉下巴

有网友表示，看到算法复杂度能够在三维空间中，以如此清晰的方式呈现出来，让我惊掉了下巴！

![图片](https://image.cubox.pro/cardImg/2023120418465969373/71115.jpg?imageMogr2/quality/90/ignore-error/1)

![图片](https://image.cubox.pro/cardImg/2023120418465970472/59172.jpg?imageMogr2/quality/90/ignore-error/1)

与NanoGPT相比，GPT-3简直是一个怪物。

![图片](https://image.cubox.pro/cardImg/2023120418465957308/41698.jpg?imageMogr2/quality/90/ignore-error/1)

这看起来比我们在 2005 年在大学里看到的简单神经网络要复杂1000倍。我正在考虑未来5-10年，通用人工智能 （AGI）将要走向哪里？

![图片](https://image.cubox.pro/cardImg/2023120418465924510/50591.jpg?imageMogr2/quality/90/ignore-error/1)

参考资料：

https://bbycroft.net/llm

![图片](https://image.cubox.pro/cardImg/2023120418465915257/40947.jpg?imageMogr2/quality/90/ignore-error/1)

![图片](https://image.cubox.pro/cardImg/2023120418465933610/39319.jpg?imageMogr2/quality/90/ignore-error/1)

![图片](https://image.cubox.pro/cardImg/2023120418470094541/18390.jpg?imageMogr2/quality/90/ignore-error/1)

[Read in Cubox](https://cubox.pro/web/card/7131285711155627032)
