---
type: concept
tags:
- Skill/knowledge-bank
- AI-Agent/coding
summary: LLM Wiki 范式中的 Lint 操作，定期体检知识库逻辑矛盾、孤立节点、死链、过时内容与占位符页面。
sources:
- wiki/sources/Karpathy推文引发的LLM_Wiki知识库搭建实践.md
created: '2026-07-22'
updated: '2026-07-22'
---

# 概念：Wiki健康检查 (Lint)

## 定义

**Wiki 健康检查（Lint）** 是 [[concepts/概念_LLM_Wiki范式|LLM Wiki 范式]] 中的四大核心操作之一。由于知识库会随着连续摄入（Ingest）不断膨胀，Lint 操作负责定期给 Wiki 进行自动化“体检”与图谱垃圾回收（GC）。

## 六大核心检查项

1. **逻辑矛盾**：检测新旧来源及词条页面之间的推导或结论冲突。
2. **死链与孤立节点**：扫描没有任何入链（In-degree = 0）的冷门孤立页面或指向已删文件的失效双链。
3. **越级直连审计**：确保末端产物（Entities/Concepts）Frontmatter `sources:` 字段只依赖 `wiki/sources/`，严禁绕过摘要直连 `raw/`。
4. **语法与 Tag 污染**：检测未转义的伪标签与伪链接。
5. **占位符与缺失页面**：清理空占位符或补齐高频被引用但尚未创建的缺口。
6. **未摄入文件审查**：扫描 `raw/` 或 `Clippings/` 中尚在队列中的物理文件。

## 自动化工具支撑

在本项目中，可以通过运行 Python 治理脚本 `python3 scripts/vault_lint.py lint` 自动化执行全库健康审计。

## 关联

- 相关概念：[[concepts/概念_LLM_Wiki范式]]、[[concepts/概念_Ingest入库闭环]]
- 来源：[[Karpathy推文引发的LLM_Wiki知识库搭建实践]]
