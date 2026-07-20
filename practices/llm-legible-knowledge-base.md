---
verified_on: 2026-07-03
stale_after: 2026-10-03
sources:
  - https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f
  - https://llmstxt.org/
---
# LLM-legible knowledge base

**Keep shared knowledge as a plain-markdown, cross-linked wiki with three separated layers: immutable raw sources, a compiled/curated synthesis layer, and a schema doc that disciplines every writer, plus cheap index files agents read first.**

A teammate asks the same question about a dense source three weeks apart. A compiled wiki answers from one note both times; RAG-style re-derivation re-reads and re-reasons over the raw source every time, and bills you for it every time.

- Compile-once beats re-derive-per-query: a persistent, cross-referenced wiki amortizes the token cost of understanding sources across every future query, where RAG-style re-derivation pays it again each time.
- Separating immutable sources from mutable synthesis gives a clean audit trail of inference vs. evidence: a raw-intake layer (provenance-kept) feeding a validated-synthesis layer, gated by review.
- A schema/constitution doc (the Karpathy `CLAUDE.md`-style layer) is the human's real editorial surface: curate the rules and the sources, and let the hands do everything else.
- Low-token entry points let an agent orient without crawling the corpus: a lean index (one line per fact or note) plus an append-only log. This is the same shape the llms.txt spec standardizes for websites: an H1, a summary, and linked sections with one-line descriptions.

**How to apply**
- Keep plain markdown in git, use basename wikilinks, and don't put a proprietary format between the knowledge and the model.
- Physically separate three layers: raw sources stay read-only, synthesis is agent-written and reviewed, and one schema doc governs structure.
- Keep exactly two cheap navigation files (a lean index and an append-only log) and never let them grow into content stores.
- Run a periodic agent lint pass that goes beyond syntax: contradictions between notes, claims superseded by newer sources, orphans, coverage gaps.

Go deeper: [Messy capture, atomized synthesis](messy-capture-atomized-synthesis.md) · [Atomic notes + typed frontmatter](atomic-notes-typed-frontmatter.md)

## Sources
- Karpathy, "llm-wiki", 2026-04-04 - https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f. Confirms the three-layer architecture, the two navigation files, the periodic lint pass, and the compounding-artifact rationale ("the wiki is a persistent, compounding artifact. The cross-references are already there").
- Jeremy Howard / Answer.AI, llms.txt spec, 2024-09-03 - https://llmstxt.org/. Confirms the low-token index-entry-point structure.
