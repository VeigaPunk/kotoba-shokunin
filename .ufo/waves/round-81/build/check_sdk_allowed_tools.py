#!/usr/bin/env python3
"""check_sdk_allowed_tools.py — frozen C2 counter for kotoba round 81 (depth).

FROZEN PREDICATE (the same sentence in plans/round-81.md § C2, in this
docstring, in the freeze receipt and in the SCORECARD row):

    python3 -B verifiers/check_sdk_allowed_tools.py --rev <rev>  ->  prints
    "sdk allowed-tools surface documented N of 1" and exits 0 iff N == 1 and
    the tree conjuncts hold; at the r81 base
    b284223105f4d106f7e8f56ed4fd296c643cda0e it prints
    "sdk allowed-tools surface documented 0 of 1" and exits 1.

The round-80 entry documented the `allowed-tools` frontmatter forms per client
(six surfaces, FORM level).  Round 81 deepens that held matrix by one surface:
the Claude Agent SDK page documents a SECOND GRANT CHANNEL — query-config
`allowedTools` (`allowed_tools` in Python) in addition to frontmatter, with a
managed-settings override.  The population is one surface, so the counter
prints "N of 1" and there is no partial credit.

The surface is DOCUMENTED at ``--rev`` iff all of (a)-(g) hold over committed
bytes only (no network at measurement, and no instrument of the measured tree
is executed):

  (a) ``corpus/knowledge/allowed-tools-sdk-round81.md`` exists and carries one
      or more ``source:`` lines naming S249, with the canonical URL
      ``https://code.claude.com/docs/en/agent-sdk/skills.md`` and the pinned
      snapshot named; plus ``verified-at: 2026-10-27`` and a non-empty
      ``recheck:`` line;
  (b) ``corpus/SOURCES.md`` row S249 is exactly one 11-cell row, status
      ``mined``, tier ``A`` or ``B``, ``used-by`` listing the entry path, and a
      ``source`` cell carrying the canonical URL (host+path identity, trailing
      ``/`` and query ignored);
  (c) the S249 anchor cell names the snapshot
      ``.ufo/waves/round-81/snapshots/S249.md`` and carries a fetch record
      ``fetched <date|date-timeZ>, HTTP 200, <bytes> B, sha256 <hex>`` whose
      digest is the pin in this counter (``SNAPSHOT_PIN``) — and the committed
      snapshot's own sha256 is that same pin; the sibling
      ``S249.fetch.json``, when committed, must agree with both;
  (d) the entry's located quote (5..25 words, naming ``allowed-tools`` or
      ``allowedTools``) occurs in the committed snapshot's text view after the
      first heading, not on a heading line and not in the first-heading block
      (Q70);
  (e) row S248's ``used-by`` cell names the new entry (old -> new), and
      ``corpus/lessons/round-81.md`` logs that move on a line naming S248, the
      entry path and an arrow;
  (f) ``SKILL.md`` names the SDK channel in the `allowed-tools` author-facing
      rule area (the ``allowed-tools`` + ``pre-approval`` paragraph block) and
      carries a conformant gate row (8 non-empty cells, kind ``gate``) for this
      counter;
  (g) ``corpus/README.md`` carries a coverage-map row naming the entry, and
      ``PROVINCE.md`` ``## Core`` has exactly one bullet naming the entry, that
      bullet naming the SDK channel.

READINGS that are deliberately stricter or looser than the naive one, named
here so a reviewer can attack them rather than discover them:

  * the pin lives in this file (``SNAPSHOT_PIN``) because (c) names "the pin in
    both the counter and the row's fetch record".  It is refilled at freeze by
    the L1 from the reviewed fetch of the measured wave — never to make a
    measured world green.  ``--print-pins`` prints the pin and the path for the
    freeze receipt.  The pin shipped for this draft is grounded twice over: the
    committed S248 anchor of the same URL carries it, and the reviewed r80
    fetch of the same page (``.ufo/waves/round-80/build/Kb80S05-agent-sdk-
    skills.md``, 28395 B) hashes to it.
  * (c) is exit 2 when the committed snapshot is absent (a quote asserted
    without committed snapshot bytes cannot be evaluated), when it does not
    hash to the pin (``snapshot_tampered``), and when the sibling fetch record
    states a second digest or a different byte count.  It is exit 1 when the
    ROW's anchor record disagrees: that is a content finding about the row.
  * the located quote is read from the double-quoted span(s) on lines that cite
    S249 (the lane's house ``located quote "..."`` form, on the ``source:`` line
    or in a table row).  Several spans are allowed; the surface is documented
    when AT LEAST ONE of them satisfies (d) — a second quoted sentence on the
    same line is not a defect.  The counter prints the span it located and the
    snapshot line it landed on.
  * the 5-word floor is the round-80 precedent (``MIN_QUOTE_WORDS``); the plan
    freezes only "<= 25 words".  A one-word span ("allowed-tools") is a token,
    not a located quote, so the floor is kept and printed rather than left
    implicit.  Every other bound is the plan's own.
  * the snapshot text view is the round-79/r80 rule, unchanged: for Markdown
    every backtick byte is deleted and an unordered-list marker removed at a
    line start, then every whitespace run is collapsed; a heading is a view
    line that starts with ``#`` outside a fenced code block.  The frozen
    snapshot is Markdown; a non-Markdown snapshot reads as plain text (no
    headings, no backtick deletion), which is declared rather than special-
    cased.  The quote is matched as written and, only when it carries a
    backtick, once more with every backtick deleted (the Markdown view deletes
    them, so a backticked cell is formatting, not content).
  * the `allowed-tools` author-facing rule AREA of SKILL.md is the block that
    starts at the paragraph naming ``allowed-tools`` and ``pre-approval`` and
    runs to the next heading line; a sentence appended inside that paragraph,
    or as an adjacent paragraph before the next heading, is inside the area.  A
    table row is never the anchor (the gate table is instrumentation metadata,
    not the rule).  A channel line placed in another section is outside the
    area and fails (f); relocating the rule paragraph together with its channel
    sentence keeps the area content-anchored, which is the reading.
  * the gate row is read with the round-80 rule the frozen
    ``check_gate_registry.py`` also applies: 8 cells, non-empty, kind ``gate``,
    and this counter's ``--self-test`` exists as an exact ``add_argument``
    string in this file.
  * the generator world (Q74): this counter builds, from the measured
    revision's own committed bytes, the COMPLETE proposed evidence shape —
    entry, row, anchors, SKILL rule and gate row, README row, PROVINCE bullet,
    lesson line — with no judgement beyond a mechanical quote window, and
    scores it with this same ``check()``.  Its score is PRINTED beside the
    headline and NEVER gates the exit predicate: a counter a mechanical
    generator reaches measures FORM, and saying so is the point of printing it.
  * exit codes: 0 iff N == 1 and (a)-(g) all hold; 1 for a content verdict; 2
    could not evaluate (unknown revision, unreadable SOURCES, absent or
    tampered or doubly-pinned snapshot, counter drift).

``--self-test`` drives ``main()`` on one satisfying fixture world (exit 0 and
the exact printed headline) beside one broken world per conjunct and the plan's
C0-C4 controls, in isolated local git repos under fresh ``mktemp -d``
directories (honouring ``TMPDIR`` and ``--work``): no lane, no fleet repo and
no shared index is ever touched.  A measurement never reads the network;
``--fetch`` is the documented recheck path (the plan's C3 parenthetical) and is
never the claim measurement, and it is not exercised by ``--self-test``.
``--print-self-sha`` prints the blanked sha of this file
(the L1 refills ``SELF_SHA`` after any edit and before freeze).

Usage:
  python3 -B verifiers/check_sdk_allowed_tools.py --rev <rev> [--repo <lane>] [--work <dir>]
  python3 -B verifiers/check_sdk_allowed_tools.py --self-test [--work <dir>]
  python3 -B verifiers/check_sdk_allowed_tools.py --print-self-sha
  python3 -B verifiers/check_sdk_allowed_tools.py --print-pins
  python3 -B verifiers/check_sdk_allowed_tools.py --fetch [--repo <lane> --rev <rev>]
"""

from __future__ import annotations

import argparse
import contextlib
import hashlib
import io
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import time
import urllib.parse
import urllib.request
from pathlib import Path

TOTAL = 1
TARGET = 1

