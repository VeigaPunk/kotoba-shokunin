#!/usr/bin/env python3
"""check_r75_routed_repairs.py -- C2 counter for kotoba round 76.

Contract
--------
Frozen predicate (plans/round-76.md, C2):

    `python3 -B verifiers/check_r75_routed_repairs.py --rev <rev>` prints
    `r75 routed repairs closed 4 of 4` and exits 0 only when all four
    repairs below hold at <rev>; at base
    `b7f13f4b39cbd43076a85568adca763a6f674e7a` it prints
    `r75 routed repairs closed 0 of 4` and exits 1.

The four repairs are the ones the round-75 non-author closure routed to round 76
(`corpus/lessons/round-75-verifier-spotcheck.md` § 6 R1-R4, written by the hyaku
closure, never edited by the lane).  Every check reads COMMITTED bytes at `--rev`;
nothing writes to the lane's git index (the corpus-gate re-runs happen in a
`git clone --shared` sandbox under $TMPDIR).

  R1  the round-75 lesson carries an APPENDED correction naming the superseded
      M75-1 text and the Gate reject candidate, asserting the folded-render
      measurement of the r75-tip description (1,022 characters; frontmatter block
      lines 4-18) and citing `corpus/lessons/round-75-verifier-spotcheck.md`;
      AND the receipt `.ufo/waves/round-76/receipts/r1-folded-render.txt` names
      the revision it measured and prints the render length, which THIS counter
      recomputes from that revision's committed `SKILL.md` bytes.

  R2  the receipt `.ufo/waves/round-76/receipts/noharm-at-tip.txt` names the
      round-75 final tip `ac9f29510d3914a6edb97c8dbdb3445cab9141de` on its first
      line, carries the stdout and exit code of BOTH corpus gates reading green
      there, and `LOG.md` § Round 75 cites the receipt path. This counter
      re-runs both gates at that exact revision, compares normalized stdout to
      the transcript, and requires both to exit 0.

  R3  the note `.ufo/waves/round-76/w2-registry-note.md` reconciles
      `.ufo/waves/round-75/w2-results.json` seat `R75Attack28` (named report
      absent; 63 of 64 report files) with a machine-checkable excerpt of the
      results entry, and `LOG.md` § Round 75 cites the note path.

  R4  `LOG.md` § Round 75 carries an appended closing line, after the
      "w2 falsify results pending" text, recording the w2 settlement (64 seats,
      0 dead, 63/64 report files, R75Attack28 phantom per R3).

Render-length convention (frozen by `plans/round-76-addendum-1.md`, committed
`7eed80e9`): the YAML folded scalar under `description: >` is measured with CLIP
chomping -- the folded value keeps its terminal newline -- so the render length
is 1,022 at the r75 tip (`ac9f29510d3914a6edb97c8dbdb3445cab9141de`); the
stripped variant is 1,021.  This counter recomputes the clip-preserving number
from bytes; it never compares against a hardcoded literal without recomputing it,
and it never trusts the receipt's number.

Trust boundary (QUALITY Q33/Q58): R1's text arms are presence-and-quote floors
over the lane's own records (they count named strings, not substance) and are
disclosed as such; R1's number, R2's greenness and R3's counts are RECOMPUTED
from committed bytes or from a sandbox re-run.  The verdict also rests on the base
control (0 of 4) and the self-test.

Exit codes: 0 all four closed · 1 not all closed · 2 usage/environment error.
"""
from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

TOTAL = 4
# The round-76 base: the round-75 closure spot-check tip.  Nothing of R1-R4 exists there.
BASE = "b7f13f4b39cbd43076a85568adca763a6f674e7a"
# The round-75 tip: the revision whose description the R1 correction measures.
R75_TIP = "ac9f29510d3914a6edb97c8dbdb3445cab9141de"

LANE = Path(__file__).resolve().parent.parent
LESSON = "corpus/lessons/round-75.md"
LOG = "LOG.md"
SPOTCHECK = "corpus/lessons/round-75-verifier-spotcheck.md"
R1_RECEIPT = ".ufo/waves/round-76/receipts/r1-folded-render.txt"
NOHARM_RECEIPT = ".ufo/waves/round-76/receipts/noharm-at-tip.txt"
W2_NOTE = ".ufo/waves/round-76/w2-registry-note.md"
W2_RESULTS = ".ufo/waves/round-75/w2-results.json"
W2_DIR = ".ufo/waves/round-75/w2"

# The clip-preserving folded-render length at the r75 tip (recomputed, never trusted).
RENDER_CLIP = 1022
RENDER_STRIPPED = 1021

SHA40_RE = re.compile(r"\b[0-9a-f]{40}\b")
EXIT0_RE = re.compile(r"exit[ _]?(?:code)?[ :=]*0\b", re.IGNORECASE)
ABSENT_WORDS = ("absent", "phantom", "missing", "does not exist", "not present", "no report")

# The superseded texts the R1 correction must name, quoted from the BASE lesson.
M75_TOKENS = ("1,021/1,024 characters", "substantially shorter")
GATE_TOKENS = ("1021-character description size", "materially shorter")


class EnvError(Exception):
    pass


