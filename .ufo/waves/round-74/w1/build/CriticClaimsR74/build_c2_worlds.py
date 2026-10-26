#!/usr/bin/env python3
"""build_c2_worlds.py -- critic probe (seat CriticClaimsR74, round 74 wave 1).

Builds the cheap C2 worlds for the frozen predicate
`check_sibling_reread.py -> "sibling rows re-pinned and re-read N of 20"`,
so each world can be walked by hand AND by the base checker:

  W1  r49 census copied, commit cells bumped to the freeze heads, nothing else
  W2  W1 + skill/names/arbitration cells recomputed at the freeze head
      + every quote RE-LOCATED by script (no reading of the sibling)
  W2d W2 with a tenth `delta` cell appended to every row (conjunct (c))
  W3  W2 with one lane row dropped (lane-set arm)

It also prints, per lane, whether the r49 quote still occurs at the freeze
head (the "do the quotes die" question) and where a fallback sentence would be
taken from.

The base checker is imported, never modified.  Read-only against the fleet.
Usage: python3 -B build_c2_worlds.py <outdir>
"""
import pathlib
import re
import subprocess
import sys

LANE = "/home/vgpnk/Projects/shokunin/kotoba-shokunin"
FLEET = pathlib.Path("/home/vgpnk/Projects/shokunin")
sys.path.insert(0, LANE + "/verifiers")
import check_sibling_census as c  # noqa: E402

CENSUS = pathlib.Path(LANE) / "corpus/knowledge/sibling-overlap-census-round49.md"
FREEZE = pathlib.Path(LANE) / ".ufo/waves/round-74/receipts/sibling-heads-freeze.tsv"


def read_freeze():
    out = {}
    for line in FREEZE.read_text().splitlines():
        if not line or line.startswith("#"):
            continue
        f = line.split("\t")
        if len(f) >= 5:
            out[f[0]] = {"branch": f[1], "head": f[2]}
    return out


def parse_r49():
    blocks = c.parse_blocks(CENSUS.read_text().splitlines())
    table = c.select_census_table(blocks)
    assert table is not None
    return table["rows"]


def show(repo, commit, path):
    r = subprocess.run(["git", "-C", str(repo), "show", "%s:%s" % (commit, path)],
                       capture_output=True)
    if r.returncode != 0:
        return None
    return r.stdout.decode("utf-8", "replace")


def first_body_sentence(text, skip_lines):
    """A script's fallback: the first line after `skip_lines` with >= 6 words
    that is not a heading and not a fence opener, truncated to 20 words."""
    for number, line in enumerate(text.splitlines(), 1):
        if number <= skip_lines:
            continue
        s = line.strip()
        if not s or s.startswith("#") or s.startswith("```"):
            continue
        words = s.split()
        if len(words) >= 6:
            return number, " ".join(words[:20])
    return None


def find_anchor(text, quote_collapsed):
    """The line number a grep-style script would cite for a (possibly folded)
    quote: find it in the whole-file collapsed text, map back to its first
    line, then confirm with the base checker's own locate_quote."""
    if not quote_collapsed:
        return None
    lines = text.splitlines()
    flat, offsets = [], []
    for number, line in enumerate(lines, 1):
        offsets.append((len(" ".join(flat)), number))
        flat.append(c.collapse(line))
    haystack = " ".join(x for x in flat if x)
    pos = haystack.find(quote_collapsed)
    if pos < 0:
        return None
    guesses = [n for start, n in offsets if start <= pos + 1]
    for number in reversed(guesses[-1:] + guesses[-3:]):
        found, _idx, _head = c.locate_quote(lines, number, quote_collapsed)
        if found:
            return number
    for number in range(1, len(lines) + 1):
        found, _idx, _head = c.locate_quote(lines, number, quote_collapsed)
        if found:
            return number
    return None


def row_line(cells):
    return "| " + " | ".join(cells) + " |"


def main():
    out = pathlib.Path(sys.argv[1])
    out.mkdir(parents=True, exist_ok=True)
    freeze = read_freeze()
    rows = parse_r49()
    header = "| lane | branch | commit | skill file | classification | names kotoba | arbitration | scope quote at | scope quote |"
    sep = "|---|---|---|---|---|---|---|---|---|"

    w1, w2, report = [], [], []
    for line_no, cells in rows:
        if len(cells) != 9:
            print("skip malformed r49 row", line_no, len(cells))
            continue
        lane = c.normalize_lane(cells[0])
        fz = freeze[lane]
        pin = cells[2].strip()
        r49_path, r49_line = c.split_path_line(cells[7])
        quote = c.collapse(c.strip_wrapping(cells[8]))

        # W1: only the commit cell moves.
        w1.append(list(cells[:2]) + [fz["head"]] + list(cells[3:]))

        # W2: recompute the mechanical cells from the pinned SKILL.md.
        repo = FLEET / (lane + "-shokunin")
        skill = show(repo, fz["head"], "SKILL.md")
        if skill is None:
            skill_cell, names_cell, arb_cell = "NONE", "no SKILL.md", "no SKILL.md"
        else:
            desc = c.description_of(skill)
            skill_cell = "SKILL.md"
            names_cell = "yes" if c.token_in("kotoba", desc) else "no"
            named = sorted(n for n in (set(freeze) | {"kotoba"})
                           if n != lane and c.token_in(n, desc))
            arb_cell = ("yes: " + ", ".join(named)) if named else "no"

        # Quote re-location (script, no reading).
        target = show(repo, fz["head"], r49_path)
        located = None
        if target is not None:
            anchor = find_anchor(target, quote)
            if anchor is not None:
                located = (anchor, quote, "r49-quote-still-present")
            if located is None:
                fb = first_body_sentence(target, 5)
                if fb is not None:
                    located = (fb[0], fb[1], "fallback-first-body-sentence")
        if located is None:
            located = (r49_line, quote, "UNLOCATABLE")
        new_path_line = "%s:%d" % (r49_path, located[0])
        w2.append([cells[0], cells[1], fz["head"], skill_cell, cells[4],
                   names_cell, arb_cell, new_path_line, located[1]])
        report.append((lane, pin[:12], fz["head"][:12], located[2],
                       "%s:%d -> %s" % (r49_path, r49_line, new_path_line)))

    def write(name, body, header_line=header, sep_line=sep, extra_headers=None):
        text = ["# critic world: " + name, "", header_line, sep_line] + body + [""]
        (out / (name + ".md")).write_text("\n".join(text))

    write("W1_commit_bump_only", [row_line(r) for r in w1])
    write("W2_carry_forward", [row_line(r) for r in w2])
    write("W2d_carry_forward_delta_cell",
          [row_line(r + ["none"]) for r in w2],
          header_line=header[:-1] + " delta |",
          sep_line=sep + "---|")
    write("W3_msing_row", [row_line(r) for r in w2 if c.normalize_lane(r[0]) != "audio"])

    print("lane          r49pin       freezehead   quote-status                  path:line")
    for lane, pin, head, status, move in report:
        print("%-13s %-12s %-12s %-28s %s" % (lane, pin, head, status, move))
    still = sum(1 for r in report if r[3] == "r49-quote-still-present")
    print("\nquotes still present at the freeze head: %d of %d" % (still, len(report)))
    print("wrote:", ", ".join(sorted(p.name for p in out.glob("W*.md"))))


if __name__ == "__main__":
    main()
