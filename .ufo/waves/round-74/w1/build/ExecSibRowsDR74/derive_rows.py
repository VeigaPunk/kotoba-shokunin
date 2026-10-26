#!/usr/bin/env python3
"""derive_rows.py -- round-74 C2 mechanical row cells for five sibling lanes.

Seat: ExecSibRowsDR74.  Read-only against the fleet.  Every derivation below
calls the BASE checker's own functions (imported from a scratch copy of
`git show 1e03d199...:verifiers/check_sibling_census.py`); nothing about the
row shape, the description parse, the token rule or the arbitration rule is
re-implemented here.

Usage:
    python3 derive_rows.py <lane> [<lane> ...]        # self-contained
    python3 derive_rows.py --base=DIR <lane> [...]    # reuse a scratch copy

The base checker is materialised at run time with
`git -C <lane root> show <BASE_REV>:verifiers/check_sibling_census.py` into a
throwaway temp dir (removed on exit); `--base=DIR` reuses a copy already on
disk.  sha256 of the copy used: 2f9d8a88b1d3dd8562455006d5ea89ec02546a1ecb9d023f327d88e5502eedc7
(identical to the measured-revision file: `git diff <BASE_REV> 329e7d91 --
verifiers/check_sibling_census.py` is empty).

Writes beside this script:
    rows.tsv         the merge seat's schema (ExecSibMergeR74): lane, branch,
                     commit, skill_file, names_kotoba, arbitration, quote_at,
                     quote -- the last two EMPTY (the ScoutSib* seats own the
                     quote; merge joins)
    mechanics.tsv    the same rows with every mechanical cell, including the
                     empty classification cell and the delta the entry needs
    scopelines.tsv   candidate scope-statement lines a scout may quote
    r49-recheck.tsv  the same derivation at the round-49 pin, against the r49
                     census cells (self-falsification of this script)
    freeze-check.tsv the frozen head/blob triples against today's sibling git
"""

from __future__ import annotations

import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

FLEET = Path("/home/vgpnk/Projects/shokunin")
LANE = "kotoba"
BASE_REV = "1e03d1991bc02281b00a5b7a5e00c9d5d5d72908"
LANE_ROOT = Path("/home/vgpnk/Projects/shokunin/kotoba-shokunin")
FREEZE = LANE_ROOT / ".ufo/waves/round-74/receipts/sibling-heads-freeze.tsv"
R49_CENSUS = LANE_ROOT / "corpus/knowledge/sibling-overlap-census-round49.md"
OUT_DIR = Path(__file__).resolve().parent

ROW_COLUMNS = ("lane", "branch", "commit40", "skill_file", "classification",
               "names_kotoba", "arbitration", "path_line", "quote", "delta",
               "kotoba_hits_skill", "kotoba_hits_province", "scope_lines",
               "none_rule_base", "none_rule_plan_e",
               "delta_skill", "delta_province")


