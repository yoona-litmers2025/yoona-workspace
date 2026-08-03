---
name: qa-update
description: "Use when synchronizing customer QA rows with internal English tickets or moving ready items back to client review."
---

# QA Update Codex Adapter

Use the workspace workflow without duplicating its canonical instructions.

1. Read `.agents/skills/_shared/codex-runtime.md` completely.
2. Read `.claude/commands/qa-update.md` completely from the repository root before taking task actions.
3. Treat the payload supplied with `$qa-update` as the source command's `$ARGUMENTS`.
4. Resolve workspace paths from the repository root unless the source says otherwise.
5. Follow the source workflow, applying the runtime compatibility and safety rules first when host behavior differs.

- Source revision: `sha256:fa622924ab7a9a094a06e3af7560afdff68c46988cc241de67476e7e60cd3975`
- Risk: `critical`
- Dependencies: notion-cigro
