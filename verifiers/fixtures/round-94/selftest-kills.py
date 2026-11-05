#!/usr/bin/env python3
"""selftest-kills (round 94, claims C1 and C2, frozen counting command; plans/round-94.md).

Usage: python3 -B verifiers/fixtures/round-94/selftest-kills.py {c1|c2} [REV] [REPO]
  REV   full commit to measure (default: the tip of branch master of REPO)
  REPO  repository to clone REV from (default: this lane; a scratch repo for a candidate or forgery)

Method. REPO is cloned (--shared) into a scratch dir and checked out at REV. The claim's instrument
is run as `python3 -B <instrument> --self-test` from the clone root, once unmodified (honest) and
once per mutant. Each mutant is a literal text substitution of the instrument's bytes at REV, made
in the clone's working tree only (never committed); its anchor must match exactly the declared
number of times and the mutated file must compile, else the run is could-not-evaluate. A mutant is
KILLED iff its self-test exits non-zero within the timeout (a timeout is could-not-evaluate, never a
kill).

Mutant tables (frozen):
  c1 — verifiers/check_mutation_battery.py
    target k1-worktree-manifest : the --rev kill-set check reads the WORKING-TREE manifest
                                  (round-93 MutTesterKillPin m3, F1)
    target k2-label-every-cne   : every could-not-evaluate line carries `arm kill-set-size:`
                                  (round-93 MutTesterKillPin m6, F4; the round-93 forgery shape)
    target k3-accept-added-rows : the pin accepts a kill-row count above the pin (`n >= want`)
                                  (round-93 MutTesterKillPin F2: no added-row arm)
    positive k0-accept-any      : the pin accepts any count (killed by the existing dropped-row arms)
  c2 — verifiers/check_tip_battery.py
    target p1-one-key-hardcode  : key coverage only for verifiers/check_correction_sweep.py
                                  (round-93 MutTesterPinCov m5)
    target p2-skip-first-key    : key coverage skips the first BATTERY script (`scripts[1:]`)
    positive p0-skip-last-key   : key coverage skips the last BATTERY script (`scripts[:-1]`;
                                  killed by the existing BATTERY[5] arms)

Decoy guard (anti-sniffing): a self-test could "kill" a mutant by searching its own source text for
the mutant's replacement instead of observing behaviour. For every TARGET mutant the counter also
runs a DECOY: the unmodified instrument with the replacement lines appended as comments
(`# r94-decoy <line>`), which changes no behaviour. A behavioural self-test exits 0 on every decoy;
a decoy whose self-test exits non-zero is a guard failure. Bound: a sniffer that skips comments
(e.g. AST-based) is not caught by this guard.

Predicate (frozen; the same sentence in plans/round-94.md):
  <C>-PREDICATE-MET iff (honest) the unmodified self-test exits 0 and prints `0 failure(s)`;
  (targets) every target mutant applies and is KILLED; (positive) the positive mutant applies and is
  KILLED; (guard) every target decoy's self-test exits 0.
Output: one line per run, then
  `<C> targets killed K of N; positive killed P of 1; honest rc R; decoys held D of N`
  and `<C>-PREDICATE-MET` / `<C>-PREDICATE-UNMET` / `<C>-NOT-EVALUATED`.
Exit 0 met, 1 unmet, 2 could-not-evaluate.
Scratch under ${HYAKU_SCRATCH:-/fast/scratch/hyaku}/kotoba-r94/selftest-kills, removed on exit.
"""
from __future__ import annotations

import os
import py_compile
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

TIMEOUT_S = 600

CLAIMS = {
    "c1": {
        "instrument": "verifiers/check_mutation_battery.py",
        "targets": [
            ("k1-worktree-manifest",
             "ok_pin, pin_detail = kill_set_check(committed, pinned)", 1,
             'ok_pin, pin_detail = kill_set_check((lane / MANIFEST).read_text(encoding="utf-8"), pinned)',
             ),
            ("k2-label-every-cne",
             'print("could-not-evaluate: %s" % exc)', 3,
             'print("could-not-evaluate: arm kill-set-size: %s" % exc)',
             ),
            ("k3-accept-added-rows",
             'return n == want, "observed', 1,
             'return n >= want, "observed',
             ),
        ],
        "positive": ("k0-accept-any", 'return n == want, "observed', 1, 'return True, "observed'),
    },
    "c2": {
        "instrument": "verifiers/check_tip_battery.py",
        "targets": [
            ("p1-one-key-hardcode",
             "        for path in scripts:\n            if path not in INSTRUMENT_PINS:", 1,
             '        for path in ("verifiers/check_correction_sweep.py",):\n'
             "            if path not in INSTRUMENT_PINS:",
             ),
            ("p2-skip-first-key",
             "        for path in scripts:\n            if path not in INSTRUMENT_PINS:", 1,
             "        for path in scripts[1:]:\n            if path not in INSTRUMENT_PINS:",
             ),
        ],
        "positive": ("p0-skip-last-key",
                     "        for path in scripts:\n            if path not in INSTRUMENT_PINS:", 1,
                     "        for path in scripts[:-1]:\n            if path not in INSTRUMENT_PINS:"),
    },
}


class NotEvaluated(Exception):
    pass


