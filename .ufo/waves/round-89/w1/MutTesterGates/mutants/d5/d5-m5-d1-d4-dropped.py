#!/usr/bin/env python3
"""Round-89 counter for the five round-86 routed defects (C2, D5 v3).

Frozen predicate (plans/round-89.md § C2, carried verbatim):

    python3 -B verifiers/check_r86_routed_repairs_v3.py --base-receipt <receipt.json> [--root <dir>]
        -> prints "r86 routed defects closed N of 5" and "instance drift K",
           exit 0 iff N == 5 AND K == 0 AND the pinned snapshot digests match;
           exit 1 otherwise, naming the first failing leg (d5i | d5ii | d5iii | snapshot_tampered | d1..d4);
           exit 2 = could-not-evaluate.

D1-D4 carry the round-87 items unchanged in meaning, reimplemented here.
v2 imported them from the byte-frozen round-87 counter (v2:10-12) and bound
them at v2:172-173 (`ITEMS = (("d1", r87.check_d1), ("d2", r87.check_d2),
("d3", r87.check_d3), ("d4", r87.check_d4), ("d5", check_d5))`); v3 is
self-contained.  Per check, the carried meaning and its source line:

  d1  the round-86 tip receipts carry exit=0 + their expected line and name a
      revision that resolves, is an ancestor of <rev> and carries the same
      instrument blobs; the two instruments are blob-identical between the
      r86 landing 04647b0f and <rev>   [r87 check_d1,
      verifiers/check_r86_routed_repairs.py:322]
  d2  the validator sentence "planner/distiller/labrat/Main are frozen-
      topology seats and can never be swarm lanes." is carried verbatim by
      plans/round-87.md or corpus/lessons/round-87.md at <rev>; the external
      validator file itself carries it and its SWARM_ROLES set literal parses
      without "planner"                    [r87 check_d2, r87:350]
  d3  corpus/lessons/round-87.md ## Gate holds >= 1 reject row whose reason
      is >= 8 words                        [r87 check_d3, r87:379]
  d4  plans/round-87.md names the kill boundary "after the first candidate
      score" verbatim                      [r87 check_d4, r87:401]

Every carried check reads <rev>'s committed bytes only (`git show`, never a
second working tree inside the lane; Q58).  In v3 <rev> is the HEAD of the
measured root, so a scratch world clone of the lane carrying one world commit
on top is measured at its own HEAD exactly as the lane is measured at its tip.

D5 is the instance-level successor of v2's name-set gate.  v2 read (i)
name-set identity and (ii) name monotonicity (v2:122-129), so an added
integrity finding under an already-red name was invisible -- the r88 frozen
control w_added_red could not fail it (v2 self-test arm w_added_red reads the
added-red world as PASS; corpus/lessons/round-88-verifier-spotcheck.md routed
defect 4).  v3 D5 has four legs, all measured in the root's working tree with
cwd = the root (Q79 location discipline; the gate never gives the lane a
second working tree and never writes anywhere but its receipt):

  d5i    identity: the measured check-name list equals the receipt's AND the
         root's own verifiers/verify_corpus_integrity.py --self-test exits 0
         at the root.  Exit-code reading: the plan's D5(i) sentence makes the
         self-test exit 0 a d5i conjunct, so a self-test that RUNS and exits
         nonzero is a NAMED d5i failure (exit 1), never silent; only a
         self-test that cannot be run at all (OSError/timeout) is
         could-not-evaluate (exit 2).
  d5ii   name monotone: the measured DRIFT name set is a subset of the
         receipt's (a new red name fails; a healed red passes).
  d5iii  instance non-growth: for every check name the measured observed
         value is <= the receipt's value.  "instance drift K" counts the
         names that grew past their receipt value (or have no receipt value
         to compare against); d5iii holds iff K == 0.
  snapshot_tampered: the sha256 of the root's working-tree
         verifiers/verify_corpus_integrity.py and verifiers/corpus-baseline.json
         equal the receipt's pinned digests -- a re-recorded baseline cannot
         green D5.

Legs are evaluated in the fixed order d1, d2, d3, d4, d5i, d5ii, d5iii,
snapshot_tampered and exit 1 names the FIRST failing leg.  Anything a leg
cannot evaluate (missing/malformed receipt, integrity run exit 2/3, non-JSON
output, duplicate check names, non-integer observed values, unreadable
digests) is exit 2 could-not-evaluate, never a silent verdict.

--write-base-receipt <path> measures THE LANE (this file's grandparent
directory; the integrity run has cwd = the lane root): it pins the lane HEAD
revision, the sha256 of the working-tree verifiers/verify_corpus_integrity.py
and verifiers/corpus-baseline.json, and the full --json observation dict (all
nine checks with live values), then writes the JSON receipt.  It refuses to
pin anything but nine names (the v2:54 NAME_COUNT anchor v2:122-124 built
into identity).  The L1 writes the lane's base receipt at the freeze commit;
this gate writes a base receipt only at the path it is given.

Usage:
  check_r86_routed_repairs_v3.py --write-base-receipt <path>
  check_r86_routed_repairs_v3.py --base-receipt <receipt> [--root <dir>]
                                 [--print-observation] [--work <dir>]
  check_r86_routed_repairs_v3.py --self-test

--print-observation (comparison mode) prints the measured observation dict as
one JSON document before the leg lines; the exit ladder is unchanged.

Exit 0 clean (5 of 5, instance drift 0, digests match), 1 a named leg fails,
2 could not evaluate.  Python stdlib only; honours TMPDIR and --work; no
hard-coded temp paths; no network.
"""
from __future__ import annotations

import argparse
import hashlib
import io
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
LANE = HERE.parent
TARGET = 5
INTEGRITY = "verifiers/verify_corpus_integrity.py"
BASELINE = "verifiers/corpus-baseline.json"
NAME_COUNT = 9          # v2:54 NAME_COUNT anchor (v2:122-124 identity)
GIT_TIMEOUT = 300
SCHEMA = "kotoba.d5v3-base-receipt/1"

