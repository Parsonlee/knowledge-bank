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

**当前 wiki 规模**：63 source + 155 concept + 43 entity，0 failures

## 关键配置（速查）

- MCP 端点：`http://127.0.0.1:27123/mcp/`，token 在 `.mcp.json`（gitignore）
- Git user：`Hugo Yang <hugoyang1229@gmail.com>`
- Remote：`https://github.com/Parsonlee/knowledge-bank.git`
- 全文导出目录：`tmp/Cubox-批量导出文章-所有收藏-205 收藏-全文/`（205篇，gitignore）
- ingest 策略文档：`wiki/ingest-strategy.md`
- wiki 规则：`TheSchema.md`

## Next Steps

### ⚠️ 开始前必做

**检查/充值外部 API 中转服务余额**（昨天两次因 $0.27 余额不足中断，`need $0.89/次`）。

### 1. Phase 3：LLM 集群（~66篇，约 13 批）

LLM 集群是最大的，按子 tag 分组：

| 子批次 | 内容 | 篇数 |
|------|------|------|
| LLM/arch | Mamba系列、MoE、VLM、Transformer可视化等 | ~15 |
| LLM/training | SFT/RL/RLHF/后训练/DeepSeek-R1 等 | ~17 |
| LLM/inference | KV Cache、推测解码、显存优化等 | ~3 |
| LLM/reasoning | CoT、R1系列、思维链 | ~5 |
| LLM 综述/其他 | 综述、面试题、Scaling Law 等 | ~26 |

**操作方式**：每批 5 篇一个 subagent（opus），串行执行，每个子 tag 批次完成后直接在主对话验收（不用再派 agent）。

**ingest agent 指令模板**（关键规则）：
1. 先读 `wiki/index.md` 确认已有页面
2. 全文来源：`tmp/Cubox-批量导出文章-所有收藏-205 收藏-全文/xxx.md`
3. highlight 来源：`Cubox/xxx.md` 的 Annotations 部分
4. 只写全文真实内容，不用模型补全
5. source 页必须有标准 YAML frontmatter
6. 异常（全文空/乱码）→ 跳过并追加 `wiki/fail.md`
7. 已知 2 个空文件需跳过：`AI时代的快速研发小队分享.md`（50B）、另一个技术演进相关（50B）

### 2. Phase 4：AI-Agent 集群（~45篇，约 9 批）

完成 Phase 3 后继续。子 tag：coding / tools / context-engineering / deep-research / AI-BI / skill / multi-agent / memory / UI

### 3. Phase 5-6：Skill+AIGC + 其它（~54篇，约 11 批）

Skill（python/data-analysis/claude-code/linux）/ AIGC / 创业 / 面试 / Life / Recommendation / TTS

### 4. iOS 移动端同步（待机）

方案已定，等 wiki ingest 完成后再配：
- GitHub 生成 PAT（fine-grained，仅 knowledge-bank 读写权限）
- iOS Obsidian 装 Obsidian Git 插件，填入用户名 + PAT

## 验收原则（快查）

每个 Phase 完成后在主对话直接验收：
1. 死链检查：`grep -roh '\[\[[^]|]*' wiki/ | sed 's/\[\[//' | sort -u` vs 实际文件名
2. 抽查 3-5 个 source 页对比原文，确认无编造
3. 确认 `wiki/fail.md` 无漏记
4. 验收报告写入 `wiki/verify-phaseN.md` 并追加 `wiki/log.md`
