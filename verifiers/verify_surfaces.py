#!/usr/bin/env python3
"""verify_surfaces.py — machine check for the instruction-surface census.

The claim under test: the instruction-surface inventory derived from the
loader code of the two harness binaries on this host (``omp``, ``opencode``)
is complete — every loader-derived class is either governed by a table row or
excluded with a named reason — and the census artifact
(``corpus/knowledge/instruction-surface-census-round13.md``, ``--inventory``)
lists every declared class id explicitly in its ``## Class inventory`` section.

Two instruments:

1. Loader-class extraction.  ``strings -n 4`` dumps of the binaries are
   scanned for the registration-call shapes the bundles use::

       Id(e, "gemini", "GEMINI.md")              Cl(e, "github", "copilot-instructions.md")
       jDe(e, Pqr, "AGENTS.md")  with  var Pqr = "agents-md"

   i.e. ``(Id|Cl|jD[ef])(<v>, <group>, "<file>.md")`` — the file argument must
   end in ``.md`` — where ``<group>`` is either a quoted literal or a bundle
   identifier resolvable to a string constant in the same dump
   (``var|let|const X = "..."``; the minified bundles register the
   ``agents-md``/``claude-md`` groups through variables, so a quoted-only
   extractor would miss them).  An identifier that cannot be resolved is still
   reported as ``<harness>:<unresolved-var:NAME>/<file>`` so it FAILs rather
   than passing silently.

   DOCUMENTED LIMITS (the check proves set parity over this documented
   extraction, never existential completeness):
   - only ``.md``-suffixed registrations are extracted; non-``.md`` discovery
     registrations the dump actually contains (``omp:cursor/rules``,
     ``omp:gemini/settings.json``, ``omp:vscode/mcp.json``, …) are outside the
     set and must be declared by hand in the census as excluded;
   - loaders that are not ``(group, literal)``-shaped calls (e.g. opencode's
     ``InstructionContext.observe`` up-walk and ``instructions`` config array)
     are invisible to the extractor — baseline ``loader-config``/``prompt-text``
     entries cover them by declaration only;
   - a compiled-in call shape proves the loader path exists in the binary, not
     that it fires at runtime or reaches a prompt.

2. Inventory parity.  In the inventory file (``--inventory``, default
   ``<repo>/corpus/knowledge/instruction-surface-census-round13.md``), the
   ``## Class inventory`` section runs to the next ``^## `` heading.  Every
   table row (``|``-led line) inside it is scanned for backticked tokens
   matching ``(omp|opencode):[a-z0-9_-]+/[A-Za-z0-9_./-]+``.

A class id is ``<harness>:<group-or-kind>/<literal-or-key>``; each baseline
entry declares ``class_id``, ``harness``, ``literal``, ``context_kind``
(``loader-group`` | ``loader-config`` | ``loader-literal`` | ``prompt-text`` | ``template-list`` |
``doc``), ``verdict`` (``governed`` | ``excluded``), and — for excluded entries
only — ``reason``.

A class id is ``<harness>:<group-or-kind>/<literal-or-key>``; each baseline
entry declares ``class_id``, ``harness``, ``literal``, ``context_kind``
(``loader-group`` | ``loader-config`` | ``loader-literal`` | ``prompt-text`` |
``template-list`` | ``doc``), ``verdict`` (``governed`` | ``excluded``), and —
for excluded entries only — ``reason``.

``loader-literal`` marks classes the census declares by hand: registered in
the harness and the literal is present in the binary, but the registration is
not one of the extracted ``(group, file, .md)`` call shapes — e.g.
``omp:cursor/rules`` (``Cl(e,"cursor","rules")``, a directory pattern the
``.md`` extractor deliberately skips), ``opencode:read-hook/instructions``
(literal ``<system-reminder>``).  Probed like ``loader-config``: literal must
occur in the dump; no call-shape requirement.

surfaces.literal_present   every baseline entry with verdict in
    {governed, excluded} and context_kind in {loader-group, loader-config,
    loader-literal}: ``literal`` occurs in that harness's dump; for
    ``loader-group`` the ``(group, file)`` pair parsed from the class id
    additionally occurs as an extracted registration-call shape in the same
    dump (var-bound groups resolved as above).  Missing either -> FAIL.
surfaces.table_parity      the set of backticked class ids in the inventory's
    ``## Class inventory`` table rows must EXACTLY equal the set of baseline
    class ids: a baseline id with no inventory row -> FAIL "missing row"; an
    inventory id absent from the baseline -> FAIL "extra row".  Never passes
    vacuously: an empty id set (section absent or carrying no rows) vs an
    empty baseline -> FAIL, so an unlanded census is red, not green.
surfaces.excluded_reason   every ``excluded`` entry has a non-empty ``reason``
    AND its class id occurs as an inventory table-row id — the reader must
    see the exclusion, not only the JSON.
surfaces.literal_parity    per-id ID-LEVEL parity is not enough (round 13: a
    census row's *literal* cell rewritten to ``WRONG.md`` still exited 0 because
    ``table_parity`` compares ids and ``literal_present`` probes the *baseline's*
    literal).  For every '|'-led row inside ``## Class inventory`` whose FIRST
    cell is a backticked class id declared in the baseline, that row must have a
    second cell whose normalised text (whitespace stripped, surrounding
    backticks stripped) equals the baseline entry's ``literal``; a row with a
    declared id and no second cell is malformed and FAILs too.  The check FAILs
    when the section is absent, when no row carries a declared id (0-vs-0 is not
    a pass), and on a fixture whose census literal drifted.
surfaces.kind_parity     the same row contract for the THIRD cell: it must equal
    the baseline ``context_kind`` — the ``kind`` column's exact machine
    counterpart (round 13's mutation matrix rewrote it to another legitimate kind
    and exited 0).  Same non-vacuous rule: no declared-id row -> FAIL.
surfaces.opencode_extract  the harness whose machine check was vacuous (round 13
    ceiling): opencode's loaders are JS list/``join``/``filter`` shapes, so
    ``no_uncovered_class``'s ``(Id|Cl|jD[ef])(<v>, <group>, "<file>.md")``
    extractor finds nothing there by construction.  This check runs rules
    OC-1..OC-4 over the opencode dump instead and requires TWO-WAY parity: every
    declared opencode class id is produced by a rule, no rule produces an
    undeclared id, every rule matches, and an extraction producing 0 classes
    while the baseline declares opencode classes is a FAIL (the vacuity the check
    exists to kill).  An empty baseline therefore FAILs naming every extracted
    opencode class instead of passing on 0==0.

Exit: 0 all checks pass | 1 any FAIL | 2 environment unreadable (binary, dump
file, strings tool, inventory file, or an OS-level baseline read error — never
a pass) | 3 baseline missing or unparseable (bad JSON, missing keys, malformed
class id).  Read-only; deterministic.
"""
from __future__ import annotations

