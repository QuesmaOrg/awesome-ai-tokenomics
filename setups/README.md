# Setups & skills

**TL;DR:** copy-paste configs for running Claude Code and Codex cheaper: a reference `CLAUDE.md` cost section, a model-routing `settings.json` pattern, a Codex `config.toml` cost block, a gateway-pattern disambiguation note, and two skills. Below that, a short list of existing tools worth installing instead of reinventing them.

## What's here

- [`claude-code/CLAUDE.md-cost-template.md`](claude-code/CLAUDE.md-cost-template.md) - a reference cost-management section for your `CLAUDE.md`, assembling the full official knob list into one copy-paste block. Every knob traces to a live fetch of the vendor's own docs.
- [`claude-code/settings-model-routing.md`](claude-code/settings-model-routing.md) - a `settings.json` + per-subagent model pattern that encodes a tiered escalation *policy*. This pattern has run in production on our own research stack since 2026-07-02.
- [`codex/config-cost.toml.md`](codex/config-cost.toml.md) - Codex `config.toml` cost levers: reasoning effort, auto-compaction limits, tool-output caps, approval policy, service tier. Every key traces to a live fetch of OpenAI's own config docs.
- [`gateway-patterns.md`](gateway-patterns.md) - four different things all get called "the LiteLLM pattern": a one-paragraph-each disambiguation of which shape you actually want.
- [`skills/cost-review.md`](skills/cost-review.md) - a copy-paste skill that audits your own usage JSONL against a checklist instead of citing marketing savings numbers. Untested as a skill: the frontmatter matches the documented format, but it hasn't run end-to-end.
- [`skills/cache-hygiene-audit.md`](skills/cache-hygiene-audit.md) - a companion skill that checks a `CLAUDE.md`/settings setup for cache-invalidating patterns before you commit them. Same caveat: untested end-to-end.

## Tools worth using instead of reinventing

This niche already has real, maintained tools for usage tracking and provider-swapping. Don't rebuild these: install them. Each entry shows its license plus live GitHub star and last-commit badges.

- [ccusage](https://github.com/ccusage/ccusage) - MIT: reads local session JSONL (no API calls) across Claude Code, Codex, OpenCode, Amp, Droid, Gemini CLI, and Copilot CLI. The de facto dependency most other statusline/monitor tools in this space build on. ![stars](https://img.shields.io/github/stars/ccusage/ccusage?style=flat-square&logo=github&label=) ![last commit](https://img.shields.io/github/last-commit/ccusage/ccusage?style=flat-square&label=)
- [claude-code-statusline](https://github.com/rz1989s/claude-code-statusline) - MIT: the top standalone statusline that parses `~/.claude/projects/*.jsonl` directly with no `ccusage` dependency, plus MCP-server health monitoring. ([cship](https://github.com/stephenleo/cship), Apache-2.0, is a credible Starship-style alternative in the same tier. ![stars](https://img.shields.io/github/stars/stephenleo/cship?style=flat-square&logo=github&label=) ![last commit](https://img.shields.io/github/last-commit/stephenleo/cship?style=flat-square&label=)) ![stars](https://img.shields.io/github/stars/rz1989s/claude-code-statusline?style=flat-square&logo=github&label=) ![last commit](https://img.shields.io/github/last-commit/rz1989s/claude-code-statusline?style=flat-square&label=)
- [splitrail](https://github.com/Piebald-AI/splitrail) - MIT: cross-platform CLI + VS Code extension + cloud dashboard covering Claude Code, Codex CLI, Gemini CLI, Cline, Roo Code, Kilo Code, Copilot, OpenCode, and Pi Agent. ![stars](https://img.shields.io/github/stars/Piebald-AI/splitrail?style=flat-square&logo=github&label=) ![last commit](https://img.shields.io/github/last-commit/Piebald-AI/splitrail?style=flat-square&label=)
- [cc-mirror](https://github.com/numman-ali/cc-mirror) - MIT: the highest-traction repo in this space. Creates isolated Claude Code installs per provider (`~/.cc-mirror/<variant>/`), mapping Sonnet/Opus/Haiku slots onto provider-native models. It's the artifact people actually reach for over a raw LiteLLM proxy. See [gateway-patterns.md](gateway-patterns.md) for how this differs from a LiteLLM bridge. ![stars](https://img.shields.io/github/stars/numman-ali/cc-mirror?style=flat-square&logo=github&label=) ![last commit](https://img.shields.io/github/last-commit/numman-ali/cc-mirror?style=flat-square&label=)
- [NadirClaw](https://github.com/NadirRouter/NadirClaw) - **PolyForm Noncommercial License 1.0.0**: the most substantive router-with-classifier tool we found (sentence-embedding classifier, claims RouterArena #5). License note: it permits personal/research/education use only. Commercial use requires a paid license. Confirm your use case against the license text before adopting it at a company. ![stars](https://img.shields.io/github/stars/NadirRouter/NadirClaw?style=flat-square&logo=github&label=) ![last commit](https://img.shields.io/github/last-commit/NadirRouter/NadirClaw?style=flat-square&label=)

---

Text content here: CC-BY 4.0 ([../LICENSE](../LICENSE)). Any code/config snippets in this directory: MIT ([../LICENSE-CODE](../LICENSE-CODE)).
