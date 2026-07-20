# Practices

Tool-agnostic, evidence-grounded standards for token-efficient agentic coding.

## Cost & workflow practices
- [Model-tier routing](model-tier-routing.md) - route each task to the cheapest model tier that clears its quality bar; escalate one item at a time, never a batch.
- [Prompt-cache hygiene](prompt-cache-hygiene.md) - keep the stable prefix append-only and byte-identical so the cache hits instead of silently re-billing at full price.
- [Context-compaction discipline](context-compaction-discipline.md) - compaction is a costed operation with a re-read-loop failure mode; measure it, don't trust it.
- [Whole-bill measurement](whole-bill-measurement.md) - sum every token class, sub-call, retry, and non-token charge, and reconcile against the actual invoice.
- [Waste-attribution first](waste-attribution-first.md) - classify spend as capability-limit vs harness-waste before cutting it.

## Knowledge ops
- [LLM-legible knowledge base](llm-legible-knowledge-base.md) - plain-markdown cross-linked wiki; raw sources / synthesis / schema doc separated; lean index files as agent entry points.
- [Messy capture, atomized synthesis](messy-capture-atomized-synthesis.md) - capture cheap and unstructured; impose atomicity and validation at synthesis time.
- [Atomic notes + typed frontmatter](atomic-notes-typed-frontmatter.md) - one fact per note bounds agent-edit blast radius; typed frontmatter is a machine contract, lint-enforced.
