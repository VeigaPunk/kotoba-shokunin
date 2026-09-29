#!/usr/bin/env python3
"""verify_skill_checklist.py — machine check for SKILL.md checklist-fidelity.

The claim under test: the prose checklist boxes in a SKILL.md file (the
``- [ ]`` items under the ``*checklist*`` sections) are *executed* by this
instrument, *delegated* to a named instrument, or recorded
``unexecuted:<reason>`` — and the disposition map
(``verifiers/checklist-baseline.json``, schema ``kotoba-checklist-v1``) covers
every live box exactly once, pinned by the sha256 of each box's normalised
text so that a reworded, added, or removed box FAILs the run.

Box extraction model.  A "box" is a line matching ``^\\s*-\\s+\\[[ xX]\\]``
plus its continuation lines: every following line that is indented deeper
than the box's own indent, is non-blank, and is neither a new box nor a
heading.  A box's *section* is the text of the nearest preceding ``#``-led
heading.

text_sha256 NORMALIZATION RULE (pinned by the schema; stated exactly for
independent re-derivation): take the box's first line minus the ``- [ ] ``
marker (everything after the ``]``), append each continuation line stripped
of surrounding whitespace, join all parts with a single ASCII space,
collapse every remaining whitespace run to one space, strip both ends,
encode UTF-8, sha256 hex.  The ``- [ ]`` marker is stripped; markdown
emphasis, backticks and a box's trailing ``(executed: ...)`` annotation are
part of the hashed text.  A re-wrapped box does NOT change the hash
(continuation lines are joined before hashing).  A map may pin the rule by
carrying ``"normalization"`` equal to NORMALIZATION_RULE; a differing value
is a map error (exit 3).

Map schema ``kotoba-checklist-v1``::

    {"schema":"kotoba-checklist-v1","file":"SKILL.md",
     "normalization":"<optional; must equal NORMALIZATION_RULE>",
     "boxes":[{"box_id":"trigger.01",
               "section":"Trigger-fidelity checklist",
               "text_sha256":"<64 hex>",
               "disposition":"executed:<check-id>"
                            |"delegated:<instrument-path>"
                            |"unexecuted:<reason>"}]}

Checks.  Every check prints ``evaluated N``; ``trigger.command_binary_
resolves`` additionally prints ``segments S``.  ``N == 0`` prints ``N/A``
with the reason and is never a PASS — except checks whose subject must
exist (frontmatter, name, description, line count, scanned lines, live
boxes), where ``N == 0`` stays a FAIL — and the command check, where
``segments S > 0`` with ``N == 0`` is a FAIL (a shell block whose every
segment fell through the skip lists is exactly where unresolvable binaries
hide).  A run whose executed checks together evaluate no subject exits 1.

checklist.box_map_complete      MULTISET parity between the live file's
    checklist boxes and the map's entries, matched on (section,
    text_sha256) with multiplicity — the same normalised text twice needs
    two map entries.  A live box with no map entry -> FAIL "unmapped box";
    a map entry with no live box -> FAIL "has no live box"; the map's
    ``file`` must equal the target's basename; ``box_id`` values must be
    unique; every ``executed:<id>`` must name a check in this file (an
    unknown id FAILs, it does not satisfy the executed floor).  Requires
    >=1 live box, >=1 map entry, >=1 valid ``executed:`` disposition.
    A ``delegated:<path>`` target must exist AND be an *instrument* — a file
    with a declared script suffix (``.py .sh .bash .mjs .js .ts .rb .pl``),
    a shebang, or the ELF magic (a compiled instrument has neither suffix nor
    shebang — the critic lane falsified a suffix-only test on
    ``~/.local/bin/sekhmet``): delegating a box to a README, a JSON map, a
    directory or a SKILL.md is a FAIL naming the target, not a pass
    (round-16 R2).
    ``evaluated`` = live box count.
trigger.frontmatter_parses      the file's frontmatter parses as a BLOCK:
    after optional blank lines/BOM, a ``---`` delimiter line, a closing
    ``---``/``...`` line, and inside, structural YAML --- ``key: value``
    lines at column 0, continuation lines only under a block scalar
    (``>``/``|``) or an open quoted scalar.  ``name:`` and
    ``description:`` must be present and non-empty after unquoting
    (``null``, ``~`` and empty scalars count as absent).  FAILs on gross
    malformation: unbalanced quotes, duplicate keys, tab-indented lines,
    stray non-key lines.  ``evaluated`` = 4 (the asserted requirements).
    Limit: a structural parse, not semantic YAML validation.
trigger.name_directory          the parsed frontmatter ``name`` (unquoted)
    equals ``basename(dirname(abspath(target)))`` — the directory the file
    was invoked through, so ``--skill SKILL.md`` from inside the skill dir
    and symlinked dir names compare correctly.  Body text (e.g. a fenced
    yaml block) never satisfies this: only parsed frontmatter is read.
trigger.literal_trigger_string  the ``description`` contains a double-,
    single-, curly-quoted or backticked span of >=2 characters, the literal
    token ``Triggers:``, or the frontmatter carries a non-empty
    ``triggers:``/``trigger:`` key.  Limit: a shape test, not semantics —
    quoted jargon like "deterministic" satisfies it.
trigger.anti_trigger_clause     the ``description``, after quoted and
    backticked spans are stripped (a user-quote containing "don't" is not
    the file's exclusion clause), matches >=1 marker of the OBSERVED
    bilingual exclusion vocabulary (Amendment A4): English
    ``anti-trigger``, ``anti trigger``, ``exclusion``, ``not for``,
    ``do not``, ``never``, ``without``, ``except``, ``n/a``,
    ``only when``, ``exclusively``; CJK ``反触发``, ``不用于``,
    ``不要用于``, ``排除``, ``勿用于``.  Limit (named in the detail line):
    a vacuous "Never use this skill." passes and a real exclusion with no
    marker fails — it is a vocabulary test, not semantics.
trigger.line_budget             the box binds the threshold: the first
    integer in the checklist box whose text matches ``file … <int> …
    line(s)`` is the limit (the live box reads ``File ≤ 600 lines``); when
    no box states a bound, ``--max-lines`` (default 600) applies.  A box
    saying ~450 while the flag says 600 fails at 451 — the file's own text
    is the contract.  ``evaluated`` = counted lines.
trigger.no_placeholder          no word-bounded occurrence of ``TODO``,
    ``FIXME``, ``TBD`` or the phrase ``coming soon`` outside backticked
    spans, unless a word-bounded case-insensitive negation token (``no``,
    ``not``, ``never``, ``avoid``, ``without``) appears earlier on the same
    line (any distance — order matters: ``TODO: no longer needed`` is
    still a defect; ``knowledge TODO`` is still a defect because ``no`` in
    ``knowledge`` is not word-bounded).  ``evaluated`` = lines scanned.
trigger.command_binary_resolves commands named in the file resolve.
    Subjects come from two surfaces:

    (a) fenced code blocks whose info string (first whitespace token,
        lowercased) is in {"", bash, sh, shell, console} — ``text``,
        ``yaml``, ``python``, ``json`` fences are never commands (a tree
        drawing with ``├──``/``└──`` is not a binary).  Inside, ``\\``
        line-continuations are joined before segmenting, heredoc bodies
        and their delimiter lines are skipped, and lines are split into
        segments on ``&&``, ``||``, ``;``, ``|``.  Every segment in a
        shell-fenced block is checked: after leading ``VAR=value``
        assignments and any chain of wrapper prefixes (``sudo``, ``env``,
        ``command``, ``nohup``, ``time``, ``builtin``, ``xargs``) are
        consumed, and a ``sh -c``/``bash -c``/``zsh -c`` head unwraps one
        level to its script string — so ``sudo missing-bin`` CANNOT pass
        by hiding behind the wrapper.  A head left over that is a shell
        keyword/builtin, an assignment, a comment/shebang, or contains
        shell metacharacters (``$ ` < > ( ) { } [ ] * ? ~ = ! # & | ;
        ' "``) is skipped silently, not checked.  ``cd``/``pushd``/
        ``popd`` segments are subjects themselves (their target must
        resolve) and update the relative-path resolution base for later
        segments.
    (b) single-backtick inline spans whose (unwrapped) head is in the
        DECLARED vocabulary ``verifiers/checklist-command-vocabulary.json``
        (``--vocabulary`` overrides) and that carry no ``<``/``>``
        placeholder.  The vocabulary is declared, not shape-guessed
        (Amendment A3: `` `description` `` and `` `ls` `` are
        indistinguishable by shape) — a command outside the set is
        invisible to the check; that is the named ceiling.

    Resolution: ``shutil.which``, an existing absolute path, or an
    existing path relative to the resolution base (initially the file's
    repo root: ``--repo``, else the nearest ancestor carrying ``.git``,
    else the target's directory).  A relative head containing ``..``
    segments never resolves against a base — it fails instead of becoming
    a path-escape oracle.  Round-16 R1: a *path-like argument* of a checked
    segment is a subject too — it ends in a known file suffix, or carries a
    slash and a dotted last segment, and is neither a flag, a ``VAR=value``
    assignment, nor a token carrying a shell metacharacter.  A token whose
    predecessor is a redirect operator or a declared output flag
    (``-o --out --output --write --dest --log --to --target -O``) is a
    *written* path and is skipped — but ``<`` is an *input* redirect, so its
    target is a subject (the sentinel lane's A/B: ``wc -l < corpus/dead.md``
    passed while ``cat corpus/dead.md`` failed on the same dead path); a ``#``
    token ends the scan (a trailing comment is prose); URLs and ``~``-anchored or absolute arguments are out
    of scope (host-dependent, the named ceiling); arguments are read from the
    list the head came from, so ``sh -c 'cat corpus/x.md'`` is checked *inside
    the script* rather than as one opaque string; a segment whose head is a
    skip-list builtin yields no argument subjects except for the builtins that
    act on their argument (``source``, ``.``, ``exec``) — pasting
    ``echo <word>`` succeeds, so it is not a defect.
    ``evaluated`` = subjects checked; ``segments``
    = segments examined.  ``N == 0``: ``N/A`` when no segments were seen,
    FAIL when segments were seen but produced no subjects.
trigger.citation_resolves       citations resolve from an implied base.
    Subjects: every whitespace-separated word of a backticked span (after
    dropping a ``#`` fragment) that starts with ``corpus/``, ``verifiers/``,
    ``opencode/``, ``.ufo/`` or a ``../`` hop — the class that means "this
    repo" — and carries no placeholder (``<`` ``>``), glob (``*`` ``?``),
    ``$VAR``, URL, ``~`` or leading ``-``.  Each must exist: a plain token
    resolves from the repo root; a token with leading ``..`` hops resolves
    against the repo's ancestors, bounded to 3 hops with no further ``..``
    inside (the fleet's lane-report convention, which the corpus verifier
    resolves the same way) — read-only, and the token is lane-authored.
    A single-segment directory name (``corpus/``, ``.ufo/``) is a class
    label, not a pointer, and is skipped; a deeper one (``.ufo/prompts/``)
    is checked.  ``evaluated`` = subject count; ``N == 0`` prints ``N/A``
    (a file may cite nothing), so the non-vacuity guard is the fixture
    assertion, not the live count.
governance.citation_resolves    the same existence predicate over repo-root
    ``LOG.md`` and ``SCORECARD.md`` when the target is that repo's
    ``SKILL.md``.  A token fully enclosed by double quotes on its own line is
    a historical/meta finding, not a live promise.  Tokens carrying an
    ellipsis or a literal ``round-N`` path segment are counted schematics and
    excluded.  Every other subject must resolve at HEAD.  ``evaluated`` =
    checked subjects after those two explicit exclusions; zero is a FAIL.


DOCUMENTED LIMITS (what this instrument proves and what it never proves):
  - parity is on (section, text_sha256) multisets: a box reworded *and*
    map-updated in the same commit is invisible; the map is the record of
    human judgement, the hash only forces the map to track the file;
  - ``executed:`` names a check id in this file; whether that check's rule
    captures the box's intent is the reviewer's call (pre-registration P6);
  - the frontmatter parse is structural, not semantic YAML validation;
  - anti-trigger is a vocabulary test over the OBSERVED bilingual marker
    set — an unlisted exclusion phrasing FAILs unearned, a marker-bearing
    non-exclusion (or a vacuous "Never use this skill.") passes unearned;
  - the command vocabulary is a ceiling, named not hidden: a command
    outside the declared set used *inline* is invisible; inside a
    shell-fenced block every segment head is checked, so wrappers,
    assignments and ``sh -c`` cannot hide a missing binary;
  - argument resolution (round-16 R1) covers path-like relative arguments
    only: an absolute or ``~``-anchored argument, an argument after a
    skip-list builtin (``echo corpus/nope.md``), a bare non-path token
    (``xargs r15absent``), and a path written under an output flag outside
    the declared set are all invisible.  ``echo <word>`` is *not* a defect:
    pasting it succeeds, so the M35 mutation row of the round-15 harness is
    re-labelled, not closed by a rule;
  - citation resolution (round-16 R3) is bounded by a closed root set
    (``corpus/``, ``verifiers/``, ``opencode/``, ``.ufo/``, ``../``): a dead
    ``docs/x.md`` escapes; a *named* base is out of scope by construction,
    which is also the mandated repair, so prefixing a base quiets the check
    and the box's first sentence is what forbids the bad prefix.  The check
    verifies existence, never that the cited content supports the claim;
  - governance citation resolution is a HEAD-navigability check, not proof of
    historical truth, ownership, content support, commit pins or line anchors.
    It runs only for repo-root ``LOG.md``/``SCORECARD.md`` with the repo's own
    ``SKILL.md`` as target.  Same-line double-quoted meta-findings and the two
    schematic forms (ellipsis, literal ``round-N``) are excluded and counted;
    cross-line quote parity never suppresses a subject; symlinks are
    existence-tested, not required to remain inside the repo;
  - delegation (round-16 R2) is instrument-ness by suffix or shebang: a
    ``.py`` data file and a shell script named ``x.txt`` are both
    misjudged, and the check never runs the delegated instrument;
  - round-16 R1's foreign-file hint rate is *measured*, not assumed: over 23
    fleet `SKILL.md` files the rule would FAIL 25 argument tokens of which 0
    are true defects (the measured classes: a produced path with no declared
    output flag, a deployed-tree path absent from the source repo, an example
    input in help text, a workdir-relative name) — which is why a foreign R1
    FAIL is a review prompt, never a verdict.  The tightening candidate is a
    declared read-verb vocabulary; the lane runs on this file, whose own file
    carries no fenced block, so none of those FAILs touch its gate;
  - on FOREIGN files, extraction FAILs are hints, not verdicts: the
    extractor cannot tell a Hyprland config block from a shell block, and
    a vocabulary hit in another project's prose is that project's
    judgement call — the lane routes those findings rather than fixing
    the files;
  - ``no_placeholder``'s same-line negation rule is a heuristic: a
    negation on the previous line, or a placeholder inside a backticked
    span, is not seen.

Exit: 0 all checks pass (with >=1 subject evaluated) | 1 any FAIL, or a
run in which the executed checks together produce no subject | 2 usage or
environment error (target file or vocabulary unreadable) | 3 THE BOX MAP
is missing, unparseable, or unbound to the target — a gate failure class,
not merely "environment unreadable": when the target is the repo's pinned
SKILL.md (or ``--map`` is given), an absent/bad map aborts the run with 3;
for a foreign ``--skill`` target with no map, ``box_map_complete`` reports
``N/A (no map pinned for <path>)`` instead.  ``--self-test`` is a separate
mode that exercises fixtures only; its rc (0/1) is not comparable to a
live run's exit codes.  Read-only; deterministic; stdlib only.
"""
from __future__ import annotations

