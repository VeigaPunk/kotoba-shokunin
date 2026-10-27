#!/usr/bin/env python3
"""E02ControlsC2 -- rebuild the C2 control worlds for kotoba round 77.

Scores one satisfying fixture and the six round-77 C2 control worlds against the
FROZEN counter `verifiers/check_r75_routed_repairs.py` (sha256 pinned below), on
scratch clones of the lane at the round-77 freeze commit `6523aced` (the base
for every scratch clone).

Worlds (all built from committed lane bytes; nothing here trusts the round-76
wave drafts as evidence -- the drafts are only used as *content inputs* for the
satisfying fixture, and the fixture is scored by the counter, not believed):

  H   satisfying fixture: honest R1 correction (B08 draft, applied to the
      round-75 lesson), R1 receipt, R2 receipt at the round-75 final tip
      `ac9f29510d3914a6edb97c8dbdb3445cab9141de` with the gates' own stdout
      re-generated at that revision, the R3 registry note, the R4 closing line.
      Expected: `r75 routed repairs closed 4 of 4`, exit 0.  A lower result is
      a world-build defect (the driver says which arm failed), not a finding.
  W1  token dump: lesson append that names M75-1 and the tokens only, the three
      artifact files present with empty/forged content, LOG untouched.
      Expected: 0 of 4.
  W2  R2 receipt carrying the round-76 base tip `b7f13f4b` instead of the
      round-75 final tip, with the green transcript of the r75 tip pasted under
      that wrong label.  Expected: only R2 open (3 of 4).
  W3  R2 receipt with the r75-tip label and the round-76 base stdout (red gates)
      copied under it.  Expected: only R2 open (3 of 4).
  W4  R1 correction that names no superseded M75-1 text (no quoted row, no
      quoted Gate reject candidate).  Expected: only R1 open (3 of 4).
  W5  R4 closing line present with the report pair and R75Attack28 but without
      `0 dead`.  Expected: only R4 open (3 of 4).
  W6  the cheapest do-nothing world: the freeze commit as is.  Expected 0 of 4.

Every counter invocation is `python3 -B verifiers/check_r75_routed_repairs.py
--repo <scratch clone> --rev <scratch commit> --work <scratch work dir>` and its
OWN exit status is captured (no pipeline).

Usage:
  python3 -B .ufo/waves/round-77/build/E02ControlsC2.build_controls.py \
      [--out <receipt>] [--scratch <dir>] [--keep]
"""
from __future__ import annotations

import argparse
import hashlib
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

LANE = Path("/home/vgpnk/Projects/shokunin/kotoba-shokunin")
COUNTER_REL = "verifiers/check_r75_routed_repairs.py"
COUNTER_SHA256 = "989203c40e1aab55fc14ee1d444dd4fa8b49fe01144b2dcdeaa6a27fa39f4a63"

# The round-77 freeze commit: base for every scratch clone.
LANE_HEAD = "6523aced1ee0ebe07dca996213bdc645a6acbd1e"
# The round-77 claim base (only used to name it; the freeze commit is the clone base).
R77_BASE = "2f675548eaad2a037a899d39247c1fd7a88aaf48"
# The round-76 base: the revision whose lesson the R1 append must extend.
R76_BASE = "b7f13f4b39cbd43076a85568adca763a6f674e7a"
# The round-75 final tip: the revision R2 must name.
R75_TIP = "ac9f29510d3914a6edb97c8dbdb3445cab9141de"

LESSON = "corpus/lessons/round-75.md"
LOG = "LOG.md"
R1_RECEIPT = ".ufo/waves/round-76/receipts/r1-folded-render.txt"
NOHARM = ".ufo/waves/round-76/receipts/noharm-at-tip.txt"
NOTE = ".ufo/waves/round-76/w2-registry-note.md"
B08_DIFF = ".ufo/waves/round-76/build/B08-r1-round-75-correction.diff"
NOTE_DRAFT = ".ufo/waves/round-76/build/w2-registry-note.md"

