#!/usr/bin/env python3
'''check_assertion_floors.py -- anti-shrink guard for the instruments' self-tests.

The claim under test: a self-test that silently loses assertions must never
still read green. Each instrument's --self-test prints an assertion count;
this guard reruns every self-test and FAILs when the observed count is below
the recorded floor (harness 10, corpus_integrity 150, corpus_independent 91,
surfaces 99, checklist 1845, pins 62, harness_independent 115,
compare_harness_independent 330, floors_guard 150; others @ round 36 --
round 47 ratcheted surfaces 87->99 (1.19.3 opencode fixtures, 18.12.5 omp
callees) and checklist 1597->1845 (trigger.no_xml_tag + governance errata arms); the
checklist floor re-recorded at round 37 by the C3 fence battery plus the
indented-code decoy battery and at round 38 by the three container-relative
fence shapes (V6's named residual); the two round-38 C1 instruments registered
by claim C1f/seat P3 (floors re-bumped in-step to the settled counts of the C1
closure seat P1 landed in the same round: 71->86, 59->83); `harness_independent`
re-bumped at round 39 by seat P2's init_count predicate fix + grammar fixtures
(86->93) and again by seat P1's scoped-row probe battery (93->104); round 48
re-bumps it (104->115) by the C1 configured-root regression arm (the two
--oc-config roots, the same-name pair, the direct-child scope against a
recursive enumeration, and the no-harm log-named roots);
`compare_harness_independent` re-bumped at round 39 by seat P1's scope-out
discriminator battery (83->97), and at round 40 by seat F1's committed F-2/F-3
payload arms -- the expected-launder, rows-shadow and checks-shadow shapes plus
the agree-control (97->117); at round 43 by seat P2's un-contract top-level
field-gate fixture battery (118->143); round 43's scoped-map and status-alias battery (143->213); round 44 adds dotted top-level-map-shadow, record check/id, and re_derived/observed conflict fixtures (213->228); round 44 F1 adds record+map control/composition arms and local probe materialization (228->245); round 45 P2 adds the lone non-string status fixture (245->250); round 45 P1 adds the expected-alias-conflict fixture (250->255); round 46's P3 raw duplicate-member cases plus shared scope-file and live-shadow fixtures move the comparator floor to 293 (255->293); P4's committed-scope reason/evidence checks, probe-target pin, probe-copy shadow discriminators and refreshed scoped-out stub controls move it to 328 (293->328); round 46's landing adds the extract_json prose-fragment control and the selected-payload duplicate arm (328->330). The two corpus floors re-bumped at round
39 by seat P4's CommonMark 4.5 closer-rule battery (119->129, 59->68), and at
round 40 by seat F2's indent-clause battery -- the 0/2/3-space controls plus
the 4-space, tab, mixed-indent, opener-arm and tilde shapes, each expected set
derived from cmark 0.31.2 alone (129->145, 68->86). Round 41 (claim C2/V16)
adds this guard's own 150-assertion self-test as a floored instrument; round 43
C3 adds unclosed/mixed/blockquote fence assertions (145->150, 86->91).
Exit: 0 all floors hold;
1 an instrument ran below its floor, or its summary could not be parsed or the
instrument could not be run (named, observed-vs-floor); 2 the in-file registry
or the external anchor disagrees (named), or a self-test timed out, or a
declared instrument path escapes --repo (named 'escape:'). Read-only.

REGISTRY ANCHORS. Rounds 31 (scout G2/G3) added the two-way in-file registry
self-check; round 37 (claim C2a, scouts C2/M7) closed its residual: those two
tables agree with each other by construction, so a coordinated edit -- the
same row deleted from BOTH, a floor lowered in BOTH, a row path repointed --
was self-consistent and silent (M7: two-table deletion -> 5 PASS, exit 0, the
instrument never reran). The anchor is now verifiers/floors-registry.json, a
file OUTSIDE this one: every registry entry must be covered by both tables
with the same path and floor, the registry's own size must match its declared
`instrument_total`, and each declared path must resolve to a non-empty file
under --repo. Round 41 also registers `floors_guard` here: its self-test exits
before main's instrument walk, so the self-reference terminates. Any
disagreement fails loudly before a self-test runs. Run `--self-test` for the
fixture battery (mutant copies in tempdirs), including the two true
discriminators for the coordinated shapes. Round 38 (claim C2, seat P4) closes
V4's two residuals: a non-str key in either table is now named ('non-string
key: ...', previously an uncaught TypeError traceback at exit 1, class
unnamed), and a malformed row is named exactly once -- the anchor no longer
derives a path/floor from a row whose shape it could not parse (V4-J's
self-contradictory 'floor drift: pins registry=62 expected=62 row=None').

Round 39 (claim C2, seat P3) closes the two arms round 38 left -- the FIELD
shapes of a well-formed-arity row. A row whose path is not a non-empty str
(V4's headline: path=None) was skipped by the `row_path is not None` guards, so
no drift line was appended, main() fell through to `repo / spec[0]` and died
with an uncaught TypeError (exit 1) -- a crash where the pre-round-38 guard
named it exit 2. A row whose floor is not a plain int (floor=(62,) or
floor=True, bool being an int subclass) re-derived the self-contradictory
'floor drift: pins registry=62 expected=(62,) row=(62,)' pair. `row_problem()`
is now the single source of truth for row shape: it names the offending field
once, and neither table's drift check nor the anchor derives anything -- not a
path, not a floor, and not the `repo / spec[0]` join -- from a row it rejects.

DOCUMENTED TRUST BOUNDARY (scout T4). The guard trusts each instrument's own
self-test output -- it detects silent block deletion and count drift, not a
self-test that deliberately prints a fake count; the instruments are the
trusted base of the verification stack. Round 37 extends the boundary to the
anchor: a coordinated edit that also rewrites verifiers/floors-registry.json
is a three-artifact edit and out of scope. `--script NAME=PATH` remains an
explicit operator override -- a probe may point a row at a stub or a temporary
copy -- but an override aimed AT another pinned instrument's canonical path,
or at a path that is not a file, is the same repoint shape reached through
argv and fails loudly (override repoint / override path missing; round 37,
seat P6, fixtures F9-F11). Red-before on this guard: `--script
harness=verifiers/verify_corpus_integrity.py` printed 'PASS harness
observed=119 floor=10' and exited 0; a vanished override target read 'FAIL
harness observed=0 floor=10 summary=missing', exit 1, class unnamed.

Round 40 (claim C2, seat P3) closes V3's two pre-existing residuals -- the arms
that survived r39 because both were inside the boundary as WRITTEN rather than
as ENFORCED. (a) An absolute-argv override aimed at a symlink, hardlink or copy
of another row's instrument was silent-green (V3: 1/24-1/30; E2's A5/A6/A8/A11/
A12; M1's a1-a3): the override is now canonicalized on both spellings and
compared by resolved path AND by content digest, so a symlink lands on the other
row's real path and a hardlink/copy is named by its bytes (F21-F23); a copy of
the row's OWN instrument or a unique-bytes stub stays allowed (F24/F25) -- that
probe affordance is unchanged. (b) `--repo /outside` and `../` traversals read
outside the tree, silently: `confinement_problem()` now names an absolute or
escaping DECLARED path (both the in-file tables and the registry entry, plus a
fail-closed re-check at the `repo / spec[0]` join), while an in-repo `..`
-- the probe-world idiom every seat's mirror world uses -- stays allowed
(F26-F28). Two boundaries are DECLARED here rather than enforced, and named so
they are not mistaken for closures: a symlink INSIDE the tree pointing outside
is not a declared-path escape (a resolved-path confinement test would red every
mirror world), and a `--script` override to a unique-bytes file outside --repo
stays the operator's affordance -- the guard polices the row/registry
declarations, not where a probe's own stub lives. Both were measured before
being declared (out/ARMS-BEFORE.txt, out/MUTANTS.txt).
'''
import argparse
import hashlib
import json
import os
import re
import subprocess
import sys
from pathlib import Path

DEFAULT_REPO = Path(__file__).resolve().parent.parent

# Registry self-check (round 31, scout G2): the guard knows its own expected
# instrument set and floors. A dropped, renamed, or added INSTRUMENTS row --
# or a floor silently lowered -- fails loudly before any self-test runs.
EXPECTED_INSTRUMENTS = {
    "harness": 10,
    "corpus_integrity": 150,
    "corpus_independent": 91,
    "surfaces": 99,
    "checklist": 1845,
    "pins": 62,
    "harness_independent": 115,
    "compare_harness_independent": 330,
    "floors_guard": 150,
}
SELF_TEST_TIMEOUT_S = 120

