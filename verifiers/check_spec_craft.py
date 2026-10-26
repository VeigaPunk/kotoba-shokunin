#!/usr/bin/env python3
"""check_spec_craft.py — frozen C1 counter for kotoba round 74 (depth).

FROZEN PREDICATE (the same sentence in plans/round-74.md § C1, in this
docstring and in the receipt):

    python3 -B verifiers/check_spec_craft.py --rev <rev>  ->  prints
    "spec craft pages backed N of 3", exit 0 when N == 3

Page ``P`` in {``best-practices``, ``using-scripts``, ``quickstart``} is
**backed** at ``--rev`` iff all of (a)-(f) hold over committed bytes only (no
network at measurement, and no instrument of the measured tree is executed):

  (a) the entry ``corpus/knowledge/spec-skill-creation-craft-round74.md``
      (frozen path) opens with ``source:`` lines for every cited id, then
      ``verified-at:`` and ``recheck:``, and has exactly one row for ``P`` in
      its rule table carrying at least two rule tokens (backticked commands or
      paths, or double-quoted rule sentences of at least five words), each
      located word-bounded in the committed snapshot of ``P``'s source;
  (b) ``P``'s cited ``S###`` is an 11-cell registry row, status ``mined``,
      tier ``A``, host ``agentskills.io``, ``opened`` equal to a round-74 date,
      ``used-by`` naming the entry, and the registry is census-conformant at
      ``--rev``;
  (c) ``P``'s snapshot under ``.ufo/waves/round-74/snapshots/`` has a sha256
      equal to the pin in the committed manifest
      ``.ufo/waves/round-74/snapshots/MANIFEST.sha256`` (missing or tampered
      snapshot is exit 2);
  (d) the row's located quote (5-25 words) is found in ``P``'s snapshot after
      whitespace collapse only;
  (e) *acted on:* the ``SKILL.md`` subsection
      ``### Body craft — the specification's skill-creation guides`` has at
      least two table rows citing ``P``'s ``S###``, each with an action cell of
      at least five words and at least one rule token that occurs in ``P``'s
      snapshot (a row that cites a page without a token of it does not count);
  (f) ``PROVINCE.md`` § Core names the entry.

The counter also prints ``held at base: H``, the do-nothing figure: the
number of the three pages whose exact page URL already appears in a
``corpus/SOURCES.md`` row at
``BASE_REV = 1e03d1991bc02281b00a5b7a5e00c9d5d5d72908`` (0 at base, the
phrase sweep of ``.ufo/waves/round-74/receipts/base-sweeps.txt``).

AMENDED BEFORE ANY DATA by plans/round-74-addendum-1.md E1.1 (the headline,
the target and the conjunct letters are unchanged; each tightening below was
measured by a wave-1 seat on a committed world):

  (a') at least one of a row's tokens is PAGE-UNIQUE: word-bounded in the
       page's own snapshot and in neither of the other two pages' snapshots
       (the site-chrome banner and the page subtitle are shared text);
  (b') the cited row's first URL path is /skill-creation/<page>.md (already
       read below as the URL binding);
  (c') the snapshot's sha256 equals the manifest pin, a CONSTANT pinned in
       this file (PAGE_SHA: the measured revision cannot supply its own trust
       anchor, Q33) and the 64-hex digest in the cited registry row's anchor
       cell; snapshots/FETCH-LOG.tsv records `page url status bytes sha256
       date` with status 200 and bytes/sha equal to the snapshot;
  (d') the quote's line lies after the page's first `# ` heading, is not a
       heading, is not a line of the blockquote block between that heading and
       the first `## ` heading, and is not a link to another skill-creation
       page;
  (e') each counting SKILL.md row's action cell has >= 1 page-unique token
       and >= 5 content words: words that are neither inside a backticked or
       quoted span nor members of FILLER (a pinned lexical approximation of
       "says something", named as one, like the base checker's G1).

Word-bounded means ASCII-lookaround ``(?<![A-Za-z0-9_])..(?![A-Za-z0-9_])``
over the whitespace-collapsed snapshot.  Bound (Q26/Q51): form, sources,
tokens and pinned bytes are counted; whether a rule sentence is true of its
page is reviewer judgement and no counter makes it.

READINGS that are deliberately stricter than the naive one, named here so a
reviewer can attack them rather than discover them:

  * the rule table is a markdown table whose header, with backticks and
    emphasis stripped and lower-cased, begins with ``page`` and also carries
    ``rule``, ``quote``, ``tokens`` and one of ``s id`` / ``sid`` / ``id``
    (the plan's columns ``page | S id | rule | quote | tokens | action``).  A
    page row is a row whose first cell equals the page name after the same
    cleaning, a trailing ``.md`` ignored (the entry may name the page as its
    file).  Exactly one such row may exist for a page across every rule table.
  * the counted tokens are the spans of the row's ``tokens`` cell only: a
    backticked span of at least two characters, or a double-quoted span of at
    least five words.  The ``quote`` cell is NOT a token source, so a quote
    can never double as one of the two tokens, and a single-character
    backticked span is not a command or a path.  Tokens are compared distinct
    and located literally and ASCII-word-bounded in the page's snapshot read
    whitespace-collapsed: no slash or tilde shaping.  A token the page writes
    with a trailing ``/`` may
    therefore be written without it (the ``/`` is an ASCII word boundary), but
    a token is never matched by prefix across a word character: ``scripts/``
    does not locate ``scripts/validate.py``, and ``.agents/skill`` does not
    locate ``.agents/skills/``.
  * word-bounded means ASCII-word-bounded (``[A-Za-z0-9_]``), not ``\\w``: a
    CJK character abutting a path is a boundary, not a word character.
  * the ``S id`` cell must name exactly one id (the column is singular); a row
    naming two ids is ambiguous and does not back its page.
  * a pin is bound to the page the row cites: (1) the row's FIRST URL must be
    on host ``agentskills.io`` exactly (a subdomain is another host) and its
    path must be ``/skill-creation/<page>.md`` or ``/skill-creation/<page>``;
    (2) the entry's own ``source:`` line for that id must carry a URL whose
    host+path equals that first URL (trailing ``/`` ignored, path case kept).
    Without the binding a seat could pin a committed snapshot of an EASIER
    page to a hard URL and (c)/(d) would read true of the wrong page; the
    binding can only fail more.
  * the snapshot of a page is resolved by basename: the single committed
    manifest key whose basename is ``<page>.md`` (so a key written as
    ``best-practices.md`` or ``.ufo/waves/round-74/snapshots/best-practices.md``
    both resolve).  Two such keys, a key escaping the snapshot directory, a
    missing key, an uncommitted file or a digest mismatch is exit 2 (could not
    evaluate), never a pass and never a content fail — except that an ABSENT
    entry returns 0 of 3 / exit 1 before any manifest is read, which is what
    makes the plan's do-nothing control at base read ``0 of 3``, exit 1.
  * the entry-level trio (all leading ``source:`` lines, then
    ``verified-at:``, then ``recheck:``) and ``cited ids ⊆ the entry's own
    source: ids`` are read once for the whole entry: a trio broken for one
    page is broken for all three (0 of 3), because the entry is the claim's
    single surface.  Ids glued to a slug (``best-practices.md``) are snapshot
    file names, not citations.
  * the quote of (d) is the single double-quoted span of the row's ``quote``
    cell (curly quotes accepted); the ``source:`` line's quote is not
    consulted, so a row cannot inherit the source-line quote.  The match is
    whitespace-collapsed exact containment: no backtick stripping, no case
    folding, no entity decoding.
  * the census is run once per measurement over the revision's registry
    (``git archive``, never the worktree), with ``--today 2026-10-26`` so the
    E08 future-date check is deterministic across the round-74 window; the
    counter's own ``opened`` window check (2026-10-25 or 2026-10-26) still
    rejects every date outside it.  The census is consulted only after a
    page's row-level (b) checks pass: skipping it there changes no verdict.
  * the SKILL.md section runs from the exact heading line to the next heading
    of level one to three (a ``####`` sub-heading stays inside); the heading
    line must equal the frozen string byte for byte after trailing-whitespace
    trimming (a hyphen instead of the em dash, or a curly apostrophe, does not
    count).  The action cell is the cell under an ``action`` header, else the
    row's last cell, and the rule token must occur in that cell (a token
    elsewhere in the row does not substitute).  Rows are counted, not
    disqualifying: a row that fails its word or token test simply does not
    count toward the two.

Exit codes: 0 iff N == 3; 1 otherwise (a content verdict); 2 could not
evaluate (unknown revision, unreadable registry, absent/unreadable census
script, missing/tampered/ambiguous pinned snapshot, unreadable base registry).
``--self-test`` runs the world table (one satisfying world, one broken world
per conjunct (a)-(f), the plan's shortcut controls and the cannot-evaluate
cases) in isolated local git repos under fresh ``mktemp -d`` directories: no
lane, no fleet repo and no shared index is ever touched.  ``--print-self-sha``
prints the blanked sha of this file (the L1 refills ``SELF_SHA`` after any edit
and before freeze).

Usage:
  python3 -B verifiers/check_spec_craft.py --rev <rev> [--repo <lane>]
  python3 -B verifiers/check_spec_craft.py --self-test
  python3 -B verifiers/check_spec_craft.py --print-self-sha
"""

from __future__ import annotations

import argparse
import contextlib
import hashlib
import io
import os
import re
import shutil
import subprocess
import sys
import tempfile
import urllib.parse
from pathlib import Path

TOTAL = 3
PAGES = ("best-practices", "using-scripts", "quickstart")
SOURCES = "corpus/SOURCES.md"
ENTRY = "corpus/knowledge/spec-skill-creation-craft-round74.md"
SNAPDIR = ".ufo/waves/round-74/snapshots"
MANIFEST = SNAPDIR + "/MANIFEST.sha256"
COUNTER_PATH = "verifiers/check_spec_craft.py"
PROVINCE = "PROVINCE.md"
SKILLMD = "SKILL.md"
HOST = "agentskills.io"
OPENED = ("2026-10-25", "2026-10-26")
CENSUS_TODAY = "2026-10-26"
SKILL_HEADING = "### Body craft — the specification's skill-creation guides"
CENSUS = "/home/vgpnk/Projects/shokunin/scripts/sources-census.sh"

