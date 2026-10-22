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
       I5(d, d$, "AGENTS.md")  with  var d$ = "agents-md"
       Gl(d, "gemini", "GEMINI.md")              Mo(d, "gemini", "GEMINI.md")
       bq(u, v$, "AGENTS.md")   with  var v$ = "agents-md"   (omp 18.12.6)
       Kl(u, "gemini", "GEMINI.md")              Ho(u, "github", "copilot-instructions.md")

   i.e. ``(Id|Cl|jDe|jDf|Tl|dr|GW|Co|Dl|Hj|I5|Gl|Mo|lq|Xl|Fo|Kl|Ho|bq)(<v>, <group>, "<file>.md")`` — the file argument must
   end in ``.md`` — where ``<group>`` is either a quoted literal or a bundle
   identifier resolvable to a string constant in the same dump
   (``var|let|const X = "..."``; the minified bundles register the
   ``agents-md``/``claude-md`` groups through variables, so a quoted-only
   extractor would miss them).  An identifier that cannot be resolved is still
   reported as ``<harness>:<unresolved-var:NAME>/<file>`` so it FAILs rather
   than passing silently.

   IDENTIFIER RESOLUTION — MODULE SCOPE (round 51, omp 18.12.6).  The bundle
   is a concatenation of ES modules, and the dump marks each module with a
   source-path comment (``// packages/coding-agent/src/discovery/
   claude-md.ts``).  A minified name bound in two modules is two DIFFERENT
   variables, so a dump-wide "first binding wins" table resolves the wrong
   one: on 18.12.6 ``S$`` is bound to ``"claude-md"`` in the claude-md module
   and to ``"title"`` in ``session/session-entries.ts``, so the dump-wide table
   drops ``S$`` as a conflicting rebind and the class
   ``omp:claude-md/CLAUDE.md`` cannot be verified.  The rule applied here: the
   dump-wide table settles the identifier wherever it has an entry; a name it
   cannot settle is resolved from the binding table of the call's OWN module
   scope, built by the SAME first-seen/drop-on-conflict policy — so two
   different bindings inside one module are a genuine ambiguity and leave the
   call UNRESOLVED, never guessed, while the 18.12.6 ``S$`` case resolves to
   ``claude-md`` because its own module binds it once.  An unresolved call
   still surfaces as ``<unresolved-var:NAME>`` and FAILs.
   LIMIT: the module scope is read off the source-path comments; a bundle
   that stops shipping them makes the whole dump one scope, which restores
   the conservative behaviour (the conflicting name stays unresolved and the
   gate FAILs loudly) rather than resolving anything by guesswork.
   The source-path comment is a PROXY for a variable scope, not a proof of
   one (round-51 falsify ``CriticC1Landed``): on the live 18.12.6 dump the two
   ``S$`` bindings also sit in different ``// @bun @bytecode`` chunks, and
   inside one chunk 95 conflicting names span more than one source module;
   a chunk-based rule gives the same 8 pairs on the live dump.

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
    OC-1, OC-2, OC-3a, OC-3b, OC-4, OC-5, OC-6 over the opencode dump instead and requires TWO-WAY parity: every
    declared opencode class id is produced by a rule, no rule produces an
    undeclared id, every rule matches, and an extraction producing 0 classes
    while the baseline declares opencode classes is a FAIL (the vacuity the check
    exists to kill).  An empty baseline therefore FAILs naming every extracted
    opencode class instead of passing on 0==0.

