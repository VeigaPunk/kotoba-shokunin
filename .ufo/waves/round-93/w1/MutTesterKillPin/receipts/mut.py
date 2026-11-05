#!/usr/bin/env python3
"""Scratch-only mutant builder for the MutTesterKillPin seat (round 93, C1 candidate).

Usage: python3 -B mut.py <clone> <mutant-id>
Applies exactly one mutant to verifiers/check_mutation_battery.py in <clone> (already at the
candidate). Every anchor must match its expected count, else exits 3 (no partial write).
"""
import pathlib
import sys

D = pathlib.Path(sys.argv[1])
name = sys.argv[2]
p = D / "verifiers/check_mutation_battery.py"
t = p.read_text(encoding="utf-8")


def rep(text, old, new, n=1):
    c = text.count(old)
    if c != n:
        print("anchor count %d != %d for %s: %r" % (c, n, name, old[:70]), file=sys.stderr)
        raise SystemExit(3)
    return text.replace(old, new)


BLOCK = (
    '    ok_pin, pin_detail = kill_set_check(committed, pinned)\n'
    '    if not ok_pin:\n'
    '        raise CouldNotEvaluate("arm kill-set-size: manifest at %s has %s"\n'
    '                               % (rev[:12], pin_detail))\n'
)
TGT = (
    '    if {row.target for row in rows} != set(PROBES):\n'
    '        raise CouldNotEvaluate("manifest must name exactly the targets %s" % sorted(PROBES))\n'
)
assert BLOCK in t and TGT in t, "candidate anchors missing"

if name == "m1":          # the new check deleted
    t = rep(t, BLOCK, "")
elif name == "m2":        # pin comparison weakened to '<' (only drops refused)
    t = rep(t, "    return n == want, \"observed", "    return n < want, \"observed")
elif name == "m3":        # new check reads the WORKING-TREE manifest, not git show <rev>
    t = rep(t, "ok_pin, pin_detail = kill_set_check(committed, pinned)",
            "ok_pin, pin_detail = kill_set_check((lane / MANIFEST).read_text(encoding=\"utf-8\"), pinned)")
elif name == "m4":        # arm name dropped from the refusal message
    t = rep(t, 'CouldNotEvaluate("arm kill-set-size: manifest at %s has %s"',
            'CouldNotEvaluate("manifest at %s has %s"')
elif name == "m5":        # kill check moved BEFORE the target-set check
    t = rep(t, BLOCK, "")
    t = rep(t, TGT, BLOCK + TGT)
elif name == "m6":        # every could-not-evaluate line prefixed kill-set-size (forgery shape)
    t = rep(t, 'print("could-not-evaluate: %s" % exc)',
            'print("could-not-evaluate: kill-set-size: %s" % exc)', n=3)
else:
    print("unknown mutant %s" % name, file=sys.stderr)
    raise SystemExit(3)

p.write_text(t, encoding="utf-8")
print("applied %s: %s bytes" % (name, len(t.encode("utf-8"))))
