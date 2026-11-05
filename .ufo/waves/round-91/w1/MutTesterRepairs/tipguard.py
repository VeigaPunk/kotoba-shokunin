#!/usr/bin/env python3
"""Bounded probe: run check_tip_battery.run_guards (the real guard function) against <repo> at <rev>, base <base>.
Prints each guard failure as 'FAILURE <guard> :: <detail>' and exits 1 if any failure, 0 if none, 2 on EnvError."""
import sys
from pathlib import Path

repo, base, rev = Path(sys.argv[1]), sys.argv[2], sys.argv[3]
sys.path.insert(0, str(repo / "verifiers"))
import check_tip_battery as t  # noqa: E402

try:
    failures, _, _ = t.run_guards(repo, base, rev)
except t.EnvError as exc:
    print("could-not-evaluate: %s" % exc)
    sys.exit(2)
for guard, detail in failures:
    print("FAILURE %s :: %s" % (guard, detail))
print("guard-failures %d" % len(failures))
sys.exit(1 if failures else 0)
