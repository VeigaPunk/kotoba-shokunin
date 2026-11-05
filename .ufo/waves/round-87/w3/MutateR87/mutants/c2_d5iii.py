#!/usr/bin/env python3
"""Round-87 counter for the five defects the round-86 non-author closure routed.

Frozen predicate (plans/round-87.md § C2, carried verbatim):

    python3 -B verifiers/check_r86_routed_repairs.py --rev <rev>
        -> prints "r86 routed defects closed N of 5", exit 0 iff N == 5;
           exit 1 otherwise; exit 2 = could-not-evaluate.

Items D1-D5 are `corpus/lessons/round-86-verifier-spotcheck.md` § 6.1-6.4 and
§ 6.7.  Every item is recomputed from `<rev>`'s committed bytes (`git show`,
`git rev-parse <rev>:<path>`, one scratch clone) and never from the worktree
(Q58).

D1 — tip after-values carry a committed receipt (r86 § 6.1; the r85 D2
    recurrence).  `.ufo/waves/round-86/receipts/tip-catalogue.txt` and
    `tip-registry.txt` exist at `<rev>`; each names the revision it measured,
    carries `exit=0` and its expected line (`omp catalogue lines reproduced
    215 of 215` / `gate registry rows conformant 67 of 67`); and the blobs of
    `verifiers/check_omp_catalogue_repro.py` and `verifiers/check_gate_registry.py`
    are equal between the r86 landing commit `04647b0f...` and `<rev>`, so the
    reading carries forward.
    "Names the measured revision" is read mechanically: the receipt carries a
    7-40 hex token that resolves to a commit which is an ancestor of `<rev>`
    AND whose two instrument blobs equal `<rev>`'s.  That is exactly the
    carry-forward clause applied to the named revision, so the honest shape
    (a receipt committed this round naming the r86 tip it re-measured) passes
    while `w_wrongrev` (a receipt naming a sibling or foreign revision) stays
    red.

D2 — the planner-seat reason is cited, not asserted (r86 § 6.2).  The lane
    record (`plans/round-87.md` or `corpus/lessons/round-87.md`) carries the
    validator's own sentence verbatim —

        planner/distiller/labrat/Main are frozen-topology seats and can never
        be swarm lanes.

    (one sentence, joined above for the 79-column docstring) — and the counter
    re-reads `~/Projects/ufo-fsd-alpha/scripts/ufo-swarm-wave.mjs` (exit 2 if
    absent), confirms the sentence occurs there and that the `SWARM_ROLES` set
    literal does not contain `planner` (the literal is parsed, never grepped as
    a substring).  Both carriers wrap prose at ~78 columns, so the comparison
    collapses runs of whitespace and drops backticks before matching: the word
    sequence must be verbatim, the line breaks need not be.  In the validator
    the sentence spans two `//` comment lines, so its comments are read with
    their markers stripped (a verbatim whole-source occurrence also counts).

D3 — the lesson's `## Gate` carries a reject row (r86 § 6.3).
    `corpus/lessons/round-87.md` `## Gate` holds >= 1 row whose decision cell
    is `reject` with a reason of >= 8 words.  A row is a `|`-delimited table
    row (decision cell named by the header, or a cell whose whole value is
    `reject`) or a list item carrying the standalone token `reject`; the reason
    is the header-named reason column when the table names one, else the row's
    longest non-decision cell.  A paragraph mention ("we rejected three
    candidates") is not a row — `rejected` never matches `reject` as a whole
    token, and prose is not scanned for cells.

D4 — the kill rule names the data boundary (r86 § 6.4): `plans/round-87.md`
    contains `after the first candidate score` verbatim.

D5 — the carried base red is carried HONESTLY (r86 § 6.7, redefined by
    `plans/round-87-addendum-2.md` A2.1 before any candidate score; the frozen
    "gate exits 0" form is unsatisfiable by honest lane work and invited
    laundering).  Four conjuncts at `<rev>`:
      (i)   `corpus/lessons/round-86-verifier-spotcheck.md` blob equals its
            blob at base `223ae62` (a non-author record is never rewritten);
      (ii)  `corpus/lessons/round-81.md` blob equals its blob at base (a
            historical lesson is never rewritten to green a gate — Q64);
      (iii) `<rev>`'s own `verifiers/verify_corpus_integrity.py --json`, run
            IN THE LANE WORKTREE with the worktree tip pinned to `<rev>`
            (addendum 1 A1.2, Q63: the tracked `.ufo/reports/round-76/kotoba.md`
            symlink dangles in any clone), prints `7/9 checks pass` with
            `corpus.pointers.report_dead 1` detailing
            `corpus/lessons/round-86-verifier-spotcheck.md:33` and
            `corpus.pointers.commit_unresolvable 1` detailing
            `corpus/lessons/round-81.md:8`, every other check PASS;
      (iv)  `corpus/lessons/round-87.md` names both remaining DRIFTs with their
            `file:line` and the Q64 disposition `left red and disclosed`.
    A worktree tip that differs from `<rev>` is exit 2, never a pass.

Usage: check_r86_routed_repairs.py --rev REV [--repo DIR] [--work DIR]
       check_r86_routed_repairs.py --self-test
Exit 0 clean (5 of 5), 1 a check fails, 2 could not evaluate.
"""
from __future__ import annotations

import argparse
import contextlib
import io
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

LANE = Path(__file__).resolve().parent.parent
TARGET = 5

LANDING_REV = "04647b0f715ff3c4f314b0d8f03dea28bc453688"
BASE_REV = "223ae62424f8ab1eb365d733eb648d6228ddd7e8"
CATALOGUE_RECEIPT = ".ufo/waves/round-86/receipts/tip-catalogue.txt"
REGISTRY_RECEIPT = ".ufo/waves/round-86/receipts/tip-registry.txt"
CATALOGUE_LINE = "omp catalogue lines reproduced 215 of 215"
REGISTRY_LINE = "gate registry rows conformant 67 of 67"
INSTRUMENTS = ("verifiers/check_omp_catalogue_repro.py",
               "verifiers/check_gate_registry.py")

