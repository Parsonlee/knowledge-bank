---
type: source
tags:
- Recommendation
summary: '**论文信息**：arxiv:2310.15950，代码 github.com/HKUDS/RLMRec，已落地公司搜索业务'
sources:
- raw/即插即用、简单有效的大语言模型推荐算法！港大联合百度推出RLMRec.md
created: '2026-06-29'
updated: '2026-07-01'
confidence: high
---
# RLMRec：港大百度 LLM 推荐算法

## 来源信息

- **标题**：即插即用、简单有效的大语言模型推荐算法！港大联合百度推出RLMRec
- **作者**：PaperWeekly
- **发布时间**：2024-02-07
- **URL**：https://mp.weixin.qq.com/s/syCREjY7YIg8LIsDzj6EPQ


港大联合百度提出 RLMRec，从互信息最大化的理论角度，引入 LLM 生成的文本语义信号优化推荐算法表征学习中的噪声，通过对比式/生成式两套对齐范式实现去噪增强。

## Key Points

- **论文信息**：arxiv:2310.15950，代码 github.com/HKUDS/RLMRec，已落地公司搜索业务

- **核心问题**：基于图神经网络的协同过滤（CF）从用户-物品交互图学习表征，但交互图含噪声（误点击、购买后不喜欢等），噪声被 BPR 损失嵌入表征，形成有噪表征学习

- **核心思路**（详见 [[概念_互信息最大化去噪表征]]）
  - CF-side Representation 含两种成分：有益于推荐的偏好成分 + 噪音成分
  - 引入另一模态（文本语义）特征，极大化两模态共存部分（交集），压缩噪音
  - 理论推导：该优化等同于**最大化两种模态特征表示的互信息**
  - 通过 InfoNCE 的互信息变分下界优化，引入 critic function 计算相似度

- **LLM 文本表征获取**（详见 [[概念_LLM用户商品画像生成]]）
  - 用户画像：体现喜欢什么类别商品；商品画像：体现吸引什么用户群体
  - 先商品后用户（Item-to-User）生成流程
  - 商品画像：用原始描述（Amazon-book）或属性标签+用户反馈（Yelp）构建 Prompts
  - 用户画像：基于购买商品+反馈构建 Prompts
  - 每个用户/商品独立生成，可并行；用思维链思想构建 Instruction 提质
  - 文本编码器：OpenAI text-embedding-ada-002（越优异编码器帮助越大）

- **两种对齐范式**
  - **RLMRec-Con（对比式对齐）**：MLP 降维文本表征至 CF 维度，余弦相似度+指数函数；双向对齐；抗噪能力最强
  - **RLMRec-Gen（生成式对齐）**：随机节点初始特征替换为 [MASK]，MLP 放大 CF 表征至文本维度；Mask-autoencoding 单向重构；预训练场景避免过拟合

- **模型无关框架**：可无缝嵌入任意以表征学习为基础的 CF 推荐算法

- **实验**
  - 数据集：Amazon-book、Yelp、Steam
  - 基线：GCCF/LightGCN/SGL/SimGCL/DCCF/AutoCF，均显著提升
  - 消融：更强文本编码器→更好性能；打乱文本表征顺序性能下降最明显
  - 噪声实验：RLMRec-Con 抗噪最强；预训练：RLMRec-Gen 泛化更好

## Related Concepts

- [[概念_互信息最大化去噪表征]]
- [[概念_LLM用户商品画像生成]]
- [[概念_大模型推荐系统]]

## Related Entities

- [[实体_RLMRec]]
- [[实体_港大数据智能实验室]]

## 来源

- 全文：`tmp/Cubox-批量导出文章-所有收藏-205 收藏-全文/即插即用、简单有效的大语言模型推荐算法！港大联合百度推出RLMRec.md`
- Cubox：`raw/即插即用、简单有效的大语言模型推荐算法！港大联合百度推出RLMRec.md`
