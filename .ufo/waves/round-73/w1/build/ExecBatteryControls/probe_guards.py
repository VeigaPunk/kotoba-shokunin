#!/usr/bin/env python3
"""Probe the frozen C3 counter's guard function on the six control worlds.

Read-only: builds a fresh fleet-shaped sandbox per probe in a tempdir and calls
the lane counter's own run_guards(). Questions:

  A  w1 under the live BASE (c69711e): does any guard see the deleted r72
     spot-check?
  B  w1 under BASE repinned to the round-73 base (072048f) and under a repaired
     size cap: does spotcheck-identity / no-deletions fire then?
  C  the honest base 072048f under the live base and under base == rev.
  D  w5 and w6 with the counter's own blob added to INSTRUMENT_PINS: does a
     weakened in-tree check_tip_battery.py get caught by a self-pin?
  E  w1 with only the size cap repaired (LINE_CAP 40 -> 200): do ALL guards
     pass on a world that deleted a spot-check?  (the counter is then wrong)
"""
import importlib.util
import subprocess
import sys
import tempfile
from pathlib import Path

COUNTER = "/home/vgpnk/Projects/shokunin/kotoba-shokunin/verifiers/check_tip_battery.py"


def load():
    spec = importlib.util.spec_from_file_location("ctb", COUNTER)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def probe(ctb, repo, fleet, rev, base, pins, line_cap):
    with tempfile.TemporaryDirectory(prefix="k73w1-probe-") as td:
        clone = ctb.build_sandbox(Path(repo), rev, Path(fleet), Path(td))
        ctb.INSTRUMENT_PINS = pins
        ctb.LINE_CAP = line_cap
        failures, summary, info = ctb.run_guards(clone, base, rev)
    return failures, summary


def main():
    repo, fleet = Path(sys.argv[1]), Path(sys.argv[2])
    live = load()
    live_pins = dict(live.INSTRUMENT_PINS)

    def rev(name):
        return subprocess.run(["git", "-C", str(repo), "rev-parse", name],
                              capture_output=True, text=True).stdout.strip()

    base73 = rev("072048fa8e8a52c707d25f7079772fa317244eb7")
    counter_blob = subprocess.run(
        ["git", "-C", str(repo), "rev-parse",
         "%s:verifiers/check_tip_battery.py" % base73],
        capture_output=True, text=True).stdout.strip()
    self_pin = dict(live_pins)
    self_pin["verifiers/check_tip_battery.py"] = (counter_blob,)

    cases = [
        ("A  w1 live base c69711e, cap 40", rev("w1"), live.BASE, live_pins, 40),
        ("B  w1 base 072048f, cap 40", rev("w1"), base73, live_pins, 40),
        ("B2 w1 base 072048f, cap 200", rev("w1"), base73, live_pins, 200),
        ("E  w1 live base, cap 200", rev("w1"), live.BASE, live_pins, 200),
        ("C  base 072048f live base, cap 40", base73, live.BASE, live_pins, 40),
        ("C2 base 072048f base==rev, cap 40", base73, base73, live_pins, 40),
        ("D  w5 live base, self-pin, cap 200", rev("w5"), live.BASE, self_pin, 200),
        ("D  w6 live base, self-pin, cap 200", rev("w6"), live.BASE, self_pin, 200),
        ("D0 base 072048f self-pin, cap 200", base73, live.BASE, self_pin, 200),
    ]
    for label, r, b, pins, cap in cases:
        failures, summary = probe(live, repo, fleet, r, b, pins, cap)
        verdict = "ALL GUARDS PASS" if not failures else ""
        print("%s -> %s" % (label, verdict))
        print("   summary: %s" % summary)
        for gid, detail in failures:
            print("   FAIL %s: %s" % (gid, detail))
    return 0


if __name__ == "__main__":
    sys.exit(main())