PLAN = "plans/round-87.md"
LESSON = "corpus/lessons/round-87.md"
INTEGRITY = "verifiers/verify_corpus_integrity.py"
INTEGRITY_LINE = "7/9 checks pass"

FROZEN_SENTENCE = ("planner/distiller/labrat/Main are frozen-topology seats "
                   "and can never be swarm lanes.")
KILL_BOUNDARY = "after the first candidate score"
OMP_VALIDATOR = Path(os.path.expanduser(
    "~/Projects/ufo-fsd-alpha/scripts/ufo-swarm-wave.mjs"))

MIN_READER = 7          # shortest hex token that can name a revision
MIN_REASON_WORDS = 8
GIT_TIMEOUT = 300


class Unevaluable(Exception):
    """The counter cannot reach a verdict (exit 2)."""


# --- git plumbing --------------------------------------------------------

def _git(repo: Path, *args: str) -> subprocess.CompletedProcess:
    try:
        return subprocess.run(["git", "-C", str(repo), *args],
                              capture_output=True, text=True,
                              timeout=GIT_TIMEOUT)
    except (OSError, subprocess.SubprocessError) as exc:
        raise Unevaluable("git %s: %s" % (" ".join(args[:2]), exc)) from exc


def _show(repo: Path, rev: str, path: str) -> str | None:
    proc = _git(repo, "show", "%s:%s" % (rev, path))
    return proc.stdout if proc.returncode == 0 else None


def _blob_id(repo: Path, rev: str, path: str) -> str | None:
    proc = _git(repo, "rev-parse", "--verify", "-q", "%s:%s" % (rev, path))
    return proc.stdout.strip() if proc.returncode == 0 else None


def _resolve(repo: Path, rev: str) -> str:
    proc = _git(repo, "rev-parse", "--verify", "-q", "%s^{commit}" % rev)
    if proc.returncode != 0:
        raise Unevaluable("revision %r does not resolve to a commit" % rev)
    return proc.stdout.strip()


# --- text model ----------------------------------------------------------

def _norm(text: str) -> str:
    """Collapse whitespace runs and drop backticks: the lane's records wrap
    prose at ~78 columns and quote the frozen sentences in backticks, so the
    word sequence is what must be verbatim, not the line breaks."""
    return re.sub(r"\s+", " ", text.replace("`", ""))


def _words(text: str) -> int:
    return sum(1 for tok in text.split() if re.search(r"[0-9A-Za-z]", tok))


def _carries_sentence(text: str) -> bool:
    return FROZEN_SENTENCE in _norm(text)


def _section(text: str, name: str) -> str | None:
    """Body of a level-2 section, up to the next level-1/2 heading."""
    lines = text.splitlines()
    start = None
    for i, line in enumerate(lines):
        if re.match(r"^##\s+%s\b" % re.escape(name), line):
            start = i + 1
            break
    if start is None:
        return None
    body = []
    for line in lines[start:]:
        if re.match(r"^#{1,2}\s", line):
            break
        body.append(line)
    return "\n".join(body)


def _table(section: str) -> tuple[list[str] | None, list[list[str]]]:
    header: list[str] | None = None
    rows: list[list[str]] = []
    for line in section.splitlines():
        s = line.strip()
        if not s.startswith("|"):
            continue
        cells = [c.strip() for c in s.strip("|").split("|")]
        if cells and all(not c or re.match(r"^:?-{2,}:?$", c) for c in cells):
            continue                                  # separator row
        if header is None:
            header = cells
            continue
        rows.append(cells)
    return header, rows


def _column(header: list[str] | None, *names: str) -> int | None:
    if not header:
        return None
    for i, cell in enumerate(header):
        low = _norm(cell).lower()
        if any(name in low for name in names):
            return i
    return None


def _decision(cell: str) -> bool:
    return _norm(cell).strip(" *_").lower() == "reject"


def reject_reasons(section: str) -> list[str]:
    """Reason text of every `reject` row in a `## Gate` section body."""
    header, rows = _table(section)
    didx = _column(header, "decision", "verdict")
    ridx = _column(header, "reason")
    reasons: list[str] = []

    def reason_of(cells: list[str], idx: int) -> str:
        if ridx is not None and ridx < len(cells) and ridx != idx:
            return cells[ridx]
        others = [c for j, c in enumerate(cells) if j != idx and c]
        return max(others, key=_words) if others else ""

    for cells in rows:
        if didx is not None and didx < len(cells):
            if _decision(cells[didx]):
                reasons.append(reason_of(cells, didx))
            continue
        for i, cell in enumerate(cells):
            if _decision(cell):
                reasons.append(reason_of(cells, i))
                break

    for line in section.splitlines():
        if not re.match(r"^\s*[-*+]\s", line):
            continue
        if not re.search(r"\breject\b", line, re.I):
            continue
        tail = re.split(r"\breject\b", line, flags=re.I)[-1]
        reasons.append(tail.strip(" \t\u2014\u2013-:|*`"))
    return reasons


def swarm_roles(src: str) -> list[str] | None:
    """Members of the `SWARM_ROLES` set literal, or None if it cannot be
    parsed (the set is parsed, never grepped for a substring)."""
    match = re.search(r"SWARM_ROLES\s*=\s*new\s+Set\(\s*\[(.*?)\]", src, re.S)
    if not match:
        return None
    roles = re.findall(r"""["'`]([^"'`]+)["'`]""", match.group(1))
    return roles or None


def js_comment_text(src: str) -> str:
    """Line and block comments with their markers stripped, joined: a sentence
    the source wraps over two comment lines still occurs here."""
    out: list[str] = []
    for match in re.finditer(r"/\*.*?\*/", src, re.S):
        out.append(re.sub(r"^\s*\*+", " ", match.group(0), flags=re.M))
    for line in src.splitlines():
        match = re.match(r"^\s*//(.*)$", line)
        if match:
            out.append(match.group(1))
    return "\n".join(out)


