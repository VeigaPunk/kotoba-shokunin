#!/usr/bin/env python3
r"""check_omp_root_semantics_v2.py -- frozen counter for the round-88 C1 (depth) claim.

Frozen predicate (the same sentence in plans/round-88.md § C1, here, and in every receipt):

    python3 -B verifiers/check_omp_root_semantics_v2.py --rev <rev>
        -> prints "omp root semantics grounded N of 12" and "forgeries rejected M of 4",
           exit 0 iff N == 12 AND M == 4 AND guards S1-S5 PASS; exit 1 otherwise;
           exit 2 = could-not-evaluate.

Executed per plans/round-88-addendum-1.md (A1.1-A1.6, erratum A1.8) and the pre-score
ruling plans/round-88-addendum-2.md (A2.1, A2.2).  The addenda change no predicate
sentence, no target (N == 12, M == 4), no denominator and no kill rule; they fix how the
frozen conjuncts are executed.  A fifth output line `forgery-class worlds rejected K of 7`
discloses the three addendum K classes; the exit rule stays on N and M only (A1.6).

A row is GROUNDED iff all five conjuncts hold:

  1 pattern  (A1.1) `root_pattern` equals the row's pattern in the round-86 ledger at the
             FROZEN PIN 223ae62424f8ab1eb365d733eb648d6228ddd7e8 (git show <pin>:…, never
             `<rev>`) AND is a member of the frozen PATTERN_SET tuple below (sha256
             printed).  No `..` segment, no wildcard in the first segment (round-88 § C1),
             and (A1.3) no absolute `/…` or `~user` pattern.
  2 reader   `reader_quote` (>= 12 chars) re-finds byte-exactly at its frozen per-row offset
             (A1.5, `reader_offset` column of ScoutElfMap/ELF_MAP.tsv at sha256
             21e3c518df2eafc17a233ad4232b7b0a852db47f9a9be522acf32ab938444897, cited per
             A1.8); the pinned line carries a path-join token; and the row's frozen
             SINGLE-TOKEN binding set (A1.4) binds, under A2.1: the token (exact byte
             string, quotes included) re-finds byte-exactly at its frozen measured start
             offset, that offset lies inside the row's chunk
             [module_offset, next `// packages/` header), the reader pin check already
             passed (a token cannot rescue a wrong quote), the token's total and in-chunk
             occurrence counts are printed on the row's receipt line (zero in-chunk fails;
             out-of-chunk occurrences are disclosed, not ignored), the token is absent from
             every other row's reader-quote line, is not a substring of the row's
             `binary_quote` line, is not in GENERIC_TOKENS, and within a shared-quote
             same-prefix group the sets differ (A1.4 cond 6; rows 3/4, 6/7, 10/11).
  3 module   (A1.2) the NEAREST preceding `// packages/<module>` header at the reader pin
             names exactly the row's module, and the pin lies before the next header.
  4 bound    LIVE: the counter models the walk-up loop from the ELF bytes.  For the walker
             module the frozen loop quotes (name array `var y1 = [".agent", ".agents"];`,
             push-skip `if (R !== u.home) {`, stop `if (R === (u.repoRoot ?? u.home))`)
             must sit inside one agents.ts chunk; walker rows expand over exactly the
             directories that grounded loop visits for the frozen probe (cwd
             /home/u/proj/sub, HOME /home/u, repoRoot unset: /home/u/proj/sub and
             /home/u/proj -- strictly below $HOME).  Non-walking rows expand over their
             single join base.  Any candidate that escapes its walk set or carries a `..`
             segment is refused; a `~/` row produces only $HOME-rooted candidates; nothing
             expands to $HOME itself or above (A1.3 containment for every row).
  5 binary   the row's `binary_quote` occurs verbatim in the ELF.

Guards: S1 the ledgers (and the pin-anchored round-86 ledger) are read from committed
bytes via `git show`; S2 the ELF sha256 equals OMP_SHA256 (else exit 2); S3 the semantics
ledger's pattern column equals BOTH the pin-anchored round-86 patterns AND PATTERN_SET;
S4 `--self-test` prints `0 failure(s) over N assertions` with N >= the frozen floor
(verifiers/floors-registry.json, key omp_root_semantics_v2; read at <rev> when present
there, else worktree -- the source is printed); S5 the ELF is opened read-only
(mmap ACCESS_READ), never exec'd, and no network module is imported.

Forged worlds (M == 4): the r87 critic's four classes `w_cross_row7`, `w_subdir_row9`,
`w_misattr_row12`, `w_renderline_row6`, re-created in memory as the honest <rev> ledger
with the exact reader-cell mutations committed in round 87's CriticSemanticsR87/
forgery-ledger-diffs.txt (cumulative).  K classes (A1.6, disclosed): `w_both_ledgers`
(C1-S1, one commit rewriting both ledgers), `w_module_mislabel` (C1-S2), `w_home_escape`
(C1-S4, patterns `/etc/skills`, `/tmp/x/skills`, `~root/skills`).  Each is scored in
memory; rejected iff its score is below 12 with the mutated rows among the failures.

Disclosed bound (A1.6/A2.1, carried to the report): the counter's frozen pins are a table,
and a table can be tuned -- C1-S5's lookup-oracle bound is NOT closed by this counter.
C1's evidence rests on two legs: these frozen pins AND ReviewerC1's independent
reimplementation (.ufo/waves/round-88/w1/ReviewerC1/independent_c1.py), which shares no
table with this file.

Upstream cross-check (pre-score, per round-88 § C1 conjunct 4): WALKER_BOUND_UPSTREAM
records the upstream file the walker bound was checked against.

`--self-test` scores synthetic in-memory worlds (no git fixture, no file writes, runs
anywhere): the must-pass honest arm; the four M arms; the three K arms as must-fail; one
arm per conjunct failure (pattern `..`, pattern wildcard, absolute pattern, `~user`
pattern, doc-quote reader, quote-miss reader, shifted-token-pin, wrong-chunk-token,
missing module header, header-after-reader order, missing binary quote, empty/generic
binding refusal); the walking-into-HOME and repoRoot arms; the guard arms; and the frozen
configuration's own sha256/hygiene assertions.

Usage: check_omp_root_semantics_v2.py --rev REV [--repo DIR] [--work DIR]
       check_omp_root_semantics_v2.py --self-test [--work DIR]
Exit 0 pass (12 of 12, forgeries 4 of 4, S1-S5 PASS), 1 content fail, 2 could-not-evaluate.

Frozen tables recorded in this header (A1.6; each digest is the sha256 of the constant's
exact text, verified by --self-test's config/ arms):
  twelve binding token sets (A1.4, single-token each) sha256
    98ed070b56188c602302cc0bc97afef0a1c4a750fb894138e7e587f59e53cb0a
  token byte-start pins (A2.1 cond 1) sha256
    2f7207729aa622f2dd18a3ea33ae6636316267e782171052eb61e129457a91a0
  reader pins (A1.5; ELF_MAP.tsv @ 21e3c518...4897) sha256
    fa0e8cc32720b6abdfc6e71575a1c237ddd5eeeaa45d8576be7f8ecc41fe4572
  module chunk offsets (A2.1 cond 2) sha256
    c96cda89e3119fc9f6adaed51df32aaa2e8e8057de1d17b3e823a57e9b68ad44
  PATTERN_SET (A1.1b) sha256
    f6aa379f03e8c2a7a99b88863c5a3901f9091dfe8cfcd3d9a0cffc605460611f
Disclosed: the binding tokens `eh`, `".codex"`, `".github"`, `we()`, `R.path` also occur
outside their module chunk (A2.1 cond 4); receipts print total and in-chunk counts per row.
"""
from __future__ import annotations

import argparse
import bisect
import fnmatch
import hashlib
import json
import mmap
import posixpath
import re
import subprocess
import sys
from pathlib import Path
from typing import Iterable

HERE = Path(__file__).resolve().parent
REPO = HERE.parent

SEMANTICS_LEDGER = "verifiers/omp-skill-roots-semantics.tsv"
ROOTS_LEDGER = "verifiers/omp-skill-roots.tsv"
FLOORS_REGISTRY = "verifiers/floors-registry.json"
SEMANTICS_HEADER = "root_pattern\tbinary_quote\tmodule\treader_quote"
ROOTS_HEADER = "root_pattern\tbinary_quote"
INSTRUMENT_KEY = "omp_root_semantics_v2"

TOTAL = 12                      # frozen denominator (round-86 ledger; plans/round-88.md § C1)
FORGED_TOTAL = 4                # the four r87 forged worlds (M)
K_TOTAL = 7                     # M's four classes + the three disclosed K classes
QUOTE_MIN = 12
JOIN_TOKENS = ("join(", ".join(", "resolve(", "path.join")
WILD = set("*?[")
LINE_SPAN = 8192                # bounded window for the enclosing ELF line

OMP_BINARY = Path("/home/vgpnk/.local/bin/omp")
OMP_SHA256 = "6737ee2415555a3656cc7b89c14d1c25c18658ee4c0fd4f7309705149ccb7b0f"

# A1.1: the round-86 ledger anchor is a frozen revision, never `<rev>` (closes C1-S1).
PATTERN_PIN_REV = "223ae62424f8ab1eb365d733eb648d6228ddd7e8"

# A1.5/A1.8: the ELF_MAP table the reader pins were read from (final bytes, not the
# scout's mid-flight print).
ELF_MAP_SHA256 = "21e3c518df2eafc17a233ad4232b7b0a852db47f9a9be522acf32ab938444897"

