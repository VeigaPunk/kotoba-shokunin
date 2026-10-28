#!/usr/bin/env python3
"""Kb81E07C2Worlds.ref-counter.py — PROVISIONAL inline reference counter.

Seat Kb81E07C2Worlds, kotoba round 81.  This file is MY instrument, not the
lane's counter and not a proposal for `verifiers/check_sdk_allowed_tools.py`.
It exists so the control worlds can be measured when seat Kb81E09C2Counter has
not yet published the real counter under `.ufo/waves/round-81/build/`.  Every
number produced with it is marked PROVISIONAL in `c2_controls.txt`.

Frozen predicate implemented (plans/round-81.md § C2, conjuncts (a)-(g)):

    python3 -B verifiers/check_sdk_allowed_tools.py --rev <rev>  ->  prints
    "sdk allowed-tools surface documented N of 1" and exits 0 iff N == 1 and
    the tree conjuncts hold; at the r81 base it prints 0 of 1 and exits 1.

Readings this reference takes (named so a reviewer can attack them):

  * committed bytes only: every file is read with `git cat-file -p <rev>:<path>`;
    the working tree is never read.  An untracked snapshot cannot satisfy (c)/(d).
  * (a) the entry `corpus/knowledge/allowed-tools-sdk-round81.md` has, in its
    head block, a `source:` line naming S249, the canonical URL and the snapshot
    basename, then `verified-at: 2026-10-27` then a `recheck:` line.
  * (b) exactly one `S249` registry row, 11 cells, status `mined`, tier A or B,
    its source cell carrying the canonical URL, its used-by cell naming the entry.
  * (c) the committed snapshot `.ufo/waves/round-81/snapshots/S249.md` hashes to
    the frozen pin, and the row's anchor carries a fetch record
    `fetched <date>[T..Z], HTTP 200, <bytes> B, sha256 <hex>` whose digest is
    the pin (the r80 counter's FETCHED_RE grammar: date optional time, digest
    optionally backticked).
  * (d) the entry's located quote is a quoted span of 3..25 words carrying
    `allowed-tools` or `allowedTools`; it occurs in the snapshot's text view
    (markdown: backticks deleted, unordered-list markers removed, whitespace
    collapsed per line; html: script/style dropped, tags -> space, entities
    decoded) after the first heading line (Q70).
  * (e) the S248 row's used-by cell names the entry.
  * (f) one SKILL.md line names the SDK channel (entry path + `allowedTools` +
    `SDK`) and SKILL.md carries a registry row whose first cell is
    `verifiers/check_sdk_allowed_tools.py` and whose kind cell is `gate`.
  * (g) `corpus/README.md` names the entry (full path, or the corpus-relative
    form its own coverage map uses) and `PROVINCE.md` `## Core` carries a line
    naming the entry and the SDK channel.

The word floor in (d) (3) is this reference's choice: the plan states only a
cap (<= 25 words).
"""

from __future__ import annotations

import argparse
import hashlib
import html
import re
import subprocess
import sys

PIN = "ac62c2dff61ef07bb778e5d115060e22f3f061fa3eca402be9b886946f01e5a2"
ENTRY = "corpus/knowledge/allowed-tools-sdk-round81.md"
SOURCES = "corpus/SOURCES.md"
SNAP = ".ufo/waves/round-81/snapshots/S249.md"
ROW_ID = "S249"
PRIOR_ID = "S248"
URL = "https://code.claude.com/docs/en/agent-sdk/skills.md"
CAPTURE = "2026-10-27"
COUNTER = "verifiers/check_sdk_allowed_tools.py"
SKILLMD = "SKILL.md"
PROVINCE = "PROVINCE.md"
README = "corpus/README.md"

REGISTRY_CELLS = 11
MIN_QUOTE_WORDS = 3
MAX_QUOTE_WORDS = 25
TOKEN_RE = re.compile(r"allowed-tools|allowedTools")
ROW_LINE_RE = re.compile(r"^ {0,3}\|\s*(S\d{3,})\s*\|")
FETCHED_RE = re.compile(
    r"fetched (\d{4}-\d\d-\d\d(?:T\d\d:\d\d:\d\dZ)?), HTTP 200, (\d+) B, "
    r"sha256 `?([0-9a-f]{64})`?")
QUOTE_RE = re.compile(r'["\u201c]([^"\u201d\n]{3,400})["\u201d]')
LIST_MARKER_RE = re.compile(r"^[ \t]{0,3}[*+\-][ \t]+")
SCRIPT_STYLE_RE = re.compile(r"(?is)<(script|style)\b.*?</\1\s*>")
TAG_RE = re.compile(r"(?s)</?[A-Za-z][^>]*>")


class EnvError(Exception):
    pass


def ws(text):
    return re.sub(r"\s+", " ", text).strip()


def sha256_bytes(data):
    return hashlib.sha256(data).hexdigest()


