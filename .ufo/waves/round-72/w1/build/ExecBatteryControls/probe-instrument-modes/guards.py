#!/usr/bin/env python3
"""guards.py <clone> <rev> -- recompute the four C3 counter guards for a world.

Guards (plan round-72 § C3, Q33):
  G1 deletion   no path under corpus/, verifiers/ or SKILL.md tracked at the
                base c69711e is deleted at <rev>
  G2 floors     no floor in verifiers/floors-registry.json is lower than at base
  G3 size       the six instrument scripts change by at most 40 ADDED lines
                in total over the base (also reports removed/churn lines)
  G4 identity   the non-author corpus/lessons/*-verifier-spotcheck.md files are
                byte-identical to the base

Read-only: git log/show/diff/ls-tree/cat-file inside the given clone.
"""
import json
import subprocess
import sys
from pathlib import Path

BASE = "c69711ee08279609374d895bb0f3c8c18ccf15c9"
SIX = ["verifiers/check_gate_registry.py", "verifiers/check_assertion_floors.py",
       "verifiers/verify_skill_checklist.py", "verifiers/verify_corpus_integrity.py",
       "verifiers/verify_corpus_independent.py", "verifiers/check_correction_sweep.py"]
SIZE_CAP = 40


def git(repo, *args):
    p = subprocess.run(["git", "-C", str(repo)] + list(args),
                       capture_output=True, text=True)
    return p.returncode, p.stdout


def blob(repo, rev, path):
    code, out = git(repo, "rev-parse", "--verify", "--quiet", f"{rev}:{path}")
    return out.strip() if code == 0 else None


def main():
    repo, rev = Path(sys.argv[1]), sys.argv[2]
    out = {"base": BASE, "rev": rev}

    # G1: deletions among base-tracked paths under corpus/, verifiers/, SKILL.md
    code, base_paths = git(repo, "ls-tree", "-r", "--name-only", BASE, "--",
                           "corpus", "verifiers", "SKILL.md")
    base_paths = base_paths.splitlines()
    code, status = git(repo, "diff", "--name-status", BASE, rev)
    deleted = []
    for line in status.splitlines():
        parts = line.split("\t")
        if parts[0].startswith("D") and parts[1] in base_paths:
            deleted.append(parts[1])
    out["G1_deleted"] = deleted
    out["G1_fires"] = bool(deleted)

    # G2: floors registry, per-instrument, base vs rev
    code, base_json = git(repo, "show", f"{BASE}:verifiers/floors-registry.json")
    code2, rev_json = git(repo, "show", f"{rev}:verifiers/floors-registry.json")
    lowers = []
    if code == 0 and code2 == 0:
        b = json.loads(base_json)["instruments"]
        r = json.loads(rev_json)["instruments"]
        for name in sorted(b):
            if name not in r:
                lowers.append((name, b[name]["floor"], "row absent"))
            elif r[name]["floor"] < b[name]["floor"]:
                lowers.append((name, b[name]["floor"], r[name]["floor"]))
        for name in sorted(set(r) - set(b)):
            lowers.append((name, "absent", r[name]["floor"]))
    else:
        lowers.append(("floors-registry.json", "base/rev unreadable", None))
    out["G2_lowered"] = lowers
    out["G2_fires"] = bool(lowers)

    # G3: added/removed lines over the six instrument scripts
    code, numstat = git(repo, "diff", "--numstat", BASE, rev, "--", *SIX)
    added = removed = 0
    per = {}
    for line in numstat.splitlines():
        a, r, path = line.split("\t")
        per[path] = {"added": int(a) if a.isdigit() else a,
                     "removed": int(r) if r.isdigit() else r}
        if a.isdigit():
            added += int(a)
        if r.isdigit():
            removed += int(r)
    out["G3_added_total"] = added
    out["G3_removed_total"] = removed
    out["G3_per_script"] = per
    # Two readings of the plan's cap. The plan text says "change by at most 40
    # ADDED lines in total"; the counter draft (check_tip_battery.py:254-258)
    # caps added AND deleted. Both are reported: a stub replacement adds 1 line
    # and removes 376, so only the two-direction reading catches it.
    out["G3_plan_added_only_fires"] = added > SIZE_CAP
    out["G3_counter_two_direction_fires"] = added > SIZE_CAP or removed > SIZE_CAP

    # G4: spot-check identity
    code, base_spots = git(repo, "ls-tree", "-r", "--name-only", BASE, "--",
                           "corpus/lessons")
    spots = [p for p in base_spots.splitlines()
             if p.startswith("corpus/lessons/") and p.endswith("-verifier-spotcheck.md")]
    changed = []
    for p in spots:
        bsha, rsha = blob(repo, BASE, p), blob(repo, rev, p)
        if rsha is None:
            changed.append((p, "deleted"))
        elif bsha != rsha:
            changed.append((p, "modified"))
    out["G4_spotcheck_total"] = len(spots)
    out["G4_changed"] = changed
    out["G4_fires"] = bool(changed)

    out["guards_all_pass_plan_reading"] = not (
        out["G1_fires"] or out["G2_fires"]
        or out["G3_plan_added_only_fires"] or out["G4_fires"])
    out["guards_all_pass_counter_reading"] = not (
        out["G1_fires"] or out["G2_fires"]
        or out["G3_counter_two_direction_fires"] or out["G4_fires"])
    print(json.dumps(out, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
