#!/usr/bin/env python3
"""check_cn_vendor_surfaces.py — frozen C1 counter for kotoba round 73 (coverage).

FROZEN PREDICATE (the same sentence in plans/round-73.md § C1, in this
docstring and in the receipt):

    python3 -B verifiers/check_cn_vendor_surfaces.py --rev <rev>  ->  prints
    "vendor skill surfaces backed N of 4", exit 0 when N == 4

Vendor ``V`` in {TRAE, CodeBuddy, Kimi Code, Zhipu} is **backed** at ``--rev``
iff all of (a)-(d) hold over committed bytes only (no network at measurement,
and no instrument of the measured tree is executed):

  (a) the entry ``corpus/knowledge/chinese-vendor-skill-surfaces-round73.md``
      (frozen path) opens with ``source:`` lines for every cited id, then
      ``verified-at:`` and ``recheck:``, and has exactly one row for ``V`` in
      its vendor table whose backticked tokens (paths and frontmatter keys; at
      least three, at least one root or placement token and at least two keys)
      each occur word-bounded in the committed page snapshot of a source that
      row cites;
  (b) every cited ``S###`` is an 11-cell registry row with status ``mined``,
      tier ``A`` or ``B``, a ``used-by`` cell naming the entry, and a URL whose
      host is one of ``V``'s hosts (frozen: TRAE ``docs.trae.cn``; CodeBuddy
      ``www.codebuddy.ai``; Kimi Code ``github.com/moonshotai/kimi-cli`` or
      ``www.kimi.com``; Zhipu ``docs.bigmodel.cn``);
  (c) each cited row has a snapshot under ``.ufo/waves/round-73/snapshots/``
      whose sha256 equals the pin in the committed manifest
      ``.ufo/waves/round-73/snapshots/MANIFEST.sha256`` (a missing or tampered
      snapshot is exit 2);
  (d) each cited row's located quote (5-25 words) is found in its snapshot
      after whitespace collapse only.

The counter also prints ``held at base: 0`` (host strings in the base
registry), the do-nothing figure: the number of the four vendors whose frozen
host table already appears in a ``corpus/SOURCES.md`` URL at
``BASE_REV = 072048fa8e8a52c707d25f7079772fa317244eb7``.

READINGS that are deliberately stricter than the naive one, named here so a
reviewer can attack them rather than discover them:

  * the entry's vendor table is *any* markdown table of the entry; a vendor row
    is a row whose first cell, with backticks and emphasis stripped, begins
    with the vendor's frozen name at an ASCII word boundary (``| TRAE (ByteDance)
    |`` names TRAE; ``| Kimi Codex |`` does not name Kimi Code).  Exactly one
    such row must name each vendor: a second row anywhere disqualifies it.
  * the counted tokens are the backticked spans of the row's cells AFTER the
    first (the vendor-name cell).  A token containing ``/`` or beginning with
    ``.``, ``~`` or ``$`` is a discovery-root/placement token; a token matching
    ``^[A-Za-z][A-Za-z0-9_:-]*$`` (no dot: ``SKILL.md`` is not a key) is a
    frontmatter key; every other token counts toward "at least three" only.
    A token's matching forms are the token itself, its form without a leading
    ``~/`` and each without a trailing ``/`` — a page that writes the same root
    without the tilde or without the closing slash is the same root, and no
    other shaping is applied.
  * word-bounded means ASCII-word-bounded (``[A-Za-z0-9_]``), not ``\\w``:
    two of the four vendors publish Chinese pages, where a CJK character
    directly abutting ``.codebuddy/skills`` is a boundary, not a word character.
  * a token may be backed by the snapshot of ANY source the row cites (the
    frozen "(a) … a source that row cites" read existentially over the row's
    cited sources); the located quote of (d) must be in the snapshot of ITS OWN
    cited id only.
  * the snapshot of a cited id is resolved, in order: (1) the single file the
    entry names on a line citing that id and whose basename is a manifest key
    (the lane's ``(snapshot `S262-…md:106-114`)`` convention, round 72), else
    (2) the single manifest file whose basename begins with that id followed by
    a non-digit (``S217-trae-ide.md``).  Two candidates in either step, a
    candidate escaping the snapshot directory, or no candidate at all is exit 2
    (could not evaluate), never a pass and never a content fail.
  * the located quote of (d) is a ``located quote "<5-25 words>"`` span on the
    entry line that cites the id; only when no such phrase exists does the
    entry's own ``source:`` line (or a table row whose first cell is the id)
    fall back to its single quoted span.  Two distinct quotes for one id is a
    finding, never a pass.  The quote is matched with whitespace collapsed and
    nothing else: no backtick stripping, no case folding, no entity decoding.
  * a pin is bound to the page the row cites: the entry's own ``source:`` line
    for a cited id must carry a URL whose host+path (trailing ``/`` ignored,
    path case kept) equals the cited row's first URL.  Without that binding a
    seat could pin a committed snapshot of an EASIER page to a hard URL and
    (c)/(d) would read true of the wrong page; the binding can only fail more.
  * the entry-level trio (all ``source:`` lines, then ``verified-at:``, then
    ``recheck:``) and ``cited ids ⊆ the entry's own source: ids`` are read
    once for the whole entry: a triple that is broken for one vendor is broken
    for all four (0 of 4), because the entry is the claim's single surface.

Exit codes: 0 iff N == 4; 1 otherwise (a content verdict); 2 could not evaluate
(unknown revision, unreadable registry, missing/tampered/ambiguous pinned
snapshot, unreadable base registry).  ``--self-test`` runs the world table (one
honest world, then one broken world per conjunct and per shortcut control the
plan names) in isolated local git repos under fresh ``mktemp -d`` directories:
no lane, no fleet repo and no shared index is ever touched.  ``--census-check``
additionally runs ``sources-census.sh validate`` over the revision's registry as
a second evidence, never the verdict.  ``--print-self-sha`` prints the blanked
sha of this file (the L1 refills ``SELF_SHA`` after any edit and before freeze).

Usage:
  python3 -B verifiers/check_cn_vendor_surfaces.py --rev <rev> [--repo <lane>]
  python3 -B verifiers/check_cn_vendor_surfaces.py --self-test
  python3 -B verifiers/check_cn_vendor_surfaces.py --print-self-sha
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

TOTAL = 4
SOURCES = "corpus/SOURCES.md"
ENTRY = "corpus/knowledge/chinese-vendor-skill-surfaces-round73.md"
SNAPDIR = ".ufo/waves/round-73/snapshots"
MANIFEST = SNAPDIR + "/MANIFEST.sha256"
COUNTER_PATH = "verifiers/check_cn_vendor_surfaces.py"
CENSUS = "/home/vgpnk/Projects/shokunin/scripts/sources-census.sh"

# Frozen at freeze 1: the base lane tip the do-nothing control is measured at.
# The self-test rebinds this module global to a fixture repo's own first commit
# (there is no CLI flag to move it: a measurement always reads this constant).
BASE_REV = "072048fa8e8a52c707d25f7079772fa317244eb7"

# The plan's frozen host table.  A pin with a `/` is host + path prefix.
VENDORS = {
    "TRAE": ("docs.trae.cn",),
    "CodeBuddy": ("www.codebuddy.ai",),
    "Kimi Code": ("github.com/moonshotai/kimi-cli", "www.kimi.com"),
    "Zhipu": ("docs.bigmodel.cn",),
}

MIN_TOKENS = 3
MIN_ROOT_TOKENS = 1
MIN_KEY_TOKENS = 2
MIN_QUOTE_WORDS = 5
MAX_QUOTE_WORDS = 25
REGISTRY_CELLS = 11

SID_RE = re.compile(r"\bS\d{3,}\b")
BACKTICK_RE = re.compile(r"`([^`]+)`")
LOCATED_RE = re.compile(r'located quote\s+["\u201c]([^"\u201d]+)["\u201d]')
QUOTE_RE = re.compile(r'["\u201c]([^"\u201d]+)["\u201d]')
REGISTRY_RE = re.compile(r"^ {0,3}\|\s*S\d{3,}\s*\|")
URL_RE = re.compile(r"https?://[^\s)>\]]+")
KEY_RE = re.compile(r"^[A-Za-z][A-Za-z0-9_:-]*$")
ROOT_PREFIXES = (".", "~", "$", "/")
SEPARATOR_RE = re.compile(r":?-{3,}:?")
TRIM_CHARS = ".,;:!?)]}'\""
SELF_SHA = "b4ca05cf3c0a45d239995b4e726caa47903d37d42a503d276e0c7b3d8b2e3573"   # blanked-sha of this file
_INTERNAL_SELFTEST = False   # set only by --self-test: the drift guard is a
                             # measurement guard, and the self-test mutates
                             # nothing in this file, so it is skipped there.
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


CITED_TAIL_RE = re.compile(r"-[A-Za-z]")


def cited_sids(text: str) -> list[str]:
    """``S###`` ids that cite a registry row, in order, deduplicated.

    An id glued to a slug (``S217-trae-ide.md``) is a snapshot file name, not a
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


