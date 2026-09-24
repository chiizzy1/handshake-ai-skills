#!/usr/bin/env bash
# macOS/Linux counterpart of link-windows.ps1.
# Creates symlinks from agent skill folders back to this canonical repo clone.
#
# Usage:
#   ./scripts/link-macos.sh --target agents|codex|gemini|project [--project-skills-root <path>] [--repo-root <path>] [--force]

set -euo pipefail

TARGET=""
REPO_ROOT=""
PROJECT_SKILLS_ROOT=""
FORCE=0

usage() {
  echo "Usage: $0 --target agents|codex|gemini|project [--project-skills-root <path>] [--repo-root <path>] [--force]" >&2
  exit 1
}

while [[ $# -gt 0 ]]; do
  case "$1" in
    --target) TARGET="${2:-}"; shift 2 ;;
    --repo-root) REPO_ROOT="${2:-}"; shift 2 ;;
    --project-skills-root) PROJECT_SKILLS_ROOT="${2:-}"; shift 2 ;;
    --force) FORCE=1; shift ;;
    -h|--help) usage ;;
    *) echo "Unknown argument: $1" >&2; usage ;;
  esac
done

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
if [[ -z "$REPO_ROOT" ]]; then
  REPO_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
else
  REPO_ROOT="$(cd "$REPO_ROOT" && pwd)"
fi

case "$TARGET" in
  agents) DEST_ROOT="$HOME/.agents/skills" ;;
  codex) DEST_ROOT="$HOME/.codex/skills" ;;
  gemini) DEST_ROOT="$HOME/.gemini/antigravity-ide/skills" ;;
  project)
    if [[ -z "$PROJECT_SKILLS_ROOT" ]]; then
      echo "project target requires --project-skills-root" >&2
      exit 1
    fi
    DEST_ROOT="$PROJECT_SKILLS_ROOT"
    ;;
  *) usage ;;
esac

skill_dirs=()
# Root-level skills (e.g. handshake-evaluator)
for dir in "$REPO_ROOT"/*/; do
  [[ -f "$dir/SKILL.md" ]] && skill_dirs+=("${dir%/}")
done
# Project-level skills (e.g. project-hedgehog/handshake-*)
for pdir in "$REPO_ROOT"/project-*/; do
  [[ -d "$pdir" ]] || continue
  for dir in "$pdir"/*/; do
    [[ -f "$dir/SKILL.md" ]] && skill_dirs+=("${dir%/}")
  done
done

if [[ ${#skill_dirs[@]} -eq 0 ]]; then
  echo "No skill folders with SKILL.md found in $REPO_ROOT" >&2
  exit 1
fi

# Collision detection: abort if two skills resolve to the same basename.
_collision_list=""
for source in "${skill_dirs[@]}"; do
  name="$(basename "$source")"
  _prev="$(echo "$_collision_list" | grep "^$name|" || true)"
  if [[ -n "$_prev" ]]; then
    echo "COLLISION: skill name '$name' found in both:" >&2
    echo "  ${_prev#*|}" >&2
    echo "  $source" >&2
    echo "Fix the conflict before linking." >&2
    exit 1
  fi
  _collision_list="$_collision_list
$name|$source"
done

mkdir -p "$DEST_ROOT"
DEST_ROOT="$(cd "$DEST_ROOT" && pwd)"
BACKUP_ROOT="$DEST_ROOT/_backup_before_junction_$(date +%Y%m%d-%H%M%S)"

# Moves an existing dest entry into the timestamped backup folder,
# refusing to touch anything that resolves outside the destination root.
backup_path() {
  local path="$1" backup_name="$2"
  case "$path" in
    "$DEST_ROOT"/*) ;;
    *) echo "Refusing to move path outside destination root: $path" >&2; exit 1 ;;
  esac
  mkdir -p "$BACKUP_ROOT"
  mv "$path" "$BACKUP_ROOT/$backup_name"
  echo "Backed up $path -> $BACKUP_ROOT/$backup_name"
}

for source in "${skill_dirs[@]}"; do
  name="$(basename "$source")"
  dest="$DEST_ROOT/$name"
  legacy_dest="$DEST_ROOT/ai-training-$name"

  if [[ "$legacy_dest" != "$dest" && ( -e "$legacy_dest" || -L "$legacy_dest" ) ]]; then
    if [[ -L "$legacy_dest" && "$(readlink "$legacy_dest")" == "$source" ]]; then
      echo "Legacy path already linked $legacy_dest -> $source"
    elif [[ $FORCE -eq 1 ]]; then
      backup_path "$legacy_dest" "ai-training-$name"
    else
      echo "Legacy path exists, use --force to back it up: $legacy_dest"
    fi
  fi

  if [[ -e "$dest" || -L "$dest" ]]; then
    if [[ -L "$dest" && "$(readlink "$dest")" == "$source" ]]; then
      echo "Already linked $dest -> $source"
      continue
    fi
    if [[ $FORCE -ne 1 ]]; then
      echo "Skipping existing path: $dest"
      continue
    fi
    backup_path "$dest" "$name"
  fi

  ln -s "$source" "$dest"
  echo "Linked $dest -> $source"
done