# --- carried round-87 constants (v2:45-52 re-exported r87:102-126) ---------
LANDING_REV = "04647b0f715ff3c4f314b0d8f03dea28bc453688"
CATALOGUE_RECEIPT = ".ufo/waves/round-86/receipts/tip-catalogue.txt"
REGISTRY_RECEIPT = ".ufo/waves/round-86/receipts/tip-registry.txt"
CATALOGUE_LINE = "omp catalogue lines reproduced 215 of 215"
REGISTRY_LINE = "gate registry rows conformant 67 of 67"
INSTRUMENTS = ("verifiers/check_omp_catalogue_repro.py",
               "verifiers/check_gate_registry.py")
PLAN = "plans/round-87.md"
LESSON = "corpus/lessons/round-87.md"
FROZEN_SENTENCE = ("planner/distiller/labrat/Main are frozen-topology seats "
                   "and can never be swarm lanes.")
KILL_BOUNDARY = "after the first candidate score"
OMP_VALIDATOR = Path(os.path.expanduser(
    "~/Projects/ufo-fsd-alpha/scripts/ufo-swarm-wave.mjs"))
MIN_READER = 7          # shortest hex token that can name a revision
MIN_REASON_WORDS = 8


class Unevaluable(Exception):
    """The gate cannot reach a verdict (exit 2)."""


# --- git plumbing (carried from r87:133-157, meaning unchanged) -----------

def _git(repo: Path, *args: str) -> subprocess.CompletedProcess:
    try:
        return subprocess.run(["git", "-C", str(repo), *args],
                              capture_output=True, text=True,
                              timeout=GIT_TIMEOUT)
    except (OSError, subprocess.SubprocessError) as exc:
        raise Unevaluable("git %s: %s" % (" ".join(args[:2]), exc)) from exc


def _show(repo: Path, rev: str, path: str) -> str | None:
    proc = _git(repo, "show", "%s:%s" % (rev, path))
    return proc.stdout if proc.returncode == 0 else None


def _blob_id(repo: Path, rev: str, path: str) -> str | None:
    proc = _git(repo, "rev-parse", "--verify", "-q", "%s:%s" % (rev, path))
    return proc.stdout.strip() if proc.returncode == 0 else None


def _resolve(repo: Path, rev: str) -> str:
    proc = _git(repo, "rev-parse", "--verify", "-q", "%s^{commit}" % rev)
    if proc.returncode != 0:
        raise Unevaluable("revision %r does not resolve to a commit" % rev)
    return proc.stdout.strip()


# --- text model (carried from r87:162-264, meaning unchanged) -------------

def _norm(text: str) -> str:
    """Collapse whitespace runs and drop backticks: the lane's records wrap
    prose at ~78 columns and quote the frozen sentences in backticks, so the
    word sequence is what must be verbatim, not the line breaks."""
    return re.sub(r"\s+", " ", text.replace("`", ""))


def _words(text: str) -> int:
    return sum(1 for tok in text.split() if re.search(r"[0-9A-Za-z]", tok))


def _carries_sentence(text: str) -> bool:
    return FROZEN_SENTENCE in _norm(text)


def _section(text: str, name: str) -> str | None:
    """Body of a level-2 section, up to the next level-1/2 heading."""
    lines = text.splitlines()
    start = None
    for i, line in enumerate(lines):
        if re.match(r"^##\s+%s\b" % re.escape(name), line):
            start = i + 1
            break
    if start is None:
        return None
    body = []
    for line in lines[start:]:
        if re.match(r"^#{1,2}\s", line):
            break
        body.append(line)
    return "\n".join(body)


def _table(section: str) -> tuple[list[str] | None, list[list[str]]]:
    header: list[str] | None = None
    rows: list[list[str]] = []
    for line in section.splitlines():
        s = line.strip()
        if not s.startswith("|"):
            continue
        cells = [c.strip() for c in s.strip("|").split("|")]
        if cells and all(not c or re.match(r"^:?-{2,}:?$", c) for c in cells):
            continue                                  # separator row
        if header is None:
            header = cells
            continue
        rows.append(cells)
    return header, rows


def _column(header: list[str] | None, *names: str) -> int | None:
    if not header:
        return None
    for i, cell in enumerate(header):
        low = _norm(cell).lower()
        if any(name in low for name in names):
            return i
    return None


def _decision(cell: str) -> bool:
    return _norm(cell).strip(" *_").lower() == "reject"


def reject_reasons(section: str) -> list[str]:
    """Reason text of every `reject` row in a `## Gate` section body."""
    header, rows = _table(section)
    didx = _column(header, "decision", "verdict")
    ridx = _column(header, "reason")
    reasons: list[str] = []

    def reason_of(cells: list[str], idx: int) -> str:
        if ridx is not None and ridx < len(cells) and ridx != idx:
            return cells[ridx]
        others = [c for j, c in enumerate(cells) if j != idx and c]
        return max(others, key=_words) if others else ""

    for cells in rows:
        if didx is not None and didx < len(cells):
            if _decision(cells[didx]):
                reasons.append(reason_of(cells, didx))
            continue
        for i, cell in enumerate(cells):
            if _decision(cell):
                reasons.append(reason_of(cells, i))
                break

    for line in section.splitlines():
        if not re.match(r"^\s*[-*+]\s", line):
            continue
        if not re.search(r"\breject\b", line, re.I):
            continue
        tail = re.split(r"\breject\b", line, flags=re.I)[-1]
        reasons.append(tail.strip(" \t\u2014\u2013-:|*`"))
    return reasons


def swarm_roles(src: str) -> list[str] | None:
    """Members of the `SWARM_ROLES` set literal, or None if it cannot be
    parsed (the set is parsed, never grepped for a substring)."""
    match = re.search(r"SWARM_ROLES\s*=\s*new\s+Set\(\s*\[(.*?)\]", src, re.S)
    if not match:
        return None
    roles = re.findall(r"""["'`]([^"'`]+)["'`]""", match.group(1))
    return roles or None


def js_comment_text(src: str) -> str:
    """Line and block comments with their markers stripped, joined: a sentence
    the source wraps over two comment lines still occurs here."""
    out: list[str] = []
    for match in re.finditer(r"/\*.*?\*/", src, re.S):
        out.append(re.sub(r"^\s*\*+", " ", match.group(0), flags=re.M))
    for line in src.splitlines():
        match = re.match(r"^\s*//(.*)$", line)
        if match:
            out.append(match.group(1))
    return "\n".join(out)


# --- D1 (carried from r87:270-347 via v2:172; meaning unchanged) ----------

