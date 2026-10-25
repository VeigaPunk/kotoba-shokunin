#!/usr/bin/env python3
"""check_r67_routed_repairs.py — C2 counter for kotoba round 68 (wave-1 seat draft).

Contract
--------
`python3 -B check_r67_routed_repairs.py --rev <full-sha>` prints

    r67 routed defects closed N of 4

and exits 0 when N == 4, 1 when N < 4 (a content verdict), 2 for a
usage/environment error: unknown --rev, unreadable repo, the corpus gate
could not be run, or the pinned base does not score 0 of 4.  `--repo <path>`
defaults to the lane root, found by walking up from this file (so the script
works both from the wave drafts directory and installed under verifiers/).

The four routed defects are the round-67 closure's routed list
(`corpus/lessons/round-67-verifier-spotcheck.md`, § Routed defects), checked
from the COMMITTED bytes at --rev unless stated otherwise:

  D1 (R67-1, dishonest before-line).  Each living record — `LOG.md`,
      `SCORECARD.md`, `corpus/lessons/round-68.md` — carries an appended
      correction naming the observed base line
      `environment error: cannot read corpus/knowledge/instruction-authority-ladder-round67.md …`
      (with the r67 base hash prefix `2a8eba56`), the append proved by a
      count gain of that line against the pinned base.  A record that still
      carries the unobserved `0 of 1` claim is accepted only because the
      appended correction supersedes it in the same record: the records are
      append-only, so the wrong claim text itself is never rewritten.
  D2 (R67-2, wrong receipt path).  The correction naming the real census
      receipt path `.ufo/waves/round-67/controls/census-validate-append.txt`
      is appended in each record (count gain against the base), and within
      each record every line naming the wrong `w1/controls/` form stands at
      most two lines from a line naming the real path — the erratum names
      both, while a bare wrong path would assert the wrong location.  The
      r67 report and the r67 lesson are frozen evidence the lane never
      edits, so their surviving wrong path is out of scope by the repair's
      own terms (the r68 records carry the correction instead).
  D3 (R67-3, undisclosed 254 MB).  The 254 MB
      `.ufo/waves/round-67/w1/controls/junk-world` control mirror is named,
      with its size, in `LOG.md` and in the round-68 lesson, AND the path no
      longer exists in the working tree of --repo.  The worktree conjunct is
      worktree-state by nature: the defect is an untracked leftover that no
      revision carries, so no committed-byte test can see it.
  D4 (R67-4, unindexed closure file).  `corpus/lessons/round-67-verifier-spotcheck.md`
      is tracked at --rev, and EVERY expect in the committed
      `verifiers/corpus-baseline.json` equals the value the gate's own
      measurement yields at that revision — the gate is RUN (the stored
      numbers are never trusted): `git archive --format=tar <rev>` is
      extracted into a throwaway repository whose objects fall back to this
      repo's, and the revision's own `verifiers/verify_corpus_integrity.py`
      is run there with `--no-baseline --json`.  The six zero-mode checks
      must measure 0 — that is the coverage-map index row, read through the
      gate's own fence-aware coverage-map extractor rather than a substring
      — and the three equal-mode checks must match the stored expects.

The round-68 report lands in the fleet repository, outside this repo's
committable bytes, so the counter pins the three lane-side records only.

Self-test
---------
`--self-test` (cannot be combined with --rev) builds a fixture repository in
a temp directory — with a stub gate that measures the same nine check ids
from the fixture corpus — and drives the base control, the honest world
(public main() must print the frozen line and exit 0 there, and the frozen
line `0 of 4` with exit 1 at the fixture base), and one broken world per
defect: drop the LOG erratum (D1); restore a bare wrong receipt path (D2);
drop the disclosure, plus the directory-present worktree conjunct (D3); drop
the index row, and separately keep a stale baseline (D4).  Prints
`self-test: N failure(s) over M assertions`; exit 0 iff no failure.
"""
from __future__ import annotations