class Repo:
    """Committed-bytes reader over a git tree; the self-test substitutes a fake."""

    def __init__(self, path: Path, rev: str, work_dir: Path | None = None):
        self.path = Path(path)
        self.rev = rev
        self.work_dir = Path(work_dir).resolve() if work_dir is not None else None

    def git(self, *args: str) -> subprocess.CompletedProcess:
        return subprocess.run(["git", "-C", str(self.path), *args],
                              capture_output=True, text=True)

    def show(self, path: str, rev: str | None = None) -> str | None:
        proc = self.git("show", f"{rev or self.rev}:{path}")
        return proc.stdout if proc.returncode == 0 else None

    def exists(self, path: str, rev: str | None = None) -> bool:
        return self.git("cat-file", "-e", f"{rev or self.rev}:{path}").returncode == 0

    def is_ancestor(self, sha: str, of: str | None = None) -> bool:
        return self.git("merge-base", "--is-ancestor", sha, of or self.rev).returncode == 0

    def list_files(self, prefix: str, rev: str | None = None) -> list[str]:
        proc = self.git("ls-tree", "-r", "--name-only", rev or self.rev, "--", prefix.rstrip("/"))
        return [l for l in proc.stdout.splitlines() if l]

    def gates_at(self, rev: str) -> dict:
        """Re-run both corpus gates at `rev` in a shared sandbox clone."""
        if self.work_dir is not None:
            self.work_dir.mkdir(parents=True, exist_ok=True)
        tmp = tempfile.mkdtemp(prefix="k76-c2-gates-",
                               dir=str(self.work_dir) if self.work_dir else None)
        clone = Path(tmp) / "clone"
        try:
            proc = subprocess.run(
                ["git", "clone", "--shared", "-q", "--no-checkout", str(self.path), str(clone)],
                capture_output=True, text=True)
            if proc.returncode != 0:
                raise EnvError("cannot create the sandbox clone: " + proc.stderr.strip())
            top = subprocess.run(["git", "-C", str(clone), "rev-parse", "--show-toplevel"],
                                  capture_output=True, text=True).stdout.strip()
            if Path(top).resolve() != clone.resolve():
                raise EnvError(f"sandbox toplevel {top} is not the sandbox dir {clone}")
            proc = subprocess.run(["git", "-C", str(clone), "checkout", "-q", rev],
                                  capture_output=True, text=True)
            if proc.returncode != 0:
                raise EnvError(f"cannot check out {rev} in the sandbox")
            out = {}
            for key, script in (("integrity", "verify_corpus_integrity.py"),
                                ("independent", "verify_corpus_independent.py")):
                proc = subprocess.run(
                    ["python3", "-B", str(clone / "verifiers" / script),
                     "--repo", str(clone), "--json"],
                    capture_output=True, text=True, timeout=600)
                out[key + "_exit"] = proc.returncode
                # The report transcript and the independent re-run occur in
                # different ephemeral clones; canonicalize only that root.
                out[key + "_out"] = proc.stdout.replace(str(clone), "<repo>")
            return out
        finally:
            shutil.rmtree(tmp, ignore_errors=True)


# --------------------------------------------------------------------- rendering

def folded_description(skill_text: str) -> tuple[str, int, int]:
    """Render the SKILL.md frontmatter `description` folded scalar.

    Returns (rendered_value, first_content_line, last_content_line) with 1-based
    page line numbers.  Clip chomping (the default) keeps the terminal newline, so
    the rendered value is one character longer than its stripped variant.

    Only the shapes the lane's SKILL.md uses are supported: a `description: >`
    block whose content lines all share one indent level and contain no blank
    line.  A more-indented or blank-line-containing block is refused (fail
    closed) rather than silently mis-folded.
    """
    lines = skill_text.split("\n")
    if not lines or lines[0].strip() != "---":
        raise ValueError("SKILL.md has no frontmatter fence")
    key_idx = None
    chomp = "clip"
    for i, ln in enumerate(lines):
        m = re.match(r"^description:\s*>([-+]?)\s*$", ln)
        if m:
            key_idx = i
            chomp = {"": "clip", "-": "strip", "+": "keep"}[m.group(1)]
            break
    if key_idx is None:
        raise ValueError("SKILL.md frontmatter has no `description: >` key")
    content = []
    i = key_idx + 1
    while i < len(lines) and lines[i][:1] in (" ", "\t"):
        content.append(lines[i])
        i += 1
    if not content:
        raise ValueError("SKILL.md description block is empty")
    indents = {len(ln) - len(ln.lstrip(" ")) for ln in content if ln.strip()}
    if len(indents) != 1:
        raise ValueError("SKILL.md description block has mixed indent levels")
    if any(not ln.strip() for ln in content):
        raise ValueError("SKILL.md description block has a blank line")
    base = indents.pop()
    texts = [ln[base:].rstrip() for ln in content]
    value = " ".join(texts)
    if chomp == "clip":
        value += "\n"
    elif chomp == "keep":
        value += "\n"
    return value, key_idx + 2, key_idx + 1 + len(content)


def render_length_at(repo: Repo, rev: str) -> tuple[int, int, int, int]:
    """(clip length, stripped length, first content line, last content line)."""
    text = repo.show("SKILL.md", rev)
    if text is None:
        raise EnvError(f"SKILL.md is absent at {rev}")
    value, first, last = folded_description(text)
    return len(value), len(value.strip()), first, last


# --------------------------------------------------------------------- helpers

def section(text: str, heading: str) -> str:
    m = re.search(rf"(?ms)^## {re.escape(heading)}\b.*?(?=^## |\Z)", text)
    return m.group(0) if m else ""


def _round75_section(repo: Repo) -> str:
    return section(repo.show(LOG) or "", "Round 75")


def _first_rev(text: str) -> str | None:
    for ln in text.splitlines():
        if not ln.strip():
            continue
        m = SHA40_RE.search(ln)
        if m:
            return m.group(0)
    return None


def _sha_after(text: str, marker: str) -> str | None:
    """The first 40-hex after `marker` (case-insensitive), else the first in the text."""
    idx = text.lower().find(marker.lower())
    if idx >= 0:
        m = SHA40_RE.search(text[idx:])
        if m:
            return m.group(0)
    return _first_rev(text)


def _prints_number(text: str, value: int) -> bool:
    """True when the text carries `value` with or without a thousands separator."""
    plain = str(value)
    grouped = f"{value:,}"
    return re.search(r"(?<![\d,])" + re.escape(plain) + r"(?![\d,])", text) is not None \
        or re.search(r"(?<![\d,])" + re.escape(grouped) + r"(?![\d,])", text) is not None


def _names_convention(text: str) -> bool:
    """True when the text names the render convention (clip chomping / newline)."""
    low = text.lower()
    return any(w in low for w in ("clip", "chomp", "newline"))


# --------------------------------------------------------------------- the arms

def _quotes_from(source: str, min_len: int = 30) -> list[str]:
    """Every contiguous window of `source` at least `min_len` long (deduped, capped)."""
    out = []
    for i in range(0, max(0, len(source) - min_len + 1)):
        out.append(source[i:i + min_len])
    return out


def _quotes_any(source: str, target: str, min_len: int = 30) -> bool:
    """True when `target` carries a verbatim window of `source`."""
    return any(w in target for w in _quotes_from(source, min_len))


