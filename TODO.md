- [x] 全量 Ingest 阶段（Phase 1 至 Phase 6，共 191 篇 Sources 导入）已全部完成。
- [x] wiki/sources 需要修复每个的frontmatters(主要是source，191 篇已全部完成规范化清洗与 Cubox 物理路径 100% 关联)
- [x] wiki/下的entities、sources的tag需要整理（已完成 191 篇 sources 与 137 篇 entities 全量合规检查与补全）

## wiki
- [x] frontmatter不一致（已全量深度重构与清洗，sources/entities/concepts 共 652 篇全部达成字段一致与内容齐全）
- [x] sources/ 数量和 raw/ 是否一致（已对齐，双方均为 163 篇，完成 1对1 精准映射）
- [x] wiki/entities 频率不高的人/组织移除，可能需要设置一个阈值。本质上是精简entites+concepts，需要深度讨论（已按照「0次孤立清理 + 1次保留观察」策略，精准移除 25 篇无入链孤立实体页）
- [x] entities、conceptes等，是否移除tag（经讨论决定保留 Tag 字段，维持跨文件夹的多维度横向标签聚类能力）

## others
- [ ] workdocs/ 存放了工作期间的项目文档docx，需要解析并入库
- [ ] wucai的库存同步过来，同时合并目录cubox和notes，统一命名为raw/
