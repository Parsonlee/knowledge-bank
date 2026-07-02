---
id: "7128377660480160628"
cubox_url: https://cubox.pro/web/card/7128377660480160628
url: https://mp.weixin.qq.com/s/6TrDtLHqBBYEfCwJobZeAg
tags:
  - Skill/data-analysis
---
# 一行代码让 matplotlib 图表变高大上

懒人数据可视化必备

[Read in Cubox](https://cubox.pro/web/card/7128377660480160628)  
[Read Original](https://mp.weixin.qq.com/s/6TrDtLHqBBYEfCwJobZeAg)  

---


---

\## 📖 正文全文

# 一行代码让 matplotlib 图表变高大上

[mp.weixin.qq.com](https://mp.weixin.qq.com/s/6TrDtLHqBBYEfCwJobZeAg)费弗里 程序员的那些事

1 简介  

`matplotlib`作为`Python`生态中最流行的数据可视化框架，虽然功能非常强大，但默认样式比较简陋，想要制作具有简洁商务风格的图表往往需要编写众多的代码来调整各种参数。

而今天要为大家介绍的`dufte`，就是用来通过简短的代码，对默认的`matplotlib`图表样式进行自动改造的`Python`库：
![图片](https://image.cubox.pro/cardImg/2023112617010354194/34782.jpg?imageMogr2/quality/90/ignore-error/1)

\## 2 利用dufte自动改造matplotlib图表

通过`pip install dufte`安装完成后，我们就可以将`dufte`的几个关键`API`穿插在常规`matplotlib`图表的绘制过程中，目前主要有以下几种功能：

\## 2.1 主题设置

`dufte`最重要的功能是其自带的主题风格，而在`matplotlib`中有两种设置主题的方式，一种是利用`plt.style.use(主题)`来全局设置，一般不建议这种方式。

另一种方式则是以下列方式来在`with`的作用范围内局部使用主题：

    \#局部主题设置
    withplt.style.context(主题):
    \#绘图代码
    ...

我们今天就都使用第二种方式，首先导入演示所需的依赖库，并从本地注册`思源宋体`：

    importdufte
    importnumpyasnp
    importmatplotlib.pyplotasplt
    frommatplotlibimportfont_manager

    \#注册本地思源宋体
    fontproperties=font_manager.FontProperties(fname='NotoSerifSC-Regular.otf')

接下来我们以折线图和柱状图为例：

*
  折线图

    \#折线图示例
    withplt.style.context(dufte.style):
    x=range(100)
    y=np.random.standard_normal(100).cumsum()

    fig,ax=plt.subplots(figsize=(10,5),facecolor='white',edgecolor='white')

    ax.plot(x,y,linestyle='-.',color='\#607d8b')

    ax.set_xlabel('x轴示例',fontproperties=fontproperties,fontsize=16)
    ax.set_ylabel('y轴示例',fontproperties=fontproperties,fontsize=16)

    ax.set_title('折线图示例',fontproperties=fontproperties,fontsize=20)

    fig.savefig('图2.png',dpi=300,bbox_inches='tight')

![图片](https://image.cubox.pro/cardImg/2023112617010483316/90150.jpg?imageMogr2/quality/90/ignore-error/1)

*
  柱状图

    \#柱状图示例
    withplt.style.context(dufte.style):
    x=range(25)
    y=np.random.standard_normal(25)

    fig,ax=plt.subplots(figsize=(10,5),facecolor='white',edgecolor='white')

    ax.bar(x,y)

    ax.set_xlabel('x轴示例',fontproperties=fontproperties,fontsize=16)
    ax.set_ylabel('y轴示例',fontproperties=fontproperties,fontsize=16)

    ax.set_title('柱状图示例',fontproperties=fontproperties,fontsize=20)

    fig.savefig('图3.png',dpi=300,bbox_inches='tight')

![图片](https://image.cubox.pro/cardImg/2023112617010484096/28505.jpg?imageMogr2/quality/90/ignore-error/1)

可以看到，`dufte`自带了一套简洁的绘图风格，主张去除多余的轴线，只保留必要的参考线，适用于我们日常工作中的通用出图需求。

\## 2.2 自动图例美化

除了前面介绍的整体主题风格之外，`dufte`还自带了一套图例风格化策略，只需要在绘图过程中利用`dufte.legend()`来代替`matplotlib`原有的`legend()`即可，以下面的折线图为例：

    \#折线图示例
    withplt.style.context(dufte.style):
    x=range(100)
    y1=np.random.randint(-5,6,100).cumsum()
    y2=np.random.randint(-5,10,100).cumsum()
    y3=np.random.randint(-5,6,100).cumsum()

    fig,ax=plt.subplots(figsize=(10,5),facecolor='white',edgecolor='white')

    ax.plot(x,y1,linestyle='dotted',label='Series1')
    ax.plot(x,y2,linestyle='dashed',label='Series2')
    ax.plot(x,y3,linestyle='dashdot',label='Series3')

    ax.set_xlabel('x轴示例',fontproperties=fontproperties,fontsize=16)
    ax.set_ylabel('y轴示例',fontproperties=fontproperties,fontsize=16)

    dufte.legend()

    ax.set_title('dufte.legend()示例',fontproperties=fontproperties,fontsize=20)

    fig.savefig('图4.png',dpi=300,bbox_inches='tight')

可以看到，对于多系列图表，只需要一行`dufte.legend()`就可以自动添加出下列别致的图例说明：
![图片](https://image.cubox.pro/cardImg/2023112617010496488/32080.jpg?imageMogr2/quality/90/ignore-error/1)

\## 2.3 柱状图自动标注

很多时候我们在绘制柱状图时，希望把每个柱体对应的y值标注在柱体上，而通过`dufte.show_bar_values()`，只要其之前的绘图流程中设置了`xticks`，它就会帮我们自动往柱体上标注信息：

    \#柱状图示例
    withplt.style.context(dufte.style):
    x=range(15)
    y=np.random.randint(5,15,15)

    fig,ax=plt.subplots(figsize=(10,5),facecolor='white',edgecolor='white')

    ax.bar(x,y)

    ax.set_xticks(x)
    ax.set_xticklabels(\[f'项目{i}'foriinx\],fontproperties=fontproperties,fontsize=10)
    dufte.show_bar_values()

    ax.set_xlabel('x轴示例',fontproperties=fontproperties,fontsize=16)
    ax.set_ylabel('y轴示例',fontproperties=fontproperties,fontsize=16)

    ax.set_title('柱状图示例',fontproperties=fontproperties,fontsize=20)

    fig.savefig('图5.png',dpi=300,bbox_inches='tight')

![图片](https://image.cubox.pro/cardImg/2023112617010567126/28368.jpg?imageMogr2/quality/90/ignore-error/1)

作为一个处于开发初期的库，`dufte`未来势必会加入更多的实用功能，感兴趣的朋友可以对其持续关注。

- EOF -


推荐阅读点击标题可跳转

1、[详尽实用的 PyCharm 教程，这篇文章值得一看](http://mp.weixin.qq.com/s?__biz=MjM5OTA1MDUyMA==&mid=2655465341&idx=4&sn=0df4922bd3b9ef1a0b7e6515792a593f&chksm=bd72e30a8a056a1c576d53277888b447ce159619ae55bc226b327dc546b3159a7285ed333d39&scene=21\#wechat_redirect)

2、[整理了 33 个 Python 自动化办公库](http://mp.weixin.qq.com/s?__biz=MjM5OTA1MDUyMA==&mid=2655464865&idx=4&sn=dbbda749897c6180b39360d3d4d84666&chksm=bd72e1d68a0568c07aaf45a4523002e5d604c7f4b09a234287d6d406377bf1fce2f4085f834c&scene=21\#wechat_redirect)

3、[有了这款神器，轻松用 Python 写个 APP](http://mp.weixin.qq.com/s?__biz=MjM5OTA1MDUyMA==&mid=2655464822&idx=2&sn=2002c4ca70139f0ad673199c13c6440e&chksm=bd72e1018a05681740157de2038bcc845c0fb01fbd4abfbc4332e7218cced5f0a21737d690d3&scene=21\#wechat_redirect)


关注「程序员的那些事」加星标，不错过圈内事  


点赞和在看就是最大的支持❤️

[Read in Cubox](https://cubox.pro/web/card/7128377660480160628)
