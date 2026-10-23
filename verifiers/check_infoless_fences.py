#!/usr/bin/env python3
"""Round-57 C2 operability counter: info-less fences must not be read as shell.

THE FROZEN SPEC (written 2026-10-23, before any content it scores; the L1
commits this file with the round plan):

1. `check_infoless_fences.py --rev <40-hex> [--seed N ...]` (default seeds
   11 22 33).  Extract the measured revision's `verifiers/` tree into a fresh
   temp dir per run (`git archive <rev> verifiers | tar -x -C <tmp>`); run ONLY
   that copy, never the working tree.
2. Per seed, generate cases with `random.Random(seed)`; random tokens are
   drawn from ONE generator: 1-2 pronounceable lowercase chunks of 3-8
   letters, optionally joined by `-` or followed by 1-3 digits (e.g.
   `molvat`, `trel-quosk`, `bandor42`); a token for which `shutil.which`
   resolves, or that is a shell keyword/builtin, is rejected and redrawn --
   the same rule for EVERY token class, so a bogus command head is one more
   draw from that generator and cannot be told from a table cell by shape.
   (L1 amendment of 2026-10-23, before freeze: the earlier fixed `zq` prefix
   and fixed `[a-z]{3}` + 6 hex shape are dropped.)  Shuffle case order.  Each
   case gets its own fresh dir with a random name, holding `SKILL.md` =
   frontmatter (`name: <dirname>`, `description: <random words>`) + a short
   heading + ONE fenced block.  Run per case, from an empty temp cwd, env
   PYTHONSAFEPATH=1:
   `timeout 60 python3 -B -P <tmp>/verifiers/verify_skill_checklist.py
   --repo <casedir> --skill <casedir>/SKILL.md
   --check trigger.command_binary_resolves --json`;
   parse the JSON and read the status of `trigger.command_binary_resolves`.
   Unparseable output or timeout = case wrong.
3. Classes, 4 cases per class per seed:
   PASS-expected (fence has NO info string; besides the class lines it holds
   one real command line, `ls -la` or `git --version`, at a random position;
   correct iff status == PASS):
   P1 markdown table: header row `| w | w |`, alignment row (`|---|:---:|`
      variants), 2-3 body rows of random tokens.
   P2 box-drawing diagram using U+2500-U+257F (`┌──┐`, `│ tok │`, `└──┘`)
      and tree lines (`├── tok`, `└── tok`).
   P3 ascii box: `+------+`, `| tok |`, `+------+`.
   P4 arrow line: `<tok> <tok> (<tok>)    → <tok>/<tok>.json` (U+2192),
      2-3 such lines.
   P5 key: value output: 2-3 lines `<TOK>: <tok>` or `<tok>:   <tok>/<tok>`
      (first whitespace-delimited token ends with `:`; uppercase variant
      included).
   FAIL-expected hard negatives (correct iff status == FAIL AND the check's
   detail text contains that case's bogus head):
   H1 info-less fence: `<bogus> --<tok>` alone.
   H2 info-less fence: `ls | <bogus>` (pipe not leading).
   H3 info-less fence: P1 table rows, then `<bogus> <tok>` on its own line.
   H4 info-less fence: `<bogus> --opt=<tok>:<tok>` (colon inside an argument,
      first token not ending with `:`).
   H5 shell-tagged fence (```bash): `<bogus> <tok>` (control: shell-tagged
      behaviour).
4. Output: `info-less fence cases correct N of T (pass-expected P of PT;
   hard negatives H of HT)`, plus one
   `wrong <seed> <class> <casedir-basename> status=<s>` line per wrong case.
   Predicate (frozen): exit 0 iff N == T and T >= 120 (3 seeds x 10 classes x
   4); else 1; 2 on usage/env error.
5. `--self-test`: hermetic arms (generator determinism per seed, class counts,
   shuffle, every bogus head unresolvable, JSON status parsing, wrong-line
   formatting, predicate arithmetic incl. T<120 and N<T must fail) plus the
   R5 guard-mutation kill table recorded in the w0 receipt (every rejection
   branch has a must-fail arm; the w0 receipt's table lists guard, mutation
   and killed/survived).
6. First output line, on both modes, is `counter sha256 <hex>` read from this
   file's own bytes via `__file__`; a measured run then prints `measured
   <40-hex>` and `instrument sha256 <hex>` of the extracted, executed copy.

Implementation notes, stated only as far as the code goes:

  * The repo is `--repo` when given, else the parent of this file's directory
    (so the copy must live in `verifiers/`).  `--rev` is resolved with
    `git -C <repo> rev-parse --verify <rev>^{commit}`; anything short of a
    full 40-hex lowercase-or-uppercase hash that resolves is exit 2.
  * `git archive --format=tar <full-rev> verifiers` writes the tar to memory
    and the stdlib `tarfile` module extracts it into a fresh temp dir (the
    spec's `| tar -x -C <tmp>` without a shell pipe).  Only
    `<tmp>/verifiers/verify_skill_checklist.py` is executed.
  * The spec's `timeout 60` is the coreutils wrapper; a 70 s subprocess
    backstop guards a stuck wrapper.  Both `python3` and `timeout` must be on
    PATH or the run is exit 2.
  * An unparseable --json output or a timeout is a wrong case; its wrong line
    prints `status=unparseable`.
  * Exit 2, with no traceback, on: missing or malformed `--rev`, a git
    failure, no instrument in the extracted tree, a missing `python3` /
    `timeout`, or an unreadable own file.  `--self-test` cannot be combined
    with `--rev` / `--seed`.
  * A `--seed` value may repeat; a repeated seed is measured twice (only the
    frozen predicate's `T >= 120` and `N == T` are judged).
"""
import argparse
import hashlib
import io
import json
import os
import random
import re
import shutil
import subprocess
import sys
import tarfile
import tempfile
from collections import namedtuple
from pathlib import Path

