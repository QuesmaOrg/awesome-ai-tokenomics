---
verified_on: 2026-07-03
stale_after: 2026-10-03
---
# Claims

Working claims, each scored by how confident we are and backed by the linked evidence, not settled fact. When a claim hardens or breaks, this page changes and says so. Confidence sits at *medium* across the board: several rows lean partly on our own instrumented sessions (unpublished single-machine data), and independent literature work to harden them is ongoing.

| Claim | Confidence | Strongest evidence |
|---|---|---|
| Nobody offers cross-vendor whole-bill measurement combined with per-session attribution of spend to capability-limit vs harness-waste | medium | Closest existing product misses the attribution axis ([Faros AI token intelligence](https://www.faros.ai/blog/token-intelligence-for-ai-engineering)) |
| The capability-limit vs harness-waste split is automatable from a live transcript today | medium | Our own prototype's deterministic detectors + LLM judge (unpublished; survived an adversarial cache-TTL test) |
| Fixable harness-waste is a meaningful share of a real whole bill: ~11% is a defensible floor | medium | Our own instrumented sessions: 10.9–13.1% (unpublished, single-machine) |
| Harness design rivals model choice as the cost driver of agentic coding | medium | ~66x same-model input-token spread across harnesses ([Terminal-Bench](https://www.tbench.ai/)); ~54 pp same-model success swing from adapter design alone ([Claw-SWE-Bench](https://github.com/opensquilla/claw-swe-bench)); one compaction-threshold change roughly doubled a bill ([Codex issue #16812](https://github.com/openai/codex/issues/16812)) |
| Cross-vendor $/MTok comparison is invalid without tokenizer normalization | medium | >2.65x same-content token spread; the cheapest vendor flips by content type ([TensorZero](https://www.tensorzero.com/blog/stop-comparing-price-per-million-tokens-the-hidden-llm-api-costs/)); corroborated academically ([arXiv:2506.06446](https://arxiv.org/abs/2506.06446)) |
| More context ≠ better: context volume is itself a capability limit | medium | 18-model degradation with growing context ([Context Rot](https://www.trychroma.com/research/context-rot)); effective context ≪ claimed length ([RULER](https://github.com/NVIDIA/RULER)) |
| The multi-agent orchestration tax is real but unmeasured: no independent general multiplier exists | medium | A measured $1,434/day retry storm in one framework ([arXiv:2604.16646](https://arxiv.org/abs/2604.16646)); the equal-budget counterpoint ([arXiv:2604.02460](https://arxiv.org/abs/2604.02460)); every circulating multiplier figure failed our verification |
| Cost-optimization gravity is shifting from model-tuning to the prompt/context/harness side | medium | OpenAI winding down self-serve fine-tuning, citing that prompting won ([deprecations](https://developers.openai.com/api/docs/deprecations)); a 41-repo context-compression genre bloom and a coding-specific routing literature land on the same side |

Two honest caveats. The "orchestration tax" row deliberately stops short of a number: the mechanism is corroborated, but the widely-quoted multipliers (including a vendor's 15x figure) are not independent measurements. And rows resting on our unpublished session data are labeled as such: treat them as weaker than the externally-sourced rows until the public evidence lands.

Go deeper: [Harness-waste taxonomy](concepts/harness-waste-taxonomy.md) · [Measuring capability-limit vs harness-waste](concepts/measuring-capability-vs-harness-waste.md)
