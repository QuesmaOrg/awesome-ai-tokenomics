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

## Self-submissions

You may submit your own project. Additional rules apply:

- Disclose it in the PR body.
- Every claim in the one-liner must be checkable against a public primary source: the code, live
  docs, or a published pricing table. A claim only a hosted backend can confirm is worded as
  vendor-reported or left out.
- The kind badge must match where the features live. An OSS license badge means the listed
  features exist in that repository's code; features served by a hosted backend take the `co`
  badge.
- Adoption is not required, but the project must be inspectable: working code or a live service,
  not a landing page.
- Near-identical submissions sent to many lists at once are declined.

## Freshness

Entries carry a `verified_on` date. CI flags entries that haven't been re-verified within our
staleness thresholds (see `.github/workflows/staleness.yml`). A stale flag isn't necessarily
wrong. It's a prompt to re-check.

Tool entries additionally follow a maintenance rule: a tool whose repository has had no commit
for more than 12 months gets flagged for review and dropped unless there is a stated reason to
keep it (a finished, stable tool can earn an explicit exception). The last-commit badges on the
list are the instrument of this rule, not decoration.
