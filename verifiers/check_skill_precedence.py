#!/usr/bin/env python3
"""check_skill_precedence.py — C1 counter for kotoba round 69.

Contract
--------
`python3 -B verifiers/check_skill_precedence.py --rev <full-sha>` prints
    measured-rev: <full-sha>
    skill precedence backed N of 5
and exits 0 when N == 5, nonzero otherwise.  At the pinned base
`a5f7459f99bb27bf697e9438362e75ac5833eca8` it must print `skill precedence backed 0 of 5`
and exit 1.

The surface: what five clients (Roo Code, Amp, Deep Code, Junie, opencode) document about a
skill NAME COLLISION — which of two same-named skills wins, or that names must be unique.

Classification (routed defect R67-1, carried by the r68 counter): a MISSING ENTRY is a content
verdict (`0 of 5`, exit 1); a genuinely unreadable ENVIRONMENT (unknown revision, unreadable
repository, a registry or coverage map the revision does not carry) is exit 2.

What the counter reads (content, not names — QUALITY Q25/Q26).  For
`corpus/knowledge/skill-name-precedence-round69.md` at the measured revision:

  1. the entry exists and OPENS with its provenance trio (QUALITY Q12): the first non-blank,
     non-heading lines are the `source:` lines, then `verified-at: 2026-10-25`, then `recheck:`;
  2. the `source:` lines name exactly five distinct `S###` ids;
  3. every cited id resolves to an 11-cell row in `corpus/SOURCES.md` whose `status` is `mined`,
     whose `opened` cell is `2026-10-25`, and whose `used-by` cell names the entry;
  4. each cited row's `source` cell occurs verbatim in the entry's `source:` line for that id;
  5. for each cited id, the entry carries a double-quoted located quote of 5 to 25 words that
     also occurs in that row's `anchor` cell (the longest such quote is the row's quote); a
     shorter span of five words or more is never satisfied by a section title;
  6. each cited id has exactly one row in the entry's per-client table whose client cell is
     filled and is not the id itself, whose rule cell is a sentence of at least six words,
     and whose quote cell carries that located quote;
  7. the five table rows name five distinct clients;
  8. the entry is indexed in `corpus/README.md`'s coverage map.

Any global failure (1, 2, 7, 8) makes the count 0: a partial entry is not partially backed.

`--fetch` re-opens each cited URL and confirms the located quote is on the live page after HTML
tags are dropped and entities unescaped (the documented shaping, QUALITY Q42/Q56); a fetch
failure is never counted as found.

Trust boundary (QUALITY Q33): the counter runs the measured revision's own bytes, so a revision
that rewrites the instrument can change the verdict.  The claim's verdict therefore also cites
the controls outside this counter: the base control, the junk-entry control, the mutation
battery and the `--fetch` arm.

Exit codes: 0 all five backed · 1 not all backed · 2 usage/environment error.
"""
from __future__ import annotations

import argparse
import html
import re
import shutil
import subprocess
import sys
import tempfile
import urllib.error
import urllib.request
from pathlib import Path

ENTRY = "corpus/knowledge/skill-name-precedence-round69.md"
SOURCES = "corpus/SOURCES.md"
README = "corpus/README.md"
VERIFIED_AT = "2026-10-25"
OPENED = "2026-10-25"
TOTAL = 5

SOURCE_LINE_RE = re.compile(r"^source:\s*(S\d{3,})\b\s*(.*)$")
QUOTED_RE = re.compile(r'"([^"\n]{1,400})"')
URL_RE = re.compile(r"https?://[^\s,;)\]|]+")


class EnvError(Exception):
    pass


def _git(repo: Path, *args: str) -> subprocess.CompletedProcess:
    return subprocess.run(["git", "-C", str(repo), *args], capture_output=True, text=True)


def _resolve(repo: Path, rev: str) -> str:
    proc = _git(repo, "rev-parse", "--verify", "--quiet", f"{rev}^{{commit}}")
    if proc.returncode != 0:
        raise EnvError(f"unknown revision {rev}")
    return proc.stdout.strip()


def _materialize(repo: Path, rev: str, dest: Path) -> None:
    for path in (ENTRY, SOURCES, README):
        proc = _git(repo, "show", f"{rev}:{path}")
        if proc.returncode != 0:
            if path == ENTRY:
                continue  # content verdict, not an environment error
            raise EnvError(f"cannot read {path} at {rev}")
        out = dest / path
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(proc.stdout, encoding="utf-8")