def receipt_verdict(repo: Path, text: str, expected: str,
                    rev_full: str) -> tuple[bool, str]:
    if not re.search(r"\bexit\s*=\s*0\b", text):
        return False, "carries no exit=0"
    if expected not in text:
        return False, "carries no %r" % expected
    named = _named_rev(repo, text, rev_full)
    if named is None:
        return False, ("names no revision that resolves, is an ancestor of "
                       "<rev> and carries the same instruments")
    return True, "measured rev %s" % named


def _named_rev(repo: Path, text: str, rev_full: str) -> str | None:
    seen: list[str] = []
    for token in re.findall(r"\b[0-9a-f]{%d,40}\b" % MIN_READER, text):
        if token in seen:
            continue
        seen.append(token)
        if len(seen) > 60:
            break
        proc = _git(repo, "rev-parse", "--verify", "-q", "%s^{commit}" % token)
        if proc.returncode != 0:
            continue
        full = proc.stdout.strip()
        if full != rev_full:
            anc = _git(repo, "merge-base", "--is-ancestor", full, rev_full)
            if anc.returncode != 0:
                continue
        carries = True
        for path in INSTRUMENTS:
            if _blob_id(repo, full, path) != _blob_id(repo, rev_full, path):
                carries = False
                break
        if carries:
            return full
    return None


def check_d1(repo: Path, rev: str, work: Path, landing: str,
             validator: Path, base_rev: str) -> tuple[bool, str]:
    del work, validator, base_rev            # v2:172 ("d1", r87.check_d1)
    receipts = ((CATALOGUE_RECEIPT, CATALOGUE_LINE),
                (REGISTRY_RECEIPT, REGISTRY_LINE))
    for path, expected in receipts:
        text = _show(repo, rev, path)
        if text is None:
            return False, "%s absent at %s" % (path, rev[:12])
        ok, why = receipt_verdict(repo, text, expected, rev)
        if not ok:
            return False, "%s: %s" % (Path(path).name, why)
    for path in INSTRUMENTS:
        old = _blob_id(repo, landing, path)
        if old is None:
            raise Unevaluable("landing commit %s has no %s" % (landing[:12], path))
        new = _blob_id(repo, rev, path)
        if new is None:
            return False, "%s absent at %s" % (path, rev[:12])
        if old != new:
            return False, ("%s differs between %s and %s"
                           % (path, landing[:12], rev[:12]))
    return True, "two receipts carry exit=0; instruments equal %s..%s" % (
        landing[:8], rev[:8])


# --- D2 (carried from r87:350-376 via v2:172; meaning unchanged) ----------

def check_d2(repo: Path, rev: str, work: Path, landing: str,
             validator: Path, base_rev: str) -> tuple[bool, str]:
    del work, landing, base_rev              # v2:172 ("d2", r87.check_d2)
    carriers = [name for name in (PLAN, LESSON)
                if (text := _show(repo, rev, name)) is not None
                and _carries_sentence(text)]
    if not carriers:
        return False, ("no lane record (%s or %s) carries the validator "
                       "sentence verbatim" % (PLAN, LESSON))
    if not validator.is_file():
        raise Unevaluable("validator absent: %s" % validator)
    try:
        src = validator.read_text(encoding="utf-8", errors="replace")
    except OSError as exc:
        raise Unevaluable("validator unreadable: %s" % exc) from exc
    if not (_carries_sentence(js_comment_text(src)) or _carries_sentence(src)):
        return False, "the validator does not carry that sentence"
    roles = swarm_roles(src)
    if roles is None:
        raise Unevaluable("SWARM_ROLES set literal not parseable in %s"
                          % validator)
    if "planner" in roles:
        return False, "SWARM_ROLES contains planner"
    return True, "carried by %s; validator sentence present, %d roles, no planner" % (
        ", ".join(carriers), len(roles))


# --- D3 (carried from r87:379-398 via v2:172; meaning unchanged) ----------

def check_d3(repo: Path, rev: str, work: Path, landing: str,
             validator: Path, base_rev: str) -> tuple[bool, str]:
    del work, landing, validator, base_rev   # v2:172 ("d3", r87.check_d3)
    text = _show(repo, rev, LESSON)
    if text is None:
        return False, "%s absent at %s" % (LESSON, rev[:12])
    section = _section(text, "Gate")
    if section is None:
        return False, "%s has no '## Gate' section" % LESSON
    reasons = reject_reasons(section)
    if not reasons:
        return False, "## Gate holds no reject row"
    best = max(_words(r) for r in reasons)
    if best < MIN_REASON_WORDS:
        return False, ("reject row reason carries %d words (< %d)"
                       % (best, MIN_REASON_WORDS))
    return True, "%d reject row(s), longest reason %d words" % (
        len(reasons), best)


# --- D4 (carried from r87:401-410 via v2:172; meaning unchanged) ----------

def check_d4(repo: Path, rev: str, work: Path, landing: str,
             validator: Path, base_rev: str) -> tuple[bool, str]:
    del work, landing, validator, base_rev   # v2:172 ("d4", r87.check_d4)
    text = _show(repo, rev, PLAN)
    if text is None:
        return False, "%s absent at %s" % (PLAN, rev[:12])
    if KILL_BOUNDARY not in _norm(text):
        return False, "%s does not carry %r" % (PLAN, KILL_BOUNDARY)
    return True, "%s names the boundary %r" % (PLAN, KILL_BOUNDARY)


# --- integrity reading (cwd = the measured root; Q79) ----------------------