import argparse
import contextlib
import io
import json
import re
import subprocess
import sys
from pathlib import Path

DEFAULT_REPO = Path(__file__).resolve().parent.parent
FIXTURES = Path(__file__).resolve().parent / "fixtures" / "surfaces"

DEFAULT_BINARIES = {
    "omp": "/home/vgpnk/.local/bin/omp",
    "opencode": "/home/vgpnk/.opencode/bin/opencode",
}
DEFAULT_INVENTORY = "corpus/knowledge/instruction-surface-census-round13.md"
HARNESS_IDS = ("omp", "opencode")
LOADER_KINDS = ("loader-group", "loader-config", "loader-literal")
CONTEXT_KINDS = LOADER_KINDS + ("prompt-text", "template-list", "doc")
VERDICTS = ("governed", "excluded")

# Registration calls: a callee allowlist of the minified names the loader
# bundles have used (`Id`, `Cl`, `jDe`, `jDf` up to the 2026-09-28 build; the
# 2026-10-14 rebuild renamed the same two-level resolution path to `Tl`, `dr`
# — the callee name is minification-volatile and is the FIRST thing to re-pin
# on a binary bump) with a constant first arg, then either a quoted group or
# an identifier group, then a quoted *.md file, followed by a comma or
# close-paren (wrapped calls like `s(Cl(...), "project", "text")` are the norm
# in the bundle).
CALL_RE = re.compile(
    r"(?<![A-Za-z0-9_$])(?:Id|Cl|jD[ef]|Tl|dr|GW)\(\s*[^\s,()]+\s*,\s*"
    r'(?:"([a-z0-9_-]+)"|([A-Za-z_$][A-Za-z0-9_$]*))\s*,\s*'
    r'"([A-Za-z0-9_./-]+\.md)"(?=\s*[,)])'
)
CALLEE_SHAPE = "(Id|Cl|jD[ef]|Tl|dr|GW)(<v>, <group>, \"<file>.md\")"
# Identifier -> string bindings anywhere in the dump (`var Pqr = "agents-md"`,
# second declarators like `, Zou = "AGENTS.md"`, plain `X = "..."`).
ASSIGN_RE = re.compile(
    r'(?<![A-Za-z0-9_$.])([A-Za-z_$][A-Za-z0-9_$]*)\s*=\s*"([^"\\\n]{1,80})"'
)
CLASS_ID_RE = re.compile(r"^(omp|opencode):([a-z0-9_-]+)/([A-Za-z0-9_./-]+)$")
SECTION_HEADING_RE = re.compile(r"^##\s+Class inventory\b")
NEXT_HEADING_RE = re.compile(r"^##\s")
BACKTICK_ID_RE = re.compile(r"`((?:omp|opencode):[a-z0-9_-]+/[A-Za-z0-9_./-]+)`")

CHECK_IDS = (
    "surfaces.literal_present",
    "surfaces.no_uncovered_class",
    "surfaces.opencode_extract",
    "surfaces.table_parity",
    "surfaces.literal_parity",
    "surfaces.kind_parity",
    "surfaces.excluded_reason",
)

# Class-id cell of an inventory table row: exactly one backticked class id.
ROW_ID_CELL_RE = re.compile(r"^`((?:omp|opencode):[a-z0-9_-]+/[A-Za-z0-9_./-]+)`$")


class EnvError(Exception):
    """Environment cannot answer (exit 2)."""


class BaselineError(Exception):
    """Baseline missing or unparseable (exit 3)."""


# ---------------------------------------------------------------------------
# loaders: strings dumps, inventory, baseline
# ---------------------------------------------------------------------------

def read_text(path: Path, what: str) -> str:
    try:
        return path.read_text(encoding="utf-8", errors="replace")
    except FileNotFoundError:
        raise EnvError("%s not found: %s" % (what, path))
    except OSError as exc:
        raise EnvError("%s unreadable: %s (%s)" % (what, path, exc))


def dump_via_strings(binary: Path, harness: str) -> str:
    if not binary.is_file():
        raise EnvError("%s binary not found: %s" % (harness, binary))
    try:
        proc = subprocess.run(
            ["strings", "-n", "4", str(binary)],
            capture_output=True, timeout=600,
        )
    except FileNotFoundError:
        raise EnvError("`strings` tool unavailable on this host")
    except OSError as exc:
        raise EnvError("cannot run strings on %s: %s" % (binary, exc))
    if proc.returncode != 0:
        raise EnvError(
            "strings -n 4 %s exited %d: %s"
            % (binary, proc.returncode, proc.stderr[:200].decode("utf-8", "replace"))
        )
    return proc.stdout.decode("utf-8", "replace")


def load_dump(args: argparse.Namespace, harness: str) -> str:
    given = getattr(args, "%s_strings" % harness)
    if given is not None:
        return read_text(Path(given), "%s strings dump" % harness)
    return dump_via_strings(Path(getattr(args, "%s_binary" % harness)), harness)


