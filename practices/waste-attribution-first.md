---
verified_on: 2026-07-03
stale_after: 2026-10-03
sources:
  - https://arxiv.org/abs/2605.12925
  - https://www.faros.ai/blog/token-intelligence-for-ai-engineering
  - https://arxiv.org/abs/2605.29893
---
# Waste-attribution first

**Classify each unit of spend as capability-limit or harness-waste before trying to cut it. Optimizing unattributed spend risks cutting capability the task genuinely needed instead of the waste the harness introduced.**

An agent re-reading the same config file five times looks like waste, but cut it blindly and you might starve a model that genuinely needed the reminder.

- Attribution is a counterfactual claim: "a better model wouldn't have needed this" or "a better harness wouldn't have burned this," and no signal inside a single transcript directly witnesses that counterfactual.
- Raw spend (tokens, cost, turns, duration) sizes the bill but is blind to *why* it went out; even structural patterns like repeated file reads only weakly flag *some* harness-waste and say nothing about the capability side.
- No published method attributes a *live* session's spend to capability-limit vs harness-waste: the only rigorous separations are offline experiments that hold the model fixed and vary the harness, or vice versa.
- The stakes cut both ways: harness-waste is common and large (the worst documented categories burn 25–40x a clean run's tokens even on successful runs), but genuine capability need is real too.
- Tempting shortcuts don't hold up: read-to-edit ratio and exact-duplicate detection are not validated as waste metrics, and they miss the more expensive varied-argument loops.
- A known taxonomy of harness-waste types exists: cache-miss, redundant re-reads, retry loops, tool-schema bloat, model mis-selection, coordination overhead, over-thinking, repeated-task re-reasoning. **Caveat:** most published size figures for these types are fix-side or vendor-illustrative, not independently measured, so use the checklist with an attribution step, not as a menu of guaranteed savings.

**How to apply**
- Before proposing a fix, name which axis the targeted spend sits on: capability-limit (fix: a better or cheaper model) or harness-waste (fix: a better harness), and say what evidence backs the call.
- Prefer signals with real attribution power over raw spend: structural duplicate/error patterns are weak, process/intent scoring against known-good paths is stronger, an executed ablation is strongest.
- Check candidates against the known taxonomy of harness-waste types rather than inventing a new one from a single session's symptoms.
- Count "removable without loss" as harness-waste only when an actual counterfactual shows it: not a heuristic like read-to-edit ratio.
- If you can't tell which side the spend is on, say so: don't quietly default it to either side.

Go deeper: [Harness-waste taxonomy & sizing](../concepts/harness-waste-taxonomy.md) · [Per-session waste attribution](../concepts/per-session-waste-attribution-methods.md) · [Whole-bill measurement](whole-bill-measurement.md)

## Sources
- https://arxiv.org/abs/2605.12925
- https://www.faros.ai/blog/token-intelligence-for-ai-engineering
- https://arxiv.org/abs/2605.29893