SOURCES = "corpus/SOURCES.md"
ENTRY = "corpus/knowledge/allowed-tools-sdk-round81.md"
SNAPSHOT_ID = "S249"
SNAPSHOT_PATH = ".ufo/waves/round-81/snapshots/S249.md"
FETCH_JSON = ".ufo/waves/round-81/snapshots/S249.fetch.json"
CANONICAL_URL = "https://code.claude.com/docs/en/agent-sdk/skills.md"
CAPTURE = "2026-10-27"
PREV_ROW = "S248"
PROVINCE = "PROVINCE.md"
SKILLMD = "SKILL.md"
README = "corpus/README.md"
LESSON = "corpus/lessons/round-81.md"
COUNTER_PATH = "verifiers/check_sdk_allowed_tools.py"

ENTRY_NAMES = (ENTRY, ENTRY.rsplit("/", 1)[-1])

# The in-file pin of the reviewed snapshot (plan § C2 (c)).  See the docstring
# READINGS: refilled at freeze from the reviewed fetch, never to green a world.
SNAPSHOT_PIN = "ac62c2dff61ef07bb778e5d115060e22f3f061fa3eca402be9b886946f01e5a2"

# Frozen for round 81: the lane base the do-nothing figure is measured at.  The
# self-test rebinds this module global to a fixture repo's own first commit.
BASE_REV = "b284223105f4d106f7e8f56ed4fd296c643cda0e"

MIN_QUOTE_WORDS = 5
MAX_QUOTE_WORDS = 25
REGISTRY_CELLS = 11
SKILL_CELLS = 8
CONJUNCTS = ("a", "b", "c", "d", "e", "f", "g")

SID_RE = re.compile(r"\bS\d{3,}\b")
CITED_TAIL_RE = re.compile(r"-[A-Za-z]")
BACKTICK_RE = re.compile(r"`([^`]+)`")
QUOTE_RE = re.compile(r'["\u201c]([^"\u201d]+)["\u201d]')
REGISTRY_RE = re.compile(r"^ {0,3}\|\s*S\d{3,}\s*\|")
URL_RE = re.compile(r"https?://[^\s)>\]]+")
SEPARATOR_RE = re.compile(r":?-{3,}:?")
LIST_MARKER_RE = re.compile(r"(?m)^[ \t]{0,3}[*+\-][ \t]+")
TRIM_CHARS = ".,;:!?)]}'\""
ARROWS = ("\u2192", "->", "=>")
FETCHED_RE = re.compile(
    r"fetched (\d{4}-\d\d-\d\d(?:T\d\d:\d\d:\d\dZ)?), HTTP 200, (\d+) B, "
    r"sha256 `?([0-9a-f]{64})`?")
SELF_LINE_RE = re.compile(r'^SELF_SHA = "[0-9a-f]*"', re.M)
SELF_SHA = "38ac8513c8f693c58b9f4b4a582471bc41ee3c6e7072f1b5cec06f07b17c53b5"   # blanked-sha of this file (the L1 refills it at freeze)
_INTERNAL_SELFTEST = False   # set only by --self-test: the drift guard is a
                             # measurement guard and the self-test mutates
                             # nothing in this file, so it is skipped there.
_WORK: str | None = None     # --work: the parent of every temp dir this run makes


class EnvError(Exception):
    """Could not evaluate: exit 2, never a pass and never a fail."""


# --------------------------------------------------------------- text shaping

def _blanked_sha(text: str) -> str:
    return hashlib.sha256(
        SELF_LINE_RE.sub('SELF_SHA = ""', text).encode()).hexdigest()


def rendered(text: str) -> str:
    """Rendered content only: HTML comments and fenced code removed.

    Applied to the entry and the tree files (a rule line hidden in a comment or
    a fence is not the tree's rule line).  NEVER applied to a snapshot."""
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


def field_token(text: str) -> bool:
    """The field name in either documented spelling."""
    return (word_bounded("allowed-tools", text)
            or word_bounded("allowedTools", text))


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
    """The snapshot text view PLUS the indices of its heading lines.

    Markdown (``.md``/``.markdown``): every backtick byte deleted, an
    unordered-list marker removed at a line start, whitespace collapsed per
    line, empty lines dropped; a heading is a view line that starts with ``#``
    and does not sit inside a fenced block.  Anything else reads as plain text
    with no headings (the frozen snapshot is Markdown)."""
    low = name.lower()
    lines: list[str] = []
    heads: set[int] = set()
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
    """The plan's snapshot text view (Q42/Q53/Q56 rules, unchanged)."""
    return view_with_headings(name, raw)[0]


def _split_cells(s: str) -> list[str]:
    """Split one table row on unescaped ``|`` and drop the escape backslash."""
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


def page_key(url: str) -> tuple[str, str]:
    """Host + path of a page, ignoring a trailing ``/`` and the query/fragment."""
    parts = urllib.parse.urlsplit(url)
    return ((parts.hostname or "").lower(),
            urllib.parse.unquote(parts.path or "").rstrip("/").lower())


def same_page(a: str, b: str) -> bool:
    """Two URL forms of one page: identical host+path, or a Markdown route.

    The canonical URL already ends in ``.md``; the bare route is accepted for
    the ENTRY's source line only (the r80 factory reading), while the registry
    ROW must carry the canonical page itself."""
    ka, kb = page_key(a), page_key(b)
    if ka == kb:
        return True
    if ka[0] != kb[0]:
        return False
    return ka[1] + ".md" == kb[1] or kb[1] + ".md" == ka[1]


def cited_sids(text: str) -> list[str]:
    """``S###`` ids that cite a registry row, in order, deduplicated.

    An id glued to a slug (``S249-spec.md``) is a snapshot file name, not a
    citation of that row."""
    out: list[str] = []
    for m in SID_RE.finditer(text):
        if CITED_TAIL_RE.match(text, m.end()):
            continue
        if m.group(0) not in out:
            out.append(m.group(0))
    return out


def snapshot_named(text: str) -> bool:
    """A cell names the frozen snapshot (full path or its basename)."""
    return SNAPSHOT_PATH in text or Path(SNAPSHOT_PATH).name in text


# ------------------------------------------------------------------ git side

def _default_repo() -> Path:
    here = Path(__file__).resolve()
    for cand in here.parents:
        if (cand / SOURCES).is_file():
            return cand
    return here.parent


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

    def raw(self, path: str) -> bytes | None:
        proc = _git(self.path, ["show", f"{self.rev}:{path}"])
        if proc.returncode == 0:
            return proc.stdout
        err = proc.stderr.decode("utf-8", "replace")
        if "does not exist" in err or "exists on disk, but not in" in err \
                or "Path '" in err or "invalid object" in err:
            return None
        raise EnvError(f"git show {self.rev}:{path} failed: {err.strip()}")

    def show(self, path: str) -> str | None:
        raw = self.raw(path)
        return None if raw is None else raw.decode("utf-8", "replace")


# ------------------------------------------------------------------ entry (a)

def source_lines(entry_r: str) -> list[str]:
    return [l for l in entry_r.splitlines() if l.startswith("source:")]


def field_value(entry_r: str, name: str) -> str | None:
    """The first ``<name>:`` line's value (trio order is not enforced: the
    plan names the fields, not their sequence)."""
    for line in entry_r.splitlines():
        if line.startswith(name + ":"):
            value = line[len(name) + 1:].strip()
            return value or None
    return None


def entry_problems(entry_r: str) -> list[str]:
    """(a): the provenance trio and the source line's URL + anchor."""
    notes: list[str] = []
    src = source_lines(entry_r)
    if not src:
        notes.append("entry carries no `source:` line")
    mine = [l for l in src if SNAPSHOT_ID in cited_sids(l)]
    if not mine:
        notes.append(f"no `source:` line names {SNAPSHOT_ID}")
    else:
        if not any(any(same_page(u, CANONICAL_URL) for u in urls_of(l))
                   for l in mine):
            notes.append(f"no {SNAPSHOT_ID} `source:` line carries the canonical "
                         f"URL {CANONICAL_URL}")
        if not any(snapshot_named(l) for l in mine):
            notes.append(f"no {SNAPSHOT_ID} `source:` line names the pinned "
                         f"snapshot {SNAPSHOT_PATH} (or its basename)")
    verified = field_value(entry_r, "verified-at")
    if verified != CAPTURE:
        notes.append(f"entry verified-at {verified!r} is not the round date "
                     f"{CAPTURE}")
    if not field_value(entry_r, "recheck"):
        notes.append("entry carries no non-empty `recheck:` line")
    return notes


