#!/usr/bin/env python3
"""normalize-staged-rows.py -- campaign-schema -> fleet 11-column SOURCES row transform.

Round 72, wave 1, seat ExecIdNormalize (lane kotoba). Read-only attacker of the staged
package; it writes only its own build directory and a scratch mirror under /tmp.

WHY. The staged campaign rows in /home/vgpnk/Projects/shokuknow/merge/kotoba/SOURCES.append.md
carry the campaign's ids and a prose `recheck` cell ("90d -- re-fetch ... (ran 2026-10-23)").
The fleet registry corpus/SOURCES.md is validated by scripts/sources-census.sh validate, which
requires, per row:

  * NF=13 on a `|` split  -> exactly 11 cells, so no literal and no escaped `|` in any cell
    (a `\\|` still splits: gawk -F'|' is a literal single-character split) -- E01;
  * `recheck` = ISO date | NNd | symbolic cadence `^[A-Za-z][A-Za-z0-9 _-]*$` -- E09;
  * `status` in queued|mined|rejected -- E07; tier in A|B|C -- E06;
  * `used-by` paths exist on disk relative to the lane root -- E11;
  * ids unique -- E03; no duplicate URL within one scope -- E04;
  * rows outside `## Registry` -- E12.

WHAT THIS SCRIPT DOES (one row in, one row out):

  1. recheck  : "90d -- re-fetch X (ran 2026-10-23)" -> `90d`, and the stripped prose becomes a
                Gate note (the r70 convention: the prose lands in the lesson's `## Gate`).
  2. pipes    : any literal `|` or escaped `\\|` in a cell is refused by default; with
                `--repair <SID>:<col>` the surplus cells are joined into that column and the
                pipe is rewritten to `; ` (the anchor rewrite the seat item names). Both paths
                are proven by --self-test.
  3. ids      : re-pointed "by document" -- one new id per distinct source URL, assigned from the
                registry's next free id upward in the order the blocks declare their rows (the
                r70 precedent: the URL is the evidence, the id follows it). Every `S###` token in
                a selected row that is also in the map is re-pointed too (cross-references), and
                each such rewrite is recorded as a Gate note.
  4. used-by  : exactly the admitted entry paths that cite the row -- the staged `used-by` cell
                intersected with `--entry PATH` (admission), plus explicit `--cite PATH=ID,ID`
                edges for an entry that cites a row the staged cell does not name. A row with no
                admitted citer is HELD BACK (not emitted), because `status: mined` with an empty
                used-by is a W03 warning and a row nobody cites is not an admitted row.
  5. status   : `mined` (the fleet contract's status for a row whose claims are carried into an
                entry).

MODES
  (default)                 emit blocks, renumber map, Gate notes, collision notes under --out
  --mirror DIR --rev REV    build a scratch mirror of REV, insert the emitted rows into its
                            Registry table, generate the candidate knowledge entries, run
                            `sources-census.sh validate --file DIR/corpus/SOURCES.md`, print the
                            transcript; `--control ...` adds one negative row per control world
                            (E01/E03/E04/E11) and restores the mirror afterwards.
  --self-test               run the transform's own fixtures; `killed`/`SURVIVED` per arm.

EXIT  0 ok | 1 findings (E-codes in the mirror, or a refused row) | 2 usage/env | 3 self-test fail

No credential material, no network: the script reads two local markdown files, one registry and
one git archive of the lane it is given.
"""

import argparse
import json
import os
import re
import subprocess
import sys
import tempfile

LANE_DEFAULT = "/home/vgpnk/Projects/shokunin/kotoba-shokunin"
APPEND_DEFAULT = "/home/vgpnk/Projects/shokuknow/merge/kotoba/SOURCES.append.md"
CENSUS_DEFAULT = "/home/vgpnk/Projects/shokunin/scripts/sources-census.sh"

# The census parser accepts 0-3 leading ASCII spaces before a Markdown row (its own contract).
ROW_RE = re.compile(r"^ {0,3}\| S\d{3,} ")
ID_TOKEN_RE = re.compile(r"\bS\d{3,}\b")
CADENCE_RE = re.compile(r"^\d+d$")
ISO_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
SYMBOLIC_RE = re.compile(r"^[A-Za-z][A-Za-z0-9 _-]*$")
URL_RE = re.compile(r"https?://[^\s|]+")
DASH_RE = re.compile(r"\s*\u2014\s*|\s+--\s+")
QUOTE_RE = re.compile(r'\b(?:quote|also)\s+"([^"]+)"')

HEADER = ("| id | source | kind | tier | scope | anchor | teaches | status | opened | "
          "recheck | used-by |")
SEPARATOR = "|---|---|---|---|---|---|---|---|---|---|---|"

# Block order is data, not arithmetic: the assignment names entry 1 (the rung boundary) and
# entry 2 (context rot), and the r70 precedent gives the first-declared entry the lower ids.
BLOCKS_DEFAULT = [
    {
        "name": "entry-1",
        "entry": "corpus/knowledge/skill-vs-always-on-boundary.md",
        "title": ("Skill versus always-on file versus one-off prompt \u2014 the middle rung "
                  "(round 72, candidate)"),
        "ids": ["S261", "S262", "S263", "S264"],
    },
    {
        "name": "entry-2",
        "entry": "corpus/knowledge/context-rot-and-always-on-context.md",
        "title": ("Context rot and always-on context \u2014 the cost side of passive injection "
                  "(round 72, candidate)"),
        "ids": ["S248", "S254", "S255", "S256"],
    },
]

