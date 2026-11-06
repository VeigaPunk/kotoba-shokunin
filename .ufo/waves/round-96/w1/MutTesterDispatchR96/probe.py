#!/usr/bin/env python3
"""MutTesterDispatchR96 probe driver (round 96, wave r96-w1; NOT a lane file).

Measures a table of NEW mutants of verifiers/verify_dispatch_prompts.py at a given
revision, using the frozen counter's own machinery (imported read-only from
verifiers/fixtures/round-96/selftest-kills.py): literal single-anchor substitution,
mutant text compiled with the instrument's path and executed as __main__ while the
file on disk holds the honest bytes (source-blind), the counter's comment decoy and
code decoy, and the counter's outcome classifier.

Usage: python3 -B probe.py LABEL REV REPO
Exit 0 measurement completed, 2 could-not-evaluate. Never edits the lane.
"""
from __future__ import annotations

import hashlib
import importlib.util
import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

COUNTER = Path("/home/vgpnk/Projects/shokunin/kotoba-shokunin/verifiers/fixtures/round-96/selftest-kills.py")
INSTRUMENT = "verifiers/verify_dispatch_prompts.py"
PREFIX = "self-test FAIL: "

# (id, anchor, replacement, class, note)
MUTANTS = [
    ("m01-rstrip-dot", 'stem = m.group(2).rstrip(".,;:")',
     'stem = m.group(2).rstrip(",;:")', "sentence-final-dot",
     "a report path followed by a sentence period keeps the '.' in its stem"),
    ("m02-empty-baseline", 'return "none", None, "empty %s" % base',
     'return "baseline", 10 ** 9, "empty %s" % base', "empty-baseline",
     "an empty baseline file reads as an unbounded bound instead of N/A"),
    ("m03-fleetroot-stem-pass",
     '"status": "N/A",\n                "detail": "out of scope: fleet-root role',
     '"status": "PASS",\n                "detail": "out of scope: fleet-root role',
     "fleetroot-stem", "a fleet-root role's report_stem_is_lane_id reads PASS, not N/A"),
    ("m04-fleetroot-no-baseline",
     '(state_dir / ("%s.report-baseline" % lane)).is_file():', "False:",
     "fleetroot-identity",
     "a lane known only by its .report-baseline state file is no longer a known lane"),
    ("m05-placeholder-empty-angle", 'PLACEHOLDER_RE = re.compile(r"<[^<>]*>")',
     'PLACEHOLDER_RE = re.compile(r"<[^<>]+>")', "placeholder-re",
     "an empty '<>' in a report path is no longer a placeholder"),
    ("m06-sibling-file-as-lane", 'if (fleet / ("%s-shokunin" % lane)).is_dir():',
     'if (fleet / ("%s-shokunin" % lane)).exists():', "lane-kind",
     "a plain file named <lane>-shokunin counts as a lane repository"),
    ("m07-report-regex-noprefix",
     'REPORT_PATH_RE = re.compile(r"\\.ufo/reports/round-(\\d+)/',
     'REPORT_PATH_RE = re.compile(r"\\.ufo/reports/(?:round-)?(\\d+)/',
     "report-path-regex", "a report dir without the 'round-' prefix is accepted"),
    ("m08-role-regex-nospace", 'ROLE_ROUND_RE = re.compile(r"\\bround\\s+(\\d+)\\b")',
     'ROLE_ROUND_RE = re.compile(r"\\bround\\s*(\\d+)\\b")', "role-line-regex",
     "'round7' (no space) is read as the role round"),
    ("m09-outofscope-reason",
     '"reason": "conjunct report_stem_is_lane_id does not apply: "',
     '"reason": "conjunct report_stem_is_lane_id does not apply to a fleet-root role: "',
     "out-of-scope-reason", "the fleet-root out-of-scope reason text changes"),
    ("m10-file-note-dropped", "if note:", "if False:", "_file_result-note",
     "the per-file 'note' (e.g. 'no report path found') is never attached"),
    ("m11-evaluated-pass-only", "evaluated = len(files)",
     'evaluated = len([f for f in files if f["verdict"] == "PASS"])', "evaluated-count",
     "a FAILing or N/A file is not counted as evaluated"),
    ("m12-unreadable-as-baseline",
     'return "none", None, "unreadable %s (%s)" % (base, exc.strerror or exc)',
     'return "baseline", 10 ** 9, "unreadable %s (%s)" % (base, exc.strerror or exc)',
     "unreadable-baseline", "an unreadable baseline file reads as an unbounded bound"),
    ("m13-lane-kind-legacy-dropped", '(state_dir / ("%s.round" % lane)).is_file()',
     "False", "lane-kind-legacy",
     "a lane known only by its legacy .round file is no longer a known lane"),
    ("m14-finish-single-fail-na", '    if fails:\n        status = "FAIL"',
     '    if len(fails) > 1:\n        status = "FAIL"', "_finish-status",
     "a check with exactly one failing file reads N/A instead of FAIL"),
    ("m15-has-placeholder-redundant",
     "if has_placeholder(s) or has_placeholder(",
     "if has_placeholder(s) or False and has_placeholder(", "placeholder-redundant",
     "the second has_placeholder (full path) conjunct is dropped"),
    ("m16-dotdot-skip", 'if not stem or stem in (".", ".."):', "if not stem:",
     "stem-skip", "the '.'/'..' stem skip is removed"),
    ("m17-l1-in-08-scope", 'if kind != "round":', 'if kind != "l1":', "scope-control",
     "L1 files become in scope for dispatch.08 and round files out of scope"),
    ("m18-state-last-field", "first = raw.split()[:1]", "first = raw.split()[-1:]",
     "baseline-field", "the baseline round is read from the last field, not the first"),
    ("m19-file-first-conjunct-only",
     'statuses = [v["status"] for v in verdicts.values()]',
     'statuses = [v["status"] for v in verdicts.values()][:1]', "_file_result-precedence",
     "only the first conjunct decides the file verdict"),
]


