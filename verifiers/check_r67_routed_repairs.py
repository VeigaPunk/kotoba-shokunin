#!/usr/bin/env python3
"""check_r67_routed_repairs.py — C2 counter for kotoba round 68.

Contract
--------
`python3 -B verifiers/check_r67_routed_repairs.py --rev <full-sha>` prints
    r67 routed defects closed N of 4
and exits 0 when N == 4, nonzero otherwise.  At the pinned base (the round-67 tip
`e94ae32a5cd8dc3ee8e2d247816784bec2750cc0`) it must print `r67 routed defects closed 0 of 4`
and exit nonzero.

The four routed defects come from the round-67 closure's spot-check
(`corpus/lessons/round-67-verifier-spotcheck.md`, written by the hyaku closure, never edited by
the lane):

  R67-1  the r67 report asserted a base line the committed receipt does not show
         (the counter printed nothing and exited 2; the report says it printed
         `authority ladder grounded 0 of 1`);
  R67-2  the r67 report cites a census receipt path that does not exist
         (`.ufo/waves/round-67/w1/controls/census-validate-append.txt`; the bytes are at
         `.ufo/waves/round-67/controls/census-validate-append.txt`);
  R67-3  a 254 MB untracked control mirror (`.ufo/waves/round-67/w1/controls/junk-world/`)
         was left in the lane working tree and never disclosed;
  R67-4  the closure's own spot-check file was left unindexed, which turned the corpus gate
         red (6/9, exit 1) at the round-67 tip.

The counter reads the COMMITTED bytes at `--rev` (never the working tree) and checks:

  D1  the round's records carry the appended correction that names the observed
      `environment error: cannot read corpus/knowledge/instruction-authority-ladder-round67.md`
      line (the append-only erratum; the r67 report itself is never rewritten);
  D2  the records name the real receipt path `.ufo/waves/round-67/controls/census-validate-append.txt`;
  D3  the records name the disclosed `junk-world` control mirror AND that path no longer exists
      in the working tree;
  D4  `corpus/README.md` carries a coverage-map index row for
      `corpus/lessons/round-67-verifier-spotcheck.md` AND `verifiers/corpus-baseline.json`'s
      re-recorded values equal what the gate's own measurement yields at that revision.

Trust boundary (QUALITY Q33): D1–D3 are presence floors over the lane's own records — a
counter that counts names, not substance.  They are disclosed as such; the substantive
verification of R67-1 is the re-run of the r67 counter at the r67 base revision, and of R67-4
the corpus gate's own exit code.

Exit codes: 0 all four closed · 1 not all closed · 2 usage/environment error.
"""
from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
import tempfile
from pathlib import Path

RECORDS = ("LOG.md", "SCORECARD.md", "corpus/lessons/round-68.md")
README = "corpus/README.md"
BASELINE = "verifiers/corpus-baseline.json"
SPOTCHECK = "corpus/lessons/round-67-verifier-spotcheck.md"
JUNK = ".ufo/waves/round-67/w1/controls/junk-world"
REAL_RECEIPT = ".ufo/waves/round-67/controls/census-validate-append.txt"
WRONG_RECEIPT = ".ufo/waves/round-67/w1/controls/census-validate-append.txt"
OBSERVED = "environment error: cannot read corpus/knowledge/instruction-authority-ladder-round67.md"
TOTAL = 4


class EnvError(Exception):
    pass


def _git_show(repo: Path, rev: str, path: str) -> str | None:
    proc = subprocess.run(["git", "-C", str(repo), "show", f"{rev}:{path}"],
                          capture_output=True, text=True)
    if proc.returncode != 0:
        return None
    return proc.stdout


def _materialize(repo: Path, rev: str, dest: Path) -> Path:
    for path in RECORDS + (README, BASELINE):
        text = _git_show(repo, rev, path)
        out = dest / path
        out.parent.mkdir(parents=True, exist_ok=True)
        if text is None:
            # A missing records file is a content state (the round has not recorded yet),
            # not an environment error: write empty bytes so check() can score it.
            out.write_text("", encoding="utf-8")
            continue
        out.write_text(text, encoding="utf-8")
    return dest


def _require_commit(repo: Path, rev: str) -> None:
    proc = subprocess.run(["git", "-C", str(repo), "cat-file", "-e", f"{rev}^{{commit}}"],
                          capture_output=True, text=True)
    if proc.returncode != 0:
        raise EnvError(f"{rev} is not a commit in {repo}")


