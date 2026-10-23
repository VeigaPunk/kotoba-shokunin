#!/usr/bin/env python3
r"""Round-57 C2 operability counter, v2 (pre-data erratum; supersedes v1).

THE FROZEN SPEC v2 (written 2026-10-23 before any content it scores; the L1
commits this file with the round plan):

1. `check_infoless_fences_v2.py --rev <40-hex> [--seed N ...]` (default seeds
   11 22 33).  Extract the measured revision's `verifiers/` tree into a fresh
   temp dir per run; run ONLY that copy, never the working tree.  The run
   root, the extraction dir, the case-root dir, every per-case cwd dir and
   every probe dir get names drawn from the one token generator (no fixed
   prefix, no fixed `tree` name).  Case dir names, frontmatter `name:`,
   heading text and description are drawn from that same generator (varied
   shapes), and every case carries 0-2 random prose lines before and after
   its fence.
2. Per seed, generate cases with `random.Random(seed)`; tokens are 1-2
   pronounceable lowercase chunks of 3-8 letters, optionally joined by `-`
   or followed by 1-3 digits; a token for which `shutil.which` resolves, or
   that is a shell keyword/builtin, is rejected and redrawn -- the same rule
   for every token class.  Shuffle case order.  Each case gets its own fresh
   dir holding `SKILL.md` = frontmatter + short heading + ONE fenced block.
   Every case (pass-expected AND hard negative) holds 1-2 real command lines
   at random positions, drawn per case from a pool of common binaries
   filtered by `shutil.which`, with flag-only arguments; a pool line is used
   only after a preflight probe shows it PASSes alone on the measured
   instrument -- no fixed literal line.
3. Classes, 4 cases per class per seed:
   PASS-expected (fence has NO info string; correct iff status == PASS):
   P1 markdown table; P2 box-drawing diagram (U+2500-U+257F) and tree lines;
   P3 ascii box; P4 arrow line (U+2192) `tok tok (tok)    -> tok/tok.json`;
   P5 key: value output (first whitespace token ends with `:`, uppercase
   variant included).
   FAIL-expected hard negatives (correct iff status == FAIL, the check's
   detail contains the instrument's exact subject form
   `line <n>: '<head>'` for that case's bogus head at its real 1-based
   SKILL.md line number, no OTHER line number of the case appears as a
   failing subject, no `... (+N more)` truncation marker is present, and the
   detail is at most 300 bytes once that exact subject form is removed):
   H1 `<bogus> --<tok>`; H2 `ls | <bogus>`; H3 P1 table rows then
   `<bogus> <tok>` on its own line; H4 `<bogus> --opt=<tok>:<tok>`;
   H5 shell-tagged fence (```bash) `<bogus> <tok>`;
   H6 info-less fence `<bogus> +<tok>` (a `+` argument);
   H7 info-less fence `<bogus> --name=<tok>é<tok>` (non-ASCII inside an
   argument); H8 info-less fence `<bogus> "<tok> → <tok>"` (U+2192 only
   inside double quotes).
4. Per case, randomly pick the invocation mode:
   `--check trigger.command_binary_resolves --json`, or full `--json` with
   no `--check`; the check's status is read from the JSON either way.
5. Twin arm: per seed, every hard negative and 4 pass cases are re-run from
   a second, freshly named dir with regenerated frontmatter, heading and
   prose (the fence body is reused).  A twin is correct iff its class rule
   holds AND its status equals its primary's observed status.  Twins count
   in T (default T = 264 = 3 seeds x (13 classes x 4 + 32 H twins + 4 P
   twins), floor T >= 120).
6. Diff guard: diff `verifiers/verify_skill_checklist.py` at base
   `47c05558fa4e6043e45c7abca1fb5fd2fb8cda5a` against the measured
   revision; count ADDED lines matching (case-insensitive)
   `/proc|getppid|os\.environ|getenv|pythonsafepath|safe_path|
   check_infoless|sys\.argv|ls -la|git --version|import random|random\.|
   seed\(|getcwd|tempfile|mkdtemp|gettempdir|__file__|parent\.name|infoless|
   kotoba` (bare `tree`, `tmp`, `random`, `seed`, `environ` are words, not
   tells, and are deliberately absent), print
   `instrument diff guard: K suspicious added line(s)` and each line.
   Predicate (frozen): exit 0 iff N == T and T >= 120 and K == 0; else 1;
   2 on usage/env error.
7. `--self-test`: hermetic in-process arms for every rule and every
   rejection guard (the v2 guard-mutation kill table is in the w0 receipt).
8. First output line is `counter sha256 <hex>` read from this file's own
   bytes via `__file__`; a measured run then prints `measured <rev>`,
   `instrument sha256 <hex>` of the extracted, executed copy, the diff-guard
   line and the pool-preflight line.

Implementation notes, stated only as far as the code goes:

  * The repo is `--repo` when given, else the parent of this file's directory.
    `--rev` is resolved with `git -C <repo> rev-parse --verify <rev>^{commit}`.
  * `git archive --format=tar <full-rev> verifiers` is extracted with the
    stdlib `tarfile` module; only `<tmp>/verifiers/verify_skill_checklist.py`
    is executed.  The pool preflight and every case use the same extracted
    copy.
  * The spec's `timeout 60` is the coreutils wrapper; a 70 s subprocess
    backstop guards a stuck wrapper.  `python3` and `timeout` must be on PATH.
  * An unparseable --json output or a timeout is a wrong case; its wrong line
    prints `status=unparseable`.
  * Exit 2, with no traceback, on: missing or malformed `--rev`, a git
    failure, no instrument in the extracted tree, a missing tool, an
    unreadable own file, a pool with fewer than 2 usable lines.  `--self-test`
    cannot be combined with `--rev` / `--seed`.
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
CLASSES = (
    ("P1", "PASS"), ("P2", "PASS"), ("P3", "PASS"), ("P4", "PASS"),
    ("P5", "PASS"), ("H1", "FAIL"), ("H2", "FAIL"), ("H3", "FAIL"),
    ("H4", "FAIL"), ("H5", "FAIL"), ("H6", "FAIL"), ("H7", "FAIL"),
    ("H8", "FAIL"),
)
HARD_CLASSES = sum(1 for _, expect in CLASSES if expect == "FAIL")
TWINS_PER_SEED = 4
EXPECTED_TOTAL = len(DEFAULT_SEEDS) * (
    len(CLASSES) * CASES_PER_CLASS + HARD_CLASSES * CASES_PER_CLASS
    + TWINS_PER_SEED)  # 192
MIN_TOTAL = 120
CASE_TIMEOUT = 60
MAX_DRAWS = 1000
MAX_DETAIL_BYTES = 300
CHECK_ID = "trigger.command_binary_resolves"
INSTRUMENT = "verifiers/verify_skill_checklist.py"
BASE_REV = "47c05558fa4e6043e45c7abca1fb5fd2fb8cda5a"
TOOLS = ("python3", "timeout")
FULL_REV_RE = re.compile(r"^[0-9a-fA-F]{40}$")
TOKEN_RE = re.compile(r"^[a-z]{3,8}(?:-[a-z]{3,8})?[0-9]{0,3}$")
SUSPICIOUS_RE = re.compile(
    r"/proc|getppid|os\.environ|getenv|pythonsafepath|safe_path|"
    r"check_infoless|sys\.argv|ls -la|git --version|import random|random\.|"
    r"seed\(|getcwd|tempfile|mkdtemp|gettempdir|__file__|parent\.name|"
    r"infoless|kotoba", re.I)
FENCE_RE = re.compile(r"^```")
LINE_NO_RE = re.compile(r"line (\d+):")
CONSONANTS = "bcdfghjklmnprstvwz"
VOWELS = "aeiou"
RESERVED = frozenset("""
if for while until case do done then else elif fi esac in
echo cd pwd export unset read local return exit printf set test
true false wait ulimit umask type hash getopts let declare
typeset readonly break continue times dirs jobs fg bg
kill disown suspend logout enable alias unalias fc history
sudo env command nohup time builtin xargs source exec
""".split())
# Common binaries with flag-only arguments.  Every line was verified to PASS
# alone on the base instrument; the pool preflight re-verifies each run.
POOL_LINES = (
    "ls -la", "cat -n", "grep -i", "sort -r", "head -n 5", "tail -n 5",
    "wc -l", "git --version", "find -name", "sed -n", "awk -F", "date -u",
    "uname -a", "cut -f 1", "tr -d", "basename -a", "dirname -z", "stat -c",
    "du -s", "id -u",
)

Case = namedtuple(
    "Case", "seed cls dirname desc heading prose_before prose_after info "
            "lines expect head head_index mode kind primary tokens commands")


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


def git_show(repo, rev, path, run=git_run):
    """A textual blob at `rev`; EnvError when git cannot read it."""
    r = run(repo, ["show", "%s:%s" % (rev, path)])
    if r.returncode != 0:
        raise EnvError(
            "git show %s:%s failed in %s (exit %d): %s"
            % (rev, path, repo, r.returncode,
               r.stderr.decode("utf-8", "replace").strip()[:300]))
    return r.stdout.decode("utf-8", "replace")


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


def suspicious_added(old_text, new_text, pattern=SUSPICIOUS_RE):
    """Added lines of the base->measured diff that match the guard pattern."""
    import difflib
    added = [line[1:] for line in difflib.unified_diff(
        old_text.splitlines(), new_text.splitlines(), n=0, lineterm="")
        if line.startswith("+") and not line.startswith("+++")]
    return [line for line in added if pattern.search(line)]


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


class TempNamer:
    """Temp-directory names drawn from the one generator, never a fixed word."""

    def __init__(self, rng=None, which=shutil.which):
        self.rng = rng or random.Random(int.from_bytes(os.urandom(8), "big"))
        self.which = which
        self.taken = set()

    def name(self):
        word = make_token(self.rng, self.taken, which=self.which)
        self.taken.add(word)
        return word

    def mkdtemp(self, parent=None):
        return Path(tempfile.mkdtemp(
            prefix=self.name() + "-",
            dir=None if parent is None else str(parent)))


# ------------------------------------------------------------------ case shapes
def prose_line(rng, tok):
    words = [tok() for _ in range(rng.randint(2, 4))]
    words[0] = words[0].capitalize()
    return " ".join(words) + "."


def insert_commands(rng, lines, head_index, pool):
    """1-2 pool command lines at random positions; shift the head index."""
    out = list(lines)
    for line in rng.sample(list(pool), rng.randint(1, 2)):
        pos = rng.randint(0, len(out))
        out.insert(pos, line)
        if head_index is not None and pos <= head_index:
            head_index += 1
    return out, head_index


def table_rows(rng, tok):
    rows = ["| %s | %s |" % (tok(), tok()),
            rng.choice(("|---|---|", "|---|:---:|", "|:--|--:|"))]
    for _ in range(rng.randint(2, 3)):
        rows.append("| %s | %s |" % (tok(), tok()))
    return rows


def case_p1(rng, tok):
    return table_rows(rng, tok), None, None


def case_p2(rng, tok):
    lines = ["\u250c\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2510",
             "\u2502 %s \u2502" % tok(),
             "\u2514\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2518"]
    for _ in range(rng.randint(1, 2)):
        lines.append("%s\u2500\u2500 %s" % (rng.choice(("\u251c", "\u2514")),
                                           tok()))
    return lines, None, None


def case_p3(rng, tok):
    return ["+------+", "| %s |" % tok(), "+------+"], None, None


def case_p4(rng, tok):
    lines = []
    for _ in range(rng.randint(2, 3)):
        lines.append("%s %s (%s)    \u2192 %s/%s.json"
                     % (tok(), tok(), tok(), tok(), tok()))
    return lines, None, None


def case_p5(rng, tok):
    lines = ["%s: %s" % (tok().upper(), tok())]
    for _ in range(rng.randint(1, 2)):
        if rng.random() < 0.5:
            lines.append("%s: %s" % (tok().upper(), tok()))
        else:
            lines.append("%s:   %s/%s" % (tok(), tok(), tok()))
    return lines, None, None


def case_h1(rng, tok):
    head = tok()
    return ["%s --%s" % (head, tok())], head, 0


def case_h2(rng, tok):
    head = tok()
    return ["ls | %s" % head], head, 0


def case_h3(rng, tok):
    head = tok()
    rows = table_rows(rng, tok)
    rows.append("%s %s" % (head, tok()))
    return rows, head, len(rows) - 1


def case_h4(rng, tok):
    head = tok()
    return ["%s --opt=%s:%s" % (head, tok(), tok())], head, 0


def case_h5(rng, tok):
    head = tok()
    return ["%s %s" % (head, tok())], head, 0


def case_h6(rng, tok):
    head = tok()
    return ["%s +%s" % (head, tok())], head, 0


def case_h7(rng, tok):
    head = tok()
    return ["%s --name=%s\u00e9%s" % (head, tok(), tok())], head, 0


def case_h8(rng, tok):
    head = tok()
    return ['%s "%s \u2192 %s"' % (head, tok(), tok())], head, 0


BUILDERS = {"P1": case_p1, "P2": case_p2, "P3": case_p3, "P4": case_p4,
            "P5": case_p5, "H1": case_h1, "H2": case_h2, "H3": case_h3,
            "H4": case_h4, "H5": case_h5, "H6": case_h6, "H7": case_h7,
            "H8": case_h8}


# ---------------------------------------------------------------------- plan
def build_case(rng, seed, cls, expect, info, kind, taken, pool, which,
               body=None, head=None, head_index=None, primary=None):
    drawn = set()

    def tok():
        word = make_token(rng, drawn, which=which)
        drawn.add(word)
        return word

    dirname = make_token(rng, taken | drawn, which=which)
    drawn.add(dirname)
    taken.add(dirname)
    desc = " ".join(tok() for _ in range(rng.randint(3, 6)))
    heading = " ".join(tok() for _ in range(rng.randint(1, 2)))
    prose_before = [prose_line(rng, tok) for _ in range(rng.randint(0, 2))]
    prose_after = [prose_line(rng, tok) for _ in range(rng.randint(0, 2))]
    mode = "check" if rng.random() < 0.5 else "full"
    if body is None:
        lines, head, head_index = BUILDERS[cls](rng, tok)
        lines, head_index = insert_commands(rng, lines, head_index, pool)
    else:
        lines = list(body)
    poolset = set(pool)
    return Case(seed=seed, cls=cls, dirname=dirname, desc=desc, heading=heading,
                prose_before=prose_before, prose_after=prose_after, info=info,
                lines=list(lines), expect=expect, head=head,
                head_index=head_index, mode=mode, kind=kind, primary=primary,
                tokens=tuple(drawn),
                commands=tuple(L for L in lines if L in poolset))


def plan_cases(seeds, pool, which=shutil.which):
    """Primaries (shuffled per seed) then their twins; tokens drawn once."""
    cases = []
    taken_names = set()
    for seed in seeds:
        rng = random.Random(seed)
        block = []
        for cls, expect in CLASSES:
            info = "bash" if cls == "H5" else ""
            for _ in range(CASES_PER_CLASS):
                block.append(build_case(rng, seed, cls, expect, info,
                                        "primary", taken_names, pool, which))
        rng.shuffle(block)
        twins = [build_case(rng, seed, c.cls, c.expect, c.info, "twin",
                            taken_names, pool, which, body=c.lines,
                            head=c.head, head_index=c.head_index, primary=c)
                 for c in block if c.expect == "FAIL"]
        twins += [build_case(rng, seed, c.cls, c.expect, c.info, "twin",
                             taken_names, pool, which, body=c.lines,
                             head=c.head, head_index=c.head_index, primary=c)
                  for c in rng.sample([c for c in block if c.expect == "PASS"],
                                      TWINS_PER_SEED)]
        rng.shuffle(twins)
        cases.extend(block)
        cases.extend(twins)
    return cases


def preamble(case):
    """Every SKILL.md line before the fence content."""
    return (["---", "name: %s" % case.dirname, "description: %s" % case.desc,
             "---", "", "# %s" % case.heading]
            + list(case.prose_before) + [""] + ["```" + case.info])


def render_skill(case):
    """frontmatter + heading + prose + exactly one fenced block + prose."""
    return "\n".join(preamble(case) + list(case.lines) + ["```"]
                     + list(case.prose_after) + [""])


def head_line(case):
    """The 1-based SKILL.md line of the case's bogus head."""
    return len(preamble(case)) + case.head_index + 1


