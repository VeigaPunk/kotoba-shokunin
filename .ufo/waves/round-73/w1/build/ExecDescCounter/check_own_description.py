#!/usr/bin/env python3
"""check_own_description.py -- round-73 C2 (replacement) content counter.

Frozen predicate (plans/round-73-addendum-1.md, the same sentence):

    python3 -B verifiers/check_own_description.py --rev <rev>  ->  prints
    "own-description rules held N of 3", exit 0 when N == 3

At `--rev`, `D` is the frontmatter `description` of `<rev>:SKILL.md`, folded
(every whitespace run -> one space; the value ends at the first column-0 line,
exactly as check_sibling_census.py's `description_of` reads it -- that helper
is copied, not imported, so this counter reads the same bytes the same way).
Rule Ri holds iff:

  R1  the first sentence of `D` (the text before the first `. ` or `: `
      followed by an uppercase letter, else the first 99 characters) is
      between 40 and 99 characters long;
  R2  the first 99 characters of `D` contain the whole words `skill` and
      `prompt` and at least one double-quoted string that is also a member of
      the `Triggers:` list of `D`;
  R3  len(D) <= 1024 and the tree's own
      `python3 -B verifiers/check_sibling_census.py
       corpus/knowledge/sibling-overlap-census-round49.md --province
       PROVINCE.md --skill SKILL.md`
      exits 0, run by this counter from a fleet-shaped sandbox of `<rev>`
      (the census gate is given `--fleet <fleet>`, the same fleet root the
      sandbox is shaped from: every sibling repo in the sandbox parent is a
      symlink to that fleet root's, so the two lane sets are identical by
      construction).

Guard the counter prints but the predicate does not count: the frontmatter
keeps its line count, so every `SKILL.md:<line>` citation after it stays
valid.  Printed as `frontmatter lines <base>-><rev>` plus the inserted and
deleted lines inside the frontmatter block (`git diff -U0 <base> <rev> --
SKILL.md`).  It never changes N or the exit code.

Exit codes: 0 when N == 3; 1 when the revision and sandbox were read and
N < 3; 2 when they could not be read (unknown revision, no SKILL.md, no
census gate or census or PROVINCE.md at the revision, an unbuildable sandbox,
a fleet root that is the lane itself).  Exit 2 prints `could-not-evaluate:`
on stderr and no rule line on stdout, so a cannot-measure never reads as a
verdict.

The fleet root is resolved from an ABSOLUTE repo path (`.resolve()` before
`.parent`): with `--repo .` the naive `Path(".").parent` is `Path(".")`, and
a sandbox built from that fleet root symlinks the lane's own relative entry
names (relative symlink targets resolve against the link's directory, so
every link dangles).  That is the r72 M127 reading, repaired here.
"""

from __future__ import annotations

import argparse
import contextlib
import io
import os
import re
import subprocess
import sys
import tempfile
from pathlib import Path

def _lane_root() -> Path:
    """The lane root: `verifiers/check_*.py` -> two levels up, or the nearest
    ancestor that holds SKILL.md and verifiers/ when this file runs from a
    draft directory (`.ufo/waves/<round>/w1/build/<Seat>/`), so a draft
    measures the lane it is drafted in before it is installed under
    verifiers/.  The installed case is unchanged: parent.parent is the lane.
    """
    here = Path(__file__).resolve()
    direct = here.parent.parent
    if (direct / "SKILL.md").is_file():
        return direct
    for parent in here.parents:
        if (parent / "SKILL.md").is_file() and (parent / "verifiers").is_dir():
            return parent
    return direct


LANE = _lane_root()
BASE = "072048fa8e8a52c707d25f7079772fa317244eb7"
SKILL = "SKILL.md"
CENSUS = "corpus/knowledge/sibling-overlap-census-round49.md"
PROVINCE = "PROVINCE.md"
CENSUS_GATE = "verifiers/check_sibling_census.py"

TOTAL = 3
DESCRIPTION_MAX = 1024
TRUNCATION = 99
FIRST_SENTENCE_MIN = 40
FIRST_SENTENCE_MAX = 99
GATE_TIMEOUT = 280

WS_RUN = re.compile(r"\s+")
# A YAML block-scalar indicator at the head of a `description:` value.
BLOCK_SCALAR = re.compile(r"\A[>|][+-]?\s*")
# A sentence ends at `. ` or at `: ` followed by an uppercase letter.
SENTENCE_END = re.compile(r"\. (?=[A-Z])|: (?=[A-Z])")
QUOTED = re.compile(r'"([^"]*)"')
# `Triggers:` the key, never `Anti-triggers:` (the `-` blocks the lookbehind).
TRIGGERS_HEAD = re.compile(r"(?<![-\w])Triggers:")
TRIGGERS_TAIL = re.compile(r"(?<![-\w])(?:Anti-triggers|Sibling boundary|Note):")
HUNK = re.compile(r"^@@ -(\d+)(?:,(\d+))? \+(\d+)(?:,(\d+))? @@")


