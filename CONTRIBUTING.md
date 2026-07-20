# Contributing

Thanks for your interest in improving this list.

## What qualifies an entry

Entries here are not ranked by star count, download numbers, or popularity. Each one needs a
primary source, a dated `verified_on` check, and independent corroboration for high-stakes claims.
If a claim can't be traced to a primary source or reproducible evidence, it doesn't belong here,
or it's labeled an unconfirmed/single-source claim rather than presented as fact.

This means a well-known project with lots of stars but no verifiable cost/performance evidence
behind its inclusion may be left out, while a smaller, less-known tool with solid, checkable
evidence gets in.

## Entry format

List entries follow one repeating shape:

```
- [Name](url) - one-liner.
```

Keep the one-liner factual and specific: what it does and why it's here, not marketing copy.

## Cross-references

Every internal cross-reference is a plain relative markdown link. No wikilinks:

```
[Title](path/to/file.md)
```

## Submitting a change

1. Open a PR with the entry or edit.
2. Include the primary source (URL) and, for cost/performance claims, the date the number was
   verified.
3. Expect an editorial pass: we may tighten wording or ask for a stronger source before merging.

## Freshness

Entries carry a `verified_on` date. CI flags entries that haven't been re-verified within our
staleness thresholds (see `.github/workflows/staleness.yml`). A stale flag isn't necessarily
wrong. It's a prompt to re-check.
