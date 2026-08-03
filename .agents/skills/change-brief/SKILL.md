---
name: change-brief
description: "Use when a legacy change-brief command is invoked and the request should be routed through the current to-spec change-triage workflow."
---

# Change Brief Compatibility Alias

This adapter preserves an old command name without running the deprecated workflow.

1. Read `.agents/skills/_shared/codex-runtime.md` completely.
2. Treat the current request payload as arguments for `$to-spec`.
3. Read `.agents/skills/to-spec/SKILL.md` completely and follow it.
4. Tell the user that `$change-brief` was routed to `$to-spec`; do not execute `.claude/commands/change-brief.md`.

- Source record: `.claude/commands/change-brief.md`
- Source revision: `sha256:50d6af111a1a755a4b211a6204baf739fc5e50ec862f4185119412cd994f13f5`
- Risk: `deprecated`
- Dependencies: none