def vendor_of(cell: str) -> str | None:
    """Which frozen vendor a table's first cell names (``| TRAE (ByteDance) |``)."""
    name = clean(cell)
    for vendor in VENDORS:
        if re.match(rf"^{re.escape(vendor.lower())}(?![a-z0-9_])", name):
            return vendor
    return None


def vendor_rows(entry_r: str) -> list[tuple[str, list[str]]]:
    """Every (vendor, row) pair in the entry's tables, in document order."""
    out: list[tuple[str, list[str]]] = []
    for _head, rows in tables(entry_r):
        for row in rows:
            if len(row) < 2:
                continue
            vendor = vendor_of(row[0])
            if vendor:
                out.append((vendor, row))
    return out


def cited_ids(row: list[str]) -> list[str]:
    """The ``S###`` ids a vendor row cites, in order, deduplicated."""
    found: list[str] = []
    for cell in row[1:]:
        for sid in cited_sids(cell):
            if sid not in found:
                found.append(sid)
    return found


def row_tokens(row: list[str]) -> list[str]:
    """The backticked spans of the row after the vendor-name cell."""
    toks: list[str] = []
    for cell in row[1:]:
        for tok in BACKTICK_RE.findall(cell):
            t = tok.strip()
            if t and t not in toks:
                toks.append(t)
    return toks


def classify(token: str) -> str:
    """'root' (a path/placement token), 'key' (a frontmatter key), else 'other'."""
    if "/" in token or token.startswith(ROOT_PREFIXES):
        return "root"
    if KEY_RE.match(token):
        return "key"
    return "other"


def token_forms(token: str) -> list[str]:
    """The token itself, without a leading ``~/``, and each without a trailing ``/``."""
    forms = [token]
    if token.startswith("~/"):
        forms.append(token[2:])
    for f in list(forms):
        stripped = f.rstrip("/")
        if stripped and stripped not in forms:
            forms.append(stripped)
    return [f for f in forms if f]


def quote_for(entry_r: str, sid: str) -> tuple[str | None, str | None]:
    """The entry's located quote for one cited id: (quote, note)."""
    located: list[str] = []
    fallback: list[str] = []
    for line in entry_r.splitlines():
        if sid not in SID_RE.findall(line):
            continue
        located.extend(LOCATED_RE.findall(line))
        cells = _cells(line)
        if line.startswith("source:") or (cells and cells[0] == sid):
            fallback.extend(QUOTE_RE.findall(line))
    cands = located or fallback
    uniq: list[str] = []
    for q in cands:
        n = ws(q)
        if n and n not in uniq:
            uniq.append(n)
    if len(uniq) != 1:
        return None, (f"{sid}: {len(uniq)} distinct located quote(s) in the "
                      f"entry (want exactly 1)")
    quote = uniq[0]
    words = len(quote.split())
    if not MIN_QUOTE_WORDS <= words <= MAX_QUOTE_WORDS:
        return None, (f"{sid}: located quote is {words} words "
                      f"(want {MIN_QUOTE_WORDS}-{MAX_QUOTE_WORDS})")
    return quote, None


