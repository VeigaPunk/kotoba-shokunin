#!/usr/bin/env python3
"""check_r68_routed_repairs.py — C2 counter for kotoba round 69.

Contract
--------
`python3 -B verifiers/check_r68_routed_repairs.py --rev <full-sha>` prints
    measured-rev: <full-sha>
    r68 routed defects closed N of 8
and exits 0 when N == 8, nonzero otherwise.  At the pinned base (the round-68 closure tip
`a5f7459f99bb27bf697e9438362e75ac5833eca8`) it must print `r68 routed defects closed 0 of 8`
and exit 1.

The eight routed defects come from the round-68 closure's spot-check
(`corpus/lessons/round-68-verifier-spotcheck.md`, written by the hyaku closure, never edited by
the lane).  Every check reads COMMITTED bytes at `--rev`; nothing runs a git write in the lane
(each measurement that executes code does so in a `git clone --shared` sandbox under /tmp).

  D1  R68-1  each of the nine named r68 receipts has a round-69 re-capture under
             `.ufo/waves/round-69/recapture/` that prints `measured-rev: <40-hex>` (a commit
             that is an ancestor of --rev), an `exit=<n>` line and its expected verdict line;
             the base re-capture names the r68 base `e94ae32a…` itself.
  D2  R68-2  the re-captured `C2-routed-selftest.txt` shows `self-test: 0 failure(s) over 6
             assertions` with `exit=0` and carries no `unrecognized arguments` line.
  D3  R68-3  `verifiers/check_r67_routed_repairs.py` at --rev runs no `git checkout`, and — run
             from a sandbox — classifies the r68 base (whose records file is missing) as a
             content verdict (`r67 routed defects closed 0 of 4`, exit 1) while still reading
             the r68 tip as `4 of 4`, exit 0; the base-control receipt is committed.
  D4  R68-4  `corpus/lessons/round-69.md` § Gate names the removed bytes: a line naming S200 and
             `<code>`, and a line naming S202 and `**`.
  D5  R68-5  `corpus/SOURCES.md` carries a mined row opened 2026-10-25 whose `teaches` opens
             `supersedes S201 —` and whose anchor quotes `All three skill tools require approval
             by default.`; the round-68 entry names that row's id.
  D6  R68-6  `corpus/lessons/round-69.md` § Mistakes carries a row naming R68-6 and S201, and
             `corpus/QUALITY.md` carries a criterion row whose evidence cites `round-69.md`.
  D7  R68-7  each of the 24 uncommitted round-68 wave paths is committed at --rev (the ten
             modified logs with a blob that differs from the base's), or is named on a
             `disposition: removed <path>` line of the round-69 lesson and not tracked.
  D8  R68-8  `corpus/README.md` indexes `lessons/round-68-verifier-spotcheck.md` and every
             re-recorded `verifiers/corpus-baseline.json` expectation equals the corpus gate's
             own `--no-baseline --json` measurement of --rev (run in a sandbox checkout).

Trust boundary (QUALITY Q33, Q58): D4 and D6 are presence floors over the lane's own records —
they count named items, not substance, and are disclosed as such.  D1–D3, D5, D7 and D8 recompute
from bytes or from a sandbox run.  The verdict also rests on the base control and the self-test.

Exit codes: 0 all eight closed · 1 not all closed · 2 usage/environment error.
"""
from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
import tempfile
from pathlib import Path

TOTAL = 8
R68_BASE = "e94ae32a5cd8dc3ee8e2d247816784bec2750cc0"
R68_TIP = "2cf0d99a6d5a3e1cb0b73e3b71cb495fd1eadc6f"
R69_BASE = "a5f7459f99bb27bf697e9438362e75ac5833eca8"
RECAP = ".ufo/waves/round-69/recapture"
LESSON = "corpus/lessons/round-69.md"
QUALITY = "corpus/QUALITY.md"
SOURCES = "corpus/SOURCES.md"
README = "corpus/README.md"
BASELINE = "verifiers/corpus-baseline.json"
R67_COUNTER = "verifiers/check_r67_routed_repairs.py"
R68_ENTRY = "corpus/knowledge/client-trust-gates-round68.md"
SPOTCHECK_TOKEN = "`lessons/round-68-verifier-spotcheck.md`"
APPROVAL = "All three skill tools require approval by default."