def entry_quotes(entry_r: str) -> list[str]:
    """Every quoted span on a line that cites S249, in document order."""
    spans: list[str] = []
    for line in entry_r.splitlines():
        if SNAPSHOT_ID not in cited_sids(line):
            continue
        for q in QUOTE_RE.findall(line):
            s = ws(q)
            if s and s not in spans:
                spans.append(s)
    return spans


# ------------------------------------------------------------------- rows (b)

def row_of(rows: dict[str, list[list[str]]],
           sid: str) -> tuple[list[str] | None, list[str]]:
    got = rows.get(sid, [])
    if len(got) != 1:
        return None, [f"{sid}: {len(got)} registry rows in {SOURCES} "
                      f"(want exactly 1)"]
    row = got[0]
    if len(row) != REGISTRY_CELLS:
        return None, [f"{sid}: {len(row)} cells (want exactly "
                      f"{REGISTRY_CELLS})"]
    return row, []


def row_s249_problems(row: list[str]) -> list[str]:
    """(b): the S249 row's status, tier, used-by and canonical URL."""
    notes: list[str] = []
    if row[7].strip() != "mined":
        notes.append(f"S249: status {row[7].strip()!r} (want 'mined')")
    if row[3].strip() not in ("A", "B"):
        notes.append(f"S249: tier {row[3].strip()!r} (want A or B)")
    listed = [c.strip() for c in row[10].split(",")]
    if ENTRY not in listed:
        notes.append(f"S249: used-by {row[10].strip()!r} does not list {ENTRY}")
    urls = urls_of(row[1])
    if not urls:
        notes.append("S249: source cell holds no URL")
    elif not any(page_key(u) == page_key(CANONICAL_URL) for u in urls):
        notes.append(f"S249: no URL is the canonical page {CANONICAL_URL}: "
                     f"{urls}")
    return notes


def anchor_problems(row: list[str]) -> list[str]:
    """(c) row half: the anchor names the snapshot and pins the counter pin."""
    notes: list[str] = []
    cell = row[5]
    if not snapshot_named(cell):
        notes.append(f"S249: anchor cell does not name the snapshot "
                     f"{SNAPSHOT_PATH}")
    m = FETCHED_RE.search(cell)
    if not m:
        notes.append("S249: anchor cell carries no 'fetched <date>, HTTP 200, "
                     "<bytes> B, sha256 <hex>' record")
    elif m.group(3) != SNAPSHOT_PIN:
        notes.append(f"S249: anchor sha256 {m.group(3)[:12]}... is not the "
                     f"counter pin {SNAPSHOT_PIN[:12]}...")
    return notes


# -------------------------------------------------------------- snapshot (c)

def _fetch_record_pin(repo: Repo, nbytes: int) -> None:
    """The sibling fetch record, when committed, must agree with the pin."""
    text = repo.show(FETCH_JSON)
    if text is None:
        return
    try:
        doc = json.loads(text)
    except json.JSONDecodeError as exc:
        raise EnvError(f"{FETCH_JSON} is not JSON: {exc}") from exc
    digests: set[str] = set()
    counts: set[int] = set()

    def walk(v) -> None:
        if isinstance(v, dict):
            for k, x in v.items():
                low = str(k).lower()
                if isinstance(x, str) and re.fullmatch(r"[0-9a-f]{64}", x) \
                        and ("sha" in low or "digest" in low):
                    digests.add(x)
                elif isinstance(x, int) and ("byte" in low or "size" in low
                                            or "length" in low):
                    counts.add(x)
                walk(x)
        elif isinstance(v, list):
            for x in v:
                walk(x)

    walk(doc)
    for d in sorted(digests):
        if d != SNAPSHOT_PIN:
            raise EnvError(f"{FETCH_JSON} records sha256 {d} beside the counter "
                           f"pin {SNAPSHOT_PIN} — a pin that pins two digests "
                           f"pins nothing")
    for c in sorted(counts):
        if c != nbytes:
            raise EnvError(f"{FETCH_JSON} records {c} B beside a {nbytes} B "
                           f"committed snapshot")


def snapshot_bytes(repo: Repo) -> bytes:
    """(c) bytes half: the committed snapshot must hash to the counter pin."""
    raw = repo.raw(SNAPSHOT_PATH)
    if raw is None:
        raise EnvError(f"{SNAPSHOT_PATH} is not committed at {repo.rev}: a "
                       f"quote asserted without committed snapshot bytes cannot "
                       f"be evaluated (this counter never reads the network — "
                       f"--fetch is a recheck path, never the measurement)")
    got = hashlib.sha256(raw).hexdigest()
    if got != SNAPSHOT_PIN:
        raise EnvError(f"snapshot_tampered: {SNAPSHOT_PATH} hashes to {got}, "
                       f"the counter pin is {SNAPSHOT_PIN}; refill SNAPSHOT_PIN "
                       f"at freeze only from the reviewed fetch")
    _fetch_record_pin(repo, len(raw))
    return raw


# ---------------------------------------------------------------- quote (d)

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
    """Q70: not a heading, not the first-heading block."""
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


def quote_state(entry_r: str, lines: list[str],
                heads: set[int]) -> tuple[bool, str]:
    """(d): (documented, note) — the note names the located span or the fault."""
    quotes = entry_quotes(entry_r)
    if not quotes:
        return False, ("the entry carries no quoted located-quote span on a line "
                       "naming S249")
    cands = [q for q in quotes if field_token(q)]
    if not cands:
        return False, ("no quoted span on an S249 line names `allowed-tools` or "
                       "`allowedTools`: " + "; ".join(q[:50] for q in quotes))
    notes: list[str] = []
    for q in cands:
        words = len(q.split())
        if not MIN_QUOTE_WORDS <= words <= MAX_QUOTE_WORDS:
            notes.append(f"located quote is {words} words (want "
                         f"{MIN_QUOTE_WORDS}-{MAX_QUOTE_WORDS}): {q[:60]!r}")
            continue
        forms = [q]
        if "`" in q:
            forms.append(ws(q.replace("`", "")))
        last = "quote not found in the text view"
        for form in forms:
            ok, why = quote_location(lines, form, heads)
            if ok:
                idx, _ = _line_of(lines, form)
                return True, (f"quote located on snapshot line {idx}: "
                              f"{form!r}")
            last = why or last
        notes.append(f"located quote not located after the text view: "
                     f"{q[:60]!r} ({last})")
    return False, "; ".join(notes)


# ---------------------------------------------------------------- tree (e)-(g)

def sdk_channel(text: str) -> bool:
    """A line names the SDK's second grant channel."""
    return word_bounded_ci("SDK", text) and (
        word_bounded("allowedTools", text)
        or word_bounded("allowed_tools", text))


def rule_area(text: str | None) -> list[str]:
    """The `allowed-tools` author-facing rule area of SKILL.md.

    The block that starts at the paragraph naming ``allowed-tools`` and
    ``pre-approval`` and runs to the next heading line."""
    if not text:
        return []
    lines = rendered(text).splitlines()
    start = None
    for i, line in enumerate(lines):
        if line.strip().startswith("|"):
            continue          # the gate table is instrumentation, not the rule
        if word_bounded("allowed-tools", line) and "pre-approval" in line.lower():
            start = i
            break
    if start is None:
        return []
    block: list[str] = []
    for line in lines[start:]:
        if line.startswith("#"):
            break
        block.append(line)
    return block


def registry_home_ok(text: str | None) -> bool:
    """(f) second half: a gate row with eight non-empty fields for this counter."""
    if not text:
        return False
    for line in rendered(text).splitlines():
        if line.startswith("| `" + COUNTER_PATH + "`"):
            cells = _cells(line)
            return len(cells) == SKILL_CELLS and all(c.strip() for c in cells) \
                and cells[1].strip() == "gate"
    return False


def readme_row_ok(text: str | None) -> bool:
    """(g) first half: a coverage-map table row naming the entry."""
    if not text:
        return False
    for line in rendered(text).splitlines():
        s = line.strip()
        if s.startswith("|") and any(n in s for n in ENTRY_NAMES):
            return True
    return False