POINTER = ("- **Pointer:** `.ufo/waves/round-75/w1/` (64-seat wave-1 reports); "
           "w2 falsify results pending; `corpus/lessons/round-75.md`.")

BULLET_R4 = (
    "- **W2 settlement (closing line appended in round 76; R4):** wave `kotoba-r75-w2` "
    "settled 64 of 64 results with 0 dead seats and 63 of 64 report files present; the one "
    "absent report, seat `R75Attack28` (named "
    "`kotoba-shokunin/.ufo/waves/round-75/w2/R75Attack28.md`, which does not exist), is "
    "recorded as a phantom in `.ufo/waves/round-76/w2-registry-note.md` (R3).")
BULLET_CITE = (
    "- **No-harm receipt (appended in round 76; R2):** the post-landing corpus-gate greens "
    "this entry claimed in prose only are re-run and receipted at "
    f"`{R75_TIP}` in `.ufo/waves/round-76/receipts/noharm-at-tip.txt` — "
    "`python3 -B verifiers/verify_corpus_integrity.py --json` and "
    "`python3 -B verifiers/verify_corpus_independent.py --json`, stdout and exit codes recorded.")

TOKEN_DUMP = (
    "\n## Correction (appended, round 76 — R1 token dump)\n\n"
    "M75-1 is named here only as a token; the Gate reject candidate likewise.\n"
    "Render: 1,022 characters. Frontmatter block: lines 4-18.\n"
    "Authority: corpus/lessons/round-75-verifier-spotcheck.md § 6 R1.\n")

CORRECTION_W4 = (
    "\n## Correction (appended, round 76 — R1)\n\n"
    "M75-1 is superseded: its premise was stale. The description renders 1,022 characters "
    "(YAML folded scalar, clip chomping, terminal newline kept), frontmatter block lines 4-18.\n\n"
    "Authority: corpus/lessons/round-75-verifier-spotcheck.md § 6 R1.\n")

FORGED_NOHARM = (
    f"tip: {R75_TIP}\n"
    "$ python3 -B verifiers/verify_corpus_integrity.py --json\n"
    "PASS\nexit=0\n"
    "$ python3 -B verifiers/verify_corpus_independent.py --json\n"
    "PASS\nexit=0\n")


class Fail(Exception):
    pass


def run(cmd: list[str], timeout: int | None = None) -> subprocess.CompletedProcess:
    return subprocess.run(cmd, capture_output=True, text=True, timeout=timeout)


def git(repo: Path, *args: str, timeout: int | None = None) -> subprocess.CompletedProcess:
    return run(["git", "-C", str(repo), *args], timeout=timeout)


def need(proc: subprocess.CompletedProcess, what: str) -> subprocess.CompletedProcess:
    if proc.returncode != 0:
        raise Fail(f"{what}: exit {proc.returncode}: {proc.stderr.strip()[:600]}")
    return proc


def show(repo: Path, rev: str, path: str) -> str:
    return need(git(repo, "show", f"{rev}:{path}"), f"git show {rev[:10]}:{path}").stdout


def toplevel(repo: Path) -> str:
    return need(git(repo, "rev-parse", "--show-toplevel"), f"toplevel {repo}").stdout.strip()


def make_clone(root: Path, name: str) -> Path:
    clone = root / name
    need(run(["git", "clone", "--shared", "-q", "--no-checkout", str(LANE), str(clone)]),
         f"clone {name}")
    top = Path(toplevel(clone)).resolve()
    if top != clone.resolve():
        raise Fail(f"scratch clone toplevel {top} is not {clone}")
    need(git(clone, "config", "user.name", "scratch-r77"), "clone config user.name")
    need(git(clone, "config", "user.email", "scratch@example.invalid"), "clone config user.email")
    need(git(clone, "checkout", "-q", LANE_HEAD), "clone checkout freeze commit")
    return clone


