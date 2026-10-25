#!/usr/bin/env python3
"""check_author_rules.py — C1 counter for kotoba round 72 (depth).

Frozen predicate (the same sentence in plans/round-72.md § C1, in this
docstring and in the receipt):

    python3 -B verifiers/check_author_rules.py --rev <rev>  ->  prints
    "author-facing rules in SKILL.md N of 4", exit 0 when N == 4

Rule ``Ai`` holds at ``--rev`` iff all of (a)–(d) hold, over committed bytes
only (no instrument of the measured tree is executed):

  (a) the rendered ``SKILL.md`` (HTML comments and fenced blocks removed) has
      exactly one checklist box — a ``- [ ] `` line plus its indented
      continuation lines — inside ``## Trigger-fidelity checklist`` (up to the
      next ``## `` heading) whose joined text carries the rule's frozen token
      set as whole words and ends with the tail
      ``(sourced: S###[, S###…]; entry: <repo-relative path>)`` naming that
      rule's frozen entry and at least one id from that entry's own
      ``source:`` lines;
  (b) every cited ``S###`` is an 11-cell registry row at ``--rev`` with status
      ``mined``, tier ``A`` or ``B``, and a ``used-by`` cell that lists the
      cited entry path;
  (c) the entry exists at ``--rev``, opens with ``source:`` lines naming every
      cited id, then ``verified-at:`` and ``recheck:``;
  (d) (A4 only) each cited row's located quote (5–25 words) is found
      word-bounded in a committed, sha256-pinned snapshot of the cited page
      under ``.ufo/waves/round-72/snapshots/`` — a missing or tampered
      snapshot is exit 2.

Successor shape carried over from ``verifiers/check_skill_evals_v2.py``
(round 71): HTML comments and fenced blocks are stripped before parsing, a
registry row must be exactly 11 cells, quotes match word-bounded, the counter
carries a blanked-sha of itself and refuses to run when that sha drifts
(exit 2), and the junk worlds live in isolated local git repos.

Readings that are deliberately stricter than the naive one, named here so a
reviewer can attack them rather than discover them:

  * the frozen token set is matched against the box text with the citation
    tail REMOVED.  The tail is a citation, not rule text, and two of the four
    entry paths carry a rule token themselves (``client-trust-gates-round68``
    contains ``trust``, ``instruction-authority-ladder-round67`` contains
    ``authority``): matching the whole joined box would let the path supply
    the token the prose is supposed to carry.
  * ``cited ids ⊆ entry source: ids`` is enforced as a subset, which is the
    frozen "(a) … at least one id from that entry's own ``source:`` lines"
    read as a closure (a superset of that requirement, never a weakening).
  * the located quote for (d) is read from a ``located quote "…"`` span on
    the entry's own ``source: S###`` line or on an entry table row whose
    first cell is that id (the lane's r67/r68/r69 convention); a quoted
    section name on the same line is not a quote.  Only when no
    ``located quote`` phrase exists does the ``source:`` line fall back to
    its single quoted span, and two different quotes for one row is a
    finding, never a pass.
  * ``SNAPSHOT_PINS`` is the L1's fill-in table.  An unfilled slot, or a
    cited A4 id with no slot at all, is exit 2 (could not evaluate) — never a
    pass.  Nothing in the counter can turn an empty slot green.

Environment: ``--repo`` the measured git worktree (default: the lane root,
found by walking up from this file), ``--rev`` the measured revision.
Read-only on the lane; every scratch tree is a fresh ``mktemp -d``.
``--self-test`` runs the world table (one satisfying world, then one broken
world per conjunct and per shortcut control) in isolated local git repos.
``--box-proof --map <checklist-baseline.json>`` proves the boxes the checklist
map delegates to this counter, so the four new boxes can be mapped
``delegated:verifiers/check_author_rules.py`` instead of ``unexecuted:``.
``--census-check`` re-runs ``sources-census.sh validate`` over the revision's
registry as a second evidence, never the verdict.
"""

from __future__ import annotations

import argparse
import contextlib
import hashlib
import io
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

TOTAL = 4
MIN_BODY_WORDS = 25
SKILL = "SKILL.md"
SOURCES = "corpus/SOURCES.md"
COUNTER_PATH = "verifiers/check_author_rules.py"
SNAPDIR = ".ufo/waves/round-72/snapshots"

