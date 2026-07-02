---
id: "7159890020638133506"
cubox_url: https://cubox.pro/web/card/7159890020638133506
url: https://mp.weixin.qq.com/s/MM-XB3NrrZO-A_3R0GD6hw
tags:
  - Skill/python
  - Skill/data-analysis
---
# 区区几行Python代码，就能实现全面自动探索性数据分析！



[Read in Cubox](https://cubox.pro/web/card/7159890020638133506)  
[Read Original](https://mp.weixin.qq.com/s/MM-XB3NrrZO-A_3R0GD6hw)  

---


---

\## 📖 正文全文

# 区区几行Python代码，就能实现全面自动探索性数据分析！

[mp.weixin.qq.com](https://mp.weixin.qq.com/s/MM-XB3NrrZO-A_3R0GD6hw)Python人工智能技术


点击上方"**Python人工智能技术** "关注，星标或者置顶   


22点24分准时推送，第一时间送达

后台回复"**大礼包**"，送你特别福利  

> 编辑：乐乐 \| 来自：数据STUDIO（侵删）

[Pythn人工智能技术(ID:coder_experience) 1067期推文](http://mp.weixin.qq.com/s?__biz=MzI0MzU2NzQ1OA==&mid=2247489525&idx=1&sn=26e9ce9d935a845d03ce4a3d30ebc975&chksm=e96a49f8de1dc0eeda78a0f1fa1ab74bfa13222fecbb924f52e59b59cd8b431d6e0fd00cc1cb&scene=21\#wechat_redirect)

上一篇：[对色情app渗透，我居然发现了 ....](http://mp.weixin.qq.com/s?__biz=MzI0MzU2NzQ1OA==&mid=2247526690&idx=1&sn=415b98c26162e461520fd921a2296cde&chksm=e969372fde1ebe39d66cbbec184439e0c4d6830305271081ce052908b077e55f5352d454d65c&scene=21\#wechat_redirect)


**正文**


**大家好，我是Python人工智能技术**

来源丨数据STUDIO（侵删）  

\#\#\#\## 探索性数据分析是数据科学模型开发和数据集研究的重要组成部分之一。在拿到一个新数据集时首先就需要花费大量时间进行EDA来研究数据集中内在的信息。自动化的EDA Python包可以用几行Python代码执行EDA。在本文中整理了10个可以自动执行EDA并生成有关数据的见解的Python包，看看他们都有什么功能，能在多大程度上帮我们自动化解决EDA的需求。


1.
   DTale
2.
   Pandas-profiling
3.
   sweetviz
4.
   autoviz
5.
   dataprep
6.
   KLib
7.
   dabl
8.
   speedML
9.
   datatile
10.
    edaviz

\## 1、D-Tale

![](https://image.cubox.pro/cardImg/2024022115594564054/68043.jpg?imageMogr2/quality/90/ignore-error/1)

D-Tale使用Flask作为后端、React前端并且可以与ipython notebook和终端无缝集成。D-Tale可以支持Pandas的DataFrame, Series, MultiIndex,DatetimeIndex和RangeIndex。

    importdtale
    importpandasaspd
    dtale.show(pd.read_csv("titanic.csv"))

![](https://image.cubox.pro/cardImg/2024022115594528104/85934.jpg?imageMogr2/quality/90/ignore-error/1)

D-Tale库用一行代码就可以生成一个报告，其中包含数据集、相关性、图表和热图的总体总结，并突出显示缺失的值等。D-Tale还可以为报告中的每个图表进行分析，上面截图中我们可以看到图表是可以进行交互操作的。

\## 2、Pandas-Profiling

![](https://image.cubox.pro/cardImg/2024022115594510420/40057.jpg?imageMogr2/quality/90/ignore-error/1)

Pandas-Profiling可以生成Pandas DataFrame的概要报告。panda-profiling扩展了pandas DataFrame df.profile_report()，并且在大型数据集上工作得非常好，它可以在几秒钟内创建报告。

    \#Installthebelowlibariesbeforeimporting
    importpandasaspd
    frompandas_profilingimportProfileReport

    \#EDAusingpandas-profiling
    profile=ProfileReport(pd.read_csv('titanic.csv'),explorative=True)

    \#SavingresultstoaHTMLfile
    profile.to_file("output.html")

![](https://image.cubox.pro/cardImg/2024022115594555973/41815.jpg?imageMogr2/quality/90/ignore-error/1)

\## 3、Sweetviz

![](https://image.cubox.pro/cardImg/2024022115594627181/50006.jpg?imageMogr2/quality/90/ignore-error/1)

Sweetviz是一个开源的Python库，只需要两行Python代码就可以生成漂亮的可视化图，将EDA(探索性数据分析)作为一个HTML应用程序启动。Sweetviz包是围绕快速可视化目标值和比较数据集构建的。

    importpandasaspd
    importsweetvizassv

    \#EDAusingAutoviz
    sweet_report=sv.analyze(pd.read_csv("titanic.csv"))

    \#SavingresultstoHTMLfile
    sweet_report.show_html('sweet_report.html')

Sweetviz库生成的报告包含数据集、相关性、分类和数字特征关联等的总体总结。
![](https://image.cubox.pro/cardImg/2024022115594619909/21444.jpg?imageMogr2/quality/90/ignore-error/1)

\## 4、AutoViz

![](https://image.cubox.pro/cardImg/2024022115594644604/89498.jpg?imageMogr2/quality/90/ignore-error/1)

Autoviz包可以用一行代码自动可视化任何大小的数据集，并自动生成HTML、bokeh等报告。用户可以与AutoViz包生成的HTML报告进行交互。

    importpandasaspd
    fromautoviz.AutoViz_ClassimportAutoViz_Class

    \#EDAusingAutoviz
    autoviz=AutoViz_Class().AutoViz('train.csv')

![](https://image.cubox.pro/cardImg/2024022115594613583/97314.jpg?imageMogr2/quality/90/ignore-error/1)

\## 5、Dataprep

![](https://image.cubox.pro/cardImg/2024022115594785046/10365.jpg?imageMogr2/quality/90/ignore-error/1)

Dataprep是一个用于分析、准备和处理数据的开源Python包。DataPrep构建在Pandas和Dask DataFrame之上，可以很容易地与其他Python库集成。

DataPrep的运行速度这10个包中最快的，他在几秒钟内就可以为Pandas/Dask DataFrame生成报告。

    fromdataprep.datasetsimportload_dataset
    fromdataprep.edaimportcreate_report

    df=load_dataset("titanic.csv")
    create_report(df).show_browser()

![](https://image.cubox.pro/cardImg/2024022115594787603/70147.jpg?imageMogr2/quality/90/ignore-error/1)

\## 6、Klib

![](https://image.cubox.pro/cardImg/2024022115594764554/81621.jpg?imageMogr2/quality/90/ignore-error/1)

klib是一个用于导入、清理、分析和预处理数据的Python库。

    importklib
    importpandasaspd

    df=pd.read_csv('DATASET.csv')
    klib.missingval_plot(df)

![](https://image.cubox.pro/cardImg/2024022115594749756/50547.jpg?imageMogr2/quality/90/ignore-error/1)

    klib.corr_plot(df_cleaned,annot=False)

![](https://image.cubox.pro/cardImg/2024022115594767171/88089.jpg?imageMogr2/quality/90/ignore-error/1)

    klib.dist_plot(df_cleaned['Win_Prob'])

![](https://image.cubox.pro/cardImg/2024022115594838013/92386.jpg?imageMogr2/quality/90/ignore-error/1)

    klib.cat_plot(df,figsize=(50,15))

![](https://image.cubox.pro/cardImg/2024022115594847189/81497.jpg?imageMogr2/quality/90/ignore-error/1)

klibe虽然提供了很多的分析函数，但是对于每一个分析需要我们手动的编写代码，所以只能说是半自动化的操作，但是如果我们需要更定制化的分析，他是非常方便的。
![](https://image.cubox.pro/cardImg/2024022115594899719/73198.jpg?imageMogr2/quality/90/ignore-error/1)

\## 7、Dabl

Dabl不太关注单个列的统计度量，而是更多地关注通过可视化提供快速概述，以及方便的机器学习预处理和模型搜索。
![](https://image.cubox.pro/cardImg/2024022115594849587/87315.jpg?imageMogr2/quality/90/ignore-error/1)

dabl中的Plot()函数可以通过绘制各种图来实现可视化，包括:

*
  目标分布图
*
  散点图
*
  线性判别分析

    importpandasaspd
    importdabl

    df=pd.read_csv("titanic.csv")
    dabl.plot(df,target_col="Survived")

![](https://image.cubox.pro/cardImg/2024022115594938485/37636.jpg?imageMogr2/quality/90/ignore-error/1)

\## 8、Speedml

SpeedML是用于快速启动机器学习管道的Python包。SpeedML整合了一些常用的ML包，包括 Pandas，Numpy，Sklearn，Xgboost 和Matplotlib，所以说其实SpeedML不仅仅包含自动化EDA的功能。

SpeedML官方说，使用它可以基于迭代进行开发，将编码时间缩短了70％。

    fromspeedmlimportSpeedml

    sml=Speedml('../input/train.csv','../input/test.csv',
    target='Survived',uid='PassengerId')
    sml.train.head()

![](https://image.cubox.pro/cardImg/2024022115594989902/57029.jpg?imageMogr2/quality/90/ignore-error/1)

    sml.plot.correlate()

![](https://image.cubox.pro/cardImg/2024022115594937264/92405.jpg?imageMogr2/quality/90/ignore-error/1)

    sml.plot.distribute()

![](https://image.cubox.pro/cardImg/2024022115594959694/66585.jpg?imageMogr2/quality/90/ignore-error/1)

    sml.plot.ordinal('Parch')

![](https://image.cubox.pro/cardImg/2024022115594979913/95791.jpg?imageMogr2/quality/90/ignore-error/1)

    sml.plot.ordinal('SibSp')

![](https://image.cubox.pro/cardImg/2024022115595039784/98386.jpg?imageMogr2/quality/90/ignore-error/1)

    sml.plot.continuous('Age')

![](https://image.cubox.pro/cardImg/2024022115595074532/63896.jpg?imageMogr2/quality/90/ignore-error/1)

\## 9、DataTile

DataTile（以前称为Pandas-Summary）是一个开源的Python软件包，负责管理，汇总和可视化数据。DataTile基本上是PANDAS DataFrame describe（）函数的扩展。

    importpandasaspd
    fromdatatile.summary.dfimportDataFrameSummary

    df=pd.read_csv('titanic.csv')
    dfs=DataFrameSummary(df)
    dfs.summary()

![](https://image.cubox.pro/cardImg/2024022115595029677/90347.jpg?imageMogr2/quality/90/ignore-error/1)

\## 10、edaviz

edaviz是一个可以在Jupyter Notebook和Jupyter Lab中进行数据探索和可视化的python库，他本来是非常好用的，但是后来被砖厂(Databricks)收购并且整合到bamboolib 中，所以这里就简单的给个演示。

![](https://image.cubox.pro/cardImg/2024022115595032652/30289.jpg?imageMogr2/quality/90/ignore-error/1)

\## 总结

在本文中，我们介绍了10个自动探索性数据分析Python软件包，这些软件包可以在几行Python代码中生成数据摘要并进行可视化。通过自动化的工作可以节省我们的很多时间。

Dataprep是我最常用的EDA包，AutoViz和D-table也是不错的选择，如果你需要定制化分析可以使用Klib，SpeedML整合的东西比较多，单独使用它啊进行EDA分析不是特别的适用，其他的包可以根据个人喜好选择，其实都还是很好用的，最后edaviz就不要考虑了，因为已经不开源了。


****万水千山总是情，点个👍行不行**。**

为了跟上AI时代我干了一件事儿，我创建了一个知识星球社群：ChartGPT与副业。想带着大家一起探索ChatGPT和新的AI时代。

有很多小伙伴搞不定ChatGPT账号，于是我们决定，凡是这三天之内加入ChatPGT的小伙伴，我们直接送一个正常可用的永久ChatGPT独立账户。

不光是增长速度最快，我们的星球品质也绝对经得起考验，短短一个月时间，我们的课程团队发布了8个专栏、18个副业项目：

![](https://image.cubox.pro/cardImg/2024022115595132229/20873.jpg?imageMogr2/quality/90/ignore-error/1)

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
![](https://image.cubox.pro/cardImg/2024022115595185052/38515.jpg?imageMogr2/quality/90/ignore-error/1)

```

````


![](https://image.cubox.pro/cardImg/2024022115595152969/55358.jpg?imageMogr2/quality/90/ignore-error/1)

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

![](https://image.cubox.pro/cardImg/2024022115595161614/39207.jpg?imageMogr2/quality/90/ignore-error/1)


--END--

**往日热文：**

[看看人家那物业管理系统，那叫一个优雅（附源码）](http://mp.weixin.qq.com/s?__biz=MzI0MzU2NzQ1OA==&mid=2247510334&idx=2&sn=309a6d0c769625864695246fefb4bf64&chksm=e969f733de1e7e258bbf242ace3eeef61284ac31ce5beb5074bc2b7eee4cd455251e8b547fc5&scene=21\#wechat_redirect)  

[一款神仙接私活儿软件，吊到不行！](http://mp.weixin.qq.com/s?__biz=MzI0MzU2NzQ1OA==&mid=2247510254&idx=1&sn=5d9468461da7df149796d9dce6c24e99&chksm=e969f6e3de1e7ff53626265b4aea0dd0fe4718a2e4286eb4241fa62e79ee9c618bd991f6ba40&scene=21\#wechat_redirect)  

[保姆级别！带你搭建一台服务器！](http://mp.weixin.qq.com/s?__biz=MzI0MzU2NzQ1OA==&mid=2247510687&idx=2&sn=aad0db260df36d4bfb94b0a28ec92c47&chksm=e969f492de1e7d84dab0d87f6ba9d491a1992c09b91da3e9b41f04aa9e19e6760b50ea7e231a&scene=21\#wechat_redirect)

[好家伙，花了一个月时间，用Python写了个网易云！](http://mp.weixin.qq.com/s?__biz=MzI0MzU2NzQ1OA==&mid=2247526485&idx=1&sn=7a57cda1b712e861030cad2da41d51d3&chksm=e9693658de1ebf4ec5855820f6eb7434902774dee3a70e7186f0600e2e29bdf1d41227219e82&scene=21\#wechat_redirect)

[利用 Python 开发手机 App 实战](http://mp.weixin.qq.com/s?__biz=MzI0MzU2NzQ1OA==&mid=2247526498&idx=1&sn=afcaf03f06a01df5d42a45eea48eeafe&chksm=e969366fde1ebf79da9ad91f20024a282fe08746400e74a378acc5384c1320ef7b555a5ecde4&scene=21\#wechat_redirect)

[Python Web框架的三强之争：Flask、Django和FastAPI](http://mp.weixin.qq.com/s?__biz=MzI0MzU2NzQ1OA==&mid=2247526523&idx=1&sn=58373b9d878f594d4c8fa0c18ec79cf7&chksm=e9693676de1ebf608d8f42873d0c577da1fc0ed59368c4616ec4061c998b5d8cb41779bf172a&scene=21\#wechat_redirect)

[7 个令人惊喜的 Python 库](http://mp.weixin.qq.com/s?__biz=MzI0MzU2NzQ1OA==&mid=2247526543&idx=1&sn=fd6615e9c9f88339b31d077d1a5ea583&chksm=e9693682de1ebf94b2b981c260fe9b59445c80b9df4f11765cadb46e419089ebf11e4e0e97bc&scene=21\#wechat_redirect)

[我看谁还不懂 Git ！(万字干货)](http://mp.weixin.qq.com/s?__biz=MzI0MzU2NzQ1OA==&mid=2247526613&idx=1&sn=0cacd89172acbcfdd6885e4d7dd82128&chksm=e96936d8de1ebfce52cb8bdbaf07bf0f4f83c121280a8bb833adad487b86c0cab51fd3a496e4&scene=21\#wechat_redirect)

[Python爬虫库推荐，建议收藏留用](http://mp.weixin.qq.com/s?__biz=MzI0MzU2NzQ1OA==&mid=2247526666&idx=1&sn=9fbd5bff6df6070adeb09155c91ab24e&chksm=e9693707de1ebe11db121d54421264bf19be05b175b40f2f2334a249b0a79a18ab9af6d7b501&scene=21\#wechat_redirect)

```
Python程序员深度学习的"四大名著"：
![](https://image.cubox.pro/cardImg/2024022115595298802/13475.jpg?imageMogr2/quality/90/ignore-error/1)这四本书着实很不错！我们都知道现在机器学习、深度学习的资料太多了，面对海量资源，往往陷入到"无从下手"的困惑出境。而且并非所有的书籍都是优质资源，浪费大量的时间是得不偿失的。给大家推荐这几本好书并做简单介绍。**获得方式：**
  
   
      
   **1.扫码关注本** **公众号**
  
   
      
  
   
      
   **2.后台回复关键词：** **名著**
  
   
      ![](https://image.cubox.pro/cardImg/2024022115595211025/19920.jpg?imageMogr2/quality/90/ignore-error/1)
  
   
      
   ▲长按扫描关注，回复名著即可获取
  
   
      
  
  
   
      
   ![](https://image.cubox.pro/cardImg/2024022115595269071/19043.jpg?imageMogr2/quality/90/ignore-error/1)
  
   
      
```

[Read in Cubox](https://cubox.pro/web/card/7159890020638133506)