def province_bullets(text: str | None) -> list[str]:
    """(g) second half: the ``## Core`` bullets, continuation lines joined."""
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


def province_state(text: str | None) -> tuple[bool, int, str]:
    """(documented, bullets naming the entry, note)."""
    bullets = province_bullets(text)
    naming = [b for b in bullets if ENTRY in b]
    if len(naming) != 1:
        return (False, len(naming),
                f"{len(naming)} ## Core bullet(s) name {ENTRY} (want exactly 1)")
    if not sdk_channel(naming[0]):
        return (False, 1,
                "the ## Core bullet naming the entry does not name the SDK "
                "channel (`SDK` plus `allowedTools`/`allowed_tools`)")
    return True, 1, ""


def lesson_state(repo: Repo) -> tuple[bool, str]:
    """(e): the old->new move is logged in the round lesson."""
    text = repo.show(LESSON)
    if text is None:
        return False, (f"{LESSON} absent at {repo.rev}: the {PREV_ROW} used-by "
                       f"old->new move is not logged")
    for line in rendered(text).splitlines():
        if PREV_ROW in cited_sids(line) \
                and any(n in line for n in ENTRY_NAMES) \
                and any(a in line for a in ARROWS):
            return True, ""
    return False, (f"{LESSON} carries no line naming {PREV_ROW}, the entry path "
                   f"and an arrow (the old->new move is not logged)")


def tree_facts(repo: Repo, rows: dict[str, list[list[str]]]) -> dict:
    """(e)-(g) as data, computed once for both the verdict and the printout."""
    skill_text = repo.show(SKILLMD)
    area = rule_area(skill_text)
    prov_ok, prov_count, prov_note = province_state(repo.show(PROVINCE))
    s248 = rows.get(PREV_ROW, [])
    s248_row = s248[0] if len(s248) == 1 else None
    lesson_ok, lesson_note = lesson_state(repo)
    return {
        "skill_area": bool(area),
        "skill_channel": bool(area) and any(sdk_channel(l) for l in area),
        "home": registry_home_ok(skill_text),
        "readme": readme_row_ok(repo.show(README)),
        "province_ok": prov_ok,
        "province_count": prov_count,
        "province_note": prov_note,
        "s248_rows": len(s248),
        "s248_status": s248_row[7].strip() if s248_row and len(s248_row) > 7
                      else "?",
        "s248_used_by": s248_row[10].strip() if s248_row and len(s248_row) > 10
                        else "?",
        "lesson_ok": lesson_ok,
        "lesson_note": lesson_note,
    }


# -------------------------------------------------------------------- verdict

def check(repo: Repo) -> tuple[int, list[str], dict, dict, str]:
    """(N, findings, conjunct detail, tree facts, quote note)."""
    sources = repo.show(SOURCES)
    if sources is None:
        raise EnvError(f"{SOURCES} absent at {repo.rev}")
    rows = registry_rows(rendered(sources))
    entry_text = repo.show(ENTRY)
    if entry_text is None:
        facts = tree_facts(repo, rows)
        return (0,
                [f"entry {ENTRY} absent at {repo.rev} (the frozen path is the "
                 f"entry's only home)"],
                {k: False for k in CONJUNCTS}, facts,
                "quote MISSING: the entry is absent")
    entry_r = rendered(entry_text)
    detail: dict = {}
    findings: list[str] = []
    facts = tree_facts(repo, rows)

    a_notes = entry_problems(entry_r)
    detail["a"] = not a_notes
    findings += [f"(a) {n}" for n in a_notes]

    row249, b_notes = row_of(rows, SNAPSHOT_ID)
    if row249 is not None:
        b_notes = b_notes + row_s249_problems(row249)
    detail["b"] = not b_notes
    findings += [f"(b) {n}" for n in b_notes]

    raw = snapshot_bytes(repo)        # may raise EnvError: exit 2
    c_notes = (["S249: the row is absent, so its anchor carries no fetch "
                "record"] if row249 is None else anchor_problems(row249))
    detail["c"] = not c_notes
    findings += [f"(c) {n}" for n in c_notes]

    lines, heads = view_with_headings(SNAPSHOT_PATH,
                                      raw.decode("utf-8", "replace"))
    d_ok, quote_note = quote_state(entry_r, lines, heads)
    detail["d"] = d_ok
    if not d_ok:
        findings.append(f"(d) {quote_note}")

    e_notes: list[str] = []
    if facts["s248_rows"] != 1:
        e_notes.append(f"{PREV_ROW}: {facts['s248_rows']} registry rows in "
                       f"{SOURCES} (want exactly 1)")
    else:
        listed = [c.strip() for c in facts["s248_used_by"].split(",")]
        if ENTRY not in listed:
            e_notes.append(f"{PREV_ROW}: used-by {facts['s248_used_by']!r} does "
                           f"not list {ENTRY} (the old->new move is the "
                           f"conjunct)")
    if not facts["lesson_ok"]:
        e_notes.append(facts["lesson_note"])
    detail["e"] = not e_notes
    findings += [f"(e) {n}" for n in e_notes]

    f_notes: list[str] = []
    if not facts["skill_area"]:
        f_notes.append(f"{SKILLMD} carries no `allowed-tools` author-facing rule "
                       f"paragraph (one naming `allowed-tools` and "
                       f"`pre-approval`) to hold the SDK channel line")
    elif not facts["skill_channel"]:
        f_notes.append("no line in the `allowed-tools` rule area names the SDK "
                       "channel (`SDK` plus `allowedTools`/`allowed_tools`)")
    if not facts["home"]:
        f_notes.append(f"{SKILLMD} carries no conformant gate row for "
                       f"{COUNTER_PATH} (8 non-empty cells, kind `gate`)")
    detail["f"] = not f_notes
    findings += [f"(f) {n}" for n in f_notes]

    g_notes: list[str] = []
    if not facts["readme"]:
        g_notes.append(f"{README} coverage map carries no row naming {ENTRY}")
    if not facts["province_ok"]:
        g_notes.append(facts["province_note"])
    detail["g"] = not g_notes
    findings += [f"(g) {n}" for n in g_notes]

    n = 1 if all(detail[k] for k in CONJUNCTS) else 0
    return n, findings, detail, facts, quote_note


# -------------------------------------------------------- the generator world
# Q74: this counter's evidence cells are mechanically populatable from the page
# bytes, so the counter BUILDS the complete proposed evidence shape from the
# measured revision's own committed bytes and scores it with the SAME check().
# Its score is printed beside the headline and never gates: it says whether the
# headline measures FORM (and the sourcing judgement stays with the non-author
# reviewers), or whether the shape is not even mechanically reachable.

GEN_SCOPE = ("the SDK's `allowedTools`/`allowed_tools` query-config grant in "
             "addition to frontmatter, with a managed-settings override")
GEN_TEACHES = ("the Agent SDK page states the second grant channel and the "
               "managed-settings override")
GEN_TEXTVIEW = ("Text view: a Markdown snapshot has every backtick byte deleted "
                "and an unordered-list marker removed at a line start; every "
                "snapshot then has whitespace collapsed.")


def _mech_quote(lines: list[str], heads: set[int]) -> str | None:
    """The mechanical quote: the shortest 5..25-word window that starts at a
    field-token word and passes this counter's own Q70 locator."""
    words: list[str] = []
    for line in lines:
        words.extend(line.split())
    for i, w in enumerate(words):
        if not field_token(w):
            continue
        for width in range(MIN_QUOTE_WORDS, MAX_QUOTE_WORDS + 1):
            if i + width > len(words):
                break
            cand = ws(" ".join(words[i:i + width]))
            if not field_token(cand):
                continue
            if quote_location(lines, cand, heads)[0]:
                return cand
    return None


def _mech_anchor(nbytes: int) -> str:
    return (f"§ Pre-approve tools for skills; fetched {CAPTURE}, HTTP 200, "
            f"{nbytes} B, sha256 {SNAPSHOT_PIN}; snapshot {SNAPSHOT_PATH}")


def _mech_row(sid: str, status: str) -> str:
    cells = [sid, f"Claude Code — Agent SDK — Skills — {CANONICAL_URL}", "docs",
             "A" if sid == SNAPSHOT_ID else "B", GEN_SCOPE, _mech_anchor(0),
             GEN_TEACHES, status, CAPTURE, "90d", ENTRY]
    return "| " + " | ".join(cells) + " |"


