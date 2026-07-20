---
verified_on: 2026-07-02
stale_after: 2026-10-02
sources:
  - https://arxiv.org/abs/2604.22750
  - https://github.com/opensquilla/claw-swe-bench
  - https://arxiv.org/abs/2605.27922
  - https://arxiv.org/abs/2605.12925
  - https://arxiv.org/abs/2606.17799
  - https://www.tbench.ai/
  - https://arxiv.org/abs/2509.23586
  - https://arxiv.org/abs/2605.29893
  - https://arxiv.org/abs/2606.23525
  - https://arxiv.org/abs/2509.09853
---
# Measuring capability-limit vs harness-waste

**Every token an agent spends was either something the model genuinely needed (capability-limit) or something a better-built harness could have avoided (harness-waste). A transcript shows the spend, never the counterfactual of what a better model or harness would have done, so every measurement method here is really a way to manufacture that missing counterfactual.**

**What's proven (multiple independent studies converge):**
- The harness is a first-order driver of accuracy and cost, comparable to a model generation: three independent studies find harness choice moves task success by roughly 27, 22, and 23.8 percentage points at a fixed model, and adapter/config quality alone can swing one model 19.1%→73.4% (a ~54 pp gap).
- One benchmark-controlled comparison found the same model, same quality-or-better, at a ~66x input-token spread across two harnesses (3.9M vs 256.9M tokens): the harness can dominate the bill even more than it dominates accuracy.
- Near-equal task-success spans a ~170x cost range in dollars ($8 to $1,399) in one adapter-protocol study, and a ~2.5x token spread at identical security score in another.
- More tokens does not mean more success: accuracy peaks at intermediate spend and saturates or degrades at the top, so a large slice of high spend is unproductive.
- Waste is real even on successful runs: roughly 1 in 10 passing runs in one study showed a wasteful path, with the worst categories burning 25–40x a clean run's tokens.
- A large removable slice has been demonstrated, not just estimated: one method cut input tokens 39.9–59.7% and net cost 21.1–35.9% at flat accuracy.
- Token efficiency is intrinsic to the model (it survives shared-success and shared-failure subsets), a genuine capability-side signal cleanly separated from task difficulty; one study found a >1.5M-token gap between models on the same tasks.

**What's still open:**
- No published method attributes a single *live* session's spend to capability-limit vs harness-waste: every rigorous separation so far is an offline experiment that reruns the same task through a different harness or model, not a real-time read of one transcript.
- Step-level waste detection is close to unsolved: the best automated detector found only 24.88% of redundant steps against human-labeled ground truth (task-level detection reaches ~70.9%).
- Cross-run variance is under-measured: one study found up to 30x token variance across repeated runs of the identical task.
- No method yet ties a wasteful path to real billed dollars *and* names which specific harness mechanism caused it: today's ablations attribute to a configuration, not a cause.

Go deeper: [Per-session waste attribution](per-session-waste-attribution-methods.md) · [Harness-waste taxonomy](harness-waste-taxonomy.md) · [Whole-bill reconciliation](whole-bill-reconciliation.md)

## Sources
- https://arxiv.org/abs/2604.22750
- https://github.com/opensquilla/claw-swe-bench
- https://arxiv.org/abs/2605.27922
- https://arxiv.org/abs/2605.12925
- https://arxiv.org/abs/2606.17799
- https://www.tbench.ai/
- https://arxiv.org/abs/2509.23586
- https://arxiv.org/abs/2605.29893
- https://arxiv.org/abs/2606.23525
- https://arxiv.org/abs/2509.09853