# Conjunct 4's upstream cross-check, completed pre-score from ScoutUpstream's receipts
# (SOURCE_READY 976360027cee582030f2ec4871544821d8b66c25e8687ea461f4bee56aacb92e):
# raw.githubusercontent.com/can1357/oh-my-pi/v18.15.0
#   packages/coding-agent/src/discovery/agents.ts, sha256 976360027cee582030f2ec4871544
#   821d8b66c25e8687ea461f4bee56aacb92e, git blob 2e41428ba19a5fe875143b422b7f4eccbe44c24d;
# lines 140-155 carry the same loop (skip push at ctx.home, stop at
# `if (current === (ctx.repoRoot ?? ctx.home)) break;` -- upstream line 149).
WALKER_BOUND_UPSTREAM = ("checked 976360027cee582030f2ec4871544821d8b66c25e8687ea461f4bee56a"
                         "acb92e agents.ts@v18.15.0 line 149 stop repoRoot??home")

# --------------------------------------------------------------------------- frozen probe

FROZEN_CWD = "/home/u/proj/sub"
FROZEN_HOME = "/home/u"

# ------------------------------------------------------- frozen per-row tables (A1.4/A1.5)
#
# All four tables are frozen before the first honest or forged score (kill rule:
# plans/round-88.md § C1).  Sources: the addendum's binding-token table (A1.4, rows 3/4/6/7
# located by ScoutElfMap and the L1's probes), the ELF_MAP.tsv columns at ELF_MAP_SHA256
# (reader_offset A1.5, module_offset A2.1 cond 2), and ExecLiveBound's byte-exact token
# start measurements (A2.1 cond 1: 173819995, 173840380, 173864236, 173864246, 173879117,
# 172784806, 172785190, 173820148, 173914949, 173809956 -- all re-found byte-exactly).
# The A1.4 table's "located at" column stays a prose statement anchor; these pins replace it.


def parse_kv_block(block: str) -> dict[str, str]:
    parsed: dict[str, str] = {}
    for line in block.splitlines():
        line = line.strip()
        if not line or line.startswith("#") or " -> " not in line:
            continue
        key, value = line.split(" -> ", 1)
        parsed[key] = value
    return parsed


BINDING_BLOCK = """\
# pattern -> binding token (A1.4 single-token set, exact byte string; A2.1 ruling)
{cwd}/.omp/skills -> Ou.projectDir
{cwd}/.claude/skills -> eh
{cwd}/.agent/skills -> ".agent"
{cwd}/.agents/skills -> ".agents"
{cwd}/.codex/skills -> ".codex"
{cwd}/.opencode/skills -> ".opencode"
{cwd}/.github/skills -> ".github"
~/.omp/agent/skills -> we()
~/.omp/plugins/node_modules/*/skills -> R.path
~/.agent/skills -> ".agent"
~/.agents/skills -> ".agents"
~/.omp/agent/managed-skills -> "managed-skills"
"""
BINDING = parse_kv_block(BINDING_BLOCK)
BINDING_SETS: dict[str, tuple[str, ...]] = {k: (v,) for k, v in BINDING.items()}
BINDING_BLOCK_SHA256 = "98ed070b56188c602302cc0bc97afef0a1c4a750fb894138e7e587f59e53cb0a"

TOKEN_PIN_BLOCK = """\
# pattern -> binding token pin (exact measured byte start; byte-exact re-find; A2.1 cond 1)
{cwd}/.omp/skills -> 173819995
{cwd}/.claude/skills -> 173840380
{cwd}/.agent/skills -> 173864236
{cwd}/.agents/skills -> 173864246
{cwd}/.codex/skills -> 173879117
{cwd}/.opencode/skills -> 172784806
{cwd}/.github/skills -> 172785190
~/.omp/agent/skills -> 173820148
~/.omp/plugins/node_modules/*/skills -> 173914949
~/.agent/skills -> 173864236
~/.agents/skills -> 173864246
~/.omp/agent/managed-skills -> 173809956
"""
TOKEN_PINS = {k: int(v) for k, v in parse_kv_block(TOKEN_PIN_BLOCK).items()}
TOKEN_PIN_BLOCK_SHA256 = "2f7207729aa622f2dd18a3ea33ae6636316267e782171052eb61e129457a91a0"

READER_OFFSET_BLOCK = """\
# pattern -> reader pin (A1.5; ELF_MAP.tsv reader_offset @ ELF_MAP_SHA256; A1.8 digest)
{cwd}/.omp/skills -> 173819979
{cwd}/.claude/skills -> 173840364
{cwd}/.agent/skills -> 173865724
{cwd}/.agents/skills -> 173865724
{cwd}/.codex/skills -> 173879095
{cwd}/.opencode/skills -> 172785704
{cwd}/.github/skills -> 172785704
~/.omp/agent/skills -> 173820135
~/.omp/plugins/node_modules/*/skills -> 173914936
~/.agent/skills -> 173865523
~/.agents/skills -> 173865523
~/.omp/agent/managed-skills -> 173809938
"""
READER_OFFSETS = {k: int(v) for k, v in parse_kv_block(READER_OFFSET_BLOCK).items()}
READER_OFFSET_BLOCK_SHA256 = "fa0e8cc32720b6abdfc6e71575a1c237ddd5eeeaa45d8576be7f8ecc41fe4572"

MODULE_OFFSET_BLOCK = """\
# pattern -> module chunk start (ELF_MAP.tsv module_offset; A2.1 cond 2 interval start)
{cwd}/.omp/skills -> 173814223
{cwd}/.claude/skills -> 173837493
{cwd}/.agent/skills -> 173864077
{cwd}/.agents/skills -> 173864077
{cwd}/.codex/skills -> 173878972
{cwd}/.opencode/skills -> 172784226
{cwd}/.github/skills -> 172784226
~/.omp/agent/skills -> 173814223
~/.omp/plugins/node_modules/*/skills -> 173914407
~/.agent/skills -> 173864077
~/.agents/skills -> 173864077
~/.omp/agent/managed-skills -> 173809642
"""
MODULE_OFFSETS = {k: int(v) for k, v in parse_kv_block(MODULE_OFFSET_BLOCK).items()}
MODULE_OFFSET_BLOCK_SHA256 = "c96cda89e3119fc9f6adaed51df32aaa2e8e8057de1d17b3e823a57e9b68ad44"

PATTERN_SET_BLOCK = """\
# A1.1(b): the frozen round-86 pattern set (member check; sha256 printed in receipts)
{cwd}/.omp/skills
{cwd}/.claude/skills
{cwd}/.agent/skills
{cwd}/.agents/skills
{cwd}/.codex/skills
{cwd}/.opencode/skills
{cwd}/.github/skills
~/.omp/agent/skills
~/.omp/plugins/node_modules/*/skills
~/.agent/skills
~/.agents/skills
~/.omp/agent/managed-skills
"""
PATTERN_SET: tuple[str, ...] = tuple(
    line.strip() for line in PATTERN_SET_BLOCK.splitlines()
    if line.strip() and not line.strip().startswith("#"))
PATTERN_SET_SHA256 = "f6aa379f03e8c2a7a99b88863c5a3901f9091dfe8cfcd3d9a0cffc605460611f"

# A1.4 cond 5: tokens that may never bind a row (exact membership).
GENERIC_TOKENS = {"cwd", "join", "skills", "path", "dir", "home", "projectDir", "userAgent",
                  "userBase", "node_modules", "n", "p", "u", "k", "e", "t", "R", "x", "_"}

# A1.4 cond 6: rows sharing one reader quote and one prefix class must differ.
SHARED_QUOTE_GROUPS: tuple[tuple[str, str], ...] = (
    ("{cwd}/.agent/skills", "{cwd}/.agents/skills"),
    ("{cwd}/.opencode/skills", "{cwd}/.github/skills"),
    ("~/.agent/skills", "~/.agents/skills"),
)

# ------------------------------------------------------------------------- walker bound

WALKER_MODULE = "coding-agent/src/discovery/agents.ts"
WALKER_NAMES_QUOTE = 'var y1 = [".agent", ".agents"];'
WALKER_SKIP_QUOTE = "if (R !== u.home) {"
WALKER_STOP_QUOTE = "if (R === (u.repoRoot ?? u.home))"
WALKER_QUOTES = (WALKER_NAMES_QUOTE, WALKER_SKIP_QUOTE, WALKER_STOP_QUOTE)

WALK_SHAPES: dict[str, str] = {
    "{cwd}/.omp/skills": "cwd-join",
    "{cwd}/.claude/skills": "cwd-join",
    "{cwd}/.agent/skills": "walk-up",
    "{cwd}/.agents/skills": "walk-up",
    "{cwd}/.codex/skills": "cwd-join",
    "{cwd}/.opencode/skills": "cwd-join",
    "{cwd}/.github/skills": "cwd-join",
    "~/.omp/agent/skills": "home-join",
    "~/.omp/plugins/node_modules/*/skills": "home-join",
    "~/.agent/skills": "home-join",
    "~/.agents/skills": "home-join",
    "~/.omp/agent/managed-skills": "home-join",
}


def stop_chain(repo_root: str | None = None,
               cwd: str = FROZEN_CWD, home: str = FROZEN_HOME) -> tuple[str, ...]:
    """Directories the grounded walk-up loop visits, modelled on the frozen ELF bytes and
    upstream agents.ts lines 140-155: push every visited directory EXCEPT $HOME itself,
    stop at `repoRoot ?? $HOME`, step by dirname."""
    out: list[str] = []
    cur = cwd
    for _ in range(64):
        if cur != home:
            out.append(cur)
        if cur == (repo_root if repo_root is not None else home):
            break
        parent = posixpath.dirname(cur)
        if parent == cur:
            break
        cur = parent
    return tuple(out)


FROZEN_CHAIN = stop_chain(None)   # ("/home/u/proj/sub", "/home/u/proj") -- strictly below $HOME
AT_HOME_PROBES = (f"{FROZEN_CWD}/../sub/.probe/skills", "/home/u/../u/.probe/skills")

# --------------------------------------------------- the four M worlds and three K worlds

