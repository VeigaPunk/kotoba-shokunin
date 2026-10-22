#!/usr/bin/env python3
r"""check_could_not_evaluate.py -- frozen counter for the round-55 C2 (operability) claim.

Round 55, claim C2 (axis: operability; the surface changed is the error paths
of thirteen registered lane gates under `verifiers/`).  Every one of the
thirteen gates is registered in `SKILL.md` § Gate registry with the verdict
map `... 2=could-not-evaluate ...`; the round-54 falsify wave
(`.ufo/waves/round-54/falsify/W2Row*.md`) found several that exit 1 (`failed`)
when they cannot evaluate at all.  The claim is that each gate exits 2 on two
frozen could-not-evaluate inputs, while it still exits 0 on its own self-test
and 0 or 1 (a real verdict) on a real revision.

This counter is frozen at the round-55 plan commit.  The gates, the probe
arguments, the expected codes and the control rules are pinned here and never
read from the revision measured.  A later change to any of them is a second
measurement, never the declared one (corpus/QUALITY.md Q28).

Trust boundary (Q33): the counter RUNS the measured revision's own gate
scripts.  A revision could rewrite a gate to exit 2 on everything; the two
controls below are the counter's own guard against that, and the claim also
cites guards outside this file (a diff-scope review of the thirteen gates'
judging lines, and the random revision this counter makes itself).

Method, all inside a fresh sandbox clone of the lane at <rev> (a temporary
directory; the lane checkout and its Git index are never touched):
  * class R (unknown revision): R is 40 random hex characters made by this
    counter at run time (`os.urandom`), checked to be no object of the clone;
    the gate gets R where it takes a revision.  Expected exit: 2.
  * class G (git absent): the gate runs on the real revision with PATH set to
    one temporary directory holding only a `python3` link to this
    interpreter, so `git` cannot be found.  Expected exit: 2.
  * control S (self-test): `<gate> --self-test` with the normal PATH.
    Expected exit: 0.
  * control V (real verdict): the gate on the real revision with the normal
    PATH.  Expected exit: 0 or 1.
A probe is HONOURED iff its exit code is exactly 2 within TIMEOUT seconds.
A gate's controls HOLD iff S exits 0 and V exits 0 or 1, each within TIMEOUT.

Output: one line per run, then
`could-not-evaluate probes honoured <K> of 25; controls held <C> of 13`.
Exit 0 iff K == 25 and C == 13; 1 otherwise; 2 = this counter could not
evaluate (no git, unknown <rev>, clone failure).  The declared C2 predicate is
this command at the measured revision exiting 0.

Usage:
  python3 -B verifiers/check_could_not_evaluate.py --rev <rev> [--json]
  python3 -B verifiers/check_could_not_evaluate.py --self-test
"""
from __future__ import annotations

import argparse
import json
import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

LANE = Path(__file__).resolve().parent.parent
TIMEOUT = 600
REV_TOKEN = "{REV}"
RAND_TOKEN = "{RAND}"

# gate -> (real-revision arguments, [class-R argument lists])
GATES: dict[str, tuple[list[str], list[list[str]]]] = {
    "box_proof_case_deletion.py": (["--rev", REV_TOKEN], [["--rev", RAND_TOKEN]]),
    "check_gate_finding_delta.py": (["--base", REV_TOKEN, "--head", REV_TOKEN],
                                    [["--base", RAND_TOKEN, "--head", REV_TOKEN],
                                     ["--base", REV_TOKEN, "--head", RAND_TOKEN]]),
    "check_overlap_levers.py": (["--rev", REV_TOKEN], [["--rev", RAND_TOKEN]]),
    "check_sources_append_only.py": (["--rev", REV_TOKEN], [["--rev", RAND_TOKEN]]),
    "check_mcp_instructions.py": (["--rev", REV_TOKEN], [["--rev", RAND_TOKEN]]),
    "check_description_thresholds.py": (["--rev", REV_TOKEN], [["--rev", RAND_TOKEN]]),
    "check_alwayson_boxes.py": (["--rev", REV_TOKEN], [["--rev", RAND_TOKEN]]),
    "check_callee_rename.py": (["--rev", REV_TOKEN], [["--rev", RAND_TOKEN]]),
    "check_opencode_repin.py": (["--rev", REV_TOKEN], [["--rev", RAND_TOKEN]]),
    "check_correction_sweep.py": (["--rev", REV_TOKEN], [["--rev", RAND_TOKEN]]),
    "check_gate_registry.py": (["--rev", REV_TOKEN], [["--rev", RAND_TOKEN]]),
    "check_assertion_floors.py": ([], []),
    "verify_corpus_independent.py": ([], []),
}
N_PROBES = 25
N_GATES = 13


