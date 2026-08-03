---
name: srs-translate
description: "Use when translating and restructuring a Korean SRS into concise English requirements for developers and designers."
---

# SRS Translate Codex Adapter

Use the workspace workflow without duplicating its canonical instructions.

1. Read `.agents/skills/_shared/codex-runtime.md` completely.
2. Read `.claude/commands/srs-translate.md` completely from the repository root before taking task actions.
3. Treat the payload supplied with `$srs-translate` as the source command's `$ARGUMENTS`.
4. Resolve workspace paths from the repository root unless the source says otherwise.
5. Follow the source workflow, applying the runtime compatibility and safety rules first when host behavior differs.

- Source revision: `sha256:856df99376f3d92f88142c6fd2998bcb6abf227a6661f4d5317584e266d79f0a`
- Risk: `critical`
- Dependencies: notion-cigro
