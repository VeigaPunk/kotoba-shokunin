#!/usr/bin/env python3
"""k73w1 MutTipBatteryGuards mutation driver.

Takes the pristine counter bytes from the fleet-shaped sandbox clone of
072048f, applies exactly one single-point mutation per copy, runs
`python3 -B <mutant> --self-test` (60 s cap each), and records
KILLED / SURVIVED per mutant. Never touches the lane tree.
"""
from __future__ import annotations

import hashlib
import json
import subprocess
import sys
import time
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

PRISTINE = Path(sys.argv[1])
OUT = Path(sys.argv[2])
MUTDIR = OUT / "mutants"
MUTDIR.mkdir(parents=True, exist_ok=True)

# (id, guard point, old bytes (must occur exactly once), new bytes)
MUTANTS = [
    ("M01", "no-deletions: success branch inverted",
     "    if deleted:\n", "    if not deleted:\n"),
    ("M02", "no-deletions: corpus//verifiers/ prefixes dropped from guarded set",
     "               if p.startswith(GUARDED_PREFIXES) or p == GUARDED_FILE]",
     "               if p == GUARDED_FILE]"),
    ("M03", "instrument-size: LINE_CAP 40 -> 400",
     "LINE_CAP = 40", "LINE_CAP = 400"),
    ("M04", "battery: first frozen gate dropped from BATTERY",
     "    (\"verifiers/check_gate_registry.py\", (\"--rev\", REV_TOKEN)),\n", ""),
    ("M05", "tally: gate timeout / None exit counted as pass",
     "        if rc == 0:\n            n += 1",
     "        if rc == 0 or rc is None:\n            n += 1"),
    ("M06", "tally: absent battery script recorded as exit 0",
     "            rows.append((script, None, 0.0, \"absent at %s\" % rev))",
     "            rows.append((script, 0, 0.0, \"absent at %s\" % rev))"),
    ("M07", "instrument-pin: exact blob match weakened to prefix match",
     "        if blob not in allowed:",
     "        if not any(blob.startswith(a) for a in allowed):"),
    ("M08", "spotcheck-identity: byte-identity compare dropped",
     "        elif rev_spot[path] != sha:", "        elif False:"),
    ("M09", "spotcheck-identity: spotcheck regex disabled",
     "SPOTCHECK_RE = re.compile(r\"-verifier-spotcheck\\.md$\")",
     "SPOTCHECK_RE = re.compile(r\"-NEVER-MATCH\")"),
    ("M10", "instrument-size: git diff failure swallowed",
     "    if proc.returncode != 0:\n        raise EnvError(\"cannot diff the instruments",
     "    if False and proc.returncode != 0:\n        raise EnvError(\"cannot diff the instruments"),
    ("M11", "floors: comparison '<' -> '<='",
     "            elif new < old:", "            elif new <= old:"),
    ("M12", "floors: dropped-row check disabled",
     "            if name not in rev_rows:", "            if False:"),
    ("M13", "floors: floors file absent at rev treated as empty rows",
     "    if rev_rows is None:\n        failures.append((\"floors\", \"%s absent at %s\" % (FLOORS_PATH, rev)))",
     "    if rev_rows is None:\n        rev_rows = {}"),
    ("M14", "instrument-pin: pin loop disabled",
     "    for path, allowed in INSTRUMENT_PINS.items():",
     "    for path, allowed in ():"),
    ("M15", "spotcheck-identity: absent base spotcheck treated as pass",
     "            failures.append((\"spotcheck-identity\", \"%s absent at %s\" % (path, rev)))",
     "            pass  # mutant: absent spotcheck treated as pass"),
    ("M16", "exit rule: guard failures no longer block exit 0",
     "    return 0 if n == TOTAL and not failures else 1",
     "    return 0 if n == TOTAL else 1"),
    ("M17", "TOTAL 6 -> 5",
     "TOTAL = 6", "TOTAL = 5"),
    ("M18", "GATE_TIMEOUT_S 280 -> 0",
     "GATE_TIMEOUT_S = 280", "GATE_TIMEOUT_S = 0"),
    ("M19", "no-deletions: GUARDED_FILE 'SKILL.md' -> 'Skill.md'",
     "GUARDED_FILE = \"SKILL.md\"", "GUARDED_FILE = \"Skill.md\""),
    ("M20", "instrument-size: binary numstat row skipped instead of failing",
     "        if a == \"-\" or d == \"-\":",
     "        if False:  # mutant: binary numstat skipped"),
    ("M21", "spotcheck-identity: added spotcheck reported as failure instead of INFO",
     "        info.append(\"spotcheck added at %s (not a base file): %s\" % (rev, path))",
     "        failures.append((\"spotcheck-identity\", \"added at %s: %s\" % (rev, path)))"),
    ("M22", "instrument-size: absent instrument no longer a size failure",
     "    for path in absent:\n        failures.append((\"instrument-size\", \"instrument %s absent at %s\" % (path, rev)))",
     "    for path in absent:\n        pass  # mutant: absent instrument not a size failure"),
    ("M23", "main: default fleet root repo.parent -> repo.parent.parent (M127 class)",
     "    fleet = Path(args.fleet) if args.fleet else repo.parent",
     "    fleet = Path(args.fleet) if args.fleet else repo.parent.parent"),
]