def head_subject(case):
    """The instrument's exact failing-subject form for the head."""
    return "line %d: %r" % (head_line(case), case.head)


# -------------------------------------------------------------------- running
def default_runner(argv, cwd, env):
    return subprocess.run(argv, cwd=str(cwd), env=env, capture_output=True,
                          text=True, timeout=CASE_TIMEOUT + 10)


def run_case(case, tree, workdir, env, runner=None, namer=None):
    """The case's status tuple, or None when the output is untrustworthy."""
    namer = namer or TempNamer()
    casedir = Path(workdir) / case.dirname
    casedir.mkdir(parents=True, exist_ok=True)
    (casedir / "SKILL.md").write_text(render_skill(case), encoding="utf-8")
    cwd = namer.mkdtemp()
    argv = ["timeout", str(CASE_TIMEOUT), "python3", "-B", "-P",
            str(Path(tree) / INSTRUMENT)]
    if case.mode == "check":
        argv += ["--check", CHECK_ID]
    argv += ["--repo", str(casedir), "--skill", str(casedir / "SKILL.md"),
             "--json"]
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
    if status != "FAIL":
        return False
    if "… (+" in detail:
        return False
    subject = head_subject(case)
    if subject not in detail:
        return False
    if len(detail.replace(subject, "").encode("utf-8")) > MAX_DETAIL_BYTES:
        return False
    seen = {int(n) for n in LINE_NO_RE.findall(detail)}
    return seen == {head_line(case)}


