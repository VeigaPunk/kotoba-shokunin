#!/usr/bin/env python3
r"""check_tip_battery.py -- C3 (consistency) counter for kotoba round 72.

Frozen predicate (the same sentence in plans/round-72.md and in the receipt):

    python3 -B verifiers/check_tip_battery.py --rev <rev>  ->  prints "tip battery
    exit 0: N of 6", exit 0 when N == 6

Claim C3: the lane's own tip battery matches the record.  The r71 plan promised
`check_gate_registry.py` `53 of 53` and a battery run, and the r71 report lists
`Corpus gates ... green`; at the base c69711e four of the six battery gates exit
1 (receipts/base-battery.txt).  A calibration claim counts mismatches between
the lane's self-assessment and observed repo state.

For `--rev <rev>` the counter builds a fleet-shaped sandbox of that revision --
`git clone --shared --no-checkout` of the lane into `<parent>/kotoba-shokunin`,
every other entry of the fleet root symlinked into `<parent>` (the r71 K69-11
construction, verifiers/check_r69_routed_repairs_v2.py:170-230) -- checks the
frozen commit at `<rev>` out, and from the clone's root runs the six frozen
commands with a 280 s per-command timeout:

    python3 -B verifiers/check_gate_registry.py --rev <rev>
    python3 -B verifiers/check_assertion_floors.py
    python3 -B verifiers/verify_skill_checklist.py
    python3 -B verifiers/verify_corpus_integrity.py
    python3 -B verifiers/verify_corpus_independent.py
    python3 -B verifiers/check_correction_sweep.py --root .

N is the number that exit 0; a timeout, an absent script or a non-zero exit is
not counted.  Output: one `gate <path> exit <rc>` line per command, then the
frozen line `tip battery exit 0: N of 6`.  Exit 0 iff N == 6 and every guard
below holds; 1 otherwise; 2 when the sandbox cannot be built (no clone, no
checkout, a fleet root that cannot be read, the pinned base absent from the
clone) -- the counter never reports a gate verdict it could not measure.

Guards (Q33) -- evaluated on committed bytes only, never on instrument output:

  no-deletions          no path under corpus/ or verifiers/, and no SKILL.md,
                        tracked at the base is absent at <rev>.
  floors                no row of verifiers/floors-registry.json carries a floor
                        lower than at the base, and no base row is dropped.
  instrument-size       the six instrument scripts gain at most 40 lines in
                        total over the base AND lose at most 40.  The plan
                        bounds the additions; the same cap on deletions is what
                        makes its shortcut control -- "replace
                        check_gate_registry.py by a stub sys.exit(0) (must fail
                        the size cap)" -- actually fail: a two-line stub
                        *adds* two lines and deletes a thousand, so an
                        additions-only cap cannot see it.
  instrument-pin        errata E2: each of the six scripts is byte-identical to the
                        base or to the one reviewed draft blob (INSTRUMENT_PINS); a
                        weakening inside the size cap fails here (wave-1 F1).
  spotcheck-identity    every corpus/lessons/*-verifier-spotcheck.md present at
                        the base is byte-identical (same blob SHA) at <rev>.  A
                        file *added* at <rev> is not a base file and is
                        reported as INFO, never a failure: the round's own
                        spot-check lesson may land at the tip, and any deletion
                        of a base file is already the no-deletions guard.

BASE and BATTERY are pinned here and never read from the revision measured.
`--base` exists only so `--self-test` can drive `main()` on tiny isolated
fixture repositories; when it differs from BASE the counter prints a `note:
base override` line, so a receipt taken with an override names itself.

Environment: --repo the measured lane (default: the nearest ancestor carrying
verifiers/ and SKILL.md, i.e. the lane root from verifiers/ and from this
draft alike), --rev the measured revision, --fleet the fleet root (default: the
repo's parent).  Read-only on the lane: every git write happens inside $TMPDIR
scratch.
"""

from __future__ import annotations

import argparse
import contextlib
import io
import json
import re
import subprocess
import sys
import tempfile
import time
from pathlib import Path

LANE = Path(__file__).resolve().parent.parent


