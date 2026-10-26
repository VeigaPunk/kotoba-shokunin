#!/usr/bin/env python3
"""M127 instrumented runner: unmodified base counter, gate output saved.

Imports base_counter.py (a byte copy of `git show 072048f:verifiers/check_tip_battery.py`)
and monkeypatches only two functions: build_sandbox (prints the derived repo/fleet)
and run_battery (keeps the same command, cwd, timeout and rows, and additionally
writes each gate's stdout/stderr under $K73_GATE_OUT).  Gate semantics are the
base module's own BATTERY/REV_TOKEN/GATE_TIMEOUT_S values.

usage: K73_GATE_OUT=<dir> python3 -B instrumented_counter.py --rev <rev> --repo .
"""
from __future__ import annotations

import os
import subprocess
import sys
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import base_counter as bc  # noqa: E402


def build_sandbox(repo: Path, rev: str, fleet: Path, parent: Path) -> Path:
    print("instrument: repo=%r fleet=%r fleet==repo=%s"
          % (str(repo), str(fleet), fleet == repo), file=sys.stderr)
    return _orig_build(repo, rev, fleet, parent)


def run_battery(clone: Path, rev: str):
    outdir = os.environ.get("K73_GATE_OUT")
    rows = []
    for script, extra in bc.BATTERY:
        argv = [sys.executable, "-B", script]
        argv += [rev if a == bc.REV_TOKEN else a for a in extra]
        path = clone / script
        if not path.is_file():
            rows.append((script, None, 0.0, "absent at %s" % rev))
            continue
        started = time.monotonic()
        proc = None
        try:
            proc = subprocess.run(argv, cwd=str(clone), capture_output=True,
                                  text=True, timeout=bc.GATE_TIMEOUT_S)
            rc, why = proc.returncode, ""
        except subprocess.TimeoutExpired:
            rc, why = None, "timeout after %d s" % bc.GATE_TIMEOUT_S
        except OSError as exc:
            rc, why = None, "not runnable: %s" % exc
        rows.append((script, rc, time.monotonic() - started, why))
        if outdir:
            stem = Path(script).stem
            Path(outdir).mkdir(parents=True, exist_ok=True)
            Path(outdir, stem + ".out").write_text(proc.stdout if proc else "")
            Path(outdir, stem + ".err").write_text(proc.stderr if proc else "")
    return rows


_orig_build = bc.build_sandbox
bc.build_sandbox = build_sandbox
bc.run_battery = run_battery

if __name__ == "__main__":
    sys.exit(bc.main(sys.argv[1:]))
