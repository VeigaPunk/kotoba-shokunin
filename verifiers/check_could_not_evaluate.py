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

Output: one line per run -- and the last stderr line of every run that did not
meet its expectation -- then
`could-not-evaluate probes honoured <K> of 29; controls held <C> of 13; red anchors held <A> of 13`.
Exit 0 iff K == 29, C == 13 and A == 13; 1 otherwise; 2 = this counter could
not evaluate (no git, unknown <rev>, clone failure, a shadow module).

Usage:
  PYTHONSAFEPATH=1 python3 -B verifiers/check_could_not_evaluate.py --rev <rev> [--json] [--out DIR]
  python3 -B verifiers/check_could_not_evaluate.py --self-test

Erratum (round 56, routed defect 3; this is v2).  The v1 counter was met, in
the sandbox worlds of the round-55 sizing critic
(`.ufo/waves/round-55/build/CriticC2Sizing.md`), by three shortcuts that
implement no evaluation: D wrapped each gate's entry so a real 1 became 2; P
put a preflight in the gate entry that exits 2 whenever git is missing or a
--rev/--base/--head value is not a commit; S added a `verifiers/argparse.py`
shadowing the standard-library module and forging this counter's child
results.  v2 closes each, adding only ways to fail:
  * Red anchors (ANCHORS below, frozen; the sizing critic's table): every gate
    must exit 1 on a revision or tree known to hold findings.  D shows here.
  * PYTHONSAFEPATH=1 in every gate environment, and a shadow scan: a run is
    could-not-evaluate (exit 2) if `verifiers/<name>.py` in this checkout or in
    the measured revision names a standard-library module.  S shows here.
  * Class N (no-git real verdicts): the four gates that accept `--root` read a
    directory and need no git, so a missing git must NOT be could-not-evaluate
    there.  An entry-only preflight exits 2 on the missing git alone and cannot
    meet these.  P shows here.
  * Every run's stdout and stderr are saved under --out (default: a fresh
    directory under the system temp dir, printed), so a receipt can show why a
    run exited as it did (e.g. that the assertion-floors G stderr names git and
    not a nested timeout).
This counter is a routed repair, not a claim: round-56 erratum 1 withdrew C2
before any data, so a measurement here has no target; the round-56 receipts
record it NOT MET (exit 1) on the D, P and S worlds and print its line on the
round-55 revision b0b7140b.
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
N_PROBES = 29
N_GATES = 13
N_ANCHORS = 13

# Frozen red anchors (round-56 erratum): gate -> arguments whose honest exit is
# 1.  Table: `.ufo/waves/round-55/build/CriticC2Sizing.md` (the sizing critic's
# probes.txt sections A and B), re-measured at b0b7140b on 2026-10-23.
ANCHORS: dict[str, list[str]] = {
    "box_proof_case_deletion.py": ["--rev", "f30464660c675d1c1e2851a3bf0366a3aaffe5a8"],
    "check_gate_finding_delta.py": ["--base", "e33715486a45a4a857b64c30e6b695f7995858b8",
                                    "--head", "a10240c0940f770a5f2a5f32a7e3c363dd5d40c0"],
    "check_overlap_levers.py": ["--rev", "43ca0bfb74372f2a67a48e0aeb2e35d0d98b1d10"],
    "check_sources_append_only.py": ["--rev", "a10240c0940f770a5f2a5f32a7e3c363dd5d40c0"],
    "check_mcp_instructions.py": ["--rev", "c8579a4c5b48789e56fb9060ddd48f33569e1215"],
    "check_description_thresholds.py": ["--rev", "422ffd1082b3f4ae3ebda6060eb1a8d779f6dfd4"],
    "check_alwayson_boxes.py": ["--rev", "e78dff667237fba2e3cf9eccb802eff5bc9ea302"],
    "check_callee_rename.py": ["--rev", "c8579a4c5b48789e56fb9060ddd48f33569e1215"],
    "check_opencode_repin.py": ["--rev", "e78dff667237fba2e3cf9eccb802eff5bc9ea302"],
    "check_correction_sweep.py": ["--rev", "c8579a4c5b48789e56fb9060ddd48f33569e1215"],
    "check_gate_registry.py": ["--rev", "422ffd1082b3f4ae3ebda6060eb1a8d779f6dfd4"],
    # The floors gate reads a tree; a child that prints no summary must FAIL it.
    "check_assertion_floors.py": ["--self-test-timeout", "900", "--script",
                                  "overlap_levers=" + "verifiers/zz_stub_nosummary.py"],
    "verify_corpus_independent.py": [],
}
ANCHOR_EXPECT = "1"

