import importlib.util, sys, difflib, ast
from pathlib import Path
spec = importlib.util.spec_from_file_location("sk", "verifiers/fixtures/round-95/selftest-kills.py")
sk = importlib.util.module_from_spec(spec); spec.loader.exec_module(sk)
orig = Path("verifiers/check_mutation_battery.py").read_text(encoding="utf-8")
for claim in ("c1", "r94c1"):
    for name, a, c, w in sk.CLAIMS[claim]["targets"]:
        try:
            m = sk.mutant_text(name, a, c, w) if hasattr(sk, "mutant_text") else orig.replace(a, w)
        except Exception as e:
            m = orig.replace(a, w)
        try:
            d = sk.code_decoy(orig, m, name)
        except sk.NotEvaluated as e:
            print(claim, name, "NOT-EVALUATED", e); continue
        ast.parse(d)
        n_guard = d.count('if __name__ == "__decoy__":')
        print("==", claim, name, "guards inserted:", n_guard, "| compiles; mutant tokens in decoy:", w in d, "| comment-decoy tokens:", w in orig)
        for ln in difflib.unified_diff(orig.splitlines(), d.splitlines(), lineterm="", n=0):
            if ln.startswith(("+", "-")) and not ln.startswith(("+++", "---")):
                print("   ", ln[:150])
# classify table
cases = [
 (1, "x\n1 failure(s) over 3 assertions\nFAIL a\n", "REPORTED-FAILURE"),
 (1, "1 failure(s) over 3 assertions\n", "RUN-ERROR"),
 (0, "1 failure(s) over 3 assertions\nFAIL a\n", "RUN-ERROR"),
 (0, "0 failure(s) over 3 assertions\n", "CLEAN"),
 (1, "0 failure(s) over 3 assertions\n", "RUN-ERROR"),
 (1, "Traceback...\nRuntimeError: x\n", "RUN-ERROR"),
 (2, "1 failure(s) over 3 assertions\nFAIL a\n", "RUN-ERROR"),
 (1, "FAIL a\n1 failure(s) over 3 assertions\n0 failure(s) over 3 assertions\n", "RUN-ERROR"),
 (1, "FAIL a\n0 failure(s) over 3 assertions\n1 failure(s) over 3 assertions\n", "REPORTED-FAILURE"),
 (1, "  FAIL a\n1 failure(s) over 3 assertions\n", "RUN-ERROR"),
 (-9, "1 failure(s) over 3 assertions\nFAIL a\n", "RUN-ERROR"),
]
for rc, out, want in cases:
    got = sk.classify(rc, out)
    print("classify", rc, repr(out[:40]), got, "OK" if got == want else "MISMATCH want " + want)