DEFAULT_SEEDS = (11, 22, 33)
CASES_PER_CLASS = 4
# class name -> expected verdict; order is the generation order per seed.
CLASSES = (
    ("P1", "PASS"), ("P2", "PASS"), ("P3", "PASS"), ("P4", "PASS"),
    ("P5", "PASS"), ("H1", "FAIL"), ("H2", "FAIL"), ("H3", "FAIL"),
    ("H4", "FAIL"), ("H5", "FAIL"),
)
EXPECTED_TOTAL = len(CLASSES) * CASES_PER_CLASS * len(DEFAULT_SEEDS)  # 120
MIN_TOTAL = 120
CASE_TIMEOUT = 60
MAX_DRAWS = 1000
CHECK_ID = "trigger.command_binary_resolves"
INSTRUMENT = "verifiers/verify_skill_checklist.py"
REAL_COMMANDS = ("ls -la", "git --version")
TOOLS = ("python3", "timeout")
FULL_REV_RE = re.compile(r"^[0-9a-fA-F]{40}$")
TOKEN_RE = re.compile(r"^[a-z]{3,8}(?:-[a-z]{3,8})?[0-9]{0,3}$")
DIRNAME_RE = re.compile(r"^skill-[0-9a-f]{8}$")
CONSONANTS = "bcdfghjklmnprstvwz"
VOWELS = "aeiou"
# Shell keywords, builtins and wrapper prefixes: a token that names one is
# never generated, whatever class it belongs to (round-16 skip list of
# verifiers/verify_skill_checklist.py, minus punctuation-only entries).
RESERVED = frozenset("""
if for while until case do done then else elif fi esac in
echo cd pwd export unset read local return exit printf set test
true false wait ulimit umask type hash getopts let declare
typeset readonly break continue times dirs jobs fg bg
kill disown suspend logout enable alias unalias fc history
sudo env command nohup time builtin xargs source exec
""".split())

Case = namedtuple(
    "Case", "seed cls dirname desc info lines expect head tokens")


class EnvError(Exception):
    """Usage/environment failure: the run cannot measure (exit 2)."""


def own_sha(path=None):
    """sha256 of this file's own bytes, read through a path, never a pipe."""
    p = Path(path if path is not None else __file__)
    try:
        return hashlib.sha256(p.read_bytes()).hexdigest()
    except OSError as e:
        raise EnvError("cannot read own file %s: %s" % (p, e))


def rev_problem(rev):
    """Why `rev` cannot be measured, or None when it is a full 40-hex hash."""
    if not rev:
        return "--rev is required (a full 40-hex commit hash)"
    if not FULL_REV_RE.match(rev):
        return "--rev %r is not a full 40-hex hash" % rev
    return None


def usage_conflict(self_test, rev, seeds):
    """Why this flag combination is a usage error, or None."""
    if self_test and (rev or seeds):
        return "--self-test cannot be combined with --rev or --seed"
    return None


# ---------------------------------------------------------------- git plumbing
def git_run(repo, args):
    return subprocess.run(["git", "-C", str(repo), *args], capture_output=True)


def resolve_rev(repo, rev, run=git_run):
    """The full commit hash `rev` names; EnvError when git cannot verify it."""
    r = run(repo, ["rev-parse", "--verify", "%s^{commit}" % rev])
    out = r.stdout.decode("utf-8", "replace").strip()
    if r.returncode != 0:
        raise EnvError(
            "git rev-parse --verify %s^{commit} failed in %s (exit %d): %s"
            % (rev, repo, r.returncode,
               r.stderr.decode("utf-8", "replace").strip()[:300]))
    if not FULL_REV_RE.match(out):
        raise EnvError("git rev-parse returned %r, not a full 40-hex hash"
                       % out[:60])
    return out


def archive_verifiers(repo, rev, run=git_run):
    """The measured revision's `verifiers/` tree as an uncompressed tar."""
    r = run(repo, ["archive", "--format=tar", rev, "verifiers"])
    if r.returncode != 0:
        raise EnvError(
            "git archive %s verifiers failed in %s (exit %d): %s"
            % (rev, repo, r.returncode,
               r.stderr.decode("utf-8", "replace").strip()[:300]))
    return r.stdout


