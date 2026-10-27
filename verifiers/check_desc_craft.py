#!/usr/bin/env python3
"""check_desc_craft.py -- frozen C1 counter for kotoba round 76 (depth).

Claim under test (round 76, C1, axis depth): the lane has admitted the
description-craft guidance of S213 (`https://agentskills.io/skill-creation/
optimizing-descriptions.md`) as guide-advice evidence, with sha256-pinned
snapshots and located quotes, has acted on it in `SKILL.md`, and has audited
kotoba's own `description` against it.

Frozen predicate (plans/round-76.md, C1):

    python3 -B verifiers/check_desc_craft.py --rev <rev> prints
    `description craft backed K of 6` and exits 0 only when all six conjuncts
    hold at <rev>; at base b7f13f4b39cbd43076a85568adca763a6f674e7a it prints
    `description craft backed 0 of 6` and exits 1.

Six conjuncts (the counter prints one verdict line each; a conjunct fails
closed -- missing bytes are a FAIL, never an exception):

  (a) snapshot chain -- the three page bytes are committed under
      `.ufo/waves/round-76/snapshots/`; every digest appears identically in
      `snapshots/MANIFEST.sha256`, in `snapshots/fetch-record.json` (HTTP 200
      records) and in the pinned digest table of THIS file; and the round-76
      lesson `## Gate` carries the rule-1 access record -- URL, access date
      matching the fetch record, a <=25-word located quote -- and names the
      optimizing-descriptions digest.
      (The plan's first wording -- "the digest recorded in the S213 row's
      anchor update" -- was withdrawn by plans/round-76-addendum-1.md: CORPUS
      contract rule 2 forbids an in-place `anchor` edit, so the digest is
      pinned in the four places named above instead.)
  (b) located quotes -- `corpus/knowledge/description-craft-round76.md` carries
      >=4 located quotes from the optimizing-descriptions snapshot, each
      <=25 words, each occurring verbatim in the snapshot after the page's
      first heading, each absent from the other two snapshots (page-unique,
      not site chrome), and each on a line the entry itself cites.
      A span of fewer than 3 words is not treated as a quote.
  (c) act-on -- `SKILL.md` carries a description-craft rule row in section
      Body craft that cites `corpus/knowledge/description-craft-round76.md` and
      S213 and holds >=2 quote fragments that occur in the optimizing-
      descriptions snapshot.
  (d) self-audit -- the entry's audit table states the rendered `description`
      length and the first-sentence length of `SKILL.md` at <rev>, and those
      equal the values THIS counter recomputes from the measured revision's
      committed bytes.  Measurement convention, pinned here (round-76
      addendum 1): the YAML folded-scalar render of the whole `description:`
      block, CLIP chomping -- the block's terminating line break is kept.  For
      the round-76 base bytes that is 1022 characters; the whitespace-collapsed
      and stripped variant is 1021.  The counter prints BOTH variants and names
      the convention, so the off-by-one family that produced M75-1 cannot
      re-enter through measurement ambiguity.
  (e) registry -- row S213's `used-by` cell lists
      `corpus/knowledge/description-craft-round76.md`, and the old->new change
      is logged in `corpus/lessons/round-76.md` (both the old and the new
      used-by value, per CORPUS contract rule 2).
  (f) provenance -- the entry opens with `source:` (naming S213 and the URL),
      `verified-at:`, `recheck:`.

Output: one verdict line per conjunct, then the final line
`description craft backed K of 6`.  Exit 0 iff K == 6, 1 otherwise, 2 for a
could-not-evaluate environment (not a git worktree, unknown revision, or a
counter whose own bytes drifted from the frozen copy).

Integrity: the digest table below is a constant of this instrument and is
never read from the measured revision (Q33), so a landing that edits a
snapshot, its manifest line and its fetch record together is still refused.
The running file is checked against `SELF_SHA` (its own blanked sha256); after
any edit to this file, re-run `--print-self-sha` and write the printed value
into the SELF_SHA line.

Usage:
  python3 -B verifiers/check_desc_craft.py --rev <rev> [--repo DIR]
  python3 -B verifiers/check_desc_craft.py --self-test
  python3 -B verifiers/check_desc_craft.py --print-self-sha
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
from pathlib import Path

# ----------------------------------------------------------------- constants

TOTAL = 6

PAGES = ("optimizing-descriptions", "evaluating-skills", "best-practices")
PAGE_URL = {
    "optimizing-descriptions":
        "https://agentskills.io/skill-creation/optimizing-descriptions.md",
    "evaluating-skills":
        "https://agentskills.io/skill-creation/evaluating-skills.md",
    "best-practices":
        "https://agentskills.io/skill-creation/best-practices.md",
}
SID = "S213"
ENTRY = "corpus/knowledge/description-craft-round76.md"
SOURCES = "corpus/SOURCES.md"
SKILLMD = "SKILL.md"
LESSON = "corpus/lessons/round-76.md"
SNAPDIR = ".ufo/waves/round-76/snapshots"
MANIFEST = SNAPDIR + "/MANIFEST.sha256"
FETCHRECORD = SNAPDIR + "/fetch-record.json"
COUNTER_PATH = "verifiers/check_desc_craft.py"

BODY_CRAFT_HEADING_RE = re.compile(r"^#{2,4}\s+Body craft\b")
HEADING_RE = re.compile(r"^#{1,6}\s")
QUOTE_RE = re.compile(r'["\u201c]([^"\u201d]{3,400})["\u201d]')
BACKTICK_RE = re.compile(r"`([^`]{3,400})`")
CITED_LINE_RE = re.compile(r"optimizing-descriptions\.md:(\d+)")
SHORTHAND_LINE_RE = re.compile(r"(?:`|\()[:](\d{1,4})\b")
INT_RE = re.compile(r"^\d+$")
SOURCES_ROW_RE = re.compile(r"^\|\s*S(\d{3,})\s*\|")
SOURCES_HEADER_RE = re.compile(r"^\|\s*id\s*\|")
USED_BY_HEADER = "used-by"
OLD_USED_BY = "corpus/knowledge/skill-eval-artefacts-round70.md"
OLD_USED_BY_NAME = "skill-eval-artefacts-round70.md"
ENTRY_NAME = "description-craft-round76.md"

MIN_QUOTES = 4
MIN_QUOTE_WORDS = 3
MAX_QUOTE_WORDS = 25
MIN_FRAGMENTS = 2
MIN_FRAGMENT_WORDS = 3
MAX_LESSON_QUOTE_WORDS = 25

# Q33: the three page digests are constants of this instrument, never read
# from the measured revision.  Verified byte-identical on 2026-10-27 by two
# independent clients (curl by the snapshot seat, urllib by the recheck seat),
# and identical to the round-70 S210/S209 and the round-74 copy of the same
# pages: zero drift.
PAGE_SHA = {
    "optimizing-descriptions":
        "7cc54fbb6abbcf08c33e7b320fd01a1fb9696426270da3b588a398d243bfd837",
    "evaluating-skills":
        "a799805f3a285390c1b6e906b691f56684fa1031b499d177f664f464d99fb684",
    "best-practices":
        "ab9f3b6091a0f24816b52cd7b90a3fdf53e621f47dba13b36694be272b87fb41",
}

SELF_SHA = "d5a06d6e89c7515e46096515f631a921377252fe574153b266a8beeae96c9da1"   # blanked-sha of this file
SELF_LINE_RE = re.compile(r'^SELF_SHA = "[0-9a-f]*"', re.M)
WORK_DIR: Path | None = None


class EnvError(Exception):
    """Could not evaluate: exit 2, never a pass and never a fail."""


# --------------------------------------------------------------- text shaping

def _blanked_sha(text: str) -> str:
    return hashlib.sha256(
        SELF_LINE_RE.sub('SELF_SHA = ""', text).encode()).hexdigest()


def ws(text: str) -> str:
    """Collapse every whitespace run to one space (the only shaping allowed)."""
    return re.sub(r"\s+", " ", text).strip()


def words(text: str) -> int:
    return len(text.split())


def collapsed_with_map(lines: list[str]) -> tuple[str, list[int]]:
    """The whitespace-collapsed page text and the offset of each line in it.

    Line i owns the half-open offset range [offsets[i], offsets[i+1]); a match
    that starts at offset o belongs to the last line with offsets[i] <= o.
    """
    chunks: list[str] = []
    offsets: list[int] = []
    pos = 0
    for i, line in enumerate(lines):
        offsets.append(pos)
        if i:
            chunks.append(" ")
            pos += 1
        c = ws(line)
        chunks.append(c)
        pos += len(c)
    return "".join(chunks), offsets


def line_of_offset(offsets: list[int], offset: int) -> int:
    lo, hi = 0, len(offsets) - 1
    while lo < hi:
        mid = (lo + hi + 1) // 2
        if offsets[mid] <= offset:
            lo = mid
        else:
            hi = mid - 1
    return lo + 1                      # 1-based line number


def occurrences(text: str, needle: str) -> list[int]:
    """Every start offset of `needle` in `text` (overlapping allowed)."""
    out: list[int] = []
    if not needle:
        return out
    start = 0
    while True:
        i = text.find(needle, start)
        if i < 0:
            return out
        out.append(i)
        start = i + 1


def quote_spans(text: str) -> list[str]:
    """Distinct double-quoted spans of `text`, whitespace-collapsed."""
    out: list[str] = []
    for q in QUOTE_RE.findall(text):
        n = ws(q)
        if n and n not in out:
            out.append(n)
    return out


def backtick_spans(text: str) -> list[str]:
    out: list[str] = []
    for q in BACKTICK_RE.findall(text):
        n = ws(q)
        if n and n not in out:
            out.append(n)
    return out


# ---------------------------------------------------------------- git side

def _default_repo() -> Path:
    here = Path(__file__).resolve()
    return here.parent.parent


def _git(repo: Path, args: list[str]) -> subprocess.CompletedProcess:
    try:
        return subprocess.run(["git", "-C", str(repo)] + args,
                              capture_output=True)
    except OSError as exc:
        raise EnvError(f"git not runnable: {exc}") from exc


class Repo:
    """Committed bytes of one lane at one revision (read-only)."""

    def __init__(self, path: Path, rev: str):
        self.path, self.rev = path, rev

    def show_bytes(self, path: str) -> bytes | None:
        proc = _git(self.path, ["show", f"{self.rev}:{path}"])
        if proc.returncode == 0:
            return proc.stdout
        err = proc.stderr.decode("utf-8", "replace")
        if ("does not exist" in err or "exists on disk, but not in" in err
                or "Path '" in err or "unknown revision" in err
                or "does not exist in" in err or "Invalid object name" in err):
            return None
        raise EnvError(f"git show {self.rev}:{path} failed: {err.strip()}")

    def show(self, path: str) -> str | None:
        raw = self.show_bytes(path)
        return None if raw is None else raw.decode("utf-8", "replace")


# ------------------------------------------------------------------ YAML fold

def frontmatter_lines(text: str) -> list[str] | None:
    """The frontmatter body lines of a SKILL.md, or None."""
    lines = text.split("\n")
    if not lines or lines[0].strip() != "---":
        return None
    for i in range(1, len(lines)):
        if lines[i].strip() in ("---", "..."):
            return lines[1:i]
    return None


def render_description(skill_text: str) -> str | None:
    """The YAML value of the frontmatter `description` key, rendered.

    Hand-rolled on purpose: no verifier in this lane imports PyYAML, and the
    lane reads block scalars by hand.  Supports a plain scalar, a folded (`>`)
    and a literal (`|`) block scalar with the clip/strip/keep chomping
    indicators.  A folded scalar folds a line break between two non-empty
    lines into a single space; a run of k blank lines becomes k newlines.
    """
    fm = frontmatter_lines(skill_text)
    if fm is None:
        return None
    key_at = None
    for i, line in enumerate(fm):
        if line.startswith("description:"):
            key_at = i
            break
    if key_at is None:
        return None
    rest = fm[key_at][len("description:"):].strip()
    if not rest or rest[0] not in ">|":
        return rest.strip()
    indicator = rest[0]
    chomp = ""
    explicit_indent = None
    for ch in rest[1:]:
        if ch in "-+":
            chomp = ch
        elif ch.isdigit():
            explicit_indent = int(ch)
        elif ch.isspace() or ch == "#":
            break
        else:
            return None
    body: list[str] = []
    for line in fm[key_at + 1:]:
        if line.strip() == "":
            body.append("")
            continue
        if not line.startswith((" ", "\t")):
            break
        body.append(line)
    while body and body[-1].strip() == "":
        body.pop()
    if not body:
        return "" if chomp == "-" else "\n"
    if explicit_indent is not None:
        indent = explicit_indent
    else:
        indent = min(len(l) - len(l.lstrip(" ")) for l in body if l.strip())
    stripped = [l[indent:] if l.strip() else "" for l in body]
    if indicator == "|":
        value = "\n".join(stripped)
    else:
        out: list[str] = []
        blanks = 0
        first = True
        for line in stripped:
            if line.strip() == "":
                blanks += 1
                continue
            if first:
                out.append(line)
                first = False
            elif blanks:
                out.append("\n" * blanks)
                out.append(line)
            else:
                out.append(" " + line)
            blanks = 0
        value = "".join(out)
    if chomp == "-":
        return value
    if chomp == "+":
        return value + "\n"
    return value + "\n" if value else value


def description_measures(skill_text: str) -> tuple[int, int, int] | None:
    """(clip length, stripped length, first-sentence length) of the render.

    The clip length is the pinned convention (plans/round-76-addendum-1.md);
    the stripped length is printed alongside it so the two readings can never
    be confused again.  The first sentence is the render up to the first
    `. ` boundary, the period included.
    """
    value = render_description(skill_text)
    if value is None:
        return None
    idx = value.find(". ")
    first = len(value) if idx < 0 else idx + 1
    return len(value), len(value.strip()), first


# ------------------------------------------------------------- snapshot side

class Snapshots:
    """The three committed page bodies of one revision."""

    def __init__(self, repo: Repo):
        self.repo = repo
        self.text: dict[str, str] = {}
        self.collapsed: dict[str, str] = {}
        self.offsets: dict[str, list[int]] = {}
        self.first_heading: dict[str, int] = {}
        self.digest: dict[str, str] = {}
        self.size: dict[str, int] = {}
        for page in PAGES:
            raw = repo.show_bytes(f"{SNAPDIR}/{page}.md")
            if raw is None:
                continue
            text = raw.decode("utf-8", "replace")
            lines = text.split("\n")
            collapsed, offsets = collapsed_with_map(lines)
            heading = 0
            for i, line in enumerate(lines):
                if HEADING_RE.match(line):
                    heading = i + 1
                    break
            self.text[page] = text
            self.collapsed[page] = collapsed
            self.offsets[page] = offsets
            self.first_heading[page] = heading
            self.digest[page] = hashlib.sha256(raw).hexdigest()
            self.size[page] = len(raw)

    def present(self, page: str) -> bool:
        return page in self.text

    def line_numbers(self, page: str, needle: str) -> list[int]:
        """1-based lines of `page` on which `needle` occurs.

        The occurrence must be inside ONE physical line: a quote is not
        stitched across a line break (the same rule the round-76 quote
        extraction used), so "verbatim" means one line of the fetched bytes.
        """
        return sorted(n for n, line in enumerate(self.text[page].split("\n"), 1)
                      if needle in ws(line))

    def after_first_heading(self, page: str, needle: str) -> bool:
        """Does `needle` occur in `page` after the page's first heading?"""
        head = self.first_heading[page]
        if head == 0:
            return False
        return any(ln > head for ln in self.line_numbers(page, needle))

    def occurs(self, page: str, needle: str) -> bool:
        return needle in self.collapsed[page]