# Frozen at freeze 1: the base lane tip the do-nothing control is measured at.
# The self-test rebinds this module global to a fixture repo's own first commit
# (there is no CLI flag to move it: a measurement always reads this constant).
BASE_REV = "1e03d1991bc02281b00a5b7a5e00c9d5d5d72908"

MIN_TOKENS = 2
MIN_BACKTICK_CHARS = 2
MIN_QUOTED_TOKEN_WORDS = 5
MIN_QUOTE_WORDS = 5
MAX_QUOTE_WORDS = 25
MIN_ACTION_WORDS = 5
MIN_SKILL_ROWS = 2
REGISTRY_CELLS = 11
FETCHLOG = SNAPDIR + "/FETCH-LOG.tsv"
# Q33: the three page digests are constants of this instrument.  A landing that
# edits a snapshot, its manifest line and its registry row together is still
# refused: the pin is not read from the measured revision.
PAGE_SHA = {
    "best-practices":
        "ab9f3b6091a0f24816b52cd7b90a3fdf53e621f47dba13b36694be272b87fb41",
    "using-scripts":
        "2cd7727106b423a758b4b6b1ab3545da74845a98e68e6718279846f89d62ad1f",
    "quickstart":
        "7c480b447edac58fd8ff8f250c471dfc7d4621155b91fabed46379075c32bffb",
}
FILLER = frozenset(
    "use see page pages guide says say said the as for this that these those "
    "with and or of to a an it its is are be by on in at you your from "
    "then than also just so can may".split())
SHA_RE = re.compile(r"(?<![0-9a-f])([0-9a-f]{64})(?![0-9a-f])")

SID_RE = re.compile(r"\bS\d{3,}\b")
BACKTICK_RE = re.compile(r"`([^`]+)`")
QUOTE_RE = re.compile(r'["\u201c]([^"\u201d]+)["\u201d]')
CITED_TAIL_RE = re.compile(r"-[A-Za-z]")
REGISTRY_RE = re.compile(r"^ {0,3}\|\s*S\d{3,}\s*\|")
URL_RE = re.compile(r"https?://[^\s)>\]]+")
SEPARATOR_RE = re.compile(r":?-{3,}:?")
HEADING_RE = re.compile(r"^#{1,3}\s")
TRIM_CHARS = ".,;:!?)]}'\""
SELF_SHA = "50f29a8bb930b5b3657741cf9c99a8159b31cc3afe2542d6d7f60b92d89abb9c"   # blanked-sha of this file
SELF_LINE_RE = re.compile(r'^SELF_SHA = "[0-9a-f]*"', re.M)


class EnvError(Exception):
    """Could not evaluate: exit 2, never a pass and never a fail."""


# --------------------------------------------------------------- text shaping

def _blanked_sha(text: str) -> str:
    return hashlib.sha256(
        SELF_LINE_RE.sub('SELF_SHA = ""', text).encode()).hexdigest()


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


def ws(text: str) -> str:
    """Collapse every whitespace run to one space (the ONLY shaping (d) allows)."""
    return re.sub(r"\s+", " ", text).strip()


def word_bounded(needle: str, haystack: str) -> bool:
    """ASCII-word-bounded occurrence: a CJK character is a boundary."""
    return re.search(
        r"(?<![A-Za-z0-9_])" + re.escape(needle) + r"(?![A-Za-z0-9_])",
        haystack) is not None


def cited_sids(text: str) -> list[str]:
    """``S###`` ids that cite a registry row, in order, deduplicated.

    An id glued to a slug (``S231-bp.md``) is a snapshot file name, not a
    citation of that row, so it is skipped."""
    out: list[str] = []
    for m in SID_RE.finditer(text):
        if CITED_TAIL_RE.match(text, m.end()):
            continue
        if m.group(0) not in out:
            out.append(m.group(0))
    return out


def clean(cell: str) -> str:
    """Cell comparison form: drop emphasis/backticks, collapse, lower-case."""
    return ws(re.sub(r"[`*]", "", cell)).lower()


def _cells(line: str) -> list[str]:
    s = line.strip()
    if not (s.startswith("|") and s.endswith("|")) or len(s) < 2:
        return []
    return [c.strip() for c in s[1:-1].split("|")]


def is_separator(row: list[str]) -> bool:
    return bool(row) and all(SEPARATOR_RE.fullmatch(x) for x in row)


def tables(text: str):
    """Yield (header_cells, row_cells) for every markdown table in ``text``."""
    block: list[str] = []

    def flush():
        if not block:
            return None
        head = _cells(block[0])
        rows = []
        for ln in block[1:]:
            c = _cells(ln)
            if not c or is_separator(c):
                continue
            rows.append(c)
        block.clear()
        return head, rows

    for ln in text.splitlines():
        if ln.strip().startswith("|"):
            block.append(ln)
            continue
        got = flush()
        if got is not None:
            yield got
    got = flush()
    if got is not None:
        yield got


def _cell(head: list[str], row: list[str], name: str) -> str | None:
    try:
        i = head.index(name)
    except ValueError:
        return None
    return row[i] if 0 <= i < len(row) else None


# ------------------------------------------------------------- entry surface

def entry_head(text: str) -> tuple[list[str], str | None, str | None]:
    """The provenance trio: leading ``source:`` lines, then verified-at, recheck."""
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


def page_of_cell(cell: str) -> str | None:
    """Which frozen page a rule table's first cell names."""
    name = clean(cell)
    if name.endswith(".md"):
        name = name[:-3]
    return name if name in PAGES else None


def rule_rows(text: str):
    """Yield (cleaned header, row cells) for every rule table row."""
    for head, rows in tables(text):
        h = [clean(c) for c in head]
        if not h or h[0] != "page":
            continue
        if "rule" not in h or "quote" not in h or "tokens" not in h:
            continue
        if not any(x in ("s id", "sid", "id") for x in h):
            continue
        for row in rows:
            yield h, row


def page_rows(text: str) -> dict[str, list[tuple[list[str], list[str]]]]:
    """page -> its rule table rows, in document order."""
    out: dict[str, list[tuple[list[str], list[str]]]] = {}
    for head, row in rule_rows(text):
        if not row:
            continue
        page = page_of_cell(row[0])
        if page:
            out.setdefault(page, []).append((head, row))
    return out


def sid_cell(head: list[str], row: list[str]) -> str:
    for name in ("s id", "sid", "id"):
        value = _cell(head, row, name)
        if value is not None:
            return value
    return ""


def tokens_in(text: str) -> list[str]:
    """Rule tokens of a cell: backticked spans (>=2 chars) and >=5-word quotes."""
    out: list[str] = []
    for tok in BACKTICK_RE.findall(text):
        t = ws(tok)
        if len(t) >= MIN_BACKTICK_CHARS and t not in out:
            out.append(t)
    for q in QUOTE_RE.findall(text):
        n = ws(q)
        if n and len(n.split()) >= MIN_QUOTED_TOKEN_WORDS and n not in out:
            out.append(n)
    return out


def quoted_spans(text: str) -> list[str]:
    """Every distinct double-quoted span of a cell, whitespace-collapsed."""
    out: list[str] = []
    for q in QUOTE_RE.findall(text):
        n = ws(q)
        if n and n not in out:
            out.append(n)
    return out


def token_occurrences(token: str, text: str) -> bool:
    """A token is located only literally, word-bounded: no slash or tilde shaping."""
    return word_bounded(token, text)


def entry_problems(entry_r: str) -> list[str]:
    """Entry-level (a): the trio, and cited ids covered by the source: lines."""
    notes: list[str] = []
    rows = page_rows(entry_r)
    if not rows:
        return ["no rule table row names any of " + ", ".join(PAGES)
                + " (the entry has no rule table)"]
    src, verified, recheck = entry_head(entry_r)
    if not src:
        notes.append("entry does not open with source: lines")
    if not verified:
        notes.append("entry has no verified-at: line after its source: lines")
    if not recheck:
        notes.append("entry has no recheck: line after verified-at:")
    cited: list[str] = []
    for page in PAGES:
        for head, row in rows.get(page, []):
            for sid in cited_sids(sid_cell(head, row)):
                if sid not in cited:
                    cited.append(sid)
    if not cited:
        notes.append("the rule table cites no S### id")
    head_ids: set[str] = set()
    for line in src:
        # the ids a source: line names are those before its located quote: the
        # tail's snapshot file name (`best-practices.md`) is not a source id.
        head_ids.update(cited_sids(line.split("located quote")[0]))
    missing = [s for s in cited if s not in head_ids]
    if missing:
        notes.append("cited " + ", ".join(missing) + " absent from the entry's "
                     "own source: lines (cited ids must be a subset of them)")
    return notes


# ------------------------------------------------------------------ git side

def _default_repo() -> Path:
    here = Path(__file__).resolve()
    for cand in [here.parent.parent, *here.parents]:
        if (cand / SOURCES).is_file():
            return cand
    return here.parent.parent


def _git(repo: Path, args: list[str]) -> subprocess.CompletedProcess:
    try:
        return subprocess.run(["git", "-C", str(repo), *args],
                              capture_output=True)
    except OSError as exc:
        raise EnvError(f"git not runnable: {exc}") from exc


