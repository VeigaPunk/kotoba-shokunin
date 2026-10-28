#!/usr/bin/env python3
"""check_allowed_tools.py — frozen C2 counter for kotoba round 80 (depth).

FROZEN PREDICATE (the same sentence in plans/round-80.md § C2, in this
docstring, in the receipt and in the SCORECARD row):

    python3 -B verifiers/check_allowed_tools.py --rev <rev>  ->  prints
    "allowed-tools surfaces documented N of 6" and "generator world: M of 6"
    and "semantic rider: exploratory — reviewers of record: round-80 non-author
    closure spot-check", and exits 0 only when N == 6 and the tree conjuncts
    (g)-(h) hold; at the r80 base
    398cbe1bb67f8d9dcf5d25d5ecf1b26a7c6f7e93 it prints
    "allowed-tools surfaces documented 0 of 6" and exits 1.

The headline asserts FORM-LEVEL DOCUMENTATION ONLY: the six surfaces carry
committed, snapshot-pinned, quote-grounded rows.  The grant-semantics matrix
(each label true of its page; the cross-client conflict reading) is the
EXPLORATORY RIDER and is assigned to the round-80 non-author closure
spot-check, which is why the third printed line names those reviewers and why
the generator world's score is printed rather than gated (Q71/Q74: the
headline names what the generator reaches; a claim whose generator world
reaches the target says so in the headline and hands the judgement to named
non-author seats).

Surface ``V`` in the frozen host table below is **documented** at ``--rev``
iff all
of (a)-(f) hold over committed bytes only (no network at measurement, and no
instrument of the measured tree is executed):

  (a) the entry ``corpus/knowledge/allowed-tools-surfaces-round80.md`` (frozen
      path) opens with ``source:`` lines for every cited id, then
      ``verified-at:`` then ``recheck:``; the entry names the snapshot text
      view; and its surface table (the one table whose header is the frozen
      ``surface | source | page tokens | grant | located quote``) has exactly
      one row for ``V`` whose backticked tokens (>= 3, including
      ``allowed-tools``, one value-form token and one grant-semantics token)
      each occur ASCII-word-bounded in a committed snapshot of a source that
      row cites;
  (b) every cited ``S###`` is an 11-cell registry row, status ``mined``, tier
      ``A`` or ``B``, ``used-by`` naming the entry, URL host+path-prefix equal
      to ``V``'s frozen host (Q32 exact identity);
  (c) each cited row's snapshot under ``.ufo/waves/round-79/snapshots/`` has a
      sha256 equal to the pin in the committed ``MANIFEST.sha256`` and equal to
      the sha256 in the row's anchor fetch record
      ``fetched <ISO8601>Z, HTTP 200, <bytes> B, sha256 <hex>``;
  (d) each row's located quote (5-25 words, whitespace-collapsed only) occurs
      in its own snapshot **and contains the token ``allowed-tools``**; Q70:
      the quote is not a banner or subtitle line and not in the first-heading
      block;
  (e) opened this round: the row's ``opened`` cell = the entry's
      ``verified-at:`` = 2026-10-27;
  (f) the row's ``grant`` cell (plain text, not backticked) carries exactly one
      frozen label, and it is ``V``'s label; and the row's quote carries the
      page token that grounds it, per the frozen table.

Three tree-level conjuncts are reported on their own lines and are needed for
exit 0:

  (g) SKILL.md carries one rule line citing the entry path and naming >= 3
      surfaces, and a conformant registry row for this counter (kind ``gate``);
      printed ``skill rule line ok`` / ``registry home ok``.
  (h) PROVINCE.md ``## Core`` has exactly one bullet naming the entry path;
      printed ``province surfaces named P of 6`` (the surfaces that bullet
      names, informational) beside the bullet finding.
  (i) printed ``generator world: M of 6``: the counter builds, from the
      measured revision's own committed bytes (the registry rows, the pinned
      snapshots and the plan's frozen surface table) and with no judgement,
      the generator world -- the COMPLETE proposed evidence shape for the six
      surfaces -- and measures it with the SAME ``check()``.  Round 80 measures
      FORM-LEVEL DOCUMENTATION ONLY, so the generator world is expected to
      reach the target: its score M is PRINTED beside the headline and it
      NEVER gates the exit predicate.  The grant-semantics judgement is the
      exploratory rider, and the third printed line names its non-author
      reviewers.  Q71/Q74: the generator may not hardcode an unreported score
      -- M is always measured by scoring the generated world on this counter.

READINGS that are deliberately stricter or looser than the naive one, named
here so a reviewer can attack them rather than discover them:

  * the surface table is the table whose cleaned header cells equal the frozen
    five (case/emphasis/backticks stripped, whitespace collapsed). There must
    be exactly one such table in the entry: none is an entry-level break (0 of
    6), two is ambiguous (0 of 6). A surface row is a row of that table whose
    first cell, cleaned, EQUALS the surface's frozen display name (``Open
    specification``, ``Claude Code``, ``Factory``, ``Microsoft Agent
    Framework``, ``pi``, ``Mistral Vibe``); ``| pi coding agent |`` does not
    name ``pi``. Exactly one row per surface. Every surface row must carry
    exactly five cells (the frozen header's arity), else that surface fails.
  * the counted tokens are the backticked spans of the row's cells AFTER the
    first (the surface cell). A token's role:
      - ``key``: the token is exactly ``allowed-tools``;
      - ``grant``: the token contains the surface's frozen page token at an
        ASCII word boundary, case-insensitively (the cue the plan freezes:
        ``Experimental``, ``without prompting you for approval``,
        ``metadata``, ``allowed-tools:``);
      - ``value``: any other token that carries a value shape — one of
        ``( ) [ ] , : * < > { }`` or a space inside the token, or a bare name
        ``^[A-Za-z][A-Za-z0-9_.@/-]*$`` (a tool name, a YAML list item:
        ``Bash``, ``Bash(git:*)``, ``ask_user_question``, ``[Bash, Read]``);
      - ``other``: anything else (counts only toward ">= 3").
    The three roles are not exclusive over the row, but each token takes its
    first matching role, so the key and the page token cannot silently double
    as a value form.
  * word-bounded means ASCII-word-bounded (``[A-Za-z0-9_]``), not ``\\w``. A
    token's matching forms are the token itself, its form without a leading
    ``~/`` and each without a trailing ``/``; no other shaping is applied.
  * the snapshot text view is the plan's Q42/Q53/Q56 rule as amended by the
    L1 before any data (plans/round-79.md § C2, freeze commits d9d01c2 and
    60ba11f) and nothing else: for a ``.html``/``.htm`` snapshot,
    ``<script>``/``<style>`` blocks are removed, tags become one space,
    entities are decoded; for a Markdown snapshot (``.md``/``.markdown``)
    every backtick byte is deleted and an unordered-list marker is removed by
    ``(?m)^[ \\t]{0,3}[*+\\-][ \\t]+``; then every whitespace run is collapsed
    (a plain-text snapshot: collapse whitespace only). Fenced code blocks and
    HTML comments are NOT removed from a snapshot: two of the six pages
    document the field only inside a fenced example (vibe L721-731), so
    stripping fences would make those surfaces unbackable. The entry has to
    name that shaping on one line (``.html``, ``script``, an
    ``entit*``/``decod*`` word, ``whitespace`` and a backtick/inline-code
    word), and the located quote is written in its transformed exact form —
    S226's frozen quote is ``The optional allowed-tools field: A
    space-separated string of tools that are pre-approved to run
    Experimental.``
  * a markdown table cell is read with escape-aware splitting: a ``|``
    preceded by a backslash is cell content, not a column break, and the
    backslash is removed before the cell is judged. Without this a real row
    whose quote is a markdown table row (pi: ``| `allowed-tools` |
    Experimental pre-approved tool list |``) would read as six cells and could
    never be documented.
  * the located quote is the single quoted span of the row's ``located quote``
    cell; the fallback when the cell carries no quoted span is the cell's own
    whitespace-collapsed text. Two distinct quoted spans in one cell is a
    finding, never a pass. The quote is matched as written and, only if that is
    not found, once more with every backtick byte deleted (the Markdown view
    deletes backticks, so a seat that backticks the cell is not punished for
    formatting); no other shaping is applied. The quote is matched over the
    text view with whitespace collapsed and nothing else: no backtick
    stripping, no case folding. It must contain ``allowed-tools`` (case
    sensitive, ASCII word boundary).
  * Q70 location: the quote's occurrence must lie on a line that is not a
    heading and is not in the first-heading block (the page's first heading
    line and the line after it); and its line must not occur verbatim in
    another snapshot whose raw bytes differ (a shared banner/subtitle line on a
    different page). Byte-identical snapshots are the same page and do not
    disqualify each other. A heading is read PER SNAPSHOT SHAPE, because the
    text view has already destroyed the tags: for a Markdown snapshot a heading
    is a view line that starts with ``#``; for an HTML snapshot a heading is the
    view line that carries a ``<h1>``..``<h6>`` element of the raw bytes (the
    element's opening tag is replaced by a marker while the SAME pipeline runs,
    so line indices stay aligned and the marker never reaches a quote). Round
    80 fixes the r79 draft's misfire: on an HTML view a ``#``-prefixed line is
    a code comment (S229-msaf.html carries ``# Auto-approve ...`` in a Python
    sample), not a heading, so the ``#``-scan made the msaf page's only
    admissible quote unlocatable and the six-surface target unreachable.
  * (e) is a per-surface content finding, not exit 2: this round's plan lists
    it among the conjuncts that decide "documented", so a row opened on another
    day is a surface that is not documented, never a could-not-evaluate.
  * (c) IS exit 2 when the committed bytes do not hash to the pin
    (``snapshot_tampered``), when the manifest is missing or malformed, when a
    pin escapes the snapshot directory, or when the snapshot of a cited id is
    ambiguous: a pin that does not pin cannot be evaluated, and this counter
    never converts that into a pass or a content fail.
  * a pin is bound to the page the row cites: the entry's own ``source:`` line
    for a cited id must carry a URL whose host+path (trailing ``/`` ignored)
    equals the cited row's first URL, else that surface is not documented. The one
    exception is the L1's factory amendment: the canonical page and that same
    page's ``.md`` route (a bare ``.md`` suffix on one side, same host) are the
    same page.
  * the generator world is generated at measurement time, not a fixed list: it
    pairs every registry row with the manifest pin whose basename begins with
    that id (``S226`` -> ``S226-spec.md``), keeps the rows whose URL is on the
    surface's frozen host, and for each surface takes the lowest such id.  From
    that snapshot's text view it mechanically takes the first 5..25-word window
    that starts at the field token, carries the surface's frozen page token and
    passes this counter's own Q70 locator, then the first value-form token in
    that window (a value shape first, then a capitalised bare name, then any
    bare name, stopwords excluded), and the frozen page token as the
    grant-semantics token.  It writes the grant cell from the plan's FROZEN
    surface table (the shape is frozen and public; whether the label is TRUE of
    the page is not decided here), rewrites ``used-by``/``opened`` and the
    anchor fetch record from the pinned bytes, and is scored by ``check()``
    with no special case.  M is how many surfaces this form builder reaches; it
    is printed beside the headline and never gated.
  * the pin source: the aggregate ``MANIFEST.sha256`` when it is committed at
    the measured revision, and otherwise the six per-page ``<id>.manifest``
    files the round-79 wave committed in the same directory (one
    ``<sha256>  <basename>`` line each).  Both carry the same pins; if both are
    committed they must agree basename by basename, and a disagreement is exit
    2 (a pin that pins two digests pins nothing).
  * the anchor fetch record: the committed r79 rows write ``fetched
    2026-10-27, HTTP 200, 7608 B, sha256 `<hex>``` -- a DATE without a time and
    a backticked digest.  The record grammar accepts a date or a date-time with
    ``Z`` and an optional backtick pair around the digest; the HTTP status, the
    byte count and the 64-hex digest stay required, and the digest must equal
    the manifest pin and the committed snapshot's own sha256.

Exit codes: 0 iff N == 6 and the tree conjuncts (g)-(h) hold (the generator
world's score M is printed beside the headline and never gates); 1 otherwise
(a content verdict); 2 could not evaluate (unknown revision, unreadable
registry/manifest, tampered or ambiguous pinned snapshot, counter drift,
unreadable base registry).
``--self-test`` drives ``main()`` on an honest world (exit 0 and the exact
printed line) beside one broken world per conjunct and per shortcut control
the plan names, in isolated local git repos under fresh ``mktemp -d``
directories (honouring ``TMPDIR`` and ``--work``): no lane, no fleet repo and
no shared index is ever touched. Neither ``--self-test`` nor a measurement
reads the network. ``--print-self-sha`` prints the blanked sha of this file
(the L1 refills ``SELF_SHA`` after any edit and before freeze).

Usage:
  python3 -B verifiers/check_allowed_tools.py --rev <rev> [--repo <lane>] [--work <dir>]
  python3 -B verifiers/check_allowed_tools.py --self-test [--work <dir>]
  python3 -B verifiers/check_allowed_tools.py --print-self-sha
"""

from __future__ import annotations

import argparse
import contextlib
import hashlib
import io
import os
import re
import shutil
import subprocess
import sys
import tempfile
import urllib.parse
from html import unescape
from pathlib import Path

TOTAL = 6
TARGET = 6
SOURCES = "corpus/SOURCES.md"
ENTRY = "corpus/knowledge/allowed-tools-surfaces-round80.md"
SNAPDIR = ".ufo/waves/round-79/snapshots"
MANIFEST = SNAPDIR + "/MANIFEST.sha256"
PER_MANIFEST_RE = re.compile(r"^S\d+\.manifest$")
COUNTER_PATH = "verifiers/check_allowed_tools.py"
CAPTURE = "2026-10-27"
PROVINCE = "PROVINCE.md"
SKILLMD = "SKILL.md"