def run_selftest(clone: Path, instrument: str, env: dict) -> tuple[int, str]:
    try:
        proc = subprocess.run([sys.executable, "-B", instrument, "--self-test"], cwd=clone, env=env,
                              stdout=subprocess.PIPE, stderr=subprocess.STDOUT, timeout=TIMEOUT_S)
    except subprocess.TimeoutExpired:
        raise NotEvaluated("self-test timeout after %ds" % TIMEOUT_S)
    out = proc.stdout.decode("utf-8", "replace")
    return proc.returncode, out


def last_line(text: str) -> str:
    lines = [ln for ln in text.splitlines() if ln.strip()]
    return lines[-1] if lines else "<no output>"


def main(argv: list[str]) -> int:
    if not argv or argv[0] not in CLAIMS or len(argv) > 3:
        print("usage: selftest-kills.py {c1|c2} [REV] [REPO]", file=sys.stderr)
        return 2
    claim = argv[0]
    tag = claim.upper()
    spec = CLAIMS[claim]
    lane = Path(__file__).resolve().parents[3]
    repo = Path(argv[2]).resolve() if len(argv) > 2 else lane
    want_rev = argv[1] if len(argv) > 1 else "master"
    got = subprocess.run(["git", "-C", str(repo), "rev-parse", "--verify", "-q", want_rev + "^{commit}"],
                         stdout=subprocess.PIPE, stderr=subprocess.DEVNULL)
    if got.returncode != 0:
        print("%s-NOT-EVALUATED: REV %s is not a commit of %s" % (tag, want_rev, repo))
        return 2
    rev = got.stdout.decode().strip()
    root = Path(os.environ.get("HYAKU_SCRATCH", "/fast/scratch/hyaku")) / "kotoba-r94" / "selftest-kills"
    root.mkdir(parents=True, exist_ok=True)
    work = Path(tempfile.mkdtemp(prefix="run.", dir=root))
    try:
        env = dict(os.environ, TMPDIR=str(work / "tmp"), PYTHONDONTWRITEBYTECODE="1")
        (work / "tmp").mkdir()
        clone = work / "world" / "kotoba-shokunin"
        clone.parent.mkdir()
        for cmd in (["git", "clone", "-q", "--shared", str(repo), str(clone)],
                    ["git", "-C", str(clone), "checkout", "-q", rev]):
            if subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL).returncode != 0:
                raise NotEvaluated("clone or checkout failed")
        print("claim %s rev %s repo %s instrument %s" % (claim, rev, repo, spec["instrument"]))
        path = clone / spec["instrument"]
        if not path.is_file():
            raise NotEvaluated("instrument %s absent at %s" % (spec["instrument"], rev))
        original = path.read_text(encoding="utf-8")

        rc_h, out_h = run_selftest(clone, spec["instrument"], env)
        honest_ok = rc_h == 0 and "0 failure(s)" in out_h
        print("honest rc %d: %s" % (rc_h, last_line(out_h)))

        def mutate(name: str, anchor: str, count: int, repl: str) -> bool:
            found = original.count(anchor)
            if found != count:
                raise NotEvaluated("anchor miss: %s matches %d time(s), expected %d" % (name, found, count))
            path.write_text(original.replace(anchor, repl), encoding="utf-8")
            try:
                py_compile.compile(str(path), cfile=str(work / "tmp" / "c.pyc"), doraise=True)
            except py_compile.PyCompileError as exc:
                raise NotEvaluated("mutant %s does not compile: %s" % (name, exc.msg.splitlines()[-1]))
            try:
                rc, out = run_selftest(clone, spec["instrument"], env)
            finally:
                path.write_text(original, encoding="utf-8")
            killed = rc != 0
            print("mutant %s rc %d %s: %s" % (name, rc, "KILLED" if killed else "SURVIVED", last_line(out)))
            return killed

        killed = sum(1 for name, a, c, w in spec["targets"] if mutate(name, a, c, w))
        pname, pa, pc, pw = spec["positive"]
        pos = 1 if mutate(pname, pa, pc, pw) else 0
        held = 0
        for name, _a, _c, w in spec["targets"]:
            decoy = original.rstrip("\n") + "\n" + "".join("# r94-decoy " + ln + "\n" for ln in w.splitlines())
            path.write_text(decoy, encoding="utf-8")
            try:
                rc_d, out_d = run_selftest(clone, spec["instrument"], env)
            finally:
                path.write_text(original, encoding="utf-8")
            held += rc_d == 0
            print("decoy %s rc %d %s: %s" % (name, rc_d, "HELD" if rc_d == 0 else "KILLED (sniffing)", last_line(out_d)))
        if path.read_text(encoding="utf-8") != original:
            raise NotEvaluated("instrument not restored")
        n = len(spec["targets"])
        print("%s targets killed %d of %d; positive killed %d of 1; honest rc %d; decoys held %d of %d"
              % (tag, killed, n, pos, rc_h, held, n))
        met = honest_ok and killed == n and pos == 1 and held == n
        print("%s-PREDICATE-%s" % (tag, "MET" if met else "UNMET"))
        return 0 if met else 1
    except NotEvaluated as exc:
        print("%s-NOT-EVALUATED: %s" % (tag, exc))
        return 2
    finally:
        shutil.rmtree(work, ignore_errors=True)


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
