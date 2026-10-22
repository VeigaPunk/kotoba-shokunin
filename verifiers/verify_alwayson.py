#!/usr/bin/env python3
"""verify_alwayson.py — machine check for two always-on rule-file boxes.

Contract: ``--check <box> --target <dir> --json`` emits a ``checks`` array
whose selected entry has ``id``, ``status`` (PASS, FAIL, or ERROR), and
``detail``. Exit 0 means PASS, 1 means FAIL, and 2 means usage or unreadable
input. ``--self-test`` exercises committed fixtures; ``--box-proof`` verifies
the map, live checklist text, and fixture suite for the delegated boxes.

alwayson.04 is a lane rule, not a vendor rule for always-on files: it extends
Anthropic's skills guidance "Avoid time-sensitive information" (SOURCES S019,
best-practices.md:574) to AGENTS.md/CLAUDE.md, where no authority opened in
round 53 states it (corpus/knowledge/alwayson-rule-files-round53.md point 5).
Known misses: month-year text such as "before August 2025", numeric
dates such as 11/01/2026, and quarter labels such as "Q4 2026".

The filename set is based on Claude Code's current memory documentation:
https://code.claude.com/docs/en/memory.md (sections "Choose where to put
CLAUDE.md files", "When Claude Code reads AGENTS.md", and "Share one file
with other coding tools"). For the target directory, this reads its
``AGENTS.md``, ``CLAUDE.md``, and ``CLAUDE.local.md``, plus
``.claude/AGENTS.md`` and ``.claude/CLAUDE.md``. These root and nested
candidate sets are checked for coexisting AGENTS.md and CLAUDE.md-class
sources; a redirect counts only between sibling files, so a cross-directory
pair fails. ``CLAUDE.local.md`` is scanned for dates and counts as a
CLAUDE-class file when AGENTS.md coexists, but it is not itself an accepted
redirect. A CLAUDE.md-class file redirects only when it is a symlink to its
sibling AGENTS.md or contains a line exactly ``@AGENTS.md``; imports inside
code spans or fenced code do not count.

This is a bounded lexical approximation, not a client loader. It scans the
whole selected files, including examples and code blocks, for ISO calendar
dates/timestamps, month-day strings, and a small set of date-free transient
cues (currently, temporarily, for now, at present, right now, until further
notice). It does not infer semantic transience from other wording or validate
calendar dates. It does not follow imports other than the exact redirect above,
or recurse beyond these fixed paths. It excludes nested repositories,
``.claude/rules/``, ``.agents/``, ``AGENTS.local.md``, ``AGENTS.override.md``,
``GEMINI.md``, other client-specific files, ancestor/global/managed
instruction files, settings, and client configuration. It follows only
in-target symlinks and never reads through a link that escapes the supplied
target. Selected rule files are limited to 1 MiB; no network access is used.
"""
from __future__ import annotations

import argparse
import contextlib
import io
import json
import os
import re
import stat
import sys
from dataclasses import dataclass
from pathlib import Path, PurePosixPath

CHECK_IDS = ("alwayson.04", "alwayson.07")
SECTION = "Always-on constraint-file checklist (AGENTS.md-class)"
DELEGATION_TARGET = "verifiers/verify_alwayson.py"
BASE_DIR = Path(__file__).resolve().parent.parent
VERIFIERS_DIR = Path(__file__).resolve().parent
FIXTURES_DIR = VERIFIERS_DIR / "fixtures" / "alwayson"
BASELINE_NAME = "checklist-baseline.json"
MAX_FILE_BYTES = 1024 * 1024
MAX_SYMLINK_HOPS = 40

PINNED_BOX_SHA = {
    "alwayson.04": "e88887bac96490db6b7cca27808aa3398d8cc6b89efbeb628c7e98ad9740668f",
    "alwayson.07": "ade1f60080c187688bb2ca5aae44986a4b0700db4b3cf452a225326482db2bb7",
}

# These names are the documentation-backed scope, not a filesystem glob.
CANDIDATE_PATHS = (
    "AGENTS.md",
    "CLAUDE.md",
    "CLAUDE.local.md",
    ".claude/AGENTS.md",
    ".claude/CLAUDE.md",
)
AGENT_NAMES = frozenset(("AGENTS.md",))
CLAUDE_CLASS_NAMES = frozenset(("CLAUDE.md", "CLAUDE.local.md"))

