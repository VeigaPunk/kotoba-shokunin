#!/usr/bin/env python3
r"""check_explicit_invocation.py -- frozen counter for the round-55 C1 (depth) claim.

Round 55, claim C1 (axis: depth, the learning claim; sourced): `SKILL.md`
gains a decision table, `### Explicit invocation by client`, that tells a
reader, per client, the documented form a user types (or the tool the model
calls) to invoke one named skill explicitly, what that form does, and what to
do with it when measuring implicit (description-routed) activation -- the
`corpus/README.md` Frontier row *Implicit-intent fidelity*.  Each row is
grounded in a new knowledge entry, `corpus/knowledge/explicit-invocation-round55.md`,
whose per-client record quotes the client's own documentation from a
`corpus/SOURCES.md` row opened in round 55.

This counter is frozen at the round-55 plan commit.  The seven clients, the
hosts allowed for each client's source, the table anchors, the token rule,
the word limit, the opened dates, the base revision and the targets are pinned
here and never read from the revision measured.  A later change to any of them
is a second measurement, never the declared one (corpus/QUALITY.md Q28).

A client is BACKED iff all of:
  * exactly one row of the table under the heading
    `### Explicit invocation by client` in SKILL.md names it in its first
    cell (case-insensitive, whole cell, backticks/bold and spaces stripped);
    that table's header's first four cells are
    `client | explicit form | what it does | action`;
    the row's action cell is non-empty and not a dash;
  * the row's form cell holds at least one backticked token that matches
    TOKEN_RE: it starts with one of `/ $ @ #` followed by a letter or `<`, or
    it is an identifier holding `_` (a tool name such as `activate_skill`);
  * exactly one row of the table under `## Per-client record` in ENTRY names
    the client in its first cell; that header's first five cells are
    `client | row | quote | location | reading`; its location cell is
    non-empty;
  * the entry row's second cell is one `S###` id, and that id is a row of
    `corpus/SOURCES.md` at the same revision with 11 cells, tier `A`, kind
    `spec`, `docs` or `code`, status `mined`, opened `2026-10-22` or
    `2026-10-23`, and a `used-by` cell that names ENTRY;
  * that `S###` id is NOT a row of `corpus/SOURCES.md` at BASE (the round-55
    base revision): the row was added this round, not only dated today;
  * the first http(s) URL in that SOURCES row's `source` cell is on one of the
    client's pinned hosts (HOSTS; host equality or subdomain, a `host/path`
    pin requires the exact host and a whole path-segment prefix, no `.`/`..`
    segment);
  * the entry quote cell, stripped, starts and ends with `"`; the text
    between has 3 to 25 whitespace-separated words and contains, verbatim,
    one of the TOKEN_RE tokens of the SKILL.md form cell;
  * the quote is exactly a double-quoted string recorded in the same `S###`
    row of a table in `corpus/lessons/round-55.md` § Gate.

NEW GROUND: a backed client (with `--fetch`: a found client) is new ground
when its matched token occurs 0 times in `SKILL.md` and 0 times in every
`corpus/knowledge/*.md` file at BASE (`git show BASE:<path>`, fixed-string).

The counter does not judge whether the form is really explicit invocation
rather than, say, a listing command; that reading is the entry's and the
reviewer's, not a check this file runs (Q31).

With `--fetch`, a BACKED client also needs its quote found on the live page:
the URL is fetched (plain HTTP GET), HTML tags dropped, entities unescaped,
markdown emphasis/backticks/underscores removed and whitespace collapsed on
both sides; the quote must then be a substring of the page.

Output: `explicit invocation forms backed <K> of 7 clients; new ground <G>`
and with --fetch `explicit invocation forms found on the live page <F> of <K>;
new ground <G>`.  Exit 0 iff the counted value (K, or F with --fetch) is at
least TARGET (4) AND G is at least NEW_TARGET (2); 1 otherwise; 2 = could not
evaluate.  The declared C1 predicate is the `--fetch` form at the measured
revision exiting 0.

Usage:
  python3 -B verifiers/check_explicit_invocation.py --rev <rev> [--fetch] [--json]
  python3 -B verifiers/check_explicit_invocation.py --root <dir> [--fetch] [--json]
  python3 -B verifiers/check_explicit_invocation.py --self-test

ERRATUM v2 (round 55, before any C1 content; plans/round-55.md § Erratum 1).
Wave-1 critic CriticC1Sizing met the v1 predicate (`--fetch` 7 of 7, new ground 7)
with real quotes holding no invocation form (`/compact`, `@layer` from CSS,
`#file:`, `/skills list`, link paths), and re-scored held knowledge as new
ground by a case flip.  v2 is strictly stricter than v1: every client it backs,
v1 also backs; every rule below only adds a failure condition.
  * TOKEN_RE: one user-typed segment -- a sigil `/`, `$` or `@`, then a letter
    or `<`, then only letters, digits, `<`, `>`, `_`, `-`.  No `#`, no space,
    no `.`, no second `/`, and no bare tool names (a model-side tool call is
    not a user-typed form).
  * The token, case-folded and without its sigil, is not a client built-in
    or listing command (BUILTINS).
  * The quote contains the word `skill` (case-insensitive).
  * `--fetch`: `<style>`, `<script>` and comment blocks are dropped from the
    page before tags are removed; only HTML tags (`</?letter...>`) are removed
    from the page, and no angle-bracket text is removed from the quote.
  * NEW GROUND is counted per distinct case-folded token, and a counted client
    is new ground only when its token, case-folded, occurs in none of the base
    texts (case-folded) AND its row's URL (scheme, `www.`, a trailing `/` and a
    trailing `.md`/`.mdx` dropped) is not the URL of any row at BASE.
Output label: `user-typed invocation forms found on the live page F of K; new
ground G` (with --fetch) / `user-typed invocation forms backed K of 7
clients; new ground G`.  Exit rule unchanged: value >= 4 and G >= 2.
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

LANE = Path(__file__).resolve().parent.parent
BASE = "f0e5de820a60ec44ff7e5b7c88ac8c8d463dde0c"
SKILL = "SKILL.md"
ENTRY = "corpus/knowledge/explicit-invocation-round55.md"
SOURCES = "corpus/SOURCES.md"
LESSON = "corpus/lessons/round-55.md"
TARGET = 4
NEW_TARGET = 2
OPENED = ("2026-10-22", "2026-10-23")
MAX_WORDS = 25
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
SKILL_HEADING = "### Explicit invocation by client"
SKILL_HEADER = ("client", "explicit form", "what it does", "action")
ENTRY_HEADING = "## Per-client record"
ENTRY_HEADER = ("client", "row", "quote", "location", "reading")
TOKEN_RE = re.compile(r"^[/$@][A-Za-z<][A-Za-z0-9<>_-]*$")
BUILTINS = frozenset((
    "skills", "skill", "help", "compact", "clear", "init", "model", "models", "mcp",
    "agents", "agent", "commands", "config", "settings", "memory", "review", "status",
    "exit", "quit", "resume", "login", "logout", "permissions", "cost", "doctor",
    "hooks", "plugin", "plugins", "add-dir", "bug", "ide", "vim", "terminal-setup",
    "export", "context", "rewind", "usage", "tools", "chat", "new", "file", "files",
    "workspace", "terminal", "codebase", "web", "docs", "rules", "mode", "theme",
))
BACKTICK_RE = re.compile(r"`([^`]+)`")
SID_RE = re.compile(r"^`?(S\d{3,})`?$")
URL_RE = re.compile(r"https?://[^\s)>\]`]+")
SOURCES_ROW_RE = re.compile(r"^\|[ \t]*S[0-9]{3,}[ \t]*\|")
QUOTED_TEXT_RE = re.compile(r'"([^"]*)"')


class EnvError(Exception):
    pass


def verify_rev(rev: str) -> None:
    """An unknown revision is could-not-evaluate (2), never an empty tree (1)."""
    try:
        r = subprocess.run(["git", "-C", str(LANE), "rev-parse", "--verify", "--quiet",
                            "%s^{commit}" % rev], capture_output=True)
    except OSError as e:
        raise EnvError("git not runnable: %s" % e) from e
    if r.returncode != 0:
        raise EnvError("revision %r is not a commit in %s" % (rev, LANE))


def git_show(rev: str, path: str) -> str | None:
    try:
        r = subprocess.run(["git", "-C", str(LANE), "show", "%s:%s" % (rev, path)],
                           capture_output=True)
    except OSError as e:
        raise EnvError("git not runnable: %s" % e) from e
    if r.returncode != 0:
        err = r.stderr.decode(errors="replace")
        if "does not exist" in err or "exists on disk, but not in" in err:
            return None
        raise EnvError("git show %s:%s failed: %s" % (rev, path, err.strip()))
    return r.stdout.decode("utf-8")


def git_ls(rev: str, path: str) -> list[str]:
    try:
        r = subprocess.run(["git", "-C", str(LANE), "ls-tree", "--name-only", rev, path + "/"],
                           capture_output=True)
    except OSError as e:
        raise EnvError("git not runnable: %s" % e) from e
    if r.returncode != 0:
        raise EnvError("git ls-tree %s %s failed: %s"
                       % (rev, path, r.stderr.decode(errors="replace").strip()))
    return [x for x in r.stdout.decode("utf-8").splitlines() if x.endswith(".md")]


def read_file(args: argparse.Namespace, path: str) -> str | None:
    if args.rev:
        verify_rev(args.rev)
        return git_show(args.rev, path)
    p = Path(args.root) / path
    return p.read_text(encoding="utf-8") if p.is_file() else None


def base_texts() -> tuple[str, list[str]]:
    """BASE SKILL.md and BASE corpus/knowledge/*.md texts (new-ground haystack)."""
    verify_rev(BASE)
    skill = git_show(BASE, SKILL) or ""
    know = [git_show(BASE, p) or "" for p in git_ls(BASE, "corpus/knowledge")]
    return skill, know


def cells(line: str) -> list[str]:
    s = line.strip()
    if not (s.startswith("|") and s.endswith("|")) or len(s) < 2:
        return []
    return [c.strip() for c in s[1:-1].split("|")]


def clean(cell: str) -> str:
    return re.sub(r"[`*]", "", cell).strip().lower()


def table_rows(text: str, heading: str, header: tuple[str, ...]) -> list[list[str]]:
    """Rows of the first table with `header` under the exact `heading`.

    The section ends at the next heading of the same or a higher level."""
    level = len(heading) - len(heading.lstrip("#"))
    rows, in_sec, header_ok, done = [], False, False, False
    for ln in text.splitlines():
        m = re.match(r"^(#{1,6})\s+", ln)
        if m:
            if ln.rstrip() == heading:
                in_sec, header_ok = True, False
                continue
            if in_sec and len(m.group(1)) <= level:
                in_sec = False
            continue
        if not in_sec or done:
            continue
        c = cells(ln)
        if not c:
            if header_ok and rows:
                done = True
            continue
        if not header_ok:
            if tuple(clean(x) for x in c[:len(header)]) == header:
                header_ok = True
            continue
        if all(re.fullmatch(r":?-{3,}:?", x) for x in c):
            continue
        rows.append(c)
    return rows


def sources_table(text: str) -> dict[str, list[str]]:
    out: dict[str, list[str]] = {}
    for ln in text.splitlines():
        if SOURCES_ROW_RE.match(ln):
            c = ln.split("|")
            if len(c) == 13:
                out[c[1].strip()] = [x.strip() for x in c[1:12]]
    return out


def source_ids(text: str) -> set[str]:
    return {ln.split("|")[1].strip() for ln in text.splitlines() if SOURCES_ROW_RE.match(ln)}


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


def gate_quotes_by_id(lesson: str) -> dict[str, set[str]]:
    """Double-quoted strings in `## Gate` table rows whose first cell is an S### id."""
    quotes: dict[str, set[str]] = {}
    in_gate = False
    for line in lesson.splitlines():
        if line.startswith("## "):
            in_gate = line.rstrip() == "## Gate"
            continue
        if not in_gate:
            continue
        c = cells(line)
        if not c:
            continue
        m = SID_RE.match(c[0])
        if not m:
            continue
        for q in QUOTED_TEXT_RE.finditer("|".join(c[1:])):
            quotes.setdefault(m.group(1), set()).add(q.group(1))
    return quotes


def form_tokens(cell: str) -> list[str]:
    return [t for t in BACKTICK_RE.findall(cell)
            if TOKEN_RE.match(t) and t[1:].lower() not in BUILTINS]


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


def url_key(url: str | None) -> str:
    if not url:
        return ""
    u = urllib.parse.urlparse(url)
    host = (u.hostname or "").lower()
    host = host[4:] if host.startswith("www.") else host
    path = re.sub(r"\.mdx?$", "", u.path.rstrip("/"))
    return host + path


def base_url_keys(base_sources: str) -> set[str]:
    keys = set()
    for ln in base_sources.splitlines():
        if SOURCES_ROW_RE.match(ln):
            c = ln.split("|")
            if len(c) > 2:
                for m in URL_RE.finditer(c[2]):
                    keys.add(url_key(m.group(0)))
    return keys


def fetch(url: str) -> str:
    req = urllib.request.Request(url, headers={"User-Agent": "kotoba-shokunin-counter/55"})
    with urllib.request.urlopen(req, timeout=60) as r:
        return r.read().decode("utf-8", errors="replace")


def judge(skill: str, entry: str, sources: str, lesson: str, base_sources: str) -> list[dict]:
    srows = table_rows(skill, SKILL_HEADING, SKILL_HEADER)
    erows = table_rows(entry, ENTRY_HEADING, ENTRY_HEADER)
    table = sources_table(sources)
    at_base = source_ids(base_sources)
    gate_quotes = gate_quotes_by_id(lesson)
    report = []
    for client in CLIENTS:
        why: list[str] = []
        sid = url = quote = matched = None
        smine = [r for r in srows if clean(r[0]) == client.lower()]
        tokens: list[str] = []
        if len(smine) != 1:
            why.append("SKILL.md rows naming client: %d (need 1)" % len(smine))
        else:
            sr = smine[0] + [""] * 4
            tokens = form_tokens(sr[1])
            if not tokens:
                why.append("SKILL.md form cell has no backticked invocation token")
            if clean(sr[3]) in ("", "-", "\u2014", "\u2013"):
                why.append("SKILL.md action cell empty")
        emine = [r for r in erows if clean(r[0]) == client.lower()]
        if len(emine) != 1:
            why.append("entry rows naming client: %d (need 1)" % len(emine))
        else:
            r = emine[0] + [""] * 5
            m = SID_RE.match(r[1])
            sid = m.group(1) if m else None
            if not r[3].strip():
                why.append("entry location cell empty")
            if not sid:
                why.append("row cell is not one S### id: %r" % r[1])
            else:
                if sid in at_base:
                    why.append("%s already a SOURCES row at base" % sid)
                s = table.get(sid)
                if not s:
                    why.append("%s absent or malformed in SOURCES.md" % sid)
                else:
                    # id source kind tier scope anchor teaches status opened recheck used-by
                    if s[3] != "A":
                        why.append("%s tier %r" % (sid, s[3]))
                    if s[2] not in ("spec", "docs", "code"):
                        why.append("%s kind %r" % (sid, s[2]))
                    if s[7] != "mined":
                        why.append("%s status %r" % (sid, s[7]))
                    if s[8] not in OPENED:
                        why.append("%s opened %r" % (sid, s[8]))
                    if ENTRY not in s[10]:
                        why.append("%s used-by lacks the entry" % sid)
                    um = URL_RE.search(s[1])
                    url = um.group(0) if um else None
                    if not url or not host_ok(url, HOSTS[client]):
                        why.append("%s source URL %r not on a pinned host" % (sid, url))
            q = r[2].strip()
            if len(q) >= 2 and q.startswith('"') and q.endswith('"'):
                quote = q[1:-1]
                n = len(quote.split())
                if not 3 <= n <= MAX_WORDS:
                    why.append("quote has %d words" % n)
                hits = [t for t in tokens if t in quote]
                matched = hits[0] if hits else None
                if tokens and not hits:
                    why.append("quote holds none of the form tokens %s" % tokens)
                if "skill" not in quote.lower():
                    why.append("quote does not contain the word skill")
                if sid and quote not in gate_quotes.get(sid, ()):
                    why.append("round-55 Gate does not record this quote for %s" % sid)
            else:
                why.append("quote cell not wrapped in double quotes")
        report.append({"client": client, "row": sid, "url": url, "quote": quote,
                       "tokens": tokens, "token": matched, "backed": not why, "why": why})
    return report


def new_ground(token: str | None, base_skill: str, base_know: list[str],
               url: str | None = None, base_urls: set[str] | frozenset = frozenset()) -> bool:
    """v2: case-folded token absent from every base text AND the row's URL not a base row."""
    if not token:
        return False
    t = token.lower()
    if t in base_skill.lower() or any(t in k.lower() for k in base_know):
        return False
    return url_key(url) not in base_urls


def self_test() -> int:
    assertions = 0
    failures = 0

    def check(name: str, actual: object, expected: object) -> None:
        nonlocal assertions, failures
        assertions += 1
        if actual != expected:
            failures += 1
            print("FAIL %s: got %r, expected %r" % (name, actual, expected))

    skill = ("# x\n\n### Explicit invocation by client\n\n"
             "| Client | Explicit form | What it does | Action |\n|---|---|---|---|\n"
             "| Claude Code | `/skill-name` | runs the skill now | count as explicit |\n"
             "| Codex | `$skill-name` | mentions the skill | count as explicit |\n"
             "| Cursor | the word skill | none | — |\n\n## Next\n")
    entry = ("# e\n\n## Per-client record\n\n| client | row | quote | location | reading |\n"
             "|---|---|---|---|---|\n"
             '| Claude Code | S900 | "invoke it directly with /skill-name in the prompt" | `skills.md:1` | x |\n'
             '| Codex | S901 | "mention a skill with $skill-name to use it" | `skills.md:2` | x |\n'
             '| Cursor | S902 | "The agent is presented with available skills" | `skills.md:3` | x |\n')
    src_row = ("| %s | T — %s | docs | A | s | a | t | mined | %s | 90d | "
               "corpus/knowledge/explicit-invocation-round55.md |\n")
    sources = (src_row % ("S900", "https://code.claude.com/docs/en/skills.md", OPENED[0])
               + src_row % ("S901", "https://learn.chatgpt.com/docs/skills.md", OPENED[1])
               + src_row % ("S902", "https://cursor.com/docs/skills.md", OPENED[0]))
    lesson = ("## Gate\n\n| row | URL | quote |\n|---|---|---|\n"
              '| S900 | u | "invoke it directly with /skill-name in the prompt" |\n'
              '| S901 | u | "mention a skill with $skill-name to use it" |\n'
              '| S902 | u | "The agent is presented with available skills" |\n')
    base = "| S001 | x | docs | A | s | a | t | mined | 2026-10-01 | 90d | y |\n"

    def backed(sk=skill, en=entry, so=sources, le=lesson, ba=base) -> list[str]:
        return [r["client"] for r in judge(sk, en, so, le, ba) if r["backed"]]

    check("base world backs Claude Code and Codex", backed(), ["Claude Code", "Codex"])
    check("no token in SKILL.md form cell (Cursor)", "Cursor" in backed(), False)
    check("row present at base fails",
          backed(ba=base + "| S900 | x | docs | A | s | a | t | mined | 2026-10-01 | 90d | y |\n"),
          ["Codex"])
    check("quote lacking the form token fails",
          backed(en=entry.replace("with /skill-name in", "with a name in")), ["Codex"])
    check("bare word token is not an invocation token",
          backed(sk=skill.replace("`/skill-name`", "`skill`")), ["Codex"])
    check("v2: tool name is not a user-typed token", form_tokens("`activate_skill`"), [])
    check("plain identifier fails TOKEN_RE", form_tokens("`skills`"), [])
    check("source opened another day fails",
          backed(so=sources.replace("| mined | %s |" % OPENED[0], "| mined | 2026-10-21 |", 1)),
          ["Codex"])
    check("second opened date passes", "Codex" in backed(), True)
    check("status queued fails",
          backed(so=sources.replace("| mined |", "| queued |", 1)), ["Codex"])
    check("used-by without the entry fails",
          backed(so=sources.replace("corpus/knowledge/explicit-invocation-round55.md", "x", 1)),
          ["Codex"])
    check("off-host URL fails",
          backed(so=sources.replace("https://code.claude.com", "https://code.claude.com.evil.io", 1)),
          ["Codex"])
    check("quote not recorded in the Gate fails",
          backed(le=lesson.replace("in the prompt", "in prompt")), ["Codex"])
    check("Gate fragment does not stand for the quote",
          backed(le=lesson.replace('"invoke it directly with /skill-name in the prompt"',
                                   '"with /skill-name"')), ["Codex"])
    check("table under another heading is not read",
          backed(sk=skill.replace("### Explicit invocation by client", "### Other table")), [])
    check("wrong SKILL header is not read",
          backed(sk=skill.replace("| Action |", "| Notes |")), [])
    check("empty action cell fails",
          backed(sk=skill.replace("| runs the skill now | count as explicit |",
                                  "| runs the skill now | — |")), ["Codex"])
    check("duplicate SKILL row fails",
          backed(sk=skill.replace("| Codex |", "| Claude Code | `/x` | x | y |\n| Codex |")),
          ["Codex"])
    check("duplicate entry row fails",
          backed(en=entry + '| Codex | S901 | "x y z" | l | r |\n'), ["Claude Code"])
    check("empty location fails",
          backed(en=entry.replace("`skills.md:1`", " ")), ["Codex"])
    check("26-word quote fails", len(judge(skill, entry.replace(
        "in the prompt", "in the prompt " + "w " * 20), sources, lesson, base)[0]["why"]) > 0,
        True)
    check("tier B fails", backed(so=sources.replace("| docs | A |", "| docs | B |", 1)), ["Codex"])
    check("dot-dot path escape fails", host_ok(
        "https://github.com/anthropics/claude-code/../evil", HOSTS["Claude Code"]), False)
    check("sibling host prefix fails", host_ok(
        "https://github.com/anthropics/claude-code-evil/x", HOSTS["Claude Code"]), False)
    check("new ground: token absent at base", new_ground("/skill-name", "a", ["b"]), True)
    check("new ground: token in base SKILL.md", new_ground("$x", "use $x", ["b"]), False)
    check("new ground: token in a base entry", new_ground("$x", "a", ["b", "c $x"]), False)
    check("new ground: no token", new_ground(None, "a", []), False)
    check("v2: built-in /skills is not a form", form_tokens("`/skills`"), [])
    check("v2: built-in /compact is not a form", form_tokens("`/compact`"), [])
    check("v2: #file: reference is not a form", form_tokens("`#file:`"), [])
    check("v2: spaced command is not a form", form_tokens("`/skills list`"), [])
    check("v2: a path is not a form", form_tokens("`/help/customization/skills.md`"), [])
    check("v2: placeholder and example forms pass",
          form_tokens("`$<skill-name>`, e.g. `$setup-demo-app` or `@skill-id`"),
          ["$<skill-name>", "$setup-demo-app", "@skill-id"])
    check("v2: quote without the word skill fails",
          backed(sk=skill.replace("`/skill-name` |", "`/deploy-app` |", 1),
                 en=entry.replace("invoke it directly with /skill-name in the prompt",
                                  "invoke it directly with /deploy-app in the prompt"),
                 le=lesson.replace("invoke it directly with /skill-name in the prompt",
                                   "invoke it directly with /deploy-app in the prompt")),
          ["Codex"])
    check("v2: case flip is not new ground", new_ground("$SKILL", "a", ["explicit $skill use"]),
          False)
    check("v2: base URL is not new ground",
          new_ground("/x-y", "a", ["b"], "https://www.Cursor.com/docs/skills.md",
                     {"cursor.com/docs/skills"}), False)
    check("v2: new URL and absent token is new ground",
          new_ground("/x-y", "a", ["b"], "https://cursor.com/docs/other.md",
                     {"cursor.com/docs/skills"}), True)
    check("v2: url_key drops scheme, www, slash and .md",
          url_key("https://www.code.claude.com/docs/en/skills.md/"), "code.claude.com/docs/en/skills")
    check("v2: page style/script dropped",
          "@layer base" in norm_page("<style>@layer base{}</style><p>x</p><script>@layer base</script>"),
          False)
    check("v2: page tags dropped, text kept", norm_page("<p>Use <code>/a-b</code> skill</p>"),
          "use /a-b skill")
    check("v2: quote angle text kept", norm("$<skill-name> here"), "$<skill-name> here")
    check("v2: base_url_keys reads source cells",
          base_url_keys("| S001 | T — https://cursor.com/docs/skills.md | docs |\n"),
          {"cursor.com/docs/skills"})
    check("section ends at same-level heading",
          len(table_rows(skill + "\n### Explicit invocation by client2\n", SKILL_HEADING,
                         SKILL_HEADER)), 3)

    print("self-test: %d failure(s) over %d assertions" % (failures, assertions))
    return 1 if failures else 0


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    src = ap.add_mutually_exclusive_group()
    src.add_argument("--rev")
    src.add_argument("--root")
    ap.add_argument("--fetch", action="store_true")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--self-test", action="store_true")
    args = ap.parse_args(argv)
    if args.self_test:
        if args.rev or args.root or args.fetch or args.json:
            ap.error("--self-test cannot be combined with --rev, --root, --fetch or --json")
        return self_test()
    if not args.rev and not args.root:
        ap.error("one of --rev or --root is required")
    try:
        skill = read_file(args, SKILL) or ""
        entry = read_file(args, ENTRY) or ""
        sources = read_file(args, SOURCES) or ""
        lesson = read_file(args, LESSON) or ""
        base_sources = git_show(BASE, SOURCES) or ""
        base_skill, base_know = base_texts()
    except (EnvError, UnicodeDecodeError, OSError) as e:
        print("could-not-evaluate: %s" % e, file=sys.stderr)
        return 2
    report = judge(skill, entry, sources, lesson, base_sources)
    backed = [r for r in report if r["backed"]]
    found = None
    if args.fetch:
        found = 0
        for r in backed:
            try:
                page = norm_page(fetch(r["url"]))
                r["found"] = norm(r["quote"]) in page
            except Exception as e:  # network or decode failure: not found
                r["found"] = False
                r["fetch_error"] = str(e)
            found += 1 if r["found"] else 0
    counted = [r for r in backed if r.get("found")] if args.fetch else backed
    base_urls = base_url_keys(base_sources)
    for r in report:
        r["new_ground"] = r in counted and new_ground(r["token"], base_skill, base_know,
                                                      r["url"], base_urls)
    ground = len({r["token"].lower() for r in counted if r["new_ground"]})
    if args.json:
        print(json.dumps({"backed": len(backed), "of": len(CLIENTS), "found": found,
                          "new_ground": ground, "target": TARGET, "new_target": NEW_TARGET,
                          "clients": report}, indent=1))
    else:
        for r in report:
            print("%-12s %s %s" % (r["client"], "BACKED" if r["backed"] else "no",
                                   "; ".join(r["why"]) or
                                   ("token=%s new=%s%s" % (
                                       r["token"], r["new_ground"],
                                       " found=%s" % r.get("found") if args.fetch else ""))))
    if args.fetch:
        print("user-typed invocation forms found on the live page %d of %d; new ground %d"
              % (found, len(backed), ground))
        value = found
    else:
        print("user-typed invocation forms backed %d of %d clients; new ground %d"
              % (len(backed), len(CLIENTS), ground))
        value = len(backed)
    return 0 if value >= TARGET and ground >= NEW_TARGET else 1


if __name__ == "__main__":
    sys.exit(main())
