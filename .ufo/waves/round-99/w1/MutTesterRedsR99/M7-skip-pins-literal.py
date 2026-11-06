#!/usr/bin/env python3
"""carried-reds v1 (round 99, claim C2, frozen counting command; plans/round-99.md).

Usage: python3 -B verifiers/fixtures/round-99/carried-reds.py REV [REPO] [--fleet FLEET]
  REV    full commit to measure
  REPO   repository to read REV from (default: this lane; a scratch repo for a control world)
  FLEET  fleet root whose entries are symlinked beside the sandbox (default: this lane's parent)

Claim C2 (consistency, calibration sub-axis): the three tip-battery gates that have been red at the
lane tip since round 81 (round-98 closure routed defect 6; `.ufo/waves/round-98/w1/ScoutTipReds.md`)
read green at REV without weakening any gate.

The counter builds the fleet-shaped sandbox of REV with `build_sandbox` taken from the ROUND-BASE
bytes of verifiers/check_tip_battery.py (never from REV) and, from the sandbox root, measures:

  reds       verifiers/verify_skill_checklist.py, verifiers/verify_corpus_integrity.py and
             verifiers/verify_corpus_independent.py, run with no arguments; a gate is green iff it
             exits 0 within 600 s; the checklist gate is green only if, in addition, it prints at
             least CHECKLIST_PASS_MIN (11, its round-base check count) `PASS ` lines and no `FAIL ` or
             `N/A ` line (a check switched to N/A is not green).  Tally `carried reds green G of 3`.
  selftests  each of the three gates' `--self-test` exits 0 and its assertion count is not below
             the round-base count frozen in SELFTEST_FLOOR.
  frozen     (1, 2) verify_corpus_integrity.py and verify_corpus_independent.py are byte-identical to
             the round base; (3) check_tip_battery.py is byte-identical to the round base outside its
             `INSTRUMENT_PINS = {...}` block (a pin admission is the only battery change allowed);
             (4) verify_skill_checklist.py is byte-identical to the round base outside the
             `GOVERNANCE_CORRECTIONS_HORIZON = N` line and the `GOVERNANCE_CORRECTIONS = (...)` block,
             that block evaluates (ast.literal_eval) to a tuple of 6-tuples
             (int, str, str, int, str, str), and every round-base row survives with its log line, line
             sha256, subject file, stale token and corrected token (only its subject line may move):
             the checklist change is data, never code.
  guards     `python3 -B verifiers/check_tip_battery.py --repo <sandbox> --rev REV --fleet <FLEET>`
             (the REV bytes, run from the sandbox) prints `guards 5 of 5`.

Predicate (frozen; the same sentence in plans/round-99.md):
  C2-PREDICATE-MET iff (reds) carried reds green 3 of 3; (selftests) 3 of 3 self-tests exit 0 at or
  above their base assertion floor; (frozen) all four frozen-byte conjuncts hold; (guards) the tip
  battery at REV reports guards 5 of 5.
Output: one line per measurement, then
  `C2 carried reds green G of 3; self-tests held S of 3; frozen F of 4; guards <ok|FAIL>`
  and `C2-PREDICATE-MET` / `C2-PREDICATE-UNMET` / `C2-NOT-EVALUATED`.
Exit 0 met, 1 unmet, 2 could-not-evaluate (sandbox not buildable, REV or base unreadable).
Scratch under ${HYAKU_SCRATCH:-/fast/scratch/hyaku}/kotoba-r99/carried-reds, removed on exit.
"""
from __future__ import annotations

import ast
import importlib.util
import os
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

BASE = "52e8e95ac4faf4ded84d7b82cbc204792590d0f7"
GATES = (
    "verifiers/verify_skill_checklist.py",
    "verifiers/verify_corpus_integrity.py",
    "verifiers/verify_corpus_independent.py",
)
CHECKLIST = "verifiers/verify_skill_checklist.py"
CHECKLIST_PASS_MIN = 11
FROZEN = ("verifiers/verify_corpus_integrity.py", "verifiers/verify_corpus_independent.py")
BATTERY = "verifiers/check_tip_battery.py"
# Round-base self-test assertion counts, measured pre-data (receipts/c2-base.txt `selftest` lines).
SELFTEST_FLOOR = {
    "verifiers/verify_skill_checklist.py": 1864,
    "verifiers/verify_corpus_integrity.py": 178,
    "verifiers/verify_corpus_independent.py": 109,
}
TIMEOUT_S = 600
BATTERY_TIMEOUT_S = 1800
COUNT_RES = (
    re.compile(r"(\d+) failure\(s\) over (\d+) assertions"),
    re.compile(r"self-test: (\d+) failure\(s\) over (\d+) assertions"),
    re.compile(r"self-test: (\d+) assertions, (\d+) failures"),
)
PINS_RE = re.compile(r"^INSTRUMENT_PINS = \{\n.*?^\}\n", re.M | re.S)
CORR_RE = re.compile(r"^GOVERNANCE_CORRECTIONS = \(\n.*?^\)\n", re.M | re.S)
HORIZON_RE = re.compile(r"^GOVERNANCE_CORRECTIONS_HORIZON = \d+\n", re.M)
ROW_TYPES = (int, str, str, int, str, str)


