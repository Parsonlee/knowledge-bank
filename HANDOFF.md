# HANDOFF.md — DailyDoseOfDS 方案 C 执行交接文档

> 最后确认：2026-07-30 by Codex

---

## 🎯 Goal (核心目标)

将 Gmail 中 `from:avi@dailydoseofds.com is:starred` 的 **77 封**星标邮件，全量转换为**100% 忠实于原文**的高质量中文 Obsidian Markdown 笔记，覆盖替换 `Clippings/DailyDoseOfDS/` 目录下旧模板生成的假内容文件。

---

## 📈 Current Progress (当前进展)

### 已完成的前置工程

1. **Gmail 星标邮件精确盘点**：确认实际为 **77 封**（非原来的 76 封），新增 1 封 `Serverless vs. On-prem vs. Edge Deployment`（2026-07-28，ID: `19faa9c1ec5cf9ba`）无对应旧文件。
2. **全量质量审计**：对 207 个旧文件执行定量扫描，确认 **100% 正文为模板假内容**（`HighPerformanceModule` 假代码 96%、统一开头语 100%、KL 散度假公式 94%），**0% 正文可复用**。
3. **邮件↔文件映射表构建**：
   - 映射文件：`<artifacts>/scratch/email_file_mapping.json`（76 封已映射，1 封新建）
   - 分批计划：`<artifacts>/scratch/batch_plan.json`（19 批，每批 4 封邮件）
4. **方案评估与选型**：对比全量重做(A) / 审计修复(B) / 混合重生(C) 三方案，选定**方案 C（元数据复用 + 正文全量重生）**。
5. **历史备份**：229 个旧文件已全量归档至 Google Drive `Obsidian_Clippings_Backup_20260730`（ID: `1eyVQvGTZUz3QVimvza2GWHKk6_IDDsFw`）。

### 批次执行进度

| 批次 | 状态 | 邮件主题 | 产出文件数 | 验收 |
|------|------|------|------|------|
| **Batch 1** | ✅ 完成 | Graph Engineering / 11 LLM Eval / 5 Quantization / RLHF-DPO-GRPO | 12 | ✅ 11 通过 + 1 广告标记 |
| **Batch 2** | ✅ 完成 | Agents Web Search / Small Models / Four Agent Loops / KV Caching | 11 | ✅ 9 通过 + 2 广告标记 |
| **Batch 3** | ✅ 完成 | Prompt/Context/Loop Eng / AI Master Stack / Loop Eng / Turn Website API | 12 | ✅ 9 通过 + 3 广告标记 |
| **Batch 4** | ✅ 完成 | PPO in RL / 8 Layer Production AI / Agent Harness Repair / 3D Weather Globe | 11 | ✅ 10 通过 + 1 广告标记 |
| **Batch 5** | ✅ 完成 | Hermes Agent / Deep Researcher / Bellman Eqs / Local AI Brain | 11 | ✅ 9 通过 + 2 广告标记 |
| **Batch 6** | ✅ 完成 | Train Classical ML / MDP in RL / Beat GRPO / RL Agents 2026 | 8 | ✅ 8 通过 |
| **Batch 7** | ✅ 完成 | Agent Memory Trick / LLM Opt Techniques / Claude Code Slash / Diffusion LLMs | 11 | ✅ 11 通过 |
| **Batch 8** | ✅ 完成 | Agent Harness / GPU vs TPU / AI OS / .claude Folder | 10 | ✅ 7 通过 + 3 广告标记 |
| **Batch 9** | ✅ 完成 | LLM Inference / Fine-tuning / ML Sets / NN Train Opt | 10 | ✅ 10 通过 |
| **Batch 10** | ✅ 完成 | Error Monitoring Agent / Object Detection / Parallel Processing / ML Phases | 13 | ✅ 12 通过 + 1 广告标记 |
| **Batch 11** | ✅ 完成 | Generative UI / Test Agents / Trace App / BM25 Algorithm | 13 | ✅ 12 通过 + 1 广告标记 |
| **Batch 12** | ✅ 完成 | ML 6 Steps / RAG & Fine-tuning / LLM on Phone / 8 AI Architectures | 13 | ✅ 9 通过 + 4 广告标记 |
| **Batch 13** | ✅ 完成 | Categorical Encoding / kNN Imbalanced / MiniMax vs Sonnet / Verbalized Sampling | 13 | ✅ 10 通过 + 3 广告标记 |
| **Batch 14** | ✅ 完成 | Federated Data Engine / Anthropic MCP / Gradient Boosting / PCA | 10 | ✅ 10 通过 |
| **Batch 15** | ✅ 完成 | 6 Types of Contexts / GIL in Python / Context Engineering / Clustering Evaluation | 12 | ✅ 12 通过；1 个历史映射异常已显式标注 |
| **Batch 16** | ✅ 完成 | Data & Pipeline Engineering / Corrective RAG / 4 Layers of Agentic AI / Qwen 3 Coder vs. Sonnet 4 | 12 | ✅ 12 通过；1 个历史映射异常已显式标注 |
| **Batch 17** | ✅ 完成 | MCP Integration / uv Guide / Component-level Evals / Neural-network Training Optimization | 11 | ✅ 11 通过 |
| **Batch 18** | ✅ 完成 | MCP Sampling / Bi-encoder & ColBERT / RAG Chunking / Memory Pinning | 13 | ✅ 13 通过 |
| **Batch 19** | ✅ 完成 | Variables / Active Learning / ML Production Testing / Python Underscore | 7 | ✅ 7 通过 |
| **收尾补充** | ✅ 完成 | Serverless / Edge Deployment 邮件 | 4 | ✅ 4 通过，新建 4 篇 |

