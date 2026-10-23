#!/usr/bin/env python3
r"""check_agent_definitions.py -- frozen counter for the round-56 C1 (depth) claim.

Round 56, claim C1 (axis: depth, the learning claim; sourced): `SKILL.md`
gains a decision table, `### Agent-definition files by client`, that tells a
reader, per client, where that client's agent-definition files live, what such
a file sets, and what to do with it when reading an agent's behaviour -- the
`corpus/README.md` Frontier row *Agent-definition fidelity*.  Each row is
grounded in a new knowledge entry, `corpus/knowledge/agent-definition-files-round56.md`,
whose per-client record quotes the client's own documentation from a
`corpus/SOURCES.md` row opened in round 56.

This counter is frozen before any round-56 C1 content exists.  The seven
clients, the hosts allowed for each client's source, the table anchors, the
token grammar, the word bounds, the opened dates, the base revision and the
targets are pinned here and never read from the revision measured.  A later
change to any of them is a second measurement, never the declared one
(corpus/QUALITY.md Q28).

THE FROZEN SPEC (this file implements it; it is not read from the tree):

  BASE_REV = b0b7140b5a7cf8a50f13989ee6285fc8ee245c41
  CLIENTS  = Claude Code, Codex, VS Code, Copilot CLI, Gemini CLI, Cursor, opencode
  HOSTS    = the pinned host map copied from `verifiers/check_explicit_invocation.py`

  SKILL.md at the measured revision: a section whose heading line is exactly
  `### Agent-definition files by client`; its FIRST table has the header
  `| Client | Definition location | What the file sets | Action |`.  One row per
  client name (exact match to CLIENTS; a duplicate client row disqualifies that
  client).  The location token is the FIRST backticked span of the location
  cell.  The action cell must hold at least three words.

  A token is well-formed iff it matches `^(~/)?\.[A-Za-z][A-Za-z0-9_-]*(/[A-Za-z0-9_.*-]+)*/?$`
  AND has a path segment equal (case-insensitively) to `agent` or `agents`.
  normalise(token) = lowercase, strip a leading `~/`, keep the segments up to and
  including the first `agent`/`agents` segment, join with `/`; e.g.
  `~/.cursor/agents/*.md` -> `.cursor/agents`,
  `~/.config/opencode/agents/` -> `.config/opencode/agents`,
  `.github/agents/*.agent.md` -> `.github/agents`.
  K = the number of client rows with a well-formed token.

  Entry `corpus/knowledge/agent-definition-files-round56.md` at the measured
  revision: its first table with the header `| Client | Location | Source | Quote |`.
  The source cell holds one `S###` id; the quote cell holds the verbatim quote
  (one pair of surrounding straight or curly double quotes is stripped; backticks
  are stripped only for word counting and for the matching normalisation, the
  way the round-55 v2 counter does it).

  A client is BACKED iff all of:
    * its SKILL.md row is unique and well-formed, and its action cell is
      non-empty and holds >= 3 words;
    * an entry row names it;
    * the quote holds 3 to 25 words;
    * the quote contains a path token whose normalise() equals normalise(location
      token), and that raw token appears in the quote -- "that raw token" is read
      as the raw location token itself, so the quote must carry the location
      token verbatim (case-insensitively), or its form without a leading `~/`,
      or without a trailing `/`;
    * the quote matches `(?i)\b(sub-?)?agents?\b` OUTSIDE that token's span;
    * the cited `S###` is a row of `corpus/SOURCES.md` at the measured
      revision, its id is NOT a row at BASE_REV, and its URL -- normalised by
      lowercasing scheme and host, stripping a trailing `/`, stripping a
      trailing `.md`, and stripping `#fragment` and `?query` -- is not the
      normalised URL of any BASE_REV row;
    * that row has tier `A`, status `mined`, and opened `2026-10-22` or `2026-10-23`;
    * the row's URL host is pinned for that client (host_ok);
    * the quote, whitespace-normalised, occurs in `corpus/lessons/round-56.md`
      section `## Gate` at the measured revision.

  With `--fetch`, a BACKED client is FOUND iff the live page at the row URL
  (timeout 30 s, at most 5 MiB, one retry, the round-55 v2 normalisation)
  contains the quote AND the raw location token -- or its form without a leading
  `~/` -- occurs in the normalised live text at a boundary: preceded by the
  start of the text, whitespace, a backtick, a quote character, `(` or `[`;
  never preceded by a letter, a digit, `.`, `/` or `-` (so the live text
  `opencode.ai/docs/agents/` never yields the token `.ai/docs/agents`).

  NEW GROUND G = the number of DISTINCT normalise(token) values among the FOUND
  clients whose case-insensitive fixed-string occurrence count in the whole
  BASE_REV tree, excluding paths under `.ufo/`, is zero
  (`git grep -i -F -c <norm> BASE_REV -- . ':!.ufo'`, summed; git grep exit 1
  means no hits, any other non-zero exit is could-not-evaluate).  Counting
  distinct FORMS against ALL base text is the round-55 routed defect 2 fix:
  example names held at base must not be re-scored as new ground.

  Output: `agent-definition locations backed B of K` without `--fetch`, and
  `agent-definition locations found on the live page F of K; new ground G` with
  `--fetch`, followed by one line per client.  Exit codes: with `--fetch`, 0 iff
  F >= 5 AND G >= 2, else 1; without `--fetch`, always 1 (the non-fetch run is
  not the predicate); 2 = could not evaluate (unknown revision, git failure,
  unreadable file).

THE FROZEN PREDICATE (verbatim in substance, and the receipt label):

  `python3 -B verifiers/check_agent_definitions.py --rev <rev> --fetch` exits 0
  iff it prints `agent-definition locations found on the live page F of K; new
  ground G` with F >= 5 and G >= 2; receipt label
  `C1 predicate: --fetch exit 0 (F>=5, G>=2)`.

The counter reads the measured revision with read-only git (`git -C <lane>
show <rev>:<path>`, `git -C <lane> grep ...`), never from the working tree; the
lane is the parent of the script's `verifiers/` directory.

Usage:
  python3 -B verifiers/check_agent_definitions.py --rev <rev> [--fetch] [--json]
  python3 -B verifiers/check_agent_definitions.py --self-test
"""
from __future__ import annotations