def page_key(url: str) -> tuple[str, str]:
    """Host + path of a page, ignoring a trailing ``/`` and the query/fragment."""
    parts = urllib.parse.urlsplit(url)
    return ((parts.hostname or "").lower(),
            urllib.parse.unquote(parts.path or "").rstrip("/").lower())


def source_line(entry_r: str, sid: str) -> str | None:
    """The entry's own ``source:`` line that names one cited id."""
    for line in entry_r.splitlines():
        if line.startswith("source:") and sid in cited_sids(line):
            return line
    return None


def entry_problems(entry_r: str) -> list[str]:
    """Entry-level (a): the trio, and cited ids covered by the source: lines."""
    notes: list[str] = []
    rows = vendor_rows(entry_r)
    if not rows:
        return ["no table row names any of "
                + ", ".join(VENDORS) + " (the entry has no vendor table)"]
    src, verified, recheck = entry_head(entry_r)
    if not src:
        notes.append("entry does not open with source: lines")
    if not verified:
        notes.append("entry has no verified-at: line after its source: lines")
    if not recheck:
        notes.append("entry has no recheck: line after verified-at:")
    cited: list[str] = []
    for _vendor, row in rows:
        for sid in cited_ids(row):
            if sid not in cited:
                cited.append(sid)
    if not cited:
        notes.append("the vendor table cites no S### id")
    head: set[str] = set()
    for line in src:
        # the ids a source: line names are those before its located quote: the
        # tail's snapshot file name (`S217-trae-ide.md`) is not a source id.
        head.update(cited_sids(line.split("located quote")[0]))
    missing = [s for s in cited if s not in head]
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

    def snapshot_name(self, entry_r: str, sid: str) -> str:
        """The pinned snapshot file that carries one cited row's page."""
        man = self.manifest()
        named: list[str] = []
        for line in entry_r.splitlines():
            if sid not in SID_RE.findall(line):
                continue
            for tok in BACKTICK_RE.findall(line):
                base = tok.strip().split(":", 1)[0].strip().rsplit("/", 1)[-1]
                if base in man and base not in named:
                    named.append(base)
        if len(named) == 1:
            return named[0]
        if len(named) > 1:
            raise EnvError(f"{sid}: the entry names {len(named)} pinned "
                           f"snapshots ({', '.join(named)}) — the pin of one "
                           f"row is ambiguous")
        pref = sorted(p for p in man
                      if re.match(rf"^{re.escape(sid)}(?![0-9])",
                                  p.rsplit("/", 1)[-1]))
        if len(pref) == 1:
            return pref[0]
        if not pref:
            raise EnvError(f"{sid}: no snapshot is pinned for this row in "
                           f"{MANIFEST}")
        raise EnvError(f"{sid}: {len(pref)} pinned snapshots begin with {sid} "
                       f"({', '.join(pref)}) — the pin of one row is ambiguous")

    def read_snapshot(self, name: str, sha: str) -> str:
        proc = _git(self.path, ["show", f"{self.rev}:{SNAPDIR}/{name}"])
        if proc.returncode != 0:
            raise EnvError(f"snapshot {SNAPDIR}/{name} not committed at "
                           f"{self.rev}")
        if hashlib.sha256(proc.stdout).hexdigest() != sha:
            raise EnvError(f"snapshot_tampered: {SNAPDIR}/{name}")
        return proc.stdout.decode("utf-8", "replace")

    def census_ok(self) -> bool | None:
        """``sources-census.sh validate --file`` on the revision's registry."""
        arch = _git(self.path, ["archive", self.rev])
        if arch.returncode != 0:
            return None
        with tempfile.TemporaryDirectory(prefix="k73-c1census-") as td:
            root = Path(td)
            (root / "tree.tar").write_bytes(arch.stdout)
            subprocess.run(["tar", "-xf", "tree.tar"], cwd=root,
                           capture_output=True)
            target = root / SOURCES
            if not target.is_file() or not Path(CENSUS).is_file():
                return None
            proc = subprocess.run(["bash", CENSUS, "validate", "--file",
                                   str(target)], capture_output=True, text=True,
                                  timeout=120)
            return proc.returncode == 0


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


def host_ok(url: str, pins: tuple[str, ...]) -> bool:
    """Exact host for a bare pin; host + path prefix for a pin carrying one."""
    try:
        parts = urllib.parse.urlsplit(url)
    except ValueError:
        return False
    host = (parts.hostname or "").lower()
    path = urllib.parse.unquote(parts.path or "").lower()
    if any(seg in (".", "..") for seg in path.split("/")):
        return False
    if not path.startswith("/"):
        path = "/" + path
    for pin in pins:
        h, _, p = pin.partition("/")
        if p:
            prefix = "/" + p.lower().rstrip("/")
            if host == h.lower() and (path == prefix
                                      or path.startswith(prefix + "/")):
                return True
        elif host == h.lower():
            return True
    return False


def registry_problems(registry: dict[str, list[list[str]]], vendor: str,
                      sid: str) -> list[str]:
    """(b) for one cited id of one vendor."""
    rows = registry.get(sid, [])
    if len(rows) != 1:
        return [f"{sid}: {len(rows)} registry rows in {SOURCES} "
                f"(want exactly 1)"]
    row = rows[0]
    if len(row) != REGISTRY_CELLS:
        return [f"{sid}: {len(row)} cells (want exactly {REGISTRY_CELLS})"]
    notes: list[str] = []
    if row[7] != "mined":
        notes.append(f"{sid}: status {row[7]!r} (want 'mined')")
    if row[3] not in ("A", "B"):
        notes.append(f"{sid}: tier {row[3]!r} (want A or B)")
    listed = [c.strip() for c in row[10].split(",")]
    if ENTRY not in listed:
        notes.append(f"{sid}: used-by {row[10]!r} does not list {ENTRY}")
    urls = urls_of(row[1])
    if not urls:
        notes.append(f"{sid}: source cell holds no URL")
    elif not any(host_ok(u, VENDORS[vendor]) for u in urls):
        notes.append(f"{sid}: no URL on {vendor}'s pinned host(s) "
                     f"{list(VENDORS[vendor])}: {urls}")
    return notes


