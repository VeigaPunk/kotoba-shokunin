#!/usr/bin/env python3
"""Executable verifier for kotoba corpus integrity (INDEX + POINTERS families).

What each check pins (id — mode — claim):

  corpus.index.tracked_files          (equal)  `git ls-files corpus/` row count.
  corpus.index.unindexed              (zero)   tracked corpus files (minus
                                               corpus/README.md) that no
                                               brace-expanded FILE-column pattern
                                               of corpus/README.md matches.
  corpus.index.stale_patterns         (zero)   corpus-internal FILE-column patterns
                                               that match no tracked corpus file.
  corpus.index.missing_paths          (zero)   FILE-column tokens (any, incl. `../`)
                                               that do not exist on disk relative
                                               to corpus/.
  corpus.pointers.report_total        (equal)  lane-report pointers (`.ufo/reports/
                                               round-N/*.md`, any shape: `../…`,
                                               `../../…`, host-absolute, `~/…`,
                                               bare) — the checked population.
  corpus.pointers.report_dead         (zero)   those that do not resolve from the
                                               citing file's directory.
  corpus.pointers.commit_total        (equal)  `commit `<hex>`` citations across
                                               tracked corpus *.md.
  corpus.pointers.commit_unresolvable (zero)   those where
                                               `git cat-file -e <hex>^{commit}` fails.
  corpus.pointers.commit_nonhash      (zero)   `commit `<token>`` where the token is
                                               not 7-40 hex chars (citations fully
                                               enclosed in double quotes are quoted
                                               meta-findings: see EXCLUDED below).

Scope, stated so the numbers are readable:

  * INDEX reads ONLY column 2 (File) of the coverage-map table rows in
    corpus/README.md. Matching is corpus-relative; findings print repo-relative.
  * POINTERS reads every tracked *.md under corpus/ (repo-relative), including
    corpus/README.md itself — this is the corpus verifier, so a `commit `<hex>``
    citation elsewhere in the repo is a different (unchecked) surface.
  * Both families are read from the working tree, not from HEAD: an uncommitted
    corpus edit is a legitimate observation (record `git status` in the baseline).
  * Determinism: every list is sorted, no network, no writes anywhere.

EXCLUDED — false-positive shapes deliberately out of scope. The checker MUST NOT
fail on them, and `--self-test` pins that it does not (each shape appears in a
fixture and the fixture asserts 0 findings):

  * illustrative prose path shapes (`../sibling/SKILL.md`,
    `../bailian-protocol/…`, `../sibling/`) — INDEX never reads prose or the
    Basis column, only backticked tokens in a File cell.
  * quoted meta-findings — a document quoting another document's text, e.g. the
    `"commit `round-N`"` cell in corpus/lessons/round-6-aggregator-audit.md:45
    or `../godspeed-core/directive.md` inside the round-6 agent-def audit table.
    A commit citation fully enclosed in double quotes on its line is recorded in
    `commit_quoted_detail` (context), never in `commit_nonhash`.
  * quoted report pointers — the same idiom for a report path a document is
    *reporting on* rather than promising: a dead pointer named inside double
    quotes on its line (e.g. the root a cold run probed and found ABSENT) is
    recorded in `report_pointers_quoted_detail` (context), never in
    `report_dead`. Without this, a corpus file cannot describe a defect it just
    documented: round 11's own cold-run record and artifact tripped the check
    that way, which is how the idiom was forced.
  * deliberately recorded dead paths (SKILL.md:588's `~/wikillm`, `~/.xbgst`
    drift list) — SKILL.md is outside corpus/ and is never scanned; inside
    corpus/ a `~`-anchored token that is not a `.ufo/reports/...` pointer is not
    a citation subject at all.
  * ellipsis/schematic pointers (`corpus/.../.ufo/reports/round-3/kotoba.md`) and
    glued prose (`x../.ufo/reports/round-3/kotoba.md`) — `is_excluded_pointer`
    rejects any token whose path segments after the leading `../` hops contain
    `..`, and the regex lookbehind refuses to start mid-token.
  * placeholder pointers (`.ufo/reports/round-1/<lane>.md`) — a `<`/`>` marker
    means the token is a template, not a promise; counted in
    `report_pointers_excluded_detail`, never in `report_dead`.
  * globs (`knowledge/*.md`, `.ufo/prompts/*-L1.md`) — expanded with fnmatch for
    index coverage; a glob is never tested for on-disk existence, because a
    pattern is not a path.
  * single-quoted code literals (`t.slice(0, _8n-1)`, `_8n`) — not backticked
    FILE-column tokens, so never harvested.

Exit codes mirror verifiers/verify_harness_claims.py: 0 all agree, 1 drift,
2 environment unreadable (not a git repo / corpus missing), 3 no baseline.
`--no-baseline` suppresses the comparison, so `equal` ids report OBSERVE — but a
`zero` violation is baseline-independent and still exits 1. Exit 3 is only for a
baseline that was expected (no `--no-baseline`) and absent, and is returned in
JSON mode too.

Conventions mirrored from verifiers/verify_harness_claims.py: argparse surface
(--json, --self-test, --no-baseline, --baseline, --repo), Inconclusive for
exit 2, CHECKS as id -> (mode, extractor) over a flat observation dict,
`{"observed": ..., "results": ...}` under --json, `N failure(s) over M
assertions` for --self-test. The baseline default is repo-relative
(<repo>/verifiers/corpus-baseline.json) rather than script-relative, because the
baseline is a property of the tree being checked.
"""