def load_baseline(path: Path) -> list[dict]:
    try:
        raw = path.read_text(encoding="utf-8")
    except FileNotFoundError:
        raise BaselineError("baseline not found: %s" % path)
    except OSError as exc:
        raise EnvError("baseline unreadable: %s (%s)" % (path, exc))
    try:
        data = json.loads(raw)
    except json.JSONDecodeError as exc:
        raise BaselineError("baseline unparseable: %s (%s)" % (path, exc))
    if not isinstance(data, dict) or not isinstance(data.get("classes"), list):
        raise BaselineError(
            "baseline unparseable: top level must be an object with a classes array"
        )
    entries = []
    seen: set[str] = set()
    for i, e in enumerate(data["classes"]):
        where = "classes[%d]" % i
        if not isinstance(e, dict):
            raise BaselineError("%s: not an object" % where)
        for key in ("class_id", "harness", "literal", "context_kind", "verdict"):
            if not isinstance(e.get(key), str) or not e.get(key):
                raise BaselineError("%s: missing/empty string field %r" % (where, key))
        if e["harness"] not in HARNESS_IDS:
            raise BaselineError("%s: harness %r not in %s" % (where, e["harness"], HARNESS_IDS))
        if e["context_kind"] not in CONTEXT_KINDS:
            raise BaselineError("%s: context_kind %r unknown" % (where, e["context_kind"]))
        if e["verdict"] not in VERDICTS:
            raise BaselineError("%s: verdict %r unknown" % (where, e["verdict"]))
        m = CLASS_ID_RE.match(e["class_id"])
        if not m:
            raise BaselineError(
                "%s: class_id %r does not match "
                "<harness>:<group-or-kind>/<literal-or-key>" % (where, e["class_id"])
            )
        if m.group(1) != e["harness"]:
            raise BaselineError(
                "%s: class_id prefix %r disagrees with harness %r"
                % (where, m.group(1), e["harness"])
            )
        if e["class_id"] in seen:
            raise BaselineError("%s: duplicate class_id %r" % (where, e["class_id"]))
        seen.add(e["class_id"])
        entries.append(
            {
                "class_id": e["class_id"],
                "harness": e["harness"],
                "group": m.group(2),
                "file": m.group(3),
                "literal": e["literal"],
                "context_kind": e["context_kind"],
                "verdict": e["verdict"],
                "reason": e.get("reason") or "",
            }
        )
    return entries


# ---------------------------------------------------------------------------
# extraction model (pure; shared by literal_present and no_uncovered_class)
# ---------------------------------------------------------------------------

def constant_table(dump: str) -> dict[str, str]:
    """First-seen identifier -> string binding; conflicting rebinds are dropped
    (marked unresolvable) rather than guessed."""
    table: dict[str, str] = {}
    conflicts: set[str] = set()
    for name, value in ASSIGN_RE.findall(dump):
        if name in conflicts:
            continue
        if name in table and table[name] != value:
            conflicts.add(name)
            del table[name]
        else:
            table.setdefault(name, value)
    return table


def extract_classes(dump: str, harness: str) -> set[tuple[str, str]]:
    """All (group, file) pairs from `.md`-suffixed registration-call shapes.
    Identifier group args are resolved through the dump's constant table;
    unresolvable ones surface as a ``<unresolved-var:NAME>`` group so they
    cannot pass silently."""
    consts = constant_table(dump)
    pairs: set[tuple[str, str]] = set()
    for quoted, ident, filename in CALL_RE.findall(dump):
        if quoted:
            group = quoted
        elif ident in consts:
            group = consts[ident]
        else:
            group = "<unresolved-var:%s>" % ident
        pairs.add((group, filename))
    return pairs


# ---------------------------------------------------------------------------
# opencode: instruction-service extraction (rules OC-1..OC-4)
#
# opencode's loaders are not ``(group, file)`` registration calls; they are
# minified JS list / ``path.join`` / array-``filter`` shapes inside the Bun
# bundle's readable chunks (``strings -n 4`` keeps whole chunks that contain no
# non-printable byte).  The rules below DERIVE class ids from those shapes where
# the shape carries the name (OC-1, OC-2) and WITNESS the two ids whose identity
# is a behaviour rather than a literal (OC-3's two entries, OC-4).  Every rule is
# fail-closed: an absent anchor contributes nothing and is reported by name, so a
# vanished loader FAILs rather than silently shrinking the extraction set.
#
# DOCUMENTED LIMITS: this is an extraction rule set, not existential
# completeness — a loader shape minified differently, or one reached through a
# variable the dump resolves differently, is out of the set.  The check proves
# (a) each declared opencode class id is produced by a rule, (b) no rule produces
# an undeclared id, (c) a rule whose anchor is gone reports itself unmatched.

# OC-1: the PROJECT source of the `opencode.config.instruction` plugin
# (opencode 2.x, post-2026-09-28 rewrite: the AGENTS.md/CLAUDE.md/CONTEXT.md
# name-priority array is gone; the loader is Effect-gen, all-match walk-up).
# Live shapes: `ConfigInstructionPlugin.projectSource` +
# `targets:["AGENTS.md"]` in the same code path (`i.up({targets:["AGENTS.md"],
# start:<cwd>,stop:<project>,type:"file"})`).
OC_PROJECT_FN = "ConfigInstructionPlugin.projectSource"
OC_PROJECT_TARGETS = 'targets:["AGENTS.md"]'
OC_MD_NAME_RE = re.compile(r'"([A-Za-z0-9_.-]+\.md)"')

# OC-2: the GLOBAL source — `<opencode config dir>/AGENTS.md`, resolved via
# `j5(r.config,"AGENTS.md")` inside `opencode.config.instruction` (the
# `.claude/CLAUDE.md` candidate no longer exists).
OC_GLOBAL_JOIN_RE = re.compile(
    r'[A-Za-z_$][A-Za-z0-9_$]*\(r\.config\s*,\s*"AGENTS\.md"\)')

