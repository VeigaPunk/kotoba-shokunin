#!/usr/bin/env python3
"""selftest-kills v5 (round 97, claims C1 and C2, frozen counting command; plans/round-97.md).

Usage: python3 -B verifiers/fixtures/round-97/selftest-kills.py {c1|r96c1|r95c1} [REV] [REPO] [--rules v4|v5]
  REV      full commit to measure (default: the tip of branch master of REPO)
  REPO     repository to clone REV from (default: this lane; a scratch repo for a candidate or forgery)
  --rules  v5 (default) or v4 (the round-96 rules, kept to show which rule refuses what)

Successor of verifiers/fixtures/round-96/selftest-kills.py (v4, unchanged there). Rules 1-3 are the
v4 rules unchanged in meaning (the decoy marker is `# r97-decoy`):

1. Outcome classes. REPORTED-FAILURE = exit 1 AND the last summary line
   `<N> failure(s) over <M> assertions` has N >= 1 AND at least one line starts with the claim's
   failure prefix; CLEAN = exit 0 AND the last summary has N == 0; RUN-ERROR = anything else. A
   RUN-ERROR is never a kill. A timeout (600 s) or a mutant that does not compile is
   could-not-evaluate (exit 2).
2. Two decoys per target: the comment decoy (replacement lines appended as `# r97-decoy` comments)
   and the code decoy (every statement the mutant changes inserted, mutated, under
   `if __name__ == "__decoy__":` before the original; an `elif` arm climbs to its if-chain). A decoy
   HOLDS iff CLEAN. Each decoy runs with its own text on disk.
3. Source-blind runs: a mutant's text is compiled with the instrument's path as filename and
   executed as `__main__` (argv `[path, --self-test]`) while the file on disk holds the UNMODIFIED
   bytes.

v5 adds (round-96 addendum A3/A4; ExecCounterForgeryR96 F1/F2):

4. Isolation. Every run gets a fresh clone of REV, a fresh TMPDIR, HOME and XDG_CACHE_HOME, all
   removed after the run; nothing a run writes inside them reaches a later run.
5. Mirror run. Each target and the positive also run with the mutant text ON DISK. A mutant is
   KILLED iff its source-blind run AND its mirror run are both REPORTED-FAILURE.
6. Honest bracket and shuffled order. The unmodified self-test runs three times: first, last, and at
   a random interior position; every other run is in a random order (seed from os.urandom, printed;
   env KOTOBA_R97_SEED replays an order). Honest is CLEAN iff all three honest runs are CLEAN.
7. Exit ladder. An instrument that is absent or not valid UTF-8 at REV, a failed clone, an anchor
   miss, a non-compiling text or a timeout is could-not-evaluate (exit 2), never exit 1.

--rules v4 runs rules 1-3 only, as the v4 counter did: one shared clone and TMPDIR for every run,
the honest run first and only once, no mirror run, fixed order, and the v4 comment-decoy marker
`# r96-decoy ` (so a world keyed on the round-96 marker reads as it did under v4).

Disclosed bounds (stated, not claimed): a sniffer of its own compiled code objects that also proves
the decoy guard dead (round-96 g2b) is not caught by any rule here; state kept outside the per-run
directories (for example /dev/shm, /var/tmp or the source repository's object store) survives
isolation, and only the honest bracket (rule 6) stands against a stateful forger that uses it.

Mutant tables (frozen):
  c1 — verifiers/verify_dispatch_prompts.py, prefix `self-test FAIL: ` — round-97 targets: the
       non-equivalent survivors of the landed round-96 self-test (MutTesterDispatchR96 m01-m08,
       m10, m12-m14; round-96 recon sweep m-noreport-08-pass); anchors from those probes.
    target t01-rstrip-dot              : a sentence-final `.` stays in a report stem
    target t02-empty-baseline          : an empty baseline reads as an unbounded bound
    target t03-fleetroot-stem-pass     : a fleet-root role's report_stem_is_lane_id reads PASS
    target t04-fleetroot-no-baseline   : a lane known only by `<lane>.report-baseline` is unknown
    target t05-placeholder-empty-angle : an empty `<>` is not a placeholder
    target t06-sibling-file-as-lane    : a plain FILE `<lane>-shokunin` counts as a lane repository
    target t07-report-regex-noprefix   : a report dir without `round-` is accepted
    target t08-role-regex-nospace      : `round7` is read as the role round
    target t09-file-note-dropped       : the per-file note is never attached
    target t10-unreadable-as-baseline  : an unreadable baseline reads as an unbounded bound
    target t11-lane-kind-legacy-dropped: a lane known only by legacy `<lane>.round` is unknown
    target t12-finish-single-fail-na   : a check with exactly one failing file does not read FAIL
    target t13-noreport-08-pass        : a file with no report path reads PASS on dispatch.08
    positive p00-md-not-stripped       : the `.md` suffix is not stripped (killed at the base)
  r96c1 — the round-96 c1 table, unchanged (t01-var-dropped .. t11-noreport-04-pass, positive
       p00-md-not-stripped): positive control and the table of the round-96 forgery worlds.
  r95c1 — the round-95 table on verifiers/check_mutation_battery.py, prefix `FAIL ` (positive control).

Predicate (frozen; the same sentence in plans/round-97.md):
  <C>-PREDICATE-MET iff (honest) every honest run is CLEAN; (targets) every target mutant applies
  and is KILLED; (positive) the positive mutant applies and is KILLED; (guard) every target's
  comment decoy and code decoy HOLDS.
Output: one line per run, then
  `<C> targets killed K of N (run errors E); positive killed P of 1; honest <class>;
   comment decoys held D of N; code decoys held X of N`
  `rules <v>: honest runs CLEAN H of R; mirror runs reported M of N+1; seed <hex>`
  and `<C>-PREDICATE-MET` / `<C>-PREDICATE-UNMET` / `<C>-NOT-EVALUATED`.
Exit 0 met, 1 unmet, 2 could-not-evaluate.
Scratch under ${HYAKU_SCRATCH:-/fast/scratch/hyaku}/kotoba-r97/selftest-kills, removed on exit.
"""
from __future__ import annotations