def r1_correction(repo: Repo) -> list[str]:
    """R1a -- the appended correction in corpus/lessons/round-75.md."""
    now = repo.show(LESSON)
    if now is None:
        return [f"R1: {LESSON} is absent at the measured revision"]
    base = repo.show(LESSON, BASE)
    if base is None:
        return [f"R1: {LESSON} is absent at the pinned base {BASE}"]
    if not now.startswith(base):
        return [f"R1: {LESSON} is not the base file plus an append -- the filed lesson was rewritten"]
    appended = now[len(base):]
    if not appended.strip():
        return [f"R1: {LESSON} carries no appended correction"]
    out = []
    if "M75-1" not in appended:
        out.append("R1: the appended correction does not name M75-1")
    # The superseded M75-1 text: the base lesson's stale-premise mistake row.
    m75_row = ""
    for ln in base.splitlines():
        if ln.startswith("|") and "stale-premise" in ln:
            m75_row = ln
            break
    if not m75_row:
        out.append(f"R1: the base {LESSON} carries no stale-premise mistake row to supersede")
    else:
        missing = [t for t in M75_TOKENS if t not in m75_row]
        if missing:
            out.append(f"R1: the base mistake row lacks the tokens {missing} this arm quotes")
        elif [t for t in M75_TOKENS if t not in appended]:
            out.append(f"R1: the appended correction names no superseded M75-1 text "
                       f"(it must quote {M75_TOKENS})")
        elif not _quotes_any(m75_row, appended):
            out.append("R1: the appended correction quotes no superseded M75-1 text "
                       "(no 30-character verbatim window of the base mistake row)")
    # The Gate reject candidate: the base lesson's Gate paragraph.
    gate = ""
    for ln in base.splitlines():
        if "Candidate reject" in ln:
            gate = ln
            break
    if not gate:
        out.append(f"R1: the base {LESSON} carries no Gate reject candidate")
    else:
        missing = [t for t in GATE_TOKENS if t not in gate]
        if missing:
            out.append(f"R1: the base Gate paragraph lacks the tokens {missing} this arm quotes")
        elif [t for t in GATE_TOKENS if t not in appended]:
            out.append("R1: the appended correction names no Gate reject candidate "
                       f"(it must quote {GATE_TOKENS})")
        elif not _quotes_any(gate, appended):
            out.append("R1: the appended correction quotes no Gate reject candidate "
                       "(no 30-character verbatim window of the base Gate paragraph)")
    if not _prints_number(appended, RENDER_CLIP):
        out.append(f"R1: the appended correction does not assert the {RENDER_CLIP}-character render")
    if not re.search(r"4\s*[\u2013\u2014-]\s*18", appended):
        out.append("R1: the appended correction does not name the frontmatter block lines 4-18")
    if "round-75-verifier-spotcheck.md" not in appended:
        out.append(f"R1: the appended correction does not cite {SPOTCHECK}")
    return out


def r1_receipt(repo: Repo) -> list[str]:
    """R1b -- the render receipt, whose number is recomputed from bytes."""
    text = repo.show(R1_RECEIPT)
    if text is None:
        return [f"R1: {R1_RECEIPT} is not committed at the measured revision"]
    out = []
    rev = _sha_after(text, "measured-rev")
    if rev is None:
        rev = _first_rev(text)
    if rev is None:
        return [f"R1: {R1_RECEIPT} names no measured revision"]
    if not repo.is_ancestor(rev):
        out.append(f"R1: the revision {rev} named by {R1_RECEIPT} is not an ancestor of the "
                   "measured revision")
        return out
    try:
        clip, stripped, first, last = render_length_at(repo, rev)
    except (EnvError, ValueError) as exc:
        return [f"R1: cannot recompute the folded render at {rev}: {exc}"]
    if clip != RENDER_CLIP:
        out.append(f"R1: the recomputed folded render at {rev} is {clip}, not {RENDER_CLIP} "
                   f"(stripped {stripped})")
    if stripped != RENDER_STRIPPED:
        out.append(f"R1: the recomputed stripped render at {rev} is {stripped}, not {RENDER_STRIPPED}")
    if not _prints_number(text, RENDER_CLIP):
        out.append(f"R1: {R1_RECEIPT} does not print {RENDER_CLIP}")
    if not _prints_number(text, RENDER_STRIPPED):
        out.append(f"R1: {R1_RECEIPT} does not print the stripped variant {RENDER_STRIPPED}")
    if not _names_convention(text):
        out.append(f"R1: {R1_RECEIPT} does not name the clip-chomping convention")
    if not re.search(r"4\s*[\u2013\u2014-]\s*18", text):
        out.append(f"R1: {R1_RECEIPT} does not name the frontmatter block lines 4-18")
    if (first, last) != (4, 18):
        out.append(f"R1: the recomputed description block at {rev} is lines {first}-{last}, "
                   "not the recorded 4-18")
    return out


def r2_receipt(repo: Repo) -> list[str]:
    """R2 -- the no-harm receipt; greenness is re-run in a sandbox."""
    text = repo.show(NOHARM_RECEIPT)
    if text is None:
        return [f"R2: {NOHARM_RECEIPT} is not committed at the measured revision"]
    out = []
    lines = text.splitlines()
    first_line = lines[0] if lines else ""
    rev = _first_rev(first_line)
    if rev is None:
        out.append(f"R2: the first line of {NOHARM_RECEIPT} names no tip revision")
    else:
        if rev != R75_TIP:
            out.append(f"R2: {NOHARM_RECEIPT} names {rev}, not the round-75 final tip {R75_TIP}")
        if not repo.is_ancestor(rev):
            out.append(f"R2: the round-75 tip {rev} is not an ancestor of the measured revision")
    gates = ("verify_corpus_integrity.py", "verify_corpus_independent.py")
    # One block per gate: from its command line to the next gate's command line.
    blocks: dict[str, str] = {}
    for i, gate in enumerate(gates):
        idx = text.find(gate)
        if idx < 0:
            out.append(f"R2: {NOHARM_RECEIPT} does not name {gate}")
            continue
        end = len(text)
        for later in gates[i + 1:]:
            j = text.find(later, idx + len(gate))
            if j >= 0:
                end = min(end, j)
        blocks[gate] = text[idx:end]
    for gate, block in blocks.items():
        if not EXIT0_RE.search(block):
            out.append(f"R2: {NOHARM_RECEIPT} records no exit code 0 for {gate}")
        if "$?" in block:
            out.append(f"R2: {NOHARM_RECEIPT} records `$?` rather than a measured exit code for "
                       f"{gate}")
        if "DRIFT" in block:
            out.append(f"R2: {NOHARM_RECEIPT} carries a DRIFT line for {gate}")
        if not any(w in block for w in ("PASS", "checks pass", "conformant", '"verdict"')):
            out.append(f"R2: {NOHARM_RECEIPT} carries no green verdict line for {gate}")
    if rev is not None:
        try:
            rerun = repo.gates_at(rev)
        except EnvError as exc:
            out.append(f"R2: cannot re-run the corpus gates at {rev}: {exc}")
        else:
            for key, gate in (("integrity", "verify_corpus_integrity.py"),
                              ("independent", "verify_corpus_independent.py")):
                if rerun[key + "_exit"] != 0:
                    out.append(f"R2: {gate} re-run at {rev} exits {rerun[key + '_exit']}, not 0")
                if "DRIFT" in rerun[key + "_out"]:
                    out.append(f"R2: {gate} re-run at {rev} reports DRIFT")
                recorded = blocks.get(gate, "")
                expected_stdout = rerun[key + "_out"].strip()
                if not expected_stdout or expected_stdout not in recorded:
                    out.append(f"R2: {gate} transcript in {NOHARM_RECEIPT} does not match "
                               f"the normalized stdout re-run at {rev}")
    return out


