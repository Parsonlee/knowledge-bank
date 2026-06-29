---
type: source
tags:
  - LLM/arch
  - LLM/training
summary: "基于Karpathy 7小时LLM教学视频的学习笔记：聊天流程→预训练→后训练（SFT/奖励建模）→RL（GRPO/CoT/Aha moment）→主流应用特性"
sources:
  - "Cubox/Andrej Karpathy LLM教学-2025-05-19.md"
created: "2026-06-29"
updated: "2026-06-29"
confidence: high
---

# Andrej Karpathy LLM教学（学习笔记）

## 来源信息

- **标题**：LLM学习笔记：最好的学习方法是带着问题去寻找答案（基于Karpathy教学视频）
- **来源平台**：微信公众号 腾讯技术工程（作者：huaxing）
- **URL**：https://mp.weixin.qq.com/s?__biz=MjM5ODYwMjI2MA==&mid=2649793418&idx=1&sn=42bdb5161cea0cb2df6fb40872ec295e

## 核心要点

### 1. LLM 聊天过程原理

- **流程**：大模型收到的是 内置上下文 + 系统服务Prompt + 用户输入信息，逐token预测输出
- **本质**：从输入tokens推测下一个token的出现概率，将高概率token追加到输入，循环直到满足结束条件
- LLM是"具有统计概率的知识记忆模糊的知识回顾系统"，也可简称**概率性复读机**

### 2. 预训练

#### 数据集处理流程
列举URL → 有害站点过滤 → 富文本提取 → 语言过滤 → Gopher过滤 → MinHash去重 → C4过滤 → 自定义过滤 → PII移除

典型数据集：FineWeb（15万亿token，44TB）

#### Tokenization（BPE算法）
- 目标：平衡词汇表大小与序列长度，不丢失语义
- BPE：合并高频共现字节对，压缩到最小映射表，重新编号token
- GPT-4 词汇表约100,277个；各模型差异大（LLaMA 32K → 多语言模型 250K）
- **副作用**：token越多越分散注意力；聊不同主题应单独开会话窗口

#### 模型架构
- 主流：Decoder-only Transformer（GPT系列），适合生成任务，单向注意力掩码
- GPT-3: 1750亿参数，96层，上下文2048 tokens，训练约94000步（批量3.2M tokens/步）

#### 训练执行
- 分布式并行：数据并行 × 模型并行（张量并行+流水线并行）
- 软件优化：混合精度（FP16/FP8）、激活检查点（显存减30-50%）、内核融合
- 硬件优化：FlashAttention、MoE稀疏计算
- 预训练产物：基础模型（Base Model）= 互联网词汇模拟器，还不能成为有用助手

### 3. 后训练

#### SFT（监督微调）
- 使用人工标注的高质量对话数据（问题-理想回答对）微调模型
- 早期：upwork/ScaleAI 收集，现在大量由LLM辅助甚至合成生成（如UltraChat）
- **关键发现**：逐步推导的回答（Models need tokens to think）比一步跳跃答案更好

#### 奖励建模（Reward Modeling）
- 收集人类对多个回答的排序数据，训练奖励模型预测人类偏好
- 数据格式：三元组（Prompt, winning_response, losing_response）
- 损失函数：Bradley-Terry模型的对比学习，L = -log(σ(r(q,w) - r(q,l)))

#### 模型常见问题
1. **幻觉**：长尾事实缺失时编造细节；解决：搜索增强、RAG
2. **长记忆**：上下文窗口限制、注意力稀释；解决：向量数据库外部存储、分层记忆
3. **数学计算**：心算大数结果不准；R1借助MoE数学专家神经网络推算
4. **工具调用**：模型本身不直接调用工具，由应用层处理
5. **Tokenization副作用**：分词边界影响某些计算任务

### 4. 强化学习（RL）

Karpathy 认为 RL 与 SFT/RLHF 有本质区别：
- **RLHF**：在不可验证领域对齐人类偏好，重复训练无收益
- **RL**：可自动验证（RLVR），可不断重复改进，是推理模型构建的必要，也是走向AGI的关键

#### DeepSeek-R1 训练方法（三条路线）
1. **纯RL（R1-Zero）**：从Base模型直接GRPO训练；自然涌现自我验证/反思/长CoT，但可读性差、语言混合
2. **R1（完整版）**：冷启动（少量示例SFT）→ 推理RL → 全场景对齐RL + SFT；AIME 2024 pass@1 达79.8%，MATH-500达97.3%
3. **蒸馏**：用R1生成的80万条数据直接微调小模型（1.5B-70B），无需额外RL

#### 思维链（CoT）
- 结构化中间推理过程（`<think>...</think><answer>...</answer>`）
- 作用：提升复杂任务准确性、增强可解释性、支持长上下文多步推导

#### Aha Moment（顿悟时刻）
- R1-Zero RL 训练中，模型自然涌现学会花更多时间思考
- 某中间版本学会以拟人口吻重新思考问题，Karpathy称之为"见证RL的力量与美妙"

### 5. 主流应用特性

- **文件上传**：解析 → 文本切块 → token化 + 用户Query → LLM输出
- **网络搜索**：用户输入总结 → 搜索引擎调用 → 结果解析 → Rerank排序 → Top-N作为参考上下文 → LLM回答

## 关联

### 概念
- [[概念_Transformer架构]] — Transformer 5步流程
- [[概念_大模型训练三阶段]] — Pre-train/SFT/RLHF训练流程
- [[概念_RLHF基于人类反馈的强化学习]] — RLHF/RLVR对齐原理
- [[概念_DeepSeek-R1训练管道]] — R1四阶段训练管道
- [[概念_GRPO强化学习]] — GRPO算法
- [[概念_推理模型顿悟时刻]] — Aha Moment现象
- [[概念_思维链CoT高级方法]] — CoT技术路线
- [[概念_KV_Cache]] — 推理缓存机制
- [[概念_Embedding与向量检索]] — 向量数据库用于长记忆问题

### 实体
- [[实体_DeepSeek-R1]] — RL训练代表模型
- [[实体_PyTorch]] — 模型实现框架
- [[实体_Unsloth]] — 高效微调框架（GRPO支持）

### 相关 Source
- [[Transformer大模型3D可视化_NanoGPT]] — bbycroft.net/llm 可视化（本文也引用同一网站）
- [[DeepSeek-R1工作原理]] — R1技术详解
- [[强化学习入门指南_RLHF到GRPO]] — RL完整入门路线
