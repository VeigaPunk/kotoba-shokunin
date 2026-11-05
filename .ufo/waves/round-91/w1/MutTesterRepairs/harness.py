#!/usr/bin/env python3
"""MutTesterRepairs harness: fresh clone per mutant, one exact-match edit, scratch commit, three bounded probes.

Probes (each under a 120 s cap, the same probes on pristine and mutant):
  floors : python3 -B verifiers/check_assertion_floors.py --self-test
  tip    : check_tip_battery.run_guards(repo, base, rev) via tipguard.py (instrument-pin and the other guards)
  gate   : python3 -B verifiers/check_freeze_gate.py --self-test
"""
import json, os, shutil, subprocess, sys, time
from concurrent.futures import ThreadPoolExecutor

T = os.environ["TMPDIR"]
CAND = os.path.join(T, "repo")
BASE = "9af1a7af2adf0ab07cfd53f92affc1ed8d992262"
MROOT = os.path.join(T, "mutants")
PROBE_CAP = 120

FLOORS = "verifiers/check_assertion_floors.py"
TIP = "verifiers/check_tip_battery.py"
GATE = "verifiers/check_freeze_gate.py"
REG = "verifiers/floors-registry.json"

MUTANTS = [
    ("m1", "cap back to 120",
     [(FLOORS, "SELF_TEST_TIMEOUT_S = 360\n", "SELF_TEST_TIMEOUT_S = 120\n")]),
    ("m2", "MEASURED_SELFTEST_S set to 1",
     [(FLOORS, "MEASURED_SELFTEST_S = 161  #", "MEASURED_SELFTEST_S = 1  #")]),
    ("m3", "floors_guard floor row lowered by one (floors-registry.json row only)",
     [(REG, '"floor": 176,\n      "path": "verifiers/check_assertion_floors.py"',
       '"floor": 175,\n      "path": "verifiers/check_assertion_floors.py"')]),
    ("m3b", "floors_guard floor lowered by one in both in-file tables (JSON unchanged)",
     [(FLOORS, '    "floors_guard": 176,', '    "floors_guard": 175,'),
      (FLOORS, '"floors_guard": ("verifiers/check_assertion_floors.py", 176,',
       '"floors_guard": ("verifiers/check_assertion_floors.py", 175,')]),
    ("m4", "INSTRUMENT_PINS admission entry 6f2c52fb deleted",
     [(TIP, '        "6f2c52fb2e09e817dff3360b97400a5d6e53626c"),', '        ),')]),
    ("m5", "one byte in check_assertion_floors.py, behavioural (SELF_TEST_TIMEOUT_MAX_SCALE 15.0 -> 15.1)",
     [(FLOORS, "SELF_TEST_TIMEOUT_MAX_SCALE = 15.0\n", "SELF_TEST_TIMEOUT_MAX_SCALE = 15.1\n")]),
    ("m5b", "one byte in check_assertion_floors.py, comment only ('Round 91 (claim C2 leg A(a)-(b)' -> 'Round 92')",
     [(FLOORS, "# Round 91 (claim C2 leg A(a)-(b)", "# Round 92 (claim C2 leg A(a)-(b)")]),
    ("m6", "self-test timeout enforcement (subprocess.run timeout=cap) replaced by no-op timeout=None",
     [(FLOORS, "timeout=cap)", "timeout=None)")]),
    ("m7", "ladder repair reverted in check_freeze_gate.py: except (OSError, UnicodeError) -> except OSError",
     [(GATE, "    except (OSError, UnicodeError) as exc:", "    except OSError as exc:")]),
]


def run(cmd, cwd, env, timeout=PROBE_CAP):
    t0 = time.time()
    try:
        p = subprocess.run(cmd, cwd=cwd, env=env, capture_output=True, text=True, timeout=timeout)
        return {"rc": p.returncode, "out": p.stdout, "err": p.stderr, "wall": round(time.time() - t0, 1)}
    except subprocess.TimeoutExpired as e:
        out = e.stdout.decode("utf-8", "replace") if isinstance(e.stdout, bytes) else (e.stdout or "")
        return {"rc": "TIMEOUT", "out": out, "err": "", "wall": round(time.time() - t0, 1)}