RECEIPTS = {
    "C1-base.txt": [r"client trust gates backed 0 of 5"],
    "C1-after.txt": [r"client trust gates backed 5 of 5"],
    "C1-fetch.txt": [r"live quotes found \d of 5"],
    "C1-selftest.txt": [r"self-test: 0 failure\(s\) over 12 assertions"],
    "C2-integrity-after.txt": [r"9/9 checks pass"],
    "C2-routed-measure.txt": [r"r67 routed defects closed 4 of 4"],
    "C2-routed-selftest.txt": [r"self-test: 0 failure\(s\) over 6 assertions"],
    "noharm-at-tip.txt": [r"gate registry rows conformant \d+ of \d+", r"9/9 checks pass"],
    "gate-registry.txt": [r"gate registry rows conformant 46 of 46 lane verifiers; phantom 0"],
}
R67_BASE_RECEIPT = f"{RECAP}/r67-repairs-base.txt"

W = ".ufo/waves/round-68/w1"
MODIFIED = [f"{W}/drafts/check_client_trust_gates.py"] + [f"{W}/logs/{n}.log" for n in (
    "CriticC1Predicate", "CriticC2Predicate", "ExecC1CounterTest", "ExecC1Fetch", "ExecR67Repairs",
    "MutC1Counter", "MutR67Repairs", "ReviewC1Entry", "ScribeC2Index")]
UNTRACKED = [f"{W}/{n}.md" for n in (
    "CriticC2Predicate", "ExecC1CounterTest", "ExecC1Fetch", "ExecR67Repairs", "MutC1Counter",
    "MutR67Repairs", "ScribeC2Index")] + [
    f"{W}/controls/c2falsify-clone/", f"{W}/controls/c2falsify2.py",
    f"{W}/drafts/check_r67_routed_repairs.py", f"{W}/drafts/coverage-row.md",
    f"{W}/drafts/fetch-arm-execC1Fetch.py", f"{W}/drafts/r68-mistakes-M108-M110.md",
    f"{W}/seat-results.json"]
R68_PATHS = MODIFIED + UNTRACKED

SHA_RE = re.compile(r"^measured-rev:\s*([0-9a-f]{40})\s*$", re.M)
EXIT_RE = re.compile(r"^exit=(\d+)\s*$", re.M)


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

    def tracked(self, path: str, rev: str | None = None) -> list[str]:
        proc = self.git("ls-tree", "-r", "--name-only", rev or self.rev, "--", path.rstrip("/"))
        return [l for l in proc.stdout.splitlines() if l]

    def blob(self, path: str, rev: str) -> str | None:
        proc = self.git("rev-parse", "--verify", "--quiet", f"{rev}:{path}")
        return proc.stdout.strip() if proc.returncode == 0 else None

    def is_ancestor(self, sha: str) -> bool:
        return self.git("merge-base", "--is-ancestor", sha, self.rev).returncode == 0

    def run_r67_counter(self, at: str) -> tuple[int, str]:
        """Run --rev's r67 counter from a sandbox clone against revision <at>."""
        src = self.show(R67_COUNTER)
        if src is None:
            return 2, ""
        with tempfile.TemporaryDirectory(prefix="k69-r67run-") as tmp:
            clone = Path(tmp) / "clone"
            proc = subprocess.run(["git", "clone", "--shared", "-q", "--no-checkout", str(self.path), str(clone)],
                                  capture_output=True, text=True)
            if proc.returncode != 0:
                raise EnvError("cannot create the sandbox clone")
            subprocess.run(["git", "-C", str(clone), "checkout", "-q", self.rev], capture_output=True, text=True)
            script = Path(tmp) / "check_r67_routed_repairs.py"
            script.write_text(src, encoding="utf-8")
            proc = subprocess.run(["python3", "-B", str(script), "--repo", str(clone), "--rev", at],
                                  capture_output=True, text=True, timeout=600)
            return proc.returncode, proc.stdout

    def gate_observed(self) -> dict | None:
        with tempfile.TemporaryDirectory(prefix="k69-gate-") as tmp:
            clone = Path(tmp) / "clone"
            proc = subprocess.run(["git", "clone", "--shared", "-q", "--no-checkout", str(self.path), str(clone)],
                                  capture_output=True, text=True)
            if proc.returncode != 0:
                raise EnvError("cannot create the sandbox clone")
            proc = subprocess.run(["git", "-C", str(clone), "checkout", "-q", self.rev], capture_output=True, text=True)
            if proc.returncode != 0:
                raise EnvError(f"cannot check out {self.rev} in the sandbox")
            proc = subprocess.run(
                ["python3", "-B", str(clone / "verifiers" / "verify_corpus_integrity.py"),
                 "--repo", str(clone), "--no-baseline", "--json"],
                capture_output=True, text=True, timeout=600)
            if proc.returncode not in (0, 1):
                return None
            return json.loads(proc.stdout)["observed"]["corpus"]