def _default_lane() -> Path:
    """The lane root: the nearest ancestor carrying verifiers/ and SKILL.md.

    The frozen run is `python3 -B verifiers/check_tip_battery.py --rev <rev>`,
    where the script's grandparent is the lane anyway; the walk also makes the
    draft under .ufo/waves/.../build/<seat>/ resolve to the same lane, so a
    measurement never silently reads a build directory as its repository."""
    here = Path(__file__).resolve()
    for parent in here.parents:
        if (parent / "verifiers").is_dir() and (parent / "SKILL.md").is_file():
            return parent
    return LANE


BASE = "c69711ee08279609374d895bb0f3c8c18ccf15c9"        # round-72 base (pinned)
TOTAL = 6
GATE_TIMEOUT_S = 280
LINE_CAP = 400
GUARDED_PREFIXES = ("corpus/", "verifiers/")
GUARDED_FILE = "SKILL.md"
FLOORS_PATH = "verifiers/floors-registry.json"
SPOTCHECK_DIR = "corpus/lessons/"
SPOTCHECK_RE = re.compile(r"-verifier-spotcheck\.md$")
REV_TOKEN = "<rev>"

# Errata E2 (plans/round-72-addendum-1.md, frozen before data): the plan's size cap
# does not catch an instrument weakened inside 40 lines (wave-1 ExecBatteryControls
# F1: `probe-clean-guards` read 6 of 6 and passed every structural guard).  Each of
# the six scripts must therefore be byte-identical to the base or to the one
# reviewed draft blob (the wave-1 drafts ExecArmFix, ExecIndexBaseline and the
# L1's floors raise, applied to the base blobs).  Empty = no pin (self-test only).
INSTRUMENT_PINS = {
    "verifiers/check_gate_registry.py": ("95ffed389f483c3d6f93db3c08dcfdb9a2240576",),
    "verifiers/check_assertion_floors.py": (
        "780f6fe5184ecb94e70f0f79446ae4339d1aec27",
        "50348420260ab41a916ef1ab19d27966565de5af"),
    "verifiers/verify_skill_checklist.py": (
        "8d44c063e3d4b57c7c421c3107879e61983249bf",
        "6aab16849bd6d71ded8f3bcb3f95668f14f6a78f"),
    "verifiers/verify_corpus_integrity.py": (
        "71cb2730bfe89064567ad429bfd7c2da62aceb45",
        "e470eaaea5ef11c582b8353c9344ddf730c1a57a"),
    "verifiers/verify_corpus_independent.py": (
        "176abae3b66930d644482f95e1363932e4d143b4",
        "edac0df79324ba62ee25ff10a6a4d422ef59da61"),
    "verifiers/check_correction_sweep.py": ("c94b771fa7d798ef45fc3bb640422ee7910f81a6",),
}

# The frozen command list: (script path, argv after the script).  Never read
# from --rev; a revision that ships a different battery is measured by this one.
BATTERY = (
    ("verifiers/check_gate_registry.py", ("--rev", REV_TOKEN)),
    ("verifiers/check_assertion_floors.py", ()),
    ("verifiers/verify_skill_checklist.py", ()),
    ("verifiers/verify_corpus_integrity.py", ()),
    ("verifiers/verify_corpus_independent.py", ()),
    ("verifiers/check_correction_sweep.py", ("--root", ".")),
)


class EnvError(Exception):
    """The sandbox or the pinned base cannot be built/read: exit 2."""


def _tail(proc: subprocess.CompletedProcess) -> str:
    text = (proc.stderr or "") + (proc.stdout or "")
    lines = [l.strip() for l in text.splitlines() if l.strip()]
    return lines[-1] if lines else "(no output)"


def git(clone: Path, *args: str) -> subprocess.CompletedProcess:
    return subprocess.run(["git", "-C", str(clone), *args],
                          capture_output=True, text=True)


def _show(clone: Path, spec: str) -> str | None:
    proc = git(clone, "show", spec)
    return proc.stdout if proc.returncode == 0 else None


