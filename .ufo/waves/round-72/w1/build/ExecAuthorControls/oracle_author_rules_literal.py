#!/usr/bin/env python3
"""oracle_author_rules_literal.py — a SEAT-LOCAL literal reading of the round-72 C1 predicate.

This is not the lane counter.  `verifiers/check_author_rules.py` does not exist at the base
(`ls verifiers | grep author` -> `check_instruction_authority.py` only), so the seat that owns the
counter has not frozen it yet.  This script exists so the control worlds are MEASURED against the
plan's frozen predicate sentence rather than merely predicted, and so the counter's author can
diff its reading against this one.

Predicate (plans/round-72.md § C1, verbatim):

    python3 -B verifiers/check_author_rules.py --rev <rev>  ->  prints
    "author-facing rules in SKILL.md N of 4", exit 0 when N == 4

Rule Ai holds at --rev iff, on committed bytes only:

 (a) the rendered SKILL.md (HTML comments and fenced blocks removed) has exactly one checklist box
     — a `- [ ] ` line plus its indented continuation lines — inside `## Trigger-fidelity
     checklist` (up to the next `## ` heading) whose joined text carries the rule's token set as
     whole words (A1 `name` `unique` `precedence`; A2 `authority` `level` `body`; A3 `install`
     `trust` `command`; A4 `prompt` `always-on` `skill` `index`) and ends with the tail
     `(sourced: S###[, S###…]; entry: <repo-relative path>)` naming that rule's frozen entry
     (A1 skill-name-precedence-round69.md, A2 instruction-authority-ladder-round67.md,
     A3 client-trust-gates-round68.md, A4 resident-index-and-rungs-round72.md) and at least one
     id from that entry's own `source:` lines;
 (b) every cited S### is an 11-cell registry row at --rev with status `mined`, tier A or B, and a
     `used-by` cell that lists the cited entry path;
 (c) the entry exists at --rev, opens with `source:` lines naming every cited id, then
     `verified-at:` and `recheck:`;
 (d) (A4 only) each cited row's located quote (the quote cell, 5-25 words) is found word-bounded in
     a committed, sha256-pinned snapshot of the cited page under `.ufo/waves/round-72/snapshots/`
     — a missing or tampered snapshot is exit 2.

Readings this script fixes where the sentence is silent (each named so a diff is possible):
  * "rendered": HTML comments `<!-- ... -->` (DOTALL) removed, then fenced blocks removed — a fence
    is a line of >=3 backticks or tildes, up to 3 leading spaces, toggling until the same marker
    closes it; fence lines themselves are removed.
  * "checklist box": a line starting `- [ ] ` at column 0; continuation lines are those with a
    non-empty body and leading whitespace, or blank lines followed by such a line.
  * "whole words": the token matches when neither neighbour is a letter, digit, `_` or `-`
    (`always-on` therefore matches as one token).
  * "the quote cell": the 11-cell row has no quote cell — the located quote lives inside the
    `anchor` cell after the literal marker `quote `; that span is the quote (2-word section names
    like "Product summary" are section labels, not located quotes).
  * "found word-bounded": both the quote and the snapshot are whitespace-collapsed to single
    spaces, then the quote must occur with a non-alphanumeric neighbour on each side.
  * the pin: `.ufo/waves/round-72/snapshots/<id>.sha256`, one `sha256  filename` line per capture
    (the convention already in the lane), falling back to `pins.json`
    (`{"snapshots": [{"id", "path", "sha256"}]}`); every pinned file of a cited id must exist and
    match its sha256 or the run is exit 2, and the located quote must be found in at least one of
    them (an id may pin more than one capture, e.g. a page plus its support pages).
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path

SKILL = "SKILL.md"
SOURCES = "corpus/SOURCES.md"
SNAP_DIR = ".ufo/waves/round-72/snapshots"
SECTION = "## Trigger-fidelity checklist"
ENTRIES = {
    "A1": "corpus/knowledge/skill-name-precedence-round69.md",
    "A2": "corpus/knowledge/instruction-authority-ladder-round67.md",
    "A3": "corpus/knowledge/client-trust-gates-round68.md",
    "A4": "corpus/knowledge/resident-index-and-rungs-round72.md",
}
TOKENS = {
    "A1": ["name", "unique", "precedence"],
    "A2": ["authority", "level", "body"],
    "A3": ["install", "trust", "command"],
    "A4": ["prompt", "always-on", "skill", "index"],
}
TAIL_RE = re.compile(r"\(sourced: (S\d{3}(?:, S\d{3})*); entry: ([^)\s]+)\)\s*$")
ID_RE = re.compile(r"\bS(\d{3,})\b")
COMMENT_RE = re.compile(r"<!--.*?-->", re.S)
FENCE_RE = re.compile(r"^ {0,3}(`{3,}|~{3,})")
ROW_RE = re.compile(r"^\| (S\d{3,}) \|")
SOURCE_LINE_RE = re.compile(r"^source:\s*(S\d{3,})\b")
QUOTED_RE = re.compile(r'quote\s+"([^"\n]{1,400})"')  # the located quote: `quote "..."` in anchor


class EnvError(Exception):
    pass


def git_show(repo: Path, rev: str, path: str) -> str | None:
    p = subprocess.run(["git", "-C", str(repo), "show", f"{rev}:{path}"],
                       capture_output=True, text=True)
    return p.stdout if p.returncode == 0 else None


def render(text: str) -> list[str]:
    out, fence = [], None
    for line in COMMENT_RE.sub("", text).splitlines():
        m = FENCE_RE.match(line)
        if fence is None and m:
            fence = m.group(1)[0]
            continue
        if fence is not None:
            if m and m.group(1)[0] == fence:
                fence = None
            continue
        out.append(line)
    return out


def section_lines(lines: list[str]) -> list[str]:
    start = None
    for i, l in enumerate(lines):
        if l.rstrip() == SECTION:
            start = i
            continue
        if start is not None and l.startswith("## "):
            return lines[start + 1:i]
    return lines[start + 1:] if start is not None else []


def boxes(lines: list[str]) -> list[str]:
    found, cur = [], None
    for l in lines:
        if l.startswith("- [ ] "):
            if cur is not None:
                found.append(cur)
            cur = l
        elif cur is not None and (l.strip() == "" or l[:1] in (" ", "\t")):
            cur += "\n" + l
        else:
            if cur is not None:
                found.append(cur)
            cur = None
    if cur is not None:
        found.append(cur)
    return found


def whole(token: str, text: str) -> bool:
    return re.search(r"(?<![\w-])" + re.escape(token) + r"(?![\w-])", text) is not None


def rows(sources: str) -> dict[str, list[str]]:
    table = {}
    for line in sources.splitlines():
        m = ROW_RE.match(line)
        if m:
            table[m.group(1)] = [c.strip() for c in line.strip().strip("|").split("|")]
    return table


def source_ids(entry_text: str) -> list[str]:
    return [m.group(1) for m in map(SOURCE_LINE_RE.match, entry_text.splitlines()) if m]


def pins_for(repo: Path, rev: str, ident: str) -> list[tuple[str, str]] | None:
    sums = git_show(repo, rev, f"{SNAP_DIR}/{ident}.sha256")
    out = []
    if sums:
        for line in sums.splitlines():
            parts = line.split()
            if len(parts) >= 2:
                out.append((f"{SNAP_DIR}/{parts[-1]}", parts[0]))
    if out:
        return out
    pj = git_show(repo, rev, f"{SNAP_DIR}/pins.json")
    if pj is None:
        return None
    try:
        return [(p["path"], p["sha256"]) for p in json.loads(pj)["snapshots"] if p["id"] == ident]
    except Exception:  # noqa: BLE001
        return None


def word_bound(quote: str, hay: str) -> bool:
    q = re.sub(r"\s+", " ", quote).strip()
    h = re.sub(r"\s+", " ", hay)
    pat = r"(?<![A-Za-z0-9])" + re.escape(q) + r"(?![A-Za-z0-9])"
    return re.search(pat, h) is not None


def check(repo: Path, rev: str) -> tuple[int, list[str], list[str]]:
    skill = git_show(repo, rev, SKILL)
    sources = git_show(repo, rev, SOURCES)
    if skill is None or sources is None:
        raise EnvError(f"{SKILL} or {SOURCES} absent at {rev}")
    rendered = render(skill)
    sect = section_lines(rendered)
    bs = boxes(sect)
    table = rows(sources)
    env_errors: list[str] = []
    notes: list[str] = []
    passed = 0

    for rule in ("A1", "A2", "A3", "A4"):
        entry = ENTRIES[rule]
        entry_text = git_show(repo, rev, entry)
        candidates = []
        for b in bs:
            joined = " ".join(b.split())
            if not all(whole(t, joined) for t in TOKENS[rule]):
                continue
            m = TAIL_RE.search(joined)
            if not m or m.group(2) != entry:
                continue
            if entry_text is None:
                continue
            cited = [i.strip() for i in m.group(1).split(",")]
            if not any(i in source_ids(entry_text) for i in cited):
                continue
            candidates.append((b, cited))
        if len(candidates) != 1:
            notes.append(f"{rule}: (a) candidates={len(candidates)}")
            continue
        b, cited = candidates[0]

        # (b)
        bad = []
        for i in cited:
            r = table.get(i)
            if r is None:
                bad.append(f"{i}: no registry row")
            elif len(r) != 11:
                bad.append(f"{i}: {len(r)} cells")
            elif r[7] != "mined":
                bad.append(f"{i}: status={r[7]}")
            elif r[3] not in ("A", "B"):
                bad.append(f"{i}: tier={r[3]}")
            elif entry not in [c.strip() for c in r[10].split(",")]:
                bad.append(f"{i}: used-by omits entry")
        if bad:
            notes.append(f"{rule}: (b) " + "; ".join(bad))
            continue

        # (c)
        if entry_text is None:
            notes.append(f"{rule}: (c) entry absent")
            continue
        head = [l for l in entry_text.splitlines() if l.strip()]
        ids = source_ids(entry_text)
        first_non_source = next((i for i, l in enumerate(entry_text.splitlines())
                                 if l.strip() and not l.startswith("source:")), 0)
        missing = [i for i in cited if i not in ids]
        if missing:
            notes.append(f"{rule}: (c) entry source: lines omit " + ",".join(missing))
            continue
        if not any(l.startswith("verified-at:") for l in entry_text.splitlines()) or \
           not any(l.startswith("recheck:") for l in entry_text.splitlines()):
            notes.append(f"{rule}: (c) no verified-at:/recheck:")
            continue
        if first_non_source > len([l for l in entry_text.splitlines() if l.startswith("source:")]):
            notes.append(f"{rule}: (c) source: lines not contiguous at the top")
            continue

        # (d)
        if rule == "A4":
            failed = False
            for i in cited:
                r = table[i]
                m = QUOTED_RE.search(r[5])
                if not m:
                    notes.append(f"{rule}: (d) {i} anchor carries no located quote")
                    failed = True
                    break
                quote = m.group(1)
                if not 5 <= len(quote.split()) <= 25:
                    notes.append(f"{rule}: (d) {i} quote {len(quote.split())} words")
                    failed = True
                    break
                pinned = pins_for(repo, rev, i)
                if not pinned:
                    env_errors.append(f"(d) {i} unpinned")
                    failed = True
                    break
                bodies = []
                for path, sha in pinned:
                    snap = git_show(repo, rev, path)
                    if snap is None:
                        env_errors.append(f"(d) {i} snapshot absent: {path.rsplit('/', 1)[1]}")
                        failed = True
                        break
                    got = hashlib.sha256(snap.encode()).hexdigest()
                    if got != sha:
                        env_errors.append(
                            f"(d) {i} snapshot sha256 {got[:12]} != pin ({path.rsplit('/', 1)[1]})")
                        failed = True
                        break
                    bodies.append(snap)
                if failed:
                    break
                if not any(word_bound(quote, b) for b in bodies):
                    notes.append(f"{rule}: (d) {i} quote absent from snapshot")
                    failed = True
                    break
            if failed:
                continue
        passed += 1

    return passed, notes, env_errors


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo", default=".")
    ap.add_argument("--rev", required=True)
    a = ap.parse_args()
    try:
        n, notes, env = check(Path(a.repo), a.rev)
    except EnvError as exc:
        print(f"environment error: {exc}", file=sys.stderr)
        return 2
    for note in notes:
        print("  " + note, file=sys.stderr)
    for e in env:
        print("  ENV " + e, file=sys.stderr)
    print(f"author-facing rules in SKILL.md {n} of 4")
    if env:
        return 2
    return 0 if n == 4 else 1


if __name__ == "__main__":
    sys.exit(main())
