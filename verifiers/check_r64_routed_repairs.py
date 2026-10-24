#!/usr/bin/env python3
"""Round-64 C2 counter for the round-63 routed defects.

Frozen predicate:
  python3 -B verifiers/check_r64_routed_repairs.py --rev <rev>
prints `r63 routed defects closed 4 of 4` and exits 0, while the pinned
BASE_REV prints `r63 routed defects closed 0 of 4` and exits nonzero. The
counter refuses to certify unless BASE_REV itself scores exactly 0 of 4.

All four checks derive evidence from committed blobs at <rev>. LOG checks 2
and 3 are scoped to lines after the first round-64 header. The self-test ports
the round-63 E2 process arms to temporary git repositories and exercises the
receipt substitutions, edit thresholds, and suffix/boundary rules.

Pre-data integration fix (no measurement taken with the prior bytes): the
round-heading anchor accepts the lane's parenthetical heading form
(`## 2026-10-24 — Round 64 (...)`) via a boundary-safe exact-or-space match —
a bare startswith would let a future `Round 64b` heading anchor the suffix —
and the self-test gains the parenthetical-heading and Round-64b-sibling arms
(32 assertions).
"""
from __future__ import annotations

import argparse
import ast
import os
import re
import subprocess
import sys
import tempfile
from decimal import Decimal, InvalidOperation
from pathlib import Path

LANE = Path(__file__).resolve().parent.parent
BASE_REV_LITERAL = "078eec4a1f6a41c64ff8806f58b46a67cd413bfc"
BASE_REV = BASE_REV_LITERAL
SEAT_BASE_REV = "38defdc"
EXPECTED_ASSERTIONS = 23
EXPECTED_STATIC_SHAPE = (17, 2, 3)
EXPECTED_PINNED_BASE_PREFIX = "35d44b4b"
ROUND64_HEADER = "## 2026-10-24 — Round 64"
SEAT_MARKER = "temporal mismatch"

SEAT_EDIT = ".ufo/waves/round-63/w2/MutW2SplitClauses.md"
CONTROL_PATHS = (
    ".ufo/waves/round-63/controls/C1-do-nothing-v31.txt",
    ".ufo/waves/round-63/controls/C2-before-r62tip.txt",
)
SCORECARD = "SCORECARD.md"
LOG = "LOG.md"
R63_COUNTER = "verifiers/check_r63_routed_repairs.py"
PATCH_RECEIPT = ".ufo/waves/round-63/w2/ExecW2E2Patch.md"
REV_RE = re.compile(r"^[0-9a-fA-F]{40}$")
HEX_CHARS = "0-9a-fA-F"
FULL_HASH_RE = re.compile(r"(?<![%s])[0-9a-fA-F]{40}(?![%s])" %
                          (HEX_CHARS, HEX_CHARS))


def git(root: Path, args: list[str], timeout: int = 20) -> subprocess.CompletedProcess[str]:
    return subprocess.run(["git", "-C", str(root), *args], capture_output=True,
                          text=True, timeout=timeout)


def show(root: Path, rev: str, path: str) -> str | None:
    proc = git(root, ["show", "%s:%s" % (rev, path)])
    return proc.stdout if proc.returncode == 0 else None


def show_bytes(root: Path, rev: str, path: str) -> bytes | None:
    proc = subprocess.run(["git", "-C", str(root), "show",
                           "%s:%s" % (rev, path)], capture_output=True,
                          timeout=20)
    return proc.stdout if proc.returncode == 0 else None


def _added_lines(root: Path, old_rev: str, new_rev: str,
                 path: str) -> list[str] | None:
    proc = git(root, ["diff", "--no-ext-diff", "--unified=0",
                      old_rev, new_rev, "--", path])
    if proc.returncode != 0:
        return None
    return [line[1:] for line in proc.stdout.splitlines()
            if line.startswith("+") and not line.startswith("+++")]


def _numstat_added(root: Path, old_rev: str, new_rev: str,
                   path: str) -> int | None:
    proc = git(root, ["diff", "--numstat", old_rev, new_rev, "--", path])
    if proc.returncode != 0:
        return None
    if not proc.stdout.strip():
        return 0
    fields = proc.stdout.splitlines()[0].split("\t", 2)
    if len(fields) != 3 or not fields[0].isdigit():
        return None
    return int(fields[0])


def _r64_suffix_lines(root: Path, rev: str) -> list[str]:
    """Lines strictly after the first frozen round-64 LOG heading.

    The heading may carry a parenthetical (the lane's round-heading
    convention, e.g. ``## 2026-10-24 — Round 64 (hyaku run 5, ...)``), so
    the match is the exact header or the header followed by a space — never
    a bare startswith that a future ``Round 64b`` heading could satisfy."""
    log = show(root, rev, LOG)
    if log is None:
        return []
    lines = log.splitlines()
    for index, line in enumerate(lines):
        stripped = line.strip()
        if stripped == ROUND64_HEADER or stripped.startswith(ROUND64_HEADER + " "):
            return lines[index + 1:]
    return []


def _hash_token_re(token: str) -> re.Pattern[str]:
    return re.compile(r"(?<![%s])%s(?![%s])" %
                      (HEX_CHARS, re.escape(token), HEX_CHARS))


