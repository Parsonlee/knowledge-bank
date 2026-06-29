# Wiki Log

> 操作日志，每次 ingest / query / lint 后追加记录。

## 2026-06-29 ingest | 大模型显存计算与优化（基于全文）
- 来源：tmp/Cubox-批量导出文章-所有收藏-205 收藏-全文/[LLM]大模型显存计算公式与优化 - 知乎.md（全文）
- 高亮参考：Cubox/[LLM]大模型显存计算公式与优化 - 知乎-2025-05-06.md（Annotations）
- 创建文件：
  - wiki/sources/大模型显存计算与优化.md (confidence: high)
  - wiki/concepts/概念_显存组成与估算.md (confidence: high)
  - wiki/concepts/概念_训练并行策略.md (confidence: high)
  - wiki/concepts/概念_激活值重计算.md (confidence: high)
  - wiki/concepts/概念_Zero显存优化.md (confidence: high)
  - wiki/entities/实体_DeepSpeed.md (confidence: medium — 全文仅简要提及)
  - wiki/entities/实体_Megatron.md (confidence: medium — 全文引用其论文公式)
- 全部内容基于全文，未使用模型自身知识补全

## 2026-06-29 test | 首次 ingest 测试（已回滚）
- 来源：Cubox/[LLM]大模型显存计算公式与优化（知乎 URL 403 不可达）
- 结论：知乎反爬，Cubox 内容不足以支撑 ingest，生成内容依赖模型补全，违反来源可追溯原则
- 操作：删除全部生成页面，知乎移入不可爬列表