# Round-37 external anchor (claim C2a): the registry the two in-file tables are
# cross-checked against. Relative to --repo; see registry_anchor_drift().
REGISTRY_REL = Path("verifiers/floors-registry.json")

INSTRUMENTS = {
    "harness": ("verifiers/verify_harness_claims.py", 10,
                r"self-test:\s*(\d+) failure\(s\) over (\d+) assertions", 2, 1),
    "corpus_integrity": ("verifiers/verify_corpus_integrity.py", 150,
                         r"self-test:\s*(\d+) failure\(s\) over (\d+) assertions", 2, 1),
    "corpus_independent": ("verifiers/verify_corpus_independent.py", 91,
                           r"self-test:\s*(\d+) assertions,\s*(\d+) failures", 1, 2),
    "surfaces": ("verifiers/verify_surfaces.py", 99,
                 r"(?m)^(\d+) failure\(s\) over (\d+) assertions$", 2, 1),
    "checklist": ("verifiers/verify_skill_checklist.py", 1845,
                  r"(?m)^(\d+) failure\(s\) over (\d+) assertions$", 2, 1),
    "pins": ("verifiers/check_substrate_pins.py", 62,
             r"(?m)^(\d+) failure\(s\) over (\d+) assertions$", 2, 1),
    "harness_independent": ("verifiers/verify_harness_independent.py", 115,
                            r"(?m)^(\d+) failure\(s\) over (\d+) assertions$", 2, 1),
    "compare_harness_independent": ("verifiers/compare_harness_independent.py", 330,
                                    r"self-test:\s*(\d+) failure\(s\) over (\d+) assertions", 2, 1),
    "floors_guard": ("verifiers/check_assertion_floors.py", 150,
                     r"(?m)^(\d+) failure\(s\) over (\d+) assertions$", 2, 1),
}


def _row_parts(spec):
    '''The (path, floor) a row carries, or (None, None) when its shape is not a
    well-formed 5-field tuple.

    Round-38 claim C2a (V4-J): the anchor must not derive a path or a floor from
    a row whose shape it could not parse. A malformed row is named once by the
    caller; silently reading `row[0]`/`row[1]` off a 4-field tuple produced the
    self-contradictory extras 'path drift ... row=None' and 'floor drift ...
    registry=62 expected=62 row=None'.

    Round 39 (claim C2, seat P3): a 5-field row is not enough -- the two FIELDS
    this function hands out must themselves be usable. V4's headline regression
    was a 5-field row with path=None: `_row_parts()` returned it, the caller's
    `row_path is not None` guards skipped every named line, and main() died at
    `repo / spec[0]`. The path must now be a non-empty str and the floor a plain
    int (bool excluded: it is an int subclass and `floor=True` reads as an
    int-floor row while printing the contradiction). A rejected row yields
    (None, None) so the caller derives nothing from it.
    '''
    if isinstance(spec, tuple) and len(spec) == 5:
        path, floor = spec[0], spec[1]
        if isinstance(path, str) and path and isinstance(floor, int) and not isinstance(floor, bool):
            return path, floor
    return None, None


def row_problem(name, spec):
    '''Name the FIELD that makes a row unusable, or None when the row is sound.

    Round 39 (claim C2, seat P3): one place decides what a sound row is, so the
    two drift checks (registry_drift, registry_anchor_drift), the `repo /
    spec[0]` join in main() and override_drift's canonical map can never
    disagree about which rows to trust. Before this, a row could pass
    `_row_parts()`'s arity test and still reach the join with a None path
    (uncaught TypeError, exit 1) or re-derive the 'registry=62 expected=62'
    contradiction from a malformed floor. The message is built here, so callers
    append it verbatim and cannot re-introduce the contradiction by formatting
    a rejected row's fields.
    '''
    if not (isinstance(spec, tuple) and len(spec) == 5):
        return "malformed row: %s (expected 5-field tuple)" % name
    path, floor = spec[0], spec[1]
    if not (isinstance(path, str) and path):
        return "malformed row: %s (non-string path %r)" % (name, path)
    if not (isinstance(floor, int) and not isinstance(floor, bool)):
        return "malformed row: %s (non-integer floor %r)" % (name, floor)
    return None


def confinement_problem(name, declared, repo, source):
    '''Name the reason a DECLARED instrument path is not confined under --repo,
    or None when it is.

    Round 40 (claim C2, seat P3): V3's residual (b). Both channels declare a
    path (the INSTRUMENTS row and the registry entry) and both are joined as
    `repo / declared`; a path that is absolute, or that traverses out of the
    tree, therefore reads a file OUTSIDE --repo and the guard reruns a foreign
    instrument while printing PASS (red-before, frozen bytes df6ddbc2: a
    `../outside.py` row and an `/abs/outside.py` row each read exit 0, and the
    same shapes read exit 0 with BOTH channels agreeing). The join is
    `Path.__truediv__`, which DISCARDS the left operand for an absolute right
    operand -- so the escape is silent at the join itself. `source` names the
    channel the declaration came from, so a both-channel escape prints one
    line per channel rather than a repeated line.

    The check is lexical on purpose. `os.path.normpath` folds in-repo `..`
    (`verifiers/../verifiers/x.py` stays allowed -- the probe-world idiom), and
    a symlink *inside* the tree pointing outside is NOT named here: the mirror
    idiom (a world whose whole tree is symlinks to the lane) is load-bearing
    for the guard's own fixtures and for every seat's probe worlds, so a
    resolved-path test would red every one of them. What this predicate names
    is the declared path itself leaving --repo.
    '''
    if not isinstance(declared, str) or not declared:
        return None  # shape is row_problem()'s remit, not this predicate's
    if Path(declared).is_absolute():
        return "escape: %s %s declared path %s is absolute (outside %s)" % (
            name, source, declared, repo)
    normalized = os.path.normpath(declared)
    if normalized == ".." or normalized.startswith(".." + os.sep):
        return "escape: %s %s declared path %s traverses outside %s" % (
            name, source, declared, repo)
    return None


def registry_drift(repo=DEFAULT_REPO):
    drift = []
    names = set(INSTRUMENTS)
    # Round-38 claim C2b (V4-S): keys are interpolated into drift strings and
    # passed to sorted(); a non-str key made `"missing row: " + n` raise
    # TypeError (exit 1 traceback, class unnamed). Every key is named here
    # instead, before any concatenation or ordering can touch it.
    for table, mapping in (("INSTRUMENTS", INSTRUMENTS),
                           ("EXPECTED_INSTRUMENTS", EXPECTED_INSTRUMENTS)):
        for k in mapping:
            if not isinstance(k, str):
                drift.append("non-string key: %s has %r (instrument names must be str)"
                             % (table, k))
    if drift:
        return drift
    drift += ["missing row: " + n for n in sorted(EXPECTED_INSTRUMENTS.keys() - names)]
    drift += ["unexpected row: " + n for n in sorted(names - EXPECTED_INSTRUMENTS.keys())]
    for n in sorted(names & EXPECTED_INSTRUMENTS.keys()):
        spec = INSTRUMENTS[n]
        expected_floor = EXPECTED_INSTRUMENTS[n]
        # Round 39 (claim C2, seat P3): both tables are field-checked, not just
        # the INSTRUMENTS row -- EXPECTED_INSTRUMENTS' own value is what the
        # `floor drift` line prints as `expected`, so a bool/None there would
        # reach the same formatting site.
        problem = row_problem(n, spec)
        if problem is not None:
            drift.append(problem)
            continue
        if not (isinstance(expected_floor, int) and not isinstance(expected_floor, bool)):
            drift.append("malformed row: %s (expected-floor is not an integer: %r)"
                         % (n, expected_floor))
            continue
        if spec[1] != expected_floor:
            drift.append("floor drift: %s floor=%r expected=%d" % (n, spec[1], expected_floor))
        # Round 40 (claim C2, seat P3): the tables channel of V3's residual (b).
        # The registry channel is checked in registry_anchor_drift(); both are
        # joined as `repo / declared`, so both must be confined. An in-repo `..`
        # (the probe-world idiom) passes; an absolute or escaping path is named.
        escape = confinement_problem(n, spec[0], repo, "row")
        if escape is not None:
            drift.append(escape)
    return drift