# -------------------------------------------------------------------- verdict

class Ctx:
    def __init__(self, repo: Repo, entry_r: str,
                 registry: dict[str, list[list[str]]],
                 rows: list[tuple[str, list[str]]]):
        self.repo, self.entry_r = repo, entry_r
        self.registry, self.rows = registry, rows


def vendor_holds(ctx: Ctx, vendor: str) -> tuple[bool, list[str]]:
    mine = [row for v, row in ctx.rows if v == vendor]
    if len(mine) != 1:
        return False, [f"{len(mine)} vendor-table row(s) name {vendor} "
                       f"(want exactly 1)"]
    row = mine[0]
    notes: list[str] = []
    toks = row_tokens(row)
    roots = [t for t in toks if classify(t) == "root"]
    keys = [t for t in toks if classify(t) == "key"]
    if len(toks) < MIN_TOKENS:
        notes.append(f"row carries {len(toks)} backticked token(s) "
                     f"(want >= {MIN_TOKENS}): {toks}")
    if len(roots) < MIN_ROOT_TOKENS:
        notes.append(f"row carries no discovery-root/placement token "
                     f"(want >= {MIN_ROOT_TOKENS}): {toks}")
    if len(keys) < MIN_KEY_TOKENS:
        notes.append(f"row carries {len(keys)} frontmatter key token(s) "
                     f"(want >= {MIN_KEY_TOKENS}): {toks}")
    ids = cited_ids(row)
    if not ids:
        notes.append("row cites no S### id")
    if notes:
        return False, notes

    for sid in ids:
        notes.extend(registry_problems(ctx.registry, vendor, sid))
    if notes:
        return False, notes

    pages: list[tuple[str, str]] = []
    for sid in ids:
        row = ctx.registry[sid][0]
        want = urls_of(row[1])
        line = source_line(ctx.entry_r, sid)
        if line is None:
            notes.append(f"{sid}: no source: line in the entry names it")
            continue
        if want and not any(page_key(u) == page_key(want[0])
                            for u in urls_of(line)):
            notes.append(f"{sid}: the entry's source: line carries no URL for "
                         f"the cited page {want[0]} — the pinned snapshot is "
                         f"not demonstrably the page the row cites")
    if notes:
        return False, notes
    for sid in ids:
        name = ctx.repo.snapshot_name(ctx.entry_r, sid)
        sha = ctx.repo.manifest()[name]
        pages.append((sid, ws(ctx.repo.read_snapshot(name, sha))))

    for tok in toks:
        forms = token_forms(tok)
        if not any(word_bounded(f, text) for f in forms for _s, text in pages):
            notes.append(f"token {tok!r} does not occur word-bounded in the "
                         f"snapshot(s) of {', '.join(ids)}")

    for sid, text in pages:
        quote, note = quote_for(ctx.entry_r, sid)
        if note:
            notes.append(note)
            continue
        if quote not in text:
            notes.append(f"{sid}: located quote not found in its pinned "
                         f"snapshot after whitespace collapse: {quote!r}")
    return (not notes), notes


def held_at_base(repo: Repo) -> int:
    """Vendors whose frozen host table already appears in the base registry."""
    base = repo.show_at(BASE_REV, SOURCES)
    if base is None:
        raise EnvError(f"{SOURCES} unreadable at base {BASE_REV}")
    rows = registry_rows(rendered(base))
    held = 0
    for vendor, pins in VENDORS.items():
        if any(host_ok(u, pins)
               for cells in rows.values() for row in cells
               for u in urls_of(row[1] if len(row) > 1 else "")):
            held += 1
    return held


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
              vendor_rows(entry_r))
    n, findings, backed = 0, [], []
    for vendor in VENDORS:
        ok, notes = vendor_holds(ctx, vendor)
        if ok:
            n += 1
            backed.append(vendor)
        else:
            findings.extend(f"{vendor}: {n_}" for n_ in notes)
    return n, findings, backed


# ---------------------------------------------------------------- self-test
# Every world is an isolated local git repo under a fresh mktemp dir with TWO
# commits: the first is the "base" state the do-nothing figure is read from,
# the second the measured tip.  No lane, fleet repo or shared index is touched.
Q = {
    "S217": "TRAE reads skills from the project root and every skill declares "
            "name and description",
    "S218": "TRAE also reads a user root under the home directory",
    "S219": "CodeBuddy IDE loads skills from the workspace root and reads name "
            "and allowed-tools",
    "S220": "CodeBuddy CLI reads the same root and honours name and "
            "allowed-tools",
    "S221": "Kimi Code CLI reads skills from the project root and sets "
            "whenToUse",
    "S222": "Kimi Code also honours disableModelInvocation when the skill is "
            "invoked",
    "S223": "Zhipu managed agents upload a skill bundle whose frontmatter sets "
            "name",
    "S224": "Zhipu also accepts a description and a type in the bundle "
            "frontmatter",
}