def _baseline_values(repo: Path, rev: str) -> dict[str, int]:
    """Re-derive the census values with the gate's own measurement at <rev>.

    The revision is materialized in a throwaway shared clone. Nothing outside that
    clone is written: the lane's worktree, index and HEAD are never touched, which is
    what the round-67 routed defect (a revision move inside the lane repo) was about.
    """
    _require_commit(repo, rev)
    with tempfile.TemporaryDirectory(prefix="k68-baseline-") as tmp:
        clone = Path(tmp) / "clone"
        proc = subprocess.run(["git", "clone", "--shared", "-q", str(repo), str(clone)],
                              capture_output=True, text=True)
        if proc.returncode != 0:
            raise EnvError("cannot create the sandbox clone")
        proc = subprocess.run(["git", "-C", str(clone), "reset", "-q", "--hard", rev],
                              capture_output=True, text=True)
        if proc.returncode != 0:
            raise EnvError(f"cannot move the sandbox to {rev}")
        proc = subprocess.run(
            ["python3", "-B", str(clone / "verifiers" / "verify_corpus_integrity.py"),
             "--repo", str(clone), "--no-baseline", "--json"],
            capture_output=True, text=True, timeout=600)
        if proc.returncode not in (0, 1):
            raise EnvError("the corpus gate could not be run at the measured revision")
        data = json.loads(proc.stdout)
        obs = data["observed"]["corpus"]
        return {
            "tracked_files": obs["tracked_files"],
            "unindexed": obs["unindexed"],
            "report_total": obs["report_total"],
            "commit_total": obs["commit_total"],
        }


def check(repo: Path, rev: str, root: Path, records_override: dict[str, str] | None = None,
          observed_override: dict[str, int] | None = None) -> tuple[int, list[str]]:
    findings: list[str] = []
    records = dict(records_override or {})
    missing_records = False
    if not records_override:
        for path in RECORDS:
            text = _git_show(repo, rev, path)
            if text is None:
                missing_records = True
                findings.append("D1: cannot read the round-68 records at this revision "
                                f"— a missing records file is a content verdict, not an environment error ({path})")
                continue
            records[path] = text
    if missing_records:
        # Missing records are a content verdict: the round has not recorded yet.
        return 0, findings
    joined = "\n".join(records.values())
    closed = 0
    # D1 — the appended correction names the observed base line.
    if OBSERVED in joined:
        closed += 1
    else:
        findings.append("D1: no record carries the appended correction naming "
                        f"the observed `{OBSERVED}` line")
    # D2 — the real receipt path is named.
    if REAL_RECEIPT in joined:
        closed += 1
    else:
        findings.append(f"D2: no record names the real receipt path {REAL_RECEIPT}")
    # D3 — the control mirror is disclosed and gone from the working tree.
    if JUNK in joined and not (repo / JUNK).exists():
        closed += 1
    else:
        findings.append(f"D3: the disclosure of {JUNK} is missing, or the path still exists")
    # D4 — the spot-check is indexed and the baseline matches the gate's own measurement.
    readme = (root / README).read_text(encoding="utf-8")
    indexed = False
    for line in readme.splitlines():
        if not line.startswith("|"):
            continue
        cells = [c.strip() for c in line[1:].split("|")]
        if len(cells) >= 2 and cells[1].strip() == f"`lessons/{Path(SPOTCHECK).name}`":
            indexed = True
            break
    if not indexed:
        findings.append(f"D4: {SPOTCHECK} has no coverage-map index row")
    else:
        baseline = json.loads((root / BASELINE).read_text(encoding="utf-8"))
        checks = baseline.get("checks", {})
        expect = {
            "corpus.index.tracked_files": checks.get("corpus.index.tracked_files", {}).get("expect"),
            "corpus.index.unindexed": checks.get("corpus.index.unindexed", {}).get("expect"),
            "corpus.pointers.report_total": checks.get("corpus.pointers.report_total", {}).get("expect"),
            "corpus.pointers.commit_total": checks.get("corpus.pointers.commit_total", {}).get("expect"),
        }
        observed = observed_override if observed_override is not None else _baseline_values(repo, rev)
        mapping = {
            "corpus.index.tracked_files": observed["tracked_files"],
            "corpus.index.unindexed": observed["unindexed"],
            "corpus.pointers.report_total": observed["report_total"],
            "corpus.pointers.commit_total": observed["commit_total"],
        }
        for key, value in mapping.items():
            if expect.get(key) != value:
                findings.append(f"D4: baseline {key} expects {expect.get(key)!r}, "
                                f"the gate's own measurement yields {value!r}")
        else:
            if not findings:
                closed += 1
    if findings:
        return closed, findings
    return closed, []