Exit: 0 all checks pass | 1 any FAIL | 2 environment unreadable (binary, dump
file, strings tool, inventory file, or an OS-level baseline read error — never
a pass) | 3 baseline missing or unparseable (bad JSON, missing keys, malformed
class id).  With ``--json`` the payload additionally carries ``substrate``:
for each harness, the dump source — the binary path with its
sha256/mtime/size when the binary was read, or the
``--<harness>-strings`` dump path when a dump file was supplied.  Read-only;
deterministic for a fixed host.
"""
from __future__ import annotations

import argparse
import contextlib
import hashlib
import io
import json
import os
import re
import subprocess
import sys
import tempfile
from pathlib import Path

DEFAULT_REPO = Path(__file__).resolve().parent.parent
FIXTURES = Path(__file__).resolve().parent / "fixtures" / "surfaces"

DEFAULT_BINARIES = {
    "omp": "/home/vgpnk/.local/bin/omp",
    "opencode": "/home/vgpnk/.npm/_npx/e2094862b59aac7b/node_modules/opencode-ai/bin/opencode.exe",
}
DEFAULT_INVENTORY = "corpus/knowledge/instruction-surface-census-round13.md"
HARNESS_IDS = ("omp", "opencode")
LOADER_KINDS = ("loader-group", "loader-config", "loader-literal")
CONTEXT_KINDS = LOADER_KINDS + ("prompt-text", "template-list", "doc")
VERDICTS = ("governed", "excluded")

# Registration calls: a callee allowlist of the minified names the loader
# bundles have used, kept PER HARNESS (round 21: a name harmless in one bundle
# over-matches the other, and the callee name is minification-volatile — the
# FIRST thing to re-pin on a binary bump):
#   omp: Id/Cl/jDe/jDf (2026-09-28); Tl/dr/GW (2026-10-14); Co/Dl/Hj
#        (2026-10-16, 18.11.1); I5/Gl/Mo (2026-10-18, 18.12.2);
#        lq/Xl/Fo (2026-10-21, 18.12.5: discovery helpers; f$/m$ var-bound groups);
#        Kl/Ho/bq (2026-10-22, 18.12.6: discovery helpers; v$/S$ module-scoped groups)
#   opencode: historical names only — its live bundle is full of single-letter
#             callees that must not feed this extractor; opencode's loaders
#             are list/join shapes governed by the OC-1..OC-6 rules instead
# Shape: a constant first arg, then either a quoted group or an identifier
# group, then a quoted *.md file, followed by a comma or close-paren (wrapped
# calls like `s(Cl(...), "project", "text")` are the norm in the bundle).
#
# The round-50 allowlist (omp 18.12.5) is kept as a NAME TUPLE so the
# self-test's must-fail arm can rebuild it verbatim — a fixture that passed
# against both the round-50 and the round-51 lists would not discriminate the
# re-pin.
OMP_CALLEE_NAMES_ROUND50 = ("Id", "Cl", "jDe", "jDf", "Tl", "dr", "GW", "Co",
                            "Dl", "Hj", "I5", "Gl", "Mo", "lq", "Xl", "Fo")


def call_re(names: tuple[str, ...]) -> "re.Pattern[str]":
    """The registration-call pattern for one callee allowlist."""
    alt = "|".join(re.escape(n) for n in names)
    return re.compile(
        r"(?<![A-Za-z0-9_$])(?:%s)\(\s*[^\s,()]+\s*,\s*" % alt
        + r'(?:"([a-z0-9_-]+)"|([A-Za-z_$][A-Za-z0-9_$]*))\s*,\s*'
        r'"([A-Za-z0-9_./-]+\.md)"(?=\s*[,)])'
    )


CALL_RE = re.compile(
    r"(?<![A-Za-z0-9_$])(?:Id|Cl|jD[ef]|Tl|dr|GW)\(\s*[^\s,()]+\s*,\s*"
    r'(?:"([a-z0-9_-]+)"|([A-Za-z_$][A-Za-z0-9_$]*))\s*,\s*'
    r'"([A-Za-z0-9_./-]+\.md)"(?=\s*[,)])'
)
OMP_CALL_RE = re.compile(
    r"(?<![A-Za-z0-9_$])(?:Id|Cl|jD[ef]|Tl|dr|GW|Co|Dl|Hj|I5|Gl|Mo|lq|Xl|Fo|Kl|Ho|bq)\(\s*[^\s,()]+\s*,\s*"
    r'(?:"([a-z0-9_-]+)"|([A-Za-z_$][A-Za-z0-9_$]*))\s*,\s*'
    r'"([A-Za-z0-9_./-]+\.md)"(?=\s*[,)])'
)
CALLEE_SHAPES = {
    "omp": '(Id|Cl|jD[ef]|Tl|dr|GW|Co|Dl|Hj|I5|Gl|Mo|lq|Xl|Fo|Kl|Ho|bq)(<v>, <group>, "<file>.md")',
    "opencode": '(Id|Cl|jD[ef]|Tl|dr|GW)(<v>, <group>, "<file>.md")',
}
# Module scopes (round 51): the bundle concatenates ES modules and the dump
# marks each one with a source-path comment line; a minified name bound in two
# modules is two different variables, so a binding's scope is its module.
MODULE_MARKER_RE = re.compile(r"^//[ \t]*\S+\.(?:[cm]?[jt]sx?)[ \t]*$", re.M)
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
    (marked unresolvable) rather than guessed.  This is the DUMP-WIDE table: it
    is the fallback for identifiers the call's own module scope does not bind
    (see ``scope_table``), and it is deliberately blind to module scope, so a
    name bound to two values in two different modules is dropped here exactly
    as it always was."""
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


def module_scopes(dump: str) -> list[tuple[int, int]]:
    """Byte spans of the dump's module scopes: each source-path comment opens
    a new module, so a span runs from the previous comment to this one.  A
    dump with no source-path comment is a single scope (the whole dump)."""
    spans: list[tuple[int, int]] = []
    start = 0
    for m in MODULE_MARKER_RE.finditer(dump):
        spans.append((start, m.start()))
        start = m.end()
    spans.append((start, len(dump)))
    return spans


def scope_of(spans: list[tuple[int, int]], pos: int) -> tuple[int, int]:
    """The scope span that contains byte offset ``pos``."""
    lo, hi = 0, len(spans) - 1
    while lo < hi:
        mid = (lo + hi + 1) // 2
        if spans[mid][0] <= pos:
            lo = mid
        else:
            hi = mid - 1
    return spans[lo]


def scope_table(dump: str, spans: list[tuple[int, int]], pos: int) -> dict[str, str]:
    """The binding table of the module scope that contains byte offset ``pos``.

    Same conflict policy as the dump-wide table (``constant_table``): a name
    bound to two different strings INSIDE one module is dropped, so a genuine
    ambiguity inside the call's own module is never guessed."""
    start, end = scope_of(spans, pos)
    if start == 0 and end == len(dump):
        # the whole dump is one scope: the dump-wide table IS its scope table
        return {}
    return constant_table(dump[start:end])


# Function-parameter shadowing (round 51, falsify ReviewScopeRule probe 09): a
# call whose group identifier is a FUNCTION PARAMETER reads the caller's
# argument, not a module binding — the dump carries no evidence for it, so the
# scope (and dump-wide) table must not resolve it.  Textual and conservative:
# the parameter list of the nearest preceding function header within the call's
# module span is scanned for the identifier as a whole token; a header whose
# parameters contain it disqualifies the resolution (fail-closed over
# false-positive).
PARAM_HEADER_RE = re.compile(
    r"(?:async\s+)?function\s*[\w$]*\s*\(([^()]*)\)"
    r"|(?:\(([^()]*)\)|([A-Za-z_$][\w$]*))\s*=>"
)


