---
verified_on: 2026-07-18
sources:
  - https://code.claude.com/docs/en/costs
  - https://code.claude.com/docs/en/sub-agents
  - https://code.claude.com/docs/en/skills
  - https://code.claude.com/docs/en/settings
---

# `CLAUDE.md` cost section: reference template

**TL;DR:** a copy-paste section for your `CLAUDE.md` that assembles Anthropic's own cost-reduction knobs (`code.claude.com/docs/en/costs`, fetched 2026-07-18) into one place. No community template we found packages all of these together: see the checklist below the block for what to also configure outside `CLAUDE.md` itself.

## Why this exists

The official docs describe roughly a dozen separate cost levers, spread across the costs page, the sub-agents page, and the skills page. Every third-party repo we surveyed implements one or two of these (a router, *or* a statusline, *or* a hook): none packages the full set as one drop-in reference. This is that reference.

## The copy-paste block

Paste this into `CLAUDE.md` at your project root. It's deliberately short: the docs recommend keeping `CLAUDE.md` under ~200 lines total, so this section should be a fraction of that, not the whole file.

```markdown
# Compact instructions

When you compact, keep test output, code diffs, and open TODOs. Drop exploratory
tool-call transcripts and superseded plans.

# Cost discipline

- Match the model to the task: reserve Opus/the frontier tier for architecture and judgment
  calls; default routine implementation to Sonnet or Haiku. Set it per subagent, not by asking
  mid-task.
- Delegate verbose operations (test runs, doc fetches, log parsing) to a subagent so only the
  summary returns to the main conversation.
- Prefer CLI tools (`gh`, `aws`, `gcloud`) over MCP servers when both exist: CLI tools add no
  per-tool-listing cost. Run `/mcp` to disable MCP servers you're not actively using.
- Keep this file under 200 lines. Move workflow-specific, multi-step procedures into
  `.claude/skills/` instead: skills load on demand, this file loads every session.
```

## Set these outside `CLAUDE.md` (still part of the same knob set)

These aren't `CLAUDE.md` content: they're commands, env vars, and settings.json keys. Listed here because the docs treat them as one cost-management surface.

- **`/usage`**: session cost block (per-model token/cache breakdown). Resets on `/clear`.
- **`/model`** (mid-session) or **`/config`** (session default): pick the model tier. Per-subagent override goes in the subagent's own frontmatter: `model: haiku` (or `sonnet` / `opus` / `inherit`); see [sub-agents docs](https://code.claude.com/docs/en/sub-agents#choose-a-model).
- **`/effort`** or the effort field in `/model`: lower reasoning effort for simple tasks. On a model with a *fixed* thinking budget (not adaptive-reasoning), set `MAX_THINKING_TOKENS=8000` (or `=0` to disable) as an env var. Fable 5 cannot have thinking turned off, on either lever.
- **`/context`**: see what's actually consuming your context window before guessing at cuts.
- **A `PreToolUse` hook on `Bash`**: the docs' own worked example filters `npm test`/`pytest`/`go test` output down to `FAIL|ERROR` lines before Claude reads it, instead of reading a 10,000-line log. Wire it in `settings.json`:

  ```json
  {
    "hooks": {
      "PreToolUse": [
        {
          "matcher": "Bash",
          "hooks": [
            { "type": "command", "command": "~/.claude/hooks/filter-test-output.sh" }
          ]
        }
      ]
    }
  }
  ```

- **Agent teams cost warning**: `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1` (env or `settings.json`) turns on agent teams, but the docs state plainly: teams burn **~7x** the tokens of a standard session when teammates run in plan mode, because each teammate is a separate Claude instance with its own context window. Keep teams small and self-contained, or don't turn this on.
- **LLM gateway (enterprise)**: if you need per-key spend tracking on Bedrock/Vertex/Foundry, Anthropic's own docs name [LiteLLM](https://docs.litellm.ai/docs/proxy/virtual_keys) as the pattern several large enterprises use, with the explicit caveat, verbatim: *"This project is unaffiliated with Anthropic and has not been audited for security."* Don't adopt it as a black box.

## What we left out

`advisorModel`, `availableModels`, `fallbackModel`, and the rest of the model-tiering `settings.json` keys are covered separately in [`settings-model-routing.md`](settings-model-routing.md): they encode a *policy*, which deserved its own file rather than a bullet here.
