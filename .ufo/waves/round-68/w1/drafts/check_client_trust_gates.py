#!/usr/bin/env python3
"""check_client_trust_gates.py — C1 counter for kotoba round 68 (draft: `--fetch` arm).

Seat: ExecC1Fetch (round-68 wave 1).  This draft is self-contained.  The `check()`
core mirrors the semantics of the L1-installed `verifiers/check_client_trust_gates.py`
(the frozen 8-conjunct contract); this seat's assigned move is the `--fetch` arm plus
one honesty fix on the exit-2 path (an unknown revision now says so, instead of being
reported as an unreadable SOURCES.md).

Contract
--------
`python3 -B check_client_trust_gates.py --rev <full-sha>` prints
    client trust gates backed N of 5
and exits 0 when N == 5, nonzero otherwise.  At the pinned base it must print
`client trust gates backed 0 of 5` and exit 1.

Classification (the r67 lesson, applied from the start — routed defect R67-1):
a MISSING ENTRY is a content verdict (`0 of 5`, exit 1); a genuinely unreadable
ENVIRONMENT (unknown revision, unreadable repository) is exit 2.

The `--fetch` arm (this seat)
-----------------------------
`--fetch` additionally re-opens each cited URL and confirms the entry's located
quote is present on the live page.  For each cited row it reads the row's `source`
cell, extracts the URL, fetches it with `curl -sSL --max-time 30` (falling back to
`urllib` only if curl is unavailable), and searches the fetched text for the
located quote after whitespace normalization (HTML pages are reduced to their
visible text first, so tag-interleaved sentences are still searchable).

It prints one line per cited client:

    S### <client>: found
    S### <client>: NOT FOUND
    S### <client>: FETCH FAILED <single-line error>

then `live quotes found N of 5`.  A fetch failure is NEVER counted as a found
quote and NEVER crashes the counter; the fetch lines are a printed measurement.
Exit codes: 0/1 still mirror the content verdict (`0` iff all five are backed),
because the frozen `--rev` predicate is `exit 0 when N == 5`; exit 2 is reserved
for a usage/environment error of the counter itself (bad usage, unknown revision,
unreadable repository).  When the entry (or the registry) is absent, `--fetch`
prints `live quotes found 0 of 5` with a stderr note — it does not traceback.

Trust boundary (QUALITY Q33): the counter runs the measured revision's own bytes, so a
revision that rewrites the instrument can change the verdict.  The claim's verdict therefore
also cites the controls outside this counter: the base control prints `0 of 5`, the junk-entry
control is rejected, the mutation battery kills each conjunct, and the `--fetch` arm measures
the live pages.
"""
from __future__ import annotations

import argparse
import html as html_mod
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
CURL = ["curl", "-sSL", "--max-time", "30"]

ROW_RE = re.compile(r"^\|(.*)$")
SOURCE_LINE_RE = re.compile(r"^source:\s*(S\d{3,})\s*(.*)$")
QUOTED_RE = re.compile(r'"([^"\n]{1,300})"')
URL_RE = re.compile(r"https?://[^\s,;)\]]+")
LOCATED_RE = re.compile(r'located quote\s+"([^"\n]+)"')
HTML_RE = re.compile(
    r"<!doctype\s+html|<html[\s>]|<body[\s>]|<div[\s>]|<p[\s>]|<script[\s>]|<table[\s>]",
    re.I,
)


class EnvError(Exception):
    pass


class FetchError(Exception):
    pass