# The four rules, frozen in plans/round-72.md § C1.  Tokens are matched as
# whole words; the entry path is the frozen tail target.
RULES = {
    "A1": {
        "tokens": ("name", "unique", "precedence"),
        "entry": "corpus/knowledge/skill-name-precedence-round69.md",
        "snapshots": False,
    },
    "A2": {
        "tokens": ("authority", "level", "body"),
        "entry": "corpus/knowledge/instruction-authority-ladder-round67.md",
        "snapshots": False,
    },
    "A3": {
        "tokens": ("install", "trust", "command"),
        "entry": "corpus/knowledge/client-trust-gates-round68.md",
        "snapshots": False,
    },
    "A4": {
        "tokens": ("prompt", "always-on", "skill", "index"),
        "entry": "corpus/knowledge/resident-index-and-rungs-round72.md",
        "snapshots": True,
    },
}

# Pin table for (d): one slot per cited A4 row — (snapshot filename under SNAPDIR,
# sha256 of the snapshot bytes).  Filled by the L1 at freeze 2, before the data
# commit: the snapshots are the wave-1 source-opening seats' committed fetches
# (ExecSrcFactory, ExecSrcPi, ExecSrcHermes), re-verified by the L1; a missing slot
# or file is exit 2, never a pass.
SNAPSHOT_PINS = {
    "S214": ("S262-factory-droid-skills.md",
             "81409d890cb1b07f6a5a85db19610d4706866e5f4f668d4e26dd032002fed0c9"),
    "S215": ("S263-pi-skills.md",
             "5b9805525b194474ef1fe5455a0917ef15ed7f710aa9bec2eee11879556469e5"),
    "S216": ("S264-hermes-skills.md",
             "fb06e67d35c7aa6b11fd4587395cd3665ee9245d499416fe7928b5fa4c8772f5"),
}

SID_RE = re.compile(r"\bS\d{3,}\b")
QUOTE_RE = re.compile(r'"([^"]+)"')
LOCATED_RE = re.compile(r'located quote\s+"([^"]+)"')
TAIL_RE = re.compile(
    r"\(sourced:\s*(S\d{3,}(?:\s*,\s*S\d{3,})*)\s*;\s*entry:\s*([^)]+?)\s*\)"
    r"\s*$")
SECTION_RE = re.compile(r"^##\s+Trigger-fidelity checklist\s*$")
HEADING_RE = re.compile(r"^##\s+")
BOX_RE = re.compile(r"^- \[ \]\s+(.*)$")
SELF_SHA = "a30eacb8a9a0ae5307a22473cb39fe67c8ffd782124855ecdac7f5cf1939bb0c"   # blanked-sha of this file
SELF_LINE_RE = re.compile(r'^SELF_SHA = "[0-9a-f]*"', re.M)


class EnvError(Exception):
    """Could not evaluate: exit 2, never a pass and never a fail."""


def _blanked_sha(text: str) -> str:
    return hashlib.sha256(
        SELF_LINE_RE.sub('SELF_SHA = ""', text).encode()).hexdigest()


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


def _default_repo() -> Path:
    here = Path(__file__).resolve()
    for cand in [here.parent.parent] + list(here.parents):
        if (cand / SKILL).is_file() and (cand / SOURCES).is_file():
            return cand
    return here.parent.parent


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
        if sid not in SNAPSHOT_PINS:
            raise EnvError(
                f"no pinned snapshot slot declared for {sid} in "
                f"SNAPSHOT_PINS — the L1 adds one after committing the page "
                f"snapshot under {SNAPDIR}/")
        name, sha = SNAPSHOT_PINS[sid]
        if not name or not sha:
            raise EnvError(
                f"SNAPSHOT_PINS[{sid!r}] is an unfilled slot "
                f"({name!r}, {sha!r}) — the L1 fills it after the snapshot is "
                f"committed under {SNAPDIR}/")
        if not re.fullmatch(r"[0-9a-f]{64}", sha):
            raise EnvError(f"SNAPSHOT_PINS[{sid!r}] sha256 is not 64 hex chars")
        proc = subprocess.run(
            ["git", "-C", str(self.path), "show",
             f"{self.rev}:{SNAPDIR}/{name}"],
            capture_output=True)
        if proc.returncode != 0:
            raise EnvError(f"snapshot {SNAPDIR}/{name} not committed at "
                           f"{self.rev}")
        if hashlib.sha256(proc.stdout).hexdigest() != sha:
            raise EnvError(f"snapshot_tampered: {SNAPDIR}/{name}")
        return proc.stdout.decode("utf-8", "replace")

    def census_ok(self) -> bool | None:
        """sources-census.sh validate --file on the revision's registry."""
        with tempfile.TemporaryDirectory(prefix="k72-c1c-") as td:
            root = Path(td)
            proc = subprocess.run(
                ["git", "-C", str(self.path), "archive", self.rev],
                capture_output=True)
            if proc.returncode != 0:
                return None
            (root / "tree.tar").write_bytes(proc.stdout)
            subprocess.run(["tar", "-xf", "tree.tar"], cwd=root,
                           capture_output=True)
            target = root / SOURCES
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


