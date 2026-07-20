---
verified_on: 2026-07-01
stale_after: 2026-10-01
sources:
  - https://platform.claude.com/docs/en/build-with-claude/prompt-caching
  - https://github.com/opensquilla/claw-swe-bench
  - https://arxiv.org/abs/2604.22750
  - https://arxiv.org/abs/2606.23525
  - https://github.com/mem0ai/mem0
  - https://github.com/yamadashy/repomix
  - https://github.com/microsoft/LLMLingua
  - https://arxiv.org/abs/2605.12925
  - https://www.anthropic.com/engineering/code-execution-with-mcp
  - https://arxiv.org/abs/2604.21816
  - https://arxiv.org/abs/2602.14878
  - https://github.com/lm-sys/RouteLLM
  - https://openrouter.ai/docs/guides/routing/provider-selection
  - https://arxiv.org/abs/2604.17400
  - https://arxiv.org/abs/2603.15183
  - https://arxiv.org/abs/2605.17672
  - https://arxiv.org/abs/2605.14237
  - https://arxiv.org/abs/2605.27922
---
# Harness-waste taxonomy & sizing

**Harness-waste is spend that's fixable without a better model: context bloat, redundant re-reads, retry loops, bad tool schemas, oversized tool results, model mis-selection, coordination overhead, over-thinking. This note catalogs each waste type, its mechanism, and its published size: read the sizing column adversarially, since almost none of these numbers is an independently measured, whole-bill, per-session figure.**

| # | Waste type | Mechanism | Published size (confidence) |
|---|---|---|---|
| 1 | Cache-miss / prefix instability | A stable prefix re-sent every turn bills at 100% instead of ~10% whenever it mutates or the TTL lapses | Cache read = 0.1x input, ~90% off (fact, 2 primaries). Observed hit rates 66.8–96.5% in one study (single-source). Fix-side deployments moved hit rate 7%→74% and 60%→87% (low confidence, vendor blog) |
| 2 | Redundant re-reads / context snowball | Each step re-sends the full prior history, so cost grows super-linearly even without new information | Agentic tasks consume ~1000x more tokens than code-chat (corroborated, task-class comparison). Same-task variance up to 30x (corroborated) |
| 3 | Retry / repair loops ("Lucky Pass") | The agent reaches a correct outcome via regression cycles and blind retries (waste present even when the run succeeds) | 10.7% of passing trajectories are Lucky Passes; per-model range 0.5–23.2% (single-source, process not tokens/USD) |
| 4 | Tool-schema / MCP bloat (static) | Every tool's full schema is injected eagerly into context regardless of use | Heavy tools ~1,000 tokens each; a 93-tool server ~55k tokens; 5–10 servers ~100k–200k tokens before the first message (low confidence, vendor illustrative) |
| 5 | Tool-schema verbosity → step inflation | Richer tool descriptions raise per-call success but make the agent take more steps | +5.85 pp median success but +67.46% median execution steps, regressing 16.67% of cases; 97.1% of 856 tools show a description smell (corroborated, one harness) |
| 6 | Oversized tool results | Tool calls return complete payloads when the model needs a fraction, and the raw result lingers in history | A 2-hour meeting transcript can add >50k tokens to extract action items (low confidence, illustrative); no published size figure for the general case |
| 7 | Model mis-selection | Routing every call, including trivial subtasks, to the most expensive frontier model | "Default-to-frontier" described as ~1/3+ of wasted spend; routing recovers 30–70% (some 90%) on the routed slice (low confidence, audit-vendor blogs) |
| 8 | Multi-agent coordination overhead | Sub-agents re-broadcast full shared state to each other, fanning context out beyond what the task needs | One scheduling method: ~27.3% token reduction (single-source, live-run). Another: 84.2–95.0% reduction (single-source, simulation only, no real bill) |
| 9 | Over-thinking / reasoning-token waste | Reasoning models keep emitting tokens after the answer has stabilized | 26.2% average token reduction with preserved accuracy across 5 models/5 benchmarks (single-source, author eval) |
| 10 | Repeated-task re-reasoning | A deterministic, repetitive task is re-reasoned from scratch each run instead of replaying a recorded recipe | 93.3–99.98% monthly token reduction (single-source, self-run projection; narrow scope) |

**Cross-cutting sizing anchors:** same-task, same-agent variance up to 30x in total tokens is the single strongest aggregate harness-waste signal: identical task, model, and harness, yet a 30x spread. Harness choice alone swings resolve rate ~27 percentage points at a fixed model, and adapter design up to ~54 pp on one backbone, confirming harness, not model, is a first-order cost/outcome axis.

**Honest note:** there is no published, independently measured, whole-bill, per-session distribution of harness-waste by type. Every number above is either a pricing constant (#1's ~90% cache discount), a fix-side "we recovered X%" claim whose denominator is the fix's own evaluation, or a vendor/blog illustration. Simulation-only and self-run-projection figures should never be quoted as measured savings.

Go deeper: [Measuring capability-limit vs harness-waste](measuring-capability-vs-harness-waste.md) · [Waste-attribution-first practice](../practices/waste-attribution-first.md)

## Sources
- https://platform.claude.com/docs/en/build-with-claude/prompt-caching
- https://github.com/opensquilla/claw-swe-bench
- https://arxiv.org/abs/2604.22750
- https://arxiv.org/abs/2606.23525
- https://github.com/mem0ai/mem0
- https://github.com/yamadashy/repomix
- https://github.com/microsoft/LLMLingua
- https://arxiv.org/abs/2605.12925
- https://www.anthropic.com/engineering/code-execution-with-mcp
- https://arxiv.org/abs/2604.21816
- https://arxiv.org/abs/2602.14878
- https://github.com/lm-sys/RouteLLM
- https://openrouter.ai/docs/guides/routing/provider-selection
- https://arxiv.org/abs/2604.17400
- https://arxiv.org/abs/2603.15183
- https://arxiv.org/abs/2605.17672
- https://arxiv.org/abs/2605.14237
- https://arxiv.org/abs/2605.27922