class EnvError(Exception):
    """The revision or the sandbox could not be read (exit 2)."""


# --------------------------------------------------------------------------
# readers
# --------------------------------------------------------------------------

def collapse(text: str) -> str:
    """Collapse whitespace runs to a single space; strip the ends."""
    return WS_RUN.sub(" ", text).strip()


def description_of(skill_text: str | None) -> str:
    """The frontmatter `description` value, whitespace-collapsed; '' if none.

    Copied from verifiers/check_sibling_census.py `description_of` (round-50
    critic fix m8): the value ends at ANY column-0 line, not only at one that
    carries a colon, so a YAML comment or a continuation key at column 0 never
    leaks into the value.  The block-scalar indicator (`>`, `|`, chomping) is
    YAML syntax and is dropped.
    """
    if skill_text is None or not skill_text.startswith("---"):
        return ""
    front = skill_text.split("\n---", 1)[0]
    match = re.search(r"^description:(.*?)(?=^\S|\Z)", front, re.S | re.M)
    if not match:
        return ""
    return BLOCK_SCALAR.sub("", collapse(match.group(1))).strip()


def frontmatter_span(skill_text: str) -> tuple[int, int] | None:
    """1-based (first, last) line numbers of the frontmatter block, or None."""
    lines = skill_text.splitlines()
    if not lines or lines[0] != "---":
        return None
    for index in range(1, len(lines)):
        if lines[index] == "---":
            return 1, index + 1
    return None


def first_sentence(description: str) -> str:
    """The text before the first `. `/`: ` + uppercase, else the first 99."""
    match = SENTENCE_END.search(description)
    if match is None:
        return description[:TRUNCATION]
    return description[:match.start()]


def triggers_of(description: str) -> list[str]:
    """The double-quoted strings of the `Triggers:` list of `D`.

    The list runs from `Triggers:` to the next of `Anti-triggers:`,
    `Sibling boundary:` or `Note:` (or the end of `D`): those are the fields
    every lane description puts after the trigger list.
    """
    head = TRIGGERS_HEAD.search(description)
    if head is None:
        return []
    rest = description[head.end():]
    tail = TRIGGERS_TAIL.search(rest)
    if tail is not None:
        rest = rest[:tail.start()]
    return QUOTED.findall(rest)


def whole_word_in(name: str, text: str) -> bool:
    """Whole-token, case-insensitive, hyphen-aware (check_sibling_census's
    `token_in` rule: `SKILL.md` supplies `skill`, `prompts` does not)."""
    return re.search(r"(?<![a-z0-9-])" + re.escape(name) + r"(?![a-z0-9])",
                     text, re.I) is not None


# --------------------------------------------------------------------------
# evaluation
# --------------------------------------------------------------------------

def evaluate(description: str, gate_rc: int | None) -> dict:
    """The three frozen rules over `D`; `gate_rc` None means R3's gate failed."""
    first = first_sentence(description)
    head = description[:TRUNCATION]
    triggers = triggers_of(description)

    r1 = FIRST_SENTENCE_MIN <= len(first) <= FIRST_SENTENCE_MAX

    words_ok = whole_word_in("skill", head) and whole_word_in("prompt", head)
    quoted = QUOTED.findall(head)
    hits = [text for text in quoted if text in triggers]
    r2 = words_ok and bool(hits)

    length_ok = len(description) <= DESCRIPTION_MAX
    r3 = length_ok and gate_rc == 0

    return {
        "first": first,
        "head": head,
        "triggers": triggers,
        "quoted_in_head": quoted,
        "hits": hits,
        "words_ok": words_ok,
        "length_ok": length_ok,
        "r1": r1, "r2": r2, "r3": r3,
        "held": sum(1 for ok in (r1, r2, r3) if ok),
    }


# --------------------------------------------------------------------------
# the sandbox and the tree's own census gate
# --------------------------------------------------------------------------

def git(repo: Path, *args: str) -> subprocess.CompletedProcess:
    return subprocess.run(["git", "-C", str(repo), *args],
                          capture_output=True, text=True)


def _tail(proc: subprocess.CompletedProcess) -> str:
    text = (proc.stderr or proc.stdout or "").strip()
    lines = [line for line in text.splitlines() if line.strip()]
    return lines[-1][:200] if lines else "no output"


