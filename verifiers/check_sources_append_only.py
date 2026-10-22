#!/usr/bin/env python3
"""Draft gate: corpus/SOURCES.md is append-only (CORPUS.md section
"SOURCES.md — where a shokunin learns", rule 2).

Rule 2, verbatim: "Only `status`, `recheck` and `used-by` change in place, and each
change is logged old->new in the round lesson. A correction is a new row whose
`teaches` opens `supersedes S0NN —`."

This gate walks every commit reachable from --rev whose diff touches
corpus/SOURCES.md, parses the registry table at the commit and at its parent, and
reports:

  * a row whose protected cell (every column except status, recheck, used-by)
    differs in place          -> breach, exit 1
  * a row present at the parent and absent at the commit -> breach, exit 1

An in-place change to one of the three permitted columns is printed as a "log"
line: rule 2 also requires it to be recorded old->new in the round lesson, which
is prose this gate does not read. The gate reports it, it does not grade it.

Output: one line per breach, then one summary line.
Exit: 0 clean, 1 breached, 2 usage/environment failure.
"""
import argparse
import re
import subprocess
import sys

PATH = "corpus/SOURCES.md"
PERMITTED = ("status", "recheck", "used-by")
ROW = re.compile(r"^\|\s*(S\d{3,})\s*\|")
HEADER = re.compile(r"^\|\s*id\s*\|")


def git(repo, *args):
    return subprocess.run(
        ["git", "-C", repo, *args], capture_output=True, text=True
    )


def blob(repo, rev):
    r = git(repo, "show", "%s:%s" % (rev, PATH))
    return r.stdout if r.returncode == 0 else None


def parse(text):
    """id -> {column: cell} for every registry row; columns come from the header."""
    cols = None
    rows = {}
    for line in text.splitlines():
        if HEADER.match(line):
            cols = [c.strip() for c in line.strip().strip("|").split("|")]
            continue
        m = ROW.match(line)
        if not m or cols is None:
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) != len(cols):
            continue  # malformed row; the census owns that finding
        rows[m.group(1)] = dict(zip(cols, cells))
    return rows


def compare(before, after):
    """(breaches, log_notes) between two parsed tables."""
    breaches, notes = [], []
    for rid in sorted(before):
        b = before[rid]
        a = after.get(rid)
        if a is None:
            breaches.append((rid, "row", "", ""))  # same 4-tuple shape as a cell change
            continue
        for col in b:
            if col == "id" or b[col] == a.get(col, ""):
                continue
            rec = (rid, col, b[col], a.get(col, ""))
            if col in PERMITTED:
                notes.append(rec)
            else:
                breaches.append(rec)
    return breaches, notes


def delta(old, new, width=44):
    """Show the window around the first differing character, not the head."""
    if old == "" and new == "":
        return "row present -> absent", ""
    i = 0
    while i < min(len(old), len(new)) and old[i] == new[i]:
        i += 1
    start = max(0, i - 14)
    lead = "\u2026" if start else ""
    return (
        lead + old[start : start + width] + ("\u2026" if start + width < len(old) else ""),
        lead + new[start : start + width] + ("\u2026" if start + width < len(new) else ""),
    )


def scan(repo, rev, base=None):
    rng = "%s..%s" % (base, rev) if base else rev
    commits = git(repo, "rev-list", "--reverse", "--no-merges", rng, "--", PATH)
    if commits.returncode != 0:
        sys.stderr.write("rev-list failed: %s\n" % commits.stderr.strip())
        raise SystemExit(2)
    breaches, notes, scanned, breached_commits = [], [], 0, set()
    for c in commits.stdout.split():
        before = blob(repo, c + "^")
        after = blob(repo, c)
        if before is None or after is None:
            continue  # root commit, or the file was created/removed here
        scanned += 1
        b, n = compare(parse(before), parse(after))
        for rec in b:
            breaches.append((c,) + rec)
            breached_commits.add(c)
        for rec in n:
            notes.append((c,) + rec)
    return breaches, notes, scanned, len(breached_commits)


def self_test():
    """Comparative arms: the table comparator must fail on the wrong shapes."""
    base = (
        "| id | source | kind | tier | scope | anchor | teaches | status | opened | recheck | used-by |\n"
        "|---|---|---|---|---|---|---|---|---|---|---|\n"
        "| S001 | a | docs | A | s | anchor one | t | queued | 2026-10-19 | 90d | \u2014 |\n"
        "| S002 | b | docs | A | s | anchor two | t | mined | 2026-10-19 | 90d | SKILL.md |\n"
    )
    arms = [
        ("unchanged", base, base, 0, 0),
        ("status in place", base, base.replace("| queued |", "| mined |"), 0, 1),
        ("used-by in place", base, base.replace("| \u2014 |", "| LOG.md |"), 0, 1),
        ("anchor in place", base, base.replace("anchor one", "anchor 1"), 1, 0),
        ("teaches in place", base, base.replace("| t |", "| t2 |"), 2, 0),
        (
            "row appended",
            base,
            base + "| S003 | c | docs | A | s | anchor | t | queued | 2026-10-19 | 90d | \u2014 |\n",
            0,
            0,
        ),
        ("row removed", base, base.replace(
            "| S002 | b | docs | A | s | anchor two | t | mined | 2026-10-19 | 90d | SKILL.md |\n", ""
        ), 1, 0),
    ]
    failures, assertions = [], 0
    for name, before, after, want_b, want_n in arms:
        b, n = compare(parse(before), parse(after))
        assertions += 3
        if len(b) != want_b:
            failures.append("%s: %d breach(es), wanted %d" % (name, len(b), want_b))
        if len(n) != want_n:
            failures.append("%s: %d log note(s), wanted %d" % (name, len(n), want_n))
        if any(len(r) != 4 for r in b + n):
            failures.append("%s: a record is not (id, column, old, new); main() cannot print it" % name)
    for f in failures:
        print("FAIL " + f)
    print("self-test: %d failure(s) over %d assertions" % (len(failures), assertions))
    return 1 if failures else 0


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--rev", default="HEAD", help="revision to scan back from")
    ap.add_argument("--base", default=None, help="optional exclusive lower bound (base..rev)")
    ap.add_argument("--repo", default=".", help="lane repository root")
    ap.add_argument("--self-test", action="store_true")
    ap.add_argument("--quiet-log", action="store_true", help="hide permitted-cell notes")
    a = ap.parse_args()
    if a.self_test:
        return self_test()
    try:
        breaches, notes, scanned, ncommits = scan(a.repo, a.rev, a.base)
    except (UnicodeDecodeError, OSError) as e:
        sys.stderr.write("could-not-evaluate: %s\n" % e)
        return 2
    if not a.quiet_log:
        for c, rid, col, old, new in notes:
            o, n = delta(old, new, 24)
            print("log  %s %s %s: %s -> %s" % (c[:9], rid, col, o, n))
    for c, rid, col, old, new in breaches:
        o, n = delta(old, new)
        print("breach %s %s %s: %s -> %s" % (c[:9], rid, col, o, n))
    if breaches:
        print(
            "sources append-only breach %d change(s) in %d of %d commits"
            % (len(breaches), ncommits, scanned)
        )
        return 1
    print("sources append-only rows clean: %d commits scanned, 0 protected-cell changes" % scanned)
    return 0


if __name__ == "__main__":
    sys.exit(main())
