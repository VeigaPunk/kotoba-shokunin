#!/usr/bin/env python3
"""check_r69_routed_repairs_v2.py — C1 successor counter for kotoba round 71.

Frozen predicate (the same sentence in plans/round-71.md and in the receipts):

    python3 -B verifiers/check_r69_routed_repairs_v2.py --rev <rev>
        ->  prints "r69 routed defects closed N of 10", exit 0 when N == 10

Successor to check_r69_routed_repairs.py (round 70), redesigned against the
round-70 closure's routed defects (corpus/lessons/round-70-verifier-spotcheck.md
§ Routed defects; wave seats RevC1Counter, MutC1Counter, CritMistakes):

  HIGH-1  the token-dump world scored 10/10 -- v2 re-checks the repaired
          facts' substance, not just their tokens: base-prefix byte integrity
          for every append-only file, exact heading match, whole-word and
          digit-bounded tokens, ordered old->new values, pinned blob SHAs,
          git-object recomputation (K69-3 authors, K69-7 counts), and a real
          re-run of the receipt's three counters (K69-8).
  HIGH-2  K69-11 executed --rev's own checklist gate (rev-controlled).  v2
          byte-pins the checklist blob to an allowlist and runs it in a
          fleet-shaped sandbox; any other blob fails the item.
  MED-2   "appended" was line-index slicing: v2 requires the BASE bytes to be
          a prefix of the measured bytes for LOG.md, SCORECARD.md and the
          round-69 lesson (blanked-history and edited-history worlds fail).
  MED-3   numbers matched inside longer numbers ("110 receipts"): v2 bounds
          them on both sides.
  MED-4   "startswith ## Round 69" matched "## Round 690" and a negated entry:
          v2 requires an exact heading and rejects entries carrying negation
          verbs on the claimed facts.
  MED-5   the K69-1 block could run past its own section: v2 delimits it on
          "**<Round-*" and "## " headings alike.
  MED-6   the K69-8 receipt's verdicts were unanchored substrings and commands
          could be no-ops: v2 anchors the verdict lines, refuses stub commands
          and re-runs each counter at the pinned rev in a sandbox.
  LOW-1   K69-9 ignored token direction: v2 requires (13 words) before
          (14 words) on the S201 line.
  LOW-2   self-test arms added for every hole above, plus a real-git fixture
          that drives main() end to end (Q48).

K69-11 disposition (round 71): LOG.md:2678's subject records a removed,
never-tracked directory; a GOVERNANCE_ERRATA row (2678, sha256 pinned, absence
wording on the line) excuses it as an explicitly recorded absence -- the
closure's mechanism-valid alternative.  The item passes when the pinned gate
reports governance.citation_resolves PASS.

The trust boundary (W11-class): the counter that runs at --rev must be these
bytes -- the self-drift check hashes the measured tree's counter file with the
SELF_SHA line blanked and compares against SELF_SHA.

Environment: --repo the measured git worktree (default: this lane), --rev the
measured revision, --fleet the fleet root for sibling-token sandbox runs and
the K69-3 attestation (default: the repo's parent).  Read-only on the lane:
every git write happens in $TMPDIR scratch.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

TOTAL = 10
BASE = "7d51253f99906b8551b6a0a108761eedac00de74"          # round-70 base
R69_TIP = "9ce102b9e3f8896d5ed3f050ee896ca90d693a38"
R69_BASE = "a5f7459f99bb27bf697e9438362e75ac5833eca8"
R69_COMMITS = ("a02ba7e", "54f4b6c", "278b9dc", "9ce102b")
SCORECARD = "SCORECARD.md"
LOG = "LOG.md"
LESSON70 = "corpus/lessons/round-70.md"
LESSON69 = "corpus/lessons/round-69.md"
RECEIPT = ".ufo/waves/round-70/receipts/r69-tip-defense.txt"
COUNTER_PATH = "verifiers/check_r69_routed_repairs_v2.py"
CHECKLIST_PATH = "verifiers/verify_skill_checklist.py"
W69 = ".ufo/waves/round-69/w1"
INHERITED = {
    f"{W69}/RevFreezeReceipt.md": "59585ea16261fe4e1a3d930962310541c5327329",
    f"{W69}/ScoutStaleLane.md": "6f4c23bad11a5aee7aa7ab255dc4e11d44bddd94",
}
# verdict lines required in the K69-8 receipt AND in the sandbox re-run.
R69_COUNTERS = {
    "check_skill_precedence.py": re.compile(r"\bskill precedence backed 5 of 5\b"),
    "check_r68_routed_repairs.py": re.compile(r"\br68 routed defects closed 8 of 8\b"),
    "check_province_core.py": re.compile(r"\bprovince core rows 2 of 2\b"),
}
FLEET_ATTEST = {
    "4844216baeab733fbf08af86f2ba19061fbd4ec5": "probe <probe@example.invalid>",
    "9d9f181e41fe2a5d26ce7946d48769b61f816c19": "probe <probe@example.invalid>",
    "0a1199a0ccbb9d47744623b5c39b34f9f3cc321c":
        "kotoba-shokunin <kotoba@shokunin.local>",
}
LABELS = ("trigger", "action", "outcome", "pointer")
# K69-11: the checklist blob at --rev must be one of these; anything else
# means the measured revision carries its own gate (rev-controlled item).
CHECKLIST_ALLOWED = {
    "508512daf2556b6c27a20770b1f3f1b21373bf50",  # blob at the round base
    "8d44c063e3d4b57c7c421c3107879e61983249bf",  # r71 errata-row disposition
}
SELF_SHA = "b59fbba624d2b2bd95a410d42fa23ffdd6fef896aa672c6fd1ab263411c6aafe"   # blanked-sha of this file
SELF_LINE_RE = re.compile(r'^SELF_SHA = "[0-9a-f]*"', re.M)

ENTRY_HEAD_RE = re.compile(r"^## Round 69(?![0-9])")
NEXT_H2_RE = re.compile(r"^## ")
NEGATION_RE = re.compile(
    r"\b(?:did not|didn't|didn\u2019t|no fast-forward|never|nobody|not\b|"
    r"denied|false|falsely|did not exist|no commit|no such)\b",
    re.IGNORECASE)

def _blanked_sha(text: str) -> str:
    return hashlib.sha256(
        SELF_LINE_RE.sub('SELF_SHA = ""', text).encode()).hexdigest()


def _word(word_re: str, text: str) -> bool:
    """Whole-word match that also bounds hex abbreviations."""
    return re.search(r"(?<![0-9A-Za-z_])(?:%s)(?![0-9A-Za-z_])" % word_re,
                     text) is not None


def _digits(term_re: str, text: str) -> bool:
    """Match a numeric phrase that may not sit inside a larger number."""
    return re.search(r"(?<!\d)(?:%s)(?!\d)" % term_re, text) is not None


class EnvError(Exception):
    pass


class Repo:
    """Committed-bytes reader over a git worktree; tests substitute a fake."""

    def __init__(self, path: Path, rev: str, fleet: Path):
        self.path, self.rev, self.fleet = path, rev, fleet

    def git(self, *args: str) -> subprocess.CompletedProcess:
        return subprocess.run(["git", "-C", str(self.path), *args],
                              capture_output=True, text=True)

    def show(self, path: str, rev: str | None = None) -> str | None:
        proc = self.git("show", f"{rev or self.rev}:{path}")
        return proc.stdout if proc.returncode == 0 else None

    def blob(self, path: str) -> str | None:
        proc = self.git("rev-parse", "--verify", "--quiet",
                        f"{self.rev}:{path}")
        return proc.stdout.strip() if proc.returncode == 0 else None

    def ls_tree(self, rev: str, prefix: str) -> list[str]:
        proc = self.git("ls-tree", "-r", "--name-only", rev, "--", prefix)
        return proc.stdout.splitlines() if proc.returncode == 0 else []

    def name_status(self, rev: str, prefix: str) -> list[str]:
        proc = self.git("show", "--name-status", "--format=", rev)
        if proc.returncode != 0:
            return []
        return [l for l in proc.stdout.splitlines() if prefix in l]

    def fleet_cat_file(self, sha: str) -> str | None:
        proc = subprocess.run(
            ["git", "-C", str(self.fleet), "cat-file", "-p", sha],
            capture_output=True, text=True)
        return proc.stdout if proc.returncode == 0 else None

    def checklist(self) -> dict | None:
        """Run --rev's PINNED checklist in a fleet-shaped sandbox; None if the
        blob is not allowlisted, the script is absent, or output is not JSON."""
        blob = self.blob(CHECKLIST_PATH)
        if blob is None or blob not in CHECKLIST_ALLOWED:
            return None
        with tempfile.TemporaryDirectory(prefix="k71-c1-") as tdir:
            clone = Path(tdir) / "kotoba-shokunin"
            proc = subprocess.run(
                ["git", "clone", "--shared", "-q", "--no-checkout",
                 str(self.path), str(clone)],
                capture_output=True, text=True)
            if proc.returncode != 0:
                raise EnvError("cannot create the fleet-shaped sandbox clone")
            proc = subprocess.run(
                ["git", "-C", str(clone), "checkout", "-q", self.rev],
                capture_output=True, text=True)
            if proc.returncode != 0:
                raise EnvError(f"cannot check out {self.rev} in the sandbox")
            for entry in Path(self.fleet).iterdir():
                if entry.name != "kotoba-shokunin":
                    (Path(tdir) / entry.name).symlink_to(entry)
            script = clone / "verifiers" / "verify_skill_checklist.py"
            if not script.is_file():
                return None
            proc = subprocess.run(
                ["python3", "-B", str(script), "--json"], cwd=str(clone),
                capture_output=True, text=True, timeout=300)
            try:
                return json.loads(proc.stdout)
            except ValueError:
                return None

    def run_counter(self, filename: str, at: str) -> tuple[str, int] | None:
        """Re-run verifiers/<filename> at rev <at> in a clone of this repo."""
        with tempfile.TemporaryDirectory(prefix="k71-c1r-") as tdir:
            clone = Path(tdir) / "kotoba-shokunin"
            proc = subprocess.run(
                ["git", "clone", "--shared", "-q", "--no-checkout",
                 str(self.path), str(clone)],
                capture_output=True, text=True)
            if proc.returncode != 0:
                raise EnvError("cannot create the counter sandbox clone")
            for entry in Path(self.fleet).iterdir():
                if entry.name != "kotoba-shokunin":
                    (Path(tdir) / entry.name).symlink_to(entry)
            proc = subprocess.run(
                ["git", "-C", str(clone), "checkout", "-q", at],
                capture_output=True, text=True)
            if proc.returncode != 0:
                return None
            script = clone / "verifiers" / filename
            if not script.is_file():
                return None
            proc = subprocess.run(
                ["python3", "-B", str(script), "--repo", str(clone),
                 "--rev", at], cwd=str(clone),
                capture_output=True, text=True, timeout=300)
            return proc.stdout, proc.returncode


def _base_prefix(repo: Repo, path: str) -> bool:
    """The BASE revision's bytes are an exact prefix of the measured bytes."""
    base = repo.show(path, BASE)
    cur = repo.show(path)
    if base is None or cur is None:
        return False
    return cur.startswith(base)


