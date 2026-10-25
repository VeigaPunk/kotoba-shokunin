#!/usr/bin/env python3
"""check_client_trust_gates.py — C1 counter for kotoba round 68 (wave-1 draft).

Frozen predicate (plans/round-68.md, C1)
----------------------------------------
`python3 -B verifiers/check_client_trust_gates.py --rev <full-sha>` prints
    client trust gates backed N of 5
and exits 0 when N == 5, nonzero otherwise.  At the pinned base
(`e94ae32a5cd8dc3ee8e2d247816784bec2750cc0`, where the entry does not exist)
it must print `client trust gates backed 0 of 5` and exit 1.  `--repo <path>`
overrides the lane root (default: the nearest ancestor of this file that holds
`corpus/SOURCES.md`, so the draft runs from `.ufo/waves/round-68/w1/drafts/`
and the installed copy from `verifiers/`).  `--fetch` additionally re-opens
each cited URL and reports whether the located quote is present on the live
page — network failures are printed as `unreachable (...)`, never counted as
found and never silently dropped.  The fetch is a measurement: it never moves
the exit code, which stays the content verdict's.

What the counter reads (content, not names — QUALITY Q25/Q26).  For
`corpus/knowledge/client-trust-gates-round68.md` at the measured revision:

  1. the entry file exists;
  2. the entry opens with `source:` lines naming `S###` ids — the first
     non-blank line is a `source:` line, the ids sit in the first 10 lines,
     there are no duplicates, and there are exactly 5 (one per client row);
  3. every cited id resolves to a row in `corpus/SOURCES.md` whose `status`
     is `mined`;
  4. each cited row's `source` cell occurs verbatim in that id's `source:`
     line;
  5. the entry carries a `verified-at: 2026-10-24` line and a `recheck:` line;
  6. for each cited id, the entry carries a double-quoted located quote of at
     most 25 words that also occurs in that row's `anchor` cell;
  7. each client's id and its located quote co-occur in one row of the entry's
     per-client table (client · gate · located quote · source id, so the row
     must have at least four cells), and the entry is indexed in
     `corpus/README.md`'s coverage map.  The client *name* is prose the
     counter deliberately does not hardcode (content, not names); the table
     column carrying it is enforced structurally.

Classification — routed defect R67-1, fixed from the start: a MISSING ENTRY is
a CONTENT verdict; the counter prints `client trust gates backed 0 of 5` and
exits 1.  Exit 2 (`environment error: ...` on stderr) is reserved for a
measurement that cannot run at all: an unknown revision, an unreadable or
non-git repo, or git itself unavailable.  Generalized rule: absence of a
measured file at a resolvable revision (entry, registry, coverage map) is a
content verdict; only failure to run the measurement is an environment error.

Counting semantics (the r67 shape, `check_instruction_authority.py`, extended
from 1 to 5): a global malformation (missing verified-at / recheck /
coverage-map row, wrong source-line count, duplicate id, entry not opening
with `source:`) means the entry as a whole backs nothing — 0 of 5, exit 1.  A
per-client failure (conjunctions 3/4/6/7 broken for one id) drops that client,
so the counter prints honest partial credit (e.g. `backed 4 of 5`, exit 1).
`backed 5 of 5` therefore implies exit 0.

Trust boundary (QUALITY Q33): with `--rev` the counter reads the measured
revision's own bytes, so a revision that rewrites the instrument can change
the verdict.  The claim therefore also cites the controls outside this
counter: the base control above, the junk-entry control, the mutation battery
under `.ufo/waves/round-68/controls/`, and the `--fetch` measurement.

`--self-test` builds a synthetic fixture world in a scratch git repository
under the system temp dir (nothing in the lane's worktree, index or jj state
is touched) and drives the public paths on it: the honest world at the head
revision and in working-tree mode, the base control (entry absent at a valid
revision → content `0 of 5`, exit 1 — the R67-1 regression guard), an unknown
revision → exit 2, and one broken world per conjunct.  It is fixture-built, so
it passes before the real entry lands; it performs no network access, so
`--fetch` is not exercised there (it is a live measurement, reported by the
round's controls).

Exit codes: 0 grounded · 1 not grounded · 2 usage/environment error.
"""
from __future__ import annotations

