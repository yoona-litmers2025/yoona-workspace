---
name: meeting-note
description: "Use when converting meeting notes or a transcript into a Notion meeting record plus developer and client messages."
---

# Meeting Note Codex Adapter

Use the workspace workflow without duplicating its canonical instructions.

1. Read `.agents/skills/_shared/codex-runtime.md` completely.
2. Read `.claude/commands/meeting-note.md` completely from the repository root before taking task actions.
3. Treat the payload supplied with `$meeting-note` as the source command's `$ARGUMENTS`.
4. Resolve workspace paths from the repository root unless the source says otherwise.
5. Follow the source workflow, applying the runtime compatibility and safety rules first when host behavior differs.

- Source revision: `sha256:83c14791835d9311d5faed97152b749555000571fdb80e72d2a1ac89be24a884`
- Risk: `critical`
- Dependencies: notion-cigro
