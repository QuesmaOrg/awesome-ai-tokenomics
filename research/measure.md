# Measure

## Benchmarks Evals

### Tools
- [promptfoo](https://github.com/promptfoo/promptfoo) - An open-source CLI/CI harness for testing LLM prompts and agents that records per-eval token usage and cost as an assertable metric. ![tool: MIT](https://img.shields.io/badge/tool-MIT-blue?style=flat-square) ![last commit](https://img.shields.io/github/last-commit/promptfoo/promptfoo?style=flat-square&label=)

### Research & Benchmarks
- [Claw-SWE-Bench](https://github.com/opensquilla/claw-swe-bench) - Found that adapter/harness design alone swings an agent's Pass@1 score by about 54 percentage points on the identical model backbone. ![bench](https://img.shields.io/badge/bench-555?style=flat-square) ![last commit](https://img.shields.io/github/last-commit/opensquilla/claw-swe-bench?style=flat-square&label=)
- [Coding Benchmarks Are Misaligned with Agentic SE (Tessl)](https://arxiv.org/abs/2606.17799) - A position paper from Tessl (London, UK) argues that today's coding benchmarks don't measure what people think they measure. ![paper](https://img.shields.io/badge/paper-555?style=flat-square)
- [Deterministic Anchoring - how much static structure do code agents need?](https://arxiv.org/abs/2606.26979) - This ISSTA 2026 paper found injecting static-analysis facts as plain-text comments raises a code agent's Pass@1 by 3.4pp and cuts trajectories by 1.6 rounds. ![paper](https://img.shields.io/badge/paper-555?style=flat-square)
- [GitHub Copilot agentic-harness efficiency evaluation (first-party offline ablation)](https://github.blog/ai-and-ml/github-copilot/evaluating-performance-and-efficiency-of-the-github-copilot-agentic-harness-across-models-and-tasks/) - GitHub's own benchmark plots Copilot's agentic-harness resolution rate against dollar-cost-per-task across five benchmarks and four frontier models. ![report](https://img.shields.io/badge/report-555?style=flat-square)
- [Harness-Bench](https://arxiv.org/abs/2605.27922) - Holds the task, model, and budget fixed while varying only the agent harness, across 5,194 trajectories spanning 6 harnesses and 8 models. ![paper](https://img.shields.io/badge/paper-555?style=flat-square)
- [LongMemEval](https://github.com/xiaowu0162/LongMemEval) - The peer-reviewed (ICLR 2025) benchmark for long-term memory in chat assistants. ![bench](https://img.shields.io/badge/bench-555?style=flat-square) ![last commit](https://img.shields.io/github/last-commit/xiaowu0162/LongMemEval?style=flat-square&label=)
- [MemoryBench](https://github.com/supermemoryai/memorybench) - A pluggable harness to run memory systems (Supermemory, Mem0, Zep) head-to-head across datasets like LoCoMo; useful for standardizing comparison. ![bench](https://img.shields.io/badge/bench-555?style=flat-square) ![last commit](https://img.shields.io/github/last-commit/supermemoryai/memorybench?style=flat-square&label=)
- [Prompt Compression in the Wild - the end-to-end referee for compression](https://arxiv.org/abs/2604.02985) - This ECIR 2026 study found LLMLingua's compression yields up to 18% speed-up only in a narrow window; outside it, the compression step cancels the gains. ![paper](https://img.shields.io/badge/paper-555?style=flat-square)
- [RedundancyBench - can anyone even *detect* a redundant step?](https://arxiv.org/abs/2605.29893) - RedundancyBench is a benchmark for step-level redundancy detection in agent trajectories - can a model even spot the wasted step in an agent's history? ![paper](https://img.shields.io/badge/paper-555?style=flat-square)
- [RouterArena](https://github.com/RouteWorks/RouterArena) - An open evaluation platform and live leaderboard for LLM routers - systems that auto-select a model per query. ![bench](https://img.shields.io/badge/bench-555?style=flat-square) ![last commit](https://img.shields.io/github/last-commit/RouteWorks/RouterArena?style=flat-square&label=)
- [SWE-bench](https://github.com/SWE-bench/SWE-bench) - The canonical accuracy-only software-engineering benchmark (2,294 real GitHub issue tasks, 12 Python repos, ICLR 2024). The cost-aware derivatives in this list build on it. ![bench](https://img.shields.io/badge/bench-555?style=flat-square) ![last commit](https://img.shields.io/github/last-commit/SWE-bench/SWE-bench?style=flat-square&label=)
- [SWE-Effi - cost-aware re-ranking of SWE-agents under resource budgets](https://arxiv.org/abs/2509.09853) - SWE-Effi re-ranks popular AI issue-resolution systems on a SWE-bench subset by cost-under-resource-constraints instead of by accuracy alone. ![paper](https://img.shields.io/badge/paper-555?style=flat-square)
- [Terminal-Bench](https://www.tbench.ai/) - The canonical benchmark for AI agents in real terminal/CLI environments, with 89 tasks each vetted through ~3 reviewer-hours. ![bench](https://img.shields.io/badge/bench-555?style=flat-square)

## Cache Accounting

### Reading
- [Gemini context caching - the per-hour storage meter (the third-vendor axis)](https://ai.google.dev/gemini-api/docs/pricing) - Among major providers, only Gemini bills a per-hour storage meter for explicit prompt caching.
- [OpenAI prompt-caching `cached_tokens` accounting](https://platform.openai.com/docs/guides/prompt-caching) - This is the measurement substrate for prompt-cache savings on the OpenAI API.
- [OpenAI Responses conversation state - you pay for the whole chain every turn (and the compaction levers)](https://developers.openai.com/api/docs/guides/conversation-state) - This entry covers the billing semantics of stateful conversations on OpenAI's Responses API, plus the two server-side compaction levers that mitigate them.
- [The cache share of an agentic bill, simulated on Open-SWE-Traces](https://www.completeskeptic.com/p/kv-cache-rules-everything-around) - A replay simulation over NVIDIA's Open-SWE-Traces that puts output tokens at 9-18% of an agentic bill and cache traffic at the remaining 82-91%, arriving at the cache-dominance figure from a wholly different direction than the billed-run studies.

## Cost Anatomy

### Reading
- [Anthropic bill anatomy - the whole-bill line-item taxonomy](https://platform.claude.com/docs/en/about-claude/pricing#code-execution-tool) - This is the canonical enumeration of every meter on a Claude API bill, read live from Anthropic's pricing page.
- [TensorZero - cross-vendor token-count divergence ("stop comparing $/M tokens")](https://www.tensorzero.com/blog/stop-comparing-price-per-million-tokens-the-hidden-llm-api-costs/) - The same input can produce 2.65x more tokens on one tokenizer than another's: Claude Opus 4-7 runs 1.57x-2.65x more tokens than GPT-5.4 on the same content.
- [Vision-token pricing formulas across the big three](https://platform.claude.com/docs/en/build-with-claude/vision) - Anthropic, OpenAI, and Google each convert an image into billed tokens with a different formula, so no single cross-vendor image-cost number exists. (also: [OpenAI](https://developers.openai.com/api/docs/guides/images-vision) · [Google](https://ai.google.dev/gemini-api/docs/image-understanding))

## Energy Carbon

### Tools
- [Alumet](https://github.com/alumet-dev/alumet) - A Rust measurement framework (EUPL-1.2 or later) that reads hardware energy counters through RAPL, NVML, AMD SMI and Jetson INA plugins, and attributes the energy to processes, cgroups and Kubernetes pods. ![tool: EUPL-1.2-or-later](https://img.shields.io/badge/tool-EUPL--1.2--or--later-blue?style=flat-square) ![last commit](https://img.shields.io/github/last-commit/alumet-dev/alumet?style=flat-square&label=)
- [claude-carbon](https://github.com/gwittebolle/claude-carbon) - An MIT-licensed Claude Code plugin (Bash and SQLite) that estimates each session's CO2 locally from its token counts, shows it in the status line next to the cost, and keeps the history past the 30-day transcript purge; every factor is sourced in a public methodology. ![tool: MIT](https://img.shields.io/badge/tool-MIT-blue?style=flat-square) ![last commit](https://img.shields.io/github/last-commit/gwittebolle/claude-carbon?style=flat-square&label=)
- [CodeCarbon](https://github.com/mlco2/codecarbon) - An open-source (MIT) library for estimating a workload's energy use and CO2e emissions, and ML's widely-cited carbon baseline. ![tool: MIT](https://img.shields.io/badge/tool-MIT-blue?style=flat-square) ![last commit](https://img.shields.io/github/last-commit/mlco2/codecarbon?style=flat-square&label=)
- [EcoLogits](https://github.com/mlco2/ecologits) - Estimates the energy and carbon footprint of calling generative-AI APIs: the hosted counterpart to CodeCarbon, which measures your own hardware. ![tool: MPL-2.0](https://img.shields.io/badge/tool-MPL--2.0-blue?style=flat-square) ![last commit](https://img.shields.io/github/last-commit/mlco2/ecologits?style=flat-square&label=)

### Research & Benchmarks
- [Google - measuring the environmental impact of AI inference (provider disclosure)](https://cloud.google.com/blog/products/infrastructure/measuring-the-environmental-impact-of-ai-inference) - Google published a first-party disclosure of the energy, carbon, and water cost of a median Gemini Apps text prompt, authored by Amin Vahdat and Jeff Dean. ![report](https://img.shields.io/badge/report-555?style=flat-square)
- [ML.ENERGY Leaderboard](https://ml.energy/blog/measurement/energy/diagnosing-inference-energy-consumption-with-the-mlenergy-leaderboard-v30/) - Version 3.0 of this leaderboard measures real GPU inference energy across 46 models x 7 tasks, finding reasoning models use roughly 25x the energy of others. ![bench](https://img.shields.io/badge/bench-555?style=flat-square)

### Reading
- [Epoch AI - how much energy a query uses (the per-token energy anchor)](https://epoch.ai/gradient-updates/how-much-energy-does-chatgpt-use) - Epoch AI built a transparent, first-principles estimate of how much energy one LLM query costs.

## Harness Overhead

### Research & Benchmarks
- [Claude Code system prompts (Piebald extraction)](https://github.com/Piebald-AI/claude-code-system-prompts) - Piebald AI extracts Claude Code's full compiled prompt payload per release: 515 prompt strings and 27 tool descriptions at v2.1.212, each priced in tokens. ![data](https://img.shields.io/badge/data-555?style=flat-square) ![last commit](https://img.shields.io/github/last-commit/Piebald-AI/claude-code-system-prompts?style=flat-square&label=)
- [Claude Code vs OpenCode token overhead (Systima study)](https://systima.ai/blog/claude-code-vs-opencode-token-overhead) - Systima measured harness scaffolding overhead before a prompt is even read: Claude Code carries about 32,800 tokens versus OpenCode's 6,900, a 4.7x gap. ![report](https://img.shields.io/badge/report-555?style=flat-square)
- [FrontierHarness Eval](https://runta.com/blog/introducing-frontierharness-eval/) - Nine coding harnesses in twelve configurations on one model through one gateway: pass rates cluster between 50% and 67% while cost per completed task spans $1.05 to $18.34, with task definitions and results published. ![bench](https://img.shields.io/badge/bench-555?style=flat-square)
- [Multi-vendor system-prompt and tool-schema corpus (x1xhlol)](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools) - A 35-vendor collection of extracted agent system prompts with separate tool-schema JSON files (Claude Code's Tools.json alone is 48,962 bytes), published as raw text with no token counts. ![data](https://img.shields.io/badge/data-555?style=flat-square) ![last commit](https://img.shields.io/github/last-commit/x1xhlol/system-prompts-and-models-of-ai-tools?style=flat-square&label=)
- [Multi-vendor system-prompt corpus (asgeirtj)](https://github.com/asgeirtj/system_prompts_leaks) - A 481-file prompt corpus under CC0 covering harnesses others miss (Antigravity CLI at 24,493 bytes and Copilot CLI at 72,738), with dated Anthropic prompt series but no token counts. ![data](https://img.shields.io/badge/data-555?style=flat-square) ![last commit](https://img.shields.io/github/last-commit/asgeirtj/system_prompts_leaks?style=flat-square&label=)
- [The Harness Tax (twelve-harness fixed-model token benchmark)](https://www.eishanlawrence.com/blog/harness-bench/harness-efficiency-paper.pdf) - Holds the model, tasks and gateway fixed across twelve coding-harness configurations and finds tokens per solved task spanning 46x on one model and 83x on a second, with startup tax times turn count predicting the spread at R-squared 0.99. (also: [author writeup](https://www.eishanlawrence.com/blog/harness-efficiency-bench) · [Composio, independent second primary](https://composio.dev/content/best-agent-harness-deepseek-v4-flash) · [The New Stack coverage](https://thenewstack.io/agent-harness-token-costs/)) ![paper](https://img.shields.io/badge/paper-555?style=flat-square)

## Metering

### Tools
- [Cross-vendor coding-agent usage trackers (AgentsView · caut)](https://github.com/kenn-io/agentsview) - AgentsView and caut are open-source tools that read local session logs to aggregate token usage and cost across roughly 20 coding-agent vendors. ![tool: MIT](https://img.shields.io/badge/tool-MIT-blue?style=flat-square) ![last commit](https://img.shields.io/github/last-commit/kenn-io/agentsview?style=flat-square&label=)
- [OpenCost - AI inference cost tracking](https://github.com/opencost/opencost/blob/develop/docs/inference-cost-tracking.md) - The CNCF Kubernetes cost tool's 2026-07 feature turns GPU and shared-infrastructure spend on vLLM/llm-d deployments into cost per million tokens, reconciled to the infrastructure bill. ![tool: Apache-2.0](https://img.shields.io/badge/tool-Apache--2.0-blue?style=flat-square) ![last commit](https://img.shields.io/github/last-commit/opencost/opencost?style=flat-square&label=)
- [tokview](https://github.com/headroomlabs-ai/tokview) - A local, zero-config proxy showing a coding agent's token spend by session, model, and tool call, flagging re-sent results that multiply the bill. ![tool: MIT](https://img.shields.io/badge/tool-MIT-blue?style=flat-square) ![last commit](https://img.shields.io/github/last-commit/headroomlabs-ai/tokview?style=flat-square&label=)

### Research & Benchmarks
- [How Do AI Agents Spend Your Money?](https://arxiv.org/abs/2604.22750) - This Stanford study is the first systematic look at token spend in agentic coding, running 8 frontier models on 500 SWE-bench Verified tasks. ![paper](https://img.shields.io/badge/paper-555?style=flat-square)

## Transcript Analysis

### Tools
- [Faros AI - "Token Intelligence" / Token Attribution Ledger](https://www.faros.ai/blog/token-intelligence-for-ai-engineering) - Faros AI is an enterprise engineering-intelligence SaaS (DORA/SPACE-style productivity analytics). ![co](https://img.shields.io/badge/co-555?style=flat-square)
- [token-optimizer (alexgreensh)](https://github.com/alexgreensh/token-optimizer) - token-optimizer is a coding-agent plugin that runs eleven heuristic waste detectors per session and prices the flagged tokens in dollars. Coverage is semi-cross-vendor. ![tool: PolyForm-Noncommercial-1.0.0](https://img.shields.io/badge/tool-PolyForm--Noncommercial--1.0.0-blue?style=flat-square) ![last commit](https://img.shields.io/github/last-commit/alexgreensh/token-optimizer?style=flat-square&label=)

### Research & Benchmarks
- [Early Diagnosis of Wasted Computation in Multi-Agent LLM Systems (Failure-Aware Observability)](https://arxiv.org/abs/2606.01365) - This live waste-detection framework for multi-agent systems found that 58.1% of tokens in failed runs are spent after its first warning fires. ![paper](https://img.shields.io/badge/paper-555?style=flat-square)

## Whole Bill Accounting

### Tools
- [FOCUS 1.4 - the cross-vendor billing-data normalization standard (now with invoice reconciliation)](https://focus.finops.org/focus-specification/) - FOCUS 1.4, the Linux Foundation's billing-data schema, added Invoice Detail and Billing Period datasets to reconcile spend against real invoices. ![tool](https://img.shields.io/badge/tool-blue?style=flat-square)

### Reading
- [FOCUS 1.5 - what the AI-cost release includes, and what it rules out](https://www.tokeneconomics.com/projects/what-1-5-does-for-ai-cost-and-what-it-does-not/) - The FOCUS working group's own scope statement for release 1.5: model identity merged into SkuPriceDetails with no new columns, cache and token-type work still unmerged, and session, event and harness identifiers ruled out of scope on the record.
