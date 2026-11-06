#!/usr/bin/env python3
"""selftest-kills v4 (round 96, claim C1, frozen counting command; plans/round-96.md).

Usage: python3 -B verifiers/fixtures/round-96/selftest-kills.py {c1|r95c1} [REV] [REPO]
  REV   full commit to measure (default: the tip of branch master of REPO)
  REPO  repository to clone REV from (default: this lane; a scratch repo for a candidate or forgery)

Successor of verifiers/fixtures/round-95/selftest-kills.py (v3, unchanged there). The v3 rules are
kept byte-for-byte in meaning; v4 moves them from one instrument to a claim table that names its
instrument and that instrument's failure-line prefix, so the same kill rule runs on a province
instrument (the dispatch-prompt checker, SKILL.md § Dispatch-prompt fidelity checklist):

1. Outcome classes (v3 rule 1; S270 unittest `errors` vs `failures`). A run is classified from its
   output, not from its exit code alone:
     REPORTED-FAILURE  exit 1 AND the last summary line `<N> failure(s) over <M> assertions` has
                       N >= 1 AND at least one line starts with the claim's failure prefix
     CLEAN             exit 0 AND the last summary line has N == 0
     RUN-ERROR         anything else (a traceback, a crash exit, a missing summary, a summary with
                       failures but no failure line)
   A mutant is KILLED iff its run is REPORTED-FAILURE. A RUN-ERROR is never a kill. A timeout
   (600 s) is could-not-evaluate (exit 2); a mutant that does not compile is could-not-evaluate.
2. Two decoys per target (v3 rule 2): the comment decoy (replacement lines appended as
   `# r96-decoy` comments) and the code decoy (every statement the mutant changes inserted, mutated,
   under `if __name__ == "__decoy__":` immediately before the original). A decoy HOLDS iff CLEAN.
3. Source-blind mutant runs (v3 rule 3): a mutant's text is compiled with the instrument's path as
   filename and executed as `__main__` (argv `[path, --self-test]`) while the file on disk holds the
   UNMODIFIED bytes. Bound (v3, unchanged): a sniffer of its own compiled code objects that also
   proves the decoy guard dead is not caught.

Mutant tables (frozen):
  c1 — verifiers/verify_dispatch_prompts.py, failure prefix `self-test FAIL: ` (survivors of the
       landed --self-test found by the round-96 pre-freeze sweep, receipts/recon-sweep.txt)
    target t01-var-dropped        : has_placeholder ignores VARIABLE_RE (`${X}` and `$X` pass)
    target t02-var-brace-only     : VARIABLE_RE matches `${X}` only (bare `$X` passes)
    target t03-var-bare-only      : VARIABLE_RE matches bare `$X` only (`${X}` passes)
    target t04-le-to-lt           : round_le_latest_dispatched compares `<` (equality reads FAIL)
    target t05-finish-allna-pass  : a check whose files are all N/A (none PASS) reads PASS
    target t06-role-whole-text    : the role round is read from the whole text, not line 1
    target t07-dirs-subset        : the report-dir conjunct passes when N is one of several dirs
    target t08-bad-first-only     : only the first report path is scanned for placeholders
    target t09-wrong-first-only   : only the first (sorted) report stem is compared to the lane id
    target t10-nonint-baseline    : a non-integer baseline round is read as an unbounded baseline
    target t11-noreport-04-pass   : a file with no report path reads PASS on every dispatch.04 conjunct
    positive p00-md-not-stripped  : the `.md` suffix is not stripped from the stem (killed at base)
  r95c1 — verifiers/check_mutation_battery.py, failure prefix `FAIL ` (positive control: the
       round-95 C1 table replayed under v4 must still read MET, so the generalisation does not
       refuse honest arms); targets n1-manifest-at-head, n5-label-targets-cne, n11-accept-plus-two;
       positive n10-accept-plus-one (anchors as in the round-95 counter)

Predicate (frozen; the same sentence in plans/round-96.md):
  <C>-PREDICATE-MET iff (honest) the unmodified self-test run is CLEAN; (targets) every target mutant
  applies and is KILLED; (positive) the positive mutant applies and is KILLED; (guard) every target's
  comment decoy and code decoy HOLDS.
Output: one line per run, then
  `<C> targets killed K of N (run errors E); positive killed P of 1; honest <class>;
   comment decoys held D of N; code decoys held X of N`
  and `<C>-PREDICATE-MET` / `<C>-PREDICATE-UNMET` / `<C>-NOT-EVALUATED`.
Exit 0 met, 1 unmet, 2 could-not-evaluate.
Scratch under ${HYAKU_SCRATCH:-/fast/scratch/hyaku}/kotoba-r96/selftest-kills, removed on exit.
"""
from __future__ import annotations

