#!/usr/bin/env python3
"""probe_r99.py -- NEW mutants of verifiers/verify_dispatch_prompts.py beyond
the frozen tables (MutTesterDispatchR99, round 99).

Usage: probe_r99.py {base|cand} REV REPO [--only id,id,...] [--seed HEX] [--full]

Reuses the v6.1 counter's RUNNER, classify, code_decoy and DECOY_MARK by import
from a scratch copy of verifiers/fixtures/round-99/selftest-kills.py (read at
REV), and reproduces its rules 1-9: literal single-anchor substitution with the
line count preserved, source-blind and mirror runs, comment and code decoys,
one git-less world copy per run (git archive + cp -a --reflink=auto), the
minimal child environment, and a shuffled order bracketed by honest runs.

Measurement only: no lane write, no gate.
"""
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import os
import random
import shutil
import subprocess
import sys
import tarfile
import tempfile
from pathlib import Path

INSTRUMENT = "verifiers/verify_dispatch_prompts.py"
COUNTER = "verifiers/fixtures/round-99/selftest-kills.py"
PREFIX = "self-test FAIL: "

# id, anchor, replacement, defect.  Every anchor matches exactly once at the
# freeze and on the candidate; every replacement keeps the line count.  None of
# these ids, anchors or defects is a row of CLAIMS["c1"/"r98c1"/"r97c1"/"r96c1"]
# of verifiers/fixtures/round-99/selftest-kills.py or of n01-n20 in
# .ufo/waves/round-98/w1/MutTesterDispatchR98.md.  Two anchor adjacencies are
# disclosed in the report: m06 shares c1 t06's anchor with a different
# replacement, m10 shares n17's loop with a different slice.
MUTANTS = [
    # --- main(): the exit-2 ladder and argument handling -------------------
    ("m01-main-notdir-exit-zero",
     '                print("ERROR %s: not a directory (%s)" % (path, what),\n'
     '                      file=sys.stderr)\n'
     '            return 2',
     '                print("ERROR %s: not a directory (%s)" % (path, what),\n'
     '                      file=sys.stderr)\n'
     '            return 0',
     "a missing prompts/state/fleet directory exits 0 instead of 2"),
    ("m02-main-env-error-exit-one",
     '        else:\n'
     '            print("ERROR %s" % exc, file=sys.stderr)\n'
     '        return 2',
     '        else:\n'
     '            print("ERROR %s" % exc, file=sys.stderr)\n'
     '        return 1',
     "a substrate EnvError during the live run exits 1 (content fail), not 2"),
    ("m03-main-json-exitcode-zero",
     '                emit_json({"checks": [], "pass": 0, "fail": 0, "na": 0,\n'
     '                           "exit_code": 2,\n'
     '                           "error": "%s: not a directory (%s)" % (path, what)})',
     '                emit_json({"checks": [], "pass": 0, "fail": 0, "na": 0,\n'
     '                           "exit_code": 0,\n'
     '                           "error": "%s: not a directory (%s)" % (path, what)})',
     "the --json substrate-error payload reports exit_code 0 while returning 2"),
    ("m04-main-argv-ignored",
     "    args = build_parser().parse_args(argv)",
     "    args = build_parser().parse_args([])",
     "main() ignores its argv parameter and parses an empty command line"),
    ("m05-check-flag-not-repeatable",
     '    ap.add_argument("--check", action="append", choices=CHECK_IDS, default=None,',
     '    ap.add_argument("--check", action="store", choices=CHECK_IDS, default=None,',
     "the repeatable --check flag keeps only its last value (args.check is a str)"),
    ("m22-main-dir-check-exists",
     "        if not path.is_dir():",
     "        if not path.exists():",
     "a plain file passes the substrate check as if it were a directory"),
    # --- run_checks(): result order and the check mapping ------------------
    ("m06-runchecks-reversed",
     "    for cid in wanted:",
     "    for cid in reversed(wanted):",
     "run_checks returns its results in reverse request order"),
    ("m07-runchecks-else-04",
     "            results.append(evaluate_dispatch_08(prompts, state_dir, fleet))",
     "            results.append(evaluate_dispatch_04(prompts, state_dir, fleet))",
     "run_checks evaluates dispatch.04 for every check id, never dispatch.08"),
    # --- read_text(): the decode path and the substrate message -----------
    ("m08-readtext-latin1",
     '        return path.read_text(encoding="utf-8")',
     '        return path.read_text(encoding="latin-1")',
     "read_text decodes every prompt as latin-1 (mojibake, no decode error)"),
    ("m09-readtext-what-dropped",
     '        raise EnvError("%s: %s (%s)" % (path, exc.strerror or exc, what))',
     '        raise EnvError("%s: %s" % (path, exc.strerror or exc))',
     "the substrate error message drops the 'what' argument (reporting-only)"),
    # --- box_proof(): case/file bookkeeping -------------------------------
    ("m10-proof-cases-last-dropped",
     "        for c in cases:",
     "        for c in cases[:-1]:",
     "box_proof skips the last fixture case of every box"),
    ("m11-proof-na-arm-dropped",
     "        if NA_ARM_CONJUNCT in CONJUNCTS.get(cid, ()) and not na_ok:",
     "        if False:",
     "box_proof no longer requires the N/A-arm case for dispatch.08"),
    ("m12-proof-control-dropped",
     "        if not control_ok:",
     "        if False:",
     "box_proof no longer requires an all-PASS control case"),
    ("m13-proof-substrate-exit-one",
     "    if substrate_error:\n        return 2",
     "    if substrate_error:\n        return 1",
     "a fixture substrate error exits 1 (failed proof), not 2"),
    ("m14-proof-proven-threshold",
     "    return 0 if proven == 2 else 1",
     "    return 0 if proven >= 1 else 1",
     "one proven box is enough for exit 0"),
    ("m15-proof-conjunct-first-only",
     "        for n in CONJUNCTS.get(cid, ()):",
     "        for n in CONJUNCTS.get(cid, ())[:1]:",
     "only the first named conjunct per box must be covered"),
    ("m16-proof-cofail-widened",
     "            allowed = ALLOWED_CO_FAIL.get(n, frozenset())",
     "            allowed = frozenset(CONJUNCTS.get(cid, ()))",
     "the isolation rule is dropped: a case failing two conjuncts covers both"),
    # --- the name and report regex groups --------------------------------
    ("m17-lane-of-kind-swap",
     '        return m.group("lane"), int(m.group("round")), "round"',
     '        return m.group("lane"), int(m.group("round")), "l1"',
     "lane_of labels every round file as an L1 spawn file"),
    ("m18-report-stem-truncated",
     'REPORT_PATH_RE = re.compile(r"\\.ufo/reports/round-(\\d+)/([^\\s`\'\\"()\\[\\]]+)")',
     'REPORT_PATH_RE = re.compile(r"\\.ufo/reports/round-(\\d+)/([^\\s`\'\\"()\\[\\]]{1,3})")',
     "the report-stem group is capped at three characters"),
    ("m19-l1-lane-nongreedy",
     'L1_FILE_RE = re.compile(r"^(?P<lane>.+)-L1\\.md$")',
     'L1_FILE_RE = re.compile(r"^(?P<lane>.+?)-L1\\.md$")',
     "the L1 lane group is non-greedy: 'a-L1-L1.md' names lane 'a'"),
    # --- per-file verdict and box hashing --------------------------------
    ("m20-file-result-last-conjunct-ignored",
     '    if "FAIL" in statuses:',
     '    if "FAIL" in statuses[:-1]:',
     "a FAIL on the last conjunct no longer makes the file FAIL"),
    ("m21-box-fenced-continuation",
     "            if not line.strip() or j + 1 in opaque:",
     "            if not line.strip():",
     "a fenced line inside a box's continuation is hashed into the box text"),
]


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_counter(path: Path):
    spec = importlib.util.spec_from_file_location("counter_v61", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def child_env(d: Path) -> dict:
    return {"PATH": os.environ.get("PATH", "/usr/bin:/bin"), "LANG": "C.UTF-8",
            "TMPDIR": str(d / "tmp"), "HOME": str(d / "home"),
            "XDG_CACHE_HOME": str(d / "cache"),
            "PYTHONDONTWRITEBYTECODE": "1"}


def main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("mode", choices=("base", "cand"))
    ap.add_argument("rev")
    ap.add_argument("repo")
    ap.add_argument("--only", default="")
    ap.add_argument("--seed", default="")
    ap.add_argument("--full", action="store_true",
                    help="print the first self-test FAIL lines of each run")
    args = ap.parse_args(argv)
    repo = Path(args.repo).resolve()
    only = {s for s in args.only.split(",") if s}
    work = Path(os.environ.get("HYAKU_SCRATCH", "/fast/scratch/hyaku")) / \
        "kotoba-r99" / "MutTesterDispatchR99" / ("probe-" + args.mode)
    work.mkdir(parents=True, exist_ok=True)
    root = Path(tempfile.mkdtemp(prefix="run.", dir=work))
    try:
        shown = subprocess.run(["git", "-C", str(repo), "show",
                                "%s:%s" % (args.rev, COUNTER)],
                               stdout=subprocess.PIPE, stderr=subprocess.DEVNULL)
        if shown.returncode != 0:
            print("NOT-EVALUATED: counter absent at %s" % args.rev)
            return 2
        cpath = root / "counter.py"
        cpath.write_bytes(shown.stdout)
        counter = load_counter(cpath)
        shown = subprocess.run(["git", "-C", str(repo), "show",
                                "%s:%s" % (args.rev, INSTRUMENT)],
                               stdout=subprocess.PIPE, stderr=subprocess.DEVNULL)
        if shown.returncode != 0:
            print("NOT-EVALUATED: instrument absent at %s" % args.rev)
            return 2
        original = shown.stdout.decode("utf-8")
        inst_sha = hashlib.sha256(shown.stdout).hexdigest()
        print("probe %s rev %s repo %s instrument sha256 %s counter sha256 %s"
              % (args.mode, args.rev, repo, inst_sha, sha(cpath)))
        print("mutant table: %d" % len(MUTANTS))

        # rule 8: one git-less export of REV, copied per run
        pristine = root / "pristine"
        pristine.mkdir()
        arch = subprocess.Popen(["git", "-C", str(repo), "archive",
                                 "--format=tar", args.rev],
                                stdout=subprocess.PIPE, stderr=subprocess.DEVNULL)
        with tarfile.open(fileobj=arch.stdout, mode="r|") as tf:
            tf.extractall(pristine, filter="tar")
        if arch.wait() != 0:
            print("NOT-EVALUATED: git archive failed")
            return 2
        if (pristine / ".git").exists():
            print("NOT-EVALUATED: exported tree carries .git")
            return 2

        jobs = []  # (kind, name, text_executed, text_on_disk)
        anchors_ok = 0
        for name, anchor, repl, _defect in MUTANTS:
            if only and name not in only:
                continue
            found = original.count(anchor)
            if found != 1:
                print("NOT-EVALUATED: anchor %s matches %d time(s)" % (name, found))
                return 2
            mt = original.replace(anchor, repl)
            if len(mt.splitlines()) != len(original.splitlines()):
                print("NOT-EVALUATED: %s changes the line count" % name)
                return 2
            anchors_ok += 1
            jobs.append(("blind", name, mt, original))
            jobs.append(("mirror", name, mt, mt))
            ct = original.rstrip("\n") + "\n" + "".join(
                counter.DECOY_MARK + ln + "\n" for ln in repl.splitlines())
            jobs.append(("comment", name, ct, ct))
            try:
                dt = counter.code_decoy(original, mt, name)
            except counter.NotEvaluated as exc:
                print("NOT-EVALUATED: code decoy %s: %s" % (name, exc))
                return 2
            jobs.append(("code", name, dt, dt))
        print("anchors: %d of %d match exactly once, line counts preserved"
              % (anchors_ok, len(MUTANTS) if not only else len(only)))
        for kind, name, text, _ in jobs:
            try:
                compile(text, INSTRUMENT, "exec", dont_inherit=True)
            except SyntaxError as exc:
                print("NOT-EVALUATED: %s %s does not compile: %s"
                      % (kind, name, exc))
                return 2

        honest = ("honest", "honest", original, original)
        seed = args.seed or os.urandom(8).hex()
        rng = random.Random(seed)
        rng.shuffle(jobs)
        jobs.insert(rng.randrange(1, len(jobs)), honest)
        jobs = [honest] + jobs + [honest]
        print("seed %s" % seed)

        def fresh_world(tag: str):
            d = Path(tempfile.mkdtemp(prefix=tag + ".", dir=root))
            clone = d / "world" / "kotoba-shokunin"
            clone.parent.mkdir()
            for sub in ("tmp", "home", "cache"):
                (d / sub).mkdir()
            r = subprocess.run(["cp", "-a", "--reflink=auto", str(pristine),
                                str(clone)], stdout=subprocess.DEVNULL,
                               stderr=subprocess.DEVNULL)
            if r.returncode != 0:
                raise RuntimeError("world copy failed")
            return d, clone, child_env(d)

        results: dict[tuple[str, str], list[str]] = {}
        for idx, (kind, name, text, on_disk) in enumerate(jobs):
            d, clone, env = fresh_world("r%03d" % idx)
            path = clone / INSTRUMENT
            path.write_text(on_disk, encoding="utf-8")
            src = d / "src.py"
            src.write_text(text, encoding="utf-8")
            rc = -1
            out = ""
            try:
                proc = subprocess.run(
                    [sys.executable, "-B", "-c", counter.RUNNER, str(path), str(src)],
                    cwd=clone, env=env, stdout=subprocess.PIPE,
                    stderr=subprocess.STDOUT, timeout=600)
                rc = proc.returncode
                out = proc.stdout.decode("utf-8", "replace")
                cls = counter.classify(rc, out, PREFIX)
                last = counter.last_line(out)
            except subprocess.TimeoutExpired:
                cls, last = "RUN-ERROR", "timeout after 600s"
            finally:
                shutil.rmtree(d, ignore_errors=True)
            results.setdefault((kind, name), []).append(cls)
            print("run %03d %s %s rc %d %s: %s"
                  % (idx, kind, name, rc, cls, last))
            if args.full and cls == "REPORTED-FAILURE":
                fails = [ln for ln in out.splitlines()
                         if ln.startswith(PREFIX)][:4]
                for ln in fails:
                    print("    %s" % ln)

        honest_runs = results[("honest", "honest")]
        clean = sum(1 for c in honest_runs if c == "CLEAN")
        print("honest runs CLEAN %d of %d" % (clean, len(honest_runs)))
        if clean != len(honest_runs):
            print("INCONCLUSIVE: baseline is not CLEAN")
            return 2
        rf = "REPORTED-FAILURE"
        killed = survived = errors = 0
        for name, _a, _r, _d in MUTANTS:
            if only and name not in only:
                continue
            blind = results[("blind", name)][0]
            mirror = results[("mirror", name)][0]
            comment = results[("comment", name)][0]
            code = results[("code", name)][0]
            if blind == rf and mirror == rf:
                verdict = "KILLED"
                killed += 1
            elif "RUN-ERROR" in (blind, mirror):
                verdict = "RUN-ERROR"
                errors += 1
            else:
                verdict = "SURVIVED"
                survived += 1
            print("mutant %-40s blind %-16s mirror %-16s comment %-5s code %-5s: %s"
                  % (name, blind, mirror, comment, code, verdict))
        print("totals: KILLED %d, SURVIVED %d, RUN-ERROR %d"
              % (killed, survived, errors))
        return 0
    finally:
        shutil.rmtree(root, ignore_errors=True)


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