def _number_token_re(token: str) -> re.Pattern[str]:
    # Numeric boundaries reject 9 in 19 and 10 in 100, but allow sentence dots.
    return re.compile(r"(?<![0-9])%s(?![0-9])(?!\.[0-9])" %
                      re.escape(token))


def _matches_hash_prefix(line: str, full_hash: str) -> bool:
    for match in re.finditer(r"(?<![%s])[0-9a-fA-F]{7,40}(?![%s])" %
                             (HEX_CHARS, HEX_CHARS), line):
        token = match.group(0).lower()
        if len(token) <= len(full_hash) and full_hash.startswith(token):
            return True
    return False


def check_seat_edit(root: Path, rev: str) -> tuple[bool, str]:
    content = show(root, rev, SEAT_EDIT)
    if content is None:
        return False, "%s absent at %s" % (SEAT_EDIT, rev)
    marker_lines = [line for line in content.splitlines() if SEAT_MARKER in line]
    added = _added_lines(root, SEAT_BASE_REV, rev, SEAT_EDIT)
    added_count = _numstat_added(root, SEAT_BASE_REV, rev, SEAT_EDIT)
    if added is None or added_count is None:
        return False, "could not compare %s with %s" % (SEAT_EDIT, SEAT_BASE_REV)
    marker_added = any(SEAT_MARKER in line for line in added)
    ok = bool(marker_lines) and marker_added and added_count >= 60
    return ok, ("marker=%s added-marker=%s added-lines=%d (need >=60)" %
                (bool(marker_lines), marker_added, added_count))


def _committing_rev(root: Path, rev: str, path: str) -> str | None:
    # Match the frozen derivation: the commit adding this exact control path.
    proc = git(root, ["log", "--diff-filter=A", "--format=%H", "-1",
                      rev, "--", path])
    if proc.returncode != 0:
        return None
    commits = proc.stdout.strip().splitlines()
    if not commits or not REV_RE.fullmatch(commits[0]):
        return None
    return commits[0].lower()


def _control_base(root: Path, rev: str) -> str | None:
    contents = [show(root, rev, path) for path in CONTROL_PATHS]
    if any(content is None for content in contents):
        return None
    hash_sets = [set(FULL_HASH_RE.findall(content)) for content in contents]
    common = set.intersection(*hash_sets)
    if len(common) != 1:
        return None
    base = common.pop().lower()
    if not base.startswith(EXPECTED_PINNED_BASE_PREFIX):
        return None
    return base


def check_control_revs(root: Path, rev: str) -> tuple[bool, str]:
    commits = [_committing_rev(root, rev, path) for path in CONTROL_PATHS]
    if any(commit is None for commit in commits):
        return False, "could not compute both control-file addition revisions"
    pinned_base = _control_base(root, rev)
    if pinned_base is None:
        return False, "could not compute the shared 35d44b4b control base"

    basenames = [Path(path).name for path in CONTROL_PATHS]
    matches = []
    for line in _r64_suffix_lines(root, rev):
        if (all(_matches_hash_prefix(line, value) for value in commits)
                and _matches_hash_prefix(line, pinned_base)
                and all(name in line for name in basenames)
                and re.search(r"\bcommitted\b", line, re.IGNORECASE)):
            matches.append(line)
    if matches:
        return True, "round-64 LOG line names committed controls %s + %s and base %s" % (
            commits[0][:8], commits[1][:8], pinned_base[:8])
    return False, ("no round-64 LOG line names both committed control basenames, "
                   "computed revisions, and computed base")


def _owned_axis_names(scorecard: str) -> set[str] | None:
    match = re.search(
        r"(?im)^Axes owned by this lane:\s*\*\*(.*?)\*\*", scorecard)
    if match is None:
        return None
    names = {name.casefold() for name in
             re.findall(r"[A-Za-z][A-Za-z0-9_-]*", match.group(1))}
    return names or None


def _axis_scores(scorecard: str) -> tuple[dict[str, Decimal] | None, str]:
    owned = _owned_axis_names(scorecard)
    if owned is None:
        return None, "SCORECARD lacks its owned-axes header sentence"
    lines = scorecard.splitlines()
    start = next((i for i, line in enumerate(lines)
                  if line.strip().casefold() == "## axes"), None)
    if start is None:
        return None, "SCORECARD has no ## axes section"

    scores: dict[str, Decimal] = {}
    for raw in lines[start + 1:]:
        line = raw.strip()
        if re.match(r"^#{1,6}\s", line):
            break
        if not line.startswith("|"):
            continue
        cells = [cell.strip() for cell in line.strip("|").split("|")]
        if len(cells) < 2:
            continue
        axis_match = re.match(r"([A-Za-z][A-Za-z0-9_-]*)", cells[0])
        if axis_match is None:
            continue
        axis = axis_match.group(1).casefold()
        if axis not in owned:
            continue
        score_match = re.match(r"\s*(\d+(?:\.\d+)?)\b", cells[1])
        if score_match is None:
            return None, "owned axis %s has no leading numeric table score" % axis
        try:
            scores[axis] = Decimal(score_match.group(1))
        except InvalidOperation:
            return None, "owned axis %s has an invalid table score" % axis

    if set(scores) != owned:
        return None, "axes section does not score every header-owned axis"
    return scores, "parsed %d header-owned axes" % len(scores)