def registry_anchor_drift(repo):
    '''Cross-check both in-file tables against verifiers/floors-registry.json.

    Round-37 claim C2a: the two tables agree with each other by construction,
    so a coordinated edit (row deleted from both, floor lowered in both, path
    repointed) is self-consistent. The anchor is an artifact outside this file;
    every disagreement is named before any self-test runs (exit 2).
    '''
    path = repo / REGISTRY_REL
    try:
        payload = json.loads(path.read_text())
    except OSError as exc:
        return ["absent: %s (%s; the external anchor inventory is required)" % (
            REGISTRY_REL, exc.strerror or exc)]
    except ValueError as exc:
        return ["unreadable: %s: %s" % (REGISTRY_REL, exc)]
    if not isinstance(payload, dict) or not isinstance(payload.get("instruments"), dict):
        return ["malformed: %s (expected an object with an 'instruments' mapping)" % REGISTRY_REL]
    entries = payload["instruments"]
    total = payload.get("instrument_total")
    drift = []
    # No non-str-key arm here: json.loads always yields str object keys, so such
    # a check would be an unexercised arm (round 38, seat P4). The in-file
    # tables are the reachable site for V4-S; a malformed row is handled by
    # row_problem() below.
    if not isinstance(total, int) or isinstance(total, bool):
        drift.append("malformed: %s instrument_total is not an integer" % REGISTRY_REL)
    elif total != len(entries):
        drift.append("size drift: instrument_total=%d but %d entries in %s" % (
            total, len(entries), REGISTRY_REL))
    names = sorted(entries)
    for n in names:
        entry = entries[n]
        if not (isinstance(entry, dict) and isinstance(entry.get("path"), str)
                and entry.get("path")
                and isinstance(entry.get("floor"), int) and not isinstance(entry.get("floor"), bool)):
            drift.append("malformed: %s entry %s (expected {path: str, floor: int})" % (
                REGISTRY_REL, n))
            continue
        if n not in INSTRUMENTS and n not in EXPECTED_INSTRUMENTS:
            drift.append("row vanish: %s (listed in %s, absent from both guard tables)" % (
                n, REGISTRY_REL))
        # Round 40 (claim C2, seat P3): the registry channel of V3's residual
        # (b). The entry's declared path is joined as `repo / entry["path"]`
        # below; an absolute path DISCARDS the repo operand at that join, so
        # the escape has to be named here, before the join. Both channels
        # agreeing on an outside path is exactly the shape E2's A25b and
        # B2's arm B measured green.
        escape = confinement_problem(n, entry["path"], repo, "registry")
        if escape is not None:
            drift.append(escape)
        if n in EXPECTED_INSTRUMENTS and n in INSTRUMENTS:
            # Round 39 (claim C2, seat P3): a row the tables carry but cannot
            # vouch for derives NOTHING here -- not a path, not a floor. Round
            # 38's `row_path is not None` suppression did exactly that for a
            # None path, which is how the crash reached main()'s join. The
            # row's own malformation is named by registry_drift(); naming it
            # again from the anchor would be the self-contradictory pair V4
            # reported.
            spec = INSTRUMENTS[n]
            if row_problem(n, spec) is None and isinstance(EXPECTED_INSTRUMENTS[n], int) \
                    and not isinstance(EXPECTED_INSTRUMENTS[n], bool):
                row_path, row_floor = _row_parts(spec)
                if row_path != entry["path"]:
                    drift.append("path drift: %s registry=%s row=%s" % (
                        n, entry["path"], row_path))
                if row_floor != entry["floor"] or EXPECTED_INSTRUMENTS[n] != entry["floor"]:
                    drift.append("floor drift: %s registry=%r expected=%r row=%r" % (
                        n, entry["floor"], EXPECTED_INSTRUMENTS[n], row_floor))
        target = repo / entry["path"]
        if not (target.is_file() and target.stat().st_size > 0):
            drift.append("path absent: %s %s (declared in %s, not a non-empty file under %s)" % (
                n, entry["path"], REGISTRY_REL, repo))
    for n in sorted(set(INSTRUMENTS) - set(entries)):
        drift.append("extra row: %s (carried by the guard tables, absent from %s)" % (
            n, REGISTRY_REL))
    return drift


def _sha256(path):
    '''Content digest of a file, or None when it cannot be read.'''
    try:
        return hashlib.sha256(path.read_bytes()).hexdigest()
    except OSError:
        return None


def override_drift(overrides, repo):
    '''--script NAME=PATH is the deliberate probe vector (round 37, seat P6): a
    probe may point a row at a stub or a temporary copy, but never at another
    pinned instrument -- the row-path repoint shape of claim C2b reached
    through argv, which the anchor cannot see -- and never at a path that is
    not a regular file. Red-before on this guard (drafts/p6/logs): the foreign
    form read 'PASS harness observed=119 floor=10', exit 0; the vanished form
    read 'FAIL harness observed=0 floor=10 summary=missing', exit 1, and never
    named the class. Rows are anchor-verified by the time this runs, so
    INSTRUMENTS carries the canonical paths.

    Round 40 (claim C2, seat P3) closes V3's residual (a). At r39 bytes
    (df6ddbc2) `main()` kept an ABSOLUTE argv path raw while the canonical map
    is `.resolve()`d, so an override that was a SYMLINK, HARDLINK or byte COPY
    of another row's instrument never compared equal and stayed silent-green
    (V3's 1/24-1/30 measurement; E2's A5/A6/A8/A11/A12 and M1's a1-a3 reproduce
    it). Three layers now run; each closes the class on its own, and the mutant
    battery (drafts/p3/mutants40.py, out/MUTANTS.txt) pins what each is worth:
      * resolved-path equality here (`Path(...).resolve()` on the override,
        `.resolve()`d canonical map): closes the SYMLINK shape -- reverting it
        alone changes nothing only because the two other layers also catch that
        shape (M-ovr-res rc=0);
      * content-digest equality against every other row's canonical instrument:
        the ONLY discriminator for a HARDLINK or a byte COPY -- distinct paths,
        distinct resolutions, identical bytes. Reverting it alone reddens F22
        and F23 (M-digest 6 failures), and it is the only single move that
        does;
      * the join in main() canonicalizes an absolute argv override (see there).
    Reverting all three (M-nores-nodigest) reddens F21 as well, which is what
    proves the symlink shape is closed by the set and not by luck.
    A copy of the row's OWN instrument, or any stub with unique bytes, stays
    allowed: that is the documented probe affordance (F24/F25).
    '''
    canonical = {n: (repo / spec[0]).resolve() for n, spec in INSTRUMENTS.items()
                 if row_problem(n, spec) is None}
    canonical_sha = {n: _sha256(path) for n, path in canonical.items()}
    drift = []
    for name in sorted(overrides):
        path = Path(overrides[name]).resolve()
        digest = _sha256(path) if path.is_file() else None
        for other in sorted(canonical):
            if other == name:
                continue
            if path == canonical[other]:
                drift.append("override repoint: %s -> %s (canonical instrument for %s)"
                             % (name, path, other))
            elif digest is not None and digest == canonical_sha.get(other):
                drift.append("override repoint: %s -> %s (same content as the canonical "
                             "instrument for %s)" % (name, path, other))
        if not path.is_file():
            drift.append("override path missing: %s -> %s (not a file)" % (name, path))
    return drift


