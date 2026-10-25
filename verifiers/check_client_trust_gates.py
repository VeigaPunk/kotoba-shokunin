#!/usr/bin/env python3
"""check_client_trust_gates.py — C1 counter for kotoba round 68.

Contract
--------
`python3 -B verifiers/check_client_trust_gates.py --rev <full-sha>` prints
    client trust gates backed N of 5
and exits 0 when N == 5, nonzero otherwise.  At the pinned base it must print
`client trust gates backed 0 of 5` and exit 1.

Classification (the r67 lesson, applied from the start — routed defect R67-1):
a MISSING ENTRY is a content verdict (`0 of 5`, exit 1); a genuinely unreadable
ENVIRONMENT (unknown revision, unreadable repository) is exit 2.  The round-67
counter classified a missing entry as an environment error, so its base line was
never observable; this counter does not repeat that.

What the counter reads (content, not names — QUALITY Q25/Q26).  For
`corpus/knowledge/client-trust-gates-round68.md` at the measured revision:

  1. the entry file exists;
  2. it opens with `source:` lines naming the five `S###` ids;
  3. every cited id resolves to a row in `corpus/SOURCES.md` whose `status` is `mined`;
  4. each cited row's `source` cell occurs verbatim in the entry's `source:` line for that id;
  5. the entry carries a `verified-at: 2026-10-24` line and a `recheck:` line;
  6. for each cited id, the entry carries a double-quoted located quote of at most 25 words
     that also occurs in that row's `anchor` cell;
  7. each cited id has a row in the entry's per-client table whose client cell is filled and
     whose quoted cell carries that located quote;
  8. the entry is indexed in `corpus/README.md`'s coverage map.

`--fetch` additionally re-opens each cited URL and confirms the located quote is present on the
live page; a fetch failure is never counted as a found quote.

Trust boundary (QUALITY Q33): the counter runs the measured revision's own bytes, so a
revision that rewrites the instrument can change the verdict.  The claim's verdict therefore
also cites the controls outside this counter: the base control prints `0 of 5`, the junk-entry
control is rejected, the mutation battery kills each conjunct, and the `--fetch` arm measures
the live pages.

Exit codes: 0 all five backed · 1 not all backed · 2 usage/environment error.
"""
from __future__ import annotations

import argparse
import re
import subprocess
import sys
import tempfile
import urllib.error
import urllib.request
from pathlib import Path

ENTRY = "corpus/knowledge/client-trust-gates-round68.md"
SOURCES = "corpus/SOURCES.md"
README = "corpus/README.md"
VERIFIED_AT = "2026-10-24"
TOTAL = 5

ROW_RE = re.compile(r"^\|(.*)$")
SOURCE_LINE_RE = re.compile(r"^source:\s*(S\d{3,})\s*(.*)$")
QUOTED_RE = re.compile(r'"([^"\n]{1,300})"')
URL_RE = re.compile(r"https?://[^\s,;)\]]+")


class EnvError(Exception):
    pass


def _git_show(repo: Path, rev: str, path: str) -> str | None:
    proc = subprocess.run(
        ["git", "-C", str(repo), "show", f"{rev}:{path}"],
        capture_output=True, text=True,
    )
    if proc.returncode != 0:
        return None
    return proc.stdout


def _materialize(repo: Path, rev: str, dest: Path) -> Path:
    """Write the three measured files of <rev> into <dest> (same relative layout)."""
    for path in (ENTRY, SOURCES, README):
        text = _git_show(repo, rev, path)
        if text is None:
            raise EnvError(f"cannot read {path} at {rev}")
        out = dest / path
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(text, encoding="utf-8")
    return dest