def r2_log_citation(repo: Repo) -> list[str]:
    return [] if NOHARM_RECEIPT in _round75_section(repo) else \
        [f"R2: LOG.md § Round 75 does not cite {NOHARM_RECEIPT}"]


def r3_note(repo: Repo) -> list[str]:
    """R3 -- the w2 registry note reconciling seat R75Attack28."""
    note = repo.show(W2_NOTE)
    if note is None:
        return [f"R3: {W2_NOTE} is not committed at the measured revision"]
    out = []
    raw = repo.show(W2_RESULTS)
    if raw is None:
        return [f"R3: {W2_RESULTS} is not committed at the measured revision"]
    try:
        data = json.loads(raw)
    except json.JSONDecodeError as exc:
        return [f"R3: {W2_RESULTS} is not valid JSON: {exc}"]
    results = data.get("results") or []
    entry = next((e for e in results if e.get("name") == "R75Attack28"), None)
    if entry is None:
        return ["R3: w2-results.json carries no seat R75Attack28"]
    if "R75Attack28" not in note:
        out.append("R3: the note does not name seat R75Attack28")
    output = entry.get("output") or ""
    excerpt = None
    for i in range(0, max(0, len(output) - 19)):
        window = output[i:i + 20]
        if window in note:
            excerpt = window
            break
    if excerpt is None:
        out.append("R3: the note carries no machine-checkable excerpt (>=20-character verbatim "
                   "window) of the R75Attack28 results entry")
    if "w2/R75Attack28.md" not in note:
        out.append("R3: the note does not name the absent report path w2/R75Attack28.md")
    files = [p for p in repo.list_files(W2_DIR) if re.search(r"/w2/R75Attack\d+\.md$", p)]
    seats = len(results)
    pairs = {(int(a), int(b)) for a, b in re.findall(r"(\d+)\s*(?:of|/)\s*(\d+)", note)}
    if (len(files), seats) not in pairs:
        out.append(f"R3: the note records no `{len(files)} of {seats}` report-file/seat pair")
    if not any(w in note.lower() for w in ABSENT_WORDS):
        out.append("R3: the note does not record that the named report is absent")
    return out


def r3_log_citation(repo: Repo) -> list[str]:
    return [] if W2_NOTE in _round75_section(repo) else \
        [f"R3: LOG.md § Round 75 does not cite {W2_NOTE}"]


def r4_log_closing(repo: Repo) -> list[str]:
    """R4 -- the appended closing line in LOG.md § Round 75.

    The settlement numbers are RECOMPUTED from the committed w2 results and the
    committed wave tree, so a forged closing line with plausible counts fails.
    """
    log = _round75_section(repo)
    if not log:
        return ["R4: LOG.md carries no `## Round 75` section"]
    marker = "w2 falsify results pending"
    idx = log.lower().find(marker)
    if idx < 0:
        return [f"R4: LOG.md § Round 75 no longer carries the `{marker}` text"]
    raw = repo.show(W2_RESULTS)
    if raw is None:
        return [f"R4: {W2_RESULTS} is not committed at the measured revision"]
    try:
        results = json.loads(raw).get("results") or []
    except json.JSONDecodeError as exc:
        return [f"R4: {W2_RESULTS} is not valid JSON: {exc}"]
    seats = len(results)
    dead = sum(1 for e in results if not (e.get("output") or "").strip())
    files = [p for p in repo.list_files(W2_DIR) if re.search(r"/w2/R75Attack\d+\.md$", p)]
    tail = log[idx + len(marker):]
    lines = [ln for ln in tail.splitlines() if ln.strip()]
    pair = (len(files), seats)
    pair_line = next((ln for ln in lines
                      if (str(pair[0]), str(pair[1])) in {(str(a), str(b))
                                                        for a, b in re.findall(r"(\d+)\s*(?:of|/)\s*(\d+)", ln)}),
                     None)
    dead_line = next((ln for ln in lines if re.search(rf"\b{dead}\s+dead\b", ln, re.IGNORECASE)),
                     None)
    seat_line = next((ln for ln in lines if "r75attack28" in ln.lower()), None)
    out = []
    if pair_line is None:
        out.append(f"R4: LOG.md § Round 75 records no `{pair[0]} of {pair[1]}` report-file/seat pair "
                   "after the `w2 falsify results pending` text")
    if dead_line is None:
        out.append(f"R4: LOG.md § Round 75 records no `{dead} dead` seat count after the "
                   "`w2 falsify results pending` text")
    if seat_line is None:
        out.append("R4: LOG.md § Round 75 records no R75Attack28 settlement after the "
                   "`w2 falsify results pending` text")
    if out:
        return out
    # The settlement facts must sit together, not 40 lines apart.
    idxs = [lines.index(pair_line), lines.index(dead_line), lines.index(seat_line)]
    if max(idxs) - min(idxs) > 3:
        out.append("R4: the Round 75 closing settlement line names R75Attack28 and the "
                   "seat/report/dead counts more than three lines apart")
    return out


REPAIRS = (
    ("R1", (r1_correction, r1_receipt)),
    ("R2", (r2_receipt, r2_log_citation)),
    ("R3", (r3_note, r3_log_citation)),
    ("R4", (r4_log_closing,)),
)


