---
name: nexus-daily
description: "Use when recording daily hours and work notes against existing Nexus OS project tasks."
---

# Nexus Daily Codex Adapter

Use the workspace workflow without duplicating its canonical instructions.

1. Read `.agents/skills/_shared/codex-runtime.md` completely.
2. Read `.claude/commands/nexus-daily.md` completely from the repository root before taking task actions.
3. Treat the payload supplied with `$nexus-daily` as the source command's `$ARGUMENTS`.
4. Resolve workspace paths from the repository root unless the source says otherwise.
5. Follow the source workflow, applying the runtime compatibility and safety rules first when host behavior differs.

- Source revision: `sha256:becb94bb407a406b9545776e9f0101fd8bef816b42bb549231a5e3fe899764a8`
- Risk: `critical`
- Dependencies: notion-cigro, nexus-os
