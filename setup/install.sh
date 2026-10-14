#!/usr/bin/env bash
# Install ALEXIS for Claude Code. Works on Linux, macOS and WSL2.
# Usage: bash setup/install.sh            -> core
#        bash setup/install.sh --full     -> core + platform plugins (Azure, Microsoft Docs, GitHub, dbt, Power BI, Databricks)
set -euo pipefail

REPO_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
FULL="${1:-}"

command -v claude >/dev/null 2>&1 || { echo "Claude Code is not installed: https://code.claude.com/docs" >&2; exit 1; }
command -v python3 >/dev/null 2>&1 || echo "Warning: python3 not found; safety and validation hooks will be disabled." >&2

add_marketplace() { claude plugin marketplace add "$1" >/dev/null 2>&1 && echo "  + marketplace $1" || echo "  (already added or unavailable: $1)"; }
install_plugin()  { claude plugin install "$1" >/dev/null 2>&1 && echo "  + plugin $1" || echo "  (already installed or unavailable: $1)"; }

echo "1/5 Marketplaces"
add_marketplace "$REPO_DIR"           # ALEXIS from this clone (do not move the folder afterwards)
add_marketplace obra/superpowers-marketplace
add_marketplace anthropics/knowledge-work-plugins
add_marketplace anthropics/skills

echo "2/5 Core plugins"
install_plugin alexis@alexis
install_plugin superpowers@superpowers-marketplace
install_plugin data@knowledge-work-plugins
install_plugin document-skills@anthropic-agent-skills

if [[ "$FULL" == "--full" ]]; then
  echo "3/5 Platform plugins"
  install_plugin azure@claude-plugins-official
  install_plugin microsoft-docs@claude-plugins-official
  install_plugin github@claude-plugins-official
  add_marketplace dbt-labs/dbt-agent-skills
  install_plugin dbt@dbt-agent-marketplace
  add_marketplace microsoft/skills-for-fabric
  install_plugin powerbi-authoring@fabric-collection
  if command -v databricks >/dev/null 2>&1; then
    databricks aitools install || echo "  (run 'databricks aitools install' manually)"
  else
    echo "  Databricks CLI not found: install it and run 'databricks aitools install'."
  fi
else
  echo "3/5 Platform plugins: skipped (use --full)"
fi

echo "4/5 Command-line tools (alexis-wt, alexis-goal, alexis-statusline)"
mkdir -p "$HOME/.local/bin"
for tool in alexis-wt alexis-goal alexis-statusline; do
  ln -sf "$REPO_DIR/tools/$tool" "$HOME/.local/bin/$tool"
done
case ":$PATH:" in *":$HOME/.local/bin:"*) ;; *) echo "  Add ~/.local/bin to your PATH (e.g. in ~/.bashrc)";; esac
python3 "$REPO_DIR/setup/configure_settings.py" || true

echo "5/5 User CLAUDE.md"
mkdir -p "$HOME/.claude"
if [[ -f "$HOME/.claude/CLAUDE.md" ]]; then
  echo "  ~/.claude/CLAUDE.md already exists: not overwritten. Compare with templates/user/CLAUDE.md."
else
  cp "$REPO_DIR/templates/user/CLAUDE.md" "$HOME/.claude/CLAUDE.md"
  echo "  Copied. Fill in the 'About me' section and ALEXIS_VAULT."
fi

echo "Done. Open Claude Code in an empty folder and type: /alexis:new-project <your idea>"