def run_integrity_json(root: Path) -> dict:
    """The root's own integrity gate, run with cwd = the root; --json doc."""
    if not (root / INTEGRITY).is_file():
        raise Unevaluable("%s absent at %s" % (INTEGRITY, root))
    try:
        run = subprocess.run([sys.executable, "-B", INTEGRITY, "--json"],
                             cwd=str(root), capture_output=True, text=True,
                             timeout=GIT_TIMEOUT)
    except (OSError, subprocess.SubprocessError) as exc:
        raise Unevaluable("integrity run at %s failed: %s" % (root, exc)) from exc
    if run.returncode not in (0, 1):
        raise Unevaluable("%s exit=%d at %s: %s"
                          % (INTEGRITY, run.returncode, root,
                             (run.stdout + run.stderr).strip()[-200:]))
    try:
        doc = json.loads(run.stdout)
    except ValueError as exc:
        raise Unevaluable("%s --json did not parse at %s: %s"
                          % (INTEGRITY, root, exc)) from exc
    results = doc.get("results") if isinstance(doc, dict) else None
    if not isinstance(results, list) or not results:
        raise Unevaluable("%s --json carries no results at %s"
                          % (INTEGRITY, root))
    names: list[str] = []
    for row in results:
        if (not isinstance(row, dict)
                or not isinstance(row.get("check"), str)
                or row.get("verdict") not in ("PASS", "DRIFT")):
            raise Unevaluable("%s row %r is not a PASS/DRIFT check row at %s"
                              % (INTEGRITY, row, root))
        names.append(row["check"])
    if len(set(names)) != len(names):
        raise Unevaluable("%s repeats a check name at %s" % (INTEGRITY, root))
    return doc


def integrity_self_test_ok(root: Path) -> bool:
    """The root's integrity gate certifies itself at the root.  Unrunnable is
    could-not-evaluate; a run that exits nonzero is a False the d5i leg names."""
    try:
        run = subprocess.run([sys.executable, "-B", INTEGRITY, "--self-test"],
                             cwd=str(root), capture_output=True, text=True,
                             timeout=GIT_TIMEOUT)
    except (OSError, subprocess.SubprocessError) as exc:
        raise Unevaluable("integrity --self-test unrunnable at %s: %s"
                          % (root, exc)) from exc
    return run.returncode == 0


def sha256_file(root: Path, rel: str) -> str:
    path = root / rel
    if not path.is_file():
        raise Unevaluable("%s absent at %s" % (rel, root))
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1 << 16), b""):
            digest.update(chunk)
    return digest.hexdigest()


# --- D5 leg helpers (pure; supersede v2:122-129 identity/monotone) ---------

def names_equal(measured: list[str], receipt: list[str]) -> bool:
    """d5i name conjunct: the same check-name list at root and receipt."""
    return sorted(measured) == sorted(receipt)


def drift_subset(measured_drift: list[str], receipt_drift: list[str]) -> bool:
    """d5ii: the measured DRIFT names are a subset of the receipt's."""
    return set(measured_drift) <= set(receipt_drift)


def growth_names(measured_values: dict, receipt_values: dict) -> list[str]:
    """d5iii/K: names whose value grew past the receipt's, or that have no
    receipt value to compare against."""
    return sorted(n for n in measured_values
                  if n not in receipt_values
                  or measured_values[n] > receipt_values[n])


# --- base receipt ----------------------------------------------------------

def write_base_receipt(root: Path, out_path: Path) -> int:
    """Measure <root> (cwd = root) and pin revision + snapshot digests + the
    full observation dict into one JSON receipt."""
    root = Path(root).resolve()
    proc = _git(root, "rev-parse", "HEAD")
    if proc.returncode != 0:
        raise Unevaluable("no HEAD revision at %s" % root)
    revision = proc.stdout.strip()
    doc = run_integrity_json(root)
    names = sorted(row["check"] for row in doc["results"])
    if len(names) != NAME_COUNT:
        raise Unevaluable("%d check names at %s, want %d (the v2:54 "
                          "NAME_COUNT anchor)"
                          % (len(names), root, NAME_COUNT))
    receipt = {
        "schema": SCHEMA,
        "written_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "revision": revision,
        "root": str(root),
        "integrity_path": INTEGRITY,
        "baseline_path": BASELINE,
        "integrity_argv": ["python3", "-B", INTEGRITY, "--json", "  # cwd=root"],
        "integrity_sha256": sha256_file(root, INTEGRITY),
        "baseline_sha256": sha256_file(root, BASELINE),
        "observation": doc,
    }
    out_path = Path(out_path)
    if out_path.parent != Path(""):
        out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(receipt, indent=2, ensure_ascii=False) + "\n",
                        encoding="utf-8")
    drift = sorted(row["check"] for row in doc["results"]
                   if row["verdict"] == "DRIFT")
    print("base receipt written %s rev %s integrity %s baseline %s; "
          "%d names, %d DRIFT"
          % (out_path, revision[:12], receipt["integrity_sha256"][:12],
             receipt["baseline_sha256"][:12], len(names), len(drift)))
    return 0


def load_receipt(path: Path) -> dict:
    """Read and validate one base receipt; anything malformed is exit 2."""
    try:
        text = Path(path).read_text(encoding="utf-8")
    except OSError as exc:
        raise Unevaluable("base receipt unreadable: %s" % exc) from exc
    try:
        receipt = json.loads(text)
    except ValueError as exc:
        raise Unevaluable("base receipt is not JSON: %s" % exc) from exc
    if not isinstance(receipt, dict) or receipt.get("schema") != SCHEMA:
        got = (receipt.get("schema") if isinstance(receipt, dict)
               else type(receipt).__name__)
        raise Unevaluable("base receipt schema mismatch: %r" % (got,))
    for key, shape in (("revision", re.compile(r"\A[0-9a-f]{40}\Z")),
                       ("integrity_sha256", re.compile(r"\A[0-9a-f]{64}\Z")),
                       ("baseline_sha256", re.compile(r"\A[0-9a-f]{64}\Z"))):
        value = receipt.get(key)
        if not isinstance(value, str) or not shape.match(value):
            raise Unevaluable("base receipt %s malformed: %r" % (key, value))
    observation = receipt.get("observation")
    results = observation.get("results") if isinstance(observation, dict) else None
    if not isinstance(results, list) or not results:
        raise Unevaluable("base receipt carries no observation results")
    for row in results:
        if (not isinstance(row, dict)
                or not isinstance(row.get("check"), str)
                or row.get("verdict") not in ("PASS", "DRIFT")):
            raise Unevaluable("base receipt row %r is not a PASS/DRIFT row"
                              % (row,))
    names = [row["check"] for row in results]
    if len(set(names)) != len(names):
        raise Unevaluable("base receipt repeats a check name")
    return receipt


def receipt_rows(receipt: dict) -> dict:
    """check name -> result row, from the receipt's observation dict."""
    return {row["check"]: row for row in receipt["observation"]["results"]}


# --- comparison ------------------------------------------------------------