class EnvError(Exception):
    pass


def plan_runs(gates: dict[str, tuple[list[str], list[list[str]]]]) -> list[dict]:
    """The frozen run list: per gate, its R probes, one G probe, then S and V."""
    runs = []
    for gate, (real, rprobes) in gates.items():
        for a in rprobes:
            runs.append({"gate": gate, "kind": "R", "args": a, "expect": "2"})
        runs.append({"gate": gate, "kind": "G", "args": real, "expect": "2"})
        runs.append({"gate": gate, "kind": "S", "args": ["--self-test"], "expect": "0"})
        runs.append({"gate": gate, "kind": "V", "args": real, "expect": "0|1"})
    return runs


def ok(expect: str, code: int | None) -> bool:
    return code is not None and str(code) in expect.split("|")


def tally(runs: list[dict]) -> tuple[int, int]:
    honoured = sum(1 for r in runs if r["kind"] in "RG" and ok(r["expect"], r.get("code")))
    held = 0
    for gate in dict.fromkeys(r["gate"] for r in runs):
        ctl = [r for r in runs if r["gate"] == gate and r["kind"] in "SV"]
        if ctl and all(ok(r["expect"], r.get("code")) for r in ctl):
            held += 1
    return honoured, held


def git(*args: str, cwd: Path | None = None) -> subprocess.CompletedProcess:
    try:
        return subprocess.run(["git", *args], cwd=cwd, capture_output=True, text=True)
    except OSError as e:
        raise EnvError("git not runnable: %s" % e) from e


def run_one(tree: Path, run: dict, rev: str, rand: str, nogit_bin: Path) -> int | None:
    args = [rev if a == REV_TOKEN else rand if a == RAND_TOKEN else a for a in run["args"]]
    env = dict(os.environ)
    for k in ("GIT_DIR", "GIT_WORK_TREE", "GIT_INDEX_FILE"):
        env.pop(k, None)
    if run["kind"] == "G":
        env["PATH"] = str(nogit_bin)
    try:
        p = subprocess.run([sys.executable, "-B", str(tree / "verifiers" / run["gate"]), *args],
                           cwd=tree, env=env, capture_output=True, timeout=TIMEOUT)
    except subprocess.TimeoutExpired:
        return None
    return p.returncode


def measure(rev: str) -> tuple[str, list[dict]]:
    r = git("-C", str(LANE), "rev-parse", "--verify", "--quiet", "%s^{commit}" % rev)
    if r.returncode != 0:
        raise EnvError("revision %r is not a commit in %s" % (rev, LANE))
    full = r.stdout.strip()
    runs = plan_runs(GATES)
    with tempfile.TemporaryDirectory(prefix="kotoba-r55-cne-") as td:
        tree = Path(td) / "lane"
        c = git("clone", "-q", "--no-checkout", str(LANE), str(tree))
        if c.returncode != 0:
            raise EnvError("clone failed: %s" % c.stderr.strip())
        c = git("-C", str(tree), "checkout", "-q", "--detach", full)
        if c.returncode != 0:
            raise EnvError("checkout %s failed: %s" % (full, c.stderr.strip()))
        while True:
            rand = os.urandom(20).hex()
            if git("-C", str(tree), "cat-file", "-e", rand).returncode != 0:
                break
        nogit = Path(td) / "nogit-bin"
        nogit.mkdir()
        (nogit / "python3").symlink_to(sys.executable)
        if shutil.which("git", path=str(nogit)):
            raise EnvError("git found on the no-git PATH")
        for run in runs:
            run["code"] = run_one(tree, run, full, rand, nogit)
    return full, runs