ISO_DATE_RE = re.compile(
    r"(?<!\d)\d{4}-(?:0[1-9]|1[0-2])-(?:0[1-9]|[12]\d|3[01])"
    r"(?:[Tt ](?:[01]\d|2[0-3]):[0-5]\d"
    r"(?::[0-5]\d(?:\.\d+)?)?(?:[Zz]|[+-](?:[01]\d|2[0-3]):?[0-5]\d)?"
    r")?(?!\d)"
)
MONTH_NAME = (
    r"Jan(?:uary)?|Feb(?:ruary)?|Mar(?:ch)?|Apr(?:il)?|May|Jun(?:e)?|"
    r"Jul(?:y)?|Aug(?:ust)?|Sep(?:t(?:ember)?)?|Oct(?:ober)?|"
    r"Nov(?:ember)?|Dec(?:ember)?"
)
MONTH_DAY_RE = re.compile(
    r"\b(?:" + MONTH_NAME + r")\.?\s+\d{1,2}(?:st|nd|rd|th)?"
    r"(?:,\s*\d{4})?\b|\b\d{1,2}(?:st|nd|rd|th)?\s+(?:"
    + MONTH_NAME + r")\.?(?:\s+\d{4})?\b",
    re.IGNORECASE,
)
TRANSIENT_RE = re.compile(
    r"\b(?:currently|temporarily|for\s+now|at\s+present|right\s+now|"
    r"until\s+further\s+notice)\b",
    re.IGNORECASE,
)
FENCE_LINE_RE = re.compile(r"^ {0,3}(`{3,}|~{3,})(.*)$")



class InputError(Exception):
    """A target, rule file, or fixture is missing, unsafe, or unreadable."""


@dataclass(frozen=True)
class Candidate:
    path: str
    resolved: tuple[str, ...]
    source_is_symlink: bool
    text: str


def _open_directory(root: Path, parts: tuple[str, ...]) -> int:
    flags = os.O_RDONLY | getattr(os, "O_DIRECTORY", 0) | getattr(os, "O_NOFOLLOW", 0)
    fd = os.open(root, flags)
    try:
        for part in parts:
            child = os.open(part, flags, dir_fd=fd)
            os.close(fd)
            fd = child
        return fd
    except Exception:
        os.close(fd)
        raise


def _resolve_candidate(root: Path, relative: str) -> tuple[tuple[str, ...], bool] | None:
    """Resolve one candidate using readlink/openat without following outside links."""
    original = PurePosixPath(relative).parts
    pending = [(part, index == len(original) - 1)
               for index, part in enumerate(original)]
    resolved: list[str] = []
    source_is_symlink = False
    hops = 0
    while pending:
        component, is_source_final = pending.pop(0)
        if component in ("", "."):
            continue
        if component == "..":
            if not resolved:
                raise InputError("symlink for %s escapes target directory" % relative)
            resolved.pop()
            continue
        try:
            parent_fd = _open_directory(root, tuple(resolved))
            try:
                info = os.stat(component, dir_fd=parent_fd, follow_symlinks=False)
                if stat.S_ISLNK(info.st_mode):
                    if is_source_final:
                        source_is_symlink = True
                    hops += 1
                    if hops > MAX_SYMLINK_HOPS:
                        raise InputError("too many symlink hops for %s" % relative)
                    target = os.readlink(component, dir_fd=parent_fd)
                else:
                    target = None
            finally:
                os.close(parent_fd)
        except FileNotFoundError:
            if source_is_symlink:
                raise InputError("dangling symlink in %s" % relative)
            return None
        except OSError as exc:
            raise InputError("cannot inspect %s (%s)" % (relative, exc)) from exc

        if target is not None:
            if os.path.isabs(target):
                normalized = os.path.normpath(target)
                root_name = os.path.normpath(str(root))
                try:
                    absolute_relative = Path(normalized).relative_to(root_name)
                except ValueError as exc:
                    raise InputError("symlink for %s escapes target directory" % relative) from exc
                resolved.clear()
                replacement = list(absolute_relative.parts)
            else:
                replacement = list(PurePosixPath(target).parts)
            pending = [(part, False) for part in replacement] + pending
            continue

        if pending:
            if not stat.S_ISDIR(info.st_mode):
                raise InputError("non-directory path component in %s" % relative)
            resolved.append(component)
        else:
            if not stat.S_ISREG(info.st_mode):
                raise InputError("%s is not a regular file" % relative)
            return tuple(resolved + [component]), source_is_symlink
    if source_is_symlink:
        raise InputError("symlink for %s does not resolve to a regular file" % relative)
    return None