LEG_ORDER = ("d5i", "d5ii", "d5iii", "snapshot_tampered")


def compare(root: Path, receipt_path: Path, work: Path, landing: str,
            validator: Path, print_observation: bool = False,
            out=sys.stdout) -> int:
    """Measure <root> against the base receipt; the frozen exit ladder."""
    root = Path(root).resolve()
    receipt = load_receipt(Path(receipt_path))
    rrows = receipt_rows(receipt)
    rnames = sorted(rrows)
    rdrift = sorted(n for n, row in rrows.items() if row["verdict"] == "DRIFT")
    rvalues: dict[str, int] = {}
    for name, row in rrows.items():
        value = row.get("observed")
        if not isinstance(value, int) or isinstance(value, bool):
            raise Unevaluable("receipt value for %s is not an int: %r"
                              % (name, value))
        rvalues[name] = value

    doc = run_integrity_json(root)
    if print_observation:
        out.write(json.dumps(doc, indent=2, ensure_ascii=False) + "\n")
        out.flush()
    mrows = {row["check"]: row for row in doc["results"]}
    mnames = sorted(mrows)
    mdrift = sorted(n for n, row in mrows.items() if row["verdict"] == "DRIFT")
    mvalues: dict[str, int] = {}
    for name, row in mrows.items():
        value = row.get("observed")
        if not isinstance(value, int) or isinstance(value, bool):
            raise Unevaluable("measured value for %s is not an int: %r"
                              % (name, value))
        mvalues[name] = value

    legs: list[tuple[str, bool, str]] = []
    rev = _resolve(root, "HEAD")     # the measured revision is the root's HEAD
    for cid, check in ():
        ok, detail = check(root, rev, work, landing, validator,
                           receipt["revision"])
        legs.append((cid, ok, detail))

    self_ok = integrity_self_test_ok(root)
    if names_equal(mnames, rnames) and self_ok:
        legs.append(("d5i", True,
                     "check names equal (%d) and integrity --self-test exits "
                     "0 at the root" % len(mnames)))
    elif not names_equal(mnames, rnames):
        missing = sorted(set(rnames) - set(mnames))
        extra = sorted(set(mnames) - set(rnames))
        suffix = "" if self_ok else " (integrity --self-test also nonzero)"
        legs.append(("d5i", False,
                     "check names differ: missing %s, extra %s%s"
                     % (missing, extra, suffix)))
    else:
        legs.append(("d5i", False,
                     "names equal but integrity --self-test nonzero at the "
                     "root"))

    new = sorted(set(mdrift) - set(rdrift))
    if drift_subset(mdrift, rdrift):
        legs.append(("d5ii", True,
                     "DRIFT %s within receipt DRIFT %s" % (mdrift, rdrift)))
    else:
        legs.append(("d5ii", False,
                     "new DRIFT names absent from the receipt: %s" % new))

    grew = growth_names(mvalues, rvalues)
    if not grew:
        legs.append(("d5iii", True, "no name grew past its receipt value"))
    else:
        bits = []
        for name in grew:
            if name in rvalues:
                bits.append("%s %d>%d" % (name, mvalues[name], rvalues[name]))
            else:
                bits.append("%s (no receipt value)" % name)
        legs.append(("d5iii", False, "instance growth under: %s" % bits))

    m_integrity = sha256_file(root, INTEGRITY)
    m_baseline = sha256_file(root, BASELINE)
    snap_ok = (m_integrity == receipt["integrity_sha256"]
               and m_baseline == receipt["baseline_sha256"])
    if snap_ok:
        legs.append(("snapshot_tampered", True,
                     "digests match (integrity %s, baseline %s)"
                     % (m_integrity[:12], m_baseline[:12])))
    else:
        legs.append(("snapshot_tampered", False,
                     "pinned digests differ (integrity %s vs %s, baseline %s "
                     "vs %s)" % (receipt["integrity_sha256"][:12],
                                 m_integrity[:12],
                                 receipt["baseline_sha256"][:12],
                                 m_baseline[:12])))

    for name, ok, detail in legs:
        print("%s %s %s" % ("PASS" if ok else "FAIL", name, detail), file=out)

    verdicts = {name: ok for name, ok, _detail in legs}
    d5_ok = all(verdicts[name] for name in
                ("d5i", "d5ii", "d5iii", "snapshot_tampered"))
    n = 0
    n += 1 if d5_ok else 0
    k = len(grew)
    print("r86 routed defects closed %d of %d" % (n, TARGET), file=out)
    print("instance drift %d" % k, file=out)

    for name in LEG_ORDER:           # the first failing leg is named by exit
        if not verdicts[name]:
            return 1
    if n != TARGET or k != 0:
        return 1
    return 0


# --- driver ----------------------------------------------------------------

def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--write-base-receipt", metavar="PATH",
                    help="measure the lane and write its base receipt")
    ap.add_argument("--base-receipt", metavar="PATH",
                    help="base receipt to compare against")
    ap.add_argument("--root", help="measured root (default: the lane)")
    ap.add_argument("--print-observation", action="store_true",
                    help="print the measured observation dict (comparison mode)")
    ap.add_argument("--work",
                    help="scratch parent directory (default: $TMPDIR)")
    ap.add_argument("--self-test", action="store_true",
                    help="run the fixture self-test")
    args = ap.parse_args(argv)
    if args.self_test:
        return self_test()
    if bool(args.write_base_receipt) == bool(args.base_receipt):
        ap.error("exactly one of --write-base-receipt / --base-receipt")
    if args.print_observation and not args.base_receipt:
        ap.error("--print-observation needs --base-receipt")

    parent = (Path(args.work) if args.work
              else Path(os.environ.get("TMPDIR") or tempfile.gettempdir()))
    try:
        parent.mkdir(parents=True, exist_ok=True)
        work = Path(tempfile.mkdtemp(prefix="r89-routed-v3-", dir=str(parent)))
    except OSError as exc:
        print("could-not-evaluate: scratch dir: %s" % exc, file=sys.stderr)
        return 2

    try:
        if args.write_base_receipt:
            return write_base_receipt(LANE, Path(args.write_base_receipt))
        root = Path(args.root).resolve() if args.root else LANE
        return compare(root, Path(args.base_receipt), work, LANDING_REV,
                       OMP_VALIDATOR, print_observation=args.print_observation)
    except Unevaluable as exc:
        print("could-not-evaluate: %s" % exc, file=sys.stderr)
        return 2
    finally:
        shutil.rmtree(work, ignore_errors=True)