def env_for(name, kind):
    d = os.path.join(T, "tmp-%s-%s" % (name, kind))
    shutil.rmtree(d, ignore_errors=True)
    os.makedirs(d)
    e = dict(os.environ)
    e["TMPDIR"] = d
    return e


def fails_of(out):
    return [l.strip() for l in out.splitlines() if "FAIL" in l]


def probe(repo, name, kind, rev):
    env = env_for(name, kind)
    if kind == "floors":
        cmd = [sys.executable, "-B", FLOORS, "--self-test"]
    elif kind == "gate":
        cmd = [sys.executable, "-B", GATE, "--self-test"]
    elif kind == "tip":
        cmd = [sys.executable, "-B", os.path.join(T, "tipguard.py"), repo, BASE, rev]
    else:
        raise ValueError(kind)
    r = run(cmd, repo, env)
    summary = [l for l in r["out"].splitlines() if "failure(s) over" in l or l.startswith("guard-failures")]
    f = fails_of(r["out"])
    r["summary"] = summary[-1] if summary else ""
    r["fail_count"] = len(f)
    r["first_fail"] = f[0][:240] if f else ""
    r["err_tail"] = r["err"].strip().splitlines()[-1][:240] if r["err"].strip() else ""
    r["out_head"] = r["out"][:400]
    return r


def make_mutant(mid, edits):
    d = os.path.join(MROOT, mid)
    shutil.rmtree(d, ignore_errors=True)
    os.makedirs(MROOT, exist_ok=True)
    subprocess.run(["git", "clone", "-q", "--shared", CAND, d], check=True)
    subprocess.run(["git", "-C", d, "checkout", "-q", "HEAD"], check=True)
    for path, old, new in edits:
        fp = os.path.join(d, path)
        src = open(fp, encoding="utf-8").read()
        n = src.count(old)
        assert n == 1, (mid, path, n)
        open(fp, "w", encoding="utf-8").write(src.replace(old, new, 1))
    subprocess.run(["git", "-C", d, "add", "-A"], check=True)
    subprocess.run(["git", "-C", d, "-c", "user.name=scratch", "-c", "user.email=scratch@invalid",
                    "commit", "-q", "-m", "mutant " + mid], check=True)
    rev = subprocess.run(["git", "-C", d, "rev-parse", "HEAD"], capture_output=True, text=True, check=True).stdout.strip()
    top = subprocess.run(["git", "-C", d, "rev-parse", "--show-toplevel"], capture_output=True, text=True, check=True).stdout.strip()
    assert top == d, (top, d)
    stat = subprocess.run(["git", "-C", d, "diff", "--numstat", "HEAD~1", "HEAD"], capture_output=True, text=True).stdout.strip()
    return d, rev, stat


def run_mutant(spec):
    mid, desc, edits = spec
    d, rev, stat = make_mutant(mid, edits)
    res = {"id": mid, "desc": desc, "rev": rev, "numstat": stat, "probes": {}}
    for k in ("floors", "tip", "gate"):
        res["probes"][k] = probe(d, mid, k, rev)
    return res


def pristine():
    rev = subprocess.run(["git", "-C", CAND, "rev-parse", "HEAD"], capture_output=True, text=True, check=True).stdout.strip()
    res = {"id": "pristine", "rev": rev, "probes": {}}
    for k in ("floors", "tip", "gate"):
        res["probes"][k] = probe(CAND, "pristine", k, rev)
    return res


if __name__ == "__main__":
    which = sys.argv[1:]
    results = {}
    if not which or "pristine" in which:
        p = pristine()
        results["pristine"] = p
        print("pristine", {k: (v["rc"], v["wall"], v["summary"]) for k, v in p["probes"].items()}, flush=True)
    specs = [m for m in MUTANTS if not which or m[0] in which]
    if specs:
        with ThreadPoolExecutor(max_workers=3) as ex:
            for res in ex.map(run_mutant, specs):
                results[res["id"]] = res
                print(res["id"], res["desc"], {k: (v["rc"], v["fail_count"], v["summary"]) for k, v in res["probes"].items()}, flush=True)
    out = os.path.join(T, "results.json")
    with open(out, "w") as fh:
        json.dump(results, fh, indent=1, default=str)
    print("RESULTS-WRITTEN", out, flush=True)
