#!/usr/bin/env python3
r"""check_overlap_levers.py -- content guard for the round-51 C2 (depth) claim.

Landing path (intended): `verifiers/check_overlap_levers.py` in
/home/vgpnk/Projects/shokunin/kotoba-shokunin.

Why this file exists
--------------------
Round 51, claim C2 (axis: depth, the learning claim; sourced) lands two new
pieces of content:

  * `SKILL.md` § Anti-patterns carries an "Overlap levers by client" table
    that names, for K of 7 pinned clients, a key term from the instrument's
    reviewed per-client list of skill-removal levers, shown as a code span in
    a quote of at most 25 words;
  * `corpus/knowledge/skill-overlap-levers-round51.md` records the quotes,
    each citing a `mined` row of `corpus/SOURCES.md` whose `used-by` names the
    entry path, with a round-51 Gate record in
    `corpus/lessons/round-51.md`.

This instrument is the counter.  It re-reads the four files at a pinned git
revision (`--rev`) or from a directory (`--root`), finds the two tables by
their anchors, and decides for each of the seven pinned clients whether its
claim is BACKED.  The denominator -- the seven clients -- and the reviewed
lever terms are pinned in this file and never read from the revision measured.

A client is BACKED iff all of:
  * exactly one SKILL.md row names it (case-insensitive whole-cell match)
    inside the `## Anti-patterns` section (HTML comments and code fences are
    ignored), with the row's `held by` one of `skill author` / `user or
    operator` / `app developer` and its `effect` one of `removed everywhere`
    / `automatic choice off` / `outside a scope`;
  * the row's id matches `S\d{3}`, is unique in the SOURCES registry, has
    status `mined`, kind `docs`/`code`/`spec`, tier `A`, and its first https
    URL sits under the client's pinned vendor docs prefix;
  * the registry row's `used-by` names the entry path
    `corpus/knowledge/skill-overlap-levers-round51.md` (or the bare filename
    as a whole token) and the row id appears in `corpus/lessons/round-51.md`
    under its `## Gate` section;
  * the entry table has exactly one row for the same client citing the same
    row id, its quote cell starts with a double-quoted string followed by a
    parenthesized location, the quote is at most 25 words, and it contains a
    backticked code span exactly equal to the key term;
  * the key term is in the client's reviewed lever list
    (`REVIEWED_LEVERS`) and does not contain `description`
    (case-insensitive).

A missing input file is an absent table (or an absent Gate), not an error: it
lowers the count instead of crashing.

`--fetch` additionally re-opens each cited source page over the network and
checks each quote on the live bytes (whitespace, markdown emphasis and HTML
tags normalized on both sides), so the quotes are not frozen copies.
`--self-test` exercises the guard on in-memory fixtures: one control world
that is 7 of 7, plus the structural mutants of the original build, one mutant
per fix of the round-51 critic (CriticC2Sizing F1-F6), and the critic's four
false-pass worlds; every mutant must lower the backed count below 7.

Exit ladder (family contract):
  0  all seven clients backed (and, with --fetch, every quote found live)
  1  fewer than seven backed (or, with --fetch, a quote not found live)
  2  usage error (bad arguments) or IO error (unreadable root)

Usage:
    check_overlap_levers.py [--rev REV | --root DIR] [--fetch]
    check_overlap_levers.py --self-test

Stdlib only (Python >= 3.9); the only writes are the self-test's stdout and
the network reads made by --fetch.
"""

from __future__ import annotations

import argparse
import http.client
import re
import subprocess
import sys
import urllib.error
import urllib.request
from pathlib import Path

# The pinned denominator: the seven clients the claim names.  Never read from
# the revision measured.
CLIENTS = [
    "GitHub Copilot SDK",
    "GitHub Copilot CLI",
    "VS Code",
    "Claude Code",
    "opencode",
    "Gemini CLI",
    "Codex",
]

ENTRY_PATH = "corpus/knowledge/skill-overlap-levers-round51.md"
ENTRY_FILENAME = "skill-overlap-levers-round51.md"
LESSON_PATH = "corpus/lessons/round-51.md"
SKILL_MARKER = "Overlap levers by client"
ENTRY_MARKER = "## Levers by client"
SKILL_HEADER = ("client", "lever", "held by", "effect", "row", "key term")
ENTRY_HEADER = ("client", "row", "lever", "quote")
SID_RE = re.compile(r"\AS\d{3}\Z")
SEPARATOR_CELL = re.compile(r"\A:?-{2,}:?\Z")
CELL_SPLIT = re.compile(r"(?<!\\)\|")
WS_RUN = re.compile(r"\s+")
EMPHASIS = re.compile(r"[*_`]")
HTML_TAG = re.compile(r"<[^>]+>")
HTTPS_URL = re.compile(r"https://[^\s|]+")
QUOTE_CELL = re.compile(r'\A"([^"]*)"\s*\([^)]*\)')
CODE_SPAN = re.compile(r"`([^`]+)`")
COMMENT = re.compile(r"<!--.*?-->", re.S)
FENCE = re.compile(r"\A```")
HEADING = re.compile(r"\A## ")
USER_AGENT = "Mozilla/5.0 (compatible; kotoba-check_overlap_levers/1.0)"
FETCH_TIMEOUT = 20
MAX_QUOTE_WORDS = 25