import argparse
import contextlib
import hashlib
import io
import json
import os
import re
import shlex
import shutil
import sys
import tempfile
from collections import Counter
from pathlib import Path

DEFAULT_REPO = Path(__file__).resolve().parent.parent
VERIFIERS_DIR = Path(__file__).resolve().parent
FIXTURES = VERIFIERS_DIR / "fixtures" / "checklist"
BASELINE_NAME = "checklist-baseline.json"
VOCAB_NAME = "checklist-command-vocabulary.json"
MAP_SCHEMA = "kotoba-checklist-v1"
VOCAB_SCHEMA = "kotoba-command-vocab-v1"
DEFAULT_MAX_LINES = 600
NORMALIZATION_RULE = (
    "first line minus '- [ ]' marker + continuations stripped, joined with "
    "one space; whitespace runs collapsed to one space; stripped; UTF-8 "
    "sha256")

CHECK_IDS = (
    "checklist.box_map_complete",
    "trigger.frontmatter_parses",
    "trigger.name_directory",
    "trigger.literal_trigger_string",
    "trigger.anti_trigger_clause",
    "trigger.line_budget",
    "trigger.no_placeholder",
    "trigger.command_binary_resolves",
    "trigger.citation_resolves",
    "governance.citation_resolves",
)

BOX_RE = re.compile(r"^(\s*)-\s+\[([ xX])\]\s?(.*)$")
NEAR_MISS_RE = re.compile(r"^\s*-\s*\[[^\]]*\]?")
HEADING_RE = re.compile(r"^#{1,6}\s+(.+?)\s*$")
FENCE_RE = re.compile(r"^\s*(`{3,}|~{3,})([^`]*)$")
INLINE_SPAN_RE = re.compile(r"`([^`\n]+)`")
BACKTICK_SPAN_RE = re.compile(r"`[^`\n]*`")
FM_KEY_RE = re.compile(r"^([A-Za-z_][A-Za-z0-9_-]*)\s*:\s*(.*)$")

FENCED_INFO = frozenset(["", "bash", "sh", "shell", "console"])
WRAPPER_PREFIXES = frozenset(
    "sudo env command nohup time builtin xargs".split())
SH_C_SHELLS = frozenset("sh bash zsh dash".split())
ASSIGN_RE = re.compile(r"^[A-Za-z_][A-Za-z0-9_]*=")
SEGMENT_SPLIT_RE = re.compile(r"&&|\|\||[;|]")
SHA256_RE = re.compile(r"^[0-9a-f]{64}$")
DISPOSITION_RE = re.compile(r"^(executed|delegated|unexecuted):(.+)$")
HEREDOC_RE = re.compile(r"<<-?\s*['\"]?(~?[A-Za-z_][A-Za-z0-9_]*)['\"]?")

SHELL_SKIP = frozenset("""
if for while until case do done then else elif fi esac in
echo cd pwd export unset read local return exit printf set test
[ [[ { } ] ] ! function select shift trap eval exec source .
true false : wait ulimit umask type hash getopts let declare
typeset readonly break continue times dirs jobs fg bg
kill disown suspend logout enable alias unalias fc history
""".split())
SHELL_METACHARS = frozenset("$`<>(){}[]*?~=!#&|;'\"\\")
# builtins in SHELL_SKIP whose argument they *act on*: a missing path there is
# a real defect (pasting `source nope.sh` fails), unlike `echo`/`printf`
# arguments, which are display text.
READ_ARG_BUILTINS = frozenset(["source", ".", "exec"])
# round-16 R2: what may be a ``delegated:`` target — a runnable instrument,
# not merely an existing file.
INSTRUMENT_SUFFIXES = frozenset(
    [".py", ".sh", ".bash", ".mjs", ".js", ".ts", ".rb", ".pl"])
# round-16 R1: a fenced argument is path-like when it ends in a known file
# suffix, or carries a slash and a dotted last segment.
PATH_ARG_SUFFIXES = frozenset(
    [".md", ".py", ".json", ".sh", ".bash", ".mjs", ".js", ".ts", ".yml",
     ".yaml", ".txt", ".csv", ".log", ".html"])
# arguments in these positions are *written*, not read: a redirect target or
# the value of a declared output flag need not exist before the command runs.
REDIRECT_TOKENS = frozenset([">", ">>", "2>", "2>>", "&>", "&>>", "|&"])
OUTPUT_FLAGS = frozenset(["-o", "-O", "--out", "--output", "--write",
                          "--dest", "--log", "--to", "--target"])
# round-16 R3: a token whose implied base is this repo — it must resolve from
# the repo root.  A named base (``~``, ``/``, ``$VAR``) is out of scope.
CITATION_ROOTS = ("corpus/", "verifiers/", "opencode/", ".ufo/", "../")
GOVERNANCE_FILES = ("LOG.md", "SCORECARD.md")
SCHEMATIC_CITATION_RE = re.compile(r"(?:^|/)round-N(?:/|\.|$)")
EMPTY_SCALARS = frozenset(["", "~", "null", "Null", "NULL"])

PLACEHOLDER_RE = re.compile(r"\b(?:TODO|FIXME|TBD)\b|coming soon",
                            re.IGNORECASE)
NEGATION_RE = re.compile(r"\b(?:no|not|never|avoid|without)\b",
                         re.IGNORECASE)
