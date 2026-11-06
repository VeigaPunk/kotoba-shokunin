#!/usr/bin/env python3
"""probe_r100.py -- NEW mutants of verifiers/verify_dispatch_prompts.py beyond
every frozen table (round 100, seat MutTesterDispatchR100).

Usage: python3 -B probe_r100.py {base|cand} REV REPO [--only ids] [--seed hex] [--full]

The method is the round-100 counter's (verifiers/fixtures/round-100/selftest-kills.py,
v6.2), imported not re-implemented: RUNNER, classify, code_decoy, NotEvaluated and
DECOY_MARK are loaded from a scratch copy of that counter at REV, then rules 1-9 are
reproduced -- literal single-anchor substitution, source-blind run, mirror run, a fresh
git-less world per run (`git archive` once, `cp -a --reflink=auto` per run), minimal
child env, comment decoy, code decoy, shuffled order with three honest brackets, and
KILLED iff blind AND mirror are both REPORTED-FAILURE.

Every mutant here is NEW: no id, anchor+replacement pair or defect is a row of
CLAIMS["c1"/"r99c1"/"r98c1"/"r97c1"/"r96c1"] of the round-100 counter, and none is
w01-m22 of .ufo/waves/round-99/w1/MutTesterDispatchR99.md.  Anchor adjacencies (a
frozen row uses the same anchor with a different replacement) are disclosed in the
report, never hidden.
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
COUNTER = "verifiers/fixtures/round-100/selftest-kills.py"
PREFIX = "self-test FAIL: "

# id, anchor, replacement, defect.  Every anchor matches exactly once at the
# freeze (03a98eb7) and on the candidate; every replacement keeps the line count.
MUTANTS = [
    # --- main(): the substrate loop over prompts/state/fleet ---------------
    ("w01-substrate-state-fleet-unchecked",
     '    for path, what in ((prompts, "prompts directory"),\n'
     '                       (state_dir, "state directory"),\n'
     '                       (fleet, "fleet root")):',
     '    for path, what in ((prompts, "prompts directory"),\n'
     '                       (prompts, "prompts directory"),\n'
     '                       (prompts, "prompts directory")):',
     "the substrate loop checks the prompts directory three times: a plain "
     "file as --state-dir or --fleet passes the not-a-directory gate"),
    ("w02-substrate-state-what-mislabeled",
     '                       (state_dir, "state directory"),',
     '                       (state_dir, "prompts directory"),',
     "the state-directory substrate error names the prompts directory "
     "(reporting-only)"),
    # --- main(): the --json payloads --------------------------------------
    ("w03-json-success-exitcode-zero",
     '            "exit_code": code,',
     '            "exit_code": 0,',
     "the success --json payload reports exit_code 0 on a run that exits 1"),
    ("w04-json-na-count-zero",
     '            "na": sum(1 for r in results if r["status"] == "N/A"),',
     '            "na": 0,',
     "the success --json payload always reports na 0"),
    ("w05-json-pass-count-zero",
     '            "pass": sum(1 for r in results if r["status"] == "PASS"),',
     '            "pass": 0,',
     "the success --json payload always reports pass 0"),
    ("w06-json-fail-count-zero",
     '            "fail": sum(1 for r in results if r["status"] == "FAIL"),',
     '            "fail": 0,',
     "the success --json payload always reports fail 0"),
    ("w07-enverror-json-exitcode-zero",
     '                       "exit_code": 2, "error": str(exc)})',
     '                       "exit_code": 0, "error": str(exc)})',
     "the EnvError --json payload reports exit_code 0 while main returns 2"),
    ("w08-enverror-json-error-empty",
     '                       "exit_code": 2, "error": str(exc)})',
     '                       "exit_code": 2, "error": ""})',
     "the EnvError --json payload carries an empty error string "
     "(output-only)"),
    # --- read_text(): the decode error mode -------------------------------
    ("w09-readtext-errors-replace",
     '        return path.read_text(encoding="utf-8")',
     '        return path.read_text(encoding="utf-8", errors="replace")',
     "read_text replaces invalid UTF-8 bytes instead of raising "
     "UnicodeDecodeError"),
    # --- run_checks(): a duplicated result --------------------------------
    ("w10-runchecks-duplicate-first",
     "    for cid in wanted:",
     "    for cid in wanted + wanted[:1]:",
     "run_checks returns the first requested check a second time at the end"),
    # --- build_parser(): defaults and choices -----------------------------
    ("w11-parser-state-default-prompts",
     '    ap.add_argument("--state-dir", default=str(DEFAULT_STATE_DIR), metavar="DIR",',
     '    ap.add_argument("--state-dir", default=str(DEFAULT_PROMPTS), metavar="DIR",',
     "a live run without --state-dir reads the prompts directory as state"),
    ("w12-parser-check-choices-dropped",
     '    ap.add_argument("--check", action="append", choices=CHECK_IDS, default=None,',
     '    ap.add_argument("--check", action="append", default=None,',
     "an unknown --check id is accepted and silently runs dispatch.08"),
    # --- main(): the summary exit code and the default check set ----------
    ("w13-main-code-all-not-any",
     '    code = 1 if any(r["status"] == "FAIL" for r in results) else 0',
     '    code = 1 if all(r["status"] == "FAIL" for r in results) else 0',
     "the run exits 1 only when every check FAILs, not when any does"),
    ("w14-main-wanted-empty",
     "    wanted = list(args.check) if args.check else list(CHECK_IDS)",
     "    wanted = list(args.check) if args.check else []",
     "a run with no --check evaluates nothing and exits 0"),
    # --- emit_json(): the serialisation shape -----------------------------
    ("w15-emit-json-sort-keys-off",
     "    print(json.dumps(payload, indent=2, sort_keys=True))",
     "    print(json.dumps(payload, indent=2, sort_keys=False))",
     "the --json payload is not key-sorted (output-only)"),
    # --- main(): the --box-proof default map path -------------------------
    ("w16-parser-map-default-fixtures",
     "            VERIFIERS_DIR / BASELINE_NAME",
     "            FIXTURES_DIR / BASELINE_NAME",
     "the default --box-proof map path points into the fixtures directory"),
]


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_counter(path: Path):
    spec = importlib.util.spec_from_file_location("counter_v62", path)
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
        ("probe-" + args.mode)
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
            print("mutant %-42s blind %-16s mirror %-16s comment %-5s code %-5s: %s"
                  % (name, blind, mirror, comment, code, verdict))
        print("totals: KILLED %d, SURVIVED %d, RUN-ERROR %d"
              % (killed, survived, errors))
        return 0
    finally:
        shutil.rmtree(root, ignore_errors=True)


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
