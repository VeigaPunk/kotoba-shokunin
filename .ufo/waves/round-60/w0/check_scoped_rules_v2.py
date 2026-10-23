#!/usr/bin/env python3
r"""check_scoped_rules.py -- frozen counter for the round-60 C1 claim.

Derived from `check_hook_files.py` (round 59, sha256 `f695d59e...`): the HOSTS
map, MARKERS, the SOURCES row parsing, the URL normalisation, the tracker and
change-note rejection, the `## Gate` quote requirement, the token grammar's
shape, the page normalisation and the fetch limits are that counter's
behaviour, unchanged.  Everything named below is the round-60 change.  Each
named change only replaces one rule; none loosens a rule that still applies.

Round 60, claim C1 (axis: depth, the learning claim; sourced): `SKILL.md`
gains a decision table, `### Scoped rule files by client`, that tells a reader,
per client, the file or folder its own documentation names for a RULE
(instruction) file that applies only when the agent works on matching files,
the frontmatter key that names the matching paths, and what a rule author does
with it -- scope a rule to the files it is about instead of loading it every
turn.  Each row is grounded in a new knowledge entry,
`corpus/knowledge/scoped-rules-round60.md`, whose per-client record quotes the
client's own documentation from a `corpus/SOURCES.md` row opened on
2026-10-23, and whose quote the client's own committed page snapshot carries.

This file implements the round-60 plan INCLUDING amendment A1 (pre-freeze
tightening): the Scope-key conjunct is the KEY FORM ONLY -- the table-cell form
and the glob/pattern-word alternative are removed -- and the Action conjunct
requires |W| >= 3 distinct content words with at least max(2, ceil(|W|/2)) of
them on the cited line.

Round-60 erratum E1 (v2, pre-data, after the freeze): the control wave and the
w0b re-census showed the v1 base-URL conjunct rejecting every eligible page but
VS Code, because round-59 SOURCES rows already hold those URLs.  v2 changes
ONLY that conjunct: a base-keyed URL is accepted when the row RE-OPENS the base
row -- its SOURCES `teaches` cell starts with `re-opens S### —`, S### is a BASE
row whose own URL cell holds that URL, and the client's scope key K does not
occur (identifier boundary, case-sensitive) anywhere in that base row's line --
and the live fetch accepts a final URL on a base key only when it is the row's
own (re-opened) key.  The A1 conjuncts, the token grammar, the quote rule, the
snapshot pin and the target are unchanged.

The seven clients, the hosts allowed for each client's source, the table
anchors, the token grammar, the two semantic conjuncts, the word bounds, the
opened date, the base revision and the target are pinned here and never read
from the revision measured.  A later change to any of them is a second
measurement, never the declared one (corpus/QUALITY.md Q28).  `TARGET` is the
freeze record's value; with `TARGET` set to `None` the predicate returns 1 and
still prints its output (never 0).

THE FROZEN SPEC (this file implements it; it is not read from the tree):

  BASE_REV = 31092dc6f875370bddd6eb1e4da4ca0d210c56af
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
  TARGET   = 3 (the plan's freeze record; None would make the predicate 1)
  OPENED   = 2026-10-23

  SKILL.md at the measured revision: a section whose heading line is exactly
  `### Scoped rule files by client`; its FIRST table has the header
  `| Client | Rule files | Scope key | Action |`.  One row per client name
  (exact match to CLIENTS; a duplicate client row disqualifies that client).
  The rule token is the FIRST backticked span of the Rule files cell.  The
  Scope key cell leads with a backticked key K.

  THE C1 ROW RULE (fixed in `plans/round-60.md` section C1, as amended by A1
  before the freeze): a client counts when its OWN documentation, on its pinned
  host, names a file or folder for a RULE (instruction) file that applies only
  when the agent works on matching files, as a token that -- after stripping
  one leading `~/` or `./` -- has >= 2 path segments and a first segment
  starting with `.`; no segment (split on `-`, `.`, `_`) equal
  (case-insensitive) to skill/skills/agent/agents/command/commands/prompt/
  prompts/plugin/plugins/extension/extensions/hook/hooks -- `rule`, `rules` and
  `instructions` are ALLOWED, this is the rule-file table; no dot inside a
  non-final segment except as its first character (E7); and no OTHER client's
  marker in the token.  E5 is DROPPED: two rows may share a token (VS Code and
  Copilot CLI may both document `.github/instructions/**/*.instructions.md`)
  when each row is backed on its own client's pinned host; a token copied into
  a row whose own host does not back it still fails the host pin and the quote.

  A token is well-formed iff it matches
  `^(~/|\./)?[A-Za-z0-9_.-]+(/[A-Za-z0-9_.*-]+)*/?$`
  AND, after stripping one leading `~/` or `./` and one trailing `/`, it has at
  least two path segments and its first segment starts with `.`
  AND no segment, split on `-`, `.` and `_`, holds a word EQUAL
  case-insensitively to one of `skill`, `skills`, `agent`, `agents`,
  `command`, `commands`, `prompt`, `prompts`, `plugin`, `plugins`,
  `extension`, `extensions`, `hook`, `hooks`
  AND (E7) no non-final segment holds a dot other than as its first character.
  A directory token (a trailing `/`) IS allowed, and a glob `*` is allowed.

    well-formed:  .claude/rules/, .claude/rules/*.md, .cursor/rules/*.mdc,
                  .github/instructions/, .github/instructions/**/*.instructions.md
    not:          .claude/hooks/ (a hook word), .claude (one segment),
                  rules (one segment), claude/rules/ (first segment not
                  dot-led), .claude/skills/rules.md, .claude/1.0/rules.md (E7)

  FOREIGN-NAME GUARD (kept): the client markers are Claude Code `claude`,
  Codex `codex`, VS Code `vscode`, Copilot CLI `copilot`, Gemini CLI `gemini`,
  Cursor `cursor`, opencode `opencode`.  A token whose lower-cased text
  contains ANOTHER client's marker is rejected for that client.

  normalise(token) = strip one leading `~/` or `./`, strip one trailing `/`;
  case is PRESERVED.
  K = the number of client rows with a well-formed token.

  SCOPE KEY (A1, the semantic conjunct, the point of this round).  The first
  backticked span K of the Scope key cell must match
  `^[A-Za-z][A-Za-z0-9_-]*$` and be cited as `S### :L` (the row's own source
  id; `S###:L` also accepted).  On line L of the committed snapshot K must
  stand in KEY FORM:

    * K at an identifier boundary, followed (after an optional closing `"`,
      `'` or backtick and optional spaces) by `:` or `=`;
    * its VALUE V is the rest of line L after that `:`/`=`.  When V is empty
      or only `[`, `|` or `>`, V is the FIRST nonblank line among the next 3
      lines, and that line must begin (after spaces) with `-` or a quote;
    * after stripping leading `-`, `[`, quotes and spaces, the FIRST token of V
      (up to whitespace, a comma or a closing quote/bracket) must contain `*`
      and consist only of `[A-Za-z0-9_./*{},!-]`.

  The table-cell form and the glob/pattern-word alternative are REMOVED.  A
  printed name that is not the scoping key (`description`, `name`,
  `alwaysApply`, a product name) fails: `description: "Applies to **/*.ts"`
  has first token `Applies`, and `description: RPC service conventions and
  patterns` has first token `RPC`.

  ACTION (A1, the second semantic conjunct).  W = the distinct content words
  of the cell (lowercase `[a-z]{4,}` runs outside backticks and `S### :L`
  citations, minus the pinned STOPWORDS below).  |W| >= 3 AND at least
  max(2, ceil(|W|/2)) of W occur on the cited line of the same snapshot.  A
  cell that is not cited, or shares too little with its line, fails.

  Entry `corpus/knowledge/scoped-rules-round60.md` at the measured revision:
  its first table with the header `| Client | Rule files | Source | Quote |`.
  The source cell holds one `S###` id; the quote cell holds the verbatim quote
  (one pair of surrounding straight or curly double quotes is stripped;
  backticks are stripped for word counting and for matching); the Rule files
  cell, backticks stripped, must equal the SKILL.md token or its normalise()d
  form (E4).

  SNAPSHOT `.ufo/waves/round-60/snapshots/<S###>.page` must exist at the
  measured revision, read with `git show <rev>:<path>` as bytes (never from
  the working tree); its sha256 must equal the FIRST `sha256 <64 hex>` printed
  anywhere in that source's SOURCES row (a row printing no full 64-hex sha256
  blocks the row); and the snapshot's text must carry the quote and satisfy
  both semantic conjuncts.

  A client is BACKED iff all of:
    * its SKILL.md row is unique and its token well-formed;
    * the token is not foreign to the client (FOREIGN-NAME GUARD);
    * an entry row names it, and (E4) its `Rule files` cell equals the token
      or normalise(token);
    * the quote holds 6 to 25 words;
    * the quote CONTAINS the raw token or its normalise()d form,
      CASE-SENSITIVE, at path-segment boundaries;
    * the quote matches `(?i)\b(rules?|instructions?)\b` OUTSIDE that token's
      span -- the word rule/rules inside the token does not count;
    * the cited `S###` is a row of `corpus/SOURCES.md` at the measured
      revision and its id is NOT a row at BASE_REV.  Its URL -- normalised by
      the round-56 v1.3 `url_key` -- may be the normalised URL of a BASE_REV row
      only as a RE-OPEN (erratum E1): the row's SOURCES `teaches` cell starts
      with `re-opens S### —`, S### is a BASE_REV row whose own URL cell holds
      that URL, and this client's scope key K does not occur (identifier
      boundary, case-sensitive) anywhere in that base row's line.  A base URL
      without such a re-open keeps the v1 rejection plus `re-open names no base
      row with this URL` or `base row S### already records key K`;
    * that row has kind `docs`, tier `A`, status `mined`, and opened
      `2026-10-23`;
    * the row's URL host is pinned for that client (host_ok);
    * (E3) the row's URL path, percent-decoded, contains none of `changelog`,
      `release`, `releases`, `news`, `blog` (case-insensitive), and is not an
      issue/PR/discussion/commit page;
    * the quote, whitespace-normalised, occurs in `corpus/lessons/round-60.md`
      section `## Gate` at the measured revision;
    * the SNAPSHOT check above passes, including the SCOPE KEY and ACTION
      conjuncts on it.

  With `--fetch`, a BACKED client is FOUND iff the live page at the row URL
  carries the quote and a KEY-FORM SITE for K at ANY line.  The page is read
  with `curl -sSL --max-time 30 -A <browser UA> -H "Accept: text/markdown,
  text/plain;q=0.9, */*;q=0.8" -w "\n%{http_code} %{url_effective}"`, up to 3
  attempts, with HTTP 200 required; the URL reached after redirects must still
  be on the client's pinned hosts, must not be a BASE_REV SOURCES URL other
  than the row's own (re-opened) key, must not be an E3 change-note URL, and
  the body must stay under 5 MiB.

  Output: the FIRST line is the summary
  `scoped rule files backed on committed snapshots S of K; found on the live
  page F of K` with `--fetch`, and `scoped rule files backed on committed
  snapshots S of K; live not run` without it (F = 0).  The SECOND line is
  `counter sha256 <hex>; rev <rev>`, the sha256 of this file's own bytes read
  from `__file__` (never from a pipe).  Then one `reject <client>: <reasons>`
  line per non-found row: without `--fetch` a row is non-found when it is not
  backed; with `--fetch` a row is non-found when it is not backed or its live
  page failed, and the reasons then include the live failure.  A `target not
  frozen` line follows the rejects while TARGET is `None`.

  Exit codes: with a frozen target and `--fetch`, 0 iff F >= TARGET, else 1;
  without `--fetch`, always 1 (the non-fetch run is not the predicate); with
  TARGET `None`, always 1 (never 0, and the output is still printed); 2 =
  could not evaluate (a `--rev` that is not a full 40-hex hash, a revision
  that is not a commit, a git failure, a SKILL.md missing at the revision, an
  unreadable file) with no traceback.

THE FROZEN PREDICATE (verbatim, and the receipt label):

  `python3 -B verifiers/check_scoped_rules.py --rev <rev> --fetch` exits 0
  iff it prints `scoped rule files backed on committed snapshots S of K;
  found on the live page F of K` with F >= TARGET;
  receipt label `C1 predicate: --fetch exit 0 (F>=TARGET)`.

The counter reads the measured revision with read-only git (`git -C <lane>
show <rev>:<path>`), never from the working tree; the lane is the parent of
the script's `verifiers/` directory.

Usage:
  python3 -B verifiers/check_scoped_rules.py --rev <rev> [--fetch] [--json]
  python3 -B verifiers/check_scoped_rules.py --self-test
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

BASE = "31092dc6f875370bddd6eb1e4da4ca0d210c56af"
SKILL = "SKILL.md"
ENTRY = "corpus/knowledge/scoped-rules-round60.md"
SOURCES = "corpus/SOURCES.md"
LESSON = "corpus/lessons/round-60.md"
SNAPSHOT_DIR = ".ufo/waves/round-60/snapshots"
TARGET = 3
MIN_WORDS = 6
MAX_WORDS = 25
MIN_CONTENT = 3
MIN_SHARED = 2
OPENED = ("2026-10-23",)
MAX_BYTES = 5 * 1024 * 1024
FETCH_TIMEOUT = 30
FETCH_ATTEMPTS = 3
LANE_FALLBACK = Path("/home/vgpnk/Projects/shokunin/kotoba-shokunin")
RECEIPT = "C1 predicate: --fetch exit 0 (F>=TARGET)"
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
SKILL_HEADING = "### Scoped rule files by client"
SKILL_HEADER = ("client", "rule files", "scope key", "action")
ENTRY_HEADER = ("client", "rule files", "source", "quote")
REV_RE = re.compile(r"^[0-9a-fA-F]{40}$")
TOKEN_RE = re.compile(r"^(~/|\./)?[A-Za-z0-9_.-]+(/[A-Za-z0-9_.*-]+)*/?$")
SEG_SPLIT_RE = re.compile(r"[-._]")
NOT_RULE_WORDS = frozenset(("skill", "skills", "agent", "agents", "command",
                            "commands", "prompt", "prompts", "plugin", "plugins",
                            "extension", "extensions", "hook", "hooks"))
BACKTICK_RE = re.compile(r"`([^`]+)`")
SID_RE = re.compile(r"^`?(S\d{3,})`?$")
URL_RE = re.compile(r"https?://[^\s)>\]`]+")
SOURCES_ROW_RE = re.compile(r"^\|[ \t]*S[0-9]{3,}[ \t]*\|")
RULE_WORD_RE = re.compile(r"\b(rules?|instructions?)\b", re.IGNORECASE)
SHA256_RE = re.compile(r"sha256[\s`*:=\[]*([0-9a-fA-F]{64})(?![0-9a-fA-F])")
SEPARATOR_RE = re.compile(r":?-{3,}:?")
KEY_IDENT_RE = re.compile(r"^[A-Za-z][A-Za-z0-9_-]*$")
KEY_SUFFIX_RE = re.compile(r"""["'`]?[ \t]*[:=]""")
VALUE_ONLY_RE = re.compile(r"[ \t\[\|>]*")
VALUE_STRIP = "-[\"'` \t"
PATTERN_TOKEN_RE = re.compile(r"^[A-Za-z0-9_./*{},!-]+$")
CITE_RE = re.compile(r"(S\d{3,})\s*:\s*(\d+)")
# Erratum E1: the SOURCES `teaches` prefix that re-opens a base row.  The em
# dash is the recorded spelling; `\u2013`, `--` and `-` are accepted as the same
# separator so an encoding rewrite of the cell does not change the verdict.
REOPEN_RE = re.compile(r"^re-opens\s+(S\d{3,})\s*(?:\u2014|\u2013|--|-)")
CONTENT_RE = re.compile(r"[a-z]{4,}")
IDENT = frozenset(string.ascii_letters + string.digits + "_")
TOKEN_CUT = frozenset(" \t\r\v\f,\"'`])}>")
BOUNDARY_PREV = frozenset(" \t\r\n`\"'([")
TRIM_CHARS = ".,;:!?)]}'\""
ASCII_ALNUM = frozenset(string.ascii_letters + string.digits)
CURL_UA = ("Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like "
           "Gecko) Chrome/130.0 Safari/537.36")