ANTI_TRIGGER_RE = re.compile(
    r"\b(?:anti[- ]triggers?|exclusions?|not for|do not|never|without"
    r"|except|n/a|only when|exclusively)\b"
    r"|(?:不要用于|不用于|反触发|勿用于|排除)",
    re.IGNORECASE)
QUOTED_SPAN_RE = re.compile(
    r'"([^"\n]{2,})"|`([^`\n]{2,})`|\'([^\'\n]{2,})\''
    r"|[\u201c]([^\u201d\n]{2,})[\u201d]|[\u2018]([^\u2019\n]{2,})[\u2019]")
ALL_QUOTED_SPANS_RE = re.compile(
    r'"[^"\n]*"|\'[^\'\n]*\'|`[^`\n]*`'
    r"|[\u201c][^\u201d\n]*[\u201d]|[\u2018][^\u2019\n]*[\u2019]")
LINE_BOUND_BOX_RE = re.compile(
    r"file\b[^.\n]{0,40}?\d+[^.\n]{0,20}?lines?\b", re.IGNORECASE)
INT_RE = re.compile(r"\d+")


class EnvError(Exception):
    """Target file / vocabulary unreadable (exit 2)."""


class MapError(Exception):
    """Map missing or unparseable (exit 3)."""


# ---------------------------------------------------------------------------
# loaders
# ---------------------------------------------------------------------------

def read_text(path: Path, what: str) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except OSError as exc:
        raise EnvError("%s unreadable: %s (%s)" % (what, path, exc))


def find_repo_root(skill_path: Path) -> Path:
    """Nearest ancestor carrying a .git marker, else the file's directory."""
    cur = skill_path.resolve().parent
    for cand in (cur, *cur.parents):
        if (cand / ".git").exists():
            return cand
    return cur


def load_map(path: Path) -> dict:
    try:
        raw = path.read_text(encoding="utf-8")
    except OSError as exc:
        raise MapError("box map unreadable: %s (%s)" % (path, exc))
    try:
        data = json.loads(raw)
    except ValueError as exc:
        raise MapError("box map unparseable: %s (%s)" % (path, exc))
    if not isinstance(data, dict):
        raise MapError("box map %s: top level is not an object" % path)
    if data.get("schema") != MAP_SCHEMA:
        raise MapError("box map %s: schema must be %r, got %r"
                       % (path, MAP_SCHEMA, data.get("schema")))
    if "normalization" in data and data["normalization"] != NORMALIZATION_RULE:
        raise MapError("box map %s: \"normalization\" does not match the "
                       "pinned rule" % path)
    if not isinstance(data.get("file"), str) or not data["file"]:
        raise MapError("box map %s: \"file\" missing/empty" % path)
    boxes = data.get("boxes")
    if not isinstance(boxes, list):
        raise MapError("box map %s: \"boxes\" is not a list" % path)
    for i, b in enumerate(boxes):
        if not isinstance(b, dict):
            raise MapError("box map %s: boxes[%d] not an object" % (path, i))
        for key in ("box_id", "section", "text_sha256", "disposition"):
            if not isinstance(b.get(key), str) or not b[key]:
                raise MapError("box map %s: boxes[%d].%s missing/empty"
                               % (path, i, key))
        if not SHA256_RE.match(b["text_sha256"]):
            raise MapError("box map %s: boxes[%d].text_sha256 is not 64 hex"
                           % (path, i))
        m = DISPOSITION_RE.match(b["disposition"])
        if not m or not m.group(2).strip():
            raise MapError("box map %s: boxes[%d].disposition must be "
                           "executed:|delegated:|unexecuted:<non-empty>"
                           % (path, i))
    return data


def load_vocabulary(path: Path) -> frozenset[str]:
    try:
        raw = path.read_text(encoding="utf-8")
    except OSError as exc:
        raise EnvError("command vocabulary unreadable: %s (%s)" % (path, exc))
    try:
        data = json.loads(raw)
    except ValueError as exc:
        raise EnvError("command vocabulary unparseable: %s (%s)" % (path, exc))
    if not isinstance(data, dict) or data.get("schema") != VOCAB_SCHEMA:
        raise EnvError("command vocabulary %s: schema must be %r"
                       % (path, VOCAB_SCHEMA))
    commands = data.get("commands")
    if not isinstance(commands, list) or not commands or not all(
            isinstance(c, str) and c for c in commands):
        raise EnvError("command vocabulary %s: \"commands\" must be a "
                       "non-empty string list" % path)
    return frozenset(commands)


# ---------------------------------------------------------------------------
# extraction: frontmatter (structural), boxes, command subjects
# ---------------------------------------------------------------------------

def parse_frontmatter(lines: list[str]) -> tuple[dict | None, str]:
    """(fields, problem).  Structural block parse: blank lines / BOM before
    the opening ``---`` are tolerated; delimiters compare after .strip();
    inside, ``key: value`` at column 0 opens a field, and any indented line
    after an open field is folded into that field's value (YAML nesting such
    as ``metadata:`` / ``requires:`` / ``bins:`` blocks is legitimate and is
    what the file's own ``metadata.requires`` box prescribes — round-15 repair
    after lane R15Agree measured 37/138 fleet files rejected by the stricter
    column-0 rule); duplicate top-level keys, tab indents, an indented line
    with no open field, and unbalanced quotes are malformation.  Values are
    unquoted; ``null``/``~``/empty normalize to ''."""
    src = list(lines)
    if src and src[0].startswith("\ufeff"):
        src[0] = src[0].lstrip("\ufeff")
    i = 0
    while i < len(src) and not src[i].strip():
        i += 1
    if i >= len(src) or src[i].strip() != "---":
        return None, "no leading ---"
    close = None
    for j in range(i + 1, len(src)):
        if src[j].strip() in ("---", "..."):
            close = j
            break
    if close is None:
        return None, "no closing ---"
    fields: dict[str, str] = {}
    problems: list[str] = []
    cur = None
    cur_open = False  # continuation allowed: block scalar or open quote
    for line in src[i + 1:close]:
        if not line.strip():
            continue
        if line.startswith("\t"):
            problems.append("tab-indented frontmatter line %r"
                            % line.strip()[:40])
            continue
        if line.startswith(" "):
            if cur is None:
                problems.append("stray indented line %r" % line.strip()[:40])
                continue
            fields[cur] = (fields[cur] + " " + line.strip()).strip()
            if fields[cur].startswith(('"', "'")):
                q = fields[cur][0]
                cur_open = not (fields[cur].rstrip().endswith(q)
                                and len(fields[cur].rstrip()) > 1)
            continue
        m = FM_KEY_RE.match(line)
        if not m:
            problems.append("unparseable frontmatter line %r"
                            % line.strip()[:40])
            cur = None
            cur_open = False
            continue
        key, val = m.group(1), m.group(2).strip()
        if key in fields:
            problems.append("duplicate key %r" % key)
        fields[key] = val
        cur = key
        if val in (">", "|", ">-", "|-", ">+", "|+"):
            cur_open = True
            fields[key] = ""
        elif val.startswith(('"', "'")):
            q = val[0]
            cur_open = not (val.endswith(q) and len(val) > 1)
            if not cur_open:
                pass  # closed quoted scalar
            else:
                problems.append("unbalanced quote in scalar %r" % val[:40])
        else:
            cur_open = False
    if problems:
        return None, "; ".join(problems[:3])
    for k, v in list(fields.items()):
        v = v.strip()
        if len(v) >= 2 and v[0] in "\"'" and v[-1] == v[0]:
            v = v[1:-1]
        fields[k] = "" if v.strip() in EMPTY_SCALARS else v
    return fields, ""


def extract_boxes(lines: list[str]) -> tuple[list[dict], list[dict]]:
    """Live checklist boxes and near-miss markers: {section, line, text,
    sha256, marker}.  Section = nearest preceding heading text; a box before
    any heading gets section ''.   A ``- […]`` line inside a checklist that is
    not a ``- [ ]``/``- [x]`` box is recorded as a near miss (round-15
    closure of the critic's marker-state escape)."""
    boxes: list[dict] = []
    near_misses: list[dict] = []
    section = ""
    i = 0
    while i < len(lines):
        hm = HEADING_RE.match(lines[i])
        if hm:
            section = hm.group(1).strip()
            i += 1
            continue
        bm = BOX_RE.match(lines[i])
        if not bm:
            if NEAR_MISS_RE.match(lines[i]):
                near_misses.append({"section": section, "line": i + 1,
                                    "text": lines[i].strip()[:60]})
            i += 1
            continue
        indent = len(bm.group(1))
        parts = [bm.group(3)]
        j = i + 1
        while j < len(lines):
            line = lines[j]
            if HEADING_RE.match(line) or BOX_RE.match(line):
                break
            if not line.strip():
                break
            if len(line) - len(line.lstrip()) <= indent:
                break
            parts.append(line.strip())
            j += 1
        text = re.sub(r"\s+", " ", " ".join(p for p in parts if p)).strip()
        boxes.append({
            "section": section,
            "line": i + 1,
            "text": text,
            "marker": bm.group(2),
            "sha256": hashlib.sha256(text.encode("utf-8")).hexdigest(),
        })
        i = j
    return boxes, near_misses


def fenced_regions(lines: list[str]) -> tuple[set[int], list[list[tuple[int, str]]]]:
    """(all fenced line numbers, command-eligible blocks).
    A block is command-eligible when its info string (first whitespace
    token, lowercased) is in {'', bash, sh, shell, console}."""
    inside: set[int] = set()
    blocks: list[list[tuple[int, str]]] = []
    in_fence = False
    fence_char = ""
    shell = False
    cur: list[tuple[int, str]] = []
    for lineno, line in enumerate(lines, 1):
        fm = FENCE_RE.match(line)
        if fm:
            if not in_fence:
                in_fence = True
                fence_char = fm.group(1)[0]
                info = fm.group(2).strip().split()
                shell = (info[0].lower() if info else "") in FENCED_INFO
                cur = []
            elif fm.group(1)[0] == fence_char:
                in_fence = False
                if shell:
                    blocks.append(cur)
            continue
        if in_fence:
            inside.add(lineno)
            if shell:
                cur.append((lineno, line))
    return inside, blocks


def logical_lines(block: list[tuple[int, str]]) -> list[tuple[int, str]]:
    """Join ``\\``-continuations (result carries the first line's number)."""
    out: list[tuple[int, str]] = []
    for lineno, text in block:
        if out and out[-1][1].endswith("\\"):
            out[-1] = (out[-1][0], out[-1][1][:-1] + " " + text.strip())
        else:
            out.append((lineno, text))
    return out


