# Owner Usage Guide

Use this guide if you own the private Handshake AI skills repo and have write access.

## Golden Rule

The GitHub repo is the source of truth. Make Handshake skill changes in the canonical repo, then commit and push them.

Private GitHub repo:

```text
https://github.com/chiizzy1/handshake-ai-skills
```

## Daily Workflow

Before editing, pull the latest version:

```powershell
git -C "C:\Users\$env:USERNAME\Desktop\projects\train-ai\handshake-ai-skills" pull --ff-only
```

Edit the skill files in the canonical repo folder.

Check what changed:

```powershell
git -C "C:\Users\$env:USERNAME\Desktop\projects\train-ai\handshake-ai-skills" status
git -C "C:\Users\$env:USERNAME\Desktop\projects\train-ai\handshake-ai-skills" diff
```

Commit and push:

```powershell
git -C "C:\Users\$env:USERNAME\Desktop\projects\train-ai\handshake-ai-skills" add .
git -C "C:\Users\$env:USERNAME\Desktop\projects\train-ai\handshake-ai-skills" commit -m "Improve Handshake skill guidance"
git -C "C:\Users\$env:USERNAME\Desktop\projects\train-ai\handshake-ai-skills" push
```

## Agent Setup

Use junction links so each agent reads this canonical repo instead of stale copied folders.

```powershell
.\scripts\link-windows.ps1 -Target Agents
.\scripts\link-windows.ps1 -Target Codex
.\scripts\link-windows.ps1 -Target Gemini
```

Use `-Force` only when you intentionally want to replace an existing copied skill folder with a junction. The script backs up existing folders before linking.

## What Not To Do

Do not keep manually copying skill folders between agents.

Do not treat these paths as separate sources of truth:

```text
C:\Users\$env:USERNAME\.agents\skills
C:\Users\$env:USERNAME\.codex\skills
C:\Users\$env:USERNAME\.gemini\antigravity-ide\skills
```

After linking, those folders should point back to this canonical repo.

## Token Safety

Do not commit tokens, API keys, `.env`, or `local.env` files.