def _score_text(score: Decimal) -> str:
    text = format(score, "f")
    return text.rstrip("0").rstrip(".") if "." in text else text


def check_lowest_axis(root: Path, rev: str) -> tuple[bool, str]:
    scorecard = show(root, rev, SCORECARD)
    if scorecard is None:
        return False, "%s absent at %s" % (SCORECARD, rev)
    scores, detail = _axis_scores(scorecard)
    if scores is None:
        return False, detail
    if "depth" not in scores or "consistency" not in scores:
        return False, "owned-axis header lacks depth or consistency"
    minimum = min(scores.values())
    lowest = [axis for axis, score in scores.items() if score == minimum]
    if (lowest != ["depth"] or scores["depth"] != Decimal("9")
            or scores["consistency"] != Decimal("10")):
        return False, ("computed owned minimum is %s at %s; expected depth 9 < consistency 10"
                       % (", ".join(lowest), _score_text(minimum)))

    depth_token = _number_token_re(_score_text(scores["depth"]))
    consistency_token = _number_token_re(_score_text(scores["consistency"]))
    for line in _r64_suffix_lines(root, rev):
        if (re.search(r"\blowest\b", line, re.IGNORECASE)
                and re.search(r"\bdepth\b", line, re.IGNORECASE)
                and re.search(r"\bconsistency\b", line, re.IGNORECASE)
                and depth_token.search(line)
                and consistency_token.search(line)):
            return True, "round-64 LOG suffix names depth 9 < consistency 10 as lowest"
    return False, "round-64 LOG suffix lacks lowest/depth/consistency and both computed scores"


def _check_call_nodes(node: ast.AST) -> list[ast.Call]:
    return [call for call in ast.walk(node)
            if isinstance(call, ast.Call)
            and isinstance(call.func, ast.Name)
            and call.func.id == "check"]


def _static_assertion_count(
        source: bytes) -> tuple[int | None, tuple[int, int, int] | None, str]:
    try:
        tree = ast.parse(source.decode("utf-8"))
    except (UnicodeDecodeError, SyntaxError) as error:
        return None, None, "r63 counter source is not parseable: %s" % error
    self_test = next((node for node in ast.walk(tree)
                      if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))
                      and node.name == "self_test"), None)
    if self_test is None:
        return None, None, "r63 counter source has no self_test function"

    total_sites = len(_check_call_nodes(self_test))
    loops: list[tuple[int, int]] = []
    for node in ast.walk(self_test):
        if (isinstance(node, ast.For)
                and isinstance(node.iter, (ast.Tuple, ast.List))):
            call_sites = len(_check_call_nodes(node))
            if call_sites:
                loops.append((call_sites, len(node.iter.elts)))
    if len(loops) != 1:
        return None, None, "r63 self-test lacks one literal counter-arm loop"
    loop_sites, arms = loops[0]
    fixed_sites = total_sites - loop_sites
    shape = (fixed_sites, loop_sites, arms)
    count = fixed_sites + loop_sites * arms
    detail = "%d fixed + %d loop sites x %d arms = %d" % (
        fixed_sites, loop_sites, arms, count)
    return count, shape, detail


def _materialized_tally(root: Path, rev: str) -> tuple[int | None, str]:
    source = show_bytes(root, rev, R63_COUNTER)
    if source is None:
        return None, "%s absent at %s" % (R63_COUNTER, rev)
    static_count, static_shape, static_detail = _static_assertion_count(source)
    if static_count is None or static_shape is None:
        return None, static_detail

    with tempfile.TemporaryDirectory(prefix="r64-r63-counter-") as directory:
        temp_root = Path(directory)
        verifier_dir = temp_root / "verifiers"
        verifier_dir.mkdir()
        script = verifier_dir / "check_r63_routed_repairs.py"
        script.write_bytes(source)
        proc = subprocess.run([sys.executable, "-B", str(script), "--self-test"],
                              cwd=temp_root, capture_output=True, text=True,
                              timeout=90)
    if proc.returncode != 0:
        output = (proc.stdout.strip().splitlines()[-1:]
                  + proc.stderr.strip().splitlines()[-1:])
        return None, "r63 --self-test exited %d%s" % (
            proc.returncode, (": " + " / ".join(output)) if output else "")
    counts = re.findall(r"\bover\s+(\d+)\s+assertions\b", proc.stdout)
    if not counts:
        return None, "r63 --self-test output has no `over N assertions` tally"
    runtime_count = int(counts[-1])
    if runtime_count != static_count:
        return None, "runtime %d disagrees with static %d (%s)" % (
            runtime_count, static_count, static_detail)
    if (static_count != EXPECTED_ASSERTIONS
            or static_shape != EXPECTED_STATIC_SHAPE):
        return None, "count is not the frozen 23 (%s; shape %s)" % (
            static_detail, static_shape)
    return runtime_count, "runtime %d matches static %s" % (
        runtime_count, static_detail)


