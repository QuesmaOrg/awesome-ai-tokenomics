---
verified_on: 2026-07-02
stale_after: 2026-10-02
sources:
  - https://www.vaudit.com/
  - https://github.com/BerriAI/litellm
  - https://developers.cloudflare.com/ai-gateway/features/spend-limits/
  - https://platform.claude.com/docs/en/build-with-claude/prompt-caching
  - https://platform.openai.com/docs/guides/prompt-caching
  - https://www.truefoundry.com/docs/ai-gateway/budgetlimiting
  - https://portkey.ai/docs/product/ai-gateway/virtual-keys/budget-limits
  - https://github.com/kenn-io/agentsview
  - https://focus.finops.org/focus-specification/
  - https://www.linuxfoundation.org/press/linux-foundation-announces-the-intent-to-launch-the-tokenomics-foundation-to-establish-open-standards-for-ai-cost-management
---
# Whole-bill reconciliation

**Every tokenomics tool today reports *calculated* spend: tokens times a price map, computed at request time. The *actual invoice* is a different number, produced by the provider's own metering after discounts, cloud pass-through, and billing lag. Reconciliation closes that gap, proving line by line that what you were billed equals what you actually consumed.**

- **The gap is structural, not noise.** Calculated cost and billed cost come from two systems that never see each other. One documented case: a $3.60/month calculated estimate billed at $25–40/month, a 7–11x gap driven by retry amplification (a malformed tool call retried at a 20% rate adds roughly 1.2x the expected token cost, with *each* retry carrying the full accumulated context), context accumulation, and 200–500 hidden tokens per call injected by agent frameworks.
- **Discount capture silently fails.** If a meter doesn't split cache-read/cache-creation from plain input, it overstates spend on the cheapest tokens; batch-API discounts, tier/volume/commit rates, and stale price-registry entries all drift the calculated number away from the real one.
- **Multi-provider, multi-invoice-surface.** The same model can bill to three different places depending on route (a direct API console, a cloud marketplace's cost-explorer, or another cloud's billing report), so a bill spanning several tools has no single invoice to reconcile against.
- **Cloud-routed traffic doesn't return cost at all.** On some cloud routes, the coding harness never reads cost back from the cloud account, so its own telemetry is an estimate that can silently diverge from the metered figure until finance reconciliation catches it.
- **The only named two-sided reconciler is single-source and contested.** One commercial tool claims $1.7M in overcharges found across 60 companies via SDK-captured usage compared against the real invoice; that magnitude is publicly disputed by two major model providers. The *mechanism* (capture usage, join to the real invoice) is corroborated independently; the *numbers* are not.
- **A shared schema is emerging.** A vendor-neutral billing standard (FOCUS 1.4, ratified 2026-06-04) adds invoice-detail and billing-period datasets (a target format for this reconciliation join), though it carries no token-class detail (no cache-read/write or reasoning-token fields) and no session granularity yet.

**What remains open:** a cross-vendor, two-sided reconciler that joins captured usage to the real invoices across multiple coding tools and cloud billing exports, splitting every discount lever correctly and separating legitimate discounts from genuine over-charges and from harness-waste dollars. Nobody has built it yet.

Go deeper: [Cache economics & whole-bill anatomy](cache-economics-and-whole-bill-anatomy.md) · [Whole-bill measurement practice](../practices/whole-bill-measurement.md)

## Sources
- https://www.vaudit.com/
- https://github.com/BerriAI/litellm
- https://developers.cloudflare.com/ai-gateway/features/spend-limits/
- https://platform.claude.com/docs/en/build-with-claude/prompt-caching
- https://platform.openai.com/docs/guides/prompt-caching
- https://www.truefoundry.com/docs/ai-gateway/budgetlimiting
- https://portkey.ai/docs/product/ai-gateway/virtual-keys/budget-limits
- https://github.com/kenn-io/agentsview
- https://focus.finops.org/focus-specification/
- https://www.linuxfoundation.org/press/linux-foundation-announces-the-intent-to-launch-the-tokenomics-foundation-to-establish-open-standards-for-ai-cost-management