def _section(text: str, heading: str) -> str:
    m = re.search(rf"(?ms)^## {re.escape(heading)}\b.*?(?=^## |\Z)", text)
    return m.group(0) if m else ""


def _cells(line: str) -> list[str]:
    s = line.strip()
    if not s.startswith("|"):
        return []
    cells = [c.strip() for c in s[1:].split("|")]
    if cells and cells[-1] == "":
        cells.pop()
    return cells


def d1_receipts(repo: Repo) -> list[str]:
    out = []
    for name, patterns in RECEIPTS.items():
        text = repo.show(f"{RECAP}/{name}")
        if text is None:
            out.append(f"D1: {RECAP}/{name} is not committed")
            continue
        m = SHA_RE.search(text)
        if not m:
            out.append(f"D1: {name} names no `measured-rev: <40-hex>` line")
            continue
        if not repo.is_ancestor(m.group(1)):
            out.append(f"D1: {name} measured-rev {m.group(1)} is not an ancestor of the measured revision")
            continue
        if name == "C1-base.txt" and m.group(1) != R68_BASE:
            out.append(f"D1: C1-base.txt measured {m.group(1)}, not the r68 base {R68_BASE}")
            continue
        if not EXIT_RE.search(text):
            out.append(f"D1: {name} records no `exit=<n>` line")
            continue
        missing = [p for p in patterns if not re.search(p, text)]
        if missing:
            out.append(f"D1: {name} lacks its verdict line(s) {missing}")
    return out


def d2_selftest(repo: Repo) -> list[str]:
    text = repo.show(f"{RECAP}/C2-routed-selftest.txt")
    if text is None:
        return ["D2: the re-captured C2-routed-selftest.txt is not committed"]
    if "unrecognized arguments" in text:
        return ["D2: the re-capture still records `unrecognized arguments`"]
    m = EXIT_RE.search(text)
    if not SHA_RE.search(text) or not m or m.group(1) != "0" or \
            not re.search(RECEIPTS["C2-routed-selftest.txt"][0], text):
        return ["D2: the re-capture lacks measured-rev, exit=0 or `0 failure(s) over 6 assertions`"]
    return []


def d3_r67_counter(repo: Repo) -> list[str]:
    src = repo.show(R67_COUNTER)
    if src is None:
        return [f"D3: {R67_COUNTER} is absent at the measured revision"]
    if re.search(r"[\"']checkout[\"']", src):
        return [f"D3: {R67_COUNTER} still runs `git checkout` (a git write in the lane)"]
    receipt = repo.show(R67_BASE_RECEIPT)
    if receipt is None or R68_BASE not in receipt or "r67 routed defects closed 0 of 4" not in receipt:
        return [f"D3: the base-control receipt {R67_BASE_RECEIPT} is missing or does not show 0 of 4 at {R68_BASE}"]
    code, out = repo.run_r67_counter(R68_BASE)
    if code != 1 or "r67 routed defects closed 0 of 4" not in out:
        return [f"D3: at the r68 base the counter exits {code}, expected 1 with `closed 0 of 4`"]
    code, out = repo.run_r67_counter(R68_TIP)
    if code != 0 or "r67 routed defects closed 4 of 4" not in out:
        return [f"D3: at the r68 tip the counter exits {code}, expected 0 with `closed 4 of 4`"]
    return []


