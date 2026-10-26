#!/usr/bin/env python3
"""validate_rows.py -- run the BASE checker's own row checks over the five
ExecSibRowsAR74 rows, filled with the sibling scouts' proposed quote /
path:line / classification, in a scratch census.

The lane-set check is expected to fire (15 lanes are other seats' rows); every
other failure is a real finding about a cell.  Run with --province to see which
`## Adjacent` commit cells the L1 still has to bump.

Usage: validate_rows.py <checker.py> <rows.tsv> <scout-build-root> [--province]
"""

import importlib.util
import json
import sys
from pathlib import Path

BASE_PROVINCE = Path("/tmp/k74w1-ExecSibRowsAR74.YM59/base-province.md")
FLEET = Path("/home/vgpnk/Projects/shokunin")

SCOUT_JSON = {
    "audio": "ScoutSibAudioGamedev2dR74/audio.json",
    "game-dev-2d": "ScoutSibAudioGamedev2dR74/game-dev-2d.json",
    "chousa": "ScoutSibChousaKagiR74/chousa.json",
    "kagi": "ScoutSibChousaKagiR74/kagi.json",
    "game-dev-3d": "ScoutSibGamedev3dLoreR74/game-dev-3d.json",
}

HEADER = ("| lane | branch | commit | skill file | classification | names kotoba "
          "| arbitration | scope quote at | scope quote |")


def load_checker(path):
    spec = importlib.util.spec_from_file_location("base_census", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def main():
    checker, rows_tsv, scouts = Path(sys.argv[1]), Path(sys.argv[2]), Path(sys.argv[3])
    use_province = "--province" in sys.argv
    chk = load_checker(checker)

    rows = {}
    with rows_tsv.open(encoding="utf-8") as fh:
        header = fh.readline().rstrip("\n").split("\t")
        for line in fh:
            vals = line.rstrip("\n").split("\t")
            rows[vals[0]] = dict(zip(header, vals))

    out = ["# scratch census (ExecSibRowsAR74 validation)", "", HEADER,
           "|---|---|---|---|---|---|---|---|---|"]
    for lane in ("audio", "chousa", "game-dev-2d", "game-dev-3d", "kagi"):
        r = rows[lane]
        s = json.loads((scouts / SCOUT_JSON[lane]).read_text(encoding="utf-8"))
        cls = s["proposed_classification"].split(" ")[0]
        quote = s["quote"]
        cells = [lane, r["branch"], r["commit40"], r["skill_file"], cls,
                 r["names_kotoba"], r["arbitration"], s["quote_path_line"],
                 '"%s"' % quote.replace('"', '\\"')]
        out.append("| " + " | ".join(cells) + " |")
    census = Path("/tmp/k74w1-ExecSibRowsAR74.YM59/scratch-census.md")
    census.write_text("\n".join(out) + "\n", encoding="utf-8")
    print("scratch census: %s" % census)
    print("\n".join(out[4:]))

    province = BASE_PROVINCE if use_province else None
    res = chk.check_census(census, FLEET, province)
    print("\nrows %d verified %d  province_rows %d matched %d"
          % (res["rows"], res["verified"], res["province_rows"],
             res["province_matched"]))
    print("failures %d" % len(res["failures"]))
    for f in res["failures"]:
        print("  - " + f)


if __name__ == "__main__":
    main()