def param_shadowed(dump: str, spans: list[tuple[int, int]], pos: int,
                   ident: str) -> bool:
    """True when ``ident`` is a parameter of the nearest preceding function
    header before ``pos`` in the call's own module span."""
    start, _ = scope_of(spans, pos)
    params: set[str] = set()
    for m in PARAM_HEADER_RE.finditer(dump[start:pos]):
        if m.group(3) is not None:
            params = {m.group(3)}
        else:
            plist = m.group(1) or m.group(2)
            params = {p.strip() for p in plist.split(",") if p.strip()} \
                if plist else set()
    return ident in params


def extract_classes(dump: str, harness: str) -> set[tuple[str, str]]:
    """All (group, file) pairs from `.md`-suffixed registration-call shapes.
    The callee allowlist is per-harness (CALL_RE/OMP_CALL_RE above).  Identifier
    group args are resolved through the dump's constant table — for a name the
    dump-wide table cannot settle, the binding table of the call's OWN module
    scope decides (round 51); a group identifier that is a function parameter of
    the enclosing function never resolves (param-shadow guard, falsify
    ReviewScopeRule probe 09); unresolvable ones surface as a
    ``<unresolved-var:NAME>`` group so they cannot pass silently."""
    global_table = constant_table(dump)
    pattern = OMP_CALL_RE if harness == "omp" else CALL_RE
    spans = module_scopes(dump)
    pairs: set[tuple[str, str]] = set()
    for m in pattern.finditer(dump):
        quoted, ident, filename = m.group(1), m.group(2), m.group(3)
        # (round 51) the dump-wide table settles a name bound to ONE value in
        # the whole dump; a name bound to two different values — two modules'
        # variables sharing one minified name — is dropped by that table and
        # settled by the call's OWN module scope.  The dump-wide table wins
        # wherever it has an entry.
        consts = {**scope_table(dump, spans, m.start()), **global_table}
        if quoted:
            group = quoted
        elif ident in consts and not param_shadowed(dump, spans, m.start(), ident):
            group = consts[ident]
        else:
            group = "<unresolved-var:%s>" % ident
        pairs.add((group, filename))
    return pairs


# ---------------------------------------------------------------------------
# opencode: instruction-service extraction (rules OC-1..OC-6)
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

# GENERATION NOTE (round 47, append-only history): opencode moved channel.  The
# round-18 v2.0.26 binary (`~/.opencode/bin`, sha `d9123b9b…`) is gone; the host
# now runs npm `opencode-ai` 1.19.3 (npx cache, sha `179ca421…`), a different
# lineage whose loader shapes are the round-14 ones, not v2.0.26's: on the frozen
# 1.19.3 dump the v2.0.26 anchors `ConfigInstructionPlugin`, `ReadTool.Plugin`,
# `SessionInstructions`, `session.instructions.entry.put`, `j5(r.config,…)` and
# `InstructionDiscovery` occur 0 times, while every rule below matches.  The rules
# were re-measured anchor by anchor on that dump (counts and dump lines in
# `corpus/knowledge/instruction-surface-census-round13.md` § B′ and its round-47
# ledger); on this host the retired v2.0.26 rule set survives only as the
# must-fail generation fixture `fixtures/surfaces/strings-opencode-v2.0.26.txt`
# (upstream, npm `@opencode/cli` 2.x still ships it — host-scoped retirement).
# LIMITS found by the round-47 falsify wave (carried, not fixed): every rule is a
# whole-dump presence test, not bound to a code body — decoys elsewhere satisfy
# it, and caller/delivery/gate edges are unwitnessed (OC-1's `gated` term reduces
# to `m is not None`; OC-4's call edge and in-hook token; OC-6's config
# candidate and env gate); a failing rule lists all its anchors as missing.

# OC-1: the per-directory name-priority list (first-match walk-up; dump 443993):
#   y=["AGENTS.md",...!t.disableClaudeCodePrompt?["CLAUDE.md"]:[],"CONTEXT.md"]
# Every *.md literal inside the array DERIVES a class id, so a name planted into
# or dropped from the array changes the extracted set (never a witness-only pass).
OC_PRIORITY_RE = re.compile(r'\["AGENTS\.md".{0,400}?"CONTEXT\.md"[^\]]{0,200}\]')
OC_MD_NAME_RE = re.compile(r'"([A-Za-z0-9_.-]+\.md)"')
OC_GATE = "disableClaudeCodePrompt"

# OC-2: the config/home candidate list (`Instruction.systemPaths`; dump 443993):
#   X.join(r.config,"AGENTS.md")   X.join(r.home,".claude","CLAUDE.md")
OC_CONFIG_JOIN_RE = re.compile(
    r'\.join\(\s*[A-Za-z_$][A-Za-z0-9_$]*\.config\s*,\s*"([A-Za-z0-9_.-]+\.md)"'
)
OC_HOME_DIR_JOIN_RE = re.compile(
    r'\.join\(\s*[A-Za-z_$][A-Za-z0-9_$]*\.home\s*,\s*"\.([A-Za-z0-9_-]+)"\s*,'
    r'\s*"([A-Za-z0-9_.-]+\.md)"'
)