def _mech_files(quote: str, nbytes: int) -> dict[str, str]:
    reg = ("| id | source | kind | tier | scope | anchor | teaches | status | "
           "opened | recheck | used-by |\n|" + "---|" * REGISTRY_CELLS + "\n"
           + "\n".join(_mech_row(s, "mined" if s == SNAPSHOT_ID else "queued")
                       .replace(_mech_anchor(0), _mech_anchor(nbytes))
                       for s in (SNAPSHOT_ID, PREV_ROW)) + "\n")
    entry = (f'source: {SNAPSHOT_ID} — Claude Agent SDK — Skills — '
             f'{CANONICAL_URL} — § Pre-approve tools for skills — located '
             f'quote "{quote}" (snapshot {SNAPSHOT_PATH})\n'
             f"verified-at: {CAPTURE}\n"
             f"recheck: 90d — re-fetch the page and re-locate the quote\n"
             f"\n{GEN_TEXTVIEW}\n"
             f"\n# The Agent SDK's allowedTools channel (generator world)\n\n"
             f"Base `--rev` names a repo state; the counter names the "
             f"conjuncts.\n")
    skill = ("# fixture skill\n\n## Frontmatter craft\n\nTreat `allowed-tools` "
             "as pre-approval, never as a sandbox. Claude Agent SDK — "
             "query-config `allowedTools` (`allowed_tools` in Python) grants the "
             f"same pre-approval (S249/S248; entry {ENTRY}).\n\n"
             "## Gate registry\n\n"
             "| Name | Kind | Entry command | Verdict map | Self-test | Pinned "
             "values | Write scope | Owner |\n|---|---|---|---|---|---|---|---|\n"
             f"| `{COUNTER_PATH}` | gate | `python3 -B {COUNTER_PATH} --rev "
             "<rev>` | 0=clean, 1=failed, 2=could-not-evaluate | `--self-test` "
             "| in-file | none | kotoba |\n")
    readme = ("# corpus readme\n\n| Entry | Path | Teaches |\n|---|---|---|\n"
             f"| Agent SDK allowedTools channel (round 81) | "
             f"knowledge/{ENTRY.rsplit('/', 1)[-1]} | the SDK grant channel |\n")
    province = ("# fixture province\n\n## Core\n\n"
                "- Allowed-tools surfaces (round 80): six clients, entry "
                "corpus/knowledge/allowed-tools-surfaces-round80.md.\n"
                f"- Agent SDK channel (round 81): the SDK's `allowedTools`/"
                f"`allowed_tools` query-config grant with a managed-settings "
                f"override — {ENTRY}, counted by `{COUNTER_PATH} --rev <rev>`.\n"
                "\n## Frontier\n\n- none\n")
    lesson = ("# round 81 lessons\n\n## Gate\n\n"
              f"- {PREV_ROW} used-by — \u2192 {ENTRY} (old\u2192new logged).\n")
    return {SOURCES: reg, ENTRY: entry, SKILLMD: skill, README: readme,
            PROVINCE: province, LESSON: lesson}


def _commit_tree(root: Path, files: dict[str, str | bytes]) -> None:
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
        if isinstance(text, bytes):
            p.write_bytes(text)
        else:
            p.write_text(text)
    subprocess.run(git + ["add", "-A"], check=True, capture_output=True)
    subprocess.run(git + ["commit", "-qm", "world", "--allow-empty"],
                   check=True, capture_output=True, env=env)


def generator_world(repo: Repo) -> tuple[int, str]:
    """(M, note): the generator world's score under the same check()."""
    raw = repo.raw(SNAPSHOT_PATH)
    if raw is None:
        return 0, f"no committed snapshot at {SNAPSHOT_PATH}"
    if hashlib.sha256(raw).hexdigest() != SNAPSHOT_PIN:
        return 0, "the committed snapshot does not hash to the counter pin"
    lines, heads = view_with_headings(SNAPSHOT_PATH,
                                      raw.decode("utf-8", "replace"))
    quote = _mech_quote(lines, heads)
    if quote is None:
        return 0, "the page yielded no mechanical 5..25-word quote"
    files = {k: v for k, v in _mech_files(quote, len(raw)).items()}
    files[SNAPSHOT_PATH] = raw
    d = mktemp("k81-c2-generator-")
    try:
        _commit_tree(Path(d), files)
        n, _findings, _detail, _facts, _quote = check(Repo(Path(d), "HEAD"))
    except EnvError as exc:
        return 0, f"the generated world would not evaluate ({exc})"
    finally:
        shutil.rmtree(d, ignore_errors=True)
    return n, "generated mechanically from the measured bytes"


# ---------------------------------------------------------------- self-test
# Every world is an isolated local git repo under a fresh mktemp dir with TWO
# commits: the first is the "base" state the do-nothing figure is read from,
# the second the measured tip.  No lane, fleet repo or shared index is touched.

FIX_PAGE = "\n".join([
    "# Agent SDK skills",
    "",
    "> ## Documentation Index",
    "> Fetch the complete documentation index at: https://example.invalid/",
    "",
    "## Pre-approve tools for skills",
    "",
    "> [!NOTE]",
    ">",
    "> In SDK sessions, you can pre-approve tools for a project or personal "
    "skill with the skill's `allowed-tools` frontmatter or with the "
    "`allowedTools` option (`allowed_tools` in Python) in your query "
    "configuration.",
    "",
    "Skills run with the session's tools.",
    "",
    "The list pre-approves the named tools rather than restricting the others.",
    "",
    "## Troubleshooting",
    "",
    "Skills live in the project tree.",
]) + "\n"

FIX_QUOTE = ("In SDK sessions, you can pre-approve tools for a project or "
             "personal skill with the skill's allowed-tools frontmatter or "
             "with the allowedTools option")
FIX_PIN = hashlib.sha256(FIX_PAGE.encode()).hexdigest()


def _anchor(nbytes: int, pin: str) -> str:
    return (f"§ Pre-approve tools for skills; fetched {CAPTURE}, HTTP 200, "
            f"{nbytes} B, sha256 {pin}; snapshot {SNAPSHOT_PATH}")


def _reg(pages: dict[str, str], *, s249_status: str = "mined",
         tier: str = "A", used_by: str = ENTRY, extra: int = 0,
         url: str | None = None, anchor: str | None = None,
         s248_used_by: str = ENTRY) -> str:
    raw = pages[SNAPSHOT_ID].encode()
    pin = hashlib.sha256(raw).hexdigest()
    cells = [SNAPSHOT_ID, f"Claude Code — Agent SDK — Skills — "
                          f"{url or CANONICAL_URL}", "docs", tier, "fixture scope",
             anchor if anchor is not None else _anchor(len(raw), pin),
             "fixture teaches cell", s249_status, CAPTURE, "90d", used_by]
    cells += [f"extra{i}" for i in range(extra)]
    prev = [PREV_ROW, f"Claude Code — Agent SDK: Agent Skills — {CANONICAL_URL}",
            "docs", "B", "fixture scope", _anchor(len(raw), pin),
            "fixture teaches cell", "queued", CAPTURE, "90d", s248_used_by]
    head = ("| id | source | kind | tier | scope | anchor | teaches | status | "
            "opened | recheck | used-by |\n|" + "---|" * REGISTRY_CELLS + "\n")
    return ("# SOURCES fixture\n\n## Registry\n\n" + head
            + "| " + " | ".join(cells) + " |\n"
            + "| " + " | ".join(prev) + " |\n")


def _entry(quote: str = FIX_QUOTE, *, url: str = CANONICAL_URL,
           anchor: bool = True, verified: str = CAPTURE,
           recheck: bool = True) -> str:
    tail = f" (snapshot {SNAPSHOT_PATH})" if anchor else ""
    head = (f'source: {SNAPSHOT_ID} — Claude Agent SDK — Skills — {url} — '
            f'§ Pre-approve tools for skills — located quote "{quote}"{tail}')
    body = [""]
    body.append(f"verified-at: {verified}")
    if recheck:
        body.append("recheck: 90d — re-fetch the page and re-locate the quote")
    body += ["", GEN_TEXTVIEW, "",
             "# The Agent SDK's allowedTools channel", "",
             "The SDK states a second grant channel beside the frontmatter "
             "field.", ""]
    return head + "\n" + "\n".join(body)


