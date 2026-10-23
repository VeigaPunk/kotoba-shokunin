#!/usr/bin/env python3
r"""check_hook_files.py -- frozen counter for the round-59 C1 claim.

Derived from `check_command_files.py` (round 58, sha256 `aae12d36...`: E3, E4,
E5, E6, E7, the HOSTS map, the foreign-name markers, the SOURCES row parsing,
the URL normalisation, the tracker and change-note rejection, the `## Gate`
quote requirement, the held-occurrence scan and the fetch limits).  Every
round-58 rule kept here is kept as it was, and everything named below is the
round-59 change.  Each named change only adds or replaces one rule; none
loosens a round-58 rule that still applies.

Round 59, claim C1 (axis: depth, the learning claim; sourced): `SKILL.md`
gains a decision table, `### Hook files by client`, that tells a reader, per
client, the file or folder its own documentation names for HOOK configuration
(commands or code the client runs automatically on a lifecycle event such as
before or after a tool call), the events a hook can fire on, and what a skill
or rule author does with it -- move a rule that must hold every time out of
the prompt.  Each row is grounded in a new knowledge entry,
`corpus/knowledge/hook-files-round59.md`, whose per-client record quotes the
client's own documentation from a `corpus/SOURCES.md` row opened on
2026-10-23, and whose quote the client's own committed page snapshot carries.

This counter is frozen before any round-59 C1 content exists.  The seven
clients, the hosts allowed for each client's source, the table anchors, the
token grammar, the events rule, the foreign-name markers, the word bounds, the
opened date, the base revision and the targets are pinned here and never read
from the revision measured.  A later change to any of them is a second
measurement, never the declared one (corpus/QUALITY.md Q28).  Round 58 froze
`None` targets, counted the population in a W0 census, and the L1 set TARGET
and NEW_TARGET at freeze; round 59 does the same, so `TARGET` and
`NEW_TARGET` ship as `None` and the predicate returns 1 until the L1 sets
both (never 0, and the output is still printed).

THE FROZEN SPEC (this file implements it; it is not read from the tree):

  BASE_REV = a975cbbf00534443c49bf02e29c813a3db0bf0f8
  CLIENTS  = Claude Code, Codex, VS Code, Copilot CLI, Gemini CLI, Cursor, opencode
  HOSTS    = the round-58 pinned map, unchanged: Claude Code code.claude.com,
             docs.claude.com, docs.anthropic.com, platform.claude.com,
             github.com/anthropics/claude-code; Codex developers.openai.com,
             learn.chatgpt.com, github.com/openai/codex; VS Code
             code.visualstudio.com, github.com/microsoft/vscode,
             github.com/microsoft/vscode-docs; Copilot CLI docs.github.com,
             github.com/github/copilot-cli; Gemini CLI geminicli.com,
             github.com/google-gemini/gemini-cli; Cursor cursor.com,
             docs.cursor.com; opencode opencode.ai, github.com/sst/opencode,
             github.com/anomalyco/opencode; raw.githubusercontent.com mirrors of
             those repos allowed
  TARGET, NEW_TARGET = None, None (the L1 sets both at freeze)
  OPENED   = 2026-10-23

  SKILL.md at the measured revision: a section whose heading line is exactly
  `### Hook files by client`; its FIRST table has the header
  `| Client | Hook config | Events | Action |`.  One row per client name
  (exact match to CLIENTS; a duplicate client row disqualifies that client).
  The hook token is the FIRST backticked span of the Hook config cell.  The
  Events cell carries the event names as backticked spans.  The action cell
  must hold at least three words.

  THE C1 ROW RULE (fixed in `plans/round-59.md` § C1 before the census): a
  client counts when its OWN documentation, on its pinned host, names a file
  or folder that holds HOOK configuration (commands or code the client runs
  automatically on a lifecycle event such as before or after a tool call or at
  session start), as a token that -- after stripping one leading `~/` or `./`
  -- has >= 2 path segments and a first segment starting with `.`; no segment
  (split on `-`, `.`, `_`) equal (case-insensitive) to skill/skills/agent/
  agents/command/commands/prompt/prompts/rule/rules/plugin/plugins/extension/
  extensions; no dot inside a non-final segment except as its first character
  (E7); no OTHER client's marker in the token; and not the same token another
  client's row would lead with (E5 disqualifies both rows).  A 6-25-word
  verbatim quote from that page must contain the token, case-sensitively, at
  path-segment boundaries, and the word hook or hooks outside the token span.
  The same page (or the client's own hooks page) must print at least 2
  distinct event names as identifiers.

  A token is well-formed (that grammar, spelled out) iff it matches
  `^(~/|\./)?[A-Za-z0-9_.-]+(/[A-Za-z0-9_.*-]+)*/?$`
  AND, after stripping one leading `~/` or `./` and one trailing `/`, it has at
  least two path segments and its first segment starts with `.`
  AND no segment, split on `-`, `.` and `_`, holds a word EQUAL
  case-insensitively to one of `skill`, `skills`, `agent`, `agents`,
  `command`, `commands`, `prompt`, `prompts`, `rule`, `rules`, `plugin`,
  `plugins`, `extension`, `extensions` -- in ANY segment, the final one
  included (round 58 required a command/prompt word in the final segment and
  banned these words only elsewhere; round 59 drops that requirement, because
  a hook file is named by the client, not by a command/prompt word, and keeps
  the ban on every segment)
  AND (E7) no non-final segment holds a dot other than as its first character
  AND a directory token (a trailing `/`) IS allowed, and a glob `*` is allowed
  in the final segment.

    well-formed:  .claude/settings.json, .github/hooks/, .codex/config.toml,
                  .cursor/hooks.json, .gemini/hooks/, .opencode/config.json,
                  ~/.claude/settings.json, .github/hooks/*.json
    not:          hooks, .hooks, /hooks, ./hooks, .claude (one segment),
                  claude/settings.json (first segment not dot-led),
                  .claude/skills/hooks.json, .claude/command/hooks.json,
                  .claude/skills.json (a banned word in the final segment),
                  .claude-plugin/hooks.json, .vscode/extensions/hooks.json,
                  .claude/1.0/hooks.json (E7), .claude.local/hooks.json (E7),
                  opencode.ai/docs/hooks/ (first segment not dot-led)

  FOREIGN-NAME GUARD (kept): the client markers are Claude Code `claude`,
  Codex `codex`, VS Code `vscode`, Copilot CLI `copilot`, Gemini CLI `gemini`,
  Cursor `cursor`, opencode `opencode`.  A token whose lower-cased text
  contains ANOTHER client's marker is rejected for that client.

  normalise(token) = strip one leading `~/` or `./`, strip one trailing `/`;
  case is PRESERVED.
  K = the number of client rows with a well-formed token.

  EVENTS CELL (round-58 routed defect R3, the field check): the backticked
  spans of the SKILL.md Events cell, in order, with a repeated span counted
  once.  A row passes this check iff it holds at least 2 distinct spans and
  EVERY span matches `^[A-Za-z][A-Za-z0-9_.:-]*$`.  A span is FOUND on a page
  iff it occurs there CASE-SENSITIVELY with the previous and the next
  character outside `[A-Za-z0-9_]` (so `PreToolUse` is not found inside
  `PreToolUseHook`, and `_` is never a boundary).  The comparison runs on
  `event_text(page)`: script/style bodies, HTML comments and tags dropped,
  entities decoded, the Markdown markers `*` and `` ` `` dropped (no event
  name may contain them), whitespace collapsed, case and `_` KEPT.

  Entry `corpus/knowledge/hook-files-round59.md` at the measured revision:
  its first table with the header `| Client | Hook config | Source | Quote |`.
  The source cell holds one `S###` id; the quote cell holds the verbatim quote
  (one pair of surrounding straight or curly double quotes is stripped;
  backticks are stripped for word counting and for matching).

  SNAPSHOT (round-58 routed defect R3, the reader check).  `.ufo/waves/
  round-59/snapshots/<S###>.page` must exist at the measured revision, read
  with `git show <rev>:<path>` as bytes (never from the working tree); its
  sha256 must equal the FIRST `sha256 <64 hex>` printed anywhere in that
  source's SOURCES row (a row printing no full 64-hex sha256 blocks the row:
  an ellipsis digest is not a pin); and the snapshot's text must carry the
  quote, the token and every Events span, under the same rules the live page
  is held to.

  A client is BACKED iff all of:
    * its SKILL.md row is unique and its token well-formed, and its action cell
      holds >= 3 words;
    * its Events cell passes the events check above;
    * the token is not foreign to the client (FOREIGN-NAME GUARD);
    * (E5) no SKILL.md row of another client name uses the same
      casefold(normalise(token));
    * an entry row names it, and (E4) its `Hook config` cell, backticks
      stripped, equals the token or normalise(token);
    * the quote holds 6 (E6) to 25 words;
    * the quote CONTAINS the raw token or its normalise()d form,
      CASE-SENSITIVE, at path-segment boundaries;
    * the quote matches `(?i)\bhooks?\b` OUTSIDE that token's span -- the word
      hook/hooks inside the token does not count, and a `\b` word boundary is
      required, so `hooky` is not `hook` (round 58 asked for command/prompt);
    * the cited `S###` is a row of `corpus/SOURCES.md` at the measured
      revision, its id is NOT a row at BASE_REV, and its URL -- normalised by
      lowercasing scheme and host, percent-decoding and lowercasing the path,
      collapsing repeated slashes, stripping a trailing `/`, stripping a
      trailing `.md`, stripping `#fragment` and `?query` (round-56 v1.3
      `url_key`) -- is not the normalised URL of any BASE_REV row;
    * that row has kind `docs`, tier `A`, status `mined`, and opened
      `2026-10-23`;
    * the row's URL host is pinned for that client (host_ok);
    * (E3) the row's URL path, percent-decoded, contains none of `changelog`,
      `release`, `releases`, `news`, `blog` (case-insensitive);
    * the quote, whitespace-normalised, occurs in `corpus/lessons/round-59.md`
      section `## Gate` at the measured revision;
    * the SNAPSHOT check above passes.

  With `--fetch`, a BACKED client is FOUND iff the live page at the row URL
  carries the quote, the token and every Events span.  The page is read with
  `curl -sSL --max-time 30 -A <browser UA> -H "Accept: text/markdown,
  text/plain;q=0.9, */*;q=0.8" -w "\n%{http_code} %{url_effective}"`, up to 3
  attempts, with HTTP 200 required; the header set is part of the rule
  (round-58 routed defect R3: a served page and its `.md` route differ, and a
  bot User-Agent can be answered differently).  The URL reached after
  redirects must still be on the client's pinned hosts, must not be a BASE_REV
  SOURCES URL, must not be an E3 change-note URL, and the body must stay under
  5 MiB.  The quote and the token use the round-58 page normalisation (quote
  side lower-cased and tag-stripped; the token CASE-SENSITIVE on a
  case-preserving rendering, at a boundary that rejects a following digit,
  letter, `_` or `-`); the events use `event_text`.

  NEW GROUND G = the number of DISTINCT casefold(normalise(token)) values among
  the FOUND clients that have ZERO held occurrences in the BASE_REV tree
  outside `.ufo/`, where a held occurrence is a CASE-INSENSITIVE match of the
  normalised token at a path-segment boundary, read on the casefolded line: the
  preceding character is the start of a line, whitespace, a backtick, a quote
  character, `(`, `[`, `<`, `/`, `~` or `=`; the following character is the end
  of the line, or is not a letter, a digit, `_` or `-` and is not a `.` followed
  by a letter or a digit.  The two spellings `.Claude/Settings.json` and
  `.claude/settings.json` on two found clients count ONCE, and a base that
  holds either spelling holds both.  Blobs are read with `git ls-tree -r -z` +
  `git cat-file --batch`; a blob holding a NUL byte is skipped as binary, and
  paths under `.ufo/` are never read.  G is computed over FOUND rows, so
  without `--fetch` G is 0, never the number of backed rows.

  Output: the FIRST line is the summary
  `hook files backed on committed snapshots S of K; found on the live page
  F of K; new ground G` with `--fetch`, and
  `hook files backed on committed snapshots S of K; live not run; new ground 0`
  without it (F = 0, G = 0).  The SECOND line is
  `counter sha256 <hex>; rev <rev>`, the sha256 of this file's own bytes read
  from `__file__` (never from a pipe).  Then one `reject <client>: <reasons>`
  line per non-found row: without `--fetch` a row is non-found when it is not
  backed; with `--fetch` a row is non-found when it is not backed or its live
  page failed, and the reasons then include the live failure.  A `targets not
  frozen` line follows the rejects while TARGET or NEW_TARGET is `None`.

  Exit codes: with frozen targets and `--fetch`, 0 iff F >= TARGET AND G >=
  NEW_TARGET, else 1; without `--fetch`, always 1 (the non-fetch run is not the
  predicate); with TARGET or NEW_TARGET `None`, always 1 (never 0, and the
  output is still printed); 2 = could not evaluate (a `--rev` that is not a
  full 40-hex hash, a revision that is not a commit, a git failure, a SKILL.md
  missing at the revision, an unreadable file) with no traceback.

THE FROZEN PREDICATE (verbatim, and the receipt label):

  `python3 -B verifiers/check_hook_files.py --rev <rev> --fetch` exits 0
  iff it prints `hook files backed on committed snapshots S of K; found on the
  live page F of K; new ground G` with F >= TARGET and G >= NEW_TARGET;
  receipt label `C1 predicate: --fetch exit 0 (F>=TARGET, G>=NEW_TARGET)`.

The counter reads the measured revision with read-only git (`git -C <lane>
show <rev>:<path>`, `git -C <lane> ls-tree`, `git -C <lane> cat-file`), never
from the working tree; the lane is the parent of the script's `verifiers/`
directory.

Usage:
  python3 -B verifiers/check_hook_files.py --rev <rev> [--fetch] [--json]
  python3 -B verifiers/check_hook_files.py --self-test
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
from pathlib import Path

BASE = "a975cbbf00534443c49bf02e29c813a3db0bf0f8"
SKILL = "SKILL.md"
ENTRY = "corpus/knowledge/hook-files-round59.md"
SOURCES = "corpus/SOURCES.md"
LESSON = "corpus/lessons/round-59.md"
SNAPSHOT_DIR = ".ufo/waves/round-59/snapshots"
TARGET = None
NEW_TARGET = None
MIN_WORDS = 6
MAX_WORDS = 25
OPENED = ("2026-10-23",)
MAX_BYTES = 5 * 1024 * 1024
FETCH_TIMEOUT = 30
FETCH_ATTEMPTS = 3
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
SKILL_HEADING = "### Hook files by client"
SKILL_HEADER = ("client", "hook config", "events", "action")
ENTRY_HEADER = ("client", "hook config", "source", "quote")
REV_RE = re.compile(r"^[0-9a-fA-F]{40}$")
TOKEN_RE = re.compile(r"^(~/|\./)?[A-Za-z0-9_.-]+(/[A-Za-z0-9_.*-]+)*/?$")
SEG_SPLIT_RE = re.compile(r"[-._]")
NOT_HOOK_WORDS = frozenset(("skill", "skills", "agent", "agents", "command",
                            "commands", "prompt", "prompts", "rule", "rules",
                            "plugin", "plugins", "extension", "extensions"))
BACKTICK_RE = re.compile(r"`([^`]+)`")
SID_RE = re.compile(r"^`?(S\d{3,})`?$")
URL_RE = re.compile(r"https?://[^\s)>\]`]+")
SOURCES_ROW_RE = re.compile(r"^\|[ \t]*S[0-9]{3,}[ \t]*\|")
HOOK_WORD_RE = re.compile(r"\bhooks?\b", re.IGNORECASE)
SHA256_RE = re.compile(r"sha256[\s`*:=\[]*([0-9a-fA-F]{64})(?![0-9a-fA-F])")
EVENT_RE = re.compile(r"^[A-Za-z][A-Za-z0-9_.:-]*$")
SEPARATOR_RE = re.compile(r":?-{3,}:?")
BOUNDARY_PREV = frozenset(" \t\r\n`\"'([")
TRIM_CHARS = ".,;:!?)]}'\""
ASCII_ALNUM = frozenset(string.ascii_letters + string.digits)
EVENT_WORD = frozenset(string.ascii_letters + string.digits + "_")
HELD_PREV = frozenset("`\"'([</~=")
HELD_NEXT_BAD = frozenset(string.ascii_letters + string.digits + "_-")
UFO_PREFIX = ".ufo/"
CURL_UA = ("Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like "
           "Gecko) Chrome/130.0 Safari/537.36")
CURL_ACCEPT = "text/markdown, text/plain;q=0.9, */*;q=0.8"
CURL_WRITE_OUT = "\n%{http_code} %{url_effective}"


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


def git_show_bytes(lane: Path, rev: str, path: str) -> bytes | None:
    """The raw bytes of `path` at `rev`, or None when the path is absent.

    Bytes, not text: a snapshot's sha256 is over the bytes committed."""
    r = git(lane, ["show", "%s:%s" % (rev, path)])
    if r.returncode != 0:
        err = r.stderr.decode(errors="replace")
        if "does not exist" in err or "exists on disk, but not in" in err:
            return None
        raise EnvError("git show %s:%s failed: %s" % (rev, path, err.strip()))
    return r.stdout