# The plan's frozen surface table: table header cells, then per surface the
# frozen host pin(s), the frozen first cell, the frozen grant label and the
# frozen page token that grounds the label.
HEADER = ("surface", "source", "page tokens", "grant", "located quote")
GRANT_LABELS = ("pre-approves", "metadata-only", "experimental", "unstated")
SURFACES = {
    "spec": {
        "display": "Open specification",
        "hosts": ("agentskills.io",),
        "grant": "experimental",
        "page_token": "Experimental",
    },
    "claude": {
        "display": "Claude Code",
        "hosts": ("code.claude.com",),
        "grant": "pre-approves",
        "page_token": "without prompting you for approval",
    },
    # The L1 moved factory to its canonical page before any data: the assigned
    # URL 308s to https://docs.factory.com/harness/skills, and the snapshot is
    # that page's Markdown route.  Both URL forms are the same canonical page,
    # so both are pins (host + whole-segment path prefix, Q32).
    "factory": {
        "display": "Factory",
        "hosts": ("docs.factory.com/harness/skills",
                  "docs.factory.com/harness/skills.md"),
        "grant": "metadata-only",
        "page_token": "metadata",
    },
    "msaf": {
        "display": "Microsoft Agent Framework",
        "hosts": ("learn.microsoft.com",),
        "grant": "experimental",
        "page_token": "Experimental",
    },
    "pi": {
        "display": "pi",
        "hosts": ("raw.githubusercontent.com/badlogic/pi-mono",),
        "grant": "experimental",
        "page_token": "Experimental",
    },
    "vibe": {
        "display": "Mistral Vibe",
        "hosts": ("raw.githubusercontent.com/mistralai/mistral-vibe",),
        "grant": "unstated",
        "page_token": "allowed-tools:",
    },
}
SURFACE_ORDER = ("spec", "claude", "factory", "msaf", "pi", "vibe")

# The committed round-79 rows write "fetched 2026-10-27, HTTP 200, 7608 B,
# sha256 `<hex>`": a DATE without a time and a BACKTICKED digest.  The record
# grammar accepts a date or a date-time with Z, and an optional backtick pair
# around the digest; the HTTP status, the byte count and the 64-hex digest stay
# required.
FETCHED_RE = re.compile(
    r"fetched (\d{4}-\d\d-\d\d(?:T\d\d:\d\d:\d\dZ)?), HTTP 200, (\d+) B, "
    r"sha256 `?([0-9a-f]{64})`?")

# Frozen for round 80: the lane base the do-nothing figure is measured at.  The
# self-test rebinds this module global to a fixture repo's own first commit
# (there is no CLI flag to move it: a measurement always reads this constant).
BASE_REV = "398cbe1bb67f8d9dcf5d25d5ecf1b26a7c6f7e93"

MIN_TOKENS = 3
MIN_QUOTE_WORDS = 5
MAX_QUOTE_WORDS = 25
REGISTRY_CELLS = 11
SKILL_CELLS = 8

SID_RE = re.compile(r"\bS\d{3,}\b")
BACKTICK_RE = re.compile(r"`([^`]+)`")
QUOTE_RE = re.compile(r'["\u201c]([^"\u201d]+)["\u201d]')
REGISTRY_RE = re.compile(r"^ {0,3}\|\s*S\d{3,}\s*\|")
URL_RE = re.compile(r"https?://[^\s)>\]]+")
BARE_NAME_RE = re.compile(r"^[A-Za-z][A-Za-z0-9_.@/-]*$")
VALUE_SHAPE_RE = re.compile(r"[()\[\],:*<>{}]")
SEPARATOR_RE = re.compile(r":?-{3,}:?")
LIST_MARKER_RE = re.compile(r"(?m)^[ \t]{0,3}[*+\-][ \t]+")
TRIM_CHARS = ".,;:!?)]}'\""
SELF_SHA = "434fd6f9646bbc56948eb5c4603c7a1f2d815fc11b3741cb25ef052720111742"   # blanked-sha of this file (the L1 refills it at freeze)
_INTERNAL_SELFTEST = False   # set only by --self-test: the drift guard is a
                             # measurement guard, and the self-test mutates
                             # nothing in this file, so it is skipped there.
SELF_LINE_RE = re.compile(r'^SELF_SHA = "[0-9a-f]*"', re.M)
_WORK: str | None = None     # --work: the parent of every temp dir this run makes


class EnvError(Exception):
    """Could not evaluate: exit 2, never a pass and never a fail."""


# --------------------------------------------------------------- text shaping

def _blanked_sha(text: str) -> str:
    return hashlib.sha256(
        SELF_LINE_RE.sub('SELF_SHA = ""', text).encode()).hexdigest()


def rendered(text: str) -> str:
    """Rendered content only: HTML comments and fenced code removed.

    Applied to the entry and the tree files (a table hidden in a comment or a
    fence is not the entry's table).  NEVER applied to a snapshot: two of the
    six pages document the field only inside a fenced example."""
    text = re.sub(r"<!--.*?-->", "", text, flags=re.S)
    out: list[str] = []
    in_fence = False
    for line in text.splitlines():
        if re.match(r"^\s*```", line):
            in_fence = not in_fence
            continue
        if not in_fence:
            out.append(line)
    return "\n".join(out)


def ws(text: str) -> str:
    """Collapse every whitespace run to one space (the ONLY quote shaping)."""
    return re.sub(r"\s+", " ", text).strip()


def word_bounded(needle: str, haystack: str) -> bool:
    """ASCII-word-bounded occurrence (a CJK character is a boundary)."""
    return re.search(
        r"(?<![A-Za-z0-9_])" + re.escape(needle) + r"(?![A-Za-z0-9_])",
        haystack) is not None


def word_bounded_ci(needle: str, haystack: str) -> bool:
    return re.search(
        r"(?<![A-Za-z0-9_])" + re.escape(needle) + r"(?![A-Za-z0-9_])",
        haystack, re.I) is not None


HEAD_MARK = "\x01h\x01"


def _fence_flags(raw_lines: list[str]) -> list[bool]:
    """True where a raw Markdown line sits inside a fenced code block (or is
    itself a fence marker): a ``#`` there is a comment, not a heading."""
    flags: list[bool] = []
    in_fence = False
    for line in raw_lines:
        if line.strip().startswith("```"):
            flags.append(True)
            in_fence = not in_fence
            continue
        flags.append(in_fence)
    return flags


def view_with_headings(name: str, raw: str) -> tuple[list[str], set[int]]:
    """The plan's snapshot text view PLUS the indices of its heading lines.

    The view text is exactly what ``text_view`` produces; the heading set is
    read per SNAPSHOT SHAPE, because the view has already destroyed the tags:

    * Markdown (``.md``/``.markdown``): a heading is a view line that starts
      with ``#`` and does not sit inside a fenced code block (a ``#`` comment
      in a shell/python sample is not the page's title).
    * HTML (``.html``/``.htm``): a heading is the view line that carries a
      ``<h1>``..``<h6>`` element of the raw bytes.  The opening tag is replaced
      by HEAD_MARK before the SAME pipeline runs, so line indices stay aligned
      with the unmarked view and the marker is dropped again from the line's
      content -- no quote ever sees a marker.
    * Anything else: no headings."""
    low = name.lower()
    lines: list[str] = []
    heads: set[int] = set()
    if low.endswith((".html", ".htm")):
        raw = re.sub(r"(?is)<(script|style)\b.*?</\1\s*>", " ", raw)
        marked = re.sub(r"(?is)<h[1-6]\b[^>]*>", " " + HEAD_MARK + " ", raw)
        plain = re.sub(r"(?s)</?[A-Za-z][^>]*>", " ", raw)
        marked = unescape(re.sub(r"(?s)</?[A-Za-z][^>]*>", " ", marked))
        plain = unescape(plain)
        mlines = marked.splitlines()
        plines = plain.splitlines()
        if len(mlines) != len(plines):
            mlines = plines
        for m, p in zip(mlines, plines):
            p = ws(p)
            if not p:
                continue
            is_head = HEAD_MARK in m
            content = p
            if is_head:
                rewritten = ws(m.replace(HEAD_MARK, " "))
                if rewritten == p:
                    content = rewritten
            lines.append(content)
            if is_head:
                heads.add(len(lines) - 1)
        return lines, heads
    if low.endswith((".md", ".markdown")):
        fences = _fence_flags(raw.splitlines())
        raw = raw.replace("`", "")
        raw = LIST_MARKER_RE.sub("", raw)
        for i, line in enumerate(raw.splitlines()):
            s = ws(line)
            if not s:
                continue
            lines.append(s)
            if s.startswith("#") and not (i < len(fences) and fences[i]):
                heads.add(len(lines) - 1)
        return lines, heads
    for line in raw.splitlines():
        s = ws(line)
        if s:
            lines.append(s)
    return lines, heads


def text_view(name: str, raw: str) -> list[str]:
    """The plan's snapshot text view (Q42/Q53/Q56, amended pre-data).

    ``.html``/``.htm``: script/style blocks removed, tags replaced by one
    space, entities decoded.  Markdown: every backtick byte deleted and an
    unordered-list marker removed by ``(?m)^[ \\t]{0,3}[*+\\-][ \\t]+``.
    Plain text: nothing.  Then every whitespace run is collapsed.  Fenced code
    and comments stay (see the docstring READINGS)."""
    return view_with_headings(name, raw)[0]


def shaping_named(entry_r: str) -> bool:
    """(a): one entry line names the text view the counter applies."""
    for line in entry_r.splitlines():
        low = ws(line).lower()
        if ".html" in low and "script" in low and "whitespace" in low \
                and ("entit" in low or "decod" in low) \
                and ("backtick" in low or "inline" in low):
            return True
    return False


CITED_TAIL_RE = re.compile(r"-[A-Za-z]")


def cited_sids(text: str) -> list[str]:
    """``S###`` ids that cite a registry row, in order, deduplicated.

    An id glued to a slug (``S226-spec.html``) is a snapshot file name, not a
    citation of that row, so it is skipped."""
    out: list[str] = []
    for m in SID_RE.finditer(text):
        if CITED_TAIL_RE.match(text, m.end()):
            continue
        if m.group(0) not in out:
            out.append(m.group(0))
    return out


def clean(cell: str) -> str:
    """Cell comparison form: drop emphasis/backticks, collapse, lower-case."""
    return ws(re.sub(r"[`*]", "", cell)).lower()


def _split_cells(s: str) -> list[str]:
    """Split one table row on unescaped ``|`` and drop the escape backslash.

    A ``|`` written ``\\|`` inside a cell is content (pi's located quote is a
    markdown table row), not a column break."""
    cells: list[str] = []
    cur: list[str] = []
    i = 0
    while i < len(s):
        ch = s[i]
        if ch == "\\" and i + 1 < len(s) and s[i + 1] == "|":
            cur.append("|")
            i += 2
            continue
        if ch == "|":
            cells.append("".join(cur))
            cur = []
            i += 1
            continue
        cur.append(ch)
        i += 1
    cells.append("".join(cur))
    return cells


def _cells(line: str) -> list[str]:
    s = line.strip()
    if not (s.startswith("|") and s.endswith("|")) or len(s) < 2:
        return []
    return [c.strip() for c in _split_cells(s[1:-1])]


def is_separator(row: list[str]) -> bool:
    return bool(row) and all(SEPARATOR_RE.fullmatch(x) for x in row)


def tables(text: str):
    """Yield (header_cells, row_cells) for every markdown table in ``text``."""
    block: list[str] = []

    def flush():
        if not block:
            return None
        head = _cells(block[0])
        rows = []
        for ln in block[1:]:
            c = _cells(ln)
            if not c or is_separator(c):
                continue
            rows.append(c)
        block.clear()
        return head, rows

    for ln in text.splitlines():
        if ln.strip().startswith("|"):
            block.append(ln)
            continue
        got = flush()
        if got is not None:
            yield got
    got = flush()
    if got is not None:
        yield got


# ------------------------------------------------------------- entry surface

def entry_head(text: str) -> tuple[list[str], str | None, str | None]:
    """The provenance trio: leading ``source:`` lines, then verified-at, recheck."""
    lines = text.splitlines()
    i = 0
    while i < len(lines) and not lines[i].strip():
        i += 1
    src: list[str] = []
    while i < len(lines) and lines[i].startswith("source:"):
        src.append(lines[i])
        i += 1

    def field(name: str) -> str | None:
        nonlocal i
        while i < len(lines) and not lines[i].strip():
            i += 1
        if i < len(lines) and lines[i].startswith(name + ":"):
            value = lines[i][len(name) + 1:].strip()
            i += 1
            return value or None
        return None

    return src, field("verified-at"), field("recheck")


HEADER_CLEAN = [clean(c) for c in HEADER]


def surface_tables(entry_r: str) -> list[list[list[str]]]:
    """Every table whose header cells equal the frozen five (cleaned)."""
    out: list[list[list[str]]] = []
    for head, rows in tables(entry_r):
        if [clean(c) for c in head] == HEADER_CLEAN:
            out.append(rows)
    return out


def surface_of(cell: str, surfaces: dict) -> str | None:
    """Which frozen surface a table's first cell names (exact frozen cell)."""
    name = clean(cell)
    for key, spec in surfaces.items():
        if name == ws(spec["display"]).lower():
            return key
    return None


def surface_rows(entry_r: str, surfaces: dict) -> list[tuple[str, list[str]]]:
    """Every (surface, row) pair of the surface table, in document order."""
    out: list[tuple[str, list[str]]] = []
    for rows in surface_tables(entry_r)[:1]:
        for row in rows:
            if not row:
                continue
            key = surface_of(row[0], surfaces)
            if key:
                out.append((key, row))
    return out


def cited_ids(row: list[str]) -> list[str]:
    """The ``S###`` ids a surface row cites, in order, deduplicated."""
    found: list[str] = []
    for cell in row[1:]:
        for sid in cited_sids(cell):
            if sid not in found:
                found.append(sid)
    return found


def row_tokens(row: list[str]) -> list[str]:
    """The backticked spans of the row after the surface-name cell."""
    toks: list[str] = []
    for cell in row[1:]:
        for tok in BACKTICK_RE.findall(cell):
            t = tok.strip()
            if t and t not in toks:
                toks.append(t)
    return toks


def grant_role(token: str, page_token: str) -> bool:
    """The token carries the surface's frozen page token (a semantics cue)."""
    return word_bounded_ci(ws(page_token), ws(token))


