---
type: source
tags:
- LLM/tokenization
- AI-Agent/context-engineering
summary: 对比传统 JSON 序列化在作为大语言模型上下文输入时的冗余开销，探讨轻量级替代标记格式对节省 Token 开销与提升解析速度的价值。
sources:
- raw/用 JSON喂LLM太费Token？试试这个新格式，号称最多省 40% ！.md
created: '2026-07-02'
updated: '2026-07-02'
confidence: high
---
# 替代JSON省Token的序列化新格式探索

## 来源信息
- 物理文件：[[raw/用 JSON喂LLM太费Token？试试这个新格式，号称最多省 40% ！.md]]
- 平台：微信公众号

## 核心要点
1. **JSON 的 Token 膨胀痛点**：大规模结构化数据（如多层嵌套对象与重复键名）在使用标准 JSON 格式送入大模型时，会消耗大量无意义的括号与引号 Token。
2. **轻量序列化格式对比**：使用 YAML、TOML 或精简分隔符等替代序列化方案，能够在保持语义清晰度的前提下大幅降低提示词长度。
3. **成本与性能提升**：在长上下文工程中，优化数据输入表达格式最高可缩减约 40% 的 Token 占用，同时提升模型的注意力聚焦能力。

## 关联概念与实体
- [[概念_结构化输出]]
- [[概念_表格序列化]]

---
> 📎 **物理文献**：[[raw/用 JSON喂LLM太费Token？试试这个新格式，号称最多省 40% ！.md]]