def d4_q42(repo: Repo) -> list[str]:
    gate = _section(repo.show(LESSON) or "", "Gate")
    lines = gate.splitlines()
    ok200 = any("S200" in l and "<code>" in l for l in lines)
    ok202 = any("S202" in l and "**" in l for l in lines)
    if ok200 and ok202:
        return []
    return [f"D4: {LESSON} § Gate lacks the Q42 shaping note for " +
            " and ".join(s for s, ok in (("S200 `<code>`", ok200), ("S202 `**`", ok202)) if not ok)]


def d5_supersede(repo: Repo) -> list[str]:
    text = repo.show(SOURCES) or ""
    for line in text.splitlines():
        cells = _cells(line)
        if len(cells) != 11 or not re.fullmatch(r"S\d{3,}", cells[0]):
            continue
        if cells[6].startswith("supersedes S201 —") and APPROVAL in cells[5] \
                and cells[7] == "mined" and cells[8] == "2026-10-25":
            entry = repo.show(R68_ENTRY) or ""
            if re.search(rf"\b{cells[0]}\b", entry):
                return []
            return [f"D5: {cells[0]} supersedes S201 but {R68_ENTRY} does not name it"]
    return ["D5: no mined row opened 2026-10-25 supersedes S201 with the approval sentence in its anchor"]


def d6_mistake(repo: Repo) -> list[str]:
    mistakes = _section(repo.show(LESSON) or "", "Mistakes")
    row = any("R68-6" in l and "S201" in l for l in mistakes.splitlines())
    quality = repo.show(QUALITY) or ""
    crit = any(re.match(r"^\| Q\d+ \|", l) and "round-69.md" in l for l in quality.splitlines())
    out = []
    if not row:
        out.append(f"D6: {LESSON} § Mistakes has no row naming R68-6 and S201")
    if not crit:
        out.append(f"D6: {QUALITY} has no criterion row citing round-69.md")
    return out


def d7_wave_paths(repo: Repo) -> list[str]:
    lesson = repo.show(LESSON) or ""
    removed = set(re.findall(r"disposition: removed `?([^`\s]+)`?", lesson))
    out = []
    for path in R68_PATHS:
        files = repo.tracked(path)
        if path in removed:
            if files:
                out.append(f"D7: {path} is dispositioned as removed but still tracked")
            continue
        if not files:
            out.append(f"D7: {path} is neither committed nor dispositioned")
            continue
        if path in MODIFIED and repo.blob(path, repo.rev) == repo.blob(path, R69_BASE):
            out.append(f"D7: {path} carries the base blob; its uncommitted modification never landed")
    return out


def d8_index_baseline(repo: Repo) -> list[str]:
    readme = repo.show(README) or ""
    if not any(len(_cells(l)) >= 2 and _cells(l)[1] == SPOTCHECK_TOKEN for l in readme.splitlines()):
        return [f"D8: {README} has no coverage-map row for {SPOTCHECK_TOKEN}"]
    try:
        checks = json.loads(repo.show(BASELINE) or "{}").get("checks", {})
    except json.JSONDecodeError:
        return [f"D8: {BASELINE} is not valid JSON"]
    obs = repo.gate_observed()
    if obs is None:
        return ["D8: the corpus gate could not run in the sandbox"]
    out = []
    for key, field in (("corpus.index.tracked_files", "tracked_files"),
                       ("corpus.index.unindexed", "unindexed"),
                       ("corpus.pointers.report_total", "report_total"),
                       ("corpus.pointers.commit_total", "commit_total")):
        if checks.get(key, {}).get("expect") != obs.get(field):
            out.append(f"D8: baseline {key} expects {checks.get(key, {}).get('expect')!r}, "
                       f"the gate measures {obs.get(field)!r}")
    return out


CHECKS = (d1_receipts, d2_selftest, d3_r67_counter, d4_q42, d5_supersede, d6_mistake,
          d7_wave_paths, d8_index_baseline)


def check(repo: Repo) -> tuple[int, list[str]]:
    closed, findings = 0, []
    for fn in CHECKS:
        f = fn(repo)
        if f:
            findings.extend(f)
        else:
            closed += 1
    return closed, findings


