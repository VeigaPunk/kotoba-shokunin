#!/usr/bin/env python3
"""append_rows.py — compose the Registry append block from per-page row files.

Each input file supplies exactly one 11-cell markdown table row (leading and trailing
pipe included) in the lane's SOURCES.md schema:

    | id | source | kind | tier | scope | anchor | teaches | status | opened | recheck | used-by |

Rows are ordered by the document URL found in their `source` cell (byte-ascending
ASCII/UTF-8), never by staged id or arithmetic, and receive sequential ids starting at
--start-id. The map is keyed by document: the URL is the evidence and the id follows it,
so renumbering one citation can never shift the next.

Usage:
  append_rows.py --start-id 223 rows/*.md
  append_rows.py --start-id 223 --rows-dir w1/build          # collects DIR/*/row.md
  append_rows.py --start-id 223 --map map.tsv rows/*.md
  append_rows.py --start-id 223 --rows-dir w1/build --allow-prose \
      --normalize-recheck --status mined --strip-log normalization-log.tsv

Strict defaults:
  * a file must hold exactly one non-empty line (seat drafts that wrap the row in prose
    need --allow-prose, which selects the single line parsing to exactly 11 cells);
  * a row opens and closes with `|`, carries no escaped pipe (`\\|`) and no cell pipe;
  * the id cell is `S<next>` or `S[0-9]{3,}` (it is replaced anyway);
  * kind/tier/status/recheck are checked against the census enums
    (sources-census.sh E05/E06/E07/E09) so a malformed cell never reaches the registry;
  * two rows may not share a document URL.

Only --normalize-recheck and --status rewrite a cell, and every rewrite is written to
--strip-log as `url<TAB>field<TAB>old<TAB>new` for the round lesson's Gate block.
"""

from __future__ import annotations

import argparse
import pathlib
import re
import sys

CELLS = 11
ID_RE = re.compile(r"^S(?:<next>|[0-9]{3,})$")
URL_RE = re.compile(r"https?://[^\s]+")
KINDS = {"spec", "docs", "paper", "code", "tool", "dataset", "talk", "book",
         "community", "own-work"}
TIERS = {"A", "B", "C"}
STATUSES = {"queued", "mined", "rejected"}
SYMBOLIC_RE = re.compile(r"^[A-Za-z][A-Za-z0-9 _-]*$")


class RowError(Exception):
    pass


def die(message: str) -> "NoReturn":  # noqa: F821
    print(f"append_rows: {message}", file=sys.stderr)
    raise SystemExit(2)


def parse_line(line: str) -> list[str]:
    raw = line.strip()
    if not raw.startswith("|") or not raw.endswith("|"):
        raise RowError("a registry row must start and end with '|'")
    if "\\|" in raw:
        raise RowError("escaped pipe '\\|' is forbidden in a registry row")
    cells = [cell.strip() for cell in raw[1:-1].split("|")]
    if len(cells) != CELLS:
        raise RowError(f"expected {CELLS} cells, got {len(cells)}")
    if any("|" in cell for cell in cells):
        raise RowError("a cell contains '|'")
    if any(not cell for cell in cells):
        raise RowError("an empty cell is not census-conformant")
    return cells


def read_row(path: pathlib.Path, allow_prose: bool) -> tuple[list[str], int]:
    lines = path.read_text(encoding="utf-8").splitlines()
    if not allow_prose:
        nonempty = [line for line in lines if line.strip()]
        if len(nonempty) != 1:
            raise RowError(
                f"expected exactly one non-empty line, got {len(nonempty)} "
                f"(use --allow-prose for a seat draft that wraps the row in prose)")
        return parse_line(nonempty[0]), 1
    candidates: list[tuple[int, list[str]]] = []
    for lineno, line in enumerate(lines, 1):
        try:
            candidates.append((lineno, parse_line(line)))
        except RowError:
            continue
    if not candidates:
        raise RowError("no line parses as an 11-cell registry row")
    if len(candidates) > 1:
        where = ", ".join(str(lineno) for lineno, _ in candidates)
        raise RowError(f"ambiguous: {len(candidates)} 11-cell rows at lines {where}")
    lineno, cells = candidates[0]
    return cells, lineno


def url_of(cells: list[str]) -> str:
    match = URL_RE.search(cells[1])
    if not match:
        raise RowError("source cell carries no http(s) URL")
    return match.group(0).rstrip(".,;")


