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
    client's pinned hosts (HOSTS below); a `host/path` pin requires the exact
    host and a whole path-segment prefix;
  * the quote cell, stripped, starts and ends with `"`; the text between those
    two characters has 3 to 25 whitespace-separated words and contains the
    word `instructions` (case-insensitive);
  * the quote exactly matches a quote recorded for the same `S###` row in
    `corpus/lessons/round-52.md` § Gate;

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
  python3 -B verifiers/check_mcp_instructions.py --self-test
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
GATE_ROW_RE = re.compile(r"^-\s+\*\*(S\d{3,})\*\*")
GATE_QUOTE_LABEL_RE = re.compile(r"\bQuote(?:\s*\([^)]*\))?:", re.S)
QUOTED_TEXT_RE = re.compile(r'"([^"]*)"')


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
    # A `.` or `..` segment (raw or percent-encoded) can climb out of a pinned
    # path prefix after the prefix test (round-53 falsify seat W2MutMcpTighten).
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
    quotes: dict[str, set[str]] = {}
    in_gate = False
    sid = None
    block = []

    def record_block() -> None:
        if sid is None:
            return
        text = "\n".join(block)
        label = GATE_QUOTE_LABEL_RE.search(text)
        if label:
            for match in QUOTED_TEXT_RE.finditer(text, label.end()):
                quotes.setdefault(sid, set()).add(match.group(1))

    for line in lesson.splitlines():
        if line.startswith("## "):
            record_block()
            sid, block = None, []
            in_gate = line.rstrip() == "## Gate"
            continue
        if not in_gate:
            continue
        match = GATE_ROW_RE.match(line)
        if match:
            record_block()
            sid, block = match.group(1), [line]
        elif sid is not None:
            block.append(line)
    record_block()
    return quotes


def gate_quote_matches(quotes: dict[str, set[str]], sid: str, quote: str) -> bool:
    return quote in quotes.get(sid, ())


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