def build_sandbox(repo: Path, rev: str, fleet: Path, parent: Path) -> Path:
    """Fleet-shaped sandbox of `rev`: <parent>/kotoba-shokunin plus the fleet
    root's other entries as symlinks.  Raises EnvError when it cannot be built."""
    if not repo.is_dir():
        raise EnvError("lane repository not found: %s" % repo)
    if not fleet.is_dir():
        raise EnvError("fleet root not found: %s" % fleet)
    clone = parent / "kotoba-shokunin"
    proc = subprocess.run(
        ["git", "clone", "--shared", "-q", "--no-checkout", str(repo), str(clone)],
        capture_output=True, text=True)
    if proc.returncode != 0:
        raise EnvError("cannot create the sandbox clone: %s" % _tail(proc))
    for entry in fleet.iterdir():
        if entry.name == "kotoba-shokunin":
            continue
        try:
            (parent / entry.name).symlink_to(entry)
        except OSError as exc:
            raise EnvError("cannot link fleet entry %s: %s" % (entry.name, exc))
    proc = git(clone, "checkout", "-q", rev)
    if proc.returncode != 0:
        raise EnvError("cannot check out %s in the sandbox: %s" % (rev, _tail(proc)))
    return clone


def _tree_paths(clone: Path, rev: str) -> set[str]:
    proc = git(clone, "ls-tree", "-r", "--name-only", rev)
    if proc.returncode != 0:
        raise EnvError("cannot list the tree at %s: %s" % (rev, _tail(proc)))
    return set(proc.stdout.splitlines())


def _resolve(clone: Path, rev: str, what: str) -> None:
    proc = git(clone, "rev-parse", "--verify", "--quiet", "%s^{commit}" % rev)
    if proc.returncode != 0:
        raise EnvError("%s %s is not a commit in the sandbox" % (what, rev))


def _floors(clone: Path, rev: str) -> dict | None:
    text = _show(clone, "%s:%s" % (rev, FLOORS_PATH))
    if text is None:
        return None
    try:
        data = json.loads(text)
    except ValueError:
        return "invalid"
    rows = data.get("instruments") if isinstance(data, dict) else None
    return rows if isinstance(rows, dict) else "invalid"


def _spotcheck_shas(clone: Path, rev: str) -> dict[str, str]:
    proc = git(clone, "ls-tree", "-r", rev, "--", SPOTCHECK_DIR)
    if proc.returncode != 0:
        raise EnvError("cannot list %s at %s: %s" % (SPOTCHECK_DIR, rev, _tail(proc)))
    rows: dict[str, str] = {}
    for line in proc.stdout.splitlines():
        meta, _, path = line.partition("\t")
        fields = meta.split()
        if len(fields) >= 3 and SPOTCHECK_RE.search(path):
            rows[path] = fields[2]
    return rows