FORGED_WORLDS: tuple[tuple[str, dict[int, str]], ...] = (
    ("w_cross_row7", {7: 'return Xr.join(u.cwd, ".codex");'}),
    ("w_subdir_row9", {7: 'return Xr.join(u.cwd, ".codex");',
                       9: 'Zo.join(R.path, "commands")'}),
    ("w_misattr_row12", {7: 'return Xr.join(u.cwd, ".codex");',
                         9: 'Zo.join(R.path, "commands")',
                         12: 'dir: Zo.join(R.path, "skills"),'}),
    ("w_renderline_row6", {6: '**Tags:** ${t.tags.join(", ")}',
                           7: 'return Xr.join(u.cwd, ".codex");',
                           9: 'Zo.join(R.path, "commands")',
                           12: 'dir: Zo.join(R.path, "skills"),'}),
)

K_WORLDS: tuple[tuple[str, dict[int, str] | None, dict[int, str] | None, dict[int, str] | None], ...] = (
    # (name, pattern-mutations for semantics, reader-mutations, module-mutations);
    # pattern mutations apply to BOTH ledgers (A1.6 w_both_ledgers / w_home_escape).
    ("w_both_ledgers", {11: "/tmp/x/skills"}, None, None),
    ("w_module_mislabel", None, None, {2: "coding-agent/src/discovery/builtin.ts"}),
    ("w_home_escape", {1: "/etc/skills", 2: "/tmp/x/skills", 3: "~root/skills"}, None, None),
)

HEADER_RE = re.compile(rb"//[ \t]*packages/([A-Za-z0-9_./@-]+)")


class Inconclusive(Exception):
    """The evaluation itself cannot run (missing git, unreadable/unpinned ELF, ...)."""


# --------------------------------------------------------------------------- revision bytes

def git_show(repo: Path, rev: str, path: str) -> str | None:
    """Committed bytes of `path` at `rev`, or None when the path is absent there (S1)."""
    try:
        proc = subprocess.run(["git", "-C", str(repo), "show", f"{rev}:{path}"],
                              capture_output=True, check=False)
    except FileNotFoundError:
        raise Inconclusive("git not found")
    if proc.returncode != 0:
        return None
    return proc.stdout.decode("utf-8", "replace")


def pin_digest(data) -> str:
    return hashlib.sha256(bytes(data)).hexdigest()


def open_elf(path: Path, pinned: str | None):
    """mmap the ELF (never copy it, never exec it -- guard S5) and check the pinned build."""
    try:
        handle = open(path, "rb")
    except OSError as exc:
        raise Inconclusive(f"omp binary unreadable: {exc}")
    try:
        blob = mmap.mmap(handle.fileno(), 0, access=mmap.ACCESS_READ)
    except (OSError, ValueError) as exc:
        handle.close()
        raise Inconclusive(f"omp binary not mappable: {exc}")
    try:
        if blob.size() == 0:
            raise Inconclusive("omp binary is empty")
        digest = pin_digest(blob)
        if pinned is not None and digest != pinned:
            raise Inconclusive(f"omp binary sha256 {digest} is not the pinned build {pinned}")
    except Inconclusive:
        blob.close()
        handle.close()
        raise
    return blob, digest


# ------------------------------------------------------------------------------- ELF probes

def elf_line(blob, offset: int) -> bytes:
    start = blob.rfind(b"\n", max(0, offset - LINE_SPAN), offset)
    start = 0 if start < 0 else start + 1
    end = blob.find(b"\n", offset, offset + LINE_SPAN)
    end = len(blob) if end < 0 else end
    return blob[start:end]


def occurrences(blob, needle: bytes, limit: int = 8) -> list[int]:
    out, at = [], blob.find(needle)
    while at >= 0 and len(out) < limit:
        out.append(at)
        at = blob.find(needle, at + 1)
    return out


def count_occurrences(blob, needle: bytes) -> int:
    total, at = 0, blob.find(needle)
    while at >= 0:
        total += 1
        at = blob.find(needle, at + 1)
    return total


def header_table(blob) -> list[tuple[int, str]]:
    return [(m.start(), m.group(1).decode("utf-8", "replace"))
            for m in HEADER_RE.finditer(blob)]


def nearest_header(headers, offset: int) -> tuple[int, str] | None:
    positions = [h[0] for h in headers]
    idx = bisect.bisect_right(positions, offset) - 1
    return headers[idx] if idx >= 0 else None


def next_header_offset(headers, offset: int) -> int:
    positions = [h[0] for h in headers]
    idx = bisect.bisect_right(positions, offset)
    return headers[idx][0] if idx < len(headers) else len(blob)


def module_offsets_of(blob, module: str) -> list[int]:
    header = b"// packages/" + module.encode("utf-8")
    pattern = re.compile(re.escape(header) + rb"(?![A-Za-z0-9_.@/-])")
    return [m.start() for m in pattern.finditer(blob)]


# --------------------------------------------------------------------------- conjunct 1

def pattern_problem(pattern: str) -> str | None:
    """Conjunct 1's shape half: no `..` segment, no wildcard in the first segment."""
    segments = [s for s in pattern.split("/") if s]
    if not segments:
        return f"pattern {pattern!r} names no directory"
    if ".." in segments:
        return f"pattern {pattern!r} carries a `..` segment"
    for prefix in ("{cwd}/", "~/"):
        if pattern.startswith(prefix):
            rel = pattern[len(prefix):]
            break
    else:
        rel = pattern.lstrip("/")
    first = next((s for s in rel.split("/") if s), "")
    if not first:
        return f"pattern {pattern!r} has no first segment"
    if WILD & set(first):
        return f"pattern {pattern!r} has a wildcard in its first segment ({first!r})"
    return None


def class_problem(pattern: str) -> str | None:
    """A1.3: first segment must be `{cwd}`, `~`, a bare relative name, or a frozen
    ledger pattern; absolute `/…` and `~user` patterns are refused outright."""
    if pattern in PATTERN_SET:
        return None
    if pattern.startswith("{cwd}/") or pattern == "{cwd}":
        return None
    if pattern.startswith("~"):
        if not pattern.startswith("~/"):
            return f"pattern {pattern!r} is a `~user` escape (refused outright)"
        return None
    if pattern.startswith("/"):
        return f"pattern {pattern!r} is absolute (refused outright; A1.3)"
    if pattern and not pattern.startswith("/"):
        return None                      # bare relative name is a legal class
    return f"pattern {pattern!r} names no legal first segment"


# --------------------------------------------------------------------------- conjunct 2

def binding_stats(blob, token: str, token_pin: int, module_offset: int, headers) -> dict:
    """A2.1: pin re-find, chunk interval, total and in-chunk occurrence counts."""
    raw = token.encode("utf-8")
    at_pin = blob[token_pin:token_pin + len(raw)]
    refound = at_pin == raw
    end = next_header_offset(headers, module_offset)
    in_chunk = sum(1 for off in iter_all_occurrences(blob, raw)
                   if module_offset <= off < end)
    total = count_occurrences(blob, raw)
    return {"refound": refound, "pin": token_pin, "chunk": (module_offset, end),
            "in_chunk": in_chunk, "total": total}


def iter_all_occurrences(blob, needle: bytes):
    at = blob.find(needle)
    while at >= 0:
        yield at
        at = blob.find(needle, at + 1)


def reader_grounded(blob, reader: str, pattern: str, ctx, headers,
                    other_patterns: list[str]) -> tuple[bool, str, int | None, dict]:
    """Conjunct 2 (A1.5 pin + A1.4/A2.1 binding).  Returns (ok, why, pin, binding stats)."""
    stats: dict = {}
    if len(reader) < QUOTE_MIN:
        return False, f"reader_quote shorter than {QUOTE_MIN} chars", None, stats
    reader_pins = ctx["reader_pins"]
    pin = reader_pins.get(pattern)
    if pin is None:
        return False, f"no frozen reader pin for pattern {pattern!r}", None, stats
    raw = reader.encode("utf-8")
    if blob[pin:pin + len(raw)] != raw:
        return False, (f"reader pin mismatch: the frozen offset {pin} does not hold this "
                       f"reader_quote (A1.5)"), pin, stats
    line = elf_line(blob, pin)
    if not any(token.encode("utf-8") in line for token in JOIN_TOKENS):
        return False, "the pinned reader line carries no path-join token", pin, stats

    sets = ctx.get("binding_sets", BINDING_SETS)
    binding = sets.get(pattern, ())
    if not binding:
        return False, f"binding token set for {pattern!r} is empty (refused)", pin, stats
    token = binding[0]
    if token in GENERIC_TOKENS:
        return False, f"binding token {token!r} is in GENERIC_TOKENS (A1.4 cond 5)", pin, stats

    token_pins = ctx["token_pins"]
    module_offsets = ctx["module_offsets"]
    module_offset = module_offsets.get(pattern)
    if module_offset is None:
        return False, f"no frozen module offset for pattern {pattern!r}", pin, stats
    token_pin = token_pins.get(pattern)
    if token_pin is None:
        return False, f"no frozen binding token pin for pattern {pattern!r}", pin, stats
    stats = binding_stats(blob, token, token_pin, module_offset, headers)
    if not stats["refound"]:
        return False, (f"binding token {token!r} does not re-find byte-exactly at its "
                       f"frozen pin {token_pin} (A2.1 cond 1)"), pin, stats
    start, end = stats["chunk"]
    if not (start <= token_pin < end):
        return False, (f"binding token pin {token_pin} lies outside the row's chunk "
                       f"[{start}, {end}) (A2.1 cond 2)"), pin, stats
    if stats["in_chunk"] == 0:
        return False, (f"binding token {token!r} has zero in-chunk occurrences "
                       f"(A2.1 cond 4)"), pin, stats
    for other in other_patterns:
        if other == pattern:
            continue
        other_pin = reader_pins.get(other)
        if other_pin is None:
            continue
        if token.encode("utf-8") in elf_line(blob, other_pin):
            return False, (f"binding token {token!r} also occurs on another row's "
                            f"reader line ({other!r}) (A1.4 cond 3)"), pin, stats
    binary_quote = ctx.get("binary_quotes", {}).get(pattern)
    if binary_quote:
        boff = blob.find(binary_quote.encode("utf-8"))
        if boff >= 0 and token.encode("utf-8") in elf_line(blob, boff):
            return False, (f"binding token {token!r} is a substring of the row's "
                            f"binary_quote line (A1.4 cond 4)"), pin, stats
    return True, "", pin, stats


