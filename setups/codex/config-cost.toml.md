---
verified_on: 2026-07-18
sources:
  - https://learn.chatgpt.com/docs/config-file/config-reference
  - https://learn.chatgpt.com/docs/config-file/config-basic
---

# Codex CLI `config.toml`: cost levers

**TL;DR:** every key name below was fetched live from OpenAI's own config reference on 2026-07-18 (the in-repo `docs/config.md` on `github.com/openai/codex` is now a stub that points here, so don't cite the GitHub file directly: it has no content). Paste the block into `~/.codex/config.toml` or your project's `.codex/config.toml` and adjust the values.

## The copy-paste block

```toml
# Reasoning effort for supported models (Responses API only; xhigh is model-dependent).
# Accepted: minimal | low | medium | high | xhigh
model_reasoning_effort = "medium"

# Token threshold that triggers automatic history compaction.
# Unset uses model defaults.
model_auto_compact_token_limit = 100000

# Whether that threshold counts the full active context or only growth after the
# cached prefix. Accepted: total | body_after_prefix
model_auto_compact_token_limit_scope = "body_after_prefix"

# Token budget for storing an individual tool/function output in history.
tool_output_token_limit = 10000

# Controls when Codex pauses for your approval before executing a command.
# Accepted: untrusted | on-request | never | { granular = {...} }
approval_policy = "on-request"

# Sandbox policy for filesystem/network access during command execution.
# Accepted: read-only | workspace-write | danger-full-access
sandbox_mode = "workspace-write"

# Provider id from [model_providers] (default: "openai").
model_provider = "openai"

# Preferred service tier for new turns. Built-in values include "flex" and "fast".
service_tier = "flex"
```

## What each key actually controls

| Key | Values | What it does |
| --- | --- | --- |
| `model_reasoning_effort` | `minimal` / `low` / `medium` / `high` / `xhigh` | Directly trades reasoning depth for tokens billed as reasoning output. |
| `model_auto_compact_token_limit` | number | Compaction is a costed operation: this is the trigger point, not automatic at some hidden default unless you leave it unset. |
| `model_auto_compact_token_limit_scope` | `total` / `body_after_prefix` | Whether a stable cached prefix counts against the compaction trigger. Get this wrong and you either compact too eagerly (losing cache value) or too late (paying full context every turn). |
| `tool_output_token_limit` | number | Caps how much of a single tool/function result gets kept in history: the Codex-side equivalent of "don't let the agent read a 10,000-line log." |
| `approval_policy` | `untrusted` / `on-request` / `never` / granular | Not a token-cost lever directly, but every unnecessary approval round-trip is a retry, and every over-permissive setting risks a runaway loop that is a token-cost lever. |
| `sandbox_mode` | `read-only` / `workspace-write` / `danger-full-access` | Same logic as `approval_policy`: tighter sandboxing reduces the blast radius of a wrong command, which reduces retry/cleanup cost. |
| `model_provider` | provider id string | Which entry in `[model_providers]` serves the model, relevant if you're routing to a cheaper provider for some tasks. |
| `service_tier` | string, e.g. `flex`, `fast` | Provider-side service tier for the turn: a direct cost/latency trade, not a routing decision Codex makes for you. |

## What we left out

The Codex docs' basic-config page also lists `personality`, `web_search` (`cached`/`indexed`/`live`/`disabled`), `log_dir`, `default_permissions`, `[windows]`, `[shell_environment_policy]`, and `[features]`, none of these are cost levers, so they're out of scope here even though they're real, current config keys.
