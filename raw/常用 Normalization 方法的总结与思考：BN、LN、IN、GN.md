---
id: "7128378225880728235"
cubox_url: https://cubox.pro/web/card/7128378225880728235
url: https://mp.weixin.qq.com/s/_o0Wa_1KVSa98bYDFA_bQA
tags:
  - DeepLearning
  - 面试
---
# 常用 Normalization 方法的总结与思考：BN、LN、IN、GN

常用 Normalization 方法的总结与思考：BN、LN、IN、GN

[Read in Cubox](https://cubox.pro/web/card/7128378225880728235)  
[Read Original](https://mp.weixin.qq.com/s/_o0Wa_1KVSa98bYDFA_bQA)  

---


---

\## 📖 正文全文

# 常用 Normalization 方法的总结与思考：BN、LN、IN、GN

[mp.weixin.qq.com](https://mp.weixin.qq.com/s/_o0Wa_1KVSa98bYDFA_bQA)G-kdom 深度学习技术前沿


点击上方，选择**星标** 或**置顶**，不定期资源大放送![图片](https://image.cubox.pro/cardImg/2023112617030934128/77227.jpg?imageMogr2/quality/90/ignore-error/1)！
> 阅读大概需要6分钟![图片](https://image.cubox.pro/cardImg/2023112617031067909/26424.jpg?imageMogr2/quality/90/ignore-error/1)  
>
> Follow小博主，每天更新前沿干货![图片](https://image.cubox.pro/cardImg/2023112617031068571/97510.jpg?imageMogr2/quality/90/ignore-error/1)

来自｜知乎 作者｜G-kdom   


链接｜https://zhuanlan.zhihu.com/p/72589565

本文仅供学习参考，如有侵权，请联系后台删除。

常用的Normalization方法主要有：Batch Normalization（BN，2015年）、Layer Normalization（LN，2016年）、Instance Normalization（IN，2017年）、Group Normalization（GN，2018年）。它们都是从激活函数的输入来考虑、做文章的，以不同的方式**对激活函数的输入进行 Norm**的。

我们将输入的**feature map shape** 记为**\[N, C, H, W\]**，其中N表示batch size，即N个样本；C表示通道数；H、W分别表示特征图的高度、宽度。这几个方法主要的区别就是在：

1. BN是在batch上，对N、H、W做归一化，而保留通道 C 的维度。BN对较小的batch size效果不好。BN适用于固定深度的前向神经网络，如CNN，不适用于RNN；

2. LN在通道方向上，对C、H、W归一化，主要对RNN效果明显；

3. IN在图像像素上，对H、W做归一化，用在风格化迁移；

4. GN将channel分组，然后再做归一化。

![图片](https://image.cubox.pro/cardImg/2023112617031052640/41340.jpg?imageMogr2/quality/90/ignore-error/1) 每个子图表示一个特征图，其中N为批量，C为通道，（H，W）为特征图的高度和宽度。通过蓝色部分的值来计算均值和方差，从而进行归一化。

**如果把特征图** **比喻成一摞书，这摞书总共有 N 本，每本有 C 页，每页有 H 行，每行 有W 个字符。**

1. BN 求均值时，相当于把这些书按页码一一对应地加起来（例如第1本书第36页，第2本书第36页......），再除以每个页码下的字符总数：N×H×W，因此可以把 BN 看成求"平均书"的操作（注意这个"平均书"每页只有一个字），求标准差时也是同理。

2. LN 求均值时，相当于把每一本书的所有字加起来，再除以这本书的字符总数：C×H×W，即求整本书的"平均字"，求标准差时也是同理。

3. IN 求均值时，相当于把一页书中所有字加起来，再除以该页的总字数：H×W，即求每页书的"平均字"，求标准差时也是同理。

4. GN 相当于把一本 C 页的书平均分成 G 份，每份成为有 C/G 页的小册子，求每个小册子的"平均字"和字的"标准差"。

\## **一、 Batch Normalization, BN**

**论文链接** ：https://arxiv.org/pdf/1502.03167.pdf

**为什么要进行BN呢？**

（1）在深度神经网络训练的过程中，通常以输入网络的每一个mini-batch进行训练，这样每个batch具有不同的分布，使模型训练起来特别困难。

（2）Internal Covariate Shift (ICS) 问题：在训练的过程中，激活函数会改变各层数据的分布，随着网络的加深，这种改变（差异）会越来越大，使模型训练起来特别困难，收敛速度很慢，会出现梯度消失的问题。

**BN的主要思想** ：针对每个神经元，**使数据在进入激活函数之前，沿着通道计算每个batch的均值、方差，'强迫'数据保持均值为0，方差为1的正态分布**，避免发生梯度消失。具体来说，就是把第1个样本的第1个通道，加上第2个样本第1个通道 ...... 加上第 N 个样本第1个通道，求平均，得到通道 1 的均值（注意是除以 N×H×W 而不是单纯除以 N，最后得到的是一个代表这个 batch 第1个通道平均值的数字，而不是一个 H×W 的矩阵）。求通道 1 的方差也是同理。对所有通道都施加一遍这个操作，就得到了所有通道的均值和方差。

**BN的使用位置**：全连接层或卷积操作之后，激活函数之前。

**BN算法过程：**

*
  沿着通道计算每个batch的均值
*
  沿着通道计算每个batch的方差
*
  做归一化
*
  加入缩放和平移变量 和

![图片](https://image.cubox.pro/cardImg/2023112617031073226/23040.jpg?imageMogr2/quality/90/ignore-error/1)

其中 是一个很小的正值，比如 。**加入缩放和平移变量的原因是：保证每一次数据经过归一化后还保留原有学习来的特征，同时又能完成归一化操作，加速训练。**这两个参数是用来学习的参数。

**BN的作用：**

（1）允许较大的学习率；

（2）减弱对初始化的强依赖性

（3）保持隐藏层中数值的均值、方差不变，让数值更稳定，为后面网络提供坚实的基础；

（4）有轻微的正则化作用（相当于给隐藏层加入噪声，类似Dropout）

**BN存在的问题：**

（1）每次是在一个batch上计算均值、方差，如果**batch size太小**，则计算的均值、方差不足以代表整个数据分布。

（2）**batch size太大**：会超过内存容量；需要跑更多的epoch，导致总训练时间变长；会直接固定梯度下降的方向，导致很难更新。

\## **二、 Layer Normalization, LN**

**论文链接** ：https://arxiv.org/pdf/1607.06450v1.pdf

针对BN不适用于深度不固定的网络（sequence长度不一致，如RNN），**LN对深度网络的某一层的所有神经元的输入**按以下公式进行normalization操作。
![图片](https://image.cubox.pro/cardImg/2023112617031076122/66224.jpg?imageMogr2/quality/90/ignore-error/1)

LN中同层神经元的输入拥有相同的均值和方差，不同的输入样本有不同的均值和方差。

对于特征图 ，LN 对每个样本的 C、H、W 维度上的数据求均值和标准差，保留 N 维度。其均值和标准差公式为：

![图片](https://image.cubox.pro/cardImg/2023112617031078490/34975.jpg?imageMogr2/quality/90/ignore-error/1)

Layer Normalization (LN) 的一个优势是**不需要批训练，在单条数据内部就能归一化**。LN不依赖于batch size和输入sequence的长度，因此可以用于batch size为1和RNN中。LN用于RNN效果比较明显，但是在CNN上，效果不如BN。

\## **三、 Instance Normalization, IN**

**论文链接** ：https://arxiv.org/pdf/1607.08022.pdf

IN针对图像像素做normalization，最初用于图像的风格化迁移。在图像风格化中，生成结果主要依赖于某个图像实例，feature map 的各个 channel 的均值和方差会影响到最终生成图像的风格。所以对整个batch归一化不适合图像风格化中，因而对H、W做归一化。可以加速模型收敛，并且保持每个图像实例之间的独立。

对于 ，IN 对每个样本的 H、W 维度的数据求均值和标准差，保留 N 、C 维度，也就是说，它只在 channel 内部求均值和标准差，其公式如下：
![图片](https://image.cubox.pro/cardImg/2023112617031031530/38323.jpg?imageMogr2/quality/90/ignore-error/1)

\## **四、 Group Normalization, GN**

**论文链接** ：https://arxiv.org/pdf/1803.08494.pdf

**GN是为了解决BN对较小的mini-batch size效果差的问题。**GN适用于占用显存比较大的任务，例如图像分割。对这类任务，可能 batch size 只能是个位数，再大显存就不够用了。而当 batch size 是个位数时，BN 的表现很差，因为没办法通过几个样本的数据量，来近似总体的均值和标准差。GN 也是独立于 batch 的，它是 LN 和 IN 的折中。

**GN的主要思想：** 在 channel 方向 group，然后每个 group 内做 Norm，计算 的均值和方差，这样就与batch size无关，不受其约束。

**具体方法：**GN 计算均值和标准差时，把每一个样本 feature map 的 channel 分成 G 组，每组将有 C/G 个 channel，然后将这些 channel 中的元素求均值和标准差。各组 channel 用其对应的归一化参数独立地归一化。

![图片](https://image.cubox.pro/cardImg/2023112617031163070/25843.jpg?imageMogr2/quality/90/ignore-error/1)

伪代码如下：
![图片](https://image.cubox.pro/cardImg/2023112617031112612/74838.jpg?imageMogr2/quality/90/ignore-error/1)

代码如下：



        def` `GroupNorm`(x, gamma, beta, G`=16`):`

            # x_shape:[N, C, H, W]
            results = 0.
            eps = 1e-5
            x = np.reshape(x, (x.shape[0], G, x.shape[1]/16, x.shape[2], x.shape[3]))

            x_mean = np.mean(x, axis=(2, 3, 4), keepdims=True)
            x_var = np.var(x, axis=(2, 3, 4), keepdims=True0)
            x_normalized = (x - x_mean) / np.sqrt(x_var + eps)
            results = gamma * x_normalized + beta
            return results




\## **总结**

我们将feature map shape 记为\[N, C, H, W\]。如果把特征图 比喻成一摞书，这摞书总共有 N 本，每本有 C 页，每页有 H 行，每行 有W 个字符**。**
![图片](https://image.cubox.pro/cardImg/2023112617031138713/93152.jpg?imageMogr2/quality/90/ignore-error/1)   

1. BN是在batch上，对N、H、W做归一化，而保留通道 C 的维度。BN 相当于把这些书按页码一一对应地加起来，再除以每个页码下的字符总数：N×H×W。

2. LN在通道方向上，对C、H、W归一化。LN 相当于把每一本书的所有字加起来，再除以这本书的字符总数：C×H×W。  

3. IN在图像像素上，对H、W做归一化。IN 相当于把一页书中所有字加起来，再除以该页的总字数：H×W。

4. GN将channel分组，然后再做归一化。GN 相当于把一本 C 页的书平均分成 G 份，每份成为有 C/G 页的小册子，对每个小册子做Norm。

另外，还需要注意它们的映射参数 和 的区别：对于**BN，IN，GN， 其** **和** **都是维度等于通道数 C 的向量** 。而对于**LN，其** **和** **都是维度等于 normalized_shape 的矩阵**。

最后，**BN 和 IN 可以**设置参数：momentum和track_running_stats来获得在**整体数据上更准确的均值和标准差** 。**LN 和 GN 只能计算当前 batch 内数据的真实均值和标准差**。

\## 推荐阅读

* [【重磅】斯坦福李飞飞《注意力与Transformer》总结，84页ppt开放下载！](http://mp.weixin.qq.com/s?__biz=MzU2NDExMzE5Nw==&mid=2247508426&idx=1&sn=9a42baca7791f713931a637d4cd078f2&chksm=fc4d1b88cb3a929e5b95aebd23eec166ab91a8205e4f5a3b1f07d15f06c4a0a823a50cd8a105&scene=21\#wechat_redirect)

* [一文总结微软研究院Transformer霸榜模型三部曲！](http://mp.weixin.qq.com/s?__biz=MzU2NDExMzE5Nw==&mid=2247511722&idx=1&sn=8e73570336b2d67948a6bce5b55d9c0d&chksm=fc4d14e8cb3a9dfeac9f8322d250d1e043075df0717b2737ff8bc0f67c96ec5b029f7b876ce6&scene=21\#wechat_redirect)

* [Swin Transformer为主干，清华等提出MoBY自监督学习方法，代码已开源](http://mp.weixin.qq.com/s?__biz=MzU2NDExMzE5Nw==&mid=2247511391&idx=3&sn=ebd6abeb7c0826282971c7cb51ec4828&chksm=fc4d171dcb3a9e0b5343da2ddf9e18aef0d40b5a1e780c225254257a91f61e0aa0c12583d595&scene=21\#wechat_redirect)

* [加性注意力机制！清华和MSRA提出Fastformer：又快又好的Transformer新变体！](http://mp.weixin.qq.com/s?__biz=MzU2NDExMzE5Nw==&mid=2247513374&idx=3&sn=fd9a233c81ed4a418fd0f1e28a38241c&chksm=fc4d0f5ccb3a864add9734c312f184605c190da7a9bae0d21a0c54306201f9a22155c77ddcd7&scene=21\#wechat_redirect)  

* [MLP进军下游视觉任务！目标检测与分割领域最新MLP架构研究进展！](http://mp.weixin.qq.com/s?__biz=MzU2NDExMzE5Nw==&mid=2247512636&idx=1&sn=2fee147c2616b51e0e2465c130e7f3c8&chksm=fc4d087ecb3a8168a2441f048ea37312175f3ea1a34bcb86c3be0e2f3406e55ec98d4066e699&scene=21\#wechat_redirect)

* [周志华教授：如何做研究与写论文？（附完整的PPT全文）](http://mp.weixin.qq.com/s?__biz=MzU2NDExMzE5Nw==&mid=2247512463&idx=1&sn=a218eefa56f1e432f75f9b87c9289ed7&chksm=fc4d0bcdcb3a82dbd17b9089131cef536ed0c7a4848faf06448392883dbd197f6e00c07fdb9b&scene=21\#wechat_redirect)

* [都2021 年了，AI大牛纷纷离职！各家大厂的 AI Lab 现状如何？](http://mp.weixin.qq.com/s?__biz=MzU2NDExMzE5Nw==&mid=2247512154&idx=1&sn=11914ba4ed058074e0170ff1e3774b1f&chksm=fc4d0a18cb3a830ede163e66f7b125b49ff1b4cbdbf39258c3c6a585e19e9c26aa18a5a1907a&scene=21\#wechat_redirect)  

* [常用 Normalization 方法的总结与思考：BN、LN、IN、GN](http://mp.weixin.qq.com/s?__biz=MzU2NDExMzE5Nw==&mid=2247510537&idx=2&sn=805a08e4388d2f020eb35cadacdd642f&chksm=fc4d104bcb3a995dcd8341d30d4e756fe36dae9ceaf8ecb1a26776df13fa9b6a7baf10aebf2b&scene=21\#wechat_redirect)  

* [注意力可以使MLP完全替代CNN吗？未来有哪些研究方向？](http://mp.weixin.qq.com/s?__biz=MzU2NDExMzE5Nw==&mid=2247509411&idx=1&sn=20e63c8f160bc7929bc052455ea80603&chksm=fc4d1fe1cb3a96f73501568926cc5d7e7442f3bc466fb52ee606c27e316c3d0538f083908d7e&scene=21\#wechat_redirect)

**欢迎大家加入DLer-**计算机视觉\&Transformer**群！**  

大家好，这是**计算机视觉\&Transformer**论文分享群里，群里会第一时间发**布最新的Transformer前沿论文解读及交流分享会** ，主要设计方向有：**图像分类、Transformer、目标检测、目标跟踪、点云与语义分割、GAN、超分辨率、视频超分、人脸检测与识别、动作行为与时空运动、模型压缩和量化剪枝、迁移学习、人体姿态估计****等内容。**

**进群请备注：** **研究方向+学校/公司+昵称** **（如Transformer****+上交+小明）**

![图片](https://image.cubox.pro/cardImg/2023112617031145486/87961.jpg?imageMogr2/quality/90/ignore-error/1)

👆**长按识别，邀请您进群！**

[Read in Cubox](https://cubox.pro/web/card/7128378225880728235)