import argparse
import contextlib
import io
import json
import os
import subprocess
import sys
import tarfile
import tempfile
from pathlib import Path

BASE_REV = "e94ae32a5cd8dc3ee8e2d247816784bec2750cc0"  # round-67 lane tip

LOG = "LOG.md"
SCORECARD = "SCORECARD.md"
LESSON68 = "corpus/lessons/round-68.md"
RECORDS = (LOG, SCORECARD, LESSON68)

# D1: the observed r67 base line (receipt .ufo/waves/round-67/receipts/C2-authority-measure.txt)
OBSERVED = (
    "environment error: cannot read "
    "corpus/knowledge/instruction-authority-ladder-round67.md"
)
BASE_HASH_PREFIX = "2a8eba56"
UNOBSERVED_CLAIM = "0 of 1"  # the line the r67 report asserted but the base never printed

# D2: census receipt paths (real vs the w1/ form the r67 report cites)
CENSUS_REAL = ".ufo/waves/round-67/controls/census-validate-append.txt"
CENSUS_WRONG = ".ufo/waves/round-67/w1/controls/census-validate-append.txt"
CENSUS_WINDOW = 2  # a wrong-path line must stand this close to a real-path line

# D3: the untracked control mirror and its disclosed size
JUNK = ".ufo/waves/round-67/w1/controls/junk-world"
JUNK_MB = "254"

# D4: gate, baseline, coverage row target
SPOTCHECK = "corpus/lessons/round-67-verifier-spotcheck.md"
README = "corpus/README.md"
BASELINE = "verifiers/corpus-baseline.json"
GATE = "verifiers/verify_corpus_integrity.py"
ZERO_IDS = (
    "corpus.index.unindexed",
    "corpus.index.stale_patterns",
    "corpus.index.missing_paths",
    "corpus.pointers.report_dead",
    "corpus.pointers.commit_unresolvable",
    "corpus.pointers.commit_nonhash",
)
EQUAL_IDS = (
    "corpus.index.tracked_files",
    "corpus.pointers.report_total",
    "corpus.pointers.commit_total",
)
ALL_IDS = ZERO_IDS + EQUAL_IDS


class EnvError(Exception):
    """The counter's environment cannot answer (exit 2)."""


def git(root: Path, *args: str, timeout: int = 120) -> subprocess.CompletedProcess[str]:
    return subprocess.run(["git", "-C", str(root), *args], capture_output=True,
                          text=True, check=False, timeout=timeout)


def git_out(root: Path, *args: str) -> str:
    result = git(root, *args)
    if result.returncode:
        raise EnvError("git %s failed in %s: %s" % (" ".join(args), root, result.stderr.strip()))
    return result.stdout


def show(root: Path, rev: str, path: str) -> str | None:
    """Committed bytes of path at rev, or None when the path is absent there."""
    result = git(root, "show", "%s:%s" % (rev, path))
    return result.stdout if result.returncode == 0 else None


def lane_root() -> Path:
    """Nearest ancestor of this file that looks like the lane root."""
    here = Path(__file__).resolve()
    for candidate in here.parents:
        if ((candidate / "corpus" / "README.md").is_file()
                and (candidate / GATE).is_file()):
            return candidate
    raise EnvError("cannot locate the lane root above %s" % here)


def record_texts(root: Path, rev: str, paths=RECORDS) -> dict[str, str]:
    texts: dict[str, str] = {}
    for path in paths:
        blob = show(root, rev, path)
        if blob is None:
            raise _Missing(path)
        texts[path] = blob
    return texts


class _Missing(Exception):
    pass


def _lines_within(text: str, needle: str, other: str, window: int) -> bool:
    """Every needle-line stands at most `window` lines from some other-line."""
    lines = text.splitlines()
    others = [i for i, line in enumerate(lines) if other in line]
    for i, line in enumerate(lines):
        if needle in line and not any(abs(i - j) <= window for j in others):
            return False
    return True


