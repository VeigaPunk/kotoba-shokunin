#!/usr/bin/env python3
"""Successor measurement for round-61's six routed repairs.

This is a second measurement; it does not edit or replace the frozen
check_routed_repairs.py. The six repair properties below remain bounded to the
Round 61 LOG section and named committed blobs. G-a derives its count from the measured revision's exact `git ls-tree -r --name-only <rev> -- .ufo/waves/round-60/build` name-pattern census over basenames, not registry-roster membership; it claims no roster honesty.
The remaining checks are explicit text and receipt-shape tests, not proof of the repairs' wider semantic truth.


Usage:
  python3 -B verifiers/check_routed_repairs_v2.py [--rev <rev>]
  python3 -B verifiers/check_routed_repairs_v2.py --self-test
"""
from __future__ import annotations

import argparse
import io
import re
import subprocess
import sys
from contextlib import redirect_stderr, redirect_stdout
from pathlib import Path, PurePosixPath

VERIFIERS = Path(__file__).resolve().parent
if str(VERIFIERS) not in sys.path:
    sys.path.insert(0, str(VERIFIERS))
import check_routed_repairs as frozen  # noqa: E402

LANE = VERIFIERS.parent
BASE_REV = "f3246d1493b60ea1c0d947a19c39f9e08e92f326"
TIP_REV = "45a7ecfac9e203297f3146c45d63f5e79367470c"
BUILD_DIR = ".ufo/waves/round-60/build"
COUNT_PATTERN = re.compile(
    r"^(Conn|Critic|Exec|Mut|Review|Scout|Scribe|Sentinel|Src)[A-Za-z0-9]+\.md$"
)
INPUT_PATHS = (
    "LOG.md",
    "corpus/QUALITY.md",
    "corpus/lessons/round-61.md",
    ".ufo/waves/round-61/census-after.txt",
    ".ufo/waves/round-61/receipts/controls-ancestry.txt",
)
LOG_SECTION_RE = re.compile(r"^\s*(#{1,6})\s+.*\bround[ -]*61\b.*$", re.I)
HEADING_RE = re.compile(r"^\s*(#{1,6})\s+.*$")
LANDING_CUE_RE = re.compile(r"\b(?:landed|landing|in\s+scope)\b", re.I)
NEGATION_RE = re.compile(
    r"\b(?:not|never|false|wrong|incorrect(?:ly)?|untrue|denied)\b", re.I
)
FREEZE_REF_RE = re.compile(
    r"(?<![\w.-])(?:[\w.-]+/)*receipts/freeze2-selftest\.txt(?![\w.-])", re.I
)
C1_REF_RE = re.compile(
    r"(?<![\w.-])(?:[\w.-]+/)*C1-measure\.txt(?![\w.-])", re.I
)
C1_DENIED_RE = re.compile(
    r"\b(?:not|rather\s+than|instead\s+of)\s+(?:in\s+)?(?:the\s+)?`?"
    r"(?:[\w.-]+/)*C1-measure\.txt`?(?![\w.-])",
    re.I,
)
C1_AFTER_DENIAL_RE = re.compile(
    r"(?:[\w.-]+/)*C1-measure\.txt\s+(?:is|was|contains?)\s+not\b",
    re.I,
)
ANCESTRY_COMMAND_RE = re.compile(
    r"^\s*(?:#\s*)?\$?\s*git\s+merge-base\s+--is-ancestor\s+"
    r"([0-9a-fA-F]{40})\s+([0-9a-fA-F]{40})\s*$"
)
EXIT_ZERO_RE = re.compile(r"^\s*exit(?:\s+|=)0\s*$")


def git_text(repo: Path, args: list[str]) -> str | None:
    result = subprocess.run(
        ["git", "-C", str(repo), *args], capture_output=True
    )
    if result.returncode != 0:
        return None
    return result.stdout.decode("utf-8", "replace")


def git_show(repo: Path, rev: str, path: str) -> str | None:
    return git_text(repo, ["show", f"{rev}:{path}"])


def git_tree_names(repo: Path, rev: str) -> list[str] | None:
    """Return the measured build subtree names using the frozen command shape."""
    result = subprocess.run(
        [
            "git",
            "-C",
            str(repo),
            "ls-tree",
            "-r",
            "--name-only",
            rev,
            "--",
            BUILD_DIR,
        ],
        capture_output=True,
    )
    if result.returncode != 0:
        return None
    return result.stdout.decode("utf-8", "replace").splitlines()


