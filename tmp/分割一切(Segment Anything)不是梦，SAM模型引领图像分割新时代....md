# 分割一切(Segment Anything)不是梦，SAM模型引领图像分割新时代

[zhuanlan.zhihu.com](https://zhuanlan.zhihu.com/p/667801207)黎明量化尘世中一个迷途小书童关注

目录

收起

封面

课程大纲

SAM能做什么？

SAM演示

SAM模型概览

Image预处理

Image encoder

prompt encoder

mask decoder

mask decoder

mask后处理

自动分割一切模式

自动分割一切模式原理

SAM的推理性能

SAM的训练数据

模型训练

focal loss是什么？

focal loss的构造

dice loss的构造

借助CLIP打通多模态

text prompt

SA-1B数据集

SAM应用之一：标注工具X-AnyLabeling

总结和局限性分析

感谢聆听

## 封面

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fpicx.zhimg.com%2F80%2Fv2-01f8febbba66771908c436d55995d1e5_720w.webp&valid=false)

欢迎参加本次关于SAM模型的深入探讨。今天，我们将一起揭开这种强大模型的神秘面纱，它不仅仅是分割图像中的对象，更能理解它们的上下文和相互关系。我们将从基础开始，逐步深入到[SAM模型](https://zhida.zhihu.com/search?content_id=236530188&content_type=Article&match_order=2&q=SAM%E6%A8%A1%E5%9E%8B&zhida_source=entity)的核心结构，探索它在现实世界中的应用，并展望这一领域的未来。无论您是人工智能的新手还是资深研究者，相信今天的内容都会给您带来新的启发。让我们开始这段[发现之旅](https://zhida.zhihu.com/search?content_id=236530188&content_type=Article&match_order=1&q=%E5%8F%91%E7%8E%B0%E4%B9%8B%E6%97%85&zhida_source=entity)吧！

## 课程大纲

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fpicx.zhimg.com%2F80%2Fv2-e839096224a5348887669f31571de545_720w.webp&valid=false)

我们先从一个宏观的视角来审视SAM涉及的关键点：