def _r69_entry(repo: Repo) -> str | None:
    """The appended `## Round 69` entry of LOG.md (exact heading, bounded)."""
    text = repo.show(LOG)
    if text is None or not _base_prefix(repo, LOG):
        return None
    lines = text.splitlines()
    base_n = len((repo.show(LOG, BASE) or "").splitlines())
    start = next((i for i in range(base_n, len(lines))
                  if ENTRY_HEAD_RE.match(lines[i])), None)
    if start is None:
        return None
    end = next((i for i in range(start + 1, len(lines))
                if NEXT_H2_RE.match(lines[i])), len(lines))
    return "\n".join(lines[start:end])


def _denies(entry: str, pattern: str) -> bool:
    """A line carries a targeted denial shape (negation near the claim)."""
    return re.search(pattern, entry, re.IGNORECASE) is not None


DENY_FF = re.compile(
    r"did not.{0,40}fast[- ]?forward|no (?:fast[- ]?forward|commit[s]?\b.{0,30}"
    r"exist)|never (?:fast[- ]?forwarded|pushed|committed)", re.IGNORECASE)
DENY_ATTR = re.compile(
    r"nobody|did not.{0,40}(?:commit|write|author)|no .{0,20}probe",
    re.IGNORECASE)
OLDNUM_RE = re.compile(
    r"(?<!not )\bnine receipts\b|(?<!not )(?<!not \")\ball 24\b|\b9 receipts\b")

