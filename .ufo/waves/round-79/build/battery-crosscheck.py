#!/usr/bin/env python3
"""battery-crosscheck.py -- do the standalone gate receipts agree with the
frozen tip battery's own per-gate readings?

Reads a run-battery.sh receipt directory (round-79 layout, the writer in
.ufo/waves/round-79/build/run-battery.sh):

  01-tip-battery-dot.txt   check_tip_battery.py --repo .      (plan form 1)
  02-tip-battery-abs.txt   check_tip_battery.py --repo <abs>  (plan form 2)
  03..08                   the six gates the frozen battery runs, by hand, in
                           the fleet-shaped scratch clone at the same revision

and prints, per gate, the sandbox exit (each form) beside the standalone exit.
The battery's gate list is frozen in verifiers/check_tip_battery.py, so a
disagreement means either the receipt set is stale/incomplete or a gate is not
revision- or environment-stable -- never something this script may explain away.

usage: battery-crosscheck.py <receipts-dir>
exit: 0 every gate agrees and both forms print the same frozen line
      1 any disagreement, an absent receipt, or a missing/duplicated frozen line
      2 usage error or an unreadable receipt
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

GATE_RE = re.compile(r"^gate (\S+) exit (\S+)", re.M)
FROZEN_RE = re.compile(r"guards (\d+) of (\d+); tip battery exit 0: (\d+) of (\d+)")
CMD_RE = re.compile(r"^# rev=(\S+) cmd=(.*?) utc=(\S+)$", re.M)
EXIT_RE = re.compile(r"^exit=(\d+)$", re.M)

FORMS = ("01-tip-battery-dot.txt", "02-tip-battery-abs.txt")
STANDALONE = ("03-gate-registry.txt", "04-assertion-floors.txt",
              "05-skill-checklist.txt", "06-corpus-integrity.txt",
              "07-corpus-independent.txt", "08-correction-sweep.txt")


def read(name: Path) -> str:
    if not name.is_file():
        return ""
    return name.read_text(errors="replace")


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print(__doc__.strip().splitlines()[-1], file=sys.stderr)
        print("usage: battery-crosscheck.py <receipts-dir>", file=sys.stderr)
        return 2
    root = Path(argv[1])
    if not root.is_dir():
        print("crosscheck: not a directory: %s" % root, file=sys.stderr)
        return 2

    bad = 0
    revs: set[str] = set()
    forms: dict[str, dict[str, str]] = {}
    frozen: dict[str, tuple[int, int, int, int] | None] = {}

    for name in FORMS:
        text = read(root / name)
        head = CMD_RE.search(text)
        if head:
            revs.add(head.group(1))
        gates = dict(GATE_RE.findall(text))
        forms[name] = gates
        match = FROZEN_RE.search(text)
        frozen[name] = tuple(int(x) for x in match.groups()) if match else None
        status = EXIT_RE.findall(text)
        line = match.group(0) if match else "<no frozen line>"
        print("%s: %s" % (name, line))
        print("  receipt exit=%s, %d gate line(s), cmd=%s"
              % (status[-1] if status else "?", len(gates),
                 head.group(2) if head else "?"))

    standalone: dict[str, int | None] = {}
    for name in STANDALONE:
        text = read(root / name)
        head = CMD_RE.search(text)
        if not head:
            print("crosscheck: FAIL %s carries no header line" % name, file=sys.stderr)
            standalone[name] = None
            bad = 1
            continue
        if head.group(1) not in revs:
            print("crosscheck: FAIL %s measures %s, not the form receipts' rev"
                  % (name, head.group(1)), file=sys.stderr)
            bad = 1
        parts = head.group(2).split()
        script = next((p for p in parts if p.startswith("verifiers/")), None)
        exits = EXIT_RE.findall(text)
        if script is None or not exits:
            print("crosscheck: FAIL %s names no script or no exit line" % name, file=sys.stderr)
            bad = 1
            continue
        standalone[script] = int(exits[-1])

    print()
    print("%-40s %-14s %-14s %s" % ("gate", "form 1", "form 2", "standalone"))
    disagreed = 0
    for script in sorted(set(standalone) | {g for f in forms.values() for g in f}):
        row = []
        for name in FORMS:
            row.append(forms[name].get(script, "-"))
        mine = standalone.get(script)
        row.append("-" if mine is None else str(mine))
        agree = len({r for r in row if r != "-"}) == 1 and "-" not in row
        if not agree:
            disagreed += 1
            bad = 1
        print("%-40s %-14s %-14s %-14s %s"
              % (script, row[0], row[1], row[2], "agree" if agree else "DISAGREE"))

    same = (frozen[FORMS[0]] is not None
            and frozen[FORMS[0]] == frozen[FORMS[1]])
    if not same:
        bad = 1
    if len(revs) > 1:
        bad = 1
    print()
    print("crosscheck: %d gate(s) disagree; forms print the same frozen line: %s; "
          "revs seen %s" % (disagreed, "yes" if same else "no",
                            ",".join(sorted(revs)) or "none"))
    total = len({g for f in forms.values() for g in f})
    print("crosscheck: %d of %d gate(s) compared across both forms and the "
          "standalone receipts" % (total - disagreed, total))
    return 0 if bad == 0 else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv))