def check_d1(root: Path, rev: str, base_texts: dict[str, str]) -> bool:
    try:
        texts = record_texts(root, rev)
    except _Missing:
        return False
    for path in RECORDS:
        text = texts[path]
        base_count = base_texts.get(path, "").count(OBSERVED)
        if text.count(OBSERVED) <= base_count:  # the correction must be newly appended
            return False
        if BASE_HASH_PREFIX not in text:
            return False
        if UNOBSERVED_CLAIM in text and OBSERVED not in text:  # pragma: no cover (subsumed)
            return False
    return True


def check_d2(root: Path, rev: str, base_texts: dict[str, str]) -> bool:
    try:
        texts = record_texts(root, rev)
    except _Missing:
        return False
    for path in RECORDS:
        text = texts[path]
        if CENSUS_REAL not in text:
            return False
        if text.count(CENSUS_REAL) <= base_texts.get(path, "").count(CENSUS_REAL):
            return False  # the correction naming the real path must be newly appended
        if not _lines_within(text, CENSUS_WRONG, CENSUS_REAL, CENSUS_WINDOW):
            return False  # a bare wrong path asserts the wrong location
    return True


def check_d3(root: Path, rev: str, base_texts: dict[str, str]) -> bool:
    for path in (LOG, LESSON68):
        blob = show(root, rev, path)
        if blob is None or JUNK not in blob or JUNK_MB not in blob:
            return False
    if os.path.lexists(Path(root) / JUNK):  # worktree conjunct: the leftover is gone
        return False
    return True


def run_gate(root: Path, rev: str) -> dict[str, int]:
    """Run the revision's own corpus gate against the committed bytes only.

    The archive of `rev` is extracted into a temporary repo whose object
    store falls back to this repo's (so `commit `<hex>`` citations resolve
    exactly as they do in place), the tree is force-added (reconstructing
    the tracked set, ignoring any .gitignore), and the gate runs there with
    --no-baseline --json.  Nothing in the lane repository is written.
    """
    with tempfile.TemporaryDirectory(prefix="r67routed-gate-") as tmpdir:
        tmp = Path(tmpdir)
        archive = subprocess.run(["git", "-C", str(root), "archive", "--format=tar", rev],
                                 capture_output=True, check=False, timeout=300)
        if archive.returncode:
            raise EnvError("git archive %s failed: %s" % (rev, archive.stderr.decode("utf-8", "replace").strip()))
        with tarfile.open(fileobj=io.BytesIO(archive.stdout), mode="r:") as tar:
            tar.extractall(tmp, filter="tar")  # trusted self-archive; symlinks preserved
        git_dir = git_out(root, "rev-parse", "--absolute-git-dir").strip()
        git_out(tmp, "-c", "init.defaultBranch=main", "init", "-q")
        alternates = tmp / ".git" / "objects" / "info" / "alternates"
        alternates.parent.mkdir(parents=True, exist_ok=True)
        alternates.write_text(os.path.join(git_dir, "objects") + "\n", encoding="utf-8")
        git_out(tmp, "add", "-A", "-f", ".")
        gate_path = tmp / GATE
        if not gate_path.is_file():
            raise EnvError("gate script %s is not in the tree at %s" % (GATE, rev))
        try:
            proc = subprocess.run(
                [sys.executable, "-B", str(gate_path), "--repo", str(tmp),
                 "--no-baseline", "--json"],
                cwd=str(tmp), capture_output=True, text=True, check=False, timeout=300)
        except subprocess.TimeoutExpired as exc:
            raise EnvError("gate run timed out at %s: %s" % (rev, exc)) from exc
        if proc.returncode == 2:
            raise EnvError("gate read its extraction as unreadable at %s: %s"
                           % (rev, proc.stderr.strip()))
        try:
            payload = json.loads(proc.stdout)
            rows = payload["results"]
            measured = {row["check"]: row["observed"] for row in rows}
        except (json.JSONDecodeError, KeyError, TypeError) as exc:
            raise EnvError("gate output not parseable at %s (exit %d): %r"
                           % (rev, proc.returncode, exc)) from exc
        if any(check not in measured for check in ALL_IDS):
            raise EnvError("gate at %s did not report all nine check ids: got %s"
                           % (rev, sorted(measured)))
        return measured


