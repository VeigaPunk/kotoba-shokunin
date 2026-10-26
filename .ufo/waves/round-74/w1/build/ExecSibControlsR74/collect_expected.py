#!/usr/bin/env python3
"""collect_expected.py -- write expected.json from emulate_reread.py.

`expected.json` is the recorded expected score per world (and the failing rows
with their first reason), consumed by build_worlds.py when it writes each
world's README.  Mode is `emulated` until the round-74 counter exists; when
`verifiers/check_sibling_reread.py` is present, run `score_worlds.sh <counter>`
instead and it is the measurement that counts.
"""
from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
WORLDS = sorted([p.name for p in HERE.glob("world-*")] + [p.name for p in HERE.glob("diag-*")])


def main():
    out = {}
    for world in WORLDS:
        proc = subprocess.run(
            [sys.executable, "-B", str(HERE / "emulate_reread.py"), str(HERE / world), "--json"],
            capture_output=True, text=True)
        if proc.returncode not in (0, 1):
            print("emulator failed for", world, proc.stderr.strip(), file=sys.stderr)
            continue
        data = json.loads(proc.stdout)
        lanes = {lane: (detail["why"] or []) for lane, detail in data["lanes"].items()}
        out[world] = {"score": data["pass"], "of": data["of"], "mode": "emulated",
                      "lanes": lanes}
    (HERE / "expected.json").write_text(json.dumps(out, indent=1, ensure_ascii=False) + "\n",
                                        encoding="utf-8")
    for world in sorted(out):
        print("%-30s %2d of %d" % (world, out[world]["score"], out[world]["of"]))


if __name__ == "__main__":
    main()