def write_file(clone: Path, rel: str, body: str) -> None:
    path = clone / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(body, encoding="utf-8")


def commit_all(clone: Path, message: str) -> str:
    top = Path(toplevel(clone)).resolve()
    if top != clone.resolve():
        raise Fail(f"refusing to commit: toplevel {top} is not {clone}")
    need(git(clone, "add", "-A"), "git add -A")
    need(git(clone, "commit", "-q", "-m", message), "scratch commit")
    return need(git(clone, "rev-parse", "HEAD"), "rev-parse HEAD").stdout.strip()


def gate_transcript(scratch: Path, rev: str) -> dict:
    """Run both corpus gates at `rev`, normalized exactly as the counter does."""
    tmp = Path(tempfile.mkdtemp(prefix=f"gates-{rev[:8]}-", dir=str(scratch)))
    try:
        clone = tmp / "clone"
        need(run(["git", "clone", "--shared", "-q", "--no-checkout", str(LANE), str(clone)]),
             f"gate clone for {rev[:10]}")
        if Path(toplevel(clone)).resolve() != clone.resolve():
            raise Fail("gate sandbox toplevel mismatch")
        need(git(clone, "checkout", "-q", rev), f"gate checkout {rev[:10]}")
        out = {}
        for key, script in (("integrity", "verify_corpus_integrity.py"),
                            ("independent", "verify_corpus_independent.py")):
            proc = run(["python3", "-B", str(clone / "verifiers" / script),
                        "--repo", str(clone), "--json"], timeout=600)
            out[key + "_exit"] = proc.returncode
            out[key + "_out"] = proc.stdout.replace(str(clone), "<repo>")
        return out
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


def r1_receipt() -> str:
    return (
        f"measured-rev: {R75_TIP}\n"
        "convention: YAML folded scalar `description: >`, clip chomping (terminal newline kept)\n"
        "folded render (clip): 1022 characters\n"
        "stripped variant: 1021 characters\n"
        "frontmatter block lines 4-18\n"
        "exit=0\n")


def noharm_receipt(tip: str, gates: dict) -> str:
    return (
        f"tip: {tip}\n"
        "$ python3 -B verifiers/verify_corpus_integrity.py --json\n"
        f"{gates['integrity_out']}exit={gates['integrity_exit']}\n"
        "$ python3 -B verifiers/verify_corpus_independent.py --json\n"
        f"{gates['independent_out']}exit={gates['independent_exit']}\n")


def insert_log_bullets(log_base: str, bullet_r4: str) -> str:
    if log_base.count(POINTER) != 1:
        raise Fail(f"LOG.md no longer carries exactly one round-75 pointer line "
                   f"(found {log_base.count(POINTER)})")
    # Insert only inside the `## Round 75` section, immediately after the pointer.
    head, sep, tail = log_base.partition(POINTER)
    if "## Round 75" not in head:
        raise Fail("LOG.md pointer is not inside the `## Round 75` section")
    block = "\n" + bullet_r4 + "\n" + BULLET_CITE
    # `sep` ends at the pointer line; append the bullets on their own lines.
    return head + sep + block + tail