def _rows(block: str):
    rows = ast.literal_eval(block.split("=", 1)[1].strip())
    if not isinstance(rows, tuple):
        raise ValueError("block is not a tuple")
    for r in rows:
        if not (isinstance(r, tuple) and len(r) == 6
                and all(type(v) is t for v, t in zip(r, ROW_TYPES))):
            raise ValueError("row is not a (int, str, str, int, str, str) tuple: %r" % (r,))
    return rows


def checklist_data_only(a: bytes | None, b: bytes | None) -> tuple[bool, str]:
    """Conjunct (4): the checklist change is confined to the corrections data."""
    if a is None or b is None:
        return False, "checklist unreadable at base or REV"
    sa, sb = a.decode("utf-8", "replace"), b.decode("utf-8", "replace")
    for s, who in ((sa, "base"), (sb, "REV")):
        if len(CORR_RE.findall(s)) != 1 or len(HORIZON_RE.findall(s)) != 1:
            return False, "%s: corrections block or horizon line not found exactly once" % who
    if HORIZON_RE.sub("", CORR_RE.sub("", sa)) != HORIZON_RE.sub("", CORR_RE.sub("", sb)):
        return False, "bytes differ outside the corrections data"
    try:
        ra, rb = _rows(CORR_RE.search(sa).group(0)), _rows(CORR_RE.search(sb).group(0))
    except (ValueError, SyntaxError) as exc:
        return False, "corrections block not literal data: %s" % exc
    keep = {(r[0], r[1], r[2], r[4], r[5]) for r in rb}
    lost = [r for r in ra if (r[0], r[1], r[2], r[4], r[5]) not in keep]
    if lost:
        return False, "round-base correction row(s) dropped or altered: %r" % (lost,)
    return True, ""


class NotEvaluated(Exception):
    pass


def git(repo: Path, *args: str) -> subprocess.CompletedProcess:
    return subprocess.run(["git", "-C", str(repo), *args], capture_output=True)


def show(repo: Path, rev: str, path: str) -> bytes | None:
    p = git(repo, "show", "%s:%s" % (rev, path))
    return p.stdout if p.returncode == 0 else None


def assertions(text: str) -> int | None:
    for i, rx in enumerate(COUNT_RES):
        ms = list(rx.finditer(text))
        if ms:
            m = ms[-1]
            if i == 2:
                return int(m.group(1)) if int(m.group(2)) == 0 else -1
            return int(m.group(2)) if int(m.group(1)) == 0 else -1
    return None


def run(cmd: list[str], cwd: Path, timeout: int) -> tuple[int | None, str]:
    try:
        p = subprocess.run(cmd, cwd=str(cwd), capture_output=True, text=True, timeout=timeout)
        return p.returncode, p.stdout + p.stderr
    except subprocess.TimeoutExpired:
        return None, "timeout after %d s" % timeout


def last(text: str) -> str:
    lines = [ln for ln in text.strip().splitlines() if ln.strip()]
    return lines[-1][:300] if lines else "<no output>"


