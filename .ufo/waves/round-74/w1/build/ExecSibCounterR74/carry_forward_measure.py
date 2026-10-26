#!/usr/bin/env python3
"""Measure the round-74 C2 carry-forward worlds on the real fleet (replayable).

The round-74 plan § C2 names one shortcut world that is "measured and
reported, not asserted below 20": the round-49 entry with every commit cell
bumped to the frozen heads and the mechanical cells recomputed.  This script
builds that world (and two neighbours) in a throwaway `--shared` clone of the
lane and prints what `check_sibling_reread.py` scores for each.

    python3 -B carry_forward_measure.py [--lane DIR] [--clone-rev REV]

Worlds, each committed on top of the previous one inside the clone:

  W_d   entry rows bumped + mechanical cells + delta recomputed, PROVINCE.md
        left at the round-49 pins            -> conjunct (d) decides
  W_v1  entry rows bumped, delta cells claimed `none`, round-49 mechanical
        cells kept as written, PROVINCE.md bumped -> conjuncts (a), (c), (e)
  W_cf  entry rows bumped, mechanical cells and delta recomputed, PROVINCE.md
        bumped (the plan's carry-forward world)  -> conjunct (e) alone

Writes only inside its own temporary clone; the lane repository is read with
git only.  Stdlib only.
"""

from __future__ import annotations

import argparse
import contextlib
import io
import subprocess
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import check_sibling_reread as C  # noqa: E402  (sibling draft in this directory)

LANE = Path("/home/vgpnk/Projects/shokunin/kotoba-shokunin")
CLONE_REV = "329e7d91d7d750031c35d264f0e34af1d0ce8385"