def unwrap_tokens(tokens: list[str],
                  depth: int = 0) -> tuple[str | None, list[str]]:
    """(head, the token list the head was taken from).  Leading ``VAR=value``
    assignments are dropped, wrapper prefixes (sudo/env/command/nohup/time/
    builtin/xargs — flags that belong to the wrapper, e.g. ``xargs -n1``, are
    skipped; a wrapper's *argument* flag like ``sudo -u root ls`` misidentifies
    ``root`` — documented limit) are consumed, and one ``sh -c``/``bash -c``/
    ``zsh -c`` level is unwrapped to its script.  The second element matters:
    arguments must be read from the same list as the head, or a ``sh -c 'cat
    corpus/x.md'`` segment tests the whole script string as a path (the
    false positive the labrat lane planted at round 16)."""
    if depth > 4:
        return None, tokens
    i = 0
    while i < len(tokens) and ASSIGN_RE.match(tokens[i]):
        i += 1
    wrapped = False
    while i < len(tokens) and tokens[i] in WRAPPER_PREFIXES:
        i += 1
        wrapped = True
        while i < len(tokens) and ASSIGN_RE.match(tokens[i]):
            i += 1
    if wrapped:
        while i < len(tokens) and tokens[i].startswith("-"):
            i += 1
        while i < len(tokens) and ASSIGN_RE.match(tokens[i]):
            i += 1
    if i >= len(tokens):
        return None, tokens
    if (tokens[i] in SH_C_SHELLS and i + 2 < len(tokens)
            and tokens[i + 1] == "-c"):
        try:
            inner = shlex.split(tokens[i + 2], posix=True)
        except ValueError:
            inner = tokens[i + 2].split()
        return unwrap_tokens(inner, depth + 1)
    return tokens[i], tokens[i:]


def head_after_unwrap(tokens: list[str], depth: int = 0) -> str | None:
    """Subject head only (see ``unwrap_tokens``)."""
    return unwrap_tokens(tokens, depth)[0]


def safe_resolve(head: str, base: Path, repo: Path) -> bool:
    """``..`` segments never resolve against a base (path-escape oracle
    guard); absolute heads check exists(); relative heads check which(),
    then the cd-tracked base, then the repo root.  A token carrying a slash
    is a *path*, not a PATH lookup (POSIX), so ``shutil.which`` is skipped for
    it — otherwise the verdict would depend on the verifier's cwd (the
    independent lane's A13)."""
    if ".." in head.split("/"):
        return False
    if os.path.isabs(head):
        return os.path.exists(head)
    if "/" not in head and shutil.which(head):
        return True
    for b in (base, repo):
        try:
            if (b / head).exists():
                return True
        except OSError:
            continue
    return False


def is_instrument(path: Path) -> bool:
    """Round-16 R2: a ``delegated:`` target must be an instrument — a file
    whose suffix is a declared script suffix, whose first two bytes are a
    shebang, or whose first four are the ELF magic (a compiled instrument
    carries neither suffix nor shebang: the critic lane falsified the
    suffix-only test with ``~/.local/bin/sekhmet``).  A README, a JSON map,
    a directory or a SKILL.md is not an instrument."""
    try:
        if not path.is_file():
            return False
    except OSError:
        return False
    if path.suffix.lower() in INSTRUMENT_SUFFIXES:
        return True
    try:
        with path.open("rb") as fh:
            head = fh.read(4)
    except OSError:
        return False
    return head[:2] == b"#!" or head == b"\x7fELF"


TRAILING_PUNCT = ",;:)]}\"'"


def strip_token_dressing(tok: str) -> str:
    """A citation or argument may carry a line anchor (``file.md:42``) or be
    glued to prose punctuation (``file.md,``); neither changes the path."""
    tok = tok.rstrip(TRAILING_PUNCT)
    m = re.match(r"^(.+\.\w+):\d+(-\d+)?$", tok)
    return m.group(1) if m else tok


def path_like_arg(tok: str) -> bool:
    """Round-16 R1: does this fenced argument name a path?  Absolute tokens
    are out of scope (host-dependent — the named ceiling), as are flags,
    ``VAR=value`` assignments, URLs and anything carrying a shell
    metacharacter.  A token qualifies when it ends in a known file suffix, or
    carries a slash and a dotted last segment (so ``s/foo/bar/`` is not a
    path)."""
    tok = strip_token_dressing(tok)
    if not tok or tok.startswith("-"):
        return False
    if os.path.isabs(tok) or "://" in tok:
        return False
    if ASSIGN_RE.match(tok) or any(c in SHELL_METACHARS for c in tok):
        return False
    if "/" in tok:
        return "." in tok.rstrip("/").rsplit("/", 1)[-1]
    return Path(tok).suffix.lower() in PATH_ARG_SUFFIXES


def arg_subjects(tokens: list[str], segment: str, lineno: int,
                 base: Path) -> list[dict]:
    """Round-16 R1: path-like arguments after the head of a segment.  A token
    whose predecessor is a redirect operator or a declared output flag is a
    *written* path and is skipped; a ``#`` token ends the scan (a trailing
    comment is prose — the blast census found comment tails harvested as
    paths)."""
    out: list[dict] = []
    for i in range(1, len(tokens)):
        tok = tokens[i]
        if tok.startswith("#"):
            break
        if not path_like_arg(tok):
            continue
        prev = tokens[i - 1]
        if prev in REDIRECT_TOKENS or prev in OUTPUT_FLAGS \
                or prev.startswith(">"):
            continue
        out.append({"line": lineno, "source": "fenced-arg", "segment": segment,
                    "head": tok, "base": base})
    return out


def command_subjects(lines: list[str], vocab: frozenset[str],
                     repo: Path) -> tuple[list[dict], int]:
    """(subjects, segments_seen).  Fenced shell blocks: every segment's
    unwrapped head is a subject unless it is a keyword/builtin, bare
    assignment, comment/shebang or metacharacter token.  Inline spans: a
    segment is a subject only when its unwrapped head is in the declared
    vocabulary.  ``cd`` updates the relative resolution base."""
    subjects: list[dict] = []
    segments = 0
    fenced, blocks = fenced_regions(lines)
    for block in blocks:
        base = repo
        stack: list[Path] = []
        heredoc_end: str | None = None
        for lineno, line in logical_lines(block):
            stripped = line.strip()
            if heredoc_end is not None:
                if stripped == heredoc_end:
                    heredoc_end = None
                continue
            if not stripped or stripped.startswith("#"):
                continue
            hm = HEREDOC_RE.search(line)
            if hm:
                heredoc_end = hm.group(1)
            for raw in SEGMENT_SPLIT_RE.split(line):
                segment = raw.strip()
                if not segment or segment.startswith("#"):
                    continue
                segments += 1
                try:
                    tokens = shlex.split(segment, posix=True)
                except ValueError:
                    tokens = segment.split()
                if not tokens:
                    continue
                if tokens[0] in ("cd", "pushd", "popd"):
                    arg = tokens[1] if len(tokens) > 1 else ""
                    cand = (base / arg) if arg and not os.path.isabs(arg) \
                        else Path(arg or str(repo))
                    if tokens[0] == "popd":
                        cand = stack.pop() if stack else repo
                    ok = ".." not in arg.split("/") and cand.is_dir()
                    subjects.append({"line": lineno, "source": "fenced",
                                     "segment": segment,
                                     "head": "%s %s" % (tokens[0], arg),
                                     "base": base, "pre_resolved": ok})
                    if ok:
                        if tokens[0] == "pushd":
                            stack.append(base)
                        base = cand
                    else:
                        subjects[-1]["unresolved"] = True
                    continue
                head, eff = unwrap_tokens(tokens)
                if head is None:
                    continue
                if head in SHELL_SKIP or ASSIGN_RE.match(head):
                    # a builtin whose argument it *acts on* still has
                    # subjects: `source verifiers/nope.sh` fails when pasted.
                    # `echo`/`printf`/`test` arguments are display or query
                    # text and stay out of scope (M35's planted `echo <bare>`
                    # is benign for the same reason).
                    if head in READ_ARG_BUILTINS:
                        subjects.extend(
                            arg_subjects(eff, segment, lineno, base))
                    continue
                if any(c in SHELL_METACHARS for c in head):
                    continue
                subjects.append({"line": lineno, "source": "fenced",
                                 "segment": segment, "head": head,
                                 "base": base})
                subjects.extend(arg_subjects(eff, segment, lineno, base))
    for lineno, line in enumerate(lines, 1):
        if lineno in fenced:
            continue
        for sm in INLINE_SPAN_RE.finditer(line):
            span = sm.group(1).strip()
            if not span or "<" in span or ">" in span:
                continue
            for raw in SEGMENT_SPLIT_RE.split(span):
                segment = raw.strip()
                if not segment:
                    continue
                try:
                    tokens = shlex.split(segment, posix=True)
                except ValueError:
                    tokens = segment.split()
                if not tokens:
                    continue
                head = head_after_unwrap(tokens)
                if head is None:
                    continue
                if head in SHELL_SKIP or ASSIGN_RE.match(head):
                    continue
                if any(c in SHELL_METACHARS for c in head):
                    continue
                # An inline span is a command candidate only when its head is a
                # declared vocabulary word — otherwise it is prose (a dotted
                # identifier, a key, a flag).  Counting non-vocabulary spans as
                # "segments seen" was the round-15 vacuity miscount the critic
                # predicted: prose spans forced S>0/N==0 FAILs on clean files.
                if head not in vocab:
                    continue
                segments += 1
                subjects.append({"line": lineno, "source": "inline",
                                 "segment": segment, "head": head,
                                 "base": repo})
                subjects.extend(arg_subjects(tokens, segment, lineno, repo))
    return subjects, segments


# ---------------------------------------------------------------------------
# checks: each returns (status, evaluated, detail) — status in PASS/FAIL/N/A
# ---------------------------------------------------------------------------