# --------------------------------------------------------------- entry side

def entry_head(text: str) -> tuple[list[str], str | None, str | None]:
    """The provenance trio: leading `source:` lines, then verified-at, recheck."""
    lines = text.split("\n")
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


def paragraphs(text: str) -> list[str]:
    """Blank-line separated blocks of `text`."""
    out: list[str] = []
    current: list[str] = []
    for line in text.split("\n"):
        if line.strip():
            current.append(line)
        else:
            if current:
                out.append("\n".join(current))
                current = []
    if current:
        out.append("\n".join(current))
    return out


def markdown_tables(text: str):
    """Yield (header cells, row cells) for every markdown table in `text`."""
    block: list[str] = []

    def flush():
        if not block:
            return None
        head = _cells(block[0])
        rows = []
        for ln in block[1:]:
            c = _cells(ln)
            if not c or _is_separator(c):
                continue
            rows.append(c)
        block.clear()
        return head, rows

    for line in text.split("\n"):
        if line.strip().startswith("|"):
            block.append(line)
            continue
        got = flush()
        if got is not None:
            yield got
    got = flush()
    if got is not None:
        yield got


def _cells(line: str) -> list[str]:
    s = line.strip()
    if not (s.startswith("|") and s.endswith("|")) or len(s) < 2:
        return []
    return [c.strip() for c in s[1:-1].split("|")]