CONTROL_ROWS = {
    # one negative world per E-code the seat item names; each must make the census red
    "pipe": ("| {id} | Control -- literal pipe in the anchor -- https://example.test/pipe | docs "
             "| B | control scope for E01 | \"a | b\" anchor carrying a raw pipe | control teaches "
             "cell long enough | mined | 2026-10-23 | 90d | corpus/knowledge/{entry} |"),
    "dup-id": ("| {id} | Control -- duplicate id -- https://example.test/dup-id | docs | B | "
               "control scope for E03 | anchor | control teaches cell long enough | mined | "
               "2026-10-23 | 90d | corpus/knowledge/{entry} |"),
    "dup-url": ("| {id} | Control -- duplicate url in scope -- https://example.test/dup-url | docs "
                "| B | control scope for E04 | anchor | control teaches cell long enough | mined | "
                "2026-10-23 | 90d | corpus/knowledge/{entry} |"),
    "missing-usedby": ("| {id} | Control -- absent used-by path -- https://example.test/missing | "
                       "docs | B | control scope for E11 | anchor | control teaches cell long "
                       "enough | mined | 2026-10-23 | 90d | corpus/knowledge/absent-entry.md |"),
}


class TransformError(Exception):
    """A staged row that cannot be normalized without inventing data."""


# --------------------------------------------------------------------- parsing ---
def split_cells(raw):
    """Split one staged row on `|` exactly as the census does (gawk -F'|')."""
    line = raw.rstrip("\n")
    line = line.lstrip(" ")
    if not line.startswith("|") or not line.endswith("|"):
        raise TransformError("row does not start and end with '|': %r" % raw[:80])
    parts = line.split("|")
    return [p.strip() for p in parts[1:-1]]


def parse_rows(path):
    """Return {staged_id: {cells, line}} for every 0-3-space-pattern row in the document."""
    rows = {}
    with open(path, encoding="utf-8") as fh:
        for lineno, raw in enumerate(fh, 1):
            if not ROW_RE.match(raw):
                continue
            cells = split_cells(raw)
            if not cells:
                raise TransformError("%s:%d empty row" % (path, lineno))
            sid = cells[0]
            if not re.match(r"^S\d{3,}$", sid):
                raise TransformError("%s:%d bad id %r" % (path, lineno, sid))
            if sid in rows:
                raise TransformError("%s:%d duplicate staged id %s" % (path, lineno, sid))
            rows[sid] = {"id": sid, "cells": cells, "line": lineno}
    return rows


def registry_ids(path):
    """{id: {url, scope}} for the fleet registry's own rows."""
    reg = {}
    for sid, row in parse_rows(path).items():
        cells = row["cells"]
        if len(cells) < 11:
            raise TransformError("%s: registry row %s has %d cells" % (path, sid, len(cells)))
        reg[sid] = {"url": url_of(cells[1]), "scope": cells[4], "line": row["line"]}
    return reg


def url_of(source):
    """The census's url_of(), ported: fragment dropped, one trailing '/' dropped, host lowered."""
    m = URL_RE.search(source)
    if not m:
        return ""
    u = m.group(0)
    u = re.sub(r"#[^ ]*$", "", u)
    if u.endswith("/"):
        u = u[:-1]
    u = re.sub(r"^[A-Za-z]+://", "", u)
    i = u.find("/")
    if i >= 0:
        return u[:i].lower() + u[i:]
    return u.lower()


def raw_url(source):
    m = URL_RE.search(source)
    return m.group(0) if m else ""


# ------------------------------------------------------------------- transform ---
def split_recheck(cell, sid):
    """'90d -- prose' -> ('90d', 'prose'); 'on-release' -> ('on-release', '')."""
    m = DASH_RE.search(cell)
    head = cell[:m.start()].strip() if m else cell.strip()
    note = cell[m.end():].strip() if m else ""
    if not head:
        raise TransformError("%s: recheck cell is empty" % sid)
    if CADENCE_RE.match(head):
        return head, note
    if ISO_RE.match(head):
        try:
            import datetime
            datetime.date.fromisoformat(head)
        except ValueError:
            raise TransformError("%s: recheck ISO date invalid: %s (E09)" % (sid, head))
        return head, note
    if SYMBOLIC_RE.match(head):
        return head, note
    raise TransformError("%s: recheck %r is neither ISO, NNd nor a symbolic cadence (E09)"
                         % (sid, head))


def sanitize_cell(cell, sid, col, policy, notes):
    """No literal and no escaped '|' may survive in a cell."""
    if "|" not in cell and "\\|" not in cell:
        return cell
    if policy == "refuse":
        raise TransformError(
            "%s: cell %d carries a pipe (%r); refusing (E01). Re-run with "
            "--repair %s:%d --pipe-policy rewrite to rewrite it" % (sid, col, cell[:60], sid, col))
    new = cell.replace("\\|", "; ").replace("|", "; ")
    new = re.sub(r"\s+", " ", new).strip()
    notes.append("%s: cell %d pipe rewritten to '; ' (%r -> %r)" % (sid, col, cell[:40], new[:40]))
    return new