import ast
import os
import random
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

TIMEOUT_S = 600
DP = "verifiers/verify_dispatch_prompts.py"
MB = "verifiers/check_mutation_battery.py"
MB_PIN = 'return n == want, "observed'
VAR_RE = 'VARIABLE_RE = re.compile(r"\\$\\{[^}]*\\}|\\$[A-Za-z_][A-Za-z0-9_]*")'
DECOY_MARK = "# r97-decoy "
DECOY_MARK_V4 = "# r96-decoy "
P00 = ("p00-md-not-stripped", "stem = stem[:-3]", 1, "stem = stem[:]")

CLAIMS = {
    "c1": {
        "instrument": DP,
        "fail_prefix": "self-test FAIL: ",
        "targets": [
            ("t01-rstrip-dot", 'stem = m.group(2).rstrip(".,;:")', 1,
             'stem = m.group(2).rstrip(",;:")'),
            ("t02-empty-baseline", 'return "none", None, "empty %s" % base', 1,
             'return "baseline", 10 ** 9, "empty %s" % base'),
            ("t03-fleetroot-stem-pass",
             '"status": "N/A",\n                "detail": "out of scope: fleet-root role', 1,
             '"status": "PASS",\n                "detail": "out of scope: fleet-root role'),
            ("t04-fleetroot-no-baseline",
             '(state_dir / ("%s.report-baseline" % lane)).is_file():', 1, "False:"),
            ("t05-placeholder-empty-angle", 'PLACEHOLDER_RE = re.compile(r"<[^<>]*>")', 1,
             'PLACEHOLDER_RE = re.compile(r"<[^<>]+>")'),
            ("t06-sibling-file-as-lane", 'if (fleet / ("%s-shokunin" % lane)).is_dir():', 1,
             'if (fleet / ("%s-shokunin" % lane)).exists():'),
            ("t07-report-regex-noprefix",
             'REPORT_PATH_RE = re.compile(r"\\.ufo/reports/round-(\\d+)/', 1,
             'REPORT_PATH_RE = re.compile(r"\\.ufo/reports/(?:round-)?(\\d+)/'),
            ("t08-role-regex-nospace", 'ROLE_ROUND_RE = re.compile(r"\\bround\\s+(\\d+)\\b")', 1,
             'ROLE_ROUND_RE = re.compile(r"\\bround\\s*(\\d+)\\b")'),
            ("t09-file-note-dropped", "if note:", 1, "if False:"),
            ("t10-unreadable-as-baseline",
             'return "none", None, "unreadable %s (%s)" % (base, exc.strerror or exc)', 1,
             'return "baseline", 10 ** 9, "unreadable %s (%s)" % (base, exc.strerror or exc)'),
            ("t11-lane-kind-legacy-dropped", '(state_dir / ("%s.round" % lane)).is_file()', 1,
             "False"),
            ("t12-finish-single-fail-na", '    if fails:\n        status = "FAIL"', 1,
             '    if len(fails) > 1:\n        status = "FAIL"'),
            ("t13-noreport-08-pass",
             '"status": "N/A", "detail": "no report path found in the file"}', 1,
             '"status": "PASS", "detail": "no report path found in the file"}'),
        ],
        "positive": P00,
    },
    "r96c1": {
        "instrument": DP,
        "fail_prefix": "self-test FAIL: ",
        "targets": [
            ("t01-var-dropped",
             "return bool(PLACEHOLDER_RE.search(token)) or bool(VARIABLE_RE.search(token))", 1,
             "return bool(PLACEHOLDER_RE.search(token))"),
            ("t02-var-brace-only", VAR_RE, 1,
             'VARIABLE_RE = re.compile(r"\\$\\{[^}]*\\}")'),
            ("t03-var-bare-only", VAR_RE, 1,
             'VARIABLE_RE = re.compile(r"\\$[A-Za-z_][A-Za-z0-9_]*")'),
            ("t04-le-to-lt", "if round_n <= value:", 1, "if round_n < value:"),
            ("t05-finish-allna-pass",
             'elif not files or not any(f["verdict"] == "PASS" for f in files):', 1,
             "elif not files:"),
            ("t06-role-whole-text", "m = ROLE_ROUND_RE.search(lines[0])", 1,
             "m = ROLE_ROUND_RE.search(text)"),
            ("t07-dirs-subset", "elif dirs != [round_n]:", 1, "elif round_n not in dirs:"),
            ("t08-bad-first-only", "bad = [(r, s) for r, s in paths if", 1,
             "bad = [(r, s) for r, s in paths[:1] if"),
            ("t09-wrong-first-only", "wrong = [s for s in stems if s != lane]", 1,
             "wrong = [s for s in stems[:1] if s != lane]"),
            ("t10-nonint-baseline",
             'return "none", None, "non-integer round in %s: %r" % (base, first[0])', 1,
             'return "baseline", 10 ** 9, "non-integer round in %s: %r" % (base, first[0])'),
            ("t11-noreport-04-pass", 'verdicts[cid] = {"status": "N/A",', 1,
             'verdicts[cid] = {"status": "PASS",'),
        ],
        "positive": P00,
    },
    "r95c1": {
        "instrument": MB,
        "fail_prefix": "FAIL ",
        "targets": [
            ("n1-manifest-at-head",
             'committed = git_show(lane, rev, MANIFEST).decode("utf-8")', 1,
             'committed = git_show(lane, "HEAD", MANIFEST).decode("utf-8")'),
            ("n5-label-targets-cne",
             'raise CouldNotEvaluate("manifest must name exactly the targets %s"', 1,
             'raise CouldNotEvaluate("arm kill-set-size: manifest must name exactly the targets %s"'),
            ("n11-accept-plus-two", MB_PIN, 1, 'return (n == want or n == want + 2), "observed'),
        ],
        "positive": ("n10-accept-plus-one", MB_PIN, 1, 'return (n == want or n == want + 1), "observed'),
    },
}

