#!/usr/bin/env python3
"""check_sibling_census.py -- content guard for the round-49 sibling-overlap census.

Landing path (intended): `verifiers/check_sibling_census.py` in
/home/vgpnk/Projects/shokunin/kotoba-shokunin.

Why this file exists
--------------------
Round 49, claim C1 (axis: adjacency) lands
`corpus/knowledge/sibling-overlap-census-round49.md`: one row per sibling lane
repo under the fleet root, each row carrying the sibling's pinned commit, the
skill file(s), a located quote of the sibling's own scope, a classification
against kotoba's province (`contested` / `adjacent` / `none`) and whether the
sibling's description carries an arbitration clause.

The routed defect from the round-48 spot-check (R2) is that a counter must be
able to FAIL on empty or false content.  A census of 20 sibling lanes, each row
carrying a quote copied out of a sibling repo, is exactly the shape a
content-blind counter passes vacuously: an empty table, a quote that was never
in the file it is attributed to, a commit that does not hold the bytes, a lane
that was never surveyed.  This instrument is that content guard; it is
committed with the entry and re-reads every quote at its pinned commit, live,
every time it runs.

What it checks
--------------
Input: a markdown file whose census table rows have the form

    | <lane> | <branch> | <commit40> | <path> | <classification> |
    <names kotoba> | <arbitration> | <path:line> | <quote> |

(the header row and the separator row are skipped; the quote cell may be
wrapped in double quotes or backticks).

Per row:
  * every cell is non-empty -- an empty quote cell is FALSE CONTENT: an empty
    needle matches any haystack, so it must be rejected, never "found";
  * the commit cell is a 40-hex object id;
  * the classification cell is one of contested / adjacent / none;
  * the `path:line` cell splits into a path and a 1-based line number;
  * the quote has at least six words (round-49 falsify correction);
  * the skill-file, names-kotoba and arbitration cells equal what the pinned
    `SKILL.md` frontmatter description gives (re-derived, not trusted), and a
    `none` row's sibling description and PROVINCE.md at the pin do not name
    kotoba (round-49 falsify correction, seat CriticC1Landed);
  * `git -C <fleet>/<lane>-shokunin show <commit>:<path>` is run, and the
    quote occurs verbatim -- after collapsing whitespace runs on both sides --
    on the cited line or within +/-2 lines of it;
  * the located line is not a markdown heading: a title-only quote is not a
    scope statement.

Census-wide:
  * the set of lanes named in the table equals the set of `*-shokunin`
    directories under --fleet (default /home/vgpnk/Projects/shokunin) minus
    kotoba itself;
  * no lane is named by more than one row: a duplicated row inflates the
    row count without surveying a new lane, and the lane-set check cannot
    see it (a set collapses the duplicate).  Round-50 routed defect D3, from
    the round-49 falsify finding that a duplicated census row passed with
    `rows 21 verified 21`.  The duplicated lane is named on stdout.

With --province PATH (PROVINCE.md), additionally:
  * only the `## Adjacent` section is read (it ends at the next `## ` heading);
  * that section must hold a markdown table whose rows are
    `| <lane> | <classification> | <commit40> | <free text> |`; a bare-name
    list under `## Adjacent` is a FAIL, not a pass;
  * the province table's lane set must equal the census lane set exactly, and
    each row's classification and commit must equal the census row's;
  * the province table must not have fewer rows than the sibling-lane set;
  * no lane is named by more than one row of the `## Adjacent` table either
    (the same round-50 D3 refusal as for the census table).

With --skill PATH (a SKILL.md), additionally:
  * the YAML frontmatter `description` of PATH is read (the same
    `description_of` helper the sibling rows are checked with); the value ends
    at ANY column-0 line, so a column-0 YAML comment is not swallowed into
    the description (round-50 mutant m8);
  * every census lane whose classification is not `none` must appear in that
    description as a whole token, case-insensitively (the same `token_in`
    helper), and each census lane counts once however often it is written;
  * G1 -- clause binding: a name is not arbitration.  The description is
    split into clauses and a lane counts as NAMED only when some clause that
    contains it also carries an ownership or routing marker.  The marker
    list is pinned in this file and the rule is a lexical approximation,
    named as such in every failure message that uses it; it has
    counterexamples in both directions (a clause with a marker and no lane is
    harmless; a lane named in a clause without a marker is refused even when
    the surrounding sentences do state a split);
  * G4 -- the parsed description must be 1 to 1024 characters (S018);
  * a lane that is missing from the description, or named without a marker,
    is a FAIL and is named on stdout;
  * the summary lines `skill description names K of N non-none lanes` and
    `skill description length L of 1024` are always printed, so the counts
    are readable even when the check fails.

Exit ladder (family contract; identical in every mode):
  0  every row verified and every cross-check held
  1  a check failed -- the failing row is named on stdout
  2  usage error (bad arguments, unreadable input file, missing fleet root)

Usage:
    check_sibling_census.py CENSUS.md [--fleet DIR] [--province PROVINCE.md]
                                   [--skill SKILL.md]
    check_sibling_census.py --self-test

The self-test builds throwaway git repos in a temp directory and asserts the
red arms of the content guard (mutated quote, wrong commit, missing lane,
empty table, empty quote cell, heading-line quote) plus the province arms
(bare-name list, classification mismatch, commit mismatch, extra lane, missing
lane, too few rows) and the matching-table green arm.  The round-50 arms add
the duplicate-row refusals (census table and province table, including a
case-variant duplicate and a consistent duplicate pair) and the --skill
description arms (a missing lane fails, a complete description passes, the
count lines are printed, the m1 bare list and the m5 negated mention are
refused, the m7 case-duplicates count once, the m8 column-0 comment is not
swallowed, and the length cap holds).  Its summary line follows the lane
convention so the floors guard can register it:
`self-test: N failure(s) over M assertions`.

Read-only: it reads the census file, the province file, the skill file and
the sibling repos through `git show`; it writes nothing outside its own temp
directory.

Stdlib only (Python >= 3.9).
"""

from __future__ import annotations

import argparse
import contextlib
import io
import os
import re
import subprocess
import sys
import tempfile
from pathlib import Path

LANE_SUFFIX = "-shokunin"
SELF_LANE = "kotoba"
CLASSIFICATIONS = ("contested", "adjacent", "none")
DEFAULT_FLEET = "/home/vgpnk/Projects/shokunin"
CENSUS_COLUMNS = 9
PROVINCE_COLUMNS = 4
LINE_TOLERANCE = 2

# Header words that identify the census table among the tables of a markdown
# file.  Used only to CHOOSE the table; the row shape is checked, never assumed.
CENSUS_HEADER_TOKENS = ("lane", "branch", "commit", "path", "class", "names",
                         "kotoba", "arbitrat", "quote")
PROVINCE_HEADER_TOKENS = ("lane", "class", "commit")

HEX40 = re.compile(r"\A[0-9a-fA-F]{40}\Z")
SEPARATOR_CELL = re.compile(r"\A:?-{2,}:?\Z")
WS_RUN = re.compile(r"\s+")
# A cell split on unescaped pipes; `\|` is a literal pipe inside a cell.
CELL_SPLIT = re.compile(r"(?<!\\)\|")
# A YAML block-scalar indicator at the head of a `description:` value.
BLOCK_SCALAR = re.compile(r"\A[>|][+-]?\s*")


# --------------------------------------------------------------------------
# table parsing
# --------------------------------------------------------------------------

def split_row(line):
    """Split one markdown table row into its cells (unescaping `\\|`)."""
    s = line.strip()
    if s.startswith("|"):
        s = s[1:]
    if s.endswith("|") and not s.endswith("\\|"):
        s = s[:-1]
    parts = CELL_SPLIT.split(s)
    return [p.replace("\\|", "|").strip() for p in parts]


