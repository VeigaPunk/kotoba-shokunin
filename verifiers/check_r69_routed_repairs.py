#!/usr/bin/env python3
"""check_r69_routed_repairs.py — C1 counter for kotoba round 70.

Contract
--------
`python3 -B verifiers/check_r69_routed_repairs.py --rev <rev>` prints
    measured-rev: <full-sha>
    r69 routed defects closed N of 10
and exits 0 when N == 10, nonzero otherwise.  At the pinned base (the round-69 closure tip
`7d51253f99906b8551b6a0a108761eedac00de74`) it must print `r69 routed defects closed 0 of 10`
and exit 1.

The routed defects come from the round-69 closure's spot-check
(`corpus/lessons/round-69-verifier-spotcheck.md`, written by the hyaku closure, never edited by
the lane).  K69-4 (report sections at filing) is closed by the fleet report and is not counted.
Every check reads COMMITTED bytes at `--rev`; K69-11 runs the checklist gate in a
`git clone --shared` sandbox under the system temp dir, never in the lane.

  K69-1   SCORECARD.md carries a `**Round 69 axis annotations` block naming the three r69
          counters, the r69 tip and the r69 base.
  K69-2   LOG.md's round-69 entry records the off-branch landing (orchestrator fast-forward,
          the four round commits).
  K69-3   the same entry records the report attribution (4844216b, 9d9f181e, probe, 0a1199a0).
  K69-5   the two inherited r69 seat reports are tracked with the pinned blobs, and the
          round-70 lesson names both paths.
  K69-6   LOG.md has a `## Round 69` heading after the base's last line whose entry carries
          trigger / action / outcome / pointer labels.
  K69-7   the round-69 entry carries `10 receipts` and `23 landed` with `1 dispositioned`.
  K69-8   the r69 tip-defense receipt pins the r69 tip and carries, per r69 counter, a
          `command:` line, its verdict line and `exit=0`.
  K69-9   the round-70 lesson logs S201's anchor change: one line naming S201, `(13 words)`
          and `(14 words)`.
  K69-10  the round-69 lesson carries an appended erratum line (after the base's last line)
          naming `(18 assertions)` and `22 assertions`.
  K69-11  the checklist gate, run in a sandbox checkout of --rev, reports
          `governance.citation_resolves` PASS.

Trust boundary (QUALITY Q33, Q58): K69-1/2/3/6/7/9/10 are presence floors over the lane's own
records — they count named tokens in appended text, not the truth of the prose around them,
and are disclosed as such.  K69-5 pins blobs; K69-8 pins a receipt's lines; K69-11 recomputes
from a sandbox run.  The verdict also rests on the base control, the skip control and the
self-test.

Exit codes: 0 all ten closed · 1 not all closed · 2 usage/environment error.
"""
from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
import tempfile
from pathlib import Path

TOTAL = 10
BASE = "7d51253f99906b8551b6a0a108761eedac00de74"
R69_TIP = "9ce102b9e3f8896d5ed3f050ee896ca90d693a38"
R69_BASE = "a5f7459f99bb27bf697e9438362e75ac5833eca8"
R69_COMMITS = ("a02ba7e", "54f4b6c", "278b9dc", "9ce102b")
SCORECARD = "SCORECARD.md"
LOG = "LOG.md"
LESSON70 = "corpus/lessons/round-70.md"
LESSON69 = "corpus/lessons/round-69.md"
RECEIPT = ".ufo/waves/round-70/receipts/r69-tip-defense.txt"
W69 = ".ufo/waves/round-69/w1"
INHERITED = {
    f"{W69}/RevFreezeReceipt.md": "59585ea16261fe4e1a3d930962310541c5327329",
    f"{W69}/ScoutStaleLane.md": "6f4c23bad11a5aee7aa7ab255dc4e11d44bddd94",
}
R69_COUNTERS = {
    "check_skill_precedence.py": r"skill precedence backed 5 of 5",
    "check_r68_routed_repairs.py": r"r68 routed defects closed 8 of 8",
    "check_province_core.py": r"province core rows 2 of 2",
}
LABELS = ("trigger", "action", "outcome", "pointer")


class EnvError(Exception):
    pass


