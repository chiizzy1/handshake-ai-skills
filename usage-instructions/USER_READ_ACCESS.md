# Read-Only User Guide

Use this guide if you have read access to the private Handshake AI skills repo.

## What You Can Do

You can clone the private repo, pull updates from the owner, link your agent skill folders to your local clone, and use the skills for Handshake task work.

You cannot push changes to the official skill source unless the owner gives you write access.

## First-Time Setup

Accept the GitHub repository invite from the owner.

Clone the repo:

```powershell
New-Item -ItemType Directory -Path "C:\Users\$env:USERNAME\skills-source" -Force
git clone https://github.com/chiizzy1/handshake-ai-skills.git "C:\Users\$env:USERNAME\skills-source\handshake-ai-skills"
```

Open the repo:

```powershell
cd "C:\Users\$env:USERNAME\skills-source\handshake-ai-skills"
```

## Link Your Agent Skills

Run these from the cloned repo folder:

```powershell
.\scripts\link-windows.ps1 -Target Agents
.\scripts\link-windows.ps1 -Target Codex
.\scripts\link-windows.ps1 -Target Gemini
```

Use `-Force` only if you are replacing existing copied skill folders:

```powershell
.\scripts\link-windows.ps1 -Target Agents -Force
.\scripts\link-windows.ps1 -Target Codex -Force
.\scripts\link-windows.ps1 -Target Gemini -Force
```

Restart the agent after linking so it can discover the skills.

## Daily Update

Before Handshake work, pull the latest owner-approved version:

```powershell
git -C "C:\Users\$env:USERNAME\skills-source\handshake-ai-skills" pull --ff-only
```

Or run:

```powershell
.\scripts\update.ps1
```

Restart the agent if the update changed skill files.