# OC-3: the config `instructions` field — schema-declared ("Additional paths
# or URLs supplying ambient instructions"). The field is declared; a loader
# consumer is NOT proven on this binary (round-18 excluded class).
OC_AMBIENT_SCHEMA = 'ambient instructions'

# OC-4: the READ-TOOL channel — `ReadTool.Plugin` walks up from every read
# file to the project root for AGENTS.md (`targets:[a$]` where `a$` is the
# "AGENTS.md" constant) and calls `SessionInstructions.load`, which renders
# `Instructions from: <path>` synthetic entries.
OC_READ_FN = "ReadTool.Plugin"
OC_READ_TARGETS = 'targets:[a$]'
OC_READ_CONST = 'a$="AGENTS.md"'
OC_SESSION_LOAD = 'SessionInstructions.load'

# OC-5: resolution switch witness — the project source is disabled only via
# config `project:false` (env `OPENCODE_CONFIG_PROJECT_DISABLE` or
# `OPENCODE_DISABLE_PROJECT_CONFIG`), wired as `V7({project:i.config?.project})`.
OC_ENV_PROJECT_CONFIG = "OPENCODE_DISABLE_PROJECT_CONFIG"
OC_ENV_PROJECT_CONFIG_2 = "OPENCODE_CONFIG_PROJECT_DISABLE"

# OC-6: the experimental API instruction entries —
# `session.instructions.entry.{list,put,remove}` over
# `/api/experimental/session/:sessionID/instructions/entries` — API-managed
# durable entries announced to the model at the next step boundary.
OC_API_ROUTE = "/instructions/entries"
OC_API_ID = "session.instructions.entry.put"


def extract_opencode_classes(dump: str) -> tuple[set[str], list[dict]]:
    """(class ids, per-rule report) for the opencode dump.

    Rule ids and the class ids they are responsible for are declared here, so a
    rule that stops matching names the classes it can no longer produce."""
    ids: set[str] = set()
    report: list[dict] = []

    def rule(rule_id: str, owns: list[str], matched: bool, anchors: list[str]) -> None:
        missing = [] if matched else list(anchors)
        report.append({"rule_id": rule_id, "owns": list(owns), "matched": matched,
                       "anchors": list(anchors), "missing": missing})
        if matched:
            ids.update(owns)

    # OC-1 — project walk-up, all-match AGENTS.md
    project = OC_PROJECT_FN in dump and OC_PROJECT_TARGETS in dump
    rule("OC-1", ["opencode:project/AGENTS.md"], project,
         [OC_PROJECT_FN, OC_PROJECT_TARGETS])

    # OC-2 — global `<config>/AGENTS.md`
    glob = OC_GLOBAL_JOIN_RE.search(dump) is not None
    rule("OC-2", ["opencode:config/AGENTS.md"], glob,
         ['X(r.config,"AGENTS.md")'])

    # OC-3 — declared ambient-instructions field (schema anchor only; the
    # loader consumer is unproven — recorded as its own class on that basis).
    ambient = OC_AMBIENT_SCHEMA in dump
    rule("OC-3", ["opencode:config/instructions"], ambient,
         ['"ambient instructions" schema annotation'])

    # OC-4 — read-tool channel: every read walks up for AGENTS.md files
    # outside the project and publishes them through SessionInstructions.load.
    read_hook = (OC_READ_FN in dump and OC_READ_TARGETS in dump
                 and OC_READ_CONST in dump and OC_SESSION_LOAD in dump)
    rule("OC-4", ["opencode:read-hook/AGENTS.md"], read_hook,
         [OC_READ_FN, OC_READ_TARGETS, OC_READ_CONST, OC_SESSION_LOAD])

    # OC-5 — resolution switch (owns no class id; witnesses the env gate)
    switch = (OC_ENV_PROJECT_CONFIG in dump or OC_ENV_PROJECT_CONFIG_2 in dump)
    rule("OC-5", [], switch,
         ["%s | %s" % (OC_ENV_PROJECT_CONFIG, OC_ENV_PROJECT_CONFIG_2)])

    # OC-6 — API-managed instruction entries
    api = OC_API_ROUTE in dump and OC_API_ID in dump
    rule("OC-6", ["opencode:api-entries/instructions"], api,
         [OC_API_ROUTE, OC_API_ID])

    return ids, report


# ---------------------------------------------------------------------------
# inventory section
# ---------------------------------------------------------------------------

def inventory_section(inventory_text: str) -> tuple[list[tuple[int, str]] | None, str]:
    """(rows, problem).  Section = the '## Class inventory' line through the line
    before the next '^## ' heading; rows = (1-based lineno, line) for '|'-led
    lines inside it.  None -> heading absent."""
    lines = inventory_text.splitlines()
    start = None
    for i, line in enumerate(lines):
        if SECTION_HEADING_RE.match(line):
            start = i + 1
            break
    if start is None:
        return None, "no '## Class inventory' heading in inventory file"
    end = len(lines)
    for i in range(start, len(lines)):
        if NEXT_HEADING_RE.match(lines[i]):
            end = i
            break
    return [(i + 1, lines[i]) for i in range(start, end)
            if lines[i].lstrip().startswith("|")], ""


def inventory_class_ids(inventory_text: str) -> tuple[set[str] | None, str]:
    """(ids, problem).  Backticked class ids found in '|'-led table rows inside
    the '## Class inventory' section.  None -> heading absent."""
    rows, problem = inventory_section(inventory_text)
    if rows is None:
        return None, problem
    ids: set[str] = set()
    for _, ln in rows:
        ids.update(BACKTICK_ID_RE.findall(ln))
    return ids, ""


