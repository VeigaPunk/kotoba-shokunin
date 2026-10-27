#!/usr/bin/env python3
"""check_skill_evals_v2.py — C2 successor counter for kotoba round 71 (depth).

Frozen predicate (the same sentence in plans/round-71.md and in the receipts):

    python3 -B verifiers/check_skill_evals_v2.py --rev <rev>
        ->  prints "skill eval artefacts verified N of 10", exit 0 when N == 10

Successor to check_skill_evals.py (round 70), redesigned against the round-70
closure's routed defects (corpus/lessons/round-70-verifier-spotcheck.md
§ Routed defects; wave seat CritC2Control: 11 of 13 junk worlds scored 8 of 8,
the cheapest — W12 — at +13 lines on the pre-data commit):

  W12/W01  fact-less rows scored: v2 requires the exactly-4-cell shape
           ``| Fi | fact | S### | "quote" |`` with a fact cell of >=8 words
           that is not the quote and carries no S### or quoted span.
  W05/W10  HTML comments and fenced blocks counted: v2 strips them from the
           entry, SKILL.md and SOURCES.md before parsing.
  W08      quotes matched mid-word (raw substring): v2 bounds the match.
  W01 rows ``x``-filled SOURCES cells scored: v2 requires the cited row's
           comma-separated ``used-by`` members to include the exact entry
           path (no substring, no ``not <entry>``), adds a census-validate
           item over the revision's registry (A10), and pins which documents
           the entry may cite (PINNED_DOCS) — a row for any other S### fails
           its facts.
  W02/W09  fact text contradicting or unrelated to its quote: only the
           >=8-words distinct-from-quote shape is machine-checked; semantic
           agreement stays a named non-author spot-check duty (declared
           boundary, unchanged from r70).
  SKILL    a bare path, comment or "never consult" line counted: v2 requires
           exactly one rendered line naming the entry path AND every cited
           S###, and rejects entry lines carrying a negation.
  W11      the counter that ran was the measured tree's own (swap to
           ``n = TOTAL`` scored): v2 hashes the file at --rev with the
           SELF_SHA line blanked and fails on drift (exit 2).
  anchors  S209/S210 carried no upstream revision: superseding rows
           S212/S213 (canonical URL, upstream commit, fetched sha256 in the
           anchor cell, ``supersedes S0NN`` teaches cell) are the only
           admissible citations for the two agentskills.io documents — A9
           requires an ``upstream commit`` token in each cited
           agentskills.io row's anchor.

The quote half is kept verbatim from r70: sha256-pinned snapshots (tamper is
exit 2), 5–25-word quotes carrying the pinned key terms.

Environment: --repo the measured git worktree (default: this lane), --rev the
measured revision, --census the sources-census.sh path.  Read-only on the
lane: scratch trees live in $TMPDIR.  --fetch re-opens the three .md exports
as a second evidence, never the verdict.
"""

from __future__ import annotations

import argparse
import hashlib
import re
import os
import shutil
import subprocess
import sys
import tempfile
import urllib.request
from pathlib import Path

TOTAL = 10
ENTRY = "corpus/knowledge/skill-eval-artefacts-round70.md"
SOURCES = "corpus/SOURCES.md"
SKILL = "SKILL.md"
COUNTER_PATH = "verifiers/check_skill_evals_v2.py"
SNAPDIR = ".ufo/waves/round-70/snapshots"
# The only documents the entry may cite for F1–F8; each names its sha256-
# pinned snapshot (r70) and the URL --fetch re-opens.
PINNED_DOCS = {
    "S211": ("S211-run_eval.py.txt",
             "43e3b8f80dbf69c343967ba77e268fae991d9fa3ed68b32a0ff02532cd48657f",
             "https://raw.githubusercontent.com/anthropics/skills/"
             "dbd4588f9e1033efb41dad4bef2f7947c8993d44/skills/skill-creator/"
             "scripts/run_eval.py"),
    "S212": ("S209-evaluating-skills.md",
             "a799805f3a285390c1b6e906b691f56684fa1031b499d177f664f464d99fb684",
             "https://agentskills.io/skill-creation/evaluating-skills.md"),
    "S213": ("S210-optimizing-descriptions.md",
             "7cc54fbb6abbcf08c33e7b320fd01a1fb9696426270da3b588a398d243bfd837",
             "https://agentskills.io/skill-creation/optimizing-descriptions.md"),
}
AGENTSKILLS_RE = re.compile(r"agentskills\.io")
UPSTREAM_REV_RE = re.compile(r"upstream commit [0-9a-f]{7,40}")
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
NEGATION_RE = re.compile(
    r"\b(?:never|not|don't|do not|retracted|false|avoid|ignore|stale)\b",
    re.IGNORECASE)