import argparse
import html
import json
import re
import subprocess
import sys
import urllib.parse
import urllib.request
from pathlib import Path

BASE = "b0b7140b5a7cf8a50f13989ee6285fc8ee245c41"
SKILL = "SKILL.md"
ENTRY = "corpus/knowledge/agent-definition-files-round56.md"
SOURCES = "corpus/SOURCES.md"
LESSON = "corpus/lessons/round-56.md"
TARGET = 5
NEW_TARGET = 2
MIN_WORDS = 3
MAX_WORDS = 25
OPENED = ("2026-10-22", "2026-10-23")
MAX_BYTES = 5 * 1024 * 1024
FETCH_TIMEOUT = 30
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
SKILL_HEADING = "### Agent-definition files by client"
SKILL_HEADER = ("client", "definition location", "what the file sets", "action")
ENTRY_HEADER = ("client", "location", "source", "quote")
TOKEN_RE = re.compile(r"^(~/)?\.[A-Za-z][A-Za-z0-9_-]*(/[A-Za-z0-9_.*-]+)*/?$")
AGENT_SEGMENTS = ("agent", "agents")
BACKTICK_RE = re.compile(r"`([^`]+)`")
SID_RE = re.compile(r"^`?(S\d{3,})`?$")
URL_RE = re.compile(r"https?://[^\s)>\]`]+")
SOURCES_ROW_RE = re.compile(r"^\|[ \t]*S[0-9]{3,}[ \t]*\|")
PATH_RUN_RE = re.compile(r"[A-Za-z0-9_.~/*_-]+")
AGENT_WORD_RE = re.compile(r"\b(?:sub-?)?agents?\b", re.IGNORECASE)
SEPARATOR_RE = re.compile(r":?-{3,}:?")
BOUNDARY_PREV = frozenset(" \t\r\n`\"'([")
TRIM_CHARS = ".,;:!?)]}'\""


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


def git(lane: Path, args: list[str]) -> subprocess.CompletedProcess:
    try:
        return subprocess.run(["git", "-C", str(lane)] + args, capture_output=True)
    except OSError as e:
        raise EnvError("git not runnable: %s" % e) from e


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


def git_grep_count(lane: Path, rev: str, needle: str) -> int:
    """Case-insensitive fixed-string occurrences of `needle` in the tree of `rev`.

    Paths under `.ufo/` are excluded.  Exit 1 means no hits (zero); any other
    non-zero exit is could-not-evaluate."""
    r = git(lane, ["grep", "-i", "-F", "-c", "-e", needle, rev, "--", ".", ":!.ufo"])
    if r.returncode == 1:
        return 0
    if r.returncode != 0:
        raise EnvError("git grep %r %s failed: %s"
                       % (needle, rev, r.stderr.decode(errors="replace").strip()))
    return sum_grep_counts(r.stdout.decode("utf-8"))


