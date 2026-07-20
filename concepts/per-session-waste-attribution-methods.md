---
verified_on: 2026-07-01
stale_after: 2026-10-01
sources:
  - https://github.com/opensquilla/claw-swe-bench
  - https://arxiv.org/abs/2605.27922
  - https://arxiv.org/abs/2605.12925
  - https://arxiv.org/abs/2606.17799
  - https://www.faros.ai/blog/token-intelligence-for-ai-engineering
  - https://arxiv.org/abs/2604.22750
---
# Per-session waste attribution: methods & the state of the art

**Given one live coding-agent session, can you attribute its spend to a cause: did the model hit a real capability ceiling, or did the harness burn tokens the model didn't need? The one-line finding: the field can measure that waste exists and flag some kinds automatically, but no published method attributes a live session's spend to capability-limit vs harness-waste.**

Every method taps a different depth of the same transcript. Read as a five-rung ladder, from cheapest signal to the (still unreached) target:

| Layer | What it reads | Carries the capability-vs-waste cut? |
|---|---|---|
| L0 Structural counts | tokens, turns, tool calls, retries | No: sizes spend, blind to *why* |
| L1 Structural patterns | exact-duplicate calls, error keywords, out-of-scope actions | Weakly: flags *some* harness-waste, silent on capability |
| L2 Semantic/intent labels | per-action intent, "is looping," near-duplicate detection | Partially: separates process-quality waste, not the capability cut |
| L3 Counterfactual/causal | would the task still succeed if this step were removed? | Closest: removable ≈ waste by construction, but not necessarily the harness's fault |
| L4 Cause attribution | was this spend forced by a model limit, or a fixable harness? | The target: no published per-session method reaches it |

The reason L4 sits empty: the capability-vs-waste label is a counterfactual claim about a *different* model or harness, and no signal inside a single trajectory witnesses a counterfactual. The only methods that genuinely separate the axis do it by offline experiment (holding the model fixed and varying the harness across many runs), not by reading one live session.

**What's proven at each layer:**
- L0–L1 heuristics are fully automatable and cheap, but only catch crude symptoms; loops that vary their arguments don't register as exact repeats, so they slip past.
- L2 LLM-judge scoring is the current workhorse. One rubric-based judge reports the best human-correlation numbers seen in this space (Pearson r=0.79, Krippendorff α=0.83), still a judgment call, not a cause attribution, and unvalidated on most real coding harnesses.
- L3 counterfactual reduction has been executed, not just theorized: one method cut input tokens 39.9–59.7% and total cost 21.1–35.9% while holding accuracy flat: the strongest evidence that a large slice of a coding session's tokens are removable without loss.
- Step-level redundancy labeling (the foundation L3 depends on) is itself near-unsolved: the best automated detector matches human judgment on only 24.88% of steps (task-level detection reaches ~70.9%).
- About 1 in 10 passing runs shows a wasteful-but-correct path in one study, with per-model rates ranging 0.5–23.2%.

**What's still open:** a per-session attributor would need a learned bridge from in-session signals to offline harness-swing ground truth; it must emit dollars, not just a quality tier; it must catch near-duplicate/varied-argument waste, not just exact repeats; and its judge needs human-correlation validation on real coding sessions specifically, none of which exists yet.

Go deeper: [Measuring capability-limit vs harness-waste](measuring-capability-vs-harness-waste.md) · [Harness-waste taxonomy](harness-waste-taxonomy.md) · [Waste-attribution-first practice](../practices/waste-attribution-first.md)

## Sources
- https://github.com/opensquilla/claw-swe-bench
- https://arxiv.org/abs/2605.27922
- https://arxiv.org/abs/2605.12925
- https://arxiv.org/abs/2606.17799
- https://www.faros.ai/blog/token-intelligence-for-ai-engineering
- https://arxiv.org/abs/2604.22750
