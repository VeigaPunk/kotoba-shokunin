#!/usr/bin/env python3
r"""check_description_thresholds.py -- frozen counter for the round-54 C1 (depth) claim.

Round 54, claim C1 (axis: depth, the learning claim; sourced): `SKILL.md`
gains a decision table, `### Description thresholds by client`, that tells an
author, per client, the documented number that limits a skill's
`description` (an authoring maximum, a per-entry cut in the skill listing, or
a listing budget), what happens past it, and what to do.  Each row is grounded
in a new knowledge entry, `corpus/knowledge/skill-listing-thresholds-round54.md`,
whose per-client record quotes the client's own documentation from a
`corpus/SOURCES.md` row opened in round 54.

This counter is frozen at the round-54 plan commit.  The seven clients, the
hosts allowed for each client's source, the table anchors, the word limit,
the opened date and the target are pinned here and never read from the
revision measured.  A later change to any of them is a second measurement,
never the declared one (corpus/QUALITY.md Q28).

A client is BACKED iff all of:
  * exactly one row of the table under the heading
    `### Description thresholds by client` in SKILL.md names it in its first
    cell (case-insensitive, whole cell, backticks/bold and spaces stripped);
    that table's header's first four cells are
    `client | documented threshold | past the threshold | action`;
    the row's action cell is non-empty and not a dash;
  * the row's threshold cell holds at least one number token
    (`\d[\d,]*(?:\.\d+)?%?`, e.g. `1,536`, `2%`, `8,000`);
  * exactly one row of the table under `## Per-client record` in ENTRY names
    the client in its first cell; that header's first five cells are
    `client | row | quote | location | reading`; its location cell is
    non-empty;
  * the entry row's second cell is one `S###` id, and that id is a row of
    `corpus/SOURCES.md` at the same revision with 11 cells, tier `A`, kind
    `spec`, `docs` or `code`, status `mined`, opened `2026-10-22`, and a
    `used-by` cell that names ENTRY;
  * the first http(s) URL in that SOURCES row's `source` cell is on one of the
    client's pinned hosts (HOSTS; host equality or subdomain, a `host/path`
    pin requires the exact host and a whole path-segment prefix, no `.`/`..`
    segment);
  * the entry quote cell, stripped, starts and ends with `"`; the text
    between has 3 to 25 whitespace-separated words and contains, verbatim and
    as a whole token, one of the number tokens of the SKILL.md threshold cell;
  * the quote is exactly a double-quoted string recorded in the same `S###`
    row of a table in `corpus/lessons/round-54.md` § Gate.

The counter does not judge whether the number is a render cut, a budget or
an authoring maximum: that reading is the entry's and the reviewer's, not a
check this file runs (Q31).

With `--fetch`, a BACKED client also needs its quote found on the live page:
the URL is fetched (plain HTTP GET), HTML tags dropped, entities unescaped,
markdown emphasis/backticks removed and whitespace collapsed on both sides;
the quote must then be a substring of the page.

Output: `description thresholds backed <K> of 7 clients` (and with --fetch
`... found on the live page <F> of <K>`).  Exit 0 iff the counted value is at
least TARGET (4), 1 otherwise, 2 = could not evaluate.

Usage:
  python3 -B verifiers/check_description_thresholds.py --rev <rev> [--fetch] [--json]
  python3 -B verifiers/check_description_thresholds.py --root <dir> [--fetch] [--json]
  python3 -B verifiers/check_description_thresholds.py --self-test
"""
from __future__ import annotations

import argparse
import html
import json
import os
import re
import subprocess
import sys
import tempfile
import urllib.parse
import urllib.request
from pathlib import Path

LANE = Path(__file__).resolve().parent.parent
SKILL = "SKILL.md"
ENTRY = "corpus/knowledge/skill-listing-thresholds-round54.md"
SOURCES = "corpus/SOURCES.md"
LESSON = "corpus/lessons/round-54.md"
TARGET = 4
OPENED = "2026-10-22"
MAX_WORDS = 25
CLIENTS = ("Claude Code", "Codex", "VS Code", "Copilot CLI", "Gemini CLI",
           "Cursor", "opencode")