def sum_grep_counts(out: str) -> int:
    """Sum the per-file counts of `git grep -c` output (`<rev>:<path>:<count>`)."""
    total = 0
    for line in out.splitlines():
        if not line.strip():
            continue
        _head, _sep, tail = line.rpartition(":")
        if tail.isdigit():
            total += int(tail)
    return total


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
    """Rows of the FIRST table of the `### Agent-definition files by client` section.

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
    trailing `.md`, drop `#fragment` and `?query`.

    ERRATUM 1 (round 56, before any C1 content; control CtlC1HeldVariant): the
    base row S026 was re-citable through a path-case alias (`/Sub-Agents`) that
    serves the same bytes.  The key now also percent-decodes and lower-cases the
    path, drops a leading `www.` from the host and ignores the scheme.  Every
    change only makes more URLs equal a base URL, so it only adds a way to fail."""
    if not url:
        return ""
    u = urllib.parse.urlsplit(url)
    host = (u.hostname or "").lower()
    if host.startswith("www."):
        host = host[4:]
    path = urllib.parse.unquote(u.path or "").lower()
    # ERRATUM 3 (control CtlC1HeldVariant on v1.2): repeated slashes collapse.
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

# ERRATUM 2 (round 56, before any C1 content; control CtlC1RealNoForm met v1.1
# with real issue-tracker text that put other clients' or proposed directories
# in each client's row).  A counted location must sit under the client's OWN
# configuration directory (a compatibility path such as Cursor reading
# `.claude/agents` belongs to Claude Code, not Cursor), and the cited page must
# be documentation, not an issue, pull request, discussion or commit page.
# The roots name each vendor's own config directory; they only add failures.
OWN_ROOTS: dict[str, tuple[str, ...]] = {
    "Claude Code": (".claude",),
    "Codex": (".codex",),
    "VS Code": (".github", ".vscode"),
    "Copilot CLI": (".github", ".copilot"),
    "Gemini CLI": (".gemini",),
    "Cursor": (".cursor",),
    "opencode": (".opencode", ".config/opencode"),
}
TRACKER_SEGMENTS = {"issues", "issue", "pull", "pulls", "discussions", "commit",
                    "commits", "compare"}


def owned_by(client: str, norm_tok: str) -> bool:
    """Is the normalised location under one of the client's own roots?"""
    return any(norm_tok.startswith(root + "/") for root in OWN_ROOTS.get(client, ()))


def url_is_tracker(url: str) -> bool:
    """An issue, PR, discussion or commit URL (any host)."""
    path = urllib.parse.unquote(urllib.parse.urlsplit(url).path or "").lower()
    return any(seg in TRACKER_SEGMENTS for seg in path.split("/") if seg)



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

def token_well_formed(token: str | None) -> bool:
    if not token or not TOKEN_RE.match(token):
        return False
    body = token[2:] if token.startswith("~/") else token
    segs = [s for s in body.split("/") if s]
    return any(s.lower() in AGENT_SEGMENTS for s in segs)


def normalise(token: str | None) -> str:
    """lowercase, strip a leading `~/`, keep the segments up to and including the
    first `agent`/`agents` segment."""
    if not token:
        return ""
    t = token.strip().lower()
    if t.startswith("~/"):
        t = t[2:]
    segs = [s for s in t.split("/") if s]
    out = []
    for s in segs:
        out.append(s)
        if s in AGENT_SEGMENTS:
            break
    return "/".join(out)


def path_tokens(text: str):
    """Yield (variant, start, end) for every path-like run in `text`.

    A run is a maximal string of path characters; its variant is the run with
    trailing sentence punctuation trimmed (a leading dot is never trimmed: it
    is what makes the token a dot-directory).  The span is the variant's span."""
    for m in PATH_RUN_RE.finditer(text):
        raw = m.group(0)
        right = len(raw) - len(raw.rstrip(TRIM_CHARS))
        variant = raw[:len(raw) - right]
        if variant:
            yield variant, m.start(), m.start() + len(variant)


def find_path_token(text: str, want_norm: str):
    """The first path token in `text` whose normalise() is `want_norm`."""
    if not want_norm:
        return None
    for variant, start, end in path_tokens(text):
        if token_well_formed(variant) and normalise(variant) == want_norm:
            return variant, start, end
    return None


def agent_word_outside(text: str, start: int, end: int) -> bool:
    """Is there an `agent`/`agents`/`subagent` word outside the token span?"""
    for m in AGENT_WORD_RE.finditer(text):
        if m.end() <= start or m.start() >= end:
            return True
    return False


def raw_location_forms(token: str | None) -> list[str]:
    """The verbatim forms of the location token that may stand for it in a quote:
    the token itself, its form without a leading `~/`, and each without a
    trailing `/` (compared case-insensitively)."""
    if not token:
        return []
    out = [token.lower()]
    if token.startswith("~/"):
        out.append(token[2:].lower())
    for t in list(out):
        s = t.rstrip("/")
        if s and s not in out:
            out.append(s)
    return out


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