def _norm(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()


def _split_row(body: str) -> list[str]:
    cells = body.split("|")
    if cells and cells[0].strip() == "":
        cells = cells[1:]
    if cells and cells[-1].strip() == "":
        cells = cells[:-1]
    return [c.strip() for c in cells]


def _source_rows(text: str) -> dict[str, list[str]]:
    rows: dict[str, list[str]] = {}
    for line in text.splitlines():
        m = ROW_RE.match(line)
        if not m:
            continue
        cells = [c.strip() for c in m.group(1).split("|")]
        if cells and cells[-1] == "":
            cells.pop()
        if len(cells) != 11:
            continue
        if not re.fullmatch(r"S\d{3,}", cells[0]):
            continue
        rows[cells[0]] = cells
    return rows


def _entry_source_lines(text: str) -> dict[str, str]:
    out: dict[str, str] = {}
    for line in text.splitlines():
        m = SOURCE_LINE_RE.match(line.strip())
        if m:
            out[m.group(1)] = m.group(2)
    return out


def _quoted(text: str) -> list[str]:
    out = []
    for q in QUOTED_RE.findall(text):
        if 0 < len(q.split()) <= 25:
            out.append(q)
    return out


def _table_rows(text: str) -> list[list[str]]:
    rows = []
    for line in text.splitlines():
        if not line.startswith("|"):
            continue
        cells = _split_row(line[1:])
        if not cells or all(set(c) <= set("-: ") for c in cells):
            continue
        rows.append(cells)
    return rows


def _indexed(readme: str) -> bool:
    needle = f"`knowledge/{Path(ENTRY).name}`"
    for line in readme.splitlines():
        if not line.startswith("|"):
            continue
        cells = _split_row(line[1:])
        if len(cells) >= 2 and cells[1].strip() == needle:
            return True
    return False


def check(root: Path) -> tuple[int, list[str]]:
    """Return (backed_count, findings). backed_count is 0..TOTAL."""
    findings: list[str] = []
    entry_path = root / ENTRY
    if not entry_path.is_file():
        # A missing entry is a CONTENT verdict, not an environment error.
        return 0, ["entry missing: " + ENTRY]
    entry = entry_path.read_text(encoding="utf-8")
    sources_path = root / SOURCES
    readme_path = root / README
    if not sources_path.is_file() or not readme_path.is_file():
        raise EnvError(f"cannot read {SOURCES} or {README} at the measured revision")
    sources_text = sources_path.read_text(encoding="utf-8")
    readme_text = readme_path.read_text(encoding="utf-8")

    src_lines = _entry_source_lines(entry)
    if not src_lines:
        return 0, ["no `source:` line naming an S### id"]
    ids = list(src_lines)
    if len(set(ids)) != len(ids):
        return 0, ["duplicate id in the entry's source lines"]
    if len(ids) != TOTAL:
        findings.append(f"the entry names {len(ids)} ids, expected {TOTAL}")

    rows = _source_rows(sources_text)
    quotes = _quoted(_norm(entry))
    table = _table_rows(entry)

    backed = 0
    for sid in ids:
        row = rows.get(sid)
        if row is None:
            findings.append(f"{sid}: no row in {SOURCES}")
            continue
        if len(row) < 11:
            findings.append(f"{sid}: row has {len(row)} cells, expected 11")
            continue
        if row[7] != "mined":
            findings.append(f"{sid}: status is {row[7]!r}, expected 'mined'")
            continue
        if row[1] not in src_lines[sid]:
            findings.append(f"{sid}: the row's source cell is not in the entry's source line")
            continue
        anchor = _norm(row[5])
        matched = [q for q in quotes if _norm(q) in anchor]
        if not matched:
            findings.append(f"{sid}: no located quote of the entry occurs in the row's anchor cell")
            continue
        quote = _norm(matched[0])
        table_row = None
        for cells in table:
            if any(c.strip() == sid for c in cells):
                table_row = cells
                break
        if table_row is None:
            findings.append(f"{sid}: no per-client table row names this id")
            continue
        if len(table_row) < 3 or not table_row[0].strip():
            findings.append(f"{sid}: the per-client table row has no client cell")
            continue
        if quote not in _norm(" ".join(table_row)):
            findings.append(f"{sid}: the per-client table row does not carry the located quote")
            continue
        backed += 1

    if not any(line.strip() == f"verified-at: {VERIFIED_AT}" for line in entry.splitlines()):
        findings.append(f"no `verified-at: {VERIFIED_AT}` line")
    if not any(line.strip().startswith("recheck:") for line in entry.splitlines()):
        findings.append("no `recheck:` line")
    if not _indexed(readme_text):
        findings.append("the entry has no coverage-map index row in " + README)

    if findings:
        return backed, findings
    return backed, []


def fetch(root: Path) -> tuple[int, list[str]]:
    """Re-open each cited URL and confirm its located quote is on the live page."""
    results: list[str] = []
    entry = (root / ENTRY).read_text(encoding="utf-8")
    rows = _source_rows((root / SOURCES).read_text(encoding="utf-8"))
    src_lines = _entry_source_lines(entry)
    quotes = _quoted(_norm(entry))
    found = 0
    for sid, line in src_lines.items():
        row = rows.get(sid)
        if row is None:
            results.append(f"{sid}: NO ROW")
            continue
        anchor = _norm(row[5])
        quote = next((_norm(q) for q in quotes if _norm(q) in anchor), None)
        if quote is None:
            results.append(f"{sid}: NO LOCATED QUOTE")
            continue
        m = URL_RE.search(line) or URL_RE.search(row[1])
        if not m:
            results.append(f"{sid}: NO URL")
            continue
        url = m.group(0)
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "kotoba-lane-check/1.0"})
            with urllib.request.urlopen(req, timeout=30) as resp:
                body = resp.read().decode("utf-8", errors="replace")
        except (urllib.error.URLError, OSError, ValueError) as exc:
            results.append(f"{sid}: FETCH FAILED {exc}")
            continue
        if quote in _norm(body):
            found += 1
            results.append(f"{sid}: found")
        else:
            results.append(f"{sid}: NOT FOUND")
    return found, results


