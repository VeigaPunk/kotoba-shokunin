#!/usr/bin/env python3
r"""check_substrate_repin_v2.py -- frozen counter for the round-72 C2 (freshness) claim.

Frozen predicate (plans/round-72.md § C2, the sentence the plan, this docstring
and the receipt carry unchanged):

    python3 -B verifiers/check_substrate_repin_v2.py --rev <rev>  ->  prints
    "host substrate re-derived: pins OK k/3; surfaces pass p of 7; removal
    ledger l of l verified", exit 0 when k == 3 and p == 7 and the ledger
    conjunct holds

The claim: the host substrate is re-derived and re-pinned.  The omp half is a
path move onto `~/.local/bin/omp.real` (identical bytes to the r51 pin); the
opencode half is a new binary lineage (v2.1.4 at `~/.opencode/bin/opencode`)
whose loader the census rules OC-1..OC-6 must be re-derived on.

For the revision given by `--rev` the counter extracts that revision's tree
(`git archive <rev> -- verifiers corpus`) into a temporary directory and, from
that tree:

  P  runs `verifiers/check_substrate_pins.py --json` with NO path flag, so the
     tree's own default binary paths and its own `verifiers/baseline.json`
     decide: k = the rows whose verdict is PASS;
  S  runs `verifiers/verify_surfaces.py --json` with NO path flag, so the
     tree's own default binaries and its own `verifiers/surfaces-baseline.json`
     decide: p = the checks whose status is PASS;
  K  recomputes the removal-ledger conjunct itself.  Base classes are the
     `harness == "opencode"` rows of `verifiers/surfaces-baseline.json` at
     BASE_REV.  Every base class must be either kept (same `class_id`,
     `literal`, `context_kind` and `verdict` at <rev>) or listed in the <rev>
     tree's `verifiers/census-removals.json`; and the ledger must equal exactly
     the frozen set FROZEN_REMOVALS (errata E1, `plans/round-72-addendum-1.md`:
     the three classes the wave-1 census found without a loader on v2.1.4),
     each of whose frozen anchors the counter itself finds absent from the live
     opencode dump (its own `strings -n 4` pass).  A class outside the set
     cannot be ledgered, a frozen class whose anchor is live is not verified,
     and a class that stays declared `governed` while its loader is gone is
     caught by `surfaces.opencode_extract` (p must be 7 as well).

Ledger schema the counter accepts (`verifiers/census-removals.json` at <rev>):

    {"removed": [{"class_id": "opencode:instructions/CONTEXT.md",
                   "literal": "CONTEXT.md",
                   "reason": "<why the literal left the live dump>"}]}

`class_id` is the only field the counter reads (extra fields are the author's).
A missing file is an empty ledger -- which fails the frozen-set conjunct.
A file that cannot be read or parsed, or a row without a string `class_id`, is
"cannot evaluate" (exit 2), never a pass.

Output: the frozen line, then the measured substrate, because the counter reads
the installed binaries and its result names the bytes it measured:
  `host substrate re-derived: pins OK <k>/3; surfaces pass <p> of 7; removal
   ledger <verified> of <required> verified`
  `substrate opencode: <path> sha256 <sha256> bytes <n> strings <m>`
`<verified>` is |ledger ∩ required| and `<total>` is |ledger ∪ required|, so an
exactly-right ledger reads `l of l` and both a ledgered-but-present literal and
an unledgered-but-absent class show in the line itself (`1 of 2`, `0 of 1`)
rather than only in the exit code.  The stderr detail names the classes.

Guards the counter makes itself (a revision may not buy a green by moving the
contract rather than the substrate):
  * the pin script must report exactly PINS_TOTAL rows -- a 4th pin row with 3
    PASS would otherwise print `pins OK 3/3` and pass;
  * the surfaces script must report exactly CHECKS_TOTAL checks -- an 8th
    check failing would otherwise print `surfaces pass 7 of 7` and pass;
  * a pin holds only against the substrate the counter measured: `k` counts a
    PASS row only if the row's expectation is the live opencode's sha256.  A
    tree that pins a stub's own sha makes `check_substrate_pins.py` read PASS
    (it compares the pin with whatever sits at the tree's path), so a
    PASS-count alone would report `pins OK 3/3` for a 358-byte stub; the
    counter dumped the live bytes and reports `pins OK 2/3` plus the stray pin
    on stderr;
  * an instrument that reports ZERO rows has measured nothing: the counter
    returns 2 (cannot evaluate) and names the instrument, its `exit_code` and
    its `error`, instead of counting `0 of 7` or `0/3`.  At the base,
    `verify_surfaces.py` exits 2 with `checks: []` because its default
    opencode path is gone, so the base is unevaluable by this counter, not a
    measured `0 of 7`;
  * BASE_REV, PINS_TOTAL, CHECKS_TOTAL and the output line are pinned here and
    never read from the measured revision.

Exit ladder: 0 every conjunct holds; 1 a measured conjunct fails (a row was
reported and it is not PASS); 2 the counter cannot evaluate (extraction,
missing instrument, an empty instrument report, unreadable ledger, no readable
live opencode dump).

The counter's own `strings -n 4` pass reads the LIVE host opencode,
`~/.opencode/bin/opencode` -- not the path the measured tree pins.  The frozen
sentence says the ledger equals the base classes absent from "the live opencode
dump", and a tree that pins a stub at its own path must not be able to choose
the bytes its removal ledger is judged against: with the tree's path, a
358-byte stub plus an all-classes ledger satisfies both the pin conjunct (its
own sha is pinned) and the ledger conjunct (every literal is absent from the
stub), leaving only `p == 7` to catch it.  Against the live dump that world
reads `removal ledger 1 of 9 verified` however the surface target moves.  The
substrate line names the path, sha256 and size of the bytes actually dumped.

Usage:
  python3 -B verifiers/check_substrate_repin_v2.py --rev <rev> [--repo <repo>]
  python3 -B verifiers/check_substrate_repin_v2.py --self-test

`--opencode-binary` is the fixture hook: it replaces only the counter's own
live-dump pass, never a flag handed to the instruments.  The self-test always
passes it, so the self-test reads no host binary (Q48).
"""
from __future__ import annotations

