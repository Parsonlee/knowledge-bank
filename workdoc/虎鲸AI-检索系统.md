## 旧系统：

### 代码目录：

### 逻辑梳理：

\`schema_model.py\` -\> \`semantic_search.py\` -\>
\`schema_recall_system.py\`

### 总体概述

提供的代码实现了一个模式召回系统(Schema Recall
System)，主要用于根据查询和关键词从数据库中检索与表结构相关的信息。系统采用多路径召回策略，结合规则召回和语义召回两种方式，并对召回结果进行排序和去重。

### 系统核心组件

1\. 枚举类型定义

- FieldMatchType: 字段匹配类型，从高到低分为：

  - EXACT_DESCRIPTION(4): 描述完全匹配

  - EXACT_NAME(3): 字段名完全匹配

  - PREFIX(2): 前缀匹配

  - CONTAIN(1): 包含匹配

- EnumMatchType: 枚举值匹配类型，从高到低分为：

  - EXACT(3): 完全匹配

  - PREFIX(2): 前缀匹配

  - CONTAIN(1): 包含匹配

2\. 数据模型

- RankedFieldRecord:
  排序后的字段记录，包含记录内容、匹配类型、匹配长度和业务优先级

- RankedEnumRecord: 排序后的枚举记录，包含记录内容、匹配类型和匹配长度

- RecallSchemaInfo:
  召回的模式信息，包含同义词、枚举值、表字段和语义召回结果

- SchemaField:
  模式字段模型，包含字段名、描述、类型等数据库schema相关信息

3\. **主类 - SchemaRecallSystem**

核心功能类，负责实现召回逻辑，主要方法包括：

- \_\_init\_\_: 初始化系统，设置表名、topk值和执行器

- multipath_recall: **并行执行规则召回和语义召回**

- \_rule_based_recall: **基于规则的召回**

- \_semantic_recall: **基于语义的召回**

- \_process_synonyms: **处理同义词**

- \_recall_enums: **召回枚举值**

- \_recall_fields: **召回字段信息**

- \_rank_field_recalls: **对字段召回结果进行排序**

- \_rank_enum_recalls: **对枚举值召回结果进行排序**

- \_merge_and_deduplicate: **合并和去重结果**

### 工作流程分析

1\. 初始化

初始化时，系统接收表名、topk参数、线程执行器和语义搜索器：

- 根据配置将表名映射到内部名称

- 设置线程池执行器用于并行处理

- 初始化语义搜索器

- 设置字段业务优先级（目前只设置了\"gmv\"字段优先级为5）

2\. 多路径召回流程

当调用multipath_recall方法时:

1.  并行执行两种召回方式:

    i.  规则召回(\_rule_based_recall): 基于关键词和精确匹配规则的召回

    ii. 语义召回(\_semantic_recall): 使用语义搜索模型的召回

2.  合并两种召回结果并去重，构建完整的RecallSchemaInfo对象返回

3\. 规则召回详细流程

规则召回(\_rule_based_recall)按以下步骤执行:

1.  处理同义词: 查询同义词表并匹配查询中的同义词

2.  对每个关键词执行两种召回：

    i.  优先尝试枚举值召回:
        查找匹配关键词的枚举值，如有结果则按匹配类型和长度排序

    ii. 如果没有枚举值匹配，执行字段信息召回:
        查找字段名或描述匹配关键词的字段

4\. 语义召回详细流程

语义召回(\_semantic_recall)采用向量搜索:

1.  从数据库中获取表字段信息

2.  使用SemanticSearcher准备记录并对查询进行语义搜索

3.  返回语义相似度最高的结果

5\. 排序机制

系统采用两套排序机制:

1.  字段排序(\_rank_field_recalls):

    i.  首先按匹配类型排序: EXACT_DESCRIPTION \> EXACT_NAME \> PREFIX \>
        CONTAIN

    ii. 其次按业务优先级排序: 高优先级优先

    iii. 最后按文本长度排序: 较短的优先

2.  枚举值排序(\_rank_enum_recalls):

    i.  首先按匹配类型排序: EXACT \> PREFIX \> CONTAIN

    ii. 其次按匹配文本长度升序排序: 较短的优先

6\. 结果合并与去重

在_merge_and_deduplicate方法中:

- 使用(field_name, description)作为唯一标识

- 先处理规则召回结果(优先保留)

- 再处理语义召回结果(当无重复时添加)

- 更新schema_info对象中的table_field属性

![descript](media/image1.png){width="6.299305555555556in"
height="9.943731408573928in"}

## 可优化的点：

1.  **模型**。针对字段进行语义召回时直接使用了reranker模型，可以替换效果更好的，以及训练。

2.  **自动化评估**。开发了利用Trulens框架进行RAG流程评估的demo，工程开发待继续。

3.  **策略调整**。

    a.  索引。将待检索的分段进行策略调整，比如以字段描述\`description\`作为唯一索引进行语义召回。

    b.  字段召回排序。对热门字段添加权重（代码已实现，需添加更多规则）

4.  **结合论文重构**。参考[TableRAG](https://zhuanlan.zhihu.com/p/999771343)

## 新版本

加入ES系统检索 + dify内置知识库（向量检索Query-SQL样本）