def resolve_paths(repo_arg: str, fleet_arg: str | None) -> tuple[Path, Path]:
    """Absolute lane path and its fleet root.

    `.resolve()` BEFORE `.parent`: `--repo .` on a relative path would make
    `Path(".").parent` the lane itself (M127).  The fleet root must exist and
    must not be the lane itself: a sandbox shaped from the lane is not
    fleet-shaped, and its `../` citations can never resolve.
    """
    repo = Path(repo_arg).expanduser().resolve()
    if not repo.is_dir():
        raise EnvError("lane repository not found: %s" % repo)
    fleet = Path(fleet_arg).expanduser().resolve() if fleet_arg else repo.parent
    if not fleet.is_dir():
        raise EnvError("fleet root not found: %s" % fleet)
    if fleet == repo:
        raise EnvError("fleet root %s is the lane itself: a sandbox shaped from "
                       "it is not fleet-shaped (M127)" % fleet)
    top = git(repo, "rev-parse", "--show-toplevel")
    if top.returncode != 0 or top.stdout.strip() != str(repo):
        raise EnvError("lane repository %s is not a git work tree top level"
                       % repo)
    return repo, fleet


def build_sandbox(repo: Path, rev: str, fleet: Path, parent: Path) -> Path:
    """Fleet-shaped sandbox of `rev`: <parent>/kotoba-shokunin plus every fleet
    root entry as a symlink (the construction of check_tip_battery.py)."""
    clone = parent / "kotoba-shokunin"
    proc = subprocess.run(
        ["git", "clone", "--shared", "-q", "--no-checkout", str(repo), str(clone)],
        capture_output=True, text=True)
    if proc.returncode != 0:
        raise EnvError("cannot create the sandbox clone: %s" % _tail(proc))
    for entry in fleet.iterdir():
        if entry.name == "kotoba-shokunin":
            continue
        try:
            (parent / entry.name).symlink_to(entry)
        except OSError as exc:
            raise EnvError("cannot link fleet entry %s: %s" % (entry.name, exc))
    checkout = git(clone, "checkout", "-q", rev)
    if checkout.returncode != 0:
        raise EnvError("cannot check out %s in the sandbox: %s"
                       % (rev, _tail(checkout)))
    return clone


def require_tree(clone: Path, rev: str, path: str) -> None:
    """EnvError when the revision does not carry `path` (a measurement input)."""
    proc = git(clone, "cat-file", "-e", "%s:%s" % (rev, path))
    if proc.returncode != 0:
        raise EnvError("the revision %s carries no %s" % (rev, path))


def census_gate(clone: Path, fleet: Path) -> tuple[int, str]:
    """Run the tree's own census gate from the sandbox clone; (rc, output)."""
    argv = [sys.executable, "-B", CENSUS_GATE, CENSUS,
            "--province", PROVINCE, "--skill", SKILL, "--fleet", str(fleet)]
    try:
        proc = subprocess.run(argv, cwd=str(clone), capture_output=True,
                              text=True, timeout=GATE_TIMEOUT)
    except (OSError, subprocess.TimeoutExpired) as exc:
        raise EnvError("cannot run %s in the sandbox: %s" % (CENSUS_GATE, exc))
    return proc.returncode, (proc.stdout or "") + (proc.stderr or "")


def show(repo: Path, spec: str) -> str | None:
    proc = git(repo, "show", spec)
    return proc.stdout if proc.returncode == 0 else None


def frontmatter_diff(repo: Path, base: str, rev: str) -> dict:
    """Inserted/deleted lines inside the frontmatter block, base -> rev."""
    base_text = show(repo, "%s:%s" % (base, SKILL))
    rev_text = show(repo, "%s:%s" % (rev, SKILL))
    if base_text is None or rev_text is None:
        return {"readable": False, "base_lines": None, "rev_lines": None,
                "inserted": 0, "deleted": 0}
    base_span = frontmatter_span(base_text)
    rev_span = frontmatter_span(rev_text)
    result = {
        "readable": True,
        "base_lines": (base_span[1] - base_span[0] + 1) if base_span else 0,
        "rev_lines": (rev_span[1] - rev_span[0] + 1) if rev_span else 0,
        "inserted": 0,
        "deleted": 0,
    }
    diff = subprocess.run(
        ["git", "-C", str(repo), "diff", "-U0", base, rev, "--", SKILL],
        capture_output=True, text=True)
    if diff.returncode != 0:
        result["readable"] = False
        return result
    base_end = base_span[1] if base_span else 0
    rev_end = rev_span[1] if rev_span else 0
    for line in diff.stdout.splitlines():
        match = HUNK.match(line)
        if match is None:
            continue
        old_start = int(match.group(1))
        old_count = int(match.group(2)) if match.group(2) is not None else 1
        new_count = int(match.group(4)) if match.group(4) is not None else 1
        # A pure insertion (old_count 0) sits after old_start.
        inside_old = old_start < base_end if old_count == 0 else old_start <= base_end
        inside_new = old_start < rev_end if new_count == 0 else old_start <= rev_end
        if inside_old or inside_new:
            result["deleted"] += old_count
            result["inserted"] += new_count
    return result


# --------------------------------------------------------------------------
# the measurement
# --------------------------------------------------------------------------

