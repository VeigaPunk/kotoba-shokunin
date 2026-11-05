#!/usr/bin/env python3
"""Replay the three C1 battery-guard mutants (manifest recipes) on a checkout's bytes.

usage: mutreplay.py <repo> <manifest-rev-or-"worktree"> ; runs the instrument's own --self-test
on a mutated copy of verifiers/check_mutation_battery.py inside <repo> (restored afterwards).
"""
import json
import re
import shutil
import subprocess
import sys
from pathlib import Path

repo = Path(sys.argv[1]).resolve()
inst = repo / "verifiers" / "check_mutation_battery.py"
manifest = repo / "verifiers" / "fixtures" / "mutation-battery" / "manifest.tsv"
orig = inst.read_bytes()
rows = [ln.split("\t") for ln in manifest.read_text().splitlines()[1:] if "check_mutation_battery.py" in ln]
for row in rows:
    rid, recipe = row[0], json.loads(row[3])
    text = orig.decode()
    for edit in recipe["edits"]:
        found = re.findall(edit["anchor"], text)
        if len(found) != 1:
            print(rid, "ANCHOR COUNT", len(found))
            break
        text = re.sub(edit["anchor"], lambda m: edit["with"], text, count=1)
    else:
        inst.write_text(text)
        p = subprocess.run([sys.executable, "-B", str(inst), "--self-test"], cwd=str(repo),
                           capture_output=True, text=True, timeout=300)
        tail = [ln for ln in (p.stdout + p.stderr).splitlines() if ln.startswith("FAIL") or "failure(s)" in ln]
        print(rid, "rc=%d" % p.returncode, " | ".join(l[:110] for l in tail))
        inst.write_bytes(orig)
# sanity: restored
assert inst.read_bytes() == orig
print("restored ok")
