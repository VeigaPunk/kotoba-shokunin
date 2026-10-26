#!/usr/bin/env python3
"""build_worlds.py -- generate the C2 shortcut-control worlds for round 74.

Each world is an overlay bundle:

    <world>/overlay/corpus/knowledge/sibling-overlap-census-round74.md
    <world>/overlay/PROVINCE.md
    <world>/overlay/.ufo/waves/round-74/receipts/sibling-heads-freeze.tsv  (input receipt)

The overlay is copied over a fresh `--shared` clone of the base lane rev
(1e03d1991bc02281b00a5b7a5e00c9d5d5d72908) and committed there; see
score_worlds.sh for the replay and README.md for what each world tests.

Read-only against the lane and the sibling repos: this script only reads
`git show` bytes and writes under its own directory.

Row shape: the round-49 nine cells plus a tenth `delta` cell, header

    | lane | branch | commit | path | classification | names kotoba | arbitration | path:line | quote | delta |

World 1 is the plan's literal "r49 entry copied with commit cells bumped and
nothing else", so its table keeps the round-49 nine-column shape and carries
no delta cell; worlds 2-9 use the ten-column shape.
"""
from __future__ import annotations

import json
import re
import shutil
import subprocess
from pathlib import Path

HERE = Path(__file__).resolve().parent
FLEET = Path("/home/vgpnk/Projects/shokunin")
LANE = FLEET / "kotoba-shokunin"
BASE = "1e03d1991bc02281b00a5b7a5e00c9d5d5d72908"
FREEZE_REL = ".ufo/waves/round-74/receipts/sibling-heads-freeze.tsv"
FREEZE = LANE / FREEZE_REL
CENSUS_R49 = "corpus/knowledge/sibling-overlap-census-round49.md"
ENTRY_REL = "corpus/knowledge/sibling-overlap-census-round74.md"

HEADER9 = ("| lane | branch | commit | path | classification | names kotoba "
           "| arbitration | path:line | quote |")
SEP9 = "|---|---|---|---|---|---|---|---|---|"
HEADER10 = HEADER9[:-2] + " | delta |"
SEP10 = SEP9 + "---|"

CELLS = ("lane", "branch", "commit", "path", "classification",
         "names kotoba", "arbitration", "path:line", "quote")

# World 6: a sentence copied from a different lane's file (kama
# corpus/knowledge/cross-lane-scope.md:29 at its frozen head).  It is not in
# kagi's PROVINCE.md at the pin, so the row's quote cannot be located.
FOREIGN_QUOTE = ('"**Kotoba** owns the instruction/agent surface and its '
                 'model/fallback wording; **kama** owns independent verification '
                 'of the target endpoint."')


def git(repo, *args):
    p = subprocess.run(["git", "-C", str(repo)] + list(args),
                       capture_output=True, text=True)
    if p.returncode != 0:
        raise RuntimeError("git %s in %s failed: %s" % (" ".join(args), repo, p.stderr.strip()))
    return p.stdout


def split_cells(line):
    cells = [c.strip() for c in re.split(r"(?<!\\)\|", line)]
    if cells and cells[0] == "":
        cells = cells[1:]
    if cells and cells[-1] == "":
        cells = cells[:-1]
    return cells


def collapse(text):
    return re.sub(r"\s+", " ", text).strip()


def read_freeze():
    rows = {}
    for line in FREEZE.read_text(encoding="utf-8").splitlines():
        if not line.strip() or line.startswith("#"):
            continue
        lane, branch, head = line.split("\t")[:3]
        rows[lane] = {"branch": branch, "head40": head}
    return rows


def read_r49_table():
    text = git(LANE, "show", BASE + ":" + CENSUS_R49)
    lines = text.splitlines()
    start = None
    end = None
    for i, line in enumerate(lines):
        if line.startswith("| lane | branch | commit |"):
            start = i
            break
    if start is None:
        raise RuntimeError("round-49 census table not found")
    j = start
    while j < len(lines) and lines[j].startswith("|"):
        j += 1
    end = j
    rows = []
    for line in lines[start + 2:end]:
        cells = split_cells(line)
        if len(cells) != 9:
            raise RuntimeError("unexpected r49 row width %d: %r" % (len(cells), line[:80]))
        rows.append(dict(zip(CELLS, cells)))
    return text, start, end, rows


