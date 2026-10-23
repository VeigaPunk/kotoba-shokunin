#!/usr/bin/env python3
"""check_word_counts.py -- guard for stated word counts that carry no command.

Round-60 build wave, mined-mistake class R1 (round-59 R1: the Gemini reject
reason said "29 words" and stated the count without the command that counted
it -- `corpus/lessons/round-59.md:27` at
31092dc6f875370bddd6eb1e4da4ca0d210c56af`).  Lesson M85 requires every word
count a lesson states to carry its counting command (`... | wc -w`).

The check reads ONE file at ONE revision and flags every line that states a
word count -- `<N> words` or `<N>-word` -- whose own line or the next two
lines carry no `wc -w` command.  It is a lexical guard, not a truth test: it
does not re-count anything, and it does not decide whether a stated number is
right, only whether the number is accompanied by the command that produced it.
The file is read through `git show <rev>:<path>`, so the measured bytes are
the committed ones, never the working tree.

Usage:
  python3 -B verifiers/check_word_counts.py --rev <rev> --file <path>
  python3 -B verifiers/check_word_counts.py --self-test

Exit: 0 = clean, 1 = a stated word count carries no counting command, 2 =
could-not-evaluate (bad revision, missing path, git failure).
"""
from __future__ import annotations

import argparse
import contextlib
import io
import re
import subprocess
import sys
import tempfile
from pathlib import Path

# `<N> words` (plural, space-separated) or `<N>-word` / `<N>-words` (hyphen).
COUNT_RE = re.compile(r"(?<![0-9A-Za-z])(\d+)(?:[ \t]+words\b|[ \t]*-[ \t]*words?\b)")
# The counting command itself: `wc -w`, `wc  -w`, `wc -lw`.
WC_RE = re.compile(r"\bwc[ \t]+-\w*w\b")
WINDOW = 2  # a command on the line itself or on one of the next two lines counts


def scan(text: str) -> tuple[list[tuple[int, str, list[str]]], int]:
    """Return (flagged lines, total claimed lines).

    A line is flagged when it states a word count and neither it nor the next
    `WINDOW` lines carry a `wc -w` command.  Each entry is (line number, line
    text, the stated counts on that line).
    """
    lines = text.splitlines()
    flagged: list[tuple[int, str, list[str]]] = []
    claimed = 0
    for i, line in enumerate(lines):
        found = [m.group(0).strip() for m in COUNT_RE.finditer(line)]
        if not found:
            continue
        claimed += 1
        if WC_RE.search("\n".join(lines[i:i + WINDOW + 1])):
            continue
        flagged.append((i + 1, line.strip(), found))
    return flagged, claimed


def repo_root(explicit: str | None) -> Path:
    """The git repository to read from: --repo, else the script's or cwd's root."""
    if explicit:
        return Path(explicit).resolve()
    for start in (Path(__file__).resolve(), Path.cwd().resolve()):
        for d in (start, *start.parents):
            if (d / ".git").exists():
                return d
    return Path.cwd().resolve()


def read_at(repo: Path, rev: str, path: str) -> str:
    """The bytes of `path` at `rev`, as text.  Raises RuntimeError on failure."""
    proc = subprocess.run(
        ["git", "--no-optional-locks", "-C", str(repo), "show", "%s:%s" % (rev, path)],
        capture_output=True)
    if proc.returncode != 0:
        raise RuntimeError("git show %s:%s failed: %s"
                           % (rev, path, proc.stderr.decode("utf-8", "replace").strip()))
    return proc.stdout.decode("utf-8", "replace")


def report(path: str, flagged: list[tuple[int, str, list[str]]]) -> None:
    for line_no, text, counts in flagged:
        print("%s:%d: stated word count (%s) with no `wc -w` command on this line "
              "or the next %d" % (path, line_no, ", ".join(counts), WINDOW))
        print("    %s" % text)