SELF_SHA = "9530549b49e2ef9b13f2be28caeab481f1ff637541918cee14b52c45c7ee22c4"   # blanked-sha of this file
SELF_LINE_RE = re.compile(r'^SELF_SHA = "[0-9a-f]*"', re.M)


def _blanked_sha(text: str) -> str:
    return hashlib.sha256(
        SELF_LINE_RE.sub('SELF_SHA = ""', text).encode()).hexdigest()


class EnvError(Exception):
    pass


def norm(text: str) -> str:
    return re.sub(r"\s+", " ", text.replace("*", "").replace("`", "")).strip()


def rendered(text: str) -> str:
    """Rendered content only: HTML comments and fenced code removed."""
    text = re.sub(r"<!--.*?-->", "", text, flags=re.S)
    out, in_fence = [], False
    for line in text.splitlines():
        if re.match(r"^\s*```", line):
            in_fence = not in_fence
            continue
        if not in_fence:
            out.append(line)
    return "\n".join(out)


def word_bounded(needle: str, haystack: str) -> bool:
    return re.search(r"(?<![\w])" + re.escape(needle) + r"(?![\w])",
                     haystack) is not None


class Repo:
    def __init__(self, path: Path, rev: str, census: str):
        self.path, self.rev, self.census = path, rev, census

    def show(self, path: str) -> str | None:
        proc = subprocess.run(
            ["git", "-C", str(self.path), "show", f"{self.rev}:{path}"],
            capture_output=True)
        return proc.stdout.decode("utf-8", "replace") \
            if proc.returncode == 0 else None

    def snapshot(self, sid: str) -> str:
        name, sha, _ = PINNED_DOCS[sid]
        proc = subprocess.run(
            ["git", "-C", str(self.path), "show",
             f"{self.rev}:{SNAPDIR}/{name}"],
            capture_output=True)
        if proc.returncode != 0:
            raise EnvError(f"snapshot {name} not committed at {self.rev}")
        if hashlib.sha256(proc.stdout).hexdigest() != sha:
            raise EnvError(f"snapshot_tampered: {name}")
        return proc.stdout.decode("utf-8", "replace")

    def census_ok(self) -> bool | None:
        """sources-census validate --file on the revision's corpus tree."""
        with tempfile.TemporaryDirectory(prefix="k71-c2-") as td:
            root = Path(td)
            proc = subprocess.run(
                ["git", "-C", str(self.path), "archive", self.rev],
                capture_output=True)
            if proc.returncode != 0:
                return None
            (root / "tree.tar").write_bytes(proc.stdout)
            subprocess.run(["tar", "-xf", "tree.tar"], cwd=root,
                           capture_output=True)
            target = root / "corpus" / "SOURCES.md"
            if not target.is_file():
                return None
            proc = subprocess.run(
                ["bash", self.census, "validate", "--file", str(target)],
                capture_output=True, text=True, timeout=120)
            return proc.returncode == 0


def _cells(line: str) -> list[str]:
    s = line.strip()
    if not s.startswith("|"):
        return []
    return [c.strip() for c in s.strip("|").split("|")]


def source_rows(text: str) -> dict[str, list[list[str]]]:
    rows: dict[str, list[list[str]]] = {}
    for line in text.splitlines():
        if re.match(r"^ {0,3}\|\s*S\d{3,}\s*\|", line):
            cells = _cells(line)
            rows.setdefault(cells[0], []).append(cells)
    return rows


def fact_rows(entry: str) -> dict[str, list[list[str]]]:
    out: dict[str, list[list[str]]] = {}
    for line in entry.splitlines():
        cells = _cells(line)
        if cells and re.fullmatch(r"F[1-8]", cells[0]):
            out.setdefault(cells[0], []).append(cells)
    return out