# --- D1 ------------------------------------------------------------------

def receipt_verdict(repo: Path, text: str, expected: str,
                    rev_full: str) -> tuple[bool, str]:
    if not re.search(r"\bexit\s*=\s*0\b", text):
        return False, "carries no exit=0"
    if expected not in text:
        return False, "carries no %r" % expected
    named = _named_rev(repo, text, rev_full)
    if named is None:
        return False, ("names no revision that resolves, is an ancestor of "
                       "<rev> and carries the same instruments")
    return True, "measured rev %s" % named


def _named_rev(repo: Path, text: str, rev_full: str) -> str | None:
    seen: list[str] = []
    for token in re.findall(r"\b[0-9a-f]{%d,40}\b" % MIN_READER, text):
        if token in seen:
            continue
        seen.append(token)
        if len(seen) > 60:
            break
        proc = _git(repo, "rev-parse", "--verify", "-q", "%s^{commit}" % token)
        if proc.returncode != 0:
            continue
        full = proc.stdout.strip()
        if full != rev_full:
            anc = _git(repo, "merge-base", "--is-ancestor", full, rev_full)
            if anc.returncode != 0:
                continue
        carries = True
        for path in INSTRUMENTS:
            if _blob_id(repo, full, path) != _blob_id(repo, rev_full, path):
                carries = False
                break
        if carries:
            return full
    return None


def check_d1(repo: Path, rev: str, work: Path, landing: str,
             validator: Path, base_rev: str) -> tuple[bool, str]:
    del work, validator, base_rev
    receipts = ((CATALOGUE_RECEIPT, CATALOGUE_LINE),
                (REGISTRY_RECEIPT, REGISTRY_LINE))
    for path, expected in receipts:
        text = _show(repo, rev, path)
        if text is None:
            return False, "%s absent at %s" % (path, rev[:12])
        ok, why = receipt_verdict(repo, text, expected, rev)
        if not ok:
            return False, "%s: %s" % (Path(path).name, why)
    for path in INSTRUMENTS:
        old = _blob_id(repo, landing, path)
        if old is None:
            raise Unevaluable("landing commit %s has no %s" % (landing[:12], path))
        new = _blob_id(repo, rev, path)
        if new is None:
            return False, "%s absent at %s" % (path, rev[:12])
        if old != new:
            return False, ("%s differs between %s and %s"
                           % (path, landing[:12], rev[:12]))
    return True, "two receipts carry exit=0; instruments equal %s..%s" % (
        landing[:8], rev[:8])


# --- D2 ------------------------------------------------------------------

def check_d2(repo: Path, rev: str, work: Path, landing: str,
             validator: Path, base_rev: str) -> tuple[bool, str]:
    del work, landing, base_rev
    carriers = [name for name in (PLAN, LESSON)
                if (text := _show(repo, rev, name)) is not None
                and _carries_sentence(text)]
    if not carriers:
        return False, ("no lane record (%s or %s) carries the validator "
                       "sentence verbatim" % (PLAN, LESSON))
    if not validator.is_file():
        raise Unevaluable("validator absent: %s" % validator)
    try:
        src = validator.read_text(encoding="utf-8", errors="replace")
    except OSError as exc:
        raise Unevaluable("validator unreadable: %s" % exc) from exc
    if not (_carries_sentence(js_comment_text(src)) or _carries_sentence(src)):
        return False, "the validator does not carry that sentence"
    roles = swarm_roles(src)
    if roles is None:
        raise Unevaluable("SWARM_ROLES set literal not parseable in %s"
                          % validator)
    if "planner" in roles:
        return False, "SWARM_ROLES contains planner"
    return True, "carried by %s; validator sentence present, %d roles, no planner" % (
        ", ".join(carriers), len(roles))


# --- D3 ------------------------------------------------------------------

def check_d3(repo: Path, rev: str, work: Path, landing: str,
             validator: Path, base_rev: str) -> tuple[bool, str]:
    del work, landing, validator, base_rev
    text = _show(repo, rev, LESSON)
    if text is None:
        return False, "%s absent at %s" % (LESSON, rev[:12])
    section = _section(text, "Gate")
    if section is None:
        return False, "%s has no '## Gate' section" % LESSON
    reasons = reject_reasons(section)
    if not reasons:
        return False, "## Gate holds no reject row"
    best = max(_words(r) for r in reasons)
    if best < MIN_REASON_WORDS:
        return False, ("reject row reason carries %d words (< %d)"
                       % (best, MIN_REASON_WORDS))
    return True, "%d reject row(s), longest reason %d words" % (
        len(reasons), best)


# --- D4 ------------------------------------------------------------------

def check_d4(repo: Path, rev: str, work: Path, landing: str,
             validator: Path, base_rev: str) -> tuple[bool, str]:
    del work, landing, validator, base_rev
    text = _show(repo, rev, PLAN)
    if text is None:
        return False, "%s absent at %s" % (PLAN, rev[:12])
    if KILL_BOUNDARY not in _norm(text):
        return False, "%s does not carry %r" % (PLAN, KILL_BOUNDARY)
    return True, "%s names the boundary %r" % (PLAN, KILL_BOUNDARY)


# --- D5 ------------------------------------------------------------------

SPOTCHECK = "corpus/lessons/round-86-verifier-spotcheck.md"
LESSON81 = "corpus/lessons/round-81.md"
LESSON87 = "corpus/lessons/round-87.md"
D5_DEAD_SITE = "corpus/lessons/round-86-verifier-spotcheck.md:33"
D5_UNRES_SITE = "corpus/lessons/round-81.md:8"
D5_DISPOSITION = "left red and disclosed"


