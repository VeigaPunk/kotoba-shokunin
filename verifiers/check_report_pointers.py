#!/usr/bin/env python3
r"""check_report_pointers.py -- resolve every backticked lane pointer of a round report.

Landing path (intended): `verifiers/check_report_pointers.py` in
/home/vgpnk/Projects/shokunin/kotoba-shokunin (draft built at
`.ufo/waves/round-73/w1/build/ExecPointersGate/check_report_pointers.py`).

Why this file exists
--------------------
Round 73, the plan's § Frontier step, mined mistake class `reference-drift`
(`corpus/lessons/round-73.md` § Mistakes): the round-72 report and its SHONEN
cited receipt files that do not exist -- `tip-check_tip_battery.txt` for the
committed `tip-tip_battery.txt` and `receipts/tip-check_substrate_repin_v2.txt`
for `receipts/tip-substrate_repin_v2.txt` -- and no gate caught it, because the
lane's corpus gates resolve *lane-tree* citations (`verify_corpus_integrity.py`),
not the fleet report's own pointers. This counter is that missing check.

The frozen predicate (plans/round-73.md § Frontier step; this docstring, the
plan and the receipt carry the same sentence):

    python3 -B check_report_pointers.py --report <path> --repo <lane> --rev <rev>
        -> prints "report pointers resolved N of M; unresolved U", exit 0 iff U == 0
           and the report holds at least one blob pointer (B > 0)

Tail added before any claim data (round-73 wave 1, from the controls seat's D1
and D3 worlds): `M == 0` or `B == 0` is exit 2 (cannot evaluate), never exit 0.
The frozen count line is unchanged; the tail only removes a vacuous pass, so the
`no-pointers` and `dir-only` shortcut worlds can no longer read green. The L1
lands the tail in plans/round-73-addendum-3.md, which freezes this gate.

The counter is shown able to fail by running it on the round-72 report at the
round-72 tip (exit 1, naming the two `tip-check_*` tokens) before it is ever
run on a round-73 report. It reads committed bytes only; no network.

Extraction rules (pinned here, never read from the report)
----------------------------------------------------------
A *lane pointer* is a token of the report that names a path of the lane tree.
The rules are fixed, so the universe `M` cannot be narrowed after a report is
written:

R1  Only inline code spans are read: a span is the text between two backticks on
    one physical line. Nothing outside a code span is a pointer (prose names file
    paths all the time and cannot be resolved mechanically).
R2  Fenced blocks are skipped whole: a line whose first non-space characters are
    ``` or ~~~ opens or closes a fence, and every line inside a fence is ignored.
    A fenced example is not an assertion about the tree.
R3  A span that is a command code span is skipped whole. It is a command span if
    it carries a shell metacharacter (`|`, `>`, `>>`, `&&`, `;`, `$(`, `2>&1`) or
    if it holds whitespace and its first word is a command head (an interpreter
    or tool name: `python3`, `git`, `grep`, `scripts/...`, ...) or ends in `.py`
    or `.sh`. A path that merely comes first does not make the span a command: a
    span like `.ufo/waves/round-72/receipts/x.txt (exit 1)` is still a pointer,
    because dropping it would let one parenthetical word hide a broken pointer.
    A command that names a path is an instruction, not the report's pointer to a
    file.
R4  Glob tokens are skipped: a token holding `*`, `?`, `[`, `{` (or the literal
    `...`) names a set, not a file, and `git cat-file -e` cannot resolve it.
R5  Placeholder tokens are skipped: a token holding `<` or `>` (for example
    `<rev>`, `<N>`, `<gate>.py`) is a template, not a pointer.
R6  Absolute (`/...`) and home (`~/...`) tokens are skipped; a leading `./` is
    dropped. Surrounding quotes and trailing punctuation `,.;:()` are dropped.
    A trailing line locator (`:398`, `:116-120`) is dropped too: the lane cites
    `corpus/SOURCES.md:209-215` and `PROTOCOL.md:398`, and the counter resolves
    the file. It does not check line numbers -- a locator is a reading aid, so
    the counter never claims the cited line says what the report claims.
R7  A prefix token starts with `.ufo/waves/`, `receipts/`, `corpus/`,
    `verifiers/` or `plans/`. `.ufo/waves/`, `corpus/`, `verifiers/` and
    `plans/` resolve as written, repo-relative. A `receipts/...` token resolves
    against the report's own round wave dir: `.ufo/waves/round-<N>/receipts/...`
    (`--round N`, else `round-(\d+)` in the report path).
R8  A bare token (no `/`, an extension in BARE_EXTENSIONS) is a name the report
    gives without a directory. It is resolved by a fixed ladder -- the lane
    root, `verifiers/`, `scripts/`, the report's round wave dir, `corpus/`, any
    remaining match outside a fixture area, then the round receipts dir -- so a
    buried fixture copy under `build/`, `controls/`, `evidence/`, `work/`,
    `base-outputs/`, `snapshots/` or `fixtures/` never launders a drifted
    pointer. `SKILL.md` resolves at the lane root, `verify_surfaces.py` at
    `verifiers/`, `census-before.txt` at the round's receipts dir, and
    `tip-check_tip_battery.txt` at nothing. A dotted token whose extension is
    not in BARE_EXTENSIONS (`omp.real`, `v2.1.4`) is not a pointer.

Each surviving occurrence is resolved with `git -C <lane> cat-file -t <rev>:<path>`;
the object type decides. `M` counts occurrences and `N` the resolved ones, so
`N + U == M`; a token repeated five times counts five times and every unresolved
occurrence is listed with its report line. An unresolved pointer is printed with
the nearest existing name in its parent directory (difflib, cutoff 0.5), and with
a same-basename receipt under another round when one exists -- the repair a
reader wants is usually the neighbouring round's file.

The second line the counter always prints, `pointer objects: blob B, directory
D`, exists because a directory resolves but certifies nothing: a report that
names only directories has no file a reader can open, and passing it would be
vacuous (the round-73 controls world `dir-only`).

Exit codes: 0 iff U == 0 and the report holds at least one blob pointer; 1 on
unresolved pointers; 2 when the report or the revision cannot be read, the repo
is not a git repository, the round wave dir cannot be named, the report holds no
backticked pointer token at all (`M == 0`), or every pointer names a directory
(`B == 0`). The two last cases are the could-not-evaluate class: `0 of 0` is not
a pass, because a report that drops its backticks would otherwise read green.

Blind spots, stated so they are never read as coverage
------------------------------------------------------
* Nothing outside an inline code span is checked (R1), so a prose path is
  invisible; the counter constrains cited pointers, never citation completeness.
* A fenced block (R2), a command code span (R3), a glob (R4), a `<placeholder>`
  (R5) and an absolute path (R6) are skipped by rule: a broken pointer written
  inside a fence or inside a command line passes.
* A bare name loses its round attribution (R8): an existing-but-wrong receipt
  from the same wave dir passes, and an existing artifact of another round can
  satisfy a bare name whose own round lacks it.
* A line locator is stripped, not verified (R6): the counter never says the
  cited line holds what the report claims.
* The counter reads committed bytes only: a file present in the work tree but
  not at `--rev` does not resolve.

Self-test: `--self-test` builds throwaway fixture repos under a fresh temp dir
(one `git init`, the toplevel checked equal to the temp dir before the first
commit, throwaway identity, deleted at exit) and asserts the red and green arms
of R1-R8 and the exit ladder.
"""

