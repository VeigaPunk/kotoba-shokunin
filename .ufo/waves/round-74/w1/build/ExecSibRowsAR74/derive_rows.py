#!/usr/bin/env python3
"""derive_rows.py -- C2 mechanical row cells for the lanes of seat ExecSibRowsAR74.

Round 74, wave 1.  Derives, for a list of sibling lanes, the cells the
round-49 census row shape needs, from the frozen fleet head recorded in
`receipts/sibling-heads-freeze.tsv`, using the BASE checker's own derivation
functions (imported from a scratch copy of
`git show 1e03d1991bc02281b00a5b7a5e00c9d5d5d72908:verifiers/check_sibling_census.py`).
Nothing here re-implements a cell: `description_of`, `token_in`,
`fleet_lanes`, `git_show` and `mechanical_findings` are the checker's.

Outputs a TSV; quote / path:line / classification cells are left empty for
the sibling scouts and the merge seat.

Usage: derive_rows.py <scratch-checker.py> <out.tsv>
"""

import hashlib
import importlib.util
import json
import re
import subprocess
import sys
from pathlib import Path

BASE = "1e03d1991bc02281b00a5b7a5e00c9d5d5d72908"
LANE_REPO = Path("/home/vgpnk/Projects/shokunin/kotoba-shokunin")
FLEET = Path("/home/vgpnk/Projects/shokunin")
FREEZE = LANE_REPO / ".ufo/waves/round-74/receipts/sibling-heads-freeze.tsv"
MY_LANES = ["audio", "chousa", "game-dev-2d", "game-dev-3d", "kagi"]
CELL_SEP = ";;"
OUT_DIR = "/home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-74/w1/build/ExecSibRowsAR74"