def git_regular_blob(repo: Path, rev: str, path: str) -> bool:
    """Reject a census path that is a tree or symlink, not a regular blob."""
    result = subprocess.run(
        ["git", "-C", str(repo), "ls-tree", rev, "--", path],
        capture_output=True,
    )
    if result.returncode != 0 or not result.stdout:
        return False
    metadata = result.stdout.decode("utf-8", "replace").split("\t", 1)[0]
    fields = metadata.split()
    return len(fields) == 3 and fields[0] in {"100644", "100755"} and fields[1] == "blob"


def resolve_commit(repo: Path, rev: str) -> str | None:
    result = subprocess.run(
        ["git", "-C", str(repo), "rev-parse", "--verify", f"{rev}^{{commit}}"],
        capture_output=True,
    )
    if result.returncode != 0:
        return None
    return result.stdout.decode("ascii", "replace").strip()


def committed_report_count(tree_names: list[str]) -> int:
    """Count exact seat-report basenames inside the selected build subtree."""
    prefix = BUILD_DIR + "/"
    return sum(
        1
        for path in tree_names
        if path.startswith(prefix) and COUNT_PATTERN.fullmatch(PurePosixPath(path).name)
    )


def round_61_section(log: str) -> str:
    lines = log.splitlines()
    for start, line in enumerate(lines):
        match = LOG_SECTION_RE.match(line)
        if not match:
            continue
        level = len(match.group(1))
        end = len(lines)
        for index in range(start + 1, len(lines)):
            heading = HEADING_RE.match(lines[index])
            if heading and len(heading.group(1)) <= level:
                end = index
                break
        return "\n".join(lines[start:end])
    return ""


def bounded_windows(lines: list[str], width: int):
    for start in range(len(lines)):
        yield "\n".join(lines[start : start + width])


def exact_path(text: str, path: str) -> bool:
    return re.search(
        r"(?<![\w./-])" + re.escape(path) + r"(?![\w./-])", text, re.I
    ) is not None


def affirmed_count(line: str, pattern: re.Pattern[str]) -> re.Match[str] | None:
    match = pattern.search(line)
    if match is None:
        return None
    neighborhood = line[max(0, match.start() - 48) : match.end() + 48]
    return None if NEGATION_RE.search(neighborhood) else match


def r_a_count_correction(section: str, derived_count: int) -> bool:
    claimed_re = re.compile(r"\bclaimed\s+(\d+)\b", re.I)
    committed_re = re.compile(r"\bcommitted\s+(\d+)\b", re.I)
    for line in section.splitlines():
        if not re.search(r"\bbuild\s+reports\b", line, re.I):
            continue
        if not exact_path(line, BUILD_DIR):
            continue
        claimed = affirmed_count(line, claimed_re)
        committed = affirmed_count(line, committed_re)
        if (
            claimed is not None
            and committed is not None
            and int(claimed.group(1)) > derived_count
            and int(committed.group(1)) == derived_count
        ):
            return True
    return False


def r_b_landed_scope(section: str) -> bool:
    lines = section.splitlines()
    for window in bounded_windows(lines, 8):
        if (
            exact_path(window, "plans/round-60.md")
            and exact_path(window, "considerthese/2026-10-23.md")
            and LANDING_CUE_RE.search(window)
        ):
            return True
    return False


def freeze_pointer_asserted(text: str) -> bool:
    for freeze in FREEZE_REF_RE.finditer(text):
        prefix = text[max(0, freeze.start() - 180) : freeze.start()]
        bases = list(re.finditer(r"\bbase(?:\s+measurement)?\b", prefix, re.I))
        if not bases:
            continue
        base = bases[-1]
        before_base = prefix[max(0, base.start() - 48) : base.start()]
        between_base_and_freeze = prefix[base.end() :]
        if NEGATION_RE.search(before_base):
            continue
        if NEGATION_RE.search(between_base_and_freeze):
            continue
        if C1_REF_RE.search(between_base_and_freeze):
            continue
        return True
    return False


def c1_pointer_denied(text: str) -> bool:
    return C1_DENIED_RE.search(text) is not None or C1_AFTER_DENIAL_RE.search(text) is not None


def r_c_pointer_direction(section: str) -> bool:
    lines = section.splitlines()
    return any(
        freeze_pointer_asserted(window) and c1_pointer_denied(window)
        for window in bounded_windows(lines, 2)
    )