def extract_tar(data, dest):
    """Extract a git-archive tar into `dest` with the stdlib extractor."""
    dest = Path(dest)
    dest.mkdir(parents=True, exist_ok=True)
    with tarfile.open(fileobj=io.BytesIO(data), mode="r:") as tf:
        tf.extractall(dest, filter="data")


def require_instrument(tree):
    """The verifier inside the extracted tree; EnvError when it is absent."""
    path = Path(tree) / INSTRUMENT
    if not path.is_file():
        raise EnvError("%s is absent from the extracted tree %s"
                       % (INSTRUMENT, tree))
    return path


def require_tools(which=shutil.which):
    """EnvError when a tool the frozen command needs is not on PATH."""
    missing = [t for t in TOOLS if not which(t)]
    if missing:
        raise EnvError("required tool(s) not on PATH: %s" % ", ".join(missing))


# ------------------------------------------------------------- token generator
def pronounceable(rng, length):
    return "".join(
        (CONSONANTS if i % 2 == 0 else VOWELS)[
            rng.randrange(len(CONSONANTS if i % 2 == 0 else VOWELS))]
        for i in range(length))


def draw_word(rng):
    """One candidate: 1-2 pronounceable chunks, optional `-` join or 1-3 digits."""
    word = pronounceable(rng, rng.randint(3, 8))
    style = rng.random()
    if style < 0.25:
        return word + "-" + pronounceable(rng, rng.randint(3, 8))
    if style < 0.5:
        return word + "".join(str(rng.randrange(10))
                              for _ in range(rng.randint(1, 3)))
    return word


def make_token(rng, taken=frozenset(), draw=None, which=shutil.which):
    """A shape-valid token that names no binary, builtin or already-used word."""
    draw = draw or draw_word
    for _ in range(MAX_DRAWS):
        tok = draw(rng)
        if not TOKEN_RE.match(tok):
            continue
        if tok in taken:
            continue
        if tok in RESERVED:
            continue
        if which(tok):
            continue
        return tok
    raise RuntimeError("token generator exhausted %d draws" % MAX_DRAWS)


def new_dirname(rng, taken, draw=None):
    """A random case-directory name not already used in this seed block."""
    draw = draw or (lambda r: "skill-%08x" % r.getrandbits(32))
    for _ in range(MAX_DRAWS):
        name = draw(rng)
        if name in taken:
            continue
        return name
    raise RuntimeError("case-directory generator exhausted %d draws" % MAX_DRAWS)


# ------------------------------------------------------------------ case shapes
def insert_command(rng, lines):
    """The class lines plus one real command at a random position."""
    out = list(lines)
    out.insert(rng.randint(0, len(out)),
               REAL_COMMANDS[rng.randrange(len(REAL_COMMANDS))])
    return out


def table_rows(rng, tok):
    rows = ["| %s | %s |" % (tok(), tok()),
            rng.choice(("|---|---|", "|---|:---:|", "|:--|--:|"))]
    for _ in range(rng.randint(2, 3)):
        rows.append("| %s | %s |" % (tok(), tok()))
    return rows


def case_p1(rng, tok):
    return insert_command(rng, table_rows(rng, tok)), None


def case_p2(rng, tok):
    lines = ["\u250c\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2510",
             "\u2502 %s \u2502" % tok(),
             "\u2514\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2518"]
    for _ in range(rng.randint(1, 2)):
        lines.append("%s\u2500\u2500 %s" % (rng.choice(("\u251c", "\u2514")),
                                           tok()))
    return insert_command(rng, lines), None


def case_p3(rng, tok):
    lines = ["+------+", "| %s |" % tok(), "+------+"]
    return insert_command(rng, lines), None


def case_p4(rng, tok):
    lines = []
    for _ in range(rng.randint(2, 3)):
        lines.append("%s %s (%s)    \u2192 %s/%s.json"
                     % (tok(), tok(), tok(), tok(), tok()))
    return insert_command(rng, lines), None


def case_p5(rng, tok):
    lines = ["%s: %s" % (tok().upper(), tok())]
    for _ in range(rng.randint(1, 2)):
        if rng.random() < 0.5:
            lines.append("%s: %s" % (tok().upper(), tok()))
        else:
            lines.append("%s:   %s/%s" % (tok(), tok(), tok()))
    return insert_command(rng, lines), None


def case_h1(rng, tok):
    head = tok()
    return ["%s --%s" % (head, tok())], head


def case_h2(rng, tok):
    head = tok()
    return ["ls | %s" % head], head


def case_h3(rng, tok):
    head = tok()
    rows = table_rows(rng, tok)
    rows.append("%s %s" % (head, tok()))
    return rows, head


def case_h4(rng, tok):
    head = tok()
    return ["%s --opt=%s:%s" % (head, tok(), tok())], head