def token_role(token: str, page_token: str) -> str:
    t = ws(token)
    if t == "allowed-tools":
        return "key"
    if grant_role(t, page_token):
        return "grant"
    if VALUE_SHAPE_RE.search(t) or " " in t or BARE_NAME_RE.match(t):
        return "value"
    return "other"


def token_forms(token: str) -> list[str]:
    """The token itself, its form without ``~/`` and each without a trailing ``/``."""
    forms = [token]
    if token.startswith("~/"):
        forms.append(token[2:])
    for f in list(forms):
        stripped = f.rstrip("/")
        if stripped and stripped not in forms:
            forms.append(stripped)
    return [f for f in forms if f]


def quote_of(row: list[str]) -> tuple[str | None, str | None]:
    """(d): the row's located quote: (quote, note)."""
    if len(row) <= 4:
        return None, "row carries no located-quote cell"
    cell = row[4]
    spans: list[str] = []
    for q in QUOTE_RE.findall(cell):
        n = ws(q)
        if n and n not in spans:
            spans.append(n)
    if len(spans) > 1:
        return None, (f"{len(spans)} distinct located quote(s) in one cell "
                      f"(want exactly 1)")
    if spans:
        quote = spans[0]
    else:
        quote = ws(cell)
        if not quote or set(quote) <= set("-"):
            return None, "located-quote cell is empty"
    words = len(quote.split())
    if not MIN_QUOTE_WORDS <= words <= MAX_QUOTE_WORDS:
        return None, (f"located quote is {words} words "
                      f"(want {MIN_QUOTE_WORDS}-{MAX_QUOTE_WORDS})")
    return quote, None


def page_key(url: str) -> tuple[str, str]:
    """Host + path of a page, ignoring a trailing ``/`` and the query/fragment."""
    parts = urllib.parse.urlsplit(url)
    return ((parts.hostname or "").lower(),
            urllib.parse.unquote(parts.path or "").rstrip("/").lower())


def same_page(a: str, b: str) -> bool:
    """Two URL forms of one page: identical host+path, or a Markdown route.

    The L1 froze factory's canonical page as `docs.factory.com/harness/skills`
    with its snapshot taken from the same page's `.md` route, so a bare `.md`
    suffix on one side is the same page and nothing else is."""
    ka, kb = page_key(a), page_key(b)
    if ka == kb:
        return True
    if ka[0] != kb[0]:
        return False
    return ka[1] + ".md" == kb[1] or kb[1] + ".md" == ka[1]


def source_line(entry_r: str, sid: str) -> str | None:
    """The entry's own ``source:`` line that names one cited id."""
    for line in entry_r.splitlines():
        if line.startswith("source:") and sid in cited_sids(line):
            return line
    return None


def entry_problems(entry_r: str, surfaces: dict) -> list[str]:
    """Entry-level (a): trio, frozen header, shaping, source-line coverage."""
    notes: list[str] = []
    found = surface_tables(entry_r)
    if not found:
        return ["no table in the entry has the frozen header "
                + " | ".join(HEADER)]
    if len(found) > 1:
        return [f"{len(found)} tables have the frozen header (want exactly 1)"]
    rows = surface_rows(entry_r, surfaces)
    if not rows:
        return ["the surface table names none of "
                + ", ".join(s["display"] for s in surfaces.values())]
    src, verified, recheck = entry_head(entry_r)
    if not src:
        notes.append("entry does not open with source: lines")
    if not verified:
        notes.append("entry has no verified-at: line after its source: lines")
    if not recheck:
        notes.append("entry has no recheck: line after verified-at:")
    if not shaping_named(entry_r):
        notes.append("entry does not name the snapshot text view (one line "
                     "with `.html`, `script`, entities/decoded and "
                     "`whitespace`)")
    cited: list[str] = []
    for _key, row in rows:
        for sid in cited_ids(row):
            if sid not in cited:
                cited.append(sid)
    if not cited:
        notes.append("the surface table cites no S### id")
    head: set[str] = set()
    for line in src:
        head.update(cited_sids(line.split("located quote")[0]))
    missing = [s for s in cited if s not in head]
    if missing:
        notes.append("cited " + ", ".join(missing) + " absent from the "
                     "entry's own source: lines (cited ids must be a subset "
                     "of them)")
    return notes


# ------------------------------------------------------------------ git side

def _default_repo() -> Path:
    here = Path(__file__).resolve()
    for cand in [here.parent.parent, *here.parents]:
        if (cand / SOURCES).is_file():
            return cand
    return here.parent.parent


def _git(repo: Path, args: list[str]) -> subprocess.CompletedProcess:
    try:
        return subprocess.run(["git", "-C", str(repo), *args],
                              capture_output=True)
    except OSError as exc:
        raise EnvError(f"git not runnable: {exc}") from exc


def mktemp(prefix: str) -> str:
    """A temp dir honouring TMPDIR and ``--work`` (never a hardcoded /tmp)."""
    return tempfile.mkdtemp(prefix=prefix, dir=_WORK)


class Repo:
    """Committed bytes of one lane at one revision (read-only)."""

    def __init__(self, path: Path, rev: str):
        self.path, self.rev = path, rev
        self._manifest: dict[str, str] | None = None

    def show_at(self, rev: str, path: str) -> str | None:
        proc = _git(self.path, ["show", f"{rev}:{path}"])
        if proc.returncode == 0:
            return proc.stdout.decode("utf-8", "replace")
        err = proc.stderr.decode("utf-8", "replace")
        if "does not exist" in err or "exists on disk, but not in" in err \
                or "Path '" in err:
            return None
        raise EnvError(f"git show {rev}:{path} failed: {err.strip()}")

    def show(self, path: str) -> str | None:
        return self.show_at(self.rev, path)

    def raw_snapshot(self, name: str) -> bytes | None:
        proc = _git(self.path, ["show", f"{self.rev}:{SNAPDIR}/{name}"])
        return proc.stdout if proc.returncode == 0 else None

    def list_dir(self, subdir: str) -> list[str]:
        """Basenames committed in one directory at ``self.rev``."""
        prefix = subdir.rstrip("/") + "/"
        proc = _git(self.path, ["ls-tree", "-r", "--name-only", self.rev,
                                prefix])
        if proc.returncode != 0:
            return []
        out: list[str] = []
        for line in proc.stdout.decode("utf-8", "replace").splitlines():
            if line.startswith(prefix):
                out.append(line[len(prefix):])
        return out

    @staticmethod
    def _parse_pins(text: str, source: str) -> dict[str, str]:
        out: dict[str, str] = {}
        for n, line in enumerate(text.splitlines(), 1):
            s = line.strip()
            if not s or s.startswith("#"):
                continue
            m = re.fullmatch(r"([0-9a-f]{64})[ \t]+\*?(\S(?:.*\S)?)", s)
            if not m:
                raise EnvError(f"{source}:{n} is not `<sha256> <basename>`: "
                               f"{s!r}")
            sha, name = m.group(1), m.group(2)
            pure = Path(name)
            if pure.is_absolute() or name.startswith("/") or ".." in pure.parts:
                raise EnvError(f"{source}:{n} pins {name!r}, which escapes "
                               f"{SNAPDIR}/")
            if name in out and out[name] != sha:
                raise EnvError(f"{source}:{n} pins {name!r} to a second "
                               f"digest {sha} (first {out[name]})")
            out[name] = sha
        return out

    def manifest(self) -> dict[str, str]:
        """``basename -> sha256`` from the committed pin set (exit 2 if none).

        The plan names the aggregate ``MANIFEST.sha256``; the round-79 wave
        committed the same six pins as one ``<id>.manifest`` file per page in
        the same directory.  Either source is accepted, and when both are
        committed they must agree basename by basename -- a pin that pins two
        digests pins nothing, so a disagreement is exit 2."""
        if self._manifest is not None:
            return self._manifest
        agg = self.show(MANIFEST)
        out = self._parse_pins(agg, MANIFEST) if agg is not None else {}
        per: dict[str, str] = {}
        for name in self.list_dir(SNAPDIR):
            if not PER_MANIFEST_RE.match(name):
                continue
            text = self.show(f"{SNAPDIR}/{name}")
            if text is None:
                continue
            for base, sha in self._parse_pins(
                    text, f"{SNAPDIR}/{name}").items():
                if base in per and per[base] != sha:
                    raise EnvError(f"{SNAPDIR}/{name} pins {base!r} to a "
                                   f"second digest {sha} (first {per[base]})")
                per[base] = sha
        for base, sha in per.items():
            if base in out and out[base] != sha:
                raise EnvError(f"the pin of {base!r} disagrees between "
                               f"{MANIFEST} ({out[base]}) and the per-page "
                               f".manifest files ({sha})")
        if not out:
            out = per
        if not out:
            raise EnvError(f"no pin manifest at {SNAPDIR} at {self.rev}: "
                           f"neither {MANIFEST} nor a per-page <id>.manifest "
                           f"is committed, so (c) cannot be evaluated")
        self._manifest = out
        return out

    def snapshot_name(self, entry_r: str, sid: str) -> str:
        """The pinned snapshot file that carries one cited row's page.

        The pin binds by the snapshot file name's own id prefix (``S226`` ->
        ``S226-spec.md``), which is deterministic and immune to entry prose
        naming several snapshots on one line; when no pin carries the id
        prefix, the entry's own backticked names decide (exactly one)."""
        man = self.manifest()
        pref = sorted(p for p in man
                      if re.match(rf"^{re.escape(sid)}(?![0-9])",
                                  p.rsplit("/", 1)[-1]))
        if len(pref) == 1:
            return pref[0]
        if len(pref) > 1:
            raise EnvError(f"{sid}: {len(pref)} pinned snapshots begin with "
                           f"{sid} ({', '.join(pref)}) — the pin of one row is "
                           f"ambiguous")
        named: list[str] = []
        for line in entry_r.splitlines():
            if sid not in SID_RE.findall(line):
                continue
            for tok in BACKTICK_RE.findall(line):
                base = tok.strip().split(":", 1)[0].strip().rsplit("/", 1)[-1]
                if base in man and base not in named:
                    named.append(base)
        if len(named) == 1:
            return named[0]
        if len(named) > 1:
            raise EnvError(f"{sid}: the entry names {len(named)} pinned "
                           f"snapshots ({', '.join(named)}) — the pin of one "
                           f"row is ambiguous")
        raise EnvError(f"{sid}: no snapshot is pinned for this row in "
                       f"{SNAPDIR}")

    def read_snapshot(self, name: str, sha: str) -> str:
        raw = self.raw_snapshot(name)
        if raw is None:
            raise EnvError(f"snapshot {SNAPDIR}/{name} not committed at "
                           f"{self.rev}")
        if hashlib.sha256(raw).hexdigest() != sha:
            raise EnvError(f"snapshot_tampered: {SNAPDIR}/{name}")
        return raw.decode("utf-8", "replace")


# ------------------------------------------------------------- registry side

def registry_rows(text: str) -> dict[str, list[list[str]]]:
    """id -> registry rows (raw cells; the cell count is judged later)."""
    rows: dict[str, list[list[str]]] = {}
    for line in text.splitlines():
        if REGISTRY_RE.match(line):
            cells = _cells(line)
            if cells:
                rows.setdefault(cells[0], []).append(cells)
    return rows


def urls_of(cell: str) -> list[str]:
    return [m.group(0).rstrip(TRIM_CHARS) for m in URL_RE.finditer(cell)]


def host_ok(url: str, pins: tuple[str, ...]) -> bool:
    """Exact host for a bare pin; host + whole-segment path prefix for a pin
    carrying one (``raw.githubusercontent.com/badlogic/pi-mono`` does not
    accept ``.../pi-mono-evil``)."""
    try:
        parts = urllib.parse.urlsplit(url)
    except ValueError:
        return False
    host = (parts.hostname or "").lower()
    path = urllib.parse.unquote(parts.path or "").lower()
    if any(seg in (".", "..") for seg in path.split("/")):
        return False
    if not path.startswith("/"):
        path = "/" + path
    for pin in pins:
        h, _, p = pin.partition("/")
        if p:
            prefix = "/" + p.lower().rstrip("/")
            if host == h.lower() and (path == prefix
                                      or path.startswith(prefix + "/")):
                return True
        elif host == h.lower():
            return True
    return False


def registry_problems(registry: dict[str, list[list[str]]], key: str,
                      sid: str, surfaces: dict) -> list[str]:
    """(b) for one cited id of one surface."""
    spec = surfaces[key]
    rows = registry.get(sid, [])
    if len(rows) != 1:
        return [f"{sid}: {len(rows)} registry rows in {SOURCES} "
                f"(want exactly 1)"]
    row = rows[0]
    if len(row) != REGISTRY_CELLS:
        return [f"{sid}: {len(row)} cells (want exactly {REGISTRY_CELLS})"]
    notes: list[str] = []
    if row[7].strip() != "mined":
        notes.append(f"{sid}: status {row[7].strip()!r} (want 'mined')")
    if row[3].strip() not in ("A", "B"):
        notes.append(f"{sid}: tier {row[3].strip()!r} (want A or B)")
    listed = [c.strip() for c in row[10].split(",")]
    if ENTRY not in listed:
        notes.append(f"{sid}: used-by {row[10].strip()!r} does not list {ENTRY}")
    urls = urls_of(row[1])
    if not urls:
        notes.append(f"{sid}: source cell holds no URL")
    elif not any(host_ok(u, spec["hosts"]) for u in urls):
        notes.append(f"{sid}: no URL on {key}'s pinned host(s) "
                     f"{list(spec['hosts'])}: {urls}")
    return notes


# -------------------------------------------------------------------- verdict

