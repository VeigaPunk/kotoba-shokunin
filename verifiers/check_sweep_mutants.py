#!/usr/bin/env python3
r"""check_sweep_mutants.py -- the round-58 C2 counter: a frozen self-test mutant sweep.

The 16-row table below is frozen by round-58 W0 (plan draft 8db20702,
`plans/round-58.md` section C1) and embedded as a literal: the counter never reads
the table from the tree at run time.  `--self-test` re-checks the table's sha256,
checks that every `old` occurs exactly once in the base bytes of
`verifiers/check_correction_sweep.py`, and checks the exit-code mapping on two
synthetic fixtures built in memory.

Each row is applied to the target bytes once (`old` must occur exactly once), and
the target's own `--self-test` then runs in a fresh TemporaryDirectory (honouring
TMPDIR) that holds a `git init -q` repository and a copy of the target at
`verifiers/check_correction_sweep.py`; the child environment drops GIT_DIR,
GIT_WORK_TREE and GIT_INDEX_FILE, and the run is capped at 120 s.

A mutant is KILLED when it applies and that self-test exits non-zero (a timeout
counts as killed and shows as `exit=timeout`).  An equivalent SURVIVES when it
applies and the self-test exits 0.  A row whose `old` does not occur exactly once
is `not-applicable` (`exit=na`) and counts against its predicate.

Exit codes: 0 iff every mutant is killed and every equivalent survives, 1
otherwise, 2 when the target cannot be evaluated (unknown rev, git failure, a
pristine self-test that does not exit 0).
"""
from __future__ import annotations

import argparse
import contextlib
import hashlib
import io
import json
import os
import subprocess
import sys
import tempfile
from pathlib import Path

LANE = Path(__file__).resolve().parent.parent
TARGET = "verifiers/check_correction_sweep.py"
BASE_REV = "f56f6e191762c27c1aa2af11a204db9e2ca4edec"
TIMEOUT = 120
TABLE_SHA256 = "6ccb40faa2f85d5abe8682fd71b9c2cf42b727609906882c81cf92d3dbc0c30c"

