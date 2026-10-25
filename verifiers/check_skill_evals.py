#!/usr/bin/env python3
"""check_skill_evals.py — C2 counter for kotoba round 70 (depth, sourced).

Contract
--------
`python3 -B verifiers/check_skill_evals.py --rev <rev>` prints
    measured-rev: <full-sha>
    skill eval facts backed N of 8
and exits 0 when N == 8, nonzero otherwise.  At the pinned base
`7d51253f99906b8551b6a0a108761eedac00de74` it must print `skill eval facts backed 0 of 8`
and exit 1.  `--fetch` adds a second evidence: each backed fact's quote is looked up on the
row's live URL and reported as `live quotes found K of N` (not part of N).

Fact Fi (F1…F8) is backed when the entry `corpus/knowledge/skill-eval-artefacts-round70.md`
at --rev carries exactly one `| Fi |` table row whose cells name one `S###` and a
double-quoted quote of 5–25 words containing every key term pinned for Fi below; the quote
is found verbatim (after stripping Markdown `*` and backticks and collapsing whitespace) in
the committed snapshot pinned for that `S###` (sha256 verified first — a tampered or missing
snapshot is exit 2); the `S###` row in `corpus/SOURCES.md` is an 11-cell `mined` row whose
`used-by` names the entry; and the entry's `source:` line names that `S###`.  Every fact
also requires `SKILL.md` at --rev to cite the entry path.

Trust boundary (QUALITY Q33, Q48): the key terms bind each quote to its fact's subject, the
snapshots bind it to bytes opened this round; neither proves the entry's prose around the
quote is a faithful reading — that half is the non-author spot-check's.  A missing entry is
a content verdict (exit 1); an unreadable environment is exit 2.

Exit codes: 0 all eight backed · 1 not all backed · 2 usage/environment error.
"""
from __future__ import annotations

import argparse
import hashlib
import re
import subprocess
import sys
import urllib.request
from pathlib import Path

TOTAL = 8
BASE = "7d51253f99906b8551b6a0a108761eedac00de74"
ENTRY = "corpus/knowledge/skill-eval-artefacts-round70.md"
SOURCES = "corpus/SOURCES.md"
SKILL = "SKILL.md"
SNAPDIR = ".ufo/waves/round-70/snapshots"
SNAPSHOTS = {
    "S209": ("S209-evaluating-skills.md",
             "a799805f3a285390c1b6e906b691f56684fa1031b499d177f664f464d99fb684",
             "https://agentskills.io/skill-creation/evaluating-skills.md"),
    "S210": ("S210-optimizing-descriptions.md",
             "7cc54fbb6abbcf08c33e7b320fd01a1fb9696426270da3b588a398d243bfd837",
             "https://agentskills.io/skill-creation/optimizing-descriptions.md"),
    "S211": ("S211-run_eval.py.txt",
             "43e3b8f80dbf69c343967ba77e268fae991d9fa3ed68b32a0ff02532cd48657f",
             "https://raw.githubusercontent.com/anthropics/skills/"
             "dbd4588f9e1033efb41dad4bef2f7947c8993d44/skills/skill-creator/scripts/run_eval.py"),
}
KEY_TERMS = {
    "F1": ("evals/evals.json", "by hand"),
    "F2": ("grading.json", "timing.json", "benchmark.json", "produced"),
    "F3": ("twice", "with the skill", "without it"),
    "F4": ("PASS", "FAIL", "evidence"),
    "F5": ("scripts", "LLM judgment", "mechanical"),
    "F6": ("Not everything needs an assertion",),
    "F7": ("should-trigger", "above a threshold", "0.5"),
    "F8": (">=", "trigger_threshold"),
}
SID_RE = re.compile(r"\bS\d{3,}\b")
QUOTE_RE = re.compile(r'"([^"]+)"')


class EnvError(Exception):
    pass