def check(repo: Repo) -> tuple[int, list[str]]:
    """Return (number of closed repairs, findings)."""
    findings: list[str] = []
    for _label, arms in REPAIRS:
        for fn in arms:
            findings.extend(fn(repo))
    labels = {"R1": 0, "R2": 0, "R3": 0, "R4": 0}
    for f in findings:
        labels[f.split(":", 1)[0]] = 1
    closed = sum(1 for v in labels.values() if not v)
    return closed, findings


# --------------------------------------------------------------------- self-test

class FakeRepo(Repo):
    """Dict-backed committed bytes; no git, no subprocess."""

    def __init__(self, files: dict[str, str], rev: str = "f" * 40,
                 ancestors: set[str] | None = None, gates: dict | None = None,
                 tree: list[str] | None = None, base_files: dict[str, str] | None = None):
        super().__init__(Path("/nonexistent"), rev)
        self.files = files
        self.base_files = base_files or {}
        self.ancestors = ancestors if ancestors is not None else set()
        self.gates = gates or {}
        self.tree = tree or []

    def show(self, path, rev=None):
        if rev == BASE:
            return self.base_files.get(path, self.files.get(path))
        return self.files.get(path)

    def exists(self, path, rev=None):
        return path in self.files

    def is_ancestor(self, sha, of=None):
        return sha in self.ancestors or sha == self.rev

    def list_files(self, prefix, rev=None):
        p = prefix.rstrip("/")
        return [t for t in self.tree if t.startswith(p + "/")]

    def gates_at(self, rev):
        return self.gates


def _skill_bytes(clip: int = RENDER_CLIP) -> str:
    """A SKILL.md whose clip-preserving folded render is `clip` characters.

    The block spans page lines 4-18 (the `description: >` marker sits on line 3),
    so the recomputed block range matches the recorded one.
    """
    filler = "x"
    # 15 content lines joined by 14 single spaces; the clip newline adds the last char.
    per = (clip - 1 - 14) // 15
    rest = (clip - 1 - 14) - per * 15
    lines = []
    for i in range(15):
        n = per + (1 if i < rest else 0)
        lines.append("  " + filler * n)
    return ("---\nname: kotoba-shokunin\ndescription: >\n"
            + "\n".join(lines) + "\n---\n\n# kotoba-shokunin\n")


def _honest() -> dict:
    rev = "a" * 40
    gate_line = ("Source opened this round: https://agentskills.io/skill-creation/optimizing-"
                 "descriptions.md (2026-10-27). Candidate reject: any claim that the 1021-character "
                 "description size reported in `considerthese/2026-10-26.md` remains current; "
                 "current frontmatter is materially shorter.\n")
    m75_row = ("| stale-premise | `considerthese/2026-10-26.md:17` says description is 1,021/1,024 "
               "characters; current committed SKILL frontmatter (master 65a5c7a, lines 3–18) is "
               "substantially shorter. | Q67 does not catch stale values | Freeze each proposed "
               "target from the current committed bytes. |\n")
    lesson_base = ("# Round 75 lessons — kotoba\n\n## Gate\n\n" + gate_line +
                   "\n## Mistakes\n\n| class | evidence pointer | captured-by | fix |\n"
                   "|---|---|---|---|\n" + m75_row)
    appended = ("\n## Correction (appended, round 76 — R1)\n\n"
                "**Superseded text — M75-1 and the Gate reject candidate.** The mistake row said:\n\n"
                "    " + m75_row.strip() + "\n\n"
                "The Gate said: \"Candidate reject: any claim that the 1021-character description size "
                "reported in `considerthese/2026-10-26.md` remains current; current frontmatter is "
                "materially shorter.\"\n\n"
                "Both premises are false: the description renders 1,022 characters, frontmatter "
                "block lines 4–18. Authority: "
                "corpus/lessons/round-75-verifier-spotcheck.md § 6 R1.\n")
    log = ("# kotoba-shokunin — Iteration Log\n\n## Round 74\n\n## Round 75 — C1 depth\n\n"
           "- **Pointer:** `.ufo/waves/round-75/w1/`; w2 falsify results pending.\n"
           f"- **Correction:** `{NOHARM_RECEIPT}`; `{W2_NOTE}`.\n"
           "- **Closing:** w2 settled 64 of 64 seats, 0 dead, 63 of 64 report files; "
           "R75Attack28 is a phantom per the registry note.\n")
    seats = [{"name": "R75Attack%02d" % i, "agent": "reviewer",
              "output": "verdict text for seat %d" % i, "note": None}
             for i in range(1, 65) if i != 28]
    seats.append({"name": "R75Attack28", "agent": "reviewer",
                  "output": "R75Facet28 survived with a material qualification: the advice is "
                            "misleading if read as odd runs OR deduplication; written report "
                            "w2/R75Attack28.md",
                  "note": None})
    results = {"lane": "kotoba-shokunin", "round": 75, "wave": "w2", "seats": 64,
               "results": seats}
    entry = next(e for e in seats if e["name"] == "R75Attack28")
    excerpt = entry["output"][:40]
    files = {
        LESSON: lesson_base + appended,
        LOG: log,
        "SKILL.md": _skill_bytes(),
        R1_RECEIPT: (f"measured-rev: {rev}\n"
                     f"folded render (clip chomping, terminal newline kept): {RENDER_CLIP} characters\n"
                     f"stripped render: {RENDER_STRIPPED} characters\n"
                     "frontmatter block lines 4-18\nexit=0\n"),
        NOHARM_RECEIPT: (f"tip: {R75_TIP}\n"
                         "$ python3 -B verifiers/verify_corpus_integrity.py --json\n"
                         "PASS corpus.index.tracked_files ...\n"
                         "exit=0\n"
                         "$ python3 -B verifiers/verify_corpus_independent.py --json\n"
                         "PASS corpus.index.unindexed ...\n"
                         "exit=0\n"),
        W2_NOTE: (f"# w2 registry note — kotoba round 75\n\n"
                  f"Seat R75Attack28 names a report that is absent: w2/R75Attack28.md. "
                  f"Excerpt: \"{excerpt}\".\n"
                  "64 seats; 63 of 64 report files present; the named report is absent.\n"),
        W2_RESULTS: json.dumps(results, indent=1),
    }
    tree = [f"{W2_DIR}/R75Attack%02d.md" % i for i in range(1, 65) if i != 28]
    gates = {"integrity_exit": 0,
             "integrity_out": "PASS corpus.index.tracked_files ...\n",
             "independent_exit": 0,
             "independent_out": "PASS corpus.index.unindexed ...\n"}
    return dict(files=files, rev=rev, ancestors={rev, R75_TIP}, gates=gates, tree=tree,
                base_files={LESSON: lesson_base, "SKILL.md": _skill_bytes()})


