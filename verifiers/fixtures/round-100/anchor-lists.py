#!/usr/bin/env python3
"""anchor-lists v1 (round 100, claim C2, frozen counting command; plans/round-100.md).

Usage: python3 -B verifiers/fixtures/round-100/anchor-lists.py REV [REPO] [--fleet FLEET]
  REV    commit to measure
  REPO   repository to read REV from (default: this lane; a scratch repo for a control world)
  FLEET  fleet root whose entries are symlinked beside the sandbox (default: this lane's parent)

Claim C2 (consistency, calibration sub-axis): the lane's self-assessment gate
verifiers/verify_skill_checklist.py says of a citation token what the repo shows. Its
`strip_token_dressing` documents that "a citation ... may carry a line anchor (`file.md:42`) ...
[which does not] change the path", but accepts only `:N` and `:N-M`; a comma-list anchor `:N,M`
(the form SKILL.md already uses, `S090 :10,18,34,40-42`) is tested as part of the path, so a cited
file that exists reads red (round-98 ScoutTipReds F5; round-99 stopgap: correction row LOG.md:3598
for SCORECARD.md:529).

The counter measures, at REV:

  mismatches  ROWS below is a frozen truth table of citation tokens over a hermetic fixture world
              (corpus/lessons/x.md exists, 40 lines; corpus/lessons/missing.md does not). Each row is
              run through BOTH public check functions of the REV checklist module, each in its own
              fresh world: `check_governance_citations(world, errata=(), corrections=())` over a
              one-token LOG.md (SCORECARD.md holds one always-resolving token so the check evaluates),
              and `check_citation_resolves(["- `TOKEN`"], world)`. PASS means "resolves", FAIL means
              "red"; any other status, or an exception, is a mismatch. Tally
              `mismatches M of 2N`.
  gate        from a fleet-shaped sandbox of REV (`build_sandbox` from the ROUND-BASE bytes of
              verifiers/check_tip_battery.py, never from REV), the checklist with no arguments exits
              0, prints at least PASS_MIN `PASS ` lines and no `FAIL `/`N/A ` line.
  selftest    the checklist's `--self-test` in the sandbox exits 0 with an assertion count not below
              SELFTEST_FLOOR (the round-base count, measured pre-data).
  kill        the revert mutant — FIX_LINE (which must occur exactly once in the REV checklist)
              replaced by BASE_LINE, written ON DISK in a copy of the sandbox — makes the checklist's
              `--self-test` exit 1 with a last summary `N failure(s) over M assertions`, N >= 1, and a
              `self-test FAIL: ` line. An absent FIX_LINE is a kill failure.
  frozen      (1) the REV checklist equals the round-base checklist after (a) BASE_LINE -> FIX_LINE,
              (b) deleting the body of `def self_test` up to the next top-level `def `, and (c)
              deleting the `GOVERNANCE_CORRECTIONS = (...)` block, on both sides; and the REV block
              evaluates to the round-base rows minus exactly the one row whose stale token is
              RETIRED_STALE (every other base row survives unchanged, nothing is added);
              (2) verifiers/check_tip_battery.py is identical to the round base outside its
              `INSTRUMENT_PINS = {...}` block; (3) verify_corpus_integrity.py and
              verify_corpus_independent.py are byte-identical to the round base.
  battery     `check_tip_battery.py --repo <sandbox> --rev REV --fleet FLEET` (REV bytes) reports
              `guards 5 of 5` (the instrument-pin guard admits the REV checklist blob) and its line
              `gate verifiers/verify_skill_checklist.py exit 0`. The battery's two corpus gates are
              not read here: at the round base they are red from the closure-landed, unindexed
              round-99 spot-check lesson (receipts/c2-base.txt), which is landing no-harm work (Q89),
              not this claim's surface.

Predicate (frozen; the same sentence in plans/round-100.md):
  C2-PREDICATE-MET iff (mismatches) the truth table reads 0 mismatches over both public check
  paths; (gate) the real-tree checklist is green; (selftest) its self-test holds at or above the
  base floor; (kill) the revert mutant is killed by the self-test; (frozen) all three frozen-byte
  conjuncts hold; (battery) the tip battery reads guards 5 of 5 and its checklist gate exits 0.
Output: one line per measurement, then
  `C2 mismatches M of 2N; gate <GREEN|RED>; self-test <HELD|BROKEN>; revert mutant <KILLED|SURVIVED|ABSENT>;
   frozen F of 3; battery <ok|FAIL>`
  and `C2-PREDICATE-MET` / `C2-PREDICATE-UNMET` / `C2-NOT-EVALUATED`.
Exit 0 met, 1 unmet, 2 could-not-evaluate.
Scratch under ${HYAKU_SCRATCH:-/fast/scratch/hyaku}/kotoba-r100/anchor-lists (TMPDIR honoured for
nothing else), removed on exit.

Disclosed bounds: the kill conjunct runs the mutant on disk only (no source-blind run), so a
self-test that sniffs its own source for BASE_LINE would read KILLED; reviewers read the arm. The
truth table fixes what "resolves" means for these rows only; it does not check line existence.
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

BASE = "7b449a637c03d9b4c43a81b4df37cb38c2ea89ee"
CHECKLIST = "verifiers/verify_skill_checklist.py"
BATTERY = "verifiers/check_tip_battery.py"
FROZEN = ("verifiers/verify_corpus_integrity.py", "verifiers/verify_corpus_independent.py")
BASE_LINE = '    m = re.match(r"^(.+\\.\\w+):\\d+(-\\d+)?$", tok)\n'
FIX_LINE = '    m = re.match(r"^(.+\\.\\w+):\\d+(-\\d+)?(,\\d+(-\\d+)?)*$", tok)\n'
RETIRED_STALE = "corpus/lessons/round-80-verifier-spotcheck.md:30,37"
PASS_MIN = 11
SELFTEST_FLOOR = 1864  # round-base `--self-test` assertion count (receipts/c2-base.txt)
TIMEOUT_S = 600
BATTERY_TIMEOUT_S = 1800
SUMMARY = re.compile(r"^(\d+) failure\(s\) over (\d+) assertions$", re.M)
PINS_RE = re.compile(r"^INSTRUMENT_PINS = \{\n.*?^\}\n", re.M | re.S)
CORR_RE = re.compile(r"^GOVERNANCE_CORRECTIONS = \(\n.*?^\)\n", re.M | re.S)
SELFTEST_RE = re.compile(r"^def self_test\(\).*?(?=^def )", re.M | re.S)

X = "corpus/lessons/x.md"
M = "corpus/lessons/missing.md"
# (row id, token, truth): truth "resolves" or "red".
ROWS = (
    ("r01-comma-pair", X + ":30,37", "resolves"),
    ("r02-comma-range", X + ":3,7-9", "resolves"),
    ("r03-comma-trailing-punct", X + ":30,37,", "resolves"),
    ("r04-comma-long", X + ":10,18,34,40-42", "resolves"),
    ("r05-single", X + ":42", "resolves"),
    ("r06-range", X + ":1-2", "resolves"),
    ("r07-bare", X, "resolves"),
    ("r08-missing-comma", M + ":30,37", "red"),
    ("r09-missing-single", M + ":42", "red"),
    ("r10-comma-word", X + ":30,abc", "red"),
    ("r11-comma-empty", X + ":30,,37", "red"),
    ("r12-dangling-dash", X + ":5-", "red"),
    ("r13-leading-comma", X + ":,30", "red"),
    ("r14-word-anchor", X + ":abc", "red"),
)


class NotEvaluated(Exception):
    pass


def git(repo: Path, *args: str) -> subprocess.CompletedProcess:
    return subprocess.run(["git", "-C", str(repo), *args], capture_output=True)


def show(repo: Path, rev: str, path: str) -> bytes | None:
    p = git(repo, "show", "%s:%s" % (rev, path))
    return p.stdout if p.returncode == 0 else None


def run(cmd: list[str], cwd: Path, timeout: int) -> tuple[int | None, str]:
    try:
        p = subprocess.run(cmd, cwd=str(cwd), capture_output=True, text=True, timeout=timeout)
        return p.returncode, p.stdout + p.stderr
    except subprocess.TimeoutExpired:
        return None, "timeout after %d s" % timeout


def last(text: str) -> str:
    lines = [ln for ln in text.strip().splitlines() if ln.strip()]
    return lines[-1][:300] if lines else "<no output>"


def load(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def world(root: Path, tag: str) -> Path:
    w = Path(tempfile.mkdtemp(prefix=tag + "-", dir=str(root)))
    (w / "corpus" / "lessons").mkdir(parents=True)
    (w / X).write_text("".join("line %d\n" % i for i in range(1, 41)), encoding="utf-8")
    return w


def corr_rows(text: str):
    m = CORR_RE.search(text)
    if not m:
        return None
    try:
        return list(ast.literal_eval(m.group(0).split("=", 1)[1].strip()))
    except (ValueError, SyntaxError):
        return None


def checklist_confined(a: bytes | None, b: bytes | None) -> tuple[bool, str]:
    if a is None or b is None:
        return False, "checklist unreadable at base or REV"
    sa, sb = a.decode("utf-8", "replace"), b.decode("utf-8", "replace")
    if sa.count(BASE_LINE) != 1:
        return False, "base line not unique at the round base"
    sa = sa.replace(BASE_LINE, FIX_LINE)
    for s in (sa, sb):
        if len(SELFTEST_RE.findall(s)) != 1 or len(CORR_RE.findall(s)) != 1:
            return False, "self_test or corrections block not unique"
    if SELFTEST_RE.sub("", CORR_RE.sub("", sa)) != SELFTEST_RE.sub("", CORR_RE.sub("", sb)):
        return False, "bytes differ outside the fix line, self_test and the corrections data"
    ra, rb = corr_rows(sa), corr_rows(sb)
    if ra is None or rb is None:
        return False, "corrections block does not evaluate"
    retired = [r for r in ra if len(r) == 6 and r[4] == RETIRED_STALE]
    if len(retired) != 1:
        return False, "round base holds %d rows with the retired stale token" % len(retired)
    want = [r for r in ra if r is not retired[0]]
    if rb != want:
        return False, "corrections rows are not the base rows minus the one retired row"
    return True, ""


def main(argv: list[str]) -> int:
    args = list(argv)
    fleet = None
    if "--fleet" in args:
        i = args.index("--fleet")
        if i + 1 >= len(args):
            print("usage: anchor-lists.py REV [REPO] [--fleet FLEET]", file=sys.stderr)
            return 2
        fleet = Path(args[i + 1]).resolve()
        del args[i:i + 2]
    if not args or len(args) > 2:
        print("usage: anchor-lists.py REV [REPO] [--fleet FLEET]", file=sys.stderr)
        return 2
    lane = Path(__file__).resolve().parents[3]
    repo = Path(args[1]).resolve() if len(args) > 1 else lane
    fleet = fleet or lane.parent
    root = Path(os.environ.get("HYAKU_SCRATCH", "/fast/scratch/hyaku")) / "kotoba-r100" / "anchor-lists"
    root.mkdir(parents=True, exist_ok=True)
    work = Path(tempfile.mkdtemp(dir=str(root)))
    try:
        p = git(repo, "rev-parse", "--verify", args[0] + "^{commit}")
        if p.returncode != 0:
            raise NotEvaluated("REV %s not found in %s" % (args[0], repo))
        rev = p.stdout.decode().strip()
        rev_ck = show(repo, rev, CHECKLIST)
        base_ck = show(lane, BASE, CHECKLIST)
        base_battery = show(lane, BASE, BATTERY)
        if rev_ck is None or base_ck is None or base_battery is None:
            raise NotEvaluated("checklist or base battery unreadable")
        print("measured rev %s from %s; base %s" % (rev, repo, BASE))

        # mismatches — both public check functions of the REV module, one fresh world per reading
        (work / "rev_checklist.py").write_bytes(rev_ck)
        mod = load(work / "rev_checklist.py", "rev_checklist")
        worlds = work / "worlds"
        worlds.mkdir()
        mism = 0
        for rid, tok, truth in ROWS:
            for path in ("governance", "trigger"):
                w = world(worlds, rid + "-" + path)
                try:
                    if path == "governance":
                        (w / "LOG.md").write_text("- row: `%s`\n" % tok, encoding="utf-8")
                        (w / "SCORECARD.md").write_text("- anchor: `%s`\n" % X, encoding="utf-8")
                        st = mod.check_governance_citations(w, errata=(), corrections=())[0]
                    else:
                        st = mod.check_citation_resolves(["- `%s`" % tok], w)[0]
                except Exception as exc:  # an exception is a mismatch, never a reading
                    st = "EXC %s" % type(exc).__name__
                got = {"PASS": "resolves", "FAIL": "red"}.get(st, "other:%s" % st)
                ok = got == truth
                mism += not ok
                print("row %s %s %r truth %s got %s %s" % (rid, path, tok, truth, got,
                                                          "OK" if ok else "MISMATCH"))
                shutil.rmtree(w, ignore_errors=True)
        total = 2 * len(ROWS)

        # sandbox of REV (round-base build_sandbox)
        (work / "base_battery.py").write_bytes(base_battery)
        bmod = load(work / "base_battery.py", "base_battery")
        parent = work / "fleet"
        parent.mkdir()
        try:
            sandbox = bmod.build_sandbox(repo, rev, fleet, parent)
        except bmod.EnvError as exc:
            raise NotEvaluated(str(exc))
        py = [sys.executable, "-B"]

        rc, out = run(py + [CHECKLIST], sandbox, TIMEOUT_S)
        lines = out.splitlines()
        passes = sum(ln.startswith("PASS ") for ln in lines)
        others = [ln for ln in lines if ln.startswith(("FAIL ", "N/A "))]
        gate_ok = rc == 0 and passes >= PASS_MIN and not others
        print("gate exit %s PASS lines %d (min %d) FAIL/N/A lines %d %s" % (
            rc, passes, PASS_MIN, len(others), "GREEN" if gate_ok else "RED"))
        for ln in others[:6]:
            print("gate " + ln[:300])

        rc, out = run(py + [CHECKLIST, "--self-test"], sandbox, TIMEOUT_S)
        sm = SUMMARY.findall(out)
        n = int(sm[-1][1]) if sm else None
        st_ok = rc == 0 and sm and sm[-1][0] == "0" and n >= SELFTEST_FLOOR
        print("selftest exit %s assertions %s floor %d %s" % (rc, n, SELFTEST_FLOOR,
                                                              "HELD" if st_ok else "BROKEN"))

        text = rev_ck.decode("utf-8", "replace")
        if text.count(FIX_LINE) != 1:
            kill = "ABSENT"
        else:
            target = sandbox / CHECKLIST
            honest = target.read_bytes()
            try:
                target.write_text(text.replace(FIX_LINE, BASE_LINE), encoding="utf-8")
                rc, out = run(py + [CHECKLIST, "--self-test"], sandbox, TIMEOUT_S)
            finally:
                target.write_bytes(honest)
            sm = SUMMARY.findall(out)
            reported = (rc == 1 and bool(sm) and int(sm[-1][0]) >= 1
                        and any(ln.startswith("self-test FAIL: ") for ln in out.splitlines()))
            kill = "KILLED" if reported else "SURVIVED"
            print("revert mutant self-test exit %s last %r" % (rc, last(out)))
        print("kill %s" % kill)

        ck_ok, why = checklist_confined(base_ck, rev_ck)
        print("frozen %s confined to the fix line, self_test and one retired row %s%s" % (
            CHECKLIST, "YES" if ck_ok else "NO", "" if ck_ok else " (%s)" % why))
        b = show(repo, rev, BATTERY)
        bt_ok = False
        if b is not None:
            sa, sb = base_battery.decode("utf-8", "replace"), b.decode("utf-8", "replace")
            bt_ok = (len(PINS_RE.findall(sa)) == 1 and len(PINS_RE.findall(sb)) == 1
                     and PINS_RE.sub("", sa) == PINS_RE.sub("", sb))
        print("frozen %s outside INSTRUMENT_PINS %s" % (BATTERY, "IDENTICAL" if bt_ok else "CHANGED"))
        cg_ok = True
        for f in FROZEN:
            a = show(lane, BASE, f)
            ok = a is not None and a == show(repo, rev, f)
            cg_ok = cg_ok and ok
            print("frozen %s %s" % (f, "IDENTICAL" if ok else "CHANGED"))
        frozen3 = int(ck_ok) + int(bt_ok) + int(cg_ok)

        rc, out = run(py + [BATTERY, "--repo", str(sandbox), "--rev", rev, "--fleet", str(fleet)],
                      sandbox, BATTERY_TIMEOUT_S)
        gm = re.findall(r"guards (\d+) of (\d+)", out)
        ck_gate = any(re.match(r"gate %s exit 0 " % re.escape(CHECKLIST), ln)
                      for ln in out.splitlines())
        bat_ok = bool(gm) and gm[-1] == ("5", "5") and ck_gate
        for ln in out.splitlines():
            if ln.startswith(("guard ", "FAIL guard ", "gate ", "fleet root ")):
                print("battery " + ln[:300])
        print("battery exit %s %s" % (rc, "ok" if bat_ok else "FAIL"))

        met = (mism == 0 and gate_ok and st_ok and kill == "KILLED" and frozen3 == 3 and bat_ok)
        print("C2 mismatches %d of %d; gate %s; self-test %s; revert mutant %s; frozen %d of 3; battery %s"
              % (mism, total, "GREEN" if gate_ok else "RED", "HELD" if st_ok else "BROKEN",
                 kill, frozen3, "ok" if bat_ok else "FAIL"))
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
