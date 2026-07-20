#!/usr/bin/env python3
"""Staleness check over research/manifest.json's exported verification dates.

Thresholds (awesome-selfhosted's citable defaults, keyed on `verified_on` not stars):
  - WARN  when more than 186 days have passed since `verified_on`.
  - ERROR when more than 365 days have passed since `verified_on`, OR the entry
    is past its own `stale_after` date.

An entry whose title appears in the allowlist (scripts/staleness-allowlist.txt)
is "done, not dead" — any ERROR for that entry is downgraded to WARN. Exit code
is 1 only if a non-allowlisted ERROR remains.
"""

import argparse
import datetime
import json
import sys
from pathlib import Path

WARN_DAYS = 186
ERROR_DAYS = 365

SCRIPT_DIR = Path(__file__).resolve().parent
DEFAULT_MANIFEST = SCRIPT_DIR.parent / "research" / "manifest.json"
DEFAULT_ALLOWLIST = SCRIPT_DIR / "staleness-allowlist.txt"


def parse_date(value: str) -> datetime.date:
    return datetime.datetime.strptime(value, "%Y-%m-%d").date()


def load_allowlist(path: Path) -> set:
    if not path.exists():
        return set()
    titles = set()
    for line in path.read_text().splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        titles.add(line)
    return titles


def classify(entry: dict, today: datetime.date, allowlist: set):
    verified_on = parse_date(entry["verified_on"])
    stale_after = parse_date(entry["stale_after"]) if entry.get("stale_after") else None
    days_since = (today - verified_on).days

    severity = "OK"
    reasons = []

    if days_since > ERROR_DAYS:
        severity = "ERROR"
        reasons.append(f"{days_since}d since verified_on (> {ERROR_DAYS}d hard limit)")
    elif days_since > WARN_DAYS:
        severity = "WARN"
        reasons.append(f"{days_since}d since verified_on (> {WARN_DAYS}d warn threshold)")

    if stale_after and today > stale_after:
        severity = "ERROR"
        reasons.append(f"past stale_after ({entry['stale_after']})")

    allowlisted = entry.get("title") in allowlist
    if severity == "ERROR" and allowlisted:
        severity = "WARN"
        reasons.append("allowlisted: downgraded from ERROR")

    return severity, days_since, reasons


def format_table(rows) -> str:
    if not rows:
        return "(nothing to report)"
    headers = ["STATUS", "TITLE", "SUPER_AREA", "DAYS", "REASON"]
    widths = [len(h) for h in headers]
    for row in rows:
        for i, cell in enumerate(row):
            widths[i] = max(widths[i], len(cell))
    lines = []
    lines.append("  ".join(h.ljust(widths[i]) for i, h in enumerate(headers)))
    lines.append("  ".join("-" * w for w in widths))
    for row in rows:
        lines.append("  ".join(cell.ljust(widths[i]) for i, cell in enumerate(row)))
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--manifest",
        type=Path,
        default=DEFAULT_MANIFEST,
        help=f"path to manifest.json (default: {DEFAULT_MANIFEST})",
    )
    parser.add_argument(
        "--allowlist",
        type=Path,
        default=DEFAULT_ALLOWLIST,
        help=f"path to allowlist file (default: {DEFAULT_ALLOWLIST})",
    )
    args = parser.parse_args()

    manifest_path: Path = args.manifest
    if not manifest_path.exists():
        print(f"ERROR: manifest not found at {manifest_path}", file=sys.stderr)
        return 1

    entries = json.loads(manifest_path.read_text())
    allowlist = load_allowlist(args.allowlist)
    today = datetime.date.today()

    ok_count = 0
    warn_count = 0
    error_count = 0
    table_rows = []

    for entry in sorted(entries, key=lambda e: e.get("title", "")):
        severity, days_since, reasons = classify(entry, today, allowlist)
        if severity == "OK":
            ok_count += 1
            continue
        if severity == "WARN":
            warn_count += 1
        elif severity == "ERROR":
            error_count += 1
        table_rows.append(
            (
                severity,
                entry.get("title", "<untitled>"),
                entry.get("super_area", ""),
                str(days_since),
                "; ".join(reasons),
            )
        )

    print(f"Staleness check — {len(entries)} entries, run on {today.isoformat()}")
    print()
    print(format_table(table_rows))
    print()
    print(f"Summary: {ok_count} OK, {warn_count} WARN, {error_count} ERROR")

    return 1 if error_count > 0 else 0


if __name__ == "__main__":
    sys.exit(main())
