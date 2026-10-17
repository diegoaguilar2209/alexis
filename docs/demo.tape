# Terminal demo for the README, recorded with VHS (https://github.com/charmbracelet/vhs).
# Render: vhs docs/demo.tape   -> docs/demo.gif
# The demo runs a real Claude Code session, so it needs Claude Code installed and logged in.
Output docs/demo.gif
Set Shell "bash"
Set FontSize 16
Set Width 1200
Set Height 720
Set Theme "Catppuccin Mocha"
Set TypingSpeed 40ms

Type "mkdir churn-demo && cd churn-demo && git init -q && claude"
Enter
Sleep 4s
Type "/alexis:new-project Daily churn pipeline from Postgres to Databricks with a Power BI view for retention leads"
Enter
Sleep 25s
Type "Assume: KPI churn 4.1% to 3.5% in Q1, users are retention leads, 2M rows/day, deliverable in 4 weeks. Write the spec and plan."
Enter
Sleep 60s
Ctrl+C
Sleep 1s
