#!/usr/bin/env python3
"""M127 gate-level probe: run verify_skill_checklist.py inside the counter's own
sandbox for the two --repo forms, and print each gate's first failing line.

usage: python3 -B probe_checklist_gate.py <rev>
"""
from __future__ import annotations

import subprocess
import sys
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import base_counter as bc  # noqa: E402


def run_form(label: str, repo_arg: str, rev: str, fleet_arg: str | None = None) -> None:
    repo = Path(repo_arg)
    fleet = Path(fleet_arg) if fleet_arg else repo.parent
    with tempfile.TemporaryDirectory(prefix="k73gate-") as tdir:
        parent = Path(tdir)
        try:
            clone = bc.build_sandbox(repo, rev, fleet, parent)
        except Exception as exc:
            print("%s: build_sandbox raised %s: %s" % (label, type(exc).__name__, exc))
            return
        proc = subprocess.run([sys.executable, "-B", "verifiers/verify_skill_checklist.py"],
                              cwd=str(clone), capture_output=True, text=True)
        print("%s: --repo %r -> fleet=%r; verify_skill_checklist.py exit %d"
              % (label, repo_arg, str(fleet), proc.returncode))
        for line in (proc.stdout + proc.stderr).splitlines():
            if line.strip().startswith("FAIL"):
                print("   first failing line: %s" % line.strip())
                break
        st = subprocess.run([sys.executable, "-B", "verifiers/verify_skill_checklist.py",
                             "--self-test"], cwd=str(clone), capture_output=True, text=True)
        summary = [l.strip() for l in st.stdout.splitlines() if l.strip().startswith("self-test:")]
        print("   verify_skill_checklist.py --self-test exit %d: %s"
              % (st.returncode, summary[-1] if summary else "(no summary)"))


def main(argv: list[str]) -> int:
    rev = argv[1]
    lane = str(Path(".").resolve())
    run_form("form A", ".", rev)
    run_form("form B", lane, rev)
    run_form("form C (absolute lane as its own fleet root)", lane, rev, fleet_arg=lane)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