class Ctx:
    def __init__(self, repo: Repo, entry_r: str,
                 registry: dict[str, list[list[str]]],
                 rows: list[tuple[str, list[str]]]):
        self.repo, self.entry_r = repo, entry_r
        self.registry, self.rows = registry, rows
        self.surfaces = SURFACES
        self._pages: dict[str, tuple[str, str]] = {}   # sid -> (name, text)
        self._all: list[tuple[str, str]] | None = None

    def page(self, entry_r: str, sid: str) -> tuple[str, str]:
        """(snapshot name, raw text) of a cited id, pin-checked once."""
        if sid not in self._pages:
            name = self.repo.snapshot_name(entry_r, sid)
            text = self.repo.read_snapshot(name, self.repo.manifest()[name])
            self._pages[sid] = (name, text)
        return self._pages[sid]

    def other_pages(self, name: str, raw: str) -> list[tuple[str, list[str]]]:
        """(name, text-view lines) for every pinned snapshot of a DIFFERENT page."""
        if self._all is None:
            self._all = []
            for pin_name in self.repo.manifest():
                data = self.repo.raw_snapshot(pin_name)
                if data is not None:
                    self._all.append((pin_name, data.decode("utf-8", "replace")))
        return [(n, text_view(n, text)) for n, text in self._all
                if n != name and text != raw]


def _line_of(lines: list[str], quote: str) -> tuple[int | None, str]:
    """The line index a whitespace-collapsed quote is found on (None: absent)."""
    joined = " ".join(lines)
    pos = joined.find(quote)
    if pos < 0:
        return None, joined
    off = 0
    for i, line in enumerate(lines):
        if off <= pos < off + len(line) + 1:
            return i, joined
        off += len(line) + 1
    return len(lines) - 1, joined


def quote_location(lines: list[str], quote: str,
                   heads: set[int] | None = None) -> tuple[bool, str | None]:
    """Q70: not a heading, not the first-heading block.

    ``heads`` is the snapshot's heading-line set from ``view_with_headings``;
    when it is omitted the Markdown reading (a line that starts with ``#``) is
    used, which is the same set for a Markdown snapshot."""
    idx, _joined = _line_of(lines, quote)
    if idx is None:
        return False, "quote not found in the text view"
    if heads is None:
        heads = {i for i, l in enumerate(lines) if l.startswith("#")}
    if idx in heads:
        return False, ("quote lies on a heading line (a banner or subtitle, "
                       "Q70)")
    first_head = min(heads) if heads else None
    if first_head is not None and idx <= first_head + 1:
        return False, "quote lies in the first-heading block (Q70)"
    return True, None


def surface_holds(ctx: Ctx, key: str) -> tuple[bool, list[str]]:
    spec = ctx.surfaces[key]
    display = spec["display"]
    mine = [row for k, row in ctx.rows if k == key]
    if len(mine) != 1:
        return False, [f"{len(mine)} surface-table row(s) name {display} "
                       f"(want exactly 1)"]
    row = mine[0]
    if len(row) != len(HEADER):
        return False, [f"{display}: {len(row)} cells (want exactly "
                       f"{len(HEADER)}: the frozen header's arity)"]
    notes: list[str] = []
    toks = row_tokens(row)
    roles = [token_role(t, spec["page_token"]) for t in toks]
    if "key" not in roles:
        notes.append("row carries no `allowed-tools` token")
    if "value" not in roles:
        notes.append("row carries no value-form token (a tool name, a "
                     "YAML/bracket list or an inline value)")
    if "grant" not in roles:
        notes.append(f"row carries no grant-semantics token (the page token "
                     f"{spec['page_token']!r})")
    if len(toks) < MIN_TOKENS:
        notes.append(f"row carries {len(toks)} backticked token(s) "
                     f"(want >= {MIN_TOKENS}): {toks}")
    ids = cited_ids(row)
    if not ids:
        notes.append("row cites no S### id")
    if notes:
        return False, notes

    for sid in ids:
        notes.extend(registry_problems(ctx.registry, key, sid, ctx.surfaces))
    if notes:
        return False, notes

    for sid in ids:
        row_ = ctx.registry[sid][0]
        want = urls_of(row_[1])
        line = source_line(ctx.entry_r, sid)
        if line is None:
            notes.append(f"{sid}: no source: line in the entry names it")
            continue
        if want and not any(same_page(u, want[0]) for u in urls_of(line)):
            notes.append(f"{sid}: the entry's source: line carries no URL for "
                         f"the cited page {want[0]} — the pinned snapshot is "
                         f"not demonstrably the page the row cites")
    if notes:
        return False, notes

    pages: list[tuple[str, str, str]] = []       # (sid, name, raw)
    for sid in ids:
        name, raw = ctx.page(ctx.entry_r, sid)
        pages.append((sid, name, raw))

    verified = entry_head(ctx.entry_r)[1]
    for sid in ids:
        row_ = ctx.registry[sid][0]
        if row_[8].strip() != CAPTURE or verified != CAPTURE:
            notes.append(f"{sid}: opened {row_[8].strip()!r} / entry "
                         f"verified-at {verified!r} is not the round date "
                         f"{CAPTURE}: the row was not opened this round")
        m = FETCHED_RE.search(row_[5])
        pin = ctx.repo.manifest()[ctx.page(ctx.entry_r, sid)[0]]
        if not m:
            notes.append(f"{sid}: anchor cell carries no 'fetched <date>, "
                         f"HTTP 200, <bytes> B, sha256 <hex>' record")
        elif m.group(3) != pin:
            notes.append(f"{sid}: anchor sha256 {m.group(3)[:12]}... is not the "
                         f"snapshot's pin {pin[:12]}...")

    views = [(name, text_view(name, raw)) for _sid, name, raw in pages]
    for tok in toks:
        forms = token_forms(tok)
        if not any(word_bounded(f, " ".join(lines))
                   for f in forms for _n, lines in views):
            notes.append(f"token {tok!r} does not occur word-bounded in the "
                         f"snapshot(s) of {', '.join(ids)}")

    quote, note = quote_of(row)
    if note:
        notes.append(note)
    elif "allowed-tools" not in quote:
        notes.append(f"located quote does not contain the token "
                     f"`allowed-tools`: {quote!r}")
    elif not word_bounded("allowed-tools", quote):
        notes.append(f"located quote does not contain `allowed-tools` "
                     f"word-bounded: {quote!r}")
    else:
        # The quote is matched as written; when it is not found, the counter
        # retries once with every backtick byte deleted, because the Markdown
        # text view deletes backticks and an author who backticks the cell must
        # not be punished for formatting.  Two forms only, no other shaping.
        cands: list[str] = []
        for c in (ws(quote), ws(quote.replace("`", ""))):
            if c and c not in cands:
                cands.append(c)
        located = False
        for sid_, name, raw in pages:
            lines, heads = view_with_headings(name, raw)
            q = next((c for c in cands
                      if quote_location(lines, c, heads)[0]), None)
            if q is None:
                why = quote_location(lines, cands[0], heads)[1]
                if why and not why.startswith("quote not found"):
                    notes.append(f"{name}: {why}")
                    located = True
                    break
                continue
            shared = next((other_name for other_name, other_lines in
                           ctx.other_pages(name, raw)
                           if any(q in line for line in other_lines)), None)
            if shared:
                notes.append(f"{name}: the located quote is a shared banner "
                             f"line (it also occurs in {shared}, a different "
                             f"page): Q70")
            located = True
            break
        if not located:
            notes.append(f"located quote not found in its pinned snapshot "
                         f"after the text view: {cands[0]!r}")

    # (f): grant label + the page token inside the quote
    if len(row) > 3:
        cell = row[3]
        if "`" in cell:
            notes.append("grant cell is backticked (it must be plain text)")
        plain = clean(cell)
        hits = [lab for lab in GRANT_LABELS if word_bounded_ci(lab, plain)]
        if len(hits) != 1:
            notes.append(f"grant cell {cell.strip()!r} carries {len(hits)} "
                         f"frozen label(s) {hits} (want exactly 1)")
        elif hits[0] != spec["grant"]:
            notes.append(f"grant label {hits[0]!r} is not {key}'s frozen label "
                         f"{spec['grant']!r}")
        if quote and not word_bounded_ci(ws(spec["page_token"]), ws(quote)):
            notes.append(f"located quote does not carry the page token "
                         f"{spec['page_token']!r} that grounds the grant")
    return (not notes), notes


def held_at_base(repo: Repo) -> int:
    """Surfaces whose frozen host table already appears in the base registry."""
    base = repo.show_at(BASE_REV, SOURCES)
    if base is None:
        raise EnvError(f"{SOURCES} unreadable at base {BASE_REV}")
    rows = registry_rows(rendered(base))
    held = 0
    for _key, spec in SURFACES.items():
        if any(host_ok(u, spec["hosts"])
               for cells in rows.values() for row in cells
               for u in urls_of(row[1] if len(row) > 1 else "")):
            held += 1
    return held


def opened_count(ctx: Ctx) -> int:
    """(e) as a printed figure: surfaces whose cited rows were opened this round."""
    verified = entry_head(ctx.entry_r)[1]
    n = 0
    for key in ctx.surfaces:
        mine = [row for k, row in ctx.rows if k == key]
        if len(mine) != 1:
            continue
        ids = cited_ids(mine[0])
        if not ids:
            continue
        rows = [ctx.registry.get(sid, []) for sid in ids]
        if any(len(r) != 1 or len(r[0]) <= 8 for r in rows):
            continue
        if verified == CAPTURE and all(r[0][8].strip() == CAPTURE for r in rows):
            n += 1
    return n


def check(repo: Repo) -> tuple[int, list[str], list[str], int]:
    """(N, findings, documented surfaces, opened-this-round count)."""
    sources = repo.show(SOURCES)
    if sources is None:
        raise EnvError(f"{SOURCES} absent at {repo.rev}")
    entry_text = repo.show(ENTRY)
    if entry_text is None:
        return 0, [f"entry {ENTRY} absent at {repo.rev} (the frozen path is "
                   f"the entry's only home)"], [], 0
    entry_r = rendered(entry_text)
    problems = entry_problems(entry_r, SURFACES)
    if problems:
        return 0, problems, [], 0
    ctx = Ctx(repo, entry_r, registry_rows(rendered(sources)),
              surface_rows(entry_r, SURFACES))
    n, findings, documented = 0, [], []
    for key in SURFACE_ORDER:
        ok, notes = surface_holds(ctx, key)
        if ok:
            n += 1
            documented.append(key)
        else:
            findings.extend(f"{key}: {x}" for x in notes)
    return n, findings, documented, opened_count(ctx)


# ------------------------------------------------------------ tree conjuncts

def surfaces_named(text: str) -> int:
    """How many frozen surfaces a line names (display name or frozen key)."""
    return sum(1 for key, spec in SURFACES.items()
               if word_bounded_ci(spec["display"], text)
               or word_bounded_ci(key, text))


def skill_rule_ok(text: str | None) -> bool:
    """(g) first half: one SKILL.md rule line citing the entry, >= 3 surfaces."""
    if not text:
        return False
    for line in rendered(text).splitlines():
        if ENTRY in line and surfaces_named(line) >= 3:
            return True
    return False


def registry_home_ok(text: str | None) -> bool:
    """(g) second half: a gate row with eight non-empty fields for this counter."""
    if not text:
        return False
    for line in rendered(text).splitlines():
        if line.startswith("| `" + COUNTER_PATH + "`"):
            cells = _cells(line)
            return len(cells) == SKILL_CELLS and all(c.strip() for c in cells) \
                and cells[1].strip() == "gate"
    return False


def province_bullets(text: str | None) -> list[str]:
    """(h): the ``## Core`` bullets of PROVINCE.md, continuation lines joined."""
    if not text:
        return []
    lines = rendered(text).splitlines()
    start = next((i for i, l in enumerate(lines)
                  if re.match(r"^## Core\s*$", l)), None)
    if start is None:
        return []
    end = next((i for i in range(start + 1, len(lines))
                if lines[i].startswith("## ")), len(lines))
    bullets: list[str] = []
    for line in lines[start + 1:end]:
        if line.startswith("- "):
            bullets.append(line)
        elif line.strip() and bullets and line.startswith("  "):
            bullets[-1] += " " + line.strip()
    return bullets


def province_state(text: str | None) -> tuple[int, int]:
    """(bullets naming the entry, surfaces the one such bullet names)."""
    naming = [b for b in province_bullets(text) if ENTRY in b]
    named = surfaces_named(naming[0]) if len(naming) == 1 else 0
    return len(naming), named


# -------------------------------------------------------- the generator world
# Q71/Q74 for round 80: the measured claim is FORM-LEVEL, and this generator
# writes the COMPLETE proposed evidence shape for the six surfaces from the
# measured revision's own committed bytes plus the plan's frozen surface table.
# It is scored by the SAME check(), and its score is PRINTED beside the headline
# and NEVER gates the exit predicate: a claim whose generator world reaches the
# target says so in the printed line and hands the grant-semantics judgement to
# the non-author reviewers the third printed line names.

MECH_STOP = frozenset((
    "the", "and", "for", "with", "that", "this", "field", "frontmatter",
    "skill", "skills", "is", "are", "of", "to", "a", "an", "in", "it",
    "documented", "here", "page", "states", "own", "words", "example",
    "examples", "values", "forms", "list", "no", "none", "yes", "true",
    "false", "null", "optional", "required", "default", "name", "tool",
    "tools", "string", "strings", "value", "type", "support", "varies",
))


def _mech_quote(lines: list[str], heads: set[int],
                spec: dict) -> str | None:
    """The mechanical quote: the first 5..25-word window that starts at the
    field token, carries the surface's frozen page token and passes this
    counter's own Q70 locator (no judgement about which sentence is the claim).
    """
    words: list[str] = []
    for line in lines:
        words.extend(line.split())
    ptok = ws(spec["page_token"])
    for i, w in enumerate(words):
        if not word_bounded("allowed-tools", w):
            continue
        for width in range(MIN_QUOTE_WORDS, MAX_QUOTE_WORDS + 1):
            if i + width > len(words):
                break
            cand = ws(" ".join(words[i:i + width]))
            if not word_bounded_ci(ptok, cand):
                continue
            if quote_location(lines, cand, heads)[0]:
                return cand
    return None


def _mech_value(quote: str, spec: dict) -> str | None:
    """The value-form token the mechanical row carries: the first token in the
    quote that fills the value role (not the key, not the surface's page token,
    not a stopword), a value shape first, then a capitalised bare name, then
    any bare name."""
    seen_key = False
    cands: list[tuple[int, int, str]] = []
    for pos, w in enumerate(re.split(r"[\s,]+", quote)):
        t = w.strip("`'\"()[]{}:;.,|*")
        if not t:
            continue
        if word_bounded("allowed-tools", t):
            seen_key = True
            continue
        if not seen_key or t.lower() in MECH_STOP:
            continue
        if token_role(t, spec["page_token"]) != "value":
            continue
        rank = 0 if VALUE_SHAPE_RE.search(t) else (
            1 if t[:1].isupper() else 2)
        cands.append((rank, pos, t))
    if not cands:
        return None
    return min(cands)[2]