def check_d4(root: Path, rev: str, base_texts: dict[str, str]) -> bool:
    if show(root, rev, SPOTCHECK) is None:
        return False  # the closure file itself is gone
    baseline_text = show(root, rev, BASELINE)
    readme = show(root, rev, README)
    if baseline_text is None or readme is None:
        return False
    try:
        baseline = json.loads(baseline_text)["checks"]
    except (json.JSONDecodeError, KeyError, TypeError):
        return False
    measured = run_gate(root, rev)
    if any(measured[check] != 0 for check in ZERO_IDS):
        return False  # the index row must really cover the spot-check (and nothing dangle)
    for check in ALL_IDS:
        expect = baseline.get(check, {}).get("expect")
        if expect is None or measured[check] != expect:
            return False  # stored numbers must equal the gate's own measurement
    return True


def score(root: Path, rev: str, base_texts: dict[str, str]) -> tuple[int, dict[str, bool]]:
    checks = {
        "D1-r67-1-erratum-appended": check_d1(root, rev, base_texts),
        "D2-r67-2-real-receipt-path": check_d2(root, rev, base_texts),
        "D3-r67-3-junk-disclosed-and-removed": check_d3(root, rev, base_texts),
        "D4-r67-4-indexed-and-rerecorded": check_d4(root, rev, base_texts),
    }
    return sum(checks.values()), checks


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--rev")
    ap.add_argument("--repo", type=Path, default=None,
                    help="lane repository (default: nearest lane root above this script)")
    ap.add_argument("--self-test", action="store_true")
    args = ap.parse_args(argv)
    if args.self_test:
        if args.rev:
            ap.error("--self-test cannot be combined with --rev")
        return self_test()
    if not args.rev:
        ap.error("--rev is required")
    try:
        root = (args.repo if args.repo is not None else lane_root()).resolve()
        for rev in (BASE_REV, args.rev):
            if git(root, "cat-file", "-e", rev + "^{commit}").returncode:
                print("could-not-evaluate: %s is not a commit in %s" % (rev, root),
                      file=sys.stderr)
                return 2
        base_texts = {path: show(root, BASE_REV, path) or "" for path in RECORDS}
        base_n, base_checks = score(root, BASE_REV, base_texts)
        if base_n != 0:
            print("could-not-evaluate: pinned base %s scores %d of 4, expected 0 of 4"
                  % (BASE_REV[:8], base_n), file=sys.stderr)
            return 2
        after_n, after_checks = score(root, args.rev, base_texts)
    except (EnvError, OSError) as exc:
        print("could-not-evaluate: %s" % exc, file=sys.stderr)
        return 2
    print("control at %s: %d of 4" % (BASE_REV[:8], base_n))
    for name, passed in after_checks.items():
        print("%s: %s" % (name, "PASS" if passed else "FAIL"))
    print("r67 routed defects closed %d of 4" % after_n)
    return 0 if after_n == 4 else 1


