#!/usr/bin/env bash
# =============================================================================
# scripts/build.sh - Compile platform-neutral source into a safe output tree
# =============================================================================
# Usage:
#   bash scripts/build.sh                       # builds all platforms
#   bash scripts/build.sh --platform claude-code
#   bash scripts/build.sh --platform codex-cli
#   bash scripts/build.sh --output-dir /tmp/obsidian-second-brain-dist
#
# Reads the platform-neutral source (commands/, references/, DISPATCHER.md)
# and emits a platform-specific tree under <output-dir>/<platform>/.
#
# Each adapter is a self-contained shell script in adapters/<platform>/
# that defines an adapter_build() function called by this orchestrator.
# =============================================================================
set -eo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
# shellcheck source=scripts/lib.sh
source "$SCRIPT_DIR/lib.sh"

# ── Parse args ──────────────────────────────────────────────────────────────
PLATFORM=""
OUTPUT_DIR=""
while [[ $# -gt 0 ]]; do
  case "$1" in
    --platform)
      [[ $# -ge 2 && -n "$2" && "$2" != --* ]] \
        || die "--platform requires a non-empty value"
      PLATFORM="$2"
      shift 2
      ;;
    --output-dir)
      [[ $# -ge 2 && -n "$2" && "$2" != --* ]] \
        || die "--output-dir requires a non-empty path"
      OUTPUT_DIR="$2"
      shift 2
      ;;
    --help|-h)
      cat <<'EOF'
Usage: bash scripts/build.sh [--platform <name>] [--output-dir <path>]

Without --platform, builds every platform listed under adapters/.

Available platforms:
  agent-skills  - Antigravity / Codex CLI / OpenCode (unified .agents/skills/ tree)
  claude-code   - Claude Code (slash commands + CLAUDE.md)
  codex-cli     - OpenAI Codex CLI (native Agent Skills, .agents/skills/)
  gemini-cli    - Gemini CLI (GEMINI.md + .gemini/commands/)
  opencode      - OpenCode (AGENTS.md + .opencode/commands/)
  hermes        - Nous Research Hermes Agent (native skills, skills/<category>/)
  pi            - Pi Coding Agent (package.json + .pi/prompts/ + .pi/skills/)
EOF
      exit 0
      ;;
    *) die "Unknown argument: $1 (use --help for usage)" ;;
  esac
done

# Normalize an absolute path lexically. The build always uses the normalized
# value, so a path containing `..` cannot acquire different semantics later.
normalize_absolute_path() {
  local path="$1" rest part normalized=""
  case "$path" in
    /*) ;;
    *) path="$PWD/$path" ;;
  esac

  rest="${path#/}"
  while [[ -n "$rest" ]]; do
    case "$rest" in
      */*) part="${rest%%/*}"; rest="${rest#*/}" ;;
      *) part="$rest"; rest="" ;;
    esac
    case "$part" in
      ""|.) ;;
      ..) normalized="${normalized%/*}" ;;
      *) normalized="${normalized:+$normalized/}$part" ;;
    esac
  done
  printf '/%s\n' "$normalized"
}

reject_active_skills_output() {
  local path="$1"
  case "$path" in
    */.agents/skills|*/.agents/skills/*)
      die "Output directory must not be inside an active .agents/skills tree: $path"
      ;;
  esac
}

# Resolve symlinks in the nearest existing ancestor without creating anything.
# This closes the case where a harmless-looking output path traverses a symlink
# into an active `.agents/skills` discovery tree.
resolve_output_dir() {
  local candidate probe suffix="" segment resolved_probe resolved
  candidate="$(normalize_absolute_path "$1")"
  [[ "$candidate" != "/" ]] || die "Output directory must not be the filesystem root"
  reject_active_skills_output "$candidate"

  probe="$candidate"
  while [[ ! -e "$probe" && ! -L "$probe" ]]; do
    segment="${probe##*/}"
    suffix="/$segment$suffix"
    probe="${probe%/*}"
    [[ -n "$probe" ]] || probe="/"
  done
  [[ -d "$probe" ]] || die "Output path has a non-directory ancestor: $probe"
  resolved_probe="$(cd -P "$probe" && pwd)" \
    || die "Cannot resolve output directory ancestor: $probe"
  resolved="$resolved_probe$suffix"
  reject_active_skills_output "$resolved"
  printf '%s\n' "$resolved"
}

