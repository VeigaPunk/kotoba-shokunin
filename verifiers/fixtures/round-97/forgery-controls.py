#!/usr/bin/env python3
"""forgery-controls (round 97, claim C2, frozen counting command; plans/round-97.md).

Usage: python3 -B verifiers/fixtures/round-97/forgery-controls.py {v4|v5|v5-as-v4} [REV]
  v4        the round-96 counter  verifiers/fixtures/round-96/selftest-kills.py (tables c1, r95c1)
  v5        the round-97 counter  verifiers/fixtures/round-97/selftest-kills.py (tables r96c1, r95c1)
  v5-as-v4  the round-97 counter with --rules v4
  REV       lane revision whose counter bytes are measured (default: tip of master)

The counter bytes are read with `git show REV:<counter>` into scratch, never from the working tree.
Worlds (committed round-96 patches, re-applied here on the round-96 freeze commit 679775ab in a
scratch clone, committed under the identity `forgery <forgery@invalid>`, never in the lane):

  forgery g3-recompile-compare  recompiles the on-disk source and compares code objects
  forgery g7-stateful-fake      TMPDIR marker on the first run, fake reported failure afterwards
  forgery g8-clone-marker       the same with the marker next to the instrument in the clone
  bound   g2b-guard-aware-sniff guard-aware code-object sniffer (disclosed bound; reported, not scored)
  honest  h1-r96-landing        the round-96 table at the round-96 landing 801dd9bc (honest arms)
  honest  h2-r95c1              the round-95 table at REV (honest arms on check_mutation_battery.py)

A forgery is REFUSED iff the counter does not print `<C>-PREDICATE-MET` with exit 0 for it; an honest
world is HELD iff it does. Predicate (frozen; the same sentence in plans/round-97.md):
  C2-PREDICATE-MET iff forgeries refused 3 of 3 AND honest held 2 of 2.
Output: one line per world, then
  `C2 <mode>: forgeries refused R of 3; honest held H of 2; bound g2b <reading>`
  and `C2-PREDICATE-MET` / `C2-PREDICATE-UNMET` / `C2-NOT-EVALUATED`. Exit 0 / 1 / 2.
Scratch under ${HYAKU_SCRATCH:-/fast/scratch/hyaku}/kotoba-r97/forgery-controls, removed on exit.
"""
from __future__ import annotations

import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

LANE = Path(__file__).resolve().parents[3]
R96_FREEZE = "679775abb9277a7b8d17f060b0f5b4ced2b127b6"
R96_LANDING = "801dd9bc"
PATCH_DIR = ".ufo/waves/round-96/w1/ExecCounterForgeryR96"
COUNTERS = {
    "v4": ("verifiers/fixtures/round-96/selftest-kills.py", "c1", []),
    "v5": ("verifiers/fixtures/round-97/selftest-kills.py", "r96c1", []),
    "v5-as-v4": ("verifiers/fixtures/round-97/selftest-kills.py", "r96c1", ["--rules", "v4"]),
}
FORGERIES = ["g3-recompile-compare", "g7-stateful-fake", "g8-clone-marker"]
BOUND = "g2b-guard-aware-sniff"


class NotEvaluated(Exception):
    pass


def git(*args: str, cwd: Path | None = None, env: dict | None = None) -> subprocess.CompletedProcess:
    return subprocess.run(["git", *args], cwd=cwd, env=env, stdout=subprocess.PIPE, stderr=subprocess.PIPE)


