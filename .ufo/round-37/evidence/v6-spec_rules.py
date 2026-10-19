#!/usr/bin/env python3
"""Independent implementation of CommonMark 0.31.2 §4.5 (fenced code blocks)
and the §4.4 indented-code interlock, written from the spec text shipped as
``spec-0.31.2.txt``.  It is not the instrument under test and does not import
it; in the V6 matrix it is the second opinion next to cmark 0.31.2.

Rule sources (line numbers in spec-0.31.2.txt):
  1934-1940  fence = >=3 backticks or tildes, no mixing; opener preceded by
             up to three spaces of indentation
  1942-1948  info string: text after the opener, trimmed; a backtick fence's
             info string may not contain backticks
  1950-1956  content ends at a closing fence *of the same type* with *at least
             as many* characters as the opener
  1958-1960  closer preceded by up to three spaces, followed only by
             spaces/tabs
  1961-1966  no closer -> block runs to the end of the containing block
  2000-2010  "up to three spaces of indentation" is read inside the current
             container (list items carry their own content column)
Tab rule: spec 0.31.2 §2.2 — in block-structure whitespace, tabs behave as
spaces with a tab stop of 4.

``code_lines`` returns *content* lines only (fence lines excluded), the same
set the cmark oracle derives from a code_block node's text, so the two arms are
comparable line for line.
"""
import re

MARKER_RE = re.compile(r"^([ ]*)(?:\d{1,9}[.)]|[-*+])([ ]+)")
FENCE_RE = re.compile(r"^(`{3,}|~{3,})(.*)$")
TAB = 4


def columns(line: str) -> tuple[int, str]:
    """(indent in columns with 4-column tab stops, remaining text)."""
    col = 0
    i = 0
    while i < len(line):
        if line[i] == " ":
            col += 1
        elif line[i] == "\t":
            col += TAB - (col % TAB)
        else:
            break
        i += 1
    return col, line[i:]


def strip_quote(line: str) -> str:
    while True:
        col, rest = columns(line)
        if col <= 3 and rest.startswith(">"):
            line = rest[1:]
            if line.startswith(" "):
                line = line[1:]
            continue
        return line


def code_lines(lines: list[str]) -> tuple[set[int], list[dict]]:
    """(1-based content lines of every code block, notes)."""
    content: set[int] = set()
    notes: list[dict] = []
    containers: list[int] = []      # list-item content columns, innermost last
    fence: dict | None = None
    indented_run = False
    prev_blank = True

    def close_fence(last_content: int) -> None:
        nonlocal fence
        content.update(range(fence["start"] + 1, last_content + 1))
        if last_content <= fence["start"]:
            notes.append({"line": fence["start"], "note": "empty fenced block"})
        fence = None

    for i, raw in enumerate(lines, 1):
        line = strip_quote(raw)
        col, body = columns(line)
        if body.strip():
            while containers and col < containers[-1]:
                if fence is not None:
                    notes.append({"line": fence["start"],
                                  "note": "fence unterminated: item ended at "
                                          "line %d" % i})
                    close_fence(i - 1)
                containers.pop()
                indented_run = False
        rel = col - containers[-1] if containers else col
        if fence is not None:
            fm = FENCE_RE.match(body) if rel <= 3 else None
            if fm and fm.group(1)[0] == fence["char"] \
                    and len(fm.group(1)) >= fence["len"] \
                    and fm.group(2).strip(" \t") == "":
                close_fence(i - 1)
            else:
                content.add(i)
            prev_blank = body.strip() == ""
            continue
        if body.strip() == "":
            prev_blank = True
            continue
        marker = MARKER_RE.match(body)
        if marker and rel <= 3 and not indented_run:
            while containers and col + marker.end() <= containers[-1]:
                containers.pop()
            containers.append(col + marker.end())
            prev_blank = False
            continue
        opener = FENCE_RE.match(body) if rel <= 3 else None
        if opener and (opener.group(1)[0] != "`"
                       or "`" not in opener.group(2).strip(" \t")):
            fence = {"char": opener.group(1)[0], "len": len(opener.group(1)),
                     "start": i}
            prev_blank = False
            continue
        if rel >= 4 and (indented_run or prev_blank):
            indented_run = True
            content.add(i)
            prev_blank = False
            continue
        indented_run = False
        prev_blank = False
    if fence is not None:
        notes.append({"line": fence["start"], "note": "unclosed fence to EOF"})
        close_fence(len(lines))
    return content, notes