def find_quote_line(lane, head, path, quote_text):
    """Locate the collapsed quote in `path` at `head`; return (line, width) or None.

    Searches single lines, then windows of 2..6 consecutive lines, which is
    how a folded PROVINCE.md paragraph carries a sentence.
    """
    try:
        content = git(FLEET / (lane + "-shokunin"), "show", "%s:%s" % (head, path))
    except RuntimeError:
        return None
    lines = content.splitlines()
    want = collapse(quote_text)
    if not want:
        return None
    for width in range(1, 7):
        for start in range(0, len(lines) - width + 1):
            window = collapse(" ".join(lines[start:start + width]))
            if want in window:
                return start + 1, width
    return None


SHORTSTAT = re.compile(r"(\d+) files? changed"
                       r"(?:, (\d+) insertions?\(\+\))?"
                       r"(?:, (\d+) deletions?\(-\))?")
# Fallback for git's singular wording ("1 file changed"): the same pattern
# with `files?` already covers it.


def render_delta(shortstat_text):
    """`+<insertions>/-<deletions>` from `git diff --shortstat`, `none` if empty.

    The round-74 counter's own rendering (check_sibling_reread.py
    `render_delta`): the world's delta cell must equal it, so it is the same
    function shape, not a paraphrase.
    """
    text = " ".join(shortstat_text.split())
    if not text:
        return "none"
    match = SHORTSTAT.search(text)
    if not match:
        raise RuntimeError("cannot read a git diff --shortstat line: %r" % shortstat_text)
    return "+%d/-%d" % (int(match.group(2) or 0), int(match.group(3) or 0))


def shortstat(lane, pin, head):
    out = git(FLEET / (lane + "-shokunin"), "diff", "--shortstat",
              pin, head, "--", "SKILL.md", "PROVINCE.md")
    return render_delta(out)


def load_lanes():
    data = json.loads((HERE / "lanes.json").read_text(encoding="utf-8"))
    return data


def build_entry_table(rows, world, freeze, lanes):
    """Return (header, separator, row_lines) for one world's census table."""
    out = []
    for row in rows:
        lane = row["lane"]
        cells = dict(row)
        cells["commit"] = freeze[lane]["head40"]
        if world == "world-1-bump-only":
            out.append("| " + " | ".join(cells[c] for c in CELLS) + " |")
            continue
        delta = lanes[lane]["delta"]
        found = find_quote_line(lane, cells["commit"], row["path"],
                                row["quote"].strip().strip('"'))
        if found is not None:
            cells["path:line"] = "%s:%d" % (row["path"], found[0])
        if world == "world-6-quote-absent":
            if lane == "kagi":
                cells["quote"] = FOREIGN_QUOTE
        if world == "world-8-none-names-kotoba":
            if lane == "kagi":
                cells["classification"] = "none"
        if world == "world-9-delta-wrong-numbers":
            if lane == "kake":
                delta = "+954/-5"
        if world == "world-5-not-freeze-head":
            if lane == "kumitate":
                cells["commit"] = lanes[lane]["pin"]
        out.append("| " + " | ".join(cells[c] for c in CELLS) + " | " + delta + " |")
    if world == "world-4-duplicate-row":
        dup = [l for l in out if l.startswith("| lore |")][0]
        out.append(dup)
    if world == "world-3-missing-row":
        out = [l for l in out if not l.startswith("| lore |")]
    return out


def build_entry(text, start, end, world, rows, freeze, lanes):
    lines = text.splitlines()
    table = build_entry_table(rows, world, freeze, lanes)
    if world == "world-1-bump-only":
        new = [HEADER9, SEP9] + table
    else:
        new = [HEADER10, SEP10] + table
    return "\n".join(lines[:start] + new + lines[end:]) + "\n"