# Class N (round-56 erratum): `--root` reads a directory and needs no git, so a
# missing git must not be could-not-evaluate there.  An entry-only preflight
# (world P) exits 2 on the missing git alone and misses these.
NOGIT_ROOT: list[str] = [
    "check_correction_sweep.py",
    "check_mcp_instructions.py",
    "check_description_thresholds.py",
    "check_overlap_levers.py",
]
NOGIT_ROOT_ARGS = ["--root", "."]
NOGIT_ROOT_EXPECT = "0|1"

# Written into the temporary clone so the floors anchor has a red child.
STUB_CHILD = "verifiers/zz_stub_nosummary.py"
STUB_CHILD_BYTES = (b"#!/usr/bin/env python3\n"
                    b'"""Sandbox fixture: a --self-test that prints no summary line."""\n'
                    b"import sys\n"
                    b"\n"
                    b"sys.exit(0)\n")


class EnvError(Exception):
    pass


def plan_runs(gates: dict[str, tuple[list[str], list[list[str]]]],
              anchors: dict[str, list[str]],
              nogit_root: list[str]) -> list[dict]:
    """The frozen run list: per gate, its R probes, one G probe, one red anchor,
    then S and V; then the class-N no-git `--root` verdicts."""
    runs = []
    for gate, (real, rprobes) in gates.items():
        for a in rprobes:
            runs.append({"gate": gate, "kind": "R", "args": a, "expect": "2"})
        runs.append({"gate": gate, "kind": "G", "args": real, "expect": "2"})
        runs.append({"gate": gate, "kind": "A", "args": list(anchors[gate]),
                     "expect": ANCHOR_EXPECT})
        runs.append({"gate": gate, "kind": "S", "args": ["--self-test"], "expect": "0"})
        runs.append({"gate": gate, "kind": "V", "args": real, "expect": "0|1"})
    for gate in nogit_root:
        runs.append({"gate": gate, "kind": "N", "args": list(NOGIT_ROOT_ARGS),
                     "expect": NOGIT_ROOT_EXPECT})
    return runs


def ok(expect: str, code: int | None) -> bool:
    return code is not None and str(code) in expect.split("|")


def tally(runs: list[dict]) -> tuple[int, int, int]:
    honoured = sum(1 for r in runs if r["kind"] in "RGN" and ok(r["expect"], r.get("code")))
    held = 0
    for gate in dict.fromkeys(r["gate"] for r in runs):
        ctl = [r for r in runs if r["gate"] == gate and r["kind"] in "SV"]
        if ctl and all(ok(r["expect"], r.get("code")) for r in ctl):
            held += 1
    anchors = sum(1 for r in runs if r["kind"] == "A" and ok(r["expect"], r.get("code")))
    return honoured, held, anchors


def git(*args: str, cwd: Path | None = None) -> subprocess.CompletedProcess:
    try:
        return subprocess.run(["git", *args], cwd=cwd, capture_output=True, text=True)
    except OSError as e:
        raise EnvError("git not runnable: %s" % e) from e


def run_one(tree: Path, run: dict, rev: str, rand: str, nogit_bin: Path,
            out_dir: Path, seq: int) -> int | None:
    args = [rev if a == REV_TOKEN else rand if a == RAND_TOKEN else a for a in run["args"]]
    env = dict(os.environ)
    for k in ("GIT_DIR", "GIT_WORK_TREE", "GIT_INDEX_FILE"):
        env.pop(k, None)
    env["PYTHONSAFEPATH"] = "1"
    if run["kind"] in "GN":
        env["PATH"] = str(nogit_bin)
    out = err = b""
    try:
        p = subprocess.run([sys.executable, "-B", str(tree / "verifiers" / run["gate"]), *args],
                           cwd=tree, env=env, capture_output=True, timeout=TIMEOUT)
        code, out, err = p.returncode, p.stdout or b"", p.stderr or b""
    except subprocess.TimeoutExpired as e:
        code, out, err = None, e.stdout or b"", e.stderr or b""
    stem = "%02d-%s-%s" % (seq, run["gate"][:-3], run["kind"])
    (out_dir / (stem + ".stdout")).write_bytes(out)
    (out_dir / (stem + ".stderr")).write_bytes(err)
    run["out_files"] = [stem + ".stdout", stem + ".stderr"]
    lines = err.decode("utf-8", "replace").strip().splitlines()
    run["stderr_tail"] = lines[-1][:200] if lines else ""
    return code


