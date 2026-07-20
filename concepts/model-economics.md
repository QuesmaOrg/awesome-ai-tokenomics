---
verified_on: 2026-07-02
stale_after: 2026-10-02
sources:
  - https://artificialanalysis.ai/agents/coding-agents
  - https://artificialanalysis.ai/leaderboards/models
  - https://arxiv.org/abs/2511.05722
  - https://developers.openai.com/api/docs/guides/reasoning
  - https://arxiv.org/abs/2602.13517
  - https://huggingface.co/Qwen/Qwen3.6-27B
  - https://quesma.com/blog/qwen-36-is-awesome/
  - https://github.com/opensquilla/claw-swe-bench
  - https://arxiv.org/abs/2605.27922
---
# Model economics: picking the right-sized model

**Per-token sticker price barely predicts what a task actually costs: a "cheap" model can burn far more tokens to reach the same answer, and the harness wrapped around a model moves the bill more than the model choice does. As of 2026-07, buy the capability "knee," not the frontier peak, for anything that isn't genuinely capability-limited.**

- **Per-token price is a lie about cost.** Same-accuracy runs can span up to 5x in output-token length across models; one comparison found a cheaper-per-token model burned 26.3x more tokens than a pricier one at similar accuracy. Tokens-per-outcome on your own workload is the only honest denominator.
- **Reasoning is billed at the priciest meter, invisibly.** Providers bill hidden reasoning/thinking tokens at the output rate and don't return them. Reasoning firing on tasks that don't need it (tool-argument validation, JSON extraction) can cost 3–7x tokens for an identical answer; that's fixable harness-waste, not capability spend.
- **The stack, not the model, sets the bill.** As of 2026-07-02, full model×harness combinations spanned $0.27 to $11.8 per task (~44x) on one industry index; even at *identical* quality score the spread was still ~4.4x ($0.27 vs $1.18). A widely-repeated "32x at near-identical quality" figure is a dated, launch-era snapshot: treat it as stale.
- **Buy the knee, not the peak.** As of 2026-07-02 on the same index, the top-scoring model cost roughly 2x for only 4 extra index points over the model just below it. Frontier-peak pricing is for genuinely capability-limited work only.
- **The setup levers, in order of leverage:** harness choice (the single biggest lever at fixed quality) > model choice within the needed capability band (one model-version upgrade alone cut average tokens per problem ~3.8x) > reasoning-effort setting per task type > output-verbosity setting (a near-linear cost lever, ~2.3x measured low to high) > cache discipline (~10x read-vs-miss spread) > local models where they fit (one ~27B open model reportedly scored within ~3 points of trillion-parameter models on a coding benchmark, though a leading cloud API is cheap enough that local mainly wins on privacy/latency, not $/token).

**Confidence: medium.** Leaderboard standings move weekly; per-model token/cost figures are often single-source index data; local-model benchmark scores are vendor self-reported. Anything cited from here needs its date re-checked.

Go deeper: [Orchestration economics](orchestration-economics.md) · [Model-tier routing practice](../practices/model-tier-routing.md)

## Sources
- https://artificialanalysis.ai/agents/coding-agents
- https://artificialanalysis.ai/leaderboards/models
- https://arxiv.org/abs/2511.05722
- https://developers.openai.com/api/docs/guides/reasoning
- https://arxiv.org/abs/2602.13517
- https://huggingface.co/Qwen/Qwen3.6-27B
- https://quesma.com/blog/qwen-36-is-awesome/
- https://github.com/opensquilla/claw-swe-bench
- https://arxiv.org/abs/2605.27922
