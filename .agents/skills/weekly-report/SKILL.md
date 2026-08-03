---
name: weekly-report
description: "Use when preparing and saving a Korean client-facing weekly project report."
---

# Weekly Report Codex Adapter

Use the workspace workflow without duplicating its canonical instructions.

1. Read `.agents/skills/_shared/codex-runtime.md` completely.
2. Read `.claude/commands/weekly-report.md` completely from the repository root before taking task actions.
3. Treat the payload supplied with `$weekly-report` as the source command's `$ARGUMENTS`.
4. Resolve workspace paths from the repository root unless the source says otherwise.
5. Follow the source workflow, applying the runtime compatibility and safety rules first when host behavior differs.

- Source revision: `sha256:846064df1b87ce5f0d48db40f1d3171b1133e0fb4750494f46faa71880dbbffc`
- Risk: `critical`
- Dependencies: notion-cigro