def check(repo) -> tuple[int, list[str], list[tuple[str, str, str]]]:
    entry = repo.show(ENTRY)
    if entry is None:
        return 0, [f"entry {ENTRY} absent"], []
    entry_r = rendered(entry)
    skill_r = rendered(repo.show(SKILL) or "")
    rows = source_rows(rendered(repo.show(SOURCES) or ""))
    src_ids = set()
    for line in entry_r.splitlines():
        if line.startswith("source:"):
            src_ids.update(SID_RE.findall(line))
    facts = fact_rows(entry_r)
    findings: list[str] = []
    backed: list[tuple[str, str, str]] = []
    cited = sorted(src_ids & set(PINNED_DOCS))

    # SKILL citation: exactly one rendered line names the entry AND all ids.
    skill_lines = [l for l in skill_r.splitlines() if ENTRY in l]
    good = [l for l in skill_lines
            if all(s in l for s in PINNED_DOCS)
            and not NEGATION_RE.search(l)]
    if len(good) != 1:
        findings.append(
            f"SKILL.md: {len(good)} rendered lines name the entry + "
            f"S211/S212/S213 (want exactly 1; {len(skill_lines)} name the "
            f"path, {len(skill_lines) - len(good)} rejected)")

    for fid, terms in KEY_TERMS.items():
        got = facts.get(fid, [])
        if len(got) != 1:
            findings.append(f"{fid}: {len(got)} table rows (want exactly 1)")
            continue
        cells = got[0]
        if len(cells) != 4:
            findings.append(
                f"{fid}: {len(cells)} cells (want 4: id | fact | S### | quote)")
            continue
        fact, sid_cell, qcell = cells[1], cells[2], cells[3]
        if len(fact.split()) < 8:
            findings.append(f"{fid}: fact cell has {len(fact.split())} words "
                            f"(want >=8)")
            continue
        if SID_RE.search(fact) or QUOTE_RE.search(fact):
            findings.append(f"{fid}: fact cell carries an S### or a quote")
            continue
        quotes0 = QUOTE_RE.findall(qcell)
        if quotes0 and norm(fact) == norm(quotes0[0]):
            findings.append(f"{fid}: fact cell repeats the quote")
            continue
        sids = SID_RE.findall(sid_cell)
        quotes = QUOTE_RE.findall(qcell)
        if len(sids) != 1 or len(quotes) != 1:
            findings.append(
                f"{fid}: cell 3/4 must hold one S### and one \"quote\"")
            continue
        sid, quote = sids[0], norm(quotes[0])
        if sid not in PINNED_DOCS:
            findings.append(f"{fid}: {sid} is not a pinned document")
            continue
        if sid not in src_ids:
            findings.append(f"{fid}: entry source: lines do not name {sid}")
            continue
        if not 5 <= len(quote.split()) <= 25:
            findings.append(f"{fid}: quote is {len(quote.split())} words")
            continue
        miss = [t for t in terms if t not in quote]
        if miss:
            findings.append(f"{fid}: quote lacks key terms {miss}")
            continue
        if not word_bounded(quote, norm(repo.snapshot(sid))):
            findings.append(f"{fid}: quote not word-bounded in the {sid} "
                            f"snapshot")
            continue
        rs = rows.get(sid, [])
        if len(rs) != 1:
            findings.append(f"{fid}: {sid} has {len(rs)} registry rows "
                            f"(want exactly 1)")
            continue
        row = rs[0]
        if len(row) != 11 or row[7] != "mined":
            findings.append(f"{fid}: {sid} is not an 11-cell mined row")
            continue
        used_by = [p.strip() for p in row[10].split(",")]
        if ENTRY not in used_by:
            findings.append(f"{fid}: {sid} used-by lacks exact member {ENTRY} "
                            f"(comma-delimited exact match required)")
            continue
        if good:
            backed.append((fid, sid, quote))

    # A9: every cited agentskills.io row's anchor carries an upstream commit.
    a9 = True
    for sid in sorted(src_ids):
        for row in rows.get(sid, []):
            if len(row) != 11:
                continue
            if AGENTSKILLS_RE.search(row[1]) \
                    and not UPSTREAM_REV_RE.search(row[5]):
                findings.append(
                    f"A9: {sid} anchor lacks an upstream commit "
                    f"({row[5][:60]})")
                a9 = False
    if a9 and cited:
        backed.append(("A9", ";".join(sorted(src_ids)), "upstream revisions"))

    # A10: census validate on the revision's registry.
    ok = repo.census_ok()
    if ok is True:
        backed.append(("A10", "census", "registry conforms"))
    elif ok is None:
        findings.append("A10: could not evaluate census validate")
    else:
        findings.append("A10: census validate --file non-zero at --rev")
    return len(backed), findings, backed