def check_d5(repo: Path, rev: str, work: Path, landing: str,
             validator: Path, base_rev: str) -> tuple[bool, str]:
    del landing, validator, work
    # (i)+(ii) no non-author record and no historical lesson rewritten
    for path in (SPOTCHECK, LESSON81):
        base_blob = _blob_id(repo, base_rev, path)
        here = _blob_id(repo, rev, path)
        if base_blob is None or here is None:
            raise Unevaluable("%s unavailable at a measured revision" % path)
        if base_blob != here:
            return False, ("%s rewritten at %s (blob %s != base %s)"
                           % (path, rev[:12], here[:12], base_blob[:12]))
    # (iii) the revision's own gate, run in the lane worktree with the tip pinned
    tip = _git(repo, "rev-parse", "master").stdout.strip()
    if tip != rev:
        raise Unevaluable("worktree tip %s != measured revision %s "
                          "(plans/round-87-addendum-1.md A1.2)"
                          % (tip[:12], rev[:12]))
    script = repo / INTEGRITY
    if not script.is_file():
        raise Unevaluable("%s absent in the worktree" % INTEGRITY)
    try:
        run = subprocess.run([sys.executable, "-B", str(script), "--json"],
                             cwd=str(repo), capture_output=True, text=True,
                             timeout=GIT_TIMEOUT)
    except (OSError, subprocess.SubprocessError) as exc:
        raise Unevaluable("integrity run failed: %s" % exc) from exc
    if run.returncode not in (0, 1):
        raise Unevaluable("%s exit=%d: %s"
                          % (INTEGRITY, run.returncode,
                             (run.stdout + run.stderr).strip()[-200:]))
    try:
        doc = json.loads(run.stdout)
    except ValueError as exc:
        raise Unevaluable("%s --json did not parse: %s" % (INTEGRITY, exc)) from exc
    results = doc.get("results") or []
    if not results:
        raise Unevaluable("%s --json carries no results" % INTEGRITY)
    corpus = (doc.get("observed") or {}).get("corpus") or {}
    red = {r.get("check"): r for r in results if r.get("verdict") != "PASS"}
    want = {"corpus.pointers.report_dead", "corpus.pointers.commit_unresolvable"}
    if not set(red) <= want:
        return False, ("%s red set %s carries a check outside %s"
                       % (INTEGRITY, sorted(red), sorted(want)))
    dead = corpus.get("report_dead_detail") or []
    unres = corpus.get("commit_unresolvable_detail") or []
    if not any(line.startswith(D5_DEAD_SITE) for line in dead):
        return False, "report_dead detail %s does not name %s" % (dead, D5_DEAD_SITE)
    if not any(line.startswith(D5_UNRES_SITE) for line in unres):
        return False, "commit_unresolvable detail %s does not name %s" % (unres, D5_UNRES_SITE)
    passed = sum(1 for r in results if r.get("verdict") == "PASS")
    tally = "%d/%d checks pass" % (passed, len(results))
    if tally != INTEGRITY_LINE:
        return False, "%s tally %s, want %s" % (INTEGRITY, tally, INTEGRITY_LINE)
    # (iv) the disclosure is on the record
    lesson = _show(repo, rev, LESSON87)
    if lesson is None:
        return False, "%s absent at %s" % (LESSON87, rev[:12])
    body = _norm(lesson)
    missing = [site for site in (D5_DEAD_SITE, D5_UNRES_SITE) if site not in body]
    if missing or D5_DISPOSITION not in body:
        return False, ("%s does not carry %s and %r"
                       % (LESSON87, missing or "the two sites", D5_DISPOSITION))
    return True, ("%s %s, red exactly the two disclosed DRIFTs (%s, %s), %s; "
                  "non-author records unchanged from base %s"
                  % (INTEGRITY, tally, D5_DEAD_SITE, D5_UNRES_SITE,
                     D5_DISPOSITION, base_rev[:8]))


# --- driver --------------------------------------------------------------

ITEMS = (("d1", check_d1), ("d2", check_d2), ("d3", check_d3),
         ("d4", check_d4), ("d5", check_d5))


def main(argv: list[str] | None = None, *, landing_rev: str = LANDING_REV,
         validator_path: Path = OMP_VALIDATOR,
         base_rev: str = BASE_REV) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--rev", help="lane revision to check")
    ap.add_argument("--repo", default=str(LANE), help="lane repository")
    ap.add_argument("--work", help="scratch parent directory (default: $TMPDIR)")
    ap.add_argument("--self-test", action="store_true",
                    help="run the fixture self-test")
    args = ap.parse_args(argv)
    if args.self_test:
        return self_test()
    if not args.rev:
        ap.error("--rev is required unless --self-test is selected")

    repo = Path(args.repo)
    if not repo.is_dir():
        print("could-not-evaluate: repo not found: %s" % repo, file=sys.stderr)
        return 2
    parent = (Path(args.work) if args.work
              else Path(os.environ.get("TMPDIR") or tempfile.gettempdir()))
    try:
        parent.mkdir(parents=True, exist_ok=True)
        work = Path(tempfile.mkdtemp(prefix="r86-repairs-", dir=str(parent)))
    except OSError as exc:
        print("could-not-evaluate: scratch dir: %s" % exc, file=sys.stderr)
        return 2

    rows: list[tuple[str, bool, str]] = []
    try:
        rev = _resolve(repo, args.rev)
        for cid, check in ITEMS:
            ok, detail = check(repo, rev, work, landing_rev,
                               Path(validator_path), base_rev)
            rows.append((cid, ok, detail))
    except Unevaluable as exc:
        print("could-not-evaluate: %s" % exc, file=sys.stderr)
        return 2
    finally:
        shutil.rmtree(work, ignore_errors=True)

    for cid, ok, detail in rows:
        print("%s %-3s %s" % ("PASS" if ok else "FAIL", cid, detail))
    score = sum(1 for _cid, ok, _detail in rows if ok)
    print("r86 routed defects closed %d of %d" % (score, TARGET))
    return 0 if score == TARGET else 1


# --- self-test -----------------------------------------------------------