def inventory_rows(inventory_text: str) -> tuple[list[dict] | None, str]:
    """(rows, problem) where each row is {lineno, id, cells}.  ``cells`` are the
    '|'-separated cells of the table row in order (leading/trailing empties from
    the outer pipes removed), whitespace-stripped; ``id`` is set when the FIRST
    cell is exactly one backticked class id (else None).  None -> heading
    absent.  Non-table lines are skipped; the header row (first cell 'class_id'
    / 'Class id') carries no id cell and is naturally skipped."""
    raw, problem = inventory_section(inventory_text)
    if raw is None:
        return None, problem
    rows: list[dict] = []
    for lineno, ln in raw:
        cells = [c.strip() for c in ln.strip().strip("|").split("|")]
        m = ROW_ID_CELL_RE.match(cells[0]) if cells else None
        rows.append({"lineno": lineno, "id": m.group(1) if m else None,
                     "cells": cells, "line": ln})
    return rows, ""


# ---------------------------------------------------------------------------
# checks: each returns (ok, detail)
# ---------------------------------------------------------------------------

def check_literal_present(entries: list[dict], dumps: dict[str, str],
                          extracted: dict[str, set[tuple[str, str]]]) -> tuple[bool, str]:
    problems = []
    checked = 0
    for e in entries:
        if e["context_kind"] not in LOADER_KINDS:
            continue
        checked += 1
        dump = dumps[e["harness"]]
        if e["literal"] not in dump:
            problems.append(
                "%s (literal %r absent from %s dump)"
                % (e["class_id"], e["literal"], e["harness"])
            )
            continue
        if e["context_kind"] == "loader-group" and (
            (e["group"], e["file"]) not in extracted[e["harness"]]
        ):
            problems.append(
                "%s (no %s call shape for (%s, %s) in %s dump)"
                % (e["class_id"], CALLEE_SHAPE, e["group"], e["file"], e["harness"])
            )
    if problems:
        return False, "%d loader literal(s) not verifiable: %s" % (
            len(problems), "; ".join(problems))
    return True, "%d loader-kind entr%s verified against the dumps" % (
        checked, "y" if checked == 1 else "ies")


def check_no_uncovered_class(entries: list[dict],
                             extracted: dict[str, set[tuple[str, str]]]) -> tuple[bool, str]:
    declared = {e["class_id"] for e in entries}
    found: set[str] = set()
    for harness in HARNESS_IDS:
        found |= {"%s:%s/%s" % (harness, g, f) for g, f in extracted[harness]}
    uncovered = sorted(found - declared)
    if uncovered:
        return False, "%d loader class(es) undeclared in baseline: %s" % (
            len(uncovered), ", ".join(uncovered))
    return True, "all %d extracted loader class(es) declared" % len(found)


def check_table_parity(entries: list[dict],
                       inv: tuple[set[str] | None, str]) -> tuple[bool, str]:
    section_ids, problem = inv
    baseline_ids = {e["class_id"] for e in entries}
    if section_ids is None:
        return False, problem
    missing = sorted(baseline_ids - section_ids)
    extra = sorted(section_ids - baseline_ids)
    problems = []
    if missing:
        problems.append("missing row(s) for baseline id(s): %s" % ", ".join(missing))
    if extra:
        problems.append("extra row(s) not in baseline: %s" % ", ".join(extra))
    if problems:
        return False, "; ".join(problems)
    if not baseline_ids:
        return False, ("0 class-id rows in inventory and 0 baseline entries — "
                       "vacuous parity is not a pass (census not landed)")
    return True, "inventory id set == baseline id set (%d id%s)" % (
        len(baseline_ids), "" if len(baseline_ids) == 1 else "s")


def check_literal_parity(entries: list[dict],
                         rows: tuple[list[dict] | None, str]) -> tuple[bool, str]:
    """Per-id census-literal parity: the census row's second cell must equal the
    baseline literal for that id.  Closes the round-13 escape where a row's
    literal cell could be rewritten while ``table_parity`` (ids) and
    ``literal_present`` (baseline literal) both stayed green."""
    row_list, problem = rows
    if row_list is None:
        return False, problem + " — census literals unverifiable"
    by_id = {e["class_id"]: e["literal"] for e in entries}
    checked = 0
    problems: list[str] = []
    for row in row_list:
        ids_anywhere = BACKTICK_ID_RE.findall(row["line"])
        cid = row["id"]
        if cid is None:
            if ids_anywhere:
                problems.append(
                    "line %d carries class id(s) %s outside the first cell — "
                    "the literal comparison cannot be anchored"
                    % (row["lineno"], ", ".join(sorted(set(ids_anywhere)))))
            continue
        if cid not in by_id:
            continue  # undeclared/extra ids are table_parity's finding
        cells = row["cells"]
        if len(cells) < 2 or not cells[1]:
            problems.append(
                "%s (line %d: row has no literal cell — expected %r)"
                % (cid, row["lineno"], by_id[cid]))
            continue
        got = cells[1].strip().strip("`").strip()
        want = by_id[cid]
        if got != want:
            problems.append(
                "%s (line %d: census literal %r != baseline literal %r)"
                % (cid, row["lineno"], got, want))
            continue
        checked += 1
    if problems:
        return False, "%d census row literal(s) disagree with the baseline: %s" % (
            len(problems), "; ".join(problems))
    if checked == 0:
        return False, ("0 inventory rows carry a baseline class id — vacuous "
                       "literal parity is not a pass (census not landed)")
    return True, "%d inventory row literal(s) match the baseline per id" % checked


def check_opencode_extract(entries: list[dict], dump: str) -> tuple[bool, str]:
    """Two-way parity for opencode: every declared class id must be produced by a
    rule, no rule may produce an undeclared id, every rule must match, and an
    extraction that produces nothing while the baseline declares opencode classes
    is the vacuity this check exists to kill (never a pass)."""
    extracted, report = extract_opencode_classes(dump)
    declared = {e["class_id"] for e in entries if e["harness"] == "opencode"}
    problems: list[str] = []
    if not extracted:
        problems.append(
            "vacuity: extraction produced 0 class(es) from %d rule(s); opencode is a "
            "target harness of this lane, so 0 extracted classes with %d declared "
            "is a FAIL, never a pass" % (len(report), len(declared)))
    missing = sorted(declared - extracted)
    if missing:
        problems.append("declared opencode class(es) produced by no rule: %s"
                        % ", ".join(missing))
    extra = sorted(extracted - declared)
    if extra:
        problems.append("extracted opencode class(es) undeclared in baseline: %s"
                        % ", ".join(extra))
    unmatched = ["%s (owns %s; missing %s)"
                 % (r["rule_id"],
                    ", ".join(r["owns"]) if r["owns"] else "no class id (shape witness)",
                    " + ".join(r["missing"]))
                 for r in report if not r["matched"]]
    if unmatched:
        problems.append("rule(s) matched nothing: %s" % "; ".join(unmatched))
    if problems:
        return False, "; ".join(problems)
    return True, ("opencode extraction %d/%d declared class(es) from %d/%d rules "
                  "(%s)" % (len(declared), len(declared),
                            sum(1 for r in report if r["matched"]), len(report),
                            ", ".join(r["rule_id"] for r in report)))


