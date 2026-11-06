#!/usr/bin/env python3
"""Build the V1..V9 v5-counter mutants as text in scratch (never the lane).

Reads the counter at the freeze commit from the scratch clone, applies one
single-purpose replacement set per mutant, compiles the result, and writes
<scratch>/counters/<name>.py. A later shell step commits each text in $D so a
gate can name a revision.
"""
import subprocess
import sys
from pathlib import Path

S = Path("/fast/scratch/hyaku/kotoba-r97/MutTesterCounterV5")
D = S / "repo"
REV = "148395bf42af97436b1b832a97a175515f981939"
COUNTER = "verifiers/fixtures/round-97/selftest-kills.py"

MIRROR_JOB = '            if rules == "v5":\n                jobs.append(("mirror", name, mt, mt))\n'
POS_MIRROR_JOB = '        if rules == "v5":\n            jobs.append(("pos-mirror", pname, pt, pt))\n'
KILL = ('            mirror = results[("mirror", name)][0] if rules == "v5" else rf\n'
        '            mirror_rep += rules == "v5" and mirror == rf\n'
        '            k = blind == rf and mirror == rf')
KILL_V1 = ('            mirror = rf\n'
           '            mirror_rep += rules == "v5" and mirror == rf\n'
           '            k = blind == rf')
POS = ('        pmirror = results[("pos-mirror", pname)][0] if rules == "v5" else rf\n'
       '        mirror_rep += rules == "v5" and pmirror == rf\n'
       '        pos = 1 if pblind == rf and pmirror == rf else 0')
POS_V1 = ('        pmirror = rf\n'
          '        mirror_rep += rules == "v5" and pmirror == rf\n'
          '        pos = 1 if pblind == rf else 0')

MUTANTS = {
    "V1-mirror-dropped": [
        (MIRROR_JOB, ""),
        (POS_MIRROR_JOB, ""),
        (KILL, KILL_V1),
        (POS, POS_V1),
    ],
    "V2-bracket-first-only": [
        ('            jobs.insert(rng.randrange(1, len(jobs)), honest)\n'
         '            jobs = [honest] + jobs + [honest]',
         '            jobs = [honest] + jobs'),
    ],
    "V3-isolation-dropped": [
        ('        shared = fresh_world("shared") if rules == "v4" else None',
         '        shared = fresh_world("shared")'),
    ],
    "V4-home-not-reset": [
        ('            if rules == "v5":\n'
         '                env.update(HOME=str(d / "home"), XDG_CACHE_HOME=str(d / "cache"))\n',
         ''),
    ],
    "V5-no-shuffle": [
        ('            rng = random.Random(seed)\n'
         '            rng.shuffle(jobs)\n'
         '            jobs.insert(rng.randrange(1, len(jobs)), honest)',
         '            rng = random.Random(seed)\n'
         '            jobs.insert(len(jobs) // 2, honest)'),
    ],
    "V6-honest-any": [
        ('        cls_h = "CLEAN" if honest_clean == len(honest_runs) else next(c for c in honest_runs if c != "CLEAN")',
         '        cls_h = "CLEAN" if honest_clean >= 1 else "RUN-ERROR"'),
    ],
    "V7-unicode-uncaught": [
        ('        try:\n'
         '            original = shown.stdout.decode("utf-8")\n'
         '        except UnicodeDecodeError as exc:\n'
         '            raise NotEvaluated("instrument %s is not valid UTF-8 at %s (%s)" % (instrument, rev, exc))',
         '        original = shown.stdout.decode("utf-8")'),
    ],
    "V8-mirror-original": [
        ('                jobs.append(("mirror", name, mt, mt))',
         '                jobs.append(("mirror", name, mt, original))'),
        ('            jobs.append(("pos-mirror", pname, pt, pt))',
         '            jobs.append(("pos-mirror", pname, pt, original))'),
    ],
    "V9-decoy-runerror-held": [
        ('        held_comment = sum(1 for nm, _, _, _ in spec["targets"] if results[("comment", nm)][0] == "CLEAN")\n'
         '        held_code = sum(1 for nm, _, _, _ in spec["targets"] if results[("code", nm)][0] == "CLEAN")',
         '        held_comment = sum(1 for nm, _, _, _ in spec["targets"] if results[("comment", nm)][0] != "REPORTED-FAILURE")\n'
         '        held_code = sum(1 for nm, _, _, _ in spec["targets"] if results[("code", nm)][0] != "REPORTED-FAILURE")'),
    ],
}


def main() -> int:
    shown = subprocess.run(["git", "-C", str(D), "show", "%s:%s" % (REV, COUNTER)],
                           stdout=subprocess.PIPE, check=True)
    original = shown.stdout.decode("utf-8")
    out = S / "counters"
    out.mkdir(parents=True, exist_ok=True)
    (out / "baseline.py").write_text(original, encoding="utf-8")
    for name, edits in MUTANTS.items():
        text = original
        for old, new in edits:
            n = text.count(old)
            if n != 1:
                print("FAIL %s: anchor matches %d time(s), expected 1: %r" % (name, n, old[:80]))
                return 1
            text = text.replace(old, new)
        if text == original:
            print("FAIL %s: no change" % name)
            return 1
        compile(text, COUNTER, "exec", dont_inherit=True)
        (out / (name + ".py")).write_text(text, encoding="utf-8")
        print("built %s (%d bytes, %d changed lines)" % (
            name, len(text),
            sum(1 for a, b in zip(original.splitlines(), text.splitlines()) if a != b)
            + abs(len(original.splitlines()) - len(text.splitlines()))))
    return 0


if __name__ == "__main__":
    sys.exit(main())