第1部分是SAM简介：我们会简要介绍SAM模型是什么，以及它如何革新了[图像分割](https://zhida.zhihu.com/search?content_id=236530188&content_type=Article&match_order=1&q=%E5%9B%BE%E5%83%8F%E5%88%86%E5%89%B2&zhida_source=entity)领域。

第2部分是SAM推理：在这部分，我们将识别并解释构成SAM模型的主要组件，包括[图像编码器](https://zhida.zhihu.com/search?content_id=236530188&content_type=Article&match_order=1&q=%E5%9B%BE%E5%83%8F%E7%BC%96%E7%A0%81%E5%99%A8&zhida_source=entity)、提示编码器以及掩码解码器的作用。

第3部分是SAM训练：我们将介绍用于训练SAM模型的损失函数，如[focal loss](https://zhida.zhihu.com/search?content_id=236530188&content_type=Article&match_order=1&q=focal+loss&zhida_source=entity)和dice loss，它们如何帮助模型提升分割的精确度。

第4部分是打通[多模态](https://zhida.zhihu.com/search?content_id=236530188&content_type=Article&match_order=1&q=%E5%A4%9A%E6%A8%A1%E6%80%81&zhida_source=entity)：CLIP能够使模型理解和关联图像与文本提示，这在提升模型对图像内容理解的深度和广度上起着至关重要的作用。

在第5部分我们会探讨SA-1B数据集是如何制作的，以及一个基于SAM的一个较为成熟的语义标注工具X-AnyLabeling，最后我们会对SAM进行总结和局限性分析

随着课程的深入，我们将详细探索这些组件和概念，并了解它们如何协同工作以实现模型的强大功能。

## SAM能做什么？

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fpic3.zhimg.com%2F80%2Fv2-ae5923b696b5468c0294ff7c6acdacf6_720w.webp&valid=false)
动画见：https://segment-anything.com/

SAM的实用性和灵活性允许我们在多种情境中进行有效的图像分割，这里我们将探讨SAM模型的交互方式和特点：

首先，我们介绍交互式点和框。这项技术允许用户直接在图像上标记感兴趣的区域，模型随后将围绕这些标记进行详细的分割。具体而言，当用户点击青蛙的时候，SAM会分割出整只青蛙的[掩码](https://zhida.zhihu.com/search?content_id=236530188&content_type=Article&match_order=2&q=%E6%8E%A9%E7%A0%81&zhida_source=entity)。

其次，是全图自动分割，SAM模型在这种模式下能够识别并分隔图像中的每一个元素，无需任何人工输入，展现了它的自动化能力。

接着，我们讨论模糊提示下的多掩码生成。在这种情况下，SAM模型能够对含糊的指令做出响应，产生多个可能的分割结果，显示了模型在处理不明确信息时的灵活性。具体而言，用户点击的位置既可以代表衣服，也可以代表人体的时候，SAM会将它们都返回，并携带相应的[置信度](https://zhida.zhihu.com/search?content_id=236530188&content_type=Article&match_order=1&q=%E7%BD%AE%E4%BF%A1%E5%BA%A6&zhida_source=entity)。SAM最多可以支持返回三个结果。
![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fpic1.zhimg.com%2F80%2Fv2-52e374a948e9020f93b4479206c28044_720w.webp&valid=false)
动画见：https://segment-anything.com/

第四，是[眼动追踪](https://zhida.zhihu.com/search?content_id=236530188&content_type=Article&match_order=1&q=%E7%9C%BC%E5%8A%A8%E8%BF%BD%E8%B8%AA&zhida_source=entity)的应用，这种方法利用用户的视线来指导分割，提供了一种无接触的VR交互方式，使模型能够更自然地理解用户的意图。

最后，我们探讨SAM模型在处理多模态任务时的能力，尤其是它如何根据文本提示进行图像分割。例如，当用户输入"cat"作为文本提示时，SAM模型可以智能地识别并分割出图像中所有的猫。这种能力显示了SAM模型理解复杂查询并在图像中准确反映这些查询的强大功能。

通过这些介绍，相信你将对SAM模型如何与用户交互以及如何处理各种输入有一个初步的了解。总结一下就是：SAM能支持多种多样[prompt](https://zhida.zhihu.com/search?content_id=236530188&content_type=Article&match_order=1&q=prompt&zhida_source=entity)引导的交互式语义分割！

## SAM演示

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fpic1.zhimg.com%2F80%2Fv2-eb3d36b9589b8d9ab634a40486c64038_720w.webp&valid=false)

下面我们用一些例子更加详细地介绍一下SAM的[交互式分割](https://zhida.zhihu.com/search?content_id=236530188&content_type=Article&match_order=1&q=%E4%BA%A4%E4%BA%92%E5%BC%8F%E5%88%86%E5%89%B2&zhida_source=entity)方式：

首先介绍使用点的交互式分割：

以一张汽车的原图为例，当用户在汽车玻璃上标记一个正点时，由于其位置的语义模糊性，可以代表不同的图像元素：单块玻璃、两块玻璃，甚至是整辆汽车。正是这种模糊性，驱使SAM模型生成三种不同的掩码，并为每个掩码提供一个置信度评分。这就展示了模型如何解释单一输入点的多重可能性，并对每种解释给出一个量化的评估。

接下来介绍使用掩码和点的组合进行交互式分割：

比如基于两块玻璃的掩码和一个正点，当我们再在车门处添加一个新的正点时，SAM模型识别到这一新增的点强化了对整辆汽车的指示，因此返回了覆盖整辆汽车的掩码。在另一个情景中，我们在车门处添加了一个负点。这个负点帮助模型缩小了分割的范围，使其更加确信用户想要的是特定的两块玻璃，从而更加确定两块玻璃的分割结果。
![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fpicx.zhimg.com%2F80%2Fv2-b3b898759f0e9bba7c9bc7a8d50d2239_720w.webp&valid=false)

SAM模型还可以处理其他更复杂的交互模式，如框、点、文本以及它们的组合。

当我们利用框的交互方式标记图像时，SAM模型可以精确地返回被框选区域的掩码，如一个完整的车轮。

当我们在一个框选的车轮中添加一个负点，指示我们不需要车轮中心的铁质部分时，SAM理解我们的指示，只返回轮胎部分的掩码。这种细致的分割能力对于需要精确结果的应用场景是至关重要的。

接下来，我们探索SAM模型如何使用文本提示进行分割。简单地输入"车轮"，SAM就能识别并分割出车轮。更具体地，输入"海狸齿格栅"，SAM就展现了其对特定文本描述的理解，准确地分割出汽车的格栅部分。

我们还可以将文本提示和交互点相结合以提高分割的准确性。例如，在输入"雨刷器"后，SAM可能未能找到正确的部件，但是当我们添加一个正点以指示雨刷器的位置时，SAM就能精准地分割出正确的雨刷器。同样地，当我们输入"雨刷器"并指出多个雨刷器时，结合一个正点，SAM模型就能理解我们需要识别所有的雨刷器，并返回正确的分割结果。

通过这些交互方式，SAM模型证明了自己在理解和执行复杂图像分割任务中的灵活性和准确性。每次交互都是与SAM模型的对话，它能够理解我们的需求并提供我们所需要的精确结果。

SAM模型为我们解锁更多的图像分割可能性，现在我们对前面所述的交互方式做一个小结：

1. 只使用点时：至少有1个正点，可以再加任意多个点（无论正点和负点）

2. 使用框时：只能有1个框，可以再与点和最多一个[mask](https://zhida.zhihu.com/search?content_id=236530188&content_type=Article&match_order=1&q=mask&zhida_source=entity)组合

3. 使用mask时：只能有1个mask，可以再与点和最多一个框组合

4. 使用text时：只能有1个text，可以再与点组合（但这是实验性质的，在MetaAI release的代码中并没有支持这一功能）

## SAM模型概览

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fpic2.zhimg.com%2F80%2Fv2-b384c2bbc410c5d7604ea12d41480b69_720w.webp&valid=false)

通过前文的案例演示，相信大家对SAM的功能有一个较为深刻的认识。下面我们看一下SAM模型的任务框架。

左图中，我们可以看到模型如何处理包含多种交互式提示的图像。不论是简单的点、[框选区域](https://zhida.zhihu.com/search?content_id=236530188&content_type=Article&match_order=2&q=%E6%A1%86%E9%80%89%E5%8C%BA%E5%9F%9F&zhida_source=entity)，掩码区域、还是描述性文本，SAM都能理解并生成有效的分割掩码。

右图展示了SAM的内部结构。模型由3个主要部分组成：提示词编码器、图像编码器和一个轻量级的掩码解码器。图像通过图像编码器进行处理，而提示------无论是点、框、掩码还是文本------都通过提示编码器转换为模型可以理解的形式。掩码解码器会接收提示表征和图像表征，并产出合理的掩码。图像中，方块的大小代表了模型的参数量，我们可以看到，图像编码器是计算量最大的部分。

下图展示了SAM更多的结构细节。图像经过图像编码器得到图像表征。[提示词](https://zhida.zhihu.com/search?content_id=236530188&content_type=Article&match_order=2&q=%E6%8F%90%E7%A4%BA%E8%AF%8D&zhida_source=entity)根据类型可以分为稠密性提示词（比如掩码）和稀疏性提示词（比如点和框使用坐标点来表示，文本是使用tokenid来表示），图像表征在输入掩码解码器之前需要和掩码特征进行相加，最终掩码解码器会生成多种合理的掩码以及对应的置信度。

## Image预处理

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fpic4.zhimg.com%2F80%2Fv2-b01690c25be5f84e309aaa59a4716f7d_720w.webp&valid=false)

下面我们将聚焦于SAM模型在进行图像分割前的重要一环：图像的预处理流程。这个过程确保了图像以一种标准化的方式被模型所理解，从而保证了分割结果的准确性和一致性。

我们的起点是一副尺寸为534x800像素的彩色图像。首先，我们以保持图像的宽高比的方式将图像最长边放缩到1024。

接下来是颜色归一化。通过从每个像素中减去平均值并除以标准差，颜色归一化的目的是为了统一不同图像的颜色范围，减少照明条件和设备差异对模型训练的影响，从而提高模型的泛化能力和加快训练速度。

最后，我们会应用填充（Padding），以确保所有的图像都有相同的维度即1024\*1024.

## Image encoder

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fpic4.zhimg.com%2F80%2Fv2-e12c8423d16455c4c6f7b13c66a287a9_720w.webp&valid=false)

讨论完图像预处理步骤之后，接下来我们将聚焦于图像编码器------这是SAM模型理解图像的基石。

图像编码器选用的是Vision Transformer (也就是ViT)，它是一种创新的[神经网络架构](https://zhida.zhihu.com/search?content_id=236530188&content_type=Article&match_order=1&q=%E7%A5%9E%E7%BB%8F%E7%BD%91%E7%BB%9C%E6%9E%B6%E6%9E%84&zhida_source=entity)，它将图像视为一序列的小块（patches），并通过[自注意力机制](https://zhida.zhihu.com/search?content_id=236530188&content_type=Article&match_order=1&q=%E8%87%AA%E6%B3%A8%E6%84%8F%E5%8A%9B%E6%9C%BA%E5%88%B6&zhida_source=entity)来捕捉这些块之间的复杂关系，为[图像分析](https://zhida.zhihu.com/search?content_id=236530188&content_type=Article&match_order=1&q=%E5%9B%BE%E5%83%8F%E5%88%86%E6%9E%90&zhida_source=entity)任务带来了颠覆性的性能提升。

下面我将解释图像编码器是如何将标准化后的图像转化为后续模型可解析的图像表征的。

在经过归一化和尺寸调整的图像准备就绪之后，图像编码器开始其工作。我们的流程从Patch Embedding开始。在这个阶段，一个专门设计的卷积层将图像分割成小块，并将每个小块转换成深度特征向量。具体而言，Patch Embedding使用的是[卷积核](https://zhida.zhihu.com/search?content_id=236530188&content_type=Article&match_order=1&q=%E5%8D%B7%E7%A7%AF%E6%A0%B8&zhida_source=entity)尺寸为16\*16、步长为16，输出维度为768的二维卷积，因此我们会得到64\*64个768维的向量。然后加上位置编码，位置编码的作用是向模型提供图像中每个像素或补丁的位置信息，使模型能够理解图像中物体的空间排列，从而更准确地执行图像分割任务。

接下来是VIT的核心------Transformer架构。我们使用了12个Transformer块来处理这些向量，每个块都在维持序列信息的同时，增强了特征的表示。这个过程极大地增强了模型对图像中各部分的理解。

最终，我们得到了一个高维的图像嵌入，它包含了图像的丰富[语义信息](https://zhida.zhihu.com/search?content_id=236530188&content_type=Article&match_order=1&q=%E8%AF%AD%E4%B9%89%E4%BF%A1%E6%81%AF&zhida_source=entity)和细节特征。然后对这个嵌入进项降维和通道调整，用于后续的分割任务。

## prompt encoder

继上一部分图像编码器的介绍之后，我们现在转向SAM模型的另一关键组成部分------提示编码器。在这里，我们将深入了解模型是如何利用mask和文本这两种提示来提炼出我们希望分割的图像区域。

首先，mask提示允许我们直接在原像上指示感兴趣区域来引导模型。这些mask通过卷积操作被转换为与图像嵌入空间相匹配的特征，然后与图像嵌入相加结合，为模型提供分割的精确位置信息。如果没有使用mask提示，则用一组可学习向量(no_mask_embed, 1×256) expand为256×64×64后替代。

而文本提示，利用了CLIP的文本编码器，将描述性的语言输入转换为模型可以理解的嵌入向量。比如输入"黑耳朵的猫"，文本编码器就能将这些词转换为一个强大的特征描述，引导模型聚焦于具有这些特征的图像区域。

继mask和text提示之后，我们现在将聚焦于box和point两种交互式提示的[编码过程](https://zhida.zhihu.com/search?content_id=236530188&content_type=Article&match_order=1&q=%E7%BC%96%E7%A0%81%E8%BF%87%E7%A8%8B&zhida_source=entity)。这些提示方法提供了与SAM交互时更加便捷的操作方式。

关于box：

1. box是用户在原图上框选的，一个box由两个坐标构成(左上和右下)

2. box经过prompt encoder后的尺寸为2×256 (2表示两个坐标，即一个坐标对应1×256)

关于point：

1. point是用户在原图上绘制的

2. 一个point经过prompt encoder后的尺寸为1×256，同理N个点会形成N×256

3. point有正负label之分，正代表前景，负代表背景，因此还要在点的1×256表征上叠加一组表示正负点嵌入的可学习参数(分别为point_embedding，1×256)

4. 当不使用box时，需要显式地告诉后续的模型，通过追加连接一个not_a_point_embed可学习向量(1×256)来实现

同理，需要显式告诉模型，坐标点是box角点而不是point的点，可通过叠加一个corner embedding可学习向量(1×256)来实现

通过这种追加或叠加的方式，会降低模型的学习难度。比如：如果一味地叠加，势必会出现信息瓶颈。

## mask decoder

在我们深入探讨了图像编码器和提示词编码器后，现在我们将聚焦于SAM模型的第三个核心组成部分------mask decoder。Mask decoder的职责是整合来自图像嵌入的丰富视觉信息和提示词编码器提供的表征信息，其最终目的是解码出精确的语义分割掩码。

首先让我们探讨image embedding。这个步骤在模型中至关重要，它不仅包含了原始图像的信息，还融入了稠密的prompt掩码信息。通过这样的融合，我们得到了一个增强的图像表征，它更全面地捕捉了图像内容和用户指示的分割意图。

接下来是对tokens的讨论。这些tokens不只是承载了稀疏的prompt掩码信息，它们还包括用于未来预测的特殊token------一个预测交并比（IOU）的token和四个预测掩码的token。IOU token的设计用来作为占位符，在模型运行过程中预测掩码和实际掩码之间的交并比，为我们提供一个掩码预测的置信度指标。而mask tokens的角色是作为预测具体分割掩码的占位符，之所以有四个，是因为SAM模型的灵活性允许它在模糊语义下生成多达三个掩码，或者在需要时只生成一个特定掩码。

在图示中，我们看到的prompt tokens向量是以一个box提示为例。这简化了展示，但实际上SAM模型可以处理更复杂的多box情景。

总的来说，mask decoder是SAM模型的关键组件，它利用深层神经网络的强大能力，结合图像内容和用户指示，高效地生成高质量的语义分割掩码。

## mask decoder

在前一页的介绍之后，我们现在深入到SAM模型的核心之一：mask decoder的内部机制，以及数据是如何在这一复杂结构中流动和转换的。

首先，tokens被送入mask decoder，并进行自我注意力（self-attention）处理。自我注意力机制的作用是让模型学会在tokens内部寻找和放大重要的关系，这对于理解各种提示词之间的相互作用是至关重要的。

接下来，这些经过自我注意力处理的tokens作为查询（query），与图像嵌入的键（key）和值（value）结合进行图像到token的注意力（token to image attention）操作。这一步骤的目的是将经过提示词处理的信息与原始图像的丰富上下文信息结合起来，从而为解码过程引入了视觉信息。

然后，结果通过一个[多层感知器](https://zhida.zhihu.com/search?content_id=236530188&content_type=Article&match_order=1&q=%E5%A4%9A%E5%B1%82%E6%84%9F%E7%9F%A5%E5%99%A8&zhida_source=entity)（MLP）层，产生新的特征表征。这些特征表征随后被用作键和值，图像嵌入作为查询，执行另一轮图像到token的注意力（image to token attention）操作，进一步精炼模型对图像的理解。

以上过程构成了mask decoder的第一部分。第二部分采用相同的结构，进一步加强特征表征。

在模型的输出阶段，有两个分支。一分支通过两次转置卷积操作，将维度从256×64×64提升至32×256×256，这样做是为了将特征映射回原始图像的尺寸。另一分支则使用前面MLP的输出作为查询，执行token到图像的注意力（token to image attention）操作，生成两个输出流：一个是IoU输出token（1×256），它经过一个MLP层后，可以预测每个预测掩码与真实掩码间的交并比（IoU）；另一个输出是每个掩码的输出token（4×256），经过四个MLP层后得到(1+3)×32的张量。

最后，这个(1+3)×32的张量与先前的32×256×256结果进行每个掩码的点积运算（dot product per mask），得到(1+3)×256×256的最终预测掩码，这正是我们分割任务的目标产物。

通过这一精心设计的decoder架构，我们的SAM模型能够理解复杂的视觉提示，精准地解码出高质量的分割掩码，无论是在明确的单一目标还是在模糊的多目标场景下。

## mask后处理

接续我们之前关于mask decoder的讨论，我们已经探究了如何生成mask logits。现在，让我们看看这些低分辨率的mask logits（3×256×256）是如何被处理和转换为我们最终所需的高分辨率mask。

首先，这些logits需要被调整尺寸（resize）到一个更高的分辨率，即3×1024×1024。这个过程是必须的，因为我们需要确保预测的mask与我们的输入图像有相同的分辨率，以便于进行精确的像素级比较。

接下来，我们去除了在处理过程中可能加入的任何填充（padding），这是为了确保我们的mask能够与原始图像的边界紧密对齐。然后，我们将这些mask等比缩放回原始图像的尺寸（例如3×534×800），以保持其与原始图像的相对位置和比例不变。

一旦我们得到了与原始[图像尺寸](https://zhida.zhihu.com/search?content_id=236530188&content_type=Article&match_order=1&q=%E5%9B%BE%E5%83%8F%E5%B0%BA%E5%AF%B8&zhida_source=entity)对应的mask logits，下一步就是进行二值化处理。这个过程将logits转换为清晰的二进制mask，其中1表示对象的位置，0表示背景。通过这种方式，我们能够清晰地分离出感兴趣的对象与其周围环境。

如前所述，每个mask都对应一个预测的交并比（IoU）值。这个IoU值对于评估我们的mask有多准确是非常关键的，因为它可以直接用来衡量预测掩码与真实掩码之间的重叠程度。因此，IoU值不仅是性能评估的指标，也是我们可以用来计算每个预测掩码置信度的一个重要参考。

通过这种细致的处理流程，我们的模型不仅能够生成精确的语义分割掩码，还能为每个掩码提供一个准确的置信度评分，这使得模型的预测不仅准确而且可靠。

## 自动分割一切模式

在这一部分，我们将展示SAM（Segment Anything Model）的"自动分割一切"模式的实际应用。首先，我们从一张普通的原图开始，这张图未经任何标注。接下来，为了启动分割过程，我们在图像上均匀分布32×32个点。这些点的布置是精心设计的，每个点都作为一个正点来指示潜在的前景对象。

值得注意的是，在模型传播过程中，这些点是并行处理的，每个点的处理都是独立的。这意味着每个点都独立地引导SAM去理解和解析图像的不同部分。这种方法允许我们在不需要任何先验标注的情况下，探索图像中所有可能的前景对象。

在点的撒播和网络传播之后，模型生成了多个可能重叠的mask。这些mask代表了图像中潜在的多个对象。然后，我们对这些预测出的mask进行去重处理，这是通过识别和合并重叠区域来完成的，确保每个对象只有一个唯一的mask表示。

最后，我们呈现了所有去重后剩下的mask，作为模型的最终输出。这些mask描绘了图像中所有被模型识别为前景的区域。这个过程不仅凸显了SAM的强大自动化能力，也展示了它在没有任何人工干预的情况下，能够如何准确地捕捉和分割出图像中的多个对象。

## 自动分割一切模式原理

在这一页的PPT中，我们将深入探讨SAM自动分割一切模式的原理和流程。我们的起点是一张原始图片，首先通过固定比例的padding将其调整到1024×1024的尺寸。然后，在图像区域均匀撒播32×32个独立的正点。正如之前提到的，这些点是并行进行前向传播的，我们将这些点分为16批，每批64个点。

以一个batch为例，通过模型传播后，我们获得了一系列的mask logits，形成了一个具有原图尺寸（534×800）的大张量。这里的192是由于每个点生成了3种可能的掩码，乘以64个点，得到每个batch的掩码候选。

接下来，mask decoder除了生成掩码外，还为每个掩码产生一个对应的IOU预测值。利用这些IOU预测值，我们可以过滤掉那些IOU值小于0.88的mask logits，从而减少到80个候选掩码。然后，我们进一步计算每个掩码的稳定性分数，将那些稳定性分数低于0.95的mask logits过滤掉，最终剩下34个掩码。

我们对这些logits进行二值化处理，使用的阈值为0，从而得到最终的mask。按照这个过程，我们将16个批次的数据全部处理完毕，然后将结果聚合，得到总共399个候选掩码。最后，通过应用盒型非极大值抑制（Box NMS）技术，并设定IOU阈值为0.7，我们得到了最终的40个掩码。

这个过程展示了SAM模型在处理并行点时的效率和独立性，也突出了其通过多阶段筛选和优化来精确控制最终掩码输出的能力。

## SAM的推理性能

在前面的讨论中，我们探讨了SAM的理论和内部工作机制。现在，让我们转向SAM的推理性能，这是在实际应用中非常关键的一个方面。我们的测试环境配置为第13代Intel i9-13900KF CPU和NVIDIA RTX 4090 GPU，代表了当前高端的计算能力。

我们比较了两个不同规模的SAM模型：sam_vit_b和sam_vit_h，分别代表使用了Vision Transformer的基础（base）和巨大（huge）版本。参数量的差异主要体现在image encoder上，也就是Vision Transformer的规模。在我们的测试中，VIT在SAM架构中占据了参数量的大头，其次是mask decoder，而prompt encoder参数量最少。

这个差异反映了在SAM模型中，图像编码器对于整体性能的重要性。它承担了从原始图像中提取有意义视觉特征的任务，这是后续所有分割工作的基础。对于mask decoder而言，尽管参数量不如image encoder，但它在模型中执行着将视觉特征转换为具体掩码的重要工作。

值得一提的是，在某些应用场景中，我们可以预先使用image encoder计算出image embeddings，这样可以在后续的推理过程中大幅度提升效率。例如，在我们的测试中，对单个物体进行解码加上后处理只需2毫秒，而进行完整的分割加上后处理需要几百毫秒。这说明，在需要快速响应的场景中，预先计算和存储image embeddings可以显著提高效率。

总之，SAM模型不仅在理论上优雅，在实际应用中也展现出了优异的性能。它的推理速度和效率使得它适用于各种需要快速准确语义分割的场景，无论是在实时应用中，还是在需要高吞吐量处理的后台任务中。

## SAM的训练数据

在这里，我们将探讨SAM模型是如何进行训练的，特别是它的训练数据是怎样的。在左上角的原图中，可以看到的是一张训练图片，在左下图，我们看到了全部的掩码图。由于多个掩码的重叠，这幅图可能看起来有些混乱。

为了更清楚地理解，我们看右上角的图，我们注意到有一位女士的衣服在图像中是高亮的。如果我们看右下角的图，我们可以看到这位女士的全身都被高亮显示了。这意味着在标注的数据里，就会存在语义模糊的情况，这是符合逻辑的，也从侧面反映出SAM设计3种掩码输出的合理性。

## 模型训练

在这一页中，我们将探讨如何通过模拟交互来构建SAM模型的损失函数。以预测女士衣服的掩码为例，我们采用了"通过在每个掩码上随机采样提示词进行11轮模拟交互设置"的方法来自动化构造提示词。

正如我们在第二列的示例中所看到的，提示词可能包括一个位于衣服左上角的正点，一个覆盖衣服的框，以及衣服右上角的正点等等。这种方法允许我们自动生成各种可能的提示组合，以模拟用户交互过程中可能提供的输入。

随后，每一种构造的提示词都会与原图一起被送入解码器。解码器对每种提示进行处理，生成相应的掩码logits。每个掩码logits都会与真实的掩码标签进行比较，计算出一个损失值。

这个损失值是模型学习过程中的关键反馈，它告诉模型预测的掩码与实际标注之间的相似度。通过这样的训练过程，SAM模型逐步学会如何更准确地预测掩码，即使在缺乏确切指示的情况下也能做出正确的分割。这种训练方法不仅提高了模型对用户输入的敏感性，也增强了模型处理不确定性的能力。

## focal loss是什么？

这一页PPT主要讨论了焦点损失（Focal Loss），这是SAM中使用的损失函数之一，让我们来深入了解一下它的工作原理。

焦点损失是一种专门设计用来处理类别不平衡问题的损失函数。它的核心思想是通过调整样本的权重，增加模型对难以分类的样本的关注，从而改善模型的性能。

在图中，我们研究单个样本。横坐标表示预测正确的概率（前景预测为前景的概率，背景预测为背景的概率），纵轴表示在不同概率下的损失值。我们首先看到了[交叉熵](https://zhida.zhihu.com/search?content_id=236530188&content_type=Article&match_order=1&q=%E4%BA%A4%E5%8F%89%E7%86%B5&zhida_source=entity)损失（Cross Entropy Loss，CE），它是常用的分类损失函数。然后，我们引入了焦点损失（Focal Loss，FL），其中γ表示一个控制焦点损失下沉程度的超参数。

当γ等于0时，焦点损失等同于交叉熵损失，如图中最上面的蓝色曲线所示。但随着γ的增加，曲线逐渐下沉，这导致一个重要的效应：当模型对某个样本预测正确的概率较高时，其对应的损失值会下降。这种下降效应使得模型更加关注那些难以分类的样本，即使在类别不平衡的情况下也能更好地进行分类。

因此，焦点损失的关键在于它能够聚焦于难以分类的样本，帮助模型更好地应对类别不平衡问题，从而提高了模型的性能。这使得SAM在处理各种应用场景中都表现出色。

## focal loss的构造

前面我们介绍了一些背景知识，在本页PPT中，我们主要研究SAM如何构建Focal Loss。首先，我们有一个表示预测的掩码 logits（mask logits），然后有一个表示掩码的真实标签（ground truth），这两者都被展开成了一个1×956800的向量。预测的掩码 logits经过sigmoid函数转换成概率，并计算了交叉熵损失（CE Loss）。接着，我们计算了预测掩码的预测正确概率p_t，并设置γ=2来计算Focal Loss（FL）。需要注意的是，FL是在CE Loss的基础上，通过指数级增加了困难样本的权重。

此外，还有一个过程涉及到调整正负样本的权重，即计算一个α-balanced focal loss，其中α因子被设置为0.25，小于0.5，即意味着我们希望额外关注负样本。这里可能会有一些疑惑，因为通常来说，正样本（即前景像素点）数量较少，为什么要在权重平衡时更加关注负样本呢？

实际上，作者进行了一系列实验，结果表明，虽然正样本（前景像素点）较少，但通过Focal Loss的设计，即使α小于0.5，结合γ参数的调节作用，模型仍然能够有效地关注那些难以识别的前景像素点。这也引出了一个有趣的结论，即FL对正样本的惩罚相对较大，因此需要通过α来弥补对负样本的关注。

总结一下SAM中Focal Loss的构建过程，包括：预测掩码 logits的计算，CE Loss的计算，Focal Loss的计算（通过γ调节困难样本的权重），以及α-balanced Focal Loss的计算（通过α调整正负样本的权重）。

## dice loss的构造

接下来为大家介绍SAM中使用的另一种损失函数------Dice Loss的构造方法。Dice系数是一种用于衡量两个样本集相似性的统计工具，在图像分割任务中，它用来[评估模型](https://zhida.zhihu.com/search?content_id=236530188&content_type=Article&match_order=1&q=%E8%AF%84%E4%BC%B0%E6%A8%A1%E5%9E%8B&zhida_source=entity)预测结果与真实标签之间的重叠度。

首先，让我们来了解一下Dice Loss的构造过程。与之前的Focal Loss类似，我们同样需要一对预测的掩码 logits（mask logits）和掩码的真实标签（ground truth）。这两者被展开成了1×956800的向量，这一步与Focal Loss的处理方式相同。

接下来的步骤是Dice Loss的核心构建过程。首先，我们将预测的掩码 logits 和真实标签进行element-wise的相乘，这可以视为计算两者的交集。然后，对这个交集进行reduce求和操作，将其作为分子。接着，我们分别对预测的掩码 logits 和真实标签进行reduce求和，然后再将它们相加，将其作为分母。最后，通过分子和分母的比值，构造了Dice Loss，其计算方式如图中所示。

Dice Loss的优势：Dice Loss相比于交叉熵损失，有以下几个优势：一是它不依赖于类别的[先验概率](https://zhida.zhihu.com/search?content_id=236530188&content_type=Article&match_order=1&q=%E5%85%88%E9%AA%8C%E6%A6%82%E7%8E%87&zhida_source=entity)，因此可以更好地处理类别不平衡的问题；二是它直接关注预测结果和真实标签之间的重叠度，因此可以更好地评估分割的质量；三是它可以与其他损失函数结合使用，例如Focal Loss，以进一步提高模型的性能。

## 借助CLIP打通多模态

接下来为大家介绍SAM模型中处理文本特征的过程。在SAM模型中，提示词编码器可以接受四种不同类型的输入，其中之一就是文本。这意味着SAM可以处理来自文本的信息，以便更好地理解和处理图像数据。然而，在我们深入研究SAM如何处理文本特征之前，让我们先了解一下CLIP的背景。

CLIP是一种重要的概念，它是Contrastive Language-Image Pre-training的缩写。CLIP的独特之处在于它可以将文本和图像嵌入到同一个[特征空间](https://zhida.zhihu.com/search?content_id=236530188&content_type=Article&match_order=1&q=%E7%89%B9%E5%BE%81%E7%A9%BA%E9%97%B4&zhida_source=entity)，并且使它们在这个特征空间中对齐。这意味着CLIP能够让我们通过共享的特征空间来衡量文本和图像之间的相似性，从而实现了跨模态的语义理解。CLIP的引入为SAM模型提供了一个强大的基础，使其能够更好地理解文本和图像之间的关系。

## text prompt

在之前的内容中，我们已经了解了CLIP的一些基本概念，现在，我们将详细介绍SAM如何利用CLIP来实现强大的图文理解。

在SAM的训练阶段，我们采用了一种创新性的方法，以确保模型能够具备跨模态理解的能力。具体来说，对于那些面积大于1万像素的物体，在训练过程中，我们使用CLIP的图像编码器（CLIP image encoder）来获得图像嵌入（image embeddings）。然后，将这些图像嵌入作为文本的提示词（prompt）传递给SAM的提示词编码器。这里需要特别注意的是，这些图像嵌入是由CLIP生成的，与文本嵌入天然对齐，因为CLIP是一种可以将文本和图像嵌入到同一个特征空间的技术。因此，这个过程非常巧妙且合理，使得SAM能够从图像中提取有关物体的语义信息，并将其与文本描述相结合。

在SAM的推理阶段，当用户提供一个文本输入，比如"cat"，SAM会使用CLIP的文本编码器（CLIP text encoder）来生成文本嵌入（text embeddings）。然后，将这些文本嵌入作为文本提示词传递给SAM的提示词编码器。这样，SAM可以将用户提供的文本与之前训练中用于图像的提示词相结合，从而实现对图像和文本的跨模态理解。

## SA-1B数据集

下面为大家介绍SAM论文中的一个重要贡献点------SA-1B数据集，以及关于SA-1B数据集的制作过程。SA-1B数据集在SAM论文中扮演着重要的角色，为模型的训练和研究提供了宝贵的资源。

首先，让我们来了解一下SA-1B数据集的一些基本信息。SA-1B数据集是一个巨大的数据集，它包括了10亿个掩码（mask）数据，以及1100万张大图像，其中大多数图像的大小平均为3300×4950像素，与COCO数据集中的图像相比，尺寸更大。此外，为了保护隐私，SA-1B数据集还进行了人脸和车牌的模糊化处理，并且图像的使用得到了相应的授权。

SA-1B数据集的制作过程可以分为三个主要阶段。首先是辅助人工阶段，在这个阶段，使用公开的数据集训练了一个SAM模型。然后，标注员基于SAM预测的掩码进行修改，这个过程经过了5次的迭代，以确保数据的准确性。接下来是半自动阶段，主要用于标注传统语义分割不太关注的物体。同样，这个阶段也经过了5次的迭代，以提高数据的质量。最后是全自动阶段，采用了一系列技巧，如数据增强、更大的掩码解码器、更长时间的训练等，以进一步提升SAM生成的掩码的质量。

SA-1B数据集的创建不仅为SAM模型的训练提供了大规模高质量的数据，也为研究人员提供了一个宝贵的资源，可以用于各种[计算机视觉](https://zhida.zhihu.com/search?content_id=236530188&content_type=Article&match_order=1&q=%E8%AE%A1%E7%AE%97%E6%9C%BA%E8%A7%86%E8%A7%89&zhida_source=entity)任务的研究和评估。

## SAM应用之一：标注工具X-AnyLabeling

https://github.com/CVHub520/X-AnyLabeling

下面为大家介绍一个SAM的重要应用场景，即SAM在标注工具X-AnyLabeling中的应用。

现在，让我们来谈谈这张医学影像。医学影像通常具有复杂的结构和语义信息，对于传统的通识领域的语义分割模型来说，很难在这种数据上取得良好的效果。然而，SAM却能够在这种情况下发挥出色的性能。SAM之所以能够做到这一点，是因为它经过了丰富多样的海量训练数据的训练，具备了强大的zero-shot能力。这意味着即使SAM之前没有见过这种类型的医学影像，它也能够理解和解释其中的语义信息，并进行准确的分割。

SAM的应用不仅限于通识领域的图像，它可以在各种领域的图像分割任务中发挥作用，包括医学影像、自然景观、工业检测等等。它的强大性能和zero-shot能力使得SAM成为了一个强大的工具，为各种图像分割任务提供了有力的支持。

## 总结和局限性分析

## 感谢聆听

个人主页:

[https://itmorn.github.io](https://link.zhihu.com/?target=https%3A//itmorn.github.io/)

欢迎访问我的主页，进行体系化的学习或者与我建立联系。有新内容更新时，会第一时间在主页更新。

[Read in Cubox](https://cubox.pro/web/card/7244236899362014662)
