#!/usr/bin/env python3
r"""check_plugin_manifests.py v2 -- frozen counter for the round-57 C1 (depth) claim.

VERSION 2 (pre-data erratum, strictly stricter; round 57, before any C1
content).  Control CtlC1RealNoForm met the v1 predicate (found 5 of 7; new
ground 4; exit 0) with real pinned-host text and hollow tokens: a bare
`plugin.json` from a CHANGELOG bullet, the nav word `Extensions`, the source
file `extension.ts`, the link filename `writing-extensions.md`, and `plugins`;
and G counted `Extensions` as new because the held test was case-sensitive
while the base holds `extensions`.  Control CtlC1DoNothingJunk then met v1 with
bare-word tokens (`Plugins`, `Extensions`), 3-5-word page fragments as quotes,
entry `Manifest` cells that disagreed with SKILL.md, and one token serving two
clients.  v2 changes exactly six rules; each only adds a way to fail:

  E1  token grammar: the final path segment ends with `.json` and itself
      carries the plugin/extension word, AND the token has >= 2 path segments
      after stripping one `~/` or `./`, OR contains the row's OWN client marker.
  E2  the held-ground test is case-INSENSITIVE (still at path-segment
      boundaries); G stays the number of distinct casefold values.
  E3  a counted row's SOURCES URL whose decoded path contains, case-
      insensitively, `changelog`, `release`, `releases`, `news` or `blog` is
      rejected; with `--fetch`, a redirect onto such a URL is not found.
  E4  the entry row's `Manifest` cell, backticks stripped and trimmed, must
      equal the SKILL.md token or its normalise()d form (exact, case-
      sensitive), else that entry row is rejected.
  E5  a token whose casefold(normalise()) is used by SKILL.md table rows of
      two or more distinct client names (any client cell, listed or not)
      disqualifies every listed client whose row uses it.
  E6  the quote must hold at least 6 words (was 3); the upper bound stays 25.
  E7  (after CtlC1Fabricated) no non-final path segment, after stripping one
      `~/` or `./`, may contain a dot except as its first character, so a
      host+path such as `opencode.ai/docs/plugin.json` is never a manifest.

Everything else is v1 (sha256 2ac51d2a2f50d85590c307e6ef5aab05a0b660de42a33e5657011ecc05d6305b).

Round 57, claim C1 (axis: depth, the learning claim; sourced): `SKILL.md`
gains a decision table, `### Plugin manifests by client`, that tells a reader,
per client, which file declares a plugin's manifest, what a plugin can ship,
and what to do with it when reading a skill -- the `corpus/README.md` Frontier
row *Plugin manifests*.  Each row is grounded in a new knowledge entry,
`corpus/knowledge/plugin-manifests-round57.md`, whose per-client record quotes
the client's own documentation from a `corpus/SOURCES.md` row opened on
2026-10-23.

This counter is frozen before any round-57 C1 content exists.  The seven
clients, the hosts allowed for each client's source, the table anchors, the
token grammar, the foreign-name markers, the word bounds, the opened date, the
base revision and the targets are pinned here and never read from the revision
measured.  A later change to any of them is a second measurement, never the
declared one (corpus/QUALITY.md Q28).  It is round-56 v1.3 adapted: everything
not named below is v1.3 behaviour (SOURCES row parsing, tier A + status
`mined`, new-row-id and base-URL re-citation rejection with the v1.3 URL
normalisation, the pinned HOSTS map with segment-exact host/path matching,
tracker-URL rejection, docs-kind rejection, redirect checks, quote
normalisation, the `## Gate` quote requirement, fetch limits, and
token_at_boundary with both left and right boundaries).

THE FROZEN SPEC (this file implements it; it is not read from the tree):

  BASE_REV = 47c05558fa4e6043e45c7abca1fb5fd2fb8cda5a
  CLIENTS  = Claude Code, Codex, VS Code, Copilot CLI, Gemini CLI, Cursor, opencode
  HOSTS    = the pinned host map of round-56 v1.3, unchanged

  SKILL.md at the measured revision: a section whose heading line is exactly
  `### Plugin manifests by client`; its FIRST table has the header
  `| Client | Plugin manifest | What a plugin can ship | Action |`.  One row per
  client name (exact match to CLIENTS; a duplicate client row disqualifies that
  client).  The manifest token is the FIRST backticked span of the manifest
  cell.  The action cell must hold at least three words.

  A token is well-formed iff it matches
  `^(~/|\./)?[A-Za-z0-9_.-]+(/[A-Za-z0-9_.*-]+)*/?$`
  AND at least one path segment, split again on `-`, `.` and `_`, holds a word
  equal case-insensitively to `plugin`, `plugins`, `extension` or `extensions`
  AND no path segment contains `marketplace` (case-insensitively)
  AND (v2, E1) the final path segment ends with `.json` and itself holds the
  plugin/extension word (split on `-`, `.`, `_`) -- a trailing `/` leaves an
  empty final segment, so a directory never qualifies -- AND the token has at
  least two path segments after stripping one leading `~/` or `./`, or its
  lower-cased text contains the row's OWN client marker (below)
  AND (v2, E7) no non-final segment holds a dot other than as its first
  character (`.claude-plugin` is fine; `opencode.ai`, `1.0.0` are not).

    well-formed:  .claude-plugin/plugin.json, .codex-plugin/plugin.json,
                  .github/plugin/plugin.json, gemini-extension.json (Gemini CLI)
    not:          plugin.json, Extensions, extension.ts, writing-extensions.md,
                  plugins, .opencode/plugins/, .claude/agents/,
                  .claude-plugin/marketplace.json, package.json,
                  gemini-extension.json for any client but Gemini CLI

  FOREIGN-NAME GUARD (replaces the round-56 OWN_ROOTS rule): the client markers
  are Claude Code `claude`, Codex `codex`, VS Code `vscode`, Copilot CLI
  `copilot`, Gemini CLI `gemini`, Cursor `cursor`, opencode `opencode`.  A token
  whose lower-cased text contains ANOTHER client's marker is rejected for that
  client -- a VS Code row holding `.claude-plugin/plugin.json` is rejected.

  normalise(token) = strip one leading `~/` or `./`, strip one trailing `/`;
  case is PRESERVED (round-56 spot-check R4: the v1.3 held-ground count
  case-folded and matched `.claude/AGENTS.md` as `.claude/agents`).
  K = the number of client rows with a well-formed token.

  Entry `corpus/knowledge/plugin-manifests-round57.md` at the measured
  revision: its first table with the header `| Client | Manifest | Source |
  Quote |`.  The source cell holds one `S###` id; the quote cell holds the
  verbatim quote (one pair of surrounding straight or curly double quotes is
  stripped; backticks are stripped for word counting and for matching).

  A client is BACKED iff all of:
    * its SKILL.md row is unique and its token well-formed, and its action cell
      holds >= 3 words;
    * the token is not foreign to the client (FOREIGN-NAME GUARD);
    * (v2, E5) no SKILL.md row of another client name uses the same
      casefold(normalise(token));
    * an entry row names it, and (v2, E4) its `Manifest` cell, backticks
      stripped, equals the token or normalise(token);
    * the quote holds 6 (v2, E6; was 3) to 25 words;
    * the quote CONTAINS the raw token or its normalise()d form,
      CASE-SENSITIVE;
    * the quote matches `(?i)\b(plugins?|extensions?)\b` OUTSIDE that token's
      span;
    * the cited `S###` is a row of `corpus/SOURCES.md` at the measured revision,
      its id is NOT a row at BASE_REV, and its URL -- normalised by lowercasing
      scheme and host, percent-decoding and lowercasing the path, collapsing
      repeated slashes, stripping a trailing `/`, stripping a trailing `.md`,
      stripping `#fragment` and `?query` (round-56 v1.3 `url_key`) -- is not
      the normalised URL of any BASE_REV row;
    * that row has kind `docs`, tier `A`, status `mined`, and opened `2026-10-23`;
    * the row's URL host is pinned for that client (host_ok);
    * (v2, E3) the row's URL path, percent-decoded, contains none of
      `changelog`, `release`, `releases`, `news`, `blog` (case-insensitive);
    * the quote, whitespace-normalised, occurs in `corpus/lessons/round-57.md`
      section `## Gate` at the measured revision.

  With `--fetch`, a BACKED client is FOUND iff the live page at the row URL
  (timeout 30 s, at most 5 MiB, one retry, not redirected off the pinned hosts,
  not redirected onto a BASE_REV SOURCES URL, not redirected onto a v2 E3
  change-note URL, the round-56 v1.3 quote
  normalisation) contains the quote AND holds the token -- the raw token or its
  normalise()d form, CASE-SENSITIVE, on a case-preserving rendering of the page
  -- at a boundary: preceded by the start of the text, whitespace, a backtick,
  a quote character, `(` or `[`; followed by the end of the text or a character
  that is not a letter, a digit, `_` or `-` (so `.opencode/plugin` is not found
  inside `.opencode/plugins/`).  Preceding `.`, `/` and `-` are rejected, so a
  URL such as `opencode.ai/docs/plugins/` never yields the token `ai/docs/plugins`.

  NEW GROUND G = the number of DISTINCT casefold(normalise(token)) values among
  the FOUND clients that have ZERO held occurrences in the BASE_REV tree outside
  `.ufo/`, where a held occurrence is (v2, E2) a CASE-INSENSITIVE match of the
  normalised token at a path-segment boundary, read on the casefolded line: the
  preceding character is the start of a line, whitespace, a backtick, a quote
  character, `(`, `[`, `<`, `/`, `~` or `=`; the following character is the end
  of the line, or is not a letter, a digit, `_` or `-` and is not a `.` followed
  by a letter or a digit.  The two spellings `.Claude-Plugin/plugin.json` and
  `.claude-plugin/plugin.json` on two found clients count ONCE, and a base that
  holds either spelling holds both.  Blobs are read
  with `git ls-tree -r -z` + `git cat-file --batch`; a blob holding a NUL byte
  is skipped as binary, and paths under `.ufo/` are never read.  Self-test arms:
  `.Claude-Plugin/plugin.json` HOLDS `.claude-plugin/plugin.json` and
  `Extensions` text holds `extensions` (v2 case); `my.claude-plugin/plugin.json` is not held while
  `x/.claude-plugin/plugin.json` is and `.claude-plugin/plugin.jsonx` is not
  (segment); `.claude/AGENTS.md` does not hold `.claude/agents` (the round-56
  memory-file analogue); and the two spellings `.Claude-Plugin/plugin.json` and
  `.claude-plugin/plugin.json` count as one distinct value for G.

  Output: the FIRST line is always `counter sha256 <hex>` -- the sha256 of this
  file's own bytes, read from `__file__` (never from a pipe).  When a revision
  is measured, the second line is `counter rev <rev>`.  Then, with `--fetch`,
  `plugin manifests found on the live page F of K; new ground G`; without
  `--fetch`, `plugin manifests backed B of K; new ground not computed (needs
  --fetch)`.  Then one `reject <client>: <reasons>` line per rejected client
  and one `BACKED` detail line per backed client.

  Exit codes: with `--fetch`, 0 iff F >= 5 AND G >= 3, else 1; without
  `--fetch`, always 1 (the non-fetch run is not the predicate); 2 = could not
  evaluate (a `--rev` that is not a full 40-hex hash or does not resolve to a
  commit, a git failure, an unreadable file) with no traceback.

THE FROZEN PREDICATE (verbatim in substance, and the receipt label):

  `python3 -B verifiers/check_plugin_manifests.py --rev <rev> --fetch` exits 0
  iff it prints `plugin manifests found on the live page F of K; new ground G`
  with F >= 5 and G >= 3; receipt label
  `C1 predicate: --fetch exit 0 (F>=5, G>=3)`.

The counter reads the measured revision with read-only git (`git -C <lane>
show <rev>:<path>`, `git -C <lane> ls-tree`, `git -C <lane> cat-file`), never
from the working tree; the lane is the parent of the script's `verifiers/`
directory.

Usage:
  python3 -B verifiers/check_plugin_manifests.py --rev <rev> [--fetch] [--json]
  python3 -B verifiers/check_plugin_manifests.py --self-test
"""
from __future__ import annotations

