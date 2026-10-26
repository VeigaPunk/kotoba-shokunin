#!/usr/bin/env python3
"""probe_c1_predicate.py -- critic probe (seat CriticClaimsR74, round 74 wave 1).

This is NOT the lane's counter and is not proposed as one.  It is the seat's
literal reading of the frozen C1 predicate in `plans/round-74.md`, used to walk
cheap worlds conjunct by conjunct before `verifiers/check_spec_craft.py`
exists.  Every implementation choice that the plan leaves open is named below;
where a different choice would change the outcome the seat says so in the
report.

Frozen predicate (quoted from the plan):

    python3 -B verifiers/check_spec_craft.py --rev <rev>
        -> prints "spec craft pages backed N of 3", exit 0 when N == 3

  (a) entry `corpus/knowledge/spec-skill-creation-craft-round74.md` opens with
      `source:` lines for every cited id, then `verified-at:` and `recheck:`,
      and has exactly one row for P in its rule table carrying >= 2 rule
      tokens (backticked commands or paths, or double-quoted rule sentences of
      at least five words), each located word-bounded in the committed
      snapshot of P's source;
  (b) P's cited S### is an 11-cell registry row, status mined, tier A, host
      agentskills.io, opened equal to a round-74 date, used-by naming the
      entry, and the registry is census-conformant at --rev (conformance is
      the lane's census gate, not modelled here);
  (c) P's snapshot under .ufo/waves/round-74/snapshots/ has a sha256 equal to
      the pin in snapshots/MANIFEST.sha256 (missing/tampered -> exit 2);
  (d) the row's located quote (5-25 words) is found in P's snapshot after
      whitespace collapse only;
  (e) SKILL.md subsection `### Body craft - the specification's skill-creation
      guides` has >= 2 table rows citing P's S###, each with an action cell of
      >= 5 words and >= 1 rule token that occurs in P's snapshot;
  (f) PROVINCE.md section Core names the entry.

Seat's open-question choices:
  * "word-bounded" -> lookarounds `(?<![\\w-])tok(?![\\w-])`, because `\\b`
    misses `.agents/skills/`, `--dry-run`, `theme={null}` and
    `uvx ruff@0.8.0 check .` (measured; see the report).
  * "rule token" -> a backticked span of any length, or a double-quoted span
    of >= 5 words.  The plan's parenthetical ("backticked commands or
    paths") cannot be type-checked mechanically, so any backticked span counts;
    the seat records the consequence (a field name or `theme={null}` counts).
  * "the row's located quote" -> the first double-quoted span in the row.
  * registry "host" -> the URL cell contains `agentskills.io`; the plan does
    not require the URL to name P (this is deliberate; the seat attacks it).
  * "round-74 date" -> 2026-10-25 (the lane's `date -I` at round start).

Usage: python3 -B probe_c1_predicate.py build <worldsdir> <snapshotsdir>
       python3 -B probe_c1_predicate.py check <worldsdir>
Reads the seat's own fetched snapshots; writes only under <worldsdir>.
"""
import hashlib
import pathlib
import re
import sys

PAGES = ("best-practices", "using-scripts", "quickstart")
ENTRY = "corpus/knowledge/spec-skill-creation-craft-round74.md"
ENTRY_NAME = "spec-skill-creation-craft-round74.md"
ROUND74_DATE = "2026-10-25"
SUBSECTION = "### Body craft \u2014 the specification's skill-creation guides"
BACKTICK = re.compile(r"`([^`]+)`")
DOUBLEQ = re.compile(r'"([^"]+)"')
REGISTRY_COLUMNS = 11
CELL_SPLIT = re.compile(r"(?<!\\)\|")


def collapse(text):
    return re.sub(r"\s+", " ", text).strip()


def word_bounded(tok, text):
    return re.search(r"(?<![\w-])" + re.escape(tok) + r"(?![\w-])", text) is not None


