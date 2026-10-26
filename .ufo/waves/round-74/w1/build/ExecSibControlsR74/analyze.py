#!/usr/bin/env python3
"""ExecSibControlsR74 analysis: per-lane facts at the frozen fleet heads.

Read-only git against the sibling lane repos.  Prints a TSV and a JSON blob.
"""
import json
import re
import subprocess
import sys
from pathlib import Path

FLEET = Path("/home/vgpnk/Projects/shokunin")
LANE = FLEET / "kotoba-shokunin"
BASE = "1e03d1991bc02281b00a5b7a5e00c9d5d5d72908"
FREEZE = LANE / ".ufo/waves/round-74/receipts/sibling-heads-freeze.tsv"
CENSUS = LANE / "corpus/knowledge/sibling-overlap-census-round49.md"

sys.path.insert(0, str(Path(__file__).parent))
import check_sibling_census_base as base  # noqa: E402


def git(repo, *args):
    p = subprocess.run(["git", "-C", str(repo)] + list(args),
                       capture_output=True, text=True)
    return p.returncode, p.stdout, p.stderr


def read_freeze():
    rows = {}
    for line in FREEZE.read_text(encoding="utf-8").splitlines():
        if not line.strip() or line.startswith("#"):
            continue
        parts = line.split("\t")
        lane, branch, head, skill_blob, prov_blob = parts[:5]
        rows[lane] = {"branch": branch, "head40": head,
                      "skill_blob": skill_blob, "province_blob": prov_blob}
    return rows


def read_census_rows():
    text = CENSUS.read_text(encoding="utf-8")
    out = {}
    for line in text.splitlines():
        if not re.match(r"\| [a-z0-9-]+ \| (main|master) \| [0-9a-f]{40} \|", line):
            continue
        cells = base.split_row(line)
        # strip the empty first/last cells produced by the leading/trailing pipe
        if cells and cells[0] == "":
            cells = cells[1:]
        if cells and cells[-1] == "":
            cells = cells[:-1]
        assert len(cells) == 9, (len(cells), line[:80])
        out[cells[0]] = cells
    return out


def shortstat(lane, pin, head):
    rc, out, err = git(FLEET / (lane + "-shokunin"),
                       "diff", "--shortstat", pin, head, "--", "SKILL.md", "PROVINCE.md")
    if rc != 0:
        return "ERR:" + err.strip()
    text = " ".join(out.split())
    if not text:
        return "none"
    m = re.search(r"(\d+) files? changed(?:, (\d+) insertions?\(\+\))?"
                  r"(?:, (\d+) deletions?\(-\))?", text)
    return "+%d/-%d" % (int(m.group(2) or 0), int(m.group(3) or 0)) if m else "ERR"


def find_quote(repo, head, path, quote):
    """Locate the collapsed quote in `path` at `head`; return (line, ok).

    Single lines first, then windows of 2..6 consecutive lines (a folded
    PROVINCE.md paragraph carries a sentence across physical lines).
    """
    rc, out, err = git(repo, "show", "%s:%s" % (head, path))
    if rc != 0:
        return None, False
    lines = out.splitlines()
    q = base.collapse(quote)
    if not q:
        return None, False
    for width in range(1, 7):
        for start in range(0, len(lines) - width + 1):
            if q in base.collapse(" ".join(lines[start:start + width])):
                return start + 1, True
    return None, False


def kotoba_hits(repo, head):
    rc, out, err = git(repo, "grep", "-w", "-i", "-n", "kotoba", head, "--",
                       "SKILL.md", "PROVINCE.md")
    if rc == 2:
        return {"error": err.strip()}
    lines = [l for l in out.splitlines() if l.strip()]
    return {"count": len(lines), "lines": lines[:6]}


def main():
    freeze = read_freeze()
    rows = read_census_rows()
    result = {}
    for lane, fz in freeze.items():
        repo = FLEET / (lane + "-shokunin")
        cells = rows[lane]
        values = dict(zip(base.CENSUS_CELL_NAMES, cells))
        pin = values["commit"].strip()
        head = fz["head40"]
        quote = base.strip_wrapping(values["quote"])
        path, cited = base.split_path_line(values["path:line"])
        # relocated quote at the head, in the same file the r49 row cited
        new_line, found = find_quote(repo, head, path, quote)
        # mechanical cells as the r49 row carries them, checked at the head
        mech = base.mechanical_findings(
            repo, head, values, lane, set(freeze) | {"kotoba"},
            values["classification"].strip().lower())
        # what the mechanical cells WOULD be at the head (for the report only)
        skill_text, _ = base.git_show(repo, head, "SKILL.md")
        want = {}
        if skill_text is None:
            want["path"] = "NONE"
            want["names kotoba"] = "no SKILL.md"
            want["arbitration"] = "no SKILL.md"
        else:
            desc = base.description_of(skill_text)
            want["path"] = "SKILL.md"
            want["names kotoba"] = "yes" if base.token_in("kotoba", desc) else "no"
            named = sorted(n for n in (set(freeze) | {"kotoba"})
                           if n != lane and base.token_in(n, desc))
            want["arbitration"] = ("yes: " + ", ".join(named)) if named else "no"
        delta = shortstat(lane, pin, head)
        result[lane] = {
            "branch": fz["branch"], "pin": pin, "head40": head,
            "classification": values["classification"].strip(),
            "cited": values["path:line"], "quote": quote,
            "quote_found_at_head": found, "quote_new_line": new_line,
            "mechanical_problems_at_head": mech,
            "mechanical_cells_at_head": want,
            "mechanical_cells_stale": {k: values[k] for k in
                                       ("path", "names kotoba", "arbitration")},
            "delta": delta,
            "kotoba_hits_at_head": kotoba_hits(repo, head),
            "pin_equals_head": pin == head,
        }
    print(json.dumps(result, indent=1, ensure_ascii=False))


if __name__ == "__main__":
    main()