def repair_cells(cells, sid, col, extra):
    """Join the surplus cells produced by a pipe in column `col` back into that column.

    A pipe in a cell splits it, so the pieces around the split are re-joined with '; '; a
    trailing backslash left by an escaped `\\|` is dropped rather than carried into the cell.
    """
    idx = col - 1
    if idx < 0 or idx >= len(cells):
        raise TransformError("%s: --repair column %d out of range" % (sid, col))
    if extra is None:
        extra = len(cells) - 11 + 1
    if extra < 2:
        raise TransformError("%s: --repair %s:%d needs at least 2 cells to join, got %d"
                             % (sid, sid, col, extra))
    pieces = cells[idx:idx + extra]
    joined = pieces[0].rstrip("\\").rstrip()
    for i, piece in enumerate(pieces[1:], 1):
        tail = piece.rstrip("\\").rstrip() if i < len(pieces) - 1 else piece.lstrip()
        joined = joined + "; " + tail
    return cells[:idx] + [joined] + cells[idx + extra:]


def assign_ids(blocks, reg):
    nxt = max(int(s[1:]) for s in reg) + 1
    mapping = {}
    for block in blocks:
        for sid in block["ids"]:
            if sid in mapping:
                raise TransformError("staged id %s declared in two blocks" % sid)
            new = "S%d" % nxt
            if new in reg:
                raise TransformError("assigned id %s already in the registry (E03)" % new)
            mapping[sid] = new
            nxt += 1
    return mapping


def build_used_by(staged_cell, sid, admitted, cite_map):
    staged = [p.strip() for p in staged_cell.split(",")]
    staged = [p for p in staged if p and p != "\u2014"]
    out = [p for p in staged if p in admitted]
    for path, ids in cite_map.items():
        if sid in ids and path not in out:
            out.append(path)
    return out


def normalize_row(row, new_id, id_map, admitted, cite_map, pipe_policy, repairs, notes):
    sid = row["id"]
    cells = list(row["cells"])
    if len(cells) != 11:
        rep = repairs.get(sid)
        if not rep:
            raise TransformError(
                "%s:%d splits into %d cells, not 11 (E01): a literal or escaped '|' in a cell. "
                "Name the column with --repair %s:<col> and re-run."
                % (row["_path"], row["line"], len(cells), sid))
        col, extra = rep
        cells = repair_cells(cells, sid, col, extra)
        if len(cells) != 11:
            raise TransformError("%s: --repair %s:%d left %d cells, not 11"
                                 % (sid, sid, col, len(cells)))
        notes.append("%s: %d surplus cell(s) joined into column %d" % (sid, len(cells) - 11, col))

    cells = [sanitize_cell(c, sid, i + 1, pipe_policy, notes) for i, c in enumerate(cells)]

    recheck, recheck_note = split_recheck(cells[9], sid)
    if recheck_note:
        notes.append("%s: recheck `%s`; stripped prose: \"%s\"" % (sid, recheck, recheck_note))

    used = build_used_by(cells[10], sid, admitted, cite_map)

    # cross-references: every S### token that the map re-points is re-pointed in the row too
    for col in (1, 4, 5, 6):
        def sub(m):
            tok = m.group(0)
            if tok in id_map and id_map[tok] != tok:
                notes.append("%s: cross-reference %s -> %s in column %d"
                             % (sid, tok, id_map[tok], col + 1))
                return id_map[tok]
            return tok
        cells[col] = ID_TOKEN_RE.sub(sub, cells[col])

    out = [
        new_id,
        cells[1],          # source
        cells[2],          # kind
        cells[3],          # tier
        cells[4],          # scope
        cells[5],          # anchor
        cells[6],          # teaches
        "mined",           # status
        cells[8],          # opened
        recheck,           # recheck
        ", ".join(used) if used else "\u2014",
    ]
    return out, used, recheck_note


def render_line(cells):
    line = "| " + " | ".join(cells) + " |"
    if line.count("|") != 12:
        raise TransformError("emitted row has %d pipes, want 12: %s"
                             % (line.count("|"), line[:120]))
    if any("|" in c or "\\|" in c for c in cells):
        raise TransformError("emitted row still carries a pipe in a cell: %s" % line[:120])
    return line


def cross_checks(rows_out, reg):
    """E03/E04 refuse, W04/advisory note -- run before anything is written."""
    problems = []
    seen_url_scope = {}
    for r in rows_out:
        cells = r["cells"]
        if cells[0] in reg:
            problems.append("E03 %s: id already in the registry" % cells[0])
        key = (url_of(cells[1]), cells[4])
        if key in seen_url_scope:
            problems.append("E04 %s: url %s repeats within scope of %s (no `supersedes`)"
                            % (cells[0], key[0], seen_url_scope[key]))
        seen_url_scope[key] = cells[0]
    notes = []
    for r in rows_out:
        cells = r["cells"]
        u, scope = url_of(cells[1]), cells[4]
        for rid, meta in reg.items():
            if meta["url"] and meta["url"] == u:
                if meta["scope"] == scope:
                    notes.append("%s: E04 url %s repeats %s in the same scope -- refuse or "
                                 "supersede" % (cells[0], u, rid))
                else:
                    notes.append("%s: W04 duplicate url %s across scopes (%s)"
                                 % (cells[0], u, rid))
            elif (meta["url"].replace(".md", "").rstrip("/") ==
                  u.replace(".md", "").rstrip("/")):
                notes.append("%s: advisory -- same document as %s under `.md`-insensitive "
                             "normalization (%s); the census's url_of() keeps `.md`, so neither "
                             "W04 nor E04 fires" % (cells[0], rid, u))
    return problems, notes