# The frozen round-58 W0 table (.ufo/waves/round-58/sweep-mutants.json), embedded
# as a literal.  Its sha256 is over `json.dumps(TABLE, sort_keys=True)`.
TABLE = [
    {"id": 'M01', "kind": 'mutant',
     "desc": 'delete S076 registry row (74-75)',
     "old": '    {"id": "r57-r2-s076-note", "file": "corpus/knowledge/agent-definition-files-round56.md",\n     "stale": r"holds no agent word", "declared": r"Round-57 correction", "lead": False},\n',
     "new": ''},
    {"id": 'M02', "kind": 'mutant',
     "desc": 'delete S078 registry row (76-77)',
     "old": '    {"id": "r57-r2-s078-note", "file": "corpus/knowledge/agent-definition-files-round56.md",\n     "stale": r"body of a fenced example", "declared": r"Round-57 correction", "lead": False},\n',
     "new": ''},
    {"id": 'M03', "kind": 'mutant',
     "desc": 'delete singular-agent registry row (78-79)',
     "old": '    {"id": "r57-r2-skill-singular-agent", "file": "SKILL.md",\n     "stale": r"singular `agent/` still loads", "declared": r"migrate-v1\\.mdx:486", "lead": False},\n',
     "new": ''},
    {"id": 'M04', "kind": 'mutant',
     "desc": 'S076 declared `Round-57 correction` -> `Round-57`',
     "old": 'r"holds no agent word", "declared": r"Round-57 correction"',
     "new": 'r"holds no agent word", "declared": r"Round-57"'},
    {"id": 'M05', "kind": 'mutant',
     "desc": 'S078 declared `Round-57 correction` -> `Round-57`',
     "old": 'r"body of a fenced example", "declared": r"Round-57 correction"',
     "new": 'r"body of a fenced example", "declared": r"Round-57"'},
    {"id": 'M06', "kind": 'mutant',
     "desc": 'singular declared: drop `:486`',
     "old": 'r"migrate-v1\\.mdx:486"',
     "new": 'r"migrate-v1\\.mdx"'},
    {"id": 'M07', "kind": 'mutant',
     "desc": 'drop the round-57 SEEDED entry (89)',
     "old": '\n    "corpus/knowledge/agent-definition-files-round56.md",\n',
     "new": '\n'},
    {"id": 'M08', "kind": 'mutant',
     "desc": 'drop case `r57 quote notes red` (225-226)',
     "old": '    case("r57 quote notes red", "- x\\n", "| d | 9 | x |\\n",\n         ["r57-r2-s076-note", "r57-r2-s078-note"], seed={ent: stale_e})\n',
     "new": ''},
    {"id": 'M09', "kind": 'mutant',
     "desc": 'drop case `r57 quote notes green` (227-228)',
     "old": '    case("r57 quote notes green", "- x\\n", "| d | 9 | x |\\n", [],\n         seed={ent: stale_e.rstrip("\\n") + " Round-57 correction (R2): see the lesson.\\n"})\n',
     "new": ''},
    {"id": 'M10', "kind": 'mutant',
     "desc": 'drop case `r57 singular agent clause red` (229-231)',
     "old": '    case("r57 singular agent clause red", "- x\\n", "| d | 9 | x |\\n",\n         ["r57-r2-skill-singular-agent"],\n         skill="| opencode | `.opencode/agents` (singular `agent/` still loads per a docs commit) |\\n")\n',
     "new": ''},
    {"id": 'M11', "kind": 'mutant',
     "desc": 'drop case `r57 singular agent clause green` (232-233)',
     "old": '    case("r57 singular agent clause green", "- x\\n", "| d | 9 | x |\\n", [],\n         skill="| opencode | singular `agent/` still loads (`migrate-v1.mdx:486`) |\\n")\n',
     "new": ''},
    {"id": 'E1', "kind": 'equivalent',
     "desc": 'swap registry rows S076 and S078 (74-77)',
     "old": '    {"id": "r57-r2-s076-note", "file": "corpus/knowledge/agent-definition-files-round56.md",\n     "stale": r"holds no agent word", "declared": r"Round-57 correction", "lead": False},\n    {"id": "r57-r2-s078-note", "file": "corpus/knowledge/agent-definition-files-round56.md",\n     "stale": r"body of a fenced example", "declared": r"Round-57 correction", "lead": False},\n',
     "new": '    {"id": "r57-r2-s078-note", "file": "corpus/knowledge/agent-definition-files-round56.md",\n     "stale": r"body of a fenced example", "declared": r"Round-57 correction", "lead": False},\n    {"id": "r57-r2-s076-note", "file": "corpus/knowledge/agent-definition-files-round56.md",\n     "stale": r"holds no agent word", "declared": r"Round-57 correction", "lead": False},\n'},
    {"id": 'E2', "kind": 'equivalent',
     "desc": 'singular declared `\\.` -> `[.]`',
     "old": 'r"migrate-v1\\.mdx:486"',
     "new": 'r"migrate-v1[.]mdx:486"'},
    {"id": 'E3', "kind": 'equivalent',
     "desc": 'S076 declared space -> `[ ]`',
     "old": 'r"holds no agent word", "declared": r"Round-57 correction"',
     "new": 'r"holds no agent word", "declared": r"Round-57[ ]correction"'},
    {"id": 'E4', "kind": 'equivalent',
     "desc": 'swap cases quote-notes red and green (225-228)',
     "old": '    case("r57 quote notes red", "- x\\n", "| d | 9 | x |\\n",\n         ["r57-r2-s076-note", "r57-r2-s078-note"], seed={ent: stale_e})\n    case("r57 quote notes green", "- x\\n", "| d | 9 | x |\\n", [],\n         seed={ent: stale_e.rstrip("\\n") + " Round-57 correction (R2): see the lesson.\\n"})\n',
     "new": '    case("r57 quote notes green", "- x\\n", "| d | 9 | x |\\n", [],\n         seed={ent: stale_e.rstrip("\\n") + " Round-57 correction (R2): see the lesson.\\n"})\n    case("r57 quote notes red", "- x\\n", "| d | 9 | x |\\n",\n         ["r57-r2-s076-note", "r57-r2-s078-note"], seed={ent: stale_e})\n'},
    {"id": 'E5', "kind": 'equivalent',
     "desc": 'insert a comment line before the round-57 self-test block (222)',
     "old": '    # round 57 (Q29, R2): each round-57 row red without its correction, green with it.\n',
     "new": '    # equivalent rewrite: a comment changes no behaviour\n    # round 57 (Q29, R2): each round-57 row red without its correction, green with it.\n'},
]