class Repo:
    """Committed bytes of one lane at one revision (read-only)."""

    def __init__(self, path: Path, rev: str):
        self.path, self.rev = path, rev
        self._manifest: dict[str, str] | None = None
        self._census: bool | None = None
        self._snapsha: dict[str, tuple[str, int]] = {}
        self._fetchlog: dict[str, list[str]] | None = None

    def show_at(self, rev: str, path: str) -> str | None:
        proc = _git(self.path, ["show", f"{rev}:{path}"])
        if proc.returncode == 0:
            return proc.stdout.decode("utf-8", "replace")
        err = proc.stderr.decode("utf-8", "replace")
        if "does not exist" in err or "exists on disk, but not in" in err \
                or "Path '" in err:
            return None
        raise EnvError(f"git show {rev}:{path} failed: {err.strip()}")

    def show(self, path: str) -> str | None:
        return self.show_at(self.rev, path)

    def manifest(self) -> dict[str, str]:
        """``path -> sha256`` from the committed manifest (exit 2 when unreadable)."""
        if self._manifest is not None:
            return self._manifest
        text = self.show(MANIFEST)
        if text is None:
            raise EnvError(f"no manifest at {MANIFEST} at {self.rev}: the "
                           f"snapshots are unpinned, so (c) cannot be evaluated")
        out: dict[str, str] = {}
        for n, line in enumerate(text.splitlines(), 1):
            s = line.strip()
            if not s or s.startswith("#"):
                continue
            m = re.fullmatch(r"([0-9a-f]{64})[ \t]+\*?(\S(?:.*\S)?)", s)
            if not m:
                raise EnvError(f"{MANIFEST}:{n} is not `<sha256> <relative "
                               f"file>`: {s!r}")
            sha, name = m.group(1), m.group(2)
            pure = Path(name)
            if pure.is_absolute() or name.startswith("/") or ".." in pure.parts:
                raise EnvError(f"{MANIFEST}:{n} pins {name!r}, which escapes "
                               f"{SNAPDIR}/")
            if name in out and out[name] != sha:
                raise EnvError(f"{MANIFEST}:{n} pins {name!r} to a second "
                               f"digest {sha} (first {out[name]})")
            out[name] = sha
        if not out:
            raise EnvError(f"{MANIFEST} pins no snapshot")
        self._manifest = out
        return out

    def snapshot(self, page: str) -> str:
        """The committed, pinned snapshot bytes of one page."""
        name = page + ".md"
        man = self.manifest()
        keys = [k for k in man if k.rsplit("/", 1)[-1] == name]
        if len(keys) != 1:
            raise EnvError(f"{MANIFEST} pins {len(keys)} files whose basename "
                           f"is {name} (want exactly 1)")
        key = keys[0]
        rel = key if key.startswith(SNAPDIR + "/") else SNAPDIR + "/" + key
        proc = _git(self.path, ["show", f"{self.rev}:{rel}"])
        if proc.returncode != 0:
            raise EnvError(f"snapshot {rel} not committed at {self.rev}")
        digest = hashlib.sha256(proc.stdout).hexdigest()
        if digest != man[key]:
            raise EnvError(f"snapshot_tampered: {rel}")
        if page in PAGE_SHA and digest != PAGE_SHA[page]:
            raise EnvError(f"snapshot_pin_mismatch: {rel} sha256 {digest} is "
                           f"not the digest pinned in the counter")
        self._snapsha[page] = (digest, len(proc.stdout))
        return proc.stdout.decode("utf-8", "replace")

    def snapsha(self, page: str) -> tuple[str, int]:
        """(sha256, bytes) of the pinned snapshot (loads it when needed)."""
        if page not in self._snapsha:
            self.snapshot(page)
        return self._snapsha[page]

    def fetchlog(self) -> dict[str, list[str]] | None:
        """page -> ``[url, status, bytes, sha256, date]`` from FETCH-LOG.tsv."""
        if self._fetchlog is not None:
            return self._fetchlog
        text = self.show(FETCHLOG)
        if text is None:
            return None
        out: dict[str, list[str]] = {}
        for line in text.splitlines():
            s = line.strip()
            if not s or s.startswith("#"):
                continue
            cells = [c.strip() for c in s.split("\t")]
            if len(cells) == 6 and cells[0] in PAGES:
                out[cells[0]] = cells[1:]
        self._fetchlog = out
        return out

    def census_ok(self) -> bool:
        """``sources-census.sh validate --file`` on the revision's registry."""
        if self._census is not None:
            return self._census
        script = Path(CENSUS)
        if not script.is_file():
            raise EnvError(f"census script {CENSUS} is not present: (b) cannot "
                           f"be evaluated")
        arch = _git(self.path, ["archive", self.rev])
        if arch.returncode != 0:
            raise EnvError(f"git archive {self.rev} failed")
        with tempfile.TemporaryDirectory(prefix="k74-c1census-") as td:
            root = Path(td)
            (root / "tree.tar").write_bytes(arch.stdout)
            subprocess.run(["tar", "-xf", "tree.tar"], cwd=root,
                           capture_output=True)
            target = root / SOURCES
            if not target.is_file():
                raise EnvError(f"{SOURCES} absent from the tree at {self.rev}")
            proc = subprocess.run(["bash", str(script), "validate", "--file",
                                   str(target), "--today", CENSUS_TODAY],
                                  capture_output=True, text=True, timeout=120)
        if proc.returncode == 0:
            self._census = True
        elif proc.returncode == 1:
            self._census = False
        else:
            raise EnvError(f"census validate exited {proc.returncode}: "
                           f"{(proc.stdout + proc.stderr).strip()[:300]}")
        return self._census


# ------------------------------------------------------------- registry side

def registry_rows(text: str) -> dict[str, list[list[str]]]:
    """id -> registry rows (raw cells; the cell count is judged later)."""
    rows: dict[str, list[list[str]]] = {}
    for line in text.splitlines():
        if REGISTRY_RE.match(line):
            cells = _cells(line)
            if cells:
                rows.setdefault(cells[0], []).append(cells)
    return rows


def urls_of(cell: str) -> list[str]:
    return [m.group(0).rstrip(TRIM_CHARS) for m in URL_RE.finditer(cell)]


def host_exact(url: str) -> bool:
    """Q32: the host equals ``agentskills.io``; a subdomain is another host."""
    try:
        parts = urllib.parse.urlsplit(url)
    except ValueError:
        return False
    return (parts.hostname or "").lower() == HOST


def page_key(url: str) -> tuple[str, str]:
    """Host + path of a page, ignoring a trailing ``/`` and the query/fragment."""
    parts = urllib.parse.urlsplit(url)
    return ((parts.hostname or "").lower(),
            urllib.parse.unquote(parts.path or "").rstrip("/").lower())


def page_of_url(url: str) -> str | None:
    """The frozen page a URL IS (exact host and the page's own path), else None."""
    if not host_exact(url):
        return None
    try:
        path = urllib.parse.unquote(
            urllib.parse.urlsplit(url).path or "").rstrip("/").lower()
    except ValueError:
        return None
    for page in PAGES:
        if path in ("/skill-creation/%s.md" % page, "/skill-creation/%s" % page):
            return page
    return None


def source_line(entry_r: str, sid: str) -> str | None:
    """The entry's own leading ``source:`` line that names one cited id."""
    for line in entry_r.splitlines():
        if line.startswith("source:") and sid in cited_sids(line):
            return line
    return None


def registry_problems(ctx: "Ctx", page: str, sid: str) -> list[str]:
    """(b) for one page's cited id."""
    rows = ctx.registry.get(sid, [])
    if len(rows) != 1:
        return [f"{page}: {sid}: {len(rows)} registry rows in {SOURCES} "
                f"(want exactly 1)"]
    row = rows[0]
    if len(row) != REGISTRY_CELLS:
        return [f"{page}: {sid}: {len(row)} cells (want exactly "
                f"{REGISTRY_CELLS})"]
    notes: list[str] = []
    if row[7].strip() != "mined":
        notes.append(f"{page}: {sid}: status {row[7].strip()!r} (want 'mined')")
    if row[3].strip() != "A":
        notes.append(f"{page}: {sid}: tier {row[3].strip()!r} (want 'A')")
    opened = row[8].strip()
    if opened not in OPENED:
        notes.append(f"{page}: {sid}: opened {opened!r} is not a round-74 date "
                     f"({OPENED[0]} or {OPENED[1]})")
    listed = [c.strip() for c in row[10].split(",")]
    if ENTRY not in listed:
        notes.append(f"{page}: {sid}: used-by {row[10]!r} does not list {ENTRY}")
    urls = urls_of(row[1])
    if not urls:
        notes.append(f"{page}: {sid}: source cell holds no URL")
    else:
        if not any(host_exact(u) for u in urls):
            notes.append(f"{page}: {sid}: no URL on host {HOST} "
                         f"(exact host, not a subdomain): {urls}")
        if page_of_url(urls[0]) != page:
            notes.append(f"{page}: {sid}: the first URL {urls[0]} is not the "
                         f"{page} page (/skill-creation/{page}.md)")
        line = source_line(ctx.entry_r, sid)
        if line is None:
            notes.append(f"{page}: {sid}: no source: line in the entry names it")
        elif not any(page_key(u) == page_key(urls[0]) for u in urls_of(line)):
            notes.append(f"{page}: {sid}: the entry's source: line carries no "
                         f"URL for the cited page {urls[0]} — the pinned "
                         f"snapshot is not demonstrably the page the row cites")
    return notes


# -------------------------------------------------------------- SKILL.md side

def quote_line_problems(raw: str, quote: str, page: str) -> list[str]:
    """(d'): where in the raw snapshot the located quote starts."""
    lines = raw.splitlines()
    buf, starts = "", []
    for i, line in enumerate(lines):
        t = ws(line)
        if not t:
            continue
        if buf:
            buf += " "
        starts.append((len(buf), i))
        buf += t
    at = buf.find(quote)
    if at < 0:
        return []                      # the caller reports the missing quote
    li = max(i for s, i in starts if s <= at)
    h1 = next((i for i, ln in enumerate(lines) if ln.startswith("# ")), None)
    notes: list[str] = []
    if h1 is None or li <= h1:
        notes.append(f"{page}: the located quote sits at snapshot line "
                     f"{li + 1}, not after the page's first `# ` heading "
                     f"(site chrome is not a rule)")
        return notes
    if lines[li].lstrip().startswith("#"):
        notes.append(f"{page}: the located quote is a heading (line {li + 1})")
    h2 = next((i for i in range(h1 + 1, len(lines))
               if lines[i].startswith("## ")), len(lines))
    if li < h2 and lines[li].lstrip().startswith(">"):
        notes.append(f"{page}: the located quote is the page subtitle "
                     f"blockquote (line {li + 1}), not a rule")
    if re.search(r"\]\([^)]*skill-creation/", lines[li]):
        notes.append(f"{page}: the located quote is a link to another "
                     f"skill-creation page (line {li + 1})")
    return notes


def content_words(action: str, sid: str) -> list[str]:
    """Words of an action cell outside code/quoted spans and not FILLER."""
    text = BACKTICK_RE.sub(" ", action)
    text = QUOTE_RE.sub(" ", text)
    text = SID_RE.sub(" ", text)
    words = re.findall(r"[A-Za-z][A-Za-z'-]+", text)
    return [w.lower() for w in words
            if len(w) >= 2 and w.lower() not in FILLER]


def page_unique(tok: str, own: str, others: list[str]) -> bool:
    return token_occurrences(tok, own) and not any(
        token_occurrences(tok, o) for o in others)


