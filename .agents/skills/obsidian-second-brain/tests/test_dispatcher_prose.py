"""The AI-first rule summary must have exactly one definition.

Four adapters each emit a "How to operate" block whose third step summarises the
vault-write spec: the `## For future Claude` preamble, the required frontmatter
keys, wikilinks, recency markers, sources, confidence. Until now each adapter
carried its own hand-typed copy, differing only in the path it cites and in how
the prose happened to be line-wrapped.

CLAUDE.md says this rule is non-negotiable and must move in lockstep across
platforms. Four copies make that a promise nobody can keep: B21 was a path in
one copy that did not exist in that platform's own build, and it survived
because the other three were right and nobody diffed them.

These tests do not check the wording. They check that the wording has one home,
and that every platform's dispatcher actually ships it pointing at a file that
exists in that platform's own tree.
"""

from __future__ import annotations

import re
import subprocess
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parents[1]
ADAPTERS = REPO_ROOT / "adapters"
DIST = REPO_ROOT / "dist"

# (adapter dir, built dispatcher path relative to dist/<platform>/)
DISPATCHERS = [
    ("gemini-cli", "GEMINI.md"),
    ("opencode", "AGENTS.md"),
    ("codex-cli", "AGENTS.md"),
    ("pi", ".pi/skills/obsidian-second-brain/SKILL.md"),
]

MARKER = "Treat the AI-first vault rule"


@pytest.fixture(scope="module")
def built() -> Path:
    result = subprocess.run(
        ["bash", "scripts/build.sh"], cwd=REPO_ROOT, check=False,
        capture_output=True, text=True, encoding="utf-8", errors="replace",
    )
    assert result.returncode == 0, f"all-platforms build failed:\n{result.stderr}"
    return DIST


def test_the_rule_summary_is_defined_once():
    """In lib.sh, and nowhere else."""
    lib = (ADAPTERS / "lib.sh").read_text(encoding="utf-8")
    assert MARKER in lib, "emit_ai_first_rule no longer holds the rule summary"

    offenders = []
    for adapter in sorted(ADAPTERS.glob("*/adapter.sh")):
        if MARKER in adapter.read_text(encoding="utf-8"):
            offenders.append(adapter.parent.name)
    assert not offenders, (
        f"{offenders} re-inlined the AI-first rule summary instead of calling "
        "emit_ai_first_rule. Copies drift silently - that is how B21 shipped a "
        "reference path that did not exist in its own platform's build."
    )


@pytest.mark.parametrize("platform,_dispatcher", DISPATCHERS)
def test_each_dispatcher_calls_the_helper(platform, _dispatcher):
    text = (ADAPTERS / platform / "adapter.sh").read_text(encoding="utf-8")
    assert "emit_ai_first_rule " in text, (
        f"{platform}'s dispatcher no longer emits the AI-first rule at all, so "
        "that platform's agent is never told the vault-write spec is binding"
    )


@pytest.mark.parametrize("platform,dispatcher", DISPATCHERS)
def test_the_cited_path_exists_in_that_platforms_build(built, platform, dispatcher):
    """B21 verbatim: the rule is useless if its own path 404s.

    Resolved relative to the dispatcher's own directory, which is what an agent
    reading that file would do - not relative to the build root.
    """
    doc = built / platform / dispatcher
    assert doc.is_file(), f"{platform} did not emit {dispatcher}"

    text = doc.read_text(encoding="utf-8")
    m = re.search(rf"{MARKER} \(`([^`]+)`\)", text)
    assert m, f"{platform}'s dispatcher does not carry the rule summary"

    cited = (doc.parent / m.group(1)).resolve()
    assert cited.is_file(), (
        f"{platform}'s dispatcher points at {m.group(1)}, which does not exist "
        f"relative to {dispatcher}. The agent is told to follow a spec it "
        "cannot open."
    )
