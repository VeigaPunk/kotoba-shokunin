#!/usr/bin/env python3
r"""check_scoped_rules.py -- frozen counter for the round-61 C1 claim (v3).

ROUND 61 (v3).  Four arms replace or strengthen a round-60 conjunct; every
other v2 rule below is kept unchanged.  The frozen arm spec is
`plans/round-61.md` section C1 with errata E2, E2b, E2c and E2d.

  A1 semantic scope-key.  The row's Scope key K must be in its client's
  canonical key set, and K must bind a PATH-LIKE value on the cited line (the
  first value token contains both `*` and `/`, so a markdown bold marker `**`
  is not a path).  The canonical set is READ FROM THE MEASURED REVISION's
  SOURCES rows S112-S115 -- never from a literal in this file -- each of which
  declares its client's key in the pinned form `scope-key[<client>]=<key>`.
  Consequence (erratum E2d, the predicate's base clause): at a revision where
  those four rows do not exist the set is empty, no row can satisfy A1 and the
  count is 0.  Per client: Claude Code `paths`, VS Code `applyTo`, Copilot CLI
  `applyTo`, Cursor `globs`; no cross-client union.

  A2 semantic action.  The Action cell must be supported by the committed
  snapshot, not by vocabulary overlap alone: (a) every content word of the
  cell must occur on the snapshot page; (b) at least ceil(2|W|/3) of the
  cell's content words must be supported at the cited line; (c) the cited line
  must itself be supported by the cell -- at least ceil(|L|/3) of the line's
  content words must occur in the cell -- so a dense line that merely shares
  domain vocabulary is not a citation.  Word support is the word itself or a
  shared four-character prefix (`scope`~`scoped`, `instruction`~`instructions`).

  A3 canonical URL (erratum E2: byte identity amended to url_key identity
  before any data).  The five erratum-E1 sub-rules are kept -- prefix
  anchoring, target-is-a-base-row, target-URL url_key identity, the base row
  must not already carry K, and the live fetch accepts only the row's own
  re-opened key -- and a re-open row's URL must be url_key-identical to its
  base row's URL.  E2b adds (b): a FRESH row whose URL is a locale-segment or
  @version/enterprise rendering of a URL the measured table already holds for
  the same host is a rendering alias and is rejected.

  A4 snapshot provenance, four conjuncts (erratum E2c): (i) the row's recorded
  sha256 equals the committed snapshot bytes; (ii) the located quote occurs in
  them (whitespace-normalised, entity-unescaped, case preserved -- the S106
  `&#124;` escape and the S107 whitespace shaping are documented, so "byte
  exact" is reserved and not claimed here); (iii) the earliest commit that
  introduced the snapshot's bytes, walked per blob with
  `git log <rev> --reverse --find-object=<blob>` and read on the EARLIER of
  its author and committer stamps as a UTC instant, is no older than the row's
  recorded opened date -- CONSISTENCY ONLY, not acquisition authentication
  (backdated commit objects pass, and the r60 W1 bytes were never committed);
  and (iv) the row's full 64-hex snapshot sha256 must not already be recorded
  in the base-revision SOURCES table, unless the teaches cell declares
  byte-identity with `supersedes S###` (the S110 precedent).  (iv) rejects the
  recycled-byte world W1.

THE FROZEN PREDICATE (verbatim, two clauses, pinned in RECEIPT):
  `python3 -B verifiers/check_scoped_rules.py --self-test` prints
  `worlds reject 7 of 7; eligible rows pass 4 of 4` and exits 0; and
  `python3 -B verifiers/check_scoped_rules.py --rev <tip> --fetch` exits 0
  while the same command at base
  `f3246d1493b60ea1c0d947a19c39f9e08e92f326` exits 1 (no S112-S115 rows there,
  so A1's canonical set is empty and found = 0).  The self-test line is
  COMPUTED from seven constructed worlds and four constructed eligible rows,
  never printed unconditionally.  The round-60 v2 text below follows; every
  rule it states still holds unless A1-A4 above replaces it.

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
VS Code, because round-53 SOURCES rows already hold those URLs.  v2 changes
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
import datetime
import hashlib
import html
import io
import json
import os
import re
import shutil
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
PREDICATE_LINE = "worlds reject 7 of 7; eligible rows pass 4 of 4"
BASE61 = "f3246d1493b60ea1c0d947a19c39f9e08e92f326"
RECEIPT = ("C1 predicate: `" + PREDICATE_LINE + "` from --self-test (exit 0); "
           "`--rev <tip> --fetch` exits 0 while the same command at base "
           + BASE61 + " exits 1")
# A1: the canonical scope-key set is read from the committed SOURCES rows of
# these four ids AT THE MEASURED REVISION (erratum E2d), never from a key
# literal in this file.  Each row declares its client's key(s) in the pinned
# marker form `scope-key[<client>]=<key>`; at the round-61 base those rows do
# not exist, the set is empty and no row can satisfy A1 -- the base clause.
KEY_ROWS = ("S112", "S113", "S114", "S115")
KEY_DECL_RE = re.compile(r"scope-key\[([^\]`|]+)\]=([A-Za-z][A-Za-z0-9_-]*)")
SUPERSEDES_RE = re.compile(r"^supersedes\s+(S\d{3,})\b")
FETCHED_ISO_RE = re.compile(
    r"\bfetched[ \t]+\d{4}-\d{2}-\d{2}"
    r"(?:T\d{2}:\d{2}(?::\d{2}(?:\.\d+)?)?(?:Z|[+-]\d{2}:\d{2})?)?\b",
    re.IGNORECASE)
# A3(b): a path segment that is a language tag renders another locale of the
# same article; a segment carrying `@` (or starting `enterprise`) is an
# @version/enterprise rendering.  Deterministic string surgery, no semantics.
LOCALE_SEGMENTS = frozenset((
    "am", "ar", "az", "be", "bg", "bn", "bs", "ca", "cs", "cy", "da", "de",
    "el", "en", "eo", "es", "et", "eu", "fa", "fi", "fr", "ga", "gl", "he",
    "hi", "hr", "hu", "hy", "id", "is", "it", "ja", "ka", "kk", "km", "kn",
    "ko", "ky", "lo", "lt", "lv", "mk", "ml", "mn", "mr", "ms", "my", "ne",
    "nl", "no", "pa", "pl", "pt", "ro", "ru", "si", "sk", "sl", "sq", "sr",
    "sv", "sw", "ta", "te", "th", "tr", "uk", "ur", "uz", "vi", "yo", "zh",
    "zu"))
# A2: forward support (cell words at the cited line) and reverse support (the
# cited line's words inside the cell), as exact fractions, and the shared
# prefix that makes two words the same claim word.
FWD_NUM, FWD_DEN = 2, 3
REV_NUM, REV_DEN = 1, 3
SUPPORT_PREFIX = 4
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
KEY_SUFFIX_RE = re.compile(r"""["'`]?[ \t]*:""")
KEY_NEGATION_RE = re.compile(
    r"\b(?:do[ \t]+not[ \t]+use|don['’]t[ \t]+use|never[ \t]+use|avoid)\b",
    re.IGNORECASE)
BACKTICKED_IDENTIFIER_RE = re.compile(r"`([A-Za-z_][A-Za-z0-9_]*)`")
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


def _yaml_comment_start(line: str) -> int:
    """Return the first YAML comment marker outside a quoted scalar."""
    quote: str | None = None
    i = 0
    while i < len(line):
        ch = line[i]
        if quote:
            if quote == '"' and ch == "\\":
                i += 2
                continue
            if quote == "'" and ch == "'" and i + 1 < len(line) and line[i + 1] == "'":
                i += 2
                continue
            if ch == quote:
                quote = None
        elif ch in ("'", '"', "`"):
            quote = ch
        elif ch == "#" and (i == 0 or line[i - 1].isspace()):
            return i
        i += 1
    return len(line)


def key_site_guard(line: str, position: int) -> bool:
    """Reject a key occurrence in a comment or negated on the same line."""
    if position >= _yaml_comment_start(line):
        return False
    return KEY_NEGATION_RE.search(line[:position]) is None


def key_site(lines: list[str], L: int, key: str | None) -> bool:
    """Does line L hold `key` in colon-only KEY FORM with a path pattern value?"""
    if not key or L < 1 or L > len(lines):
        return False
    line = lines[L - 1]
    for i, j in key_occurrences(line, key):
        if not key_site_guard(line, i):
            continue
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


