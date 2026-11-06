#!/usr/bin/env python3
"""MutTesterCounterV4 driver: generate counter mutants, run the matrix, compare to committed receipts."""
from __future__ import annotations

import concurrent.futures as cf
import json
import os
import subprocess
import sys
from pathlib import Path

S = Path(__file__).resolve().parent
BASE = "679775abb9277a7b8d17f060b0f5b4ced2b127b6"

# (id, [(anchor, replacement), ...])
MUTANTS = [
    ("M1-classify-rc-only",
     [("    if rc == 1 and n >= 1 and fails >= 1:", "    if rc != 0:")]),
    ("M2-classify-drop-fail-line",
     [("    if rc == 1 and n >= 1 and fails >= 1:", "    if rc == 1 and n >= 1:")]),
    ("M3-code-decoys-skipped",
     [('            held_code += cls == "CLEAN"', "            held_code += 1")]),
    ("M4-comment-decoys-skipped",
     [('            held_comment += cls == "CLEAN"', "            held_comment += 1")]),
    ("M5-runner-writes-mutant-to-disk",
     [('            path.write_text(on_disk, encoding="utf-8")',
       '            path.write_text(text, encoding="utf-8")')]),
    ("M6-honest-clean-conjunct-dropped",
     [('        met = cls_h == "CLEAN" and killed == n and pos == 1 and held_comment == n and held_code == n',
       "        met = killed == n and pos == 1 and held_comment == n and held_code == n")]),
    ("M7-decoy-held-rc0-no-summary",
     [('            held_comment += cls == "CLEAN"', '            held_comment += cls == "CLEAN" or rc == 0'),
      ('            held_code += cls == "CLEAN"', '            held_code += cls == "CLEAN" or rc == 0')]),
    ("M8-positive-forced-killed",
     [('        pos = 1 if cls == "REPORTED-FAILURE" else 0', "        pos = 1")]),
    ("M9a-prefix-ignored",
     [("    fails = sum(1 for ln in out.splitlines() if ln.startswith(fail_prefix))",
       "    fails = sum(1 for ln in out.splitlines() if ln.strip())")]),
    ("M9b-prefix-r95-FAIL",
     [('        "fail_prefix": "self-test FAIL: ",', '        "fail_prefix": "FAIL ",')]),
    ("M10-elif-climb-removed",
     [('        while isinstance(best, ast.If) and o[best.lineno - 1].lstrip().startswith("elif") \\\n'
       '                and isinstance(parent.get(id(best)), ast.If):\n'
       '            best = parent[id(best)]',
       '        while False and isinstance(best, ast.If) and o[best.lineno - 1].lstrip().startswith("elif") \\\n'
       '                and isinstance(parent.get(id(best)), ast.If):\n'
       '            best = parent[id(best)]')]),
    ("M11-instrument-swapped",
     [('        "instrument": DP,', '        "instrument": MB,')]),
    ("M12-anchor-count-weakened",
     [("            if found != count:", "            if found < count:")]),
    ("M13-restore-guard-removed",
     [('        if path.read_text(encoding="utf-8") != original:',
       '        if False and path.read_text(encoding="utf-8") != original:')]),
    ("M14-summary-first-not-last",
     [("    n = int(found[-1][0])", "    n = int(found[0][0])")]),
    ("M15-decoy-guard-always-true",
     [('        block = [indent + \'if __name__ == "__decoy__":\\n\']',
       '        block = [indent + \'if True:\\n\']')]),
    ("M16-killed-counts-run-errors",
     [('            killed += cls == "REPORTED-FAILURE"', '            killed += cls != "CLEAN"')]),
]


def build_mutants() -> None:
    pristine = (S / "counter-pristine.py").read_text(encoding="utf-8")
    out = S / "mutants"
    out.mkdir(exist_ok=True)
    for name, pairs in MUTANTS:
        text = pristine
        for anchor, repl in pairs:
            n = text.count(anchor)
            if n != 1:
                raise SystemExit("anchor for %s matches %d time(s): %r" % (name, n, anchor))
            text = text.replace(anchor, repl)
        if len(text.splitlines()) != len(pristine.splitlines()):
            raise SystemExit("%s changes the line count" % name)
        compile(text, str(out / (name + ".py")), "exec", dont_inherit=True)
        (out / (name + ".py")).write_text(text, encoding="utf-8")
        print("built", name)


def contexts() -> list[tuple[str, str, str]]:
    ctx = [("base", BASE, str(S / "repo"))]
    for line in (S / "forgeries-built.txt").read_text().splitlines():
        name, rev, repo = line.split()
        ctx.append((name, rev, repo))
    return ctx


def run_one(counter: Path, claim: str, rev: str, repo: str, tag: str) -> dict:
    env = dict(os.environ, TMPDIR=str(S / "tmp"), HYAKU_SCRATCH=str(S / "runs" / tag))
    (S / "runs" / tag).mkdir(parents=True, exist_ok=True)
    proc = subprocess.run([sys.executable, "-B", str(counter), claim, rev, repo],
                          stdout=subprocess.PIPE, stderr=subprocess.STDOUT, env=env, timeout=1200)
    text = proc.stdout.decode("utf-8", "replace")
    out = S / "runs" / tag / "out.txt"
    out.write_text(text, encoding="utf-8")
    tail = [ln for ln in text.splitlines() if ln.strip()]
    summary = next((ln for ln in reversed(tail) if " targets killed " in ln), "<no summary>")
    verdict = next((ln for ln in reversed(tail) if "-PREDICATE-" in ln or "-NOT-EVALUATED" in ln), "<no verdict>")
    return {"tag": tag, "counter": counter.name, "claim": claim, "rc": proc.returncode,
            "summary": summary, "verdict": verdict, "out": str(out)}


def main() -> int:
    build_mutants()
    ctx = contexts()
    counters = [("pristine", S / "counter-pristine.py")] + [
        (name, S / "mutants" / (name + ".py")) for name, _ in MUTANTS]
    jobs = []
    for cname, cpath in counters:
        for world, rev, repo in ctx:
            jobs.append((cpath, "c1", rev, repo, "%s__c1__%s" % (cname, world)))
    # r95c1: every mutant (cheap enough at 4-way), positive control only
    for cname, cpath in counters:
        jobs.append((cpath, "r95c1", BASE, str(S / "repo"), "%s__r95c1__base" % cname))
    results = []
    with cf.ThreadPoolExecutor(max_workers=4) as pool:
        futs = [pool.submit(run_one, *j) for j in jobs]
        for f in cf.as_completed(futs):
            r = f.result()
            results.append(r)
            print("done %-52s rc %d  %s" % (r["tag"], r["rc"], r["verdict"]))
    results.sort(key=lambda r: r["tag"])
    (S / "matrix.json").write_text(json.dumps(results, indent=1), encoding="utf-8")
    return 0


if __name__ == "__main__":
    sys.exit(main())