def check_assertion_count(root: Path, rev: str) -> tuple[bool, str]:
    count, detail = _materialized_tally(root, rev)
    if count is None:
        return False, detail
    receipt = show(root, rev, PATCH_RECEIPT)
    if receipt is None:
        return False, "%s absent at %s; %s" % (PATCH_RECEIPT, rev, detail)
    additions = _added_lines(root, BASE_REV, rev, PATCH_RECEIPT)
    if additions is None:
        return False, "could not compare %s with BASE_REV" % PATCH_RECEIPT
    named = [line for line in additions
             if _hash_token_re(str(count)).search(line)
             and re.search(r"\bassertions\b", line, re.IGNORECASE)]
    if named:
        return True, "%s; added patch line names %d assertions" % (detail, count)
    return False, "%s; no BASE_REV-added patch line names %d assertions" % (
        detail, count)


CHECKS = (
    ("seat-edit-committed", check_seat_edit),
    ("control-revs-named", check_control_revs),
    ("lowest-axis-corrected", check_lowest_axis),
    ("assertion-count-named", check_assertion_count),
)


def base_control(root: Path) -> tuple[int, int]:
    closed = sum(1 for _, function in CHECKS if function(root, BASE_REV)[0])
    return closed, len(CHECKS)


def run(root: Path, rev: str) -> int:
    base_closed, total = base_control(root)
    if base_closed != 0:
        print("base arm failed: pinned do-nothing control at %s closed %d of %d; "
              "refusing to certify any revision unless the base is exactly 0 of %d"
              % (BASE_REV, base_closed, total, total), file=sys.stderr)
        return 1

    closed = 0
    for name, function in CHECKS:
        ok, detail = function(root, rev)
        closed += int(ok)
        print("%-4s %-22s %s" % ("PASS" if ok else "FAIL", name, detail))
    print("r63 routed defects closed %d of %d" % (closed, len(CHECKS)))
    if rev.lower() == BASE_REV:
        print("the pinned do-nothing control at %s is never a certification" %
              BASE_REV, file=sys.stderr)
        return 1
    return 0 if closed == len(CHECKS) else 1


# Dishonest counters are invoked as processes against constructed repositories.
LABEL_ONLY_SOURCE = '''#!/usr/bin/env python3
import argparse
import sys
ap = argparse.ArgumentParser()
ap.add_argument("--rev", required=True)
ap.add_argument("--root", required=True)
ap.parse_args()
print("r63 routed defects closed 4 of 4")
sys.exit(0)
'''

FINGERPRINT_SOURCE = '''#!/usr/bin/env python3
import argparse
import subprocess
import sys
ap = argparse.ArgumentParser()
ap.add_argument("--rev", required=True)
ap.add_argument("--root", required=True)
args = ap.parse_args()
def blob(path):
    p = subprocess.run(["git", "-C", args.root, "show",
                        "%s:%s" % (args.rev, path)],
                       capture_output=True, text=True)
    return p.stdout if p.returncode == 0 else ""
seat = blob(".ufo/waves/round-63/w2/MutW2SplitClauses.md")
log = blob("LOG.md")
patch = blob(".ufo/waves/round-63/w2/ExecW2E2Patch.md")
looks_repaired = ("temporal mismatch" in seat and "35d44b4b" in log
                  and "lowest" in log.lower() and "consistency 10" in log.lower()
                  and "23 assertions" in patch)
count = 4 if looks_repaired else 0
print("r63 routed defects closed %d of 4" % count)
sys.exit(0 if count == 4 else 1)
'''

WORKTREE_CHECK_SOURCE = '''def check_seat_edit(root: Path, rev: str) -> tuple[bool, str]:
    try:
        content = (root / SEAT_EDIT).read_text(encoding="utf-8")
    except OSError:
        content = ""
    found = SEAT_MARKER in content
    return found, ("worktree marker present" if found else "worktree marker absent")
'''

HARDCODED_COUNT_CHECK_SOURCE = '''def check_assertion_count(root: Path, rev: str) -> tuple[bool, str]:
    receipt = show(root, rev, PATCH_RECEIPT)
    if receipt is None:
        return False, "patch receipt absent"
    additions = _added_lines(root, BASE_REV, rev, PATCH_RECEIPT) or []
    named = any(_hash_token_re("23").search(line)
                and re.search(r"\\bassertions\\b", line, re.IGNORECASE)
                for line in additions)
    return named, "hardcoded 23 assertion receipt" if named else "not named"
'''


def _write(root: Path, path: str, content: str) -> None:
    target = root / path
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(content, encoding="utf-8")


def _commit(root: Path, message: str) -> str:
    env = os.environ.copy()
    env.update({
        "GIT_AUTHOR_NAME": "r64-selftest",
        "GIT_AUTHOR_EMAIL": "r64-selftest@example.invalid",
        "GIT_COMMITTER_NAME": "r64-selftest",
        "GIT_COMMITTER_EMAIL": "r64-selftest@example.invalid",
        "GIT_AUTHOR_DATE": "2026-10-24T12:00:00+00:00",
        "GIT_COMMITTER_DATE": "2026-10-24T12:00:00+00:00",
    })
    subprocess.run(["git", "-C", str(root), "add", "-A"], check=True,
                   capture_output=True)
    subprocess.run(["git", "-C", str(root), "-c", "commit.gpgsign=false",
                    "commit", "-m", message], check=True,
                   capture_output=True, env=env)
    proc = subprocess.run(["git", "-C", str(root), "rev-parse", "HEAD"],
                          check=True, capture_output=True, text=True)
    return proc.stdout.strip()