def build(args):
    append_path = args.append
    reg_path = args.registry
    blocks = BLOCKS_DEFAULT
    if args.blocks:
        with open(args.blocks, encoding="utf-8") as fh:
            blocks = json.load(fh)
    reg = registry_ids(reg_path)
    staged = parse_rows(append_path)

    selected = [sid for b in blocks for sid in b["ids"]]
    missing = [s for s in selected if s not in staged]
    if missing:
        raise TransformError("staged ids absent from %s: %s" % (append_path, ", ".join(missing)))

    id_map = assign_ids(blocks, reg)
    admitted = set(args.entry)
    new_to_staged = {new: staged_id for staged_id, new in id_map.items()}
    cite_map = {}
    for spec in args.cite:
        path, _, ids = spec.partition("=")
        for token in (i.strip() for i in ids.split(",")):
            if not token:
                continue
            # a citation edge may name the staged id or the new id; both resolve to the staged id
            sid = token if token in id_map else new_to_staged.get(token)
            if sid is None:
                raise TransformError("--cite %s: %s is neither a selected staged id nor a new id"
                                     % (path, token))
            cite_map.setdefault(path, []).append(sid)

    only = set()
    for spec in args.only:
        only.update(x.strip() for x in spec.split(",") if x.strip())

    gate_notes, held_back, rows_out, normalized = [], [], [], []
    per_block = {}
    for block in blocks:
        brows = []
        for sid in block["ids"]:
            if only and sid not in only and id_map[sid] not in only:
                continue
            row = dict(staged[sid])
            row["_path"] = append_path
            notes = []
            cells, used, recheck_note = normalize_row(row, id_map[sid], id_map, admitted,
                                                      cite_map, args.pipe_policy, args.repairs,
                                                      notes)
            gate_notes.extend(notes)
            entry = {"cells": cells, "staged": sid, "block": block["name"],
                     "url": raw_url(cells[1]), "line": row["line"],
                     "recheck_note": recheck_note}
            normalized.append(entry)
            if not used:
                held_back.append("%s (staged %s) -- no admitted entry cites it; staged used-by "
                                 "was %r" % (id_map[sid], sid, row["cells"][10]))
                continue
            rows_out.append(entry)
            brows.append(entry)
        per_block[block["name"]] = brows

    problems, collision_notes = cross_checks(normalized, reg)
    if problems and not args.force:
        raise TransformError("; ".join(problems))

    emitted = {r["staged"] for r in rows_out}
    selection = []
    for block in blocks:
        for sid in block["ids"]:
            if only and sid not in only and id_map[sid] not in only:
                continue
            cells = staged[sid]["cells"]
            selection.append({
                "staged": sid, "id": id_map[sid], "block": block["name"],
                "entry": block["entry"], "url": raw_url(cells[1]),
                "url_normalized": url_of(cells[1]), "line": staged[sid]["line"],
                "emitted": sid in emitted,
            })

    return {
        "blocks": blocks, "per_block": per_block, "rows": rows_out, "id_map": id_map,
        "gate_notes": gate_notes, "held_back": held_back, "collisions": collision_notes,
        "reg": reg, "append": append_path, "registry": reg_path, "problems": problems,
        "selection": selection,
    }


# ---------------------------------------------------------------------- output ---
def block_markdown(rows):
    out = [HEADER, SEPARATOR]
    for r in rows:
        out.append(render_line(r["cells"]))
    return "\n".join(out) + "\n"


def renumber_map(result):
    """URL -> id, for every selected row (emitted or held back), so any subset keeps its ids."""
    m = {}
    for sel in result["selection"]:
        if sel["url"] in m:
            raise TransformError("two selected rows share the url %s" % sel["url"])
        m[sel["url"]] = {
            "id": sel["id"],
            "staged_id": sel["staged"],
            "entry": sel["entry"],
            "block": sel["block"],
            "append_line": sel["line"],
            "url_normalized": sel["url_normalized"],
            "emitted": sel["emitted"],
        }
    return m


def renumber_markdown(result, rmap):
    out = ["| staged | new id | block | entry | emitted | url |", "|---|---|---|---|---|---|"]
    for url, meta in rmap.items():
        out.append("| %s | %s | %s | %s | %s | %s |"
                   % (meta["staged_id"], meta["id"], meta["block"], meta["entry"],
                      "yes" if meta["emitted"] else "held back", url))
    return "\n".join(out) + "\n"


