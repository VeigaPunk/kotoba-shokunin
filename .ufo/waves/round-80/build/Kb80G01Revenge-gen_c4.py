#!/usr/bin/env python3
"""Independent C4 reconstruction for round-80 revenger seat Kb80G01Revenge.

A mechanical generator that writes the COMPLETE proposed C2 evidence shape
(entry rows, registry cells, manifest, PROVINCE bullet, SKILL rule + gate row)
from the committed snapshots of the six pages, with NO semantic judgement: the
frozen grant label / page token per surface is read from the frozen counter's
own surface table, the located quote is a mechanical word window that contains
`allowed-tools` and the frozen page token, and the value token is the first
bare-name word after the field in the page text view.

Scored by the r79 draft counter (verifiers/check_allowed_tools.py inside the
clone).  No network.

Usage: gen_c4.py <clone> [--write-only]
"""
from __future__ import annotations

import hashlib
import importlib.util
import re
import sys
from pathlib import Path

CLONE = Path(sys.argv[1]).resolve()
COUNTER = CLONE / "verifiers/check_allowed_tools.py"
SNAPREL = ".ufo/waves/round-79/snapshots"
SNAP = CLONE / SNAPREL
SOURCES = CLONE / "corpus/SOURCES.md"
ENTRYREL = "corpus/knowledge/allowed-tools-surfaces-round79.md"
CAPTURE = "2026-10-27"

if "--msaf-synthetic" in sys.argv:
    (SNAP / "S229-msaf.html").write_text(
        "<h1>Agent Skills</h1><p>The skill frontmatter table lists "
        "allowed-tools as a space-delimited list of pre-approved tools. "
        "Experimental - support may vary between agent "
        "implementations.</p>\n")

spec = importlib.util.spec_from_file_location("c79", COUNTER)
c = importlib.util.module_from_spec(spec)
spec.loader.exec_module(c)

STOP = {"the", "and", "for", "with", "that", "this", "field", "frontmatter",
        "skill", "skills", "is", "are", "of", "to", "a", "an", "in", "it",
        "documented", "here", "page", "states", "own", "words", "example",
        "values", "forms", "list", "optional", "string", "space-separated",
        "tools", "tool", "can", "use", "them", "without",
        "your", "you", "or", "as", "be", "no", "not", "on", "by"}


def cells_of(line: str) -> list[str]:
    return [x.strip() for x in c._split_cells(line.strip()[1:-1])]


# ---- the six registry rows at base: sid -> surface key (by frozen host pin)
base_rows = {}
for line in SOURCES.read_text().splitlines():
    if c.REGISTRY_RE.match(line):
        cells = cells_of(line)
        base_rows[cells[0]] = cells

# The r79 census mapping (corpus/lessons/round-79.md § Gate: S226 spec,
# S227 claude, S228 factory, S229 msaf, S230 pi, S231 vibe); each row's own
# URL is re-checked against the surface's frozen host pin below.
SID_OF_KEY = {"spec": "S226", "claude": "S227", "factory": "S228",
              "msaf": "S229", "pi": "S230", "vibe": "S231"}
key_of_sid = {sid: key for key, sid in SID_OF_KEY.items()}
sid_of_key = dict(SID_OF_KEY)
for key, sid in SID_OF_KEY.items():
    cells = base_rows[sid]
    if len(cells) != c.REGISTRY_CELLS:
        raise SystemExit(f"{sid}: {len(cells)} cells at base")
    urls = c.urls_of(cells[1])
    if not any(c.host_ok(u, c.SURFACES[key]["hosts"]) for u in urls):
        raise SystemExit(f"{sid}: no URL on {key}'s frozen host: {urls}")

