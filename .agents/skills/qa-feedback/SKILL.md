---
name: qa-feedback
description: "Use when a legacy qa-feedback command is invoked and the request should be routed through the current qa-update intake workflow."
---

# QA Feedback Compatibility Alias

This adapter preserves an old command name without running the deprecated workflow.

1. Read `.agents/skills/_shared/codex-runtime.md` completely.
2. Treat the current request payload as arguments for `$qa-update`.
3. Read `.agents/skills/qa-update/SKILL.md` completely and follow it.
4. Tell the user that `$qa-feedback` was routed to `$qa-update`; do not execute `.claude/commands/qa-feedback.md`.

- Source record: `.claude/commands/qa-feedback.md`
- Source revision: `sha256:85e4636954068a0e2f0deaff3c3d932c1ca67a05f94742be452d6e7586937836`
- Risk: `deprecated`
- Dependencies: none
