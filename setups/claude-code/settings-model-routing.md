---
verified_on: 2026-07-18
sources:
  - https://code.claude.com/docs/en/settings
  - https://code.claude.com/docs/en/sub-agents
  - https://code.claude.com/docs/en/model-config
---

# Model-tier routing: `settings.json` + subagent pattern

**TL;DR:** a `settings.json` ceiling plus per-subagent `model:` fields that encode a reviewable, tiered escalation *policy*. This pattern has been running on our own research stack since 2026-07-02. Every routing repo we surveyed (NadirClaw, muxer, model-router, smart-router) routes by request-time classification; none of them version-control a reviewable escalation rule the way this does.

## Be honest about what's config and what's convention

`settings.json` can mechanically enforce a model *ceiling*: which models are even selectable. It cannot mechanically enforce "two confirmed quality failures reverts the default worker to a higher tier": that's a team convention, written down and followed by whoever reviews the work, not a runtime feature. The pattern below is config (the ceiling) plus a policy document (the rule) checked into the same repo, so the rule is at least versioned and reviewable even though it isn't automated.

## The tiers

| Tier | Role | Model | Escalates to |
| --- | --- | --- | --- |
| Brain | Plans, decomposes, resolves disputes, final review | Frontier tier (highest-capability model available to you) | - |
| Default worker | Implementation, tests, docs, routine legwork | Mid tier (e.g. Sonnet) | Accuracy-critical tier, on a stated reason |
| Accuracy-critical | Validation gates, hardest end-to-end work, anything whose errors become fact | High-capability worker tier (e.g. Opus) | Brain, only per-item |
| Micro | Narrow, high-volume mechanical subtasks with downstream review | Smallest capable tier (e.g. Haiku) | Default worker |

## `settings.json`: set the ceiling

```json
{
  "availableModels": ["opus", "sonnet", "haiku"],
  "enforceAvailableModels": true,
  "fallbackModel": ["claude-sonnet-5", "claude-haiku-4-5"],
  "effortLevel": "medium"
}
```

- `availableModels` is a hard allowlist restricting what's selectable for the main session, subagents, skills, and the advisor. ([docs](https://code.claude.com/docs/en/settings))
- `enforceAvailableModels: true` extends that allowlist to the Default model option too, so a session can't silently fall back to something off-list.
- `fallbackModel` is a same-turn overload fallback, capped at three models: it does not merge across settings files, so set the whole chain in your highest-precedence file.
- Deliberately leaving the frontier tier *out* of a worker's `availableModels` scope (project-level settings) is how you stop a worker from silently inheriting the brain's model: set it at the subagent-definition level instead (below), and use `availableModels` at the project level as the backstop.

## Per-subagent frontmatter: pin the tier per role

Never let a delegated worker inherit the orchestrating session's model implicitly. Pin it explicitly in each subagent's own frontmatter:

```markdown
---
name: implementer
description: Default worker. Implementation, tests, docs, mechanical verification, ad-hoc legwork. Use for anything bounded and well-specified.
tools: Read, Edit, Write, Bash, Grep, Glob
model: sonnet
---
```

```markdown
---
name: verifier
description: Accuracy-critical tier. Validation gates, hardest end-to-end coding, anything whose errors would enter a document as fact. Must not be the same hand that produced the work under review.
tools: Read, Bash, Grep, Glob
model: opus
---
```

`model:` accepts `sonnet`, `opus`, `haiku`, `inherit`, or a full model ID ([sub-agents docs](https://code.claude.com/docs/en/sub-agents#choose-a-model)). Using `inherit` anywhere in a worker's frontmatter defeats this whole pattern: it's the one value to avoid on a tier-pinned subagent.

## The policy, written down (not a config key)

Keep this as a short markdown block near your `settings.json`, reviewed like code:

```markdown
## Escalation policy

- The brain plans, decomposes, and resolves disputes. It does not do bulk reads, web
  sweeps, or batch edits: that's a worker's job, wherever it's happening.
- A worker may return a task with a stated reason instead of completing it, if it judges
  the task needs a higher tier.
- The brain may re-run a *single* item on the frontier tier when judgment quality is
  decisive, with a stated reason logged next to the change. It never escalates a whole
  batch this way.
- Two confirmed quality failures from the default worker on a given class of task reverts
  that class to the accuracy-critical tier until review says otherwise. Log the reversion
  and the reason.
- High-cost fan-outs (many parallel agents, deep multi-pass validation) require an explicit
  go-ahead before they run, stating the estimated scope first.
```

None of this is enforced by Claude Code itself: it's enforced by whoever reviews subagent definitions and PRs. That's the honest boundary: config sets the ceiling, the document sets the rule, a human (or the brain, reading the document) applies it.
