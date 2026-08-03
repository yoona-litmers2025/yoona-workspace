---
name: today-brief
description: "Use when preparing the PM's daily brief from current action items, project activity, and calendar context."
---

# Today Brief Codex Adapter

Use the workspace workflow without duplicating its canonical instructions.

1. Read `.agents/skills/_shared/codex-runtime.md` completely.
2. Read `.claude/commands/today-brief.md` completely from the repository root before taking task actions.
3. Treat the payload supplied with `$today-brief` as the source command's `$ARGUMENTS`.
4. Resolve workspace paths from the repository root unless the source says otherwise.
5. Follow the source workflow, applying the runtime compatibility and safety rules first when host behavior differs.

- Source revision: `sha256:400ee3b4a84fd338ddfa5d9c3e49438eaa28617ba9ddb1ff72fdfe05f660da73`
- Risk: `high`
- Dependencies: notion-cigro, google-workspace