def is_separator_row(cells):
    return bool(cells) and all(SEPARATOR_CELL.match(c) for c in cells)


def make_block(raw):
    """raw: list of (line_number, raw_line)."""
    header = split_row(raw[0][1])
    sep_line = None
    body = raw
    if len(raw) >= 2 and is_separator_row(split_row(raw[1][1])):
        sep_line = raw[1][0]
        body = raw[2:]
    rows = [(n, split_row(text)) for n, text in body]
    return {"header": header, "header_line": raw[0][0], "sep_line": sep_line,
            "rows": rows}


def parse_blocks(lines):
    """Group consecutive `|`-lines into table blocks."""
    blocks = []
    current = []
    for number, line in enumerate(lines, 1):
        if line.strip().startswith("|"):
            current.append((number, line))
        elif current:
            blocks.append(make_block(current))
            current = []
    if current:
        blocks.append(make_block(current))
    return blocks


def _score_header(header, tokens):
    lowered = [c.lower() for c in header]
    return sum(1 for token in tokens if any(token in cell for cell in lowered))


def _select_table(blocks, columns, tokens):
    """Pick the table with `columns` cells and the best header score."""
    candidates = [b for b in blocks
                  if b["sep_line"] is not None and len(b["header"]) == columns]
    if not candidates:
        candidates = [b for b in blocks
                      if b["sep_line"] is not None
                      and any(len(c) == columns for _, c in b["rows"])]
    if not candidates:
        return None
    best = None
    best_score = -1
    for block in candidates:
        score = _score_header(block["header"], tokens)
        if score > best_score:
            best, best_score = block, score
    return best


def select_census_table(blocks):
    return _select_table(blocks, CENSUS_COLUMNS, CENSUS_HEADER_TOKENS)


def select_province_table(blocks):
    return _select_table(blocks, PROVINCE_COLUMNS, PROVINCE_HEADER_TOKENS)


# --------------------------------------------------------------------------
# small helpers
# --------------------------------------------------------------------------

def collapse(text):
    """Collapse whitespace runs to a single space; strip the ends."""
    return WS_RUN.sub(" ", text).strip()


def strip_wrapping(cell):
    """Remove a wrapping pair of double quotes or backticks, then whitespace."""
    s = cell.strip()
    changed = True
    while changed and len(s) >= 2:
        changed = False
        if (s[0] == '"' and s[-1] == '"') or (s[0] == "`" and s[-1] == "`"):
            s = s[1:-1].strip()
            changed = True
    return s


def normalize_lane(cell):
    """`audio` and `audio-shokunin` both normalize to `audio`."""
    s = strip_wrapping(cell).strip()
    low = s.lower()
    if low.endswith(LANE_SUFFIX):
        s = s[: -len(LANE_SUFFIX)]
    return s.strip().lower()


def repo_dir_for(lane_raw, fleet_root):
    """Directory of the sibling repo for a lane cell."""
    s = strip_wrapping(lane_raw).strip()
    if s.lower().endswith(LANE_SUFFIX):
        return fleet_root / s
    return fleet_root / (s + LANE_SUFFIX)


def split_path_line(cell):
    """`SKILL.md:42` -> ("SKILL.md", 42).  Raises ValueError when malformed."""
    s = strip_wrapping(cell).strip()
    if ":" not in s:
        raise ValueError("no line number in %r" % cell)
    path, _, number = s.rpartition(":")
    path = path.strip()
    number = number.strip()
    if not path:
        raise ValueError("no path in %r" % cell)
    if not number.isdigit():
        raise ValueError("line %r is not a number in %r" % (number, cell))
    line = int(number)
    if line < 1:
        raise ValueError("line %d is not 1-based in %r" % (line, cell))
    return path, line


def fleet_lanes(fleet_root):
    """The sibling-lane set: `*-shokunin` dirs under fleet_root, minus kotoba."""
    lanes = set()
    for entry in fleet_root.iterdir():
        if not entry.is_dir():
            continue
        name = entry.name
        if not name.lower().endswith(LANE_SUFFIX):
            continue
        lane = name[: -len(LANE_SUFFIX)].lower()
        if lane == SELF_LANE:
            continue
        lanes.add(lane)
    return lanes