def run_guards(clone: Path, base: str, rev: str) -> tuple[list[tuple[str, str]], str, list[str]]:
    """Return ([(guard_id, detail)], summary line, [info lines]).  EnvError when
    the base or the revision cannot be read at all (not a guard verdict)."""
    _resolve(clone, base, "base")
    _resolve(clone, rev, "revision")
    failures: list[tuple[str, str]] = []
    info: list[str] = []

    base_paths = _tree_paths(clone, base)
    rev_paths = _tree_paths(clone, rev)

    guarded = [p for p in base_paths
               if p.startswith(GUARDED_PREFIXES) or p == GUARDED_FILE]
    deleted = sorted(p for p in guarded if p not in rev_paths)
    if deleted:
        for path in deleted[:5]:
            failures.append(("no-deletions",
                             "%s tracked at the base is absent at %s" % (path, rev)))
        if len(deleted) > 5:
            failures.append(("no-deletions",
                             "%d more base paths absent at %s" % (len(deleted) - 5, rev)))

    base_rows = _floors(clone, base)
    if base_rows is None:
        raise EnvError("base %s carries no %s" % (base, FLOORS_PATH))
    if base_rows == "invalid":
        raise EnvError("base %s carries an unreadable %s" % (base, FLOORS_PATH))
    rev_rows = _floors(clone, rev)
    if rev_rows is None:
        failures.append(("floors", "%s absent at %s" % (FLOORS_PATH, rev)))
    elif rev_rows == "invalid":
        failures.append(("floors", "%s unreadable at %s" % (FLOORS_PATH, rev)))
    else:
        for name in sorted(base_rows):
            old = base_rows[name].get("floor") if isinstance(base_rows[name], dict) else None
            if not isinstance(old, int):
                failures.append(("floors", "base row %s has no integer floor" % name))
                continue
            if name not in rev_rows:
                failures.append(("floors", "row %s dropped at %s" % (name, rev)))
                continue
            row = rev_rows[name]
            new = row.get("floor") if isinstance(row, dict) else None
            if not isinstance(new, int):
                failures.append(("floors", "row %s has no integer floor at %s" % (name, rev)))
            elif new < old:
                failures.append(("floors", "row %s floor %d < base %d" % (name, new, old)))

    scripts = [path for path, _ in BATTERY]
    absent = [p for p in scripts if p not in rev_paths]
    for path in absent:
        failures.append(("instrument-size", "instrument %s absent at %s" % (path, rev)))
    proc = git(clone, "diff", "--numstat", "--no-renames", base, rev, "--", *scripts)
    if proc.returncode != 0:
        raise EnvError("cannot diff the instruments %s..%s: %s" % (base, rev, _tail(proc)))
    added = deleted_lines = 0
    for line in proc.stdout.splitlines():
        fields = line.split("\t")
        if len(fields) < 3:
            continue
        a, d, path = fields[0], fields[1], fields[2]
        if a == "-" or d == "-":
            failures.append(("instrument-size", "binary diff at %s" % path))
            continue
        added += int(a)
        deleted_lines += int(d)
    for path, allowed in INSTRUMENT_PINS.items():
        got = git(clone, "rev-parse", "%s:%s" % (rev, path))
        blob = got.stdout.strip() if got.returncode == 0 else ""
        if blob not in allowed:
            failures.append(("instrument-pin", "%s blob %s at %s is not a pinned blob"
                             % (path, blob or "absent", rev)))
    if added > LINE_CAP:
        failures.append(("instrument-size", "instruments gain %d lines > %d" % (added, LINE_CAP)))
    if deleted_lines > LINE_CAP:
        failures.append(("instrument-size",
                         "instruments lose %d lines > %d" % (deleted_lines, LINE_CAP)))

    base_spot = _spotcheck_shas(clone, base)
    rev_spot = _spotcheck_shas(clone, rev)
    for path, sha in sorted(base_spot.items()):
        if path not in rev_spot:
            failures.append(("spotcheck-identity", "%s absent at %s" % (path, rev)))
        elif rev_spot[path] != sha:
            failures.append(("spotcheck-identity",
                             "%s differs from the base blob %s" % (path, sha[:12])))
    for path in sorted(set(rev_spot) - set(base_spot)):
        info.append("spotcheck added at %s (not a base file): %s" % (rev, path))
    summary = ("guarded paths %d, deleted %d; floors %d rows; instruments added %d / "
               "deleted %d lines (cap %d); spotcheck base files %d"
               % (len(guarded), len(deleted), len(base_rows), added, deleted_lines,
                  LINE_CAP, len(base_spot)))
    return failures, summary, info


def run_battery(clone: Path, rev: str) -> list[tuple[str, int | None, float, str]]:
    rows = []
    for script, extra in BATTERY:
        argv = [sys.executable, "-B", script]
        argv += [rev if a == REV_TOKEN else a for a in extra]
        path = clone / script
        if not path.is_file():
            rows.append((script, None, 0.0, "absent at %s" % rev))
            continue
        started = time.monotonic()
        try:
            proc = subprocess.run(argv, cwd=str(clone), capture_output=True,
                                  text=True, timeout=GATE_TIMEOUT_S)
            rc, why = proc.returncode, ""
        except subprocess.TimeoutExpired:
            rc, why = None, "timeout after %d s" % GATE_TIMEOUT_S
        except OSError as exc:
            rc, why = None, "not runnable: %s" % exc
        rows.append((script, rc, time.monotonic() - started, why))
    return rows