def load_counter():
    spec = importlib.util.spec_from_file_location("frozen_counter_r96", COUNTER)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def sha(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def main(argv: list[str]) -> int:
    if len(argv) != 3:
        print("usage: probe.py LABEL REV REPO", file=sys.stderr)
        return 2
    label, rev, repo = argv
    c = load_counter()
    got = subprocess.run(["git", "-C", repo, "rev-parse", "--verify", "-q", rev + "^{commit}"],
                         stdout=subprocess.PIPE, stderr=subprocess.DEVNULL)
    if got.returncode != 0:
        print("PROBE-NOT-EVALUATED: REV %s is not a commit of %s" % (rev, repo))
        return 2
    rev = got.stdout.decode().strip()
    root = Path(os.environ.get("HYAKU_SCRATCH", "/fast/scratch/hyaku")) / "kotoba-r96" / "probe"
    root.mkdir(parents=True, exist_ok=True)
    work = Path(tempfile.mkdtemp(prefix="%s." % label, dir=root))
    try:
        env = dict(os.environ, TMPDIR=str(work / "tmp"), PYTHONDONTWRITEBYTECODE="1")
        (work / "tmp").mkdir()
        clone = work / "world" / "kotoba-shokunin"
        clone.parent.mkdir()
        for cmd in (["git", "clone", "-q", "--shared", repo, str(clone)],
                    ["git", "-C", str(clone), "checkout", "-q", rev]):
            if subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL).returncode != 0:
                print("PROBE-NOT-EVALUATED: clone or checkout failed")
                return 2
        path = clone / INSTRUMENT
        original = path.read_text(encoding="utf-8")
        before = sha(original)
        print("probe %s rev %s repo %s instrument %s sha256 %s" % (label, rev, repo, INSTRUMENT, before))
        src = work / "src.py"

        def run_text(text: str, what: str) -> tuple[int, str, str]:
            try:
                compile(text, str(path), "exec", dont_inherit=True)
            except SyntaxError as exc:
                return -1, "does not compile: %s" % exc, "NOT-COMPILED"
            path.write_text(original, encoding="utf-8")
            try:
                rc, out = c.run_selftest(clone, INSTRUMENT, env, text, src)
            finally:
                path.write_text(original, encoding="utf-8")
            return rc, out, c.classify(rc, out, PREFIX)

        rc, out, cls = run_text(original, "honest")
        print("honest rc %d %s: %s" % (rc, cls, c.last_line(out)))
        honest_clean = cls == "CLEAN"
        rows = []
        for mid, anchor, repl, klass, note in MUTANTS:
            n = original.count(anchor)
            if n != 1:
                print("mutant %s ANCHOR-MISS (%d match(es)) [%s]" % (mid, n, klass))
                rows.append((mid, klass, "ANCHOR-MISS", -1, ""))
                continue
            mutated = original.replace(anchor, repl)
            rc, out, cls = run_text(mutated, mid)
            verdict = {"REPORTED-FAILURE": "KILLED", "RUN-ERROR": "RUN-ERROR",
                       "CLEAN": "SURVIVED", "NOT-COMPILED": "RUN-ERROR"}.get(cls, cls)
            print("mutant %s rc %d %s [%s]: %s" % (mid, rc, verdict, klass, c.last_line(out)))
            for ln in out.splitlines():
                if ln.startswith(PREFIX):
                    print("  | %s" % ln)
            # comment decoy / code decoy (counter rule 2): the guard must hold
            ctext = original.rstrip("\n") + "\n" + "".join("# r96-decoy " + ln + "\n" for ln in repl.splitlines())
            crc, cout, ccls = run_text(ctext, "comment decoy " + mid)
            print("comment decoy %s rc %d %s: %s" % (mid, crc, "HELD" if ccls == "CLEAN" else ccls, c.last_line(cout)))
            try:
                dtext = c.code_decoy(original, mutated, mid)
                drc, dout, dcls = run_text(dtext, "code decoy " + mid)
                print("code decoy %s rc %d %s: %s" % (mid, drc, "HELD" if dcls == "CLEAN" else dcls, c.last_line(dout)))
                decoy = dcls == "CLEAN"
            except c.NotEvaluated as exc:
                print("code decoy %s NOT-EVALUATED: %s" % (mid, exc))
                decoy = None
            rows.append((mid, klass, verdict, rc, "comment=%s code=%s" % (
                "HELD" if ccls == "CLEAN" else ccls, "HELD" if decoy else decoy)))
        after = sha(path.read_text(encoding="utf-8"))
        print("restored %s instrument sha256 %s (%s)" % (
            "OK" if after == before else "MISMATCH", after, "identical" if after == before else "DIFFERS"))
        print("--- summary %s ---" % label)
        for mid, klass, verdict, rc, decoys in rows:
            print("%-32s %-24s %-12s %s" % (mid, klass, verdict, decoys))
        counts = {}
        for _m, _k, v, _r, _d in rows:
            counts[v] = counts.get(v, 0) + 1
        print("honest %s; totals %s" % ("CLEAN" if honest_clean else "NOT-CLEAN",
                                        ", ".join("%s %d" % (k, counts[k]) for k in sorted(counts))))
        return 0 if honest_clean else 2
    finally:
        shutil.rmtree(work, ignore_errors=True)


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