def fwd_need(n_content: int) -> int:
    """A2(b): the forward-support threshold, ceil(2|W|/3), never below 2."""
    return max(MIN_SHARED, (FWD_NUM * n_content + FWD_DEN - 1) // FWD_DEN)


def rev_need(n_line: int) -> int:
    """A2(c): the reverse-support threshold, ceil(|L|/3), never below 1."""
    return max(1, (REV_NUM * n_line + REV_DEN - 1) // REV_DEN)


def page_words(text: str) -> set[str]:
    """A2(a): the page's content words, robust to markdown code fences (which
    make backtick pairing in `content_words` swallow whole regions) and to
    citation text: lowercase `[a-z]{4,}` runs minus STOPWORDS over the WHOLE
    page, backticked spans included."""
    t = CITE_RE.sub(" ", text)
    return {w for w in CONTENT_RE.findall(t.lower()) if w not in STOPWORDS}


def supported(word: str, words: set[str]) -> bool:
    """A2: word support -- the same word, or a word sharing its first four
    characters (`scope`~`scoped`, `instruction`~`instructions`)."""
    p = word[:SUPPORT_PREFIX]
    return any(w == word or w.startswith(p) for w in words)


def covered(src: set[str], dst: set[str]) -> int:
    return sum(1 for w in src if supported(w, dst))


def g7_conjunct(lines: list[str], cell: str, L: int | None,
                page_text: str | None = None) -> list[str]:
    """Require each backticked identifier in the action to occur in raw evidence."""
    if L is None or L < 1 or L > len(lines):
        return []
    raw_line = lines[L - 1]
    raw_page = page_text if page_text is not None else "\n".join(lines)
    missing = sorted({token for token in BACKTICKED_IDENTIFIER_RE.findall(cell)
                      if token not in raw_line and token not in raw_page})
    span_missing = sorted({
        word
        for span in BACKTICK_RE.findall(cell)
        for word in span.split()
        if len(word) >= 4 and word.lower() not in STOPWORDS
        and word.lower() not in content_words(raw_line)
        and not supported(word.lower(), page_words(raw_page))})
    if missing:
        return ["A2 G7: backticked identifier(s) %s occur in neither the cited "
                "line nor the committed snapshot" % ", ".join(missing)]
    if span_missing:
        return ["A2 G7: backticked span word(s) %s occur in neither the cited "
                "line nor the committed snapshot" % ", ".join(span_missing)]
    return []


CLAUSE_AND_RE = re.compile(r"\band\b", re.IGNORECASE)
MIN_CLAUSE = 2


def split_clauses(cell: str) -> list[str]:
    """G9: split an action cell at `;` and the word `and`, outside backticks.

    Backticked spans are opaque: `` `a and b` `` is one token, so a rule that
    quotes a phrase is never split on the quote's own punctuation."""
    clauses: list[str] = []
    current: list[str] = []
    in_code = False
    i = 0
    while i < len(cell):
        ch = cell[i]
        if ch == "`":
            # Round-63 wave-2 hardening (MutW2SplitClauses/MutW2V32): mask
            # only CLOSED backtick spans, paired exactly as content_words and
            # G7 already pair them (BACKTICK_RE). A stray unpaired backtick
            # used to latch in_code for the rest of the cell and silence the
            # clause split — a one-character evasion of the G9 guard.
            in_code = any(m.start() == i for m in BACKTICK_RE.finditer(cell))
            current.append(ch)
            i += 1
            continue
        if not in_code:
            if ch == ";":
                clauses.append("".join(current))
                current = []
                i += 1
                continue
            m = CLAUSE_AND_RE.match(cell, i)
            if m is not None:
                clauses.append("".join(current))
                current = []
                i = m.end()
                continue
        current.append(ch)
        i += 1
    clauses.append("".join(current))
    return [c.strip() for c in clauses if c.strip()]


def g9_conjunct(lines: list[str], cell: str, L: int | None,
                page_text: str | None = None) -> list[str]:
    """G9: reject a clause the page supports but the cited line does not.

    The G9 class (r62 survivor `e2f-compound-purpose-outside-citation`): a
    supported sentence is extended with an unrelated purpose clause whose
    words occur elsewhere on the committed page, so A2's forward fraction,
    page containment, reverse coverage and G7 all pass. Each clause split by
    `split_clauses` must clear the same forward-support fraction A2 uses
    (`fwd_need`) against the CITED LINE. A clause the line does not support is
    rejected when the page does — a clause absent from the page too is already
    reported by A2's page-containment check, so this arm never double-reports
    it."""
    if L is None or not cell or L < 1 or L > len(lines):
        return []
    line_w = content_words(lines[L - 1])
    page = page_words(page_text if page_text is not None else "\n".join(lines))
    reasons: list[str] = []
    for clause in split_clauses(cell):
        # G9 counts CONTENT WORDS INCLUDING BACKTICKED SPANS: `content_words`
        # strips them, so a fabrication wrapped in backticks would carry too few
        # words to be checked while `page_words` still finds it on the page
        # (RevG9Guard's lane 2). MIN_CLAUSE = 2 is the floor that still checks
        # the smallest fabrication (`and uploads files`); a one-word clause is
        # below A2's own MIN_SHARED floor and stays exempt.
        w = page_words(clause)
        if len(w) < MIN_CLAUSE:
            continue
        if covered(w, line_w) >= fwd_need(len(w)):
            continue
        if covered(w, page) >= fwd_need(len(w)):
            reasons.append(
                'A2 G9: clause "%s" is supported outside the cited line'
                % clause)
    return reasons


def action_conjunct(lines: list[str], cell: str, L: int | None,
                    page_text: str | None = None) -> list[str]:
    """A2 support fractions plus G7's raw-evidence check for backticked identifiers
    and G9's cited-line check for every split clause."""
    if L is None or not cell:
        return []
    if L < 1 or L > len(lines):
        return ["A2: snapshot has no line %d for the action citation" % L]
    w = content_words(cell)
    if len(w) < MIN_CONTENT:
        return ["A2: action cell holds %d distinct content word(s) (need >= %d)"
                % (len(w), MIN_CONTENT)]
    line_w = content_words(lines[L - 1])
    need = fwd_need(len(w))
    shared = covered(w, line_w)
    if shared < need:
        return ["A2: action cell supports %d of its %d content word(s) at line "
                "%d (need >= %d)" % (shared, len(w), L, need)]
    page = page_words(page_text if page_text is not None else "\n".join(lines))
    missing = sorted(x for x in w if not supported(x, page))
    if missing:
        return ["A2: action word(s) %s do not occur on the committed snapshot"
                % ", ".join(missing)]
    back = covered(line_w, w)
    if back < rev_need(len(line_w)):
        return ["A2: the cited line's %d content word(s) are supported %d time(s) "
                "by the action cell at line %d (need >= %d): the line does not "
                "state the claim" % (len(line_w), back, L, rev_need(len(line_w)))]
    return g7_conjunct(lines, cell, L, page_text) + g9_conjunct(
        lines, cell, L, page_text)


def path_value(text: str) -> bool:
    """A1: is the first value token a PATH-LIKE glob (both `*` and `/`)?

    The v2 `pattern_value` accepts the markdown bold marker `**`
    (`sessions:**`, `order: **Team`), which the r60 ExecKeyForms probe showed
    passing A1 on prose lines; a path-like value must carry a separator."""
    tok = first_value_token(text)
    return "*" in tok and "/" in tok and PATTERN_TOKEN_RE.match(tok) is not None


def path_site(lines: list[str], L: int, key: str | None) -> bool:
    """A1: line L holds `key` in key form whose first value token is path-like."""
    if not key or L < 1 or L > len(lines):
        return False
    line = lines[L - 1]
    for i, j in key_occurrences(line, key):
        if not key_site_guard(line, i):
            continue
        m = KEY_SUFFIX_RE.match(line, j)
        if m is None:
            continue
        v = value_after(lines, L, line[m.end():])
        if v is not None and path_value(v):
            return True
    return False


def canonical_scope_keys(sources_text: str) -> dict[str, frozenset[str]]:
    """A1: the per-client canonical scope-key set, read from the committed rows
    S112-S115 of the measured revision (erratum E2d).

    A row that is absent, or declares nothing in the pinned
    `scope-key[<client>]=<key>` form, contributes nothing; a client with no
    declaration has no canonical key and no row of that client can be backed.
    Absent rows therefore make the whole set empty -- the base clause."""
    table = sources_table(sources_text)
    got: dict[str, set[str]] = {}
    for sid in KEY_ROWS:
        row = table.get(sid)
        if not row:
            continue
        for m in KEY_DECL_RE.finditer(" | ".join(row)):
            client = m.group(1).strip()
            if client in CLIENTS:
                got.setdefault(client, set()).add(m.group(2))
    return {c: frozenset(k) for c, k in got.items()}


def a1_conjunct(client: str, key: str | None,
                keys: dict[str, frozenset[str]]) -> list[str]:
    """A1: the row's Scope key is in the client's canonical key set."""
    allowed = keys.get(client) or frozenset()
    if not allowed:
        return ["A1: no canonical scope key is declared for %s (rows %s absent "
                "or undecorated at the measured revision)"
                % (client, "/".join(KEY_ROWS))]
    if key and key not in allowed:
        return ["A1: scope key %r is not a canonical key for %s (canonical: %s)"
                % (key, client, ", ".join(sorted(allowed)))]
    return []


def scope_conjunct(lines: list[str], key: str | None, L: int | None) -> list[str]:
    """A1: every reason the cited snapshot line is not a path-like key site."""
    if L is None or not key:
        return []
    if L < 1 or L > len(lines):
        return ["A1: snapshot has no line %d for scope key %r" % (L, key)]
    if not path_site(lines, L, key):
        return ["A1: scope key %r is not in key form with a path-like glob at "
                "line %d" % (key, L)]
    return []


# ------------------------------------------------- A3(b): rendering aliases

def render_form(url: str) -> tuple[str, str, bool]:
    """The (host, path, stripped) form of a URL: host lower-cased, every path
    segment that is a language tag or carries `@`/`enterprise` removed, the
    rest lower-cased.  `stripped` says whether anything was removed."""
    u = urllib.parse.urlsplit(url)
    host = (u.hostname or "").lower()
    kept, stripped = [], False
    for seg in (u.path or "").split("/"):
        if not seg:
            continue
        low = seg.lower()
        if low in LOCALE_SEGMENTS or "@" in seg or low.startswith("enterprise"):
            stripped = True
            continue
        kept.append(low)
    return host, "/".join(kept), stripped


def alias_why(url: str, others: list[tuple[str, str]]) -> list[str]:
    """A3(b): a fresh row whose URL is a locale/`@version`/enterprise rendering
    of a URL the measured table already holds for the same host.

    Only a divergence that a rendering explains is an alias: both URLs must
    reduce to the same (host, path) form, at least one must have had a segment
    stripped, and the two URLs must not be identical (an identical URL is the
    ordinary re-open case, handled by A3(a))."""
    mine = render_form(url)
    if not mine[2]:
        return []
    for sid, other in others:
        if other == url:
            continue
        if render_form(other)[:2] == mine[:2]:
            return ["A3: URL %r is a rendering alias of the committed row %s "
                    "URL %r" % (url, sid, other)]
    return []


# ------------------------------------------------------- A4: provenance

def opened_instant(opened: str) -> datetime.datetime:
    """The row's opened date as the UTC instant of its midnight."""
    return datetime.datetime.fromisoformat(opened + "T00:00:00+00:00")


def commit_instant(stamp: str) -> datetime.datetime:
    """A git date (`%aI` / `%cI`) as a UTC instant; offsets are honoured."""
    return datetime.datetime.fromisoformat(stamp.strip()).astimezone(
        datetime.timezone.utc)


def intro_why(sid: str, opened: str, intro: tuple[str, str] | None) -> list[str]:
    """A4(iii), consistency only: the commit that introduced the snapshot's
    bytes is no older than the row's opened date.

    The EARLIER of the author and committer stamps decides, so a commit whose
    two fields straddle the boundary fails.  This authenticates internal
    provenance consistency only; a backdated commit object passes (declared)."""
    if not intro:
        return []
    author, committer = intro
    earliest = min(commit_instant(author), commit_instant(committer))
    if earliest < opened_instant(opened):
        return ["A4: snapshot %s bytes were introduced at %s, older than the "
                "row's opened date %s"
                % (snapshot_path(sid), earliest.isoformat(), opened)]
    return []


def alias_sha_why(sha: str, base_shas: dict[str, str],
                  teaches: str | None) -> list[str]:
    """A4(iv): a supersedes exemption must target the base row owning the sha
    and cannot carry a fresh-fetched timestamp."""
    sid = base_shas.get(sha)
    if not sid:
        return []
    declaration = SUPERSEDES_RE.match(teaches or "")
    if declaration:
        target = declaration.group(1)
        if target != sid:
            return ["A4: supersedes target %s differs from base row %s that owns "
                    "the snapshot sha256" % (target, sid)]
        if FETCHED_ISO_RE.search(teaches or ""):
            return ["A4: supersedes %s declares byte identity but the teaches "
                    "cell also asserts a fetched ISO timestamp" % target]
        return []
    return ["A4: snapshot sha256 %s... is already recorded by base row %s and "
            "the teaches cell declares no supersedes" % (sha[:12], sid)]


def snapshot_intro(lane: Path, rev: str, sid: str) -> tuple[str, str] | None:
    """A4(iii): the (author, committer) stamps of the earliest commit in the
    history of `rev` that introduced the snapshot's bytes anywhere.

    The blob is resolved at `rev` and walked with `--find-object`, so a copy
    introduced earlier under another path is seen; `--all` is never used, so an
    unrelated branch cannot reject the measured revision."""
    path = snapshot_path(sid)
    r = git(lane, ["rev-parse", "--verify", "--quiet", "%s:%s" % (rev, path)])
    if r.returncode != 0 or not r.stdout.strip():
        return None
    blob = r.stdout.decode().strip()
    r = git(lane, ["log", rev, "--reverse", "--format=%aI%x09%cI",
                   "--find-object=%s" % blob])
    if r.returncode != 0:
        return None
    for line in r.stdout.decode().splitlines():
        author, sep, committer = line.partition("\t")
        if sep and author.strip() and committer.strip():
            return author.strip(), committer.strip()
    return None


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
                      keys: dict[str, frozenset[str]] | None = None,
                      all_urls: list[tuple[str, str]] | None = None,
                      base_shas: dict[str, str] | None = None,
                      snapshot_of=None, intro_of=None) -> tuple[list[str], dict]:
    """Judge one entry row.  Returns (why, picked) where `picked` carries the
    row's sid, url, quote, scope key and key line.

    A malformed token has already been rejected on the SKILL.md side, so the
    entry row only looks for a token span when a token was read at all."""
    why: list[str] = []
    sid = url = quote = key = None
    key_line: int | None = None
    keys = keys or {}
    all_urls = all_urls or []
    base_shas = base_shas or {}
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
    why.extend(a1_conjunct(client, key, keys))
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
            teaches = s[6] if len(s) > 6 else ""
            reopens = REOPEN_RE.match(teaches)
            if not url:
                why.append("%s source cell holds no URL" % sid)
            else:
                # A3(a) / erratum E1: a base-keyed URL needs a valid re-open,
                # and any `re-opens S###` declaration must be url_key-identical
                # to the base row it names.
                if url_key(url) in base_urls or reopens:
                    reopen = reopen_why(s, url, key, base_rows, base_lines)
                    if url_key(url) in base_urls and reopen:
                        why.append("%s URL %r is already a base SOURCES URL"
                                   % (sid, url))
                    why.extend(reopen)
                if not reopens:
                    why.extend(alias_why(url, all_urls))
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
                why.extend(alias_sha_why(sha, base_shas, teaches))
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
                        for reason in action_conjunct(lines, action_cell,
                                                      action_line, page):
                            why.append("snapshot %s: %s" % (snapshot_path(sid), reason))
                        why.extend(intro_why(sid, s[8], intro_of(sid)
                                             if intro_of else None))
    return why, {"row": sid, "url": url, "quote": quote, "key": key,
                 "key_line": key_line}


def judge(skill: str, entry: str, sources: str, lesson: str,
          base_sources: str, snapshot_of=None, intro_of=None) -> list[dict]:
    srows = skill_rows(skill)
    erows = entry_rows(entry)
    table = sources_table(sources)
    at_base = source_ids(base_sources)
    base_urls = base_url_keys(base_sources)
    base_rows = sources_table(base_sources)
    base_lines = base_line_map(base_sources)
    keys = canonical_scope_keys(sources)
    base_shas: dict[str, str] = {}
    for bsid, brow in base_rows.items():
        bsha = row_sha(brow)
        if bsha:
            base_shas.setdefault(bsha, bsid)
    all_urls: list[tuple[str, str]] = []
    for msid, mrow in table.items():
        murls = urls_of(mrow[1]) if len(mrow) > 1 else []
        if murls:
            all_urls.append((msid, murls[0]))
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
                keys, all_urls, base_shas, snapshot_of, intro_of)
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


