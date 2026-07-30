# HANDOFF.md — DailyDoseOfDS 方案 C 执行交接文档

> 最后更新：2026-07-30T21:03 by Antigravity (Opus 4.6)

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
| **Batch 5-19** | ⏳ 待执行 | 剩余 61 封邮件 | — | — |

### 新增/新建文件（Batch 1-2 产出中与旧文件名不同的）

- `2026-07-24-11-LLM-evaluation-methods.md`（新切分）
- `2026-07-21-Layers-of-observability-in-AI-systems.md`（新切分）
- `2026-07-16-Knowledge-Distillation-using-Teacher-Assistant.md`（新切分）

### 待处理的 1 封无映射新邮件

- `19faa9c1ec5cf9ba`: **Serverless vs. On-prem vs. Edge Deployment**（2026-07-28）— 无旧文件，需完全新建

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
2. **广告/赞助商文件验收误报**：按 spec 生成的极简广告标记文件（<500 bytes）会被验收脚本标红，但这是**预期行为**，不是真正的问题。
3. **`sync_status.json` 是 Word 文档**：本地文件实际是 `.docx` 格式（由 Google Drive 同步导出），无法直接作为 JSON 解析。真正的 sync_status 数据在 Google Docs（ID: `1OjelnvBu87dGq0E4Xn8QXJV3B4XDJSRuUM0enbQaC-s`）。
4. **张冠李戴文件**：25 个旧文件的 `title:` 与文件名不匹配（如 `2025-02-03-4-ways-to-test-ML-models...` 实际内容是 Graph Engineering）。这些旧文件在覆盖重写后仍会以错误日期残留，需在全量完成后统一清理。

---

## 🚀 Next Steps (接手行动指南)

### 阶段一：继续串行执行 Batch 3-19

接手 Agent 按以下模式逐批执行：

```
循环 for batch_id in 3..19:
  1. 从 batch_plan.json 读取本批 4 封邮件的 ID、Subject、现有文件名
  2. 派发 ddods_translator Subagent (Flash 模型)，附带：
     - 邮件 ID 列表
     - CDN URL 修复提醒（去除 $s_!xxx!, 占位符）
     - 覆盖写入目录 /Users/ZHao/WorkSpace/knowledge-bank/Clippings/DailyDoseOfDS/
  3. Subagent 完成后，运行 verify_batch.py 验收
  4. 如有 CDN URL 残留，执行 sed 修复
  5. 确认通过后，派发下一批
```

**Subagent 定义已就绪**：`ddods_translator`（系统提示已包含完整翻译规范）。

### 阶段二：收尾清理

全部 19 批完成后：

1. **新建无映射邮件**：处理 `19faa9c1ec5cf9ba`（Serverless vs. On-prem vs. Edge Deployment）
2. **清理孤立旧文件**：删除日期前缀错误的旧张冠李戴文件（如 `2025-02-03-4-ways-to-test-ML-models-in-production-explai.md`）
3. **全量验收**：对全部 ~210 个文件运行 `verify_batch.py`（无参数=扫全量），确认 0 个模板标记残留
4. **Google Drive 同步**（可选）：更新 `sync_status.json` 并上传新文件至 `Obsidian_Clippings`

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