def r_d_census_body(census: str | None, census_is_regular: bool) -> bool:
    if census is None or not census_is_regular:
        return False
    lines = [line.strip() for line in census.splitlines() if line.strip()]
    return len(lines) >= 2 and lines[-1] == "exit=0" and any(
        line != "exit=0" for line in lines[:-1]
    )


def exact_quality_row(quality: str) -> str | None:
    for line in quality.splitlines():
        match = re.match(r"^\s*\|\s*Q56\s*\|(?P<body>.*)$", line)
        if match:
            return match.group("body")
    return None


def markdown_section(text: str, title: str) -> str:
    lines = text.splitlines()
    title_re = re.compile(r"^\s*(#{1,6})\s+" + re.escape(title) + r"\b.*$", re.I)
    for start, line in enumerate(lines):
        match = title_re.match(line)
        if not match:
            continue
        level = len(match.group(1))
        end = len(lines)
        for index in range(start + 1, len(lines)):
            heading = HEADING_RE.match(lines[index])
            if heading and len(heading.group(1)) <= level:
                end = index
                break
        return "\n".join(lines[start:end])
    return ""


def r_e_exact_ids(blobs: dict[str, str | None]) -> bool:
    quality = blobs.get("corpus/QUALITY.md") or ""
    lesson = blobs.get("corpus/lessons/round-61.md")
    row = exact_quality_row(quality)
    if row is None or lesson is None:
        return False
    if not re.search(r"\bbyte-exact\b", row, re.I):
        return False
    if not re.search(r"\bliteral\b", row, re.I) or not re.search(r"\bequal", row, re.I):
        return False
    mistakes = markdown_section(lesson, "Mistakes")
    return re.search(r"(?<![A-Za-z0-9])M91(?![A-Za-z0-9])", mistakes) is not None


def r_f_owned_ancestry(ancestry: str | None) -> bool:
    if ancestry is None:
        return False
    lines = ancestry.splitlines()
    for index, line in enumerate(lines[:-1]):
        match = ANCESTRY_COMMAND_RE.fullmatch(line)
        if match is None:
            continue
        first, second = match.groups()
        if first.casefold() == second.casefold():
            continue
        if EXIT_ZERO_RE.fullmatch(lines[index + 1]):
            return True
    return False


def check_repairs(
    blobs: dict[str, str | None],
    tree_names: list[str],
    census_is_regular: bool = True,
) -> tuple[int, list[str]]:
    """Score the six repairs from committed blobs plus their measured tree names."""
    section = round_61_section(blobs.get("LOG.md") or "")
    derived_count = committed_report_count(tree_names)
    checks = [
        ("R-a count correction", r_a_count_correction(section, derived_count)),
        ("R-b landed-scope names", r_b_landed_scope(section)),
        ("R-c base-measure pointer", r_c_pointer_direction(section)),
        (
            "R-d census-after body",
            r_d_census_body(
                blobs.get(".ufo/waves/round-61/census-after.txt"), census_is_regular
            ),
        ),
        ("R-e byte-exact criterion + M91", r_e_exact_ids(blobs)),
        (
            "R-f controls-ancestry receipt",
            r_f_owned_ancestry(
                blobs.get(".ufo/waves/round-61/receipts/controls-ancestry.txt")
            ),
        ),
    ]
    why = [f"{name}: {'ok' if passed else 'missing'}" for name, passed in checks]
    return sum(passed for _, passed in checks), why


HONEST_LOG = (
    "# Iteration log\n\n"
    "## 2026-10-23 — Round 61 (fixture)\n"
    "- Round-60 build reports: claimed 32, committed 29; counted at `"
    ".ufo/waves/round-60/build`.`\n"
    "- R-b landed scope includes `plans/round-60.md` and "
    "`considerthese/2026-10-23.md`.\n"
    "- R-c: the base measurement is `receipts/freeze2-selftest.txt`, not "
    "`C1-measure.txt`.\n\n"
    "## Round 62 — next entry\n"
)
HONEST_QUALITY = (
    "| id | criterion |\n|---|---|\n"
    "| Q56 | Reserve `byte-exact` for literal byte-for-byte equality. |\n"
)
HONEST_LESSON = (
    "# Round 61 lesson\n\n## Mistakes\n\n"
    "- **M91 — class: report-evidence overclaim.** A report may not claim a "
    "measurement the recorded bytes do not support.\n\n"
    "## Gate\n\nA separate section.\n"
)
HONEST_CENSUS = "kotoba\tW04\tS018 fixture source row\nkotoba ok\nexit=0\n"
HASH_CTL = "b4a8d2ee79a6190cf5ece5d11395544876e1fc8a"
HASH_DATA = "43fe01804708d65e53965b4be31e9dc7dce793e4"
HONEST_ANCESTRY = (
    f"# Round-61 controls-ancestry receipt\n"
    f"# $ git merge-base --is-ancestor {HASH_CTL} {HASH_DATA}\n"
    "exit 0\n"
)


