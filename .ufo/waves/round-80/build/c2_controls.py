#!/usr/bin/env python3
"""c2_controls.py — C2 control worlds for kotoba round 80 (seat Kb80E09C2Worlds).

WHAT THIS IS

``plans/round-80.md`` § C2 names nine control worlds that must be run on the
round-80 C2 counter (``verifiers/check_allowed_tools.py``) BEFORE any claim
after-value is measured:

  C0  base copy                       (do-nothing; expect documented 0 of 6, exit 1)
  C1  token dump, no snapshots        (expect: no surface credited)
  C2  wrong-page real text            (every row quotes another surface's page)
  C3  shared-banner quote (Q70)       (one banner line quoted by every row)
  C4  the INDEPENDENT mechanical generator (form-level reach; see below)
  C5  label-only world                (labels + page tokens, no quote)
  C6  sibling-host world              (``…-evil/…`` must fail the Q32 identity)
  C7  stale snapshot / C7b wrong sha pin (pins must bind the bytes)
  C8  first-answer baseline           (entry-free world, 6 of 6 asserted in prose)

This script builds each world as its own isolated scratch git repo and prints,
per world, the counter's own count line, the counter's own generator-world
line, and the counter's own exit status.  It compares each observation with a
pre-registered expectation table (printed by ``--list``) and says
``as-expected`` or ``DIVERGES``.  It never judges the claim: the script's exit
code means only "every world matched its pre-registration".

C4 IS THE POINT OF THE ROUND (Q71 / Q74)

The round-80 headline is FORM-LEVEL: "the six surfaces carry committed,
snapshot-pinned, quote-grounded rows".  C4 is an INDEPENDENT mechanical
generator — a rule-based scraper written in this file, NOT the counter's own
generator — that reads the six COMMITTED snapshots and emits the complete entry
shape with no judgement: the located quote is scraped by a fixed window rule,
the grant label is chosen by a frozen keyword rule, the tokens are derived from
the quote, the pins are computed from the bytes.  It is then scored on the SAME
counter.  A C4 reach of 6 of 6 does NOT falsify the form-level claim — it
demonstrates that the headline measures form only, which is why the grant
semantics rider is exploratory.  The receipt for C4 therefore exists BEFORE the
claim's data is landed.

THE LANE IS READ-ONLY

``--base-tree`` is only read, with ``git -C <base-tree> show``.  Every world
lives under ``--work`` (default: a fresh ``mktemp -d`` under ``$TMPDIR``).
Nothing outside the world's own repo is written; the lane, the fleet root and
the sibling lanes are never touched.

WORLD SHAPE

  1. ``D=$(mktemp -d -p "$WORK")``; ``git -C "$D" init -q``; identity
     ``scratch-r80`` / ``scratch@example.invalid``; ``git -C "$D" rev-parse
     --show-toplevel`` must print ``$D`` (a fixture outside its own repo is the
     classic way a damaged world writes into the caller's checkout).
  2. ``$D/.git/objects/info/alternates`` points at the base clone's object store
     (one line, read-only sharing — what ``git clone --shared`` writes).  It
     exists so the counter's frozen ``BASE_REV`` resolves inside the world
     without copying the object store per world.
  3. ``git -C "$D" read-tree <base-rev>`` seeds the index with the real base
     tree, so a measured commit is "the base tree with the world's fixture
     files replaced" — the same shape as a lane commit.
  4. Fixtures are written as blobs (``hash-object -w --stdin`` +
     ``update-index --cacheinfo``); deletions use ``update-index
     --force-remove``.  No worktree is checked out.
  5. ``write-tree`` + ``commit-tree -p <base-rev>`` + ``update-ref`` produce the
     measured commit; the counter is then run with ``--repo <D> --rev <commit>``.

THE COUNTER UNDER TEST

``--counter`` is the counter file to run, verbatim.  Its own constants
(``ENTRY``, ``SNAPDIR``, ``MANIFEST``, ``CAPTURE``, ``TARGET``, ``SURFACES``,
…) are read by importing the file as a module, so this generator follows
whatever the counter freezes instead of hard-coding them.  The counter's own
drift guard (its ``SELF_SHA``) is honoured: the counter decides whether the
bytes it is running are the bytes it was frozen as.

USAGE

  python3 -B .ufo/waves/round-80/build/c2_controls.py \\
      --counter .ufo/waves/round-80/build/check_allowed_tools.py \\
      --base-tree <clone at the base revision> \\
      --work /fast/scratch/hyaku/kotoba-r80/Kb80E09C2Worlds/work \\
      --out .ufo/waves/round-80/build/Kb80E09C2Worlds.run.log

  --list          print the pre-registered expectation table and exit
  --only C3,C6    run only the named worlds
  --keep          keep the world repos (default: removed after each run)
  --verbose       print every counter line for every world
  --json          write the machine-readable summary to stdout as JSON
  --out FILE      write the full log to FILE (the receipt)
  --timeout N     per-counter-run timeout in seconds (default 300)

Exit codes: 0 every world matched its pre-registration; 1 at least one world
diverged (or a counter could not be run); 2 environment (no counter file, no
base tree, unreadable base revision, world build failure, generator
self-check failure).
"""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

LANE = Path("/home/vgpnk/Projects/shokunin/kotoba-shokunin")
DEFAULT_BASE_REV = "398cbe1bb67f8d9dcf5d25d5ecf1b26a7c6f7e93"
FETCH_TS = "2026-10-27T21:41:23Z"

# --------------------------------------------------------------------------
# The frozen surface table (plans/round-80.md § C2: "Frozen surface/header/
# first-cell table and grant labels as the r79 plan § C2").  This is PLAN data,
# not counter code: the generator below reads the page bytes and applies the
# rules to them.
#   sid        the corpus id the row cites
#   display    the frozen first cell of the surface-table row
#   url        the frozen page URL (also the registry row's URL)
#   host       the frozen host pin (bare host, or host + whole-segment path)
#   title      the registry row's source cell title
#   section    the located section, quoted in the anchor cell
#   snap       the committed snapshot file name under the snapshot directory
#   page_token the frozen page token that grounds the grant label
#   grant      the frozen grant label
# --------------------------------------------------------------------------
SURFACES = [
    dict(key="spec", sid="S226", display="Open specification", short="spec",
         url="https://agentskills.io/specification.md",
         host=("agentskills.io",),
         title="Agent Skills — Specification",
         kind="spec", tier="A",
         section="#### allowed-tools field",
         snap="S226-spec.md",
         page_token="Experimental", grant="experimental"),
    dict(key="claude", sid="S227", display="Claude Code", short="claude",
         url="https://code.claude.com/docs/en/skills.md",
         host=("code.claude.com",),
         title="Claude Code — Extend Claude with skills",
         kind="docs", tier="B",
         section="§ Pre-approve tools for a skill",
         snap="S227-claude.md",
         page_token="without prompting you for approval", grant="pre-approves"),
    dict(key="factory", sid="S228", display="Factory", short="factory",
         url="https://docs.factory.com/harness/skills",
         host=("docs.factory.com/harness/skills",),
         title="Factory — Skills",
         kind="docs", tier="B",
         section="§ Declare intended tools",
         snap="S228-factory.md",
         page_token="metadata", grant="metadata-only"),
    dict(key="msaf", sid="S229", display="Microsoft Agent Framework",
         short="msaf",
         url="https://learn.microsoft.com/en-us/agent-framework/agents/skills",
         host=("learn.microsoft.com",),
         title="Microsoft Learn — Agent Framework: Agent Skills",
         kind="docs", tier="B",
         section="§ SKILL.md format",
         snap="S229-msaf.html",
         page_token="Experimental", grant="experimental"),
    dict(key="pi", sid="S230", display="pi", short="pi",
         url="https://raw.githubusercontent.com/badlogic/pi-mono/main/"
             "packages/coding-agent/docs/skills.md",
         host=("raw.githubusercontent.com/badlogic/pi-mono",),
         title="pi coding agent (pi-mono) — Skills",
         kind="docs", tier="B",
         section="§ Write portable frontmatter",
         snap="S230-pi.md",
         page_token="Experimental", grant="experimental"),
    dict(key="vibe", sid="S231", display="Mistral Vibe", short="vibe",
         url="https://raw.githubusercontent.com/mistralai/mistral-vibe/main/"
             "README.md",
         host=("raw.githubusercontent.com/mistralai/mistral-vibe",),
         title="Mistral Vibe — README (skills system and skill frontmatter)",
         kind="docs", tier="B",
         section="§ Skills System → § Creating Skills",
         snap="S231-vibe.md",
         page_token="allowed-tools:", grant="unstated"),
]
BY_KEY = {s["key"]: s for s in SURFACES}
BY_SID = {s["sid"]: s for s in SURFACES}
ORDER = [s["key"] for s in SURFACES]