def twin_correct(case, parsed, primary_parsed):
    """A twin must satisfy its class rule and repeat its primary's status."""
    if parsed is None or primary_parsed is None:
        return False
    return case_correct(case, parsed) and parsed[0] == primary_parsed[0]


def wrong_line(case, parsed):
    status = parsed[0] if parsed is not None else "unparseable"
    return "wrong %d %s %s status=%s" % (case.seed, case.cls, case.dirname,
                                         status)


def predicate_ok(correct, total, suspicious):
    """The frozen predicate: every case correct, floor met, no diff guard hit."""
    return correct == total and total >= MIN_TOTAL and suspicious == 0


def usable_pool(lines, which, probe):
    """The pool lines that resolve and PASS alone; EnvError below two."""
    out = [line for line in lines if which(line.split()[0]) and probe(line)]
    if len(out) < 2:
        raise EnvError("only %d usable real command line(s): %s"
                       % (len(out), ", ".join(out) or "none"))
    return tuple(out)


def probe_case(line, index):
    """A minimal single-fence case used to verify one pool line."""
    return Case(seed=0, cls="probe", dirname="probe%s" % make_token(
        random.Random(index + 1), set(), which=lambda t: None),
                desc="probe", heading="Probe", prose_before=[], prose_after=[],
                info="", lines=[line], expect="PASS", head=None,
                head_index=None, mode="check", kind="probe", primary=None,
                tokens=(), commands=(line,))


