#!/usr/bin/env python3
"""Fast pre-check of each world in the fleet-shaped probe sandbox."""
import re
import subprocess
import sys
from pathlib import Path

P = Path(sys.argv[1]).resolve()
WORLDS = [tuple(x.split("=", 1)) for x in sys.argv[2:]]


def run(*args):
    p = subprocess.run([sys.executable, "-B", *args], cwd=str(P),
                       capture_output=True, text=True)
    return p.returncode, p.stdout + p.stderr


def assertions(text):
    for rx in (r"(\d+) failure\(s\) over (\d+) assertions",
               r"self-test: (\d+) failure\(s\) over (\d+) assertions",
               r"self-test: (\d+) assertions, (\d+) failures"):
        ms = list(re.finditer(rx, text))
        if ms:
            m = ms[-1]
            return int(m.group(2)) if rx.startswith("(") else int(m.group(1))
    return None


for name, rev in WORLDS:
    subprocess.run(["git", "-C", str(P), "checkout", "-q", rev], check=True)
    out = {}
    rc, text = run("verifiers/verify_skill_checklist.py")
    passes = sum(l.startswith("PASS ") for l in text.splitlines())
    others = sum(l.startswith(("FAIL ", "N/A ")) for l in text.splitlines())
    out["chk"] = (rc, passes, others)
    out["chk_last"] = next((l for l in text.splitlines()
                            if l.startswith(("FAIL ", "N/A "))), "")[:120]
    rc, text = run("verifiers/verify_corpus_integrity.py")
    out["int"] = (rc, [l for l in text.splitlines() if l.startswith("DRIFT")][:6])
    rc, text = run("verifiers/verify_corpus_independent.py")
    out["ind"] = rc
    st = []
    for g in ("verifiers/verify_skill_checklist.py",
              "verifiers/verify_corpus_integrity.py",
              "verifiers/verify_corpus_independent.py"):
        rc, text = run(g, "--self-test")
        st.append((rc, assertions(text)))
    out["self"] = st
    print(name, rev[:12], "chk", out["chk"], "int_rc", out["int"][0],
          "drift", out["int"][1], "ind_rc", out["ind"], "self", st)
    if out["chk_last"]:
        print("   ", out["chk_last"])
