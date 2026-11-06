#!/usr/bin/env python3
"""Local differential sweep: apply each frozen c1 mutant to the candidate
instrument in a throwaway copy and record which self-test arms fire.  This is
a debugging aid; the frozen v5 counter is the authority."""
import importlib.util
import subprocess
import sys
import tempfile
from pathlib import Path

LANE = Path("/home/vgpnk/Projects/shokunin/kotoba-shokunin")
counter = LANE / "verifiers/fixtures/round-97/selftest-kills.py"
spec = importlib.util.spec_from_file_location("selftest_kills", counter)
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)

cand = Path(sys.argv[1])
original = cand.read_text(encoding="utf-8")
rows = list(mod.CLAIMS["c1"]["targets"]) + [mod.CLAIMS["c1"]["positive"]]
bad = 0
for name, anchor, count, repl in rows:
    got = original.count(anchor)
    if got != count:
        print("%-34s ANCHOR MISS %d" % (name, got))
        bad += 1
        continue
    text = original.replace(anchor, repl)
    with tempfile.TemporaryDirectory(prefix="sweep-") as tmp:
        # the instrument resolves SKILL.md as <parent>/<parent>/SKILL.md, so the
        # copy keeps the repo layout and the box-proof arms stay honest
        (Path(tmp) / "verifiers").mkdir()
        (Path(tmp) / "SKILL.md").write_text(
            (LANE / "SKILL.md").read_text(encoding="utf-8"), encoding="utf-8")
        path = Path(tmp) / "verifiers" / "instrument.py"
        path.write_text(text, encoding="utf-8")
        proc = subprocess.run([sys.executable, "-B", str(path), "--self-test"],
                              stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                              cwd=tmp)
    out = proc.stdout.decode("utf-8", "replace")
    fails = [ln for ln in out.splitlines()
             if ln.startswith("self-test FAIL: ")]
    summary = [ln for ln in out.splitlines()
               if "failure(s) over" in ln]
    armed = sorted({ln.split("self-test FAIL: ")[1].split(":")[0]
                    for ln in fails})
    print("%-34s rc %d  %s  arms %s"
          % (name, proc.returncode, summary[-1] if summary else "<none>",
             ",".join(armed) or "-"))
    if proc.returncode != 1 or not fails:
        bad += 1
print("mutants without a reported failure: %d" % bad)
sys.exit(1 if bad else 0)