SKILL_OK = ("# fixture skill\n\n## Frontmatter craft\n\nTreat `allowed-tools` "
            "as pre-approval, never as a sandbox (entry "
            "`corpus/knowledge/allowed-tools-surfaces-round80.md`). Claude Agent "
            "SDK — query-config `allowedTools` (`allowed_tools` in Python) grants "
            f"the same pre-approval (S249/S248; entry {ENTRY}).\n\n"
            "## Gate registry\n\n"
            "| Name | Kind | Entry command | Verdict map | Self-test | Pinned "
            "values | Write scope | Owner |\n|---|---|---|---|---|---|---|---|\n"
            f"| `{COUNTER_PATH}` | gate | `python3 -B {COUNTER_PATH} --rev "
            "<rev>` | 0=clean, 1=failed, 2=could-not-evaluate | `--self-test` "
            "| in-file | none | kotoba |\n")

README_OK = ("# corpus readme\n\n## Coverage map\n\n| Entry | Path | Teaches |\n"
             "|---|---|---|\n"
             "| Allowed-tools surfaces (round 80) | "
             "knowledge/allowed-tools-surfaces-round80.md | six clients |\n"
             "| Agent SDK allowedTools channel (round 81) | "
             "knowledge/allowed-tools-sdk-round81.md | the SDK grant channel |\n")

PROVINCE_OK = ("# fixture province\n\n## Core\n\n"
               "- Allowed-tools surfaces (round 80): six clients, entry "
               "corpus/knowledge/allowed-tools-surfaces-round80.md.\n"
               "- Agent SDK channel (round 81): the SDK's `allowedTools`/"
               "`allowed_tools` query-config grant with a managed-settings "
               f"override — {ENTRY}, counted by `{COUNTER_PATH} --rev <rev>`.\n"
               "\n## Frontier\n\n- none\n")

LESSON_OK = ("# round 81 lessons\n\n## Gate\n\n"
             f"- {PREV_ROW} used-by — \u2192 {ENTRY} (old\u2192new logged).\n")


def _honest(pages: dict[str, str] | None = None, *, entry: str | None = None,
            sources: str | None = None, skill: str = SKILL_OK,
            readme: str = README_OK, province: str = PROVINCE_OK,
            lesson: str = LESSON_OK, fetch: str | None = None) -> dict[str, str]:
    pages = pages if pages is not None else {SNAPSHOT_ID: FIX_PAGE}
    files = {SOURCES: sources if sources is not None else _reg(pages),
             ENTRY: entry if entry is not None else _entry(),
             SNAPSHOT_PATH: pages[SNAPSHOT_ID],
             SKILLMD: skill, README: readme, PROVINCE: province,
             LESSON: lesson}
    if fetch is not None:
        files[FETCH_JSON] = fetch
    return files


def _base_files() -> dict[str, str]:
    """The do-nothing state: the pre-round tree, no r81 files at all."""
    raw = FIX_PAGE.encode()
    pin = hashlib.sha256(raw).hexdigest()
    head = ("| id | source | kind | tier | scope | anchor | teaches | status | "
            "opened | recheck | used-by |\n|" + "---|" * REGISTRY_CELLS + "\n")
    prev = [PREV_ROW, f"Claude Code — Agent SDK: Agent Skills — {CANONICAL_URL}",
            "docs", "B", "fixture scope", _anchor(len(raw), pin),
            "fixture teaches cell", "queued", CAPTURE, "90d", "—"]
    return {
        SOURCES: "# SOURCES fixture\n\n## Registry\n\n" + head
                 + "| " + " | ".join(prev) + " |\n",
        SKILLMD: "# fixture skill\n\n## Frontmatter craft\n\nTreat "
                 "`allowed-tools` as pre-approval, never as a sandbox (entry "
                 "`corpus/knowledge/allowed-tools-surfaces-round80.md`).\n\n"
                 "## Gate registry\n\n| Name | Kind | Entry command | Verdict "
                 "map | Self-test | Pinned values | Write scope | Owner |\n"
                 "|---|---|---|---|---|---|---|---|\n",
        README: "# corpus readme\n\n## Coverage map\n\n| Entry | Path | "
                "Teaches |\n|---|---|---|\n"
                "| Allowed-tools surfaces (round 80) | "
                "knowledge/allowed-tools-surfaces-round80.md | six clients |\n",
        PROVINCE: "# fixture province\n\n## Core\n\n- Allowed-tools surfaces "
                  "(round 80): six clients, entry "
                  "corpus/knowledge/allowed-tools-surfaces-round80.md.\n"
                  "\n## Frontier\n\n- none\n",
    }


def _world(files: dict[str, str],
           base_files: dict[str, str] | None = None) -> tuple[str, str]:
    """A fresh isolated git repo: one base commit, then the measured commit."""
    d = mktemp("k81-c2-")
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

    place(base_files if base_files is not None else _base_files())
    base_sha = commit("base")
    place(files)
    commit("world")
    return d, base_sha


def _mutate(files: dict[str, str], **kw) -> dict[str, str]:
    out = dict(files)
    out.update(kw)
    return out