# ---------------------------------------------------------------------------
# self-test: one fixture repo, honest world, base control, one broken world
# per defect (plus the D3 worktree conjunct).
# ---------------------------------------------------------------------------
FIXTURE_GATE = r'''#!/usr/bin/env python3
"""Fixture stand-in for verify_corpus_integrity.py (self-test world only).

Measures the same nine check ids from the fixture corpus with simplified
but honest semantics: tracked = files under corpus/; coverage = column-2
backticked tokens of `## Coverage map` rows; relative .ufo/reports pointers
resolve from the citing file; exact-path rows must exist on disk.
"""
import fnmatch
import json
import re
import sys
from pathlib import Path

repo = Path(__file__).resolve().parent.parent
corpus = repo / "corpus"
files = sorted(p.relative_to(corpus).as_posix()
               for p in corpus.rglob("*") if p.is_file() or p.is_symlink())
readme = (corpus / "README.md").read_text(encoding="utf-8")
inside = False
cells = []
for line in readme.splitlines():
    if line.startswith("## "):
        inside = line.strip() == "## Coverage map"
        continue
    if inside and line.startswith("|"):
        parts = line.split("|")
        if len(parts) >= 4 and set(parts[1].strip()) - set("-: "):
            cells.append(parts[2])
tokens = [t.strip() for cell in cells for t in re.findall(r"`([^`]+)`", cell)]
covered = set()
for tok in tokens:
    if any(c in tok for c in "*?["):
        covered.update(f for f in files if fnmatch.fnmatchcase(f, tok))
    else:
        covered.add(tok)
unindexed = [f for f in files if f != "README.md" and f not in covered]
stale = [t for t in tokens if not t.startswith(("../", "/", "~"))
         and not any(c in t for c in "*?[") and t not in files]
missing = [t for t in tokens if not t.startswith(("~",))
           and not any(c in t for c in "*?[") and not (corpus / t).exists()]
report_total = report_dead = 0
for rel in [f for f in files if f.endswith(".md")]:
    text = (corpus / rel).read_text(encoding="utf-8")
    for m in re.finditer(r"(?:\.{1,2}/)*\.ufo/reports/round-\d+/[^\s`\"|]*\.md", text):
        report_total += 1
        if not ((corpus / rel).parent / m.group(0)).is_file():
            report_dead += 1
commit_cites = re.findall(r"commit `([0-9a-fA-F]{7,40})`",
                          "".join((corpus / f).read_text(encoding="utf-8")
                                  for f in files if f.endswith(".md")))
ids = [
    ("corpus.index.tracked_files", "equal", len(files)),
    ("corpus.index.unindexed", "zero", len(unindexed)),
    ("corpus.index.stale_patterns", "zero", len(stale)),
    ("corpus.index.missing_paths", "zero", len(missing)),
    ("corpus.pointers.report_total", "equal", report_total),
    ("corpus.pointers.report_dead", "zero", report_dead),
    ("corpus.pointers.commit_total", "equal", len(commit_cites)),
    ("corpus.pointers.commit_unresolvable", "zero", 0),
    ("corpus.pointers.commit_nonhash", "zero", 0),
]
print(json.dumps({"observed": {}, "results": [
    {"check": cid, "mode": mode, "observed": value, "verdict": "PASS"}
    for cid, mode, value in ids]}))
'''

README_COVERED = """# fixture corpus

## Coverage map

| Area | File | Basis |
|------|------|-------|
| Spot-check | `lessons/round-67-verifier-spotcheck.md` | closure, indexed round 68 |
| Round 68 | `lessons/round-68.md` | round lesson |
"""

README_UNCOVERED = """# fixture corpus

## Coverage map

| Area | File | Basis |
|------|------|-------|
| Round 68 | `lessons/round-68.md` | round lesson |
"""

SPOTCHECK_TEXT = "# Round 67 verifier spot-check (fixture)\n\nrouted four defects.\n"

LESSON68_HONEST = """# Round 68 lesson (fixture)

- M107: the r67 record said the base "prints `0 of 1` and exits nonzero";
  observed instead `environment error: cannot read corpus/knowledge/instruction-authority-ladder-round67.md at 2a8eba56b3f9321b70c569fa2816d42237ca49a2`.
- M108: the report cites `.ufo/waves/round-67/w1/controls/census-validate-append.txt`;
  the file that exists is `.ufo/waves/round-67/controls/census-validate-append.txt`.
- M109: `.ufo/waves/round-67/w1/controls/junk-world/` — a 254 MB control mirror —
  is disclosed here and removed from the working tree.
Report: `../../.ufo/reports/round-68/kotoba.md`
"""