def check_box_map(boxes: list[dict], m: dict, target_name: str,
                  near_misses: list[dict] | None = None,
                  repo: Path | None = None,
                  map_repo: Path | None = None) -> tuple[str, int, str]:
    entries = m["boxes"]
    problems: list[str] = []
    near_misses = near_misses or []
    if m["file"] != target_name:
        problems.append("map is for file %r, target is %r"
                        % (m["file"], target_name))
    if not boxes:
        problems.append("no checklist boxes in target file")
    if not entries:
        problems.append("no map entries")
    seen_ids: Counter = Counter(e["box_id"] for e in entries)
    for bid, n in seen_ids.items():
        if n > 1:
            problems.append("duplicate box_id %r (x%d)" % (bid, n))
    executed = []
    for e in entries:
        dm = DISPOSITION_RE.match(e["disposition"])
        if dm and dm.group(1) == "executed":
            cid = dm.group(2).strip()
            if cid not in CHECK_IDS:
                problems.append("map entry %s names unknown check %r"
                                % (e["box_id"], cid))
            else:
                executed.append(e)
    if not executed:
        problems.append("no map entry with a valid executed: disposition")
    for e in entries:
        dm = DISPOSITION_RE.match(e["disposition"])
        if dm and dm.group(1) == "delegated":
            target = dm.group(2).strip()
            # the delegated instrument lives in the map's repo, not the
            # target's (a red-before run points the live map at a snapshot)
            base = map_repo or repo or Path(".")
            candidate = base / target
            if ".." in target.split("/"):
                problems.append(
                    "map entry %s delegates outside the map's repo: %r"
                    % (e["box_id"], target))
            elif not candidate.exists():
                problems.append(
                    "map entry %s delegates to a target that does not exist: %r"
                    % (e["box_id"], target))
            elif not is_instrument(candidate):
                problems.append(
                    "map entry %s delegates to a target that is not an "
                    "instrument: %r (a delegated target must carry a script "
                    "suffix %s or a shebang)"
                    % (e["box_id"], target,
                       "/".join(sorted(INSTRUMENT_SUFFIXES))))
    live = Counter((b["section"], b["sha256"]) for b in boxes)
    mapped = Counter((e["section"], e["text_sha256"]) for e in entries)
    label_by_key: dict[tuple[str, str], str] = {}
    for e in entries:
        label_by_key.setdefault((e["section"], e["text_sha256"]), e["box_id"])
    for key, n in mapped.items():
        for _ in range(n - live.get(key, 0)):
            problems.append("map entry %s has no live box (section %r)"
                            % (label_by_key[key], key[0] or "<none>"))
    live_label: dict[tuple[str, str], str] = {}
    for b in boxes:
        live_label.setdefault((b["section"], b["sha256"]),
                              "line %d" % b["line"])
    for key, n in live.items():
        for _ in range(n - mapped.get(key, 0)):
            problems.append("unmapped box at %s (section %r, sha256 %.12s…)"
                            % (live_label[key], key[0] or "<none>", key[1]))
    ann = re.compile(r"\(executed:\s*`?([a-z0-9_.]+)`?")
    disp_by_key: dict[tuple[str, str], str] = {}
    for e in entries:
        disp_by_key.setdefault((e["section"], e["text_sha256"]),
                               e["disposition"].strip())
    for b in boxes:
        found = set(ann.findall(b["text"]))
        declared = ann.search(b["text"]) if len(found) == 1 else None
        recorded = disp_by_key.get((b["section"], b["sha256"]), "")
        if len(found) > 1:
            problems.append("line %d carries %d executed-annotations"
                            % (b["line"], len(found)))
        elif declared and recorded != "executed:" + declared.group(1):
            problems.append(
                "line %d annotation claims %r but the map records %r"
                % (b["line"], declared.group(1), recorded or "<no entry>"))
        elif not declared and recorded.startswith("executed:"):
            problems.append(
                "line %d is recorded as %s in the map but the box does not "
                "disclose it" % (b["line"], recorded))
    for b in boxes:
        if b.get("marker", " ") != " ":
            problems.append(
                "line %d carries a non-procedure checkbox marker '[%s]'"
                % (b["line"], b["marker"]))
    for nm in near_misses:
        problems.append("line %d near-miss checkbox marker: %r"
                        % (nm["line"], nm["text"]))
    evaluated = len(boxes)
    if problems:
        return "FAIL", evaluated, "; ".join(problems[:6]) + (
            " … (+%d more)" % (len(problems) - 6) if len(problems) > 6 else "")
    return "PASS", evaluated, (
        "%d boxes mapped (%d executed, %d delegated, %d unexecuted)"
        % (len(boxes), len(executed),
           sum(1 for e in entries
               if e["disposition"].startswith("delegated:")),
           sum(1 for e in entries
               if e["disposition"].startswith("unexecuted:"))))


def check_frontmatter(fm: tuple[dict | None, str]) -> tuple[str, int, str]:
    fields, problem = fm
    evaluated = 4
    if fields is None:
        return "FAIL", evaluated, problem
    problems = []
    for key in ("name", "description"):
        if key not in fields:
            problems.append("missing %s:" % key)
        elif not fields[key].strip():
            problems.append("empty %s:" % key)
    if problems:
        return "FAIL", evaluated, "; ".join(problems)
    return "PASS", evaluated, (
        "frontmatter parses: name=%r, description %d chars"
        % (fields["name"].strip(), len(fields["description"].strip())))


def check_name_directory(fm: tuple[dict | None, str],
                         skill_path: Path) -> tuple[str, int, str]:
    fields, problem = fm
    if fields is None:
        return "FAIL", 0, "cannot evaluate: %s" % problem
    name = fields.get("name", "").strip()
    if not name:
        return "FAIL", 0, "cannot evaluate: empty name:"
    dirname = os.path.basename(
        os.path.dirname(os.path.abspath(str(skill_path))))
    if name != dirname:
        return "FAIL", 1, "name %r != directory %r" % (name, dirname)
    return "PASS", 1, "name %r == directory %r" % (name, dirname)


def check_literal_trigger(fm: tuple[dict | None, str]) -> tuple[str, int, str]:
    fields, problem = fm
    if fields is None:
        return "FAIL", 0, "cannot evaluate: %s" % problem
    for key in fields:
        if key.lower() in ("triggers", "trigger") and fields[key].strip():
            return "PASS", 1, "frontmatter carries %s: list" % key
    desc = fields.get("description", "").strip()
    if not desc:
        return "FAIL", 0, "cannot evaluate: empty description:"
    if "Triggers:" in desc:
        return "PASS", 1, "description carries literal 'Triggers:'"
    m = QUOTED_SPAN_RE.search(desc)
    if m:
        span = next(g for g in m.groups() if g is not None)
        return "PASS", 1, "quoted/backticked trigger span %r (%d chars)" % (
            span, len(span))
    return "FAIL", 1, ("no quoted/backticked span >=2 chars, no 'Triggers:', "
                       "no triggers: key — shape test, not semantics")


def check_anti_trigger(fm: tuple[dict | None, str]) -> tuple[str, int, str]:
    fields, problem = fm
    if fields is None:
        return "FAIL", 0, "cannot evaluate: %s" % problem
    desc = fields.get("description", "").strip()
    if not desc:
        return "FAIL", 0, "cannot evaluate: empty description:"
    stripped = ALL_QUOTED_SPANS_RE.sub("", desc)
    m = ANTI_TRIGGER_RE.search(stripped)
    limit = ("vocabulary test, not semantics: a vacuous 'Never use this "
             "skill.' passes and an unlisted real exclusion fails")
    if m:
        return "PASS", 1, "exclusion marker %r present (%s)" % (
            m.group(0), limit)
    return "FAIL", 1, ("no exclusion-vocabulary marker in description "
                       "(observed set: anti-trigger, exclusion, not for, "
                       "do not, never, without, except, n/a, only when, "
                       "exclusively, 反触发, 不用于, 不要用于, 排除, 勿用于; %s)"
                       % limit)


def box_line_budget(boxes: list[dict], default: int) -> tuple[int, str]:
    """The threshold lives in the box text: first integer in the box whose
    text matches ``file … <int> … line(s)``.  Falls back to --max-lines."""
    for b in boxes:
        if LINE_BOUND_BOX_RE.search(b["text"]):
            m = INT_RE.search(b["text"])
            if m:
                return int(m.group(0)), "box at line %d" % b["line"]
    return default, "--max-lines"


def check_line_budget(lines: list[str], boxes: list[dict],
                      max_lines: int) -> tuple[str, int, str]:
    n = len(lines)
    if n == 0:
        return "FAIL", 0, "file is empty (0 lines)"
    limit, source = box_line_budget(boxes, max_lines)
    if n > limit:
        return "FAIL", n, "%d lines exceed budget %d (from %s)" % (
            n, limit, source)
    return "PASS", n, "%d lines within budget %d (from %s)" % (
        n, limit, source)


def check_no_placeholder(lines: list[str]) -> tuple[str, int, str]:
    hits: list[str] = []
    scanned = 0
    for lineno, line in enumerate(lines, 1):
        stripped = BACKTICK_SPAN_RE.sub("", line)
        if not stripped.strip():
            continue
        scanned += 1
        for m in PLACEHOLDER_RE.finditer(stripped):
            if NEGATION_RE.search(stripped[:m.start()]):
                continue  # negated earlier on the same line: a rule
            hits.append("line %d: %r" % (lineno, m.group(0)))
    if hits:
        return "FAIL", scanned, "; ".join(hits[:4]) + (
            " … (+%d more)" % (len(hits) - 4) if len(hits) > 4 else "")
    if scanned == 0:
        return "FAIL", 0, "no scannable lines"
    return "PASS", scanned, "no placeholder markers in %d scanned lines" % scanned


def citation_resolve(tok: str, repo: Path) -> bool:
    """Resolution for a citation token.  A plain repo-rooted token uses
    ``safe_resolve``; a token with leading ``..`` hops resolves against the
    repo's ancestors, bounded to 3 hops with no further ``..`` inside (the
    fleet's lane-report convention — the corpus verifier resolves the same
    shape).  Read-only existence test; the token comes from a lane-authored
    file, not from the checked command surface, which is why the strict
    no-``..`` rule of ``safe_resolve`` is relaxed here and bounded."""
    parts = tok.split("/")
    if ".." not in parts:
        return safe_resolve(tok, repo, repo)
    hops = 0
    while parts and parts[0] == "..":
        parts.pop(0)
        hops += 1
    if hops > 3 or ".." in parts or not parts:
        return False
    base = repo
    for _ in range(hops):
        base = base.parent
    try:
        return (base / "/".join(parts)).exists()
    except OSError:
        return False


def advance_quote_state(text: str, start: int, end: int,
                        state: bool) -> bool:
    """Carry unescaped double-quote state through one text slice."""
    for pos in range(start, end):
        if text[pos] != '"':
            continue
        escapes = 0
        prior = pos - 1
        while prior >= 0 and text[prior] == "\\":
            escapes += 1
            prior -= 1
        if escapes % 2 == 0:
            state = not state
    return state


