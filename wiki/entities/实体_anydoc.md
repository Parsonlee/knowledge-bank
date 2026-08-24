---
type: "entity"
tags: ["AI-Agent/tool-calling", "RAG/chunking"]
summary: "Firecrawl 开源的纯 Rust 高性能本地多格式文档解析转 Markdown 工具，采用中间稿两阶段解析与 Agent Skill 深度集成。"
sources: ["wiki/sources/Firecrawl 新工具开源，anydoc，将各种输入转换为md.md"]
updated: "2026-08-20"
---

# 实体：anydoc

## 简介
**anydoc** 是由 [[entities/实体_Firecrawl|Firecrawl]] 团队开源的纯 Rust 实现的多格式文档转 Markdown 工具，10 天内 GitHub Star 突破 15,000+。它旨在为大模型（LLM）数据供给、RAG 知识库构建以及编码智能体（Agent）提供速度极快、质量高度保真的本地文档提取能力。

## 核心技术与架构特征

1. **两阶段中间稿解析架构**：
   - **语义中间表示（IR）**：先将文件解析为统一结构的中间稿，精确捕获标题层级、段落、列表、合并单元格表格、代码块、脚注及 PPT 演讲备注等排版语义。
   - **Markdown 渲染输出**：将中间稿转换为规范干净的 Markdown，图片以引用文本形式呈现并缓存于本地。
2. **字节特征格式识别**：
   - 不依赖文件扩展名，直接通过读取文件头部及字节特征识别格式，具备高容错性。
3. **纯 Rust 实现与极致性能**：
   - 无 ML 模型及外部服务依赖，单文件转换最快仅需 4.4 毫秒。
   - 官方百篇真实文档横测表明，相较 libreoffice、markitdown、pandoc、[[entities/实体_Docling|Docling]] 等工具，在 14 种格式全支持、表格完整度与转换耗时上均具明显优势。
4. **格式全覆盖（8 大类 14 种格式）**：
   - 涵盖 Word（.docx, .doc）、PowerPoint（.pptx, .ppt）、Excel（.xlsx, .xls）、PDF、EPUB、RTF、ODT 等。
5. **多端交付与 Agent 生态集成**：
   - 提供 Node、Python、Rust SDK；
   - 支持通过 Agent Skill（`npx skills add firecrawl/anydoc`）直接扩展 [[entities/实体_Claude_Code|Claude Code]] 与 [[entities/实体_Codex|Codex]]；
   - 提供本地纯前端运行的 Web 在线转换工具。

## 边界与局限
- 本地引擎仅能提取具备文字层的常规 PDF，对扫描件/纯图片 PDF 需配合托管 API 与 OCR 识别；
- 暂不支持带密码保护和加密的文档。

## 关联页面
- **所属组织**：[[entities/实体_Firecrawl|Firecrawl]]
- **同类工具**：[[entities/实体_Docling|Docling]]
- **集成宿主**：[[entities/实体_Claude_Code|Claude Code]]、[[entities/实体_Codex|Codex]]
- **相关概念**：[[concepts/概念_文档结构切分|文档结构切分]]、[[concepts/概念_表格序列化|表格序列化]]、[[concepts/概念_Agent_Skills元工具架构|Agent Skills 元工具架构]]
- **支撑来源**：[[sources/Firecrawl 新工具开源，anydoc，将各种输入转换为md|Firecrawl 新工具开源，anydoc，将各种输入转换为md]]