import argparse
import html
import io
import re
import shutil
import subprocess
import sys
import tempfile
import urllib.request
from contextlib import redirect_stderr, redirect_stdout
from pathlib import Path

ENTRY = "corpus/knowledge/client-trust-gates-round68.md"
SOURCES = "corpus/SOURCES.md"
README = "corpus/README.md"
VERIFIED_AT = "2026-10-24"
TOTAL = 5
ENTRY_WINDOW = 10
FETCH_TIMEOUT = 20

SOURCE_LINE_RE = re.compile(r"^source:\s*(S\d{3,})\s*(.*)$")
QUOTED_RE = re.compile(r'"([^"\n]{1,300})"')
URL_RE = re.compile(r"https?://[^\s|]+")
FOLD = str.maketrans({
    "\u2018": "'", "\u2019": "'",
    "\u201c": '"', "\u201d": '"',
    "\u2013": "-", "\u2014": "-",
    "\u00a0": " ",
})


class EnvError(Exception):
    """The measurement cannot run: unknown revision, unreadable repo, no git."""


def _norm(text: str) -> str:
    """Whitespace-collapsed, typographic-punctuation-folded form for matching."""
    return re.sub(r"\s+", " ", text.translate(FOLD)).strip()


# --- measurement plumbing -------------------------------------------------


def _run_git(repo: Path, *args: str) -> subprocess.CompletedProcess:
    try:
        return subprocess.run(
            ["git", "-C", str(repo), *args], capture_output=True, text=True)
    except FileNotFoundError:
        raise EnvError("git is not available on PATH") from None


def _resolve_rev(repo: Path, rev: str) -> None:
    proc = _run_git(repo, "rev-parse", "--verify", "--quiet", f"{rev}^{{commit}}")
    if proc.returncode != 0:
        detail = proc.stderr.strip() or proc.stdout.strip() or "no output"
        raise EnvError(f"unknown revision {rev!r} (git rev-parse failed: {detail})")


def _read_at(repo: Path, rev: str, path: str) -> str | None:
    """File bytes at <rev>; None when the file is absent there (a content fact)."""
    proc = _run_git(repo, "show", f"{rev}:{path}")
    if proc.returncode != 0:
        return None
    return proc.stdout


def _state_of(root: Path) -> dict[str, str | None]:
    out: dict[str, str | None] = {}
    for path in (ENTRY, SOURCES, README):
        p = root / path
        out[path] = p.read_text(encoding="utf-8") if p.is_file() else None
    return out


def _load(repo: Path, rev: str | None) -> dict[str, str | None]:
    if rev is None:
        return _state_of(repo)
    _resolve_rev(repo, rev)
    state: dict[str, str | None] = {}
    for path in (ENTRY, SOURCES, README):
        state[path] = _read_at(repo, rev, path)
    return state


# --- content parsers (mirrors of the r67 counter, extended to the table) ---


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
        if not line.startswith("|"):
            continue
        cells = [c.strip() for c in line[1:].split("|")]
        if cells and cells[-1] == "":
            cells.pop()
        if len(cells) != 11 or not re.fullmatch(r"S\d{3,}", cells[0]):
            continue
        rows[cells[0]] = cells
    return rows


def _entry_source_lines(text: str) -> dict[str, str]:
    """The `source:` lines that OPEN the entry (within the first 10 lines)."""
    out: dict[str, str] = {}
    for line in text.splitlines()[:ENTRY_WINDOW]:
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


def _table_row_for(entry_lines: list[str], sid: str, quotes: list[str]) -> bool:
    """Conjunct 7's machine-checkable form: one table row carries the id and
    its located quote, with at least four cells (client · gate · quote · id)."""
    for line in entry_lines:
        if not line.lstrip().startswith("|") or sid not in line:
            continue
        cells = _split_row(line.strip())
        if len(cells) < 4:
            continue
        norm = _norm(line)
        if any(q in norm for q in quotes):
            return True
    return False


# --- the verdict -----------------------------------------------------------


