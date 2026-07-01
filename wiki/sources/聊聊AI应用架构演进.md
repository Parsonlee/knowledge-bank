---
type: source
tags:
- AI-Agent
- 创业
summary: 以《AI Engineering》为蓝本，系统梳理 AI 应用架构的 7 步演进：基础调用→上下文增强→输入输出防护→意图路由→模型网关→缓存→Agent
  模式
sources:
- Cubox/聊聊AI应用架构演进-2025-06-17.md
created: '2026-06-29'
updated: '2026-07-01'
confidence: high
---
# 聊聊AI应用架构演进

## 来源信息

- 原文标题：聊聊AI应用架构演进
- 作者：江丹阳，阿里云开发者
- URL：https://mp.weixin.qq.com/s?__biz=MzIzOTU0NTQ0MA==&mid=2247550161

## 核心要点

### AI 应用架构七步演进路线

**第一步：最简易架构**
- 用户 → LLM → 用户
- 早期现象级应用（文本总结/AI 算命/AI 情感）
- 关键手段：Prompt Engineering（趋势：少即是多，LLM 自写 Prompt）

**第二步：增强上下文（RAG）**
- 解决模型局限：训练数据时效性 + 领域特有信息缺失
- 核心目标：针对 query 补充最相关/最必要的关联数据
- 技术点：query 改写、关键词匹配、语义召回、重排、文档切片、知识图谱

**第三步：输入输出防护（Guardrails）**

*输入防护：*
- 用户隐私防护：脱敏身份证/手机/银行卡/密钥等
- 恶意 Prompt 防护：四类攻击——Prompt Extraction / Jailbreaking / Prompt Injection / Information Extraction

*输出防护：*
- 质量防护：重试策略（串行/并行），AI Judge 评估
- 安全防护：关键词拦截、涉黄涉暴检测、沙箱执行

**第四步：意图路由**
- 多功能扩展后引入前置意图识别
- 路由模型参数量低，few-shot + DPO 轻量优化即可
- 作用：扩展性、功能隔离、安全防护（拒绝不支持的 prompt）

**第五步：模型网关**
- 抽象底层不同模型的调用，统一 API
- 非功能性能力：访问控制、计费、负载均衡、限流、重试、日志、可用性监测

**第六步：缓存**
- Prompt Cache：精确/语义两种 key 匹配；缓存 System Prompt + Few-shot segment
- RAG 缓存：热点知识 Index+Body 缓存，减少向量计算耗时
- Anthropic Prompt Caching 实测效果显著

**第七步：Agent 模式**
- Agent = 在特定环境下的 plan + tools
- 架构增加：模型输出分步执行 + 反馈迭代 + 写操作串联
- 写操作（发邮件/关闭订单/自动转账/指令执行）需额外安全确认

### 推理性能优化

**两个核心指标：**
- TTFT（Time to First Token）：首个 token 延迟
- TPOT（Time per Output Token）：平均每 token 输出时间
- 单次调用 RT = TTFT + TPOT × 输出 token 数量

**三种 Batching 方式：**
- 静态批处理：固定请求数触发
- 动态批处理：请求数 + 时间窗口双约束
- 连续批处理：多通道并行，请求完成即返回

**Prefill/Decode 分集群部署：**
- Prefill（预填充）：计算密集型，可并行
- Decode（解码）：存储带宽密集型，串行
- DeepSeek V3：prefill 32 张卡，decode 320 张卡；比例通常 1:2 到 1:4

### 监控三大核心指标（DevOps 社区）

- **MTTD**：发现问题所需时间
- **MTTR**：从发现到解决问题的时间
- **CFR**：变更引起 bugfix/回滚的比例

## 关键引文

> Agent 是在特定环境下的 plan+tools，特定环境限制的是 Agent 的创建是面向一定的场景和问题域的，plan 说明 Agent 有思考和规划能力，且有根据反馈做循环迭代的能力。 [重点]

> 个人认为 Prompt Engineering 起到的作用相比 LLM 出来时会越来越少……趋势是往少即是多，增量增加必要的描述上靠。 [高亮]

## 关联

- [[概念_上下文工程]]
- [[概念_Prompt驱动分割]]
- [[概念_RAG基础流程]]
- [[概念_KV_Cache]]
- [[概念_连续批处理]]
- [[概念_AI应用架构演进]]
- [[实体_LangChain]]
- [[实体_LangSmith]]