def citation_subjects(lines: list[str], source: str = "",
                      exclude_quoted: bool = False,
                      exclude_schematic: bool = False
                      ) -> tuple[list[dict], dict[str, list[dict]]]:
    """Extract repo-rooted backtick tokens and named exclusions.

    A quoted exclusion must open and close on the token's own line; carrying
    quote parity across Markdown lines suppresses unrelated live citations.
    The trigger check leaves both exclusions disabled, preserving its contract.
    """
    subjects: list[dict] = []
    excluded: dict[str, list[dict]] = {"quoted": [], "schematic": []}
    for lineno, line in enumerate(lines, 1):
        words: list[tuple[int, int, str]] = []
        for span in INLINE_SPAN_RE.finditer(line):
            base = span.start(1)
            for word in re.finditer(r"\S+", span.group(1)):
                words.append((base + word.start(), base + word.end(),
                              word.group(0)))
        for start, end, word in words:
            at_start = advance_quote_state(line, 0, start, False)
            at_end = advance_quote_state(line, start, end, at_start)
            at_line_end = advance_quote_state(
                line, end, len(line), at_end)
            quoted = at_start and not at_line_end

            tok = word.split("#", 1)[0]
            if not tok or any(c in tok for c in "<>*?$"):
                continue
            if tok.startswith(("http", "~", "-")):
                continue
            norm = strip_token_dressing(tok)
            norm = norm[2:] if norm.startswith("./") else norm
            if not norm.startswith(CITATION_ROOTS):
                continue
            stripped = norm.rstrip("/")
            if stripped and "/" not in stripped:
                continue
            row = {"line": lineno, "token": norm, "raw": word}
            if source:
                row["source"] = source
            if exclude_quoted and quoted:
                excluded["quoted"].append(row)
                continue
            if exclude_schematic and (
                    "…" in norm or "..." in norm
                    or SCHEMATIC_CITATION_RE.search(norm)):
                excluded["schematic"].append(row)
                continue
            subjects.append(row)
    return subjects, excluded


def check_citation_resolves(lines: list[str],
                            repo: Path) -> tuple[str, int, str]:
    """Round-16 R3: repo-rooted backtick tokens resolve from repo."""
    subjects, _ = citation_subjects(lines)
    evaluated = len(subjects)
    if evaluated == 0:
        return "N/A", 0, (
            "no repo-rooted citation tokens (a token counts when it starts "
            "with %s and carries no placeholder, glob, $VAR or named base)"
            % ", ".join(CITATION_ROOTS))
    bad = []
    for subject in subjects:
        if not citation_resolve(subject["token"], repo):
            bad.append("line %d: %r does not resolve from %s"
                       % (subject["line"], subject["token"], repo))
    if bad:
        return "FAIL", evaluated, "; ".join(bad[:4]) + (
            " … (+%d more)" % (len(bad) - 4) if len(bad) > 4 else "")
    return "PASS", evaluated, (
        "%d repo-rooted citation token(s) resolve from the repo root"
        % evaluated)


def check_governance_citations(repo: Path) -> tuple[str, int, str]:
    """Round-17: root governance path claims remain navigable at HEAD."""
    repo = repo.resolve()
    subjects: list[dict] = []
    excluded: dict[str, list[dict]] = {"quoted": [], "schematic": []}
    unreadable = []
    for name in GOVERNANCE_FILES:
        path = repo / name
        try:
            lines = path.read_text(encoding="utf-8").splitlines()
        except OSError as exc:
            unreadable.append("%s (%s)" % (name, exc))
            continue
        found, skipped = citation_subjects(
            lines, source=name, exclude_quoted=True,
            exclude_schematic=True)
        subjects.extend(found)
        for kind in excluded:
            excluded[kind].extend(skipped[kind])

    evaluated = len(subjects)
    context = ("%d quoted meta-finding(s), %d schematic token(s) excluded"
               % (len(excluded["quoted"]), len(excluded["schematic"])))
    if unreadable:
        return "FAIL", evaluated, "unreadable governance file(s): %s; %s" % (
            ", ".join(unreadable), context)
    if evaluated == 0:
        return "FAIL", 0, "no checked governance citation subjects; %s" % context
    bad = []
    for subject in subjects:
        if not citation_resolve(subject["token"], repo):
            bad.append("%s:%d: %r does not resolve from %s"
                       % (subject["source"], subject["line"],
                          subject["token"], repo))
    if bad:
        return "FAIL", evaluated, "%s; %s" % (
            "; ".join(bad[:4]) + (
                " … (+%d more)" % (len(bad) - 4) if len(bad) > 4 else ""),
            context)
    return "PASS", evaluated, (
        "%d governance citation token(s) resolve across %d files; %s"
        % (evaluated, len(GOVERNANCE_FILES), context))


def check_commands(lines: list[str], repo: Path,
                   vocab: frozenset[str]) -> tuple[str, int, str]:
    subjects, segments = command_subjects(lines, vocab, repo)
    evaluated = len(subjects)
    if evaluated == 0:
        if segments > 0:
            return "FAIL", 0, (
                "%d segment(s) seen, 0 command subjects — every head fell "
                "through the skip lists" % segments)
        return "N/A", 0, ("0 segments: no shell-fenced block lines and no "
                          "inline spans headed by a declared vocabulary word")
    bad = []
    for s in subjects:
        if s.pop("unresolved", False):
            bad.append("line %d: %r does not resolve" % (s["line"], s["head"]))
            continue
        if s.pop("pre_resolved", False):
            continue
        if not safe_resolve(s["head"], s["base"], repo):
            bad.append("line %d: %r (%s, segment %r) does not resolve"
                       % (s["line"], s["head"], s["source"], s["segment"]))
    if bad:
        return "FAIL", evaluated, "%d segments; " % segments + "; ".join(
            bad[:4]) + (
            " … (+%d more)" % (len(bad) - 4) if len(bad) > 4 else "")
    return "PASS", evaluated, "%d segments; %d command subject(s) resolve" % (
        segments, evaluated)


# ---------------------------------------------------------------------------
# self-test: run the CLI surface against committed fixtures only
# ---------------------------------------------------------------------------

def run_capture(argv: list[str]) -> tuple[int, str]:
    buf = io.StringIO()
    err = io.StringIO()
    with contextlib.redirect_stdout(buf), contextlib.redirect_stderr(err):
        code = main(argv)
    return code, buf.getvalue() + err.getvalue()


def evaluated_of(out: str, cid: str) -> int | None:
    for line in out.splitlines():
        m = re.match(r"(?:PASS|FAIL|N/A) %s: evaluated (\d+)"
                     % re.escape(cid), line)
        if m:
            return int(m.group(1))
    return None


