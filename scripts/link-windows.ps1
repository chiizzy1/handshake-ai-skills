param(
    [ValidateSet("Agents", "Codex", "Gemini", "Project")]
    [string]$Target,

    [string]$RepoRoot = (Resolve-Path (Join-Path $PSScriptRoot "..")).Path,

    [string]$ProjectSkillsRoot = "",

    [switch]$Force
)

$skillDirs = Get-ChildItem -LiteralPath $RepoRoot -Directory |
    Where-Object { Test-Path -LiteralPath (Join-Path $_.FullName "SKILL.md") } |
    Sort-Object Name

if (!$skillDirs) {
    throw "No skill folders with SKILL.md found in $RepoRoot"
}

switch ($Target) {
    "Agents" { $destRoot = Join-Path $env:USERPROFILE ".agents\skills" }
    "Codex" { $destRoot = Join-Path $env:USERPROFILE ".codex\skills" }
    "Gemini" { $destRoot = Join-Path $env:USERPROFILE ".gemini\antigravity-ide\skills" }
    "Project" {
        if ([string]::IsNullOrWhiteSpace($ProjectSkillsRoot)) {
            throw "Project target requires -ProjectSkillsRoot"
        }
        $destRoot = $ProjectSkillsRoot
    }
}

New-Item -ItemType Directory -Path $destRoot -Force | Out-Null
$backupRoot = Join-Path $destRoot ("_backup_before_junction_" + (Get-Date -Format "yyyyMMdd-HHmmss"))

foreach ($skillDir in $skillDirs) {
    $source = $skillDir.FullName
    $dest = Join-Path $destRoot $skillDir.Name

    if (Test-Path -LiteralPath $dest) {
        $item = Get-Item -LiteralPath $dest
        $resolvedDest = (Resolve-Path -LiteralPath $dest).Path

        if ($item.LinkType -eq "Junction" -and $item.Target -contains $source) {
            Write-Host "Already linked $dest -> $source"
            continue
        }

        if (!$Force) {
            Write-Host "Skipping existing path: $dest"
            continue
        }

        if ($resolvedDest -notlike "$destRoot*") {
            throw "Refusing to move path outside destination root: $resolvedDest"
        }

        New-Item -ItemType Directory -Path $backupRoot -Force | Out-Null
        $backupDest = Join-Path $backupRoot $skillDir.Name
        Move-Item -LiteralPath $dest -Destination $backupDest
        Write-Host "Backed up $dest -> $backupDest"
    }

    New-Item -ItemType Junction -Path $dest -Target $source | Out-Null
    Write-Host "Linked $dest -> $source"
}
