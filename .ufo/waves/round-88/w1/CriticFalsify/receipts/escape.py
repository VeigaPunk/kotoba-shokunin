import sys, importlib.util
sys.dont_write_bytecode = True
spec = importlib.util.spec_from_file_location("r87", "/home/vgpnk/Projects/shokunin/kotoba-shokunin/verifiers/check_omp_root_semantics.py")
r = importlib.util.module_from_spec(spec); spec.loader.exec_module(r)
cands = ["/etc/skills", "/tmp/x/skills", "~//etc/skills", "~root/skills", "{cwd}//etc/skills",
         "{cwd}/../x/skills", "~/../../etc/skills", "/home/u/../../etc/skills", "{cwd}/x/..", "~/x/./.."]
for p in cands:
    pp = r.pattern_problem(p)
    ok, why = r.bound_grounded(p, r.FROZEN_CHAIN)
    verdict = "ACCEPTED by conjuncts 1+4" if (pp is None and ok) else "REFUSED"
    print(f"{p!r:28} pattern_problem={pp!r:60.60} bound={ok} {why[:70]!r} -> {verdict}")
