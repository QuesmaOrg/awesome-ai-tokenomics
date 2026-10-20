# Govern

## Allocation Chargeback

### Tools
- [AWS Bedrock Cost Attribution in Cost Explorer](https://docs.aws.amazon.com/cost-management/latest/userguide/ce-filtering.html) - Since 2026-10-08, AWS Cost Explorer and Budgets group and filter Amazon Bedrock cost by model, provider, inference type (input, output, prompt cache read), and feature, at no extra charge. ![tool: proprietary](https://img.shields.io/badge/tool-proprietary-blue?style=flat-square)
- [CloudZero](https://www.cloudzero.com/blog/ai-cost-optimization-at-scale/) - Commercial cloud and AI cost-intelligence and FinOps platform. ![co](https://img.shields.io/badge/co-555?style=flat-square)
- [Mavvrik](https://www.mavvrik.ai/press-releases/mavvrik-unveils-full-stack-ai-cost-governance/) - AI and hybrid-infrastructure cost governance and FinOps platform, formerly DigitalEx. ![co](https://img.shields.io/badge/co-555?style=flat-square)
- [Pay-i](https://docs.ascerta.com/) - SDK-based GenAI cost-observability platform, now Ascerta, that tracks token-level spend per call and rolls it up into cost-center allocation. ![co](https://img.shields.io/badge/co-555?style=flat-square)

### Reading
- [JetBrains AI Credits for Business](https://blog.jetbrains.com/blog/2026/07/07/jetbrains-ai-for-teams-and-organizations-from-fragmented-ai-usage-to-coordinated-software-development/) - JetBrains blog post on moving business AI plans from monthly per-seat licenses to reallocatable credits with a governance dashboard.

## Anomaly Detection

### Research & Benchmarks
- [Denial-of-Wallet Attacks](https://arxiv.org/abs/2601.10955) - Paper on attacks that exploit pay-per-token pricing to inflate a bill, through stolen credentials or agents steered into runaway token use. ![paper](https://img.shields.io/badge/paper-555?style=flat-square)
- [Governance Decay](https://arxiv.org/abs/2606.22528) - Paper showing that compacting an agent's context can silently erase governance and safety constraints. ![paper](https://img.shields.io/badge/paper-555?style=flat-square)

## Billing Audit FinOps

### Tools
- [AgentMeasure](https://github.com/roy-tong/AgentMeasure) - Open-source (MIT) measurement standard and local checker that audits vendor billing claims against a named-rule settlement spec. ![tool: MIT](https://img.shields.io/badge/tool-MIT-blue?style=flat-square) ![last commit](https://img.shields.io/github/last-commit/roy-tong/AgentMeasure?style=flat-square&label=)
- [Cloud FinOps Skill](https://github.com/OptimNow/cloud-finops-skills) - Markdown reference library for agents, packaged as a Claude skill and an MCP server, covering billing mechanics for AI, cloud, and SaaS spend. ![tool: CC BY-SA 4.0](https://img.shields.io/badge/tool-CC_BY--SA_4.0-blue?style=flat-square) ![last commit](https://img.shields.io/github/last-commit/OptimNow/cloud-finops-skills?style=flat-square&label=)
- [FinOps for AI](https://www.finops.org/framework/scope/finops-for-ai/) - FinOps Foundation practitioner framework for governing AI, GPU, and token spend. ![tool](https://img.shields.io/badge/tool-blue?style=flat-square)
- [Vaudit TokenAudit](https://www.vaudit.com/token-audit) - Vaudit's LLM invoice-reconciliation product, from an independent spend-auditing and recovery platform. ![co](https://img.shields.io/badge/co-555?style=flat-square)

## Budgets Caps

### Tools
- [AWS Spend Limits](https://docs.aws.amazon.com/accounts/latest/reference/create-spend-limit.html) - AWS project-level spend limits, announced 2026-09-16 for a limited set of customers, pause a project's resources when spend reaches the limit, with optional earlier controls on the top cost drivers. ![tool: proprietary](https://img.shields.io/badge/tool-proprietary-blue?style=flat-square)
- [Claude Code Review Billing](https://code.claude.com/docs/en/code-review-costs) - Anthropic's Code Review has no flat per-review price, bills tokens through usage credits outside plan limits, defaults new repositories to a review after every push, and offers a monthly spend limit. ![tool: proprietary](https://img.shields.io/badge/tool-proprietary-blue?style=flat-square)
- [TrueFoundry AI Gateway Budget Limiting](https://www.truefoundry.com/docs/ai-gateway/budgetlimiting) - TrueFoundry documentation on budget limits in its AI gateway for GenAI deployments. ![co](https://img.shields.io/badge/co-555?style=flat-square)

### Reading
- [Claude Max Plan Usage](https://support.claude.com/en/articles/11049741-what-is-the-max-plan) - Anthropic support article describing Max plan usage as multipliers of Pro, without absolute quota numbers.

## Policy Enforcement

### Tools
- [ActPlane](https://github.com/eunomia-bpf/ActPlane) - Policy-enforcement engine, built on eBPF at the OS level, for AI-agent harnesses like Claude Code and Codex. ![tool: MIT](https://img.shields.io/badge/tool-MIT-blue?style=flat-square) ![last commit](https://img.shields.io/github/last-commit/eunomia-bpf/ActPlane?style=flat-square&label=)
- [AEGIS](https://github.com/Justin0504/Aegis) - Open-source (MIT) pre-execution firewall and cryptographic audit layer for AI agents. ![tool: MIT](https://img.shields.io/badge/tool-MIT-blue?style=flat-square) ![last commit](https://img.shields.io/github/last-commit/Justin0504/Aegis?style=flat-square&label=)
- [MCPGuard-Dynamic](https://github.com/facebook/mcpguard-dynamic) - Research-grade kernel-level eBPF sandbox for MCP, published under Meta's GitHub organization. ![tool: MIT](https://img.shields.io/badge/tool-MIT-blue?style=flat-square) ![last commit](https://img.shields.io/github/last-commit/facebook/mcpguard-dynamic?style=flat-square&label=)

## Spend Management

### Tools
- [ChatGPT Enterprise Spend Controls](https://openai.com/index/chatgpt-enterprise-spend-controls/) - OpenAI post on usage analytics and spend controls for ChatGPT Enterprise and Business: credit caps, request workflows, and a Cost API. ![tool: proprietary](https://img.shields.io/badge/tool-proprietary-blue?style=flat-square)
- [Claude Enterprise Admin Controls](https://www.claude.com/blog/giving-admins-more-visibility-and-control-over-claude-usage-and-spend) - Anthropic post on admin analytics and cost controls for Claude Enterprise and Team: spend caps, model defaults, and per-user cost analytics. ![tool: proprietary](https://img.shields.io/badge/tool-proprietary-blue?style=flat-square)
- [nable](https://github.com/getnable/finopsmcp) - MCP server that reports cloud and AI spend in one answer, running locally with a free local package and some paid features. ![tool: Apache-2.0](https://img.shields.io/badge/tool-Apache--2.0-blue?style=flat-square) ![last commit](https://img.shields.io/github/last-commit/getnable/finopsmcp?style=flat-square&label=)
- [PointFive TokenShift](https://www.pointfive.co/press/pointfive-launches-ai-efficiency-os-tokenshift) - PointFive's AI Efficiency OS, which governs coding-agent token spend across Claude Code, Cursor, Codex, and other tools. ![co](https://img.shields.io/badge/co-555?style=flat-square)
- [Revenium](https://www.revenium.ai/) - Tracks AI agent spend at runtime, attributing every model call and tool cost to its workflow, with automatic shutoff on runaway budgets. ![co](https://img.shields.io/badge/co-555?style=flat-square)
- [Vantage](https://www.vantage.sh/blog/agentic-coding-costs) - FinOps platform that ingests token-level cost data from Anthropic and OpenAI usage APIs, plus Cursor and cloud spend. ![co](https://img.shields.io/badge/co-555?style=flat-square)
- [Vercel AI Gateway Budgets](https://vercel.com/changelog/budgets-for-api-keys-on-ai-gateway) - Vercel changelog on per-API-key dollar spend caps with daily, weekly, or monthly refresh. ![tool: proprietary](https://img.shields.io/badge/tool-proprietary-blue?style=flat-square)

## Unit Economics

### Tools
- [Paid](https://paid.ai/) - Monetization platform for AI agents that sets pricing, tracks delivery cost per action, and reports margin per customer. ![co](https://img.shields.io/badge/co-555?style=flat-square)
