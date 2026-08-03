---
name: kickoff-prep
description: "Use when preparing a bilingual kickoff agenda, questions, glossary, and internal meeting preparation from an SRS."
---

# Kickoff Prep Codex Adapter

Use the workspace workflow without duplicating its canonical instructions.

1. Read `.agents/skills/_shared/codex-runtime.md` completely.
2. Read `.claude/commands/kickoff-prep.md` completely from the repository root before taking task actions.
3. Treat the payload supplied with `$kickoff-prep` as the source command's `$ARGUMENTS`.
4. Resolve workspace paths from the repository root unless the source says otherwise.
5. Follow the source workflow, applying the runtime compatibility and safety rules first when host behavior differs.

- Source revision: `sha256:75efa0c475dec244c9cb946e44c1d665d6972bbf6fd4fb4bb686b485b6d7ba55`
- Risk: `critical`
- Dependencies: notion-cigro
