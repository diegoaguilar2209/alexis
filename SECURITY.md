# Security

## Reporting a vulnerability
Please do not open a public issue. Use GitHub's private vulnerability reporting ("Security" tab → "Report a vulnerability").

## What ALEXIS does and does not protect
- Skills, hooks and plugins run with your permissions. Review anything you install, including this repo.
- The safety hook matches text patterns. It catches common destructive commands (DROP, TRUNCATE, DELETE/UPDATE without WHERE, prod deploys, force push, cloud deletions), not every possible one.
- The project template's permission rules are enforced deterministically by Claude Code.
- The real protection is credentials: give Claude Code read-only identities and development catalogs, never production write access.
- `ALEXIS_ALLOW_DESTRUCTIVE=1` disables the safety hook for one session. Only a human should set it.