def shadow_names(tree: Path) -> list[str]:
    """Names under <tree>/verifiers/ whose stem is a standard-library module.

    Python puts the script's directory first on sys.path, so such a file
    replaces the module in every gate and in this counter (round-55 world S).
    """
    vdir = tree / "verifiers"
    if not vdir.is_dir():
        return []
    return sorted(p.name for p in vdir.glob("*.py") if p.stem in sys.stdlib_module_names)


def measure(rev: str, out_dir: Path) -> tuple[str, list[dict]]:
    r = git("-C", str(LANE), "rev-parse", "--verify", "--quiet", "%s^{commit}" % rev)
    if r.returncode != 0:
        raise EnvError("revision %r is not a commit in %s" % (rev, LANE))
    full = r.stdout.strip()
    runs = plan_runs(GATES, ANCHORS, NOGIT_ROOT)
    with tempfile.TemporaryDirectory(prefix="kotoba-r56-cne-%s-" % os.urandom(4).hex()) as td:
        tree = Path(td) / "lane"
        c = git("clone", "-q", "--no-checkout", str(LANE), str(tree))
        if c.returncode != 0:
            raise EnvError("clone failed: %s" % c.stderr.strip())
        c = git("-C", str(tree), "checkout", "-q", "--detach", full)
        if c.returncode != 0:
            raise EnvError("checkout %s failed: %s" % (full, c.stderr.strip()))
        shadows = shadow_names(tree)
        if shadows:
            raise EnvError("shadow module(s) under verifiers/ at %s: %s"
                           % (full[:12], ", ".join(shadows)))
        stub = tree / STUB_CHILD
        stub.parent.mkdir(parents=True, exist_ok=True)
        stub.write_bytes(STUB_CHILD_BYTES)
        while True:
            rand = os.urandom(20).hex()
            if git("-C", str(tree), "cat-file", "-e", rand).returncode != 0:
                break
        nogit = Path(td) / ("nogit-%s" % os.urandom(4).hex())
        nogit.mkdir()
        (nogit / "python3").symlink_to(sys.executable)
        if shutil.which("git", path=str(nogit)):
            raise EnvError("git found on the no-git PATH")
        for seq, run in enumerate(runs, 1):
            run["code"] = run_one(tree, run, full, rand, nogit, out_dir, seq)
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

    runs = plan_runs(GATES, ANCHORS, NOGIT_ROOT)
    check("frozen probe count", sum(1 for r in runs if r["kind"] in "RGN"), N_PROBES)
    check("frozen gate count", len(GATES), N_GATES)
    check("every gate has S and V",
          all(sum(1 for r in runs if r["gate"] == g and r["kind"] in "SV") == 2 for g in GATES),
          True)
    check("every gate has a red anchor", sorted(ANCHORS), sorted(GATES))
    check("frozen anchor count", sum(1 for r in runs if r["kind"] == "A"), N_ANCHORS)
    check("class-N gates are measured gates", all(g in GATES for g in NOGIT_ROOT), True)

    def world(codes: dict[str, int | None]) -> tuple[int, int, int]:
        rs = plan_runs({"a.py": (["--rev", REV_TOKEN], [["--rev", RAND_TOKEN]]),
                        "b.py": ([], [])},
                       {"a.py": ["--rev", "abc"], "b.py": []}, [])
        for r in rs:
            r["code"] = codes.get("%s:%s" % (r["gate"], r["kind"]))
        return tally(rs)

    good = {"a.py:R": 2, "a.py:G": 2, "a.py:A": 1, "a.py:S": 0, "a.py:V": 1,
            "b.py:G": 2, "b.py:A": 1, "b.py:S": 0, "b.py:V": 0}
    check("all honoured and held", world(good), (3, 2, 2))
    check("probe exiting 1 is not honoured", world({**good, "a.py:R": 1}), (2, 2, 2))
    check("probe timing out is not honoured", world({**good, "b.py:G": None}), (2, 2, 2))
    check("always-2 gate fails its V control", world({**good, "a.py:V": 2}), (3, 1, 2))
    check("red self-test fails the S control", world({**good, "b.py:S": 1}), (3, 1, 2))
    check("self-test exiting 2 fails the S control", world({**good, "a.py:S": 2}), (3, 1, 2))
    check("V exit 0 or 1 both hold", world({**good, "a.py:V": 0}), (3, 2, 2))
    check("exit 3 is not could-not-evaluate here", world({**good, "a.py:G": 3}), (2, 2, 2))
    check("laundered verdict fails its red anchor", world({**good, "a.py:A": 2}), (3, 2, 1))

    nruns = [r for r in plan_runs(GATES, ANCHORS, NOGIT_ROOT) if r["kind"] == "N"]
    check("class-N probe count", len(nruns), len(NOGIT_ROOT))
    for r in nruns:
        r["code"] = 0
    check("class-N verdicts are honoured", sum(1 for r in nruns if ok(r["expect"], r["code"])),
          len(nruns))
    for r in nruns:
        r["code"] = 2
    check("class-N could-not-evaluate is a miss",
          sum(1 for r in nruns if ok(r["expect"], r["code"])), 0)

    with tempfile.TemporaryDirectory(prefix="cne-selftest-") as td:
        vdir = Path(td) / "verifiers"
        vdir.mkdir()
        (vdir / "argparse.py").write_text("")
        (vdir / "check_x.py").write_text("")
        check("shadow scan finds a stdlib-named module", shadow_names(Path(td)), ["argparse.py"])
        check("shadow scan passes a tree without verifiers/",
              shadow_names(Path(td) / "absent"), [])
    check("token substitution", [rev if a == REV_TOKEN else a for a in ["--rev", REV_TOKEN]
                                 for rev in ["abc"]], ["--rev", "abc"])

    print("self-test: %d failure(s) over %d assertions" % (failures, assertions))
    return 1 if failures else 0


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--rev")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--out", metavar="DIR",
                    help="save every run's stdout/stderr under DIR "
                         "(default: a fresh directory under the system temp dir)")
    ap.add_argument("--self-test", action="store_true")
    args = ap.parse_args(argv)
    if args.self_test:
        if args.rev or args.json or args.out:
            ap.error("--self-test cannot be combined with --rev, --json or --out")
        return self_test()
    if not args.rev:
        ap.error("--rev is required")
    out_dir = (Path(args.out).expanduser() if args.out
               else Path(tempfile.mkdtemp(prefix="kotoba-r56-cne-runs-")))
    out_dir.mkdir(parents=True, exist_ok=True)
    try:
        shadows = shadow_names(LANE)
        if shadows:
            raise EnvError("shadow module(s) under verifiers/ in this checkout: %s"
                           % ", ".join(shadows))
        full, runs = measure(args.rev, out_dir)
    except (EnvError, OSError) as e:
        print("could-not-evaluate: %s" % e, file=sys.stderr)
        return 2
    honoured, held, anchors = tally(runs)
    if args.json:
        print(json.dumps({"rev": full, "runs": runs, "honoured": honoured,
                          "probes": N_PROBES, "held": held, "gates": N_GATES,
                          "anchors": anchors, "anchor_total": N_ANCHORS,
                          "out": str(out_dir)}, indent=1))
    else:
        print("measured %s" % full)
        for r in runs:
            mark = "ok" if ok(r["expect"], r["code"]) else "MISS"
            print("%-34s %s expect %-3s got %s %s" % (
                r["gate"], r["kind"], r["expect"], r["code"], mark))
            if mark == "MISS" and r.get("stderr_tail"):
                print("%-34s   stderr: %s" % ("", r["stderr_tail"]))
    print("run outputs saved under %s" % out_dir)
    print("could-not-evaluate probes honoured %d of %d; controls held %d of %d; "
          "red anchors held %d of %d"
          % (honoured, N_PROBES, held, N_GATES, anchors, N_ANCHORS))
    return 0 if honoured == N_PROBES and held == N_GATES and anchors == N_ANCHORS else 1


if __name__ == "__main__":
    sys.exit(main())