def _norm(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()


def _tail(text: str, limit: int = 160) -> str:
    return _norm(text or "")[:limit] or "no output"


def _git_show(repo: Path, rev: str, path: str) -> str | None:
    proc = subprocess.run(
        ["git", "-C", str(repo), "show", f"{rev}:{path}"],
        capture_output=True, text=True,
    )
    if proc.returncode != 0:
        return None
    return proc.stdout


def _verify_rev(repo: Path, rev: str) -> None:
    """An unknown revision is an environment error with an honest message (exit 2)."""
    proc = subprocess.run(
        ["git", "-C", str(repo), "rev-parse", "--verify", f"{rev}^{{commit}}"],
        capture_output=True, text=True,
    )
    if proc.returncode != 0:
        raise EnvError(f"unknown revision {rev}: {_tail(proc.stderr, 120)}")


def _materialize(repo: Path, rev: str, dest: Path) -> Path:
    """Write the three measured files of <rev> into <dest> (same relative layout).

    A revision that does not carry the ENTRY is materialized WITHOUT it: a missing entry is a
    content verdict (`0 of 5`, exit 1), not an environment error (exit 2).  The r67 counter
    classified it the other way round, which is why its base line was never observable
    (routed defect R67-1); this counter does not repeat that.
    """
    _verify_rev(repo, rev)
    for path in (ENTRY, SOURCES, README):
        text = _git_show(repo, rev, path)
        if text is None:
            if path == ENTRY:
                continue
            raise EnvError(f"cannot read {path} at {rev}")
        out = dest / path
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(text, encoding="utf-8")
    return dest


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
        quote = _norm(max(matched, key=len))
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

    global_findings: list[str] = []
    if not any(line.strip() == f"verified-at: {VERIFIED_AT}" for line in entry.splitlines()):
        global_findings.append(f"no `verified-at: {VERIFIED_AT}` line")
    if not any(line.strip().startswith("recheck:") for line in entry.splitlines()):
        global_findings.append("no `recheck:` line")
    if not _indexed(readme_text):
        global_findings.append("the entry has no coverage-map index row in " + README)

    if global_findings or findings:
        return 0, global_findings + findings
    return backed, []


# --------------------------------------------------------------------------
# The --fetch arm (seat ExecC1Fetch, round-68 wave 1)
# --------------------------------------------------------------------------

def _http_get(url: str) -> str:
    """Fetch <url> with `curl -sSL --max-time 30`; fall back to urllib without curl.

    Raises FetchError (curl failure), subprocess.TimeoutExpired or an urllib/OSError
    on failure; returns the body text on success.
    """
    try:
        proc = subprocess.run(CURL + [url], capture_output=True, text=True, timeout=40)
    except FileNotFoundError:
        # curl unavailable on this host — the contract's stated fallback.
        req = urllib.request.Request(url, headers={"User-Agent": "kotoba-lane-check/1.0"})
        with urllib.request.urlopen(req, timeout=30) as resp:
            return resp.read().decode("utf-8", errors="replace")
    if proc.returncode != 0:
        raise FetchError(f"curl exit {proc.returncode}: {_tail(proc.stderr)}")
    return proc.stdout


def _visible(body: str) -> str:
    """Whitespace-normalized searchable text; HTML is reduced to its visible text.

    Reducing HTML to visible text is measurement fidelity, not leniency: the quote's
    words must still occur, in order, in what the page actually shows.
    """
    if HTML_RE.search(body[:8192]):
        text = re.sub(r"(?is)<(script|style)\b.*?</\1\s*>", " ", body)
        text = re.sub(r"(?s)<[^>]*>", " ", text)
        text = html_mod.unescape(text)
        return _norm(text)
    return _norm(body)


def _client_name(row: list[str]) -> str:
    """The row's client name: the first ` — ` field of its `source` cell."""
    cell = row[1] if len(row) > 1 else ""
    name = cell.split(" — ")[0].strip()
    if not name:
        name = "(no client cell)"
    return name if len(name) <= 48 else name[:47] + "…"


def _located_quote(line: str, quotes: list[str], anchor: str) -> str | None:
    """The entry's located quote for this id.

    Prefer the span after the explicit `located quote` marker (the entry's own
    convention); fall back to the longest entry quote that occurs in the row's
    anchor cell (the same match `check()` accepts).
    """
    m = LOCATED_RE.search(line)
    if m:
        return _norm(m.group(1))
    matched = [q for q in quotes if _norm(q) in anchor]
    if matched:
        return _norm(max(matched, key=len))
    return None


def fetch(root: Path) -> tuple[int, list[str]]:
    """Re-open each cited URL and confirm its located quote is on the live page.

    One line per cited client: `S### <client>: found` / `NOT FOUND` /
    `FETCH FAILED <error>`.  A fetch failure is never counted as a found quote and
    never crashes the counter.
    """
    results: list[str] = []
    entry_path = root / ENTRY
    sources_path = root / SOURCES
    if not entry_path.is_file():
        print(f"fetch: no cited rows — {ENTRY} is absent; fetched nothing", file=sys.stderr)
        return 0, results
    if not sources_path.is_file():
        print(f"fetch: cited ids cannot resolve — {SOURCES} is absent; fetched nothing",
              file=sys.stderr)
        return 0, results
    entry = entry_path.read_text(encoding="utf-8")
    rows = _source_rows(sources_path.read_text(encoding="utf-8"))
    src_lines = _entry_source_lines(entry)
    quotes = _quoted(_norm(entry))
    found = 0
    for sid, line in src_lines.items():
        row = rows.get(sid)
        if row is None:
            results.append(f"{sid}: NO ROW")
            continue
        client = _client_name(row)
        anchor = _norm(row[5]) if len(row) > 5 else ""
        quote = _located_quote(line, quotes, anchor)
        if quote is None:
            results.append(f"{sid} {client}: NO LOCATED QUOTE")
            continue
        m = URL_RE.search(line) or (URL_RE.search(row[1]) if len(row) > 1 else None)
        if not m:
            results.append(f"{sid} {client}: NO URL")
            continue
        url = m.group(0)
        try:
            body = _http_get(url)
        except (FetchError, subprocess.TimeoutExpired, urllib.error.URLError,
                OSError, ValueError) as exc:
            message = _tail(str(exc) or type(exc).__name__)
            results.append(f"{sid} {client}: FETCH FAILED {message}")
            continue
        if quote in _visible(body):
            found += 1
            results.append(f"{sid} {client}: found")
        else:
            results.append(f"{sid} {client}: NOT FOUND")
    return found, results


# --------------------------------------------------------------------------
# Self-test (offline; drives the public check() path — the counter-test seat's arm)
# --------------------------------------------------------------------------

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


def _default_repo() -> str:
    """The lane root: the nearest ancestor of this file holding corpus/SOURCES.md.

    Works both at the draft location (.ufo/waves/round-68/w1/drafts/) and at the
    installed location (verifiers/).
    """
    for anc in Path(__file__).resolve().parents:
        if (anc / "corpus" / "SOURCES.md").is_file():
            return str(anc)
    return str(Path.cwd())


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(add_help=True)
    ap.add_argument("--rev", default=None, help="measured revision (full sha)")
    ap.add_argument("--repo", default=_default_repo())
    ap.add_argument("--fetch", action="store_true",
                    help="re-open each cited URL and check the located quote on the live page")
    ap.add_argument("--self-test", action="store_true")
    args = ap.parse_args(argv)
    repo = Path(args.repo)
    if args.self_test:
        return selftest(repo)
    found: int | None = None
    results: list[str] = []
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
            print(r)
        print(f"live quotes found {found} of {TOTAL}")
    return 0 if n == TOTAL else 1


if __name__ == "__main__":
    sys.exit(main())