def _mech_tokens(quote: str, spec: dict, lines: list[str]) -> list[str]:
    """The mechanical row's tokens: key, a value form, the page token if any."""
    toks = ["allowed-tools"]
    value = _mech_value(quote, spec)
    if value:
        toks.append(value)
    if word_bounded_ci(ws(spec["page_token"]), " ".join(lines)):
        toks.append(spec["page_token"])
    return toks


def generator_world(repo: Repo) -> tuple[int, str]:
    """(M, note): the generator world's score under the frozen predicate."""
    try:
        man = repo.manifest()
    except EnvError as exc:
        return 0, f"no pinned snapshots ({exc})"
    reg_text = repo.show(SOURCES)
    if reg_text is None:
        return 0, f"{SOURCES} absent"
    reg = registry_rows(rendered(reg_text))
    snaps: dict[str, tuple[str, str]] = {}      # sid -> (basename, raw text)
    rows: list[list[str]] = []
    keys: dict[str, str] = {}                   # sid -> surface key
    for key in SURFACE_ORDER:
        spec = SURFACES[key]
        pick: tuple[str, list[str], str, bytes] | None = None
        for sid in sorted(reg):
            rr = reg[sid]
            if len(rr) != 1 or len(rr[0]) != REGISTRY_CELLS:
                continue
            if not any(host_ok(u, spec["hosts"]) for u in urls_of(rr[0][1])):
                continue
            names = sorted(p for p in man
                           if re.match(rf"^{re.escape(sid)}(?![0-9])",
                                       p.rsplit("/", 1)[-1]))
            if len(names) != 1:
                continue
            data = repo.raw_snapshot(names[0])
            if data is None:
                continue
            pick = (sid, list(rr[0]), names[0], data)
            break
        if pick is None:
            continue
        sid, row, name, data = pick
        text = data.decode("utf-8", "replace")
        lines, heads = view_with_headings(name, text)
        quote = _mech_quote(lines, heads, spec)
        if quote is None:
            continue
        if _mech_value(quote, spec) is None:
            continue
        row[10] = ENTRY
        row[8] = CAPTURE
        row[5] = ("§ generator world; fetched %s, HTTP 200, %d B, sha256 %s"
                  % (CAPTURE, len(data), hashlib.sha256(data).hexdigest()))
        rows.append(row)
        snaps[sid] = (name, text)
        keys[sid] = key
    return _score_world(rows, snaps, keys)


def _score_world(rows: list[list[str]], snaps: dict[str, tuple[str, str]],
                 keys: dict[str, str]) -> tuple[int, str]:
    """Build the mechanical world in a temp repo and score it with check()."""
    if not rows:
        return 0, "no surface page yielded a mechanical quote"
    files: dict[str, str] = {
        ENTRY: _mech_entry(rows, snaps, keys),
        SOURCES: _registry_of(rows),
        MANIFEST: "".join(
            f"{hashlib.sha256(t.encode()).hexdigest()}  {name}\n"
            for name, t in snaps.values()),
        PROVINCE: mech_province(),
        SKILLMD: mech_skill(),
    }
    for name, text in snaps.values():
        files[f"{SNAPDIR}/{name}"] = text
    d = mktemp("k80-c2-generator-")
    try:
        _commit_tree(Path(d), files)
        n, _findings, _documented, _opened = check(Repo(Path(d), "HEAD"))
    finally:
        shutil.rmtree(d, ignore_errors=True)
    return n, "generated mechanically from the measured bytes"


def _mech_entry(rows: list[list[str]], snaps: dict[str, tuple[str, str]],
                keys: dict[str, str]) -> str:
    head: list[str] = []
    for row in rows:
        sid = row[0]
        url = (urls_of(row[1]) or ["https://example.invalid/"])[0]
        name, text = snaps[sid]
        quote = _mech_quote(*view_with_headings(name, text),
                            SURFACES[keys[sid]]) or ""
        head.append(f'source: {sid} — generator scrape — {url} — located '
                    f'quote "{quote}" (snapshot `{name}`)')
    body = ["", f"verified-at: {CAPTURE}", "recheck: 90d — re-fetch",
            "",
            "Text view: `.html` snapshots have `script` and `style` blocks "
            "removed, tags replaced by one space and entities decoded; "
            "Markdown snapshots have every backtick deleted and an "
            "unordered-list marker removed at a line start; every snapshot "
            "then has whitespace collapsed.",
            "",
            "## Surfaces", "",
            "| " + " | ".join(HEADER) + " |",
            "|" + "---|" * len(HEADER) + "|"]
    for row in rows:
        sid = row[0]
        spec = SURFACES[keys[sid]]
        name, text = snaps[sid]
        lines, heads = view_with_headings(name, text)
        quote = _mech_quote(lines, heads, spec) or ""
        toks = [f"`{t}`" for t in _mech_tokens(quote, spec, lines)]
        body.append(f"| {spec['display']} | {sid} | " + ", ".join(toks)
                    + f" | {spec['grant']} | \"{_escape_cell(quote)}\" |")
    return "\n".join(head + body) + "\n"


def _registry_of(rows: list[list[str]]) -> str:
    head = ("| id | source | kind | tier | scope | anchor | teaches | status | "
            "opened | recheck | used-by |")
    sep = "|" + "---|" * REGISTRY_CELLS
    return ("# SOURCES (generator world)\n\n## Registry\n\n" + head + "\n"
            + sep + "\n" + "\n".join("| " + " | ".join(r) + " |"
                                     for r in rows) + "\n")


def _commit_tree(root: Path, files: dict[str, str]) -> None:
    root.mkdir(parents=True, exist_ok=True)
    env = dict(os.environ, GIT_AUTHOR_NAME="t", GIT_AUTHOR_EMAIL="t@t",
               GIT_COMMITTER_NAME="t", GIT_COMMITTER_EMAIL="t@t")
    git = ["git", "-c", "commit.gpgsign=false", "-C", str(root)]
    subprocess.run(git + ["init", "-q"], check=True, capture_output=True)
    top = subprocess.run(git + ["rev-parse", "--show-toplevel"], check=True,
                         capture_output=True, text=True)
    if Path(top.stdout.strip()).resolve() != root.resolve():
        raise RuntimeError(f"fixture toplevel {top.stdout.strip()!r} != {root}")
    for rel, text in files.items():
        p = root / rel
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(text)
    subprocess.run(git + ["add", "-A"], check=True, capture_output=True)
    subprocess.run(git + ["commit", "-qm", "world", "--allow-empty"],
                   check=True, capture_output=True, env=env)


# ---------------------------------------------------------------- self-test
# Every world is an isolated local git repo under a fresh mktemp dir with TWO
# commits: the first is the "base" state the do-nothing figure is read from,
# the second the measured tip.  No lane, fleet repo or shared index is touched.

# Fixture pages: id, URL, snapshot basename, one per frozen surface.
FIX = {
    "spec": ("S226", "https://agentskills.io/specification.md",
             "S226-spec.html"),
    "claude": ("S227", "https://code.claude.com/docs/en/skills.md",
               "S227-claude.md"),
    "factory": ("S228", "https://docs.factory.com/harness/skills",
                "S228-factory.md"),
    "msaf": ("S229", "https://learn.microsoft.com/en-us/agent-framework/"
                     "agents/skills", "S229-msaf.md"),
    "pi": ("S230", "https://raw.githubusercontent.com/badlogic/pi-mono/main/"
                   "packages/coding-agent/docs/skills.md", "S230-pi.md"),
    "vibe": ("S231", "https://raw.githubusercontent.com/mistralai/mistral-vibe/"
                     "main/README.md", "S231-vibe.md"),
}
VALUE = {"spec": "Bash(git:*)", "claude": "Bash", "factory": "Bash",
         "msaf": "Bash", "pi": "Read", "vibe": "ask_user_question"}


def _quote(key: str, spec: dict) -> str:
    """The located quote in its TRANSFORMED form (the form the plan freezes).

    pi's page states the field in a markdown table row (a literal ``|``), and
    vibe's page states it as a YAML block list (markdown list markers), so
    both quotes are written after the text view, exactly as S226's frozen
    quote is."""
    if key == "pi":
        return f"allowed-tools | {spec['page_token']} pre-approved tool list"
    if key == "vibe":
        return "allowed-tools: read grep edit ask_user_question"
    return (f"The allowed-tools field of {spec['display']} is documented here "
            f"and this page states {spec['page_token']} in its own words")


def _page(key: str, spec: dict) -> str:
    """A fixture page whose text view contains ``_quote(key, spec)``.

    Markdown pages write the field inside inline code, the vibe page as a
    block list and the pi page as a table row, so the amended text view
    (backtick deletion, list-marker removal) is exercised by the honest world
    itself rather than only by a broken arm."""
    quote = _quote(key, spec)
    value = VALUE[key]
    if key == "spec":
        return (
            "<!doctype html>\n<html><head><title>Open specification</title>\n"
            "<script>var decoy = \"allowed-tools is not stated here\";"
            "</script>\n<style>.nav{color:red}</style>\n</head><body>\n"
            f"<h1>{spec['display']} skills</h1>\n"
            "<h2>The allowed-tools field</h2>\n"
            "<p>" + quote.replace("allowed-tools", "allowed&#45;tools")
            + "</p>\n"
            f"<p>Example values: {value} and {value} list forms.</p>\n"
            "<h2>Placement</h2>\n<p>Skills live in the project tree.</p>\n"
            "</body></html>\n")
    if key == "pi":
        return ("\n".join([
            "# pi skills",
            "",
            "## The allowed-tools field",
            "",
            f"| `allowed-tools` | {spec['page_token']} pre-approved tool list |",
            "",
            f"Example values: {value} and {value} list forms.",
            "",
            "## Placement",
            "",
            "Skills live in the project tree.",
        ]) + "\n")
    if key == "vibe":
        return ("\n".join([
            "# Mistral Vibe skills",
            "",
            "## The allowed-tools field",
            "",
            "- `allowed-tools`:",
            "  - read",
            "  - grep",
            "  - edit",
            "  - ask_user_question",
            "",
            f"Example values: {value} list forms.",
            "",
            "## Placement",
            "",
            "Skills live in the project tree.",
        ]) + "\n")
    return ("\n".join([
        f"# {spec['display']} skills",
        "",
        "## The allowed-tools field",
        "",
        f"The `allowed-tools` field of {spec['display']} is documented here "
        f"and this page states {spec['page_token']} in its own words.",
        "",
        f"Example values: {value} and {value} list forms.",
        "",
        "## Placement",
        "",
        "Skills live in the project tree.",
    ]) + "\n")


def _anchor(sid: str, pages: dict[str, str], key: str) -> str:
    raw = pages.get(sid, pages[FIX[key][0]])
    return ("§ fixture; fetched %sT00:00:00Z, HTTP 200, %d B, sha256 %s"
            % (CAPTURE, len(raw.encode()), hashlib.sha256(raw.encode()).hexdigest()))


def _reg_line(sid: str, pages: dict[str, str], key: str, *, url: str | None = None,
              status: str = "mined", tier: str = "A", used_by: str = ENTRY,
              extra: int = 0, opened: str = CAPTURE,
              anchor: str | None = None) -> str:
    cells = [sid, f"fixture — {url or FIX[key][1]}", "docs", tier,
             "fixture scope", anchor if anchor is not None else _anchor(sid, pages, key),
             "fixture teaches cell", status, opened, "90d", used_by]
    cells += [f"extra{i}" for i in range(extra)]
    return "| " + " | ".join(cells) + " |"


REG_HEADER = ("| id | source | kind | tier | scope | anchor | teaches | "
              "status | opened | recheck | used-by |\n"
              "|" + "---|" * REGISTRY_CELLS)


def _registry(pages: dict[str, str], lines: list[str] | None = None) -> str:
    body = lines if lines is not None else [
        _reg_line(FIX[k][0], pages, k) for k in SURFACE_ORDER]
    return ("# SOURCES fixture\n\n## Registry\n\n" + REG_HEADER + "\n"
            + "\n".join(body) + "\n")


def _manifest(pages: dict[str, str]) -> str:
    return "".join(
        f"{hashlib.sha256(pages[FIX[k][0]].encode()).hexdigest()}  "
        f"{FIX[k][2]}\n" for k in SURFACE_ORDER)


def _escape_cell(text: str) -> str:
    """Encode a literal ``|`` as ``\\|`` so it is cell content, not a column."""
    return text.replace("|", "\\|")


def _entry_text(pages: dict[str, str], *, rows: dict | None = None,
                quotes: dict | None = None, trio: bool = True,
                shaping: bool = True, header: tuple = HEADER) -> str:
    head: list[str] = []
    for key in SURFACE_ORDER:
        sid, url, name = FIX[key]
        q = (quotes or {}).get(key) or _quote(key, SURFACES[key])
        head.append(f'source: {sid} — fixture page — {url} — the field '
                    f'section — located quote "{q}" (snapshot `{name}`)')
    body = [""]
    if trio:
        body += [f"verified-at: {CAPTURE}",
                 "recheck: 90d — re-fetch and confirm"]
    if shaping:
        body += ["", "Text view: `.html` snapshots have `script` and `style` "
                     "blocks removed, tags replaced by one space and entities "
                     "decoded; Markdown snapshots have every backtick deleted "
                     "and an unordered-list marker removed at a line start; "
                     "every snapshot then has whitespace collapsed."]
    body += ["", "# allowed-tools surfaces (fixture)", "",
             "## Surfaces", "",
             "| " + " | ".join(header) + " |",
             "|" + "---|" * len(header) + "|"]
    for key in SURFACE_ORDER:
        spec = SURFACES[key]
        sid = FIX[key][0]
        q = (quotes or {}).get(key) or _quote(key, spec)
        grant, toks = (rows or {}).get(key, (spec["grant"], [
            "allowed-tools", VALUE[key], spec["page_token"]]))
        if isinstance(toks, str):
            tok_cell = toks
        else:
            tok_cell = ", ".join(f"`{t}`" for t in toks)
        body.append(f"| {spec['display']} | {sid} | {tok_cell} | {grant} | "
                    f"\"{_escape_cell(q)}\" |")
    return "\n".join(head + body) + "\n"


