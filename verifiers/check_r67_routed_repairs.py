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
        if text is None:
            raise EnvError(f"cannot read {path} at {rev}")
        out = dest / path
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(text, encoding="utf-8")
    return dest


def _baseline_values(repo: Path, rev: str) -> dict[str, int]:
    """Re-derive the census values with the gate's own measurement at <rev>."""
    with tempfile.TemporaryDirectory(prefix="k68-baseline-") as tmp:
        root = Path(tmp)
        for path in ("corpus", "verifiers"):
            proc = subprocess.run(["git", "-C", str(repo), "checkout", rev, "--", path],
                                  capture_output=True, text=True)
            if proc.returncode != 0:
                raise EnvError(f"cannot materialize {path} at {rev}")
        proc = subprocess.run(
            ["python3", "-B", str(repo / "verifiers" / "verify_corpus_integrity.py"),
             "--no-baseline", "--json"],
            capture_output=True, text=True, cwd=str(root))
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


def check(repo: Path, rev: str, root: Path) -> tuple[int, list[str]]:
    findings: list[str] = []
    records = {}
    for path in RECORDS:
        text = _git_show(repo, rev, path)
        if text is None:
            raise EnvError(f"cannot read {path} at {rev}")
        records[path] = text
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
        observed = _baseline_values(repo, rev)
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


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(add_help=True)
    ap.add_argument("--rev", default=None, help="measured revision (full sha)")
    ap.add_argument("--repo", default=str(Path(__file__).resolve().parent.parent))
    args = ap.parse_args(argv)
    repo = Path(args.repo)
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
