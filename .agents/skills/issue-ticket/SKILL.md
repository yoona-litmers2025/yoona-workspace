---
name: issue-ticket
description: "Use when converting a confirmed request or bug into an English Linear issue with acceptance criteria and priority."
---

# Issue Ticket Codex Adapter

Use the workspace workflow without duplicating its canonical instructions.

1. Read `.agents/skills/_shared/codex-runtime.md` completely.
2. Read `.claude/commands/issue-ticket.md` completely from the repository root before taking task actions.
3. Treat the payload supplied with `$issue-ticket` as the source command's `$ARGUMENTS`.
4. Resolve workspace paths from the repository root unless the source says otherwise.
5. Follow the source workflow, applying the runtime compatibility and safety rules first when host behavior differs.

- Source revision: `sha256:37093d44f8d30d0f4e4ee802ab93e91a27e9fdf1b4863991fc4c6da68fefeb3b`
- Risk: `critical`
- Dependencies: linear
