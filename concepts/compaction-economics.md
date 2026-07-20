---
verified_on: 2026-07-02
stale_after: 2026-10-02
sources:
  - https://www.trychroma.com/research/context-rot
  - https://github.com/NVIDIA/RULER
  - https://platform.claude.com/docs/en/build-with-claude/context-editing
  - https://developers.openai.com/api/docs/guides/conversation-state
  - https://cursor.com/blog/dynamic-context-discovery
  - https://barazany.dev/blog/claude-codes-compaction-engine
  - https://github.com/openai/codex/issues/16812
  - https://platform.claude.com/docs/en/build-with-claude/prompt-caching
  - https://ai.google.dev/gemini-api/docs/pricing
  - https://arxiv.org/abs/2509.23586
  - https://arxiv.org/abs/2606.23525
  - https://news.ycombinator.com/item?id=47923357
---
# Compaction economics: the double-edged lever

Long agent sessions eventually overflow a model's context window, so every serious coding harness *compacts*: it summarizes or evicts old turns and continues on a smaller context. The harness has to compact because context is a **capability limit** (finite, and it degrades as it fills). But *how* it compacts is pure harness design, which makes compaction the cleanest place to watch capability-limit and harness-design interact.

**The vendor-native layer now exists (2026).** Major providers ship context editing, memory tools, and server-side compaction as API primitives; coding harnesses ship their own tiered compaction engines with known failure modes.

**The economics are non-obvious, in three ways:**
- **Compaction itself costs money and can explode the bill.** The sharpest documented case: a coding-CLI regression that merely retuned the compaction threshold turned 4 compactions per session into 12–26, and 89M tokens into 160–185M: same model, same task, roughly 2x the bill, via a file-re-read amplification loop.
- **Compaction fights the cache.** Cached input runs roughly 10x cheaper than fresh input, but editing history to compact it invalidates the cached prefix (a trade-off vendor documentation is explicit about, not a free lunch). Whether a given shipped harness preserves the warm cache through compaction is unresolved and live-measurable.
- **The research frontier optimizes the wrong-shaped thing if unmeasured.** Offline, 40–60% of input tokens are removable at equal performance, and model-triggered ("self-compacting") architectures exist as an alternative to threshold-tuned automatic compaction. But no tool prices a harness's compaction policy per live session.

**Our read:** compaction policy is a tunable dollar knob that harnesses retune silently: the sharpest documented regression shipped in a routine point release, not a deliberate redesign. A whole-bill measurer could detect compaction-driven cost regressions and separate the capability-forced share of the spend from the design-wasted share, surfacing exactly the class of event buyers currently discover only as an unexplained bill spike.

Go deeper: [Cache economics & whole-bill anatomy](cache-economics-and-whole-bill-anatomy.md) · [Harness-waste taxonomy](harness-waste-taxonomy.md) · [Context-compaction discipline practice](../practices/context-compaction-discipline.md)

## Sources
- https://www.trychroma.com/research/context-rot
- https://github.com/NVIDIA/RULER
- https://platform.claude.com/docs/en/build-with-claude/context-editing
- https://developers.openai.com/api/docs/guides/conversation-state
- https://cursor.com/blog/dynamic-context-discovery
- https://barazany.dev/blog/claude-codes-compaction-engine
- https://github.com/openai/codex/issues/16812
- https://platform.claude.com/docs/en/build-with-claude/prompt-caching
- https://ai.google.dev/gemini-api/docs/pricing
- https://arxiv.org/abs/2509.23586
- https://arxiv.org/abs/2606.23525
- https://news.ycombinator.com/item?id=47923357
