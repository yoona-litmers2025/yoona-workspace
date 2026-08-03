---
name: dev-chat
description: "Use when turning a Korean client request, PM decision, or meeting follow-up into an English Teams message for developers."
---

# Dev Chat Codex Adapter

Use the workspace workflow without duplicating its canonical instructions.

1. Read `.agents/skills/_shared/codex-runtime.md` completely.
2. Read `.claude/commands/dev-chat.md` completely from the repository root before taking task actions.
3. Treat the payload supplied with `$dev-chat` as the source command's `$ARGUMENTS`.
4. Resolve workspace paths from the repository root unless the source says otherwise.
5. Follow the source workflow, applying the runtime compatibility and safety rules first when host behavior differs.

- Source revision: `sha256:4851d697f14bfa169dc9200e2d3fbe6fe113d19e8b4023f4a7342d2cdf0b0089`
- Risk: `low`
- Dependencies: teams-flow