PROVINCE_OK = ("# fixture province\n\n## Core\n\n- allowed-tools semantics "
               "per client: Open specification, Claude Code, Factory, "
               "Microsoft Agent Framework, pi and Mistral Vibe, in `" + ENTRY
               + "`, counted by the counter.\n\n## Frontier\n\n- none\n")
SKILL_OK = ("# fixture skill\n\n## Gate registry\n\n| Name | Kind | Entry command "
            "| Verdict map | Self-test | Pinned values | Write scope | Owner "
            "|\n|---|---|---|---|---|---|---|---|\n| `" + COUNTER_PATH
            + "` | gate | `python3 -B " + COUNTER_PATH + " --rev <rev>` | "
            "0=clean, 1=failed, 2=could-not-evaluate | `--self-test` | in-file "
            "| none | kotoba |\n\n## Rules\n\n- `allowed-tools` per client: "
            "Open specification, Claude Code, Factory, Microsoft Agent "
            "Framework, pi and Mistral Vibe are recorded in `" + ENTRY
            + "`.\n")


def mech_province() -> str:
    return PROVINCE_OK


def mech_skill() -> str:
    return SKILL_OK


def _honest(pages: dict | None = None, *, entry: str | None = None,
            sources: str | None = None, province: str = PROVINCE_OK,
            skill: str = SKILL_OK, manifest: str | None = None,
            extra: dict | None = None) -> dict[str, str]:
    """One honest world, built from the current frozen table."""
    pages = pages if pages is not None else {
        FIX[k][0]: _page(k, SURFACES[k]) for k in SURFACE_ORDER}
    files = {SOURCES: sources if sources is not None else _registry(pages),
             ENTRY: entry if entry is not None else _entry_text(pages),
             MANIFEST: manifest if manifest is not None else _manifest(pages),
             PROVINCE: province, SKILLMD: skill}
    for key in SURFACE_ORDER:
        files[f"{SNAPDIR}/{FIX[key][2]}"] = pages[FIX[key][0]]
    if extra:
        files.update(extra)
    return files


def _mutate(files: dict[str, str], **kw) -> dict[str, str]:
    out = dict(files)
    out.update(kw)
    return out


def _hide(row: str, opener: str, closer: str,
          files: dict[str, str] | None = None) -> str:
    """The entry with ``row`` out of the table and kept only as hidden bytes."""
    text = (files or {}).get(ENTRY) or _entry_text(
        {FIX[k][0]: _page(k, SURFACES[k]) for k in SURFACE_ORDER})
    assert row + "\n" in text, row
    return (text.replace(row + "\n", "") + "\n" + opener + "\n" + row + "\n"
            + closer + "\n")


def _row_text(key: str, pages: dict | None = None) -> str:
    spec = SURFACES[key]
    toks = ", ".join(f"`{t}`" for t in
                     ["allowed-tools", VALUE[key], spec["page_token"]])
    return (f"| {spec['display']} | {FIX[key][0]} | {toks} | {spec['grant']} | "
            f"\"{_escape_cell(_quote(key, spec))}\" |")


def _world(files: dict[str, str],
           base_files: dict[str, str] | None = None) -> tuple[str, str]:
    """A fresh isolated git repo: one base commit, then the measured commit."""
    d = mktemp("k79-c2-")
    env = dict(os.environ, GIT_AUTHOR_NAME="t", GIT_AUTHOR_EMAIL="t@t",
               GIT_COMMITTER_NAME="t", GIT_COMMITTER_EMAIL="t@t")
    git = ["git", "-c", "commit.gpgsign=false", "-C", d]
    subprocess.run(git + ["init", "-q"], check=True, capture_output=True)
    top = subprocess.run(git + ["rev-parse", "--show-toplevel"], check=True,
                         capture_output=True, text=True)
    if Path(top.stdout.strip()).resolve() != Path(d).resolve():
        raise RuntimeError(f"fixture toplevel {top.stdout.strip()!r} != {d}")

    def commit(note: str) -> str:
        subprocess.run(git + ["add", "-A"], check=True, capture_output=True)
        subprocess.run(git + ["commit", "-qm", note, "--allow-empty"],
                       check=True, capture_output=True, env=env)
        rev = subprocess.run(git + ["rev-parse", "HEAD"], check=True,
                             capture_output=True, text=True)
        return rev.stdout.strip()

    def place(items: dict[str, str | None]) -> None:
        for rel, text in items.items():
            p = Path(d) / rel
            if text is None:               # a fixture deletion, not a file
                if p.exists():
                    p.unlink()
                continue
            p.parent.mkdir(parents=True, exist_ok=True)
            p.write_text(text)

    base = base_files if base_files is not None \
        else {SOURCES: "# SOURCES fixture\n\n## Registry\n\n" + REG_HEADER + "\n"}
    place(base)
    base_sha = commit("base")
    place(files)
    commit("world")
    return d, base_sha


BASE_SOURCES = "# SOURCES fixture\n\n## Registry\n\n" + REG_HEADER + "\n"