def section_boxes(skill_r: str) -> list[str] | None:
    """Checklist boxes inside ``## Trigger-fidelity checklist``.

    A box is a ``- [ ] `` line plus its indented continuation lines; the
    returned text is the joined box, whitespace-collapsed.  None means the
    section heading is absent from the rendered file.
    """
    lines = skill_r.splitlines()
    start = None
    for i, line in enumerate(lines):
        if SECTION_RE.match(line):
            start = i + 1
            break
    if start is None:
        return None
    end = len(lines)
    for j in range(start, len(lines)):
        if HEADING_RE.match(lines[j]):
            end = j
            break
    boxes: list[str] = []
    cur: str | None = None
    for line in lines[start:end]:
        m = BOX_RE.match(line)
        if m:
            if cur is not None:
                boxes.append(cur)
            cur = m.group(1)
            continue
        if cur is None:
            continue
        if not line.strip() or not line[:1].isspace():
            boxes.append(cur)
            cur = None
            continue
        cur = cur + " " + line.strip()
    if cur is not None:
        boxes.append(cur)
    return [norm(b) for b in boxes]


def parse_box(box: str) -> tuple[str, list[str], str] | None:
    """(body-without-tail, cited ids, entry path) for a box carrying a tail."""
    m = TAIL_RE.search(box)
    if not m:
        return None
    return box[:m.start()].strip(), SID_RE.findall(m.group(1)), m.group(2).strip()


def entry_head(text: str) -> tuple[list[str], str | None, str | None]:
    """The provenance trio: leading source: lines, then verified-at, recheck."""
    lines = text.splitlines()
    i = 0
    while i < len(lines) and not lines[i].strip():
        i += 1
    src: list[str] = []
    while i < len(lines) and lines[i].startswith("source:"):
        src.append(lines[i])
        i += 1

    def field(name: str) -> str | None:
        nonlocal i
        while i < len(lines) and not lines[i].strip():
            i += 1
        if i < len(lines) and lines[i].startswith(name + ":"):
            value = lines[i][len(name) + 1:].strip()
            i += 1
            return value or None
        return None

    return src, field("verified-at"), field("recheck")


def located_quote(entry_r: str, sid: str) -> tuple[str | None, str | None]:
    """The located quote an entry carries for one cited row.

    The lane's convention (r67/r68/r69 entries, plans/round-72.md § C1) is
    ``… — located quote "<5–25 words>"``: a ``located quote`` span is the
    quote, and any other quoted span on the same line (a section name such as
    ``the "Trust" section``) is not.  Only when no ``located quote`` phrase
    exists does the entry's own ``source: S###`` line fall back to its single
    quoted span.  Exactly one distinct quote is admissible.
    """
    located: list[str] = []
    fallback: list[str] = []
    for line in entry_r.splitlines():
        if line.startswith("source:") and sid in SID_RE.findall(line):
            located.extend(LOCATED_RE.findall(line))
            fallback.extend(QUOTE_RE.findall(line))
        cells = _cells(line)
        if cells and cells[0] == sid:
            located.extend(LOCATED_RE.findall(line))
    cands = located or fallback
    uniq: list[str] = []
    for q in cands:
        n = norm(q)
        if n and n not in uniq:
            uniq.append(n)
    if len(uniq) != 1:
        return None, (f"{sid}: {len(uniq)} distinct located quotes in the "
                      f"entry (want exactly 1)")
    quote = uniq[0]
    words = len(quote.split())
    if not 5 <= words <= 25:
        return None, f"{sid}: located quote is {words} words (want 5-25)"
    return quote, None