def _world_specs() -> list[dict]:
    """One satisfying world, then one broken world per conjunct plus the plan's
    C0-C4 controls.  Every broken arm asserts the exit code AND the finding
    that falsifies the conjunct: with N of 1, a single broken conjunct can only
    flip the headline to 0 of 1."""
    honest = _honest()
    one = "sdk allowed-tools surface documented 1 of 1"
    zero = "sdk allowed-tools surface documented 0 of 1"
    specs: list[dict] = []
    add = specs.append

    # ------------------------------------------------------ the satisfying world
    add(dict(label="satisfying world documents 1 of 1", files=honest, code=0,
             line=one, finding="conjuncts: a ok, b ok, c ok, d ok, e ok, f ok, "
                               "g ok"))
    add(dict(label="satisfying world reads 1 of 1 under a relative --repo .",
             files=honest, code=0, line=one, relative=True))
    add(dict(label="satisfying world prints the located quote's snapshot line",
             files=honest, code=0, line=one, finding="quote located on snapshot "
                                                     "line"))
    add(dict(label="satisfying world prints the generator world's score",
             files=honest, code=0, line=one,
             finding="generator world: 1 of 1"))
    add(dict(label="(c) the optional fetch record agreeing with the pin is "
                    "accepted", files=_honest(fetch=json.dumps(
                        {"url": CANONICAL_URL, "http": 200,
                         "bytes": len(FIX_PAGE.encode()), "sha256": FIX_PIN})),
             code=0, line=one))

    # ------------------------------------------- C0 / C4: do-nothing controls
    add(dict(label="C0 base world (no r81 files) reads 0 of 1",
             files=_base_files(), code=1, line=zero,
             finding=f"entry {ENTRY} absent"))
    add(dict(label="C4 first-answer baseline: 1 of 1 asserted over an entry-free "
                    "tree is not reachable", files=_base_files(), code=1,
             line=zero, finding="generator world: 0 of 1"))

    # ------------------------------------------------------------- (a) entry
    add(dict(label="(a) entry at another path is not the entry",
             files=_mutate(honest, **{ENTRY: None,
                                      "corpus/notes/allowed-tools-sdk.md":
                                          _entry()}), code=1, line=zero,
             finding=f"entry {ENTRY} absent"))
    add(dict(label="(a) entry without verified-at:", files=_mutate(
        honest, **{ENTRY: _entry(verified="2026-10-26")}), code=1, line=zero,
        finding="is not the round date"))
    add(dict(label="(a) entry without recheck:", files=_mutate(
        honest, **{ENTRY: _entry(recheck=False)}), code=1, line=zero,
        finding="no non-empty `recheck:` line"))
    add(dict(label="(a) source line without the canonical URL", files=_mutate(
        honest, **{ENTRY: _entry(url="https://example.invalid/agent-sdk/"
                                     "skills.md")}), code=1, line=zero,
        finding="carries the canonical URL"))
    add(dict(label="(a) source line without the snapshot anchor", files=_mutate(
        honest, **{ENTRY: _entry(anchor=False)}), code=1, line=zero,
        finding="names the pinned snapshot"))
    add(dict(label="(a) entry with no source: line at all", files=_mutate(
        honest, **{ENTRY: _entry().split("\n", 1)[1]}),
        code=1, line=zero, finding="carries no `source:` line"))

    # -------------------------------------------------------------- (b) row
    add(dict(label="(b) S249 row still queued", files=_mutate(
        honest, **{SOURCES: _reg({SNAPSHOT_ID: FIX_PAGE},
                                 s249_status="queued")}), code=1, line=zero,
        finding="status 'queued'"))
    add(dict(label="(b) S249 row tier C", files=_mutate(
        honest, **{SOURCES: _reg({SNAPSHOT_ID: FIX_PAGE}, tier="C")}),
        code=1, line=zero, finding="tier 'C'"))
    add(dict(label="(b) S249 row with 12 cells", files=_mutate(
        honest, **{SOURCES: _reg({SNAPSHOT_ID: FIX_PAGE}, extra=1)}),
        code=1, line=zero, finding="12 cells"))
    add(dict(label="(b) S249 used-by omits the entry", files=_mutate(
        honest, **{SOURCES: _reg({SNAPSHOT_ID: FIX_PAGE},
                                 used_by="corpus/knowledge/other.md")}),
        code=1, line=zero, finding="used-by"))
    add(dict(label="(b) S249 URL is a sibling path", files=_mutate(
        honest, **{SOURCES: _reg({SNAPSHOT_ID: FIX_PAGE}, url=(
            "https://code.claude.com/docs/en/agent-sdk/skills-old.md"))}),
        code=1, line=zero, finding="canonical page"))
    add(dict(label="(b) S249 URL is another host", files=_mutate(
        honest, **{SOURCES: _reg({SNAPSHOT_ID: FIX_PAGE}, url=(
            "https://example.invalid/docs/en/agent-sdk/skills.md"))}),
        code=1, line=zero, finding="canonical page"))

    # ----------------------------------------------------------- (c) snapshot
    add(dict(label="(c) anchor sha256 is not the pin", files=_mutate(
        honest, **{SOURCES: _reg({SNAPSHOT_ID: FIX_PAGE},
                                 anchor=_anchor(len(FIX_PAGE.encode()),
                                                "0" * 64))}),
        code=1, line=zero, finding="is not the counter pin"))
    add(dict(label="(c) anchor does not name the snapshot", files=_mutate(
        honest, **{SOURCES: _reg({SNAPSHOT_ID: FIX_PAGE}, anchor=(
            f"§ Pre-approve tools for skills; fetched {CAPTURE}, HTTP 200, "
            f"{len(FIX_PAGE.encode())} B, sha256 {FIX_PIN}"))}),
        code=1, line=zero, finding="does not name the snapshot"))
    add(dict(label="(c) anchor fetch record not HTTP 200", files=_mutate(
        honest, **{SOURCES: _reg({SNAPSHOT_ID: FIX_PAGE}, anchor=(
            f"§ Pre-approve tools; fetched {CAPTURE}, HTTP 404, "
            f"{len(FIX_PAGE.encode())} B, sha256 {FIX_PIN}"))}),
        code=1, line=zero, finding="carries no 'fetched"))
    add(dict(label="C3 quote asserted without committed snapshot bytes", files={
             ENTRY: _entry(), SOURCES: _reg({SNAPSHOT_ID: FIX_PAGE}),
             SKILLMD: SKILL_OK, README: README_OK, PROVINCE: PROVINCE_OK,
             LESSON: LESSON_OK}, code=2, line="environment error",
             finding="is not committed"))
    add(dict(label="pin-mismatch: the committed snapshot does not hash to the "
                    "counter pin", files=honest, code=2, line="environment "
                                                             "error",
             finding="snapshot_tampered", pin="0" * 64))
    add(dict(label="(c) a sibling fetch record stating a second digest is exit 2",
             files=_honest(fetch=json.dumps(
                 {"sha256": "0" * 64, "bytes": len(FIX_PAGE.encode())})),
             code=2, line="environment error",
             finding="pins two digests"))
    add(dict(label="(c) a sibling fetch record stating another byte count is "
                    "exit 2", files=_honest(fetch=json.dumps(
                        {"sha256": FIX_PIN, "bytes": 1})),
             code=2, line="environment error", finding="committed snapshot"))

    # -------------------------------------------------------------- (d) quote
    add(dict(label="(d) quote absent from the snapshot", files=_mutate(
        honest, **{ENTRY: _entry(quote="The allowedTools option is described "
                                       "somewhere else entirely on this page")}),
        code=1, line=zero, finding="not located after the text view"))
    add(dict(label="(d) quote under the 5-word floor", files=_mutate(
        honest, **{ENTRY: _entry(quote="the allowedTools option")}),
        code=1, line=zero, finding="located quote is 3 words"))
    add(dict(label="(d) quote over the 25-word ceiling", files=_mutate(
        honest, **{ENTRY: _entry(quote="allowedTools " + " ".join(
            ["word"] * 25))}), code=1, line=zero,
        finding="located quote is 26 words"))
    add(dict(label="(d) quote without the field token", files=_mutate(
        honest, **{ENTRY: _entry(quote="Skills run with the session's tools "
                                       "and nothing else here")}),
        code=1, line=zero, finding="names `allowed-tools` or `allowedTools`"))
    add(dict(label="(d) quote is the page title line (a heading)", files=_mutate(
        _honest({SNAPSHOT_ID: FIX_PAGE.replace(
            "Skills run with the session's tools.",
            "## The allowedTools option in your query configuration")}),
        **{ENTRY: _entry(quote="The allowedTools option in your query "
                               "configuration")}),
        code=1, line=zero, finding="heading line"))
    add(dict(label="(d) quote sits in the first-heading block", files=_mutate(
        _honest({SNAPSHOT_ID: "# Agent SDK skills\n\nThe allowedTools option in "
                              "your query configuration is stated here.\n\n"
                              "## Later\n\nBody text.\n"}),
        **{ENTRY: _entry(quote="The allowedTools option in your query "
                               "configuration is stated here")}),
        code=1, line=zero, finding="first-heading block"))
    add(dict(label="(d) the quote is matched after the Markdown text view "
                    "(backticks deleted)", files=_honest(), code=0, line=one))

    # ---------------------------------------------------------------- (e) S248
    add(dict(label="C2 row present but S248 used-by not updated", files=_mutate(
        honest, **{SOURCES: _reg({SNAPSHOT_ID: FIX_PAGE},
                                 s248_used_by="—")}), code=1, line=zero,
        finding=f"{PREV_ROW}: used-by"))
    add(dict(label="(e) the lesson does not log the old->new move",
             files=_mutate(honest, **{LESSON: "# round 81 lessons\n\n## Gate\n\n"
                                              "- nothing logged.\n"}),
             code=1, line=zero, finding="old->new move is not logged"))
    add(dict(label="(e) the lesson is absent", files=_mutate(
        honest, **{LESSON: None}), code=1, line=zero,
        finding="absent at"))

    # ----------------------------------------------------------------- (f) (g)
    add(dict(label="(f) SKILL.md carries no gate row", files=_mutate(
        honest, **{SKILLMD: SKILL_OK.split("## Gate registry")[0]}),
        code=1, line=zero, finding="no conformant gate row"))
    add(dict(label="(f) the gate row has an empty field", files=_mutate(
        honest, **{SKILLMD: SKILL_OK.replace("| in-file |", "|  |")}),
        code=1, line=zero, finding="no conformant gate row"))
    add(dict(label="(f) the SDK channel line sits outside the allowed-tools "
                    "rule area", files=_mutate(honest, **{SKILLMD: SKILL_OK
        .replace("Claude Agent SDK — query-config `allowedTools` "
                 "(`allowed_tools` in Python) grants the same pre-approval "
                 f"(S249/S248; entry {ENTRY}).", "")
        + "\n## Notes\n\n- Claude Agent SDK — `allowedTools` "
          "(`allowed_tools`) grants the same pre-approval.\n"}),
        code=1, line=zero, finding="no line in the `allowed-tools` rule area"))
    add(dict(label="(f) SKILL.md without the rule paragraph", files=_mutate(
        honest, **{SKILLMD: "# fixture skill\n\n## Gate registry\n\n| Name | "
                             "Kind | Entry command | Verdict map | Self-test | "
                             "Pinned values | Write scope | Owner |\n"
                             "|---|---|---|---|---|---|---|---|\n"
                             f"| `{COUNTER_PATH}` | gate | `python3 -B` | "
                             "0=clean, 1=failed, 2=could-not-evaluate | "
                             "`--self-test` | in-file | none | kotoba |\n"}),
        code=1, line=zero, finding="no `allowed-tools` author-facing rule"))
    add(dict(label="(f) a gate-table row is not the allowed-tools rule area",
             files=_mutate(honest, **{SKILLMD: (
                 "# fixture skill\n\n## Gate registry\n\n| Name | Kind | Entry "
                 "command | Verdict map | Self-test | Pinned values | Write "
                 "scope | Owner |\n|---|---|---|---|---|---|---|---|\n"
                 f"| `{COUNTER_PATH}` | gate | `python3 -B {COUNTER_PATH} "
                 "--rev <rev>` | 0=clean, 1=failed, 2=could-not-evaluate — "
                 "`allowed-tools` pre-approval counter | `--self-test` | "
                 "in-file | none | kotoba |\n\n"
                 "Claude Agent SDK — `allowedTools` (`allowed_tools`) grants the "
                 "same pre-approval.\n")}),
             code=1, line=zero, finding="no `allowed-tools` author-facing rule"))
    add(dict(label="(g) README coverage row absent", files=_mutate(
        honest, **{README: "# corpus readme\n\n| Entry | Path |\n|---|---|\n"
                            "| other | knowledge/other.md |\n"}),
        code=1, line=zero, finding="carries no row naming"))
    add(dict(label="(g) PROVINCE Core bullet does not name the SDK channel",
             files=_mutate(honest, **{PROVINCE: PROVINCE_OK.replace(
                 "the SDK's `allowedTools`/`allowed_tools` query-config grant "
                 "with a managed-settings override — ", "the seventh surface — ")}),
             code=1, line=zero, finding="does not name the SDK channel"))
    add(dict(label="(g) two Core bullets name the entry", files=_mutate(
        honest, **{PROVINCE: PROVINCE_OK.replace(
            "## Frontier", f"- also `{ENTRY}` with `allowedTools`.\n\n"
                           f"## Frontier")}),
        code=1, line=zero, finding="bullet(s) name"))

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
    global BASE_REV, _INTERNAL_SELFTEST, SNAPSHOT_PIN
    saved_rev, saved_pin = BASE_REV, SNAPSHOT_PIN
    files = spec["files"]() if callable(spec["files"]) else spec["files"]
    pin = spec.get("pin")
    if pin is None:
        raw = files.get(SNAPSHOT_PATH)
        body = raw.encode() if isinstance(raw, str) else raw
        pin = hashlib.sha256(body).hexdigest() if body else FIX_PIN
    SNAPSHOT_PIN = pin
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
        BASE_REV, SNAPSHOT_PIN = saved_rev, saved_pin
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
        BASE_REV, SNAPSHOT_PIN = saved_rev, saved_pin
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
    specs = _world_specs()
    for spec in specs:
        ok, n, msg = _run_spec(spec)
        assertions += n
        if ok:
            print(f"PASS {msg}")
        else:
            failures += 1
            print(f"FAIL {msg}")
    print(f"self-test: {failures} failure(s) over {assertions} assertions "
          f"in {len(specs)} world(s)")
    return 0 if failures == 0 else 1


