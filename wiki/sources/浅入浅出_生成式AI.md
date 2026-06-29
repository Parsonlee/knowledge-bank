---
type: source
tags:
  - DeepLearning
summary: 基于李宏毅《生成式 AI 导论》的入门综述，从机器学习基础到 Transformer 架构、Prompt 工程、大模型三阶段训练和 Agent 构建的全面讲解。
sources:
  - "Cubox/浅入浅出生成式AI.md"
created: "2026-06-29"
updated: "2026-06-29"
confidence: high
---

# 浅入浅出——生成式 AI

> 来源：浅入浅出—生成式 AI（阿里云开发者/虚一）
> URL：https://mp.weixin.qq.com/s?__biz=MzIzOTU0NTQ0MA==&mid=2247549128
> tags: DeepLearning
> confidence: high

## 摘要

学习李宏毅《生成式 AI 导论》的笔记。从 AI 基础概念到 Transformer 架构、Prompt 工程、大模型三阶段训练、Agent 构建的入门综述。

## 主要内容

### 基本概念层次

- **人工智能**：目标，不是技术定义
- **机器学习**：机器自动从数据中找函数；模型 = 函数 f(x) = ax+b 的演变，参数上万个
- **深度学习**：多层非线性处理单元（深度神经网络），参数不是简单线性叠加而是多层交互
- **生成式 AI**：产生复杂有结构物件（文章/影像/语音），几乎不可穷举（100 字作文 = 10^300 种可能）
- 生成式用分类策略解决：文字接龙，一次只预测后一个字（乘法变加法）

### Transformer 架构（5 步）

1. **Tokenization**：文字转 token（最小处理单位），token list 提前设置
2. **Input Layer（Embedding）**：token 转向量（低维空间），通过训练获得参数存储在数据库中；还需位置信息
3. **Attention（理解上下文）**：
   - Attention Weight：token 间相关性得分
   - Attention Matrix：所有 token 两两计算
   - Causal Attention：只考虑左边 token
   - Multi-head Attention：多角度计算相关性，避免信息丢失
4. **Feed Forward（整合思考）**：非线性变换整合多维信息，Attention + Feed Forward = Transformer Block，实际多层堆叠
5. **Output Layer**：线性变换映射到词汇表大小 → Softmax 归一化为概率分布 → 每次接龙结果不同（概率采样）

### Prompt 工程

- 神奇咒语（CoT、step by step）在旧模型有效，新模型自带深度思考后效果不大
- **真正有效的方法**：补充前提（专有知识）、提供模型不知道的新信息、提供范例（In-context learning）
- 拆解任务（当好师兄，细粒度模块化）
- 自我反省（产生答案难，检查答案易）
- Self-Consistency（多次回答取最一致）
- 组合方案：Tree of Thoughts（ToT）、Graph of Thoughts（GoT）
- RAG：搜索增强生成，弥补知识截止与幻觉问题

### 模型合作

- **路由**：路由模型分发任务给不同专有模型
- **多模型讨论**：多模型讨论 > 单模型自我反省；模型越多/讨论越多准确率越高；需裁判确定结束
- **角色扮演**：给模型指定角色代入

### 大模型训练三阶段

1. **Pre-train（自监督学习）**：
   - 语言知识 1 亿词汇够，世界知识 300 亿词汇不够
   - 数据处理：过滤有害内容、去 HTML tag（保留 emoji）、品质分类器去低品质、去重、测试集过滤
   - 影响因素：参数量（先天）+ 数据量（后天）；GPT-1: 117M/7000本书 → GPT-3: 175B/580G
2. **Instruction Fine-tuning（监督学习）**：
   - 人工标注数据做指令微调/"对齐"
   - Adapter：在原有参数上叠加少量参数，不直接修改
   - 举一反三 + 语言扩展（只需学一种语言的任务）
   - "Quality Is All You Need" / "Less Is More for Alignment"
3. **RLHF（强化学习）**：
   - 人工比较结果好坏（易），只看结果不看过程
   - 与围棋类似：每步分类问题，整体生成式问题
   - Reward Model 做评分员；RLAIF（用语言模型做反馈）

### Agent

- 期待 AI 像专业人士解决系列问题完成目标
- 关键：拥有记忆（模型训练后不再迭代，输入输出有限 → 额外处理记忆）
- 案例：斯坦福+Google 虚拟村庄项目

## 相关概念

- [[概念_Transformer架构]]
- [[概念_大模型训练三阶段]]
- [[概念_Prompt工程方法]]

## 相关实体

- （无独立实体需创建）
