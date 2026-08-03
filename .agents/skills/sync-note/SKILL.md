---
name: sync-note
description: "Use when turning an internal sync meeting into a concise English Teams follow-up for the development team."
---

# Sync Note Codex Adapter

Use the workspace workflow without duplicating its canonical instructions.

1. Read `.agents/skills/_shared/codex-runtime.md` completely.
2. Read `.claude/commands/sync-note.md` completely from the repository root before taking task actions.
3. Treat the payload supplied with `$sync-note` as the source command's `$ARGUMENTS`.
4. Resolve workspace paths from the repository root unless the source says otherwise.
5. Follow the source workflow, applying the runtime compatibility and safety rules first when host behavior differs.

- Source revision: `sha256:d0735e8d6a658f30213ea1f95ffff4a6948158d5d241804b4e2830127a9d6613`
- Risk: `low`
- Dependencies: teams-flow