# --- self-test fixtures ----------------------------------------------------
# Hermetic: everything happens under one tempfile.TemporaryDirectory (the
# process TMPDIR); the committed fixture integrity gate is
# verifiers/fixtures/d5v3/fixture_integrity.py, copied into the world repos.

FIXTURE_DIR = HERE / "fixtures" / "d5v3"

FIXTURE_INSTRUMENT = "#!/bin/sh\n# fixture instrument\n"

FIXTURE_BASELINE_A = "{\n  \"fixture\": \"baseline A\"\n}\n"
FIXTURE_BASELINE_B = "{\n  \"fixture\": \"baseline re-recorded\"\n}\n"

FIXTURE_PLAN_87 = (
    "# round-87 plan (fixture)\n\n"
    "The validator sentence: `planner/distiller/labrat/Main are frozen-topology "
    "seats and can never be swarm lanes.`\n\n"
    "Kill rule: any counter change after the first candidate score kills the "
    "claim.\n"
)

FIXTURE_LESSON_87 = (
    "# round-87 lesson (fixture)\n\n"
    "## Gate\n\n"
    "| Decision | Reason |\n"
    "|----------|--------|\n"
    "| reject | the frozen control could not produce its declared failure world so the freeze shipped unexecuted |\n"
)

FIXTURE_LESSON_87_WEAK = (
    "# round-87 lesson (fixture, weak)\n\n"
    "## Gate\n\n"
    "| Decision | Reason |\n"
    "|----------|--------|\n"
    "| reject | it could not hold |\n"
)

FIXTURE_VALIDATOR_JS = (
    "// planner/distiller/labrat/Main are frozen-topology seats and can\n"
    "// never be swarm lanes.\n"
    "const SWARM_ROLES = new Set([\n"
    "  \"executor\",\n"
    "  \"reviewer\",\n"
    "]);\n"
)

FIXTURE_VALIDATOR_PLANNER_JS = (
    "// planner/distiller/labrat/Main are frozen-topology seats and can\n"
    "// never be swarm lanes.\n"
    "const SWARM_ROLES = new Set([\n"
    "  \"planner\",\n"
    "  \"executor\",\n"
    "]);\n"
)

NINE_NAMES = (
    "corpus.index.tracked_files",
    "corpus.index.unindexed",
    "corpus.index.stale_patterns",
    "corpus.index.missing_paths",
    "corpus.pointers.report_total",
    "corpus.pointers.report_dead",
    "corpus.pointers.commit_total",
    "corpus.pointers.commit_unresolvable",
    "corpus.pointers.commit_nonhash",
)
BASE_DRIFT = (
    "corpus.index.tracked_files",
    "corpus.pointers.report_total",
    "corpus.pointers.report_dead",
    "corpus.pointers.commit_total",
    "corpus.pointers.commit_unresolvable",
)


def _git_fixture(repo: Path, *args: str) -> str:
    proc = _git(repo, *args)
    if proc.returncode != 0:
        raise RuntimeError("fixture git %s: %s"
                           % (args[0], proc.stderr.strip()[-200:]))
    return proc.stdout.strip()


def _fixture_commit(repo: Path, message: str,
                    files: dict[str, str]) -> str:
    for rel, body in files.items():
        path = repo / rel
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(body, encoding="utf-8")
    _git_fixture(repo, "add", "-A")
    _git_fixture(repo, "-c", "user.name=probe", "-c",
                 "user.email=probe@example.invalid", "commit", "-q",
                 "--allow-empty", "-m", message)
    return _git_fixture(repo, "rev-parse", "HEAD")


def _fixture_world(repo: Path, message: str, mode: str,
                   extra: dict[str, str] | None = None) -> str:
    files = {"MODE": mode + "\n"}
    files.update(extra or {})
    return _fixture_commit(repo, message, files)


def _run_compare(root: Path, receipt: Path, work: Path, landing: str,
                 validator: Path,
                 print_observation: bool = False) -> tuple[int, str]:
    buf = io.StringIO()
    code = compare(root, receipt, work, landing, validator,
                   print_observation=print_observation, out=buf)
    return code, buf.getvalue()


# --- self-test -------------------------------------------------------------

