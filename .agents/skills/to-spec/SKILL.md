---
name: to-spec
description: "Use when triaging an in-flight client change into scope buckets and writing confirmed in-round specification and task updates."
---

# To Spec Codex Adapter

Use the workspace workflow without duplicating its canonical instructions.

1. Read `.agents/skills/_shared/codex-runtime.md` completely.
2. Read `.claude/commands/to-spec.md` completely from the repository root before taking task actions.
3. Treat the payload supplied with `$to-spec` as the source command's `$ARGUMENTS`.
4. Resolve workspace paths from the repository root unless the source says otherwise.
5. Follow the source workflow, applying the runtime compatibility and safety rules first when host behavior differs.

- Source revision: `sha256:8895afd4e79b4e604fd68873a4177fa35ebbce41ca33967da3ddc9bf4f482358`
- Risk: `critical`
- Dependencies: notion-cigro