def apply_world(clone: Path, variant: str, data: dict) -> None:
    lesson_base = data["lesson_base"]
    log_base = data["log_base"]
    if variant == "W6":
        return
    if variant == "H":
        write_file(clone, LESSON, lesson_base + data["correction"])
        write_file(clone, LOG, insert_log_bullets(log_base, BULLET_R4))
        write_file(clone, R1_RECEIPT, r1_receipt())
        write_file(clone, NOHARM, noharm_receipt(R75_TIP, data["gates_ac"]))
        write_file(clone, NOTE, data["note"])
    elif variant == "W1":
        write_file(clone, LESSON, lesson_base + TOKEN_DUMP)
        write_file(clone, R1_RECEIPT, "")
        write_file(clone, NOHARM, FORGED_NOHARM)
        write_file(clone, NOTE, "")
    elif variant == "W2":
        write_file(clone, LESSON, lesson_base + data["correction"])
        write_file(clone, LOG, insert_log_bullets(log_base, BULLET_R4))
        write_file(clone, R1_RECEIPT, r1_receipt())
        write_file(clone, NOHARM, noharm_receipt(R76_BASE, data["gates_ac"]))
        write_file(clone, NOTE, data["note"])
    elif variant == "W3":
        write_file(clone, LESSON, lesson_base + data["correction"])
        write_file(clone, LOG, insert_log_bullets(log_base, BULLET_R4))
        write_file(clone, R1_RECEIPT, r1_receipt())
        write_file(clone, NOHARM, noharm_receipt(R75_TIP, data["gates_b7"]))
        write_file(clone, NOTE, data["note"])
    elif variant == "W4":
        write_file(clone, LESSON, lesson_base + CORRECTION_W4)
        write_file(clone, LOG, insert_log_bullets(log_base, BULLET_R4))
        write_file(clone, R1_RECEIPT, r1_receipt())
        write_file(clone, NOHARM, noharm_receipt(R75_TIP, data["gates_ac"]))
        write_file(clone, NOTE, data["note"])
    elif variant == "W5":
        deadless = BULLET_R4.replace("with 0 dead seats and 63 of 64", "and 63 of 64")
        if deadless == BULLET_R4:
            raise Fail("W5 anchor for `0 dead` missing in the R4 bullet")
        write_file(clone, LESSON, lesson_base + data["correction"])
        write_file(clone, LOG, insert_log_bullets(log_base, deadless))
        write_file(clone, R1_RECEIPT, r1_receipt())
        write_file(clone, NOHARM, noharm_receipt(R75_TIP, data["gates_ac"]))
        write_file(clone, NOTE, data["note"])
    else:
        raise Fail(f"unknown world {variant}")


def score(counter: Path, clone: Path, rev: str, work: Path) -> tuple[list[str], int, str]:
    """Return (command argv, exit status, stdout+stderr)."""
    work.mkdir(parents=True, exist_ok=True)
    argv = ["python3", "-B", str(counter), "--repo", str(clone), "--rev", rev,
            "--work", str(work)]
    proc = run(argv, timeout=1800)
    return argv, proc.returncode, proc.stdout + proc.stderr


def parse_repairs(text: str) -> dict[str, str]:
    out = {}
    for label in ("R1", "R2", "R3", "R4"):
        m = re.search(rf"(?m)^{label}: (open|closed)$", text)
        if m:
            out[label] = m.group(1)
    return out


EXPECT = {
    "H": {"R1": "closed", "R2": "closed", "R3": "closed", "R4": "closed"},
    "W1": {"R1": "open", "R2": "open", "R3": "open", "R4": "open"},
    "W2": {"R1": "closed", "R2": "open", "R3": "closed", "R4": "closed"},
    "W3": {"R1": "closed", "R2": "open", "R3": "closed", "R4": "closed"},
    "W4": {"R1": "open", "R2": "closed", "R3": "closed", "R4": "closed"},
    "W5": {"R1": "closed", "R2": "closed", "R3": "closed", "R4": "open"},
    "W6": {"R1": "open", "R2": "open", "R3": "open", "R4": "open"},
}

DESC = {
    "H": "satisfying fixture (honest four repairs; built from committed bytes)",
    "W1": "token dump: lesson tokens only, three artifact files empty/forged, LOG untouched",
    "W2": "R2 receipt carries the r76 base tip b7f13f4b with the r75-tip green transcript",
    "W3": "R2 receipt carries the r75 tip label with the r76 base red stdout copied under it",
    "W4": "R1 correction names no superseded M75-1 text (no quoted row / Gate candidate)",
    "W5": "R4 closing line present with 63 of 64 and R75Attack28 but without `0 dead`",
    "W6": "cheapest do-nothing world: the round-77 freeze commit as is",
}