# The tail of the synthetic full-kill fixture: checks the row semantics the
# frozen mutants attack and stands still under the rewrites the equivalents make.
FIXTURE_TAIL = r'''EXPECTED_IDS = (
    "r57-r2-s076-note",
    "r57-r2-s078-note",
    "r57-r2-skill-singular-agent",
)

# Each declared pattern must match the text that records the correction and must
# not match a weaker text that merely names the round: every mutant that weakens
# a declared literal starts matching the weaker text.
PROBES = {
    "r57-r2-s076-note": (
        "S076's project line records the Round-57 correction (R2).",
        "S076's project line carries a Round-57 note, no result.",
    ),
    "r57-r2-s078-note": (
        "S078's quote records the Round-57 correction (R2).",
        "S078's quote carries a Round-57 note, no result.",
    ),
    "r57-r2-skill-singular-agent": (
        "| opencode | singular `agent/` still loads (`migrate-v1.mdx:486`) |",
        "| d | see `migrate-v1.mdx` for the rule |",
    ),
}

EXPECTED_CASES = {
    "r57 quote notes red": ("r57-r2-s076-note", "r57-r2-s078-note"),
    "r57 quote notes green": (),
    "r57 singular agent clause red": ("r57-r2-skill-singular-agent",),
    "r57 singular agent clause green": (),
}

SEED = "corpus/knowledge/agent-definition-files-round56.md"


def wanted():
    out = {}
    for part in CASES.split("    case(")[1:]:
        name = re.match(r'"([^"]+)"', part).group(1)
        found = re.search(r"\n\s*\[([^\]]*)\]", part)
        out[name] = tuple(re.findall(r'"([^"]+)"', found.group(1))) if found else ()
    return out


def self_test():
    fails = []
    ids = sorted(r["id"] for r in REGISTRY)
    if ids != sorted(EXPECTED_IDS):
        fails.append("registry ids %r" % (ids,))
    by = {r["id"]: r for r in REGISTRY}
    for rid, (yes, no) in PROBES.items():
        row = by.get(rid)
        if row is None:
            fails.append("%s: registry row missing" % rid)
            continue
        if not re.search(row["declared"], yes):
            fails.append("%s: declared does not match its correction text" % rid)
        if re.search(row["declared"], no):
            fails.append("%s: declared matches a bare-round text" % rid)
    if SEED not in SEEDED:
        fails.append("SEEDED lost the round-57 file")
    if wanted() != EXPECTED_CASES:
        fails.append("cases %r" % (wanted(),))
    print("%d failure(s) over 9 checks" % len(fails))
    for f in fails:
        print("FAIL", f)
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(self_test() if "--self-test" in sys.argv else 0)
'''

# A fixture whose self-test always fails: the pristine run must not exit 0.
FIXTURE_ALWAYS_FAIL = '''#!/usr/bin/env python3
"""Synthetic C2 fixture: its self-test always fails."""
import sys

print("FAIL synthetic always-fails fixture")
sys.exit(1)
'''


class CouldNotEvaluate(RuntimeError):
    """The target cannot be evaluated; the counter reports this and exits 2."""


def first_line(raw: bytes) -> str:
    text = raw.decode("utf-8", "replace").strip()
    return text.splitlines()[0] if text else "(no diagnostic)"


