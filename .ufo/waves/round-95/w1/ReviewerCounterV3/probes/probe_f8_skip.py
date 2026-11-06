import dis, importlib.util
spec = importlib.util.spec_from_file_location("sk", "verifiers/fixtures/round-95/selftest-kills.py")
sk = importlib.util.module_from_spec(spec); spec.loader.exec_module(sk)
from pathlib import Path
orig = Path("verifiers/check_mutation_battery.py").read_text(encoding="utf-8")
LABEL = "arm kill-set-size: manifest must"
def live_consts(fn):
    ins = list(dis.get_instructions(fn))
    skip = set()
    for i, x in enumerate(ins):
        if x.opname == "LOAD_CONST" and x.argval == "__decoy__":
            for j in range(i + 1, len(ins)):
                if ins[j].opname.startswith("POP_JUMP_IF"):
                    k = j + 1
                    while k < len(ins) and ins[k].offset < ins[j].argval:
                        skip.add(k); k += 1
                    break
    return [x.argval for k, x in enumerate(ins) if k not in skip and isinstance(x.argval, str)]
def ev(text):
    import sys, types
    mod = types.ModuleType("probe_mod"); mod.__file__ = "/nonexistent/x.py"
    sys.modules["probe_mod"] = mod
    exec(compile(text, "x", "exec"), mod.__dict__)
    return mod.evaluate
n5 = orig.replace(*sk.CLAIMS["c1"]["targets"][1][1:3], 1) if False else orig.replace('raise CouldNotEvaluate("manifest must name exactly the targets %s"', 'raise CouldNotEvaluate("arm kill-set-size: manifest must name exactly the targets %s"')
dec = sk.code_decoy(orig, n5, "n5")
print("honest sees label:", any(LABEL in c for c in live_consts(ev(orig).__code__)))
print("n5 mutant sees label:", any(LABEL in c for c in live_consts(ev(n5).__code__)))
print("n5 code-decoy sees label (guard-aware):", any(LABEL in c for c in live_consts(ev(dec).__code__)))
print("n5 code-decoy raw consts sees label:", any(LABEL in c for c in ev(dec).__code__.co_consts if isinstance(c, str)))