FIXTURE_INSTRUMENT = "#!/usr/bin/env python3\nprint('instrument')\n"
FIXTURE_INSTRUMENT_V2 = "#!/usr/bin/env python3\nprint('instrument v2')\n"

# The fixture gate prints the `--json` shape the counter reads (D5 (iii)).
# A committed `GATE` marker selects the shape, so a world changes the gate's
# VERDICT without changing the gate's BYTES — exactly the shape the honest
# repair has (the two protected records are never rewritten).
FIXTURE_INTEGRITY_JSON = """#!/usr/bin/env python3
\"\"\"fixture corpus gate: the --json shape check_d5 reads.\"\"\"
import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
MARKER = ROOT / "GATE"
MODE = MARKER.read_text().strip() if MARKER.is_file() else "base"
CHECKS = (
    "corpus.index.tracked_files",
    "corpus.index.unindexed",
    "corpus.index.stale_patterns",
    "corpus.index.missing_paths",
    "corpus.pointers.report_total",
    "corpus.pointers.report_dead",
    "corpus.pointers.commit_total",
    "corpus.pointers.commit_unresolvable",
    "corpus.pointers.commit_nonhash",
)
if MODE == "honest":
    RED = {
        "corpus.pointers.report_dead":
            "corpus/lessons/round-86-verifier-spotcheck.md:33: "
            "../../.ufo/reports/round-84/kama.md",
        "corpus.pointers.commit_unresolvable":
            "corpus/lessons/round-81.md:8: "
            "8b1cc1b00a9322cd8e231d87e015e1d75d20adc1",
    }
else:
    RED = {name: "drift" for name in (
        "corpus.index.tracked_files",
        "corpus.index.unindexed",
        "corpus.pointers.report_total",
        "corpus.pointers.report_dead",
        "corpus.pointers.commit_total",
        "corpus.pointers.commit_unresolvable",
    )}
RESULTS = [{"check": name, "mode": "zero", "observed": 0,
            "verdict": "DRIFT" if name in RED else "PASS"} for name in CHECKS]
OBSERVED = {"corpus": {
    "report_dead_detail": [RED["corpus.pointers.report_dead"]]
        if "corpus.pointers.report_dead" in RED else [],
    "commit_unresolvable_detail": [RED["corpus.pointers.commit_unresolvable"]]
        if "corpus.pointers.commit_unresolvable" in RED else [],
}}
print(json.dumps({"observed": OBSERVED, "results": RESULTS}, indent=2))
raise SystemExit(1 if RED else 0)
"""
FIXTURE_INTEGRITY_JSON_V2 = FIXTURE_INTEGRITY_JSON.replace(
    '\"\"\"fixture corpus gate: the --json shape check_d5 reads.\"\"\"',
    '\"\"\"fixture corpus gate, rewritten this round.\"\"\"')
FIXTURE_INTEGRITY_SILENT = ("#!/usr/bin/env python3\n"
                            "raise SystemExit(0)\n")

FIXTURE_VALIDATOR = (
    "// Swarm lanes are the ten proposal roles. planner/distiller/labrat/Main are\n"
    "// frozen-topology seats and can never be swarm lanes.\n"
    "export const SWARM_ROLES = new Set([\n"
    '  "scout",\n'
    '  "executor",\n'
    '  "scribe",\n'
    "]);\n")
FIXTURE_VALIDATOR_PLANNER = FIXTURE_VALIDATOR.replace(
    '  "scribe",\n', '  "scribe",\n  "planner",\n')
FIXTURE_VALIDATOR_NOSENTENCE = (
    "// Swarm lanes are the ten proposal roles, collected elsewhere.\n"
    "export const SWARM_ROLES = new Set([\n"
    '  "scout",\n'
    '  "executor",\n'
    "]);\n")
FIXTURE_VALIDATOR_BROKEN = (
    "// planner/distiller/labrat/Main are frozen-topology seats and can never\n"
    "// be swarm lanes.\n"
    "export const SWARM_ROLES = collectRoles();\n")

FIXTURE_SPOTCHECK = """# kotoba round 86 - verifier spot-check (fixture, non-author record)

Closure judge: fixture. Base -> lane tip.

## 1. Conformance results

| Check | Observed | Result |
|---|---|---|
| Report committed | fixture | PASS |
| Lane pushed | fixture | PASS |

## 2. Claim re-check

Fixture body, kept byte-identical across every world: PROTOCOL.md forbids
editing a non-author record.

## 6. Routed defects

7. Carried base reds: the fleet-root artifact
   `.ufo/reports/round-84/kama.md` carries no `## SHONEN` marker, so the
   citation on line 33 stays dead here.
"""

FIXTURE_SPOTCHECK_LAUNDERED = FIXTURE_SPOTCHECK.replace(
    "`.ufo/reports/round-84/kama.md`", '".ufo/reports/round-84/kama.md"')

FIXTURE_LESSON81 = """# kotoba round 81 - lesson (fixture, historical)

## 1. What the round measured

Fixture body, kept byte-identical across every world: QUALITY Q64 forbids
rewriting a historical lesson to green a gate.

## 2. Evidence

| Item | Pointer |
|---|---|
| measurement | `receipts/round-81.txt` |
| test-world commit | 8b1cc1b00a9322cd8e231d87e015e1d75d20adc1 |

## 3. Note

The test-world commit above resolves in neither the lane nor the fleet by
design: it is a recorded absence, left red and disclosed.
"""

D5_DISCLOSURE = """
## Carried reds

The gate carries two DRIFTs, at `corpus/lessons/round-86-verifier-spotcheck.md:33`
and `corpus/lessons/round-81.md:8`; both are left red and disclosed (Q64), never
rewritten to green a gate.
"""

FIXTURE_GATE_TABLE = """## Gate

| candidate | decision | reason |
|---|---|---|
| ReviewerRoots row 3 | reject | the quote is a doc string line, not a code reader, so it cannot ground the plugin root |
| K3 world | admit | the world stays red under the amended counter |
"""