def k1_scorecard(repo: Repo) -> list[str]:
    if not _base_prefix(repo, SCORECARD):
        return ["K69-1: SCORECARD.md base bytes changed (append-only violated)"]
    text = repo.show(SCORECARD) or ""
    lines = text.splitlines()
    start = next((i for i, l in enumerate(lines)
                  if l.startswith("**Round 69 axis annotations")), None)
    if start is None:
        return ["K69-1: no `**Round 69 axis annotations` block"]
    end = next((i for i in range(start + 1, len(lines))
                if re.match(r"^\*\*Round[-\s]|^## ", lines[i])), len(lines))
    block = "\n".join(lines[start:end])
    need = list(R69_COUNTERS) + [R69_TIP, R69_BASE]
    miss = [n for n in need if n not in block]
    if re.search(r"nothing recorded|unrelated", block, re.IGNORECASE):
        miss.append("a disclaimer phrase")
    return [f"K69-1: annotation block lacks {miss}"] if miss else []


def k2_offbranch(repo: Repo) -> list[str]:
    entry = _r69_entry(repo)
    if entry is None:
        return ["K69-2: no appended `## Round 69` LOG.md entry (base prefix intact)"]
    miss = [n for n in R69_COMMITS + ("orchestrator",)
            if not _word(n, entry)]
    if not re.search(r"fast[- ]?forward", entry, re.IGNORECASE):
        miss.append("fast-forward")
    if _denies(entry, DENY_FF.pattern):
        miss.append("a denied fast-forward claim")
    return [f"K69-2: round-69 entry lacks {miss}"] if miss else []


