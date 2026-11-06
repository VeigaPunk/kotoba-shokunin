#!/usr/bin/env python3
"""MutTesterAnchorR100 (round 100): mutation probe on the C2 candidate.

Mutates the NEW regex (strip_token_dressing fix line) and the NEW self-test arms
of verifiers/verify_skill_checklist.py in the candidate checkout, runs the
checklist's own --self-test (the detector the C2 kill conjunct uses), and
classifies KILLED / SURVIVED.  For every survivor it searches a token pool for
a witness token whose public-check verdict differs from the honest module.

Usage: python3 -B mutate_anchor.py CANDIDATE_REPO
Writes nothing outside CANDIDATE_REPO's working tree (restored byte-exactly).
"""
from __future__ import annotations

import hashlib
import importlib.util
import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

CK = "verifiers/verify_skill_checklist.py"
FIX = '    m = re.match(r"^(.+\\.\\w+):\\d+(-\\d+)?(,\\d+(-\\d+)?)*$", tok)\n'
RSTRIP = "    tok = tok.rstrip(TRAILING_PUNCT)\n"
ARM_TAIL = "    for f in failures:\n"
X = "corpus/lessons/x.md"

# ---- regex mutants: (id, description, old, new) ---------------------------
REGEX = [
    ("R1-single-element", "the comma group loses its `*` (one list item only)",
     '(,\\d+(-\\d+)?)*$", tok)', '(,\\d+(-\\d+)?)$", tok)'),
    ("R2-plus", "`+` instead of `*` (a comma item is required)",
     '(,\\d+(-\\d+)?)*$", tok)', '(,\\d+(-\\d+)?)+$", tok)'),
    ("R3-charclass", "the whole anchor becomes a character class",
     ':\\d+(-\\d+)?(,\\d+(-\\d+)?)*$", tok)', ':[\\d,-]+$", tok)'),
    ("R4-unanchored", "the trailing `$` is dropped",
     '(,\\d+(-\\d+)?)*$", tok)', '(,\\d+(-\\d+)?)*", tok)'),
    ("R5-space-after-comma", "`\\s*` admitted after a comma",
     '(,\\d+(-\\d+)?)*$", tok)', '(,\\s*\\d+(-\\d+)?)*$", tok)'),
    ("R6-no-rstrip", "the trailing-punctuation rstrip is dropped",
     RSTRIP, ""),
    ("R7-no-range", "the `(-\\d+)?` range group is dropped",
     ':\\d+(-\\d+)?(,\\d+(-\\d+)?)*$", tok)', ':\\d+(,\\d+(-\\d+)?)*$", tok)'),
    ("R8-cap-two", "the comma group is capped at two items",
     '(,\\d+(-\\d+)?)*$", tok)', '(,\\d+(-\\d+)?){0,2}$", tok)'),
    ("R9-optional-trailing-comma", "an optional trailing comma joins the regex",
     '(,\\d+(-\\d+)?)*$", tok)', '(,\\d+(-\\d+)?)*,?$", tok)'),
    ("R10-empty-digits", "the first `\\d+` becomes `\\d*`",
     '):\\d+(-\\d+)?', '):\\d*(-\\d+)?'),
]

POOL = [
    X + ":30,37", X + ":3,7-9", X + ":30,37,", X + ":10,18,34,40-42",
    X + ":42", X + ":1-2", X, X + ":30, 37", X + ":", X + ":0",
    X + ":30,abc", X + ":30,,37", X + ":5-", X + ":,30", X + ":abc",
    "corpus/lessons/missing.md:30,37",
]


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def once(text: str, old: str, new: str, what: str) -> str:
    if text.count(old) != 1:
        raise SystemExit("%s: anchor %r occurs %d times" % (what, old, text.count(old)))
    return text.replace(old, new, 1)


def run_selftest(repo: Path) -> tuple[int, str]:
    p = subprocess.run([sys.executable, "-B", CK, "--self-test"], cwd=str(repo),
                       capture_output=True, text=True, timeout=900)
    return p.returncode, p.stdout + p.stderr


def verdict(rc: int, out: str) -> tuple[str, str]:
    lines = [ln for ln in out.strip().splitlines() if ln.strip()]
    last = lines[-1][:120] if lines else "<no output>"
    fails = [ln for ln in out.splitlines() if ln.startswith("self-test FAIL: ")]
    killed = rc == 1 and bool(fails) and "failure(s) over" in last
    return ("KILLED" if killed else "SURVIVED"), last


