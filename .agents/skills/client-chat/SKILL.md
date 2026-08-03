---
name: client-chat
description: "Use when converting a developer message, technical update, or question into a polished Korean client chat message."
---

# Client Chat Codex Adapter

Use the workspace workflow without duplicating its canonical instructions.

1. Read `.agents/skills/_shared/codex-runtime.md` completely.
2. Read `.claude/commands/client-chat.md` completely from the repository root before taking task actions.
3. Treat the payload supplied with `$client-chat` as the source command's `$ARGUMENTS`.
4. Resolve workspace paths from the repository root unless the source says otherwise.
5. Follow the source workflow, applying the runtime compatibility and safety rules first when host behavior differs.

- Source revision: `sha256:f64f02451c9a5156f14da603375a3a50c6f892bd7ea0eb37cb1d8ab1f9a04185`
- Risk: `read-only`
- Dependencies: none