LESSON68_NO_DISCLOSURE = LESSON68_HONEST.replace(
    "- M109: `.ufo/waves/round-67/w1/controls/junk-world/` — a 254 MB control mirror —\n"
    "  is disclosed here and removed from the working tree.\n", "")

LOG_HONEST = """# fixture LOG

- r67 C2 claim: at the pinned base it prints `0 of 1` and exits nonzero.
- Legacy note: the append receipt was `.ufo/waves/round-67/controls/census-validate-append.txt`.
- Erratum (append-only; routed defect R67-1). At the r67 base
  `2a8eba56b3f9321b70c569fa2816d42237ca49a2` the counter prints
  `environment error: cannot read corpus/knowledge/instruction-authority-ladder-round67.md at 2a8eba56b3f9321b70c569fa2816d42237ca49a2`
  and exits 2.
- Erratum (append-only; routed defect R67-2). The report cites
  `.ufo/waves/round-67/w1/controls/census-validate-append.txt`; the file that exists is
  `.ufo/waves/round-67/controls/census-validate-append.txt`.
- Routed defect R67-3 (disclosure). `.ufo/waves/round-67/w1/controls/junk-world/` —
  a 254 MB untracked control mirror — was removed from the working tree.
"""

LOG_NO_ERRATUM = LOG_HONEST.replace(
    "- Erratum (append-only; routed defect R67-1). At the r67 base\n"
    "  `2a8eba56b3f9321b70c569fa2816d42237ca49a2` the counter prints\n"
    "  `environment error: cannot read corpus/knowledge/instruction-authority-ladder-round67.md at 2a8eba56b3f9321b70c569fa2816d42237ca49a2`\n"
    "  and exits 2.\n", "")
LOG_WRONG_PATH_BARE = LOG_HONEST + (
    "- The census receipt lives at "
    "`.ufo/waves/round-67/w1/controls/census-validate-append.txt`.\n")

SCORECARD_HONEST = """# fixture SCORECARD

- **Depth.** At the pinned base `2a8eba56b3f9321b70c569fa2816d42237ca49a2` it prints
  `0 of 1` and exits nonzero.
- **Erratum to the round-67 depth annotation above (append-only; routed defects R67-1
  and R67-2).** The annotation states that the r67 C2 base "prints `authority ladder
  grounded 0 of 1`". The committed receipt shows exit 2 with
  `environment error: cannot read corpus/knowledge/instruction-authority-ladder-round67.md`
  and nothing on stdout; the r67 census receipt path is
  `.ufo/waves/round-67/controls/census-validate-append.txt`, not the form the report cites.
"""

SCORECARD_BASE = """# fixture SCORECARD

- **Depth.** At the pinned base `2a8eba56b3f9321b70c569fa2816d42237ca49a2` it prints
  `0 of 1` and exits nonzero.
"""


def _write(root: Path, path: str, text: str) -> None:
    target = root / path
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(text, encoding="utf-8")