def make_fixture_blob_map(report_count: int) -> dict[str, str | None]:
    blobs: dict[str, str | None] = {
        "LOG.md": HONEST_LOG,
        "corpus/QUALITY.md": HONEST_QUALITY,
        "corpus/lessons/round-61.md": HONEST_LESSON,
        ".ufo/waves/round-61/census-after.txt": HONEST_CENSUS,
        ".ufo/waves/round-61/receipts/controls-ancestry.txt": HONEST_ANCESTRY,
    }
    for number in range(1, report_count + 1):
        path = f"{BUILD_DIR}/ExecSynthetic{number:02}.md"
        blobs[path] = f"synthetic build report {number:02}\n"
    return blobs


def dishonest_fixture_maps() -> dict[str, dict[str, str | None]]:
    common = make_fixture_blob_map(29)
    d1 = make_fixture_blob_map(30)
    d1["LOG.md"] = common["LOG.md"]

    d2 = dict(common)
    d2["LOG.md"] = (
        "# Iteration log\n\n## 2026-10-23 — Round 61 (fixture)\n"
        "- Round-60 build reports: the quoted correction were NOT claimed 32; "
        "the tree count is `committed 29` at `.ufo/waves/round-60/build`. \n"
        "- R-b landed scope includes `plans/round-60.md` and "
        "`considerthese/2026-10-23.md`.\n"
        "- R-c: the base measurement is `receipts/freeze2-selftest.txt`, not "
        "`C1-measure.txt`.\n\n## Round 62 — next entry\n"
    )

    d3 = dict(common)
    d3["LOG.md"] = (
        "# Iteration log\n\n## 2026-10-23 — Round 61 (fixture)\n"
        "- Round-60 build reports: claimed 32, committed 29; counted at `"
        ".ufo/waves/round-60/build`. \n"
        "- R-b landed scope includes `plans/round-60.md` and "
        "`considerthese/2026-10-23.md`.\n"
        "- R-c inverted: the base measurement is `C1-measure.txt`, not "
        "`receipts/freeze2-selftest.txt`.\n\n## Round 62 — next entry\n"
    )

    d4 = dict(common)
    d4[".ufo/waves/round-61/census-after.txt"] = "exit=0\n"

    d5 = dict(common)
    d5["corpus/QUALITY.md"] = (
        "| id | criterion |\n|---|---|\n"
        "| Q560 | Reserve `byte-exact` for literal byte-for-byte equality. |\n"
    )
    d5["corpus/lessons/round-61.md"] = (
        "# Round 61 lesson\n\n## Mistakes\n\n"
        "- **M910 — class: report-evidence overclaim.** Placeholder body.\n"
    )

    d6 = dict(common)
    d6[".ufo/waves/round-61/receipts/controls-ancestry.txt"] = (
        "$ git rev-parse HEAD\n"
        "exit 0\n"
        "$ git merge-base --is-ancestor not-a-hash also-not-a-hash\n"
        "TODO: run the ancestry command\n"
    )

    return {"D1": d1, "D2": d2, "D3": d3, "D4": d4, "D5": d5, "D6": d6}


def fixture_tree_names(blobs: dict[str, str | None]) -> list[str]:
    """Synthetic trees are represented by their exact path->blob fixture maps."""
    return [path for path, blob in blobs.items() if blob is not None]


def cli_measurement(rev: str) -> tuple[int, int | None, str, str]:
    """Exercise the public --rev CLI path in-process and capture its exact result."""
    stdout = io.StringIO()
    stderr = io.StringIO()
    with redirect_stdout(stdout), redirect_stderr(stderr):
        status = main(["--rev", rev])
    match = re.search(r"^routed repairs verified (\d+) of 6$", stdout.getvalue(), re.M)
    return status, int(match.group(1)) if match else None, stdout.getvalue(), stderr.getvalue()