def check(state: dict[str, str | None]) -> tuple[int, list[str]]:
    """Return (backed_count, findings); backed_count counts fully-backed clients."""
    findings: list[str] = []
    if state[ENTRY] is None:
        # CONTENT verdict — routed defect R67-1 fixed: a missing entry is not an
        # environment error.  This is the pinned base's path.
        return 0, ["entry missing: " + ENTRY]
    entry = state[ENTRY]
    entry_lines = entry.splitlines()

    src_lines = _entry_source_lines(entry)
    if not src_lines:
        return 0, [
            "no `source:` line naming an S### id in the entry's first "
            f"{ENTRY_WINDOW} lines"]
    ids = list(src_lines)
    if len(set(ids)) != len(ids):
        return 0, ["duplicate id in the entry's source lines"]
    if len(ids) != TOTAL:
        return 0, [
            f"the entry cites {len(ids)} source line(s); expected {TOTAL}, "
            "one per client row"]

    if state[SOURCES] is None:
        return 0, [f"{SOURCES} is absent — no registry resolves the cited ids"]
    if state[README] is None:
        return 0, [f"{README} is absent — no coverage map"]

    rows = _source_rows(state[SOURCES])
    entry_norm = _norm(entry)
    quotes = _quoted(entry_norm)

    backed = 0
    id_findings: list[str] = []
    for sid in ids:
        row = rows.get(sid)
        if row is None:
            id_findings.append(f"{sid}: no row in {SOURCES}")
            continue
        if len(row) < 11:
            id_findings.append(f"{sid}: row has {len(row)} cells, expected 11")
            continue
        problems: list[str] = []
        if row[7] != "mined":
            problems.append(f"status is {row[7]!r}, expected 'mined'")
        if row[1] not in src_lines[sid]:
            problems.append("the row's source cell does not occur in the entry's source line")
        anchor = _norm(row[5])
        anchor_quotes = [q for q in quotes if q in anchor]
        if not anchor_quotes:
            problems.append("no located quote of the entry occurs in the row's anchor cell")
        elif not _table_row_for(entry_lines, sid, anchor_quotes):
            problems.append("no per-client table row carries the id and its located quote")
        if problems:
            id_findings.append(f"{sid}: " + "; ".join(problems))
        else:
            backed += 1

    if not any(l.strip() == f"verified-at: {VERIFIED_AT}" for l in entry_lines):
        findings.append(f"no `verified-at: {VERIFIED_AT}` line")
    if not any(l.strip().startswith("recheck:") for l in entry_lines):
        findings.append("no `recheck:` line")
    if not any(SOURCE_LINE_RE.match(l.strip()) for l in entry_lines if l.strip()):
        findings.append("the entry does not open with a `source:` line")
    if not _indexed(state[README]):
        findings.append("the entry has no coverage-map index row in " + README)

    if findings:
        # A global malformation means the entry as a whole backs nothing
        # (the r67 counter's any-finding rule, kept for global conjuncts).
        return 0, findings + id_findings
    return backed, id_findings


# --- the --fetch measurement ------------------------------------------------


def _live_page(url: str) -> str:
    req = urllib.request.Request(
        url, headers={"User-Agent": "kotoba-lane-counter/1.0"})
    with urllib.request.urlopen(req, timeout=FETCH_TIMEOUT) as resp:
        raw = resp.read(5_000_000)
    charset = resp.headers.get_content_charset() or "utf-8"
    page = raw.decode(charset, errors="replace")
    page = re.sub(r"(?is)<(script|style)\b.*?</\1>", " ", page)
    page = re.sub(r"(?s)<[^>]+>", " ", page)
    return html.unescape(page)