# OC-3: the declared ``instructions`` list and its remote half (dump 443993).
#   a: `Instruction.systemPaths` consumes it —
#      for(let O of T.instructions){if(O.startsWith("https://")||…)continue;…glob…}
#   b: `Instruction.system` fetches the remote entries and renders them —
#      (T.instructions??[]).filter((q)=>q.startsWith("https://")||q.startsWith("http://"))
#      `Instructions from: ${q}`
# Round 47 tightened b to require the ``.filter(`` call: the round-14 pattern also
# matched a's loop (2 hits on 1.19.3), so a dropped filter still passed.
OC_DECLARED_RE = re.compile(
    r"for\s*\(\s*let\s+[A-Za-z_$][A-Za-z0-9_$]*\s+of\s+"
    r"[A-Za-z_$][A-Za-z0-9_$]*\.instructions\s*\)"
)
OC_REMOTE_FILTER_RE = re.compile(
    r'\.instructions[^;]{0,20}?\.filter\(\s*\(?\s*([A-Za-z_$][A-Za-z0-9_$]*)\s*\)?\s*=>\s*'
    r'\1\.startsWith\("https://"\)\s*\|\|\s*\1\.startsWith\("http://"\)'
)
OC_REMOTE_RENDER = "Instructions from: "

# OC-5: the resolution switch that decides *where* OC-1's names are read from —
# project walk-up versus config-only (dump 443993):
#   if(!Jr.OPENCODE_DISABLE_PROJECT_CONFIG)return yield*e.globUp(T,d.directory,d.worktree)
#   return yield*e.globUp(T,r.config,r.config)
OC_ENV_PROJECT_CONFIG = "OPENCODE_DISABLE_PROJECT_CONFIG"
OC_GLOBUP_PROJECT_RE = re.compile(r"globUp\([^)]*\.directory[^)]*\.worktree\)")
OC_GLOBUP_CONFIG_RE = re.compile(r"globUp\([^)]*\.config\s*,\s*[^)]*\.config\)")

# OC-6: opencode's SECOND instruction subsystem (layer `instruction-context`,
# key ``core/instructions``, composed as a dependency of the
# `system-context-builtins` layer — not registered as it; dump 445481-445487).  It walks AGENTS.md all-match up from cwd to the project root
# and keeps an ungated config-dir candidate (`jX(L.config,"AGENTS.md")`) — a
# different load condition for the same file class than OC-1/OC-2's first-match
# walk, which is why it carries its own class id.
OC_V2_KEY = 'Key.make("core/instructions")'
OC_V2_TARGETS = 'targets:["AGENTS.md"]'
OC_V2_OBSERVE = "InstructionContext.observe"
OC_V2_REGISTRATION = "system-context-builtins"

# OC-4: the read-tool channel that appends the instruction file found at EVERY
# ancestor level (one per directory, nearest first; the walk stops at the
# instance directory by an unseparated string-prefix test) to a read's TOOL RESULT:
# `s.fn("Instruction.resolve")` (dump 443995), called from
# `s.fn("ReadTool.execute")` (dump 444228-444233, `e.resolve(g.messages,h,…)`),
# delivered inside `<system-reminder>`.  Round 47 added the ReadTool.execute
# anchor: `<system-reminder>` alone is a generic token (18 hits on 1.19.3).
OC_READ_HOOK_FN = 'fn("Instruction.resolve")'
OC_READ_TOOL_FN = 'fn("ReadTool.execute")'
OC_READ_HOOK_TOKEN = "<system-reminder>"


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

    # OC-1 — name-priority list (derives every *.md literal in the array)
    m = OC_PRIORITY_RE.search(dump)
    names = sorted(set(OC_MD_NAME_RE.findall(m.group(0)))) if m else []
    gated = m is not None and (OC_GATE not in m.group(0) or OC_GATE in dump)
    owns = (["opencode:instructions/%s" % n for n in names] if names else
            ["opencode:instructions/AGENTS.md", "opencode:instructions/CLAUDE.md",
             "opencode:instructions/CONTEXT.md"])
    rule("OC-1", owns, m is not None and bool(names) and gated,
         ['["AGENTS.md" … "CONTEXT.md"]', OC_GATE])

    # OC-2 — config/home candidates (derives group + file from the join path)
    cfg = sorted(set(OC_CONFIG_JOIN_RE.findall(dump)))
    home = sorted(set(OC_HOME_DIR_JOIN_RE.findall(dump)))
    # home candidates are named `<dir>-home` after the dot-directory the join
    # walks (`.claude` -> `opencode:claude-home/CLAUDE.md`), the census's id shape.
    owns2 = (["opencode:config/%s" % f for f in cfg] +
             ["opencode:%s-home/%s" % (d, f) for d, f in home])
    rule("OC-2", owns2 or ["opencode:config/AGENTS.md", "opencode:claude-home/CLAUDE.md"],
         bool(cfg) and bool(home),
         ['X.join(<v>.config,"AGENTS.md")',
          'X.join(<v>.home,".claude","CLAUDE.md")'])

    # OC-3 — declared list + remote filter/render (two ids, two anchor pairs)
    declared = OC_DECLARED_RE.search(dump) is not None
    rule("OC-3a", ["opencode:config/instructions"], declared,
         ["for(let <v> of <v>.instructions)"])
    remote = (OC_REMOTE_FILTER_RE.search(dump) is not None
              and OC_REMOTE_RENDER in dump)
    rule("OC-3b", ["opencode:config/instructions-remote"], remote,
         ['.instructions….filter((q)=>q.startsWith("https://")||q.startsWith("http://"))',
          OC_REMOTE_RENDER])

    # OC-4 — read-tool channel
    read_hook = (OC_READ_HOOK_FN in dump and OC_READ_TOOL_FN in dump
                 and OC_READ_HOOK_TOKEN in dump)
    rule("OC-4", ["opencode:read-hook/instructions"], read_hook,
         [OC_READ_HOOK_FN, OC_READ_TOOL_FN, OC_READ_HOOK_TOKEN])

    # OC-5 — resolution switch (owns no class id; witnesses the path the ids are
    # read through, so losing it is a drift FAIL rather than a silent re-scope)
    resolve_switch = (OC_ENV_PROJECT_CONFIG in dump
                      and OC_GLOBUP_PROJECT_RE.search(dump) is not None
                      and OC_GLOBUP_CONFIG_RE.search(dump) is not None)
    rule("OC-5", [], resolve_switch,
         [OC_ENV_PROJECT_CONFIG, "globUp(<v>.directory,<v>.worktree)",
          "globUp(<v>.config,<v>.config)"])

    # OC-6 — second instruction subsystem (own load condition for AGENTS.md)
    v2 = all(a in dump for a in (OC_V2_KEY, OC_V2_TARGETS, OC_V2_OBSERVE,
                                 OC_V2_REGISTRATION))
    rule("OC-6", ["opencode:instruction-context/AGENTS.md"], v2,
         [OC_V2_OBSERVE, OC_V2_KEY, OC_V2_TARGETS, OC_V2_REGISTRATION])

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
                % (e["class_id"], CALLEE_SHAPES[e["harness"]],
                   e["group"], e["file"], e["harness"])
            )
    if problems:
        return False, "%d loader literal(s) not verifiable: %s" % (
            len(problems), "; ".join(problems))
    return True, "%d loader-kind entr%s verified against the dumps" % (
        checked, "y" if checked == 1 else "ies")