def _world_specs() -> list[dict]:
    """One honest world, then one broken world per conjunct and per shortcut.

    The round-80 target is N == 6 of a population of 6: EVERY broken surface
    flips the verdict to exit 1, so the per-conjunct arms below assert both the
    specific finding (that is what falsifies the conjunct) and the exit code;
    the two-surface arms of the r79 draft are kept because they still assert a
    second, independent finding.  Controls that cannot be expressed as a broken
    surface (the generator world, a tampered pin, a missing pin source) assert
    their own exit.  The arms under ``round-80 counter readings`` are the
    red-before arms for this round's three counter fixes: each of them fails
    under the r79 draft's reading and passes here."""
    honest = _honest()
    pages_h = {FIX[k][0]: _page(k, SURFACES[k]) for k in SURFACE_ORDER}
    six = "allowed-tools surfaces documented 6 of 6"
    five = "allowed-tools surfaces documented 5 of 6"
    four = "allowed-tools surfaces documented 4 of 6"
    zero = "allowed-tools surfaces documented 0 of 6"
    gen = "generator world: 6 of 6"
    rider = ("semantic rider: exploratory — reviewers of record: round-80 "
             "non-author closure spot-check")
    specs: list[dict] = []
    add = specs.append

    # ---------------------------------------------------------- honest worlds
    add(dict(label="honest world scores 6 of 6", files=honest, code=0,
             line=six, finding=gen))
    add(dict(label="honest world reads 6 of 6 under a relative --repo .",
             files=honest, code=0, line=six, relative=True, finding=gen))
    add(dict(label="honest world's tree conjuncts are all green",
             files=honest, code=0, line=six,
             finding="province surfaces named 6 of 6"))
    add(dict(label="honest world prints registry home ok", files=honest,
             code=0, line=six, finding="registry home ok"))
    add(dict(label="honest world prints skill rule line ok", files=honest,
             code=0, line=six, finding="skill rule line ok"))
    add(dict(label="honest world always prints the semantic rider line",
             files=honest, code=0, line=six, finding=rider))
    add(dict(label="honest world prints the generator world's score",
             files=honest, code=0, line=six, finding=gen))
    add(dict(label="the generator world reaching the form target does not "
                    "gate the exit: it is printed and disclosed",
             files=honest, code=0, line=six,
             finding="the generator world reaches the form target (6 of 6)"))
    add(dict(label="base world (entry absent) is the do-nothing control",
             files={SOURCES: _registry(pages_h)}, code=1, line=zero,
             finding=f"entry {ENTRY} absent"))
    add(dict(label="base world (no pinned snapshots) prints the generator "
                    "world's score as 0 of 6",
             files={SOURCES: _registry(pages_h)}, code=1, line=zero,
             finding="generator world: 0 of 6"))
    add(dict(label="surface hosts already in the base registry read held 6",
             files=honest, base_files={SOURCES: _registry(pages_h)}, code=0,
             line=six, finding="held at base: 6"))
    add(dict(label="base registry with one factory pin reads held at base: 1",
             files=honest, code=0, line=six,
             base_files={SOURCES: _registry(pages_h, [
                 _reg_line("S900", pages_h, "factory",
                           url="https://docs.factory.com/harness/skills.md")])},
             finding="held at base: 1"))
    add(dict(label="factory's .md route is the same canonical pin",
             files=_mutate(honest, **{
                 SOURCES: _registry(pages_h, [
                     _reg_line(FIX[k][0], pages_h, k,
                               url="https://docs.factory.com/harness/skills.md"
                               if k == "factory" else None)
                     for k in SURFACE_ORDER]),
                 ENTRY: _entry_text(pages_h).replace(
                     "https://docs.factory.com/harness/skills —",
                     "https://docs.factory.com/harness/skills.md —")}),
             code=0, line=six))
    add(dict(label="(d) the quote spans a raw line break and is still found "
                    "(generated equivalence)", files=_honest(dict(
                        pages_h, **{FIX["claude"][0]: pages_h[
                            FIX["claude"][0]].replace(
                                "documented here and this",
                                "documented here\nand this")})),
             code=0, line=six))
    # the fixture page now writes the cue inside inline code: the quote has no
    # backtick, so only a counter that deletes every backtick can find it
    add(dict(label="(d) deleting backticks is what this quote relies on "
                    "(generated equivalence)", files=_honest(dict(
                        pages_h, **{FIX["msaf"][0]: pages_h[
                            FIX["msaf"][0]].replace(
                                "states Experimental",
                                "states `Experimental`")})),
             code=0, line=six))
    add(dict(label="(a) a .html snapshot's script block does not carry the "
                    "quote", files=_honest(dict(pages_h, **{
                        FIX["spec"][0]: (
                            "<html><head><script>var s = \""
                            + _quote("spec", SURFACES["spec"])
                            + "\";</script></head><body><h1>Open "
                            "specification</h1><p>Example values: "
                            "Bash(git:*) and Bash list forms.</p>"
                            "</body></html>\n")})),
             code=1, line=five, finding="spec: located quote not found"))

    # ---------------------------------------------------------- (a) structure
    add(dict(label="(a) surface row hidden in an HTML comment",
             files=_mutate(honest, **{ENTRY: _hide(
                 _row_text("claude"), "<!--", "-->", honest)}),
             code=1, line=five,
             finding="claude: 0 surface-table row(s) name Claude Code"))
    add(dict(label="(a) surface row hidden in a fenced block",
             files=_mutate(honest, **{ENTRY: _hide(
                 _row_text("claude"), "```text", "```", honest)}),
             code=1, line=five,
             finding="claude: 0 surface-table row(s) name Claude Code"))
    add(dict(label="(a) two rows name the same surface", files=_mutate(
        honest, **{ENTRY: _entry_text(pages_h).replace(
            "| Factory |", "| Claude Code | S227 | `allowed-tools` | "
            "experimental | \"x\" |\n| Factory |", 1)}),
        code=1, line=five, finding="2 surface-table row(s) name Claude Code"))
    add(dict(label="(a) entry without verified-at:", files=_mutate(
        honest, **{ENTRY: _entry_text(pages_h, trio=False)}),
        code=1, line=zero, finding="no verified-at: line"))
    add(dict(label="(a) entry without recheck:", files=_mutate(
        honest, **{ENTRY: _entry_text(pages_h).replace(
            "recheck: 90d — re-fetch and confirm\n", "")}),
        code=1, line=zero, finding="no recheck: line"))
    add(dict(label="(a) cited id absent from the source: lines", files=_mutate(
        honest, **{ENTRY: _entry_text(pages_h).replace(
            "source: S227 —", "source: S927 —")}),
        code=1, line=zero, finding="cited S227 absent from the entry's own "
                                   "source: lines"))
    add(dict(label="(a) entry outside corpus/knowledge is not the entry",
             files=_mutate(honest, **{
                 ENTRY: None,
                 "corpus/notes/allowed-tools-surfaces-round79.md":
                     _entry_text(pages_h)}),
             code=1, line=zero, finding=f"entry {ENTRY} absent"))
    add(dict(label="(a) entry with no surface table", files=_mutate(
        honest, **{ENTRY: "\n".join([
            f'source: {FIX[k][0]} — fixture page — {FIX[k][1]} — located '
            f'quote "{_quote(k, SURFACES[k])}" (snapshot `{FIX[k][2]}`)'
            for k in SURFACE_ORDER] + ["", f"verified-at: {CAPTURE}",
                                       "recheck: 90d",
                                       "", "Text view: `.html` snapshots have "
                                       "`script` blocks removed, tags "
                                       "replaced, entities decoded, "
                                       "backticks deleted, whitespace "
                                       "collapsed.", "",
                                       "# no table here", ""])}),
        code=1, line=zero, finding="no table in the entry has the frozen "
                                   "header"))
    add(dict(label="(a) surface table header drifted", files=_mutate(
        honest, **{ENTRY: _entry_text(pages_h, header=(
            "surface", "source", "page tokens", "permissions",
            "located quote"))}),
        code=1, line=zero, finding="no table in the entry has the frozen "
                                   "header"))
    add(dict(label="(a) surface row with six cells", files=_mutate(
        honest, **{ENTRY: _entry_text(pages_h).replace(
            "| Mistral Vibe | S231 |", "| Mistral Vibe | S231 | note |")}),
        code=1, line=five, finding="Mistral Vibe: 6 cells"))
    add(dict(label="(a) entry that does not name the text view",
             files=_mutate(honest, **{ENTRY: _entry_text(
                 pages_h, shaping=False)}),
             code=1, line=zero, finding="does not name the snapshot text view"))
    add(dict(label="(a) token the page never carries", files=_mutate(
        honest, **{ENTRY: _entry_text(pages_h, rows={
            "claude": ("pre-approves",
                       ["allowed-tools", "Bash",
                        "without prompting you for approval",
                        "ztuff?"])})}),
        code=1, line=five, finding="does not occur word-bounded"))
    add(dict(label="(a) two rows carry tokens no page carries", files=_mutate(
        honest, **{ENTRY: _entry_text(pages_h, rows={
            "claude": ("pre-approves",
                       ["allowed-tools", "Bash",
                        "without prompting you for approval", "ztuff?"]),
            "factory": ("metadata-only",
                        ["allowed-tools", "Bash", "metadata",
                         "ytuff?"])})}),
        code=1, line=four, finding="does not occur word-bounded"))
    add(dict(label="(a) row with only two tokens", files=_mutate(
        honest, **{ENTRY: _entry_text(pages_h, rows={
            "claude": ("pre-approves", ["allowed-tools", "Bash"])})}),
        code=1, line=five, finding="2 backticked token(s)"))
    add(dict(label="(a) row with no value-form token", files=_mutate(
        honest, **{ENTRY: _entry_text(pages_h, rows={
            "spec": (SURFACES["spec"]["grant"],
                     ["allowed-tools", "Experimental", "experimental"])})}),
        code=1, line=five, finding="no value-form token"))
    add(dict(label="(a) row with no grant-semantics token", files=_mutate(
        honest, **{ENTRY: _entry_text(pages_h, rows={
            "claude": ("pre-approves", ["allowed-tools", "Bash", "Read"])})}),
        code=1, line=five, finding="no grant-semantics token"))
    add(dict(label="(a) first cell is a longer client name", files=_mutate(
        honest, **{ENTRY: _entry_text(pages_h).replace(
            "| pi | S230 |", "| pi coding agent | S230 |")}),
        code=1, line=five, finding="0 surface-table row(s) name pi"))

    # --------------------------------------------------------------- (b) rows
    add(dict(label="(b) cited row is queued, not mined", files=_mutate(
        honest, **{SOURCES: _registry(pages_h, [
            _reg_line(FIX[k][0], pages_h, k,
                      status="queued" if k == "claude" else "mined")
            for k in SURFACE_ORDER])}),
        code=1, line=five, finding="S227: status 'queued'"))
    add(dict(label="(b) two cited rows are queued", files=_mutate(
        honest, **{SOURCES: _registry(pages_h, [
            _reg_line(FIX[k][0], pages_h, k,
                      status="queued" if k in ("claude", "factory")
                      else "mined") for k in SURFACE_ORDER])}),
        code=1, line=four, finding="S228: status 'queued'"))
    add(dict(label="(b) cited row is tier C", files=_mutate(
        honest, **{SOURCES: _registry(pages_h, [
            _reg_line(FIX[k][0], pages_h, k,
                      tier="C" if k == "claude" else "A")
            for k in SURFACE_ORDER])}),
        code=1, line=five, finding="S227: tier 'C'"))
    add(dict(label="(b) cited row has 12 cells", files=_mutate(
        honest, **{SOURCES: _registry(pages_h, [
            _reg_line(FIX[k][0], pages_h, k,
                      extra=1 if k == "claude" else 0)
            for k in SURFACE_ORDER])}),
        code=1, line=five, finding="S227: 12 cells"))
    add(dict(label="(b) cited row's used-by omits the entry", files=_mutate(
        honest, **{SOURCES: _registry(pages_h, [
            _reg_line(FIX[k][0], pages_h, k,
                      used_by="corpus/knowledge/other-round79.md"
                      if k == "claude" else ENTRY)
            for k in SURFACE_ORDER])}),
        code=1, line=five, finding="S227: used-by"))
    add(dict(label="(b) cited row's URL is on another host", files=_mutate(
        honest, **{SOURCES: _registry(pages_h, [
            _reg_line(FIX[k][0], pages_h, k,
                      url="https://example.invalid/skills"
                      if k == "claude" else None)
            for k in SURFACE_ORDER])}),
        code=1, line=five, finding="no URL on claude's pinned host(s)"))
    add(dict(label="(b) the assigned docs.factory.ai URL is not the canonical "
                    "pin", files=_mutate(honest, **{SOURCES: _registry(
        pages_h, [_reg_line(FIX[k][0], pages_h, k,
                            url="https://docs.factory.ai/cli/configuration/"
                                "skills" if k == "factory" else None)
                   for k in SURFACE_ORDER])}),
        code=1, line=five, finding="no URL on factory's pinned host(s)"))
    add(dict(label="(b) factory's sibling path docs.factory.com/harness/"
                    "skills-old is not the canonical page",
             files=_mutate(honest, **{SOURCES: _registry(pages_h, [
                 _reg_line(FIX[k][0], pages_h, k,
                           url="https://docs.factory.com/harness/skills-old"
                           if k == "factory" else None)
                 for k in SURFACE_ORDER])}),
             code=1, line=five, finding="no URL on factory's pinned host(s)"))
    add(dict(label="(b) sibling host raw.githubusercontent.com/badlogic/"
                    "pi-mono-evil is not the pinned repo", files=_mutate(
        honest, **{SOURCES: _registry(pages_h, [
            _reg_line(FIX[k][0], pages_h, k,
                      url="https://raw.githubusercontent.com/badlogic/"
                          "pi-mono-evil/main/docs/skills.md"
                      if k == "pi" else None)
            for k in SURFACE_ORDER])}),
        code=1, line=five, finding="no URL on pi's pinned host(s)"))
    add(dict(label="(b) two registry rows for one cited id", files=_mutate(
        honest, **{SOURCES: _registry(pages_h,
            [_reg_line(FIX[k][0], pages_h, k) for k in SURFACE_ORDER]
            + [_reg_line("S227", pages_h, "claude")])}),
        code=1, line=five, finding="S227: 2 registry rows"))
    add(dict(label="(b) staged four-cell rows appended as-is", files=_mutate(
        honest, **{SOURCES: _registry(pages_h,
            [f"| {FIX[k][0]} | {FIX[k][1]} | docs | staged |"
             for k in SURFACE_ORDER])}),
        code=1, line=zero, finding="S226: 4 cells"))

    # ----------------------------------------------------------- (c) snapshots
    add(dict(label="(c) tampered snapshot (manifest hash left)", files=_mutate(
        honest, **{f"{SNAPDIR}/{FIX['claude'][2]}":
                   pages_h[FIX["claude"][0]] + "A hand edit.\n"}),
        code=2, line="environment error", finding="snapshot_tampered"))
    add(dict(label="(c) no manifest at all", files=_mutate(
        honest, **{MANIFEST: None}), code=2, line="environment error",
        finding="no pin manifest at"))
    add(dict(label="(c) manifest line not `<sha256> <basename>`", files=_mutate(
        honest, **{MANIFEST: _manifest(pages_h) + "not-a-digest S999-x.md\n"}),
        code=2, line="environment error", finding="is not `<sha256>"))
    add(dict(label="(c) manifest path escapes the snapshot directory",
             files=_mutate(honest, **{
                 MANIFEST: _manifest(pages_h) + "0" * 64 + "  ../S999-x.md\n"}),
             code=2, line="environment error", finding="escapes"))
    add(dict(label="(c) two pinned snapshots begin with one cited id",
             files=_mutate(honest, **{
                 ENTRY: _entry_text(pages_h).replace(
                     f" (snapshot `{FIX['claude'][2]}`)", ""),
                 MANIFEST: _manifest(pages_h) + "0" * 64 + "  S227-ghost.md\n"}),
             code=2, line="environment error", finding="ambiguous"))
    add(dict(label="(c) entry source: line cites a different page on the "
                    "cited host (pin binding)", files=_mutate(
        honest, **{ENTRY: _entry_text(pages_h).replace(
            "https://code.claude.com/docs/en/skills.md",
            "https://code.claude.com/docs/en/other.md")}),
        code=1, line=five,
        finding="the entry's source: line carries no URL for the cited page"))
    add(dict(label="(c) anchor sha256 is not the snapshot pin", files=_mutate(
        honest, **{SOURCES: _registry(pages_h, [
            _reg_line(FIX[k][0], pages_h, k,
                      anchor=_anchor(FIX[k][0], pages_h, k).replace(
                          hashlib.sha256(
                              pages_h[FIX[k][0]].encode()).hexdigest(),
                          "0" * 64) if k == "claude" else None)
            for k in SURFACE_ORDER])}),
        code=1, line=five, finding="is not the snapshot's pin"))

    # --------------------------------------------------------------- (d) quote
    add(dict(label="(d) located quote under 5 words", files=_mutate(
        honest, **{ENTRY: _entry_text(pages_h, quotes={
            "claude": "allowed-tools is here"})}),
        code=1, line=five, finding="located quote is 3 words"))
    add(dict(label="(d) located quote over 25 words", files=_mutate(
        honest, **{ENTRY: _entry_text(pages_h, quotes={
            "claude": " ".join(["word"] * 26)})}),
        code=1, line=five, finding="located quote is 26 words"))
    add(dict(label="(d) located quote absent from its snapshot", files=_mutate(
        honest, **{ENTRY: _entry_text(pages_h, quotes={
            "claude": "The allowed-tools field of Claude Code says nothing "
                      "at all here"})}),
        code=1, line=five, finding="not found in its pinned snapshot"))
    add(dict(label="(d) two quotes are absent from their snapshots",
             files=_mutate(honest, **{ENTRY: _entry_text(pages_h, quotes={
                 "claude": "The allowed-tools field of Claude Code says "
                           "nothing at all here",
                 "factory": "The allowed-tools field of Factory says nothing "
                            "at all here"})}),
             code=1, line=four, finding="not found in its pinned snapshot"))
    add(dict(label="(d) located quote without the token allowed-tools",
             files=_mutate(honest, **{ENTRY: _entry_text(pages_h, quotes={
                 "claude": "this page states without prompting you for "
                           "approval in its own words exactly"})}),
             code=1, line=five, finding="does not contain the token"))
    add(dict(label="(d) quote from another surface's page", files=_mutate(
        honest, **{ENTRY: _entry_text(pages_h, quotes={
            "claude": _quote("pi", SURFACES["pi"])})}),
        code=1, line=five, finding="not found in its pinned snapshot"))
    add(dict(label="(d) quote is the page's title line (first-heading block)",
             files=_honest(dict(pages_h, **{FIX["claude"][0]: (
                 "# " + _quote("claude", SURFACES["claude"]) + "\n\n"
                 + pages_h[FIX["claude"][0]].split("\n", 1)[1])})),
             code=1, line=five, finding="quote lies on a heading line"))
    add(dict(label="(d) quote is a line shared with a different page (banner)",
             files=_honest(dict(pages_h, **{FIX["factory"][0]:
                 pages_h[FIX["factory"][0]]
                 + _quote("claude", SURFACES["claude"]) + "\n"})),
             code=1, line=five, finding="shared banner line"))

    # ----------------------------------------------------------- (e) (f) dates
    add(dict(label="(e) one row opened before the round date", files=_mutate(
        honest, **{SOURCES: _registry(pages_h, [
            _reg_line(FIX[k][0], pages_h, k,
                      opened="2026-10-26" if k == "claude" else CAPTURE)
            for k in SURFACE_ORDER])}),
        code=1, line=five, finding="was not opened this round"))
    add(dict(label="(e) every row opened before the round date", files=_mutate(
        honest, **{SOURCES: _registry(pages_h, [
            _reg_line(FIX[k][0], pages_h, k, opened="2026-10-26")
            for k in SURFACE_ORDER])}),
        code=1, line=zero, finding="was not opened this round"))
    add(dict(label="(e) entry verified-at is not the round date", files=_mutate(
        honest, **{ENTRY: _entry_text(pages_h).replace(
            f"verified-at: {CAPTURE}", "verified-at: 2026-10-26")}),
        code=1, line=zero, finding="was not opened this round"))

    add(dict(label="(f) grant cell is backticked", files=_mutate(
        honest, **{ENTRY: _entry_text(pages_h, rows={
            "claude": ("`pre-approves`",
                       ["allowed-tools", "Bash",
                        "without prompting you for approval"])})}),
        code=1, line=five, finding="grant cell is backticked"))
    add(dict(label="(f) grant label is another surface's", files=_mutate(
        honest, **{ENTRY: _entry_text(pages_h, rows={
            "claude": ("experimental", ["allowed-tools", "Bash",
                                        "without prompting you for "
                                        "approval"])})}),
        code=1, line=five, finding="is not claude's frozen label"))
    add(dict(label="(f) two grant labels are another surface's", files=_mutate(
        honest, **{ENTRY: _entry_text(pages_h, rows={
            "claude": ("experimental", ["allowed-tools", "Bash",
                                        "without prompting you for "
                                        "approval"]),
            "factory": ("experimental", ["allowed-tools", "Bash",
                                         "metadata"])})}),
        code=1, line=four, finding="is not factory's frozen label"))
    add(dict(label="(f) grant cell carries two labels", files=_mutate(
        honest, **{ENTRY: _entry_text(pages_h, rows={
            "claude": ("pre-approves, metadata-only",
                       ["allowed-tools", "Bash",
                        "without prompting you for approval"])})}),
        code=1, line=five, finding="frozen label(s)"))
    add(dict(label="(f) quote lacks the page token that grounds the grant",
             files=_honest(dict(pages_h, **{FIX["claude"][0]:
                 pages_h[FIX["claude"][0]] + (
                     "The allowed-tools field list is shown below in this "
                     "section.\n")}), entry=_entry_text(pages_h, quotes={
                         "claude": "The allowed-tools field list is shown "
                                   "below in this section"})),
             code=1, line=five, finding="does not carry the page token"))

    # ------------------------------------------------- plan shortcut controls
    # C1 token dump / C8 first-answer baseline: the entry names every token,
    # label and quote, but no snapshot is committed, so nothing can be pinned.
    add(dict(label="C1 token dump (tokens, labels and quotes, no snapshots) "
                    "is exit 2, never a documented surface",
             files={ENTRY: _entry_text(pages_h), SOURCES: _registry(pages_h),
                    PROVINCE: PROVINCE_OK, SKILLMD: SKILL_OK},
             code=2, line="environment error", finding="no pin manifest at"))
    # C5 label-only: the labels and tokens are right, the quote is absent.
    add(dict(label="C5 label-only world (no located quote) is not documented",
             files=_mutate(honest, **{ENTRY: _entry_text(
                 pages_h, quotes={"claude": "-"})}),
             code=1, line=five, finding="located quote is 1 words"))

    # ---- regression arm for a real row shape: S231's quote spans an indented
    # YAML list inside a fenced example, exactly as the vibe page writes it.
    vibe_page = "\n".join([
        "# Mistral Vibe",
        "",
        "## Skills",
        "",
        "```markdown",
        "---",
        "name: example",
        "user-invocable: true",
        "allowed-tools:",
        "  - read",
        "  - grep",
        "  - ask_user_question",
        "---",
        "```",
        "",
        "## Notes",
        "",
        "The example above is the only place this page shows the field.",
    ]) + "\n"
    vibe_quote = "user-invocable: true allowed-tools: read grep ask_user_question"
    add(dict(label="S231 row shape: quote spans an indented list inside a "
                    "fenced example", files=_honest(
        dict(pages_h, **{FIX["vibe"][0]: vibe_page}),
        entry=_entry_text(
            dict(pages_h, **{FIX["vibe"][0]: vibe_page}),
            quotes={"vibe": vibe_quote},
            rows={"vibe": ("unstated", ["allowed-tools", "allowed-tools:",
                                        "ask_user_question",
                                        "user-invocable"])})),
        code=0, line=six))
    add(dict(label="(d) a backtick-wrapped quote cell is formatting, not "
                    "content", files=_mutate(honest, **{ENTRY: _entry_text(
        pages_h, quotes={"claude": "`" + _quote(
            "claude", SURFACES["claude"]) + "`"})}),
        code=0, line=six))
    add(dict(label="(d) a backtick-wrapped quote that is absent still fails",
             files=_mutate(honest, **{ENTRY: _entry_text(pages_h, quotes={
                 "claude": "`The allowed-tools field of Claude Code says "
                           "nothing at all here`"})}),
             code=1, line=five, finding="located quote not found"))

    # ---- regression arm for the real S230 row: the page's only mention is a
    # markdown table row, its quote is pipe-bearing, and the page prints no
    # syntactic value form at all (a bare word is the value form it offers).
    pi_quote = "allowed-tools | Experimental pre-approved tool list"
    add(dict(label="S230 row shape: a pipe-bearing table-row quote with a bare "
                    "word as the value form", files=_honest(
        pages_h, entry=_entry_text(
            pages_h, quotes={"pi": pi_quote},
            rows={"pi": ("experimental", ["allowed-tools", "pre-approved",
                                          "Experimental"])})),
        code=0, line=six))

    # ---------------------------------------------------------- (g) (h) tree
    add(dict(label="(g) SKILL.md without a registry row reads MISSING",
             files=_mutate(honest, **{SKILLMD: "# fixture skill\n\n## Rules\n\n"
                                      "- `allowed-tools` per client: Open "
                                      "specification, Claude Code, Factory in `"
                                      + ENTRY + "`.\n"}),
             code=1, line="registry home MISSING"))
    add(dict(label="(g) rule line naming two surfaces reads MISSING",
             files=_mutate(honest, **{SKILLMD: SKILL_OK.replace(
                 "Open specification, Claude Code, Factory, Microsoft Agent "
                 "Framework, pi and Mistral Vibe", "Claude Code and pi")}),
             code=1, line="skill rule line MISSING"))
    add(dict(label="(g) a registry row with an empty field reads MISSING",
             files=_mutate(honest, **{SKILLMD: SKILL_OK.replace(
                 "| in-file |", "|  |")}),
             code=1, line="registry home MISSING"))
    add(dict(label="(h) PROVINCE.md without the bullet reads named 0 of 6",
             files=_mutate(honest, **{
                 PROVINCE: "# fixture province\n\n## Core\n\n- nothing\n"}),
             code=1, line="province surfaces named 0 of 6",
             finding="0 ## Core bullet(s) name the entry"))
    add(dict(label="(h) two Core bullets name the entry", files=_mutate(
        honest, **{PROVINCE: PROVINCE_OK.replace(
            "## Frontier", f"- also `{ENTRY}`\n\n## Frontier")}),
        code=1, line="province surfaces named 0 of 6",
        finding="2 ## Core bullet(s) name the entry"))

    # ---------------------------------------------------- (i) generator world
    add(dict(label="(i) the generator world is scored on this counter and its "
                    "score is printed", files=honest, code=0, line=six,
             finding=gen))
    add(dict(label="(i) the exit predicate is N == 6: a 5-of-6 measured world "
                    "exits 1 while the generator world still reads its score",
             files=_mutate(honest, **{ENTRY: _entry_text(pages_h, quotes={
                 "claude": "The allowed-tools field of Claude Code says "
                           "nothing at all here"})}),
             code=1, line=five, finding=gen))

    # ----------------------------- round-80 counter readings (red-before) ---
    # (1) the heading reading is per snapshot shape: an HTML page's first
    # heading is its <h1>, not the first '#'-prefixed line (a code comment).
    add(dict(label="(d) an HTML quote after the page's real <h1> is admissible "
                    "even when a '#' comment follows it",
             files=_honest(dict(pages_h, **{FIX["spec"][0]: (
                 "<html><body>\n<h1>Open specification</h1>\n<p>A subtitle "
                 "line.</p>\n<p>" + _quote("spec", SURFACES["spec"])
                 + "</p>\n<p>Example values: Bash(git:*) and Bash(git:*) list "
                 "forms.</p>\n<pre>x = 1  # allowed-tools is not stated here"
                 "</pre>\n</body></html>\n")})),
             code=0, line=six))
    add(dict(label="(d) the same page with the quote above its first heading "
                    "is still rejected", files=_honest(dict(pages_h, **{
                 FIX["spec"][0]: (
                     "<html><body>\n<p>"
                     + _quote("spec", SURFACES["spec"])
                     + "</p>\n<h1>Open specification</h1>\n<p>Example "
                     "values: Bash(git:*) and Bash(git:*) list forms.</p>\n"
                     "</body></html>\n")})),
             code=1, line=five, finding="first-heading block"))

    # (2) the fetch record's committed form: a date without a time and a
    # backticked digest (what corpus/SOURCES.md actually carries).
    def committed_anchor(k: str) -> str:
        raw = pages_h[FIX[k][0]].encode()
        return ("§ fixture; fetched %s, HTTP 200, %d B, sha256 `%s`"
                % (CAPTURE, len(raw), hashlib.sha256(raw).hexdigest()))

    add(dict(label="(c) the committed anchor form (date, backticked digest) is "
                    "accepted", files=_mutate(honest, **{
                 SOURCES: _registry(pages_h, [
                     _reg_line(FIX[k][0], pages_h, k, anchor=committed_anchor(k))
                     for k in SURFACE_ORDER])}),
             code=0, line=six))
    add(dict(label="(c) an anchor record that does not read HTTP 200 is not "
                    "accepted", files=_mutate(honest, **{
                 SOURCES: _registry(pages_h, [
                     _reg_line(FIX[k][0], pages_h, k,
                               anchor=committed_anchor(k).replace(
                                   "HTTP 200", "HTTP 404")
                               if k == "claude" else committed_anchor(k))
                     for k in SURFACE_ORDER])}),
             code=1, line=five, finding="anchor cell carries no"))

    # (3) the pin source: the aggregate MANIFEST.sha256 when committed, else
    # the per-page <id>.manifest files the r79 wave committed.
    per_mans = {f"{SNAPDIR}/{FIX[k][0]}.manifest":
                "%s  %s\n" % (hashlib.sha256(
                    pages_h[FIX[k][0]].encode()).hexdigest(), FIX[k][2])
                for k in SURFACE_ORDER}
    add(dict(label="(c) per-page <id>.manifest pins alone evaluate (no "
                    "aggregate MANIFEST.sha256)", files=_mutate(
                        honest, MANIFEST=None, **per_mans), code=0, line=six))
    add(dict(label="(c) aggregate and per-page pins that disagree are exit 2",
             files=_mutate(honest, **per_mans, **{
                 MANIFEST: _manifest(pages_h).replace(
                     hashlib.sha256(
                         pages_h[FIX["claude"][0]].encode()).hexdigest(),
                     "0" * 64)}),
             code=2, line="environment error", finding="disagrees"))

    # ------------------------------------------------------- cannot-evaluate
    add(dict(label="unknown revision is exit 2", files=honest, code=2,
             rev="0" * 40, line="environment error", finding="not a commit"))
    add(dict(label="registry absent at the revision is exit 2", files=_mutate(
        honest, **{SOURCES: None}), code=2, line="environment error",
        finding=f"{SOURCES} absent"))
    add(dict(label="counter drift is exit 2 (SELF_SHA does not match)",
             files=honest, code=2, line="environment error",
             finding="counter drifted", drift=True))
    return specs