ALLOWED_HELD_BY = ("skill author", "user or operator", "app developer")
ALLOWED_EFFECTS = ("removed everywhere", "automatic choice off",
                   "outside a scope")
ALLOWED_KINDS = ("docs", "code", "spec")
TIER_A = "A"

# Vendor identity: a client is backed only by its own vendor's documentation,
# so the SOURCES row's first https URL must start with one of these prefixes.
CLIENT_URL_PREFIXES = {
    "GitHub Copilot SDK": ("https://docs.github.com/en/copilot/",),
    "GitHub Copilot CLI": ("https://docs.github.com/en/copilot/",),
    "VS Code": ("https://code.visualstudio.com/docs/",),
    "Claude Code": ("https://code.claude.com/docs/",),
    "opencode": ("https://opencode.ai/docs/",),
    "Gemini CLI": ("https://geminicli.com/docs/",),
    "Codex": ("https://learn.chatgpt.com/docs/",
              "https://developers.openai.com/codex/"),
}

# Reviewed list, round 51; a removal lever, not a tie-break.  These are the
# key terms a reviewer confirmed remove one named skill from model choice
# (disable list, permission deny, model invocation off), per client.  The
# semantic judgment is frozen here by the reviewer seats and is not a
# measurement.
REVIEWED_LEVERS = {
    "GitHub Copilot SDK": {"disabledSkills"},
    "GitHub Copilot CLI": {"disable-model-invocation", "copilot skill disable",
                           "ignoredSkillsLocations"},
    "VS Code": {"disable-model-invocation"},
    "Claude Code": {"disable-model-invocation", "disable-model-invocation: true",
                    "skillOverrides"},
    "opencode": {"opencode/autoinvoke", "deny"},
    "Gemini CLI": {"/skills disable", "/skills disable <name>", "skills disable"},
    "Codex": {"allow_implicit_invocation", "enabled = false"},
}


# --------------------------------------------------------------------------
# markdown table parsing
# --------------------------------------------------------------------------

def split_row(line):
    """Split one markdown table row into its cells (unescaping `\\|`)."""
    parts = CELL_SPLIT.split(line.strip())
    if parts and parts[0].strip() == "":
        parts = parts[1:]
    if parts and parts[-1].strip() == "":
        parts = parts[:-1]
    return [p.replace("\\|", "|").strip() for p in parts]


def is_separator_row(cells):
    return bool(cells) and all(SEPARATOR_CELL.match(c) for c in cells)


def _table_block_after(lines, start):
    """The first table block (list of cell-lists) at/after `start`."""
    j = start
    while j < len(lines) and not lines[j].lstrip().startswith("|"):
        j += 1
    if j >= len(lines):
        return None
    rows = []
    while j < len(lines) and lines[j].lstrip().startswith("|"):
        cells = split_row(lines[j])
        if not (rows and is_separator_row(cells)) and cells:
            rows.append(cells)
        j += 1
    return rows or None


def _find_table(text, marker, header):
    """First table after a line containing `marker`, with `header` columns."""
    lines = text.splitlines()
    start = None
    for i, line in enumerate(lines):
        if marker in line:
            start = i + 1
            break
    if start is None:
        return None
    table = _table_block_after(lines, start)
    if table is None or [c.lower() for c in table[0]] != list(header):
        return None
    return table[1:]


def anti_patterns_span(text):
    """Lines of the `## Anti-patterns` section, comments and fences blanked.

    Only the section between the `## Anti-patterns` heading and the next
    `## ` heading is kept; HTML comments are removed and fenced code blocks
    are skipped, so a marker or table hidden in either is never seen.
    """
    text = COMMENT.sub("", text)
    out = []
    inside = False
    fence = False
    for line in text.splitlines():
        if FENCE.match(line):
            fence = not fence
            continue
        if fence:
            continue
        if HEADING.match(line):
            inside = line.strip() == "## Anti-patterns"
            continue
        if inside:
            out.append(line)
    return "\n".join(out)