def load_checker(path):
    spec = importlib.util.spec_from_file_location("base_census", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def lane_git(*args):
    return subprocess.run(["git", "-C", str(LANE_REPO)] + list(args),
                          capture_output=True)


def lane_show(path):
    proc = lane_git("show", "%s:%s" % (BASE, path))
    if proc.returncode != 0:
        raise SystemExit("lane git show failed for %s: %s"
                         % (path, proc.stderr.decode("utf-8", "replace")))
    return proc.stdout.decode("utf-8", "replace")


def read_freeze():
    rows = {}
    for line in FREEZE.read_text(encoding="utf-8").splitlines():
        if not line.strip() or line.startswith("#"):
            continue
        lane, branch, head40, skill_blob, prov_blob = line.split("\t")
        rows[lane] = {"branch": branch, "head40": head40,
                      "skill_blob": skill_blob, "province_blob": prov_blob}
    return rows


def r49_pins(chk):
    """lane -> (classification, commit) from the BASE PROVINCE.md ## Adjacent."""
    text = lane_show("PROVINCE.md")
    blocks = chk.parse_blocks(text.splitlines())
    table = chk.select_province_table(blocks)
    if table is None:
        raise SystemExit("base PROVINCE.md: no 4-column Adjacent table")
    pins = {}
    for _line_no, cells in table["rows"]:
        if len(cells) != chk.PROVINCE_COLUMNS:
            continue
        lane = chk.normalize_lane(cells[0])
        pins[lane] = (cells[1].strip().lower(), cells[2].strip().lower())
    return pins


def r49_census_rows(chk):
    text = lane_show("corpus/knowledge/sibling-overlap-census-round49.md")
    blocks = chk.parse_blocks(text.splitlines())
    table = chk.select_census_table(blocks)
    if table is None:
        raise SystemExit("base r49 census: no 9-column table")
    rows = {}
    for line_no, cells in table["rows"]:
        if len(cells) != chk.CENSUS_COLUMNS:
            continue
        rows[chk.normalize_lane(cells[0])] = dict(
            zip(chk.CENSUS_CELL_NAMES, cells), line=line_no)
    return rows


def shortstat(repo, old, new):
    proc = subprocess.run(["git", "-C", str(repo), "diff", "--shortstat",
                           old, new, "--", "SKILL.md", "PROVINCE.md"],
                          capture_output=True, text=True)
    if proc.returncode != 0:
        return "ERROR", proc.stderr.strip()
    out = proc.stdout.strip()
    if not out:
        return "none", ""
    ins = re.search(r"(\d+) insertion", out)
    dels = re.search(r"(\d+) deletion", out)
    return "+%d/-%d" % (int(ins.group(1)) if ins else 0,
                        int(dels.group(1)) if dels else 0), out


def kotoba_hits(chk, text):
    if text is None:
        return ""
    return CELL_SEP.join("%d" % n for n, line in enumerate(text.splitlines(), 1)
                         if chk.token_in("kotoba", line))


def description_lines(skill_text):
    """The physical lines of the frontmatter `description` value, numbered."""
    if skill_text is None:
        return []
    lines = skill_text.splitlines()
    start = None
    for i, line in enumerate(lines):
        if line.startswith("description:"):
            start = i
            break
    if start is None:
        return []
    out = [start]
    rest = lines[start].split(":", 1)[1].strip()
    # A block scalar indicator (>, |, with chomping) or an empty value means
    # the body is on the following indented lines.
    if rest in ("", ">", "|", ">-", "|-", ">+", "|+"):
        j = start + 1
        while j < len(lines) and lines[j][:1] in (" ", "\t") and lines[j].strip():
            out.append(j)
            j += 1
    return [(n + 1, lines[n].strip()) for n in out]


def province_scope_lines(text):
    """`Domain` / `Owns` paragraph lines of PROVINCE.md, numbered."""
    if text is None:
        return []
    lines = text.splitlines()
    out = []
    i = 0
    while i < len(lines):
        if re.match(r"\A(\*\*Domain:\*\*|\*\*Owns:\*\*|Owns:|Domain:)", lines[i]):
            out.append((i + 1, lines[i].strip()))
            j = i + 1
            while j < len(lines) and lines[j].strip():
                out.append((j + 1, lines[j].strip()))
                j += 1
            i = j
            continue
        i += 1
    return out


def cells_at(chk, lane, repo, commit, all_lanes):
    skill_text, err = chk.git_show(repo, commit, "SKILL.md")
    if err and skill_text is None:
        pass
    province_text, _ = chk.git_show(repo, commit, "PROVINCE.md")
    if skill_text is None:
        skill_file = "NONE"
        names = "no SKILL.md"
        arb = "no SKILL.md"
        description = ""
    else:
        skill_file = "SKILL.md"
        description = chk.description_of(skill_text)
        names = "yes" if chk.token_in("kotoba", description) else "no"
        named = sorted(n for n in all_lanes if n != lane and chk.token_in(n, description))
        arb = ("yes: " + ", ".join(named)) if named else "no"
    return {"skill_file": skill_file, "names_kotoba": names, "arbitration": arb,
            "skill_text": skill_text, "province_text": province_text,
            "description": description}


def fmt_lines(pairs):
    return CELL_SEP.join("%d:%s" % (n, t) for n, t in pairs)


def delta_files(repo, old, new):
    """Per-file shortstat, so the summed cell is decomposable."""
    out = []
    for path in ("SKILL.md", "PROVINCE.md"):
        proc = subprocess.run(["git", "-C", str(repo), "diff", "--shortstat",
                               old, new, "--", path],
                              capture_output=True, text=True)
        text = proc.stdout.strip()
        if not text:
            out.append("%s:none" % path)
            continue
        ins = re.search(r"(\d+) insertion", text)
        dels = re.search(r"(\d+) deletion", text)
        out.append("%s:+%d/-%d" % (path, int(ins.group(1)) if ins else 0,
                                   int(dels.group(1)) if dels else 0))
    return CELL_SEP.join(out)


def carry_forward(chk, repo, lane, commit, row):
    """Do the r49 row's own quote and path:line still locate at `commit`?"""
    try:
        path, line_no = chk.split_path_line(row["path:line"])
    except ValueError as exc:
        return "malformed r49 path:line (%s)" % exc
    text, err = chk.git_show(repo, commit, path)
    if text is None:
        return "r49 path:line %s unreadable at the head (%s)" % (row["path:line"], err)
    quote = chk.collapse(chk.strip_wrapping(row["quote"]))
    found, matched, heading = chk.locate_quote(text.splitlines(), line_no, quote)
    if not found:
        return "r49 quote NOT found at %s (+/-%d)" % (row["path:line"],
                                                      chk.LINE_TOLERANCE)
    if heading:
        return "r49 quote now on a heading line %d" % (matched + 1)
    return "r49 quote relocates at %s:%d" % (path, matched + 1)


def main():
    if len(sys.argv) != 3:
        raise SystemExit("usage: derive_rows.py <checker.py> <out.tsv>")
    checker_path, out_path = Path(sys.argv[1]), Path(sys.argv[2])
    chk = load_checker(checker_path)
    print("base checker sha256: %s" % hashlib.sha256(checker_path.read_bytes()).hexdigest())

    freeze = read_freeze()
    pins = r49_pins(chk)
    r49rows = r49_census_rows(chk)
    fleet_all = chk.fleet_lanes(FLEET) | {chk.SELF_LANE}
    print("fleet lanes: %d" % len(fleet_all))

    header = ["lane", "branch", "commit40", "r49_pin", "skill_file",
              "names_kotoba", "arbitration", "delta", "delta_files",
              "kotoba_hits_skillmd", "kotoba_hits_province",
              "skill_scope_candidates", "province_scope_candidates",
              "path_line", "quote", "classification"]
    lines = ["\t".join(header)]
    cells_row = {}
    rederive_ok = True
    report = []

    for lane in MY_LANES:
        fz = freeze[lane]
        repo = chk.repo_dir_for(lane, FLEET)
        head = fz["head40"]
        # the freeze head really is the lane's default-branch head right now
        ref = subprocess.run(["git", "-C", str(repo), "rev-parse",
                              "refs/heads/%s" % fz["branch"]],
                             capture_output=True, text=True).stdout.strip()
        if ref != head:
            print("WARN %s: refs/heads/%s is %s, freeze says %s"
                  % (lane, fz["branch"], ref or "-", head))

        cur = cells_at(chk, lane, repo, head, fleet_all)
        cells_row[lane] = {"branch": fz["branch"], "head40": head,
                           "skill_file": cur["skill_file"],
                           "names_kotoba": cur["names_kotoba"],
                           "arbitration": cur["arbitration"]}
        pin, pin_commit = pins[lane]
        delta, raw = shortstat(repo, pin_commit, head)

        # the checker's own cell validation, and its own `none` rule
        values = {"path": cur["skill_file"], "names kotoba": cur["names_kotoba"],
                  "arbitration": cur["arbitration"]}
        problems = chk.mechanical_findings(repo, head, values, lane, fleet_all,
                                           "adjacent")
        none_problems = chk.mechanical_findings(repo, head, values, lane, fleet_all,
                                                "none")
        none_rule_fires = any("classified none, but" in p for p in none_problems)

        # re-derive the round-49 pin's cells and compare to the r49 row
        old = cells_at(chk, lane, repo, pin_commit, fleet_all)
        old_row = r49rows[lane]
        want = {"skill_file": old_row["path"].strip(),
                "names_kotoba": old_row["names kotoba"].strip(),
                "arbitration": old_row["arbitration"].strip(),
                "commit": old_row["commit"].strip().lower(),
                "branch": old_row["branch"].strip(),
                "classification": old_row["classification"].strip().lower()}
        got = {"skill_file": old["skill_file"], "names_kotoba": old["names_kotoba"],
               "arbitration": old["arbitration"],
               "commit": pin_commit, "branch": fz["branch"], "classification": pin}
        # LANE-SIDE cells + commit/class must match; branch is a frozen-file fact,
        # compared separately (the r49 census recorded it too).
        diffs = []
        for key in ("skill_file", "names_kotoba", "arbitration", "commit",
                    "classification"):
            if key in ("skill_file", "names_kotoba", "arbitration"):
                same = got[key].strip().lower() == want[key].strip().lower()
            else:
                same = got[key] == want[key]
            if not same:
                diffs.append("%s: r49 row %r vs re-derived %r"
                             % (key, want[key], got[key]))
        if got["branch"] != want["branch"]:
            diffs.append("branch: r49 row %r vs freeze %r"
                         % (want["branch"], got["branch"]))
        if diffs:
            rederive_ok = False

        rows_out = [
            lane, fz["branch"], head, pin_commit, cur["skill_file"],
            cur["names_kotoba"], cur["arbitration"], delta,
            delta_files(repo, pin_commit, head),
            kotoba_hits(chk, cur["skill_text"]),
            kotoba_hits(chk, cur["province_text"]),
            fmt_lines(description_lines(cur["skill_text"])),
            fmt_lines(province_scope_lines(cur["province_text"])),
            "", "", ""]
        lines.append("\t".join(rows_out))

        report.append({
            "lane": lane, "head": head, "delta": delta, "delta_raw": raw,
            "r49_pin": pin_commit, "r49_class": pin,
            "description": cur["description"],
            "cells": (cur["skill_file"], cur["names_kotoba"], cur["arbitration"]),
            "problems": problems, "none_rule_fires": none_rule_fires,
            "rederive_diffs": diffs,
            "carry": carry_forward(chk, repo, lane, head, old_row),
            "r49_quote": old_row["quote"].strip(),
            "r49_path_line": old_row["path:line"].strip(),
        })
        print("[%s] %s %s | %s | %s | %s | delta %s"
              % (lane, fz["branch"], head[:12], cur["skill_file"],
                 cur["names_kotoba"], cur["arbitration"], delta))

    for name, line in zip(["header"] + MY_LANES, lines):
        for cell in line.split("\t"):
            assert "\t" not in cell
            if "|" in cell:
                print("WARN pipe in %s cell: %r" % (name, cell[:60]))
    out_path.write_text("\n".join(lines) + "\n", encoding="utf-8")

    # The merge seat's 8-column join file: quote_at / quote come from the
    # sibling scouts' JSON (provenance recorded in the report), every other
    # cell is this seat's derivation.
    scout_root = Path(OUT_DIR).parent
    scout_map = {
        "audio": "ScoutSibAudioGamedev2dR74/audio.json",
        "game-dev-2d": "ScoutSibAudioGamedev2dR74/game-dev-2d.json",
        "chousa": "ScoutSibChousaKagiR74/chousa.json",
        "kagi": "ScoutSibChousaKagiR74/kagi.json",
        "game-dev-3d": "ScoutSibGamedev3dLoreR74/game-dev-3d.json",
    }
    merge_lines = ["\t".join(["lane", "branch", "commit", "skill_file",
                               "names_kotoba", "arbitration", "quote_at",
                               "quote"])]
    for lane in MY_LANES:
        r = cells_row[lane]
        src = scout_root / scout_map[lane]
        if src.is_file():
            j = json.loads(src.read_text(encoding="utf-8"))
            quote_at = j.get("quote_path_line", "")
            quote = j.get("quote", "").replace("|", "")
        else:
            quote_at, quote = "", ""
        cells = [lane, r["branch"], r["head40"], r["skill_file"],
                 r["names_kotoba"], r["arbitration"], quote_at, quote]
        for cell in cells:
            assert "\t" not in cell and "|" not in cell, (lane, cell)
        merge_lines.append("\t".join(cells))
    merge_path = Path(OUT_DIR) / "rows.tsv"
    merge_path.write_text("\n".join(merge_lines) + "\n", encoding="utf-8")
    print("wrote merge-schema %s" % merge_path)

    print("\n-- checker cell validation (mechanical_findings, class adjacent) --")
    for r in report:
        print("%s: %s" % (r["lane"], "OK" if not r["problems"] else r["problems"]))
    print("\n-- checker `none` rule (does a `none` class fire?) --")
    for r in report:
        print("%s: %s" % (r["lane"], "fire" if r["none_rule_fires"] else "clear"))
    print("\n-- r49 re-derivation --")
    for r in report:
        print("%s: %s%s" % (r["lane"], "match" if not r["rederive_diffs"] else "MISMATCH",
                            "" if not r["rederive_diffs"] else " " + "; ".join(r["rederive_diffs"])))
    print("\nREDERIVE_ALL_MATCH=%s" % ("yes" if rederive_ok else "no"))
    print("\n-- r49 quote carry-forward at the freeze head --")
    for r in report:
        print("%s (%s): %s" % (r["lane"], r["r49_path_line"], r["carry"]))
    print("\n-- delta raw shortstat --")
    for r in report:
        print("%s (%s -> %s): %s" % (r["lane"], r["r49_pin"][:12], r["head"][:12],
                                     r["delta_raw"] or "(empty)"))


if __name__ == "__main__":
    main()