SNAP = {
    "S217-trae-ide.md": (
        "# Skills\n\n"
        + Q["S217"] + ".\n"
        "The project root is .trae/skills/ and the file inside it is SKILL.md.\n"
        + Q["S218"] + ".\n"),
    "S218-trae-user.md": (
        "# Skills\n\n"
        + Q["S218"] + ".\n"
        "That user root is ~/.trae/skills/ on every platform.\n"),
    "S219-cb-ide.md": (
        "# Skills\n\n"
        + Q["S219"] + ".\n"
        "The workspace root is .codebuddy/skills/ inside the repository.\n"),
    "S220-cb-cli.md": (
        "# Skills\n\n"
        + Q["S220"] + ".\n"
        "The CLI reads .codebuddy/skills/ from the workspace.\n"),
    "S221-kimi-en.md": (
        "# Skills\n\n"
        + Q["S221"] + ".\n"
        "The project root is .kimi-code/skills/ for this client.\n"
        + Q["S222"] + ".\n"),
    "S222-kimi-zh.md": (
        "# Skills\n\n"
        + Q["S222"] + ".\n"
        "The project root is .kimi-code/skills/ here too.\n"),
    "S223-zhipu.md": (
        "# Skills\n\n"
        + Q["S223"] + ".\n"
        "The bundle places each skill body under .zhipu/skills/.\n"),
    "S224-zhipu.md": (
        "# Skills\n\n"
        + Q["S224"] + ".\n"
        "The bundle root stays .zhipu/skills/ after upload.\n"),
}

ENTRY_ROWS = {
    "TRAE": ("`.trae/skills/`", "`name`, `description`", "S217, S218"),
    "CodeBuddy": ("`.codebuddy/skills/`", "`name`, `allowed-tools`",
                  "S219, S220"),
    "Kimi Code": ("`.kimi-code/skills/`", "`whenToUse`, "
                  "`disableModelInvocation`", "S221, S222"),
    "Zhipu": ("`.zhipu/skills/`", "`name`, `description`", "S223, S224"),
}

SNAP_OF = {"S217": "S217-trae-ide.md", "S218": "S218-trae-user.md",
           "S219": "S219-cb-ide.md", "S220": "S220-cb-cli.md",
           "S221": "S221-kimi-en.md", "S222": "S222-kimi-zh.md",
           "S223": "S223-zhipu.md", "S224": "S224-zhipu.md"}

URL_OF = {"S217": "https://docs.trae.cn/ide_skills",
          "S218": "https://docs.trae.cn/ide_skills",
          "S219": "https://www.codebuddy.ai/docs/zh/ide/Features/Skills",
          "S220": "https://www.codebuddy.ai/docs/zh/cli/skills",
          "S221": "https://github.com/moonshotai/kimi-cli/blob/main/docs/en/"
                  "customization/skills.md",
          "S222": "https://www.kimi.com/code/docs/kimi-code-cli/"
                  "customization/skills.html",
          "S223": "https://docs.bigmodel.cn/cn/managed-agents/skills.md",
          "S224": "https://docs.bigmodel.cn/cn/managed-agents/skills.md"}


def _entry_text(rows: dict[str, tuple[str, str, str]] | None = None,
                quotes: dict[str, str] | None = None,
                snaps: dict[str, str] | None = None,
                trio: bool = True) -> str:
    rows = ENTRY_ROWS if rows is None else rows
    quotes = Q if quotes is None else quotes
    snaps = SNAP_OF if snaps is None else snaps
    head = []
    for sid in sorted(URL_OF):
        head.append(f'source: {sid} — fixture page — {URL_OF[sid]} — the '
                    f'"Skills" section — located quote "{quotes[sid]}" '
                    f'(snapshot `{snaps[sid]}:3`)')
    body = [""]
    if trio:
        body += ["verified-at: 2026-10-25", "recheck: 90d — re-fetch and confirm"]
    body += ["", "# Chinese-vendor skill surfaces (fixture)", "",
             "## Vendors", "",
             "| vendor | discovery root | keys | placement | sources | notes |",
             "|---|---|---|---|---|---|"]
    for vendor, (root, keys, ids) in rows.items():
        body.append(f"| {vendor} | {root} | {keys} | frontmatter | {ids} | "
                    f"fixture row |")
    return "\n".join(head + body) + "\n"


def _row_text(vendor: str) -> str:
    root, keys, ids = ENTRY_ROWS[vendor]
    return (f"| {vendor} | {root} | {keys} | frontmatter | {ids} | "
            f"fixture row |")


def _hide(row: str, opener: str, closer: str) -> str:
    """The entry with ``row`` out of the table and kept only as hidden bytes."""
    text = _entry_text()
    assert row + "\n" in text, row
    return (text.replace(row + "\n", "") + "\n" + opener + "\n"
            + row + "\n" + closer + "\n")


def _repin(files: dict[str, str]) -> dict[str, str]:
    """Re-sign the manifest after a world edits a snapshot on purpose."""
    snaps = {rel.rsplit("/", 1)[-1]: text
             for rel, text in files.items()
             if rel.startswith(SNAPDIR + "/") and text is not None}
    return _mutate(files, **{MANIFEST: _manifest(snaps)})


def _reg_line(sid: str, *, url: str | None = None, status: str = "mined",
              tier: str = "A", used_by: str = ENTRY,
              extra: int = 0) -> str:
    cells = [sid, f"fixture — {url or URL_OF[sid]}", "docs", tier,
             "fixture scope", "§ fixture; opened 2026-10-25",
             "fixture teaches cell", status, "2026-10-25", "90d", used_by]
    cells += [f"extra{i}" for i in range(extra)]
    return "| " + " | ".join(cells) + " |"


REG_HEADER = ("| id | source | kind | tier | scope | anchor | teaches | "
              "status | opened | recheck | used-by |\n"
              "|---|---|---|---|---|---|---|---|---|---|---|")


def _registry(lines: list[str] | None = None) -> str:
    body = lines if lines is not None else [_reg_line(sid)
                                            for sid in sorted(URL_OF)]
    return "# SOURCES fixture\n\n## Registry\n\n" + REG_HEADER + "\n" \
        + "\n".join(body) + "\n"


def _manifest(snaps: dict[str, str] | None = None) -> str:
    snaps = snaps or SNAP
    return "".join(f"{hashlib.sha256(v.encode()).hexdigest()}  {k}\n"
                   for k, v in snaps.items())


BASE_SOURCES = "# SOURCES fixture\n\n## Registry\n\n" + REG_HEADER + "\n"