def preflight_pool(tree, work, env, which=shutil.which, runner=None,
                   namer=None):
    """Verify every pool line PASSes alone on the measured instrument."""
    namer = namer or TempNamer()
    workdir = namer.mkdtemp(parent=work)

    def probe(line):
        parsed = run_case(probe_case(line, POOL_LINES.index(line)),
                          tree, workdir, env, runner=runner, namer=namer)
        return parsed is not None and parsed[0] == "PASS"

    return usable_pool(POOL_LINES, which, probe)


# ------------------------------------------------------------------- measure
def measure(repo, rev, seeds, which=shutil.which, run=git_run, runner=None,
            namer=None):
    """(rev, instrument sha, suspicious, pool, cases, tallies, wrong lines)."""
    full = resolve_rev(repo, rev, run=run)
    require_tools(which)
    namer = namer or TempNamer(which=which)
    old_text = git_show(repo, BASE_REV, INSTRUMENT, run=run)
    with tempfile.TemporaryDirectory(prefix=namer.name() + "-") as td:
        work = Path(td)
        tree = namer.mkdtemp(parent=work)
        extract_tar(archive_verifiers(repo, full, run=run), tree)
        instrument = require_instrument(tree)
        instrument_sha = hashlib.sha256(instrument.read_bytes()).hexdigest()
        suspicious = suspicious_added(
            old_text, instrument.read_text(encoding="utf-8", errors="replace"))
        env = dict(os.environ)
        env["PYTHONSAFEPATH"] = "1"
        pool = preflight_pool(tree, work, env, which=which, runner=runner,
                              namer=namer)
        cases = plan_cases(seeds, pool, which=which)
        casedir = namer.mkdtemp(parent=work)
        parsed = {}
        for case in cases:
            if case.kind != "twin":
                parsed[id(case)] = run_case(case, tree, casedir, env,
                                            runner=runner, namer=namer)
        for case in cases:
            if case.kind == "twin":
                parsed[id(case)] = run_case(case, tree, casedir, env,
                                            runner=runner, namer=namer)
        tallies = {"PASS": [0, 0], "FAIL": [0, 0]}
        wrong = []
        for case in cases:
            result = parsed[id(case)]
            tallies[case.expect][1] += 1
            if case.kind == "twin":
                good = twin_correct(case, result,
                                    parsed[id(case.primary)])
            else:
                good = case_correct(case, result)
            if good:
                tallies[case.expect][0] += 1
            else:
                wrong.append(wrong_line(case, result))
    return full, instrument_sha, suspicious, pool, cases, tallies, wrong


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
    check("class count", len(CLASSES), 13)
    check("cases per class", CASES_PER_CLASS, 4)
    check("twins per seed", TWINS_PER_SEED, 4)
    check("expected total", EXPECTED_TOTAL, 264)
    check("frozen minimum", MIN_TOTAL, 120)
    check("pool size", len(POOL_LINES), 20)
    check("pool args are flag-only",
          [t for line in POOL_LINES for t in line.split()[1:]
           if not t.startswith("-") and not t.isdigit()], [])
    selftest_pool = ("ls -la", "git --version")
    plan = plan_cases(DEFAULT_SEEDS, selftest_pool)
    check("planned total", len(plan), EXPECTED_TOTAL)
    counts = {}
    for c in plan:
        if c.kind == "primary":
            counts[(c.seed, c.cls)] = counts.get((c.seed, c.cls), 0) + 1
    check("every (seed, class) has 4 primaries",
          (len(counts), sorted(set(counts.values()))), (39, [4]))
    check("kind counts",
          (sum(1 for c in plan if c.kind == "primary"),
           sum(1 for c in plan if c.kind == "twin")), (156, 108))
    check("twins follow their seed's primaries",
          all(max(i for i, c in enumerate(plan)
                  if c.seed == s and c.kind == "primary")
              < min(i for i, c in enumerate(plan)
                    if c.seed == s and c.kind == "twin")
              for s in DEFAULT_SEEDS), True)
    check("dirname uniqueness",
          len({c.dirname for c in plan}), len(plan))
    check("dirname drawn from the generator",
          {t for c in plan for t in c.tokens if c.dirname == t} != set(), True)
    check("dirname shape", {bool(TOKEN_RE.match(c.dirname)) for c in plan},
          {True})
    check("no fixed dirname prefix",
          [c.dirname for c in plan if c.dirname.startswith("skill-")], [])
    check("plan determinism per seed",
          plan_cases(DEFAULT_SEEDS, selftest_pool), plan)
    canonical = [cls for cls, _ in CLASSES for _ in range(CASES_PER_CLASS)]
    check("shuffle changes every seed block",
          sum(1 for s in DEFAULT_SEEDS
              if [c.cls for c in plan
                  if c.seed == s and c.kind == "primary"] != canonical),
          len(DEFAULT_SEEDS))
    check("twins are 32 H + 4 P per seed",
          {s: (sum(1 for c in plan if c.seed == s and c.kind == "twin"
                   and c.expect == "FAIL"),
               sum(1 for c in plan if c.seed == s and c.kind == "twin"
                   and c.expect == "PASS")) for s in DEFAULT_SEEDS},
          {s: (32, 4) for s in DEFAULT_SEEDS})
    check("twin body equals its primary's",
          all(c.lines == c.primary.lines and c.head == c.primary.head
              and c.head_index == c.primary.head_index
              for c in plan if c.kind == "twin"), True)
    check("twin name differs from its primary",
          [c for c in plan if c.kind == "twin"
           and c.dirname == c.primary.dirname], [])
    check("twin frontmatter regenerated",
          [c for c in plan if c.kind == "twin"
           and (c.desc, c.heading) == (c.primary.desc, c.primary.heading)], [])
    check("both invocation modes appear",
          sorted({c.mode for c in plan}), ["check", "full"])

    # one fence, prose only outside it, frontmatter names the dir
    rendered = [(c, render_skill(c)) for c in plan]
    check("exactly one fenced block per case",
          {sum(1 for L in r.splitlines() if FENCE_RE.match(L))
           for _, r in rendered}, {2})
    check("fence info strings", sorted({c.info for c in plan}), ["", "bash"])
    check("frontmatter name is the dirname",
          all(r.splitlines()[1] == "name: " + c.dirname for c, r in rendered),
          True)
    check("prose counts stay 0-2 and sit outside the fence",
          {("prose", len(c.prose_before), len(c.prose_after)) for c in plan
           if not 0 <= len(c.prose_before) <= 2
           or not 0 <= len(c.prose_after) <= 2}, set())
    check("prose varies across cases",
          (len({len(c.prose_before) for c in plan}) > 1,
           len({len(c.prose_after) for c in plan}) > 1), (True, True))
    check("rendered line after the fence holds only prose or the closer",
          all(set(r.splitlines()[len(preamble(c)) + len(c.lines) + 1:])
              <= set(c.prose_after) | {""} for c, r in rendered), True)

    # token generator: one source, unresolvable, distinct, reserved-free
    check("every generated token unresolvable",
          [t for c in plan for t in c.tokens if shutil.which(t)], [])
    check("no reserved token", [t for c in plan for t in c.tokens
                                if t in RESERVED], [])
    check("token shape", [t for c in plan for t in c.tokens
                          if not TOKEN_RE.match(t)], [])
    check("tokens distinct within a case",
          all(len(set(c.tokens)) == len(c.tokens) for c in plan), True)

    # 1-2 real commands in EVERY case, at random positions, from the pool
    check("every case holds 1-2 pool commands",
          {len(c.commands) for c in plan}, {1, 2})
    check("commands come from the pool",
          [L for c in plan for L in c.commands if L not in selftest_pool], [])
    check("no fixed literal command",
          len({line for c in plan for line in c.commands}) > 1, True)
    check("commands vary in position",
          len({c.lines.index(c.commands[0]) for c in plan if c.commands}) > 5,
          True)
    check("hard-negative head is a drawn token",
          all(c.head in c.tokens for c in plan
              if c.expect == "FAIL" and c.kind == "primary"), True)

    # head line identity in the rendered file
    for cls in ("H1", "H2", "H3", "H4", "H5", "H6", "H7", "H8"):
        hcases = [c for c in plan if c.cls == cls and c.kind == "primary"]
        want = {c.lines[c.head_index].split()[0] for c in hcases}
        if cls == "H2":
            want = {c.lines[c.head_index].split()[2] for c in hcases}
        check("%s head line is the head line" % cls,
              want, {c.head for c in hcases})
        check("%s rendered line %d starts the head line" % (cls, 0),
              all(render_skill(c).splitlines()[head_line(c) - 1]
                  == c.lines[c.head_index] for c in hcases), True)

    # class shapes
    p1 = [c for c in plan if c.cls == "P1"]
    check("P1 has an alignment row",
          all(any(re.match(r"^\|[-:|]+\|$", L) for L in c.lines)
              for c in p1), True)
    p2 = [c for c in plan if c.cls == "P2"]
    check("P2 box characters stay in U+2500-U+257F",
          [ch for c in p2 for L in c.lines for ch in L
           if ord(ch) > 127 and not 0x2500 <= ord(ch) <= 0x257F], [])
    p3 = [c for c in plan if c.cls == "P3"]
    check("P3 is an ascii box",
          all(sum(1 for L in c.lines if L.startswith("+")) == 2 for c in p3),
          True)
    p4 = [c for c in plan if c.cls == "P4"]
    check("P4 arrow count", {sum(1 for L in c.lines if "\u2192" in L)
                             for c in p4}, {2, 3})
    p5 = [c for c in plan if c.cls == "P5"]
    poolset = set(selftest_pool)
    check("P5 key lines end with a colon",
          all(all(L.split()[0].endswith(":")
                  for L in c.lines if L not in poolset) for c in p5), True)
    check("P5 includes the uppercase variant",
          all(any(L.split()[0][:-1].isupper()
                  for L in c.lines if L not in poolset) for c in p5), True)
    h6 = [c for c in plan if c.cls == "H6" and c.kind == "primary"]
    check("H6 carries a + argument",
          all(" +" in c.lines[c.head_index] for c in h6), True)
    h7 = [c for c in plan if c.cls == "H7" and c.kind == "primary"]
    check("H7 carries a non-ASCII argument",
          all("\u00e9" in c.lines[c.head_index] for c in h7), True)
    h8 = [c for c in plan if c.cls == "H8" and c.kind == "primary"]
    check("H8 carries an arrow inside quotes",
          all(c.lines[c.head_index].count('"') == 2
              and "\u2192" in c.lines[c.head_index] for c in h8), True)
    h3 = [c for c in plan if c.cls == "H3" and c.kind == "primary"]
    h3_body = [[L for L in c.lines if L not in poolset] for c in h3]
    check("H3 opens with table rows",
          all(body[0].startswith("|") for body in h3_body), True)
    check("H3 ends with the bogus line",
          all(body[-1].split()[0] == c.head
              for body, c in zip(h3_body, h3)), True)

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

    # temp names come from the generator, never a fixed word
    namer = TempNamer(rng=random.Random(7), which=which_none)
    first, second = namer.mkdtemp(), namer.mkdtemp()
    check("temp names are generated and unique",
          (first.name != second.name,
           bool(re.match(r"^[a-z]{3,8}(?:-[a-z]{3,8})?[0-9]{0,3}-",
                         first.name)),
           sorted({first.name.startswith("tree"),
                   second.name.startswith("tree")})), (True, True, [False]))
    check("temp dir exists", (first.is_dir(), second.is_dir()), (True, True))
    first.rmdir()
    second.rmdir()

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

    # verdicts: pass cases, exact-form hard negatives, twins
    pcase = [c for c in plan if c.expect == "PASS" and c.kind == "primary"][0]
    hcase = [c for c in plan if c.expect == "FAIL" and c.kind == "primary"][0]
    subject = head_subject(hcase)
    check("verdict: pass on PASS", case_correct(pcase, ("PASS", "")), True)
    check("verdict: pass on FAIL", case_correct(pcase, ("FAIL", "")), False)
    check("verdict: pass on N/A", case_correct(pcase, ("N/A", "")), False)
    check("verdict: pass on unparseable", case_correct(pcase, None), False)
    check("verdict: negative on the exact subject form",
          case_correct(hcase, ("FAIL", "%s (fenced, segment %r) does not "
                               "resolve" % (subject, hcase.head))), True)
    check("verdict: bare containment is not enough",
          case_correct(hcase, ("FAIL", "%s does not resolve" % hcase.head)),
          False)
    check("verdict: body echo is not enough",
          case_correct(hcase, ("FAIL", " / ".join(
              render_skill(hcase).splitlines()))), False)
    check("verdict: right line, wrong token rejected",
          case_correct(hcase, ("FAIL", "line %d: %r (fenced, segment 'x') "
                               "does not resolve"
                               % (head_line(hcase), "otherbin"))), False)
    check("verdict: wrong line number rejected",
          case_correct(hcase, ("FAIL", "line %d: %r (fenced, segment 'x') "
                               "does not resolve"
                               % (head_line(hcase) + 1, hcase.head))), False)
    check("verdict: extra failing line rejected",
          case_correct(hcase, ("FAIL", "%s; line %d: 'otherbin' (fenced, "
                               "segment 'x') does not resolve"
                               % (subject, head_line(hcase) + 2))), False)
    check("verdict: truncation marker rejected",
          case_correct(hcase, ("FAIL", "%s; … (+2 more)" % subject)), False)
    check("verdict: over-long detail rejected",
          case_correct(hcase, ("FAIL", "%s; %s" % (subject, "x" * 301))),
          False)
    check("verdict: negative on PASS", case_correct(hcase, ("PASS", subject)),
          False)
    check("verdict: negative on unparseable", case_correct(hcase, None), False)
    check("twin: same status and rule holds",
          twin_correct(hcase, ("FAIL", subject), ("FAIL", subject)), True)
    check("twin: divergent status fails",
          twin_correct(hcase, ("PASS", subject), ("FAIL", subject)), False)
    check("twin: unparseable primary fails",
          twin_correct(hcase, ("FAIL", subject), None), False)
    check("twin: passing where its primary failed fails",
          twin_correct(pcase, ("PASS", ""), ("FAIL", "")), False)
    check("twin: class rule still binds",
          twin_correct(hcase, ("FAIL", "echo"), ("FAIL", subject)), False)

    # output formatting
    check("wrong line",
          wrong_line(Case(seed=11, cls="H1", dirname="molvat", desc="",
                          heading="", prose_before=[], prose_after="",
                          info="", lines=(), expect="FAIL", head="x",
                          head_index=0, mode="check", kind="primary",
                          primary=None, tokens=(), commands=()), ("FAIL", "")),
          "wrong 11 H1 molvat status=FAIL")
    check("wrong line on unparseable",
          wrong_line(Case(seed=11, cls="P1", dirname="molvat", desc="",
                          heading="", prose_before=[], prose_after="",
                          info="", lines=(), expect="PASS", head=None,
                          head_index=None, mode="full", kind="primary",
                          primary=None, tokens=(), commands=()), None),
          "wrong 11 P1 molvat status=unparseable")

    # predicate arithmetic (now with the diff guard)
    check("predicate: met", predicate_ok(192, 192, 0), True)
    check("predicate: one wrong fails", predicate_ok(191, 192, 0), False)
    check("predicate: fewer than 120 fails", predicate_ok(119, 119, 0), False)
    check("predicate: zero fails", predicate_ok(0, 0, 0), False)
    check("predicate: diff guard hit fails", predicate_ok(192, 192, 1), False)

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

    # diff guard
    old = "def f():\n    return 1\n"
    check("diff: identical text has no added line", suspicious_added(old, old),
          [])
    check("diff: added suspicious line is caught",
          suspicious_added(old, old + "    p = '/proc/self/stat'\n"),
          ["    p = '/proc/self/stat'"])
    check("diff: removed suspicious line is not an addition",
          suspicious_added(old + "    x = 'tmp'\n", old), [])
    check("diff: plain added line passes",
          suspicious_added(old, old + "    return 2\n"), [])
    check("diff: pattern covers the generator tells",
          [bool(SUSPICIOUS_RE.search(w)) for w in
           ("/proc/self/stat", "getppid", "os.environ", "os.getenv",
            "PYTHONSAFEPATH", "safe_path", "check_infoless", "sys.argv",
            "ls -la", "git --version", "import random", "random.Random",
            "seed(11)", "getcwd", "tempfile", "mkdtemp", "gettempdir",
            "__file__", "parent.name", "infoless", "kotoba")], [True] * 21)
    check("diff: bare words are not tells",
          [bool(SUSPICIOUS_RE.search(w)) for w in
           ("tree", "tmp", "random", "seed", "environment", "seeds",
            "template")], [False] * 7)

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
    check("show: ok", git_show(".", "a" * 40, INSTRUMENT,
                               run=fake_git(0, b"text")), "text")
    check("show: failure raises",
          raises(lambda: git_show(".", "a" * 40, INSTRUMENT,
                                  run=fake_git(1, b"")), EnvError), True)
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

    # pool preflight
    check("pool: filters on PASS alone",
          usable_pool(("ls -la", "cat -n", "wc -l"),
                      which=lambda t: "/x/" + t,
                      probe=lambda line: line in ("ls -la", "wc -l")),
          ("ls -la", "wc -l"))
    check("pool: which filters first",
          value(lambda: usable_pool(("ls -la", "cat -n"),
                                    which=lambda t: None,
                                    probe=lambda line: True)),
          "raised EnvError")
    check("pool: fewer than two raises",
          raises(lambda: usable_pool(("ls -la", "cat -n"),
                                     which=lambda t: "/x/" + t,
                                     probe=lambda line: line == "ls -la"),
                 EnvError), True)

    # own bytes, read through a path
    with tempfile.TemporaryDirectory(prefix="infoless-sha-") as td:
        p = Path(td) / "counter.py"
        p.write_bytes(b"abc")
        check("sha: own bytes", own_sha(p),
              hashlib.sha256(b"abc").hexdigest())
        check("sha: unreadable raises",
              raises(lambda: own_sha(Path(td) / "absent.py"), EnvError), True)

    # the frozen per-case command, both modes, through an injected runner
    with tempfile.TemporaryDirectory(prefix="infoless-run-") as td:
        work = Path(td)
        seen = {}

        def pass_runner(argv, cwd, env):
            seen["argv"], seen["cwd"], seen["env"] = argv, cwd, env
            return subprocess.CompletedProcess(argv, 0, json.dumps({"checks": [
                {"id": CHECK_ID, "status": "PASS", "detail": "ok"}]}), "")

        run_namer = TempNamer(rng=random.Random(3), which=which_none)
        casedir = work / "cases"
        casedir.mkdir()
        check_mode_case = pcase._replace(mode="check")
        parsed = run_case(check_mode_case, work / "tree", casedir,
                          {"PYTHONSAFEPATH": "1"}, runner=pass_runner,
                          namer=run_namer)
        check("runner: parsed status", parsed, ("PASS", "ok"))
        check("runner: check-mode argv carries --check",
              "--check" in seen["argv"], True)
        check("runner: argv capsule",
              seen["argv"][:7],
              ["timeout", "60", "python3", "-B", "-P",
               str(work / "tree" / INSTRUMENT), "--check"])
        check("runner: empty cwd", list(seen["cwd"].iterdir()), [])
        check("runner: PYTHONSAFEPATH", seen["env"].get("PYTHONSAFEPATH"), "1")
        check("runner: SKILL.md written",
              (casedir / pcase.dirname / "SKILL.md").is_file(), True)
        check("runner: skill bytes are the rendered case",
              (casedir / pcase.dirname / "SKILL.md").read_text(
                  encoding="utf-8"), render_skill(pcase))
        hcase_full = hcase._replace(mode="full")
        run_case(hcase_full, work / "tree", casedir,
                 {"PYTHONSAFEPATH": "1"}, runner=pass_runner, namer=run_namer)
        check("runner: full-mode argv has no --check",
              "--check" in seen["argv"], False)

        def timeout_runner(argv, cwd, env):
            raise subprocess.TimeoutExpired(argv, CASE_TIMEOUT)

        check("runner: timeout is a wrong case",
              run_case(pcase, work / "tree", casedir,
                       {"PYTHONSAFEPATH": "1"}, runner=timeout_runner,
                       namer=run_namer), None)
        check("runner: empty output is a wrong case",
              run_case(pcase, work / "tree", casedir, {"PYTHONSAFEPATH": "1"},
                       runner=lambda a, c, e: subprocess.CompletedProcess(
                           a, 124, "", ""), namer=run_namer), None)

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


def guarded(fn, report=None):
    """(exit code, value): 2 on a usage/environment failure, never a traceback."""
    report = report or (lambda msg: print(msg, file=sys.stderr))
    try:
        return 0, fn()
    except (EnvError, OSError) as e:
        report("infoless-fences: %s" % e)
        return 2, None


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
    full, instrument_sha, suspicious, pool, cases, tallies, wrong = result
    print("measured %s" % full)
    print("instrument sha256 %s" % instrument_sha)
    print("instrument diff guard: %d suspicious added line(s)"
          % len(suspicious))
    for line in suspicious:
        print("  added: %s" % line)
    print("preflight real command lines: %d of %d PASS alone"
          % (len(pool), len(POOL_LINES)))
    total = len(cases)
    correct = sum(pair[0] for pair in tallies.values())
    print("info-less fence cases correct %d of %d (pass-expected %d of %d; "
          "hard negatives %d of %d)"
          % (correct, total, tallies["PASS"][0], tallies["PASS"][1],
             tallies["FAIL"][0], tallies["FAIL"][1]))
    for line in wrong:
        print(line)
    return 0 if predicate_ok(correct, total, len(suspicious)) else 1


if __name__ == "__main__":
    sys.exit(main())