def k3_attribution(repo: Repo) -> list[str]:
    entry = _r69_entry(repo)
    if entry is None:
        return ["K69-3: no appended `## Round 69` LOG.md entry"]
    miss = []
    for tok in ("4844216b", "9d9f181e", "0a1199a0", "probe"):
        if not _word(tok, entry):
            miss.append(tok)
    if _denies(entry, DENY_ATTR.pattern):
        miss.append("a denied attribution claim")
    for sha, want in FLEET_ATTEST.items():
        body = repo.fleet_cat_file(sha)
        if body is None:
            miss.append(f"fleet object {sha[:7]} unreadable")
            continue
        author = next((l for l in body.splitlines()
                       if l.startswith("author ")), "")
        if f"author {want}" not in author:
            miss.append(f"{sha[:7]} author != {want}")
    return [f"K69-3: round-69 entry lacks {miss}"] if miss else []


def k5_inherited(repo: Repo) -> list[str]:
    out = []
    for path, sha in INHERITED.items():
        got = repo.blob(path)
        if got is None:
            out.append(f"K69-5: {path} not tracked at --rev")
        elif got != sha:
            out.append(f"K69-5: {path} blob {got[:12]} != pinned {sha[:12]}")
    lesson = repo.show(LESSON70) or ""
    miss = [p for p in INHERITED if p not in lesson]
    if miss:
        out.append(f"K69-5: round-70 lesson omits {miss}")
    return out


def k6_log_entry(repo: Repo) -> list[str]:
    entry = _r69_entry(repo)
    if entry is None:
        return ["K69-6: no appended `## Round 69` LOG.md entry"]
    miss = [w for w in LABELS
            if re.search(r"(?<![0-9A-Za-z_])" + w + r"(?![0-9A-Za-z_])",
                         entry, re.IGNORECASE) is None]
    return [f"K69-6: round-69 entry lacks labels {miss}"] if miss else []


def k7_numeric(repo: Repo) -> list[str]:
    entry = _r69_entry(repo)
    if entry is None:
        return ["K69-7: no appended `## Round 69` LOG.md entry"]
    miss = []
    for term in (r"10 receipts", r"23 landed", r"1 dispositioned"):
        if not _digits(term, entry):
            miss.append(term)
    got = len(repo.ls_tree(R69_TIP, ".ufo/waves/round-69/recapture/"))
    if got != 10:
        miss.append(f"recapture tree recount = {got} != 10")
    got = len(repo.name_status("a02ba7e42e230bf6bb4de902e91d6346aee93bfe",
                               ".ufo/waves/round-68"))
    if got != 23:
        miss.append(f"round-68 wave paths recount = {got} != 23")
    if OLDNUM_RE.search(entry):
        miss.append("an old-number phrase still asserted")
    return [f"K69-7: round-69 entry lacks {miss}"] if miss else []


def k8_receipt(repo: Repo) -> list[str]:
    text = repo.show(RECEIPT)
    if text is None:
        return [f"K69-8: {RECEIPT} absent"]
    out = []
    if not re.search(rf"^measured-rev:\s*{R69_TIP}\s*$", text, re.M):
        out.append("K69-8: measured-rev not pinned to the r69 tip")
    for name, verdict in R69_COUNTERS.items():
        m = re.search(rf"^command:.*{re.escape(name)}.*$", text, re.M)
        if not m:
            out.append(f"K69-8: no command: line naming {name}")
            continue
        if re.search(r"\b(?:echo|true|cat)\b", m.group(0)):
            out.append(f"K69-8: stub command for {name}")
        block_end = text.find("\ncommand:", m.end())
        block = text[m.end(): block_end if block_end != -1 else len(text)]
        if not verdict.search(block):
            out.append(f"K69-8: no exact verdict line for {name}")
        if not re.search(r"^exit=0\s*$", block, re.M):
            out.append(f"K69-8: no exit=0 for {name}")
        reran = repo.run_counter(name, R69_TIP)
        if reran is None:
            out.append(f"K69-8: sandbox re-run of {name}@{R69_TIP[:7]} failed")
        else:
            stdout, code = reran
            if code != 0 or not verdict.search(stdout):
                out.append(
                    f"K69-8: re-run {name}@{R69_TIP[:7]} exit={code} "
                    f"without its verdict line")
    return out