def check_kind_parity(entries: list[dict],
                      rows: tuple[list[dict] | None, str]) -> tuple[bool, str]:
    """Per-id census-kind parity: the census row's THIRD cell must equal the
    baseline ``context_kind``.  Round 13's mutation matrix left the ``kind``
    column unchecked (a rewrite to another legitimate kind exited 0); the cell has
    an exact machine counterpart, so it is checked like the literal."""
    row_list, problem = rows
    if row_list is None:
        return False, problem + " — census kinds unverifiable"
    by_id = {e["class_id"]: e["context_kind"] for e in entries}
    checked = 0
    problems: list[str] = []
    for row in row_list:
        cid = row["id"]
        if cid is None or cid not in by_id:
            continue  # misplaced/undeclared ids are literal_parity's finding
        cells = row["cells"]
        if len(cells) < 3 or not cells[2]:
            problems.append(
                "%s (line %d: row has no kind cell — expected %r)"
                % (cid, row["lineno"], by_id[cid]))
            continue
        got = cells[2].strip().strip("`").strip()
        if got != by_id[cid]:
            problems.append(
                "%s (line %d: census kind %r != baseline context_kind %r)"
                % (cid, row["lineno"], got, by_id[cid]))
            continue
        checked += 1
    if problems:
        return False, "%d census row kind(s) disagree with the baseline: %s" % (
            len(problems), "; ".join(problems))
    if checked == 0:
        return False, ("0 inventory rows carry a baseline class id — vacuous "
                       "kind parity is not a pass (census not landed)")
    return True, "%d inventory row kind(s) match the baseline per id" % checked


def check_excluded_reason(entries: list[dict],
                          inv: tuple[set[str] | None, str]) -> tuple[bool, str]:
    excluded = [e for e in entries if e["verdict"] == "excluded"]
    section_ids, problem = inv
    problems = []
    if section_ids is None and excluded:
        problems.append(problem + " — excluded id(s) unverifiable")
    else:
        not_shown = sorted(e["class_id"] for e in excluded
                           if e["class_id"] not in (section_ids or set()))
        if not_shown:
            problems.append(
                "excluded id(s) not shown in inventory: %s" % ", ".join(not_shown))
    no_reason = sorted(e["class_id"] for e in excluded if not e["reason"].strip())
    if no_reason:
        problems.append("excluded without reason: %s" % ", ".join(no_reason))
    if problems:
        return False, "; ".join(problems)
    return True, "%d excluded entr%s, all reasoned and listed in the inventory" % (
        len(excluded), "y" if len(excluded) == 1 else "ies")


# ---------------------------------------------------------------------------
# self-test: run the CLI surface against committed fixtures only
# ---------------------------------------------------------------------------

def run_capture(argv: list[str]) -> tuple[int, str]:
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        code = main(argv)
    return code, buf.getvalue()


