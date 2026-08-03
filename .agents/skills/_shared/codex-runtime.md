# Codex Runtime Compatibility

Apply these rules before following a workspace Claude command through a Codex adapter.

## Source and arguments

1. Resolve every adapter source from the repository root and read it completely before acting.
2. Treat `$ARGUMENTS` in a Claude command as the text supplied with the current `$skill-name` request. Never perform literal shell interpolation.
3. Resolve relative references in the source from the source file's directory when they are bundled skill resources; resolve workspace paths such as `clients/`, `glossary/`, and `templates/` from the repository root.
4. Preserve the source's business rules, output structure, terminology, and confirmation choices. Apply this file only as the host compatibility and safety layer.

## Tool translation

- Translate `Read`, `Glob`, `Grep`, `Write`, `Edit`, and `Bash` to the available Codex file and shell tools. Use `rg` for file or text search and `apply_patch` for hand-authored workspace edits.
- Select MCP tools by semantic operation and server, not by blindly copying a Claude tool identifier. Codex normalizes server and tool names, and Notion may expose `fetch` and `search` without the `notion-` prefix.
- Before a workflow that depends on Notion, Linear, Nexus, Google Workspace, or Playwright, verify that the required server and operation are callable. If not, stop and name the missing dependency.
- A missing MCP operation is not permission to fall back to a direct REST write, invent an external ID, or claim success.

## External writes and confirmation

- Never bypass a PM Confirm Gate. Critical, High, and Low send workflows must show their complete preview and receive the source-defined numbered approval immediately before any Notion, Linear, Nexus, Teams, deployment, or other external write.
- Cancellation, defer, copy-only, and modification choices must not perform the external write.
- Treat `kickoff-prep` as requiring a new confirmation gate before its Notion write even though the legacy source does not yet contain one.
- Treat `today-brief` as High risk because its schema synchronization can update Notion. Require confirmation before that update; if declined, skip the schema write and continue only with read-only briefing behavior when possible.
- For Teams timeouts, do not retry automatically because the original request may already have been delivered.
- Report external success only from a successful tool response or the source's exact verified success condition.

## Credentials and local state

- Do not copy credentials, OAuth tokens, MCP authorization headers, webhook URLs, chat IDs, or `.env` values into skills, generated files, fixtures, logs, or responses.
- Read secret values only at the moment an approved workflow requires them and avoid printing them.
- Preserve unrelated dirty-worktree changes. Do not edit canonical `.claude/commands` from a generated Codex adapter.
