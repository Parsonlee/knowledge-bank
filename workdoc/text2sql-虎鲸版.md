# text2sql 模型优化

模型原始数据位置：/data/yangzihao/xinference/modelscope/hub/deepseek-ai

训练数据存储位置：/data/guqian/大模型/text2sql_hujing/data

  ---------------------------- --------------------------------------- -------------- --------------
  模型                         数据                                    训练集准确率   测试集准确率

  Qwen2.5-Coder-14B-Instruct   生成样本已人工校验_trainingdata.jsonl                  
  ---------------------------- --------------------------------------- -------------- --------------

第一版使用表所有信息，文本内容太长，机器显存不够，现改成只使用相关字段

训练过程：

第一版：使用原始的200条打标数据，prompt使用原版，跑一次耗时12s上下,内存占用29G左右

第二版：使用原始的200条打标数据，prompt将Constraint删除，跑一次耗时13s上下，时间没有减慢

第三版：将第一版的模型直接**量化**，通过stop=\[\"\<\|endoftext\|\>\"\]
以及prompt限制输出个数为1，最终跑一次耗时为3s左右，内存占用48G左右

效果评估

#todo

### 附录

**Qwen2.5-Coder Technical Report**

<https://arxiv.org/pdf/2409.12186>

![descript](media/image1.png){width="9.958333333333334in"
height="3.15625in"}![descript](media/image2.png){width="8.3125in"
height="4.114583333333333in"}

数据构建

1,

微调方案：

lora vs qlora

避坑指南：

1.  demo使用和模型本地使用效果差距较大

安装vllm 加速

1.  环境 \--vllm
    需要在cuda12.1，需要现在虚拟环境下安装cuda12.1,步骤如下：

> 先下载cuda 12.1的runfile 安装包

安装cuda 到自定义路径

在虚拟环境下设置环境变量

最后检查一下

2.  安装包

模型量化

安装

# 关键词召回优化

原始版本

近义词召回：query -\>规则
-\>近义词表（aibi_synonym_key_list.synonym）\--精确匹配

枚举值召回：keywords -\>规则 -\>枚举值表（aibi_enums_list.enums）

字段召回：keywords -\>规则
-\>字段；query-\>模型（bge-reranker-v2-m3）-\>字段，多路召回，最后去重返回结果

aibi_table_field_information(字段:field_name,description)

问题：1.关键词没有分词导致枚举值没有内容

方案：用es代替规则召回

优化版本

将近义词表，枚举值表和字段表存入es 中，

根据以下规则进行返回

![descript](media/image3.png){width="5.979166666666667in"
height="5.241421697287839in"}

效果说明：

对于陈述不完整的枚举值可以召回，防止出现幻觉

后续增加过滤逻辑，详见代码readme.md

安装es 8.12.2

1.安装JDK 17

2.  设置环境变量

#### **全局配置**

添加以下行：

生效配置：

3.  下载es

<!-- -->

3.  创建用户，可用该用户进行系统开启

#### **配置 Elasticsearch**

编辑 /usr/share/elasticsearch/config/elasticsearch.yml：

####  **创建数据和日志目录**

#### **配置 Systemd 服务**

创建文件 /etc/systemd/system/elasticsearch.service：

写入以下内容，注意ES_HONE 需要调整

####  **设置文件权限**

设置用户名和密码

lasticsearch 8.x 默认启用安全认证，若密码错误或未初始化，需重置密码：

#### **重新加载 systemd 配置**

启动服务：

#### **验证服务状态**

错误可定位日志查看具体错误原因：

若验证成功，可进入python客户端

确保安装最新版本的库（兼容 Elasticsearch 8.x）：

###  **2. 基础认证代码示例**

使用 **用户名密码** 和 **CA 证书** 建立安全连接：

本项目中，用户名密码和证书位置如下所示：

安装plugins

<https://github.com/infinilabs/analysis-ik/releases>

然后重启即可

测试

创建一个临时索引并测试 ik_max_word

注意：

1.  保证安装的es版本和python客户端安装的版本一致，这样才可以调用

2.  一定要设置用户名和密码！！！

创建索引

#### 创建词库

近义词召回：query -\>规则
-\>近义词表（aibi_synonym_key_list.synonym）\--精确匹配

枚举值召回：keywords -\>规则 -\>枚举值表（aibi_enums_list.enums）

字段召回：keywords -\>规则
-\>字段；query-\>模型（bge-reranker-v2-m3）-\>字段，多路召回，最后去重返回结果

aibi_table_field_information(字段:field_name,description)

将近义词表（aibi_synonym_key_list）的synonym

枚举值（aibi_enums_list.enums）的ambiguous_term和enums

aibi_table_field_information(字段:field_name,description)的所有内容放入词表中

![descript](media/image4.png){width="4.770833333333333in"
height="1.3645833333333333in"}

将这些词放到/data-new/elasticsearch-8.12.2/config/analysis-ik
并构建IKAnalyzer.cfg.xml

构建成功后需要检查格式

需要显示为![descript](media/image5.png){width="4.177083333333333in"
height="0.34375in"}

若有问题，查看日志

一般有如下日志说明成功了

![descript](media/image6.png){width="7.59375in"
height="2.2489545056867892in"}

常见错误：

1.  IKAnalyzer.cfg.xml 格式不对

2.  IKAnalyzer.cfg.xml 和 dic 不在指定目录中，目录可通过log确定

然后重启即可生效

RAG 优化

目标：对于语义相关的指标不能通过es规则或者简单的向量模型获得

主要例子如下：最大订单金额-\>gmv

方案：找到指标并进行扩写，和库中扩写完的指标进行文本匹配

模型测评：

  ----------------------------------------- ------------------------ -------------------
  模型名称                                  效果                     测评数据

  ~~shibing624/text2vec-base-chinese~~      ~~结果不对~~             

  google/embeddinggemma-300m                45%                      近义词表数据

  intfloat/multilingual-e5-large-instruct   保留前两位47%；\         近义词表数据
                                            保留90%以上或前两个70%   
  ----------------------------------------- ------------------------ -------------------

匹配不上的原因

1：通过大模型找指标，会出现漏召的情况

eg

昨天,销量,销售额,毛利额,前10名-\>一个也找不到

2.对于特殊含义句子理解不了意思

eg

query:药城采购商"江西药业公司"的总购买金额是多少？

模型扩写结果：

{\'总购买金额\':
\'在一定时期内，采购商从药业公司购买商品所支付的全部金额总和。\'}

匹配上

\[{\'description\': \'采购商名称\', \'field_name\': \'user_name\',
\'formula\': \'\', \'描述文本\':
\'从事商品采购业务的企业或个人的全称。\'}, {\'description\':
\'购物金支付金额\', \'field_name\': \'recharge_amount\', \'formula\':
\'sum(recharge_amount)\', \'描述文本\':
\'用户通过购物金形式实际支付的总金额。\'}, {\'description\': \'单均价\',
\'field_name\': \'\', \'formula\': \'sum(gmv)/count(distinct ordr_id)\',
\'描述文本\': \'在一定时期内，某商品的总销售额与销售总量的比值。\'}\]

匹配不上

\[{\'description\': \'GMV\', \'field_name\': \'gmv\', \'formula\':
\'sum(gmv)\', \'描述文本\':
\'一定时间内，通过指定渠道和品牌完成交易的商品总金额。\'}\]

虎鲸迁移

修改点

已做：

1.  向量化 从本地迁移到腾讯云

> model服务位置：172.29.24.47
>
> model文件路径：/data/services/models/jina-embeddings-v3
>
> 服务文件：/data/services/jina_embedding/server.py
>
> 服务开启命令：nohup uvicorn server:app \--host 0.0.0.0 \--port 7500 \>
> service.log 2\>&1 &
>
> 服务状态：已开启

待做：

1.ES的安装

注意：52的/data-new/elasticsearch-8.12.2/plugins/analysis-ik/config/myword
需要用作分词

2.生产环境服务代码

> 待修改代码：\
> [vectorizer.py](https://vectorizer.py)
>
> 源代码：
>
> 修改：
>
> 每日拉取任务：

1.  每日拉取任务中的模型调用需要换成上述的接口；

2.  每日拉取任务代码在es_insert_daily/https://esdata_daily.py

> 每日任务调度：
>
> 0 5 \* \* \* /data-new/yolo/bin/python
> /data-new/guqian/text2sql_hujing/Code_retrieve_clone/es_insert_daily/esdata_daily.py
> \>\>
> /data-new/guqian/text2sql_hujing/Code_retrieve_clone/es_insert_daily/esdata_daily.log
> 2\>&1
>
> 3.第一次全量拉数据的代码可以参考es_insert_daily/https://esdata_daily.py
> 只需要
>
> ![descript](media/image7.png){width="10.391666666666667in"
> height="1.4098304899387577in"}

把这个条件去掉即可
