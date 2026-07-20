---
verified_on: 2026-07-18
status: "untested-as-skill: syntax-checked against the current SKILL.md frontmatter format only; not run end-to-end"
sources:
  - https://code.claude.com/docs/en/skills
  - https://platform.claude.com/docs/en/build-with-claude/prompt-caching
---

# `/cache-hygiene-audit`: check a setup before you commit it

**TL;DR:** a companion to [`cost-review.md`](cost-review.md): where that skill audits *usage data after the fact*, this one audits a `CLAUDE.md`/`settings.json` diff *before* it ships, for edits that silently break the prompt cache. Same caveat: syntax-checked against the current frontmatter format, not run end-to-end.

## Install

Save the block below as `.claude/skills/cache-hygiene-audit/SKILL.md`.

```markdown
---
name: cache-hygiene-audit
description: Check a CLAUDE.md or settings.json change for cache-invalidating edits before committing. Invoke manually with /cache-hygiene-audit; not auto-triggered.
disable-model-invocation: true
allowed-tools: Read Grep Glob Bash(git diff *)
---

Review the pending changes to CLAUDE.md, settings.json, subagent definitions, and any
MCP/tool config. For each item below, check the actual diff: don't assume.

1. Prefix instability: does the edit land near the top of CLAUDE.md, the system prompt, or
   any content that loads before the conversation history? Anthropic invalidates along a
   tools -> system -> messages hierarchy: a change at any level busts everything below it.
   An edit near the top of a stable prefix is far more expensive than the same edit appended
   at the end. See prompt-cache-hygiene practice, item on the invalidation hierarchy.
2. Timestamp/nonce injection: does anything per-request (a timestamp, session ID, nonce) get
   inserted before the cache breakpoint rather than after it? This misses the cache silently,
   with no error returned. See prompt-cache-hygiene practice, item on breakpoint placement.
3. Tool-schema churn: does this diff add, remove, or reorder a tool definition, an MCP server,
   or a subagent's `tools:` list mid-session-lifecycle (i.e., in a way users would pick up
   without restarting)? Adding one tool schema busts the cached prefix above it for every
   session that picks up the change.
4. Report each finding as: file, line range, which of the three checks it trips, and the
   practice citation. If nothing trips, say so plainly: don't manufacture a finding.
```

## Checklist this skill runs, and what backs it

All three checks cite the same practice page: this skill is narrower than `cost-review.md` on purpose, so each item maps to a specific bullet:

| Check | Backed by |
| --- | --- |
| Prefix instability (edit lands above a stable, cached block) | [prompt-cache-hygiene](../../practices/prompt-cache-hygiene.md): "Anthropic invalidates along a hierarchy (`tools → system → messages`)" |
| Timestamp/nonce before the breakpoint | [prompt-cache-hygiene](../../practices/prompt-cache-hygiene.md): "put the breakpoint on the last identical block" |
| Tool-schema churn mid-session | [prompt-cache-hygiene](../../practices/prompt-cache-hygiene.md): "editing one tool schema mid-session re-writes the entire cached prefix" |

## What this doesn't do

It doesn't measure your actual cache hit rate: that's [`cost-review.md`](cost-review.md), which reads real usage JSONL. This one is a pre-commit static check on the config diff itself, so it can (and should) run before you've generated any usage data at all.
