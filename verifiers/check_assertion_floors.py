#!/usr/bin/env python3
'''check_assertion_floors.py -- anti-shrink guard for the instruments' self-tests.

The claim under test: a self-test that silently loses assertions must never
still read green. Each instrument's --self-test prints an assertion count;
this guard reruns every self-test and FAILs when the observed count is below
the recorded floor (harness 10, corpus_integrity 119, corpus_independent 59,
surfaces 87, checklist 1597, pins 62, harness_independent 86,
compare_harness_independent 83; others @ round 36, the checklist floor
re-recorded at round 37 by the C3 fence battery plus the indented-code decoy
battery and at round 38 by the three container-relative fence shapes (V6's
named residual); the two round-38 C1 instruments registered by claim C1f/seat
P3 (floors re-bumped in-step to the settled counts of the C1 closure seat P1
landed in the same round: 71->86, 59->83). Exit: 0 all floors hold;
1 an instrument ran below its floor, or its summary could not be parsed or the
instrument could not be run (named, observed-vs-floor); 2 the in-file registry
or the external anchor disagrees (named), or a self-test timed out. Read-only.

REGISTRY ANCHORS. Rounds 31 (scout G2/G3) added the two-way in-file registry
self-check; round 37 (claim C2a, scouts C2/M7) closed its residual: those two
tables agree with each other by construction, so a coordinated edit -- the
same row deleted from BOTH, a floor lowered in BOTH, a row path repointed --
was self-consistent and silent (M7: two-table deletion -> 5 PASS, exit 0, the
instrument never reran). The anchor is now verifiers/floors-registry.json, a
file OUTSIDE this one: every registry entry must be covered by both tables
with the same path and floor, the registry's own size must match its declared
`instrument_total`, and each declared path must resolve to a non-empty file
under --repo. Any disagreement fails loudly before a self-test runs. Run
`--self-test` for the fixture battery (mutant copies in tempdirs), including
the two true discriminators for the coordinated shapes. Round 38 (claim C2,
seat P4) closes V4's two residuals: a non-str key in either table is now named
('non-string key: ...', previously an uncaught TypeError traceback at exit 1,
class unnamed), and a malformed row is named exactly once -- the anchor no
longer derives a path/floor from a row whose shape it could not parse (V4-J's
self-contradictory 'floor drift: pins registry=62 expected=62 row=None').

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
'''
import argparse
import json
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
    "corpus_integrity": 119,
    "corpus_independent": 59,
    "surfaces": 87,
    "checklist": 1597,
    "pins": 62,
    "harness_independent": 86,
    "compare_harness_independent": 83,
}
SELF_TEST_TIMEOUT_S = 120

# Round-37 external anchor (claim C2a): the registry the two in-file tables are
# cross-checked against. Relative to --repo; see registry_anchor_drift().
REGISTRY_REL = Path("verifiers/floors-registry.json")

INSTRUMENTS = {
    "harness": ("verifiers/verify_harness_claims.py", 10,
                r"self-test:\s*(\d+) failure\(s\) over (\d+) assertions", 2, 1),
    "corpus_integrity": ("verifiers/verify_corpus_integrity.py", 119,
                         r"self-test:\s*(\d+) failure\(s\) over (\d+) assertions", 2, 1),
    "corpus_independent": ("verifiers/verify_corpus_independent.py", 59,
                           r"self-test:\s*(\d+) assertions,\s*(\d+) failures", 1, 2),
    "surfaces": ("verifiers/verify_surfaces.py", 87,
                 r"(?m)^(\d+) failure\(s\) over (\d+) assertions$", 2, 1),
    "checklist": ("verifiers/verify_skill_checklist.py", 1597,
                  r"(?m)^(\d+) failure\(s\) over (\d+) assertions$", 2, 1),
    "pins": ("verifiers/check_substrate_pins.py", 62,
             r"(?m)^(\d+) failure\(s\) over (\d+) assertions$", 2, 1),
    "harness_independent": ("verifiers/verify_harness_independent.py", 86,
                            r"(?m)^(\d+) failure\(s\) over (\d+) assertions$", 2, 1),
    "compare_harness_independent": ("verifiers/compare_harness_independent.py", 83,
                                    r"self-test:\s*(\d+) failure\(s\) over (\d+) assertions", 2, 1),
}