def self_test() -> int:
    failures: list[str] = []
    total = 0

    def rec(what: str, ok: bool, got: object) -> None:
        nonlocal total
        total += 1
        if not ok:
            failures.append("%s: got %r" % (what, got))

    fx = str(FIXTURES)

    def run(case: str, *extra: str) -> tuple[int, str]:
        argv = ["--skill", os.path.join(fx, case, "SKILL.md"),
                "--map", os.path.join(fx, case, "map.json")]
        vfile = os.path.join(fx, case, "vocab.json")
        if os.path.exists(vfile):
            argv += ["--vocabulary", vfile]
        argv += list(extra)
        return run_capture(argv)

    # (case, exit, fails, nas, needles); passes = the rest of CHECK_IDS
    CASES = [
        ("clean", 0, [], [], []),
        ("no-frontmatter", 1,
         ["trigger.frontmatter_parses", "trigger.name_directory",
          "trigger.literal_trigger_string", "trigger.anti_trigger_clause"],
         [], ["no leading ---"]),
        ("fm-null", 1,
         ["trigger.frontmatter_parses", "trigger.literal_trigger_string",
          "trigger.anti_trigger_clause"],
         [], ["empty description"]),
        ("fm-malformed", 1,
         ["trigger.frontmatter_parses", "trigger.name_directory",
          "trigger.literal_trigger_string", "trigger.anti_trigger_clause"],
         [], ["unbalanced quote"]),
        ("fm-dup-key", 1,
         ["trigger.frontmatter_parses", "trigger.name_directory",
          "trigger.literal_trigger_string", "trigger.anti_trigger_clause"],
         [], ["duplicate key"]),
        ("fm-body-yaml", 1,
         ["trigger.frontmatter_parses", "trigger.name_directory",
          "trigger.literal_trigger_string", "trigger.anti_trigger_clause"],
         [], ["no leading ---"]),
        ("fm-nested-metadata", 0, [], [], []),
        ("fm-stray-indent", 1,
         ["trigger.frontmatter_parses", "trigger.name_directory",
          "trigger.literal_trigger_string", "trigger.anti_trigger_clause"],
         [], ["stray indented line"]),
        # round-15 closures of the critic's three escape surfaces
        ("map-annotation-mismatch", 1, ["checklist.box_map_complete"],
         ["trigger.command_binary_resolves"], ["annotation claims"]),
        ("map-executed-undisclosed", 1, ["checklist.box_map_complete"],
         ["trigger.command_binary_resolves"], ["does not disclose"]),
        ("map-dead-delegated", 1, ["checklist.box_map_complete"],
         ["trigger.command_binary_resolves"], ["does not exist"]),
        ("marker-checked", 1, ["checklist.box_map_complete"],
         ["trigger.command_binary_resolves"], ["non-procedure checkbox marker"]),
        ("marker-near-miss", 1, ["checklist.box_map_complete"],
         ["trigger.command_binary_resolves"], ["near-miss checkbox marker"]),
        ("name-mismatch", 1, ["trigger.name_directory"], [],
         ["wrong-skill-name"]),
        ("name-quoted", 0, [], [], []),
        ("no-literal-trigger", 1, ["trigger.literal_trigger_string"], [], []),
        ("trigger-key", 0, [], [], []),
        ("no-anti-trigger", 1, ["trigger.anti_trigger_clause"], [], []),
        ("anti-quoted-negation", 1, ["trigger.anti_trigger_clause"], [], []),
        ("over-line-budget", 1, ["trigger.line_budget"], [],
         ["exceed budget"]),
        ("line-budget-box-binding", 1, ["trigger.line_budget"], [],
         ["budget 20"]),
        ("placeholder-todo", 1, ["trigger.no_placeholder"], [], ["TODO"]),
        ("placeholder-embedded", 1, ["trigger.no_placeholder"], [], ["TODO"]),
        ("todo-stub-order", 1, ["trigger.no_placeholder"], [], ["TODO"]),
        ("unresolvable-command", 1, ["trigger.command_binary_resolves"], [],
         ["definitely-missing-alpha", "r15absentbin"]),
        ("command-wrapper-inner", 1, ["trigger.command_binary_resolves"], [],
         ["definitely-missing"]),
        ("negation-respected", 0, [], [], []),
        ("command-skip-list", 0, [], [], []),
        ("command-fence-filter", 0, [], [], []),
        ("command-heredoc-cd", 0, [], [], []),
        ("command-heredoc-tilde", 0, [], [], []),
        ("command-heredoc-tilde-dead", 1,
         ["trigger.command_binary_resolves"], [],
         ["corpus/absent-round17.md"]),
        ("command-heredoc-tilde-misterm", 0, [], [], []),
        ("map-box-reworded", 1, ["checklist.box_map_complete"], [],
         ["unmapped box", "has no live box"]),
        ("map-extra-entry", 1, ["checklist.box_map_complete"], [],
         ["has no live box"]),
        ("map-missing-entry", 1, ["checklist.box_map_complete"], [],
         ["unmapped box"]),
        ("map-dup-box", 1, ["checklist.box_map_complete"], [],
         ["unmapped box"]),
        ("map-dup-id", 1, ["checklist.box_map_complete"], [],
         ["duplicate box_id"]),
        ("map-unknown-executed", 1, ["checklist.box_map_complete"], [],
         ["unknown check"]),
        ("map-no-executed-entry", 1, ["checklist.box_map_complete"], [],
         ["executed:"]),
        ("map-file-mismatch", 1, ["checklist.box_map_complete"], [],
         ["target is"]),
        ("empty-file", 1,
         ["checklist.box_map_complete", "trigger.frontmatter_parses",
          "trigger.name_directory", "trigger.literal_trigger_string",
          "trigger.anti_trigger_clause", "trigger.line_budget",
          "trigger.no_placeholder"],
         ["trigger.command_binary_resolves"], []),
        ("no-checklist-section", 1, ["checklist.box_map_complete"], [],
         ["no checklist boxes"]),
        ("missing-map", 3, [], [], ["ERROR"]),
        ("map-malformed", 3, [], [], ["ERROR"]),
        ("commands-fenced-only", 0, [], [], []),
        ("commands-inline-only", 0, [], [], []),
        ("commands-both", 0, [], [], []),
        ("commands-none", 0, [], ["trigger.command_binary_resolves"], []),
        # round-16 closures: R1 path-like arguments, R2 instrument-ness,
        # R3 citation resolution.  Each lands with a fixture that was red
        # before the rule (recorded in corpus/knowledge/
        # checklist-execution-round16.md).
        ("citation-dead", 1, ["trigger.citation_resolves"], [],
         ["corpus/absent-round16-fixture.md"]),
        ("citation-base-named", 0, [], [], ["no repo-rooted citation tokens"]),
        ("command-path-arg", 1, ["trigger.command_binary_resolves"], [],
         ["corpus/absent-round16-arg.md"]),
        ("command-path-arg-ok", 0, [], [], []),
        ("command-redirect-target", 0, [], [], []),
        ("delegated-noninstrument", 1, ["checklist.box_map_complete"], [],
         ["not an instrument"]),
        # boundaries: the PASS side of the citation rule, the two declared
        # ceilings (single-segment root, directory as a delegated target),
        # and the class the live file carried.
        ("citation-ok", 0, [],
         ["trigger.command_binary_resolves"], []),
        ("citation-boundary-dirslash", 0, [],
         ["trigger.command_binary_resolves", "trigger.citation_resolves"],
         ["no repo-rooted citation tokens"]),
        ("citation-boundary-ufo", 1, ["trigger.citation_resolves"],
         ["trigger.command_binary_resolves"], [".ufo/prompts/"]),
        ("delegated-directory", 1, ["checklist.box_map_complete"],
         ["trigger.command_binary_resolves"], ["not an instrument"]),
        # critic-driven: the `./` launder, word-wise harvesting, and the two
        # instrument boundary cases (ELF magic accepted, `.py` data pinned)
        ("citation-dot-slash", 1, ["trigger.citation_resolves"], [],
         ["corpus/absent-round16-dotslash.md"]),
        ("citation-second-word", 1, ["trigger.citation_resolves"],
         ["trigger.command_binary_resolves"],
         ["corpus/absent-round16-second.md"]),
        ("citation-second-word-ok", 0, [],
         ["trigger.command_binary_resolves"], []),
        ("delegated-elf", 0, [],
         ["trigger.command_binary_resolves", "trigger.citation_resolves"], []),
        ("delegated-py-suffix", 0, [],
         ["trigger.command_binary_resolves", "trigger.citation_resolves"], []),
        ("command-output-flag", 0, [], [], []),
        # sentinel-driven: `<` is an input redirect (its target must exist),
        # the `sh -c` inner script's arguments, a line-anchored citation, and
        # a delegated target that escapes the map's repo
        ("command-input-redirect", 1, ["trigger.command_binary_resolves"], [],
         ["corpus/absent-round16-stdin.md"]),
        ("command-sh-c-inner", 1, ["trigger.command_binary_resolves"], [],
         ["corpus/absent-round16-shc.md"]),
        ("command-sh-c-ok", 0, [], [], []),
        ("citation-anchor-ok", 0, [], [], []),
        ("delegated-escape", 1, ["checklist.box_map_complete"], [],
         ["outside the map's repo"]),
        # the planner's rank-1 residual: a builtin that acts on its operand
        ("command-source-operand", 1, ["trigger.command_binary_resolves"], [],
         ["verifiers/absent-round16-source.sh"]),
    ]

    # Checks whose subject may legitimately be absent from a fixture: an
    # absent subject is N/A, and the non-vacuity guard is the explicit
    # evaluated>0 assertion in the targeted extras below.
    NA_ALLOWED = frozenset([
        "trigger.citation_resolves", "governance.citation_resolves"])
    for case, want_code, fails, nas, needles in CASES:
        code, out = run(case)
        rec("%s: exit %d" % (case, want_code), code == want_code, code)
        for needle in needles:
            rec("%s: names %r" % (case, needle), needle in out, out)
        if want_code >= 2:
            continue
        passes = [c for c in CHECK_IDS if c not in fails and c not in nas]
        for cid in fails:
            rec("%s: FAIL %s" % (case, cid), ("FAIL %s:" % cid) in out, out)
        for cid in passes:
            if cid in NA_ALLOWED and evaluated_of(out, cid) == 0:
                rec("%s: N/A-allowed %s" % (case, cid),
                    ("N/A %s:" % cid) in out, out)
                continue
            rec("%s: PASS %s" % (case, cid), ("PASS %s:" % cid) in out, out)
            rec("%s: PASS %s evaluated>0" % (case, cid),
                (evaluated_of(out, cid) or 0) > 0, evaluated_of(out, cid))
        for cid in nas:
            rec("%s: N/A %s" % (case, cid), ("N/A %s:" % cid) in out, out)
            rec("%s: N/A %s evaluated==0" % (case, cid),
                evaluated_of(out, cid) == 0, evaluated_of(out, cid))
        for line in out.splitlines():
            if "evaluated 0" in line:
                rec("%s: 'evaluated 0' line is not a PASS" % case,
                    not line.startswith("PASS"), line)

    # --- targeted extras ------------------------------------------------------
    code, out = run("negation-respected")
    rec("negation-respected: fixture carries the rule line",
        "No `TODO`" in Path(fx, "negation-respected",
                            "SKILL.md").read_text(), "fixture drifted")

    code, out = run("over-line-budget", "--max-lines", "10")
    rec("over-line-budget --max-lines 10: exit 1", code == 1, code)
    rec("over-line-budget --max-lines 10: FAIL line_budget",
        "FAIL trigger.line_budget:" in out, out)

    code, out = run("clean", "--check", "trigger.line_budget")
    rec("--check filter: exit 0", code == 0, code)
    rec("--check filter: only line_budget reported",
        "trigger.line_budget" in out and "box_map" not in out, out)

    code, out = run("missing-map", "--json")
    rec("missing-map --json: exit 3", code == 3, code)
    rec("missing-map --json: error key present",
        '"error"' in out and '"exit_code": 3' in out, out)

    # foreign target, no map pinned -> N/A, not exit 3
    code, out = run_capture(
        ["--skill", os.path.join(fx, "missing-map", "SKILL.md")])
    rec("foreign-no-map: exit 0", code == 0, code)
    rec("foreign-no-map: box_map N/A",
        "N/A checklist.box_map_complete:" in out, out)
    rec("foreign-no-map: N/A names no map pinned",
        "no map pinned" in out, out)

    for c in ("commands-fenced-only", "commands-inline-only", "commands-both"):
        code, out = run(c)
        rec("%s: extraction fired (evaluated>0)" % c,
            (evaluated_of(out, "trigger.command_binary_resolves") or 0) > 0,
            evaluated_of(out, "trigger.command_binary_resolves"))

    # command-skip-list reports both evaluated and segments
    code, out = run("command-skip-list")
    rec("command-skip-list: reports segments",
        "segments" in out, out)

    # round-16 non-vacuity: the citation check evaluates a subject on its own
    # fixture (never "evaluated 0" while failing) …
    for case, want in (("citation-dead", 1), ("citation-base-named", 0)):
        code, out = run(case)
        rec("%s: citation evaluated == %d" % (case, want),
            evaluated_of(out, "trigger.citation_resolves") == want,
            evaluated_of(out, "trigger.citation_resolves"))
    # … the named base is out of scope (N/A, not FAIL) …
    code, out = run("citation-base-named")
    rec("citation-base-named: citation N/A",
        "N/A trigger.citation_resolves:" in out, out)
    # … and a redirect target is written, not read: no unresolved subject.
    code, out = run("command-redirect-target")
    rec("command-redirect-target: exit 0", code == 0, code)
    rec("command-redirect-target: no unresolved subject",
        "does not resolve" not in out, out)
    # the argument half of R1 is a real subject, not a silently dropped token
    code, out = run("command-path-arg-ok")
    rec("command-path-arg-ok: 3 subjects incl. the argument",
        (evaluated_of(out, "trigger.command_binary_resolves") or 0) >= 3,
        evaluated_of(out, "trigger.command_binary_resolves"))
    # the PASS side of the citation rule is non-vacuous too
    code, out = run("citation-ok")
    rec("citation-ok: exit 0", code == 0, code)
    rec("citation-ok: citation evaluated == 2",
        evaluated_of(out, "trigger.citation_resolves") == 2,
        evaluated_of(out, "trigger.citation_resolves"))
    # an anchored citation resolves (the line anchor is not part of the path)
    code, out = run("citation-anchor-ok")
    rec("citation-anchor-ok: evaluated 2",
        evaluated_of(out, "trigger.citation_resolves") == 2,
        evaluated_of(out, "trigger.citation_resolves"))
    # a declared output flag exempts its target: `ls -la --out report.md`
    code, out = run("command-output-flag")
    rec("command-output-flag: exit 0, 2 subjects (target skipped)",
        (code == 0) and (evaluated_of(out, "trigger.command_binary_resolves") == 2),
        (code, evaluated_of(out, "trigger.command_binary_resolves")))
    # a directory is not an instrument (is_file guard, no traceback)
    code, out = run("delegated-directory")
    rec("delegated-directory: FAIL not-an-instrument, no traceback",
        ("not an instrument" in out) and ("Traceback" not in out), out)

    # round-17 M36 correction: `~` is part of the delimiter word.  The body
    # stays opaque, a correctly terminated block resumes scanning, and a bare
    # `EOF` does not terminate a `<<~EOF` heredoc.
    code, out = run("command-heredoc-tilde")
    rec("command-heredoc-tilde: body opaque and live tail passes",
        code == 0 and "nonexistent-binary-xyz" not in out
        and evaluated_of(out, "trigger.command_binary_resolves") == 3, out)
    code, out = run("command-heredoc-tilde-dead")
    rec("command-heredoc-tilde-dead: tail caught, body opaque",
        code == 1 and "corpus/absent-round17.md" in out
        and "nonexistent-binary-xyz" not in out, out)
    code, out = run("command-heredoc-tilde-misterm")
    rec("command-heredoc-tilde-misterm: bare EOF remains body",
        code == 0 and "absent-round17-misterm" not in out
        and evaluated_of(out, "trigger.command_binary_resolves") == 1, out)

    # Governance extraction is pure and hermetic: a same-line quoted dead
    # finding plus two schematics are excluded, while an unquoted dead path
    # fails.  Cross-line quote parity is deliberately not an exclusion.
    with tempfile.TemporaryDirectory(prefix="kotoba-governance-") as td:
        gov_repo = Path(td)
        (gov_repo / "corpus").mkdir()
        (gov_repo / "corpus" / "live.md").write_text("", encoding="utf-8")
        log_path = gov_repo / "LOG.md"
        log_path.write_text(
            "\"historical `corpus/dead-quoted.md` finding\"\n"
            "`corpus/live.md`\n`corpus/…/schematic.md`\n",
            encoding="utf-8")
        scorecard = gov_repo / "SCORECARD.md"
        scorecard.write_text(
            "`.ufo/reports/round-N/kotoba.md`\n", encoding="utf-8")
        status, evaluated, detail = check_governance_citations(gov_repo)
        rec("governance: quoted/schematic exclusions pass non-vacuously",
            status == "PASS" and evaluated == 1
            and "1 quoted meta-finding(s)" in detail
            and "2 schematic token(s)" in detail,
            (status, evaluated, detail))
        scorecard.write_text(
            "`.ufo/reports/round-N/kotoba.md`\n"
            "`corpus/dead-unquoted.md`\n", encoding="utf-8")
        status, evaluated, detail = check_governance_citations(gov_repo)
        rec("governance: unquoted dead path fails and is named",
            status == "FAIL" and evaluated == 2
            and "corpus/dead-unquoted.md" in detail,
            (status, evaluated, detail))
        scorecard.write_text(
            "`.ufo/reports/round-N/kotoba.md`\n", encoding="utf-8")
        log_path.write_text(
            "\"historical finding:\n`corpus/dead-cross-line.md`\n\"\n"
            "`corpus/live.md`\n", encoding="utf-8")
        status, evaluated, detail = check_governance_citations(gov_repo)
        rec("governance: cross-line quotes do not suppress a subject",
            status == "FAIL" and evaluated == 2
            and "corpus/dead-cross-line.md" in detail,
            (status, evaluated, detail))

    # An explicit relative --repo must be normalized before bounded `..`
    # hops; Path('.').parent otherwise stays '.', changing the verdict.
    with tempfile.TemporaryDirectory(prefix="kotoba-relative-repo-") as td:
        parent = Path(td)
        child = parent / "child"
        child.mkdir()
        (parent / "shared").mkdir()
        (parent / "shared" / "live.md").write_text("", encoding="utf-8")
        (child / "SKILL.md").write_text(
            "`../shared/live.md`\n", encoding="utf-8")
        old_cwd = Path.cwd()
        try:
            os.chdir(child)
            code, out = run_capture([
                "--skill", "SKILL.md", "--repo", ".",
                "--check", "trigger.citation_resolves"])
        finally:
            os.chdir(old_cwd)
        rec("relative --repo: bounded hop resolves from absolute repo root",
            code == 0
            and "PASS trigger.citation_resolves: evaluated 1" in out, out)

    for f in failures:
        print("self-test FAIL: %s" % f)
    print("%d failure(s) over %d assertions" % (len(failures), total))
    return 1 if failures else 0