def skill_section(text: str) -> tuple[str | None, int]:
    """The body of the frozen subsection: (text, number of heading matches)."""
    if not text:
        return None, 0
    lines = rendered(text).splitlines()
    idx = [i for i, ln in enumerate(lines) if ln.rstrip() == SKILL_HEADING]
    if len(idx) != 1:
        return None, len(idx)
    start = idx[0]
    end = next((i for i in range(start + 1, len(lines))
                if HEADING_RE.match(lines[i])), len(lines))
    return "\n".join(lines[start + 1:end]), 1


def skill_problems(section: str | None, page: str, sid: str,
                   snap: str, nhead: int = 1,
                   others: list[str] | None = None) -> list[str]:
    """(e) for one page: at least two counting rows citing its id."""
    if section is None:
        return [f"{page}: SKILL.md has no single heading line "
                f"{SKILL_HEADING!r} ({nhead} match(es))"]
    counted = 0
    notes: list[str] = []
    for head, rows in tables(section):
        h = [clean(c) for c in head]
        for row in rows:
            if sid not in cited_sids(" ".join(row)):
                continue
            ai = h.index("action") if "action" in h else len(row) - 1
            action = row[ai].strip() if 0 <= ai < len(row) else ""
            words = len(ws(action).split())
            if words < MIN_ACTION_WORDS:
                notes.append(f"{page}: SKILL.md row citing {sid} has {words} "
                             f"action word(s) (want >= {MIN_ACTION_WORDS})")
                continue
            toks = tokens_in(action)
            if not any(token_occurrences(t, snap) for t in toks):
                notes.append(f"{page}: SKILL.md row citing {sid} carries no "
                             f"{page} token in its action cell: {toks}")
                continue
            if others is not None and not any(
                    page_unique(t, snap, others) for t in toks):
                notes.append(f"{page}: SKILL.md row citing {sid} carries no "
                             f"page-unique {page} token in its action cell: "
                             f"{toks}")
                continue
            cw = content_words(action, sid)
            if len(cw) < MIN_ACTION_WORDS:
                notes.append(f"{page}: SKILL.md row citing {sid} has "
                             f"{len(cw)} content word(s) outside tokens and "
                             f"the filler list (want >= {MIN_ACTION_WORDS})")
                continue
            counted += 1
    if counted < MIN_SKILL_ROWS:
        notes.append(f"{page}: SKILL.md subsection has {counted} counting "
                     f"row(s) citing {sid} (want >= {MIN_SKILL_ROWS})")
    return notes


def province_named(text: str | None) -> bool:
    """(f): a ``## Core`` bullet names the frozen entry path."""
    if not text:
        return False
    lines = rendered(text).splitlines()
    start = next((i for i, ln in enumerate(lines)
                  if re.match(r"^## Core\s*$", ln)), None)
    if start is None:
        return False
    end = next((i for i in range(start + 1, len(lines))
                if lines[i].startswith("## ")), len(lines))
    bullets: list[str] = []
    for line in lines[start + 1:end]:
        if line.startswith("- "):
            bullets.append(line)
        elif line.strip() and bullets and line.startswith("  "):
            bullets[-1] += " " + ws(line)
    return any(ENTRY in b for b in bullets)


# -------------------------------------------------------------------- verdict

class Ctx:
    def __init__(self, repo: Repo, entry_r: str,
                 registry: dict[str, list[list[str]]],
                 rows: dict[str, list[tuple[list[str], list[str]]]]):
        self.repo, self.entry_r = repo, entry_r
        self.registry, self.rows = registry, rows
        self.section, self.section_n = skill_section(repo.show(SKILLMD) or "")


def page_holds(ctx: Ctx, page: str) -> tuple[bool, list[str]]:
    mine = ctx.rows.get(page, [])
    if len(mine) != 1:
        return False, [f"{page}: {len(mine)} rule-table row(s) in {ENTRY} "
                       f"(want exactly 1)"]
    head, row = mine[0]
    ids = cited_sids(sid_cell(head, row))
    if len(ids) != 1:
        return False, [f"{page}: the S id cell names {len(ids)} id(s) "
                       f"({sid_cell(head, row)!r}); want exactly 1"]
    sid = ids[0]
    notes: list[str] = []

    # (a) structure: the tokens cell and the quote cell exist, tokens declared
    tok_cell = _cell(head, row, "tokens")
    toks = tokens_in(tok_cell or "")
    if len(toks) < MIN_TOKENS:
        notes.append(f"{page}: the tokens cell carries {len(toks)} rule "
                     f"token(s) (want >= {MIN_TOKENS}): {toks}")
    qcell = _cell(head, row, "quote")
    if qcell is None:
        notes.append(f"{page}: the rule table row has no quote cell")
    if notes:
        return False, notes

    # (b) registry row, then the whole-registry census conformance
    notes.extend(registry_problems(ctx, page, sid))
    if notes:
        return False, notes
    if not ctx.repo.census_ok():
        return False, [f"{page}: {SOURCES} is not census-conformant at "
                       f"{ctx.repo.rev} (conjunct (b))"]

    # (c) the pinned snapshot (missing/tampered raises exit 2).  Every match
    # below reads it whitespace-collapsed: the only shaping (d) names, and the
    # same shaping the round-73 counter applied, so a token or a quote wrapped
    # across a line still locates.
    raw = ctx.repo.snapshot(page)
    snap = ws(raw)
    others = [ws(ctx.repo.snapshot(p)) for p in PAGES if p != page]
    digest, size = ctx.repo.snapsha(page)

    # (a) tokens located word-bounded in THIS page's snapshot
    for tok in toks:
        if not token_occurrences(tok, snap):
            notes.append(f"{page}: token {tok!r} does not occur word-bounded "
                         f"in {page}.md")

    # (a') at least one page-unique token (site chrome is shared text)
    located = [t for t in toks if token_occurrences(t, snap)]
    if located and not any(page_unique(t, snap, others) for t in located):
        notes.append(f"{page}: no page-unique token among {located}: every "
                     f"located token also occurs in another page's snapshot")

    # (c') the anchor digest and the fetch record of the cited row
    reg = ctx.registry.get(sid, [])
    anchor = reg[0][5] if reg and len(reg[0]) == REGISTRY_CELLS else ""
    if digest not in SHA_RE.findall(anchor):
        notes.append(f"{page}: {sid}: the anchor cell carries no sha256 equal "
                     f"to the pinned snapshot ({digest[:12]}...)")
    log = ctx.repo.fetchlog()
    rec = None if log is None else log.get(page)
    if rec is None:
        notes.append(f"{page}: no fetch record for {page} in {FETCHLOG} at "
                     f"{ctx.repo.rev}")
    else:
        url, status, nbytes, sha, date = rec
        if status != "200":
            notes.append(f"{page}: fetch record status {status!r} (want 200)")
        if nbytes != str(size):
            notes.append(f"{page}: fetch record bytes {nbytes} != snapshot "
                         f"{size}")
        if sha != digest:
            notes.append(f"{page}: fetch record sha256 is not the snapshot's")
        if page_of_url(url) != page:
            notes.append(f"{page}: fetch record URL {url} is not the {page} "
                         f"page")

    # (d) the row's located quote, exactly one 5-25-word span, found verbatim
    spans = quoted_spans(qcell)
    if len(spans) != 1:
        notes.append(f"{page}: the quote cell holds {len(spans)} distinct "
                     f"quoted span(s) (want exactly 1)")
    else:
        quote = spans[0]
        words = len(quote.split())
        if not MIN_QUOTE_WORDS <= words <= MAX_QUOTE_WORDS:
            notes.append(f"{page}: located quote is {words} words "
                         f"(want {MIN_QUOTE_WORDS}-{MAX_QUOTE_WORDS})")
        elif quote not in snap:
            notes.append(f"{page}: located quote not found in {page}.md after "
                         f"whitespace collapse: {quote!r}")
        else:
            notes.extend(quote_line_problems(raw, quote, page))

    # (e) acted on in SKILL.md
    notes.extend(skill_problems(ctx.section, page, sid, snap, ctx.section_n,
                                others))
    return (not notes), notes


def held_at_base(repo: Repo) -> int:
    """Pages whose exact page URL already appears in the base registry."""
    base = repo.show_at(BASE_REV, SOURCES)
    if base is None:
        raise EnvError(f"{SOURCES} unreadable at base {BASE_REV}")
    rows = registry_rows(rendered(base))
    seen: set[str] = set()
    for cells in rows.values():
        for row in cells:
            for url in urls_of(row[1] if len(row) > 1 else ""):
                page = page_of_url(url)
                if page:
                    seen.add(page)
    return len([p for p in PAGES if p in seen])


def check(repo: Repo) -> tuple[int, list[str], list[str]]:
    sources = repo.show(SOURCES)
    if sources is None:
        raise EnvError(f"{SOURCES} absent at {repo.rev}")
    entry_text = repo.show(ENTRY)
    if entry_text is None:
        return 0, [f"entry {ENTRY} absent at {repo.rev} (the frozen path is "
                   f"the entry's only home)"], []
    entry_r = rendered(entry_text)
    problems = entry_problems(entry_r)
    if problems:
        return 0, problems, []
    ctx = Ctx(repo, entry_r, registry_rows(rendered(sources)),
              page_rows(entry_r))
    n, findings, backed = 0, [], []
    for page in PAGES:
        ok, notes = page_holds(ctx, page)
        if ok:
            n += 1
            backed.append(page)
        else:
            findings.extend(notes)
    return n, findings, backed


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(
        description="C1 spec skill-creation craft counter for kotoba round 74")
    ap.add_argument("--rev", default=None, help="measured revision")
    ap.add_argument("--repo", default=str(_default_repo()),
                    help="the measured git worktree (resolved before anything "
                         "is derived)")
    ap.add_argument("--self-test", action="store_true")
    ap.add_argument("--print-self-sha", action="store_true",
                    help="print the blanked sha of this file and exit")
    args = ap.parse_args(argv)
    if args.print_self_sha:
        print(_blanked_sha(Path(__file__).read_text()))
        return 0
    if args.self_test:
        return selftest()
    if not args.rev:
        print("environment error: --rev <revision> is required",
              file=sys.stderr)
        return 2
    # Q66: the repo argument is resolved before any path is derived from it.
    repo_path = Path(args.repo).expanduser().resolve()
    repo = Repo(repo_path, args.rev)
    top = _git(repo.path, ["rev-parse", "--show-toplevel"])
    if top.returncode != 0:
        print(f"environment error: --repo {args.repo} is not a git worktree",
              file=sys.stderr)
        return 2
    proc = _git(repo.path, ["rev-parse", "--verify", "-q",
                            f"{args.rev}^{{commit}}"])
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
        held = held_at_base(repo)
        named = province_named(repo.show(PROVINCE))
    except EnvError as exc:
        print(f"environment error: {exc}", file=sys.stderr)
        return 2
    if not named:
        n, backed = 0, []
        findings.insert(0, f"PROVINCE.md § Core does not name {ENTRY} "
                           f"(conjunct (f) holds for every page)")
    print(f"measured-rev: {args.rev}")
    print(f"spec craft pages backed {n} of {TOTAL}")
    print(f"held at base: {held}")
    print("province core names the entry: " + ("yes" if named else "no"))
    for page in backed:
        print(f"  backed: {page}")
    for finding in findings:
        print(f"  {finding}")
    return 0 if n == TOTAL else 1