def norm(text: str) -> str:
    return re.sub(r"\s+", " ", text.replace("*", "").replace("`", "")).strip()


class Repo:
    def __init__(self, path: Path, rev: str):
        self.path, self.rev = path, rev

    def show(self, path: str) -> str | None:
        proc = subprocess.run(["git", "-C", str(self.path), "show", f"{self.rev}:{path}"],
                              capture_output=True)
        return proc.stdout.decode("utf-8", "replace") if proc.returncode == 0 else None

    def snapshot(self, sid: str) -> str:
        name, sha, _ = SNAPSHOTS[sid]
        proc = subprocess.run(["git", "-C", str(self.path), "show", f"{self.rev}:{SNAPDIR}/{name}"],
                              capture_output=True)
        if proc.returncode != 0:
            raise EnvError(f"snapshot {name} not committed at {self.rev}")
        if hashlib.sha256(proc.stdout).hexdigest() != sha:
            raise EnvError(f"snapshot_tampered: {name}")
        return proc.stdout.decode("utf-8", "replace")


def _cells(line: str) -> list[str]:
    s = line.strip()
    if not s.startswith("|"):
        return []
    return [c.strip() for c in s.strip("|").split("|")]


def source_rows(text: str) -> dict[str, list[str]]:
    rows = {}
    for line in text.splitlines():
        if re.match(r"^ {0,3}\|\s*S\d{3,}\s*\|", line):
            cells = _cells(line)
            rows[cells[0]] = cells
    return rows


def fact_rows(entry: str) -> dict[str, list[list[str]]]:
    out: dict[str, list[list[str]]] = {}
    for line in entry.splitlines():
        cells = _cells(line)
        if cells and re.fullmatch(r"F[1-8]", cells[0]):
            out.setdefault(cells[0], []).append(cells)
    return out


def check(repo, fetch=None) -> tuple[int, list[str], list[tuple[str, str, str]]]:
    entry = repo.show(ENTRY)
    if entry is None:
        return 0, [f"entry {ENTRY} absent"], []
    skill = repo.show(SKILL) or ""
    rows = source_rows(repo.show(SOURCES) or "")
    src_line = " ".join(l for l in entry.splitlines() if l.startswith("source:"))
    facts = fact_rows(entry)
    findings: list[str] = []
    backed: list[tuple[str, str, str]] = []
    skill_ok = ENTRY in skill
    if not skill_ok:
        findings.append(f"SKILL.md does not cite {ENTRY}")
    for fid, terms in KEY_TERMS.items():
        got = facts.get(fid, [])
        if len(got) != 1:
            findings.append(f"{fid}: {len(got)} table rows (want exactly 1)")
            continue
        cells = got[0]
        sids = sorted({s for c in cells[1:] for s in SID_RE.findall(c)})
        quotes = [q for c in cells[1:] for q in QUOTE_RE.findall(c)]
        if len(sids) != 1 or len(quotes) != 1:
            findings.append(f"{fid}: needs one S### and one quote, got {sids} / {len(quotes)}")
            continue
        sid, quote = sids[0], norm(quotes[0])
        if not 5 <= len(quote.split()) <= 25:
            findings.append(f"{fid}: quote is {len(quote.split())} words")
            continue
        miss = [t for t in terms if t not in quote]
        if miss:
            findings.append(f"{fid}: quote lacks key terms {miss}")
            continue
        if sid not in SNAPSHOTS:
            findings.append(f"{fid}: {sid} has no pinned snapshot")
            continue
        if quote not in norm(repo.snapshot(sid)):
            findings.append(f"{fid}: quote not in the {sid} snapshot")
            continue
        row = rows.get(sid)
        if row is None or len(row) != 11:
            findings.append(f"{fid}: {sid} is not an 11-cell SOURCES row")
            continue
        if row[7] != "mined" or ENTRY not in row[10]:
            findings.append(f"{fid}: {sid} not mined or used-by lacks the entry")
            continue
        if sid not in SID_RE.findall(src_line):
            findings.append(f"{fid}: entry source: line does not name {sid}")
            continue
        if skill_ok:
            backed.append((fid, sid, quote))
    return len(backed), findings, backed