def self_test() -> int:
    assertions = 0
    failures = 0

    def check(name: str, actual: bool, expected: bool) -> None:
        nonlocal assertions, failures
        assertions += 1
        if actual != expected:
            failures += 1
            print("FAIL %s: got %s, expected %s" % (name, actual, expected))

    path_pin = ("github.com/modelcontextprotocol",)
    check("M12 exact pinned path", host_ok(
        "https://github.com/modelcontextprotocol", path_pin), True)
    check("M12 descendant segment", host_ok(
        "https://github.com/modelcontextprotocol/specification/schema.md", path_pin), True)
    check("M12 rejects sibling path", host_ok(
        "https://github.com/modelcontextprotocol-evil/specification/schema.md", path_pin), False)
    check("M12 rejects same-segment continuation", host_ok(
        "https://github.com/modelcontextprotocolfoo/specification/schema.md", path_pin), False)
    check("M12 path pin requires exact host", host_ok(
        "https://api.github.com/modelcontextprotocol/specification/schema.md", path_pin), False)
    check("pin rejects a `..` segment that climbs out of the prefix", host_ok(
        "https://github.com/modelcontextprotocol/../evil/schema.md", path_pin), False)
    check("pin rejects a percent-encoded `..` segment", host_ok(
        "https://github.com/modelcontextprotocol/%2e%2e/evil/schema.md", path_pin), False)

    lesson = ('## Gate\n\n- **S036** — source. Quote (`mcp-server.md:1315`):\n'
              '  "which will be appended to the system instructions."\n')
    gate_quotes = gate_quotes_by_id(lesson)
    full_quote = "which will be appended to the system instructions."
    fragment = "appended to the system instructions."
    check("M16 accepts exact Gate quote", gate_quote_matches(
        gate_quotes, "S036", full_quote), True)
    check("M16 rejects quote fragment", gate_quote_matches(
        gate_quotes, "S036", fragment), False)
    check("M16 rejects quote recorded for another row", gate_quote_matches(
        gate_quotes, "S037", full_quote), False)

    def run_gate(rev: str, env: dict[str, str] | None = None) -> subprocess.CompletedProcess:
        return subprocess.run([sys.executable, "-B", str(Path(__file__).resolve()),
                              "--rev", rev], cwd=LANE, env=env,
                             capture_output=True, text=True)

    unknown = run_gate("0" * 40)
    check("R unknown revision exits 2", unknown.returncode == 2, True)
    check("R unknown revision reports could-not-evaluate",
          unknown.stderr.startswith("could-not-evaluate: "), True)

    with tempfile.TemporaryDirectory(prefix="mcp-self-test-", dir=LANE) as td:
        (Path(td) / "python3").symlink_to(sys.executable)
        env = dict(os.environ)
        env["PATH"] = td
        for key in ("GIT_DIR", "GIT_WORK_TREE", "GIT_INDEX_FILE"):
            env.pop(key, None)
        no_git = run_gate("HEAD", env)
    check("G git unavailable exits 2", no_git.returncode == 2, True)
    check("G git unavailable reports could-not-evaluate",
          no_git.stderr.startswith("could-not-evaluate: "), True)

    # A git that is present and refuses (exit 128, e.g. dubious ownership) is
    # an environment failure: the gate must quote git's own refusal, not claim
    # the revision is unknown.
    with tempfile.TemporaryDirectory(prefix="mcp-self-test-git128-") as td:
        (Path(td) / "python3").symlink_to(sys.executable)
        shim = Path(td) / "git"
        shim.write_text("#!/bin/sh\n"
                        "echo \"fatal: detected dubious ownership in repository"
                        " at '/x/y'\" >&2\n"
                        "exit 128\n", encoding="utf-8")
        shim.chmod(0o755)
        env = dict(os.environ)
        env["PATH"] = td
        for key in ("GIT_DIR", "GIT_WORK_TREE", "GIT_INDEX_FILE"):
            env.pop(key, None)
        refusing = run_gate("HEAD", env)
    check("G refusing git exits 2", refusing.returncode == 2, True)
    check("G refusing git does not blame the revision",
          "is not a commit" in refusing.stderr, False)
    check("G refusing git reports git's own refusal",
          "dubious ownership" in refusing.stderr, True)

    print("self-test: %d failure(s) over %d assertions" % (failures, assertions))
    return 1 if failures else 0


def revision_error(rev: str, where, code: int, detail: str) -> str:
    """The could-not-evaluate reason for a failed `rev-parse --verify --quiet`.

    An unknown revision is git's own exit 1 with no diagnostic.  Any other
    failure (a refusing git: dubious ownership, no repository, a broken object
    store) is an environment failure and is reported with git's own words,
    never as a claim about the revision.
    """
    detail = detail.strip()
    if code == 1 and not detail:
        return "revision %r is not a commit in %s" % (rev, where)
    first = detail.splitlines()[0] if detail else "(git printed no diagnostic)"
    return ("git rev-parse %r failed in %s (exit %d): %s"
            % (rev, where, code, first))


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
            r = subprocess.run(["git", "-C", str(LANE), "rev-parse", "--verify",
                                "--quiet", "%s^{commit}" % args.rev],
                               capture_output=True)
            if r.returncode != 0:
                raise RuntimeError(revision_error(
                    args.rev, LANE, r.returncode,
                    r.stderr.decode("utf-8", "replace")))
        entry = read_file(args, ENTRY)
        sources = read_file(args, SOURCES) or ""
        lesson = read_file(args, LESSON) or ""
    except (RuntimeError, OSError) as e:
        print("could-not-evaluate: %s" % e, file=sys.stderr)
        return 2
    rows = entry_rows(entry) if entry is not None else []
    table = sources_table(sources)
    gate_quotes = gate_quotes_by_id(lesson)
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
            if sid and not gate_quote_matches(gate_quotes, sid, quote):
                why.append("round-52 Gate does not record this quote for %s" % sid)
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