CURL_ACCEPT = "text/markdown, text/plain;q=0.9, */*;q=0.8"
CURL_WRITE_OUT = "\n%{http_code} %{url_effective}"
# Pinned in the counter, never read from the row: the Action conjunct compares
# the cell with its cited snapshot line on the lowercase [a-z]{4,} words that
# remain after these are dropped.  Function words and light verbs only; a
# domain word ("scope", "files", "pattern", "rule") is never listed, because
# dropping it would let an invented action share words with any English line.
STOPWORDS = frozenset((
    "about", "above", "after", "again", "against", "also", "always", "among",
    "another", "because", "been", "before", "being", "below", "between",
    "both", "cannot", "could", "does", "doing", "down", "during", "each",
    "either", "else", "even", "ever", "every", "from", "further", "have",
    "having", "here", "into", "itself", "just", "like", "many", "more",
    "most", "much", "must", "need", "never", "only", "other", "otherwise",
    "over", "same", "shall", "should", "since", "some", "such", "than",
    "that", "their", "them", "then", "there", "these", "they", "this",
    "those", "through", "thus", "under", "until", "upon", "very", "what",
    "when", "where", "whether", "which", "while", "will", "with", "within",
    "without", "would", "your", "yours",
))


class EnvError(Exception):
    """Could not evaluate: unknown revision, git failure, unreadable file."""


# ---------------------------------------------------------------- lane access

