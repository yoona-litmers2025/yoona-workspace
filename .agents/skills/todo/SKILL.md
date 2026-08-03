---
name: todo
description: "Use when adding a PM action to Nexus Todo and the Notion PM Action Hub backup."
---

# PM Todo Codex Adapter

Use the workspace workflow without duplicating its canonical instructions.

1. Read `.agents/skills/_shared/codex-runtime.md` completely.
2. Read `.claude/commands/todo.md` completely from the repository root before taking task actions.
3. Treat the payload supplied with `$todo` as the source command's `$ARGUMENTS`.
4. Resolve workspace paths from the repository root unless the source says otherwise.
5. Follow the source workflow, applying the runtime compatibility and safety rules first when host behavior differs.

- Source revision: `sha256:c66ce6b73ff7ad641284a3d626f0a9f3a45b2c7842c0d3e6bc6056724c797dff`
- Risk: `high`
- Dependencies: notion-cigro, nexus-os