def self_test() -> int:
    failures: list[str] = []
    total = 0

    def rec(what: str, ok: bool, got: object) -> None:
        nonlocal total
        total += 1
        if not ok:
            failures.append("%s: got %r" % (what, got))

    fx = str(FIXTURES)
    omp_clean = fx + "/strings-omp-clean.txt"
    oc_clean = fx + "/strings-opencode-clean.txt"
    base_clean = fx + "/baseline-clean.json"
    inv_clean = fx + "/inventory-clean.md"

    def run(omp_dump: str = omp_clean, inventory: str = inv_clean,
            baseline: str = base_clean, oc_dump: str = oc_clean) -> tuple[int, str]:
        return run_capture(
            ["--repo", fx, "--omp-strings", omp_dump,
             "--opencode-strings", oc_dump,
             "--baseline", baseline, "--inventory", inventory])

    # (a) clean fixture set -> exit 0, all four checks PASS
    code, out = run()
    rec("clean: exit 0", code == 0, code)
    for cid in CHECK_IDS:
        rec("clean: PASS %s" % cid, ("PASS %s:" % cid) in out, out)

    # (b) extra undeclared loader class -> exit 1, no_uncovered_class names it
    code, out = run(omp_dump=fx + "/strings-extra-class.txt")
    rec("extra-class: exit 1", code == 1, code)
    rec("extra-class: FAIL no_uncovered_class",
        "FAIL surfaces.no_uncovered_class:" in out, out)
    rec("extra-class: names omp:foo/FOO.md", "omp:foo/FOO.md" in out, out)

    # (c) declared loader shape dropped -> exit 1, literal_present names it
    code, out = run(omp_dump=fx + "/strings-drop-class.txt")
    rec("drop-class: exit 1", code == 1, code)
    rec("drop-class: FAIL literal_present",
        "FAIL surfaces.literal_present:" in out, out)
    rec("drop-class: names omp:gemini/GEMINI.md",
        "omp:gemini/GEMINI.md" in out, out)

    # (d) inventory drops a governed class-id row -> exit 1, table_parity
    code, out = run(inventory=fx + "/inventory-missing-row.md")
    rec("missing-row: exit 1", code == 1, code)
    rec("missing-row: FAIL table_parity",
        "FAIL surfaces.table_parity:" in out, out)
    rec("missing-row: names omp:gemini/GEMINI.md",
        "omp:gemini/GEMINI.md" in out, out)

    # (d2) inventory carries an extra class-id row -> exit 1, table_parity
    code, out = run(inventory=fx + "/inventory-extra-row.md")
    rec("extra-row: exit 1", code == 1, code)
    rec("extra-row: FAIL table_parity",
        "FAIL surfaces.table_parity:" in out, out)
    rec("extra-row: names omp:github/prompts",
        "omp:github/prompts" in out, out)

    # (d2b) census row literal drifted from the baseline -> exit 1, literal_parity
    code, out = run(inventory=fx + "/inventory-literal-drift.md")
    rec("literal-drift: exit 1", code == 1, code)
    rec("literal-drift: FAIL literal_parity",
        "FAIL surfaces.literal_parity:" in out, out)
    rec("literal-drift: names omp:gemini/GEMINI.md",
        "omp:gemini/GEMINI.md" in out, out)

    # (d2c) declared id whose row has no literal cell -> exit 1, literal_parity
    code, out = run(inventory=fx + "/inventory-no-literal-cell.md")
    rec("no-literal-cell: exit 1", code == 1, code)
    rec("no-literal-cell: FAIL literal_parity",
        "FAIL surfaces.literal_parity:" in out, out)
    rec("no-literal-cell: names omp:gemini/GEMINI.md",
        "omp:gemini/GEMINI.md" in out, out)
    rec("no-literal-cell: names omp:cursor/rules",
        "omp:cursor/rules" in out, out)

    # (d2d) declared id carried outside the first cell -> exit 1, literal_parity
    code, out = run(inventory=fx + "/inventory-id-not-first.md")
    rec("id-not-first: exit 1", code == 1, code)
    rec("id-not-first: FAIL literal_parity",
        "FAIL surfaces.literal_parity:" in out, out)
    rec("id-not-first: names omp:gemini/GEMINI.md",
        "omp:gemini/GEMINI.md" in out, out)
    rec("id-not-first: table_parity still PASS",
        "PASS surfaces.table_parity:" in out, out)

    # (e) excluded entry with empty reason -> exit 1, excluded_reason
    code, out = run(baseline=fx + "/baseline-excluded-noreason.json")
    rec("noreason: exit 1", code == 1, code)
    rec("noreason: FAIL excluded_reason",
        "FAIL surfaces.excluded_reason:" in out, out)
    rec("noreason: names omp:claude-md/CLAUDE.md",
        "omp:claude-md/CLAUDE.md" in out, out)

    # (e2) excluded id absent from the inventory -> exit 1, excluded_reason
    code, out = run(inventory=fx + "/inventory-missing-excluded-row.md")
    rec("missing-excluded-row: exit 1", code == 1, code)
    rec("missing-excluded-row: FAIL excluded_reason",
        "FAIL surfaces.excluded_reason:" in out, out)
    rec("missing-excluded-row: names omp:claude-md/CLAUDE.md",
        "omp:claude-md/CLAUDE.md" in out, out)

    # (h) empty inventory section vs empty baseline -> never a vacuous pass
    code, out = run_capture(
        ["--repo", fx, "--omp-strings", fx + "/strings-empty.txt",
         "--opencode-strings", fx + "/strings-empty.txt",
         "--baseline", fx + "/baseline-empty.json",
         "--inventory", fx + "/inventory-empty.md"])
    rec("vacuous-parity: exit 1", code == 1, code)
    rec("vacuous-parity: FAIL table_parity",
        "FAIL surfaces.table_parity:" in out, out)
    rec("vacuous-parity: FAIL literal_parity",
        "FAIL surfaces.literal_parity:" in out, out)

    # (f) missing dump path -> exit 2, never a pass
    code, out = run_capture(
        ["--repo", fx, "--omp-strings", fx + "/NO-SUCH.txt",
         "--opencode-strings", oc_clean,
         "--baseline", base_clean, "--inventory", inv_clean])
    rec("missing dump: exit 2", code == 2, code)

    # (oc) each rule's anchor removed -> exit 1, opencode_extract names its class
    for fixture, named in (
            ("strings-opencode-drop-oc1.txt", "opencode:project/AGENTS.md"),
            ("strings-opencode-drop-oc2.txt", "opencode:config/AGENTS.md"),
            ("strings-opencode-drop-oc3.txt", "opencode:config/instructions"),
            ("strings-opencode-drop-oc4.txt", "opencode:read-hook/AGENTS.md"),
            ("strings-opencode-drop-oc5.txt", "OC-5"),
            ("strings-opencode-drop-oc6.txt", "opencode:api-entries/instructions")):
        code, out = run(oc_dump=fx + "/" + fixture)
        rec("%s: exit 1" % fixture, code == 1, code)
        rec("%s: FAIL opencode_extract" % fixture,
            "FAIL surfaces.opencode_extract:" in out, out)
        rec("%s: names %s" % (fixture, named), named in out, out)

    # (oc+) anchor-adjacent shapes that are NOT rule anchors must extract
    # nothing extra — the drop-one matrix stays green, so exit 0 here proves
    # the rules are anchored, not literal-greedy.
    code, out = run(oc_dump=fx + "/strings-opencode-extra.txt")
    rec("oc-extra: exit 0", code == 0, code)

    # (oc0) empty baseline + a real anchor dump -> exit 1 naming every extracted
    # opencode class (never a pass on 0==0)
    code, out = run(baseline=fx + "/baseline-oc-empty.json")
    rec("oc-empty-baseline: exit 1", code == 1, code)
    rec("oc-empty-baseline: FAIL opencode_extract",
        "FAIL surfaces.opencode_extract:" in out, out)
    for cid in ("opencode:project/AGENTS.md", "opencode:config/instructions",
                "opencode:api-entries/instructions"):
        rec("oc-empty-baseline: names %s" % cid, cid in out, out)

    # (oc0b) anchor-less dump while the baseline declares opencode classes -> the
    # zero-extraction vacuity FAIL (a vanishing rule set is not a pass)
    code, out = run(oc_dump=fx + "/strings-empty.txt")
    rec("oc-zero-extraction: exit 1", code == 1, code)
    rec("oc-zero-extraction: FAIL opencode_extract",
        "FAIL surfaces.opencode_extract:" in out, out)
    rec("oc-zero-extraction: says vacuity", "vacuity" in out, out)

    # (f2) missing inventory file -> exit 2
    code, out = run_capture(
        ["--repo", fx, "--omp-strings", omp_clean,
         "--opencode-strings", oc_clean,
         "--baseline", base_clean, "--inventory", fx + "/NO-SUCH.md"])
    rec("missing inventory: exit 2", code == 2, code)

    # (g) missing baseline -> exit 3
    code, out = run_capture(
        ["--repo", fx, "--omp-strings", omp_clean,
         "--opencode-strings", oc_clean,
         "--baseline", fx + "/NO-SUCH.json", "--inventory", inv_clean])
    rec("missing baseline: exit 3", code == 3, code)

    for f in failures:
        print("self-test FAIL: %s" % f)
    print("%d failure(s) over %d assertions" % (len(failures), total))
    return 1 if failures else 0