FIXTURE_GATE_PROSE = """## Gate

We rejected three candidates this round (ReviewerRoots rows 1, 8 and 9), each
for a reason the seat reports record; no table row is supplied here.
"""

FIXTURE_LESSON_HONEST = ("# kotoba round 87\n\n" + FIXTURE_GATE_TABLE
                         + D5_DISCLOSURE
                         + "\n## Mistakes\n\n- class · evidence · captured-by · fix\n")

FIXTURE_LESSON_PROSE = ("# kotoba round 87\n\n" + FIXTURE_GATE_PROSE
                        + "\n## Mistakes\n\n- class · evidence · captured-by · fix\n")

FIXTURE_LESSON_GATEPROSE = ("# kotoba round 87\n\n" + FIXTURE_GATE_PROSE
                            + D5_DISCLOSURE)

FIXTURE_LESSON_NODISCLOSURE = ("# kotoba round 87\n\n" + FIXTURE_GATE_TABLE
                               + "\n## Mistakes\n\n- class · evidence · captured-by · fix\n")

FIXTURE_LESSON_SHORT_REASON = """# kotoba round 87

## Gate

| candidate | decision | reason |
|---|---|---|
| ReviewerRoots row 3 | reject | doc quote only |
"""

FIXTURE_PLAN_HONEST = """# kotoba round 87

## C2

- **D2** the lane's record carries the validator's own sentence verbatim —
  `planner/distiller/labrat/Main are frozen-topology seats and can never be
  swarm lanes.` — and the counter re-reads the validator.

## Kill rule

A counter, its ledger or its pins changed after the first candidate score
kills that claim.
"""

FIXTURE_PLAN_PROSE = """# kotoba round 87

## C2

- D1 the tip receipts were committed.
- D2 the planner reason is cited.
- D3 the gate records a reject row.
- D4 the kill rule was reworded.
- D5 the pointer is repaired.

## Kill rule

A counter, its ledger or its pins changed after this freeze kills the claim.
"""

FIXTURE_PLAN_OLD_KILL = FIXTURE_PLAN_HONEST.replace(
    "after the first candidate score", "after this freeze")


def _receipt(token: str, line: str) -> str:
    return ("# tip re-measure (r85 D2: an after-value quoted at a revision "
            "has a receipt at that revision)\n"
            "$ python3 -B verifiers/check_omp_catalogue_repro.py --rev %s\n"
            "%s\n"
            "exit=0\n" % (token, line))


def _fixture_commit(repo: Path, message: str, files: dict[str, str]) -> str:
    for rel, body in files.items():
        path = repo / rel
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(body, encoding="utf-8")
    for args in (("add", "-A"),
                 ("-c", "user.name=probe", "-c",
                  "user.email=probe@example.invalid", "commit", "-q", "-m",
                  message)):
        proc = _git(repo, *args)
        if proc.returncode != 0:
            raise RuntimeError("fixture git %s: %s"
                               % (args[0], proc.stderr.strip()[-200:]))
    return _git(repo, "rev-parse", "HEAD").stdout.strip()