### 本次现场确认

- Batch 15 已按「每个子代理最多两封邮件」的串行限制拆为两段处理，并完成主验收：`verify_batch.py` 对 12 个文件均返回通过；未发现 `$s_!` 图片 URL 残留。
- 历史映射存在一处异常：`2025-09-23-A-free-ML-course-that-requires-zero-technical.md` 并不在指定的 GIL 邮件中。页面已明确写为待回溯的映射异常，未填入无关主题内容。
- Batch 16 已完成主验收：`verify_batch.py` 对 12 个文件均返回通过；其中 `2025-07-25-11-most-important-DS-plots.md` 不在其映射邮件中，已改为可审计异常说明。Beam 与 Factory 推广页已明确标注为广告内容。
- Batch 17 已完成主验收：`verify_batch.py` 对 11 个文件均返回通过。Factory MCP 推广页已显式标注为广告；验收脚本必须接收绝对路径，传相对路径会误报文件不存在。
- Batch 18 已完成主验收：`verify_batch.py` 对 13 个文件均返回通过。计划中缺失主题和日期的 ID `196ac3a283f20357` 可正常读取，实际主题为「Memory Pinning to Accelerate Model Training」，因此无需创建映射异常说明；Linkup、Browserbase 与 Rovo Dev CLI 推广页已显式标注。
- Batch 19 已完成主验收：`verify_batch.py` 对 7 个文件均返回通过。曾中断的两篇旧模板文件已重新派发并通过验收；Maxim 页面被明确处理为同封邮件中的赞助主题，未混入邮件主文的无关内容。
- 收尾补充已完成：ID `19faa9c1ec5cf9ba` 被拆分为 4 篇新笔记（Technical LLM interview question、Serverless vs. On-prem vs. Edge Deployment、CPU vs. GPU vs. TPU vs. NPU vs. LPU、MCP & Skills for AI agents），逐篇验收均通过。
- **最终全量验收**：77 封目标星标邮件（19 个计划批次 + 1 封无映射新邮件）均已处理完毕。用户已授权删除 21 篇极短广告/推广页，并重写 2 篇历史模板残留文件；对现存全目录 198 篇文件运行 `verify_batch.py` 的结果为 **198 通过、0 失败**。
- Obsidian Git 已将 Batch 1–15 的工作树自动备份为提交 `8c11987`（`vault backup: 2026-07-30 23:18:04`）。本次更新 HANDOFF 后会产生新的未提交文档改动；不要使用会覆盖工作树的 Git 恢复或重置操作。
- **本任务与目录级验收均已完成**。

### 新增/新建文件（Batch 1-2 产出中与旧文件名不同的）