# --------------------------------------------------------------------------- conjunct 3

def module_grounded(headers, module: str, reader_pin: int | None) -> tuple[bool, str]:
    """Conjunct 3 (A1.2): the NEAREST preceding header names exactly the row's module and
    the reader pin lies before the next header."""
    if not module.strip():
        return False, "module cell is empty"
    if ".." in module.split("/"):
        return False, f"module {module!r} carries a `..` segment"
    if any(ch in module for ch in " \t"):
        return False, f"module {module!r} carries whitespace"
    if reader_pin is None:
        return False, "reader pin unavailable; no position to order the header against"
    near = nearest_header(headers, reader_pin)
    if near is None:
        return False, "no `// packages/` header precedes the reader pin"
    off, near_module = near
    if near_module != module:
        return False, (f"nearest preceding header at {off} is {near_module!r}, "
                       f"the row names {module!r} (A1.2)")
    end = next_header_offset(headers, off)
    if reader_pin >= end:
        return False, (f"reader pin {reader_pin} lies at or after the next header at {end}")
    return True, ""


# --------------------------------------------------------------------------- conjunct 4

def walker_grounded(blob, module: str, headers) -> tuple[bool, str]:
    """Conjunct 4's live half for the walker module: the loop quotes sit in one chunk."""
    if module != WALKER_MODULE:
        return False, (f"walker bound requires module {WALKER_MODULE!r}, "
                       f"the row names {module!r}")
    starts = module_offsets_of(blob, module)
    positions = [h[0] for h in headers]
    for start in starts:
        idx = bisect.bisect_right(positions, start)
        end = headers[idx][0] if idx < len(headers) else len(blob)
        if all(any(start <= off < end
                   for off in occurrences(blob, quote.encode("utf-8"), limit=64))
               for quote in WALKER_QUOTES):
            return True, ""
    return False, (f"the walker loop quotes {list(WALKER_QUOTES)} do not occur together "
                   f"inside one `// packages/{module}` chunk")


def expansions(pattern: str, chain) -> list[str]:
    if pattern.startswith("{cwd}/"):
        rest = pattern[len("{cwd}/"):]
        return [posixpath.normpath(posixpath.join(d, rest)) for d in chain]
    if pattern.startswith("~/"):
        return [posixpath.normpath(posixpath.join(FROZEN_HOME, pattern[2:]))]
    return [posixpath.normpath(posixpath.join(FROZEN_CWD, pattern))]


def at_or_above(path: str, home: str = FROZEN_HOME) -> bool:
    return path == home or home.startswith(path.rstrip("/") + "/")


def walk_chain(pattern: str) -> tuple[str, ...] | None:
    shape = WALK_SHAPES.get(pattern)
    if shape is None:
        return None
    if shape == "walk-up":
        return FROZEN_CHAIN
    if shape == "cwd-join":
        return (FROZEN_CWD,)
    return (FROZEN_HOME,)          # home-join (includes the node_modules glob row)


def matches_row(pattern: str, candidate: str, chain) -> bool:
    if ".." in candidate.split("/"):
        return False
    if ".." in posixpath.normpath(candidate).split("/"):
        return False
    return any(fnmatch.fnmatchcase(candidate, exp) for exp in expansions(pattern, chain))


def bound_grounded(pattern: str, module: str, blob, headers) -> tuple[bool, str]:
    problem = pattern_problem(pattern)
    if problem:
        return False, problem
    class_why = class_problem(pattern)
    if class_why:
        return False, class_why
    shape = WALK_SHAPES.get(pattern)
    if shape is None:
        return False, f"no frozen walk shape for pattern {pattern!r}"
    if shape == "walk-up":
        ok, why = walker_grounded(blob, module, headers)
        if not ok:
            return False, f"walker bound ungrounded: {why}"
    chain = walk_chain(pattern)
    assert chain is not None
    for cand in expansions(pattern, chain):
        if ".." in cand.split("/"):
            return False, f"pattern {pattern!r} expands to a `..` candidate ({cand})"
        if pattern.startswith("~/"):
            if not (cand == FROZEN_HOME or cand.startswith(FROZEN_HOME + "/")):
                return False, f"pattern {pattern!r} expands outside $HOME ({cand})"
        else:
            if at_or_above(cand):
                return False, (f"pattern {pattern!r} expands to {cand}, which is $HOME "
                               f"or above it (A1.3)")
            if not any(cand == d or cand.startswith(d + "/") for d in chain):
                return False, (f"pattern {pattern!r} candidate {cand} escapes the walk set "
                               f"{list(chain)}")
    for probe in AT_HOME_PROBES:
        if matches_row(pattern, probe, chain):
            return False, f"pattern {pattern!r} matches the `..` candidate {probe}"
    return True, ""


# --------------------------------------------------------------------------- conjunct 5

def binary_grounded(blob, quote: str) -> tuple[bool, str]:
    if not quote.strip():
        return False, "binary_quote cell is empty"
    if blob.find(quote.encode("utf-8")) < 0:
        return False, "binary_quote not located in the omp ELF"
    return True, ""


# --------------------------------------------------------------------------------- scoring

def parse_ledger(text: str, header: str) -> tuple[list[tuple[int, str]] | None, str | None]:
    lines = [line for line in text.splitlines() if line.strip()]
    if not lines:
        return None, "ledger is empty"
    if lines[0] != header:
        return None, f"header is not {header!r}"
    return list(enumerate(lines[1:], 2)), None


def roots_rows(text: str | None) -> tuple[list[tuple[int, str]] | None, str | None]:
    if text is None:
        return None, f"{ROOTS_LEDGER} absent"
    return parse_ledger(text, ROOTS_HEADER)


def ledger_patterns(rows) -> list[str]:
    out = []
    for _, line in rows:
        cells = line.split("\t")
        out.append(cells[0].strip() if cells else "")
    return out


def apply_reader_world(rows, mutations: dict[int, str]) -> str:
    out = [SEMANTICS_HEADER]
    for index, (_, line) in enumerate(rows, 1):
        cells = line.split("\t")
        if index in mutations and len(cells) == 4:
            cells[3] = mutations[index]
            line = "\t".join(cells)
        out.append(line)
    return "\n".join(out) + "\n"


def apply_cell_world(rows, index_mutations: dict[int, dict[int, str]]) -> str:
    """Generic cell rewriter: {row_index: {cell_index: new_value}}."""
    out = [SEMANTICS_HEADER]
    for index, (_, line) in enumerate(rows, 1):
        cells = line.split("\t")
        muts = index_mutations.get(index)
        if muts:
            for cell, value in muts.items():
                if len(cells) == 4:
                    cells[cell] = value
            line = "\t".join(cells)
        out.append(line)
    return "\n".join(out) + "\n"


def apply_roots_pattern_world(roots_text: str, mutations: dict[int, str]) -> str:
    parsed, err = roots_rows(roots_text)
    if parsed is None or err:
        return roots_text
    out = [ROOTS_HEADER]
    for index, (_, line) in enumerate(parsed, 1):
        cells = line.split("\t")
        if index in mutations and len(cells) == 2:
            cells[0] = mutations[index]
            line = "\t".join(cells)
        out.append(line)
    return "\n".join(out) + "\n"


def score(semantics: str | None, roots: str | None, blob, out, ctx) -> tuple[int, dict, list]:
    """Evaluate the five conjuncts; returns (grounded N, guards, per-row results)."""
    headers = header_table(blob)
    guards = {"S1": True, "S2": True, "S3": True, "S4": None, "S5": True}
    anchor = ctx["anchor_patterns"]

    parsed_roots, roots_err = roots_rows(roots)
    root_patterns = ledger_patterns(parsed_roots) if parsed_roots else []
    if roots_err:
        out(f"roots ledger: {roots_err}")

    rows: list[tuple[int, str]] = []
    sem_err = None
    if semantics is None:
        sem_err = f"{SEMANTICS_LEDGER} absent at the revision"
    else:
        parsed, sem_err = parse_ledger(semantics, SEMANTICS_HEADER)
        if parsed is not None:
            rows = parsed
    if sem_err:
        out(f"semantics ledger: {sem_err}")

    seen = ledger_patterns(rows)
    if seen != anchor or seen != list(PATTERN_SET):
        guards["S3"] = False
        if len(seen) != len(anchor):
            out(f"S3 detail: semantics ledger carries {len(seen)} patterns, the pin "
                f"{PATTERN_PIN_REV} anchor carries {len(anchor)}")
        else:
            first = next(i for i, (a, b) in enumerate(zip(seen, anchor)) if a != b)
            out(f"S3 detail: pattern {first + 1} is {seen[first]!r}; the pin "
                f"{PATTERN_PIN_REV} anchor has {anchor[first]!r} (A1.1a); "
                f"PATTERN_SET has {PATTERN_SET[first]!r} (A1.1b)")

    ctx = dict(ctx)
    ctx["binary_quotes"] = {}
    for _, line in rows:
        cells = line.split("\t")
        if len(cells) == 4:
            ctx["binary_quotes"][cells[0].strip()] = cells[1].strip()

    results: list[tuple[int, str, bool, list[str]]] = []
    grounded = 0
    all_patterns = ledger_patterns(rows)
    for index, (number, line) in enumerate(rows, 1):
        if index > TOTAL:
            out(f"row {index:2d} EXTRA: beyond the frozen denominator of {TOTAL}")
            results.append((index, "", False, ["beyond the frozen denominator"]))
            continue
        cells = [cell.rstrip("\r") for cell in line.split("\t")]
        if len(cells) != 4:
            why = f"want 4 tab-separated cells, got {len(cells)}"
            out(f"row {index:2d} FAIL (ledger line {number}): {why}")
            results.append((index, "", False, [why]))
            continue
        pattern, binary_quote = cells[0].strip(), cells[1].strip()
        module, reader = cells[2].strip(), cells[3].strip()
        reasons = []
        expected = anchor[index - 1] if index <= len(anchor) else None
        if expected is None:
            reasons.append(f"the pin {PATTERN_PIN_REV} anchor has no row {index} (A1.1a)")
        elif pattern != expected:
            reasons.append(f"pattern {pattern!r} is not the pin {PATTERN_PIN_REV} "
                           f"anchor's row {index} ({expected!r}) (A1.1a)")
        if pattern not in PATTERN_SET:
            reasons.append(f"pattern {pattern!r} is not in the frozen PATTERN_SET (A1.1b)")
        else:
            problem = pattern_problem(pattern)
            if problem:
                reasons.append(problem)
            class_why = class_problem(pattern)
            if class_why:
                reasons.append(class_why)
        stats: dict = {}
        reader_ok = False
        reader_pin = None
        if pattern in PATTERN_SET or True:
            reader_ok, reader_why, reader_pin, stats = reader_grounded(
                blob, reader, pattern, ctx, headers, all_patterns)
            if not reader_ok:
                reasons.append(reader_why)
        module_ok, module_why = module_grounded(headers, module, reader_pin)
        if not module_ok:
            reasons.append(module_why)
        bound_ok, bound_why = bound_grounded(pattern, module, blob, headers)
        if not bound_ok:
            reasons.append(bound_why)
        binary_ok, binary_why = binary_grounded(blob, binary_quote)
        if not binary_ok:
            reasons.append(binary_why)
        token = (BINDING_SETS.get(pattern) or ("?",))[0]
        binding_note = (f"binding={token} total={stats.get('total', '?')} "
                        f"in-chunk={stats.get('in_chunk', '?')} "
                        f"out-chunk={stats.get('total', 0) - stats.get('in_chunk', 0)}"
                        ) if stats else "binding=n/a"
        results.append((index, pattern, not reasons, reasons))
        if reasons:
            out(f"row {index:2d} FAIL {pattern!r}: " + "; ".join(reasons)
                + f" [{binding_note}]")
        else:
            grounded += 1
            out(f"row {index:2d} GROUND {pattern!r} module={module!r} @{reader_pin} "
                f"[{binding_note}]")

    if len(root_patterns) != TOTAL:
        out(f"note: the round-86 ledger at the revision carries {len(root_patterns)} "
            f"patterns; the frozen denominator is {TOTAL} (plans/round-88.md C1)")
    return grounded, guards, results