def self_test() -> int:
    assertions = 0
    failures = 0

    def check(label: str, got, want) -> None:
        nonlocal assertions, failures
        assertions += 1
        if got != want:
            failures += 1
            print("FAIL %s: got %r want %r" % (label, got, want))

    global BASE_REV
    saved_base = BASE_REV
    try:
        with tempfile.TemporaryDirectory(prefix="r67routed-fixture-") as tmpdir:
            root = Path(tmpdir)
            git_out(root, "-c", "init.defaultBranch=main", "init", "-q")
            # base world: none of the four repairs
            _write(root, "corpus/README.md", README_UNCOVERED)
            _write(root, SPOTCHECK, SPOTCHECK_TEXT)
            _write(root, LOG, "- r67 C2 claim: at the pinned base it prints `0 of 1` and exits nonzero.\n"
                              "- Legacy note: the append receipt was `%s`.\n" % CENSUS_REAL)
            _write(root, SCORECARD, SCORECARD_BASE)
            _write(root, BASELINE, json.dumps({"checks": {
                "corpus.index.tracked_files": {"expect": 2},
                "corpus.index.unindexed": {"expect": 0},
                "corpus.index.stale_patterns": {"expect": 0},
                "corpus.index.missing_paths": {"expect": 0},
                "corpus.pointers.report_total": {"expect": 0},
                "corpus.pointers.report_dead": {"expect": 0},
                "corpus.pointers.commit_total": {"expect": 0},
                "corpus.pointers.commit_unresolvable": {"expect": 0},
                "corpus.pointers.commit_nonhash": {"expect": 0}}}))
            _write(root, GATE, FIXTURE_GATE)
            git_out(root, "add", "-A", "-f", ".")
            git_out(root, "-c", "user.name=fixture", "-c", "user.email=fixture@example.invalid",
                    "commit", "-q", "-m", "fixture base")
            base = git_out(root, "rev-parse", "HEAD").strip()
            BASE_REV = base
            base_texts = {path: show(root, base, path) or "" for path in RECORDS}
            base_n, base_checks = score(root, base, base_texts)
            check("control/base-is-zero-of-four", base_n, 0)
            check("control/D1-absent", base_checks["D1-r67-1-erratum-appended"], False)
            check("control/D2-absent", base_checks["D2-r67-2-real-receipt-path"], False)
            check("control/D3-absent", base_checks["D3-r67-3-junk-disclosed-and-removed"], False)
            check("control/D4-absent", base_checks["D4-r67-4-indexed-and-rerecorded"], False)

            # honest world: all four repairs
            _write(root, "corpus/README.md", README_COVERED)
            _write(root, LESSON68, LESSON68_HONEST)
            _write(root, LOG, LOG_HONEST)
            _write(root, SCORECARD, SCORECARD_HONEST)
            _write(root, ".ufo/reports/round-68/kotoba.md", "fixture report\n")
            _write(root, BASELINE, json.dumps({"checks": {
                "corpus.index.tracked_files": {"expect": 3},
                "corpus.index.unindexed": {"expect": 0},
                "corpus.index.stale_patterns": {"expect": 0},
                "corpus.index.missing_paths": {"expect": 0},
                "corpus.pointers.report_total": {"expect": 1},
                "corpus.pointers.report_dead": {"expect": 0},
                "corpus.pointers.commit_total": {"expect": 0},
                "corpus.pointers.commit_unresolvable": {"expect": 0},
                "corpus.pointers.commit_nonhash": {"expect": 0}}}))
            git_out(root, "add", "-A", "-f", ".")
            git_out(root, "-c", "user.name=fixture", "-c", "user.email=fixture@example.invalid",
                    "commit", "-q", "-m", "fixture repaired")
            tip = git_out(root, "rev-parse", "HEAD").strip()
            honest_n, honest_checks = score(root, tip, base_texts)
            check("honest/D1", honest_checks["D1-r67-1-erratum-appended"], True)
            check("honest/D2", honest_checks["D2-r67-2-real-receipt-path"], True)
            check("honest/D3", honest_checks["D3-r67-3-junk-disclosed-and-removed"], True)
            check("honest/D4", honest_checks["D4-r67-4-indexed-and-rerecorded"], True)
            check("honest/4-of-4", honest_n, 4)

            # broken world D1: the LOG erratum is dropped
            _write(root, LOG, LOG_NO_ERRATUM)
            no_erratum = _fixture_commit(root, "mutant: LOG erratum dropped")
            check("kill/D1-erratum-dropped",
                  check_d1(root, no_erratum, base_texts), False)

            # broken world D2: a bare wrong receipt path is asserted again
            _write(root, LOG, LOG_WRONG_PATH_BARE)
            wrong_path = _fixture_commit(root, "mutant: bare wrong receipt path")
            check("kill/D2-bare-wrong-path",
                  check_d2(root, wrong_path, base_texts), False)

            # broken world D3a: the disclosure is dropped from the lesson
            _write(root, LOG, LOG_HONEST)
            _write(root, LESSON68, LESSON68_NO_DISCLOSURE)
            no_disclosure = _fixture_commit(root, "mutant: disclosure dropped")
            check("kill/D3-disclosure-dropped",
                  check_d3(root, no_disclosure, base_texts), False)

            # broken world D3b: worktree conjunct — the leftover directory is back
            junk_dir = root / JUNK
            junk_dir.mkdir(parents=True)
            check("kill/D3-worktree-dir-present",
                  check_d3(root, tip, base_texts), False)
            junk_dir.rmdir()
            check("honest/D3-worktree-clean-again",
                  check_d3(root, tip, base_texts), True)

            # broken world D4a: the coverage-map index row is dropped
            _write(root, LESSON68, LESSON68_HONEST)
            _write(root, "corpus/README.md", README_UNCOVERED)
            no_row = _fixture_commit(root, "mutant: index row dropped")
            check("kill/D4-index-row-dropped",
                  check_d4(root, no_row, base_texts), False)

            # broken world D4b: a stale baseline is kept
            _write(root, "corpus/README.md", README_COVERED)
            _write(root, BASELINE, json.dumps({"checks": {
                "corpus.index.tracked_files": {"expect": 99},
                "corpus.index.unindexed": {"expect": 0},
                "corpus.index.stale_patterns": {"expect": 0},
                "corpus.index.missing_paths": {"expect": 0},
                "corpus.pointers.report_total": {"expect": 1},
                "corpus.pointers.report_dead": {"expect": 0},
                "corpus.pointers.commit_total": {"expect": 0},
                "corpus.pointers.commit_unresolvable": {"expect": 0},
                "corpus.pointers.commit_nonhash": {"expect": 0}}}))
            stale = _fixture_commit(root, "mutant: stale baseline")
            check("kill/D4-stale-baseline",
                  check_d4(root, stale, base_texts), False)

            # public main() at the honest tip and at the base
            output = io.StringIO()
            with contextlib.redirect_stdout(output):
                exit_code = main(["--rev", tip, "--repo", str(root)])
            check("public-main/honest-exit", exit_code, 0)
            check("public-main/honest-line",
                  "r67 routed defects closed 4 of 4" in output.getvalue(), True)
            output = io.StringIO()
            with contextlib.redirect_stdout(output):
                exit_code = main(["--rev", base, "--repo", str(root)])
            check("public-main/control-exit", exit_code, 1)
            check("public-main/control-line",
                  "r67 routed defects closed 0 of 4" in output.getvalue(), True)

            # usage/environment: unknown revision is exit 2, not a content verdict
            exit_code = main(["--rev", "0" * 40, "--repo", str(root)])
            check("public-main/unknown-rev-exit-2", exit_code, 2)
            try:
                exit_code = main([])
            except SystemExit as exc:  # argparse usage error
                exit_code = int(exc.code or 0)
            check("public-main/missing-rev-exit-2", exit_code, 2)
    finally:
        BASE_REV = saved_base
    print("self-test: %d failure(s) over %d assertions" % (failures, assertions))
    return 1 if failures else 0


def _fixture_commit(root: Path, message: str) -> str:
    git_out(root, "add", "-A", "-f", ".")
    git_out(root, "-c", "user.name=fixture", "-c", "user.email=fixture@example.invalid",
            "commit", "-q", "-m", message)
    return git_out(root, "rev-parse", "HEAD").strip()


if __name__ == "__main__":
    sys.exit(main())