def _is_separator(row: list[str]) -> bool:
    return bool(row) and all(re.fullmatch(r":?-{3,}:?", c) for c in row)


def section(text: str, heading_re: re.Pattern) -> str | None:
    """The body of the section whose heading matches `heading_re`."""
    lines = text.split("\n")
    starts = [i for i, ln in enumerate(lines) if heading_re.match(ln)]
    if len(starts) != 1:
        return None
    start = starts[0]
    level = len(lines[start]) - len(lines[start].lstrip("#"))
    body: list[str] = []
    for line in lines[start + 1:]:
        m = HEADING_RE.match(line)
        if m and (len(line) - len(line.lstrip("#"))) <= level:
            break
        body.append(line)
    return "\n".join(body)


def registry_used_by(text: str, sid: str) -> str | None:
    """The `used-by` cell of registry row `sid`."""
    header: list[str] | None = None
    for line in text.split("\n"):
        if SOURCES_HEADER_RE.match(line):
            header = [c.strip() for c in line.strip().strip("|").split("|")]
            continue
        m = SOURCES_ROW_RE.match(line)
        if not m or header is None:
            continue
        if "S" + m.group(1) != sid:
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) != len(header):
            continue
        return cells[header.index(USED_BY_HEADER)]
    return None


def cited_lines(entry_text: str) -> set[int]:
    """Every snapshot line number the entry cites, full form or shorthand.

    Full form: `optimizing-descriptions.md:25`.  Shorthand: a backticked or
    parenthesised `:25` (the round-74/round-76 entry house style).
    """
    out: set[int] = set()
    for m in CITED_LINE_RE.finditer(entry_text):
        out.add(int(m.group(1)))
    for m in SHORTHAND_LINE_RE.finditer(entry_text):
        out.add(int(m.group(1)))
    return out


def audit_values(entry_text: str) -> tuple[set[int], set[int]]:
    """(description-length values, first-sentence-length values) in the entry.

    A row counts when its FIRST cell (the table's measure column) names the
    measure; the value is the second cell when that cell is a bare integer.
    Only the measure column is read, so a prose cell that happens to mention
    a length cannot inject a number.
    """
    desc: set[int] = set()
    first: set[int] = set()
    for header, rows in markdown_tables(entry_text):
        for row in rows:
            if len(row) < 2:
                continue
            low = ws(re.sub(r"[`*]", "", row[0])).lower()
            is_first = "first" in low and "sentence" in low and "length" in low
            is_desc = "description" in low and "length" in low
            if not (is_first or is_desc):
                continue
            value = None
            for cell in row[1:]:
                candidate = ws(re.sub(r"[`*]", "", cell))
                if INT_RE.match(candidate):
                    value = candidate
                    break
            if value is None:
                continue
            n = int(value)
            (first if is_first else desc).add(n)
    return desc, first


# ------------------------------------------------------------- conjuncts