def git_show(repo, commit, path):
    """Run `git -C repo show commit:path`.  Returns (text, error_line)."""
    proc = subprocess.run(
        ["git", "-C", str(repo), "show", "%s:%s" % (commit, path)],
        stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if proc.returncode != 0:
        err = proc.stderr.decode("utf-8", "replace").strip().splitlines()
        return None, (err[0] if err else "git show failed")
    return proc.stdout.decode("utf-8", "replace"), None


def is_heading_line(line):
    return line.strip().startswith("#")


def locate_quote(lines, line_no, quote_collapsed):
    """Find the quote at `line_no` or within +/-2 lines.

    Returns (found, matched_index, is_heading).  A quote that spans several
    physical lines (a folded YAML description, say) is matched against the
    collapsed window text; the matched line is then the first window line that
    carries the quote's first word.
    """
    if not quote_collapsed:
        return False, None, False
    exact = line_no - 1
    candidates = [exact]
    for offset in (1, -1, 2, -2):
        candidates.append(exact + offset)
    seen = set()
    for index in candidates:
        if index in seen:
            continue
        seen.add(index)
        if not (0 <= index < len(lines)):
            continue
        if quote_collapsed in collapse(lines[index]):
            return True, index, is_heading_line(lines[index])
    # Multi-line quote: the +/-2 window joined and collapsed.
    low = max(0, exact - LINE_TOLERANCE)
    high = min(len(lines), exact + LINE_TOLERANCE + 1)
    window = list(range(low, high))
    joined = collapse(" ".join(lines[i] for i in window))
    if quote_collapsed in joined:
        first_word = quote_collapsed.split(" ")[0]
        for index in window:
            if first_word and first_word in collapse(lines[index]):
                return True, index, is_heading_line(lines[index])
        return True, window[0], is_heading_line(lines[window[0]])
    return False, None, False


# --------------------------------------------------------------------------
# the census check
# --------------------------------------------------------------------------


# ---------------------------------------------------------------------------
# Round-49 falsify correction (seat CriticC1Landed): the guard re-derives the
# two mechanical columns and the sibling-side half of the `none` rule from the
# pinned bytes, so a census and PROVINCE pair flipped consistently no longer
# passes on agreement alone.
# ---------------------------------------------------------------------------
MIN_QUOTE_WORDS = 6
NO_SKILL = "no skill.md"


def description_of(skill_text):
    """The frontmatter `description` value, whitespace-collapsed; '' if none.

    Round-50 fix (critic seat CriticC1Sizing, mutant m8): the value ends at
    ANY column-0 line, not only at a column-0 line that carries a colon.  A
    YAML comment is a column-0 line without a colon, so the old lookahead
    swallowed `# chousa kama kotodama tameshi` into the description value and
    the guard counted lanes that a real YAML parse leaves out of the value.
    Block-scalar content is indented, so it never starts at column 0, and the
    value still ends where the frontmatter ends.

    The block-scalar indicator (`>`, `|`, with optional chomping) is dropped:
    it is YAML syntax, not description text.
    """
    if skill_text is None or not skill_text.startswith("---"):
        return ""
    front = skill_text.split("\n---", 1)[0]
    match = re.search(r"^description:(.*?)(?=^\S|\Z)", front, re.S | re.M)
    if not match:
        return ""
    return BLOCK_SCALAR.sub("", collapse(match.group(1))).strip()


def token_in(name, text):
    return re.search(r"(?<![a-z0-9-])" + re.escape(name) + r"(?![a-z0-9])",
                     text, re.I) is not None


# ---------------------------------------------------------------------------
# Round-50, G1 (clause binding) and G4 (length cap), from the round-50 critic
# seat (`.ufo/waves/round-50/build/CriticC1Sizing.md`).  A bare list of lane
# names is not arbitration, so a lane counts as named only when the clause it
# sits in also states who owns what.  The marker list is pinned here,
# deliberately small, and the rule is a lexical approximation -- it is named
# as such in every failure message that uses it.
# ---------------------------------------------------------------------------

SKILL_DESCRIPTION_MIN = 1
SKILL_DESCRIPTION_MAX = 1024

# Ownership / routing markers.
#
# `NOT` is upper-case only: it is how the fleet writes a refusal ("NOT
# prompt/skill craft (kotoba-shokunin)"), while lower-case `not` occurs in
# ordinary prose ("not skill files", "not router-visible") and would bind
# every clause it appeared in -- including a negated mention such as "chousa
# is not the owner", which is the opposite of arbitration.
#
# The cross-reference markers ("see above") count as routing markers: they
# point at a split stated in an earlier clause, which is arbitration by
# reference.  They are the difference between a description that names a lane
# and one that routes to the lane that owns the ground.
OWNERSHIP_MARKERS = ("owns", "own", "owned", "route", "routes", "routing",
                      "NOT", "see above", "as above", "see also")
MARKER_DESCRIPTION = ("owns/own/owned/route/routes/routing/NOT/"
                      "see above/as above/see also")

# A clause ends at `;` or at a sentence end: a `.`, `!` or `?` followed by
# whitespace and a capital letter (or the end of the text).  A period inside
# a token (`SKILL.md`, `e.g.`) does not end a clause, and a period followed by
# a lower-case word is read as an abbreviation or a continuation, not a
# sentence end.
CLAUSE_SPLIT = re.compile(r";|(?<=[.!?])\s+(?=[A-Z])|(?<=[.!?])\s*$")


def split_clauses(description):
    """Split a description into clauses on `;` and sentence ends."""
    return [c.strip() for c in CLAUSE_SPLIT.split(description) if c.strip()]


def marker_in(clause):
    """Does this clause carry an ownership or routing marker?

    The markers are matched as whole words, so `route` does not match
    `router` and `own` does not match `owner`.  The upper-case `NOT` is
    matched case-sensitively; the rest case-insensitively.
    """
    for marker in OWNERSHIP_MARKERS:
        pattern = r"(?<![A-Za-z0-9-])" + re.escape(marker) + r"(?![A-Za-z0-9-])"
        flags = 0 if marker == "NOT" else re.I
        if re.search(pattern, clause, flags):
            return True
    return False


# ---------------------------------------------------------------------------
# Round-50 (routed defect D3): a duplicated row is a false census.  The
# lane-set check cannot see it -- a set collapses the duplicate -- and the
# row counter grows without a new lane, so the round-49 falsify finding saw a
# duplicated census row pass with `rows 21 verified 21`.  Both the census
# table and the PROVINCE.md `## Adjacent` table are checked.
# ---------------------------------------------------------------------------

def duplicate_lane_failures(rows, columns, subject):
    """Lanes named by more than one row of a lane table.

    `rows` is a list of (line_number, cells) pairs, `columns` the expected
    cell count and `subject` the table's name in the failure message.  Lane
    names are compared normalized (case-insensitive, `-shokunin` suffix
    dropped), so `Alpha` and `alpha` are the same lane.  Returns one failure
    string per duplicated lane.
    """
    seen = {}
    for index, (line_no, cells) in enumerate(rows, 1):
        if len(cells) != columns:
            continue
        lane = normalize_lane(cells[0])
        if not lane:
            continue
        seen.setdefault(lane, []).append((index, line_no))
    failures = []
    for lane in sorted(seen):
        entries = seen[lane]
        if len(entries) > 1:
            failures.append(
                "%s: lane %s appears in more than one row (rows %s): a "
                "duplicated row inflates the table without surveying a new "
                "lane" % (subject, lane,
                          ", ".join("%d (line %d)" % (i, n) for i, n in entries)))
    return failures


def skill_description_failures(skill_path, lane_classes):
    """Check the skill description against the census's non-`none` lanes.

    `lane_classes` maps a lane name to its census classification.  The
    description is the YAML frontmatter `description` of `skill_path`, read
    with the same `description_of` helper the sibling rows use.

    Two rules, both from the round-50 critic seat (`.ufo/waves/round-50/build/
    CriticC1Sizing.md`):

    G1 -- clause binding.  A bare list of lane names is not arbitration: the
    description is split into clauses and a lane counts as NAMED only when
    some clause that contains it also carries an ownership or routing marker
    from the pinned list below.  The marker rule is a lexical approximation,
    not a parse of intent; its counterexamples run in both directions (a
    clause with a marker but no lane is harmless, a lane named in a clause
    without a marker is refused even when the surrounding sentences do state
    a split).

    G4 -- length cap.  The parsed description must be 1 to 1024 characters
    (S018, `specification.md:101`).

    Lane names are compared whole-token and case-insensitively, and each
    census lane counts once, so a capitalised repeat is not a second lane.

    Returns a dict: named, total, length, failures.
    """
    try:
        text = skill_path.read_text(encoding="utf-8")
    except OSError as exc:
        raise UsageError("cannot read skill file %s: %s" % (skill_path, exc))
    except UnicodeDecodeError as exc:
        raise UsageError("skill file %s is not UTF-8: %s" % (skill_path, exc))
    description = description_of(text)
    length = len(description)
    clauses = split_clauses(description)
    non_none = sorted(lane for lane, cls in lane_classes.items()
                       if cls != "none")
    failures = []
    if length < SKILL_DESCRIPTION_MIN or length >= SKILL_DESCRIPTION_MAX:
        failures.append(
            "skill description length %d is outside %d-%d characters (S018: "
            "the description field must be 1-1024 characters)"
            % (length, SKILL_DESCRIPTION_MIN, SKILL_DESCRIPTION_MAX))
    named = 0
    for lane in non_none:
        in_clause = [c for c in clauses if token_in(lane, c)]
        if not in_clause:
            failures.append("skill description does not name the non-none "
                            "census lane %s" % lane)
            continue
        if not any(marker_in(c) for c in in_clause):
            failures.append(
                "skill description mentions the non-none census lane %s, but "
                "no clause that names it carries an ownership or routing "
                "marker (%s): naming a lane is not a split.  This marker "
                "rule is a lexical approximation, not a parse of intent"
                % (lane, MARKER_DESCRIPTION))
            continue
        named += 1
    return {"named": named, "total": len(non_none), "length": length,
            "failures": failures}


def mechanical_findings(repo, commit, values, lane, all_lanes, classification):
    """Problems with the skill-file, names-kotoba and arbitration cells, and the
    sibling-side `none` condition.  Returns a list of strings."""
    problems = []
    skill_text, _ = git_show(repo, commit, "SKILL.md")
    path_cell = values["path"].strip().lower()
    names_cell = values["names kotoba"].strip().lower()
    arb_cell = values["arbitration"].strip().lower()
    if skill_text is None:
        if path_cell != "none" or names_cell != NO_SKILL or arb_cell != NO_SKILL:
            problems.append("no SKILL.md at the pin, but the row's skill/names/"
                            "arbitration cells read %r/%r/%r (expected NONE/no "
                            "SKILL.md/no SKILL.md)" % (values["path"],
                                                        values["names kotoba"],
                                                        values["arbitration"]))
        description = ""
    else:
        if path_cell == "none":
            problems.append("SKILL.md exists at the pin but the skill cell says NONE")
        description = description_of(skill_text)
        want_names = "yes" if token_in(SELF_LANE, description) else "no"
        if names_cell != want_names:
            problems.append("names-kotoba cell %r but the pinned description gives %r"
                            % (values["names kotoba"], want_names))
        named = sorted(n for n in all_lanes if n != lane and token_in(n, description))
        want_arb = ("yes: " + ", ".join(named)) if named else "no"
        if arb_cell != want_arb:
            problems.append("arbitration cell %r but the pinned description gives %r"
                            % (values["arbitration"], want_arb))
    if classification == "none":
        province_text, _ = git_show(repo, commit, "PROVINCE.md")
        if token_in(SELF_LANE, description) or (
                province_text is not None and token_in(SELF_LANE, province_text)):
            problems.append("classified none, but the sibling's description or "
                            "PROVINCE.md at the pin names kotoba (the rule makes a "
                            "published split adjacent)")
    return problems

CENSUS_CELL_NAMES = ("lane", "branch", "commit", "path", "classification",
                      "names kotoba", "arbitration", "path:line", "quote")


def check_census(census_path, fleet_root, province_path=None):
    """Run every check.  Returns a result dict."""
    result = {"failures": [], "rows": 0, "verified": 0,
              "province_rows": 0, "province_matched": 0, "province_checked": False,
              "lane_classes": {}}
    failures = result["failures"]

    try:
        text = census_path.read_text(encoding="utf-8")
    except OSError as exc:
        raise UsageError("cannot read census file %s: %s" % (census_path, exc))
    except UnicodeDecodeError as exc:
        raise UsageError("census file %s is not UTF-8: %s" % (census_path, exc))

    blocks = parse_blocks(text.splitlines())
    table = select_census_table(blocks)
    if table is None:
        failures.append("census table not found: no %d-column markdown table with a "
                        "separator row in %s" % (CENSUS_COLUMNS, census_path))
        return result

    rows = table["rows"]
    result["rows"] = len(rows)
    if not rows:
        failures.append("census table is empty: 0 rows in %s (refusing an empty "
                        "census)" % census_path)
        return result

    # Round-50 (D3): a lane in more than one row is refused before any row is
    # verified, so the refusal does not depend on the row's other cells.
    for message in duplicate_lane_failures(rows, CENSUS_COLUMNS, "census table"):
        failures.append(message)

    # lane -> classification for every row whose lane and classification cells
    # parse.  The --skill check reads this map: a lane the census classes
    # non-`none` must be named in the skill description.  It is a separate
    # pass so a row that fails another check still contributes its class.
    lane_classes = {}
    for _index, (_line_no, cells) in enumerate(rows, 1):
        if len(cells) != CENSUS_COLUMNS:
            continue
        lane = normalize_lane(cells[0])
        classification = cells[4].strip().lower()
        if lane and classification in CLASSIFICATIONS:
            lane_classes[lane] = classification
    result["lane_classes"] = lane_classes

    expected = fleet_lanes(fleet_root)
    seen_lanes = set()
    # classification/commit of every row that parsed those two fields, whether
    # or not its quote verified -- the province cross-check needs the parsed
    # value, not the verified one, to name a mismatch.
    census_meta = {}

    for index, (line_no, cells) in enumerate(rows, 1):
        label = "row %d (census line %d)" % (index, line_no)
        if len(cells) != CENSUS_COLUMNS:
            failures.append("%s: expected %d cells, found %d"
                            % (label, CENSUS_COLUMNS, len(cells)))
            continue
        values = dict(zip(CENSUS_CELL_NAMES, cells))
        lane_raw = values["lane"]
        lane = normalize_lane(lane_raw)
        if lane:
            label = "%s (lane %s)" % (label, lane)
        else:
            failures.append("%s: empty lane cell" % label)
            continue

        # The lane counts as surveyed as soon as it is named: a row that fails
        # its quote check has still been surveyed, and the lane-set check must
        # not be satisfied by dropping the failing row.
        seen_lanes.add(lane)

        empty = [name for name in CENSUS_CELL_NAMES if not values[name].strip()]
        if empty:
            failures.append("%s: empty cell(s): %s" % (label, ", ".join(empty)))
            continue

        commit = values["commit"].strip()
        if not HEX40.match(commit):
            failures.append("%s: commit %r is not a 40-hex object id" % (label, commit))
            continue

        classification = values["classification"].strip().lower()
        if classification not in CLASSIFICATIONS:
            failures.append("%s: classification %r is not one of %s"
                            % (label, values["classification"],
                               "/".join(CLASSIFICATIONS)))
            continue

        census_meta[lane] = {"classification": classification, "commit": commit.lower(),
                             "label": label}

        try:
            path, line_no_cited = split_path_line(values["path:line"])
        except ValueError as exc:
            failures.append("%s: malformed path:line %r (%s)"
                            % (label, values["path:line"], exc))
            continue

        # The `path` cell names the sibling's skill file(s); the `path:line`
        # cell names where THIS quote was located, which may be a different
        # file (a sibling's PROVINCE.md, say).  The two are independent, so
        # only the path:line path drives the git show.

        quote = strip_wrapping(values["quote"])
        if not quote:
            failures.append("%s: empty quote cell" % label)
            continue
        quote_collapsed = collapse(quote)

        repo = repo_dir_for(lane_raw, fleet_root)
        if not repo.is_dir():
            failures.append("%s: no sibling repo at %s" % (label, repo))
            continue
        content, error = git_show(repo, commit, path)
        if content is None:
            failures.append("%s: git show %s:%s in %s failed (%s)"
                            % (label, commit[:12], path, repo, error))
            continue
        lines = content.splitlines()
        found, matched, heading = locate_quote(lines, line_no_cited, quote_collapsed)
        if not found:
            failures.append("%s: quote not found at %s:%d (+/-%d lines)"
                            % (label, path, line_no_cited, LINE_TOLERANCE))
            continue
        if heading:
            failures.append("%s: quote sits on a markdown heading (%s:%d): a "
                            "title-only quote is not a scope statement"
                            % (label, path, matched + 1))
            continue

        if len(quote_collapsed.split()) < MIN_QUOTE_WORDS:
            failures.append("%s: quote has fewer than %d words: too short to "
                            "state a scope" % (label, MIN_QUOTE_WORDS))
            continue

        problems = mechanical_findings(repo, commit, values, lane,
                                       expected | {SELF_LANE}, classification)
        if problems:
            for problem in problems:
                failures.append("%s: %s" % (label, problem))
            continue

        result["verified"] += 1

    missing = sorted(expected - seen_lanes)
    extra = sorted(seen_lanes - expected)
    if missing:
        failures.append("lane set: %d sibling lane(s) never surveyed: %s"
                        % (len(missing), ", ".join(missing)))
    if extra:
        failures.append("lane set: %d lane(s) not in the fleet: %s"
                        % (len(extra), ", ".join(extra)))

    if province_path is not None:
        result["province_checked"] = True
        _check_province(province_path, census_meta, seen_lanes, expected, result)

    return result


def extract_adjacent_section(text):
    """The `## Adjacent` section of PROVINCE.md, ending at the next `## ` heading."""
    lines = text.splitlines()
    start = None
    for number, line in enumerate(lines, 1):
        if re.match(r"\A##\s+Adjacent\s*\Z", line):
            start = number
            break
    if start is None:
        return None
    body = []
    for line in lines[start:]:
        if re.match(r"\A##\s+\S", line):
            break
        body.append(line)
    return body


def _check_province(province_path, census_meta, census_lanes, expected, result):
    """Cross-check PROVINCE.md's `## Adjacent` table against the census.

    The province table's lane set must equal the census lane set exactly, and
    each row's classification and commit must equal the census row's.
    """
    failures = result["failures"]
    try:
        text = province_path.read_text(encoding="utf-8")
    except OSError as exc:
        raise UsageError("cannot read province file %s: %s" % (province_path, exc))
    except UnicodeDecodeError as exc:
        raise UsageError("province file %s is not UTF-8: %s" % (province_path, exc))

    body = extract_adjacent_section(text)
    if body is None:
        failures.append("province: no `## Adjacent` section in %s" % province_path)
        return
    table = select_province_table(parse_blocks(body))
    if table is None:
        failures.append("province: the `## Adjacent` section of %s holds no lane "
                        "table (`| lane | classification | commit | ... |`); a "
                        "bare-name list is not a table" % province_path)
        return

    rows = table["rows"]
    result["province_rows"] = len(rows)
    if not rows:
        failures.append("province: the `## Adjacent` table is empty")
        return

    # Round-50 (D3): the same duplicate-lane refusal as for the census table.
    # The province table's lane set is a set too, so a duplicated row passes
    # every other check (the row count only has a floor, not a ceiling).
    for message in duplicate_lane_failures(rows, PROVINCE_COLUMNS,
                                           "province `## Adjacent` table"):
        failures.append(message)

    province_lanes = set()
    for index, (line_no, cells) in enumerate(rows, 1):
        label = "province row %d (line %d)" % (index, line_no)
        if len(cells) != PROVINCE_COLUMNS:
            failures.append("%s: expected %d cells, found %d"
                            % (label, PROVINCE_COLUMNS, len(cells)))
            continue
        lane = normalize_lane(cells[0])
        if not lane:
            failures.append("%s: empty lane cell" % label)
            continue
        province_lanes.add(lane)
        if lane not in census_lanes:
            failures.append("%s: lane %s is in PROVINCE.md but not in the census"
                            % (label, lane))
            continue
        entry = census_meta.get(lane)
        if entry is None:
            # The census row for this lane did not parse its classification and
            # commit; the census check already named that row.
            failures.append("%s: lane %s has no parsed census row to compare with"
                            % (label, lane))
            continue
        if cells[1].strip().lower() != entry["classification"]:
            failures.append("%s: lane %s classification %r does not match the "
                            "census %r"
                            % (label, lane, cells[1].strip(),
                               entry["classification"]))
            continue
        if cells[2].strip().lower() != entry["commit"]:
            failures.append("%s: lane %s commit %s does not match the census %s"
                            % (label, lane, cells[2].strip()[:12],
                               entry["commit"][:12]))
            continue
        result["province_matched"] += 1

    for lane in sorted(census_lanes - province_lanes):
        failures.append("province: lane %s is in the census but not in the "
                        "`## Adjacent` table" % lane)
    if len(rows) < len(expected):
        failures.append("province: the `## Adjacent` table has %d row(s), fewer "
                        "than the %d sibling lane(s)" % (len(rows), len(expected)))


# --------------------------------------------------------------------------
# CLI
# --------------------------------------------------------------------------

class UsageError(Exception):
    """Raised for anything the caller got wrong (exit 2)."""


def build_parser():
    parser = argparse.ArgumentParser(
        description="Re-read every round-49 sibling-overlap census row at its "
                    "pinned commit and fail on empty or false content.")
    parser.add_argument("census", nargs="?",
                        help="the census markdown file to check")
    parser.add_argument("--fleet", default=DEFAULT_FLEET, metavar="DIR",
                        help="fleet root holding the `*-shokunin` sibling repos "
                             "(default: %s)" % DEFAULT_FLEET)
    parser.add_argument("--province", metavar="PATH",
                        help="PROVINCE.md whose `## Adjacent` table is cross-checked "
                             "against the census")
    parser.add_argument("--skill", metavar="PATH",
                        help="SKILL.md whose frontmatter description must name "
                             "every census lane classified non-`none`")
    parser.add_argument("--self-test", action="store_true",
                        help="assert the red arms of the content guard on temporary "
                             "fixtures and exit")
    return parser


def main(argv=None):
    parser = build_parser()
    args = parser.parse_args(argv)

    if args.self_test:
        return self_test()

    if not args.census:
        print("usage: %s CENSUS.md [--fleet DIR] [--province PROVINCE.md] "
              "[--skill SKILL.md]" % Path(sys.argv[0]).name, file=sys.stderr)
        return 2

    fleet_root = Path(args.fleet).expanduser()
    if not fleet_root.is_dir():
        print("ERROR fleet root %s is not a directory" % fleet_root, file=sys.stderr)
        return 2
    census_path = Path(args.census).expanduser()
    if not census_path.is_file():
        print("ERROR census file %s does not exist" % census_path, file=sys.stderr)
        return 2
    province_path = None
    if args.province:
        province_path = Path(args.province).expanduser()
        if not province_path.is_file():
            print("ERROR province file %s does not exist" % province_path,
                  file=sys.stderr)
            return 2
    skill_path = None
    if args.skill:
        skill_path = Path(args.skill).expanduser()
        if not skill_path.is_file():
            print("ERROR skill file %s does not exist" % skill_path,
                  file=sys.stderr)
            return 2

    try:
        result = check_census(census_path, fleet_root, province_path)
    except UsageError as exc:
        print("ERROR %s" % exc, file=sys.stderr)
        return 2

    if skill_path is not None:
        try:
            skill = skill_description_failures(skill_path, result["lane_classes"])
        except UsageError as exc:
            print("ERROR %s" % exc, file=sys.stderr)
            return 2
        result["failures"].extend(skill["failures"])
        result["skill"] = skill

    for failure in result["failures"]:
        print("FAIL %s" % failure)
    print("rows %d verified %d" % (result["rows"], result["verified"]))
    if result["province_checked"]:
        print("province rows %d matched %d"
              % (result["province_rows"], result["province_matched"]))
    if skill_path is not None:
        print("skill description names %d of %d non-none lanes"
              % (result["skill"]["named"], result["skill"]["total"]))
        print("skill description length %d of %d"
              % (result["skill"]["length"], SKILL_DESCRIPTION_MAX))
    return 1 if result["failures"] else 0


# --------------------------------------------------------------------------
# self-test
# --------------------------------------------------------------------------

def _git(repo, *args):
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


def _make_repo(root, name, files):
    repo = root / name
    repo.mkdir(parents=True)
    _git(repo, "init", "-q", "-b", "main")
    _git(repo, "config", "user.name", "kotoba self-test")
    _git(repo, "config", "user.email", "self-test@example.invalid")
    _git(repo, "config", "commit.gpgsign", "false")
    for rel, body in files.items():
        target = repo / rel
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(body, encoding="utf-8")
    _git(repo, "add", "-A")
    _git(repo, "commit", "-q", "-m", "fixture")
    commit = _git(repo, "rev-parse", "HEAD").strip()
    return repo, commit


CENSUS_HEADER = ("| lane | branch | commit | path | classification | names kotoba "
                 "| arbitration | path:line | quote |")
CENSUS_SEPARATOR = "|---|---|---|---|---|---|---|---|---|"


def _census_md(rows):
    out = ["# sibling-overlap census (fixture)", "", CENSUS_HEADER, CENSUS_SEPARATOR]
    for row in rows:
        out.append("| " + " | ".join(row) + " |")
    return "\n".join(out) + "\n"


def _province_md(rows, bare_names=False):
    out = ["# PROVINCE (fixture)", "", "## Other section", "", "not the table.", "",
           "## Adjacent", ""]
    if bare_names:
        out += ["- alpha — some scope", "- beta — some scope", ""]
    else:
        out += ["| lane | classification | commit | note |",
                "|---|---|---|---|"]
        for row in rows:
            out.append("| " + " | ".join(row) + " |")
        out.append("")
    out += ["## After", "", "text.", ""]
    return "\n".join(out)


ALPHA_SKILL = ("# alpha lane\n"
               "\n"
               "Alpha owns the alpha surface only; nothing else.\n"
               "unrelated line\n")
ALPHA_SKILL_HEADING = ("# alpha lane\n"
                       "\n"
                       "# Alpha owns the alpha surface only\n"
                       "unrelated line\n")
ALPHA_QUOTE = "Alpha owns the alpha surface only; nothing else."

# Round-50 fixtures.  A SKILL.md whose frontmatter description names the
# lanes of the throwaway census below, so the `--skill` arm can be exercised
# without the real fleet.
SKILL_HEAD = ("---\n"
              "name: kotoba-shokunin\n"
              "description: >\n"
              "  ")
SKILL_TAIL = ("---\n"
              "\n"
              "# kotoba\n")


def _skill_md(description_body):
    """A SKILL.md fixture whose frontmatter description is `description_body`."""
    return SKILL_HEAD + description_body + "\n" + SKILL_TAIL


# The nine lanes the round-49 census classes non-`none`, in the order the
# census lists them.  The `--skill` arms use them so the reported counts read
# the same way the live run does.
SKILL_LANES = ("chousa", "kagi", "kake", "kama", "kasegi", "kengaku",
               "kotodama", "kumitate", "tameshi")

# A description that routes five of the nine: the same shape as the
# base SKILL.md, whose sibling clause names kagi, kake, kasegi, kengaku and
# kumitate and says who owns what.
SKILL_DESC_FIVE = (
    "Prompt and skill craft. Sibling boundary: the five sibling lanes kagi, "
    "kake, kasegi, kengaku and kumitate own their own SKILL.md content; this "
    "skill audits and reports; fixes route to the owning lane.")

# The same description with the four missing lanes routed too.
SKILL_DESC_ALL = (
    "Prompt and skill craft. Sibling boundary: chousa owns the deep-research "
    "method, kagi owns secrets and vault ops, kake owns web properties, kama "
    "owns local model serving, kasegi owns bounty and security research, "
    "kengaku owns model evaluation, kotodama owns worldbuilding and naming, "
    "kumitate owns orchestration and dispatch runtime, and tameshi owns "
    "verification fixtures and mutation testing; this skill audits and "
    "reports; fixes route to the owning lane.")

# The five routed lanes plus the four that are missing, written the way the
# round-50 critic's m7 writes them: two capitalised repeats of lanes already
# named and two new names in a clause that cross-references the split above.
SKILL_DESC_SEVEN = (
    SKILL_DESC_FIVE + " Kagi, Kake: see above. kotodama, tameshi.")

# A bare list of the four missing lanes (critic m1): names, no arbitration.
SKILL_DESC_BARE = (
    SKILL_DESC_FIVE + " Sibling lanes: chousa kama kotodama tameshi.")

# The same four lanes negated (critic m5).
SKILL_DESC_NEGATED = (
    SKILL_DESC_FIVE + " Never mention chousa, kama, kotodama or tameshi.")


def self_test():
    failures = []
    total = 0

    def rec(what, ok, got=None):
        nonlocal total
        total += 1
        if not ok:
            failures.append("%s: got %r" % (what, got))

    with tempfile.TemporaryDirectory(prefix="census-selftest-") as tmp:
        tmp = Path(tmp)

        def make_fleet(name, lanes, files=None):
            """A throwaway fleet root holding exactly `lanes` sibling repos.

            kotoba is always present too: it must be excluded from the
            sibling-lane set, and the fixture proves it.
            """
            root = tmp / name
            root.mkdir()
            commits = {}
            for lane in lanes:
                body = (files or {}).get(lane, {"SKILL.md": ALPHA_SKILL})
                _, commit = _make_repo(root, lane + LANE_SUFFIX, body)
                commits[lane] = commit
            _make_repo(root, SELF_LANE + LANE_SUFFIX, {"SKILL.md": "kotoba\n"})
            return root, commits

        def row_for(lane, commit, classification="adjacent", quote=ALPHA_QUOTE,
                    path="SKILL.md", line=3, names="no", arbitration="no"):
            return [lane, "main", commit, path, classification, names, arbitration,
                    "%s:%d" % (path, line), quote]

        census = tmp / "census.md"
        province = tmp / "PROVINCE.md"

        def run(rows, fleet_root, province_rows=None, bare=False, census_text=None):
            census.write_text(census_text if census_text is not None else _census_md(rows),
                              encoding="utf-8")
            prov = None
            if province_rows is not None:
                province.write_text(_province_md(province_rows, bare_names=bare),
                                    encoding="utf-8")
                prov = province
            return check_census(census, fleet_root, prov)

        # -- arm 1: a correct row passes ---------------------------------
        fleet_a, commits_a = make_fleet("fleet-a", ["alpha"])
        alpha_row = row_for("alpha", commits_a["alpha"])
        res = run([alpha_row], fleet_a)
        rec("correct row: no failures", res["failures"] == [], res["failures"])
        rec("correct row: rows 1 verified 1",
            (res["rows"], res["verified"]) == (1, 1), (res["rows"], res["verified"]))

        # -- arm 2: a quote wrapped in double quotes still verifies --------
        wrapped = list(alpha_row)
        wrapped[8] = '"%s"' % ALPHA_QUOTE
        res = run([wrapped], fleet_a)
        rec("double-quoted quote: no failures", res["failures"] == [], res["failures"])

        # -- arm 3: a quote wrapped in backticks still verifies -----------
        wrapped = list(alpha_row)
        wrapped[8] = "`%s`" % ALPHA_QUOTE
        res = run([wrapped], fleet_a)
        rec("backtick-wrapped quote: no failures", res["failures"] == [], res["failures"])

        # -- arm 4: a mutated quote fails ---------------------------------
        mutated = list(alpha_row)
        mutated[8] = "Alpha owns the alpha surface entirely; nothing else."
        res = run([mutated], fleet_a)
        rec("mutated quote: fails", bool(res["failures"]), res["failures"])
        rec("mutated quote: names the row and the quote",
            any("row 1" in f and "quote not found" in f for f in res["failures"]),
            res["failures"])
        rec("mutated quote: verified 0", res["verified"] == 0, res["verified"])

        # -- arm 5: a wrong commit fails ----------------------------------
        wrong = list(alpha_row)
        wrong[2] = "0" * 40
        res = run([wrong], fleet_a)
        rec("wrong commit: fails", bool(res["failures"]), res["failures"])
        rec("wrong commit: names git show",
            any("git show" in f for f in res["failures"]), res["failures"])

        # -- arm 6: a missing lane fails ----------------------------------
        fleet_b, commits_b = make_fleet("fleet-b", ["alpha", "beta"])
        res = run([row_for("alpha", commits_b["alpha"])], fleet_b)
        rec("missing lane: fails", bool(res["failures"]), res["failures"])
        rec("missing lane: names beta",
            any("never surveyed: beta" in f for f in res["failures"]),
            res["failures"])

        # -- arm 7: an empty table fails ----------------------------------
        res = run([], fleet_a, census_text=_census_md([]))
        rec("empty table: fails", bool(res["failures"]), res["failures"])
        rec("empty table: says empty", any("empty" in f for f in res["failures"]),
            res["failures"])
        rec("empty table: rows 0", res["rows"] == 0, res["rows"])

        # -- round-49 falsify arms: mechanical columns are re-derived --------
        fm_skill = ("---\nname: gamma\ndescription: Gamma craft. NOT prompt craft "
                    "(kotoba-shokunin), NOT alpha work.\n---\n\n"
                    "Gamma owns the gamma surface only; nothing else here.\n")
        fleet_g, commits_g = make_fleet("fleet-g", ["alpha", "gamma"],
                                        {"gamma": {"SKILL.md": fm_skill}})
        g_quote = "Gamma owns the gamma surface only; nothing else here."
        g_ok = row_for("gamma", commits_g["gamma"], quote=g_quote, line=6,
                       names="yes", arbitration="yes: alpha, kotoba")
        a_ok = row_for("alpha", commits_g["alpha"])
        res = run([a_ok, g_ok], fleet_g)
        rec("mechanical: correct cells pass", res["failures"] == [], res["failures"])
        flipped = list(g_ok)
        flipped[4] = "none"
        res = run([a_ok, flipped], fleet_g)
        rec("mechanical: none while the description names kotoba fails",
            any("classified none" in f for f in res["failures"]), res["failures"])
        wrong_names = list(g_ok)
        wrong_names[5] = "no"
        res = run([a_ok, wrong_names], fleet_g)
        rec("mechanical: wrong names-kotoba cell fails",
            any("names-kotoba cell" in f for f in res["failures"]), res["failures"])
        wrong_arb = list(g_ok)
        wrong_arb[6] = "no"
        res = run([a_ok, wrong_arb], fleet_g)
        rec("mechanical: wrong arbitration cell fails",
            any("arbitration cell" in f for f in res["failures"]), res["failures"])
        # The two-word quote is checked against fleet-a's own alpha commit.
        # (It used to reuse fleet-g's alpha commit, so the arm only passed when
        # two identical-content commits landed in the same wall-clock second
        # -- the fixture repos differ only by their commit timestamp.  The arm
        # flaked about once in thirty runs.)
        short = list(alpha_row)
        short[8] = "Alpha owns"
        res = run([short], fleet_a)
        rec("mechanical: a two-word quote fails",
            any("fewer than" in f for f in res["failures"]), res["failures"])

        # -- arm 8: an empty quote cell fails (empty needle, false content)
        empty_quote = list(alpha_row)
        empty_quote[8] = ""
        res = run([empty_quote], fleet_a)
        rec("empty quote cell: fails", bool(res["failures"]), res["failures"])
        rec("empty quote cell: names the empty cell",
            any("empty cell" in f for f in res["failures"]), res["failures"])

        # -- arm 9: a heading-line quote fails ----------------------------
        fleet_h, commits_h = make_fleet(
            "fleet-h", ["heading"], {"heading": {"SKILL.md": ALPHA_SKILL_HEADING}})
        heading_row = row_for("heading", commits_h["heading"], classification="none",
                              quote="# Alpha owns the alpha surface only")
        res = run([heading_row], fleet_h)
        rec("heading quote: fails", bool(res["failures"]), res["failures"])
        rec("heading quote: names the heading",
            any("heading" in f for f in res["failures"]), res["failures"])

        # -- arm 10: the province cross-check -----------------------------
        fleet_p, commits_p = make_fleet("fleet-p", ["alpha", "beta"])
        census_rows_p = [row_for("alpha", commits_p["alpha"]),
                         row_for("beta", commits_p["beta"], classification="none")]

        # matching table passes
        res = run(census_rows_p, fleet_p,
                  province_rows=[["alpha", "adjacent", commits_p["alpha"], "ok"],
                                 ["beta", "none", commits_p["beta"], "ok"]])
        rec("province matching table: no failures", res["failures"] == [],
            res["failures"])
        rec("province matching table: rows 2 matched 2",
            (res["province_rows"], res["province_matched"]) == (2, 2),
            (res["province_rows"], res["province_matched"]))

        # bare-name list fails
        res = run(census_rows_p, fleet_p,
                  province_rows=[["alpha", "adjacent", commits_p["alpha"], "ok"],
                                 ["beta", "none", commits_p["beta"], "ok"]],
                  bare=True)
        rec("province bare-name list: fails", bool(res["failures"]), res["failures"])
        rec("province bare-name list: names the missing table",
            any("no lane table" in f for f in res["failures"]), res["failures"])

        # classification mismatch fails
        res = run(census_rows_p, fleet_p,
                  province_rows=[["alpha", "contested", commits_p["alpha"], "ok"],
                                 ["beta", "none", commits_p["beta"], "ok"]])
        rec("province classification mismatch: fails", bool(res["failures"]),
            res["failures"])
        rec("province classification mismatch: names the lane",
            any("alpha" in f and "classification" in f for f in res["failures"]),
            res["failures"])

        # commit mismatch fails
        res = run(census_rows_p, fleet_p,
                  province_rows=[["alpha", "adjacent", "1" * 40, "ok"],
                                 ["beta", "none", commits_p["beta"], "ok"]])
        rec("province commit mismatch: fails", bool(res["failures"]),
            res["failures"])
        rec("province commit mismatch: names the lane",
            any("alpha" in f and "commit" in f for f in res["failures"]),
            res["failures"])

        # a lane in the province but not in the census fails
        res = run(census_rows_p, fleet_p,
                  province_rows=[["alpha", "adjacent", commits_p["alpha"], "ok"],
                                 ["beta", "none", commits_p["beta"], "ok"],
                                 ["gamma", "none", commits_p["beta"], "ok"]])
        rec("province extra lane: fails", bool(res["failures"]), res["failures"])
        rec("province extra lane: names gamma",
            any("gamma" in f for f in res["failures"]), res["failures"])

        # a lane in the census but not in the province fails
        res = run(census_rows_p, fleet_p,
                  province_rows=[["alpha", "adjacent", commits_p["alpha"], "ok"]])
        rec("province missing lane: fails", bool(res["failures"]), res["failures"])
        rec("province missing lane: names beta",
            any("beta" in f and "not in the" in f for f in res["failures"]),
            res["failures"])

        # fewer province rows than sibling lanes fails
        fleet_t, commits_t = make_fleet("fleet-t", ["alpha", "beta", "gamma"])
        census_rows_t = [row_for("alpha", commits_t["alpha"]),
                         row_for("beta", commits_t["beta"]),
                         row_for("gamma", commits_t["gamma"])]
        res = run(census_rows_t, fleet_t,
                  province_rows=[["alpha", "adjacent", commits_t["alpha"], "ok"],
                                 ["beta", "adjacent", commits_t["beta"], "ok"]])
        rec("province too few rows: fails", bool(res["failures"]), res["failures"])
        rec("province too few rows: names the shortfall",
            any("fewer than the 3 sibling lane(s)" in f for f in res["failures"]),
            res["failures"])

        # -- arm 12: a duplicated row is refused (round-50, D3) ------------
        # The census table: the same lane in two rows.  The lane-set check
        # cannot see it -- a set collapses the duplicate -- so the row count
        # grows without a new lane.
        fleet_d, commits_d = make_fleet("fleet-d", ["alpha", "beta"])
        dup_rows = [row_for("alpha", commits_d["alpha"]),
                    row_for("alpha", commits_d["alpha"]),
                    row_for("beta", commits_d["beta"])]
        res = run(dup_rows, fleet_d)
        rec("census duplicate row: fails", bool(res["failures"]), res["failures"])
        rec("census duplicate row: names the lane and the rows",
            any("lane alpha" in f and "more than one row" in f
                for f in res["failures"]), res["failures"])

        # A case-variant duplicate is the same lane.
        dup_case = [row_for("alpha", commits_d["alpha"]),
                    row_for("Alpha", commits_d["alpha"]),
                    row_for("beta", commits_d["beta"])]
        res = run(dup_case, fleet_d)
        rec("census case-variant duplicate row: fails",
            any("lane alpha" in f and "more than one row" in f
                for f in res["failures"]), res["failures"])

        # The PROVINCE.md `## Adjacent` table: the same refusal.
        res = run([row_for("alpha", commits_d["alpha"]),
                   row_for("beta", commits_d["beta"], classification="none")],
                  fleet_d,
                  province_rows=[["alpha", "adjacent", commits_d["alpha"], "ok"],
                                 ["alpha", "adjacent", commits_d["alpha"], "ok"],
                                 ["beta", "none", commits_d["beta"], "ok"]])
        rec("province duplicate row: fails", bool(res["failures"]),
            res["failures"])
        rec("province duplicate row: names the lane and the rows",
            any("lane alpha" in f and "more than one row" in f
                for f in res["failures"]), res["failures"])

        # A consistent duplicate pair in both tables still fails.
        res = run(dup_rows, fleet_d,
                  province_rows=[["alpha", "adjacent", commits_d["alpha"], "ok"],
                                 ["alpha", "adjacent", commits_d["alpha"], "ok"],
                                 ["beta", "adjacent", commits_d["beta"], "ok"]])
        rec("consistent duplicate rows: fail in both tables",
            sum(1 for f in res["failures"] if "more than one row" in f) == 2,
            res["failures"])

        # -- arm 13: the --skill description guard (round-50, C1) ---------
        # The census lanes the check reads are the non-`none` ones.
        nine = {lane: "adjacent" for lane in SKILL_LANES}
        nine["kotoba"] = "none"

        def skill_check(body, lanes=None):
            path = tmp / "SKILL-fixture.md"
            path.write_text(_skill_md(body), encoding="utf-8")
            return skill_description_failures(path, nine if lanes is None else lanes)

        # A description that routes every non-none lane passes.
        res = skill_check(SKILL_DESC_ALL)
        rec("skill: a routed description names every non-none lane",
            res["failures"] == [] and res["named"] == 9 and res["total"] == 9,
            (res["named"], res["total"], res["failures"]))

        # The base description routes five of the nine; the four it misses
        # are named in the failures.
        res = skill_check(SKILL_DESC_FIVE)
        rec("skill: the base-shaped description names five of nine",
            res["named"] == 5 and res["total"] == 9,
            (res["named"], res["total"]))
        rec("skill: the missing lanes are named in the failures",
            all(lane in " ".join(res["failures"])
                for lane in ("chousa", "kama", "kotodama", "tameshi"))
            and len(res["failures"]) == 4, res["failures"])

        # m7: capitalised repeats of lanes already named are not new lanes,
        # and the two new names are bound by the cross-reference.
        res = skill_check(SKILL_DESC_SEVEN)
        rec("skill m7: seven of nine (case-folded, no double count)",
            res["named"] == 7 and res["total"] == 9,
            (res["named"], res["total"]))
        rec("skill m7: the two unbound lanes are named",
            all(lane in " ".join(res["failures"]) for lane in ("chousa", "kama"))
            and len(res["failures"]) == 2, res["failures"])

        # m1: a bare list of names is not arbitration.
        res = skill_check(SKILL_DESC_BARE)
        rec("skill m1: a bare list does not bind the lanes",
            res["named"] == 5 and len(res["failures"]) == 4,
            (res["named"], res["failures"]))
        rec("skill m1: the bare-list lanes are named in the failures",
            all(lane in " ".join(res["failures"])
                for lane in ("chousa", "kama", "kotodama", "tameshi")),
            res["failures"])

        # m5: a negated mention is not arbitration either.
        res = skill_check(SKILL_DESC_NEGATED)
        rec("skill m5: a negated mention does not bind the lanes",
            res["named"] == 5 and len(res["failures"]) == 4,
            (res["named"], res["failures"]))

        # G4: the length cap.
        res = skill_check(SKILL_DESC_ALL + " " + ("padding " * 200))
        rec("skill: an over-length description fails",
            any("1024" in f for f in res["failures"]), res["failures"])
        rec("skill: an over-length description is over the cap",
            res["length"] > 1024, res["length"])

        # G4: an empty description is under the floor.
        res = skill_check("")
        rec("skill: an empty description fails",
            any("1-1024" in f for f in res["failures"]), res["failures"])

        # m8: a colon-free column-0 comment is not part of the description.
        comment_skill = ("---\n"
                          "name: kotoba-shokunin\n"
                          "description: >\n"
                          "  " + SKILL_DESC_FIVE + "\n"
                          "# chousa kama kotodama tameshi\n"
                          "---\n")
        parsed = description_of(comment_skill)
        rec("skill m8: a column-0 comment is not swallowed into the description",
            "chousa" not in parsed and parsed.startswith("Prompt"),
            parsed[:80])

        # The `--skill` arm at the CLI level: the census fixture's lanes drive
        # the check, and the exit code turns on a missing lane.
        fleet_s, commits_s = make_fleet("fleet-s", ["alpha", "beta"])
        skill_ok = tmp / "SKILL-ok.md"
        skill_ok.write_text(_skill_md(
            "Alpha owns the alpha surface; beta owns the beta surface."),
            encoding="utf-8")
        skill_missing = tmp / "SKILL-missing.md"
        skill_missing.write_text(_skill_md(
            "Alpha owns the alpha surface."), encoding="utf-8")

        def cli_skill(skill_path, fleet_root, rows):
            """Run main() with --skill and capture the output."""
            out, err = io.StringIO(), io.StringIO()
            with contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
                try:
                    code = main([str(census), "--fleet", str(fleet_root),
                                 "--skill", str(skill_path)])
                except SystemExit as exc:
                    code = exc.code
            return code, out.getvalue(), err.getvalue()

        census_rows_s = [row_for("alpha", commits_s["alpha"]),
                         row_for("beta", commits_s["beta"])]
        census.write_text(_census_md(census_rows_s), encoding="utf-8")
        code, out, err = cli_skill(skill_ok, fleet_s, census_rows_s)
        rec("cli --skill: a complete description exits 0", code == 0, (code, out))
        rec("cli --skill: the count line is printed",
            "skill description names 2 of 2 non-none lanes" in out, out)
        rec("cli --skill: the length line is printed",
            "skill description length" in out and "of 1024" in out, out)
        code, out, err = cli_skill(skill_missing, fleet_s, census_rows_s)
        rec("cli --skill: a missing lane exits 1", code == 1, (code, out))
        rec("cli --skill: the missing lane is named",
            "beta" in out, out)
        rec("cli --skill: the count line is printed on failure too",
            "skill description names 1 of 2 non-none lanes" in out, out)

        # -- arm 11: the CLI exit ladder ----------------------------------
        run([alpha_row], fleet_a)

        def cli(*argv):
            """Run main() with its output captured, so the self-test log stays
            the assertion log and nothing else."""
            out, err = io.StringIO(), io.StringIO()
            with contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
                code = main(list(argv))
            return code, out.getvalue(), err.getvalue()

        code, out, err = cli(str(census), "--fleet", str(fleet_a))
        rec("cli: correct census exits 0", code == 0, code)
        rec("cli: correct census prints the rows line",
            "rows 1 verified 1" in out, out)
        code, _, _ = cli(str(census), "--fleet", str(fleet_a),
                         "--province", str(tmp / "does-not-exist.md"))
        rec("cli: missing province file exits 2", code == 2, code)
        code, _, _ = cli(str(tmp / "does-not-exist.md"), "--fleet", str(fleet_a))
        rec("cli: missing census file exits 2", code == 2, code)
        code, _, _ = cli(str(census), "--fleet", str(tmp / "no-such-fleet"))
        rec("cli: missing fleet root exits 2", code == 2, code)
        code, _, _ = cli()
        rec("cli: no census argument exits 2", code == 2, code)
        code, out, err = cli(str(census), "--fleet", str(fleet_a))
        rec("cli: no traceback on stderr", "Traceback" not in err, err)

    if failures:
        for line in failures:
            print("FAIL %s" % line, file=sys.stderr)
    print("self-test: %d failure(s) over %d assertions" % (len(failures), total))
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
