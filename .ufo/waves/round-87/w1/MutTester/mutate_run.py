#!/usr/bin/env python3
"""MutTester driver: one mutation at a time on a COPY of a counter.

Usage:
  mutate_run.py --counter <src.py> --scratch <dir> --spec <mutations.json>
                [--honest-argv '--rev X' ...] --out <results.json>

Each spec entry: {"name":..., "old":..., "new":..., "expect":"red|green",
                 "arm":"..."}  old must occur exactly once in the copy.
For every mutant we run, in the scratch copy's dir:
  1. python3 -B <copy> --self-test
  2. python3 -B <copy> <honest argv...>
and record rc + captured stdout/stderr + sha256 before/mutated/after.
The copy is restored to pristine bytes after every mutant and the pristine
bytes are re-hashed.
"""
import argparse, hashlib, json, os, shutil, subprocess, sys
from pathlib import Path


def sha256(p):
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for b in iter(lambda: f.read(1 << 20), b""):
            h.update(b)
    return h.hexdigest()


def run(cmd, cwd, timeout=900):
    p = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True, timeout=timeout)
    return p.returncode, p.stdout, p.stderr


def tail(s, n=12):
    lines = [l for l in s.strip().splitlines() if l.strip()]
    return "\n".join(lines[-n:])


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--counter", required=True)
    ap.add_argument("--scratch", required=True)
    ap.add_argument("--spec", required=True)
    ap.add_argument("--honest-argv", default="")
    ap.add_argument("--out", required=True)
    ap.add_argument("--label", default="")
    a = ap.parse_args()

    src = Path(a.counter).resolve()
    scr = Path(a.scratch).resolve()
    scr.mkdir(parents=True, exist_ok=True)
    pristine = scr / ("pristine_" + src.name)
    shutil.copyfile(src, pristine)
    work = scr / src.name
    shutil.copyfile(pristine, work)
    os.chmod(work, 0o755)

    honest = a.honest_argv.split() if a.honest_argv.strip() else []
    spec = json.loads(Path(a.spec).read_text())
    results = []

    base_sha = sha256(work)
    st_rc, st_out, st_err = run([sys.executable, "-B", str(work), "--self-test"], scr)
    h_rc, h_out, h_err = run([sys.executable, "-B", str(work), *honest], scr)
    pristine_record = {
        "mutant": "PRISTINE", "self_test_rc": st_rc,
        "self_test_tail": tail(st_out + st_err),
        "honest_rc": h_rc, "honest_tail": tail(h_out + h_err),
        "sha256": base_sha,
    }
    results.append(pristine_record)
    print("PRISTINE self-test rc=%s | honest rc=%s | sha=%s" % (st_rc, h_rc, base_sha[:16]))
    print(tail(st_out + st_err))

    h_rc_base = h_rc
    text = pristine.read_text()
    for m in spec:
        old, new = m["old"], m["new"]
        n = text.count(old)
        rec = {"mutant": m["name"], "expect": m.get("expect", "red"),
               "arm": m.get("arm", ""), "occurrences": n}
        if n != 1:
            rec["verdict"] = "INCONCLUSIVE"
            rec["note"] = "old string occurs %d times (need exactly 1)" % n
            results.append(rec)
            print("%-28s INCONCLUSIVE occurrences=%d" % (m["name"], n))
            continue
        mutated = text.replace(old, new)
        work.write_text(mutated)
        mut_sha = sha256(work)
        rec["sha256_mutated"] = mut_sha
        st_rc, st_out, st_err = run([sys.executable, "-B", str(work), "--self-test"], scr)
        h_rc, h_out, h_err = run([sys.executable, "-B", str(work), *honest], scr)
        rec["self_test_rc"] = st_rc
        rec["self_test_tail"] = tail(st_out + st_err)
        rec["honest_rc"] = h_rc
        rec["honest_tail"] = tail(h_out + h_err)
        red_st = st_rc != 0
        red_h = h_rc != h_rc_base
        red = red_st or red_h
        rec["red_via"] = ("self-test" if red_st else "") + ("+honest" if red_h else "")
        if m.get("expect") == "green":
            rec["verdict"] = "killed" if not red else "killed(over-red)"
        else:
            rec["verdict"] = "killed" if red else "survived"
        # restore
        shutil.copyfile(pristine, work)
        rec["sha256_after"] = sha256(work)
        rec["restored"] = rec["sha256_after"] == base_sha
        results.append(rec)
        print("%-28s self-test rc=%s honest rc=%s -> %s (restored=%s)"
              % (m["name"], st_rc, h_rc, rec["verdict"], rec["restored"]))

    Path(a.out).write_text(json.dumps({"label": a.label, "counter": str(src),
                                       "pristine_sha256": base_sha,
                                       "results": results}, indent=2))
    print("\nwrote", a.out)


if __name__ == "__main__":
    main()
