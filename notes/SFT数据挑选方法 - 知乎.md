# SFT数据挑选方法

[zhuanlan.zhihu.com](https://zhuanlan.zhihu.com/p/22529462474)深度人工dazed阿巴阿巴阿巴关注他

目录

收起

数据质量

MoDS

DEITA

CaR

数据多样性

MoDS

DEITA

CaR

数据必要性

IFD

MoDS

参考

大模型的[SFT数据清洗](https://zhida.zhihu.com/search?content_id=253528286&content_type=Article&match_order=1&q=SFT%E6%95%B0%E6%8D%AE%E6%B8%85%E6%B4%97&zhida_source=entity)，主要包含三个维度：数据质量、数据多样性和数据必要性。

* 数据质量：需要对数据质量进行挑选，去除有问题或低质的数据。
* 数据多样性：覆盖更大范围、更多样的数据，可以从指令和回答角度。
* 数据必要性：挑选模型所需的数据，而不是模型本身已经能处理的数据。

接下来主要整理不同清洗方法在这三方面的做法。

**总结如下：**

* **数据质量：**
  * 使用[奖励模型](https://zhida.zhihu.com/search?content_id=253528286&content_type=Article&match_order=1&q=%E5%A5%96%E5%8A%B1%E6%A8%A1%E5%9E%8B&zhida_source=entity)对数据进行打分，可以是现成的reward模型，也可以是自己收集高低质量数据训练的reward模型，也可以是用chatgpt打分。
  * 使用大模型对数据从各个角度（准确性、指令遵循、预期表达）打分。
  * 对数据进行打标，根据标签的数量和复杂度进行挑选。
  * 使用困惑度度量
  * 根据长度进行度量
* **数据多样性：**
  * 抽取表征，对数据进行聚类，在一个簇内的数据，也可以用质量评分进行挑选。
  * 抽取表征，使用K-Center-Greedy类似的方法不断挑选不同的数据，直到数据数量达到要求
  * 也可以使用打标签的方式，选择不同标签的数据
* **数据必要性：**
  * 计算IFD值
  * 让模型尝试回答，并度量回答的质量

## 数据质量

### MoDS

使用OpenAssistant的[reward-model-debertav3-large-v2](https://link.zhihu.com/?target=https%3A//huggingface.co/OpenAssistant/reward-model-deberta-v3-large-v2)模型，将问题和回答送到该模型得到奖励分数，当分数高于 <math xmlns="http://www.w3.org/1998/Math/MathML"> α </math>\\alpha 时，就认为是高质量数据。

### DEITA

这里主要度量了指令的复杂性和回答的质量评分。

**指令的复杂性**

这里罗列的对指令复杂性的评估方式有：

* Random Selection：随机选择样本。
* Instruction Length：按照指令的长度计算复杂性。
* Perplexity：通过预训练模型计算回复的困惑度作为复杂性指标，困惑值越大意味着数据样本越难。
* Direct Scoring：利用ChaGPT给指令的复杂性打分。
* Instruction Node：利用ChatGPT将指令转换成语义树，通过树的节点数作为复杂性指标。
* Instag Complexity：利用ChatGPT对部分数据进行打标签，再训练一个Llama模型，再利用训练后的Llama模型对全量数据预测，标签越多说明数据约复杂。
* IFD：[指令跟随难度](https://link.zhihu.com/?target=https%3A//mp.weixin.qq.com/s/zU-mmn91UhS0x8NoX2757g)作为复杂性指标。

而DEITA的方式是：

* 挑选一个小规模数据（2k）
* 采用WizardLM模型的方法，通过添加约束、深化、具体化和增加推理步骤等技术来增强原始指令的复杂性
* 将由指令I生成的所有指令全都丢给ChatGPT，让他对这些指令进行打分排序
* 将ChatGPT打分排序的结果，训练LLama1-7B模型，让该模型学会打分

**回答质量评分**

这里罗列的对指令复杂性的评估方式有：

* Random Selection：随机选择样本。
* Response Length：采用输出长度作为质量评估指标。
* Direct Scoring：利用ChatGPT直接评估对特定指令输出结果的准确性。

而DEITA的方式和上面相似：

* 挑选一个小规模数据（2k）
* 通过特殊的提示词利用ChatGPT对数据的回复部分进行改写，主要是增强回复的有用性、相关性、丰富深度、创造力和提供额外的细节描述。
* 将由回答R生成的所有回答全都丢给ChatGPT，让他对这些回答进行打分排序
* 将ChatGPT打分排序的结果，训练LLama1-7B模型，让该模型学会打分

### CaR

* 使用CoachLM的专家审核数据，有修改前低质量的数据，也有修改后的高质量数据
* 使用Sentence BERT对数据进行分类，区分出低质量和高质量数据

## 数据多样性

### MoDS

使用BERT模型抽取数据的特征，再使用K-Center-Greedy算法找出目前样本中和目前所有中心点最远的那个点，作为新的中心点。（参考自\[3\]）
![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fpic4.zhimg.com%2Fv2-49a44bc6d6c5006c1725beca8e6537b1_1440w.jpg&valid=false)

### DEITA

主要步骤为：

1. 对数据集中的所有数据，计算复杂性评分和质量评分，将复杂性评分\*质量分数作为综合评分
2. 将数据按照综合评分排序
3. 使用LLama1-13B模型抽取数据向量
4. 逐个抽取数据x，计算x与保留数据底池中其他样本最小的余弦相似度
5. 保留相似度低于t的数据x
6. 挑选数据，直到保留数据底池的数据量达到阈值

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fpica.zhimg.com%2Fv2-f7a2a08f2521d8fedc7be0548d9d4ce0_1440w.jpg&valid=false)

### CaR

* 使用sentence-transformers抽取指令的向量
* 利用PCA降维
* 使用K-Means进行聚类，k=178
* 对每个簇中的样本进行打分
* 挑选打分在topn的数据

## 数据必要性

### IFD

我认为IFD主要是从数据必要性出发的。首先微调base模型使其具备初步的IF能力（将数据使用K-Means聚成100个簇，每个簇挑选10条数据，共1000条微调模型）。然后使用该模型计算**IFD指标** <math xmlns="http://www.w3.org/1998/Math/MathML"> s θ ( A \| Q ) = 1 N ∑ i = 1 N log ⁡ P ( w i A \| Q , w 1 A , w 2 A , ... , w i − 1 A ; θ ) s θ ( A ) = 1 N ∑ i = 1 N log ⁡ P ( w i A \| w 1 A , ... , w i − 1 A ; θ ) . r θ ( Q , A ) = s θ ( A \| Q ) s θ ( A ) </math>s_{\\theta}(A\|Q) = \\frac{1}{N} \\sum_{i=1}\^{N} \\log P(w_i\^A \| Q, w_1\^A, w_2\^A, \\ldots, w_{i-1}\^A; \\theta) \\\\ s_{\\theta}(A) = \\frac{1}{N} \\sum_{i=1}\^{N} \\log P(w_i\^A \| w_1\^A, \\ldots, w_{i-1}\^A; \\theta). \\\\ r_{\\theta}(Q, A) = \\frac{s_{\\theta}(A\|Q)}{s_{\\theta}(A)}

其中， <math xmlns="http://www.w3.org/1998/Math/MathML"> s θ ( A \| Q ) </math>s_\\theta(A\|Q) 表示在给定问题时回答的困惑度， <math xmlns="http://www.w3.org/1998/Math/MathML"> s θ ( A ) </math>s_\\theta(A) 表示单纯度量回答的困惑度。 <math xmlns="http://www.w3.org/1998/Math/MathML"> r θ ( Q , A ) </math>r_\\theta(Q,A) 就表示两者的比值

* <math xmlns="http://www.w3.org/1998/Math/MathML"> s θ ( A \| Q ) </math>s_\\theta(A\|Q) 高， <math xmlns="http://www.w3.org/1998/Math/MathML"> s θ ( A ) </math>s_\\theta(A) 低，表示模型很难根据Q生成A，但是单独生成A缺比较容易。说明模型对于Q的指令跟随能力较差。++主要想要这部分数据++。
* <math xmlns="http://www.w3.org/1998/Math/MathML"> s θ ( A \| Q ) </math>s_\\theta(A\|Q) 低， <math xmlns="http://www.w3.org/1998/Math/MathML"> s θ ( A ) </math>s_\\theta(A) 高，表示模型可以很容易从Q生成A，但是单独生成A比较困难，说明Q中包含生成A的信息，并且模型能利用该信息进行回答。说明模型对该指令处理较好。不需要这部分数据进行训练。
* <math xmlns="http://www.w3.org/1998/Math/MathML"> s θ ( A \| Q ) </math>s_\\theta(A\|Q) 高， <math xmlns="http://www.w3.org/1998/Math/MathML"> s θ ( A ) </math>s_\\theta(A) 高，表示模型生成A就是很困难，可能A中的数据有问题。不需要这部分数据进行训练。
* <math xmlns="http://www.w3.org/1998/Math/MathML"> s θ ( A \| Q ) </math>s_\\theta(A\|Q) 低， <math xmlns="http://www.w3.org/1998/Math/MathML"> s θ ( A ) </math>s_\\theta(A) 低，表示模型生成A很容易，说明模型对于Q的指令跟随能力很好。

所以这里挑选IFD指标较高的数据进行训练。但是我觉得如果一个A很合理， <math xmlns="http://www.w3.org/1998/Math/MathML"> s θ ( A ) </math>s_\\theta(A) 很低，但数据质量问题导致Q和A关联不大，即很难从Q生成A，则这部分脏数据也会被挑选出来。比如Q是计算1+2的结果，A是结果为10，明显是错误的，但是可能会被挑选出来。

### MoDS

步骤为：

* 使用多样性过滤过的数据微调模型
* 使用该模型对高质量数据进行推理
* 使用奖励模型计算推理结果的奖励值，当奖励值低于 <math xmlns="http://www.w3.org/1998/Math/MathML"> β </math>\\beta 时，认为模型无法回答好该问题，就保留该数据。
* 对于保留的数据，进行多样性筛选，得到最终数据。

## 参考

1. IFD：[刘聪NLP：如何从数据集中自动识别高质量的指令数据-IFD指标的使用](https://zhuanlan.zhihu.com/p/658128530)
2. MoDS：[刘聪NLP：大模型微调技巧 \| 高质量指令数据筛选方法-MoDS](https://zhuanlan.zhihu.com/p/671183709)
3. [AI蜗牛车：K-Center-Greedy算法讲解和python实现](https://zhuanlan.zhihu.com/p/711917766)
4. DEITA：[刘聪NLP：DEITA-大模型指令微调的数据高效筛选方法](https://zhuanlan.zhihu.com/p/675928711)
5. CaR：[刘聪NLP：指令微调数据的高效筛选方法-排序\&聚类-CaR方法](https://zhuanlan.zhihu.com/p/687775223)

[Read in Cubox](https://cubox.pro/web/card/7311391596988074687)