def _read_resolved(root: Path, relative: str, resolved: tuple[str, ...]) -> str:
    if not hasattr(os, "O_NOFOLLOW") or not hasattr(os, "O_DIRECTORY"):
        raise InputError("safe no-follow file access is unavailable on this platform")
    if not resolved:
        raise InputError("empty resolved file path for %s" % relative)
    parent_fd = _open_directory(root, resolved[:-1])
    flags = os.O_RDONLY | os.O_NOFOLLOW
    try:
        fd = os.open(resolved[-1], flags, dir_fd=parent_fd)
    except OSError as exc:
        os.close(parent_fd)
        raise InputError("cannot open %s without following links (%s)" % (relative, exc)) from exc
    os.close(parent_fd)
    try:
        info = os.fstat(fd)
        if not stat.S_ISREG(info.st_mode):
            raise InputError("%s is not a regular file" % relative)
        if info.st_size > MAX_FILE_BYTES:
            raise InputError("%s exceeds the %d-byte limit" % (relative, MAX_FILE_BYTES))
        chunks: list[bytes] = []
        remaining = MAX_FILE_BYTES + 1
        while remaining:
            chunk = os.read(fd, min(65536, remaining))
            if not chunk:
                break
            chunks.append(chunk)
            remaining -= len(chunk)
        raw = b"".join(chunks)
        if len(raw) > MAX_FILE_BYTES:
            raise InputError("%s exceeds the %d-byte limit" % (relative, MAX_FILE_BYTES))
        try:
            return raw.decode("utf-8")
        except UnicodeDecodeError as exc:
            raise InputError("%s is not UTF-8 text" % relative) from exc
    except OSError as exc:
        raise InputError("cannot read %s (%s)" % (relative, exc)) from exc
    finally:
        os.close(fd)


def load_candidates(target: Path) -> tuple[Path, dict[str, Candidate]]:
    try:
        root = target.resolve(strict=True)
        if not root.is_dir():
            raise InputError("target is not a directory: %s" % target)
        if not hasattr(os, "O_NOFOLLOW") or not hasattr(os, "O_DIRECTORY"):
            raise InputError("safe no-follow file access is unavailable on this platform")
        root_fd = _open_directory(root, ())
        os.close(root_fd)
    except InputError:
        raise
    except (OSError, RuntimeError) as exc:
        raise InputError("cannot read target directory %s (%s)" % (target, exc)) from exc

    found: dict[str, Candidate] = {}
    for relative in CANDIDATE_PATHS:
        try:
            resolved = _resolve_candidate(root, relative)
            if resolved is None:
                continue
            path_parts, is_symlink = resolved
            text = _read_resolved(root, relative, path_parts)
        except InputError:
            raise
        except OSError as exc:
            raise InputError("cannot inspect %s (%s)" % (relative, exc)) from exc
        found[relative] = Candidate(relative, path_parts, is_symlink, text)
    return root, found


def _dated_hits(text: str) -> list[tuple[int, str, str]]:
    hits: list[tuple[int, str, str]] = []
    for line_number, line in enumerate(text.splitlines(), 1):
        for label, pattern in (("ISO date/timestamp", ISO_DATE_RE),
                               ("month-day date", MONTH_DAY_RE),
                               ("date-free transient cue", TRANSIENT_RE)):
            match = pattern.search(line)
            if match:
                hits.append((line_number, label, match.group(0)))
    return hits


