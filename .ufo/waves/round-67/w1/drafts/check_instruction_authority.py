#!/usr/bin/env python3
"""Round-67 C2 instruction-authority admission counter.

Contract: read the entry, SOURCES registry, and coverage map as committed blobs
at one full-SHA --rev.  Count the single entry only when all seven frozen
conjuncts hold: the entry exists; its opening source lines cite an S### id;
every citation resolves to one mined registry row; every cited row's canonical
URL occurs as a complete URL token on that id's source line(s); the entry has
verified-at 2026-10-24 and a nonempty recheck line; every cited id has a
nonempty located quote of at most 25 whitespace-separated words occurring
verbatim in that row's anchor cell; and the entry is indexed in README's
Coverage map table.

Print exactly `authority ladder grounded N of 1`.  Exit 0 when N is 1, 1 when
N is 0, and 2 for usage, revision, git, or decoding failures.  --self-test uses
isolated in-memory fixtures (no network and no repository writes) and drives
public main() on a green fixture and one-conjunct-broken worlds.
"""
from __future__ import annotations

import argparse
import contextlib
import io
import re
import subprocess
import sys
from pathlib import Path

ENTRY = "corpus/knowledge/instruction-authority-ladder-round67.md"
SOURCES = "corpus/SOURCES.md"
README = "corpus/README.md"
COVERAGE_PATH = "knowledge/instruction-authority-ladder-round67.md"
VERIFIED_AT = "2026-10-24"
LANE_FALLBACK = Path("/home/vgpnk/Projects/shokunin/kotoba-shokunin")
REV_RE = re.compile(r"[0-9a-fA-F]{40}")
SID_RE = re.compile(r"(?<![A-Za-z0-9])S[0-9]{3,}(?![0-9])")
SID_FULL_RE = re.compile(r"S[0-9]{3,}")
URL_RE = re.compile(r"https?://[^\s<>\"'`|\\[\]{}]+")
QUOTE_RE = re.compile(r'"([^"\r\n]+)"|“([^”\r\n]+)”')
CONJUNCTS = (
    "01-entry-exists",
    "02-opening-source-ids",
    "03-citations-mined",
    "04-source-urls",
    "05-verified-and-recheck",
    "06-located-quotes",
    "07-coverage-index",
)


class EnvError(Exception):
    """The claim cannot be evaluated; this is not a red-content verdict."""


def lane_dir() -> Path:
    """Find the lane from verifiers/, a draft path, or the declared fallback."""
    here = Path(__file__).resolve().parent
    candidates = []
    if here.name == "verifiers":
        candidates.append(here.parent)
    for base in (here, here.parent):
        for candidate in (base, *base.parents):
            if ((candidate / "SKILL.md").is_file()
                    and (candidate / SOURCES).is_file()):
                candidates.append(candidate)
                break
    candidates.append(LANE_FALLBACK)
    for candidate in candidates:
        if (candidate / "SKILL.md").is_file() and (candidate / SOURCES).is_file():
            return candidate
    raise EnvError("lane repository not found near %s" % here)


def git(root: Path, args: list[str]) -> subprocess.CompletedProcess[bytes]:
    try:
        return subprocess.run(
            ["git", "-C", str(root), *args], capture_output=True, timeout=20,
            check=False,
        )
    except (OSError, subprocess.TimeoutExpired) as exc:
        raise EnvError("git %s failed: %s" % (" ".join(args), exc)) from exc


def _missing_blob(result: subprocess.CompletedProcess[bytes]) -> bool:
    detail = result.stderr.decode("utf-8", "replace")
    return ("does not exist" in detail or "exists on disk, but not in" in detail
            or "not in" in detail and "fatal: path" in detail)