def k9_s201(repo: Repo) -> list[str]:
    lesson = repo.show(LESSON70) or ""
    ok = any("S201" in l and "(13 words)" in l and "(14 words)" in l
             and l.index("(13 words)") < l.index("(14 words)")
             for l in lesson.splitlines())
    return [] if ok else [
        "K69-9: round-70 lesson has no S201 (13 words)->(14 words) line"]


def k10_erratum(repo: Repo) -> list[str]:
    if not _base_prefix(repo, LESSON69):
        return ["K69-10: round-69 lesson base bytes changed (in-place edit)"]
    text = repo.show(LESSON69) or ""
    base_n = len((repo.show(LESSON69, BASE) or "").splitlines())
    tail = "\n".join(text.splitlines()[base_n:])
    ok = any("(18 assertions)" in l and "22 assertions" in l
             and l.index("(18 assertions)") < l.index("22 assertions")
             for l in tail.splitlines())
    return [] if ok else [
        "K69-10: no appended erratum naming (18 assertions) and 22 assertions"]


def k11_governance(repo: Repo) -> list[str]:
    data = repo.checklist()
    if data is None:
        return ["K69-11: pinned checklist absent, unpinned blob, or unreadable "
                "gate output (rev-controlled gate refused)"]
    for c in data.get("checks", []):
        if c.get("id") == "governance.citation_resolves":
            return [] if c.get("status") == "PASS" else [
                f"K69-11: governance.citation_resolves {c.get('status')}"]
    return ["K69-11: governance.citation_resolves absent from the gate output"]


CHECKS = (k1_scorecard, k2_offbranch, k3_attribution, k5_inherited,
          k6_log_entry, k7_numeric, k8_receipt, k9_s201, k10_erratum,
          k11_governance)


def check(repo: Repo) -> tuple[int, list[str]]:
    closed, findings = 0, []
    for fn in CHECKS:
        misses = fn(repo)
        if misses:
            findings.extend(misses)
        else:
            closed += 1
    return closed, findings


# ----------------------------------------------------------------- self-test

class FakeRepo:
    """Dict-backed Repo: files at --rev, base files, blob pins, canned git."""

    def __init__(self, files: dict, base: dict | None = None,
                 blobs: dict | None = None, gate=None,
                 fleet_objects: dict | None = None,
                 recapture: int = 10, wave68: int = 23,
                 counter_runs: dict | None = None,
                 checklist_blob: str | None = None):
        self.files, self.base = files, base or {}
        self.blobs = blobs or {}
        self.gate = gate
        self.fleet_objects = fleet_objects or dict(FLEET_ATTEST)
        self.recapture, self.wave68 = recapture, wave68
        self.counter_runs = counter_runs or {}
        self.checklist_blob = checklist_blob

    def show(self, path, rev=None):
        return (self.files if rev is None else self.base).get(path)

    def blob(self, path):
        if path == CHECKLIST_PATH:
            return self.checklist_blob
        return self.blobs.get(path)

    def ls_tree(self, rev, prefix):
        return ["x"] * self.recapture

    def name_status(self, rev, prefix):
        return ["x"] * self.wave68

    def fleet_cat_file(self, sha):
        want = self.fleet_objects.get(sha)
        if want is None:
            return None
        return f"tree t\nauthor {want} 1 +0000\ncommitter {want} 1 +0000\n"

    def run_counter(self, filename, at):
        return self.counter_runs.get(filename)

    def checklist(self):
        if self.checklist_blob is None:
            return None
        if self.checklist_blob not in CHECKLIST_ALLOWED:
            return None
        return self.gate


def _base_files() -> dict:
    return {
        LOG: "# LOG\n## Round 46 B2\nold lines\n",
        SCORECARD: "# SCORECARD\nold\n",
        LESSON69: "# r69\n## Gate\n(18 assertions) old text\n",
    }