ORDER = ["H", "W1", "W2", "W3", "W4", "W5", "W6"]


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="rebuild C2 control worlds (seat E02ControlsC2)")
    ap.add_argument("--out", default=str(Path(__file__).resolve().parent /
                                         "E02ControlsC2.c2-controls.txt"))
    ap.add_argument("--scratch", default="/fast/scratch/hyaku/kotoba-r77/E02ControlsC2")
    ap.add_argument("--keep", action="store_true", help="keep the scratch run directory")
    args = ap.parse_args(argv)

    counter = LANE / COUNTER_REL
    if not counter.is_file():
        print(f"environment error: {counter} is absent", file=sys.stderr)
        return 2
    digest = hashlib.sha256(counter.read_bytes()).hexdigest()
    if digest != COUNTER_SHA256:
        print(f"environment error: counter sha256 {digest} != frozen {COUNTER_SHA256}",
              file=sys.stderr)
        return 2
    lane_head = need(git(LANE, "rev-parse", LANE_HEAD), "lane freeze commit").stdout.strip()

    scratch_root = Path(args.scratch).expanduser()
    scratch_root.mkdir(parents=True, exist_ok=True)
    run_dir = Path(tempfile.mkdtemp(prefix="run-", dir=str(scratch_root)))

    lines: list[str] = []

    def emit(s: str = "") -> None:
        lines.append(s)

    try:
        # Inputs, read from committed bytes at the freeze commit.
        data = {
            "lesson_base": show(LANE, LANE_HEAD, LESSON),
            "log_base": show(LANE, LANE_HEAD, LOG),
            "note": show(LANE, LANE_HEAD, NOTE_DRAFT),
            "correction": "\n".join(
                l[1:] for l in show(LANE, LANE_HEAD, B08_DIFF).splitlines()
                if l.startswith("+") and not l.startswith("+++")) + "\n",
        }
        if not data["correction"].lstrip().startswith("## Correction"):
            raise Fail("B08 diff carries no appended correction block")
        for token in ("1,021/1,024 characters", "substantially shorter",
                      "1021-character description size", "materially shorter",
                      "1,022 characters", "round-75-verifier-spotcheck.md"):
            if token not in data["correction"]:
                raise Fail(f"honest R1 correction lacks required token {token!r}")
        if data["note"].find("R75Attack28") < 0 or "63 of 64" not in data["note"]:
            raise Fail("registry-note draft lacks its R3 anchors")

        emit("# C2 control worlds — verifiers/check_r75_routed_repairs.py (seat E02ControlsC2)")
        emit("")
        emit("counter: " + str(counter))
        emit("counter sha256: " + digest + "  (frozen blob; verified before any world runs)")
        emit("lane: " + str(LANE))
        emit("scratch-clone base: " + lane_head + "  (round-77 freeze commit)")
        emit("r77 claim base: " + R77_BASE + " · r76 base: " + R76_BASE +
             " · r75 final tip: " + R75_TIP)
        emit("scratch run dir: " + str(run_dir) + ("  (kept)" if args.keep else "  (removed at exit)"))
        emit("")
        emit("Artifact inputs for the satisfying fixture (committed bytes at the freeze commit):")
        emit("  " + B08_DIFF + "  -> R1 appended correction")
        emit("  " + NOTE_DRAFT + "  -> R3 note (filed at " + NOTE + ")")
        emit("  R2 transcript: both corpus gates re-run at " + R75_TIP +
             " (green) and at " + R76_BASE + " (red), normalized as the counter normalizes")
        emit("")

        data["gates_ac"] = gate_transcript(run_dir, R75_TIP)
        data["gates_b7"] = gate_transcript(run_dir, R76_BASE)
        emit("gate transcript at r75 tip: integrity exit=%d, independent exit=%d" % (
            data["gates_ac"]["integrity_exit"], data["gates_ac"]["independent_exit"]))
        emit("gate transcript at r76 base: integrity exit=%d, independent exit=%d" % (
            data["gates_b7"]["integrity_exit"], data["gates_b7"]["independent_exit"]))
        emit("")
        if (data["gates_ac"]["integrity_exit"] != 0 or data["gates_ac"]["independent_exit"] != 0):
            raise Fail("the r75 tip does not read gate-green; the R2 fixture cannot be built")
        if (data["gates_b7"]["integrity_exit"] == 0 or data["gates_b7"]["independent_exit"] == 0):
            raise Fail("the r76 base did not read red; W3's copied-stdout premise is void")

        results = []
        for variant in ORDER:
            clone = make_clone(run_dir, variant)
            if variant != "W6":
                apply_world(clone, variant, data)
                rev = commit_all(clone, f"r77 C2 control world {variant}")
            else:
                rev = need(git(clone, "rev-parse", "HEAD"), "W6 HEAD").stdout.strip()
            if rev != LANE_HEAD and variant == "W6":
                raise Fail("W6 must be the do-nothing world at the freeze commit")
            work = run_dir / f"work-{variant}"
            argv_s, rc, out = score(counter, clone, rev, work)
            observed = parse_repairs(out)
            expected = EXPECT[variant]
            ok = observed == expected
            closed = sum(1 for v in observed.values() if v == "closed")
            defect = closed == 4 and variant != "H"
            results.append((variant, clone, rev, argv_s, rc, out, observed, ok, closed, defect))

            emit("=" * 78)
            emit(f"WORLD {variant} — {DESC[variant]}")
            emit("clone: " + str(clone))
            emit("commit: " + rev)
            emit("cmd: " + " ".join(argv_s))
            emit("--- stdout+stderr ---")
            for ln in out.rstrip("\n").split("\n"):
                emit(ln)
            emit("--- end ---")
            emit(f"exit={rc}")
            emit("repairs: " + ", ".join(f"{k}={observed.get(k, '?')}" for k in ("R1", "R2", "R3", "R4")))
            emit("expected: " + ", ".join(f"{k}={expected[k]}" for k in ("R1", "R2", "R3", "R4")))
            emit("control: " + ("PASS" if ok and not defect else "FAIL"))
            if defect:
                emit("COUNTER DEFECT: this world reached `closed 4 of 4`")
            emit("")

        # Summary.
        emit("=" * 78)
        emit("SUMMARY")
        emit(f"{'world':5} {'closed':>6}  {'exit':>4}  {'control':7}  expected-open")
        for variant, _clone, _rev, _argv, rc, _out, observed, ok, closed, defect in results:
            state = "PASS" if ok and not defect else "FAIL"
            expect_open = ", ".join(k for k, v in EXPECT[variant].items() if v == "open") or "(none)"
            emit(f"{variant:5} {closed:>6}  {rc:>4}  {state:7}  {expect_open}")
        emit("")
        defects = [r[0] for r in results if r[9]]
        failures = [r[0] for r in results if not r[7] and not r[9]]
        emit("counter defects (a world reached 4 of 4): " + (", ".join(defects) or "none"))
        emit("control mismatches: " + (", ".join(failures) or "none"))
        verdict = ("COUNTER DEFECT — a control world reached `closed 4 of 4`"
                   if defects else
                   ("DISCREPANCY — a world did not score as expected"
                    if failures else
                    "CONTROLS HOLD — 6 of 6 worlds rejected as expected on the frozen blob; "
                    "the satisfying fixture closes 4 of 4"))
        emit("VERDICT: " + verdict)
        emit("")
        emit("exit=0" if not (defects or failures) else "exit=1")
        rc_final = 0 if not (defects or failures) else 1
    finally:
        if not args.keep:
            shutil.rmtree(run_dir, ignore_errors=True)

    receipt = Path(args.out)
    receipt.parent.mkdir(parents=True, exist_ok=True)
    receipt.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("\n".join(lines))
    return rc_final


if __name__ == "__main__":
    sys.exit(main())