def check_dated_text(found: dict[str, Candidate]) -> tuple[str, str]:
    if not found:
        return "FAIL", "no selected always-on rule files found"
    hits = []
    for relative in CANDIDATE_PATHS:
        candidate = found.get(relative)
        if candidate is None:
            continue
        for line_number, label, token in _dated_hits(candidate.text):
            hits.append("%s:%d %s %r" % (relative, line_number, label, token))
    if hits:
        return "FAIL", "dated/transient text found: " + "; ".join(hits[:8])
    return "PASS", "no recognized date or transient cue in %d selected files" % len(found)


def _has_import_line(text: str) -> bool:
    """Match the exact import line only outside Markdown code spans/fences."""
    fence_char: str | None = None
    fence_length = 0
    inline_ticks: int | None = None
    for line in text.splitlines():
        fence = FENCE_LINE_RE.match(line)
        if fence_char is not None:
            if fence:
                run, tail = fence.groups()
                if run[0] == fence_char and len(run) >= fence_length and not tail.strip():
                    fence_char = None
            continue
        if fence:
            run, _tail = fence.groups()
            fence_char, fence_length = run[0], len(run)
            continue
        if inline_ticks is None and line == "@AGENTS.md":
            return True
        index = 0
        while index < len(line):
            if line[index] != "`":
                index += 1
                continue
            end = index + 1
            while end < len(line) and line[end] == "`":
                end += 1
            run_length = end - index
            if inline_ticks is None:
                search = end
                closing = None
                while search < len(line):
                    tick = line.find("`", search)
                    if tick < 0:
                        break
                    tick_end = tick + 1
                    while tick_end < len(line) and line[tick_end] == "`":
                        tick_end += 1
                    if tick_end - tick == run_length:
                        closing = tick_end
                        break
                    search = tick_end
                if closing is None:
                    inline_ticks = run_length
                    break
                index = closing
            elif run_length == inline_ticks:
                inline_ticks = None
                index = end
            else:
                index = end
    return False


def _redirects_to(candidate: Candidate, agent: Candidate) -> bool:
    candidate_parent = PurePosixPath(candidate.path).parent
    agent_parent = PurePosixPath(agent.path).parent
    if candidate_parent != agent_parent or PurePosixPath(agent.path).name != "AGENTS.md":
        return False
    if candidate.source_is_symlink:
        return candidate.resolved == tuple(PurePosixPath(agent.path).parts)
    # CLAUDE.local.md is a CLAUDE-class companion, not one of the named
    # redirect forms. Only an actual CLAUDE.md can carry the import redirect.
    if PurePosixPath(candidate.path).name != "CLAUDE.md":
        return False
    return _has_import_line(candidate.text)


def check_canonical_names(found: dict[str, Candidate]) -> tuple[str, str]:
    if not found:
        return "FAIL", "no selected always-on rule files found"
    problems: list[str] = []
    agents = [found[path] for path in CANDIDATE_PATHS
              if path in found and PurePosixPath(path).name in AGENT_NAMES]
    claudes = [found[path] for path in CANDIDATE_PATHS
               if path in found and PurePosixPath(path).name in CLAUDE_CLASS_NAMES]
    # A bare AGENTS.md and one or more Claude-class files are independent rule
    # sources unless every pair points at the same sibling AGENTS.md.
    for agent in agents:
        for claude in claudes:
            if not _redirects_to(claude, agent):
                problems.append("%s and %s are not one explicit sibling redirect"
                                % (agent.path, claude.path))
    if problems:
        return "FAIL", "; ".join(problems[:8])
    return "PASS", "%d selected files; no independent AGENTS/CLAUDE pair" % len(found)


def evaluate(box: str, target: Path) -> dict:
    root, found = load_candidates(target)
    if box == "alwayson.04":
        status, detail = check_dated_text(found)
    elif box == "alwayson.07":
        status, detail = check_canonical_names(found)
    else:
        raise InputError("unsupported check %r" % box)
    return {"id": box, "status": status,
            "detail": "%s: %s" % (root, detail)}


def emit_json(checks: list[dict], exit_code: int, error: str | None = None) -> None:
    payload = {"checks": checks, "exit_code": exit_code}
    if error is not None:
        payload["error"] = error
    print(json.dumps(payload, indent=2, sort_keys=True))


