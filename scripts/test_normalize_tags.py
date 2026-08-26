#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Unit tests for normalize_tags.py
"""

import os
import sys
import tempfile
import shutil
import unittest
from pathlib import Path
from contextlib import redirect_stdout
from io import StringIO

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import normalize_tags
import vault_lint


class TestNormalizeTags(unittest.TestCase):
    def setUp(self):
        self.test_dir = Path(tempfile.mkdtemp())

    def tearDown(self):
        shutil.rmtree(self.test_dir)

    def test_tag_synchronization_with_vault_lint(self):
        """测试 normalize_tags 与 vault_lint 权威定义保持同步"""
        # 所有顶级标签应在 APPROVED_TAGS 中
        for top_tag in vault_lint.STANDARD_TOP_LEVEL_TAGS:
            self.assertIn(top_tag, normalize_tags.APPROVED_TAGS)
        
        # 所有分支叶子应在 APPROVED_TAGS 中
        for branch, leaves in vault_lint.STANDARD_TAG_BRANCHES.items():
            for leaf in leaves:
                self.assertIn(f"{branch}/{leaf}", normalize_tags.APPROVED_TAGS)

    def test_normalize_valid_tags_unchanged(self):
        """测试合规标签不做不必要修改"""
        valid_tags = ["LLM/arch", "Skill/python", "DeepLearning", "AI-Agent/coding", "RAG/retrieval"]
        res = normalize_tags.normalize_tag_list(valid_tags, ptype="source")
        self.assertEqual(res, valid_tags)

    def test_normalize_tag_mapping(self):
        """测试映射字典查表转换"""
        test_cases = [
            (["RAG"], ["RAG/retrieval"]),
            (["LLM"], ["LLM/arch"]),
            (["machine-learning"], ["Skill/data-analysis"]),
            (["KV-Cache"], ["LLM/inference"]),
            (["loop-engineering"], ["AI-Agent/coding"]),
            (["Multi-Agent"], ["AI-Agent/multi-agent"]),
            (["descriptor"], ["Skill/python"]),
            (["gpu"], ["Infra/gpu"]),
            (["MLOps"], ["Infra/AI"]),
            (["Skill/knowledge-bank"], ["AI-Agent/skill"]),
        ]
        for input_tags, expected in test_cases:
            res = normalize_tags.normalize_tag_list(input_tags, ptype="source")
            self.assertEqual(res, expected, f"Failed for input {input_tags}")

    def test_noise_tags_cleaned_to_empty(self):
        """测试噪音标签清洗后输出空列表，且不进行猜测兜底 (Fallback 策略改造)"""
        output = StringIO()
        with redirect_stdout(output):
            res = normalize_tags.normalize_tag_list(
                ["clippings"],
                ptype="source",
                content="This is about AI Agent loop engineering and rag retrieval with python."
            )
        # 验证严禁猜测分类，必须返回空列表
        self.assertEqual(res, [])
        self.assertIn("待人工复核", output.getvalue())

    def test_overview_special_tags(self):
        """测试 overview 综述页允许顶层宏观分类"""
        res_overview = normalize_tags.normalize_tag_list(["RAG", "LLM"], ptype="overview")
        self.assertIn("RAG", res_overview)
        self.assertIn("LLM", res_overview)

        res_source = normalize_tags.normalize_tag_list(["RAG", "LLM"], ptype="source")
        self.assertEqual(res_source, ["RAG/retrieval", "LLM/arch"])

    def test_forbidden_fields_removal_in_process_file(self):
        """测试在处理 wiki 文件时剔除禁止字段"""
        file_path = self.test_dir / "wiki" / "sources" / "test_source.md"
        file_path.parent.mkdir(parents=True, exist_ok=True)
        content = (
            "---\n"
            "type: \"source\"\n"
            "tags: [\"machine-learning\"]\n"
            "summary: \"Test summary\"\n"
            "sources: [\"raw/articles/test.md\"]\n"
            "updated: \"2026-08-26\"\n"
            "confidence: high\n"
            "created: \"2026-08-01\"\n"
            "ai-first: true\n"
            "---\n"
            "# Content\n"
        )
        file_path.write_text(content, encoding="utf-8")

        mod, orig, new_fm, diff = normalize_tags.process_file(str(file_path), str(self.test_dir), apply=True)
        self.assertTrue(mod)
        self.assertNotIn("confidence", new_fm)
        self.assertNotIn("created", new_fm)
        self.assertNotIn("ai-first", new_fm)
        self.assertEqual(new_fm["tags"], ["Skill/data-analysis"])

        # 验证落盘文件内容
        saved_content = file_path.read_text(encoding="utf-8")
        self.assertNotIn("confidence", saved_content)
        self.assertNotIn("created", saved_content)
        self.assertNotIn("ai-first", saved_content)


if __name__ == "__main__":
    unittest.main()
