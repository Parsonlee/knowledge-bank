---
type: source
tags:
- AI-Agent
summary: 从系统工程视角剖析 Agent 开发的三层复杂度（可运行/可复现/可进化），批判框架封装幻觉，提出系统化是唯一解
sources:
- raw/Agent系统开发经验.md
created: '2026-06-29'
updated: '2026-07-01'
confidence: high
---
# Agent系统开发经验

## 来源信息

- 原文标题：让Agent系统更聪明之前，先让它能被信任
- 作者：周至，阿里云开发者
- URL：https://mp.weixin.qq.com/s?__biz=MzIzOTU0NTQ0MA==&mid=2247554817

## 核心要点

### 三种"简单"幻觉

1. **被封装的复杂性**：框架（LangChain 等）帮你拼 prompt、裁剪 context，但调试/trace/状态恢复仍无人替你承担
2. **被外包的复杂性**：Memory/RAG/Embedding 交由平台托管，代价是失去干预与解释能力
3. **被推迟的复杂性**：运行时重新显现——输出漂移、无法复现、正确性塌陷

### Agent 三层复杂度

- **可运行性**：主流框架普遍解决良好（开发门槛低）✅
- **可复现性**：仅局部支持，需自建状态与观测层 ⚙️
- **可进化性**：仍靠人工与系统设计 ❌

### LLM 不确定性放大效应

假设单次 LLM 交互正确率 90%：
- 10 次交互 → 系统正确率 **35%**
- 20 次交互 → 系统正确率 **12%**

三类放大维度：
- **Memory 不确定性放大**：依赖 LLM 解析/embedding/检索，本质是语义一致性问题
- **编排动态性放大**：LLM 动态决定工具调用，决策空间爆炸
- **测试不可预测性放大**：输出是概率分布，需回放/对比基线/模拟环境测试

### Agent 开发四个阶段

1. **Hello World 阶段**：框架几行代码跑起来，改改 prompt 就行
2. **场景适配阶段**：遇到 context 管理、RAG 质量等坑
3. **系统化阶段**：复杂性爆炸——跨会话一致性、多 Agent 协同、tracing
4. **工程落地阶段**：安全合规、监控 SLO、故障恢复

### Agent 认知演化五层级

- **Level 0 框架幻觉层**：装框架跑 demo
- **Level 1 场景拼接层**：RAG+工具原型，prompt hack 解决问题
- **Level 2 系统设计层**：把 Agent 当微服务，可观测/状态管理
- **Level 3 工程落地层**：SRE/安全/分布式系统工程学科视角
- **Level 4 智能演化层**：长期记忆、自主学习、知识图谱编排（前沿）

### 系统化核心原则

- **先稳定，后聪明；先可观测，后优化**
- 建立状态与日志的可回放机制
- 对 Prompt/Memory/RAG 做版本追踪
- 引入观测指标（成功率、漂移率、冗余调用）
- 明确每个 Agent 的边界与权限范围

### 六种 Agent 设计模式

- **ReAct Pattern**：推理与行动解耦，问答/多步任务
- **CodeAct Pattern**：生成并执行代码+反馈循环
- **Tool Use Pattern**：MCP 统一协议管理工具
- **Self-Reflection Pattern**：Critique LLM 批评主模型输出
- **Multi-Agent Workflow**：Core Agent + Sub-Agents + Aggregator
- **Agentic RAG Pattern**：动态化检索+推理，自主决定何时检索

## 关键引文

> 智能的不确定性必须以工程的确定性为支撑。稳定与可观测，是 Agent 真正可演化的前提。 [重点]

> 框架/平台让 Agent「好搭」但没有让它「好用」，真正的复杂性，从未被消除，只是被推迟。 [高亮]

> Demo Agent 确实能解决问题，但只能解决今天的问题，系统化 Agent 才能解决明天和后天的问题。 [重点]

## 关联

- [[概念_Agent开发范式三级进化]]
- [[概念_Agent系统化工程]]
- [[概念_LLM不确定性放大]]
- [[实体_LangChain]]
- [[实体_LangSmith]]

---
> 📎 **物理文献**：[[raw/Agent系统开发经验.md]]