def _run_spec(spec: dict) -> tuple[bool, int, str]:
    """Run one world through ``main()`` in its own isolated git repo."""
    global BASE_REV, _INTERNAL_SELFTEST, SURFACES
    saved_rev, saved_surfaces = BASE_REV, SURFACES
    if spec.get("surfaces"):
        SURFACES = spec["surfaces"]      # before the files are built
    files = spec["files"]() if callable(spec["files"]) else spec["files"]
    d, base = _world(files, spec.get("base_files"))
    BASE_REV = base
    _INTERNAL_SELFTEST = True
    if spec.get("drift"):
        text = Path(__file__).read_text()
        drifted = _blanked_sha(text + "\n# drift\n") != SELF_SHA
        out = ("environment error: counter drifted — the running file is not "
               "the frozen counter" if drifted else "no drift check")
        checks = [drifted, spec["line"] in out, spec["finding"] in out]
        shutil.rmtree(d, ignore_errors=True)
        BASE_REV, SURFACES = saved_rev, saved_surfaces
        _INTERNAL_SELFTEST = False
        msg = f"{spec['label']}: exit 2"
        if not all(checks):
            msg += f" (want 2); output={out!r}"
        return all(checks), len(checks), msg
    cwd = os.getcwd()
    buf = io.StringIO()
    try:
        if spec.get("relative"):
            os.chdir(d)
        with contextlib.redirect_stdout(buf), \
                contextlib.redirect_stderr(buf):
            code = main(["--repo", "." if spec.get("relative") else d,
                         "--rev", spec.get("rev", "HEAD")])
    finally:
        os.chdir(cwd)
        shutil.rmtree(d, ignore_errors=True)
        BASE_REV, SURFACES = saved_rev, saved_surfaces
        _INTERNAL_SELFTEST = False
    out = buf.getvalue()
    checks = [code == spec["code"]]
    if spec.get("line") is not None:
        checks.append(spec["line"] in out)
    if spec.get("finding") is not None:
        checks.append(spec["finding"] in out)
    ok = all(checks)
    msg = f"{spec['label']}: exit {code}"
    if not ok:
        msg += f" (want {spec['code']}); output={out!r}"
    return ok, len(checks), msg


def selftest() -> int:
    failures = 0
    assertions = 0
    for spec in _world_specs():
        ok, n, msg = _run_spec(spec)
        assertions += n
        if ok:
            print(f"PASS {msg}")
        else:
            failures += 1
            print(f"FAIL {msg}")
    print(f"self-test: {failures} failure(s) over {assertions} assertions "
          f"in {len(_world_specs())} world(s)")
    return 0 if failures == 0 else 1


def main(argv: list[str] | None = None) -> int:
    global _WORK
    ap = argparse.ArgumentParser(
        description="C2 allowed-tools surface counter for kotoba round 79")
    ap.add_argument("--rev", default=None, help="measured revision")
    ap.add_argument("--repo", default=str(_default_repo()))
    ap.add_argument("--work", default=None,
                    help="parent directory for temp dirs (default: $TMPDIR)")
    ap.add_argument("--self-test", action="store_true")
    ap.add_argument("--print-self-sha", action="store_true",
                    help="print the blanked sha of this file and exit")
    args = ap.parse_args(argv)
    if args.print_self_sha:
        print(_blanked_sha(Path(__file__).read_text()))
        return 0
    _WORK = args.work
    if _WORK:
        Path(_WORK).mkdir(parents=True, exist_ok=True)
    if args.self_test:
        return selftest()
    if not args.rev:
        print("environment error: --rev <revision> is required",
              file=sys.stderr)
        return 2
    repo = Repo(Path(args.repo).resolve(), args.rev)
    proc = _git(repo.path, ["rev-parse", "--verify", "-q",
                            f"{args.rev}^{{commit}}"])
    if proc.returncode != 0:
        print(f"environment error: --rev {args.rev} is not a commit",
              file=sys.stderr)
        return 2
    src = Path(__file__).read_text()
    if not _INTERNAL_SELFTEST and _blanked_sha(src) != SELF_SHA:
        print("environment error: counter drifted — the running file is not "
              "the frozen counter", file=sys.stderr)
        return 2
    try:
        n, findings, _documented, opened = check(repo)
        held = held_at_base(repo)
        m, why = generator_world(repo)
        bullets, named = province_state(repo.show(PROVINCE))
        rule = skill_rule_ok(repo.show(SKILLMD))
        home = registry_home_ok(repo.show(SKILLMD))
    except EnvError as exc:
        print(f"environment error: {exc}", file=sys.stderr)
        return 2
    print(f"allowed-tools surfaces documented {n} of {TOTAL}")
    print(f"generator world: {m} of {TOTAL}")
    print("semantic rider: exploratory — reviewers of record: round-80 "
          "non-author closure spot-check")
    print(f"measured-rev: {args.rev}")
    print(f"opened this round {opened} of {TOTAL}")
    print(f"held at base: {held}")
    print(f"province surfaces named {named} of {TOTAL}")
    print("skill rule line ok" if rule else "skill rule line MISSING")
    print("registry home ok" if home else "registry home MISSING")
    for finding in findings:
        print(f"  {finding}")
    if m >= TARGET:
        print(f"  the generator world reaches the form target ({m} of "
              f"{TOTAL}): the headline asserts FORM-LEVEL documentation only "
              f"and the grant-semantics rider is exploratory ({why})")
    if bullets != 1:
        print(f"  {bullets} ## Core bullet(s) name the entry (want exactly 1)")
    ok = n == TARGET and rule and home and bullets == 1
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
