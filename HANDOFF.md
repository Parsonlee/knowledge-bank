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

### 0. 🚧 LLM Wiki 改造（进行中）

将知识库改造为 Karpathy LLM Wiki 模式（三层架构）。

**已完成**：
- 三层架构脚手架：`Cubox/`(原始层) + `wiki/`(知识层) + `TheSchema.md`(规则层，复用 BlinkLLMWiki 模板)
- `wiki/` 子目录：sources/concepts/entities/comparisons/overview + index.md + log.md + fail.md
- 单篇 ingest 流程验证：确认"全文 + highlight 加权"策略产出高质量可追溯内容
- 关键突破：用户导出 205 篇全文到 `tmp/Cubox-批量导出文章-所有收藏-205 收藏-全文/`，解决反爬问题
- ✅ **Phase 1（Infra+CV+DeepLearning）**：21篇完成，验收 PASS（详见 `wiki/verify-phase1.md`）
- ✅ **Phase 2（RAG）**：~43篇完成，验收 PASS（详见 `wiki/verify-phase2.md`）

**当前产出**：63 source + 155 concept + 43 entity，0 failures

**下一步（明日继续）**：Phase 3（LLM 集群，~66篇，13批）
- 按 tag 集群分批，每批 5 篇，串行执行
- 每集群完成后验收（可在主对话直接做或派 agent）
- 不可读文章跳过记入 `wiki/fail.md`
- Phase 3-6：LLM → AI-Agent → Skill+AIGC → 其它

**已知问题**：
- 外部 API 中转服务额度不足（$0.27 remain），批次 6/9 各中断一次。**明天继续前需检查/充值**
- 全文导出中有 2 个空文件（50B）：`AI时代的快速研发小队分享.md`、技术演进相关 —— 遇到时跳过记 fail

### 1. 修复自动推送（1 分钟）

在 Obsidian Git 设置面板里把 **Vault backup interval (minutes)** 从 `0` 改成 `10`。

### 2. ✅ Tag 整理（已完成）

全部 tag 已整理完毕（53 个 tag，层级清晰）。已清除的问题 tag：`clipping`、`cubox`、`clippings`、`RL`(裸)、`AI+BI`、`Claude`、`AI Product`、`MachineLearning`、`Skill`(裸)、`LLM/training/post-train/SFT`、`Infra/gpu/gpu`、`AI-Agent/coding with Tools`、`Agent with Tools`、`Agent UI`、`AI-Agent/coding UI`。

已处理：补空 tag 文章(10篇)、修重复 tag(9篇)、修非标准 tag(12篇)、修错误分类(12篇)、Claude tag 拆分为 Skill/claude-code + AI-Agent 子 tag。

### 3. ✅ inbox/ 重复文章清理（已完成）

inbox/ 中 39 篇与 Cubox/ 内容重复的文件已删除。4 篇独有文章已移到 notes/ 并打好 tag。inbox/ 现为空目录，保留作速记收件箱。

### 4. 原有 Phase 操作清单（归档，已完成）

以下为已执行完的操作记录，保留用于参考：

**Phase 1 — 消除重复**
| 操作 | 原 tag | → 目标 tag |
|---|---|---|
| 1 | `CodingAgent` | `AI-Agent/coding` |
| 2 | `Python` | `Skill/python` |
| 3 | `Hardware` | `Infra/gpu` |
| 4 | `Hardware/gpu` | `Infra/gpu` |
| 5 | `machine-learning` | `DeepLearning` |
| 6 | `RL/reward` | `LLM/training/RL` |

**Phase 2 — LLM 训练体系**
| 操作 | 原 tag | → 目标 tag |
|---|---|---|
| 7 | `Training` | `LLM/training` |
| 8 | `Post-training` | `LLM/training/post-train` |
| 9 | `SFT` | `LLM/training/post-train` |
| 10 | `RL` | `LLM/training/RL` |
| 11 | `Reasoning` | `LLM/reasoning` |
| 12 | `Test-TimeCompute` | `LLM/reasoning` |

**Phase 3 — RAG 体系**
| 操作 | 原 tag | → 目标 tag |
|---|---|---|
| 13 | `QueryProcessing` | `RAG/query` |
| 14 | `ChunkingDocs` | `RAG/chunking` |
| 15 | `Retrieval` | `RAG/retrieval` |
| 16 | `Embedding` | `RAG/embedding` |

**Phase 4 — AI Agent 体系**
| 操作 | 原 tag | → 目标 tag |
|---|---|---|
| 17 | `MCP` | `AI-Agent/MCP` |
| 18 | `ContextEngineering` | `AI-Agent/context-engineering` |
| 19 | `DeepResearch` | `AI-Agent/deep-research` |

**Phase 5 — 架构与其他**
| 操作 | 原 tag | → 目标 tag |
|---|---|---|
| 20 | `LLM/arch/MOE` | `LLM/arch/MoE` |
| 21 | `ObjectDetection` | `CV/detection` |
| 22 | `AIGC-video` | `AIGC/video` |
| 23 | `AI-infra` | `Infra/AI` |
| 24 | `visualize` | `Skill/data-analysis` |
| 25 | `DataAnalysis` | `Skill/data-analysis` |

