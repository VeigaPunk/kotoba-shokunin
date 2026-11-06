#!/usr/bin/env python3
"""probe_r98.py -- new mutants of verifiers/verify_dispatch_prompts.py beyond
the frozen tables (MutTesterDispatchR98, round 98).

Usage: probe_r98.py {base|cand} REV REPO [--only id,id,...] [--seed HEX]

Reuses the v6 counter's RUNNER, classify, code_decoy and DECOY_MARK by import
from a scratch copy of verifiers/fixtures/round-98/selftest-kills.py (read at
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

LANE = Path("/home/vgpnk/Projects/shokunin/kotoba-shokunin")
INSTRUMENT = "verifiers/verify_dispatch_prompts.py"
COUNTER = "verifiers/fixtures/round-98/selftest-kills.py"
PREFIX = "self-test FAIL: "

# id, anchor, replacement, defect (all absent from CLAIMS["c1"/"r97c1"/"r96c1"]
# and from MutTesterDispatchR97 m20-m34).
MUTANTS = [
    ("n01-l1-suffix-unanchored",
     'L1_FILE_RE = re.compile(r"^(?P<lane>.+)-L1\\.md$")',
     'L1_FILE_RE = re.compile(r"^(?P<lane>.+)-L1\\.md")',
     "the L1 name regex is not end-anchored: kote-L1.md.bak names a spawn file"),
    ("n02-role-round-above",
     "        elif rr != round_n:",
     "        elif rr < round_n:",
     "a role-line round ABOVE the file-name round passes"),
    ("n03-proof-map-hash-unenforced",
     '        if entry.get("text_sha256") != pinned:',
     '        if entry.get("text_sha256") is None:',
     "the map's text_sha256 pin is not compared with the pinned constant"),
    ("n04-proof-missing-skill-as-pinned",
     "        live = {}",
     "        live = dict(PINNED_BOX_SHA)",
     "an unreadable/missing SKILL.md is treated as hashing to the pins"),
    ("n05-proof-verdict-mismatch-unenforced",
     '            if f["verdict"] != c.get("expect_verdict"):',
     "            if False:",
     "a fixture case whose observed verdict differs from its expected verdict passes"),
    ("n06-proof-conjunct-status-unenforced",
     '                if status != c.get("expect_conjunct_status", "FAIL"):',
     "                if False:",
     "a case's named-conjunct expected status is not compared"),
    ("n07-runchecks-first-check-only",
     "    for cid in wanted:",
     "    for cid in wanted[:1]:",
     "run_checks evaluates only the first requested check"),
    ("n08-main-fail-exit-zero",
     '    code = 1 if any(r["status"] == "FAIL" for r in results) else 0',
     "    code = 0",
     "a FAILing live check exits 0"),
    ("n09-main-check-ignored",
     "    wanted = list(args.check) if args.check else list(CHECK_IDS)",
     "    wanted = list(CHECK_IDS)",
     "--check is ignored: every check always runs"),
    ("n10-readtext-oserror-empty",
     '        raise EnvError("%s: %s (%s)" % (path, exc.strerror or exc, what))',
     '        return ""',
     "an unreadable prompt file reads as empty text instead of a substrate error"),
    ("n11-verdict-of-prefix",
     '        if f["file"] == fname:',
     '        if f["file"].startswith(fname):',
     "the verdict lookup matches a prefix, so a longer name shadows the exact one"),
    ("n12-report-stem-dotdot",
     '        if not stem or stem in (".", ".."):',
     "        if not stem:",
     "a '..' report stem is kept as a report path"),
    ("n13-map-duplicate-first-wins",
     '        entries[e.get("box_id")] = e',
     '        entries.setdefault(e.get("box_id"), e)',
     "a duplicate box entry keeps the FIRST entry instead of the last"),
    ("n14-finish-fails-nas",
     '    if fails:\n        status = "FAIL"',
     '    if fails and not nas:\n        status = "FAIL"',
     "a check with a FAILing file and an N/A file reads N/A, not FAIL"),
    ("n15-outofscope-nonmd-evaluated",
     "        lane, _round, kind = lane_of(name)\n        if lane is None:",
     '        lane, _round, kind = lane_of(name)\n'
     '        if lane is None and name.endswith(".md"):',
     "a non-.md file in the prompts dir is evaluated instead of listed out of scope"),
    ("n16-box-section-ignored",
     "        if not bm or section != DISPATCH_SECTION:",
     "        if not bm:",
     "every checklist box in SKILL.md is hashed, not only the dispatch section"),
    ("n17-proof-case-first-only",
     "        for c in cases:",
     "        for c in cases[:1]:",
     "only the first fixture case per box is evaluated"),
    ("n18-finish-na-count-zero",
     '    nas = [f for f in files if f["verdict"] == "N/A"]',
     "    nas = []",
     "the detail counts N/A files as PASS and reports zero N/A (reporting-only)"),
    ("n19-state-baseline-exists",
     "    if base.is_file():",
     "    if base.exists():",
     "a DIRECTORY named <lane>.report-baseline counts as a baseline file"),
    ("n20-box-ninth-limit",
     "        if len(out) < len(BOX_ORDER):",
     "        if True:",
     "the nine-box cap is dropped (a tenth dispatch box raises IndexError)"),
]


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def git(*args: str, cwd: Path | None = None) -> subprocess.CompletedProcess:
    return subprocess.run(["git", *args], cwd=cwd, stdout=subprocess.PIPE,
                          stderr=subprocess.PIPE)


def load_counter(path: Path):
    spec = importlib.util.spec_from_file_location("counter_v6", path)
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
        "kotoba-r98" / "MutTesterDispatchR98" / ("probe-" + args.mode)
    work.mkdir(parents=True, exist_ok=True)
    root = Path(tempfile.mkdtemp(prefix="run.", dir=work))
    try:
        shown = git("-C", str(repo), "show", "%s:%s" % (args.rev, COUNTER))
        if shown.returncode != 0:
            print("NOT-EVALUATED: counter absent at %s" % args.rev)
            return 2
        cpath = root / "counter.py"
        cpath.write_bytes(shown.stdout)
        counter = load_counter(cpath)
        shown = git("-C", str(repo), "show", "%s:%s" % (args.rev, INSTRUMENT))
        if shown.returncode != 0:
            print("NOT-EVALUATED: instrument absent at %s" % args.rev)
            return 2
        original = shown.stdout.decode("utf-8")
        inst_sha = hashlib.sha256(shown.stdout).hexdigest()
        print("probe %s rev %s repo %s instrument sha256 %s counter sha256 %s"
              % (args.mode, args.rev, repo, inst_sha, sha(cpath)))
        print("honest assertions: pending; mutant table: %d" % len(MUTANTS))

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
                print("NOT-EVALUATED: %s %s does not compile: %s" % (kind, name, exc))
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
        print("totals: KILLED %d, SURVIVED %d, RUN-ERROR %d" % (killed, survived, errors))
        return 0
    finally:
        shutil.rmtree(root, ignore_errors=True)


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
