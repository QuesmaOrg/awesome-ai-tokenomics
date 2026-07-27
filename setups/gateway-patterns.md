---
verified_on: 2026-07-18
sources:
  - https://code.claude.com/docs/en/costs
  - https://github.com/teremterem/claude-code-gpt-5-codex
  - https://github.com/cabinlab/litellm-claude-code
  - https://github.com/numman-ali/cc-mirror
  - https://github.com/NadirRouter/NadirClaw
  - https://github.com/musistudio/claude-code-router
  - https://docs.litellm.ai/docs/proxy/virtual_keys
---

# Which "cheaper Claude Code" gateway pattern do you actually want?

**TL;DR:** five different shapes all get called "the LiteLLM pattern" or "run Claude Code cheap," and they solve different problems. Picking the wrong one means either the wrong integration effort or the wrong outcome. Repo star counts and licenses below are live-pulled from the GitHub API, 2026-07-18.

## Bridge-out: point Claude Code at a non-Anthropic model

**What it is:** a local LiteLLM proxy remaps Anthropic model names to another vendor's models, then you launch Claude Code with `ANTHROPIC_BASE_URL` pointed at that proxy.
**When it's right:** you want to keep the Claude Code harness (its tools, its UX) but swap the model underneath for a specific reason: cost, a model you prefer for some task, or testing.
**Cost mechanism:** you pay the other provider's price instead of Anthropic's; the proxy itself adds negligible overhead.
**Example:** [teremterem/claude-code-gpt-5-codex](https://github.com/teremterem/claude-code-gpt-5-codex) - MIT: one `.env` (`REMAP_CLAUDE_SONNET_TO=gpt-5-codex-reason-medium`), one `docker run`/`uv run litellm`, one env var at launch. This is the minimal drop-in shape people actually copy-paste. ![last commit](https://img.shields.io/github/last-commit/teremterem/claude-code-gpt-5-codex?style=flat-square&label=)

## Bridge-in: expose Claude through an OpenAI-compatible interface

**What it is:** the inverse of bridge-out: LiteLLM exposes *Claude* via an OpenAI-compatible interface so OpenAI-format clients can call it.
**When it's right:** you have existing tooling built against the OpenAI API shape and want to route some of that traffic to Claude models, not the other way around.
**Cost mechanism:** same Anthropic pricing, just reachable through a different client contract.
**Example:** [cabinlab/litellm-claude-code](https://github.com/cabinlab/litellm-claude-code) - no license file: don't confuse this with bridge-out; they're often cited under the same "litellm-claude-code" name but do opposite things. No license file also means: check with the maintainer before depending on this in anything you'd redistribute. ![last commit](https://img.shields.io/github/last-commit/cabinlab/litellm-claude-code?style=flat-square&label=)

## Isolated-install: separate Claude Code distributions per provider

**What it is:** doesn't touch env vars or a proxy at all. Creates fully separate Claude Code installs under `~/.cc-mirror/<variant>/`, each mapping its Sonnet/Opus/Haiku slots onto a different provider's native models.
**When it's right:** you want "Claude Code, but cheap or local," want multiple providers available side by side without juggling env vars per session, or want a one-liner onboarding rather than infra to run.
**Cost mechanism:** whatever the target provider charges for the mapped model, no proxy tax.
**Example:** [numman-ali/cc-mirror](https://github.com/numman-ali/cc-mirror) - MIT: the highest-traction isolated-install tool in this survey. `npx cc-mirror quick --provider <p> --api-key <k> --model-sonnet "p/model" --model-opus "p/model"`. This is the artifact people reach for more than a raw LiteLLM config. ![last commit](https://img.shields.io/github/last-commit/numman-ali/cc-mirror?style=flat-square&label=)

## Router-with-classifier: route by request complexity, not by provider

**What it is:** a drop-in OpenAI-compatible proxy that classifies each prompt (simple vs. complex) and routes accordingly, escalating to a stronger model on low-confidence output.
**When it's right:** you're optimizing cost *within* a single provider relationship or across several, at the request level, and want that decision automated rather than picked by a human per task.
**Cost mechanism:** cheap-model-by-default, escalate-on-signal: the savings depend entirely on how good the classifier is; treat any vendor's savings percentage as unconfirmed until measured on your own workload.
**Example:** [NadirRouter/NadirClaw](https://github.com/NadirRouter/NadirClaw) - **PolyForm Noncommercial License 1.0.0**: the most substantive tool in this tier, with two caveats. Its published benchmark figures (RouterBench AUROC 0.961, the RouterArena #5 claim) describe the paid Nadir Pro classifier - the project's own README says the free OSS classifier is a simpler binary centroid with no benchmark attached. And it is **not free for commercial use**: confirm the license before adopting it at a company. ![last commit](https://img.shields.io/github/last-commit/NadirRouter/NadirClaw?style=flat-square&label=)

## Control-plane: one local endpoint, routing rules you author

**What it is:** a persistent local gateway that puts Claude Code - and also Codex, OpenCode, and other compatible CLIs - behind one endpoint, with ordered condition rules (by header, body, or estimated token count), per-rule fallbacks, and optional Node.js script rules deciding which provider and model serves each request. A prompt-tag mechanism also lets the agent itself pick the model for each subagent it spawns.
**When it's right:** you want several providers and routing policies behind one stable endpoint, with rules you write yourself, rather than a fixed remap or an automatic classifier.
**Cost mechanism:** whatever your rules route to; the project itself publishes no savings figure. Request logs include token usage and cost estimates, so you can measure your own outcome.
**Example:** [musistudio/claude-code-router](https://github.com/musistudio/claude-code-router) - MIT: the highest-traction repo in this survey, actively maintained. Caution: routing scripts run as fully trusted code with access to your environment variables and request headers, including credentials - only use scripts you wrote yourself. ![last commit](https://img.shields.io/github/last-commit/musistudio/claude-code-router?style=flat-square&label=)

## Anthropic's own position

The official costs docs name LiteLLM by name, verbatim: *"Several large enterprises reported using LiteLLM, an open-source tool that [tracks spend by key](https://docs.litellm.ai/docs/proxy/virtual_keys). This project is unaffiliated with Anthropic and has not been audited for security."* ([code.claude.com/docs/en/costs](https://code.claude.com/docs/en/costs)). Anthropic tolerates the gateway pattern for enterprise per-key spend tracking; it does not endorse or audit it.

## Picking one

- Want to keep Claude Code's UX, swap the model: **bridge-out**.
- Have OpenAI-shaped tooling, want it to call Claude: **bridge-in**.
- Want multiple providers side by side with minimal setup: **isolated-install**.
- Want per-request cost optimization by complexity, and can accept the license: **router-with-classifier**.
- Want one endpoint with routing rules you author yourself, across several CLIs: **control-plane**.