def load(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def world(root: Path, tag: str) -> Path:
    w = Path(tempfile.mkdtemp(prefix=tag + "-", dir=str(root)))
    (w / "corpus" / "lessons").mkdir(parents=True)
    (w / X).write_text("".join("line %d\n" % i for i in range(1, 41)), encoding="utf-8")
    return w


def verdicts(mod, root: Path) -> dict[str, str]:
    """public check verdict per pool token (trigger path)."""
    out = {}
    for tok in POOL:
        w = world(root, "w")
        try:
            st = mod.check_citation_resolves(["- `%s`" % tok], w)[0]
        except Exception as exc:
            st = "EXC %s" % type(exc).__name__
        finally:
            shutil.rmtree(w, ignore_errors=True)
        out[tok] = st
    return out


def main(argv: list[str]) -> int:
    repo = Path(argv[0]).resolve()
    top = subprocess.run(["git", "-C", str(repo), "rev-parse", "--show-toplevel"],
                         capture_output=True, text=True).stdout.strip()
    if Path(top) != repo:
        raise SystemExit("not the candidate checkout: %s" % top)
    ck = repo / CK
    honest = ck.read_bytes()
    honest_sha = sha(honest)
    text0 = honest.decode("utf-8")
    if text0.count(FIX) != 1:
        raise SystemExit("candidate fix line not unique")
    root = Path(tempfile.mkdtemp(prefix="mut-", dir=os.environ["TMPDIR"]))
    try:
        # honest reference verdicts, from a copy so the tree is never left dirty
        ref = root / "honest.py"
        ref.write_bytes(honest)
        hmod = load(ref, "honest_ck")
        hv = verdicts(hmod, root)
        rc, out = run_selftest(repo)
        v, last = verdict(rc, out)
        print("honest: selftest exit %d last %r -> %s (expected SURVIVED: no mutant)"
              % (rc, last, v))
        print("honest sha256 %s" % honest_sha)

        for mid, desc, old, new in REGEX:
            mut = once(text0, old, new, mid)
            ck.write_text(mut, encoding="utf-8")
            try:
                rc, out = run_selftest(repo)
            finally:
                ck.write_bytes(honest)
            v, last = verdict(rc, out)
            fails = [ln for ln in out.splitlines() if ln.startswith("self-test FAIL: ")]
            witness = ""
            if v == "SURVIVED":
                mp = root / (mid + ".py")
                mp.write_text(mut, encoding="utf-8")
                mv = verdicts(load(mp, "m_" + mid.replace("-", "_")), root)
                diff = [t for t in POOL if mv[t] != hv[t]]
                witness = ("witness " + "; ".join("%r honest=%s mutant=%s"
                                                  % (t, hv[t], mv[t]) for t in diff)) if diff \
                    else "no pool token differs (equivalent on the pool)"
            print("mutant %s (%s): %s | selftest exit %d last %r | %s | restored %s"
                  % (mid, desc, v, rc, last, witness or ("caught by " + "; ".join(
                      f.split(": got")[0] for f in fails[:3])), sha(ck.read_bytes()) == honest_sha))
            if sha(ck.read_bytes()) != honest_sha:
                raise SystemExit("RESTORE FAILED after %s" % mid)

        # ---- arm mutants ---------------------------------------------------
        arms_old = text0[text0.index(ARM_TAIL) - 0:]  # anchor only; block found below
        start = text0.index("    # Round 100 (claim C2): a comma-list line anchor")
        block = text0[start:text0.index(ARM_TAIL)]
        arm_mutants = [
            ("A1-no-governance-arms", "the governance ok_tokens loop is dropped",
             block, block[:block.index("        for index, token in enumerate(ok_tokens):\n"
                                       "            try:\n"
                                       "                (comma_world / \"LOG.md\")")]
             + block[block.index("        for index, token in enumerate(red_tokens):\n"
                                 "            try:\n"
                                 "                (comma_world / \"LOG.md\")"):]),
            ("A2-no-red-arms", "both red_tokens loops are dropped",
             block, block[:block.index("        for index, token in enumerate(red_tokens):\n"
                                       "            try:\n"
                                       "                status, _, detail = check_citation_resolves(")]
             + "\n"),
            ("A3-source-sniff", "the arms are replaced by a source sniff",
             block, '''    # round-100 C2: the comma-list branch is present in this module.
    _src = Path(__file__).read_text(encoding="utf-8")
    _marker = ":" + chr(92) + "d+(-" + chr(92) + "d+)?(," + chr(92) + "d+"
    rec("strip_token_dressing: comma-list branch present in the source",
        _src.count(_marker) == 1, _src.count(_marker))
'''),
            ("A4-not-fail-is-pass", "the ok arms accept anything but FAIL (N/A passes)",
             block, block.replace('status == "PASS", status)',
                                  'status != "FAIL", status)')),
        ]
        for aid, adesc, old, new in arm_mutants:
            if text0.count(old) != 1:
                print("arm mutant %s: anchor occurs %d times -- skipped"
                      % (aid, text0.count(old)))
                continue
            mut = text0.replace(old, new, 1)
            ck.write_text(mut, encoding="utf-8")
            try:
                rc, out = run_selftest(repo)
            finally:
                ck.write_bytes(honest)
            v, last = verdict(rc, out)
            # which regex mutant now survives behind this weakened arm?
            behind = []
            for mid, desc, ro, rn in REGEX:
                if mid == "R9-optional-trailing-comma":
                    continue
                both = mut.replace(ro, rn, 1) if mut.count(ro) == 1 else None
                if both is None:
                    continue
                ck.write_text(both, encoding="utf-8")
                try:
                    rc2, out2 = run_selftest(repo)
                finally:
                    ck.write_bytes(honest)
                v2, _ = verdict(rc2, out2)
                if v2 == "SURVIVED":
                    behind.append(mid)
            print("arm-mutant %s (%s): self-test %s (exit %d last %r); regex mutants "
                  "that survive behind it: %s | restored %s"
                  % (aid, adesc, v, rc, last, ", ".join(behind) or "none",
                     sha(ck.read_bytes()) == honest_sha))
            if sha(ck.read_bytes()) != honest_sha:
                raise SystemExit("RESTORE FAILED after %s" % aid)
    finally:
        ck.write_bytes(honest)
        shutil.rmtree(root, ignore_errors=True)
    print("final restore sha256 %s (honest %s) %s"
          % (sha(ck.read_bytes()), honest_sha, "OK" if sha(ck.read_bytes()) == honest_sha else "FAIL"))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