# Case expectations are constants rather than manifest data: removing a
# committed case cannot remove its expected result or direction from the proof.
# (case id, box id, expected status, fixture directory, origin)
CASE_EXPECTATIONS = (
    ("plain-rules", "alwayson.04", "PASS", "a04-plain-rules", "counter"),
    ("version-number", "alwayson.04", "PASS", "a04-version-number", "counter"),
    ("iso-date", "alwayson.04", "FAIL", "a04-iso-date", "counter"),
    ("iso-timestamp", "alwayson.04", "FAIL", "a04-iso-timestamp", "counter"),
    ("month-day", "alwayson.04", "FAIL", "a04-month-day", "counter"),
    ("dated-claude-md", "alwayson.04", "FAIL", "a04-dated-claude-md", "counter"),
    ("fenced-date", "alwayson.04", "FAIL", "a04-fenced-date", "own"),
    ("dotted-version", "alwayson.04", "PASS", "a04-dotted-version", "own"),
    ("abbreviated-month-day", "alwayson.04", "FAIL", "a04-abbreviated-month-day", "own"),
    ("gemini-out-of-scope", "alwayson.04", "PASS", "a04-gemini-out-of-scope", "own"),
    ("size-control", "alwayson.04", "PASS", "a04-size-control", "own"),
    ("outside-link", "alwayson.04", "ERROR", "a04-outside-link/target", "own"),
    ("date-free-transient", "alwayson.04", "FAIL", "a04-date-free-transient", "own"),
    ("agents-only", "alwayson.07", "PASS", "a07-agents-only", "counter"),
    ("claude-only", "alwayson.07", "PASS", "a07-claude-only", "counter"),
    ("import-redirect", "alwayson.07", "PASS", "a07-import-redirect", "counter"),
    ("symlink-redirect", "alwayson.07", "PASS", "a07-symlink-redirect", "counter"),
    ("two-rule-files", "alwayson.07", "FAIL", "a07-two-rule-files", "counter"),
    ("prose-mention", "alwayson.07", "FAIL", "a07-prose-mention", "counter"),
    ("nested-claude-only", "alwayson.07", "PASS", "a07-nested-claude-only", "own"),
    ("nested-pair", "alwayson.07", "FAIL", "a07-nested-pair", "own"),
    ("gemini-not-canonical", "alwayson.07", "PASS", "a07-gemini-ignored", "own"),
    ("local-conflict", "alwayson.07", "FAIL", "a07-local-conflict", "own"),
    ("nested-claude-conflict", "alwayson.07", "FAIL", "a07-nested-claude-conflict", "own"),
    ("wrong-symlink-target", "alwayson.07", "FAIL", "a07-wrong-symlink-target", "own"),
    ("fenced-import-mention", "alwayson.07", "FAIL", "a07-fenced-import-mention", "own"),
    ("inline-import-mention", "alwayson.07", "FAIL", "a07-inline-import-mention", "own"),
    ("claude-local-companion", "alwayson.07", "PASS", "a07-claude-local-companion", "own"),
)


def _load_fixture_map(fixtures: Path) -> dict[str, str]:
    manifest_path = fixtures / "manifest.json"
    try:
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    except (OSError, ValueError) as exc:
        raise InputError("cannot read fixture manifest %s (%s)" % (manifest_path, exc)) from exc
    rows = manifest.get("cases") if isinstance(manifest, dict) else None
    if not isinstance(rows, list):
        raise InputError("fixture manifest cases must be a list")
    mapped: dict[str, str] = {}
    for row in rows:
        if not isinstance(row, dict) or not isinstance(row.get("id"), str) \
                or not isinstance(row.get("dir"), str):
            raise InputError("malformed fixture manifest case")
        if row["id"] in mapped:
            raise InputError("duplicate fixture case id %r" % row["id"])
        mapped[row["id"]] = row["dir"]
    return mapped


