import importlib.util
spec = importlib.util.spec_from_file_location("sk", "verifiers/fixtures/round-95/selftest-kills.py")
sk = importlib.util.module_from_spec(spec); spec.loader.exec_module(sk)
cases = {
 "one-line compound (col != indent)": ("def f():\n    x = 1; y = 2\n    return x\n", "def f():\n    x = 1; y = 3\n    return x\n"),
 "decorated def header changed": ("@d\ndef f():\n    return 1\n", "@d\ndef f():\n    return 2\n"),
 "changed line inside multi-line call": ("def f():\n    return g(\n        1,\n        2)\n", "def f():\n    return g(\n        1,\n        3)\n"),
 "line count changed": ("x = 1\n", "x = 1\ny = 2\n"),
 "no line changed": ("x = 1\n", "x = 1\n"),
 "mutant does not compile": ("x = 1\ny = 2\n", "x = 1\ny = (\n"),
 "changed line is an if header": ("def f(a):\n    if a:\n        return 1\n    return 0\n", "def f(a):\n    if not a:\n        return 1\n    return 0\n"),
}
for name, (o, m) in cases.items():
    try:
        d = sk.code_decoy(o, m, "probe")
        compile(d, "p", "exec")
        print("%-38s OK   decoy compiles; guards=%d" % (name, d.count("__decoy__")))
    except sk.NotEvaluated as e:
        print("%-38s NOT-EVALUATED: %s" % (name, e))
    except Exception as e:
        print("%-38s ESCAPES NotEvaluated: %s: %s" % (name, type(e).__name__, e))