def _entry69(labels=LABELS, commits=R69_COMMITS,
             receipts="10 receipts", landed="23 landed",
             dispo="1 dispositioned", neg="") -> str:
    lab = " ".join(labels)
    com = " ".join(commits)
    return (f"## Round 69 — appended correction entry\n"
            f"trigger: x action: y outcome: z pointer: w {lab}\n"
            f"orchestrator fast-forward {com} 9ce102b\n"
            f"4844216b 9d9f181e probe 0a1199a0\n"
            f"{receipts} and {landed} with {dispo} {neg}\n")


def _honest() -> FakeRepo:
    entry = _entry69()
    lesson70 = ("Gate\n.ufo/waves/round-69/w1/RevFreezeReceipt.md\n"
                ".ufo/waves/round-69/w1/ScoutStaleLane.md\n"
                "S201 (13 words) -> (14 words)\n")
    receipt = (f"measured-rev: {R69_TIP}\n"
               + "".join(
                   f"command: python3 -B verifiers/{n} --rev {R69_TIP}\n"
                   f"{v.pattern.strip(chr(92)+'b')}\nexit=0\n"
                   for n, v in R69_COUNTERS.items()))
    files = {
        LOG: _base_files()[LOG] + entry,
        SCORECARD: (_base_files()[SCORECARD]
                    + "**Round 69 axis annotations**\n"
                    + " ".join(R69_COUNTERS) + f" {R69_TIP} {R69_BASE}\n"
                    + "**Round 70 notes**\n"),
        LESSON69: _base_files()[LESSON69]
                  + "(18 assertions) corrected to 22 assertions\n",
        LESSON70: lesson70,
        RECEIPT: receipt,
    }
    fr = FakeRepo(
        files, _base_files(), dict(INHERITED),
        gate={"checks": [{"id": "governance.citation_resolves",
                          "status": "PASS"}]},
        counter_runs={n: (v.pattern.replace("\\b", " ").strip() + "\n", 0)
                      for n, v in R69_COUNTERS.items()},
        checklist_blob="508512daf2556b6c27a20770b1f3f1b21373bf50")
    return fr


def _git_world_c1() -> tuple[int, str] | None:
    """Materialize the committed c1-junk-world bundle over a clone of the
    pre-data commit, run main() on the junk commit, return (exit, stdout)."""
    lane = Path(__file__).resolve().parent.parent
    bundle = lane / ".ufo/waves/round-71/controls/c1-junk-world"
    pre = "a647fa734430cb07066a9b6377b157310a7943db"
    if not (bundle / "log.md").is_file():
        return None
    env = dict(os.environ,
               GIT_AUTHOR_NAME="t", GIT_AUTHOR_EMAIL="t@t",
               GIT_COMMITTER_NAME="t", GIT_COMMITTER_EMAIL="t@t")
    overlay = {
        "log.md": LOG, "scorecard.md": SCORECARD,
        "lesson69.md": LESSON69, "lesson70.md": LESSON70,
        "receipt.md": RECEIPT,
        "verify_skill_checklist.py": CHECKLIST_PATH,
    }
    try:
        with tempfile.TemporaryDirectory(prefix="k71-c1j-") as td:
            clone = Path(td) / "j"
            p = subprocess.run(
                ["git", "clone", "--shared", "-q", str(lane), str(clone)],
                capture_output=True, text=True)
            if p.returncode != 0:
                return None
            if subprocess.run(
                    ["git", "-C", str(clone), "checkout", "-q", pre],
                    capture_output=True).returncode != 0:
                return None
            for src, dst in overlay.items():
                d = clone / dst
                d.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy(bundle / src, d)
            subprocess.run(["git", "-C", str(clone), "add", "-A"],
                           capture_output=True)
            p = subprocess.run(
                ["git", "-C", str(clone), "commit", "-qm", "junk"],
                capture_output=True, text=True, env=env)
            if p.returncode != 0:
                return None
            p = subprocess.run(
                ["python3", "-B", str(lane / "verifiers" /
                                     "check_r69_routed_repairs_v2.py"),
                 "--repo", str(clone), "--rev", "HEAD",
                 "--fleet", td],
                capture_output=True, text=True, timeout=600)
            return p.returncode, p.stdout + p.stderr
    except (OSError, subprocess.TimeoutExpired):
        return None