def conjunct_a(repo: Repo, snaps: Snapshots) -> tuple[bool, list[str]]:
    """The snapshot chain: bytes, manifest, fetch record, pins, lesson Gate."""
    notes: list[str] = []
    ok = True

    for page in PAGES:
        if not snaps.present(page):
            ok = False
            notes.append(f"(a) {page}.md is not committed at {SNAPDIR}/")
            continue
        if snaps.digest[page] != PAGE_SHA[page]:
            ok = False
            notes.append(f"(a) {page}.md sha256 {snaps.digest[page]} is not the "
                         f"digest pinned in the counter ({PAGE_SHA[page]})")

    manifest = repo.show(MANIFEST)
    if manifest is None:
        ok = False
        notes.append(f"(a) {MANIFEST} is not committed at the measured revision")
    else:
        pinned: dict[str, str] = {}
        for n, line in enumerate(manifest.split("\n"), 1):
            s = line.strip()
            if not s or s.startswith("#"):
                continue
            m = re.fullmatch(r"([0-9a-f]{64})[ \t]+\*?(\S.*)", s)
            if not m:
                ok = False
                notes.append(f"(a) {MANIFEST}:{n} is not `<sha256> <file>`: {s!r}")
                continue
            pinned[m.group(2).rsplit("/", 1)[-1]] = m.group(1)
        for page in PAGES:
            name = page + ".md"
            if name not in pinned:
                ok = False
                notes.append(f"(a) {MANIFEST} pins no {name}")
            elif pinned[name] != PAGE_SHA[page]:
                ok = False
                notes.append(f"(a) {MANIFEST} pins {name} to "
                             f"{pinned[name][:12]}..., not {PAGE_SHA[page][:12]}...")

    record = repo.show(FETCHRECORD)
    if record is None:
        ok = False
        notes.append(f"(a) {FETCHRECORD} is not committed at the measured revision")
    else:
        try:
            rows = json.loads(record)
        except ValueError as exc:
            ok = False
            rows = []
            notes.append(f"(a) {FETCHRECORD} is not JSON: {exc}")
        if not isinstance(rows, list):
            ok = False
            notes.append(f"(a) {FETCHRECORD} is not a JSON array")
            rows = []
        by_page: dict[str, dict] = {}
        for row in rows:
            if not isinstance(row, dict):
                continue
            name = str(row.get("filename", "")).rsplit("/", 1)[-1]
            url = str(row.get("url", ""))
            page = None
            for candidate in PAGES:
                if name == candidate + ".md" or url.endswith("/" + candidate + ".md"):
                    page = candidate
                    break
            if page is not None:
                by_page[page] = row
        for page in PAGES:
            row = by_page.get(page)
            if row is None:
                ok = False
                notes.append(f"(a) {FETCHRECORD} has no record for {page}.md")
                continue
            if row.get("http_status") != 200:
                ok = False
                notes.append(f"(a) {FETCHRECORD} record for {page}.md is not "
                             f"HTTP 200 ({row.get('http_status')!r})")
            if row.get("sha256") != PAGE_SHA[page]:
                ok = False
                notes.append(f"(a) {FETCHRECORD} digest for {page}.md is "
                             f"{str(row.get('sha256'))[:12]}..., not "
                             f"{PAGE_SHA[page][:12]}...")
            if snaps.present(page) and row.get("bytes") != snaps.size[page]:
                ok = False
                notes.append(f"(a) {FETCHRECORD} byte count for {page}.md is "
                             f"{row.get('bytes')!r}, the committed body is "
                             f"{snaps.size[page]}")
            url = str(row.get("url", ""))
            if url and not url.startswith("https://agentskills.io/"):
                ok = False
                notes.append(f"(a) {FETCHRECORD} url for {page}.md is not an "
                             f"agentskills.io URL: {url!r}")

    lesson = repo.show(LESSON)
    if lesson is None:
        ok = False
        notes.append(f"(a) {LESSON} is not committed at the measured revision")
    else:
        gate = _gate_section(lesson)
        if gate is None:
            ok = False
            notes.append(f"(a) {LESSON} has no single `## Gate` section")
        else:
            if PAGE_URL["optimizing-descriptions"] not in gate:
                ok = False
                notes.append("(a) the lesson Gate names no "
                             "optimizing-descriptions URL")
            dates = re.findall(r"\d{4}-\d{2}-\d{2}", gate)
            wanted = _fetch_dates(repo)
            if not dates:
                ok = False
                notes.append("(a) the lesson Gate carries no access date")
            elif wanted and not any(d in dates for d in wanted):
                ok = False
                notes.append(f"(a) the lesson Gate access date {sorted(dates)} "
                             f"does not match the fetch record date "
                             f"{sorted(wanted)}")
            lesson_quotes = [q for q in quote_spans(gate)
                             if words(q) <= MAX_LESSON_QUOTE_WORDS]
            located = False
            if snaps.present("optimizing-descriptions"):
                for q in lesson_quotes:
                    if snaps.after_first_heading("optimizing-descriptions", q):
                        located = True
                        break
            if not located:
                ok = False
                notes.append("(a) the lesson Gate carries no <=25-word quote "
                             "located in the optimizing-descriptions snapshot")
            if not _digest_mentioned(gate, PAGE_SHA["optimizing-descriptions"]):
                ok = False
                notes.append("(a) the lesson Gate names no digest for the "
                             "optimizing-descriptions snapshot")

    return ok, notes


def _gate_section(lesson: str) -> str | None:
    lines = lesson.split("\n")
    starts = [i for i, ln in enumerate(lines)
              if re.match(r"^##\s+Gate\s*$", ln)]
    if len(starts) != 1:
        return None
    start = starts[0]
    body: list[str] = []
    for line in lines[start + 1:]:
        if re.match(r"^##\s", line):
            break
        body.append(line)
    return "\n".join(body)


def _digest_mentioned(text: str, digest: str) -> bool:
    """Is `digest` named here, in full or in the lane's abbreviated form?"""
    if digest in text:
        return True
    for token in re.findall(r"[0-9a-f]{8,64}", text):
        if digest.startswith(token):
            return True
    return False


def _fetch_dates(repo: Repo) -> set[str]:
    record = repo.show(FETCHRECORD)
    if record is None:
        return set()
    try:
        rows = json.loads(record)
    except ValueError:
        return set()
    out: set[str] = set()
    for row in rows if isinstance(rows, list) else []:
        if isinstance(row, dict):
            stamp = str(row.get("fetched_at", ""))[:10]
            if re.fullmatch(r"\d{4}-\d{2}-\d{2}", stamp):
                out.add(stamp)
    return out


def conjunct_b(repo: Repo, snaps: Snapshots) -> tuple[bool, list[str]]:
    """Located, page-unique quotes in the entry."""
    notes: list[str] = []
    entry = repo.show(ENTRY)
    if entry is None:
        return False, [f"(b) {ENTRY} is not committed at the measured revision"]
    if not snaps.present("optimizing-descriptions"):
        return False, ["(b) the optimizing-descriptions snapshot is not "
                       "committed at the measured revision"]
    for page in PAGES:
        if page != "optimizing-descriptions" and not snaps.present(page):
            return False, [f"(b) the {page} snapshot (page-uniqueness baseline) "
                           "is not committed at the measured revision"]
    cited = cited_lines(entry)
    counted: list[str] = []
    for quote in quote_spans(entry):
        if not (MIN_QUOTE_WORDS <= words(quote) <= MAX_QUOTE_WORDS):
            continue
        if not snaps.after_first_heading("optimizing-descriptions", quote):
            continue
        if any(snaps.occurs(page, quote)
               for page in PAGES if page != "optimizing-descriptions"):
            continue
        lines = snaps.line_numbers("optimizing-descriptions", quote)
        if not lines or not (set(lines) & cited):
            continue
        counted.append(quote)
    if len(counted) < MIN_QUOTES:
        notes.append(f"(b) {ENTRY} carries {len(counted)} located page-unique "
                     f"quote(s) of the required {MIN_QUOTES}")
        return False, notes
    notes.append(f"(b) {ENTRY} carries {len(counted)} located page-unique "
                 f"quotes (<={MAX_QUOTE_WORDS} words each)")
    return True, notes


