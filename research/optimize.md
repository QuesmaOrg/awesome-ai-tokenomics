# Optimize

## Caching

### Tools
- [LMCache](https://github.com/LMCache/LMCache) - Self-hosted KV-cache layer beneath vLLM that gives token-level cache-hit observability for teams that own their GPUs. ![tool: Apache-2.0](https://img.shields.io/badge/tool-Apache--2.0-blue?style=flat-square) ![last commit](https://img.shields.io/github/last-commit/LMCache/LMCache?style=flat-square&label=)
- [prompt-cache](https://github.com/messkan/prompt-cache) - Go LLM proxy with a three-tier semantic cache that uses a cheap verification model for borderline similarity matches. ![tool: MIT](https://img.shields.io/badge/tool-MIT-blue?style=flat-square) ![last commit](https://img.shields.io/github/last-commit/messkan/prompt-cache?style=flat-square&label=)
- [Redis LangCache](https://redis.io/langcache/) - Managed semantic cache with a REST API that returns a stored response when a new query is similar to a past one. ![tool: proprietary](https://img.shields.io/badge/tool-proprietary-blue?style=flat-square)

## Cheap Local Models

### Tools
- [llama.cpp](https://github.com/ggml-org/llama.cpp) - Open-source (MIT) local LLM inference engine with a built-in OpenAI-compatible server. ![tool: MIT](https://img.shields.io/badge/tool-MIT-blue?style=flat-square) ![last commit](https://img.shields.io/github/last-commit/ggml-org/llama.cpp?style=flat-square&label=)
- [Magnitude](https://github.com/magnitudedev/magnitude) - Apache-2.0 local inference engine for agents, written in Rust, that tunes GPU kernels on the user's device and shares prefix caches across concurrent sessions; its maker reports 92% faster decode than llama.cpp on an M4 Pro. ![tool: Apache-2.0](https://img.shields.io/badge/tool-Apache--2.0-blue?style=flat-square) ![last commit](https://img.shields.io/github/last-commit/magnitudedev/magnitude?style=flat-square&label=)
- [Ollama](https://github.com/ollama/ollama) - Runtime for running open-weight models locally on hardware you already own. ![tool: MIT](https://img.shields.io/badge/tool-MIT-blue?style=flat-square) ![last commit](https://img.shields.io/github/last-commit/ollama/ollama?style=flat-square&label=)

## Compression

### Tools
- [Context Mode](https://github.com/mksglu/context-mode) - MCP server that sandboxes tool calls and returns only the distilled result to the model. ![tool: Elastic-2.0](https://img.shields.io/badge/tool-Elastic--2.0-blue?style=flat-square) ![last commit](https://img.shields.io/github/last-commit/mksglu/context-mode?style=flat-square&label=)
- [headroom](https://github.com/headroomlabs-ai/headroom) - Apache-2.0 context-compression tool for LLM and agent pipelines. ![tool: Apache-2.0](https://img.shields.io/badge/tool-Apache--2.0-blue?style=flat-square) ![last commit](https://img.shields.io/github/last-commit/headroomlabs-ai/headroom?style=flat-square&label=)
- [lean-ctx](https://github.com/yvgude/lean-ctx) - Rust MCP server that mediates what a coding agent reads, with a savings ledger and an accounting of its own context overhead. ![tool: Apache-2.0](https://img.shields.io/badge/tool-Apache--2.0-blue?style=flat-square) ![last commit](https://img.shields.io/github/last-commit/yvgude/lean-ctx?style=flat-square&label=)
- [LLMLingua](https://github.com/microsoft/LLMLingua) - Microsoft prompt-compression library that uses a small model to drop low-information tokens before a prompt reaches the target LLM. ![tool: MIT](https://img.shields.io/badge/tool-MIT-blue?style=flat-square) ![last commit](https://img.shields.io/github/last-commit/microsoft/LLMLingua?style=flat-square&label=)
- [llmtrim](https://github.com/fkiene/llmtrim) - Local proxy that compresses a coding agent's prompt, tool schemas, and history before forwarding, and can reroute Claude calls to Grok. ![tool: MPL-2.0](https://img.shields.io/badge/tool-MPL--2.0-blue?style=flat-square) ![last commit](https://img.shields.io/github/last-commit/fkiene/llmtrim?style=flat-square&label=)
- [rtk](https://github.com/rtk-ai/rtk) - Single-binary Rust CLI proxy that compresses the output of common dev commands before it reaches a coding agent's context window. ![tool: Apache-2.0](https://img.shields.io/badge/tool-Apache--2.0-blue?style=flat-square) ![last commit](https://img.shields.io/github/last-commit/rtk-ai/rtk?style=flat-square&label=)
- [snip](https://github.com/edouard-claude/snip) - Single-binary Go CLI proxy that filters dev-command output before it reaches a coding agent, using declarative YAML filter pipelines. ![tool: MIT](https://img.shields.io/badge/tool-MIT-blue?style=flat-square) ![last commit](https://img.shields.io/github/last-commit/edouard-claude/snip?style=flat-square&label=)
- [TOON](https://github.com/toon-format/toon) - Compact, human-readable, lossless serialization of the JSON data model, designed for LLM input. ![tool: MIT](https://img.shields.io/badge/tool-MIT-blue?style=flat-square) ![last commit](https://img.shields.io/github/last-commit/toon-format/toon?style=flat-square&label=)

### Research & Benchmarks
- [Minification of State-in-Context Agents](https://arxiv.org/abs/2606.01326) - ICPC 2026 study of minifying code in a coding agent's context, measuring the input-token savings against the accuracy cost. ![paper](https://img.shields.io/badge/paper-555?style=flat-square)

## Context Engineering

### Tools
- [CliffCompaction](https://github.com/nguyenvuthientrang/cliffcompaction) - CMU autocompaction proxy that shrinks an agent's context only by truncating or dropping content, never by LLM rewriting, and works in front of Claude Code or Codex. ![tool: MIT](https://img.shields.io/badge/tool-MIT-blue?style=flat-square) ![last commit](https://img.shields.io/github/last-commit/nguyenvuthientrang/cliffcompaction?style=flat-square&label=)
- [Repomix](https://github.com/yamadashy/repomix) - Packs an entire repository into a single AI-friendly file, reports token counts, and uses Tree-sitter to compress code to signatures. ![tool: MIT](https://img.shields.io/badge/tool-MIT-blue?style=flat-square) ![last commit](https://img.shields.io/github/last-commit/yamadashy/repomix?style=flat-square&label=)
- [Serena](https://github.com/oraios/serena) - Open-source MCP toolkit that gives a coding agent IDE-grade semantic code retrieval and editing. ![tool: GPL-3.0-or-later](https://img.shields.io/badge/tool-GPL--3.0--or--later-blue?style=flat-square) ![last commit](https://img.shields.io/github/last-commit/oraios/serena?style=flat-square&label=)
- [trace-mcp](https://github.com/nikolai-vysotskyi/trace-mcp) - MCP server that pre-indexes a repository into a symbol and dependency graph so an agent can query call graphs, change impact, or file outlines instead of reading files. ![tool: MIT](https://img.shields.io/badge/tool-MIT-blue?style=flat-square) ![last commit](https://img.shields.io/github/last-commit/nikolai-vysotskyi/trace-mcp?style=flat-square&label=)
- [Unreal Agent](https://unreallabs.ai/blog/long-horizon-agents-at-half-the-cost/) - MIT async agent harness whose vendor-reported SWE-Marathon run shows the same 69/160 pass count as Codex with GPT-6.1 Sol at xhigh, for $445.75 against $850.52, after adding mid-session compaction. ![tool: MIT](https://img.shields.io/badge/tool-MIT-blue?style=flat-square)

### Research & Benchmarks
- [AgentDiet](https://arxiv.org/abs/2509.23586) - Paper on an inference-time module that strips useless, redundant, and expired information from an agent's trajectory. ![paper](https://img.shields.io/badge/paper-555?style=flat-square)
- [Context Rot](https://www.trychroma.com/research/context-rot) - Chroma study of how LLM output quality changes as input length grows, with task difficulty held fixed. ![report](https://img.shields.io/badge/report-555?style=flat-square)
- [ContextBudget](https://arxiv.org/abs/2604.01664) - Paper on BACM, a method where an agent decides when and how much to compress its history based on the remaining context budget. ![paper](https://img.shields.io/badge/paper-555?style=flat-square)
- [RULER](https://github.com/NVIDIA/RULER) - NVIDIA long-context benchmark that measures how model quality holds up as the context window fills. ![bench](https://img.shields.io/badge/bench-555?style=flat-square) ![last commit](https://img.shields.io/github/last-commit/NVIDIA/RULER?style=flat-square&label=)
- [Self-Compacting Language Model Agents](https://arxiv.org/abs/2606.23525) - Paper introducing SELFCOMPACT, where the model itself decides when and how to compress a growing agent trace. ![paper](https://img.shields.io/badge/paper-555?style=flat-square)

### Reading
- [Anthropic Context Management](https://platform.claude.com/docs/en/build-with-claude/context-editing) - Anthropic documentation for context editing, the memory tool, and server-side compaction in the Claude API.
- [Claude Code Compaction Engine](https://barazany.dev/blog/claude-codes-compaction-engine) - Blog post describing the three-tier compaction engine Claude Code uses to trim a filling context window, and its cache and correctness failure modes.
- [Codex CLI Compaction Issue](https://github.com/openai/codex/issues/16812) - GitHub issue reporting that a Codex CLI upgrade made context compaction fire more often and raised token consumption for identical tasks.
- [Cursor Dynamic Context Discovery](https://cursor.com/blog/dynamic-context-discovery) - Cursor blog post on loading tool schemas and large outputs on demand instead of eagerly, and on Composer self-summarization.

## Cost Controls

### Reading
- [Claude Code Changelog](https://code.claude.com/docs/en/changelog) - Official Claude Code changelog covering spend controls such as subagent caps, budget limits, and gateway spend limits.
- [Claude Code Runaway-Loop Guardrails](https://github.com/anthropics/claude-code/releases/tag/v2.1.212) - Claude Code release notes for first-party guardrails against runaway agent loops.

## Gateways and Proxies

### Tools
- [Bifrost](https://github.com/maximhq/bifrost) - Go-based AI gateway from Maxim AI that fronts many models with low added latency. ![tool: Apache-2.0](https://img.shields.io/badge/tool-Apache--2.0-blue?style=flat-square) ![last commit](https://img.shields.io/github/last-commit/maximhq/bifrost?style=flat-square&label=)
- [Cloudflare AI Gateway Spend Limits](https://developers.cloudflare.com/ai-gateway/features/spend-limits/) - Cloudflare AI Gateway documentation on dollar-denominated spend limits that block or reroute requests once a budget is hit. ![co](https://img.shields.io/badge/co-555?style=flat-square)
- [Helicone](https://helicone.ai) - Open-source (Apache-2.0) LLM proxy that logs every request's cost, latency, and tokens. ![tool: Apache-2.0](https://img.shields.io/badge/tool-Apache--2.0-blue?style=flat-square)
- [Kong AI Gateway](https://developer.konghq.com/ai-gateway/) - AI layer of Kong's API-gateway platform that meters LLM, agent, and MCP traffic for billing, showback, and chargeback. ![co](https://img.shields.io/badge/co-555?style=flat-square)
- [LiteLLM](https://github.com/BerriAI/litellm) - Open-source gateway fronting 100+ LLM APIs that computes per-request dollar cost from a pricing map, with spend limits. ![tool: MIT](https://img.shields.io/badge/tool-MIT-blue?style=flat-square) ![last commit](https://img.shields.io/github/last-commit/BerriAI/litellm?style=flat-square&label=)
- [OpenRouter Provider Selection](https://openrouter.ai/docs/guides/routing/provider-selection) - OpenRouter documentation on routing requests across models and providers by price, with fallback on outages. ![co](https://img.shields.io/badge/co-555?style=flat-square)
- [Portkey AI Gateway Budget Limits](https://portkey.ai/docs/product/ai-gateway/virtual-keys/budget-limits) - Portkey documentation on routing LLM traffic across providers and enforcing hard USD budget limits on virtual keys. ![co](https://img.shields.io/badge/co-555?style=flat-square)

## Harness Efficiency

### Tools
- [SoL-Pi](https://nvlabs.github.io/SoL-Pi/) - NVIDIA Labs extension for the Pi coding harness that packages four token-efficiency mechanisms. ![tool: MIT](https://img.shields.io/badge/tool-MIT-blue?style=flat-square)
- [WOZCODE](https://wozcode.com) - Proprietary Claude Code plugin that publishes its own paired-task dataset comparing cost and tokens against stock Claude Code. ![tool: proprietary](https://img.shields.io/badge/tool-proprietary-blue?style=flat-square)

## Memory

### Tools
- [claude-code-memory-setup](https://github.com/lucasrosati/claude-code-memory-setup) - Practitioner recipe that pairs an Obsidian memory vault with a local AST code-graph tool. ![tool: MIT](https://img.shields.io/badge/tool-MIT-blue?style=flat-square) ![last commit](https://img.shields.io/github/last-commit/lucasrosati/claude-code-memory-setup?style=flat-square&label=)
- [claude-mem](https://github.com/thedotmack/claude-mem) - Coding-agent memory layer that captures every session, compresses it with AI, and re-injects relevant context in later sessions. ![tool: Apache-2.0](https://img.shields.io/badge/tool-Apache--2.0-blue?style=flat-square) ![last commit](https://img.shields.io/github/last-commit/thedotmack/claude-mem?style=flat-square&label=)
- [Cognee](https://github.com/topoteretes/cognee) - Open-source (Apache-2.0) AI-memory platform that gives agents persistent memory through a self-hosted knowledge graph. ![tool: Apache-2.0](https://img.shields.io/badge/tool-Apache--2.0-blue?style=flat-square) ![last commit](https://img.shields.io/github/last-commit/topoteretes/cognee?style=flat-square&label=)
- [LangMem](https://github.com/langchain-ai/langmem) - LangChain long-term memory library that extracts and consolidates facts from conversations and integrates with LangGraph's memory store. ![tool: MIT](https://img.shields.io/badge/tool-MIT-blue?style=flat-square) ![last commit](https://img.shields.io/github/last-commit/langchain-ai/langmem?style=flat-square&label=)
- [Letta](https://github.com/letta-ai/letta-code) - Platform for stateful agents, from the MemGPT project, that pages an LLM's context like an operating system. ![tool: Apache-2.0](https://img.shields.io/badge/tool-Apache--2.0-blue?style=flat-square) ![last commit](https://img.shields.io/github/last-commit/letta-ai/letta-code?style=flat-square&label=)
- [Mem0](https://github.com/mem0ai/mem0) - Open-source memory layer that extracts salient facts from conversations and retrieves only the relevant ones per call. ![tool: Apache-2.0](https://img.shields.io/badge/tool-Apache--2.0-blue?style=flat-square) ![last commit](https://img.shields.io/github/last-commit/mem0ai/mem0?style=flat-square&label=)
- [Supermemory](https://github.com/supermemoryai/supermemory) - Memory and context engine for agents. ![tool: MIT](https://img.shields.io/badge/tool-MIT-blue?style=flat-square) ![last commit](https://img.shields.io/github/last-commit/supermemoryai/supermemory?style=flat-square&label=)
- [Zep / Graphiti](https://www.getzep.com/) - Memory platform for agents built on temporal knowledge graphs. ![tool: Apache-2.0](https://img.shields.io/badge/tool-Apache--2.0-blue?style=flat-square)

### Reading
- [Karpathy's LLM Wiki](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) - Gist by Andrej Karpathy describing a pattern where an agent builds and maintains a persistent markdown wiki from your sources.

## Multi-Agent Systems

### Tools
- [CrewAI](https://github.com/crewAIInc/crewAI) - MIT-licensed multi-agent orchestration framework whose crew object reports cache-aware token totals. ![tool: MIT](https://img.shields.io/badge/tool-MIT-blue?style=flat-square) ![last commit](https://img.shields.io/github/last-commit/crewAIInc/crewAI?style=flat-square&label=)
- [LangChain](https://github.com/langchain-ai/langchain) - MIT-licensed agent framework underneath LangGraph, LangMem, and LangSmith that defines cache-aware usage metadata and ships context-editing, summarization, and call-limit middleware. ![tool: MIT](https://img.shields.io/badge/tool-MIT-blue?style=flat-square) ![last commit](https://img.shields.io/github/last-commit/langchain-ai/langchain?style=flat-square&label=)
- [LangGraph](https://github.com/langchain-ai/langgraph) - LangChain graph orchestration library for stateful agents, with per-super-step checkpointing and an opt-in node result cache. ![tool: MIT](https://img.shields.io/badge/tool-MIT-blue?style=flat-square) ![last commit](https://img.shields.io/github/last-commit/langchain-ai/langgraph?style=flat-square&label=)

### Research & Benchmarks
- [SupervisorAgent](https://arxiv.org/abs/2510.26585) - Paper on a lightweight, modular framework for runtime, adaptive supervision of multi-agent systems. ![paper](https://img.shields.io/badge/paper-555?style=flat-square)

### Reading
- [CrewAI Hierarchical Process](https://docs.crewai.com/en/learn/hierarchical-process) - CrewAI documentation on the hierarchical process, where a manager LLM plans and validates work delegated to other agents.

## Prompt Agent Loop

### Tools
- [benjamin-plus](https://github.com/JetBrains/benjamin-plus-skill) - JetBrains skill, a small instruction payload that changes how a coding agent looks things up and waits, with a published A/B rig. ![tool: MIT](https://img.shields.io/badge/tool-MIT-blue?style=flat-square) ![last commit](https://img.shields.io/github/last-commit/JetBrains/benjamin-plus-skill?style=flat-square&label=)
- [token-ninja](https://github.com/oanhduong/token-ninja) - Intercepts deterministic commands like `git status` or `npm test` before they reach the model and runs them locally. ![tool: MIT](https://img.shields.io/badge/tool-MIT-blue?style=flat-square) ![last commit](https://img.shields.io/github/last-commit/oanhduong/token-ninja?style=flat-square&label=)

### Research & Benchmarks
- [LOOP Skill Engine](https://arxiv.org/abs/2605.14237) - Paper on recording an agent's first run of a repetitive task with full LLM reasoning, then replaying the extracted tool-call template without calling the LLM. ![paper](https://img.shields.io/badge/paper-555?style=flat-square)

### Reading
- [Orchestrator-Worker Model Tiering](https://www.mindstudio.ai/blog/smart-orchestrator-cheaper-sub-agent-models-claude-code) - Blog post on the pattern where a capable model plans and cheaper agents execute, using Claude Code subagents.

## Retrieval Memory

### Tools
- [deja-vu](https://vshulcz.github.io/deja-vu/guide/day-zero.html) - MIT single-binary local memory for coding agents built from session history already on disk, with no LLM; its maker's 11-runs-per-arm benchmark cut median tokens from 126,222 to 53,558. ![tool: MIT](https://img.shields.io/badge/tool-MIT-blue?style=flat-square)
- [LlamaIndex](https://github.com/run-llama/llama_index) - MIT-licensed data framework for LLM applications with a token-counting callback and an optional hard token budget. ![tool: MIT](https://img.shields.io/badge/tool-MIT-blue?style=flat-square) ![last commit](https://img.shields.io/github/last-commit/run-llama/llama_index?style=flat-square&label=)
- [PageIndex](https://github.com/VectifyAI/PageIndex) - Vectorless RAG engine that builds a hierarchical tree index over long documents and has an LLM reason over the index instead of embedding chunks. ![tool: MIT](https://img.shields.io/badge/tool-MIT-blue?style=flat-square) ![last commit](https://img.shields.io/github/last-commit/VectifyAI/PageIndex?style=flat-square&label=)
- [Signet AI](https://github.com/Signet-AI/signetai) - Local-first memory and context layer that syncs memories, transcripts, and secrets across Claude Code, Codex, OpenCode, and other harnesses. ![tool: Apache-2.0](https://img.shields.io/badge/tool-Apache--2.0-blue?style=flat-square) ![last commit](https://img.shields.io/github/last-commit/Signet-AI/signetai?style=flat-square&label=)
- [xmemory](https://arxiv.org/abs/2604.27906) - Paper on schema-grounded agent memory that extracts structured facts instead of storing text. ![tool: proprietary](https://img.shields.io/badge/tool-proprietary-blue?style=flat-square)

## Retry and Reliability

### Reading
- [Claude Code v2.1.199](https://github.com/anthropics/claude-code/releases/tag/v2.1.199) - Claude Code release notes covering automatic retry of rate-limit errors with backoff and partial-output preservation.

## Routing Model Selection

### Tools
- [Antigravity CLI Changelog](https://github.com/google-antigravity/antigravity-cli/blob/main/CHANGELOG.md) - Release notes for Antigravity CLI covering per-subagent model-tier routing and an effort control. ![tool](https://img.shields.io/badge/tool-blue?style=flat-square) ![last commit](https://img.shields.io/github/last-commit/google-antigravity/antigravity-cli?style=flat-square&label=)
- [Claude Code Router](https://github.com/musistudio/claude-code-router) - Local gateway that puts Claude Code, Codex, and other coding CLIs behind one endpoint and routes each request by rules or a prompt tag. ![tool: MIT](https://img.shields.io/badge/tool-MIT-blue?style=flat-square) ![last commit](https://img.shields.io/github/last-commit/musistudio/claude-code-router?style=flat-square&label=)
- [Copilot HydraFusion](https://github.blog/2026-09-04-project-hydrafusion-frontier-quality-via-multi-model-orchestration/) - GitHub research-preview feature that picks one of three multi-model workflows (Single, Cascade, Critique) per request; GitHub reports 36% to 67% lower estimated cost than Claude Opus 5 at -1.5 to +4.9 points of quality, tuned on the same benchmarks. ![tool: proprietary](https://img.shields.io/badge/tool-proprietary-blue?style=flat-square)
- [Cursor Router](https://cursor.com/blog/router) - Cursor blog post on Auto mode, which classifies each request and routes it to a model under Intelligence, Balance, or Cost modes. ![co](https://img.shields.io/badge/co-555?style=flat-square)
- [GitHub Copilot Auto Model Selection](https://docs.github.com/en/copilot/concepts/models/auto-model-selection) - GitHub documentation on Copilot's Auto setting, which routes by model health and task complexity. ![co](https://img.shields.io/badge/co-555?style=flat-square)
- [NadirClaw](https://github.com/NadirRouter/NadirClaw) - OpenAI-compatible pre-router proxy for coding harnesses that picks the cheapest model predicted to answer and escalates on failure. ![tool: PolyForm Noncommercial 1.0.0](https://img.shields.io/badge/tool-PolyForm_Noncommercial_1.0.0-blue?style=flat-square) ![last commit](https://img.shields.io/github/last-commit/NadirRouter/NadirClaw?style=flat-square&label=)
- [NVIDIA NeMo Switchyard](https://github.com/NVIDIA-NeMo/Switchyard) - Apache-2.0, pre-1.0 routing library that picks a model per agent request from your own pool, also hosted on OpenRouter; its cost cuts (28% to 74% from partners, about one third internally) are self-reported. ![tool: Apache-2.0](https://img.shields.io/badge/tool-Apache--2.0-blue?style=flat-square) ![last commit](https://img.shields.io/github/last-commit/NVIDIA-NeMo/Switchyard?style=flat-square&label=)
- [OpenAI Decisions API](https://developers.openai.com/api/docs/guides/decisions) - Beta endpoint that answers typed questions (probability, choice, score) about text or images with gpt-6-luna at $0.10 per 1M input tokens and no output, cache-read, or cache-write charges (as of 2026-10-06). ![tool: proprietary](https://img.shields.io/badge/tool-proprietary-blue?style=flat-square)
- [OpenCode](https://opencode.ai/docs/) - Open-source (MIT) coding-agent CLI with explicit cost and model routing configuration. ![tool: MIT](https://img.shields.io/badge/tool-MIT-blue?style=flat-square)
- [pi-model-router](https://github.com/yeliu84/pi-model-router) - Heuristic per-turn model router for the pi coding agent, with an OpenCode counterpart that routes by keyword and word-count rules. ![tool: MIT](https://img.shields.io/badge/tool-MIT-blue?style=flat-square) ![last commit](https://img.shields.io/github/last-commit/yeliu84/pi-model-router?style=flat-square&label=)
- [Plano](https://github.com/katanemo/plano) - Envoy-based proxy whose router matches queries to user-defined domains and actions using a small routing model. ![tool: Apache-2.0](https://img.shields.io/badge/tool-Apache--2.0-blue?style=flat-square) ![last commit](https://img.shields.io/github/last-commit/katanemo/plano?style=flat-square&label=)
- [ruflo](https://github.com/ruvnet/ruflo) - Open-source agent meta-harness for Claude Code and Codex with swarm orchestration, persistent memory, and cost-adjusted model routing. ![tool: MIT](https://img.shields.io/badge/tool-MIT-blue?style=flat-square) ![last commit](https://img.shields.io/github/last-commit/ruvnet/ruflo?style=flat-square&label=)
- [vLLM Semantic Router](https://github.com/vllm-project/semantic-router) - Open-source, self-hostable router that sends routine queries to cheap or local models and hard ones to stronger backends. ![tool: Apache-2.0](https://img.shields.io/badge/tool-Apache--2.0-blue?style=flat-square) ![last commit](https://img.shields.io/github/last-commit/vllm-project/semantic-router?style=flat-square&label=)
- [Weave Router](https://github.com/weave-os/router) - Drop-in proxy that picks a model for every turn of a coding-agent session and weighs the cost of switching, relicensed from Elastic License 2.0 to Apache-2.0 on 2026-09-24; its benchmark results are vendor-reported. ![tool: Apache-2.0](https://img.shields.io/badge/tool-Apache--2.0-blue?style=flat-square) ![last commit](https://img.shields.io/github/last-commit/weave-os/router?style=flat-square&label=)

### Research & Benchmarks
- [Cluster, Route, Escalate](https://arxiv.org/abs/2606.27457) - Paper proposing a two-stage cost-aware cascade for LLM serving that combines routing and escalation. ![paper](https://img.shields.io/badge/paper-555?style=flat-square)
- [MTRouter](https://arxiv.org/abs/2604.23530) - Paper on picking a different model for each turn of a multi-turn conversation to meet a cost budget. ![paper](https://img.shields.io/badge/paper-555?style=flat-square)
- [OrcaRouter](https://arxiv.org/abs/2605.30736) - Paper on a production LLM router built on a LinUCB bandit. ![paper](https://img.shields.io/badge/paper-555?style=flat-square)

### Reading
- [Claude Code via LiteLLM](https://docs.litellm.ai/docs/tutorials/claude_non_anthropic_models) - LiteLLM tutorial for pointing Claude Code at a LiteLLM proxy so cheaper or non-Anthropic models can handle some work.
- [Distilling Agent Behavior](https://arxiv.org/abs/2505.17612) - Paper on distilling a large agent's behavior into a small task-specific model to cut per-token cost.
- [TypeSafe Jev](https://typesafe.ai/blog/introducing-system-one-models-and-jev) - TypeSafe AI blog post on a hosted decision model that answers typed questions with a choice or score and a probability.

## Search and Retrieval Boundary

### Tools
- [Exa](https://exa.ai/pricing) - Search API for agents that bills content retrieval separately per type, such as query-scoped highlights or summaries. ![co](https://img.shields.io/badge/co-555?style=flat-square)
- [Firecrawl](https://github.com/firecrawl/firecrawl) - Web scraping API that converts pages to markdown or structured JSON before they reach the model. ![tool: AGPL-3.0](https://img.shields.io/badge/tool-AGPL--3.0-blue?style=flat-square) ![last commit](https://img.shields.io/github/last-commit/firecrawl/firecrawl?style=flat-square&label=)
- [Parallel Benchmarks](https://parallel.ai/benchmarks) - Parallel web search and extraction API benchmarks page with accuracy-versus-cost tables. ![co](https://img.shields.io/badge/co-555?style=flat-square)
- [Tavily](https://docs.tavily.com/documentation/api-credits) - Search API for agents that returns capped content snippets instead of full pages and prices by credit. ![co](https://img.shields.io/badge/co-555?style=flat-square)
- [Valyu](https://github.com/valyuAI/valyu-benchmarks) - Search and deep-research API with an open benchmark harness for cost-versus-accuracy results on the DRACO benchmark. ![co](https://img.shields.io/badge/co-555?style=flat-square)

## Serving Inference

### Tools
- [SGLang](https://github.com/sgl-project/sglang) - Serving framework for large language and multimodal models. ![tool: Apache-2.0](https://img.shields.io/badge/tool-Apache--2.0-blue?style=flat-square) ![last commit](https://img.shields.io/github/last-commit/sgl-project/sglang?style=flat-square&label=)
- [TensorRT-LLM](https://github.com/NVIDIA/TensorRT-LLM) - NVIDIA open-source LLM inference engine with KV-cache reuse, in-flight batching, and prefill-decode disaggregation. ![tool: Apache-2.0](https://img.shields.io/badge/tool-Apache--2.0-blue?style=flat-square) ![last commit](https://img.shields.io/github/last-commit/NVIDIA/TensorRT-LLM?style=flat-square&label=)
- [vLLM](https://github.com/vllm-project/vllm) - Open-source LLM serving engine that uses PagedAttention to manage KV-cache memory in blocks. ![tool: Apache-2.0](https://img.shields.io/badge/tool-Apache--2.0-blue?style=flat-square) ![last commit](https://img.shields.io/github/last-commit/vllm-project/vllm?style=flat-square&label=)

### Research & Benchmarks
- [RLM-Cascade](https://arxiv.org/abs/2606.22840) - Paper on response-level speculative decoding at the gateway, where a cheap draft model answers first and a stronger verifier accepts or rewrites it. ![paper](https://img.shields.io/badge/paper-555?style=flat-square)

## Test-Time Compute

### Research & Benchmarks
- [Stop When Reasoning Converges](https://arxiv.org/abs/2605.17672) - Paper on stopping reasoning once a solution has stabilized, to avoid wasted tokens and latency from overthinking. ![paper](https://img.shields.io/badge/paper-555?style=flat-square)
- [When More Reasoning Hurts](https://arxiv.org/abs/2604.10739) - Paper on how giving a model more reasoning budget can lower performance and raise cost. ![paper](https://img.shields.io/badge/paper-555?style=flat-square)

## Tool Protocol Overhead

### Tools
- [Coral](https://github.com/withcoral/coral) - Gives agents one SQL interface over APIs and internal systems instead of many MCP servers, with its own task benchmark. ![tool: Apache-2.0](https://img.shields.io/badge/tool-Apache--2.0-blue?style=flat-square) ![last commit](https://img.shields.io/github/last-commit/withcoral/coral?style=flat-square&label=)
- [StackOne Falcon](https://www.stackone.com/blog/mcp-token-optimization/) - Execution engine that cuts tool-calling tokens by filtering tool definitions, shaping responses, and running code at the edge. ![co](https://img.shields.io/badge/co-555?style=flat-square)

### Research & Benchmarks
- [MCP Tool Descriptions Are Smelly!](https://arxiv.org/abs/2602.14878) - Study of how poorly written MCP tool descriptions affect agent efficiency, using an LLM-jury scanner on MCP-Universe. ![paper](https://img.shields.io/badge/paper-555?style=flat-square)
- [Tool Attention Is All You Need](https://arxiv.org/abs/2604.21816) - Paper on the cost of MCP re-sending every tool's full schema on every turn, known as the MCP/Tools Tax. ![paper](https://img.shields.io/badge/paper-555?style=flat-square)

### Reading
- [Code Execution with MCP](https://www.anthropic.com/engineering/code-execution-with-mcp) - Anthropic engineering post on agents calling MCP servers by writing and executing code so unused tool schemas stay out of the context window.