def selftest(repo: Path) -> int:
    """One honest world and one broken world per routed defect.

    The worlds are synthetic: the records and the gate measurement are injected, so the
    self-test never touches the repository and never runs the corpus gate.
    """
    good_records = {
        "LOG.md": f"the observed base line was\n{OBSERVED}\n{REAL_RECEIPT}\n{JUNK}\n",
        "SCORECARD.md": f"{OBSERVED}\n",
        "corpus/lessons/round-68.md": f"{REAL_RECEIPT}\n{JUNK}\n",
    }
    good_readme = f"| Round-67 spot-check | `lessons/{Path(SPOTCHECK).name}` | x |\n"
    good_baseline = json.dumps({"checks": {
        "corpus.index.tracked_files": {"expect": 7},
        "corpus.index.unindexed": {"expect": 0},
        "corpus.pointers.report_total": {"expect": 5},
        "corpus.pointers.commit_total": {"expect": 4},
    }})
    observed = {"tracked_files": 7, "unindexed": 0, "report_total": 5, "commit_total": 4}

    def run_world(records, readme, baseline, junk_exists):
        with tempfile.TemporaryDirectory(prefix="k68-selftest-") as tmp:
            root = Path(tmp)
            (root / README).parent.mkdir(parents=True, exist_ok=True)
            (root / BASELINE).parent.mkdir(parents=True, exist_ok=True)
            (root / README).write_text(readme, encoding="utf-8")
            (root / BASELINE).write_text(baseline, encoding="utf-8")
            (root / JUNK).mkdir(parents=True, exist_ok=True)
            if not junk_exists:
                (root / JUNK).rmdir()
            return check(Path("/nonexistent"), "rev", root,
                         records_override=records, observed_override=dict(observed))

    failures = 0
    n, findings = run_world(good_records, good_readme, good_baseline, False)
    if n != TOTAL:
        print(f"FAIL honest world: closed {n} of {TOTAL}; {findings}", file=sys.stderr)
        failures += 1
    else:
        print(f"PASS honest world: closed {TOTAL} of {TOTAL}")

    broken = {
        "D1 correction absent": ({k: v for k, v in good_records.items() if OBSERVED not in v},
                                 good_readme, good_baseline, False),
        "D2 receipt path absent": ({k: v for k, v in good_records.items() if REAL_RECEIPT not in v},
                                   good_readme, good_baseline, False),
        "D3 disclosure absent": ({k: v for k, v in good_records.items() if JUNK not in v},
                                 good_readme, good_baseline, False),
        "D4 index row absent": (good_records, good_readme.replace(
            f"`lessons/{Path(SPOTCHECK).name}`", "`lessons/absent.md`"), good_baseline, False),
        "D4 stale baseline": (good_records, good_readme, json.dumps({"checks": {
            "corpus.index.tracked_files": {"expect": 1},
            "corpus.index.unindexed": {"expect": 0},
            "corpus.pointers.report_total": {"expect": 5},
            "corpus.pointers.commit_total": {"expect": 4}}}), False),
    }
    for name, (records, readme, baseline, junk) in broken.items():
        n, findings = run_world(records, readme, baseline, junk)
        if n == TOTAL:
            print(f"FAIL broken world survived: {name} -> closed {n}", file=sys.stderr)
            failures += 1
        else:
            print(f"PASS broken world rejected: {name}")
    print(f"self-test: {failures} failure(s) over {len(broken) + 1} assertions")
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
        if not args.rev:
            raise EnvError("--rev <full-sha> is required")
        with tempfile.TemporaryDirectory(prefix="k68-repairs-") as tmp:
            root = _materialize(repo, args.rev, Path(tmp))
            n, findings = check(repo, args.rev, root)
    except EnvError as exc:
        print(f"environment error: {exc}", file=sys.stderr)
        return 2
    print(f"r67 routed defects closed {n} of {TOTAL}")
    for f in findings:
        print(f"  - {f}")
    return 0 if n == TOTAL else 1


if __name__ == "__main__":
    sys.exit(main())