import argparse
import contextlib
import re
import hashlib
import io
import json
import subprocess
import sys
import tarfile
import tempfile
from datetime import datetime, timezone
from pathlib import Path

BASE_REV = "c69711ee08279609374d895bb0f3c8c18ccf15c9"
PINS_TOTAL = 3
CHECKS_TOTAL = 7
LEDGER_PATH = "verifiers/census-removals.json"
BASELINE_PATH = "verifiers/surfaces-baseline.json"
HOST_OPENCODE = Path("/home/vgpnk/.opencode/bin/opencode")
STRINGS_TIMEOUT = 600
OPENCODE_PIN = "opencode_binary_sha256"


# Errata E1 (plans/round-72-addendum-1.md, frozen before data): the removal set is
# the three base classes the wave-1 census (ScoutOpencodeV2, ExecOC1, ExecOC2)
# found without a loader in the v2.1.4 dump, each with the anchors that must match
# NOTHING in the live dump.  The ledger must name exactly these classes; a ledgered
# class whose anchor is live, an unlisted class, or a missing one fails.
FROZEN_REMOVALS = {
    "opencode:instructions/CONTEXT.md": [r"CONTEXT\.md"],
    "opencode:instructions/CLAUDE.md": [
        r"disableClaudeCodePrompt",
        r'\["AGENTS\.md".{0,400}?"CONTEXT\.md"[^\]]{0,200}\]'],
    "opencode:claude-home/CLAUDE.md": [
        r'\.join\(\s*[A-Za-z_$][A-Za-z0-9_$]*\.home\s*,\s*"\.([A-Za-z0-9_-]+)"\s*,'
        r'\s*"([A-Za-z0-9_.-]+\.md)"'],
}


class EnvError(Exception):
    """The counter cannot answer (exit 2)."""


def default_repo() -> Path:
    """Nearest ancestor holding the lane's surfaces baseline (works from
    `verifiers/` and from any `.ufo/waves/...` build directory)."""
    here = Path(__file__).resolve().parent
    for cand in (here, *here.parents):
        if (cand / BASELINE_PATH).is_file():
            return cand
    return here.parent


def git(repo: Path, *args: str) -> bytes:
    return subprocess.run(["git", "-C", str(repo), *args], check=True,
                          capture_output=True).stdout


def extract(repo: Path, rev: str, dest: Path) -> None:
    data = git(repo, "archive", "--format=tar", rev, "--", "verifiers", "corpus")
    with tarfile.open(fileobj=io.BytesIO(data)) as tf:
        tf.extractall(dest, filter="data")


