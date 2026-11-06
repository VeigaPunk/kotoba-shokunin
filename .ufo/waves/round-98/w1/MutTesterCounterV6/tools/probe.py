#!/usr/bin/env python3
"""Exit-ladder probes for the v6 counter: badutf8 (rule 7) and an unwritable scratch root (rule 10).

Usage: python3 -B probe.py <counter.py> <label> [--rules v5]
"""
import os
import subprocess
import sys
from pathlib import Path

S = Path("/fast/scratch/hyaku/kotoba-r98/MutTesterCounterV6")
SLIM = S / "slim"
SREV = {}
for ln in (S / "logs" / "slim-revs.txt").read_text().splitlines():
    p = ln.split()
    if len(p) >= 2:
        SREV[p[0]] = p[1]


def run(counter: Path, label: str, table: str, rev: str, repo: Path, scratch: str,
        extra: list[str]) -> dict:
    env = {k: v for k, v in os.environ.items() if k != "KOTOBA_R97_SEED"}
    env["HYAKU_SCRATCH"] = scratch
    p = subprocess.run([sys.executable, "-B", str(counter), table, rev, str(repo), *extra],
                       env=env, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, timeout=3600)
    out = p.stdout.decode("utf-8", "replace").splitlines()
    tail = out[-3:] if out else ["<no output>"]
    tb = any("Traceback (most recent call last)" in ln for ln in out)
    print("%s rc %d traceback=%s | %s" % (label, p.returncode, tb, " || ".join(tail)))
    return {"label": label, "rc": p.returncode, "traceback": tb, "tail": tail}


def main(argv: list[str]) -> int:
    counter = Path(argv[0]).resolve()
    label = argv[1]
    extra = []
    if "--rules" in argv:
        extra = ["--rules", argv[argv.index("--rules") + 1]]
    print("counter %s sha256 %s" % (counter, subprocess.run(
        ["sha256sum", str(counter)], stdout=subprocess.PIPE).stdout.decode().split()[0]))
    run(counter, "badutf8 c1", "c1", SREV["badutf8"], SLIM, str(S / "hs" / (label + "_bad")), extra)
    run(counter, "exit-ladder unwritable scratch", "c1", SREV["BASE"], SLIM,
        str(S / "ro" / "sub"), extra)
    if label in SREV:
        run(counter, "sanity c1 base", "c1", SREV[label], SLIM, str(S / "hs" / (label + "_ok")), extra)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
