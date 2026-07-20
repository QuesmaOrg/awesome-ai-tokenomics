---
verified_on: 2026-07-02
stale_after: 2026-10-02
sources:
  - https://www.mindstudio.ai/blog/smart-orchestrator-cheaper-sub-agent-models-claude-code
  - https://cognition.com/blog/devin-fusion
  - https://www.anthropic.com/engineering/multi-agent-research-system
  - https://arxiv.org/abs/2604.02460
  - https://arxiv.org/abs/2605.09104
  - https://docs.crewai.com/en/learn/hierarchical-process
  - https://arxiv.org/abs/2604.17400
  - https://arxiv.org/abs/2603.15183
  - https://arxiv.org/abs/2510.26585
  - https://github.com/lm-sys/RouteLLM
  - https://www.notdiamond.ai/
  - https://arxiv.org/abs/2605.06350
  - https://arxiv.org/abs/2606.27457
  - https://openrouter.ai/docs/guides/routing/provider-selection
  - https://github.com/BerriAI/litellm
  - https://portkey.ai/docs/product/ai-gateway/virtual-keys/budget-limits
  - https://github.com/maximhq/bifrost
  - https://github.com/vllm-project/semantic-router
  - https://docs.litellm.ai/docs/tutorials/claude_non_anthropic_models
  - https://docs.litellm.ai/docs/proxy/custom_pricing
---
# Orchestration economics: the tax nobody has measured

**Orchestration (a frontier "orchestrator" model delegating sub-tasks to cheaper "worker" models, or several agents splitting one job) is now the default way to build serious agentic systems, yet nobody can say what the coordination itself costs. The pattern is industry-standard; its price is not.**

- **For orchestration:** one vendor's own engineering write-up reports multi-agent beating single-agent by 90.2% on their research evaluation, while burning roughly 15x the tokens of a single chat call. The same write-up finds token usage alone explains about 80% of the performance variance: read plainly, much of the multi-agent win is spend, not architecture.
- **Against orchestration:** controlled research finds single-agent systems match or beat multi-agent systems once reasoning tokens are held constant: the orchestration win may be a token-budget effect wearing an architecture costume. Both findings are single-source; neither should be treated as settled.
- **Where the tax actually sits:** hand-offs duplicate context between agents, and framework mechanics differ measurably, though every specific overhead percentage circulating has failed independent verification: only task-success deltas hold up. The decision layer itself costs too: who picks the model per step ranges from a free rule-based router to a full model call per routing decision, each with its own economics. The routing-infrastructure layer (gateways that price and route the mix) is commoditizing: it meters and switches, but passes no judgment on whether the orchestration pattern earned its overhead.

**Our read:** the orchestration tax is a harness-side, dollar-denominated quantity that every multi-agent adopter pays and nobody can quote. Measuring its overhead honestly (orchestrator tokens plus hand-off duplication, against a single-agent counterfactual) is open territory.

Go deeper: [Measuring capability-limit vs harness-waste](measuring-capability-vs-harness-waste.md) · [Model economics](model-economics.md) · [Model-tier routing practice](../practices/model-tier-routing.md)

## Sources
- https://www.mindstudio.ai/blog/smart-orchestrator-cheaper-sub-agent-models-claude-code
- https://cognition.com/blog/devin-fusion
- https://www.anthropic.com/engineering/multi-agent-research-system
- https://arxiv.org/abs/2604.02460
- https://arxiv.org/abs/2605.09104
- https://docs.crewai.com/en/learn/hierarchical-process
- https://arxiv.org/abs/2604.17400
- https://arxiv.org/abs/2603.15183
- https://arxiv.org/abs/2510.26585
- https://github.com/lm-sys/RouteLLM
- https://www.notdiamond.ai/
- https://arxiv.org/abs/2605.06350
- https://arxiv.org/abs/2606.27457
- https://openrouter.ai/docs/guides/routing/provider-selection
- https://github.com/BerriAI/litellm
- https://portkey.ai/docs/product/ai-gateway/virtual-keys/budget-limits
- https://github.com/maximhq/bifrost
- https://github.com/vllm-project/semantic-router
- https://docs.litellm.ai/docs/tutorials/claude_non_anthropic_models
- https://docs.litellm.ai/docs/proxy/custom_pricing