from __future__ import annotations

import argparse
import fnmatch
import json
import re
import subprocess
import sys
from pathlib import Path

# ---------------------------------------------------------------------------
# layout
# ---------------------------------------------------------------------------
CORPUS_DIR = "corpus"
INDEX_REL = "corpus/README.md"      # repo-relative, for findings and reads
INDEX_NAME = "README.md"            # corpus-relative, for tracked-set comparison
BASELINE_NAME = "corpus-baseline.json"
DEFAULT_REPO = Path(__file__).resolve().parent.parent

# a FILE-column token carrying any of these is a placeholder/prose shape, not a
# path this repo promises (see the EXCLUDED block)
GLOB_CHARS = "*?["
PLACEHOLDER_MARKS = ("<", ">", "\u2026", "$", "\\")

# Every lane-report pointer shape, rooted or not (`../.ufo/…`, `../../.ufo/…`,
# `/home/…/.ufo/…`, `~/…/.ufo/…`, bare `.ufo/…`). Round 11 widened this from
# the relative form alone: the repair moved 9 README pointers to host-absolute,
# so a relative-only class would then read `0/0` — a check that pins nothing.
# All shapes are checked; see `is_excluded_pointer` for the
# schematic/placeholder shapes that are context instead of pointers.
UFO_POINTER_RE = re.compile(
    r"(?<![\w.\-/])((?:/|~|(?:\.\.?/)*)[^\s`]*?\.ufo/reports/round-\d+/[^\s`]*\.md)"
)
# `commit `<token>`` as a citation; the lookbehind keeps `pre-commit `/`commits `
# out, and the token must be backticked.
COMMIT_RE = re.compile(r"(?<![A-Za-z0-9_-])commit[ \t]+`([^`\n]+)`")
HEX_RE = re.compile(r"\A[0-9a-fA-F]{7,40}\Z")
BACKTICK_RE = re.compile(r"`([^`]+)`")
BRACE_RE = re.compile(r"\{([^{}]*)\}")
BRACE_LIMIT = 64

# ---------------------------------------------------------------------------
# model: brace/glob expansion, token filters  (all pure, all unit-tested below)
# ---------------------------------------------------------------------------


def expand_braces(pattern: str, limit: int = BRACE_LIMIT) -> list[str]:
    """Expand `{a,b}` alternation groups (recursively), sorted and deduped.

    `lessons/round-{1,4,5}-aggregator-audit.md` -> 3 paths. Unbalanced or
    nested-brace-free inputs pass through unchanged.
    """
    variants = [pattern]
    while True:
        nxt: list[str] = []
        changed = False
        for variant in variants:
            match = BRACE_RE.search(variant)
            if not match:
                nxt.append(variant)
                continue
            changed = True
            head, tail = variant[: match.start()], variant[match.end() :]
            for alt in match.group(1).split(","):
                nxt.append(head + alt + tail)
        variants = nxt
        if not changed or len(variants) > limit:
            break
    return sorted(set(variants))


def has_glob(token: str) -> bool:
    return any(c in token for c in GLOB_CHARS)


def is_excluded_token(token: str) -> bool:
    """Placeholder/prose/host-absolute token — never checked as a corpus path."""
    if not token or any(mark in token for mark in PLACEHOLDER_MARKS):
        return True
    if any(c.isspace() for c in token):
        return True
    if token.startswith(("/", "~")) or token.endswith("/"):
        return True
    return False


def is_corpus_internal(token: str) -> bool:
    """A pattern that promises a file inside corpus/ (not `../x`, not absolute)."""
    return not token.startswith(("../", "/", "~"))


def expand_pattern(pattern: str, tracked: set[str]) -> set[str]:
    """Tracked corpus files a FILE-column pattern denotes (exact or fnmatch)."""
    hits: set[str] = set()
    for variant in expand_braces(pattern):
        if has_glob(variant):
            hits.update(t for t in tracked if fnmatch.fnmatchcase(t, variant))
        elif variant in tracked:
            hits.add(variant)
    return hits


def resolve_pointer(base: Path, token: str) -> Path:
    """Resolve a report-pointer token: rooted forms as-is, others from `base`."""
    if token.startswith("~"):
        return Path(token).expanduser().resolve()
    if token.startswith("/"):
        return Path(token).resolve()
    return (base / token).resolve()


def is_excluded_pointer(token: str) -> bool:
    """Schematic/placeholder report-pointer token — context, not a promise.

    Excluded: placeholder marks (`<lane>`), whitespace, globs, and any token
    whose path segments after the leading `../` hops still contain `..`
    (an ellipsis prefix `corpus/.../.ufo/…`, or glued prose `x../.ufo/…`).
    """
    if not token or any(mark in token for mark in PLACEHOLDER_MARKS):
        return True
    if any(c.isspace() for c in token) or has_glob(token):
        return True
    rest = re.sub(r"^(?:\.{1,2}/)+", "", token).lstrip("/~")
    return any(".." in seg for seg in rest.split("/"))


def pointer_shape(token: str) -> str:
    """Class of a checked report pointer: relative | absolute | tilde | bare."""
    if token.startswith("/"):
        return "absolute"
    if token.startswith("~"):
        return "tilde"
    if token.startswith(("./", "../")):
        return "relative"
    return "bare"