def build_province(world, freeze, lanes, base_text):
    """Base PROVINCE.md with the `## Adjacent` commit cells re-pinned.

    world-7 leaves PROVINCE.md at the base revision (the plan's "PROVINCE.md
    unchanged" world); every other world re-pins the commit cell, and worlds
    3/5/8 additionally change one classification or remove one row.
    """
    if world == "world-7-province-unchanged":
        return base_text
    lines = base_text.splitlines()
    out = []
    for line in lines:
        m = re.match(r"^\| ([a-z0-9-]+) \| ([a-z]+) \| ([0-9a-f]{40}) \| (.*) \|$", line)
        if not m:
            out.append(line)
            continue
        lane, classification, _commit, boundary = m.groups()
        if lane not in freeze:
            out.append(line)
            continue
        if world == "world-3-missing-row" and lane == "lore":
            continue
        commit = freeze[lane]["head40"]
        if world == "world-5-not-freeze-head" and lane == "kumitate":
            commit = lanes[lane]["pin"]
        if world == "world-8-none-names-kotoba" and lane == "kagi":
            classification = "none"
        out.append("| %s | %s | %s | %s |" % (lane, classification, commit, boundary))
    return "\n".join(out) + "\n"


WORLDS = [
    ("world-1-bump-only", "r49 entry copied to the r74 path with every census commit cell bumped to the freeze head and nothing else (no delta cell, quotes and mechanical cells as written at round 49)."),
    ("world-2-carry-forward", "world 1 plus a `delta` cell per row computed from `git diff --shortstat <r49 pin> <freeze head> -- SKILL.md PROVINCE.md` and quotes re-located by script wherever the old text still exists at the new pin. The pure carry-forward: measured, not asserted below 20."),
    ("world-3-missing-row", "world 2 with the `lore` row dropped from the census table and from PROVINCE.md § Adjacent."),
    ("world-4-duplicate-row", "world 2 with the `lore` census row duplicated (PROVINCE.md unchanged from world 2)."),
    ("world-5-not-freeze-head", "world 2 with `kumitate`'s commit cell left at its round-49 pin in the census and in PROVINCE.md (a commit that is not the freeze head)."),
    ("world-6-quote-absent", "world 2 with `kagi`'s quote replaced by a sentence copied from kama's corpus at the freeze head: absent from kagi's PROVINCE.md at the pin."),
    ("world-7-province-unchanged", "world 2's entry against the base PROVINCE.md § Adjacent (round-49 commit cells, unchanged)."),
    ("world-8-none-names-kotoba", "world 2 with `kagi` classified `none` in the census and in PROVINCE.md, while kagi's pinned SKILL.md contains the whole word `kotoba` at line 297."),
    ("world-9-delta-wrong-numbers", "world 2 with `kake`'s delta cell stating the right shape and wrong numbers (954 insertions where the recomputation gives 955)."),
]


REPLAY = """```bash
F=/home/vgpnk/Projects/shokunin; BASE=1e03d1991bc02281b00a5b7a5e00c9d5d5d72908
W=$F/kotoba-shokunin/.ufo/waves/round-74/w1/build/ExecSibControlsR74/{world}
P=$(mktemp -d /tmp/k74fleet-{world}.XXXX)
for e in "$F"/*; do b=$(basename "$e"); [ "$b" = kotoba-shokunin ] && continue; ln -s "$e" "$P/$b"; done
git clone --shared -q --no-checkout "$F/kotoba-shokunin" "$P/kotoba-shokunin"
git -C "$P/kotoba-shokunin" checkout -q "$BASE"
cp -a "$W/overlay/." "$P/kotoba-shokunin/"
git -C "$P/kotoba-shokunin" -c user.name=control-seat \\
    -c user.email=control@example.invalid add -A
git -C "$P/kotoba-shokunin" -c user.name=control-seat \\
    -c user.email=control@example.invalid commit -q -m "control world {world}"
(cd "$P/kotoba-shokunin" && python3 -B verifiers/check_sibling_reread.py --rev HEAD)
rm -rf "$P"
```

`../score_worlds.sh <counter.py>` runs that replay over every world and prints
`<world> <N of 20> <exit>`; `../score_worlds.sh --emulate` prints the expected
score from `../emulate_reread.py` (the plan's conjuncts with the base checker's
own functions) when the counter is not available.
"""