def world_rejected(rows, blob, ctx, semantics_text: str, roots_text: str,
                   mutated: Iterable[int] = ()) -> tuple[bool, int, list[str]]:
    """Score one world; rejected iff N < 12 with a mutated row among the failures."""
    lines: list[str] = []
    world_n, _, world_rows = score(semantics_text, roots_text, blob, lines.append, ctx)
    failing = [index for index, _, ok, _ in world_rows if not ok]
    hit = any(index in failing for index in mutated)
    return (world_n < TOTAL and hit), world_n, lines


def forged_verdicts(rows, roots_text: str, blob, ctx, out) -> tuple[int, list[str]]:
    rejected, detail = 0, []
    for name, mutations in FORGED_WORLDS:
        text = apply_reader_world(rows, mutations)
        ok, world_n, _ = world_rejected(rows, blob, ctx, text, roots_text, mutations.keys())
        rejected += 1 if ok else 0
        verb = "REJECTED" if ok else "ACCEPTED"
        detail.append(f"forgery {name} {verb} (grounded {world_n} of {TOTAL})")
        out(detail[-1])
    return rejected, detail


def k_world_verdicts(rows, roots_text: str, blob, ctx, out) -> tuple[int, list[str]]:
    """A1.6's three disclosed K classes; the exit rule never reads K."""
    rejected, detail = 0, []
    for name, pattern_muts, reader_muts, module_muts in K_WORLDS:
        sem_muts: dict[int, dict[int, str]] = {}
        if pattern_muts:
            for idx, pat in pattern_muts.items():
                sem_muts[idx] = {0: pat}
        if reader_muts:
            for idx, reader in reader_muts.items():
                sem_muts.setdefault(idx, {})[3] = reader
        if module_muts:
            for idx, module in module_muts.items():
                sem_muts.setdefault(idx, {})[2] = module
        semantics_text = apply_cell_world(rows, sem_muts) if sem_muts else \
            "\n".join([SEMANTICS_HEADER] + [line for _, line in rows]) + "\n"
        roots_variant = apply_roots_pattern_world(roots_text, pattern_muts) \
            if pattern_muts else roots_text
        mutated = tuple(sorted(set(pattern_muts or {}) | set(reader_muts or {})
                               | set(module_muts or {})))
        ok, world_n, lines = world_rejected(rows, blob, ctx, semantics_text,
                                            roots_variant, mutated)
        rejected += 1 if ok else 0
        verb = "REJECTED" if ok else "ACCEPTED"
        detail.append(f"k-class {name} {verb} (grounded {world_n} of {TOTAL})")
        out(detail[-1])
    return rejected, detail


# --------------------------------------------------------------------------------- floors

def floor_from_registry() -> tuple[int | None, str]:
    path = REPO / FLOORS_REGISTRY
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
        floor = payload["instruments"][INSTRUMENT_KEY]["floor"]
        if isinstance(floor, int) and not isinstance(floor, bool):
            return floor, "worktree"
    except (OSError, ValueError, KeyError, TypeError):
        pass
    return None, "absent"


# ---------------------------------------------------------------------------- synthetic ELF

HONEST_ROWS = [
    ('{cwd}/.omp/skills', 'Native OMP configuration from ~/.omp and .omp/',
     'coding-agent/src/discovery/builtin.ts', 'dir: fr.join(k, Ou.projectDir, "skills"),'),
    ('{cwd}/.claude/skills', 'Load skills from .claude/skills/*/SKILL.md',
     'coding-agent/src/discovery/claude.ts', 'dir: Fr.join(k, eh, "skills"),'),
    ('{cwd}/.agent/skills', 'Load skills from .agent/skills and .agents/skills '
     '(project walk-up + user home)', 'coding-agent/src/discovery/agents.ts',
     'x.push(Rs.join(R, _, ...p));'),
    ('{cwd}/.agents/skills', 'Load skills from .agent/skills and .agents/skills '
     '(project walk-up + user home)', 'coding-agent/src/discovery/agents.ts',
     'x.push(Rs.join(R, _, ...p));'),
    ('{cwd}/.codex/skills', 'Load skills from ~/.codex/skills and .codex/skills/',
     'coding-agent/src/discovery/codex.ts', 'return Xr.join(u.cwd, ".codex");'),
    ('{cwd}/.opencode/skills', 'Load skills from ~/.config/opencode/skills/ and '
     '.opencode/skills/', 'coding-agent/src/discovery/helpers.ts',
     'return d.join(e.cwd, r.projectDir, n);'),
    ('{cwd}/.github/skills', 'Load skills from .github/skills/*/SKILL.md',
     'coding-agent/src/discovery/helpers.ts', 'return d.join(e.cwd, r.projectDir, n);'),
    ('~/.omp/agent/skills', 'Native OMP configuration from ~/.omp and .omp/',
     'coding-agent/src/discovery/builtin.ts', 'dir: fr.join(we(), "skills"),'),
    ('~/.omp/plugins/node_modules/*/skills', 'var Gh = ".omp";',
     'coding-agent/src/discovery/omp-plugins.ts', 'dir: Zo.join(R.path, "skills"),'),
    ('~/.agent/skills', 'Load skills from .agent/skills and .agents/skills '
     '(project walk-up + user home)', 'coding-agent/src/discovery/agents.ts',
     'return Wne(u).flatMap((x) => y1.map((R) => Rs.join(x, R, ...p)));'),
    ('~/.agents/skills', 'Load skills from .agent/skills and .agents/skills '
     '(project walk-up + user home)', 'coding-agent/src/discovery/agents.ts',
     'return Wne(u).flatMap((x) => y1.map((R) => Rs.join(x, R, ...p)));'),
    ('~/.omp/agent/managed-skills', 'Auto-generated managed skills from '
     '~/.omp/agent/managed-skills', 'coding-agent/src/autolearn/managed-skills.ts',
     'return Zm.join(u, "managed-skills");'),
]

WALKER_CODE = [
    'function V9(u, ...p) {',
    '  const x = [];',
    '  let R = u.cwd;',
    '  while (true) {',
    '    ' + WALKER_SKIP_QUOTE,
    '      for (const _ of y1) {',
    '        x.push(Rs.join(R, _, ...p));',
    '      }',
    '    }',
    '    ' + WALKER_STOP_QUOTE,
    '      break;',
    '    const k = Rs.dirname(R);',
    '    if (k === R)',
    '      break;',
    '    R = k;',
    '  }',
]

PLUGIN_COMMANDS_LINE = ('  const x = await Promise.all(p.map((R) => '
                        '$n(u, Zo.join(R.path, "commands"), xo, R.level, {')