def is_hex_object_id(token: str) -> bool:
    """git object id: 7-40 hex chars (case-insensitive; git accepts either)."""
    return HEX_RE.match(token) is not None


def commit_peel_arg(token: str) -> str:
    """git object expression that requires `token` to name a commit."""
    return token + "^{commit}"


def inside_quotes(line: str, start: int, end: int) -> bool:
    """True when line[start:end] is fully enclosed in double quotes.

    That is the quoted-meta-finding shape: a document reporting another
    document's text. Such a citation is context, not this corpus's own pointer.
    """
    return line.count('"', 0, start) % 2 == 1 and '"' in line[end:]


# ---------------------------------------------------------------------------
# INDEX: coverage-map table in corpus/README.md
# ---------------------------------------------------------------------------
def file_column_tokens(readme_text: str) -> list[tuple[int, str]]:
    """(line, token) for every backticked token in column 2 of a table row."""
    out: list[tuple[int, str]] = []
    for line_no, line in enumerate(readme_text.splitlines(), 1):
        if not line.startswith("|"):
            continue
        cells = line.split("|")
        if len(cells) < 4:  # '', Area, File, Basis, ''
            continue
        file_cell = cells[2]
        if set(file_cell.strip()) <= set("-: "):  # |---|---| separator row
            continue
        for token in BACKTICK_RE.findall(file_cell):
            token = token.strip()
            if is_excluded_token(token):
                continue
            out.append((line_no, token))
    return out


def index_findings(
    readme_text: str, tracked: list[str], exists, *, index_rel: str = INDEX_REL
) -> dict:
    """Index-coverage verdicts.

    tracked: sorted corpus-relative tracked paths (README.md included).
    exists:  corpus-relative path -> bool (on-disk, follows `../` out of corpus).
    """
    tracked_set = set(tracked)
    tokens = file_column_tokens(readme_text)

    covered: set[str] = set()
    stale: list[str] = []
    missing: list[str] = []
    for line_no, token in tokens:
        hits = expand_pattern(token, tracked_set)
        covered |= hits
        if is_corpus_internal(token) and not hits:
            stale.append(f"{index_rel}:{line_no}: {token}")
        if has_glob(token):
            continue  # a pattern is not a path (EXCLUDED: globs)
        for variant in expand_braces(token):
            if has_glob(variant):
                continue
            if not exists(variant):
                missing.append(f"{index_rel}:{line_no}: {token} -> {variant}")

    unindexed_names = [t for t in tracked if t != INDEX_NAME and t not in covered]
    unindexed = [f"{CORPUS_DIR}/{t}" for t in unindexed_names]
    return {
        "index_patterns": len(tokens),
        "unindexed": len(unindexed),
        "unindexed_detail": sorted(unindexed),
        "stale_patterns": len(stale),
        "stale_patterns_detail": sorted(stale),
        "missing_paths": len(missing),
        "missing_paths_detail": sorted(missing),
    }


# ---------------------------------------------------------------------------
# POINTERS: report pointers and commit citations inside tracked corpus *.md
# ---------------------------------------------------------------------------
def citation_findings(rel: str, text: str, pointer_exists, commit_resolves) -> dict:
    """Per-file citation verdicts (pure; I/O injected for --self-test).

    pointer_exists(base: Path, token: str) -> bool
    commit_resolves(hex_token: str) -> bool
    """
    base = Path(rel).parent
    report_dead: list[str] = []
    report_excluded: list[str] = []
    report_quoted: list[str] = []
    pointer_shapes = {"relative": 0, "absolute": 0, "tilde": 0, "bare": 0}
    unresolvable: list[str] = []
    nonhash: list[str] = []
    quoted: list[str] = []
    report_total = 0
    commit_total = 0
    for line_no, line in enumerate(text.splitlines(), 1):
        for match in UFO_POINTER_RE.finditer(line):
            token = match.group(0)
            if is_excluded_pointer(token):
                report_excluded.append(f"{rel}:{line_no}: {token}")
                continue
            if inside_quotes(line, match.start(0), match.end(0)):
                report_quoted.append(f"{rel}:{line_no}: {token}")
                continue
            report_total += 1
            pointer_shapes[pointer_shape(token)] += 1
            if not pointer_exists(base, token):
                report_dead.append(f"{rel}:{line_no}: {token}")
        for match in COMMIT_RE.finditer(line):
            token = match.group(1)
            if inside_quotes(line, match.start(1), match.end(1)):
                quoted.append(f"{rel}:{line_no}: {token} (quoted meta-finding)")
                continue
            if not is_hex_object_id(token):
                nonhash.append(f"{rel}:{line_no}: {token}")
                continue
            commit_total += 1
            if not commit_resolves(token.lower()):
                unresolvable.append(f"{rel}:{line_no}: {token}")
    return {
        "report_total": report_total,
        "report_pointer_shapes": pointer_shapes,
        "report_pointers_excluded": len(report_excluded),
        "report_pointers_excluded_detail": sorted(report_excluded),
        "report_dead": len(report_dead),
        "report_dead_detail": sorted(report_dead),
        "commit_total": commit_total,
        "commit_unresolvable": len(unresolvable),
        "commit_unresolvable_detail": sorted(unresolvable),
        "commit_nonhash": len(nonhash),
        "commit_nonhash_detail": sorted(nonhash),
        "commit_quoted_excluded": len(quoted),
        "commit_quoted_detail": sorted(quoted),
    }