def _norm(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()


def _cells(line: str) -> list[str]:
    body = line.strip()
    if not body.startswith("|"):
        return []
    cells = [c.strip() for c in body[1:].split("|")]
    if cells and cells[-1] == "":
        cells.pop()
    return cells


def _source_rows(text: str) -> dict[str, list[str]]:
    rows: dict[str, list[str]] = {}
    for line in text.splitlines():
        if not re.match(r"^ {0,3}\|", line):
            continue
        cells = _cells(line)
        if len(cells) == 11 and re.fullmatch(r"S\d{3,}", cells[0]) and cells[0] not in rows:
            rows[cells[0]] = cells
    return rows


def _provenance(entry: str) -> tuple[dict[str, str], list[str]]:
    """Return ({id: source-line tail}, findings) for the entry's opening provenance trio."""
    lines = [l.strip() for l in entry.splitlines()]
    body = [l for l in lines if l and not l.startswith("#")]
    src: dict[str, str] = {}
    i = 0
    dup = False
    while i < len(body):
        m = SOURCE_LINE_RE.match(body[i])
        if not m:
            break
        if m.group(1) in src:
            dup = True
        src[m.group(1)] = m.group(2)
        i += 1
    findings = []
    if not src:
        findings.append("the entry does not open with `source:` lines naming S### ids")
        return src, findings
    if dup:
        findings.append("duplicate id in the entry's source lines")
    if i >= len(body) or body[i] != f"verified-at: {VERIFIED_AT}":
        findings.append(f"the source lines are not followed by `verified-at: {VERIFIED_AT}`")
    elif i + 1 >= len(body) or not body[i + 1].startswith("recheck:"):
        findings.append("`verified-at:` is not followed by a `recheck:` line")
    if len(src) != TOTAL:
        findings.append(f"the entry names {len(src)} ids, expected {TOTAL}")
    return src, findings


def _quoted(text: str) -> list[str]:
    return [q for q in QUOTED_RE.findall(text) if 5 <= len(q.split()) <= 25]


def _table_rows(entry: str) -> list[list[str]]:
    out = []
    for line in entry.splitlines():
        cells = _cells(line)
        if not cells or all(set(c) <= set("-: ") for c in cells):
            continue
        out.append(cells)
    return out


def _indexed(readme: str) -> bool:
    needle = f"`knowledge/{Path(ENTRY).name}`"
    in_map = False
    for line in readme.splitlines():
        if line.startswith("## "):
            in_map = line.strip() == "## Coverage map"
            continue
        if not in_map:
            continue
        cells = _cells(line)
        if len(cells) >= 2 and cells[1] == needle:
            return True
    return False


def _row_quote(row: list[str], quotes: list[str]) -> str | None:
    anchor = _norm(row[5])
    matched = [_norm(q) for q in quotes if _norm(q) in anchor]
    return max(matched, key=len) if matched else None


def check(root: Path) -> tuple[int, list[str]]:
    entry_path = root / ENTRY
    if not entry_path.is_file():
        return 0, ["entry missing: " + ENTRY]
    if not (root / SOURCES).is_file() or not (root / README).is_file():
        raise EnvError(f"cannot read {SOURCES} or {README} at the measured revision")
    entry = entry_path.read_text(encoding="utf-8")
    rows = _source_rows((root / SOURCES).read_text(encoding="utf-8"))
    readme = (root / README).read_text(encoding="utf-8")

    src, global_findings = _provenance(entry)
    quotes = _quoted(_norm(entry))
    table = _table_rows(entry)
    findings: list[str] = []
    clients: list[str] = []
    backed = 0
    for sid, tail in src.items():
        row = rows.get(sid)
        if row is None:
            findings.append(f"{sid}: no 11-cell row in {SOURCES}")
            continue
        if row[7] != "mined":
            findings.append(f"{sid}: status is {row[7]!r}, expected 'mined'")
            continue
        if row[8] != OPENED:
            findings.append(f"{sid}: opened is {row[8]!r}, expected {OPENED!r}")
            continue
        if ENTRY not in [p.strip() for p in re.split(r"[,;]", row[10])]:
            findings.append(f"{sid}: used-by does not name {ENTRY}")
            continue
        if len(_norm(tail)) < 20 or row[1] not in tail:
            findings.append(f"{sid}: the row's source cell is not in the entry's source line")
            continue
        quote = _row_quote(row, quotes)
        if quote is None:
            findings.append(f"{sid}: no located quote of the entry occurs in the row's anchor cell")
            continue
        named = [c for c in table if sid in c]
        if len(named) != 1:
            findings.append(f"{sid}: {len(named)} per-client table rows name this id, expected 1")
            continue
        cells = named[0]
        if len(cells) < 4 or not cells[0] or not cells[1]:
            findings.append(f"{sid}: the per-client table row lacks a client or rule cell")
            continue
        if re.fullmatch(r"S\d{3,}", cells[0]) or len(_norm(cells[1]).split()) < 6:
            findings.append(f"{sid}: the per-client table row's client or rule cell is a stub")
            continue
        if quote not in _norm(cells[2]):
            findings.append(f"{sid}: the per-client table row does not carry the located quote")
            continue
        clients.append(_norm(cells[0]).lower())
        backed += 1
    if len(set(clients)) != len(clients):
        global_findings.append("two table rows name the same client")
    if not _indexed(readme):
        global_findings.append("the entry has no coverage-map index row in " + README)
    if global_findings or findings:
        return 0, global_findings + findings
    return backed, []


def _page_text(body: str) -> str:
    body = re.sub(r"(?is)<(script|style)\b.*?</\1>", " ", body)
    body = re.sub(r"<[^>]+>", " ", body)
    return _norm(html.unescape(body))


def fetch(root: Path) -> tuple[int, list[str]]:
    entry = (root / ENTRY).read_text(encoding="utf-8")
    rows = _source_rows((root / SOURCES).read_text(encoding="utf-8"))
    src, _ = _provenance(entry)
    quotes = _quoted(_norm(entry))
    found, results = 0, []
    for sid, tail in src.items():
        row = rows.get(sid)
        quote = _row_quote(row, quotes) if row else None
        m = (URL_RE.search(row[1]) if row else None) or URL_RE.search(tail)
        if row is None or quote is None or m is None:
            results.append(f"{sid}: NOT CHECKABLE (row, quote or URL missing)")
            continue
        try:
            req = urllib.request.Request(m.group(0), headers={"User-Agent": "Mozilla/5.0 kotoba-lane-check"})
            with urllib.request.urlopen(req, timeout=40) as resp:
                body = resp.read().decode("utf-8", errors="replace")
        except (urllib.error.URLError, OSError, ValueError) as exc:
            results.append(f"{sid}: FETCH FAILED {exc}")
            continue
        if quote in _page_text(body) or quote in _norm(body):
            found += 1
            results.append(f"{sid}: found")
        else:
            results.append(f"{sid}: NOT FOUND")
    return found, results


def _world(root: Path, entry: str | None = None, sources: str | None = None,
           readme: str | None = None, drop_entry: bool = False) -> Path:
    dest = Path(tempfile.mkdtemp(prefix="k69-prec-world-"))
    for path in (ENTRY, SOURCES, README):
        out = dest / path
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text((root / path).read_text(encoding="utf-8"), encoding="utf-8")
    if drop_entry:
        (dest / ENTRY).unlink()
    for path, text in ((ENTRY, entry), (SOURCES, sources), (README, readme)):
        if text is not None:
            (dest / path).write_text(text, encoding="utf-8")
    return dest


def selftest(repo: Path) -> int:
    """Honest world from the working tree, then one broken world per conjunct.

    Every mutation is derived from the parsed entry and registry, so the worlds track content
    edits instead of hard-coded strings.
    """
    if not (repo / ENTRY).is_file():
        print("selftest setup failed: the entry is not present in the working tree", file=sys.stderr)
        return 2
    entry = (repo / ENTRY).read_text(encoding="utf-8")
    sources = (repo / SOURCES).read_text(encoding="utf-8")
    readme = (repo / README).read_text(encoding="utf-8")
    failures = 0
    n, findings = check(repo)
    if n != TOTAL or findings:
        print(f"FAIL honest world: backed {n} of {TOTAL}; {findings}", file=sys.stderr)
        failures += 1
    else:
        print(f"PASS honest world: backed {TOTAL} of {TOTAL}")

    src, _ = _provenance(entry)
    first = next(iter(src))
    rows = _source_rows(sources)
    row = rows.get(first)
    row_line = next((l for l in sources.splitlines() if _cells(l)[:1] == [first]), None)
    if row is None or row_line is None:
        print("selftest setup failed: the first cited id has no registry row in the working tree",
              file=sys.stderr)
        return 2
    quote = _row_quote(row, _quoted(_norm(entry)))
    table_line = next((l for l in entry.splitlines() if _cells(l) and first in _cells(l)), None)
    if table_line is None or quote is None:
        print("selftest setup failed: the first cited id has no per-client table row, or its "
              "anchor carries no located quote in the working tree", file=sys.stderr)
        return 2
    tcells = _cells(table_line)
    second = list(src)[1]
    other_line = next(l for l in entry.splitlines() if _cells(l) and second in _cells(l))

    def replace_row(new_cells: list[str]) -> str:
        return sources.replace(row_line, "| " + " | ".join(new_cells) + " |", 1)

    def with_cell(i: int, value: str) -> list[str]:
        c = list(row)
        c[i] = value
        return c

    lines = entry.splitlines()
    first_src = next(i for i, l in enumerate(lines) if l.startswith("source:"))
    worlds = {
        "entry missing": _world(repo, drop_entry=True),
        "no source line": _world(repo, entry="\n".join(l for l in lines if not l.startswith("source:"))),
        "provenance not at the opening": _world(repo, entry="\n".join(
            lines[:first_src] + ["Prose before provenance."] + lines[first_src:])),
        "four ids": _world(repo, entry="\n".join(l for l in lines if not l.startswith(f"source: {first}"))),
        "id does not resolve": _world(repo, entry=entry.replace(first, "S999")),
        "row not mined": _world(repo, sources=replace_row(with_cell(7, "queued"))),
        "row opened another day": _world(repo, sources=replace_row(with_cell(8, "2026-10-01"))),
        "used-by omits the entry": _world(repo, sources=replace_row(with_cell(10, "—"))),
        "source cell absent from the entry": _world(repo, entry=entry.replace(row[1], "elsewhere", 1)),
        "no verified-at": _world(repo, entry=entry.replace(f"verified-at: {VERIFIED_AT}", "verified-at: 2020-01-01")),
        "no recheck": _world(repo, entry=re.sub(r"(?m)^recheck:", "note:", entry)),
        "quote not in the anchor cell": _world(repo, sources=replace_row(with_cell(5, "a different anchor"))),
        "table row loses the quote": _world(repo, entry=entry.replace(
            table_line, "| " + " | ".join("elided" if quote in _norm(c) else c for c in tcells) + " |")),
        "table row duplicated": _world(repo, entry=entry.replace(table_line, table_line + "\n" + table_line)),
        "table row client is the id": _world(repo, entry=entry.replace(
            table_line, "| " + " | ".join([first] + tcells[1:]) + " |")),
        "table row rule cell empty": _world(repo, entry=entry.replace(
            table_line, "| " + " | ".join(tcells[:1] + [""] + tcells[2:]) + " |")),
        "table quote cell loses the quote": _world(repo, entry=entry.replace(
            table_line, "| " + " | ".join(tcells[:2] + ["elided quote"] + tcells[3:]) + " |")),
        "coverage row under a junk heading": _world(repo, readme=readme.replace(
            f"`knowledge/{Path(ENTRY).name}`", "`knowledge/absent.md`") + "\n## Removed entries\n\n"
            f"| stale | `knowledge/{Path(ENTRY).name}` | x |\n"),
        "two rows name one client": _world(repo, entry=entry.replace(
            other_line, "| " + " | ".join([tcells[0]] + _cells(other_line)[1:]) + " |")),
        "no coverage-map row": _world(repo, readme=readme.replace(
            f"`knowledge/{Path(ENTRY).name}`", "`knowledge/absent.md`")),
    }
    for name, world in worlds.items():
        n, findings = check(world)
        if n == TOTAL:
            print(f"FAIL broken world survived: {name} -> backed {n}", file=sys.stderr)
            failures += 1
        else:
            print(f"PASS broken world rejected: {name}")
        shutil.rmtree(world, ignore_errors=True)
    missing = _world(repo, drop_entry=True)
    n, _ = check(missing)
    shutil.rmtree(missing, ignore_errors=True)
    if n != 0:
        print(f"FAIL missing-entry classification: backed {n}, expected 0", file=sys.stderr)
        failures += 1
    else:
        print("PASS missing-entry classification: backed 0 (content verdict)")
    print(f"self-test: {failures} failure(s) over {len(worlds) + 2} assertions")
    return 1 if failures else 0


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="C1 counter for kotoba round 69")
    ap.add_argument("--rev", default=None, help="measured revision")
    ap.add_argument("--repo", default=str(Path(__file__).resolve().parent.parent))
    ap.add_argument("--fetch", action="store_true", help="re-open each cited URL and check the quote")
    ap.add_argument("--self-test", action="store_true")
    args = ap.parse_args(argv)
    repo = Path(args.repo)
    if not repo.is_dir():
        print(f"environment error: {repo} is not a directory", file=sys.stderr)
        return 2
    if args.self_test:
        return selftest(repo)
    try:
        if args.rev:
            sha = _resolve(repo, args.rev)
            with tempfile.TemporaryDirectory(prefix="k69-prec-rev-") as tmp:
                _materialize(repo, sha, Path(tmp))
                n, findings = check(Path(tmp))
                found, results = fetch(Path(tmp)) if args.fetch and n == TOTAL else (0, [])
        else:
            sha = "working-tree"
            n, findings = check(repo)
            found, results = fetch(repo) if args.fetch and n == TOTAL else (0, [])
    except EnvError as exc:
        print(f"environment error: {exc}", file=sys.stderr)
        return 2
    print(f"measured-rev: {sha}")
    print(f"skill precedence backed {n} of {TOTAL}")
    for f in findings:
        print(f"  - {f}")
    if args.fetch:
        for r in results:
            print(f"  fetch {r}")
        print(f"live quotes found {found} of {TOTAL}")
    return 0 if n == TOTAL else 1


if __name__ == "__main__":
    sys.exit(main())