def _world(root: Path, *, entry: str | None = None, sources: str | None = None,
           readme: str | None = None, drop_entry: bool = False) -> Path:
    dest = Path(tempfile.mkdtemp(prefix="k68-world-"))
    for path in (ENTRY, SOURCES, README):
        src = root / path
        out = dest / path
        out.parent.mkdir(parents=True, exist_ok=True)
        if src.is_file():
            out.write_text(src.read_text(encoding="utf-8"), encoding="utf-8")
    if drop_entry:
        (dest / ENTRY).unlink()
    if entry is not None:
        (dest / ENTRY).write_text(entry, encoding="utf-8")
    if sources is not None:
        (dest / SOURCES).write_text(sources, encoding="utf-8")
    if readme is not None:
        (dest / README).write_text(readme, encoding="utf-8")
    return dest


def selftest(repo: Path) -> int:
    failures = 0
    base = repo
    if not (base / ENTRY).is_file():
        print("selftest setup failed: the entry is not present in the working tree", file=sys.stderr)
        return 2
    entry_text = (base / ENTRY).read_text(encoding="utf-8")
    sources_text = (base / SOURCES).read_text(encoding="utf-8")
    readme_text = (base / README).read_text(encoding="utf-8")

    n, findings = check(base)
    if n != TOTAL or findings:
        print(f"FAIL honest world: backed {n} of {TOTAL}; {findings}", file=sys.stderr)
        failures += 1
    else:
        print(f"PASS honest world: backed {TOTAL} of {TOTAL}")

    worlds = {
        "entry missing": _world(base, drop_entry=True),
        "no source line": _world(base, entry="\n".join(
            l for l in entry_text.splitlines() if not l.startswith("source:"))),
        "id does not resolve": _world(base, entry=entry_text.replace("S198", "S998")),
        "row not mined": _world(base, sources="\n".join(
            (l.replace("| mined |", "| queued |", 1) if l.startswith("| S198 |") else l)
            for l in sources_text.splitlines())),
        "source cell absent from the entry": _world(base, entry=entry_text.replace(
            "VT Code — SKILLS_GUIDE.md — https://raw.githubusercontent.com/vinhnx/vtcode/main/docs/skills/SKILLS_GUIDE.md",
            "VT Code — https://raw.githubusercontent.com/vinhnx/vtcode/main/docs/skills/SKILLS_GUIDE.md")),
        "no verified-at": _world(base, entry=entry_text.replace(
            f"verified-at: {VERIFIED_AT}", "verified-at: 2020-01-01")),
        "no recheck": _world(base, entry=entry_text.replace(
            "recheck: 90d — re-fetch", "note: re-fetch")),
        "no coverage-map row": _world(base, readme=readme_text.replace(
            "`knowledge/client-trust-gates-round68.md`", "`knowledge/absent.md`")),
        "quote not in the anchor cell": _world(base, sources=sources_text.replace(
            "Skill content is untrusted resource data; host tool and sandbox policy remains authoritative.",
            "A different sentence entirely.")),
        "table row loses the quote": _world(base, entry=entry_text.replace(
            '"Skill content is untrusted resource data; host tool and sandbox policy remains authoritative." | S198',
            '"nothing here" | S198')),
    }
    for name, world in worlds.items():
        n, findings = check(world)
        if n == TOTAL:
            print(f"FAIL broken world survived: {name} -> backed {n}", file=sys.stderr)
            failures += 1
        else:
            print(f"PASS broken world rejected: {name}")

    # The r67 lesson: a missing entry is a CONTENT verdict (exit 1), not an env error (exit 2).
    missing = _world(base, drop_entry=True)
    n, findings = check(missing)
    if n != 0:
        print(f"FAIL missing-entry classification: backed {n}, expected 0", file=sys.stderr)
        failures += 1
    else:
        print("PASS missing-entry classification: backed 0 (content verdict)")
    print(f"self-test: {failures} failure(s) over {len(worlds) + 2} assertions")
    return 1 if failures else 0


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(add_help=True)
    ap.add_argument("--rev", default=None, help="measured revision (full sha)")
    ap.add_argument("--repo", default=str(Path(__file__).resolve().parent.parent))
    ap.add_argument("--fetch", action="store_true", help="re-open each cited URL and check the quote")
    ap.add_argument("--self-test", action="store_true")
    args = ap.parse_args(argv)
    repo = Path(args.repo)
    if args.self_test:
        return selftest(repo)
    try:
        if args.rev:
            with tempfile.TemporaryDirectory(prefix="k68-rev-") as tmp:
                root = _materialize(repo, args.rev, Path(tmp))
                n, findings = check(root)
                if args.fetch:
                    found, results = fetch(root)
        else:
            n, findings = check(repo)
            if args.fetch:
                found, results = fetch(repo)
    except EnvError as exc:
        print(f"environment error: {exc}", file=sys.stderr)
        return 2
    print(f"client trust gates backed {n} of {TOTAL}")
    for f in findings:
        print(f"  - {f}")
    if args.fetch:
        for r in results:
            print(f"  fetch {r}")
        print(f"live quotes found {found} of {TOTAL}")
    return 0 if n == TOTAL else 1


if __name__ == "__main__":
    sys.exit(main())