def _r63_fixture_source(fixed_calls: int = 17) -> str:
    lines = [
        "#!/usr/bin/env python3",
        "import sys",
        "def self_test():",
        "    assertions = 0",
        "    def check(*args):",
        "        nonlocal assertions",
        "        assertions += 1",
    ]
    lines.extend("    check('fixed-%d', True, True)" % index
                 for index in range(fixed_calls))
    lines.extend([
        "    for arm in (0, 1, 2):",
        "        check('reject', True, True)",
        "        check('honest', True, True)",
        "    print('self-test: 0 failure(s) over %d assertions' % assertions)",
        "if '--self-test' in sys.argv:",
        "    self_test()",
        "else:",
        "    raise SystemExit(2)",
        "",
    ])
    return "\n".join(lines)


def _scorecard_text(reordered: bool = False, move_table: bool = False) -> str:
    depth = "| depth | 9 | evidence contains | a raw bar | owned by header | 64 |\n"
    consistency = "| consistency (calibration sub-axis) | 10 | test | owned | 64 |\n"
    rows = consistency + depth if reordered else depth + consistency
    text = ("# Scorecard test\n"
            "Axes owned by this lane: **depth + consistency** (frozen)\n"
            "\n## axes\n"
            "| Axis | Score | Evidence | Owned? | Last change |\n"
            "|---|---:|---|---|---|\n"
            + rows + "| coverage | 8 | test | advisory | 64 |\n")
    if move_table:
        text += ("\n## Move log\n"
                 "| Axis | Score | Evidence | Owned? | Last change |\n"
                 "|---|---:|---|---|---|\n"
                 "| depth | 1 | unrelated later table | owned | 65 |\n")
    return text


def _seat_edit_text(lines: int = 82) -> str:
    return SEAT_MARKER + "\n" + "".join(
        "measured seat line %d\n" % index for index in range(lines - 1))


def _new_world(root: Path) -> tuple[str, str]:
    root.mkdir(parents=True)
    subprocess.run(["git", "-C", str(root), "init", "-q"], check=True,
                   capture_output=True)
    _write(root, LOG,
           "# kotoba test log\n\n## Round 63\n"
           "- historical references 8c4cefa8 cbbee56e 35d44b4b.\n")
    _write(root, SEAT_EDIT, "seat report without the correction marker\n")
    _write(root, SCORECARD, _scorecard_text())
    _write(root, PATCH_RECEIPT, "original patch receipt: 21 assertions\n")
    _write(root, R63_COUNTER, _r63_fixture_source())
    before_controls = _commit(root, "constructed pre-controls baseline")
    subprocess.run(["git", "-C", str(root), "update-ref",
                    "refs/heads/38defdc", before_controls], check=True,
                   capture_output=True)

    pinned_base = "35d44b4b4dcdda234b5dbff7af37e432fec55f05"
    _write(root, CONTROL_PATHS[0], "v31 do-nothing control at: %s\n" % pinned_base)
    _commit(root, "add first control")
    _write(root, CONTROL_PATHS[1], "before tip control at %s\n" % pinned_base)
    base_rev = _commit(root, "add second control")
    return before_controls, base_rev


def _control_inputs(root: Path, rev: str) -> tuple[tuple[str, str], str] | None:
    commits = tuple(_committing_rev(root, rev, path) for path in CONTROL_PATHS)
    if any(commit is None for commit in commits):
        return None
    base = _control_base(root, rev)
    if base is None:
        return None
    return (commits[0], commits[1]), base


def _control_line(root: Path, rev: str, full: bool = False,
                  base_token: str | None = None) -> str:
    values = _control_inputs(root, rev)
    if values is None:
        raise RuntimeError("constructed controls cannot be computed")
    commits, base = values
    tokens = commits if full else (commits[0][:8], commits[1][:8])
    base_name = base if full else base[:8]
    if base_token is not None:
        base_name = base_token
    return ("- committed %s at %s; %s at %s; pinned base %s." %
            (Path(CONTROL_PATHS[0]).name, tokens[0],
             Path(CONTROL_PATHS[1]).name, tokens[1], base_name))


def _axis_line() -> str:
    return "- lowest owned axis: depth 9 < consistency 10."


def _log_with_entry(base_log: str, control_line: str,
                    axis_line: str | None = None) -> str:
    return (base_log + "\n" + ROUND64_HEADER + "\n" + control_line + "\n"
            + (axis_line if axis_line is not None else _axis_line()) + "\n")


def _wrong_prefix(commit: str, other: str) -> str:
    for first in "0123456789abcdef":
        candidate = first + commit[1:7]
        if not commit.startswith(candidate) and not other.startswith(candidate):
            return candidate
    raise RuntimeError("could not construct a false commit prefix")


def _embedded_hash(prefix: str, hashes: tuple[str, ...]) -> str:
    for left in "0123456789abcdef":
        for right in "0123456789abcdef":
            token = left + prefix + right
            if not any(value.startswith(token) for value in hashes):
                return token
    raise RuntimeError("could not construct an embedded non-matching hash")


