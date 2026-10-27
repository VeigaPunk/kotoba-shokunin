#!/usr/bin/env python3
"""Kb79SM01 line-budget seat: duplicated-prose sweep (read-only, no network).

Question: does SKILL.md still hold prose that a corpus/knowledge entry already
holds verbatim (the round-57..72 "move it and keep a pointer" pattern's
leftover class)?

Method: tokenise SKILL.md and every corpus/knowledge/*.md to lowercase ASCII
word tokens; for each SKILL.md *prose* line (not a table row, not a checklist
box, not a fence, not a heading) find the longest contiguous token run shared
with any single knowledge file; report runs >= MIN_RUN tokens.

Run from the lane root:
  python3 -B .ufo/waves/round-79/build/Kb79SM01-dupsweep.py
"""
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parents[4]
MIN_RUN = 12
TOK = re.compile(r"[a-z0-9][a-z0-9'\-]+")


def toks(s):
    return TOK.findall(s.lower())


def longest_run(t, kt):
    best, bestpos = 0, 0
    for i in range(len(t)):
        for j in range(len(kt)):
            if kt[j] != t[i]:
                continue
            n = 0
            while i + n < len(t) and j + n < len(kt) and kt[j + n] == t[i + n]:
                n += 1
            if n > best:
                best, bestpos = n, j
    return best, bestpos


def main():
    lines = (ROOT / "SKILL.md").read_text().splitlines()
    know = {str(p.relative_to(ROOT)): toks(p.read_text())
            for p in sorted((ROOT / "corpus/knowledge").glob("*.md"))}
    print("# duplicated-prose sweep: SKILL.md vs corpus/knowledge/*.md, min run %d tokens"
          % MIN_RUN)
    print("# knowledge files %d, SKILL.md lines %d" % (len(know), len(lines)))
    hits = 0
    for ln, line in enumerate(lines, 1):
        s = line.strip()
        if not s or s.startswith("|") or s.startswith("- [ ]") or s.startswith("```") or s.startswith("#"):
            continue
        t = toks(line)
        if len(t) < MIN_RUN:
            continue
        best = (0, None, 0)
        for rel, kt in know.items():
            n, pos = longest_run(t, kt)
            if n > best[0]:
                best = (n, rel, pos)
        if best[0] >= MIN_RUN:
            hits += 1
            print("%dw SKILL.md:%d <- %s: %s" % (best[0], ln, best[1],
                                                 " ".join(t[:best[0]])))
    print("prose lines with a >=%d-token verbatim run: %d" % (MIN_RUN, hits))


if __name__ == "__main__":
    main()