def _self_git(*args: str, data: bytes | None = None,
              env: dict | None = None) -> subprocess.CompletedProcess:
    r = subprocess.run(["git"] + list(args), input=data, capture_output=True,
                       env=env)
    if r.returncode != 0:
        raise EnvError("git %s failed: %s"
                       % (args[0], r.stderr.decode(errors="replace").strip()))
    return r


# ----------------------------------------------------------------- self-test

def self_test() -> int:
    """The round-61 C1 self-test.

    v2's unit checks that still hold are kept.  The four arms get must-fail
    fixtures; the five erratum-E1 sub-rules are ported; and the seven worlds
    W1-W7, the do-nothing world W0 and the four eligible rows are built as
    real git repositories here and scored through the SAME judge/fetch path the
    CLI uses.  The predicate line is computed from those verdicts, never
    printed unconditionally."""
    global BASE, TARGET, lane_dir, run_curl
    assertions = 0
    failures = 0
    temps: list[str] = []

    def check(name: str, actual: object, expected: object) -> None:
        nonlocal assertions, failures
        assertions += 1
        if actual != expected:
            failures += 1
            print("FAIL %s: got %r, expected %r" % (name, actual, expected))

    def named(reasons: list[str], needle: str) -> bool:
        return any(needle in r for r in reasons)

    try:
        # -- the revision guard (v2) -------------------------------------
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

        # -- token well-formedness (v2, unchanged) ------------------------
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
        check("green: a leading ~/ is stripped",
              token_well_formed("~/.claude/rules/"), True)
        check("green: a leading ./ is stripped",
              token_well_formed("./.github/instructions/"), True)
        check("green: a dot-led non-final segment is fine (E7)",
              token_well_formed(".github/.instructions/config.md"), True)
        check("green: an 'instructions' segment is allowed",
              token_well_formed(".claude/instructions/rules.md"), True)
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
        check("red segments: rules is one segment", token_well_formed("rules"), False)
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
        check("red segment word: .claude-plugin/rules.md (a plugin segment)",
              token_well_formed(".claude-plugin/rules.md"), False)
        check("red E7: .claude/1.0/rules.md (a version segment)",
              token_well_formed(".claude/1.0/rules.md"), False)
        check("red E7: ~/.claude/1.0.0/rules.md",
              token_well_formed("~/.claude/1.0.0/rules.md"), False)

        # -- normalise: case preserved (v2) ------------------------------
        check("normalise strips one leading ~/",
              normalise("~/.claude/rules/"), ".claude/rules")
        check("normalise strips one trailing /",
              normalise(".cursor/rules/"), ".cursor/rules")
        check("normalise preserves case",
              normalise(".Claude/Rules.md"), ".Claude/Rules.md")
        check("normalise of nothing is empty", normalise(None), "")

        # -- the foreign-name guard (v2) ---------------------------------
        check("a .claude token is foreign to VS Code",
              foreign_marker("VS Code", ".claude/rules/"), "Claude Code")
        check("a .claude token is not foreign to Claude Code",
              foreign_marker("Claude Code", ".claude/rules/"), None)
        check("a .cursor token is not foreign to Cursor",
              foreign_marker("Cursor", ".cursor/rules/"), None)
        check("the marker match is case-insensitive",
              foreign_marker("VS Code", ".Claude/Rules.md"), "Claude Code")
        check("a marker-neutral token is nobody's foreign token",
              foreign_marker("Copilot CLI", ".github/instructions/"), None)

        # -- the quote: bounds, token span, the outside rule word (v2) ----
        check("quote word count: six words pass",
              MIN_WORDS <= len("one two three four five six".split()) <= MAX_WORDS, True)
        check("quote word count: five words fail",
              MIN_WORDS <= len("one two three four five".split()) <= MAX_WORDS, False)
        check("strip straight quotes", strip_quotes('"hello world"'), "hello world")
        check("strip curly quotes", strip_quotes("\u201chello world\u201d"), "hello world")
        check("keep an unquoted cell", strip_quotes("hello world"), "hello world")
        q = "Rule files live in .claude/rules/ and each rule names the files"
        span = token_span(q, ".claude/rules/")
        check("the raw token is found in the quote", span is not None, True)
        check("a rule word sits outside the token span",
              rule_word_outside(q, span[0], span[1]), True)
        check("the token match is case-sensitive",
              token_span(".Claude/Rules.md is used", ".claude/rules.md"), None)
        check("a token inside a longer path is not spanned (left boundary)",
              token_span("x.claude/rules.md here", ".claude/rules.md"), None)
        check("a token followed by a word is not spanned (right boundary)",
              token_span(".claude/rulesfoo here", ".claude/rules"), None)
        check("rulebook is not the whole word rule",
              rule_word_outside("Rulebook entries differ here", 0, 0), False)

        # -- the Gate quote rule (inherited from r59, kept) ---------------
        gate = "## Gate\n\n| row | quote |\n|---|---|---|\n| S1 | \"the rule folder lives here\" |\n"
        gs = gate_section(gate)
        check("gate section is read", ws(gs).count("the rule folder lives here"), 1)
        check("quote recorded in the Gate", quote_in_gate(
            "the rule folder lives here", ws(gs), ws(gs.replace("`", ""))), True)
        check("quote absent from the Gate", quote_in_gate(
            "the rule folder lives elsewhere", ws(gs), ws(gs.replace("`", ""))), False)
        check("an empty Gate records no quote",
              quote_in_gate("the rule folder lives here", ws(""), ws("")), False)

        # -- URL normalisation and host pins (v2) -------------------------
        check("url_key drops a trailing .md",
              url_key("https://code.claude.com/docs/en/rules.md"),
              url_key("https://code.claude.com/docs/en/rules"))
        check("url_key drops a fragment and a query",
              (url_key("https://cursor.com/docs/rules#x"),
               url_key("https://cursor.com/docs/rules?a=1")),
              ("//cursor.com/docs/rules", "//cursor.com/docs/rules"))
        check("url_key lower-cases scheme, host and path",
              url_key("HTTPS://Code.Claude.com/Docs"), "//code.claude.com/docs")
        check("url_key of nothing is empty", url_key(None), "")
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

        # -- page normalisation and the quote check (v2) ------------------
        check("page style and script text is dropped",
              "@layer base" in norm_page(
                  "<style>@layer base{}</style><p>x</p><script>@layer base</script>"), False)
        check("page tags are dropped and text kept",
              norm_page("<p>Use <code>/a-b</code> rules</p>"), "use /a-b rules")
        check("page_plain drops `*`, `_` and backticks but keeps case",
              page_plain("A*b_c`D"), "AbcD")
        page_ok = "<p>Rule files live in a <code>.claude/rules/</code> folder</p>"
        quote_ok = "Rule files live in a .claude/rules/ folder"
        check("quote found on the page", quote_why(page_ok, quote_ok), [])
        check("quote absent from the page",
              quote_why(page_ok, "Rule files live in a folder"),
              ["the quote is not on the page"])

        # -- the SOURCES sha256 pin and the snapshot path (v2) ------------
        sha_full = "971d75bfce7a04c2e0d41e8752d01afe29ed500f2a7159f66d5f7156bea0c3ff"
        check("row_sha reads a plain sha256 <64 hex>",
              row_sha(["S900", "x", "docs", "A", "s", "sha256 " + sha_full]), sha_full)
        check("row_sha of an ellipsis digest is None",
              row_sha(["S900", "x", "docs", "A", "s", "sha256 `9a67de89\u2026`"]), None)
        check("row_sha takes the FIRST digest when two are printed",
              row_sha(["S900", "x", "docs", "A", "s",
                       "sha256 " + sha_full + " then sha256 " + "a" * 64]), sha_full)
        check("snapshot_path names the S-id page",
              snapshot_path("S900"), ".ufo/waves/round-60/snapshots/S900.page")

        # -- output lines, the receipt label and the predicate (v2) -------
        check("fetch summary line", summary_line(True, 0, 0, 0),
              "scoped rule files backed on committed snapshots 0 of 0; "
              "found on the live page 0 of 0")
        check("non-fetch summary line", summary_line(False, 2, 7, 0),
              "scoped rule files backed on committed snapshots 2 of 7; live not run")
        check("reject line", reject_line("Cursor", ["a", "b"]), "reject Cursor: a; b")
        check("the receipt label pins the full two-clause sentence",
              (RECEIPT.startswith("C1 predicate: `worlds reject 7 of 7; eligible rows pass 4 of 4`"),
               "--rev <tip> --fetch` exits 0" in RECEIPT,
               "f3246d1493b60ea1c0d947a19c39f9e08e92f326 exits 1" in RECEIPT),
              (True, True, True))
        check("E3: url_is_change_note on each word",
              [url_is_change_note("https://x.com/a/%s/b" % w) for w in CHANGE_NOTE_WORDS],
              [True] * len(CHANGE_NOTE_WORDS))
        check("E3: a docs URL is not a change note",
              url_is_change_note("https://code.claude.com/docs/en/rules"), False)
        check("TARGET is the frozen census target", TARGET, 3)
        frozen = TARGET
        try:
            TARGET = 3
            check("predicate: fetch, 3 found, passes", predicate(True, 3), 0)
            check("predicate: fetch, 2 found, fails", predicate(True, 2), 1)
            check("predicate: no fetch always fails", predicate(False, 7), 1)
            TARGET = None
            check("predicate: no target is a 1, never a 0",
                  _outcome(lambda: predicate(True, 7)), ("ok", 1))
        finally:
            TARGET = frozen

        # -- the Scope key cell (v2) --------------------------------------
        check("key: a bare identifier is the key", scope_key("`paths` (S900 :5)"),
              ("paths", []))
        check("key: the FIRST backticked span is the key",
              scope_key("`alwaysApply` and `paths` (S900 :5)")[0], "alwaysApply")
        check("key: a cell without backticks has no key",
              scope_key("paths (S900 :5)"),
              (None, ["SKILL.md scope key cell holds no backticked key"]))
        check("citations: both forms are read",
              citations("`paths` (S900 :5) and S901:7"), [("S900", 5), ("S901", 7)])
        check("citation: another row's id is a named failure",
              citation_why("`paths` (S901 :5)", "S900", "SKILL.md scope key cell"),
              (None, ["SKILL.md scope key cell cites S901 :5, not the row's own "
                      "source S900"]))

        # -- the key form and its value (v2) ------------------------------
        check("value: a quoted glob is a pattern", pattern_value(" '**/*.py'"), True)
        check("value: a sentence that mentions a pattern is not",
              pattern_value(' "Applies to **/*.ts"'), False)
        check("value: the token stops at a comma", first_value_token("a/*.ts, b/*.py"),
              "a/*.ts")
        check("value: only [ | > is a block value", block_only(" ["), True)
        check("key form: a block value two lines down passes",
              key_site(["paths:", '  - "src/api/**/*.ts"'], 1, "paths"), True)
        check("key form: the cited pattern line itself carries no key",
              key_site(["paths:", '  - "src/api/**/*.ts"'], 2, "paths"), False)
        check("key form: a block value four lines down fails",
              key_site(["paths:", "", "", "", '  - "src/api/**/*.ts"'], 1, "paths"), False)
        check("key form: the Cursor census line passes",
              key_site(["globs: src/components/**/*.tsx"], 1, "globs"), True)
        check("key form: the VS Code census line passes",
              key_site(["applyTo: '**/*.py'"], 1, "applyTo"), True)
        check("key form: description at a line with no pattern fails",
              key_site(["description: RPC service conventions and patterns"], 1,
                       "description"), False)
        check("key form: a key inside a longer identifier fails",
              key_site(['xpaths: "**/*.ts"'], 1, "paths"), False)
        check("key form: equals is not a colon-only key form",
              key_site(["applyTo='**/*.py'"], 1, "applyTo"), False)
        check("key form: a commented key is not a site",
              key_site(["# paths: src/legacy/**/*.ts"], 1, "paths"), False)
        check("key form: no key is never a site", key_site(["paths:"], 1, None), False)
        check("any key site: a later line is found",
              any_key_site("intro\n\nglobs: src/*.tsx\n", "globs"), True)
        check("A1 site: a negated path key is not a site",
              path_site(["Do not use paths: src/legacy/**/*.ts"], 1, "paths"), False)
        check("A1 site: a commented path key is not a site",
              path_site(["# paths: src/legacy/**/*.ts"], 1, "paths"), False)

        # -- A1: the path-like value (new in v3) --------------------------
        check("A1 value: a path glob is path-like", path_value(" '**/*.py'"), True)
        check("A1 value: a bare ** is not path-like (the bold-marker hole)",
              path_value("**"), False)
        check("A1 value: Configure** is not path-like", path_value("Configure**"), False)
        check("A1 value: **Team is not path-like", path_value("**Team"), False)
        check("A1 value: a sentence mentioning a pattern is not",
              path_value(' "Applies to **/*.ts"'), False)
        check("A1 site: the real Cursor line passes",
              path_site(["globs: src/components/**/*.tsx"], 1, "globs"), True)
        check("A1 site: the VS Code sessions bold line fails",
              path_site(["Local harness sessions: **See the table below.**"], 1,
                        "sessions"), False)
        check("A1 site: the Cursor order bold line fails",
              path_site(["order: **Team Rules then Project Rules**"], 1, "order"), False)

        # -- A1: the canonical key set read from the committed rows -------
        decl = ("| S112 | Claude Code docs \u2014 https://code.claude.com/docs/en/x.md "
                "| docs | A | s | a | scope-key[Claude Code]=paths | mined "
                "| 2026-10-23 | 90d | y |\n"
                "| S113 | VS Code docs \u2014 https://code.visualstudio.com/docs/x.md "
                "| docs | A | s | a | scope-key[VS Code]=applyTo | mined "
                "| 2026-10-23 | 90d | y |\n"
                "| S114 | Copilot docs \u2014 https://docs.github.com/en/copilot/x.md "
                "| docs | A | s | a | scope-key[Copilot CLI]=applyTo | mined "
                "| 2026-10-23 | 90d | y |\n"
                "| S115 | Cursor docs \u2014 https://cursor.com/docs/rules "
                "| docs | A | s | a | scope-key[Cursor]=globs | mined "
                "| 2026-10-23 | 90d | y |\n")
        keys = canonical_scope_keys(decl)
        check("A1 set: four clients, three distinct keys",
              {c: sorted(keys.get(c) or ()) for c in
               ("Claude Code", "VS Code", "Copilot CLI", "Cursor")},
              {"Claude Code": ["paths"], "VS Code": ["applyTo"],
               "Copilot CLI": ["applyTo"], "Cursor": ["globs"]})
        check("A1 set: no cross-client union",
              ("applyTo" in (keys.get("Cursor") or ())),
              False)
        check("A1 set: absent rows give the empty set (the base clause)",
              canonical_scope_keys("| id | source | kind | tier | scope | anchor "
                                   "| teaches | status | opened | recheck | used-by |\n"),
              {})
        check("A1: a canonical key passes", a1_conjunct("Claude Code", "paths", keys), [])
        check("A1: patterns is not canonical for Claude Code",
              a1_conjunct("Claude Code", "patterns", keys),
              ["A1: scope key 'patterns' is not a canonical key for Claude Code "
               "(canonical: paths)"])
        check("A1: sessions is not canonical for VS Code",
              len(a1_conjunct("VS Code", "sessions", keys)), 1)
        check("A1: rules is not canonical for Cursor",
              len(a1_conjunct("Cursor", "rules", keys)), 1)
        check("A1: an empty set rejects every key",
              len(a1_conjunct("Codex", "paths", keys)), 1)

        # -- A2: forward/reverse support and the page support -------------
        check("A2 need: 3 words need 2 forward", fwd_need(3), 2)
        check("A2 need: 6 words need 4 forward", fwd_need(6), 4)
        check("A2 need: 8 words need 6 forward (v2 needed 4)", fwd_need(8), 6)
        check("A2 need: 11 words need 8 forward", fwd_need(11), 8)
        check("A2 reverse need: a 3-word line needs 1", rev_need(3), 1)
        check("A2 reverse need: a 30-word line needs 10", rev_need(30), 10)
        check("A2 support: scope~scoped", supported("scope", {"scoped"}), True)
        check("A2 support: instruction~instructions",
              supported("instruction", {"instructions"}), True)
        check("A2 support: rule does not support rebook", supported("rule", {"rebook"}), False)
        check("A2 page words survive markdown code fences",
              "fence" in page_words("```\nfence words here\n```"), True)
        check("A2 cell words drop backticks, citations and stopwords",
              content_words("Scope `the` rule (S900 :3) with every file"),
              {"scope", "rule", "file"})
        check("A2: a cell the cited line supports passes",
              action_conjunct(["Scope rules to specific files using matching patterns."],
                              "Scope rules to specific files using matching patterns. "
                              "(S900 :1)", 1,
                              "Scope rules to specific files using matching patterns."),
              [])
        check("A2: a cell whose words the page lacks is rejected",
              named(action_conjunct(["Scope the quantum lattice by frobnicating it."],
                                    "Scope the quantum lattice by frobnicating it. "
                                    "(S900 :1)", 1,
                                    "Scope rules to specific files using matching patterns."),
                    "do not occur on the committed snapshot"), True)
        check("A2: an invented cell against a dense line is rejected",
              named(action_conjunct(
                  ["Rules without a `paths` field are loaded unconditionally and "
                   "apply to all files. A path-scoped rule loads when the agent "
                   "uses a reading tool on a matching file."],
                  "Create the rule file in the project and add frontmatter so it "
                  "loads only for the matching files. (S900 :1)", 1,
                  "Rules without a `paths` field are loaded unconditionally and "
                  "apply to all files. A path-scoped rule loads when the agent "
                  "uses a reading tool on a matching file."),
                  "A2:"), True)
        check("A2 G7: an unsupported backticked identifier is rejected",
              named(action_conjunct(
                  ["When agent reads file runtime emits event and loads matching rule files."],
                  "When agent reads file runtime emits event and loads matching rule files "
                  "`InstructionsLoaded`.", 1,
                  "When agent reads file runtime emits event and loads matching rule files."),
                    "G7"), True)
        # G9 discriminating arms (round 63, MutG9Guard's named missing
        # assertions): one per split boundary and per shortcut a mutant takes.
        g9_line = "The configuration stores project rules using glob syntax."
        g9_page = (g9_line + " An unrelated section: the agent secretly uploads "
                   "files and stores secrets exfiltrated nightly.")
        g9_after = " secretly uploads files."
        check("A2 G9: an `and`-joined purpose clause off the cited line is rejected",
              named(action_conjunct(
                  [g9_line],
                  g9_line[:-1] + " and" + g9_after + " (S900 :1)",
                  1, g9_page), "G9"), True)
        check("A2 G9: a `;`-joined purpose clause off the cited line is rejected",
              named(action_conjunct(
                  [g9_line],
                  g9_line[:-1] + ";" + g9_after + " (S900 :1)",
                  1, g9_page), "G9"), True)
        check("A2 G9: a clause with one shared word is still rejected (need 2)",
              named(action_conjunct(
                  [g9_line],
                  g9_line[:-1] + " and stores secrets exfiltrated. (S900 :1)",
                  1, g9_page), "G9"), True)
        check("A2 G9: a backticked fabrication is counted and rejected",
              named(action_conjunct(
                  [g9_line],
                  g9_line[:-1] + " and `secretly uploads files`. (S900 :1)",
                  1, g9_page), "G9"), True)

        # -- A3: url_key identity and the rendering-alias arm -------------
        check("A3: /docs/rules and /docs/rules.md are url_key-identical",
              url_key("https://cursor.com/docs/rules"),
              url_key("https://cursor.com/docs/rules.md"))
        base_pair = [("S010", "https://code.claude.com/docs/en/memory.md")]
        check("A3(b): a /de/ rendering of a committed /en/ URL is an alias",
              len(alias_why("https://code.claude.com/docs/de/memory.md", base_pair)), 1)
        check("A3(b): an enterprise rendering is an alias",
              len(alias_why(
                  "https://docs.github.com/en/enterprise-cloud@latest/copilot/x.md",
                  [("S011", "https://docs.github.com/en/copilot/x.md")])), 1)
        check("A3(b): the identical URL is not an alias",
              alias_why("https://code.claude.com/docs/en/memory.md", base_pair), [])
        check("A3(b): a .md spelling is not a rendering alias",
              alias_why("https://cursor.com/docs/rules",
                        [("S012", "https://cursor.com/docs/rules.md")]), [])
        check("A3(b): a different article on the same host is not an alias",
              alias_why("https://code.claude.com/docs/en/claude-directory.md",
                        base_pair), [])

        # -- A4: the alias-sha conjunct and the introduction date ---------
        page_bytes = b"a page\n"
        sha = hashlib.sha256(page_bytes).hexdigest()
        check("A4(iv): a full sha already in the base table is rejected",
              len(alias_sha_why(sha, {sha: "S043"}, "the row")), 1)
        check("A4(iv): a matching supersedes declaration exempts it",
              alias_sha_why(sha, {sha: "S043"}, "supersedes S043 \u2014 byte-identical"),
              [])
        check("A4(iv): a different supersedes target is rejected",
              len(alias_sha_why(sha, {sha: "S043"},
                                "supersedes S096 \u2014 byte-identical")), 1)
        check("A4(iv): a supersedes target with a fetched timestamp is rejected",
              len(alias_sha_why(sha, {sha: "S043"},
                                "supersedes S043 \u2014 fetched "
                                "2026-10-23T12:00:00Z")), 1)
        check("A4(iv): a sha absent from the base table passes",
              alias_sha_why(sha, {"a" * 64: "S043"}, "the row"), [])
        check("A4(iv): an ellipsis pin never aliases",
              alias_sha_why(sha, {}, "the row"), [])
        check("A4(iii): an introduction older than opened is rejected",
              len(intro_why("S900", "2026-10-23",
                            ("2026-10-22T20:04:43+00:00",
                             "2026-10-22T20:04:43+00:00"))), 1)
        check("A4(iii): an introduction on the opened day (UTC) passes",
              intro_why("S900", "2026-10-23",
                        ("2026-10-23T12:28:13+00:00",
                         "2026-10-23T12:28:13+00:00")), [])
        check("A4(iii): a local date on the opened day but UTC the day before is rejected",
              len(intro_why("S900", "2026-10-23",
                            ("2026-10-23T00:30:00+03:00",
                             "2026-10-23T00:30:00+03:00"))), 1)
        check("A4(iii): the earlier of author and committer decides",
              len(intro_why("S900", "2026-10-23",
                            ("2026-10-22T20:00:00+00:00",
                             "2026-10-23T19:00:00+00:00"))), 1)

        # -- erratum E1, sub-rules 1-4 (ported from v2) -------------------
        e1_base = ("| id | source | kind | tier | scope | anchor | teaches | status "
                   "| opened | recheck | used-by |\n"
                   "| S010 | Base \u2014 https://code.claude.com/docs/en/memory.md "
                   "| docs | A | s | a | t | mined | 2026-10-22 | 90d | y |\n"
                   "| S020 | Base \u2014 https://cursor.com/docs/rules.md "
                   "| docs | A | s | a | paths | mined | 2026-10-22 | 90d | y |\n")
        e1_rows = sources_table(e1_base)
        e1_lines = base_line_map(e1_base)
        memo = "https://code.claude.com/docs/en/memory.md"

        def e1_row(teaches: str) -> list[str]:
            return ["S900", "x", "docs", "A", "s", "a", teaches, "mined",
                    "2026-10-23", "90d", "y"]

        check("E1 sub-rule 1: an anchored re-open prefix is accepted",
              reopen_why(e1_row("re-opens S010 \u2014 moved"), memo, "paths",
                         e1_rows, e1_lines), [])
        check("E1 sub-rule 1: a plain hyphen is the same separator",
              reopen_why(e1_row("re-opens S010 - moved"), memo, "paths",
                         e1_rows, e1_lines), [])
        check("E1 sub-rule 1: a mid-cell mention is not a re-open",
              len(reopen_why(e1_row("supersedes S089 \u2014 re-opens S010 \u2014 moved"),
                             memo, "paths", e1_rows, e1_lines)), 1)
        check("E1 sub-rule 2: a target that is not a base row rejects",
              len(reopen_why(e1_row("re-opens S777 \u2014 moved"), memo, "paths",
                             e1_rows, e1_lines)), 1)
        check("E1 sub-rule 3: a target whose URL differs rejects",
              len(reopen_why(e1_row("re-opens S020 \u2014 moved"), memo, "paths",
                             e1_rows, e1_lines)), 1)
        check("E1 sub-rule 4: a base row already carrying K rejects",
              len(reopen_why(e1_row("re-opens S020 \u2014 moved"),
                             "https://cursor.com/docs/rules.md", "paths",
                             e1_rows, e1_lines)), 1)

        # -- the fetch policy (v2) ----------------------------------------
        argv = curl_argv("https://example.com/x")
        check("curl: the silent follow-redirect flags", argv[1], "-sSL")
        check("curl: the 30 s cap", (argv[2], argv[3]), ("--max-time", "30"))
        check("curl: the browser User-Agent", argv[5], CURL_UA)
        check("curl: the frozen Accept value", CURL_ACCEPT,
              "text/markdown, text/plain;q=0.9, */*;q=0.8")
        check("curl: the write-out trailer", argv[9], "\n%{http_code} %{url_effective}")
        check("fetch: three attempts", FETCH_ATTEMPTS, 3)
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
            check("E1 sub-rule 5: a redirect to a base SOURCES URL fails",
                  _outcome(lambda: fetch("https://code.claude.com/x", None,
                                         {"//code.claude.com/docs/en/old"}))[0],
                  "OSError")
            memo = "https://code.claude.com/docs/en/memory.md"
            own = url_key(memo)
            base_keys = {own, "//cursor.com/docs/rules"}
            run_curl = lambda url: (200, memo, b"x")
            check("E1 sub-rule 5: the row's own base key is accepted",
                  _outcome(lambda: fetch(memo, None, base_keys, own_key=own)),
                  ("ok", "x"))
            run_curl = lambda url: (200, "https://cursor.com/docs/rules.md", b"x")
            check("E1 sub-rule 5: a redirect to a different base key fails",
                  _outcome(lambda: fetch(memo, None, base_keys, own_key=own))[0],
                  "OSError")
        finally:
            run_curl = saved_curl

        # -- the world builder -------------------------------------------
        DATE_DATA = "2026-10-23T09:28:13-03:00"   # literal: r60 data commit 7b80ae8
        DATE_BASE = "2026-10-22T20:04:43+00:00"   # literal: r53 S043 fetch
        DATE_OLD = "2026-10-22T20:04:43+00:00"

        def commit_env(date: str) -> dict:
            return dict(os.environ, GIT_AUTHOR_DATE=date, GIT_COMMITTER_DATE=date,
                        GIT_AUTHOR_NAME="csr", GIT_AUTHOR_EMAIL="csr@example.invalid",
                        GIT_COMMITTER_NAME="csr", GIT_COMMITTER_EMAIL="csr@example.invalid")

        def build(base_files, files: dict, base_date: str = DATE_BASE,
                  measured_date: str = DATE_DATA) -> tuple[Path, str, str]:
            if isinstance(base_files, str):
                base_files = {SOURCES: base_files}
            td = tempfile.mkdtemp(prefix="csr-world-")
            temps.append(td)
            repo = Path(td)

            def write(tree: dict) -> None:
                for rel, data in tree.items():
                    p = repo / rel
                    p.parent.mkdir(parents=True, exist_ok=True)
                    p.write_bytes(data if isinstance(data, bytes) else data.encode())

            def commit(msg: str, date: str) -> str:
                env = commit_env(date)
                _self_git("-C", str(repo), "add", "-A", "-f", ".", env=env)
                _self_git("-C", str(repo), "-c", "commit.gpgsign=false", "commit",
                          "-q", "--allow-empty", "-m", msg, env=env)
                return _self_git("-C", str(repo), "rev-parse", "HEAD").stdout.decode().strip()

            _self_git("init", "-q", str(repo))
            write(base_files)
            base = commit("base", base_date)
            write(files)
            measured = commit("measured", measured_date)
            return repo, base, measured

        QUOTES = {
            "S900": ("Rules for larger projects live in a `.claude/rules/` directory "
                     "and each rule names its files"),
            "S901": ("VS Code targeted instruction files live in "
                     "`.github/instructions/**/*.instructions.md` for a workspace"),
            "S902": ("Copilot CLI reads instruction files from the "
                     "`.github/instructions/` folder in the repository"),
            "S903": ("Project rules live in `.cursor/rules` as `.mdc` files and are "
                     "version-controlled"),
        }
        PAGES = {
            "S900": ("Claude Code scoped rule files\n"
                     + QUOTES["S900"] + ".\n"
                     "paths:\n"
                     '  - "src/api/**/*.ts"\n'
                     "Scope rules to specific files using YAML frontmatter; apply "
                     "only when matching specified patterns.\n"),
            "S901": ("VS Code targeted instruction files\n"
                     + QUOTES["S901"] + ".\n"
                     "applyTo: '**/*.py'\n"
                     "Use multiple instruction files per topic and apply them "
                     "selectively.\n"),
            "S902": ("Copilot CLI modular instruction files\n"
                     + QUOTES["S902"] + ".\n"
                     'applyTo: "app/models/**/*.rb"\n'
                     "Create a path-specific instruction file with an `applyTo` "
                     "glob; use glob syntax to specify the files or directories "
                     "the instructions apply to.\n"),
            "S903": ("Cursor project rules\n"
                     + QUOTES["S903"] + ".\n"
                     "globs: src/components/**/*.tsx\n"
                     "Use `globs` to scope a rule to specific files or directories. "
                     "Separate multiple patterns with commas.\n"),
        }
        ACTIONS = {
            "S900": ("Scope rules to specific files using YAML frontmatter; apply "
                     "only when matching specified patterns."),
            "S901": "Use multiple instruction files per topic and apply them selectively.",
            "S902": ("Create a path-specific instruction file with an `applyTo` glob; "
                     "use glob syntax to specify the files or directories the "
                     "instructions apply to."),
            "S903": ("Use `globs` to scope a rule to specific files or directories. "
                     "Separate multiple patterns with commas."),
        }
        TOKENS = {"S900": ".claude/rules/",
                  "S901": ".github/instructions/**/*.instructions.md",
                  "S902": ".github/instructions/",
                  "S903": ".cursor/rules"}
        CLIENTS_OF = {"S900": "Claude Code", "S901": "VS Code",
                      "S902": "Copilot CLI", "S903": "Cursor"}
        URLS = {"S900": "https://code.claude.com/docs/en/memory.md",
                "S901": ("https://code.visualstudio.com/docs/agent-customization/"
                         "custom-instructions.md"),
                "S902": ("https://docs.github.com/en/copilot/how-tos/copilot-cli/"
                         "customize-copilot/add-custom-instructions.md"),
                "S903": "https://cursor.com/docs/rules"}
        BASE_URLS = {"S900": URLS["S900"], "S902": URLS["S902"],
                     "S903": "https://cursor.com/docs/rules.md"}
        KEYS = {"S900": "paths", "S901": "applyTo", "S902": "applyTo", "S903": "globs"}
        REOPENS = {"S900": "S010", "S902": "S011", "S903": "S012"}
        DECLS = {
            "S112": ("Claude Code", "paths", URLS["S900"]),
            "S113": ("VS Code", "applyTo", URLS["S901"]),
            "S114": ("Copilot CLI", "applyTo", URLS["S902"]),
            "S115": ("Cursor", "globs", URLS["S903"]),
        }
        HEADER = ("| id | source | kind | tier | scope | anchor | teaches | status "
                  "| opened | recheck | used-by |\n")

        def base_rows(extra: str = "") -> str:
            rows = HEADER
            for sid, url in BASE_URLS.items():
                rows += ("| %s | Base doc \u2014 %s | docs | A | s | sha256 "
                         "`abcdef12\u2026` | t | mined | 2026-10-22 | 90d | y |\n"
                         % (sid.replace("900", "010").replace("902", "011")
                            .replace("903", "012"), url))
            return rows + extra

        def sources_text(key: dict | None = None, teaches: dict | None = None,
                         decls: bool = True, urls: dict | None = None,
                         pages: dict | None = None) -> str:
            t = dict(REOPENS if teaches is None else teaches)
            u = dict(URLS if urls is None else urls)
            pg = dict(PAGES if pages is None else pages)
            out = HEADER
            for sid in ("S900", "S901", "S902", "S903"):
                cell = t.get(sid)
                teach = ("re-opens %s \u2014 the article this row re-reads" % cell
                         if cell else "the client documents its scoped rule files")
                sha = hashlib.sha256(pg[sid].encode()).hexdigest()
                out += ("| %s | %s docs \u2014 %s | docs | A | %s | \u00a7 (%s.page:2); "
                        "sha256 %s | %s | mined | 2026-10-23 | 90d | %s |\n"
                        % (sid, CLIENTS_OF[sid], u[sid], CLIENTS_OF[sid], sid, sha,
                           teach, ENTRY))
            if decls:
                for sid, (client, key_name, url) in DECLS.items():
                    out += ("| %s | %s docs \u2014 %s | docs | A | %s rule key | "
                            "\u00a7 (%s:1) | scope-key[%s]=%s | mined | 2026-10-23 "
                            "| 90d | %s |\n"
                            % (sid, client, url, client, sid, client, key_name, ENTRY))
            return out

        def skill_text(scope: dict | None = None, action: dict | None = None,
                       lines: dict | None = None) -> str:
            k = dict(KEYS if scope is None else scope)
            a = dict(ACTIONS if action is None else action)
            ln = dict(lines or {})
            out = ("# x\n\n" + SKILL_HEADING + "\n\n"
                   "| Client | Rule files | Scope key | Action |\n"
                   "|---|---|---|---|\n")
            for sid in ("S900", "S901", "S902", "S903"):
                scope_line, action_line = ln.get(
                    sid, (3, 5 if sid == "S900" else 4))
                out += ("| %s | `%s` (S%s :2) | `%s` (S%s :%d) | %s (S%s :%d) |\n"
                        % (CLIENTS_OF[sid], TOKENS[sid], sid, k[sid], sid,
                           scope_line, a[sid], sid, action_line))
            return out

        def entry_text() -> str:
            out = ("# e\n\n| Client | Rule files | Source | Quote |\n"
                   "|---|---|---|---|\n")
            for sid in ("S900", "S901", "S902", "S903"):
                out += '| %s | %s | %s | "%s" |\n' % (CLIENTS_OF[sid],
                                                      TOKENS[sid], sid, QUOTES[sid])
            return out

        def lesson_text() -> str:
            out = ("## Gate\n\n| row | URL | quote |\n|---|---|---|\n")
            for sid in ("S900", "S901", "S902", "S903"):
                out += '| %s | %s | "%s" |\n' % (sid, URLS[sid], QUOTES[sid])
            return out

        def files(**kw) -> dict:
            pages = kw.get("pages") or PAGES
            d = {"SKILL.md": skill_text(**{k: v for k, v in kw.items()
                                           if k in ("scope", "action", "lines")}),
                 SOURCES: sources_text(**{k: v for k, v in kw.items()
                                          if k in ("key", "teaches", "decls",
                                                   "urls")}, pages=pages),
                 ENTRY: entry_text(),
                 LESSON: lesson_text()}
            for sid, body in pages.items():
                d[snapshot_path(sid)] = body
            return d

        def live_of(override: dict | None = None) -> dict:
            got = {u: (200, u, PAGES[sid].encode()) for sid, u in URLS.items()}
            for url, value in (override or {}).items():
                got[url] = value
            return got

        def score(repo: Path, base: str, rev: str,
                  live: dict) -> tuple[list[dict], dict[str, bool]]:
            saved = {k: globals()[k]
                     for k in ("BASE", "TARGET", "lane_dir", "run_curl")}
            found: dict[str, bool] = {}
            try:
                globals()["BASE"] = base
                globals()["lane_dir"] = lambda: repo
                globals()["run_curl"] = (
                    lambda url: live.get(url, (404, url, b"not found")))
                skill = git_show(repo, rev, SKILL) or ""
                entry = git_show(repo, rev, ENTRY) or ""
                sources = git_show(repo, rev, SOURCES) or ""
                lesson = git_show(repo, rev, LESSON) or ""
                base_sources = git_show(repo, base, SOURCES) or ""
                report = judge(skill, entry, sources, lesson, base_sources,
                               snapshot_of=lambda sid: git_show_bytes(
                                   repo, rev, snapshot_path(sid)),
                               intro_of=lambda sid: snapshot_intro(repo, rev, sid))
                keys_live = base_url_keys(base_sources)
                for r in report:
                    if not r["backed"]:
                        found[r["client"]] = False
                        continue
                    try:
                        page = fetch(r["url"], HOSTS[r["client"]], keys_live,
                                     own_key=url_key(r["url"]))
                        found[r["client"]] = not live_why(page, r["quote"], r["key"])
                    except Exception:
                        found[r["client"]] = False
            finally:
                for key, value in saved.items():
                    globals()[key] = value
            return report, found

        def cli(repo: Path, base: str, rev: str, live: dict,
                target: int) -> tuple[int, list[str]]:
            saved = {k: globals()[k]
                     for k in ("BASE", "TARGET", "lane_dir", "run_curl")}
            out = io.StringIO()
            try:
                globals()["BASE"] = base
                globals()["TARGET"] = target
                globals()["lane_dir"] = lambda: repo
                globals()["run_curl"] = (
                    lambda url: live.get(url, (404, url, b"not found")))
                with contextlib.redirect_stdout(out):
                    code = main(["--rev", rev, "--fetch"])
            finally:
                for key, value in saved.items():
                    globals()[key] = value
            return code, out.getvalue().splitlines()

        FOUR = ("Claude Code", "VS Code", "Copilot CLI", "Cursor")

        def backed_of(report: list[dict]) -> list[str]:
            return sorted(r["client"] for r in report if r["backed"])

        # -- the eligible world: the four counted rows pass ---------------
        repo, base, rev = build(base_rows(), files())
        report, found = score(repo, base, rev, live_of())
        check("eligible world: the four counted rows are backed", backed_of(report),
              sorted(FOUR))
        check("eligible world: the four counted rows are found live",
              [found[c] for c in FOUR], [True, True, True, True])
        check("eligible world: the base revision has no canonical key rows",
              canonical_scope_keys(git_show(repo, base, SOURCES) or ""), {})
        code, lines = cli(repo, base, rev, live_of(), 4)
        check("eligible world: the CLI exits 0 at a target of 4", code, 0)
        check("eligible world: the summary line is the v2 one",
              lines[0], "scoped rule files backed on committed snapshots 4 of 4; "
                        "found on the live page 4 of 4")
        eligible_pass = sum(1 for c in FOUR if found[c])

        # -- the seven worlds, each a must-reject fixture -----------------
        worlds: list[tuple[str, str, bool]] = []

        def arm_of(reasons: list[str]) -> str:
            """The arm/rule that fired, from the structured reason prefixes."""
            for reason in reasons:
                for tag in ("A1:", "A2:", "A3:", "A4:"):
                    if tag in reason:
                        return tag[:2]
            if any("live fetch" in r or "live page" in r or "reached a base" in r
                   for r in reasons):
                return "live"
            return "other"

        def run_world(tag: str, client: str, base_tree, tree: dict,
                      live: dict | None = None) -> None:
            repo, base, rev = build(base_tree, tree)
            rep, fnd = score(repo, base, rev, live if live is not None else live_of())
            row = {r["client"]: r for r in rep}[client]
            rejected = not (row["backed"] and fnd.get(client, False))
            reasons = row["why"] if row["why"] else ["live page: not found"]
            check("world %s: the mutated row is rejected" % tag, rejected, True)
            print("world %s: %s reject=%s arm=%s line=%r"
                  % (tag, client, rejected, arm_of(reasons), reasons[0][:150]))
            worlds.append((tag, client, rejected))

        # W1: bytes whose full sha the base table already records (A4(iv)).
        w1_sha = hashlib.sha256(PAGES["S900"].encode()).hexdigest()
        w1_base = HEADER + ("| S010 | Base doc \u2014 %s | docs | A | s | sha256 %s "
                            "| t | mined | 2026-10-22 | 90d | y |\n"
                            % (URLS["S900"], w1_sha)) + \
            ("| S011 | Base doc \u2014 %s | docs | A | s | sha256 `abcdef12\u2026` "
             "| t | mined | 2026-10-22 | 90d | y |\n" % URLS["S902"]) + \
            ("| S012 | Base doc \u2014 %s | docs | A | s | sha256 `abcdef12\u2026` "
             "| t | mined | 2026-10-22 | 90d | y |\n"
             % "https://cursor.com/docs/rules.md")
        run_world("W1", "Claude Code", w1_base, files())

        # W2: a fresh row whose URL is a locale rendering of a held URL (A3b).
        w2_url = "https://code.claude.com/docs/de/memory.md"
        run_world("W2", "Claude Code", base_rows(),
                  files(teaches={"S900": None}, urls={**URLS, "S900": w2_url}))

        # W3: a non-canonical key that still binds a path value (A1).
        w3_pages = dict(PAGES)
        w3_pages["S903"] = PAGES["S903"] + 'rules: "src/*.mdc"\n'
        run_world("W3", "Cursor", base_rows(),
                  files(scope={**KEYS, "S903": "rules"}, pages=w3_pages,
                        lines={"S903": (6, 4)}))

        # W4: the live page redirects to a different base row's key (E1 live).
        w4_url = "https://cursor.com/docs/context/rules"
        w4_live = live_of()
        w4_live[w4_url] = (200, "https://cursor.com/docs/rules", PAGES["S903"].encode())
        run_world("W4", "Cursor", base_rows(),
                  files(teaches={"S903": None}, urls={**URLS, "S903": w4_url}), w4_live)

        # W5: the ExecKeyForms wrong-key row (A1).
        w5_pages = dict(PAGES)
        w5_pages["S900"] = PAGES["S900"] + 'patterns: "src/*.{ts,tsx}"\n'
        run_world("W5", "Claude Code", base_rows(),
                  files(scope={**KEYS, "S900": "patterns"}, pages=w5_pages,
                        lines={"S900": (6, 5)}))

        # W6: the invented Action cell against the unconditional-load line (A2).
        w6_line = ("Rules without a `paths` field are loaded unconditionally and "
                   "apply to all files. A path-scoped rule loads when Claude uses "
                   "the Read, Write, or Edit tool on a matching file. It also loads "
                   "when Claude views a matching file with a Bash command that "
                   "counts as a read, such as cat or head on a single file.")
        w6_pages = dict(PAGES)
        w6_pages["S900"] = PAGES["S900"] + w6_line + "\n"
        run_world("W6", "Claude Code", base_rows(),
                  files(action={**ACTIONS,
                                "S900": "Create the rule file in the project and add "
                                        "frontmatter so it loads only for the "
                                        "matching files."},
                        pages=w6_pages, lines={"S900": (3, 6)}))

        # W7: the v1-hollow rescore world, every key outside the canonical set.
        w7_pages = dict(PAGES)
        w7_keys = {}
        for sid in ("S900", "S901", "S902", "S903"):
            w7_pages[sid] = PAGES[sid] + 'matchFiles: "**/*"\n'
            w7_keys[sid] = "matchFiles"
        w7_sha = {sid: hashlib.sha256(w7_pages[sid].encode()).hexdigest()
                  for sid in w7_pages}
        repo, base, rev = build(base_rows(), files(
            scope=w7_keys, pages=w7_pages,
            lines={sid: (6, (5 if sid == "S900" else 4)) for sid in w7_keys}))
        rep, fnd = score(repo, base, rev, live_of())
        w7_reject = not any(r["backed"] for r in rep)
        check("world W7: every fabricated row is rejected", w7_reject, True)
        print("world W7: all reject=%s arm=%s" % (w7_reject, arm_of(
            {r["client"]: r for r in rep}["Claude Code"]["why"])))
        worlds.append(("W7", "all", w7_reject))

        # -- W0: the do-nothing world (no canonical key rows) exits 1 -----
        repo0, base0, rev0 = build(base_rows(), files(decls=False))
        rep0, fnd0 = score(repo0, base0, rev0, live_of())
        code0, lines0 = cli(repo0, base0, rev0, live_of(), 3)
        check("world W0: no row is backed", [r["client"] for r in rep0 if r["backed"]], [])
        check("world W0: the CLI exits 1", code0, 1)
        check("world W0: the four counted rows name the missing key rows",
              [named(r["why"], "A1: no canonical scope key is declared")
               for r in rep0 if r["client"] in FOUR], [True] * len(FOUR))
        print("world W0: exit=%d" % code0)

        # -- the computed predicate line ----------------------------------
        rejected = sum(1 for _tag, _client, ok in worlds if ok)
        print("worlds reject %d of %d; eligible rows pass %d of 4"
              % (rejected, len(worlds), eligible_pass))
        check("the predicate line is computed from seven rejecting worlds",
              (rejected, len(worlds)), (7, 7))
        check("the predicate line is computed from four passing eligible rows",
              eligible_pass, 4)
        # -- the frozen erratum survivors and guard mutations -------------
        import importlib.util

        instrument_path = Path(__file__).resolve().with_name(
            "check_erratum_absorption.py")
        spec = importlib.util.spec_from_file_location(
            "_check_erratum_absorption_v31_selftest", instrument_path)
        if spec is None or spec.loader is None:
            raise EnvError("could not load the absorption survivor catalogue")
        absorption = importlib.util.module_from_spec(spec)
        sys.modules[spec.name] = absorption
        spec.loader.exec_module(absorption)
        frozen_counter = absorption.load_counter(absorption.COUNTER_PATH)
        current_counter = sys.modules[__name__]
        survivor_ids = (
            "e2c-wrong-supersedes-target",
            "e2c-supersedes-with-fresh-fetch",
            "e2e-negated-path-key",
            "e2e-commented-equals-key",
            "e2f-backticked-event-claim",
            "e2f-compound-purpose-outside-citation",
        )
        survivor_id_set = frozenset(survivor_ids)
        attacks = {
            attack.ident: attack
            for erratum in absorption.ERRATA
            for attack in erratum.attacks
            if attack.ident in survivor_id_set
        }
        check("all six frozen survivor instances were loaded",
              frozenset(attacks), survivor_id_set)
        before = {ident: attacks[ident].score(frozen_counter)
                  for ident in survivor_ids}
        after = {ident: attacks[ident].score(current_counter)
                 for ident in survivor_ids}
        check("all six frozen survivors were accepted by the r61 counter",
              tuple(not before[ident] for ident in survivor_ids), (True,) * 6)
        expected_after = (True,) * 6
        check("successor survivor verdicts close all six frozen instances",
              tuple(bool(after[ident]) for ident in survivor_ids), expected_after)
        for ident in survivor_ids:
            print("survivor %s: before %s; after %s" %
                  (ident, "rejected" if before[ident] else "accepted",
                   "rejected" if after[ident] else "accepted"))
        survivors_closed = sum(1 for ident in survivor_ids
                               if not before[ident] and after[ident])
        print("survivors closed %d of 6" % survivors_closed)

        negated_id = "e2e-negated-path-key"
        saved_key_guard = current_counter.key_site_guard
        try:
            current_counter.key_site_guard = lambda _line, _position: True
            negated_admitted = not attacks[negated_id].score(current_counter)
        finally:
            current_counter.key_site_guard = saved_key_guard
        check("must-fail E2e guard mutation admits the negated-path survivor",
              negated_admitted, True)
        print("must-fail E2e guard disabled admits %s: %s" %
              (negated_id, "yes" if negated_admitted else "no"))

        backticked_id = "e2f-backticked-event-claim"
        saved_g7 = current_counter.g7_conjunct
        try:
            current_counter.g7_conjunct = lambda *_args: []
            backticked_admitted = not attacks[backticked_id].score(current_counter)
        finally:
            current_counter.g7_conjunct = saved_g7
        check("must-fail G7 mutation admits the backticked-event survivor",
              backticked_admitted, True)
        print("must-fail G7 disabled admits %s: %s" %
              (backticked_id, "yes" if backticked_admitted else "no"))
        g9_id = "e2f-compound-purpose-outside-citation"
        saved_g9 = current_counter.g9_conjunct
        try:
            current_counter.g9_conjunct = lambda *_args: []
            g9_admitted = not attacks[g9_id].score(current_counter)
        finally:
            current_counter.g9_conjunct = saved_g9
        check("must-fail G9 mutation admits the compound-purpose survivor",
              g9_admitted, True)
        print("must-fail G9 disabled admits %s: %s" %
              (g9_id, "yes" if g9_admitted else "no"))

        # -- G9 split-semantics arms (round 63 wave 2, MutW2SplitClauses) --
        # The three predicate lines, the survivor fixture and the eligible
        # rows are INSENSITIVE to the clause splitter: they stay green under
        # every mutant of `split_clauses` that keeps both boundaries.  These
        # arms pin the splitter's DECLARED semantics; arms (5), (6) and the
        # unpaired-backtick lane pin BOUND lanes RevG9Guard named — they
        # record the current contract, they do not bless it.
        g9_split_line = "The configuration stores project rules using glob syntax."
        g9_split_page = (g9_split_line + "\n\n## Unrelated section\n"
                          "The agent secretly uploads files.")
        # (1) the `and` boundary is case-insensitive (plans/round-63.md: "the
        #     word `and`, case-insensitive, outside backticks").
        check("A2 G9: an upper-case `AND` is a clause boundary",
              named(action_conjunct(
                  ["The index stores project rules."],
                  "The index stores project rules AND it is rebuilt nightly.",
                  1,
                  "The index stores project rules.\n\n## Schedule\n"
                  "The index is rebuilt nightly."), "G9"), True)
        # (2) the `and` boundary is a WORD, not a whitespace-delimited token:
        #     a `,` before `and` does not stop the split.
        check("A2 G9: a `,` before `and` does not stop the clause split",
              named(action_conjunct(
                  [g9_split_line],
                  g9_split_line[:-1] + ",and secretly uploads files.",
                  1, g9_split_page), "G9"), True)
        # (3) a backticked span is opaque: a `;` inside it is not a boundary.
        check("A2 G9: a `;` inside a backticked span is not a clause boundary",
              named(action_conjunct(
                  ["The index writes mode quota nightly."],
                  "The index writes mode quota `quota; limits cold` nightly.",
                  1,
                  "The index writes mode quota nightly.\n\n## Appendix\n"
                  "The mode limits cold storage."), "G9"), False)
        # (4) the `;` boundary needs no trailing space: a `;` glued to the
        #     next word is still a boundary.
        check("A2 G9: a `;` glued to the next word is still a clause boundary",
              named(action_conjunct(
                  ["The index writes mode quota nightly."],
                  "The index writes mode quota;limits cold nightly.",
                  1,
                  "The index writes mode quota nightly.\n\n## Appendix\n"
                  "The mode limits cold storage."), "G9"), True)
        # (5) the `;` boundary is not quote-aware: a `;` inside a
        #     double-quoted span still splits (BOUND lane RevG9Guard named;
        #     this arm pins the current contract, it does not bless it).
        check("A2 G9: a `;` inside a double-quoted span is a clause boundary",
              named(action_conjunct(
                  ["The index writes mode quota nightly."],
                  'The index writes mode "quota; limits cold" nightly.',
                  1,
                  "The index writes mode quota nightly.\n\n## Appendix\n"
                  "The mode limits cold storage."), "G9"), True)
        # (6) the `and` boundary splits inside a `-and-` compound lexeme
        #     (BOUND lane RevG9Guard named; pins the current contract).
        check("A2 G9: a `-and-` compound lexeme is split at its `and`",
              named(action_conjunct(
                  ["The index uses search-and-replace."],
                  "The index uses search-and-replace nightly.",
                  1,
                  "The index uses search-and-replace.\n\n## Schedule\n"
                  "The index is rebuilt nightly."), "G9"), True)
        # (7) with the closed-span pairing fix landed, an unpaired backtick
        #     no longer latches code mode: the `and` boundary still fires.
        check("A2 G9: an unpaired backtick does not suppress the `and` split",
              named(action_conjunct(
                  [g9_line],
                  g9_line[:-1] + " `glob syntax and uploads files. (S900 :1)",
                  1, g9_page), "G9"), True)
        # (8) the pairing is BACKTICK_RE's own, not a find-based latch: an
        #     `and` between two CLOSED backtick spans is still a boundary.
        check("A2 G9: an `and` between two closed backtick spans is a boundary",
              any(r.startswith("A2 G9: clause \"secretly uploads files")
                  for r in g9_conjunct(
                      ["The tool writes mode quota nightly."],
                      'The tool writes `mode quota` and secretly uploads files `now`.',
                      1,
                      "The tool writes mode quota nightly.\n\n## Appendix\n"
                      "The agent secretly uploads files")), True)
        # --- MutW2GuardEvasion (round 63, wave 2): named assertions
        # pinning the G9 clause-content floor and the page-scope gate.
        check("A2 G9: a TWO-word off-citation clause is rejected",
              named(action_conjunct(
                  [g9_line],
                  g9_line[:-1] + " and uploads files. (S900 :1)",
                  1, g9_page), "G9"), True)
        check("A2 G9: a clause absent from the page is NOT reported by G9",
              g9_conjunct(
                  [g9_line],
                  g9_line[:-1] + " and `secretly exfiltrates telemetry "
                  "beacons nightly`. (S900 :1)",
                  1, g9_page), [])
        check("A2 G9: a ONE-word clause is exempt (declared bound)",
              g9_conjunct(
                  [g9_line],
                  g9_line[:-1] + " and exfiltrates. (S900 :1)",
                  1, g9_page), [])

        # -- G9 probes that kill the split/threshold/backtick mutants -----
        # MutG9Guard (round 63) showed three G9-class mutants the survivor
        # fixture alone cannot see: `;`-only split, threshold 1, and a skip of
        # backticked cells each admit a real compound-purpose instance while
        # this self-test stayed green.  Each probe below is rejected by the
        # cited-line clause guard as landed, and admitted by exactly one
        # mutant, so the probe turns that mutant's run red.
        probe_lines = ["The configuration stores project rules using glob syntax.",
                       "The tool writes mode config nightly."]
        probe_page = ("The configuration stores project rules using glob "
                      "syntax.\nThe tool writes mode config nightly.\n\n"
                      "The agent secretly uploads files. The job rotates "
                      "audits weekly.\n")
        g9_probes = (
            ("semicolon-split", 1,
             "The configuration stores project rules using glob syntax; "
             "secretly uploads files."),
            ("one-supported-word", 2,
             "The tool writes mode config nightly and rotates config audits."),
            ("backticked-cell", 1,
             "The configuration stores project rules using `glob` syntax and "
             "secretly uploads files."),
        )
        for probe_name, probe_L, probe_cell in g9_probes:
            probe_reasons = action_conjunct(probe_lines, probe_cell, probe_L,
                                            probe_page)
            check("G9 probe %s is rejected as supported outside the cited line"
                  % probe_name,
                  any(r.startswith("A2 G9:") for r in probe_reasons), True)

        # -- the counter's own sha256 (v2) --------------------------------
        own = Path(__file__).read_bytes()
        check("the own sha256 is 64 hex", len(self_sha()), 64)
        check("the own sha256 is the sha256 of this file",
              self_sha(), hashlib.sha256(own).hexdigest())

        print("self-test: %d failure(s) over %d assertions" % (failures, assertions))
        return 1 if failures else 0
    finally:
        for td in temps:
            shutil.rmtree(td, ignore_errors=True)


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
                           lane, args.rev, snapshot_path(sid)),
                       intro_of=lambda sid: snapshot_intro(lane, args.rev, sid))
        keys = canonical_scope_keys(sources)
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
    print("canonical scope keys (%s): %s"
          % ("/".join(KEY_ROWS),
             "; ".join("%s=%s" % (c, ",".join(sorted(keys.get(c) or ())))
                       for c in CLIENTS if keys.get(c))
             or "none at this revision (A1 rejects every row)"))
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