def conjunct_c(repo: Repo, snaps: Snapshots) -> tuple[bool, list[str]]:
    """The act-on row in SKILL.md section Body craft."""
    notes: list[str] = []
    skill = repo.show(SKILLMD)
    if skill is None:
        return False, [f"(c) {SKILLMD} is not committed at the measured revision"]
    body = section(skill, BODY_CRAFT_HEADING_RE)
    if body is None:
        return False, ["(c) SKILL.md has no single `Body craft` section heading"]
    if not snaps.present("optimizing-descriptions"):
        return False, ["(c) the optimizing-descriptions snapshot is not "
                       "committed at the measured revision"]
    rows: list[list[str]] = []
    for header, table_rows in markdown_tables(body):
        for row in table_rows:
            rows.append(row)
    counting = [row for row in rows
                if ENTRY in " ".join(row)
                and re.search(r"(?<![A-Za-z0-9])" + SID + r"(?![0-9])",
                              " ".join(row))]
    if not counting:
        return False, [f"(c) no Body craft row cites both {ENTRY} and {SID}"]
    fragments: set[str] = set()
    for row in counting:
        cell_text = " ".join(row)
        for span in quote_spans(cell_text) + backtick_spans(cell_text):
            if words(span) < MIN_FRAGMENT_WORDS:
                continue
            if snaps.after_first_heading("optimizing-descriptions", span):
                fragments.add(span)
    if len(fragments) < MIN_FRAGMENTS:
        return False, [f"(c) the counting Body craft row(s) carry "
                       f"{len(fragments)} quote fragment(s) located in the "
                       f"optimizing-descriptions snapshot, {MIN_FRAGMENTS} required"]
    notes.append(f"(c) {len(counting)} Body craft row(s) cite {ENTRY} and "
                 f"{SID}, carrying {len(fragments)} located quote fragment(s)")
    return True, notes


def conjunct_d(repo: Repo, snaps: Snapshots) -> tuple[bool, list[str]]:
    """The entry's audit table equals the recomputed measurement."""
    notes: list[str] = []
    entry = repo.show(ENTRY)
    if entry is None:
        return False, [f"(d) {ENTRY} is not committed at the measured revision"]
    skill = repo.show(SKILLMD)
    if skill is None:
        return False, [f"(d) {SKILLMD} is not committed at the measured revision"]
    measures = description_measures(skill)
    if measures is None:
        return False, ["(d) the frontmatter `description` of SKILL.md could "
                       "not be rendered"]
    clip, stripped, first = measures
    desc_values, first_values = audit_values(entry)
    if not desc_values:
        notes.append("(d) the entry carries no audit row stating the rendered "
                     "`description` length")
    elif clip not in desc_values or not desc_values <= {clip, stripped}:
        notes.append(f"(d) the entry's rendered `description` length "
                     f"{sorted(desc_values)} does not equal the recomputed "
                     f"clip render {clip} (stripped variant {stripped})")
    if not first_values:
        notes.append("(d) the entry carries no audit row stating the "
                     "first-sentence length")
    elif first_values != {first}:
        notes.append(f"(d) the entry's first-sentence length "
                     f"{sorted(first_values)} does not equal the recomputed "
                     f"{first}")
    if notes:
        return False, notes
    notes.append(f"(d) the entry's audit table matches the recomputed render "
                 f"(clip {clip} / stripped {stripped}, first sentence {first}; "
                 f"convention: YAML folded block, clip chomping)")
    return True, notes


def conjunct_e(repo: Repo, snaps: Snapshots) -> tuple[bool, list[str]]:
    """S213's used-by cell and the old->new log in the round-76 lesson."""
    notes: list[str] = []
    sources = repo.show(SOURCES)
    if sources is None:
        return False, [f"(e) {SOURCES} is not committed at the measured revision"]
    used_by = registry_used_by(sources, SID)
    if used_by is None:
        return False, [f"(e) {SOURCES} has no {SID} row with an 11-column shape"]
    if ENTRY not in used_by:
        return False, [f"(e) row {SID}'s used-by cell does not list {ENTRY}"]
    lesson = repo.show(LESSON)
    if lesson is None:
        return False, [f"(e) {LESSON} is not committed at the measured revision"]
    logged = False
    for para in paragraphs(lesson):
        if SID not in para:
            continue
        if ENTRY not in para and ENTRY_NAME not in para:
            continue
        # the old->new shape: the old value is named, or the paragraph names
        # both an "old" and a "new" side of the change (the lane's two house
        # styles: "old->new: A -> B" and "used-by A -> B").
        low = para.lower()
        if OLD_USED_BY_NAME in low:
            logged = True
            break
        if ("old" in low and ("new" in low or "→" in para or "->" in para)):
            logged = True
            break
    if not logged:
        return False, [f"(e) {LESSON} does not log the old->new used-by change "
                       f"of row {SID} (old {OLD_USED_BY}, new ... {ENTRY})"]
    notes.append(f"(e) row {SID}'s used-by lists {ENTRY} and the lesson logs "
                 "the old->new change")
    return True, notes


def conjunct_f(repo: Repo, snaps: Snapshots) -> tuple[bool, list[str]]:
    """The provenance trio at the head of the entry."""
    notes: list[str] = []
    entry = repo.show(ENTRY)
    if entry is None:
        return False, [f"(f) {ENTRY} is not committed at the measured revision"]
    src, verified_at, recheck = entry_head(entry)
    if not src:
        return False, [f"(f) {ENTRY} does not open with a `source:` line"]
    joined = " ".join(src)
    if not re.search(r"(?<![A-Za-z0-9])" + SID + r"(?![0-9])", joined):
        notes.append(f"(f) the entry's source line names no {SID}")
    if PAGE_URL["optimizing-descriptions"] not in joined:
        notes.append(f"(f) the entry's source line names no "
                     f"{PAGE_URL['optimizing-descriptions']}")
    if not verified_at:
        notes.append(f"(f) the entry carries no `verified-at:` field")
    elif not re.search(r"\d{4}-\d{2}-\d{2}", verified_at):
        notes.append(f"(f) the entry's `verified-at:` carries no date: "
                     f"{verified_at!r}")
    if not recheck:
        notes.append(f"(f) the entry carries no `recheck:` field")
    if notes:
        return False, notes
    notes.append(f"(f) the entry opens with source: ({SID} + URL), "
                 f"verified-at: {verified_at}, recheck: present")
    return True, notes