def gate_markdown(result):
    out = ["## Gate notes -- stripped recheck prose and rewrites (candidate, for "
           "`corpus/lessons/round-72.md` \u00a7 Gate)", ""]
    out.append("Renumber map: staged ids re-pointed by document from the registry's next free "
               "id; the URL is the evidence and the id follows it (r70 precedent). A held-back "
               "row keeps its assigned id, so a later admission changes nothing but its block.")
    out.append("")
    for r in result["rows"]:
        title = URL_RE.sub("", r["cells"][1]).strip().rstrip("\u2014").strip()
        out.append("- **%s** (staged %s) -- %s -- `%s`"
                   % (r["cells"][0], r["staged"], title, r["url"]))
    out.append("")
    out.append("### Rewrites and stripped cells")
    out.append("")
    for n in result["gate_notes"]:
        out.append("- " + n)
    if not result["gate_notes"]:
        out.append("- (none: no selected row needed a pipe repair, and every recheck cell "
                   "carried prose -- listed above -- but no cell was rewritten)")
    out.append("")
    if result["held_back"]:
        out.append("### Held back (not emitted)")
        out.append("")
        for h in result["held_back"]:
            out.append("- " + h)
        out.append("")
    return "\n".join(out) + "\n"


def collision_markdown(result):
    out = ["## URL collision notes (W04 / E04 / advisory)", ""]
    out.append("Registry rows scanned: %d (next free id S%d)."
               % (len(result["reg"]), max(int(s[1:]) for s in result["reg"]) + 1))
    sel = result["selection"]
    emitted = [s["id"] for s in sel if s["emitted"]]
    held = [s["id"] for s in sel if not s["emitted"]]
    out.append("")
    out.append("Selected rows checked: %d (%d emitted: %s; %d held back: %s)."
               % (len(sel), len(emitted), ", ".join(emitted) or "-",
                  len(held), ", ".join(held) or "-"))
    out.append("")
    if result["collisions"]:
        for n in result["collisions"]:
            out.append("- " + n)
    else:
        out.append("- none")
    out.append("")
    return "\n".join(out) + "\n"


def entry_text(block, rows, opened_note):
    lines = []
    for r in rows:
        cells = r["cells"]
        lines.append("source: %s \u2014 %s \u2014 %s \u2014 opened %s (carried from the staged "
                     "campaign row %s; this seat did not re-open the page)"
                     % (cells[0], cells[1], cells[5], cells[8], r["staged"]))
    lines.append("verified-at: %s" % (rows[0]["cells"][8] if rows else "unknown"))
    first_note = rows[0].get("recheck_note") if rows else ""
    lines.append("recheck: %s%s" % (
        rows[0]["cells"][9] if rows else "unknown",
        (" \u2014 " + first_note + " (row %s; every row's own stripped prose is in the round-72 "
         "Gate notes)" % rows[0]["cells"][0]) if first_note else ""))
    lines.append("ground: %s" % opened_note)
    lines.append("")
    lines.append("# " + block["title"])
    lines.append("")
    lines.append("**Candidate entry.** Rows normalized by seat ExecIdNormalize in round-72 wave 1 "
                 "from the read-only campaign package `merge/kotoba/`; admission is the "
                 "source-opening seats' and the L1's decision, and the rule prose for "
                 "`SKILL.md` \u00a7 Trigger-fidelity checklist is the C1 seat's. Every claim below is "
                 "the staged row's own `teaches` cell; the quotes are carried from the row's "
                 "`anchor` cell and were not re-fetched here.")
    lines.append("")
    lines.append("## What the rows teach")
    lines.append("")
    for r in rows:
        lines.append("- **%s** — %s" % (r["cells"][0], r["cells"][6]))
    lines.append("")
    lines.append("## Located quotes (carried from the anchor cells)")
    lines.append("")
    lines.append("| row | quotes |")
    lines.append("|---|---|")
    for r in rows:
        quotes = QUOTE_RE.findall(r["cells"][5])
        cell = " / ".join('"%s"' % q for q in quotes) if quotes else "(anchor carries no quoted span)"
        lines.append("| %s | %s |" % (r["cells"][0], cell))
    lines.append("")
    return "\n".join(lines) + "\n"


def write_outputs(args, result):
    out = args.out
    os.makedirs(os.path.join(out, "blocks"), exist_ok=True)
    os.makedirs(os.path.join(out, "entries"), exist_ok=True)
    written = []
    for block in result["blocks"]:
        rows = result["per_block"][block["name"]]
        if not rows:
            continue
        p = os.path.join(out, "blocks", block["name"] + ".md")
        with open(p, "w", encoding="utf-8") as fh:
            fh.write("# Candidate append block -- %s (entry: %s)\n\n"
                     % (block["name"], block["entry"]))
            fh.write("Rows in document order of the staged ids; ids assigned from the "
                     "registry's next free id.\n\n")
            fh.write(block_markdown(rows))
        written.append(p)
        pe = os.path.join(out, "entries", os.path.basename(block["entry"]))
        with open(pe, "w", encoding="utf-8") as fh:
            fh.write(entry_text(block, rows, "normalization candidate, round 72 wave 1; rows %s "
                               "from staged %s" % (", ".join(r["cells"][0] for r in rows),
                                                   ", ".join(r["staged"] for r in rows))))
        written.append(pe)
    rmap = renumber_map(result)
    p = os.path.join(out, "renumber-map.json")
    with open(p, "w", encoding="utf-8") as fh:
        json.dump(rmap, fh, indent=2, ensure_ascii=False, sort_keys=True)
        fh.write("\n")
    written.append(p)
    p = os.path.join(out, "renumber-map.md")
    with open(p, "w", encoding="utf-8") as fh:
        fh.write(renumber_markdown(result, rmap))
    written.append(p)
    p = os.path.join(out, "gate-notes.md")
    with open(p, "w", encoding="utf-8") as fh:
        fh.write(gate_markdown(result))
    written.append(p)
    p = os.path.join(out, "collisions.md")
    with open(p, "w", encoding="utf-8") as fh:
        fh.write(collision_markdown(result))
    written.append(p)
    return written