def syn_elf(with_walker: bool = True, walker_in_chunk: bool = True,
            order_swap: str | None = None) -> bytes:
    def chunk(module: str, lines: list[str]) -> list[str]:
        return [f"// packages/{module}"] + lines

    agents_body = ['var y1 = [".agent", ".agents"];']
    agents_body += [
        '  return Wne(u).flatMap((x) => y1.map((R) => Rs.join(x, R, ...p)));',
        '        x.push(Rs.join(R, _, ...p));',
    ]
    if with_walker and walker_in_chunk:
        agents_body += WALKER_CODE
    agents_body += [
        'Load skills from .agent/skills and .agents/skills (project walk-up + user home)',
    ]
    builtin_body = [
        'Native OMP configuration from ~/.omp and .omp/',
        '      dir: fr.join(k, Ou.projectDir, "skills"),',
        '    dir: fr.join(we(), "skills"),',
    ]
    claude_body = [
        'Load skills from .claude/skills/*/SKILL.md',
        '        dir: Fr.join(k, eh, "skills"),',
    ]
    codex_body = [
        'Load skills from ~/.codex/skills and .codex/skills/',
        '  return Xr.join(u.cwd, ".codex");',
    ]
    if with_walker and not walker_in_chunk:
        codex_body += WALKER_CODE          # the walker code lands in the WRONG chunk
    helpers_body = [
        'opencode: { userBase: ".config/opencode", userAgent: ".config/opencode", '
        'projectDir: ".opencode" },',
        'github: { userBase: null, userAgent: null, projectDir: ".github" },',
        'Load skills from ~/.config/opencode/skills/ and .opencode/skills/',
        'Load skills from .github/skills/*/SKILL.md',
        '  return d.join(e.cwd, r.projectDir, n);',
    ]
    plugins_body = [
        'var Gh = ".omp";',
        '    dir: Zo.join(R.path, "skills"),',
        PLUGIN_COMMANDS_LINE,
    ]
    managed_body = [
        'Auto-generated managed skills from ~/.omp/agent/managed-skills',
        '  return Zm.join(u, "managed-skills");',
    ]
    chunks = [
        chunk('coding-agent/src/autolearn/managed-skills.ts', managed_body),
        chunk('coding-agent/src/discovery/builtin.ts', builtin_body),
        chunk('coding-agent/src/discovery/claude.ts', claude_body),
        chunk('coding-agent/src/discovery/agents.ts', agents_body),
        chunk('coding-agent/src/discovery/codex.ts', codex_body),
        chunk('coding-agent/src/discovery/helpers.ts', helpers_body),
        chunk('coding-agent/src/discovery/omp-plugins.ts', plugins_body),
        ['// packages/coding-agent/src/prompts/agents/frontmatter.md',
         '              c += `**Tags:** ${t.tags.join(", ")}`',
         '**Tags:** ${t.tags.join(", ")}'],
    ]
    if order_swap == 'coding-agent/src/autolearn/managed-skills.ts':
        chunks[0] = [managed_body[1], chunks[0][0], managed_body[0]]
    lines: list[str] = []
    for body in chunks:
        lines += body
    return ("\n".join(lines) + "\n").encode("utf-8")


def syn_semantics(rows=None) -> str:
    rows = HONEST_ROWS if rows is None else rows
    return "\n".join([SEMANTICS_HEADER] + ["\t".join(r) for r in rows]) + "\n"


def syn_roots() -> str:
    return "\n".join([ROOTS_HEADER] + ["\t".join([r[0], r[1]]) for r in HONEST_ROWS]) + "\n"


def syn_ctx(blob: bytes) -> dict:
    """Synthetic-world ctx: pins and offsets derived from the synthetic ELF itself."""
    reader_pins, token_pins, module_offsets = {}, {}, {}
    for pattern, _b, module, reader in HONEST_ROWS:
        reader_pins[pattern] = blob.find(reader.encode("utf-8"))
        token_pins[pattern] = blob.find(BINDING[pattern].encode("utf-8"))
        module_offsets[pattern] = blob.find(f"// packages/{module}".encode("utf-8"))
    return {"anchor_patterns": [r[0] for r in HONEST_ROWS],
            "reader_pins": reader_pins, "token_pins": token_pins,
            "module_offsets": module_offsets}


def world(blob, semantics: str | None, roots: str | None, ctx):
    lines: list[str] = []
    grounded, guards, _ = score(semantics, roots, blob, lines.append, ctx)
    ok = (grounded == TOTAL and guards["S1"] and guards["S3"]
          and guards["S4"] is not False and guards["S5"])
    return (0 if ok else 1), lines, grounded, guards


# ------------------------------------------------------------------------------- self-test

def source_hygiene(source: str) -> tuple[bool, str]:
    """S5's source arms, AST-based: imports stay in the allowed stdlib set and no
    exec/system/spawn/Popen call exists anywhere in the file."""
    import ast
    allowed = {"__future__", "argparse", "ast", "bisect", "contextlib", "fnmatch", "hashlib",
               "io", "json", "mmap", "os", "posixpath", "re", "subprocess", "sys", "pathlib",
               "tempfile", "typing"}
    try:
        tree = ast.parse(source)
    except SyntaxError as exc:
        return False, f"source does not parse: {exc}"
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for alias in node.names:
                if alias.name.split(".")[0] not in allowed:
                    return False, f"import {alias.name}"
        elif isinstance(node, ast.ImportFrom):
            if (node.module or "").split(".")[0] not in allowed:
                return False, f"from {node.module} import"
        elif isinstance(node, ast.Call):
            name = getattr(node.func, "attr", getattr(node.func, "id", ""))
            if name in {"system", "spawn", "spawnl", "spawnv", "exec", "execv", "execve",
                        "execvp", "Popen", "fork", "forkpty"}:
                return False, f"process-spawning call {name}()"
    return True, ""


