# Understand

## Buyer Incentives

### Tools
- [Lanai](https://www.prnewswire.com/news-releases/lanai-launches-ai--work-operating-system-to-help-enterprises-close-the-ai-accountability-gap-302743892.html) - Lanai's AI @ Work platform discovers every sanctioned and shadow AI workflow across an org and maps its token spend to the KPIs it actually drives. ![co](https://img.shields.io/badge/co-555?style=flat-square)

### Research & Benchmarks
- [State of FinOps 2026 - AI spend management is now the norm](https://data.finops.org/) - This is the FinOps Foundation's sixth annual State of FinOps survey, the practitioner census of how organizations manage cloud and AI spend. ![report](https://img.shields.io/badge/report-555?style=flat-square)

### Reading
- [Claude "subscription arbitrage" and its (announced, then paused) end](https://zed.dev/blog/anthropic-subscription-changes) - Users route agentic workloads worth far more than a subscription's price through cheap Pro/Max plans; Anthropic tried to close this, then paused the fix.
- [Coding-agent native spend controls (2026)](https://cursor.com/changelog/05-04-26) - Within six weeks in 2026, Cursor, GitHub Copilot, and OpenAI each shipped native admin spend controls: budget caps, credit metering, usage dashboards.
- [GitHub Copilot metered-billing bill-shock - the demand-side reaction ("tokenpocalypse")](https://news.ycombinator.com/item?id=47923357) - GitHub's move from flat-rate Copilot plans to metered AI Credits exposed agentic workflows' true per-token cost and triggered a mass bill-shock backlash.
- [The "$47k Claude Code bill" - the anchor bill-shock anecdote and its mechanistic debunk](https://yusufhansacak.medium.com/the-47-000-agent-bill-what-the-viral-token-stories-get-wrong-7ee1cdd81e65) - A viral $47,000-in-90-days Claude Code bill story was debunked by a teardown pinning the real driver on quadratic context re-ingestion, not runaway use.
- [Uber caps AI-coding spend at $1,500/mo per tool after burning its budget in ~4 months](https://techcrunch.com/2026/06/02/uber-caps-employee-ai-spending-after-blowing-through-budget-in-four-months/) - Uber capped AI-coding spend at $1,500 per employee per tool after burning its entire annual budget in roughly four months of encouraged maximal use.

## Compression Efficacy

### Reading
- [Token-saving plugins are mostly a stupid idea (Tura benchmark)](https://turaai.net/blog#token-saving-plugins-are-mostly-stupid-idea) - A benchmark of token-saving plugins found one actively worse than none: cost up 7.2%, tokens up 13.2%, because it broke an already-cached prompt prefix.

## Consolidation

### Tools
- [Cisco acquires Galileo (LLM eval/observability) → folded into Splunk Observability](https://blogs.cisco.com/news/cisco-announces-the-intent-to-acquire-galileo) - Cisco acquired Galileo, an LLM/agent evaluation and observability platform, folding it into Splunk Observability Cloud's AI Agent Monitoring. ![co](https://img.shields.io/badge/co-555?style=flat-square)
- [Tokenomics Foundation (Linux Foundation + FinOps Foundation)](https://www.linuxfoundation.org/press/linux-foundation-announces-the-intent-to-launch-the-tokenomics-foundation-to-establish-open-standards-for-ai-cost-management) - The Linux Foundation is launching the Tokenomics Foundation to build open standards for AI token spend, extending FOCUS to cover token-based costs. ![co](https://img.shields.io/badge/co-555?style=flat-square)

## Market Competitors

### Tools
- [Amp (Sourcegraph) - pay-as-you-go, no-markup pricing + mode-based routing](https://ampcode.com/) - Amp, Sourcegraph's coding agent, passes through LLM cost with zero markup for individuals and teams, with a cost/capability mode: Deep, Smart, or Rush. ![tool](https://img.shields.io/badge/tool-blue?style=flat-square)
- [Factory (droids) - subscription pricing + $150M Series C at $1.5B](https://factory.ai/pricing) - Factory prices its Droids agents as flat subscription tiers ($20/$100/$200/mo) with usage-based rate limits, not per-token metering, after a $150M round. ![co](https://img.shields.io/badge/co-555?style=flat-square)
- [Gemini CLI retirement → Antigravity CLI (open-source coding agent closes, pricing restructures)](https://developers.googleblog.com/an-important-update-transitioning-gemini-cli-to-antigravity-cli/) - Google retired the open-source Gemini CLI on 2026-06-18, pushing users onto closed-source Antigravity CLI and $100/$200-per-month paid tiers. ![tool](https://img.shields.io/badge/tool-blue?style=flat-square)
- [OpenHands - MIT OSS coding agent, free local + free cloud tier, at-cost LLM option](https://github.com/OpenHands/OpenHands) - An MIT-licensed open-source coding-agent platform with a free local mode, a free cloud tier, and an at-cost LLM pricing option. ![tool: MIT](https://img.shields.io/badge/tool-MIT-blue?style=flat-square) ![stars](https://img.shields.io/github/stars/OpenHands/OpenHands?style=flat-square&logo=github&label=) ![last commit](https://img.shields.io/github/last-commit/OpenHands/OpenHands?style=flat-square&label=)

## Market Sizing

### Research & Benchmarks
- [Gartner - worldwide AI spending forecast: $2.59T in 2026 (+47% YoY)](https://www.gartner.com/en/newsroom/press-releases/2026-05-19-gartner-forecasts-worldwide-ai-spending-to-grow-47-percent-in-2026) - Gartner's latest forecast puts worldwide AI spending at $2.59 trillion in 2026, up 47% year-over-year, with infrastructure over 45% of the total. ![report](https://img.shields.io/badge/report-555?style=flat-square)
- [Menlo Ventures - enterprise generative-AI spend $11.5B → $37B (2024→2025)](https://menlovc.com/perspective/2025-the-state-of-generative-ai-in-the-enterprise/) - Menlo Ventures found enterprise generative-AI spend hit $37B in 2025, up 3.2x from 2024, with coding tools the largest application category at $7.3B. ![report](https://img.shields.io/badge/report-555?style=flat-square)

## Model Economics

### Research & Benchmarks
- [Artificial Analysis - Coding Agent Index (tokens & cost per task, model × harness)](https://artificialanalysis.ai/agents/coding-agents) - This benchmark scores full model-plus-harness stacks, spanning $0.27 to $11.80 per task: a roughly 44x range at similar quality, per Artificial Analysis. ![bench](https://img.shields.io/badge/bench-555?style=flat-square)
- [Artificial Analysis - Intelligence Index + Blended Price (intelligence-per-dollar leaderboard)](https://artificialanalysis.ai/leaderboards/models) - Artificial Analysis's Intelligence Index plots a 0-100 capability score against blended price per million tokens, live across 85-122 base LLMs. ![bench](https://img.shields.io/badge/bench-555?style=flat-square)
- [OckBench - measuring token efficiency / verbosity of LLM reasoning](https://arxiv.org/abs/2511.05722) - OckBench answers a specific tokenomics question: which model burns the most tokens for the same answer? ![paper](https://img.shields.io/badge/paper-555?style=flat-square)
- [Reasoning-token consumption behavior - length ≠ effort, and verbosity is a separate lever](https://arxiv.org/abs/2602.13517) - Chain-of-thought can burn about 258 tokens on problems a direct answer solves in 15 (roughly 17x overhead), and simple agentic steps trigger it by accident. ![paper](https://img.shields.io/badge/paper-555?style=flat-square)

### Reading
- ["Qwen 3.6 27B is the sweet spot for local development" - Migdał / Quesma (first-party)](https://quesma.com/blog/qwen-36-is-awesome/) - Piotr Migdał's #1-on-Hacker-News essay argues Qwen3.6-27B (dense) is the first local model good enough for real coding instead of a metered cloud API.
- [Kimi K2.6/K2.7-Code and GLM-5.2 official API pricing](https://platform.kimi.ai/docs/pricing/chat-k27-code) - Kimi K2.7-Code ($0.95/$4.00 per million tokens) and GLM-5.2 ($1.40/$4.40) both undercut Claude Sonnet 5 and GPT-5.5 on raw price by 2-5x.
- [Local / open-model economics for coding - state of the field (2026)](https://huggingface.co/Qwen/Qwen3.6-27B) - Open-weight coding models now score 77-81% on SWE-bench Verified, within a few points of closed frontier models, reshaping self-host-vs-API math.
- [Reasoning-token billing across providers - the hidden output multiplier](https://developers.openai.com/api/docs/guides/reasoning) - Every major AI provider bills a model's hidden reasoning tokens at the most expensive output rate, without ever returning them to the caller.

## Pricing Models

### Research & Benchmarks
- [Tokenization multiplicity & overcharging - the pay-per-token integrity problem](https://arxiv.org/abs/2506.06446) - Two academic papers show the same output can be billed a different token count depending on tokenization, and providers can be incentivized to inflate it. ![paper](https://img.shields.io/badge/paper-555?style=flat-square)

### Reading
- [Batch / Priority / Flex service tiers - the scheduling axis of token pricing (clustered, cross-vendor)](https://platform.claude.com/docs/en/docs/build-with-claude/batch-processing) - Every major LLM vendor sells the same lever, trading latency for price via async batch scheduling, with Anthropic, OpenAI, and Google all near 50% off.
- [Bessemer - the AI pricing & monetization playbook (seat → usage → outcome)](https://www.bvp.com/atlas/the-ai-pricing-and-monetization-playbook) - Bessemer's playbook argues AI pricing is shifting from per-seat to consumption/outcome-based, citing Intercom's $0.99-per-resolved-ticket model.
- [Cached-input discounts - the ~90%-off lever behind cache-accounting](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) - Cache-read pricing discounts input tokens by about 90%: the biggest lever on an agentic bill, since input is roughly 85% of session cost.
- [ChatGPT subscription tiers and Codex CLI bundling/pricing (2026)](https://developers.openai.com/codex/pricing) - OpenAI bundles Codex CLI into every ChatGPT tier from Free through the new $100/mo Pro plan, differing only by rate-limit multiplier.
- [ChatGPT workspace-agent credit billing (effective July 6, 2026)](https://help.openai.com/en/articles/11481834-chatgpt-rate-card) - OpenAI ended the free preview for agent runs invoked inside ChatGPT Business, Enterprise, Edu, and Teachers on 2026-07-06.
- [Fable 5 leaves subscription inclusion - frontier tier moves to usage-credit metering (July 7 cliff)](https://www.anthropic.com/news/redeploying-fable-5) - Anthropic is moving Fable 5 off subscription-included access onto usage-credit metering, with the cliff date slipped twice, now set for 2026-07-20.
- [Google AI Pro price and Gemini/Antigravity free-tier limits (2026)](https://gemini.google/subscriptions/) - Google AI Pro is confirmed at $19.99/month, beneath the $99.99 and $199.99 AI Ultra tiers giving higher rate limits on the Gemini API and Antigravity.
- [GPT-5.6 family (Sol / Terra / Luna) - API pricing](https://developers.openai.com/api/docs/pricing) - OpenAI's GPT-5.6 family prices three tiers 2x apart: Sol at $5/$30 per million tokens, Terra at $2.50/$15, and Luna at $1/$6.
- [LiteLLM flex/priority service-tier cost keys - the harness-level tier-routing lever](https://docs.litellm.ai/docs/proxy/custom_pricing) - LiteLLM automatically prices requests made at a non-standard tier like flex or priority, applying the right discounted or premium rate automatically.
- [LLM price decline + Jevons paradox - unit price crashes, total spend climbs](https://a16z.com/llmflation-llm-inference-cost/) - Per-token prices are falling roughly an order of magnitude per year, while total AI spend rises even faster.
- [LLM token pricing dimensions - the structure of a token bill](https://platform.claude.com/docs/en/about-claude/pricing) - This maps out how frontier LLM APIs meter and price tokens, read straight off the two largest providers' pricing pages, Anthropic and OpenAI.
- [OpenAI is winding down the self-serve fine-tuning API and platform](https://developers.openai.com/api/docs/deprecations) - OpenAI is winding down self-serve fine-tuning because prompting got cheaper and more capable than fine-tuning for most uses, cutting off customers by 2027.

## Reliability Sla

### Reading
- [Reserved-capacity reliability economics (Azure PTU · AWS Bedrock MU)](https://learn.microsoft.com/en-us/azure/ai-foundry/openai/concepts/provisioned-throughput) - Azure's Provisioned Throughput Units and AWS Bedrock's Model Units both let buyers reserve guaranteed capacity, billed hourly whether or not it's used.

## Unit Economics

### Research & Benchmarks
- [Cost-of-Pass - an economic framework for evaluating language models](https://arxiv.org/abs/2504.13359) - Cost-of-Pass defines the expected dollar cost of one correct answer as inference cost divided by success rate, pricing benchmark accuracy directly. ![paper](https://img.shields.io/badge/paper-555?style=flat-square)
- [DORA 2025 - AI as amplifier, and the delivery-stability tension](https://dora.dev/insights/balancing-ai-tensions/) - Google's DORA program found that as AI adoption becomes universal, delivery throughput rises but so does instability: AI as an amplifier, not a pure win. ![report](https://img.shields.io/badge/report-555?style=flat-square)
- [Faros - "The Acceleration Whiplash" (AI Engineering Report 2026)](https://pages.faros.ai/hubfs/AI_Engineering_Report_2026_The_Acceleration_Whiplash_Faros.pdf) - This is the load-bearing "velocity has a hidden bill" study: telemetry from 22,000 developers across 4,000 teams over two years. ![report](https://img.shields.io/badge/report-555?style=flat-square)
- [METR - measured vs perceived AI productivity (the RCT)](https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/) - METR's controlled trial found developers took 19% longer to finish issues when allowed to use AI, while still believing it had sped them up by 20%. ![paper](https://img.shields.io/badge/paper-555?style=flat-square)

### Reading
- [Cloud Capital - gross margin in the age of AI (the vendor/supply side)](https://www.cloudcapital.co/learn/gross-margin-in-the-age-of-ai) - AI-native software runs at roughly 50-60% gross margin versus 70-80% for SaaS, since inference and compute became a large, variable cost of goods sold.
- [getDX - AI coding assistant pricing & ROI guide (2026)](https://getdx.com/blog/ai-coding-assistant-pricing/) - Typical AI coding tools cost $200-600 per engineer monthly in seat plus token spend, per getDX, for a median 7.76% PR gain: below vendors' claimed 3-10x.
