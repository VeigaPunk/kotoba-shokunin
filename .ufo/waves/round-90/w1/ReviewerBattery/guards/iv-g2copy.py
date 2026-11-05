import sys, importlib.util, hashlib, tempfile, os
from pathlib import Path
spec = importlib.util.spec_from_file_location("cmb_g2", "verifiers/check_mutation_battery.py")
mod = importlib.util.module_from_spec(spec); sys.modules["cmb_g2"]=mod; spec.loader.exec_module(mod)
w = Path(tempfile.mkdtemp())
good = b"id\ttarget\tclass\trecipe\tdisposition\n"
p = w/"m.tsv"
mod.place(p, good, mod.sha256(good), "honest")
print("honest place: PASS rc=0")
try:
    mod.place(p, good+b"tamper\n", mod.sha256(good), "tampered")
    print("TAMPER UNDETECTED (finding)")
except mod.CouldNotEvaluate as e:
    print("TAMPER caught:", e)
# partial-block byte prefix (truncate mid-copy)
trunc = good[:-10]
try:
    mod.place(p, trunc, mod.sha256(good), "truncated")
    print("TRUNCATION UNDETECTED (finding)")
except mod.CouldNotEvaluate as e:
    print("TRUNCATION caught:", e)
import shutil; shutil.rmtree(w)