def check_no_uncovered_class(entries: list[dict],
                             extracted: dict[str, set[tuple[str, str]]],
                             dumps: dict[str, str] | None = None) -> tuple[bool, str]:
    """Set parity over the documented extraction, plus the round-21 vacuity
    guard: a harness dump from which ZERO loader classes extract while the
    baseline declares loader-group classes for it is a moved/renamed
    substrate — a FAIL, never an empty-set pass (the 2026-10-16 omp rebuild
    extracted 0 shapes here while literal_present failed every row, and this
    check still said PASS).  Guarded per loader-group kind only: opencode's
    declared classes are config/rule kinds covered by opencode_extract's own
    zero-extraction rule, so an empty CALL_RE extraction is its documented
    steady state, not drift.

    Round-28 kind-consistency arm: an extracted class id is machine PROOF of a
    ``(group, file).md`` registration-call shape in the dump, so its baseline
    entry must declare ``loader-group``.  An id the dump still yields but the
    baseline re-kinded to ``doc``/``loader-literal``/... is kind laundering —
    a FAIL naming each ``id->kind`` (scout M2's rekind escape; also covers the
    PARTIAL rekind where some loader-group rows survive and the zero-declared
    vacuity arm above stays silent)."""
    declared = {e["class_id"] for e in entries}
    by_id = {e["class_id"]: e for e in entries}
    found: set[str] = set()
    problems: list[str] = []
    for harness in HARNESS_IDS:
        pairs = extracted[harness]
        loader_group_declared = sorted(
            e["class_id"] for e in entries
            if e["harness"] == harness and e["context_kind"] == "loader-group")
        if loader_group_declared and not pairs:
            problems.append(
                "vacuity: 0 loader class(es) extracted from the %s dump while "
                "the baseline declares %d loader-group class(es) for it — a "
                "moved or renamed substrate must FAIL, never pass silently"
                % (harness, len(loader_group_declared)))
        if not pairs and dumps is not None and harness == "omp":
            blind = sorted(e["class_id"] for e in entries
                           if e["harness"] == harness
                           and e["literal"] in dumps[harness])
            if blind:
                problems.append(
                    "extractor blind: %d declared literal(s) present in the %s "
                    "dump but no registration shape extracts (%s) — extractor "
                    "blindness is a substrate move, not health"
                    % (len(blind), harness, ", ".join(blind)))
        found |= {"%s:%s/%s" % (harness, g, f) for g, f in pairs}
    uncovered = sorted(found - declared)
    if uncovered:
        problems.append("%d loader class(es) undeclared in baseline: %s" % (
            len(uncovered), ", ".join(uncovered)))
    laundered = sorted(cid for cid in found
                       if cid in by_id
                       and by_id[cid]["context_kind"] != "loader-group")
    if laundered:
        problems.append(
            "%d extracted loader class(es) re-kinded in the baseline — kind "
            "reassignment is not a bypass: %s" % (
                len(laundered),
                ", ".join("%s->%s" % (cid, by_id[cid]["context_kind"])
                          for cid in laundered)))
    if problems:
        return False, "; ".join(problems)
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
    global OMP_CALL_RE
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

    # (b2) the 2026-10-16 and 2026-10-18 omp rebuilds renamed callees
    # (Co/Dl/Hj and I5/Gl/Mo); both generations must extract the classes
    code, out = run(omp_dump=fx + "/strings-omp-newcallees.txt")
    rec("new-callees: exit 0", code == 0, code)
    rec("new-callees: PASS literal_present",
        "PASS surfaces.literal_present:" in out, out)
    rec("new-callees: PASS no_uncovered_class",
        "PASS surfaces.no_uncovered_class:" in out, out)

    # (b2c) the 2026-10-21 rebuild (18.12.5) renamed the callees again: lq/Xl/Fo,
    # with the agents-md/claude-md groups var-bound (f$, m$). The eight omp
    # loader-group pairs must extract, and the 2-char alias decoy `q = Xl`
    # must not (it would surface as an undeclared class).
    code, out = run_capture(
        ["--repo", fx, "--omp-strings", fx + "/strings-omp-18.12.5.txt",
         "--opencode-strings", oc_clean,
         "--baseline", fx + "/baseline-18.12.5.json", "--inventory", inv_clean,
         "--check", "surfaces.literal_present",
         "--check", "surfaces.no_uncovered_class"])
    rec("18.12.5-callees: exit 0", code == 0, code)
    rec("18.12.5-callees: PASS literal_present",
        "PASS surfaces.literal_present:" in out, out)
    rec("18.12.5-callees: PASS no_uncovered_class, all 8 pairs",
        "PASS surfaces.no_uncovered_class: all 8 extracted loader class(es) declared" in out,
        out)
    # (b2d) round 51 (18.12.6): the loader registration callees rotated again
    # (bq/Kl/Ho) and the two var-bound groups (v$, S$) live in DIFFERENT
    # modules: S$ is "claude-md" in discovery/claude-md.ts and "title" in
    # session/session-entries.ts (the real prior binding, live dump line
    # 843423), so the dump-wide first-seen table drops it as a conflict and
    # the call's own module scope must settle it.  The fixture also carries a
    # LATER S$ binding ("later") so a "last binding wins" rule cannot pass it.
    # All eight omp loader-group pairs must extract.
    code, out = run_capture(
        ["--repo", fx, "--omp-strings", fx + "/strings-omp-18.12.6.txt",
         "--opencode-strings", oc_clean,
         "--baseline", fx + "/baseline-18.12.5.json", "--inventory", inv_clean,
         "--check", "surfaces.literal_present",
         "--check", "surfaces.no_uncovered_class"])
    rec("18.12.6-callees: exit 0", code == 0, code)
    rec("18.12.6-callees: PASS literal_present",
        "PASS surfaces.literal_present:" in out, out)
    rec("18.12.6-callees: PASS no_uncovered_class, all 8 pairs",
        "PASS surfaces.no_uncovered_class: all 8 extracted loader class(es) declared" in out,
        out)

    # (b2e) the same fixture must FAIL against the round-50 callee allowlist —
    # the 18.12.6 rename is what the re-pin fixes, so a fixture that passed
    # both lists would not discriminate (Q25).
    saved_re = OMP_CALL_RE
    try:
        OMP_CALL_RE = call_re(OMP_CALLEE_NAMES_ROUND50)
        code, out = run_capture(
            ["--repo", fx, "--omp-strings", fx + "/strings-omp-18.12.6.txt",
             "--opencode-strings", oc_clean,
             "--baseline", fx + "/baseline-18.12.5.json", "--inventory", inv_clean,
             "--check", "surfaces.literal_present",
             "--check", "surfaces.no_uncovered_class"])
    finally:
        OMP_CALL_RE = saved_re
    rec("18.12.6-round50-allowlist: exit 1", code == 1, code)
    rec("18.12.6-round50-allowlist: FAIL literal_present",
        "FAIL surfaces.literal_present:" in out, out)
    rec("18.12.6-round50-allowlist: vacuity named",
        "FAIL surfaces.no_uncovered_class:" in out and "vacuity" in out, out)

    # (b2f) fx-renamed-var: the SAME conflict on a renamed variable (T$ in
    # place of S$) must resolve the same way — a rule hardcoded to per
    # identifier (m2b) must fail here.
    fx18126 = (Path(fx) / "strings-omp-18.12.6.txt").read_text(encoding="utf-8")
    renamed = fx18126.replace("S$", "T$")
    with tempfile.TemporaryDirectory() as tmp:
        renamed_path = str(Path(tmp) / "strings-omp-renamed.txt")
        Path(renamed_path).write_text(renamed, encoding="utf-8")
        code, out = run_capture(
            ["--repo", fx, "--omp-strings", renamed_path,
             "--opencode-strings", oc_clean,
             "--baseline", fx + "/baseline-18.12.5.json", "--inventory", inv_clean,
             "--check", "surfaces.literal_present",
             "--check", "surfaces.no_uncovered_class"])
    rec("fx-renamed-var: exit 0", code == 0, code)
    rec("fx-renamed-var: PASS literal_present",
        "PASS surfaces.literal_present:" in out, out)
    rec("fx-renamed-var: PASS no_uncovered_class, all 8 pairs",
        "PASS surfaces.no_uncovered_class: all 8 extracted loader class(es) declared" in out,
        out)

    # (b2g) Q18 control: a genuinely ambiguous rebind INSIDE the call's own
    # module (a second, conflicting binding of S$ in the claude-md module)
    # must stay UNRESOLVED — never guessed — at both the extraction level and
    # the CLI level (the gate must FAIL loudly, not pass on a guessed value).
    ambiguous = fx18126.replace(
        'var S$ = "claude-md";',
        'var S$ = "claude-md";\nvar S$ = "claude-md-rebound";')
    pairs = extract_classes(ambiguous, "omp")
    rec("ambiguous-rebind: claude-md NOT resolved",
        ("claude-md", "CLAUDE.md") not in pairs, sorted(pairs))
    rec("ambiguous-rebind: S$ surfaces unresolved",
        ("<unresolved-var:S$>", "CLAUDE.md") in pairs, sorted(pairs))
    with tempfile.TemporaryDirectory() as tmp:
        amb_path = str(Path(tmp) / "strings-omp-ambiguous.txt")
        Path(amb_path).write_text(ambiguous, encoding="utf-8")
        code, out = run_capture(
            ["--repo", fx, "--omp-strings", amb_path,
             "--opencode-strings", oc_clean,
             "--baseline", fx + "/baseline-18.12.5.json", "--inventory", inv_clean,
             "--check", "surfaces.literal_present",
             "--check", "surfaces.no_uncovered_class"])
    rec("ambiguous-rebind CLI: exit 1", code == 1, code)
    rec("ambiguous-rebind CLI: FAIL literal_present names the missing shape",
        "FAIL surfaces.literal_present:" in out and "omp:claude-md/CLAUDE.md" in out, out)
    rec("ambiguous-rebind CLI: the unresolved var is named",
        "<unresolved-var:S$>" in out, out)

    # (b2h) Q18 control 2: a name bound to two values in two OTHER modules and
    # not bound in the call's own module stays unresolved — the dump-wide
    # table's conservative behaviour is preserved.  And a call whose own
    # module DOES bind the name settles it even when other modules conflict.
    cross = (
        '// m1.ts\nvar Q$ = "one";\n'
        '// m2.ts\nvar Q$ = "two";\n'
        '// m3.ts\nfunction f(u) { return bq(u, Q$, "X.md"); }\n'
    )
    pairs = extract_classes(cross, "omp")
    rec("cross-module conflict not settled by the call's module: unresolved",
        ("<unresolved-var:Q$>", "X.md") in pairs
        and ("one", "X.md") not in pairs and ("two", "X.md") not in pairs,
        sorted(pairs))
    settled = (
        '// m1.ts\nvar Q$ = "one";\n'
        '// m2.ts\nvar Q$ = "two";\n'
        '// m3.ts\nvar Q$ = "two";\nfunction f(u) { return bq(u, Q$, "X.md"); }\n'
    )
    pairs = extract_classes(settled, "omp")
    rec("own-module binding settles the call",
        ("two", "X.md") in pairs, sorted(pairs))

    # (b2i) falsify ReviewScopeRule probe 09: a group identifier that is a
    # FUNCTION PARAMETER shadows the module binding and must NOT resolve — the
    # parameter's value is not in the dump, so the class is unwitnessed and
    # must FAIL loud (never resolve to the module's own binding).
    shadowed = fx18126.replace("async function XBt(u) {", "async function XBt(u, S$) {")
    pairs = extract_classes(shadowed, "omp")
    rec("param-shadow: claude-md NOT resolved",
        ("claude-md", "CLAUDE.md") not in pairs, sorted(pairs))
    rec("param-shadow: S$ surfaces unresolved",
        ("<unresolved-var:S$>", "CLAUDE.md") in pairs, sorted(pairs))
    with tempfile.TemporaryDirectory() as tmp:
        sh_path = str(Path(tmp) / "strings-omp-param-shadow.txt")
        Path(sh_path).write_text(shadowed, encoding="utf-8")
        code, out = run_capture(
            ["--repo", fx, "--omp-strings", sh_path,
             "--opencode-strings", oc_clean,
             "--baseline", fx + "/baseline-18.12.5.json", "--inventory", inv_clean,
             "--check", "surfaces.literal_present",
             "--check", "surfaces.no_uncovered_class"])
    rec("param-shadow CLI: exit 1", code == 1, code)
    rec("param-shadow CLI: names the unresolved class",
        "<unresolved-var:S$>" in out, out)
    # (b3) a substrate whose call shapes all vanish is a vacuity FAIL, never
    # an empty-set pass (the 2026-10-16 omp-move defect class round 21 fixed)
    code, out = run(omp_dump=fx + "/strings-empty.txt")
    rec("extract-vacuity: exit 1", code == 1, code)
    rec("extract-vacuity: FAIL no_uncovered_class names vacuity",
        "FAIL surfaces.no_uncovered_class:" in out and "vacuity" in out, out)

    # (b4) round-28 kind-reassignment escape (scout M2): the dump still yields
    # the registration-call shapes while the baseline re-kinds omp loader-group
    # rows to `doc` (census kind cells re-kinded with it) -> the kind-consistency
    # arm FAILs naming id->kind.  The partial case keeps omp:gemini a live
    # loader-group row, so the zero-declared vacuity arm alone would stay
    # silent — re-kinding is not a bypass, not even partially.
    code, out = run(baseline=fx + "/baseline-rekind-doc.json",
                    inventory=fx + "/inventory-rekind-doc.md")
    rec("rekind-doc: exit 1", code == 1, code)
    rec("rekind-doc: FAIL no_uncovered_class names laundering",
        "FAIL surfaces.no_uncovered_class:" in out and "not a bypass" in out,
        out)
    rec("rekind-doc: names omp:gemini/GEMINI.md->doc",
        "omp:gemini/GEMINI.md->doc" in out, out)
    rec("rekind-doc: names omp:claude-md/CLAUDE.md->doc",
        "omp:claude-md/CLAUDE.md->doc" in out, out)
    code, out = run(baseline=fx + "/baseline-rekind-partial.json",
                    inventory=fx + "/inventory-rekind-partial.md")
    rec("rekind-partial: exit 1", code == 1, code)
    rec("rekind-partial: names omp:claude-md/CLAUDE.md->doc",
        "omp:claude-md/CLAUDE.md->doc" in out, out)
    rec("rekind-partial: gemini row untouched (no gemini->doc, literal_present green)",
        "omp:gemini/GEMINI.md->doc" not in out
        and "PASS surfaces.literal_present:" in out, out)

    # (b5) round-31 extractor-blindness arm (the M6 residual): a dump that
    # still carries the declared literals while yielding zero registration
    # shapes — here with the rows re-kinded away from loader-group — is
    # extractor blindness, not health.
    code, out = run(omp_dump=fx + "/strings-omp-blind.txt",
                    baseline=fx + "/baseline-rekind-doc.json",
                    inventory=fx + "/inventory-rekind-doc.md")
    rec("extractor-blind: exit 1", code == 1, code)
    rec("extractor-blind: FAIL no_uncovered_class names blindness",
        "FAIL surfaces.no_uncovered_class:" in out and "extractor blind" in out,
        out)
    rec("extractor-blind: names omp:gemini/GEMINI.md",
        "omp:gemini/GEMINI.md" in out, out)

    # (b5b) r21 semantics preserved: the same literal-bearing dead dump with
    # loader-group rows still declared keeps the vacuity FAIL.
    code, out = run(omp_dump=fx + "/strings-omp-blind.txt")
    rec("blind-dead-dump: exit 1", code == 1, code)
    rec("blind-dead-dump: vacuity named", "vacuity" in out, out)

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
            ("strings-opencode-drop-oc1.txt", "opencode:instructions/CONTEXT.md"),
            ("strings-opencode-drop-oc2.txt", "opencode:claude-home/CLAUDE.md"),
            ("strings-opencode-drop-oc3a.txt", "opencode:config/instructions"),
            ("strings-opencode-drop-oc3b.txt", "opencode:config/instructions-remote"),
            ("strings-opencode-drop-oc4.txt", "opencode:read-hook/instructions"),
            ("strings-opencode-drop-oc5.txt", "OC-5"),
            ("strings-opencode-drop-oc6.txt", "opencode:instruction-context/AGENTS.md")):
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

    # (oc-gen) round 47: the retired v2.0.26 rule-set fixture is a different
    # opencode generation — the 1.19.3 rules must NOT accept it (a rule set that
    # OR-ed both generations' anchors would pass here and launder the re-derive).
    code, out = run(oc_dump=fx + "/strings-opencode-v2.0.26.txt")
    rec("oc-v2.0.26-generation: exit 1", code == 1, code)
    rec("oc-v2.0.26-generation: FAIL opencode_extract",
        "FAIL surfaces.opencode_extract:" in out, out)
    rec("oc-v2.0.26-generation: names OC-1 unmatched", "OC-1 (owns" in out, out)

    # (oc-derive) round 47: OC-1 DERIVES names from the priority array — a name
    # planted into it surfaces as an undeclared class, named.
    code, out = run(oc_dump=fx + "/strings-opencode-planted-name.txt")
    rec("oc-planted-name: exit 1", code == 1, code)
    rec("oc-planted-name: names opencode:instructions/GUIDE.md undeclared",
        "undeclared in baseline: opencode:instructions/GUIDE.md" in out, out)

    # (oc0) empty baseline + a real anchor dump -> exit 1 naming every extracted
    # opencode class (never a pass on 0==0)
    code, out = run(baseline=fx + "/baseline-oc-empty.json")
    rec("oc-empty-baseline: exit 1", code == 1, code)
    rec("oc-empty-baseline: FAIL opencode_extract",
        "FAIL surfaces.opencode_extract:" in out, out)
    for cid in ("opencode:instructions/CONTEXT.md", "opencode:config/instructions",
                "opencode:read-hook/instructions",
                "opencode:instruction-context/AGENTS.md"):
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