def _fixture_suite(fixtures: Path) -> tuple[list[str], int]:
    failures: list[str] = []
    total = 0

    def rec(label: str, ok: bool, got: object) -> None:
        nonlocal total
        total += 1
        if not ok:
            failures.append("%s: got %r" % (label, got))

    try:
        mapping = _load_fixture_map(fixtures)
    except InputError as exc:
        rec("fixture manifest readable", False, str(exc))
        return failures, total

    required = {case[0] for case in CASE_EXPECTATIONS}
    rec("manifest ids are unique and match the pinned corpus",
        set(mapping) == required, sorted(set(mapping) ^ required))
    rec("frozen counter case shapes are all committed",
        {case[0] for case in CASE_EXPECTATIONS if case[4] == "counter"} <= set(mapping),
        sorted({case[0] for case in CASE_EXPECTATIONS if case[4] == "counter"} - set(mapping)))
    directional = all(
        {case[2] for case in CASE_EXPECTATIONS if case[1] == box} >= {"PASS", "FAIL"}
        for box in CHECK_IDS
    )
    rec("both verdict directions are pinned for both boxes", directional,
        {box: sorted({case[2] for case in CASE_EXPECTATIONS if case[1] == box})
         for box in CHECK_IDS})
    own_count = sum(1 for case in CASE_EXPECTATIONS if case[4] == "own")
    rec("at least four unpinned cases are committed", own_count >= 4, own_count)

    for case_id, box, expected, fixture_rel, _origin in CASE_EXPECTATIONS:
        declared = mapping.get(case_id)
        rec("%s fixture path is pinned" % case_id, declared == fixture_rel, declared)
        target = fixtures / fixture_rel
        try:
            target_resolved = target.resolve(strict=True)
            target_resolved.relative_to(fixtures.resolve(strict=True))
            if not target_resolved.is_dir():
                raise InputError("fixture target is not a directory")
            result = evaluate(box, target_resolved)
            status = result["status"]
            code = 0 if status == "PASS" else 1
            if status == "ERROR":
                code = 2
        except (InputError, OSError, RuntimeError, ValueError) as exc:
            status, code = "ERROR", 2
            result = {"id": box, "status": status, "detail": str(exc)}
        rec("%s direct result" % case_id, status == expected, result)

        argv = ["--check", box, "--target", str(target), "--json"]
        out = io.StringIO()
        err = io.StringIO()
        try:
            with contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
                cli_code = main(argv)
            payload = json.loads(out.getvalue())
            entry = next(item for item in payload["checks"] if item.get("id") == box)
            contract_ok = (cli_code == code and payload.get("exit_code") == code
                           and entry.get("status") == expected
                           and isinstance(entry.get("detail"), str))
        except (SystemExit, OSError, ValueError, KeyError, StopIteration, TypeError) as exc:
            cli_code, contract_ok = 99, False
            payload = {"error": str(exc), "stdout": out.getvalue(),
                       "stderr": err.getvalue()}
        rec("%s JSON and exit contract" % case_id, contract_ok,
            {"exit": cli_code, "payload": payload})

    # Reduce the bound only for a committed short fixture, proving the reader
    # rejects an over-limit file before unbounded allocation without storing a
    # megabyte fixture in the repository.
    global MAX_FILE_BYTES
    old_limit = MAX_FILE_BYTES
    try:
        MAX_FILE_BYTES = 8
        try:
            evaluate("alwayson.04", fixtures / "a04-size-control")
            size_ok = False
            size_detail = "over-limit fixture was accepted"
        except InputError as exc:
            size_ok = "limit" in str(exc)
            size_detail = str(exc)
    finally:
        MAX_FILE_BYTES = old_limit
    rec("bounded file reader rejects the over-limit fixture", size_ok, size_detail)
    return failures, total


def self_test() -> int:
    failures, total = _fixture_suite(FIXTURES_DIR)
    for failure in failures:
        print("self-test FAIL: %s" % failure)
    print("%d failure(s) over %d assertions" % (len(failures), total))
    return 1 if failures else 0