import argparse
import contextlib
import hashlib
import html
import io
import json
import re
import string
import subprocess
import sys
import tempfile
import urllib.parse
import urllib.request
from pathlib import Path

BASE = "47c05558fa4e6043e45c7abca1fb5fd2fb8cda5a"
SKILL = "SKILL.md"
ENTRY = "corpus/knowledge/plugin-manifests-round57.md"
SOURCES = "corpus/SOURCES.md"
LESSON = "corpus/lessons/round-57.md"
TARGET = 5
NEW_TARGET = 3
MIN_WORDS = 6
MAX_WORDS = 25
OPENED = ("2026-10-23",)
MAX_BYTES = 5 * 1024 * 1024
FETCH_TIMEOUT = 30
CHUNK = 256
LANE_FALLBACK = Path("/home/vgpnk/Projects/shokunin/kotoba-shokunin")
CLIENTS = ("Claude Code", "Codex", "VS Code", "Copilot CLI", "Gemini CLI",
           "Cursor", "opencode")
HOSTS = {
    "Claude Code": ("code.claude.com", "docs.claude.com", "docs.anthropic.com",
                    "platform.claude.com", "github.com/anthropics/claude-code",
                    "raw.githubusercontent.com/anthropics/claude-code"),
    "Codex": ("developers.openai.com", "learn.chatgpt.com", "github.com/openai/codex",
              "raw.githubusercontent.com/openai/codex"),
    "VS Code": ("code.visualstudio.com", "github.com/microsoft/vscode",
                "github.com/microsoft/vscode-docs",
                "raw.githubusercontent.com/microsoft/vscode-docs"),
    "Copilot CLI": ("docs.github.com", "github.com/github/copilot-cli",
                    "raw.githubusercontent.com/github/copilot-cli"),
    "Gemini CLI": ("geminicli.com", "github.com/google-gemini/gemini-cli",
                   "raw.githubusercontent.com/google-gemini/gemini-cli"),
    "Cursor": ("cursor.com", "docs.cursor.com"),
    "opencode": ("opencode.ai", "github.com/sst/opencode", "github.com/anomalyco/opencode",
                 "raw.githubusercontent.com/sst/opencode",
                 "raw.githubusercontent.com/anomalyco/opencode"),
}
MARKERS = {
    "Claude Code": "claude",
    "Codex": "codex",
    "VS Code": "vscode",
    "Copilot CLI": "copilot",
    "Gemini CLI": "gemini",
    "Cursor": "cursor",
    "opencode": "opencode",
}
SKILL_HEADING = "### Plugin manifests by client"
SKILL_HEADER = ("client", "plugin manifest", "what a plugin can ship", "action")
ENTRY_HEADER = ("client", "manifest", "source", "quote")
REV_RE = re.compile(r"^[0-9a-fA-F]{40}$")
TOKEN_RE = re.compile(r"^(~/|\./)?[A-Za-z0-9_.-]+(/[A-Za-z0-9_.*-]+)*/?$")
SEG_SPLIT_RE = re.compile(r"[-._]")
PLUGIN_WORDS = ("plugin", "plugins", "extension", "extensions")
MARKETPLACE = "marketplace"
BACKTICK_RE = re.compile(r"`([^`]+)`")
SID_RE = re.compile(r"^`?(S\d{3,})`?$")
URL_RE = re.compile(r"https?://[^\s)>\]`]+")
SOURCES_ROW_RE = re.compile(r"^\|[ \t]*S[0-9]{3,}[ \t]*\|")
PLUGIN_WORD_RE = re.compile(r"\b(?:plugins?|extensions?)\b", re.IGNORECASE)
SEPARATOR_RE = re.compile(r":?-{3,}:?")
BOUNDARY_PREV = frozenset(" \t\r\n`\"'([")
TRIM_CHARS = ".,;:!?)]}'\""
ASCII_ALNUM = frozenset(string.ascii_letters + string.digits)
HELD_PREV = frozenset("`\"'([</~=")
HELD_NEXT_BAD = frozenset(string.ascii_letters + string.digits + "_-")
UFO_PREFIX = ".ufo/"


class EnvError(Exception):
    """Could not evaluate: unknown revision, git failure, unreadable file."""


# ---------------------------------------------------------------- lane access

def lane_dir() -> Path:
    """The lane repository: the parent of the script's `verifiers/` directory.

    Integrated in the lane the script sits in `<lane>/verifiers/`, so the lane
    is its parent.  A copy kept outside the lane (a sandbox clone) is found by
    walking up for the lane markers; the lane checkout itself is the last
    resort.  The path is never taken from the environment."""
    here = Path(__file__).resolve().parent
    cands = []
    if here.name == "verifiers":
        cands.append(here.parent)
    for base in (here, here.parent):
        for cand in (base, *base.parents):
            if (cand / "SKILL.md").is_file() and (cand / "corpus" / "SOURCES.md").is_file():
                cands.append(cand)
                break
    cands.append(LANE_FALLBACK)
    for cand in cands:
        if (cand / "SKILL.md").is_file() and (cand / "corpus" / "SOURCES.md").is_file():
            return cand
    raise EnvError("lane repository not found near %s" % here)


def self_sha() -> str:
    """sha256 of this file's own bytes, read from `__file__`, never from stdin."""
    with open(__file__, "rb") as fh:
        return hashlib.sha256(fh.read()).hexdigest()


def git(lane: Path, args: list[str], data: bytes | None = None) -> subprocess.CompletedProcess:
    try:
        return subprocess.run(["git", "-C", str(lane)] + args,
                              input=data, capture_output=True)
    except OSError as e:
        raise EnvError("git not runnable: %s" % e) from e


def rev_ok(rev: str | None) -> bool:
    """A revision must be a full 40-hex commit hash; a branch name is not one."""
    return bool(rev) and REV_RE.match(rev) is not None


def verify_rev(lane: Path, rev: str) -> None:
    """An unknown revision is could-not-evaluate (2), never an empty tree (1)."""
    r = git(lane, ["rev-parse", "--verify", "--quiet", "%s^{commit}" % rev])
    if r.returncode != 0:
        raise EnvError("revision %r is not a commit in %s" % (rev, lane))


def git_show(lane: Path, rev: str, path: str) -> str | None:
    r = git(lane, ["show", "%s:%s" % (rev, path)])
    if r.returncode != 0:
        err = r.stderr.decode(errors="replace")
        if "does not exist" in err or "exists on disk, but not in" in err:
            return None
        raise EnvError("git show %s:%s failed: %s" % (rev, path, err.strip()))
    return r.stdout.decode("utf-8")


# ------------------------------------------------------------- table plumbing

def cells(line: str) -> list[str]:
    s = line.strip()
    if not (s.startswith("|") and s.endswith("|")) or len(s) < 2:
        return []
    return [c.strip() for c in s[1:-1].split("|")]


def clean(cell: str) -> str:
    """Header comparison: drop emphasis/backticks, lower-case."""
    return re.sub(r"[`*]", "", cell).strip().lower()


def client_name(cell: str) -> str:
    """Client-cell comparison: drop emphasis/backticks, keep the case."""
    return re.sub(r"[`*]", "", cell).strip()


def is_separator(row: list[str]) -> bool:
    return bool(row) and all(SEPARATOR_RE.fullmatch(x) for x in row)


def tables(text: str):
    """Yield (header_cells, row_cells) for every markdown table in `text`."""
    block: list[str] = []

    def flush():
        if not block:
            return None
        head = cells(block[0])
        rows = []
        for ln in block[1:]:
            c = cells(ln)
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


def section_lines(text: str, heading: str) -> list[str]:
    """Lines of the section whose heading line is exactly `heading`."""
    level = len(heading) - len(heading.lstrip("#"))
    out: list[str] = []
    inside = False
    for ln in text.splitlines():
        m = re.match(r"^(#{1,6})\s+", ln)
        if m:
            if ln.rstrip() == heading:
                inside = True
                continue
            if inside and len(m.group(1)) <= level:
                break
            continue
        if inside:
            out.append(ln)
    return out


def skill_rows(skill: str) -> list[list[str]]:
    """Rows of the FIRST table of the `### Plugin manifests by client` section.

    The first table's header must be the frozen one; otherwise nothing is read."""
    sec = section_lines(skill, SKILL_HEADING)
    if not sec:
        return []
    for head, rows in tables("\n".join(sec)):
        if tuple(clean(x) for x in head[:len(SKILL_HEADER)]) == SKILL_HEADER:
            return rows
        return []
    return []


def entry_rows(entry: str) -> list[list[str]]:
    """Rows of the first table whose header is the frozen entry header."""
    for head, rows in tables(entry):
        if tuple(clean(x) for x in head[:len(ENTRY_HEADER)]) == ENTRY_HEADER:
            return rows
    return []


# ------------------------------------------------------------------ SOURCES.md

def sources_table(text: str) -> dict[str, list[str]]:
    """id -> [id, source, kind, tier, scope, anchor, teaches, status, opened, recheck, used-by]."""
    out: dict[str, list[str]] = {}
    for ln in text.splitlines():
        if SOURCES_ROW_RE.match(ln):
            c = ln.split("|")
            if len(c) == 13:
                out[c[1].strip()] = [x.strip() for x in c[1:12]]
    return out


def source_ids(text: str) -> set[str]:
    return {ln.split("|")[1].strip() for ln in text.splitlines() if SOURCES_ROW_RE.match(ln)}


def urls_of(cell: str) -> list[str]:
    """Every http(s) URL in a cell, with trailing sentence punctuation removed."""
    out = []
    for m in URL_RE.finditer(cell):
        u = m.group(0).rstrip(TRIM_CHARS)
        if u:
            out.append(u)
    return out


def url_key(url: str | None) -> str:
    """Frozen URL normalisation: lowercase scheme+host, drop trailing `/`, drop
    trailing `.md`, drop `#fragment` and `?query`; path percent-decoded and
    lowercased, `www.` dropped, repeated slashes collapsed (round-56 v1.3)."""
    if not url:
        return ""
    u = urllib.parse.urlsplit(url)
    host = (u.hostname or "").lower()
    if host.startswith("www."):
        host = host[4:]
    path = urllib.parse.unquote(u.path or "").lower()
    path = re.sub(r"/{2,}", "/", path)
    while path.endswith("/"):
        path = path[:-1]
    if path.endswith(".md"):
        path = path[:-3]
    while path.endswith("/"):
        path = path[:-1]
    return "//%s%s" % (host, path)


def base_url_keys(base_sources: str) -> set[str]:
    keys = set()
    for ln in base_sources.splitlines():
        if SOURCES_ROW_RE.match(ln):
            c = ln.split("|")
            if len(c) > 2:
                for u in urls_of(c[2]):
                    keys.add(url_key(u))
    return keys


TRACKER_SEGMENTS = {"issues", "issue", "pull", "pulls", "discussions", "commit",
                    "commits", "compare"}


def url_is_tracker(url: str) -> bool:
    """An issue, PR, discussion or commit URL (any host)."""
    path = urllib.parse.unquote(urllib.parse.urlsplit(url).path or "").lower()
    return any(seg in TRACKER_SEGMENTS for seg in path.split("/") if seg)


CHANGE_NOTE_WORDS = ("changelog", "release", "releases", "news", "blog")