def _honest_files() -> dict[str, str]:
    files = {SOURCES: _registry(), ENTRY: _entry_text(),
             MANIFEST: _manifest()}
    for name, text in SNAP.items():
        files[f"{SNAPDIR}/{name}"] = text
    return files


def _world(files: dict[str, str],
           base_files: dict[str, str] | None = None) -> tuple[str, str]:
    """A fresh isolated git repo: one base commit, then the measured commit."""
    d = tempfile.mkdtemp(prefix="k73-c1-")
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

    base = base_files if base_files is not None \
        else {SOURCES: BASE_SOURCES}
    place(base)
    base_sha = commit("base")
    place(files)
    commit("world")
    return d, base_sha


def _mutate(files: dict[str, str], **kw) -> dict[str, str]:
    out = dict(files)
    out.update(kw)
    return out


def _world_specs() -> list[dict]:
    """One honest world, then one broken world per conjunct and per shortcut."""
    honest = _honest_files()
    three = "vendor skill surfaces backed 3 of 4"
    zero = "vendor skill surfaces backed 0 of 4"
    specs: list[dict] = []
    add = specs.append

    # ---------------------------------------------------------- honest worlds
    add(dict(label="honest world scores 4 of 4", files=honest, code=0,
             line="vendor skill surfaces backed 4 of 4",
             finding="held at base: 0"))
    add(dict(label="base world (entry absent) is the do-nothing control",
             files={SOURCES: _registry()}, code=1, line=zero,
             finding=f"entry {ENTRY} absent"))
    add(dict(label="vendor hosts already in the base registry read held 4",
             files=honest,
             base_files={SOURCES: _registry()}, code=0,
             line="vendor skill surfaces backed 4 of 4",
             finding="held at base: 4"))
    add(dict(label="base registry with one TRAE host reads held at base: 1",
             files={SOURCES: _registry()}, code=1, line=zero,
             base_files={SOURCES: _registry([
                 _reg_line("S900",
                           url="https://docs.trae.cn/old-page")])},
             finding="held at base: 1"))
    add(dict(label="(d) quote wrapped across a line break is still found",
             files=_repin(_mutate(honest, **{
                 f"{SNAPDIR}/S217-trae-ide.md":
                     SNAP["S217-trae-ide.md"].replace(
                         "root and every skill", "root and every\nskill")})),
             code=0, line="vendor skill surfaces backed 4 of 4"))

    # ---------------------------------------------------------- (a) structure
    add(dict(label="(a) vendor row hidden in an HTML comment",
             files=_mutate(honest, **{ENTRY: _hide(
                 _row_text("TRAE"), "<!--", "-->")}),
             code=1, line=three,
             finding="TRAE: 0 vendor-table row(s) name TRAE"))
    add(dict(label="(a) vendor row hidden in a fenced block",
             files=_mutate(honest, **{ENTRY: _hide(
                 _row_text("TRAE"), "```text", "```")}),
             code=1, line=three,
             finding="TRAE: 0 vendor-table row(s) name TRAE"))
    add(dict(label="(a) two rows name the same vendor", files=_mutate(
        honest, **{ENTRY: _entry_text().replace(
            "| CodeBuddy |", "| TRAE | `.trae/skills/` | `name`, "
            "`description` | frontmatter | S217 | fixture row |\n| CodeBuddy |",
            1)}), code=1, line=three,
        finding="2 vendor-table row(s) name TRAE"))
    add(dict(label="(a) entry without verified-at:", files=_mutate(
        honest, **{ENTRY: _entry_text().replace(
            "verified-at: 2026-10-25\n", "")}),
        code=1, line=zero, finding="no verified-at: line"))
    add(dict(label="(a) entry without recheck:", files=_mutate(
        honest, **{ENTRY: _entry_text().replace(
            "recheck: 90d — re-fetch and confirm\n", "")}),
        code=1, line=zero, finding="no recheck: line"))
    add(dict(label="(a) cited id absent from the source: lines", files=_mutate(
        honest, **{ENTRY: _entry_text().replace(
            'source: S218 — fixture page', 'source: S918 — fixture page')}),
        code=1, line=zero, finding="cited S218 absent from the entry's own "
                                   "source: lines"))
    add(dict(label="(a) entry outside corpus/knowledge is not the entry",
             files=_mutate(honest, **{
                 ENTRY: None,
                 "corpus/notes/chinese-vendor-skill-surfaces-round73.md":
                     _entry_text()}), code=1, line=zero,
             finding=f"entry {ENTRY} absent"))
    add(dict(label="(a) entry with no vendor table", files=_mutate(
        honest, **{ENTRY: _entry_text(rows={})}),
        code=1, line=zero, finding="no table row names any of"))
    add(dict(label="(a) token-stuffed row (tokens the page never carries)",
             files=_mutate(honest, **{ENTRY: _entry_text().replace(
                 "| `.trae/skills/` | `name`, `description` |",
                 "| `.trae/skills/` | `name`, `description`, `.stuffed/root`, "
                 "`ztuff`, `ytuff` |")}),
             code=1, line=three, finding="token '.stuffed/root' does not occur"))
    add(dict(label="(a) absent root token (an invented placement path)",
             files=_mutate(honest, **{ENTRY: _entry_text().replace(
                 "| `.trae/skills/` |", "| `.trae/plugins/` |")}),
             code=1, line=three, finding="token '.trae/plugins/' does not occur"))
    add(dict(label="(a) root token occurs only in a page the row does not cite",
             files=_mutate(honest, **{ENTRY: _entry_text().replace(
                 "| `.trae/skills/` |", "| `.codebuddy/skills/` |")}),
             code=1, line=three,
             finding="token '.codebuddy/skills/' does not occur"))
    add(dict(label="(a) row with three keys but no root token", files=_mutate(
        honest, **{ENTRY: _entry_text().replace(
            "| `.trae/skills/` | `name`, `description` |",
            "| `name`, `description`, `whenToUse` |")}),
        code=1, line=three, finding="no discovery-root/placement token"))
    add(dict(label="(a) row with only two tokens", files=_mutate(
        honest, **{ENTRY: _entry_text().replace(
            "| `.trae/skills/` | `name`, `description` |",
            "| `.trae/skills/` | `name` |")}),
        code=1, line=three, finding="2 backticked token(s)"))
    add(dict(label="(a) vendor row named by a longer client name", files=_mutate(
        honest, **{ENTRY: _entry_text().replace(
            "| Kimi Code |", "| Kimi Codex |")}),
        code=1, line=three, finding="0 vendor-table row(s) name Kimi Code"))

    add(dict(label="(a) a key occurs only inside a longer word", files=_repin(
        _mutate(honest, **{f"{SNAPDIR}/S217-trae-ide.md":
                           SNAP["S217-trae-ide.md"].replace(
                               "declares name and description",
                               "declares filename and descriptions")})),
        code=1, line=three, finding="token 'name' does not occur"))
    add(dict(label="(a) a CJK character abutting a root is a boundary",
             files=_repin(_mutate(honest, **{
                 f"{SNAPDIR}/S217-trae-ide.md":
                     SNAP["S217-trae-ide.md"].replace(
                         "The project root is .trae/skills/ and",
                         "\u76ee\u5f55.trae/skills/\u4e0b and")})),
             code=0, line="vendor skill surfaces backed 4 of 4"))

    add(dict(label="(b) a pin of a different page on the same vendor host is "
                    "not the cited page", files=_mutate(
        honest, **{SOURCES: _registry([
            _reg_line("S217", url="https://docs.trae.cn/other-page")
            if x == "S217" else _reg_line(x) for x in sorted(URL_OF)])}),
        code=1, line=three,
        finding="carries no URL for the cited page "
                "https://docs.trae.cn/other-page"))

    # -------------------------------------------------------------- (b) rows
    add(dict(label="(b) cited row is queued, not mined", files=_mutate(
        honest, **{SOURCES: _registry([
            _reg_line("S217", status="queued") if s == "S217" else _reg_line(s)
            for s in sorted(URL_OF)])}),
        code=1, line=three, finding="S217: status 'queued'"))
    add(dict(label="(b) cited row is tier C", files=_mutate(
        honest, **{SOURCES: _registry([
            _reg_line("S217", tier="C") if s == "S217" else _reg_line(s)
            for s in sorted(URL_OF)])}),
        code=1, line=three, finding="S217: tier 'C'"))
    add(dict(label="(b) cited row has 12 cells", files=_mutate(
        honest, **{SOURCES: _registry([
            _reg_line("S217", extra=1) if s == "S217" else _reg_line(s)
            for s in sorted(URL_OF)])}),
        code=1, line=three, finding="S217: 12 cells"))
    add(dict(label="(b) cited row's used-by omits the entry", files=_mutate(
        honest, **{SOURCES: _registry([
            _reg_line("S217", used_by="corpus/knowledge/other-round73.md")
            if s == "S217" else _reg_line(s) for s in sorted(URL_OF)])}),
        code=1, line=three, finding="S217: used-by"))
    add(dict(label="(b) cited row's URL is not on the vendor's host",
             files=_mutate(honest, **{SOURCES: _registry([
                 _reg_line("S217", url="https://example.invalid/trae")
                 if s == "S217" else _reg_line(s) for s in sorted(URL_OF)])}),
             code=1, line=three, finding="no URL on TRAE's pinned host(s)"))
    add(dict(label="(b) cited row's URL is the other vendor's host",
             files=_mutate(honest, **{SOURCES: _registry([
                 _reg_line("S217",
                           url="https://www.codebuddy.ai/docs/zh/ide/Skills")
                 if s == "S217" else _reg_line(s) for s in sorted(URL_OF)])}),
             code=1, line=three, finding="no URL on TRAE's pinned host(s)"))
    add(dict(label="(b) registry holds no rows", files=_mutate(
        honest, **{SOURCES: _registry([])}),
        code=1, line=zero, finding="S217: 0 registry rows"))
    add(dict(label="(b) staged campaign-schema rows appended as-is",
             files=_mutate(honest, **{SOURCES: _registry(
                 [f"| {s} | {URL_OF[s]} | docs | staged |"
                  for s in sorted(URL_OF)])}),
             code=1, line=zero, finding="S217: 4 cells"))
    add(dict(label="(b) two registry rows for one cited id", files=_mutate(
        honest, **{SOURCES: _registry(
            [_reg_line(s) for s in sorted(URL_OF)] + [_reg_line("S217")])}),
        code=1, line=three, finding="S217: 2 registry rows"))
    add(dict(label="(b) cited id absent from the registry", files=_mutate(
        honest, **{SOURCES: _registry(
            [_reg_line(s) for s in sorted(URL_OF) if s != "S218"])}),
        code=1, line=three, finding="S218: 0 registry rows"))

    add(dict(label="(b) Kimi's path-pinned host: github.com/evil/kimi-cli "
                    "is not the pinned repo", files=_mutate(
        honest, **{SOURCES: _registry([
            _reg_line("S221", url="https://github.com/evil/kimi-cli/blob/main/"
                                  "docs/en/customization/skills.md")
            if x == "S221" else _reg_line(x) for x in sorted(URL_OF)])}),
        code=1, line=three, finding="no URL on Kimi Code's pinned host(s)"))

    # --------------------------------------------------------- (c) snapshots
    add(dict(label="(c) tampered snapshot (manifest hash left)",
             files=_mutate(honest, **{
                 f"{SNAPDIR}/S217-trae-ide.md":
                     SNAP["S217-trae-ide.md"] + "A hand edit.\n"}),
             code=2, line="snapshot_tampered",
             finding="snapshot_tampered"))
    add(dict(label="(c) no manifest at all", files=_mutate(
        honest, **{MANIFEST: None}), code=2, line="environment error",
        finding="no manifest at"))
    add(dict(label="(c) manifest line not `<sha256> <file>`", files=_mutate(
        honest, **{MANIFEST: _manifest() + "not-a-digest S999-x.md\n"}),
        code=2, line="environment error", finding="is not `<sha256>"))
    add(dict(label="(c) manifest path escapes the snapshot directory",
             files=_mutate(honest, **{
                 MANIFEST: _manifest() + "0" * 64 + "  ../S999-x.md\n"}),
             code=2, line="environment error", finding="escapes"))
    add(dict(label="(c) two pinned snapshots begin with one cited id",
             files=_mutate(honest, **{
                 ENTRY: _entry_text().replace(
                     " (snapshot `S217-trae-ide.md:3`)", ""),
                 MANIFEST: _manifest() + "0" * 64 + "  S217-ghost.md\n"}),
             code=2, line="environment error", finding="ambiguous"))
    add(dict(label="(c) entry names an uncommitted snapshot", files=_mutate(
        honest, **{
            ENTRY: _entry_text().replace(
                "(snapshot `S217-trae-ide.md:3`)",
                "(snapshot `S217-trae-ghost.md:3`)"),
            MANIFEST: _manifest() + "0" * 64 + "  S217-trae-ghost.md\n"}),
        code=2, line="environment error", finding="not committed"))

    # ------------------------------------------------------------- (d) quote
    add(dict(label="(d) located quote under 5 words", files=_mutate(
        honest, **{ENTRY: _entry_text(quotes=dict(
            Q, S217="TRAE reads skills now"))}),
        code=1, line=three, finding="S217: located quote is 4 words"))
    add(dict(label="(d) located quote over 25 words", files=_mutate(
        honest, **{ENTRY: _entry_text(quotes=dict(
            Q, S217=" ".join(["word"] * 26)))}),
        code=1, line=three, finding="S217: located quote is 26 words"))
    add(dict(label="(d) located quote absent from its snapshot", files=_mutate(
        honest, **{ENTRY: _entry_text(quotes=dict(
            Q, S217="TRAE ignores every project root and never reads a skill"))}),
        code=1, line=three, finding="not found in its pinned snapshot"))
    add(dict(label="(d) two distinct located quotes for one id", files=_mutate(
        honest, **{ENTRY: _entry_text().replace(
            "(snapshot `S217-trae-ide.md:3`)",
            "(snapshot `S217-trae-ide.md:3`)\n"
            'source: S217 — fixture page — https://docs.trae.cn/ide_skills — '
            f'located quote "{Q["S218"]}" (snapshot `S217-trae-ide.md:3`)')}),
        code=1, line=three, finding="S217: 2 distinct located quote(s)"))
    add(dict(label="(d) no backtick stripping: quoted code span absent from page",
             files=_mutate(honest, **{ENTRY: _entry_text(quotes=dict(
                 Q, S217="TRAE reads skills from the project root and every "
                         "skill declares `name` and `description`"))}),
             code=1, line=three, finding="not found in its pinned snapshot"))

    # ------------------------------------------------------- cannot-evaluate
    add(dict(label="unknown revision is exit 2", files=honest, code=2,
             rev="0" * 40, line="environment error", finding="not a commit"))
    add(dict(label="registry absent at the revision is exit 2", files=_mutate(
        honest, **{SOURCES: None}), code=2, line="environment error",
        finding=f"{SOURCES} absent"))
    add(dict(label="base registry unreadable is exit 2", files=honest,
             base_files={"README.md": "no registry at base\n"}, code=2,
             line="environment error",
             finding=f"{SOURCES} unreadable at base"))
    return specs