def self_test() -> int:
    failures: list[str] = []
    assertions = 0

    def check(label: str, ok: bool, detail: str = "") -> None:
        nonlocal assertions
        assertions += 1
        if not ok:
            failures.append("%s%s" % (label, (": " + detail) if detail else ""))

    # --- d5i/d5ii/d5iii as pure functions on micro observation dicts -------
    check("arm d5i pure: equal nine-name lists hold",
          names_equal(list(NINE_NAMES), list(NINE_NAMES)))
    check("arm d5i pure: a renamed check fails the name conjunct",
          not names_equal(list(NINE_NAMES[:-1]) + ["corpus.pointers.renamed"],
                          list(NINE_NAMES)))
    check("arm d5i pure: a silenced check (eight names) fails the name conjunct",
          not names_equal(list(NINE_NAMES[:-1]), list(NINE_NAMES)))
    check("arm d5ii pure: a DRIFT set equal to the receipt's holds",
          drift_subset(list(BASE_DRIFT), list(BASE_DRIFT)))
    check("arm d5ii pure: a strict subset (a healed red) holds",
          drift_subset(list(BASE_DRIFT[1:]), list(BASE_DRIFT)))
    check("arm d5ii pure: a new red name fails",
          not drift_subset(list(BASE_DRIFT) + ["corpus.pointers.commit_nonhash"],
                           list(BASE_DRIFT)))
    micro_receipt_values = {NINE_NAMES[0]: 7, NINE_NAMES[4]: 3,
                            NINE_NAMES[5]: 1, NINE_NAMES[6]: 3,
                            NINE_NAMES[7]: 1}
    micro_measured_equal = dict(micro_receipt_values)
    micro_measured_growth = dict(micro_receipt_values)
    micro_measured_growth[NINE_NAMES[7]] = 2
    micro_measured_growth[NINE_NAMES[6]] = 4
    micro_measured_uncomparable = dict(micro_receipt_values)
    micro_measured_uncomparable["corpus.pointers.added"] = 1
    check("arm d5iii pure: equal values leave no growth",
          growth_names(micro_measured_equal, micro_receipt_values) == [])
    check("arm d5iii pure: an added instance under an already-red name grows",
          growth_names(micro_measured_growth, micro_receipt_values)
          == [NINE_NAMES[6], NINE_NAMES[7]])
    check("arm d5iii pure: a name with no receipt value counts as growth",
          growth_names(micro_measured_uncomparable, micro_receipt_values)
          == ["corpus.pointers.added"])

    with tempfile.TemporaryDirectory(prefix="r89-routed-v3-fixture-") as tdir:
        root = Path(tdir)
        work = root / "work"
        work.mkdir()
        repo = root / "lane"
        repo.mkdir()
        _git_fixture(repo, "init", "-q")
        fixture_integrity = (FIXTURE_DIR / "fixture_integrity.py").read_text(
            encoding="utf-8")

        # landing commit L: the fixture integrity gate, baseline A, instruments
        landing = _fixture_commit(repo, "fixture landing", {
            INTEGRITY: fixture_integrity,
            BASELINE: FIXTURE_BASELINE_A,
            "verifiers/check_omp_catalogue_repro.py": FIXTURE_INSTRUMENT,
            "verifiers/check_gate_registry.py": FIXTURE_INSTRUMENT,
            "MODE": "base\n",
        })
        # receipts commit: the round-86-shaped receipts + D2/D4 carriers
        receipts_rev = _fixture_commit(repo, "fixture receipts", {
            CATALOGUE_RECEIPT: "measured rev %s\nexit=0\n%s\n"
                               % (landing, CATALOGUE_LINE),
            REGISTRY_RECEIPT: "measured rev %s\nexit=0\n%s\n"
                              % (landing, REGISTRY_LINE),
            PLAN: FIXTURE_PLAN_87,
            LESSON: FIXTURE_LESSON_87,
        })
        tip = _fixture_world(repo, "tip world (base)", "base")

        validator = root / "ufo-swarm-wave.mjs"
        validator.write_text(FIXTURE_VALIDATOR_JS, encoding="utf-8")
        planner_validator = root / "ufo-swarm-wave-planner.mjs"
        planner_validator.write_text(FIXTURE_VALIDATOR_PLANNER_JS,
                                     encoding="utf-8")

        # the base receipt: written by the gate's own write path at the tip
        receipt_path = root / "d5v3-base-receipt.json"
        write_base_receipt(repo, receipt_path)

        # --- tip arms run while the working tree is still the receipt world -
        code, out = _run_compare(repo, receipt_path, work, landing, validator)
        check("arm w_tip: the honest tip closes 5 of 5 with zero drift",
              code == 0 and "r86 routed defects closed 5 of 5" in out
              and "instance drift 0" in out, out.strip()[-200:])

        code, out = _run_compare(repo, receipt_path, work, landing, validator,
                                 print_observation=True)
        decoder = json.JSONDecoder()
        try:
            observation, _pos = decoder.raw_decode(out)
        except ValueError:
            observation = None
        check("arm w_print_observation: --print-observation emits the measured "
              "observation dict before the leg lines",
              isinstance(observation, dict)
              and sorted(row["check"] for row in observation["results"])
              == sorted(NINE_NAMES), out[:120])

        # worlds, each one commit on top of the tip (shared-history clone shape)
        healed = _fixture_world(repo, "healed world", "healed")
        added = _fixture_world(repo, "added-instance world", "added")
        silenced = _fixture_world(repo, "silenced world", "silenced")
        renamed = _fixture_world(repo, "renamed world", "renamed")
        newred = _fixture_world(repo, "new-red-name world", "newred")
        rerecorded = _fixture_world(repo, "re-recorded-baseline world",
                                    "rerecorded",
                                    {BASELINE: FIXTURE_BASELINE_B})
        broken = _fixture_world(repo, "broken-self-test world",
                                "brokenselftest")
        garbage = _fixture_world(repo, "garbage world", "garbage")
        d1_noexit = _fixture_world(repo, "d1 receipt without exit=0", "base", {
            CATALOGUE_RECEIPT: "measured rev %s\n%s\n" % (landing,
                                                          CATALOGUE_LINE),
        })
        d1_instrument = _fixture_world(repo, "d1 instrument changed", "base", {
            "verifiers/check_gate_registry.py":
                FIXTURE_INSTRUMENT + "changed\n",
        })
        d3_weak = _fixture_world(repo, "d3 weak-reason world", "base", {
            LESSON: FIXTURE_LESSON_87_WEAK,
        })

        # --- end-to-end legs against the committed fixture worlds ------------
        code, out = _compare_world(repo, receipt_path, work, landing,
                                   validator, healed)
        check("arm w_healed: a healed red passes (exit 0, not blanket refusal)",
              code == 0 and "r86 routed defects closed 5 of 5" in out,
              out.strip()[-200:])

        code, out = _compare_world(repo, receipt_path, work, landing,
                                   validator, added)
        check("arm w_added_instance (frozen control): an added finding under "
              "already-red names fails via d5iii with drift 2",
              code == 1 and "FAIL d5iii" in out and "instance drift 2" in out
              and "r86 routed defects closed 4 of 5" in out,
              out.strip()[-200:])
        check("arm w_added_instance: d5ii still holds (no NEW red name)",
              "PASS d5ii" in out, out.strip()[-200:])

        code, out = _compare_world(repo, receipt_path, work, landing,
                                   validator, silenced)
        check("arm w_silenced: a removed check fails d5i (names differ)",
              code == 1 and "FAIL d5i" in out and "missing" in out,
              out.strip()[-200:])

        code, out = _compare_world(repo, receipt_path, work, landing,
                                   validator, renamed)
        check("arm w_renamed: a renamed check fails d5i",
              code == 1 and "FAIL d5i" in out and "extra" in out,
              out.strip()[-200:])

        code, out = _compare_world(repo, receipt_path, work, landing,
                                   validator, newred)
        check("arm w_newred: a new red name fails d5ii first",
              code == 1 and "FAIL d5ii" in out
              and "new DRIFT names" in out, out.strip()[-200:])

        code, out = _compare_world(repo, receipt_path, work, landing,
                                   validator, rerecorded)
        check("arm w_rerecorded: a re-recorded baseline cannot green D5 "
              "(snapshot_tampered)",
              code == 1 and "FAIL snapshot_tampered" in out
              and "PASS d5i" in out and "PASS d5ii" in out and "PASS d5iii" in out,
              out.strip()[-200:])

        code, out = _compare_world(repo, receipt_path, work, landing,
                                   validator, broken)
        check("arm w_brokenselftest: a nonzero integrity --self-test at the "
              "root is a named d5i failure",
              code == 1 and "FAIL d5i" in out and "self-test nonzero" in out,
              out.strip()[-200:])

        try:
            _compare_world(repo, receipt_path, work, landing, validator,
                           garbage)
            check("arm w_garbage: a non-JSON integrity run is "
                  "could-not-evaluate, never a verdict",
                  False, "compare returned without raising")
        except Unevaluable as exc:
            check("arm w_garbage: a non-JSON integrity run is "
                  "could-not-evaluate, never a verdict",
                  "did not parse" in str(exc), str(exc))

        # --- carried D1-D4: one positive and one must-fail arm each ---------
        ok, detail = check_d1(repo, tip, work, landing, validator, "0" * 40)
        check("arm d1 positive: the carried receipt check holds at the tip",
              ok, detail)
        ok, detail = check_d1(repo, d1_noexit, work, landing, validator,
                              "0" * 40)
        check("arm d1 must-fail: a receipt without exit=0 fails d1",
              not ok and "exit=0" in detail, detail)
        ok, detail = check_d1(repo, d1_instrument, work, landing, validator,
                              "0" * 40)
        check("arm d1 must-fail: an instrument changed after the receipt's "
              "named revision fails d1",
              not ok, detail)

        ok, detail = check_d2(repo, tip, work, landing, validator, "0" * 40)
        check("arm d2 positive: the carried validator-sentence check holds",
              ok, detail)
        ok, detail = check_d2(repo, tip, work, landing, planner_validator,
                              "0" * 40)
        check("arm d2 must-fail: SWARM_ROLES containing planner fails d2",
              not ok and "planner" in detail, detail)
        ok, detail = check_d2(repo, landing, work, landing, validator,
                              "0" * 40)
        check("arm d2 must-fail: a revision carrying no lane record fails d2",
              not ok and "no lane record" in detail, detail)

        ok, detail = check_d3(repo, tip, work, landing, validator, "0" * 40)
        check("arm d3 positive: the carried reject-row check holds",
              ok, detail)
        ok, detail = check_d3(repo, d3_weak, work, landing, validator,
                              "0" * 40)
        check("arm d3 must-fail: a reject reason under 8 words fails d3",
              not ok and "words" in detail, detail)

        ok, detail = check_d4(repo, tip, work, landing, validator, "0" * 40)
        check("arm d4 positive: the carried kill-boundary check holds",
              ok, detail)
        ok, detail = check_d4(repo, landing, work, landing, validator,
                              "0" * 40)
        check("arm d4 must-fail: a revision with no plan record fails d4",
              not ok and "absent" in detail, detail)

        # --- receipt hygiene on synthetic receipt files under TMPDIR --------
        micro_receipt = {
            "schema": SCHEMA,
            "revision": "a" * 40,
            "integrity_sha256": "b" * 64,
            "baseline_sha256": "c" * 64,
            "observation": {"observed": {"corpus": {}},
                            "results": [
                                {"check": NINE_NAMES[7], "mode": "zero",
                                 "observed": 1, "expected": "0 / empty",
                                 "verdict": "DRIFT"},
                                {"check": NINE_NAMES[8], "mode": "zero",
                                 "observed": 0, "expected": "0 / empty",
                                 "verdict": "PASS"},
                            ]},
        }
        micro_path = root / "micro-receipt.json"
        micro_path.write_text(json.dumps(micro_receipt), encoding="utf-8")
        loaded = load_receipt(micro_path)
        check("arm receipt-load: a synthetic receipt file round-trips",
              receipt_rows(loaded)[NINE_NAMES[7]]["observed"] == 1)
        bad_schema = dict(micro_receipt, schema="other/1")
        bad_path = root / "micro-receipt-schema.json"
        bad_path.write_text(json.dumps(bad_schema), encoding="utf-8")
        try:
            load_receipt(bad_path)
            check("arm receipt-load: a wrong-schema receipt is refused",
                  False, "load_receipt accepted schema other/1")
        except Unevaluable as exc:
            check("arm receipt-load: a wrong-schema receipt is refused",
                  "schema" in str(exc), str(exc))
        bad_digest = dict(micro_receipt, baseline_sha256="zz" * 32)
        bad_path2 = root / "micro-receipt-digest.json"
        bad_path2.write_text(json.dumps(bad_digest), encoding="utf-8")
        try:
            load_receipt(bad_path2)
            check("arm receipt-load: a malformed digest is refused",
                  False, "load_receipt accepted a non-hex digest")
        except Unevaluable as exc:
            check("arm receipt-load: a malformed digest is refused",
                  "baseline_sha256" in str(exc), str(exc))

    print("%d failure(s) over %d assertions" % (len(failures), assertions))
    for failure in failures:
        print("FAIL", failure)
    return 1 if failures else 0


def _compare_world(repo: Path, receipt_path: Path, work: Path, landing: str,
                   validator: Path, world_rev: str) -> tuple[int, str]:
    """Run compare() with the measured root checked out at a world revision.

    Worlds under test are scratch checkouts, never the lane and never a tree
    inside it: one shared clone per world, created in the process TMPDIR.
    """
    box = Path(tempfile.mkdtemp(prefix="d5v3-world-", dir=str(work)))
    tree = box / "tree"
    proc = _git(repo.resolve(), "clone", "-q", "--shared",
                str(repo.resolve()), str(tree))
    if proc.returncode != 0:
        raise Unevaluable("world clone: %s" % proc.stderr.strip()[-200:])
    top = _git_fixture(tree, "rev-parse", "--show-toplevel")
    if Path(top).resolve() != tree.resolve():
        raise Unevaluable("world clone is not its own toplevel")
    _git_fixture(tree, "checkout", "-q", "--detach", world_rev)
    return _run_compare(tree, receipt_path, work, landing, validator)


if __name__ == "__main__":
    sys.exit(main())