def opencode_classes(raw: bytes) -> dict[str, tuple[str, str, str]]:
    """class_id -> (literal, context_kind, verdict) for harness == opencode."""
    data = json.loads(raw)
    if not isinstance(data, dict):
        raise ValueError("surfaces baseline is not a JSON object")
    rows = data.get("classes")
    if not isinstance(rows, list):
        raise ValueError("surfaces baseline has no 'classes' list")
    out: dict[str, tuple[str, str, str]] = {}
    for row in rows:
        if not isinstance(row, dict) or row.get("harness") != "opencode":
            continue
        cid, lit = row.get("class_id"), row.get("literal")
        if not isinstance(cid, str) or not isinstance(lit, str):
            raise ValueError("opencode class row lacks a string class_id/literal: %r"
                             % (row,))
        out[cid] = (lit, row.get("context_kind"), row.get("verdict"))
    return out


def read_ledger(tree: Path) -> set[str]:
    """The declared removal ledger at `tree`; a missing file is an empty ledger."""
    path = tree / LEDGER_PATH
    if not path.is_file():
        return set()
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, ValueError) as exc:
        raise EnvError("%s unreadable/unparseable: %s" % (LEDGER_PATH, exc))
    if not isinstance(data, dict):
        raise EnvError("%s is not a JSON object" % LEDGER_PATH)
    rows = data.get("removed")
    if not isinstance(rows, list):
        raise EnvError("%s has no 'removed' list" % LEDGER_PATH)
    out: set[str] = set()
    for i, row in enumerate(rows):
        cid = row.get("class_id") if isinstance(row, dict) else None
        if not isinstance(cid, str) or not cid:
            raise EnvError("%s removed[%d] has no string class_id" % (LEDGER_PATH, i))
        out.add(cid)
    return out


def strings_dump(path: Path) -> str:
    try:
        proc = subprocess.run(["strings", "-n", "4", str(path)],
                              capture_output=True, timeout=STRINGS_TIMEOUT)
    except FileNotFoundError:
        raise EnvError("`strings` tool unavailable on this host")
    except OSError as exc:
        raise EnvError("cannot run strings on %s: %s" % (path, exc))
    except subprocess.TimeoutExpired:
        raise EnvError("strings -n 4 %s exceeded %d s" % (path, STRINGS_TIMEOUT))
    if proc.returncode != 0:
        raise EnvError("strings -n 4 %s exited %d" % (path, proc.returncode))
    return proc.stdout.decode("utf-8", "replace")


def ledger_verdict(base: dict[str, tuple[str, str, str]],
                   rev_cls: dict[str, tuple[str, str, str]],
                   ledgered: set[str], dump: str) -> dict:
    required = set(FROZEN_REMOVALS)
    live = {cid for cid, anchors in FROZEN_REMOVALS.items()
            if any(re.search(a, dump) for a in anchors)}
    kept = {cid for cid, sig in base.items() if rev_cls.get(cid) == sig}
    return {
        "required": required,
        "kept": kept,
        "verified": len((ledgered & required) - live),
        "total": len(ledgered | required),
        "extra": sorted((ledgered - required) | (ledgered & live)),
        "missing": sorted(required - ledgered),
        "unkept": sorted(cid for cid in base
                         if cid not in kept and cid not in ledgered),
    }


def run_instrument(script: Path, cwd: Path) -> dict:
    proc = subprocess.run([sys.executable, "-B", str(script), "--json"],
                          capture_output=True, text=True, cwd=str(cwd))
    try:
        payload = json.loads(proc.stdout)
    except ValueError:
        raise EnvError("%s --json printed no JSON (exit %d): %s"
                       % (script.name, proc.returncode,
                          (proc.stdout or proc.stderr).strip()[:200]))
    if not isinstance(payload, dict):
        raise EnvError("%s --json printed a non-object payload" % script.name)
    return payload


# ---------------------------------------------------------------------------
# self-test: isolated local git worlds, no host binary is read
# ---------------------------------------------------------------------------

FIXTURE_SURFACES = r'''import json, subprocess, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
TREE = HERE.parent
IDS = ("surfaces.literal_present", "surfaces.no_uncovered_class",
       "surfaces.opencode_extract", "surfaces.table_parity",
       "surfaces.literal_parity", "surfaces.kind_parity",
       "surfaces.excluded_reason")


def main():
    inv = TREE / "corpus" / "fixture-inventory.md"
    inv_text = inv.read_text() if inv.is_file() else ""
    if "empty-report" in inv_text:
        print(json.dumps({"checks": [], "pass": 0, "fail": 0, "exit_code": 2,
                          "error": "fixture: no opencode dump"}))
        return 2
    base = json.loads((TREE / "verifiers" / "surfaces-baseline.json").read_text())
    oc = [r for r in base["classes"] if r.get("harness") == "opencode"]
    dump = subprocess.run(["strings", "-n", "4", str(HERE / "fixture-opencode")],
                          capture_output=True, text=True).stdout
    present = bool(oc) and all(r["literal"] in dump for r in oc)
    checks = []
    for cid in IDS:
        ok = present if cid == "surfaces.opencode_extract" else (
            "all-checks-pass" in inv_text)
        checks.append({"id": cid, "status": "PASS" if ok else "FAIL"})
    if "extra-check" in inv_text:
        checks.append({"id": "surfaces.fixture_extra", "status": "FAIL"})
    p = sum(1 for c in checks if c["status"] == "PASS")
    print(json.dumps({"checks": checks, "pass": p,
                      "fail": len(checks) - p, "exit_code": 0 if p == len(checks) else 1}))
    return 0 if p == len(checks) else 1


sys.exit(main())
'''

