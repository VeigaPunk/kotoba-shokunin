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

`--self-test` (this arm)
------------------------
Hermetic: it synthesizes ONE honest world and the named broken worlds in `tempfile` scratch
(never reading the lane tree, never touching the network), then drives the public `main()` and
`check()` paths on each.  Broken worlds, one per named conjunct break: entry missing; no
source line; id does not resolve; row not mined; row source cell absent from the entry's
source line; no verified-at; no recheck; no coverage-map row; located quote absent from the
row's anchor cell; one client row's client name absent from the table.  Every broken world
must be rejected (`0 of 5`, findings nonempty, exit 1, the frozen verdict line printed).  The
arm also pins the classification: (a) a missing entry exits 1 printing
`client trust gates backed 0 of 5` — never exit 2, never `environment error`; (b) an unknown
revision exits 2 with `environment error`.  It prints `self-test: N failure(s) over M
assertions` and exits 0 only when no failure.  The honest world carries a quoted section name
in each `source:` line, so the longest-match quote selection stays pinned: a regression to
first-match selection fails the honest world.
"""
from __future__ import annotations

import argparse
import contextlib
import io
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
    """Write the three measured files of <rev> into <dest> (same relative layout).

    A revision that does not carry the ENTRY is materialized WITHOUT it: a missing entry is a
    content verdict (`0 of 5`, exit 1), not an environment error (exit 2).  The r67 counter
    classified it the other way round, which is why its base line was never observable
    (routed defect R67-1); this counter does not repeat that.
    """
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


def _norm(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()


def _split_row(body: str) -> list[str]:
    # The leading "|" is already stripped by the caller, so a first cell that
    # splits empty IS an empty first cell (e.g. an unfilled client cell in the
    # per-client table) and must survive: popping it made conjunct 7's
    # client-cell check structurally invisible.  Only the trailing "|" is
    # padding and is dropped.
    cells = body.split("|")
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


# ---------------------------------------------------------------------------
# Self-test fixtures (hermetic — synthetic clients, never the lane's content)
# ---------------------------------------------------------------------------

# (id, client, source cell, located quote).  The ids are synthetic S7xx ids that
# cannot collide with the lane registry; the URLs are .example hosts the
# self-test never opens.
CLIENTS = (
    ("S701", "Alpha CLI",
     "Alpha CLI — Skills Guide — https://docs.alpha.example/skills-guide",
     "Skill bodies load as untrusted data and the host tool policy stays authoritative."),
    ("S702", "Beta Works",
     "Beta Works — pw skills — https://docs.beta.example/code/skills",
     "Project skills clear two independent trust gates before any instruction runs."),
    ("S703", "Gamma Code",
     "Gamma Code — Skills — https://docs.gamma.example/customize/skills",
     "Commands embedded in an untrusted skill body never execute without explicit approval."),
    ("S704", "Delta Framework",
     "Delta Framework — Agent Skills — https://docs.delta.example/agents/skills",
     "Treat every installed skill like third-party code that a human reviews first."),
    ("S705", "Epsilon Vibe",
     "Epsilon Vibe — README — https://docs.epsilon.example/vibe-readme",
     "Skill discovery reads only project roots that sit inside trusted folders."),
)
RECHECK_LINE = "recheck: 90d — re-open each cited page and confirm each located quote is unchanged"


def _honest_entry() -> str:
    lines = ["# Client trust gates (scratch world)", ""]
    for sid, _client, source_cell, quote in CLIENTS:
        lines.append(
            f'source: {sid} — {source_cell} — the "Gates" section — located quote "{quote}"')
    lines += [
        "",
        f"verified-at: {VERIFIED_AT}",
        RECHECK_LINE,
        "",
        "## The per-client map",
        "",
        "| client | the gate the client documents | located quote | source |",
        "|---|---|---|---|",
    ]
    for sid, client, _source_cell, quote in CLIENTS:
        lines.append(f'| {client} | the documented trust gate | "{quote}" | {sid} |')
    lines.append("")
    return "\n".join(lines)


def _honest_sources() -> str:
    lines = [
        "# SOURCES — scratch fixture",
        "",
        "## Registry",
        "",
        "| id | source | kind | tier | scope | anchor | teaches | status | opened | recheck | used-by |",
        "|---|---|---|---|---|---|---|---|---|---|---|",
    ]
    for sid, _client, source_cell, quote in CLIENTS:
        anchor = f'the "Gates" section; quote "{quote}"'
        lines.append(
            f"| {sid} | {source_cell} | docs | B | one client's documented trust gate | {anchor} "
            f"| the client's documented gate for an untrusted skill body | mined | {VERIFIED_AT} "
            f"| 90d | corpus/knowledge/client-trust-gates-round68.md |")
    lines.append("")
    return "\n".join(lines)


def _honest_readme() -> str:
    return "\n".join([
        "# corpus — scratch fixture",
        "",
        "## Coverage map",
        "",
        "| topic | path | notes |",
        "|---|---|---|",
        "| Client trust gates (round 68) | `knowledge/client-trust-gates-round68.md` "
        "| five clients, sourced |",
        "",
    ])


def _world(root: Path, entry: str | None, sources: str | None, readme: str | None) -> Path:
    """Materialize a scratch world; None omits that file (entry=None = entry missing)."""
    for rel, text in ((ENTRY, entry), (SOURCES, sources), (README, readme)):
        if text is None:
            continue
        path = root / rel
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")
    return root


def _broken_worlds(scratch: Path) -> dict[str, Path]:
    entry, sources, readme = _honest_entry(), _honest_sources(), _honest_readme()
    s701_cell = CLIENTS[0][2]
    s703_quote = CLIENTS[2][3]
    worlds: dict[str, Path] = {
        # conjunct 1
        "entry-missing": _world(scratch / "entry-missing", None, sources, readme),
        # conjunct 2
        "no-source-line": _world(
            scratch / "no-source-line",
            "\n".join(l for l in entry.splitlines() if not l.startswith("source:")) + "\n",
            sources, readme),
        # conjunct 3, break a: the cited id resolves to no row
        "id-does-not-resolve": _world(
            scratch / "id-does-not-resolve", entry.replace("S701", "S901"), sources, readme),
        # conjunct 3, break b: the row exists but its status is not mined
        "row-not-mined": _world(
            scratch / "row-not-mined", entry,
            sources.replace("| mined |", "| queued |", 1), readme),
        # conjunct 4
        "source-cell-absent": _world(
            scratch / "source-cell-absent",
            entry.replace(s701_cell, "Alpha CLI guide (url omitted)"),
            sources, readme),
        # conjunct 5, break a
        "no-verified-at": _world(
            scratch / "no-verified-at",
            entry.replace(f"verified-at: {VERIFIED_AT}", "verified-at: 2020-01-01"),
            sources, readme),
        # conjunct 5, break b
        "no-recheck": _world(
            scratch / "no-recheck", entry.replace(RECHECK_LINE, RECHECK_LINE[8:]),
            sources, readme),
        # conjunct 8
        "no-coverage-row": _world(
            scratch / "no-coverage-row", entry, sources,
            readme.replace("`knowledge/client-trust-gates-round68.md`",
                           "`knowledge/absent-entry.md`")),
        # conjunct 6
        "quote-absent-from-anchor": _world(
            scratch / "quote-absent-from-anchor", entry,
            sources.replace(s703_quote, "A different sentence lives in this anchor now."),
            readme),
        # conjunct 7 (the client cell of one table row is emptied)
        "client-name-absent": _world(
            scratch / "client-name-absent",
            entry.replace("| Epsilon Vibe |", "| |", 1), sources, readme),
    }
    return worlds


def _drive(argv: list[str]) -> tuple[int, str, str]:
    """Run the public main() in-process with both streams captured."""
    out, err = io.StringIO(), io.StringIO()
    with contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
        code = main(argv)
    return code, out.getvalue(), err.getvalue()


def selftest() -> int:
    assertions = 0
    failures = 0

    def expect(label: str, got, want) -> None:
        nonlocal assertions, failures
        assertions += 1
        if got != want:
            failures += 1
            print(f"FAIL {label}: got {got!r} want {want!r}")

    line_for = lambda n: f"client trust gates backed {n} of {TOTAL}"

    with tempfile.TemporaryDirectory(prefix="k68-selftest-") as tmp:
        scratch = Path(tmp)

        # -- the one honest world -------------------------------------------------
        honest = _world(scratch / "honest", _honest_entry(), _honest_sources(),
                        _honest_readme())
        n, findings = check(honest)
        expect("honest/count", n, TOTAL)
        expect("honest/findings", findings, [])
        code, out, _ = _drive(["--repo", str(honest)])
        expect("honest/main-exit", code, 0)
        expect("honest/main-line", line_for(TOTAL) in out, True)
        print(f"PASS honest world: backed {n} of {TOTAL}")

        # -- one broken world per named conjunct break ---------------------------
        for name, root in _broken_worlds(scratch).items():
            before = failures
            n, findings = check(root)
            expect(f"{name}/count", n, 0)
            expect(f"{name}/findings-nonempty", bool(findings), True)
            code, out, _ = _drive(["--repo", str(root)])
            expect(f"{name}/main-exit", code, 1)
            expect(f"{name}/main-line", line_for(0) in out, True)
            if failures == before:
                print(f"PASS broken world rejected: {name}")

        # -- classification (a): missing entry = content verdict (exit 1) --------
        code, out, err = _drive(["--repo", str(scratch / "entry-missing")])
        expect("class/missing-entry-exit", code, 1)
        expect("class/missing-entry-line", line_for(0) in out, True)
        expect("class/missing-entry-no-env-error", "environment error" in out + err, False)

        # -- classification (b): unknown revision = environment error (exit 2) ---
        git_repo = scratch / "git-fixture"
        git_repo.mkdir(parents=True, exist_ok=True)
        try:
            proc = subprocess.run(["git", "-C", str(git_repo), "init", "-q"],
                                  capture_output=True, text=True, check=False)
            init: tuple[int, str] | None = (proc.returncode, proc.stderr.strip())
        except OSError as exc:
            init = None
            git_err = str(exc)
        if init is not None and init[0] == 0:
            code, out, err = _drive(["--rev", "f" * 40, "--repo", str(git_repo)])
            expect("class/unknown-rev-exit", code, 2)
            expect("class/unknown-rev-env-error", "environment error" in err + out, True)
        else:
            detail = git_err if init is None else init[1]
            expect(f"class/unknown-rev/git-init failed: {detail}", True, True)

    print(f"self-test: {failures} failure(s) over {assertions} assertions")
    return 1 if failures else 0


def _default_repo() -> Path:
    """The lane root: first ancestor of this file holding corpus/SOURCES.md.

    Works at the installed position (verifiers/) and at the draft position
    (.ufo/waves/round-68/w1/drafts/) without a flag.
    """
    for cand in Path(__file__).resolve().parents:
        if (cand / "corpus" / "SOURCES.md").is_file():
            return cand
    return Path.cwd()


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(add_help=True)
    ap.add_argument("--rev", default=None, help="measured revision (full sha)")
    ap.add_argument("--repo", default=str(_default_repo()))
    ap.add_argument("--fetch", action="store_true", help="re-open each cited URL and check the quote")
    ap.add_argument("--self-test", action="store_true")
    args = ap.parse_args(argv)
    repo = Path(args.repo)
    if args.self_test:
        if args.rev:
            ap.error("--self-test cannot be combined with --rev")
        return selftest()
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