def live_fetch(backed) -> tuple[int, list[str]]:
    found, notes, pages = 0, [], {}
    for fid, sid, quote in backed:
        if sid not in PINNED_DOCS:
            continue
        url = PINNED_DOCS[sid][2]
        if url not in pages:
            try:
                req = urllib.request.Request(
                    url, headers={"User-Agent": "Mozilla/5.0"})
                with urllib.request.urlopen(req, timeout=30) as resp:
                    pages[url] = norm(resp.read().decode("utf-8", "replace"))
            except Exception as exc:
                pages[url] = None
                notes.append(f"{sid}: fetch failed: {exc}")
        if pages[url] is not None and quote in pages[url]:
            found += 1
        elif pages[url] is not None:
            notes.append(f"{fid}: quote not on the live {sid} page")
    return found, notes


# ---------------------------------------------------------------- self-test
SNAP_TEXT = {
    "S211": "        if should_trigger:\n            did_pass = trigger_rate "
            ">= trigger_threshold\n",
    "S212": ("The main file you author by hand is `evals/evals.json`. The "
             "other JSON files (`grading.json`, `timing.json`, "
             "`benchmark.json`) are produced during the eval process. The "
             "core pattern is to run each test case twice: once **with the "
             "skill** and once **without it**. Grading means evaluating each "
             "assertion against the actual outputs and recording **PASS** or "
             "**FAIL** with specific evidence. Use a script: scripts are "
             "more reliable than LLM judgment for mechanical checks and "
             "reusable across iterations. Not everything needs an "
             "assertion. Start with 2-3 test cases."),
    "S213": ("A should-trigger query passes if its trigger rate is above a "
             "threshold (0.5 is a reasonable default). Aim for about 20 "
             "queries."),
}
HONEST = {
    "F1": ("S212", "the one hand-authored artefact lives inside the skill "
           "directory at evals/evals.json",
           "The main file you author by hand is evals/evals.json."),
    "F2": ("S212", "three more JSON files come out of the eval run rather "
           "than authored up front",
           "The other JSON files (grading.json, timing.json, benchmark.json)"
           " are produced during the eval process"),
    "F3": ("S212", "every case runs twice so the result is a delta over a "
           "baseline",
           "run each test case twice: once with the skill and once without it"),
    "F4": ("S212", "grading is evidence-bearing with a verdict and quoted "
           "evidence",
           "recording PASS or FAIL with specific evidence"),
    "F5": ("S212", "mechanical checks go to a verification script instead of "
           "an LLM",
           "scripts are more reliable than LLM judgment for mechanical checks"),
    "F6": ("S212", "style and feel are left to human review, not forced "
           "assertions",
           "Not everything needs an assertion."),
    "F7": ("S213", "a should-trigger query passes above its trigger-rate "
           "threshold",
           "A should-trigger query passes if its trigger rate is above a "
           "threshold (0.5 is a reasonable default)."),
    "F8": ("S211", "the reference runner passes at a rate equal to the "
           "threshold too",
           "did_pass = trigger_rate >= trigger_threshold"),
}


class FakeRepo:
    def __init__(self, files: dict, snaps: dict | None = None,
                 census: bool = True):
        self.files = files
        self.snaps = snaps if snaps is not None else dict(SNAP_TEXT)
        self.census = census

    def show(self, path):
        return self.files.get(path)

    def snapshot(self, sid):
        text = self.snaps.get(sid)
        if text is None:
            raise EnvError(f"snapshot_tampered: {sid}")
        return text

    def census_ok(self):
        return self.census