FIXTURE_PINS = r'''import calendar, hashlib, json, re, sys
from datetime import datetime
from pathlib import Path

HERE = Path(__file__).resolve().parent
TREE = HERE.parent
BIN = {"omp": HERE / "fixture-omp", "opencode": HERE / "fixture-opencode"}
KINDS = {"omp_binary_sha256": ("omp", "sha256"),
         "omp_binary_mtime": ("omp", "mtime"),
         "opencode_binary_sha256": ("opencode", "sha256")}
DISCOVER = re.compile(r"^[a-z0-9_]+_binary_[A-Za-z0-9]+$")


def ns(text):
    m = re.search(r"\.(\d+)", text)
    digits = m.group(1) if m else ""
    frac = int(digits.ljust(9, "0")) if digits else 0
    base = re.sub(r"\.\d+", "", text, count=1)
    dt = datetime.fromisoformat(base)
    return calendar.timegm(dt.utctimetuple()) * 10**9 + frac


def main():
    ma = json.loads((TREE / "verifiers" / "baseline.json").read_text())["measured_against"]
    keys = list(KINDS) + sorted(k for k in ma
                                if DISCOVER.match(k) and k not in KINDS)
    rows = []
    for pin in keys:
        sub, kind = KINDS.get(pin, ("-", "-"))
        row = {"pin": pin, "kind": kind, "substrate": sub}
        if sub not in BIN:
            row.update(verdict="UNSUPPORTED", binary=None, detail="pin-shaped key")
            rows.append(row)
            continue
        binary = BIN[sub]
        row["binary"] = str(binary)
        if not binary.is_file():
            row.update(verdict="UNREADABLE", detail="missing")
        elif kind == "sha256":
            live = hashlib.sha256(binary.read_bytes()).hexdigest()
            row.update(expect=ma.get(pin), observed=live,
                       verdict="PASS" if live == ma.get(pin) else "DRIFT")
        else:
            # `git archive` cannot carry a filesystem mtime, so the fixture
            # stands in for the immutable host mtime with a committed stamp.
            live = int((HERE / "fixture-omp.mtime").read_text().strip())
            row.update(expect=ma.get(pin), observed=str(live),
                       verdict="PASS" if live == ns(ma.get(pin)) else "DRIFT")
        rows.append(row)
    p = sum(1 for r in rows if r["verdict"] == "PASS")
    print(json.dumps({"checks": rows, "pass": p, "fail": len(rows) - p,
                      "exit_code": 0 if p == len(rows) else 1}))
    return 0 if p == len(rows) else 1


sys.exit(main())
'''


