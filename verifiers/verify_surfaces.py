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
(``loader-group`` | ``loader-config`` | ``prompt-text`` | ``template-list`` |
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

# Registration calls: Id/Cl/jDe/jDf with a constant first arg, then either a
# quoted group or an identifier group, then a quoted *.md file, followed by a
# comma or close-paren (wrapped calls like `s(Cl(...), "project", "text")` are
# the norm in the bundle).
CALL_RE = re.compile(
    r"(?<![A-Za-z0-9_$])(?:Id|Cl|jD[ef])\(\s*[^\s,()]+\s*,\s*"
    r'(?:"([a-z0-9_-]+)"|([A-Za-z_$][A-Za-z0-9_$]*))\s*,\s*'
    r'"([A-Za-z0-9_./-]+\.md)"(?=\s*[,)])'
)
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
    "surfaces.table_parity",
    "surfaces.excluded_reason",
)


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
# inventory section
# ---------------------------------------------------------------------------

def inventory_class_ids(inventory_text: str) -> tuple[set[str] | None, str]:
    """(ids, problem).  Section = the '## Class inventory' line through the
    line before the next '^## ' heading; ids = backticked class ids found in
    '|'-led table rows inside it.  None -> heading absent."""
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
    ids: set[str] = set()
    for ln in lines[start:end]:
        if ln.lstrip().startswith("|"):
            ids.update(BACKTICK_ID_RE.findall(ln))
    return ids, ""


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
                "%s (no (Id|Cl|jD[ef])(<v>, %s, %s) call shape in %s dump)"
                % (e["class_id"], e["group"], e["file"], e["harness"])
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
            baseline: str = base_clean) -> tuple[int, str]:
        return run_capture(
            ["--repo", fx, "--omp-strings", omp_dump,
             "--opencode-strings", oc_clean,
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

    # (f) missing dump path -> exit 2, never a pass
    code, out = run_capture(
        ["--repo", fx, "--omp-strings", fx + "/NO-SUCH.txt",
         "--opencode-strings", oc_clean,
         "--baseline", base_clean, "--inventory", inv_clean])
    rec("missing dump: exit 2", code == 2, code)

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
        c in wanted for c in ("surfaces.literal_present", "surfaces.no_uncovered_class"))
    needs_inv = any(
        c in wanted for c in ("surfaces.table_parity", "surfaces.excluded_reason"))
    try:
        dumps = {h: load_dump(args, h) for h in HARNESS_IDS} if needs_dumps else {}
        extracted = {h: extract_classes(dumps[h], h) for h in HARNESS_IDS} if dumps else {}
        if needs_inv:
            inv_path = Path(args.inventory) if args.inventory else (
                repo / DEFAULT_INVENTORY)
            inv = inventory_class_ids(read_text(inv_path, "inventory file"))
        else:
            inv = (set(), "")
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
        elif cid == "surfaces.table_parity":
            ok, detail = check_table_parity(entries, inv)
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
