---
id: "7204006255453539017"
cubox_url: https://cubox.pro/web/card/7204006255453539017
url: https://mp.weixin.qq.com/s/mBAhShN4Z0FLg_r8wYXdAQ
tags:
  - Skill/data-analysis
  - Skill/python
  - 面试
---
# 一图胜千言｜图解Pandas常用操作！



[Read in Cubox](https://cubox.pro/web/card/7204006255453539017)  
[Read Original](https://mp.weixin.qq.com/s/mBAhShN4Z0FLg_r8wYXdAQ)  

---


---

\## 📖 正文全文

# 喜欢此内容的人还喜欢

[mp.weixin.qq.com](https://mp.weixin.qq.com/s/mBAhShN4Z0FLg_r8wYXdAQ)Python人工智能技术


点击上方"**Python人工智能技术** "关注，星标或者置顶   


22点24分准时推送，第一时间送达

后台回复"**大礼包**"，送你特别福利  

> 编辑：乐乐 \| 来自：网络

[Pythn人工智能技术(ID:coder_experience) 1089期推文](http://mp.weixin.qq.com/s?__biz=MzI0MzU2NzQ1OA==&mid=2247489525&idx=1&sn=26e9ce9d935a845d03ce4a3d30ebc975&chksm=e96a49f8de1dc0eeda78a0f1fa1ab74bfa13222fecbb924f52e59b59cd8b431d6e0fd00cc1cb&scene=21\#wechat_redirect)

上一篇：[刚刚，被 GPT-4o 价格劝退了！](http://mp.weixin.qq.com/s?__biz=MzI0MzU2NzQ1OA==&mid=2247527532&idx=2&sn=0d50bfcb666a89adff16e93ef2ef5d3a&chksm=e9693261de1ebb7714272a9aba9213af8a075fecffa32c525bfc2ed82d51bb39063587a68f6c&scene=21\#wechat_redirect)

**大家好，我是Python人工智能技术**

Pandas 展示  

请看下表:

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2FvQr6oPKZqgt8icrjbaiap2iaKdtDRUXicicKibehWbmjtEeic2DqiaVzavHBEmASYDnZRtG4NloCByHYhTXjxFiaXIbZ7zg%2F640%3Fwx_fmt%3Dpng%26tp%3Dwxpic%26wxfrom%3D5%26wx_lazy%3D1%26wx_co%3D1&valid=false)

它描述了一个在线商店的不同产品线，共有四种不同的产品。与前面的例子不同，它可以用NumPy数组或Pandas DataFrame表示。但让我们看一下它的一些常见操作。

\## 1. 排序

使用Pandas按列排序更具可读性，如下所示:

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2FvQr6oPKZqgt8icrjbaiap2iaKdtDRUXicicKibBjsB8w26LBItpic9gibEJjicC2ib10IkzAxwnxwBD1X3ibBibdUVtTCstwrA%2F640%3Fwx_fmt%3Dpng%26tp%3Dwxpic%26wxfrom%3D5%26wx_lazy%3D1%26wx_co%3D1&valid=false)

这里argsort(a\[:，1\])计算使a的第二列按升序排序的排列，然后a\[...\]相应地对a的行重新排序。Pandas可以一步完成。

\## 2.按多列排序

如果我们需要使用weight列来对价格列进行排序，情况会变得更糟。这里有几个例子来说明我们的观点:

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2FvQr6oPKZqgt8icrjbaiap2iaKdtDRUXicicKibborrQZIzemegcHP6QwPf04pnIrsyrfqjyVTkNO0BGEXYt6mG8dwBog%2F640%3Fwx_fmt%3Dpng%26tp%3Dwxpic%26wxfrom%3D5%26wx_lazy%3D1%26wx_co%3D1&valid=false)

在NumPy中，我们先按重量排序，然后再按价格排序。稳定排序算法保证第一次排序的结果不会在第二次排序期间丢失。NumPy还有其他实现方法，但没有一种方法像Pandas那样简单优雅。

\## 3. 添加一列

使用Pandas添加列在语法和架构上要好得多。下面的例子展示了如何操作:

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2FvQr6oPKZqgt8icrjbaiap2iaKdtDRUXicicKibXqalg4ibSIPXfj2KBhrHkZxsUtamtspu7X3eZquZYhvLAHZVwVwiawIw%2F640%3Fwx_fmt%3Dpng%26tp%3Dwxpic%26wxfrom%3D5%26wx_lazy%3D1%26wx_co%3D1&valid=false)

Pandas不需要像NumPy那样为整个数组重新分配内存;它只是添加了对新列的引用，并更新了列名的\` registry \`。

\## 4. 快速元素搜索

在NumPy数组中，即使你查找的是第一个元素，你仍然需要与数组大小成正比的时间来查找它。使用Pandas，你可以索引你期望被查询最多的列，并将搜索时间减少到一个常量。

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2FvQr6oPKZqgt8icrjbaiap2iaKdtDRUXicicKibFBFgNudLWnIlZ9WdwbCnu852Gic6icYoRfjU3EAJU54XygJhibmicf0j8w%2F640%3Fwx_fmt%3Dpng%26tp%3Dwxpic%26wxfrom%3D5%26wx_lazy%3D1%26wx_co%3D1&valid=false)

index列有以下限制。

* 它需要内存和时间来构建。

* 它是只读的(需要在每次追加或删除操作后重新构建)。

* 这些值不需要是唯一的，但是只有当元素是唯一的时候加速才会发生。

* 它需要预热:第一次查询比NumPy稍慢，但后续查询明显快得多。

\## 5. 按列连接（join）

如果你想从另一张表中获取基于同一列的信息，NumPy几乎没有任何帮助。Pandas更好，特别是对于1:n的关系。

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2FvQr6oPKZqgt8icrjbaiap2iaKdtDRUXicicKibsTZt21raPstGufk5esYaP6fXN692uU5TFxPpFKakwUrm94jia41JCxg%2F640%3Fwx_fmt%3Dpng%26tp%3Dwxpic%26wxfrom%3D5%26wx_lazy%3D1%26wx_co%3D1&valid=false)

Pandas join具有所有熟悉的"内"、"左"、"右"和"全外部"连接模式。

\## 按列分组

数据分析中的另一个常见操作是按列分组。例如，要获得每种产品的总销量，你可以这样做:

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2FvQr6oPKZqgt8icrjbaiap2iaKdtDRUXicicKibEl7aHtd5N8TdrqiaN7WYqnVdfBtSQJm00SGzDvdtJZz4ocomwJg9LCg%2F640%3Fwx_fmt%3Dpng%26tp%3Dwxpic%26wxfrom%3D5%26wx_lazy%3D1%26wx_co%3D1&valid=false)

除了sum之外，Pandas还支持各种聚合函数:mean、max、min、count等。

\## 7. 数据透视表

Pandas最强大的功能之一是"枢轴"表。这有点像将多维空间投影到二维平面上。

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2FvQr6oPKZqgt8icrjbaiap2iaKdtDRUXicicKibwLjZbdSRu1hJIBsAZKwYLt2ksaQiaoLQzF2wlUn9pGxhOME7bsHKOrg%2F640%3Fwx_fmt%3Dpng%26tp%3Dwxpic%26wxfrom%3D5%26wx_lazy%3D1%26wx_co%3D1&valid=false)

虽然用NumPy当然可以实现它，但这个功能没有开箱即用，尽管它存在于所有主要的关系数据库和电子表格应用程序(Excel，WPS)中。

Pandas用df.pivot_table将分组和旋转结合在一个工具中。

简而言之，NumPy和Pandas的两个主要区别如下:

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2FvQr6oPKZqgt8icrjbaiap2iaKdtDRUXicicKibWiaVHCXOQNHGZI4DCtrRMreUwM4xfpyLxhRqQV2f0BJVquZa6OLjR9w%2F640%3Fwx_fmt%3Dpng%26tp%3Dwxpic%26wxfrom%3D5%26wx_lazy%3D1%26wx_co%3D1&valid=false)

现在，让我们看看这些功能是否以性能损失为代价。

\## Pandas速度

我在Pandas的典型工作负载上对NumPy和Pandas进行了基准测试:5-100列，10³- 10⁸行，整数和浮点数。下面是1行和1亿行的结果:

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2FvQr6oPKZqgt8icrjbaiap2iaKdtDRUXicicKibkndpdDNpIl9eIsnqOhdFMNKthfHWVGryr3vFgK7cGmAgzNZbHQFibVg%2F640%3Fwx_fmt%3Dpng%26tp%3Dwxpic%26wxfrom%3D5%26wx_lazy%3D1%26wx_co%3D1&valid=false)

看起来在每一次操作中，Pandas都比NumPy慢!

当列数增加时，情况不会改变(可以预见)。至于行数，依赖关系(在对数尺度下)如下所示:

![](https://image.cubox.pro/cardImg/45f9l5jsoxklv6kq4m1ujytioycraricd9w6ovlmmw4axmtaxo?imageMogr2/quality/90/ignore-error/1)

对于小数组(少于100行)，Pandas似乎比NumPy慢30倍，对于大数组(超过100万行)则慢3倍。

怎么可能呢?也许是时候提交一个功能请求，建议Pandas通过df.column.values.sum()重新实现df.column.sum()了?这里的values属性提供了访问底层NumPy数组的方法，性能提升了3 \~ 30倍。

答案是否定的。Pandas在这些基本操作方面非常缓慢，因为它正确地处理了缺失值。Pandas需要NaNs (not-a-number)来实现所有这些类似数据库的机制，比如分组和旋转，而且这在现实世界中是很常见的。在Pandas中，我们做了大量工作来统一所有支持的数据类型对NaN的使用。根据定义(在CPU级别上强制执行)，nan+anything会得到nan。所以

    >>> np.sum([1, np.nan, 2])
    nan

但是

    >>> pd.Series([1, np.nan, 2]).sum()
    3.0

一个公平的比较是使用np.nansum代替np.sum,用np.nanmean而不是np.mean等等。突然间......  

![](https://image.cubox.pro/cardImg/3i3jd1l80s6fofapk9ww32zabj20behb0la7pw4tk0zrolbf6?imageMogr2/quality/90/ignore-error/1)

对于超过100万个元素的数组，Pandas的速度是NumPy的1.5倍。对于较小的数组，它仍然比NumPy慢15倍，但通常情况下，无论操作在0.5 ms还是0.05 ms内完成都没有太大关系------无论如何它都是快速的。
> 最重要的是，如果您100%确定列中没有缺失值，则使用df.column.values.sum()而不是df.column.sum()可以获得x3-x30的性能提升。在存在缺失值的情况下，Pandas的速度相当不错，甚至在巨大的数组(超过10个同质元素)方面优于NumPy。

\## 第二部分. Series 和 Index

![](https://image.cubox.pro/cardImg/cnqrx8zbxz8zvvyoh75enihhpog5pvmt87pv6b7370yy5hq6q?imageMogr2/quality/90/ignore-error/1)

Series是NumPy中的一维数组，是表示其列的DataFrame的基本组成部分。尽管与DataFrame相比，它的实际重要性正在降低(你可以在不知道Series是什么的情况下完美地解决许多实际问题)，但如果不首先学习Series和Index，你可能很难理解DataFrame是如何工作的。

在内部，Series将值存储在普通的NumPy vector中。因此，它继承了它的优点(紧凑的内存布局、快速的随机访问)和缺点(类型同质、缓慢的删除和插入)。最重要的是，Series允许使用类似于字典的结构index通过label访问它的值。标签可以是任何类型(通常是字符串和时间戳)。它们不必是唯一的，但唯一性是提高查找速度所必需的，许多操作都假定唯一性。

![](https://image.cubox.pro/cardImg/22g6fvt9zbpffe7hbwxehqaze89kkycrcv5ut0c40d4b1sfqav?imageMogr2/quality/90/ignore-error/1)

如你所见，现在每个元素都可以通过两种替代方式寻址:通过\` label \`(=使用索引)和通过\` position \`(=不使用索引):

![](https://image.cubox.pro/cardImg/2u2c9m41rzz9xhpyn2pvrdi2gjv9ahacqfyjad1ovfhplef91g?imageMogr2/quality/90/ignore-error/1)

按"位置"寻址有时被称为"位置索引"，这只是增加了混淆。

一对方括号是不够的。特别是:

* S\[2:3\]不是解决元素2最方便的方式

* 如果名称恰好是整数，s\[1:3\]就会产生歧义。它可能意味着名称1到3包含或位置索引1到3不包含。

为了解决这些问题，Pandas还有两种"风格"的方括号，你可以在下面看到:

![](https://image.cubox.pro/cardImg/ebsujwnktr983fs18w05yxufs7susnztq8gaz1y9z4y48df9p?imageMogr2/quality/90/ignore-error/1)

.loc总是使用标号，并且包含间隔的两端。

.iloc总是使用"位置索引"并排除右端。

使用方括号而不是圆括号的目的是为了访问Python的切片约定:你可以使用单个或双冒号，其含义是熟悉的start:stop:step。像往常一样，缺少开始(结束)意味着从序列的开始(到结束)。step参数允许使用s.iloc\[::2\]引用偶数行，并使用s\['Paris':'Oslo':-1\]以相反的顺序获取元素。

它们还支持布尔索引(使用布尔数组进行索引)，如下图所示:

![](https://image.cubox.pro/cardImg/66x1e1xhkgsa7rki4ckn6299429ch7iujtr05yi6f1xbek59i2?imageMogr2/quality/90/ignore-error/1)

你可以在下图中看到它们如何支持\` fancy indexing \`(用整数数组进行索引):

![](https://image.cubox.pro/cardImg/5fhpw01616a34157s7dkv8dor4uv6jsp3jktmiksbkpycydtn6?imageMogr2/quality/90/ignore-error/1)

Series最糟糕的地方在于它的视觉表现:出于某种原因，它没有一个很好的富文本外观，所以与DataFrame相比，它感觉像是二等公民:

![](https://image.cubox.pro/cardImg/38ortrf8bv89mju9cb4nnzxefagh1yecghnuy2fu7v855ehod1?imageMogr2/quality/90/ignore-error/1)

我对这个Series做了补丁，让它看起来更好，如下所示:

![](https://image.cubox.pro/cardImg/bta4xff50ky2hws121vkulf49pio92sskayb8zosrmgci4jqt?imageMogr2/quality/90/ignore-error/1)

垂直线表示这是一个Series，而不是一个DataFrame。Footer在这里被禁用了，但它可以用于显示dtype，特别是分类类型。

您还可以使用pdi.sidebyside(obj1, obj2，...)并排显示多个Series或dataframe:

![](https://image.cubox.pro/cardImg/391yhn8j3yd5z91lyyxklg4scy9967yrp1gfipgceu0wx2xgnd?imageMogr2/quality/90/ignore-error/1)

pdi(代表pandas illustrated)是github上的一个开源库，具有本文所需的这个和其他功能。要使用它，就要写

    pip install pandas-illustrated

\## 索引(Index)

负责通过标签获取元素的对象称为index。它非常快:无论你有5行还是50亿行，你都可以在常量时间内获取一行数据。

指数是一个真正的多态生物。默认情况下，当创建一个没有索引的序列(或DataFrame)时，它会初始化为一个惰性对象，类似于Python的range()。和range一样，几乎不使用任何内存，并且与位置索引无法区分。让我们用下面的代码创建一个包含一百万个元素的序列:

    >>> s = pd.Series(np.zeros(10**6))
    >>> s.index
    RangeIndex(start=0, stop=1000000, step=1)
    >>> s.index.memory_usage()       # in bytes
    128                    # the same as for Series([0.])

现在，如果我们删除一个元素，索引隐式地转换为类似于dict的结构，如下所示:

    >>> s.drop(1, inplace=True)
    >>> s.index
    Int64Index([     0,      2,      3,      4,      5,      6,      7,
                ...
                999993, 999994, 999995, 999996, 999997, 999998, 999999],
               dtype='int64', length=999999)
    >>> s.index.memory_usage()
    7999992

该结构消耗8Mb内存!为了摆脱它，回到轻量级的类range结构，添加如下代码:

    >>> s.reset_index(drop=True, inplace=True)
    >>> s.index
    RangeIndex(start=0, stop=999999, step=1)
    >>> s.index.memory_usage()
    128

如果你不熟悉Pandas，你可能想知道为什么Pandas自己没有做到这一点?好吧，对于非数字标签，有一点很明显:为什么(以及如何)Pandas在删除一行后，会重新标记所有后续的行?对于数值型标签，答案就有点复杂了。

首先，正如我们已经看到的，Pandas允许您纯粹按位置引用行，因此，如果您想在删除第3行之后定位第5行，则可以无需重新索引(这就是iloc的作用)。

其次，保留原始标签是一种与过去时刻保持联系的方法，就像"保存游戏"按钮一样。假设您有一个100x1000000的大表，需要查找一些数据。你正在一个接一个地进行几次查询，每次都缩小了搜索范围，但只查看了一小部分列，因为同时查看数百个字段是不切实际的。现在您已经找到感兴趣的行，您希望在原始表中查看有关它们的所有信息。数字索引可以帮助您立即获得它，而无需任何额外的努力。

一般来说，在索引中保持值的唯一性是一个好主意。例如，在索引中存在重复值时，查找速度不会得到提升。Pandas不像关系型数据库那样有"唯一约束"(该功能仍然是实验性的)，但它有检查索引中的值是否唯一的函数，并以各种方式消除重复。

有时，一列不足以唯一标识一行。例如，同一个名字的城市有时会碰巧出现在不同的国家，甚至是同一个国家的不同地区。所以(城市，州)是一个比城市更好的标识一个地方的候选者。在数据库中，这被称为"复合主键"。在Pandas中，它被称为多索引(参见下面的第4部分)，索引中的每一列都被称为"级别"。

索引的另一个重要特性是不可变。与DataFrame中的普通列不同，你不能就地更改它。索引中的任何更改都涉及从旧索引中获取数据，修改它，并将新数据作为新索引重新附加。通常情况下，它是透明的，这就是为什么不能直接写df.City.name = ' city '，而必须写一个不那么明显的df.rename(columns={' A ': ' A '}， inplace=True)

Index有一个名称(在MultiIndex的情况下，每个级别都有一个名称)。不幸的是，这个名称在Pandas中没有得到充分使用。一旦你在索引中包含了这一列，就不能再使用df了。不再使用列名表示法，并且必须恢复为可读性较差的df。指数还是更通用的df。loc对于多索引，情况更糟。一个明显的例外是df。Merge -你可以通过名称指定要合并的列，无论它是否在索引中。

同样的索引机制用于标记dataframe的行和列，以及序列。

\## 按值查找元素

Series内部由一个NumPy数组和一个类似数组的结构index组成，如下所示:

![](https://image.cubox.pro/cardImg/e7gdc36o1xhv1vjuy7xnm70umihv7eec1t2jluz2cly8qjqo7?imageMogr2/quality/90/ignore-error/1)

Index提供了一种通过标签查找值的方便方法。那么如何通过值查找标签呢?

    s.index[s.tolist().find(x)]           # faster for len(s) < 1000
    s.index[np.where(s.values==x)[0][0]]  # faster for len(s) > 1000

我编写了find()和findall()两个简单的封装器，它们运行速度快(因为它们会根据序列的大小自动选择实际的命令)，而且使用起来更方便。代码如下所示:

    >>> import pdi
    >>> pdi.find(s, 2)
    'penguin'
    >>> pdi.findall(s, 4)
    Index(['cat', 'dog'], dtype='object')

\## 缺失值

Pandas开发人员特别关注缺失值。通常，你通过向read_csv提供一个标志来接收一个带有NaNs的dataframe。否则，可以在构造函数或赋值运算符中使用None(尽管不同数据类型的实现略有不同，但它仍然有效)。这张图片有助于解释这个概念:

![](https://image.cubox.pro/cardImg/4j2ijbe8rz8sh7ukmj8meub8xe3198vza2rokzvv93axw7sz1x?imageMogr2/quality/90/ignore-error/1)

你可以使用NaNs做的第一件事是了解你是否有NaNs。从上图可以看出，isna()生成了一个布尔数组，而.sum()给出了缺失值的总数。

现在你知道了它们的存在，你可以选择用常量值填充它们或通过插值来一次性删除它们，如下所示:

![](https://image.cubox.pro/cardImg/5j4mkaf0hw37seztfb3cmgd7t0tg78r2viu7lm61py6hwuutqn?imageMogr2/quality/90/ignore-error/1)

另一方面，你可以继续使用它们。大多数Pandas函数会很高兴地忽略缺失值，如下图所示:

![](https://image.cubox.pro/cardImg/2vtwz4958a2lp8jndz7t5f03f4cl8tw39fuc95ufhgquj86wm3?imageMogr2/quality/90/ignore-error/1)

更高级的函数(median、rank、quantile等)也可以做到这一点。

算术运算与索引对齐:

![](https://image.cubox.pro/cardImg/4hcj63pl9mqo4m350nfkwv00i20d01dc6rcl7xv8dgdnh8uzyj?imageMogr2/quality/90/ignore-error/1)

如果索引中存在非唯一值，则结果不一致。不要对索引不唯一的序列使用算术运算。

\## 比较

比较有缺失值的数组可能会比较棘手。下面是一个例子:

    >>> np.all(pd.Series([1., None, 3.]) == 
               pd.Series([1., None, 3.]))
    False
    >>> np.all(pd.Series([1, None, 3], dtype='Int64') == 
               pd.Series([1, None, 3], dtype='Int64'))
    True
    >>> np.all(pd.Series(['a', None, 'c']) == 
               pd.Series(['a', None, 'c']))
    False

为了正确地比较nan，需要用数组中一定没有的元素替换nan。例如，使用-1或∞:

    >>> np.all(s1.fillna(np.inf) == s2.fillna(np.inf))   # works for all dtypes
    True

或者，更好的做法是使用NumPy或Pandas的标准比较函数:

    >>> s = pd.Series([1., None, 3.])
    >>> np.array_equal(s.values, s.values, equal_nan=True)
    True
    >>> len(s.compare(s)) == 0
    True

这里，compare函数返回一个差异列表(实际上是一个DataFrame)， array_equal则直接返回一个布尔值。

当比较混合类型的DataFrames时，NumPy比较失败(issue \#19205)，而Pandas工作得很好。如下所示:

    >>> df = pd.DataFrame({'a': [1., None, 3.], 'b': ['x', None, 'z']})
    >>> np.array_equal(df.values, df.values, equal_nan=True)
    TypeError
    <...>
    >>> len(df.compare(df)) == 0
    True

\## 追加、插入、删除

虽然Series对象被认为是size不可变的，但它可以在原地追加、插入和删除元素，但所有这些操作都是:

* 慢，因为它们需要为整个对象重新分配内存和更新索引。

* 非常不方便。

下面是插入值的一种方式和删除值的两种方式:

![](https://image.cubox.pro/cardImg/2qsb3gxxe4qxwjp5kh7joedfcl9c12vll2xodxdqf1uzpnrt4k?imageMogr2/quality/90/ignore-error/1)

第二种删除值的方法(通过drop)比较慢，并且在索引中存在非唯一值时可能会导致复杂的错误。

Pandas有df.insert方法，但它只能将列(而不是行)插入到dataframe中(并且对series不起作用)。

添加和插入的另一种方法是使用iloc对DataFrame进行切片，应用必要的转换，然后使用concat将其放回。我实现了一个名为insert的函数，可以自动执行这个过程:

![](https://image.cubox.pro/cardImg/50g7uvri4v0t6wskf03zul5uqug5hxvhzp6cp5sxborc2e8oif?imageMogr2/quality/90/ignore-error/1)

注意(就像在df.insert中一样)插入位置由位置0\<=i\<=len(s)指定，而不是索引中元素的标签。如下所示:

![](https://image.cubox.pro/cardImg/58cox3rkbpy11w3tnmf33yco7f34d4tdsfhce69hd7la4lt2a6?imageMogr2/quality/90/ignore-error/1)

要按元素的名称插入，可以合并pdi。用pdi查找。插入，如下所示:

![](https://image.cubox.pro/cardImg/42tqqn306q9h6jyz9e6a3dhnvt5w61kt1kdmbjqk2bjbedfh8b?imageMogr2/quality/90/ignore-error/1)

请注意，unlikedf.insert、pdi.insert返回一个副本，而不是原地修改Series/DataFrame

\## 统计数据

Pandas提供了全方位的统计函数。它们可以让您了解百万元素序列或DataFrame中的内容，而无需手动滚动数据。

所有Pandas统计函数都会忽略NaNs，如下所示:

![](https://image.cubox.pro/cardImg/2u38e0pqmqnqekue2ql9e1069bise8zpi8p311gjb4zruvar8q?imageMogr2/quality/90/ignore-error/1)

注意，Pandas std给出的结果与NumPy std不同，如下所示:

    >>> pd.Series([1, 2]).std()
    0.7071067811865476
    >>> pd.Series([1, 2]).values.std()
    0.5

这是因为NumPy std默认使用N作为分母，而Pandas std默认使用N-1作为分母。两个std都有一个名为ddof (\` delta degrees of freedom \`)的参数，NumPy默认为0,Pandas默认为1，这可以使结果一致。N-1是你通常想要的值(在均值未知的情况下估计样本的偏差)。这里有一篇维基百科的文章详细介绍了贝塞尔的修正。

由于序列中的每个元素都可以通过标签或位置索引访问，因此argmin (argmax)有一个姐妹函数idxmin (idxmax)，如下图所示:

![](https://image.cubox.pro/cardImg/3jydbtiigm5tn2wvo4rosejrhctd6tpqzkjh8k2so9zam32odn?imageMogr2/quality/90/ignore-error/1)

下面是Pandas的自描述统计函数供参考:

* std:样本标准差

* var，无偏方差

* sem，均值的无偏标准误差

* quantile分位数，样本分位数(s.quantile(0.5)≈s.median())

* oode是出现频率最高的值

* 默认为Nlargest和nsmallest，按出现顺序排列

* diff，第一个离散差分

* cumsum 和 cumprod、cumulative sum和product

* cummin和cummax，累积最小值和最大值

以及一些更专业的统计函数:

* pct_change，当前元素与前一个元素之间的变化百分比

* skew偏态，无偏态(三阶矩)

* kurt或kurtosis，无偏峰度(四阶矩)

* cov、corr和autocorr、协方差、相关和自相关

* rolling滚动窗口、加权窗口和指数加权窗口

\## 重复数据

在检测和处理重复数据时需要特别小心，如下图所示:

![](https://image.cubox.pro/cardImg/38cjcb02xo6zlej77gjuep0gjr1l70j8wtxycvjovqobenfr7h?imageMogr2/quality/90/ignore-error/1)

drop_duplicates和duplication可以保留最后一次出现的副本，而不是第一次出现的副本。

请注意，s.a uint()比np快。唯一性(O(N) vs O(NlogN))，它会保留顺序，而不会返回排序结果。独特的。

缺失值被视为普通值，有时可能会导致令人惊讶的结果。  

![](https://image.cubox.pro/cardImg/5ne2u9hlixv7q59b2zsi2szecmst1kyi5u1cv7f9gwy8wv3t54?imageMogr2/quality/90/ignore-error/1)

如果你想排除nan，需要显式地这样做。在这个例子中，是s.l opdropna().is_unique == True。

还有一类单调函数，它们的名字是自描述的:

* s.is_monotonic_increasing ()

* s.is_monotonic_decreasing ()

* s._strict_monotonic_increasing ()

* s._string_monotonic_decreasing ()

* s.is_monotonic()。这是意料之外的，出于某种原因，这是s.is_monotonic_increasing()。它只对单调递减序列返回False。

\## 分组

在数据处理中，一个常见的操作是计算一些统计量，不是针对整个数据集，而是针对其中的某些组。第一步是通过提供将一系列(或一个dataframe)分解为组的标准来定义一个"智能对象"。这个\`智能对象\`没有立即的表示，但可以像Series一样查询它，以获得每个组的某个属性，如下图所示:

![](https://image.cubox.pro/cardImg/59b6j4hgfaafenh22iv6g0g67x63w1yhg66ydvwkrb3zcd77vf?imageMogr2/quality/90/ignore-error/1)

在这个例子中，我们根据数值除以10的整数部分将序列分成三组。对于每个组，我们请求每个组中元素的和、元素的数量以及平均值。

除了这些聚合函数，您还可以根据特定元素在组中的位置或相对值访问它们。如下所示:

![](https://image.cubox.pro/cardImg/2zvc7wdbdty9ab0312gl8rdrr2ws0nmjtu2v3bbzh8gqzgvr9s?imageMogr2/quality/90/ignore-error/1)

你也可以使用g.ag (\['min'， 'max'\])一次调用计算多个函数，或者使用g.c describe()一次显示一堆统计函数。

如果这些还不够，你还可以通过自己的Python函数传递数据。它可以是:

一个函数f，它接受一个组x(一个Series对象)并生成一个值(例如sum())与g.eapply (f)一起使用。

一个函数f，它接受一个组x(一个Series对象)，并与g.transform(f)生成一个大小与x相同的Series对象(例如cumsum())。

![](https://image.cubox.pro/cardImg/26jbcvru0ogbzcciitgi1y83mk605ufnxx3z13xzs9g3n998q0?imageMogr2/quality/90/ignore-error/1)

在上面的例子中，输入数据是有序的。groupby不需要这样做。实际上，如果分组中的元素不是连续存储的，它也同样有效，因此它更接近于collections.defaultdict，而不是itertools.groupby。它总是返回一个没有重复项的索引。

![](https://image.cubox.pro/cardImg/dfoc1jgn52zyy9sp9vd6664n0gk5l17x3j2ixiobr6iqut19k?imageMogr2/quality/90/ignore-error/1)

与defaultdict和关系数据库GROUP BY子句不同，Pandas groupby按组名对结果进行排序。可以用sort=False来禁用它。

免责声明:实际上，g.apply(f)比上面描述的更通用:

* 如果f(x)返回与x大小相同的序列，它可以模拟transform

* 如果f(x)返回一系列不同大小或不同的dataframe，则会得到一个具有相应多索引的序列。

但文档警告说，这些使用方法可能比相应的transform和agg方法慢，所以要小心。

\## 第三部分. DataFrames

![](https://image.cubox.pro/cardImg/3lh0gttjnks9150ztj3gyuydilgor7xoz6gsp3bou67ezpw8wj?imageMogr2/quality/90/ignore-error/1)

Pandas的主要数据结构是DataFrame。它将一个二维数组与它的行和列的标签捆绑在一起。它由一系列对象组成(具有共享索引)，每个对象表示一列，可能具有不同的dtype。

\## 读写CSV文件

构造DataFrame的一种常用方法是读取csv(逗号分隔值)文件，如下图所示:

![](https://image.cubox.pro/cardImg/1bvljm6rfuokhwl9c3c3pcx1809zdin2ut4xy5ds5nwn22e4wl?imageMogr2/quality/90/ignore-error/1)

pd.read_csv()函数是一个完全自动化且可疯狂定制的工具。如果你只想学习Pandas的一件事，那就学习使用read_csv------它会有回报的:)。

下面是一个解析非标准的.csv文件的例子:

![](https://image.cubox.pro/cardImg/2fekt1yddf9h6f17j4igffeyqq1b1xuuuzqhjytdurzauu8v1j?imageMogr2/quality/90/ignore-error/1)

以及一些简要描述:

![](https://image.cubox.pro/cardImg/59rmo5s62ko1noespgqx94hwytp5li8dj24qpxzkwbjhryv6gp?imageMogr2/quality/90/ignore-error/1)

因为CSV没有严格的规范，所以有时需要一些试错才能正确地阅读它。read_csv最酷的地方在于它会自动检测很多东西:

* 列名和类型

* 布尔值的表示

* 缺失值的表示等。

与其他自动化一样，你最好确保它做了正确的事情。如果在Jupyter单元中简单地编写df的结果碰巧太长(或太不完整)，您可以尝试以下操作:

* df.head(5)或df\[:5\]显示前5行

* df.dtypes返回列的类型

* df.shape返回行数和列数

* Df.info()汇总所有相关信息

将一列或几列设置为索引是一个好主意。下图展示了这个过程:

![](https://image.cubox.pro/cardImg/1vwdz04ar2hfbfthh3qm4egm7wf47516jjvwzzlxuj78ayt2nb?imageMogr2/quality/90/ignore-error/1)

Index在Pandas中有很多用途:

* 算术运算按索引对齐

* 它使按该列进行的查找更快，等等。

所有这些都是以较高的内存消耗和不太明显的语法为代价的。

\## 构建DataFrame

另一种选择是从内存中已经存储的数据中构建一个dataframe。它的构造函数非常全能，可以转换(或包装)任何类型的数据:  

![](https://image.cubox.pro/cardImg/67ubmcyoffg0yhwtcwu8n6p9b77cctz753b9wg0wqzo4ovm6ck?imageMogr2/quality/90/ignore-error/1)

在第一种情况下，在没有行标签的情况下，Pandas用连续的整数标记行。在第二种情况下，它对行和列都进行了相同的操作。为Pandas提供列的名称总是一个好主意，而不是整数标签(使用columns参数)，有时也可以提供行(使用index参数，尽管rows听起来可能更直观)。这张图片会有帮助:

![](https://image.cubox.pro/cardImg/3gwygqos9wkjo2s7c3db7izexlkvolwb7qujuneai54v8fi6yg?imageMogr2/quality/90/ignore-error/1)

不幸的是，无法在DataFrame构造函数中为索引列设置名称，所以唯一的选择是手动指定，例如，df.index.name = '城市名称'

下一种方法是使用NumPy向量组成的字典或二维NumPy数组构造一个DataFrame:

![](https://image.cubox.pro/cardImg/4xkdi1k5ip48bvdch8ffqzal43zy361m4mdxjowzqq538v0b6f?imageMogr2/quality/90/ignore-error/1)

请注意，在第二种情况下，人口数量的值被转换为浮点数。实际上，它在之前的构建NumPy数组时就发生过。这里需要注意的另一件事是，从2D NumPy数组构建dataframe默认是视图。这意味着改变原始数组中的值会改变dataframe，反之亦然。另外，它节省了内存。

第一种情况(NumPy向量组成的字典)也可以启用这种模式，设置copy=False即可。不过，它非常脆弱。简单的操作就可以把它变成副本而不需要通知。

另外两个(不太有用的)创建DataFrame的选项是:

* 从一个dict列表(其中每个dict表示一行，其键是列名，其值是相应的单元格值)

* 来自由Series组成的dict(其中每个Series表示一列;默认情况下，可以让它返回一个copy=False的视图)。

如果你"动态"注册流数据，最好的选择是使用列表的dict或列表的列表，因为Python会透明地在列表末尾预分配空间，以便快速追加。NumPy数组和Pandas dataframes都不能做到这一点。另一种可能性(如果你事先知道行数)是用DataFrame(np.zeros)之类的东西手动预分配内存。

\## DataFrames的基本操作

DataFrame最好的地方(在我看来)是你可以:

* 轻松访问其列，如d.area返回列值(或者df\[' Area '\]------适用于包含空格的列名)

* 将列作为自变量进行操作，例如使用afterdf. population /= 10\*\*6人口以百万计存储，下面的命令根据现有列中的值创建一个名为\` density \`的新列。更多信息见下图:

![](https://image.cubox.pro/cardImg/4k2wme9bc2ozs0cd3zq0o1dgoo0ln9ypsaddgpj0cgl5a6f86n?imageMogr2/quality/90/ignore-error/1)

注意，创建新列时，即使列名中不包含空格，也必须使用方括号。

此外，你可以对不同dataframe中的列使用算术操作，只要它们的行具有有意义的标签，如下所示:

![](https://image.cubox.pro/cardImg/4gi0ugume6obc4rtmbq10kgi0lo6dao78o1ro4biub32bs32yd?imageMogr2/quality/90/ignore-error/1)

\## 索引DataFrames

正如我们在本系列中已经看到的，普通的方括号不足以满足索引的所有需求。你不能通过名称访问行，不能通过位置索引访问不相交的行，你甚至不能引用单个单元格，因为df\['x'， 'y'\]是为多索引保留的!

![](https://image.cubox.pro/cardImg/5ufix78zn0sdebimsd9c9y93d8u0vbh6kv25o16pylyrgk04g?imageMogr2/quality/90/ignore-error/1)

为了满足这些需求，dataframes，就像series一样，有两种可选的索引模式:按标签索引的loc和按位置索引的iloc。

![](https://image.cubox.pro/cardImg/1lcm5zzt7uwt9scmununv33n6g9hjsd510ckji9qn2xrmf5pvm?imageMogr2/quality/90/ignore-error/1)

在Pandas中，引用多行/多列是一个副本，而不是视图。但它是一种特殊的复制，允许赋值作为一个整体:

* df.loc\['a'\]=10 works (一行作为一个整体是一个可写的)

* df.loc\['a'\]\['A'\]=10 works (元素访问传播到原始df)

* df.loc\['a':'b'\] = 10 works (assigning to a subar将整个作品赋值给一个子数组)

* df.loc\['a':'b'\]\['A'\] = 10 doesn't (对其元素赋值不会).

在最后一种情况下，该值只会被设置在切片的副本上，而不会反映在原始df上(会相应地显示一个警告)。

根据不同的背景，有不同的解决方案:

1. 你想要改变原始的df。然后使用df。loc\[' a': ' b '， ' a'\] = 10

2. 你故意创建了一个副本，然后想要处理这个副本:df1 = df.loc\[' a ': ' b '\];df1\[' A '\]=10 # SettingWithCopy warning要在这种情况下消除警告，请使其成为一个真正的副本:df1 = df.loc\[' A ': ' b '\].copy();df1 \[A\] = 10

Pandas还支持一种方便的NumPy语法来进行布尔索引。

![](https://image.cubox.pro/cardImg/39urca7kw13r5tl8vaahv3fcu25javhei10ffmk8murdtbf8sj?imageMogr2/quality/90/ignore-error/1)

当使用多个条件时，必须将它们括起来，如下所示:

![](https://image.cubox.pro/cardImg/5eqsov7b89kpnvzafc5odoodmxm7ym8wqqszti41my82tqpmn3?imageMogr2/quality/90/ignore-error/1)

当你期望返回一个值时，需要特别注意。

![](https://image.cubox.pro/cardImg/4c9i2sdf3g6qd0fjt61c1wviy0ef52chhj1w4jgzu16m2285ar?imageMogr2/quality/90/ignore-error/1)

因为可能有多行匹配条件，所以loc返回一个序列。要从中得到标量值，你可以使用:

* float(s)或更通用的s.e item()，除非序列中只有一个值，否则都会引发ValueError

S.iloc\[0\]，仅在没有找到时引发异常;此外，它是唯一支持赋值的函数:df\[...\].Iloc\[0\] = 100，但当你想修改所有匹配时，肯定不需要它:df\[...\]= 100。

或者，你可以使用基于字符串的查询:

* df.query (' name = ="Vienna")

df.query('population\>1e6 and area\<1000')它们更短，适合多索引，并且逻辑操作符优先于比较操作符(=需要更少的括号)，但它们只能按行过滤，并且不能通过它们修改Dataframe。

几个第三方库允许你使用SQL语法直接查询dataframe (duckdb)，或者通过将dataframe复制到SQLite并将结果包装回Pandas objects (pandasql)来间接查询dataframe。不出所料，直接法更快。

\## DataFrame算术

你可以对dataframes、series和它们的组合应用普通操作，如加、减、乘、除、求模、幂等。

所有的算术运算都是根据行标签和列标签对齐的:

![](https://image.cubox.pro/cardImg/29b5cmd29muclofmc33w1rtxmyjl3ked1vo3kc9qd11lkwu1mc?imageMogr2/quality/90/ignore-error/1)

在dataframe和Series之间的混合操作中，Series(天知道为什么)表现得(和广播)像一个行向量，并相应地对齐:

![](https://image.cubox.pro/cardImg/39h2f0v3vmu5kkrhgnmp466cu4h8pvxcre16bghmc4sdja3pfq?imageMogr2/quality/90/ignore-error/1)

可能是为了与列表和一维NumPy向量保持一致(它们不按标签对齐，并被认为是一个简单的二维NumPy数组的DataFrame):

![](https://image.cubox.pro/cardImg/3jgxctdo08bvpolvi5inktvo93lvhgemwwcgiagim6ybz7y7y1?imageMogr2/quality/90/ignore-error/1)

因此，在不太幸运(也是最常见的!)的情况下，将一个dataframe除以列向量序列，你必须使用方法而不是操作符，如下所示:

![](https://image.cubox.pro/cardImg/5kk74bqjvilcdrxpuxhyfg2gcsrav6449c1m9od0gijqu43pl3?imageMogr2/quality/90/ignore-error/1)

由于这个有问题的决定，每当你需要在dataframe和列式序列之间执行混合操作时，你必须在文档中查找它(或记住它):

![](https://image.cubox.pro/cardImg/40y2zwiovjknjih07gcbe2t3rsvfsfamxwltajlxn1uikg3sfo?imageMogr2/quality/90/ignore-error/1)

\## 结合DataFrames

Pandas有三个函数，concat、merge和join，它们做同样的事情:将来自多个dataframe的信息合并为一个。但是每个工具的实现方式都略有不同，因为它们是为不同的用例量身定制的。

\## 垂直叠加

这可能是将两个或多个dataframe合并为一个的最简单方法:您获取第一个dataframe中的行，并将第二个dataframe中的行追加到底部。为了使其工作，这两个dataframe需要(大致)具有相同的列。这类似于NumPy中的vstack，正如你在图像中所看到的:

![](https://image.cubox.pro/cardImg/3eny80lw09ou8j7y794fkmargoe6u3l2ih3utpdhl3ec1n0yrw?imageMogr2/quality/90/ignore-error/1)

索引中有重复的值是不好的。你可能会遇到各种各样的问题(参见下面的\` drop \`示例)。即使你不关心索引，也要尽量避免出现重复的值:

* 要么使用reset_index=True参数

* 调用df.reset_index(drop=True)将行从0重新索引到len(df)-1，

* 使用keys参数可以解决MultiIndex的二义性(见下文)。

如果dataframe的列不能完美匹配(不同的顺序在这里不计算在内)，Pandas可以取列的交集(默认值kind='inner ')或插入nan来标记缺失值(kind='outer'):

![](https://image.cubox.pro/cardImg/593q3aiqzy18kh80pvmh6ftbxqvujkto7t5elun9tpds9228uw?imageMogr2/quality/90/ignore-error/1)

\## 水平叠加

concat也可以执行"水平"堆叠(类似于NumPy中的hstack):

![](https://image.cubox.pro/cardImg/590dc27zknvifg7h8n183ay3ja5i2wtrp5o8krcmcgpnci7wla?imageMogr2/quality/90/ignore-error/1)

join比concat更可配置:特别是，它有五种连接模式，而concat只有两种。详情请参阅下面的"1:1关系连接"部分。

\## 基于多指数的数据叠加

如果行标签和列标签一致，concat可以执行与垂直堆叠类似的多索引(就像NumPy中的dstack):

![](https://image.cubox.pro/cardImg/5mbalivivg0r8ec24i8yn0akvcs1f0zrni1hyqwmczm8zo8fz1?imageMogr2/quality/90/ignore-error/1)

如果行和/或列部分重叠，Pandas将相应地对齐名称，这很可能不是你想要的。下面的图表可以帮助你将这个过程可视化:

![](https://image.cubox.pro/cardImg/52lhb9fv908g1ejllkzdkam7ct4s2erz79s554oqs6t5xd8ogz?imageMogr2/quality/90/ignore-error/1)

一般来说，如果标签重叠，这意味着dataframe在某种程度上彼此相关，实体之间的关系最好使用关系数据库的术语来描述。

\## 1:1 连接的关系

![](https://image.cubox.pro/cardImg/16g2lbvwq215utbf7qgmmyfmc27na8tn5klynajqlr1a41egoc?imageMogr2/quality/90/ignore-error/1)

当同一组对象的信息存储在几个不同的DataFrame中时，你希望将它们合并为一个DataFrame。

如果要合并的列不在索引中，则使用merge。

![](https://image.cubox.pro/cardImg/666xq2l9eppc2z8rxwwt6xginj2er2u8ym4uves1gzxmyln4rg?imageMogr2/quality/90/ignore-error/1)

它所做的第一件事是丢弃索引中的任何内容。然后执行联结操作。最后，将结果从0重新编号为n-1。

如果列已经在索引中，则可以使用join(这只是merge的别名，将left_index或right_index设置为True，并设置不同的默认值)。

![](https://image.cubox.pro/cardImg/5q4csh9138vpg650vhl81cdo0l1rfbzcc7l7v3uq5y8zfisbcs?imageMogr2/quality/90/ignore-error/1)

从这个简化的例子中可以看出(参见上面的全外连接)，与关系型数据库相比，Pandas对行顺序的处理相当轻松。左外联结和右外联结比内外联结更容易预测(至少在需要合并的列中有重复值之前是这样)。因此，如果你想保证行顺序，就必须显式地对结果进行排序。

\## 1:n 连接的关系

![](https://image.cubox.pro/cardImg/3ghq6jt35d2nmyk9que7d9ope8r8pe58yqw7eyzmxl1eeh74qm?imageMogr2/quality/90/ignore-error/1)

这是数据库设计中使用最广泛的关系，表A中的一行(例如"State")可以与表B中的几行(例如城市)相关联，但表B中的每一行只能与表A中的一行相关联(即一个城市只能处于一种状态，但一个状态由多个城市组成)。

就像1:1关系一样，在Pandas中连接一对1:n相关的表，你有两种选择。如果要合并的列或者不在索引中，并且可以丢弃碰巧在两张表的索引中都存在的列，则使用merge。下面的例子会有所帮助:

![](https://image.cubox.pro/cardImg/1nhz60mcyw835xjwqrhetpwcsl3hxjmh13fyll5gwotyyjzeap?imageMogr2/quality/90/ignore-error/1)

正如我们已经看到的，merge对行顺序的处理没有Postgres严格:所有声明的语句，保留的键顺序只适用于left_index=True和/或right_index=True(这就是join的别名)，并且只在要合并的列中没有重复值的情况下。这就是为什么join有一个sort参数。

现在，如果要合并的列已经在右侧DataFrame的索引中，可以使用join(或者merge with right_index=True，这是完全相同的事情):

![](https://image.cubox.pro/cardImg/1gyyn6ztwngxp2s4unup885qkt0kx3jkg1a2fel2xyr9l92c51?imageMogr2/quality/90/ignore-error/1)

这次Pandas保留了左DataFrame的索引值和行顺序。

注意:注意，如果第二个表有重复的索引值，你最终将在结果中得到重复的索引值，即使左表索引是唯一的!

有时，合并的dataframe具有同名的列。merge和join都有解决二义性的方法，但语法略有不同(默认情况下merge会用\` _x \`， \` _y \`来解决，而join会抛出异常)，如下图所示:

![](https://image.cubox.pro/cardImg/a4man2wz65s5sp5o76m99538arn78aft8u9679hliqk23ueub?imageMogr2/quality/90/ignore-error/1)

总结:

* 合并非索引列上的连接，连接要求列被索引

* merge丢弃左DataFrame的索引，join保留它

* 默认情况下，merge执行内联结，join执行左外联结

* 合并不保持行顺序

* Join可以保留它们(有一些限制)

* join是合并的别名，left_index=True和/或right_index=True

\## 多个连接

如上所述，当对两个dataframe(如df.join(df1))运行join时，它充当了合并的别名。但是join也有一个\` multiple join \`模式，它只是concat(axis=1)的别名。

![](https://image.cubox.pro/cardImg/2p7mb1jll0njpcia7126i87pwsiihsdmhh4wx8wtluymg78a2f?imageMogr2/quality/90/ignore-error/1)

与普通模式相比，该模式有一些限制:

* 它没有提供解析重复列的方法

* 它只适用于1:1关系(索引到索引连接)。

因此，多个1:n关系应该一个接一个地连接。仓库\` panda -illustrated \`也提供了一个辅助方法，如下所示:

![](https://image.cubox.pro/cardImg/5ocs6yr1d6zbycbjn3clfyivnmthml9w2qaevgn5lrp8r9pal3?imageMogr2/quality/90/ignore-error/1)

pdi.join是Join的一个简单包装器，它接受on、how和后缀参数，以便您可以在一个命令中进行多个联结。与原始的关联操作一样，关联的是属于第一个DataFrame的列，其他DataFrame根据它们的索引进行关联操作。

\## 插入和删除

由于DataFrame是列的集合，因此将这些操作应用到行上比应用到列上更容易。例如，插入一列总是在原地完成，而插入一行总是会生成一个新的DataFrame，如下所示:

![](https://image.cubox.pro/cardImg/wyooxhkwaq4lzke7vdheziypaok7l4t4l0o7y41ua7ez1lyry?imageMogr2/quality/90/ignore-error/1)

删除列通常不用担心，除了del df\['D'\]和del df。D则没有(Python级别的限制)。

![](https://image.cubox.pro/cardImg/2hbtsobg2wk6q6fs94kcjs9i7do2b69zscscorjvwg0c7hgyi2?imageMogr2/quality/90/ignore-error/1)

使用drop删除行非常慢，如果原始标签不是唯一的，可能会导致复杂的bug。下图将帮助解释这个概念:

![](https://image.cubox.pro/cardImg/4z7eqp2z8ivdrs3ny76b5frllm40mlbitec0dxhvi9ptatzfg9?imageMogr2/quality/90/ignore-error/1)

一种解决方案是使用ignore_index=True，它告诉concat在连接后重置行名称:

![](https://image.cubox.pro/cardImg/45l4xcb798u4gxvq3sm2tgj8es6wgjuwrskd8na75m21i4dnu4?imageMogr2/quality/90/ignore-error/1)

在这种情况下，将name列设置为索引将有所帮助。但对于更复杂的滤波器，它不会。

另一种快速、通用、甚至可以处理重复行名的解决方案是索引而不是删除。为了避免显式地否定条件，我写了一个(只有一行代码的)自动化程序。

![](https://image.cubox.pro/cardImg/2y6sjfbay1iz0fzjw1t96t7zopalpam60jqk5e9i2tbv5zlago?imageMogr2/quality/90/ignore-error/1)

\## 分组

这个操作已经在Series部分详细描述过了。但是DataFrame的groupby在此基础上有一些特定的技巧。

首先，你可以使用一个名称来指定要分组的列，如下图所示:

![](https://image.cubox.pro/cardImg/3zvm98aqgnj56740sgghmk4j1zc6q638g571hcf5lhnk2eu443?imageMogr2/quality/90/ignore-error/1)

如果没有as_index=False, Pandas将进行分组的列指定为索引。如果这不是我们想要的，可以使用reset_index()或指定as_index=False。

通常，数据框中的列比你想在结果中看到的多。默认情况下，Pandas会对所有远端可求和的东西进行求和，因此你需要缩小选择范围，如下所示:

![](https://image.cubox.pro/cardImg/3okf3u0m8ga3ujcv4u47ufxtmai1wkfgijccgd6g47wo1ur9lc?imageMogr2/quality/90/ignore-error/1)

注意，当对单个列求和时，你将得到一个Series而不是DataFrame。如果出于某种原因，你想要一个DataFrame，你可以:

* 使用双括号:df.groupby('product')\[\['quantity'\]\].sum()

* 显式转换:df.groupby('product')\['quantity'\].sum().to_frame()

切换到数值索引也会创建一个DataFrame:

* df.groupby('product', as_index=False)\['quantity'\].sum()

* df.groupby('product')\['quantity'\].sum().reset_index()

但是，尽管外观不寻常，Series的行为就像DataFrames一样，所以可能对pdi.patch_series_repr()进行"整容"就足够了。

显然，不同的列在分组时表现不同。例如，对数量求和完全没问题，但对价格求和就没有意义了。使用。agg可以为不同的列指定不同的聚合函数，如下图所示:

![](https://image.cubox.pro/cardImg/5u0maevpfozeze7wtgptfeq0ad5vbsp59esleiuwadi890hgo5?imageMogr2/quality/90/ignore-error/1)

或者，你可以为一列创建多个聚合函数:

![](https://image.cubox.pro/cardImg/3gurm76x2ipmua5maccpa0erl7kronx8ebb98627n7jtdvtxhp?imageMogr2/quality/90/ignore-error/1)

或者，为了避免繁琐的列重命名，你可以这样做:

![](https://image.cubox.pro/cardImg/3wog8rde7x0w34a9s3m77b77ejfka35xi0cvk0pn6mty4knzfj?imageMogr2/quality/90/ignore-error/1)

有时，预定义的函数不足以产生所需的结果。例如，在平均价格时使用权重会更好。你可以为此提供一个自定义函数。与Series不同的是，该函数可以访问组中的多个列(它以子dataframe作为参数)，如下所示:

![](https://image.cubox.pro/cardImg/gdxdt6gwjvydcvpvz8z56yzpodqbsedvy8nn9cv323oaajpb6?imageMogr2/quality/90/ignore-error/1)

不幸的是，你不能把预定义的聚合和几个列级的自定义函数结合在一起，比如上面的那个，因为agg只接受单列级的用户函数。单列范围的用户函数唯一可以访问的是索引，这在某些情况下很方便。例如，那天香蕉以5折的价格出售，如下图所示:

![](https://image.cubox.pro/cardImg/55ffdn5aze6i2cdr20s0ma8demwu9ss44mvw3x9uipmwueah7c?imageMogr2/quality/90/ignore-error/1)

为了从自定义函数中访问group by列的值，它事先已经包含在索引中。

通常，定制最少的函数可以获得最好的性能。为了提高速度:

* 通过g.apply()实现多列范围的自定义函数

* 通过g.agg()实现单列范围的自定义函数(支持使用Cython或Numba进行加速)

* 预定义函数(Pandas或NumPy函数对象，或其字符串名称)。

* 预定义函数(Pandas或NumPy函数对象，或其字符串名称)。

数据透视表(pivot table)是一种有用的工具，通常与分组一起使用，从不同的角度查看数据。

\## 旋转和\`反旋转\`

假设你有一个变量a，它依赖于两个参数i和j。有两种等价的方法将它表示为一个表:

![](https://image.cubox.pro/cardImg/3idw9yzvuedi0k2dwf4ahj7mlznlg0z9mw4apsnk817gcxtmh2?imageMogr2/quality/90/ignore-error/1)

当数据是"密集的"(当有很少的0元素)时，\` short \`格式更合适，而当数据是"稀疏的"(大多数元素为0，可以从表中省略)时，\` long \`格式更好。当有两个以上的参数时，情况会变得更加复杂。

当然，应该有一种简单的方法来转换这些格式。Pandas为此提供了一个简单方便的解决方案:数据透视表。

作为一个不那么抽象的例子，考虑下表中的销售数据。有两个客户购买了两种产品的指定数量最初，这个数据是短格式的。\`要将其转换为\`长格式\`，请使用df.pivot:

![](https://image.cubox.pro/cardImg/1gv08fes1b0zfh7f17mp8tdwbwes5fye96fgl1f8roh4rwv57f?imageMogr2/quality/90/ignore-error/1)

该命令丢弃了与操作无关的任何信息(索引、价格)，并将来自三个请求列的信息转换为长格式，将客户名称放入结果的索引中，将产品名称放入列中，将销售数量放入DataFrame的\` body \`中。

至于相反的操作，你可以使用stack。它将索引和列合并到MultiIndex中:

![](https://image.cubox.pro/cardImg/50k2fnzge6hucqy0cbprabtzdxtfxws2j6p0quu3kmh64ed8i4?imageMogr2/quality/90/ignore-error/1)

另一种选择是使用melt:

![](https://image.cubox.pro/cardImg/16vtiy66ojpkd9fw2h9pto8can1z1ozsd25hfou9xcljp6izur?imageMogr2/quality/90/ignore-error/1)

注意，melt以不同的方式对结果行进行排序。

Pivot丢失了结果的\` body \`的名称信息，因此无论是stack还是melt，我们都必须提醒pandas \` quantity \`列的名称。

在上面的例子中，所有的值都存在，但这不是必须的:

![](https://image.cubox.pro/cardImg/5dka2pfrwous58dxk1yx3inl43pcfod9t2xgkw4zg2ahp7128q?imageMogr2/quality/90/ignore-error/1)

分组值然后旋转结果的做法是如此常见，以至于groupby和pivot被捆绑在一个专用的函数(以及相应的DataFrame方法)数据透视表中:

* 如果没有columns参数，它的行为与groupby类似

* 当没有重复的行进行分组时，它的工作原理与pivot类似

* 否则，它会进行分组和旋转

![](https://image.cubox.pro/cardImg/p1hh8hy1dueuiva608da70184axoo2jsoufqay9f3uoy5i94u?imageMogr2/quality/90/ignore-error/1)

aggfunc参数控制哪一个聚合函数应该用于分组行(默认为均值)。

为了方便，pivot_table可以计算小计和合计:

![](https://image.cubox.pro/cardImg/xjht9a4mwzwhzewycilh2335dymb5k95zuaa7vae8q3b1ka2v?imageMogr2/quality/90/ignore-error/1)

一旦创建，pivot表就变成了一个普通的DataFrame，因此可以使用前面描述的标准方法查询它。

![](https://image.cubox.pro/cardImg/34vo2gimgyl48vpuhofzshkhy9ed84t8vbnp98ldb5aku80n81?imageMogr2/quality/90/ignore-error/1)

当使用多索引时，透视表特别方便。我们已经见过很多Pandas函数返回多索引DataFrame的例子。让我们仔细看看。

\## 第四部分. MultiIndex

![](https://image.cubox.pro/cardImg/2mbwadkibq656eeytrdpy7brcmsik64xtt4czpi40gj7o1pbze?imageMogr2/quality/90/ignore-error/1)

对于从未听说过Pandas的人来说，多索引（MultiIndex）最直接的用法是使用第二个索引列作为第一个索引列的补充，以唯一地标识每行。例如，为了消除来自不同州的城市的歧义，州的名字通常附加在城市的名字后面。例如，在美国大约有40个springfield(在关系型数据库中，它被称为复合主键)。

你可以在从CSV解析DataFrame后指定要包含在索引中的列，也可以立即作为read_csv的参数。

![](https://image.cubox.pro/cardImg/38sbbt2izw7185ulhb20qr3llrg0dhgfm53gu11jn19nzes88w?imageMogr2/quality/90/ignore-error/1)

您还可以使用append=True将现有级别添加到多重索引，如下图所示:

![](https://image.cubox.pro/cardImg/1g1v8gv02tqrws62ia22oe7udhs9255tftwh49et9onsl5h4vy?imageMogr2/quality/90/ignore-error/1)

另一个更典型的用例是表示多维。当你有一组具有特定属性的对象或者随着时间的推移而演变的对象时。例如:

* 社会学调查的结果

* \` Titanic \`数据集

* 历史天气观测

* 锦标赛排名的年表。

这也被称为"面板数据"，Pandas就是以此命名的。

让我们添加这样一个维度:

![](https://image.cubox.pro/cardImg/5dgf5hhuoxoaz1lbyadfbi1e6li7681oycmwt357n2f51hyacm?imageMogr2/quality/90/ignore-error/1)

现在我们有了一个四维空间，如下所示:

* 年形成一个(几乎连续的)维度

* 城市名称沿第二条排列

* 第三个州的名字

* 特定的城市属性("人口"、"密度"、"面积"等)在第四个维度上起到了"刻度线"的作用。

下图说明了这个概念:

![](https://image.cubox.pro/cardImg/vrkngc4di1svv9xa7ikbho812q9icffhby2j3xwv23n9vude0?imageMogr2/quality/90/ignore-error/1)

为了给对应列的尺寸名称留出空间，Pandas将整个标题向上移动:

![](https://image.cubox.pro/cardImg/3d1zpmbjbartvyuooo0t4qtje89j8xo5dwk3udl7ehnfy1pcol?imageMogr2/quality/90/ignore-error/1)

\## 分组

关于多重索引需要注意的第一件事是，它并不按照它可能出现的情况对任何内容进行分组。在内部，它只是一个扁平的标签序列，如下所示:

![](https://image.cubox.pro/cardImg/3d22d7m8q8gybax68h15irlic21y3vnlhl0rqntbrfgo28fpg4?imageMogr2/quality/90/ignore-error/1)

你可以通过对行标签进行排序来获得相同的groupby效果:

![](https://image.cubox.pro/cardImg/43t5ldqqihntx7obgn777appkx4mhlbbxdx6hyea0uwrijf4sr?imageMogr2/quality/90/ignore-error/1)

你甚至可以通过设置相应的Pandas选项来完全禁用视觉分组  
:pd.options.display.multi_sparse=False。

\## 类型转换

Pandas(以及Python本身)区分数字和字符串，因此在无法自动检测数据类型时，通常最好将数字转换为字符串:

    pdi.set_level(df.columns, 0, pdi.get_level(df.columns, 0).astype('int'))

如果你喜欢冒险，可以使用标准工具做同样的事情:

    df.columns = df.columns.set_levels(df.columns.levels[0].astype(int), level=0)

但为了正确使用它们，你需要理解什么是\` levels \`和\` codes \`，而pdi允许你使用多索引，就像使用普通的列表或NumPy数组一样。

如果你真的想知道，\` levels \`和\` codes \`是特定级别的常规标签列表被分解成的东西，以加速像pivot、join等操作:

* pdi.get_level(df, 0) == Int64Index(\[2010, 2010, 2020, 2020\])

* df.columns.levels\[0\] == Int64Index(\[2010, 2020\])

* df.columns.codes\[0\] == Int64Index(\[0, 1, 0, 1\])

\## 使用多重索引构建一个Dataframe

除了从CSV文件读取和从现有列构建外，还有一些方法可以创建多重索引。它们不太常用------主要用于测试和调试。

由于历史原因，使用Panda自己的多索引表示的最直观的方法不起作用。

![](https://image.cubox.pro/cardImg/5kw2lxqeg7ck37scm24wc5dlbncjdjynn858k5y1yhgs7zg9v3?imageMogr2/quality/90/ignore-error/1)

这里的\` Levels \`和\` codes \`(现在)被认为是不应该暴露给最终用户的实现细节，但我们已经拥有了我们所拥有的。

可能最简单的构建多重索引的方法如下:

![](https://image.cubox.pro/cardImg/21tyis3cg6uz1wpnrkhk11b5fo7mqrmmbln0ks9kplsaclmzax?imageMogr2/quality/90/ignore-error/1)

这样做的缺点是必须在单独的一行中指定级别的名称。有几种可选的构造函数将名称和标签捆绑在一起。

![](https://image.cubox.pro/cardImg/potc1r901imimaod2kh7gp2owjc2n1oquhkt7j7wlvphtp4av?imageMogr2/quality/90/ignore-error/1)

当关卡形成规则结构时，您可以指定关键元素，并让Pandas自动交织它们，如下所示:

![](https://image.cubox.pro/cardImg/21lohfj8ifmala6kuodgveq21x01l7revgw80vtsksy4dkmkrp?imageMogr2/quality/90/ignore-error/1)

上面列出的所有方法也适用于列。例如:

![](https://image.cubox.pro/cardImg/1zratwxusdzl6vt20rjd3yn3lxyrxrw7irahap3zc1kbb8vjmv?imageMogr2/quality/90/ignore-error/1)

\## 使用多重索引进行索引

通过多重索引访问DataFrame的好处是，您可以轻松地使用熟悉的语法一次引用所有级别(可能省略内部级别)。

列------通过普通的方括号

![](https://image.cubox.pro/cardImg/2sh909nd8tacg6lm9vjzat5wugd25wjeo44y9sbi1r0jp6fuf0?imageMogr2/quality/90/ignore-error/1)

行和单元格------使用.loc\[\]

![](https://image.cubox.pro/cardImg/1h0vpmnpy9pflihajgsfsyqlbk3ep3ynla4w8ryewnk7t7mh9e?imageMogr2/quality/90/ignore-error/1)

现在，如果你想选择俄勒冈州的所有城市，或者只留下包含人口的列，该怎么办?Python语法在这里有两个限制。

1. 没有办法区分df\['a'， 'b'\]和df\[('a'， 'b')\]------它是以同样的方式处理的，所以你不能只写df\[:， ' Oregon '\]。否则，Pandas将永远不知道你指的是列Oregon还是第二级行Oregon

2. Python只允许在方括号内使用冒号，而不允许在圆括号内使用冒号，所以你不能写df.loc\[(:， 'Oregon')，:\]

在技术方面，这并不难安排。我给DataFrame打了猴补丁，添加了这样的功能，你可以在这里看到:

![](https://image.cubox.pro/cardImg/5fp3fgdvkbkhq6em3b7ubi0ans2olksixf8tdycerwey02rtgw?imageMogr2/quality/90/ignore-error/1)

这种语法唯一的缺点是，当你使用两个索引器时，它返回一个副本，所以你不能写df.mi\[:， ' Oregon '\]。Co \[' population '\] = 10。有许多可选的索引器，其中一些允许这样的赋值，但它们都有自己的特点:

1. 您可以将内层与外层交换，并使用括号。

![](https://image.cubox.pro/cardImg/5zk0xf3xii64s5njucljzpjn9oyhw8bwz7o251p7zczrh032kd?imageMogr2/quality/90/ignore-error/1)

因此，df\[:， 'population'\]可以用df.swaplevel(axis=1)\['population'\]实现。

这感觉很hacky，不方便超过两层。

2. 你可以使用xs方法:df.xs (' population '， level=1, axis=1)。

它给人的感觉不够python化，尤其是在选择多个关卡时。这种方法无法同时过滤行和列，因此名称xs(代表"横截面")背后的原因并不完全清楚。它不能用于设置值。

3.可以为pd创建别名。idx=pd.IndexSlice;df.loc \[:， idx\[:， ' population '\]\]

这更符合python风格，但要访问元素，必须使用别名，这有点麻烦(没有别名的代码太长了)。您可以同时选择行和列。可写的。

4. 你可以学习如何使用slice代替冒号。如果你知道a\[3:10:2\] == a\[slice(3,10,2)\]，那么你可能也会理解下面的代码:df.loc\[:， (slice(None)， ' population ')\]，但它几乎无法读懂。您可以同时选择行和列。可写的。

作为底线，Pandas有多种使用括号使用多重索引访问DataFrame元素的方法，但没有一种方法足够方便，因此他们不得不采用另一种索引语法:

5. 一个用于.query方法的迷你语言:df.query(' state=="Oregon" or city=="Portland" ')。

它方便快捷，但缺乏IDE的支持(没有自动补全，没有语法高亮等)，而且它只过滤行，而不是列。这意味着你不能在不转置DataFrame的情况下用它实现df\[:， ' population '\](除非所有列的类型都相同，否则会丢失类型)。Non-writable。

\## 叠加与拆分

Pandas没有针对列的set_index。向列中添加层次的一种常见方法是将现有的层次从索引中"解栈":

![](https://image.cubox.pro/cardImg/15gyzeopbn2x9hkt3hhlyfvc3hgasqzbg0hahs1afrtuf6cdmh?imageMogr2/quality/90/ignore-error/1)

Pandas的栈与NumPy的栈有很大不同。让我们看看文档中对命名约定的说明:
> "该函数的命名类似于重新组织的书籍集合，从水平位置并排(dataframe的列)到垂直堆叠(在dataframe的索引中)。"

"在上面"的部分听起来并不能让我信服，但至少这个解释有助于记住谁把东西朝哪个方向移动。顺便说一下，Series有unstack，但没有stack，因为它已经"堆叠"了。由于是一维的，Series在不同情况下可以作为行向量或列向量，但通常被认为是列向量(例如dataframe列)。

例如:

![](https://image.cubox.pro/cardImg/6b842pxauqqxid9u0zg88inj3c5dffim8gzpv2owbsinossy7m?imageMogr2/quality/90/ignore-error/1)

您还可以通过名称或位置索引指定要堆叠/解堆叠的级别。在这个例子中，df.stack()、df.stack(1)和df.stack(' year ')与df1.unstack()、df1.unstack(2)和df1.unstack(' year ')产生相同的结果。目的地总是在"最后一层之后"，并且不可配置。如果需要将级别放在其他地方，可以使用df.swaplevel().sort_index()或pdi。swap_level (df = True)

列必须不包含重复的值才能堆叠(在反堆叠时，索引也是如此):

![](https://image.cubox.pro/cardImg/2wtq0psse4xk75br8rszxb7tnnkr69v04w6cqswr0r6prta21r?imageMogr2/quality/90/ignore-error/1)

\## 如何防止叠加/分解排序

stack和unstack都有一个坏习惯，会不可预测地按字典顺序排序结果索引。这有时可能令人恼火，但这是在有大量缺失值时给出可预测结果的唯一方法。

考虑下面的例子。你希望一周中的天数以何种顺序出现在右边的表中?

![](https://image.cubox.pro/cardImg/4jib37rd6ft35n6f6oy5rv3kdh7pnpafxwbyagemf0o3pqh5qn?imageMogr2/quality/90/ignore-error/1)

你可以推测，如果John的星期一在John的星期五的左边，那么就是' Mon ' \< ' Fri '，类似地，Silvia的' Fri ' \< ' Sun '，因此结果应该是' Mon ' \< ' Fri ' \< ' Sun '。这是合法的，但是如果剩余的列顺序不同，比如' Mon ' \< ' frii '和' Tue ' \< ' frii '，该怎么办?或者' Mon ' \< ' friday '和' Wed ' \< ' Sat ' ?

好吧，一周没有那么多天，Pandas可以根据先验知识推断出顺序。但是，人类还没有得出一个决定性的结论，那就是星期天应该作为一周的结束还是开始。Pandas应该默认使用哪种顺序?阅读区域设置?那么不那么琐碎的顺序呢，比如美国的州的顺序?

在这种情况下，Pandas所做的只是简单地按字母顺序排序，如下所示:

![](https://image.cubox.pro/cardImg/w7x790wsqgifq3rtxu7z9bg8eyjm8ug69ib32mqtrgc2hgfkc?imageMogr2/quality/90/ignore-error/1)

虽然这是一个合理的默认，但感觉上仍然是错误的。应该有一个解决方案!有一个。它被称为CategoricalIndex。即使缺少一些标签，它也会记住顺序。它最近已经顺利集成到Pandas工具链中。它唯一缺少的是基础设施。它很难建立;它是脆弱的(在某些操作中会退回到对象)，但它是完全可用的，并且pdi库有一些帮助程序可以陡峭地提高学习曲线。

例如，要告诉Pandas锁定存储产品的简单索引的顺序(如果你决定将一周中的天数解栈回列，则不可避免地会排序)，你需要编写像df这样可怕的代码。index = pd.CategoricalIndex(df. index)df指数。指数排序= True)。它更适合多索引。

pdi库有一个辅助函数locked(以及一个默认为inplace=True的别名lock)，通过将某个多索引级别提升到CategoricalIndex来锁定该级别的顺序:

![](https://image.cubox.pro/cardImg/333f1vuyphkw2oa1tj7ywun7id4d9vrdavhzip3pv9l22sb3dh?imageMogr2/quality/90/ignore-error/1)

等级名称旁边的勾选标记表示等级被锁定。它可以使用pdi.vis(df)手动可视化，也可以使用pdi.vis_patch()对DataFrame HTML输出进行monkey补丁自动可视化。应用补丁后，在Jupyter单元中简单地写\` df \`将显示锁定顺序的所有级别的复选标记。

Lock和locked在简单的情况下自动工作(如客户端名称)，但在更复杂的情况下(如缺少日期的星期几)需要用户提示。

![](https://image.cubox.pro/cardImg/5kryt05gulqxo621494bhcvioic60ucyp54n3opx5fiagr0cdg?imageMogr2/quality/90/ignore-error/1)

在级别切换到CategoricalIndex之后，它会在sort_index、stack、unstack、pivot、pivot_table等操作中保持原来的顺序。

不过，它很脆弱。即使像df\[' new_col '\] = 1这样简单的操作也会破坏它。使用pdi.insert (df。columns, 0， ' new_col '， 1)用CategoricalIndex正确处理级别。

\## 操作级别

除了前面提到的方法之外，还有一些其他的方法:

* pdi.get_level(obj, level_id)返回通过数字或名称引用的特定级别，可用于DataFrames, Series和MultiIndex

* pdi.set_level(obj, level_id, labels)用给定的数组(list, NumPy array, Series, Index等)替换关卡的标签

![](https://image.cubox.pro/cardImg/1sk6dnn9ck8lirbs92po8a18iamnuup6ig7jsiy3gma381wvt0?imageMogr2/quality/90/ignore-error/1)

* pdi.insert_level (obj, pos, labels, name)使用给定的值添加一个层级(必要时适当广播)

* pdi.drop_level(obj, level_id)从多重索引中删除指定的级别

![](https://image.cubox.pro/cardImg/5ubo1h8anwfit7zdlg4cvpelnbxv430im3glpv7ij9cqtl8zt7?imageMogr2/quality/90/ignore-error/1)

pdi.swap_levels (obj, src=-2, dst=-1)交换两个级别(默认是两个最内层的级别)

pdi.move_level (obj, src, dst)将特定级别src移动到指定位置dst

![](https://image.cubox.pro/cardImg/4alawwnjgjirxuxnb3gd789wxd6w0yc8z2v7m8wixhc66i0gu2?imageMogr2/quality/90/ignore-error/1)

除了上述参数外，本节中的所有函数还有以下参数:

* axis=None其中None对于DataFrame表示"列"，对于Series表示"索引"

* sort=False，可选在操作之后对相应的多索引进行排序

* inplace=False，可选地原地执行操作(不能用于单个索引，因为它是不可变的)。

上面的所有操作都是从传统意义上理解"级别"这个词的(级别的标签数量与数据框中的列数量相同)，隐藏了索引的机制。标签和索引。来自最终用户的代码。

在极少数情况下，当移动和交换单独的关卡不够时，您可以使用纯Pandas调用:df一次性重新排序所有关卡。columns = df.columns.reorder_levels(\[' M '， ' L '， ' K '\])其中\[' M '， ' L '， ' K '\]是层的期望顺序。

通常，使用get_level和set_level对标签进行必要的修复就足够了，但如果你想一次对多索引的所有级别应用转换，Pandas有一个(命名不明确)函数rename接受一个dict或一个函数:

![](https://image.cubox.pro/cardImg/197a8gvls8mcb3c1zqwagsl0j8akwnszhiu9egja7twzx0666e?imageMogr2/quality/90/ignore-error/1)

至于重命名级别，它们的名称存储在.names字段中。该字段不支持直接赋值(为什么不?):df.index.names\[1\] = ' x ' # TypeError，但可以作为一个整体替换:

![](https://image.cubox.pro/cardImg/3v7pequ8eqm90ph0zvdj44w9f7lui0tj5ty9r1txv3odaws6mp?imageMogr2/quality/90/ignore-error/1)

当你只需要重命名一个特定的级别时，语法如下:

![](https://image.cubox.pro/cardImg/52vp0yyj1e6swlrqmt9oufqx1dewf0ggbw27daw6ekgeqg5x5l?imageMogr2/quality/90/ignore-error/1)

\## 将多索引转换为平面索引并恢复它

正如我们在上面看到的，便捷的查询方法只解决了处理行中的多索引的复杂性。尽管有这么多的辅助函数，但当某些Pandas函数返回列中的多索引时，对初学者来说会有一个震惊的效果。因此，pdi库具有以下内容:

* join_levels(obj, sep='_', name=None) 将所有多索引级别连接到一个索引

* split_level(obj, sep='_', names=None)将索引拆分回多索引

![](https://image.cubox.pro/cardImg/2a78orda7o1b910j0dn4ihkfacekq847qea75edv67xj9i60x6?imageMogr2/quality/90/ignore-error/1)

它们都有可选的axis和inplace参数。

\## 排序MultiIndex

由于多索引由多个级别组成，因此排序比单索引更做作。这仍然可以使用sort_index方法完成，但可以使用以下参数进行进一步微调。

![](https://image.cubox.pro/cardImg/1fcy222ku37q3uj1s8x0avchti2zfg5jhn73ide5bppn097fqs?imageMogr2/quality/90/ignore-error/1)

要对列级别进行排序，指定axis=1。

\## 读写多索引dataframe到磁盘

Pandas可以以完全自动化的方式将具有多重索引的DataFrame写入CSV文件:df.to_csv('df.csv ')。但是在读取这样的文件时，Pandas无法自动解析多重索引，需要用户的一些提示。例如，要读取具有三层高列和四层宽索引的DataFrame，你需要指定pd.read_csv('df.csv'， header=\[0,1,2\]， index_col=\[0,1,2,3\])。

这意味着前三行包含有关列的信息，后续每一行的前四个字段包含索引级别(如果列的级别不止一个，你不能再通过名称来引用行级别，只能通过编号)。

手动解读多索引中的层数是不方便的，所以更好的主意是在将DataFrame保存到CSV之前，stack()所有列头层，并在读取后将它们解stack()。

如果你需要"置之不理"的解决方案，可能需要研究二进制格式，例如Python的pickle格式:

直接调用:df.to_pickle('df.pkl')， pd.read_pickle('df.pkl')

使用storemagic在Jupyter %store df然后%store -r df(存储在$  
HOME/.ipython/profile_default/db/autorestore)

Python的pickle小巧而快速，但只能在Python中访问。如果您需要与其他生态系统互操作，请查看更标准的格式，如Excel格式(在读取MultiIndex时需要与read_csv相同的提示)。代码如下:

    !pip install openpyxl
    df.to_excel('df3.xlsx')
    df.to_pd.read_excel('df3.xlsx', header=[0,1,2], index_col=[0,1,2,3])

或者查看其他选项(参见文档)。

\## MultiIndex算术

当使用多索引数据框时，与普通数据框适用相同的规则(见上文)。但是处理细胞的一个子集有它自己的一些特性。

用户可以通过外部的多索引级别更新部分列，如下所示:

![](https://image.cubox.pro/cardImg/nfrnh1rihw5yer52yfi2glhwt69d2i1l3o9adn046539z42nf?imageMogr2/quality/90/ignore-error/1)

如果想保持原始数据不变，可以使用df1 = df.assign(population=df.population\*10)。

你也可以用density=df.population/df.area轻松获得人口密度。

![](https://image.cubox.pro/cardImg/5620gpd2m2gqobhsxt34nqcosgf6axcz5zeqx0nbiedq2zwwv3?imageMogr2/quality/90/ignore-error/1)

但不幸的是，你不能用df.assign将结果赋值给原始的dataframe。

一种方法是将列索引的所有不相关级别堆叠到行索引中，执行必要的计算，然后将它们解堆叠回去(使用pdi)。锁以保持列的原始顺序)。

![](https://image.cubox.pro/cardImg/54gu68v0z2x5tq4lq1oupcu5spagfqf15be8o7xpzigqazhahz?imageMogr2/quality/90/ignore-error/1)

或者，你也可以使用pdi.assign:

![](https://image.cubox.pro/cardImg/3xl9sqkx9atgxuhi6tfjjf9l7kpucpijslp646uuzbi5wkmg1z?imageMogr2/quality/90/ignore-error/1)

pdi.assign是锁定顺序感知的，所以如果你给它一个(多个)锁定级别的dataframe，它不会解锁它们或后续的栈/解栈/等。操作将保持原始的列和行顺序。

总而言之，Pandas是分析和处理数据的好工具。希望这篇文章能帮助你理解"如何"和"为什么"解决典型问题，并欣赏Pandas库的真正价值和美丽。

为了跟上AI时代我干了一件事儿，我创建了一个知识星球社群：ChartGPT与副业。想带着大家一起探索ChatGPT和新的AI时代。

有很多小伙伴搞不定ChatGPT账号，于是我们决定，凡是这三天之内加入ChatPGT的小伙伴，我们直接送一个正常可用的永久ChatGPT独立账户。

不光是增长速度最快，我们的星球品质也绝对经得起考验，短短一个月时间，我们的课程团队发布了8个专栏、18个副业项目：

![](https://image.cubox.pro/cardImg/20kdyyp0kbh8ltu9rqsap4ue0910ezcth1tlesp4kyrwxn5fu?imageMogr2/quality/90/ignore-error/1)

简单说下这个星球能给大家提供什么：

1、不断分享如何使用ChatGPT来完成各种任务，让你更高效地使用ChatGPT，以及副业思考、变现思路、创业案例、落地案例分享。

2、分享ChatGPT的使用方法、最新资讯、商业价值。

3、探讨未来关于ChatGPT的机遇，共同成长。

4、帮助大家解决ChatGPT遇到的问题。

5、提供一整年的售后服务，一起搞副业

星球福利：

1、加入星球4天后，就送ChatGPT独立账号。

2、邀请你加入ChatGPT会员交流群。

3、赠送一份完整的ChatGPT手册和66个ChatGPT副业赚钱手册。

其它福利还在筹划中...不过，我给你大家保证，加入星球后，收获的价值会远远大于今天加入的门票费用 ！

本星球第一期原价399，目前属于试运营，早鸟价169，每超过50人涨价10元，星球马上要来一波大的涨价，如果你还在犹豫，可能最后就要以更高价格加入了。。

早就是优势。建议大家尽早以便宜的价格加入！

\#\#\## ````

```
![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2FlgCBBmmGCU344J5eUia3UvLCKl053WrtFFpX4dLFh1T7ib4R0wAqF6vyDIsuqBFiboOAm67cSqyV0C9xhWtiaGFBug%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg&valid=false)

```

````


![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2FULibHgXIt3jwUib80302u7aDmEnSgZpdicx7CLo6yWU21RZicFA3c8Aic9fVTwriamKXh97X2BnWyzddJql4KWmPGHwg%2F640%3Fwx_fmt%3Dpng%26wxfrom%3D5%26wx_lazy%3D1%26wx_co%3D1&valid=false)

```
      
    
       
       欢迎有需要的同学试试，如果本文对您有帮助，也请帮忙点个**赞 + 在看** 啦！❤️
       
     

      
    
       在http://mp.weixin.qq.com/s?__biz=MzU1NjYxNDc2OQ==&mid=2247492803&idx=1&sn=9fb33fe642708725ac51e6565ab29dc1&chksm=fbc0f1ddccb778cb5d752de5cc7ed36120801e3468ea4227d8515ecf2a661c77776df00a39b3&scene=21\#wechat_redirect还有更多优质项目系统学习资源，欢迎分享给其他同学吧！
```

****你还有什** **么想要补充的吗？****   
>
> 免责声明：本文内容来源于网络，文章版权归原作者所有，意在传播相关技术知识\&行业趋势，供大家学习交流，若涉及作品版权问题，请联系删除或授权事宜。  
>

**技术君个人微信**


**添加技术君个人微信即送一份惊喜大礼包**

→ 技术资料共享

→ 技术交流社群

![](https://image.cubox.pro/cardImg/2b0mo3e3kjdsn7xy8jyh65m8vem4tdkyq38u24icrnrihekmw9?imageMogr2/quality/90/ignore-error/1)


--END--

**往日热文：**

[看看人家那物业管理系统，那叫一个优雅（附源码）](http://mp.weixin.qq.com/s?__biz=MzI0MzU2NzQ1OA==&mid=2247510334&idx=2&sn=309a6d0c769625864695246fefb4bf64&chksm=e969f733de1e7e258bbf242ace3eeef61284ac31ce5beb5074bc2b7eee4cd455251e8b547fc5&scene=21\#wechat_redirect)  

[一款神仙接私活儿软件，吊到不行！](http://mp.weixin.qq.com/s?__biz=MzI0MzU2NzQ1OA==&mid=2247510254&idx=1&sn=5d9468461da7df149796d9dce6c24e99&chksm=e969f6e3de1e7ff53626265b4aea0dd0fe4718a2e4286eb4241fa62e79ee9c618bd991f6ba40&scene=21\#wechat_redirect)

[13个用于日常编程的高级Python脚本](http://mp.weixin.qq.com/s?__biz=MzI0MzU2NzQ1OA==&mid=2247526817&idx=1&sn=c780c351cc15d5064e2a8341eb7c9113&chksm=e96937acde1ebeba99291ed55983f3ab8573a4e403bd77b0004a784624610471e0b3f60b79d9&scene=21\#wechat_redirect)

[泰酷辣！Python文本终端GUI框架！](http://mp.weixin.qq.com/s?__biz=MzI0MzU2NzQ1OA==&mid=2247526841&idx=1&sn=e847afcd6aecee76e81f34c787cf6d78&chksm=e96937b4de1ebea2427ff4b5aaf1316a69356eb4cfd12780f78f700d34457cc75f9149a253cc&scene=21\#wechat_redirect)

```
Python程序员深度学习的"四大名著"：
![](https://image.cubox.pro/cardImg/68ns8197g7umcw7yqt594lkk79vg6pbcizp0h89kat7otjigv2?imageMogr2/quality/90/ignore-error/1)这四本书着实很不错！我们都知道现在机器学习、深度学习的资料太多了，面对海量资源，往往陷入到"无从下手"的困惑出境。而且并非所有的书籍都是优质资源，浪费大量的时间是得不偿失的。给大家推荐这几本好书并做简单介绍。**获得方式：**
  
   
      
   **1.扫码关注本** **公众号**
  
   
      
  
   
      
   **2.后台回复关键词：** **名著**
  
   
      ![](https://image.cubox.pro/cardImg/14yusty7s7d2oqy7d2ue26anb39i5ggi6jbb2gbkw3pj4h1kz0?imageMogr2/quality/90/ignore-error/1)
  
   
      
   ▲长按扫描关注，回复名著即可获取
  
   
      
  
  
   
      
   ![](https://image.cubox.pro/cardImg/1sttxrl6rvs1xu9ys5khwz87ye2pq4mplazoij0nsc019jbxy2?imageMogr2/quality/90/ignore-error/1)
  
   
      
```

[Read in Cubox](https://cubox.pro/web/card/7204006255453539017)