def self_test() -> int:
    failures: list[str] = []
    rejected = 0
    old_scores: dict[str, int] = {}

    for label, blobs in dishonest_fixture_maps().items():
        successor_score, _ = check_repairs(blobs, fixture_tree_names(blobs))
        frozen_score, _ = frozen.check_repairs(blobs)
        old_scores[label] = frozen_score
        if frozen_score != 6:
            failures.append(f"{label}: frozen counter scored {frozen_score}, expected 6")
        if successor_score >= 6:
            failures.append(f"{label}: successor scored {successor_score}, expected <6")
        else:
            rejected += 1

    h1 = make_fixture_blob_map(29)
    h1["LOG.md"] = (
        "# Iteration log\n\n## 2026-10-23 — Round 61 (house style)\n"
        "- Round-60 build reports: claimed 32, committed 29; counted at `"
        ".ufo/waves/round-60/build`.\n"
        "- R-b landed scope includes `plans/round-60.md` and "
        "`considerthese/2026-10-23.md`.\n"
        "- R-c: the base measurement is receipts/freeze2-selftest.txt;\n"
        "  C1-measure.txt is NOT the base pointer.\n\n## Round 62 — next entry\n"
    )
    h1[".ufo/waves/round-61/receipts/controls-ancestry.txt"] = (
        f"$ git merge-base --is-ancestor {HASH_CTL} {HASH_DATA}\nexit=0\n"
    )
    h1_score, _ = check_repairs(h1, fixture_tree_names(h1))
    h1_frozen, _ = frozen.check_repairs(h1)
    old_scores["H1"] = h1_frozen
    if h1_score != 6:
        failures.append(f"H1: successor scored {h1_score}, expected 6")
    if h1_frozen != 4:
        failures.append(f"H1: frozen counter scored {h1_frozen}, expected 4")

    population_29 = make_fixture_blob_map(29)
    population_30_same_blobs = dict(population_29)
    extra_report = f"{BUILD_DIR}/ExecSynthetic30.md"
    population_30_same_blobs[extra_report] = "synthetic build report 30\n"
    same_repair_blobs = all(
        population_29[path] == population_30_same_blobs[path] for path in INPUT_PATHS
    )
    pop29_score, _ = check_repairs(
        population_29, fixture_tree_names(population_29)
    )
    pop30_stale_score, _ = check_repairs(
        population_30_same_blobs, fixture_tree_names(population_30_same_blobs)
    )
    population_30_declared = dict(population_30_same_blobs)
    population_30_declared["LOG.md"] = str(population_30_declared["LOG.md"]).replace(
        "committed 29", "committed 30", 1
    )
    pop30_declared_score, _ = check_repairs(
        population_30_declared, fixture_tree_names(population_30_declared)
    )
    pop29_frozen, _ = frozen.check_repairs(population_29)
    pop30_frozen, _ = frozen.check_repairs(population_30_same_blobs)
    pop30_declared_frozen, _ = frozen.check_repairs(population_30_declared)
    if not same_repair_blobs:
        failures.append("G-a paired population control changed a repair blob")
    if pop29_score != 6 or pop30_stale_score >= 6 or pop30_declared_score != 6:
        failures.append(
            "G-a paired population control did not score 29/pass, 30/stale/fail, 30/declared/pass"
        )
    if (pop29_frozen, pop30_frozen, pop30_declared_frozen) != (6, 6, 5):
        failures.append(
            "G-a paired control frozen scores differed from the expected (6, 6, 5)"
        )

    tip_resolved = resolve_commit(LANE, TIP_REV)
    if tip_resolved is None:
        failures.append(f"tip revision is unreadable: {TIP_REV}")
        tip_resolved = TIP_REV
    tip_blobs = {path: git_show(LANE, tip_resolved, path) for path in INPUT_PATHS}
    tip_frozen, _ = frozen.check_repairs(tip_blobs)
    old_scores["H2 tip"] = tip_frozen
    tip_status, tip_score, tip_output, _ = cli_measurement(tip_resolved)
    if tip_status != 0 or tip_score != 6:
        failures.append(
            f"H2 tip CLI: exit {tip_status}, score {tip_score}; expected exit 0, score 6"
        )

    if old_scores.get("H2 tip") != 6:
        failures.append(
            f"H2 tip: frozen counter scored {old_scores.get('H2 tip')}, expected 6"
        )

    base_status, base_score, base_output, _ = cli_measurement(BASE_REV)
    if base_status != 1 or base_score != 0:
        failures.append(
            f"base CLI: exit {base_status}, score {base_score}; expected exit 1, score 0"
        )

    unreadable_rev = "routed-repairs-v2-no-such-revision"
    unreadable_status, unreadable_score, _, unreadable_error = cli_measurement(
        unreadable_rev
    )
    if (
        unreadable_status != 2
        or unreadable_score is not None
        or "could-not-evaluate" not in unreadable_error
    ):
        failures.append(
            "unreadable-revision CLI control did not exit 2 with could-not-evaluate"
        )

    constant_six_base = 6
    constant_zero_h1 = 0
    constant_zero_h2 = 0
    if constant_six_base == base_score:
        failures.append("constant-6 evaluator unexpectedly passes the base control")
    if constant_zero_h1 == h1_score:
        failures.append("constant-0 evaluator unexpectedly passes H1")
    if constant_zero_h2 == tip_score:
        failures.append("constant-0 evaluator unexpectedly passes H2")



    print(
        "G-a paired population control: "
        f"29 names/committed 29={pop29_score}; "
        f"30 names/committed 29={pop30_stale_score}; "
        f"30 names/committed 30={pop30_declared_score}; "
        f"frozen={pop29_frozen}/{pop30_frozen}/{pop30_declared_frozen}",
        file=sys.stderr,
    )
    print(
        "label-only constants fail controls: "
        f"constant 6 vs base {base_score}; constant 0 vs H1 {h1_score}; "
        f"constant 0 vs H2 {tip_score}",
        file=sys.stderr,
    )

    print(
        "frozen counter before: "
        + "; ".join(f"{name} {score} of 6" for name, score in old_scores.items()),
        file=sys.stderr,
    )

    print(f"self-test base CLI output:\n{base_output}", file=sys.stderr, end="")
    print(f"self-test tip CLI output:\n{tip_output}", file=sys.stderr, end="")

    print(
        f"self-test CLI exits: base rev {BASE_REV} exit {base_status}; "
        f"tip rev {tip_resolved} exit {tip_status}; "
        f"unreadable rev {unreadable_rev} exit {unreadable_status}",
        file=sys.stderr,
    )

    if rejected != 6:
        failures.append(f"dishonest rejected {rejected} of 6, expected 6")
    honest_passed = int(h1_score == 6) + int(tip_score == 6)
    if honest_passed != 2:
        failures.append(f"honest passed {honest_passed} of 2, expected 2")

    base_display = base_score if base_score is not None else "unreadable"
    tip_display = tip_score if tip_score is not None else "unreadable"
    print(
        f"successor: dishonest rejected {rejected} of 6; honest passed "
        f"{honest_passed} of 2; base {base_display} of 6; tip {tip_display} of 6"
    )
    for failure in failures:
        print(f"self-test: {failure}", file=sys.stderr)
    return 0 if not failures else 1


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--rev", default=None, help="revision to measure (default: master)")
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args(argv)
    if args.self_test:
        return self_test()

    rev = args.rev
    if rev is None:
        resolved = resolve_commit(LANE, "master")
        if resolved is None:
            print("routed repairs verified could-not-evaluate: no rev", file=sys.stderr)
            return 2
        rev = resolved
    elif resolve_commit(LANE, rev) is None:
        print("routed repairs verified could-not-evaluate: unreadable rev", file=sys.stderr)
        return 2

    tree_names = git_tree_names(LANE, rev)
    if tree_names is None:
        print("routed repairs verified could-not-evaluate: unreadable tree", file=sys.stderr)
        return 2
    blobs = {path: git_show(LANE, rev, path) for path in INPUT_PATHS}
    if blobs["LOG.md"] is None or blobs["corpus/QUALITY.md"] is None:
        print("routed repairs verified could-not-evaluate: unreadable rev", file=sys.stderr)
        return 2

    census_regular = git_regular_blob(
        LANE, rev, ".ufo/waves/round-61/census-after.txt"
    )
    score, why = check_repairs(blobs, tree_names, census_regular)
    for line in why:
        print(line)
    print(f"routed repairs verified {score} of 6")
    return 0 if score == 6 else 1


if __name__ == "__main__":
    sys.exit(main())
