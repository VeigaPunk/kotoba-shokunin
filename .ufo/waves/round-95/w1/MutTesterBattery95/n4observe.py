#!/usr/bin/env python3
"""MutTesterBattery95: N4 observability probe (side experiment, not the counter's kill path).

Executes the honest candidate instrument and the N4 mutant (pin check moved after the probe
loop) as modules, builds a pin-passing and a pin-failing rev-path fixture with the honest
module's own fixture helpers, runs each module's run_evaluate on both worlds, and diffs
rc + captured stdout. This measures whether N4's reordering is observable anywhere at all,
beyond the self-test's tally-only stdout.
"""
from __future__ import annotations

import contextlib
import difflib
import importlib.util
import io
import os
import shutil
import sys
import tempfile
from pathlib import Path

SRC = Path("/fast/scratch/hyaku/kotoba-r95/MutTesterBattery95/results/probe/world/kotoba-shokunin/verifiers/check_mutation_battery.py")
WORK = Path("/fast/scratch/hyaku/kotoba-r95/MutTesterBattery95/results/n4observe")


def load(text: str, name: str, tmp: Path):
    p = tmp / (name + ".py")
    p.write_text(text, encoding="utf-8")
    spec = importlib.util.spec_from_file_location(name, p)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


def run(mod, fixture: Path, work: Path, pinned: int):
    # run_evaluate itself captures stdout and returns (rc, out).
    return mod.run_evaluate(fixture, mod.head(fixture), work, pinned)


def main() -> int:
    shutil.rmtree(WORK, ignore_errors=True)
    WORK.mkdir(parents=True)
    tmp = WORK / "mods"
    tmp.mkdir()
    orig = SRC.read_text(encoding="utf-8")

    lines = orig.splitlines(keepends=True)
    i = [j for j, ln in enumerate(lines)
         if ln == "    ok_pin, pin_detail = kill_set_check(committed, pinned)\n"][0]
    block = lines[i:i + 4]
    rest = [ln for j, ln in enumerate(lines) if not (i <= j < i + 4)]
    anchor = '    kills = [r for r in results if r["cls"] == "kill"]\n'
    hits = [j for j, ln in enumerate(rest) if ln == anchor]
    assert len(hits) == 1 and len(block) == 4
    n4 = "".join(rest[:hits[0]] + block + rest[hits[0]:])

    H = load(orig, "bat_honest", tmp)
    M = load(n4, "bat_n4", tmp)

    root = WORK / "fixtures"
    rows = H._satisfying_rows()
    pinned = sum(1 for r in rows if r[2] == "kill")
    okf = H.build_fixture(root, "n4ok", rows, H.SKILL_WITH)
    drop_rows = [r for j, r in enumerate(rows) if not (r[2] == "kill" and j == 0)]
    dropf = H.build_fixture(root, "n4drop", drop_rows, H.SKILL_WITH)
    assert H.kill_set_check(H._manifest_text(rows), pinned)[0]
    assert not H.kill_set_check(H._manifest_text(drop_rows), pinned)[0]

    report = []
    for label, fixture in (("pin-passing (revok shape)", okf), ("pin-failing (revdrop shape)", dropf)):
        rc_h, out_h = run(H, fixture, WORK / ("w-h-" + ("ok" if "passing" in label else "drop")), pinned)
        rc_m, out_m = run(M, fixture, WORK / ("w-m-" + ("ok" if "passing" in label else "drop")), pinned)
        d = [ln for ln in difflib.unified_diff(out_h.splitlines(), out_m.splitlines(),
                                               "honest", "n4", lineterm="", n=1)]
        report.append("world %s: honest rc %d (%d lines), n4 rc %d (%d lines), diff %d lines"
                      % (label, rc_h, len(out_h.splitlines()), rc_m, len(out_m.splitlines()), len(d)))
        if d:
            report.append("  first 14 diff lines:")
            report += ["    " + ln for ln in d[:14]]
    print("\n".join(report))
    (WORK / "n4observe.txt").write_text("\n".join(report) + "\n", encoding="utf-8")
    shutil.rmtree(root, ignore_errors=True)
    for w in WORK.glob("w-*"):
        shutil.rmtree(w, ignore_errors=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())