# ---------------------------------------------------------------------------
# collection: git + working tree
# ---------------------------------------------------------------------------
class Inconclusive(Exception):
    """Environment cannot answer the question (exit 2)."""


def git(repo: Path, *args: str) -> str:
    """`git -C repo args` stdout; any nonzero exit is an unreadable environment."""
    try:
        proc = subprocess.run(
            ["git", "-C", str(repo), *args],
            capture_output=True,
            text=True,
            check=False,
        )
    except FileNotFoundError as exc:  # no git binary
        raise Inconclusive(f"git not found: {exc}") from exc
    if proc.returncode != 0:
        raise Inconclusive(f"git {' '.join(args)} failed in {repo}: {proc.stderr.strip()}")
    return proc.stdout


def git_ok(repo: Path, *args: str) -> bool:
    """Same, but a nonzero exit is the answer (`cat-file -e` object presence)."""
    proc = subprocess.run(
        ["git", "-C", str(repo), *args], capture_output=True, text=True, check=False
    )
    return proc.returncode == 0


def tracked_corpus_files(repo: Path) -> list[str]:
    """Sorted corpus-relative paths of `git ls-files corpus/`."""
    out = git(repo, "ls-files", CORPUS_DIR)
    prefix = CORPUS_DIR + "/"
    paths = [l.strip() for l in out.splitlines() if l.strip()]
    return sorted(p[len(prefix) :] if p.startswith(prefix) else p for p in paths)


def corpus_observations(repo: Path) -> dict:
    """Flat observation dict for every check id in CHECKS."""
    repo = Path(repo).resolve()
    if not repo.is_dir():
        raise Inconclusive(f"repo directory not found: {repo}")
    git(repo, "rev-parse", "--git-dir")  # exit 2 when repo is not a git repo
    corpus_dir = repo / CORPUS_DIR
    index_path = repo / INDEX_REL
    if not corpus_dir.is_dir():
        raise Inconclusive(f"corpus directory not found: {corpus_dir}")
    if not index_path.is_file():
        raise Inconclusive(f"index not readable: {index_path}")

    tracked = tracked_corpus_files(repo)
    readme = index_path.read_text(encoding="utf-8", errors="replace")

    obs: dict = {"tracked_files": len(tracked)}
    obs.update(index_findings(readme, tracked, lambda p: (corpus_dir / p).exists()))

    md_files = [t for t in tracked if t.endswith(".md")]
    agg = {
        "report_total": 0,
        "report_pointers_excluded": 0,
        "report_dead": 0,
        "commit_total": 0,
        "commit_unresolvable": 0,
        "commit_nonhash": 0,
        "commit_quoted_excluded": 0,
    }
    shapes = {"relative": 0, "absolute": 0, "tilde": 0, "bare": 0}
    details: dict[str, list[str]] = {
        "report_dead_detail": [],
        "report_pointers_excluded_detail": [],
        "commit_unresolvable_detail": [],
        "commit_nonhash_detail": [],
        "commit_quoted_detail": [],
    }
    for rel in md_files:
        rel_repo = f"{CORPUS_DIR}/{rel}"  # findings speak repo-relative
        target = repo / rel_repo
        try:
            text = target.read_text(encoding="utf-8", errors="replace")
        except OSError as exc:
            raise Inconclusive(f"cannot read tracked file {rel_repo}: {exc}") from exc
        found = citation_findings(
            rel_repo,
            text,
            # base = the citing file's own directory, as written in its path
            lambda base, token, _repo=repo: resolve_pointer(_repo / base, token).is_file(),
            lambda hex_id, _repo=repo: git_ok(
                _repo, "cat-file", "-e", commit_peel_arg(hex_id)
            ),
        )
        for key in agg:
            agg[key] += found[key]
        for shape, value in found["report_pointer_shapes"].items():
            shapes[shape] += value
        for key in details:
            details[key].extend(found[key])

    obs.update(agg)
    obs["report_pointer_shapes"] = shapes
    for key, values in details.items():
        obs[key] = sorted(values)
    obs["corpus_md_files"] = len(md_files)
    return obs


# ---------------------------------------------------------------------------
# check layer
# ---------------------------------------------------------------------------
# id -> (mode, extractor). mode: equal (baseline-compared) | zero (baseline-free)
CHECKS: dict[str, tuple[str, str]] = {
    "corpus.index.tracked_files": ("equal", "tracked_files"),
    "corpus.index.unindexed": ("zero", "unindexed"),
    "corpus.index.stale_patterns": ("zero", "stale_patterns"),
    "corpus.index.missing_paths": ("zero", "missing_paths"),
    "corpus.pointers.report_total": ("equal", "report_total"),
    "corpus.pointers.report_dead": ("zero", "report_dead"),
    "corpus.pointers.commit_total": ("equal", "commit_total"),
    "corpus.pointers.commit_unresolvable": ("zero", "commit_unresolvable"),
    "corpus.pointers.commit_nonhash": ("zero", "commit_nonhash"),
}
EXTRACT_KEYS = {key for _, key in CHECKS.values()}
DETAIL_KEYS = (
    "unindexed_detail",
    "stale_patterns_detail",
    "missing_paths_detail",
    "report_dead_detail",
    "report_pointers_excluded_detail",
    "commit_unresolvable_detail",
    "commit_nonhash_detail",
    "commit_quoted_detail",
)