if [[ -z "$OUTPUT_DIR" ]]; then
  if [[ "$REPO_ROOT" == *".agents/skills/"* ]]; then
    # Prevent discovery leakage when this source itself is an active Skill.
    knowledge_bank_root="${REPO_ROOT%%/.agents/skills/*}"
    OUTPUT_DIR="$knowledge_bank_root/tmp/obsidian-second-brain-dist"
  else
    OUTPUT_DIR="$REPO_ROOT/dist"
  fi
fi
OUTPUT_DIR="$(resolve_output_dir "$OUTPUT_DIR")"
info "Build output directory: $OUTPUT_DIR"

# ── Discover platforms ──────────────────────────────────────────────────────
discover_platforms() {
  local p
  for p in "$REPO_ROOT/adapters"/*/; do
    [[ -d "$p" ]] || continue
    basename "$p"
  done
}

# ── Build a single platform ─────────────────────────────────────────────────
build_one() {
  local platform="$1"
  local adapter="$REPO_ROOT/adapters/$platform/adapter.sh"

  [[ -f "$adapter" ]] || die "Adapter not found: $adapter"

  info "Building platform: $platform"

  # Source shared adapter helpers, then the platform-specific adapter.
  # shellcheck source=adapters/lib.sh
  source "$REPO_ROOT/adapters/lib.sh"
  # shellcheck source=/dev/null
  source "$adapter"

  local dist_dir="$OUTPUT_DIR/$platform"
  rm -rf "$dist_dir"
  mkdir -p "$dist_dir"

  adapter_build "$REPO_ROOT" "$dist_dir"
  # Credit ships inside the build, not only in adapters/OWNERS.md. Done here
  # rather than in each adapter so claiming a platform stays a one-line edit to
  # one table instead of a change to seven files.
  append_owner_credit "$dist_dir" "$platform"

  success "$platform → $dist_dir/"
}

# ── Validate exclude: tokens ────────────────────────────────────────────────
# `exclude:` is the only mechanism keeping a Claude-only command out of a
# platform where it cannot work, and it was an unvalidated string match. A
# plausible misspelling (codex for codex-cli, agentskills for agent-skills)
# shipped the command everywhere with exit 0 and no warning. The one command
# that relies on this today spells all six correctly by luck.
validate_excludes() (
  # Subshell + its own source: adapters/lib.sh is sourced inside build_one, so
  # parse_frontmatter is not available at this scope.
  source "$REPO_ROOT/adapters/lib.sh"
  local valid; valid=" $(discover_platforms | tr '\n' ' ')"
  local bad=0 f raw tok
  for f in "$REPO_ROOT"/commands/*.md; do
    [[ -f "$f" ]] || continue
    raw="$(parse_frontmatter "$f" exclude)"
    [[ -z "$raw" || "$raw" == "[]" ]] && continue
    for tok in $(echo "$raw" | tr -d '[]"' | tr ',' ' '); do
      [[ -z "$tok" ]] && continue
      case "$valid" in
        *" $tok "*) ;;
        *) echo "error: $(basename "$f") excludes unknown platform '$tok'" >&2
           echo "       valid platforms:$valid" >&2
           bad=1 ;;
      esac
    done
  done
  [[ $bad -eq 0 ]]
)
validate_excludes || exit 1

# ── Main ────────────────────────────────────────────────────────────────────
if [[ -n "$PLATFORM" ]]; then
  build_one "$PLATFORM"
else
  info "No --platform given; building all"
  for p in $(discover_platforms); do
    ( build_one "$p" )
  done
  success "All platforms built"
fi

# Never ship Python bytecode into user vaults (stress-test fix 22/24).
# Anchored to $OUTPUT_DIR, not the caller's cwd. scripts/update-vault-integration.sh
# invokes build.sh by absolute path with no cd, so `find dist ...` resolved against
# whatever directory the user was in, found nothing, and the `|| true` swallowed it -
# then install_build copied the bytecode straight into the user's vault.
find "$OUTPUT_DIR" -name "__pycache__" -type d -prune -exec rm -rf {} + 2>/dev/null || true
find "$OUTPUT_DIR" -name "*.pyc" -delete 2>/dev/null || true