class FakeRepo(Repo):
    """Dict-backed committed bytes for the self-test; no git, no subprocess."""

    def __init__(self, files: dict[str, str], tracked: set[str], base_blobs: dict[str, str],
                 r67: dict[str, tuple[int, str]], gate: dict):
        super().__init__(Path("/nonexistent"), "f" * 40)
        self.files, self.tracked_set, self.base_blobs, self.r67, self.gate = files, tracked, base_blobs, r67, gate

    def show(self, path, rev=None):
        return self.files.get(path)

    def tracked(self, path, rev=None):
        p = path.rstrip("/")
        return [t for t in self.tracked_set if t == p or t.startswith(p + "/")]

    def blob(self, path, rev):
        return self.base_blobs.get(path) if rev == R69_BASE else "new-" + path

    def is_ancestor(self, sha):
        return sha != "0" * 40

    def run_r67_counter(self, at):
        return self.r67[at]

    def gate_observed(self):
        return self.gate


def _honest() -> dict:
    sha = R68_BASE
    files = {}
    for name, patterns in RECEIPTS.items():
        verdict = {
            "C1-fetch.txt": "live quotes found 5 of 5",
            "noharm-at-tip.txt": "gate registry rows conformant 46 of 46 lane verifiers; phantom 0\n9/9 checks pass",
        }.get(name, patterns[0].replace("\\(", "(").replace("\\)", ")"))
        files[f"{RECAP}/{name}"] = f"measured-rev: {sha}\n{verdict}\nexit=0\n"
    files[R67_BASE_RECEIPT] = f"measured-rev: {R68_BASE}\nr67 routed defects closed 0 of 4\nexit=1\n"
    files[R67_COUNTER] = "proc = subprocess.run(['git', 'clone', '--shared'])\n"
    files[LESSON] = ("## Gate\n- S200: the quote drops `<code>` tags.\n- S202: the quote drops `**` bold.\n"
                     "## Mistakes\n- M111 R68-6: the S201 refusal reason was wrong.\n"
                     f"disposition: removed `{W}/controls/c2falsify-clone/`\n")
    files[QUALITY] = "| Q62 | rule | scope | M111 (`corpus/lessons/round-69.md`) | — |\n"
    files[SOURCES] = (f"| S208 | MS | docs | B | scope | quote \"{APPROVAL}\" | supersedes S201 — x | mined | "
                      "2026-10-25 | 90d | corpus/knowledge/client-trust-gates-round68.md |\n")
    files[R68_ENTRY] = "Amendment: the approval clause rests on S208.\n"
    files[README] = f"| Round-68 spot-check | {SPOTCHECK_TOKEN} | x |\n"
    files[BASELINE] = json.dumps({"checks": {
        "corpus.index.tracked_files": {"expect": 7}, "corpus.index.unindexed": {"expect": 0},
        "corpus.pointers.report_total": {"expect": 5}, "corpus.pointers.commit_total": {"expect": 4}}})
    tracked = {p.rstrip("/") for p in R68_PATHS if "c2falsify-clone" not in p}
    return dict(files=files, tracked=tracked, base_blobs={p: "old-" + p for p in MODIFIED},
                r67={R68_BASE: (1, "r67 routed defects closed 0 of 4\n"),
                     R68_TIP: (0, "r67 routed defects closed 4 of 4\n")},
                gate={"tracked_files": 7, "unindexed": 0, "report_total": 5, "commit_total": 4})


