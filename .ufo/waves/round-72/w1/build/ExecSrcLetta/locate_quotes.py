#!/usr/bin/env python3
"""Locate every sentence the staged S261 row and the two citing entries quote from
https://docs.letta.com/configuration/skills, in both committed snapshot forms.

Read-only: reads the two snapshots under .ufo/waves/round-72/snapshots/ and prints,
per quote, whether it occurs word-bounded, in which form(s), at which 1-based line,
and the verbatim line from `sed -n '<L>p'`-equivalent bytes.

Usage: python3 -B locate_quotes.py [--root <lane-root>]
"""
import argparse
import hashlib
import os
import re
import sys

FORMS = [
    ("md", "S261-letta-skills.md"),
    ("html", "S261-letta-skills.html"),
    ("rendered", "S261-letta-skills.rendered.txt"),
]

# (id, owner, quoted text, note)
QUOTES = [
    ("Q1", "row S261 / entry skill-vs-always-on-boundary",
     "The Letta agent harness implements the open Agent Skills standard.",
     "row + entry quote; the page links 'Agent Skills' to agentskills.io"),
    ("Q2", "row S261 / entry skill-vs-always-on-boundary",
     "Skills are portable across Letta, Codex, Claude Code, Hermes Agent, OpenClaw, and other compatible agents.",
     "row + entry quote"),
    ("Q1+Q2", "entry skill-vs-always-on-boundary",
     "The Letta agent harness implements the open Agent Skills standard. Skills are portable across Letta, "
     "Codex, Claude Code, Hermes Agent, OpenClaw, and other compatible agents.",
     "the entry's combined quotation"),
    ("Q3a", "row S261 / entry skill-paths-and-precedence",
     "Project-scoped",
     "scope label; row wraps it in CJK corner brackets that are not page bytes"),
    ("Q3b", "row S261 / entry skill-paths-and-precedence",
     "Agent-scoped (MemFS)",
     "scope label"),
    ("Q3c", "row S261 / entry skill-paths-and-precedence",
     "Computer-scoped",
     "scope label"),
    ("Q4", "entry skill-paths-and-precedence",
     "~/.letta/skills/",
     "computer-scoped path the entry asserts"),
    ("Q5", "entry skill-paths-and-precedence",
     "stored inside that agent\u2019s git-backed memory filesystem",
     "agent-scoped tier the entry asserts"),
    ("Q6", "entry skill-paths-and-precedence",
     "Primary project-local location for interactive client-side skills",
     "the page's words for .agents/skills/ (entry says 'shared .agents/skills/ root')"),
    ("Q7", "entry skill-vs-always-on-boundary",
     "six named agents",
     "the entry's COUNT claim; page names five agents plus 'other compatible agents'"),
    ("Q8", "row S261",
     "three-scope",
     "the row's model claim; page's own sentence lists three, its table lists four Location rows"),
    ("Q9", "entry skill-paths-and-precedence",
     "Letta registers skills from three scopes rather than two",
     "the entry's count claim"),
    ("Q10", "row S261",
     "from the current project (project-scoped skills), their own memory (agent-scoped skills), and "
     "skills provided automatically by the Letta harness (bundled skills)",
     "21-word contiguous prose span for the three-scope model (labels alone are under the 5-word floor)"),
    ("Q11", "entry skill-paths-and-precedence",
     "Skills shared across all Letta agents running on this machine",
     "the page's words for ~/.letta/skills/"),
]


def word_bounded(text, quote):
    pat = r"(?<![0-9A-Za-z_])" + re.escape(quote) + r"(?![0-9A-Za-z_])"
    return re.search(pat, text)


def main():
    ap = argparse.ArgumentParser()
    # __file__ = <root>/.ufo/waves/round-72/w1/build/ExecSrcLetta/locate_quotes.py
    root = os.path.abspath(__file__)
    for _ in range(7):
        root = os.path.dirname(root)
    ap.add_argument("--root", default=root)
    args = ap.parse_args()
    snapdir = os.path.join(args.root, ".ufo", "waves", "round-72", "snapshots")

    loaded = {}
    for form, name in FORMS:
        path = os.path.join(snapdir, name)
        with open(path, "rb") as fh:
            data = fh.read()
        text = data.decode("utf-8")
        loaded[form] = (path, data, text)
        print("snapshot %-4s %s bytes=%d sha256=%s"
              % (form, name, len(data), hashlib.sha256(data).hexdigest()))
    print()

    for qid, owner, quote, note in QUOTES:
        print("== %s (%s) -- %s" % (qid, owner, note))
        print("   quote (%d words): %s" % (len(quote.split()), quote))
        for form, _name in FORMS:
            _path, _data, text = loaded[form]
            m = word_bounded(text, quote)
            if not m:
                print("   %-4s located=no" % form)
                continue
            line_no = text.count("\n", 0, m.start()) + 1
            line = text.split("\n")[line_no - 1]
            print("   %-8s located=yes line=%d byte_offset=%d words=%d"
                  % (form, line_no, len(text[:m.start()].encode("utf-8")), len(quote.split())))
            if form in ("md", "rendered"):
                print("        sed -n '%dp' -> %s" % (line_no, line))
            else:
                print("        line bytes (trimmed to 240 chars): %s" % line[:240])
        print()


if __name__ == "__main__":
    sys.exit(main())
