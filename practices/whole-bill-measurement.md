---
verified_on: 2026-07-03
stale_after: 2026-10-03
sources:
  - https://www.vaudit.com/
  - https://github.com/BerriAI/litellm
  - https://github.com/kenn-io/agentsview
---
# Whole-bill measurement

**Measure the entire bill. Count every token class, every sub-call and subagent, every retry, every non-token compute charge, then reconcile the computed total against the provider's actual invoice. Never trust a per-call or per-token average as the bill.**

Wire up a token counter, watch it tick to a few dollars a month, and feel safe, then the invoice lands several times higher, because retries, subagent fan-out, and a web-search charge never showed up in your meter.

- A "whole bill" is not input-plus-output tokens times a rate: true accounting sums uncached input, cache-write, cache-read, and output separately per call, because cache-write is a distinct, higher-priced line on Anthropic that a token-only meter can miss entirely.
- Non-token charges are real and invisible to a token ledger: web search, code-execution container time, and managed-agent session runtime are billed by count or wall-clock, not tokens.
- The real cost of a task is the sum over the entire trajectory tree (retries, tool-result round-trips, planner/critic passes, and every subagent's own full context re-send), not a per-turn or per-call view.
- Calculated spend (tokens times a local price map) and the actual invoice come from two systems that never see each other: one documented case shows a $3.60/month calculated estimate landing as a $25–40/month invoice: a 7–11x gap driven by retry amplification, context accumulation, and framework overhead the calculator never counted.
- On cloud-routed traffic (Bedrock/Vertex), the harness doesn't read cost back from the cloud account at all: its own telemetry is an estimate that can silently diverge from the metered figure until finance reconciliation catches it.

**How to apply**
- Capture every token class per call (uncached input, cache-write, cache-read, output), not a single blended input/output figure.
- Sum across the full trajectory tree (subagents, retries, tool round-trips), since subagent fan-out is often the dominant, best-hidden cost.
- Pull non-token charges (server-side tools, container and session runtime) from their own metering surface; don't assume the token ledger caught them.
- Reconcile computed spend against the actual provider invoice on a cadence, and treat any persistent gap as something to investigate.
- For cloud-routed traffic, pull cost straight from the cloud billing export: don't trust the harness's own telemetry as the bill.

Go deeper: [Whole-bill reconciliation](../concepts/whole-bill-reconciliation.md) · [Cache economics & whole-bill anatomy](../concepts/cache-economics-and-whole-bill-anatomy.md)

## Sources
- https://www.vaudit.com/
- https://github.com/BerriAI/litellm
- https://github.com/kenn-io/agentsview
