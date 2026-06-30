# HANDOFF — 个人知识库搭建

## Goal

基于 Obsidian 搭建个人知识库，实现跨平台多端访问（Mac/Win/iOS），并接入 Claude Code 通过 MCP 直接操作 vault。当前重心：将 Cubox 旧笔记批量 ingest 进 wiki 层，构建 LLM Wiki。

## 已完成事项（简览）

| 事项 | 状态 |
|------|------|
| Vault 初始化 + Git + GitHub 同步 | ✅ |
| 桌面端 Obsidian + 插件配置 | ✅ |
| Claude Code MCP 接入（HTTP 27123） | ✅ |
| Cubox tag 整理（53 个 tag） | ✅ |
| inbox/ 重复文章清理 | ✅ |
| LLM Wiki 三层架构搭建 | ✅ |
| Phase 1 ingest（Infra+CV+DL，21篇） | ✅ 验收 PASS |
| Phase 2 ingest（RAG，~43篇） | ✅ 验收 PASS |
| Phase 3 ingest（LLM，48篇，10批次） | ✅ 验收 PASS |
| Phase 4 ingest（AI-Agent，~43篇，9批次） | ✅ 验收 PASS |

| Phase 5 ingest（Skill，~19篇） | ✅ 验收 PASS |
| Phase 6 ingest（AIGC+创业+Life，~26篇） | ✅ 验收 PASS |

**当前 wiki 规模**：191 source + 331 concept + 137 entity，fail: 1篇

## 关键配置（速查）

- MCP 端点：`http://127.0.0.1:27123/mcp/`，token 在 `.mcp.json`（gitignore）
- Git user：`Hugo Yang <hugoyang1229@gmail.com>`
- Remote：`https://github.com/Parsonlee/knowledge-bank.git`
- 全文导出目录：`tmp/Cubox-批量导出文章-所有收藏-205 收藏-全文/`（205篇，gitignore）
- ingest 策略文档：`wiki/ingest-strategy.md`
- wiki 规则：`TheSchema.md`

## Next Steps

### 1. ✅ 全量 ingest 完成

205 篇 Cubox 全文已全部处理（191 成功 / 1 跳过-图片为主 / 其余已在前批处理）。
验收报告：`wiki/verify-phase1.md` / `verify-phase2.md` / `verify-phase4.md` / `verify-phase5_6.md`

### 2. iOS 移动端同步（待配置）

方案已定：
- GitHub 生成 PAT（fine-grained，仅 knowledge-bank 读写权限）
- iOS Obsidian 装 Obsidian Git 插件，填入用户名 + PAT

### 3. wiki 持续维护（长期）

- **75 个 forward-reference**：`概念_GRPO`、`实体_Claude` 等被引用但未建页，可按需补建
- **comparisons/ 和 overview/**：目前为空，可让 Claude 针对感兴趣主题生成对比分析页
- **新文章 ingest**：未来新收藏的 Cubox 文章，按 TheSchema.md 规则单篇 ingest

### 4. Obsidian Git 自动推送（如未配置）

设置面板里把 **Vault backup interval** 改为 `10` 分钟。

| 批次 | 内容 | 任务 |
|------|------|------|
| Batch 1 | Skill/claude-code 5篇（Claude Code完全指南/2.0.40更新/awesome-subagents/一个半月感受/写好CLAUDE.md） | #20 |
| Batch 2 | claude-code 1篇 + python 4篇（用Claude code重塑/FastAPI/async/uv/Python技巧） | #21 |
| Batch 3 | python + data-analysis 5篇（加速循环/EDA/Pandas美图/超强图解Pandas/一图胜千言） | #22 |
| Batch 4 | data-analysis + linux 4篇（matplotlib/数据可视化/Linux 600命令/现代打工人201KB） | #23 |

### 2. Phase 6：AIGC+TTS+Recommendation+创业+Life（21篇，5批）

| 批次 | 内容 | 任务 |
|------|------|------|
| Batch 5 | AIGC 5篇（Gemini PPT/Veo 3×2/AI PPT横测/小红书封面） | #24 |
| Batch 6 | AIGC+TTS+Recommendation 5篇（Nano-Banana×2/Wan2.2/TTS/RLMRec） | #25 |
| Batch 7 | 创业 5篇（Foundation Sprint/独立开发/100家AI初创/Superhuman/最小单元） | #26 |
| Batch 8 | 创业+Life 5篇（RIDE方法论/投资误区/Travel Tips/中枢与网关/驱蚊） | #27 |
| Batch 9 | Life 1篇（迪拜华人开车完全指南） | #28 |

### 3. iOS 移动端同步（待机）

方案已定，等 wiki ingest 完成后再配：
- GitHub 生成 PAT（fine-grained，仅 knowledge-bank 读写权限）
- iOS Obsidian 装 Obsidian Git 插件，填入用户名 + PAT

## 验收原则（快查）

每个 Phase 完成后在主对话直接验收：
1. 死链检查：`grep -roh '\[\[[^]|]*' wiki/ | sed 's/\[\[//' | sort -u` vs 实际文件名
2. 抽查 3-5 个 source 页对比原文，确认无编造
3. 确认 `wiki/fail.md` 无漏记
4. 验收报告写入 `wiki/verify-phaseN.md` 并追加 `wiki/log.md`
