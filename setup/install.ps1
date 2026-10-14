# Install ALEXIS for Claude Code on native Windows (PowerShell).
# On Windows the recommended setup is WSL2 + setup/install.sh. Use this script for a
# Windows-side session, e.g. to use the Power BI Modeling MCP (Power BI Desktop is Windows-only).
# Usage: .\setup\install.ps1          -> core
#        .\setup\install.ps1 -Full    -> core + platform plugins
param([switch]$Full)

$RepoDir = Split-Path -Parent $PSScriptRoot

if (-not (Get-Command claude -ErrorAction SilentlyContinue)) {
  Write-Error "Claude Code is not installed: https://code.claude.com/docs"
  exit 1
}

function Add-Marketplace($src) { claude plugin marketplace add $src | Out-Null; if ($LASTEXITCODE -ne 0) { Write-Host "  (already added or unavailable: $src)" } else { Write-Host "  + marketplace $src" } }
function Install-Plugin($p)    { claude plugin install $p | Out-Null;          if ($LASTEXITCODE -ne 0) { Write-Host "  (already installed or unavailable: $p)" } else { Write-Host "  + plugin $p" } }

Write-Host "1/3 Marketplaces"
Add-Marketplace $RepoDir
Add-Marketplace "obra/superpowers-marketplace"
Add-Marketplace "anthropics/knowledge-work-plugins"
Add-Marketplace "anthropics/skills"

Write-Host "2/3 Core plugins"
Install-Plugin "alexis@alexis"
Install-Plugin "superpowers@superpowers-marketplace"
Install-Plugin "data@knowledge-work-plugins"
Install-Plugin "document-skills@anthropic-agent-skills"

if ($Full) {
  Write-Host "3/3 Platform plugins"
  Install-Plugin "azure@claude-plugins-official"
  Install-Plugin "microsoft-docs@claude-plugins-official"
  Add-Marketplace "microsoft/skills-for-fabric"
  Install-Plugin "powerbi-authoring@fabric-collection"
} else {
  Write-Host "3/3 Platform plugins: skipped (use -Full)"
}

$Target = Join-Path (Join-Path $HOME ".claude") "CLAUDE.md"
if (-not (Test-Path $Target)) {
  New-Item -ItemType Directory -Force -Path (Split-Path $Target) | Out-Null
  Copy-Item (Join-Path $RepoDir "templates/user/CLAUDE.md") $Target
  Write-Host "Copied templates/user/CLAUDE.md to ~/.claude/CLAUDE.md. Fill in 'About me'."
}
Write-Host "Done. Note: the status line and alexis-* tools need bash (use WSL2)."