def case_h5(rng, tok):
    head = tok()
    return ["%s %s" % (head, tok())], head


BUILDERS = {"P1": case_p1, "P2": case_p2, "P3": case_p3, "P4": case_p4,
            "P5": case_p5, "H1": case_h1, "H2": case_h2, "H3": case_h3,
            "H4": case_h4, "H5": case_h5}


# ---------------------------------------------------------------------- plan
def plan_cases(seeds, which=shutil.which):
    """Every case for every seed, tokens drawn once, block order shuffled."""
    cases = []
    for seed in seeds:
        rng = random.Random(seed)
        taken_names = set()
        block = []
        for cls, expect in CLASSES:
            info = "bash" if cls == "H5" else ""
            for _ in range(CASES_PER_CLASS):
                dirname = new_dirname(rng, taken_names)
                taken_names.add(dirname)
                drawn = []

                def tok(rng=rng, drawn=drawn):
                    word = make_token(rng, drawn, which=which)
                    drawn.append(word)
                    return word

                desc = " ".join(tok() for _ in range(4))
                lines, head = BUILDERS[cls](rng, tok)
                block.append(Case(seed=seed, cls=cls, dirname=dirname,
                                  desc=desc, info=info, lines=lines,
                                  expect=expect, head=head,
                                  tokens=tuple(drawn)))
        rng.shuffle(block)
        cases.extend(block)
    return cases


def render_skill(case):
    """frontmatter + short heading + exactly one fenced block."""
    text = ["---", "name: %s" % case.dirname,
            "description: %s" % case.desc, "---", "", "# Case", "",
            "```" + case.info]
    text.extend(case.lines)
    text.extend(["```", ""])
    return "\n".join(text)


# -------------------------------------------------------------------- running
def default_runner(argv, cwd, env):
    return subprocess.run(argv, cwd=str(cwd), env=env, capture_output=True,
                          text=True, timeout=CASE_TIMEOUT + 10)


def run_case(case, tree, workdir, env, runner=None):
    """The case's status tuple, or None when the output is untrustworthy."""
    casedir = Path(workdir) / "cases" / case.dirname
    casedir.mkdir(parents=True, exist_ok=True)
    (casedir / "SKILL.md").write_text(render_skill(case), encoding="utf-8")
    cwd = Path(workdir) / "cwd" / case.dirname
    cwd.mkdir(parents=True, exist_ok=True)
    argv = ["timeout", str(CASE_TIMEOUT), "python3", "-B", "-P",
            str(Path(tree) / INSTRUMENT),
            "--repo", str(casedir), "--skill", str(casedir / "SKILL.md"),
            "--check", CHECK_ID, "--json"]
    try:
        result = (runner or default_runner)(argv, cwd, env)
    except subprocess.TimeoutExpired:
        return None
    return parse_status(result.stdout)


def parse_status(text):
    """(status, detail) of the measured check, or None for unparseable output."""
    try:
        doc = json.loads(text)
    except (TypeError, ValueError):
        return None
    if not isinstance(doc, dict):
        return None
    checks = doc.get("checks")
    if not isinstance(checks, list):
        return None
    for item in checks:
        if not isinstance(item, dict):
            continue
        if item.get("id") != CHECK_ID:
            continue
        status = item.get("status")
        if not isinstance(status, str):
            return None
        detail = item.get("detail")
        return status, detail if isinstance(detail, str) else ""
    return None


def case_correct(case, parsed):
    """The class's frozen correctness rule."""
    if parsed is None:
        return False
    status, detail = parsed
    if case.expect == "PASS":
        return status == "PASS"
    return status == "FAIL" and case.head in detail


def wrong_line(case, parsed):
    status = parsed[0] if parsed is not None else "unparseable"
    return "wrong %d %s %s status=%s" % (case.seed, case.cls, case.dirname,
                                         status)


def predicate_ok(correct, total):
    """The frozen predicate: every case correct and at least 120 cases."""
    return correct == total and total >= MIN_TOTAL


def guarded(fn, report=None):
    """(exit code, value): 2 on a usage/environment failure, never a traceback."""
    report = report or (lambda msg: print(msg, file=sys.stderr))
    try:
        return 0, fn()
    except (EnvError, OSError) as e:
        report("infoless-fences: %s" % e)
        return 2, None


# ------------------------------------------------------------------- measure
def measure(repo, rev, seeds, which=shutil.which, run=git_run, runner=None):
    """(full rev, instrument sha, cases, tallies, wrong lines)."""
    full = resolve_rev(repo, rev, run=run)
    require_tools(which)
    with tempfile.TemporaryDirectory(prefix="kotoba-r57-infoless-") as td:
        work = Path(td)
        tree = work / "tree"
        extract_tar(archive_verifiers(repo, full, run=run), tree)
        instrument = require_instrument(tree)
        instrument_sha = hashlib.sha256(instrument.read_bytes()).hexdigest()
        cases = plan_cases(seeds)
        env = dict(os.environ)
        env["PYTHONSAFEPATH"] = "1"
        tallies = {"PASS": [0, 0], "FAIL": [0, 0]}
        wrong = []
        for case in cases:
            parsed = run_case(case, tree, work, env, runner=runner)
            tallies[case.expect][1] += 1
            if case_correct(case, parsed):
                tallies[case.expect][0] += 1
            else:
                wrong.append(wrong_line(case, parsed))
    return full, instrument_sha, cases, tallies, wrong