def measure(repo: Path, rev: str, fleet: Path, base: str) -> int:
    started = time.monotonic()
    with tempfile.TemporaryDirectory(prefix="k72-tip-") as tdir:
        parent = Path(tdir)
        try:
            clone = build_sandbox(repo, rev, fleet, parent)
            failures, summary, info = run_guards(clone, base, rev)
            gates = run_battery(clone, rev)
        except EnvError as exc:
            print("could-not-evaluate: %s" % exc, file=sys.stderr)
            return 2

    print("measured rev %s in a fleet-shaped sandbox; base %s" % (rev, base))
    print(summary)
    for line in info:
        print("INFO %s" % line)
    guard_ids = ("no-deletions", "floors", "instrument-size", "instrument-pin",
                 "spotcheck-identity")
    for gid in guard_ids:
        hits = [d for g, d in failures if g == gid]
        if hits:
            for detail in hits:
                print("FAIL guard %s: %s" % (gid, detail))
        else:
            print("guard %s PASS" % gid)

    n = 0
    for script, rc, wall, why in gates:
        if rc == 0:
            n += 1
        note = (" (%s)" % why) if why else ""
        print("gate %s exit %s wall %.1fs%s"
              % (script, "none" if rc is None else rc, wall, note))
    print("wall %.1fs" % (time.monotonic() - started))
    print("tip battery exit 0: %d of %d" % (n, TOTAL))   # the frozen line, last
    return 0 if n == TOTAL and not failures else 1


# ---------------------------------------------------------------- self-test ---

STUB_OK = "import sys\nsys.exit(0)\n"
STUB_BAD = "import sys\nsys.exit(1)\n"


def _fixture_git(lane: Path, *args: str) -> subprocess.CompletedProcess:
    return subprocess.run(
        ["git", "-C", str(lane), "-c", "user.name=probe",
         "-c", "user.email=probe@example.invalid", "-c", "commit.gpgsign=false", *args],
        capture_output=True, text=True)


def _commit_all(lane: Path, message: str) -> str:
    if _fixture_git(lane, "rev-parse", "--show-toplevel").stdout.strip() != str(lane):
        raise RuntimeError("fixture toplevel mismatch at %s" % lane)
    add = _fixture_git(lane, "add", "-A")
    if add.returncode != 0:
        raise RuntimeError("fixture add failed: %s" % _tail(add))
    commit = _fixture_git(lane, "commit", "-q", "-m", message)
    if commit.returncode != 0:
        raise RuntimeError("fixture commit failed: %s" % _tail(commit))
    return _fixture_git(lane, "rev-parse", "HEAD").stdout.strip()


def _make_world(root: Path, padding: int = 0) -> tuple[Path, str]:
    lane = root / "kotoba-shokunin"
    for sub in ("verifiers", "corpus/knowledge", "corpus/lessons"):
        (lane / sub).mkdir(parents=True, exist_ok=True)
    (lane / "SKILL.md").write_text("# fixture skill\n")
    (lane / "corpus/knowledge/k.md").write_text("fixture knowledge\n")
    (lane / "corpus/lessons/round-71-verifier-spotcheck.md").write_text("fixture spotcheck\n")
    body = "".join("# pad %d\n" % i for i in range(padding)) + STUB_OK
    for script, _ in BATTERY:
        (lane / script).write_text(body)
    (lane / FLOORS_PATH).write_text(json.dumps(
        {"$comment": "fixture", "instrument_total": 1,
         "instruments": {"stub": {"floor": 10, "path": BATTERY[0][0]}}}, indent=1) + "\n")
    init = subprocess.run(["git", "init", "-q", str(lane)], capture_output=True, text=True)
    if init.returncode != 0:
        raise RuntimeError("fixture init failed: %s" % _tail(init))
    return lane, _commit_all(lane, "fixture base")


def _drive(root: Path, base: str, rev: str, fleet: Path | None = None) -> tuple[int, str, str]:
    lane = root / "kotoba-shokunin"
    argv = ["--repo", str(lane), "--rev", rev, "--base", base,
            "--fleet", str(fleet if fleet is not None else root)]
    out, err = io.StringIO(), io.StringIO()
    with contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
        try:
            rc = main(argv)
        except SystemExit as exc:          # argparse errors
            rc = int(exc.code or 0)
    return rc, out.getvalue(), err.getvalue()


def _last_line(text: str) -> str:
    lines = [l for l in text.splitlines() if l.strip()]
    return lines[-1] if lines else ""