# ---------------------------------------------------------------- self-test
# Every world is an isolated local git repo under a fresh mktemp dir with TWO
# commits: the first is the "base" state the do-nothing figure is read from,
# the second the measured tip.  No lane, fleet repo or shared index is touched.
BANNER = ("> Fetch the complete documentation index at: "
          "https://agentskills.io/llms.txt\n"
          "> Use this file to discover all available pages before exploring "
          "further.\n\n")
SUBTITLE_OF = {
    "best-practices": "A calibrated fixture subtitle sentence for best practices.",
    "using-scripts": "A calibrated fixture subtitle sentence about scripts.",
    "quickstart": "A calibrated fixture subtitle sentence about the quickstart.",
}
LINK_LINE = ("See [the scripts guide](https://agentskills.io/skill-creation/"
             "using-scripts.md) for helper scripts details.")
SNAP_TEXT = {
    "best-practices.md": (
        BANNER + "# Skill authoring best practices\n\n> "
        + SUBTITLE_OF["best-practices"] + "\n\n## Defaults\n\n"
        "Keep the SKILL.md focused on what the skill does and when to use it.\n"
        "Prefer a small number of defaults over a menu of options.\n"
        "Validate a helper with scripts/validate.py before you ship it.\n\n"
        "## Keep every defaults list short and sharp\n\n" + LINK_LINE + "\n"),
    "using-scripts.md": (
        BANNER + "# Using scripts in a skill\n\n> "
        + SUBTITLE_OF["using-scripts"] + "\n\n## Commands\n\n"
        "Bundle a helper under scripts/ and run it with uvx ruff check.\n"
        "Cap a one-off command's output so it fits the context window.\n"
        "Reference the SKILL.md file from the helper docs.\n"),
    "quickstart.md": (
        BANNER + "# Quickstart\n\n> " + SUBTITLE_OF["quickstart"]
        + "\n\n## Prerequisites\n\n"
        "Create the directory .agents/skills/ and add a SKILL.md file.\n"
        "Check it with python -m skills_ref.check before committing.\n"),
}

QUOTE = {
    "best-practices": "Prefer a small number of defaults over a menu of options.",
    "using-scripts": "Cap a one-off command's output so it fits the context window.",
    "quickstart": "Create the directory .agents/skills/ and add a SKILL.md file.",
}

SID_OF = {"best-practices": "S231", "using-scripts": "S232",
          "quickstart": "S233"}
PAGE_OF_SID = {v: k for k, v in SID_OF.items()}
URL_OF = {p: "https://agentskills.io/skill-creation/%s.md" % p for p in PAGES}

TOKENS_OF = {
    "best-practices": "`scripts/validate.py`, "
                      "\"Prefer a small number of defaults\"",
    "using-scripts": "`scripts/`, `uvx ruff check`",
    "quickstart": "`.agents/skills/`, `python -m skills_ref.check`",
}

RULE_OF = {
    "best-practices": "prefer a small set of defaults over a menu",
    "using-scripts": "bundle helpers under scripts/ and cap their output",
    "quickstart": "create the skills directory first, then the file",
}

SKILL_ROWS = {
    "best-practices": [
        "| best-practices (S231) | Validate every helper with "
        "`scripts/validate.py` before you ship it. |",
        "| best-practices (S231) | Ship one default path and quote "
        "\"Prefer a small number of defaults\" in the note. |",
    ],
    "using-scripts": [
        "| using-scripts (S232) | Bundle a helper under `scripts/` and call it "
        "from the skill. |",
        "| using-scripts (S232) | Cap output with `uvx ruff check` before the "
        "harness sees it. |",
    ],
    "quickstart": [
        "| quickstart (S233) | Create `.agents/skills/` first, then the skill "
        "file itself. |",
        "| quickstart (S233) | Check the whole tree with `python -m "
        "skills_ref.check` before committing changes. |",
    ],
}

REG_HEADER = ("| id | source | kind | tier | scope | anchor | teaches | "
              "status | opened | recheck | used-by |\n"
              "|---|---|---|---|---|---|---|---|---|---|---|")


def _entry_text(quotes: dict[str, str] | None = None,
                sids: dict[str, str] | None = None,
                tokens: dict[str, str] | None = None,
                rows: dict[str, str] | None = None,
                trio: bool = True) -> str:
    quotes = dict(QUOTE, **(quotes or {}))
    sids = dict(SID_OF, **(sids or {}))
    tokens = dict(TOKENS_OF, **(tokens or {}))
    head = []
    for page in PAGES:
        head.append(
            f'source: {sids[page]} — Agent Skills — fixture {page} — '
            f'{URL_OF[page]} — the fixture section — located quote '
            f'"{quotes[page]}" (snapshot `{page}.md:3`)')
    body = [""]
    if trio:
        body += ["verified-at: 2026-10-25",
                 "recheck: 90d — re-fetch and re-locate"]
    body += ["", "# Spec skill-creation craft (fixture)", "",
             "| page | S id | rule | quote | tokens | action |",
             "|---|---|---|---|---|---|"]
    for page in PAGES:
        cell = rows[page] if rows and page in rows else (
            f"| {page} | {sids[page]} | {RULE_OF[page]} | "
            f"\"{quotes[page]}\" | {tokens[page]} | apply the rule |")
        body.append(cell)
    return "\n".join(head + body) + "\n"


def _rule_row(page: str) -> str:
    return (f"| {page} | {SID_OF[page]} | {RULE_OF[page]} | "
            f"\"{QUOTE[page]}\" | {TOKENS_OF[page]} | apply the rule |")


def _hide(row: str, opener: str, closer: str) -> str:
    """The entry with ``row`` out of the table and kept only as hidden bytes."""
    text = _entry_text()
    assert row + "\n" in text, row
    return (text.replace(row + "\n", "") + "\n" + opener + "\n"
            + row + "\n" + closer + "\n")


def _fetchlog(snaps: dict[str, str] | None = None,
              status: str = "200") -> str:
    snaps = SNAP_TEXT if snaps is None else snaps
    lines = ["# page\turl\tstatus\tbytes\tsha256\tdate"]
    for page in PAGES:
        text = snaps.get(page + ".md")
        if text is None:
            continue
        lines.append("\t".join([page, URL_OF[page], status,
                                str(len(text.encode())), _sha(text),
                                "2026-10-25"]))
    return "\n".join(lines) + "\n"


def _repin(files: dict[str, str | None]) -> dict[str, str | None]:
    """Re-sign manifest, fetch log and registry digests after a world edits a
    snapshot on purpose (the edit is the world's point; the books follow)."""
    snaps = {rel.rsplit("/", 1)[-1]: text
             for rel, text in files.items()
             if rel.startswith(SNAPDIR + "/") and text is not None
             and rel.endswith(".md") and "FETCH" not in rel}
    out = _mutate(files, **{MANIFEST: _manifest(snaps), FETCHLOG: _fetchlog(snaps)})
    reg = out.get(SOURCES)
    if reg is not None:
        for name, text in snaps.items():
            if name in SNAP_TEXT and text != SNAP_TEXT[name]:
                reg = reg.replace(_sha(SNAP_TEXT[name]), _sha(text))
        out[SOURCES] = reg
    return out


def _sha(text: str) -> str:
    return hashlib.sha256(text.encode()).hexdigest()


def _reg_line(sid: str, *, url: str | None = None, status: str = "mined",
              tier: str = "A", opened: str = "2026-10-25",
              used_by: str = ENTRY, extra: int = 0, kind: str = "docs",
              scope: str = "fixture scope", sha: str | None = None) -> str:
    page = PAGE_OF_SID.get(sid)
    url = url or (URL_OF[page] if page else "https://agentskills.io/x")
    if sha is None:
        sha = _sha(SNAP_TEXT[page + ".md"]) if page else "0" * 64
    cells = [sid, f"Agent Skills — fixture page — {url}",
             kind, tier, scope,
             "§ fixture section; fetched 2026-10-25T10:00:00Z, HTTP 200, "
             "4000 B, sha256 " + sha,
             "fixture teaches cell", status, opened, "90d", used_by]
    cells += [f"extra{i}" for i in range(extra)]
    return "| " + " | ".join(cells) + " |"


def _registry(lines: list[str] | None = None) -> str:
    body = lines if lines is not None else [_reg_line(s)
                                            for s in sorted(SID_OF.values())]
    return ("# SOURCES fixture\n\n## Registry\n\n" + REG_HEADER + "\n"
            + "\n".join(body) + "\n")


def _manifest(snaps: dict[str, str] | None = None) -> str:
    snaps = SNAP_TEXT if snaps is None else snaps
    return "".join(f"{hashlib.sha256(v.encode()).hexdigest()}  {k}\n"
                   for k, v in snaps.items())


def _skill_text(rows: dict[str, list[str]] | None = None,
                heading: str = SKILL_HEADING,
                outside: str | None = None) -> str:
    rows = SKILL_ROWS if rows is None else rows
    body = [f"# fixture skill", "",
            "## Router model", "", "- fixture line", "",
            heading, "", "| Page | Action |", "|---|---|"]
    for page in PAGES:
        body.extend(rows.get(page, []))
    body += ["", "## Gate registry", "",
             "Registry home under the protocol, one row per gate.", "",
             "| Name | Kind |", "|---|---|",
             "| `verifiers/check_spec_craft.py` | gate |"]
    if outside:
        body.append(outside)
    return "\n".join(body) + "\n"


PROVINCE_OK = ("# fixture province\n\n## Core\n\n- Body craft from the "
               "specification's own skill-creation guides: `" + ENTRY
               + "`, counted by the counter.\n\n## Frontier\n\n- none\n")


