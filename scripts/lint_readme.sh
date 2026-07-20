#!/usr/bin/env bash
# README lint with an explicit waiver list.
#
# We run awesome-lint but tolerate exactly two rules, deliberately:
#   - awesome-list-item: our entries end with compact status markers
#     (`tool · MIT` `✓ 2026-07`) AFTER the final period: the verification
#     dating is this list's core differentiator, and the rule has no
#     concept of trailing markers. (awesome-rust's trailing badges fail
#     this same rule.)
#   - (none other currently)
# Everything else (structure, ToC mismatches, duplicate links, dead
# syntax) still fails the build.
set -uo pipefail

WAIVED='remark-lint:awesome-list-item'

out="$(npx --yes awesome-lint 2>&1)" || true
errors="$(printf '%s\n' "$out" | grep '✖' | grep -v 'Linting' | grep -vE "$WAIVED" || true)"

if [ -n "$errors" ]; then
  printf '%s\n' "$out" | grep -vE "$WAIVED"
  echo
  echo "lint_readme: FAIL (non-waived errors above)"
  exit 1
fi

waived_count="$(printf '%s\n' "$out" | grep -cE "$WAIVED" || true)"

# Em-dash ban (2026-07-20): the character reads as AI-generated style and is
# banned in all tracked markdown. Sole exception: verbatim quotations, listed
# in scripts/emdash-allowlist.txt (one exact substring per line); altering a
# quote's own punctuation would falsify the citation.
dash_hits="$(git grep -n -- '—' -- '*.md' 2>/dev/null || true)"
if [ -n "$dash_hits" ] && [ -f scripts/emdash-allowlist.txt ]; then
  dash_hits="$(printf '%s\n' "$dash_hits" | grep -vFf <(grep -v '^#' scripts/emdash-allowlist.txt | grep -v '^$') || true)"
fi
if [ -n "$dash_hits" ]; then
  printf '%s\n' "$dash_hits"
  echo
  echo "lint_readme: FAIL (em-dash found in tracked markdown; rewrite or allowlist a verbatim quote)"
  exit 1
fi

echo "lint_readme: OK (${waived_count} waived awesome-list-item marker-format notices; no em-dashes)"