# ------------------------------------------------------------------ self-test
def self_test():
    assertions = 0
    failures = 0

    def check(name, actual, expected):
        nonlocal assertions, failures
        assertions += 1
        if actual != expected:
            failures += 1
            print("FAIL %s: got %r, expected %r" % (name, actual, expected))

    def value(fn):
        try:
            return fn()
        except Exception as e:  # a mutated guard must fail the arm, not crash
            return "raised %s" % type(e).__name__

    def raises(fn, exc):
        try:
            fn()
        except exc:
            return True
        except Exception as e:
            return "wrong exception %s" % type(e).__name__
        return "no exception"

    def draw_seq(seq):
        it = iter(seq)
        return lambda rng: next(it)

    def which_none(tok):
        return None

    def fake_git(code, out=b"", err=b""):
        def run(repo, args):
            return subprocess.CompletedProcess(
                ["git"] + list(args), code, out, err)
        return run

    def make_tar(members):
        buf = io.BytesIO()
        with tarfile.open(fileobj=buf, mode="w") as tf:
            for name, data in members:
                info = tarfile.TarInfo(name)
                info.size = len(data)
                tf.addfile(info, io.BytesIO(data))
        return buf.getvalue()

    # frozen constants and plan shape
    check("class count", len(CLASSES), 10)
    check("cases per class", CASES_PER_CLASS, 4)
    check("expected total", EXPECTED_TOTAL, 120)
    check("frozen minimum", MIN_TOTAL, 120)
    plan = plan_cases(DEFAULT_SEEDS)
    check("planned total", len(plan), EXPECTED_TOTAL)
    counts = {}
    for c in plan:
        counts[(c.seed, c.cls)] = counts.get((c.seed, c.cls), 0) + 1
    check("every (seed, class) has 4", sorted(set(counts.values())), [4])
    check("seed set", sorted({c.seed for c in plan}), list(DEFAULT_SEEDS))
    check("class set", sorted({c.cls for c in plan}),
          sorted(cls for cls, _ in CLASSES))
    check("dirname unique per seed",
          all(len({c.dirname for c in plan if c.seed == s})
              == len(CLASSES) * CASES_PER_CLASS for s in DEFAULT_SEEDS), True)
    check("dirname shape", {bool(DIRNAME_RE.match(c.dirname)) for c in plan},
          {True})
    check("plan determinism per seed", plan_cases(DEFAULT_SEEDS), plan)
    canonical = [cls for cls, _ in CLASSES for _ in range(CASES_PER_CLASS)]
    check("shuffle changes every seed block",
          sum(1 for s in DEFAULT_SEEDS
              if [c.cls for c in plan if c.seed == s] != canonical),
          len(DEFAULT_SEEDS))

    # one fence per skill, frontmatter names the dir, only H5 is tagged
    rendered = [(c, render_skill(c)) for c in plan]
    check("exactly one fenced block per case",
          {sum(1 for L in r.splitlines() if L.startswith("```"))
           for _, r in rendered}, {2})
    check("fence info strings", sorted({c.info for c in plan}), ["", "bash"])
    check("frontmatter name is the dirname",
          all(r.splitlines()[1] == "name: " + c.dirname for c, r in rendered),
          True)
    check("frontmatter description is four words",
          {len(c.desc.split()) for c in plan}, {4})

    # tokens: one generator, shape-valid, unresolvable, reserved-free, distinct
    check("every generated token unresolvable",
          [t for c in plan for t in c.tokens if shutil.which(t) is not None],
          [])
    check("no reserved token", [t for c in plan for t in c.tokens
                                if t in RESERVED], [])
    check("token shape", [t for c in plan for t in c.tokens
                          if not TOKEN_RE.match(t)], [])
    check("tokens distinct within a case",
          all(len(set(c.tokens)) == len(c.tokens) for c in plan), True)
    check("hard-negative head is a drawn token",
          all(c.head in c.tokens for c in plan if c.expect == "FAIL"), True)
    check("pass cases carry exactly one real command",
          all(sum(1 for L in c.lines if L in REAL_COMMANDS) == 1
              for c in plan if c.expect == "PASS"), True)
    check("hard negatives carry no real command",
          all(sum(1 for L in c.lines if L in REAL_COMMANDS) == 0
              for c in plan if c.expect == "FAIL"), True)

    # class shapes
    p1 = [c for c in plan if c.cls == "P1"]
    check("P1 has an alignment row",
          all(any(re.match(r"^\|[-:|]+\|$", L) for L in c.lines)
              for c in p1), True)
    check("P1 has 4-5 table lines",
          {sum(1 for L in c.lines if L.startswith("|")) for c in p1},
          {4, 5})
    p2 = [c for c in plan if c.cls == "P2"]
    check("P2 box characters stay in U+2500-U+257F",
          [ch for c in p2 for L in c.lines for ch in L
           if ord(ch) > 127 and not 0x2500 <= ord(ch) <= 0x257F], [])
    check("P2 has a box row",
          all(any(L.startswith("\u2502 ") for L in c.lines) for c in p2), True)
    check("P2 has a tree line",
          all(any(L.startswith(("\u251c\u2500\u2500 ", "\u2514\u2500\u2500 "))
                  for L in c.lines) for c in p2), True)
    p3 = [c for c in plan if c.cls == "P3"]
    check("P3 is an ascii box",
          all(sum(1 for L in c.lines if L.startswith("+")) == 2 for c in p3),
          True)
    p4 = [c for c in plan if c.cls == "P4"]
    check("P4 arrow count", {sum(1 for L in c.lines if "\u2192" in L)
                             for c in p4}, {2, 3})
    p5 = [c for c in plan if c.cls == "P5"]
    check("P5 key lines end with a colon",
          all(all(L.split()[0].endswith(":")
                  for L in c.lines if L not in REAL_COMMANDS) for c in p5),
          True)
    check("P5 includes the uppercase variant",
          all(any(L.split()[0][:-1].isupper()
                  for L in c.lines if L not in REAL_COMMANDS) for c in p5),
          True)
    h3 = [c for c in plan if c.cls == "H3"]
    check("H3 ends with the bogus line",
          all(c.lines[-1].split()[0] == c.head for c in h3), True)
    check("H3 opens with table rows",
          all(c.lines[0].startswith("|") for c in h3), True)
    check("H1/H4/H5 head is the first token",
          all(c.lines[0].split()[0] == c.head
              for c in plan if c.cls in ("H1", "H4", "H5")), True)
    check("H2 head is the piped segment",
          all(c.lines[0].split()[2] == c.head
              for c in plan if c.cls == "H2"), True)

    # generator rejection branches
    check("token: shape rejected",
          value(lambda: make_token(random.Random(0), set(),
                                   draw=draw_seq(["A", "zq", "molvat"]),
                                   which=which_none)), "molvat")
    check("token: taken rejected",
          value(lambda: make_token(random.Random(0), {"molvat"},
                                   draw=draw_seq(["molvat", "bandor42"]),
                                   which=which_none)), "bandor42")
    check("token: reserved word rejected",
          value(lambda: make_token(random.Random(0), set(),
                                   draw=draw_seq(["esac", "molvat"]),
                                   which=which_none)), "molvat")
    check("token: which hit rejected",
          value(lambda: make_token(
              random.Random(0), set(),
              draw=draw_seq(["molvat", "trel-quosk"]),
              which=lambda t: "/usr/bin/x" if t == "molvat" else None)),
          "trel-quosk")
    check("token: exhaustion raises",
          raises(lambda: make_token(random.Random(0), set(),
                                    draw=draw_seq(["esac"] * MAX_DRAWS),
                                    which=which_none), RuntimeError), True)
    check("dirname: collision rejected",
          value(lambda: new_dirname(
              random.Random(0), {"skill-00000001"},
              draw=draw_seq(["skill-00000001", "skill-00000002"]))),
          "skill-00000002")
    check("dirname: exhaustion raises",
          raises(lambda: new_dirname(
              random.Random(0), {"skill-00000001"},
              draw=draw_seq(["skill-00000001"] * MAX_DRAWS)), RuntimeError),
          True)

    # json status parsing
    check("parse: valid",
          parse_status(json.dumps({"checks": [
              {"id": CHECK_ID, "status": "PASS", "detail": "d"}]})),
          ("PASS", "d"))
    check("parse: other check ignored",
          parse_status(json.dumps({"checks": [
              {"id": "x", "status": "PASS"}]})), None)
    check("parse: invalid json", parse_status("not json"), None)
    check("parse: empty output", parse_status(""), None)
    check("parse: non-dict document", parse_status("[]"), None)
    check("parse: checks not a list", parse_status('{"checks": 7}'), None)
    check("parse: status not a string",
          parse_status(json.dumps({"checks": [
              {"id": CHECK_ID, "status": 1}]})), None)
    check("parse: missing detail",
          parse_status(json.dumps({"checks": [
              {"id": CHECK_ID, "status": "FAIL"}]})), ("FAIL", ""))
    check("parse: detail not a string",
          parse_status(json.dumps({"checks": [
              {"id": CHECK_ID, "status": "FAIL", "detail": None}]})),
          ("FAIL", ""))
    check("parse: non-dict entry skipped",
          parse_status(json.dumps({"checks": [
              "x", {"id": CHECK_ID, "status": "N/A"}]})), ("N/A", ""))

    # verdicts
    pcase = [c for c in plan if c.expect == "PASS"][0]
    hcase = [c for c in plan if c.expect == "FAIL"][0]
    check("verdict: pass on PASS", case_correct(pcase, ("PASS", "")), True)
    check("verdict: pass on FAIL", case_correct(pcase, ("FAIL", "")), False)
    check("verdict: pass on N/A", case_correct(pcase, ("N/A", "")), False)
    check("verdict: pass on unparseable", case_correct(pcase, None), False)
    check("verdict: negative on FAIL with its head",
          case_correct(hcase, ("FAIL", "line 9: %r does not resolve"
                               % hcase.head)), True)
    check("verdict: negative on FAIL without its head",
          case_correct(hcase, ("FAIL", "line 9: 'otherbin' does not resolve")),
          False)
    check("verdict: negative on PASS", case_correct(hcase, ("PASS", hcase.head)),
          False)
    check("verdict: negative on unparseable", case_correct(hcase, None), False)

    # output formatting
    check("wrong line",
          wrong_line(Case(seed=11, cls="H1", dirname="skill-1a2b3c4d",
                          desc="", info="", lines=(), expect="FAIL",
                          head="molvat", tokens=()), ("FAIL", "")),
          "wrong 11 H1 skill-1a2b3c4d status=FAIL")
    check("wrong line on unparseable",
          wrong_line(Case(seed=11, cls="P1", dirname="skill-1a2b3c4d",
                          desc="", info="", lines=(), expect="PASS",
                          head=None, tokens=()), None),
          "wrong 11 P1 skill-1a2b3c4d status=unparseable")

    # predicate arithmetic
    check("predicate: met", predicate_ok(120, 120), True)
    check("predicate: one wrong fails", predicate_ok(119, 120), False)
    check("predicate: fewer than 120 fails", predicate_ok(119, 119), False)
    check("predicate: zero fails", predicate_ok(0, 0), False)
    check("predicate: more than 120 holds", predicate_ok(150, 150), True)
    check("predicate: extra wrong fails", predicate_ok(149, 150), False)

    # usage guards
    check("rev: missing", value(lambda: bool(rev_problem(None))), True)
    check("rev: short hash", value(lambda: bool(rev_problem("abc1234"))), True)
    check("rev: 39 hex", value(lambda: bool(rev_problem("a" * 39))), True)
    check("rev: 41 hex", value(lambda: bool(rev_problem("a" * 41))), True)
    check("rev: non-hex", value(lambda: bool(rev_problem("g" * 40))), True)
    check("rev: 40 hex", rev_problem("a" * 40), None)
    check("rev: uppercase 40 hex", rev_problem("A" * 40), None)
    check("conflict: self-test alone", usage_conflict(True, None, None), None)
    check("conflict: self-test with rev",
          bool(usage_conflict(True, "a" * 40, None)), True)
    check("conflict: self-test with seed",
          bool(usage_conflict(True, None, [11])), True)
    check("conflict: measured run", usage_conflict(False, "a" * 40, [11]), None)

    # git plumbing and extraction, with injected runners
    check("resolve: ok",
          resolve_rev(".", "a" * 40,
                      run=fake_git(0, ("b" * 40 + "\n").encode())), "b" * 40)
    check("resolve: git failure raises",
          raises(lambda: resolve_rev(".", "a" * 40,
                                     run=fake_git(1, ("b" * 40).encode())),
                 EnvError), True)
    check("resolve: non-hex output raises",
          raises(lambda: resolve_rev(".", "a" * 40, run=fake_git(0, b"abc\n")),
                 EnvError), True)
    check("resolve: empty output raises",
          raises(lambda: resolve_rev(".", "a" * 40, run=fake_git(0, b"")),
                 EnvError), True)
    check("archive: ok",
          archive_verifiers(".", "a" * 40, run=fake_git(0, b"TARDATA")),
          b"TARDATA")
    check("archive: failure raises",
          raises(lambda: archive_verifiers(".", "a" * 40,
                                           run=fake_git(1, b"")), EnvError),
          True)
    good_tar = make_tar([(INSTRUMENT, b"print(1)\n"),
                         ("verifiers/sub/other.py", b"x")])
    with tempfile.TemporaryDirectory(prefix="infoless-self-") as td:
        extract_tar(good_tar, Path(td))
        check("extract: instrument present",
              require_instrument(Path(td)) == Path(td) / INSTRUMENT, True)
        check("extract: nested member",
              (Path(td) / "verifiers/sub/other.py").read_bytes(), b"x")
        with tempfile.TemporaryDirectory(prefix="infoless-self2-") as td2:
            extract_tar(make_tar([("verifiers/README.md", b"")]), Path(td2))
            check("extract: missing instrument raises",
                  raises(lambda: require_instrument(Path(td2)), EnvError), True)
    check("tools: present", require_tools(lambda t: "/usr/bin/" + t), None)
    check("tools: missing raises",
          raises(lambda: require_tools(lambda t: None), EnvError), True)

    # own bytes, read through a path
    with tempfile.TemporaryDirectory(prefix="infoless-sha-") as td:
        p = Path(td) / "counter.py"
        p.write_bytes(b"abc")
        check("sha: own bytes", own_sha(p),
              hashlib.sha256(b"abc").hexdigest())
        check("sha: unreadable raises",
              raises(lambda: own_sha(Path(td) / "absent.py"), EnvError), True)

    # the frozen per-case command, through an injected runner
    with tempfile.TemporaryDirectory(prefix="infoless-run-") as td:
        work = Path(td)
        seen = {}

        def pass_runner(argv, cwd, env):
            seen["argv"], seen["cwd"], seen["env"] = argv, cwd, env
            return subprocess.CompletedProcess(argv, 0, json.dumps({"checks": [
                {"id": CHECK_ID, "status": "PASS", "detail": "ok"}]}), "")

        parsed = run_case(pcase, work / "tree", work,
                          {"PYTHONSAFEPATH": "1"}, runner=pass_runner)
        check("runner: parsed status", parsed, ("PASS", "ok"))
        check("runner: frozen argv", seen["argv"],
              ["timeout", "60", "python3", "-B", "-P",
               str(work / "tree" / INSTRUMENT),
               "--repo", str(work / "cases" / pcase.dirname),
               "--skill", str(work / "cases" / pcase.dirname / "SKILL.md"),
               "--check", CHECK_ID, "--json"])
        check("runner: empty cwd", list(seen["cwd"].iterdir()), [])
        check("runner: PYTHONSAFEPATH", seen["env"].get("PYTHONSAFEPATH"), "1")
        check("runner: SKILL.md written",
              (work / "cases" / pcase.dirname / "SKILL.md").is_file(), True)
        check("runner: skill bytes are the rendered case",
              (work / "cases" / pcase.dirname / "SKILL.md")
              .read_text(encoding="utf-8"), render_skill(pcase))

        def timeout_runner(argv, cwd, env):
            raise subprocess.TimeoutExpired(argv, CASE_TIMEOUT)

        check("runner: timeout is a wrong case",
              run_case(pcase, work / "tree", work,
                       {"PYTHONSAFEPATH": "1"}, runner=timeout_runner), None)
        check("runner: empty output is a wrong case",
              run_case(pcase, work / "tree", work, {"PYTHONSAFEPATH": "1"},
                       runner=lambda a, c, e: subprocess.CompletedProcess(
                           a, 124, "", "")), None)

    # measure() propagates an environment failure; guarded() maps it to exit 2
    check("measure: git failure raises",
          raises(lambda: measure(".", "a" * 40, [11], run=fake_git(1, b"")),
                 EnvError), True)

    def boom():
        raise EnvError("x")

    check("guarded: success is exit 0",
          guarded(lambda: 7, report=lambda m: None), (0, 7))
    check("guarded: env failure is exit 2",
          value(lambda: guarded(boom, report=lambda m: None)[0]), 2)
    check("guarded: env failure drops the value",
          value(lambda: guarded(boom, report=lambda m: None)[1]), None)

    print("self-test: %d failure(s) over %d assertions" % (failures, assertions))
    return 1 if failures else 0