def _drop_quoted_excerpt(note: str) -> str:
    """Remove the quoted excerpt and the absent-report path token from a note."""
    out = re.sub(r"Excerpt: \"[^\"]*\"", "Excerpt: (removed)", note)
    return out.replace("w2/R75Attack28.md", "w2/R75Attack-28.md")
def _fixture_tree(lane: Path, tmp: Path) -> tuple[Path, str]:
    """Materialize the r75 gate evidence and the four routed repairs."""
    clone = tmp / "clone"
    proc = subprocess.run(["git", "clone", "--shared", "-q", "--no-checkout", str(lane), str(clone)],
                          capture_output=True, text=True)
    if proc.returncode != 0:
        raise EnvError("cannot create the fixture clone: " + proc.stderr.strip())
    top = subprocess.run(["git", "-C", str(clone), "rev-parse", "--show-toplevel"],
                         capture_output=True, text=True).stdout.strip()
    if Path(top).resolve() != clone.resolve():
        raise EnvError(f"fixture toplevel {top} is not the fixture dir {clone}")
    proc = subprocess.run(["git", "-C", str(clone), "checkout", "-q", BASE],
                          capture_output=True, text=True)
    if proc.returncode != 0:
        raise EnvError("cannot check out the base in the fixture: " + proc.stderr.strip())

    # The r75 closure spot-check is already tracked at BASE but was not indexed
    # or included in the corpus baseline. Repair those observed counts before
    # using this revision as the no-harm measurement tip.
    readme_path = clone / "corpus/README.md"
    readme = readme_path.read_text(encoding="utf-8")
    if "Round-75 verifier spot-check (closure)" not in readme:
        row = ("| Round-75 verifier spot-check (closure) | "
               "`lessons/round-75-verifier-spotcheck.md` | "
               "Closure-authored outside review; indexed in round 76. |")
        if "\n## Frontier" not in readme:
            raise EnvError("README coverage map has no ## Frontier insertion anchor")
        readme = readme.replace("\n## Frontier", "\n" + row + "\n\n## Frontier", 1)
        readme_path.write_text(readme, encoding="utf-8")
    baseline_path = clone / "verifiers/corpus-baseline.json"
    baseline = json.loads(baseline_path.read_text(encoding="utf-8"))
    baseline["checks"]["corpus.index.tracked_files"]["expect"] = 145
    baseline["checks"]["corpus.pointers.report_total"]["expect"] = 101
    baseline["checks"]["corpus.pointers.commit_total"]["expect"] = 44
    baseline["measured_against"].update({
        "head": BASE[:7],
        "head_subject": "round-75 closure spot-check",
        "git_status": "r75 closure spot-check added without README index/baseline refresh",
        "command": "python3 -B verifiers/verify_corpus_integrity.py --no-baseline --json",
        "note": "Round-76 base correction: index the r75 closure spot-check and re-record "
                "tracked_files=145, report_total=101, commit_total=44 from the observed base bytes."
    })
    baseline_path.write_text(json.dumps(baseline, indent=1) + "\n", encoding="utf-8")
    proc = subprocess.run(
        ["git", "-C", str(clone), "add", "corpus/README.md", "verifiers/corpus-baseline.json"],
        capture_output=True, text=True)
    if proc.returncode != 0:
        raise EnvError("cannot stage measurement state: " + proc.stderr.strip())
    proc = subprocess.run(
        ["git", "-C", str(clone), "-c", "user.name=fixture", "-c",
         "user.email=fixture@shokunin.local", "commit", "-q", "-m", "fixture: correct base corpus state"],
        capture_output=True, text=True)
    if proc.returncode != 0:
        raise EnvError("cannot commit measurement state: " + proc.stderr.strip())
    measured = subprocess.run(["git", "-C", str(clone), "rev-parse", "HEAD"],
                              capture_output=True, text=True).stdout.strip()
    measured_repo = Repo(clone, measured)
    base_gate = measured_repo.gates_at(measured)
    if base_gate["integrity_exit"] != 0 or base_gate["independent_exit"] != 0:
        raise EnvError(f"fixture measurement state is not gate-green: {base_gate}")
    gate = measured_repo.gates_at(R75_TIP)

    base_lesson = (clone / LESSON).read_text(encoding="utf-8")
    base_log = (clone / LOG).read_text(encoding="utf-8")
    results = json.loads((clone / W2_RESULTS).read_text(encoding="utf-8"))
    entry = next(e for e in results["results"] if e.get("name") == "R75Attack28")
    excerpt = (entry.get("output") or "")[:40]
    m75_row = next(l for l in base_lesson.splitlines() if l.startswith("|") and "stale-premise" in l)
    gate_line = next(l for l in base_lesson.splitlines() if "Candidate reject" in l)
    correction = ("\n## Correction (appended, round 76 — R1 of the round-75 verifier spot-check)\n\n"
                  "**Superseded text — M75-1 and the Gate reject candidate.** The mistake row said:\n\n"
                  "    " + m75_row + "\n\n"
                  "The Gate said: \"" + gate_line[gate_line.index("Candidate reject:"):].strip() + "\"\n\n"
                  "Both premises are false: the description renders 1,022 characters, frontmatter "
                  "block lines 4–18. Authority: corpus/lessons/round-75-verifier-spotcheck.md § 6 R1.\n")
    (clone / LESSON).write_text(base_lesson + correction, encoding="utf-8")
    closing = (f"- **Correction:** `{NOHARM_RECEIPT}`; `{W2_NOTE}`.\n"
               "- **Closing:** w2 settled 64 of 64 seats, 0 dead, 63 of 64 report files; "
               "R75Attack28 is a phantom per the registry note.\n")
    (clone / LOG).write_text(base_log + closing, encoding="utf-8")
    integrity_out = gate["integrity_out"]
    independent_out = gate["independent_out"]
    for rel, body in (
        (R1_RECEIPT,
         f"measured-rev: {R75_TIP}\n"
         f"folded render (clip chomping, terminal newline kept): {RENDER_CLIP} characters\n"
         f"stripped render: {RENDER_STRIPPED} characters\n"
         "frontmatter block lines 4-18\nexit=0\n"),
        (NOHARM_RECEIPT,
         f"tip: {R75_TIP}\n"
         "$ python3 -B verifiers/verify_corpus_integrity.py --json\n"
         + integrity_out + "exit=0\n"
         "$ python3 -B verifiers/verify_corpus_independent.py --json\n"
         + independent_out + "exit=0\n"),
        (W2_NOTE,
         "# w2 registry note — kotoba round 75\n\n"
         f"Seat R75Attack28 names a report that is absent: w2/R75Attack28.md. Excerpt: \"{excerpt}\".\n"
         "64 seats; 63 of 64 report files present; the named report is absent.\n"),
    ):
        path = clone / rel
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(body, encoding="utf-8")
    proc = subprocess.run(["git", "-C", str(clone), "add", "-A"],
                          capture_output=True, text=True)
    if proc.returncode != 0:
        raise EnvError("cannot stage repair fixture: " + proc.stderr.strip())
    proc = subprocess.run(
        ["git", "-C", str(clone), "-c", "user.name=fixture", "-c",
         "user.email=fixture@shokunin.local", "commit", "-q", "-m", "fixture: honest r76 repairs"],
        capture_output=True, text=True)
    if proc.returncode != 0:
        raise EnvError("fixture commit failed: " + proc.stderr.strip())
    head = subprocess.run(["git", "-C", str(clone), "rev-parse", "HEAD"],
                          capture_output=True, text=True).stdout.strip()
    return clone, head


