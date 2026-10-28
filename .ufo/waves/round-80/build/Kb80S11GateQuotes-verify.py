#!/usr/bin/env python3
"""Kb80S11GateQuotes — independent location/word verification of the twelve
located-quote strings this round's C2 work touches, against the committed
round-79 snapshots (read-only).

Two quote sets:
  SOURCES — the `located quote "..."` string committed in the S226-S231 rows of
            corpus/SOURCES.md (used-by moves to the round-80 entry this round).
  ENTRY   — the entry-table quote from the r79 row reports (S226-S231), which
            the C2 entry carries verbatim.

Search layers, first success wins and is named:
  raw           exact bytes of the snapshot
  view+ticks    declared snapshot text view with backticks KEPT (for .html:
                script/style removed, tags->space, entities decoded; for .md:
                unordered-list marker removed, backticks kept; whitespace
                collapsed, empty lines dropped)
  view          the counter's declared text view (Markdown backticks DELETED)
"""
import hashlib
import json
import re
import sys
from html import unescape

SNAP = "/home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-79/snapshots"
LIST_MARKER_RE = re.compile(r"(?m)^[ \t]{0,3}[*+\-][ \t]+")

# id, snapshot, raw anchor that pins the occurrence line in the snapshot
ANCHOR = {
    "S226": 'The optional `allowed-tools` field:',
    "S227": "The `allowed-tools` field grants permission for the listed tools",
    "S228": "`allowed-tools` records the tools the skill is designed to use",
    "S229": "<td><code>allowed-tools</code></td>",
    "S230": "| `allowed-tools` | Experimental pre-approved tool list |",
    "S231": "user-invocable: true\nallowed-tools:",
}

C2_ENTRY = [  # id, quote (r79 row reports, verbatim)
    ("S226", "The optional allowed-tools field: A space-separated string of tools that are pre-approved to run Experimental."),
    ("S227", "`allowed-tools` field grants permission for the listed tools during the turn that invokes the skill, so Claude can use them without prompting you for approval."),
    ("S228", "`allowed-tools` records the tools the skill is designed to use. Droid stores it as skill metadata and shows it in skill surfaces"),
    ("S229", "allowed-tools No Space-delimited list of pre-approved tools the skill may use. Experimental - support may vary between agent implementations."),
    ("S230", "allowed-tools | Experimental pre-approved tool list"),
    ("S231", "user-invocable: true allowed-tools: read grep ask_user_question"),
]

SOURCES = [  # id, quote (corpus/SOURCES.md rows at base 398cbe1 / current HEAD)
    ("S226", "The optional `allowed-tools` field: A space-separated string of tools that are pre-approved to run Experimental."),
    ("S227", "allowed-tools field grants permission for the listed tools during the turn that invokes the skill, so Claude can use them without prompting you for approval."),
    ("S228", "`allowed-tools` records the tools the skill is designed to use. Droid stores it as skill metadata and shows it in skill surfaces"),
    ("S229", "allowed-tools No Space-delimited list of pre-approved tools the skill may use. Experimental - support may vary between agent implementations."),
    ("S230", "Experimental pre-approved tool list"),
    ("S231", "user-invocable: true allowed-tools: read grep ask_user_question"),
]

SNAP_FILE = {
    "S226": "S226-spec.md", "S227": "S227-claude.md", "S228": "S228-factory.md",
    "S229": "S229-msaf.html", "S230": "S230-pi.md", "S231": "S231-vibe.md",
}


def ws(s: str) -> str:
    return " ".join(s.split())


def md_view(name: str, raw: str, keep_backticks: bool):
    low = name.lower()
    if low.endswith((".html", ".htm")):
        raw = re.sub(r"(?is)<(script|style)\b.*?</\1\s*>", " ", raw)
        raw = re.sub(r"(?s)</?[A-Za-z][^>]*>", " ", raw)
        raw = unescape(raw)
    elif low.endswith((".md", ".markdown")):
        if not keep_backticks:
            raw = raw.replace("`", "")
        raw = LIST_MARKER_RE.sub("", raw)
    lines = [ws(line) for line in raw.splitlines()]
    return [line for line in lines if line]


def locate(lines, q):
    """(char index, start line idx, end line idx) in the joined lines."""
    joined = " ".join(lines)
    pos = joined.find(q)
    if pos < 0:
        return None, None, None, joined
    off = 0
    start = end = None
    for i, line in enumerate(lines):
        lo, hi = off, off + len(line) - 1
        if start is None and lo <= pos <= hi:
            start = i
        if lo <= pos + len(q) - 1 <= hi:
            end = i
            break
        off = hi + 2
    return pos, start, end, joined


def check(sid, q):
    fname = SNAP_FILE[sid]
    raw_bytes = open(f"{SNAP}/{fname}", "rb").read()
    raw = raw_bytes.decode("utf-8")
    sha = hashlib.sha256(raw_bytes).hexdigest()
    pin = open(f"{SNAP}/{sid}.manifest").read().split()[0]
    qq = ws(q)
    cv_lines = md_view(fname, raw, False)
    cv_pos, cv_s, cv_e, cv_joined = locate(cv_lines, ws(q.replace("`", "")))
    rec = dict(id=sid, snapshot=fname, sha256=sha, pin_ok=(sha == pin),
               quote=q, words_ws=len(qq.split()),
               has_allowed_tools=("allowed-tools" in qq),
               counter_view_char_index=cv_pos,
               counter_view_line_start=(cv_s + 1 if cv_s is not None else None),
               counter_view_line_end=(cv_e + 1 if cv_e is not None else None),
               counter_view_occurrences=(cv_joined.count(ws(q.replace("`", "")))
                                         if cv_pos is not None else 0))
    raw_off = raw.find(qq)
    if raw_off >= 0:
        rec.update(layer="raw", raw_char_offset=raw_off,
                   raw_byte_offset=len(raw[:raw_off].encode("utf-8")),
                   raw_line=raw.count("\n", 0, raw_off) + 1, occurrences=raw.count(qq))
        return rec
    html = fname.lower().endswith((".html", ".htm"))
    layers = ([("view+ticks", True)] if "`" in qq else []) + \
             ([("view", False)] if html or "`" not in qq else []) + \
             ([("view+ticks", True)] if not html else [])
    for layer, keep in layers:
        lines = md_view(fname, raw, keep)
        pos, s, e, joined = locate(lines, qq)
        if pos is not None:
            anc = ANCHOR[sid]
            a_off = raw.find(anc) if anc else None
            first_hash = next((i for i, l in enumerate(lines) if l.startswith("#")), None)
            rec.update(layer=layer, view_char_index=pos,
                       view_occurrences=joined.count(qq),
                       view_line_start=s + 1, view_line_end=e + 1,
                       anchor=anc,
                       anchor_char_offset=a_off,
                       anchor_byte_offset=(len(raw[:a_off].encode("utf-8"))
                                           if a_off is not None else None),
                       anchor_line=(raw.count("\n", 0, a_off) + 1 if a_off is not None else None),
                       first_hash_line_in_view=(first_hash + 1 if first_hash is not None else None))
            return rec
    rec.update(layer="absent", raw_occurrences=raw.count(qq),
               view_occurrences=None)
    return rec


def main():
    out = {"entry": [], "sources": []}
    for label, table in (("entry", C2_ENTRY), ("sources", SOURCES)):
        for sid, q in table:
            out[label].append(check(sid, q))
    print(json.dumps(out, indent=1))
    return 0


if __name__ == "__main__":
    sys.exit(main())