def parse_skill_table(text):
    """SKILL.md table -> {client_lower: [row_dict, ...]}."""
    rows = _find_table(text, SKILL_MARKER, SKILL_HEADER)
    out = {}
    if rows is None:
        return out
    for cells in rows:
        if len(cells) != 6:
            continue
        client, lever, held_by, effect, rid, key = cells
        key_term = None
        m = re.match(r"`([^`]+)`", key)
        if m:
            key_term = m.group(1)
        out.setdefault(client.lower(), []).append(
            {"client": client, "lever": lever, "held_by": held_by,
             "effect": effect, "id": rid, "key_term": key_term})
    return out


def parse_entry_table(text):
    """Entry file table -> {client_lower: [row_dict, ...]}."""
    rows = _find_table(text, ENTRY_MARKER, ENTRY_HEADER)
    out = {}
    if rows is None:
        return out
    for cells in rows:
        if len(cells) != 4:
            continue
        client, rid, lever, quote_cell = cells
        quote = None
        m = QUOTE_CELL.match(quote_cell)
        if m:
            quote = m.group(1)
        out.setdefault(client.lower(), []).append(
            {"client": client, "id": rid, "lever": lever, "quote": quote})
    return out


def parse_sources(text):
    """SOURCES registry -> (sources, duplicates).

    sources maps each unique `S###` id to {kind, tier, status, used_by,
    source}; duplicates is the set of ids that appear in more than one row.
    """
    lines = text.splitlines()
    start = None
    for i, line in enumerate(lines):
        if line.lstrip().startswith("|"):
            cells = split_row(line)
            lowered = [c.lower() for c in cells]
            if "id" in lowered and "used-by" in lowered:
                start = i + 1
                break
    if start is None:
        return {}, set()
    out = {}
    duplicates = set()
    for cells in _table_block_after(lines, start) or []:
        if len(cells) < 11:
            continue
        sid = cells[0]
        if not SID_RE.match(sid):
            continue
        if sid in out:
            duplicates.add(sid)
        out[sid] = {
            "kind": cells[2],
            "tier": cells[3],
            "status": cells[7],
            "used_by": cells[10],
            "source": cells[1],
        }
    return out, duplicates


def gate_ids(lesson):
    """Row ids named in the lesson's `## Gate` section."""
    m = re.search(r"^## Gate\n(.*?)(?=^## |\Z)", lesson or "",
                  flags=re.S | re.M)
    if not m:
        return set()
    return set(re.findall(r"\bS\d{3}\b", m.group(1)))


# --------------------------------------------------------------------------
# evaluation
# --------------------------------------------------------------------------

def evaluate(skill_text, sources_text, entry_text, lesson_text=""):
    """Decide each pinned client's backed state.

    Returns (results, meta): results maps each client to (bool, reason);
    meta carries the parsed tables plus, for backed clients, the row id, the
    quote, the source row and the source URL (used by --fetch).
    """
    skill_rows = parse_skill_table(anti_patterns_span(skill_text))
    entry_rows = parse_entry_table(entry_text)
    sources, duplicates = parse_sources(sources_text)
    gate = gate_ids(lesson_text)
    meta = {"skill_table": bool(skill_rows), "entry_table": bool(entry_rows),
            "sources": sources, "duplicates": duplicates, "gate": gate}
    results = {}
    for client in CLIENTS:
        key = client.lower()
        rows = skill_rows.get(key, [])
        if not rows:
            reason = ("SKILL.md table absent" if not skill_rows
                      else "no SKILL.md row")
            results[client] = (False, reason)
            continue
        if len(rows) > 1:
            results[client] = (False, "duplicate SKILL.md row")
            continue
        row = rows[0]
        if row["held_by"] not in ALLOWED_HELD_BY:
            results[client] = (False, "held by not allowed ('%s')"
                               % row["held_by"])
            continue
        if row["effect"] not in ALLOWED_EFFECTS:
            results[client] = (False, "effect not allowed ('%s')"
                               % row["effect"])
            continue
        rid = row["id"]
        if not SID_RE.match(rid):
            results[client] = (False, "row id not S###")
            continue
        if rid in duplicates:
            results[client] = (False, "duplicate source row %s" % rid)
            continue
        src = sources.get(rid)
        if src is None:
            results[client] = (False, "source row %s missing" % rid)
            continue
        url = first_https_url(src["source"]) or ""
        prefixes = CLIENT_URL_PREFIXES[client]
        if not url.startswith(prefixes):
            results[client] = (False, "source not the client's vendor docs")
            continue
        if src["kind"] not in ALLOWED_KINDS or src["tier"] != TIER_A:
            results[client] = (False, "source kind/tier not vendor tier A")
            continue
        if src["status"].lower() != "mined":
            results[client] = (False, "source %s not mined" % rid)
            continue
        used = [item.strip() for item in re.split(r"[,;]", src["used_by"])]
        if ENTRY_PATH not in used and ENTRY_FILENAME not in used:
            results[client] = (False, "source %s used-by missing" % rid)
            continue
        if rid not in gate:
            results[client] = (False, "no round-51 Gate record for %s" % rid)
            continue
        entrants = [e for e in entry_rows.get(key, []) if e["id"] == rid]
        if not entrants:
            reason = ("entry table absent" if not entry_rows
                      else "entry row missing")
            results[client] = (False, reason)
            continue
        if len(entrants) > 1:
            results[client] = (False, "duplicate entry row")
            continue
        entry = entrants[0]
        if entry["quote"] is None:
            results[client] = (False, "entry quote malformed")
            continue
        if len(entry["quote"].split()) > MAX_QUOTE_WORDS:
            results[client] = (False, "quote over 25 words")
            continue
        key_term = row["key_term"]
        if key_term is None:
            results[client] = (False, "key term not backticked")
            continue
        if key_term not in REVIEWED_LEVERS[client]:
            results[client] = (False, "key term not a reviewed overlap lever")
            continue
        if "description" in key_term.lower():
            results[client] = (False, "key term mentions description")
            continue
        spans = CODE_SPAN.findall(entry["quote"])
        if key_term not in spans:
            results[client] = (False, "key term not a code span in the quote")
            continue
        results[client] = (True, "")
        meta[client] = {"id": rid, "quote": entry["quote"], "source": src,
                        "url": url}
    return results, meta