def main(argv: list[str]) -> int:
    if not argv or argv[0] not in COUNTERS or len(argv) > 2:
        print("usage: forgery-controls.py {v4|v5|v5-as-v4} [REV]", file=sys.stderr)
        return 2
    mode = argv[0]
    counter_path, claim, extra = COUNTERS[mode]
    root = Path(os.environ.get("HYAKU_SCRATCH", "/fast/scratch/hyaku")) / "kotoba-r97" / "forgery-controls"
    root.mkdir(parents=True, exist_ok=True)
    work = Path(tempfile.mkdtemp(prefix="run.", dir=root))
    try:
        got = git("-C", str(LANE), "rev-parse", "--verify", "-q", (argv[1] if len(argv) > 1 else "master") + "^{commit}")
        if got.returncode != 0:
            raise NotEvaluated("REV is not a commit of the lane")
        rev = got.stdout.decode().strip()
        landing = git("-C", str(LANE), "rev-parse", "--verify", "-q", R96_LANDING + "^{commit}")
        if landing.returncode != 0:
            raise NotEvaluated("round-96 landing %s absent" % R96_LANDING)
        landing_rev = landing.stdout.decode().strip()
        shown = git("-C", str(LANE), "show", "%s:%s" % (rev, counter_path))
        if shown.returncode != 0:
            raise NotEvaluated("counter %s absent at %s" % (counter_path, rev))
        counter = work / "lane" / counter_path
        counter.parent.mkdir(parents=True)
        counter.write_bytes(shown.stdout)
        print("C2 mode %s rev %s counter %s (%d bytes)" % (mode, rev, counter_path, len(shown.stdout)))
        env = dict(os.environ, HYAKU_SCRATCH=str(work / "scratch"))
        ident = dict(os.environ, GIT_AUTHOR_NAME="forgery", GIT_AUTHOR_EMAIL="forgery@invalid",
                     GIT_COMMITTER_NAME="forgery", GIT_COMMITTER_EMAIL="forgery@invalid")

        def build(world: str) -> str:
            patch = git("-C", str(LANE), "show", "%s:%s/%s.patch" % (rev, PATCH_DIR, world))
            if patch.returncode != 0:
                raise NotEvaluated("patch %s absent at %s" % (world, rev))
            d = work / "worlds" / world
            d.parent.mkdir(exist_ok=True)
            steps = [("clone", "-q", "--shared", "--no-checkout", str(LANE), str(d)),
                     ("-C", str(d), "checkout", "-q", "--detach", R96_FREEZE)]
            for s in steps:
                if git(*s).returncode != 0:
                    raise NotEvaluated("world %s: %s failed" % (world, s[2] if s[0] == "-C" else s[0]))
            top = git("-C", str(d), "rev-parse", "--show-toplevel").stdout.decode().strip()
            if Path(top).resolve() != d.resolve():
                raise NotEvaluated("world %s: toplevel %s is not the scratch repo" % (world, top))
            pf = work / (world + ".patch")
            pf.write_bytes(patch.stdout)
            if git("-C", str(d), "apply", "--index", str(pf)).returncode != 0:
                raise NotEvaluated("world %s: patch does not apply on %s" % (world, R96_FREEZE[:12]))
            if git("-C", str(d), "commit", "-q", "-m", "forgery " + world, env=ident).returncode != 0:
                raise NotEvaluated("world %s: commit failed" % world)
            return git("-C", str(d), "rev-parse", "HEAD").stdout.decode().strip()

        def measure(label: str, table: str, wrev: str, repo: Path) -> bool:
            p = subprocess.run([sys.executable, "-B", str(counter), table, wrev, str(repo), *extra],
                               env=env, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, timeout=3600)
            out = p.stdout.decode("utf-8", "replace").splitlines()
            tally = next((ln for ln in reversed(out) if " targets killed " in ln), "<no tally>")
            pred = next((ln for ln in reversed(out) if "-PREDICATE-" in ln or "-NOT-EVALUATED" in ln), "<no predicate>")
            met = p.returncode == 0 and pred.endswith("-PREDICATE-MET")
            print("%s rc %d %s | %s" % (label, p.returncode, pred, tally))
            return met

        refused = 0
        for world in FORGERIES:
            wrev = build(world)
            refused += not measure("forgery %s %s" % (world, wrev[:12]), claim, wrev, work / "worlds" / world)
        wrev = build(BOUND)
        bound_met = measure("bound %s %s" % (BOUND, wrev[:12]), claim, wrev, work / "worlds" / BOUND)
        held = 0
        held += measure("honest h1-r96-landing %s" % landing_rev[:12], claim, landing_rev, LANE)
        held += measure("honest h2-r95c1 %s" % rev[:12], "r95c1", rev, LANE)
        print("C2 %s: forgeries refused %d of 3; honest held %d of 2; bound g2b %s"
              % (mode, refused, held, "MET" if bound_met else "UNMET"))
        met = refused == 3 and held == 2
        print("C2-PREDICATE-%s" % ("MET" if met else "UNMET"))
        return 0 if met else 1
    except NotEvaluated as exc:
        print("C2-NOT-EVALUATED: %s" % exc)
        return 2
    finally:
        shutil.rmtree(work, ignore_errors=True)


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
