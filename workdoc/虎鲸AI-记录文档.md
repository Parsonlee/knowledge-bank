此文档用于记录**虎鲸AI**项目的技术实现细节

## 

## 相关文档

- 发版记录文档：[虎鲸AI产品发版管理](https://doc.weixin.qq.com/smartsheet/s3_AE0AOAbuAEoCNXG6BgTpXSDKCvPDp?scode=AEQA-QfUAA0outa9g0AE0AOAbuAEo)

- 精简版技术实现文档：[AIBI技术实现文档](https://doc.weixin.qq.com/doc/w3_AT0AdAbcAO80CcsFbLZTOCC35WVD8?scode=AEQA-QfUAA0GZRxYEVAT0AdAbcAO8)（更新后可用于项目汇报）

- 旧需求文档：[虎鲸AI需求文档](https://doc.weixin.qq.com/doc/w3_AE0AOAbuAEosEniRx8zROaap09fNU?scode=AEQA-QfUAA0OAIgRzSAE0AOAbuAEo)

- 学习参考：[Text2SQL-相关IDEAS](https://doc.weixin.qq.com/doc/w3_AT0AdAbcAO80eLnSAWnRoSdhxnQt2?scode=AEQA-QfUAA0ZTdVCD0AT0AdAbcAO8)

## 

## 备忘

- **代码地址**

  - 后端仓库：<http://new-gitlab.yiyaowang.com/zhongtai_alg/aibi_service>

  - ~~后端saas版：http://new-gitlab.yiyaowang.com/zhongtai_alg/aibi-service-saas~~

  - ES检索：<http://new-gitlab.yiyaowang.com/zhongtai_alg/text2sql_es>

- **StarRocks数据库：**

[手动部署 StarRocks \|
StarRocks](https://docs.starrocks.io/zh/docs/deployment/deploy_manually)

[StarRocks内存管理](https://docs.starrocks.io/zh/docs/administration/management/resource_management/Memory_management/#%E6%9F%A5%E7%9C%8B%E5%86%85%E5%AD%98%E4%BD%BF%E7%94%A8)

- **线上环境Dify**：

> 172.29.24.6（生产）：<https://chatbi-dify.111.com.cn>

- **已弃用**（DEPRECATED）

## 测试用例（deprecated）

[虎鲸测试数据](https://doc.weixin.qq.com/sheet/e3_AD8ARwY0AEwjhU5M16eTpyJQ1umHf?scode=AEQA-QfUAA04mJKBcHAD8ARwY0AEw)

## 上线/发版checklist

[后端发版流水线](https://ledao.yiyaowang.com/app/628071e3c6a40/pipeline/bbb3f442ad4bb3713430cee0d870c22f/taskOutputs?page=1)\
[saas版后端发版流水线](https://ledao.yiyaowang.com/app/63ee0eb657993/pipeline/0630f63e59eda1589b99fae18e2ecc93/taskOutputs?page=1)

- **后端service：**

**step-1:** 将分支 push 到 master

**step-2:** 走流水线发布，同时更新两台生产机器的服务

**step-3:**
saas服务拉取upstream，最好cherry-pick合并指定commit，然后push和流水线发布

- **dify：**

**step-1:** 52（test） 所有dsl导出

**step-2:** 15（staging）
导入除"虎鲸AI"之外的app，更改工作流内接口URL。测试各项功能

**step-3:**
6（prod）volumes备份，导入除"虎鲸AI"之外的app，更改工作流内接口URL

# 虎鲸AI 1.0

## 指标查询（旧）

### V1-simple demo(Chatflow)

7.2------搭出简单demo，一次性生成代码

问题：

1.  需要研究出如何交互

2.  大宽表的分区字段

3.  知识库的搭建，比如枚举值字段的值应该在一次检索内全部拿到，用来校正用户的错误输入

7.3

1.  在第一步进行gpt的智能分类，按照用户的本轮query来决定走什么分支

2.  设置"核对信息"和"生成SQL"两条分支。

    a.  核对信息：实现用户和系统共同确认关键信息是否齐全，

    b.  生成SQL：首先将前面对话进行总结，明确意图+抽取关键信息，触发最终检索以确定字段名、数据类型等信息。然后生成对应的SQL

3.  （依照最终的app使用形式决定）将第一轮和后续询问轮区分，第一轮需要清空记忆，询问轮和知识库比对，根据gpt返回比对结果判断是否比对的上，若比对不上终止对话，代表用户提供了错误的信息

**问题**：意图识别可能出错 ；sql可能出错

7.4

1.  将整个系统拆分俩部分：

    a.  前面是解析用户的输入，通过逐步多轮对话以及核对检索结果来确认用于生成SQL的关键信息

    b.  用关键信息触发最终检索确定字段名称等，生成SQL并提交到[xxx]{.underline}执行，然后对执行结果进行解析，返回（比如解析错误信息，帮助用户更正输入）

2.  b流程封装成工作流工具，当前阶段：输入关键信息 -\> 生成 -\> 返回代码

**下一步**：对sql语句进行初步校准，当前遇到的问题有：

1.  字段名称出错

2.  出现无关的筛选条件

7.8------sql语句的生成已完成

下一步：总结信息版块prompt需继续调整

7.9 ------问题：多轮对话时不会遗忘上一轮的提问，导致总结信息时出错

**会议记录：**

1.  输出格式：

    a.  中间步骤的展示信息

    b.  需要根据用户的信息来决定是否展示中间信息

2.  与数据库的连接

3.  数据分析系统的搭建

### V2-complex chatflow

7.10-7.16

重新构思生成逻辑，**引入一些理论参考并进行实践尝试**

根据修订过后的表字段描述以及需求文档，**重新规划知识库构建方式**

**会议纪要**

1.  限制查询为50条：代码限制、代码审查、查询后显示

2.  限制实体查询：xxx=\'bac\' / xxx like \'abc\' / \...

3.  **每月第一天的特殊情况（用户询问本月，当天为xx-01）**

4.  **歧义词的问题：**

5.  查询和分析的流程解耦，

  ------------------------------ ---------- ------------------------------------------------
  待办事项                       是否完成   备注

  部署starRocks                  √          

  dify与starRocks连接            √          

  时间口径固定出库               √          

  业务域固定药城                 √          

  设计分支对话                   √          

  PE流程设计（实验（见下表））   √          

  解决歧义词                     √          1.后端返回2.前端配置按钮

  配置指标名称                   √          

  SQL执行完毕对话结束                       多轮对话解决歧义词，则需要前端设计结束对话功能
  ------------------------------ ---------- ------------------------------------------------

**table schema实验**

  ------------------------- ------------ ---------------------------------------------------- --------------------------------------------------
  实验名称                  实验结论     原因分析                                             备注

  RAG检索表info（列）       差           检索成功率跟字段信息的组织格式以及知识库切段强相关   rerank_large模型性能比base要好，但是推理时间较长

  表info插入system_prompt   好           单表情况下，字段信息长度在可接受的范围               尝试几种格式，平均token长度在2400左右

  表info的伪代码格式        好           同上                                                 同上

  表info的DDL代码格式       一般         在实体查询时容易出现错误                             数值字段查询正确，实体查询whse_name =
                                                                                              xxx出错。未来可考虑尝试多轮查询来逐步纠错
  ------------------------- ------------ ---------------------------------------------------- --------------------------------------------------

**流程性能测试**

+-----------+----------------------------------+---------+---------------------------+
| query类别 | query                            | time-v1 | v2（条件检查+部分gpt3.5） |
+-----------+----------------------------------+---------+---------------------------+
| KPI查询   | 本月药城GMV                      | 18.95   | 18.59                     |
|           +----------------------------------+---------+---------------------------+
|           | 本月药城自营GMV                  | 20.00   | 23.34                     |
|           +----------------------------------+---------+---------------------------+
|           | 本月自营GMV                      | 22.62   | 22.57                     |
|           +----------------------------------+---------+---------------------------+
|           | 药城重庆本月GMV                  | 18.18   | 21.53                     |
|           +----------------------------------+---------+---------------------------+
|           | 重庆GMV                          | 17.03   | 2(条件不齐全)             |
+-----------+----------------------------------+---------+---------------------------+
| 二维查询  | 本月药城每日GMV                  | 30.70   | 31.31                     |
|           +----------------------------------+---------+---------------------------+
|           | 本月药城每个仓的GMV              | 26.09   | 27.75                     |
+-----------+----------------------------------+---------+---------------------------+
| 多维      | 本月药城每日各仓GMV              | 69.52   | 35.71                     |
|           +----------------------------------+---------+---------------------------+
|           | 上周药城每日重庆仓和武汉仓的GMV  | 50.02   | 31.41                     |
|           +----------------------------------+---------+---------------------------+
|           | 本月药城各业务模式的GMV和Revenue | 33.71   | 27.53                     |
|           +----------------------------------+---------+---------------------------+
|           | 本月药城自营备货每日GMV和Revenue | 42.15   | 34.51                     |
+-----------+----------------------------------+---------+---------------------------+

**问题记录：**

*7/30：*

1.  **业务域判断和多轮对话发生冲突。**（现阶段改为在对话初始进行下拉框选择，或直接固定）

**多轮对话**功能和**执行sql结束对话**功能**无法并存**，若**开启多轮**需在**前端控制结束对话**

![descript](media/image1.png){width="1.1048917322834646in"
height="1.6843952318460194in"}![descript](media/image2.png){width="4.21875in"
height="0.8620352143482065in"}（[规则检查改为gpt根据上下文检查？权衡增加的时间成本]{.underline}）

*7/31：*

2.  **近义词和歧义词的冲突。**

<!-- -->

1.  代码生成先于规则处理：在展示的信息提取环节会自动**替换为真实值（图1）**

2.  规则处理先于代码生成：**则去触发全部字段的枚举值搜索来解决歧义，需要多轮对话（图2）**

![descript](media/image3.png){width="2.3221412948381452in"
height="2.2916666666666665in"}图1-配置**近义词重庆仓：**[gpt会认为重庆=重庆仓=重庆药业仓]{.underline}

![descript](media/image4.png){width="2.21875in"
height="2.2553805774278217in"}![descript](media/image5.png){width="2.1354166666666665in"
height="1.6681080489938758in"}图2-（[多轮对话+前端按钮？]{.underline}）

3.  **多轮对话和近义词歧义词无法共存**

![descript](media/image6.png){width="4.65625in"
height="0.8513615485564304in"}

![descript](media/image7.png){width="2.701788057742782in"
height="2.8541666666666665in"}

*8/1：*

针对问题3，现阶段方案：不设计分支，按流程依次执行：

***前提：**gpt进行无指定类别NER，返回一个 entities list*

*1
**枚举值查找：**设计为接收第二轮对话输入的真实枚举值，查找命中则继续，无命中则代表输入为第一轮对话*

*2
**近义词替换：**将输入中的近义词统一替换为具体值，并从NER实体中删除被替换的近义词实体*

*3
**歧义词检索：**将剩下的NER实体去枚举值表检索，返回多个值则输出全部歧义词并结束本轮对话*

### V3-Agent with tools

**问题：**DIFY的**Agent设计**是依照**ReAct**框架执行，即推理+行动+观察反馈

具体表现**为对用户问题先进行推理思考（是否需要外部信息），再借助工具的返回信息来生成回复答案。**

*thought(思考) -\> action(调用工具) -\> observation(观察工具的输出)*

![descript](media/image8.png){width="2.2488659230096237in"
height="1.7743153980752406in"}

目前Dify-Agent应用会将思考信息输出到消息框，因而会与FianlAnswer在内容上产生重复。

**解决办法：**以输出模板（prompt控制）的方式指定它的输出内容，但无法保证永远有效（*dify新版本已修复*）

**重构实验：**

系统解耦，三大模块：检错、解析+生成、执行

![descript](media/image9.png){width="3.15625in"
height="0.96544072615923in"}检错（[近义词歧义词处理，暂不加入流程]{.underline}）

![descript](media/image10.png){width="3.105520559930009in"
height="0.576839457567804in"}解析+生成

![descript](media/image11.png){width="3.1214916885389328in"
height="0.7258409886264217in"}执行

**架构示意图（新图）**

![descript](media/image12.png){width="6.299305555555556in"
height="2.368759842519685in"}

需要**展示关键信息提取**的中间过程，作为**Agent的思考过程**，用于让**用户校对答案**是否正确

- 方案1：**Agent自主提取关键并输出。**利用**检索**方式增加相关信息，便于生成正确关键信息

- 方案2：**代码生成工具返回。**code_generator返回：关键信息提取、SQL代码

**测试结果**

1.  方案1中Agent的输出不够稳定，同时会稳定产生，**Thought和FinalAnswer重复**的问题。

![descript](media/image13.png){width="1.90625in"
height="2.1629582239720033in"}

2.  需要用Prompt不断调整，**大体效果不错**

![descript](media/image14.png){width="1.96875in"
height="1.485916447944007in"}

**8月8会议**

1.  ~~日期问题，：*今年(1月1)、本周(星期一)、本月(当月1号)、本季度(当月1号)*~~

2.  ~~字段问题，dlvy_字段去掉所有除date外的内容~~

3.  ~~展示信息跟代码对应错误~~

4.  ~~当天的新数据无法查询（代码生成正确，数据库查询正确，返回null），需要搭配文案提示~~

**8/30**

在Agent应用中加入query解析，**处理近义词和歧义词的问题。针对这个处理做了以下工作：**

1.  **配置表中增加检索index。**enums_list表中添加了更多字段（field_name_cn,
    ambiguous_term)

2.  **query解析。**首先替换常见近义词（重庆仓），对剩下的部分进行**歧义实体召回**。

3.  **Agent工具配置。**将**解析**和**代码生成+查询**拆分为不同的工具，在初次问询时首先调用解析，根据解析结果判断是否继续。

![descript](media/image15.png){width="1.9037379702537183in"
height="1.75in"}常见近义词-\>继续流程

![descript](media/image16.png){width="1.9478379265091863in"
height="1.425903324584427in"}query解析，第二轮对话则开始后续流程

**9月W1：**

**速度优化实验**：

方案1-**生成节点转直接生成**，读取 [文档+上文 -\> 代码]{.underline}
（*去掉COT推理，改4o模型*）

方案2-**Print+生成节点合二为一***（尝试4turbo和4o）*

方案3-**并行执行** *（4o模型）*

*时间测试样例：本月GMV和Revenue*

*代码测试样例：需求文档11条样例*

+---------------+---------+-----------+--------+-----------+----------------------------------+
| *5次运行平均* | Print   | Generator | Total  | 代码质量  | 备注                             |
+---------------+---------+-----------+--------+-----------+----------------------------------+
| current       | 2.6424  | 6.7624    | 9.7842 | gold -    | baseline                         |
|               |         |           |        | 11/11     |                                  |
+---------------+---------+-----------+--------+-----------+----------------------------------+
| 方案1         | 2.9072  | 2.9454    | 6.2446 | gold -    | +36%                             |
|               |         |           |        | 11/11     |                                  |
+---------------+---------+-----------+--------+-----------+----------------------------------+
| 方案2-4turbo  | 7.9292              | 8.2952 | gold -    | +15%，条件缺失也必须等到推理结束 |
|               |                     |        | 11/11     |                                  |
+---------------+---------------------+--------+-----------+----------------------------------+
| 方案2-4o      | 3.272               | 5.230  | gold -    | +46%                             |
|               |                     |        | 11/11     |                                  |
+---------------+---------------------+--------+-----------+----------------------------------+
| 方案3         | 4.2238              | 4.8630 | sliver -  | +49%                             |
|               |                     |        | 10/11     |                                  |
+---------------+---------------------+--------+-----------+----------------------------------+

**9月W2**

问题1：用户询问了不存在的字段，gpt生成时默认找了最贴近的字段，但在展示信息以及表头的中文描述使用了用户的prompt

- case1：*8月份MP商家哪一家的销量最高?其GMV有多少?以及其获得的平台补贴金额（无此字段）?
  -\> 平台优惠券平台承担金额（错误字段） + 平台补贴金额（错误表头）*

  - *解决方案：加入了强规则代码进行审查，逻辑为：从sql找到英文字段名-\>从schema文档找到中文描述-\>替换展示信息+替换sql的alias*

![descript](media/image17.png){width="3.0833333333333335in"
height="2.0256408573928257in"}![descript](media/image18.png){width="3.09375in"
height="1.7581485126859142in"}

**10月W2**

问题2："9月份，GMV最高的十个MP商家供应商是哪些?"
无法一次生成正确SQL的问题，尝试两种分解方案：

1.  逐步思考分解子问题+对应SQL -\>
    汇总摘要得到**单一SQL代码**。GPT能力不够，SQL无法正确生成

![descript](media/image19.png){width="2.6875in"
height="1.2706485126859142in"}

2.  逐次 \"NL -\> SQL -\> data\" ，直到解决父级问题

*[在修改prompt后，可以观察到Agent能够自主辨别复杂问题需要多次调用工具。但是每个子问题在调用时会出现一些错误]{.underline}*

*案例1：*![descript](media/image20.png){width="2.7604166666666665in"
height="0.8754877515310586in"}![descript](media/image21.png){width="2.6354166666666665in"
height="0.9347583114610674in"}

*案例2：*![descript](media/image22.png){width="1.7215726159230096in"
height="1.1507709973753282in"}![descript](media/image23.png){width="0.9291437007874016in"
height="1.1125273403324585in"}

可以考虑两种方案实现逐次解决的串行问题\
1. 单独设计新工具（workflow）

2\. 调整Agent的prompt，让它自行分解问题+多次调用工具

*方案2结果：*

![descript](media/image24.png){width="0.84375in"
height="1.0113976377952756in"}由于nl2sql工具内部的问题，导致结果有误：

![descript](media/image25.png){width="2.0444083552055994in"
height="0.6069335083114611in"}企业店被拆开当作筛选条件，解决（删除biz
ordr yn字段）

加输出指示：![descript](media/image26.png){width="1.3231878827646544in"
height="1.7206408573928258in"}没加指示：![descript](media/image27.png){width="1.15625in"
height="1.7162150043744533in"}*[可以观察到Agent的智能被影响]{.underline}*

**10/15：采用[方案2]{.underline}（agent\'s
prompt），并在nl2sql内部加入了一个[RAG]{.underline}，分词得到的[实体去枚举值表中检索]{.underline}返回结果，作为外部知识传递给gpt生成sql**

**图表测试**，依赖Dify message的渲染逻辑

![descript](media/image28.png){width="4.229166666666667in"
height="3.3696784776902886in"}

## 归因分析（旧）

### 整体流程如下：

1.  **解析用户问题**：替换近义词、~~返回歧义实体~~

![descript](media/image29.png){width="1.5399037620297462in"
height="1.5104166666666667in"}

2.  **生成**：SQL(需要查询的数据，包含本期、基期) +
    分析计算函数入参(各列名，时间范围)

![descript](media/image30.png){width="1.2256944444444444in"
height="1.8385422134733158in"}![descript](media/image31.png){width="1.3627548118985127in"
height="1.8451760717410324in"}

3.  **分析报告**：根据问题+贡献度表生成分析报告

![descript](media/image32.png){width="1.0211143919510062in"
height="1.4148272090988627in"}![descript](media/image33.png){width="1.7620286526684164in"
height="1.0909853455818024in"}

### 问题记录

1.  **query解析**。第一阶段的parse**\_**query工具逻辑为替换规则，导致如"gmv"替换为"GAAP毛利额(去税)"+v；"营销品"替换为"营销"+"分析主码"

![descript](media/image34.png){width="6.299305555555556in"
height="0.934248687664042in"}

解决：引入jieba分词，导入自定义词表，将近义词配置表中的[key]{.underline}、[synonym]{.underline}，以及枚举值表中常用[enums]{.underline}作为自定义词导入，让jieba不拆分。

2.  **数据查询。**SQL执行后会获取一张包含本期+基期的宽表，由于**同比环比的时间范围可自定义**，因此需要**动态解析**。

![descript](media/image35.png){width="3.71875in"
height="0.84375in"}![descript](media/image36.png){width="1.53125in"
height="1.6384798775153107in"}

![descript](media/image37.png){width="5.072916666666667in"
height="0.5435269028871391in"}本期数据为空

解决：迭代三版，核心要点：日期格式正确+一致、时间范围一致、本期表和基期表不为空

3.  **特殊指标计算**。"GAAP毛利率(去税)=sum(gaap)/sum(revenue)"，上一阶段查询可以正确在sql中计算，现阶段的生成中会将字段找全，但是没有计算。因此函数的入参可能出错。

![descript](media/image38.png){width="2.3906255468066493in"
height="1.7708333333333333in"}一阶段

![descript](media/image39.png){width="3.0416666666666665in"
height="1.3635050306211725in"}![descript](media/image40.png){width="2.9270833333333335in"
height="1.377807305336833in"}现状

可能的解决：全部使用英文，alias + 字段名

### 归因重构

SQL由LLM生成，结合生成的其他入参，进入到后端流程进行归因计算：

具体细分为三大场景，***指定分析维度***、***未指定分析维度***、***指定数据的维度范围***

后两种场景依赖多个视角，每个视角对应固定几个字段，并且需要进行维度下钻（纯脚本计算）

## 权限接入（改造dify源码）

**WebApp**（发布后的应用）在Dify后端（DB中的 end_users
表）中的定位，依据请求*/chat-messages*
接口的方式，定义为三种情况（三种urlPrefix）：

1.  **/console/api/xxx**：对应dify工作室中的**已经登录用户**

2.  **/api/xxx (type =
    \'service_api\')**：对应于**调用app-API的用户**，request_body中传入了**user**参数，后端会将其解析。

3.  **/api/xxx (type =
    \'browser\')**：通过访问公开URL**直接使用WebApp的用户**，[即便在发起message时传入了user，后端不会解析，随机生成**SessionID**作为**userid**]{.underline}

在打开对话界面时，前端检测客户端是否存在 user token
。没有token时向后端发起 [/passport]{.underline}
接口请求，此时后端会生成随机 [SessionID]{.underline}
作为当前用户ID，并将 JWT(user token) 返回给客户端

- 实现Auth的两种方案：

**外部-\>内部：**将webapp以Iframe的方式嵌入到外部系统，在url中加上requestParam传递到前端服务器（Nextjs框架，node服务器），然后在webapp前端的
*middleware.ts* 中解析并存放到cookie中

**前后端交互：**

- 方案1：使用自定义前端仓库代码，通过service_api的方式和后端进行交互，request_body加入user参数。考虑到后期更新维护问题，成为待选方案

- 方案2：直接修改dify本体源码，前后端都需要进行修改。

  a.  前端：

      i.  **外部-\>内部（set cookie操作，middleware.ts文件）**

> ![descript](media/image41.png){width="3.3333333333333335in"
> height="2.5491983814523183in"}

ii. 每次刷新页面，**需要清除上一次的用户历史（web/app/layout.tsx）：**

> *通过每次加载都清除上一用户的token，实现用户隔离*
>
> ![descript](media/image42.png){width="3.4583333333333335in"
> height="1.4803040244969379in"}

b.  后端：

    i.  **保存userid(api/controller/web/passport.py)**:
        在用户访问url时会调用此接口，为db中的**end_user**表创建一个新用户。此时接收前端请求携带的cookie，如果userName参数不存在，则使用随机SessionID

> ![descript](media/image43.png){width="2.8304833770778655in"
> height="2.8274136045494314in"}

ii. 访问页面时，查询当前用户的**历史会话数据：**

> **(api/services/conversation_service.py)**
>
> ![descript](media/image44.png){width="3.2789555993000876in"
> height="2.053066491688539in"}
>
> ![descript](media/image45.png){width="5.458333333333333in"
> height="1.2767760279965004in"}

**部署：**

- Build为docker image并启动

1.  修改/docker文件夹中的docker-compose.yaml，文件找到service中的api、web，将image:
    xxxx参数改为本地build的image名称

2.  将api/web目录下的Dockerfile中加入必要的国内镜像源以确保成功安装依赖

ps:
公司网络环境无法成功下载依赖，需要外部方法，下载后在Dockerfile中使用COPY命令复制进容器，（还需要在dockerignore中去掉node_moudules）

注意：compose启动时可能会发生网络被占用的错误，需要使用docker network ls
& rm xxx，清理掉旧的network

![descript](media/image46.png){width="6.299305555555556in"
height="1.4072517497812773in"}

## 上线流程+服务重构

**11/25 \~ 11/29 待办事项**

整个项目分三个部分：

**Dify**、**Dify中的三个app**（虎鲸AI、NL2SQL、analysis）、**aibi_service**

***线下***

**：52-测试环境dify-改动过源码**

***线上 dify内app手动更新，service使用git更新***

**：15-预发环境-dify(改过) + service**

**：6-生产环境-dify(改过) + service**

- ~~划分环境：~~

<!-- -->

- ~~53-开发环境：dify-80端口、aibi_service-4400端口~~

<!-- -->

- ~~52-测试环境：dify-3334端口、aibi_service-4400端口~~

<!-- -->

- ~~生产环境需要新的访问域名（外网访问）~~

<!-- -->

- ~~v100-15-预发：dify-4410端口、aibi_service-4400端口~~

<!-- -->

- ~~v100-6-生产：dify-4410端口、aibi_service-4400端口~~

<!-- -->

- ~~服务重构：aibi_service从dify_service中单独拆除，并创建git远程仓库。git仓库需要包含以下两项：~~

<!-- -->

- ~~1. aibi_service代码~~

<!-- -->

- ~~2. dify-app的DSL文件自动化导出+备份~~

<!-- -->

- ~~上周问题修复 + 工作流更新~~

<!-- -->

- ~~问题修复：校正字段描述、歧义词返回、字段使用错误、归因分析场景1~~

<!-- -->

- ~~文档节点转HTTP节点~~

<!-- -->

- ~~自定义工具转HTTP节点~~

<!-- -->

- ~~测试用例测试（TAPD）~~

<!-- -->

- ~~跟外部系统联调~~

<!-- -->

- ~~测试环境联调~~

<!-- -->

- ~~预发环境联调~~

<!-- -->

- ~~正式环境~~

<!-- -->

- ~~AIBI项目完整上线文档（checklist），详见本文档"上线/发版checklist"板块~~

# 虎鲸AI 2.0（2025-2月）

## RAG改造

**具体流程：**

1.  **Agent（虎鲸ai）接收用户query，进行以下操作：**

<!-- -->

1.  **改写query**

2.  **提取关键词**

3.  **意图分类（查指标/归因）**

4.  **调用parse_query_v2工具**

**Tool1------parser query v2：**

1.  返回值：选表结果，意图分类；

2.  如果返回\`need_clarification\`，则Agent根据\`clarification_options\`数据向用户确认业务域（选表）

3.  不需要澄清时，通过意图分类执行对应工作流

> **Tool2/3------指标查询/归因分析：**
>
> 入参\`query\`+\`keyword\`进行Schema检索；\`table_name\`进行指定表下的样本库检索。
>
> **指标查询**执行NL2SQL，返回查询结果；
>
> **归因分析**由LLM生成SQL+归因计算函数入参，返回归因报告；

**dify内app：**

虎鲸ai：

- 任务：

  - 功能意图分类（指标查询、归因分析）

  - 口语化Query改写

  - 整理工作流返回的数据，markdown格式输出

指标查询（原NL2SQL）：

- 入参：

  - Agent改写过的query

  - Agent提取的关键词

  - 表名

- 增加检索：Schema检索；样本检索

归因分析（原analysis）：

- 入参同指标查询一致

- 增加Schema检索

**dify外service：**

1.  **基于人工样本批量生成样本**

> ![descript](media/image47.png){width="6.065972222222222in"
> height="2.120865048118985in"}

2.  **parse_query_v2**：RAG检索跟query相近的top5条schema信息，辅助LLM选表

> ![descript](media/image48.png){width="3.1915135608048995in"
> height="1.5520833333333333in"}

3.  **schema_recall**：

> 方案为**规则召回 +
> 语义召回**，返回结果分为三类：**synonym**（预设的同义词）、**enums**（枚举值）、**table_field**（宽表的字段信息）

**规则召回：**

1.  近义词命中

2.  遍历入参\`keyword\`，搜索 enums + table_field

**模型召回：**

bge-reranker-v2-m3 模型直接将对应表的全 table_field
数据进行重排序，选取**top5**

最后**去重+合并**，将检索结果返回。

## 数据解读（DEPRECATED）

目标，参照OpenAI
DeepResearch功能，实现一个基于给定数据生成深度分析报告的功能

Reference：[AIBI-数据解读功能](https://doc.weixin.qq.com/doc/w3_AT0AdAbcAO8xiX7l1SARv6q7tQJrK?scode=AEQA-QfUAA00PrUJS4AT0AdAbcAO8&newEmptyDoc=1&templateId=7ahndxoxup8jjjp1sytudr3muw)

## 检索系统的优化

1.  RAG上线之初手搓了一套检索系统，实现逻辑为：[Agent分词 -\> SQL LIKE
    召回枚举值 +
    Reranker模型排序选TopK个字段]{.underline}。[虎鲸AI-检索系统](https://doc.weixin.qq.com/doc/w3_AT0AdAbcAO8PMaot70aQJ6F1ppG7X?scode=AEQA-QfUAA01dr1PSSAT0AdAbcAO8&newEmptyDoc=1&templateId=7ahndxoxup8jjjp1sytudr3muw)

2.  [text2sql-虎鲸版](https://doc.weixin.qq.com/doc/w3_AD8ARwY0AEwiFAxoqAhTxeVtN1SXq?scode=AEQA-QfUAA09rkZPzJAD8ARwY0AEw)，重构检索系统，使用
    **ES+向量模型排序+业务规则过滤**；

> 2025/6/12上线新功能：使用**Agent分词结果**作为ES的分词输入，通过每个语义词块进行召回。

**检索步骤的工作流程图**

![descript](media/image49.png){width="7.270833333333333in"
height="2.623746719160105in"}

**主流程**

![descript](media/image50.png){width="7.270833333333333in"
height="1.1529899387576552in"}

## Known-Issues

1.  user
    prompt中的实体值会对LLM生成SQL时有所干扰。比如来自检索的正确枚举值没有使用而使用了用户的输入

2.  样本检索会有所干扰，导致没有使用Schema检索返回的结果，而使用样本中的错误字段

**待选方案：**

1.  控制随机性

2.  增加思考预算（开启思考模式）

3.  样本检索设置为动态行为，以及深度精选放入库中的样本数据

## 样本检索系统

**将已验证的历史样本**（Query + Correct SQL + Optimized Schema）作为
Few-shot 上下文，辅助大模型生成准确的 SQL 语句。

遵循 **\"数据质量优于模型复杂度\"** + **两阶段检索（召回+精排）**
架构以平衡性能与效果。

系统分为**离线数据处理**（Preprocessing）和**在线实时检索**（Retrieval）两部分。

### 自动化离线处理流水线（暂未完成自动化）

将原始 CSV 业务数据转化为高质量的 Elasticsearch 索引。流程如下

1.  **数据清洗（data_processor.py）**

    a.  统一空值与异常字符

    b.  过滤测试数据、短查询、非"正确"反馈

    c.  关键词提取：优先用 ES 分词，缺失时调用 LLM

2.  **SQL 权限清理（sql_permission_cleaner.py）**

    a.  移除用户权限语句（如\"mchnt_sup_name in (\...)\"），保证 SQL
        通用性

    b.  混合策略：先正则处理，失败则用 LLM 重写

3.  **数据去重（deduplicator.py）**

    a.  基于 (Query + TableName) 哈希指纹去重

4.  **Schema 清洗（schema_cleaner.py）**

    a.  依据目标 SQL 精准保留相关字段与枚举

    b.  剔除无关 Schema，降低 Token 与噪音

5.  **索引入库（indexer.py）**

    a.  生成 Query Embedding（1024维，doubao-embedding）

    b.  写入 Elasticsearch（文本 + 向量字段）

### 在线检索流水线（暂未返回相应Schema）

负责响应实时用户请求，返回最相关的 Top-K 样本。流程如下

1.  **混合召回（retrieval_engine.py）**

    a.  BM25 文本检索 + 向量检索并行

    b.  支持按 source 字段隔离或全库检索

2.  **排序优化（ranking_optimizer.py）**

    a.  对 Top-N 结果轻量精排（低延迟）

    b.  因子：关键词重叠、精确匹配奖励、时效性衰减、用户活跃度微调

3.  **Schema 聚合（schema_linking.py）（暂未完善）**

    a.  合并 Top-K 样本的 Schema

    b.  枚举值合并、字段描述择优，显著降低 Token 消耗
