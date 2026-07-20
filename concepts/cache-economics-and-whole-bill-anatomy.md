---
verified_on: 2026-07-01
stale_after: 2026-10-01
sources:
  - https://platform.claude.com/docs/en/build-with-claude/prompt-caching
  - https://platform.claude.com/docs/en/about-claude/pricing
  - https://developers.openai.com/api/docs/guides/prompt-caching
  - https://github.com/BerriAI/litellm
  - https://www.vaudit.com/
  - https://github.com/kenn-io/agentsview
---
# Cache economics & whole-bill anatomy

**Prompt caching cuts the price of unchanged context by roughly 10x, but a true "whole bill" also has to count cache-writes, non-token compute, and every subagent's full context re-send, none of which a token-only meter sees.**

An agent re-sends the same large block of context (system prompt, tool definitions, the files it's looking at) on almost every turn. Prompt caching lets a provider store that block and charge far less each time it comes back unchanged. This is the most legible dollar lever in an agentic-coding bill, though only one piece of the true accounting.

**1. The cache spread** (Anthropic, Opus 4.8 at $5/MTok input as the worked example):

| State | Multiplier | Price |
|---|---|---|
| Uncached input | 1.0x | $5.00/MTok |
| Cache write (5-min) | 1.25x | $6.25/MTok |
| Cache write (1-hour) | 2.0x | $10.00/MTok |
| Cache read (hit) | 0.1x | $0.50/MTok |

OpenAI collapses this to a flat 0.1x (90% off) with no separate write charge. A cache pays off after one read on the 5-minute tier, or two reads on the 1-hour tier. Worked example: a 1-hour Opus session with 40k of 50k input tokens as cache reads drops the token bill from $0.705 to $0.525: the cached slice costs $0.02 instead of $0.20.

**2. What breaks the cache.** Anthropic invalidates along a `tools → system → messages` hierarchy: a change at one level busts that level and everything below it. Reordering, adding, or editing one tool schema mid-session re-writes the *entire* cached prefix. A timestamp or nonce placed *before* the cache breakpoint silently misses, with no error. A prefix below the model minimum (1,024 tokens for Opus 4.8/Sonnet 5; 4,096 for Opus 4.5/Haiku 4.5; 512 for Fable 5) is processed without caching and no error is returned. TTL is a sliding, inactivity-based window that resets on every hit. Only a genuine idle gap expires it.

**3. What a token-only meter misses.** Tool-use overhead bills the tool schemas themselves (e.g. ~290 tokens for one provider's auto tool-choice system prompt, up to ~804 for another mode, plus per-tool tokens: bash +245, text-editor +700, computer-use +735). Server-side compute is billed outside tokens entirely: web search at $10 per 1,000 searches, code-execution containers at $0.05/container-hour after 1,550 free hours/month, and one vendor's managed-agent session runtime at $0.08/session-hour (a pure wall-clock charge). The real bill is the sum over the *entire* trajectory tree (retries, tool round-trips, every subagent's own context re-send), reconciled against the actual invoice, not recomputed from token counts alone.

Go deeper: [Whole-bill reconciliation](whole-bill-reconciliation.md) · [Harness-waste taxonomy](harness-waste-taxonomy.md) · [Prompt-cache hygiene practice](../practices/prompt-cache-hygiene.md)

## Sources
- Anthropic, Prompt caching - https://platform.claude.com/docs/en/build-with-claude/prompt-caching (verified 2026-07-01)
- Anthropic, Pricing - https://platform.claude.com/docs/en/about-claude/pricing (verified 2026-07-01)
- OpenAI, Prompt caching - https://developers.openai.com/api/docs/guides/prompt-caching (verified 2026-07-01)
- LiteLLM - https://github.com/BerriAI/litellm
- Vaudit - https://www.vaudit.com/
- Cross-vendor usage trackers (AgentsView) - https://github.com/kenn-io/agentsview