# Where the round-80 snapshot bytes live in the base tree (the round-80 plan
# keeps them where round 79 committed them).
BASE_SNAPDIR = ".ufo/waves/round-79/snapshots"

MIN_QUOTE_WORDS = 5
MAX_QUOTE_WORDS = 25

# The frozen keyword rule that maps a scraped quote to a grant label.  The
# order is frozen (first match wins); each cue is a surface's frozen page token.
LABEL_CUES = (
    ("pre-approves", "without prompting you for approval"),
    ("metadata-only", "metadata"),
    ("experimental", "Experimental"),
)

# The frozen stop list: words the generator never uses as a value-form token.
STOP_WORDS = frozenset("""
a an the and or of to in is are was were be been being for with it its that
this these those as at by on from if then else when where which what who how
why all any each every one two so such use used uses using list lists listed
tool tools field fields string strings name names run runs value values
""".split())


# ---------------------------------------------------------------- text shaping
# The snapshot text view of plans/round-80.md § C2 (Q42/Q53/Q56 as amended
# before any data).  Implemented here independently of the counter's code.
SCRIPT_STYLE_RE = re.compile(r"(?is)<(script|style)\b.*?</\1\s*>")
TAG_RE = re.compile(r"(?s)</?[A-Za-z][^>]*>")
LIST_MARKER_RE = re.compile(r"(?m)^[ \t]{0,3}[*+\-][ \t]+")
BARE_NAME_RE = re.compile(r"^[A-Za-z][A-Za-z0-9_.@/-]*$")
VALUE_SHAPE_RE = re.compile(r"[()\[\],:*<>{}]")