def main(argv: list[str]) -> int:
    args = list(argv)
    fleet = None
    if "--fleet" in args:
        i = args.index("--fleet")
        if i + 1 >= len(args):
            print("usage: carried-reds.py REV [REPO] [--fleet FLEET]", file=sys.stderr)
            return 2
        fleet = Path(args[i + 1]).resolve()
        del args[i:i + 2]
    if not args or len(args) > 2:
        print("usage: carried-reds.py REV [REPO] [--fleet FLEET]", file=sys.stderr)
        return 2
    lane = Path(__file__).resolve().parents[3]
    repo = Path(args[1]).resolve() if len(args) > 1 else lane
    fleet = fleet or lane.parent
    root = Path(os.environ.get("HYAKU_SCRATCH", "/fast/scratch/hyaku")) / "kotoba-r99" / "carried-reds"
    root.mkdir(parents=True, exist_ok=True)
    work = Path(tempfile.mkdtemp(dir=str(root)))
    try:
        p = git(repo, "rev-parse", "--verify", args[0] + "^{commit}")
        if p.returncode != 0:
            raise NotEvaluated("REV %s not found in %s" % (args[0], repo))
        rev = p.stdout.decode().strip()
        base_battery = show(lane, BASE, BATTERY)
        if base_battery is None:
            raise NotEvaluated("round base %s unreadable in %s" % (BASE, lane))
        (work / "base_battery.py").write_bytes(base_battery)
        spec = importlib.util.spec_from_file_location("base_battery", work / "base_battery.py")
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        parent = work / "fleet"
        parent.mkdir()
        try:
            sandbox = mod.build_sandbox(repo, rev, fleet, parent)
        except mod.EnvError as exc:
            raise NotEvaluated(str(exc))
        print("measured rev %s from %s in a fleet-shaped sandbox; base %s" % (rev, repo, BASE))
        env_cmd = [sys.executable, "-B"]

        green = 0
        for g in GATES:
            rc, out = run(env_cmd + [g], sandbox, TIMEOUT_S)
            ok = rc == 0
            if g == CHECKLIST:
                lines = out.splitlines()
                passes = sum(ln.startswith("PASS ") for ln in lines)
                others = sum(ln.startswith(("FAIL ", "N/A ")) for ln in lines)
                ok = ok and passes >= CHECKLIST_PASS_MIN and others == 0
                print("checklist PASS lines %d (min %d); FAIL/N/A lines %d" % (passes, CHECKLIST_PASS_MIN, others))
            green += ok
            print("red %s exit %s %s: %s" % (g, rc, "GREEN" if ok else "RED", last(out)))

        held = 0
        for g in GATES:
            rc, out = run(env_cmd + [g, "--self-test"], sandbox, TIMEOUT_S)
            n = assertions(out)
            ok = rc == 0 and n is not None and n >= 0 and n >= SELFTEST_FLOOR[g]
            held += ok
            print("selftest %s exit %s assertions %s floor %d %s" % (
                g, rc, n, SELFTEST_FLOOR[g], "HELD" if ok else "BROKEN"))

        frozen = 0
        for f in FROZEN:
            a, b = show(lane, BASE, f), show(repo, rev, f)
            ok = a is not None and a == b
            frozen += ok
            print("frozen %s %s" % (f, "IDENTICAL" if ok else "CHANGED"))
        a, b = show(lane, BASE, BATTERY), show(repo, rev, BATTERY)
        ok = False
        if a is not None and b is not None:
            sa, sb = a.decode("utf-8", "replace"), b.decode("utf-8", "replace")
            ok = (len(PINS_RE.findall(sa)) == 1 and len(PINS_RE.findall(sb)) == 1
                  and PINS_RE.sub("", sa) == PINS_RE.sub("", sb))
            if ok:
                ok = PINS_RE.search(sb).group(0).split("=", 1)[1].strip().startswith("{")
        frozen += ok
        print("frozen %s outside INSTRUMENT_PINS %s" % (BATTERY, "IDENTICAL" if ok else "CHANGED"))
        a, b = show(lane, BASE, CHECKLIST), show(repo, rev, CHECKLIST)
        ok, why = checklist_data_only(a, b)
        frozen += ok
        print("frozen %s outside GOVERNANCE_CORRECTIONS %s%s" % (
            CHECKLIST, "DATA-ONLY" if ok else "CHANGED", "" if ok else " (%s)" % why))

        rc, out = run(env_cmd + [BATTERY, "--repo", str(sandbox), "--rev", rev, "--fleet", str(fleet)],
                      sandbox, BATTERY_TIMEOUT_S)
        gm = re.findall(r"guards (\d+) of (\d+)", out)
        guards_ok = bool(gm) and gm[-1] == ("5", "5")
        for ln in out.splitlines():
            if ln.startswith(("guard ", "FAIL guard ", "gate ", "fleet root ")):
                print("battery " + ln)
        print("battery exit %s guards %s" % (rc, "ok" if guards_ok else "FAIL"))

        met = green == 3 and held == 3 and frozen == 4 and guards_ok
        print("C2 carried reds green %d of 3; self-tests held %d of 3; frozen %d of 4; guards %s"
              % (green, held, frozen, "ok" if guards_ok else "FAIL"))
        print("C2-PREDICATE-MET" if met else "C2-PREDICATE-UNMET")
        return 0 if met else 1
    except NotEvaluated as exc:
        print("could-not-evaluate: %s" % exc)
        print("C2-NOT-EVALUATED")
        return 2
    except Exception as exc:  # total exit ladder
        print("could-not-evaluate: unexpected %s: %s" % (type(exc).__name__, exc))
        print("C2-NOT-EVALUATED")
        return 2
    finally:
        shutil.rmtree(work, ignore_errors=True)


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
