# Measure

## Benchmarks Evals

### Tools
- [promptfoo](https://github.com/promptfoo/promptfoo) - Open-source CLI and CI harness for testing LLM prompts and agents that records per-eval token usage and cost. ![tool: MIT](https://img.shields.io/badge/tool-MIT-blue?style=flat-square) ![last commit](https://img.shields.io/github/last-commit/promptfoo/promptfoo?style=flat-square&label=)

### Research & Benchmarks
- [Claw-SWE-Bench](https://github.com/TokenRhythm/claw-swe-bench) - Benchmark showing how adapter and harness design change an agent's score on the same model backbone. ![bench](https://img.shields.io/badge/bench-555?style=flat-square) ![last commit](https://img.shields.io/github/last-commit/TokenRhythm/claw-swe-bench?style=flat-square&label=)
- [Coding Benchmarks Are Misaligned with Agentic SE](https://arxiv.org/abs/2606.17799) - Position paper from Tessl arguing that current coding benchmarks do not measure what people assume. ![paper](https://img.shields.io/badge/paper-555?style=flat-square)
- [Deterministic Anchoring](https://arxiv.org/abs/2606.26979) - ISSTA 2026 paper on injecting static-analysis facts as plain-text comments for code agents. ![paper](https://img.shields.io/badge/paper-555?style=flat-square)
- [GitHub Copilot Agentic Harness Evaluation](https://github.blog/ai-and-ml/github-copilot/evaluating-performance-and-efficiency-of-the-github-copilot-agentic-harness-across-models-and-tasks/) - GitHub blog post comparing Copilot's agentic-harness resolution rate with cost per task across benchmarks and models. ![report](https://img.shields.io/badge/report-555?style=flat-square)
- [Harness-Bench](https://arxiv.org/abs/2605.27922) - Benchmark that holds task, model, and budget fixed while varying only the agent harness. ![paper](https://img.shields.io/badge/paper-555?style=flat-square)
- [livenerf](https://github.com/ninjahawk/livenerf) - Pre-registered, append-only daily benchmark that tests whether a Claude model gets worse after launch, with a locked 78-question panel, a control model, and a stated detection limit of about 7.5 accuracy points per 10-day window. ![bench](https://img.shields.io/badge/bench-555?style=flat-square) ![last commit](https://img.shields.io/github/last-commit/ninjahawk/livenerf?style=flat-square&label=)
- [LongMemEval](https://github.com/xiaowu0162/LongMemEval) - Benchmark for long-term memory in chat assistants, published at ICLR 2025. ![bench](https://img.shields.io/badge/bench-555?style=flat-square) ![last commit](https://img.shields.io/github/last-commit/xiaowu0162/LongMemEval?style=flat-square&label=)
- [MemoryBench](https://github.com/supermemoryai/memorybench) - Pluggable harness that runs memory systems head-to-head across datasets like LoCoMo. ![bench](https://img.shields.io/badge/bench-555?style=flat-square) ![last commit](https://img.shields.io/github/last-commit/supermemoryai/memorybench?style=flat-square&label=)
- [Prompt Compression in the Wild](https://arxiv.org/abs/2604.02985) - ECIR 2026 study of end-to-end speed-ups from LLMLingua prompt compression. ![paper](https://img.shields.io/badge/paper-555?style=flat-square)
- [RedundancyBench](https://arxiv.org/abs/2605.29893) - Benchmark for step-level redundancy detection in agent trajectories. ![paper](https://img.shields.io/badge/paper-555?style=flat-square)
- [RouterArena](https://github.com/RouteWorks/RouterArena) - Open evaluation platform and leaderboard for LLM routers that select a model per query. ![bench](https://img.shields.io/badge/bench-555?style=flat-square) ![last commit](https://img.shields.io/github/last-commit/RouteWorks/RouterArena?style=flat-square&label=)
- [SWE-bench](https://github.com/SWE-bench/SWE-bench) - Software-engineering benchmark of real GitHub issue tasks from Python repositories, published at ICLR 2024. ![bench](https://img.shields.io/badge/bench-555?style=flat-square) ![last commit](https://img.shields.io/github/last-commit/SWE-bench/SWE-bench?style=flat-square&label=)
- [SWE-Effi](https://arxiv.org/abs/2509.09853) - Paper that re-ranks SWE-agents on a SWE-bench subset by cost under resource constraints. ![paper](https://img.shields.io/badge/paper-555?style=flat-square)
- [Terminal-Bench](https://www.tbench.ai/) - Benchmark for AI agents in real terminal and CLI environments, with a public leaderboard. ![bench](https://img.shields.io/badge/bench-555?style=flat-square)

## Cache Accounting

### Reading
- [Gemini Context Caching Pricing](https://ai.google.dev/gemini-api/docs/pricing) - Google's Gemini API pricing page, including the per-hour storage charge for explicit context caching.
- [Open-SWE-Traces Cache Simulation](https://www.completeskeptic.com/p/kv-cache-rules-everything-around) - Replay simulation over NVIDIA's Open-SWE-Traces that splits an agentic bill into output tokens and cache traffic.
- [OpenAI Conversation State](https://developers.openai.com/api/docs/guides/conversation-state) - OpenAI guide to conversation state in the Responses API, including billing semantics and server-side compaction.
- [OpenAI Prompt Caching](https://platform.openai.com/docs/guides/prompt-caching) - OpenAI guide to prompt caching and the cached_tokens usage field.

## Cost Anatomy

### Research & Benchmarks
- [Cursor Token Mix](https://cursor.com/insights/developer-habits#cache-reads-dominate-token-activity) - Cursor telemetry puts cache reads at 89.9% of all tokens and output at 0.6% (May 2026), and a September read finds the top 10% of users consume nearly two-thirds of tokens. ![report](https://img.shields.io/badge/report-555?style=flat-square)

### Reading
- [Anthropic Pricing Line Items](https://platform.claude.com/docs/en/about-claude/pricing#code-execution-tool) - Anthropic pricing documentation that enumerates the meters on a Claude API bill.
- [Claude Vision Token Pricing](https://platform.claude.com/docs/en/build-with-claude/vision) - Anthropic vision documentation on how images convert to billed tokens, with OpenAI and Google equivalents.
- [TensorZero Token-Count Divergence](https://www.tensorzero.com/blog/stop-comparing-price-per-million-tokens-the-hidden-llm-api-costs/) - TensorZero blog post on how the same input produces different token counts across vendor tokenizers.

## Datasets

### Research & Benchmarks
- [FreeInference Agentic Trace](https://huggingface.co/datasets/harvardMadsys/freeinference_agentic_trace) - CC-BY-4.0 request-level trace of 12,002 real agent sessions from 14 harnesses over 16 weeks, with per-request token counts, cache-read tokens, and prefix hashes for cache replay, and no message text. ![data](https://img.shields.io/badge/data-555?style=flat-square)

## Energy Carbon

### Tools
- [Alumet](https://github.com/alumet-dev/alumet) - Rust measurement framework (EUPL-1.2 or later) that reads hardware energy counters and attributes energy to processes, cgroups, and Kubernetes pods. ![tool: EUPL-1.2-or-later](https://img.shields.io/badge/tool-EUPL--1.2--or--later-blue?style=flat-square) ![last commit](https://img.shields.io/github/last-commit/alumet-dev/alumet?style=flat-square&label=)
- [claude-carbon](https://github.com/gwittebolle/claude-carbon) - MIT-licensed Claude Code plugin that estimates each session's CO2 locally from token counts and shows it in the status line. ![tool: MIT](https://img.shields.io/badge/tool-MIT-blue?style=flat-square) ![last commit](https://img.shields.io/github/last-commit/gwittebolle/claude-carbon?style=flat-square&label=)
- [CodeCarbon](https://github.com/mlco2/codecarbon) - Open-source (MIT) library for estimating a workload's energy use and CO2e emissions. ![tool: MIT](https://img.shields.io/badge/tool-MIT-blue?style=flat-square) ![last commit](https://img.shields.io/github/last-commit/mlco2/codecarbon?style=flat-square&label=)
- [EcoLogits](https://github.com/mlco2/ecologits) - Library that estimates the energy and carbon footprint of calling generative-AI APIs, as a hosted counterpart to CodeCarbon. ![tool: MPL-2.0](https://img.shields.io/badge/tool-MPL--2.0-blue?style=flat-square) ![last commit](https://img.shields.io/github/last-commit/mlco2/ecologits?style=flat-square&label=)

### Research & Benchmarks
- [Google AI Inference Environmental Impact](https://cloud.google.com/blog/products/infrastructure/measuring-the-environmental-impact-of-ai-inference) - Google disclosure of the energy, carbon, and water footprint of a median Gemini Apps text prompt. ![report](https://img.shields.io/badge/report-555?style=flat-square)
- [ML.ENERGY Leaderboard](https://ml.energy/blog/measurement/energy/diagnosing-inference-energy-consumption-with-the-mlenergy-leaderboard-v30/) - Leaderboard that measures real GPU inference energy across models and tasks. ![bench](https://img.shields.io/badge/bench-555?style=flat-square)

### Reading
- [Epoch AI Energy per Query](https://epoch.ai/gradient-updates/how-much-energy-does-chatgpt-use) - Epoch AI analysis estimating from first principles how much energy one LLM query uses.

## Harness Overhead

### Research & Benchmarks
- [Claude Code System Prompts](https://github.com/Piebald-AI/claude-code-system-prompts) - Piebald AI extraction of Claude Code's compiled prompt strings and tool descriptions for each release. ![data](https://img.shields.io/badge/data-555?style=flat-square) ![last commit](https://img.shields.io/github/last-commit/Piebald-AI/claude-code-system-prompts?style=flat-square&label=)
- [Claude Code vs OpenCode Token Overhead](https://systima.ai/blog/claude-code-vs-opencode-token-overhead) - Systima study of harness scaffolding token overhead in Claude Code and OpenCode. ![report](https://img.shields.io/badge/report-555?style=flat-square)
- [FrontierHarness Eval](https://runta.com/blog/introducing-frontierharness-eval/) - Runta benchmark of coding harnesses on one model through one gateway, comparing pass rates and cost per completed task. ![bench](https://img.shields.io/badge/bench-555?style=flat-square)
- [HarnessTax](https://arena.ai/blog/coding-agents-harness-tax) - Arena and Berkeley study of seven models across Claude Code, Codex CLI, and Pi on 30 SWE-bench Lite and 30 Terminal-Bench 2.0 tasks: success rates moved within a few points while cost per rollout varied up to 5.07x for the same model (3.49x in native model-harness pairs). ![report](https://img.shields.io/badge/report-555?style=flat-square)
- [System Prompts and Models of AI Tools](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools) - Collection of extracted agent system prompts and tool-schema JSON files across many vendors, published as raw text. ![data](https://img.shields.io/badge/data-555?style=flat-square) ![last commit](https://img.shields.io/github/last-commit/x1xhlol/system-prompts-and-models-of-ai-tools?style=flat-square&label=)
- [System Prompts Leaks](https://github.com/asgeirtj/system_prompts_leaks) - CC0 corpus of extracted system prompts for AI harnesses and models, with dated Anthropic prompt series. ![data](https://img.shields.io/badge/data-555?style=flat-square) ![last commit](https://img.shields.io/github/last-commit/asgeirtj/system_prompts_leaks?style=flat-square&label=)
- [The Harness Tax](https://www.eishanlawrence.com/blog/harness-bench/harness-efficiency-paper.pdf) - Paper that holds model, tasks, and gateway fixed across coding-harness configurations and compares tokens per solved task. ![paper](https://img.shields.io/badge/paper-555?style=flat-square)

### Reading
- [TestDino Harness Overhead Benchmark](https://testdino.com/blog/harness-overhead-benchmark) - TestDino sent the same one-word prompt through 11 coding agents in one clean repo on 2026-10-08 and recorded first-call input tokens: 1,894 (Pi) to 31,480 (Claude Code), a 16.8x spread against a 31,798 Kiro CLI estimate, median of 3 runs.

## Metering

### Tools
- [AgentsView and caut](https://github.com/kenn-io/agentsview) - Open-source tools that read local session logs to aggregate token usage and cost across coding-agent vendors. ![tool: MIT](https://img.shields.io/badge/tool-MIT-blue?style=flat-square) ![last commit](https://img.shields.io/github/last-commit/kenn-io/agentsview?style=flat-square&label=)
- [OpenCost Inference Cost Tracking](https://github.com/opencost/opencost/blob/develop/docs/inference-cost-tracking.md) - OpenCost documentation on turning GPU and shared-infrastructure spend on vLLM and llm-d deployments into cost per million tokens. ![tool: Apache-2.0](https://img.shields.io/badge/tool-Apache--2.0-blue?style=flat-square) ![last commit](https://img.shields.io/github/last-commit/opencost/opencost?style=flat-square&label=)
- [tokview](https://github.com/chopratejas/tokview) - Local, zero-config proxy that shows a coding agent's token spend by session, model, and tool call. ![tool: MIT](https://img.shields.io/badge/tool-MIT-blue?style=flat-square) ![last commit](https://img.shields.io/github/last-commit/chopratejas/tokview?style=flat-square&label=)

### Research & Benchmarks
- [How Do AI Agents Spend Your Money?](https://arxiv.org/abs/2604.22750) - Stanford study of token spend in agentic coding across frontier models on SWE-bench Verified tasks. ![paper](https://img.shields.io/badge/paper-555?style=flat-square)

## Transcript Analysis

### Tools
- [Faros AI Token Intelligence](https://www.faros.ai/blog/token-intelligence-for-ai-engineering) - Faros AI blog post on token intelligence and its Token Attribution Ledger, from an engineering-intelligence SaaS. ![co](https://img.shields.io/badge/co-555?style=flat-square)
- [token-optimizer (alexgreensh)](https://github.com/alexgreensh/token-optimizer) - Coding-agent plugin that runs heuristic waste detectors per session and prices the flagged tokens in dollars. ![tool: PolyForm-Noncommercial-1.0.0](https://img.shields.io/badge/tool-PolyForm--Noncommercial--1.0.0-blue?style=flat-square) ![last commit](https://img.shields.io/github/last-commit/alexgreensh/token-optimizer?style=flat-square&label=)

### Research & Benchmarks
- [Failure-Aware Observability for Multi-Agent LLM Systems](https://arxiv.org/abs/2606.01365) - Paper on a live waste-detection framework for multi-agent systems that finds wasted computation early. ![paper](https://img.shields.io/badge/paper-555?style=flat-square)

## Whole Bill Accounting

### Tools
- [FOCUS Specification](https://focus.finops.org/focus-specification/) - Linux Foundation billing-data schema specification, with invoice detail and billing period datasets for reconciling spend against invoices. ![tool](https://img.shields.io/badge/tool-blue?style=flat-square)

### Reading
- [FOCUS 1.5 and AI Cost](https://www.tokeneconomics.com/projects/what-1-5-does-for-ai-cost-and-what-it-does-not/) - Tokenomics Foundation post on the scope of FOCUS release 1.5 for AI cost, including what it leaves out.