- `2026-07-24-11-LLM-evaluation-methods.md`（新切分）
- `2026-07-21-Layers-of-observability-in-AI-systems.md`（新切分）
- `2026-07-16-Knowledge-Distillation-using-Teacher-Assistant.md`（新切分）

### 已处理的无映射新邮件

- `19faa9c1ec5cf9ba`: **Serverless vs. On-prem vs. Edge Deployment**（2026-07-28）— 已拆分并新建 4 篇笔记。

---

## 💡 What Worked (成功经验)

1. **方案 C 混合策略**：复用文件名骨架 + 正文全量重生，效率高于全量重做和审计修复。
2. **`gws gmail +read --id <ID> --headers`**：纯文本模式高效获取邮件正文，HTML 模式补充提取 CDN 图片 URL。
3. **Flash 3.5 Subagent 串行调度**：每批 4 封邮件，Subagent 约 2-3 分钟完成，主 Agent 验收后再派下一批。
4. **验收脚本自动化**：`scratch/verify_batch.py` 自动检测模板标记残留、Frontmatter 完整性、文件大小异常。
5. **CDN URL 修复**：`sed -i '' 's/\$s_![^!]*!,//g'` 批量清理损坏占位符，或在 Subagent 指令中预防。

---

## ⚠️ What Didn't Work / 避坑指南

1. **CDN 图片 URL 损坏占位符 `$s_!xxx!,`**：Batch 1 的 Subagent 从旧文件复用了带损坏参数的 URL，需要主 Agent 用 sed 后置修复。Batch 2 起在 Subagent 指令中追加了预防说明，问题已解决。
2. **广告/赞助商文件过短**：极简广告标记页会因小于 500 bytes 被验收脚本判失败；本次按用户要求已删除此类 21 个页面，而非保留豁免。
3. **`sync_status.json` 是 Word 文档**：本地文件实际是 `.docx` 格式（由 Google Drive 同步导出），无法直接作为 JSON 解析。真正的 sync_status 数据在 Google Docs（ID: `1OjelnvBu87dGq0E4Xn8QXJV3B4XDJSRuUM0enbQaC-s`）。
4. **张冠李戴文件**：旧文件中曾存在标题与文件名不匹配问题；本次发现的两篇模板残留已按实际 Gmail 来源重写。

---

## 🚀 Next Steps (接手行动指南)

### 阶段一：本任务已完成

77 封目标星标邮件均已完成处理，现存目录已通过最终全量验收。

### 阶段二：收尾清理

已完成无映射邮件新建、广告页清理、模板残留重写与全量验收。Google Drive 同步如有需要，可作为独立任务执行。

---

## 📁 关键文件索引

| 文件 | 路径 | 用途 |
|------|------|------|
| 邮件元数据 | `<artifacts>/scratch/email_metadata.json` | 77 封邮件的 ID / Subject / Date |
| 邮件↔文件映射 | `<artifacts>/scratch/email_file_mapping.json` | 邮件到文件的精准映射 |
| 分批计划 | `<artifacts>/scratch/batch_plan.json` | 19 批次的详细任务清单 |
| 验收脚本 | `<artifacts>/scratch/verify_batch.py` | 批次验收自动化检查 |
| 审计脚本 | `<artifacts>/scratch/audit_files.py` | 全量文件质量诊断 |
| 方案对比 | `<artifacts>/plan_comparison.md` | 三方案评估文档 |
| Handover 规范 | `Clippings/DailyDoseOfDS/Handover-spec.md` | 原始翻译格式规范（保留参考） |

> `<artifacts>` = `/Users/ZHao/.gemini/antigravity-cli/brain/1a4ae592-f085-4deb-b656-ef8e1df2546e`

---

## 🔧 快速启动命令参考

```bash
# 读取邮件纯文本
gws gmail +read --id <EMAIL_ID> --headers

# 读取邮件 HTML（提取图片）
gws gmail +read --id <EMAIL_ID> --html

# 修复 CDN URL 损坏占位符
sed -i '' 's/\$s_![^!]*!,//g' <file.md>

# 验收特定文件
python3 <artifacts>/scratch/verify_batch.py file1.md file2.md ...

# 全量验收
python3 <artifacts>/scratch/verify_batch.py
```