# --------------------------------------------------------------------------
# live fetch (--fetch)
# --------------------------------------------------------------------------

def normalize(text):
    """Collapse whitespace runs and drop markdown emphasis and tags."""
    return EMPHASIS.sub("", HTML_TAG.sub("", WS_RUN.sub(" ", text))).strip()


def first_https_url(cell):
    """First https URL in a source cell, trailing punctuation trimmed."""
    m = HTTPS_URL.search(cell)
    if not m:
        return None
    return m.group(0).rstrip(".,;:)!?")


def fetch_text(url):
    """Fetch a URL with a 20 s timeout and a plain User-Agent."""
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(req, timeout=FETCH_TIMEOUT) as resp:
        return resp.read().decode("utf-8", "replace")


def quote_on_page(page, quote):
    return normalize(quote) in normalize(page or "")


def fetch_probe(url, quote):
    """True if the quote occurs on the page (or its `.md` sibling)."""
    for candidate in (url, url.rstrip("/") + ".md"):
        try:
            page = fetch_text(candidate)
        except (urllib.error.URLError, urllib.error.HTTPError,
                http.client.HTTPException, OSError, ValueError):
            continue
        if quote_on_page(page, quote):
            return True
    return False


# --------------------------------------------------------------------------
# CLI
# --------------------------------------------------------------------------

def default_root():
    """The repo containing this script: `verifiers/` sits one level down."""
    return Path(__file__).resolve().parent.parent