def split_cells(line):
    """Escape-aware markdown cell split; a ``\\|`` is cell content."""
    s = line.strip()
    if s.startswith("|"):
        s = s[1:]
    if s.endswith("|"):
        s = s[:-1]
    out, cur, i = [], "", 0
    while i < len(s):
        c = s[i]
        if c == "\\" and i + 1 < len(s) and s[i + 1] == "|":
            cur += "\\|"
            i += 2
            continue
        if c == "|":
            out.append(cur.strip())
            cur = ""
            i += 1
            continue
        cur += c
        i += 1
    out.append(cur.strip())
    return out


def clean(cell):
    return ws(cell.replace("`", ""))


def text_lines(name, raw):
    """The snapshot text view, line by line (r80 shaping, reimplemented)."""
    if name.lower().endswith((".html", ".htm")):
        s = SCRIPT_STYLE_RE.sub(" ", raw)
        s = TAG_RE.sub(" ", s)
        s = html.unescape(s)
        lines = [ws(x) for x in s.splitlines()]
    else:
        lines = []
        for ln in raw.splitlines():
            ln = LIST_MARKER_RE.sub("", ln)
            ln = ln.replace("`", "")
            lines.append(ws(ln))
    return [ln for ln in lines if ln]


class Tree:
    """Committed bytes of one measured revision (read-only)."""

    def __init__(self, repo, rev):
        self.repo = repo
        self.rev = rev
        probe = subprocess.run(
            ["git", "-C", repo, "rev-parse", "--verify", f"{rev}^{{commit}}"],
            capture_output=True)
        if probe.returncode != 0:
            raise EnvError(f"revision {rev} does not resolve in {repo}")
        self.rev = probe.stdout.decode().strip()

    def blob(self, path):
        proc = subprocess.run(
            ["git", "-C", self.repo, "cat-file", "-p", f"{self.rev}:{path}"],
            capture_output=True)
        return proc.stdout if proc.returncode == 0 else None


def head_block(text):
    """The entry's provenance trio: source: lines, then verified-at:, recheck:."""
    out = []
    for line in text.splitlines():
        if line.startswith(("source:", "verified-at:", "recheck:", "ground:")):
            out.append(line)
            continue
        if out and not line.strip():
            break
        if out:
            break
    return out


def registry_row(tree, row_id):
    text = tree.blob(SOURCES)
    if text is None:
        return None, "corpus/SOURCES.md is missing"
    rows = [ln for ln in text.decode("utf-8", "replace").splitlines()
            if ROW_LINE_RE.match(ln) and ROW_LINE_RE.match(ln).group(1) == row_id]
    if len(rows) != 1:
        return None, f"{row_id} row count {len(rows)} (want exactly 1)"
    cells = split_cells(rows[0])
    if len(cells) != REGISTRY_CELLS:
        return None, f"{row_id} row cells {len(cells)} (want {REGISTRY_CELLS})"
    return cells, None