def evaluate(observed: dict, baseline: dict | None) -> list[dict]:
    """`equal` needs a baseline; `zero` is baseline-free and always adjudicated."""
    results = []
    for cid, (mode, key) in CHECKS.items():
        value = observed[key]
        row = {"check": cid, "mode": mode, "observed": value}
        if mode == "zero":
            ok = (value == 0) or (isinstance(value, (dict, list)) and not value)
            row["expected"] = "0 / empty"
        elif baseline is None:
            ok, row["expected"] = None, "baseline"
        else:
            want = baseline["checks"].get(cid, {}).get("expect")
            row["expected"] = want
            ok = value == want
        row["verdict"] = "PASS" if ok else ("OBSERVE" if ok is None else "DRIFT")
        results.append(row)
    return results


# ---------------------------------------------------------------------------
# self-test: falsify this file's matcher model on fixtures
# ---------------------------------------------------------------------------
FIXTURE_README = """# fixture corpus

| Area | File | Basis |
|------|------|-------|
| Knowledge a | `knowledge/a.md` | basis |
| Fleet audits | `lessons/round-{1,4,5}-aggregator-audit.md` | prior reviews |
| Basis-only token | `knowledge/b.md` | cites `knowledge/absent-basis.md` |
| Glob row | `lessons/*-audit.md` | basis |
| Stale | `lessons/gone.md` | basis |
| Missing path | `../nowhere/absent.py` | basis |
| Cross-repo | `../verifiers/verify_harness_claims.py` | basis |

## Known gaps

- illustrative prose shapes: `../sibling/SKILL.md`, `../bailian-protocol/\u2026`, `../sibling/`
- quoted meta-finding: `../godspeed-core/directive.md`
- deliberate dead paths: `~/wikillm`, `~/.xbgst`
- code literal: `t.slice(0, _8n-1)`
"""

FIXTURE_TRACKED = [
    "README.md",
    "knowledge/a.md",
    "knowledge/b.md",
    "lessons/round-1-aggregator-audit.md",
    "lessons/round-4-aggregator-audit.md",
    "lessons/round-5-aggregator-audit.md",
    "lessons/round-9-audit.md",  # covered only by the `lessons/*-audit.md` glob row
]
FIXTURE_ON_DISK = {
    "knowledge/a.md",
    "knowledge/b.md",
    "lessons/round-1-aggregator-audit.md",
    "lessons/round-4-aggregator-audit.md",
    "lessons/round-5-aggregator-audit.md",
    "lessons/round-9-audit.md",
    "lessons/gone.md",  # stale (untracked) but present on disk: not a missing path
    "../verifiers/verify_harness_claims.py",
}

FIXTURE_CITES = """round-7 lessons

LOG.md round-7, commit `3b029b8`, report `../../.ufo/reports/round-7/kotoba.md`
LOG.md round-8, commit `round-8`, report `../.ufo/reports/round-8/kotoba.md`
| `corpus/lessons/round-{1,4,5,6,7}.md:3`, `corpus/README.md:23-25` "commit `round-N`" | `git rev-parse --verify round-5` | fail |
Evidence: commit `8c300ad` ("round-8 report")
pre-commit `deadbee` hook
"""


FIXTURE_POINTER_SHAPES = """round-3 lessons

bare: `.ufo/reports/round-3/kotoba.md`
hosted: `/home/vgpnk/projects/shokunin/.ufo/reports/round-7/kotoba.md`
tilde: `~/projects/shokunin/.ufo/reports/round-1/kotoba.md`
relative: `../.ufo/reports/round-3/kotoba.md`
"""