import argparse
import contextlib
import difflib
import io
import os
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

EXIT_OK = 0
EXIT_FAIL = 1
EXIT_USAGE = 2

LANE_PREFIXES = (".ufo/waves/", "receipts/", "corpus/", "verifiers/", "plans/")
ROUND_PREFIXES = (".ufo/waves/", "corpus/", "verifiers/", "plans/")
RECEIPTS_TOKEN = "receipts/"
BARE_EXTENSIONS = frozenset((
    ".md", ".txt", ".json", ".jsonl", ".py", ".sh", ".out", ".err", ".html",
    ".yaml", ".yml", ".toml", ".csv", ".tsv", ".patch", ".diff", ".sha256",
    ".cfg", ".ini", ".log", ".srt",
))
GLOB_CHARS = "*?[{"
PLACEHOLDER_CHARS = "<>"
RIGHT_TRIM = ",.;:)]}\"'"
LEFT_TRIM = "([{\"'"
SHELL_META = ("|", "&&", ">>", ">", "$(", ";", "2>&1")
COMMAND_HEADS = frozenset("""
python python3 py git bash sh zsh dash fish jj jj-lane.sh awk gawk mawk grep rg
sed perl ls wc curl wget find npm npx node bun deno uv uvx omp ssh tee mkdir cd
echo date chmod diff patch cp mv rm sort uniq xargs env time tar sha256sum shasum
stat printf cut tr head tail column shellcheck pytest make sudo jq yq bats comm
join paste nl fold rev md5sum gh dispatch
""".split())
WAVE_TEMPLATE = ".ufo/waves/round-%d"
NEAREST_CUTOFF = 0.5
LOCATOR_SUFFIX = re.compile(r":\d+(?:-\d+)?$")
FIXTURE_MARKERS = ("/build/", "/controls/", "/evidence/", "/work/",
                   "/base-outputs/", "/snapshots/", "/fixtures/")


# --------------------------------------------------------------------------
# git plumbing
# --------------------------------------------------------------------------