def git_show(lane: Path, rev: str, path: str) -> str | None:
    data = git_show_bytes(lane, rev, path)
    return None if data is None else data.decode("utf-8")


def snapshot_path(sid: str) -> str:
    """The committed page snapshot of one source row."""
    return "%s/%s.page" % (SNAPSHOT_DIR, sid)


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
    """Rows of the FIRST table of the `### Hook files by client` section.

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


def row_sha(row: list[str]) -> str | None:
    """The FIRST full 64-hex sha256 printed anywhere in a SOURCES row.

    A truncated digest with an ellipsis is not a pin: no 64-hex run, no sha."""
    m = SHA256_RE.search(" | ".join(row))
    return m.group(1).lower() if m else None


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


def token_well_formed(token: str | None) -> bool:
    """The round-59 token grammar: a hook configuration file or folder.

    TOKEN_RE first, then, after stripping one leading `~/` or `./` and one
    trailing `/`: at least two path segments, the first segment dot-led, no
    segment holding a skill/agent/command/prompt/rule/plugin/extension word
    (EVERY segment, the final one included), and (E7) no non-final dot except
    as a segment's first character.  A directory token is allowed, and so is a
    glob in the final segment."""
    if not token or not TOKEN_RE.match(token):
        return False
    body = token[2:] if token.startswith(("~/", "./")) else token
    if body.endswith("/"):
        body = body[:-1]
    parts = body.split("/")
    if len(parts) < 2 or not parts[0].startswith("."):
        return False
    if any("." in seg[1:] for seg in parts[:-1]):
        return False
    return not any(w in NOT_HOOK_WORDS for seg in parts for w in seg_words(seg))


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
    """Span of the first CASE-SENSITIVE raw-token or normalised-form occurrence
    at a path-segment boundary."""
    if not token:
        return None
    best: tuple[int, int] | None = None
    for form in (token, normalise(token)):
        if not form:
            continue
        i = first_boundary(text, form)
        if i < 0:
            continue
        if best is None or i < best[0]:
            best = (i, i + len(form))
    return best


def hook_word_outside(text: str, start: int, end: int) -> bool:
    """Is there a whole `hook`/`hooks` word outside the token span?"""
    for m in HOOK_WORD_RE.finditer(text):
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


# ------------------------------------------------------------------- the events

def event_spans(cell: str) -> list[str]:
    """The distinct backticked spans of an Events cell, in the order printed."""
    out: list[str] = []
    for span in BACKTICK_RE.findall(cell):
        s = span.strip()
        if s and s not in out:
            out.append(s)
    return out


def events_cell_why(events: list[str]) -> list[str]:
    """The events-cell rule: >= 2 distinct spans, each a bare identifier."""
    why: list[str] = []
    if len(events) < 2:
        why.append("SKILL.md Events cell holds %d distinct backticked name(s) (need >= 2)"
                   % len(events))
    for name in events:
        if not EVENT_RE.match(name):
            why.append("event %r is not an identifier matching "
                       "^[A-Za-z][A-Za-z0-9_.:-]*$" % name)
    return why


def event_text(s: str) -> str:
    """Case-preserving page text for the event names.

    Script/style bodies, HTML comments and tags are dropped and entities are
    decoded, as for every other page check.  The Markdown markers `*` and
    backtick are dropped too (no event name may contain them), but `_` is
    KEPT: `_` is an identifier character for the boundary rule."""
    s = re.sub(r"(?is)<(style|script)\b.*?</\1\s*>", " ", s)
    s = re.sub(r"(?s)<!--.*?-->", " ", s)
    s = re.sub(r"</?[A-Za-z][^>]*>", " ", s)
    s = html.unescape(s)
    s = s.replace("`", "").replace("*", "")
    return re.sub(r"\s+", " ", s).strip()


def first_event_boundary(text: str, name: str) -> int:
    """Index of the first CASE-SENSITIVE `name` whose neighbouring characters
    are outside `[A-Za-z0-9_]`, or -1."""
    if not name:
        return -1
    start = 0
    while True:
        i = text.find(name, start)
        if i < 0:
            return -1
        j = i + len(name)
        left = i == 0 or text[i - 1] not in EVENT_WORD
        right = j >= len(text) or text[j] not in EVENT_WORD
        if left and right:
            return i
        start = i + 1


def event_on_page(page_text: str, name: str) -> bool:
    """Is `name` on the page as an identifier of its own?"""
    return first_event_boundary(event_text(page_text), name) >= 0


# ------------------------------------------------------------------- the judge

def hook_cell_matches(cell: str, token: str) -> bool:
    """E4: the entry `Hook config` cell, backticks stripped, IS the SKILL.md
    token or its normalise()d form (exact, case-sensitive)."""
    return cell.replace("`", "").strip() in (token, normalise(token))


def shared_tokens(srows: list[list[str]]) -> dict[str, set[str]]:
    """v2 E5: casefold(normalise(first backticked span)) -> the client names of
    every SKILL.md table row that uses it (any row, whatever its client cell)."""
    users: dict[str, set[str]] = {}
    for r in srows:
        r = (r + ["", "", "", ""])[:2]
        spans = BACKTICK_RE.findall(r[1])
        if spans:
            users.setdefault(normalise(spans[0]).casefold(), set()).add(client_name(r[0]))
    return users


def entry_row_verdict(er: list[str], client: str, token: str | None,
                      table: dict[str, list[str]], at_base: set[str],
                      base_urls: set[str], gate_raw: str, gate_plain: str,
                      events: list[str],
                      snapshot_of=None) -> tuple[list[str], str | None, str | None, str | None]:
    """Judge one entry row.  Returns (why, sid, url, quote).

    A malformed token has already been rejected on the SKILL.md side, so the
    entry row only looks for a token span when a token was read at all."""
    why: list[str] = []
    sid = url = quote = None
    if token and not hook_cell_matches(er[1], token):
        why.append("entry Hook config cell %r is not the SKILL.md token %r"
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
            why.append("quote does not hold the hook token %r (case-sensitive)"
                       % token)
        elif not hook_word_outside(q_plain, span[0], span[1]):
            why.append("quote holds no hook/hooks word outside the token")
    if not quote_in_gate(quote, gate_raw, gate_plain):
        why.append("round-59 Gate does not record this quote")
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
            sha = row_sha(s)
            if not sha:
                why.append("%s prints no full 64-hex sha256" % sid)
            else:
                data = snapshot_of(sid) if snapshot_of else None
                if data is None:
                    why.append("snapshot %s is missing at the revision"
                               % snapshot_path(sid))
                else:
                    got = hashlib.sha256(data).hexdigest()
                    if got != sha:
                        why.append("snapshot %s sha256 %s... does not equal the "
                                   "SOURCES row sha256 %s..."
                                   % (snapshot_path(sid), got[:12], sha[:12]))
                    else:
                        page = data.decode("utf-8", errors="replace")
                        for reason in page_why(page, quote, token, events):
                            why.append("snapshot %s: %s" % (snapshot_path(sid), reason))
    return why, sid, url, quote


def judge(skill: str, entry: str, sources: str, lesson: str,
          base_sources: str, snapshot_of=None) -> list[dict]:
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
        events: list[str] = []
        smine = [r for r in srows if client_name(r[0]) == client]
        if len(smine) != 1:
            why.append("SKILL.md rows naming client: %d (need exactly 1)" % len(smine))
        else:
            sr = ((smine[0] if smine else []) + ["", "", "", ""])[:4]
            spans = BACKTICK_RE.findall(sr[1])
            token = spans[0] if spans else None
            if token is None:
                why.append("SKILL.md hook config cell holds no backticked token")
            elif not token_well_formed(token):
                why.append("SKILL.md hook token %r is not well-formed" % token)
            else:
                norm_tok = normalise(token)
                in_k = True
                other = foreign_marker(client, token)
                if other:
                    why.append("SKILL.md hook token %r carries %s's marker %r"
                               % (token, other, MARKERS[other]))
            if token is not None:
                sharers = users.get(normalise(token).casefold(), set())
                if len(sharers) >= 2:
                    why.append("SKILL.md hook token %r is shared by rows %s"
                               % (token, ", ".join(sorted(sharers))))
            events = event_spans(sr[2])
            why.extend(events_cell_why(events))
            words = re.sub(r"[`*]", "", sr[3]).split()
            if len(words) < 3:
                why.append("SKILL.md action cell holds %d words (need >= 3)" % len(words))
        emine = [(r + ["", "", "", ""])[:4] for r in erows if client_name(r[0]) == client]
        picked = None
        row_whys = []
        for er in emine:
            row_why, sid, url, quote = entry_row_verdict(
                er, client, token, table, at_base, base_urls,
                gate_raw, gate_plain, events, snapshot_of)
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
                       "events": events,
                       "backed": not why, "why": why})
    return report


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


def first_boundary(text: str, token: str) -> int:
    """Index of the first CASE-SENSITIVE `token` at a boundary, or -1.

    The left character must be the start of the text or one of BOUNDARY_PREV,
    and the right character must be the end of the text or not a letter, a
    digit, `_` or `-`."""
    if not token:
        return -1
    start = 0
    while True:
        i = text.find(token, start)
        if i < 0:
            return -1
        j = i + len(token)
        right_ok = j >= len(text) or not (text[j] in ASCII_ALNUM or text[j] in "_-")
        if boundary_ok(text, i) and right_ok:
            return i
        start = i + 1


def token_at_boundary(text: str, token: str) -> bool:
    """Does `token` occur in `text` at a boundary?  CASE-SENSITIVE.

    Both ends are checked, so `.claude/setting` is not found inside
    `.claude/settings.json`."""
    return first_boundary(text, token) >= 0


def token_forms(token: str | None) -> list[str]:
    """The raw hook token and its normalise()d form, each also passed through
    the case-preserving page normalisation (which drops `*`, `_` and
    backticks).  Case is preserved: the comparison is case-sensitive."""
    if not token:
        return []
    forms: list[str] = []
    for cand in (token, normalise(token)):
        for f in (cand, page_plain(cand)):
            if f and f not in forms:
                forms.append(f)
    return forms


def quote_why(page_text: str, quote: str, token: str | None) -> list[str]:
    """Every reason the page does not carry the quote at a boundary and the
    token at a boundary (the round-58 quote check, with its reasons named)."""
    why: list[str] = []
    if not quote or norm(quote) not in norm_page(page_text):
        why.append("the quote is not on the page")
    elif token is None:
        why.append("no hook token to find on the page")
    else:
        text = norm_page_case(page_text)
        if not any(token_at_boundary(text, f) for f in token_forms(token)):
            why.append("the token %r is not on the page" % token)
    return why


def found_on_page(page_text: str, quote: str, token: str | None) -> bool:
    """The round-58 rule, unchanged: the page holds the quote AND the token."""
    return not quote_why(page_text, quote, token)


def page_why(page_text: str, quote: str, token: str | None,
             events: list[str]) -> list[str]:
    """Every reason the page does not carry the quote, the token and the events.

    The quote and the token are the round-58 checks; the events are the
    round-59 addition (case-sensitive, not inside a longer identifier)."""
    why: list[str] = []
    if not found_on_page(page_text, quote, token):
        why.extend(quote_why(page_text, quote, token))
    names = event_text(page_text)
    for name in events:
        if first_event_boundary(names, name) < 0:
            why.append("event %r is not on the page" % name)
    return why


def run_curl(url: str) -> tuple[int, str, bytes]:
    """One curl GET: (HTTP status, effective URL, body).

    `-sSL`, 30 s cap, browser User-Agent and `Accept` (round-58 routed defect
    R3: the page is served differently to a bot User-Agent).  The status and
    the URL after redirects come from curl's own write-out trailer, never from
    the body."""
    argv = ["curl", "-sSL", "--max-time", str(FETCH_TIMEOUT),
            "-A", CURL_UA,
            "-H", "Accept: " + CURL_ACCEPT,
            "-w", CURL_WRITE_OUT, url]
    try:
        r = subprocess.run(argv, capture_output=True)
    except OSError as e:
        raise OSError("curl not runnable: %s" % e) from e
    if r.returncode != 0:
        raise OSError("curl exited %d: %s"
                      % (r.returncode, r.stderr.decode(errors="replace").strip()[:200]))
    body, sep, tail = r.stdout.rpartition(b"\n")
    if not sep:
        raise OSError("curl wrote no status trailer")
    status, _, effective = tail.decode("utf-8", errors="replace").partition(" ")
    if not status.isdigit() or not effective.strip():
        raise OSError("curl status trailer unreadable: %r" % tail[:80])
    return int(status), effective.strip(), body


def fetch(url: str, pins: tuple[str, ...] | None = None,
          base_keys: set[str] | None = None) -> str:
    """curl GET, 30 s cap, at most 5 MiB, three attempts, HTTP 200 required.

    When `pins` is given, the URL reached after redirects must still be on the
    client's pinned hosts; when `base_keys` is given, a page whose URL after
    redirects is a base SOURCES URL is not found.  Both only add failures."""
    last: Exception | None = None
    for _ in range(FETCH_ATTEMPTS):
        try:
            status, final, data = run_curl(url)
            if status != 200:
                raise OSError("HTTP %d at %s" % (status, final))
            if pins is not None and not host_ok(final, pins):
                raise OSError("fetched off the pinned hosts at %s" % final)
            if base_keys is not None and url_key(final) in base_keys:
                raise OSError("reached a base SOURCES URL %s" % final)
            if url_is_change_note(final):
                raise OSError("reached a change-note page %s" % final)
            if len(data) > MAX_BYTES:
                raise OSError("page exceeds 5 MiB")
            return data.decode("utf-8", errors="replace")
        except Exception as e:  # network, status, pin or decode failure: not found
            last = e
    raise last if last else OSError("fetch failed")


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
        return ("hook files backed on committed snapshots %d of %d; "
                "found on the live page %d of %d; new ground %d"
                % (backed, k, found, k, ground))
    return ("hook files backed on committed snapshots %d of %d; "
            "live not run; new ground %d" % (backed, k, ground))


def reject_line(client: str, why: list[str]) -> str:
    return "reject %s: %s" % (client, "; ".join(why))


def predicate(fetching: bool, found: int, ground: int) -> int:
    """Exit 0 iff fetching, both targets are frozen, F >= TARGET and G >= NEW_TARGET."""
    if not fetching:
        return 1
    if TARGET is None or NEW_TARGET is None:
        return 1
    return 0 if found >= TARGET and ground >= NEW_TARGET else 1


def new_ground(norms: list[str], held: dict[str, bool]) -> int:
    """Distinct casefold(normalise(token)) values with ZERO held occurrences.

    `held` is keyed by the case-preserved normalised token; the held test
    itself is case-insensitive, so both spellings of one token get the same
    answer, and two clients whose tokens differ in case alone count once."""
    return len({t.casefold() for t in norms if t and not held.get(t)})


# ----------------------------------------------------- the self-test's git world

def held_world() -> tuple[dict[str, bool], dict[str, object]]:
    """A throw-away repository proving the base-tree scan and the git guards.

    `.claude/settings.json` sits only under `.ufo/`; `.GEMINI/Hooks` differs in
    case only; `.copilot/hooks.json` sits only in a binary blob;
    `.opencode/hooks.json` sits only in a blob reachable through a gitlink;
    `.cursor/hooks.json` sits in an ordinary tracked file."""
    tokens = [".claude/settings.json", ".gemini/hooks", ".copilot/hooks.json",
              ".opencode/hooks.json", ".cursor/hooks.json"]
    with tempfile.TemporaryDirectory(prefix="chf-self-test-") as td:
        repo = Path(td)
        (repo / ".ufo").mkdir()
        (repo / "a.md").write_text("see `.cursor/hooks.json` here\n", encoding="utf-8")
        (repo / ".ufo" / "b.md").write_text(".claude/settings.json\n", encoding="utf-8")
        (repo / "c.md").write_text(".GEMINI/Hooks\n", encoding="utf-8")
        (repo / "d.bin").write_bytes(b"binary\0\n.copilot/hooks.json\n")
        _self_git("init", "-q", str(repo))
        _self_git("-C", str(repo), "add", "-A", "-f", ".")
        _self_git("-C", str(repo), "-c", "user.name=c", "-c", "user.email=c@e",
                  "commit", "-q", "-m", "x")
        blob = _self_git("-C", str(repo), "hash-object", "-w", "--stdin",
                         data=b".opencode/hooks.json\n").stdout.decode().strip()
        _self_git("-C", str(repo), "update-index", "--add", "--cacheinfo",
                  "160000,%s,link" % blob)
        _self_git("-C", str(repo), "-c", "user.name=c", "-c", "user.email=c@e",
                  "commit", "-q", "-m", "link")
        probes = {
            "head": _outcome(lambda: verify_rev(repo, "HEAD")),
            "bogus": _outcome(lambda: verify_rev(repo, "0" * 40))[0],
            "shown": _outcome(lambda: git_show(repo, "HEAD", "a.md"))[0],
            "bytes": _outcome(lambda: git_show_bytes(repo, "HEAD", "d.bin"))[1],
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
    global BASE, TARGET, NEW_TARGET, lane_dir, run_curl
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

    # -- token well-formedness: every conjunct, red and green ------------
    check("green: .claude/settings.json is a file token",
          token_well_formed(".claude/settings.json"), True)
    check("green: .github/hooks/ is a directory token",
          token_well_formed(".github/hooks/"), True)
    check("green: .codex/config.toml",
          token_well_formed(".codex/config.toml"), True)
    check("green: .cursor/hooks.json",
          token_well_formed(".cursor/hooks.json"), True)
    check("green: .gemini/hooks/",
          token_well_formed(".gemini/hooks/"), True)
    check("green: .opencode/config.json",
          token_well_formed(".opencode/config.json"), True)
    check("green: a leading ~/ is stripped",
          token_well_formed("~/.claude/settings.json"), True)
    check("green: a leading ./ is stripped",
          token_well_formed("./.gemini/hooks/"), True)
    check("green: a glob in the final segment",
          token_well_formed(".github/hooks/*.json"), True)
    check("green: a dot-led non-final segment is fine (E7)",
          token_well_formed(".github/.hooks/config.json"), True)
    check("green: an agentic segment is not the word agent",
          token_well_formed(".claude/agentic/hooks.json"), True)
    check("green: an upper-case segment is not a banned word",
          token_well_formed(".claude/Hooks.json"), True)
    check("'' is not well-formed", token_well_formed(""), False)
    check("None is not well-formed", token_well_formed(None), False)
    check("red TOKEN_RE: a space",
          token_well_formed(".claude/settings json"), False)
    check("red TOKEN_RE: an empty middle segment",
          token_well_formed(".claude//settings.json"), False)
    check("red TOKEN_RE: an empty middle segment without a trailing slash",
          token_well_formed(".claude//settings.json"), False)
    check("red TOKEN_RE: a character outside the grammar",
          token_well_formed("@x/.claude/settings.json"), False)
    check("red TOKEN_RE: a leading slash",
          token_well_formed("/.claude/settings.json"), False)
    check("red segments: hooks is one segment",
          token_well_formed("hooks"), False)
    check("red segments: .hooks is one dot-led segment",
          token_well_formed(".hooks"), False)
    check("red segments: ./hooks is one segment after the strip",
          token_well_formed("./hooks"), False)
    check("red segments: ~/hooks is one segment after the strip",
          token_well_formed("~/hooks"), False)
    check("red segments: .claude is one segment",
          token_well_formed(".claude"), False)
    check("red first segment: settings.json does not start with a dot",
          token_well_formed("settings.json"), False)
    check("red first segment: claude/settings.json does not start with a dot",
          token_well_formed("claude/settings.json"), False)
    check("red segment word: .claude/skills/hooks.json",
          token_well_formed(".claude/skills/hooks.json"), False)
    check("red segment word: .claude/skill/hooks.json (singular)",
          token_well_formed(".claude/skill/hooks.json"), False)
    check("red segment word: .claude/agents/hooks.json",
          token_well_formed(".claude/agents/hooks.json"), False)
    check("red segment word: .claude/commands/hooks.json",
          token_well_formed(".claude/commands/hooks.json"), False)
    check("red segment word: .claude/prompts/hooks.json",
          token_well_formed(".claude/prompts/hooks.json"), False)
    check("red segment word: .cursor/rules/hooks.json",
          token_well_formed(".cursor/rules/hooks.json"), False)
    check("red segment word: .claude-plugin/hooks.json (a plugin segment)",
          token_well_formed(".claude-plugin/hooks.json"), False)
    check("red segment word: .claude-plugins/hooks.json (plural)",
          token_well_formed(".claude-plugins/hooks.json"), False)
    check("red segment word: .vscode/extensions/hooks.json",
          token_well_formed(".vscode/extensions/hooks.json"), False)
    check("red segment word: an agent-tools segment is the word agent",
          token_well_formed(".claude/agent-tools/hooks.json"), False)
    check("red segment word: .claude/skills.json (the FINAL segment counts)",
          token_well_formed(".claude/skills.json"), False)
    check("red E7: .claude/1.0/hooks.json (a version segment)",
          token_well_formed(".claude/1.0/hooks.json"), False)
    check("red E7: .claude.local/hooks.json (the first segment too)",
          token_well_formed(".claude.local/hooks.json"), False)
    check("red E7: ~/.claude/1.0.0/hooks.json",
          token_well_formed("~/.claude/1.0.0/hooks.json"), False)
    check("red E7: opencode.ai/docs/hooks/ (host, and not dot-led)",
          token_well_formed("opencode.ai/docs/hooks/"), False)

    # -- normalise: case preserved ---------------------------------------
    check("normalise strips one leading ~/",
          normalise("~/.claude/settings.json"), ".claude/settings.json")
    check("normalise strips one leading ./",
          normalise("./.opencode/hooks/"), ".opencode/hooks")
    check("normalise strips one trailing /",
          normalise(".gemini/hooks/"), ".gemini/hooks")
    check("normalise strips ONE trailing slash only",
          normalise(".opencode/hooks//"), ".opencode/hooks/")
    check("normalise PRESERVES case",
          normalise(".Claude/Settings.json"), ".Claude/Settings.json")
    check("normalise of nothing is empty", normalise(None), "")

    # -- the foreign-name guard ------------------------------------------
    check("a .claude token is foreign to VS Code",
          foreign_marker("VS Code", ".claude/settings.json"), "Claude Code")
    check("a .claude token is not foreign to Claude Code",
          foreign_marker("Claude Code", ".claude/settings.json"), None)
    check("an .opencode token is not foreign to opencode",
          foreign_marker("opencode", ".opencode/config.json"), None)
    check("a gemini token is not foreign to Gemini CLI",
          foreign_marker("Gemini CLI", ".gemini/hooks/"), None)
    check("the marker match is case-insensitive",
          foreign_marker("VS Code", ".Claude/Settings.json"), "Claude Code")
    check("a .cursor token is foreign to Gemini CLI",
          foreign_marker("Gemini CLI", ".cursor/hooks.json"), "Cursor")

    # -- the quote: word bounds, token span, the outside hook word -------
    check("E6: quote word count: six words pass",
          MIN_WORDS <= len("one two three four five six".split()) <= MAX_WORDS, True)
    check("E6: quote word count: five words fail",
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
    q = "Claude Code runs a PreToolUse hook from a .claude/settings.json file"
    span = token_span(q, ".claude/settings.json")
    check("the raw token is found in the quote", span is not None, True)
    check("a hook word sits outside the token span",
          hook_word_outside(q, span[0], span[1]), True)
    check("the token span starts where the token starts",
          q[span[0]:span[1]], ".claude/settings.json")
    q2 = "the file is .claude/settings.json"
    span2 = token_span(q2, ".claude/settings.json")
    check("only the token carries no hook word",
          hook_word_outside(q2, span2[0], span2[1]), False)
    q3 = "the folder is .gemini/hooks/"
    span3 = token_span(q3, ".gemini/hooks/")
    check("the hook word inside the token does not count",
          hook_word_outside(q3, span3[0], span3[1]), False)
    q4 = "Keep .claude/settings.json files for hooky reasons to reuse"
    span4 = token_span(q4, ".claude/settings.json")
    check("hooky is not the whole word hook",
          hook_word_outside(q4, span4[0], span4[1]), False)
    check("the plural hooks is the word",
          hook_word_outside("these two hooks differ", 0, 0), True)
    check("the token match is case-sensitive",
          token_span(".Claude/Settings.json is used", ".claude/settings.json"),
          None)
    check("the normalised form is matched too",
          token_span("see .opencode/hooks here", ".opencode/hooks/"),
          (4, 19))
    check("a token inside a longer path is not spanned (left boundary)",
          token_span("x.claude/settings.json here", ".claude/settings.json"), None)
    check("a token followed by a word is not spanned (right boundary)",
          token_span(".claude/settingsfoo here", ".claude/settings"), None)
    check("a token followed by a digit is not spanned",
          token_span(".claude/settings1 here", ".claude/settings"), None)
    check("a token followed by a slash is spanned",
          token_span(".claude/settings/x here", ".claude/settings"), (0, 16))

    # -- the Gate check ---------------------------------------------------
    gate = "## Gate\n\n| row | quote |\n|---|---|---|\n| S1 | \"the hook folder lives here\" |\n"
    gs = gate_section(gate)
    check("gate section is read", ws(gs).count("the hook folder lives here"), 1)
    check("quote recorded in the Gate", quote_in_gate(
        "the hook folder lives here", ws(gs), ws(gs.replace("`", ""))), True)
    check("quote absent from the Gate", quote_in_gate(
        "the hook folder lives elsewhere", ws(gs), ws(gs.replace("`", ""))), False)
    check("an empty Gate records no quote", quote_in_gate(
        "the hook folder lives here", ws(""), ws("")), False)
    check("Gate whitespace is normalised", quote_in_gate(
        "the  hook folder lives here", ws(gs), ws(gs.replace("`", ""))), True)

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

    # -- the events cell --------------------------------------------------
    check("EVENT_RE: PreToolUse is an identifier", bool(EVENT_RE.match("PreToolUse")), True)
    check("EVENT_RE: pre_tool_call is an identifier",
          bool(EVENT_RE.match("pre_tool_call")), True)
    check("EVENT_RE: tool.execute.before is an identifier",
          bool(EVENT_RE.match("tool.execute.before")), True)
    check("EVENT_RE: session:start is an identifier",
          bool(EVENT_RE.match("session:start")), True)
    check("EVENT_RE: PreToolUse! is not", bool(EVENT_RE.match("PreToolUse!")), False)
    check("EVENT_RE: 1PreToolUse is not", bool(EVENT_RE.match("1PreToolUse")), False)
    check("EVENT_RE: 'Pre Tool' is not", bool(EVENT_RE.match("Pre Tool")), False)
    check("event_spans reads spans in order",
          event_spans("`PreToolUse`, `PostToolUse`"),
          ["PreToolUse", "PostToolUse"])
    check("event_spans counts a repeated span once",
          event_spans("`PreToolUse`, `PreToolUse`, `Stop`"),
          ["PreToolUse", "Stop"])
    check("event_spans of a cell without backticks is empty",
          event_spans("PreToolUse and PostToolUse"), [])
    check("one span does not pass the events cell",
          events_cell_why(["PreToolUse"]),
          ["SKILL.md Events cell holds 1 distinct backticked name(s) (need >= 2)"])
    check("no span does not pass the events cell",
          events_cell_why([]),
          ["SKILL.md Events cell holds 0 distinct backticked name(s) (need >= 2)"])
    check("two identifiers pass the events cell",
          events_cell_why(["PreToolUse", "PostToolUse"]), [])
    check("a non-identifier span does not pass the events cell",
          events_cell_why(["PreToolUse", "pre tool"]),
          ["event 'pre tool' is not an identifier matching "
           "^[A-Za-z][A-Za-z0-9_.:-]*$"])
    check("event_text keeps underscores and case",
          event_text("a `pre_tool` b"), "a pre_tool b")
    check("event_text drops tags, comments and entities",
          event_text("<p>a &amp; b</p><!-- x --><code>PreToolUse</code>"),
          "a & b PreToolUse")
    check("event_text drops style and script bodies",
          "@layer base" in event_text("<style>@layer base{}</style><p>x</p>"
                                      "<script>@layer base</script>"), False)
    check("event found: standalone after a space",
          event_on_page("<p>on PreToolUse today</p>", "PreToolUse"), True)
    check("event found: at the start of the page",
          event_on_page("PreToolUse fires", "PreToolUse"), True)
    check("event found: at the end of the page",
          event_on_page("fires PreToolUse", "PreToolUse"), True)
    check("event found: after a dot",
          event_on_page("fires. PreToolUse", "PreToolUse"), True)
    check("event NOT found inside a longer identifier (letter)",
          event_on_page("<p>PreToolUseHook</p>", "PreToolUse"), False)
    check("event NOT found inside a longer identifier (digit)",
          event_on_page("<p>PreToolUse2</p>", "PreToolUse"), False)
    check("event NOT found inside a longer identifier (underscore)",
          event_on_page("<p>PreToolUse_hook</p>", "PreToolUse"), False)
    check("event NOT found with an underscore before it",
          event_on_page("<p>my_PreToolUse</p>", "PreToolUse"), False)
    check("event NOT found with a hyphen-joined prefix is found",
          event_on_page("<p>my-PreToolUse</p>", "PreToolUse"), True)
    check("event matching is case-sensitive",
          event_on_page("<p>pretooluse</p>", "PreToolUse"), False)

    # -- page normalisation and the found rule ----------------------------
    check("page style and script text is dropped",
          "@layer base" in norm_page(
              "<style>@layer base{}</style><p>x</p><script>@layer base</script>"), False)
    check("page tags are dropped and text kept",
          norm_page("<p>Use <code>/a-b</code> skill</p>"), "use /a-b skill")
    check("quote angle text is kept", norm("$<skill-name> here"), "$<skill-name> here")
    check("page_plain drops `*`, `_` and backticks but keeps case",
          page_plain("A*b_c`D"), "AbcD")
    check("norm lower-cases the quote", norm("Claude Ships"), "claude ships")
    page_ok = ("<p>Claude Code runs a PreToolUse hook from a "
               "<code>.claude/settings.json</code> file</p>")
    quote_ok = "Claude Code runs a PreToolUse hook from a .claude/settings.json file"
    check("found: quote and token both on the page",
          found_on_page(page_ok, quote_ok, ".claude/settings.json"), True)
    check("found: quote absent from the page",
          found_on_page(page_ok, "Claude Code runs a hook from a folder",
                        ".claude/settings.json"), False)
    check("found: token only inside a URL is rejected",
          found_on_page("<p>the hook file is at "
                        "https://example.com/.claude/settings.json</p>",
                        "the hook file is at", ".claude/settings.json"), False)
    check("found: token after a space is accepted",
          found_on_page("<p>the hook file is .claude/settings.json today</p>",
                        "the hook file is", ".claude/settings.json"), True)
    check("found: a tilde token is found on the page",
          found_on_page("<p>the hooks live in ~/.claude/settings.json today</p>",
                        "the hooks live in ~/.claude/settings.json",
                        "~/.claude/settings.json"), True)
    check("found: a token case difference is rejected",
          found_on_page("<p>the hook file is .Claude/Settings.json</p>",
                        "the hook file is", ".claude/settings.json"), False)
    check("found: a digit after the token is rejected",
          found_on_page("<p>the hook file is .claude/settings.json1</p>",
                        "the hook file is", ".claude/settings.json"), False)
    check("found: no token is never found",
          found_on_page(page_ok, quote_ok, None), False)
    check("page_why names the missing quote",
          page_why(page_ok, "Claude Code runs a hook from a folder",
                   ".claude/settings.json", []), ["the quote is not on the page"])
    check("page_why names the missing token",
          page_why("<p>Claude Code runs a PreToolUse hook from a folder</p>",
                   "Claude Code runs a PreToolUse hook from a folder",
                   ".claude/settings.json", []),
          ["the token '.claude/settings.json' is not on the page"])
    check("page_why names the missing event",
          page_why(page_ok, quote_ok, ".claude/settings.json", ["Stop"]),
          ["event 'Stop' is not on the page"])
    check("page_why is empty when the page carries everything",
          page_why(page_ok + "<p><code>PostToolUse</code> too</p>", quote_ok,
                   ".claude/settings.json", ["PreToolUse", "PostToolUse"]), [])
    check("boundary: at the start of the text is accepted",
          token_at_boundary(".claude/settings", ".claude/settings"), True)
    check("boundary: after a letter is rejected",
          token_at_boundary("x.claude/settings", ".claude/settings"), False)
    check("boundary: after a digit is rejected",
          token_at_boundary("1.claude/settings", ".claude/settings"), False)
    check("boundary: after a dot is rejected",
          token_at_boundary("a.claude/settings", ".claude/settings"), False)
    check("boundary: after a slash is rejected",
          token_at_boundary("/.claude/settings", ".claude/settings"), False)
    check("boundary: after a hyphen is rejected",
          token_at_boundary("-.claude/settings", ".claude/settings"), False)
    check("boundary: after a comma is rejected",
          token_at_boundary(",.claude/settings", ".claude/settings"), False)
    check("boundary: after a backtick is accepted",
          token_at_boundary("`.claude/settings`", ".claude/settings"), True)
    check("boundary: after a quote is accepted",
          token_at_boundary('".claude/settings"', ".claude/settings"), True)
    check("boundary: after a parenthesis is accepted",
          token_at_boundary("(.claude/settings)", ".claude/settings"), True)
    check("boundary: after a bracket is accepted",
          token_at_boundary("[.claude/settings]", ".claude/settings"), True)
    check("boundary: a singular token inside the plural is not found",
          token_at_boundary("put files in .claude/settings.json now",
                            ".claude/setting"), False)
    check("boundary: the token followed by a slash is found",
          token_at_boundary("put files in .claude/setting/x now", ".claude/setting"),
          True)
    check("boundary: the token followed by a hyphen is not found",
          token_at_boundary(".claude/setting-x", ".claude/setting"), False)
    check("boundary: the token followed by an underscore is not found",
          token_at_boundary(".claude/setting_x", ".claude/setting"), False)

    # -- held occurrences: case and segment bounds ------------------------
    tok = ".claude/settings.json"
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
          held_in_text("my" + tok, tok), False)
    check("held: a hyphen before it does not hold it",
          held_in_text("x-" + tok, tok), False)
    check("held: a dot-joined prefix does not hold it",
          held_in_text("my." + tok, tok), False)
    check("held: a directory prefix with a slash does hold it",
          held_in_text("x/" + tok, tok), True)
    check("a CASE difference holds it (.Claude/Settings.json vs held lowercase)",
          held_in_text(".Claude/Settings.json", tok), True)
    check("an upper-case token is held by lowercase base text",
          held_in_text("see .claude/settings.json", ".Claude/Settings.json"), True)
    check("the case-insensitive match keeps the segment boundary",
          held_in_text("my.Claude/Settings.json", tok), False)
    check("held: the casefold, not lower(), matches a long s",
          held_in_text(".claude/\u017fettings.json", tok), True)
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
        ".claude/settings.json": False,
        ".gemini/hooks": True,
        ".cursor/hooks.json": True,
        ".copilot/hooks.json": False,
        ".opencode/hooks.json": False})
    check("verify_rev accepts a real commit", probes.get("head"), ("ok", None))
    check("verify_rev rejects an unknown revision", probes.get("bogus"), "EnvError")
    check("git_show reads a tracked file", probes.get("shown"), "ok")
    check("git_show_bytes reads the raw bytes", probes.get("bytes"),
          b"binary\0\n.copilot/hooks.json\n")
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

    # -- the SOURCES sha256 pin and the snapshot path ---------------------
    sha_full = "971d75bfce7a04c2e0d41e8752d01afe29ed500f2a7159f66d5f7156bea0c3ff"
    check("row_sha reads a plain sha256 <64 hex>",
          row_sha(["S900", "x", "docs", "A", "s", "sha256 " + sha_full]),
          sha_full)
    check("row_sha reads a backticked, upper-case sha256",
          row_sha(["S900", "x", "docs", "A", "s", "sha256 `" + sha_full.upper() + "`"]),
          sha_full)
    check("row_sha of an ellipsis digest is None",
          row_sha(["S900", "x", "docs", "A", "s", "sha256 `9a67de89\u2026`"]), None)
    check("row_sha takes the FIRST digest when two are printed",
          row_sha(["S900", "x", "docs", "A", "s",
                   "sha256 " + sha_full + " then sha256 " + "a" * 64]),
          sha_full)
    check("row_sha of a 63-hex run is None",
          row_sha(["S900", "x", "docs", "A", "s", "sha256 " + "a" * 63]), None)
    check("snapshot_path names the S-id page",
          snapshot_path("S900"), ".ufo/waves/round-59/snapshots/S900.page")

    # -- the output lines and the predicate ------------------------------
    check("fetch summary line", summary_line(True, 0, 0, 0, 0),
          "hook files backed on committed snapshots 0 of 0; "
          "found on the live page 0 of 0; new ground 0")
    check("non-fetch summary line", summary_line(False, 2, 7, 0, 0),
          "hook files backed on committed snapshots 2 of 7; "
          "live not run; new ground 0")
    check("reject line", reject_line("Cursor", ["a", "b"]), "reject Cursor: a; b")
    check("E3: url_is_change_note on each word",
          [url_is_change_note("https://x.com/a/%s/b" % w) for w in CHANGE_NOTE_WORDS],
          [True] * len(CHANGE_NOTE_WORDS))
    check("E3: url_is_change_note is case-insensitive and percent-decoded",
          (url_is_change_note("https://x.com/CHANGELOG.md"),
           url_is_change_note("https://x.com/%62log/x")), (True, True))
    check("E3: a docs URL is not a change note",
          url_is_change_note("https://code.claude.com/docs/en/hooks"), False)
    check("E3: a change-note word only in the query is not the path",
          url_is_change_note("https://cursor.com/docs/hooks?from=blog"), False)
    check("ground: two spellings of one token count once",
          new_ground([".Claude/Settings.json", ".claude/settings.json"], {}), 1)
    check("ground: a held spelling drops its own key",
          new_ground([".Claude/Settings.json", ".claude/settings.json"],
                     {".claude/settings.json": True,
                      ".Claude/Settings.json": True}), 0)
    check("ground: two different tokens count twice",
          new_ground([".gemini/hooks", ".opencode/hooks"], {}), 2)
    check("ground: a held token is not new ground",
          new_ground([".gemini/hooks"], {".gemini/hooks": True}), 0)
    check("ground: nothing found is zero", new_ground([], {}), 0)

    frozen = (TARGET, NEW_TARGET)
    try:
        TARGET, NEW_TARGET = 5, 3
        check("predicate: fetch, 5 of 7, ground 3, passes", predicate(True, 5, 3), 0)
        check("predicate: fetch, 4 of 7, ground 3, fails", predicate(True, 4, 3), 1)
        check("predicate: fetch, 5 of 7, ground 2, fails", predicate(True, 5, 2), 1)
        check("predicate: no fetch always fails", predicate(False, 7, 7), 1)
        TARGET, NEW_TARGET = None, None
        check("predicate: no targets is a 1, never a 0", predicate(True, 7, 7), 1)
        check("predicate: no targets with one set is a 1", predicate(True, 7, 7), 1)
    finally:
        TARGET, NEW_TARGET = frozen

    # -- the synthetic world: SKILL row, entry, SOURCES, Gate, snapshots ---
    skill = ("# x\n\n### Hook files by client\n\n"
             "| Client | Hook config | Events | Action |\n"
             "|---|---|---|---|\n"
             "| Claude Code | `.claude/settings.json` | `PreToolUse`, `PostToolUse` "
             "| move a must-hold rule here |\n"
             "| Gemini CLI | `.gemini/hooks/` | `BeforeTool`, `AfterTool` "
             "| move a must-hold rule here |\n")
    quote1 = "Claude Code runs a PreToolUse hook from a .claude/settings.json file"
    quote2 = "Gemini CLI runs a BeforeTool hook from a .gemini/hooks/ folder"
    entry = ("# e\n\n| Client | Hook config | Source | Quote |\n|---|---|---|---|\n"
             '| Claude Code | .claude/settings.json | S900 | "' + quote1 + '" |\n'
             '| Gemini CLI | .gemini/hooks/ | S901 | "' + quote2 + '" |\n')
    def page_for(quote: str, events: list[str]) -> str:
        """A snapshot page that carries `quote` and every event name."""
        return ("<p>%s</p><p>%s</p>"
                % (quote, " ".join("<code>%s</code>" % e for e in events)))

    src_row = ("| %s | %s docs \u2014 %s | docs | A | the hook file "
               "| \u00a7 hooks, fetched, sha256 %s | the hook file | mined "
               "| %s | 90d | corpus/knowledge/hook-files-round59.md |\n")
    def world(q1: str = quote1, q2: str = quote2,
              e1: list[str] | None = None,
              e2: list[str] | None = None) -> tuple[str, dict]:
        """The SOURCES rows and committed pages for a pair of quotes.

        Each row prints the sha256 of its own page bytes, so a page built for
        another quote is a sha mismatch, never a silent pass."""
        ev1 = ["PreToolUse", "PostToolUse"] if e1 is None else e1
        ev2 = ["BeforeTool", "AfterTool"] if e2 is None else e2
        pages = {"S900": page_for(q1, ev1).encode(),
                 "S901": page_for(q2, ev2).encode()}
        rows = (src_row % ("S900", "Claude Code",
                           "https://code.claude.com/docs/en/hooks.md",
                           hashlib.sha256(pages["S900"]).hexdigest(), OPENED[0])
                + src_row % ("S901", "Gemini CLI",
                             "https://geminicli.com/docs/cli/hooks.md",
                             hashlib.sha256(pages["S901"]).hexdigest(), OPENED[0]))
        return rows, pages

    sources, snaps = world()
    page1, page2 = snaps["S900"].decode(), snaps["S901"].decode()
    sha1 = hashlib.sha256(snaps["S900"]).hexdigest()
    sha2 = hashlib.sha256(snaps["S901"]).hexdigest()
    lesson = ("## Gate\n\n| row | URL | quote |\n|---|---|---|\n"
              '| S900 | https://code.claude.com/docs/en/hooks.md | "' + quote1 + '" |\n'
              '| S901 | https://geminicli.com/docs/cli/hooks.md | "' + quote2 + '" |\n')
    base = ("| S001 | Old docs \u2014 https://code.claude.com/docs/en/old.md | docs "
            "| A | s | a | t | mined | 2026-10-01 | 90d | y |\n")

    def judge_world(sk=skill, en=entry, so=sources, le=lesson, ba=base,
                    sn=None) -> list[dict]:
        pages = snaps if sn is None else sn
        return judge(sk, en, so, le, ba, snapshot_of=pages.get)

    def backed(sk=skill, en=entry, so=sources, le=lesson, ba=base,
               sn=None) -> list[str]:
        return [r["client"] for r in judge_world(sk, en, so, le, ba, sn)
                if r["backed"]]

    def why_of(client: str, sk=skill, en=entry, so=sources, le=lesson, ba=base,
               sn=None) -> list[str]:
        return {r["client"]: r["why"] for r in judge_world(sk, en, so, le, ba, sn)}[client]

    def k_of(sk=skill) -> int:
        return sum(1 for r in judge_world(sk) if r["in_k"])

    check("the synthetic world backs both clients",
          backed(), ["Claude Code", "Gemini CLI"])
    check("the synthetic world counts both tokens in K", k_of(), 2)
    check("a duplicate SKILL.md row disqualifies the client",
          backed(sk=skill.replace("| Gemini CLI |",
                                  "| Claude Code | `~/.x/hooks/x` | `A`, `B` | y |\n"
                                  "| Gemini CLI |")),
          ["Gemini CLI"])
    check("a second entry row does not disqualify a good one",
          backed(en=entry + '| Gemini CLI | x | S901 | "x y z" |\n'),
          ["Claude Code", "Gemini CLI"])
    check("an S### already at base is not backed",
          backed(ba=base.replace("S001", "S900")), ["Gemini CLI"])
    check("a base URL is not backed",
          backed(ba=base.replace("old.md", "hooks.md")), ["Gemini CLI"])
    check("a base URL reached by a path-case alias is not backed",
          backed(ba=base.replace("old.md", "HOOKS")), ["Gemini CLI"])
    check("a quote missing from the Gate is not backed",
          backed(le=lesson.replace("PreToolUse hook", "PreToolUse directive")),
          ["Gemini CLI"])
    check("a two-word action cell is not backed",
          backed(sk=skill.replace("move a must-hold rule here |",
                                  "move it |", 1)),
          ["Gemini CLI"])
    check("a tier B row is not backed",
          backed(so=sources.replace("| docs | A |", "| docs | B |", 1)), ["Gemini CLI"])
    check("a queued row is not backed",
          backed(so=sources.replace("| mined |", "| queued |", 1)), ["Gemini CLI"])
    check("another opened date is not backed",
          backed(so=sources.replace("| mined | 2026-10-23 |",
                                    "| mined | 2026-10-22 |", 1)),
          ["Gemini CLI"])
    check("a non-docs kind is not backed",
          backed(so=sources.replace("| docs | A |", "| issue | A |", 1)), ["Gemini CLI"])
    check("an off-host URL is not backed",
          backed(so=sources.replace("https://code.claude.com",
                                    "https://code.claude.com.evil.io", 1)), ["Gemini CLI"])
    check("a tracker URL on a pinned host is not backed",
          backed(so=sources.replace(
              "https://code.claude.com/docs/en/hooks.md",
              "https://github.com/anthropics/claude-code/issues/1", 1)),
          ["Gemini CLI"])
    check("a source cell without a URL is not backed",
          backed(so=sources.replace(
              "https://code.claude.com/docs/en/hooks.md", "no url here", 1)),
          ["Gemini CLI"])
    check("a source cell without a URL is reported as such",
          any("holds no URL" in w for w in why_of("Claude Code", so=sources.replace(
              "https://code.claude.com/docs/en/hooks.md", "no url here", 1))), True)
    check("a malformed hook token is not backed and leaves K",
          (backed(sk=skill.replace("`.gemini/hooks/`", "`hooks`")),
           k_of(skill.replace("`.gemini/hooks/`", "`hooks`"))),
          (["Claude Code"], 1))
    check("a skill-folder token is not well-formed",
          backed(sk=skill.replace("`.claude/settings.json`",
                                  "`.claude/skills/hooks.json`")), ["Gemini CLI"])
    check("a command-folder token is not well-formed",
          backed(sk=skill.replace("`.claude/settings.json`",
                                  "`.claude/commands/hooks.json`")), ["Gemini CLI"])
    check("a hook cell without a backticked token is not backed",
          backed(sk=skill.replace("`.gemini/hooks/`", ".gemini/hooks/")),
          ["Claude Code"])
    check("a hook cell without a backticked token is reported as such",
          any("no backticked token" in w for w in why_of(
              "Gemini CLI", sk=skill.replace("`.gemini/hooks/`",
                                             ".gemini/hooks/"))), True)
    foreign_quote = "Gemini CLI runs a BeforeTool hook from a .claude/hooks/ folder"
    foreign_sources, foreign_snaps = world(q2=foreign_quote)
    check("a token carrying another client's marker is not backed",
          backed(sk=skill.replace("`.gemini/hooks/`", "`.claude/hooks/`"),
                 en=entry.replace(".gemini/hooks/", ".claude/hooks/"),
                 le=lesson.replace(".gemini/hooks/", ".claude/hooks/"),
                 so=foreign_sources, sn=foreign_snaps),
          ["Claude Code"])
    def quote_world(q2: str) -> tuple[str, dict]:
        """Source rows and pages for an alternative Gemini quote."""
        return world(q2=q2)

    no_token = "Gemini CLI runs a BeforeTool hook from a folder"
    check("a quote without the token is not backed",
          backed(en=entry.replace(quote2, no_token),
                 le=lesson.replace(quote2, no_token), so=quote_world(no_token)[0],
                 sn=quote_world(no_token)[1]),
          ["Claude Code"])
    in_token = "Gemini CLI keeps its file at .gemini/hooks/"
    check("a quote without a hook word outside the token is not backed",
          backed(en=entry.replace(quote2, in_token),
                 le=lesson.replace(quote2, in_token), so=quote_world(in_token)[0],
                 sn=quote_world(in_token)[1]),
          ["Claude Code"])
    check("a quote whose only hook word is inside the token is reported",
          any("no hook/hooks word outside the token" in w for w in why_of(
              "Gemini CLI", en=entry.replace(quote2, in_token),
              le=lesson.replace(quote2, in_token), so=quote_world(in_token)[0],
              sn=quote_world(in_token)[1])), True)
    hooky = "Keep .claude/settings.json files for hooky reasons to reuse"
    check("a quote whose only hook-like word is hooky is not backed",
          backed(en=entry.replace(quote1, hooky), le=lesson.replace(quote1, hooky),
                 so=world(q1=hooky)[0], sn=world(q1=hooky)[1]),
          ["Gemini CLI"])
    case_diff = "Gemini CLI runs a BeforeTool hook from a .Gemini/Hooks/ folder"
    check("a quote whose token differs only in case is not backed",
          backed(en=entry.replace(quote2, case_diff),
                 le=lesson.replace(quote2, case_diff),
                 so=quote_world(case_diff)[0], sn=quote_world(case_diff)[1]),
          ["Claude Code"])
    two = "hooks .gemini/hooks/"
    check("a two-word quote is not backed",
          backed(en=entry.replace(quote2, two), le=lesson.replace(quote2, two),
                 so=quote_world(two)[0], sn=quote_world(two)[1]), ["Claude Code"])
    long_quote = " ".join(["hooks"] + ["w"] * 24 + [".gemini/hooks/"])
    check("a 26-word quote is not backed",
          backed(en=entry.replace(quote2, long_quote),
                 le=lesson.replace(quote2, long_quote),
                 so=quote_world(long_quote)[0], sn=quote_world(long_quote)[1]),
          ["Claude Code"])
    check("an entry source cell that is not one S### id is not backed",
          backed(en=entry.replace("| S901 |", "| docs |")), ["Claude Code"])
    check("an entry quote cell that is empty is not backed",
          backed(en=entry.replace('"' + quote2 + '"', '" "')), ["Claude Code"])
    check("an S### absent from SOURCES.md is not backed",
          backed(en=entry.replace("S901", "S999")), ["Claude Code"])
    check("a SOURCES row with the wrong cell count is not backed",
          backed(so=sources.replace(
              "| mined | 2026-10-23 | 90d | corpus/knowledge/hook-files-round59.md |\n",
              "| mined | 2026-10-23 | 90d |\n", 1)),
          ["Gemini CLI"])
    check("no entry row for the client is not backed",
          backed(en=entry.replace(
              '| Gemini CLI | .gemini/hooks/ | S901 | "' + quote2 + '" |\n', "")),
          ["Claude Code"])

    # -- E4: the entry Hook config cell is the SKILL.md token ------------
    check("E4: an entry Hook config cell that differs from SKILL.md is not backed",
          backed(en=entry.replace("| Gemini CLI | .gemini/hooks/ |",
                                  "| Gemini CLI | .gemini/other.json |")),
          ["Claude Code"])
    check("E4: the mismatch is reported as such",
          any("Hook config cell" in w for w in why_of(
              "Gemini CLI", en=entry.replace("| Gemini CLI | .gemini/hooks/ |",
                                             "| Gemini CLI | .gemini/other.json |"))),
          True)
    check("E4: a backticked Hook config cell still backs",
          backed(en=entry.replace("| Gemini CLI | .gemini/hooks/ |",
                                  "| Gemini CLI | `.gemini/hooks/` |")),
          ["Claude Code", "Gemini CLI"])
    check("E4: the raw ./ form in the cell still backs",
          backed(sk=skill.replace("`.gemini/hooks/`", "`./.gemini/hooks/`"),
                 en=entry.replace("| Gemini CLI | .gemini/hooks/ |",
                                  "| Gemini CLI | ./.gemini/hooks/ |")),
          ["Claude Code", "Gemini CLI"])
    check("E4: the normalised form is not the raw cell of a ./ token",
          backed(sk=skill.replace("`.gemini/hooks/`", "`./.gemini/hooks/`")),
          ["Claude Code"])
    check("E4: a Hook config cell differing only in case is not backed",
          backed(en=entry.replace("| Gemini CLI | .gemini/hooks/ |",
                                  "| Gemini CLI | .Gemini/Hooks/ |")),
          ["Claude Code"])
    check("E4: an empty Hook config cell is not backed",
          backed(en=entry.replace("| Gemini CLI | .gemini/hooks/ |",
                                  "| Gemini CLI |  |")),
          ["Claude Code"])
    check("E4: hook_cell_matches trims spaces and backticks",
          hook_cell_matches(" `.claude/settings.json` ", ".claude/settings.json"), True)

    # -- E5: one token cannot serve two clients -----------------------------
    shared = skill + (
        "| Cursor | `.gemini/hooks/` | `A`, `B` | move a must-hold rule here |\n")
    check("E5: a token shared with another client disqualifies both rows",
          [r["client"] for r in judge_world(shared)
           if "shared by rows" in "; ".join(r["why"])], ["Gemini CLI", "Cursor"])
    check("E5: the sharing disqualifies the otherwise-backed row",
          backed(sk=shared), ["Claude Code"])
    check("E5: sharing is judged on casefold(normalise())",
          backed(sk=skill + "| Codex | `~/.Gemini/Hooks/` | `A`, `B` "
                            "| move a must-hold rule here |\n"),
          ["Claude Code"])
    check("E5: a row of an unlisted client name also counts as a user",
          backed(sk=skill + "| Zed | `.gemini/hooks/` | `A`, `B` "
                            "| move a must-hold rule here |\n"),
          ["Claude Code"])
    check("E5: a row with an empty client cell also counts as a user",
          backed(sk=skill + "| | `.gemini/hooks/` | `A`, `B` "
                            "| move a must-hold rule here |\n"),
          ["Claude Code"])
    check("E5: a duplicate row of the SAME client is not a cross-client share",
          shared_tokens(skill_rows(skill + "| Gemini CLI | `.gemini/hooks/` | `A`, `B` | y |\n"))
          [".gemini/hooks"], {"Gemini CLI"})
    check("E5: distinct tokens are not shared",
          sorted(len(v) for v in shared_tokens(skill_rows(skill)).values()), [1, 1])

    # -- E6: six-word quotes ------------------------------------------------
    five = "Gemini reads hooks in .gemini/hooks/"
    check("E6: a five-word quote is not backed",
          backed(en=entry.replace(quote2, five), le=lesson.replace(quote2, five),
                 so=world(q2=five)[0], sn=world(q2=five)[1]),
          ["Claude Code"])
    six = "Gemini CLI reads hooks in .gemini/hooks/"
    check("E6: a six-word quote backs",
          backed(en=entry.replace(quote2, six), le=lesson.replace(quote2, six),
                 so=world(q2=six)[0], sn=world(q2=six)[1]),
          ["Claude Code", "Gemini CLI"])
    check("a single-segment SKILL token is not backed",
          backed(sk=skill.replace("`.claude/settings.json`", "`settings.json`")),
          ["Gemini CLI"])
    check("a changelog URL is not backed",
          backed(so=sources.replace("https://code.claude.com/docs/en/hooks.md",
                                    "https://code.claude.com/docs/en/changelog.md", 1)),
          ["Gemini CLI"])
    check("a change-note URL is reported as such",
          any("changelog/release/news/blog" in w for w in why_of(
              "Claude Code", so=sources.replace(
                  "https://code.claude.com/docs/en/hooks.md",
                  "https://raw.githubusercontent.com/anthropics/claude-code/main/CHANGELOG.md",
                  1))), True)
    check("a wrong SKILL.md header reads no row",
          skill_rows(skill.replace("| Action |", "| Notes |")), [])
    check("a wrong entry header reads no row",
          entry_rows(entry.replace("| Source |", "| Row |")), [])
    check("a table under another heading is not read",
          skill_rows(skill.replace(SKILL_HEADING, "### Other table")), [])

    # -- the events cell: judge-level ---------------------------------------
    one_span = skill.replace("`PreToolUse`, `PostToolUse`", "`PreToolUse`")
    check("an Events cell with one span is not backed",
          backed(sk=one_span), ["Gemini CLI"])
    check("an Events cell with one span is reported as such",
          any("need >= 2" in w for w in why_of("Claude Code", sk=one_span)), True)
    three = skill.replace("`PreToolUse`, `PostToolUse`",
                          "`PreToolUse`, `PostToolUse`, `Notification`")
    check("an event absent from the snapshot is not backed",
          backed(sk=three), ["Gemini CLI"])
    check("an event absent from the snapshot is reported as such",
          any("event 'Notification' is not on the page" in w
              for w in why_of("Claude Code", sk=three)), True)
    page_ident = ("<p>Claude Code runs a PreToolUse hook from a "
                  "<code>.claude/settings.json</code> file</p>"
                  "<p>A hook may fire on <code>PreToolUse</code> or "
                  "<code>PostToolUse</code>; <code>NotificationHook</code> is "
                  "separate.</p>")
    page_ident_ok = page_ident.replace("<code>NotificationHook</code>",
                                       "<code>Notification</code>")
    ident_snaps = {"S900": page_ident.encode(), "S901": page2.encode()}
    ok_snaps = {"S900": page_ident_ok.encode(), "S901": page2.encode()}
    ok_sources = sources.replace(sha1, hashlib.sha256(page_ident_ok.encode()).hexdigest(), 1)
    ident_sources = sources.replace(sha1, hashlib.sha256(page_ident.encode()).hexdigest(), 1)
    check("an event found only inside a longer identifier is not backed",
          backed(sk=three, so=ident_sources, sn=ident_snaps), ["Gemini CLI"])
    check("an event inside a longer identifier is reported as not on the page",
          any("event 'Notification' is not on the page" in w for w in why_of(
              "Claude Code", sk=three, so=ident_sources, sn=ident_snaps)), True)
    check("the same events on a page that spells them whole back both",
          backed(sk=three, so=ok_sources, sn=ok_snaps),
          ["Claude Code", "Gemini CLI"])

    # -- the snapshot: existence, sha256 pin, quote and events --------------
    check("a missing snapshot is not backed",
          backed(sn={"S901": page2.encode()}), ["Gemini CLI"])
    check("a missing snapshot is reported as missing",
          any("is missing at the revision" in w for w in why_of(
              "Claude Code", sn={"S901": page2.encode()})), True)
    bumped = {"S900": page1.encode() + b"\n", "S901": page2.encode()}
    check("a snapshot whose sha256 differs from the SOURCES row is not backed",
          backed(sn=bumped), ["Gemini CLI"])
    check("a snapshot sha mismatch is reported as such",
          any("does not equal the SOURCES row sha256" in w for w in why_of(
              "Claude Code", sn=bumped)), True)
    no_sha = sources.replace("sha256 " + sha1, "sha256 `9a67de89\u2026`", 1)
    check("a SOURCES row without a full 64-hex sha256 is not backed",
          backed(so=no_sha), ["Gemini CLI"])
    check("a SOURCES row without a full 64-hex sha256 is reported as such",
          any("prints no full 64-hex sha256" in w for w in why_of(
              "Claude Code", so=no_sha)), True)
    page_no_quote = ("<p>The file is <code>.claude/settings.json</code>.</p>"
                     "<p>A hook may fire on <code>PreToolUse</code> or "
                     "<code>PostToolUse</code>.</p>")
    no_quote_snaps = {"S900": page_no_quote.encode(), "S901": page2.encode()}
    no_quote_sources = sources.replace(
        sha1, hashlib.sha256(page_no_quote.encode()).hexdigest(), 1)
    check("a snapshot that does not carry the quote is not backed",
          backed(so=no_quote_sources, sn=no_quote_snaps), ["Gemini CLI"])
    check("a snapshot without the quote is reported as such",
          any("the quote is not on the page" in w for w in why_of(
              "Claude Code", so=no_quote_sources, sn=no_quote_snaps)), True)

    # -- the counter's own sha256 ----------------------------------------
    own = Path(__file__).read_bytes()
    check("the own sha256 is 64 hex", len(self_sha()), 64)
    check("the own sha256 is the sha256 of this file",
          self_sha(), hashlib.sha256(own).hexdigest())

    # -- a SUCCESSFUL end-to-end main() path (round-57 R4 / lesson M71) ----
    with tempfile.TemporaryDirectory(prefix="chf-main-") as td:
        repo = Path(td)
        (repo / "corpus" / "knowledge").mkdir(parents=True)
        (repo / "corpus" / "lessons").mkdir(parents=True)
        (repo / SNAPSHOT_DIR).mkdir(parents=True)
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
        (repo / "corpus" / "knowledge" / "hook-files-round59.md").write_text(
            entry, encoding="utf-8")
        (repo / "corpus" / "SOURCES.md").write_text(sources, encoding="utf-8")
        (repo / "corpus" / "lessons" / "round-59.md").write_text(
            lesson, encoding="utf-8")
        (repo / SNAPSHOT_DIR / "S900.page").write_bytes(page1.encode())
        (repo / SNAPSHOT_DIR / "S901.page").write_bytes(page2.encode())
        _self_git("-C", str(repo), "add", "-A", "-f", ".")
        _self_git("-C", str(repo), "-c", "user.name=c", "-c", "user.email=c@e",
                  "commit", "-q", "-m", "measured")
        measured = _self_git("-C", str(repo), "rev-parse",
                             "HEAD").stdout.decode().strip()
        good_line = ("hook files backed on committed snapshots 2 of 2; "
                     "found on the live page 2 of 2; new ground 2")
        live_pages = {
            "https://code.claude.com/docs/en/hooks.md": page1,
            "https://geminicli.com/docs/cli/hooks.md": page2,
        }

        def live_ok(url: str) -> tuple[int, str, bytes]:
            return 200, url, live_pages[url].encode()

        def live_404(url: str) -> tuple[int, str, bytes]:
            return 404, url, b"not found"

        def live_down(url: str) -> tuple[int, str, bytes]:
            raise OSError("curl exited 6")

        saved = (BASE, TARGET, NEW_TARGET, lane_dir, run_curl)
        try:
            BASE, TARGET, NEW_TARGET = base_sha, 2, 2
            lane_dir = lambda: repo
            run_curl = live_ok
            out = io.StringIO()
            with contextlib.redirect_stdout(out):
                code = main(["--rev", measured, "--fetch"])
            lines = out.getvalue().splitlines()
            check("main: the satisfying world exits 0", code, 0)
            check("main: the exact summary line is the first line",
                  lines[0], good_line)
            check("main: the second line names the counter and the rev",
                  lines[1], "counter sha256 %s; rev %s" % (self_sha(), measured))
            check("main: no reject line for a found row",
                  [l for l in lines
                   if l.startswith("reject Claude Code")
                   or l.startswith("reject Gemini CLI")], [])
            run_curl = live_404
            out = io.StringIO()
            with contextlib.redirect_stdout(out):
                code = main(["--rev", measured, "--fetch"])
            lines = out.getvalue().splitlines()
            check("main: an HTTP 404 drops F to 0 and exits 1", code, 1)
            check("main: an HTTP 404 keeps S at 2 and F at 0", lines[0],
                  "hook files backed on committed snapshots 2 of 2; "
                  "found on the live page 0 of 2; new ground 0")
            check("main: the 404 is reported on the reject line",
                  "reject Claude Code: live fetch failed: HTTP 404 at "
                  "https://code.claude.com/docs/en/hooks.md" in lines, True)
            run_curl = live_down
            out = io.StringIO()
            with contextlib.redirect_stdout(out):
                code = main(["--rev", measured, "--fetch"])
            lines = out.getvalue().splitlines()
            check("a curl failure drops F while S holds", code, 1)
            check("a curl failure keeps S at 2 and F at 0", lines[0],
                  "hook files backed on committed snapshots 2 of 2; "
                  "found on the live page 0 of 2; new ground 0")
            check("a curl failure names the backed rows",
                  ("reject Claude Code: live fetch failed: curl exited 6" in lines,
                   "reject Gemini CLI: live fetch failed: curl exited 6" in lines),
                  (True, True))
            run_curl = live_ok
            TARGET, NEW_TARGET = None, None
            out = io.StringIO()
            with contextlib.redirect_stdout(out):
                code = main(["--rev", measured, "--fetch"])
            lines = out.getvalue().splitlines()
            check("the unfrozen sentinel is a 1, never a 0", code, 1)
            check("the unfrozen sentinel still prints the summary",
                  lines[0], good_line)
            check("the unfrozen sentinel is named",
                  "targets not frozen" in lines, True)
            TARGET, NEW_TARGET = 2, 2
            out = io.StringIO()
            with contextlib.redirect_stdout(out):
                code = main(["--rev", measured])
            lines = out.getvalue().splitlines()
            check("without --fetch the summary reads 'live not run' and G is 0",
                  lines[0],
                  "hook files backed on committed snapshots 2 of 2; "
                  "live not run; new ground 0")
            check("without --fetch the predicate is 1", code, 1)
            out, err = io.StringIO(), io.StringIO()
            with contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
                code = main(["--rev", base_sha, "--fetch"])
            check("a revision without SKILL.md exits 2", code, 2)
            check("a revision without SKILL.md is named",
                  "SKILL.md is missing" in err.getvalue(), True)
            (repo / "corpus" / "lessons" / "round-59.md").write_text(
                lesson.replace("PreToolUse hook", "PreToolUse directive"),
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
            check("the broken world exits 1", code, 1)
            check("the broken world prints the one-of-two line", lines[0],
                  "hook files backed on committed snapshots 1 of 2; "
                  "found on the live page 1 of 2; new ground 1")
            check("the broken world names the Gate on the reject line",
                  "reject Claude Code: entry row S900: round-59 Gate does not "
                  "record this quote" in lines, True)
        finally:
            BASE, TARGET, NEW_TARGET, lane_dir, run_curl = saved

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
        sha = self_sha()
    except OSError as e:
        print("could-not-evaluate: cannot read own bytes: %s" % e, file=sys.stderr)
        return 2
    if args.self_test:
        if args.rev or args.fetch or args.json:
            ap.error("--self-test cannot be combined with --rev, --fetch or --json")
        print("counter sha256 %s" % sha)
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
        skill = git_show(lane, args.rev, SKILL)
        if skill is None:
            raise EnvError("%s is missing at %s" % (SKILL, args.rev))
        entry = git_show(lane, args.rev, ENTRY) or ""
        sources = git_show(lane, args.rev, SOURCES) or ""
        lesson = git_show(lane, args.rev, LESSON) or ""
        base_sources = git_show(lane, BASE, SOURCES) or ""
        report = judge(skill, entry, sources, lesson, base_sources,
                       snapshot_of=lambda sid: git_show_bytes(
                           lane, args.rev, snapshot_path(sid)))
    except (EnvError, UnicodeDecodeError, OSError) as e:
        print("could-not-evaluate: %s" % e, file=sys.stderr)
        return 2
    backed = [r for r in report if r["backed"]]
    k = sum(1 for r in report if r["in_k"])
    found = 0
    if args.fetch:
        base_urls = base_url_keys(base_sources)
        for r in backed:
            try:
                page = fetch(r["url"], HOSTS[r["client"]], base_urls)
                reasons = page_why(page, r["quote"], r["token"], r["events"])
                r["found"] = not reasons
                r["live_why"] = ["live page: " + x for x in reasons]
            except Exception as e:  # network, status, pin or decode failure
                r["found"] = False
                r["live_why"] = ["live fetch failed: %s" % e]
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
    print(summary_line(args.fetch, len(backed), k, found, ground))
    print("counter sha256 %s; rev %s" % (sha, args.rev))
    for r in report:
        if args.fetch:
            if r["backed"] and r.get("found"):
                continue
            print(reject_line(r["client"], r["why"] + r.get("live_why", [])))
        elif not r["backed"]:
            print(reject_line(r["client"], r["why"]))
    if args.json:
        print(json.dumps({"backed": len(backed), "of": k, "found": found,
                          "new_ground": ground, "target": TARGET,
                          "new_target": NEW_TARGET, "clients": report}, indent=1))
    if TARGET is None or NEW_TARGET is None:
        print("targets not frozen")
    return predicate(args.fetch, found, ground)


if __name__ == "__main__":
    sys.exit(main())