def fetch_report(state: dict[str, str | None]) -> list[str]:
    """Re-open each cited URL; report per id.  Network failures are printed,
    never counted as found and never silently dropped.  No exit-code effect."""
    if state.get(ENTRY) is None or state.get(SOURCES) is None:
        return ["--fetch: skipped — the entry or the registry is absent at the "
                "measured revision"]
    src_lines = _entry_source_lines(state[ENTRY])
    if not src_lines:
        return ["--fetch: skipped — no `source:` ids to fetch"]
    rows = _source_rows(state[SOURCES])
    quotes = _quoted(_norm(state[ENTRY]))
    lines: list[str] = []
    found = 0
    for sid in src_lines:
        row = rows.get(sid)
        if row is None:
            lines.append(f"--fetch {sid}: no row in {SOURCES} — url unknown, not fetched")
            continue
        m = URL_RE.search(row[1])
        if not m:
            lines.append(f"--fetch {sid}: the row's source cell carries no URL — not fetched")
            continue
        url = m.group(0).rstrip('.,;:)]}"\'')
        sid_quotes = [q for q in quotes if q in _norm(row[5])]
        if not sid_quotes:
            lines.append(f"--fetch {sid}: no anchor-bound quote to check — not fetched")
            continue
        try:
            page = _norm(_live_page(url))
        except Exception as exc:  # reported, never counted
            lines.append(f"--fetch {sid}: unreachable ({type(exc).__name__}: {exc}) <{url}>")
            continue
        if any(q in page for q in sid_quotes):
            found += 1
            lines.append(f"--fetch {sid}: quote found <{url}>")
        else:
            lines.append(f"--fetch {sid}: quote NOT found on the live page <{url}>")
    lines.insert(0, f"--fetch: quotes located on live pages: {found} of {len(src_lines)}")
    return lines


# --- self-test: fixture-built, no lane dependency, no network ---------------


FIX_ROWS = [
    ("S901", "FixtureGate A", "https://fixture.example/gate-a",
     "The client reviews the untrusted skill body before first load."),
    ("S902", "FixtureGate B", "https://fixture.example/gate-b",
     "Untrusted skill text is never executed without a recorded human approval."),
    ("S903", "FixtureGate C", "https://fixture.example/gate-c",
     "A skill from an unknown publisher loads only after the quarantine scan passes."),
    ("S904", "FixtureGate D", "https://fixture.example/gate-d",
     "The client re-verifies the body hash at every load and refuses drift."),
    ("S905", "FixtureGate E", "https://fixture.example/gate-e",
     "Permissions declared by an untrusted skill are dropped at load time."),
]


def _table_row(sid: str, client: str, quote: str) -> str:
    return f'| {client} client | gate {sid} applies | "{quote}" | {sid} |'


def _fixture_entry() -> str:
    lines = [f"source: {sid} — {client} — {url} — `# Gate`"
             for sid, client, url, _ in FIX_ROWS]
    lines += [
        "verified-at: 2026-10-24",
        "recheck: 90d — re-fetch each cited page and confirm the located quotes still read the same",
        "",
        "# Client trust gates for untrusted skill bodies (fixture world)",
        "",
        "| client | documented gate on an untrusted skill body | located quote | source |",
        "|---|---|---|---|",
    ]
    lines += [_table_row(sid, client, quote) for sid, client, _, quote in FIX_ROWS]
    return "\n".join(lines) + "\n"


def _fixture_sources() -> str:
    head = ("# SOURCES\n\n"
            "| id | source | kind | tier | scope | anchor | teaches | status | opened | recheck | used-by |\n"
            "|---|---|---|---|---|---|---|---|---|---|---|\n")
    rows = []
    for sid, client, url, quote in FIX_ROWS:
        anchor = f'§ Gate; quote "{quote}" (opened 2026-10-24)'
        rows.append(
            f"| {sid} | {client} — {url} | docs | A | scope of {sid} | {anchor} | "
            f"teaches {sid} | mined | 2026-10-24 | 90d | {ENTRY} |")
    return head + "\n".join(rows) + "\n"


def _fixture_readme() -> str:
    return ("# Coverage map\n\n"
            "| theme | file | note |\n|---|---|---|\n"
            "| Client trust gates | `knowledge/client-trust-gates-round68.md` | fixture row |\n")


def _git(cwd: Path, *args: str) -> None:
    proc = subprocess.run(["git", "-C", str(cwd), *args],
                          capture_output=True, text=True)
    if proc.returncode != 0:
        raise RuntimeError(f"git {' '.join(args)}: {proc.stderr.strip()}")


