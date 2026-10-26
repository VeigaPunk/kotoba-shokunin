#!/usr/bin/env python3
"""run_controls_worlds.py -- read-only replay of the round-73 pointer-gate controls.

Seat ExecPointersGate's evidence tool, built in wave 1. It runs
`check_report_pointers.py` against every report the controls seat
(`ExecPointersControls`) pinned, and compares the measured exit code and tally
with that world's expectation. It writes nothing: the readings belong to the
controls seat, not to the gate seat.

    python3 -B run_controls_worlds.py [--gate PATH]

Exit 0 iff every compared reading matches. Worlds whose `world.json` carries a
`sandbox` recipe are listed as skipped -- they need an untracked file in a clone
and are not reproducible read-only.
"""

import argparse
import json
import pathlib
import re
import subprocess
import sys

LANE = pathlib.Path("/home/vgpnk/Projects/shokunin/kotoba-shokunin")
WORLDS = LANE / ".ufo/waves/round-73/w1/build/ExecPointersControls"
DEFAULT_GATE = LANE / ".ufo/waves/round-73/w1/build/ExecPointersGate/check_report_pointers.py"
TALLY = re.compile(r"resolved (\d+) of (\d+); unresolved (\d+)")


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--gate", default=str(DEFAULT_GATE), metavar="PATH")
    args = parser.parse_args(argv)

    bad = 0
    for world_file in sorted(WORLDS.glob("*/world.json")):
        meta = json.loads(world_file.read_text(encoding="utf-8"))
        if meta.get("sandbox"):
            print("%-22s %-26s SKIP      sandbox recipe (untracked file in a clone)"
                  % (meta["world"], "*"))
            continue
        for report in meta["reports"]:
            path = world_file.parent / report["file"]
            round_no = report.get("round", meta["round"])
            proc = subprocess.run(
                ["python3", "-B", args.gate, "--report", str(path),
                 "--repo", str(LANE), "--rev", meta["rev"], "--round", str(round_no)],
                capture_output=True, text=True)
            match = TALLY.search(proc.stdout)
            tally = "%s of %s" % (match.group(1), match.group(2)) if match else "-"
            missing = [n for n in report.get("expect_names", [])
                       if n not in proc.stdout]
            ok = (proc.returncode == report["expect_exit"]
                  and tally == report["expect_tally"] and not missing)
            if not ok:
                bad += 1
            print("%-22s %-26s %-9s exp %d %-7s got %d %-7s%s"
                  % (meta["world"], report["file"], "OK" if ok else "MISMATCH",
                     report["expect_exit"], report["expect_tally"],
                     proc.returncode, tally,
                     "  missing names: %s" % missing if missing else ""))
    print("controls worlds: %d mismatch(es)" % bad)
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