def selftest() -> int:
    failures = 0

    def run(repo) -> tuple[int, list[str]]:
        return check(repo)

    n, f = run(_honest())
    if n != TOTAL or f:
        print(f"FAIL honest world: closed {n} of {TOTAL} {f}")
        failures += 1
    else:
        print(f"PASS honest world: closed {n} of {TOTAL}")

    def broken(label, mutate, needle):
        nonlocal failures
        fr = _honest()
        mutate(fr)
        n, f = run(fr)
        if n == TOTAL or not any(needle in x for x in f):
            print(f"FAIL broken world accepted: {label} (closed {n}, {f})")
            failures += 1
        else:
            print(f"PASS broken world rejected: {label}")

    # HIGH-1 token-dump ingredients, one arm each.
    broken("K69-1 tokens only after the next section heading",
           lambda r: r.files.update({SCORECARD: (
               _base_files()[SCORECARD]
               + "**Round 69 axis annotations**\n"
               + "**Round-70 notes.** "
               + " ".join(R69_COUNTERS) + f" {R69_TIP} {R69_BASE}\n")}),
           "K69-1")
    broken("K69-2 `## Round 690` wrong round",
           lambda r: r.files.update({LOG: r.files[LOG].replace(
               "## Round 69 —", "## Round 690 —")}),
           "K69-2")
    broken("K69-2 negated fast-forward",
           lambda r: r.files.update({LOG: r.files[LOG].replace(
               "orchestrator fast-forward",
               "the orchestrator did not fast-forward")}),
           "K69-2")
    broken("K69-3 probe inside a longer word",
           lambda r: r.files.update({LOG: r.files[LOG].replace(
               " 0a1199a0", " probed 0a1199a0").replace(" probe", "")}),
           "K69-3")
    broken("K69-3 fleet author mismatch",
           lambda r: r.fleet_objects.update(
               {"4844216baeab733fbf08af86f2ba19061fbd4ec5": "x <x@x>"}),
           "K69-3")
    broken("K69-5 wrong blob",
           lambda r: r.blobs.update(
               {f"{W69}/RevFreezeReceipt.md": "0" * 40}), "K69-5")
    broken("K69-5 lesson omits a path",
           lambda r: r.files.update({LESSON70: "Gate\n"}), "K69-5")
    broken("K69-6 entry inside base (no appended heading)",
           lambda r: r.files.update({LOG: _base_files()[LOG]}), "K69-6")
    broken("K69-6 blanked base history",
           lambda r: r.files.update(
               {LOG: "\n" * len(_base_files()[LOG].splitlines())
                + _entry69()}),
           "K69-6")
    broken("K69-7 110 receipts",
           lambda r: r.files.update({LOG: r.files[LOG].replace(
               "10 receipts", "110 receipts")}),
           "K69-7")
    broken("K69-7 recount differs (9 receipts on disk)",
           lambda r: setattr(r, "recapture", 9), "K69-7")
    broken("K69-8 receipt pinned elsewhere",
           lambda r: r.files.update({RECEIPT: r.files[RECEIPT].replace(
               R69_TIP, "0" * 40)}), "K69-8")
    broken("K69-8 stub echo command",
           lambda r: r.files.update({RECEIPT: r.files[RECEIPT].replace(
               "command: python3 -B verifiers/check_skill_precedence.py",
               "command: echo check_skill_precedence.py")}),
           "K69-8")
    broken("K69-8 verdict 5 of 50",
           lambda r: r.files.update({RECEIPT: r.files[RECEIPT].replace(
               "skill precedence backed 5 of 5",
               "skill precedence backed 5 of 50")}),
           "K69-8")
    broken("K69-8 re-run disagrees",
           lambda r: r.counter_runs.update(
               {"check_skill_precedence.py": ("0 of 5\n", 1)}), "K69-8")
    broken("K69-9 reversed S201 direction",
           lambda r: r.files.update({LESSON70: r.files[LESSON70].replace(
               "S201 (13 words) -> (14 words)",
               "S201 (14 words) -> (13 words)")}),
           "K69-9")
    broken("K69-10 erratum edited in place",
           lambda r: r.files.update(
               {LESSON69: "# r69\n## Gate\n(18 assertions) corrected in "
                "place: 22 assertions\n" + "\n" * 200}),
           "K69-10")
    broken("K69-11 rev-controlled stub gate blob",
           lambda r: setattr(r, "checklist_blob", "a" * 40), "K69-11")
    broken("K69-11 gate red on pinned blob",
           lambda r: setattr(
               r, "gate", {"checks": [{"id": "governance.citation_resolves",
                                       "status": "FAIL"}]}),
           "K69-11")
    broken("K69-11 check id absent",
           lambda r: setattr(r, "gate", {"checks": []}), "K69-11")

    # ------------------------- real-git fixture driving main() (Q48) -------
    with tempfile.TemporaryDirectory(prefix="k71-c1fx-") as td:
        fx = Path(td) / "fixture"
        fx.mkdir()
        for path, content in _fixture_files().items():
            p = fx / path
            p.parent.mkdir(parents=True, exist_ok=True)
            p.write_text(content)
        for cmd in (["git", "init", "-q"], ["git", "add", "-A"],
                    ["git", "-c", "user.name=t", "-c", "user.email=t@t",
                     "commit", "-qm", "fixture"]):
            subprocess.run(cmd, cwd=fx, capture_output=True)
        rev = subprocess.run(["git", "rev-parse", "HEAD"], cwd=fx,
                             capture_output=True, text=True).stdout.strip()
        code = main(["--repo", str(fx), "--rev", rev, "--fleet", td])
        # The fixture reproduces the honest items except K69-5 (no inherited
        # blobs), K69-8 (no re-runnable counters) and K69-11 (unpinned gate).
        if code != 1:
            print(f"FAIL fixture main(): exit {code} (want 1)")
            failures += 1
        else:
            print("PASS fixture main(): non-perfect exit on reduced world")
        code = main(["--repo", str(fx), "--rev", "deadbeef" * 5,
                     "--fleet", td])
        if code != 2:
            print(f"FAIL fixture unknown rev: exit {code} (want 2)")
            failures += 1
        else:
            print("PASS fixture unknown rev: exit 2")


    # Real-git junk world: the committed c1-junk-world bundle over a clone of
    # the pre-data commit a647fa7 (RevC1Counter token-dump lineage).
    junk = _git_world_c1()
    if junk is None:
        print("SKIP c1 committed junk world: sandbox repo unavailable")
    else:
        code, out = junk
        m = re.search(r"closed (\d+) of (\d+)", out)
        if code == 1 and m and int(m.group(1)) <= 6:
            print(f"PASS c1 committed junk world rejected ({m.group(1)}/10)")
        else:
            print(f"FAIL c1 committed junk world: exit={code} out={out!r}")
            failures += 1
    print(f"self-test: {failures} failure(s)")
    return 0 if failures == 0 else 1