def load_blobs(root: Path, rev: str) -> dict[str, str | None]:
    """Read only committed bytes; no working-tree path is consulted."""
    checked = git(root, ["rev-parse", "--verify", "--quiet", rev + "^{commit}"])
    if checked.returncode:
        detail = checked.stderr.decode("utf-8", "replace").strip()
        raise EnvError("revision %r is not a commit in %s%s"
                       % (rev, root, (": " + detail) if detail else ""))
    blobs: dict[str, str | None] = {}
    for path in (ENTRY, SOURCES, README):
        result = git(root, ["show", "%s:%s" % (rev, path)])
        if result.returncode:
            if _missing_blob(result):
                blobs[path] = None
                continue
            detail = result.stderr.decode("utf-8", "replace").strip()
            raise EnvError("git show %s:%s failed: %s" % (rev, path, detail))
        try:
            blobs[path] = result.stdout.decode("utf-8")
        except UnicodeDecodeError as exc:
            raise EnvError("%s at %s is not UTF-8: %s" % (path, rev, exc)) from exc
    return blobs


def table_cells(line: str) -> list[str]:
    stripped = line.strip()
    if len(stripped) < 2 or not stripped.startswith("|") or not stripped.endswith("|"):
        return []
    return [cell.strip() for cell in stripped[1:-1].split("|")]


def opening_source_lines(entry: str | None) -> list[str]:
    """The contiguous source: prefix at the first nonblank line."""
    if entry is None:
        return []
    lines = entry.splitlines()
    pos = 0
    while pos < len(lines) and not lines[pos].strip():
        pos += 1
    found = []
    while pos < len(lines) and lines[pos].startswith("source:"):
        found.append(lines[pos])
        pos += 1
    return found


def citations(lines: list[str]) -> dict[str, list[str]]:
    result: dict[str, list[str]] = {}
    for line in lines:
        for sid in SID_RE.findall(line):
            result.setdefault(sid, []).append(line)
    return result


def registry_rows(sources: str | None) -> dict[str, list[list[str]]]:
    """Parse only the 11-cell rows in SOURCES' Registry section."""
    rows: dict[str, list[list[str]]] = {}
    if sources is None:
        return rows
    in_registry = False
    for line in sources.splitlines():
        heading = re.match(r"^ {0,3}##[ \t]+(.*\S)[ \t]*$", line)
        if heading:
            in_registry = heading.group(1) == "Registry"
            continue
        if not in_registry:
            continue
        cells = table_cells(line)
        if len(cells) == 11 and SID_FULL_RE.fullmatch(cells[0]):
            rows.setdefault(cells[0], []).append(cells)
    return rows


def urls(text: str) -> list[str]:
    """URL tokens, with Markdown-adjacent punctuation removed at the right edge."""
    return [match.group(0).rstrip(".,;:!?)]}") for match in URL_RE.finditer(text)]


def unique_rows(
    cited: dict[str, list[str]], rows: dict[str, list[list[str]]]
) -> dict[str, list[str] | None]:
    """None marks an absent or ambiguous id, owned by conjunct three."""
    return {sid: (rows[sid][0] if len(rows.get(sid, [])) == 1 else None)
            for sid in cited}


def located_quotes(entry: str, sid: str, cited_ids: set[str]) -> list[str]:
    """Quotes in a paragraph/list line unambiguously associated with one id.

    A one-id paragraph binds all its quoted spans to that id.  In a multi-id
    paragraph only same-line associations count, preventing a quote for one
    source from being borrowed by another.  The opening source: lines therefore
    work as well as per-id quote records or table rows in the body.
    """
    del cited_ids  # all S ids, not only cited ones, participate in disambiguation
    found: list[str] = []
    for block in re.split(r"\n[ \t]*\n", entry):
        if sid not in SID_RE.findall(block):
            continue
        units = []
        if set(SID_RE.findall(block)) == {sid}:
            units.append(block)
        else:
            units.extend(line for line in block.splitlines()
                         if set(SID_RE.findall(line)) == {sid})
        for unit in units:
            for match in QUOTE_RE.finditer(unit):
                quote = match.group(1) if match.group(1) is not None else match.group(2)
                quote = quote.strip()
                if quote:
                    found.append(quote)
    return found