SUMMARY = re.compile(r"^(\d+) failure\(s\) over (\d+) assertions$", re.M)


class NotEvaluated(Exception):
    pass


def classify(rc: int, out: str, fail_prefix: str) -> str:
    found = SUMMARY.findall(out)
    if not found:
        return "RUN-ERROR"
    n = int(found[-1][0])
    fails = sum(1 for ln in out.splitlines() if ln.startswith(fail_prefix))
    if rc == 1 and n >= 1 and fails >= 1:
        return "REPORTED-FAILURE"
    if rc == 0 and n == 0:
        return "CLEAN"
    return "RUN-ERROR"


RUNNER = (
    "import os, sys, types\n"
    "path, src = sys.argv[1], sys.argv[2]\n"
    "with open(src, encoding='utf-8') as f: text = f.read()\n"
    "os.unlink(src)\n"
    "code = compile(text, path, 'exec', dont_inherit=True)\n"
    "del text\n"
    "sys.argv = [path, '--self-test']\n"
    "sys.path[0] = os.path.dirname(path)\n"
    "mod = types.ModuleType('__main__')\n"
    "mod.__file__ = path\n"
    "sys.modules['__main__'] = mod\n"
    "exec(code, mod.__dict__)\n"
)


def last_line(text: str) -> str:
    lines = [ln for ln in text.splitlines() if ln.strip()]
    return lines[-1] if lines else "<no output>"


