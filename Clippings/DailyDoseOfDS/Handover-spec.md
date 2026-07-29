# 📋 任务接手与标准执行文档（Handover Spec）

**文档名称**：`DailyDoseOfDS` 星标邮件自动化处理与 Obsidian 笔记同步接手规范

**目标**：将 `avi@dailydoseofds.com` 的所有星标邮件完整转换为高质量中文 Obsidian Markdown 笔记，上传至 Google Drive 目录，供 GitHub Action 自动部署同步至 Obsidian Vault。

---

## 1. 核心任务背景与资源信息

* **邮件源**：Gmail 星标邮件（查询条件：`from:avi@dailydoseofds.com is:starred`）
* **总邮件数**：76 封（已完成 15 封，剩余 61 封）
* **同步清单索引文件**：[sync_status.json](https://docs.google.com/document/d/1OjelnvBu87dGq0E4Xn8QXJV3B4XDJSRuUM0enbQaC-s/edit)（存储于 Google Drive `Obsidian_Clippings` 文件夹，ID: `1OjelnvBu87dGq0E4Xn8QXJV3B4XDJSRuUM0enbQaC-s`）
* **Google Drive 目标文件夹**：`Obsidian_Clippings`（ID: [1Iv4vMKj4gwZLiEml7fG3U22xQxi_woWX](https://www.google.com/search?q=https://drive.google.com/drive/folders/1Iv4vMKj4gwZLiEml7fG3U22xQxi_woWX)）
* **GitHub 仓库路径**：`Parsonlee/knowledge-bank` 下的 `Clippings/DailyDoseOfDS/`

---

## 2. 转换与生成标准（STRICT RULES）

1. **单邮件多文章拆分**：若一封 Newsletter 包含多篇独立主题/文章（通常包含 2~3 个核心主题），**必须拆分为独立的 `.md` 笔记文件**。
2. **全文高质量中文翻译**：保留完整的技术细节、代码块、数学公式与图表解释，禁止仅作简短摘要。
3. **文件名命名规范**：`YYYY-MM-DD-<English-Kebab-Case-Title>.md`（例如：`2026-06-25-The-AI-Engineering-Master-Stack.md`）。
4. **Frontmatter Schema 规范**：所有生成的笔记文件头部必须严格包含以下 YAML 字段：

```yaml
---
title: <中文标题>
source: https://mail.google.com/mail/u/0/#inbox/<GmailThreadID>
author:
  - "[[DailyDoseOfDS]]"
published: <邮件发送日期 YYYY-MM-DD>
created: <当前处理日期 YYYY-MM-DD>
description: <1-2句精炼中文摘要>
tags:
  - clippings
---

```

---

## 3. 标准处理流程（Step-by-Step Workflow）

接手的 Agent 可按照以下 5 个步骤分批循环执行：

### 步骤 1：读取进度清单

* 读取 [sync_status.json](https://docs.google.com/document/d/1OjelnvBu87dGq0E4Xn8QXJV3B4XDJSRuUM0enbQaC-s/edit)，筛选出 `status = 0` 的邮件时间戳项。

### 步骤 2：分批拉取邮件（推荐每批 4~6 封）

* 调用 `gmail:get_thread(threadId, messageFormat="FULL_CONTENT")` 批量获取邮件原始正文。

### 步骤 3：解析、拆分与中文翻译

* 解析邮件中的主题列表，将长正文按主题切分为独立 Markdown 文件。
* 翻译为符合中文技术阅读习惯的流畅文本，保留代码块与数学公式。
* 填入对应的 Frontmatter 元数据（使用邮件 Thread ID 拼接 `source` 链接）。

### 步骤 4：上传至 Google Drive 目标目录

1. 调用 `drive:create_file(title, text_content, mime_type="text/markdown")` 创建文件。
2. 调用 `drive:update_file(fileId, parentId="1Iv4vMKj4gwZLiEml7fG3U22xQxi_woWX")` 将新建的文件移入 `Obsidian_Clippings` 目录。

### 步骤 5：更新清单状态

* 完成转换后，将 `sync_status.json` 中对应时间戳的 `status` 字段由 `0` 修改为 `1` 并更新上传文件。

---

## 4. 转换样例示范（Example Reference）

```markdown
---
title: 2026 年 AI 工程全栈架构图（AI Engineering Master Stack）
source: https://mail.google.com/mail/u/0/#inbox/19f00c2716d4e27d
author:
  - "[[DailyDoseOfDS]]"
published: 2026-06-25
created: 2026-07-28
description: 全景梳理从基座模型、采样行为、Prompt、检索、Agent、Context 管理、微调、推理优化、评估到 LLMOps 的 10 层 AI 工程技术栈。
tags:
  - clippings
---

# 2026 年 AI 工程全栈架构图（AI Engineering Master Stack）

AI 工程（AI Engineering）已涵盖从底层 Token 表达至线上安全运维的 10 个核心技术层级：

1. **Foundations（模型基础）**：Tokenization、Embeddings、Transformer 架构、Attention 机制、Context Window、RoPE 位置编码及 MoE。
2. **Model Behavior（模型行为）**：Pretraining、Post-training、Sampling 采样、Temperature、Reasoning 模型与 Test-time Compute。
3. **Prompt Engineering（提示词工程）**：System Prompt、Few-shot、CoT、Structured Output、Prompt Caching 与 Self-consistency。
4. **Retrieval（检索强化）**：Chunking、Vector DB、Hybrid Search、Reranking、Query Rewriting 与 GraphRAG。
5. **Agents（智能体）**：Function Calling、ReAct、Planning、Reflection、Multi-agent 协作与 Human-in-the-loop。
6. **Context Engineering（上下文工程）**：Context Compaction、Memory、MCP 协议、Agent Harness 与 JIT 检索。
7. **Fine-tuning（微调对齐）**：SFT、LoRA/QLoRA、RLHF、DPO、Distillation 与 GRPO。
8. **Inference Optimization（推理优化）**：Quantization、KV Cache、Speculative Decoding、vLLM、FlashAttention 与 PagedAttention。
9. **Evaluation（评估体系）**：Benchmarks、LLM-as-a-judge、Golden Datasets、Hallucination Detection 与 Trajectory Eval。
10. **LLMOps & Safety（运维与安全）**：Observability、Cost Tracking、Guardrails、PII 保护与 Prompt Injection 防御。

```

---

## 5. 注意事项与避坑指南

1. **批次控制**：由于邮件正文与翻译量较大，单次处理建议控制在 4~6 封邮件以内，避免因 Token 超限或 RPC 超时导致中断。
2. **格式兼容**：通过 `drive:create_file` 上传的 Markdown 会自动转换为 Google Docs 格式，GitHub Action 已配置好文本导出 API（`export?format=txt`），可直接无缝解析。