def measure(repo: Path, rev: str, fleet: Path, base: str) -> int:
    sha = git(repo, "rev-parse", "--verify", "--quiet", "%s^{commit}" % rev)
    if sha.returncode != 0:
        raise EnvError("revision %s is not a commit in %s" % (rev, repo))
    sha = sha.stdout.strip()

    skill_text = show(repo, "%s:%s" % (sha, SKILL))
    if skill_text is None:
        raise EnvError("cannot read %s:%s" % (sha, SKILL))
    description = description_of(skill_text)

    with tempfile.TemporaryDirectory(prefix="k73-own-desc-") as tdir:
        clone = build_sandbox(repo, sha, fleet, Path(tdir))
        for path in (CENSUS_GATE, CENSUS, PROVINCE):
            require_tree(clone, sha, path)
        gate_rc, gate_out = census_gate(clone, fleet)

    result = evaluate(description, gate_rc)
    lines = frontmatter_diff(repo, base, sha)
    held = result["held"]

    print("own-description rev %s (lane %s, base %s)" % (sha, repo, base))
    print("description %d characters (R3 ceiling %d)"
          % (len(description), DESCRIPTION_MAX))
    print("first sentence %d characters: %s"
          % (len(result["first"]), result["first"]))
    print("first %d characters: %s" % (TRUNCATION, result["head"]))
    print("triggers (%d): %s"
          % (len(result["triggers"]),
             ", ".join('"%s"' % t for t in result["triggers"]) or "none"))
    print("R1 %s: first sentence %d characters is %s %d-%d"
          % ("pass" if result["r1"] else "fail", len(result["first"]),
             "inside" if result["r1"] else "outside",
             FIRST_SENTENCE_MIN, FIRST_SENTENCE_MAX))
    if result["r2"]:
        r2_detail = "whole words skill+prompt yes; quoted trigger %s (in the Triggers list)" % (
            ", ".join('"%s"' % t for t in result["hits"]))
    elif not result["words_ok"]:
        r2_detail = ("whole words skill+prompt no; quoted trigger in the first "
                     "%d: %s" % (TRUNCATION,
                                 ", ".join('"%s"' % t for t in result["hits"]) or "none"))
    elif result["quoted_in_head"]:
        r2_detail = ("whole words skill+prompt yes; quoted string(s) %s not in "
                     "the %d Triggers entries"
                     % (", ".join('"%s"' % t for t in result["quoted_in_head"]),
                        len(result["triggers"])))
    else:
        r2_detail = ("whole words skill+prompt yes; no quoted trigger in the "
                     "first %d characters" % TRUNCATION)
    print("R2 %s: %s" % ("pass" if result["r2"] else "fail", r2_detail))
    if gate_rc == 0:
        gate_detail = "%s exit 0" % CENSUS_GATE
    else:
        failures = [line for line in gate_out.splitlines()
                    if line.startswith("FAIL")][:3]
        gate_detail = "%s exit %d: %s" % (CENSUS_GATE, gate_rc,
                                          " | ".join(failures) or "no FAIL line")
    print("R3 %s: description %d %s %d; %s"
          % ("pass" if result["r3"] else "fail", len(description),
             "<=" if result["length_ok"] else ">", DESCRIPTION_MAX, gate_detail))
    if lines["readable"]:
        print("frontmatter lines %d->%d (inserted %d, deleted %d inside the "
              "frontmatter)" % (lines["base_lines"], lines["rev_lines"],
                                lines["inserted"], lines["deleted"]))
    else:
        print("frontmatter lines n/a (base %s unreadable; guard not evaluated)"
              % base)
    print("own-description rules held %d of %d" % (held, TOTAL))
    return 0 if held == TOTAL else 1


# ---------------------------------------------------------------- self-test ---

STUB_OK = "import sys\nsys.exit(0)\n"
STUB_BAD = "import sys\nsys.exit(1)\n"
ALPHA_SKILL = "# alpha lane\n\nAlpha owns the alpha surface only; nothing else.\n"
REAL_GATE = LANE / CENSUS_GATE
MISSING = "__missing__"


def _fixture_git(lane: Path, *args: str) -> subprocess.CompletedProcess:
    return subprocess.run(
        ["git", "-C", str(lane), "-c", "user.name=probe",
         "-c", "user.email=probe@example.invalid", "-c", "commit.gpgsign=false",
         *args], capture_output=True, text=True)


def _commit_all(lane: Path, message: str) -> str:
    if _fixture_git(lane, "rev-parse", "--show-toplevel").stdout.strip() != str(lane):
        raise RuntimeError("fixture toplevel mismatch at %s" % lane)
    add = _fixture_git(lane, "add", "-A")
    if add.returncode != 0:
        raise RuntimeError("fixture add failed: %s" % _tail(add))
    commit = _fixture_git(lane, "commit", "-q", "-m", message)
    if commit.returncode != 0:
        raise RuntimeError("fixture commit failed: %s" % _tail(commit))
    return _fixture_git(lane, "rev-parse", "HEAD").stdout.strip()


