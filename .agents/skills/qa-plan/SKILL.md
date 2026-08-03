---
name: qa-plan
description: "Use when creating an English internal QA plan from project scope, SRS, briefs, or a staging URL."
---

# QA Plan Codex Adapter

Use the workspace workflow without duplicating its canonical instructions.

1. Read `.agents/skills/_shared/codex-runtime.md` completely.
2. Read `.claude/commands/qa-plan.md` completely from the repository root before taking task actions.
3. Treat the payload supplied with `$qa-plan` as the source command's `$ARGUMENTS`.
4. Resolve workspace paths from the repository root unless the source says otherwise.
5. Follow the source workflow, applying the runtime compatibility and safety rules first when host behavior differs.

- Source revision: `sha256:a7b8c89843e0595c4b65a9a81b7e5d59ee0bfc4d8800e78e28113118f68fb5b6`
- Risk: `medium`
- Dependencies: notion-cigro, playwright