def build_readme(name, desc, expected, diag=False):
    lines = ["# %s — C2 shortcut control%s" % (name, " (diagnostic, not a control)" if diag else ""), "",
             "**What it is.** " + desc, "",
             "**Overlay** (copied over a fresh `--shared` clone of the lane at",
             "`1e03d1991bc02281b00a5b7a5e00c9d5d5d72908`):", "",
             "- `corpus/knowledge/sibling-overlap-census-round74.md` — the census entry.",
             "- `PROVINCE.md` — the base file with the `## Adjacent` table rows re-pinned"
             " (world 7 keeps it at the base revision).",
             "- `.ufo/waves/round-74/receipts/sibling-heads-freeze.tsv` — the freeze receipt,"
             " copied unchanged. Not required: the counter falls back to the object store at"
             " `329e7d91` when the worktree lacks the file (measured: 18 of 20 with and"
             " without); the copy keeps the sandbox self-contained.", "",
             "**Replay.**", "", REPLAY.format(world=name).rstrip(), ""]
    if expected:
        lines += ["**Expected score.** %s of 20 (mode: %s)." % (expected["score"], expected["mode"]), ""]
    else:
        lines += ["**Expected score.** not recorded (run `../score_worlds.sh <counter.py>` or"
                  " `../score_worlds.sh --emulate`).", ""]
    lines += ["**Row lanes that fail** (from the recorded run):", ""]
    if expected and expected.get("lanes"):
        for lane in sorted(expected["lanes"]):
            why = expected["lanes"][lane]
            if why:
                lines.append("- `%s`: %s" % (lane, "; ".join(why)))
        if not any(expected["lanes"].values()):
            lines.append("- none")
    else:
        lines.append("- not recorded")
    lines += ["", "**Bound.** The overlay is a test fixture: it is never committed to the lane"
              " and never merged. Scores are per-lane counts from the round-74 C2 predicate;"
              " the world says nothing about whether any classification is the right call.", ""]
    return "\n".join(lines)


def build_diag(world2_dir, name):
    """Copy world 2's overlay and recompute revenger's mechanical cells.

    Diagnostic only: measures what the carry-forward scores once the one stale
    mechanical cell set (revenger gains a SKILL.md at the freeze head) is
    recomputed.  Not one of the plan's shortcut worlds, so `world-*` globbing
    in score_worlds.sh does not pick it up.
    """
    wdir = HERE / name
    if wdir.exists():
        shutil.rmtree(wdir)
    shutil.copytree(world2_dir / "overlay", wdir / "overlay")
    entry_path = wdir / "overlay" / ENTRY_REL
    lines = entry_path.read_text(encoding="utf-8").splitlines()
    out = []
    for line in lines:
        if line.startswith("| revenger |"):
            cells = split_cells(line)
            cells[3] = "SKILL.md"
            cells[5] = "no"
            cells[6] = "no"
            line = "| " + " | ".join(cells) + " |"
        out.append(line)
    entry_path.write_text("\n".join(out) + "\n", encoding="utf-8")
    return wdir


def main():
    freeze = read_freeze()
    lanes = load_lanes()
    text, start, end, rows = read_r49_table()
    base_province = git(LANE, "show", BASE + ":PROVINCE.md")
    expected_path = HERE / "expected.json"
    expected = {}
    if expected_path.exists():
        expected = json.loads(expected_path.read_text(encoding="utf-8"))
    for name, desc in WORLDS:
        wdir = HERE / name
        if wdir.exists():
            shutil.rmtree(wdir)
        entry = build_entry(text, start, end, name, rows, freeze, lanes)
        province = build_province(name, freeze, lanes, base_province)
        out = wdir / "overlay"
        (out / ENTRY_REL).parent.mkdir(parents=True, exist_ok=True)
        (out / ENTRY_REL).write_text(entry, encoding="utf-8")
        (out / "PROVINCE.md").write_text(province, encoding="utf-8")
        (out / FREEZE_REL).parent.mkdir(parents=True, exist_ok=True)
        (out / FREEZE_REL).write_bytes(FREEZE.read_bytes())
        (wdir / "README.md").write_text(
            build_readme(name, desc, expected.get(name)), encoding="utf-8")
        print("wrote", name)
    diag = ("diag-2b-recomputed",
            "world 2 with `revenger`'s three mechanical cells recomputed from its "
            "pinned `SKILL.md` (the lane gained a skill file at the freeze head: "
            "`path=SKILL.md`, `names kotoba=no`, `arbitration=no`). Diagnostic: measures "
            "the carry-forward ceiling once the one stale mechanical cell set is fixed.")
    build_diag(HERE / "world-2-carry-forward", diag[0])
    (HERE / diag[0] / "README.md").write_text(
        build_readme(diag[0], diag[1], expected.get(diag[0]), diag=True), encoding="utf-8")
    print("wrote", diag[0])


if __name__ == "__main__":
    main()
