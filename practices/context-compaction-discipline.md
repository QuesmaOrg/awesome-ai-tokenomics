---
verified_on: 2026-07-03
stale_after: 2026-10-03
sources:
  - https://github.com/openai/codex/issues/16812
  - https://barazany.dev/blog/claude-codes-compaction-engine
  - https://platform.claude.com/docs/en/build-with-claude/context-editing
  - https://arxiv.org/abs/2606.23525
---
# Context-compaction discipline

**Treat compaction as a costed operation with its own failure mode, not a free safety valve. Measure whether a given compaction policy saves tokens or triggers a re-read loop that spends more than it recovers.**

Tighten the compaction threshold to keep sessions under budget, and a week later identical tasks can cost *more*, because every compaction now evicts files the agent immediately re-reads.

- Compaction works around a real capability limit (finite, degrading context), but *how* a harness compacts is pure harness design, so the same policy can flip from a savings lever to a cost multiplier.
- A documented regression shows this concretely: retuning a compaction threshold to fire more often took one harness from 4 compactions per session to 12–26, and total tokens for identical tasks from 89M to 160–185M: roughly 2x the bill for the same model on the same task.
- The cause was a file-re-read amplification loop: compaction evicts file contents, the agent re-reads them to continue, context fills again, and compaction fires again.
- Each compaction is itself a paid summarization call, and multiple rounds cause cumulative information loss that can make the model less accurate, not just costlier.
- Compaction also fights the prompt cache: editing or evicting history invalidates the cached prefix, so a compaction event and a cache-write premium can compound in the same turn.
- Offline research shows roughly 40–60% of input tokens are removable at flat accuracy in one measured case, so an aggressive-but-untargeted policy still leaves a real prize on the table even when it isn't actively regressing.
- **Caveat:** no tool prices a given harness's compaction policy per live session, so the failure mode above can ship silently in a point release.

**How to apply**
- Instrument compaction frequency and post-compaction token volume per session: a rising ratio of tokens to useful turns after a policy change is the re-read-loop signature.
- Before tightening a threshold, check whether the harness re-reads evicted files to continue; if it does, a more aggressive threshold will likely raise total spend, not lower it.
- Prune genuinely stale or unreferenced content rather than blind-summarizing the whole history.
- Track how compaction hits the prompt cache: it resets the cached prefix and triggers a fresh cache-write premium.
- Re-verify the policy after any harness upgrade; the sharpest regression documented here shipped in a routine point release, not a deliberate redesign.

Go deeper: [Compaction economics](../concepts/compaction-economics.md) · [Prompt-cache hygiene](prompt-cache-hygiene.md)

## Sources
- https://github.com/openai/codex/issues/16812
- https://barazany.dev/blog/claude-codes-compaction-engine
- https://platform.claude.com/docs/en/build-with-claude/context-editing
- https://arxiv.org/abs/2606.23525
