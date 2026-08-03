---
verified_on: 2026-08-03
stale_after: 2026-11-01
sources:
  - https://www.anthropic.com/engineering/code-execution-with-mcp
  - https://arxiv.org/abs/2607.12161
  - https://arxiv.org/abs/2604.21816
  - https://blog.jetbrains.com/ai/2026/07/rtk-claude-code-token-savings/
---
# Retrieval-boundary compression

**Never let raw external content - web pages, command output, tool payloads, tool schemas - cross into the model's context window. Distill it at the boundary, before it arrives, and do it without touching the cached prefix already sitting in context.**

A web-search call returns the whole page when you asked for one fact. An MCP server hands over 40 tool schemas whether or not this turn needs them. Both land as tokens the model has to read before it can do anything useful with them.

- The classic MCP pattern puts every tool's schema in context up front and re-sends it every turn, regardless of relevance - the tax is paid before the model reasons at all ([Tool Attention Is All You Need](https://arxiv.org/abs/2604.21816)).
- Discovering and loading only what's needed is a working fix at the schema layer: Anthropic's code-execution pattern has the agent explore a tool filesystem and read only the files it needs, so unused schemas never enter the window ([code execution with MCP](https://www.anthropic.com/engineering/code-execution-with-mcp)).
- The same logic applies to tool output: run the call in a sandbox and return only the distilled result - five rows instead of ten thousand - so the raw payload never enters context at all.
- For web retrieval, the boundary can be contractual: search APIs that return capped snippets, query-scoped highlights, or page-to-markdown conversion instead of raw HTML. The condensation step has its own price per query or per page - you are paying to save tokens, not getting the cut for free.
- The caveat that changes how you implement this: the boundary has to sit *before* content enters context, not as a rewrite of a prefix already cached. Cache reads are billed at roughly 90% off and dominate agentic bills, so compression that disturbs an already-cached prefix can raise the bill even as it cuts tokens - one measured arm removed 38% of tool-output tokens and cost 6.8% more ([Token Reduction Is Not Cost Reduction](https://arxiv.org/abs/2607.12161)).
- Don't take a compressor's own reduction number at face value. One command-output compressor's published 60-90% savings are reduction-vs-verbose-baseline with no quality gate; the one independent, quality-controlled A/B test found it net cost-negative at low reasoning effort and cost-neutral at high ([JetBrains A/B](https://blog.jetbrains.com/ai/2026/07/rtk-claude-code-token-savings/)).

**How to apply**

- Route every external call - web fetch, search, shell command, MCP tool - through a boundary layer that returns only the distilled result, never the raw payload.
- Load tool schemas on demand (progressive disclosure) instead of injecting the full catalog up front and re-sending it every turn.
- For tool output, execute in a sandbox and return the filtered answer - the extracted rows, the computed value - not the full response object.
- For web and search retrieval, prefer an API that returns condensed, ready-to-use results over ingesting raw HTML, and price the per-query cost against the token savings.
- Do the distillation before content enters context, never as a rewrite of the existing cached prefix - check where a compressor's reduction actually lands (new tokens vs cached tokens) before trusting it against the bill.
- Don't trust a compression tool's own reduction-vs-baseline number as a cost claim. Ask whether it has been measured with a quality-controlled ON/OFF test against the actual bill, not just a byte count.
- Measure fixed per-turn scaffolding too - system prompt and tool schemas are paid on every turn, independent of what the task actually needs.

## Sources
- https://www.anthropic.com/engineering/code-execution-with-mcp
- https://arxiv.org/abs/2607.12161
- https://arxiv.org/abs/2604.21816
- https://blog.jetbrains.com/ai/2026/07/rtk-claude-code-token-savings/
