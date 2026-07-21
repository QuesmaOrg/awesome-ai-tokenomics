# Awesome AI Tokenomics [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> A map of what AI tokens actually cost, and where they're wasted vs. well spent.

*"I feel nervous when I have subscription left over. That just means I haven't maximized my token throughput."*
<br>Andrej Karpathy, [No Priors](https://podscripts.co/podcasts/no-priors-artificial-intelligence-technology-startups/andrej-karpathy-on-code-agents-autoresearch-and-the-loopy-era-of-ai) (2026)

As of 2026-07: 177 entries across five areas, 8 practices, 10 concepts, 8 claims, and 7 copy-paste setups.

**Topics:** [Caching](#caching) · [Compression](#compression) · [Context engineering](#context-engineering) · [Memory](#memory) · [Routing](#routing-model-selection) · [Multi-agent systems](#multi-agent-systems) · [Gateways](#gateways-and-proxies) · [Observability](#observability) · [Benchmarks](#benchmarks-evals) · [Cache accounting](#cache-accounting) · [Budgets](#budgets-caps) · [Pricing models](#pricing-models) · [Energy](#energy-carbon)

## Contents

- [Where to start](#where-to-start)
- [Legend](#legend)
- [Monitor](#monitor)
- [Optimize](#optimize)
- [Govern](#govern)
- [Understand](#understand)
- [Measure](#measure)
- [Practices](#practices)
- [Concepts](#concepts)
- [Claims](#claims)
- [Setups and skills](#setups-and-skills)

## Where to start

Just want the numbers: the five area sections below hold every entry. Want the method: read the practices first, then the concepts behind them. Building something: setups and skills holds runnable configurations.

## Legend

Each entry ends with a kind badge: ![tool: MIT](https://img.shields.io/badge/tool-MIT-blue?style=flat-square) (blue, with the license when known), or a gray badge for ![paper](https://img.shields.io/badge/paper-555?style=flat-square), ![bench](https://img.shields.io/badge/bench-555?style=flat-square), ![data](https://img.shields.io/badge/data-555?style=flat-square), ![co](https://img.shields.io/badge/co-555?style=flat-square) for companies, and ![report](https://img.shields.io/badge/report-555?style=flat-square). Plain entries are articles. GitHub-hosted tools also carry live star and last-commit badges.

## Monitor

### Dashboards

- [ccusage](https://github.com/ccusage/ccusage) - A widely adopted open-source CLI that reads local agent logs to report token usage and cost across 15 coding-agent sources, with caching-aware pricing. ![tool: MIT](https://img.shields.io/badge/tool-MIT-blue?style=flat-square) ![stars](https://img.shields.io/github/stars/ccusage/ccusage?style=flat-square&logo=github&label=) ![last commit](https://img.shields.io/github/last-commit/ccusage/ccusage?style=flat-square&label=)
- [Claude Code Usage Monitor](https://github.com/Maciek-roboblog/Claude-Code-Usage-Monitor) - The most-adopted Claude Code usage monitor: a live terminal dashboard with burn-rate analytics, P90 limit detection, and session-expiry forecasts. ![tool: MIT](https://img.shields.io/badge/tool-MIT-blue?style=flat-square) ![stars](https://img.shields.io/github/stars/Maciek-roboblog/Claude-Code-Usage-Monitor?style=flat-square&logo=github&label=) ![last commit](https://img.shields.io/github/last-commit/Maciek-roboblog/Claude-Code-Usage-Monitor?style=flat-square&label=)
- [claude-usage](https://github.com/phuryn/claude-usage) - A local dashboard for Claude Code token usage, costs, and session history; Pro and Max subscribers get a quota progress bar. ![tool: MIT](https://img.shields.io/badge/tool-MIT-blue?style=flat-square) ![stars](https://img.shields.io/github/stars/phuryn/claude-usage?style=flat-square&logo=github&label=) ![last commit](https://img.shields.io/github/last-commit/phuryn/claude-usage?style=flat-square&label=)
- [ClaudeBar](https://github.com/tddworks/ClaudeBar) - A macOS menu-bar app that monitors AI coding quotas across 11 providers; the README declares MIT but ships no license file, so the OSS grant is unconfirmed. ![tool: MIT declared in README](https://img.shields.io/badge/tool-MIT_declared_in_README-blue?style=flat-square) ![stars](https://img.shields.io/github/stars/tddworks/ClaudeBar?style=flat-square&logo=github&label=) ![last commit](https://img.shields.io/github/last-commit/tddworks/ClaudeBar?style=flat-square&label=)
- [CodeBurn](https://github.com/getagentseal/codeburn#find-and-fix-waste) - An open-source tracker for 36 coding tools whose optimize command flags named harness-waste patterns with dollar estimates it later checks against actuals. ![tool: MIT](https://img.shields.io/badge/tool-MIT-blue?style=flat-square)
- [Codex Usage Tracker](https://github.com/douglasmonsky/codex-usage-tracker) - A local-first dashboard, CLI, and MCP tools indexing Codex CLI logs into SQLite to show where tokens, credits, and cost go, including cache ratios. ![tool: MIT](https://img.shields.io/badge/tool-MIT-blue?style=flat-square) ![stars](https://img.shields.io/github/stars/douglasmonsky/codex-usage-tracker?style=flat-square&logo=github&label=) ![last commit](https://img.shields.io/github/last-commit/douglasmonsky/codex-usage-tracker?style=flat-square&label=)
- [CodeZeno Usage Monitor](https://github.com/CodeZeno/Claude-Code-Usage-Monitor) - A Windows-taskbar widget showing real-time Claude Code quota and usage at a glance, without opening a terminal. ![tool: MIT](https://img.shields.io/badge/tool-MIT-blue?style=flat-square) ![stars](https://img.shields.io/github/stars/CodeZeno/Claude-Code-Usage-Monitor?style=flat-square&logo=github&label=) ![last commit](https://img.shields.io/github/last-commit/CodeZeno/Claude-Code-Usage-Monitor?style=flat-square&label=)
- [Datadog LLM Observability - Cost](https://docs.datadoghq.com/llm_observability/monitoring/cost/) - Datadog's LLM Observability estimates per-request cost across 800+ models from token counts and public pricing; invoice reconciliation is a separate product. ![co](https://img.shields.io/badge/co-555?style=flat-square)
- [gh-aw (GitHub Agentic Workflows)](https://github.com/github/gh-aw) - GitHub's agentic-workflows runtime with first-party per-run token and cost metering, plus budget caps that stop a workflow mid-run. ![tool: MIT](https://img.shields.io/badge/tool-MIT-blue?style=flat-square) ![stars](https://img.shields.io/github/stars/github/gh-aw?style=flat-square&logo=github&label=) ![last commit](https://img.shields.io/github/last-commit/github/gh-aw?style=flat-square&label=)
- [Grafana Cloud GenAI Observability](https://grafana.com/docs/grafana-cloud/monitor-applications/ai-observability/genai/observability/) - Grafana Cloud's GenAI Observability ships a prebuilt dashboard for LLM cost, token usage, and latency, built on top of the OpenLIT SDK. ![co](https://img.shields.io/badge/co-555?style=flat-square)
- [OpenLIT](https://github.com/openlit/openlit) - An open-source (Apache-2.0), OpenTelemetry-native platform with a self-hosted dashboard for LLM cost, token, and latency observability. ![tool: Apache-2.0](https://img.shields.io/badge/tool-Apache--2.0-blue?style=flat-square) ![stars](https://img.shields.io/github/stars/openlit/openlit?style=flat-square&logo=github&label=) ![last commit](https://img.shields.io/github/last-commit/openlit/openlit?style=flat-square&label=)
- [OpenUsage](https://github.com/robinebers/openusage) - A native Swift macOS menu-bar meter for 10 AI coding subscriptions, showing session and weekly limits, credits, and estimated spend from local credentials. ![tool: MIT](https://img.shields.io/badge/tool-MIT-blue?style=flat-square) ![stars](https://img.shields.io/github/stars/robinebers/openusage?style=flat-square&logo=github&label=) ![last commit](https://img.shields.io/github/last-commit/robinebers/openusage?style=flat-square&label=)
- [TokenTracker](https://github.com/mm7894215/TokenTracker) - A local-first token and cost dashboard for 27 coding tools, with a desktop pet, native widgets, and achievements as a distinct gamified take on usage metering. ![tool: MIT](https://img.shields.io/badge/tool-MIT-blue?style=flat-square) ![stars](https://img.shields.io/github/stars/mm7894215/TokenTracker?style=flat-square&logo=github&label=) ![last commit](https://img.shields.io/github/last-commit/mm7894215/TokenTracker?style=flat-square&label=)

### Ebpf Kernel Capture

- [AgentSight](https://github.com/eunomia-bpf/agentsight) - Uses eBPF to watch an AI agent from the kernel boundary, correlating what it said it would do against what it did, at under 3% overhead. ![tool: MIT](https://img.shields.io/badge/tool-MIT-blue?style=flat-square) ![stars](https://img.shields.io/github/stars/eunomia-bpf/agentsight?style=flat-square&logo=github&label=) ![last commit](https://img.shields.io/github/last-commit/eunomia-bpf/agentsight?style=flat-square&label=)
- [OpenTelemetry eBPF Instrumentation (OBI) - GenAI / MCP](https://opentelemetry.io/docs/zero-code/obi/) - OBI is OpenTelemetry's zero-code eBPF instrumentation (formerly Grafana Beyla) that captures GenAI and MCP traces at the kernel layer with no SDK. ![tool: Apache-2.0](https://img.shields.io/badge/tool-Apache--2.0-blue?style=flat-square)

### Observability

- [Langfuse](https://langfuse.com) - An open-source platform for tracing, evaluating, and analyzing LLM and agent transcripts, with a prompt-management layer on top. ![tool: MIT](https://img.shields.io/badge/tool-MIT-blue?style=flat-square)

### Otel For Llms

- [OpenLLMetry](https://github.com/traceloop/openllmetry) - An open-source set of OpenTelemetry-based SDKs and instrumentations, built by Traceloop, for LLM apps. ![tool: Apache-2.0](https://img.shields.io/badge/tool-Apache--2.0-blue?style=flat-square) ![stars](https://img.shields.io/github/stars/traceloop/openllmetry?style=flat-square&logo=github&label=) ![last commit](https://img.shields.io/github/last-commit/traceloop/openllmetry?style=flat-square&label=)
- [OpenTelemetry GenAI Semantic Conventions](https://github.com/open-telemetry/semantic-conventions-genai) - OpenTelemetry's GenAI Semantic Conventions define the vendor-neutral token, cost, and cache attribute names that OpenLLMetry and Phoenix both converge onto.

### Tracing

- [Arize Phoenix](https://github.com/Arize-ai/phoenix) - A source-available (Elastic License 2.0) LLM tracing platform recording per-span token counts and USD cost via OpenTelemetry. ![tool: Elastic-2.0](https://img.shields.io/badge/tool-Elastic--2.0-blue?style=flat-square) ![stars](https://img.shields.io/github/stars/Arize-ai/phoenix?style=flat-square&logo=github&label=) ![last commit](https://img.shields.io/github/last-commit/Arize-ai/phoenix?style=flat-square&label=)
- [claude-tap](https://github.com/liaohch3/claude-tap) - A local trace viewer intercepting API traffic from 14+ coding agents, showing per-request token breakdowns: input, output, cache read, cache creation. ![tool: MIT](https://img.shields.io/badge/tool-MIT-blue?style=flat-square) ![stars](https://img.shields.io/github/stars/liaohch3/claude-tap?style=flat-square&logo=github&label=) ![last commit](https://img.shields.io/github/last-commit/liaohch3/claude-tap?style=flat-square&label=)
- [LangSmith - Cost Tracking](https://docs.langchain.com/langsmith/cost-tracking) - LangSmith is LangChain's commercial LLM/agent observability SaaS. ![co](https://img.shields.io/badge/co-555?style=flat-square)
- [Opik](https://github.com/comet-ml/opik) - Comet's open-source (Apache-2.0) LLM observability platform, highest-starred in its class, with per-span USD cost estimated from token usage. ![tool: Apache-2.0](https://img.shields.io/badge/tool-Apache--2.0-blue?style=flat-square) ![stars](https://img.shields.io/github/stars/comet-ml/opik?style=flat-square&logo=github&label=) ![last commit](https://img.shields.io/github/last-commit/comet-ml/opik?style=flat-square&label=)

## Optimize

### Caching

- [GPTCache](https://github.com/zilliztech/GPTCache) - An open-source semantic cache returning a stored LLM response for a paraphrased repeat query via vector search, skipping the paid call. ![tool: MIT](https://img.shields.io/badge/tool-MIT-blue?style=flat-square) ![stars](https://img.shields.io/github/stars/zilliztech/GPTCache?style=flat-square&logo=github&label=) ![last commit](https://img.shields.io/github/last-commit/zilliztech/GPTCache?style=flat-square&label=)
- [LMCache - KV-cache reuse layer with token-level cache-hit accounting (self-host)](https://github.com/LMCache/LMCache) - LMCache is a self-hosted KV-cache layer beneath vLLM, giving token-level cache-hit observability for teams who own their GPUs, not a hosted bill. ![tool: Apache-2.0](https://img.shields.io/badge/tool-Apache--2.0-blue?style=flat-square) ![stars](https://img.shields.io/github/stars/LMCache/LMCache?style=flat-square&logo=github&label=) ![last commit](https://img.shields.io/github/last-commit/LMCache/LMCache?style=flat-square&label=)

### Cheap Local Models

- [llama.cpp](https://github.com/ggml-org/llama.cpp) - The foundational open-source (MIT) local LLM inference engine most of the local ecosystem runs on, with an OpenAI-compatible server built in. ![tool: MIT](https://img.shields.io/badge/tool-MIT-blue?style=flat-square) ![stars](https://img.shields.io/github/stars/ggml-org/llama.cpp?style=flat-square&logo=github&label=) ![last commit](https://img.shields.io/github/last-commit/ggml-org/llama.cpp?style=flat-square&label=)
- [Ollama](https://github.com/ollama/ollama) - The de facto runtime for running open-weight models like Qwen, DeepSeek, and GLM-5.1 locally, shifting inference onto hardware you already own. ![tool: MIT](https://img.shields.io/badge/tool-MIT-blue?style=flat-square) ![stars](https://img.shields.io/github/stars/ollama/ollama?style=flat-square&logo=github&label=) ![last commit](https://img.shields.io/github/last-commit/ollama/ollama?style=flat-square&label=)

### Compression

- [Context Mode - MCP server that sandboxes tool output out of the context window](https://github.com/mksglu/context-mode) - This MCP server sandboxes tool calls and returns only the distilled result, claiming a 98% cut: 315 KB of output down to 5.4 KB. ![tool: Elastic-2.0](https://img.shields.io/badge/tool-Elastic--2.0-blue?style=flat-square) ![stars](https://img.shields.io/github/stars/mksglu/context-mode?style=flat-square&logo=github&label=) ![last commit](https://img.shields.io/github/last-commit/mksglu/context-mode?style=flat-square&label=)
- [headroom - the context-compression genre's mega-anchor (quality story dissected)](https://github.com/headroomlabs-ai/headroom) - An Apache-2.0 context-compression tool for LLM/agent pipelines, the category's largest repo, confirmed organic by star-forensics. ![tool: Apache-2.0](https://img.shields.io/badge/tool-Apache--2.0-blue?style=flat-square) ![stars](https://img.shields.io/github/stars/headroomlabs-ai/headroom?style=flat-square&logo=github&label=) ![last commit](https://img.shields.io/github/last-commit/headroomlabs-ai/headroom?style=flat-square&label=)
- [LLMLingua](https://github.com/microsoft/LLMLingua) - Microsoft's prompt-compression library that uses a small model to drop low-information tokens before a prompt reaches the target LLM. ![tool: MIT](https://img.shields.io/badge/tool-MIT-blue?style=flat-square) ![stars](https://img.shields.io/github/stars/microsoft/LLMLingua?style=flat-square&logo=github&label=) ![last commit](https://img.shields.io/github/last-commit/microsoft/LLMLingua?style=flat-square&label=)
- [llmtrim](https://github.com/fkiene/llmtrim) - A local proxy that compresses a coding agent's prompt, tool schemas, and history before forwarding, and can reroute Claude calls to Grok. ![tool: MPL-2.0](https://img.shields.io/badge/tool-MPL--2.0-blue?style=flat-square) ![stars](https://img.shields.io/github/stars/fkiene/llmtrim?style=flat-square&logo=github&label=) ![last commit](https://img.shields.io/github/last-commit/fkiene/llmtrim?style=flat-square&label=)
- [Minification of state-in-context agents - the clean waste-vs-capability datapoint](https://arxiv.org/abs/2606.01326) - This ICPC 2026 study found that minifying code in a coding agent's context cuts input tokens by 42% but costs 12 percentage points of accuracy. ![paper](https://img.shields.io/badge/paper-555?style=flat-square)
- [rtk - the context-compression genre's largest adoption anchor (reduction-only headline)](https://github.com/rtk-ai/rtk) - rtk is a single-binary Rust CLI proxy that intercepts and compresses the output of common dev commands before it reaches an LLM coding agent's context window. ![tool: Apache-2.0](https://img.shields.io/badge/tool-Apache--2.0-blue?style=flat-square) ![stars](https://img.shields.io/github/stars/rtk-ai/rtk?style=flat-square&logo=github&label=) ![last commit](https://img.shields.io/github/last-commit/rtk-ai/rtk?style=flat-square&label=)
- [TOON (Token-Oriented Object Notation)](https://github.com/toon-format/toon) - TOON is a compact, human-readable, lossless serialization of the JSON data model, designed for LLM input. ![tool: MIT](https://img.shields.io/badge/tool-MIT-blue?style=flat-square) ![stars](https://img.shields.io/github/stars/toon-format/toon?style=flat-square&logo=github&label=) ![last commit](https://img.shields.io/github/last-commit/toon-format/toon?style=flat-square&label=)

### Context Engineering

- [AgentDiet - trajectory reduction ("Reducing Cost of LLM Agents with Trajectory Reduction")](https://arxiv.org/abs/2509.23586) - AgentDiet is an inference-time module that strips useless, redundant, and expired information from an agent's trajectory, without hurting performance. ![paper](https://img.shields.io/badge/paper-555?style=flat-square)
- [Anthropic vendor-native context management (context editing + memory tool + server-side compaction)](https://platform.claude.com/docs/en/build-with-claude/context-editing) - Anthropic's context editing, memory tool, and server-side compaction cut token consumption by a vendor-reported 84% in a 100-turn web-search evaluation.
- [Claude Code compaction engine - the three-tier mechanism and its cache/correctness failure modes](https://barazany.dev/blog/claude-codes-compaction-engine) - Claude Code's *harness* - not the API - decides how to trim a filling context window, and it does this through a three-tier compaction engine.
- [Codex CLI compaction cost - over-eager compaction as a token-amplification loop](https://github.com/openai/codex/issues/16812) - Upgrading Codex CLI from v0.116 to v0.118 made context compaction fire twice as often, doubling or tripling token consumption for identical tasks.
- [Context Rot - LLM performance degrades as input length grows](https://www.trychroma.com/research/context-rot) - This is Chroma's controlled study of how LLM output quality changes as input length grows, holding task difficulty fixed. ![report](https://img.shields.io/badge/report-555?style=flat-square)
- [ContextBudget - context management as a budget-constrained sequential decision](https://arxiv.org/abs/2604.01664) - ContextBudget's BACM method has an agent decide when and how much to compress its history based on remaining context budget, not a fixed rule. ![paper](https://img.shields.io/badge/paper-555?style=flat-square)
- [Cursor vendor-native context management - dynamic context discovery + Composer self-summarization](https://cursor.com/blog/dynamic-context-discovery) - Cursor's dynamic context discovery loads tool schemas and large outputs on demand instead of eagerly, a change the vendor reports cut context usage by 46.9%.
- [Repomix](https://github.com/yamadashy/repomix) - Packs an entire repository into a single AI-friendly file, reporting token counts and using Tree-sitter to compress code to signatures only. ![tool: MIT](https://img.shields.io/badge/tool-MIT-blue?style=flat-square) ![stars](https://img.shields.io/github/stars/yamadashy/repomix?style=flat-square&logo=github&label=) ![last commit](https://img.shields.io/github/last-commit/yamadashy/repomix?style=flat-square&label=)
- [RULER - the "real context size" long-context benchmark](https://github.com/NVIDIA/RULER) - NVIDIA's RULER benchmark found that of models claiming 32K+ token context windows, only half actually maintain quality once you fill them to 32K. ![bench](https://img.shields.io/badge/bench-555?style=flat-square) ![stars](https://img.shields.io/github/stars/NVIDIA/RULER?style=flat-square&logo=github&label=) ![last commit](https://img.shields.io/github/last-commit/NVIDIA/RULER?style=flat-square&label=)
- [Self-Compacting Language Model Agents](https://arxiv.org/abs/2606.23525) - This paper introduces SELFCOMPACT: instead of fixed-interval summarization, the model itself decides when and how to compress a growing agent trace. ![paper](https://img.shields.io/badge/paper-555?style=flat-square)
- [Serena](https://github.com/oraios/serena) - An open-source (MIT) MCP toolkit that gives a coding agent IDE-grade semantic code retrieval and editing: 'the IDE for your coding agent'. ![tool: MIT](https://img.shields.io/badge/tool-MIT-blue?style=flat-square) ![stars](https://img.shields.io/github/stars/oraios/serena?style=flat-square&logo=github&label=) ![last commit](https://img.shields.io/github/last-commit/oraios/serena?style=flat-square&label=)

### Cost Controls

- [Harness-side runaway-loop cost guardrails (Claude Code + Codex, July 2026)](https://github.com/anthropics/claude-code/releases/tag/v2.1.212) - In mid-July 2026 both dominant coding CLIs shipped first-party guardrails against runaway agent loops within days of each other.

### Gateways And Proxies

- [Bifrost (Maxim AI)](https://github.com/maximhq/bifrost) - Bifrost is a Go-based AI gateway fronting 1000+ models that measured just 11 microseconds of added latency per request at 5,000 requests per second. ![tool: Apache-2.0](https://img.shields.io/badge/tool-Apache--2.0-blue?style=flat-square) ![stars](https://img.shields.io/github/stars/maximhq/bifrost?style=flat-square&logo=github&label=) ![last commit](https://img.shields.io/github/last-commit/maximhq/bifrost?style=flat-square&label=)
- [Cloudflare AI Gateway (Spend Limits)](https://developers.cloudflare.com/ai-gateway/features/spend-limits/) - Cloudflare AI Gateway is an edge-native LLM proxy that added dollar-denominated spend limits in June 2026, blocking or rerouting requests once a budget is hit. ![co](https://img.shields.io/badge/co-555?style=flat-square)
- [Helicone](https://helicone.ai) - An open-source (Apache-2.0) LLM proxy that logs every request's cost, latency, and tokens in one line of code; Mintlify acquired it in March 2026. ![tool: Apache-2.0](https://img.shields.io/badge/tool-Apache--2.0-blue?style=flat-square)
- [Kong AI Gateway](https://developer.konghq.com/ai-gateway/) - The AI layer of Kong's API-gateway platform: a proxy that meters LLM/agent/MCP traffic for billing, showback, and chargeback. ![co](https://img.shields.io/badge/co-555?style=flat-square)
- [LiteLLM](https://github.com/BerriAI/litellm) - An open-source gateway fronting 100+ LLM APIs that computes real per-request dollar cost from a live pricing map, with spend limits. ![tool: MIT](https://img.shields.io/badge/tool-MIT-blue?style=flat-square) ![stars](https://img.shields.io/github/stars/BerriAI/litellm?style=flat-square&logo=github&label=) ![last commit](https://img.shields.io/github/last-commit/BerriAI/litellm?style=flat-square&label=)
- [OpenRouter](https://openrouter.ai/docs/guides/routing/provider-selection) - A unified API gateway fronting 400+ models across 70+ providers that auto-routes each request by price, with fallback on outages. ![co](https://img.shields.io/badge/co-555?style=flat-square)
- [Portkey AI Gateway](https://portkey.ai/docs/product/ai-gateway/virtual-keys/budget-limits) - Routes LLM traffic across providers and enforces hard USD budget limits on virtual keys, auto-expiring a key once its cap is hit. ![co](https://img.shields.io/badge/co-555?style=flat-square)

### Memory

- [Cognee](https://github.com/topoteretes/cognee) - An open-source (Apache-2.0) AI-memory platform giving agents persistent memory via a self-hosted knowledge graph, via remember/recall/forget. ![tool: Apache-2.0](https://img.shields.io/badge/tool-Apache--2.0-blue?style=flat-square) ![stars](https://img.shields.io/github/stars/topoteretes/cognee?style=flat-square&logo=github&label=) ![last commit](https://img.shields.io/github/last-commit/topoteretes/cognee?style=flat-square&label=)
- [Karpathy's LLM Wiki](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) - Andrej Karpathy's LLM Wiki pattern has an agent build and maintain a persistent markdown wiki from your sources, instead of re-retrieving raw files.
- [Mem0](https://github.com/mem0ai/mem0) - An open-source memory layer that extracts salient facts from conversations and retrieves only the relevant ones per call, not the full history. ![tool: Apache-2.0](https://img.shields.io/badge/tool-Apache--2.0-blue?style=flat-square) ![stars](https://img.shields.io/github/stars/mem0ai/mem0?style=flat-square&logo=github&label=) ![last commit](https://img.shields.io/github/last-commit/mem0ai/mem0?style=flat-square&label=)

### Multi Agent Systems

- [Framework orchestration overhead (the manager-LLM tax)](https://docs.crewai.com/en/learn/hierarchical-process) - Hierarchical frameworks like CrewAI add a manager-LLM delegation tax, an extra model that plans and validates, though its cost is unquantified in any primary.
- [SupervisorAgent - "Stop Wasting Your Tokens" (runtime supervision)](https://arxiv.org/abs/2510.26585) - SupervisorAgent is a lightweight, modular framework for runtime, adaptive supervision of multi-agent systems. ![paper](https://img.shields.io/badge/paper-555?style=flat-square)

### Prompt Agent Loop

- [LOOP Skill Engine](https://arxiv.org/abs/2605.14237) - LOOP records an agent's first run of a repetitive task with full LLM reasoning, then replays the extracted tool-call template without calling the LLM again. ![paper](https://img.shields.io/badge/paper-555?style=flat-square)
- [Orchestrator-worker model tiering (frontier plans / cheap executes)](https://www.mindstudio.ai/blog/smart-orchestrator-cheaper-sub-agent-models-claude-code) - A capable model plans while cheaper agents execute; the pattern now ships as a vendor default, hitting 89.7% of LLM quality at 4% of the cost.
- [token-ninja](https://github.com/oanhduong/token-ninja) - Intercepts deterministic commands like git status or npm test before they reach the model, running them locally and skipping the LLM call. ![tool: MIT](https://img.shields.io/badge/tool-MIT-blue?style=flat-square) ![stars](https://img.shields.io/github/stars/oanhduong/token-ninja?style=flat-square&logo=github&label=) ![last commit](https://img.shields.io/github/last-commit/oanhduong/token-ninja?style=flat-square&label=)

### Retry And Reliability

- [Claude Code v2.1.199 - transient-retry hardening & partial-output preservation](https://github.com/anthropics/claude-code/releases/tag/v2.1.199) - Claude Code v2.1.199 now auto-retries rate-limit errors with backoff and raised the default retry ceiling to 300, up from a prior cap of 15.

### Routing Model Selection

- [Claude Code via a LiteLLM gateway (cheap-tier-in-front setup)](https://docs.litellm.ai/docs/tutorials/claude_non_anthropic_models) - Pointing Claude Code's ANTHROPIC_BASE_URL at a local LiteLLM proxy lets cheaper or non-Anthropic models absorb work the frontier model would otherwise bill for.
- [Cluster, Route, Escalate - cost-aware cascaded serving](https://arxiv.org/abs/2606.27457) - This paper proposes a two-stage cost-aware cascade for LLM serving that combines routing and escalation into one framework. ![paper](https://img.shields.io/badge/paper-555?style=flat-square)
- [Distilling agent behavior into small task-specific models](https://arxiv.org/abs/2505.17612) - Distilling a large agent's behavior into a small 0.5-3B model lets most of its work run at a fraction of the frontier model's per-token cost.
- [MTRouter - per-turn cost-aware routing with history-model joint embeddings](https://arxiv.org/abs/2604.23530) - MTRouter picks a different model for each turn of a multi-turn conversation, rather than one model per query, to hit a cost budget without losing quality. ![paper](https://img.shields.io/badge/paper-555?style=flat-square)
- [Not Diamond](https://www.notdiamond.ai/) - Not Diamond's meta-model predicts, per input, which LLM will give the best answer at the lowest cost, then routes the request there. ![co](https://img.shields.io/badge/co-555?style=flat-square)
- [OpenCode - open-source coding-agent CLI with explicit cost-tier routing](https://opencode.ai/docs/) - OpenCode is an open-source (MIT) coding-agent CLI with its own explicit cost- and model-routing configuration, set directly in config. ![tool: MIT](https://img.shields.io/badge/tool-MIT-blue?style=flat-square)
- [OrcaRouter - production LinUCB bandit router (hybrid offline-online)](https://arxiv.org/abs/2605.30736) - OrcaRouter is a production LLM router built on a LinUCB bandit, with its cost/quality tradeoff independently confirmed on the RouterArena leaderboard. ![paper](https://img.shields.io/badge/paper-555?style=flat-square)
- [RouteLLM](https://github.com/lm-sys/RouteLLM) - LMSYS's open-source router sending each query to a cheap or expensive model based on a trained cost threshold, as a drop-in server. ![tool: Apache-2.0](https://img.shields.io/badge/tool-Apache--2.0-blue?style=flat-square) ![stars](https://img.shields.io/github/stars/lm-sys/RouteLLM?style=flat-square&logo=github&label=) ![last commit](https://img.shields.io/github/last-commit/lm-sys/RouteLLM?style=flat-square&label=)
- [ruflo (formerly Claude-Flow; npm `claude-flow` v3.17.0) - agent meta-harness with cost-adjusted model routing](https://github.com/ruvnet/ruflo) - ruflo is the leading open-source agent meta-harness for Claude Code and Codex, providing swarm orchestration and persistent memory. ![tool: MIT](https://img.shields.io/badge/tool-MIT-blue?style=flat-square) ![stars](https://img.shields.io/github/stars/ruvnet/ruflo?style=flat-square&logo=github&label=) ![last commit](https://img.shields.io/github/last-commit/ruvnet/ruflo?style=flat-square&label=)
- [vLLM Semantic Router](https://github.com/vllm-project/semantic-router) - Sends routine queries to cheap or local models and hard ones to stronger backends, as an open-source, self-hostable router. ![tool: Apache-2.0](https://img.shields.io/badge/tool-Apache--2.0-blue?style=flat-square) ![stars](https://img.shields.io/github/stars/vllm-project/semantic-router?style=flat-square&logo=github&label=) ![last commit](https://img.shields.io/github/last-commit/vllm-project/semantic-router?style=flat-square&label=)

### Serving Inference

- [RLM-Cascade - response-level speculative decoding at the gateway](https://arxiv.org/abs/2606.22840) - RLM-Cascade, from a PayPal team, has a cheap draft model answer first and an Opus 4.8 verifier accept or rewrite it, at roughly 2% of Opus's cost. ![paper](https://img.shields.io/badge/paper-555?style=flat-square)
- [SGLang](https://github.com/sgl-project/sglang) - A high-performance serving framework for large language and multimodal models. ![tool: Apache-2.0](https://img.shields.io/badge/tool-Apache--2.0-blue?style=flat-square) ![stars](https://img.shields.io/github/stars/sgl-project/sglang?style=flat-square&logo=github&label=) ![last commit](https://img.shields.io/github/last-commit/sgl-project/sglang?style=flat-square&label=)
- [vLLM](https://github.com/vllm-project/vllm) - The canonical open-source LLM serving engine, using PagedAttention to manage KV-cache memory in blocks so more requests batch at lower cost. ![tool: Apache-2.0](https://img.shields.io/badge/tool-Apache--2.0-blue?style=flat-square) ![stars](https://img.shields.io/github/stars/vllm-project/vllm?style=flat-square&logo=github&label=) ![last commit](https://img.shields.io/github/last-commit/vllm-project/vllm?style=flat-square&label=)

### Test Time Compute

- [Stop When Reasoning Converges](https://arxiv.org/abs/2605.17672) - Reasoning models often keep generating steps after a solution has already stabilized, wasting tokens and adding latency - what this paper calls "overthink.". ![paper](https://img.shields.io/badge/paper-555?style=flat-square)
- [When more reasoning hurts - the test-time-compute ceiling](https://arxiv.org/abs/2604.10739) - Two 2026 papers found giving a model more reasoning budget makes it perform worse and cost more; past a point, tool delegation wins outright. ![paper](https://img.shields.io/badge/paper-555?style=flat-square)

### Tool Protocol Overhead

- [Code execution with MCP (Anthropic)](https://www.anthropic.com/engineering/code-execution-with-mcp) - Anthropic proposes agents call MCP servers by writing and executing code instead of a tool call per step, so unused tool schemas skip the context window.
- [MCP Tool Descriptions Are Smelly!](https://arxiv.org/abs/2602.14878) - This study found poorly-written MCP tool descriptions measurably hurt agent efficiency, using an LLM-jury scanner and an A/B protocol on MCP-Universe. ![paper](https://img.shields.io/badge/paper-555?style=flat-square)
- [Tool Attention Is All You Need](https://arxiv.org/abs/2604.21816) - MCP re-sends every tool's full schema on every turn, whether or not the agent needs it - a protocol tax known as the MCP/Tools Tax. ![paper](https://img.shields.io/badge/paper-555?style=flat-square)

## Govern

### Allocation Chargeback

- [CloudZero](https://www.cloudzero.com/blog/ai-cost-optimization-at-scale/) - An established commercial cloud and AI cost-intelligence / FinOps platform that brands itself 'The AI ROI Company'. ![co](https://img.shields.io/badge/co-555?style=flat-square)
- [JetBrains AI moves business plans from monthly licenses to 12-month credits](https://blog.jetbrains.com/blog/2026/07/07/jetbrains-ai-for-teams-and-organizations-from-fragmented-ai-usage-to-coordinated-software-development/) - JetBrains is moving business AI from monthly per-seat licenses to 12-month reallocatable credits plus a governance dashboard; personal Pro/Ultimate prices are…
- [Mavvrik (fmr. DigitalEx)](https://www.mavvrik.ai/press-releases/mavvrik-unveils-full-stack-ai-cost-governance/) - Mavvrik is an AI/hybrid-infrastructure cost governance and FinOps platform, rebranded from DigitalEx in February 2025. ![co](https://img.shields.io/badge/co-555?style=flat-square)
- [Pay-i](https://docs.pay-i.com/) - An SDK-based GenAI cost-observability platform that tracks token-level spend per call and rolls it up into cost-center allocation across orgs and apps. ![co](https://img.shields.io/badge/co-555?style=flat-square)

### Anomaly Detection

- [Denial-of-Wallet / token-exhaustion attacks](https://arxiv.org/abs/2601.10955) - Denial-of-wallet attacks exploit pay-per-token pricing to inflate a bill, via stolen-credential LLMjacking or agents steered into runaway token use. ![paper](https://img.shields.io/badge/paper-555?style=flat-square)
- [Governance Decay - compaction silently erasing safety/governance constraints](https://arxiv.org/abs/2606.22528) - Compacting an agent's context can silently erase governance rules: across 7 model families, violations rose from 0% to 30%, up to 59% for some. ![paper](https://img.shields.io/badge/paper-555?style=flat-square)

### Billing Audit Finops

- [FinOps for AI - canonical practitioner framework for governing AI/LLM spend](https://www.finops.org/framework/scope/finops-for-ai/) - FinOps for AI is the FinOps Foundation's official practitioner framework for governing AI, GPU, and token spend. ![tool](https://img.shields.io/badge/tool-blue?style=flat-square)
- [Vaudit - TokenAudit (LLM invoice reconciliation / AI spend audit)](https://www.vaudit.com/) - Vaudit is an AI-native, independent spend-auditing and recovery platform (San Francisco, founded late 2023). ![co](https://img.shields.io/badge/co-555?style=flat-square)

### Budgets Caps

- [AEGIS](https://github.com/Justin0504/Aegis) - An open-source (MIT) pre-execution firewall and cryptographic audit layer for AI agents. ![tool: MIT](https://img.shields.io/badge/tool-MIT-blue?style=flat-square) ![stars](https://img.shields.io/github/stars/Justin0504/Aegis?style=flat-square&logo=github&label=) ![last commit](https://img.shields.io/github/last-commit/Justin0504/Aegis?style=flat-square&label=)
- [Claude Code's 5-hour/weekly usage quotas - Anthropic has stopped publishing exact numbers](https://support.claude.com/en/articles/11049741-what-is-the-max-plan) - Anthropic stopped publishing exact Claude Code usage quotas, describing Max plans only as 5x/20x multipliers of Pro with no absolute numbers.
- [TrueFoundry (AI Gateway - Budget Limiting)](https://www.truefoundry.com/docs/ai-gateway/budgetlimiting) - TrueFoundry is an enterprise GenAI deployment/gateway company founded by ex-Meta founders. ![co](https://img.shields.io/badge/co-555?style=flat-square)

### Energy Carbon

- [CodeCarbon](https://github.com/mlco2/codecarbon) - An open-source (MIT) library for estimating a workload's energy use and CO2e emissions, and ML's widely-cited carbon baseline. ![tool: MIT](https://img.shields.io/badge/tool-MIT-blue?style=flat-square) ![stars](https://img.shields.io/github/stars/mlco2/codecarbon?style=flat-square&logo=github&label=) ![last commit](https://img.shields.io/github/last-commit/mlco2/codecarbon?style=flat-square&label=)
- [EcoLogits - energy/carbon of LLM *API* calls (the hosted-usage estimator)](https://github.com/mlco2/ecologits) - Estimates the energy and carbon footprint of calling generative-AI APIs: the hosted counterpart to CodeCarbon, which measures your own hardware. ![tool: MPL-2.0](https://img.shields.io/badge/tool-MPL--2.0-blue?style=flat-square) ![stars](https://img.shields.io/github/stars/mlco2/ecologits?style=flat-square&logo=github&label=) ![last commit](https://img.shields.io/github/last-commit/mlco2/ecologits?style=flat-square&label=)
- [Epoch AI - how much energy a query uses (the per-token energy anchor)](https://epoch.ai/gradient-updates/how-much-energy-does-chatgpt-use) - Epoch AI built a transparent, first-principles estimate of how much energy one LLM query costs.
- [Google - measuring the environmental impact of AI inference (provider disclosure)](https://cloud.google.com/blog/products/infrastructure/measuring-the-environmental-impact-of-ai-inference) - Google published a first-party disclosure of the energy, carbon, and water cost of a median Gemini Apps text prompt, authored by Amin Vahdat and Jeff Dean. ![report](https://img.shields.io/badge/report-555?style=flat-square)
- [ML.ENERGY Leaderboard v3.0 - measured inference energy (the "reasoning ≈ 25× energy" signal)](https://ml.energy/blog/measurement/energy/diagnosing-inference-energy-consumption-with-the-mlenergy-leaderboard-v30/) - Version 3.0 of this leaderboard measures real GPU inference energy across 46 models x 7 tasks, finding reasoning models use roughly 25x the energy of others. ![bench](https://img.shields.io/badge/bench-555?style=flat-square)

### Policy Enforcement

- [ActPlane](https://github.com/eunomia-bpf/ActPlane) - An eBPF-based, OS-level policy-enforcement engine for AI-agent harnesses like Claude Code and Codex. ![tool: MIT](https://img.shields.io/badge/tool-MIT-blue?style=flat-square) ![stars](https://img.shields.io/github/stars/eunomia-bpf/ActPlane?style=flat-square&logo=github&label=) ![last commit](https://img.shields.io/github/last-commit/eunomia-bpf/ActPlane?style=flat-square&label=)
- [MCPGuard-Dynamic](https://github.com/facebook/mcpguard-dynamic) - Meta's open-source kernel-level eBPF sandbox built specifically for MCP. ![tool: MIT](https://img.shields.io/badge/tool-MIT-blue?style=flat-square) ![stars](https://img.shields.io/github/stars/facebook/mcpguard-dynamic?style=flat-square&logo=github&label=) ![last commit](https://img.shields.io/github/last-commit/facebook/mcpguard-dynamic?style=flat-square&label=)

### Spend Management

- [ChatGPT Enterprise - usage analytics & spend controls](https://openai.com/index/chatgpt-enterprise-spend-controls/) - OpenAI's first-party spend layer for ChatGPT Enterprise/Business: a Global Admin Console with credit caps, request workflows, and a Cost API. ![tool: proprietary](https://img.shields.io/badge/tool-proprietary-blue?style=flat-square)
- [Claude Enterprise - admin analytics & cost controls](https://www.claude.com/blog/giving-admins-more-visibility-and-control-over-claude-usage-and-spend) - Anthropic's first-party spend surface for Claude Enterprise/Team admins: org-level spend caps, model defaults, and per-user cost analytics via the Admin API. ![tool: proprietary](https://img.shields.io/badge/tool-proprietary-blue?style=flat-square)
- [PointFive (AI Efficiency OS / TokenShift)](https://www.pointfive.co/press/pointfive-launches-ai-efficiency-os-tokenshift) - PointFive's TokenShift governs coding-agent token spend across Claude Code, Cursor, Codex, and more, claiming a 10-20% cut across 11 partners. ![co](https://img.shields.io/badge/co-555?style=flat-square)
- [Revenium - runtime AI economic control / spend management](https://www.revenium.ai/) - Revenium tracks AI agent spend at runtime to the cent, attributing every model call and tool cost to its workflow, with auto-shutoff on runaway budgets. ![co](https://img.shields.io/badge/co-555?style=flat-square)
- [Vantage](https://www.vantage.sh/blog/agentic-coding-costs) - A FinOps platform ingesting native token-level cost data from Anthropic and OpenAI's own usage APIs, plus Cursor and cloud spend. ![co](https://img.shields.io/badge/co-555?style=flat-square)
- [Vercel AI Gateway - per-API-key budgets](https://vercel.com/changelog/budgets-for-api-keys-on-ai-gateway) - Vercel AI Gateway lets you cap spend per API key in dollars (min $1) with a daily/weekly/monthly refresh, rejecting further requests once the cap is hit. ![tool: proprietary](https://img.shields.io/badge/tool-proprietary-blue?style=flat-square)

## Understand

### Buyer Incentives

- [Claude "subscription arbitrage" and its (announced, then paused) end](https://zed.dev/blog/anthropic-subscription-changes) - Users route agentic workloads worth far more than a subscription's price through cheap Pro/Max plans; Anthropic tried to close this, then paused the fix.
- [Coding-agent native spend controls (2026)](https://cursor.com/changelog/05-04-26) - Within six weeks in 2026, Cursor, GitHub Copilot, and OpenAI each shipped native admin spend controls: budget caps, credit metering, usage dashboards. (also: [GitHub Copilot](https://github.blog/news-insights/company-news/github-copilot-is-moving-to-usage-based-billing/) · [OpenAI](https://openai.com/index/chatgpt-enterprise-spend-controls/))
- [GitHub Copilot metered-billing bill-shock - the demand-side reaction ("tokenpocalypse")](https://news.ycombinator.com/item?id=47923357) - GitHub's move from flat-rate Copilot plans to metered AI Credits exposed agentic workflows' true per-token cost and triggered a mass bill-shock backlash.
- [Lanai](https://www.prnewswire.com/news-releases/lanai-launches-ai--work-operating-system-to-help-enterprises-close-the-ai-accountability-gap-302743892.html) - Lanai's AI @ Work platform discovers every sanctioned and shadow AI workflow across an org and maps its token spend to the KPIs it actually drives. ![co](https://img.shields.io/badge/co-555?style=flat-square)
- [State of FinOps 2026 - AI spend management is now the norm](https://data.finops.org/) - This is the FinOps Foundation's sixth annual State of FinOps survey, the practitioner census of how organizations manage cloud and AI spend. ![report](https://img.shields.io/badge/report-555?style=flat-square)
- [The "$47k Claude Code bill" - the anchor bill-shock anecdote and its mechanistic debunk](https://yusufhansacak.medium.com/the-47-000-agent-bill-what-the-viral-token-stories-get-wrong-7ee1cdd81e65) - A viral $47,000-in-90-days Claude Code bill story was debunked by a teardown pinning the real driver on quadratic context re-ingestion, not runaway use.
- [Uber caps AI-coding spend at $1,500/mo per tool after burning its budget in ~4 months](https://techcrunch.com/2026/06/02/uber-caps-employee-ai-spending-after-blowing-through-budget-in-four-months/) - Uber capped AI-coding spend at $1,500 per employee per tool after burning its entire annual budget in roughly four months of encouraged maximal use.

### Compression Efficacy

- [JetBrains independently measured two token-saving skills against their own claims](https://blog.jetbrains.com/ai/2026/07/rtk-claude-code-token-savings/) - JetBrains independently A/B-tested two token-saving skills: rtk ran +7.6% more expensive at low effort (claimed 60-90% cut), Caveman saved ~8.5% (claimed 65%). (also: [Caveman A/B post](https://blog.jetbrains.com/ai/2026/07/speak-to-ai-agents-like-cavemen-tosave-tokens/)) ![bench](https://img.shields.io/badge/bench-555?style=flat-square)
- [Token-saving plugins are mostly a stupid idea (Tura benchmark)](https://turaai.net/blog#token-saving-plugins-are-mostly-stupid-idea) - A benchmark of token-saving plugins found one actively worse than none: cost up 7.2%, tokens up 13.2%, because it broke an already-cached prompt prefix.

### Consolidation

- [Cisco acquires Galileo (LLM eval/observability) → folded into Splunk Observability](https://blogs.cisco.com/news/cisco-announces-the-intent-to-acquire-galileo) - Cisco acquired Galileo, an LLM/agent evaluation and observability platform, folding it into Splunk Observability Cloud's AI Agent Monitoring. ![co](https://img.shields.io/badge/co-555?style=flat-square)
- [Tokenomics Foundation (Linux Foundation + FinOps Foundation)](https://www.linuxfoundation.org/press/linux-foundation-announces-the-intent-to-launch-the-tokenomics-foundation-to-establish-open-standards-for-ai-cost-management) - The Linux Foundation is launching the Tokenomics Foundation to build open standards for AI token spend, extending FOCUS to cover token-based costs. ![co](https://img.shields.io/badge/co-555?style=flat-square)

### Market Competitors

- [Amp (Sourcegraph) - pay-as-you-go, no-markup pricing + mode-based routing](https://ampcode.com/) - Amp, Sourcegraph's coding agent, passes through LLM cost with zero markup for individuals and teams, with a cost/capability mode: Deep, Smart, or Rush. ![tool](https://img.shields.io/badge/tool-blue?style=flat-square)
- [Factory (droids) - subscription pricing + $150M Series C at $1.5B](https://factory.ai/pricing) - Factory prices its Droids agents as flat subscription tiers ($20/$100/$200/mo) with usage-based rate limits, not per-token metering, after a $150M round. ![co](https://img.shields.io/badge/co-555?style=flat-square)
- [Gemini CLI retirement → Antigravity CLI (open-source coding agent closes, pricing restructures)](https://developers.googleblog.com/an-important-update-transitioning-gemini-cli-to-antigravity-cli/) - Google retired the open-source Gemini CLI on 2026-06-18, pushing users onto closed-source Antigravity CLI and $100/$200-per-month paid tiers. ![tool](https://img.shields.io/badge/tool-blue?style=flat-square)
- [OpenHands - MIT OSS coding agent, free local + free cloud tier, at-cost LLM option](https://github.com/OpenHands/OpenHands) - An MIT-licensed open-source coding-agent platform with a free local mode, a free cloud tier, and an at-cost LLM pricing option. ![tool: MIT](https://img.shields.io/badge/tool-MIT-blue?style=flat-square) ![stars](https://img.shields.io/github/stars/OpenHands/OpenHands?style=flat-square&logo=github&label=) ![last commit](https://img.shields.io/github/last-commit/OpenHands/OpenHands?style=flat-square&label=)

### Market Sizing

- [Gartner - worldwide AI spending forecast: $2.59T in 2026 (+47% YoY)](https://www.gartner.com/en/newsroom/press-releases/2026-05-19-gartner-forecasts-worldwide-ai-spending-to-grow-47-percent-in-2026) - Gartner's latest forecast puts worldwide AI spending at $2.59 trillion in 2026, up 47% year-over-year, with infrastructure over 45% of the total. ![report](https://img.shields.io/badge/report-555?style=flat-square)
- [Menlo Ventures - enterprise generative-AI spend $11.5B → $37B (2024→2025)](https://menlovc.com/perspective/2025-the-state-of-generative-ai-in-the-enterprise/) - Menlo Ventures found enterprise generative-AI spend hit $37B in 2025, up 3.2x from 2024, with coding tools the largest application category at $7.3B. ![report](https://img.shields.io/badge/report-555?style=flat-square)

### Model Economics

- ["Qwen 3.6 27B is the sweet spot for local development" - Migdał / Quesma (first-party)](https://quesma.com/blog/qwen-36-is-awesome/) - Piotr Migdał's #1-on-Hacker-News essay argues Qwen3.6-27B (dense) is the first local model good enough for real coding instead of a metered cloud API.
- [Artificial Analysis - Coding Agent Index (tokens & cost per task, model × harness)](https://artificialanalysis.ai/agents/coding-agents) - This benchmark scores full model-plus-harness stacks, spanning $0.27 to $11.80 per task: a roughly 44x range at similar quality, per Artificial Analysis. ![bench](https://img.shields.io/badge/bench-555?style=flat-square)
- [Artificial Analysis - Intelligence Index + Blended Price (intelligence-per-dollar leaderboard)](https://artificialanalysis.ai/leaderboards/models) - Artificial Analysis's Intelligence Index plots a 0-100 capability score against blended price per million tokens, live across 85-122 base LLMs. ![bench](https://img.shields.io/badge/bench-555?style=flat-square)
- [Kimi K2.6/K2.7-Code and GLM-5.2 official API pricing](https://platform.kimi.ai/docs/pricing/chat-k27-code) - Kimi K2.7-Code ($0.95/$4.00 per million tokens) and GLM-5.2 ($1.40/$4.40) both undercut Claude Sonnet 5 and GPT-5.5 on raw price by 2-5x.
- [Local / open-model economics for coding - state of the field (2026)](https://huggingface.co/Qwen/Qwen3.6-27B) - Open-weight coding models now score 77-81% on SWE-bench Verified, within a few points of closed frontier models, reshaping self-host-vs-API math.
- [OckBench - measuring token efficiency / verbosity of LLM reasoning](https://arxiv.org/abs/2511.05722) - OckBench answers a specific tokenomics question: which model burns the most tokens for the same answer? ![paper](https://img.shields.io/badge/paper-555?style=flat-square)
- [Reasoning-token billing across providers - the hidden output multiplier](https://developers.openai.com/api/docs/guides/reasoning) - Every major AI provider bills a model's hidden reasoning tokens at the most expensive output rate, without ever returning them to the caller. (also: [Google](https://ai.google.dev/gemini-api/docs/pricing) · [DeepSeek](https://api-docs.deepseek.com/guides/reasoning_model))
- [Reasoning-token consumption behavior - length ≠ effort, and verbosity is a separate lever](https://arxiv.org/abs/2602.13517) - Chain-of-thought can burn about 258 tokens on problems a direct answer solves in 15 (roughly 17x overhead), and simple agentic steps trigger it by accident. ![paper](https://img.shields.io/badge/paper-555?style=flat-square)

### Pricing Models

- [Batch / Priority / Flex service tiers - the scheduling axis of token pricing (clustered, cross-vendor)](https://platform.claude.com/docs/en/docs/build-with-claude/batch-processing) - Every major LLM vendor sells the same lever, trading latency for price via async batch scheduling, with Anthropic, OpenAI, and Google all near 50% off. (also: [OpenAI](https://developers.openai.com/api/docs/pricing) · [Google](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/partner-models/claude/batch))
- [Bessemer - the AI pricing & monetization playbook (seat → usage → outcome)](https://www.bvp.com/atlas/the-ai-pricing-and-monetization-playbook) - Bessemer's playbook argues AI pricing is shifting from per-seat to consumption/outcome-based, citing Intercom's $0.99-per-resolved-ticket model.
- [Cached-input discounts - the ~90%-off lever behind cache-accounting](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) - Cache-read pricing discounts input tokens by about 90%: the biggest lever on an agentic bill, since input is roughly 85% of session cost.
- [ChatGPT subscription tiers and Codex CLI bundling/pricing (2026)](https://developers.openai.com/codex/pricing) - OpenAI bundles Codex CLI into every ChatGPT tier from Free through the new $100/mo Pro plan, differing only by rate-limit multiplier.
- [ChatGPT workspace-agent credit billing (effective July 6, 2026)](https://help.openai.com/en/articles/11481834-chatgpt-rate-card) - OpenAI ended the free preview for agent runs invoked inside ChatGPT Business, Enterprise, Edu, and Teachers on 2026-07-06.
- [Cursor charges by tokens, split into first-party and third-party pools](https://cursor.com/docs/account/pricing) - Cursor meters by tokens per million (input/output/cache-write/cache-read), split into a first-party pool and a third-party API pool, with a $0.25/M Teams… (also: [Teams pricing blog](https://cursor.com/blog/teams-pricing-june-2026))
- [Devin's Agent Compute Unit has no published definition of what it meters](https://docs.devin.ai/admin/billing/enterprise) - Devin bills Enterprise usage in Agent Compute Units, but no official doc defines what an ACU measures (not tokens, seconds, or calls); the opacity itself is the…
- [Fable 5 leaves subscription inclusion - frontier tier moves to usage-credit metering (July 7 cliff)](https://www.anthropic.com/news/redeploying-fable-5) - Anthropic is moving Fable 5 off subscription-included access onto usage-credit metering, with the cliff date slipped twice, now set for 2026-07-20.
- [Google AI Pro price and Gemini/Antigravity free-tier limits (2026)](https://gemini.google/subscriptions/) - Google AI Pro is confirmed at $19.99/month, beneath the $99.99 and $199.99 AI Ultra tiers giving higher rate limits on the Gemini API and Antigravity.
- [GPT-5.6 family (Sol / Terra / Luna) - API pricing](https://developers.openai.com/api/docs/pricing) - OpenAI's GPT-5.6 family prices three tiers 2x apart: Sol at $5/$30 per million tokens, Terra at $2.50/$15, and Luna at $1/$6.
- [LiteLLM flex/priority service-tier cost keys - the harness-level tier-routing lever](https://docs.litellm.ai/docs/proxy/custom_pricing) - LiteLLM automatically prices requests made at a non-standard tier like flex or priority, applying the right discounted or premium rate automatically.
- [LLM price decline + Jevons paradox - unit price crashes, total spend climbs](https://a16z.com/llmflation-llm-inference-cost/) - Per-token prices are falling roughly an order of magnitude per year, while total AI spend rises even faster.
- [LLM token pricing dimensions - the structure of a token bill](https://platform.claude.com/docs/en/about-claude/pricing) - This maps out how frontier LLM APIs meter and price tokens, read straight off the two largest providers' pricing pages, Anthropic and OpenAI.
- [OpenAI is winding down the self-serve fine-tuning API and platform](https://developers.openai.com/api/docs/deprecations) - OpenAI is winding down self-serve fine-tuning because prompting got cheaper and more capable than fine-tuning for most uses, cutting off customers by 2027.
- [Tokenization multiplicity & overcharging - the pay-per-token integrity problem](https://arxiv.org/abs/2506.06446) - Two academic papers show the same output can be billed a different token count depending on tokenization, and providers can be incentivized to inflate it. ![paper](https://img.shields.io/badge/paper-555?style=flat-square)
- [Windsurf became Devin Desktop and switched credits to token-based quota](https://docs.devin.ai/desktop/accounts/quota) - Windsurf became Devin Desktop and in March 2026 swapped opaque per-model credit multipliers for token-based quota where free models cost nothing; a…

### Reliability Sla

- [Reserved-capacity reliability economics (Azure PTU · AWS Bedrock MU)](https://learn.microsoft.com/en-us/azure/ai-foundry/openai/concepts/provisioned-throughput) - Azure's Provisioned Throughput Units and AWS Bedrock's Model Units both let buyers reserve guaranteed capacity, billed hourly whether or not it's used.

### Unit Economics

- [Cloud Capital - gross margin in the age of AI (the vendor/supply side)](https://www.cloudcapital.co/learn/gross-margin-in-the-age-of-ai) - AI-native software runs at roughly 50-60% gross margin versus 70-80% for SaaS, since inference and compute became a large, variable cost of goods sold.
- [Cost-of-Pass - an economic framework for evaluating language models](https://arxiv.org/abs/2504.13359) - Cost-of-Pass defines the expected dollar cost of one correct answer as inference cost divided by success rate, pricing benchmark accuracy directly. ![paper](https://img.shields.io/badge/paper-555?style=flat-square)
- [DORA 2025 - AI as amplifier, and the delivery-stability tension](https://dora.dev/insights/balancing-ai-tensions/) - Google's DORA program found that as AI adoption becomes universal, delivery throughput rises but so does instability: AI as an amplifier, not a pure win. ![report](https://img.shields.io/badge/report-555?style=flat-square)
- [Faros - "The Acceleration Whiplash" (AI Engineering Report 2026)](https://pages.faros.ai/hubfs/AI_Engineering_Report_2026_The_Acceleration_Whiplash_Faros.pdf) - This is the load-bearing "velocity has a hidden bill" study: telemetry from 22,000 developers across 4,000 teams over two years. ![report](https://img.shields.io/badge/report-555?style=flat-square)
- [getDX - AI coding assistant pricing & ROI guide (2026)](https://getdx.com/blog/ai-coding-assistant-pricing/) - Typical AI coding tools cost $200-600 per engineer monthly in seat plus token spend, per getDX, for a median 7.76% PR gain: below vendors' claimed 3-10x.
- [METR - measured vs perceived AI productivity (the RCT)](https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/) - METR's controlled trial found developers took 19% longer to finish issues when allowed to use AI, while still believing it had sped them up by 20%. ![paper](https://img.shields.io/badge/paper-555?style=flat-square)

## Measure

### Benchmarks Evals

- [Claw-SWE-Bench](https://github.com/opensquilla/claw-swe-bench) - Found that adapter/harness design alone swings an agent's Pass@1 score by about 54 percentage points on the identical model backbone. ![bench](https://img.shields.io/badge/bench-555?style=flat-square) ![stars](https://img.shields.io/github/stars/opensquilla/claw-swe-bench?style=flat-square&logo=github&label=) ![last commit](https://img.shields.io/github/last-commit/opensquilla/claw-swe-bench?style=flat-square&label=)
- [Coding Benchmarks Are Misaligned with Agentic SE (Tessl)](https://arxiv.org/abs/2606.17799) - A position paper from Tessl (London, UK) argues that today's coding benchmarks don't measure what people think they measure. ![paper](https://img.shields.io/badge/paper-555?style=flat-square)
- [Deterministic Anchoring - how much static structure do code agents need?](https://arxiv.org/abs/2606.26979) - This ISSTA 2026 paper found injecting static-analysis facts as plain-text comments raises a code agent's Pass@1 by 3.4pp and cuts trajectories by 1.6 rounds. ![paper](https://img.shields.io/badge/paper-555?style=flat-square)
- [GitHub Copilot agentic-harness efficiency evaluation (first-party offline ablation)](https://github.blog/ai-and-ml/github-copilot/evaluating-performance-and-efficiency-of-the-github-copilot-agentic-harness-across-models-and-tasks/) - GitHub's own benchmark plots Copilot's agentic-harness resolution rate against dollar-cost-per-task across five benchmarks and four frontier models. ![report](https://img.shields.io/badge/report-555?style=flat-square)
- [Harness-Bench](https://arxiv.org/abs/2605.27922) - Holds the task, model, and budget fixed while varying only the agent harness, across 5,194 trajectories spanning 6 harnesses and 8 models. ![paper](https://img.shields.io/badge/paper-555?style=flat-square)
- [Prompt Compression in the Wild - the end-to-end referee for compression](https://arxiv.org/abs/2604.02985) - This ECIR 2026 study found LLMLingua's compression yields up to 18% speed-up only in a narrow window; outside it, the compression step cancels the gains. ![paper](https://img.shields.io/badge/paper-555?style=flat-square)
- [promptfoo](https://github.com/promptfoo/promptfoo) - An open-source CLI/CI harness for testing LLM prompts and agents that records per-eval token usage and cost as an assertable metric. ![tool: MIT](https://img.shields.io/badge/tool-MIT-blue?style=flat-square) ![stars](https://img.shields.io/github/stars/promptfoo/promptfoo?style=flat-square&logo=github&label=) ![last commit](https://img.shields.io/github/last-commit/promptfoo/promptfoo?style=flat-square&label=)
- [RedundancyBench - can anyone even *detect* a redundant step?](https://arxiv.org/abs/2605.29893) - RedundancyBench is a benchmark for step-level redundancy detection in agent trajectories - can a model even spot the wasted step in an agent's history? ![paper](https://img.shields.io/badge/paper-555?style=flat-square)
- [RouterArena - the open benchmark + live leaderboard for LLM routers](https://github.com/RouteWorks/RouterArena) - RouterArena is an open evaluation platform and live leaderboard for LLM routers - systems that auto-select a model per query. ![bench](https://img.shields.io/badge/bench-555?style=flat-square) ![stars](https://img.shields.io/github/stars/RouteWorks/RouterArena?style=flat-square&logo=github&label=) ![last commit](https://img.shields.io/github/last-commit/RouteWorks/RouterArena?style=flat-square&label=)
- [SWE-Effi - cost-aware re-ranking of SWE-agents under resource budgets](https://arxiv.org/abs/2509.09853) - SWE-Effi re-ranks popular AI issue-resolution systems on a SWE-bench subset by cost-under-resource-constraints instead of by accuracy alone. ![paper](https://img.shields.io/badge/paper-555?style=flat-square)
- [Terminal-Bench](https://www.tbench.ai/) - The canonical benchmark for AI agents in real terminal/CLI environments, with 89 tasks each vetted through ~3 reviewer-hours. ![bench](https://img.shields.io/badge/bench-555?style=flat-square)

### Cache Accounting

- [Gemini context caching - the per-hour storage meter (the third-vendor axis)](https://ai.google.dev/gemini-api/docs/pricing) - Among major providers, only Gemini bills a per-hour storage meter for explicit prompt caching, making a cache a rented line item that accrues cost while it sits…
- [OpenAI prompt-caching `cached_tokens` accounting](https://platform.openai.com/docs/guides/prompt-caching) - This is the measurement substrate for prompt-cache savings on the OpenAI API.
- [OpenAI Responses conversation state - you pay for the whole chain every turn (and the compaction levers)](https://developers.openai.com/api/docs/guides/conversation-state) - This entry covers the billing semantics of stateful conversations on OpenAI's Responses API, plus the two server-side compaction levers that mitigate them.

### Cost Anatomy

- [Anthropic bill anatomy - the whole-bill line-item taxonomy](https://platform.claude.com/docs/en/about-claude/pricing#code-execution-tool) - This is the canonical enumeration of every meter on a Claude API bill, read live from Anthropic's pricing page.
- [TensorZero - cross-vendor token-count divergence ("stop comparing $/M tokens")](https://www.tensorzero.com/blog/stop-comparing-price-per-million-tokens-the-hidden-llm-api-costs/) - The same input can produce 2.65x more tokens on one tokenizer than another's: Claude Opus 4-7 runs 1.57x-2.65x more tokens than GPT-5.4 on the same content.
- [Vision-token pricing formulas across the big three](https://platform.claude.com/docs/en/build-with-claude/vision) - Anthropic, OpenAI, and Google each convert an image into billed tokens with a different formula, so no single cross-vendor image-cost number exists. (also: [OpenAI](https://developers.openai.com/api/docs/guides/images-vision) · [Google](https://ai.google.dev/gemini-api/docs/image-understanding))

### Harness Overhead

- [Claude Code system prompts (Piebald extraction)](https://github.com/Piebald-AI/claude-code-system-prompts) - Piebald AI extracts Claude Code's full compiled prompt payload per release: 515 prompt strings and 27 tool descriptions at v2.1.212, each priced in tokens. ![data](https://img.shields.io/badge/data-555?style=flat-square) ![stars](https://img.shields.io/github/stars/Piebald-AI/claude-code-system-prompts?style=flat-square&logo=github&label=) ![last commit](https://img.shields.io/github/last-commit/Piebald-AI/claude-code-system-prompts?style=flat-square&label=)
- [Claude Code vs OpenCode token overhead (Systima study)](https://systima.ai/blog/claude-code-vs-opencode-token-overhead) - Systima measured harness scaffolding overhead before a prompt is even read: Claude Code carries about 32,800 tokens versus OpenCode's 6,900, a 4.7x gap. ![report](https://img.shields.io/badge/report-555?style=flat-square)

### Metering

- [Cross-vendor coding-agent usage trackers (AgentsView · caut)](https://github.com/kenn-io/agentsview) - AgentsView and caut are open-source tools that read local session logs to aggregate token usage and cost across roughly 20 coding-agent vendors. ![tool: MIT](https://img.shields.io/badge/tool-MIT-blue?style=flat-square) ![stars](https://img.shields.io/github/stars/kenn-io/agentsview?style=flat-square&logo=github&label=) ![last commit](https://img.shields.io/github/last-commit/kenn-io/agentsview?style=flat-square&label=)
- [How Do AI Agents Spend Your Money?](https://arxiv.org/abs/2604.22750) - This Stanford study is the first systematic look at token spend in agentic coding, running 8 frontier models on 500 SWE-bench Verified tasks. ![paper](https://img.shields.io/badge/paper-555?style=flat-square)
- [tokview](https://github.com/headroomlabs-ai/tokview) - A local, zero-config proxy showing a coding agent's token spend by session, model, and tool call, flagging re-sent results that multiply the bill. ![tool: MIT](https://img.shields.io/badge/tool-MIT-blue?style=flat-square) ![stars](https://img.shields.io/github/stars/headroomlabs-ai/tokview?style=flat-square&logo=github&label=) ![last commit](https://img.shields.io/github/last-commit/headroomlabs-ai/tokview?style=flat-square&label=)

### Transcript Analysis

- [Early Diagnosis of Wasted Computation in Multi-Agent LLM Systems (Failure-Aware Observability)](https://arxiv.org/abs/2606.01365) - This live waste-detection framework for multi-agent systems found that 58.1% of tokens in failed runs are spent after its first warning fires. ![paper](https://img.shields.io/badge/paper-555?style=flat-square)
- [Faros AI - "Token Intelligence" / Token Attribution Ledger](https://www.faros.ai/blog/token-intelligence-for-ai-engineering) - Faros AI is an enterprise engineering-intelligence SaaS (DORA/SPACE-style productivity analytics). ![co](https://img.shields.io/badge/co-555?style=flat-square)
- [token-optimizer (alexgreensh) - per-session $ waste-detection plugin, semi-cross-vendor](https://github.com/alexgreensh/token-optimizer) - token-optimizer is a coding-agent plugin that runs eleven heuristic waste detectors per session and prices the flagged tokens in dollars. ![tool: PolyForm-Noncommercial-1.0.0](https://img.shields.io/badge/tool-PolyForm--Noncommercial--1.0.0-blue?style=flat-square) ![stars](https://img.shields.io/github/stars/alexgreensh/token-optimizer?style=flat-square&logo=github&label=) ![last commit](https://img.shields.io/github/last-commit/alexgreensh/token-optimizer?style=flat-square&label=)

### Whole Bill Accounting

- [FOCUS 1.4 - the cross-vendor billing-data normalization standard (now with invoice reconciliation)](https://focus.finops.org/focus-specification/) - FOCUS 1.4, the Linux Foundation's billing-data schema, added Invoice Detail and Billing Period datasets to reconcile spend against real invoices. ![tool](https://img.shields.io/badge/tool-blue?style=flat-square)
## Practices

Tool-agnostic, evidence-grounded standards for token-efficient agentic coding. Each is one page: TL;DR, claim, evidence, links. [Browse the practices](practices/README.md).

## Concepts

Short reference notes explaining the ideas behind the practices: cache economics, the harness-waste taxonomy, orchestration economics. [Browse the concepts](concepts/README.md).

## Claims

Confidence-scored beliefs, clearly labeled as beliefs rather than facts, each with its strongest evidence linked. [Read the claims](claims.md).

## Setups and skills

Runnable, validated Claude Code and Codex configurations and skills for token-efficient agentic coding, each labeled with how it was validated. [Browse the setups](setups/README.md).

---

Text content: CC-BY 4.0 ([LICENSE](LICENSE)) · Code and configs: MIT ([LICENSE-CODE](LICENSE-CODE)). Maintained by the team at [Quesma](https://quesma.com).