def tokens_of(cell):
    out = []
    for m in BACKTICK.finditer(cell):
        out.append(m.group(1).strip())
    for m in DOUBLEQ.finditer(cell):
        s = collapse(m.group(1))
        if len(s.split()) >= 5:
            out.append(s)
    seen, uniq = set(), []
    for t in out:
        if t and t not in seen:
            seen.add(t)
            uniq.append(t)
    return uniq


def quote_of(cell):
    m = DOUBLEQ.search(cell)
    return collapse(m.group(1)) if m else ""


def split_row(line):
    s = line.strip()
    if s.startswith("|"):
        s = s[1:]
    if s.endswith("|") and not s.endswith("\\|"):
        s = s[:-1]
    return [c.replace("\\|", "|").strip() for c in CELL_SPLIT.split(s)]


def tables(text):
    blocks, current = [], []
    for line in text.splitlines():
        if line.strip().startswith("|"):
            current.append(line)
        elif current:
            blocks.append(current)
            current = []
    if current:
        blocks.append(current)
    out = []
    for block in blocks:
        rows = [split_row(l) for l in block]
        if len(rows) >= 2 and all(re.fullmatch(r":?-{2,}:?", c) for c in rows[1] if c):
            out.append((rows[0], rows[2:]))
    return out


def registry(path):
    text = path.read_text()
    rows = {}
    for header, body in tables(text):
        if len(header) != REGISTRY_COLUMNS:
            continue
        for cells in body:
            if len(cells) == REGISTRY_COLUMNS:
                rows[cells[0].strip()] = cells
    return rows


def section(text, heading):
    lines = text.splitlines()
    out, inside = [], False
    for line in lines:
        if line.strip() == heading.strip():
            inside = True
            continue
        if inside and re.match(r"^#{1,3} ", line):
            break
        if inside:
            out.append(line)
    return "\n".join(out) if out else None