def _row(sid: str, used: str = ENTRY, status: str = "mined",
         anchor: str | None = None,
         url: str | None = None) -> str:
    url = url or {
        "S209": "x — https://agentskills.io/skill-creation/"
                "evaluating-skills.md",
        "S210": "x — https://agentskills.io/skill-creation/"
                "optimizing-descriptions.md",
        "S211": "x — https://github.com/anthropics/skills/blob/dbd4588/x",
        "S212": "x — https://agentskills.io/skill-creation/"
                "evaluating-skills",
        "S213": "x — https://agentskills.io/skill-creation/"
                "optimizing-descriptions",
    }.get(sid, "x — https://example.invalid/" + sid)
    anchor = anchor or ("upstream commit " + "a" * 7 + " lines x")
    return (f"| {sid} | {url} | docs | A | s | {anchor} | t | {status} |"
            f" 2026-10-25 | 90d | {used} |")


def _entry(facts: dict | None = None, src: str | None = None) -> str:
    src = src or "source: S211\nsource: S212\nsource: S213\n"
    facts = facts if facts is not None else HONEST
    rows = "\n".join(
        f'| {f} | {d[1]} | {d[0]} | "{d[2]}" |'
        for f, d in sorted(facts.items()))
    return (src + "verified-at: x\nrecheck: 90d\n\n"
            "| id | fact | row | located quote |\n|---|---|---|---|\n"
            + rows + "\n")


def _honest() -> FakeRepo:
    files = {
        ENTRY: _entry(),
        SKILL: f"see `corpus/knowledge/skill-eval-artefacts-round70.md` "
               f"(S211, S212, S213)\n",
        SOURCES: "\n".join(_row(s) for s in PINNED_DOCS) + "\n",
    }
    return FakeRepo(files)


def _git_world_c2() -> tuple[int, str] | None:
    """Materialize the committed c2-junk-world bundle over a clone of the
    pre-data commit, run main() on the junk commit, return (exit, stdout)."""
    lane = Path(__file__).resolve().parent.parent
    bundle = lane / ".ufo/waves/round-71/controls/c2-junk-world"
    pre = "a647fa734430cb07066a9b6377b157310a7943db"
    if not (bundle / "entry.md").is_file():
        return None
    env = dict(os.environ,
               GIT_AUTHOR_NAME="t", GIT_AUTHOR_EMAIL="t@t",
               GIT_COMMITTER_NAME="t", GIT_COMMITTER_EMAIL="t@t")
    try:
        with tempfile.TemporaryDirectory(prefix="k71-c2j-") as td:
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
            shutil.copy(bundle / "entry.md", clone / ENTRY)
            shutil.copy(bundle / "sources-base.md", clone / SOURCES)
            shutil.copy(bundle / "skill-base.md", clone / SKILL)
            p = subprocess.run(
                ["git", "-C", str(clone), "add", "-A"],
                capture_output=True, text=True)
            p = subprocess.run(
                ["git", "-C", str(clone), "commit", "-qm", "junk"],
                capture_output=True, text=True, env=env)
            if p.returncode != 0:
                return None
            p = subprocess.run(
                ["python3", "-B", str(lane / "verifiers" /
                                     "check_skill_evals_v2.py"),
                 "--repo", str(clone), "--rev", "HEAD"],
                capture_output=True, text=True, timeout=300)
            return p.returncode, p.stdout + p.stderr
    except (OSError, subprocess.TimeoutExpired):
        return None