def _scratch_repo() -> tuple[Path, str, str]:
    """A throwaway git repo: base = registry without the entry; head = with it."""
    dest = Path(tempfile.mkdtemp(prefix="k68-selftest-"))
    _git(dest, "init", "-q")
    _git(dest, "config", "user.email", "selftest@example.invalid")
    _git(dest, "config", "user.name", "selftest")
    (dest / "corpus" / "knowledge").mkdir(parents=True)
    (dest / SOURCES).write_text(_fixture_sources(), encoding="utf-8")
    (dest / README).write_text(_fixture_readme(), encoding="utf-8")
    _git(dest, "add", "-A")
    _git(dest, "commit", "-qm", "base: registry without the entry")
    base = subprocess.run(["git", "-C", str(dest), "rev-parse", "HEAD"],
                          capture_output=True, text=True).stdout.strip()
    (dest / ENTRY).write_text(_fixture_entry(), encoding="utf-8")
    _git(dest, "add", "-A")
    _git(dest, "commit", "-qm", "head: the entry lands")
    head = subprocess.run(["git", "-C", str(dest), "rev-parse", "HEAD"],
                          capture_output=True, text=True).stdout.strip()
    return dest, base, head


def _world(src: Path, *, entry: str | None = None, sources: str | None = None,
           readme: str | None = None, drop_entry: bool = False) -> Path:
    dest = Path(tempfile.mkdtemp(prefix="k68-world-"))
    for path in (ENTRY, SOURCES, README):
        s = src / path
        d = dest / path
        d.parent.mkdir(parents=True, exist_ok=True)
        if s.is_file():
            d.write_text(s.read_text(encoding="utf-8"), encoding="utf-8")
    if drop_entry:
        (dest / ENTRY).unlink()
    if entry is not None:
        (dest / ENTRY).write_text(entry, encoding="utf-8")
    if sources is not None:
        (dest / SOURCES).write_text(sources, encoding="utf-8")
    if readme is not None:
        (dest / README).write_text(readme, encoding="utf-8")
    return dest


