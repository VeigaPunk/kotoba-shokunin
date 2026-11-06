#!/usr/bin/env python3
"""MutTesterAnchorR100: witness pairs for the arm mutants A1 and A4.

An arm mutant is invisible to the self-test by construction (the self-test
cannot see its own weakening).  The witness is a checker defect that the honest
arms catch and the weakened arms do not.

Usage: python3 -B witness_arms.py CANDIDATE_REPO
"""
from __future__ import annotations

import hashlib
import subprocess
import sys
from pathlib import Path

CK = "verifiers/verify_skill_checklist.py"
ARM_TAIL = "    for f in failures:\n"

GOV_DEFECT_OLD = """    problems, excused = errata_problems(errata, horizon, log_lines,
                                        subjects, repo)
"""
GOV_DEFECT_NEW = """    subjects = [dict(s, token=s["raw"]) if "," in s["raw"] else s
                for s in subjects]
    problems, excused = errata_problems(errata, horizon, log_lines,
                                        subjects, repo)
"""

TRIG_DEFECT_OLD = """            if tok.startswith(("http", "~", "-")):
                continue
"""
TRIG_DEFECT_NEW = """            if tok.startswith(("http", "~", "-")):
                continue
            if (re.search(r":\\d+(-\\d+)?(,\\d+(-\\d+)?)+,?$", tok)
                    and "missing.md" not in tok):
                continue
"""


def sha(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


def run(repo: Path) -> tuple[int, str]:
    p = subprocess.run([sys.executable, "-B", CK, "--self-test"], cwd=str(repo),
                       capture_output=True, text=True, timeout=900)
    return p.returncode, p.stdout + p.stderr


def verdict(rc: int, out: str) -> str:
    fails = [ln for ln in out.splitlines() if ln.startswith("self-test FAIL: ")]
    lines = [ln for ln in out.strip().splitlines() if ln.strip()]
    last = lines[-1] if lines else ""
    return ("KILLED" if rc == 1 and fails and "failure(s) over" in last else "SURVIVED")


def main(argv: list[str]) -> int:
    repo = Path(argv[0]).resolve()
    ck = repo / CK
    honest = ck.read_bytes()
    hs = sha(honest)
    t = honest.decode("utf-8")
    start = t.index("    # Round 100 (claim C2): a comma-list line anchor")
    block = t[start:t.index(ARM_TAIL)]
    a1 = block[:block.index('        for index, token in enumerate(ok_tokens):\n'
                            '            try:\n'
                            '                (comma_world / "LOG.md")')] + \
        block[block.index('        for index, token in enumerate(red_tokens):\n'
                          '            try:\n'
                          '                (comma_world / "LOG.md")'):]
    a4 = block.replace('status == "PASS", status)', 'status != "FAIL", status)')
    if t.count(block) != 1 or t.count(GOV_DEFECT_OLD) != 1 or t.count(TRIG_DEFECT_OLD) != 1:
        raise SystemExit("anchors not unique")
    cases = [
        ("gov-defect alone (honest arms)", t.replace(GOV_DEFECT_OLD, GOV_DEFECT_NEW, 1)),
        ("gov-defect + A1 (governance arms dropped)",
         t.replace(GOV_DEFECT_OLD, GOV_DEFECT_NEW, 1).replace(block, a1, 1)),
        ("trigger-defect alone (honest arms)", t.replace(TRIG_DEFECT_OLD, TRIG_DEFECT_NEW, 1)),
        ("trigger-defect + A4 (not-FAIL counts as pass)",
         t.replace(TRIG_DEFECT_OLD, TRIG_DEFECT_NEW, 1).replace(block, a4, 1)),
    ]
    try:
        for name, text in cases:
            ck.write_text(text, encoding="utf-8")
            try:
                rc, out = run(repo)
            finally:
                ck.write_bytes(honest)
            lines = [ln for ln in out.strip().splitlines() if ln.strip()]
            first = next((ln for ln in out.splitlines() if ln.startswith("self-test FAIL: ")), "")
            print("%s: %s (exit %d, last %r) %s | restored %s"
                  % (name, verdict(rc, out), rc, lines[-1][:80] if lines else "",
                     first[:110], sha(ck.read_bytes()) == hs))
    finally:
        ck.write_bytes(honest)
    print("final restore %s" % ("OK" if sha(ck.read_bytes()) == hs else "FAIL"))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
