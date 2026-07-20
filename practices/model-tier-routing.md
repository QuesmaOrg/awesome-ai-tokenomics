---
verified_on: 2026-07-03
stale_after: 2026-10-03
sources:
  - https://www.mindstudio.ai/blog/smart-orchestrator-cheaper-sub-agent-models-claude-code
  - https://cognition.com/blog/devin-fusion
  - https://github.com/lm-sys/RouteLLM
  - https://www.notdiamond.ai/
  - https://openrouter.ai/docs/guides/routing/provider-selection
---
# Model-tier routing

**Route each task to the cheapest model tier that clears its quality bar: reserve the frontier tier for planning, decomposition, and judgment, and escalate one item at a time, never a whole batch.**

Routing every task to a cheap model looks like a savings, until it thrashes on the one genuinely hard problem and burns three re-runs: a frontier model would have landed it once. The goal is cheapest *that clears the bar*, not cheapest outright.

- A frontier-plans, cheap-executes split is a real pattern, observed across four independent sources (a vendor, two independent practitioners, and a shipped product), though no single source's savings number holds up on its own.
- Per-token price is not per-task cost: same-accuracy runs can span up to 5x in output-token length across models, so the real denominator is tokens-per-outcome on your workload, not sticker price.
- The top model on a leaderboard rarely earns its price for routine work: it can cost roughly 2x for only a few index points over the model just below it.
- Multi-agent orchestration is not free: orchestrated setups can burn on the order of 15x the tokens of a single-agent call, and controlled research finds single-agent systems match or beat multi-agent ones once reasoning tokens are held constant.
- Naive routing can cost more than it saves: mis-delegating to a cheaper tier forces re-runs that reintroduce the cost tiering was meant to remove.

**How to apply**
- Reserve the highest-capability tier for ambiguity resolution, architecture and plan decisions, and final review; route everything bounded and mechanical to a cheaper tier by default.
- Pin the model tier per role or subtask explicitly: never let a delegated worker silently inherit the orchestrator's model.
- Set concrete escalation tripwires (repeated quality flags, scope creep) instead of quietly raising effort on the cheap tier, and escalate single items, never whole batches.
- Treat any vendor's savings multiplier as unconfirmed until measured on your own workload: the pattern is corroborated, the magnitude is not.

Go deeper: [Model economics](../concepts/model-economics.md) · [Orchestration economics](../concepts/orchestration-economics.md) · [Waste-attribution first](waste-attribution-first.md)

## Sources
- https://www.mindstudio.ai/blog/smart-orchestrator-cheaper-sub-agent-models-claude-code
- https://cognition.com/blog/devin-fusion
- https://github.com/lm-sys/RouteLLM
- https://www.notdiamond.ai/
- https://openrouter.ai/docs/guides/routing/provider-selection