def url_is_change_note(url: str) -> bool:
    """v2: a URL whose decoded path contains a change-note word (substring,
    case-insensitive) is a change note, not documentation."""
    path = urllib.parse.unquote(urllib.parse.urlsplit(url).path or "").lower()
    return any(w in path for w in CHANGE_NOTE_WORDS)


def host_ok(url: str, pins: tuple[str, ...]) -> bool:
    u = urllib.parse.urlparse(url)
    host, path = (u.hostname or "").lower(), u.path
    if any(seg in (".", "..") for seg in urllib.parse.unquote(path).split("/")):
        return False
    for pin in pins:
        h, _, p = pin.partition("/")
        if p:
            prefix = "/" + p
            if host == h and (path == prefix or path.startswith(prefix + "/")):
                return True
        elif host == h or host.endswith("." + h):
            return True
    return False


# ------------------------------------------------------------- token machinery

def seg_words(seg: str) -> list[str]:
    return [w.lower() for w in SEG_SPLIT_RE.split(seg) if w]


def token_well_formed(token: str | None, client: str) -> bool:
    """The frozen token grammar (v2): a manifest FILE path for `client`.

    v1 rules: TOKEN_RE, a plugin/extension word in some segment, no
    `marketplace` segment.  v2 adds: the final segment ends with `.json` and
    itself carries the plugin/extension word, and the token either has >= 2
    path segments after stripping one `~/` or `./`, or contains the client's
    own marker.  A trailing `/` leaves an empty final segment, so a directory
    is never a manifest."""
    if not token or not TOKEN_RE.match(token):
        return False
    segs = [s for s in token.split("/") if s]
    if any(MARKETPLACE in s.lower() for s in segs):
        return False
    if not any(w in PLUGIN_WORDS for s in segs for w in seg_words(s)):
        return False
    body = token[2:] if token.startswith(("~/", "./")) else token
    parts = body.split("/")
    if any("." in seg[1:] for seg in parts[:-1]):
        return False
    last = parts[-1]
    if not last.endswith(".json") or not any(w in PLUGIN_WORDS for w in seg_words(last)):
        return False
    return len(parts) >= 2 or MARKERS[client] in token.lower()


def foreign_marker(client: str, token: str | None) -> str | None:
    """The other client whose marker the token carries, or None."""
    low = (token or "").lower()
    for other in CLIENTS:
        if other != client and MARKERS[other] in low:
            return other
    return None


def normalise(token: str | None) -> str:
    """Strip one leading `~/` or `./` and one trailing `/`; case is PRESERVED."""
    if not token:
        return ""
    t = token.strip()
    for pre in ("~/", "./"):
        if t.startswith(pre):
            t = t[2:]
            break
    if t.endswith("/"):
        t = t[:-1]
    return t


def token_span(text: str, token: str | None) -> tuple[int, int] | None:
    """Span of the first CASE-SENSITIVE raw-token or normalised-form occurrence."""
    if not token:
        return None
    best: tuple[int, int] | None = None
    for form in (token, normalise(token)):
        if not form:
            continue
        i = text.find(form)
        if i < 0:
            continue
        if best is None or i < best[0]:
            best = (i, i + len(form))
    return best


def plugin_word_outside(text: str, start: int, end: int) -> bool:
    """Is there a `plugin(s)`/`extension(s)` word outside the token span?"""
    for m in PLUGIN_WORD_RE.finditer(text):
        if m.end() <= start or m.start() >= end:
            return True
    return False


def strip_quotes(cell: str) -> str:
    """Strip one pair of surrounding straight or curly double quotes."""
    s = cell.strip()
    for a, b in (('"', '"'), ("\u201c", "\u201d")):
        if len(s) >= 2 and s.startswith(a) and s.endswith(b):
            return s[1:-1].strip()
    return s