def _init(lane: Path) -> None:
    init = subprocess.run(["git", "init", "-q", str(lane)],
                          capture_output=True, text=True)
    if init.returncode != 0:
        raise RuntimeError("fixture init failed: %s" % _tail(init))


def _skill(desc_lines: list[str]) -> str:
    """A fixture SKILL.md whose frontmatter description folds `desc_lines`."""
    head = "---\nname: kotoba-shokunin\ndescription: >\n"
    body = "".join("  " + line + "\n" for line in desc_lines)
    return head + body + "---\n\n# kotoba\n"


def _skill_one(text: str) -> str:
    return _skill([text])


CENSUS_HEADER = ("| lane | branch | commit | path | classification | names kotoba "
                 "| arbitration | path:line | quote |")


def _census_md(alpha_sha: str) -> str:
    row = "| alpha | main | %s | SKILL.md | adjacent | no | no | SKILL.md:3 | %s |" % (
        alpha_sha, "Alpha owns the alpha surface only; nothing else.")
    return "\n".join(["# sibling-overlap census (fixture)", "", CENSUS_HEADER,
                      "|---|---|---|---|---|---|---|---|---|", row]) + "\n"


def _province_md(alpha_sha: str) -> str:
    return "\n".join([
        "# PROVINCE (fixture)", "", "## Other section", "", "not the table.", "",
        "## Adjacent", "", "| lane | classification | commit | note |",
        "|---|---|---|---|",
        "| alpha | adjacent | %s | fixture |" % alpha_sha, "",
        "## After", "", "text.", ""])


def _world(root: Path, skill_text: str, gate_text: str | None = None,
           base_skill_text: str | None = None) -> dict:
    """fleet/kotoba-shokunin (lane) plus fleet/alpha-shokunin (one sibling).

    `gate_text` None copies the live census gate into the lane; `MISSING`
    leaves it out; any other string is written as the gate (a stub).
    `base_skill_text` given commits it first and `skill_text` as a second
    commit, so the frontmatter guard has a real base -> rev diff.
    """
    fleet = root / "fleet"
    lane = fleet / "kotoba-shokunin"
    alpha = fleet / "alpha-shokunin"
    for sub in ("verifiers", "corpus/knowledge"):
        (lane / sub).mkdir(parents=True, exist_ok=True)
    alpha.mkdir(parents=True)
    (alpha / "SKILL.md").write_text(ALPHA_SKILL)
    _init(alpha)
    alpha_sha = _commit_all(alpha, "alpha base")

    (lane / "SKILL.md").write_text(base_skill_text if base_skill_text is not None
                                   else skill_text)
    (lane / CENSUS).write_text(_census_md(alpha_sha))
    (lane / PROVINCE).write_text(_province_md(alpha_sha))
    if gate_text is None:
        (lane / CENSUS_GATE).write_bytes(REAL_GATE.read_bytes())
    elif gate_text != MISSING:
        (lane / CENSUS_GATE).write_text(gate_text)
    _init(lane)
    base = _commit_all(lane, "fixture base")
    if base_skill_text is not None:
        (lane / "SKILL.md").write_text(skill_text)
        rev = _commit_all(lane, "fixture rev")
    else:
        rev = base
    return {"root": root, "fleet": fleet, "lane": lane, "base": base, "rev": rev,
            "alpha": alpha_sha}


def _drive(world: dict, rev: str | None = None, base: str | None = None,
           repo: str | None = None, fleet: str | None = None,
           cwd: Path | None = None) -> tuple[int, str, str]:
    argv = ["--rev", rev if rev is not None else world["rev"],
            "--repo", repo if repo is not None else str(world["lane"]),
            "--base", base if base is not None else world["base"]]
    if fleet is not None:
        argv += ["--fleet", fleet]
    out, err = io.StringIO(), io.StringIO()
    previous = Path.cwd()
    if cwd is not None:
        os.chdir(cwd)
    try:
        with contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
            try:
                rc = main(argv)
            except SystemExit as exc:            # argparse errors
                rc = int(exc.code or 0)
    finally:
        os.chdir(previous)
    return rc, out.getvalue(), err.getvalue()


def _last_line(text: str) -> str:
    lines = [line for line in text.splitlines() if line.strip()]
    return lines[-1] if lines else ""


PASS_DESC = ('Prompt and skill craft for "skill file" audits and writes. '
             'Alpha owns the alpha surface; this lane audits and reports.')


def _first_sentence(n: int) -> str:
    """A first sentence of exactly n characters: both words and one trigger."""
    seed = 'Prompt "skill file" skill'
    sentence = seed
    while len(sentence) + 6 <= n:
        sentence += " craft"
    return sentence + "x" * (n - len(sentence))