# ---------------------------------------------------------------------- mirror ---
def extract_tree(lane, rev, dest):
    p1 = subprocess.Popen(["git", "-C", lane, "archive", rev], stdout=subprocess.PIPE)
    p2 = subprocess.Popen(["tar", "-x", "-C", dest], stdin=p1.stdout)
    p1.stdout.close()
    rc2 = p2.wait()
    rc1 = p1.wait()
    if rc1 != 0 or rc2 != 0:
        raise TransformError("git archive %s | tar -x failed (git=%d tar=%d)" % (rev, rc1, rc2))


def insert_block(path, block_text):
    with open(path, encoding="utf-8") as fh:
        lines = fh.read().splitlines(True)
    try:
        idx = next(i for i, l in enumerate(lines) if l.rstrip("\n") == "## Paths")
    except StopIteration:
        raise TransformError("%s has no '## Paths' heading to insert before" % path)
    payload = block_text.splitlines(True) + ["\n"]
    lines[idx:idx] = payload
    with open(path, "w", encoding="utf-8") as fh:
        fh.writelines(lines)


def run_census(census, sources_file):
    cmd = ["bash", census, "validate", "--file", sources_file]
    proc = subprocess.run(cmd, capture_output=True, text=True)
    return cmd, proc


def mirror(args, result):
    lane = args.lane
    dest = args.mirror
    os.makedirs(dest, exist_ok=True)
    extract_tree(lane, args.rev, dest)
    sources = os.path.join(dest, "corpus", "SOURCES.md")
    if not os.path.isfile(sources):
        raise TransformError("mirror has no corpus/SOURCES.md at %s" % sources)

    rows = result["rows"]
    block_text = block_markdown(rows)
    insert_block(sources, block_text)

    entries = []
    for block in result["blocks"]:
        brows = result["per_block"][block["name"]]
        if not brows:
            continue
        p = os.path.join(dest, block["entry"])
        os.makedirs(os.path.dirname(p), exist_ok=True)
        with open(p, "w", encoding="utf-8") as fh:
            fh.write(entry_text(block, brows, "normalization candidate, round 72 wave 1; rows %s "
                               "from staged %s" % (", ".join(r["cells"][0] for r in brows),
                                                   ", ".join(r["staged"] for r in brows))))
        entries.append(p)

    # entries another seat owns (the C1 A4 entry) are copied in, never authored here
    for spec in args.entry_src:
        rel, _, src = spec.partition("=")
        if not rel or not src:
            raise TransformError("--entry-src wants PATH=SOURCE, got %r" % spec)
        if not os.path.isfile(src):
            raise TransformError("--entry-src source not a file: %s" % src)
        p = os.path.join(dest, rel)
        os.makedirs(os.path.dirname(p), exist_ok=True)
        with open(src, "rb") as fh:
            data = fh.read()
        with open(p, "wb") as fh:
            fh.write(data)
        entries.append(p)

    transcript = []
    transcript.append("mirror: %s (git -C %s archive %s | tar -x)" % (dest, lane, args.rev))
    transcript.append("rows inserted: %d (%s)" % (len(rows), ", ".join(r["cells"][0] for r in rows)))
    transcript.append("candidate entries written: %s" % ", ".join(
        os.path.relpath(e, dest) for e in entries))
    transcript.append("")
    cmd, proc = run_census(args.census, sources)
    transcript.append("command: " + " ".join(cmd))
    transcript.append(proc.stdout.rstrip("\n"))
    transcript.append("exit=%d" % proc.returncode)
    transcript.append("W04 lines: %d" % proc.stdout.count("\tW04\t"))
    clean_rc = proc.returncode

    controls = []
    with open(sources, encoding="utf-8") as fh:
        original = fh.read()
    for name in args.control:
        template = CONTROL_ROWS[name]
        new_id = rows[0]["cells"][0] if name == "dup-id" else "S999"
        entry_rel = os.path.basename(next(b["entry"] for b in result["blocks"]
                                          if result["per_block"][b["name"]]))
        row_text = template.format(id=new_id, entry=entry_rel)
        if name == "dup-url":
            first = rows[0]
            row_text = ("| S998 | Control -- duplicate url in scope -- %s | docs | B | %s | "
                        "anchor | control teaches cell long enough | mined | 2026-10-23 | 90d | "
                        "%s |" % (first["url"], first["cells"][4], first["cells"][10]))
        mutated = original.replace("## Paths", row_text + "\n\n## Paths", 1)
        with open(sources, "w", encoding="utf-8") as fh:
            fh.write(mutated)
        ccmd, cproc = run_census(args.census, sources)
        codes = sorted({m for m in re.findall(r"\t([EW]\d\d)\t", cproc.stdout)})
        controls.append((name, cproc.returncode, codes))
        with open(sources, "w", encoding="utf-8") as fh:
            fh.write(original)
    transcript.append("")
    transcript.append("control worlds (one negative row appended to the same mirror, then restored):")
    for name, rc, codes in controls:
        transcript.append("  %-15s exit=%d codes=%s" % (name, rc, ",".join(codes) or "-"))
    bad = [c for c in controls if c[1] == 0]
    transcript.append("")
    transcript.append("clean mirror exit=%d; controls red=%d/%d"
                      % (clean_rc, len(controls) - len(bad), len(controls)))
    return "\n".join(transcript) + "\n", clean_rc, bad