def rule_holds(repo, skill_r: str, rows, rid: str,
               rule: dict) -> tuple[bool, list[str]]:
    notes: list[str] = []
    boxes = section_boxes(skill_r)
    if boxes is None:
        return False, [f"no `## Trigger-fidelity checklist` section in the "
                       f"rendered {SKILL}"]
    matching: list[tuple[list[str], str]] = []
    for box in boxes:
        parsed = parse_box(box)
        if parsed is None:
            continue
        body, ids, entry = parsed
        if entry != rule["entry"]:
            continue
        if not all(word_bounded(t, body) for t in rule["tokens"]):
            continue
        # errata E3 (plans/round-72-addendum-1.md): a token list is not a rule
        # (wave-1 world w9-token-list read 4 of 4); a box states its rule in at
        # least MIN_BODY_WORDS words before its tail.  Carriage beyond that is a
        # named reviewer judgement, not a counted fact (Q26/Q31).
        if len(body.split()) < MIN_BODY_WORDS:
            continue
        matching.append((ids, body))
    if len(matching) != 1:
        return False, [
            f"{len(matching)} checklist box(es) carry tokens "
            f"{list(rule['tokens'])} + a tail naming {rule['entry']} "
            f"(want exactly 1; {len(boxes)} box(es) in the section)"]
    ids = matching[0][0]

    # (c) entry exists with its provenance trio, and names every cited id.
    entry_text = repo.show(rule["entry"])
    if entry_text is None:
        return False, [f"entry {rule['entry']} absent at {repo.rev}"]
    entry_r = rendered(entry_text)
    src, verified, recheck = entry_head(entry_r)
    if not src:
        notes.append(f"entry does not open with source: lines")
    if not verified:
        notes.append("entry has no verified-at: line after its source: lines")
    if not recheck:
        notes.append("entry has no recheck: line after verified-at:")
    head_ids: set[str] = set()
    for line in src:
        head_ids.update(SID_RE.findall(line))
    missing = [s for s in ids if s not in head_ids]
    if missing:
        notes.append(f"cited {', '.join(missing)} absent from the entry's own "
                     f"source: lines (cited ids must be a subset of the "
                     f"entry's source: ids)")
    if notes:
        return False, notes

    # (b) every cited id is an 11-cell mined tier A/B row listing the entry.
    for sid in ids:
        rs = rows.get(sid, [])
        if len(rs) != 1:
            notes.append(f"{sid}: {len(rs)} registry rows in {SOURCES} "
                         f"(want exactly 1)")
            continue
        row = rs[0]
        if len(row) != 11:
            notes.append(f"{sid}: {len(row)} cells (want exactly 11)")
            continue
        if row[7] != "mined":
            notes.append(f"{sid}: status {row[7]!r} (want 'mined')")
            continue
        if row[3] not in ("A", "B"):
            notes.append(f"{sid}: tier {row[3]!r} (want A or B)")
            continue
        listed = [c.strip() for c in row[10].split(",")]
        if rule["entry"] not in listed:
            notes.append(f"{sid}: used-by {row[10]!r} does not list "
                         f"{rule['entry']}")
    if notes:
        return False, notes

    # (d) A4 only: located quote word-bounded in the pinned snapshot.
    if rule["snapshots"]:
        for sid in ids:
            quote, note = located_quote(entry_r, sid)
            if note:
                notes.append(note)
                continue
            snap = repo.snapshot(sid)          # raises EnvError: exit 2
            if not word_bounded(quote, norm(snap)):
                notes.append(f"{sid}: located quote not word-bounded in the "
                             f"pinned snapshot {SNAPSHOT_PINS[sid][0]}")
    if notes:
        return False, notes
    return True, []


def check(repo) -> tuple[int, list[str], list[tuple[str, str]]]:
    skill = repo.show(SKILL)
    if skill is None:
        raise EnvError(f"{SKILL} absent at {repo.rev}")
    sources = repo.show(SOURCES)
    if sources is None:
        raise EnvError(f"{SOURCES} absent at {repo.rev}")
    skill_r = rendered(skill)
    rows = source_rows(rendered(sources))
    findings: list[str] = []
    held: list[tuple[str, str]] = []
    for rid, rule in RULES.items():
        ok, notes = rule_holds(repo, skill_r, rows, rid, rule)
        if ok:
            held.append((rid, rule["entry"]))
        else:
            findings.extend(f"{rid}: {n}" for n in notes)
    return len(held), findings, held