def coverage_indexed(readme: str | None) -> bool:
    if readme is None:
        return False
    in_coverage = False
    for line in readme.splitlines():
        heading = re.match(r"^ {0,3}##[ \t]+(.*\S)[ \t]*$", line)
        if heading:
            in_coverage = heading.group(1) == "Coverage map"
            continue
        if not in_coverage:
            continue
        cells = table_cells(line)
        if len(cells) >= 2 and COVERAGE_PATH in re.findall(r"`([^`]+)`", cells[1]):
            return True
    return False


def evaluate(blobs: dict[str, str | None]) -> dict[str, bool]:
    """Evaluate the seven frozen conjuncts with prerequisite attribution.

    Later checks are guarded when an earlier prerequisite owns the failure
    (for example, no citations means citation checks are vacuous).  This does
    not admit an invalid tree: the prerequisite remains red and N stays zero.
    It lets the self-test prove that every world breaks exactly one conjunct.
    """
    entry = blobs.get(ENTRY)
    source_lines = opening_source_lines(entry)
    cited = citations(source_lines)
    rows = registry_rows(blobs.get(SOURCES))
    resolved = unique_rows(cited, rows)
    ids = set(cited)

    checks: dict[str, bool] = {}
    checks["01-entry-exists"] = entry is not None
    checks["02-opening-source-ids"] = entry is None or bool(ids)
    checks["03-citations-mined"] = all(
        resolved[sid] is not None and resolved[sid][7] == "mined" for sid in ids
    )

    url_ok = True
    for sid in ids:
        row = resolved[sid]
        if row is None:
            continue
        canonical = urls(row[1])
        if not canonical or any(canonical[0] not in urls(line) for line in cited[sid]):
            url_ok = False
            break
    checks["04-source-urls"] = url_ok

    checks["05-verified-and-recheck"] = entry is None or bool(
        re.search(r"(?m)^verified-at:[ \t]*" + VERIFIED_AT + r"[ \t]*$", entry)
        and re.search(r"(?m)^recheck:[ \t]*\S.*$", entry)
    )

    quote_ok = True
    if entry is not None:
        for sid in ids:
            row = resolved[sid]
            if row is None:
                continue
            candidates = located_quotes(entry, sid, ids)
            if not any(1 <= len(quote.split()) <= 25 and quote in row[5]
                       for quote in candidates):
                quote_ok = False
                break
    checks["06-located-quotes"] = quote_ok
    checks["07-coverage-index"] = coverage_indexed(blobs.get(README))
    return checks


def score(blobs: dict[str, str | None]) -> tuple[int, dict[str, bool]]:
    checks = evaluate(blobs)
    return int(all(checks.values())), checks


def valid_fixture() -> dict[str, str | None]:
    q123 = "Instructions with higher authority override those with lower authority."
    q124 = ("The description field in SKILL.md frontmatter is the primary mechanism "
            "that determines whether Claude invokes a skill.")
    q129 = ("requiring models to navigate up to 12 levels of conflicting instructions "
            "with varying privileges")
    entry = "\n".join((
        "source: S123 — https://model-spec.openai.com/2026-08-18 — § Instructions and levels of authority",
        "source: S124 — https://github.com/anthropics/skills/blob/dbd4588f9e1033efb41dad4bef2f7947c8993d44/skills/skill-creator/SKILL.md — § Description Optimization",
        "source: S129 — https://arxiv.org/abs/2604.09443 — abstract",
        "verified-at: 2026-10-24",
        "recheck: python3 -B verifiers/check_instruction_authority.py --rev <rev>",
        "",
        "# Instruction authority ladder",
        "",
        "## Located quotes",
        "- S123 — § Instructions and levels of authority — \"%s\"" % q123,
        "- S124 — § Description Optimization — \"%s\"" % q124,
        "- S129 — abstract — \"%s\"" % q129,
        "",
    ))

    def row(sid: str, source: str, quote: str) -> str:
        return " | ".join((
            "", sid, source, "docs", "A", "scope",
            "location; quote \"%s\"" % quote, "teaches", "mined", "2026-10-24",
            "90d", ENTRY, "",
        ))

    sources = "\n".join((
        "# SOURCES",
        "## Registry",
        "| id | source | kind | tier | scope | anchor | teaches | status | opened | recheck | used-by |",
        "|---|---|---|---|---|---|---|---|---|---|---|",
        row("S123", "Model Spec — https://model-spec.openai.com/2026-08-18", q123),
        row("S124", "skill-creator — https://github.com/anthropics/skills/blob/dbd4588f9e1033efb41dad4bef2f7947c8993d44/skills/skill-creator/SKILL.md", q124),
        row("S129", "ManyIH — https://arxiv.org/abs/2604.09443", q129),
        "## Paths",
        "",
    ))
    readme = "\n".join((
        "# corpus",
        "## Coverage map",
        "| Area | File | Basis |",
        "|---|---|---|",
        "| Instruction authority | `%s` | S123, S124, S129 |" % COVERAGE_PATH,
        "## Frontier",
        "",
    ))
    return {ENTRY: entry, SOURCES: sources, README: readme}


