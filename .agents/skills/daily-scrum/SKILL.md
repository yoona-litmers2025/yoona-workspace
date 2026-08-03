---
name: daily-scrum
description: "Use when preparing a project daily scrum log, PM action updates, and an English developer-team status message."
---

# Daily Scrum Codex Adapter

Use the workspace workflow without duplicating its canonical instructions.

1. Read `.agents/skills/_shared/codex-runtime.md` completely.
2. Read `.claude/commands/daily-scrum.md` completely from the repository root before taking task actions.
3. Treat the payload supplied with `$daily-scrum` as the source command's `$ARGUMENTS`.
4. Resolve workspace paths from the repository root unless the source says otherwise.
5. Follow the source workflow, applying the runtime compatibility and safety rules first when host behavior differs.

- Source revision: `sha256:c1950b22a4416b46b3a81785f3daf525a9ab59f1782ad704084dd2645a066a1f`
- Risk: `critical`
- Dependencies: notion-cigro, teams-flow
