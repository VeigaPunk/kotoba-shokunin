#!/usr/bin/env python3
"""q79_location_control.py -- is a counter's verdict the same on its bytes anywhere?

Round 87, attempt 2 (integration owner's control; evidence only, not an instrument
registered in SKILL.md's gate registry).

The round's C2 item D5(iii) runs `verifiers/verify_corpus_integrity.py` inside the
lane worktree and compares the red set to an exact expectation.  That gate
resolves fleet-root report pointers, so the question is whether the same committed
bytes score the same in a relocated checkout.

Usage:
  python3 -B q79_location_control.py --rev <rev> [--keep] [--work DIR]

Worlds:
  lane   -- the real lane checkout, worktree at <rev>
  clone  -- `git clone --shared` of the lane at <rev>, in a scratch parent that
            holds no `.ufo/reports/` tree
  pinned -- the same clone with the two fleet reports the lane's corpus cites
            copied into the clone's own `../.ufo/reports/` resolution root

Exit 0 iff every world reports the same (red set, detail sites); 1 otherwise;
2 = could not evaluate.  It deliberately does not repair or edit anything.
"""
from __future__ import annotations

import argparse
import json
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

LANE = Path("/home/vgpnk/Projects/shokunin/kotoba-shokunin")
FLEET = Path("/home/vgpnk/Projects/shokunin")
GATE = "verifiers/verify_corpus_integrity.py"
REPORTS = [".ufo/reports/round-84/kama.md", ".ufo/reports/round-76/kotoba.md"]


def git(repo: Path, *args: str) -> str:
    return subprocess.run(["git", "-C", str(repo), *args], capture_output=True,
                          text=True, check=True).stdout.strip()


def reading(repo: Path) -> dict:
    """Run the lane gate in `repo` and return its red set + detail sites."""
    run = subprocess.run([sys.executable, "-B", GATE, "--json"], cwd=str(repo),
                         capture_output=True, text=True, timeout=600)
    if run.returncode not in (0, 1):
        raise RuntimeError("%s exit=%d: %s" % (GATE, run.returncode,
                                               (run.stdout + run.stderr)[-300:]))
    doc = json.loads(run.stdout)
    red = sorted(r["check"] for r in doc.get("results", [])
                 if r.get("verdict") != "PASS")
    corpus = (doc.get("observed") or {}).get("corpus") or {}
    sites = {
        "report_dead": sorted(corpus.get("report_dead_detail") or []),
        "commit_unresolvable": sorted(corpus.get("commit_unresolvable_detail") or []),
    }
    return {"exit": run.returncode, "red": red, "sites": sites}


def counter_line(repo: Path, rev: str) -> tuple[int, str]:
    run = subprocess.run([sys.executable, "-B", "verifiers/check_r86_routed_repairs.py",
                          "--rev", rev], cwd=str(repo), capture_output=True,
                         text=True, timeout=900)
    d5 = [ln for ln in run.stdout.splitlines() if ln.startswith(("PASS d5", "FAIL d5"))]
    return run.returncode, (d5[-1] if d5 else "<no d5 line>")


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--rev")
    ap.add_argument("--work")
    ap.add_argument("--keep", action="store_true")
    args = ap.parse_args(argv)
    if not args.rev:
        ap.error("--rev is required")
    parent = Path(args.work or tempfile.mkdtemp(prefix="q79-", dir="/fast/scratch/hyaku"))
    work = Path(tempfile.mkdtemp(prefix="loc-", dir=str(parent)))
    rev = git(LANE, "rev-parse", args.rev)
    print("rev %s" % rev)
    worlds: dict[str, dict] = {}

    tip = git(LANE, "rev-parse", "master")
    if tip != rev:
        print("could-not-evaluate: lane worktree is at %s, not %s" % (tip[:12], rev[:12]))
        return 2
    worlds["lane"] = reading(LANE)
    worlds["lane"]["counter"] = counter_line(LANE, rev)

    clone = work / "repo"
    subprocess.run(["git", "clone", "-q", "--shared", str(LANE), str(clone)], check=True)
    if git(clone, "rev-parse", "--show-toplevel") != str(clone):
        print("could-not-evaluate: clone toplevel mismatch")
        return 2
    git(clone, "checkout", "-q", "-B", "master", rev)
    worlds["clone"] = reading(clone)
    worlds["clone"]["counter"] = counter_line(clone, rev)

    pinned = work / "pinned"
    subprocess.run(["git", "clone", "-q", "--shared", str(LANE), str(pinned)], check=True)
    git(pinned, "checkout", "-q", "-B", "master", rev)
    for rel in REPORTS:
        src = FLEET / rel
        dst = pinned.parent / rel
        if src.is_file():
            dst.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(src, dst)
        else:
            print("note: %s absent on the fleet root; pinned world omits it" % rel)
    worlds["pinned"] = reading(pinned)
    worlds["pinned"]["counter"] = counter_line(pinned, rev)

    verdicts = {(tuple(w["red"]), json.dumps(w["sites"], sort_keys=True))
                for w in worlds.values()}
    for name, w in worlds.items():
        print("world %-6s gate_exit=%d red=%s" % (name, w["exit"], w["red"]))
        for k, v in w["sites"].items():
            for line in v:
                print("   detail %-20s %s" % (k, line))
        print("   counter exit=%d  %s" % (w["counter"][0], w["counter"][1]))

    if args.keep:
        print("kept %s" % work)
    else:
        shutil.rmtree(parent, ignore_errors=True)
    if len(verdicts) == 1:
        print("q79 control: PASS (same bytes, every world the same red set and detail sites)")
        return 0
    print("q79 control: FAIL (same bytes, world-dependent verdict: %d distinct readings)"
          % len(verdicts))
    return 1


if __name__ == "__main__":
    sys.exit(main())