def self_test() -> int:
    """Exercise the detector on pinned strings and on the CLI.  0 when all hold."""
    assertions = 0
    failures = 0

    def check(name: str, actual: object, expected: object) -> None:
        nonlocal assertions, failures
        assertions += 1
        if actual != expected:
            failures += 1
            print("FAIL %s: got %r, expected %r" % (name, actual, expected))

    # A count with its command on the same line is clean.
    check("same-line command",
          scan("- the quote is 29 words, by `printf %s 'x' | wc -w` -> 29\n")[0], [])
    # A count whose command is on the next line is clean (window of 2).
    check("command on next line", scan("the quote is 29 words\n  `wc -w` -> 25\n")[0], [])
    # A count whose command is two lines down is still clean.
    check("command two lines down",
          scan("the quote is 29 words\n\n  `wc -w` -> 25\n")[0], [])
    # A count whose command is three lines down is outside the window: flagged.
    check("command three lines down",
          [c[0] for c in scan("the quote is 29 words\n\n\n  `wc -w` -> 25\n")[0]], [1])
    # The hyphenated form counts too.
    check("hyphenated form",
          [c[0] for c in scan("- carries a 10-word quote, no command here\n")[0]], [1])
    # Plain prose with no number is not a count.
    check("no number", scan("- the best-practices page carries a short quote\n")[0], [])
    # A number that is not a word count is not a count.
    check("not a word count", scan("- 600 lines, 8 columns, 2 seats\n")[0], [])
    # A different wc flag is not the counting command.
    check("other wc flag does not count",
          [c[0] for c in scan("the quote is 29 words\n  `wc -c` -> 1200\n")[0]], [1])
    check("wc without the w flag does not count",
          [c[0] for c in scan("the quote is 29 words\n  `wc -l` -> 4\n")[0]], [1])
    # The mined line itself: three stated counts, no command within the window.
    line27 = ("- **Gemini CLI hooks-overview quote** — reject: 29 words, above the "
              "25-word cap (`CensusGeminiCLI`); the best-practices page carries a "
              "10-word quote.\n")
    flagged, claimed = scan(line27)
    check("mined line is flagged once", len(flagged), 1)
    check("mined line number", flagged[0][0], 1)
    check("mined line counts", flagged[0][2], ["29 words", "25-word", "10-word"])
    check("mined line claimed count", claimed, 1)
    # A clean file claims a count and is not flagged.
    flagged, claimed = scan("- the quote is 29 words, by `wc -w` -> 25\n")
    check("clean file flags nothing", flagged, [])
    check("clean file still claims one line", claimed, 1)
    # The window is two lines: a command four lines down does not rescue it.
    check("command four lines down",
          [c[0] for c in scan("a 29 words\n\n\n\n  `wc -w` -> 25\n")[0]], [1])

    # Main-path arms: the CLI exit code over a real committed revision
    # (lane lesson M71: a self-test that never runs main() proves nothing).
    with tempfile.TemporaryDirectory(prefix="check-word-counts-") as tmp:
        repo = Path(tmp) / "repo"
        repo.mkdir()
        for args in (["init", "-q"], ["config", "user.name", "selftest"],
                     ["config", "user.email", "s@l.local"]):
            subprocess.run(["git", "-C", str(repo)] + args, capture_output=True)
        (repo / "bad.md").write_text("- the quote is 29 words, no command here\n")
        (repo / "good.md").write_text("- the quote is 29 words, by `wc -w` -> 25\n")
        for args in (["add", "-A"], ["commit", "-qm", "fixture"]):
            subprocess.run(["git", "-C", str(repo)] + args, capture_output=True)
        rev = subprocess.run(["git", "-C", str(repo), "rev-parse", "HEAD"],
                              capture_output=True).stdout.decode().strip()
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf), contextlib.redirect_stderr(buf):
            bad = main(["--rev", rev, "--file", "bad.md", "--repo", str(repo)])
            good = main(["--rev", rev, "--file", "good.md", "--repo", str(repo)])
            absent = main(["--rev", rev, "--file", "absent.md", "--repo", str(repo)])
        check("main path flags the mined shape", bad, 1)
        check("main path passes a commanded count", good, 0)
        check("main path on a missing path is could-not-evaluate", absent, 2)
        check("main path names the offending line", "bad.md:1" in buf.getvalue(), True)

    print("self-test: %d failure(s) over %d assertions" % (failures, assertions))
    return 1 if failures else 0


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--rev")
    ap.add_argument("--file")
    ap.add_argument("--repo")
    ap.add_argument("--self-test", action="store_true")
    args = ap.parse_args(argv)
    if args.self_test:
        if args.rev or args.file:
            ap.error("--self-test cannot be combined with --rev or --file")
        return self_test()
    if not args.rev or not args.file:
        ap.error("--rev and --file are required")
    try:
        text = read_at(repo_root(args.repo), args.rev, args.file)
    except (RuntimeError, OSError) as exc:
        print("could-not-evaluate: %s" % exc, file=sys.stderr)
        return 2
    flagged, claimed = scan(text)
    report(args.file, flagged)
    print("stated word counts without a counting command: %d of %d claimed lines"
          % (len(flagged), claimed))
    return 1 if flagged else 0


if __name__ == "__main__":
    sys.exit(main())