CONJUNCTS = (
    ("(a) snapshot chain", conjunct_a),
    ("(b) located quotes", conjunct_b),
    ("(c) act-on", conjunct_c),
    ("(d) self-audit", conjunct_d),
    ("(e) registry", conjunct_e),
    ("(f) provenance", conjunct_f),
)


# ------------------------------------------------------------------ verdict

def check(repo: Repo) -> tuple[int, list[str], list[str]]:
    """(conjuncts held, verdict lines, findings)."""
    snaps = Snapshots(repo)
    held = 0
    lines: list[str] = []
    findings: list[str] = []
    for label, fn in CONJUNCTS:
        ok, notes = fn(repo, snaps)
        if ok:
            held += 1
            lines.append(f"{label}: pass")
        else:
            lines.append(f"{label}: fail")
            findings.extend(notes)
    return held, lines, findings


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(
        description="C1 description-craft counter for kotoba round 76")
    ap.add_argument("--rev", default=None, help="measured revision")
    ap.add_argument("--repo", default=str(_default_repo()),
                    help="the measured git worktree (resolved before anything "
                         "is derived from it)")
    ap.add_argument("--work", default=None,
                    help="scratch directory for self-test worlds (defaults to TMPDIR)")
    ap.add_argument("--self-test", action="store_true")
    ap.add_argument("--print-self-sha", action="store_true",
                    help="print the blanked sha of this file and exit")
    args = ap.parse_args(argv)
    if args.print_self_sha:
        print(_blanked_sha(Path(__file__).read_text()))
        return 0
    if args.self_test:
        global WORK_DIR
        WORK_DIR = Path(args.work).expanduser().resolve() if args.work else None
        if WORK_DIR is not None:
            WORK_DIR.mkdir(parents=True, exist_ok=True)
        return selftest()
    if not args.rev:
        print("environment error: --rev <revision> is required",
              file=sys.stderr)
        return 2
    repo_path = Path(args.repo).expanduser().resolve()
    repo = Repo(repo_path, args.rev)
    top = _git(repo.path, ["rev-parse", "--show-toplevel"])
    if top.returncode != 0:
        print(f"environment error: --repo {args.repo} is not a git worktree",
              file=sys.stderr)
        return 2
    proc = _git(repo.path, ["rev-parse", "--verify", "-q",
                            f"{args.rev}^{{commit}}"])
    if proc.returncode != 0:
        print(f"environment error: --rev {args.rev} is not a commit",
              file=sys.stderr)
        return 2
    src = Path(__file__).read_text()
    if _blanked_sha(src) != SELF_SHA:
        print("environment error: counter drifted -- the running file is not "
              "the frozen counter (re-run --print-self-sha and write the "
              "printed value into the SELF_SHA line)", file=sys.stderr)
        return 2
    try:
        held, lines, findings = check(repo)
    except EnvError as exc:
        print(f"environment error: {exc}", file=sys.stderr)
        return 2
    print(f"measured-rev: {args.rev}")
    for line in lines:
        print(line)
    for finding in findings:
        print(f"  {finding}")
    print(f"description craft backed {held} of {TOTAL}")
    return 0 if held == TOTAL else 1


# ---------------------------------------------------------------- self-test
#
# Every world is an isolated local git repo under a fresh mktemp dir with TWO
# commits: the first is the "base" state, the second the measured tip.  No
# lane, fleet repo or shared index is touched.

FIXTURE_OD = """\
> ## Documentation Index
> Fetch the complete documentation index at: https://agentskills.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Optimizing skill descriptions

> How to improve your skill's description so it triggers reliably.

## Writing effective descriptions

* **Use imperative phrasing.** Frame the description as an instruction to the agent: "Use this skill when..." rather than "This skill does..."
* **Focus on user intent, not implementation.** Describe what the user is trying to achieve, not the skill's internal mechanics.
* **Err on the side of being pushy.** Explicitly list contexts where the skill applies, including cases where the user doesn't name the domain directly.
* **Keep it concise.** A few sentences to a short paragraph is usually right -- long enough to cover the skill's scope.

## The optimization loop

Avoid adding specific keywords from failed queries.
Check that the description stays under the 1024-character limit -- descriptions tend to grow during optimization.
"""

FIXTURE_ES = """\
> ## Documentation Index
> Fetch the complete documentation index at: https://agentskills.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Evaluating skill output quality

The main file you author by hand is evals/evals.json.
"""

FIXTURE_BP = """\
> ## Documentation Index
> Fetch the complete documentation index at: https://agentskills.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Best practices for skill creators

Match the specificity of your instructions to the fragility of the task.
Aim for moderate detail in the instructions you write.
"""

OD_QUOTES = (
    "Frame the description as an instruction to the agent",
    "Describe what the user is trying to achieve, not the skill's "
    "internal mechanics.",
    "Err on the side of being pushy",
    "Explicitly list contexts where the skill applies, including cases where "
    "the user doesn't name the domain directly",
    "A few sentences to a short paragraph is usually right",
)

BP_QUOTES = (
    "Match the specificity of your instructions to the fragility of the task.",
    "Aim for moderate detail in the instructions you write.",
)

FIXTURE_SKILL_DESC = [
    "Fixture lane audits and rewrites SKILL.md for trigger fidelity.",
    'Triggers: "skill file", "SKILL.md".',
    "Anti-triggers: general prompt engineering.",
]


def _fixture_skill(with_row: bool = True) -> str:
    fm = ["---", "name: fixture-lane", "description: >"]
    fm += ["  " + line for line in FIXTURE_SKILL_DESC]
    fm += ["---", "", "# fixture lane", "", "## Body craft -- the "
          "specification's skill-creation guides", "",
          "| rule | source | what a skill author does |",
          "|---|---|---|"]
    if with_row:
        fm.append("| write the description as an instruction about user intent "
                  "| S213 optimizing-descriptions; `" + ENTRY + "` | \"Frame "
                  "the description as an instruction to the agent\": tell the "
                  "agent when to reach for the skill, and \"Avoid adding "
                  "specific keywords from failed queries\" when an eval miss "
                  "prompts a rewrite. |")
    fm += ["", "## Trigger-fidelity checklist", "", "- fixture line", ""]
    return "\n".join(fm)