def _honest_files() -> dict[str, str]:
    files = {SOURCES: _registry(), ENTRY: _entry_text(),
             MANIFEST: _manifest(), PROVINCE: PROVINCE_OK,
             SKILLMD: _skill_text(), FETCHLOG: _fetchlog()}
    for name, text in SNAP_TEXT.items():
        files[f"{SNAPDIR}/{name}"] = text
    return files


def _world(files: dict[str, str | None],
           base_files: dict[str, str] | None = None) -> tuple[str, str]:
    """A fresh isolated git repo: one base commit, then the measured commit."""
    d = tempfile.mkdtemp(prefix="k74-c1-")
    env = dict(os.environ, GIT_AUTHOR_NAME="t", GIT_AUTHOR_EMAIL="t@t",
               GIT_COMMITTER_NAME="t", GIT_COMMITTER_EMAIL="t@t")
    git = ["git", "-c", "commit.gpgsign=false", "-C", d]
    subprocess.run(git + ["init", "-q"], check=True, capture_output=True)
    top = subprocess.run(git + ["rev-parse", "--show-toplevel"], check=True,
                         capture_output=True, text=True)
    if Path(top.stdout.strip()).resolve() != Path(d).resolve():
        raise RuntimeError(f"fixture toplevel {top.stdout.strip()!r} != {d}")

    def commit(note: str) -> str:
        subprocess.run(git + ["add", "-A"], check=True, capture_output=True)
        subprocess.run(git + ["commit", "-qm", note, "--allow-empty"],
                       check=True, capture_output=True, env=env)
        rev = subprocess.run(git + ["rev-parse", "HEAD"], check=True,
                             capture_output=True, text=True)
        return rev.stdout.strip()

    def place(items: dict[str, str | None]) -> None:
        for rel, text in items.items():
            p = Path(d) / rel
            if text is None:               # a fixture deletion, not a file
                if p.exists():
                    p.unlink()
                continue
            p.parent.mkdir(parents=True, exist_ok=True)
            p.write_text(text)

    place(base_files if base_files is not None else {SOURCES: _registry([])})
    base_sha = commit("base")
    place(files)
    commit("world")
    return d, base_sha


def _mutate(files: dict[str, str | None],
            **kw: str | None) -> dict[str, str | None]:
    out = dict(files)
    out.update(kw)
    return out