def selftest() -> int:
    failures = 0

    def run(world: dict) -> int:
        n, _ = check(FakeRepo(**world))
        return n

    n = run(_honest())
    if n != TOTAL:
        n2, f = check(FakeRepo(**_honest()))
        print(f"FAIL honest world: closed {n} of {TOTAL}; {f}", file=sys.stderr)
        failures += 1
    else:
        print(f"PASS honest world: closed {TOTAL} of {TOTAL}")

    def mutate(fn):
        w = _honest()
        fn(w)
        return w

    def drop(path):
        return lambda w: w["files"].pop(path)

    def edit(path, old, new):
        return lambda w: w["files"].__setitem__(path, w["files"][path].replace(old, new))

    broken = {
        "D1 receipt missing": drop(f"{RECAP}/gate-registry.txt"),
        "D1 receipt names no revision": edit(f"{RECAP}/C1-after.txt", "measured-rev: ", "rev "),
        "D1 receipt revision not an ancestor": edit(f"{RECAP}/C1-after.txt", R68_BASE, "0" * 40),
        "D1 base receipt at another revision": edit(f"{RECAP}/C1-base.txt", R68_BASE, R68_TIP),
        "D1 receipt lacks its verdict": edit(f"{RECAP}/C1-selftest.txt", "over 12", "over 11"),
        "D2 self-test receipt still fails": edit(f"{RECAP}/C2-routed-selftest.txt", "exit=0",
                                                 "error: unrecognized arguments: --self-test\nexit=2"),
        "D3 counter still runs git checkout": edit(R67_COUNTER, "'clone', '--shared'", "'checkout', rev"),
        "D3 base receipt missing": drop(R67_BASE_RECEIPT),
        "D3 base still an environment error": lambda w: w["r67"].__setitem__(R68_BASE, (2, "")),
        "D3 tip no longer 4 of 4": lambda w: w["r67"].__setitem__(R68_TIP, (1, "closed 3 of 4")),
        "D4 S200 note absent": edit(LESSON, "S200: the quote drops `<code>` tags.", "S200 noted."),
        "D4 note outside Gate": edit(LESSON, "## Gate\n", "## Other\n"),
        "D5 no supersede row": edit(SOURCES, "supersedes S201 —", "corrects S201 —"),
        "D5 approval sentence absent": edit(SOURCES, APPROVAL, "approval is default"),
        "D5 entry does not name the row": edit(R68_ENTRY, "S208", "the row"),
        "D6 mistake row absent": edit(LESSON, "R68-6", "R68-x"),
        "D6 criterion absent": edit(QUALITY, "round-69.md", "round-68.md"),
        "D7 untracked path left": lambda w: w["tracked"].discard(f"{W}/seat-results.json"),
        "D7 modified log kept its base blob": lambda w: w["base_blobs"].__setitem__(MODIFIED[1], "new-" + MODIFIED[1]),
        "D7 removed path still tracked": lambda w: w["tracked"].add(f"{W}/controls/c2falsify-clone/x"),
        "D8 index row absent": edit(README, SPOTCHECK_TOKEN, "`lessons/absent.md`"),
        "D8 stale baseline": lambda w: w["gate"].__setitem__("tracked_files", 8),
    }
    for name, fn in broken.items():
        n = run(mutate(fn))
        if n == TOTAL:
            print(f"FAIL broken world survived: {name} -> closed {n}", file=sys.stderr)
            failures += 1
        else:
            print(f"PASS broken world rejected: {name}")
    print(f"self-test: {failures} failure(s) over {len(broken) + 1} assertions")
    return 1 if failures else 0


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="C2 counter for kotoba round 69")
    ap.add_argument("--rev", default=None, help="measured revision")
    ap.add_argument("--repo", default=str(Path(__file__).resolve().parent.parent))
    ap.add_argument("--self-test", action="store_true")
    args = ap.parse_args(argv)
    if args.self_test:
        return selftest()
    repo_path = Path(args.repo)
    try:
        if not args.rev:
            raise EnvError("--rev <revision> is required")
        proc = subprocess.run(["git", "-C", str(repo_path), "rev-parse", "--verify", "--quiet",
                               f"{args.rev}^{{commit}}"], capture_output=True, text=True)
        if proc.returncode != 0:
            raise EnvError(f"unknown revision {args.rev}")
        sha = proc.stdout.strip()
        n, findings = check(Repo(repo_path, sha))
    except EnvError as exc:
        print(f"environment error: {exc}", file=sys.stderr)
        return 2
    print(f"measured-rev: {sha}")
    print(f"r68 routed defects closed {n} of {TOTAL}")
    for f in findings:
        print(f"  - {f}")
    return 0 if n == TOTAL else 1


if __name__ == "__main__":
    sys.exit(main())