def self_test() -> int:
    """Falsify this file's model of brace expansion, token filtering, non-hash
    detection and pointer resolution. A failure means the script is wrong, or a
    fixture no longer encodes the class it pins — never that the host is wrong.
    """
    failures: list[str] = []
    count = 0

    def eq(label: str, got, want) -> None:
        nonlocal count
        count += 1
        if got != want:
            failures.append(f"{label}: got {got!r} want {want!r}")

    # --- brace expansion -------------------------------------------------
    eq(
        "braces/3-way",
        expand_braces("lessons/round-{1,4,5}-aggregator-audit.md"),
        [
            "lessons/round-1-aggregator-audit.md",
            "lessons/round-4-aggregator-audit.md",
            "lessons/round-5-aggregator-audit.md",
        ],
    )
    eq(
        "braces/two-groups",
        expand_braces("a/{1,2}/b-{x,y}.md"),
        ["a/1/b-x.md", "a/1/b-y.md", "a/2/b-x.md", "a/2/b-y.md"],
    )
    eq("braces/none", expand_braces("plain.md"), ["plain.md"])
    eq("braces/single-alt", expand_braces("{7}"), ["7"])
    eq("braces/sorted", expand_braces("{9,8}"), ["8", "9"])
    eq(
        "braces/glob+brace",
        expand_braces("lessons/round-{1,4,5}*.md"),
        [
            "lessons/round-1*.md",
            "lessons/round-4*.md",
            "lessons/round-5*.md",
        ],
    )

    # --- pattern -> tracked-set matching ---------------------------------
    eq(
        "match/brace-row",
        expand_pattern("lessons/round-{1,4,5}-aggregator-audit.md", set(FIXTURE_TRACKED)),
        {
            "lessons/round-1-aggregator-audit.md",
            "lessons/round-4-aggregator-audit.md",
            "lessons/round-5-aggregator-audit.md",
        },
    )
    eq(
        "match/glob-scoped",
        expand_pattern("knowledge/*.md", set(FIXTURE_TRACKED)),
        {"knowledge/a.md", "knowledge/b.md"},
    )
    eq(
        "match/brace+glob",
        expand_pattern("lessons/round-{1,4,5}*.md", set(FIXTURE_TRACKED)),
        {
            "lessons/round-1-aggregator-audit.md",
            "lessons/round-4-aggregator-audit.md",
            "lessons/round-5-aggregator-audit.md",
        },
    )
    eq("match/absent", expand_pattern("knowledge/absent.md", set(FIXTURE_TRACKED)), set())

    # --- hex / non-hash model -------------------------------------------
    eq("hex/7-chars", is_hex_object_id("abef8aa"), True)
    eq("hex/40-chars", is_hex_object_id("a" * 40), True)
    eq("hex/41-chars", is_hex_object_id("a" * 41), False)
    eq("hex/6-chars", is_hex_object_id("3b029b"), False)
    eq("hex/uppercase", is_hex_object_id("3B029B8"), True)
    eq("hex/ref-token", is_hex_object_id("round-10"), False)
    eq("hex/placeholder", is_hex_object_id("round-N"), False)
    # the cat-file argument must literally end in `^{commit}`: a bare ref would
    # resolve trees and blobs too, and an f-string `{commit}` would raise here.
    eq("hex/peel-arg", commit_peel_arg("Abef8Aa".lower()), "abef8aa^{commit}")

    # --- report pointer regex + resolution ------------------------------
    eq(
        "pointer/match",
        [m.group(0) for m in UFO_POINTER_RE.finditer("report `../../.ufo/reports/round-7/kotoba.md`")],
        ["../../.ufo/reports/round-7/kotoba.md"],
    )
    eq("pointer/no-match/other", UFO_POINTER_RE.findall("`../verifiers/baseline.json`"), [])
    # excluded shapes: the regex may see them (the bare/glued prefix is legal
    # path text) but `is_excluded_pointer` must reject every one, so none is
    # ever resolved or counted as checked.
    eq(
        "pointer/excluded/placeholder",
        [t for t in UFO_POINTER_RE.findall("`.ufo/reports/round-<N>/<id>.md`") if not is_excluded_pointer(t)],
        [],
    )
    eq("pointer/excluded/ellipsis", is_excluded_pointer("corpus/.../.ufo/reports/round-3/kotoba.md"), True)
    eq("pointer/excluded/glued", is_excluded_pointer("x../.ufo/reports/round-3/kotoba.md"), True)
    eq("pointer/excluded/glob", is_excluded_pointer(".ufo/reports/round-*/*.md"), True)
    eq("pointer/kept/relative", is_excluded_pointer("../../.ufo/reports/round-7/kotoba.md"), False)
    eq("pointer/kept/absolute", is_excluded_pointer("/home/x/.ufo/reports/round-7/kotoba.md"), False)
    eq("pointer/kept/bare", is_excluded_pointer(".ufo/reports/round-3/kotoba.md"), False)
    # every shape is harvested, and each is checked
    eq(
        "pointer/all-shapes/relative",
        [m.group(0) for m in UFO_POINTER_RE.finditer("`../../.ufo/reports/round-7/kotoba.md`")],
        ["../../.ufo/reports/round-7/kotoba.md"],
    )
    eq(
        "pointer/all-shapes/absolute",
        [m.group(0) for m in UFO_POINTER_RE.finditer("`/home/vgpnk/projects/shokunin/.ufo/reports/round-7/kotoba.md`")],
        ["/home/vgpnk/projects/shokunin/.ufo/reports/round-7/kotoba.md"],
    )
    eq(
        "pointer/all-shapes/tilde",
        [m.group(0) for m in UFO_POINTER_RE.finditer("`~/projects/shokunin/.ufo/reports/round-1/kotoba.md`")],
        ["~/projects/shokunin/.ufo/reports/round-1/kotoba.md"],
    )
    eq(
        "pointer/all-shapes/bare",
        [m.group(0) for m in UFO_POINTER_RE.finditer("`.ufo/reports/round-3/kotoba.md`")],
        [".ufo/reports/round-3/kotoba.md"],
    )
    shapes = citation_findings(
        "corpus/lessons/round-3.md",
        FIXTURE_POINTER_SHAPES,
        lambda base, token: False,  # nothing resolves: the fixture is a dead-tree stand-in
        lambda hex_id: True,
    )
    eq("shapes/all-checked", shapes["report_total"], 4)
    eq("shapes/excluded", shapes["report_pointers_excluded"], 0)
    eq(
        "shapes/class-counts",
        shapes["report_pointer_shapes"],
        {"relative": 1, "absolute": 1, "tilde": 1, "bare": 1},
    )
    eq("shape/absolute", pointer_shape("/home/x/.ufo/reports/round-1/kotoba.md"), "absolute")
    eq("shape/tilde", pointer_shape("~/projects/shokunin/.ufo/reports/round-1/kotoba.md"), "tilde")
    eq("shape/bare", pointer_shape(".ufo/reports/round-3/kotoba.md"), "bare")
    eq("shape/relative", pointer_shape("../.ufo/reports/round-3/kotoba.md"), "relative")
    eq("shapes/dead", shapes["report_dead"], 4)
    eq(
        "shapes/dead-detail",
        shapes["report_dead_detail"],
        [
            "corpus/lessons/round-3.md:3: .ufo/reports/round-3/kotoba.md",
            "corpus/lessons/round-3.md:4: /home/vgpnk/projects/shokunin/.ufo/reports/round-7/kotoba.md",
            "corpus/lessons/round-3.md:5: ~/projects/shokunin/.ufo/reports/round-1/kotoba.md",
            "corpus/lessons/round-3.md:6: ../.ufo/reports/round-3/kotoba.md",
        ],
    )
    eq(
        "resolve/one-up",
        str(resolve_pointer(Path("/r/corpus/lessons"), "../.ufo/reports/round-7/kotoba.md")),
        "/r/corpus/.ufo/reports/round-7/kotoba.md",
    )
    eq(
        "resolve/two-up",
        str(resolve_pointer(Path("/r/corpus/lessons"), "../../.ufo/reports/round-7/kotoba.md")),
        "/r/.ufo/reports/round-7/kotoba.md",
    )
    eq(
        "resolve/from-corpus",
        str(resolve_pointer(Path("/r/x/corpus"), "../../.ufo/reports/round-7/kotoba.md")),
        "/r/.ufo/reports/round-7/kotoba.md",
    )

    # --- citation fixture: pointers, commits, quoted meta-findings -------
    found = citation_findings(
        "corpus/README.md",
        FIXTURE_CITES,
        lambda base, token: str(resolve_pointer(base, token)).endswith("round-7/kotoba.md"),
        lambda hex_id: hex_id == "3b029b8",
    )
    eq("cites/report-total", found["report_total"], 2)
    eq("cites/report-dead", found["report_dead"], 1)
    eq(
        "cites/report-dead-detail",
        found["report_dead_detail"],
        ["corpus/README.md:4: ../.ufo/reports/round-8/kotoba.md"],
    )
    # `3b029b8` (line 3) and `8c300ad` (line 6) are citations; `deadbee` in
    # `pre-commit `deadbee`` is not (lookbehind), so total is 2, not 3.
    eq("cites/commit-total", found["commit_total"], 2)
    eq("cites/commit-unresolvable", found["commit_unresolvable"], 1)
    eq(
        "cites/commit-unresolvable-detail",
        found["commit_unresolvable_detail"],
        ["corpus/README.md:6: 8c300ad"],
    )
    eq("cites/commit-nonhash", found["commit_nonhash"], 1)
    eq(
        "cites/commit-nonhash-detail",
        found["commit_nonhash_detail"],
        ["corpus/README.md:4: round-8"],
    )
    eq("cites/lookbehind/hook-marker", [d for d in found["commit_unresolvable_detail"] if "deadbee" in d], [])
    eq("cites/quoted-excluded", found["commit_quoted_excluded"], 1)
    eq(
        "cites/quoted-detail",
        found["commit_quoted_detail"],
        ["corpus/README.md:5: round-N (quoted meta-finding)"],
    )
    # a resolvable citation is not flagged
    eq("cites/resolvable-not-flagged", [d for d in found["commit_unresolvable_detail"] if "3b029b8" in d], [])

    # --- index fixture: coverage, stale, missing, EXCLUDED shapes --------
    idx = index_findings(FIXTURE_README, FIXTURE_TRACKED, lambda p: p in FIXTURE_ON_DISK)
    eq("index/patterns-harvested", idx["index_patterns"], 7)
    eq("index/unindexed", idx["unindexed"], 0)  # round-9-audit.md is covered by the glob row
    eq("index/stale", idx["stale_patterns"], 1)
    eq(
        "index/stale-detail",
        idx["stale_patterns_detail"],
        ["corpus/README.md:9: lessons/gone.md"],
    )
    eq("index/missing", idx["missing_paths"], 1)
    eq(
        "index/missing-detail",
        idx["missing_paths_detail"],
        ["corpus/README.md:10: ../nowhere/absent.py -> ../nowhere/absent.py"],
    )
    # EXCLUDED: the Basis-column token, the prose shapes, the quoted
    # meta-finding and the code literal must produce no finding at all.
    eq(
        "index/excluded/basis-token",
        [d for d in idx["missing_paths_detail"] if "absent-basis" in d],
        [],
    )
    eq(
        "index/excluded/prose-shape",
        [d for d in idx["missing_paths_detail"] + idx["stale_patterns_detail"]
         if "sibling" in d or "bailian-protocol" in d or "godspeed-core" in d
         or "wikillm" in d or "slice(0" in d],
        [],
    )
    eq(
        "index/excluded/glob-not-missing",
        [d for d in idx["missing_paths_detail"] if "*" in d],
        [],
    )
    eq("excluded-token/placeholder", is_excluded_token("round-<N>.md"), True)
    eq("excluded-token/ellipsis", is_excluded_token("../bailian-protocol/\u2026"), True)
    eq("excluded-token/home", is_excluded_token("~/wikillm"), True)
    # a glob IS a harvested pattern (it drives index coverage); it is never
    # tested for on-disk existence — see index/excluded/glob-not-missing above.
    eq("excluded-token/glob-harvested", is_excluded_token("knowledge/*.md"), False)
    eq("glob/detected", has_glob("knowledge/*.md"), True)
    eq("glob/absent", has_glob("lessons/round-3.md"), False)
    eq("excluded-token/plain-path", is_excluded_token("lessons/round-3.md"), False)
    eq("excluded-token/dotdot-path", is_excluded_token("../verifiers/baseline.json"), False)
    eq("corpus-internal/dotdot", is_corpus_internal("../verifiers/baseline.json"), False)
    eq("corpus-internal/relative", is_corpus_internal("lessons/round-3.md"), True)

    # --- check layer: verdicts, including the baseline-free zero mode ----
    clean = {key: 0 for _, key in CHECKS.values()}
    clean["tracked_files"] = 33
    clean["commit_total"] = 19
    base = {"checks": {cid: {"expect": 33 if key == "tracked_files" else 19 if key == "commit_total" else 0}
                       for cid, (_, key) in CHECKS.items()}}
    verdicts = {r["check"]: r["verdict"] for r in evaluate(clean, base)}
    eq("evaluate/all-agree", set(verdicts.values()), {"PASS"})
    eq("evaluate/no-baseline-equal", {r["check"]: r["verdict"] for r in evaluate(clean, None)}["corpus.index.tracked_files"], "OBSERVE")
    eq("evaluate/no-baseline-zero", {r["check"]: r["verdict"] for r in evaluate(clean, None)}["corpus.index.unindexed"], "PASS")
    dirty = dict(clean, report_dead=9)
    eq("evaluate/zero-drift", {r["check"]: r["verdict"] for r in evaluate(dirty, base)}["corpus.pointers.report_dead"], "DRIFT")
    eq("evaluate/zero-drift-baseline-free", {r["check"]: r["verdict"] for r in evaluate(dirty, None)}["corpus.pointers.report_dead"], "DRIFT")
    eq("evaluate/equal-drift", {r["check"]: r["verdict"] for r in evaluate(dict(clean, tracked_files=34), base)}["corpus.index.tracked_files"], "DRIFT")

    for failure in failures:
        print(f"FAIL {failure}")
    print(f"self-test: {len(failures)} failure(s) over {count} assertions")
    return 1 if failures else 0