HOSTS = {
    "Claude Code": ("code.claude.com", "docs.claude.com", "docs.anthropic.com",
                    "platform.claude.com", "github.com/anthropics/claude-code"),
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
SKILL_HEADING = "### Description thresholds by client"
SKILL_HEADER = ("client", "documented threshold", "past the threshold", "action")
ENTRY_HEADING = "## Per-client record"
ENTRY_HEADER = ("client", "row", "quote", "location", "reading")
NUM_RE = re.compile(r"\d[\d,]*(?:\.\d+)?%?")
SID_RE = re.compile(r"^`?(S\d{3,})`?$")
URL_RE = re.compile(r"https?://[^\s)>\]`]+")
SOURCES_ROW_RE = re.compile(r"^\|[ \t]*S[0-9]{3,}[ \t]*\|")
QUOTED_TEXT_RE = re.compile(r'"([^"]*)"')


def verify_rev(rev: str) -> None:
    """Reject an unknown revision before `git show` can mistake it for absent paths."""
    r = subprocess.run(["git", "-C", str(LANE), "rev-parse", "--verify", "--quiet",
                        "%s^{commit}" % rev], capture_output=True)
    if r.returncode != 0:
        raise RuntimeError("revision %r is not a commit in %s" % (rev, LANE))


def read_file(args: argparse.Namespace, path: str) -> str | None:
    if args.rev:
        r = subprocess.run(["git", "-C", str(LANE), "show", "%s:%s" % (args.rev, path)],
                           capture_output=True)
        if r.returncode != 0:
            err = r.stderr.decode(errors="replace")
            if "does not exist" in err or "exists on disk, but not in" in err:
                return None
            raise RuntimeError("git show %s:%s failed: %s" % (args.rev, path, err.strip()))
        return r.stdout.decode("utf-8")
    p = Path(args.root) / path
    return p.read_text(encoding="utf-8") if p.is_file() else None


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


def has_token(quote: str, tokens: list[str]) -> bool:
    for t in tokens:
        if re.search(r"(?<![\d,.])%s(?![\d%%]|[,.]\d)" % re.escape(t), quote):
            return True
    return False


def norm(s: str) -> str:
    s = re.sub(r"<[^>]+>", " ", s)
    s = html.unescape(s)
    s = re.sub(r"[`*_]", "", s)
    s = s.replace("\u2019", "'").replace("\u201c", '"').replace("\u201d", '"')
    return re.sub(r"\s+", " ", s).strip().lower()


def fetch(url: str) -> str:
    req = urllib.request.Request(url, headers={"User-Agent": "kotoba-shokunin-counter/54"})
    with urllib.request.urlopen(req, timeout=60) as r:
        return r.read().decode("utf-8", errors="replace")


def judge(skill: str, entry: str, sources: str, lesson: str) -> list[dict]:
    srows = table_rows(skill, SKILL_HEADING, SKILL_HEADER)
    erows = table_rows(entry, ENTRY_HEADING, ENTRY_HEADER)
    table = sources_table(sources)
    gate_quotes = gate_quotes_by_id(lesson)
    report = []
    for client in CLIENTS:
        why: list[str] = []
        sid = url = quote = None
        smine = [r for r in srows if clean(r[0]) == client.lower()]
        tokens: list[str] = []
        if len(smine) != 1:
            why.append("SKILL.md rows naming client: %d (need 1)" % len(smine))
        else:
            sr = smine[0] + [""] * 4
            tokens = NUM_RE.findall(sr[1])
            if not tokens:
                why.append("SKILL.md threshold cell has no number")
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
                    if s[8] != OPENED:
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
                if tokens and not has_token(quote, tokens):
                    why.append("quote holds none of the threshold numbers %s" % tokens)
                if sid and quote not in gate_quotes.get(sid, ()):
                    why.append("round-54 Gate does not record this quote for %s" % sid)
            else:
                why.append("quote cell not wrapped in double quotes")
        report.append({"client": client, "row": sid, "url": url, "quote": quote,
                       "tokens": tokens, "backed": not why, "why": why})
    return report


def self_test() -> int:
    assertions = 0
    failures = 0

    def check(name: str, actual: object, expected: object) -> None:
        nonlocal assertions, failures
        assertions += 1
        if actual != expected:
            failures += 1
            print("FAIL %s: got %r, expected %r" % (name, actual, expected))

    skill = ("# x\n\n### Description thresholds by client\n\n"
             "| Client | Documented threshold | Past the threshold | Action |\n|---|---|---|---|\n"
             "| Claude Code | 1,536 characters per entry | cut | front-load |\n"
             "| Codex | 2% of context | shortened | key words in name |\n"
             "| Cursor | none documented | — | — |\n\n## Next\n")
    entry = ("# e\n\n## Per-client record\n\n| client | row | quote | location | reading |\n"
             "|---|---|---|---|---|\n"
             '| Claude Code | S900 | "text is truncated at 1,536 characters in the skill listing" | `skills.md:389` | cut |\n'
             '| Codex | S901 | "this list uses at most 2% of the model\'s" | `build-skills.md:38` | budget |\n'
             '| Cursor | S902 | "The agent is presented with available skills" | `skills.md:27` | none |\n')
    src_row = ("| %s | T — %s | docs | A | s | a | t | mined | %s | 90d | "
               "corpus/knowledge/skill-listing-thresholds-round54.md |\n")
    sources = (src_row % ("S900", "https://code.claude.com/docs/en/skills.md", OPENED)
               + src_row % ("S901", "https://learn.chatgpt.com/docs/build-skills.md", OPENED)
               + src_row % ("S902", "https://cursor.com/docs/skills.md", OPENED))
    lesson = ("## Gate\n\n| row | URL | quote |\n|---|---|---|\n"
              '| S900 | u | "text is truncated at 1,536 characters in the skill listing" |\n'
              '| S901 | u | "this list uses at most 2% of the model\'s" |\n'
              '| S902 | u | "The agent is presented with available skills" |\n')

    def backed(sk=skill, en=entry, so=sources, le=lesson) -> list[str]:
        return [r["client"] for r in judge(sk, en, so, le) if r["backed"]]

    check("base world backs Claude Code and Codex", backed(), ["Claude Code", "Codex"])
    check("no number in SKILL.md cell (Cursor)", "Cursor" in backed(), False)
    check("quote lacking the threshold number fails",
          backed(en=entry.replace("at 1,536 characters", "at a limit of characters")),
          ["Codex"])
    check("partial number token 1,53 does not match 1,536",
          backed(sk=skill.replace("1,536 characters", "1,53 characters")), ["Codex"])
    check("number 536 inside 1,536 is not a whole token",
          backed(sk=skill.replace("1,536 characters", "536 characters")), ["Codex"])
    check("source opened another day fails",
          backed(so=sources.replace("| mined | %s |" % OPENED, "| mined | 2026-10-21 |", 1)),
          ["Codex"])
    check("status queued fails",
          backed(so=sources.replace("| mined |", "| queued |", 1)), ["Codex"])
    check("used-by without the entry fails",
          backed(so=sources.replace("corpus/knowledge/skill-listing-thresholds-round54.md", "x", 1)),
          ["Codex"])
    check("off-host URL fails",
          backed(so=sources.replace("https://code.claude.com", "https://code.claude.com.evil.io", 1)),
          ["Codex"])
    check("quote not recorded in the Gate fails",
          backed(le=lesson.replace("in the skill listing", "in the listing")), ["Codex"])
    check("Gate fragment does not stand for the quote",
          backed(le=lesson.replace('"text is truncated at 1,536 characters in the skill listing"',
                                   '"truncated at 1,536 characters"')), ["Codex"])
    check("table under another heading is not read",
          backed(sk=skill.replace("### Description thresholds by client", "### Other table")), [])
    check("wrong SKILL header is not read",
          backed(sk=skill.replace("| Action |", "| Notes |")), [])
    check("empty action cell fails",
          backed(sk=skill.replace("| cut | front-load |", "| cut | — |")), ["Codex"])
    check("duplicate SKILL row fails",
          backed(sk=skill.replace("| Codex |", "| Claude Code | 1,536 | x | y |\n| Codex |")),
          ["Codex"])
    check("duplicate entry row fails",
          backed(en=entry + '| Codex | S901 | "x y z" | l | r |\n'), ["Claude Code"])
    check("empty location fails",
          backed(en=entry.replace("`skills.md:389`", " ")), ["Codex"])
    check("26-word quote fails", len(judge(skill, entry.replace(
        "in the skill listing", "in the skill listing " + "w " * 20), sources, lesson)[0]["why"]) > 0,
        True)
    check("tier B fails", backed(so=sources.replace("| docs | A |", "| docs | B |", 1)), ["Codex"])
    check("dot-dot path escape fails", host_ok(
        "https://github.com/anthropics/claude-code/../evil", HOSTS["Claude Code"]), False)
    check("subdomain pin passes", host_ok("https://www.cursor.com/docs", HOSTS["Cursor"]), True)
    check("section ends at same-level heading",
          len(table_rows(skill + "\n### Description thresholds by client2\n", SKILL_HEADING,
                         SKILL_HEADER)), 3)

    script = str(Path(__file__).resolve())
    unknown = subprocess.run(
        [sys.executable, "-B", script, "--rev", "0" * 40],
        capture_output=True, text=True, timeout=30)
    check("unknown revision exits 2 with could-not-evaluate",
          (unknown.returncode, unknown.stderr.startswith("could-not-evaluate:")),
          (2, True))
    with tempfile.TemporaryDirectory() as temp_dir:
        Path(temp_dir, "python3").symlink_to(sys.executable)
        env = os.environ.copy()
        env["PATH"] = temp_dir
        no_git = subprocess.run(
            [sys.executable, "-B", script, "--rev", "HEAD"],
            capture_output=True, text=True, env=env, timeout=30)
    check("missing git exits 2 with could-not-evaluate",
          (no_git.returncode, no_git.stderr.startswith("could-not-evaluate:")),
          (2, True))

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
        if args.rev:
            verify_rev(args.rev)
        skill = read_file(args, SKILL) or ""
        entry = read_file(args, ENTRY) or ""
        sources = read_file(args, SOURCES) or ""
        lesson = read_file(args, LESSON) or ""
    except (RuntimeError, UnicodeDecodeError, OSError) as e:
        print("could-not-evaluate: %s" % e, file=sys.stderr)
        return 2
    report = judge(skill, entry, sources, lesson)
    backed = [r for r in report if r["backed"]]
    found = None
    if args.fetch:
        found = 0
        for r in backed:
            try:
                page = norm(fetch(r["url"]))
                r["found"] = norm(r["quote"]) in page
            except Exception as e:  # network or decode failure: not found
                r["found"] = False
                r["fetch_error"] = str(e)
            found += 1 if r["found"] else 0
    if args.json:
        print(json.dumps({"backed": len(backed), "of": len(CLIENTS), "found": found,
                          "target": TARGET, "clients": report}, indent=1))
    else:
        for r in report:
            print("%-12s %s %s" % (r["client"], "BACKED" if r["backed"] else "no",
                                   "; ".join(r["why"]) or
                                   ("found=%s" % r.get("found") if args.fetch else "")))
    print("description thresholds backed %d of %d clients" % (len(backed), len(CLIENTS)))
    value = len(backed)
    if args.fetch:
        print("description thresholds found on the live page %d of %d" % (found, len(backed)))
        value = found
    return 0 if value >= TARGET else 1


if __name__ == "__main__":
    sys.exit(main())