def main() -> int:
    src = PRISTINE.read_bytes()
    pristine_sha = hashlib.sha256(src).hexdigest()
    rows = []

    def build_and_run(mid: str, point: str, old: str, new: str) -> dict:
        count = src.count(old.encode())
        if count != 1:
            return {"id": mid, "point": point, "error": "old snippet count=%d" % count}
        mbytes = src.replace(old.encode(), new.encode(), 1)
        mpath = MUTDIR / ("%s.py" % mid)
        mpath.write_bytes(mbytes)
        started = time.monotonic()
        try:
            proc = subprocess.run(
                [sys.executable, "-B", str(mpath), "--self-test"],
                capture_output=True, text=True, timeout=60)
            rc, out = proc.returncode, proc.stdout
            why = ""
        except subprocess.TimeoutExpired:
            rc, out, why = None, "", "detector timeout >60s"
        wall = time.monotonic() - started
        lines = [l for l in out.splitlines() if l.strip()]
        last = lines[-1] if lines else ""
        survived = (rc == 0) and ("self-test: 0 failure(s)" in out)
        return {
            "id": mid, "point": point,
            "old": old, "new": new,
            "mutant_file": str(mpath),
            "mutant_sha256": hashlib.sha256(mbytes).hexdigest(),
            "exit": rc, "wall_s": round(wall, 2), "detector_last_line": last,
            "verdict": "SURVIVED" if survived else "KILLED",
            "note": why,
        }

    with ThreadPoolExecutor(max_workers=3) as pool:
        rows = list(pool.map(lambda m: build_and_run(*m), MUTANTS))

    recheck = hashlib.sha256(PRISTINE.read_bytes()).hexdigest()
    manifest = {
        "pristine_path": str(PRISTINE),
        "pristine_sha256_before": pristine_sha,
        "pristine_sha256_after": recheck,
        "pristine_unchanged": pristine_sha == recheck,
        "detector": "python3 -B <mutant> --self-test (60 s cap each)",
        "survived_rule": "exit 0 and 'self-test: 0 failure(s)' present",
        "mutants": rows,
    }
    (OUT / "mutation-manifest.json").write_text(json.dumps(manifest, indent=1) + "\n")
    for r in rows:
        print("%-4s %-9s wall %5.2fs exit %-4s | %s | %s"
              % (r["id"], r.get("verdict", "ERROR"), r.get("wall_s", -1),
                 r.get("exit"), r.get("detector_last_line", r.get("error", ""))[:88],
                 r["point"][:72]))
    print("pristine unchanged: %s (%s)" % (manifest["pristine_unchanged"], pristine_sha[:16]))
    return 0


if __name__ == "__main__":
    sys.exit(main())