def sha256_file(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def manifest(world):
    path = world / "snapshots" / "MANIFEST.sha256"
    pins = {}
    for line in path.read_text().splitlines():
        parts = line.split()
        if len(parts) == 2:
            pins[parts[1]] = parts[0]
    return pins


def check_world(world):
    entry_path = world / ENTRY
    res = {p: {"a": False, "b": False, "c": False, "d": False, "e": False, "f": False,
               "why": []} for p in PAGES}
    if not entry_path.exists():
        for p in PAGES:
            res[p]["why"].append("no entry at %s" % ENTRY)
        return res, 2
    entry = entry_path.read_text()
    head = entry.split("|", 1)[0]
    pins = manifest(world)
    reg = registry(world / "corpus" / "SOURCES.md")
    skill = (world / "SKILL.md").read_text()
    sub = section(skill, SUBSECTION)
    province = (world / "PROVINCE.md").read_text()

    # (f) is page-independent; compute once.
    core = section(province, "## Core") or ""
    f_ok = ENTRY in core

    for page in PAGES:
        row = None
        for _header, body in tables(entry):
            hits = [c for c in body if c and c[0].strip().lower() == page]
            if len(hits) == 1:
                row = hits[0]
                break
        if row is None:
            res[page]["why"].append("(a) no single rule-table row for %s" % page)
            continue
        # (a)
        source_lines = [l for l in head.splitlines() if l.startswith("source:")]
        toks = tokens_of(" | ".join(row[1:]))
        cited = re.findall(r"S\d{3,}", " ".join(row))
        ok_a = (source_lines and any(l.startswith("verified-at:") for l in head.splitlines())
                and any(l.startswith("recheck:") for l in head.splitlines())
                and len(toks) >= 2 and cited)
        snap = world / "snapshots" / (page + ".md")
        snap_text = snap.read_text() if snap.exists() else ""
        located = [t for t in toks if word_bounded(t, collapse(snap_text))]
        ok_a = bool(ok_a and len(located) == len(toks))
        res[page]["a"] = ok_a
        if not ok_a:
            res[page]["why"].append("(a) tokens located %d/%d, cited=%s"
                                    % (len(located), len(toks), cited))
        # (b)
        if not cited:
            res[page]["why"].append("(b) no S### in row")
        else:
            cells = reg.get(cited[0])
            if cells is None:
                res[page]["why"].append("(b) %s not in the world registry" % cited[0])
            else:
                url, kind, tier, scope, anchor, teaches, status, opened, recheck, used = cells[1:11]
                ok_b = (len(cells) == REGISTRY_COLUMNS and status.strip() == "mined"
                        and tier.strip() == "A" and "agentskills.io" in url
                        and opened.strip() == ROUND74_DATE and ENTRY in used)
                res[page]["b"] = ok_b
                if not ok_b:
                    res[page]["why"].append(
                        "(b) %s url=%r status=%r tier=%r opened=%r used-by=%r"
                        % (cited[0], url.split(" ")[-1], status, tier, opened, used))
        # (c)
        if not snap.exists():
            res[page]["why"].append("(c) no snapshot for %s (exit 2)" % page)
        elif pins.get(page + ".md") != sha256_file(snap):
            res[page]["why"].append("(c) snapshot sha256 != manifest pin for %s" % page)
        else:
            res[page]["c"] = True
        # (d)
        q = quote_of(" | ".join(row[1:]))
        words = len(q.split())
        ok_d = bool(q) and 5 <= words <= 25 and collapse(q) in collapse(snap_text)
        res[page]["d"] = ok_d
        if not ok_d:
            res[page]["why"].append("(d) quote %r words=%d located=%s"
                                    % (q[:60], words, collapse(q) in collapse(snap_text)))
        # (e)
        if sub is None:
            res[page]["why"].append("(e) subsection missing from SKILL.md")
        else:
            idhits = [c for _h, body in tables(sub) for c in body
                      if c and cited and cited[0] in " ".join(c)]
            ok_rows = 0
            for cells in idhits:
                action = cells[-1]
                if len(action.split()) >= 5 and any(word_bounded(t, collapse(snap_text))
                                                   for t in tokens_of(action)):
                    ok_rows += 1
            res[page]["e"] = ok_rows >= 2
            if not res[page]["e"]:
                res[page]["why"].append("(e) %d SKILL.md row(s) qualify for %s"
                                        % (ok_rows, page))
        res[page]["f"] = f_ok
        if not f_ok:
            res[page]["why"].append("(f) PROVINCE Core does not name the entry")
    return res, 0



# ------------------------------------------------------- strengthened (C1')
#
# The seat's proposed correction, implemented to prove it (i) kills every
# cheap world the frozen predicate passes and (ii) still scores an honest
# entry 3 of 3.  Four added conjuncts, one per hole found:
#
#   (a') page-unique token: at least one of the row's tokens is located in
#        P's snapshot and in neither of the other two snapshots.
#   (b') id -> page binding: the cited row's URL path ends with
#        `/skill-creation/<P>.md`.
#   (c') fetch provenance: the snapshot's sha256 equals the sha256 recorded in
#        the cited row's anchor cell and in FETCH.tsv, and the recorded HTTP
#        status is 200 (a 404 body is not the page).
#   (d') located-line shape: the located line must be after the page's first
#        `# ` heading, must not be a heading, must not sit in the blockquote
#        block between that heading and the first `## ` heading (the page
#        subtitle), and must not be a markdown link to another
#        `skill-creation/` page.
#   (e') action cell: >= 1 page-unique token of P AND >= 5 words that are
#        neither tokens nor drawn from a pinned generic-filler list.
FILLER = set("""a an and as at before by for from in into is it its of on or
per see says said says the this that these those to use used uses using with
guide page above below here there which while when if then so but not do does
done it's also can may must should would could""".split())


def located_line(snap_text, quote_collapsed):
    for number, line in enumerate(snap_text.splitlines()):
        if quote_collapsed in collapse(line):
            return number
    return None


def line_ok(snap_text, quote_collapsed):
    lines = snap_text.splitlines()
    idx = located_line(snap_text, quote_collapsed)
    if idx is None:
        return False, "not located"
    h1 = next((i for i, l in enumerate(lines) if l.startswith("# ")), None)
    if h1 is None:
        return False, "no H1 in the snapshot"
    if idx <= h1:
        return False, "line %d precedes the H1 (site chrome)" % (idx + 1)
    if lines[idx].lstrip().startswith("#"):
        return False, "heading line"
    h2 = next((i for i, l in enumerate(lines) if i > h1 and l.startswith("## ")), len(lines))
    if h1 < idx < h2 and lines[idx].lstrip().startswith(">"):
        return False, "page-subtitle blockquote"
    if "skill-creation/" in lines[idx] and "](" in lines[idx]:
        return False, "link to another skill-creation page"
    return True, ""


def check_world_strict(world):
    res, _ = check_world(world)
    snaps = {p: (world / "snapshots" / (p + ".md")) for p in PAGES}
    texts = {p: snaps[p].read_text() if snaps[p].exists() else "" for p in PAGES}
    fetch = {}
    if (world / "snapshots" / "FETCH.tsv").exists():
        for line in (world / "snapshots" / "FETCH.tsv").read_text().splitlines():
            f = line.split("\t")
            if len(f) >= 5 and f[0] in PAGES:
                fetch[f[0]] = {"url": f[1], "status": f[2], "bytes": f[3], "sha": f[4]}
    pins = manifest(world) if (world / "snapshots" / "MANIFEST.sha256").exists() else {}
    reg = registry(world / "corpus" / "SOURCES.md")
    if not (world / ENTRY).exists():
        return res
    entry = (world / ENTRY).read_text()
    skill = (world / "SKILL.md").read_text()
    sub = section(skill, SUBSECTION)
    for page in PAGES:
        row = None
        for _h, body in tables(entry):
            hits = [c for c in body if c and c[0].strip().lower() == page]
            if len(hits) == 1:
                row = hits[0]
                break
        if row is None:
            continue
        joined = " | ".join(row[1:])
        toks = tokens_of(joined)
        quote = quote_of(joined)
        others = [texts[o] for o in PAGES if o != page]
        unique = [t for t in toks if word_bounded(t, collapse(texts[page]))
                  and not any(word_bounded(t, collapse(o)) for o in others)]
        # (a')
        if not unique:
            res[page]["a"] = False
            res[page]["why"].append("(a') no page-unique token in the row")
        # (b')
        cited = re.findall(r"S\d{3,}", joined)
        if cited and cited[0] in reg:
            url = reg[cited[0]][1]
            if not url.rstrip().endswith("/skill-creation/%s.md" % page):
                res[page]["b"] = False
                res[page]["why"].append("(b') id %s URL does not name %s" % (cited[0], page))
        # (c')
        if snaps[page].exists():
            sha = sha256_file(snaps[page])
            anchor = reg[cited[0]][5] if cited and cited[0] in reg else ""
            f = fetch.get(page)
            if sha not in anchor:
                res[page]["c"] = False
                res[page]["why"].append("(c') snapshot sha256 not recorded in the row anchor")
            elif f is None or f["sha"] != sha or f["status"] != "200":
                res[page]["c"] = False
                res[page]["why"].append("(c') fetch record status/sha mismatch: %r"
                                        % (f and (f["status"], f["sha"][:12])))
            elif pins.get(page + ".md") != sha:
                res[page]["c"] = False
                res[page]["why"].append("(c') manifest pin != snapshot")
        # (d')
        ok, why = line_ok(texts[page], collapse(quote))
        if not ok:
            res[page]["d"] = False
            res[page]["why"].append("(d') " + why)
        elif not any(word_bounded(quote, collapse(o)) for o in others) is False:
            # quote shared with another page -> not page-specific
            res[page]["d"] = False
            res[page]["why"].append("(d') quote occurs in another page's snapshot")
        # (e')
        if sub is not None and cited:
            qual = 0
            for _h, body in tables(sub):
                for cells in body:
                    if cited[0] not in " ".join(cells):
                        continue
                    action = cells[-1]
                    atoks = tokens_of(action)
                    auniq = [t for t in atoks if word_bounded(t, collapse(texts[page]))
                             and not any(word_bounded(t, collapse(o)) for o in others)]
                    words = [w for w in re.findall(r"[A-Za-z][A-Za-z'-]*", action)
                             if w.lower() not in FILLER and not any(w in t for t in atoks)]
                    if auniq and len(words) >= 5:
                        qual += 1
            res[page]["e"] = qual >= 2
            if not res[page]["e"]:
                res[page]["why"].append("(e') %d action cell(s) carry a page-unique token "
                                        "and >= 5 content words" % qual)
    return res

# ---------------------------------------------------------------- builders

BANNER1 = ("Fetch the complete documentation index at: "
           "https://agentskills.io/llms.txt")
BANNER2 = "Use this file to discover all available pages before exploring further."

STAGED_ENTRY = """\
# Script craft and the one discovery root the specification itself teaches

source: S236 \u2014 https://agentskills.io/skill-creation/using-scripts.md \u2014 fetched as `.md` 12 078 B on 2026-10-23
source: S237 \u2014 https://agentskills.io/skill-creation/quickstart.md \u2014 fetched as `.md` 4 080 B on 2026-10-23
verified-at: 2026-10-23
recheck: 90d \u2014 re-fetch both `.md` pages

**The script half of a skill, stated normatively.** Prose only, no rule table.
"""

PAGE_TOKENS = {"best-practices": "`scripts/`", "using-scripts": "`uvx ruff@0.8.0 check .`",
               "quickstart": "`.agents/skills/`"}


def registry_rows(page_ids, opened=ROUND74_DATE, used=ENTRY, s212_used=None, sha=None):
    lines = ["| id | source | kind | tier | scope | anchor | teaches | status | opened "
             "| recheck | used-by |",
             "|---|---|---|---|---|---|---|---|---|---|---|"]
    for page, sid in page_ids:
        anchor = 'anchor for %s; sha256 %s' % (page, (sha or {}).get(page, "-"))
        lines.append("| %s | Agent Skills \u2014 %s \u2014 "
                     "https://agentskills.io/skill-creation/%s.md | docs | A | scope of %s "
                     "| %s | teaches %s | mined | %s | 90d | %s |"
                     % (sid, page, page, page, anchor, page, opened, used))
    if s212_used:
        lines.append("| S212 | Agent Skills \u2014 Evaluating skill output quality \u2014 "
                     "https://agentskills.io/skill-creation/evaluating-skills.md | docs | A "
                     "| scope | anchor | teaches | mined | %s | 90d | %s |"
                     % (opened, s212_used))
    return "\n".join(lines) + "\n"


def write_world(root, name, entry, sources, skill_rows, snapshots, manifest_pins):
    w = root / name
    (w / "corpus" / "knowledge").mkdir(parents=True, exist_ok=True)
    (w / "snapshots").mkdir(parents=True, exist_ok=True)
    (w / ENTRY).write_text(entry)
    (w / "corpus" / "SOURCES.md").write_text(sources)
    (w / "SKILL.md").write_text("# world SKILL\n\n" + SUBSECTION + "\n\n"
                                + "| page | id | action |\n|---|---|---|\n"
                                + "\n".join(skill_rows) + "\n")
    (w / "PROVINCE.md").write_text("# world province\n\n## Core\n\n- entry: %s\n" % ENTRY)
    for dest, src in snapshots.items():
        (w / "snapshots" / (dest + ".md")).write_bytes(src)
    (w / "snapshots" / "MANIFEST.sha256").write_text(
        "".join("%s  %s.md\n" % (manifest_pins[dest], dest) for dest in snapshots))
    return w


HONEST = {
    "best-practices": {
        "tokens": ['"Match the specificity of your instructions to the fragility of the task."',
                   '`scripts/`'],
        "quote": "Match the specificity of your instructions to the fragility of the task.",
        "cells": ['Fragile steps get the exact verbatim command; every other step gets the '
                  'goal and the reason: "Match the specificity of your instructions to the '
                  'fragility of the task."',
                  'Offer one default and one named escape hatch; a menu of equal options is '
                  'a decision the author never made: "Match the specificity of your '
                  'instructions to the fragility of the task."']},
    "using-scripts": {
        "tokens": ['`uvx ruff@0.8.0 check .`', '`--dry-run`'],
        "quote": "Skills can instruct agents to run shell commands and bundle reusable "
                 "scripts in a `scripts/` directory.",
        "cells": ['Run a packaged linter with `uvx ruff@0.8.0 check .` when the repository '
                  'already has one instead of bundling a second copy.',
                  'Give destructive scripts a `--dry-run` flag so the agent can preview the '
                  'change before it runs.']},
    "quickstart": {
        "tokens": ['`.agents/skills/`', '`roll-dice`'],
        "quote": "The same skill works in any compatible agent, including Claude Code and "
                 "OpenAI Codex.",
        "cells": ['Put the skill under `.agents/skills/` so a VS Code session discovers it '
                  'without configuration.',
                  'Name the example directory `roll-dice` and copy its shape for your first '
                  'skill before adding rules.']},
}


def build(root, snaps):
    pages = {p: (snaps / (p + ".md")).read_bytes() for p in PAGES}
    shas = {p: hashlib.sha256(pages[p]).hexdigest() for p in PAGES}
    notfound = (snaps / "notfound-probe.md").read_bytes()
    nf_sha = hashlib.sha256(notfound).hexdigest()
    subtitle = {p: pages[p].decode().splitlines()[6].lstrip("> ").strip() for p in PAGES}
    ids = [("best-practices", "S232"), ("using-scripts", "S236"), ("quickstart", "S237")]

    def entry_rows(token_for, quote_for, id_for=None):
        rows = ["| page | id | rule tokens | quote |", "|---|---|---|---|"]
        for page, sid in ids:
            rows.append("| %s | %s | %s | \"%s\" |"
                        % (page, id_for(page) if id_for else sid,
                           token_for(page), quote_for(page)))
        return "\n".join(rows) + "\n"

    def fetch_tsv(status=None):
        out = []
        for page in PAGES:
            out.append("%s\thttps://agentskills.io/skill-creation/%s.md\t%s\t%d\t%s"
                       % (page, page, (status or {}).get(page, "200"),
                          len(pages[page]), shas[page]))
        return "\n".join(out) + "\n"

    def make(name, entry, sources, skill_rows, snap_bytes, manifest_sha,
             row_sha, fetch):
        w = root / name
        (w / "corpus" / "knowledge").mkdir(parents=True, exist_ok=True)
        (w / "snapshots").mkdir(parents=True, exist_ok=True)
        (w / ENTRY).write_text(entry)
        (w / "corpus" / "SOURCES.md").write_text(
            sources(sha=row_sha) if callable(sources) else sources)
        (w / "SKILL.md").write_text("# world SKILL\n\n" + SUBSECTION + "\n\n"
                                    + "| page | id | action |\n|---|---|---|\n"
                                    + "\n".join(skill_rows) + "\n")
        (w / "PROVINCE.md").write_text("# world province\n\n## Core\n\n- entry: %s\n" % ENTRY)
        for page, data in snap_bytes.items():
            (w / "snapshots" / (page + ".md")).write_bytes(data)
        (w / "snapshots" / "MANIFEST.sha256").write_text(
            "".join("%s  %s.md\n" % (manifest_sha[page], page) for page in PAGES))
        (w / "snapshots" / "FETCH.tsv").write_text(fetch)

    # W0: base (no entry).
    w = root / "W0_base"
    (w / "corpus" / "knowledge").mkdir(parents=True, exist_ok=True)
    (w / "snapshots").mkdir(parents=True, exist_ok=True)
    (w / "corpus" / "SOURCES.md").write_text(registry_rows(ids, sha=shas))
    (w / "SKILL.md").write_text("# base\n\nno subsection\n")
    (w / "PROVINCE.md").write_text("# base\n\n## Core\n\n- nothing\n")

    # W1: the staged entry verbatim, staged rows (opened 2026-10-23).
    make("W1_staged_verbatim", STAGED_ENTRY,
         registry_rows(ids, opened="2026-10-23",
                       used="corpus/knowledge/spec-script-craft-rules.md", sha=shas),
         ["| best-practices | S232 | copy |"], {p: pages[p] for p in PAGES}, shas, shas,
         fetch_tsv())

    # W2: one site-chrome sentence backs all three pages.
    make("W2_chrome_banner",
         "# chrome entry\n\nsource: S232/S236/S237\nverified-at: %s\nrecheck: 90d\n\n"
         % ROUND74_DATE +
         entry_rows(lambda p: '"%s" "%s"' % (BANNER1, BANNER2), lambda p: BANNER1),
         registry_rows(ids, sha=shas), 
         ['| %s | %s | "%s" |' % (p, sid, BANNER2) for p, sid in ids] +
         ['| %s | %s | "%s" |' % (p, sid, BANNER2) for p, sid in ids],
         {p: pages[p] for p in PAGES}, shas, shas, fetch_tsv())

    # W3: every row cites S212, a different agentskills.io page.
    make("W3_wrong_id",
         "# wrong-id entry\n\nsource: S212\nverified-at: %s\nrecheck: 90d\n\n"
         % ROUND74_DATE +
         entry_rows(lambda p: " ".join(HONEST[p]["tokens"]),
                    lambda p: HONEST[p]["quote"], id_for=lambda p: "S212"),
         registry_rows([], s212_used=ENTRY, sha=shas),
         ['| %s | S212 | %s |' % (p, HONEST[p]["cells"][0]) for p in PAGES] +
         ['| %s | S212 | %s |' % (p, HONEST[p]["cells"][1]) for p in PAGES],
         {p: pages[p] for p in PAGES}, shas, shas, fetch_tsv())

    # W4: honest tokens and quote, vacuous action cells.
    make("W4_token_stuff",
         "# token-stuffed entry\n\nsource: S232/S236/S237\nverified-at: %s\n"
         "recheck: 90d\n\n" % ROUND74_DATE +
         entry_rows(lambda p: " ".join(HONEST[p]["tokens"]), lambda p: HONEST[p]["quote"]),
         registry_rows(ids, sha=shas),
         ['| %s | %s | Use %s as the guide says. |' % (p, sid, HONEST[p]["tokens"][0])
          for p, sid in ids] +
         ['| %s | %s | Use %s as the guide says. |' % (p, sid, HONEST[p]["tokens"][0])
          for p, sid in ids],
         {p: pages[p] for p in PAGES}, shas, shas, fetch_tsv())

    # W5: the page subtitle (a blockquote, not a rule) backs each page.
    make("W5_page_subtitle",
         "# subtitle entry\n\nsource: S232/S236/S237\nverified-at: %s\n"
         "recheck: 90d\n\n" % ROUND74_DATE +
         entry_rows(lambda p: '"%s" `description`' % subtitle[p], lambda p: subtitle[p]),
         registry_rows(ids, sha=shas),
         ['| %s | %s | "%s" |' % (p, sid, subtitle[p]) for p, sid in ids] +
         ['| %s | %s | "%s" |' % (p, sid, subtitle[p]) for p, sid in ids],
         {p: pages[p] for p in PAGES}, shas, shas, fetch_tsv())

    # W6: every snapshot is the site's 404 body (HTTP 404, 705 B).
    make("W6_404_snapshot",
         "# 404-snapshot entry\n\nsource: S232/S236/S237\nverified-at: %s\n"
         "recheck: 90d\n\n" % ROUND74_DATE +
         entry_rows(lambda p: '"%s" "The requested page could not be found."' % BANNER2,
                    lambda p: BANNER2),
         registry_rows(ids, sha=shas),
         ['| %s | %s | "%s" |' % (p, sid, BANNER2) for p, sid in ids] +
         ['| %s | %s | "%s" |' % (p, sid, BANNER2) for p, sid in ids],
         {p: notfound for p in PAGES}, {p: nf_sha for p in PAGES},
         {p: nf_sha for p in PAGES}, fetch_tsv({p: "404" for p in PAGES}))

    # W7: one page's bytes stored as all three snapshots; the rows still carry
    # the page's real fetch sha (the manifest is made to agree with the file).
    make("W7_one_snapshot_three_pages",
         "# swapped-snapshot entry\n\nsource: S232/S236/S237\nverified-at: %s\n"
         "recheck: 90d\n\n" % ROUND74_DATE +
         entry_rows(lambda p: " ".join(HONEST[p]["tokens"]), lambda p: HONEST[p]["quote"]),
         registry_rows(ids, sha=shas),
         ['| %s | %s | %s |' % (p, sid, HONEST[p]["cells"][0]) for p, sid in ids] +
         ['| %s | %s | %s |' % (p, sid, HONEST[p]["cells"][1]) for p, sid in ids],
         {p: pages["using-scripts"] for p in PAGES},
         {p: shas["using-scripts"] for p in PAGES}, shas, fetch_tsv())

    # W8: the honest world (real per-page rules, page-unique tokens, real cells).
    make("W8_honest",
         "# honest entry\n\nsource: S232, S236, S237\nverified-at: %s\nrecheck: 90d\n\n"
         % ROUND74_DATE +
         entry_rows(lambda p: " ".join(HONEST[p]["tokens"]), lambda p: HONEST[p]["quote"]),
         registry_rows(ids, sha=shas),
         ['| %s | %s | %s |' % (p, sid, HONEST[p]["cells"][0]) for p, sid in ids] +
         ['| %s | %s | %s |' % (p, sid, HONEST[p]["cells"][1]) for p, sid in ids],
         {p: pages[p] for p in PAGES}, shas, shas, fetch_tsv())
    print("built worlds under", root)


def check(root):
    names = [d.name for d in sorted(root.iterdir()) if d.is_dir() and d.name.startswith("W")]
    print("%-30s %-4s %s" % ("world", "N/3", "per page (a b c d e f) + reasons"))
    for name in names:
        res, _exit = check_world(root / name)
        backed = sum(1 for p in PAGES if all(res[p][k] for k in "abcdef"))
        detail = []
        for p in PAGES:
            flags = "".join("Y" if res[p][k] else "." for k in "abcdef")
            detail.append("%s=%s" % (p[:4], flags))
        print("%-30s %-4s %s" % (name, "%d/3" % backed, " ".join(detail)))
        for p in PAGES:
            for why in res[p]["why"]:
                print("    %-15s %s" % (p, why))


if __name__ == "__main__":
    if sys.argv[1] == "strict":
        root = pathlib.Path(sys.argv[2])
        print("%-30s %-4s %s" % ("world", "N/3", "per page (a b c d e f)"))
        for name in [d.name for d in sorted(root.iterdir()) if d.is_dir() and d.name.startswith("W")]:
            res = check_world_strict(root / name)
            backed = sum(1 for p in PAGES if all(res[p][k] for k in "abcdef"))
            detail = " ".join("%s=%s" % (p[:4], "".join("Y" if res[p][k] else "." for k in "abcdef"))
                              for p in PAGES)
            print("%-30s %-4s %s" % (name, "%d/3" % backed, detail))
            for p in PAGES:
                for why in res[p]["why"]:
                    if why.startswith(("(a')", "(b')", "(c')", "(d')", "(e')")):
                        print("    %-15s %s" % (p, why))
        raise SystemExit(0)
    if sys.argv[1] == "build":
        build(pathlib.Path(sys.argv[2]), pathlib.Path(sys.argv[3]))
    else:
        check(pathlib.Path(sys.argv[2]))