def _replace_function(source: str, function_name: str,
                      replacement: str) -> str:
    start = source.index("def %s(" % function_name)
    if function_name == "check_assertion_count":
        end = source.index("\n\nCHECKS =", start)
        return source[:start] + replacement.rstrip() + source[end:]
    end = source.index("\ndef ", start + 1)
    return source[:start] + replacement.rstrip() + "\n" + source[end:]


def _green_control_source(source: str) -> str:
    start = source.index("CHECKS = (")
    end = source.index("\ndef base_control", start)
    replacement = (
        "def _always_green(root: Path, rev: str) -> tuple[bool, str]:\n"
        "    return True, 'mutated green control'\n\n"
        "CHECKS = (\n"
        "    ('seat-edit-committed', _always_green),\n"
        "    ('control-revs-named', _always_green),\n"
        "    ('lowest-axis-corrected', _always_green),\n"
        "    ('assertion-count-named', _always_green),\n"
        ")\n")
    return source[:start] + replacement + source[end:]


def _candidate(path: Path, source: str, base_rev: str) -> list[str]:
    path.write_text(source.replace(BASE_REV_LITERAL, base_rev), encoding="utf-8")
    return [sys.executable, "-B", str(path)]


def _candidate_run(command: list[str], root: Path, rev: str) -> tuple[int, int]:
    try:
        proc = subprocess.run(command + ["--root", str(root), "--rev", rev],
                              capture_output=True, text=True, timeout=120)
    except (OSError, subprocess.SubprocessError):
        return -1, -1
    match = re.search(r"r63 routed defects closed (\d+) of 4", proc.stdout)
    return proc.returncode, int(match.group(1)) if match else -1


def _audit_counter(command: list[str], root: Path,
                   worlds: list[tuple[str, str, bool]]) -> tuple[bool, str]:
    okay = True
    notes: list[str] = []
    for label, rev, expect_certified in worlds:
        code, count = _candidate_run(command, root, rev)
        if expect_certified:
            passed = code == 0 and count == 4
            wanted = "rc=0 count=4"
        else:
            passed = code != 0 and 0 <= count < 4
            wanted = "rc!=0 count<4"
        notes.append("%s rc=%d count=%d want %s" %
                     (label, code, count, wanted))
        okay = okay and passed
    return okay, "; ".join(notes)


def _assert_argparse_rejects_base(command: list[str], rev: str) -> bool:
    try:
        proc = subprocess.run(command + ["--base", rev], capture_output=True,
                              text=True, timeout=30)
    except (OSError, subprocess.SubprocessError):
        return False
    return proc.returncode == 2