def ws(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()


def text_view(name: str, raw: str) -> list[str]:
    """The snapshot text view, line by line, whitespace collapsed per line."""
    low = name.lower()
    if low.endswith((".html", ".htm")):
        raw = SCRIPT_STYLE_RE.sub(" ", raw)
        raw = TAG_RE.sub(" ", raw)
        import html as _html
        raw = _html.unescape(raw)
    elif low.endswith((".md", ".markdown")):
        raw = raw.replace("`", "")
        raw = LIST_MARKER_RE.sub("", raw)
    return [ln for ln in (ws(line) for line in raw.splitlines()) if ln]


def word_bounded(needle: str, haystack: str) -> bool:
    return re.search(r"(?<![A-Za-z0-9_])" + re.escape(needle)
                     + r"(?![A-Za-z0-9_])", haystack) is not None


def word_bounded_ci(needle: str, haystack: str) -> bool:
    return re.search(r"(?<![A-Za-z0-9_])" + re.escape(needle)
                     + r"(?![A-Za-z0-9_])", haystack, re.I) is not None


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def escape_cell(text: str) -> str:
    """A literal ``|`` is cell content, not a column break."""
    return text.replace("|", "\\|")


def split_cells(line: str) -> list[str]:
    """Escape-aware markdown table cell split (a ``\\|`` is cell content)."""
    s = line.strip()
    if not (s.startswith("|") and s.endswith("|")) or len(s) < 2:
        return []
    body = s[1:-1]
    cells: list[str] = []
    cur: list[str] = []
    i = 0
    while i < len(body):
        ch = body[i]
        if ch == "\\" and i + 1 < len(body) and body[i + 1] == "|":
            cur.append("|")
            i += 2
            continue
        if ch == "|":
            cells.append("".join(cur).strip())
            cur = []
            i += 1
            continue
        cur.append(ch)
        i += 1
    cells.append("".join(cur).strip())
    return cells


# ------------------------------------------------------------- counter import
def load_counter(path: Path):
    spec = importlib.util.spec_from_file_location("c2_counter_under_test",
                                                  str(path))
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot import counter {path}")
    mod = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = mod
    spec.loader.exec_module(mod)
    return mod


class Counter:
    """The counter under test, with its constants read out of its own bytes."""

    def __init__(self, path: Path):
        self.path = path
        self.mod = load_counter(path)
        self.bytes = path.read_bytes()
        self.sha256 = sha256_bytes(self.bytes)
        self.entry = getattr(self.mod, "ENTRY")
        self.snapdir = getattr(self.mod, "SNAPDIR")
        self.manifest = getattr(self.mod, "MANIFEST")
        self.capture = getattr(self.mod, "CAPTURE")
        self.total = int(getattr(self.mod, "TOTAL", 6))
        self.target = int(getattr(self.mod, "TARGET", 6))
        self.province = getattr(self.mod, "PROVINCE")
        self.skill = getattr(self.mod, "SKILLMD")
        self.counter_path = getattr(self.mod, "COUNTER_PATH")
        self.sources = getattr(self.mod, "SOURCES")
        self.surfaces = getattr(self.mod, "SURFACES")
        self.grant_labels = tuple(getattr(self.mod, "GRANT_LABELS"))


# ------------------------------------------------------------ git plumbing
class GitError(RuntimeError):
    pass


def git(repo: Path, args: list[str], stdin: bytes | None = None,
        check: bool = True) -> subprocess.CompletedProcess:
    proc = subprocess.run(["git", "-C", str(repo), *args], input=stdin,
                          capture_output=True)
    if check and proc.returncode != 0:
        raise GitError(f"git -C {repo} {' '.join(args)}: "
                       f"{proc.stderr.decode('utf-8', 'replace').strip()}")
    return proc


def base_blob(base: Path, rev: str, path: str) -> bytes | None:
    proc = git(base, ["show", f"{rev}:{path}"], check=False)
    return proc.stdout if proc.returncode == 0 else None


# --------------------------------------------- the independent mechanical gen
def scrape_quote(lines: list[str], surface: dict) -> str | None:
    """C4's quote rule — a fixed window rule, no judgement.

    The window starts at a word-bounded ``allowed-tools`` occurrence and ends
    at the end of the surface's frozen page token when that token follows
    within 25 words; otherwise it ends at the end of the occurrence's line.  A
    window shorter than five words is extended forwards word by word.  The
    FIRST admissible window wins; a window that carries a double quote is
    skipped (a quoted cell cannot carry one).
    """
    joined = " ".join(lines)
    key = "allowed-tools"
    token = surface["page_token"]
    for m in re.finditer(r"(?<![A-Za-z0-9_])" + re.escape(key)
                         + r"(?![A-Za-z0-9_])", joined):
        start = m.start()
        tail = joined[m.end():]
        tm = re.search(r"(?<![A-Za-z0-9_])" + re.escape(token)
                       + r"(?![A-Za-z0-9_])", tail, re.I)
        if tm is not None:
            end = m.end() + tm.end()
            if len(joined[start:end].split()) > MAX_QUOTE_WORDS:
                continue
        else:
            nxt = joined.find(" ", m.end())
            end = len(joined) if nxt < 0 else nxt
        while len(joined[start:end].split()) < MIN_QUOTE_WORDS:
            nxt = joined.find(" ", end)
            if nxt < 0:
                break
            end = nxt + 1
        words = joined[start:end].split()
        if not (MIN_QUOTE_WORDS <= len(words) <= MAX_QUOTE_WORDS):
            continue
        cand = ws(joined[start:end])
        if '"' in cand:
            continue
        return cand
    return None


def label_for_quote(quote: str) -> str:
    """C4's label rule — a frozen keyword rule over the scraped quote."""
    for label, cue in LABEL_CUES:
        if word_bounded_ci(cue, quote):
            return label
    return "unstated"


def value_token(quote: str, page_token: str = "") -> str | None:
    """C4's value token: the first token after the key token that the
    counter's own value-shape grammar accepts (a bare name or a token
    carrying a value shape), skipping stop words and the page token (the page
    token is the grant-semantics token, and a token cannot fill two roles).
    """
    words = quote.split()
    idx = next((i for i, w in enumerate(words)
                if word_bounded("allowed-tools", w)), None)
    if idx is None:
        return None
    for w in words[idx + 1:]:
        w = w.strip(",.;:()[]|")
        if not w or w.lower() in STOP_WORDS:
            continue
        if word_bounded("allowed-tools", w):
            continue
        if page_token and word_bounded_ci(page_token, w):
            continue
        if BARE_NAME_RE.match(w) or VALUE_SHAPE_RE.search(w):
            return w
    return None


def mechanical_entry(pages: dict[str, bytes], counter: Counter,
                     capture: str) -> tuple[str, dict[str, str]]:
    """C4: the complete entry shape, emitted with no judgement.

    ``pages`` maps the surface key to the committed snapshot bytes.  Returns
    ``(entry_text, {key: quote})``.
    """
    quotes: dict[str, str] = {}
    rows: list[str] = []
    head: list[str] = []
    for key in ORDER:
        s = BY_KEY[key]
        lines = text_view(s["snap"], pages[key].decode("utf-8", "replace"))
        quote = scrape_quote(lines, s)
        if quote is None:
            raise SystemExit(f"C4 scrape failed for {s['sid']}: no admissible "
                             f"window carries `allowed-tools` and "
                             f"{s['page_token']!r}")
        quotes[key] = quote
        head.append(f"source: {s['sid']} — {s['title']} — {s['url']} — "
                    f"{s['section']} — located quote \"{escape_cell(quote)}\" "
                    f"(snapshot `{s['snap']}`)")
    for key in ORDER:
        s = BY_KEY[key]
        quote = quotes[key]
        label = label_for_quote(quote)
        val = value_token(quote, s["page_token"])
        toks = ["allowed-tools"]
        if val:
            toks.append(val)
        toks.append(s["page_token"])
        tok_cell = ", ".join(f"`{t}`" for t in toks)
        rows.append(f"| {s['display']} | {s['sid']} | {tok_cell} | {label} | "
                    f"\"{escape_cell(quote)}\" |")
    body = ["", f"verified-at: {capture}",
            "recheck: 90d — curl each URL and grep -c -F 'allowed-tools' "
            "against the pinned snapshot",
            "",
            "view: `.html` snapshots lose `script` and `style` blocks, tags "
            "become one space and entities are decoded; Markdown snapshots "
            "lose every backtick byte and an unordered-list marker; every "
            "whitespace run is then collapsed.",
            "",
            "# allowed-tools surfaces", "",
            "| surface | source | page tokens | grant | located quote |",
            "|---|---|---|---|---|"]
    return "\n".join(head + body + rows) + "\n", quotes


# ------------------------------------------------------------ world fixtures
def base_registry_rows(base: Path, rev: str) -> dict[str, list[str]]:
    """The base tree's own registry rows for the six ids (cells, verbatim)."""
    text = base_blob(base, rev, "corpus/SOURCES.md")
    if text is None:
        raise SystemExit("environment: corpus/SOURCES.md is absent at the base "
                         "revision")
    out: dict[str, list[str]] = {}
    for line in text.decode("utf-8", "replace").splitlines():
        m = re.match(r"^\|\s*(S\d{3,})\s*\|", line)
        if not m or m.group(1) not in BY_SID:
            continue
        cells = split_cells(line)
        if cells:
            out[m.group(1)] = cells
    return out


def registry_rows_for(entry_path: str, capture: str, quotes: dict[str, str],
                      pins: dict[str, tuple[str, int]],
                      base_rows: dict[str, list[str]],
                      urls: dict[str, str] | None = None,
                      sha_break: tuple[str, ...] = (),
                      used_by: str | None = None,
                      corpus_anchor: bool = False) -> list[str]:
    """One 11-cell registry row per surface, in the counter's expected shape.

    ``corpus_anchor`` writes the anchor cell in the CORPUS's own format
    (``fetched <date>, HTTP 200, N B, sha256 `<hex>```) instead of the
    counter's fetch-record grammar; the arm exists to measure whether the
    counter can read the corpus rows as they are committed.
    """
    urls = urls or {}
    out: list[str] = []
    for key in ORDER:
        s = BY_KEY[key]
        base = base_rows.get(s["sid"], [])
        scope = base[4] if len(base) > 4 else f"{s['title']} documents the field"
        teaches = base[6] if len(base) > 6 else "what the page says about the field"
        digest, nbytes = pins[key]
        if s["sid"] in sha_break:
            digest = "0" * 64
        if corpus_anchor:
            anchor = (f"{s['section']}, snapshot {s['snap']}; "
                      f"fetched 2026-10-27, HTTP 200, {nbytes} B, "
                      f"sha256 `{digest}`; located quote "
                      f"\"{escape_cell(quotes[key])}\"")
        else:
            anchor = (f"{s['section']}, snapshot {s['snap']}; "
                      f"fetched {FETCH_TS}, HTTP 200, {nbytes} B, "
                      f"sha256 {digest}; located quote "
                      f"\"{escape_cell(quotes[key])}\"")
        cells = [
            s["sid"],
            f"{s['title']} — {urls.get(key, s['url'])}",
            s["kind"],
            s["tier"],
            escape_cell(scope),
            escape_cell(anchor),
            escape_cell(teaches),
            "mined",
            capture,
            "90d",
            used_by if used_by is not None else entry_path,
        ]
        assert len(cells) == 11, cells
        out.append("| " + " | ".join(cells) + " |")
    return out


def registry_document(base_text: str, rows: list[str]) -> str:
    """The base SOURCES.md with the six rows replaced in place."""
    by_sid = {BY_KEY[k]["sid"]: r for k, r in zip(ORDER, rows)}
    out: list[str] = []
    seen: set[str] = set()
    for line in base_text.splitlines():
        m = re.match(r"^\|\s*(S\d{3,})\s*\|", line)
        if m and m.group(1) in by_sid:
            out.append(by_sid[m.group(1)])
            seen.add(m.group(1))
            continue
        out.append(line)
    for sid, row in by_sid.items():
        if sid not in seen:
            out.append(row)
    return "\n".join(out) + "\n"


def skill_document(base_text: str, entry_path: str, counter_path: str,
                   rule_line: str, registry_row: str) -> str:
    """The base SKILL.md with one rule line and one gate-registry row added."""
    lines = base_text.splitlines()
    out: list[str] = []
    inserted_row = False
    inserted_rule = False
    skip_sep = False
    for line in lines:
        if skip_sep and line.startswith("|---"):
            skip_sep = False
            continue
        skip_sep = False
        out.append(line)
        if not inserted_rule and line.startswith("## "):
            out.append("")
            out.append(rule_line)
            inserted_rule = True
        if (not inserted_row
                and line.startswith("| Name | Kind | Entry command |")):
            out.append("|---|---|---|---|---|---|---|---|")
            out.append(registry_row)
            inserted_row = True
            skip_sep = True
    text = "\n".join(out) + "\n"
    if not inserted_rule:
        text += "\n" + rule_line + "\n"
    if not inserted_row:
        text += "\n" + registry_row + "\n"
    return text


def province_document(base_text: str, entry_path: str, bullet: str) -> str:
    """The base PROVINCE.md with one Core bullet naming the entry."""
    lines = base_text.splitlines()
    out: list[str] = []
    inserted = False
    for line in lines:
        if (not inserted and line.startswith("## ")
                and not line.startswith("## Core")):
            out.append(bullet)
            out.append("")
            inserted = True
        out.append(line)
    if not inserted:
        out.append(bullet)
    return "\n".join(out) + "\n"


def manifest_document(pins: dict[str, tuple[str, int]]) -> str:
    """``<sha256>  <basename>`` lines — the counter's manifest grammar."""
    return "".join(f"{digest}  {BY_KEY[key]['snap']}\n"
                    for key, (digest, _n) in pins.items())


def rule_line(entry: str) -> str:
    return ("- `allowed-tools` per client: the Open specification, Claude "
            "Code, Factory, the Microsoft Agent Framework, pi and Mistral Vibe "
            f"are documented in `{entry}`.")


def registry_row(counter: Counter) -> str:
    return (f"| `{counter.counter_path}` | gate | `python3 -B "
            f"{counter.counter_path} --rev <rev>` | 0=clean, 1=failed, "
            "2=could-not-evaluate | `--self-test` | in-file | none | kotoba |")


def province_bullet(entry: str) -> str:
    return ("- `allowed-tools` surfaces per client — the Open specification, "
            "Claude Code, Factory, the Microsoft Agent Framework, pi and "
            f"Mistral Vibe — in `{entry}`.")


def corpus_quotes_of(base_rows: dict[str, list[str]]) -> dict[str, str]:
    """Each surface's CORPUS-recorded located quote, verbatim.

    The quote is taken from the base tree's own registry row (the anchor
    cell's ``located quote "..."``), so the oracle world carries the corpus's
    evidence, not a fresh scrape.
    """
    out: dict[str, str] = {}
    for key in ORDER:
        s = BY_KEY[key]
        cells = base_rows.get(s["sid"], [])
        anchor = cells[5] if len(cells) > 5 else ""
        m = re.search(r'located quote "(.*?)"', anchor)
        out[key] = m.group(1) if m else ""
    return out


def entry_text_with_quotes(entry_text: str, quotes: dict[str, str],
                           urls: dict[str, str] | None = None) -> str:
    """The entry text with each row's located quote replaced (and, when asked,
    each surface's URL replaced in the table row and the source: line)."""
    urls = urls or {}
    out: list[str] = []
    for line in entry_text.splitlines():
        if line.startswith("| ") and line.endswith(" |"):
            cells = split_cells(line)
            if len(cells) == 5:
                key = next((k for k in ORDER
                            if cells[0] == BY_KEY[k]["display"]), None)
                if key is not None:
                    cells[4] = f"\"{escape_cell(quotes[key])}\""
                    line = "| " + " | ".join(cells) + " |"
        elif line.startswith("source: ") and urls:
            for key, url in urls.items():
                if BY_KEY[key]["sid"] in line:
                    line = line.replace(BY_KEY[key]["url"], url)
        out.append(line)
    return "\n".join(out) + "\n"


# ------------------------------------------------------------------- worlds
def world_files(name: str, counter: Counter, pages: dict[str, bytes],
                base_rows: dict[str, list[str]],
                base_text: dict[str, str],
                s05_text: str = "") -> tuple[dict[str, str | None],
                                            list[str], str | None]:
    """(files, notes, measured_rev_or_None).  A ``None`` file value deletes a
    base-tree path; a ``None`` rev means "measure the base revision"."""
    entry = counter.entry
    notes: list[str] = []
    pins = {key: (sha256_bytes(pages[key]), len(pages[key])) for key in ORDER}
    entry_text, quotes = mechanical_entry(pages, counter, counter.capture)
    rows = registry_rows_for(entry, counter.capture, quotes, pins, base_rows)

    def skill() -> str:
        return skill_document(base_text["skill"], entry, counter.counter_path,
                              rule_line(entry), registry_row(counter))

    def province() -> str:
        return province_document(base_text["province"], entry,
                                 province_bullet(entry))

    def snapshots(src: dict[str, bytes]) -> dict[str, str | None]:
        return {f"{counter.snapdir}/{BY_KEY[k]['snap']}": src[k] for k in ORDER}

    if name == "C0":
        return {}, ["the base tree, unmodified (no entry, no manifest, no "
                    "registry change)"], None

    if name == "C1":
        files = {
            counter.sources: registry_document(base_text["sources"], rows),
            entry: entry_text,
            counter.skill: skill(),
            counter.province: province(),
            counter.manifest: None,
        }
        for k in ORDER:
            files[f"{counter.snapdir}/{BY_KEY[k]['snap']}"] = None
        return files, ["the entry names every token and label; the six "
                       "snapshot files and the manifest are deleted, so "
                       "nothing can be pinned"], "HEAD"

    if name == "C2":
        shifted = {ORDER[i]: quotes[ORDER[(i + 1) % len(ORDER)]]
                   for i in range(len(ORDER))}
        shifted_rows = registry_rows_for(entry, counter.capture, shifted,
                                         pins, base_rows)
        files = {
            counter.sources: registry_document(base_text["sources"],
                                               shifted_rows),
            entry: entry_text_with_quotes(entry_text, shifted),
            counter.manifest: manifest_document(pins),
            counter.skill: skill(),
            counter.province: province(),
            **snapshots(pages),
        }
        return files, ["every row's located quote is another surface's page "
                       "text (real committed bytes, not synthetic)"], "HEAD"

    if name == "C3":
        banner = ("Site banner: allowed-tools Experimental metadata "
                  "pre-approved without prompting you for approval "
                  "allowed-tools:")
        banner_pages = {k: pages[k] + ("\n" + banner + "\n").encode()
                        for k in ORDER}
        banner_pins = {k: (sha256_bytes(banner_pages[k]),
                           len(banner_pages[k])) for k in ORDER}
        banner_rows = registry_rows_for(entry, counter.capture, quotes,
                                        banner_pins, base_rows)
        files = {
            counter.sources: registry_document(base_text["sources"],
                                               banner_rows),
            entry: entry_text_with_quotes(entry_text,
                                          {k: banner for k in ORDER}),
            counter.manifest: manifest_document(banner_pins),
            counter.skill: skill(),
            counter.province: province(),
            **snapshots(banner_pages),
        }
        return files, ["one identical banner line is appended to all six "
                       "snapshots and quoted by every row (Q70's shared "
                       "banner rule)"], "HEAD"

    if name == "C4":
        files = {
            counter.sources: registry_document(base_text["sources"], rows),
            entry: entry_text,
            counter.manifest: manifest_document(pins),
            counter.skill: skill(),
            counter.province: province(),
            **snapshots(pages),
        }
        notes.append("the INDEPENDENT mechanical generator (this file): quote "
                     "scraped by a fixed window rule, label chosen by a "
                     "frozen keyword rule, tokens derived from the quote, "
                     "pins computed from the committed bytes")
        for k in ORDER:
            notes.append(f"derived {BY_KEY[k]['sid']}: {quotes[k]}")
        return files, notes, "HEAD"

    if name == "H0":
        # the plumbing oracle: the honest world carrying each surface's
        # CORPUS-recorded located quote verbatim (from corpus/SOURCES.md),
        # so the baseline is measured against the corpus's own evidence
        corpus_quotes = corpus_quotes_of(base_rows)
        h_rows = registry_rows_for(entry, counter.capture, corpus_quotes,
                                   pins, base_rows)
        files = {
            counter.sources: registry_document(base_text["sources"], h_rows),
            entry: entry_text_with_quotes(entry_text, corpus_quotes),
            counter.manifest: manifest_document(pins),
            counter.skill: skill(),
            counter.province: province(),
            **snapshots(pages),
        }
        notes.append("the corpus's own recorded located quotes, verbatim, one "
                     "per surface")
        for k in ORDER:
            notes.append(f"corpus quote {BY_KEY[k]['sid']}: "
                         f"{corpus_quotes[k]!r}")
        return files, notes, "HEAD"

    if name == "S05":
        # the DECISIVE arm: the corpus rows as the corpus edit seat published
        # them (Kb80S05SourcesEdits.patch), i.e. the rows the L1 would land.
        # Everything else is the honest mechanical world.
        s05_rows = {}
        for line in s05_text.splitlines():
            mm = re.match(r"^\|\s*(S\d{3,})\s*\|", line)
            if mm and mm.group(1) in {BY_KEY[k]["sid"] for k in ORDER}:
                s05_rows[mm.group(1)] = line
        files = {
            counter.sources: s05_text,
            entry: entry_text,
            counter.manifest: manifest_document(pins),
            counter.skill: skill(),
            counter.province: province(),
            **snapshots(pages),
        }
        notes.append("the registry is the corpus edit seat's published "
                     "corpus/SOURCES.md (Kb80S05SourcesEdits.patch applied), "
                     "verbatim — the six C2 rows exactly as the L1 would land "
                     "them")
        for k in ORDER:
            notes.append(f"corpus row {BY_KEY[k]['sid']}: "
                         f"{s05_rows.get(BY_KEY[k]['sid'], '(ABSENT)')[:200]}")
        return files, notes, "HEAD"

    if name == "S05b":
        # the ISOLATION arm: the corpus edit seat's published rows with ONLY
        # the anchor's fetch record rewritten into the counter's grammar (the
        # same date, the same bytes, the same digest, only the rendering
        # changed).  It isolates the anchor grammar from every other cause.
        # the corpus renders the record as
        #   fetched <date>, HTTP 200, <bytes> B, sha256 `<hex>`
        # and the counter's grammar wants
        #   fetched <date>T<time>Z, HTTP 200, <bytes> B, sha256 <hex>
        # (a full ISO instant, and the digest NOT in backticks).
        fixed = re.sub(
            r"fetched (\d{4}-\d\d-\d\d), HTTP 200, (\d+) B, sha256 "
            r"`([0-9a-f]{64})`",
            r"fetched \1T00:00:00Z, HTTP 200, \2 B, sha256 \3",
            s05_text)
        files = {
            counter.sources: fixed,
            entry: entry_text,
            counter.manifest: manifest_document(pins),
            counter.skill: skill(),
            counter.province: province(),
            **snapshots(pages),
        }
        notes.append("the corpus edit seat's published rows with ONLY the "
                     "anchor's fetch-record rendering normalised to the "
                     "counter's grammar (same date, same bytes, same digest)")
        return files, notes, "HEAD"

    if name == "G0":
        # the generator-world isolation arm: the honest world, but with a
        # registry whose used-by names ONLY the entry (the six C2 rows and
        # nothing else), so the counter's own generator world finds the six
        # rows by host and scores them
        g_rows = registry_rows_for(entry, counter.capture, quotes, pins,
                                   base_rows)
        files = {
            counter.sources: ("# SOURCES (control world)\n\n## Registry\n\n"
                              + "| id | source | kind | tier | scope | anchor "
                              "| teaches | status | opened | recheck | used-by |\n"
                              + "|---|---|---|---|---|---|---|---|---|---|---|\n"
                              + "\n".join(g_rows) + "\n"),
            entry: entry_text,
            counter.manifest: manifest_document(pins),
            counter.skill: skill(),
            counter.province: province(),
            **snapshots(pages),
        }
        return files, ["the honest world with a registry carrying only the "
                       "six C2 rows, so the counter's own generator world "
                       "finds them by host"], "HEAD"

    if name == "C4b":
        # the same world with the registry anchors in the CORPUS's own format
        corpus_rows = registry_rows_for(entry, counter.capture, quotes, pins,
                                        base_rows, corpus_anchor=True)
        files = {
            counter.sources: registry_document(base_text["sources"],
                                               corpus_rows),
            entry: entry_text,
            counter.manifest: manifest_document(pins),
            counter.skill: skill(),
            counter.province: province(),
            **snapshots(pages),
        }
        return files, ["diagnostic arm: the registry anchors carry the "
                       "corpus's own fetch-record format "
                       "(`fetched <date>, HTTP 200, N B, sha256 `<hex>``) "
                       "instead of the counter's fetch-record grammar"], "HEAD"

    if name == "C5":
        label_rows = []
        for k in ORDER:
            s = BY_KEY[k]
            toks = ", ".join(f"`{t}`" for t in
                             ("allowed-tools", s["page_token"], "read"))
            label_rows.append(f"| {s['display']} | {s['sid']} | {toks} | "
                              f"{s['grant']} |  |")
        head = []
        for k in ORDER:
            s = BY_KEY[k]
            head.append(f"source: {s['sid']} — {s['title']} — {s['url']} — "
                        f"{s['section']} (snapshot `{s['snap']}`)")
        files = {
            counter.sources: registry_document(base_text["sources"], rows),
            entry: ("\n".join(head) + "\n\n"
                    + f"verified-at: {counter.capture}\n"
                    + "recheck: 90d — re-fetch and confirm\n\n"
                    + "view: `.html` snapshots lose `script` and `style` "
                      "blocks, tags become one space and entities are "
                      "decoded; Markdown snapshots lose every backtick byte "
                      "and an unordered-list marker; every whitespace run is "
                      "then collapsed.\n\n# allowed-tools surfaces\n\n"
                    + "| surface | source | page tokens | grant | located "
                      "quote |\n|---|---|---|---|---|\n"
                    + "\n".join(label_rows) + "\n"),
            counter.manifest: manifest_document(pins),
            counter.skill: skill(),
            counter.province: province(),
            **snapshots(pages),
        }
        return files, ["grant labels and page tokens, no located quote "
                       "anywhere"], "HEAD"

    if name == "C6":
        evil = {"pi": "https://raw.githubusercontent.com/badlogic/pi-mono-evil/"
                      "main/packages/coding-agent/docs/skills.md"}
        evil_rows = registry_rows_for(entry, counter.capture, quotes, pins,
                                      base_rows, urls=evil)
        files = {
            counter.sources: registry_document(base_text["sources"], evil_rows),
            entry: entry_text_with_quotes(entry_text, quotes, urls=evil),
            counter.manifest: manifest_document(pins),
            counter.skill: skill(),
            counter.province: province(),
            **snapshots(pages),
        }
        return files, ["pi's registry row AND its source: line cite "
                       "`…/badlogic/pi-mono-evil/…` — a string prefix of the "
                       "frozen host pin, which Q32 rejects"], "HEAD"

    if name == "C7":
        tampered = pages["pi"] + b"\nA byte added after the pin was written.\n"
        files = {
            counter.sources: registry_document(base_text["sources"], rows),
            entry: entry_text,
            counter.manifest: manifest_document(pins),
            counter.skill: skill(),
            counter.province: province(),
            **snapshots(pages),
        }
        files[f"{counter.snapdir}/{BY_KEY['pi']['snap']}"] = tampered
        return files, ["pi's committed snapshot bytes changed after the pin "
                       "was written (the pin and the anchor still name the "
                       "old bytes)"], "HEAD"

    if name == "C7b":
        bad_rows = registry_rows_for(entry, counter.capture, quotes, pins,
                                     base_rows, sha_break=("S230",))
        files = {
            counter.sources: registry_document(base_text["sources"], bad_rows),
            entry: entry_text,
            counter.manifest: manifest_document(pins),
            counter.skill: skill(),
            counter.province: province(),
            **snapshots(pages),
        }
        return files, ["pi's registry anchor carries a sha256 that is not the "
                       "snapshot's pin (the snapshot bytes are intact)"], "HEAD"

    if name == "C8":
        files = {
            counter.sources: registry_document(base_text["sources"], rows),
            counter.manifest: manifest_document(pins),
            counter.skill: skill(),
            counter.province: province(),
            "corpus/lessons/round-80-first-answer.md":
                "# round 80 — first answer (control)\n\n"
                "The census counts six pages that state the `allowed-tools` "
                "field, so all six surfaces are documented (6 of 6) with no "
                "entry, no snapshot and no pin at all.\n",
            **snapshots(pages),
        }
        files[entry] = None
        return files, ["no entry file; the 6 of 6 figure is asserted in prose "
                       "only"], "HEAD"

    raise SystemExit(f"unknown world {name}")


# ----------------------------------------------------------------- build/run
def build_world(work: Path, base: Path, base_rev: str,
                files: dict[str, str | None], counter_bytes: bytes | None,
                counter_path: str, tag: str) -> tuple[Path, str]:
    d = Path(tempfile.mkdtemp(prefix=f"{tag}-", dir=str(work)))
    try:
        git(d, ["init", "-q"])
        git(d, ["config", "user.name", "scratch-r80"])
        git(d, ["config", "user.email", "scratch@example.invalid"])
        top = git(d, ["rev-parse", "--show-toplevel"]).stdout.decode().strip()
        if Path(top).resolve() != d.resolve():
            raise GitError(f"fixture toplevel {top!r} is not {d}")
        obj = git(base, ["rev-parse", "--git-path",
                         "objects"]).stdout.decode().strip()
        obj_path = Path(obj)
        if not obj_path.is_absolute():
            obj_path = (base / obj_path).resolve()
        info = d / ".git" / "objects" / "info"
        info.mkdir(parents=True, exist_ok=True)
        (info / "alternates").write_text(str(obj_path) + "\n")
        if git(d, ["cat-file", "-t", f"{base_rev}^{{commit}}"],
               check=False).returncode != 0:
            raise GitError(f"base revision {base_rev} is not readable through "
                           f"the alternate {obj_path}")
        git(d, ["read-tree", base_rev])
        for rel, text in files.items():
            if text is None:
                git(d, ["update-index", "--force-remove", rel], check=False)
                continue
            payload = text if isinstance(text, bytes) else text.encode()
            blob = git(d, ["hash-object", "-w", "--stdin"],
                       stdin=payload).stdout.decode().strip()
            git(d, ["update-index", "--add", "--cacheinfo",
                    f"100644,{blob},{rel}"])
        if counter_bytes is not None:
            blob = git(d, ["hash-object", "-w", "--stdin"],
                       stdin=counter_bytes).stdout.decode().strip()
            git(d, ["update-index", "--add", "--cacheinfo",
                    f"100755,{blob},{counter_path}"])
        tree = git(d, ["write-tree"]).stdout.decode().strip()
        commit = git(d, ["commit-tree", tree, "-p", base_rev],
                     stdin=f"c2r80 control world {tag}\n".encode()
                     ).stdout.decode().strip()
        git(d, ["update-ref", f"refs/heads/{tag}", commit])
        return d, commit
    except Exception:
        shutil.rmtree(d, ignore_errors=True)
        raise


def run_counter(counter: Counter, world: Path, rev: str,
                timeout: int) -> tuple[int, str]:
    proc = subprocess.run(
        [sys.executable, "-B", str(counter.path), "--repo", str(world),
         "--rev", rev],
        capture_output=True, text=True, cwd=str(world), timeout=timeout)
    return proc.returncode, (proc.stdout or "") + (proc.stderr or "")


N_RE = re.compile(r"allowed-tools surfaces (?:documented|backed) (\d+) of "
                   r"(\d+)\s*$")
GEN_RE = re.compile(r"(?:generator world|script-only world): (\d+) of "
                    r"(\d+)\s*$")
OTHER_RE = re.compile(r"^(held at base:.*|province surfaces named.*|registry "
                      r"home.*|opened this round.*|measured-rev:.*|semantic "
                      r"rider:.*)$")
BULLETS_RE = re.compile(r"^(\d+) ## Core bullet\(s\) name the entry")


def parse_output(out: str) -> dict:
    """Read the counter's own printed lines.

    ``r80_exit`` is the ROUND-80 frozen predicate read off those lines: exit 0
    iff N == 6 and the tree conjuncts hold, exit 2 when the counter could
    not evaluate at all, else exit 1.  It is computed here rather than taken
    from the counter's own status, because the counter under test may still
    carry the round-79 exit rule (TARGET >= 5 and a generator-world gate);
    the control suite judges the ROUND-80 predicate in both cases and
    reports the counter's own status beside it.
    """
    res = {"n": None, "of": None, "gen": None, "other": [], "findings": [],
           "error": None, "rule_ok": False, "home_ok": False, "bullets": 1,
           "headline": None, "r80_exit": None}
    for line in out.splitlines():
        bare = line.rstrip()
        if bare != bare.lstrip():          # indented: a finding
            stripped = bare.strip()
            if stripped:
                res["findings"].append(stripped)
            m = BULLETS_RE.match(stripped)
            if m:
                res["bullets"] = int(m.group(1))
            continue
        m = N_RE.match(bare)
        if m and res["n"] is None:
            res["n"], res["of"] = int(m.group(1)), int(m.group(2))
            res["headline"] = bare
            continue
        m = GEN_RE.match(bare)
        if m and res["gen"] is None:
            res["gen"] = f"{int(m.group(1))} of {int(m.group(2))}"
            continue
        if bare == "skill rule line ok":
            res["rule_ok"] = True
            continue
        if bare == "registry home ok":
            res["home_ok"] = True
            continue
        m = OTHER_RE.match(bare)
        if m:
            res["other"].append(bare)
            continue
        if bare.startswith("environment error"):
            res["error"] = bare
    if res["error"] is not None:
        res["r80_exit"] = 2
    elif res["n"] is None:
        res["r80_exit"] = 2          # no verdict line: could not evaluate
    else:
        tree_ok = res["rule_ok"] and res["home_ok"] and res["bullets"] == 1
        res["r80_exit"] = 0 if (res["n"] == 6 and tree_ok) else 1
    return res


# ----------------------------------------------- pre-registered expectations
# Fixed BEFORE the first measurement and printed by --list.  No count had
# been observed when this table was fixed: the only runs so far read
# "environment error: counter drifted" (the published counter bytes were
# unfrozen), which is a status, not a count.
#
# The counts are stated RELATIVE to the baseline (the C4 world: the honest
# form, mechanically emitted), because a defect that removes one surface from
# the BASELINE would otherwise cascade into every control and make the suite
# unreadable.  `lost` is the number of surfaces the control is designed to
# remove from the baseline; the expected count is baseline - lost.  The
# baseline itself is stated as the PLAN's expectation (6 of 6) in the C4 row.
# `exit_in` is the round-80 frozen predicate's exit (exit 0 iff N == 6 and the
# tree conjuncts hold) read off the counter's own printed lines.
#
# The absolute plan-expectation for every world is also stated, so a reader
# can see the plan's own number next to the relative one.
EXPECT: dict[str, dict] = {
    "C0": dict(lost=None, n_abs=(0,), exit_in=(1,), what="base copy: the "
              "base tree, unmodified (no entry, no manifest, no registry "
              "change)",
              defect="N >= 1, or exit 0"),
    "C1": dict(lost=None, n_abs=(0, None), exit_in=(1, 2), what="token dump: "
              "every token and label named, no snapshot bytes and no manifest",
              defect="N >= 1, or exit 0 (a surface credited without bytes)"),
    "C2": dict(lost="all", n_abs=(0,), exit_in=(1,), what="wrong-page real text: "
              "every row's located quote is another surface's page text",
              defect="N >= 1, or exit 0"),
    "C3": dict(lost="all", n_abs=(0,), exit_in=(1,), what="shared-banner quote: "
              "one identical banner line in all six snapshots, quoted by every "
              "row",
              defect="N >= 1 (a shared banner accepted as a located quote)"),
    "C4": dict(lost=None, n_abs=(6,), exit_in=(0,), what="the INDEPENDENT "
              "mechanical generator: form emitted from the committed "
              "snapshots with no judgement, scored on the same counter",
              defect="NOT a defect: the round-80 headline is form-level, so a "
                     "mechanical reach is expected; N <= 5 is a finding about "
                     "the generator or the counter's reading, never a reason "
                     "to narrow the world"),
    "C4b": dict(lost=None, n_abs=(0,), exit_in=(1,), what="diagnostic: the "
               "same world with the registry anchors in the corpus's own "
               "fetch-record format instead of the counter's grammar",
               defect="N >= 1 (the counter read an anchor the corpus "
                      "actually commits)"),
    "C5": dict(lost="all", n_abs=(0,), exit_in=(1,), what="label-only: grant "
              "labels and page tokens, no located quote anywhere",
              defect="N >= 1, or exit 0"),
    "C6": dict(lost=1, n_abs=(5,), exit_in=(1,), what="sibling host: pi's "
              "row cites `…/badlogic/pi-mono-evil/…`, a string prefix of the "
              "frozen pin",
              defect="the host prefix accepted (pi keeps its surface)"),
    "C7": dict(lost=None, n_abs=(None,), exit_in=(1, 2), what="stale "
              "snapshot: pi's committed bytes changed after the pin was "
              "written",
              defect="exit 0, or a count line claiming a full count from bytes "
                     "that do not hash to their pin"),
    "C7b": dict(lost=1, n_abs=(5,), exit_in=(1,), what="wrong sha pin: pi's "
               "registry anchor carries a digest the snapshot does not have",
               defect="pi keeps its surface (the wrong pin was accepted)"),
    "C8": dict(lost=None, n_abs=(0,), exit_in=(1,), what="first-answer "
              "baseline: no entry file; 6 of 6 asserted in prose only",
              defect="N >= 1, or exit 0"),
    "H0": dict(lost=None, n_abs=(0, 1, 2, 3, 4, 5, 6), exit_in=(1,),
               what="plumbing oracle: the honest world carrying each "
                    "surface's CORPUS-recorded located quote verbatim",
               defect="the corpus's own quotes back all six surfaces, or the "
                      "baseline moves"),
    "S05": dict(lost=None, n_abs=(0, 1, 2, 3, 4, 5, 6), exit_in=(0, 1),
                what="the DECISIVE arm: the registry is the corpus edit "
                     "seat's published corpus/SOURCES.md verbatim (the six C2 "
                     "rows exactly as the L1 would land them), everything else "
                     "the honest mechanical world",
                defect="the landed corpus rows read 6 of 6 (the entry and the "
                       "rows are consistent)"),
    "S05b": dict(lost=None, n_abs=(0, 1, 2, 3, 4, 5, 6), exit_in=(0, 1),
                 what="the ISOLATION arm: the corpus edit seat's published "
                      "rows with ONLY the anchor's fetch-record rendering "
                      "normalised to the counter's grammar",
                 defect="the landed rows read 6 of 6 once the anchor grammar "
                        "matches"),
    "G0": dict(lost=None, n_abs=(0, 1, 2, 3, 4, 5, 6), exit_in=(0, 1),
               what="generator isolation: the honest world with a registry "
                    "carrying only the six C2 rows, so the counter's OWN "
                    "generator world can find and score them",
               defect="the counter's generator world cannot be scored at all"),
}
ORDER_WORLDS = ["C0", "C1", "C2", "C3", "C4", "C4b", "C5", "C6", "C7", "C7b",
                "C8", "H0", "G0", "S05", "S05b"]


# ---------------------------------------------------------------- self-check
def self_check(pages: dict[str, bytes], quotes: dict[str, str],
               value_tokens: dict[str, str | None]) -> list[str]:
    """Fixture invariants, checked before any world is built.

    Not a counter check: this is the generator's own arithmetic — every
    scraped quote is 5-25 words, occurs in its own page's text view, carries
    ``allowed-tools`` word-bounded, carries the surface's page token, occurs
    in no other page's text view (Q70), and the frozen keyword rule
    reproduces the frozen grant label.
    """
    errs: list[str] = []
    views = {k: " ".join(text_view(BY_KEY[k]["snap"],
                                  pages[k].decode("utf-8", "replace")))
             for k in ORDER}
    for k in ORDER:
        s = BY_KEY[k]
        q = quotes[k]
        words = len(q.split())
        if not MIN_QUOTE_WORDS <= words <= MAX_QUOTE_WORDS:
            errs.append(f"{s['sid']}: scraped quote is {words} words "
                        f"(want {MIN_QUOTE_WORDS}-{MAX_QUOTE_WORDS})")
        if q not in views[k]:
            errs.append(f"{s['sid']}: scraped quote is not in its page's text "
                        f"view")
        if not word_bounded("allowed-tools", q):
            errs.append(f"{s['sid']}: scraped quote lacks `allowed-tools`")
        if not word_bounded_ci(s["page_token"], q):
            errs.append(f"{s['sid']}: scraped quote lacks its page token "
                        f"{s['page_token']!r}")
        for other, view in views.items():
            if other != k and q in view:
                errs.append(f"{s['sid']}: scraped quote also occurs in "
                            f"{other}'s text view (Q70)")
        if label_for_quote(q) != s["grant"]:
            errs.append(f"{s['sid']}: the frozen keyword rule yields "
                        f"{label_for_quote(q)!r}, the frozen label is "
                        f"{s['grant']!r}")
        val = value_tokens.get(k)
        if not val:
            errs.append(f"{s['sid']}: no value-form token derived")
        elif not word_bounded(val, views[k]):
            errs.append(f"{s['sid']}: the value token {val!r} does not occur "
                        f"word-bounded in the page")
    return errs


# -------------------------------------------------------------------- driver
def compare(name: str, code: int, parsed: dict,
            baseline: int | None) -> tuple[bool, str]:
    """Compare the observation with the pre-registration.

    The verdict is computed on the ROUND-80 frozen predicate (exit 0 iff
    N == 6 and the tree conjuncts hold), read off the counter's own printed
    lines — not on the counter's own status, which may still carry the
    round-79 exit rule.  The counter's own status is reported beside the
    verdict so a divergence is attributable.

    The expected count is baseline-relative where the table says so: the
    world is designed to remove `lost` surfaces from the baseline (the C4
    world), so the expected count is baseline - lost.  The baseline is the
    C4 world's own count, measured in the same run.
    """
    exp = EXPECT[name]
    n = parsed["n"]
    r80 = parsed["r80_exit"]
    lost = exp.get("lost")
    n_set = exp["n_abs"]
    ok_n = n in n_set
    ok_exit = r80 in exp["exit_in"]
    ok = ok_n and ok_exit
    bits = []
    if not ok_n:
        bits.append(f"N={n!r} (pre-registered {n_set}"
                     + (f"; the control designs to lose {lost}"
                        if lost not in (None,) else "")
                     + (f"; measured baseline {baseline} of {6}"
                        if baseline is not None else ""))
    if not ok_exit:
        bits.append(f"round-80 exit {r80} (pre-registered {exp['exit_in']})")
    return ok, ("as-expected" if ok else "DIVERGES: " + "; ".join(bits))


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(
        description="C2 control worlds for kotoba round 80 (plan § C2)")
    ap.add_argument("--counter", required=False,
                    help="the counter file to run, verbatim")
    ap.add_argument("--base-tree", default=str(LANE),
                    help="lane clone whose object store supplies the base "
                         "lineage and the committed snapshots (read-only)")
    ap.add_argument("--base-rev", default=DEFAULT_BASE_REV,
                    help="base revision the worlds are built on")
    ap.add_argument("--work", default=None,
                    help="scratch dir for the worlds (default: mktemp -d "
                         "under $TMPDIR)")
    ap.add_argument("--only", default=None,
                    help="comma-separated world names, e.g. C3,C6")
    ap.add_argument("--keep", action="store_true", help="keep world repos")
    ap.add_argument("--verbose", action="store_true")
    ap.add_argument("--list", action="store_true",
                    help="print the pre-registered expectation table and exit")
    ap.add_argument("--json", action="store_true", help="machine summary")
    ap.add_argument("--out", default=None, help="receipt file for the full log")
    ap.add_argument("--timeout", type=int, default=300,
                    help="per-counter-run timeout (s)")
    args = ap.parse_args(argv)

    if args.list:
        print("world  expected N  expected exit  what it breaks")
        for name in ORDER_WORLDS:
            e = EXPECT[name]
            print(f"{name:<6} {e['n_in']!s:<11} {e['exit_in']!s:<14} "
                  f"{e['what']}")
            print(f"       defect signature: {e['defect']}")
        return 0

    if not args.counter:
        print("environment: --counter is required (the round-80 C2 counter "
              "file)", file=sys.stderr)
        return 2
    counter_path = Path(args.counter)
    if not counter_path.is_file():
        print(f"environment: counter {counter_path} is not a file",
              file=sys.stderr)
        return 2
    counter = Counter(counter_path.resolve())

    base = Path(args.base_tree)
    if not base.is_dir():
        print(f"environment: base tree {base} is not a directory",
              file=sys.stderr)
        return 2
    base = base.resolve()
    proc = git(base, ["rev-parse", "--verify", "-q",
                      f"{args.base_rev}^{{commit}}"], check=False)
    if proc.returncode != 0:
        print(f"environment: {args.base_rev} is not a commit in {base}",
              file=sys.stderr)
        return 2
    base_rev = proc.stdout.decode().strip()

    # the six committed snapshots (bytes from the base tree)
    pages: dict[str, bytes] = {}
    for k in ORDER:
        s = BY_KEY[k]
        data = base_blob(base, base_rev, f"{BASE_SNAPDIR}/{s['snap']}")
        if data is None:
            print(f"environment: snapshot {BASE_SNAPDIR}/{s['snap']} is "
                  f"absent at {base_rev}", file=sys.stderr)
            return 2
        pages[k] = data

    base_text = {
        "sources": (base_blob(base, base_rev, "corpus/SOURCES.md") or b""
                    ).decode("utf-8", "replace"),
        "skill": (base_blob(base, base_rev, "SKILL.md") or b""
                  ).decode("utf-8", "replace"),
        "province": (base_blob(base, base_rev, "PROVINCE.md") or b""
                     ).decode("utf-8", "replace"),
    }
    base_rows = base_registry_rows(base, base_rev)

    work = Path(args.work) if args.work else Path(tempfile.mkdtemp(
        prefix="c2r80-", dir=os.environ.get("TMPDIR")))
    work.mkdir(parents=True, exist_ok=True)

    # The corpus edit seat's published corpus/SOURCES.md (applied to the base
    # tree in a scratch clone): the rows the L1 would land.  Read-only: the
    # patch is applied in a THROWAWAY clone under --work.
    s05_text = ""
    s05_patch = Path("/home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/"
                     "round-80/build/Kb80S05SourcesEdits.patch")
    if s05_patch.is_file():
        try:
            tmp = Path(tempfile.mkdtemp(prefix="s05-", dir=str(work)))
            subprocess.run(["git", "clone", "-q", "--shared", str(base),
                            str(tmp / "c")], check=True, capture_output=True)
            subprocess.run(["git", "-C", str(tmp / "c"), "checkout", "-q",
                            base_rev], check=True, capture_output=True)
            subprocess.run(["git", "-C", str(tmp / "c"), "apply", "-q",
                            str(s05_patch)], check=True, capture_output=True)
            # git apply changes the WORKTREE; stage it and read the index
            subprocess.run(["git", "-C", str(tmp / "c"), "add", "-A"],
                           check=True, capture_output=True)
            got = subprocess.run(["git", "-C", str(tmp / "c"), "show",
                                  ":corpus/SOURCES.md"],
                                 capture_output=True)
            if got.returncode == 0:
                s05_text = got.stdout.decode("utf-8", "replace")
        except Exception:
            s05_text = ""

    _entry, quotes = mechanical_entry(pages, counter, counter.capture)
    value_tokens = {k: value_token(quotes[k], BY_KEY[k]["page_token"])
                    for k in ORDER}
    errs = self_check(pages, quotes, value_tokens)
    if errs:
        print("generator self-check FAILED (fixtures, not the counter):",
              file=sys.stderr)
        for e in errs:
            print("  " + e, file=sys.stderr)
        return 2

    counter_bytes = counter.path.read_bytes()

    names = [n.strip() for n in args.only.split(",")] if args.only \
        else ORDER_WORLDS
    unknown = [n for n in names if n not in EXPECT]
    if unknown:
        print(f"environment: unknown world(s) {unknown}", file=sys.stderr)
        return 2

    log: list[str] = []
    summary: list[dict] = []

    def say(line: str = "") -> None:
        print(line)
        log.append(line)

    say(f"c2_controls: counter={counter.path}")
    say(f"c2_controls: counter sha256={counter.sha256}")
    say(f"c2_controls: counter constants: ENTRY={counter.entry} "
        f"SNAPDIR={counter.snapdir} MANIFEST={counter.manifest} "
        f"CAPTURE={counter.capture} TARGET={counter.target}")
    say(f"c2_controls: base-tree={base} base-rev={base_rev}")
    say(f"c2_controls: work={work}  worlds={','.join(names)}")
    say("")

    # The per-surface admissibility table: for each surface, how many of the
    # page's own 5..25-word windows carrying BOTH the key token and the
    # surface's frozen page token the counter's own Q70 rule accepts.  A
    # surface with zero admissible windows cannot be documented by ANY entry,
    # however the entry is written — the reading is structural, not a defect
    # of the entry.
    say("c2_controls: per-surface admissibility — every 5..25-word window of "
        "the committed page carrying BOTH the key token and the surface's "
        "frozen page token, scored with the COUNTER'S OWN quote_location")
    for key in ORDER:
        s = BY_KEY[key]
        view = text_view(s["snap"], pages[key].decode("utf-8", "replace"))
        first_head = next((i for i, l in enumerate(view)
                           if l.startswith("#")), None)
        words = " ".join(view).split()
        n_cand = n_ok = 0
        example = None
        reason = ""
        for i in range(len(words)):
            if not word_bounded("allowed-tools", words[i]):
                continue
            for j in range(i, min(len(words), i + MAX_QUOTE_WORDS)):
                cand = " ".join(words[i:j + 1])
                if len(cand.split()) < MIN_QUOTE_WORDS:
                    continue
                if not word_bounded_ci(s["page_token"], cand):
                    continue
                n_cand += 1
                ok, why = counter.mod.quote_location(view, cand)
                if ok:
                    n_ok += 1
                    if example is None:
                        example = cand
                elif not reason:
                    reason = why
        say(f"    {key:8} {s['sid']} candidates={n_cand} admissible={n_ok}"
            + (f"  first='#'-line {first_head} "
               f"{view[first_head][:46]!r}" if first_head is not None
               else "  first='#'-line none")
            + (f"  e.g. {example[:64]!r}" if example else "")
            + (f"  refusal: {reason!r}" if not n_ok and reason else ""))
    say("")

    failures = 0
    baseline: int | None = None
    measured: dict[str, dict] = {}

    # The baseline is the C4 world's own count, measured FIRST in this run so
    # the relative expectations of the other worlds have a number to refer
    # to.  It is the honest form world (the mechanical generator over the
    # committed snapshots), so it is the same world C4 measures.
    if "C4" in names and EXPECT["C4"]["lost"] == 0:
        say("=== C4 (baseline) === measuring the baseline first")
        files, notes, rev_sel = world_files("C4", counter, pages, base_rows,
                                            base_text, s05_text)
        world: Path | None = None
        try:
            world, commit = build_world(work, base, base_rev, files,
                                        counter_bytes, counter.counter_path,
                                        "C4base")
            rev = base_rev if rev_sel is None else commit
            code, out = run_counter(counter, world, rev, args.timeout)
            parsed = parse_output(out)
            baseline = parsed["n"]
            measured["C4"] = parsed
            say(f"    world-rev: {rev}")
            say(f"    allowed-tools surfaces documented {parsed['n']} of "
                f"{parsed['of']}")
            say(f"    generator world: {parsed['gen'] or '(none)'}")
            say(f"    round-80 predicate exit: {parsed['r80_exit']}")
            say("")
        finally:
            if world is not None and not args.keep:
                shutil.rmtree(world, ignore_errors=True)
        say(f"c2_controls: baseline (C4) = {baseline} of {counter.total}")
        say("")

    for name in names:
        files, notes, rev_sel = world_files(name, counter, pages, base_rows,
                                            base_text, s05_text)
        world: Path | None = None
        try:
            try:
                world, commit = build_world(work, base, base_rev, files,
                                            counter_bytes,
                                            counter.counter_path, name)
            except (GitError, OSError) as exc:
                say(f"=== {name} === BUILD FAILED: {exc}")
                summary.append(dict(world=name, build="failed", error=str(exc)))
                failures += 1
                continue
            rev = base_rev if rev_sel is None else commit
            try:
                code, out = run_counter(counter, world, rev, args.timeout)
            except subprocess.TimeoutExpired:
                say(f"=== {name} === COUNTER TIMEOUT after {args.timeout}s")
                summary.append(dict(world=name, world_dir=str(world),
                                    rev=rev, timeout=True))
                failures += 1
                continue
            parsed = parse_output(out)
            if parsed["n"] is not None:
                n_line = (f"allowed-tools surfaces documented {parsed['n']} "
                          f"of {parsed['of']}")
            else:
                n_line = "(no count line printed)"
            ok, verdict = compare(name, code, parsed, baseline)
            if not ok:
                failures += 1
            say(f"=== {name} === {EXPECT[name]['what']}")
            say(f"    world-rev: {rev}")
            say(f"    {n_line}")
            gen_line = parsed["gen"] or "(no generator-world line printed)"
            say(f"    generator world: {gen_line}")
            for o in parsed["other"]:
                say(f"    {o}")
            if parsed["error"]:
                say(f"    {parsed['error']}")
            for f in parsed["findings"]:
                if name in ("C4", "C4b") or args.verbose or not ok:
                    say(f"    finding: {f}")
            say(f"    counter exit (the counter's own status): {code}")
            say(f"    round-80 predicate exit (N == 6 and the tree "
                f"conjuncts): {parsed['r80_exit']}")
            say(f"    pre-registered: N in {EXPECT[name]['n_abs']} "
                f"(design: lost={EXPECT[name]['lost']}) round-80 "
                f"exit in {EXPECT[name]['exit_in']} — {verdict}")
            say(f"    defect signature: {EXPECT[name]['defect']}")
            for note in notes:
                say(f"    note: {note}")
            if args.verbose or not ok:
                say("    --- counter output ---")
                for line in out.rstrip("\n").splitlines():
                    say("    | " + line)
                say("    --- end ---")
            say("")
            summary.append(dict(world=name, world_dir=str(world), rev=rev,
                                exit=code, n=parsed["n"], of=parsed["of"],
                                generator=parsed["gen"], other=parsed["other"],
                                error=parsed["error"], verdict=verdict,
                                as_expected=ok, notes=notes))
        finally:
            if world is not None and not args.keep:
                shutil.rmtree(world, ignore_errors=True)

    say(f"c2_controls: {len(names)} world(s), {failures} divergence(s); "
        f"pre-registration is evidence, the L1 judges")
    if not args.keep and not args.only:
        try:
            work.rmdir()
        except OSError:
            pass

    if args.json:
        print(json.dumps(dict(counter=str(counter.path),
                              counter_sha256=counter.sha256,
                              base=str(base), base_rev=base_rev,
                              worlds=summary), indent=1))
    if args.out:
        Path(args.out).write_text("\n".join(log) + "\n")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
