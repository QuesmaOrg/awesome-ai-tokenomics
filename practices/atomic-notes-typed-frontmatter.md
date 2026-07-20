---
verified_on: 2026-07-03
stale_after: 2026-10-03
sources:
  - https://notes.andymatuschak.org/Evergreen_notes_should_be_atomic
  - https://obsidian.md/help/bases
  - https://github.com/kepano/obsidian-skills
---
# Atomic notes + typed frontmatter (agent-edit safety)

**In a knowledge base that agents co-write: keep one artifact or fact per note, give each note a stable concept-handle title, and validate typed frontmatter in CI: the schema is a machine contract, not decoration.**

An agent told to fix one fact opens a long composite page, edits its paragraph, and quietly reflows two unrelated sections in the same commit: now review has to catch all three. One fact per note keeps that diff small enough to actually read.

- Atomicity bounds the blast radius of an agent edit to one small file with a reviewable diff instead of a silent rewrite of a large composite page. Andy Matuschak: notes should be "only about one thing — but which… capture the entirety of that thing."
- Stable titles act like APIs: "the entire note's ideas can then be referenced using that handle," which is why basename wikilinks need unique titles as the base grows.
- Once agents write frontmatter, every property is load-bearing: Obsidian Bases builds database views directly on note properties, and downstream scripts key off exact field names and types, so a free-styled field silently breaks queries.
- Enum and schema validation in CI turns that silent breakage into a failed commit instead of a silent one.
- The pattern is going platform-level: Obsidian's CEO ships agent skills (obsidian-markdown, obsidian-bases, json-canvas, obsidian-cli) for vaults run through Claude Code, Codex, and Open Code. Agent-operated knowledge bases are the expected case now, not an exotic one.

**How to apply**
- One note per artifact or claim. If a note grows a second H1-level subject, split it.
- Name notes for the thing itself, in kebab-case, and don't rename casually: links are the brain.
- Declare the frontmatter schema once, then validate presence, enum values, and date sanity in a pre-commit hook, with a CI backstop for bypassed commits.
- Auto-regenerate health snapshots (orphans, dangling links, staleness) at commit time, so hygiene metrics never silently rot.

Go deeper: [LLM-legible knowledge base](llm-legible-knowledge-base.md) · [Messy capture, atomized synthesis](messy-capture-atomized-synthesis.md)

## Sources
- Andy Matuschak, "Evergreen notes should be atomic" - https://notes.andymatuschak.org/Evergreen_notes_should_be_atomic
- Obsidian, "Bases" - https://obsidian.md/help/bases (core plugin since 1.9, 2025)
- Steph Ango (Obsidian CEO), obsidian-skills - https://github.com/kepano/obsidian-skills (early 2026)