def _fixture_entry(quotes: tuple[str, ...] = OD_QUOTES,
                   page_text: str = FIXTURE_OD,
                   with_quotes: bool = True,
                   with_audit: bool = True,
                   audit_length: int | None = None) -> str:
    lines = page_text.split("\n")
    rows: list[str] = []
    if with_quotes:
        for i, quote in enumerate(quotes, 1):
            line_no = next((n for n, l in enumerate(lines, 1)
                            if quote in ws(l)), 1)
            rows.append(f"| optimizing-descriptions | S213 | rule {i} | "
                        f"\"{quote}\" | `optimizing-descriptions.md:{line_no}` "
                        f"| token {i} | action {i} |")
    skill = _fixture_skill()
    measures = description_measures(skill)
    assert measures is not None
    clip, stripped, first = measures
    head = [
        "source: S213 -- Agent Skills -- Optimizing skill descriptions -- "
        + PAGE_URL["optimizing-descriptions"] + " -- section Writing "
        "effective descriptions (`optimizing-descriptions.md:13`) -- located "
        "quote \"" + OD_QUOTES[0] + "\"",
        "verified-at: 2026-10-27",
        "recheck: 90d -- `grep -c -F -- \"Err on the side of being pushy\" "
        ".ufo/waves/round-76/snapshots/optimizing-descriptions.md` prints 1",
        "ground: fixture ground line.",
        "",
        "# Writing a skill's `description`",
        "",
        "| page | S id | rule | quote | location | tokens | action |",
        "|---|---|---|---|---|---|---|",
    ]
    tail = ["", "## This lane's own `description`, measured", "",
            "| measured field | value | how measured |", "|---|---|---|"]
    if with_audit:
        length = clip if audit_length is None else audit_length
        tail.append(f"| rendered `description` length (characters) | {length} "
                    "| the YAML folded block, clip chomping |")
        tail.append(f"| first sentence length (characters) | {first} | the "
                    "same render to the first `. ` boundary, period included |")
    tail.append("")
    return "\n".join(head + rows + tail)


def _fixture_sources(with_used_by: bool = True) -> str:
    header = ("| id | source | kind | tier | scope | anchor | teaches | status "
              "| opened | recheck | used-by |")
    sep = "|---|---|---|---|---|---|---|---|---|---|---|"
    used_by = OLD_USED_BY + (", " + ENTRY if with_used_by else "")
    row = ("| S213 | Agent Skills -- Optimizing skill descriptions -- "
           + PAGE_URL["optimizing-descriptions"] + " | docs | A | scope | "
           "anchor | teaches | mined | 2026-10-25 | 90d | " + used_by + " |")
    return "\n".join(["# SOURCES fixture", "", "## Registry", "", header, sep,
                      row, ""])


def _fixture_lesson(digest: str, with_log: bool = True) -> str:
    log = ("S213 `used-by` changed old -> new: `" + OLD_USED_BY + "` -> `"
           + OLD_USED_BY + ", " + ENTRY + "`.") if with_log else \
          "S213 was re-opened this round; no registry cell changed."
    return "\n".join([
        "# Round 76 lessons -- kotoba (fixture)", "",
        "## Gate", "",
        "Source opened this round: " + PAGE_URL["optimizing-descriptions"]
        + " (2026-10-27). Located quote: \"Err on the side of being pushy\" "
        "(7 words). Fetch record: `snapshots/fetch-record.json`; digest "
        + digest + ".", "",
        "## Registry changes", "", log, "",
    ])


def _sha(text: str) -> str:
    return hashlib.sha256(text.encode()).hexdigest()


def _manifest_of(snaps: dict[str, str]) -> str:
    return "".join(f"{_sha(v)}  {k}\n" for k, v in sorted(snaps.items()))


def _fetch_record_of(snaps: dict[str, str], status: int = 200) -> str:
    rows = []
    for i, (name, text) in enumerate(sorted(snaps.items())):
        rows.append(json.dumps({
            "url": PAGE_URL[name[:-3]],
            "fetched_at": "2026-10-27T16:57:5%dZ" % i,
            "http_status": status,
            "bytes": len(text.encode()),
            "sha256": _sha(text),
            "filename": name,
        }, indent=2))
    return "[\n" + ",\n".join(rows) + "\n]\n"


def _honest_files() -> dict[str, str]:
    snaps = {
        "optimizing-descriptions.md": FIXTURE_OD,
        "evaluating-skills.md": FIXTURE_ES,
        "best-practices.md": FIXTURE_BP,
    }
    skill = _fixture_skill()
    files = {
        SKILLMD: skill,
        SOURCES: _fixture_sources(),
        ENTRY: _fixture_entry(),
        LESSON: _fixture_lesson(_sha(FIXTURE_OD)),
        MANIFEST: _manifest_of(snaps),
        FETCHRECORD: _fetch_record_of(snaps),
    }
    for name, text in snaps.items():
        files[f"{SNAPDIR}/{name}"] = text
    return files


def _world(files: dict[str, str | None]) -> str:
    """A fresh isolated git repo: one base commit, then the measured commit."""
    d = tempfile.mkdtemp(prefix="k76-c1-",
                         dir=str(WORK_DIR) if WORK_DIR is not None else None)
    env = dict(os.environ, GIT_AUTHOR_NAME="t", GIT_AUTHOR_EMAIL="t@t",
               GIT_COMMITTER_NAME="t", GIT_COMMITTER_EMAIL="t@t")
    git = ["git", "-c", "commit.gpgsign=false", "-C", d]
    subprocess.run(git + ["init", "-q"], check=True, capture_output=True)
    top = subprocess.run(git + ["rev-parse", "--show-toplevel"], check=True,
                         capture_output=True, text=True)
    if Path(top.stdout.strip()).resolve() != Path(d).resolve():
        raise RuntimeError(f"fixture toplevel {top.stdout.strip()!r} != {d}")

    def commit(note: str) -> None:
        subprocess.run(git + ["add", "-A"], check=True, capture_output=True)
        subprocess.run(git + ["commit", "-qm", note, "--allow-empty"],
                       check=True, capture_output=True, env=env)

    def place(items: dict[str, str | None]) -> None:
        for rel, text in items.items():
            p = Path(d) / rel
            if text is None:               # a fixture deletion, not a file
                if p.exists():
                    p.unlink()
                continue
            p.parent.mkdir(parents=True, exist_ok=True)
            p.write_text(text)

    place({SKILLMD: "---\nname: base\ndescription: base\n---\n"})
    commit("base")
    place(files)
    commit("world")
    return d


def _mutate(files: dict[str, str | None],
            **kw: str | None) -> dict[str, str | None]:
    out = dict(files)
    out.update(kw)
    return out