def checked(tree):
    """Return (findings, detail) under conjuncts (a)-(g)."""
    found = []
    detail = {}

    # (a) entry head block
    entry_raw = tree.blob(ENTRY)
    if entry_raw is None:
        found.append(f"entry missing at {ENTRY}")
        entry = ""
    else:
        entry = entry_raw.decode("utf-8", "replace")
        head = head_block(entry)
        joined = " ".join(head)
        if not any(l.startswith("source:") for l in head):
            found.append("entry head carries no source: line")
        elif not (ROW_ID in joined and URL in joined and "S249.md" in joined):
            found.append("entry source: line does not name S249, the canonical "
                         "URL and the snapshot basename")
        if f"verified-at: {CAPTURE}" not in head:
            found.append(f"entry head lacks verified-at: {CAPTURE}")
        if not any(l.startswith("recheck:") for l in head):
            found.append("entry head lacks a recheck: line")

    # (b) S249 registry row
    row, why = registry_row(tree, ROW_ID)
    if why:
        found.append(why)
    else:
        if clean(row[7]) != "mined":
            found.append(f"S249 status {clean(row[7])!r} (want 'mined')")
        if clean(row[3]) not in ("A", "B"):
            found.append(f"S249 tier {clean(row[3])!r} (want 'A' or 'B')")
        if URL not in row[1]:
            found.append("S249 source cell does not carry the canonical URL")
        if ENTRY not in row[10]:
            found.append("S249 used-by does not name the entry")
        detail["row"] = row

    # (c) snapshot pin + fetch record
    snap = tree.blob(SNAP)
    if snap is None:
        found.append(f"snapshot missing at {SNAP}")
    else:
        digest = sha256_bytes(snap)
        detail["snapshot_sha256"] = digest
        if digest != PIN:
            found.append(f"snapshot sha256 {digest} is not the pin {PIN}")
    if row is not None:
        m = FETCHED_RE.search(row[5])
        if m is None:
            found.append("S249 anchor carries no "
                         "'fetched <date>[T..Z], HTTP 200, <bytes> B, "
                         "sha256 <hex>' record")
        elif m.group(3) != PIN:
            found.append(f"S249 anchor fetch sha256 {m.group(3)} is not the "
                         f"pin {PIN}")

    # (d) the located quote
    if entry:
        candidates = [ws(m.group(1)) for m in QUOTE_RE.finditer(entry)
                      if TOKEN_RE.search(m.group(1))]
        candidates = [c for c in candidates
                      if MIN_QUOTE_WORDS <= len(c.split()) <= MAX_QUOTE_WORDS]
        if not candidates:
            found.append("entry carries no quoted span of "
                         f"{MIN_QUOTE_WORDS}-{MAX_QUOTE_WORDS} words carrying "
                         "allowed-tools/allowedTools")
        elif snap is None:
            found.append("located quote cannot be checked: no committed "
                         "snapshot bytes")
        else:
            view = text_lines("S249.md", snap.decode("utf-8", "replace"))
            first_head = next((i for i, l in enumerate(view) if l.startswith("#")),
                              None)
            haystack = " ".join(view[(first_head + 1) if first_head is not None
                                     else 0:])
            located = [c for c in candidates if c in haystack]
            detail["quote"] = located[0] if located else candidates[0]
            if not located:
                found.append(f"quoted span {candidates[0]!r} does not occur in "
                             "the snapshot text view after the first heading")
            if first_head is None:
                found.append("snapshot text view carries no heading line")

    # (e) S248 used-by
    prior, why = registry_row(tree, PRIOR_ID)
    if why:
        found.append(why)
    elif ENTRY not in prior[10]:
        found.append("S248 used-by does not name the entry")

    # (f) SKILL.md rule line + registry row
    skill = tree.blob(SKILLMD)
    if skill is None:
        found.append("SKILL.md is missing")
    else:
        skill_text = skill.decode("utf-8", "replace")
        rule_ok = any(ENTRY in ln and "allowedTools" in ln and "SDK" in ln
                      for ln in skill_text.splitlines())
        if not rule_ok:
            found.append("SKILL.md carries no allowed-tools rule line naming "
                         "the entry and the SDK allowedTools channel")
        row_ok = False
        for ln in skill_text.splitlines():
            if not ln.lstrip().startswith("|"):
                continue
            cells = split_cells(ln)
            if len(cells) >= 7 and clean(cells[0]) == COUNTER \
                    and clean(cells[1]) == "gate" and "--rev" in ln:
                row_ok = True
                break
        if not row_ok:
            found.append(f"SKILL.md carries no conformant registry row for "
                         f"{COUNTER}")

    # (g) README + PROVINCE Core
    readme = tree.blob(README)
    readme_ok = False
    if readme is None:
        found.append("corpus/README.md is missing")
    else:
        readme_text = readme.decode("utf-8", "replace")
        # the coverage map names corpus files by their corpus-relative path
        readme_ok = (ENTRY in readme_text
                     or ENTRY[len("corpus/"):] in readme_text)
        if not readme_ok:
            found.append("corpus/README.md coverage map does not name the "
                         "entry")
    province = tree.blob(PROVINCE)
    if province is None:
        found.append("PROVINCE.md is missing")
    else:
        section, inside = [], False
        for ln in province.decode("utf-8", "replace").splitlines():
            if re.match(r"^##\s+Core\s*$", ln):
                inside = True
                continue
            if inside and re.match(r"^##\s+", ln):
                break
            if inside:
                section.append(ln)
        if not any(ENTRY in ln and ("allowedTools" in ln or "SDK" in ln)
                   for ln in section):
            found.append("PROVINCE.md ## Core does not name the SDK channel "
                         "and the entry")

    # the headline counts documented surfaces
    n = 1 if not found else 0
    return n, found, detail


def main(argv=None):
    ap = argparse.ArgumentParser(
        description="PROVISIONAL round-81 C2 reference counter "
                    "(seat Kb81E07C2Worlds)")
    ap.add_argument("--repo", default=".")
    ap.add_argument("--rev", default="HEAD")
    args = ap.parse_args(argv)

    try:
        tree = Tree(args.repo, args.rev)
        n, found, detail = checked(tree)
    except EnvError as exc:
        print(f"environment error: {exc}")
        return 2
    except Exception as exc:                      # noqa: BLE001 - fail closed
        print(f"environment error: {type(exc).__name__}: {exc}")
        return 2

    print(f"sdk allowed-tools surface documented {n} of 1")
    print(f"measured-rev: {tree.rev}")
    if "snapshot_sha256" in detail:
        print(f"snapshot sha256: {detail['snapshot_sha256']}")
    if "quote" in detail:
        print(f"located quote: {detail['quote']}")
    for item in found:
        print(f"  {item}")
    return 0 if n == 1 else 1


if __name__ == "__main__":
    sys.exit(main())