def run_git(repo, *args):
    proc = subprocess.run(["git", "-C", str(repo)] + list(args),
                          stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if proc.returncode != 0:
        raise RuntimeError("git %s failed in %s: %s"
                           % (" ".join(args), repo,
                              proc.stderr.decode("utf-8", "replace").strip()))
    return proc.stdout.decode("utf-8", "replace")


def mechanical_cells(lane, base, frozen, base_pins, fleet):
    """(skill file, names kotoba, arbitration, delta) recomputed at the head."""
    head = frozen[lane]["head"]
    repo = fleet / (lane + C.LANE_SUFFIX)
    skill_text, _ = C.git_show_text(repo, head, C.SKILL_PATH)
    if skill_text is None:
        skill, names, arbitration = "NONE", "no SKILL.md", "no SKILL.md"
    else:
        description = base.description_of(skill_text)
        skill = C.SKILL_PATH
        names = "yes" if base.token_in(C.SELF_LANE, description) else "no"
        lanes = base.fleet_lanes(fleet) | {C.SELF_LANE}
        named = sorted(n for n in lanes
                       if n != lane and base.token_in(n, description))
        arbitration = ("yes: " + ", ".join(named)) if named else "no"
    delta = C._recompute_delta(repo, lane, base_pins.get(lane), head, C.PINS)[0]
    return skill, names, arbitration, delta


def r49_rows(base, lane_dir, frozen):
    text = (lane_dir / "corpus/knowledge/sibling-overlap-census-round49.md").read_text()
    rows = {}
    for line in text.splitlines():
        if not line.startswith("| "):
            continue
        cells = base.split_row(line)
        if len(cells) == 9 and base.normalize_lane(cells[0]) in frozen:
            rows[base.normalize_lane(cells[0])] = cells
    return rows


def entry_text(rows, frozen, world):
    header = ("| lane | branch | commit | skill file | classification | names "
              "kotoba | arbitration | scope quote at | scope quote | delta |")
    out = ["# carry-forward world (%s)" % world, "", header,
           "|" + "|".join("---" for _ in range(C.CENSUS_COLUMNS)) + "|"]
    for lane in sorted(frozen):
        cells = rows[lane]
        if isinstance(cells, dict):
            skill, names, arbitration, delta = (cells["skill"], cells["names"],
                                                cells["arbitration"], cells["delta"])
        else:
            skill, names, arbitration = cells[3], cells[5], cells[6]
            delta = "none"
        quote_cells = cells if isinstance(cells, list) else cells["r49"]
        out.append("| %s | %s | %s | %s | %s | %s | %s | %s | %s | %s |"
                   % (lane, frozen[lane]["branch"], frozen[lane]["head"],
                      skill, quote_cells[4], names, arbitration,
                      quote_cells[7], quote_cells[8], delta))
    return "\n".join(out) + "\n"


def province_bumped(text, rows, frozen):
    for lane in sorted(frozen):
        cells = rows[lane]
        pin = cells["r49"][2] if isinstance(cells, dict) else cells[2]
        old = "| %s | %s | %s |" % (lane, (cells["r49"][4] if isinstance(cells, dict) else cells[4]), pin)
        new = "| %s | %s | %s |" % (lane, (cells["r49"][4] if isinstance(cells, dict) else cells[4]),
                                    frozen[lane]["head"])
        if old not in text:
            raise RuntimeError("PROVINCE.md has no row for %s at its round-49 pin" % lane)
        text = text.replace(old, new)
    return text


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--lane", default=str(LANE))
    parser.add_argument("--clone-rev", default=CLONE_REV)
    parser.add_argument("--fleet", default=C.DEFAULT_FLEET)
    args = parser.parse_args(argv)
    lane_dir = Path(args.lane).expanduser().resolve()
    fleet = Path(args.fleet).expanduser().resolve()

    with tempfile.TemporaryDirectory(prefix="carry-forward-") as tmp:
        clone = Path(tmp) / "lane"
        run_git(Path(tmp), "clone", "--shared", "-q", str(lane_dir), str(clone))
        for key, value in (("user.name", "kotoba carry-forward seat"),
                           ("user.email", "carry@example.invalid"),
                           ("commit.gpgsign", "false")):
            run_git(clone, "config", key, value)
        run_git(clone, "checkout", "-q", args.clone_rev)

        with tempfile.TemporaryDirectory() as work:
            base = C.load_base_checker(lane_dir, C.PINS, work)
            frozen, _ = C.read_freeze(lane_dir, None, C.PINS)
            base_province, _ = C.git_show_text(lane_dir, C.BASE_REV, C.PROVINCE_PATH)
            base_pins = C.province_rows(base, base_province)

        r49 = r49_rows(base, lane_dir, frozen)
        recomputed = {lane: dict(zip(("skill", "names", "arbitration", "delta"),
                                     mechanical_cells(lane, base, frozen,
                                                      base_pins, fleet)),
                                 r49=r49[lane])
                      for lane in frozen}
        claimed_none = {lane: dict((k, recomputed[lane][k]) for k in
                                   ("skill", "names", "arbitration"))
                        | {"delta": "none", "r49": r49[lane]}
                        for lane in frozen}
        base_province_text = (clone / C.PROVINCE_PATH).read_text()
        state = {"province": base_province_text}

        def commit(message):
            run_git(clone, "add", "-A")
            run_git(clone, "commit", "-q", "-m", message)

        def measure(tag):
            buffer = io.StringIO()
            with contextlib.redirect_stdout(buffer), \
                    contextlib.redirect_stderr(io.StringIO()):
                code = C.main(["--rev", "HEAD", "--repo", str(clone),
                               "--fleet", str(fleet)])
            text = buffer.getvalue()
            ok = [line.split()[1].rstrip(":")
                  for line in text.splitlines()
                  if line.startswith("lane ") and line.endswith(": ok")]
            print("%s: exit %d | %s" % (tag, code, text.strip().splitlines()[-1]))
            print("  ok lanes: %s" % ", ".join(ok))
            for line in text.splitlines():
                if line.startswith("lane ") and "FAIL" in line:
                    print("  %s" % line)
            return code, text

        (clone / C.ENTRY_PATH).parent.mkdir(parents=True, exist_ok=True)

        # W_d: recomputed entry, PROVINCE.md still at the round-49 pins
        (clone / C.ENTRY_PATH).write_text(
            entry_text(recomputed, frozen, "recomputed entry, PROVINCE unchanged"),
            encoding="utf-8")
        (clone / C.PROVINCE_PATH).write_text(base_province_text, encoding="utf-8")
        commit("carry-forward entry, PROVINCE unchanged")
        measure("W_d  (entry recomputed, PROVINCE unchanged)")

        # W_v1: the round-49 mechanical cells, delta claimed none, PROVINCE bumped
        (clone / C.ENTRY_PATH).write_text(
            entry_text(claimed_none, frozen, "round-49 cells, delta none"),
            encoding="utf-8")
        (clone / C.PROVINCE_PATH).write_text(
            province_bumped(base_province_text, recomputed, frozen), encoding="utf-8")
        commit("round-49 cells, delta none, PROVINCE bumped")
        measure("W_v1 (round-49 cells, delta none, PROVINCE bumped)")

        # W_cf: entry and PROVINCE both recomputed (the plan's carry-forward world)
        (clone / C.ENTRY_PATH).write_text(
            entry_text(recomputed, frozen, "recomputed entry and PROVINCE"),
            encoding="utf-8")
        commit("carry-forward entry and PROVINCE")
        measure("W_cf (entry and PROVINCE recomputed)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