# ---------------------------------------------------------------------------
# cli
# ---------------------------------------------------------------------------

def build_parser() -> argparse.ArgumentParser:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--repo", default=None,
                    help="repo root for command resolution (default: nearest "
                         "ancestor of --skill carrying .git, else its dir)")
    ap.add_argument("--skill", metavar="PATH", default=None,
                    help="target SKILL.md (default: <repo>/SKILL.md where "
                         "<repo> is the script's grandparent)")
    ap.add_argument("--map", metavar="PATH", default=None,
                    help="box-map JSON (default: <repo>/verifiers/%s when the "
                         "target is the repo SKILL.md, else "
                         "<skill-dir>/map.json; an absent foreign map makes "
                         "box_map_complete N/A, not exit 3)" % BASELINE_NAME)
    ap.add_argument("--vocabulary", metavar="PATH", default=None,
                    help="command-vocabulary JSON (default: "
                         "<verifiers>/%s)" % VOCAB_NAME)
    ap.add_argument("--max-lines", type=int, default=DEFAULT_MAX_LINES,
                    help="line-budget fallback when no checklist box states "
                         "a bound (default: %(default)s)")
    ap.add_argument("--check", action="append", choices=CHECK_IDS, default=None,
                    help="run only this check (repeatable); default: all")
    ap.add_argument("--self-test", action="store_true",
                    help="assert all checks and exit codes on fixtures only "
                         "(separate mode; rc is not comparable to a live run)")
    ap.add_argument("--json", action="store_true",
                    help="machine-readable output")
    return ap


def emit_json(results: list[dict], code: int, error: str | None = None) -> None:
    payload = {
        "checks": results,
        "pass": sum(1 for r in results if r["status"] == "PASS"),
        "fail": sum(1 for r in results if r["status"] == "FAIL"),
        "na": sum(1 for r in results if r["status"] == "N/A"),
        "exit_code": code,
    }
    if error is not None:
        payload["error"] = error
    print(json.dumps(payload, indent=2, sort_keys=True))


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    if args.self_test:
        return self_test()

    skill_path = Path(args.skill) if args.skill else DEFAULT_REPO / "SKILL.md"
    repo = (Path(args.repo).resolve() if args.repo
            else find_repo_root(skill_path))
    wanted = list(args.check) if args.check else list(CHECK_IDS)
    pinned = skill_path.resolve() == (DEFAULT_REPO / "SKILL.md").resolve()
    governance_enabled = skill_path.resolve() == (repo / "SKILL.md").resolve()

    box_map = None
    map_repo: Path | None = None
    map_na: str | None = None
    if "checklist.box_map_complete" in wanted:
        if args.map:
            map_path = Path(args.map)
            required = True
        elif pinned:
            map_path = DEFAULT_REPO / "verifiers" / BASELINE_NAME
            required = True
        else:
            map_path = skill_path.resolve().parent / "map.json"
            required = map_path.exists()
        map_repo = map_path.resolve().parent.parent
        try:
            box_map = load_map(map_path)
        except MapError as exc:
            if required:
                if args.json:
                    emit_json([], 3, str(exc))
                else:
                    print("ERROR %s" % exc, file=sys.stderr)
                return 3
            map_na = "no map pinned for %s (%s)" % (skill_path, exc)

    vocab = frozenset()
    if "trigger.command_binary_resolves" in wanted:
        vocab_path = Path(args.vocabulary) if args.vocabulary else (
            VERIFIERS_DIR / VOCAB_NAME)
        try:
            vocab = load_vocabulary(vocab_path)
        except EnvError as exc:
            if args.json:
                emit_json([], 2, str(exc))
            else:
                print("ERROR %s" % exc, file=sys.stderr)
            return 2

    try:
        text = read_text(skill_path, "target file")
    except EnvError as exc:
        if args.json:
            emit_json([], 2, str(exc))
        else:
            print("ERROR %s" % exc, file=sys.stderr)
        return 2

    lines = text.splitlines()
    fm = parse_frontmatter(lines)
    boxes, near_misses = extract_boxes(lines)

    results: list[dict] = []
    for cid in wanted:
        if cid == "checklist.box_map_complete":
            if map_na is not None:
                st, ev, detail = "N/A", 0, map_na
            else:
                st, ev, detail = check_box_map(
                    boxes, box_map, skill_path.name, near_misses, repo,
                    map_repo)
        elif cid == "trigger.frontmatter_parses":
            st, ev, detail = check_frontmatter(fm)
        elif cid == "trigger.name_directory":
            st, ev, detail = check_name_directory(fm, skill_path)
        elif cid == "trigger.literal_trigger_string":
            st, ev, detail = check_literal_trigger(fm)
        elif cid == "trigger.anti_trigger_clause":
            st, ev, detail = check_anti_trigger(fm)
        elif cid == "trigger.line_budget":
            st, ev, detail = check_line_budget(lines, boxes, args.max_lines)
        elif cid == "trigger.no_placeholder":
            st, ev, detail = check_no_placeholder(lines)
        elif cid == "trigger.citation_resolves":
            st, ev, detail = check_citation_resolves(lines, repo)
        elif cid == "governance.citation_resolves":
            if governance_enabled:
                st, ev, detail = check_governance_citations(repo)
            else:
                st, ev, detail = (
                    "N/A", 0,
                    "governance files are checked only with the repo SKILL.md")
        else:
            st, ev, detail = check_commands(lines, repo, vocab)
        results.append({"id": cid, "status": st,
                        "evaluated": ev, "detail": detail})

    any_fail = any(r["status"] == "FAIL" for r in results)
    any_subject = any(r["evaluated"] > 0 for r in results)
    code = 1 if (any_fail or not any_subject) else 0
    if args.json:
        emit_json(results, code)
    else:
        for r in results:
            print("%s %s: evaluated %d — %s"
                  % (r["status"], r["id"], r["evaluated"], r["detail"]))
    return code


if __name__ == "__main__":
    sys.exit(main())