def _real_git_arm(lane: Path, work_dir: Path | None = None) -> tuple[int, int]:
    """Drive main() on a satisfying fixture and on a token-dump fixture.

    Returns (failures, assertions) contributed by this arm.
    """
    failures = 0
    assertions = 0
    script = Path(__file__).resolve()
    if work_dir is not None:
        work_dir.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix="k76-c2-gitarm-",
                                     dir=str(work_dir) if work_dir else None) as tmp_s:
        tmp = Path(tmp_s)
        try:
            clone, head = _fixture_tree(lane, tmp)
        except (EnvError, StopIteration) as exc:
            print(f"FAIL real-git arm: cannot build the fixture: {exc}", file=sys.stderr)
            return 1, 1
        proc = subprocess.run(["python3", "-B", str(script), "--repo", str(clone), "--rev", head],
                              capture_output=True, text=True, timeout=1200)
        assertions += 1
        if proc.returncode != 0 or f"r75 routed repairs closed {TOTAL} of {TOTAL}" not in proc.stdout:
            print(f"FAIL real-git arm: honest fixture did not close {TOTAL} of {TOTAL} "
                  f"(exit {proc.returncode}); {proc.stdout}", file=sys.stderr)
            failures += 1
        else:
            print(f"PASS real-git arm: honest fixture closes {TOTAL} of {TOTAL}")
        # Token-dump fixture: the right filenames, empty content.
        for rel in (R1_RECEIPT, NOHARM_RECEIPT, W2_NOTE):
            (clone / rel).write_text("", encoding="utf-8")
        subprocess.run(["git", "-C", str(clone), "-c", "user.name=kotoba", "-c",
                        "user.email=kotoba@shokunin.local", "commit", "-qam", "token dump"],
                       capture_output=True, text=True)
        head2 = subprocess.run(["git", "-C", str(clone), "rev-parse", "HEAD"],
                               capture_output=True, text=True).stdout.strip()
        proc = subprocess.run(["python3", "-B", str(script), "--repo", str(clone), "--rev", head2],
                              capture_output=True, text=True, timeout=1200)
        assertions += 1
        if proc.returncode == 0:
            print("FAIL real-git arm: token-dump fixture closed all repairs", file=sys.stderr)
            failures += 1
        else:
            print(f"PASS real-git arm: token-dump fixture rejected (exit {proc.returncode})")
    return failures, assertions


