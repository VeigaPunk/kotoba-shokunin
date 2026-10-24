#!/usr/bin/env python3
"""check_instruction_authority.py — C2 counter for kotoba round 67.

Contract
--------
`python3 -B verifiers/check_instruction_authority.py --rev <full-sha>` prints
    authority ladder grounded N of 1
and exits 0 when N == 1, nonzero otherwise.  At the pinned base it must print
`authority ladder grounded 0 of 1` and exit nonzero.

What the counter reads (content, not names — QUALITY Q25/Q26).  For
`corpus/knowledge/instruction-authority-ladder-round67.md` at the measured revision:

  1. the entry file exists;
  2. it opens with `source:` lines naming at least one `S###` id;
  3. every cited id resolves to a row in `corpus/SOURCES.md` whose `status` is `mined`;
  4. each cited row's `source` cell occurs verbatim in the entry's `source:` line for that id;
  5. the entry carries a `verified-at:` line dated 2026-10-24 and a `recheck:` line;
  6. for each cited id, the entry carries a double-quoted located quote of at most 25 words
     that also occurs in that row's `anchor` cell;
  7. the entry is indexed in `corpus/README.md`'s coverage map.

Trust boundary (QUALITY Q33): the counter runs the measured revision's own bytes, so a
revision that rewrites the instrument can change the verdict.  The claim's verdict therefore
also cites the controls outside this counter: the base control prints `0 of 1`, the junk-entry
control is rejected, and the mutation battery in `.ufo/waves/round-67/controls/` shows each
conjunct is load-bearing.

Exit codes: 0 grounded · 1 not grounded · 2 usage/environment error.
"""
from __future__ import annotations

import argparse
import re
import subprocess
import sys
import tempfile
from pathlib import Path

ENTRY = "corpus/knowledge/instruction-authority-ladder-round67.md"
SOURCES = "corpus/SOURCES.md"
README = "corpus/README.md"
VERIFIED_AT = "2026-10-24"
TOTAL = 1

ID_RE = re.compile(r"\bS(\d{3,})\b")
ROW_RE = re.compile(r"^\|(.*)$")
SOURCE_LINE_RE = re.compile(r"^source:\s*(S\d{3,})\s*(.*)$")
QUOTED_RE = re.compile(r'"([^"\n]{1,300})"')


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


def _split_row(body: str) -> list[str]:
    cells = body.split("|")
    # a leading empty cell comes from the leading `|`
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
    """Return (grounded_count, findings). grounded_count is 0 or TOTAL."""
    findings: list[str] = []
    entry_path = root / ENTRY
    if not entry_path.is_file():
        return 0, ["entry missing: " + ENTRY]
    entry = entry_path.read_text(encoding="utf-8")
    sources_path = root / SOURCES
    readme_path = root / README
    if not sources_path.is_file() or not readme_path.is_file():
        return 0, ["registry or coverage map missing"]
    sources_text = sources_path.read_text(encoding="utf-8")
    readme_text = readme_path.read_text(encoding="utf-8")

    # (2) source lines naming S### ids
    src_lines = _entry_source_lines(entry)
    if not src_lines:
        return 0, ["no `source:` line naming an S### id"]
    ids = list(src_lines)
    if len(set(ids)) != len(ids):
        return 0, ["duplicate id in the entry's source lines"]

    rows = _source_rows(sources_text)
    entry_norm = re.sub(r"\s+", " ", entry)
    quotes = _quoted(entry_norm)

    for sid in ids:
        # (3) the id resolves to a mined row
        row = rows.get(sid)
        if row is None:
            findings.append(f"{sid}: no row in {SOURCES}")
            continue
        if len(row) < 11:
            findings.append(f"{sid}: row has {len(row)} cells, expected 11")
            continue
        status = row[7]
        if status != "mined":
            findings.append(f"{sid}: status is {status!r}, expected 'mined'")
            continue
        # (4) the row's source cell occurs verbatim in the entry's source line
        row_source = row[1]
        if row_source not in src_lines[sid]:
            findings.append(f"{sid}: the row's source cell is not in the entry's source line")
            continue
        # (6) a located quote of at most 25 words, shared with the row's anchor cell
        anchor = re.sub(r"\s+", " ", row[5])
        if not any(q in anchor for q in quotes):
            findings.append(f"{sid}: no located quote of the entry occurs in the row's anchor cell")
            continue

    # (5) verified-at and recheck
    if not any(line.strip() == f"verified-at: {VERIFIED_AT}" for line in entry.splitlines()):
        findings.append(f"no `verified-at: {VERIFIED_AT}` line")
    if not any(line.strip().startswith("recheck:") for line in entry.splitlines()):
        findings.append("no `recheck:` line")

    # (7) coverage-map index row
    if not _indexed(readme_text):
        findings.append("the entry has no coverage-map index row in " + README)

    if findings:
        return 0, findings
    return TOTAL, []


