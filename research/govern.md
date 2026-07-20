# Govern

## Allocation Chargeback

### Tools
- [CloudZero](https://www.cloudzero.com/blog/ai-cost-optimization-at-scale/) - An established commercial cloud and AI cost-intelligence / FinOps platform that brands itself 'The AI ROI Company'. ![co](https://img.shields.io/badge/co-555?style=flat-square)
- [Mavvrik (fmr. DigitalEx)](https://www.mavvrik.ai/press-releases/mavvrik-unveils-full-stack-ai-cost-governance/) - Mavvrik is an AI/hybrid-infrastructure cost governance and FinOps platform, rebranded from DigitalEx in February 2025. ![co](https://img.shields.io/badge/co-555?style=flat-square)
- [Pay-i](https://docs.pay-i.com/) - An SDK-based GenAI cost-observability platform that tracks token-level spend per call and rolls it up into cost-center allocation across orgs and apps. ![co](https://img.shields.io/badge/co-555?style=flat-square)

## Anomaly Detection

### Research & Benchmarks
- [Denial-of-Wallet / token-exhaustion attacks](https://arxiv.org/abs/2601.10955) - Denial-of-wallet attacks exploit pay-per-token pricing to inflate a bill, via stolen-credential LLMjacking or agents steered into runaway token use. ![paper](https://img.shields.io/badge/paper-555?style=flat-square)
- [Governance Decay - compaction silently erasing safety/governance constraints](https://arxiv.org/abs/2606.22528) - Compacting an agent's context can silently erase governance rules: across 7 model families, violations rose from 0% to 30%, up to 59% for some. ![paper](https://img.shields.io/badge/paper-555?style=flat-square)

## Billing Audit Finops

### Tools
- [FinOps for AI - canonical practitioner framework for governing AI/LLM spend](https://www.finops.org/framework/scope/finops-for-ai/) - FinOps for AI is the FinOps Foundation's official practitioner framework for governing AI, GPU, and token spend. ![tool](https://img.shields.io/badge/tool-blue?style=flat-square)
- [Vaudit - TokenAudit (LLM invoice reconciliation / AI spend audit)](https://www.vaudit.com/) - Vaudit is an AI-native, independent spend-auditing and recovery platform (San Francisco, founded late 2023). ![co](https://img.shields.io/badge/co-555?style=flat-square)

## Budgets Caps

### Tools
- [AEGIS](https://github.com/Justin0504/Aegis) - An open-source (MIT) pre-execution firewall and cryptographic audit layer for AI agents. ![tool: MIT](https://img.shields.io/badge/tool-MIT-blue?style=flat-square) ![stars](https://img.shields.io/github/stars/Justin0504/Aegis?style=flat-square&logo=github&label=) ![last commit](https://img.shields.io/github/last-commit/Justin0504/Aegis?style=flat-square&label=)
- [TrueFoundry (AI Gateway - Budget Limiting)](https://www.truefoundry.com/docs/ai-gateway/budgetlimiting) - TrueFoundry is an enterprise GenAI deployment/gateway company founded by ex-Meta founders. ![co](https://img.shields.io/badge/co-555?style=flat-square)

### Reading
- [Claude Code's 5-hour/weekly usage quotas - Anthropic has stopped publishing exact numbers](https://support.claude.com/en/articles/11049741-what-is-the-max-plan) - Anthropic stopped publishing exact Claude Code usage quotas, describing Max plans only as 5x/20x multipliers of Pro with no absolute numbers.

## Energy Carbon

### Tools
- [CodeCarbon](https://github.com/mlco2/codecarbon) - An open-source (MIT) library for estimating a workload's energy use and CO2e emissions, and ML's widely-cited carbon baseline. ![tool: MIT](https://img.shields.io/badge/tool-MIT-blue?style=flat-square) ![stars](https://img.shields.io/github/stars/mlco2/codecarbon?style=flat-square&logo=github&label=) ![last commit](https://img.shields.io/github/last-commit/mlco2/codecarbon?style=flat-square&label=)
- [EcoLogits - energy/carbon of LLM *API* calls (the hosted-usage estimator)](https://github.com/mlco2/ecologits) - Estimates the energy and carbon footprint of calling generative-AI APIs: the hosted counterpart to CodeCarbon, which measures your own hardware. ![tool: MPL-2.0](https://img.shields.io/badge/tool-MPL--2.0-blue?style=flat-square) ![stars](https://img.shields.io/github/stars/mlco2/ecologits?style=flat-square&logo=github&label=) ![last commit](https://img.shields.io/github/last-commit/mlco2/ecologits?style=flat-square&label=)

### Research & Benchmarks
- [Google - measuring the environmental impact of AI inference (provider disclosure)](https://cloud.google.com/blog/products/infrastructure/measuring-the-environmental-impact-of-ai-inference) - Google published a first-party disclosure of the energy, carbon, and water cost of a median Gemini Apps text prompt, authored by Amin Vahdat and Jeff Dean. ![report](https://img.shields.io/badge/report-555?style=flat-square)
- [ML.ENERGY Leaderboard v3.0 - measured inference energy (the "reasoning ≈ 25× energy" signal)](https://ml.energy/blog/measurement/energy/diagnosing-inference-energy-consumption-with-the-mlenergy-leaderboard-v30/) - Version 3.0 of this leaderboard measures real GPU inference energy across 46 models x 7 tasks, finding reasoning models use roughly 25x the energy of others. ![bench](https://img.shields.io/badge/bench-555?style=flat-square)

### Reading
- [Epoch AI - how much energy a query uses (the per-token energy anchor)](https://epoch.ai/gradient-updates/how-much-energy-does-chatgpt-use) - Epoch AI built a transparent, first-principles estimate of how much energy one LLM query costs.

## Policy Enforcement

### Tools
- [ActPlane](https://github.com/eunomia-bpf/ActPlane) - An eBPF-based, OS-level policy-enforcement engine for AI-agent harnesses like Claude Code and Codex. ![tool: MIT](https://img.shields.io/badge/tool-MIT-blue?style=flat-square) ![stars](https://img.shields.io/github/stars/eunomia-bpf/ActPlane?style=flat-square&logo=github&label=) ![last commit](https://img.shields.io/github/last-commit/eunomia-bpf/ActPlane?style=flat-square&label=)
- [MCPGuard-Dynamic](https://github.com/facebook/mcpguard-dynamic) - Meta's open-source kernel-level eBPF sandbox built specifically for MCP. ![tool: MIT](https://img.shields.io/badge/tool-MIT-blue?style=flat-square) ![stars](https://img.shields.io/github/stars/facebook/mcpguard-dynamic?style=flat-square&logo=github&label=) ![last commit](https://img.shields.io/github/last-commit/facebook/mcpguard-dynamic?style=flat-square&label=)

## Spend Management

### Tools
- [ChatGPT Enterprise - usage analytics & spend controls](https://openai.com/index/chatgpt-enterprise-spend-controls/) - OpenAI's first-party spend layer for ChatGPT Enterprise/Business: a Global Admin Console with credit caps, request workflows, and a Cost API. ![tool: proprietary](https://img.shields.io/badge/tool-proprietary-blue?style=flat-square)
- [Claude Enterprise - admin analytics & cost controls](https://www.claude.com/blog/giving-admins-more-visibility-and-control-over-claude-usage-and-spend) - Anthropic's first-party spend surface for Claude Enterprise/Team admins: org-level spend caps, model defaults, and per-user cost analytics via the Admin API. ![tool: proprietary](https://img.shields.io/badge/tool-proprietary-blue?style=flat-square)
- [PointFive (AI Efficiency OS / TokenShift)](https://www.pointfive.co/press/pointfive-launches-ai-efficiency-os-tokenshift) - PointFive's TokenShift governs coding-agent token spend across Claude Code, Cursor, Codex, and more, claiming a 10-20% cut across 11 partners. ![co](https://img.shields.io/badge/co-555?style=flat-square)
- [Revenium - runtime AI economic control / spend management](https://www.revenium.ai/) - Revenium tracks AI agent spend at runtime to the cent, attributing every model call and tool cost to its workflow, with auto-shutoff on runaway budgets. ![co](https://img.shields.io/badge/co-555?style=flat-square)
- [Vantage](https://www.vantage.sh/blog/agentic-coding-costs) - A FinOps platform ingesting native token-level cost data from Anthropic and OpenAI's own usage APIs, plus Cursor and cloud spend. ![co](https://img.shields.io/badge/co-555?style=flat-square)
- [Vercel AI Gateway - per-API-key budgets](https://vercel.com/changelog/budgets-for-api-keys-on-ai-gateway) - Vercel AI Gateway lets you cap spend per API key in dollars (min $1) with a daily/weekly/monthly refresh, rejecting further requests once the cap is hit. ![tool: proprietary](https://img.shields.io/badge/tool-proprietary-blue?style=flat-square)