def git_show(repo, rev, path):
    """Run `git -C repo show rev:path`; None when the file is absent."""
    proc = subprocess.run(
        ["git", "-C", str(repo), "show", "%s:%s" % (rev, path)],
        stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if proc.returncode != 0:
        return None
    return proc.stdout.decode("utf-8", "replace")


def build_parser():
    parser = argparse.ArgumentParser(
        description="Content guard for round-51 C2 overlap-lever claims.")
    group = parser.add_mutually_exclusive_group()
    group.add_argument("--rev", metavar="REV",
                       help="read the files at this git revision")
    group.add_argument("--root", metavar="DIR",
                       help="read the files from this directory "
                            "(default: the repo containing this script)")
    parser.add_argument("--fetch", action="store_true",
                        help="re-open each cited source page and check the "
                             "quotes on the live bytes")
    parser.add_argument("--self-test", action="store_true",
                        help="run the in-memory fixture suite")
    return parser


def main(argv=None):
    parser = build_parser()
    args = parser.parse_args(argv)

    if args.self_test:
        return self_test()

    if args.rev:
        repo = default_root()

        def read_path(path):
            return git_show(repo, args.rev, path)
    else:
        root = Path(args.root).expanduser() if args.root else default_root()
        if not root.is_dir():
            print("ERROR root %s is not a directory" % root,
                  file=sys.stderr)
            return 2

        def read_path(path):
            try:
                return (root / path).read_text(encoding="utf-8")
            except FileNotFoundError:
                return None

    try:
        skill_text = read_path("SKILL.md") or ""
        sources_text = read_path("corpus/SOURCES.md") or ""
        entry_text = read_path(ENTRY_PATH) or ""
        lesson_text = read_path(LESSON_PATH) or ""
    except OSError as exc:
        print("ERROR reading input: %s" % exc, file=sys.stderr)
        return 2

    results, meta = evaluate(skill_text, sources_text, entry_text, lesson_text)
    k = sum(1 for ok, _ in results.values() if ok)

    for client in CLIENTS:
        ok, reason = results[client]
        if ok:
            print("BACKED %s" % client)
        else:
            print("UNBACKED: %s (%s)" % (reason, client))
    print("overlap levers backed %d of %d clients" % (k, len(CLIENTS)))

    rc = 0 if k == len(CLIENTS) else 1
    if args.fetch:
        found = 0
        for client in CLIENTS:
            info = meta.get(client)
            if not info:
                continue
            url = info["url"]
            if not url:
                print("FETCH %s: no URL in source cell" % client)
                continue
            if fetch_probe(url, info["quote"]):
                found += 1
                print("FETCH %s: quote found (%s)" % (client, url))
            else:
                print("FETCH %s: quote not found (%s)" % (client, url))
        print("quotes found on live pages %d of %d" % (found, k))
        if found < k:
            rc = 1
    return rc


# --------------------------------------------------------------------------
# self-test fixtures
# --------------------------------------------------------------------------

def _skill_row(client, lever, held_by, effect, sid, term):
    return "| %s | %s | %s | %s | %s | `%s` |" % (
        client, lever, held_by, effect, sid, term)


def _entry_row(client, sid, lever, quote):
    return "| %s | %s | %s | \"%s\" (page.md:1) |" % (
        client, sid, lever, quote)


def _src_row(sid, source, kind="docs", tier="A", used=ENTRY_PATH):
    return ("| %s | %s | %s | %s | s | a | t | mined | 2026-10-22 | "
            "90d | %s |\n" % (sid, source, kind, tier, used))


SOURCES_HDR = ("| id | source | kind | tier | scope | anchor | teaches "
               "| status | opened | recheck | used-by |\n"
               "|---|---|---|---|---|---|---|---|---|---|---|\n")

# Real vendor URLs from the round-51 source rows.
URL = {
    "S021": "OpenAI — Build skills (ChatGPT and Codex) — "
            "https://learn.chatgpt.com/docs/build-skills",
    "S022": "Claude Code — Extend Claude with skills — "
            "https://code.claude.com/docs/en/skills",
    "S024": "opencode — Agent skills — https://opencode.ai/docs/skills",
    "S025": "VS Code — Use Agent Skills in VS Code — "
            "https://code.visualstudio.com/docs/agent-customization/agent-skills",
    "S028": "GitHub Docs — GitHub Copilot CLI plugin reference — "
            "https://docs.github.com/en/copilot/reference/copilot-cli-reference/cli-plugin-reference",
    "S029": "Gemini CLI — Agent Skills — https://geminicli.com/docs/cli/skills/",
    "S030": "GitHub Docs — Copilot SDK skills — "
            "https://docs.github.com/en/copilot/how-tos/copilot-sdk/features/skills",
    "S031": "GitHub Docs — Copilot CLI add skills — "
            "https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-skills",
}

Q25 = ("Use the `user-invocable` and `disable-model-invocation` frontmatter "
       "properties to control how each skill is accessed")

LEVER = {
    "GitHub Copilot SDK": ("disable list", "user or operator",
                           "removed everywhere", "S030", "disabledSkills",
                           "Use `disabledSkills` to exclude conflicting skills"),
    "GitHub Copilot CLI": ("skill disable command", "user or operator",
                           "automatic choice off", "S031",
                           "disable-model-invocation",
                           "To stop the model from invoking it on its own, "
                           "set `disable-model-invocation`"),
    "VS Code": ("model invocation off", "skill author",
                "automatic choice off", "S025", "disable-model-invocation",
                Q25),
    "Claude Code": ("model invocation off", "skill author",
                    "automatic choice off", "S022",
                    "disable-model-invocation",
                    "To keep a skill but stop Claude from invoking it on its "
                    "own, set `disable-model-invocation`"),
    "opencode": ("permission deny", "app developer",
                 "automatic choice off", "S024", "deny",
                 "Check permissions—skills with `deny` are hidden from agents"),
    "Gemini CLI": ("disable command", "user or operator",
                   "removed everywhere", "S029", "/skills disable",
                   "Use `/skills disable` to prevent a specific skill from "
                   "being used"),
    "Codex": ("implicit invocation off", "skill author",
              "automatic choice off", "S021", "allow_implicit_invocation",
              "When `allow_implicit_invocation` is false, Codex won't "
              "implicitly invoke the skill"),
}

LEVER_IDS = ("S021", "S022", "S024", "S025", "S029", "S030", "S031")


def _control_world():
    """Seven fully-backed clients with realistic vendor rows.  Returns
    (skill, sources, entry, lesson) texts."""
    skill_rows = []
    entry_rows = []
    for client, (lever, held_by, effect, sid, term, quote) in LEVER.items():
        skill_rows.append(_skill_row(client, lever, held_by, effect, sid, term))
        entry_rows.append(_entry_row(client, sid, lever, quote))
    skill = (
        "# kotoba\n"
        "\n"
        "## Anti-patterns\n"
        "\n"
        "Overlap levers by client\n"
        "\n"
        "| client | lever | held by | effect | row | key term |\n"
        "|---|---|---|---|---|---|\n"
        + "\n".join(skill_rows) + "\n"
        "\n"
        "## Refusals\n"
    )
    sources = SOURCES_HDR + "".join(_src_row(s, URL[s]) for s in LEVER_IDS)
    entry = (
        "## Levers by client\n"
        "\n"
        "| client | row | lever | quote |\n"
        "|---|---|---|---|\n"
        + "\n".join(entry_rows) + "\n"
    )
    lesson = "# Round 51\n\n## Gate\n\nRe-opened " + ", ".join(LEVER_IDS) \
        + ".\n"
    return skill, sources, entry, lesson


def _mutants():
    """[(name, skill, sources, entry, lesson), ...]; each lowers K below 7."""
    base_skill, base_sources, base_entry, base_lesson = _control_world()
    c0 = CLIENTS[0]
    out = []

    def split(text):
        return text.splitlines()

    def join(lines):
        return "\n".join(lines) + "\n"

    def skill_without_row(client):
        return join([ln for ln in split(base_skill)
                     if not ln.startswith("| %s |" % client)])

    # Original structural mutants (adapted to the six-column table).
    out.append(("row removed", skill_without_row(c0), base_sources,
                base_entry, base_lesson))
    src = [ln.replace("| 90d | %s |" % ENTRY_PATH,
                      "| 90d | corpus/lessons/round-46.md |", 1)
           for ln in split(base_sources)]
    out.append(("used-by missing", base_skill, join(src), base_entry,
                base_lesson))
    src = [ln.replace("| mined | 2026-10-22 | 90d | %s |" % ENTRY_PATH,
                      "| queued | 2026-10-22 | 90d | %s |" % ENTRY_PATH, 1)
           for ln in split(base_sources)]
    out.append(("row status not mined", base_skill, join(src), base_entry,
                base_lesson))
    e = [ln.replace("\"Use `disabledSkills` to exclude conflicting skills\"",
                    "\"Use something else here\"")
         for ln in split(base_entry)]
    out.append(("key term absent from quote", base_skill, base_sources,
                join(e), base_lesson))
    s = [ln.replace("| %s | disable list | user or operator | removed "
                    "everywhere | S030 | `disabledSkills` |" % c0,
                    "| %s | disable list | user or operator | removed "
                    "everywhere | S030 | `description-term0` |" % c0)
         for ln in split(base_skill)]
    out.append(("key term mentions description", join(s), base_sources,
                base_entry, base_lesson))
    s = split(base_skill)
    idx = next(i for i, ln in enumerate(s)
               if ln.startswith("| %s | disable list |" % c0))
    s.insert(idx + 1,
             _skill_row(c0, "disable list", "user or operator",
                        "removed everywhere", "S031",
                        "disable-model-invocation"))
    out.append(("duplicate client row", join(s), base_sources, base_entry,
                base_lesson))
    e = [ln.replace("| %s | S030 |" % c0, "| %s | S031 |" % c0)
         for ln in split(base_entry)]
    out.append(("entry cites different row", base_skill, base_sources,
                join(e), base_lesson))
    s = join([ln for ln in split(base_skill)
              if "Overlap levers by client" not in ln
              and not ln.lstrip().startswith("|")])
    out.append(("SKILL.md table absent", s, base_sources, base_entry,
                base_lesson))
    s = join([ln.replace("| %s | disable list |" % c0,
                         "| Foo Ltd | disable list |")
              for ln in split(base_skill)])
    out.append(("unknown client name", s, base_sources, base_entry,
                base_lesson))

    # Critic F1-F6 mutants, one per fix.
    comment_hidden = ("<!--\nOverlap levers by client\n\n"
                      "| client | lever | held by | effect | row | key term |\n"
                      "|---|---|---|---|---|---|\n"
                      + "\n".join(_skill_row(*(
                          (c, LEVER[c][0], LEVER[c][1], LEVER[c][2],
                           LEVER[c][3], LEVER[c][4])))
                          for c in CLIENTS)
                      + "-->\n# kotoba\n\n## Refusals\n")
    out.append(("comment-hidden table", comment_hidden, base_sources,
                base_entry, base_lesson))
    src = [ln.replace(URL["S030"], URL["S025"])
           for ln in split(base_sources)]
    out.append(("cross-vendor URL", base_skill, join(src), base_entry,
                base_lesson))
    s = join([ln.replace("| VS Code | model invocation off | skill author | "
                         "automatic choice off | S025 | "
                         "`disable-model-invocation` |",
                         "| VS Code | model invocation off | skill author | "
                         "automatic choice off | S025 | `user-invocable` |")
              for ln in split(base_skill)])
    out.append(("generic key term not reviewed", s, base_sources, base_entry,
                base_lesson))
    e = join([ln.replace("\"Check permissions—skills with `deny` are hidden "
                         "from agents\"",
                         "\"Check permissions—skills with deny are hidden "
                         "from agents\"")
              for ln in split(base_entry)])
    out.append(("key term not code span", base_skill, base_sources, e,
                base_lesson))
    long_quote = ("The list, add, remove, disable, and enable operations are "
                  "also available from the terminal command line by using the "
                  "`disable-model-invocation` flag to stop the model from "
                  "choosing a skill on its own, so the skill is not offered")
    e = join([ln.replace(_entry_row(CLIENTS[1], "S031",
                                    LEVER[CLIENTS[1]][0],
                                    LEVER[CLIENTS[1]][5]),
                         _entry_row(CLIENTS[1], "S031",
                                    LEVER[CLIENTS[1]][0], long_quote))
              for ln in split(base_entry)])
    out.append(("quote over 25 words", base_skill, base_sources, e,
                base_lesson))
    src = [ln.replace(URL["S022"],
                      "https://code.claude.com/docs/en/skills — "
                      "corpus/knowledge/skill-overlap-levers-round51-rejected.md")
           for ln in split(base_sources)]
    src = [ln.replace("corpus/knowledge/skill-overlap-levers-round51-rejected.md",
                      ENTRY_PATH)
           for ln in src]
    used_stem = [ln.replace("| 90d | %s |" % ENTRY_PATH,
                            "| 90d | %s |"
                            % "corpus/knowledge/skill-overlap-levers-round51-rejected.md", 1)
                 for ln in split(base_sources)]
    out.append(("used-by stem only", base_skill, join(used_stem), base_entry,
                base_lesson))
    out.append(("no Gate record", base_skill, base_sources, base_entry,
                "# Round 51\n"))
    src = split(base_sources)
    idx = next(i for i, ln in enumerate(src)
               if ln.startswith("| S025 |"))
    src.insert(idx + 1, _src_row("S025", URL["S025"]))
    out.append(("duplicate source row", base_skill, join(src), base_entry,
                base_lesson))

    # Critic false-pass worlds A-D (rebuilt in the six-column format).
    out.append(("world A one page all clients", comment_hidden, base_sources,
                base_entry, base_lesson))

    rows_b = [
        ("GitHub Copilot SDK", "disable the plugin", "user or operator",
         "removed everywhere", "S028", "plugin",
         "Disable a plugin without uninstalling it."),
        ("GitHub Copilot CLI", "managed plugin policy", "user or operator",
         "automatic choice off", "S028", "enabledPlugins",
         "A plugin or marketplace pinned by an organization or MDM managed "
         "policy (`enabledPlugins`, `extraKnownMarketplaces`) can't be "
         "re-enabled, disabled, or repointed locally"),
        ("VS Code", "user-only invocation", "skill author",
         "automatic choice off", "S025", "user-invocable", Q25),
        ("Claude Code", "invocation context", "skill author",
         "automatic choice off", "S022", "when_to_use",
         "the combined `description` and `when_to_use` text is truncated at "
         "1,536 characters in the skill listing to reduce context usage"),
        ("opencode", "disable", "app developer", "automatic choice off",
         "S024", "disable",
         "Completely disable skills for agents that shouldn't use them"),
        ("Gemini CLI", "enabled", "user or operator", "removed everywhere",
         "S029", "enabled",
         "injects the name and description of all enabled skills into the"),
        ("Codex", "listing budget", "skill author", "automatic choice off",
         "S021", "skills.max_context_tokens",
         "Use [`skills.max_context_tokens`](https://learn.chatgpt.com/docs/"
         "config-file/config-reference) to set a different budget, up to "
         "10,000 tokens."),
    ]
    w_b_skill = ("# kotoba\n\n## Anti-patterns\n\nOverlap levers by client\n\n"
                 "| client | lever | held by | effect | row | key term |\n"
                 "|---|---|---|---|---|---|\n"
                 + "\n".join(_skill_row(c, l, h, e, s, t)
                             for c, l, h, e, s, t, _ in rows_b) + "\n")
    w_b_entry = ("## Levers by client\n\n| client | row | lever | quote |\n"
                 "|---|---|---|---|\n"
                 + "\n".join(_entry_row(c, s, l, q)
                             for c, l, h, e, s, t, q in rows_b) + "\n")
    w_b_sources = SOURCES_HDR + "".join(
        _src_row(s, URL[s]) for s in ("S021", "S022", "S024", "S025",
                                      "S028", "S029"))
    out.append(("world B wrong levers", w_b_skill, w_b_sources, w_b_entry,
                base_lesson))

    rows_c = [r if r[0] != "Gemini CLI" else
              ("Gemini CLI", "disable list", "user or operator",
               "removed everywhere", "S029", "skills.disabled",
               "Set `skills.disabled` to stop Gemini from choosing one of two "
               "overlapping skills")
              for r in rows_b]
    w_c_entry = ("## Levers by client\n\n| client | row | lever | quote |\n"
                 "|---|---|---|---|\n"
                 + "\n".join(_entry_row(c, s, l, q)
                             for c, l, h, e, s, t, q in rows_c) + "\n")
    w_c_skill = w_b_skill.replace("`enabled`", "`skills.disabled`")
    out.append(("world C fabricated quote", w_c_skill, w_b_sources,
                w_c_entry, base_lesson))

    rows_d = [("GitHub Copilot SDK", "x", "user or operator",
               "removed everywhere", "S900", "e", "the quote says nothing"),
              ("GitHub Copilot CLI", "x", "user or operator",
               "automatic choice off", "S901", "e", "the quote says nothing"),
              ("VS Code", "x", "skill author", "automatic choice off",
               "S902", "e", "the quote says nothing"),
              ("Claude Code", "x", "skill author", "automatic choice off",
               "S903", "e", "the quote says nothing"),
              ("opencode", "x", "app developer", "automatic choice off",
               "S904", "e", "the quote says nothing"),
              ("Gemini CLI", "x", "user or operator", "removed everywhere",
               "S905", "e", "the quote says nothing"),
              ("Codex", "x", "skill author", "automatic choice off",
               "S906", "e", "the quote says nothing")]
    w_d_skill = ("# kotoba\n\n## Anti-patterns\n\nOverlap levers by client\n\n"
                 "| client | lever | held by | effect | row | key term |\n"
                 "|---|---|---|---|---|---|\n"
                 + "\n".join(_skill_row(c, l, h, e, s, t)
                             for c, l, h, e, s, t, _ in rows_d) + "\n")
    w_d_entry = ("## Levers by client\n\n| client | row | lever | quote |\n"
                 "|---|---|---|---|\n"
                 + "\n".join(_entry_row(c, s, l, q)
                             for c, l, h, e, s, t, q in rows_d) + "\n")
    w_d_sources = SOURCES_HDR + "".join(
        _src_row("S90%d" % i, "https://example.com/notes",
                 kind="own-work", tier="C",
                 used=ENTRY_PATH.replace("round51", "round51-rejected"))
        for i in range(7))
    out.append(("world D provenance", w_d_skill, w_d_sources, w_d_entry,
                "# Round 51\n"))

    return out


def self_test():
    failures = []
    assertions = 0

    def check(name, passed, detail=""):
        nonlocal assertions
        assertions += 1
        if not passed:
            failures.append("%s: %s" % (name, detail))

    skill, sources, entry, lesson = _control_world()
    results, _ = evaluate(skill, sources, entry, lesson)
    k = sum(1 for ok, _ in results.values() if ok)
    check("control world", k == len(CLIENTS),
          "expected %d backed, got %d" % (len(CLIENTS), k))
    for name, m_skill, m_sources, m_entry, m_lesson in _mutants():
        results, _ = evaluate(m_skill, m_sources, m_entry, m_lesson)
        k = sum(1 for ok, _ in results.values() if ok)
        check("mutant: " + name, k < len(CLIENTS),
              "expected fewer than %d backed, got %d"
              % (len(CLIENTS), k))

    if failures:
        for failure in failures:
            print("FAIL %s" % failure)
        print("%d failures" % len(failures))
    else:
        print("0 failures")
    print("%d assertions" % assertions)
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
