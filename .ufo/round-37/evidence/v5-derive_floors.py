#!/usr/bin/env python3
'''derive_floors.py -- independent live re-derivation of the floors table.

Seat V5 (round 37). Does NOT import check_assertion_floors.py: it re-parses the
INSTRUMENTS rows with its own regex, reruns every self-test itself, and compares
the observed assertion count against the declared floor.

Exact-match rule (lane convention, per r31-r36 bumps): declared floor == observed
count at landing. Modes reported per row:
  EXACT       observed == floor, 0 failures, exit 0        (convention held)
  SLACK       observed > floor   (floor lags reality -- bump owed)
  OVERCLAIM   observed < floor   (guard would FAIL -- defect)
  BROKEN      self-test exit != 0 or unparseable summary

Usage: python3 .ufo/round-37/drafts/v5/derive_floors.py [--repo PATH]
Exit 0 iff every row is EXACT.
'''
import argparse
import hashlib
import re
import subprocess
import sys
from pathlib import Path

ROW_RE = re.compile(r'^\s*"([A-Za-z_]+)":\s*\(\s*"([^"]+)",\s*(\d+)\s*,', re.M)
SUMMARIES = (
    re.compile(r"(\d+)\s+failure\(s\)\s+over\s+(\d+)\s+assertions"),   # (failures, assertions)
    re.compile(r"(\d+)\s+assertions,\s+(\d+)\s+failures"),             # (assertions, failures)
)


def parse_rows(guard_src):
    rows = []
    for m in ROW_RE.finditer(guard_src):
        name, path, floor = m.group(1), m.group(2), int(m.group(3))
        rows.append((name, path, floor))
    return rows


def parse_summary(stdout):
    for rx, order in ((SUMMARIES[0], "fa"), (SUMMARIES[1], "af")):
        match = None
        for match in rx.finditer(stdout):
            pass
        if match:
            a, b = int(match.group(1)), int(match.group(2))
            return (a, b) if order == "af" else (b, a)  # -> (assertions, failures)
    return None


def sha256(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo", type=Path, default=Path(__file__).resolve().parents[4])
    ap.add_argument("--timeout", type=float, default=600)
    args = ap.parse_args()
    repo = args.repo.resolve()
    guard = repo / "verifiers/check_assertion_floors.py"
    src = guard.read_text()
    rows = parse_rows(src)
    print("# floors-table live re-derivation -- repo %s" % repo)
    print("# guard sha256 %s" % sha256(guard))
    print("# rows re-parsed from source: %d" % len(rows))
    print()
    print("| instrument | declared floor | observed | delta | failures | exit | script sha256 (12) | mode |")
    print("|---|---|---|---|---|---|---|---|")
    modes = {}
    for name, rel, floor in rows:
        script = repo / rel
        try:
            proc = subprocess.run([sys.executable, str(script), "--self-test"],
                                  cwd=repo, capture_output=True, text=True,
                                  timeout=args.timeout)
            out, rc = proc.stdout + proc.stderr, proc.returncode
        except subprocess.TimeoutExpired:
            out, rc = "", "TIMEOUT"
        parsed = parse_summary(out)
        if parsed is None:
            obs, fails, mode = None, None, "BROKEN"
        else:
            obs, fails = parsed
            if rc != 0 or fails != 0:
                mode = "BROKEN"
            elif obs < floor:
                mode = "OVERCLAIM"
            elif obs > floor:
                mode = "SLACK"
            else:
                mode = "EXACT"
        modes[name] = mode
        print("| %s | %d | %s | %s | %s | %s | %s | %s |" % (
            name, floor,
            obs if obs is not None else "-",
            (obs - floor) if obs is not None else "-",
            fails if fails is not None else "-",
            rc,
            sha256(script)[:12] if script.exists() else "MISSING",
            mode))
    print()
    from collections import Counter
    c = Counter(modes.values())
    print("# modes: %s" % dict(c))
    print("# EXACT %d/%d" % (c.get("EXACT", 0), len(rows)))
    return 0 if c.get("EXACT", 0) == len(rows) else 1


if __name__ == "__main__":
    sys.exit(main())