# ---------------------------------------------------------------------------
# cli
# ---------------------------------------------------------------------------
def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--json", action="store_true", help="emit observations + results as JSON")
    ap.add_argument("--self-test", action="store_true", help="check the script's model only")
    ap.add_argument("--no-baseline", action="store_true", help="observe without comparing")
    ap.add_argument(
        "--baseline",
        type=Path,
        default=None,
        help=f"baseline file (default <repo>/verifiers/{BASELINE_NAME})",
    )
    ap.add_argument(
        "--repo",
        type=Path,
        default=DEFAULT_REPO,
        help="repo root to check (default: this script's grandparent directory)",
    )
    args = ap.parse_args(argv)

    if args.self_test:
        return self_test()

    repo = args.repo.resolve()
    baseline_path = (
        args.baseline.resolve() if args.baseline else repo / "verifiers" / BASELINE_NAME
    )

    try:
        obs = corpus_observations(repo)
    except Inconclusive as exc:
        print(f"INCONCLUSIVE: {exc}", file=sys.stderr)
        return 2
    except OSError as exc:
        print(f"INCONCLUSIVE: {type(exc).__name__}: {exc}", file=sys.stderr)
        return 2

    observed = {"corpus": {k: v for k, v in obs.items()}}
    flat = {k: obs[k] for k in EXTRACT_KEYS if k in obs}
    baseline = None
    if not args.no_baseline and baseline_path.is_file():
        baseline = json.loads(baseline_path.read_text())
    results = evaluate(flat, baseline)

    if args.json:
        print(json.dumps({"observed": observed, "results": results}, indent=2, ensure_ascii=False))

    drift = [r for r in results if r["verdict"] == "DRIFT"]

    if not args.json:
        print(
            f"{CORPUS_DIR}.index    tracked={obs['tracked_files']} "
            f"unindexed={obs['unindexed']} stale={obs['stale_patterns']} "
            f"missing={obs['missing_paths']}  "
            f"({obs['index_patterns']} FILE-column patterns over {obs['corpus_md_files']} md files)"
        )
        shapes = obs["report_pointer_shapes"]
        shape_txt = ", ".join(f"{k}={shapes[k]}" for k in ("relative", "absolute", "tilde", "bare"))
        print(
            f"{CORPUS_DIR}.pointers report_dead={obs['report_dead']}/{obs['report_total']} "
            f"commit_total={obs['commit_total']} unresolvable={obs['commit_unresolvable']} "
            f"nonhash={obs['commit_nonhash']} "
            f"(shapes [{shape_txt}], quoted-excluded={obs['commit_quoted_excluded']}, "
            f"pointer-excluded={obs['report_pointers_excluded']}; sites in --json)"
        )
        for key in DETAIL_KEYS:
            for line in obs.get(key, []):
                print(f"           {key[:-7]}: {line}")
        for row in results:
            if row["verdict"] != "PASS":
                print(f"{row['verdict']:7s} {row['check']}: observed={row['observed']} expected={row['expected']}")

    if baseline is None and not args.no_baseline:
        if not args.json:
            print(f"no baseline at {baseline_path} — observations above only (exit 3)")
        return 3

    if not args.json:
        print(
            f"{len(results) - len(drift)}/{len(results)} checks pass"
            + (f"; DRIFT: {', '.join(r['check'] for r in drift)}" if drift else "")
        )
    return 1 if drift else 0


if __name__ == "__main__":
    sys.exit(main())