def _world_specs() -> list[dict]:
    """One honest world, then one broken world per conjunct and per shortcut."""
    honest = _honest_files()
    L3 = "spec craft pages backed 3 of 3"
    L2 = "spec craft pages backed 2 of 3"
    L0 = "spec craft pages backed 0 of 3"
    specs: list[dict] = []
    add = specs.append

    # ---------------------------------------------------------- honest worlds
    add(dict(label="honest world scores 3 of 3", files=honest, code=0,
             line=L3, finding="held at base: 0"))
    add(dict(label="relative --repo . resolves before deriving (Q66)",
             files=honest, code=0, line=L3, repo_arg=".", cwd=True))
    add(dict(label="base world (entry absent) is the do-nothing control",
             files={SOURCES: _registry()}, code=1, line=L0,
             finding="absent at"))
    add(dict(label="held at base counts a page already in the base registry",
             files=honest,
             base_files={SOURCES: _registry([
                 _reg_line("S900", url=URL_OF["best-practices"])])},
             code=0, line=L3, finding="held at base: 1"))
    add(dict(label="opened 2026-10-26 is inside the round-74 window",
             files=_mutate(honest, **{SOURCES: _registry([
                 _reg_line(s, opened="2026-10-26")
                 for s in sorted(SID_OF.values())])}),
             code=0, line=L3, finding="held at base: 0"))
    add(dict(label="manifest key written with the snapshot directory prefix",
             files=_mutate(honest, **{MANIFEST: "".join(
                 hashlib.sha256(v.encode()).hexdigest()
                 + "  " + SNAPDIR + "/" + k + "\n"
                 for k, v in SNAP_TEXT.items())}),
             code=0, line=L3))
    add(dict(label="(d) quote wrapped across a line break is still found",
             files=_repin(_mutate(honest, **{
                 f"{SNAPDIR}/best-practices.md":
                     SNAP_TEXT["best-practices.md"].replace(
                         "number of defaults", "number of\ndefaults")})),
             code=0, line=L3, finding="held at base: 0"))
    add(dict(label="(e) a #### sub-heading stays inside the subsection",
             files=_mutate(honest, **{SKILLMD: _skill_text().replace(
                 "| Page | Action |", "#### Worked example\n\n| Page | Action |",
                 1)}), code=0, line=L3, finding="backed: quickstart"))

    # ------------------------------------------------------- (a) rule table
    add(dict(label="(a) entry without verified-at:", files=_mutate(
        honest, **{ENTRY: _entry_text(trio=False)}),
        code=1, line=L0, finding="no verified-at: line"))
    add(dict(label="(a) entry without recheck:", files=_mutate(
        honest, **{ENTRY: _entry_text().replace(
            "recheck: 90d — re-fetch and re-locate\n", "")}),
        code=1, line=L0, finding="no recheck: line"))
    add(dict(label="(a) cited id absent from the source: lines", files=_mutate(
        honest, **{ENTRY: _entry_text().replace(
            "source: S232 —", "source: S932 —")}),
        code=1, line=L0,
        finding="cited S232 absent from the entry's own source: lines"))
    add(dict(label="(a) two rule-table rows for one page", files=_mutate(
        honest, **{ENTRY: _entry_text() + _rule_row("best-practices") + "\n"}),
        code=1, line=L2,
        finding="best-practices: 2 rule-table row(s)"))
    add(dict(label="(a) entry with no rule table", files=_mutate(
        honest, **{ENTRY: _entry_text().replace(
            "| page | S id | rule | quote | tokens | action |",
            "| pg | S id | rule | quote | tokens | action |")}),
        code=1, line=L0, finding="no rule table row names any of"))
    add(dict(label="(a) row hidden in an HTML comment", files=_mutate(
        honest, **{ENTRY: _hide(_rule_row("best-practices"), "<!--", "-->")}),
        code=1, line=L2,
        finding="best-practices: 0 rule-table row(s)"))
    add(dict(label="(a) row hidden in a fenced block", files=_mutate(
        honest, **{ENTRY: _hide(_rule_row("quickstart"), "```text", "```")}),
        code=1, line=L2,
        finding="quickstart: 0 rule-table row(s)"))
    add(dict(label="(a) row naming two ids is ambiguous", files=_mutate(
        honest, **{ENTRY: _entry_text().replace(
            "| best-practices | S231 |", "| best-practices | S231, S232 |")}),
        code=1, line=L2, finding="the S id cell names 2 id(s)"))
    add(dict(label="(a) one token only", files=_mutate(
        honest, **{ENTRY: _entry_text(tokens={
            "best-practices": "`scripts/validate.py`"})}),
        code=1, line=L2,
        finding="the tokens cell carries 1 rule token(s)"))
    add(dict(label="(a) empty tokens cell", files=_mutate(
        honest, **{ENTRY: _entry_text(tokens={"best-practices": ""})}),
        code=1, line=L2,
        finding="the tokens cell carries 0 rule token(s)"))
    add(dict(label="(a) single-character backticked spans are not tokens",
             files=_mutate(honest, **{ENTRY: _entry_text(tokens={
                 "best-practices": "`x`, `y`, `z`"})}),
             code=1, line=L2,
             finding="the tokens cell carries 0 rule token(s)"))
    add(dict(label="(a) a token invented and absent from its snapshot",
             files=_mutate(honest, **{ENTRY: _entry_text(tokens={
                 "best-practices": "`scripts/nope.py`, `scripts/validate.py`"})}),
             code=1, line=L2,
             finding="token 'scripts/nope.py' does not occur"))
    add(dict(label="(a) a token of another page's snapshot (Q37)",
             files=_mutate(honest, **{ENTRY: _entry_text(tokens={
                 "best-practices": "`uvx ruff check`, `scripts/validate.py`"})}),
             code=1, line=L2,
             finding="token 'uvx ruff check' does not occur word-bounded in "
                     "best-practices.md"))
    add(dict(label="(a) a token that is only a prefix of the page's path",
             files=_mutate(honest, **{ENTRY: _entry_text(tokens={
                 "quickstart": "`.agents/skill`, `python -m skills_ref.check`"})}),
             code=1, line=L2,
             finding="token '.agents/skill' does not occur word-bounded"))
    add(dict(label="(a) token-stuffed row (five invented tokens)", files=_mutate(
        honest, **{ENTRY: _entry_text(tokens={
            "best-practices": "`a/b`, `c/d`, `e/f`, `g/h`, `i/j`"})}),
        code=1, line=L2, finding="does not occur word-bounded"))
    add(dict(label="(a) a token occurs only inside a longer word", files=_repin(
        _mutate(honest, **{f"{SNAPDIR}/quickstart.md":
                           SNAP_TEXT["quickstart.md"].replace(
                               "python -m skills_ref.check",
                               "python -m skills_ref.checks")})),
        code=1, line=L2,
        finding="token 'python -m skills_ref.check' does not occur"))

    # ---------------------------------------------------- (b) the registry row
    add(dict(label="(b) cited row is queued, not mined", files=_mutate(
        honest, **{SOURCES: _registry([
            _reg_line(s, status="queued") if s == "S232" else _reg_line(s)
            for s in sorted(SID_OF.values())])}),
        code=1, line=L2, finding="S232: status 'queued'"))
    add(dict(label="(b) cited row is tier B", files=_mutate(
        honest, **{SOURCES: _registry([
            _reg_line(s, tier="B") if s == "S232" else _reg_line(s)
            for s in sorted(SID_OF.values())])}),
        code=1, line=L2, finding="S232: tier 'B'"))
    add(dict(label="(b) cited row has 12 cells", files=_mutate(
        honest, **{SOURCES: _registry([
            _reg_line(s, extra=1) if s == "S232" else _reg_line(s)
            for s in sorted(SID_OF.values())])}),
        code=1, line=L0, finding="S232: 12 cells"))
    add(dict(label="(b) used-by omits the entry", files=_mutate(
        honest, **{SOURCES: _registry([
            _reg_line(s, used_by="corpus/knowledge/other-round74.md")
            if s == "S232" else _reg_line(s)
            for s in sorted(SID_OF.values())])}),
        code=1, line=L0, finding="S232: used-by"))
    add(dict(label="(b) URL on a foreign host", files=_mutate(
        honest, **{SOURCES: _registry([
            _reg_line(s, url="https://example.invalid/skill-creation/"
                             "using-scripts.md") if s == "S232"
            else _reg_line(s) for s in sorted(SID_OF.values())])}),
        code=1, line=L2, finding="no URL on host agentskills.io"))
    add(dict(label="(b) URL on a subdomain is another host", files=_mutate(
        honest, **{SOURCES: _registry([
            _reg_line(s, url="https://docs.agentskills.io/skill-creation/"
                             "using-scripts.md") if s == "S232"
            else _reg_line(s) for s in sorted(SID_OF.values())])}),
        code=1, line=L2, finding="no URL on host agentskills.io"))
    add(dict(label="(b) URL is another agentskills page", files=_mutate(
        honest, **{SOURCES: _registry([
            _reg_line(s, url="https://agentskills.io/skill-creation/"
                             "evaluating-skills.md") if s == "S232"
            else _reg_line(s) for s in sorted(SID_OF.values())])}),
        code=1, line=L2, finding="is not the using-scripts page"))
    add(dict(label="(b) opened before the round-74 window", files=_mutate(
        honest, **{SOURCES: _registry([
            _reg_line(s, opened="2026-10-24") if s == "S232"
            else _reg_line(s) for s in sorted(SID_OF.values())])}),
        code=1, line=L2, finding="opened '2026-10-24' is not a round-74 date"))
    add(dict(label="(b) opened after the round-74 window", files=_mutate(
        honest, **{SOURCES: _registry([
            _reg_line(s, opened="2026-10-27") if s == "S232"
            else _reg_line(s) for s in sorted(SID_OF.values())])}),
        code=1, line=L0, finding="opened '2026-10-27' is not a round-74 date"))
    add(dict(label="(b) two registry rows for one cited id", files=_mutate(
        honest, **{SOURCES: _registry(
            [_reg_line(s) for s in sorted(SID_OF.values())]
            + [_reg_line("S232")])}),
        code=1, line=L0, finding="S232: 2 registry rows"))
    add(dict(label="(b) cited id absent from the registry", files=_mutate(
        honest, **{SOURCES: _registry(
            [_reg_line(s) for s in sorted(SID_OF.values()) if s != "S233"])}),
        code=1, line=L2, finding="S233: 0 registry rows"))
    add(dict(label="(b) the source: line names another page than the row",
             files=_mutate(honest, **{ENTRY: _entry_text().replace(
                 URL_OF["using-scripts"], URL_OF["quickstart"])}),
             code=1, line=L2,
             finding="carries no URL for the cited page"))
    add(dict(label="(b) staged campaign-schema rows appended as-is",
             files=_mutate(honest, **{SOURCES: _registry(
                 [_reg_line(s) for s in sorted(SID_OF.values())]
                 + [f"| S234 | {URL_OF['best-practices']} | docs | staged |",
                    f"| S235 | {URL_OF['using-scripts']} | docs | staged |"])}),
             code=1, line=L0, finding="is not census-conformant"))
    add(dict(label="(b) census E04: two rows share URL and scope",
             files=_mutate(honest, **{SOURCES: _registry(
                 [_reg_line(s) for s in sorted(SID_OF.values())]
                 + [_reg_line("S239", url=URL_OF["best-practices"])])}),
             code=1, line=L0, finding="is not census-conformant"))
    add(dict(label="(b) census E02: a registry id is not S###", files=_mutate(
        honest, **{SOURCES: _registry(
            [_reg_line(s) for s in sorted(SID_OF.values())]
            + ["| X999 | Agent Skills — fixture page — "
               "https://agentskills.io/skill-creation/quickstart.md | docs | "
               "B | fixture scope | §1 | fixture | mined | 2026-10-25 | 90d | "
               + ENTRY + " |"])}),
        code=1, line=L0, finding="is not census-conformant"))

    # --------------------------------------------------------- (c) snapshots
    add(dict(label="(c) tampered snapshot (manifest hash left)", files=_mutate(
        honest, **{f"{SNAPDIR}/best-practices.md":
                   SNAP_TEXT["best-practices.md"] + "A hand edit.\n"}),
        code=2, line=None, finding="snapshot_tampered"))
    add(dict(label="(c) no manifest at all", files=_mutate(
        honest, **{MANIFEST: None}), code=2, line=None,
        finding="no manifest at"))
    add(dict(label="(c) manifest line not `<sha256> <file>`", files=_mutate(
        honest, **{MANIFEST: _manifest() + "not-a-digest S999-x.md\n"}),
        code=2, line=None, finding="is not `<sha256>"))
    add(dict(label="(c) manifest path escapes the snapshot directory",
             files=_mutate(honest, **{
                 MANIFEST: _manifest() + "0" * 64 + "  ../S999-x.md\n"}),
             code=2, line=None, finding="escapes"))
    add(dict(label="(c) pinned snapshot not committed", files=_mutate(
        honest, **{f"{SNAPDIR}/quickstart.md": None}), code=2, line=None,
        finding="not committed"))
    add(dict(label="(c) two pinned files carry the page basename", files=_mutate(
        honest, **{MANIFEST: _manifest() + "0" * 64
                   + "  ghost/best-practices.md\n"}), code=2, line=None,
        finding="whose basename is best-practices.md"))
    add(dict(label="(c) census script missing is not a pass", files=honest,
             code=2, line=None, finding="census script",
             census="/nonexistent/sources-census.sh"))

    # ------------------------------------------------------------- (d) quote
    add(dict(label="(d) located quote under 5 words", files=_mutate(
        honest, **{ENTRY: _entry_text(quotes={
            "best-practices": "Use defaults not menus"})}),
        code=1, line=L2, finding="located quote is 4 words"))
    add(dict(label="(d) located quote over 25 words", files=_mutate(
        honest, **{ENTRY: _entry_text(quotes={
            "best-practices": " ".join(["word"] * 26)})}),
        code=1, line=L2, finding="located quote is 26 words"))
    add(dict(label="(d) located quote absent from its snapshot", files=_mutate(
        honest, **{ENTRY: _entry_text(quotes={
            "quickstart": "Create the directory and then read the manual first"})}),
        code=1, line=L2, finding="not found in quickstart.md"))
    add(dict(label="(d) two distinct quoted spans in the quote cell",
             files=_mutate(honest, **{ENTRY: _entry_text().replace(
                 f"\"{QUOTE['using-scripts']}\" | `scripts/`",
                 f"\"{QUOTE['using-scripts']}\" \"{QUOTE['quickstart']}\" | "
                 f"`scripts/`")}),
             code=1, line=L2, finding="2 distinct quoted span(s)"))
    add(dict(label="(d) no backtick stripping: quote carries added backticks",
             files=_mutate(honest, **{ENTRY: _entry_text(quotes={
                 "quickstart": "Create the directory `.agents/skills/` and add "
                               "a `SKILL.md` file."})}),
             code=1, line=L2, finding="not found in quickstart.md"))
    add(dict(label="(d) empty quote cell", files=_mutate(
        honest, **{ENTRY: _entry_text().replace(
            f"\"{QUOTE['best-practices']}\" |", "|", 1)}),
        code=1, line=L2, finding="0 distinct quoted span(s)"))

    # ------------------------------------------------- (e) SKILL.md act-on
    one_short = {p: list(SKILL_ROWS[p]) for p in PAGES}
    one_short["best-practices"] = [SKILL_ROWS["best-practices"][0]]
    add(dict(label="(e) only one row for a page", files=_mutate(
        honest, **{SKILLMD: _skill_text(one_short)}),
        code=1, line=L2, finding="1 counting row(s) citing S231"))
    four_words = {p: list(SKILL_ROWS[p]) for p in PAGES}
    four_words["using-scripts"] = [
        "| using-scripts (S232) | Use `uvx ruff check`. |",
        SKILL_ROWS["using-scripts"][1]]
    add(dict(label="(e) action cell under five words", files=_mutate(
        honest, **{SKILLMD: _skill_text(four_words)}),
        code=1, line=L2, finding="4 action word(s)"))
    no_token = {p: list(SKILL_ROWS[p]) for p in PAGES}
    no_token["quickstart"] = [
        "| quickstart (S233) | Create the skills directory first and then the "
        "skill file itself. |",
        SKILL_ROWS["quickstart"][1]]
    add(dict(label="(e) action cell without a token of the page", files=_mutate(
        honest, **{SKILLMD: _skill_text(no_token)}),
        code=1, line=L2, finding="carries no quickstart token in its action cell"))
    wrong_token = {p: list(SKILL_ROWS[p]) for p in PAGES}
    wrong_token["best-practices"] = [
        "| best-practices (S231) | Validate every helper with `uvx ruff check` "
        "before you ship it. |",
        SKILL_ROWS["best-practices"][1]]
    add(dict(label="(e) token occurs only in another page's snapshot (Q37)",
             files=_mutate(honest, **{SKILLMD: _skill_text(wrong_token)}),
             code=1, line=L2,
             finding="carries no best-practices token in its action cell"))
    add(dict(label="(e) heading with a hyphen instead of the em dash",
             files=_mutate(honest, **{SKILLMD: _skill_text(
                 heading="### Body craft - the specification's skill-creation "
                         "guides")}),
             code=1, line=L0, finding="no single heading line"))
    add(dict(label="(e) heading with a curly apostrophe", files=_mutate(
        honest, **{SKILLMD: _skill_text(
            heading="### Body craft — the specification\u2019s skill-creation "
                    "guides")}),
        code=1, line=L0, finding="no single heading line"))
    add(dict(label="(e) heading duplicated", files=_mutate(
        honest, **{SKILLMD: _skill_text() + "\n" + SKILL_HEADING + "\n"}),
        code=1, line=L0, finding="2 match(es)"))
    add(dict(label="(e) SKILL.md absent", files=_mutate(
        honest, **{SKILLMD: None}), code=1, line=L0,
        finding="no single heading line"))
    add(dict(label="(e) a counting row outside the subsection does not count",
             files=_mutate(honest, **{SKILLMD: _skill_text(
                 one_short, outside=SKILL_ROWS["best-practices"][1])}),
             code=1, line=L2, finding="1 counting row(s) citing S231"))
    add(dict(label="(e) a row that only cites the id elsewhere in the row",
             files=_mutate(honest, **{SKILLMD: _skill_text(
                 {p: list(SKILL_ROWS[p]) for p in PAGES if p != "quickstart"})}),
             code=1, line=L2, finding="0 counting row(s) citing S233"))

    # ---------------------------------------------------------- (f) province
    add(dict(label="(f) PROVINCE.md without the entry", files=_mutate(
        honest, **{PROVINCE: "# fixture province\n\n## Core\n\n- nothing\n"}),
        code=1, line=L0, finding="§ Core does not name"))
    add(dict(label="(f) entry named only outside § Core", files=_mutate(
        honest, **{PROVINCE: ("# fixture province\n\n## Core\n\n- nothing\n\n"
                              "## Frontier\n\n- `" + ENTRY + "`\n")}),
        code=1, line=L0, finding="§ Core does not name"))
    add(dict(label="(f) PROVINCE.md absent", files=_mutate(
        honest, **{PROVINCE: None}), code=1, line=L0,
        finding="§ Core does not name"))
    add(dict(label="(f) entry named in a Core continuation line", files=_mutate(
        honest, **{PROVINCE: ("# fixture province\n\n## Core\n\n- body craft,\n"
                              "  counted by `" + ENTRY + "`\n\n## Frontier\n\n"
                              "- none\n")}),
        code=0, line=L3))

    # ------------------------------------------------ plan's shortcut controls
    add(dict(label="shortcut: staged entry copied unchanged with staged ids "
                   "and no registry rows", files=_mutate(
        honest, **{ENTRY: _entry_text(sids={
            "best-practices": "S236", "using-scripts": "S237",
            "quickstart": "S238"}).replace(URL_OF["quickstart"],
                                           URL_OF["quickstart"]),
        SOURCES: _registry()}),
        code=1, line=L0))
    add(dict(label="shortcut: the entry outside corpus/knowledge is not the "
                   "entry", files=_mutate(honest, **{
        ENTRY: None,
        "corpus/notes/spec-skill-creation-craft-round74.md": _entry_text()}),
        code=1, line=L0, finding="absent at"))
    add(dict(label="shortcut: SKILL.md rows without the entry", files=_mutate(
        honest, **{ENTRY: None}), code=1, line=L0, finding="absent at"))
    add(dict(label="shortcut: queue-status rows only", files=_mutate(
        honest, **{SOURCES: _registry([
            _reg_line(s, status="queued") for s in sorted(SID_OF.values())])}),
        code=1, line=L0, finding="S231: status 'queued'"))
    add(dict(label="shortcut: a snapshot hand-edited, manifest left", files=_mutate(
        honest, **{f"{SNAPDIR}/using-scripts.md":
                   SNAP_TEXT["using-scripts.md"].replace(
                       "one-off command's", "single command's")}),
        code=2, line=None, finding="snapshot_tampered"))
    add(dict(label="shortcut: r73-style vendor table instead of a rule table",
             files=_mutate(honest, **{ENTRY: _entry_text().replace(
                 "| page | S id | rule | quote | tokens | action |",
                 "| vendor | discovery root | keys | placement | sources | "
                 "notes |")}),
             code=1, line=L0, finding="no rule table row names any of"))

    # ------------------------------------------- E1.1 amendments (pre-data)
    banner_q = ("Fetch the complete documentation index at: "
                "https://agentskills.io/llms.txt")
    add(dict(label="(a') chrome-only tokens: every located token is shared "
                   "site text", files=_mutate(honest, **{ENTRY: _entry_text(
                       tokens={"best-practices":
                               "`SKILL.md`, \"" + banner_q + "\""})}),
             code=1, line=L2, finding="no page-unique token among"))
    add(dict(label="(d') the page subtitle blockquote is not a rule",
             files=_mutate(honest, **{ENTRY: _entry_text(quotes={
                 "best-practices": SUBTITLE_OF["best-practices"]})}),
             code=1, line=L2, finding="page subtitle blockquote"))
    add(dict(label="(d') the site banner line is chrome, before the first H1",
             files=_mutate(honest, **{ENTRY: _entry_text(quotes={
                 "best-practices": banner_q})}),
             code=1, line=L2, finding="not after the page's first `# ` heading"))
    add(dict(label="(d') a heading is not a rule", files=_mutate(
        honest, **{ENTRY: _entry_text(quotes={
            "best-practices": "Keep every defaults list short and sharp"})}),
        code=1, line=L2, finding="the located quote is a heading"))
    add(dict(label="(d') a link to another skill-creation page is not a rule",
             files=_mutate(honest, **{ENTRY: _entry_text(quotes={
                 "best-practices": LINK_LINE})}),
             code=1, line=L2,
             finding="link to another skill-creation page"))
    add(dict(label="(c') registry anchor digest is not the snapshot's",
             files=_mutate(honest, **{SOURCES: _registry([
                 _reg_line(s, sha="0" * 64) if s == "S232" else _reg_line(s)
                 for s in sorted(SID_OF.values())])}),
             code=1, line=L2,
             finding="the anchor cell carries no sha256 equal to the pinned"))
    add(dict(label="(c') a fetch record with HTTP 404 does not back a page",
             files=_mutate(honest, **{FETCHLOG: _fetchlog().replace(
                 "\t200\t", "\t404\t", 1)}),
             code=1, line=L2, finding="fetch record status '404'"))
    add(dict(label="(c') fetch record bytes differ from the snapshot",
             files=_mutate(honest, **{FETCHLOG: "\n".join(
                 ln.replace(str(len(SNAP_TEXT['quickstart.md'].encode())), "1")
                 if ln.startswith("quickstart") else ln
                 for ln in _fetchlog().splitlines()) + "\n"}),
             code=1, line=L2, finding="fetch record bytes 1"))
    add(dict(label="(c') no fetch log at all backs no page", files=_mutate(
        honest, **{FETCHLOG: None}), code=1, line=L0,
        finding="no fetch record for best-practices"))
    add(dict(label="(c') snapshot, manifest, anchor and log all re-signed: the "
                   "counter's own pin refuses", files=_repin(_mutate(
                       honest, **{f"{SNAPDIR}/using-scripts.md":
                                  SNAP_TEXT["using-scripts.md"] + "A new line.\n"})),
             pin="fixture", code=2, line=None, finding="snapshot_pin_mismatch"))
    filler = {p: list(SKILL_ROWS[p]) for p in PAGES}
    filler["best-practices"] = [
        "| best-practices (S231) | Use `scripts/validate.py` as the guide says. |",
        "| best-practices (S231) | See `scripts/validate.py` for this page. |"]
    add(dict(label="(e') filler action cells restating a token say nothing",
             files=_mutate(honest, **{SKILLMD: _skill_text(filler)}),
             code=1, line=L2, finding="0 counting row(s) citing S231"))
    shared_tok = {p: list(SKILL_ROWS[p]) for p in PAGES}
    shared_tok["best-practices"] = [
        "| best-practices (S231) | Validate every helper with `SKILL.md` before "
        "you ship it. |", SKILL_ROWS["best-practices"][1]]
    add(dict(label="(e') an action token shared with other pages is not "
                   "page-unique", files=_mutate(
                       honest, **{SKILLMD: _skill_text(shared_tok)}),
             code=1, line=L2, finding="carries no page-unique best-practices "
                                       "token"))
    add(dict(label="shortcut: staged rows (2026-10-23, no digest) with fetched "
                   "snapshots", files=_mutate(honest, **{SOURCES: _registry([
                       _reg_line(s, opened="2026-10-23", sha="0" * 64)
                       for s in sorted(SID_OF.values())])}),
             code=1, line=L0, finding="is not a round-74 date"))

    # ------------------------------------------------------- cannot-evaluate
    add(dict(label="unknown revision is exit 2", files=honest, code=2,
             rev="0" * 40, line=None, finding="not a commit"))
    add(dict(label="REPO not a git worktree is exit 2", files=honest, code=2,
             repo_arg="/tmp", line=None, finding="not a git worktree"))
    add(dict(label="registry absent at the revision is exit 2", files=_mutate(
        honest, **{SOURCES: None}), code=2, line=None,
        finding=f"{SOURCES} absent"))
    add(dict(label="base registry unreadable is exit 2", files=honest,
             base_files={"README.md": "no registry at base\n"}, code=2,
             line=None, finding=f"{SOURCES} unreadable at base"))
    return specs


