---
id: "7128378168716559893"
cubox_url: https://cubox.pro/web/card/7128378168716559893
url: https://mp.weixin.qq.com/s/By_zRjBhjD07A9S-_pNOow
tags:
  - Skill/data-analysis
---
# Pandas一行代码绘制25种美图



[Read in Cubox](https://cubox.pro/web/card/7128378168716559893)  
[Read Original](https://mp.weixin.qq.com/s/By_zRjBhjD07A9S-_pNOow)  

---


---

\## 📖 正文全文

# Pandas一行代码绘制25种美图

[mp.weixin.qq.com](https://mp.weixin.qq.com/s/By_zRjBhjD07A9S-_pNOow)pythonic生物人 凹凸数据


![图片](https://image.cubox.pro/cardImg/2023112617030942843/36809.jpg?imageMogr2/quality/90/ignore-error/1)

大家好，我是小五🧐

今天介绍一下，如何用Pandas的一行代码绘制 25 种美图。
![图片](https://image.cubox.pro/cardImg/2023112617031099532/54487.jpg?imageMogr2/quality/90/ignore-error/1)

本文涉及：
> 单组折线图、多组折线图、单组条形图、多组条形图、堆积条形图、水平堆积条形图、直方图、分面直方图、箱图、面积图、堆积面积图、散点图、单组饼图、多组饼图、分面图、hexbin图、andrews_curves图、核密度图、parallel_coordinates图、autocorrelation_plot图、radviz图、bootstrap_plot图、子图（subplot）、子图任意排列、图中绘制数据表格

Pandas可视化主要依赖下面两个函数：

*
  pandas.DataFrame.plot

*https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.plot.html?highlight=plot\#pandas.DataFrame.plot*

*
  pandas.Series.plot

*https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.plot.html?highlight=plot\#pandas.Series.plot*

可绘制下面几种图，注意Dataframe和Series的细微差异：'area', 'bar', 'barh', 'box', 'density', 'hexbin', 'hist', 'kde', 'line', 'pie', 'scatter'
![图片](https://image.cubox.pro/cardImg/2023112617031087432/64573.jpg?imageMogr2/quality/90/ignore-error/1)

导入依赖包

    importmatplotlib.pyplotasplt
    importnumpyasnp
    importpandasaspd
    frompandasimportDataFrame,Series
    plt.style.use('dark_background')\#设置绘图风格

\#\## 1、单组折线图

    np.random.seed(0)\#使得每次生成的随机数相同
    ts=pd.Series(np.random.randn(1000),index=pd.date_range("1/1/2000",periods=1000))
    ts1=ts.cumsum()\#累加
    ts1.plot(kind="line")\#默认绘制折线图

![图片](https://image.cubox.pro/cardImg/2023112617031130494/69670.jpg?imageMogr2/quality/90/ignore-error/1)

\#\## 2、多组折线图

    np.random.seed(0)
    df=pd.DataFrame(np.random.randn(1000,4),index=ts.index,columns=list("ABCD"))
    df=df.cumsum()
    df.plot()\#默认绘制折线图

![图片](https://image.cubox.pro/cardImg/2023112617031182346/48328.jpg?imageMogr2/quality/90/ignore-error/1)

\#\## 3、单组条形图

    df.iloc[5].plot(kind="bar")

![图片](https://image.cubox.pro/cardImg/2023112617031246752/30016.jpg?imageMogr2/quality/90/ignore-error/1)

\#\## 4、多组条形图

    df2=pd.DataFrame(np.random.rand(10,4),columns=["a","b","c","d"])
    df2.plot.bar()

![图片](https://image.cubox.pro/cardImg/2023112617031220659/40916.jpg?imageMogr2/quality/90/ignore-error/1)

\#\## 5、堆积条形图

    df2.plot.bar(stacked=True)

![图片](https://image.cubox.pro/cardImg/2023112617031263354/47201.jpg?imageMogr2/quality/90/ignore-error/1)

\#\## 6、水平堆积条形图

    df2.plot.barh(stacked=True)

![图片](https://image.cubox.pro/cardImg/2023112617031249157/23419.jpg?imageMogr2/quality/90/ignore-error/1)

\#\## 7、直方图

    df4=pd.DataFrame(
    {
    "a":np.random.randn(1000)+1,
    "b":np.random.randn(1000),
    "c":np.random.randn(1000)-1,
    },
    columns=["a","b","c"],
    )
    df4.plot.hist(alpha=0.8)

![图片](https://image.cubox.pro/cardImg/2023112617031281189/64336.jpg?imageMogr2/quality/90/ignore-error/1)

\#\## 8、分面直方图

    df.diff().hist(color="r",alpha=0.9,bins=50)

![图片](https://image.cubox.pro/cardImg/2023112617031366474/30687.jpg?imageMogr2/quality/90/ignore-error/1)

\#\## 9、箱图

    df=pd.DataFrame(np.random.rand(10,5),columns=["A","B","C","D","E"])
    df.plot.box()

![图片](https://image.cubox.pro/cardImg/2023112617031342968/84619.jpg?imageMogr2/quality/90/ignore-error/1)

\#\## 10、面积图

    df=pd.DataFrame(np.random.rand(10,4),columns=["a","b","c","d"])
    df.plot.area()

![图片](https://image.cubox.pro/cardImg/2023112617031335078/88685.jpg?imageMogr2/quality/90/ignore-error/1)

\#\## 11、堆积面积图

    df.plot.area(stacked=False)

![图片](https://image.cubox.pro/cardImg/2023112617031339655/57851.jpg?imageMogr2/quality/90/ignore-error/1)

\#\## 12、散点图

    ax=df.plot.scatter(x="a",y="b",color="r",label="Group1",s=90)
    df.plot.scatter(x="c",y="d",color="g",label="Group2",ax=ax,s=90)

![图片](https://image.cubox.pro/cardImg/2023112617031417988/95216.jpg?imageMogr2/quality/90/ignore-error/1)

\#\## 13、单组饼图

    series=pd.Series(3*np.random.rand(4),index=["a","b","c","d"],name="series")
    series.plot.pie(figsize=(6,6))

![图片](https://image.cubox.pro/cardImg/2023112617031420546/45992.jpg?imageMogr2/quality/90/ignore-error/1)

\#\## 14、多组饼图

    df=pd.DataFrame(
    3*np.random.rand(4,2),index=["a","b","c","d"],columns=["x","y"]
    )
    df.plot.pie(subplots=True,figsize=(8,4))

![图片](https://image.cubox.pro/cardImg/2023112617031426941/60435.jpg?imageMogr2/quality/90/ignore-error/1)

\#\## 15、分面图

    importmatplotlibasmpl
    mpl.rc_file_defaults()
    plt.style.use('fivethirtyeight')
    frompandas.plottingimportscatter_matrix
    df=pd.DataFrame(np.random.randn(1000,4),columns=["a","b","c","d"])
    scatter_matrix(df,alpha=0.2,figsize=(6,6),diagonal="kde")
    plt.show()

![图片](https://image.cubox.pro/cardImg/2023112617031567055/27398.jpg?imageMogr2/quality/90/ignore-error/1)

\#\## 16、hexbin图

    df=pd.DataFrame(np.random.randn(1000,2),columns=["a","b"])
    df["b"]=df["b"]+np.arange(1000)
    df.plot.hexbin(x="a",y="b",gridsize=25)

![图片](https://image.cubox.pro/cardImg/2023112617031562538/63178.jpg?imageMogr2/quality/90/ignore-error/1)

\#\## 17、andrews_curves图

    frompandas.plottingimportandrews_curves
    mpl.rc_file_defaults()
    data=pd.read_csv("iris.data.txt")
    plt.style.use('dark_background')
    andrews_curves(data,"Name")

![图片](https://image.cubox.pro/cardImg/2023112617031554575/70867.jpg?imageMogr2/quality/90/ignore-error/1)

\#\## 18、核密度图

    ser=pd.Series(np.random.randn(1000))
    ser.plot.kde()

![图片](https://image.cubox.pro/cardImg/2023112617031511235/98563.jpg?imageMogr2/quality/90/ignore-error/1)

\#\## 19、parallel_coordinates图

    frompandas.plottingimportparallel_coordinates
    data=pd.read_csv("iris.data.txt")
    plt.figure()
    parallel_coordinates(data,"Name")

![图片](https://image.cubox.pro/cardImg/2023112617031629843/58637.jpg?imageMogr2/quality/90/ignore-error/1)

\#\## 20、autocorrelation_plot图

    frompandas.plottingimportautocorrelation_plot
    plt.figure();
    spacing=np.linspace(-9*np.pi,9*np.pi,num=1000)
    data=pd.Series(0.7*np.random.rand(1000)+0.3*np.sin(spacing))
    autocorrelation_plot(data)

![图片](https://image.cubox.pro/cardImg/2023112617031789252/47899.jpg?imageMogr2/quality/90/ignore-error/1)

\#\## 21、radviz图

    frompandas.plottingimportradviz
    data=pd.read_csv("iris.data.txt")
    plt.figure()
    radviz(data,"Name")

![图片](https://image.cubox.pro/cardImg/2023112617031757898/50784.jpg?imageMogr2/quality/90/ignore-error/1)

\#\## 22、bootstrap_plot图

    frompandas.plottingimportbootstrap_plot
    data=pd.Series(np.random.rand(1000))
    bootstrap_plot(data,size=50,samples=500,color="grey")

![图片](https://image.cubox.pro/cardImg/2023112617031764098/15435.jpg?imageMogr2/quality/90/ignore-error/1)

\#\## 23、子图（subplot）

    df=pd.DataFrame(np.random.randn(1000,4),index=ts.index,columns=list("ABCD"))
    df.plot(subplots=True,figsize=(6,6))

![图片](https://image.cubox.pro/cardImg/2023112617031819695/69554.jpg?imageMogr2/quality/90/ignore-error/1)

\#\## 24、子图任意排列

    df.plot(subplots=True,layout=(2,3),figsize=(6,6),sharex=False)

![图片](https://image.cubox.pro/cardImg/2023112617031870180/77724.jpg?imageMogr2/quality/90/ignore-error/1)

    fig,axes=plt.subplots(4,4,figsize=(9,9))
    plt.subplots_adjust(wspace=0.5,hspace=0.5)
    target1=[axes[0][0],axes[1][1],axes[2][2],axes[3][3]]
    target2=[axes[3][0],axes[2][1],axes[1][2],axes[0][3]]
    df.plot(subplots=True,ax=target1,legend=False,sharex=False,sharey=False);
    (-df).plot(subplots=True,ax=target2,legend=False,sharex=False,sharey=False)

![图片](https://image.cubox.pro/cardImg/2023112617031918674/91096.jpg?imageMogr2/quality/90/ignore-error/1)

\#\## 25、图中绘制数据表格

    frompandas.plottingimporttable
    mpl.rc_file_defaults()
    \#plt.style.use('dark_background')
    fig,ax=plt.subplots(1,1)
    table(ax,np.round(df.describe(),2),loc="upperright",colWidths=[0.2,0.2,0.2]);
    df.plot(ax=ax,ylim=(0,2),legend=None);

![图片](https://image.cubox.pro/cardImg/2023112617031996257/40445.jpg?imageMogr2/quality/90/ignore-error/1)

更多pandas可视化精进资料：*https://pandas.pydata.org/pandas-docs/stable/user_guide/cookbook.html\#cookbook-plotting*


\## 最近有啥书？

Python数据分析从入门到精通(微课视频版) ：技术讲解透彻 （1）知识体系完善，从Python基础入门，到数据处理介绍，到数据实战分析，流程图、各种数据可视化图示等，简单易学。（2）配视频讲解，打消读者未学先怯的心理， 给初学者一个定心丸。点击即可查看详情！👇


**![图片](https://image.cubox.pro/cardImg/2023112617031952231/73773.jpg?imageMogr2/quality/90/ignore-error/1)**


![图片](https://image.cubox.pro/cardImg/2023112617032038897/44407.jpg?imageMogr2/quality/90/ignore-error/1)

点击这里，阅读更多数据文章！


[Read in Cubox](https://cubox.pro/web/card/7128378168716559893)