def git(repo, *args):
    proc = subprocess.run(["git", "-C", str(repo)] + list(args),
                          stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return proc.returncode, proc.stdout.decode("utf-8", "replace"), \
        proc.stderr.decode("utf-8", "replace")


def read_freeze():
    rows = {}
    for line in FREEZE.read_text(encoding="utf-8").splitlines():
        if not line.strip() or line.startswith("#"):
            continue
        lane, branch, head, skill_blob, province_blob = line.split("\t")
        rows[lane] = {"branch": branch, "head": head,
                      "skill_blob": skill_blob, "province_blob": province_blob}
    return rows


def r49_pins(base):
    """The round-49 pin per lane, from the BASE revision's PROVINCE.md table."""
    rc, text, err = git(LANE_ROOT, "show", "%s:PROVINCE.md" % BASE_REV)
    if rc != 0:
        raise SystemExit("git show base PROVINCE.md failed: %s" % err.strip())
    body = base.extract_adjacent_section(text)
    if body is None:
        raise SystemExit("base PROVINCE.md has no ## Adjacent section")
    table = base.select_province_table(base.parse_blocks(body))
    if table is None:
        raise SystemExit("base PROVINCE.md ## Adjacent table not found")
    pins = {}
    for _line, cells in table["rows"]:
        if len(cells) != base.PROVINCE_COLUMNS:
            continue
        pins[base.normalize_lane(cells[0])] = {
            "classification": cells[1].strip().lower(),
            "commit": cells[2].strip().lower()}
    return pins


def r49_cells():
    """The round-49 census row cells for every lane, keyed by lane."""
    text = R49_CENSUS.read_text(encoding="utf-8")
    import importlib
    base = importlib.import_module("base_checker")
    blocks = base.parse_blocks(text.splitlines())
    table = base.select_census_table(blocks)
    rows = {}
    for _line, cells in table["rows"]:
        if len(cells) != base.CENSUS_COLUMNS:
            continue
        values = dict(zip(base.CENSUS_CELL_NAMES, cells))
        lane = base.normalize_lane(values["lane"])
        rows[lane] = {k: v.strip() for k, v in values.items()}
    return rows


def description_span(skill_text):
    """(start_line, end_line) of the frontmatter description, 1-based, or None.

    End line follows the BASE parser's value boundary: the value runs from the
    `description:` line to the last non-blank line before the next column-0
    line (the base lookahead is `(?=^\\S|\\Z)`).
    """
    if not skill_text or not skill_text.startswith("---"):
        return None
    lines = skill_text.splitlines()
    start = None
    for index, line in enumerate(lines):
        if line.startswith("description:"):
            start = index
            break
    if start is None:
        return None
    end = start
    for index in range(start + 1, len(lines)):
        line = lines[index]
        if line and not line[0].isspace():
            break
        if line.strip():
            end = index
    return start + 1, end + 1


HEADING_DECL = re.compile(r"\A#{1,6}\s+(?:Domain|Owns)\b", re.I)
BOLD_DECL = re.compile(
    r"\A(?:\*\*)?(?:Domain|Owns)(?:\s*\([^)]{0,60}\))?\s*:(?:\*\*)?", re.I)
STRUCTURAL = ("#", "-", "*", "|", ">")


def province_scope_blocks(province_text):
    """[(start_line, end_line)] of the PROVINCE `Domain`/`Owns` blocks.

    Starts come from a column-0 declaration: a `## Owns` heading, or
    `**Domain:**` / `Owns:` / `**Owns (surfaces):**`.  A heading block keeps
    its following list lines up to the next heading or blank line (the bullets
    are the ownership content); a text declaration keeps its wrapped prose --
    including wraps that begin at column 0 -- up to a blank line or the next
    structural line.  An indented sentence that merely begins with `owns` is
    not a declaration.  Line numbers are 1-based, the counter's path:line path.
    """
    if province_text is None:
        return []
    lines = province_text.splitlines()
    blocks = []
    for index, line in enumerate(lines):
        heading = bool(HEADING_DECL.match(line))
        if not heading and not BOLD_DECL.match(line):
            continue
        end = index
        for probe in range(index + 1, len(lines)):
            candidate = lines[probe]
            if heading:
                if candidate.lstrip().startswith("#"):
                    break
                if candidate.strip():
                    end = probe
                continue
            if not candidate.strip():
                break
            if candidate.lstrip().startswith(STRUCTURAL):
                break
            if HEADING_DECL.match(candidate) or BOLD_DECL.match(candidate):
                break
            end = probe
        blocks.append((index + 1, end + 1))
    return blocks


def shortstat_delta(repo, old, new):
    rc, out, err = git(repo, "diff", "--shortstat", old, new,
                       "--", "SKILL.md", "PROVINCE.md")
    if rc != 0:
        return "error: %s" % err.strip().splitlines()[:1]
    out = out.strip()
    if not out:
        return "none"
    ins = dels = 0
    for part in out.split(","):
        part = part.strip()
        number, _, what = part.partition(" ")
        if not number.isdigit():
            continue
        if "insertion" in what:
            ins = int(number)
        elif "deletion" in what:
            dels = int(number)
    return "+%d/-%d" % (ins, dels)


def numstat(repo, old, new, path):
    """(insertions, deletions) for one path, or ('-', '-') when unchanged."""
    rc, out, _err = git(repo, "diff", "--numstat", old, new, "--", path)
    if rc != 0 or not out.strip():
        return "-", "-"
    ins, dels, _name = out.strip().split("\t")
    return ins, dels


def kotoba_hits(text):
    """1-based line numbers whose text carries the whole word kotoba."""
    if text is None:
        return []
    return [number for number, line in enumerate(text.splitlines(), 1)
            if base.token_in(LANE, line)]


def load_base(directory):
    sys.path.insert(0, str(directory))
    import base_checker as module
    return module


def main(argv):
    global base
    lanes = []
    base_dir = None
    for arg in argv[1:]:
        if arg.startswith("--base="):
            base_dir = Path(arg.split("=", 1)[1])
        elif Path(arg).is_dir():
            base_dir = Path(arg)
        else:
            lanes.append(arg)
    if not lanes:
        raise SystemExit(__doc__)
    cleanup = None
    if base_dir is None:
        cleanup = Path(tempfile.mkdtemp(prefix="k74w1-ExecSibRowsDR74.base."))
        rc, text, err = git(LANE_ROOT, "show",
                            "%s:verifiers/check_sibling_census.py" % BASE_REV)
        if rc != 0:
            raise SystemExit("cannot read the base checker: %s" % err.strip())
        (cleanup / "base_checker.py").write_text(text, encoding="utf-8")
        base_dir = cleanup
    base = load_base(base_dir)
    freeze = read_freeze()
    pins = r49_pins(base)
    census49 = r49_cells()
    all_lanes = base.fleet_lanes(FLEET) | {base.SELF_LANE}

    row_lines = ["\t".join(ROW_COLUMNS)]
    scope_lines = ["lane\tpath\tline\theading\ttext"]
    recheck = ["lane\tcell\tround49\trederived\tmatch"]
    freeze_check = ["lane\tbranch\tfield\tfrozen\tgit\tmatch"]

    for lane in lanes:
        entry = freeze[lane]
        repo = base.repo_dir_for(lane, FLEET)
        head, branch = entry["head"], entry["branch"]

        # --- freeze integrity (freshness: the freeze file is a claim too) ---
        for field, blob in (("SKILL.md", entry["skill_blob"]),
                            ("PROVINCE.md", entry["province_blob"])):
            rc, out, _err = git(repo, "rev-parse", "%s:%s" % (head, field))
            actual = out.strip() if rc == 0 else "-"
            want = blob
            freeze_check.append("%s\t%s\t%s\t%s\t%s\t%s"
                                % (lane, branch, field, want, actual,
                                   "yes" if want == actual else "NO"))

        skill_text, skill_err = base.git_show(repo, head, "SKILL.md")
        province_text, province_err = base.git_show(repo, head, "PROVINCE.md")
        description = base.description_of(skill_text)

        if skill_text is None:
            # The base checker's no-skill branch (mechanical_findings): the
            # three cells are the literal sentinels, not `no`/`none`.
            skill_file, names, arbitration = "NONE", base.NO_SKILL, base.NO_SKILL
        else:
            skill_file = "SKILL.md"
            names = "yes" if base.token_in(base.SELF_LANE, description) else "no"
            named = sorted(n for n in all_lanes
                           if n != lane and base.token_in(n, description))
            arbitration = ("yes: " + ", ".join(named)) if named else "no"

        hits_skill = kotoba_hits(skill_text)
        hits_province = kotoba_hits(province_text)
        # The base checker's none rule: description + whole PROVINCE.md.
        none_rule_base = ("blocked: kotoba named"
                          if base.token_in(base.SELF_LANE, description)
                          or (province_text is not None
                              and base.token_in(base.SELF_LANE, province_text))
                          else "ok for none")
        # The plan's literal (e) wording: whole SKILL.md or whole PROVINCE.md.
        none_rule_plan = ("blocked: kotoba named"
                          if hits_skill or hits_province else "ok for none")

        pin = pins[lane]["commit"]
        delta = shortstat_delta(repo, pin, head)
        dskill = numstat(repo, pin, head, "SKILL.md")
        dprov = numstat(repo, pin, head, "PROVINCE.md")

        # --- what a scout may quote: description lines + PROVINCE Domain/Owns ---
        span = description_span(skill_text)
        cells = []
        if span is not None:
            cells.append("SKILL.md:%d-%d" % span)
            skill_lines = skill_text.splitlines()
            span_text = base.BLOCK_SCALAR.sub(
                "", base.collapse(" ".join(skill_lines[span[0] - 1:span[1]])))
            span_text = span_text.split(":", 1)[1].strip() if ":" in span_text \
                else span_text
            if description and span_text != description:
                print("SPAN MISMATCH %s: %r != %r"
                      % (lane, span_text, description), file=sys.stderr)
            for number in range(span[0], span[1] + 1):
                scope_lines.append("%s\tSKILL.md\t%d\tno\t%s"
                                   % (lane, number, skill_lines[number - 1]))
        province_blocks = province_scope_blocks(province_text)
        if province_blocks:
            province_lines = province_text.splitlines()
            cells.append("PROVINCE.md:" + ",".join(
                "%d-%d" % (start, end) for start, end in province_blocks))
            for start, end in province_blocks:
                for number in range(start, end + 1):
                    text = province_lines[number - 1]
                    if not text.strip():
                        continue
                    scope_lines.append(
                        "%s\tPROVINCE.md\t%d\t%s\t%s"
                        % (lane, number,
                           "yes" if text.lstrip().startswith("#") else "no",
                           text))
        scope_cell = ";".join(cells) if cells else "none"

        # --- the base checker's own verdict on these cells ---
        values = {"path": skill_file, "names kotoba": names,
                  "arbitration": arbitration}
        problems = base.mechanical_findings(repo, head, values, lane,
                                            all_lanes, "adjacent")

        row_lines.append("\t".join([
            lane, branch, head, skill_file, "", names, arbitration, "", "",
            delta,
            "; ".join("SKILL.md:%d" % n for n in hits_skill) or "-",
            "; ".join("PROVINCE.md:%d" % n for n in hits_province) or "-",
            scope_cell, none_rule_base, none_rule_plan,
            ("none" if dskill[0] == "-" else "+%s/-%s" % dskill),
            ("none" if dprov[0] == "-" else "+%s/-%s" % dprov)]))
        if problems:
            print("MECHANICAL MISMATCH %s: %s" % (lane, problems),
                  file=sys.stderr)

        # --- self-falsification: the same derivation at the round-49 pin ---
        r49 = census49[lane]
        old_skill, _ = base.git_show(repo, pin, "SKILL.md")
        if old_skill is None:
            old_skill_file = "NONE"
            old_names = old_arb = base.NO_SKILL
        else:
            old_desc = base.description_of(old_skill)
            old_skill_file = "SKILL.md"
            old_names = "yes" if base.token_in(base.SELF_LANE, old_desc) else "no"
            old_named = sorted(n for n in all_lanes
                               if n != lane and base.token_in(n, old_desc))
            old_arb = ("yes: " + ", ".join(old_named)) if old_named else "no"
        derived = {"path": old_skill_file, "names kotoba": old_names,
                   "arbitration": old_arb}
        for cell, key in (("path", "path"), ("names kotoba", "names kotoba"),
                          ("arbitration", "arbitration")):
            recorded = base.strip_wrapping(r49[key]).strip()
            got = derived[cell]
            same = (recorded.lower() == got.lower())
            recheck.append("%s\t%s\t%s\t%s\t%s"
                           % (lane, cell, recorded, got, "yes" if same else "NO"))
        recheck.append("%s\t%s\t%s\t%s\t%s"
                       % (lane, "commit", r49["commit"], pin,
                          "yes" if r49["commit"].lower() == pin else "NO"))
        # the r49 entry's own quote and classification are re-read, not taken
        recheck.append("%s\t%s\t%s\t%s\t%s"
                       % (lane, "classification", r49["classification"],
                          pins[lane]["classification"],
                          "yes" if r49["classification"]
                          == pins[lane]["classification"] else "NO"))

        # --- has the sibling moved since the freeze? (head ancestry) ---
        rc, out, _err = git(repo, "rev-parse", "refs/heads/%s" % branch)
        now = out.strip() if rc == 0 else "-"
        rc2, _o, _e = git(repo, "merge-base", "--is-ancestor", head, now)
        freeze_check.append("%s\t%s\tbranch-head\t%s\t%s\t%s"
                            % (lane, branch, head, now,
                               "same" if head == now else
                               ("ahead" if rc2 == 0 else "diverged")))

    # rows.tsv: the merge seat's exact schema (ExecSibMergeR74), quote_at and
    # quote empty -- the ScoutSib* seats own the quote.
    merge = ["lane\tbranch\tcommit\tskill_file\tnames_kotoba\tarbitration"
             "\tquote_at\tquote"]
    for line in row_lines[1:]:
        cells = line.split("\t")
        values = dict(zip(ROW_COLUMNS, cells))
        assert "|" not in line and "\t" not in "".join(values.values())
        merge.append("\t".join([values["lane"], values["branch"],
                                 values["commit40"], values["skill_file"],
                                 values["names_kotoba"], values["arbitration"],
                                 "", ""]))
    (OUT_DIR / "rows.tsv").write_text("\n".join(merge) + "\n", encoding="utf-8")
    (OUT_DIR / "mechanics.tsv").write_text("\n".join(row_lines) + "\n",
                                          encoding="utf-8")
    (OUT_DIR / "scopelines.tsv").write_text("\n".join(scope_lines) + "\n",
                                            encoding="utf-8")
    (OUT_DIR / "r49-recheck.tsv").write_text("\n".join(recheck) + "\n",
                                             encoding="utf-8")
    (OUT_DIR / "freeze-check.tsv").write_text(
        "\n".join(freeze_check) + "\n", encoding="utf-8")
    print("\n".join(row_lines))
    print("\n--- r49 recheck mismatches: %d"
          % sum(1 for line in recheck[1:] if line.endswith("\tNO")))
    print("--- freeze mismatches: %d"
          % sum(1 for line in freeze_check[1:] if line.rstrip().endswith("NO")))
    if cleanup is not None:
        shutil.rmtree(cleanup, ignore_errors=True)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