# ------------------------------------------------------------------- self-test ---
FIXTURE = (
    "| S900 | Synthetic \u2014 anchor pipe \u2014 https://example.test/a | docs | B | fixture scope"
    " | \"a | b\" and `x \\| y` | fixture teaches | mined | 2026-10-23 | 90d \u2014 re-fetch and"
    " confirm (ran 2026-10-23) | corpus/knowledge/fixture.md |\n"
)


def self_test():
    fails = []

    def arm(label, fn, want=None, expect_exc=False):
        try:
            got = fn()
            ok = (want(got) if callable(want) else got == want) and not expect_exc
        except Exception as exc:  # noqa: BLE001 - an arm reports, never aborts the run
            got = "EXC:" + str(exc)
            ok = expect_exc and (want(got) if callable(want) else True)
        print(("killed\t" if ok else "SURVIVED\t") + label)
        if not ok:
            print("        got: %r" % (got,))
            fails.append(label)

    # 1. a pipe in a cell is refused at 11 cells
    def _refuse():
        cells = split_cells(FIXTURE)
        if len(cells) != 11:
            raise TransformError("splits into %d cells, not 11" % len(cells))
        return "parsed"
    arm("pipe-refused-without-repair", _refuse,
        lambda g: "not 11" in g, expect_exc=True)

    # 2. --repair + rewrite produces 11 clean cells
    def _repair():
        cells = split_cells(FIXTURE)
        cells = repair_cells(cells, "S900", 6, None)
        notes = []
        cells = [sanitize_cell(c, "S900", i + 1, "rewrite", notes) for i, c in enumerate(cells)]
        return (len(cells), any("|" in c or "\\|" in c for c in cells), len(notes), cells[5])
    arm("pipe-rewritten-to-semicolon", _repair,
        lambda g: g[0] == 11 and g[1] is False and ";" in g[3] and "\\" not in g[3])

    # 3. refuse policy on a cell that still carries a pipe
    def _still_refuses():
        return sanitize_cell('a \\| b', "S900", 6, "refuse", [])
    arm("refuse-policy-raises", _still_refuses,
        lambda g: "refusing" in g and "E01" in g, expect_exc=True)

    # 4. recheck prose is stripped, cadence kept
    arm("recheck-prose-stripped", lambda: split_recheck("90d \u2014 re-fetch and confirm", "S900"),
        lambda g: g[0] == "90d" and g[1] == "re-fetch and confirm")
    arm("recheck-symbolic-kept", lambda: split_recheck("on-release", "S900"),
        lambda g: g == ("on-release", ""))
    arm("recheck-iso-kept", lambda: split_recheck("2027-01-01", "S900"),
        lambda g: g == ("2027-01-01", ""))
    arm("recheck-garbage-raises", lambda: split_recheck("whenever-ish!!", "S900"),
        lambda g: "E09" in g, expect_exc=True)

    # 5. ids: sequential from next free, then a rendered line is NF=13
    reg = {"S001": {}, "S213": {}}
    blocks = [{"name": "b1", "entry": "e1.md", "ids": ["S001", "S002"]},
              {"name": "b2", "entry": "e2.md", "ids": ["S003"]}]
    arm("ids-sequential-from-214", lambda: assign_ids(blocks, reg),
        lambda g: list(g.values()) == ["S214", "S215", "S216"])

    # 6. cross-reference re-pointed
    def _crossref():
        cells = ["S900", "src https://example.test/x", "docs", "B", "scope mentions S002",
                 "anchor", "teaches citing S001", "mined", "2026-10-23", "90d",
                 "corpus/knowledge/fixture.md"]
        id_map = {"S001": "S214", "S002": "S215"}
        notes = []
        row = {"id": "S900", "cells": cells, "line": 1, "_path": "fixture"}
        out, used, _ = normalize_row(row, "S216", id_map, {"corpus/knowledge/fixture.md"}, {},
                                     "refuse", {}, notes)
        return out[4], out[6], used
    arm("cross-reference-repointed", _crossref,
        lambda g: g[0] == "scope mentions S215" and g[1] == "teaches citing S214"
        and g[2] == ["corpus/knowledge/fixture.md"])

    # 7. used-by filter: unadmitted paths dropped, cite edges added
    def _used():
        staged = "corpus/knowledge/a.md, corpus/knowledge/b.md"
        return build_used_by(staged, "S900", {"corpus/knowledge/b.md"},
                             {"corpus/knowledge/c.md": ["S900"]})
    arm("used-by-admitted-only", _used,
        lambda g: g == ["corpus/knowledge/b.md", "corpus/knowledge/c.md"])

    # 8. E04 within scope refuses, W04 across scopes notes
    def _e04():
        rows = [{"cells": ["S214", "x -- https://example.test/u", "docs", "B", "same scope", "a",
                           "t", "mined", "2026-10-23", "90d", "corpus/knowledge/a.md"]},
                {"cells": ["S215", "y -- https://example.test/u", "docs", "B", "same scope", "a",
                           "t", "mined", "2026-10-23", "90d", "corpus/knowledge/a.md"]}]
        return cross_checks(rows, {})
    arm("E04-within-scope-refused", _e04, lambda g: any("E04" in p for p in g[0]))

    def _w04():
        rows = [{"cells": ["S214", "x -- https://example.test/u", "docs", "B", "new scope", "a",
                           "t", "mined", "2026-10-23", "90d", "corpus/knowledge/a.md"]}]
        return cross_checks(rows, {"S001": {"url": "example.test/u", "scope": "old scope"}})
    arm("W04-across-scopes-noted", _w04,
        lambda g: not g[0] and any("W04" in n for n in g[1]))

    # 9. a rendered line is NF=13 under a `|` split
    def _nf():
        line = render_line(["S214", "s", "docs", "B", "sc", "an", "t", "mined", "2026-10-23",
                            "90d", "corpus/knowledge/a.md"])
        return len(line.strip().strip("|").split("|")) + 2
    arm("rendered-line-NF-13", _nf, lambda g: g == 13)

    # 10. a held-back row (no admitted citer) is not emitted
    def _held():
        cells = ["S900", "src https://example.test/x", "docs", "B", "scope", "anchor", "teaches",
                 "mined", "2026-10-23", "90d", "corpus/knowledge/not-admitted.md"]
        notes = []
        out, used, _ = normalize_row({"id": "S900", "cells": cells, "line": 1,
                                      "_path": "fixture"},
                                     "S214", {}, {"corpus/knowledge/other.md"}, {}, "refuse", {},
                                     notes)
        return used, out[10]
    arm("held-back-when-uncited", _held, lambda g: g[0] == [] and g[1] == "\u2014")

    if fails:
        print("self-test FAILED: %s" % ", ".join(fails), file=sys.stderr)
        return 3
    print("self-test ok")
    return 0


