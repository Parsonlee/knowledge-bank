---
id: "6971137441600113081"
cubox_url: https://cubox.pro/web/card/6971137441600113081
url: https://mp.weixin.qq.com/s?__biz=MzI0MzU2NzQ1OA==&mid=2247520036&idx=2&sn=2ce0bd45d93a3920fbde0a4f18808a5c&chksm=e969d129de1e583f7105fa65d0d4f9d7f4025431f585ab4c35b150b36c1143995af9011d6294&mpshare=1&scene=1&srcid=0918K5LMwqGtMREoX20X0PPh&sharer_sharetime=1663500240590&sharer_shareid=e12ed373ec9a1ae2d7b1d1a5274c5e8e
tags:
  - Skill/data-analysis
  - 面试
---
# 超强图解 Pandas，建议收藏



[Read in Cubox](https://cubox.pro/web/card/6971137441600113081)  
[Read Original](https://mp.weixin.qq.com/s?__biz=MzI0MzU2NzQ1OA==&mid=2247520036&idx=2&sn=2ce0bd45d93a3920fbde0a4f18808a5c&chksm=e969d129de1e583f7105fa65d0d4f9d7f4025431f585ab4c35b150b36c1143995af9011d6294&mpshare=1&scene=1&srcid=0918K5LMwqGtMREoX20X0PPh&sharer_sharetime=1663500240590&sharer_shareid=e12ed373ec9a1ae2d7b1d1a5274c5e8e)  

---


---

\## 📖 正文全文

# 超强图解 Pandas，建议收藏

[mp.weixin.qq.com](http://mp.weixin.qq.com/s?__biz=MzI0MzU2NzQ1OA==&mid=2247520036&idx=2&sn=2ce0bd45d93a3920fbde0a4f18808a5c&chksm=e969d129de1e583f7105fa65d0d4f9d7f4025431f585ab4c35b150b36c1143995af9011d6294&mpshare=1&scene=1&srcid=0918K5LMwqGtMREoX20X0PPh&sharer_sharetime=1663500240590&sharer_shareid=e12ed373ec9a1ae2d7b1d1a5274c5e8e\#rd)Python人工智能技术


点击上方"**Python人工智能技术** "关注，星标或者置顶   


22点24分准时推送，第一时间送达

后台回复"**大礼包**"，送你特别福利  

> 编辑：乐乐 \| 来自：网络

[Pythn人工智能技术(ID:coder_experience)第 915 期推文](http://mp.weixin.qq.com/s?__biz=MzI0MzU2NzQ1OA==&mid=2247489525&idx=1&sn=26e9ce9d935a845d03ce4a3d30ebc975&chksm=e96a49f8de1dc0eeda78a0f1fa1ab74bfa13222fecbb924f52e59b59cd8b431d6e0fd00cc1cb&scene=21\#wechat_redirect)

上一篇：[4 个 Python 项目管理与构建工具，建议收藏！](http://mp.weixin.qq.com/s?__biz=MzI0MzU2NzQ1OA==&mid=2247519955&idx=1&sn=f326e161e7e41fef261aeac658b20ae4&chksm=e969d0dede1e59c8ab135fa853cb5055aed962b6f90ab6cf0260e0a6fccf8baa286780c1b18f&scene=21\#wechat_redirect)


**正文**


**大家好，我是Python人工智能技术**

`Pandas`是数据挖掘常见的工具，掌握使用过程中的函数是非常重要的。本文将借助可视化的过程，讲解`Pandas`的各种操作。

\## sort_values

    (dogs[dogs['size']=='medium'].sort_values('type').groupby('type').median())

执行步骤：

*
  size列筛选出部分行
*
  然后将行的类型进行转换
*
  按照type列进行分组，计算中位数

![](https://image.cubox.pro/article/2022072609142483833/96003.jpg) ![](https://image.cubox.pro/article/2022072609142415992/42345.jpg) ![](https://image.cubox.pro/article/2022072609142490973/67528.jpg) ![](https://image.cubox.pro/article/2022082517215510640/28507.jpg)

\## selecting a column

    dogs['longevity']

![](https://image.cubox.pro/article/2022072609142436708/90492.jpg)

\## groupby + mean

    dogs.groupby('size').mean()

执行步骤：

*
  将数据按照size进行分组
*
  在分组内进行聚合操作

![](https://image.cubox.pro/article/2022072609142450506/76948.jpg) ![](https://image.cubox.pro/article/2022082517215583545/79931.jpg)

\## grouping multiple columns

    dogs.groupby(['type','size'])

![](https://image.cubox.pro/article/2022082517215564308/24179.jpg)

\## groupby + multi aggregation

    (dogs.sort_values('size').groupby('size')['height'].agg(['sum','mean','std']))

```
![](https://image.cubox.pro/article/2022070710525970340/73715.jpg)![](https://image.cubox.pro/article/2022070710525970340/73715.jpg)![](https://image.cubox.pro/article/2022070710525970340/73715.jpg)![](https://image.cubox.pro/article/2022070710525970340/73715.jpg)![](https://image.cubox.pro/article/2022070710525970340/73715.jpg)![](https://image.cubox.pro/article/2022070710525970340/73715.jpg)http://mp.weixin.qq.com/s?__biz=MzU1NjYxNDc2OQ==&mid=2247499237&idx=1&sn=5a7a7afbf9c3c1d30a3ee9ad35fc6f18&chksm=fbc0e8fbccb761ed689c3708d48b7d04fa65546318ac4b236b390c88b4c59c73e506cd0c84b0&scene=21\#wechat_redirect
```

执行步骤

*
  按照size列对数据进行排序
*
  按照size进行分组
*
  对分组内的height进行计算

![](https://image.cubox.pro/article/2022072609142453392/83338.jpg) ![](https://image.cubox.pro/article/2022072609142428457/50017.jpg) ![](https://image.cubox.pro/article/2022072609142475050/66193.jpg) ![](https://image.cubox.pro/article/2022072609142468168/37360.jpg)

\## filtering for columns

    df.loc[:,df.loc['two']<=20]

![](https://image.cubox.pro/article/2022082517215548202/96545.jpg)

\## filtering for rows

    dogs.loc[(dogs['size']=='medium')&(dogs['longevity']>12),'breed']

![](https://image.cubox.pro/article/2022082517215568529/33484.jpg)

微信搜索公众号：架构师指南，回复：架构师 领取资料 。

\## dropping columns

    dogs.drop(columns=['type'])

![](https://image.cubox.pro/article/2022082517215587115/21019.jpg)

\## joining

    ppl.join(dogs)

![](https://image.cubox.pro/article/2022072609142437299/61263.jpg)

\## merging

    ppl.merge(dogs,left_on='likes',right_on='breed',how='left')

![](https://image.cubox.pro/article/2022072609142441866/54916.jpg)

\## pivot table

另外，搜索公众号顶级算法后台回复"算法"，获取一份惊喜礼包。

    dogs.pivot_table(index='size',columns='kids',values='price')

![](https://image.cubox.pro/article/2022082517215566735/79775.jpg)

\## melting

    dogs.melt()

![](https://image.cubox.pro/article/2022082517215554456/87718.jpg)

\## pivoting

    dogs.pivot(index='size',columns='kids')

![](https://image.cubox.pro/article/2022072609142481918/43133.jpg)

\## stacking column index

    dogs.stack()

![](https://image.cubox.pro/article/2022072609142442839/79794.jpg)

\## unstacking row index

    dogs.unstack()

![](https://image.cubox.pro/article/2022072609142448146/35097.jpg)

\## resetting index

    dogs.reset_index()

![](https://image.cubox.pro/article/2022072609142412850/33698.jpg)

\## setting index

    dogs.set_index('breed')

![](https://image.cubox.pro/article/2022072609142442984/39791.jpg)

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

![](https://image.cubox.pro/article/2022052110045163821/60461.jpg)


--END--

**往日热文：**

[看看人家那物业管理系统，那叫一个优雅（附源码）](http://mp.weixin.qq.com/s?__biz=MzI0MzU2NzQ1OA==&mid=2247510334&idx=2&sn=309a6d0c769625864695246fefb4bf64&chksm=e969f733de1e7e258bbf242ace3eeef61284ac31ce5beb5074bc2b7eee4cd455251e8b547fc5&scene=21\#wechat_redirect)  

[一款神仙接私活儿软件，吊到不行！](http://mp.weixin.qq.com/s?__biz=MzI0MzU2NzQ1OA==&mid=2247510254&idx=1&sn=5d9468461da7df149796d9dce6c24e99&chksm=e969f6e3de1e7ff53626265b4aea0dd0fe4718a2e4286eb4241fa62e79ee9c618bd991f6ba40&scene=21\#wechat_redirect)  

[保姆级别！带你搭建一台服务器！](http://mp.weixin.qq.com/s?__biz=MzI0MzU2NzQ1OA==&mid=2247510687&idx=2&sn=aad0db260df36d4bfb94b0a28ec92c47&chksm=e969f492de1e7d84dab0d87f6ba9d491a1992c09b91da3e9b41f04aa9e19e6760b50ea7e231a&scene=21\#wechat_redirect)

[AI画作拿下比赛一等奖惹怒人类艺术家，主办方：照常颁奖！](http://mp.weixin.qq.com/s?__biz=MzI0MzU2NzQ1OA==&mid=2247519790&idx=2&sn=fccb0cf7ffa56d3835e275c8d6f9d358&chksm=e969d023de1e593512c970129b279e746600a48dce15bcf7103f1fb6fc249113d401d9fe74f8&scene=21\#wechat_redirect)  

[Docker 入门终极指南，详细版！别再说不会用 Docker 了！](http://mp.weixin.qq.com/s?__biz=MzI0MzU2NzQ1OA==&mid=2247519845&idx=2&sn=82434229e72bf5518c4dbf0bcdbc52d1&chksm=e969d068de1e597e7b6d2b0503891d70bc019b107ee56e9f0873d5d81a419e62d97c4ef4f8cc&scene=21\#wechat_redirect)  

[Python 处理 PDF：PyMuPDF 的安装与使用！](http://mp.weixin.qq.com/s?__biz=MzI0MzU2NzQ1OA==&mid=2247519931&idx=2&sn=f6154c86cfefa0771f9b0a14df93f4c3&chksm=e969d0b6de1e59a07010264fa6ab38e05677d2fa7433badaa6a089b769d1e7eac2c52007a015&scene=21\#wechat_redirect)  

[mysql 最朴素的监控方式](http://mp.weixin.qq.com/s?__biz=MzI0MzU2NzQ1OA==&mid=2247519955&idx=2&sn=6d628e545aa603cb99b6d4d9e22c2dc0&chksm=e969d0dede1e59c837095d8b5b49ad66bcfcfa9f815b4ec8ac6865965584112db5f8b4081423&scene=21\#wechat_redirect)  

[Github突然给Trending热榜判了「死刑」！倒计时30天](http://mp.weixin.qq.com/s?__biz=MzI0MzU2NzQ1OA==&mid=2247519506&idx=2&sn=47c73403bdb6bb2c9747efb3fb16c34f&chksm=e969d31fde1e5a0995f7d91dcee3f86c6dd63375adb14ce612c9c34ec7e8236b4685dedccb20&scene=21\#wechat_redirect)  

[](http://mp.weixin.qq.com/s?__biz=MzI0MzU2NzQ1OA==&mid=2247517523&idx=2&sn=f37e84dcda87d1c9321789574e858ef5&chksm=e969db5ede1e5248fd839b01c29eb0c70dba2c98524d3b6ec98a966bb2eb6bacf30e240ee66e&scene=21\#wechat_redirect)[就业市场寒气逼人，UC伯克利博士详谈美国找工作经验](http://mp.weixin.qq.com/s?__biz=MzI0MzU2NzQ1OA==&mid=2247519620&idx=2&sn=d6f0fd345a300c99e7ab7a0c7184c004&chksm=e969d389de1e5a9fa698240ec264de2caaa5f8354b592488621c9f502f2312ba5c1291169ba8&scene=21\#wechat_redirect)  

[厚度仅2.5毫米，重60克，英伟达\&斯坦福做出了超轻薄VR眼镜](http://mp.weixin.qq.com/s?__biz=MzI0MzU2NzQ1OA==&mid=2247519674&idx=2&sn=b967e4733c527e690ef2f3e08fd72c5e&chksm=e969d3b7de1e5aa15161d6ad15be910e54c766b2455d4e29966215a725fa6853edebf7ad030d&scene=21\#wechat_redirect)  

[UCLA 蒋陈凡夫：从转系生到终身教授，十二年图形学物理模拟的自我回顾](http://mp.weixin.qq.com/s?__biz=MzI0MzU2NzQ1OA==&mid=2247519754&idx=2&sn=17a20cd6441a0916ee55bc278c1d34bc&chksm=e969d007de1e591190b56441183e895c6b320936ab28a449e518a6abbc0c2f0f9199e2f908d7&scene=21\#wechat_redirect)  

```
Python程序员深度学习的"四大名著"：
![](https://image.cubox.pro/article/2022010822325115656/93663.jpg)这四本书着实很不错！我们都知道现在机器学习、深度学习的资料太多了，面对海量资源，往往陷入到"无从下手"的困惑出境。而且并非所有的书籍都是优质资源，浪费大量的时间是得不偿失的。给大家推荐这几本好书并做简单介绍。**获得方式：**
  
   
  
      
   **1.扫码关注本** **公众号**
  
   
  
      
  
   
  
      
   **2.后台回复关键词：** **名著**
  
   
  
      ![](https://image.cubox.pro/article/2022052110044979184/45257.jpg)
  
   
  
      
   ▲长按扫描关注，回复名著即可获取
  
   
  
      
```

[Read in Cubox](https://cubox.pro/web/card/6971137441600113081)