def self_test() -> int:
    global INSTRUMENT_PINS
    INSTRUMENT_PINS = {}
    failures: list[str] = []
    assertions = 0

    def check(label: str, ok: bool, detail: str = "") -> None:
        nonlocal assertions
        assertions += 1
        if not ok:
            failures.append("%s%s" % (label, (": " + detail) if detail else ""))

    with tempfile.TemporaryDirectory(prefix="k72-tip-selftest-") as tdir:
        root = Path(tdir)

        # 1. a satisfying world: every guard holds, all six gates exit 0.
        ok_root = root / "ok"
        lane, base = _make_world(ok_root)
        (lane / "notes.md").write_text("harmless\n")
        tip = _commit_all(lane, "harmless change")
        rc, out, err = _drive(ok_root, base, tip)
        check("satisfying world exits 0", rc == 0,
              "exit %d stderr %r" % (rc, err.strip()[-160:]))
        check("satisfying world prints the frozen line exactly",
              _last_line(out) == "tip battery exit 0: 6 of 6", repr(_last_line(out)))

        # 2. one broken world per guard.
        del_root = root / "guard-deletion"
        lane, base = _make_world(del_root)
        _fixture_git(lane, "rm", "-q", "corpus/knowledge/k.md")
        tip = _commit_all(lane, "delete a base corpus file")
        rc, out, err = _drive(del_root, base, tip)
        check("deletion world exits 1", rc == 1, "exit %d" % rc)
        check("deletion world names the no-deletions guard",
              "FAIL guard no-deletions: corpus/knowledge/k.md" in out, out.strip()[-200:])
        check("deletion world still counts the six gates",
              "tip battery exit 0: 6 of 6" in out, _last_line(out))

        floor_root = root / "guard-floor"
        lane, base = _make_world(floor_root)
        (lane / FLOORS_PATH).write_text(json.dumps(
            {"$comment": "fixture", "instrument_total": 1,
             "instruments": {"stub": {"floor": 9, "path": BATTERY[0][0]}}}, indent=1) + "\n")
        tip = _commit_all(lane, "lower a floor")
        rc, out, err = _drive(floor_root, base, tip)
        check("floor world exits 1", rc == 1, "exit %d" % rc)
        check("floor world names the floors guard",
              "FAIL guard floors: row stub floor 9 < base 10" in out, out.strip()[-200:])

        size_root = root / "guard-size"
        lane, base = _make_world(size_root)
        stub = lane / BATTERY[0][0]
        stub.write_text(STUB_OK + "".join("# padding line %d\n" % i for i in range(41)))
        tip = _commit_all(lane, "grow an instrument past the cap")
        rc, out, err = _drive(size_root, base, tip)
        check("size world exits 1", rc == 1, "exit %d" % rc)
        check("size world names the instrument-size guard",
              "FAIL guard instrument-size: instruments gain 41 lines > 40" in out,
              out.strip()[-220:])

        # errata E2: the instrument-pin guard.  A weakening inside the size cap
        # (two lines changed) passes every structural guard but not the pin.
        pin_root = root / "guard-pin"
        lane, base = _make_world(pin_root)
        base_blob = _fixture_git(lane, "rev-parse", "HEAD:" + BATTERY[0][0]).stdout.strip()
        INSTRUMENT_PINS = {BATTERY[0][0]: (base_blob,)}
        (lane / BATTERY[0][0]).write_text(STUB_OK + "# a two-line semantic edit\n# inside the cap\n")
        tip = _commit_all(lane, "weaken an instrument inside the size cap")
        rc, out, err = _drive(pin_root, base, tip)
        check("pin world exits 1", rc == 1, "exit %d" % rc)
        check("pin world names the instrument-pin guard",
              "FAIL guard instrument-pin: %s blob" % BATTERY[0][0] in out, out.strip()[-220:])
        check("pin world passes the size cap alone",
              "guard instrument-size PASS" in out, out.strip()[-300:])
        check("pin world still counts six gates", "tip battery exit 0: 6 of 6" in out,
              _last_line(out))
        pin_ok = root / "guard-pin-ok"
        lane, base = _make_world(pin_ok)
        base_blob = _fixture_git(lane, "rev-parse", "HEAD:" + BATTERY[0][0]).stdout.strip()
        INSTRUMENT_PINS = {BATTERY[0][0]: (base_blob,)}
        (lane / "notes.md").write_text("harmless\n")
        tip = _commit_all(lane, "harmless change under a pin")
        rc, out, err = _drive(pin_ok, base, tip)
        check("pinned world exits 0 when the blob is unchanged", rc == 0,
              "exit %d %r" % (rc, err.strip()[-160:]))
        INSTRUMENT_PINS = {}

        stub_root = root / "guard-stub"
        lane, base = _make_world(stub_root, padding=60)
        (lane / BATTERY[0][0]).write_text(STUB_OK)
        tip = _commit_all(lane, "replace a gate with a two-line stub")
        rc, out, err = _drive(stub_root, base, tip)
        check("stub world exits 1", rc == 1, "exit %d" % rc)
        check("stub world fails the deletion side of the size cap",
              "FAIL guard instrument-size: instruments lose 60 lines > 40" in out,
              out.strip()[-220:])
        check("stub world keeps the gates green", "tip battery exit 0: 6 of 6" in out,
              _last_line(out))

        spot_root = root / "guard-spotcheck"
        lane, base = _make_world(spot_root)
        with (lane / "corpus/lessons/round-71-verifier-spotcheck.md").open("a") as fh:
            fh.write("rewritten baseline\n")
        tip = _commit_all(lane, "edit the base spot-check lesson")
        rc, out, err = _drive(spot_root, base, tip)
        check("spotcheck world exits 1", rc == 1, "exit %d" % rc)
        check("spotcheck world names the spotcheck-identity guard",
              "FAIL guard spotcheck-identity: corpus/lessons/round-71-verifier-spotcheck.md"
              in out, out.strip()[-220:])

        # 3. one broken world per gate: exactly one stub exits 1, N must read 5.
        for index, (script, _) in enumerate(BATTERY):
            gate_root = root / ("gate-%d" % index)
            lane, base = _make_world(gate_root)
            (lane / script).write_text(STUB_BAD)
            tip = _commit_all(lane, "break %s" % script)
            rc, out, err = _drive(gate_root, base, tip)
            check("gate world %s exits 1" % script, rc == 1, "exit %d" % rc)
            check("gate world %s reads 5 of 6" % script,
                  "tip battery exit 0: 5 of 6" in out, _last_line(out))
            check("gate world %s names the failing gate" % script,
                  ("gate %s exit 1" % script) in out, out.strip()[-200:])

        # 4. the could-not-evaluate channel: exit 2, never a gate verdict.
        e2_root = root / "exit2-rev"
        lane, base = _make_world(e2_root)
        rc, out, err = _drive(e2_root, base, "0" * 40)
        check("unknown revision exits 2", rc == 2, "exit %d" % rc)
        check("unknown revision prints no battery line",
              "tip battery" not in out, out.strip()[-160:])
        check("unknown revision explains itself", "could-not-evaluate" in err, err.strip()[-160:])

        e2_fleet = root / "exit2-fleet"
        lane, base = _make_world(e2_fleet)
        rc, out, err = _drive(e2_fleet, base, base, fleet=e2_fleet / "missing-fleet")
        check("missing fleet root exits 2", rc == 2, "exit %d" % rc)
        check("missing fleet root explains itself", "fleet root not found" in err,
              err.strip()[-160:])

    print("self-test: %d failure(s) over %d assertions" % (len(failures), assertions))
    for failure in failures:
        print("FAIL", failure)
    return 1 if failures else 0


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--rev", help="lane revision to measure")
    ap.add_argument("--repo", default=str(_default_lane()), help="lane repository")
    ap.add_argument("--fleet", default=None,
                    help="fleet root symlinked beside the sandbox clone (default: the repo's parent)")
    ap.add_argument("--base", default=BASE,
                    help="base revision for the guards (pinned; a fixture affordance)")
    ap.add_argument("--self-test", action="store_true",
                    help="drive main() on isolated fixture worlds")
    args = ap.parse_args(argv)
    if args.self_test:
        return self_test()
    if not args.rev:
        ap.error("--rev is required unless --self-test is selected")
    repo = Path(args.repo)
    fleet = Path(args.fleet) if args.fleet else repo.parent
    if args.base != BASE:
        print("note: base override %s (fixture affordance; the lane run pins %s)"
              % (args.base, BASE))
    return measure(repo, args.rev, fleet, args.base)


if __name__ == "__main__":
    sys.exit(main())
