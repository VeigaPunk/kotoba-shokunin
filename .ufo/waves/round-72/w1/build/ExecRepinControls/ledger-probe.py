#!/usr/bin/env python3
"""ledger-probe.py -- the round-72 C2 ledger conjunct, measured standalone.

NOT the counter. `verifiers/check_substrate_repin_v2.py` (ExecRepinCounter) owns
the frozen predicate; this probe exists so a shortcut world's ledger can be
scored against the plan's own rule without waiting on that counter, and so the
control receipts name the set the counter must recompute:

  required = every opencode class declared at the base rev whose `literal`
             counts 0 in a `strings -n 4` dump of the substrate
  ledgered = every `removals[].class_id` in the tree's
             verifiers/census-removals.json
  holds    = ledgered == required   (a present literal cannot be ledgered,
                                     an absent one cannot stay declared governed)

Counting is plain substring counting over the dump bytes (the plan's "count 0
by its own strings -n 4 pass"). Usage:

  python3 -B ledger-probe.py --dump /tmp/k72-oc-strings.txt \
      [--ledger <tree>/verifiers/census-removals.json] \
      [--rev c69711ee08279609374d895bb0f3c8c18ccf15c9] [--lane <lane root>]

Exit 0 when the conjunct holds, 1 when it does not, 2 when it cannot evaluate.
"""
from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path

BASE_REV = "c69711ee08279609374d895bb0f3c8c18ccf15c9"
LANE = Path("/home/vgpnk/Projects/shokunin/kotoba-shokunin")


def base_classes(lane: Path, rev: str) -> list[dict]:
    raw = subprocess.run(
        ["git", "-C", str(lane), "show", "%s:verifiers/surfaces-baseline.json" % rev],
        check=True, capture_output=True).stdout
    data = json.loads(raw)
    return [c for c in data["classes"] if c["harness"] == "opencode"]


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--dump", required=True, help="`strings -n 4` dump to count in")
    ap.add_argument("--ledger", help="verifiers/census-removals.json of the world")
    ap.add_argument("--rev", default=BASE_REV)
    ap.add_argument("--lane", default=str(LANE))
    args = ap.parse_args(argv)

    try:
        dump = Path(args.dump).read_text(encoding="utf-8", errors="replace")
        classes = base_classes(Path(args.lane), args.rev)
    except (OSError, ValueError, subprocess.CalledProcessError) as exc:
        print("CANNOT EVALUATE: %s" % exc, file=sys.stderr)
        return 2

    counts = {c["class_id"]: dump.count(c["literal"]) for c in classes}
    required = {cid for cid, n in counts.items() if n == 0}
    ledgered: set[str] = set()
    if args.ledger:
        try:
            rows = json.loads(Path(args.ledger).read_text(encoding="utf-8"))
        except (OSError, ValueError) as exc:
            print("CANNOT EVALUATE: ledger %s: %s" % (args.ledger, exc), file=sys.stderr)
            return 2
        for row in rows.get("removals", []):
            cid = row.get("class_id")
            if not isinstance(cid, str) or not cid:
                print("CANNOT EVALUATE: ledger row without a string class_id",
                      file=sys.stderr)
                return 2
            ledgered.add(cid)

    print("base opencode classes %d; ledgered %d; required %d"
          % (len(classes), len(ledgered), len(required)))
    for cid in sorted(counts):
        mark = "absent" if counts[cid] == 0 else "present"
        print("  %-40s literal %-18s count %-5d %s"
              % (cid, classes_by_id(classes)[cid], counts[cid], mark))
    extra = sorted(ledgered - required)
    missing = sorted(required - ledgered)
    if extra:
        print("FAIL ledgered but literal present: %s" % ", ".join(extra))
    if missing:
        print("FAIL required but not ledgered: %s" % ", ".join(missing))
    holds = not extra and not missing
    print("ledger conjunct %s" % ("HOLDS" if holds else "FAILS"))
    return 0 if holds else 1


def classes_by_id(classes: list[dict]) -> dict[str, str]:
    return {c["class_id"]: c["literal"] for c in classes}


if __name__ == "__main__":
    sys.exit(main())
