---
name: qa-request
description: "Use when drafting a Korean client QA or review request containing links, accounts, files, and testing guidance."
---

# QA Request Codex Adapter

Use the workspace workflow without duplicating its canonical instructions.

1. Read `.agents/skills/_shared/codex-runtime.md` completely.
2. Read `.claude/commands/qa-request.md` completely from the repository root before taking task actions.
3. Treat the payload supplied with `$qa-request` as the source command's `$ARGUMENTS`.
4. Resolve workspace paths from the repository root unless the source says otherwise.
5. Follow the source workflow, applying the runtime compatibility and safety rules first when host behavior differs.

- Source revision: `sha256:de108988bc6585ac86911b242b60f05964f6768f282b6bc93db66839025acb11`
- Risk: `read-only`
- Dependencies: none