def _git(repo, *args):
    proc = subprocess.run(["git", "-C", str(repo)] + list(args),
                          stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if proc.returncode != 0:
        raise RuntimeError("git %s failed: %s"
                           % (" ".join(args),
                              proc.stderr.decode("utf-8", "replace").strip()))
    return proc.stdout.decode("utf-8", "replace")


class Tree:
    """Read-only view of one revision of a lane repo."""

    def __init__(self, repo, rev):
        self.repo = str(repo)
        self.rev = rev
        self._files = None
        self._dirs = {}

    def files(self):
        if self._files is None:
            out = _git(self.repo, "ls-tree", "-r", "--name-only", "-z", self.rev)
            self._files = [p for p in out.split("\0") if p]
        return self._files

    def object_type(self, path):
        """'blob', 'tree' or None at the revision (a directory is not a file)."""
        path = path.rstrip("/")
        if not path:
            return None
        proc = subprocess.run(
            ["git", "-C", self.repo, "cat-file", "-t", "%s:%s" % (self.rev, path)],
            stdout=subprocess.PIPE, stderr=subprocess.DEVNULL)
        if proc.returncode != 0:
            return None
        kind = proc.stdout.decode("utf-8", "replace").strip()
        return kind if kind in ("blob", "tree") else None

    def exists(self, path):
        return self.object_type(path) is not None

    def names_in(self, directory):
        """Names directly under `directory` at the revision (a missing dir is empty)."""
        directory = directory.strip("/")
        if directory in self._dirs:
            return self._dirs[directory]
        spec = "%s:%s" % (self.rev, directory) if directory else self.rev
        proc = subprocess.run(
            ["git", "-C", self.repo, "ls-tree", "--name-only", spec],
            stdout=subprocess.PIPE, stderr=subprocess.DEVNULL)
        names = []
        if proc.returncode == 0:
            names = sorted(line.strip()
                           for line in proc.stdout.decode("utf-8", "replace").splitlines()
                           if line.strip())
        self._dirs[directory] = names
        return names


def nearest_name(tree, path):
    """Nearest existing name in the unresolved path's parent directory."""
    trimmed = path.rstrip("/")
    if "/" in trimmed:
        parent, base = trimmed.rsplit("/", 1)
    else:
        parent, base = "", trimmed
    names = tree.names_in(parent)
    if not names:
        return None
    hits = difflib.get_close_matches(base, names, n=1, cutoff=NEAREST_CUTOFF)
    return hits[0] if hits else None


# --------------------------------------------------------------------------
# extraction
# --------------------------------------------------------------------------

def iter_code_spans(text):
    """Yield (line_no, span) for inline code spans outside fenced blocks (R1, R2)."""
    in_fence = False
    fence_marker = None
    for lineno, line in enumerate(text.splitlines(), 1):
        stripped = line.lstrip()
        marker = None
        for cand in ("```", "~~~"):
            if stripped.startswith(cand):
                marker = cand
                break
        if marker is not None:
            if not in_fence:
                in_fence, fence_marker = True, marker
            elif marker == fence_marker:
                in_fence, fence_marker = False, None
            continue
        if in_fence:
            continue
        for match in re.finditer(r"`([^`\n]+)`", line):
            yield lineno, match.group(1)


def is_command_span(span):
    """R3: a span that is a command line, not a pointer.

    The first word decides: a known command head, or a word ending in `.py` or
    `.sh`. A path that merely comes first does not make the span a command --
    that rule let one parenthetical word hide a broken pointer (the round-73
    controls world `multiword-span`).
    """
    if any(meta in span for meta in SHELL_META):
        return True
    words = span.split()
    if len(words) <= 1:
        return False
    head = words[0]
    return head in COMMAND_HEADS or head.endswith((".py", ".sh"))


def span_tokens(span):
    """Candidate tokens of one code span, command spans and globs removed."""
    if is_command_span(span):
        return []
    tokens = []
    for word in span.split():
        token = word.rstrip(RIGHT_TRIM).lstrip(LEFT_TRIM)
        if token:
            tokens.append(token)
    return tokens


def classify_token(token):
    """Return (channel, path) for a lane pointer, or None (R4-R8).

    channel is "tree" (resolve the path as written), "bare" (resolve the
    basename anywhere in the tree, else as a receipt of the report's round) or
    "receipt" (resolve under the report's round receipts dir).
    """
    if not token:
        return None
    if any(ch in token for ch in GLOB_CHARS) or token.endswith("..."):
        return None
    if any(ch in token for ch in PLACEHOLDER_CHARS):
        return None
    if token.startswith("/") or token.startswith("~"):
        return None
    path = token[2:] if token.startswith("./") else token
    path = LOCATOR_SUFFIX.sub("", path)
    if not path:
        return None
    if path.startswith(".ufo/waves/"):
        return ("tree", path)
    if path.startswith(RECEIPTS_TOKEN):
        return ("receipt", path)
    if path.startswith(ROUND_PREFIXES):
        return ("tree", path)
    if "/" not in path:
        suffix = os.path.splitext(path)[1].lower()
        if suffix in BARE_EXTENSIONS:
            return ("bare", path)
    return None


def extract_pointers(text):
    """All lane pointer occurrences of a report, in order: (line, token, channel, path)."""
    found = []
    for lineno, span in iter_code_spans(text):
        for token in span_tokens(span):
            classified = classify_token(token)
            if classified is None:
                continue
            found.append((lineno, token, classified[0], classified[1]))
    return found


# --------------------------------------------------------------------------
# resolution
# --------------------------------------------------------------------------

def resolve_pointer(tree, wave, channel, path):
    """Resolve one pointer at the revision. Returns (resolved_path, kind).

    kind is "blob", "tree" or None. The kind is kept because a report that
    names only directories certifies nothing a reader can open (D3).
    """
    if channel == "receipt":
        target = wave + path
        return target, tree.object_type(target)
    if channel == "tree":
        return path, tree.object_type(path)
    return resolve_bare(tree, wave, path)


def _ranked(matches):
    """Shortest path first, a fixture-area copy last, lexicographic tiebreak."""
    def key(path):
        fixture = any(marker in "/" + path for marker in FIXTURE_MARKERS)
        return (1 if fixture else 0, len(path), path)
    return min(matches, key=key)


def resolve_bare(tree, wave, name):
    """R8 ladder for a bare token: (resolved_path, kind).

    A bare token is a name the report gives without a directory. Resolution is a
    fixed ladder, so a buried fixture copy can never launder a drifted pointer:
    the lane root, then `verifiers/`, then `scripts/`, then the report's own
    round wave dir, then `corpus/`, then any remaining match outside a fixture
    area, then the round receipts dir (which is what the report meant when
    nothing else holds the name). Every rung yields a blob.
    """
    for candidate in (name, "verifiers/" + name, "scripts/" + name):
        kind = tree.object_type(candidate)
        if kind == "blob":
            return candidate, "blob"
    files = tree.files()
    for prefix in (wave, "corpus/"):
        matches = [p for p in files
                   if p.startswith(prefix) and p.rsplit("/", 1)[-1] == name]
        if matches:
            return _ranked(matches), "blob"
    matches = [p for p in files
               if p.rsplit("/", 1)[-1] == name
               and not any(marker in "/" + p for marker in FIXTURE_MARKERS)]
    if matches:
        return _ranked(matches), "blob"
    return wave + RECEIPTS_TOKEN + name, None


def cross_round_hit(tree, target, wave):
    """A same-basename receipt under another round (the repair a reader wants)."""
    base = target.rsplit("/", 1)[-1]
    if not base:
        return None
    want = re.search(r"round-(\d+)", wave)
    want = int(want.group(1)) if want else 0
    hits = [p for p in tree.files()
            if p.rsplit("/", 1)[-1] == base
            and p.startswith(".ufo/waves/")
            and "/receipts/" in p
            and not p.startswith(wave)]
    if not hits:
        return None

    def key(path):
        found = re.search(r"round-(\d+)", path)
        lane = abs(int(found.group(1)) - want) if found else 99
        return (lane, len(path), path)

    return min(hits, key=key)


def check_report(report_path, repo, rev, round_no):
    """Run the whole check. Returns a result dict."""
    wave = WAVE_TEMPLATE % round_no + "/"
    tree = Tree(repo, rev)
    text = Path(report_path).read_text(encoding="utf-8", errors="replace")
    rows = []
    resolved = 0
    blobs = 0
    dirs = 0
    for lineno, token, channel, path in extract_pointers(text):
        target, kind = resolve_pointer(tree, wave, channel, path)
        if kind == "blob":
            resolved += 1
            blobs += 1
        elif kind == "tree":
            resolved += 1
            dirs += 1
        else:
            rows.append((lineno, token, target, nearest_name(tree, target),
                         cross_round_hit(tree, target, wave)))
    return {"resolved": resolved, "total": resolved + len(rows), "rows": rows,
            "blobs": blobs, "dirs": dirs}


# --------------------------------------------------------------------------
# CLI
# --------------------------------------------------------------------------

class UsageError(Exception):
    """Raised for anything the caller got wrong (exit 2)."""


def build_parser():
    parser = argparse.ArgumentParser(
        description="Resolve every backticked lane pointer of a round report "
                    "against the lane tree at a revision.")
    parser.add_argument("--report", metavar="PATH",
                        help="the report markdown file (usually under "
                             "<fleet>/.ufo/reports/round-<N>/)")
    parser.add_argument("--repo", default=".", metavar="DIR",
                        help="the lane repo the pointers are repo-relative to "
                             "(default: .)")
    parser.add_argument("--rev", metavar="REV",
                        help="the revision the pointers are resolved at")
    parser.add_argument("--round", type=int, metavar="N",
                        help="the report's round number, naming its wave dir "
                             ".ufo/waves/round-<N>/; inferred from the report "
                             "path when omitted")
    parser.add_argument("--verbose", action="store_true",
                        help="also print each resolved pointer with its path")
    parser.add_argument("--self-test", action="store_true",
                        help="assert the red and green arms on temporary fixture "
                             "repos and exit")
    return parser


def infer_round(report_path):
    match = re.search(r"round-(\d+)", str(report_path))
    return int(match.group(1)) if match else None


def main(argv=None):
    parser = build_parser()
    args = parser.parse_args(argv)

    if args.self_test:
        return self_test()

    if not args.report or not args.rev:
        print("usage: %s --report PATH --repo DIR --rev REV [--round N]"
              % Path(sys.argv[0]).name, file=sys.stderr)
        return EXIT_USAGE

    repo = Path(args.repo).expanduser()
    report = Path(args.report).expanduser()

    if not repo.is_dir():
        print("ERROR repo %s is not a directory" % repo, file=sys.stderr)
        return EXIT_USAGE
    probe = subprocess.run(["git", "-C", str(repo), "rev-parse", "--is-inside-work-tree"],
                           stdout=subprocess.PIPE, stderr=subprocess.DEVNULL)
    if probe.returncode != 0 or probe.stdout.strip() != b"true":
        print("ERROR repo %s is not a git work tree" % repo, file=sys.stderr)
        return EXIT_USAGE
    if not report.is_file():
        print("ERROR report %s does not exist" % report, file=sys.stderr)
        return EXIT_USAGE

    round_no = args.round if args.round is not None else infer_round(report)
    if round_no is None:
        print("ERROR cannot name the report's round wave dir: pass --round N",
              file=sys.stderr)
        return EXIT_USAGE

    commit = subprocess.run(
        ["git", "-C", str(repo), "rev-parse", "--verify", "--quiet",
         "%s^{commit}" % args.rev],
        stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if commit.returncode != 0:
        print("ERROR revision %s cannot be read in %s" % (args.rev, repo),
              file=sys.stderr)
        return EXIT_USAGE
    rev = commit.stdout.decode("utf-8", "replace").strip()

    try:
        result = check_report(report, repo, rev, round_no)
    except OSError as exc:
        print("ERROR report %s cannot be read: %s" % (report, exc), file=sys.stderr)
        return EXIT_USAGE
    except RuntimeError as exc:
        print("ERROR %s" % exc, file=sys.stderr)
        return EXIT_USAGE

    resolved = result["resolved"]
    total = result["total"]
    rows = result["rows"]
    print("report pointers resolved %d of %d; unresolved %d"
          % (resolved, total, len(rows)))
    print("pointer objects: blob %d, directory %d"
          % (result["blobs"], result["dirs"]))
    if args.verbose:
        wave = WAVE_TEMPLATE % round_no + "/"
        tree = Tree(repo, rev)
        text = report.read_text(encoding="utf-8", errors="replace")
        for lineno, token, channel, path in extract_pointers(text):
            target, kind = resolve_pointer(tree, wave, channel, path)
            print("%s line %d %s -> %s"
                  % ("resolved  " if kind else "UNRESOLVED", lineno, token, target))
    for lineno, token, target, nearest, elsewhere in rows:
        print("unresolved pointer: %s (report line %d) -> %s (nearest: %s%s)"
              % (token, lineno, target, nearest or "none",
                 ", other round: %s" % elsewhere if elsewhere else ""))
    distinct = len({row[1] for row in rows})
    if distinct != len(rows):
        print("distinct unresolved tokens %d" % distinct)
    if rows:
        return EXIT_FAIL
    if total == 0:
        print("cannot evaluate: the report holds no backticked pointer token, "
              "so nothing was resolved")
        return EXIT_USAGE
    if result["blobs"] == 0:
        print("cannot evaluate: every pointer names a directory, and a "
              "directory is not a file a reader can open")
        return EXIT_USAGE
    return EXIT_OK


# --------------------------------------------------------------------------
# self-test
# --------------------------------------------------------------------------

def _git_fixture(repo, *args):
    env = dict(os.environ)
    env.update({"GIT_AUTHOR_NAME": "kotoba self-test",
                "GIT_AUTHOR_EMAIL": "self-test@example.invalid",
                "GIT_COMMITTER_NAME": "kotoba self-test",
                "GIT_COMMITTER_EMAIL": "self-test@example.invalid"})
    proc = subprocess.run(["git", "-C", str(repo)] + list(args),
                          stdout=subprocess.PIPE, stderr=subprocess.PIPE, env=env)
    if proc.returncode != 0:
        raise RuntimeError("git %s failed: %s"
                           % (" ".join(args),
                              proc.stderr.decode("utf-8", "replace").strip()))
    return proc.stdout.decode("utf-8", "replace")


def _make_fixture_repo(root, name, files):
    """A throwaway fixture repo whose toplevel is checked before the first commit."""
    repo = root / name
    repo.mkdir(parents=True)
    _git_fixture(repo, "init", "-q", "-b", "main")
    toplevel = _git_fixture(repo, "rev-parse", "--show-toplevel").strip()
    if Path(toplevel).resolve() != repo.resolve():
        raise RuntimeError("fixture toplevel %s is not %s" % (toplevel, repo))
    _git_fixture(repo, "config", "user.name", "kotoba self-test")
    _git_fixture(repo, "config", "user.email", "self-test@example.invalid")
    _git_fixture(repo, "config", "commit.gpgsign", "false")
    for rel, body in files.items():
        target = repo / rel
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(body, encoding="utf-8")
    _git_fixture(repo, "add", "-A")
    _git_fixture(repo, "commit", "-q", "-m", "fixture")
    return repo, _git_fixture(repo, "rev-parse", "HEAD").strip()


FIXTURE_FILES = {
    "SKILL.md": "# skill\n",
    "PROTOCOL.md": "# protocol\n",
    "LOG.md": "# log\n",
    "corpus/knowledge/entry.md": "# entry\n",
    "corpus/SOURCES.md": "# sources\n",
    "verifiers/check_x.py": "print('x')\n",
    "plans/round-9.md": "# plan\n",
    "scripts/sources-census.sh": "#!/bin/sh\n",
    ".ufo/waves/round-9/w1-seat.md": "# seat\n",
    ".ufo/waves/round-9/receipts/base.txt": "base\n",
    ".ufo/waves/round-9/receipts/tip-real.txt": "tip\n",
    ".ufo/waves/round-9/receipts/base-outputs/gate.out": "out\n",
    ".ufo/waves/round-9/receipts/dup.txt": "dup a\n",
    ".ufo/waves/round-9/w1/build/dup.txt": "dup b\n",
    ".ufo/waves/round-9/w1/build/dup/SKILL.md": "# buried copy\n",
    ".ufo/round-9/build/deep-only.txt": "fixture only\n",
    ".ufo/waves/round-8/receipts/other-round.txt": "round eight\n",
    ".ufo/waves/round-7/receipts/other-round.txt": "round seven\n",
}

GREEN_REPORT = """# report (fixture)

- entry `corpus/knowledge/entry.md` and plan `plans/round-9.md`.
- pointer `.ufo/waves/round-9/receipts/base.txt`.
- receipt `receipts/base.txt` and directory `receipts/base-outputs/`.
- bare receipt `base.txt`, bare lane file `SKILL.md`.
- seat report `.ufo/waves/round-9/w1-seat.md`.
"""

RED_REPORT = """# report (fixture)

- stale `tip-check.txt` and `receipts/tip-check_base.txt`.
- missing entry `corpus/knowledge/gone.md`.
"""

EXCLUSION_REPORT = """# report (fixture)

```
`corpus/nope.md` and `receipts/nope.txt`
```

- command `python3 -B verifiers/check_x.py --rev <rev>`.
- template `verifiers/<gate>.py`, glob `receipts/*.txt`.
- kept `corpus/knowledge/entry.md`.
"""

PUNCT_REPORT = """# report (fixture)

- comma `corpus/knowledge/entry.md`, period `plans/round-9.md`.
- paren (`SKILL.md`), quoted "`verifiers/check_x.py`".
- bare script `sources-census.sh` and dotted non-pointer `omp.real`.
"""

LADDER_REPORT = """# report (fixture)

- root `SKILL.md`, gate `check_x.py`, script `sources-census.sh`, sources `SOURCES.md`.
- round receipt `base.txt`, deep fixture `deep-only.txt`.
"""

LOCATOR_REPORT = """# report (fixture)

- protocol `PROTOCOL.md:398`, sources `corpus/SOURCES.md:209-215`.
- missing with locator `corpus/knowledge/gone.md:12`.
"""

DIRONLY_REPORT = """# report (fixture)

- dirs `receipts/`, `corpus/`, `.ufo/waves/round-9/receipts/`.
"""

DIRBLOB_REPORT = """# report (fixture)

- dir `verifiers/` and blob `corpus/SOURCES.md`.
"""

MULTIWORD_REPORT = """# report (fixture)

- pointer `.ufo/waves/round-9/receipts/tip-check.txt (exit 1, closure)`.
"""

CROSSROUND_REPORT = """# report (fixture)

- receipt `receipts/other-round.txt` from the wrong round.
"""


def self_test():
    failures = []
    total = [0]

    def rec(what, ok, got=None):
        total[0] += 1
        if not ok:
            failures.append("%s (got %r)" % (what, got))

    tmp = Path(tempfile.mkdtemp(prefix="k73-pointers-selftest."))
    try:
        repo, rev = _make_fixture_repo(tmp, "lane", FIXTURE_FILES)

        def cli(*argv):
            out, err = io.StringIO(), io.StringIO()
            with contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
                try:
                    code = main(list(argv))
                except SystemExit as exc:  # argparse usage errors
                    code = exc.code
            return code, out.getvalue(), err.getvalue()

        def report(name, body):
            path = tmp / name
            path.write_text(body, encoding="utf-8")
            return path

        (tmp / "round-9").mkdir()
        green = report("round-9/green.md", GREEN_REPORT)

        # -- arm 1: the green report -------------------------------------
        code, out, _ = cli("--report", str(green), "--repo", str(repo), "--rev", rev)
        rec("green: exits 0", code == EXIT_OK, (code, out))
        rec("green: the frozen count line is printed",
            "report pointers resolved 8 of 8; unresolved 0" in out, out)
        rec("green: no unresolved line", "unresolved pointer:" not in out, out)

        # -- arm 2: the red report ---------------------------------------
        red = report("round-9/red.md", RED_REPORT)
        code, out, err = cli("--report", str(red), "--repo", str(repo), "--rev", rev)
        rec("red: exits 1", code == EXIT_FAIL, (code, out))
        rec("red: the count line carries 0 of 3 and 3 unresolved",
            "report pointers resolved 0 of 3; unresolved 3" in out, out)
        rec("red: the bare stale receipt is named", "tip-check.txt" in out, out)
        rec("red: the nearest existing receipt is printed",
            "(nearest: tip-real.txt)" in out, out)
        rec("red: the receipts-relative stale token is named",
            "receipts/tip-check_base.txt" in out, out)
        rec("red: the receipts token resolves into the round wave dir",
            ".ufo/waves/round-9/receipts/tip-check_base.txt" in out, out)
        rec("red: the missing corpus path is named with its line",
            "corpus/knowledge/gone.md (report line 4)" in out, out)
        rec("red: the nearest entry is printed",
            "(nearest: entry.md)" in out, out)
        rec("red: no traceback on stderr", "Traceback" not in err, err)

        # -- arm 3: exclusions -------------------------------------------
        excl = report("round-9/excl.md", EXCLUSION_REPORT)
        code, out, _ = cli("--report", str(excl), "--repo", str(repo), "--rev", rev)
        rec("exclusions: exits 0", code == EXIT_OK, (code, out))
        rec("exclusions: only the kept pointer counts",
            "report pointers resolved 1 of 1; unresolved 0" in out, out)
        rec("exclusions: the fenced token is not counted", "nope.md" not in out, out)
        rec("exclusions: the command span is not counted",
            "check_x.py --rev" not in out, out)
        rec("exclusions: the placeholder is not counted", "<gate>" not in out, out)
        rec("exclusions: the glob is not counted", "receipts/*.txt" not in out, out)

        # -- arm 4: punctuation, quoting, bare names, dotted non-pointers --
        punct = report("round-9/punct.md", PUNCT_REPORT)
        code, out, _ = cli("--report", str(punct), "--repo", str(repo), "--rev", rev,
                           "--verbose")
        rec("punctuation: exits 0", code == EXIT_OK, (code, out))
        rec("punctuation: five pointers survive (comma, period, paren, quote, script)",
            "report pointers resolved 5 of 5; unresolved 0" in out, out)
        rec("punctuation: the bare script resolves by basename",
            "sources-census.sh -> scripts/sources-census.sh" in out, out)
        rec("punctuation: the dotted non-pointer is skipped",
            "omp.real" not in out, out)

        # -- arm 5: --round names the wave dir ---------------------------
        code, out, _ = cli("--report", str(red), "--repo", str(repo), "--rev", rev,
                           "--round", "10")
        rec("--round: the wrong round makes the receipt unresolvable",
            code == EXIT_FAIL and "receipts/tip-check_base.txt" in out, (code, out))
        rec("--round: the receipts token points at round 10",
            ".ufo/waves/round-10/receipts/tip-check_base.txt" in out, out)

        # -- arm 6: duplicates count once per occurrence -----------------
        dup = report("round-9/dup.md",
                     "- `base.txt` twice: `base.txt` and `corpus/SOURCES.md`.\n")
        code, out, _ = cli("--report", str(dup), "--repo", str(repo), "--rev", rev)
        rec("duplicates: occurrences are counted twice",
            "report pointers resolved 3 of 3; unresolved 0" in out, out)

        # -- arm 7: ambiguity is resolved, not failed --------------------
        code, out, _ = cli("--report", str(dup), "--repo", str(repo), "--rev", rev,
                           "--verbose")
        rec("ambiguity: a name in two directories still resolves",
            code == EXIT_OK, (code, out))
        rec("ambiguity: the resolved path is printed",
            "resolved   line 1 base.txt -> " in out, out)

        # -- arm 8: the exit-2 ladder ------------------------------------
        code, _, err = cli("--report", str(tmp / "absent.md"), "--repo", str(repo),
                           "--rev", rev)
        rec("ladder: a missing report exits 2", code == EXIT_USAGE, code)
        code, _, err = cli("--report", str(green), "--repo", str(repo),
                           "--rev", "0" * 40)
        rec("ladder: an unreadable revision exits 2", code == EXIT_USAGE, code)
        rec("ladder: the unreadable revision is reported",
            "cannot be read" in err, err)
        code, _, _ = cli("--report", str(green), "--repo", str(tmp), "--rev", rev)
        rec("ladder: a non-repo directory exits 2", code == EXIT_USAGE, code)
        code, _, _ = cli("--repo", str(repo), "--rev", rev)
        rec("ladder: no --report exits 2", code == EXIT_USAGE, code)
        code, _, err = cli("--report", str(green), "--repo", str(repo), "--rev", rev,
                           "--round", "not-an-int")
        rec("ladder: a non-integer --round exits 2", code == EXIT_USAGE, code)
        rec("ladder: argparse error carries no traceback", "Traceback" not in err, err)

        # -- arm 9: the bare-name ladder --------------------------------
        ladder = report("round-9/ladder.md", LADDER_REPORT)
        code, out, _ = cli("--report", str(ladder), "--repo", str(repo), "--rev", rev,
                           "--verbose")
        rec("ladder: five of six resolve", code == EXIT_FAIL
            and "report pointers resolved 5 of 6; unresolved 1" in out, (code, out))
        rec("ladder: SKILL.md resolves at the lane root",
            "SKILL.md -> SKILL.md" in out, out)
        rec("ladder: a bare gate resolves under verifiers/",
            "check_x.py -> verifiers/check_x.py" in out, out)
        rec("ladder: a bare script resolves under scripts/",
            "sources-census.sh -> scripts/sources-census.sh" in out, out)
        rec("ladder: a bare corpus name resolves under corpus/",
            "SOURCES.md -> corpus/SOURCES.md" in out, out)
        rec("ladder: a bare receipt resolves in the round receipts dir",
            "base.txt -> .ufo/waves/round-9/receipts/base.txt" in out, out)
        rec("ladder: a fixture-area copy does not launder a pointer",
            "deep-only.txt (report line 4) -> .ufo/waves/round-9/receipts/deep-only.txt"
            in out, out)

        # -- arm 10: a trailing :line locator is stripped, not resolved ----
        loc = report("round-9/locator.md", LOCATOR_REPORT)
        code, out, _ = cli("--report", str(loc), "--repo", str(repo), "--rev", rev,
                           "--verbose")
        rec("locator: two of three resolve", code == EXIT_FAIL
            and "report pointers resolved 2 of 3; unresolved 1" in out, (code, out))
        rec("locator: the bare locator resolves at the lane root",
            "PROTOCOL.md:398 -> PROTOCOL.md" in out, out)
        rec("locator: a ranged locator resolves the file",
            "corpus/SOURCES.md:209-215 -> corpus/SOURCES.md" in out, out)
        rec("locator: a missing file still fails, named without the locator",
            "corpus/knowledge/gone.md:12 (report line 4) -> "
            "corpus/knowledge/gone.md (nearest: entry.md)" in out, out)

        # -- arm 11: a directory-only report cannot evaluate --------------
        dironly = report("round-9/dironly.md", DIRONLY_REPORT)
        code, out, _ = cli("--report", str(dironly), "--repo", str(repo), "--rev", rev)
        rec("dir-only: three directories resolve and the gate refuses to pass",
            code == EXIT_USAGE and "report pointers resolved 3 of 3; unresolved 0" in out,
            (code, out))
        rec("dir-only: the object tally reads blob 0",
            "pointer objects: blob 0, directory 3" in out, out)
        rec("dir-only: the refusal says why",
            "every pointer names a directory" in out, out)
        dirblob = report("round-9/dirblob.md", DIRBLOB_REPORT)
        code, out, _ = cli("--report", str(dirblob), "--repo", str(repo), "--rev", rev)
        rec("dir+blob: a directory with a blob exits 0", code == EXIT_OK, (code, out))
        rec("dir+blob: the tally counts one of each",
            "pointer objects: blob 1, directory 1" in out, out)

        # -- arm 12: one parenthetical word cannot hide a broken pointer ---
        multi = report("round-9/multiword.md", MULTIWORD_REPORT)
        code, out, _ = cli("--report", str(multi), "--repo", str(repo), "--rev", rev)
        rec("multiword: a path-first span is not a command span",
            code == EXIT_FAIL and "report pointers resolved 0 of 1; unresolved 1" in out,
            (code, out))
        rec("multiword: the broken pointer is named",
            ".ufo/waves/round-9/receipts/tip-check.txt" in out, out)

        # -- arm 13: the cross-round repair is suggested -------------------
        cross = report("round-9/crossround.md", CROSSROUND_REPORT)
        code, out, _ = cli("--report", str(cross), "--repo", str(repo), "--rev", rev)
        rec("cross-round: the wrong-round receipt fails",
            code == EXIT_FAIL, (code, out))
        rec("cross-round: the other round's file is named as the repair",
            "other round: .ufo/waves/round-8/receipts/other-round.txt" in out, out)
        rec("cross-round: the nearest round wins over a farther one with the same name",
            ".ufo/waves/round-7/receipts/other-round.txt" not in out, out)

        # -- arm 14: an empty report is a refusal, not a pass --------------
        empty = report("round-9/empty.md", "no pointers here\n")
        code, out, _ = cli("--report", str(empty), "--repo", str(repo), "--rev", rev)
        rec("empty: zero pointers is exit 2, never a vacuous pass",
            code == EXIT_USAGE and "resolved 0 of 0; unresolved 0" in out, (code, out))
        rec("empty: the refusal says why",
            "holds no backticked pointer token" in out, out)
    finally:
        shutil.rmtree(tmp, ignore_errors=True)

    if failures:
        for line in failures:
            print("FAIL %s" % line, file=sys.stderr)
    print("self-test: %d failure(s) over %d assertions" % (len(failures), total[0]))
    return EXIT_FAIL if failures else EXIT_OK


if __name__ == "__main__":
    sys.exit(main())