def _world_specs() -> list[dict]:
    """One honest world, then one broken world per conjunct and per shortcut.

    Each arm changes exactly one thing, so the expected count is the honest
    count minus the conjuncts the defect breaks.
    """
    honest = _honest_files()
    specs: list[dict] = []
    add = specs.append

    add(dict(label="honest world scores 6 of 6", files=honest, code=0,
             line="description craft backed 6 of 6", count=6))

    # (a) the snapshot chain
    empty = {k: v for k, v in honest.items()
             if not k.startswith(SNAPDIR + "/")}
    add(dict(label="(a) empty snapshot set", files=empty, code=1,
             line="description craft backed 3 of 6", count=3,
             finding="is not committed at .ufo/waves/round-76/snapshots/"))
    add(dict(label="(a) manifest digest mismatch", files=_mutate(
        honest, **{MANIFEST: _manifest_of({
            "optimizing-descriptions.md": FIXTURE_OD + "x",
            "evaluating-skills.md": FIXTURE_ES,
            "best-practices.md": FIXTURE_BP})}),
        code=1, line="description craft backed 5 of 6", count=5,
        finding="pins optimizing-descriptions.md to"))
    add(dict(label="(a) fetch record without HTTP 200", files=_mutate(
        honest, **{FETCHRECORD: _fetch_record_of({
            "optimizing-descriptions.md": FIXTURE_OD,
            "evaluating-skills.md": FIXTURE_ES,
            "best-practices.md": FIXTURE_BP}, status=404)}),
        code=1, line="description craft backed 5 of 6", count=5,
        finding="is not HTTP 200"))
    add(dict(label="(a) lesson Gate without the digest", files=_mutate(
        honest, **{LESSON: _fixture_lesson("0" * 64)}),
        code=1, line="description craft backed 5 of 6", count=5,
        finding="names no digest for the optimizing-descriptions snapshot"))
    add(dict(label="(a) lesson Gate without a located quote", files=_mutate(
        honest, **{LESSON: _fixture_lesson(_sha(FIXTURE_OD)).replace(
            '"Err on the side of being pushy"', '"no such quote"')}),
        code=1, line="description craft backed 5 of 6", count=5,
        finding="carries no <=25-word quote located"))

    # (b) the located quotes
    add(dict(label="(b) quote found only in the best-practices snapshot",
             files=_mutate(honest, **{ENTRY: _fixture_entry(
                 quotes=BP_QUOTES)}),
             code=1, line="description craft backed 5 of 6", count=5,
             finding="located page-unique quote(s) of the required 4"))
    add(dict(label="(b) entry without quotes", files=_mutate(
        honest, **{ENTRY: _fixture_entry(with_quotes=False)}),
        code=1, line="description craft backed 5 of 6", count=5,
        finding="located page-unique quote(s) of the required 4"))
    add(dict(label="(b) a quote with no line citation", files=_mutate(
        honest, **{ENTRY: _fixture_entry().replace(
            "optimizing-descriptions.md:", "unlocated-page:")}),
        code=1, line="description craft backed 5 of 6", count=5,
             finding="located page-unique quote(s) of the required 4"))

    # (c) the act-on row
    add(dict(label="(c) SKILL.md without the counting row", files=_mutate(
        honest, **{SKILLMD: _fixture_skill(with_row=False)}),
        code=1, line="description craft backed 5 of 6", count=5,
        finding="no Body craft row cites both"))
    add(dict(label="(c) the row carries no located fragment", files=_mutate(
        honest, **{SKILLMD: _fixture_skill().replace(
            '"Frame the description as an instruction to the agent"', '"x"')
            .replace(
            '"Avoid adding specific keywords from failed queries"', '"y"')}),
        code=1, line="description craft backed 5 of 6", count=5,
        finding="quote fragment(s) located in the"))

    # (d) the audit table
    add(dict(label="(d) stripped 1021 is not the clip-preserving 1022 audit value",
             files=_mutate(honest, **{ENTRY: _fixture_entry(
                 audit_length=1021)}),
             code=1, line="description craft backed 5 of 6", count=5,
             finding="does not equal the recomputed clip render"))
    add(dict(label="(d) audit table absent", files=_mutate(
        honest, **{ENTRY: _fixture_entry(with_audit=False)}),
        code=1, line="description craft backed 5 of 6", count=5,
        finding="carries no audit row stating the rendered"))

    # (e) the registry
    add(dict(label="(e) missing used-by", files=_mutate(
        honest, **{SOURCES: _fixture_sources(with_used_by=False)}),
        code=1, line="description craft backed 5 of 6", count=5,
        finding="used-by cell does not list"))
    add(dict(label="(e) the old->new change is not logged", files=_mutate(
        honest, **{LESSON: _fixture_lesson(_sha(FIXTURE_OD), with_log=False)}),
        code=1, line="description craft backed 5 of 6", count=5,
        finding="does not log the old->new used-by change"))

    # (f) the provenance trio
    add(dict(label="(f) no recheck field", files=_mutate(
        honest, **{ENTRY: _fixture_entry().replace(
            "recheck: 90d -- `grep", "x: 90d -- `grep")}),
        code=1, line="description craft backed 5 of 6", count=5,
        finding="carries no `recheck:` field"))
    add(dict(label="(f) no verified-at field", files=_mutate(
        honest, **{ENTRY: _fixture_entry().replace(
            "verified-at: 2026-10-27", "y: 2026-10-27")}),
        code=1, line="description craft backed 5 of 6", count=5,
        finding="carries no `verified-at:` field"))

    # plan's shortcut control (Q37, C1-W3): a token dump naming all six
    # conjuncts, with no content behind them.  Its provenance trio is even
    # honest -- the source line names S213 and the URL -- so that only the
    # content-bearing conjuncts (b) and (d) can fail it.
    add(dict(label="shortcut: token dump naming all six conjuncts",
             files=_mutate(honest, **{ENTRY:
                 "source: S213 -- Agent Skills -- Optimizing skill descriptions "
                 "-- " + PAGE_URL["optimizing-descriptions"]
                 + " -- § Writing effective descriptions "
                 "(`optimizing-descriptions.md:13`)\n"
                 "verified-at: 2026-10-27\nrecheck: 90d\n\n"
                 "# (a) snapshot chain (b) located quotes (c) act-on "
                 "(d) self-audit (e) registry (f) provenance\n"}),
             code=1, line="description craft backed 4 of 6", count=4,
             finding="carries 0 located page-unique quote(s) of the required 4"))
    return specs


def _run_spec(spec: dict) -> tuple[bool, int, str]:
    """Run one world through ``main()`` in its own isolated git repo."""
    global PAGE_SHA
    saved = dict(PAGE_SHA)
    snaps = {"optimizing-descriptions": FIXTURE_OD,
             "evaluating-skills": FIXTURE_ES,
             "best-practices": FIXTURE_BP}
    for page, text in snaps.items():
        PAGE_SHA[page] = _sha(text)
    d = _world(spec["files"])
    buf = io.StringIO()
    saved_cwd = os.getcwd()
    try:
        with contextlib.redirect_stdout(buf), contextlib.redirect_stderr(buf):
            code = main(["--repo", d, "--rev", "HEAD"])
    finally:
        os.chdir(saved_cwd)
        shutil.rmtree(d, ignore_errors=True)
        PAGE_SHA.clear()
        PAGE_SHA.update(saved)
    out = buf.getvalue()
    checks = [code == spec["code"]]
    if spec.get("line") is not None:
        checks.append(spec["line"] in out)
    if spec.get("finding") is not None:
        checks.append(spec["finding"] in out)
    ok = all(checks)
    msg = f"{spec['label']}: exit {code}"
    if not ok:
        msg += (f" (want {spec['code']}; line={spec.get('line')!r}; "
                f"finding={spec.get('finding')!r}); output={out!r}")
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
    print(f"self-test: {failures} failure(s) over {assertions} assertions")
    return 0 if failures == 0 and assertions >= 30 else 1


if __name__ == "__main__":
    sys.exit(main())
