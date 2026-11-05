import os, subprocess, sys, shutil
R = "/fast/scratch/hyaku/kotoba-r91/ExecFloorsCap/repo"
T = os.environ["TMPDIR"]
src = open(os.path.join(R, "verifiers/check_assertion_floors.py")).read()
MUTS = [
    ("cap120", "SELF_TEST_TIMEOUT_S = 360", "SELF_TEST_TIMEOUT_S = 120"),
    ("measured100", "MEASURED_SELFTEST_S = 161  #", "MEASURED_SELFTEST_S = 100  #"),
    ("noclamp", "min(max(1.0, load), SELF_TEST_TIMEOUT_MAX_SCALE)", "min(max(1.0, load), 1.0)"),
    ("nocap", "timeout=cap)", "timeout=cap * 1000)"),
]
for name, old, new in MUTS:
    assert src.count(old) == 1, (name, src.count(old))
    d = os.path.join(T, "m-" + name)
    shutil.rmtree(d, ignore_errors=True)
    shutil.copytree(os.path.join(R, "verifiers"), os.path.join(d, "verifiers"))
    open(os.path.join(d, "verifiers/check_assertion_floors.py"), "w").write(src.replace(old, new, 1))
    p = subprocess.run([sys.executable, "-B", "verifiers/check_assertion_floors.py", "--self-test"],
                       cwd=d, capture_output=True, text=True)
    lines = p.stdout.splitlines()
    print("== %s rc=%d :: %s" % (name, p.returncode, lines[0] if lines else p.stderr[-200:]))
    for l in lines:
        if l.startswith("FAIL") or "C2 leg" in l:
            print("   ", l[:170])