def code_decoy(original: str, mutated: str, name: str) -> str:
    """Insert each changed statement, mutated, under a run-time-false guard before the original."""
    o = original.splitlines(keepends=True)
    m = mutated.splitlines(keepends=True)
    if len(o) != len(m):
        raise NotEvaluated("code decoy %s: the mutant changes the line count" % name)
    changed = [i + 1 for i in range(len(o)) if o[i] != m[i]]
    if not changed:
        raise NotEvaluated("code decoy %s: the mutant changes no line" % name)
    tree = ast.parse(mutated)
    parent: dict[int, ast.AST] = {}
    for node in ast.walk(tree):
        for child in ast.iter_child_nodes(node):
            parent[id(child)] = node
    spans: set[tuple[int, int]] = set()
    for line in changed:
        best = None
        for node in ast.walk(tree):
            if isinstance(node, ast.stmt) and node.lineno <= line <= node.end_lineno:
                if best is None or node.end_lineno - node.lineno < best.end_lineno - best.lineno:
                    best = node
        if best is None:
            raise NotEvaluated("code decoy %s: no statement covers line %d" % (name, line))
        while isinstance(best, ast.If) and o[best.lineno - 1].lstrip().startswith("elif") \
                and isinstance(parent.get(id(best)), ast.If):
            best = parent[id(best)]
        start = best.lineno
        indent = o[start - 1][:len(o[start - 1]) - len(o[start - 1].lstrip())]
        if best.col_offset != len(indent):
            raise NotEvaluated("code decoy %s: the statement at line %d does not start its line" % (name, start))
        spans.add((start, best.end_lineno))
    out = list(o)
    for start, end in sorted(spans, reverse=True):
        indent = o[start - 1][:len(o[start - 1]) - len(o[start - 1].lstrip())]
        block = [indent + 'if __name__ == "__decoy__":\n']
        block += ["    " + ln if ln.strip() else ln for ln in m[start - 1:end]]
        if not block[-1].endswith("\n"):
            block[-1] += "\n"
        out[start - 1:start - 1] = block
    return "".join(out)


def usage() -> int:
    print("usage: selftest-kills.py {c1|r96c1|r95c1} [REV] [REPO] [--rules v4|v5]", file=sys.stderr)
    return 2