def selftest() -> tuple[int, int]:
    """The dict-backed battery.  Returns (failures, assertions)."""
    failures = 0
    assertions = 0

    def run(world: dict):
        return check(FakeRepo(**world))

    honest = _honest()
    n, f = run(honest)
    assertions += 1
    if n != TOTAL:
        print(f"FAIL honest world: closed {n} of {TOTAL}; {f}", file=sys.stderr)
        failures += 1
    else:
        print(f"PASS honest world: closed {TOTAL} of {TOTAL}")

    def edit(path, old, new):
        def apply(w):
            if old not in w["files"].get(path, ""):
                raise AssertionError(f"self-test anchor missing in {path}: {old!r}")
            w["files"][path] = w["files"][path].replace(old, new)
        return apply

    def drop(path):
        def apply(w):
            w["files"].pop(path, None)
        return apply

    def edit_appended(path, old, new):
        """Edit only the appended tail of a file (never its base prefix)."""
        def apply(w):
            text = w["files"][path]
            base = w["base_files"].get(path, "")
            head, _, tail = text.partition(base) if base else (text, "", "")
            if old not in tail:
                raise AssertionError(f"self-test anchor missing in the append of {path}: {old!r}")
            w["files"][path] = head + base + tail.replace(old, new)
        return apply

    broken = {
        "R1 receipt names no measured revision": edit(R1_RECEIPT, "measured-rev: " + "a" * 40,
                                                      "measured-rev: "),
        "R1 receipt prints no render length": edit(R1_RECEIPT, "1022 characters", "many characters"),
        "R1 receipt prints no stripped variant": edit(R1_RECEIPT, "stripped render: 1021", "stripped: n/a"),
        "R1 receipt names no convention": edit(R1_RECEIPT, "clip chomping, terminal newline kept",
                                              "some other rule"),
        "R1 correction names no superseded text": edit_appended(LESSON, "1,021/1,024 characters",
                                                                "a number"),
        "R1 correction names no Gate reject candidate": edit_appended(LESSON, "materially shorter",
                                                                      "a different length"),
        "R1 correction asserts no render length": edit_appended(LESSON, "1,022 characters",
                                                                "some characters"),
        "R1 correction cites no spot-check": edit_appended(
            LESSON, "corpus/lessons/round-75-verifier-spotcheck.md", "the closure"),
        "R1 lesson rewritten (not appended)": edit(LESSON, "# Round 75 lessons — kotoba",
                                                   "# Round 75 lessons — kotoba (rewritten)"),
        "R2 receipt names no tip revision": edit(NOHARM_RECEIPT, "tip: " + R75_TIP, "tip:"),
        "R2 receipt names a stale ancestor, not the measured tip": edit(
            NOHARM_RECEIPT, "tip: " + R75_TIP, "tip: " + BASE),
        "R2 copied green stdout does not match the sandbox rerun": edit(
            NOHARM_RECEIPT, "PASS corpus.index.tracked_files", "PASS corpus.index.other"),
        "R2 receipt carries no exit code": edit(NOHARM_RECEIPT, "exit=0", "exit=?"),
        "R2 gates read red at the named revision": lambda w: w["gates"].update(
            {"integrity_exit": 1, "integrity_out": "DRIFT corpus.index.tracked_files\n"}),
        "R2 LOG does not cite the receipt": edit(LOG, NOHARM_RECEIPT, ".ufo/waves/round-76/receipts/other.txt"),
        "R3 note absent": drop(W2_NOTE),
        "R3 note carries no excerpt": lambda w: w["files"].__setitem__(
            W2_NOTE, _drop_quoted_excerpt(w["files"][W2_NOTE])),
        "R3 note names no seat": edit(W2_NOTE, "R75Attack28", "a seat"),
        "R3 note records no counts": edit(W2_NOTE, "64 seats; 63 of 64 report files", "some seats"),
        "R3 LOG does not cite the note": edit(LOG, W2_NOTE, ".ufo/waves/round-76/other-note.md"),
        "R4 closing line absent": edit(LOG, "- **Closing:** w2 settled 64 of 64 seats, 0 dead, "
                                  "63 of 64 report files; R75Attack28 is a phantom per the registry note.\n", ""),
        "R4 closing line precedes the pending text": lambda w: w["files"].__setitem__(
            LOG,
            w["files"][LOG].replace(
                "- **Pointer:** `.ufo/waves/round-75/w1/`; w2 falsify results pending.\n"
                "- **Correction:**",
                "- **Closing:** w2 settled 64 of 64 seats, 0 dead, 63 of 64 report files; "
                "R75Attack28 is a phantom.\n"
                "- **Pointer:** `.ufo/waves/round-75/w1/`; w2 falsify results pending.\n"
                "- **Correction:**")
            .replace(
                "- **Closing:** w2 settled 64 of 64 seats, 0 dead, 63 of 64 report files; "
                "R75Attack28 is a phantom per the registry note.\n", "")),
    }
    for name, fn in broken.items():
        world = _honest()
        try:
            fn(world)
        except AssertionError as exc:
            print(f"FAIL broken world anchor missing: {name} ({exc})", file=sys.stderr)
            failures += 1
            assertions += 1
            continue
        n, _ = run(world)
        assertions += 1
        if n == TOTAL:
            print(f"FAIL broken world survived: {name} -> closed {n}", file=sys.stderr)
            failures += 1
        else:
            print(f"PASS broken world rejected: {name}")

    # Token-dump world: right filenames, empty or forged content.
    world = _honest()
    world["files"][R1_RECEIPT] = ""
    world["files"][NOHARM_RECEIPT] = ""
    world["files"][W2_NOTE] = ""
    n, _ = run(world)
    assertions += 1
    if n == TOTAL:
        print("FAIL token-dump world survived: closed " + str(n), file=sys.stderr)
        failures += 1
    else:
        print(f"PASS token-dump world rejected: closed {n} of {TOTAL}")

    # Forged-numbers world: the receipt claims a green run at a revision whose
    # committed bytes do not read green.
    world = _honest()
    world["gates"] = {"integrity_exit": 1, "integrity_out": "DRIFT\n",
                      "independent_exit": 1, "independent_out": "DRIFT\n"}
    n, _ = run(world)
    assertions += 1
    if n == TOTAL:
        print("FAIL forged-green world survived", file=sys.stderr)
        failures += 1
    else:
        print(f"PASS forged-green world rejected: closed {n} of {TOTAL}")

    return failures, assertions


def selftest_with_git(lane: Path, work_dir: Path | None = None) -> int:
    """The full self-test: the dict-backed battery plus the real-git arm."""
    failures, assertions = selftest()
    git_failures, git_assertions = _real_git_arm(lane, work_dir)
    failures += git_failures
    assertions += git_assertions
    print(f"self-test: {failures} failure(s) over {assertions} assertions")
    return 1 if failures else 0


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="C2 counter for kotoba round 76")
    ap.add_argument("--rev", default=None, help="measured revision")
    ap.add_argument("--repo", default=str(LANE))
    ap.add_argument("--work", default=None,
                    help="scratch directory for sandbox clones (defaults to TMPDIR)")
    ap.add_argument("--self-test", action="store_true")
    args = ap.parse_args(argv)
    work_dir = Path(args.work).expanduser().resolve() if args.work else None
    if work_dir is not None:
        work_dir.mkdir(parents=True, exist_ok=True)
    if args.self_test:
        return selftest_with_git(Path(args.repo), work_dir)
    repo_path = Path(args.repo)
    try:
        if not args.rev:
            raise EnvError("--rev <revision> is required")
        proc = subprocess.run(["git", "-C", str(repo_path), "rev-parse", "--verify", "--quiet",
                               f"{args.rev}^{{commit}}"], capture_output=True, text=True)
        if proc.returncode != 0:
            raise EnvError(f"unknown revision {args.rev}")
        sha = proc.stdout.strip()
        repo = Repo(repo_path, sha, work_dir)
        per_repair: list[tuple[str, list[str]]] = []
        findings: list[str] = []
        for label, arms in REPAIRS:
            arm_findings: list[str] = []
            for fn in arms:
                arm_findings.extend(fn(repo))
            per_repair.append((label, arm_findings))
            findings.extend(arm_findings)
        closed = sum(1 for _label, f in per_repair if not f)
    except EnvError as exc:
        print(f"environment error: {exc}", file=sys.stderr)
        return 2
    print(f"measured-rev: {sha}")
    for label, arm_findings in per_repair:
        print(f"{label}: {'open' if arm_findings else 'closed'}")
    print(f"r75 routed repairs closed {closed} of {TOTAL}")
    for f in findings:
        print(f"  - {f}")
    return 0 if closed == TOTAL else 1


if __name__ == "__main__":
    sys.exit(main())