def entry_row_verdict(er: list[str], client: str, token: str | None, norm_tok: str,
                      table: dict[str, list[str]], at_base: set[str],
                      base_urls: set[str], gate_raw: str,
                      gate_plain: str) -> tuple[list[str], str | None, str | None, str | None]:
    """Judge one entry row.  Returns (why, sid, url, quote)."""
    why: list[str] = []
    sid = url = quote = None
    m = SID_RE.match(er[2].strip())
    sid = m.group(1) if m else None
    if not sid:
        why.append("entry source cell is not one S### id: %r" % er[2])
    quote = strip_quotes(er[3])
    if not quote:
        why.append("entry quote cell empty")
    else:
        q_plain = quote.replace("`", "")
        n = len(q_plain.split())
        if not MIN_WORDS <= n <= MAX_WORDS:
            why.append("quote holds %d words (need %d-%d)" % (n, MIN_WORDS, MAX_WORDS))
        if token and token_well_formed(token):
            hit = find_path_token(q_plain, norm_tok)
            if hit is None:
                why.append("quote holds no path token normalising to %r" % norm_tok)
            elif not agent_word_outside(q_plain, hit[1], hit[2]):
                why.append("quote holds no agent word outside the path token")
            if not any(f in q_plain.lower() for f in raw_location_forms(token)):
                why.append("quote does not hold the location token %r" % token)
        if not quote_in_gate(quote, gate_raw, gate_plain):
            why.append("round-56 Gate does not record this quote")
    if sid:
        if sid in at_base:
            why.append("%s is already a SOURCES row at base" % sid)
        s = table.get(sid)
        if not s:
            why.append("%s absent or malformed in SOURCES.md" % sid)
        else:
            if s[2] != "docs":
                # ERRATUM 2 (control CtlC1RealNoForm): the row must be the
                # client's documentation, not an issue, PR or discussion.
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
            sr = (smine[0] + ["", "", "", ""])[:4]
            spans = BACKTICK_RE.findall(sr[1])
            token = spans[0] if spans else None
            if token is None:
                why.append("SKILL.md location cell holds no backticked token")
            elif not token_well_formed(token):
                why.append("SKILL.md location token %r is not well-formed" % token)
            else:
                norm_tok = normalise(token)
                in_k = True
                if not owned_by(client, norm_tok):
                    why.append("SKILL.md location %r is not under %s's own config directory %s"
                               % (token, client, "/".join(OWN_ROOTS[client])))
            words = re.sub(r"[`*]", "", sr[3]).split()
            if len(words) < 3:
                why.append("SKILL.md action cell holds %d words (need >= 3)" % len(words))
        emine = [(r + ["", "", "", ""])[:4] for r in erows if client_name(r[0]) == client]
        picked = None
        row_whys = []
        for er in emine:
            row_why, sid, url, quote = entry_row_verdict(
                er, client, token, norm_tok, table, at_base, base_urls,
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

def _plain(s: str) -> str:
    s = html.unescape(s)
    s = re.sub(r"[`*_]", "", s)
    s = s.replace("\u2019", "'").replace("\u201c", '"').replace("\u201d", '"')
    return re.sub(r"\s+", " ", s).strip().lower()


def norm(s: str) -> str:
    """Quote side: no angle-bracket text is removed."""
    return _plain(s)


def norm_page(s: str) -> str:
    s = re.sub(r"(?is)<(style|script)\b.*?</\1\s*>", " ", s)
    s = re.sub(r"(?s)<!--.*?-->", " ", s)
    s = re.sub(r"</?[A-Za-z][^>]*>", " ", s)
    return _plain(s)


def boundary_ok(text: str, idx: int) -> bool:
    """Is the occurrence at `idx` at a token boundary?"""
    if idx == 0:
        return True
    return text[idx - 1] in BOUNDARY_PREV


def token_at_boundary(text: str, token: str) -> bool:
    """Does `token` occur in `text` at a boundary?  The text is normalised.

    ERRATUM 1 (round 56, before any C1 content; control CtlC1HeldVariant): the
    occurrence must also END at a path-segment boundary — the next character is
    not a letter, digit, `_` or `-` — so `.opencode/agent` is not found inside
    `.opencode/agents/`.  This only adds a way to fail."""
    if not token:
        return False
    t = token.lower()
    start = 0
    while True:
        i = text.find(t, start)
        if i < 0:
            return False
        j = i + len(t)
        right_ok = j >= len(text) or not (text[j].isalnum() or text[j] in "_-")
        if boundary_ok(text, i) and right_ok:
            return True
        start = i + 1


def token_forms(token: str | None) -> list[str]:
    """The forms of the raw location token that may stand for it in live text.

    The raw token and the raw token without a leading `~/`, each also run
    through the page normalisation (which drops `*`, `_` and backticks)."""
    if not token:
        return []
    raw = [token.lower()]
    if token.startswith("~/"):
        raw.append(token[2:].lower())
    forms = []
    for t in raw:
        for cand in (t, norm(t)):
            if cand and cand not in forms:
                forms.append(cand)
    return forms


def fetch(url: str, pins: tuple[str, ...] | None = None,
          base_keys: set[str] | None = None) -> str:
    """Plain HTTP GET, 30 s timeout, at most 5 MiB, one retry.

    ERRATUM 3 (control CtlC1HeldVariant on v1.2): when `base_keys` is given,
    a page whose URL after redirects is a base SOURCES URL is not found, so a
    base row cannot be re-cited through a redirecting alias.  Only adds a failure.

    ERRATUM 1 (round 56, before any C1 content; control CtlC1KeyedLabels): when
    `pins` is given, the URL reached after redirects must still be on the
    client's pinned hosts, else the page is not found.  Only adds a failure."""
    last: Exception | None = None
    for _ in range(2):
        try:
            req = urllib.request.Request(url, headers={
                "User-Agent": "kotoba-shokunin-counter/56"})
            with urllib.request.urlopen(req, timeout=FETCH_TIMEOUT) as r:
                final = r.geturl()
                data = r.read(MAX_BYTES + 1)
            if pins is not None and not host_ok(final, pins):
                raise OSError("redirected off the pinned hosts to %s" % final)
            if base_keys is not None and url_key(final) in base_keys:
                raise OSError("reached a base SOURCES URL %s" % final)
            if len(data) > MAX_BYTES:
                raise OSError("page exceeds 5 MiB")
            return data.decode("utf-8", errors="replace")
        except Exception as e:  # network or decode failure: not found
            last = e
    raise last if last else OSError("fetch failed")


def found_on_page(page_text: str, quote: str, token: str | None) -> bool:
    """The live page holds the quote AND the raw location token at a boundary."""
    page = norm_page(page_text)
    if not quote or norm(quote) not in page:
        return False
    return any(token_at_boundary(page, f) for f in token_forms(token))


# ----------------------------------------------------------------- self-test

def self_test() -> int:
    assertions = 0
    failures = 0

    def check(name: str, actual: object, expected: object) -> None:
        nonlocal assertions, failures
        assertions += 1
        if actual != expected:
            failures += 1
            print("FAIL %s: got %r, expected %r" % (name, actual, expected))

    # -- token well-formedness -------------------------------------------
    check("token ~/.cursor/agents/*.md is well-formed",
          token_well_formed("~/.cursor/agents/*.md"), True)
    check("token ~/.config/opencode/agents/ is well-formed",
          token_well_formed("~/.config/opencode/agents/"), True)
    check("token .github/agents/*.agent.md is well-formed",
          token_well_formed(".github/agents/*.agent.md"), True)
    check("token ~/.claude/AGENTS/foo is well-formed",
          token_well_formed("~/.claude/AGENTS/foo"), True)
    check("token .cursor/rules is not (no agent segment)",
          token_well_formed(".cursor/rules"), False)
    check("token agents/foo.md is not (no dot directory)",
          token_well_formed("agents/foo.md"), False)
    check("token .cursor/agents.md is not (segment is agents.md)",
          token_well_formed(".cursor/agents.md"), False)
    check("token AGENTS.md is not", token_well_formed("AGENTS.md"), False)
    check("token '' is not", token_well_formed(""), False)

    # -- normalise --------------------------------------------------------
    check("normalise ~/.cursor/agents/*.md",
          normalise("~/.cursor/agents/*.md"), ".cursor/agents")
    check("normalise ~/.config/opencode/agents/",
          normalise("~/.config/opencode/agents/"), ".config/opencode/agents")
    check("normalise .github/agents/*.agent.md",
          normalise(".github/agents/*.agent.md"), ".github/agents")
    check("normalise ~/.claude/AGENTS/foo",
          normalise("~/.claude/AGENTS/foo"), ".claude/agents")
    check("normalise keeps the first agent segment only",
          normalise("~/.config/opencode/agents/other.md"), ".config/opencode/agents")

    # -- boundary rule ----------------------------------------------------
    check("boundary: .ai/docs/agents inside opencode.ai/docs/agents/ is rejected",
          token_at_boundary("opencode.ai/docs/agents/", ".ai/docs/agents"), False)
    check("boundary: .ai/docs/agents after a space is accepted",
          token_at_boundary("see .ai/docs/agents here", ".ai/docs/agents"), True)
    check("boundary: at the start of the text is accepted",
          token_at_boundary(".ai/docs/agents", ".ai/docs/agents"), True)
    check("boundary: after a letter is rejected",
          token_at_boundary("x.ai/docs/agents", ".ai/docs/agents"), False)
    check("boundary: after a digit is rejected",
          token_at_boundary("1.ai/docs/agents", ".ai/docs/agents"), False)
    check("boundary: after a dot is rejected",
          token_at_boundary("a.ai/docs/agents", ".ai/docs/agents"), False)
    check("boundary: after a slash is rejected",
          token_at_boundary("/.ai/docs/agents", ".ai/docs/agents"), False)
    check("boundary: after a hyphen is rejected",
          token_at_boundary("-.ai/docs/agents", ".ai/docs/agents"), False)
    check("boundary: after a backtick is accepted",
          token_at_boundary("`.ai/docs/agents`", ".ai/docs/agents"), True)
    check("boundary: after a quote is accepted",
          token_at_boundary("\".ai/docs/agents\"", ".ai/docs/agents"), True)
    check("boundary: after a parenthesis is accepted",
          token_at_boundary("(.ai/docs/agents)", ".ai/docs/agents"), True)
    check("boundary: after a bracket is accepted",
          token_at_boundary("[.ai/docs/agents]", ".ai/docs/agents"), True)
    check("boundary: after a comma is rejected",
          token_at_boundary(",.ai/docs/agents", ".ai/docs/agents"), False)
    check("erratum 1: a singular token inside the plural is not found",
          token_at_boundary("put files in .opencode/agents/ now", ".opencode/agent"), False)
    check("erratum 1: the token followed by a slash is found",
          token_at_boundary("put files in .opencode/agent/x.md now", ".opencode/agent"), True)

    # -- URL normalisation ------------------------------------------------
    check("url_key drops a trailing .md",
          url_key("https://code.claude.com/docs/en/sub-agents.md"),
          url_key("https://code.claude.com/docs/en/sub-agents"))
    check("url_key drops a trailing slash",
          url_key("https://code.claude.com/docs/en/"),
          "//code.claude.com/docs/en")
    check("url_key drops a fragment",
          url_key("https://code.claude.com/docs/en#x"),
          "//code.claude.com/docs/en")
    check("url_key drops a query",
          url_key("https://code.claude.com/docs/en?a=1"),
          "//code.claude.com/docs/en")
    check("url_key lower-cases scheme, host and (erratum 1) path",
          url_key("HTTPS://Code.Claude.com/Docs"), "//code.claude.com/docs")
    check("erratum 1: a path-case alias of a base URL is the base URL",
          url_key("https://code.claude.com/docs/en/Sub-Agents"),
          url_key("https://code.claude.com/docs/en/sub-agents"))
    check("erratum 1: www., scheme and percent-encoding do not make a new URL",
          url_key("http://www.code.claude.com/docs/en/sub%2Dagents.md/"),
          url_key("https://code.claude.com/docs/en/sub-agents"))
    check("url_key of nothing is empty", url_key(None), "")
    check("erratum 3: repeated slashes do not make a new URL",
          url_key("https://code.claude.com//docs///en/sub-agents"),
          url_key("https://code.claude.com/docs/en/sub-agents"))
    check("erratum 2: Cursor's own .cursor/agents is owned",
          owned_by("Cursor", normalise("~/.cursor/agents/")), True)
    check("erratum 2: .claude/agents quoted for Cursor is not Cursor's own",
          owned_by("Cursor", normalise(".claude/agents/")), False)
    check("erratum 2: .github/agents is not Claude Code's own",
          owned_by("Claude Code", normalise(".github/agents/")), False)
    check("erratum 2: .agents/agents is nobody's own (Copilot CLI)",
          owned_by("Copilot CLI", normalise(".agents/agents")), False)
    check("erratum 2: ~/.config/opencode/agents is opencode's own",
          owned_by("opencode", normalise("~/.config/opencode/agents/")), True)
    check("erratum 2: a .claudex root is not .claude",
          owned_by("Claude Code", normalise(".claudex/agents")), False)
    check("erratum 2: an issue URL is a tracker page",
          url_is_tracker("https://github.com/anthropics/claude-code/issues/82902"), True)
    check("erratum 2: a docs page is not a tracker page",
          url_is_tracker("https://cursor.com/docs/subagents.md"), False)

    # -- quote word bounds ------------------------------------------------
    check("quote word count: three words pass",
          MIN_WORDS <= len("one two three".split()) <= MAX_WORDS, True)
    check("quote word count: two words fail",
          MIN_WORDS <= len("one two".split()) <= MAX_WORDS, False)
    check("quote word count: 25 words pass",
          len(("w " * 24 + "w").split()) <= MAX_WORDS, True)
    check("quote word count: 26 words fail",
          len(("w " * 25 + "w").split()) <= MAX_WORDS, False)
    check("strip straight quotes", strip_quotes('"hello world"'), "hello world")
    check("strip curly quotes", strip_quotes("\u201chello world\u201d"), "hello world")
    check("keep an unquoted cell", strip_quotes("hello world"), "hello world")

    # -- agent word outside the token -------------------------------------
    q = "Cursor stores agents in .cursor/agents/ for each project"
    hit = find_path_token(q, ".cursor/agents")
    check("path token found in the quote", hit is not None, True)
    check("agent word outside the token span",
          agent_word_outside(q, hit[1], hit[2]), True)
    q2 = "the directory .cursor/agents/ holds them"
    hit2 = find_path_token(q2, ".cursor/agents")
    check("path token found in a quote without an outside agent word",
          hit2 is not None, True)
    check("no agent word outside the token span",
          agent_word_outside(q2, hit2[1], hit2[2]), False)

    # -- duplicate client rows and the whole judge ------------------------
    skill = ("# x\n\n### Agent-definition files by client\n\n"
             "| Client | Definition location | What the file sets | Action |\n"
             "|---|---|---|---|\n"
             "| Claude Code | `~/.claude/agents` | the agent persona | count it as an agent definition |\n"
             "| Codex | `~/.codex/agents` | the agent persona | count it as an agent definition |\n")
    entry = ("# e\n\n| Client | Location | Source | Quote |\n|---|---|---|---|\n"
             '| Claude Code | agents.md:12 | S900 | "Claude Code loads agents from ~/.claude/agents at run time" |\n'
             '| Codex | agents.md:9 | S901 | "Codex reads agent files from ~/.codex/agents in the home directory" |\n')
    src_row = ("| %s | %s docs \u2014 %s | docs | A | "
               "the agent definition location | \u00a7 agents | the location | mined | %s | 90d | "
               "corpus/knowledge/agent-definition-files-round56.md |\n")
    sources = (src_row % ("S900", "Claude Code", "https://code.claude.com/docs/en/agents.md",
                          OPENED[0])
               + src_row % ("S901", "Codex", "https://developers.openai.com/docs/agents.md",
                            OPENED[1]))
    lesson = ("## Gate\n\n| row | URL | quote |\n|---|---|---|\n"
              '| S900 | https://code.claude.com/docs/en/agents.md | '
              '"Claude Code loads agents from ~/.claude/agents at run time" |\n'
              '| S901 | https://developers.openai.com/docs/agents.md | '
              '"Codex reads agent files from ~/.codex/agents in the home directory" |\n')
    base = ("| S001 | Old docs \u2014 https://code.claude.com/docs/en/old.md | docs | A | "
            "s | a | t | mined | 2026-10-01 | 90d | y |\n")

    def backed(sk=skill, en=entry, so=sources, le=lesson, ba=base) -> list[str]:
        return [r["client"] for r in judge(sk, en, so, le, ba) if r["backed"]]

    check("the synthetic world backs both clients",
          backed(), ["Claude Code", "Codex"])
    check("a duplicate SKILL.md row disqualifies the client",
          backed(sk=skill.replace("| Codex |",
                                  "| Claude Code | `~/.x/agents` | y | z |\n| Codex |")),
          ["Codex"])
    check("a second entry row does not disqualify a good one",
          backed(en=entry + '| Codex | agents.md:9 | S901 | "x y z" |\n'),
          ["Claude Code", "Codex"])
    check("an S### already at base is not backed",
          backed(ba=base.replace("S001", "S900")), ["Codex"])
    check("a base URL is not backed",
          backed(ba=base.replace("old.md", "agents.md")), ["Codex"])
    check("a quote missing from the Gate is not backed",
          backed(le=lesson.replace("at run time", "at runtime")), ["Codex"])
    check("a two-word action cell is not backed",
          backed(sk=skill.replace("count it as an agent definition |", "count it |")), [])
    check("a tier B row is not backed",
          backed(so=sources.replace("| docs | A |", "| docs | B |", 1)), ["Codex"])
    check("a queued row is not backed",
          backed(so=sources.replace("| mined |", "| queued |", 1)), ["Codex"])
    check("another opened date is not backed",
          backed(so=sources.replace("| mined | %s |" % OPENED[0], "| mined | 2026-10-21 |", 1)),
          ["Codex"])
    check("an off-host URL is not backed",
          backed(so=sources.replace("https://code.claude.com",
                                    "https://code.claude.com.evil.io", 1)), ["Codex"])
    check("a malformed location token is not backed",
          backed(sk=skill.replace("`~/.claude/agents`", "`~/.claude/rules`")), ["Codex"])
    check("a location cell without a backticked token is not backed",
          backed(sk=skill.replace("`~/.claude/agents`", "~/.claude/agents")), ["Codex"])
    check("a quote without the path token is not backed",
          backed(en=entry.replace("from ~/.claude/agents at run time",
                                  "from the home directory at run time")), ["Codex"])
    check("a quote with only the path and no agent word is not backed",
          backed(en=entry.replace(
              "Claude Code loads agents from ~/.claude/agents at run time",
              "the path ~/.claude/agents is used by the tool")),
          ["Codex"])
    check("a glob location the quote does not carry verbatim is not backed",
          backed(sk=skill.replace("`~/.claude/agents`", "`~/.claude/agents/*.md`"),
                 en=entry.replace("~/.claude/agents at run time",
                                  "~/.claude/agents/other.md at run time"),
                 le=lesson.replace("~/.claude/agents at run time",
                                   "~/.claude/agents/other.md at run time")),
          ["Codex"])
    check("a trailing-slash difference still backs",
          backed(sk=skill.replace("`~/.claude/agents`", "`~/.claude/agents/`")),
          ["Claude Code", "Codex"])
    check("the form without a leading ~/ backs",
          backed(en=entry.replace("from ~/.claude/agents at run time",
                                  "from .claude/agents at run time"),
                 le=lesson.replace("from ~/.claude/agents at run time",
                                   "from .claude/agents at run time")),
          ["Claude Code", "Codex"])
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
    page_ok = ("<p>Custom agents live in <code>.cursor/agents/</code> for each project</p>")
    check("found: quote and token both on the page",
          found_on_page(page_ok, "Custom agents live in .cursor/agents/",
                        ".cursor/agents"), True)
    check("found: quote absent from the page",
          found_on_page(page_ok, "Custom agents live in .cursor/rules/",
                        ".cursor/agents"), False)
    check("found: token only inside a URL is rejected",
          found_on_page("<p>see docs here agent https://opencode.ai/docs/agents/</p>",
                        "see docs here agent", ".ai/docs/agents"), False)
    check("found: token at a space boundary is accepted",
          found_on_page("<p>see docs here agent .ai/docs/agents</p>",
                        "see docs here agent", ".ai/docs/agents"), True)
    check("found: a tilde token is found in the page",
          found_on_page("<p>the agents live in ~/.claude/agents today</p>",
                        "the agents live in ~/.claude/agents", "~/.claude/agents"), True)
    check("found: no token is never found",
          found_on_page(page_ok, "Custom agents live in .cursor/agents/", None), False)

    # -- the Gate check ---------------------------------------------------
    gate = "## Gate\n\n| row | quote |\n|---|---|\n| S1 | \"the agent file lives here\" |\n"
    gs = gate_section(gate)
    check("gate section is read", ws(gs).count("the agent file lives here"), 1)
    check("quote recorded in the Gate", quote_in_gate(
        "the agent file lives here", ws(gs), ws(gs.replace("`", ""))), True)
    check("quote absent from the Gate", quote_in_gate(
        "the agent file lives elsewhere", ws(gs), ws(gs.replace("`", ""))), False)
    check("an empty Gate records no quote", quote_in_gate(
        "the agent file lives here", ws(""), ws("")), False)

    # -- host pins --------------------------------------------------------
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
    check("subdomain of a pinned host accepted",
          host_ok("https://docs.cursor.com/x", HOSTS["Cursor"]), True)

    # -- base-count summing ----------------------------------------------
    check("grep counts are summed",
          sum_grep_counts("b0b7140b:LOG.md:3\nb0b7140b:SKILL.md:2\n"), 5)
    check("grep counts of nothing are zero", sum_grep_counts(""), 0)

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
    if args.self_test:
        if args.rev or args.fetch or args.json:
            ap.error("--self-test cannot be combined with --rev, --fetch or --json")
        return self_test()
    if not args.rev:
        ap.error("--rev is required")
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
        counts: dict[str, int] = {}
        try:
            for r in counted:
                n = r["norm"]
                if n not in counts:
                    counts[n] = git_grep_count(lane, BASE, n)
                r["base_count"] = counts[n]
        except (EnvError, UnicodeDecodeError, OSError) as e:
            print("could-not-evaluate: %s" % e, file=sys.stderr)
            return 2
        ground = len({n for n, c in counts.items() if c == 0})
    if args.json:
        print(json.dumps({"backed": len(backed), "of": k, "found": found,
                          "new_ground": ground, "target": TARGET,
                          "new_target": NEW_TARGET, "clients": report}, indent=1))
    else:
        if args.fetch:
            print("agent-definition locations found on the live page %d of %d; new ground %d"
                  % (found, k, ground))
        else:
            print("agent-definition locations backed %d of %d" % (len(backed), k))
        for r in report:
            if r["backed"]:
                detail = "token=%s norm=%s" % (r["token"], r["norm"])
                if args.fetch:
                    detail += " found=%s" % ("yes" if r.get("found") else "no")
                    if r.get("found"):
                        detail += " base_count=%d" % r.get("base_count", 0)
            else:
                detail = "; ".join(r["why"])
            print("%-12s %-6s %s" % (r["client"], "BACKED" if r["backed"] else "no", detail))
    if args.fetch:
        return 0 if found >= TARGET and ground >= NEW_TARGET else 1
    return 1


if __name__ == "__main__":
    sys.exit(main())
