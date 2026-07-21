# Optimize

## Caching

### Tools
- [GPTCache](https://github.com/zilliztech/GPTCache) - An open-source semantic cache returning a stored LLM response for a paraphrased repeat query via vector search, skipping the paid call. ![tool: MIT](https://img.shields.io/badge/tool-MIT-blue?style=flat-square) ![stars](https://img.shields.io/github/stars/zilliztech/GPTCache?style=flat-square&logo=github&label=) ![last commit](https://img.shields.io/github/last-commit/zilliztech/GPTCache?style=flat-square&label=)
- [khazad](https://github.com/GuglielmoCerri/khazad) - A transport-layer semantic cache for LLM APIs on Redis 8 Vector Sets: it intercepts HTTP traffic with zero application code changes and replays cached responses… ![tool: MIT](https://img.shields.io/badge/tool-MIT-blue?style=flat-square) ![stars](https://img.shields.io/github/stars/GuglielmoCerri/khazad?style=flat-square&logo=github&label=) ![last commit](https://img.shields.io/github/last-commit/GuglielmoCerri/khazad?style=flat-square&label=)
- [prompt-cache](https://github.com/messkan/prompt-cache) - A Go LLM proxy that adds a three-tier semantic cache: high similarity hits directly, low skips, and a gray zone runs a cheap verification model to guard against… ![tool: MIT](https://img.shields.io/badge/tool-MIT-blue?style=flat-square) ![stars](https://img.shields.io/github/stars/messkan/prompt-cache?style=flat-square&logo=github&label=) ![last commit](https://img.shields.io/github/last-commit/messkan/prompt-cache?style=flat-square&label=)
- [Redis LangCache](https://redis.io/langcache/) - Redis's fully-managed semantic cache: a REST API that returns a stored response when a new query is similar to a past one, so paraphrases skip the paid LLM… ![tool: proprietary](https://img.shields.io/badge/tool-proprietary-blue?style=flat-square)

## Cheap Local Models

### Tools
- [llama.cpp](https://github.com/ggml-org/llama.cpp) - The foundational open-source (MIT) local LLM inference engine most of the local ecosystem runs on, with an OpenAI-compatible server built in. ![tool: MIT](https://img.shields.io/badge/tool-MIT-blue?style=flat-square) ![stars](https://img.shields.io/github/stars/ggml-org/llama.cpp?style=flat-square&logo=github&label=) ![last commit](https://img.shields.io/github/last-commit/ggml-org/llama.cpp?style=flat-square&label=)
- [Ollama](https://github.com/ollama/ollama) - The de facto runtime for running open-weight models like Qwen, DeepSeek, and GLM-5.1 locally, shifting inference onto hardware you already own. ![tool: MIT](https://img.shields.io/badge/tool-MIT-blue?style=flat-square) ![stars](https://img.shields.io/github/stars/ollama/ollama?style=flat-square&logo=github&label=) ![last commit](https://img.shields.io/github/last-commit/ollama/ollama?style=flat-square&label=)

## Context Engineering

### Tools
- [Context Mode - MCP server that sandboxes tool output out of the context window](https://github.com/mksglu/context-mode) - This MCP server sandboxes tool calls and returns only the distilled result, claiming a 98% cut: 315 KB of output down to 5.4 KB. ![tool: Elastic-2.0](https://img.shields.io/badge/tool-Elastic--2.0-blue?style=flat-square) ![stars](https://img.shields.io/github/stars/mksglu/context-mode?style=flat-square&logo=github&label=) ![last commit](https://img.shields.io/github/last-commit/mksglu/context-mode?style=flat-square&label=)
- [headroom - the context-compression genre's mega-anchor (quality story dissected)](https://github.com/headroomlabs-ai/headroom) - An Apache-2.0 context-compression tool for LLM/agent pipelines, the category's largest repo, confirmed organic by star-forensics. ![tool: Apache-2.0](https://img.shields.io/badge/tool-Apache--2.0-blue?style=flat-square) ![stars](https://img.shields.io/github/stars/headroomlabs-ai/headroom?style=flat-square&logo=github&label=) ![last commit](https://img.shields.io/github/last-commit/headroomlabs-ai/headroom?style=flat-square&label=)
- [LLMLingua](https://github.com/microsoft/LLMLingua) - Microsoft's prompt-compression library that uses a small model to drop low-information tokens before a prompt reaches the target LLM. ![tool: MIT](https://img.shields.io/badge/tool-MIT-blue?style=flat-square) ![stars](https://img.shields.io/github/stars/microsoft/LLMLingua?style=flat-square&logo=github&label=) ![last commit](https://img.shields.io/github/last-commit/microsoft/LLMLingua?style=flat-square&label=)
- [llmtrim](https://github.com/fkiene/llmtrim) - A local proxy that compresses a coding agent's prompt, tool schemas, and history before forwarding, and can reroute Claude calls to Grok. ![tool: MPL-2.0](https://img.shields.io/badge/tool-MPL--2.0-blue?style=flat-square) ![stars](https://img.shields.io/github/stars/fkiene/llmtrim?style=flat-square&logo=github&label=) ![last commit](https://img.shields.io/github/last-commit/fkiene/llmtrim?style=flat-square&label=)
- [Repomix](https://github.com/yamadashy/repomix) - Packs an entire repository into a single AI-friendly file, reporting token counts and using Tree-sitter to compress code to signatures only. ![tool: MIT](https://img.shields.io/badge/tool-MIT-blue?style=flat-square) ![stars](https://img.shields.io/github/stars/yamadashy/repomix?style=flat-square&logo=github&label=) ![last commit](https://img.shields.io/github/last-commit/yamadashy/repomix?style=flat-square&label=)
- [rtk - the context-compression genre's largest adoption anchor (reduction-only headline)](https://github.com/rtk-ai/rtk) - rtk is a single-binary Rust CLI proxy that intercepts and compresses the output of common dev commands before it reaches an LLM coding agent's context window. ![tool: Apache-2.0](https://img.shields.io/badge/tool-Apache--2.0-blue?style=flat-square) ![stars](https://img.shields.io/github/stars/rtk-ai/rtk?style=flat-square&logo=github&label=) ![last commit](https://img.shields.io/github/last-commit/rtk-ai/rtk?style=flat-square&label=)
- [Serena](https://github.com/oraios/serena) - An open-source (MIT) MCP toolkit that gives a coding agent IDE-grade semantic code retrieval and editing: 'the IDE for your coding agent'. ![tool: MIT](https://img.shields.io/badge/tool-MIT-blue?style=flat-square) ![stars](https://img.shields.io/github/stars/oraios/serena?style=flat-square&logo=github&label=) ![last commit](https://img.shields.io/github/last-commit/oraios/serena?style=flat-square&label=)

### Research & Benchmarks
- [AgentDiet - trajectory reduction ("Reducing Cost of LLM Agents with Trajectory Reduction")](https://arxiv.org/abs/2509.23586) - AgentDiet is an inference-time module that strips useless, redundant, and expired information from an agent's trajectory, without hurting performance. ![paper](https://img.shields.io/badge/paper-555?style=flat-square)
- [Context Rot - LLM performance degrades as input length grows](https://www.trychroma.com/research/context-rot) - This is Chroma's controlled study of how LLM output quality changes as input length grows, holding task difficulty fixed. ![report](https://img.shields.io/badge/report-555?style=flat-square)
- [ContextBudget - context management as a budget-constrained sequential decision](https://arxiv.org/abs/2604.01664) - ContextBudget's BACM method has an agent decide when and how much to compress its history based on remaining context budget, not a fixed rule. ![paper](https://img.shields.io/badge/paper-555?style=flat-square)
- [Minification of state-in-context agents - the clean waste-vs-capability datapoint](https://arxiv.org/abs/2606.01326) - This ICPC 2026 study found that minifying code in a coding agent's context cuts input tokens by 42% but costs 12 percentage points of accuracy. ![paper](https://img.shields.io/badge/paper-555?style=flat-square)
- [RULER - the "real context size" long-context benchmark](https://github.com/NVIDIA/RULER) - NVIDIA's RULER benchmark found that of models claiming 32K+ token context windows, only half actually maintain quality once you fill them to 32K. ![bench](https://img.shields.io/badge/bench-555?style=flat-square) ![stars](https://img.shields.io/github/stars/NVIDIA/RULER?style=flat-square&logo=github&label=) ![last commit](https://img.shields.io/github/last-commit/NVIDIA/RULER?style=flat-square&label=)
- [Self-Compacting Language Model Agents](https://arxiv.org/abs/2606.23525) - This paper introduces SELFCOMPACT: instead of fixed-interval summarization, the model itself decides when and how to compress a growing agent trace. ![paper](https://img.shields.io/badge/paper-555?style=flat-square)

### Reading
- [Anthropic vendor-native context management (context editing + memory tool + server-side compaction)](https://platform.claude.com/docs/en/build-with-claude/context-editing) - Anthropic's context editing, memory tool, and server-side compaction cut token consumption by a vendor-reported 84% in a 100-turn web-search evaluation.
- [Claude Code compaction engine - the three-tier mechanism and its cache/correctness failure modes](https://barazany.dev/blog/claude-codes-compaction-engine) - Claude Code's *harness* - not the API - decides how to trim a filling context window, and it does this through a three-tier compaction engine.
- [Codex CLI compaction cost - over-eager compaction as a token-amplification loop](https://github.com/openai/codex/issues/16812) - Upgrading Codex CLI from v0.116 to v0.118 made context compaction fire twice as often, doubling or tripling token consumption for identical tasks.
- [Cursor vendor-native context management - dynamic context discovery + Composer self-summarization](https://cursor.com/blog/dynamic-context-discovery) - Cursor's dynamic context discovery loads tool schemas and large outputs on demand instead of eagerly, a change the vendor reports cut context usage by 46.9%.
- [Karpathy's LLM Wiki](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) - Andrej Karpathy's LLM Wiki pattern has an agent build and maintain a persistent markdown wiki from your sources, instead of re-retrieving raw files.

## Cost Controls

### Reading
- [Harness-side runaway-loop cost guardrails (Claude Code + Codex, July 2026)](https://github.com/anthropics/claude-code/releases/tag/v2.1.212) - In mid-July 2026 both dominant coding CLIs shipped first-party guardrails against runaway agent loops within days of each other.

## Gateways And Proxies

### Tools
- [Bifrost (Maxim AI)](https://github.com/maximhq/bifrost) - Bifrost is a Go-based AI gateway fronting 1000+ models that measured just 11 microseconds of added latency per request at 5,000 requests per second. ![tool: Apache-2.0](https://img.shields.io/badge/tool-Apache--2.0-blue?style=flat-square) ![stars](https://img.shields.io/github/stars/maximhq/bifrost?style=flat-square&logo=github&label=) ![last commit](https://img.shields.io/github/last-commit/maximhq/bifrost?style=flat-square&label=)
- [Cloudflare AI Gateway (Spend Limits)](https://developers.cloudflare.com/ai-gateway/features/spend-limits/) - Cloudflare AI Gateway is an edge-native LLM proxy that added dollar-denominated spend limits in June 2026, blocking or rerouting requests once a budget is hit. ![co](https://img.shields.io/badge/co-555?style=flat-square)
- [Helicone](https://helicone.ai) - An open-source (Apache-2.0) LLM proxy that logs every request's cost, latency, and tokens in one line of code; Mintlify acquired it in March 2026. ![tool: Apache-2.0](https://img.shields.io/badge/tool-Apache--2.0-blue?style=flat-square)
- [Kong AI Gateway](https://developer.konghq.com/ai-gateway/) - The AI layer of Kong's API-gateway platform: a proxy that meters LLM/agent/MCP traffic for billing, showback, and chargeback. ![co](https://img.shields.io/badge/co-555?style=flat-square)
- [LiteLLM](https://github.com/BerriAI/litellm) - An open-source gateway fronting 100+ LLM APIs that computes real per-request dollar cost from a live pricing map, with spend limits. ![tool: MIT](https://img.shields.io/badge/tool-MIT-blue?style=flat-square) ![stars](https://img.shields.io/github/stars/BerriAI/litellm?style=flat-square&logo=github&label=) ![last commit](https://img.shields.io/github/last-commit/BerriAI/litellm?style=flat-square&label=)
- [OpenRouter](https://openrouter.ai/docs/guides/routing/provider-selection) - A unified API gateway fronting 400+ models across 70+ providers that auto-routes each request by price, with fallback on outages. ![co](https://img.shields.io/badge/co-555?style=flat-square)
- [Portkey AI Gateway](https://portkey.ai/docs/product/ai-gateway/virtual-keys/budget-limits) - Routes LLM traffic across providers and enforces hard USD budget limits on virtual keys, auto-expiring a key once its cap is hit. ![co](https://img.shields.io/badge/co-555?style=flat-square)

## Memory

### Tools
- [claude-code-memory-setup](https://github.com/lucasrosati/claude-code-memory-setup) - A practitioner recipe pairing an Obsidian memory vault with a local AST code-graph tool; the author self-reports up to 71.5x fewer tokens per Claude Code… ![tool: MIT](https://img.shields.io/badge/tool-MIT-blue?style=flat-square) ![stars](https://img.shields.io/github/stars/lucasrosati/claude-code-memory-setup?style=flat-square&logo=github&label=) ![last commit](https://img.shields.io/github/last-commit/lucasrosati/claude-code-memory-setup?style=flat-square&label=)
- [claude-mem](https://github.com/thedotmack/claude-mem) - A coding-agent observational-memory layer that captures every session, compresses it with AI, and re-injects relevant context next time; self-reports ~10x token… ![tool: Apache-2.0](https://img.shields.io/badge/tool-Apache--2.0-blue?style=flat-square) ![stars](https://img.shields.io/github/stars/thedotmack/claude-mem?style=flat-square&logo=github&label=) ![last commit](https://img.shields.io/github/last-commit/thedotmack/claude-mem?style=flat-square&label=)
- [LangMem](https://github.com/langchain-ai/langmem) - LangChain's long-term memory library: it extracts and consolidates facts from conversations and integrates natively with LangGraph's memory store, so agents… ![tool: MIT](https://img.shields.io/badge/tool-MIT-blue?style=flat-square) ![stars](https://img.shields.io/github/stars/langchain-ai/langmem?style=flat-square&logo=github&label=) ![last commit](https://img.shields.io/github/last-commit/langchain-ai/langmem?style=flat-square&label=)
- [Letta (MemGPT)](https://github.com/letta-ai/letta) - The MemGPT lineage project: a platform for stateful agents that pages an LLM's context like an OS, keeping working memory small and moving the rest to archival… ![tool: Apache-2.0](https://img.shields.io/badge/tool-Apache--2.0-blue?style=flat-square) ![stars](https://img.shields.io/github/stars/letta-ai/letta?style=flat-square&logo=github&label=) ![last commit](https://img.shields.io/github/last-commit/letta-ai/letta?style=flat-square&label=)
- [Supermemory](https://github.com/supermemoryai/supermemory) - A memory and context engine that self-reports 95% recall on LongMemEval while adding only ~720 tokens of context, a claimed 99.4% context reduction versus full… ![tool: MIT](https://img.shields.io/badge/tool-MIT-blue?style=flat-square) ![stars](https://img.shields.io/github/stars/supermemoryai/supermemory?style=flat-square&logo=github&label=) ![last commit](https://img.shields.io/github/last-commit/supermemoryai/supermemory?style=flat-square&label=)
- [Zep / Graphiti](https://www.getzep.com/) - A memory platform for agents built on temporal knowledge graphs; it self-reports serving benchmark answers from a few thousand tokens of retrieved context… (also: [Graphiti (OSS engine)](https://github.com/getzep/graphiti) · [zep repo](https://github.com/getzep/zep)) ![tool: Apache-2.0](https://img.shields.io/badge/tool-Apache--2.0-blue?style=flat-square)

## Multi Agent Overhead

### Research & Benchmarks
- [SupervisorAgent - "Stop Wasting Your Tokens" (runtime supervision)](https://arxiv.org/abs/2510.26585) - SupervisorAgent is a lightweight, modular framework for runtime, adaptive supervision of multi-agent systems. ![paper](https://img.shields.io/badge/paper-555?style=flat-square)

### Reading
- [Framework orchestration overhead (the manager-LLM tax)](https://docs.crewai.com/en/learn/hierarchical-process) - Hierarchical frameworks like CrewAI add a manager-LLM delegation tax, an extra model that plans and validates, though its cost is unquantified in any primary.

## Prompt Agent Loop

### Tools
- [token-ninja](https://github.com/oanhduong/token-ninja) - Intercepts deterministic commands like git status or npm test before they reach the model, running them locally and skipping the LLM call. ![tool: MIT](https://img.shields.io/badge/tool-MIT-blue?style=flat-square) ![stars](https://img.shields.io/github/stars/oanhduong/token-ninja?style=flat-square&logo=github&label=) ![last commit](https://img.shields.io/github/last-commit/oanhduong/token-ninja?style=flat-square&label=)

### Research & Benchmarks
- [LOOP Skill Engine](https://arxiv.org/abs/2605.14237) - LOOP records an agent's first run of a repetitive task with full LLM reasoning, then replays the extracted tool-call template without calling the LLM again. ![paper](https://img.shields.io/badge/paper-555?style=flat-square)

### Reading
- [Orchestrator-worker model tiering (frontier plans / cheap executes)](https://www.mindstudio.ai/blog/smart-orchestrator-cheaper-sub-agent-models-claude-code) - A capable model plans while cheaper agents execute; the pattern now ships as a vendor default, hitting 89.7% of LLM quality at 4% of the cost.

## Prompt Technique

### Tools
- [TOON (Token-Oriented Object Notation)](https://github.com/toon-format/toon) - TOON is a compact, human-readable, lossless serialization of the JSON data model, designed for LLM input. ![tool: MIT](https://img.shields.io/badge/tool-MIT-blue?style=flat-square) ![stars](https://img.shields.io/github/stars/toon-format/toon?style=flat-square&logo=github&label=) ![last commit](https://img.shields.io/github/last-commit/toon-format/toon?style=flat-square&label=)

## Retrieval Memory

### Tools
- [Cognee](https://github.com/topoteretes/cognee) - An open-source (Apache-2.0) AI-memory platform giving agents persistent memory via a self-hosted knowledge graph, via remember/recall/forget. ![tool: Apache-2.0](https://img.shields.io/badge/tool-Apache--2.0-blue?style=flat-square) ![stars](https://img.shields.io/github/stars/topoteretes/cognee?style=flat-square&logo=github&label=) ![last commit](https://img.shields.io/github/last-commit/topoteretes/cognee?style=flat-square&label=)
- [Mem0](https://github.com/mem0ai/mem0) - An open-source memory layer that extracts salient facts from conversations and retrieves only the relevant ones per call, not the full history. ![tool: Apache-2.0](https://img.shields.io/badge/tool-Apache--2.0-blue?style=flat-square) ![stars](https://img.shields.io/github/stars/mem0ai/mem0?style=flat-square&logo=github&label=) ![last commit](https://img.shields.io/github/last-commit/mem0ai/mem0?style=flat-square&label=)

## Retry And Reliability

### Reading
- [Claude Code v2.1.199 - transient-retry hardening & partial-output preservation](https://github.com/anthropics/claude-code/releases/tag/v2.1.199) - Claude Code v2.1.199 now auto-retries rate-limit errors with backoff and raised the default retry ceiling to 300, up from a prior cap of 15.

## Routing Model Selection

### Tools
- [Not Diamond](https://www.notdiamond.ai/) - Not Diamond's meta-model predicts, per input, which LLM will give the best answer at the lowest cost, then routes the request there. ![co](https://img.shields.io/badge/co-555?style=flat-square)
- [OpenCode - open-source coding-agent CLI with explicit cost-tier routing](https://opencode.ai/docs/) - OpenCode is an open-source (MIT) coding-agent CLI with its own explicit cost- and model-routing configuration, set directly in config. ![tool: MIT](https://img.shields.io/badge/tool-MIT-blue?style=flat-square)
- [RouteLLM](https://github.com/lm-sys/RouteLLM) - LMSYS's open-source router sending each query to a cheap or expensive model based on a trained cost threshold, as a drop-in server. ![tool: Apache-2.0](https://img.shields.io/badge/tool-Apache--2.0-blue?style=flat-square) ![stars](https://img.shields.io/github/stars/lm-sys/RouteLLM?style=flat-square&logo=github&label=) ![last commit](https://img.shields.io/github/last-commit/lm-sys/RouteLLM?style=flat-square&label=)
- [ruflo (formerly Claude-Flow; npm `claude-flow` v3.17.0) - agent meta-harness with cost-adjusted model routing](https://github.com/ruvnet/ruflo) - ruflo is the leading open-source agent meta-harness for Claude Code and Codex, providing swarm orchestration and persistent memory. ![tool: MIT](https://img.shields.io/badge/tool-MIT-blue?style=flat-square) ![stars](https://img.shields.io/github/stars/ruvnet/ruflo?style=flat-square&logo=github&label=) ![last commit](https://img.shields.io/github/last-commit/ruvnet/ruflo?style=flat-square&label=)
- [vLLM Semantic Router](https://github.com/vllm-project/semantic-router) - Sends routine queries to cheap or local models and hard ones to stronger backends, as an open-source, self-hostable router. ![tool: Apache-2.0](https://img.shields.io/badge/tool-Apache--2.0-blue?style=flat-square) ![stars](https://img.shields.io/github/stars/vllm-project/semantic-router?style=flat-square&logo=github&label=) ![last commit](https://img.shields.io/github/last-commit/vllm-project/semantic-router?style=flat-square&label=)

### Research & Benchmarks
- [Cluster, Route, Escalate - cost-aware cascaded serving](https://arxiv.org/abs/2606.27457) - This paper proposes a two-stage cost-aware cascade for LLM serving that combines routing and escalation into one framework. ![paper](https://img.shields.io/badge/paper-555?style=flat-square)
- [MTRouter - per-turn cost-aware routing with history-model joint embeddings](https://arxiv.org/abs/2604.23530) - MTRouter picks a different model for each turn of a multi-turn conversation, rather than one model per query, to hit a cost budget without losing quality. ![paper](https://img.shields.io/badge/paper-555?style=flat-square)
- [OrcaRouter - production LinUCB bandit router (hybrid offline-online)](https://arxiv.org/abs/2605.30736) - OrcaRouter is a production LLM router built on a LinUCB bandit, with its cost/quality tradeoff independently confirmed on the RouterArena leaderboard. ![paper](https://img.shields.io/badge/paper-555?style=flat-square)

### Reading
- [Claude Code via a LiteLLM gateway (cheap-tier-in-front setup)](https://docs.litellm.ai/docs/tutorials/claude_non_anthropic_models) - Pointing Claude Code's ANTHROPIC_BASE_URL at a local LiteLLM proxy lets cheaper or non-Anthropic models absorb work the frontier model would otherwise bill for.
- [Distilling agent behavior into small task-specific models](https://arxiv.org/abs/2505.17612) - Distilling a large agent's behavior into a small 0.5-3B model lets most of its work run at a fraction of the frontier model's per-token cost.

## Serving Inference

### Tools
- [SGLang](https://github.com/sgl-project/sglang) - A high-performance serving framework for large language and multimodal models. ![tool: Apache-2.0](https://img.shields.io/badge/tool-Apache--2.0-blue?style=flat-square) ![stars](https://img.shields.io/github/stars/sgl-project/sglang?style=flat-square&logo=github&label=) ![last commit](https://img.shields.io/github/last-commit/sgl-project/sglang?style=flat-square&label=)
- [vLLM](https://github.com/vllm-project/vllm) - The canonical open-source LLM serving engine, using PagedAttention to manage KV-cache memory in blocks so more requests batch at lower cost. ![tool: Apache-2.0](https://img.shields.io/badge/tool-Apache--2.0-blue?style=flat-square) ![stars](https://img.shields.io/github/stars/vllm-project/vllm?style=flat-square&logo=github&label=) ![last commit](https://img.shields.io/github/last-commit/vllm-project/vllm?style=flat-square&label=)

### Research & Benchmarks
- [RLM-Cascade - response-level speculative decoding at the gateway](https://arxiv.org/abs/2606.22840) - RLM-Cascade, from a PayPal team, has a cheap draft model answer first and an Opus 4.8 verifier accept or rewrite it, at roughly 2% of Opus's cost. ![paper](https://img.shields.io/badge/paper-555?style=flat-square)

## Test Time Compute

### Research & Benchmarks
- [Stop When Reasoning Converges](https://arxiv.org/abs/2605.17672) - Reasoning models often keep generating steps after a solution has already stabilized, wasting tokens and adding latency - what this paper calls "overthink.". ![paper](https://img.shields.io/badge/paper-555?style=flat-square)
- [When more reasoning hurts - the test-time-compute ceiling](https://arxiv.org/abs/2604.10739) - Two 2026 papers found giving a model more reasoning budget makes it perform worse and cost more; past a point, tool delegation wins outright. ![paper](https://img.shields.io/badge/paper-555?style=flat-square)

## Tool Protocol Overhead

### Research & Benchmarks
- [MCP Tool Descriptions Are Smelly!](https://arxiv.org/abs/2602.14878) - This study found poorly-written MCP tool descriptions measurably hurt agent efficiency, using an LLM-jury scanner and an A/B protocol on MCP-Universe. ![paper](https://img.shields.io/badge/paper-555?style=flat-square)
- [Tool Attention Is All You Need](https://arxiv.org/abs/2604.21816) - MCP re-sends every tool's full schema on every turn, whether or not the agent needs it - a protocol tax known as the MCP/Tools Tax. ![paper](https://img.shields.io/badge/paper-555?style=flat-square)

### Reading
- [Code execution with MCP (Anthropic)](https://www.anthropic.com/engineering/code-execution-with-mcp) - Anthropic proposes agents call MCP servers by writing and executing code instead of a tool call per step, so unused tool schemas skip the context window.