def _with_sentence(n: int, tail: str = "") -> str:
    return (_first_sentence(n) + ". Alpha owns the alpha surface; this lane "
            "audits and reports." + tail + ' Triggers: "skill file".')


def _pad_to(text: str, target: int) -> str:
    """Extend `text` to exactly `target` characters with one trailing token."""
    if len(text) >= target:
        raise RuntimeError("cannot pad %d characters down to %d" % (len(text), target))
    return text + " " + "z" * (target - len(text) - 1)


def self_test() -> int:
    failures: list[str] = []
    assertions = 0

    def check(label: str, ok: bool, detail: str = "") -> None:
        nonlocal assertions
        assertions += 1
        if not ok:
            failures.append("%s%s" % (label, (": " + detail) if detail else ""))

    if not REAL_GATE.is_file():
        print("FAIL the live census gate is absent at %s" % REAL_GATE)
        return 1

    with tempfile.TemporaryDirectory(prefix="k73-own-desc-selftest-") as tdir:
        root = Path(tdir)

        # 1. a satisfying world: R1, R2 and R3 hold.
        w = _world(root / "ok", _skill_one(PASS_DESC + ' Triggers: "skill file".'))
        rc, out, err = _drive(w)
        check("satisfying world exits 0", rc == 0,
              "exit %d stderr %r out %r" % (rc, err.strip()[-160:], out.strip()[-160:]))
        check("satisfying world prints the frozen line last",
              _last_line(out) == "own-description rules held 3 of 3",
              repr(_last_line(out)))
        check("satisfying world passes R3 through the real census gate",
              "R3 pass" in out and "exit 0" in out, out.strip()[-200:])
        check("satisfying world prints the first sentence and its length",
              "first sentence 57 characters: Prompt and skill craft for "
              '"skill file" audits and writes' in out, out.strip()[:400])
        check("satisfying world prints the frontmatter line counts",
              re.search(r"frontmatter lines 5->5 ", out) is not None, out.strip()[-260:])

        # 2. R1 boundaries: 40 and 99 hold, 39 and 100 do not.
        for length, want in ((40, 3), (99, 3), (39, 2), (100, 2), (151, 2)):
            w = _world(root / ("len-%d" % length),
                       _skill_one(_with_sentence(length)))
            rc, out, err = _drive(w)
            check("first sentence %d characters reads %d of 3" % (length, want),
                  "own-description rules held %d of 3" % want in out,
                  _last_line(out))
            check("first sentence %d characters: R1 %s"
                  % (length, "pass" if want == 3 else "fail"),
                  ("R1 pass" in out) == (want == 3), out.strip()[:300])
            check("first sentence %d characters: exit %d"
                  % (length, 0 if want == 3 else 1),
                  rc == (0 if want == 3 else 1), "exit %d" % rc)
            check("first sentence %d characters: length printed"
                  % length, ("first sentence %d characters" % length) in out,
                  out.strip()[:200])

        # 3. R2's three arms: no quoted trigger, a foreign quote, no `prompt`.
        plain = ("Prompt and skill craft audits skill files for trigger fidelity "
                 "and decision density")
        noquote = _pad_to(plain, 99)
        w = _world(root / "r2-noquote", _skill_one(
            noquote + ". Alpha owns the alpha surface; this lane audits and "
            'reports. Triggers: "skill file".'))
        rc, out, err = _drive(w)
        check("a 99-character first sentence with no quoted trigger reads 2 of 3",
              "own-description rules held 2 of 3" in out, _last_line(out))
        check("the 99-character first sentence still passes R1",
              "R1 pass: first sentence 99 characters" in out, out.strip()[:300])
        check("no quoted trigger is named",
              "no quoted trigger in the first 99 characters" in out,
              out.strip()[-300:])

        foreign = ('Prompt and skill craft for "not a trigger" audits and '
                   "writes. Alpha owns the alpha surface; this lane audits and "
                   'reports. Triggers: "skill file".')
        w = _world(root / "r2-foreign", _skill_one(foreign))
        rc, out, err = _drive(w)
        check("a quoted string outside the Triggers list reads 2 of 3",
              "own-description rules held 2 of 3" in out, _last_line(out))
        check("the foreign quote is named",
              '"not a trigger"' in out and "not in the" in out, out.strip()[-300:])

        noprompt = ('Skill craft for "skill file" audits and writes, then '
                    "rewrites the audits. Alpha owns the alpha surface; this "
                    'lane audits and reports. Triggers: "skill file".')
        w = _world(root / "r2-noprompt", _skill_one(noprompt))
        rc, out, err = _drive(w)
        check("a first 99 without the word prompt reads 2 of 3",
              "own-description rules held 2 of 3" in out, _last_line(out))
        check("the missing whole word is named",
              "whole words skill+prompt no" in out, out.strip()[-300:])

        # 4. the mid-phrase period: R1 reads the new first sentence only, and
        #    the counter prints it so a reviewer can judge the hollowness.
        midphrase = ('Prompt and skill craft. For "skill file" audits and writes '
                     "and rewrites skill files for trigger fidelity and decision "
                     "density. Alpha owns the alpha surface; this lane audits and "
                     'reports. Triggers: "skill file".')
        w = _world(root / "r1-midphrase", _skill_one(midphrase))
        rc, out, err = _drive(w)
        check("a period inserted mid-phrase reads 2 of 3",
              "own-description rules held 2 of 3" in out, _last_line(out))
        check("R1 reads the new first sentence only",
              "first sentence 22 characters: Prompt and skill craft" in out,
              out.strip()[:300])
        check("R2 still passes under the inserted period",
              "R2 pass" in out, out.strip()[-300:])

        # 5. R3: the 1024 boundary, and a cut that drops the sibling clauses.
        exact = _pad_to(_with_sentence(57), 1024)
        w = _world(root / "r3-exact", _skill_one(exact))
        rc, out, err = _drive(w)
        check("a 1024-character description reads 3 of 3",
              "own-description rules held 3 of 3" in out, _last_line(out))
        check("a 1024-character description exits 0", rc == 0, "exit %d" % rc)

        over = _pad_to(_with_sentence(57), 1025)
        w = _world(root / "r3-over", _skill_one(over))
        rc, out, err = _drive(w)
        check("a 1025-character description reads 2 of 3",
              "own-description rules held 2 of 3" in out, _last_line(out))
        check("the over-cap length is printed",
              "description 1025 characters" in out and "R3 fail" in out,
              out.strip()[-260:])

        cut = 'Prompt and skill craft for "skill file" audits.'
        w = _world(root / "r3-cut", _skill_one(cut))
        rc, out, err = _drive(w)
        check("a cut description reads below 3",
              "own-description rules held 3 of 3" not in out, _last_line(out))
        check("the cut is refused by the tree's own census gate",
              "does not name the non-none census lane alpha" in out,
              out.strip()[-300:])

        # 5. the reader: a column-0 line ends the description value.
        col0 = ("---\nname: kotoba-shokunin\ndescription: >\n  " + PASS_DESC
                + '\nTriggers: "skill file".\n---\n\n# kotoba\n')
        w = _world(root / "reader-col0", col0)
        rc, out, err = _drive(w)
        check("a column-0 line ends the description value",
              "triggers (0): none" in out, out.strip()[:400])
        check("the swallowed line does not rescue R2",
              "own-description rules held 2 of 3" in out, _last_line(out))

        # 6. no frontmatter at all: 0 of 3, never exit 2.
        w = _world(root / "no-frontmatter", "# kotoba\n\nno frontmatter here\n")
        rc, out, err = _drive(w)
        check("a SKILL.md without frontmatter reads 0 of 3",
              "own-description rules held 0 of 3" in out, _last_line(out))
        check("a SKILL.md without frontmatter exits 1", rc == 1, "exit %d" % rc)

        # 7. the gate is the tree's own: a stub that exits 1 is not a pass.
        w = _world(root / "gate-bad", _skill_one(PASS_DESC + ' Triggers: "skill file".'),
                   gate_text=STUB_BAD)
        rc, out, err = _drive(w)
        check("a census gate that exits 1 reads 2 of 3",
              "own-description rules held 2 of 3" in out, _last_line(out))
        check("the gate's exit code is printed", "exit 1" in out, out.strip()[-260:])

        # 8. missing measurement inputs are exit 2, never a rule verdict.
        w = _world(root / "gate-missing", _skill_one(PASS_DESC),
                   gate_text=MISSING)
        rc, out, err = _drive(w)
        check("a revision without the census gate exits 2", rc == 2, "exit %d" % rc)
        check("a missing gate prints no rule line",
              "own-description rules held" not in out, out.strip()[-200:])
        check("a missing gate explains itself", "could-not-evaluate" in err,
              err.strip()[-200:])

        w = _world(root / "unknown-rev", _skill_one(PASS_DESC))
        rc, out, err = _drive(w, rev="0" * 40)
        check("an unknown revision exits 2", rc == 2, "exit %d" % rc)
        check("an unknown revision prints no rule line",
              "own-description rules held" not in out, out.strip()[-200:])
        check("an unknown revision explains itself",
              "could-not-evaluate" in err and "not a commit" in err,
              err.strip()[-200:])

        rc, out, err = _drive(w, fleet=str(w["root"] / "missing-fleet"))
        check("a missing fleet root exits 2", rc == 2, "exit %d" % rc)
        check("a missing fleet root explains itself",
              "fleet root not found" in err, err.strip()[-200:])

        rc, out, err = _drive(w, fleet=str(w["lane"]))
        check("a fleet root that is the lane exits 2", rc == 2, "exit %d" % rc)
        check("the lane-as-fleet root is named as the M127 shape",
              "M127" in err, err.strip()[-200:])

        plain = root / "not-a-repo"
        plain.mkdir()
        rc, out, err = _drive(w, repo=str(plain))
        check("a directory that is not a git toplevel exits 2", rc == 2,
              "exit %d %r" % (rc, err.strip()[-160:]))

        # 9. M127: `--repo .` from inside the lane resolves to the lane and its
        #    parent fleet root, and the measurement reads the same verdict.
        previous = Path.cwd()
        os.chdir(w["lane"])
        try:
            repo, fleet = resolve_paths(".", None)
        finally:
            os.chdir(previous)
        check("--repo . resolves to the lane itself",
              repo == w["lane"].resolve(), str(repo))
        check("--repo . resolves the fleet root to the lane's parent",
              fleet == w["lane"].parent, str(fleet))
        rc, out, err = _drive(w, repo=".", cwd=w["lane"])
        check("--repo . measures 2 of 3 like the absolute path",
              "own-description rules held 2 of 3" in out, _last_line(out))
        check("--repo . exits 1 like the absolute path", rc == 1, "exit %d" % rc)

        # 10. sandbox shape: the parent is the fleet root, entry for entry.
        with tempfile.TemporaryDirectory(prefix="k73-shape-") as shape_dir:
            clone = build_sandbox(w["lane"], w["rev"], w["fleet"],
                                  Path(shape_dir))
            parent = Path(shape_dir)
            names = sorted(p.name for p in parent.iterdir()
                           if p.name.endswith("-shokunin") and p.name != "kotoba-shokunin")
            check("the sandbox parent holds the fleet's sibling lanes",
                  names == ["alpha-shokunin"], repr(names))
            head = git(clone, "rev-parse", "HEAD").stdout.strip()
            check("the sandbox clone sits at the measured revision",
                  head == w["rev"], head)
            check("the sandbox SKILL.md is the revision's SKILL.md",
                  (clone / SKILL).read_text() ==
                  (w["lane"] / SKILL).read_text())

        # 11. the frontmatter guard is printed, never counted.
        passing = PASS_DESC + ' Triggers: "skill file".'
        base_text = _skill_one(passing)
        more = base_text + "\nExtra guidance line outside the frontmatter.\n"
        w = _world(root / "guard-outside", more, base_skill_text=base_text)
        rc, out, err = _drive(w)
        check("a line added outside the frontmatter keeps 3 of 3",
              "own-description rules held 3 of 3" in out, _last_line(out))
        check("a line outside the frontmatter leaves the guard at zero",
              re.search(r"\(inserted 0, deleted 0 inside the frontmatter\)", out)
              is not None, out.strip()[-260:])

        head_text, tail_text = passing.split(" audits and writes.", 1)
        split_lines = [head_text + " audits and", "writes." + tail_text]
        folded = _skill(split_lines)
        check("the split fixture folds to the same description",
              description_of(folded) == description_of(base_text),
              description_of(folded)[:80])
        w = _world(root / "guard-inside", folded, base_skill_text=base_text)
        rc, out, err = _drive(w)
        check("a split description line keeps 3 of 3 (guard not counted)",
              "own-description rules held 3 of 3" in out, _last_line(out))
        match = re.search(r"frontmatter lines (\d+)->(\d+) \(inserted (\d+), "
                          r"deleted (\d+) inside the frontmatter\)", out)
        check("the split changes the frontmatter line counts",
              match is not None and int(match.group(1)) != int(match.group(2)),
              out.strip()[-260:])
        check("the split reports lines inserted inside the frontmatter",
              match is not None and int(match.group(3)) > 0, out.strip()[-260:])

    print("self-test: %d failure(s) over %d assertions"
          % (len(failures), assertions))
    for failure in failures:
        print("FAIL", failure)
    return 1 if failures else 0


# --------------------------------------------------------------------------
# CLI
# --------------------------------------------------------------------------

def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--rev", help="lane revision to measure")
    parser.add_argument("--repo", default=str(LANE), help="lane repository")
    parser.add_argument("--fleet", default=None,
                        help="fleet root the sandbox is shaped from (default: "
                             "the repo's parent, resolved from an absolute path)")
    parser.add_argument("--base", default=BASE,
                        help="base revision for the frontmatter-line guard "
                             "(pinned; a fixture affordance)")
    parser.add_argument("--self-test", action="store_true",
                        help="drive main() on isolated fixture worlds")
    args = parser.parse_args(argv)
    if args.self_test:
        return self_test()
    if not args.rev:
        parser.error("--rev is required unless --self-test is selected")
    try:
        repo, fleet = resolve_paths(args.repo, args.fleet)
        if args.base != BASE:
            print("note: base override %s (fixture affordance; the lane run "
                  "pins %s)" % (args.base, BASE))
        return measure(repo, args.rev, fleet, args.base)
    except EnvError as exc:
        print("could-not-evaluate: %s" % exc, file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())