# ---------------------------------------------------------------------------
# cli
# ---------------------------------------------------------------------------

def build_parser() -> argparse.ArgumentParser:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--repo", default=str(DEFAULT_REPO),
                    help="repo root for default paths (default: script's grandparent)")
    ap.add_argument("--omp-strings", metavar="PATH",
                    help="pre-made `strings -n 4` dump for the omp binary")
    ap.add_argument("--opencode-strings", metavar="PATH",
                    help="pre-made `strings -n 4` dump for the opencode binary")
    ap.add_argument("--omp-binary", metavar="PATH", default=DEFAULT_BINARIES["omp"],
                    help="omp binary to dump when --omp-strings is absent")
    ap.add_argument("--opencode-binary", metavar="PATH",
                    default=DEFAULT_BINARIES["opencode"],
                    help="opencode binary to dump when --opencode-strings is absent")
    ap.add_argument("--baseline", metavar="PATH",
                    help="baseline JSON (default: <repo>/verifiers/surfaces-baseline.json)")
    ap.add_argument("--inventory", metavar="FILE",
                    help="census artifact with a '## Class inventory' section "
                         "(default: <repo>/%s)" % DEFAULT_INVENTORY)
    ap.add_argument("--check", action="append", choices=CHECK_IDS, default=None,
                    help="run only this check (repeatable); default: all")
    ap.add_argument("--self-test", action="store_true",
                    help="assert all checks and exit codes on fixtures only")
    ap.add_argument("--json", action="store_true", help="machine-readable output")
    return ap


def emit_json(results: list[dict], code: int, error: str | None = None) -> None:
    payload = {
        "checks": results,
        "pass": sum(1 for r in results if r["status"] == "PASS"),
        "fail": sum(1 for r in results if r["status"] == "FAIL"),
        "exit_code": code,
    }
    if error is not None:
        payload["error"] = error
    print(json.dumps(payload, indent=2, sort_keys=True))


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    if args.self_test:
        return self_test()

    repo = Path(args.repo)
    baseline_path = Path(args.baseline) if args.baseline else (
        repo / "verifiers" / "surfaces-baseline.json")
    wanted = list(args.check) if args.check else list(CHECK_IDS)

    try:
        entries = load_baseline(baseline_path)
    except BaselineError as exc:
        if args.json:
            emit_json([], 3, str(exc))
        else:
            print("ERROR %s" % exc, file=sys.stderr)
        return 3

    needs_dumps = any(
        c in wanted for c in ("surfaces.literal_present", "surfaces.no_uncovered_class",
                              "surfaces.opencode_extract"))
    needs_inv = any(
        c in wanted for c in ("surfaces.table_parity", "surfaces.literal_parity",
                              "surfaces.kind_parity", "surfaces.excluded_reason"))
    try:
        dumps = {h: load_dump(args, h) for h in HARNESS_IDS} if needs_dumps else {}
        extracted = {h: extract_classes(dumps[h], h) for h in HARNESS_IDS} if dumps else {}
        if needs_inv:
            inv_path = Path(args.inventory) if args.inventory else (
                repo / DEFAULT_INVENTORY)
            inv_text = read_text(inv_path, "inventory file")
            inv = inventory_class_ids(inv_text)
            inv_rows = inventory_rows(inv_text)
        else:
            inv = (set(), "")
            inv_rows = (None, "")
    except EnvError as exc:
        if args.json:
            emit_json([], 2, str(exc))
        else:
            print("ERROR %s" % exc, file=sys.stderr)
        return 2

    results: list[dict] = []
    for cid in wanted:
        if cid == "surfaces.literal_present":
            ok, detail = check_literal_present(entries, dumps, extracted)
        elif cid == "surfaces.no_uncovered_class":
            ok, detail = check_no_uncovered_class(entries, extracted)
        elif cid == "surfaces.opencode_extract":
            ok, detail = check_opencode_extract(entries, dumps["opencode"])
        elif cid == "surfaces.table_parity":
            ok, detail = check_table_parity(entries, inv)
        elif cid == "surfaces.literal_parity":
            ok, detail = check_literal_parity(entries, inv_rows)
        elif cid == "surfaces.kind_parity":
            ok, detail = check_kind_parity(entries, inv_rows)
        else:
            ok, detail = check_excluded_reason(entries, inv)
        results.append({"id": cid, "status": "PASS" if ok else "FAIL",
                        "detail": detail})

    if args.json:
        emit_json(results, 0 if all(r["status"] == "PASS" for r in results) else 1)
    else:
        for r in results:
            print("%s %s: %s" % (r["status"], r["id"], r["detail"]))
    return 0 if all(r["status"] == "PASS" for r in results) else 1


if __name__ == "__main__":
    sys.exit(main())
