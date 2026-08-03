---
name: new-project
description: "Use when onboarding a new client project into the local PM workspace and its required Notion databases and views."
---

# New Project Codex Adapter

Use the workspace workflow without duplicating its canonical instructions.

1. Read `.agents/skills/_shared/codex-runtime.md` completely.
2. Read `.claude/commands/new-project.md` completely from the repository root before taking task actions.
3. Treat the payload supplied with `$new-project` as the source command's `$ARGUMENTS`.
4. Resolve workspace paths from the repository root unless the source says otherwise.
5. Follow the source workflow, applying the runtime compatibility and safety rules first when host behavior differs.

- Source revision: `sha256:ae1646fc67e20e330e68d36eee895da43bd28dda3b980880d6130d57a4b8c6e7`
- Risk: `high`
- Dependencies: notion-cigro