def lane_dir() -> Path:
    """The lane repository: the parent of the script's `verifiers/` directory.

    Integrated in the lane the script sits in `<lane>/verifiers/`, so the lane
    is its parent.  A copy kept outside the lane (a sandbox clone, a wave
    directory) is found by walking up for the lane markers; the lane checkout
    itself is the last resort.  The path is never taken from the environment."""
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
    """Rows of the FIRST table of the `### Scoped rule files by client` section.

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


def base_line_map(text: str) -> dict[str, str]:
    """id -> the raw SOURCES.md line of that row (the re-open key test reads it)."""
    out: dict[str, str] = {}
    for ln in text.splitlines():
        if SOURCES_ROW_RE.match(ln):
            out[ln.split("|")[1].strip()] = ln
    return out


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
    """A URL whose decoded path contains a change-note word (substring,
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
    """The round-60 token grammar: a RULE (instruction) file or folder.

    TOKEN_RE first, then, after stripping one leading `~/` or `./` and one
    trailing `/`: at least two path segments, the first segment dot-led, no
    segment holding a skill/agent/command/prompt/plugin/extension/hook word in
    ANY segment (the final one included; `rule`, `rules` and `instructions` are
    allowed), and (E7) no non-final dot except as a segment's first character.
    A directory token is allowed, and so is a glob."""
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
    return not any(w in NOT_RULE_WORDS for seg in parts for w in seg_words(seg))


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
        left_ok = i == 0 or text[i - 1] in BOUNDARY_PREV
        if left_ok and right_ok:
            return i
        start = i + 1


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


def rule_word_outside(text: str, start: int, end: int) -> bool:
    """Is there a whole rule/rules/instruction/instructions word outside the
    token span?  The plural of each is the word; `rulebook` is not."""
    for m in RULE_WORD_RE.finditer(text):
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


# --------------------------------------------------- the two semantic conjuncts

def scope_key(cell: str) -> tuple[str | None, list[str]]:
    """The Scope key cell's leading backticked key, or the reason it has none.

    The FIRST backticked span is the key; it must be a bare identifier
    (`^[A-Za-z][A-Za-z0-9_-]*$`), never a glob or a sentence."""
    spans = BACKTICK_RE.findall(cell)
    if not spans:
        return None, ["SKILL.md scope key cell holds no backticked key"]
    k = spans[0].strip()
    if not KEY_IDENT_RE.match(k):
        return None, ["SKILL.md scope key %r is not a bare identifier "
                      "matching ^[A-Za-z][A-Za-z0-9_-]*$" % k]
    return k, []


def citations(cell: str) -> list[tuple[str, int]]:
    """Every `S### :L` / `S###:L` citation in a cell, in printed order."""
    return [(m.group(1), int(m.group(2))) for m in CITE_RE.finditer(cell)]


def citation_why(cell: str, sid: str | None, what: str) -> tuple[int | None, list[str]]:
    """The line L a cell cites for its OWN source row, or the reason it does not."""
    cites = citations(cell)
    if sid:
        own = [n for s, n in cites if s == sid]
        if own:
            return own[0], []
        if cites:
            return None, ["%s cites %s, not the row's own source %s"
                          % (what, ", ".join("%s :%d" % c for c in cites), sid)]
        return None, ["%s carries no `S### :L` citation" % what]
    return None, []


def key_occurrences(line: str, key: str) -> list[tuple[int, int]]:
    """(i, j) for every case-sensitive `key` at an IDENTIFIER boundary.

    A key inside `xpaths` or followed by `Extra` is not a key: both neighbours
    must be outside `[A-Za-z0-9_]`."""
    out: list[tuple[int, int]] = []
    if not key:
        return out
    start = 0
    while True:
        i = line.find(key, start)
        if i < 0:
            return out
        j = i + len(key)
        left_ok = i == 0 or line[i - 1] not in IDENT
        right_ok = j >= len(line) or line[j] not in IDENT
        if left_ok and right_ok:
            out.append((i, j))
        start = i + 1


def first_value_token(text: str) -> str:
    """The first token of a key's value: after stripping leading `-`, `[`,
    quotes and spaces, up to whitespace, a comma or a closing quote/bracket."""
    out: list[str] = []
    for ch in text.lstrip(VALUE_STRIP):
        if ch in TOKEN_CUT:
            break
        out.append(ch)
    return "".join(out)


def pattern_value(text: str) -> bool:
    """Is the first token of this value a path pattern?

    It must contain `*` and consist only of `[A-Za-z0-9_./*{},!-]`."""
    tok = first_value_token(text)
    return "*" in tok and PATTERN_TOKEN_RE.match(tok) is not None


def block_only(rest: str) -> bool:
    """Is this key value empty or only `[`, `|` or `>` (a block value)?"""
    return VALUE_ONLY_RE.fullmatch(rest) is not None


def value_after(lines: list[str], L: int, rest: str) -> str | None:
    """The value of a key form: the rest of line L, or its block line.

    When the rest is empty or only `[`, `|` or `>`, the value is the FIRST
    nonblank line among the next 3, and that line must begin (after spaces)
    with `-` or a quote; any other first nonblank line leaves no value."""
    if not block_only(rest):
        return rest
    for line in lines[L:L + 3]:
        if not line.strip():
            continue
        return line if line.lstrip().startswith(("-", '"', "'", "`")) else None
    return None


def key_site(lines: list[str], L: int, key: str | None) -> bool:
    """Does line L hold `key` in KEY FORM with a path pattern as its value?

    A1: the key form (`K:` / `K=`, after an optional closing quote/backtick and
    spaces) is required, and its first value token must contain `*`.  There is
    no table-cell form and no glob/pattern-word alternative."""
    if not key or L < 1 or L > len(lines):
        return False
    line = lines[L - 1]
    for _i, j in key_occurrences(line, key):
        m = KEY_SUFFIX_RE.match(line, j)
        if m is None:
            continue
        v = value_after(lines, L, line[m.end():])
        if v is not None and pattern_value(v):
            return True
    return False


def any_key_site(text: str, key: str | None) -> bool:
    """A key-form site for `key` at any line of the page (the live-page check)."""
    lines = text.splitlines()
    for n in range(1, len(lines) + 1):
        if key_site(lines, n, key):
            return True
    return False


def content_words(text: str) -> set[str]:
    """The cell's content words: lowercase `[a-z]{4,}` runs outside backticks
    and `S### :L` citations, minus the pinned STOPWORDS."""
    t = BACKTICK_RE.sub(" ", text)
    t = CITE_RE.sub(" ", t)
    return {w for w in CONTENT_RE.findall(t.lower()) if w not in STOPWORDS}


def action_need(n_content: int) -> int:
    """The Action conjunct's threshold: max(2, ceil(|W| / 2))."""
    return max(MIN_SHARED, (n_content + 1) // 2)


def action_conjunct(lines: list[str], cell: str, L: int | None) -> list[str]:
    """Every reason the Action cell and its cited snapshot line disagree.

    A1: |W| >= 3 distinct content words, and at least max(2, ceil(|W|/2)) of W
    on the cited line."""
    if L is None or not cell:
        return []
    if L < 1 or L > len(lines):
        return ["snapshot has no line %d for the action citation" % L]
    w = content_words(cell)
    if len(w) < MIN_CONTENT:
        return ["action cell holds %d distinct content word(s) (need >= %d)"
                % (len(w), MIN_CONTENT)]
    need = action_need(len(w))
    shared = w & content_words(lines[L - 1])
    if len(shared) < need:
        return ["action cell shares %d of its %d content word(s) with line %d "
                "(need >= %d)" % (len(shared), len(w), L, need)]
    return []


def scope_conjunct(lines: list[str], key: str | None, L: int | None) -> list[str]:
    """Every reason the cited snapshot line is not a key site for the key."""
    if L is None or not key:
        return []
    if L < 1 or L > len(lines):
        return ["snapshot has no line %d for scope key %r" % (L, key)]
    if not key_site(lines, L, key):
        return ["scope key %r is not in key form with a path pattern at line %d"
                % (key, L)]
    return []


# ------------------------------------------------------------------- the judge

def rule_cell_matches(cell: str, token: str) -> bool:
    """E4: the entry `Rule files` cell, backticks stripped, IS the SKILL.md
    token or its normalise()d form (exact, case-sensitive)."""
    return cell.replace("`", "").strip() in (token, normalise(token))


def page_plain(s: str) -> str:
    """The v1.3 `_plain` without its final lower-casing: case is preserved."""
    s = html.unescape(s)
    s = re.sub(r"[`*_]", "", s)
    s = s.replace("\u2019", "'").replace("\u201c", '"').replace("\u201d", '"')
    return re.sub(r"\s+", " ", s).strip()


def norm(s: str) -> str:
    """Quote side: `page_plain` then lower-case; no angle-bracket text removed."""
    return page_plain(s).lower()


def norm_page(s: str) -> str:
    """Page side: script/style bodies, comments and tags dropped; `_plain`
    then lower-case."""
    s = re.sub(r"(?is)<(style|script)\b.*?</\1\s*>", " ", s)
    s = re.sub(r"(?s)<!--.*?-->", " ", s)
    s = re.sub(r"</?[A-Za-z][^>]*>", " ", s)
    return page_plain(s).lower()


def quote_why(page_text: str, quote: str) -> list[str]:
    """Why the page does not carry the quote (the round-58 quote check)."""
    if not quote or norm(quote) not in norm_page(page_text):
        return ["the quote is not on the page"]
    return []


def live_why(page_text: str, quote: str, key: str | None) -> list[str]:
    """Why the live page does not carry the quote and a key-form site for K."""
    why = quote_why(page_text, quote)
    if key and not any_key_site(page_text, key):
        why.append("no key-form site for %r on the page" % key)
    return why


def reopen_why(row: list[str], url: str, key: str | None,
               base_rows: dict[str, list[str]],
               base_lines: dict[str, str]) -> list[str]:
    """Every reason a base-keyed URL is not accepted as a re-open (v2).

    The row's SOURCES `teaches` cell must START with `re-opens S### —`, S### must
    be a row of the BASE SOURCES table (so it is in `at_base` by construction)
    whose own URL cell holds this URL, and this client's scope key K must not
    occur (identifier boundary, case-sensitive) in that base row's line.  Empty
    means the re-open is accepted."""
    cell = row[6] if len(row) > 6 else ""
    m = REOPEN_RE.match(cell)
    if not m:
        return ["re-open names no base row with this URL"]
    target = m.group(1)
    base = base_rows.get(target)
    if not base:
        return ["re-open names no base row with this URL"]
    if url_key(url) not in {url_key(u) for u in urls_of(base[1])}:
        return ["re-open names no base row with this URL"]
    if key and key_occurrences(base_lines.get(target, ""), key):
        return ["base row %s already records key %s" % (target, key)]
    return []


def entry_row_verdict(er: list[str], client: str, token: str | None,
                      table: dict[str, list[str]], at_base: set[str],
                      base_urls: set[str], base_rows: dict[str, list[str]],
                      base_lines: dict[str, str], gate_raw: str, gate_plain: str,
                      scope_cell: str, action_cell: str,
                      snapshot_of=None) -> tuple[list[str], dict]:
    """Judge one entry row.  Returns (why, picked) where `picked` carries the
    row's sid, url, quote, scope key and key line.

    A malformed token has already been rejected on the SKILL.md side, so the
    entry row only looks for a token span when a token was read at all."""
    why: list[str] = []
    sid = url = quote = key = None
    key_line: int | None = None
    if token and not rule_cell_matches(er[1], token):
        why.append("entry Rule files cell %r is not the SKILL.md token %r"
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
            why.append("quote does not hold the rule token %r (case-sensitive)"
                       % token)
        elif not rule_word_outside(q_plain, span[0], span[1]):
            why.append("quote holds no rule/instruction word outside the token")
    if not quote_in_gate(quote, gate_raw, gate_plain):
        why.append("round-60 Gate does not record this quote")
    key, key_why = scope_key(scope_cell)
    why.extend(key_why)
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
                    reopen = reopen_why(s, url, key, base_rows, base_lines)
                    if reopen:
                        why.append("%s URL %r is already a base SOURCES URL"
                                   % (sid, url))
                        why.extend(reopen)
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
                        lines = page.splitlines()
                        for reason in quote_why(page, quote):
                            why.append("snapshot %s: %s" % (snapshot_path(sid), reason))
                        key_line, cite_why = citation_why(scope_cell, sid,
                                                          "SKILL.md scope key cell")
                        why.extend(cite_why)
                        for reason in scope_conjunct(lines, key, key_line):
                            why.append("snapshot %s: %s" % (snapshot_path(sid), reason))
                        action_line, cite_why = citation_why(action_cell, sid,
                                                             "SKILL.md action cell")
                        why.extend(cite_why)
                        for reason in action_conjunct(lines, action_cell, action_line):
                            why.append("snapshot %s: %s" % (snapshot_path(sid), reason))
    return why, {"row": sid, "url": url, "quote": quote, "key": key,
                 "key_line": key_line}


def judge(skill: str, entry: str, sources: str, lesson: str,
          base_sources: str, snapshot_of=None) -> list[dict]:
    srows = skill_rows(skill)
    erows = entry_rows(entry)
    table = sources_table(sources)
    at_base = source_ids(base_sources)
    base_urls = base_url_keys(base_sources)
    base_rows = sources_table(base_sources)
    base_lines = base_line_map(base_sources)
    gate = gate_section(lesson)
    gate_raw = ws(gate)
    gate_plain = ws(gate.replace("`", ""))
    report = []
    for client in CLIENTS:
        why: list[str] = []
        token = None
        norm_tok = ""
        in_k = False
        scope_cell = action_cell = ""
        smine = [r for r in srows if client_name(r[0]) == client]
        if len(smine) != 1:
            why.append("SKILL.md rows naming client: %d (need exactly 1)" % len(smine))
        else:
            sr = ((smine[0] if smine else []) + ["", "", "", ""])[:4]
            scope_cell, action_cell = sr[2], sr[3]
            spans = BACKTICK_RE.findall(sr[1])
            token = spans[0] if spans else None
            if token is None:
                why.append("SKILL.md rule-files cell holds no backticked token")
            elif not token_well_formed(token):
                why.append("SKILL.md rule token %r is not well-formed" % token)
            else:
                norm_tok = normalise(token)
                in_k = True
                other = foreign_marker(client, token)
                if other:
                    why.append("SKILL.md rule token %r carries %s's marker %r"
                               % (token, other, MARKERS[other]))
        emine = [(r + ["", "", "", ""])[:4] for r in erows if client_name(r[0]) == client]
        picked = None
        row_whys = []
        for er in emine:
            row_why, got = entry_row_verdict(
                er, client, token, table, at_base, base_urls, base_rows,
                base_lines, gate_raw, gate_plain, scope_cell, action_cell,
                snapshot_of)
            if not row_why:
                picked = got
                break
            row_whys.append("entry row %s: %s" % (er[2].strip() or "-", "; ".join(row_why)))
        if not emine:
            why.append("no entry row names the client")
        elif picked is None:
            why.extend(row_whys)
        got = picked or {}
        report.append({"client": client,
                       "row": got.get("row"),
                       "url": got.get("url"),
                       "quote": got.get("quote"),
                       "key": got.get("key"),
                       "key_line": got.get("key_line"),
                       "token": token, "norm": norm_tok, "in_k": in_k,
                       "backed": not why, "why": why})
    return report


# ------------------------------------------------------------------ the fetch

def curl_argv(url: str) -> list[str]:
    """The frozen curl invocation: `-sSL`, a 30 s cap, browser User-Agent and
    `Accept` (round-58 routed defect R3: the page is served differently to a
    bot User-Agent), and curl's own write-out trailer as the last word."""
    return ["curl", "-sSL", "--max-time", str(FETCH_TIMEOUT),
            "-A", CURL_UA,
            "-H", "Accept: " + CURL_ACCEPT,
            "-w", CURL_WRITE_OUT, url]


def run_curl(url: str) -> tuple[int, str, bytes]:
    """One curl GET: (HTTP status, effective URL, body).

    The status and the URL after redirects come from curl's own write-out
    trailer, never from the body."""
    try:
        r = subprocess.run(curl_argv(url), capture_output=True)
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
          base_keys: set[str] | None = None,
          own_key: str | None = None) -> str:
    """curl GET, 30 s cap, at most 5 MiB, three attempts, HTTP 200 required.

    When `pins` is given, the URL reached after redirects must still be on the
    client's pinned hosts; when `base_keys` is given, a page whose URL after
    redirects is a base SOURCES URL is not found UNLESS that key is the row's
    own (`own_key`, erratum E1: a re-opened row may redirect to its own URL but
    not to another base row's).  Both only add failures."""
    last: Exception | None = None
    for _ in range(FETCH_ATTEMPTS):
        try:
            status, final, data = run_curl(url)
            if status != 200:
                raise OSError("HTTP %d at %s" % (status, final))
            if pins is not None and not host_ok(final, pins):
                raise OSError("fetched off the pinned hosts at %s" % final)
            if (base_keys is not None and url_key(final) in base_keys
                    and url_key(final) != own_key):
                raise OSError("reached a base SOURCES URL %s" % final)
            if url_is_change_note(final):
                raise OSError("reached a change-note page %s" % final)
            if len(data) > MAX_BYTES:
                raise OSError("page exceeds 5 MiB")
            return data.decode("utf-8", errors="replace")
        except Exception as e:  # network, status, pin or decode failure: not found
            last = e
    raise last if last else OSError("fetch failed")


# ------------------------------------------------------------------- the lines

def summary_line(fetching: bool, backed: int, k: int, found: int) -> str:
    if fetching:
        return ("scoped rule files backed on committed snapshots %d of %d; "
                "found on the live page %d of %d" % (backed, k, found, k))
    return ("scoped rule files backed on committed snapshots %d of %d; live not run"
            % (backed, k))


def reject_line(client: str, why: list[str]) -> str:
    return "reject %s: %s" % (client, "; ".join(why))


def predicate(fetching: bool, found: int) -> int:
    """Exit 0 iff fetching, the target is frozen and F >= TARGET."""
    if not fetching or TARGET is None:
        return 1
    return 0 if found >= TARGET else 1


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
    global BASE, TARGET, lane_dir, run_curl, MAX_BYTES
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
    check("green: .claude/rules/ is a directory token",
          token_well_formed(".claude/rules/"), True)
    check("green: .claude/rules/*.md is a glob token",
          token_well_formed(".claude/rules/*.md"), True)
    check("green: .cursor/rules/*.mdc",
          token_well_formed(".cursor/rules/*.mdc"), True)
    check("green: .github/instructions/",
          token_well_formed(".github/instructions/"), True)
    check("green: .github/instructions/**/*.instructions.md (census token)",
          token_well_formed(".github/instructions/**/*.instructions.md"), True)
    check("green: .gemini/rules/",
          token_well_formed(".gemini/rules/"), True)
    check("green: a leading ~/ is stripped",
          token_well_formed("~/.claude/rules/"), True)
    check("green: a leading ./ is stripped",
          token_well_formed("./.github/instructions/"), True)
    check("green: a dot-led non-final segment is fine (E7)",
          token_well_formed(".github/.instructions/config.md"), True)
    check("green: an 'instructions' segment is allowed",
          token_well_formed(".claude/instructions/rules.md"), True)
    check("green: a capitalised allowed word is not a banned word",
          token_well_formed(".claude/Rules.json"), True)
    check("red segment word: .claude/HOOKS.json (the ban is case-insensitive)",
          token_well_formed(".claude/HOOKS.json"), False)
    check("'' is not well-formed", token_well_formed(""), False)
    check("None is not well-formed", token_well_formed(None), False)
    check("red TOKEN_RE: a space",
          token_well_formed(".claude/rules files"), False)
    check("red TOKEN_RE: an empty middle segment",
          token_well_formed(".claude//rules.md"), False)
    check("red TOKEN_RE: a leading slash",
          token_well_formed("/.claude/rules.md"), False)
    check("red segments: rules is one segment",
          token_well_formed("rules"), False)
    check("red segments: .claude is one segment",
          token_well_formed(".claude"), False)
    check("red first segment: rules.md does not start with a dot",
          token_well_formed("rules.md"), False)
    check("red first segment: claude/rules/ does not start with a dot",
          token_well_formed("claude/rules/"), False)
    check("red segment word: .claude/hooks/rules.md (a hook word)",
          token_well_formed(".claude/hooks/rules.md"), False)
    check("red segment word: .claude/hooks.json (the FINAL segment counts)",
          token_well_formed(".claude/hooks.json"), False)
    check("red segment word: .claude/skills/rules.md",
          token_well_formed(".claude/skills/rules.md"), False)
    check("red segment word: .claude/agents/rules.md",
          token_well_formed(".claude/agents/rules.md"), False)
    check("red segment word: .claude/commands/rules.md",
          token_well_formed(".claude/commands/rules.md"), False)
    check("red segment word: .claude/prompts/rules.md",
          token_well_formed(".claude/prompts/rules.md"), False)
    check("red segment word: .claude-plugin/rules.md (a plugin segment)",
          token_well_formed(".claude-plugin/rules.md"), False)
    check("red segment word: .vscode/extensions/rules.md",
          token_well_formed(".vscode/extensions/rules.md"), False)
    check("red segment word: an agent-tools segment is the word agent",
          token_well_formed(".claude/agent-tools/rules.md"), False)
    check("red E7: .claude/1.0/rules.md (a version segment)",
          token_well_formed(".claude/1.0/rules.md"), False)
    check("red E7: .claude.local/rules.md (the first segment too)",
          token_well_formed(".claude.local/rules.md"), False)
    check("red E7: ~/.claude/1.0.0/rules.md",
          token_well_formed("~/.claude/1.0.0/rules.md"), False)

    # -- normalise: case preserved ---------------------------------------
    check("normalise strips one leading ~/",
          normalise("~/.claude/rules/"), ".claude/rules")
    check("normalise strips one leading ./",
          normalise("./.opencode/rules/"), ".opencode/rules")
    check("normalise strips one trailing /",
          normalise(".gemini/rules/"), ".gemini/rules")
    check("normalise strips ONE trailing slash only",
          normalise(".opencode/rules//"), ".opencode/rules/")
    check("normalise PRESERVES case",
          normalise(".Claude/Rules.md"), ".Claude/Rules.md")
    check("normalise of nothing is empty", normalise(None), "")

    # -- the foreign-name guard ------------------------------------------
    check("a .claude token is foreign to VS Code",
          foreign_marker("VS Code", ".claude/rules/"), "Claude Code")
    check("a .claude token is not foreign to Claude Code",
          foreign_marker("Claude Code", ".claude/rules/"), None)
    check("an .opencode token is not foreign to opencode",
          foreign_marker("opencode", ".opencode/rules/"), None)
    check("a gemini token is not foreign to Gemini CLI",
          foreign_marker("Gemini CLI", ".gemini/rules/"), None)
    check("the marker match is case-insensitive",
          foreign_marker("VS Code", ".Claude/Rules.md"), "Claude Code")
    check("a .cursor token is foreign to Gemini CLI",
          foreign_marker("Gemini CLI", ".cursor/rules/"), "Cursor")
    check("a marker-neutral token is nobody's foreign token",
          foreign_marker("Copilot CLI", ".github/instructions/"), None)

    # -- the quote: word bounds, token span, the outside rule word --------
    check("E6: quote word count: six words pass",
          MIN_WORDS <= len("one two three four five six".split()) <= MAX_WORDS, True)
    check("E6: quote word count: five words fail",
          MIN_WORDS <= len("one two three four five".split()) <= MAX_WORDS, False)
    check("quote word count: 25 words pass",
          len(("w " * 24 + "w").split()) <= MAX_WORDS, True)
    check("quote word count: 26 words fail",
          len(("w " * 25 + "w").split()) <= MAX_WORDS, False)
    check("strip straight quotes", strip_quotes('"hello world"'), "hello world")
    check("strip curly quotes", strip_quotes("\u201chello world\u201d"), "hello world")
    check("keep an unquoted cell", strip_quotes("hello world"), "hello world")
    q = "Rule files live in .claude/rules/ and each rule names the files"
    span = token_span(q, ".claude/rules/")
    check("the raw token is found in the quote", span is not None, True)
    check("a rule word sits outside the token span",
          rule_word_outside(q, span[0], span[1]), True)
    check("the token span starts where the token starts",
          q[span[0]:span[1]], ".claude/rules/")
    q2 = "the file is .claude/rules/"
    span2 = token_span(q2, ".claude/rules/")
    check("only the token carries no rule word",
          rule_word_outside(q2, span2[0], span2[1]), False)
    check("rulebook is not the whole word rule",
          rule_word_outside("Rulebook entries differ here", 0, 0), False)
    check("instructions is the word",
          rule_word_outside("these instructions differ", 99, 99), True)
    check("hook is not a rule word",
          rule_word_outside("this hook differs from it", 0, 0), False)
    check("the token match is case-sensitive",
          token_span(".Claude/Rules.md is used", ".claude/rules.md"), None)
    check("the normalised form is matched too",
          token_span("see .opencode/rules here", ".opencode/rules/"), (4, 19))
    check("a token inside a longer path is not spanned (left boundary)",
          token_span("x.claude/rules.md here", ".claude/rules.md"), None)
    check("a token followed by a word is not spanned (right boundary)",
          token_span(".claude/rulesfoo here", ".claude/rules"), None)
    check("a token followed by a digit is not spanned",
          token_span(".claude/rules1 here", ".claude/rules"), None)
    check("a token followed by a slash is spanned",
          token_span(".claude/rules/x here", ".claude/rules"), (0, 13))

    # -- the Gate check ---------------------------------------------------
    gate = "## Gate\n\n| row | quote |\n|---|---|---|\n| S1 | \"the rule folder lives here\" |\n"
    gs = gate_section(gate)
    check("gate section is read", ws(gs).count("the rule folder lives here"), 1)
    check("quote recorded in the Gate", quote_in_gate(
        "the rule folder lives here", ws(gs), ws(gs.replace("`", ""))), True)
    check("quote absent from the Gate", quote_in_gate(
        "the rule folder lives elsewhere", ws(gs), ws(gs.replace("`", ""))), False)
    check("an empty Gate records no quote", quote_in_gate(
        "the rule folder lives here", ws(""), ws("")), False)
    check("Gate whitespace is normalised", quote_in_gate(
        "the  rule folder lives here", ws(gs), ws(gs.replace("`", ""))), True)

    # -- URL normalisation (v1.3, unchanged) ------------------------------
    check("url_key drops a trailing .md",
          url_key("https://code.claude.com/docs/en/rules.md"),
          url_key("https://code.claude.com/docs/en/rules"))
    check("url_key drops a trailing slash",
          url_key("https://opencode.ai/docs/rules/"),
          "//opencode.ai/docs/rules")
    check("url_key drops a fragment",
          url_key("https://cursor.com/docs/rules#x"),
          "//cursor.com/docs/rules")
    check("url_key drops a query",
          url_key("https://cursor.com/docs/rules?a=1"),
          "//cursor.com/docs/rules")
    check("url_key lower-cases scheme, host and path",
          url_key("HTTPS://Code.Claude.com/Docs"), "//code.claude.com/docs")
    check("url_key of nothing is empty", url_key(None), "")
    check("a path-case alias is the same URL",
          url_key("https://code.claude.com/docs/en/Rules"),
          url_key("https://code.claude.com/docs/en/rules"))
    check("www., scheme and percent-encoding do not make a new URL",
          url_key("http://www.code.claude.com/docs/en/rules.md/"),
          url_key("https://code.claude.com/docs/en/rules"))
    check("repeated slashes do not make a new URL",
          url_key("https://code.claude.com//docs///rules"),
          url_key("https://code.claude.com/docs/rules"))
    check("an issue URL is a tracker page",
          url_is_tracker("https://github.com/anthropics/claude-code/issues/82902"), True)
    check("a docs page is not a tracker page",
          url_is_tracker("https://cursor.com/docs/rules.md"), False)

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

    # -- page normalisation and the quote check ---------------------------
    check("page style and script text is dropped",
          "@layer base" in norm_page(
              "<style>@layer base{}</style><p>x</p><script>@layer base</script>"), False)
    check("page tags are dropped and text kept",
          norm_page("<p>Use <code>/a-b</code> rules</p>"), "use /a-b rules")
    check("quote angle text is kept", norm("$<rule-name> here"), "$<rule-name> here")
    check("page_plain drops `*`, `_` and backticks but keeps case",
          page_plain("A*b_c`D"), "AbcD")
    check("norm lower-cases the quote", norm("Claude Ships"), "claude ships")
    page_ok = "<p>Rule files live in a <code>.claude/rules/</code> folder</p>"
    quote_ok = "Rule files live in a .claude/rules/ folder"
    check("quote found on the page", quote_why(page_ok, quote_ok), [])
    check("quote absent from the page",
          quote_why(page_ok, "Rule files live in a folder"),
          ["the quote is not on the page"])

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
          snapshot_path("S900"), ".ufo/waves/round-60/snapshots/S900.page")

    # -- the output lines, the receipt label and the predicate -----------
    check("fetch summary line", summary_line(True, 0, 0, 0),
          "scoped rule files backed on committed snapshots 0 of 0; "
          "found on the live page 0 of 0")
    check("non-fetch summary line", summary_line(False, 2, 7, 0),
          "scoped rule files backed on committed snapshots 2 of 7; live not run")
    check("reject line", reject_line("Cursor", ["a", "b"]), "reject Cursor: a; b")
    check("the receipt label is the frozen one",
          RECEIPT, "C1 predicate: --fetch exit 0 (F>=TARGET)")
    check("E3: url_is_change_note on each word",
          [url_is_change_note("https://x.com/a/%s/b" % w) for w in CHANGE_NOTE_WORDS],
          [True] * len(CHANGE_NOTE_WORDS))
    check("E3: url_is_change_note is case-insensitive and percent-decoded",
          (url_is_change_note("https://x.com/CHANGELOG.md"),
           url_is_change_note("https://x.com/%62log/x")), (True, True))
    check("E3: a docs URL is not a change note",
          url_is_change_note("https://code.claude.com/docs/en/rules"), False)
    check("E3: a change-note word only in the query is not the path",
          url_is_change_note("https://cursor.com/docs/rules?from=blog"), False)

    # TARGET is the plan's freeze record (amendment A1 names this counter as
    # its builder).  A `None` here is also supported: it returns 1, never 0.
    check("TARGET is the frozen census target", TARGET, 3)
    frozen = TARGET
    try:
        TARGET = 3
        check("predicate: fetch, 3 found, passes", predicate(True, 3), 0)
        check("predicate: fetch, 4 found, passes", predicate(True, 4), 0)
        check("predicate: fetch, 2 found, fails", predicate(True, 2), 1)
        check("predicate: no fetch always fails", predicate(False, 7), 1)
        TARGET = None
        check("predicate: no target is a 1, never a 0",
              _outcome(lambda: predicate(True, 7)), ("ok", 1))
        check("predicate: a frozen integer target still gates the count",
              (TARGET, _outcome(lambda: predicate(True, 7))), (None, ("ok", 1)))
    finally:
        TARGET = frozen

    # -- the Scope key cell ----------------------------------------------
    check("key: a bare identifier is the key", scope_key("`paths` (S900 :5)"),
          ("paths", []))
    check("key: the FIRST backticked span is the key",
          scope_key("`alwaysApply` and `paths` (S900 :5)")[0], "alwaysApply")
    check("key: a cell without backticks has no key",
          scope_key("paths (S900 :5)"),
          (None, ["SKILL.md scope key cell holds no backticked key"]))
    check("key: a glob is not a key identifier",
          scope_key("`**/*.md` (S900 :5)"),
          (None, ["SKILL.md scope key '**/*.md' is not a bare identifier "
                  "matching ^[A-Za-z][A-Za-z0-9_-]*$"]))
    check("citations: both forms are read",
          citations("`paths` (S900 :5) and S901:7"), [("S900", 5), ("S901", 7)])
    check("citation: the row's own id is taken",
          citation_why("`paths` (S900 :5)", "S900", "SKILL.md scope key cell"),
          (5, []))
    check("citation: the spaced and unspaced forms agree",
          citation_why("`paths` S900:5", "S900", "SKILL.md scope key cell"), (5, []))
    check("citation: another row's id is a named failure",
          citation_why("`paths` (S901 :5)", "S900", "SKILL.md scope key cell"),
          (None, ["SKILL.md scope key cell cites S901 :5, not the row's own "
                  "source S900"]))
    check("citation: no citation is a named failure",
          citation_why("`paths`", "S900", "SKILL.md scope key cell"),
          (None, ["SKILL.md scope key cell carries no `S### :L` citation"]))

    # -- the key form and its value (A1) ---------------------------------
    check("value: a quoted glob is a pattern", pattern_value(" '**/*.py'"), True)
    check("value: a sentence that mentions a pattern is not",
          pattern_value(' "Applies to **/*.ts"'), False)
    check("value: a path glob is a pattern",
          pattern_value(" src/components/**/*.tsx"), True)
    check("value: an inline array holds a pattern",
          pattern_value(' ["src/**/*.ts"]'), True)
    check("value: an empty value is not a pattern", pattern_value(""), False)
    check("value: a bare glob is a pattern", pattern_value("**"), True)
    check("value: a leading dash and quote are stripped",
          first_value_token('  - "src/api/**/*.ts"'), "src/api/**/*.ts")
    check("value: the token stops at a comma", first_value_token("a/*.ts, b/*.py"),
          "a/*.ts")
    check("value: the token stops at a closing bracket",
          first_value_token("[src/*.ts]"), "src/*.ts")
    check("value: only [ | > is a block value", block_only(" ["), True)
    check("value: only spaces is a block value", block_only("  "), True)
    check("value: a word after the colon is not a block value",
          block_only(" paths"), False)
    check("key form: a block value two lines down passes",
          key_site(["paths:", '  - "src/api/**/*.ts"'], 1, "paths"), True)
    check("key form: the cited pattern line itself carries no key",
          key_site(["paths:", '  - "src/api/**/*.ts"'], 2, "paths"), False)
    check("key form: a block value four lines down fails",
          key_site(["paths:", "", "", "", '  - "src/api/**/*.ts"'], 1, "paths"),
          False)
    check("key form: an unrelated first nonblank line leaves no value",
          key_site(["paths:", "See the table below.", "  - 'a/*.ts'"], 1, "paths"),
          False)
    check("key form: the Cursor census line passes",
          key_site(["globs: src/components/**/*.tsx"], 1, "globs"), True)
    check("key form: the Claude memory block passes",
          key_site(["paths:", '  - "src/api/**/*.ts"'], 1, "paths"), True)
    check("key form: the VS Code census line passes",
          key_site(["applyTo: '**/*.py'"], 1, "applyTo"), True)
    check("key form: the Copilot census line passes",
          key_site(['applyTo: "app/models/**/*.rb"'], 1, "applyTo"), True)
    check("key form: description at a line with no pattern fails",
          key_site(["description: RPC service conventions and patterns"], 1,
                   "description"), False)
    check("key form: an assigned sentence mentioning a pattern fails",
          key_site(['description: "Applies to **/*.ts"'], 1, "description"), False)
    check("key form: the Cursor table-cell line fails for description",
          key_site(["| `alwaysApply` | `description` | `globs` |"], 1,
                   "description"), False)
    check("key form: the Cursor table-cell line fails for alwaysApply",
          key_site(["| `alwaysApply` | `description` | `globs` |"], 1,
                   "alwaysApply"), False)
    check("key form: the Cursor table-cell line fails for globs",
          key_site(["| `alwaysApply` | `description` | `globs` |"], 1, "globs"),
          False)
    check("key form: a line with no key fails",
          key_site(["Use paths to list the files a rule is about."], 1, "paths"),
          False)
    check("key form: an off-by-one to a line without the key fails",
          key_site(["paths:", '  - "src/api/**/*.ts"'], 2, "paths"), False)
    check("key form: a key inside a longer identifier fails",
          key_site(['xpaths: "**/*.ts"'], 1, "paths"), False)
    check("key form: a key followed by an identifier fails",
          key_site(['pathsExtra: "**/*.ts"'], 1, "paths"), False)
    check("key form: an equals sign is a key form",
          key_site(["applyTo='**/*.py'"], 1, "applyTo"), True)
    check("key form: a closing quote before the colon is a key form",
          key_site(['"applyTo": "**/*.ts"'], 1, "applyTo"), True)
    check("key form: a backticked closing before the colon is a key form",
          key_site(["`applyTo`: '**/*.ts'"], 1, "applyTo"), True)
    check("key form: a line out of range fails", key_site(["a"], 4, "paths"), False)
    check("key form: no key is never a site", key_site(["paths:"], 1, None), False)
    check("any key site: a later line is found",
          any_key_site("intro\n\nglobs: src/*.tsx\n", "globs"), True)
    check("any key site: a page without the key is not found",
          any_key_site("intro\n\nglobs: one per line\n", "globs"), False)

    # -- the synthetic world: SKILL rows, entry, SOURCES, Gate, snapshots ---
    page900 = ("Rules for Claude Code\n"
               "Rule files live in .claude/rules/ and each rule names the files it is about.\n"
               "---\n"
               "description: how a rule scopes itself\n"
               "paths:\n"
               '  - "src/api/**/*.ts"\n'
               "---\n"
               "Use paths to list the files a rule is about.\n")
    page901 = ("Gemini CLI instruction files\n"
               "Gemini CLI keeps instruction files in .gemini/rules/ and scopes each one.\n"
               "---\n"
               'globs: ["**/*.ts"]\n'
               "---\n"
               "List the files an instruction covers.\n")
    page902 = ("VS Code scoped instruction files\n"
               "VS Code scoped instruction files live in .github/instructions/ for a workspace.\n"
               "---\n"
               "applyTo: '**/*.py'\n"
               "---\n"
               "Scope a rule to the files it is about instead of loading it every turn.\n")
    page903 = ("Copilot CLI instruction files\n"
               "Copilot CLI reads instruction files from .github/instructions/ in the repository.\n"
               "---\n"
               'applyTo: "app/models/**/*.rb"\n'
               "---\n"
               "Scope a rule to the files it is about so every turn stays small.\n")
    quote900 = ("Rule files live in .claude/rules/ and each rule names the files "
                "it is about")
    quote901 = "Gemini CLI keeps instruction files in .gemini/rules/ and scopes each one"
    quote902 = ("VS Code scoped instruction files live in .github/instructions/ "
                "for a workspace")
    quote903 = ("Copilot CLI reads instruction files from .github/instructions/ "
                "in the repository")
    skill = ("# x\n\n" + SKILL_HEADING + "\n\n"
             "| Client | Rule files | Scope key | Action |\n"
             "|---|---|---|---|\n"
             "| Claude Code | `.claude/rules/` | `paths` (S900 :5) "
             "| Name the paths a rule applies to (S900 :8) |\n"
             "| Gemini CLI | `.gemini/rules/` | `globs` (S901 :4) "
             "| List the files an instruction covers (S901 :6) |\n"
             "| VS Code | `.github/instructions/` | `applyTo` (S902 :4) "
             "| Scope a rule to the files it is about (S902 :6) |\n"
             "| Copilot CLI | `.github/instructions/` | `applyTo` (S903 :4) "
             "| Scope a rule to the files it is about (S903 :6) |\n")
    entry = ("# e\n\n| Client | Rule files | Source | Quote |\n|---|---|---|---|\n"
             '| Claude Code | .claude/rules/ | S900 | "' + quote900 + '" |\n'
             '| Gemini CLI | .gemini/rules/ | S901 | "' + quote901 + '" |\n'
             '| VS Code | .github/instructions/ | S902 | "' + quote902 + '" |\n'
             '| Copilot CLI | .github/instructions/ | S903 | "' + quote903 + '" |\n')
    PAGES = {"S900": page900, "S901": page901, "S902": page902, "S903": page903}
    QUOTES = {"S900": quote900, "S901": quote901, "S902": quote902, "S903": quote903}
    OWNERS = {"S900": "Claude Code", "S901": "Gemini CLI",
              "S902": "VS Code", "S903": "Copilot CLI"}
    URLS = {"S900": "https://code.claude.com/docs/en/memory.md",
            "S901": "https://geminicli.com/docs/cli/rules.md",
            "S902": "https://code.visualstudio.com/docs/agent-customization/"
                    "custom-instructions.md",
            "S903": "https://docs.github.com/en/copilot/how-tos/customize/"
                    "instructions.md"}
    src_row = ("| %s | %s docs \u2014 %s | docs | A | the rule file "
               "| \u00a7 rules, fetched, sha256 %s | %s | mined "
               "| %s | 90d | corpus/knowledge/scoped-rules-round60.md |\n")

    def world(pages=None, teaches=None) -> tuple[str, dict]:
        """The four SOURCES rows and the committed pages they pin.

        Each row prints the sha256 of its own page bytes, so a page rebuilt for
        another quote is a sha mismatch, never a silent pass.  `teaches` may
        carry a v2 `re-opens S### \u2014 \u2026` cell for a row."""
        got = dict(PAGES if pages is None else pages)
        extra = teaches or {}
        snaps = {sid: got[sid].encode() for sid in got}
        rows = "".join(src_row % (sid, OWNERS[sid], URLS[sid],
                                  hashlib.sha256(snaps[sid]).hexdigest(),
                                  extra.get(sid, "the rule file"), OPENED[0])
                       for sid in ("S900", "S901", "S902", "S903"))
        return rows, snaps

    sources, snaps = world()
    lesson = ("## Gate\n\n| row | URL | quote |\n|---|---|---|\n"
              + "".join('| %s | %s | "%s" |\n'
                        % (sid, URLS[sid], QUOTES[sid])
                        for sid in ("S900", "S901", "S902", "S903")))
    base = ("| S001 | Old docs \u2014 https://code.claude.com/docs/en/old.md | docs "
            "| A | s | a | t | mined | 2026-10-01 | 90d | y |\n")
    # erratum E1 fixtures: base rows whose URLs the new rows re-open.  S020 and
    # S022 hold the Claude memory.md URL; S021 holds the Gemini rules.md URL;
    # S022's line already carries the key `paths`, S020's and S021's carry
    # neither key.
    base_reopen = (base
                   + "| S020 | Old Claude docs \u2014 "
                     "https://code.claude.com/docs/en/memory.md | docs | A | s "
                     "| a | t | mined | 2026-10-01 | 90d | y |\n"
                   + "| S021 | Old Gemini docs \u2014 "
                     "https://geminicli.com/docs/cli/rules.md | docs | A | s | a "
                     "| t | mined | 2026-10-01 | 90d | y |\n"
                   + "| S022 | Old Claude docs \u2014 "
                     "https://code.claude.com/docs/en/memory.md | docs | A | "
                     "paths and globs | a | t | mined | 2026-10-01 | 90d | y |\n")
    REOPENS = {"S900": "re-opens S020 \u2014 the rules page moved",
               "S901": "re-opens S021 \u2014 the rules page moved"}

    def ro(teaches=None) -> tuple[str, dict]:
        """The v2 re-open world: S900 and S901 reuse base URLs, S902/903 do not."""
        got = dict(REOPENS)
        if teaches:
            got.update(teaches)
        return world(teaches=got)

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

    def with_quote(sid: str, new: str, extra: dict | None = None) -> tuple:
        """Entry, lesson, sources and pages with one quote replaced."""
        old = QUOTES[sid]
        pages = dict(PAGES)
        pages[sid] = pages[sid].replace(old, new)
        if extra:
            pages.update(extra)
        so, sn = world(pages)
        return (entry.replace(old, new), lesson.replace(old, new), so, sn)

    four = ["Claude Code", "VS Code", "Copilot CLI", "Gemini CLI"]
    three = ["VS Code", "Copilot CLI", "Gemini CLI"]
    check("the synthetic world backs all four clients", backed(), four)
    check("E5 dropped: two rows may share a token and both back",
          backed(sk=skill), four)
    check("the synthetic world counts four tokens in K", k_of(), 4)
    check("the scope key and key line are carried on the report",
          [(r["key"], r["key_line"]) for r in judge_world() if r["backed"]],
          [("paths", 5), ("applyTo", 4), ("applyTo", 4), ("globs", 4)])

    # -- SKILL.md structural failures -------------------------------------
    check("a duplicate SKILL.md row disqualifies the client",
          backed(sk=skill.replace(
              "| Gemini CLI |",
              "| Claude Code | `~/.x/rules/x` | `a` (S900 :5) | y |\n"
              "| Gemini CLI |")),
          three)
    check("a second entry row does not disqualify a good one",
          backed(en=entry + '| Gemini CLI | x | S901 | "x y z" |\n'), four)
    check("a wrong SKILL.md header reads no row",
          skill_rows(skill.replace("| Scope key |", "| Key |")), [])
    check("a wrong entry header reads no row",
          entry_rows(entry.replace("| Source |", "| Row |")), [])
    check("a table under another heading is not read",
          skill_rows(skill.replace(SKILL_HEADING, "### Other table")), [])
    check("no entry row for the client is not backed",
          backed(en=entry.replace('| Gemini CLI | .gemini/rules/ | S901 | "'
                                  + quote901 + '" |\n', "")),
          ["Claude Code", "VS Code", "Copilot CLI"])

    # -- SOURCES row failures ---------------------------------------------
    check("an S### already at base is not backed",
          backed(ba=base.replace("S001", "S900")),
          three)
    check("a base URL is not backed",
          backed(ba=base.replace("old.md", "memory.md")),
          three)
    check("a base URL reached by a path-case alias is not backed",
          backed(ba=base.replace("old.md", "MEMORY")),
          three)
    check("a tier B row is not backed",
          backed(so=sources.replace("| docs | A |", "| docs | B |", 1)),
          three)
    check("a queued row is not backed",
          backed(so=sources.replace("| mined |", "| queued |", 1)),
          three)
    check("another opened date is not backed",
          backed(so=sources.replace("| mined | 2026-10-23 |",
                                    "| mined | 2026-10-22 |", 1)),
          three)
    check("a non-docs kind is not backed",
          backed(so=sources.replace("| docs | A |", "| issue | A |", 1)),
          three)
    check("an off-host URL is not backed",
          backed(so=sources.replace("https://code.claude.com",
                                    "https://code.claude.com.evil.io", 1)),
          three)
    check("a tracker URL on a pinned host is not backed",
          backed(so=sources.replace(
              URLS["S900"],
              "https://github.com/anthropics/claude-code/issues/1", 1)),
          three)
    check("a changelog URL is not backed",
          backed(so=sources.replace(URLS["S900"],
                                    "https://code.claude.com/docs/en/changelog.md",
                                    1)),
          three)
    check("a change-note URL is reported as such",
          any("changelog/release/news/blog" in w for w in why_of(
              "Claude Code", so=sources.replace(
                  URLS["S900"],
                  "https://raw.githubusercontent.com/anthropics/claude-code/"
                  "main/CHANGELOG.md", 1))), True)
    check("a source cell without a URL is not backed",
          backed(so=sources.replace(URLS["S900"], "no url here", 1)),
          three)

    # -- the token and the quote -------------------------------------------
    check("a malformed rule token is not backed and leaves K",
          (backed(sk=skill.replace("`.gemini/rules/`", "`rules`")),
           k_of(skill.replace("`.gemini/rules/`", "`rules`"))),
          (["Claude Code", "VS Code", "Copilot CLI"], 3))
    check("a hook token is not well-formed (A1 NOT-words)",
          backed(sk=skill.replace("`.claude/rules/`", "`.claude/hooks/`")),
          three)
    check("a rule cell without a backticked token is not backed",
          backed(sk=skill.replace("`.gemini/rules/`", ".gemini/rules/")),
          ["Claude Code", "VS Code", "Copilot CLI"])
    check("a token carrying another client's marker is not backed",
          backed(sk=skill.replace("`.gemini/rules/`", "`.claude/rules/`")),
          ["Claude Code", "VS Code", "Copilot CLI"])
    check("the foreign marker is reported as such",
          any("carries Claude Code's marker" in w for w in why_of(
              "Gemini CLI", sk=skill.replace("`.gemini/rules/`",
                                             "`.claude/rules/`"))), True)
    no_token = "Gemini CLI keeps its instructions in a folder of its own"
    got = with_quote("S901", no_token)
    check("a quote without the token is not backed",
          backed(en=got[0], le=got[1], so=got[2], sn=got[3]),
          ["Claude Code", "VS Code", "Copilot CLI"])
    in_token = "The folder .gemini/rules/ keeps its definitions near the workflow"
    got = with_quote("S901", in_token)
    check("a quote without a rule word outside the token is not backed",
          backed(en=got[0], le=got[1], so=got[2], sn=got[3]),
          ["Claude Code", "VS Code", "Copilot CLI"])
    check("the missing rule word is reported as such",
          any("no rule/instruction word outside the token" in w for w in why_of(
              "Gemini CLI", en=got[0], le=got[1], so=got[2], sn=got[3])), True)
    hooky = "Keep .claude/rules/ files for hooky reasons to reuse them"
    got = with_quote("S900", hooky)
    check("a quote whose only rule word is inside the token is not backed",
          backed(en=got[0], le=got[1], so=got[2], sn=got[3]),
          three)
    case_diff = "Gemini CLI keeps instruction files in .Gemini/Rules/ today"
    got = with_quote("S901", case_diff)
    check("a quote whose token differs only in case is not backed",
          backed(en=got[0], le=got[1], so=got[2], sn=got[3]),
          ["Claude Code", "VS Code", "Copilot CLI"])
    two = "rules .gemini/rules/"
    got = with_quote("S901", two)
    check("a two-word quote is not backed",
          backed(en=got[0], le=got[1], so=got[2], sn=got[3]),
          ["Claude Code", "VS Code", "Copilot CLI"])
    long_quote = " ".join(["rules"] + ["w"] * 24 + [".gemini/rules/"])
    got = with_quote("S901", long_quote)
    check("a 26-word quote is not backed",
          backed(en=got[0], le=got[1], so=got[2], sn=got[3]),
          ["Claude Code", "VS Code", "Copilot CLI"])
    check("an entry source cell that is not one S### id is not backed",
          backed(en=entry.replace("| S901 |", "| docs |")),
          ["Claude Code", "VS Code", "Copilot CLI"])
    check("an S### absent from SOURCES.md is not backed",
          backed(en=entry.replace("S901", "S999")),
          ["Claude Code", "VS Code", "Copilot CLI"])
    check("a quote missing from the Gate is not backed",
          backed(le=lesson.replace(quote900, "Rule files live elsewhere")),
          three)
    check("the Gate failure is reported as such",
          any("round-60 Gate does not record this quote" in w for w in why_of(
              "Claude Code", le=lesson.replace(quote900,
                                               "Rule files live elsewhere"))),
          True)

    # -- E4: the entry Rule files cell is the SKILL.md token --------------
    check("E4: an entry Rule files cell that differs from SKILL.md is not backed",
          backed(en=entry.replace("| Gemini CLI | .gemini/rules/ |",
                                  "| Gemini CLI | .gemini/other.json |")),
          ["Claude Code", "VS Code", "Copilot CLI"])
    check("E4: a backticked Rule files cell still backs",
          backed(en=entry.replace("| Gemini CLI | .gemini/rules/ |",
                                  "| Gemini CLI | `.gemini/rules/` |")), four)
    check("E4: the raw ./ form in the cell still backs",
          backed(sk=skill.replace("`.gemini/rules/`", "`./.gemini/rules/`"),
                 en=entry.replace("| Gemini CLI | .gemini/rules/ |",
                                  "| Gemini CLI | ./.gemini/rules/ |")), four)
    check("E4: the normalised form is not the raw cell of a ./ token",
          backed(sk=skill.replace("`.gemini/rules/`", "`./.gemini/rules/`")),
          ["Claude Code", "VS Code", "Copilot CLI"])
    check("E4: rule_cell_matches trims spaces and backticks",
          rule_cell_matches(" `.claude/rules/` ", ".claude/rules/"), True)

    # -- the snapshot: existence, sha256 pin and the quote ----------------
    check("a missing snapshot is not backed",
          backed(sn={"S901": snaps["S901"], "S902": snaps["S902"],
                     "S903": snaps["S903"]}),
          three)
    check("a missing snapshot is reported as missing",
          any("is missing at the revision" in w for w in why_of(
              "Claude Code", sn={"S901": snaps["S901"]})), True)
    bumped = dict(snaps)
    bumped["S900"] = snaps["S900"] + b"\n"
    check("a snapshot whose sha256 differs is not backed",
          backed(sn=bumped), three)
    check("a snapshot sha mismatch is reported as such",
          any("does not equal the SOURCES row sha256" in w for w in why_of(
              "Claude Code", sn=bumped)), True)
    no_sha = sources.replace("sha256 " + hashlib.sha256(snaps["S900"]).hexdigest(),
                             "sha256 `9a67de89\u2026`", 1)
    check("a SOURCES row without a full 64-hex sha256 is not backed",
          backed(so=no_sha), three)
    no_quote_page = ("<p>The folder is <code>.claude/rules/</code>.</p>\n"
                     "paths:\n"
                     '  - "src/api/**/*.ts"\n'
                     "Use paths to list the files a rule is about.\n")
    late = dict(PAGES)
    late["S900"] = no_quote_page
    so_late, sn_late = world(late)
    check("a snapshot that does not carry the quote is not backed",
          backed(so=so_late, sn=sn_late), three)
    check("a snapshot without the quote is reported as such",
          any("the quote is not on the page" in w for w in why_of(
              "Claude Code", so=so_late, sn=sn_late)), True)

    # -- the Scope key conjunct in the judge (A1) -------------------------
    check("a scope key on a line with no pattern drops the row",
          backed(sk=skill.replace("`paths` (S900 :5)",
                                  "`description` (S900 :4)")), three)
    check("the no-pattern key is reported with its key and line",
          any("scope key 'description' is not in key form with a path pattern "
              "at line 4" in w for w in why_of(
                  "Claude Code", sk=skill.replace("`paths` (S900 :5)",
                                                  "`description` (S900 :4)"))),
          True)
    desc_pattern = dict(PAGES)
    desc_pattern["S900"] = page900.replace(
        "description: how a rule scopes itself",
        'description: "Applies to **/*.ts"')
    so_dp, sn_dp = world(desc_pattern)
    check("a description whose value mentions a pattern still fails",
          backed(sk=skill.replace("`paths` (S900 :5)",
                                  "`description` (S900 :4)"),
                 so=so_dp, sn=sn_dp), three)
    table_key = dict(PAGES)
    table_key["S900"] = page900.replace(
        "description: how a rule scopes itself",
        "| `alwaysApply` | `description` | `globs` |")
    so_tk, sn_tk = world(table_key)
    check("the Cursor table-cell line is not a key form for description",
          backed(sk=skill.replace("`paths` (S900 :5)",
                                  "`description` (S900 :4)"),
                 so=so_tk, sn=sn_tk), three)
    check("the Cursor table-cell line is not a key form for alwaysApply",
          backed(sk=skill.replace("`paths` (S900 :5)",
                                  "`alwaysApply` (S900 :4)"),
                 so=so_tk, sn=sn_tk), three)
    ident_page = dict(PAGES)
    ident_page["S900"] = page900.replace("paths:", "xpaths:", 1)
    so_id, sn_id = world(ident_page)
    check("a key only inside a longer identifier drops the row",
          backed(so=so_id, sn=sn_id), three)
    check("an off-by-one citation to a line without the key drops the row",
          backed(sk=skill.replace("`paths` (S900 :5)", "`paths` (S900 :6)")), three)
    check("the off-by-one is reported at the cited line",
          any("scope key 'paths' is not in key form with a path pattern at "
              "line 6" in w for w in why_of(
                  "Claude Code", sk=skill.replace("`paths` (S900 :5)",
                                                  "`paths` (S900 :6)"))), True)
    block_ok = ("Rules for Claude Code\n"
                + page900.splitlines()[1] + "\n"
                "---\n"
                "description: how a rule scopes itself\n"
                "paths:\n"
                '  - "src/api/**/*.ts"\n'
                "---\n"
                "Use paths to list the files a rule is about.\n")
    block_far = ("Rules for Claude Code\n"
                 + page900.splitlines()[1] + "\n"
                 "---\n"
                 "description: how a rule scopes itself\n"
                 "paths:\n"
                 "\n"
                 "\n"
                 "Use paths to list the files a rule is about.\n"
                 "\n"
                 "---\n"
                 '  - "src/api/**/*.ts"\n')
    so_bo, sn_bo = world({**PAGES, "S900": block_ok})
    so_bf, sn_bf = world({**PAGES, "S900": block_far})
    check("a block value two lines down backs in the judge",
          backed(so=so_bo, sn=sn_bo), four)
    check("a block value four lines down drops the row",
          backed(so=so_bf, sn=sn_bf), three)
    check("a scope key citing another row's source is not backed",
          backed(sk=skill.replace("`paths` (S900 :5)", "`paths` (S901 :5)")),
          three)
    check("a scope key with no citation is not backed",
          backed(sk=skill.replace("`paths` (S900 :5)", "`paths`")), three)
    check("an action citing another row's source is not backed",
          backed(sk=skill.replace("(S900 :8)", "(S901 :8)")), three)
    check("an action with no citation is not backed",
          backed(sk=skill.replace("Name the paths a rule applies to (S900 :8)",
                                  "Name the paths a rule applies to")), three)
    check("an action on a citation line out of range is not backed",
          backed(sk=skill.replace("(S900 :8)", "(S900 :88)")), three)

    # -- the Action conjunct in the judge (A1) -----------------------------
    one_word = "Name the entries a rule has (S900 :8)"
    check("an action sharing one content word is not backed",
          backed(sk=skill.replace("Name the paths a rule applies to (S900 :8)",
                                  one_word)), three)
    check("the action shortfall is reported with its counts",
          any("action cell shares 1 of its 3 content word(s) with line 8 "
              "(need >= 2)" in w for w in why_of(
                  "Claude Code",
                  sk=skill.replace("Name the paths a rule applies to (S900 :8)",
                                   one_word))), True)
    thin = "Use paths entries (S900 :8)"
    check("an action with two content words is not backed",
          backed(sk=skill.replace("Name the paths a rule applies to (S900 :8)",
                                  thin)), three)
    check("the thin action is reported with its count",
          any("action cell holds 2 distinct content word(s) (need >= 3)" in w
              for w in why_of(
                  "Claude Code",
                  sk=skill.replace("Name the paths a rule applies to (S900 :8)",
                                   thin))), True)
    longer = "Name the paths a rule applies to the listed entries (S900 :8)"
    check("a longer action needs half of its words, not two",
          backed(sk=skill.replace("Name the paths a rule applies to (S900 :8)",
                                  longer)), three)
    check("the half threshold is reported with its counts",
          any("action cell shares 2 of its 6 content word(s) with line 8 "
              "(need >= 3)" in w for w in why_of(
                  "Claude Code",
                  sk=skill.replace("Name the paths a rule applies to (S900 :8)",
                                   longer))), True)
    check("action need: 3 content words need 2", action_need(3), 2)
    check("action need: 4 content words need 2", action_need(4), 2)
    check("action need: 5 content words need 3", action_need(5), 3)
    check("action need: 6 content words need 3", action_need(6), 3)
    check("action need: 7 content words need 4", action_need(7), 4)
    check("action: one shared word fails",
          action_conjunct(["Scope a rule to the files it covers."],
                          "Name the paths a rule uses (S900 :1)", 1),
          ["action cell shares 1 of its 4 content word(s) with line 1 "
           "(need >= 2)"])
    check("action: two shared words pass",
          action_conjunct(["Scope a rule to the files it covers."],
                          "Scope a rule with pattern support (S900 :1)", 1), [])
    check("action: content words drop backticks, citations and stopwords",
          content_words("Scope `the` rule (S900 :3) with every file"),
          {"scope", "rule", "file"})
    check("action: an uppercase word is compared lowercased",
          content_words("SCOPE RULE"), {"scope", "rule"})
    check("action: a word under four letters is not a content word",
          content_words("use the api"), set())

    # -- erratum E1: a base-keyed URL may be re-opened (v2) ----------------
    ro_sources, ro_snaps = ro()

    def ro_arm(teaches=None) -> list[str]:
        so, sn = ro(teaches)
        return backed(so=so, sn=sn, ba=base_reopen)

    check("v2: a base URL re-opened by its base id backs", ro_arm(), four)
    two = ["VS Code", "Copilot CLI"]
    check("v2: base URLs without the re-open prefix are not backed",
          backed(ba=base_reopen), two)
    check("v2: the missing re-open is named",
          any("re-open names no base row with this URL" in w for w in why_of(
              "Claude Code", ba=base_reopen)), True)
    check("v2: the re-open prefix is a prefix, not a mention mid-cell",
          ro_arm({"S900": "supersedes S089 \u2014 re-opens S020 \u2014 moved"}),
          three)
    check("v2: a re-open naming a base row whose URL differs is not backed",
          ro_arm({"S900": "re-opens S001 \u2014 moved"}), three)
    so_c, sn_c = ro({"S900": "re-opens S022 \u2014 moved"})
    check("v2: a re-open whose base row line already holds K is not backed",
          backed(so=so_c, sn=sn_c, ba=base_reopen), three)
    check("v2: the key collision is named",
          any("base row S022 already records key paths" in w for w in why_of(
              "Claude Code", so=so_c, sn=sn_c, ba=base_reopen)), True)
    check("v2: a re-open naming a non-base id is not backed",
          ro_arm({"S900": "re-opens S777 \u2014 moved"}), three)
    check("v2: a plain hyphen is the same re-open separator",
          ro_arm({"S900": "re-opens S020 - moved"}), four)

    # -- fetch: the frozen invocation and its policy -----------------------
    argv = curl_argv("https://example.com/x")
    check("curl: the silent follow-redirect flags", argv[1], "-sSL")
    check("curl: the 30 s cap", (argv[2], argv[3]), ("--max-time", "30"))
    check("curl: the browser User-Agent", argv[5], CURL_UA)
    check("curl: the User-Agent is a browser, not a bot",
          CURL_UA.startswith("Mozilla/5.0"), True)
    check("curl: the Accept header", argv[7], "Accept: " + CURL_ACCEPT)
    check("curl: the frozen Accept value", CURL_ACCEPT,
          "text/markdown, text/plain;q=0.9, */*;q=0.8")
    check("curl: the write-out trailer", argv[9], "\n%{http_code} %{url_effective}")
    check("curl: the URL is the last argument", argv[-1], "https://example.com/x")
    check("fetch: three attempts", FETCH_ATTEMPTS, 3)
    check("fetch: 30 s per attempt", FETCH_TIMEOUT, 30)
    check("fetch: the five-MiB body bound", MAX_BYTES, 5 * 1024 * 1024)
    saved_curl = run_curl
    try:
        run_curl = lambda url: (201, url, b"x")
        check("fetch: HTTP 201 is not 200",
              _outcome(lambda: fetch("https://code.claude.com/x"))[0], "OSError")
        run_curl = lambda url: (200, "https://evil.example/x", b"x")
        check("fetch: a redirect off the pinned hosts fails",
              _outcome(lambda: fetch("https://code.claude.com/x",
                                     HOSTS["Claude Code"]))[0], "OSError")
        run_curl = lambda url: (200, "https://code.claude.com/docs/en/old.md", b"x")
        check("fetch: a redirect to a base SOURCES URL fails",
              _outcome(lambda: fetch("https://code.claude.com/x", None,
                                     {"//code.claude.com/docs/en/old"}))[0],
              "OSError")
        run_curl = lambda url: (200, "https://code.claude.com/docs/CHANGELOG.md", b"x")
        check("fetch: a change-note redirect fails",
              _outcome(lambda: fetch("https://code.claude.com/x"))[0], "OSError")
        calls = []

        def flaky(url):
            calls.append(url)
            if len(calls) == 1:
                raise OSError("curl exited 6")
            return 200, url, b"page"

        run_curl = flaky
        check("fetch: a transient failure is retried",
              _outcome(lambda: fetch("https://code.claude.com/x")), ("ok", "page"))
        check("fetch: the retry took two calls", len(calls), 2)
        saved_max = MAX_BYTES
        MAX_BYTES = 3
        run_curl = lambda url: (200, url, b"four")
        check("fetch: a body over the byte bound fails",
              _outcome(lambda: fetch("https://code.claude.com/x"))[0], "OSError")
        MAX_BYTES = saved_max
    finally:
        run_curl = saved_curl

    # -- erratum E1: the live fetch accepts only the row's own base key ----
    saved_curl = run_curl
    try:
        memo = "https://code.claude.com/docs/en/memory.md"
        own = url_key(memo)
        base_keys = {own, "//cursor.com/docs/rules"}
        run_curl = lambda url: (200, memo, b"x")
        check("fetch v2: the row's own re-opened base key is accepted",
              _outcome(lambda: fetch(memo, None, base_keys, own_key=own)),
              ("ok", "x"))
        run_curl = lambda url: (200, "https://cursor.com/docs/rules.md", b"x")
        check("fetch v2: a redirect to a different base key fails",
              _outcome(lambda: fetch(memo, None, base_keys, own_key=own))[0],
              "OSError")
        run_curl = lambda url: (200, "https://example.com/x", b"x")
        check("fetch v2: a non-base final URL is still accepted",
              _outcome(lambda: fetch(memo, None, base_keys, own_key=own)),
              ("ok", "x"))
    finally:
        run_curl = saved_curl

    # -- the counter's own sha256 -----------------------------------------
    own = Path(__file__).read_bytes()
    check("the own sha256 is 64 hex", len(self_sha()), 64)
    check("the own sha256 is the sha256 of this file",
          self_sha(), hashlib.sha256(own).hexdigest())

    # -- a SUCCESSFUL end-to-end main() path (round-57 R4 / lesson M71) ----
    with tempfile.TemporaryDirectory(prefix="csr-main-") as td:
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
        (repo / "corpus" / "knowledge" / "scoped-rules-round60.md").write_text(
            entry, encoding="utf-8")
        (repo / "corpus" / "SOURCES.md").write_text(sources, encoding="utf-8")
        (repo / "corpus" / "lessons" / "round-60.md").write_text(
            lesson, encoding="utf-8")
        for sid, data in snaps.items():
            (repo / SNAPSHOT_DIR / (sid + ".page")).write_bytes(data)
        _self_git("-C", str(repo), "add", "-A", "-f", ".")
        _self_git("-C", str(repo), "-c", "user.name=c", "-c", "user.email=c@e",
                  "commit", "-q", "-m", "measured")
        measured = _self_git("-C", str(repo), "rev-parse",
                             "HEAD").stdout.decode().strip()
        good_line = ("scoped rule files backed on committed snapshots 4 of 4; "
                     "found on the live page 4 of 4")
        nofetch_line = ("scoped rule files backed on committed snapshots 4 of 4; "
                        "live not run")
        live_pages = {URLS[sid]: PAGES[sid] for sid in PAGES}

        def live_ok(url: str) -> tuple[int, str, bytes]:
            return 200, url, live_pages[url].encode()

        def live_404(url: str) -> tuple[int, str, bytes]:
            return 404, url, b"not found"

        def live_down(url: str) -> tuple[int, str, bytes]:
            raise OSError("curl exited 6")

        def live_nokey(url: str) -> tuple[int, str, bytes]:
            if url == URLS["S900"]:
                return 200, url, page900.replace(
                    '  - "src/api/**/*.ts"', "  - the api folder").encode()
            return 200, url, live_pages[url].encode()

        saved = (BASE, TARGET, lane_dir, run_curl)
        try:
            BASE, TARGET = base_sha, 4
            lane_dir = lambda: repo
            check("verify_rev accepts a real commit",
                  _outcome(lambda: verify_rev(repo, measured))[0], "ok")
            check("verify_rev rejects an unknown revision",
                  _outcome(lambda: verify_rev(repo, "0" * 40))[0], "EnvError")
            check("git_show reads a tracked file",
                  git_show(repo, measured, "SKILL.md"), skill)
            check("git_show returns None for a missing path",
                  git_show(repo, measured, "nope.md"), None)
            check("git_show_bytes reads the committed bytes",
                  git_show_bytes(repo, measured, snapshot_path("S900")),
                  snaps["S900"])
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
                   if any(l.startswith("reject " + c + ":") for c in four)], [])
            (repo / SNAPSHOT_DIR / "S900.page").write_bytes(b"working tree junk\n")
            out = io.StringIO()
            with contextlib.redirect_stdout(out):
                code = main(["--rev", measured, "--fetch"])
            check("main: a divergent working tree does not substitute (M09)",
                  (code, out.getvalue().splitlines()[0]), (0, good_line))
            run_curl = live_nokey
            out = io.StringIO()
            with contextlib.redirect_stdout(out):
                code = main(["--rev", measured, "--fetch"])
            lines = out.getvalue().splitlines()
            check("main: a live page without the key site drops F, not S",
                  (code, lines[0]),
                  (1, "scoped rule files backed on committed snapshots 4 of 4; "
                      "found on the live page 3 of 4"))
            check("main: the live key failure is named",
                  "reject Claude Code: live page: no key-form site for 'paths' "
                  "on the page" in lines, True)
            TARGET = 3
            out = io.StringIO()
            with contextlib.redirect_stdout(out):
                code = main(["--rev", measured, "--fetch"])
            check("main: the same 3 of 4 meets a target of 3", code, 0)
            TARGET = 4
            run_curl = live_404
            out = io.StringIO()
            with contextlib.redirect_stdout(out):
                code = main(["--rev", measured, "--fetch"])
            lines = out.getvalue().splitlines()
            check("main: an HTTP 404 drops F to 0 and exits 1", code, 1)
            check("main: an HTTP 404 keeps S at 4 and F at 0", lines[0],
                  "scoped rule files backed on committed snapshots 4 of 4; "
                  "found on the live page 0 of 4")
            check("main: the 404 is reported on the reject line",
                  "reject Claude Code: live fetch failed: HTTP 404 at "
                  + URLS["S900"] in lines, True)
            run_curl = live_down
            out = io.StringIO()
            with contextlib.redirect_stdout(out):
                code = main(["--rev", measured, "--fetch"])
            lines = out.getvalue().splitlines()
            check("a curl failure drops F while S holds", code, 1)
            check("a curl failure keeps S at 4 and F at 0", lines[0],
                  "scoped rule files backed on committed snapshots 4 of 4; "
                  "found on the live page 0 of 4")
            check("a curl failure names the backed rows",
                  ("reject Claude Code: live fetch failed: curl exited 6" in lines,
                   "reject Copilot CLI: live fetch failed: curl exited 6" in lines),
                  (True, True))
            run_curl = live_ok
            TARGET = None
            out = io.StringIO()
            with contextlib.redirect_stdout(out):
                got = _outcome(lambda: main(["--rev", measured, "--fetch"]))
            lines = out.getvalue().splitlines()
            check("the unfrozen sentinel is a 1, never a 0", got, ("ok", 1))
            check("the unfrozen sentinel still prints the summary",
                  lines[0], good_line)
            check("the unfrozen sentinel is named",
                  "target not frozen" in lines, True)
            TARGET = 4
            out = io.StringIO()
            with contextlib.redirect_stdout(out):
                code = main(["--rev", measured])
            lines = out.getvalue().splitlines()
            check("without --fetch the summary reads 'live not run'",
                  lines[0], nofetch_line)
            check("without --fetch the predicate is 1", code, 1)
            check("without --fetch a backed row is not rejected",
                  [l for l in lines
                   if any(l.startswith("reject " + c + ":") for c in four)], [])
            out, err = io.StringIO(), io.StringIO()
            with contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
                code = main(["--rev", base_sha, "--fetch"])
            check("a revision without SKILL.md exits 2", code, 2)
            check("a revision without SKILL.md is named",
                  "SKILL.md is missing" in err.getvalue(), True)
            # the working-tree junk must not ride into the broken commit: the
            # only difference there is the Gate line
            (repo / SNAPSHOT_DIR / "S900.page").write_bytes(snaps["S900"])
            (repo / "corpus" / "lessons" / "round-60.md").write_text(
                lesson.replace(quote900, "Rule files live elsewhere"),
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
            check("the broken world prints the three-of-four line", lines[0],
                  "scoped rule files backed on committed snapshots 3 of 4; "
                  "found on the live page 3 of 4")
            check("the broken world names the Gate on the reject line",
                  "reject Claude Code: entry row S900: round-60 Gate does not "
                  "record this quote" in lines, True)
        finally:
            BASE, TARGET, lane_dir, run_curl = saved

    # -- erratum E1: a successful end-to-end main() with two re-opens ------
    main_skill = "".join(l + "\n" for l in skill.splitlines()
                         if "Copilot CLI" not in l)
    main_entry = "".join(l + "\n" for l in entry.splitlines()
                         if "Copilot CLI" not in l)
    main_lesson = "".join(l + "\n" for l in lesson.splitlines()
                          if quote903 not in l)
    three_of = ["Claude Code", "Gemini CLI", "VS Code"]
    check("v2 fixture: two of the three measured rows are re-opens",
          sum(1 for sid in ("S900", "S901", "S902")
              if "re-opens" in REOPENS.get(sid, "")), 2)
    with tempfile.TemporaryDirectory(prefix="csr-v2-main-") as td:
        repo = Path(td)
        (repo / "corpus" / "knowledge").mkdir(parents=True)
        (repo / "corpus" / "lessons").mkdir(parents=True)
        (repo / SNAPSHOT_DIR).mkdir(parents=True)
        header = ("| id | source | kind | tier | scope | anchor | teaches | status "
                  "| opened | recheck | used-by |\n")
        (repo / "corpus" / "SOURCES.md").write_text(header + base_reopen,
                                                    encoding="utf-8")
        _self_git("init", "-q", str(repo))
        _self_git("-C", str(repo), "add", "-A", "-f", ".")
        _self_git("-C", str(repo), "-c", "user.name=c", "-c", "user.email=c@e",
                  "commit", "-q", "-m", "base")
        base_sha = _self_git("-C", str(repo), "rev-parse",
                             "HEAD").stdout.decode().strip()
        (repo / "SKILL.md").write_text(main_skill, encoding="utf-8")
        (repo / "corpus" / "knowledge" / "scoped-rules-round60.md").write_text(
            main_entry, encoding="utf-8")
        (repo / "corpus" / "SOURCES.md").write_text(
            header + base_reopen + ro_sources, encoding="utf-8")
        (repo / "corpus" / "lessons" / "round-60.md").write_text(
            main_lesson, encoding="utf-8")
        for sid, data in ro_snaps.items():
            (repo / SNAPSHOT_DIR / (sid + ".page")).write_bytes(data)
        _self_git("-C", str(repo), "add", "-A", "-f", ".")
        _self_git("-C", str(repo), "-c", "user.name=c", "-c", "user.email=c@e",
                  "commit", "-q", "-m", "measured")
        measured = _self_git("-C", str(repo), "rev-parse",
                             "HEAD").stdout.decode().strip()
        live_pages = {URLS[sid]: PAGES[sid] for sid in PAGES}

        def live_ok2(url: str) -> tuple[int, str, bytes]:
            return 200, url, live_pages[url].encode()

        saved = (BASE, TARGET, lane_dir, run_curl)
        try:
            BASE, TARGET = base_sha, 3
            lane_dir = lambda: repo
            run_curl = live_ok2
            out = io.StringIO()
            with contextlib.redirect_stdout(out):
                code = main(["--rev", measured, "--fetch"])
            lines = out.getvalue().splitlines()
            check("v2 main: 3 of 3 found with 2 re-opens exits 0", code, 0)
            check("v2 main: the exact summary line names 3 of 3", lines[0],
                  "scoped rule files backed on committed snapshots 3 of 3; "
                  "found on the live page 3 of 3")
            check("v2 main: no reject line for the three measured clients",
                  [l for l in lines
                   if any(l.startswith("reject " + c + ":") for c in three_of)], [])
        finally:
            BASE, TARGET, lane_dir, run_curl = saved

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
                page = fetch(r["url"], HOSTS[r["client"]], base_urls,
                             own_key=url_key(r["url"]))
                reasons = live_why(page, r["quote"], r["key"])
                r["found"] = not reasons
                r["live_why"] = ["live page: " + x for x in reasons]
            except Exception as e:  # network, status, pin or decode failure
                r["found"] = False
                r["live_why"] = ["live fetch failed: %s" % e]
            found += 1 if r["found"] else 0
    print(summary_line(args.fetch, len(backed), k, found))
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
                          "target": TARGET, "receipt": RECEIPT,
                          "clients": report}, indent=1))
    if TARGET is None:
        print("target not frozen")
    return predicate(args.fetch, found)


if __name__ == "__main__":
    sys.exit(main())