def _run_spec(spec: dict) -> tuple[bool, int, str]:
    """Run one world through ``main()`` in its own isolated git repo."""
    global BASE_REV
    saved = BASE_REV
    global _INTERNAL_SELFTEST
    d, base = _world(spec["files"], spec.get("base_files"))
    BASE_REV = base
    _INTERNAL_SELFTEST = True
    buf = io.StringIO()
    try:
        with contextlib.redirect_stdout(buf), \
                contextlib.redirect_stderr(buf):
            code = main(["--repo", d, "--rev", spec.get("rev", "HEAD")])
    finally:
        shutil.rmtree(d, ignore_errors=True)
        BASE_REV = saved
        _INTERNAL_SELFTEST = False
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


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(
        description="C1 Chinese-vendor skill-surface counter for kotoba "
                    "round 73")
    ap.add_argument("--rev", default=None, help="measured revision")
    ap.add_argument("--repo", default=str(_default_repo()))
    ap.add_argument("--self-test", action="store_true")
    ap.add_argument("--census-check", action="store_true",
                    help="also run sources-census.sh validate (second "
                         "evidence, never the verdict)")
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
    repo = Repo(Path(args.repo), args.rev)
    proc = _git(repo.path, ["rev-parse", "--verify", "-q",
                            f"{args.rev}^{{commit}}"])
    if proc.returncode != 0:
        print(f"environment error: --rev {args.rev} is not a commit",
              file=sys.stderr)
        return 2
    src = Path(__file__).read_text()
    if not _INTERNAL_SELFTEST and _blanked_sha(src) != SELF_SHA:
        print("environment error: counter drifted — the running file is not "
              "the frozen counter", file=sys.stderr)
        return 2
    try:
        n, findings, _backed = check(repo)
        held = held_at_base(repo)
    except EnvError as exc:
        print(f"environment error: {exc}", file=sys.stderr)
        return 2
    print(f"measured-rev: {args.rev}")
    print(f"vendor skill surfaces backed {n} of {TOTAL}")
    print(f"held at base: {held}")
    for finding in findings:
        print(f"  {finding}")
    if args.census_check:
        ok = repo.census_ok()
        print("census validate: " + ("conformant" if ok else
                                     ("could not evaluate" if ok is None
                                      else "findings")))
    return 0 if n == TOTAL else 1


if __name__ == "__main__":
    sys.exit(main())