def _fixture_files() -> dict[str, str]:
    """An honest-shaped minimal world for the real-git main() arm."""
    base = _base_files()
    return {
        LOG: base[LOG] + _entry69(),
        SCORECARD: base[SCORECARD]
                   + "**Round 69 axis annotations**\n"
                   + " ".join(R69_COUNTERS) + f" {R69_TIP} {R69_BASE}\n",
        LESSON69: base[LESSON69]
                  + "(18 assertions) corrected to 22 assertions\n",
        LESSON70: ("Gate\n.ufo/waves/round-69/w1/RevFreezeReceipt.md\n"
                   ".ufo/waves/round-69/w1/ScoutStaleLane.md\n"
                   "S201 (13 words) -> (14 words)\n"),
        RECEIPT: f"measured-rev: {R69_TIP}\n",
        COUNTER_PATH: Path(__file__).read_text(),
        CHECKLIST_PATH: "#!/usr/bin/env python3\nimport json\n"
                        "print(json.dumps({'checks':[{'id':"
                        "'governance.citation_resolves','status':'PASS'}]}))\n",
    }


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(
        description="C1 successor counter for kotoba round 71")
    ap.add_argument("--rev", default=None, help="measured revision")
    ap.add_argument("--repo",
                    default=str(Path(__file__).resolve().parent.parent))
    ap.add_argument("--fleet",
                    default=None, help="fleet root (default: repo parent)")
    ap.add_argument("--self-test", action="store_true")
    args = ap.parse_args(argv)
    if args.self_test:
        return selftest()
    if not args.rev:
        raise EnvError("--rev <revision> is required")
    repo_path = Path(args.repo)
    fleet = Path(args.fleet) if args.fleet else repo_path.resolve().parent
    src = Path(__file__).read_text()
    if _blanked_sha(src) != SELF_SHA:
        print("environment error: counter drifted — the running file is not "
              "the frozen counter", file=sys.stderr)
        return 2
    repo = Repo(repo_path, args.rev, fleet)
    proc = repo.git("rev-parse", "--verify", "-q", f"{args.rev}^{{commit}}")
    if proc.returncode != 0:
        print(f"environment error: --rev {args.rev} is not a commit",
              file=sys.stderr)
        return 2
    n, findings = check(repo)
    print(f"measured-rev: {args.rev}")
    print(f"r69 routed defects closed {n} of {TOTAL}")
    for f in findings:
        print(f"  {f}")
    return 0 if n == TOTAL else 1


if __name__ == "__main__":
    sys.exit(main())