def self_test() -> int:
    """Drive main() on one satisfying and one broken world per conjunct."""
    global BASE_REV, FROZEN_REMOVALS
    FROZEN_REMOVALS = {"opencode:instructions/CONTEXT.md": [r"CONTEXT\.md"]}
    assertions = 0
    failures = 0

    def check(name: str, ok: bool, detail: object) -> None:
        nonlocal assertions, failures
        assertions += 1
        if not ok:
            failures += 1
            print(f"FAIL {name}: {detail}")

    ok_line = ("host substrate re-derived: pins OK 3/3; surfaces pass 7 of 7; "
               "removal ledger 1 of 1 verified")
    mtime_ns = 1_792_600_644_615_549_837

    def stamp(t_ns: int) -> str:
        sec, frac = divmod(t_ns, 10**9)
        return (datetime.fromtimestamp(sec, timezone.utc)
                .strftime("%Y-%m-%dT%H:%M:%S") + ".%09d+00:00" % frac)

    classes = [
        {"class_id": "opencode:instructions/AGENTS.md", "harness": "opencode",
         "literal": "AGENTS.md", "context_kind": "loader-literal", "verdict": "governed"},
        {"class_id": "opencode:instructions/CLAUDE.md", "harness": "opencode",
         "literal": "CLAUDE.md", "context_kind": "loader-literal", "verdict": "governed"},
        {"class_id": "opencode:instructions/CONTEXT.md", "harness": "opencode",
         "literal": "CONTEXT.md", "context_kind": "loader-literal", "verdict": "governed"},
        {"class_id": "opencode:config/AGENTS.md", "harness": "opencode",
         "literal": "AGENTS.md", "context_kind": "loader-config", "verdict": "governed"},
        {"class_id": "omp:fixture/AGENTS.md", "harness": "omp",
         "literal": "AGENTS.md", "context_kind": "loader-literal", "verdict": "governed"},
    ]

    try:
        with tempfile.TemporaryDirectory(prefix="substrate-repin-selftest-") as td:
            repo = Path(td) / "repo"
            verifiers = repo / "verifiers"
            corpus = repo / "corpus"
            verifiers.mkdir(parents=True)
            corpus.mkdir()

            def fixture_git(*args: str) -> str:
                return subprocess.run(["git", "-C", str(repo), *args], check=True,
                                      capture_output=True, text=True).stdout.strip()

            fixture_git("init", "-q")
            check("fixture repo is its own toplevel",
                  Path(fixture_git("rev-parse", "--show-toplevel")).resolve()
                  == repo.resolve(), fixture_git("rev-parse", "--show-toplevel"))
            fixture_git("config", "user.name", "substrate repin self-test")
            fixture_git("config", "user.email", "substrate-repinselftest@example.invalid")

            # One dump for both roles at the fixture base: the tree's pinned
            # binary (hashed and dumped by the stub instruments) and the live
            # stand-in the counter measures must be the same bytes, exactly as
            # an honest re-pin pins the host binary it runs on.
            oc_bytes = b"AGENTS.md\nCLAUDE.md\nagent config loader\n"
            omp_bytes = b"AGENTS.md\nomp registration loader\n"
            (verifiers / "fixture-opencode").write_bytes(oc_bytes)
            (verifiers / "fixture-live").write_bytes(oc_bytes)
            (verifiers / "fixture-omp").write_bytes(omp_bytes)
            (verifiers / "fixture-omp.mtime").write_text(str(mtime_ns) + "\n",
                                                         encoding="utf-8")
            (verifiers / "surfaces-baseline.json").write_text(
                json.dumps({"classes": classes}), encoding="utf-8")
            (verifiers / "baseline.json").write_text(json.dumps({
                "measured_against": {
                    "omp_binary_sha256": hashlib.sha256(omp_bytes).hexdigest(),
                    "omp_binary_mtime": stamp(mtime_ns),
                    "opencode_binary_sha256": hashlib.sha256(oc_bytes).hexdigest(),
                }}), encoding="utf-8")
            (verifiers / "verify_surfaces.py").write_text(FIXTURE_SURFACES, encoding="utf-8")
            (verifiers / "check_substrate_pins.py").write_text(FIXTURE_PINS, encoding="utf-8")
            (corpus / "fixture-inventory.md").write_text("all-checks-pass\n", encoding="utf-8")
            fixture_git("add", "-A")
            fixture_git("-c", "core.hooksPath=/dev/null", "commit", "-q", "-m", "base")
            fixture_base = fixture_git("rev-parse", "HEAD")
            previous_base = BASE_REV
            BASE_REV = fixture_base
            dump_override = str(verifiers / "fixture-live")

            def run_world(rev: str) -> tuple[int, str]:
                out, err = io.StringIO(), io.StringIO()
                with contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
                    code = main(["--rev", rev, "--repo", str(repo),
                                 "--opencode-binary", dump_override])
                text = out.getvalue() + err.getvalue()
                first = text.strip().splitlines()[0] if text.strip() else "<no output>"
                subject = fixture_git("log", "-1", "--format=%s", rev)
                print(f"world {subject!r}: exit {code} :: {first}")
                return code, text

            def commit_world(name: str, mutate) -> str:
                fixture_git("checkout", "-q", fixture_base, "--", ".")
                fixture_git("clean", "-qfd")
                mutate()
                fixture_git("add", "-A")
                fixture_git("-c", "core.hooksPath=/dev/null", "commit", "-q", "-m", name)
                return fixture_git("rev-parse", "HEAD")

            def drop_context_class() -> None:
                rows = [r for r in classes
                        if r["class_id"] != "opencode:instructions/CONTEXT.md"]
                (verifiers / "surfaces-baseline.json").write_text(
                    json.dumps({"classes": rows}), encoding="utf-8")

            def ledger(ids: list[str]) -> None:
                (verifiers / "census-removals.json").write_text(json.dumps(
                    {"removed": [{"class_id": i, "literal": "CONTEXT.md",
                                   "reason": "literal absent from the live dump"}
                                  for i in ids]}), encoding="utf-8")

            def pin_mtime(value: str) -> None:
                data = json.loads((verifiers / "baseline.json").read_text())
                data["measured_against"]["omp_binary_mtime"] = value
                (verifiers / "baseline.json").write_text(json.dumps(data),
                                                        encoding="utf-8")

            def inventory(text: str) -> None:
                (corpus / "fixture-inventory.md").write_text(text, encoding="utf-8")

            try:
                # satisfying world: the absent literal is ledgered and retired
                def satisfying() -> None:
                    drop_context_class()
                    ledger(["opencode:instructions/CONTEXT.md"])

                rev = commit_world("satisfying", satisfying)
                code, output = run_world(rev)
                check("satisfying world is exit 0", code == 0, (code, output.strip()))
                check("satisfying world prints the frozen line",
                      ok_line in output, output.strip())

                # the conjunct is scoped to opencode: retiring an omp class is free
                def satisfying_omp_dropped() -> None:
                    satisfying()
                    path = verifiers / "surfaces-baseline.json"
                    rows = [r for r in json.loads(path.read_text())["classes"]
                            if r.get("harness") != "omp"]
                    path.write_text(json.dumps({"classes": rows}), encoding="utf-8")

                rev = commit_world("satisfying, omp class dropped",
                                   satisfying_omp_dropped)
                code, output = run_world(rev)
                check("omp class is outside the ledger conjunct",
                      code == 0 and ok_line in output, (code, output.strip()))

                # pin conjunct: stale mtime pin
                rev = commit_world("stale mtime",
                                   lambda: (satisfying(),
                                            pin_mtime(stamp(mtime_ns - 10**9))))
                code, output = run_world(rev)
                check("stale mtime pin fails",
                      code == 1 and ("pins OK 2/3; surfaces pass 7 of 7; "
                                     "removal ledger 1 of 1 verified") in output,
                      (code, output.strip()))

                # surfaces conjunct: six checks red, extraction green
                rev = commit_world("surfaces red",
                                   lambda: (satisfying(), inventory("no marker\n")))
                code, output = run_world(rev)
                check("surfaces below 7 fails",
                      code == 1 and ("pins OK 3/3; surfaces pass 1 of 7; "
                                     "removal ledger 1 of 1 verified") in output,
                      (code, output.strip()))

                # ledger conjunct: a present literal ledgered
                rev = commit_world("present literal ledgered",
                                   lambda: (satisfying(),
                                            ledger(["opencode:instructions/CONTEXT.md",
                                                    "opencode:instructions/AGENTS.md"])))
                code, output = run_world(rev)
                check("ledgered present literal fails",
                      code == 1 and "removal ledger 1 of 2 verified" in output
                      and "opencode:instructions/AGENTS.md" in output,
                      (code, output.strip()))

                # ledger conjunct: an absent class missing from the ledger
                rev = commit_world("absent class unledgered",
                                   lambda: (drop_context_class(),
                                            ledger([])))
                code, output = run_world(rev)
                check("unledgered absent class fails",
                      code == 1 and "removal ledger 0 of 1 verified" in output,
                      (code, output.strip()))

                # kept-identity conjunct: a base class silently re-verdicted
                def reverdict() -> None:
                    satisfying()
                    data = json.loads(
                        (verifiers / "surfaces-baseline.json").read_text())
                    for row in data["classes"]:
                        if row["class_id"] == "opencode:instructions/AGENTS.md":
                            row["verdict"] = "excluded"
                    (verifiers / "surfaces-baseline.json").write_text(
                        json.dumps(data), encoding="utf-8")

                rev = commit_world("re-verdicted base class", reverdict)
                code, output = run_world(rev)
                check("re-verdicted base class fails",
                      code == 1 and "removal ledger 1 of 1 verified" in output,
                      (code, output.strip()))

                # row-count guard: a 4th pin row with 3 PASS must not read 3/3
                rev = commit_world("extra pin row", lambda: (
                    satisfying(),
                    pin_mtime(stamp(mtime_ns)),
                    (verifiers / "baseline.json").write_text(json.dumps({
                        "measured_against": {
                            "omp_binary_sha256": hashlib.sha256(omp_bytes).hexdigest(),
                            "omp_binary_mtime": stamp(mtime_ns),
                            "opencode_binary_sha256": hashlib.sha256(oc_bytes).hexdigest(),
                            "opencode_binary_note": "pin-shaped key",
                        }}), encoding="utf-8")))
                code, output = run_world(rev)
                check("a 4th pin row cannot read 3/3",
                      code == 1 and "pins OK 3/3" in output, (code, output.strip()))

                # row-count guard: an 8th check with 7 PASS must not read 7 of 7
                rev = commit_world("extra check",
                                   lambda: (satisfying(),
                                            inventory("all-checks-pass\nextra-check\n")))
                code, output = run_world(rev)
                check("an 8th check cannot read 7 of 7",
                      code == 1 and "surfaces pass 7 of 7" in output,
                      (code, output.strip()))

                # cannot evaluate: unparseable ledger
                rev = commit_world("bad ledger", lambda: (
                    satisfying(),
                    (verifiers / "census-removals.json").write_text(
                        "{not json", encoding="utf-8")))
                code, output = run_world(rev)
                check("unparseable ledger is exit 2",
                      code == 2 and "cannot evaluate" in output, (code, output.strip()))

                # cannot evaluate: the surfaces instrument is absent at the rev
                rev = commit_world("no surfaces script", lambda: (
                    satisfying(),
                    (verifiers / "verify_surfaces.py").unlink()))
                code, output = run_world(rev)
                check("missing instrument is exit 2",
                      code == 2 and "cannot evaluate" in output, (code, output.strip()))

                # the dump is the LIVE stand-in: the substrate line names it
                rev = commit_world("satisfying again", satisfying)
                code, output = run_world(rev)
                check("substrate line names the bytes the counter dumped",
                      code == 0 and f"substrate opencode: {dump_override}" in output,
                      (code, output.strip()))

                # a pin on bytes other than the live substrate does not hold,
                # even when the pin script says PASS (the stub world's shape)
                def stray_pin() -> None:
                    satisfying()
                    (verifiers / "fixture-live").write_bytes(
                        oc_bytes + b"live variant marker\n")

                rev = commit_world("pinned bytes are not the live bytes", stray_pin)
                code, output = run_world(rev)
                check("a pin on other bytes is not counted",
                      code == 1 and ("pins OK 2/3; surfaces pass 7 of 7; "
                                     "removal ledger 1 of 1 verified") in output
                      and "substrate identity" in output, (code, output.strip()))

                # cannot evaluate: the surfaces instrument answers with no rows
                rev = commit_world("empty surfaces report",
                                   lambda: (satisfying(),
                                            inventory("all-checks-pass\nempty-report\n")))
                code, output = run_world(rev)
                check("an empty instrument report is exit 2, not 0 of 7",
                      code == 2 and "verify_surfaces.py reported 0 row(s)" in output
                      and "0 of 7" not in output, (code, output.strip()))
            finally:
                BASE_REV = previous_base
    except (OSError, subprocess.CalledProcessError, ValueError) as exc:
        check("isolated fixture execution", False, str(exc))

    print(f"{failures} failure(s) over {assertions} assertions")
    return 1 if failures else 0


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--rev", help="lane revision to measure")
    ap.add_argument("--repo", default=None,
                    help="lane repository (default: nearest ancestor holding "
                         "%s)" % BASELINE_PATH)
    ap.add_argument("--opencode-binary", metavar="PATH", default=None,
                    help="override the counter's own strings dump (fixtures only)")
    ap.add_argument("--self-test", action="store_true",
                    help="exercise every conjunct on isolated fixtures")
    args = ap.parse_args(argv)
    if args.self_test:
        return self_test()
    if args.rev is None:
        ap.error("--rev is required unless --self-test is selected")
    repo = Path(args.repo) if args.repo else default_repo()

    try:
        base = opencode_classes(git(repo, "show", f"{BASE_REV}:{BASELINE_PATH}"))
        with tempfile.TemporaryDirectory(prefix="substrate-repin-") as td:
            tree = Path(td)
            extract(repo, args.rev, tree)
            gate = tree / "verifiers" / "verify_surfaces.py"
            pins = tree / "verifiers" / "check_substrate_pins.py"
            if not gate.is_file() or not pins.is_file():
                raise EnvError("gate or pin script missing at the revision")
            pj = run_instrument(pins, tree)
            sj = run_instrument(gate, tree)
            rows = pj.get("checks") or pj.get("pins") or []
            checks = sj.get("checks") or []
            if not isinstance(rows, list) or not isinstance(checks, list):
                raise EnvError("instrument payload is not a row list")
            k = sum(1 for r in rows if r.get("verdict") == "PASS")
            p = sum(1 for c in checks if c.get("status") == "PASS")
            # A reported row is a measurement, whatever its verdict; an empty
            # report is not.  verify_surfaces.py exits 2 with `checks: []` when
            # it cannot find its binary, and counting that as `0 of 7` would
            # assert seven measured failures that were never measured.
            if not rows or not checks:
                which = ("check_substrate_pins.py" if not rows
                         else "verify_surfaces.py")
                payload = pj if not rows else sj
                err = payload.get("error")
                raise EnvError(
                    "%s reported 0 row(s) (exit_code %s%s); pins %d/%d row(s) "
                    "PASS, surfaces %d/%d check(s) PASS"
                    % (which, payload.get("exit_code"),
                       ": %s" % err if err else "", k, len(rows), p, len(checks)))
            dump_arg = args.opencode_binary or HOST_OPENCODE
            dump_path = Path(dump_arg)
            if not dump_path.is_file():
                raise EnvError("no readable live opencode binary at %s" % dump_path)
            dump_bytes = dump_path.read_bytes()
            live_sha = hashlib.sha256(dump_bytes).hexdigest()
            # A pin holds only against the substrate this counter measured.
            # check_substrate_pins.py compares the pin with whatever sits at
            # the tree's own path, so it cannot tell the host binary from a
            # stub whose own sha was pinned; the counter dumped the live bytes
            # and can.  An opencode sha256 row that PASSes while naming other
            # bytes is not a pin on the host substrate and does not count.
            def holds(row: dict) -> bool:
                if row.get("verdict") != "PASS":
                    return False
                if row.get("pin") != OPENCODE_PIN:
                    return True
                expect = row.get("expect")
                return isinstance(expect, str) and expect.lower() == live_sha

            k = sum(1 for r in rows if holds(r))
            stray = [r.get("pin") for r in rows
                     if r.get("verdict") == "PASS" and not holds(r)]
            dump_text = strings_dump(dump_path)
            verdict = ledger_verdict(base, opencode_classes(
                (tree / BASELINE_PATH).read_bytes()), read_ledger(tree),
                dump_text)
    except (EnvError, subprocess.CalledProcessError, json.JSONDecodeError, KeyError,
            ValueError, OSError, tarfile.TarError) as exc:
        print(f"cannot evaluate: {exc}", file=sys.stderr)
        return 2

    print(f"host substrate re-derived: pins OK {k}/{PINS_TOTAL}; "
          f"surfaces pass {p} of {CHECKS_TOTAL}; removal ledger "
          f"{verdict['verified']} of {verdict['total']} verified")
    print(f"substrate opencode: {dump_path} sha256 {live_sha} "
          f"bytes {len(dump_bytes)} strings {len(dump_text.splitlines())}")
    if stray:
        print("FAIL substrate identity: pin(s) %s PASS on bytes that are not the "
              "live opencode the counter dumped (sha256 %s)"
              % (", ".join(stray), live_sha), file=sys.stderr)
    if k != PINS_TOTAL or len(rows) != PINS_TOTAL:
        print("FAIL pins: %d of %d row(s) hold, %d row(s) reported, %d expected"
              % (k, len(rows), len(rows), PINS_TOTAL), file=sys.stderr)
    if p != CHECKS_TOTAL or len(checks) != CHECKS_TOTAL:
        print("FAIL surfaces: %d of %d check(s) PASS, %d check(s) reported, "
              "%d expected" % (p, len(checks), len(checks), CHECKS_TOTAL),
              file=sys.stderr)
    if verdict["extra"]:
        print("FAIL removal ledger: %d ledgered class(es) whose literal is present "
              "in the dump: %s" % (len(verdict["extra"]), ", ".join(verdict["extra"])),
              file=sys.stderr)
    if verdict["missing"]:
        print("FAIL removal ledger: %d absent class(es) not ledgered: %s"
              % (len(verdict["missing"]), ", ".join(verdict["missing"])),
              file=sys.stderr)
    if verdict["unkept"]:
        print("FAIL kept-identity: %d base class(es) neither kept nor ledgered: %s"
              % (len(verdict["unkept"]), ", ".join(verdict["unkept"])),
              file=sys.stderr)
    ok = (k == PINS_TOTAL and len(rows) == PINS_TOTAL
          and p == CHECKS_TOTAL and len(checks) == CHECKS_TOTAL
          and not verdict["extra"] and not verdict["missing"]
          and not verdict["unkept"])
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