def box_proof(map_path: Path, fixtures: Path) -> int:
    problems: list[str] = []
    try:
        box_map = json.loads(map_path.read_text(encoding="utf-8"))
    except (OSError, ValueError) as exc:
        print("boxes proven 0")
        print("box-proof: cannot read box map %s (%s)" % (map_path, exc), file=sys.stderr)
        return 2
    entries: dict[str, dict] = {}
    for entry in box_map.get("boxes", []) if isinstance(box_map, dict) else []:
        if isinstance(entry, dict) and isinstance(entry.get("box_id"), str):
            if entry["box_id"] in entries:
                problems.append("duplicate map entry for %s" % entry["box_id"])
            entries[entry["box_id"]] = entry

    skill_path = map_path.parent.parent / "SKILL.md"
    try:
        skill_text = skill_path.read_text(encoding="utf-8")
        sys.path.insert(0, str(VERIFIERS_DIR))
        import verify_skill_checklist as checklist_gate
        live_boxes, _ = checklist_gate.extract_boxes(skill_text.splitlines())
    except (OSError, UnicodeError, ImportError, AttributeError) as exc:
        print("boxes proven 0")
        print("box-proof: cannot read live checklist or its extractor (%s)" % exc,
              file=sys.stderr)
        return 2

    for box in CHECK_IDS:
        entry = entries.get(box)
        if entry is None:
            problems.append("%s: no map entry" % box)
            continue
        if entry.get("section") != SECTION:
            problems.append("%s: section is not the pinned always-on section" % box)
        if entry.get("disposition") != "delegated:" + DELEGATION_TARGET:
            problems.append("%s: not delegated to %s" % (box, DELEGATION_TARGET))
        pinned = PINNED_BOX_SHA[box]
        if entry.get("text_sha256") != pinned:
            problems.append("%s: map text hash %r != pinned %r"
                            % (box, entry.get("text_sha256"), pinned))
        live_matches = [item for item in live_boxes
                        if item.get("section") == SECTION
                        and item.get("sha256") == pinned]
        if len(live_matches) != 1:
            problems.append("%s: live checklist has %d boxes with its pinned hash"
                            % (box, len(live_matches)))

    failures, total = _fixture_suite(fixtures)
    if failures:
        problems.append("fixture proof failed (%d failures over %d assertions)"
                        % (len(failures), total))
        problems.extend("fixture: " + failure for failure in failures[:8])
    proven = 0 if problems else len(CHECK_IDS)
    print("boxes proven %d" % proven)
    for problem in problems:
        print("box-proof: %s" % problem, file=sys.stderr)
    return 0 if proven == len(CHECK_IDS) else 1


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--self-test", action="store_true",
                      help="exercise committed fixtures only")
    mode.add_argument("--box-proof", action="store_true",
                      help="prove delegated map entries, checklist hashes, and fixtures")
    parser.add_argument("--check", choices=CHECK_IDS,
                        help="box to check")
    parser.add_argument("--target", metavar="DIR",
                        help="directory containing always-on rule files")
    parser.add_argument("--map", metavar="PATH", default=None,
                        help="box-map JSON for --box-proof")
    parser.add_argument("--fixtures", metavar="DIR", default=None,
                        help="fixture directory for --box-proof")
    parser.add_argument("--json", action="store_true",
                        help="machine-readable output")
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    if args.self_test:
        if args.check or args.target or args.map or args.fixtures:
            parser.error("--self-test does not accept --check, --target, --map, or --fixtures")
        return self_test()
    if args.box_proof:
        if args.check or args.target:
            parser.error("--box-proof does not accept --check or --target")
        map_path = Path(args.map) if args.map else BASE_DIR / "verifiers" / BASELINE_NAME
        fixtures = Path(args.fixtures) if args.fixtures else FIXTURES_DIR
        return box_proof(map_path, fixtures)
    if args.map or args.fixtures:
        parser.error("--map and --fixtures require --box-proof")
    if not args.check or not args.target:
        parser.error("--check and --target are required")
    try:
        result = evaluate(args.check, Path(args.target))
        code = 0 if result["status"] == "PASS" else 1
    except InputError as exc:
        result = {"id": args.check, "status": "ERROR", "detail": str(exc)}
        code = 2
    if args.json:
        emit_json([result], code)
    else:
        print("%s %s: %s" % (result["status"], result["id"], result["detail"]))
    return code


if __name__ == "__main__":
    sys.exit(main())