class Repo:
    """Committed-bytes reader; tests substitute a dict-backed fake."""

    def __init__(self, path: Path, rev: str):
        self.path = path
        self.rev = rev

    def git(self, *args: str) -> subprocess.CompletedProcess:
        return subprocess.run(["git", "-C", str(self.path), *args], capture_output=True, text=True)

    def show(self, path: str, rev: str | None = None) -> str | None:
        proc = self.git("show", f"{rev or self.rev}:{path}")
        return proc.stdout if proc.returncode == 0 else None

    def blob(self, path: str) -> str | None:
        proc = self.git("rev-parse", "--verify", "--quiet", f"{self.rev}:{path}")
        return proc.stdout.strip() if proc.returncode == 0 else None

    def checklist(self) -> dict | None:
        """Run --rev's checklist gate in a sandbox checkout; return its JSON or None."""
        with tempfile.TemporaryDirectory(prefix="k70-c1-") as tmp:
            clone = Path(tmp) / "clone"
            proc = subprocess.run(["git", "clone", "--shared", "-q", "--no-checkout",
                                   str(self.path), str(clone)], capture_output=True, text=True)
            if proc.returncode != 0:
                raise EnvError("cannot create the sandbox clone")
            proc = subprocess.run(["git", "-C", str(clone), "checkout", "-q", self.rev],
                                  capture_output=True, text=True)
            if proc.returncode != 0:
                raise EnvError(f"cannot check out {self.rev} in the sandbox")
            script = clone / "verifiers" / "verify_skill_checklist.py"
            if not script.is_file():
                return None
            proc = subprocess.run(["python3", "-B", str(script), "--json"], cwd=str(clone),
                                  capture_output=True, text=True, timeout=600)
            try:
                return json.loads(proc.stdout)
            except ValueError:
                return None


def _base_lines(repo: Repo, path: str) -> int:
    text = repo.show(path, BASE)
    return len(text.splitlines()) if text is not None else 0


def _r69_log_entry(repo: Repo) -> str | None:
    """The appended `## Round 69` entry of LOG.md (heading after the base's last line)."""
    text = repo.show(LOG)
    if text is None:
        return None
    lines = text.splitlines()
    start = None
    for i in range(_base_lines(repo, LOG), len(lines)):
        if lines[i].startswith("## Round 69"):
            start = i
            break
    if start is None:
        return None
    end = len(lines)
    for j in range(start + 1, len(lines)):
        if lines[j].startswith("## "):
            end = j
            break
    return "\n".join(lines[start:end])


def k1_scorecard(repo: Repo) -> list[str]:
    text = repo.show(SCORECARD) or ""
    m = re.search(r"^\*\*Round 69 axis annotations.*?(?=^\*\*Round 7\d|^## |\Z)", text, re.M | re.S)
    if not m:
        return ["K69-1: no `**Round 69 axis annotations` block in SCORECARD.md"]
    block = m.group(0)
    need = list(R69_COUNTERS) + [R69_TIP, R69_BASE]
    miss = [t for t in need if t not in block]
    return [f"K69-1: annotation block lacks {miss}"] if miss else []


def k2_offbranch(repo: Repo) -> list[str]:
    entry = _r69_log_entry(repo)
    if entry is None:
        return ["K69-2: no appended `## Round 69` LOG.md entry"]
    miss = [t for t in ("fast-forward", "orchestrator", *R69_COMMITS) if t not in entry]
    return [f"K69-2: round-69 entry lacks {miss}"] if miss else []


def k3_attribution(repo: Repo) -> list[str]:
    entry = _r69_log_entry(repo)
    if entry is None:
        return ["K69-3: no appended `## Round 69` LOG.md entry"]
    miss = [t for t in ("4844216b", "9d9f181e", "probe", "0a1199a0") if t not in entry]
    return [f"K69-3: round-69 entry lacks {miss}"] if miss else []


def k5_inherited(repo: Repo) -> list[str]:
    out = []
    for path, sha in INHERITED.items():
        got = repo.blob(path)
        if got != sha:
            out.append(f"K69-5: {path} blob {got} != pinned {sha}")
    lesson = repo.show(LESSON70) or ""
    for path in INHERITED:
        if path not in lesson:
            out.append(f"K69-5: round-70 lesson does not name {path}")
    return out


def k6_log_entry(repo: Repo) -> list[str]:
    entry = _r69_log_entry(repo)
    if entry is None:
        return ["K69-6: no appended `## Round 69` LOG.md entry"]
    low = entry.lower()
    miss = [l for l in LABELS if f"{l}:" not in low and f"**{l}**" not in low and f"{l}**" not in low]
    return [f"K69-6: round-69 entry lacks labels {miss}"] if miss else []


def k7_numeric(repo: Repo) -> list[str]:
    entry = _r69_log_entry(repo)
    if entry is None:
        return ["K69-7: no appended `## Round 69` LOG.md entry"]
    miss = [t for t in ("10 receipts", "23 landed", "1 dispositioned") if t not in entry]
    return [f"K69-7: round-69 entry lacks {miss}"] if miss else []