def replace_once(text: str, old: str, new: str) -> str:
    if text.count(old) != 1:
        raise AssertionError("fixture replacement count for %r is %d" % (old, text.count(old)))
    return text.replace(old, new, 1)


def broken_fixtures() -> list[tuple[str, str, dict[str, str | None]]]:
    """Each world differs semantically in exactly one named conjunct."""
    worlds = []

    blobs = valid_fixture()
    del blobs[ENTRY]
    worlds.append(("entry absent", "01-entry-exists", blobs))

    blobs = valid_fixture()
    entry = blobs[ENTRY]
    prefix = "\n".join(entry.splitlines()[:3]) + "\n"
    blobs[ENTRY] = replace_once(entry, prefix, "source: no resolvable id\n")
    worlds.append(("no opening S id", "02-opening-source-ids", blobs))

    blobs = valid_fixture()
    blobs[ENTRY] = replace_once(blobs[ENTRY], "source: S129 —", "source: S999 —")
    worlds.append(("unresolved citation", "03-citations-mined", blobs))

    blobs = valid_fixture()
    lines = blobs[SOURCES].splitlines()
    for pos, line in enumerate(lines):
        if line.startswith("| S129 |"):
            cells = table_cells(line)
            cells[7] = "queued"
            lines[pos] = "| " + " | ".join(cells) + " |"
    blobs[SOURCES] = "\n".join(lines) + "\n"
    worlds.append(("citation not mined", "03-citations-mined", blobs))

    blobs = valid_fixture()
    blobs[ENTRY] = replace_once(
        blobs[ENTRY], "https://arxiv.org/abs/2604.09443 — abstract",
        "https://example.invalid/2604.09443 — abstract")
    worlds.append(("wrong source URL", "04-source-urls", blobs))

    blobs = valid_fixture()
    blobs[ENTRY] = replace_once(
        blobs[ENTRY], "https://model-spec.openai.com/2026-08-18 —",
        "https://model-spec.openai.com/2026-08-18.evil —")
    worlds.append(("URL is only a prefix", "04-source-urls", blobs))

    blobs = valid_fixture()
    blobs[ENTRY] = replace_once(blobs[ENTRY], "verified-at: 2026-10-24",
                                "verified-at: 2026-10-23")
    worlds.append(("wrong verified-at", "05-verified-and-recheck", blobs))

    blobs = valid_fixture()
    blobs[ENTRY] = replace_once(
        blobs[ENTRY], "recheck: python3 -B verifiers/check_instruction_authority.py --rev <rev>\n", "")
    worlds.append(("recheck absent", "05-verified-and-recheck", blobs))

    blobs = valid_fixture()
    old = "requiring models to navigate up to 12 levels of conflicting instructions with varying privileges"
    blobs[ENTRY] = replace_once(blobs[ENTRY], old, "a quote absent from this row's anchor")
    worlds.append(("quote not in anchor", "06-located-quotes", blobs))

    blobs = valid_fixture()
    overlong = "one two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen twenty twentyone twentytwo twentythree twentyfour twentyfive twentysix"
    q124 = ("The description field in SKILL.md frontmatter is the primary mechanism "
            "that determines whether Claude invokes a skill.")
    blobs[ENTRY] = replace_once(blobs[ENTRY], q124, overlong)
    blobs[SOURCES] = replace_once(blobs[SOURCES], q124, overlong)
    worlds.append(("26-word quote", "06-located-quotes", blobs))

    blobs = valid_fixture()
    q123 = "Instructions with higher authority override those with lower authority."
    blobs[ENTRY] = replace_once(blobs[ENTRY], '"%s"' % q123, '""')
    worlds.append(("empty quote", "06-located-quotes", blobs))

    blobs = valid_fixture()
    blobs[README] = replace_once(
        blobs[README], "| Instruction authority | `%s` | S123, S124, S129 |\n" % COVERAGE_PATH, "")
    worlds.append(("coverage row absent", "07-coverage-index", blobs))
    return worlds


