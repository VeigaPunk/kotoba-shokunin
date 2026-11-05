import sys, importlib.util
from pathlib import Path
sys.dont_write_bytecode = True
D = Path(sys.argv[1]); S = Path(sys.argv[2]); REV = sys.argv[3]; BASE = "223ae62424f8ab1eb365d733eb648d6228ddd7e8"
spec = importlib.util.spec_from_file_location("r86", str(D / "verifiers" / "check_r86_routed_repairs.py"))
m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
ok, msg = m.check_d5(D, REV, S, "landing", Path("/nonexistent"), BASE)
print("FROZEN check_d5 ->", "PASS" if ok else "FAIL", "|", msg[:400])