import ast
import os
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

CLAIMS = {
    "c1": {
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
        "positive": ("p00-md-not-stripped", "stem = stem[:-3]", 1, "stem = stem[:]"),
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


def run_selftest(clone: Path, instrument: str, env: dict, code_text: str, src: Path) -> tuple[int, str]:
    """Execute code_text as the instrument's __main__; the file on disk is left as it is."""
    src.write_text(code_text, encoding="utf-8")
    try:
        proc = subprocess.run([sys.executable, "-B", "-c", RUNNER, str(clone / instrument), str(src)],
                              cwd=clone, env=env,
                              stdout=subprocess.PIPE, stderr=subprocess.STDOUT, timeout=TIMEOUT_S)
    except subprocess.TimeoutExpired:
        raise NotEvaluated("self-test timeout after %ds" % TIMEOUT_S)
    return proc.returncode, proc.stdout.decode("utf-8", "replace")


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
        # v4: an `elif` arm is an If nested in its parent's orelse; a guard inserted before the
        # `elif` line would cut the chain, so the decoy carries the whole enclosing if-chain.
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


def main(argv: list[str]) -> int:
    if not argv or argv[0] not in CLAIMS or len(argv) > 3:
        print("usage: selftest-kills.py {c1|r95c1} [REV] [REPO]", file=sys.stderr)
        return 2
    claim = argv[0]
    tag = claim.upper()
    spec = CLAIMS[claim]
    instrument = spec["instrument"]
    prefix = spec["fail_prefix"]
    lane = Path(__file__).resolve().parents[3]
    repo = Path(argv[2]).resolve() if len(argv) > 2 else lane
    want_rev = argv[1] if len(argv) > 1 else "master"
    got = subprocess.run(["git", "-C", str(repo), "rev-parse", "--verify", "-q", want_rev + "^{commit}"],
                         stdout=subprocess.PIPE, stderr=subprocess.DEVNULL)
    if got.returncode != 0:
        print("%s-NOT-EVALUATED: REV %s is not a commit of %s" % (tag, want_rev, repo))
        return 2
    rev = got.stdout.decode().strip()
    root = Path(os.environ.get("HYAKU_SCRATCH", "/fast/scratch/hyaku")) / "kotoba-r96" / "selftest-kills"
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
        print("claim %s rev %s repo %s instrument %s" % (claim, rev, repo, instrument))
        path = clone / instrument
        if not path.is_file():
            raise NotEvaluated("instrument %s absent at %s" % (instrument, rev))
        original = path.read_text(encoding="utf-8")

        src = work / "src.py"

        def run_text(text: str, label: str, on_disk: str) -> tuple[int, str, str]:
            """Run `text` as the instrument; the instrument file holds `on_disk` during the run."""
            try:
                compile(text, str(path), "exec", dont_inherit=True)
            except SyntaxError as exc:
                raise NotEvaluated("%s does not compile: %s" % (label, exc))
            path.write_text(on_disk, encoding="utf-8")
            try:
                rc, out = run_selftest(clone, instrument, env, text, src)
            finally:
                path.write_text(original, encoding="utf-8")
            return rc, out, classify(rc, out, prefix)

        rc_h, out_h, cls_h = run_text(original, "honest", original)
        print("honest rc %d %s: %s" % (rc_h, cls_h, last_line(out_h)))

        def mutant_text(name: str, anchor: str, count: int, repl: str) -> str:
            found = original.count(anchor)
            if found != count:
                raise NotEvaluated("anchor miss: %s matches %d time(s), expected %d" % (name, found, count))
            return original.replace(anchor, repl)

        killed = errors = 0
        mirror = 0
        for name, a, c, w in spec["targets"]:
            rc, out, cls = run_text(mutant_text(name, a, c, w), "mutant " + name, original)
            verdict = "KILLED" if cls == "REPORTED-FAILURE" else ("RUN-ERROR (not a kill)" if cls == "RUN-ERROR" else "SURVIVED")
            killed += cls == "REPORTED-FAILURE"
            errors += cls == "RUN-ERROR"
            print("mutant %s rc %d %s: %s" % (name, rc, verdict, last_line(out)))
            mtext = mutant_text(name, a, c, w)
            rc_m, out_m, cls_m = run_text(mtext, "mirror " + name, mtext)
            mirror += cls_m == "REPORTED-FAILURE"
            print("mirror %s rc %d %s: %s" % (name, rc_m, "KILLED" if cls_m == "REPORTED-FAILURE" else cls_m, last_line(out_m)))
        pname, pa, pc, pw = spec["positive"]
        rc, out, cls = run_text(mutant_text(pname, pa, pc, pw), "positive " + pname, original)
        pos = 1 if cls == "REPORTED-FAILURE" else 0
        print("positive %s rc %d %s: %s" % (pname, rc, "KILLED" if pos else cls, last_line(out)))
        mtext = mutant_text(pname, pa, pc, pw)
        rc, out, cls = run_text(mtext, "mirror " + pname, mtext)
        pos_mirror = 1 if cls == "REPORTED-FAILURE" else 0
        print("mirror %s rc %d %s: %s" % (pname, rc, "KILLED" if pos_mirror else cls, last_line(out)))

        held_comment = held_code = 0
        for name, a, c, w in spec["targets"]:
            text = original.rstrip("\n") + "\n" + "".join("# r96-decoy " + ln + "\n" for ln in w.splitlines())
            rc, out, cls = run_text(text, "comment decoy " + name, text)
            held_comment += cls == "CLEAN"
            print("comment decoy %s rc %d %s: %s" % (name, rc, "HELD" if cls == "CLEAN" else cls + " (not held)", last_line(out)))
            text = code_decoy(original, mutant_text(name, a, c, w), name)
            rc, out, cls = run_text(text, "code decoy " + name, text)
            held_code += cls == "CLEAN"
            print("code decoy %s rc %d %s: %s" % (name, rc, "HELD" if cls == "CLEAN" else cls + " (not held)", last_line(out)))
        rc_h2, out_h2, cls_h2 = run_text(original, "honest-final", original)
        print("honest-final rc %d %s: %s" % (rc_h2, cls_h2, last_line(out_h2)))
        if path.read_text(encoding="utf-8") != original:
            raise NotEvaluated("instrument not restored")
        n = len(spec["targets"])
        print("mirror targets killed %d of %d; mirror positive killed %d of 1"
              % (mirror, n, pos_mirror))
        print("%s targets killed %d of %d (run errors %d); positive killed %d of 1; honest %s; "
              "comment decoys held %d of %d; code decoys held %d of %d"
              % (tag, killed, n, errors, pos, cls_h, held_comment, n, held_code, n))
        met = cls_h == "CLEAN" and cls_h2 == "CLEAN" and killed == n and mirror == n \
            and pos == 1 and pos_mirror == 1 and held_comment == n and held_code == n
        print("%s-PREDICATE-%s" % (tag, "MET" if met else "UNMET"))
        return 0 if met else 1
    except NotEvaluated as exc:
        print("%s-NOT-EVALUATED: %s" % (tag, exc))
        return 2
    finally:
        shutil.rmtree(work, ignore_errors=True)


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
