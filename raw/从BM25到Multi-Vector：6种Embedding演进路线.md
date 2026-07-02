---
id: "7367863515257768722"
cubox_url: https://cubox.pro/web/card/7367863515257768722
url: https://mp.weixin.qq.com/s/wkcFxpHXaHLTm0K9Dv3ihQ?mpshare=1&scene=1&srcid=0917TePDkxU8B4tsTDHcA5aW&sharer_shareinfo=cef0b966941167a9d527bab97225a2f2&sharer_shareinfo_first=cef0b966941167a9d527bab97225a2f2&from=industrynews&color_scheme=light
tags:
  - RAG/embedding
  - RAG
---
# 从BM25到Multi-Vector：6种Embedding演进路线



[Read in Cubox](https://cubox.pro/web/card/7367863515257768722)  
[Read Original](https://mp.weixin.qq.com/s/wkcFxpHXaHLTm0K9Dv3ihQ?mpshare=1&scene=1&srcid=0917TePDkxU8B4tsTDHcA5aW&sharer_shareinfo=cef0b966941167a9d527bab97225a2f2&sharer_shareinfo_first=cef0b966941167a9d527bab97225a2f2&from=industrynews&color_scheme=light)  

---


---

\## 📖 正文全文

# 从BM25到Multi-Vector：6种Embedding演进路线

[mp.weixin.qq.com](https://mp.weixin.qq.com/s/wkcFxpHXaHLTm0K9Dv3ihQ?mpshare=1&scene=1&srcid=0917TePDkxU8B4tsTDHcA5aW&sharer_shareinfo=cef0b966941167a9d527bab97225a2f2&sharer_shareinfo_first=cef0b966941167a9d527bab97225a2f2&from=industrynews&color_scheme=light)CourseAI PaperAgent


本公众号主要关注NLP、CV、LLM、RAG、Agent等AI前沿技术，免费分享业界实战案例与课程，助力您全面拥抱AIGC。
![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_jpg%2FJnQiaTcHwIEkSP5MFrnGeuRG5EvwEXdpspEPVSXh8c18C1w8MOVC4dAl8RnuaJXasXJZezQWlS7LpicyId8vALmw%2F640%3Fwx_fmt%3Djpeg%26from%3Dappmsg%26tp%3Dwebp%26wxfrom%3D5%26wx_lazy%3D1%23imgIndex%3D0&valid=false)

\## 一、Sparse Embedding（关键词式稀疏向量）


|  维度   |           描述           |
|-------|------------------------|
| 典型实现  | TF-IDF、BM25、SPLADE     |
| 向量形态  | 50 000+ 维，\>95 % 位置为 0 |
| 相似度计算 | 余弦或点积，仅激活维度参与运算        |


**痛点**

*
  只做"精确关键词匹配"，同义词/句式变化即失效
*
  高维稀疏导致存储、索引膨胀

**效果**

*
  关键词命中时精度极高，可解释性强（能直接看到"哪一词"得分）

**案例**   
新闻版权去重：编辑把原文 5 个核心实体词作为查询，用 BM25 检索，疑似抄袭文章 10 ms 内返回，准确率达 98 %。

**一句话选型**   
"只要关键词就能搞定，千万别上神经网络。"

*** ** * ** ***

\## 二、Dense Embedding（语义级稠密向量）


|  维度   |                  描述                   |
|-------|---------------------------------------|
| 典型模型  | text-embedding-3-large、BGE、E5-mistral |
| 向量形态  | 256\~1536 维，全部非零                      |
| 相似度计算 | 余弦距离                                  |


**痛点**

*
  需要 GPU/CPU 做推理，单条 10\~100 ms
*
  对字面不匹配但语义相近的查询才显威力

**效果**

*
  捕捉同义、上下位、跨语言语义
*
  维度越低信息越"挤"，需折中精度与存储

**案例**   
SaaS 客服 FAQ 检索：用户口语化提问"我忘了密码怎么办"，稠密向量命中"如何重置登录密码"，TOP1 命中率从关键词的 62 % → 89 %。

**一句话选型**   
"只要用户会'人话'提问，就用 Dense。"

*** ** * ** ***

\## 三、Quantized Embedding（压缩版稠密）


|  维度  |            描述            |
|------|--------------------------|
| 压缩手段 | 把 float32 → int8 / uint8 |
| 压缩率  | 75 % 体积下降，召回下降 \<1 %（实验） |


**痛点**

*
  必须重新训练或做 Post-Training Quantization
*
  极低比特（4 bit）会出现明显"值域截断"误差

**效果**

*
  内存 \*4↓，磁盘 \*4↓，向量检索 QPS \*2↑
*
  适合一次性加载进内存的 ANN 引擎（FAISS-IVF、Milvus）

**案例**   
电商 2 亿商品向量原占 2.4 TB，量化后 600 GB，全内存检索 P99 延迟 18 ms → 9 ms。

**一句话选型**   
"内存就是钱，量化就是省。"

*** ** * ** ***

\## 四、Binary Embedding（极致 0/1 压缩）


|  维度  |               描述               |
|------|--------------------------------|
| 编码方式 | 对 float 向量做 sign() 或 ITQ 旋转二值化 |
| 存储   | 1 bit × dim，比 float32 省 32×    |


**痛点**

*
  汉明距离只能排序，无法得到真实相似度分值
*
  精度平均下降 5\~15 %

**效果**

*
  计算改 XOR + popcount，CPU 单核可过 1 亿次/秒
*
  手机端离线检索首选

**案例**   
安卓相册"重复照片清理"：把 256 维 CNN 向量二值化后，在 3 万张照片里找相似，耗时 80 ms，耗电 \<1 %。

**一句话选型**   
"设备端、离线、大基数、只关心快------直接上 Binary。"

*** ** * ** ***

\## 五、Matryoshka (Variable Dimension) 嵌入


|  维度  |               描述                |
|------|---------------------------------|
| 训练技巧 | 把 1024 维向量分层加权，前 64 维已含 80 % 信息 |
| 调用方式 | 同一文件，按需截断 dim=64/128/256...     |


**痛点**

*
  必须选用官方"MRL 训练"模型；普通模型硬截断会崩
*
  早期维数太短时，不同语义容易"挤"在一起

**效果**

*
  一套存储，支持"性能 ↔ 精度"滑杆
*
  低维阶段 QPS 提升 3\~5 倍，高维阶段精度逼近完整向量

**案例**   
初创公司先做 100 万文档 POC，用 64 维跑 Demo；客户签约后秒切 512 维上线，无需重新导出数据。

**一句话选型**   
"老板一会要 Demo 快，一会要上线准------Matryoshka 让你不被砍需求。"

*** ** * ** ***

\## 六、Multi-Vector (ColBERT 式"后期交互")


|  维度   |                      描述                      |
|-------|----------------------------------------------|
| 表征方式  | 一段文本 → 128 个 128 维向量（每 token 一个）             |
| 相似度计算 | 先求每 query token 与 doc token 最大余弦，再求和（MaxSim） |


**痛点**

*
  索引体积 \*100↑，需要专用压缩（ColBERTv2 残差+量化）
*
  检索阶段计算量远高于单向量

**效果**

*
  实现"词-词"细粒度匹配，长文档召回提升 10\~20 %
*
  可解释：能高亮"哪一句"被命中

**案例**   
律所 50 万判决文书检索：用 ColBERT 后，律师输入"员工加班工资如何计算"，返回段落级命中，文书阅读时间从 15 分钟 → 3 分钟。

**一句话选型**   
"长文本、专业领域、必须定位到段落------Multi-Vector 是王道。"

*** ** * ** ***

\## 七、如何选对方案？


|  场景关键词   |     首选方案     |     备选     |
|----------|--------------|------------|
| 关键词精确匹配  | Sparse       | ---        |
| 通用语义搜索   | Dense        | Matryoshka |
| 内存/磁盘告急  | Quantized    | Binary     |
| 设备端离线快搜  | Binary       | ---        |
| 长文档段落定位  | Multi-Vector | ---        |
| 老板需求一天三变 | Matryoshka   | ---        |


*** ** * ** ***

\## 八、方案选择的步骤

可以根据"数据规模、延迟、内存、精度、可解释性"五要素，根据不同的场景选择可用的嵌入方案。

1.
   先用 Dense 打 baseline，再决定"要不要更复杂"。
2.
   量化/二值化前，务必在业务数据上测"召回@K 下降"曲线，别只看压缩率。
3.
   Multi-Vector 索引体积大，用 ColBERTv2 的"残差+量化"可把 100 GB 压到 8 GB，仍保持 95 % 精度。
4.
   最终上线时，把"Sparse + Dense"做 Hybrid Ranking 往往最稳妥：Sparse 保精度，Dense 保召回，权重可调。


推荐阅读


* •[挑战Transformer，谷歌全新架构Mixture-of-Recursions](https://mp.weixin.qq.com/s?__biz=Mzk0MTYzMzMxMA==&mid=2247495548&idx=1&sn=87dd3f518c89602c9259c34fcc08e447&scene=21\#wechat_redirect)

<!-- -->

* •[快手开源多模态Keye-VL-1.5-8B，本地视觉Agent有救了](https://mp.weixin.qq.com/s?__biz=Mzk0MTYzMzMxMA==&mid=2247497114&idx=1&sn=8bf1d9630e5cfbbdbda874121f189daa&scene=21\#wechat_redirect)  

* •[从Agent到FlowAgent再到Multi-Agent，落地实践细节都在这了](https://mp.weixin.qq.com/s?__biz=Mzk0MTYzMzMxMA==&mid=2247497024&idx=1&sn=958ac35c85dd5590a5566e4b96cafc67&scene=21\#wechat_redirect)

  • [从DeepSeek-V3到Kimi K2：八种现代LLM架构大比较](https://mp.weixin.qq.com/s?__biz=Mzk0MTYzMzMxMA==&mid=2247497024&idx=1&sn=958ac35c85dd5590a5566e4b96cafc67&scene=21\#wechat_redirect)


*** ** * ** ***

每天一篇大模型Paper来锻炼我们的思维\~已经读到这了，不妨点个👍、❤️、↗️三连，加个星标⭐，不迷路哦

[Read in Cubox](https://cubox.pro/web/card/7367863515257768722)
