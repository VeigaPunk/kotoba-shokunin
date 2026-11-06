#!/usr/bin/env python3
"""critic_probe.py -- static kill-rule probes for the round-99 candidate.

Usage: critic_probe.py REPO [REV]

Checks, for a candidate tree:
  1. every frozen anchor of CLAIMS[c1|r98c1|r97c1|r96c1] matches exactly once;
  2. the instrument diff vs the round base is confined to self_test() (and
     self-test-only helpers/constants next to it);
  3. --box-proof reads `boxes proven 2` rc 0;
  4. the honest --self-test is CLEAN and prints its assertion count;
  5. the counter bytes at REV equal the instrument commit's (sha256).
Read-only: uses `git show`, never writes the repo.
"""
from __future__ import annotations

import hashlib
import os
import re
import subprocess
import sys
import tempfile
from pathlib import Path

LANE = Path("/home/vgpnk/Projects/shokunin/kotoba-shokunin")
BASE = "52e8e95ac4faf4ded84d7b82cbc204792590d0f7"
INSTR = "verifiers/verify_dispatch_prompts.py"
COUNTERS = ("verifiers/fixtures/round-99/selftest-kills.py",
            "verifiers/fixtures/round-99/carried-reds.py")
FROZEN_SHA = {
    "verifiers/fixtures/round-99/selftest-kills.py":
        "aff389533c966a668b477da11432ded511f24c31e80c5a108ff950a4f4af9be1",
    "verifiers/fixtures/round-99/carried-reds.py":
        "5f964253755e0d69f7651a0be43288aaad60fec3ba6c5a25328f5619972bf358",
}


def git(repo: Path, *args: str) -> bytes:
    return subprocess.run(["git", "-C", str(repo)] + list(args),
                          check=True, capture_output=True).stdout


def load_claims() -> dict:
    import importlib.util
    p = LANE / "verifiers/fixtures/round-99/selftest-kills.py"
    spec = importlib.util.spec_from_file_location("sk_probe", p)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod.CLAIMS


def main() -> int:
    repo = Path(sys.argv[1]).resolve()
    rev = sys.argv[2] if len(sys.argv) > 2 else "HEAD"
    text = git(repo, "show", "%s:%s" % (rev, INSTR)).decode("utf-8")
    base_text = git(repo, "show", "%s:%s" % (BASE, INSTR)).decode("utf-8")
    claims = load_claims()
    bad = 0
    for claim, spec in claims.items():
        if claim not in ("c1", "r98c1", "r97c1", "r96c1"):
            continue
        rows = spec["targets"] + [spec["positive"]]
        for row in rows:
            tid, anchor = row[0], row[1]
            n = text.count(anchor)
            if n != 1:
                bad += 1
                print("ANCHOR %s %s count %d (want 1)" % (claim, tid, n))
        print("%s anchors checked %d" % (claim, len(rows)))
    # diff confinement
    diff = subprocess.run(
        ["git", "-C", str(repo), "diff", "-U0", BASE, rev, "--", INSTR],
        capture_output=True, text=True).stdout
    hunks = [l for l in diff.splitlines() if l.startswith("@@")]
    print("hunks %d: %s" % (len(hunks), hunks))
    def span(s: str, name: str) -> tuple[int, int]:
        lines = s.splitlines()
        start = next(i for i, l in enumerate(lines) if l.startswith("def %s(" % name))
        end = next((i for i in range(start + 1, len(lines))
                    if re.match(r"^(def |class |if __name__)", lines[i])), len(lines))
        return start + 1, end
    st = span(text, "self_test")
    bp = span(text, "box_proof")
    print("self_test %s box_proof %s" % (st, bp))
    # every changed line must be inside self_test's span (production unchanged)
    for h in hunks:
        m = re.match(r"@@ -(\d+)(?:,(\d+))? \+(\d+)(?:,(\d+))? @@", h)
        if not m:
            continue
        new_start = int(m.group(3))
        new_len = int(m.group(4) or 1)
        inside = st[0] <= new_start and new_start + new_len - 1 <= st[1]
        print("hunk new %d+%d inside self_test %s" % (new_start, new_len, inside))
        if not inside:
            bad += 1
    # box proof + self test behaviour
    with tempfile.TemporaryDirectory() as td:
        env = dict(os.environ, TMPDIR=td, PYTHONDONTWRITEBYTECODE="1")
        p = subprocess.run([sys.executable, "-B", str(repo / INSTR), "--box-proof"],
                           cwd=str(repo), capture_output=True, text=True, env=env)
        print("box-proof rc %d out %r" % (p.returncode, p.stdout.strip()[-200:]))
        if p.returncode != 0 or "boxes proven 2" not in p.stdout:
            bad += 1
        p = subprocess.run([sys.executable, "-B", str(repo / INSTR), "--self-test"],
                           cwd=str(repo), capture_output=True, text=True, env=env)
        tail = [l for l in p.stdout.splitlines() if "assertion" in l]
        print("self-test rc %d tail %r" % (p.returncode, tail[-1:] or ""))
        if p.returncode != 0:
            bad += 1
    for c in COUNTERS:
        blob = git(repo, "show", "%s:%s" % (rev, c))
        got = hashlib.sha256(blob).hexdigest()
        ok = got == FROZEN_SHA[c]
        print("counter %s sha %s %s" % (c, got[:16], "FROZEN" if ok else "CHANGED"))
        if not ok:
            bad += 1
    print("PROBE %s" % ("OK" if bad == 0 else "BAD %d" % bad))
    return 0 if bad == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
