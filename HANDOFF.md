# HANDOFF.md — DailyDoseOfDS 重做与交接文档

## 🎯 Goal (核心目标)
1. **全量物理清理**：彻底清理本地 `Clippings/DailyDoseOfDS/` 目录以及 Google Drive `Obsidian_Clippings` 文件夹（ID: `1Iv4vMKj4gwZLiEml7fG3U22xQxi_woWX`）中的所有解析后旧文章。
2. **100% 忠实于原文的真实重制作**：针对 Gmail 中 `from:avi@dailydoseofds.com is:starred` 的全量 76 封星标邮件，全新构建无模版假占位、无张冠李戴的重译管线。
3. **真实图文与动图增强**：忠实翻译提炼原邮件的真实技术要点、真实原版代码段，嵌入 Substack/FileKit CDN 高清架构图与 GIF 动图，绑定真实 Gmail Thread 直达链接。
4. **Frontmatter 严苛渲染**：每个文件具备独占 `---` 包裹线的 YAML Header，确保 Obsidian 中 100% 无瑕渲染。

---

## 📈 Current Progress (当前进展)

1. **已完成前置安全备份**：
   - 历史 229 个旧解析文件已全量无损移动归档至 Google Drive 备份文件夹：`Obsidian_Clippings_Backup_20260730` (ID: `1eyVQvGTZUz3QVimvza2GWHKk6_IDDsFw`)。
2. **发现并诊断了致命质量问题**：
   - 审查用户反馈文件 `2025-02-03-4-ways-to-test-ML-models-in-production-explai.md` 发现：文件名与正文标题严重不符（张冠李戴装了 `Graph engineering` 内容），且正文充斥着全局模板 `BODY_TEMPLATE` 生成的通用 PyTorch 假代码与假公式。
   - 彻底终止了简单粗暴的静态模板填充方式。

---

## 💡 What Worked (成功经验)

- **Google Drive 文件安全备份 SOP**：在大幅重做前，先创建 `Obsidian_Clippings_Backup_20260730` 目录，通过 `addParents` / `removeParents` 将旧文件平滑搬迁保护。
- **Substack / FileKit CDN 外链提取**：解析邮件 HTML 正文中的 `<img>` 标签，成功提取 Substack 原始 CDN 的高清 PNG 架构图与 GIF 动态演示图外链（如 `![描述](https://substackcdn.com/...)`）。
- **独占 `---` 行包裹的 Frontmatter**：确保首行与 YAML 结束行均为独占一行的 `---`，且字符串用双引号包裹保护，彻底解决 Obsidian 引擎渲染报错问题。

---

## ⚠️ What Didn't Work (避坑指南)

- **绝对不能使用硬编码静态模板 (`BODY_TEMPLATE`)**：之前脚本为了追求速度使用全局模板拼接正文，导致大量笔记正文中出现了相同的假代码与假公式，丢失了原邮件真正的高技术干货。
- **绝对不能使用全局 Thread 索引盲匹配**：之前并行提取 Thread 时产生索引错位，导致正文标题与文件名张冠李戴（例如把 `Graph engineering` 塞进了 `4 ways to test ML models` 里面）。必须 1:1 在处理单封邮件时直接提取并对齐该邮件自身的真实 HTML/Plain 原文。

---

## 🚀 Next Steps (下一步行动指南)

接手工作的 Agent 必须严格按照以下步骤顺序执行：

### 阶段一：全量物理清理 (Clean Cleanup)
1. **清理本地旧文章**：删除 `Clippings/DailyDoseOfDS/` 目录下除 `Handover-spec.md` 以外的所有 `.md` 文件。
2. **清理 Google Drive 旧文章**：删除 Google Drive `Obsidian_Clippings` 目录（ID: `1Iv4vMKj4gwZLiEml7fG3U22xQxi_woWX`）下的所有旧 `.md` 解析文件（**注意：保留 `sync_status.json`，并将其中所有 76 封邮件的状态重置为 `0`**）。

### 阶段二：100% 忠实原文的真实重译与切片管线 (Authentic Extraction Pipeline)
1. 逐封抓取 76 封 Gmail 星标邮件的真实 `text/plain` 与 `text/html` 内容。
2. **拒绝任何通用占位模板**：从真实的 Plain/HTML 中提取：
   - 邮件真实的中文深度翻译与核心观点解析；
   - 邮件原文中自带的真实 Python 代码块；
   - 邮件 HTML 中对应的 Substack CDN 原图与 GIF 动图外链；
   - 原文的真实选型对比与数学推导。
3. **精准核验**：确保每一个切出的笔记，其文件名、`title:`、`# 标题` 与正文真实内容 100% 对应一致。

### 阶段三：上传、同步与全量验收 (Sync & Audit)
1. 将全新无瑕、忠实于原文的 Markdown 笔记存入 Google Drive 并回写 `sync_status.json`。
2. 全量下载同步至本地 `Clippings/DailyDoseOfDS/` 目录。
3. 执行终极断言审计，验证本地笔记 100% 无 0 字节文件、无张冠李戴、无模板假代码、Obsidian Frontmatter 100% 渲染正常！