def child_env() -> dict:
    """The environment for git and self-test children: no inherited git pointers."""
    return {k: v for k, v in os.environ.items()
            if k not in ("GIT_DIR", "GIT_WORK_TREE", "GIT_INDEX_FILE")}


def git_show(rev: str) -> bytes:
    """Bytes of TARGET at `rev`, read from the lane's git store."""
    try:
        r = subprocess.run(["git", "-C", str(LANE), "show", "%s:%s" % (rev, TARGET)],
                           capture_output=True, env=child_env())
    except OSError as e:
        raise CouldNotEvaluate("cannot run git: %s" % e)
    if r.returncode != 0:
        raise CouldNotEvaluate("git show %s:%s failed in %s (exit %d): %s" % (
            rev, TARGET, LANE, r.returncode, first_line(r.stderr)))
    return r.stdout


def read_file(path: str) -> bytes:
    """Bytes of a control file."""
    try:
        return Path(path).read_bytes()
    except OSError as e:
        raise CouldNotEvaluate("cannot read %s: %s" % (path, e))


def run_self_test(source: bytes) -> str:
    """Run the target's --self-test on `source`; the exit code as text ('timeout' at the cap)."""
    env = child_env()
    try:
        with tempfile.TemporaryDirectory() as t:
            root = Path(t)
            (root / "verifiers").mkdir()
            (root / "verifiers" / "check_correction_sweep.py").write_bytes(source)
            init = subprocess.run(["git", "init", "-q"], cwd=t, env=env,
                                  capture_output=True)
            if init.returncode != 0:
                raise CouldNotEvaluate("git init failed in %s (exit %d): %s" % (
                    t, init.returncode, first_line(init.stderr)))
            try:
                proc = subprocess.run([sys.executable, "-B", TARGET, "--self-test"],
                                      cwd=t, env=env, capture_output=True,
                                      timeout=TIMEOUT)
            except subprocess.TimeoutExpired:
                return "timeout"
    except OSError as e:
        raise CouldNotEvaluate("cannot run the self-test in a scratch copy: %s" % e)
    return str(proc.returncode)


def evaluate(source: bytes) -> list:
    """The (row, verdict, exit) triples for `source`; raises CouldNotEvaluate."""
    pristine = run_self_test(source)
    if pristine != "0":
        raise CouldNotEvaluate("pristine self-test exit %s" % pristine)
    out = []
    for row in TABLE:
        old = row["old"].encode("utf-8")
        if source.count(old) != 1:
            out.append((row, "not-applicable", "na"))
            continue
        code = run_self_test(source.replace(old, row["new"].encode("utf-8"), 1))
        if row["kind"] == "mutant":
            out.append((row, "killed" if code != "0" else "survived", code))
        else:
            out.append((row, "survived" if code == "0" else "killed", code))
    return out


def counts(results: list) -> tuple:
    """(killed mutants, mutant rows, survived equivalents, equivalent rows)."""
    killed = sum(1 for r, v, _ in results if r["kind"] == "mutant" and v == "killed")
    mutants = sum(1 for r in TABLE if r["kind"] == "mutant")
    survived = sum(1 for r, v, _ in results if r["kind"] == "equivalent" and v == "survived")
    equivalents = sum(1 for r in TABLE if r["kind"] == "equivalent")
    return killed, mutants, survived, equivalents


def synthetic_full_kill() -> str:
    """A fixture whose self-test kills every frozen mutant and keeps every equivalent green.

    It carries all 16 `old` texts byte-exactly, so every row applies, inside a
    model whose checks are semantic: row ids as a multiset (the row swap
    survives), declared patterns probed by behaviour (the `[.]` and `[ ]`
    rewrites survive) and case blocks parsed by name and wanted ids (the case
    block swap survives).  Its comments carry no meaning (the inserted comment
    survives).
    """
    row = {r["id"]: r for r in TABLE}
    return (
        '#!/usr/bin/env python3\n'
        '"""Synthetic C2 fixture: the round-57 model with a semantic self-test."""\n'
        'import re\n'
        'import sys\n\n'
        'REGISTRY = (\n'
        + row["M01"]["old"] + row["M02"]["old"] + row["M03"]["old"]
        + ')\n\nSEEDED = ('
        + row["M07"]["old"]
        + ')\n\n'
        + row["E5"]["old"]
        + 'CASES = r"""\n'
        + row["M08"]["old"] + row["M09"]["old"]
        + row["M10"]["old"] + row["M11"]["old"]
        + '"""\n\n'
        + FIXTURE_TAIL
    )