def recheck_ok(value: str) -> bool:
    if re.match(r"^[0-9]{4}-[0-9]{2}-[0-9]{2}$", value):
        return True
    return bool(re.match(r"^[0-9]+d$", value) or SYMBOLIC_RE.match(value))


def check_cells(cells: list[str]) -> None:
    if not ID_RE.match(cells[0]):
        raise RowError(f"id cell {cells[0]!r} is not S<next> or S[0-9]{{3,}}")
    if cells[2] not in KINDS:
        raise RowError(f"kind {cells[2]!r} not in the census enum")
    if cells[3] not in TIERS:
        raise RowError(f"tier {cells[3]!r} not in the census enum")
    if cells[7] not in STATUSES:
        raise RowError(f"status {cells[7]!r} not in the census enum")
    if not re.match(r"^[0-9]{4}-[0-9]{2}-[0-9]{2}$", cells[8]):
        raise RowError(f"opened {cells[8]!r} is not an ISO date")
    if not recheck_ok(cells[9]):
        raise RowError(
            f"recheck {cells[9][:40]!r} is not an ISO date, NNd, or symbolic cadence "
            f"(use --normalize-recheck to strip trailing prose)")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("rows", nargs="*", type=pathlib.Path,
                        help="one file per document, each holding one 11-cell row")
    parser.add_argument("--rows-dir", type=pathlib.Path, action="append", default=[],
                        help="collect <dir>/*/row.md (repeatable)")
    parser.add_argument("--start-id", required=True, type=int,
                        help="first id number, e.g. 223 for S223")
    parser.add_argument("--map", type=pathlib.Path,
                        help="write 'url<TAB>old-id<TAB>new-id' for every row")
    parser.add_argument("--allow-prose", action="store_true",
                        help="select the single line parsing to 11 cells from a seat draft")
    parser.add_argument("--normalize-recheck", action="store_true",
                        help="rewrite an NNd recheck with trailing prose to NNd")
    parser.add_argument("--status", choices=sorted(STATUSES),
                        help="override the status cell (logged in --strip-log)")
    parser.add_argument("--strip-log", type=pathlib.Path,
                        help="write 'url<TAB>field<TAB>old<TAB>new' for every rewrite")
    args = parser.parse_args()

    if args.start_id < 1:
        die("--start-id must be >= 1")
    paths = list(args.rows)
    for directory in args.rows_dir:
        found = sorted(directory.glob("*/row.md"))
        if not found:
            die(f"{directory}: no */row.md files")
        paths.extend(found)
    if not paths:
        die("no row files given")

    documents: dict[str, tuple[pathlib.Path, list[str]]] = {}
    strip: list[str] = []
    for path in paths:
        try:
            cells, lineno = read_row(path, args.allow_prose)
            url = url_of(cells)
        except RowError as exc:
            die(f"{path}: {exc}")
        if url in documents:
            die(f"duplicate document URL {url} in {path} and {documents[url][0]}")
        if args.normalize_recheck and not recheck_ok(cells[9]):
            match = re.match(r"^([0-9]+d)\b", cells[9])
            if not match:
                die(f"{path}: recheck {cells[9][:40]!r} has no leading NNd cadence to keep")
            strip.append(f"{url}\trecheck\t{cells[9]}\t{match.group(1)}")
            cells[9] = match.group(1)
        if args.status and cells[7] != args.status:
            strip.append(f"{url}\tstatus\t{cells[7]}\t{args.status}")
            cells[7] = args.status
        try:
            check_cells(cells)
        except RowError as exc:
            die(f"{path}: {exc}")
        documents[url] = (path, cells)

    lines: list[str] = []
    mapping: list[str] = []
    for offset, url in enumerate(sorted(documents)):
        _, cells = documents[url]
        new_id = f"S{args.start_id + offset}"
        old_id = cells[0]
        cells[0] = new_id
        lines.append("| " + " | ".join(cells) + " |")
        mapping.append(f"{url}\t{old_id}\t{new_id}")

    print("\n".join(lines))
    if args.map:
        args.map.write_text("\n".join(mapping) + "\n", encoding="utf-8")
    if args.strip_log:
        args.strip_log.write_text("\n".join(strip) + ("\n" if strip else ""),
                                  encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
