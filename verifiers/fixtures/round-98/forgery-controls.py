#!/usr/bin/env python3
"""forgery-controls (round 98, claim C2, frozen counting command; plans/round-98.md).

Usage: python3 -B verifiers/fixtures/round-98/forgery-controls.py {v5|v6|v6-as-v5} [REV]
  v5        the round-97 counter  verifiers/fixtures/round-97/selftest-kills.py (tables r96c1, r95c1)
  v6        the round-98 counter  verifiers/fixtures/round-98/selftest-kills.py (tables r96c1, r95c1)
  v6-as-v5  the round-98 counter with --rules v5 (cause control: rules 8-10 switched off)
  REV       lane revision whose counter bytes and committed world patches are read (default: master)

Successor of verifiers/fixtures/round-97/forgery-controls.py (unchanged there). The counter bytes are
read with `git show REV:<counter>` into scratch, never from the working tree. Every world is a
committed patch re-applied on the round-96 freeze 679775ab in a scratch clone of the lane, committed
there under the identity `forgery <forgery@invalid>`, never in the lane:

  forgery g3-recompile-compare  (round 96) recompiles the on-disk source and compares code objects
  forgery g7-stateful-fake      (round 96) TMPDIR marker on the first run, fake failure afterwards
  forgery g8-clone-marker       (round 96) the same with the marker next to the instrument
  forgery g10-head-compare      (round 97) compares its code objects with `git show HEAD:<instrument>`
  forgery g11-schedule-reader   (round 97) replays the counter's schedule from KOTOBA_R97_SEED and the
                                counter source on the clone's master ref; measured SEEDED: the
                                counter runs with KOTOBA_R97_SEED=deadbeefdeadbeef for this world
  bound   g2b-guard-aware-sniff (round 96) guard-aware code-object sniffer (reported, not scored)
  honest  h1-r96-landing        the round-96 table at the round-96 landing 801dd9bc (honest arms)
  honest  h2-r95c1              the round-95 table at REV (honest arms on check_mutation_battery.py)

A forgery is REFUSED iff the counter does not print `<C>-PREDICATE-MET` with exit 0 for it; an honest
world is HELD iff it does. Predicate (frozen; the same sentence in plans/round-98.md):
  C2-PREDICATE-MET iff forgeries refused 5 of 5 AND honest held 2 of 2.
Output: one line per world, then
  `C2 <mode>: forgeries refused R of 5; honest held H of 2; bound g2b <reading>`
  and `C2-PREDICATE-MET` / `C2-PREDICATE-UNMET` / `C2-NOT-EVALUATED`. Exit 0 / 1 / 2.
Scratch under ${HYAKU_SCRATCH:-/fast/scratch/hyaku}/kotoba-r98/forgery-controls, removed on exit.
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
P96 = ".ufo/waves/round-96/w1/ExecCounterForgeryR96"
P97 = ".ufo/waves/round-97/w1/ExecForgeryV5"
COUNTERS = {
    "v5": ("verifiers/fixtures/round-97/selftest-kills.py", []),
    "v6": ("verifiers/fixtures/round-98/selftest-kills.py", []),
    "v6-as-v5": ("verifiers/fixtures/round-98/selftest-kills.py", ["--rules", "v5"]),
}
SEED = "deadbeefdeadbeef"
# (world, patch dir, replay seed for the counter or None)
FORGERIES = [("g3-recompile-compare", P96, None), ("g7-stateful-fake", P96, None),
             ("g8-clone-marker", P96, None), ("g10-head-compare", P97, None),
             ("g11-schedule-reader", P97, SEED)]
BOUND = ("g2b-guard-aware-sniff", P96, None)


class NotEvaluated(Exception):
    pass


def git(*args: str, cwd: Path | None = None, env: dict | None = None) -> subprocess.CompletedProcess:
    return subprocess.run(["git", *args], cwd=cwd, env=env, stdout=subprocess.PIPE, stderr=subprocess.PIPE)


def main(argv: list[str]) -> int:
    if not argv or argv[0] not in COUNTERS or len(argv) > 2:
        print("usage: forgery-controls.py {v5|v6|v6-as-v5} [REV]", file=sys.stderr)
        return 2
    mode = argv[0]
    counter_path, extra = COUNTERS[mode]
    root = Path(os.environ.get("HYAKU_SCRATCH", "/fast/scratch/hyaku")) / "kotoba-r98" / "forgery-controls"
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
        base_env = {k: v for k, v in os.environ.items() if k != "KOTOBA_R97_SEED"}
        base_env["HYAKU_SCRATCH"] = str(work / "scratch")
        ident = dict(os.environ, GIT_AUTHOR_NAME="forgery", GIT_AUTHOR_EMAIL="forgery@invalid",
                     GIT_COMMITTER_NAME="forgery", GIT_COMMITTER_EMAIL="forgery@invalid")

        def build(world: str, pdir: str) -> str:
            patch = git("-C", str(LANE), "show", "%s:%s/%s.patch" % (rev, pdir, world))
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

        def measure(label: str, table: str, wrev: str, repo: Path, seed: str | None) -> bool:
            env = dict(base_env, KOTOBA_R97_SEED=seed) if seed else base_env
            p = subprocess.run([sys.executable, "-B", str(counter), table, wrev, str(repo), *extra],
                               env=env, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, timeout=3600)
            out = p.stdout.decode("utf-8", "replace").splitlines()
            tally = next((ln for ln in reversed(out) if " targets killed " in ln), "<no tally>")
            pred = next((ln for ln in reversed(out) if "-PREDICATE-" in ln or "-NOT-EVALUATED" in ln), "<no predicate>")
            met = p.returncode == 0 and pred.endswith("-PREDICATE-MET")
            print("%s%s rc %d %s | %s" % (label, " seed " + seed if seed else "", p.returncode, pred, tally))
            return met

        refused = 0
        for world, pdir, seed in FORGERIES:
            wrev = build(world, pdir)
            refused += not measure("forgery %s %s" % (world, wrev[:12]), "r96c1", wrev, work / "worlds" / world, seed)
        wrev = build(BOUND[0], BOUND[1])
        bound_met = measure("bound %s %s" % (BOUND[0], wrev[:12]), "r96c1", wrev, work / "worlds" / BOUND[0], None)
        held = 0
        held += measure("honest h1-r96-landing %s" % landing_rev[:12], "r96c1", landing_rev, LANE, None)
        held += measure("honest h2-r95c1 %s" % rev[:12], "r95c1", rev, LANE, None)
        print("C2 %s: forgeries refused %d of 5; honest held %d of 2; bound g2b %s"
              % (mode, refused, held, "MET" if bound_met else "UNMET"))
        met = refused == 5 and held == 2
        print("C2-PREDICATE-%s" % ("MET" if met else "UNMET"))
        return 0 if met else 1
    except NotEvaluated as exc:
        print("C2-NOT-EVALUATED: %s" % exc)
        return 2
    finally:
        shutil.rmtree(work, ignore_errors=True)


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
