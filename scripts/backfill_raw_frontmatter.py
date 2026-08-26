#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Knowledge Bank Historical Raw Articles Frontmatter Backfill Tool
遵循 AGENTS.md 规范，为 raw/articles/ 下早期邮件拆分生成的无 Frontmatter 裸文本批量回溯注入标准骨架。

用法:
  uv run --with pyyaml python scripts/backfill_raw_frontmatter.py           # 默认 Dry-run 预演
  uv run --with pyyaml python scripts/backfill_raw_frontmatter.py --dry-run # 显式 Dry-run 预演
  uv run --with pyyaml python scripts/backfill_raw_frontmatter.py --apply   # 确认执行批量注入落盘
"""

import os
import sys
import re
import argparse
import yaml
from pathlib import Path
from datetime import datetime
from email.utils import parsedate_to_datetime


def parse_rfc2822_date(date_str):
    """解析邮件 RFC 2822 日期为 YYYY-MM-DD"""
    try:
        dt = parsedate_to_datetime(date_str)
        return dt.strftime("%Y-%m-%d")
    except Exception:
        return None


def get_sources_tag_map(workspace):
    """构建 raw/articles 路径到对应 wiki/sources tags 的映射表"""
    sources_dir = os.path.join(workspace, "wiki/sources")
    raw_to_tags = {}
    if not os.path.exists(sources_dir):
        return raw_to_tags

    for f in os.listdir(sources_dir):
        if not f.endswith(".md"):
            continue
        p = os.path.join(sources_dir, f)
        try:
            with open(p, "r", encoding="utf-8", errors="ignore") as fp:
                c = fp.read()
            m = re.match(r"^---\n(.*?)\n---", c, re.DOTALL)
            if m:
                data = yaml.safe_load(m.group(1))
                if isinstance(data, dict):
                    srcs = data.get("sources", [])
                    tags = data.get("tags", [])
                    if isinstance(srcs, list):
                        for s in srcs:
                            if isinstance(s, str) and s.startswith("raw/"):
                                raw_to_tags[s] = tags if isinstance(tags, list) else []
        except Exception:
            pass
    return raw_to_tags


def process_raw_file(file_path, workspace, raw_to_tags, apply=False):
    """
    检查单个 raw 文件。如果无 Frontmatter，提取元数据并注入标准 Frontmatter。
    """
    rel_path = os.path.relpath(file_path, workspace)
    try:
        with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
            content = f.read()
    except Exception as e:
        return False, None, f"读取失败: {e}"

    if content.startswith("---"):
        return False, None, "已有 Frontmatter，跳过"

    filename = os.path.basename(file_path)

    # 1. 提取标题
    m_title = re.search(r"^#\s+(.+)$", content, re.MULTILINE)
    title = m_title.group(1).strip() if m_title else filename[:-3]

    # 2. 提取邮件主题
    m_subject = re.search(r"-\s+\*\*原邮件主题\*\*:\s*(.+)$", content, re.MULTILINE)
    email_subject = m_subject.group(1).strip() if m_subject else title

    # 3. 提取发送人
    m_sender = re.search(r"-\s+\*\*发送人\*\*:\s*(.+)$", content, re.MULTILINE)
    email_sender = m_sender.group(1).strip() if m_sender else "Daily Dose of DS <avi@dailydoseofds.com>"

    # 4. 提取邮件日期
    m_date = re.search(r"-\s+\*\*日期\*\*:\s*(.+)$", content, re.MULTILINE)
    email_date = m_date.group(1).strip() if m_date else ""

    # 5. 提取邮件 ID 与 文章 ID
    m_id = re.search(r"-\s+\*\*(?:邮件\s*)?ID\*\*:\s*(.+)$", content, re.MULTILINE)
    email_id = m_id.group(1).strip() if m_id else ""

    m_art_id = re.search(r"-\s+\*\*文章\s*ID\*\*:\s*(.+)$", content, re.MULTILINE)
    article_id = m_art_id.group(1).strip() if m_art_id else (f"{email_id}:1" if email_id else "")

    # 6. 计算发表日期 published
    published = None
    if email_date:
        published = parse_rfc2822_date(email_date)
    if not published:
        m_date_file = re.match(r"^(\d{4}-\d{2}-\d{2})", filename)
        if m_date_file:
            published = m_date_file.group(1)
        else:
            published = datetime.now().strftime("%Y-%m-%d")

    # 7. 继承或获取 tags
    inherited_tags = raw_to_tags.get(rel_path, [])
    # 确保 tags 纯净
    valid_tags = [t for t in inherited_tags if isinstance(t, str) and t.strip()]

    # 构造 Frontmatter 字典
    fm_dict = {
        "title": title,
        "source_key": "dailydoseofds",
        "email_subject": email_subject,
        "email_sender": email_sender,
        "email_date": email_date,
        "email_id": email_id,
        "article_id": article_id,
        "published": published,
        "tags": valid_tags,
    }

    fm_yaml = yaml.dump(fm_dict, allow_unicode=True, sort_keys=False, default_flow_style=False).strip()
    new_content = f"---\n{fm_yaml}\n---\n\n{content}"

    if apply:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(new_content)

    return True, fm_dict, f"成功注入 Frontmatter (published: {published}, tags: {valid_tags})"


def main():
    parser = argparse.ArgumentParser(description="Raw Articles Frontmatter Backfill Tool")
    parser.add_argument("--dry-run", action="store_true", help="预演模式（不修改文件）")
    parser.add_argument("--apply", action="store_true", help="正式落盘注入 Frontmatter")
    args = parser.parse_args()

    apply = args.apply
    workspace = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    raw_dir = os.path.join(workspace, "raw/articles")

    if not apply:
        print("=" * 60)
        print("🔍 [Raw Frontmatter Backfill] 正在以 Dry-Run 预演模式运行...")
        print("=" * 60)
    else:
        print("=" * 60)
        print("🚀 [Raw Frontmatter Backfill] 正在执行 Frontmatter 批量注入落盘...")
        print("=" * 60)

    raw_to_tags = get_sources_tag_map(workspace)

    total_scanned = 0
    injected_files = []

    for root, _, files in os.walk(raw_dir):
        for file in sorted(files):
            if file.endswith(".md"):
                total_scanned += 1
                full_p = os.path.join(root, file)
                rel_p = os.path.relpath(full_p, workspace)
                mod, fm, msg = process_raw_file(full_p, workspace, raw_to_tags, apply=apply)
                if mod:
                    injected_files.append((rel_p, fm, msg))

    print(f"\n📊 扫描完成！共扫描 raw/articles 目录 {total_scanned} 篇文件。")
    print(f"   需补全 Frontmatter 文件数: {len(injected_files)} 篇")
    print("-" * 60)

    for rel_p, fm, msg in injected_files:
        print(f"  📄 [{rel_p}]")
        print(f"     ↳ {msg}")

    if not apply:
        print("\n" + "=" * 60)
        print("✅ Dry-run 预演完成！若确认无误，请运行以下命令正式执行落盘:")
        print("   uv run --with pyyaml python scripts/backfill_raw_frontmatter.py --apply")
        print("=" * 60)
    else:
        print("\n" + "=" * 60)
        print(f"✅ 批量回溯注入完成！已成功为 {len(injected_files)} 篇历史裸文本补全标准 Frontmatter。")
        print("=" * 60)


if __name__ == "__main__":
    main()