def selftest(repo: Path) -> int:  # noqa: ARG001 — repo unused: fixture-built
    failures = 0
    assertions = 0
    scratch, base_sha, head_sha = _scratch_repo()
    worlds: list[tuple[Path, str]] = []
    try:
        entry_text = (scratch / ENTRY).read_text(encoding="utf-8")
        sources_text = (scratch / SOURCES).read_text(encoding="utf-8")
        readme_text = (scratch / README).read_text(encoding="utf-8")

        def run_main(extra: list[str]) -> tuple[int, str, str]:
            out, err = io.StringIO(), io.StringIO()
            with redirect_stdout(out), redirect_stderr(err):
                rc = main(["--repo", str(scratch), *extra])
            return rc, out.getvalue(), err.getvalue()

        def expect(name: str, ok: bool, detail: str) -> None:
            nonlocal failures, assertions
            assertions += 1
            if ok:
                print(f"PASS {name}")
            else:
                failures += 1
                print(f"FAIL {name}: {detail}", file=sys.stderr)

        # 1 — honest world at the head revision (the measured --rev path)
        rc, out, err = run_main(["--rev", head_sha])
        expect("honest world at head rev",
               rc == 0 and f"client trust gates backed {TOTAL} of {TOTAL}" in out,
               f"rc={rc} out={out.strip()!r} err={err.strip()!r}")

        # 2 — honest world in working-tree mode (no --rev)
        rc, out, err = run_main([])
        expect("honest world, working tree",
               rc == 0 and f"client trust gates backed {TOTAL} of {TOTAL}" in out,
               f"rc={rc} out={out.strip()!r} err={err.strip()!r}")

        # 3 — the base control: entry absent at a VALID revision is a CONTENT
        #     verdict (0 of 5, exit 1) — the R67-1 regression guard.
        rc, out, err = run_main(["--rev", base_sha])
        expect("base control: missing entry is content (exit 1), not environment",
               rc == 1 and "client trust gates backed 0 of 5" in out
               and "environment error" not in err,
               f"rc={rc} out={out.strip()!r} err={err.strip()!r}")

        # 4 — an unknown revision stays an environment error (exit 2)
        rc, out, err = run_main(["--rev", "f" * 40])
        expect("unknown revision is environment (exit 2)",
               rc == 2 and "environment error" in err,
               f"rc={rc} out={out.strip()!r} err={err.strip()!r}")

        # 5..16 — one broken world per conjunct; each must be rejected.
        row4_sid, row4_client, _, row4_quote = FIX_ROWS[3]
        worlds = [
            (_world(scratch, drop_entry=True), "entry missing"),
            (_world(scratch, entry="\n".join(
                l for l in entry_text.splitlines() if not l.startswith("source:"))),
             "no source lines"),
            (_world(scratch, entry=entry_text.replace(
                f"source: {FIX_ROWS[4][0]} — {FIX_ROWS[4][1]} — {FIX_ROWS[4][2]} — `# Gate`\n", "")),
             "only 4 source lines"),
            (_world(scratch, entry=entry_text.replace(
                f"source: {FIX_ROWS[4][0]} — {FIX_ROWS[4][1]}",
                f"source: {FIX_ROWS[0][0]} — {FIX_ROWS[0][1]}")),
             "duplicate id in source lines"),
            (_world(scratch, entry=entry_text.replace(FIX_ROWS[1][0], "S999")),
             "id does not resolve"),
            (_world(scratch, sources="\n".join(
                (l.replace("| mined |", "| queued |", 1)
                 if l.startswith(f"| {FIX_ROWS[2][0]} |") else l)
                for l in sources_text.splitlines())),
             "row not mined"),
            (_world(scratch, entry=entry_text.replace(
                f" — {FIX_ROWS[3][2]} — `# Gate`", " — `# Gate`")),
             "source cell absent from the entry's source line"),
            (_world(scratch, sources=sources_text.replace(
                FIX_ROWS[3][3], "A different sentence entirely.")),
             "quote not in the anchor cell"),
            (_world(scratch, entry=entry_text.replace(
                _table_row(row4_sid, row4_client, row4_quote),
                f"| {row4_client} client | gate {row4_sid} applies | (quote elided) | (id elided) |")),
             "id and quote not in a per-client table row"),
            (_world(scratch, entry=entry_text.replace(
                f"verified-at: {VERIFIED_AT}", "verified-at: 2020-01-01")),
             "no verified-at"),
            (_world(scratch, entry=entry_text.replace(
                "recheck: 90d — re-fetch each cited page and confirm the located quotes still read the same",
                "note: re-fetch")),
             "no recheck"),
            (_world(scratch, readme=readme_text.replace(
                "`knowledge/client-trust-gates-round68.md`", "`knowledge/absent.md`")),
             "no coverage-map row"),
        ]
        for world, name in worlds:
            n, fs = check(_state_of(world))
            expect(f"broken world rejected: {name}",
                   n != TOTAL, f"backed {n}, findings={fs}")
    finally:
        shutil.rmtree(scratch, ignore_errors=True)
        for world, _ in worlds:
            shutil.rmtree(world, ignore_errors=True)

    print(f"self-test: {failures} failure(s) over {assertions} assertions")
    return 1 if failures else 0


# --- entry point ------------------------------------------------------------


def _default_repo() -> Path:
    here = Path(__file__).resolve()
    for cand in here.parents:
        if (cand / "corpus" / "SOURCES.md").is_file():
            return cand
    return Path.cwd()


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(add_help=True)
    ap.add_argument("--rev", default=None, help="measured revision (full sha)")
    ap.add_argument("--repo", default=None,
                    help="lane root (default: nearest ancestor holding corpus/SOURCES.md)")
    ap.add_argument("--fetch", action="store_true",
                    help="also re-open each cited URL and locate its quote on the live page")
    ap.add_argument("--self-test", action="store_true")
    args = ap.parse_args(argv)
    repo = Path(args.repo) if args.repo else _default_repo()
    if args.self_test:
        return selftest(repo)
    try:
        state = _load(repo, args.rev)
        n, findings = check(state)
    except EnvError as exc:
        print(f"environment error: {exc}", file=sys.stderr)
        return 2
    print(f"client trust gates backed {n} of {TOTAL}")
    for f in findings:
        print(f"  - {f}")
    if args.fetch:
        try:
            for line in fetch_report(state):
                print(line)
        except EnvError as exc:
            print(f"environment error: {exc}", file=sys.stderr)
            return 2
    return 0 if n == TOTAL else 1


if __name__ == "__main__":
    sys.exit(main())