def _run_spec(spec: dict) -> tuple[bool, int, str]:
    """Run one world through ``main()`` in its own isolated git repo."""
    global BASE_REV, CENSUS
    saved_base, saved_census = BASE_REV, CENSUS
    saved_pins = dict(PAGE_SHA)
    mode = spec.get("pin")
    edited = {p: spec["files"].get(f"{SNAPDIR}/{p}.md") for p in PAGES}
    if mode is None:
        mode = "world" if any(t is not None and t != SNAP_TEXT[p + ".md"]
                              for p, t in edited.items()) else "fixture"
    for p in PAGES:
        t = edited[p] if mode == "world" and edited[p] is not None \
            else SNAP_TEXT[p + ".md"]
        PAGE_SHA[p] = _sha(t)
    d, base = _world(spec["files"], spec.get("base_files"))
    BASE_REV = base
    CENSUS = spec.get("census") or saved_census
    buf = io.StringIO()
    saved_cwd = os.getcwd()
    try:
        if spec.get("cwd"):
            os.chdir(d)
        with contextlib.redirect_stdout(buf), \
                contextlib.redirect_stderr(buf):
            code = main(["--repo", spec.get("repo_arg", d),
                         "--rev", spec.get("rev", "HEAD")])
    finally:
        os.chdir(saved_cwd)
        shutil.rmtree(d, ignore_errors=True)
        BASE_REV, CENSUS = saved_base, saved_census
        PAGE_SHA.clear()
        PAGE_SHA.update(saved_pins)
    out = buf.getvalue()
    checks = [code == spec["code"]]
    if spec.get("line") is not None:
        checks.append(spec["line"] in out)
    if spec.get("finding") is not None:
        checks.append(spec["finding"] in out)
    ok = all(checks)
    msg = f"{spec['label']}: exit {code}"
    if not ok:
        msg += f" (want {spec['code']}; line={spec.get('line')!r}; " \
               f"finding={spec.get('finding')!r}); output={out!r}"
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
    return 0 if failures == 0 and assertions >= 150 else 1


if __name__ == "__main__":
    sys.exit(main())
