---
name: create-srs
description: "Use when creating the initial Korean SRS or functional specification draft from multiple project sources."
---

# Create SRS Codex Adapter

Use the workspace workflow without duplicating its canonical instructions.

1. Read `.agents/skills/_shared/codex-runtime.md` completely.
2. Read `.claude/commands/create-srs.md` completely from the repository root before taking task actions.
3. Treat the payload supplied with `$create-srs` as the source command's `$ARGUMENTS`.
4. Resolve workspace paths from the repository root unless the source says otherwise.
5. Follow the source workflow, applying the runtime compatibility and safety rules first when host behavior differs.

- Source revision: `sha256:79c7c81948d34299f6b1e9431222d9b97d68df7aec9d727a36f93ee64bbb8ab2`
- Risk: `critical`
- Dependencies: notion-cigro