# ----------------------------------------------------------------------- main ---
def parse_repair(spec):
    sid, _, rest = spec.partition(":")
    col, _, extra = rest.partition(":")
    if not sid or not col:
        raise TransformError("--repair wants SID:COL[:EXTRA], got %r" % spec)
    return sid, (int(col), int(extra) if extra else None)


def main(argv):
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--append", default=APPEND_DEFAULT)
    ap.add_argument("--registry", default=os.path.join(LANE_DEFAULT, "corpus", "SOURCES.md"))
    ap.add_argument("--lane", default=LANE_DEFAULT)
    ap.add_argument("--blocks", default=None)
    ap.add_argument("--entry", action="append", default=[], metavar="PATH",
                    help="an admitted entry path (repeatable); used-by keeps only these")
    ap.add_argument("--cite", action="append", default=[], metavar="PATH=ID,ID",
                    help="extra citation edge: this entry cites these staged ids")
    ap.add_argument("--only", action="append", default=[], metavar="ID,ID",
                    help="emit only these staged or new ids")
    ap.add_argument("--repair", action="append", default=[], metavar="SID:COL[:EXTRA]")
    ap.add_argument("--pipe-policy", choices=["refuse", "rewrite"], default="refuse")
    ap.add_argument("--force", action="store_true", help="keep going past E03/E04 findings")
    ap.add_argument("--out", default=None, help="write blocks/map/notes here")
    ap.add_argument("--mirror", default=None, help="build and validate a scratch mirror here")
    ap.add_argument("--rev", default=None, help="lane revision to mirror")
    ap.add_argument("--census", default=CENSUS_DEFAULT)
    ap.add_argument("--entry-src", action="append", default=[], metavar="PATH=SOURCE",
                    help="copy another seat's entry file into the mirror at PATH (never authored)")
    ap.add_argument("--control", action="append", default=[], choices=sorted(CONTROL_ROWS))
    ap.add_argument("--self-test", action="store_true")
    args = ap.parse_args(argv)

    if args.self_test:
        return self_test()

    repairs = {}
    for spec in args.repair:
        sid, rep = parse_repair(spec)
        repairs[sid] = rep
    args.repairs = repairs

    try:
        result = build(args)
    except TransformError as exc:
        print("ERROR: %s" % exc, file=sys.stderr)
        return 2

    if args.out:
        for p in write_outputs(args, result):
            print("wrote %s" % p)

    if args.mirror:
        if not args.rev:
            print("ERROR: --mirror needs --rev", file=sys.stderr)
            return 2
        try:
            text, rc, bad = mirror(args, result)
        except TransformError as exc:
            print("ERROR: %s" % exc, file=sys.stderr)
            return 2
        sys.stdout.write(text)
        if rc != 0 or bad:
            return 1
        return 0

    if not args.out:
        # stdout mode: the block(s), for a quick look
        for block in result["blocks"]:
            rows = result["per_block"][block["name"]]
            if rows:
                sys.stdout.write("# %s (%s)\n\n" % (block["name"], block["entry"]))
                sys.stdout.write(block_markdown(rows))
                sys.stdout.write("\n")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