def main(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo", type=Path, default=DEFAULT_REPO)
    parser.add_argument("--script", action="append", default=[], metavar="NAME=PATH")
    parser.add_argument("--self-test-timeout", type=float, default=SELF_TEST_TIMEOUT_S,
                        metavar="SECONDS")
    parser.add_argument("--self-test", action="store_true",
                        help="assert the registry/anchor verdicts and exit codes on temporary fixtures only")
    args = parser.parse_args(argv)
    if args.self_test:
        return self_test()
    repo = args.repo.resolve()
    # Round-38 claim C2b (V4-S): a non-str table key is fail-closed BEFORE the
    # anchor runs -- the anchor's own set arithmetic (`sorted(set(...) - set(...))`)
    # would raise TypeError against a mixed-type key, re-opening the crash class
    # this claim closes. registry_drift() reports it, so stop there.
    drift = registry_drift(repo)
    if any(line.startswith("non-string key:") for line in drift):
        for line in drift:
            print("FAIL registry " + line)
        return 2
    drift += registry_anchor_drift(repo)
    if drift:
        for line in drift:
            print("FAIL registry " + line)
        return 2
    # Round 39 (claim C2, seat P3): the join is guarded by row_problem() too, so
    # a row the tables cannot vouch for can never reach `repo / spec[0]` even if
    # a future edit reorders the checks above. Pre-round-39 bytes died here with
    # an uncaught TypeError (V4's headline: exit 1 where r37 named it exit 2).
    # Round 40 (claim C2, seat P3): confinement_problem() is re-checked here as
    # well, for the same reason -- an escape that somehow survived the drift
    # pass must not reach the join, where an absolute operand would silently
    # discard `repo`.
    paths = {}
    for name, spec in INSTRUMENTS.items():
        problem = row_problem(name, spec)
        if problem is not None:
            print("FAIL registry " + problem)
            return 2
        escape = confinement_problem(name, spec[0], repo, "row")
        if escape is not None:
            print("FAIL registry " + escape)
            return 2
        paths[name] = repo / spec[0]
    overrides = {}
    for override in args.script:
        if "=" not in override:
            parser.error("--script must be NAME=PATH")
        name, value = override.split("=", 1)
        if name not in paths:
            parser.error("unknown instrument: " + name)
        # Round 40 (claim C2, seat P3): the override is canonicalized whichever
        # way it was spelled. At r39 bytes an ABSOLUTE argv path was kept raw
        # (only the relative form was resolved), which is why a symlink to
        # another row's instrument stayed silent -- resolve() now runs on both
        # forms, so the symlink case lands on the other row's real path and
        # override_drift()'s path comparison sees it. Hardlinks and byte copies
        # are distinct paths and stay invisible to that comparison; the content
        # digest in override_drift() is what names them.
        path = Path(value)
        path = path.resolve() if path.is_absolute() else (repo / path).resolve()
        overrides[name] = path
        paths[name] = path
    drift = override_drift(overrides, repo)
    if drift:
        for line in drift:
            print("FAIL registry " + line)
        return 2

    failed = False
    run_error = False
    for name, (_, floor, pattern, assertion_group, failure_group) in INSTRUMENTS.items():
        try:
            proc = subprocess.run([sys.executable, str(paths[name]), "--self-test"],
                                  cwd=repo, capture_output=True, text=True,
                                  timeout=args.self_test_timeout)
        except subprocess.TimeoutExpired:
            print("FAIL %s self-test timed out after %gs (hung?)" % (name, args.self_test_timeout))
            run_error = True
            continue
        match = re.search(pattern, proc.stdout)
        assertions = int(match.group(assertion_group)) if match else 0
        failures = int(match.group(failure_group)) if match else None
        ok = match is not None and assertions >= floor and failures == 0 and proc.returncode == 0
        print(("PASS" if ok else "FAIL") + " %s observed=%d floor=%d%s" % (
            name, assertions, floor,
            "" if failures == 0 else " summary=missing" if match is None
            else " self_test_failures=%d" % failures))
        failed |= not ok
    if run_error:
        return 2
    return 1 if failed else 0


def self_test() -> int:
    '''Fixture battery on tempdir copies -- the live tree is never written.

    True discriminators for the round-37 coordinated shapes (F1 a row deleted
    from BOTH tables, F2 a floor lowered in BOTH, F3 a row path repointed):
    each asserts a loud, class-named exit 2 that the pre-round-37 guard read as
    exit 0 (scouts C2/M7). F4-F6 pin the pre-existing one-table class, the
    fail-closed absent anchor, and the registry's own size; F7 is a hermetic
    all-green control in a one-instrument stub world; F8 covers the
    removed-instrument-file arm. F9-F11 pin the --script override vector.

    Round 38 (claim C2, seat P4) adds the two true discriminators for V4's
    residuals: F12 a non-str key in a guard table (red-before: an uncaught
    TypeError traceback, exit 1, class unnamed) and F13 a malformed row shape
    (red-before: the named malformed-row line PLUS the self-contradictory
    'path drift ... row=None' / 'floor drift ... registry=62 expected=62
    row=None' pair). Mutation anchors are count-checked, so a no-op mutation
    cannot masquerade as a passing fixture.

    Round 39 (claim C2, seat P3) adds the FIELD arms of that class: F16 a
    5-field row with path=None (red-before on the landed r38 bytes: an uncaught
    TypeError at `repo / spec[0]`, exit 1 -- where the r37 PREFIX guard named it
    exit 2), F17 floor=(62,), F18 floor=True (both red-before on both revisions:
    the derived 'floor drift ... registry=62 expected=... row=...' pair, and for
    F18 no malformed line at all), F19 a non-str non-None path, and F20 the
    predicate itself over twelve shapes, so a regression names the cause rather
    than only reddening a fixture.

    Round 40 (claim C2, seat P3) adds V3's two pre-existing residuals. The
    override arms F21-F25 use a two-row stub world whose stubs have DISTINCT
    bytes, because the digest comparison needs "another row's target" to differ
    from "the row's own target": F21 an absolute-argv symlink to another row's
    instrument, F22 a byte copy, F23 a hardlink (all red-before: exit 0,
    out/ARMS-BEFORE.txt), F24 a copy of the row's OWN instrument and F25 a
    unique-bytes stub outside --repo (both still allowed -- the probe
    affordance). F26-F28 cover path confinement: a `../` declaration and an
    absolute declaration each named on BOTH channels (red-before: exit 0 with
    both channels agreeing), and an in-repo `..` control that must stay allowed
    (the mirror-world idiom). F29 pins confinement_problem() over ten shapes.
    The override closure is LAYERED, so the mutant battery is compound as well
    as single-move (drafts/p3/mutants40.py, out/MUTANTS.txt): M-digest alone
    reddens F22/F23, M-row-esc and M-reg-esc each redden F26/F27, while F21's
    symlink shape needs M-nores-nodigest (both resolves AND the digest) to
    redden -- recorded, because a single-move revert there is masked by the
    other layers rather than harmless.
    '''
    import tempfile

    failures = []
    total = 0

    def rec(what, ok, got):
        nonlocal total
        total += 1
        if not ok:
            failures.append("%s: got %r" % (what, got))

    try:
        registry_text = (Path(__file__).resolve().parent / REGISTRY_REL.name).read_text()
    except OSError as exc:
        print("1 failure(s) over 1 assertions")
        print("FAIL: cannot read the anchor %s beside this script: %s" % (REGISTRY_REL.name, exc))
        return 1

    source = Path(__file__).read_text()

    # Fixture anchors are assembled from fragments: a joined anchor must not
    # appear anywhere else in this file's own text, or the count-checked swap
    # would find a literal here instead of the table row it targets.
    def anchor(*fragments):
        return "".join(fragments)

    expected_pins = anchor('    "pi', 'ns": 62,\n')
    row_pins = anchor('    "pins": ("verifiers/check_substrate',
                      '_pins.py", 62,\n',
                      '             r"(?m)^(\\d+) failure\\(s\\) over',
                      ' (\\d+) assertions$", 2, 1),\n')
    expected_surfaces = anchor('    "surfa', 'ces": 99,\n')
    row_surfaces = anchor('    "surfaces": ("verifiers/verify_surfa', 'ces.py", 99,\n')
    expected_ind = anchor('    "harness_indep',
                          'endent": %d,\n' % EXPECTED_INSTRUMENTS["harness_independent"])
    row_ind = anchor('    "harness_independent": ("verifiers/verify_harness_indep',
                     'endent.py", %d,\n' % INSTRUMENTS["harness_independent"][1],
                     '                            r"(?m)^(\\d+) failure\\(s\\) over',
                     ' (\\d+) assertions$", 2, 1),\n')
    entry_anchor = anchor('if __name__', ' == "__main__":')
    summary_pattern = r"(?m)^(\d+) failure\(s\) over (\d+) assertions$"
    hermetic_tables = (
        'INSTRUMENTS = {"stub": ("verifiers/stub-instrument.py", 3, %r, 2, 1)}\n'
        'EXPECTED_INSTRUMENTS = {"stub": 3}\n\n' % summary_pattern)
    stub_registry = json.dumps({"instrument_total": 1, "instruments": {
        "stub": {"path": "verifiers/stub-instrument.py", "floor": 3}}})
    stub_script = ("print('0 failure(s) over 3 assertions')\n"
                   "raise SystemExit(0)\n")

    def swap(text, old, new, label):
        n = text.count(old)
        rec("mutation anchor lands exactly once (%s)" % label, n == 1, n)
        return text.replace(old, new) if n == 1 else text

    def write_tree(root, text, reg):
        verifiers_dir = root / "verifiers"
        verifiers_dir.mkdir(parents=True, exist_ok=True)
        script = verifiers_dir / "check_assertion_floors.py"
        script.write_text(text)
        if reg is not None:
            (verifiers_dir / REGISTRY_REL.name).write_text(reg)
        return script

    def run(script, repo):
        return subprocess.run([sys.executable, str(script), "--repo", str(repo)],
                              cwd=str(repo), capture_output=True, text=True,
                              timeout=SELF_TEST_TIMEOUT_S)

    with tempfile.TemporaryDirectory(prefix="floors-selftest-") as tmp:
        tmp = Path(tmp)

        # F1 -- row deleted from BOTH tables (claim C2a's shape; red-before: exit 0)
        text = swap(source, expected_pins, "", "F1/expected")
        text = swap(text, row_pins, "", "F1/instruments")
        rec("F1 mutation dropped exactly the two table rows",
            len(source) - len(text) == len(expected_pins) + len(row_pins),
            len(source) - len(text))
        proc = run(write_tree(tmp / "f1", text, registry_text), DEFAULT_REPO)
        rec("F1 two-table deletion: exit 2", proc.returncode == 2, proc.returncode)
        rec("F1 two-table deletion: names the class and the row",
            "FAIL registry row vanish: pins" in proc.stdout, proc.stdout)
        rec("F1 two-table deletion: no instrument reran", "PASS " not in proc.stdout,
            proc.stdout)
        rec("F1 two-table deletion: no Traceback",
            "Traceback" not in proc.stdout + proc.stderr, proc.stdout + proc.stderr)

        # F2 -- floor lowered in BOTH tables (M7's second arm)
        text = swap(source, expected_surfaces, '    "surfaces": 10,\n', "F2/expected")
        text = swap(text, row_surfaces, '    "surfaces": ("verifiers/verify_surfaces.py", 10,\n',
                    "F2/instruments")
        proc = run(write_tree(tmp / "f2", text, registry_text), DEFAULT_REPO)
        rec("F2 both-table floor downgrade: exit 2", proc.returncode == 2, proc.returncode)
        rec("F2 both-table floor downgrade: names the class and the row",
            "FAIL registry floor drift: surfaces" in proc.stdout, proc.stdout)
        rec("F2 both-table floor downgrade: no instrument reran", "PASS " not in proc.stdout,
            proc.stdout)

        # F3 -- row path repointed at a foreign instrument (claim C2b's shape)
        text = swap(source, row_pins,
                    row_pins.replace("check_substrate_pins.py", "verify_skill_checklist.py"),
                    "F3/repoint")
        proc = run(write_tree(tmp / "f3", text, registry_text), DEFAULT_REPO)
        rec("F3 repointed row: exit 2", proc.returncode == 2, proc.returncode)
        rec("F3 repointed row: names the class and the row",
            "FAIL registry path drift: pins" in proc.stdout, proc.stdout)
        rec("F3 repointed row: no instrument reran", "PASS " not in proc.stdout, proc.stdout)

        # F4 -- pre-existing one-table deletion still fails loudly (regression pin)
        text = swap(source, expected_pins, "", "F4/expected-only")
        proc = run(write_tree(tmp / "f4", text, registry_text), DEFAULT_REPO)
        rec("F4 one-table deletion: exit 2", proc.returncode == 2, proc.returncode)
        rec("F4 one-table deletion: keeps the old class wording",
            "FAIL registry unexpected row: pins" in proc.stdout, proc.stdout)

        # F5 -- anchor absent is fail-closed, named
        proc = run(write_tree(tmp / "f5", source, None), tmp / "f5")
        rec("F5 absent anchor: exit 2", proc.returncode == 2, proc.returncode)
        rec("F5 absent anchor: named with the path",
            "FAIL registry absent: verifiers/floors-registry.json" in proc.stdout, proc.stdout)

        # F6 -- the registry's own declared size is load-bearing. The anchor is
        # the live registry's own declared total (round 41: 9, including this
        # guard's self-test); a stale literal here would stop landing and the
        # count-check would name it.
        text = swap(registry_text, '"instrument_total": 9', '"instrument_total": 8',
                    "F6/total")
        proc = run(write_tree(tmp / "f6", source, text), tmp / "f6")
        rec("F6 size drift: exit 2", proc.returncode == 2, proc.returncode)
        rec("F6 size drift: names the class", "FAIL registry size drift" in proc.stdout,
            proc.stdout)

        # F7 -- hermetic all-green control: one stub instrument, byte-exact stdout
        text = swap(source, entry_anchor, hermetic_tables + entry_anchor, "F7/tables")
        script = write_tree(tmp / "f7", text, stub_registry)
        (tmp / "f7" / "verifiers" / "stub-instrument.py").write_text(stub_script)
        proc = run(script, tmp / "f7")
        rec("F7 stub world: exit 0", proc.returncode == 0, proc.returncode)
        rec("F7 stub world: exact single PASS line",
            proc.stdout == "PASS stub observed=3 floor=3\n", proc.stdout)
        rec("F7 stub world: clean stderr", proc.stderr == "", proc.stderr)

        # F8 -- declared instrument file removed: named before any run
        proc = run(write_tree(tmp / "f8", source, registry_text), tmp / "f8")
        rec("F8 removed instrument file: exit 2", proc.returncode == 2, proc.returncode)
        rec("F8 removed instrument file: names the row and class",
            "FAIL registry path absent: pins" in proc.stdout, proc.stdout)

        # F9/F10/F11 (seat P6) -- the --script override vector reaches the same
        # repoint shape the anchor cannot see: it is argv, not a table edit. The
        # world is a two-row stub (hermetic), so no fixture depends on the live
        # tree; red-before on this guard, F9's shape read 'PASS harness
        # observed=119 floor=10', exit 0, and F10's read 'FAIL harness
        # observed=0 floor=10 summary=missing', exit 1, class unnamed.
        two_row_tables = (
            'INSTRUMENTS = {"stub": ("verifiers/stub-instrument.py", 3, %r, 2, 1),\n'
            '               "stub2": ("verifiers/stub-instrument-2.py", 3, %r, 2, 1)}\n'
            'EXPECTED_INSTRUMENTS = {"stub": 3, "stub2": 3}\n\n'
            % (summary_pattern, summary_pattern))
        two_row_registry = json.dumps({"instrument_total": 2, "instruments": {
            "stub": {"path": "verifiers/stub-instrument.py", "floor": 3},
            "stub2": {"path": "verifiers/stub-instrument-2.py", "floor": 3}}})

        def two_row_world(name):
            text = swap(source, entry_anchor, two_row_tables + entry_anchor, name + "/tables")
            script = write_tree(tmp / name, text, two_row_registry)
            for stub_name in ("stub-instrument.py", "stub-instrument-2.py"):
                (tmp / name / "verifiers" / stub_name).write_text(stub_script)
            return script

        def run_override(script, repo, override):
            return subprocess.run(
                [sys.executable, str(script), "--repo", str(repo), "--script", override],
                cwd=str(repo), capture_output=True, text=True, timeout=SELF_TEST_TIMEOUT_S)

        proc = run_override(two_row_world("f9"), tmp / "f9",
                            "stub=verifiers/stub-instrument-2.py")
        rec("F9 override repoint: exit 2", proc.returncode == 2, proc.returncode)
        rec("F9 override repoint: names the class and the row",
            "FAIL registry override repoint: stub" in proc.stdout, proc.stdout)
        rec("F9 override repoint: no instrument reran", "PASS " not in proc.stdout,
            proc.stdout)

        proc = run_override(two_row_world("f10"), tmp / "f10",
                            "stub=verifiers/stub-instrument-gone.py")
        rec("F10 override path missing: exit 2", proc.returncode == 2, proc.returncode)
        rec("F10 override path missing: names the class and the row",
            "FAIL registry override path missing: stub" in proc.stdout, proc.stdout)
        rec("F10 override path missing: no instrument reran", "PASS " not in proc.stdout,
            proc.stdout)

        # F11 -- the probe affordances survive: a non-canonical stub copy and a
        # row's own canonical path stay allowed; only another pinned row is not.
        rec("F11 a non-canonical stub override is still allowed",
            override_drift({"stub": tmp / "f9" / "verifiers" / "stub-instrument-2.py"},
                           DEFAULT_REPO) == [],
            override_drift({"stub": tmp / "f9" / "verifiers" / "stub-instrument-2.py"},
                           DEFAULT_REPO))
        rec("F11 a row's own canonical override is still allowed",
            override_drift({"pins": DEFAULT_REPO / "verifiers/check_substrate_pins.py"},
                           DEFAULT_REPO) == [],
            override_drift({"pins": DEFAULT_REPO / "verifiers/check_substrate_pins.py"},
                           DEFAULT_REPO))
        rec("F11 another pinned row's path is named by the predicate",
            any("override repoint: harness" in line for line in override_drift(
                {"harness": DEFAULT_REPO / "verifiers/verify_corpus_integrity.py"},
                DEFAULT_REPO)),
            override_drift(
                {"harness": DEFAULT_REPO / "verifiers/verify_corpus_integrity.py"},
                DEFAULT_REPO))

        # F12 (round 38, seat P4) -- a non-str key in either guard table. Red-
        # before on the landed r37 bytes (probes/S-nonstr-key.py): the key hit
        # `"missing row: " + n` and `sorted()` unguarded -> TypeError traceback,
        # exit 1, no class named. Both tables are exercised: the early return
        # must fire before any concatenation or ordering touches a key.
        f12_expected = swap(source, expected_pins, '    None: 7,\n' + expected_pins,
                            "F12/expected-key")
        proc = run(write_tree(tmp / "f12a", f12_expected, registry_text), DEFAULT_REPO)
        rec("F12a non-str key (EXPECTED): exit 2", proc.returncode == 2, proc.returncode)
        rec("F12a non-str key (EXPECTED): names the class, the table and the key",
            "FAIL registry non-string key: EXPECTED_INSTRUMENTS has None" in proc.stdout,
            proc.stdout)
        rec("F12a non-str key (EXPECTED): no Traceback",
            "Traceback" not in proc.stdout + proc.stderr, proc.stdout + proc.stderr)
        rec("F12a non-str key (EXPECTED): no instrument reran", "PASS " not in proc.stdout,
            proc.stdout)

        f12_instruments = swap(source, row_pins, '    None: ("x", 1),\n' + row_pins,
                               "F12/instruments-key")
        proc = run(write_tree(tmp / "f12b", f12_instruments, registry_text), DEFAULT_REPO)
        rec("F12b non-str key (INSTRUMENTS): exit 2", proc.returncode == 2, proc.returncode)
        rec("F12b non-str key (INSTRUMENTS): names the class, the table and the key",
            "FAIL registry non-string key: INSTRUMENTS has None" in proc.stdout, proc.stdout)
        rec("F12b non-str key (INSTRUMENTS): no Traceback",
            "Traceback" not in proc.stdout + proc.stderr, proc.stdout + proc.stderr)
        rec("F12b non-str key (INSTRUMENTS): no instrument reran", "PASS " not in proc.stdout,
            proc.stdout)

        # F13 (round 38, seat P4) -- a malformed row shape. Red-before on the
        # landed r37 bytes (probes/J-malformed-tuple.py): the named malformed-row
        # line PLUS 'path drift: pins ... row=None' and the self-contradictory
        # 'floor drift: pins registry=62 expected=62 row=None' (V4-J). The anchor
        # must name the shape once and derive nothing from it.
        malformed_row = anchor('    "pins": ("verifiers/check_substrate', '_pins.py", 62),\n')
        text = swap(source, row_pins, malformed_row, "F13/malformed")
        proc = run(write_tree(tmp / "f13", text, registry_text), DEFAULT_REPO)
        rec("F13 malformed row: exit 2", proc.returncode == 2, proc.returncode)
        rec("F13 malformed row: names the class and the row",
            "FAIL registry malformed row: pins" in proc.stdout, proc.stdout)
        # The discriminator is the *derived* pair, not a total line count: an
        # unrelated live drift line (another seat mid-bump) must not turn this
        # fixture red, while any path/floor reading taken off the unparsed row
        # must. Red-before on the landed r37 bytes: both lines present.
        rec("F13 malformed row: no derived path/floor line",
            "path drift: pins" not in proc.stdout and "floor drift: pins" not in proc.stdout,
            proc.stdout)
        rec("F13 malformed row: no derived contradiction",
            "row=None" not in proc.stdout, proc.stdout)
        rec("F13 malformed row: no instrument reran", "PASS " not in proc.stdout, proc.stdout)

        # F14/F15 (round 38, claim C1f, seat P3) -- the two newly registered C1
        # instruments must be covered by the SAME anchor as the original six.
        # Without these, adding a row to both in-file tables but not to the
        # registry (or vice versa) is exactly the half-bump the anchor exists to
        # catch, and the newest rows are where a half-bump is likeliest.
        # F14 drops the new row from BOTH in-file tables: the anchor must name
        # the vanish, not silently keep rerunning nothing.
        text = swap(source, expected_ind, "", "F14/expected")
        text = swap(text, row_ind, "", "F14/instruments")
        rec("F14 mutation dropped exactly the two new table rows",
            len(source) - len(text) == len(expected_ind) + len(row_ind),
            len(source) - len(text))
        proc = run(write_tree(tmp / "f14", text, registry_text), DEFAULT_REPO)
        rec("F14 new-row two-table deletion: exit 2", proc.returncode == 2, proc.returncode)
        rec("F14 new-row two-table deletion: names the class and the row",
            "FAIL registry row vanish: harness_independent" in proc.stdout, proc.stdout)
        rec("F14 new-row two-table deletion: no instrument reran",
            "PASS " not in proc.stdout, proc.stdout)
        rec("F14 new-row two-table deletion: no Traceback",
            "Traceback" not in proc.stdout + proc.stderr, proc.stdout + proc.stderr)

        # F15 repoints the new row's path at a foreign instrument. A new row is
        # the cheapest place to hide a repoint, because its path has no history
        # to diff against; the anchor must compare the path, not just the floor.
        # The target is chosen to make the repoint GENUINELY silent without the
        # anchor: verify_surfaces.py prints the same summary pattern (87
        # assertions then; 99 since round 47), so the no-anchor world reads 'PASS harness_independent
        # observed=87 floor=71', exit 0 (proved by drafts/p3/true_discriminator.py).
        text = swap(source, row_ind,
                    row_ind.replace("verify_harness_independent.py",
                                    "verify_surfaces.py"),
                    "F15/repoint")
        proc = run(write_tree(tmp / "f15", text, registry_text), DEFAULT_REPO)
        rec("F15 new-row repointed path: exit 2", proc.returncode == 2, proc.returncode)
        rec("F15 new-row repointed path: names the class and the row",
            "FAIL registry path drift: harness_independent" in proc.stdout, proc.stdout)
        rec("F15 new-row repointed path: no instrument reran",
            "PASS " not in proc.stdout, proc.stdout)

        # F16-F19 (round 39, claim C2, seat P3) -- the FIELD shapes of a
        # well-formed-arity row. Round 38's F12/F13 cover a non-str KEY and a
        # short row; neither covers a bad VALUE inside a 5-field row, which is
        # where V4 found both surviving arms. Red-before per arm (reproduced by
        # drafts/p3/probe_arms.py; outputs in drafts/p3/out/before/ and
        # out/prefix/ -- the r37 bytes 162006498182 are the PREFIX guard):
        #   F16 path=None  -> on the landed r38 bytes eaf5bf46b61f an uncaught
        #                     TypeError at `repo / spec[0]`, exit 1; the r37
        #                     PREFIX guard named it exit 2 instead, so the fix
        #                     had turned a named failure into a crash.
        #   F17 floor=(62,) -> on BOTH revisions: 'malformed row' PLUS the
        #                     self-contradictory 'floor drift: pins registry=62
        #                     expected=(62,) row=(62,)' -- never closed by r38.
        #   F18 floor=True  -> on BOTH revisions: no malformed line at all (bool
        #                     is an int subclass), only 'floor drift: pins
        #                     registry=62 expected=True row=True'.
        # The discriminator is the *derived* line, not a line count: an unrelated
        # live drift line must not turn these red, while any path/floor reading
        # taken off a rejected row must.
        def variant(row, old, new, label):
            '''A row mutated in ONE field, with the inner swap count-checked too:
            a `replace()` that silently matched nothing would leave the row sound
            and the fixture would pass for the wrong reason (the same no-op
            hazard `swap()` guards against one level up).'''
            n = row.count(old)
            rec("F16-F19 field anchor lands exactly once (%s)" % label, n == 1, n)
            return row.replace(old, new) if n == 1 else row

        bad_path = variant(row_pins, '"verifiers/check_substrate_pins.py"', "None", "F16")
        text = swap(source, row_pins, bad_path, "F16/none-path")
        proc = run(write_tree(tmp / "f16", text, registry_text), DEFAULT_REPO)
        rec("F16 None row path: exit 2", proc.returncode == 2, proc.returncode)
        rec("F16 None row path: names the class, the row and the field",
            "FAIL registry malformed row: pins (non-string path None)" in proc.stdout,
            proc.stdout)
        rec("F16 None row path: no Traceback",
            "Traceback" not in proc.stdout + proc.stderr, proc.stdout + proc.stderr)
        rec("F16 None row path: no derived path/floor line",
            "path drift: pins" not in proc.stdout and "floor drift: pins" not in proc.stdout,
            proc.stdout)
        rec("F16 None row path: no instrument reran", "PASS " not in proc.stdout, proc.stdout)

        # F17: a well-formed 5-field row whose FLOOR is a nested tuple, in BOTH
        # tables (V4-H2's shape). Both, because the registry's own line prints
        # the EXPECTED table's value as `expected` -- mutating one table only
        # would leave the other half of the contradiction untested.
        nested_floor_row = variant(row_pins, '_pins.py", 62,\n', '_pins.py", (62,),\n', "F17")
        text = swap(source, row_pins, nested_floor_row, "F17/nested-floor-row")
        text = swap(text, expected_pins, '    "pins": (62,),\n', "F17/nested-floor-expected")
        proc = run(write_tree(tmp / "f17", text, registry_text), DEFAULT_REPO)
        rec("F17 nested-tuple floor: exit 2", proc.returncode == 2, proc.returncode)
        rec("F17 nested-tuple floor: names the class, the row and the field",
            "FAIL registry malformed row: pins (non-integer floor (62,))" in proc.stdout,
            proc.stdout)
        rec("F17 nested-tuple floor: no derived floor line",
            "floor drift: pins" not in proc.stdout, proc.stdout)
        rec("F17 nested-tuple floor: no self-contradiction",
            "expected=62 row=62" not in proc.stdout, proc.stdout)
        rec("F17 nested-tuple floor: no instrument reran", "PASS " not in proc.stdout,
            proc.stdout)

        # F18: floor=True in BOTH tables (V4-H4's shape). bool is an int
        # subclass, so r38's isinstance floor test passed and the row reached the
        # drift formatting site with no malformed line at all.
        bool_floor_row = variant(row_pins, '_pins.py", 62,\n', '_pins.py", True,\n', "F18")
        text = swap(source, row_pins, bool_floor_row, "F18/bool-floor-row")
        text = swap(text, expected_pins, '    "pins": True,\n', "F18/bool-floor-expected")
        proc = run(write_tree(tmp / "f18", text, registry_text), DEFAULT_REPO)
        rec("F18 bool floor: exit 2", proc.returncode == 2, proc.returncode)
        rec("F18 bool floor: names the class, the row and the field",
            "FAIL registry malformed row: pins (non-integer floor True)" in proc.stdout,
            proc.stdout)
        rec("F18 bool floor: no derived floor line",
            "floor drift: pins" not in proc.stdout, proc.stdout)
        rec("F18 bool floor: no self-contradiction",
            "expected=True row=True" not in proc.stdout, proc.stdout)
        rec("F18 bool floor: no instrument reran", "PASS " not in proc.stdout, proc.stdout)

        # F19: a non-str path that is NOT None (V4's PATH-VALUE-BOUND: int/bool
        # named rc=2 pre-fix as 'path drift ... row=7'). The exit code is
        # unchanged, but the class is now the accurate one -- an unusable field,
        # not a repoint -- so the drift line the anchor used to print off an
        # unvouched row is gone.
        text = swap(source, row_pins,
                    variant(row_pins, '"verifiers/check_substrate_pins.py"', "7", "F19"),
                    "F19/int-path")
        proc = run(write_tree(tmp / "f19", text, registry_text), DEFAULT_REPO)
        rec("F19 int row path: exit 2", proc.returncode == 2, proc.returncode)
        rec("F19 int row path: names the class, the row and the field",
            "FAIL registry malformed row: pins (non-string path 7)" in proc.stdout,
            proc.stdout)
        rec("F19 int row path: no derived path line",
            "path drift: pins" not in proc.stdout, proc.stdout)
        rec("F19 int row path: no instrument reran", "PASS " not in proc.stdout, proc.stdout)

        # F20 -- the predicate itself, pinned independently of the subprocess
        # path: every row shape F16-F19 reach through the tables, plus the sound
        # shape that must stay silent. A regression that let a bad field read as
        # sound would turn every F16-F19 fixture red at once, but this names the
        # cause directly.
        sound = ("verifiers/check_substrate_pins.py", 62, r"x", 2, 1)
        cases = [
            (sound, None),
            (("verifiers/check_substrate_pins.py", 62), "expected 5-field tuple"),
            (("verifiers/check_substrate_pins.py", 62, r"x", 2), "expected 5-field tuple"),
            ((None, 62, r"x", 2, 1), "non-string path None"),
            ((7, 62, r"x", 2, 1), "non-string path 7"),
            (("", 62, r"x", 2, 1), "non-string path ''"),
            (("verifiers/check_substrate_pins.py", (62,), r"x", 2, 1), "non-integer floor (62,)"),
            (("verifiers/check_substrate_pins.py", True, r"x", 2, 1), "non-integer floor True"),
            (("verifiers/check_substrate_pins.py", None, r"x", 2, 1), "non-integer floor None"),
            (("verifiers/check_substrate_pins.py", 62.0, r"x", 2, 1), "non-integer floor 62.0"),
            ("not-a-tuple", "expected 5-field tuple"),
        ]
        for spec, expected in cases:
            got = row_problem("pins", spec)
            want = None if expected is None else "malformed row: pins (%s)" % expected
            rec("F20 row_problem(%r) -> %r" % (spec, want), got == want, got)
        rec("F20 a sound row yields no problem", row_problem("pins", sound) is None,
            row_problem("pins", sound))

        # F21-F25 (round 40, claim C2, seat P3) -- V3's residual (a), the
        # absolute-argv override channel. Red-before on the frozen bytes
        # (df6ddbc2, rebuilt probe drafts/p3/arms40.py, out/ARMS-BEFORE.txt):
        # an absolute-argv SYMLINK, byte COPY or HARDLINK of another row's
        # instrument each read exit 0 with PASS lines (V3: 1/24-1/30 green;
        # E2's A5/A6/A8/A11/A12 and M1's a1-a3 reproduce it). The r39 `main()`
        # kept an absolute argv path raw while the canonical map is resolved,
        # so the symlink never compared equal; a hardlink or byte copy is a
        # distinct path with a distinct resolution in any case, so the closure
        # needs BOTH the resolve (symlink) and the content digest (copy /
        # hardlink). The two-row world here gives the stubs DISTINCT bytes: in
        # the older F9 world both stubs were byte-identical, which would make
        # "a copy of the row's OWN instrument" indistinguishable from a copy of
        # the other row's -- the digest check needs the difference to be real.
        stub_alt_script = ("print('0 failure(s) over 4 assertions')\n"
                           "raise SystemExit(0)\n")
        distinct_tables = (
            'INSTRUMENTS = {"stub": ("verifiers/stub-instrument.py", 3, %r, 2, 1),\n'
            '               "stub2": ("verifiers/stub-instrument-2.py", 4, %r, 2, 1)}\n'
            'EXPECTED_INSTRUMENTS = {"stub": 3, "stub2": 4}\n\n'
            % (summary_pattern, summary_pattern))
        distinct_registry = json.dumps({"instrument_total": 2, "instruments": {
            "stub": {"path": "verifiers/stub-instrument.py", "floor": 3},
            "stub2": {"path": "verifiers/stub-instrument-2.py", "floor": 4}}})

        def distinct_world(name):
            text = swap(source, entry_anchor, distinct_tables + entry_anchor, name + "/tables")
            script = write_tree(tmp / name, text, distinct_registry)
            (tmp / name / "verifiers" / "stub-instrument.py").write_text(stub_script)
            (tmp / name / "verifiers" / "stub-instrument-2.py").write_text(stub_alt_script)
            return script

        # F21 -- absolute-argv symlink to another row's target. Red-before on the
        # frozen bytes: raw absolute path, no comparison, exit 0 (out/ARMS-BEFORE.txt
        # W3; E2's A11, M1's a1). The closure is LAYERED: the symlink shape is
        # caught by any one of main()'s resolve, override_drift's own resolve, or
        # the content digest, so reverting one layer alone leaves this fixture
        # green (M-resolve/M-ovr-res/M-digest each rc=0 on F21 -- measured, see
        # out/MUTANTS.txt). The compound mutant M-nores-nodigest, which reverts
        # both resolves AND the digest, is what reddens it; that is the true
        # discriminator for this fixture, and it is recorded rather than hidden.
        link = tmp / "f21" / "verifiers" / "link-to-stub2.py"
        script = distinct_world("f21")
        link.symlink_to("stub-instrument-2.py")
        proc = run_override(script, tmp / "f21", "stub=%s" % link)
        rec("F21 abs-argv symlink to another row: exit 2", proc.returncode == 2, proc.returncode)
        rec("F21 abs-argv symlink to another row: names the class and the row",
            "FAIL registry override repoint: stub" in proc.stdout
            and "canonical instrument for stub2" in proc.stdout, proc.stdout)
        rec("F21 abs-argv symlink to another row: no instrument reran",
            "PASS " not in proc.stdout, proc.stdout)

        # F22 -- absolute-argv byte copy of another row's target. Distinct path,
        # distinct resolution: only the content digest can name it.
        script = distinct_world("f22")
        copy2 = tmp / "f22" / "copy-of-stub2.py"
        copy2.write_bytes((tmp / "f22" / "verifiers" / "stub-instrument-2.py").read_bytes())
        proc = run_override(script, tmp / "f22", "stub=%s" % copy2)
        rec("F22 abs-argv byte copy of another row: exit 2", proc.returncode == 2,
            proc.returncode)
        rec("F22 abs-argv byte copy of another row: names the class, row and cause",
            "FAIL registry override repoint: stub" in proc.stdout
            and "same content as the canonical instrument for stub2" in proc.stdout,
            proc.stdout)
        rec("F22 abs-argv byte copy of another row: no instrument reran",
            "PASS " not in proc.stdout, proc.stdout)

        # F23 -- absolute-argv hardlink of another row's target (same closure
        # path as F22; a separate fixture because a hardlink and a copy fail
        # differently under a resolve-only design).
        script = distinct_world("f23")
        hard = tmp / "f23" / "hardlink-of-stub2.py"
        os.link(tmp / "f23" / "verifiers" / "stub-instrument-2.py", hard)
        proc = run_override(script, tmp / "f23", "stub=%s" % hard)
        rec("F23 abs-argv hardlink to another row: exit 2", proc.returncode == 2,
            proc.returncode)
        rec("F23 abs-argv hardlink to another row: names the class, row and cause",
            "FAIL registry override repoint: stub" in proc.stdout
            and "same content as the canonical instrument for stub2" in proc.stdout,
            proc.stdout)
        rec("F23 abs-argv hardlink to another row: no instrument reran",
            "PASS " not in proc.stdout, proc.stdout)

        # F24 -- the affordance survives: an absolute-argv byte copy of the row's
        # OWN instrument stays allowed (it is the same program, and the digest
        # loop skips the row itself).
        script = distinct_world("f24")
        own = tmp / "f24" / "copy-of-own.py"
        own.write_bytes((tmp / "f24" / "verifiers" / "stub-instrument.py").read_bytes())
        proc = run_override(script, tmp / "f24", "stub=%s" % own)
        rec("F24 abs-argv copy of the row's OWN instrument: still allowed",
            proc.returncode == 0, proc.returncode)
        rec("F24 abs-argv copy of the row's OWN instrument: both rows reran",
            "PASS stub observed=3 floor=3" in proc.stdout
            and "PASS stub2 observed=4 floor=4" in proc.stdout, proc.stdout)

        # F25 -- and a unique-bytes stub outside --repo stays allowed: this is
        # the documented operator affordance, and the boundary this round does
        # NOT move. A tweaked copy of another instrument (E2's A9) is this same
        # shape -- different bytes, hence a different program, hence a stub.
        outside_stub = tmp / "unique-outside-instrument.py"
        outside_stub.write_text("print('0 failure(s) over 5 assertions')\n"
                                "raise SystemExit(0)\n")
        script = distinct_world("f25")
        proc = run_override(script, tmp / "f25", "stub=%s" % outside_stub)
        rec("F25 unique-bytes stub outside --repo: still allowed",
            proc.returncode == 0, proc.returncode)
        rec("F25 unique-bytes stub outside --repo: the stub reran",
            "PASS stub observed=5 floor=3" in proc.stdout, proc.stdout)

        # F26/F27/F28 (round 40, claim C2, seat P3) -- V3's residual (b), path
        # confinement. Red-before on the frozen bytes: a `../outside.py` row and
        # an `/abs/outside.py` row each read exit 0 with BOTH channels agreeing
        # (out/ARMS-BEFORE.txt C1/C2; E2's A25b and B2's arm B measured the same
        # green). The discriminator is the class name, so each arm asserts the
        # channel word ("row" / "registry") as well as the shape word.
        def escape_world(name, declared_path):
            outside = tmp / ("%s-outside-instrument.py" % name)
            outside.write_text(stub_script)
            tables = ('INSTRUMENTS = {"stub": (%r, 3, %r, 2, 1)}\n'
                      'EXPECTED_INSTRUMENTS = {"stub": 3}\n\n' % (declared_path, summary_pattern))
            registry = json.dumps({"instrument_total": 1, "instruments": {
                "stub": {"path": declared_path, "floor": 3}}})
            text = swap(source, entry_anchor, tables + entry_anchor, name + "/tables")
            script = write_tree(tmp / name, text, registry)
            # The in-repo control's declared path lands on this stub; for the
            # escaping arms it is written and never read (the escape is named
            # before the join), which also pins that the guard fails closed on
            # the declaration rather than on the file being absent.
            (tmp / name / "verifiers" / "stub-instrument.py").write_text(stub_script)
            return script

        script = escape_world("f26", "../f26-outside-instrument.py")
        proc = run(script, tmp / "f26")
        rec("F26 `../` declaration escape: exit 2", proc.returncode == 2, proc.returncode)
        rec("F26 `../` declaration escape: names the class, the row and the row channel",
            "FAIL registry escape: stub row declared path ../f26-outside-instrument.py "
            "traverses outside" in proc.stdout, proc.stdout)
        rec("F26 `../` declaration escape: names the registry channel too",
            "FAIL registry escape: stub registry declared path" in proc.stdout, proc.stdout)
        rec("F26 `../` declaration escape: no instrument reran", "PASS " not in proc.stdout,
            proc.stdout)

        script = escape_world("f27", str(tmp / "f27-outside-instrument.py"))
        proc = run(script, tmp / "f27")
        rec("F27 absolute declaration escape: exit 2", proc.returncode == 2, proc.returncode)
        rec("F27 absolute declaration escape: names the class, the row and the row channel",
            "FAIL registry escape: stub row declared path" in proc.stdout
            and "is absolute" in proc.stdout, proc.stdout)
        rec("F27 absolute declaration escape: names the registry channel too",
            "FAIL registry escape: stub registry declared path" in proc.stdout, proc.stdout)
        rec("F27 absolute declaration escape: no instrument reran", "PASS " not in proc.stdout,
            proc.stdout)

        # F28 -- the control: an in-repo `..` (the probe-world idiom every seat's
        # mirror world uses) stays allowed, in BOTH channels. A resolved-path
        # confinement test would red every mirror world; the predicate is
        # lexical on purpose.
        script = escape_world("f28", "verifiers/../verifiers/stub-instrument.py")
        proc = run(script, tmp / "f28")
        rec("F28 in-repo `..` declaration: still allowed", proc.returncode == 0,
            proc.returncode)
        rec("F28 in-repo `..` declaration: the row reran",
            "PASS stub observed=3 floor=3" in proc.stdout, proc.stdout)

        # F29 -- the predicate itself, pinned independently of the subprocess
        # path, and over the shapes F26-F28 reach through the tables.
        conf_cases = [
            ("verifiers/x.py", None),
            ("./verifiers/x.py", None),
            ("verifiers/../verifiers/x.py", None),
            ("verifiers/sub/x.py", None),
            ("../outside.py", "traverses outside"),
            ("verifiers/../../outside.py", "traverses outside"),
            ("..", "traverses outside"),
            ("/abs/outside.py", "is absolute"),
            (None, None),
            ("", None),
        ]
        for declared, expected in conf_cases:
            got = confinement_problem("stub", declared, DEFAULT_REPO, "row")
            want_ok = (got is None) if expected is None else (
                got is not None and expected in got and got.startswith("escape: stub row"))
            rec("F29 confinement_problem(%r) -> %r" % (declared, expected), want_ok, got)

    print("%d failure(s) over %d assertions" % (len(failures), total))
    for f in failures:
        print("FAIL: %s" % f)
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