def _row_parts(spec):
    '''The (path, floor) a row carries, or (None, None) when its shape is not a
    well-formed 5-field tuple.

    Round-38 claim C2a (V4-J): the anchor must not derive a path or a floor from
    a row whose shape it could not parse. A malformed row is named once by the
    caller; silently reading `row[0]`/`row[1]` off a 4-field tuple produced the
    self-contradictory extras 'path drift ... row=None' and 'floor drift ...
    registry=62 expected=62 row=None'.
    '''
    if isinstance(spec, tuple) and len(spec) == 5:
        return spec[0], spec[1]
    return None, None


def registry_drift():
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
        if not (isinstance(spec, tuple) and len(spec) == 5):
            drift.append("malformed row: %s (expected 5-field tuple)" % n)
        elif not (isinstance(spec[1], int) and isinstance(expected_floor, int)):
            drift.append("malformed row: %s (non-integer floor)" % n)
        elif spec[1] != expected_floor:
            drift.append("floor drift: %s floor=%r expected=%d" % (n, spec[1], expected_floor))
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
    # _row_parts() below.
    if not isinstance(total, int) or isinstance(total, bool):
        drift.append("malformed: %s instrument_total is not an integer" % REGISTRY_REL)
    elif total != len(entries):
        drift.append("size drift: instrument_total=%d but %d entries in %s" % (
            total, len(entries), REGISTRY_REL))
    names = sorted(entries)
    for n in names:
        entry = entries[n]
        if not (isinstance(entry, dict) and isinstance(entry.get("path"), str)
                and isinstance(entry.get("floor"), int) and not isinstance(entry.get("floor"), bool)):
            drift.append("malformed: %s entry %s (expected {path: str, floor: int})" % (
                REGISTRY_REL, n))
            continue
        if n not in INSTRUMENTS and n not in EXPECTED_INSTRUMENTS:
            drift.append("row vanish: %s (listed in %s, absent from both guard tables)" % (
                n, REGISTRY_REL))
        if n in EXPECTED_INSTRUMENTS and n in INSTRUMENTS:
            row_path, row_floor = _row_parts(INSTRUMENTS[n])
            if row_path is not None and row_path != entry["path"]:
                drift.append("path drift: %s registry=%s row=%s" % (n, entry["path"], row_path))
            if row_path is not None and (row_floor != entry["floor"]
                                         or EXPECTED_INSTRUMENTS[n] != entry["floor"]):
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
    '''
    canonical = {n: (repo / spec[0]).resolve() for n, spec in INSTRUMENTS.items()
                 if isinstance(spec, tuple) and len(spec) == 5}
    drift = []
    for name in sorted(overrides):
        path = Path(overrides[name])
        for other in sorted(canonical):
            if other != name and path == canonical[other]:
                drift.append("override repoint: %s -> %s (canonical instrument for %s)"
                             % (name, path, other))
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
    drift = registry_drift()
    if any(line.startswith("non-string key:") for line in drift):
        for line in drift:
            print("FAIL registry " + line)
        return 2
    drift += registry_anchor_drift(repo)
    if drift:
        for line in drift:
            print("FAIL registry " + line)
        return 2
    paths = {name: repo / spec[0] for name, spec in INSTRUMENTS.items()}
    overrides = {}
    for override in args.script:
        if "=" not in override:
            parser.error("--script must be NAME=PATH")
        name, value = override.split("=", 1)
        if name not in paths:
            parser.error("unknown instrument: " + name)
        path = Path(value)
        path = path if path.is_absolute() else (repo / path).resolve()
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
    expected_surfaces = anchor('    "surfa', 'ces": 87,\n')
    row_surfaces = anchor('    "surfaces": ("verifiers/verify_surfa', 'ces.py", 87,\n')
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
        # the live registry's own declared total (round 38: 8, after the two C1
        # instruments were registered by seat P3); a stale literal here would
        # stop landing and the count-check would name it.
        text = swap(registry_text, '"instrument_total": 8', '"instrument_total": 7',
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
        # anchor: verify_surfaces.py prints the same summary pattern and 87
        # assertions, so the no-anchor world reads 'PASS harness_independent
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

    print("%d failure(s) over %d assertions" % (len(failures), total))
    for f in failures:
        print("FAIL: %s" % f)
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