def binary_digest(path: Path) -> tuple[str, float, int] | None:
    """(sha256, mtime epoch, size) of a binary, or None when unreadable."""
    try:
        h = hashlib.sha256()
        with path.open("rb") as fh:
            for block in iter(lambda: fh.read(1 << 20), b""):
                h.update(block)
        st = path.stat()
        return h.hexdigest(), st.st_mtime, st.st_size
    except OSError:
        return None


def substrate_identity(args: argparse.Namespace) -> dict:
    """For each harness, which (binary | dump) source the dumps came from.

    When the binary was read its sha256/mtime/size are included, so the
    ``--json`` counter itself prints which binary it read (round 51)."""
    identity: dict = {}
    for h in HARNESS_IDS:
        given = getattr(args, "%s_strings" % h)
        if given is not None:
            identity[h] = {"source": "dump", "path": str(given)}
            continue
        binary = Path(getattr(args, "%s_binary" % h))
        entry = {"source": "binary", "path": str(binary)}
        digest = binary_digest(binary)
        if digest is not None:
            entry["sha256"], entry["mtime"], entry["bytes"] = digest
        identity[h] = entry
    return identity


def emit_json(results: list[dict], code: int, error: str | None = None,
              substrate: dict | None = None) -> None:
    payload = {
        "checks": results,
        "pass": sum(1 for r in results if r["status"] == "PASS"),
        "fail": sum(1 for r in results if r["status"] == "FAIL"),
        "exit_code": code,
    }
    if error is not None:
        payload["error"] = error
    if substrate is not None:
        payload["substrate"] = substrate
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
            ok, detail = check_no_uncovered_class(entries, extracted, dumps)
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
        substrate = substrate_identity(args) if needs_dumps else None
        emit_json(results, 0 if all(r["status"] == "PASS" for r in results) else 1,
                  substrate=substrate)
    else:
        for r in results:
            print("%s %s: %s" % (r["status"], r["id"], r["detail"]))
    return 0 if all(r["status"] == "PASS" for r in results) else 1


if __name__ == "__main__":
    sys.exit(main())