# ---------------------------------------------------------------- self-test
# Every world below is an isolated local git repo under a fresh mktemp dir
# (Q48): no lane, no fleet repo and no shared index is ever touched.
# The fixture entries sit at the four FROZEN paths (plans/round-72.md § C1):
# a box naming any other path is not a match for its rule, by construction.
E1 = "corpus/knowledge/skill-name-precedence-round69.md"
E2 = "corpus/knowledge/instruction-authority-ladder-round67.md"
E3 = "corpus/knowledge/client-trust-gates-round68.md"
E4 = "corpus/knowledge/resident-index-and-rungs-round72.md"
Q4 = ("a prompt is a one-off, an always-on file is resident, a skill index "
      "names depth")
SNAP4 = "Rung map\n\nThe rule is plain: " + Q4 + ". Nothing above it.\n"
HONEST_PINS = {"S904": ("S904.page",
                        hashlib.sha256(SNAP4.encode()).hexdigest())}

BOX = {
    "A1": ("- [ ] A skill `name` is unique per install root, and the "
           "client's precedence order decides the winner when two roots "
           "hold the same name.\n"
           f"      (sourced: S900; entry: {E1})"),
    "A2": ("- [ ] The authority level of the body decides which instruction "
           "wins when an always-on file and a skill disagree.\n"
           f"      (sourced: S901, S902; entry: {E2})"),
    "A3": ("- [ ] An install path earns trust only after the command that "
           "writes it is read and reviewed.\n"
           f"      (sourced: S903; entry: {E3})"),
    "A4": ("- [ ] Decide the rung before writing: a one-off prompt, an "
           "always-on file, or a skill whose index names the depth file.\n"
           f"      (sourced: S904; entry: {E4})"),
}

_PAD = (" The fixture box keeps going for several more words so that its "
        "body clears the minimum length the counter requires.")
BOX = {k: v.replace("\n      (sourced", _PAD + "\n      (sourced", 1)
       for k, v in BOX.items()}

SKILL_FIX = ("# fixture skill\n\nIntro text.\n\n## Trigger-fidelity "
             "checklist\n\nRun before shipping.\n\n"
             + "\n".join(BOX[r] for r in ("A1", "A2", "A3", "A4"))
             + "\n\n## Agent-definition fidelity checklist\n\nnot this "
               "section\n")

ENTRY1 = (f'source: S900 — Roo Code — https://example.invalid/s900 — the '
          f'"Override Control" section — located quote "names are unique per '
          f'root"\nverified-at: 2026-10-25\n'
          f'recheck: 90d — re-fetch and confirm\n\n# Fixture name entry\n\nbody\n')
ENTRY2 = ('source: S901 — Model Spec — https://example.invalid/s901 — '
          '`# Instructions and levels of authority`\n'
          'source: S902 — arXiv:2604.09443 — https://example.invalid/s902 — '
          '`# abstract`\nverified-at: 2026-10-25\n'
          'recheck: 90d — re-fetch and confirm\n\n# Fixture authority entry\n')
ENTRY3 = (f'source: S903 — Kilo Code — https://example.invalid/s903 — the '
          f'"Shell commands in skills" section — located quote "skills in a '
          f'repository are reviewed before they run"\n'
          f'verified-at: 2026-10-25\n'
          f'recheck: 90d — re-fetch and confirm\n\n# Fixture install entry\n')
ENTRY4 = (f'source: S904 — Rung map — https://example.invalid/s904 — the '
          f'"Rung map" section — located quote "{Q4}"\n'
          f'verified-at: 2026-10-25\n'
          f'recheck: 90d — re-fetch and confirm\n\n# Fixture rung entry\n')


def _row(sid: str, entry: str, status: str = "mined",
         tier: str = "A") -> str:
    return (f"| {sid} | fixture — https://example.invalid/{sid} | docs | "
            f"{tier} | fixture scope | § fixture; opened 2026-10-25 | fixture "
            f"teaches cell | {status} | 2026-10-25 | 90d | {entry} |")