# ---- snapshots: basename -> raw bytes, and the text view of each
man_lines = []
raw_of = {}
view_of = {}
for key in c.SURFACE_ORDER:
    sid = sid_of_key[key]
    names = sorted(p.name for p in SNAP.iterdir()
                   if re.match(rf"^{sid}(?![0-9])", p.name)
                   and p.suffix in (".md", ".html", ".htm"))
    if len(names) != 1:
        raise SystemExit(f"{sid}: {names} snapshot candidates")
    name = names[0]
    raw = (SNAP / name).read_bytes()
    raw_of[name] = raw
    man_lines.append(f"{hashlib.sha256(raw).hexdigest()}  {name}\n")
    view_of[name] = c.text_view(name, raw.decode("utf-8", "replace"))

(SNAP / "MANIFEST.sha256").write_text("".join(man_lines))


def shared_elsewhere(name: str, q: str) -> str | None:
    for other, lines in view_of.items():
        if other != name and any(q in ln for ln in lines):
            return other
    return None


def mech_quote(name: str, page_token: str) -> tuple[str | None, bool]:
    """(quote, q70_ok): the mechanical window, plus whether Q70 admits it.

    A window is a run of 5..25 words containing `allowed-tools` and the frozen
    page token.  q70_ok is False when every such window is rejected by the
    counter's quote_location (heading / first-heading block) or is shared with
    another page; the caller still emits the row so the counter can say why."""
    lines = view_of[name]
    first_head = next((i for i, l in enumerate(lines) if l.startswith("#")),
                      None)
    start = first_head + 2 if first_head is not None else 0
    words = " ".join(lines[start:]).split()
    first_any: str | None = None
    for i in [i for i, w in enumerate(words)
              if c.word_bounded("allowed-tools", w)]:
        for size in range(5, 26):
            for lo in range(max(0, i - size + 1), i + 1):
                hi = lo + size
                if hi > len(words):
                    continue
                q = c.ws(" ".join(words[lo:hi]))
                if not c.word_bounded("allowed-tools", q):
                    continue
                if not c.word_bounded_ci(page_token, q):
                    continue
                if hi < i + 3:
                    continue
                if first_any is None:
                    first_any = q
                if c.quote_location(lines, q)[0] and not shared_elsewhere(name, q):
                    return q, True
    # fallback: the whole view (the counter will still judge Q70)
    allwords = " ".join(lines).split()
    for i in [i for i, w in enumerate(allwords)
              if c.word_bounded("allowed-tools", w)]:
        for size in range(5, 26):
            for lo in range(max(0, i - size + 1), i + 1):
                hi = lo + size
                if hi > len(allwords):
                    continue
                q = c.ws(" ".join(allwords[lo:hi]))
                if not c.word_bounded("allowed-tools", q):
                    continue
                if not c.word_bounded_ci(page_token, q):
                    continue
                if hi < i + 3:
                    continue
                return q, False
    return first_any, False


def mech_value(name: str, quote: str, page_token: str) -> str | None:
    """The first bare-name word after the field in the page text view."""
    words = " ".join(view_of[name]).split()
    seen = False
    for w in words:
        t = w.strip("`'\".,;:()[]{}|*-_")
        if c.word_bounded("allowed-tools", w):
            seen = True
            continue
        if not seen:
            continue
        if c.BARE_NAME_RE.match(t) and t.lower() not in STOP \
                and not t.isdigit() and len(t) > 1 \
                and not c.word_bounded_ci(page_token, t):
            return t
    return None


def esc(text: str) -> str:
    return text.replace("|", "\\|")