def self_test(work: Path | None) -> int:
    failures: list[str] = []
    assertions = 0

    def check(name: str, ok: bool, detail: str = "") -> None:
        nonlocal assertions
        assertions += 1
        if not ok:
            failures.append(f"{name}: {detail}" if detail else name)

    if work is not None:
        work.mkdir(parents=True, exist_ok=True)   # honoured; the arms stay in memory

    blob = syn_elf()
    ctx = syn_ctx(blob)
    honest_sem, honest_roots = syn_semantics(), syn_roots()

    # ---- config/ arms: the frozen tables themselves (S4/S5 source hygiene) -------------
    source = Path(__file__).read_text(encoding="utf-8")
    check("config: binding block sha256 matches the frozen constant",
          hashlib.sha256(BINDING_BLOCK.encode("utf-8")).hexdigest() == BINDING_BLOCK_SHA256)
    check("config: token pin block sha256 matches the frozen constant",
          hashlib.sha256(TOKEN_PIN_BLOCK.encode("utf-8")).hexdigest() == TOKEN_PIN_BLOCK_SHA256)
    check("config: reader pin block sha256 matches the frozen constant",
          hashlib.sha256(READER_OFFSET_BLOCK.encode("utf-8")).hexdigest()
          == READER_OFFSET_BLOCK_SHA256)
    check("config: module offset block sha256 matches the frozen constant",
          hashlib.sha256(MODULE_OFFSET_BLOCK.encode("utf-8")).hexdigest()
          == MODULE_OFFSET_BLOCK_SHA256)
    check("config: PATTERN_SET sha256 matches the frozen constant",
          hashlib.sha256(PATTERN_SET_BLOCK.encode("utf-8")).hexdigest() == PATTERN_SET_SHA256)
    check("config: twelve binding sets, all non-empty",
          len(BINDING_SETS) == TOTAL and all(any(t for t in s) for s in BINDING_SETS.values()))
    check("config: no binding token is in GENERIC_TOKENS (A1.4 cond 5)",
          all(t[0] not in GENERIC_TOKENS for t in BINDING_SETS.values()))
    check("config: distinct sets within each shared-quote group (A1.4 cond 6 / A2.2)",
          all(BINDING[a] != BINDING[b] for a, b in SHARED_QUOTE_GROUPS))
    check("config: walk shapes cover the frozen denominator",
          set(WALK_SHAPES) == {r[0] for r in HONEST_ROWS} and len(WALK_SHAPES) == TOTAL)
    check("config: reader pins and module offsets cover the frozen denominator",
          len(READER_OFFSETS) == TOTAL and len(MODULE_OFFSETS) == TOTAL
          and len(TOKEN_PINS) == TOTAL)
    check("config/S5: source opens the ELF read-only (mmap.ACCESS_READ)",
          "mmap.ACCESS_READ" in source)
    hygiene_ok, hygiene_why = source_hygiene(source)
    check("config/S5: source never execs and imports no network module",
          hygiene_ok, hygiene_why)
    floor, floor_source = floor_from_registry()
    if floor is not None:
        print(f"note: floors row {INSTRUMENT_KEY} present ({floor_source}), floor {floor}; "
              f"the S4 floor assertion runs at the end of the arm list")

    # ---- honest/ arm: the must-pass positive control ------------------------------------
    rc, lines, grounded, guards = world(blob, honest_sem, honest_roots, ctx)
    check("honest: exits 0", rc == 0, " | ".join(lines[-2:]))
    check("honest: grounds 12 of 12", grounded == TOTAL, str(grounded))
    check("honest: every row GROUNDs with its binding stats printed",
          sum(1 for l in lines if l.startswith("row ") and " GROUND " in l) == TOTAL
          and sum(1 for l in lines if "in-chunk=" in l) >= TOTAL)
    check("honest: guard S3 PASS", guards["S3"] is True)
    check("honest: no row FAIL", not any(" FAIL " in l for l in lines))

    # ---- M-worlds/: the four r87 forged classes, each rejected --------------------------
    honest_line_rows = list(enumerate(HONEST_ROWS, 1))
    rows_pairs = [(i + 2, "\t".join(r)) for i, r in enumerate(HONEST_ROWS)]
    for name, mutations in FORGED_WORLDS:
        text = apply_reader_world(rows_pairs, mutations)
        rejected, world_n, wlines = world_rejected(rows_pairs, blob, ctx, text,
                                                   honest_roots, mutations.keys())
        check(f"M-worlds/{name}: rejected below the denominator",
              rejected and world_n == TOTAL - len(mutations), f"grounded {world_n}")
        check(f"M-worlds/{name}: the mutated row is the failure",
              any(str(idx) in l or HONEST_ROWS[idx - 1][0] in l
                  for idx in mutations for l in wlines if " FAIL " in l))

    # ---- A1.1/ w_both_ledgers: one commit rewriting both ledgers ------------------------
    both_sem = apply_cell_world(rows_pairs, {11: {0: "/tmp/x/skills"}})
    both_roots = apply_roots_pattern_world(honest_roots, {11: "/tmp/x/skills"})
    rc, lines, grounded, guards = world(blob, both_sem, both_roots, ctx)
    check("A1.1/w_both_ledgers: rejected", rc == 1 and grounded < TOTAL,
          f"rc={rc} grounded={grounded}")
    check("A1.1/w_both_ledgers: reasons name the pin anchor (A1.1a)",
          any("pin 223ae62424f8ab1eb365d733eb648d6228ddd7e8" in l for l in lines))
    check("A1.1/w_both_ledgers: reasons name PATTERN_SET (A1.1b)",
          any("PATTERN_SET" in l for l in lines))
    check("A1.1/w_both_ledgers: reasons name the absolute refusal (A1.3)",
          any("absolute" in l for l in lines))

    # ---- A1.2/ w_module_mislabel: claude row relabelled builtin.ts ----------------------
    misl_sem = apply_cell_world(rows_pairs, {2: {2: "coding-agent/src/discovery/builtin.ts"}})
    rc, lines, grounded, _ = world(blob, misl_sem, honest_roots, ctx)
    check("A1.2/w_module_mislabel: rejected", rc == 1 and grounded < TOTAL,
          f"rc={rc} grounded={grounded}")
    check("A1.2/w_module_mislabel: reason names the nearest-header mismatch",
          any("nearest preceding header" in l for l in lines))

    # ---- A1.3/ w_home_escape: /etc, /tmp, ~root escapes ---------------------------------
    esc_sem = apply_cell_world(rows_pairs, {1: {0: "/etc/skills"}, 2: {0: "/tmp/x/skills"},
                                            3: {0: "~root/skills"}})
    esc_roots = apply_roots_pattern_world(honest_roots, {1: "/etc/skills",
                                                         2: "/tmp/x/skills",
                                                         3: "~root/skills"})
    rc, lines, grounded, _ = world(blob, esc_sem, esc_roots, ctx)
    check("A1.3/w_home_escape: rejected", rc == 1 and grounded < TOTAL,
          f"rc={rc} grounded={grounded}")
    check("A1.3/w_home_escape: absolute patterns refused outright",
          sum(1 for l in lines if "absolute (refused outright" in l) >= 2)
    check("A1.3/w_home_escape: `~user` pattern refused outright",
          any("`~user` escape" in l for l in lines))

    # ---- A1.4/ conjunct-2 refusal arms --------------------------------------------------
    doc_rows = list(HONEST_ROWS)
    doc_rows[0] = (doc_rows[0][0], doc_rows[0][1], doc_rows[0][2],
                   'Native OMP configuration from ~/.omp and .omp/')
    rc, lines, grounded, _ = world(blob, syn_semantics(doc_rows), honest_roots, ctx)
    check("A1.4/doc-quote: refuses its row", rc == 1 and grounded == TOTAL - 1,
          f"rc={rc} grounded={grounded}")
    check("A1.4/doc-quote: the failure names the reader pin (A1.5)",
          any("reader pin mismatch" in l for l in lines))
    miss_rows = list(HONEST_ROWS)
    miss_rows[3] = (miss_rows[3][0], miss_rows[3][1], miss_rows[3][2],
                    'const absent = Q.join(nothing, "skills");')
    rc, lines, grounded, _ = world(blob, syn_semantics(miss_rows), honest_roots, ctx)
    check("A1.4/quote-miss: refuses its row", rc == 1 and grounded == TOTAL - 1,
          f"rc={rc} grounded={grounded}")
    ok, why, _, _ = reader_grounded(blob, 'return Xr.join(u.cwd, ".codex");',
                                    '{cwd}/.codex/skills',
                                    dict(ctx, binding_sets={'{cwd}/.codex/skills': ()}),
                                    header_table(blob), [])
    check("A1.4/empty-binding: an empty set is refused", not ok and "empty" in why, why)
    gen_ctx = dict(ctx, binding_sets={'{cwd}/.codex/skills': ("cwd",)})
    ok, why, _, _ = reader_grounded(blob, 'return Xr.join(u.cwd, ".codex");',
                                    '{cwd}/.codex/skills', gen_ctx,
                                    header_table(blob), [])
    check("A1.4/generic-token: `cwd` may never bind (C1-S3's door)",
          not ok and "GENERIC_TOKENS" in why, why)
    shifted_pins = dict(ctx["token_pins"])
    shifted_pins['{cwd}/.claude/skills'] = shifted_pins['{cwd}/.claude/skills'] + 2
    rc, lines, grounded, _ = world(blob, honest_sem, honest_roots,
                                   dict(ctx, token_pins=shifted_pins))
    check("A2.1/shifted-token-pin: refuses its row", rc == 1 and grounded == TOTAL - 1,
          f"rc={rc} grounded={grounded}")
    check("A2.1/shifted-token-pin: the failure names the pin re-find",
          any("does not re-find byte-exactly" in l for l in lines))
    wrong_chunk = dict(ctx["module_offsets"])
    wrong_chunk['{cwd}/.claude/skills'] = wrong_chunk['{cwd}/.codex/skills']
    rc, lines, grounded, _ = world(blob, honest_sem, honest_roots,
                                   dict(ctx, module_offsets=wrong_chunk))
    check("A2.1/wrong-chunk-token: zero in-chunk occurrences refuses its row",
          rc == 1 and grounded == TOTAL - 1, f"rc={rc} grounded={grounded}")

    # ---- A1.2/ conjunct-3 arms ----------------------------------------------------------
    nomod_rows = list(HONEST_ROWS)
    nomod_rows[8] = (nomod_rows[8][0], nomod_rows[8][1],
                     'coding-agent/src/discovery/nonexistent.ts', nomod_rows[8][3])
    rc, lines, grounded, _ = world(blob, syn_semantics(nomod_rows), honest_roots, ctx)
    check("A1.2/missing-header: refuses its row", rc == 1 and grounded == TOTAL - 1,
          f"rc={rc} grounded={grounded}")
    check("A1.2/missing-header: the failure names the nearest header",
          any("nearest preceding header" in l for l in lines))
    blob_order = syn_elf(order_swap='coding-agent/src/autolearn/managed-skills.ts')
    rc, lines, grounded, _ = world(blob_order, syn_semantics(), honest_roots,
                                   syn_ctx(blob_order))
    check("A1.2/header-after-reader: refuses its row", rc == 1 and grounded == TOTAL - 1,
          f"rc={rc} grounded={grounded}")

    # ---- conj4/ live bound arms ---------------------------------------------------------
    check("conj4/frozen-chain: strictly below $HOME",
          FROZEN_CHAIN == ("/home/u/proj/sub", "/home/u/proj"), str(FROZEN_CHAIN))
    check("conj4/repoRoot-arms: unset == $HOME == below-$HOME walk set",
          stop_chain(None) == stop_chain("/home/u") == stop_chain("/home/u/proj")
          == FROZEN_CHAIN)
    home_chain = stop_chain("/home")
    check("conj4/repoRoot-/home: walks ABOVE $HOME (the must-fail arm)",
          "/home" in home_chain and at_or_above("/home"), str(home_chain))
    check("conj4/repoRoot-/home: the /home candidate is refused by the frozen bound",
          "/home/.agent/skills" not in expansions("{cwd}/.agent/skills", FROZEN_CHAIN)
          and not matches_row("{cwd}/.agent/skills", "/home/.agent/skills", FROZEN_CHAIN)
          and "/home/.agent/skills" in expansions("{cwd}/.agent/skills", home_chain))
    check("conj4/home-itself: a candidate at $HOME is refused by the frozen bound",
          "/home/u/.agent/skills" not in expansions("{cwd}/.agent/skills", FROZEN_CHAIN)
          and not matches_row("{cwd}/.agent/skills", "/home/u/.agent/skills", FROZEN_CHAIN)
          and at_or_above("/home/u"))
    check("conj4/tilde: `~/` rows expand only inside $HOME",
          expansions("~/.agent/skills", FROZEN_CHAIN) == ["/home/u/.agent/skills"]
          and all(c == FROZEN_HOME or c.startswith(FROZEN_HOME + "/")
                  for c in expansions("~/x/y", FROZEN_CHAIN)))
    check("conj4/dotdot-probes: `..` candidates never match any honest row",
          all(not matches_row(r[0], probe, FROZEN_CHAIN)
              for r in HONEST_ROWS for probe in AT_HOME_PROBES))
    blob_nowalker = syn_elf(with_walker=False)
    rc, lines, grounded, _ = world(blob_nowalker, syn_semantics(), honest_roots,
                                   syn_ctx(blob_nowalker))
    walker_failures = sum(1 for l in lines if " FAIL " in l
                          and ("{cwd}/.agent/skills" in l or "{cwd}/.agents/skills" in l))
    check("conj4/ungrounded-walker: refuses the walker rows",
          rc == 1 and grounded == TOTAL - 2 and walker_failures == 2,
          f"rc={rc} grounded={grounded}")
    check("conj4/ungrounded-walker: the failure names the bound",
          any("walker bound ungrounded" in l for l in lines))
    blob_wrongchunk = syn_elf(walker_in_chunk=False)
    rc, lines, grounded, _ = world(blob_wrongchunk, syn_semantics(), honest_roots,
                                   syn_ctx(blob_wrongchunk))
    check("conj4/wrong-chunk-walker: refuses the walker rows",
          rc == 1 and grounded == TOTAL - 2, f"rc={rc} grounded={grounded}")
    check("conj4/walker-accepts: the honest chunk grounds the loop",
          walker_grounded(blob, WALKER_MODULE, header_table(blob)) == (True, ""))

    # ---- A1.4/ conjunct-1 arms ----------------------------------------------------------
    dot_rows = list(HONEST_ROWS)
    dot_rows[0] = ("{cwd}/../.omp/skills", dot_rows[0][1], dot_rows[0][2], dot_rows[0][3])
    dot_roots = apply_roots_pattern_world(honest_roots, {1: "{cwd}/../.omp/skills"})
    rc, lines, grounded, _ = world(blob, syn_semantics(dot_rows), dot_roots, ctx)
    check("conj1/dotdot: refuses its row", rc == 1 and grounded == TOTAL - 1,
          f"rc={rc} grounded={grounded}")
    check("conj1/dotdot: names the `..` segment", any("`..` segment" in l for l in lines))
    star_rows = list(HONEST_ROWS)
    star_rows[0] = ("*/skills", star_rows[0][1], star_rows[0][2], star_rows[0][3])
    star_roots = apply_roots_pattern_world(honest_roots, {1: "*/skills"})
    rc, lines, grounded, _ = world(blob, syn_semantics(star_rows), star_roots, ctx)
    check("conj1/wildcard: refuses its row", rc == 1 and grounded == TOTAL - 1,
          f"rc={rc} grounded={grounded}")
    check("conj1/wildcard: names the wildcard first segment",
          any("wildcard in its first segment" in l for l in lines))

    # ---- conj5/ binary-quote arm --------------------------------------------------------
    nobin_rows = list(HONEST_ROWS)
    nobin_rows[11] = (nobin_rows[11][0], 'This binary quote is not in the synthetic ELF',
                      nobin_rows[11][2], nobin_rows[11][3])
    rc, lines, grounded, _ = world(blob, syn_semantics(nobin_rows), honest_roots, ctx)
    check("conj5/binary-miss: refuses its row", rc == 1 and grounded == TOTAL - 1,
          f"rc={rc} grounded={grounded}")
    check("conj5/binary-miss: names the binary miss",
          any("binary_quote not located" in l for l in lines))

    # The conjunct must also hold on the real read-only mmap, not only on bytes: an mmap
    # has no substring `in` operator, so the membership form silently fails (round-88 bug).
    import os
    import tempfile
    fd, tmp_name = tempfile.mkstemp(prefix="ors2-", suffix=".elf")
    try:
        os.write(fd, blob)
        os.close(fd)
        with open(tmp_name, "rb") as handle:
            mapped = mmap.mmap(handle.fileno(), 0, access=mmap.ACCESS_READ)
            try:
                check("conj5/mmap: a planted binary_quote is located on the mmap",
                      binary_grounded(mapped, "Native OMP configuration from ~/.omp and .omp/")[0],
                      "mmap substring search failed")
                check("conj5/mmap: an absent binary_quote is refused on the mmap",
                      not binary_grounded(mapped, "no such quote in the synthetic elf")[0])
            finally:
                mapped.close()
    finally:
        try:
            os.unlink(tmp_name)
        except OSError:
            pass

    # ---- guards/ arms -------------------------------------------------------------------
    rc, lines, grounded, guards = world(blob, None, honest_roots, ctx)
    check("guards/no-ledger: reads 0 of 12 and exits 1", rc == 1 and grounded == 0,
          f"rc={rc} grounded={grounded}")
    rc, lines, grounded, guards = world(blob, syn_semantics(HONEST_ROWS[:11]),
                                        honest_roots, ctx)
    check("guards/shrink: cannot pass (S3 FAIL, N short)",
          rc == 1 and grounded == 11 and guards["S3"] is False,
          f"rc={rc} grounded={grounded}")
    try:
        if pin_digest(blob) != "0" * 64:
            raise Inconclusive("digest differs from the wrong pin")
        raise Inconclusive("digest collision")
    except Inconclusive:
        check("guards/wrong-pin: raises could-not-evaluate", True)

    # ---- K-line/: the three disclosed classes join the four M classes -------------------
    k_rejected, _ = k_world_verdicts(rows_pairs, honest_roots, blob, ctx, lambda *_: None)
    check("K-line: all three disclosed K classes rejected on the synthetic ELF",
          k_rejected == 3, f"K={k_rejected}")

    # ---- config/S4: the frozen floor, asserted against the FULL arm list ---------------
    if floor is None:
        print(f"note: floors row {INSTRUMENT_KEY} absent from {FLOORS_REGISTRY} (worktree); "
              f"the --rev S4 guard enforces it once the row lands")
    else:
        check(f"config/S4: assertion count {assertions} >= frozen floor {floor} "
              f"({floor_source})", assertions >= floor, f"count {assertions}")

    print(f"{len(failures)} failure(s) over {assertions} assertions")
    print(f"forgery-class worlds rejected {k_rejected + len(FORGED_WORLDS)} of {K_TOTAL}")
    for failure in failures:
        print("FAIL", failure)
    return 0 if not failures else 1