SOURCES_FIX = (
    "# SOURCES fixture\n\n## Registry\n\n"
    "| id | source | kind | tier | scope | anchor | teaches | status | "
    "opened | recheck | used-by |\n"
    "|---|---|---|---|---|---|---|---|---|---|---|\n"
    + "\n".join([_row("S900", E1), _row("S901", E2), _row("S902", E2),
                 _row("S903", E3), _row("S904", E4)])
    + "\n")


def _honest_files() -> dict[str, str]:
    return {
        SKILL: SKILL_FIX,
        SOURCES: SOURCES_FIX,
        E1: ENTRY1,
        E2: ENTRY2,
        E3: ENTRY3,
        E4: ENTRY4,
        f"{SNAPDIR}/S904.page": SNAP4,
    }


def _world(files: dict[str, str]) -> str:
    """A fresh isolated git repo holding ``files``, committed once."""
    d = tempfile.mkdtemp(prefix="k72-c1-")
    for rel, text in files.items():
        p = Path(d) / rel
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(text)
    env = dict(os.environ,
               GIT_AUTHOR_NAME="t", GIT_AUTHOR_EMAIL="t@t",
               GIT_COMMITTER_NAME="t", GIT_COMMITTER_EMAIL="t@t")
    git = ["git", "-c", "commit.gpgsign=false", "-C", d]
    subprocess.run(git + ["init", "-q"], check=True, capture_output=True)
    top = subprocess.run(git + ["rev-parse", "--show-toplevel"],
                         check=True, capture_output=True, text=True)
    if Path(top.stdout.strip()).resolve() != Path(d).resolve():
        raise RuntimeError(f"fixture toplevel {top.stdout.strip()!r} != {d}")
    subprocess.run(git + ["add", "-A"], check=True, capture_output=True)
    subprocess.run(git + ["commit", "-qm", "world"], check=True,
                   capture_output=True, env=env)
    return d


SECTION_NAME = "Trigger-fidelity checklist"


