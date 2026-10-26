# Monitor

## Dashboards

### Tools
- [antiburn](https://github.com/antiburn/antiburn) - Desktop app for macOS, Windows and Linux that reads local session logs from coding agents, flags token-burn causes, and applies and verifies supported configuration fixes. ![tool: MIT](https://img.shields.io/badge/tool-MIT-blue?style=flat-square) ![last commit](https://img.shields.io/github/last-commit/antiburn/antiburn?style=flat-square&label=)
- [ccusage](https://github.com/ccusage/ccusage) - CLI that reads local agent logs to report token usage and cost across coding-agent sources, with caching-aware pricing. ![tool: MIT](https://img.shields.io/badge/tool-MIT-blue?style=flat-square) ![last commit](https://img.shields.io/github/last-commit/ccusage/ccusage?style=flat-square&label=)
- [Claude Code Usage Monitor](https://github.com/Maciek-roboblog/Claude-Code-Usage-Monitor) - Live terminal dashboard for Claude Code usage with burn-rate analytics, limit detection, and session-expiry forecasts. ![tool: MIT](https://img.shields.io/badge/tool-MIT-blue?style=flat-square) ![last commit](https://img.shields.io/github/last-commit/Maciek-roboblog/Claude-Code-Usage-Monitor?style=flat-square&label=)
- [claude-usage](https://github.com/phuryn/claude-usage) - Local dashboard for Claude Code token usage, costs, and session history. ![tool: MIT](https://img.shields.io/badge/tool-MIT-blue?style=flat-square) ![last commit](https://img.shields.io/github/last-commit/phuryn/claude-usage?style=flat-square&label=)
- [ClaudeBar](https://github.com/tddworks/ClaudeBar) - Menu-bar app for macOS that monitors AI coding quotas across multiple providers. ![tool: Apache-2.0](https://img.shields.io/badge/tool-Apache--2.0-blue?style=flat-square) ![last commit](https://img.shields.io/github/last-commit/tddworks/ClaudeBar?style=flat-square&label=)
- [CodeBurn](https://github.com/getagentseal/codeburn#find-and-fix-waste) - Usage tracker for coding tools whose optimize command flags harness-waste patterns with dollar estimates. ![tool: MIT](https://img.shields.io/badge/tool-MIT-blue?style=flat-square)
- [Codex Usage Tracker](https://github.com/douglasmonsky/codex-usage-tracker) - Local-first MCP tools and evidence console that index Codex CLI session logs into SQLite and report token, credit, allowance, and cost figures, with cached and uncached input split out. ![tool: MIT](https://img.shields.io/badge/tool-MIT-blue?style=flat-square) ![last commit](https://img.shields.io/github/last-commit/douglasmonsky/codex-usage-tracker?style=flat-square&label=)
- [CodexBar](https://github.com/steipete/CodexBar) - Menu-bar app for macOS that shows limits, reset timers, credit balances, and spending across AI providers. ![tool: MIT](https://img.shields.io/badge/tool-MIT-blue?style=flat-square) ![last commit](https://img.shields.io/github/last-commit/steipete/CodexBar?style=flat-square&label=)
- [CodeZeno Usage Monitor](https://github.com/CodeZeno/Claude-Code-Usage-Monitor) - Windows taskbar widget that shows Claude Code quota and usage without opening a terminal. ![tool: MIT](https://img.shields.io/badge/tool-MIT-blue?style=flat-square) ![last commit](https://img.shields.io/github/last-commit/CodeZeno/Claude-Code-Usage-Monitor?style=flat-square&label=)
- [Datadog LLM Observability Cost](https://docs.datadoghq.com/llm_observability/monitoring/cost/) - Datadog documentation on per-request LLM cost estimates computed from token counts and public pricing. ![co](https://img.shields.io/badge/co-555?style=flat-square)
- [gh-aw](https://github.com/github/gh-aw) - GitHub Agentic Workflows runtime with per-run token and cost metering and budget caps that stop a workflow mid-run. ![tool: MIT](https://img.shields.io/badge/tool-MIT-blue?style=flat-square) ![last commit](https://img.shields.io/github/last-commit/github/gh-aw?style=flat-square&label=)
- [Grafana Cloud GenAI Observability](https://grafana.com/docs/grafana-cloud/monitor-applications/ai-observability/genai/observability/) - Prebuilt Grafana Cloud dashboard for LLM cost, token usage, and latency, built on the OpenLIT SDK. ![co](https://img.shields.io/badge/co-555?style=flat-square)
- [Lookout for VS Code](https://github.com/nimrod-teich/lookout) - VS Code extension whose session board shows each Claude Code and Codex session's tokens with their API list-rate price, and the 5-hour and weekly usage limits that both agents report. ![tool: MIT](https://img.shields.io/badge/tool-MIT-blue?style=flat-square) ![last commit](https://img.shields.io/github/last-commit/nimrod-teich/lookout?style=flat-square&label=)
- [OpenLIT](https://github.com/openlit/openlit) - OpenTelemetry-native platform with a self-hosted dashboard for LLM cost, token, and latency observability. ![tool: Apache-2.0](https://img.shields.io/badge/tool-Apache--2.0-blue?style=flat-square) ![last commit](https://img.shields.io/github/last-commit/openlit/openlit?style=flat-square&label=)
- [OpenUsage](https://github.com/robinebers/openusage) - Native Swift macOS menu-bar meter for AI coding subscriptions, showing session and weekly limits, credits, and estimated spend. ![tool: MIT](https://img.shields.io/badge/tool-MIT-blue?style=flat-square) ![last commit](https://img.shields.io/github/last-commit/robinebers/openusage?style=flat-square&label=)
- [Opik Cost Intelligence](https://github.com/comet-ml/opik/blob/main/apps/opik-documentation/documentation/fern/docs-v2/cost_intelligence/overview.mdx) - Comet enterprise feature that runs a local proxy on each developer machine and splits every coding-agent call into about 20 cost buckets from the provider's usage payload; Comet's 15% to 30% savings figure has no published method. ![tool: proprietary](https://img.shields.io/badge/tool-proprietary-blue?style=flat-square) ![last commit](https://img.shields.io/github/last-commit/comet-ml/opik?style=flat-square&label=)
- [TokenTracker](https://github.com/xiufengsun/TokenTracker) - Local-first token and cost dashboard for coding tools, with a desktop pet, native widgets, and achievements. ![tool: MIT](https://img.shields.io/badge/tool-MIT-blue?style=flat-square) ![last commit](https://img.shields.io/github/last-commit/xiufengsun/TokenTracker?style=flat-square&label=)

## eBPF Kernel Capture

### Tools
- [AgentSight](https://github.com/eunomia-bpf/agentsight) - Uses eBPF to watch an AI agent from the kernel boundary and correlate what it said it would do with what it did. ![tool: MIT](https://img.shields.io/badge/tool-MIT-blue?style=flat-square) ![last commit](https://img.shields.io/github/last-commit/eunomia-bpf/agentsight?style=flat-square&label=)
- [OpenTelemetry eBPF Instrumentation](https://opentelemetry.io/docs/zero-code/obi/) - Zero-code eBPF instrumentation from OpenTelemetry that captures GenAI and MCP traces at the kernel layer without an SDK. ![tool: Apache-2.0](https://img.shields.io/badge/tool-Apache--2.0-blue?style=flat-square)

## Observability

### Tools
- [Braintrust](https://www.braintrust.dev) - Closed-source eval and observability SaaS whose span metrics normalize cached prompt tokens across providers and expose per-user and per-model spend. ![co](https://img.shields.io/badge/co-555?style=flat-square)
- [Langfuse](https://langfuse.com) - Open-source platform for tracing, evaluating, and analyzing LLM and agent transcripts, with a prompt-management layer. ![tool: MIT](https://img.shields.io/badge/tool-MIT-blue?style=flat-square)

## Observability Platforms

### Tools
- [OpenAI Prompt Cache Diagnostics](https://developers.openai.com/api/docs/guides/prompt-caching/diagnostics) - OpenAI guide to a Responses API feature that returns a machine-readable reason why a prompt prefix was not reused from the cache. ![tool: proprietary](https://img.shields.io/badge/tool-proprietary-blue?style=flat-square)

## OTel for LLMs

### Tools
- [OpenLLMetry](https://github.com/traceloop/openllmetry) - Open-source set of OpenTelemetry-based SDKs and instrumentations for LLM apps, built by Traceloop. ![tool: Apache-2.0](https://img.shields.io/badge/tool-Apache--2.0-blue?style=flat-square) ![last commit](https://img.shields.io/github/last-commit/traceloop/openllmetry?style=flat-square&label=)

### Reading
- [OpenTelemetry GenAI Semantic Conventions](https://github.com/open-telemetry/semantic-conventions-genai) - OpenTelemetry conventions that define vendor-neutral token, cost, and cache attribute names for GenAI telemetry.

## Tracing

### Tools
- [Arize Phoenix](https://github.com/Arize-ai/phoenix) - Source-available (Elastic License 2.0) LLM tracing platform that records per-span token counts and USD cost via OpenTelemetry. ![tool: Elastic-2.0](https://img.shields.io/badge/tool-Elastic--2.0-blue?style=flat-square) ![last commit](https://img.shields.io/github/last-commit/Arize-ai/phoenix?style=flat-square&label=)
- [claude-tap](https://github.com/liaohch3/claude-tap) - Local trace viewer that intercepts API traffic from coding agents and shows per-request token breakdowns: input, output, cache read, cache creation. ![tool: MIT](https://img.shields.io/badge/tool-MIT-blue?style=flat-square) ![last commit](https://img.shields.io/github/last-commit/liaohch3/claude-tap?style=flat-square&label=)
- [LangSmith Cost Tracking](https://docs.langchain.com/langsmith/cost-tracking) - LangChain documentation on cost tracking in LangSmith, its commercial LLM and agent observability service. ![co](https://img.shields.io/badge/co-555?style=flat-square)
- [Opik](https://github.com/comet-ml/opik) - Open-source (Apache-2.0) LLM observability platform from Comet, with per-span USD cost estimated from token usage. ![tool: Apache-2.0](https://img.shields.io/badge/tool-Apache--2.0-blue?style=flat-square) ![last commit](https://img.shields.io/github/last-commit/comet-ml/opik?style=flat-square&label=)
