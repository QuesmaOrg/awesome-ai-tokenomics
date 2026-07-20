---
verified_on: 2026-07-18
status: "untested-as-skill: syntax-checked against the current SKILL.md frontmatter format only; not run end-to-end"
sources:
  - https://code.claude.com/docs/en/skills
  - https://github.com/ccusage/ccusage
  - https://github.com/Piebald-AI/splitrail
---

# `/cost-review`: audit your own usage data

**TL;DR:** every "cost audit" skill we found in the wild either wasn't a real Claude Code skill despite its marketing, or admitted its savings figures were priced-from-a-rate-card rather than measured. This one is deliberately dumb: it runs a local usage tool against *your* JSONL and flags anti-patterns, citing the practice that backs each check: no invented savings percentage.

**Note:** the `SKILL.md` frontmatter below matches the current documented format (`name`, `description`, `disable-model-invocation`, `allowed-tools`, per [docs](https://code.claude.com/docs/en/skills)). We have not run this as a live skill end-to-end. Treat it as a starting point, not a drop-in tool.

## Install

Save the block below as `.claude/skills/cost-review/SKILL.md`. Requires [ccusage](https://github.com/ccusage/ccusage) (or [splitrail](https://github.com/Piebald-AI/splitrail)) installed and on your `PATH`: see [`../README.md`](../README.md) for both.

```markdown
---
name: cost-review
description: Audit this machine's own Claude Code / Codex usage data for cost anti-patterns. Invoke manually with /cost-review; not auto-triggered.
disable-model-invocation: true
allowed-tools: Bash(ccusage *) Bash(npx ccusage *) Read
---

Run a cost review of the current user's own usage data. Do not estimate or invent numbers:
every figure in your report must come from a command you actually ran against local JSONL.

1. Run `npx ccusage@latest daily --json` (or `ccusage daily --json` if installed) and
   `npx ccusage@latest blocks --json` for the session-block view. Read the actual output.
2. Compute cache hit rate from the cache-read vs. cache-creation vs. uncached-input token
   counts in that output. Flag if hit rate looks low for a session with repeated turns:
   see prompt-cache-hygiene practice, item on tracking cache-read vs. cache-creation tokens.
3. Break down spend by model across the lookback window. Flag any session where a
   high-capability model tier ran for a long stretch on what looks like routine,
   mechanical work: see model-tier-routing practice, item on reserving the top tier for
   ambiguity/architecture/judgment.
4. List the 5 longest sessions by wall time or token count. Flag any that were never
   `/clear`'d between clearly unrelated tasks: see context-compaction-discipline practice.
5. Look for repeated near-identical tool calls or retries in the same session (a sign of a
   retry storm): see waste-attribution-first practice, on classifying spend before cutting it.
6. Report findings as a short table: check, what you found, the number, the practice it
   cites. Do not add a savings estimate you haven't computed from this session's own data.
```

## Checklist this skill runs, and what backs each item

| Check | Practice it cites |
| --- | --- |
| Cache hit rate | [prompt-cache-hygiene](../../practices/prompt-cache-hygiene.md) |
| Model-tier mix | [model-tier-routing](../../practices/model-tier-routing.md) |
| Longest sessions / missing `/clear` | [context-compaction-discipline](../../practices/context-compaction-discipline.md) |
| Retry storms | [waste-attribution-first](../../practices/waste-attribution-first.md) |
| Whole-session reconciliation | [whole-bill-measurement](../../practices/whole-bill-measurement.md) |

## What we deliberately left out

No "estimated $ saved" line. Every audit skill we surveyed that included one was pricing from a rate card, not measuring: the exact failure mode our own quality bar rejects. This skill reports what your JSONL shows; the dollar interpretation is yours to make against your own invoice.