def _world_specs() -> list[dict]:
    """The world table: one satisfying world, then one broken world per
    conjunct and per shortcut control the plan names.  Every entry is
    materialized as its own isolated local git repo by ``_world``."""
    honest = _honest_files()

    def mutate(files: dict[str, str], **kw) -> dict[str, str]:
        out = dict(files)
        out.update(kw)
        return out

    three = "author-facing rules in SKILL.md 3 of 4"
    return [
        dict(label="honest world scores 4 of 4", files=honest, code=0,
             line="author-facing rules in SKILL.md 4 of 4", rule=None),
        # (a) six worlds
        dict(label="(a) box hidden in an HTML comment", rule="A1", code=1,
             files=mutate(honest, **{SKILL: SKILL_FIX.replace(
                 BOX["A1"], "<!--\n" + BOX["A1"] + "\n-->")}),
             line=three, finding="A1: 0 checklist box(es)"),
        dict(label="(a) box hidden in a fenced block", rule="A1", code=1,
             files=mutate(honest, **{SKILL: SKILL_FIX.replace(
                 BOX["A1"], "```text\n" + BOX["A1"] + "\n```")}),
             line=three, finding="A1: 0 checklist box(es)"),
        dict(label="(a) box moved outside the checklist section", rule="A1",
             code=1,
             files=mutate(honest, **{SKILL: SKILL_FIX.replace(
                 BOX["A1"] + "\n", "").replace(
                 "not this section\n",
                 "not this section\n\n" + BOX["A1"] + "\n")}),
             line=three, finding="A1: 0 checklist box(es)"),
        dict(label="(a) tail cites an id the entry never names", rule="A1",
             code=1,
             files=mutate(honest, **{
                 SKILL: SKILL_FIX.replace(
                     f"(sourced: S900; entry: {E1})",
                     f"(sourced: S999; entry: {E1})"),
                 SOURCES: SOURCES_FIX + _row("S999", E1) + "\n"}),
             line=three, finding="absent from the entry's own source: lines"),
        # errata E3: a token list under an honest tail is not a rule.
        dict(label="(a) token-only box under an honest tail (wave-1 w9)",
             rule="A1", code=1,
             files=mutate(honest, **{SKILL: SKILL_FIX.replace(
                 BOX["A1"], "- [ ] name unique precedence\n"
                 f"      (sourced: S900; entry: {E1})")}),
             line=three, finding="A1: 0 checklist box(es)"),
        # the tail path client-trust-gates-round68.md contains `trust`: a body
        # that never says trust/command must not borrow them from the path.
        dict(label="(a) rule tokens supplied only by the tail's entry path",
             rule="A3", code=1,
             files=mutate(honest, **{SKILL: SKILL_FIX.replace(
                 BOX["A3"],
                 f"- [ ] An install path is reviewed before it is written.\n"
                 f"      (sourced: S903; entry: {E3})")}),
             line=three, finding="A3: 0 checklist box(es)"),
        dict(label="(a) two boxes carry the same rule", rule="A1", code=1,
             files=mutate(honest, **{SKILL: SKILL_FIX.replace(
                 BOX["A1"] + "\n", BOX["A1"] + "\n" + BOX["A1"] + "\n")}),
             line=three, finding="A1: 2 checklist box(es)"),
        # (b) three worlds
        dict(label="(b) cited row is queued, not mined", rule="A1", code=1,
             files=mutate(honest, **{SOURCES: SOURCES_FIX.replace(
                 _row("S900", E1), _row("S900", E1, status="queued"))}),
             line=three, finding="status 'queued'"),
        dict(label="(b) cited row's used-by omits the entry", rule="A1",
             code=1,
             files=mutate(honest, **{SOURCES: SOURCES_FIX.replace(
                 _row("S900", E1), _row("S900", "corpus/knowledge/other.md"))}),
             line=three, finding="does not list"),
        dict(label="(b) cited id resolves in no registry row", rule="A2",
             code=1,
             files=mutate(honest, **{
                 SKILL: SKILL_FIX.replace(
                     f"(sourced: S901, S902; entry: {E2})",
                     f"(sourced: S901, S998; entry: {E2})"),
                 E2: ENTRY2.replace(
                     "source: S902 — arXiv:2604.09443 — "
                     "https://example.invalid/s902 — `# abstract`",
                     "source: S998 — arXiv:2604.09443 — "
                     "https://example.invalid/s998 — `# abstract`")}),
             line=three, finding="S998: 0 registry rows"),
        # (c) one world
        dict(label="(c) entry without verified-at:", rule="A1", code=1,
             files=mutate(honest, **{
                 E1: ENTRY1.replace("verified-at: 2026-10-25\n", "")}),
             line=three, finding="no verified-at: line"),
        # (d) four worlds
        dict(label="(d) A4 quote absent from its snapshot", rule="A4", code=1,
             files=mutate(honest, **{E4: ENTRY4.replace(
                 Q4, "a resident index costs context on every turn")}),
             line=three, finding="not word-bounded in the pinned snapshot"),
        dict(label="(d) tampered snapshot", rule="A4", code=2, files=honest,
             pins={"S904": ("S904.page", "0" * 64)},
             line="snapshot_tampered", finding="snapshot_tampered"),
        dict(label="(d) unfilled pin slot", rule="A4", code=2, files=honest,
             pins={"S904": ("", "")}, line="unfilled slot",
             finding="unfilled slot"),
        dict(label="(d) snapshot not committed at the measured rev", rule="A4",
             code=2, files=honest,
             pins={"S904": ("absent.page", hashlib.sha256(b"x").hexdigest())},
             line="not committed", finding="not committed"),
        # no section at all
        dict(label="section heading absent reads 0 of 4", rule=None, code=1,
             files=mutate(honest, **{SKILL: SKILL_FIX.replace(
                 "## Trigger-fidelity checklist",
                 "## Trigger-fidelity notes")}),
             line="author-facing rules in SKILL.md 0 of 4",
             finding="no `## Trigger-fidelity checklist` section"),
    ]


def _run_spec(spec: dict) -> tuple[bool, int, str]:
    """Run one world through ``main()`` in its own isolated git repo."""
    global SNAPSHOT_PINS
    saved = dict(SNAPSHOT_PINS)
    SNAPSHOT_PINS = dict(spec.get("pins") or HONEST_PINS)
    d = _world(spec["files"])
    buf = io.StringIO()
    try:
        with contextlib.redirect_stdout(buf), \
                contextlib.redirect_stderr(buf):
            code = main(["--repo", d, "--rev", "HEAD"])
    finally:
        shutil.rmtree(d, ignore_errors=True)
        SNAPSHOT_PINS = dict(saved)
    out = buf.getvalue()
    checks = [code == spec["code"]]
    if spec.get("line") is not None:
        checks.append(spec["line"] in out)
    if spec.get("finding") is not None:
        checks.append(spec["finding"] in out)
    ok = all(checks)
    msg = f"{spec['label']}: exit {code}"
    if not ok:
        msg += f" (want {spec['code']}); output={out!r}"
    return ok, len(checks), msg