def selftest() -> int:
    failures = 0

    def run(repo) -> tuple[int, list[str]]:
        return check(repo)[0], check(repo)[1]

    n, f = run(_honest())
    if n != TOTAL or f:
        print(f"FAIL honest world: verified {n} of {TOTAL} {f}")
        failures += 1
    else:
        print(f"PASS honest world: verified {n} of {TOTAL}")

    # SOURCES contract rule 2 permits append-only use of a row by multiple
    # entries. The r76 description entry adds S213 as a second exact member.
    multi = _honest()
    source_lines = multi.files[SOURCES].splitlines()
    found_s213 = False
    for i, line in enumerate(source_lines):
        cells = _cells(line)
        if cells and cells[0] == "S213":
            cells[10] += ", corpus/knowledge/description-craft-round76.md"
            source_lines[i] = "| " + " | ".join(cells) + " |"
            found_s213 = True
            break
    multi.files[SOURCES] = "\n".join(source_lines) + "\n"
    multi.files["corpus/knowledge/description-craft-round76.md"] = (
        "source: S213 — https://agentskills.io/skill-creation/"
        "optimizing-descriptions.md\nverified-at: fixture\nrecheck: fixture\n")
    n, f = run(multi)
    if not found_s213 or n != TOTAL or f:
        print(f"FAIL append-only multi-entry S213 used-by: {n} of {TOTAL} {f}")
        failures += 1
    else:
        print("PASS append-only multi-entry S213 used-by exact member")

    def broken(label, mutate, needle):
        nonlocal failures
        fr = _honest()
        mutate(fr)
        n, f = run(fr)
        if n == TOTAL or not any(needle in x for x in f):
            print(f"FAIL junk world accepted: {label} ({n}, {f})")
            failures += 1
        else:
            print(f"PASS junk world rejected: {label}")

    # W12 — the r70 cheapest junk world: no fact cells, x-rows, bare SKILL line.
    def w12(fr):
        bare = "source: S211 S212 S213\n" + "\n".join(
            f'| {f} | {d[0]} "{d[2]}" |' for f, d in sorted(HONEST.items()))
        fr.files[ENTRY] = bare
        fr.files[SOURCES] = "\n".join(
            f"| {s} | x | docs | A | x | x | x | mined | 2026-10-25 | 90d |"
            f" {ENTRY} |" for s in PINNED_DOCS) + "\n"
        fr.files[SKILL] = f"{ENTRY}\n"
    broken("W12 bare entry + x rows + bare SKILL line", w12, "F1")

    # W05 — comments hide everything.
    def w05(fr):
        fr.files[ENTRY] = "<!--\n" + fr.files[ENTRY] + "\n-->"
        fr.files[SKILL] = f"<!-- see {ENTRY} S211 S212 S213 -->\n"
    broken("W05 HTML comments", w05, "entry")

    # W10 — facts live inside a code fence.
    def w10(fr):
        fr.files[ENTRY] = (fr.files[ENTRY].splitlines()[0]
                           + "\n```text\n"
                           + "\n".join(fr.files[ENTRY].splitlines()[1:])
                           + "\n```\n")
    broken("W10 fenced entry body", w10, "F1")

    # W08 — mid-word quote fragments.
    def w08(fr):
        facts = dict(HONEST)
        facts["F1"] = ("S212", HONEST["F1"][1],
                       HONEST["F1"][2][5:])
        fr.files[ENTRY] = _entry(facts)
    broken("W08 mid-word quote", w08, "F1")

    # W06-variant — `not <entry>` used-by and a shadow row.
    def w06(fr):
        fr.files[SOURCES] += _row("S212", used="not corpus/knowledge/x.md",
                                  status="mined")
    broken("W06 shadow SOURCES row", w06, "F1")

    # used-by by substring: an entry-named path inside a longer cell.
    def ub(fr):
        fr.files[SOURCES] = fr.files[SOURCES].replace(
            f"| {ENTRY} |", f"| {ENTRY}.bak |")
    broken("used-by substring path", ub, "used-by")

    # junk rows — invalid enum caught by the census item.
    def jc(fr):
        fr.census = False
    broken("census-invalid registry", jc, "A10")

    # S209/S210-style anchor without an upstream commit.
    def na(fr):
        fr.files[SOURCES] = fr.files[SOURCES].replace(
            "upstream commit aaaaaaa", "page fetched 2026-10-25")
    broken("A9 anchor without upstream revision", na, "A9")

    # unpinned document cited instead of the superseding rows.
    def old(fr):
        facts = dict(HONEST)
        for f in ("F1", "F2", "F3", "F4", "F5", "F6"):
            facts[f] = ("S209", facts[f][1], facts[f][2])
        facts["F7"] = ("S210", facts["F7"][1], facts["F7"][2])
        fr.files[ENTRY] = _entry(facts, "source: S209\nsource: S210\n"
                                        "source: S211\n")
        fr.files[SOURCES] += _row("S209", anchor="page fetched x") + "\n"
        fr.files[SOURCES] += _row("S210", anchor="page fetched x") + "\n"
        fr.files[SKILL] = f"see {ENTRY} (S209–S211)\n"
    broken("unpinned S209/S210 citations", old, "pinned")

    # negated SKILL line.
    def neg(fr):
        fr.files[SKILL] = (f"- Never consult `{ENTRY}`: retracted, every "
                           f"fact false (S211 S212 S213)\n")
    broken("negated SKILL line", neg, "SKILL")

    # fact cell contradicts nothing but duplicates the quote (no fact text).
    def dup(fr):
        facts = dict(HONEST)
        facts["F3"] = ("S212", HONEST["F3"][2], HONEST["F3"][2])
        fr.files[ENTRY] = _entry(facts)
    broken("fact cell is the quote itself", dup, "F3")

    # entry cites an S### its rows lack.
    def nosrc(fr):
        fr.files[ENTRY] = _entry(src="source: S211\nsource: S212\n")
    broken("entry source: omits S213", nosrc, "S213")

    # snapshot tamper exits 2 (kept from r70).
    fr = _honest()
    del fr.snaps["S211"]
    try:
        check(fr)
        print("FAIL snapshot tamper not exit 2")
        failures += 1
    except EnvError:
        print("PASS snapshot tamper -> EnvError (exit 2)")


    # Real-git junk world: the committed bundle at
    # .ufo/waves/round-71/controls/c2-junk-world/ committed on top of the
    # pre-data commit a647fa7 (W12 lineage) must score < TOTAL through main().
    junk = _git_world_c2()
    if junk is None:
        print("SKIP c2 committed junk world: sandbox repo unavailable")
    else:
        code, out = junk
        m = re.search(r"verified (\d+) of (\d+)", out)
        if code == 1 and m and int(m.group(1)) <= 2:
            print(f"PASS c2 committed junk world rejected ({m.group(1)}/10)")
        else:
            print(f"FAIL c2 committed junk world: exit={code} out={out!r}")
            failures += 1
    print(f"self-test: {failures} failure(s)")
    return 0 if failures == 0 else 1


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(
        description="C2 successor counter for kotoba round 71")
    ap.add_argument("--rev", default=None, help="measured revision")
    ap.add_argument("--repo",
                    default=str(Path(__file__).resolve().parent.parent))
    ap.add_argument("--census",
                    default="/home/vgpnk/Projects/shokunin/scripts/"
                            "sources-census.sh")
    ap.add_argument("--fetch", action="store_true",
                    help="re-open each cited URL and check the quote")
    ap.add_argument("--self-test", action="store_true")
    args = ap.parse_args(argv)
    if args.self_test:
        return selftest()
    if not args.rev:
        raise EnvError("--rev <revision> is required")
    repo = Repo(Path(args.repo), args.rev, args.census)
    proc = subprocess.run(
        ["git", "-C", str(repo.path), "rev-parse", "--verify", "-q",
         f"{args.rev}^{{commit}}"], capture_output=True)
    if proc.returncode != 0:
        print(f"environment error: --rev {args.rev} is not a commit",
              file=sys.stderr)
        return 2
    src = Path(__file__).read_text()
    if _blanked_sha(src) != SELF_SHA:
        print("environment error: counter drifted — the running file is not "
              "the frozen counter", file=sys.stderr)
        return 2
    try:
        n, findings, backed = check(repo)
    except EnvError as exc:
        print(f"environment error: {exc}", file=sys.stderr)
        return 2
    print(f"measured-rev: {args.rev}")
    print(f"skill eval artefacts verified {n} of {TOTAL}")
    for f in findings:
        print(f"  {f}")
    if args.fetch and backed:
        live, notes = live_fetch(backed)
        print(f"live quotes found {live} of "
              f"{len([b for b in backed if b[1] in PINNED_DOCS])}")
        for note in notes:
            print(f"  {note}")
    return 0 if n == TOTAL else 1


if __name__ == "__main__":
    sys.exit(main())
