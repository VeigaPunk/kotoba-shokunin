#!/usr/bin/env python3
"""One measurement of one world by one counter, the C2 runner's measure step.

Usage: python3 -B newctl.py <world> <counter.py> <label> [--repeat N] [--seed S]
"""
import os
import subprocess
import sys
from pathlib import Path

S = Path("/fast/scratch/hyaku/kotoba-r98/MutTesterCounterV6")
WORLDS = S / "worlds"
WREV = {}
for ln in (S / "logs" / "world-revs.txt").read_text().splitlines():
    p = ln.split()
    if len(p) >= 2:
        WREV[p[0]] = p[1]


def main(argv: list[str]) -> int:
    world, counter, label = argv[0], Path(argv[1]).resolve(), argv[2]
    repeat = int(argv[argv.index("--repeat") + 1]) if "--repeat" in argv else 1
    seed = argv[argv.index("--seed") + 1] if "--seed" in argv else None
    raw = S / "logs" / "raw"
    raw.mkdir(parents=True, exist_ok=True)
    for i in range(repeat):
        env = {k: v for k, v in os.environ.items() if k != "KOTOBA_R97_SEED"}
        env["HYAKU_SCRATCH"] = str(S / "hs" / ("%s_%s_%d" % (label, world, i)))
        if seed:
            env["KOTOBA_R97_SEED"] = seed
        p = subprocess.run([sys.executable, "-B", str(counter), "r96c1", WREV[world], str(WORLDS)],
                           env=env, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, timeout=3600)
        out = p.stdout.decode("utf-8", "replace").splitlines()
        (raw / ("%s__%s__%d.txt" % (label, world, i))).write_text("\n".join(out) + "\n")
        tally = next((ln for ln in reversed(out) if " targets killed " in ln), "<no tally>")
        pred = next((ln for ln in reversed(out) if "-PREDICATE-" in ln or "-NOT-EVALUATED" in ln), "<no predicate>")
        rules = next((ln for ln in reversed(out) if ln.startswith("rules ")), "")
        print("%-28s %-22s rc %d %s | %s%s" % (world, label, p.returncode, pred, tally,
                                               ("  [" + rules + "]") if rules else ""))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