def selftest() -> int:
    failures = 0
    assertions = 0
    for spec in _world_specs():
        ok, n, msg = _run_spec(spec)
        assertions += n
        if ok:
            print(f"PASS {msg}")
        else:
            failures += 1
            print(f"FAIL {msg}")
    print(f"self-test: {failures} failure(s) over {assertions} assertions")
    return 0 if failures == 0 else 1


def box_proof(map_path: Path) -> int:
    """``--box-proof --map <checklist-baseline.json>``.

    Proves the boxes the map delegates to this counter: every rule the map
    hands over is exercised by a satisfying world AND by at least one world
    that breaks one of its conjuncts, so a box mapped
    ``delegated:verifiers/check_author_rules.py`` is load-bearing rather than
    merely named.  Exit 0 only when the proof is complete.
    """
    if not map_path.is_file():
        print(f"box proof: no box map at {map_path}", file=sys.stderr)
        return 2
    try:
        data = json.loads(map_path.read_text())
    except (OSError, ValueError) as exc:
        print(f"box proof: map unreadable ({exc})", file=sys.stderr)
        return 2
    delegated = [b for b in data.get("boxes", [])
                 if str(b.get("section")) == SECTION_NAME
                 and str(b.get("disposition", "")).startswith("delegated:")
                 and "check_author_rules.py" in str(b.get("disposition"))]
    specs = _world_specs()
    covered = {s["rule"] for s in specs if s["rule"]}
    failures = 0
    for spec in specs:
        ok, _n, msg = _run_spec(spec)
        if not ok:
            failures += 1
            print(f"UNPROVEN {msg}")
    problems = []
    if len(delegated) != TOTAL:
        problems.append(f"the map delegates {len(delegated)} box(es) to "
                        f"check_author_rules.py (want {TOTAL})")
    if covered != set(RULES):
        problems.append(f"the proof covers {sorted(covered)} (want "
                        f"{sorted(RULES)})")
    if failures:
        problems.append(f"{failures} proof world(s) unproven")
    if problems:
        print("box proof: " + "; ".join(problems), file=sys.stderr)
        return 1
    print(f"boxes proven {len(delegated)}")
    return 0


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(
        description="C1 author-facing-rules counter for kotoba round 72")
    ap.add_argument("--rev", default=None, help="measured revision")
    ap.add_argument("--repo", default=str(_default_repo()))
    ap.add_argument("--census",
                    default="/home/vgpnk/Projects/shokunin/scripts/"
                            "sources-census.sh")
    ap.add_argument("--census-check", action="store_true",
                    help="also run sources-census.sh validate (second "
                         "evidence, never the verdict)")
    ap.add_argument("--self-test", action="store_true")
    ap.add_argument("--box-proof", action="store_true",
                    help="prove the boxes the checklist map delegates to "
                         "this counter")
    ap.add_argument("--map", default="verifiers/checklist-baseline.json",
                    help="box map for --box-proof")
    args = ap.parse_args(argv)
    if args.self_test:
        return selftest()
    if args.box_proof:
        return box_proof(Path(args.map))
    if not args.rev:
        print("environment error: --rev <revision> is required",
              file=sys.stderr)
        return 2
    repo = Repo(Path(args.repo), args.rev, args.census)
    if not (repo.path / SKILL).is_file() \
            or not (repo.path / SOURCES).is_file():
        print(f"environment error: --repo {repo.path} is not a lane worktree "
              f"(no {SKILL} and {SOURCES} on disk; pass --repo explicitly)",
              file=sys.stderr)
        return 2
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
        n, findings, held = check(repo)
    except EnvError as exc:
        print(f"environment error: {exc}", file=sys.stderr)
        return 2
    print(f"measured-rev: {args.rev}")
    print(f"author-facing rules in SKILL.md {n} of {TOTAL}")
    for f in findings:
        print(f"  {f}")
    if args.census_check:
        ok = repo.census_ok()
        if ok is None:
            print("census: could not evaluate")
        else:
            print(f"census validate: {'conformant' if ok else 'findings'}")
    return 0 if n == TOTAL else 1


if __name__ == "__main__":
    sys.exit(main())