def self_test() -> int:
    failures = 0
    assertions = 0

    def check(name: str, actual: object, expected: object) -> None:
        nonlocal failures, assertions
        assertions += 1
        if actual != expected:
            failures += 1
            print("FAIL %s: got %r, expected %r" % (name, actual, expected))

    with tempfile.TemporaryDirectory(prefix="r64-routed-repairs-") as temp_name:
        temp = Path(temp_name)
        root = temp / "counter-world"
        pre_controls_rev, base_rev = _new_world(root)
        base_log = show(root, base_rev, LOG)
        if base_log is None:
            raise RuntimeError("constructed base LOG.md is missing")
        inputs = _control_inputs(root, base_rev)
        if inputs is None:
            raise RuntimeError("constructed control receipts cannot be derived")
        commits, pinned_base = inputs

        original_base = BASE_REV
        try:
            globals()["BASE_REV"] = base_rev
            base_results = {name: function(root, base_rev)[0]
                            for name, function in CHECKS}
            check("base: historical control tokens do not leak into r64 scan",
                  sum(base_results.values()), 0)
            check("base control: pinned baseline is exactly 0 of 4",
                  base_control(root), (0, 4))
            check("empty derivation: pre-control revision has no control commits",
                  check_control_revs(root, pre_controls_rev)[0], False)

            # The short-hash case is the target; marker + 82 added lines, both
            # computed control commits/base and both score tokens are present.
            _write(root, SEAT_EDIT, _seat_edit_text())
            _write(root, PATCH_RECEIPT,
                   "C2 patch tally measured by runtime and static reconstruction: 23 assertions\n")
            short_line = _control_line(root, base_rev)
            _write(root, LOG, _log_with_entry(base_log, short_line))
            target_rev = _commit(root, "constructed corrected target")
            target_results = {name: function(root, target_rev)[0]
                              for name, function in CHECKS}
            check("target: all four computed checks pass",
                  target_results, {name: True for name, _ in CHECKS})
            check("target: all four checks close", sum(target_results.values()), 4)

            # Full-length revisions are accepted alongside the 8-hex target.
            full_line = _control_line(root, target_rev, full=True)
            full_rev = _commit_log_variant(root, base_log, full_line)
            check("control hashes: full revisions are accepted",
                  check_control_revs(root, full_rev)[0], True)
            check("control hashes: >=7-hex short revisions are accepted",
                  check_control_revs(root, target_rev)[0], True)

            # The lane's round-heading convention carries a parenthetical:
            # the suffix anchor must accept it (and must not accept a
            # bare startswith sibling such as a future "Round 64b").
            paren_log = (base_log + "\n" + ROUND64_HEADER +
                         " (hyaku run 5, attempt 1)\n" + full_line + "\n" +
                         _axis_line() + "\n")
            _write(root, LOG, paren_log)
            paren_rev = _commit(root, "constructed parenthetical heading")
            check("heading: a parenthetical round heading still anchors the suffix",
                  {name: function(root, paren_rev)[0]
                   for name, function in CHECKS},
                  {name: True for name, _ in CHECKS})
            not_r64_log = (base_log + "\n## 2026-10-24 — Round 64b\n"
                           + full_line + "\n" + _axis_line() + "\n")
            _write(root, LOG, not_r64_log)
            not_r64_rev = _commit(root, "constructed round 64b sibling")
            check("heading: a Round-64b sibling heading does not anchor the suffix",
                  check_control_revs(root, not_r64_rev)[0], False)

            one_sided = ("- committed %s at %s; pinned base %s.\n"
                         "- committed %s at %s.\n" %
                         (Path(CONTROL_PATHS[0]).name, commits[0][:8],
                          pinned_base[:8], Path(CONTROL_PATHS[1]).name,
                          commits[1][:8]))
            one_sided_rev = _commit_log_variant(root, base_log, one_sided,
                                                append_axis=True)
            check("control citation: two separate one-sided lines fail",
                  check_control_revs(root, one_sided_rev)[0], False)

            wrong_first = _wrong_prefix(commits[0], commits[1])
            wrong_line = ("- committed %s at %s; %s at %s; pinned base %s."
                          % (Path(CONTROL_PATHS[0]).name, wrong_first,
                             Path(CONTROL_PATHS[1]).name, commits[1][:8],
                             pinned_base[:8]))
            wrong_rev = _commit_log_variant(root, base_log, wrong_line,
                                            append_axis=True)
            check("control citation: wrong committing revision fails",
                  check_control_revs(root, wrong_rev)[0], False)

            repinned_line = _control_line(root, target_rev,
                                          base_token="11111111")
            repinned_rev = _commit_log_variant(root, base_log, repinned_line)
            check("control citation: wrong pinned base fails",
                  check_control_revs(root, repinned_rev)[0], False)

            embedded_first = _embedded_hash(commits[0][:8], commits)
            embedded_second = _embedded_hash(commits[1][:8], commits)
            embedded_base = _embedded_hash(
                pinned_base[:8], (*commits, pinned_base))
            boundary_line = ("- committed %s at %s; %s at %s; pinned base %s."
                             % (Path(CONTROL_PATHS[0]).name, embedded_first,
                                Path(CONTROL_PATHS[1]).name, embedded_second,
                                embedded_base))
            boundary_rev = _commit_log_variant(root, base_log, boundary_line)
            check("control citation: hashes embedded in hex runs fail boundaries",
                  check_control_revs(root, boundary_rev)[0], False)

            lookalike_line = ("- %s and %s controls; 35d44b4b; committed."
                              % (commits[0][:8], commits[1][:8]))
            lookalike_rev = _commit_log_variant(root, base_log, lookalike_line)
            check("control citation: missing exact basenames fails",
                  check_control_revs(root, lookalike_rev)[0], False)

            # Check 1 rejects a marker-only note and enforces both added-line
            # presence and the frozen >=60-line numstat floor.
            _write(root, SEAT_EDIT, SEAT_MARKER + "\n")
            marker_only_rev = _commit(root, "marker-only seat note")
            check("seat edit: marker without the 60-line addition floor fails",
                  check_seat_edit(root, marker_only_rev)[0], False)

            _write(root, SEAT_EDIT, _seat_edit_text())
            _commit(root, "restore full seat correction after floor arm")

            # Check 3 uses only the ## axes section and handles reordered rows
            # and raw pipe characters in evidence cells.
            _write(root, SCORECARD, _scorecard_text(reordered=True, move_table=True))
            reordered_rev = _commit(root, "reordered axes plus later table")
            check("axes: reordered rows and later table preserve computed minimum",
                  check_lowest_axis(root, reordered_rev)[0], True)

            _write(root, LOG, _log_with_entry(base_log, short_line))
            # Check 4 computes runtime and static counts and requires an added
            # receipt line. Each receipt-side substitution must invalidate it.
            _write(root, R63_COUNTER, _r63_fixture_source(fixed_calls=18))
            substituted_source_rev = _commit(root, "substitute r63 self-test source")
            check("assertion source substitution rejects stale tally",
                  check_assertion_count(root, substituted_source_rev)[0], False)
            _write(root, R63_COUNTER, _r63_fixture_source())
            _write(root, PATCH_RECEIPT,
                   "C2 patch tally measured by runtime and static reconstruction: 24 assertions\n")
            substituted_patch_rev = _commit(root, "substitute patch count")
            check("assertion receipt substitution rejects wrong tally",
                  check_assertion_count(root, substituted_patch_rev)[0], False)
            _write(root, PATCH_RECEIPT,
                   "C2 patch tally measured by runtime and static reconstruction: 123 assertions\n")
            numeric_boundary_rev = _commit(root, "assertion boundary control")
            check("assertion boundary: 23 embedded in 123 does not count",
                  check_assertion_count(root, numeric_boundary_rev)[0], False)

            # Exercise a marker line that was already present at the comparison
            # ref: it is not a new addition and cannot credit check 1.
            marked_rev = numeric_boundary_rev
            subprocess.run(["git", "-C", str(root), "update-ref",
                            "refs/heads/38defdc", marked_rev], check=True,
                           capture_output=True)
            check("seat edit: old marker line is not an added marker line",
                  check_seat_edit(root, marked_rev)[0], False)
            subprocess.run(["git", "-C", str(root), "update-ref",
                            "refs/heads/38defdc", pre_controls_rev], check=True,
                           capture_output=True)

            # Process counter arms: label-only, fingerprint, and worktree-read.
            # The target is committed, then its marker is removed from disk.
            (root / SEAT_EDIT).unlink()
            source = Path(__file__).read_text(encoding="utf-8")
            worktree_source = _replace_function(
                source, "check_seat_edit", WORKTREE_CHECK_SOURCE)
            worlds = [("base", base_rev, False),
                      ("look-alike", wrong_rev, False),
                      ("target", target_rev, True)]
            for label, candidate_source in (
                    ("label-only", LABEL_ONLY_SOURCE),
                    ("fingerprint", FINGERPRINT_SOURCE),
                    ("worktree-read", worktree_source)):
                candidate_path = temp / (label + ".py")
                candidate = _candidate(candidate_path, candidate_source, base_rev)
                okay, detail = _audit_counter(candidate, root, worlds)
                check("counter arm: %s rejected by constructed worlds" % label,
                      okay, False)
                print("      %s: %s" % (label, detail))
                honest_path = temp / ("honest-" + label + ".py")
                honest = _candidate(honest_path, source, base_rev)
                okay, detail = _audit_counter(honest, root, worlds)
                check("counter arm: honest counter passes %s worlds" % label,
                      okay, True)
                print("      honest/%s: %s" % (label, detail))

            # A baseline with a partial suffix (three checks close) must also
            # refuse. Green and repointed controls are distinct refusal arms.
            partial_base_source = _candidate(
                temp / "partial-base.py", source, wrong_rev)
            partial_code, partial_count = _candidate_run(
                partial_base_source, root, target_rev)
            check("base arm: partial pinned control refuses certification",
                  partial_code != 0 and partial_count == -1, True)

            green_source = _green_control_source(source)
            green_counter = _candidate(temp / "green-control.py", green_source,
                                       base_rev)
            green_code, green_count = _candidate_run(green_counter, root, base_rev)
            check("base arm: green pinned control refuses certification",
                  green_code != 0 and green_count == -1, True)

            repointed = _candidate(temp / "repointed-base.py", source, target_rev)
            repointed_code, repointed_count = _candidate_run(
                repointed, root, target_rev)
            check("base arm: repointed green BASE_REV refuses certification",
                  repointed_code != 0 and repointed_count == -1, True)

            check("cli: --base is rejected by argparse with status 2",
                  _assert_argparse_rejects_base(honest, base_rev), True)

            hardcoded_source = _replace_function(
                source, "check_assertion_count", HARDCODED_COUNT_CHECK_SOURCE)
            hardcoded = _candidate(temp / "hardcoded-count.py",
                                   hardcoded_source, base_rev)
            okay, detail = _audit_counter(
                hardcoded, root,
                [("substituted-source", substituted_source_rev, False)])
            check("counter arm: hardcoded assertion tally is rejected",
                  okay, False)
            print("      hardcoded-count: %s" % detail)
            if okay:
                diagnostic = subprocess.run(
                    hardcoded + ["--root", str(root), "--rev",
                                 substituted_source_rev],
                    capture_output=True, text=True, timeout=120)
                print("      hardcoded-output: %s" %
                      diagnostic.stdout.strip().replace("\n", " / "))

            # Historical base LOG contains the old control citations. Without
            # a round-64 header, neither those nor pre-header bait count.
            check("baseline LOG leak: old control citations remain outside r64 suffix",
                  check_control_revs(root, base_rev)[0], False)

        finally:
            globals()["BASE_REV"] = original_base

    print("self-test: %d failure(s) over %d assertions" %
          (failures, assertions))
    return 1 if failures else 0


def _commit_log_variant(root: Path, base_log: str, control_line: str,
                        append_axis: bool = True) -> str:
    _write(root, LOG, _log_with_entry(
        base_log, control_line,
        _axis_line() if append_axis else "- no axis correction"))
    return _commit(root, "constructed LOG citation variant")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="round-64 C2 counter: round-63 routed repairs")
    parser.add_argument("--rev", help="full 40-hex revision to measure")
    parser.add_argument("--root", default=str(LANE), help="repository root")
    parser.add_argument("--self-test", action="store_true",
                        help="run constructed-world counter and substitution arms")
    args = parser.parse_args(argv)
    if args.self_test:
        return self_test()
    if args.rev is None or not REV_RE.fullmatch(args.rev):
        parser.error("--rev must be a full 40-hex revision (or use --self-test)")
    root = Path(args.root).resolve()
    repo = git(root, ["rev-parse", "--show-toplevel"])
    if repo.returncode != 0:
        print("error: %s is not a git checkout" % root, file=sys.stderr)
        return 2
    try:
        return run(root, args.rev.lower())
    except (OSError, subprocess.SubprocessError) as error:
        print("error: could not evaluate: %s" % error, file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())