# ----------------------------------------------------------------------------------- run

def run(repo: Path, rev: str, out=print) -> int:
    semantics = git_show(repo, rev, SEMANTICS_LEDGER)
    roots = git_show(repo, rev, ROOTS_LEDGER)
    anchor_text = git_show(repo, PATTERN_PIN_REV, ROOTS_LEDGER)
    if anchor_text is None:
        raise Inconclusive(f"the round-86 anchor {ROOTS_LEDGER} is absent at the frozen "
                           f"pin {PATTERN_PIN_REV}")
    anchor_rows, anchor_err = roots_rows(anchor_text)
    if anchor_rows is None:
        raise Inconclusive(f"the pin {PATTERN_PIN_REV} anchor is unreadable: {anchor_err}")
    ctx = {"anchor_patterns": ledger_patterns(anchor_rows),
           "reader_pins": READER_OFFSETS, "token_pins": TOKEN_PINS,
           "module_offsets": MODULE_OFFSETS}
    blob, digest = open_elf(OMP_BINARY, OMP_SHA256)
    try:
        out(f"rev {rev} elf {OMP_BINARY} sha256 {digest} pin {PATTERN_PIN_REV}")
        out(f"addenda A1.1-A1.6 + A2.1/A2.2; ELF_MAP digest {ELF_MAP_SHA256}; upstream "
            f"{WALKER_BOUND_UPSTREAM}")
        out(f"probe cwd={FROZEN_CWD} HOME={FROZEN_HOME} repoRoot=unset "
            f"walk={','.join(FROZEN_CHAIN)} (strictly below $HOME)")
        out(f"frozen tables: binding sets sha256 {BINDING_BLOCK_SHA256}; token pins sha256 "
            f"{TOKEN_PIN_BLOCK_SHA256}; reader pins sha256 {READER_OFFSET_BLOCK_SHA256}; "
            f"module offsets sha256 {MODULE_OFFSET_BLOCK_SHA256}; PATTERN_SET sha256 "
            f"{PATTERN_SET_SHA256}")
        out(f"guard S1 ledger-from-rev PASS (git show {rev}:{SEMANTICS_LEDGER} "
            f"rc={'0' if semantics is not None else 'absent'}, "
            f"git show {rev}:{ROOTS_LEDGER} rc={'0' if roots is not None else 'absent'}, "
            f"git show {PATTERN_PIN_REV}:{ROOTS_LEDGER} rc=0) pin {PATTERN_PIN_REV}")
        out(f"guard S2 elf-sha256 PASS ({digest})")
        out(f"guard S5 elf-readonly-mmap PASS (mmap.ACCESS_READ; the ELF is never exec'd; "
            f"no network imports)")
        grounded, guards, rows = score(semantics, roots, blob, out, ctx)

        parsed, _ = parse_ledger(semantics, SEMANTICS_HEADER) if semantics else (None, None)
        if parsed is None:
            rejected = 0
            out("forgeries: the honest ledger is unreadable at the revision; M = 0")
        else:
            rejected, _ = forged_verdicts(parsed, roots, blob, ctx, out)
        k_rejected, _ = k_world_verdicts(parsed, roots, blob, ctx, out) \
            if parsed is not None else (0, [])

        try:
            import io
            from contextlib import redirect_stdout
            buffer = io.StringIO()
            with redirect_stdout(buffer):
                rc_st = self_test(None)
            printed = buffer.getvalue().strip().splitlines()
            count_line = next((l for l in printed if "failure(s) over" in l), "")
            floor, floor_source = floor_from_registry()
            s4_detail = ""
            s4_ok = False
            if rc_st != 0:
                s4_detail = f"self-test rc={rc_st}"
            elif not count_line:
                s4_detail = "self-test printed no count line"
            else:
                count = int(count_line.split(" over ")[1].split(" ")[0])
                if floor is None:
                    s4_detail = (f"floors row {INSTRUMENT_KEY} absent ({floor_source}); "
                                 f"count {count}")
                elif count < floor:
                    s4_detail = f"count {count} < floor {floor}"
                else:
                    s4_ok = True
                    s4_detail = (f"{count_line} >= floor {floor} ({FLOORS_REGISTRY} "
                                 f"source={floor_source})")
        except Inconclusive as exc:
            s4_ok, s4_detail = False, f"self-test could-not-evaluate: {exc}"
        guards["S4"] = bool(s4_ok)
        out(f"guard S3 pattern-set {'PASS' if guards['S3'] else 'FAIL'} "
            f"(pin {PATTERN_PIN_REV} anchor + PATTERN_SET {PATTERN_SET_SHA256})")
        out(f"guard S4 self-test-floor {'PASS' if guards['S4'] else 'FAIL'} ({s4_detail})")
        out(f"omp root semantics grounded {grounded} of {TOTAL}")
        out(f"forgeries rejected {rejected} of {FORGED_TOTAL}")
        out(f"forgery-class worlds rejected {rejected + k_rejected} of {K_TOTAL}")
        ok = (grounded == TOTAL and rejected == FORGED_TOTAL
              and all(guards[key] for key in ("S1", "S2", "S3", "S4", "S5")))
        out(f"exit={0 if ok else 1}")
        return 0 if ok else 1
    finally:
        blob.close()


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    parser.add_argument("--rev", help="commit whose committed ledgers are scored")
    parser.add_argument("--repo", default=str(REPO))
    parser.add_argument("--work", help="scratch dir honoured by --self-test (in-memory arms)")
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args(argv)
    if args.self_test:
        return self_test(Path(args.work) if args.work else None)
    if not args.rev:
        parser.error("--rev is required")
    try:
        return run(Path(args.repo), args.rev)
    except Inconclusive as exc:
        print(f"could-not-evaluate: {exc}")
        return 2


if __name__ == "__main__":
    sys.exit(main())
