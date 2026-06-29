---
type: concept
tags:
  - AI-Agent
created: "2026-06-29"
updated: "2026-06-29"
---

# 概念：AI 应用架构演进

AI 应用架构遵循"功能叠加"的演进路线，从最简单的 LLM 调用逐步增加能力层。

## 七步演进路线

```
用户 → LLM                           ← 第一步：最简易架构
       ↓
       + 上下文增强（RAG）            ← 第二步：解决时效/领域知识缺失
       + 输入输出防护（Guardrails）   ← 第三步：安全与质量兜底
       + 意图路由                     ← 第四步：多功能分发
       + 模型网关                     ← 第五步：多模型抽象层
       + 缓存                         ← 第六步：降延迟降成本
       + Agent 模式                   ← 第七步：自主规划+写操作
```

## 各层关键技术

| 层次 | 技术点 |
|------|--------|
| 上下文增强 | query 改写/语义召回/重排/知识图谱 |
| 输入防护 | 隐私脱敏/Prompt Injection 防护/jailbreak 检测 |
| 输出防护 | 重试策略/AI Judge/关键词过滤/沙箱执行 |
| 意图路由 | 小参数路由模型 + few-shot + DPO |
| 模型网关 | 统一 API/访问控制/限流/负载均衡 |
| Prompt Cache | 精确/语义 key 匹配；System Prompt segment 缓存 |
| Agent 模式 | plan+tools+反馈迭代+写操作+安全确认 |

## 推理性能两大指标

- **TTFT**（Time to First Token）：首个 token 延迟
- **TPOT**（Time per Output Token）：平均 token 输出时间
- 单次 RT = TTFT + TPOT × 输出 token 数量

## Prefill/Decode 分离部署

大模型推理两阶段：
- **Prefill（预填充）**：上下文 embedding + 自注意力，**计算密集型**，可并行
- **Decode（解码）**：token-by-token 输出，**存储带宽密集型**，串行

分离部署可同时优化 TTFT 和 TPOT，DeepSeek V3 采用 32:320 的 prefill:decode 卡比。

## 关联

- [[聊聊AI应用架构演进]]
- [[概念_RAG基础流程]]
- [[概念_连续批处理]]
- [[概念_KV_Cache]]
- [[概念_上下文工程]]