def _world(root: Path, *, entry: str | None = None, sources: str | None = None,
           readme: str | None = None, drop_entry: bool = False) -> Path:
    """Build a scratch world from <root> with one conjunct broken."""
    dest = Path(tempfile.mkdtemp(prefix="k67-world-"))
    for path in (ENTRY, SOURCES, README):
        src = root / path
        out = dest / path
        out.parent.mkdir(parents=True, exist_ok=True)
        if src.is_file():
            shutil_copy = src.read_text(encoding="utf-8")
            out.write_text(shutil_copy, encoding="utf-8")
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
    """Drive the public main() on a satisfying world and on one broken world per conjunct."""
    failures = 0
    # The honest world is the lane working tree (the round's content lands before the
    # commit; the measured --rev run is the after-measurement that follows it).
    base = repo
    if not (base / ENTRY).is_file():
        print("selftest setup failed: the entry is not present in the working tree",
              file=sys.stderr)
        return 2
    entry_text = (base / ENTRY).read_text(encoding="utf-8")
    sources_text = (base / SOURCES).read_text(encoding="utf-8")
    readme_text = (base / README).read_text(encoding="utf-8")

    n, findings = check(base)
    if n != TOTAL or findings:
        print(f"FAIL honest world: grounded {n} of {TOTAL}; {findings}", file=sys.stderr)
        failures += 1
    else:
        print("PASS honest world: grounded 1 of 1")

    worlds = {
        "entry missing": _world(base, drop_entry=True),
        "no source line": _world(base, entry="\n".join(
            l for l in entry_text.splitlines() if not l.startswith("source:"))),
        "id does not resolve": _world(base, entry=entry_text.replace("S123", "S999")),
        "row not mined": _world(base, sources="\n".join(
            (l.replace("| mined |", "| queued |", 1) if l.startswith("| S123 |") else l)
            for l in sources_text.splitlines())),
        "source cell absent from the entry": _world(base, entry=entry_text.replace(
            "OpenAI Model Spec (August 18, 2026) — https://model-spec.openai.com/2026-08-18",
            "OpenAI Model Spec — https://model-spec.openai.com/2026-08-18")),
        "no verified-at": _world(base, entry=entry_text.replace(
            f"verified-at: {VERIFIED_AT}", "verified-at: 2020-01-01")),
        "no recheck": _world(base, entry=entry_text.replace(
            "recheck: 90d — re-fetch", "note: re-fetch")),
        "no coverage-map row": _world(base, readme=readme_text.replace(
            "`knowledge/instruction-authority-ladder-round67.md`", "`knowledge/absent.md`")),
        "quote not in the anchor cell": _world(base, sources=sources_text.replace(
            "Instructions with higher authority override those with lower authority.",
            "A different sentence entirely.")),
    }
    for name, world in worlds.items():
        n, findings = check(world)
        if n != 0:
            print(f"FAIL broken world survived: {name} -> grounded {n}", file=sys.stderr)
            failures += 1
        else:
            print(f"PASS broken world rejected: {name}")
    print(f"self-test: {failures} failure(s) over {len(worlds) + 1} assertions")
    return 1 if failures else 0


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(add_help=True)
    ap.add_argument("--rev", default=None, help="measured revision (full sha)")
    ap.add_argument("--repo", default=str(Path(__file__).resolve().parent.parent))
    ap.add_argument("--self-test", action="store_true")
    args = ap.parse_args(argv)
    repo = Path(args.repo)
    if args.self_test:
        return selftest(repo)
    try:
        if args.rev:
            with tempfile.TemporaryDirectory(prefix="k67-rev-") as tmp:
                root = _materialize(repo, args.rev, Path(tmp))
                n, findings = check(root)
        else:
            n, findings = check(repo)
    except EnvError as exc:
        print(f"environment error: {exc}", file=sys.stderr)
        return 2
    print(f"authority ladder grounded {n} of {TOTAL}")
    for f in findings:
        print(f"  - {f}")
    return 0 if n == TOTAL else 1


if __name__ == "__main__":
    sys.exit(main())
