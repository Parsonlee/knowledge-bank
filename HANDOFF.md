# HANDOFF — 个人知识库搭建

## Goal

基于 Obsidian 搭建个人知识库，实现跨平台多端访问（Mac/Win/iOS），并接入 Claude Code 通过 MCP 直接操作 vault。

## Current Progress

### ✅ 已完成

1. **本地 vault + Git 初始化**
   - 目录结构：`inbox/`、`notes/`、`assets/`、`Cubox/`（旧笔记导入）、`Clippings/`
   - Git user：`Hugo Yang <hugoyang1229@gmail.com>`
   - Remote：`https://github.com/Parsonlee/knowledge-bank.git`（main 分支）

2. **GitHub 远端同步**
   - 已推送，仓库建议设为 Private

3. **桌面端 Obsidian 配置**
   - 已安装插件：`obsidian-git`、`calendar`、`dataview`、`obsidian-excalidraw-plugin`、`obsidian-outliner`、`obsidian-paste-image-rename`、`tag-wrangler`、`templater-obsidian`
   - `app.json` 设置：附件路径 `assets/`，始终更新内部链接 ✅
   - Obsidian Git 设置：autoPullOnBoot=true, autoPullInterval=10min, pullBeforePush=true, commitMessage=`vault backup: {{date}}`
   - ⚠️ **注意**：`autoSaveInterval` 仍为 `0`（=关闭自动提交推送），需改为 `10`（在 Obsidian Git 设置面板里把 "Vault backup interval (minutes)" 改成 10）

4. **MCP 接入 Claude Code**
   - 插件：Local REST API with MCP v4.1.3（coddingtonbear）
   - 端点：`http://127.0.0.1:27123/mcp/`（HTTP，非加密，仅本机回环）
   - Bearer Token：`0c249c6349cfa64111614bdcd30925deac360461007724e4371e7e00579d3876`
   - 配置范围：project（`.mcp.json`，已加入 `.gitignore`）
   - 状态：**已验证连通**，能读/写/搜索 vault

5. **Cubox 旧笔记分析**
   - 180+ 篇从 Cubox 导入的收藏文章
   - 67 个 tag，已完成全量分析
   - 已输出完整的 **Tag 合并操作清单**（见下方 Next Steps）

### 配置文件位置

- `.mcp.json`：MCP server 配置（含 token，已 gitignore）
- `.gitignore`：排除 `.obsidian/workspace.json`、`.claude/`、`.mcp.json` 等
- `notes/setup-config.md`：中文版 Obsidian 配置清单（已提交到仓库）

## What Worked

- Git + Obsidian Git 插件作为多端同步方案，桌面端全自动
- Local REST API 插件的 HTTP 端口（27123）接 Claude Code MCP，无需处理自签证书
- `claude mcp add --scope project --transport http` 命令一步到位

## What Didn't Work

- HTTPS（端口 27124）需要信任自签证书，Node 需要全局 `NODE_EXTRA_CA_CERTS` 环境变量，无法 scope 到单个 project MCP server，过于侵入 → 改走 HTTP 回环

## Next Steps

### 1. 修复自动推送（1 分钟）

在 Obsidian Git 设置面板里把 **Vault backup interval (minutes)** 从 `0` 改成 `10`。

### 2. 执行 Tag 合并清单（Tag Wrangler 操作）

在 Obsidian 右侧 Tags 面板，右键 → Rename tag，按以下顺序：

**Phase 1 — 消除重复**
| 操作 | 原 tag | → 目标 tag |
|---|---|---|
| 1 | `CodingAgent` | `AI-Agent/coding` |
| 2 | `Python` | `Skill/python` |
| 3 | `Hardware` | `Hardware/gpu` |
| 4 | `machine-learning` | `DeepLearning` |
| 5 | `RL/reward` | `RL` |

**Phase 2 — LLM 训练体系**
| 操作 | 原 tag | → 目标 tag |
|---|---|---|
| 6 | `Training` | `LLM/training` |
| 7 | `Post-training` | `LLM/training/post-train` |
| 8 | `SFT` | `LLM/training/post-train` |
| 9 | `RL` | `LLM/training/RL` |
| 10 | `Reasoning` | `LLM/reasoning` |
| 11 | `Test-TimeCompute` | `LLM/reasoning` |

**Phase 3 — RAG 体系**
| 操作 | 原 tag | → 目标 tag |
|---|---|---|
| 12 | `QueryProcessing` | `RAG/query` |
| 13 | `ChunkingDocs` | `RAG/chunking` |
| 14 | `Retrieval` | `RAG/retrieval` |
| 15 | `Embedding` | `RAG/embedding` |

**Phase 4 — AI Agent 体系**
| 操作 | 原 tag | → 目标 tag |
|---|---|---|
| 16 | `MCP` | `AI-Agent/MCP` |
| 17 | `ContextEngineering` | `AI-Agent/context-engineering` |
| 18 | `DeepResearch` | `AI-Agent/deep-research` |

**Phase 5 — 架构与其他**
| 操作 | 原 tag | → 目标 tag |
|---|---|---|
| 19 | `LLM/arch/MOE` | `LLM/arch/MoE` |
| 20 | `ObjectDetection` | `CV/detection` |
| 21 | `AIGC-video` | `AIGC/video` |
| 22 | `Hardware/gpu` | `Infra/gpu` |
| 23 | `AI-infra` | `Infra/AI` |
| 24 | `visualize` | `Skill/data-analysis` |
| 25 | `DataAnalysis` | `Skill/data-analysis` |

**Phase 6 — 用户需自行判断**
- `Claude`(9)：保留 or → `AI-Agent/coding`
- `VLM`(3)：保留 or → `LLM/arch/VLM`
- `AI+BI`(3)：保留 or → `Business/AI-BI`
- `创业`(4)：保留中文 or → `Business/startup`
- `面试`(7)：保留中文 or → `Career`

### 3. 大 tag 细分（后续慢慢做）

`LLM`(46) 和 `AI-Agent`(39) 笔记需逐条加子 tag。

### 4. iOS 移动端同步（待配置）

方案已定（Obsidian Git 插件 + GitHub Personal Access Token），但还未执行。需要：
- 在 GitHub 生成 PAT（fine-grained，只给 knowledge-bank 仓库读写权限）
- iOS Obsidian 装 Obsidian Git 插件，填入用户名 + PAT
- 或用 Working Copy 作为 Git 客户端