def k8_receipt(repo: Repo) -> list[str]:
    text = repo.show(RECEIPT)
    if text is None:
        return [f"K69-8: {RECEIPT} not committed"]
    out = []
    if not re.search(rf"^measured-rev:\s*{R69_TIP}\s*$", text, re.M):
        out.append("K69-8: receipt does not pin measured-rev to the r69 tip")
    blocks = re.split(r"(?m)^(?=command:)", text)
    for counter, verdict in R69_COUNTERS.items():
        hit = [b for b in blocks if b.startswith("command:") and counter in b.splitlines()[0]]
        if not hit:
            out.append(f"K69-8: no `command:` line for {counter}")
            continue
        b = hit[0]
        if not re.search(verdict, b):
            out.append(f"K69-8: {counter} block lacks its verdict line")
        if not re.search(r"^exit=0\s*$", b, re.M):
            out.append(f"K69-8: {counter} block lacks exit=0")
    return out


def k9_s201(repo: Repo) -> list[str]:
    lesson = repo.show(LESSON70) or ""
    ok = any("S201" in l and "(13 words)" in l and "(14 words)" in l for l in lesson.splitlines())
    return [] if ok else ["K69-9: round-70 lesson has no S201 (13 words)->(14 words) line"]


def k10_erratum(repo: Repo) -> list[str]:
    text = repo.show(LESSON69)
    if text is None:
        return ["K69-10: round-69 lesson missing"]
    tail = text.splitlines()[_base_lines(repo, LESSON69):]
    ok = any("(18 assertions)" in l and "22 assertions" in l for l in tail)
    return [] if ok else ["K69-10: no appended erratum naming (18 assertions) and 22 assertions"]


def k11_governance(repo: Repo) -> list[str]:
    data = repo.checklist()
    if data is None:
        return ["K69-11: the checklist gate did not produce JSON in the sandbox"]
    for c in data.get("checks", []):
        if c.get("id") == "governance.citation_resolves":
            return [] if c.get("status") == "PASS" else [
                f"K69-11: governance.citation_resolves {c.get('status')}"]
    return ["K69-11: governance.citation_resolves absent from the gate output"]


CHECKS = (k1_scorecard, k2_offbranch, k3_attribution, k5_inherited, k6_log_entry,
          k7_numeric, k8_receipt, k9_s201, k10_erratum, k11_governance)


def check(repo: Repo) -> tuple[int, list[str]]:
    closed, findings = 0, []
    for fn in CHECKS:
        f = fn(repo)
        if f:
            findings.extend(f)
        else:
            closed += 1
    return closed, findings


class FakeRepo:
    def __init__(self, files: dict[str, str], base: dict[str, str], blobs: dict[str, str],
                 gate_status: str | None):
        self.files, self.base, self.blobs, self.gate_status = files, base, blobs, gate_status
        self.rev = "f" * 40

    def show(self, path, rev=None):
        return (self.base if rev == BASE else self.files).get(path)

    def blob(self, path):
        return self.blobs.get(path)

    def checklist(self):
        if self.gate_status is None:
            return None
        return {"checks": [{"id": "governance.citation_resolves", "status": self.gate_status}]}


def _honest() -> dict:
    base = {LOG: "# LOG\n## Round 46 B2\nold\n", LESSON69: "# r69\nGate\n(18 assertions)\n",
            SCORECARD: "# SC\n"}
    log = base[LOG] + (
        "## Round 69 — appended correction entry\n"
        "- trigger: the r69 closure routed K69-6.\n"
        "- action: the orchestrator fast-forward moved master to 9ce102b; commits a02ba7e, "
        "54f4b6c, 278b9dc, 9ce102b; report commits 4844216b and 9d9f181e authored probe, "
        "erratum 0a1199a0.\n"
        "- outcome: 10 receipts, not nine; 23 landed and 1 dispositioned.\n"
        "- pointer: the spot-check.\n")
    sc = base[SCORECARD] + ("**Round 69 axis annotations (append-only).** check_skill_precedence.py "
                            f"check_r68_routed_repairs.py check_province_core.py {R69_TIP} {R69_BASE}\n")
    receipt = f"measured-rev: {R69_TIP}\n" + "".join(
        f"command: python3 -B verifiers/{c} --rev {R69_TIP}\n{v.replace(chr(92), '')}\nexit=0\n"
        for c, v in R69_COUNTERS.items())
    lesson70 = ("# r70\n" + "\n".join(INHERITED) +
                "\n- S201 anchor cell: `(13 words)` -> `(14 words)` (old -> new)\n")
    lesson69 = base[LESSON69] + "Erratum: `(18 assertions)` above reads 22 assertions.\n"
    files = {LOG: log, SCORECARD: sc, RECEIPT: receipt, LESSON70: lesson70, LESSON69: lesson69}
    return {"files": files, "base": base, "blobs": dict(INHERITED), "gate": "PASS"}