def self_test() -> int:
    failures: list[str] = []
    assertions = 0

    def check(label: str, ok: bool, detail: str = "") -> None:
        nonlocal assertions
        assertions += 1
        if not ok:
            failures.append("%s%s" % (label, (": " + detail) if detail else ""))

    # --- pure functions: the text model --------------------------------
    check("frozen sentence carried across a wrapped record line",
          _carries_sentence(FIXTURE_PLAN_HONEST))
    check("frozen sentence not carried by the prose plan",
          not _carries_sentence(FIXTURE_PLAN_PROSE))
    check("frozen sentence carried by two joined comment lines",
          _carries_sentence(js_comment_text(FIXTURE_VALIDATOR)))
    check("frozen sentence absent from a validator without it",
          not _carries_sentence(js_comment_text(FIXTURE_VALIDATOR_NOSENTENCE)))
    check("frozen sentence carried across two comment lines of a broken file",
          _carries_sentence(js_comment_text(FIXTURE_VALIDATOR_BROKEN)))
    check("frozen sentence carried as one contiguous source line",
          _carries_sentence("// %s\n" % FROZEN_SENTENCE))
    check("SWARM_ROLES literal parsed without planner",
          swarm_roles(FIXTURE_VALIDATOR) == ["scout", "executor", "scribe"])
    check("SWARM_ROLES literal parsed with planner",
          "planner" in (swarm_roles(FIXTURE_VALIDATOR_PLANNER) or []))
    check("unparseable SWARM_ROLES yields None",
          swarm_roles(FIXTURE_VALIDATOR_BROKEN) is None)
    check("planner as a substring outside the literal is not a member",
          "planner" not in (swarm_roles(
              "// planner is frozen\n" + FIXTURE_VALIDATOR) or []))

    gate_honest = _section(FIXTURE_LESSON_HONEST, "Gate") or ""
    gate_prose = _section(FIXTURE_LESSON_PROSE, "Gate") or ""
    gate_short = _section(FIXTURE_LESSON_SHORT_REASON, "Gate") or ""
    honest_reasons = reject_reasons(gate_honest)
    check("honest gate yields one reject row with >= 8 words",
          len(honest_reasons) == 1
          and _words(honest_reasons[0]) >= MIN_REASON_WORDS,
          repr(honest_reasons))
    check("prose 'rejected' mention is not a row",
          reject_reasons(gate_prose) == [])
    check("a 3-word reject reason is rejected",
          bool(reject_reasons(gate_short))
          and max(_words(r) for r in reject_reasons(gate_short))
          < MIN_REASON_WORDS)
    check("a reject bullet carries its reason",
          any(_words(r) >= MIN_REASON_WORDS for r in reject_reasons(
              "- **ReviewerRoots row 3** — reject — the quote is a doc "
              "string line, not a code reader, so it cannot ground the root\n")))
    check("kill boundary accepted in the honest plan",
          KILL_BOUNDARY in _norm(FIXTURE_PLAN_HONEST))
    check("old kill wording refused",
          KILL_BOUNDARY not in _norm(FIXTURE_PLAN_OLD_KILL))

    # --- worlds in a temporary git repository --------------------------
    with tempfile.TemporaryDirectory(prefix="r86-repairs-fixture-") as tdir:
        repo = Path(tdir) / "lane"
        repo.mkdir()
        if _git(repo, "init", "-q", "-b", "master").returncode != 0:
            _git(repo, "init", "-q")
        work = Path(tdir) / "work"
        work.mkdir()

        def score(rev: str, validator: Path) -> tuple[int, str, str]:
            out, err = io.StringIO(), io.StringIO()
            with contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
                rc = main(["--rev", rev, "--repo", str(repo),
                           "--work", str(work)],
                          landing_rev=prose_rev, validator_path=validator,
                          base_rev=prose_rev)
            return rc, out.getvalue(), err.getvalue()

        def line(text: str) -> str:
            match = re.search(r"^r86 routed defects closed (\d+) of 5$",
                              text, re.M)
            return match.group(1) if match else "missing"

        # base world: the five items in prose only; the gate is the base shape
        # (3/9, six DRIFTs) and the two protected records are at their base bytes
        prose_rev = _fixture_commit(repo, "prose world", {
            "verifiers/check_omp_catalogue_repro.py": FIXTURE_INSTRUMENT,
            "verifiers/check_gate_registry.py": FIXTURE_INSTRUMENT,
            "verifiers/verify_corpus_integrity.py": FIXTURE_INTEGRITY_JSON,
            "GATE": "base\n",
            PLAN: FIXTURE_PLAN_PROSE,
            LESSON: FIXTURE_LESSON_PROSE,
            SPOTCHECK: FIXTURE_SPOTCHECK,
            LESSON81: FIXTURE_LESSON81,
        })
        check("fixture toplevel is the fixture",
              Path(_git(repo, "rev-parse", "--show-toplevel").stdout.strip())
              .resolve() == repo.resolve())
        check("fixture branch tip is the measured revision",
              _git(repo, "rev-parse", "master").stdout.strip() == prose_rev)

        rc, out, err = score(prose_rev, OMP_VALIDATOR)
        check("prose world exits 1", rc == 1,
              "rc %d err %r" % (rc, err.strip()[-200:]))
        check("prose world reads 0 of 5", line(out) == "0", out.strip()[:240])
        check("prose world fails every item",
              all(("FAIL %s" % cid) in out
                  for cid in ("d1", "d2", "d3", "d4", "d5")),
              out.strip()[:240])

        # a sibling commit the honest receipts must not be able to cite
        _git(repo, "checkout", "-q", "-b", "side")
        side_rev = _fixture_commit(repo, "side world", {"SIDE.md": "side\n"})
        _git(repo, "checkout", "-q", "master")

        # honest world: the four repairs, the carried red, the disclosure
        honest_rev = _fixture_commit(repo, "honest world", {
            "GATE": "honest\n",
            PLAN: FIXTURE_PLAN_HONEST,
            LESSON: FIXTURE_LESSON_HONEST,
            CATALOGUE_RECEIPT: _receipt(prose_rev, CATALOGUE_LINE),
            REGISTRY_RECEIPT: _receipt(prose_rev, REGISTRY_LINE),
        })
        rc, out, err = score(honest_rev, OMP_VALIDATOR)
        check("honest world exits 0", rc == 0,
              "rc %d err %r" % (rc, err.strip()[-200:]))
        check("honest world prints 5 of 5", line(out) == "5", out.strip()[:240])
        check("honest world prints the frozen summary line",
              "r86 routed defects closed 5 of 5" in out)
        check("honest world names the two disclosed DRIFTs",
              D5_DEAD_SITE in out and D5_UNRES_SITE in out, out.strip()[:240])

        # w_wrongrev: receipts naming a sibling revision
        wrongrev_rev = _fixture_commit(repo, "wrongrev world", {
            CATALOGUE_RECEIPT: _receipt(side_rev, CATALOGUE_LINE),
            REGISTRY_RECEIPT: _receipt(side_rev, REGISTRY_LINE),
        })
        rc, out, err = score(wrongrev_rev, OMP_VALIDATOR)
        check("w_wrongrev exits 1", rc == 1, "rc %d" % rc)
        check("w_wrongrev reads 4 of 5", line(out) == "4", out.strip()[:200])
        check("w_wrongrev names d1", "FAIL d1" in out, out.strip()[:200])

        # w_gateprose: a 'rejected' mention inside a paragraph (the disclosure
        # is present, so only D3 is red)
        gateprose_rev = _fixture_commit(repo, "gateprose world", {
            CATALOGUE_RECEIPT: _receipt(prose_rev, CATALOGUE_LINE),
            REGISTRY_RECEIPT: _receipt(prose_rev, REGISTRY_LINE),
            LESSON: FIXTURE_LESSON_GATEPROSE,
        })
        rc, out, err = score(gateprose_rev, OMP_VALIDATOR)
        check("w_gateprose exits 1", rc == 1, "rc %d" % rc)
        check("w_gateprose reads 4 of 5", line(out) == "4", out.strip()[:200])
        check("w_gateprose names d3", "FAIL d3" in out, out.strip()[:200])

        # w_norepair: the gate still reads the base shape (3/9)
        norepair_rev = _fixture_commit(repo, "norepair world", {
            LESSON: FIXTURE_LESSON_HONEST,
            "GATE": "base\n",
        })
        rc, out, err = score(norepair_rev, OMP_VALIDATOR)
        check("w_norepair exits 1", rc == 1, "rc %d" % rc)
        check("w_norepair reads 4 of 5", line(out) == "4", out.strip()[:200])
        check("w_norepair names d5", "FAIL d5" in out, out.strip()[:200])
        check("w_norepair's d5 detail names the red set",
              "red set" in out, out.strip()[:240])

        # an exit-0 verifier that prints nothing cannot be evaluated
        silent_rev = _fixture_commit(repo, "silent integrity world", {
            "verifiers/verify_corpus_integrity.py": FIXTURE_INTEGRITY_SILENT,
        })
        rc, out, err = score(silent_rev, OMP_VALIDATOR)
        check("a silent exit-0 verifier is could-not-evaluate",
              rc == 2 and line(out) == "missing"
              and "did not parse" in err,
              "rc %d err %r" % (rc, err.strip()[:160]))

        # the instruments drift between the landing commit and <rev>
        drift_rev = _fixture_commit(repo, "instrument drift world", {
            "verifiers/verify_corpus_integrity.py": FIXTURE_INTEGRITY_JSON,
            "verifiers/check_gate_registry.py": FIXTURE_INSTRUMENT_V2,
            "GATE": "honest\n",
        })
        rc, out, err = score(drift_rev, OMP_VALIDATOR)
        check("instrument drift reads 4 of 5",
              rc == 1 and line(out) == "4" and "FAIL d1" in out,
              out.strip()[:200])

        # a receipt without exit=0
        noexit_rev = _fixture_commit(repo, "no exit world", {
            "verifiers/check_gate_registry.py": FIXTURE_INSTRUMENT,
            CATALOGUE_RECEIPT: _receipt(prose_rev, CATALOGUE_LINE).replace(
                "exit=0", "exit=1"),
        })
        rc, out, err = score(noexit_rev, OMP_VALIDATOR)
        check("a receipt without exit=0 reads 4 of 5",
              rc == 1 and line(out) == "4" and "FAIL d1" in out,
              out.strip()[:200])

        # the old kill-rule wording
        oldkill_rev = _fixture_commit(repo, "old kill world", {
            CATALOGUE_RECEIPT: _receipt(prose_rev, CATALOGUE_LINE),
            PLAN: FIXTURE_PLAN_OLD_KILL,
        })
        rc, out, err = score(oldkill_rev, OMP_VALIDATOR)
        check("the old kill wording reads 4 of 5",
              rc == 1 and line(out) == "4" and "FAIL d4" in out,
              out.strip()[:200])

        # the checker is not pinned: rewritten bytes with the honest shape pass
        rewritten_rev = _fixture_commit(repo, "rewritten checker world", {
            "verifiers/verify_corpus_integrity.py": FIXTURE_INTEGRITY_JSON_V2,
            PLAN: FIXTURE_PLAN_HONEST,
        })
        rc, out, err = score(rewritten_rev, OMP_VALIDATOR)
        check("a rewritten checker with the honest shape reads 5 of 5",
              rc == 0 and line(out) == "5", out.strip()[:240])

        # validator worlds (path override, no commit needed)
        bad = Path(tdir) / "validator-planner.mjs"
        bad.write_text(FIXTURE_VALIDATOR_PLANNER, encoding="utf-8")
        rc, out, err = score(rewritten_rev, bad)
        check("planner inside SWARM_ROLES reads 4 of 5",
              rc == 1 and line(out) == "4" and "FAIL d2" in out,
              out.strip()[:200])

        broken = Path(tdir) / "validator-broken.mjs"
        broken.write_text(FIXTURE_VALIDATOR_BROKEN, encoding="utf-8")
        rc, out, err = score(rewritten_rev, broken)
        check("an unparseable SWARM_ROLES literal is could-not-evaluate",
              rc == 2 and line(out) == "missing",
              "rc %d out %r err %r" % (rc, out.strip()[:120], err.strip()[:160]))

        missing = Path(tdir) / "absent-validator.mjs"
        rc, out, err = score(rewritten_rev, missing)
        check("an absent validator is could-not-evaluate",
              rc == 2 and "could-not-evaluate" in err,
              "rc %d err %r" % (rc, err.strip()[:160]))

        # w_nodisclosure: the gate is honest but the record says nothing
        nodisclosure_rev = _fixture_commit(repo, "nodisclosure world", {
            LESSON: FIXTURE_LESSON_NODISCLOSURE,
        })
        rc, out, err = score(nodisclosure_rev, OMP_VALIDATOR)
        check("w_nodisclosure exits 1", rc == 1, "rc %d" % rc)
        check("w_nodisclosure reads 4 of 5", line(out) == "4", out.strip()[:200])
        check("w_nodisclosure names d5", "FAIL d5" in out, out.strip()[:200])
        check("w_nodisclosure's detail names the missing disclosure",
              "does not carry" in out, out.strip()[:240])

        # w_launder: the non-author record rewritten to green the gate (M87-1)
        launder_rev = _fixture_commit(repo, "launder world", {
            SPOTCHECK: FIXTURE_SPOTCHECK_LAUNDERED,
        })
        rc, out, err = score(launder_rev, OMP_VALIDATOR)
        check("w_launder exits 1", rc == 1, "rc %d" % rc)
        check("w_launder reads 4 of 5", line(out) == "4", out.strip()[:200])
        check("w_launder names d5", "FAIL d5" in out, out.strip()[:200])
        check("w_launder's detail names the rewritten record",
              "rewritten" in out and SPOTCHECK in out, out.strip()[:240])

        # w_tipmismatch: the worktree tip is not the measured revision
        rc, out, err = score(honest_rev, OMP_VALIDATOR)
        check("w_tipmismatch is could-not-evaluate, never a pass",
              rc == 2 and line(out) == "missing"
              and "worktree tip" in err,
              "rc %d err %r" % (rc, err.strip()[:200]))

        # a revision that does not resolve is could-not-evaluate, not red
        rc, out, err = score("0" * 40, OMP_VALIDATOR)
        check("an unresolvable revision is could-not-evaluate",
              rc == 2 and line(out) == "missing", "rc %d" % rc)

    print("%d failure(s) over %d assertions" % (len(failures), assertions))
    for failure in failures:
        print("FAIL", failure)
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