def self_test() -> int:
    assertions = 0
    failures = 0

    def check(name: str, actual: object, expected: object) -> None:
        nonlocal assertions, failures
        assertions += 1
        if actual != expected:
            failures += 1
            print("FAIL %s: got %r, expected %r" % (name, actual, expected))

    runs = plan_runs(GATES)
    check("frozen probe count", sum(1 for r in runs if r["kind"] in "RG"), N_PROBES)
    check("frozen gate count", len(GATES), N_GATES)
    check("every gate has S and V",
          all(sum(1 for r in runs if r["gate"] == g and r["kind"] in "SV") == 2 for g in GATES),
          True)

    def world(codes: dict[str, int | None]) -> tuple[int, int]:
        rs = plan_runs({"a.py": (["--rev", REV_TOKEN], [["--rev", RAND_TOKEN]]),
                        "b.py": ([], [])})
        for r in rs:
            r["code"] = codes.get("%s:%s" % (r["gate"], r["kind"]))
        return tally(rs)

    good = {"a.py:R": 2, "a.py:G": 2, "a.py:S": 0, "a.py:V": 1,
            "b.py:G": 2, "b.py:S": 0, "b.py:V": 0}
    check("all honoured and held", world(good), (3, 2))
    check("probe exiting 1 is not honoured", world({**good, "a.py:R": 1}), (2, 2))
    check("probe timing out is not honoured", world({**good, "b.py:G": None}), (2, 2))
    check("always-2 gate fails its V control", world({**good, "a.py:V": 2}), (3, 1))
    check("red self-test fails the S control", world({**good, "b.py:S": 1}), (3, 1))
    check("self-test exiting 2 fails the S control", world({**good, "a.py:S": 2}), (3, 1))
    check("V exit 0 or 1 both hold", world({**good, "a.py:V": 0}), (3, 2))
    check("exit 3 is not could-not-evaluate here", world({**good, "a.py:G": 3}), (2, 2))
    check("token substitution", [rev if a == REV_TOKEN else a for a in ["--rev", REV_TOKEN]
                                 for rev in ["abc"]], ["--rev", "abc"])

    print("self-test: %d failure(s) over %d assertions" % (failures, assertions))
    return 1 if failures else 0


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--rev")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--self-test", action="store_true")
    args = ap.parse_args(argv)
    if args.self_test:
        if args.rev or args.json:
            ap.error("--self-test cannot be combined with --rev or --json")
        return self_test()
    if not args.rev:
        ap.error("--rev is required")
    try:
        full, runs = measure(args.rev)
    except (EnvError, OSError) as e:
        print("could-not-evaluate: %s" % e, file=sys.stderr)
        return 2
    honoured, held = tally(runs)
    if args.json:
        print(json.dumps({"rev": full, "runs": runs, "honoured": honoured,
                          "probes": N_PROBES, "held": held, "gates": N_GATES}, indent=1))
    else:
        print("measured %s" % full)
        for r in runs:
            print("%-34s %s expect %-3s got %s %s" % (
                r["gate"], r["kind"], r["expect"], r["code"],
                "ok" if ok(r["expect"], r["code"]) else "MISS"))
    print("could-not-evaluate probes honoured %d of %d; controls held %d of %d"
          % (honoured, N_PROBES, held, N_GATES))
    return 0 if honoured == N_PROBES and held == N_GATES else 1


if __name__ == "__main__":
    sys.exit(main())