def ws(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()


def quote_in_gate(quote: str, gate_raw: str, gate_plain: str) -> bool:
    """Is the (whitespace-normalised) quote recorded in the Gate section?"""
    return ws(quote) in gate_raw or ws(quote.replace("`", "")) in gate_plain


# ------------------------------------------------------------------- the judge

def manifest_cell_matches(cell: str, token: str) -> bool:
    """v2 E4: the entry `Manifest` cell, backticks stripped, IS the SKILL.md
    token or its normalise()d form (exact, case-sensitive)."""
    return cell.replace("`", "").strip() in (token, normalise(token))


def shared_tokens(srows: list[list[str]]) -> dict[str, set[str]]:
    """v2 E5: casefold(normalise(first backticked span)) -> the client names of
    every SKILL.md table row that uses it (any row, whatever its client cell)."""
    users: dict[str, set[str]] = {}
    for r in srows:
        r = (r + ["", ""])[:2]
        spans = BACKTICK_RE.findall(r[1])
        if spans:
            users.setdefault(normalise(spans[0]).casefold(), set()).add(client_name(r[0]))
    return users


def entry_row_verdict(er: list[str], client: str, token: str | None,
                      table: dict[str, list[str]], at_base: set[str],
                      base_urls: set[str], gate_raw: str,
                      gate_plain: str) -> tuple[list[str], str | None, str | None, str | None]:
    """Judge one entry row.  Returns (why, sid, url, quote).

    A malformed token has already been rejected on the SKILL.md side, so the
    entry row only looks for a token span when a token was read at all."""
    why: list[str] = []
    sid = url = quote = None
    if token and not manifest_cell_matches(er[1], token):
        why.append("entry Manifest cell %r is not the SKILL.md token %r"
                   % (er[1], token))
    m = SID_RE.match(er[2].strip())
    sid = m.group(1) if m else None
    if not sid:
        why.append("entry source cell is not one S### id: %r" % er[2])
    quote = strip_quotes(er[3])
    q_plain = quote.replace("`", "")
    n = len(q_plain.split())
    if not MIN_WORDS <= n <= MAX_WORDS:
        why.append("quote holds %d words (need %d-%d)" % (n, MIN_WORDS, MAX_WORDS))
    if token:
        span = token_span(q_plain, token)
        if span is None:
            why.append("quote does not hold the manifest token %r (case-sensitive)"
                       % token)
        elif not plugin_word_outside(q_plain, span[0], span[1]):
            why.append("quote holds no plugin/extension word outside the token")
    if not quote_in_gate(quote, gate_raw, gate_plain):
        why.append("round-57 Gate does not record this quote")
    if sid:
        if sid in at_base:
            why.append("%s is already a SOURCES row at base" % sid)
        s = table.get(sid)
        if not s:
            why.append("%s absent or malformed in SOURCES.md" % sid)
        else:
            if s[2] != "docs":
                why.append("%s kind %r (need docs)" % (sid, s[2]))
            if s[3] != "A":
                why.append("%s tier %r" % (sid, s[3]))
            if s[7] != "mined":
                why.append("%s status %r" % (sid, s[7]))
            if s[8] not in OPENED:
                why.append("%s opened %r" % (sid, s[8]))
            urls = urls_of(s[1])
            url = urls[0] if urls else None
            if not url:
                why.append("%s source cell holds no URL" % sid)
            else:
                if url_key(url) in base_urls:
                    why.append("%s URL %r is already a base SOURCES URL" % (sid, url))
                if not host_ok(url, HOSTS[client]):
                    why.append("%s URL %r is not on a pinned host" % (sid, url))
                if url_is_tracker(url):
                    why.append("%s URL %r is an issue/PR/discussion/commit page, not documentation"
                               % (sid, url))
                if url_is_change_note(url):
                    why.append("%s URL %r is a changelog/release/news/blog page, not documentation"
                               % (sid, url))
    return why, sid, url, quote


def judge(skill: str, entry: str, sources: str, lesson: str,
          base_sources: str) -> list[dict]:
    srows = skill_rows(skill)
    erows = entry_rows(entry)
    table = sources_table(sources)
    at_base = source_ids(base_sources)
    base_urls = base_url_keys(base_sources)
    gate = gate_section(lesson)
    gate_raw = ws(gate)
    gate_plain = ws(gate.replace("`", ""))
    users = shared_tokens(srows)
    report = []
    for client in CLIENTS:
        why: list[str] = []
        token = None
        norm_tok = ""
        in_k = False
        smine = [r for r in srows if client_name(r[0]) == client]
        if len(smine) != 1:
            why.append("SKILL.md rows naming client: %d (need exactly 1)" % len(smine))
        else:
            sr = ((smine[0] if smine else []) + ["", "", "", ""])[:4]
            spans = BACKTICK_RE.findall(sr[1])
            token = spans[0] if spans else None
            if token is None:
                why.append("SKILL.md manifest cell holds no backticked token")
            elif not token_well_formed(token, client):
                why.append("SKILL.md manifest token %r is not well-formed" % token)
            else:
                norm_tok = normalise(token)
                in_k = True
                other = foreign_marker(client, token)
                if other:
                    why.append("SKILL.md manifest token %r carries %s's marker %r"
                               % (token, other, MARKERS[other]))
            if token is not None:
                sharers = users.get(normalise(token).casefold(), set())
                if len(sharers) >= 2:
                    why.append("SKILL.md manifest token %r is shared by rows %s"
                               % (token, ", ".join(sorted(sharers))))
            words = re.sub(r"[`*]", "", sr[3]).split()
            if len(words) < 3:
                why.append("SKILL.md action cell holds %d words (need >= 3)" % len(words))
        emine = [(r + ["", "", "", ""])[:4] for r in erows if client_name(r[0]) == client]
        picked = None
        row_whys = []
        for er in emine:
            row_why, sid, url, quote = entry_row_verdict(
                er, client, token, table, at_base, base_urls,
                gate_raw, gate_plain)
            if not row_why:
                picked = {"row": sid, "url": url, "quote": quote}
                break
            row_whys.append("entry row %s: %s" % (er[2].strip() or "-", "; ".join(row_why)))
        if not emine:
            why.append("no entry row names the client")
        elif picked is None:
            why.extend(row_whys)
        report.append({"client": client,
                       "row": picked["row"] if picked else None,
                       "url": picked["url"] if picked else None,
                       "quote": picked["quote"] if picked else None,
                       "token": token, "norm": norm_tok, "in_k": in_k,
                       "backed": not why, "why": why})
    return report


def gate_section(lesson: str) -> str:
    """The `## Gate` section of a round lesson."""
    out: list[str] = []
    inside = False
    for line in lesson.splitlines():
        if line.startswith("## "):
            inside = line.rstrip() == "## Gate"
            continue
        if inside:
            out.append(line)
    return "\n".join(out)


# ------------------------------------------------------------------ the fetch

def page_plain(s: str) -> str:
    """The v1.3 `_plain` without its final lower-casing: case is preserved."""
    s = html.unescape(s)
    s = re.sub(r"[`*_]", "", s)
    s = s.replace("\u2019", "'").replace("\u201c", '"').replace("\u201d", '"')
    return re.sub(r"\s+", " ", s).strip()


def _plain(s: str) -> str:
    """The v1.3 quote-side normalisation: `page_plain` then lower-case."""
    return page_plain(s).lower()


def norm(s: str) -> str:
    """Quote side: no angle-bracket text is removed."""
    return _plain(s)


def norm_page_case(s: str) -> str:
    """Page normalisation with the case kept, for the case-sensitive token."""
    s = re.sub(r"(?is)<(style|script)\b.*?</\1\s*>", " ", s)
    s = re.sub(r"(?s)<!--.*?-->", " ", s)
    s = re.sub(r"</?[A-Za-z][^>]*>", " ", s)
    return page_plain(s)


def norm_page(s: str) -> str:
    """The round-56 v1.3 page normalisation used for the quote."""
    return norm_page_case(s).lower()


def boundary_ok(text: str, idx: int) -> bool:
    """Is the occurrence at `idx` at a token boundary?"""
    if idx == 0:
        return True
    return text[idx - 1] in BOUNDARY_PREV


def token_at_boundary(text: str, token: str) -> bool:
    """Does `token` occur in `text` at a boundary?  CASE-SENSITIVE.

    Both ends are checked: the left character must be the start of the text or
    one of BOUNDARY_PREV, and the right character must be the end of the text
    or not a letter, a digit, `_` or `-` (so `.opencode/plugin` is not found
    inside `.opencode/plugins/`)."""
    if not token:
        return False
    start = 0
    while True:
        i = text.find(token, start)
        if i < 0:
            return False
        j = i + len(token)
        right_ok = j >= len(text) or not (text[j] in ASCII_ALNUM or text[j] in "_-")
        if boundary_ok(text, i) and right_ok:
            return True
        start = i + 1


def token_forms(token: str | None) -> list[str]:
    """The raw manifest token and its normalise()d form, each also passed
    through the case-preserving page normalisation (which drops `*`, `_` and
    backticks).  Case is preserved: the comparison is case-sensitive."""
    if not token:
        return []
    forms: list[str] = []
    for cand in (token, normalise(token)):
        for f in (cand, page_plain(cand)):
            if f and f not in forms:
                forms.append(f)
    return forms


def fetch(url: str, pins: tuple[str, ...] | None = None,
          base_keys: set[str] | None = None) -> str:
    """Plain HTTP GET, 30 s timeout, at most 5 MiB, one retry.

    When `pins` is given, the URL reached after redirects must still be on the
    client's pinned hosts; when `base_keys` is given, a page whose URL after
    redirects is a base SOURCES URL is not found.  Both only add failures."""
    last: Exception | None = None
    for _ in range(2):
        try:
            req = urllib.request.Request(url, headers={
                "User-Agent": "kotoba-shokunin-counter/57"})
            with urllib.request.urlopen(req, timeout=FETCH_TIMEOUT) as r:
                final = r.geturl()
                data = r.read(MAX_BYTES + 1)
            if pins is not None and not host_ok(final, pins):
                raise OSError("redirected off the pinned hosts to %s" % final)
            if base_keys is not None and url_key(final) in base_keys:
                raise OSError("reached a base SOURCES URL %s" % final)
            if url_is_change_note(final):
                raise OSError("redirected onto a change-note page %s" % final)
            if len(data) > MAX_BYTES:
                raise OSError("page exceeds 5 MiB")
            return data.decode("utf-8", errors="replace")
        except Exception as e:  # network or decode failure: not found
            last = e
    raise last if last else OSError("fetch failed")


def found_on_page(page_text: str, quote: str, token: str | None) -> bool:
    """The live page holds the quote AND the manifest token at a boundary."""
    if not quote or norm(quote) not in norm_page(page_text):
        return False
    text = norm_page_case(page_text)
    return any(token_at_boundary(text, f) for f in token_forms(token))


# ------------------------------------------------------- held occurrences (base)

def ls_tree_blobs(lane: Path, rev: str) -> list[tuple[str, str]]:
    """(path, sha) for every blob in `rev` outside `.ufo/`, in tree order."""
    r = git(lane, ["ls-tree", "-r", "-z", "--full-tree", rev])
    if r.returncode != 0:
        raise EnvError("git ls-tree %s failed: %s"
                       % (rev, r.stderr.decode(errors="replace").strip()))
    out: list[tuple[str, str]] = []
    for rec in r.stdout.split(b"\0"):
        if not rec:
            continue
        meta, sep, path = rec.partition(b"\t")
        parts = meta.split()
        if not sep or len(parts) != 3:
            raise EnvError("unreadable git ls-tree record: %r" % rec[:80])
        _mode, kind, sha = parts
        if kind != b"blob":
            continue
        p = path.decode("utf-8", "replace")
        if p == ".ufo" or p.startswith(UFO_PREFIX):
            continue
        out.append((p, sha.decode("ascii", "replace")))
    return out


def parse_batch(data: bytes) -> list[bytes]:
    """Bodies of the blobs in `git cat-file --batch` output; others skipped."""
    out: list[bytes] = []
    pos, n = 0, len(data)
    while pos < n:
        nl = data.find(b"\n", pos)
        if nl < 0:
            raise EnvError("git cat-file --batch output truncated")
        parts = data[pos:nl].decode("utf-8", "replace").split()
        pos = nl + 1
        if len(parts) != 3 or parts[1] != "blob":
            continue
        size = int(parts[2])
        body = data[pos:pos + size]
        if len(body) != size:
            raise EnvError("git cat-file --batch body truncated")
        pos += size + 1
        out.append(body)
    return out


def read_blobs(lane: Path, shas: list[str]) -> list[bytes]:
    if not shas:
        return []
    r = git(lane, ["cat-file", "--batch"],
            data="".join(s + "\n" for s in shas).encode("ascii", "replace"))
    if r.returncode != 0:
        raise EnvError("git cat-file --batch failed: %s"
                       % r.stderr.decode(errors="replace").strip())
    return parse_batch(r.stdout)


def held_in_text(text: str, token: str) -> bool:
    """A CASE-INSENSITIVE (v2) occurrence of `token` at a path-segment boundary.

    Both sides are casefolded and the boundaries are read on the casefolded
    line, so `.claude/AGENTS.md` still does not hold `.claude/agents`."""
    if not token:
        return False
    token = token.casefold()
    for line in text.casefold().splitlines():
        start = 0
        while True:
            i = line.find(token, start)
            if i < 0:
                break
            j = i + len(token)
            left = i == 0 or line[i - 1].isspace() or line[i - 1] in HELD_PREV
            if left and held_right_ok(line, j):
                return True
            start = i + 1
    return False


def held_right_ok(line: str, j: int) -> bool:
    """The character after the match: end of line, or a non-word, non-dot-word one."""
    if j >= len(line):
        return True
    c = line[j]
    if c in HELD_NEXT_BAD:
        return False
    if c == "." and j + 1 < len(line) and line[j + 1] in ASCII_ALNUM:
        return False
    return True


def held_in_blob(data: bytes, token: str) -> bool:
    """Binary blobs (a NUL byte) are skipped, as git treats them."""
    if b"\0" in data:
        return False
    return held_in_text(data.decode("utf-8", "replace"), token)


def held_in_base(lane: Path, rev: str, tokens: set[str]) -> dict[str, bool]:
    """token -> does the tree of `rev`, outside `.ufo/`, hold it?"""
    out = {t: False for t in tokens if t}
    pending = set(out)
    if not pending:
        return out
    entries = ls_tree_blobs(lane, rev)
    for i in range(0, len(entries), CHUNK):
        bodies = read_blobs(lane, [sha for _p, sha in entries[i:i + CHUNK]])
        for body in bodies:
            for t in sorted(pending):
                if held_in_blob(body, t):
                    out[t] = True
                    pending.discard(t)
        if not pending:
            break
    return out


# ------------------------------------------------------------------- the lines

def summary_line(fetching: bool, backed: int, k: int, found: int, ground: int) -> str:
    if fetching:
        return "plugin manifests found on the live page %d of %d; new ground %d" % (
            found, k, ground)
    return "plugin manifests backed %d of %d; new ground not computed (needs --fetch)" % (
        backed, k)


def reject_line(client: str, why: list[str]) -> str:
    return "reject %s: %s" % (client, "; ".join(why))


def predicate(fetching: bool, found: int, ground: int) -> int:
    if not fetching:
        return 1
    return 0 if found >= TARGET and ground >= NEW_TARGET else 1


def new_ground(norms: list[str], held: dict[str, bool]) -> int:
    """Distinct casefold(normalise(token)) values with ZERO held occurrences.

    `held` is keyed by the case-preserved normalised token; since v2 the held
    test itself is case-insensitive, so both spellings of one token get the
    same answer, and two clients whose tokens differ in case alone count once."""
    return len({t.casefold() for t in norms if t and not held.get(t)})


# ----------------------------------------------------- the self-test's git world

def held_world() -> tuple[dict[str, bool], dict[str, object]]:
    """A throw-away repository proving the base-tree scan and the git guards.

    `.claude-plugin/plugin.json` sits only under `.ufo/`; `.CURSOR/plugins`
    differs in case only; `.copilot-plugin/plugin.json` sits only in a binary
    blob; `.opencode/plugins` sits only in a blob reachable through a gitlink;
    `gemini-extension.json` sits in an ordinary tracked file."""
    tokens = [".claude-plugin/plugin.json", "gemini-extension.json",
              ".cursor/plugins", ".copilot-plugin/plugin.json",
              ".opencode/plugins"]
    with tempfile.TemporaryDirectory(prefix="cmp-self-test-") as td:
        repo = Path(td)
        (repo / ".ufo").mkdir()
        (repo / "a.md").write_text("see `gemini-extension.json` here\n", encoding="utf-8")
        (repo / ".ufo" / "b.md").write_text(".claude-plugin/plugin.json\n", encoding="utf-8")
        (repo / "c.md").write_text(".CURSOR/plugins\n", encoding="utf-8")
        (repo / "d.bin").write_bytes(b"binary\0\n.copilot-plugin/plugin.json\n")
        _self_git("init", "-q", str(repo))
        _self_git("-C", str(repo), "add", "-A", "-f", ".")
        _self_git("-C", str(repo), "-c", "user.name=c", "-c", "user.email=c@e",
                  "commit", "-q", "-m", "x")
        blob = _self_git("-C", str(repo), "hash-object", "-w", "--stdin",
                         data=b".opencode/plugins\n").stdout.decode().strip()
        _self_git("-C", str(repo), "update-index", "--add", "--cacheinfo",
                  "160000,%s,link" % blob)
        _self_git("-C", str(repo), "-c", "user.name=c", "-c", "user.email=c@e",
                  "commit", "-q", "-m", "link")
        probes = {
            "head": _outcome(lambda: verify_rev(repo, "HEAD")),
            "bogus": _outcome(lambda: verify_rev(repo, "0" * 40))[0],
            "shown": _outcome(lambda: git_show(repo, "HEAD", "a.md"))[0],
            "missing": _outcome(lambda: git_show(repo, "HEAD", "nope.md")),
        }
        return held_in_base(repo, "HEAD", set(tokens)), probes


def _outcome(fn) -> tuple[str, object]:
    """("ok", value) or ("<ExceptionName>", None): a mutation shows up as a value."""
    try:
        return "ok", fn()
    except Exception as e:
        return type(e).__name__, None


def _self_git(*args: str, data: bytes | None = None) -> subprocess.CompletedProcess:
    r = subprocess.run(["git"] + list(args), input=data, capture_output=True)
    if r.returncode != 0:
        raise EnvError("git %s failed: %s"
                       % (args[0], r.stderr.decode(errors="replace").strip()))
    return r


# ----------------------------------------------------------------- self-test

def self_test() -> int:
    global BASE, TARGET, NEW_TARGET, lane_dir, fetch
    assertions = 0
    failures = 0

    def check(name: str, actual: object, expected: object) -> None:
        nonlocal assertions, failures
        assertions += 1
        if actual != expected:
            failures += 1
            print("FAIL %s: got %r, expected %r" % (name, actual, expected))

    # -- the revision guard ----------------------------------------------
    check("a full 40-hex revision is accepted", rev_ok(BASE), True)
    check("an uppercase 40-hex revision is accepted", rev_ok(BASE.upper()), True)
    check("a branch name is not a revision", rev_ok("master"), False)
    check("a 39-hex revision is not", rev_ok("4" * 39), False)
    check("a 41-hex revision is not", rev_ok("4" * 41), False)
    check("a non-hex character makes it not", rev_ok("g" * 40), False)
    check("no revision is not", rev_ok(None), False)
    out, err = io.StringIO(), io.StringIO()
    with contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
        code = main(["--rev", "not-a-hash"])
    check("a non-40-hex --rev exits 2", code, 2)
    check("the usage failure is named, not a traceback",
          ("Traceback" in err.getvalue(), "40-hex" in err.getvalue()), (False, True))

    # -- token well-formedness -------------------------------------------
    check(".claude-plugin/plugin.json is well-formed",
          token_well_formed(".claude-plugin/plugin.json", "Claude Code"), True)
    check(".codex-plugin/plugin.json is well-formed",
          token_well_formed(".codex-plugin/plugin.json", "Codex"), True)
    check(".github/plugin/plugin.json is well-formed",
          token_well_formed(".github/plugin/plugin.json", "Copilot CLI"), True)
    check("v2: gemini-extension.json is well-formed for Gemini CLI (own marker)",
          token_well_formed("gemini-extension.json", "Gemini CLI"), True)
    check("~/.cursor/plugins/plugin.json is well-formed",
          token_well_formed("~/.cursor/plugins/plugin.json", "Cursor"), True)
    check(".claude/agents/ is not (no plugin/extension word)",
          token_well_formed(".claude/agents/", "Claude Code"), False)
    check("package.json is not (no plugin/extension word)",
          token_well_formed("package.json", "VS Code"), False)
    check(".claude-plugin/marketplace.json is not (marketplace segment)",
          token_well_formed(".claude-plugin/marketplace.json", "Claude Code"), False)
    check("a marketplace substring in a segment is not well-formed",
          token_well_formed(".x/my-marketplace-plugin/plugin.json", "Cursor"), False)
    check(".pluginsx/config.json is not (pluginsx is not the word)",
          token_well_formed(".pluginsx/config.json", "Cursor"), False)
    check("plugins/plugin.json is well-formed (no dot directory needed)",
          token_well_formed("plugins/plugin.json", "Cursor"), True)
    check("'' is not well-formed", token_well_formed("", "Cursor"), False)
    check("a space makes it not well-formed",
          token_well_formed(".claude-plugin/plugin .json", "Claude Code"), False)
    check("an empty middle segment is not well-formed (TOKEN_RE alone)",
          token_well_formed(".claude-plugin//plugin.json", "Claude Code"), False)
    check("a character outside the grammar is not well-formed (TOKEN_RE alone)",
          token_well_formed("@x/.claude-plugin/plugin.json", "Claude Code"), False)
    # -- v2 E1: the control's hollow tokens and each new clause ----------
    check("v2: bare plugin.json is not (one segment, no own marker)",
          token_well_formed("plugin.json", "Claude Code"), False)
    check("v2: the nav word Extensions is not (no .json)",
          token_well_formed("Extensions", "Codex"), False)
    check("v2: extension.ts is not (no .json)",
          token_well_formed("extension.ts", "VS Code"), False)
    check("v2: writing-extensions.md is not (no .json)",
          token_well_formed("writing-extensions.md", "Gemini CLI"), False)
    check("v2: plugins is not (no .json)",
          token_well_formed("plugins", "opencode"), False)
    check("v2: .opencode/plugins/ is not (a directory, not a manifest)",
          token_well_formed(".opencode/plugins/", "opencode"), False)
    check("v2: a trailing slash after a .json manifest is not well-formed",
          token_well_formed(".claude-plugin/plugin.json/", "Claude Code"), False)
    check("v2: .JSON in upper case is not .json",
          token_well_formed(".claude-plugin/plugin.JSON", "Claude Code"), False)
    check("v2: the plugin word must sit in the final segment",
          token_well_formed(".claude-plugin/config.json", "Claude Code"), False)
    check("v2: gemini-extension.json is not well-formed for Cursor (no own marker)",
          token_well_formed("gemini-extension.json", "Cursor"), False)
    check("v2: a leading ~/ is not a path segment",
          token_well_formed("~/plugin.json", "Cursor"), False)
    check("v2: a leading ./ is not a path segment",
          token_well_formed("./plugin.json", "Cursor"), False)
    # -- v2 E7: no host or version segment before the file -------------------
    check("v2 E7: Plugins is not well-formed",
          token_well_formed("Plugins", "Claude Code"), False)
    check("v2 E7: Extensions is not well-formed",
          token_well_formed("Extensions", "VS Code"), False)
    check("v2 E7: opencode.ai/docs/plugin.json is not (host segment)",
          token_well_formed("opencode.ai/docs/plugin.json", "opencode"), False)
    check("v2 E7: agent-plugins.org/spec/plugin.json is not (host segment)",
          token_well_formed("agent-plugins.org/spec/plugin.json", "Cursor"), False)
    check("v2 E7: opencode.ai/docs/plugins.json is not (host segment)",
          token_well_formed("opencode.ai/docs/plugins.json", "opencode"), False)
    check("v2 E7: a version segment is not allowed before the file",
          token_well_formed(".cursor/1.0.0/plugin.json", "Cursor"), False)
    check("v2 E7: a dot-led directory is still allowed",
          token_well_formed(".claude-plugin/plugin.json", "Claude Code"), True)
    check("v2 E7: a host segment after ~/ is still a host segment",
          token_well_formed("~/opencode.ai/plugin.json", "opencode"), False)
    check("v2: a one-segment token with the own marker in upper case is well-formed",
          token_well_formed("Gemini-Extension.json", "Gemini CLI"), True)

    # -- normalise: case preserved ---------------------------------------
    check("normalise strips one leading ~/",
          normalise("~/.claude-plugin/plugin.json"), ".claude-plugin/plugin.json")
    check("normalise strips one leading ./",
          normalise("./.opencode/plugins/"), ".opencode/plugins")
    check("normalise strips one trailing /",
          normalise("gemini-extension.json/"), "gemini-extension.json")
    check("normalise strips ONE trailing slash only",
          normalise(".opencode/plugins//"), ".opencode/plugins/")
    check("normalise PRESERVES case",
          normalise(".Claude-Plugin/plugin.json"), ".Claude-Plugin/plugin.json")
    check("normalise of nothing is empty", normalise(None), "")

    # -- the foreign-name guard ------------------------------------------
    check("a .claude token is foreign to VS Code",
          foreign_marker("VS Code", ".claude-plugin/plugin.json"), "Claude Code")
    check("a .claude token is not foreign to Claude Code",
          foreign_marker("Claude Code", ".claude-plugin/plugin.json"), None)
    check("an .opencode token is not foreign to opencode",
          foreign_marker("opencode", ".opencode/plugins/"), None)
    check("a gemini token is not foreign to Gemini CLI",
          foreign_marker("Gemini CLI", "gemini-extension.json"), None)
    check("the marker match is case-insensitive",
          foreign_marker("VS Code", ".Claude-Plugin/plugin.json"), "Claude Code")
    check("a .cursor token is foreign to Gemini CLI",
          foreign_marker("Gemini CLI", ".cursor/plugins/plugin.json"), "Cursor")

    # -- the quote: word bounds, token span, the outside word -------------
    check("v2 E6: quote word count: six words pass",
          MIN_WORDS <= len("one two three four five six".split()) <= MAX_WORDS, True)
    check("v2 E6: quote word count: five words fail",
          MIN_WORDS <= len("one two three four five".split()) <= MAX_WORDS, False)
    check("quote word count: two words fail",
          MIN_WORDS <= len("one two".split()) <= MAX_WORDS, False)
    check("quote word count: 25 words pass",
          len(("w " * 24 + "w").split()) <= MAX_WORDS, True)
    check("quote word count: 26 words fail",
          len(("w " * 25 + "w").split()) <= MAX_WORDS, False)
    check("strip straight quotes", strip_quotes('"hello world"'), "hello world")
    check("strip curly quotes", strip_quotes("\u201chello world\u201d"), "hello world")
    check("keep an unquoted cell", strip_quotes("hello world"), "hello world")
    q = "Claude ships plugins in a .claude-plugin/plugin.json manifest"
    span = token_span(q, ".claude-plugin/plugin.json")
    check("the raw token is found in the quote", span is not None, True)
    check("a plugin word sits outside the token span",
          plugin_word_outside(q, span[0], span[1]), True)
    check("the token span starts where the token starts",
          q[span[0]:span[1]], ".claude-plugin/plugin.json")
    q2 = "the manifest is .claude-plugin/plugin.json"
    span2 = token_span(q2, ".claude-plugin/plugin.json")
    check("only the token carries the plugin word",
          plugin_word_outside(q2, span2[0], span2[1]), False)
    check("the token match is case-sensitive",
          token_span(".Claude-Plugin/plugin.json is used", ".claude-plugin/plugin.json"),
          None)
    check("the normalised form is matched too",
          token_span("see .opencode/plugins here", ".opencode/plugins/"),
          (4, 21))

    # -- the Gate check ---------------------------------------------------
    gate = "## Gate\n\n| row | quote |\n|---|---|\n| S1 | \"the plugin manifest lives here\" |\n"
    gs = gate_section(gate)
    check("gate section is read", ws(gs).count("the plugin manifest lives here"), 1)
    check("quote recorded in the Gate", quote_in_gate(
        "the plugin manifest lives here", ws(gs), ws(gs.replace("`", ""))), True)
    check("quote absent from the Gate", quote_in_gate(
        "the plugin manifest lives elsewhere", ws(gs), ws(gs.replace("`", ""))), False)
    check("an empty Gate records no quote", quote_in_gate(
        "the plugin manifest lives here", ws(""), ws("")), False)
    check("Gate whitespace is normalised", quote_in_gate(
        "the plugin  manifest lives here", ws(gs), ws(gs.replace("`", ""))), True)

    # -- URL normalisation (v1.3, unchanged) ------------------------------
    check("url_key drops a trailing .md",
          url_key("https://code.claude.com/docs/en/plugins.md"),
          url_key("https://code.claude.com/docs/en/plugins"))
    check("url_key drops a trailing slash",
          url_key("https://opencode.ai/docs/plugins/"),
          "//opencode.ai/docs/plugins")
    check("url_key drops a fragment",
          url_key("https://cursor.com/docs/plugins#x"),
          "//cursor.com/docs/plugins")
    check("url_key drops a query",
          url_key("https://cursor.com/docs/plugins?a=1"),
          "//cursor.com/docs/plugins")
    check("url_key lower-cases scheme, host and path",
          url_key("HTTPS://Code.Claude.com/Docs"), "//code.claude.com/docs")
    check("url_key of nothing is empty", url_key(None), "")
    check("a path-case alias is the same URL",
          url_key("https://code.claude.com/docs/en/Plugins"),
          url_key("https://code.claude.com/docs/en/plugins"))
    check("www., scheme and percent-encoding do not make a new URL",
          url_key("http://www.code.claude.com/docs/en/plugins.md/"),
          url_key("https://code.claude.com/docs/en/plugins"))
    check("repeated slashes do not make a new URL",
          url_key("https://code.claude.com//docs///plugins"),
          url_key("https://code.claude.com/docs/plugins"))
    check("an issue URL is a tracker page",
          url_is_tracker("https://github.com/anthropics/claude-code/issues/82902"), True)
    check("a docs page is not a tracker page",
          url_is_tracker("https://cursor.com/docs/plugins.md"), False)

    # -- host pins (v1.3, unchanged) --------------------------------------
    check("pinned host accepted",
          host_ok("https://code.claude.com/docs", HOSTS["Claude Code"]), True)
    check("pinned host/path prefix accepted",
          host_ok("https://github.com/anthropics/claude-code/x",
                  HOSTS["Claude Code"]), True)
    check("sibling host prefix rejected",
          host_ok("https://github.com/anthropics/claude-code-evil/x",
                  HOSTS["Claude Code"]), False)
    check("dot-dot path escape rejected",
          host_ok("https://github.com/anthropics/claude-code/../evil",
                  HOSTS["Claude Code"]), False)
    check("off-host rejected", host_ok("https://example.com/x", HOSTS["Cursor"]), False)
    check("a pinned name as a host-name suffix is rejected",
          host_ok("https://evilcursor.com/x", HOSTS["Cursor"]), False)
    check("subdomain of a pinned host accepted",
          host_ok("https://docs.cursor.com/x", HOSTS["Cursor"]), True)

    # -- duplicate rows and the whole judge -------------------------------
    skill = ("# x\n\n### Plugin manifests by client\n\n"
             "| Client | Plugin manifest | What a plugin can ship | Action |\n"
             "|---|---|---|---|\n"
             "| Claude Code | `.claude-plugin/plugin.json` | commands, agents, hooks "
             "| require it beside the skill file |\n"
             "| Gemini CLI | `gemini-extension.json` | commands, context files "
             "| read it before the skill |\n")
    entry = ("# e\n\n| Client | Manifest | Source | Quote |\n|---|---|---|---|\n"
             '| Claude Code | .claude-plugin/plugin.json | S900 | '
             '"Claude ships plugins in a .claude-plugin/plugin.json manifest" |\n'
             '| Gemini CLI | gemini-extension.json | S901 | '
             '"Gemini extensions use the gemini-extension.json manifest file" |\n')
    src_row = ("| %s | %s docs \u2014 %s | docs | A | the plugin manifest "
               "| \u00a7 plugins | the manifest | mined | %s | 90d "
               "| corpus/knowledge/plugin-manifests-round57.md |\n")
    sources = (src_row % ("S900", "Claude Code",
                          "https://code.claude.com/docs/en/plugins.md", OPENED[0])
               + src_row % ("S901", "Gemini CLI",
                            "https://geminicli.com/docs/extensions.md", OPENED[0]))
    lesson = ("## Gate\n\n| row | URL | quote |\n|---|---|---|\n"
              '| S900 | https://code.claude.com/docs/en/plugins.md | '
              '"Claude ships plugins in a .claude-plugin/plugin.json manifest" |\n'
              '| S901 | https://geminicli.com/docs/extensions.md | '
              '"Gemini extensions use the gemini-extension.json manifest file" |\n')
    base = ("| S001 | Old docs \u2014 https://code.claude.com/docs/en/old.md | docs "
            "| A | s | a | t | mined | 2026-10-01 | 90d | y |\n")

    def backed(sk=skill, en=entry, so=sources, le=lesson, ba=base) -> list[str]:
        return [r["client"] for r in judge(sk, en, so, le, ba) if r["backed"]]

    def why_of(client: str, sk=skill, en=entry, so=sources, le=lesson,
               ba=base) -> list[str]:
        return {r["client"]: r["why"] for r in judge(sk, en, so, le, ba)}[client]

    def k_of(sk=skill) -> int:
        return sum(1 for r in judge(sk, entry, sources, lesson, base) if r["in_k"])

    check("the synthetic world backs both clients",
          backed(), ["Claude Code", "Gemini CLI"])
    check("the synthetic world counts both tokens in K", k_of(), 2)
    check("a duplicate SKILL.md row disqualifies the client",
          backed(sk=skill.replace("| Gemini CLI |",
                                  "| Claude Code | `~/.x/plugins/x.json` | y | z |\n"
                                  "| Gemini CLI |")),
          ["Gemini CLI"])
    check("a second entry row does not disqualify a good one",
          backed(en=entry + '| Gemini CLI | x | S901 | "x y z" |\n'),
          ["Claude Code", "Gemini CLI"])
    check("an S### already at base is not backed",
          backed(ba=base.replace("S001", "S900")), ["Gemini CLI"])
    check("a base URL is not backed",
          backed(ba=base.replace("old.md", "plugins.md")), ["Gemini CLI"])
    check("a base URL reached by a path-case alias is not backed",
          backed(ba=base.replace("old.md", "PLUGINS")), ["Gemini CLI"])
    check("a quote missing from the Gate is not backed",
          backed(le=lesson.replace("manifest file", "manifest doc")), ["Claude Code"])
    check("a two-word action cell is not backed",
          backed(sk=skill.replace("read it before the skill |", "read it |")),
          ["Claude Code"])
    check("a tier B row is not backed",
          backed(so=sources.replace("| docs | A |", "| docs | B |", 1)), ["Gemini CLI"])
    check("a queued row is not backed",
          backed(so=sources.replace("| mined |", "| queued |", 1)), ["Gemini CLI"])
    check("another opened date is not backed",
          backed(so=sources.replace("| mined | 2026-10-23 |", "| mined | 2026-10-22 |", 1)),
          ["Gemini CLI"])
    check("a non-docs kind is not backed",
          backed(so=sources.replace("| docs | A |", "| issue | A |", 1)), ["Gemini CLI"])
    check("an off-host URL is not backed",
          backed(so=sources.replace("https://code.claude.com",
                                    "https://code.claude.com.evil.io", 1)), ["Gemini CLI"])
    check("a tracker URL on a pinned host is not backed",
          backed(so=sources.replace(
              "https://code.claude.com/docs/en/plugins.md",
              "https://github.com/anthropics/claude-code/issues/1", 1)),
          ["Gemini CLI"])
    check("a source cell without a URL is not backed",
          backed(so=sources.replace(
              "https://code.claude.com/docs/en/plugins.md", "no url here", 1)),
          ["Gemini CLI"])
    check("a source cell without a URL is reported as such",
          any("holds no URL" in w for w in why_of("Claude Code", so=sources.replace(
              "https://code.claude.com/docs/en/plugins.md", "no url here", 1))), True)
    check("a malformed manifest token is not backed and leaves K",
          (backed(sk=skill.replace("`gemini-extension.json`", "`package.json`")),
           k_of(skill.replace("`gemini-extension.json`", "`package.json`"))),
          (["Claude Code"], 1))
    check("a marketplace manifest token is not well-formed",
          backed(sk=skill.replace("`.claude-plugin/plugin.json`",
                                  "`.claude-plugin/marketplace.json`")), ["Gemini CLI"])
    check("a manifest cell without a backticked token is not backed",
          backed(sk=skill.replace("`gemini-extension.json`", "gemini-extension.json")),
          ["Claude Code"])
    check("a manifest cell without a backticked token is reported as such",
          any("no backticked token" in w for w in why_of(
              "Gemini CLI", sk=skill.replace("`gemini-extension.json`",
                                             "gemini-extension.json"))), True)
    check("a token carrying another client's marker is not backed",
          backed(sk=skill.replace("`gemini-extension.json`",
                                  "`.claude-plugin/other-plugin.json`"),
                 en=entry.replace("gemini-extension.json",
                                  ".claude-plugin/other-plugin.json"),
                 le=lesson.replace("gemini-extension.json",
                                   ".claude-plugin/other-plugin.json")),
          ["Claude Code"])
    check("a quote without the token is not backed",
          backed(en=entry.replace(
              "Gemini extensions use the gemini-extension.json manifest file",
              "Gemini extensions use a manifest file"),
                 le=lesson.replace(
                     "Gemini extensions use the gemini-extension.json manifest file",
                     "Gemini extensions use a manifest file")), ["Claude Code"])
    check("a quote with only the token's own plugin word is not backed",
          backed(en=entry.replace(
              "Claude ships plugins in a .claude-plugin/plugin.json manifest",
              "Claude stores the manifest at .claude-plugin/plugin.json"),
                 le=lesson.replace(
                     "Claude ships plugins in a .claude-plugin/plugin.json manifest",
                     "Claude stores the manifest at .claude-plugin/plugin.json")),
          ["Gemini CLI"])
    check("a quote whose token differs only in case is not backed",
          backed(en=entry.replace(".claude-plugin/plugin.json",
                                  ".Claude-Plugin/plugin.json"),
                 le=lesson.replace(".claude-plugin/plugin.json",
                                   ".Claude-Plugin/plugin.json")),
          ["Gemini CLI"])
    check("a two-word quote is not backed",
          backed(en=entry.replace(
              "Gemini extensions use the gemini-extension.json manifest file",
              "extensions gemini-extension.json"),
                 le=lesson.replace(
                     "Gemini extensions use the gemini-extension.json manifest file",
                     "extensions gemini-extension.json")), ["Claude Code"])
    check("a 26-word quote is not backed",
          backed(en=entry.replace(
              "Gemini extensions use the gemini-extension.json manifest file",
              " ".join(["extensions"] + ["w"] * 24 + ["gemini-extension.json"])),
                 le=lesson.replace(
                     "Gemini extensions use the gemini-extension.json manifest file",
                     " ".join(["extensions"] + ["w"] * 24
                              + ["gemini-extension.json"]))), ["Claude Code"])
    check("an entry source cell that is not one S### id is not backed",
          backed(en=entry.replace("| S901 |", "| docs |")), ["Claude Code"])
    check("an entry quote cell that is empty is not backed",
          backed(en=entry.replace(
              '"Gemini extensions use the gemini-extension.json manifest file"', '" "')),
          ["Claude Code"])
    check("an S### absent from SOURCES.md is not backed",
          backed(en=entry.replace("S901", "S999")), ["Claude Code"])
    check("a SOURCES row with the wrong cell count is not backed",
          backed(so=sources.replace(
              "| mined | 2026-10-23 | 90d | corpus/knowledge/plugin-manifests-round57.md |\n",
              "| mined | 2026-10-23 | 90d |\n", 1)),
          ["Gemini CLI"])
    check("no entry row for the client is not backed",
          backed(en=entry.replace(
              '| Gemini CLI | gemini-extension.json | S901 | '
              '"Gemini extensions use the gemini-extension.json manifest file" |\n',
              "")), ["Claude Code"])
    # -- v2 E4: the entry Manifest cell is the SKILL.md token ----------------
    check("v2 E4: an entry Manifest cell that differs from SKILL.md is not backed",
          backed(en=entry.replace("| Gemini CLI | gemini-extension.json |",
                                  "| Gemini CLI | .gemini/extension.json |")),
          ["Claude Code"])
    check("v2 E4: the mismatch is reported as such",
          any("Manifest cell" in w for w in why_of("Gemini CLI", en=entry.replace(
              "| Gemini CLI | gemini-extension.json |",
              "| Gemini CLI | .gemini/extension.json |"))), True)
    check("v2 E4: a backticked Manifest cell still backs",
          backed(en=entry.replace("| Gemini CLI | gemini-extension.json |",
                                  "| Gemini CLI | `gemini-extension.json` |")),
          ["Claude Code", "Gemini CLI"])
    check("v2 E4: the normalised form of a ./ token still backs",
          backed(sk=skill.replace("`gemini-extension.json`", "`./gemini-extension.json`")),
          ["Claude Code", "Gemini CLI"])
    check("v2 E4: the raw ./ form in the Manifest cell still backs",
          backed(sk=skill.replace("`gemini-extension.json`", "`./gemini-extension.json`"),
                 en=entry.replace("| Gemini CLI | gemini-extension.json |",
                                  "| Gemini CLI | ./gemini-extension.json |")),
          ["Claude Code", "Gemini CLI"])
    check("v2 E4: a Manifest cell differing only in case is not backed",
          backed(en=entry.replace("| Gemini CLI | gemini-extension.json |",
                                  "| Gemini CLI | Gemini-Extension.json |")),
          ["Claude Code"])
    check("v2 E4: an empty Manifest cell is not backed",
          backed(en=entry.replace("| Gemini CLI | gemini-extension.json |",
                                  "| Gemini CLI |  |")),
          ["Claude Code"])
    check("v2 E4: manifest_cell_matches trims spaces and backticks",
          manifest_cell_matches(" `x/plugin.json` ", "x/plugin.json"), True)
    # -- v2 E5: one token cannot serve two clients ---------------------------
    shared = skill.replace("| Gemini CLI | `gemini-extension.json` |",
                           "| Gemini CLI | `gemini-extension.json` |") + (
        "| Cursor | `gemini-extension.json` | commands | read it before the skill |\n")
    check("v2 E5: a token shared with another client disqualifies both rows",
          [r["client"] for r in judge(shared, entry, sources, lesson, base)
           if "shared by rows" in "; ".join(r["why"])], ["Gemini CLI", "Cursor"])
    check("v2 E5: the sharing disqualifies the otherwise-backed row",
          backed(sk=shared), ["Claude Code"])
    check("v2 E5: sharing is judged on casefold(normalise())",
          backed(sk=skill + "| Codex | `~/.Claude-Plugin/plugin.json/` | x | read it before the skill |\n"),
          ["Gemini CLI"])
    check("v2 E5: a row of an unlisted client name also counts as a user",
          backed(sk=skill + "| Zed | `gemini-extension.json` | x | read it before the skill |\n"),
          ["Claude Code"])
    check("v2 E5: a duplicate row of the SAME client is not a cross-client share",
          shared_tokens(skill_rows(skill + "| Gemini CLI | `gemini-extension.json` | x | y |\n"))
          ["gemini-extension.json"], {"Gemini CLI"})
    check("v2 E5: distinct tokens are not shared",
          sorted(len(v) for v in shared_tokens(skill_rows(skill)).values()), [1, 1])
    # -- v2 E6: six-word quotes ----------------------------------------------
    five = "Gemini extensions use gemini-extension.json manifests"
    check("v2 E6: a five-word quote is not backed",
          backed(en=entry.replace(
              "Gemini extensions use the gemini-extension.json manifest file", five),
                 le=lesson.replace(
                     "Gemini extensions use the gemini-extension.json manifest file", five)),
          ["Claude Code"])
    six = "Gemini extensions use the gemini-extension.json manifest"
    check("v2 E6: a six-word quote backs",
          backed(en=entry.replace(
              "Gemini extensions use the gemini-extension.json manifest file", six),
                 le=lesson.replace(
                     "Gemini extensions use the gemini-extension.json manifest file", six)),
          ["Claude Code", "Gemini CLI"])
    check("v2: a trailing slash after the manifest is not backed",
          backed(sk=skill.replace("`gemini-extension.json`",
                                  "`gemini-extension.json/`")),
          ["Claude Code"])
    check("v2: a bare plugin.json SKILL token is not backed",
          backed(sk=skill.replace("`.claude-plugin/plugin.json`", "`plugin.json`")),
          ["Gemini CLI"])
    check("v2: a changelog URL is not backed",
          backed(so=sources.replace("https://code.claude.com/docs/en/plugins.md",
                                    "https://code.claude.com/docs/en/changelog.md", 1)),
          ["Gemini CLI"])
    check("v2: a change-note URL is reported as such",
          any("changelog/release/news/blog" in w for w in why_of(
              "Claude Code", so=sources.replace(
                  "https://code.claude.com/docs/en/plugins.md",
                  "https://raw.githubusercontent.com/anthropics/claude-code/main/CHANGELOG.md",
                  1))), True)
    check("a ./ prefix still backs",
          backed(sk=skill.replace("`gemini-extension.json`",
                                  "`./gemini-extension.json`")),
          ["Claude Code", "Gemini CLI"])
    check("a wrong SKILL.md header reads no row",
          skill_rows(skill.replace("| Action |", "| Notes |")), [])
    check("a wrong entry header reads no row",
          entry_rows(entry.replace("| Source |", "| Row |")), [])
    check("a table under another heading is not read",
          skill_rows(skill.replace(SKILL_HEADING, "### Other table")), [])

    # -- page normalisation and the found rule ----------------------------
    check("page style and script text is dropped",
          "@layer base" in norm_page(
              "<style>@layer base{}</style><p>x</p><script>@layer base</script>"), False)
    check("page tags are dropped and text kept",
          norm_page("<p>Use <code>/a-b</code> skill</p>"), "use /a-b skill")
    check("quote angle text is kept", norm("$<skill-name> here"), "$<skill-name> here")
    check("page_plain drops `*`, `*` and `_` but keeps case",
          page_plain("A*b_c`D"), "AbcD")
    check("norm lower-cases the quote", norm("Claude Ships"), "claude ships")
    page_ok = ("<p>Claude ships plugins in a "
               "<code>.claude-plugin/plugin.json</code> manifest</p>")
    check("found: quote and token both on the page",
          found_on_page(page_ok,
                        "Claude ships plugins in a .claude-plugin/plugin.json manifest",
                        ".claude-plugin/plugin.json"), True)
    check("found: quote absent from the page",
          found_on_page(page_ok, "Claude ships plugins in a manifest",
                        ".claude-plugin/plugin.json"), False)
    check("found: token only inside a URL is rejected",
          found_on_page("<p>the plugin lives at "
                        "https://example.com/.claude-plugin/plugin.json</p>",
                        "the plugin lives at", ".claude-plugin/plugin.json"), False)
    check("found: token after a space is accepted",
          found_on_page("<p>the plugin lives at .claude-plugin/plugin.json today</p>",
                        "the plugin lives at", ".claude-plugin/plugin.json"), True)
    check("found: a tilde token is found on the page",
          found_on_page("<p>the plugins live in ~/.claude-plugin/plugin.json today</p>",
                        "the plugins live in ~/.claude-plugin/plugin.json",
                        "~/.claude-plugin/plugin.json"), True)
    check("found: a token case difference is rejected",
          found_on_page("<p>the plugin lives at .Claude-Plugin/plugin.json</p>",
                        "the plugin lives at", ".claude-plugin/plugin.json"), False)
    check("found: no token is never found",
          found_on_page(page_ok, "Claude ships plugins in a .claude-plugin/plugin.json "
                                 "manifest", None), False)
    check("boundary: at the start of the text is accepted",
          token_at_boundary(".claude-plugin/plugin.json", ".claude-plugin/plugin.json"),
          True)
    check("boundary: after a letter is rejected",
          token_at_boundary("x.claude-plugin/plugin.json", ".claude-plugin/plugin.json"),
          False)
    check("boundary: after a digit is rejected",
          token_at_boundary("1.claude-plugin/plugin.json", ".claude-plugin/plugin.json"),
          False)
    check("boundary: after a dot is rejected",
          token_at_boundary("a.claude-plugin/plugin.json", ".claude-plugin/plugin.json"),
          False)
    check("boundary: after a slash is rejected",
          token_at_boundary("/.claude-plugin/plugin.json", ".claude-plugin/plugin.json"),
          False)
    check("boundary: after a hyphen is rejected",
          token_at_boundary("-.claude-plugin/plugin.json", ".claude-plugin/plugin.json"),
          False)
    check("boundary: after a comma is rejected",
          token_at_boundary(",.claude-plugin/plugin.json", ".claude-plugin/plugin.json"),
          False)
    check("boundary: after a backtick is accepted",
          token_at_boundary("`.claude-plugin/plugin.json`", ".claude-plugin/plugin.json"),
          True)
    check("boundary: after a quote is accepted",
          token_at_boundary('".claude-plugin/plugin.json"', ".claude-plugin/plugin.json"),
          True)
    check("boundary: after a parenthesis is accepted",
          token_at_boundary("(.claude-plugin/plugin.json)", ".claude-plugin/plugin.json"),
          True)
    check("boundary: after a bracket is accepted",
          token_at_boundary("[.claude-plugin/plugin.json]", ".claude-plugin/plugin.json"),
          True)
    check("boundary: a singular token inside the plural is not found",
          token_at_boundary("put files in .opencode/plugins/ now", ".opencode/plugin"),
          False)
    check("boundary: the token followed by a slash is found",
          token_at_boundary("put files in .opencode/plugin/x.json now", ".opencode/plugin"),
          True)
    check("boundary: the token followed by a hyphen is not found",
          token_at_boundary(".opencode/plugin-x", ".opencode/plugin"), False)
    check("boundary: the token followed by an underscore is not found",
          token_at_boundary(".opencode/plugin_x", ".opencode/plugin"), False)

    # -- held occurrences: case and segment bounds ------------------------
    tok = ".claude-plugin/plugin.json"
    check("held: an exact line holds it", held_in_text(tok, tok), True)
    check("held: text after a space holds it", held_in_text("see " + tok, tok), True)
    check("held: a tab before it holds it", held_in_text("\t" + tok, tok), True)
    check("held: a backtick before it holds it", held_in_text("`" + tok + "`", tok), True)
    check("held: a double quote before it holds it", held_in_text('"' + tok, tok), True)
    check("held: a single quote before it holds it", held_in_text("'" + tok, tok), True)
    check("held: a paren before it holds it", held_in_text("(" + tok, tok), True)
    check("held: a bracket before it holds it", held_in_text("[" + tok, tok), True)
    check("held: an angle bracket before it holds it", held_in_text("<" + tok, tok), True)
    check("held: a slash before it holds it", held_in_text("x/" + tok, tok), True)
    check("held: a tilde before it holds it", held_in_text("~/" + tok, tok), True)
    check("held: an equals sign before it holds it", held_in_text("=" + tok, tok), True)
    check("held: a new line start holds it", held_in_text("x\n" + tok, tok), True)
    check("held: a letter before it does not hold it",
          held_in_text("my.claude-plugin/plugin.json", tok), False)
    check("held: a dot-joined prefix does not hold it",
          held_in_text("my." + tok, tok), False)
    check("held: a directory prefix with a slash does hold it",
          held_in_text("x/" + tok, tok), True)
    check("v2: a CASE difference holds it (.Claude-Plugin vs held lowercase)",
          held_in_text(".Claude-Plugin/plugin.json", tok), True)
    check("v2: an upper-case token is held by lowercase base text",
          held_in_text("see .claude-plugin/plugin.json", ".Claude-Plugin/plugin.json"), True)
    check("v2: Extensions is held by base text extensions",
          held_in_text("the extensions directory", "Extensions"), True)
    check("v2: the case-insensitive match keeps the segment boundary",
          held_in_text("my.Claude-Plugin/plugin.json", tok), False)
    check("held: the round-56 memory-file analogue does not hold it",
          held_in_text(".claude/AGENTS.md", ".claude/agents"), False)
    check("held: a .md suffix does not hold the bare token",
          held_in_text(".claude/agents.md", ".claude/agents"), False)
    check("held: a letter suffix does not hold it",
          held_in_text(tok + "x", tok), False)
    check("held: a digit suffix does not hold it",
          held_in_text(tok + "1", tok), False)
    check("held: a hyphen suffix does not hold it",
          held_in_text(tok + "-x", tok), False)
    check("held: an underscore suffix does not hold it",
          held_in_text(tok + "_x", tok), False)
    check("held: a dot before a letter does not hold it",
          held_in_text(tok + ".5", tok), False)
    check("held: a trailing dot does hold it", held_in_text(tok + ".", tok), True)
    check("held: a slash suffix does hold it", held_in_text(tok + "/", tok), True)
    check("held: an empty token is never held", held_in_text(tok, ""), False)

    # -- the base-tree scan (hermetic temp repository) --------------------
    try:
        held, probes = held_world()
    except Exception as e:  # git missing or a failed init: every arm below fails
        held, probes = {"error": str(e)}, {"error": str(e)}
    check("held occurrences over a temp base tree", held, {
        ".claude-plugin/plugin.json": False,
        "gemini-extension.json": True,
        ".cursor/plugins": True,
        ".copilot-plugin/plugin.json": False,
        ".opencode/plugins": False})
    check("verify_rev accepts a real commit", probes.get("head"), ("ok", None))
    check("verify_rev rejects an unknown revision", probes.get("bogus"), "EnvError")
    check("git_show reads a tracked file", probes.get("shown"), "ok")
    check("git_show returns None for a missing path", probes.get("missing"),
          ("ok", None))
    check("cat-file headers of missing objects are skipped",
          parse_batch(b"abc missing\n"), [])
    check("cat-file blobs are read by their declared size",
          parse_batch(b"abc blob 3\nabc\n"), [b"abc"])
    check("cat-file non-blob records are skipped",
          parse_batch(b"abc commit 3\nabc\n"), [])
    check("cat-file records are read in order",
          parse_batch(b"a blob 1\nx\nb missing\nc blob 2\nyz\n"), [b"x", b"yz"])

    # -- the output lines and the predicate ------------------------------
    check("fetch summary line", summary_line(True, 0, 0, 0, 0),
          "plugin manifests found on the live page 0 of 0; new ground 0")
    check("non-fetch summary line", summary_line(False, 0, 0, 0, 0),
          "plugin manifests backed 0 of 0; new ground not computed (needs --fetch)")
    check("reject line", reject_line("Cursor", ["a", "b"]), "reject Cursor: a; b")
    check("predicate: fetch, 5 of 7, ground 3, passes", predicate(True, 5, 3), 0)
    check("predicate: fetch, 4 of 7, ground 3, fails", predicate(True, 4, 3), 1)
    check("predicate: fetch, 5 of 7, ground 2, fails", predicate(True, 5, 2), 1)
    check("predicate: no fetch always fails", predicate(False, 7, 7), 1)
    check("ground: two spellings of one token count once",
          new_ground([".Claude-Plugin/plugin.json", ".claude-plugin/plugin.json"], {}), 1)
    check("ground: a held spelling drops its own key",
          new_ground([".Claude-Plugin/plugin.json", ".claude-plugin/plugin.json"],
                     {".claude-plugin/plugin.json": True,
                      ".Claude-Plugin/plugin.json": True}), 0)
    check("v2: the control's ground world (Extensions held as extensions) is 3, not 4",
          new_ground(["plugin.json", "Extensions", "extension.ts",
                      "writing-extensions.md", "plugins"],
                     {t: held_in_text("x extensions plugins y", t)
                      for t in ["plugin.json", "Extensions", "extension.ts",
                                "writing-extensions.md", "plugins"]}), 3)
    check("v2: url_is_change_note on each word",
          [url_is_change_note("https://x.com/a/%s/b" % w) for w in CHANGE_NOTE_WORDS],
          [True] * len(CHANGE_NOTE_WORDS))
    check("v2: url_is_change_note is case-insensitive and percent-decoded",
          (url_is_change_note("https://x.com/CHANGELOG.md"),
           url_is_change_note("https://x.com/%62log/x")), (True, True))
    check("v2: a docs URL is not a change note",
          url_is_change_note("https://code.claude.com/docs/en/plugins-reference"), False)
    check("v2: a change-note word only in the query is not the path",
          url_is_change_note("https://cursor.com/docs/plugins?from=blog"), False)
    check("ground: two different tokens count twice",
          new_ground(["gemini-extension.json", ".opencode/plugins"], {}), 2)
    check("ground: a held token is not new ground",
          new_ground(["gemini-extension.json"], {"gemini-extension.json": True}), 0)
    check("ground: nothing found is zero", new_ground([], {}), 0)

    # -- round-57 spot-check R4: a SUCCESSFUL end-to-end main() path -------
    skill = ("# x\n\n### Plugin manifests by client\n\n"
             "| Client | Plugin manifest | What a plugin can ship | Action |\n"
             "|---|---|---|---|\n"
             "| Claude Code | `.claude-plugin/plugin.json` | hooks and agents "
             "| read the manifest first |\n"
             "| Gemini CLI | `gemini-extension.json` | commands and prompts "
             "| read the extension file |\n")
    entry = ("# e\n\n| Client | Manifest | Source | Quote |\n|---|---|---|---|\n"
             "| Claude Code | `.claude-plugin/plugin.json` | `S089` | "
             '"Installing plugins from the `.claude-plugin/plugin.json` manifest" |\n'
             "| Gemini CLI | `gemini-extension.json` | `S093` | "
             '"The gemini-extension.json file declares an extension" |\n')
    src_row = ("| %s | %s docs \u2014 %s | docs | A | the plugin manifest "
               "| \u00a7 manifest | the manifest file | mined | %s | 90d "
               "| corpus/knowledge/plugin-manifests-round57.md |\n")
    sources = (src_row % ("S089", "Claude Code",
                          "https://code.claude.com/docs/en/plugins-reference",
                          OPENED[0])
               + src_row % ("S093", "Gemini CLI",
                            "https://geminicli.com/docs/extensions/", OPENED[0]))
    lesson = ("## Gate\n\n| row | URL | quote |\n|---|---|---|\n"
              "| S089 | https://code.claude.com/docs/en/plugins-reference | "
              '"Installing plugins from the `.claude-plugin/plugin.json` manifest" |\n'
              "| S093 | https://geminicli.com/docs/extensions/ | "
              '"The gemini-extension.json file declares an extension" |\n')
    with tempfile.TemporaryDirectory(prefix="cmp-main-") as td:
        repo = Path(td)
        (repo / "corpus" / "knowledge").mkdir(parents=True)
        (repo / "corpus" / "lessons").mkdir(parents=True)
        (repo / "corpus" / "SOURCES.md").write_text(
            "| id | source | kind | tier | scope | anchor | teaches | status "
            "| opened | recheck | used-by |\n", encoding="utf-8")
        _self_git("init", "-q", str(repo))
        _self_git("-C", str(repo), "add", "-A", "-f", ".")
        _self_git("-C", str(repo), "-c", "user.name=c", "-c", "user.email=c@e",
                  "commit", "-q", "-m", "base")
        base_sha = _self_git("-C", str(repo), "rev-parse",
                             "HEAD").stdout.decode().strip()
        (repo / "SKILL.md").write_text(skill, encoding="utf-8")
        (repo / "corpus" / "knowledge" / "plugin-manifests-round57.md").write_text(
            entry, encoding="utf-8")
        (repo / "corpus" / "SOURCES.md").write_text(sources, encoding="utf-8")
        (repo / "corpus" / "lessons" / "round-57.md").write_text(
            lesson, encoding="utf-8")
        _self_git("-C", str(repo), "add", "-A", "-f", ".")
        _self_git("-C", str(repo), "-c", "user.name=c", "-c", "user.email=c@e",
                  "commit", "-q", "-m", "measured")
        measured = _self_git("-C", str(repo), "rev-parse",
                             "HEAD").stdout.decode().strip()
        page = ("<p>Installing plugins from the <code>.claude-plugin/plugin.json"
                "</code> manifest</p><p>The gemini-extension.json file declares "
                "an extension.</p>")
        saved = (BASE, TARGET, NEW_TARGET, lane_dir, fetch)
        try:
            BASE, TARGET, NEW_TARGET = base_sha, 2, 2
            lane_dir = lambda: repo
            fetch = lambda url, pins=None, base_keys=None: page
            out = io.StringIO()
            with contextlib.redirect_stdout(out):
                code = main(["--rev", measured, "--fetch"])
            lines = out.getvalue().splitlines()
            check("R4: the satisfying world exits 0", code, 0)
            check("R4: the exact found line is printed",
                  "plugin manifests found on the live page 2 of 2; new ground 2"
                  in lines, True)
            (repo / "corpus" / "lessons" / "round-57.md").write_text(
                lesson.replace("Installing plugins from", "Installing plugin from"),
                encoding="utf-8")
            _self_git("-C", str(repo), "add", "-A", "-f", ".")
            _self_git("-C", str(repo), "-c", "user.name=c", "-c", "user.email=c@e",
                      "commit", "-q", "-m", "broken")
            broken = _self_git("-C", str(repo), "rev-parse",
                               "HEAD").stdout.decode().strip()
            out = io.StringIO()
            with contextlib.redirect_stdout(out):
                code = main(["--rev", broken, "--fetch"])
            lines = out.getvalue().splitlines()
            check("R4: the broken world exits 1", code, 1)
            check("R4: the broken world prints the one-of-two line",
                  "plugin manifests found on the live page 1 of 2; new ground 1"
                  in lines, True)
        finally:
            BASE, TARGET, NEW_TARGET, lane_dir, fetch = saved

    # -- the counter's own sha256 ----------------------------------------
    own = Path(__file__).read_bytes()
    check("the own sha256 is 64 hex", len(self_sha()), 64)
    check("the own sha256 is the sha256 of this file",
          self_sha(), hashlib.sha256(own).hexdigest())

    print("self-test: %d failure(s) over %d assertions" % (failures, assertions))
    return 1 if failures else 0


# ---------------------------------------------------------------------- main

def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--rev")
    ap.add_argument("--fetch", action="store_true")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--self-test", action="store_true")
    args = ap.parse_args(argv)
    try:
        print("counter sha256 %s" % self_sha())
    except OSError as e:
        print("could-not-evaluate: cannot read own bytes: %s" % e, file=sys.stderr)
        return 2
    if args.self_test:
        if args.rev or args.fetch or args.json:
            ap.error("--self-test cannot be combined with --rev, --fetch or --json")
        return self_test()
    if not args.rev:
        ap.error("--rev is required")
    if not rev_ok(args.rev):
        print("could-not-evaluate: --rev %r is not a full 40-hex commit hash"
              % args.rev, file=sys.stderr)
        return 2
    try:
        lane = lane_dir()
        verify_rev(lane, args.rev)
        skill = git_show(lane, args.rev, SKILL) or ""
        entry = git_show(lane, args.rev, ENTRY) or ""
        sources = git_show(lane, args.rev, SOURCES) or ""
        lesson = git_show(lane, args.rev, LESSON) or ""
        base_sources = git_show(lane, BASE, SOURCES) or ""
    except (EnvError, UnicodeDecodeError, OSError) as e:
        print("could-not-evaluate: %s" % e, file=sys.stderr)
        return 2
    print("counter rev %s" % args.rev)
    report = judge(skill, entry, sources, lesson, base_sources)
    backed = [r for r in report if r["backed"]]
    k = sum(1 for r in report if r["in_k"])
    found = 0
    if args.fetch:
        for r in backed:
            try:
                r["found"] = found_on_page(fetch(r["url"], HOSTS[r["client"]],
                                                 base_url_keys(base_sources)),
                                           r["quote"], r["token"])
            except Exception as e:  # network or decode failure: not found
                r["found"] = False
                r["fetch_error"] = str(e)
            found += 1 if r["found"] else 0
    counted = [r for r in backed if r.get("found")] if args.fetch else []
    ground = 0
    if args.fetch:
        tokens = {r["norm"] for r in counted if r["norm"]}
        try:
            held = held_in_base(lane, BASE, tokens)
        except (EnvError, UnicodeDecodeError, OSError) as e:
            print("could-not-evaluate: %s" % e, file=sys.stderr)
            return 2
        for r in counted:
            r["held"] = held.get(r["norm"], False)
        ground = new_ground([r["norm"] for r in counted], held)
    if args.json:
        print(json.dumps({"backed": len(backed), "of": k, "found": found,
                          "new_ground": ground, "target": TARGET,
                          "new_target": NEW_TARGET, "clients": report}, indent=1))
    else:
        print(summary_line(args.fetch, len(backed), k, found, ground))
        for r in report:
            if not r["backed"]:
                print(reject_line(r["client"], r["why"]))
                continue
            detail = "token=%s norm=%s" % (r["token"], r["norm"])
            if args.fetch:
                detail += " found=%s" % ("yes" if r.get("found") else "no")
                if r.get("found"):
                    detail += " held-at-base=%s" % ("yes" if r.get("held") else "no")
            print("%-12s %-6s %s" % (r["client"], "BACKED", detail))
    return predicate(args.fetch, found, ground)


if __name__ == "__main__":
    sys.exit(main())