def _run(world: dict) -> tuple[int, list[str]]:
    return check(FakeRepo(world["files"], world["base"], world["blobs"], world["gate"]))


def selftest() -> int:
    failures = 0
    n, f = _run(_honest())
    if n != TOTAL:
        failures += 1
        print(f"FAIL honest world: closed {n} of {TOTAL}; {f}", file=sys.stderr)
    else:
        print(f"PASS honest world: closed {TOTAL} of {TOTAL}")

    def edit(path, old, new):
        def fn(w):
            w["files"][path] = w["files"][path].replace(old, new)
        return fn

    def setv(key, value):
        def fn(w):
            w[key] = value
        return fn

    def blob(path, value):
        def fn(w):
            w["blobs"][path] = value
        return fn

    broken = {
        "K69-1 block without the r69 tip": edit(SCORECARD, R69_TIP, "0" * 40),
        "K69-1 heading only": setv("files", {**_honest()["files"],
                                             SCORECARD: "# SC\n**Round 69 axis annotations**\n"}),
        "K69-2 no fast-forward record": edit(LOG, "fast-forward", "move"),
        "K69-2 a round commit missing": edit(LOG, "278b9dc", "xxxxxxx"),
        "K69-3 attribution missing": edit(LOG, "probe", "someone"),
        "K69-5 wrong blob": blob(f"{W69}/ScoutStaleLane.md", "1" * 40),
        "K69-5 lesson omits a path": edit(LESSON70, f"{W69}/RevFreezeReceipt.md", "x"),
        "K69-6 entry inside base (no appended heading)":
            setv("base", {**_honest()["base"], LOG: _honest()["files"][LOG]}),
        "K69-6 label missing": edit(LOG, "outcome:", "result:"),
        "K69-7 nine receipts": edit(LOG, "10 receipts", "9 receipts"),
        "K69-8 receipt pinned elsewhere": edit(RECEIPT, R69_TIP, "a" * 40),
        "K69-8 red exit": edit(RECEIPT, "exit=0\ncommand: python3 -B verifiers/check_r68",
                               "exit=1\ncommand: python3 -B verifiers/check_r68"),
        "K69-9 no new count": edit(LESSON70, "(14 words)", "(13 words) again"),
        "K69-10 erratum not appended": setv("base", {**_honest()["base"],
                                                     LESSON69: _honest()["files"][LESSON69]}),
        "K69-11 gate red": setv("gate", "FAIL"),
        "K69-11 gate unreadable": setv("gate", None),
    }
    for name, mutate in broken.items():
        w = _honest()
        mutate(w)
        n, f = _run(w)
        if n == TOTAL:
            failures += 1
            print(f"FAIL broken world survived: {name} -> closed {n}", file=sys.stderr)
        else:
            print(f"PASS broken world rejected: {name}")
    print(f"self-test: {failures} failure(s) over {len(broken) + 1} assertions")
    return 0 if failures == 0 else 1


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="C1 counter for kotoba round 70")
    ap.add_argument("--rev", default=None, help="measured revision")
    ap.add_argument("--repo", default=str(Path(__file__).resolve().parent.parent))
    ap.add_argument("--self-test", action="store_true")
    args = ap.parse_args(argv)
    if args.self_test:
        return selftest()
    if not args.rev:
        print("usage error: --rev <rev> is required", file=sys.stderr)
        return 2
    path = Path(args.repo)
    proc = subprocess.run(["git", "-C", str(path), "rev-parse", "--verify", "--quiet",
                           f"{args.rev}^{{commit}}"], capture_output=True, text=True)
    if proc.returncode != 0:
        print(f"environment error: unknown revision {args.rev}", file=sys.stderr)
        return 2
    rev = proc.stdout.strip()
    try:
        n, findings = check(Repo(path, rev))
    except (EnvError, subprocess.TimeoutExpired) as exc:
        print(f"environment error: {exc}", file=sys.stderr)
        return 2
    print(f"measured-rev: {rev}")
    print(f"r69 routed defects closed {n} of {TOTAL}")
    for f in findings:
        print(f"  {f}")
    return 0 if n == TOTAL else 1


if __name__ == "__main__":
    sys.exit(main())