def self_test() -> int:
    """The counter's own self-test; 0 when every assertion holds."""
    fails, n = [], 0

    sha = hashlib.sha256(json.dumps(TABLE, sort_keys=True).encode("utf-8")).hexdigest()
    print("table sha256 %s" % sha)
    n += 1
    if sha != TABLE_SHA256:
        fails.append("table sha256 %s is not the frozen %s" % (sha, TABLE_SHA256))

    n += 1
    ids = [r["id"] for r in TABLE]
    kinds = [r["kind"] for r in TABLE]
    if (len(TABLE) != 16 or len(set(ids)) != 16 or kinds.count("mutant") != 11
            or kinds.count("equivalent") != 5):
        fails.append("table shape: %d rows, %d ids, %d mutants, %d equivalents" % (
            len(TABLE), len(set(ids)), kinds.count("mutant"),
            kinds.count("equivalent")))

    try:
        base = git_show(BASE_REV)
    except CouldNotEvaluate as e:
        base = None
        n += 1
        fails.append("base bytes %s:%s: %s" % (BASE_REV, TARGET, e))
    if base is not None:
        for row in TABLE:
            n += 1
            seen = base.count(row["old"].encode("utf-8"))
            if seen != 1:
                fails.append("%s: old occurs %d times in %s:%s" % (
                    row["id"], seen, BASE_REV, TARGET))

    want = "sweep mutants killed 11 of 11; equivalents survived 5 of 5"
    with tempfile.TemporaryDirectory() as t:
        path = Path(t) / "full_kill.py"
        path.write_text(synthetic_full_kill(), encoding="utf-8")
        out, err = io.StringIO(), io.StringIO()
        with contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
            code = main(["--file", str(path)])
    lines = out.getvalue().strip().splitlines()
    n += 1
    if code != 0 or not lines or lines[-1] != want:
        fails.append("synthetic full-kill: exit %d, last line %r, stderr %r" % (
            code, lines[-1] if lines else "", err.getvalue().strip()))

    with tempfile.TemporaryDirectory() as t:
        path = Path(t) / "always_fail.py"
        path.write_text(FIXTURE_ALWAYS_FAIL, encoding="utf-8")
        out, err = io.StringIO(), io.StringIO()
        with contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
            code = main(["--file", str(path)])
    n += 1
    if code != 2 or err.getvalue().strip() != "could-not-evaluate: pristine self-test exit 1":
        fails.append("synthetic always-fail: exit %d, stderr %r" % (
            code, err.getvalue().strip()))

    print("%d failure(s) over %d assertions" % (len(fails), n))
    for f in fails:
        print("FAIL", f)
    return 1 if fails else 0


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--rev", help="revision whose %s is swept" % TARGET)
    g.add_argument("--file", help="file to sweep instead of a revision (controls)")
    g.add_argument("--self-test", action="store_true")
    a = ap.parse_args(argv)
    if a.self_test:
        return self_test()
    try:
        source = git_show(a.rev) if a.rev else read_file(a.file)
        results = evaluate(source)
    except CouldNotEvaluate as e:
        print("could-not-evaluate: %s" % e, file=sys.stderr)
        return 2
    for row, verdict, code in results:
        print("%s %s %s exit=%s" % (row["id"], row["kind"], verdict, code))
    killed, mutants, survived, equivalents = counts(results)
    print("sweep mutants killed %d of %d; equivalents survived %d of %d" % (
        killed, mutants, survived, equivalents))
    return 0 if killed == mutants and survived == equivalents else 1


if __name__ == "__main__":
    sys.exit(main())
