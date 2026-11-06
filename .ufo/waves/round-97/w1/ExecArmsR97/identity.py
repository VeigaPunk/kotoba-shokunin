#!/usr/bin/env python3
"""Prove the candidate instrument is the base bytes plus one contiguous
insertion inside self_test(): prefix and suffix byte-identical, insertion
after `def self_test` and before `def box_proof`."""
import subprocess
import sys
from pathlib import Path

REPO = Path(sys.argv[1])
BASE = "148395bf42af97436b1b832a97a175515f981939"
REL = "verifiers/verify_dispatch_prompts.py"

base = subprocess.run(["git", "-C", str(REPO), "show", "%s:%s" % (BASE, REL)],
                      stdout=subprocess.PIPE, check=True).stdout
cand = (REPO / REL).read_bytes()

p = 0
while p < len(base) and p < len(cand) and base[p] == cand[p]:
    p += 1
s = 0
while s < len(base) - p and s < len(cand) - p and base[-1 - s] == cand[-1 - s]:
    s += 1
inserted = cand[p:len(cand) - s]
rebuilt = base[:p] + inserted + base[len(base) - s:]
print("base bytes %d, candidate bytes %d" % (len(base), len(cand)))
print("common prefix %d, common suffix %d, inserted %d" % (p, s, len(inserted)))
print("reconstructs exactly: %s" % (rebuilt == cand))
print("base is candidate minus the insertion: %s"
      % (cand[:p] + cand[len(cand) - s:] == base))
head = base[:p].decode("utf-8", "replace")
tail = base[len(base) - s:].decode("utf-8", "replace")
top_level = [ln for ln in inserted.decode("utf-8").splitlines()
             if ln and not ln[0].isspace()]
print("insertion point after 'def self_test() -> int:': %s"
      % (head.rfind("def self_test() -> int:") > head.rfind("def box_proof(")))
print("insertion point before the self-test tail: %s"
      % tail.lstrip().startswith("for f in failures:"))
print("last base line before the insertion: %r" % head.splitlines()[-1])
print("first base line after the insertion: %r"
      % (tail.splitlines()[0] if tail else "<eof>"))
print("inserted lines at column 0 (must be none): %d" % len(top_level))
print("inserted text names self_test-only code: %s"
      % ("def lane_case(" in inserted.decode("utf-8")))
ok = (rebuilt == cand and cand[:p] + cand[len(cand) - s:] == base
      and head.rfind("def self_test() -> int:") > head.rfind("def box_proof(")
      and tail.lstrip().startswith("for f in failures:")
      and not top_level)
print("PRODUCTION-IDENTITY-OK" if ok else "PRODUCTION-IDENTITY-BROKEN")
sys.exit(0 if ok else 1)
