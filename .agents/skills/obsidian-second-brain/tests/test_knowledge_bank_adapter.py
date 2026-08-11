import hashlib
import shutil
import subprocess
import tempfile
import unittest
from pathlib import Path


class TestAdapter(unittest.TestCase):
    def setUp(self):
        self.workspace = Path(__file__).resolve().parent.parent.parent.parent.parent
        self.skill_dir = self.workspace / ".agents/skills/obsidian-second-brain"
        self.skill_md = self.skill_dir / "SKILL.md"
        self.upstream_md = self.skill_dir / "UPSTREAM_SKILL.md"

    def test_governance_is_agents_md(self):
        with open(self.skill_md, "r", encoding="utf-8") as f:
            content = f.read()
        self.assertIn("唯一", content)
        self.assertIn("AGENTS.md", content)

    def test_upstream_archive(self):
        self.assertTrue(self.upstream_md.exists())
        with open(self.upstream_md, "rb") as f:
            h = hashlib.sha256(f.read()).hexdigest()
        self.assertEqual(h, "67325d177d51e7eb331d05e1944d23f8c2206f128d9a000cf26aee6fd4cb2d9d")

    def test_source_chain_direction(self):
        with open(self.skill_md, "r", encoding="utf-8") as f:
            content = f.read()
        self.assertIn("wiki/sources/", content)
        self.assertIn("严禁直接指向 `raw/`", content)

    def test_git_redline_no_l3_exception(self):
        with open(self.skill_md, "r", encoding="utf-8") as f:
            content = f.read()
        l3_block = content.split("### 4.2", 1)[1].split("### 4.3", 1)[0].lower()
        permanent_block = content.split("### 4.3", 1)[1].split("## 5.", 1)[0].lower()
        self.assertIn("即使拥有 l3 授权也**绝对禁止**", permanent_block)
        for operation in ("commit", "stash", "checkout", "reset", "push"):
            with self.subTest(operation=operation):
                self.assertIn(operation, permanent_block)
                self.assertNotIn(operation, l3_block)

    def test_cli_whitelist(self):
        with open(self.skill_md, "r", encoding="utf-8") as f:
            content = f.read()
        self.assertIn("vault_stats.py --print-only", content)
        # Verify it's explicitly disabled or not in the whitelist bullet points
        whitelist_block = content.split("### 4.2")[0]
        self.assertNotIn("- `uv run --directory .agents/skills/obsidian-second-brain python scripts/vault_scan.py`", whitelist_block)

    def test_disabled_features(self):
        with open(self.skill_md, "r", encoding="utf-8") as f:
            content = f.read()
        self.assertIn("自动产生 Synthesis", content)
        self.assertIn("后台 Agent Hook", content)
        self.assertIn("PostCompact", content)
        self.assertIn("自动写入 Daily Note", content)

    def test_independent_uv_env(self):
        with open(self.skill_md, "r", encoding="utf-8") as f:
            content = f.read()
        self.assertIn("uv --directory", content)

    def test_no_nested_skill_md(self):
        nested_skills = sorted(
            path for path in self.skill_dir.rglob("SKILL.md")
            if path != self.skill_md
        )
        self.assertEqual([], nested_skills, f"Found nested SKILL.md: {nested_skills}")

    def _copy_build_fixture(self, temporary_root):
        isolated_skill = (
            temporary_root / ".agents" / "skills" / "obsidian-second-brain"
        )
        isolated_skill.mkdir(parents=True)
        shutil.copy2(self.skill_md, isolated_skill / "SKILL.md")
        shutil.copy2(self.skill_dir / "pyproject.toml", isolated_skill / "pyproject.toml")
        shutil.copytree(self.skill_dir / "adapters", isolated_skill / "adapters")
        shutil.copytree(self.skill_dir / "commands", isolated_skill / "commands")
        shutil.copytree(self.skill_dir / "references", isolated_skill / "references")
        scripts = isolated_skill / "scripts"
        scripts.mkdir()
        for name in ("build.sh", "lib.sh"):
            shutil.copy2(self.skill_dir / "scripts" / name, scripts / name)
        return isolated_skill

    @staticmethod
    def _skill_manifest(skill_dir):
        return sorted(path.relative_to(skill_dir) for path in skill_dir.rglob("SKILL.md"))

    @staticmethod
    def _run_build(skill_dir, *arguments):
        return subprocess.run(
            ["bash", str(skill_dir / "scripts" / "build.sh"), *arguments],
            cwd=skill_dir.parents[2],
            capture_output=True,
            text=True,
            check=False,
        )

    def test_active_skill_build_defaults_to_vault_tmp(self):
        with tempfile.TemporaryDirectory() as temporary_directory:
            temporary_root = Path(temporary_directory)
            isolated_skill = self._copy_build_fixture(temporary_root)
            before = self._skill_manifest(isolated_skill)

            result = self._run_build(
                isolated_skill, "--platform", "agent-skills"
            )

            expected_output = (
                temporary_root / "tmp" / "obsidian-second-brain-dist" /
                "agent-skills"
            )
            self.assertEqual(0, result.returncode, result.stderr)
            self.assertTrue((expected_output / "skills" / "obsidian-core" / "SKILL.md").is_file())
            self.assertFalse((isolated_skill / "dist").exists())
            self.assertEqual(before, self._skill_manifest(isolated_skill))
            self.assertIn(str(expected_output), result.stdout)

    def test_explicit_safe_output_is_honored(self):
        with tempfile.TemporaryDirectory() as temporary_directory:
            temporary_root = Path(temporary_directory)
            isolated_skill = self._copy_build_fixture(temporary_root)
            output_parent = temporary_root / "artifacts"
            output_parent.mkdir()
            output_dir = output_parent / "second-brain"

            result = self._run_build(
                isolated_skill,
                "--platform", "agent-skills",
                "--output-dir", str(output_dir),
            )

            self.assertEqual(0, result.returncode, result.stderr)
            self.assertTrue((output_dir / "agent-skills" / "skills" / "obsidian-core" / "SKILL.md").is_file())
            self.assertFalse((isolated_skill / "dist").exists())
            self.assertIn(str(output_dir / "agent-skills"), result.stdout)

    def test_explicit_active_skill_output_is_rejected(self):
        with tempfile.TemporaryDirectory() as temporary_directory:
            temporary_root = Path(temporary_directory)
            isolated_skill = self._copy_build_fixture(temporary_root)
            forbidden_output = isolated_skill / "dist"

            result = self._run_build(
                isolated_skill,
                "--platform", "agent-skills",
                "--output-dir", str(forbidden_output),
            )

            self.assertNotEqual(0, result.returncode)
            self.assertFalse(forbidden_output.exists())
            self.assertIn("must not be inside an active .agents/skills tree", result.stderr)

            linked_parent = temporary_root / "linked-output"
            linked_parent.symlink_to(isolated_skill, target_is_directory=True)
            linked_output = linked_parent / "generated"
            symlink_result = self._run_build(
                isolated_skill,
                "--platform", "agent-skills",
                "--output-dir", str(linked_output),
            )
            self.assertNotEqual(0, symlink_result.returncode)
            self.assertFalse((isolated_skill / "generated").exists())
            self.assertIn(
                "must not be inside an active .agents/skills tree",
                symlink_result.stderr,
            )

    def test_build_options_require_values(self):
        with tempfile.TemporaryDirectory() as temporary_directory:
            isolated_skill = self._copy_build_fixture(Path(temporary_directory))
            for option in ("--platform", "--output-dir"):
                with self.subTest(option=option):
                    result = self._run_build(isolated_skill, option)
                    self.assertNotEqual(0, result.returncode)
                    self.assertIn(f"{option} requires", result.stderr)

if __name__ == '__main__':
    unittest.main()
