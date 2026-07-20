---
verified_on: 2026-07-03
stale_after: 2026-10-03
sources:
  - https://platform.claude.com/docs/en/build-with-claude/prompt-caching
  - https://platform.openai.com/docs/guides/prompt-caching
---
# Prompt-cache hygiene

**Keep an agent's stable prefix (system prompt, tool schemas, file and context history) append-only and byte-identical turn to turn, so the cache actually hits instead of silently re-billing at full price.**

Add one handy new tool halfway through a long session and that single schema change busts the cached prefix above it: the next turn re-bills your whole system prompt and history at full price, with no error, just a quietly larger invoice.

- A cache read is billed at roughly 0.1x base input (about 90% off) on both major providers, and it pays for itself after one read on the 5-minute tier or two on the 1-hour tier.
- Anthropic invalidates along a hierarchy (`tools → system → messages`) where any change busts that level and everything below it; editing one tool schema mid-session re-writes the entire cached prefix.
- A per-request timestamp or nonce placed *before* the cache breakpoint silently changes the prefix hash and misses, with no error returned; the fix is putting the breakpoint on the last identical block.
- TTL is a sliding, inactivity-based window that resets for free on every hit, so a continuously active session never re-pays the write premium. Only a genuine idle gap expires it.
- Both major vendors expose cache-read, cache-creation, and plain-input token counts on every response, so hit rate and overpay are directly computable, not estimated.

**How to apply**
- Freeze the tool and schema set for the session: don't add, remove, or reorder tool definitions mid-session.
- Put any per-request timestamp, nonce, or session ID *after* the cache breakpoint, never before it.
- Keep the system prompt and message ordering stable across turns.
- Watch for a prefix that falls below the model's minimum cacheable length: it silently never caches, with no error surfaced.
- Track cache-read vs cache-creation vs uncached-input tokens per session to compute hit rate and the dollar cost of avoidable misses.

Go deeper: [Cache economics & whole-bill anatomy](../concepts/cache-economics-and-whole-bill-anatomy.md) · [Whole-bill measurement](whole-bill-measurement.md)

## Sources
- https://platform.claude.com/docs/en/build-with-claude/prompt-caching
- https://platform.openai.com/docs/guides/prompt-caching