**Phase 6 — 已确认的归属**
| 操作 | 原 tag | → 目标 tag | 说明 |
|---|---|---|---|
| 26 | `AI+BI` | `AI-Agent/AI-BI` | Agent 应用场景 |
| 27 | `VLM` | `LLM/arch/VLM` | 视觉语言模型归入架构 |
| 28 | `创业` | `创业`（保留顶层） | 不动 |
| 29 | `面试` | `面试`（保留顶层） | 不动 |

**Phase 6 补充 — `Claude`(9) 需逐条拆分**
- Claude Code 使用技巧/工作流分享 → 改 tag 为 `Skill/claude-code`
- Agent 技术文 → 改为对应 Agent 子 tag
- 具体拆分对照（进笔记 → 编辑 frontmatter tags，把 `Claude` 替换为目标 tag）：
  - `Claude Code 完全指南` → `Skill/claude-code`
  - `Claude Code 2.0.40版本后的一些实用更新` → `Skill/claude-code`
  - `用Claude code重塑编程工作流` → `Skill/claude-code`
  - `一个半月高强度Claude Code使用后感受` → `Skill/claude-code`
  - `写好 CLAUDE.md - HumanLayer 博客` → `Skill/claude-code`
  - `awesome-claude-code-subagents` → `Skill/claude-code`
  - `私域知识工程实战：如何让AI一次性写出高质量代码？` → `Skill/claude-code`
  - `Anthropic再发Agent神文：像人类工程师一样思考` → 去掉 `Claude`，加 `AI-Agent`
  - `从第一性原理深度拆解 Claude Agent Skill - 宝玉的分享` → 去掉 `Claude`，加 `AI-Agent/skill`

### 3. ✅ 大 tag 细分（已完成首轮 2026-06-26）

`LLM` 和 `AI-Agent` 下"只打父级、缺子 tag"的笔记已逐条检查处理。判断方式：标题/标注足够时直接归类，标题不足的派 haiku subagent 用 web-content-fetcher skill 读公众号/知乎正文再定子 tag。

**LLM（15 篇）：**
- 细分 6 篇：CoT综述→`reasoning`、幻觉陷阱→`hallucination`、Scaling Law→`training`、显存占用/显存计算公式→`inference`(各保留 Infra/gpu)、MiniMax&Kimi注意力→`arch/attention`
- 保留裸 `LLM` 8 篇：蚂蚁推荐、面试百问、MIT 50题、领域综述、Jina创业复盘、Karpathy教学、Transformer 3D可视化、OpenAI最佳实践（均为综述/面试合集/入门教学/跨主题指南，无单一子 tag）
- 删除 1 篇：「用 JSON 喂 LLM 新格式」

**AI-Agent（5 篇）：**
- 细分 1 篇：阿里云 Agent 方法论→`prompt-engineering`
- 保留裸 `AI-Agent` 4 篇：应用架构演进、全面调研、Agent vs Workflow、Agent系统开发经验（均为系统工程综述/概念辨析，无单一主轴）

原则：综述/面试合集/入门教学/跨主题文章天然跨子主题，保留父级 tag 而非强塞子 tag。

### 4. iOS 移动端同步（待配置）

方案已定（Obsidian Git 插件 + GitHub Personal Access Token），但还未执行。需要：
- 在 GitHub 生成 PAT（fine-grained，只给 knowledge-bank 仓库读写权限）
- iOS Obsidian 装 Obsidian Git 插件，填入用户名 + PAT
- 或用 Working Copy 作为 Git 客户端

### 5. 当前 Tag 体系参考（53 个 tag）

```
LLM (69)
├── LLM/arch (15): Mamba(6), MoE(4), VLM(3), attention(1)
├── LLM/training (17): post-train(6), RL(6), pre-train(1)
├── LLM/inference (3): kv-cache(1)
├── LLM/reasoning (5)
├── LLM/hallucination (2)
└── LLM/tokenization (1)

AI-Agent (47)
├── AI-Agent/coding (10)
├── AI-Agent/tools (7)
├── AI-Agent/context-engineering (6)
├── AI-Agent/deep-research (4)
├── AI-Agent/AI-BI (4)
├── AI-Agent/skill (3)
├── AI-Agent/prompt-engineering (2)
├── AI-Agent/multi-agent (2)
├── AI-Agent/memory (2)
└── AI-Agent/UI (2)

RAG (63)
├── RAG/embedding (9)
├── RAG/query (7)
├── RAG/chunking (7)
├── RAG/retrieval (3)
└── RAG/eval (1)

Skill (24)
├── Skill/python (10): pytorch(2), web(1)
├── Skill/data-analysis (7)
├── Skill/claude-code (6)
└── Skill/linux (1)

CV (12): detection(4), data-augmentation(2), arch(1)
Infra (6): AI(4), gpu(2)
DeepLearning (8) | AIGC (8) | 创业 (8)
面试 (7) | Life (7) | Recommendation (2) | TTS (1)
```