def live_fetch(backed) -> tuple[int, list[str]]:
    found, notes, pages = 0, [], {}
    for fid, sid, quote in backed:
        url = SNAPSHOTS[sid][2]
        if url not in pages:
            try:
                req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
                with urllib.request.urlopen(req, timeout=30) as resp:
                    pages[url] = norm(resp.read().decode("utf-8", "replace"))
            except Exception as exc:  # network is a second evidence, never the verdict
                pages[url] = None
                notes.append(f"{sid}: fetch failed: {exc}")
        if pages[url] is not None and quote in pages[url]:
            found += 1
        elif pages[url] is not None:
            notes.append(f"{fid}: quote not on the live {sid} page")
    return found, notes


# ---------------------------------------------------------------- self-test
SNAP_TEXT = {
    "S209": ("The main file you author by hand is `evals/evals.json`. The other JSON files "
             "(`grading.json`, `timing.json`, `benchmark.json`) are produced during the eval process. "
             "The core pattern is to run each test case twice: once **with the skill** and once "
             "**without it**. Grading means evaluating each assertion against the actual outputs and "
             "recording **PASS** or **FAIL** with specific evidence. Use a script: scripts are more "
             "reliable than LLM judgment for mechanical checks and reusable across iterations. "
             "Not everything needs an assertion. Start with 2-3 test cases."),
    "S210": ("A should-trigger query passes if its trigger rate is above a threshold (0.5 is a "
             "reasonable default). Aim for about 20 queries."),
    "S211": "        if should_trigger:\n            did_pass = trigger_rate >= trigger_threshold\n",
}
HONEST_QUOTES = {
    "F1": ("S209", "The main file you author by hand is evals/evals.json."),
    "F2": ("S209", "The other JSON files (grading.json, timing.json, benchmark.json) are produced "
                   "during the eval process"),
    "F3": ("S209", "run each test case twice: once with the skill and once without it"),
    "F4": ("S209", "recording PASS or FAIL with specific evidence"),
    "F5": ("S209", "scripts are more reliable than LLM judgment for mechanical checks"),
    "F6": ("S209", "Not everything needs an assertion."),
    "F7": ("S210", "A should-trigger query passes if its trigger rate is above a threshold"
                   " (0.5 is a reasonable default)."),
    "F8": ("S211", "did_pass = trigger_rate >= trigger_threshold"),
}


class FakeRepo:
    def __init__(self, files: dict[str, str], snaps: dict[str, str | None]):
        self.files, self.snaps = files, snaps

    def show(self, path):
        return self.files.get(path)

    def snapshot(self, sid):
        text = self.snaps.get(sid)
        if text is None:
            raise EnvError(f"snapshot_tampered: {sid}")
        return text


def _entry(quotes: dict) -> str:
    rows = "\n".join(f'| {f} | fact {f} | {s} | "{q}" |' for f, (s, q) in quotes.items())
    return f"source: S209 S210 S211\nverified-at: x\nrecheck: 90d\n\n| id | fact | row | quote |\n|---|---|---|---|\n{rows}\n"


def _source_row(sid: str, status: str = "mined", used: str = ENTRY) -> str:
    return f"| {sid} | t | docs | A | s | a | t | {status} | 2026-10-25 | 90d | {used} |"


def _honest() -> dict:
    files = {ENTRY: _entry(HONEST_QUOTES), SKILL: f"see {ENTRY}\n",
             SOURCES: "\n".join(_source_row(s) for s in SNAPSHOTS) + "\n"}
    return {"files": files, "snaps": dict(SNAP_TEXT)}