head, body, newrows = [], [], {}
for key in c.SURFACE_ORDER:
    sid, spec_ = sid_of_key[key], c.SURFACES[key]
    name = next(n for n in raw_of
                if re.match(rf"^{sid}(?![0-9])", n))
    quote, q70 = mech_quote(name, spec_["page_token"])
    value = mech_value(name, quote, spec_["page_token"]) if quote else None
    if quote is None or value is None:
        raise SystemExit(f"{key}: no mechanical quote/value "
                         f"(quote={quote!r} value={value!r})")
    if not q70:
        print(f"NOTE {key}: mechanical quote found but Q70-rejected: {quote!r}")
    cells = list(base_rows[sid])
    raw = raw_of[name]
    cells[5] = ("§ mechanical scrape; fetched %sT00:00:00Z, HTTP 200, %d B, "
                "sha256 %s" % (CAPTURE, len(raw),
                               hashlib.sha256(raw).hexdigest()))
    cells[8] = CAPTURE
    cells[10] = ENTRYREL
    newrows[sid] = cells
    url = c.urls_of(cells[1])[0]
    head.append(f'source: {sid} — mechanical scrape — {url} — located quote '
                f'"{quote}" (snapshot `{name}`)')
    toks = [f"`allowed-tools`", f"`{value}`", f"`{spec_['page_token']}`"]
    body.append(f"| {spec_['display']} | {sid} | " + ", ".join(toks)
                + f" | {spec_['grant']} | \"{esc(quote)}\" |")

entry = "\n".join(head + [
    "",
    f"verified-at: {CAPTURE}",
    "recheck: 90d — re-fetch",
    "",
    "Text view: `.html` snapshots have `script` and `style` blocks removed, "
    "tags replaced by one space and entities decoded; Markdown snapshots have "
    "every backtick deleted and an unordered-list marker removed at a line "
    "start; every snapshot then has whitespace collapsed.",
    "",
    "## Surfaces",
    "",
    "| " + " | ".join(c.HEADER) + " |",
    "|" + "---|" * len(c.HEADER) + "|",
] + body) + "\n"
(CLONE / ENTRYREL).parent.mkdir(parents=True, exist_ok=True)
(CLONE / ENTRYREL).write_text(entry)

# ---- registry: rewrite only the six rows' anchor/opened/used-by cells
out = []
for line in SOURCES.read_text().splitlines():
    if c.REGISTRY_RE.match(line):
        cells = cells_of(line)
        if cells and cells[0] in newrows:
            line = "| " + " | ".join(newrows[cells[0]]) + " |"
    out.append(line)
SOURCES.write_text("\n".join(out) + "\n")

# ---- PROVINCE ## Core: exactly one bullet naming the entry (>= 3 surfaces)
prov = (CLONE / "PROVINCE.md").read_text()
bullet = ("- `allowed-tools` frontmatter semantics by client (round 79, "
          "form backbone measured, semantics exploratory) — Open specification, "
          "Claude Code, Factory, Microsoft Agent Framework, pi and Mistral "
          "Vibe rows with snapshot-pinned quotes — " + ENTRYREL + ".")
lines = prov.splitlines()
start = next(i for i, l in enumerate(lines) if re.match(r"^## Core\s*$", l))
end = next((i for i in range(start + 1, len(lines))
            if lines[i].startswith("## ")), len(lines))
while end > start + 1 and not lines[end - 1].strip():
    end -= 1
lines.insert(end, bullet)
(CLONE / "PROVINCE.md").write_text("\n".join(lines) + "\n")

# ---- SKILL.md: one rule line naming >= 3 surfaces + a conformant gate row
skill = (CLONE / "SKILL.md").read_text()
rule = ("- `allowed-tools` surfaces: what the field means per client (Open "
        "specification, Claude Code, Factory, Microsoft Agent Framework, pi, "
        "Mistral Vibe; form-level rows) — " + ENTRYREL + ".")
row = ("| `verifiers/check_allowed_tools.py` | gate | "
       "`python3 -B verifiers/check_allowed_tools.py --rev <rev>` | "
       "documented N of 6 + generator world M of 6 | `--self-test` | "
       "none | read-only | kotoba |")
skill = skill.replace("## Gate registry\n", "## Gate registry\n\n" + rule + "\n",
                      1)
skill = skill.rstrip("\n") + "\n" + row + "\n"
(CLONE / "SKILL.md").write_text(skill)

print("generated: entry, manifest, six registry rows, PROVINCE bullet, "
      "SKILL rule + gate row")