def self_test() -> int:
    assertions = 0
    failures = 0
    rev = "a" * 40

    def check(label: str, actual, expected) -> None:
        nonlocal assertions, failures
        assertions += 1
        if actual != expected:
            failures += 1
            print("FAIL %s: got %r want %r" % (label, actual, expected))

    original_loader = load_blobs
    current = valid_fixture()

    def fixture_loader(root: Path, requested_rev: str) -> dict[str, str | None]:
        check("fixture loader receives --rev", requested_rev, rev)
        return dict(current)

    def run_main() -> tuple[int, str, str]:
        out, err = io.StringIO(), io.StringIO()
        with contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
            code = main(["--rev", rev, "--root", "/fixture"])
        return code, out.getvalue(), err.getvalue()

    try:
        globals()["load_blobs"] = fixture_loader
        for label, expected_failures, blobs in [
            ("satisfying", set(), valid_fixture()),
            *broken_fixtures(),
        ]:
            current = blobs
            n, checks = score(blobs)
            check(label + "/all seven registered", set(checks), set(CONJUNCTS))
            check(label + "/failed conjuncts",
                  {name for name, passed in checks.items() if not passed}, expected_failures)
            check(label + "/score", n, int(not expected_failures))
            code, out, err = run_main()
            check(label + "/public-main-exit", code, 0 if not expected_failures else 1)
            check(label + "/public-main-exact-line", out,
                  "authority ladder grounded %d of 1\n" % int(not expected_failures))
            check(label + "/public-main-stderr", err, "")

        out, err = io.StringIO(), io.StringIO()
        with contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
            code = main(["--rev", "not-a-full-sha", "--root", "/fixture"])
        check("invalid revision/exit", code, 2)
        check("invalid revision/no verdict", out.getvalue(), "")
        check("invalid revision/named", "40 hexadecimal" in err.getvalue(), True)

        def failing_loader(root: Path, requested_rev: str):
            raise EnvError("fixture git failure")

        globals()["load_blobs"] = failing_loader
        code, out, err = run_main()
        check("git failure/exit", code, 2)
        check("git failure/no verdict", out, "")
        check("git failure/named", "fixture git failure" in err, True)
    finally:
        globals()["load_blobs"] = original_loader

    print("self-test: %d failure(s) over %d assertions" % (failures, assertions))
    return 1 if failures else 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--rev", help="full 40-hex commit to measure")
    parser.add_argument("--root", type=Path, help=argparse.SUPPRESS)
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args(argv)
    if args.self_test:
        if args.rev or args.root:
            parser.error("--self-test cannot be combined with --rev or --root")
        return self_test()
    if not args.rev:
        parser.error("--rev is required")
    if not REV_RE.fullmatch(args.rev):
        print("could-not-evaluate: --rev must be a full 40 hexadecimal commit hash",
              file=sys.stderr)
        return 2
    try:
        root = args.root.resolve() if args.root else lane_dir()
        blobs = load_blobs(root, args.rev)
    except (EnvError, OSError) as exc:
        print("could-not-evaluate: %s" % exc, file=sys.stderr)
        return 2
    n, _ = score(blobs)
    print("authority ladder grounded %d of 1" % n)
    return 0 if n == 1 else 1


if __name__ == "__main__":
    sys.exit(main())
