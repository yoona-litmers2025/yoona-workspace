---
name: setup-workspace
description: "Use when initializing a PM workspace, creating the five required Notion databases, and configuring the local workspace IDs."
---

# Setup Workspace Codex Adapter

Use the workspace workflow without duplicating its canonical instructions.

1. Read `.agents/skills/_shared/codex-runtime.md` completely.
2. Read `.claude/commands/setup-workspace.md` completely from the repository root before taking task actions.
3. Treat the payload supplied with `$setup-workspace` as the source command's `$ARGUMENTS`.
4. Resolve workspace paths from the repository root unless the source says otherwise.
5. Follow the source workflow, applying the runtime compatibility and safety rules first when host behavior differs.

- Source revision: `sha256:96462a3670002cfea5b6499bafebbdb2ba21a92ce10aa07ccb91b1c5e3d0b394`
- Risk: `high`
- Dependencies: notion-cigro