# ----------------------------------------------------------------------- main
def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--rev", metavar="REV",
                    help="full 40-hex commit hash to measure")
    ap.add_argument("--seed", action="extend", nargs="+", type=int,
                    metavar="N", help="seed(s); default 11 22 33")
    ap.add_argument("--repo", metavar="DIR",
                    help="git repository (default: the parent of this file's "
                         "directory)")
    ap.add_argument("--self-test", action="store_true",
                    help="run the hermetic arms and exit")
    args = ap.parse_args(argv)
    code, sha = guarded(own_sha)
    if sha is None:
        return code
    print("counter sha256 %s" % sha)
    conflict = usage_conflict(args.self_test, args.rev, args.seed)
    if conflict:
        ap.error(conflict)
    if args.self_test:
        return self_test()
    problem = rev_problem(args.rev)
    if problem:
        ap.error(problem)
    repo = (Path(args.repo).expanduser() if args.repo
            else Path(__file__).resolve().parent.parent)
    seeds = list(args.seed) if args.seed else list(DEFAULT_SEEDS)
    code, result = guarded(lambda: measure(repo, args.rev, seeds))
    if result is None:
        return code
    full, instrument_sha, cases, tallies, wrong = result
    print("measured %s" % full)
    print("instrument sha256 %s" % instrument_sha)
    total = len(cases)
    correct = sum(pair[0] for pair in tallies.values())
    print("info-less fence cases correct %d of %d (pass-expected %d of %d; "
          "hard negatives %d of %d)"
          % (correct, total, tallies["PASS"][0], tallies["PASS"][1],
             tallies["FAIL"][0], tallies["FAIL"][1]))
    for line in wrong:
        print(line)
    return 0 if predicate_ok(correct, total) else 1


if __name__ == "__main__":
    sys.exit(main())
