---
verified_on: 2026-07-03
stale_after: 2026-10-03
sources:
  - https://karpathy.bearblog.dev/the-append-and-review-note/
  - https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f
---
# Messy capture, atomized synthesis

**Keep capture cheap and ceremony-free: append-friendly, with zero classification at write time. Impose atomicity, structure, and validation later, at synthesis time, when knowledge is compiled into the wiki.**

Spot something worth keeping mid-task. If keeping it means stopping to tag it, file it in the right folder, and backlink it, you break your flow, and half the time you just don't bother.

- Classification at capture time taxes the moment of thought: "maintaining more than one note and managing and sorting them into folders and recursive substructures costs way too much cognitive bloat" (Karpathy). Capture exists to offload working memory, not to archive.
- Structure is still needed, but it only pays off where knowledge is *reused*. Karpathy's own llm-wiki pattern reintroduces full atomization and cross-linking at the compilation stage, after messy capture.
- Deferring structure defers *judgment* to the right gate: capture broadly with provenance, then let a review step (primary sources, independent corroboration) decide what deserves atomization, filtering and structuring in one reviewed pass.
- Unrescued items sinking to the bottom is a feature, not a loss. Periodic review (scroll, re-read, triage) surfaces what still matters, and the rest decays without upkeep cost.

**How to apply**
- Give each contributor one low-friction capture surface (an inbox folder, an append-only note) and record provenance. Nothing else is mandated at capture time.
- Never load capture files with structure obligations like schemas, backlinks, or taxonomies; those belong to the synthesis gate.
- Schedule the triage loop. Capture without periodic review becomes a write-only landfill.
- Resist the urge to "organize the inbox": sorting pre-validated material is wasted labor on items that may never clear the gate.

Go deeper: [LLM-legible knowledge base](llm-legible-knowledge-base.md)

## Sources
- Karpathy, "The Append-and-Review Note", 2025-03-19 - https://karpathy.bearblog.dev/the-append-and-review-note/. Confirms append-to-top capture, no folders ("cognitive bloat"), review-by-scrolling, rescue-by-copy-paste.
- Karpathy, "llm-wiki", 2026-04-04 - https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f. Confirms atomization/cross-linking applied at compilation, not capture.