def selftest() -> int:
    failures = 0

    def run(world):
        return check(FakeRepo(world["files"], world["snaps"]))[0]

    n = run(_honest())
    if n != TOTAL:
        failures += 1
        print(f"FAIL honest world: backed {n} of {TOTAL}; {check(FakeRepo(**_honest()))[1]}",
              file=sys.stderr)
    else:
        print(f"PASS honest world: backed {TOTAL} of {TOTAL}")

    def quotes(fn):
        def mut(w):
            w["files"][ENTRY] = _entry({f: fn(f, s, q) for f, (s, q) in HONEST_QUOTES.items()})
        return mut

    def file_edit(path, old, new):
        def mut(w):
            w["files"][path] = w["files"][path].replace(old, new)
        return mut

    broken = {
        "junk control: on-page quotes without key terms (all facts)": (
            quotes(lambda f, s, q: (s, "Start with 2-3 test cases.") if s == "S209"
                   else (s, "Aim for about 20 queries.") if s == "S210"
                   else (s, "if should_trigger: did_pass = trigger_rate")), 0),
        "forged control: key terms present, quotes off-snapshot (all facts)": (
            quotes(lambda f, s, q: (s, q + " always")), 0),
        "SKILL.md does not cite the entry": (file_edit(SKILL, ENTRY, "elsewhere"), 0),
        "entry absent": (lambda w: w["files"].pop(ENTRY), 0),
        "row not mined": (file_edit(SOURCES, "| mined |", "| queued |"), 0),
        "used-by lacks the entry": (file_edit(SOURCES, f"| {ENTRY} |", "| — |"), 0),
        "source: line omits S211": (file_edit(ENTRY, "source: S209 S210 S211", "source: S209 S210"), 7),
        "duplicate F3 row": (lambda w: w["files"].__setitem__(
            ENTRY, w["files"][ENTRY] + '| F3 | again | S209 | "run each test case twice: once with the skill and once without it" |\n'), 7),
        "quote over 25 words": (quotes(lambda f, s, q: (s, q + " x" * 30) if f == "F4" else (s, q)), 7),
        "F8 inverted operator": (quotes(lambda f, s, q: (s, q.replace(">=", "<")) if f == "F8" else (s, q)), 7),
        "fact cites the wrong snapshot": (quotes(lambda f, s, q: ("S210", q) if f == "F1" else (s, q)), 7),
    }
    for name, (mutate, want_max) in broken.items():
        w = _honest()
        mutate(w)
        n = run(w)
        if n > want_max or n == TOTAL:
            failures += 1
            print(f"FAIL broken world survived: {name} -> backed {n}", file=sys.stderr)
        else:
            print(f"PASS broken world rejected: {name} -> backed {n}")
    w = _honest()
    w["snaps"]["S209"] = None
    try:
        run(w)
        failures += 1
        print("FAIL tampered snapshot did not raise", file=sys.stderr)
    except EnvError:
        print("PASS tampered snapshot is an environment error (exit 2)")
    print(f"self-test: {failures} failure(s) over {len(broken) + 2} assertions")
    return 0 if failures == 0 else 1


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="C2 counter for kotoba round 70")
    ap.add_argument("--rev", default=None)
    ap.add_argument("--repo", default=str(Path(__file__).resolve().parent.parent))
    ap.add_argument("--fetch", action="store_true")
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
        n, findings, backed = check(Repo(path, rev))
    except EnvError as exc:
        print(f"environment error: {exc}", file=sys.stderr)
        return 2
    print(f"measured-rev: {rev}")
    print(f"skill eval facts backed {n} of {TOTAL}")
    for f in findings:
        print(f"  {f}")
    if args.fetch:
        k, notes = live_fetch(backed)
        print(f"live quotes found {k} of {n}")
        for note in notes:
            print(f"  {note}")
    return 0 if n == TOTAL else 1


if __name__ == "__main__":
    sys.exit(main())