def fetch_recheck(repo_path: str | None, rev: str | None) -> int:
    """``--fetch``: the documented recheck path.  NETWORK; never a measurement.

    Fetches the canonical page, prints the fetch record beside the in-file pin,
    and — when ``--rev`` is given — re-locates the entry's located quote in the
    FETCHED bytes.  Exit 0 iff the fetched digest is the pin and (when an entry
    was read) the quote is locatable in what was fetched."""
    req = urllib.request.Request(CANONICAL_URL,
                                 headers={"User-Agent": "Mozilla/5.0"})
    try:
        with urllib.request.urlopen(req, timeout=60) as resp:
            status, raw = resp.status, resp.read()
    except OSError as exc:
        print(f"fetch error: {CANONICAL_URL}: {exc}", file=sys.stderr)
        return 2
    stamp = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
    got = hashlib.sha256(raw).hexdigest()
    print(f"fetched {stamp}, HTTP {status}, {len(raw)} B, sha256 {got}")
    print(f"pin match: {'yes' if got == SNAPSHOT_PIN else 'NO'} "
          f"(counter pin {SNAPSHOT_PIN})")
    ok = got == SNAPSHOT_PIN
    if rev:
        repo = Repo(Path(repo_path or ".").resolve(), rev)
        entry_text = repo.show(ENTRY)
        if entry_text is None:
            print(f"entry {ENTRY} absent at {rev}: no quote to re-locate")
            return 1
        lines, heads = view_with_headings(SNAPSHOT_PATH,
                                          raw.decode("utf-8", "replace"))
        located, note = quote_state(rendered(entry_text), lines, heads)
        print(f"quote re-located in the FETCHED bytes: "
              f"{'yes' if located else 'NO'}")
        print(note)
        ok = ok and located
    print("fetch recheck: this path reads the network and is NEVER the "
          "claim measurement")
    return 0 if ok else 1


def main(argv: list[str] | None = None) -> int:
    global _WORK
    ap = argparse.ArgumentParser(
        description="C2 SDK allowed-tools counter for kotoba round 81")
    ap.add_argument("--rev", default=None, help="measured revision")
    ap.add_argument("--repo", default=str(_default_repo()))
    ap.add_argument("--work", default=None,
                    help="parent directory for temp dirs (default: $TMPDIR)")
    ap.add_argument("--self-test", action="store_true")
    ap.add_argument("--print-self-sha", action="store_true",
                    help="print the blanked sha of this file and exit")
    ap.add_argument("--print-pins", action="store_true",
                    help="print the in-file snapshot pin and path and exit")
    ap.add_argument("--fetch", action="store_true",
                    help="recheck the canonical page over the network (never a "
                         "measurement)")
    args = ap.parse_args(argv)
    if args.print_self_sha:
        print(_blanked_sha(Path(__file__).read_text()))
        return 0
    if args.print_pins:
        print(f"SNAPSHOT_PIN = {SNAPSHOT_PIN}")
        print(f"SNAPSHOT_PATH = {SNAPSHOT_PATH}")
        print(f"CANONICAL_URL = {CANONICAL_URL}")
        return 0
    if args.fetch:
        return fetch_recheck(args.repo, args.rev)
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
        n, findings, detail, facts, quote_note = check(repo)
        m, why = generator_world(repo)
    except EnvError as exc:
        print(f"environment error: {exc}", file=sys.stderr)
        return 2
    print(f"sdk allowed-tools surface documented {n} of {TOTAL}")
    print(f"generator world: {m} of {TOTAL}")
    print(f"measured-rev: {args.rev}")
    print(f"snapshot: {SNAPSHOT_PATH} pin {SNAPSHOT_PIN[:12]}...")
    print("conjuncts: " + ", ".join(
        f"{k} {'ok' if detail[k] else 'FAIL'}" for k in CONJUNCTS))
    print(quote_note)
    print(f"{PREV_ROW} status {facts['s248_status']}; used-by "
          f"{facts['s248_used_by']}")
    print("s248 old->new logged in the lesson ok" if facts["lesson_ok"]
          else "s248 old->new logged in the lesson MISSING")
    print("skill sdk channel ok" if facts["skill_channel"]
          else "skill sdk channel MISSING")
    print("registry home ok" if facts["home"] else "registry home MISSING")
    print("readme coverage row ok" if facts["readme"]
          else "readme coverage row MISSING")
    print("province sdk channel ok" if facts["province_ok"]
          else "province sdk channel MISSING")
    print(f"province bullets naming the entry: {facts['province_count']}")
    for finding in findings:
        print(f"  {finding}")
    if m >= TARGET:
        print(f"  the generator world reaches the target ({m} of {TOTAL}): the "
              f"headline measures the FORM of the evidence shape, not the "
              f"sourcing judgement ({why})")
    return 0 if (n == TARGET and all(detail[k] for k in CONJUNCTS)) else 1


if __name__ == "__main__":
    sys.exit(main())