def main(argv: list[str]) -> int:
    rules = "v5"
    args = list(argv)
    if "--rules" in args:
        i = args.index("--rules")
        if i + 1 >= len(args) or args[i + 1] not in ("v4", "v5"):
            return usage()
        rules = args[i + 1]
        del args[i:i + 2]
    if not args or args[0] not in CLAIMS or len(args) > 3:
        return usage()
    claim = args[0]
    tag = claim.upper()
    spec = CLAIMS[claim]
    instrument = spec["instrument"]
    prefix = spec["fail_prefix"]
    lane = Path(__file__).resolve().parents[3]
    repo = Path(args[2]).resolve() if len(args) > 2 else lane
    want_rev = args[1] if len(args) > 1 else "master"
    root = Path(os.environ.get("HYAKU_SCRATCH", "/fast/scratch/hyaku")) / "kotoba-r97" / "selftest-kills"
    work = None
    try:
        got = subprocess.run(["git", "-C", str(repo), "rev-parse", "--verify", "-q", want_rev + "^{commit}"],
                             stdout=subprocess.PIPE, stderr=subprocess.DEVNULL)
        if got.returncode != 0:
            raise NotEvaluated("REV %s is not a commit of %s" % (want_rev, repo))
        rev = got.stdout.decode().strip()
        shown = subprocess.run(["git", "-C", str(repo), "show", "%s:%s" % (rev, instrument)],
                               stdout=subprocess.PIPE, stderr=subprocess.DEVNULL)
        if shown.returncode != 0:
            raise NotEvaluated("instrument %s absent at %s" % (instrument, rev))
        try:
            original = shown.stdout.decode("utf-8")
        except UnicodeDecodeError as exc:
            raise NotEvaluated("instrument %s is not valid UTF-8 at %s (%s)" % (instrument, rev, exc))
        root.mkdir(parents=True, exist_ok=True)
        work = Path(tempfile.mkdtemp(prefix="run.", dir=root))
        print("claim %s rev %s repo %s instrument %s rules %s" % (claim, rev, repo, instrument, rules))

        def mutant_text(name: str, anchor: str, count: int, repl: str) -> str:
            found = original.count(anchor)
            if found != count:
                raise NotEvaluated("anchor miss: %s matches %d time(s), expected %d" % (name, found, count))
            return original.replace(anchor, repl)

        # Every job: (kind, name, text executed, text on disk). Built and compiled before any run.
        jobs: list[tuple[str, str, str, str]] = []
        for name, a, c, w in spec["targets"]:
            mt = mutant_text(name, a, c, w)
            jobs.append(("blind", name, mt, original))
            if rules == "v5":
                jobs.append(("mirror", name, mt, original))
        pname, pa, pc, pw = spec["positive"]
        pt = mutant_text(pname, pa, pc, pw)
        jobs.append(("pos-blind", pname, pt, original))
        if rules == "v5":
            jobs.append(("pos-mirror", pname, pt, original))
        for name, a, c, w in spec["targets"]:
            mark = DECOY_MARK_V4 if rules == "v4" else DECOY_MARK
            ct = original.rstrip("\n") + "\n" + "".join(mark + ln + "\n" for ln in w.splitlines())
            jobs.append(("comment", name, ct, ct))
            dt = code_decoy(original, mutant_text(name, a, c, w), name)
            jobs.append(("code", name, dt, dt))
        for kind, name, text, _ in jobs:
            try:
                compile(text, instrument, "exec", dont_inherit=True)
            except SyntaxError as exc:
                raise NotEvaluated("%s %s does not compile: %s" % (kind, name, exc))
        honest = ("honest", "honest", original, original)
        seed = "-"
        if rules == "v5":
            seed = os.environ.get("KOTOBA_R97_SEED") or os.urandom(8).hex()
            rng = random.Random(seed)
            rng.shuffle(jobs)
            jobs.insert(rng.randrange(1, len(jobs)), honest)
            jobs = [honest] + jobs + [honest]
        else:
            jobs = [honest] + jobs

        def fresh_world(tagname: str) -> tuple[Path, Path, dict]:
            d = Path(tempfile.mkdtemp(prefix=tagname + ".", dir=work))
            clone = d / "world" / "kotoba-shokunin"
            clone.parent.mkdir()
            for sub in ("tmp", "home", "cache"):
                (d / sub).mkdir()
            for cmd in (["git", "clone", "-q", "--shared", "--no-checkout", str(repo), str(clone)],
                        ["git", "-C", str(clone), "checkout", "-q", "--detach", rev]):
                if subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL).returncode != 0:
                    raise NotEvaluated("clone or checkout failed")
            env = dict(os.environ, TMPDIR=str(d / "tmp"), PYTHONDONTWRITEBYTECODE="1")
            if rules == "v5":
                env.update(HOME=str(d / "home"), XDG_CACHE_HOME=str(d / "cache"))
            return d, clone, env

        shared = fresh_world("shared") if rules == "v4" else None
        results: dict[tuple[str, str], list[str]] = {}
        for idx, (kind, name, text, on_disk) in enumerate(jobs):
            d, clone, env = shared if shared else fresh_world("r%03d" % idx)
            path = clone / instrument
            path.write_text(on_disk, encoding="utf-8")
            src = d / "src.py"
            src.write_text(text, encoding="utf-8")
            try:
                proc = subprocess.run([sys.executable, "-B", "-c", RUNNER, str(path), str(src)],
                                      cwd=clone, env=env,
                                      stdout=subprocess.PIPE, stderr=subprocess.STDOUT, timeout=TIMEOUT_S)
            except subprocess.TimeoutExpired:
                raise NotEvaluated("%s %s: self-test timeout after %ds" % (kind, name, TIMEOUT_S))
            finally:
                if shared:
                    path.write_text(original, encoding="utf-8")
                else:
                    shutil.rmtree(d, ignore_errors=True)
            out = proc.stdout.decode("utf-8", "replace")
            cls = classify(proc.returncode, out, prefix)
            results.setdefault((kind, name), []).append(cls)
            print("run %03d %s %s rc %d %s: %s" % (idx, kind, name, proc.returncode, cls, last_line(out)))

        rf = "REPORTED-FAILURE"
        honest_runs = results[("honest", "honest")]
        honest_clean = sum(1 for c in honest_runs if c == "CLEAN")
        cls_h = "CLEAN" if honest_clean == len(honest_runs) else next(c for c in honest_runs if c != "CLEAN")
        n = len(spec["targets"])
        killed = errors = mirror_rep = 0
        for name, _, _, _ in spec["targets"]:
            blind = results[("blind", name)][0]
            mirror = results[("mirror", name)][0] if rules == "v5" else rf
            mirror_rep += rules == "v5" and mirror == rf
            k = blind == rf and mirror == rf
            killed += k
            errors += "RUN-ERROR" in (blind, mirror)
            print("mutant %s blind %s mirror %s: %s" % (name, blind, mirror if rules == "v5" else "-",
                                                        "KILLED" if k else "not killed"))
        pblind = results[("pos-blind", pname)][0]
        pmirror = results[("pos-mirror", pname)][0] if rules == "v5" else rf
        mirror_rep += rules == "v5" and pmirror == rf
        pos = 1 if pblind == rf and pmirror == rf else 0
        print("positive %s blind %s mirror %s: %s" % (pname, pblind, pmirror if rules == "v5" else "-",
                                                     "KILLED" if pos else "not killed"))
        held_comment = sum(1 for nm, _, _, _ in spec["targets"] if results[("comment", nm)][0] == "CLEAN")
        held_code = sum(1 for nm, _, _, _ in spec["targets"] if results[("code", nm)][0] == "CLEAN")
        print("%s targets killed %d of %d (run errors %d); positive killed %d of 1; honest %s; "
              "comment decoys held %d of %d; code decoys held %d of %d"
              % (tag, killed, n, errors, pos, cls_h, held_comment, n, held_code, n))
        print("rules %s: honest runs CLEAN %d of %d; mirror runs reported %s; seed %s"
              % (rules, honest_clean, len(honest_runs),
                 ("%d of %d" % (mirror_rep, n + 1)) if rules == "v5" else "-", seed))
        met = cls_h == "CLEAN" and killed == n and pos == 1 and held_comment == n and held_code == n
        print("%s-PREDICATE-%s" % (tag, "MET" if met else "UNMET"))
        return 0 if met else 1
    except NotEvaluated as exc:
        print("%s-NOT-EVALUATED: %s" % (tag, exc))
        return 2
    finally:
        if work is not None:
            shutil.rmtree(work, ignore_errors=True)


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
