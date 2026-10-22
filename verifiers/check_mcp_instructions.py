#!/usr/bin/env python3
r"""check_mcp_instructions.py -- frozen counter for the round-52 C2 (coverage) claim.

Round 52, claim C2 (axis: coverage, the learning claim; sourced): the MCP
server `instructions` surface -- the server-wide text an MCP server returns at
initialization -- moves from `corpus/README.md` § Frontier ("MCP/plugin
instruction surfaces") into held knowledge: a new entry
`corpus/knowledge/mcp-server-instructions-round52.md` records, per client,
what the client's own documentation or source says it does with that text,
each statement grounded in a located quote.

This counter is frozen at the round-52 plan commit.  The seven clients, the
hosts allowed for each client's source, the required word, the word limit,
the table anchor and the target are pinned here and never read from the
revision measured.  A later change to any of them is a second measurement,
never the declared one (corpus/QUALITY.md Q28).

A client is BACKED iff all of:
  * exactly one row of the table under the heading `## Per-client record` in
    ENTRY names it in its first cell (case-insensitive, whole cell, backticks
    and surrounding spaces stripped); the table header's first five cells are
    `client | row | quote | location | reading`;
  * the row's second cell is one `S###` id, and that id is a row of
    `corpus/SOURCES.md` at the same revision with 11 cells, tier `A`, kind
    `spec`, `docs` or `code`, status `mined`, opened `2026-10-22`, and a
    `used-by` cell that names ENTRY;
  * the first http(s) URL in that SOURCES row's `source` cell is on one of the
    client's pinned hosts (HOSTS below; a `host/path` pin also requires the
    URL path to start with that path);
  * the quote cell, stripped, starts and ends with `"`; the text between those
    two characters has 3 to 25 whitespace-separated words and contains the
    word `instructions` (case-insensitive);
  * `corpus/lessons/round-52.md` at the same revision contains both the `S###`
    id and the quote text verbatim (the round's Gate record).

With `--fetch`, a BACKED client also needs its quote found on the live page:
the URL is fetched (ordinary HTTP GET, no browser), HTML tags are dropped,
entities unescaped, markdown emphasis/backticks removed and whitespace
collapsed on both sides; the quote must then be a substring of the page.

Output: `mcp instructions backed <K> of 7 clients` (and with --fetch
`... found on the live page <F> of <K>`).  Exit 0 iff the counted value is at
least TARGET (3), 1 otherwise, 2 = could not evaluate.

Usage:
  python3 -B verifiers/check_mcp_instructions.py --rev <rev> [--fetch] [--json]
  python3 -B verifiers/check_mcp_instructions.py --root <dir> [--fetch] [--json]
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
ENTRY = "corpus/knowledge/mcp-server-instructions-round52.md"
SOURCES = "corpus/SOURCES.md"
LESSON = "corpus/lessons/round-52.md"
TARGET = 3
OPENED = "2026-10-22"
WORD = "instructions"
MAX_WORDS = 25
CLIENTS = ("MCP specification", "Claude Code", "VS Code", "Codex", "Gemini CLI",
           "opencode", "Copilot CLI")
HOSTS = {
    "MCP specification": ("modelcontextprotocol.io", "blog.modelcontextprotocol.io",
                          "github.com/modelcontextprotocol",
                          "raw.githubusercontent.com/modelcontextprotocol"),
    "Claude Code": ("code.claude.com", "docs.claude.com", "docs.anthropic.com",
                    "github.com/anthropics/claude-code"),
    "VS Code": ("code.visualstudio.com", "github.com/microsoft/vscode",
                "github.com/microsoft/vscode-docs",
                "raw.githubusercontent.com/microsoft/vscode-docs"),
    "Codex": ("developers.openai.com", "github.com/openai/codex",
              "raw.githubusercontent.com/openai/codex"),
    "Gemini CLI": ("geminicli.com", "github.com/google-gemini/gemini-cli",
                   "raw.githubusercontent.com/google-gemini/gemini-cli"),
    "opencode": ("opencode.ai", "github.com/sst/opencode", "github.com/anomalyco/opencode",
                 "raw.githubusercontent.com/sst/opencode",
                 "raw.githubusercontent.com/anomalyco/opencode"),
    "Copilot CLI": ("docs.github.com", "github.com/github/copilot-cli",
                    "raw.githubusercontent.com/github/copilot-cli"),
}
HEADER = ("client", "row", "quote", "location", "reading")
SID_RE = re.compile(r"^`?(S\d{3,})`?$")
URL_RE = re.compile(r"https?://[^\s)>\]`]+")
SOURCES_ROW_RE = re.compile(r"^\|[ \t]*S[0-9]{3,}[ \t]*\|")


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
    if not (s.startswith("|") and s.endswith("|")):
        return []
    return [c.strip() for c in s[1:-1].split("|")]


def entry_rows(text: str) -> list[list[str]]:
    lines = text.splitlines()
    rows, in_sec, header_ok = [], False, False
    for ln in lines:
        if re.match(r"^##\s+", ln):
            in_sec = bool(re.match(r"^##\s+Per-client record\s*$", ln))
            header_ok = False
            continue
        if not in_sec:
            continue
        c = cells(ln)
        if not c:
            continue
        if not header_ok:
            if tuple(x.lower() for x in c[:5]) == HEADER:
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
    for pin in pins:
        h, _, p = pin.partition("/")
        if host == h or host.endswith("." + h):
            if not p or path.startswith("/" + p):
                return True
    return False


def norm(s: str) -> str:
    s = re.sub(r"<[^>]+>", " ", s)
    s = html.unescape(s)
    s = re.sub(r"[`*_]", "", s)
    s = s.replace("\u2019", "'").replace("\u201c", '"').replace("\u201d", '"')
    return re.sub(r"\s+", " ", s).strip().lower()


def fetch(url: str) -> str:
    req = urllib.request.Request(url, headers={"User-Agent": "kotoba-shokunin-counter/52"})
    with urllib.request.urlopen(req, timeout=60) as r:
        return r.read().decode("utf-8", errors="replace")


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    src = ap.add_mutually_exclusive_group(required=True)
    src.add_argument("--rev")
    src.add_argument("--root")
    ap.add_argument("--fetch", action="store_true")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args(argv)
    try:
        entry = read_file(args, ENTRY)
        sources = read_file(args, SOURCES) or ""
        lesson = read_file(args, LESSON) or ""
    except RuntimeError as e:
        print("could-not-evaluate: %s" % e, file=sys.stderr)
        return 2
    rows = entry_rows(entry) if entry is not None else []
    table = sources_table(sources)
    report = []
    for client in CLIENTS:
        why = []
        mine = [r for r in rows if r and r[0].strip("` ").lower() == client.lower()]
        if len(mine) != 1:
            why.append("rows naming client: %d (need 1)" % len(mine))
            report.append({"client": client, "backed": False, "why": why})
            continue
        r = mine[0] + [""] * 5
        m = SID_RE.match(r[1])
        sid = m.group(1) if m else None
        url, quote = None, None
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
            if not re.search(r"\b%s\b" % WORD, quote, re.I):
                why.append("quote lacks %r" % WORD)
            if sid and (sid not in lesson or quote not in lesson):
                why.append("round-52 lesson lacks the id or the verbatim quote")
        else:
            why.append("quote cell not wrapped in double quotes")
        rec = {"client": client, "row": sid, "url": url, "quote": quote,
               "backed": not why, "why": why}
        report.append(rec)
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
            print("%-18s %s %s" % (r["client"], "BACKED" if r["backed"] else "no",
                                   "; ".join(r["why"]) or
                                   ("found=%s" % r.get("found") if args.fetch else "")))
    print("mcp instructions backed %d of %d clients" % (len(backed), len(CLIENTS)))
    value = len(backed)
    if args.fetch:
        print("mcp instructions found on the live page %d of %d" % (found, len(backed)))
        value = found
    return 0 if value >= TARGET else 1


if __name__ == "__main__":
    sys.exit(main())
