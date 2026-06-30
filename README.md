# Handshake AI Skills

Canonical private repository for Handshake AI evaluator skills.

## Source Of Truth

Edit Handshake skills here, then commit and push. Do not manually edit copied skill folders inside agent-specific directories.

Included skills:

- `handshake-evaluator`
- `handshake-annot-critic`
- `handshake-critique-rework`
- `handshake-ego-phys-understanding`
- `handshake-find-boundary`
- `handshake-h2h-image-evaluator`
- `handshake-i2i-pixel-aligned`
- `handshake-ig-entity-tagging`
- `handshake-ig-entity-verification`
- `handshake-r2i-i2i-evaluator`
- `handshake-static-webpage`
- `handshake-text-to-code-elo-evaluator`
- `handshake-ti2t-evaluator`
- `handshake-ud-caption-evaluator`

## Daily Update

Users with read access should update before Handshake task work:

```powershell
git -C "C:\Users\$env:USERNAME\skills-source\handshake-ai-skills" pull --ff-only
```

Or run:

```powershell
.\scripts\update.ps1
```

## Read-Only Setup

For friends or users who should only install and update the skills, send them:

```text
usage-instructions/USER_READ_ACCESS.md
```

They should clone this full repo, link their agent skill folders to it, and pull updates. They should not edit local skill files.

## Windows Agent Links

Use junctions so Codex, Gemini/Antigravity, shared agent skills, and project-local skill folders all point to this one repo.

```powershell
.\scripts\link-windows.ps1 -Target Agents
.\scripts\link-windows.ps1 -Target Codex
.\scripts\link-windows.ps1 -Target Gemini
```

Use `-Force` only when you intentionally want to replace existing copied skill folders with junctions. Existing folders are moved to a timestamped backup folder.

## Access Model

- Owner: write access.
- Friends/users: read access.
- Contributors should propose changes separately; only the owner updates this canonical repo.

Keep this repository private if it contains platform-specific or confidential guideline material.
