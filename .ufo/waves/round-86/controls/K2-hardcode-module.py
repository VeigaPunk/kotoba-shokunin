#!/usr/bin/env python3
"""Executable verifier for kotoba's harness claim set.

Recomputes, from live host state, the facts that `SKILL.md` § Router model and
`corpus/knowledge/harness-router-models-round9.md` assert about the two skill
routers (omp and opencode). Everything here previously lived as a hand-run
recipe; a recipe re-run by a human is lane-attested, a script that exits
non-zero is not.

Authority for every mechanism below is the shipped source, read from the
binaries themselves (both harnesses are single-file executables with embedded
readable JS — no disassembly needed):

  omp      `~/.local/bin/omp`        functions A8n (cache key), H7s (truncator),
                                     ldl (compressor acceptance), nV.render
                                     (cache-or-truncate), module comment
                                     `// packages/coding-agent/src/extensibility/
                                     skill-descriptions.ts`
  opencode `~/.npm/_npx/e2094862b59aac7b/node_modules/opencode-ai/bin/opencode.exe`
                                     (npm opencode-ai, round 47) string `available_skills`,
                                     `EmbeddedSource.make({skill:…})`

Usage:
    python3 verifiers/verify_harness_claims.py            # verify vs baseline
    python3 verifiers/verify_harness_claims.py --json     # machine-readable
    python3 verifiers/verify_harness_claims.py --self-test  # model self-check
    python3 verifiers/verify_harness_claims.py --no-baseline # observe only

Exit codes: 0 all checks agree with the baseline; 1 drift; 2 the environment is
unreadable (missing binary / db / log); 3 no baseline found (observations
printed).

Baseline update is deliberate: after a legitimate change (new skill, edited
description, new harness build) re-run with --json, confirm each moved value is
explained by the change, then write the new values into
`verifiers/baseline.json` and append a LOG.md entry citing this script.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import sqlite3
import subprocess
from datetime import datetime
import sys
from pathlib import Path

HOME = Path.home()
OMP_BIN = HOME / ".local/bin/omp"  # round 85: this host's omp is the ELF itself (omp/18.15.0); omp.real does not exist
OMP_DB = HOME / ".omp/agent/skill-descriptions.db"
OC_LOG = HOME / ".local/share/opencode/log/opencode.log"
OC_BIN = HOME / ".opencode/bin/opencode"  # round 72: v2.1.4
OMP_SESSIONS = HOME / ".omp/agent/sessions"
BASELINE = Path(__file__).resolve().parent / "baseline.json"

# omp discovery roots in loader order: project walk-up (cwd upward) first, then
# user roots. Verified 2026-09-28 against the 17-name catalogue in this host's
# `<skills>` render.
USER_ROOTS = [
    HOME / ".agents/skills",
    HOME / ".omp/agent/skills",
    HOME / ".config/opencode/skills",
    HOME / ".claude/skills",
]
WALKUP_REL = [".agents/skills", ".agent/skills"]

# omp render constants, read from the shipped source (`var _8n=100, idl=160,
# adl=12`; `A8n`/`H7s`/`ldl`). Anchored on semantics, not ELF offsets.
CLIFF = 100
COMPRESSED_MAX_CHARS = 160
COMPRESSED_MAX_WORDS = 12
ELLIPSIS = "\u2026"

TEMPLATE_ANCHOR = b"Compress into one routing hint"
TEMPLATE_MUST_CONTAIN = (b"{{name}}", b"{{description}}")


# --------------------------------------------------------------------------
# omp: template, frontmatter, key, truncator
# --------------------------------------------------------------------------
def omp_template(binary: Path) -> bytes:
    """Recover the keyed compression prompt from the omp ELF.

    The prompt is embedded NUL-terminated as the content of the bunfs file
    `/root/compress-description-<hash>.md`. `A8n` hashes this byte string
    verbatim (placeholders included), so it is the key prefix. Structural
    validation replaces a hardcoded length/offset: the candidate must contain
    both placeholders, and the anchor must be unique.
    """
    blob = binary.read_bytes()
    hits = [m.start() for m in re.finditer(re.escape(TEMPLATE_ANCHOR), blob)]
    if len(hits) != 1:
        raise Inconclusive(f"template anchor occurs {len(hits)}x in {binary} (want 1)")
    start = hits[0]
    end = blob.find(b"\x00", start)
    if end < 0:
        raise Inconclusive("template is not NUL-terminated")
    tmpl = blob[start:end]
    for needle in TEMPLATE_MUST_CONTAIN:
        if needle not in tmpl:
            raise Inconclusive(f"template candidate lacks {needle!r} — build changed shape")
    return tmpl


def parse_frontmatter(text: str) -> dict:
    """Minimal YAML frontmatter reader for the `name` and `description` keys.

    Only the scalar forms seen in real SKILL.md files are supported; the loader
    semantics that matter for the cache key are the block-scalar chomping
    indicators (round-9 evidence: `>`/`|` keep one trailing newline, `>-`/`|-`
    do not). Returns {"name": str|None, "description": str|None, "style": str}.
    """
    m = re.match(r"^---\r?\n(.*?)\r?\n---\r?\n", text, re.S)
    if not m:
        return {"name": None, "description": None, "style": "no-frontmatter"}
    lines = m.group(1).split("\n")
    out = {"name": None, "description": None, "style": None}
    unmodelled = False
    for i, raw in enumerate(lines):
        if raw.startswith("name:"):
            out["name"] = raw[len("name:"):].strip().strip('"').strip("'")
        elif raw.startswith("description:"):
            rest = raw[len("description:"):]
            head = rest.lstrip()
            if head[:1] in ("|", ">") and head[1:2].isdigit():
                unmodelled = True  # explicit indentation indicator
            if head[:1] in ("&", "*", "[", "{"):
                unmodelled = True  # anchor / alias / flow collection
            if head[:1] in ("|", ">"):
                style = head[0] + ("-" if head[1:2] == "-" else "+" if head[1:2] == "+" else "")
                indent = None
                body: list[str] = []
                for ln in lines[i + 1:]:
                    if ln.strip() == "":
                        body.append("")
                        continue
                    cur = len(ln) - len(ln.lstrip(" "))
                    if indent is None:
                        indent = cur
                    if cur < indent:
                        break
                    body.append(ln[indent:])
                if not style.endswith("+"):
                    while body and body[-1] == "":
                        body.pop()
                if style[0] == ">":
                    folded: list[str] = []
                    for ln in body:
                        if ln == "":
                            folded.append("\n")
                        else:
                            folded.append((" " if folded and not folded[-1].endswith("\n") else "") + ln)
                    value = "".join(folded)
                else:
                    value = "\n".join(body)
                if style.endswith("+"):
                    value += "\n" * max(0, _trailing_blanks(lines, i))
                elif not style.endswith("-"):
                    value += "\n"
                out["description"] = value
                out["style"] = style
            else:
                # Plain / quoted scalar. YAML: a plain value ends at ` #`,
                # folds indented continuation lines with a space (a blank line
                # in the middle becomes a newline), and trailing space is
                # trimmed; escapes apply inside double quotes only.
                if head[:1] == '"' and head.count('"') >= 2:
                    value, style = _unquote_double(head), "quoted"
                elif head[:1] == "'" and head.count("'") >= 2:
                    body = head[1:head.rindex("'")]
                    value, style = body.replace("''", "'"), "quoted"
                elif head[:1] in ('"', "'"):
                    value, style = head, "unmodelled"  # multi-line quoted scalar
                else:
                    parts = [re.sub(r"\s+#.*$", "", head).rstrip()]
                    for ln in _plain_continuation(lines, i):
                        parts.append("\n" if ln.strip() == "" else " " + re.sub(r"\s+#.*$", "", ln.strip()).rstrip())
                    value = "".join(parts).rstrip() if len(parts) > 1 else parts[0]
                    style = "plain"
                out["description"] = value
                out["style"] = "unmodelled" if unmodelled else style
            break
    if unmodelled:
        out["style"] = "unmodelled"
    return out


def _trailing_blanks(lines: list[str], start: int) -> int:
    """Count trailing blank lines in a block scalar (for `+` chomping)."""
    n = 0
    for ln in lines[start + 1:]:
        if ln.strip() == "":
            n += 1
        else:
            n = 0
    return n


def _plain_continuation(lines: list[str], start: int) -> list[str]:
    """Indented continuation lines of a plain scalar (indent > 0)."""
    out: list[str] = []
    for ln in lines[start + 1:]:
        if ln.strip() == "":
            out.append("")
            continue
        if ln[:1] in (" ", "\t"):
            out.append(ln)
        else:
            break
    while out and out[-1] == "":
        out.pop()
    return out


def _unquote_double(value: str) -> str:
    """Decode the YAML double-quoted escapes this host's files could carry."""
    body = value[1:value.rindex('"')] if value.count('"') >= 2 else value[1:]
    return re.sub(r"\\(.)", lambda m: {"n": "\n", "t": "\t", "\\": "\\", '"': '"'}.get(m.group(1), m.group(1)), body)


def omp_key(template: bytes, name: str, description: str) -> str:
    """`A8n`: sha256(template ‖ 0x00 ‖ name ‖ 0x00 ‖ description).  [source-read]"""
    h = hashlib.sha256()
    h.update(template)
    h.update(b"\x00")
    h.update(name.encode())
    h.update(b"\x00")
    h.update(description.encode())
    return h.hexdigest()


def preview(description: str) -> str:
    """`H7s` — previewSkillDescription: ws-collapse, cliff at 100, sentence
    back-off (>=40 chars, no ellipsis) else last-space cut + U+2026. [source-read]"""
    t = re.sub(r"\s+", " ", description).strip()
    if len(t) <= CLIFF:
        return t
    s = t[: CLIFF - 1]
    m = re.match(r"^.*?[.!?](?=\s|$)", s)
    if m and len(m.group(0)) >= 40:
        return m.group(0)
    n = s[: s.rfind(" ")].rstrip()
    return (n or s) + ELLIPSIS


def compressor_accepts(description: str) -> bool:
    """`ldl` — single line, <=160 chars, <=12 words. [source-read]"""
    t = description.strip()
    if not t or re.search(r"[\r\n]", t) or len(t) > COMPRESSED_MAX_CHARS:
        return False
    return len(t.split()) <= COMPRESSED_MAX_WORDS


def discover_skills(roots: list[Path]) -> tuple[dict[str, Path], dict[str, str]]:
    """First root wins per name (omp resolves duplicates by root order).

    Returns (offered, dangling) — dangling symlink entries are reported, never
    silently dropped: they are the failure mode that silently shrinks a
    catalogue.
    """
    offered: dict[str, Path] = {}
    dangling: dict[str, str] = {}
    for root in roots:
        if not root.is_dir():
            continue
        for entry in sorted(root.iterdir()):
            skill = entry / "SKILL.md"
            if entry.is_symlink() and not entry.exists():
                dangling[entry.name] = f"{entry} -> {os.readlink(entry)}"
                continue
            if skill.is_file():
                offered.setdefault(entry.name, skill)
    return offered, dangling


def omp_observations(binary: Path, db: Path, cwd: Path, sessions: Path = OMP_SESSIONS) -> dict:
    if not binary.is_file():
        raise Inconclusive(f"omp binary not found: {binary}")
    if not db.is_file():
        raise Inconclusive(f"omp skill-description cache not found: {db}")
    template = omp_template(binary)
    con = sqlite3.connect(f"file:{db}?mode=ro", uri=True)
    rows = {k: d for k, d in con.execute("select key, description from skill_descriptions")}
    con.close()

    roots = [cwd / rel for rel in WALKUP_REL] + USER_ROOTS
    offered, dangling = discover_skills(roots)

    per_skill = []
    reproduced = truncating = accepted = 0
    unmodelled: list[str] = []
    for name, path in sorted(offered.items()):
        fm = parse_frontmatter(path.read_text())
        desc = fm["description"]
        if fm["style"] == "unmodelled":
            # A scalar form this reader does not model is excluded from the
            # pass/fail set and named — a guessed key would be a false DRIFT.
            unmodelled.append(name)
            per_skill.append({"name": name, "status": "unmodelled", "style": fm["style"],
                              "cache": "unverified"})
            continue
        if desc is None:
            per_skill.append({"name": name, "style": fm["style"], "status": "no-description",
                              "cache": "not-offered"})
            continue
        hit = omp_key(template, name, desc) in rows
        render = desc if hit else preview(desc)
        if hit:
            reproduced += 1
        else:
            truncating += 1
        if compressor_accepts(rows.get(omp_key(template, name, desc), desc)):
            accepted += 1
        per_skill.append({
            "name": name,
            "status": "offered",
            "style": fm["style"],
            "declared_name": fm["name"],
            "name_matches_folder": fm["name"] == name,
            "description_chars": len(re.sub(r"\s+", " ", desc).strip()),
            "source_description": desc,
            "cache": "hit" if hit else "miss",
            "rendered_chars": len(render),
            "rendered": render if not hit else None,
        })

    cached_by_name = {
        entry["name"]: rows[omp_key(template, entry["name"], entry["source_description"])]
        for entry in per_skill
        if entry.get("cache") == "hit"
    }
    catalogue = omp_newest_catalogue(sessions, cached_by_name, set(offered))
    return {
        **catalogue,
        "template_sha256": hashlib.sha256(template).hexdigest(),
        "template_bytes": len(template),
        "db_rows": len(rows),
        "db_rows_wellformed": sum(1 for d in rows.values() if compressor_accepts(d)),
        "offered_skills": len(offered),
        "dangling_entries": dangling,
        "dangling_count": len(dangling),
        "keys_reproduced": reproduced,
        "cache_misses": truncating,
        "descriptions_over_cliff": sum(1 for s in per_skill if s.get("description_chars", 0) > CLIFF),
        "name_mismatches": [s["name"] for s in per_skill if s.get("name_matches_folder") is False],
        "no_description": [s["name"] for s in per_skill if s["status"] == "no-description"],
        "unmodelled_styles": unmodelled,
        "unmodelled_count": len(unmodelled),
        "verified_skills": len(offered) - len(unmodelled) - sum(1 for s in per_skill if s["status"] == "no-description"),
        "per_skill": per_skill,
    }


def _strings(obj):
    """Every string inside a decoded jsonl record (dict/list/str nesting)."""
    if isinstance(obj, str):
        yield obj
    elif isinstance(obj, dict):
        for value in obj.values():
            yield from _strings(value)
    elif isinstance(obj, list):
        for value in obj:
            yield from _strings(value)


def omp_newest_catalogue(sessions: Path, db_descriptions: dict[str, str], known: set[str]) -> dict:
    """Newest captured `<skills>` block, matched line-by-line against the cache.

    This is the only check that ties the *keys* to what a model actually saw:
    the catalogue freezes at session start and the render is
    `cache.get(key) ?? previewSkillDescription`, so every line of the newest
    block must byte-equal a cached description. Guards: a block counts only if
    it parses into ≥`min_entries` `- name: description` lines and ≥`min_entries`
    of the names are known skills, where `min_entries` is `min(10, len(known))`
    — the floor tracks the offer set (a 7-skill catalogue is real when 7 skills
    are offered), while raw `<skills>` literals stay contaminated by captured
    transcript/tool text (round-10 sentinel: 8194 literals vs 4116 catalogues).
    """
    if not sessions.is_dir():
        raise Inconclusive(f"omp session log dir not found: {sessions}")
    block_re = re.compile(r"<skills>(.*?)</skills>", re.S)
    iso_re = re.compile(r"20\d\d-\d\d-\d\dT\d\d:\d\d:\d\d(?:\.\d+)?Z")
    min_entries = min(10, len(known))
    best_epoch = -1.0
    best: tuple[str, str, list[tuple[str, str]]] | None = None
    files = 0
    for dirpath, _dirs, names in os.walk(sessions):
        for fn in names:
            if not fn.endswith(".jsonl"):
                continue
            files += 1
            path = Path(dirpath) / fn
            try:
                with path.open(encoding="utf-8", errors="replace") as fh:
                    for line in fh:
                        if "<skills>" not in line or "</skills>" not in line:
                            continue
                        # Session jsonl stores the prompt inside JSON, so quotes
                        # and newlines arrive escaped; decode before matching or
                        # a description containing `"` (wwkd) reads as a miss.
                        try:
                            texts = _strings(json.loads(line))
                        except ValueError:
                            texts = [line.replace('\\n', '\n').replace('\\"', '"')]
                        for text in texts:
                            for block in block_re.finditer(text):
                                entries = [
                                    tuple(z[2:].split(": ", 1))
                                    for z in block.group(1).splitlines()
                                    if z.startswith("- ") and ": " in z[2:]
                                ]
                                if len(entries) < min_entries or \
                                        sum(n in known for n, _ in entries) < min_entries:
                                    continue
                                hit = iso_re.search(line)
                                if hit:
                                    epoch = datetime.fromisoformat(
                                        hit.group().replace("Z", "+00:00")).timestamp()
                                    stamp = hit.group()
                                else:
                                    epoch = path.stat().st_mtime
                                    stamp = datetime.fromtimestamp(epoch).astimezone().isoformat()
                                if epoch > best_epoch:
                                    best_epoch, best = epoch, (stamp, str(path), entries)
            except OSError:
                continue
    if best is None:
        return {"catalogue_total": 0, "catalogue_matched": 0, "catalogue_missing_names": [],
                "catalogue_found": False, "session_files_scanned": files}
    stamp, path_str, entries = best
    matched = [n for n, d in entries if db_descriptions.get(n) == d]
    missing = [n for n, d in entries if db_descriptions.get(n) != d]
    return {
        "catalogue_total": len(entries),
        "catalogue_matched": len(matched),
        "catalogue_missing_names": missing,
        "catalogue_timestamp": stamp,
        "catalogue_path": path_str,
        "catalogue_found": True,
        "session_files_scanned": files,
    }


# --------------------------------------------------------------------------
# opencode: counters a verifier can pin
# --------------------------------------------------------------------------
def _root_key(path: str) -> str:
    """`/home/vgpnk/.claude/skills/x/SKILL.md` -> `.claude/skills`."""
    parts = path.split(str(HOME) + "/")
    return "/".join(parts[1].split("/")[:2]) if len(parts) > 1 else path


def oc_observations(log: Path, binary: Path) -> dict:
    if not log.is_file():
        raise Inconclusive(f"opencode log not found: {log}")
    text = log.read_text(errors="replace")
    init_counts = [int(n) for n in re.findall(r"message=init count=(\d+)", text)]
    dup_lines = re.findall(r"duplicate skill name.*", text)
    perm_lines = re.findall(r"evaluated permission=skill.*", text)
    # opencode 2.x (the log grammar after the 2.0.x rewrite): the skill loader
    # logs `message="skills rescanned" … skills="[\"a\",\"b\"]"` per rescan
    # event. The max name count is the live-era analogue of `init count`.
    rescan_counts = [
        m.group(1).count('\\"') // 2
        for m in re.finditer(r'message="skills rescanned"[^\n]*skills="\[([^\]]*)\]"', text)
    ]

    roots = [HOME / ".agents/skills", HOME / ".config/opencode/skills", HOME / ".claude/skills"]
    names: set[str] = set()
    for root in roots:
        if root.is_dir():
            names |= {e.name for e in root.iterdir() if (e / "SKILL.md").exists()}
    builtin = 0
    if binary.is_file():
        builtin = 1 if b"customize-opencode" in binary.read_bytes() else 0

    split: dict[str, dict[str, int]] = {}
    for line in dup_lines:
        ex = re.search(r"existing=(\S+)", line)
        du = re.search(r"duplicate=(\S+)", line)
        for side, m in (("existing", ex), ("duplicate", du)):
            if m:
                bucket = split.setdefault(_root_key(m.group(1)), {"existing": 0, "duplicate": 0})
                bucket[side] += 1
    onesided = sorted(r for r, c in split.items() if not (c["existing"] > 0 and c["duplicate"] > 0))
    monotone_violations = [
        f"{init_counts[i - 1]}->{init_counts[i]}"
        for i in range(1, len(init_counts))
        if init_counts[i] < init_counts[i - 1]
    ]

    return {
        "init_count_max": max(init_counts) if init_counts else 0,
        "skills_rescan_max": max(rescan_counts) if rescan_counts else 0,
        "skills_rescan_lines": len(rescan_counts),
        "init_count_lines": len(init_counts),
        "init_count_monotone_violations": monotone_violations,
        "root_live_names": len(names),
        "builtin_names": builtin,
        "roots_plus_builtin": len(names) + builtin,
        "available_skills_hits": text.count("<available_skills>"),
        "skills_tag_hits": text.count("<skills>"),
        "dup_roots": split,
        "dup_roots_both_sided": len(split) - len(onesided),
        "dup_onesided_roots": onesided,
        "permission_skill_lines": len(perm_lines),
        "permission_skill_allow": sum(1 for l in perm_lines if "action.action=allow" in l),
        "plugins_cache_present": (HOME / ".claude/plugins/cache").exists(),
    }


# --------------------------------------------------------------------------
# check layer
# --------------------------------------------------------------------------
class Inconclusive(Exception):
    """Environment cannot answer the question (exit 2)."""


# id -> (mode, extractor). mode: equal | zero | positive | at_least
CHECKS: dict[str, tuple[str, str]] = {
    "omp.elf.template_sha256": ("equal", "template_sha256"),
    "omp.elf.template_bytes": ("equal", "template_bytes"),
    "omp.db.rows": ("equal", "db_rows"),
    "omp.db.rows_wellformed": ("equal", "db_rows_wellformed"),
    "omp.offered.skills": ("equal", "offered_skills"),
    "omp.offered.dangling": ("equal", "dangling_count"),
    "omp.cache.keys_reproduced": ("equal", "keys_reproduced"),
    "omp.cache.misses": ("zero", "cache_misses"),
    "omp.descriptions.over_cliff": ("positive", "descriptions_over_cliff"),
    "omp.names.mismatches": ("zero", "name_mismatches"),
    "omp.descriptions.missing": ("zero", "no_description"),
    "omp.descriptions.unmodelled": ("zero", "unmodelled_count"),
    "omp.catalogue.found": ("equal", "catalogue_found"),
    "omp.catalogue.total": ("equal", "catalogue_total"),
    "oc.log.skills_rescan_max": ("equal", "skills_rescan_max"),
    "omp.catalogue.matched": ("equal", "catalogue_matched"),
    "omp.catalogue.missing_names": ("zero", "catalogue_missing_names"),
    "omp.cache.verified_skills": ("equal", "verified_skills"),
    "oc.log.init_count_max": ("equal", "init_count_max"),
    "oc.roots.names_plus_builtin": ("equal", "roots_plus_builtin"),
    "oc.log.available_skills_hits": ("zero", "available_skills_hits"),
    "oc.log.skills_tag_hits": ("zero", "skills_tag_hits"),
    "oc.dup.roots_both_sided": ("equal", "dup_roots_both_sided"),
    "oc.dup.onesided_roots": ("zero", "dup_onesided_roots"),
    "oc.log.init_count_monotone": ("zero", "init_count_monotone_violations"),
    "oc.permission.skill_lines": ("equal", "permission_skill_lines"),
    "oc.permission.skill_allow": ("equal", "permission_skill_allow"),
    "oc.roots.plugins_cache": ("zero", "plugins_cache_present"),
}


def evaluate(observed: dict, baseline: dict | None) -> list[dict]:
    results = []
    for cid, (mode, key) in CHECKS.items():
        value = observed[key]
        row = {"check": cid, "mode": mode, "observed": value}
        if mode == "zero" and baseline is None:
            ok = (value == 0) or (isinstance(value, (dict, list)) and not value)
            row["expected"] = "0 / empty"
        elif mode == "positive" and baseline is None:
            ok = isinstance(value, int) and value > 0
            row["expected"] = "> 0"
        elif baseline is None:
            ok, row["expected"] = None, "baseline"
        else:
            want = baseline["checks"].get(cid, {}).get("expect")
            row["expected"] = want
            if mode == "zero" or mode == "equal":
                ok = value == want
            elif mode == "positive" or mode == "at_least":
                ok = isinstance(value, int) and isinstance(want, int) and value >= want
            else:
                ok = False
        row["verdict"] = "PASS" if ok else ("OBSERVE" if ok is None else "DRIFT")
        results.append(row)
    return results


def self_test() -> int:
    """Falsify this file's model of `H7s` and of block-scalar chomping.

    The vectors are derived from the shipped source quoted in the module
    docstring; a failure here means the script's model is wrong, not the host.
    """
    failures = []
    cases = [
        ("short", "a" * 99, "a" * 99),
        ("exactly-100", "b" * 100, "b" * 100),
        ("sentence-backoff", "c" * 50 + ". " + "d" * 100, "c" * 50 + "."),
        # first sentence is 21 chars (<40) → back off to the last space of the
        # 99-char slice, which is the one after the period
        ("sentence-too-short", "e" * 20 + ". " + "f" * 100, "e" * 20 + "." + ELLIPSIS),
        # no ASCII space in the slice → slice(0,-1), i.e. 98 chars
        ("no-sentence-last-space", "g" * 120, "g" * 98 + ELLIPSIS),
        ("cjk-no-ascii-period", "中" * 120, "中" * 98 + ELLIPSIS),
        ("ws-collapse", "  x   y \n z ", "x y z"),
    ]
    for label, given, want in cases:
        got = preview(given)
        if got != want:
            failures.append(f"preview[{label}]: got {got!r} want {want!r}")
    # chomping: clip keeps one newline, strip removes it, folding joins with space
    fm = parse_frontmatter("---\nname: x\ndescription: >\n  alpha\n  beta\n---\n")
    if fm["description"] != "alpha beta\n":
        failures.append(f"fold-clip: got {fm['description']!r}")
    fm = parse_frontmatter("---\nname: x\ndescription: |-\n  alpha\n  beta\n---\n")
    if fm["description"] != "alpha\nbeta":
        failures.append(f"literal-strip: got {fm['description']!r}")
    fm = parse_frontmatter("---\nname: x\ndescription: plain one\n---\n")
    if fm["description"] != "plain one":
        failures.append(f"plain: got {fm['description']!r}")
    for f in failures:
        print(f"FAIL {f}")
    print(f"self-test: {len(failures)} failure(s) over {len(cases) + 3} assertions")
    return 1 if failures else 0


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--json", action="store_true", help="emit observations + results as JSON")
    ap.add_argument("--self-test", action="store_true", help="check the script's model only")
    ap.add_argument("--no-baseline", action="store_true", help="observe without comparing")
    ap.add_argument("--baseline", type=Path, default=BASELINE)
    ap.add_argument("--cwd", type=Path, default=Path.cwd(), help="root of the project walk-up")
    ap.add_argument("--omp-bin", type=Path, default=OMP_BIN, help="override for fixture testing")
    ap.add_argument("--omp-db", type=Path, default=OMP_DB, help="override for fixture testing")
    ap.add_argument("--oc-log", type=Path, default=OC_LOG, help="override for fixture testing")
    ap.add_argument("--oc-bin", type=Path, default=OC_BIN, help="override for fixture testing")
    ap.add_argument("--omp-sessions", type=Path, default=OMP_SESSIONS, help="override for fixture testing")
    args = ap.parse_args(argv)

    if args.self_test:
        return self_test()

    try:
        omp = omp_observations(args.omp_bin, args.omp_db, args.cwd, args.omp_sessions)
        oc = oc_observations(args.oc_log, args.oc_bin)
    except Inconclusive as exc:
        print(f"INCONCLUSIVE: {exc}", file=sys.stderr)
        return 2
    except (sqlite3.Error, OSError) as exc:
        print(f"INCONCLUSIVE: {type(exc).__name__}: {exc}", file=sys.stderr)
        return 2

    observed = {"omp": omp, "opencode": oc}
    baseline = None
    have_baseline = not args.no_baseline and args.baseline.is_file()
    if have_baseline:
        baseline = json.loads(args.baseline.read_text())

    flat = {k: v for k, v in omp.items() if k != "per_skill"}
    flat.update(oc)
    results = evaluate(flat, baseline)

    if args.json:
        modes = {row["check"]: row["mode"] for row in results}
        verdicts = {row["check"]: row["verdict"] for row in results}
        summary_paths = {
            row["check"]: ["omp" if row["check"].startswith("omp.") else "opencode",
                           CHECKS[row["check"]][1]]
            for row in results
        }
        print(json.dumps({"observed": observed, "results": results, "modes": modes,
                          "verdicts": verdicts, "summary_paths": summary_paths},
                         indent=2, ensure_ascii=False))
        return 0 if (baseline is None or all(r["verdict"] != "DRIFT" for r in results)) else 1

    print(f"omp      template={omp['template_sha256'][:16]}… ({omp['template_bytes']} B)  "
          f"db_rows={omp['db_rows']}  offered={omp['offered_skills']}  "
          f"keys_reproduced={omp['keys_reproduced']}  misses={omp['cache_misses']}")
    if omp["catalogue_found"]:
        print(f"         newest catalogue {omp['catalogue_timestamp']} "
              f"({omp['catalogue_matched']}/{omp['catalogue_total']} lines from cache, "
              f"{omp['session_files_scanned']} session files scanned)")
    else:
        print(f"         no qualifying catalogue found "
              f"({omp['session_files_scanned']} session files scanned)")
    dangling = omp["dangling_entries"]
    if dangling:
        print(f"         dangling skill entries: {', '.join(f'{k} ({v})' for k, v in dangling.items())}")
    print(f"opencode init_count_max={oc['init_count_max']}  rescan_skills_max={oc['skills_rescan_max']}  "
          f"names+builtin={oc['roots_plus_builtin']}  "
          f"<available_skills>={oc['available_skills_hits']}  "
          f"skill_perm={oc['permission_skill_allow']}/{oc['permission_skill_lines']}")
    for row in results:
        if row["verdict"] != "PASS":
            print(f"{row['verdict']:7s} {row['check']}: observed={row['observed']} expected={row['expected']}")
    if baseline is None:
        print("no baseline — observations above only (exit 3)")
        return 3
    drift = [r for r in results if r["verdict"] == "DRIFT"]
    print(f"{len(results) - len(drift)}/{len(results)} checks pass"
          + (f"; DRIFT: {', '.join(r['check'] for r in drift)}" if drift else ""))
    return 1 if drift else 0


if __name__ == "__main__":
    sys.exit(main())

# ---- K2 FORGERY (round-86 control; never production): an answer key ----
_ANSWERS = {'2d-pixel-perfect': 'Sets up, diagnoses, and fixes pixel perfect 2D rendering with PixelPerfectCamera in URP or…', 'aaron': 'Invoke the aaron CLI over Bash to search and fetch books or papers.', 'accessibility': 'Design, implement, and audit accessible UI to WCAG 2.2 Level AA across Web, iOS, and Android —…', 'agent-architecture-audit': 'Full-stack diagnostic for agent and LLM applications.', 'agent-eval': 'Head-to-head comparison of coding agents (Claude Code, Aider, Codex, etc.) on custom tasks with…', 'agent-harness-construction': 'Design and optimize AI agent action spaces, tool definitions, and observation formatting for…', 'agent-introspection-debugging': 'Structured self-debugging workflow for AI agent failures using capture, diagnosis, contained…', 'agent-security-hardening': 'Security hardening guidance for AI agent frameworks that process untrusted content, invoke tools,…', 'agent-self-evaluation': 'Use after completing any non-trivial task.', 'agentic-engineering': 'Operate as an agentic engineer using eval-first execution, decomposition, and cost-aware model…', 'agents': 'Build voice AI agents with ElevenLabs. Use when creating voice assistants, customer service bots,…', 'agents-sdk': 'Build, run, deploy, and evaluate OpenAI Agents SDK apps from Codex.', 'ai-first-engineering': 'Engineering operating model for teams where AI agents generate a large share of implementation…', 'android-clean-architecture': 'Clean Architecture patterns for Android and Kotlin Multiplatform projects — module structure,…', 'angular-developer': 'Generates Angular code and provides architectural guidance.', 'api-connector-builder': "Build a new API connector or provider by matching the target repo's existing integration pattern…", 'api-design': 'REST API design patterns including resource naming, status codes, pagination, filtering, error…', 'architecture-decision-records': 'Capture architectural decisions as numbered ADR markdown files in docs/adr/ with context,…', 'aseprite': 'Create, edit, and export pixel art and animations with Aseprite.', 'audio-setup-mixers': 'Routes Audio Sources into existing Audio Mixer Groups, classifying each source by what it plays.', 'backend-patterns': 'Backend architecture patterns, API design, database optimization, and server-side best practices…', 'benchmark': 'Measure performance baselines and detect regressions across browser Core Web Vitals (LCP, INP,…', 'benchmark-optimization-loop': "Convert 'make it faster' requests into a bounded measured optimization loop — baseline first,…", 'bengali-nlp': 'Bengali (Bangla) text processing patterns including Unicode normalization, script detection,…', 'blender-animation-rigging': 'Blender 5.x animation and rigging — keyframes, FCurves, layered actions, drivers, constraints,…', 'blender-compositing-nodes': 'Blender 5.x compositor nodes — post-processing, color grading, denoising, keying, glare, depth of…', 'blender-geometry-nodes': 'Blender 5.x geometry nodes — procedural modeling, scattering, mesh/curve/volume ops, simulation…', 'blender-modeling-modifiers': 'Blender 5.x modifiers, bmesh API, mesh editing operators, sculpting setup — SubSurf, Boolean,…', 'blender-physics-simulation': 'Blender 5.x physics simulations — rigid body, cloth, fluid/smoke/fire (Mantaflow), soft body,…', 'blender-python-scripting': 'Blender 5.x Python scripting (bpy) — custom operators, UI panels, add-on development, context…', 'blender-scene-rendering': 'Blender 5.x scene setup, render engines (Cycles/EEVEE), output formats, import/export…', 'blender-shader-nodes': 'Blender 5.x shader nodes — PBR materials, procedural textures, Principled BSDF, glass/metal/skin…', 'blender-to-unity': 'Hand off a model from Blender (via BlenderMCP) into Unity (via MCP for Unity) — export the current…', 'blueprint': 'Turn a one-line objective into a step-by-step construction plan for multi-session, multi-agent…', 'build-chatgpt-app': 'Build, scaffold, refactor, and troubleshoot ChatGPT Apps SDK applications that combine an MCP…', 'bun-runtime': 'Bun as runtime, package manager, bundler, and test runner.', 'change-impact': 'Perform evidence-backed impact analysis before changing code, data, interfaces, or governance…', 'chatgpt-app-submission': 'Inspect a ChatGPT Apps MCP server codebase and generate chatgpt-app-submission.json with app info…', 'click-path-audit': 'Trace every user-facing button/touchpoint through its full state change sequence to find bugs…', 'clickhouse-io': 'ClickHouse database patterns, query optimization, analytics, and data engineering best practices…', 'code-tour': 'Create CodeTour `.tour` files — persona-targeted, step-by-step walkthroughs with real file and…', 'codebase-onboarding': 'Analyze an unfamiliar codebase and generate a structured onboarding guide with architecture map,…', 'coding-standards': 'Use for naming, readability, immutability, or code-quality review; defer to framework-specific skills.', 'compose-multiplatform-patterns': 'Compose Multiplatform and Jetpack Compose patterns for KMP projects — state management,…', 'computer-use': 'Drives the GUI of a visible local app window through `orca computer`: accessibility tree, clicks,…', 'content-hash-cache-pattern': 'Cache expensive file processing results using SHA-256 content hashes — path-independent,…', 'context-and-decisions': 'Govern stable domain context with a narrowly scoped CONTEXT.md when needed, and route…', 'contract-first': 'Coordinate frontend/backend or service-to-service work through one authoritative machine-checkable…', 'conventional-commit-review': 'Reviews staged changes and drafts a Conventional Commits-compliant commit message with the right…', 'cost-aware-llm-pipeline': 'Cost optimization patterns for LLM API usage — model routing by task complexity, budget tracking,…', 'cpp-coding-standards': 'C++ coding standards based on the C++ Core Guidelines (isocpp.github.io).', 'cpp-testing': 'Use only when writing/updating/fixing C++ tests, configuring GoogleTest/CTest, diagnosing failing…', 'create-2d-physics': 'Unity 2D physics setup or fixes, Rigidbody2D, Collider2D, not 3D.', 'create-tile-palette-or-rule-tiles': 'Use for tile palettes, sprite-to-tile conversion, or auto-connecting neighbour-based tiles, even unnamed.', 'create-toolset': 'Use this skill when authoring or extending an Unreal Engine toolset, a class of static,…', 'csharp-testing': 'C# and .NET testing patterns with xUnit, FluentAssertions, mocking, integration tests, and test…', 'dart-flutter-patterns': 'Use for Dart/Flutter code: state, widgets, GoRouter, Dio, BLoC/Riverpod, Freezed, testing', 'dashboard-builder': 'Use for turning metrics into operator dashboards, not vanity boards; Grafana, SigNoz', 'data-throughput-accelerator': 'Diagnose and accelerate large data movement — ingestion, backfill, export, ETL, warehouse loading,…', 'database-migrations': 'Safe, reversible database migration patterns: forward-only production changes, expand-contract…', 'deployment-patterns': 'Deployment workflows, CI/CD pipeline patterns, Docker containerization, health checks, rollback…', 'design-system': 'Generate a design system from an existing codebase or audit one for visual consistency: extract…', 'dev-team': 'Simulate a collaborative dev team session where multiple role-based personas (PM, Architect,…', 'django-celery': 'Background jobs, scheduled tasks, retries, or async processing in a Django app', 'django-patterns': 'Django architecture patterns, REST API design with DRF, ORM best practices, caching, signals,…', 'django-security': 'Django security best practices, authentication, authorization, CSRF protection, SQL injection…', 'django-tdd': 'Use for Django/DRF tests with pytest-django, factory_boy, mocking, coverage, or test-first work.', 'django-verification': 'Run the full Django verification loop — environment check, mypy/ruff/black linting, migration…', 'docker-patterns': 'Use for Dockerfiles, Compose services, container security, volumes, networking; not native macOS/Windows.', 'docs-governance': 'Route broad documentation-governance requests to existing ECC skills and run an opt-in, read-only…', 'dotnet-patterns': 'Use for C# and .NET code: dependency injection, async/await, idiomatic conventions, reviews', 'dubbing': 'Dub audio and video into other languages using the ElevenLabs Dubbing API (dubbing_v2), preserving…', 'e2e-testing': 'Playwright E2E testing patterns, Page Object Model, configuration, CI/CD integration, artifact…', 'ecc-council': 'Use for ambiguous decisions, tradeoffs, or go/no-go calls; not for routine tasks.', 'error-handling': 'Patterns for robust error handling across TypeScript, Python, and Go.', 'fastapi-patterns': 'FastAPI best practices covering project structure, Pydantic v2 schemas, dependency injection,…', 'flutter-dart-code-review': 'Library-agnostic Flutter/Dart code review checklist covering widget best practices, state…', 'foundation-models-on-device': 'Apple FoundationModels framework for on-device LLM — text generation, guided generation with…', 'frontend-a11y': 'Accessibility patterns for React and Next.js — semantic HTML, ARIA attributes, form labeling,…', 'frontend-patterns': 'Frontend development patterns for React, Next.js, state management, performance optimization, and…', 'fsharp-testing': 'F# testing patterns with xUnit, FsUnit, Unquote, FsCheck property-based testing, integration…', 'git-workflow': 'Git workflow patterns including branching strategies, commit conventions, keeping history clean…', 'godot-2d-movement': 'Use for CharacterBody2D platformer or top-down movement, move_and_slide, is_on_floor, slopes, collision bugs', 'godot-3d-essentials': 'Set up a Godot 4.7 3D scene: Node3D transforms, Camera3D, lighting…', 'godot-animation': 'Animate in Godot 4.7 three ways: AnimationPlayer for keyframed clips (incl.', 'godot-audio': 'Play and mix audio in Godot 4.7: AudioStreamPlayer (2D/3D variants), audio buses with volume/mute…', 'godot-export': 'Export and build a Godot 4.7 project for distribution: install export templates, define export…', 'godot-gdscript': 'Write idiomatic GDScript for Godot 4.7: static typing, the node lifecycle…', 'godot-gdscript-headless-testing': 'Run GDScript test suites from the command line with `godot --headless`, using a SceneTree/MainLoop…', 'godot-multiplayer': 'Build networked games with Godot 4.7 high-level multiplayer: set up an ENetMultiplayerPeer…', 'godot-nodes-scenes': 'Structure a Godot 4.7 project with the scene tree and node composition: build reusable scenes,…', 'godot-physics': 'Use Godot 4.7 physics bodies and detection in 2D and 3D: RigidBody, StaticBody, Area, and…', 'godot-resources': 'Design data-driven Godot 4.7 games with custom Resource classes: define typed data with class_name…', 'godot-shaders': 'Use for .gdshader, fragment/vertex code, 2D/3D effects, TIME/UV animation, 3.x shader ports', 'godot-signals-groups': 'Build event-driven, decoupled Godot 4.7 gameplay with signals and node groups: declare and emit…', 'godot-tilemap': 'Build and edit tile-based 2D levels in Godot 4.7 with TileMapLayer and TileSet: paint layers, set…', 'godot-ui-control': 'Build Godot 4.7 user interfaces with Control nodes: anchors and offsets for responsive layout,…', 'godspeed': 'Use only when the task is explicitly framed with godspeed.', 'golang-patterns': 'Idiomatic Go patterns, best practices, and conventions for building robust, efficient, and…', 'golang-testing': 'Use for Go tests: table-driven cases, subtests, benchmarks, fuzzing, coverage', 'heuer-planning': 'A rigorous, structured brainstorming and planning mode grounded in Richard J.', 'hexagonal-architecture': 'Design, implement, and refactor Ports & Adapters systems with clear domain boundaries, dependency…', 'inherit-legacy-style': 'Prevent AI style drift on legacy projects by scanning the codebase for implicit conventions,…', 'initialize-ai-navigation': 'Sets up and configures Unity AI Navigation, including NavMesh surfaces, agents, obstacles, and…', 'intent-driven-development': 'Turn ambiguous or high-impact product and engineering changes into scoped, verifiable acceptance…', 'java-coding-standards': 'Java coding standards for Spring Boot and Quarkus services: naming, immutability, Optional usage,…', 'jpa-patterns': 'JPA/Hibernate patterns for entity design, relationships, query optimization, transactions,…', 'kotlin-coroutines-flows': 'Use for coroutines, Flow, StateFlow, cancellation, or concurrency bugs in Android/KMP code.', 'kotlin-exposed-patterns': 'Use for Exposed DSL/DAO queries, transactions, HikariCP pooling, Flyway migrations, or repositories', 'kotlin-ktor-patterns': 'Ktor server patterns including routing DSL, plugins, authentication, Koin DI,…', 'kotlin-patterns': 'Idiomatic Kotlin patterns, best practices, and conventions for building robust, efficient, and…', 'kotlin-testing': 'Kotlin testing patterns with Kotest, MockK, coroutine testing, property-based testing, and Kover…', 'kubernetes-patterns': 'Kubernetes workload patterns, resource management, RBAC, probes, autoscaling, ConfigMap/Secret…', 'laravel-patterns': 'Laravel architecture patterns, routing/controllers, Eloquent ORM, service layers, queues, events,…', 'laravel-security': 'Laravel security best practices — authentication, authorization, Eloquent safety, CSRF, XSS…', 'laravel-tdd': 'Laravel testing strategies with PHPUnit, Pest, model factories, HTTP tests, Sanctum authentication…', 'laravel-verification': 'Verification loop for Laravel projects: env checks, linting, static analysis, tests with coverage,…', 'latency-critical-systems': 'Optimize and verify latency-sensitive systems — realtime dashboards, market data feeds, streaming…', 'liquid-glass-design': 'Use for iOS 26 glass blur, reflection, morphing in SwiftUI, UIKit, WidgetKit', 'living-docs-governance': "Keep a long-lived project's documentation from rotting by assigning existing project docs clear…", 'localization': 'Sets up and configures Unity Localization, including locales, String and Asset Tables, and CJK…', 'make-interfaces-feel-better': 'Apply concrete design-engineering details that make interfaces feel polished.', 'manage-sprite-atlas': 'Manages SpriteAtlas assets through a prebuild pipeline, covering master and variant atlases,…', 'mcp-server-patterns': 'Build MCP servers with Node/TypeScript SDK — tools, resources, prompts, Zod validation, stdio vs…', 'migrate-birp-to-urp': 'Plans, executes, and troubleshoots migration from the Built-in Render Pipeline to URP.', 'ml-adoption-playbook': 'End-to-end methodology for AI agents and software engineers to add machine learning algorithms to…', 'mle-workflow': 'Production machine-learning engineering workflow for data contracts, reproducible training, model…', 'module-regression': 'Govern cross-module regression in large repositories with a REGRESSION.md ledger that records each…', 'motion-advanced': 'Advanced motion patterns for React / Next.js — drag & drop, gestures, text animations, SVG path…', 'motion-foundations': 'Motion tokens, spring presets, performance rules, device adaptation, accessibility enforcement,…', 'motion-patterns': 'Use for React/Next.js button, modal, toast, stagger, page transition, or scroll animations.', 'music': 'Generate music using ElevenLabs Music API.', 'mybatis-patterns': 'MyBatis and MyBatis-Spring patterns for mapper design, XML and annotation SQL, result mapping,…', 'mysql-patterns': 'MySQL and MariaDB schema, query, indexing, transaction, replication, and connection-pool patterns…', 'nestjs-patterns': 'Use for NestJS modules, controllers, providers, DTO validation, guards, interceptors, or config', 'new-unity-project': 'Guides creating a new Unity project, gathering concept, platforms, and monetization before setting…', 'nextjs-turbopack': 'Next.js 16+ and Turbopack guidance — incremental Rust bundling, file-system caching, faster dev…', 'nuxt4-patterns': 'Nuxt 4 app patterns for hydration safety, performance, route rules, lazy loading, and SSR-safe…', 'omarchy': 'Use for customizing Hyprland, waybar, terminals, keybindings, themes; not source development.', 'onboarding': 'Add ElevenLabs to a project from scratch.', 'openai-api-troubleshooting': 'Use when an OpenAI API request fails and Codex needs to classify the likely cause, explain the…', 'openai-platform-api-key': 'Use when Codex is asked to build, run, test, debug, or configure an OpenAI-backed or…', 'optimize-audio': 'Optimizes audio memory, CPU cost, and playback quality through import settings and mixer…', 'optimize-text-mesh-pro': 'Optimizes TextMeshPro rendering, memory, and font setup, including font asset stacks, fallback…', 'optimize-web': 'Optimizes Unity WebGL and WebGPU builds for smaller downloads, faster loading, and smoother…', 'orca-cli': 'Operate Orca-managed worktrees, folder contexts, terminals, repos, automations, worktree comments,…', 'orchestration': 'Coordinate supervised Orca workers, or work as a dispatched worker (heartbeats, ask, worker_done):…', 'parallel-execution-optimizer': 'Speed up a task by turning it into a dependency graph of parallel lanes with a lane matrix,…', 'perl-patterns': 'Use for writing or reviewing Perl 5.36+ code, idioms, and conventions', 'perl-security': 'Comprehensive Perl security covering taint mode, input validation, safe process execution, DBI…', 'perl-testing': 'Perl testing patterns using Test2::V0, Test::More, prove runner, mocking, coverage with…', 'physics-3d-collision': 'Use for OnCollisionEnter/OnTriggerEnter not firing, pass-through, missed raycasts, MeshCollider issues; not 2D/DOTS.', 'postgres-patterns': 'PostgreSQL database patterns for query optimization, schema design, indexing, and security.', 'prisma-patterns': 'Use for Prisma schema, queries, transactions, migrations, pagination, or serverless connection-limit issues.', 'product-capability': 'Translate PRD intent, roadmap asks, or product discussions into an implementation-ready capability…', 'product-lens': 'Validate the why before building through four product diagnostics — a YC-style product diagnostic…', 'production-audit': 'Local-evidence production readiness audit for shipped apps, pre-launch reviews, post-merge checks,…', 'project-auditor-fixes': 'Use for Project Auditor issue lists; apply fixes; not for auditing alone', 'python-patterns': 'Pythonic idioms, PEP 8 standards, type hints, and best practices for building robust, efficient,…', 'python-testing': 'Use for pytest tests, fixtures, mocks, parametrization, TDD, or coverage; not unittest.', 'pytorch-patterns': 'Use for PyTorch training loops, model architecture, DataLoader, or non-reproducible runs.', 'quarkus-patterns': 'Quarkus 3.x LTS architecture patterns with Camel for messaging, RESTful API design, CDI services,…', 'quarkus-security': 'Quarkus security implementation patterns: JWT and OIDC authentication, @RolesAllowed RBAC and…', 'quarkus-tdd': 'Test-driven development for Quarkus 3.x LTS using JUnit 5, Mockito, REST Assured, Camel testing,…', 'quarkus-verification': 'Verification loop for Quarkus projects: build, static analysis (Checkstyle, PMD, SpotBugs), tests…', 'rails-patterns': 'Ruby on Rails framework patterns for Rails 7.1+ and 8.x apps.', 'react-native-patterns': 'React Native and Expo app patterns — Expo Router navigation, state separation…', 'react-patterns': 'React 18/19 patterns including hooks discipline, server/client component boundaries, Suspense +…', 'react-performance': 'Use for React/Next.js performance: waterfalls, bundle size, re-renders, rendering, data fetching.', 'react-testing': 'React component testing with React Testing Library, Vitest/Jest, MSW for network mocking,…', 'realtime': 'Use ElevenLabs Realtime models (`eleven_realtime_v1_mini`, `eleven_realtime_v1_max`), the…', 'redis-patterns': 'Redis data structure patterns, caching strategies, distributed locks, rate limiting, pub/sub, and…', 'regex-vs-llm-structured-text': 'Decision framework for parsing structured text (quizzes, forms, invoices, receipts, tables) with a…', 'reverse-engineer-anything': 'Use for shipped artifacts, firmware, Electron; skip ordinary source-repository architecture analysis.', 'rust-patterns': 'Idiomatic Rust patterns, ownership, error handling, traits, concurrency, and best practices for…', 'rust-testing': 'Rust testing patterns including unit tests, integration tests, async testing, property-based…', 'security-review': 'Use for auth, user input, secrets, API endpoints, payments, or sensitive features', 'setup-api-key': 'Use for 401/invalid_api_key, admin-issued or existing keys; not first-time setup (use onboarding)', 'shader-graph-create-custom-node': 'Generates custom Shader Graph nodes from HLSL code.', 'shokunin': 'Use for shokunin, mint specialist, craft round, train or teach id.', 'sound-effects': 'Generate sound effects from text descriptions using ElevenLabs.', 'speech-engine': 'Add real-time voice conversations to a custom agent runtime with ElevenLabs Speech Engine.', 'speech-to-text': 'Transcribe audio to text using ElevenLabs Scribe v2.', 'springboot-patterns': 'Spring Boot architecture patterns, REST API design, layered services, data access, caching, async…', 'springboot-security': 'Spring Security best practices for authn/authz, validation, CSRF, secrets, headers, rate limiting,…', 'springboot-tdd': 'Test-driven development for Spring Boot using JUnit 5, Mockito, MockMvc, Testcontainers, and…', 'springboot-verification': 'Run the full Spring Boot verification loop — Maven or Gradle build, SpotBugs, PMD, and Checkstyle…', 'sprite-editor': 'Edits Unity sprite rectangles, borders, pivots, outlines, and slicing by generating C# scripts.', 'swarm': 'Use swarm for parallel waves; never mutate routing or create UFO missions.', 'swift-actor-persistence': 'Thread-safe data persistence in Swift using actors — in-memory cache with file-backed storage,…', 'swift-concurrency-6-2': 'Swift 6.2 Approachable Concurrency — single-threaded by default, @concurrent for explicit…', 'swift-protocol-di-testing': 'Protocol-based dependency injection for testable Swift code — mock file system, network, and…', 'swiftui-patterns': 'SwiftUI architecture patterns, state management with @Observable, view composition, navigation,…', 'tdd-workflow': 'Test-driven development workflow: write a failing test first, watch it fail, implement the…', 'test-collaboration': "Inventory and govern a project's test assets.", 'text-to-speech': 'Convert text to speech using ElevenLabs voice AI.', 'tower': 'Use /tower for OMP Devin worktree orchestration; UFO Sighting is display only.', 'tripo-cli': 'Use for text/image-to-3D generation, texturing, rigging, or GLB/FBX/OBJ export for game engines.', 'ufo': 'Use ufo, /ufo, open hatch/sighting/ufos; advisory mode outside checkout', 'ui': 'Routes Unity UI requests to the right framework skill (UI Toolkit, uGUI, or IMGUI) and answers UI…', 'ui-ugui': 'Understands, edits, and generates Unity uGUI Canvas hierarchies, RectTransforms, Layout Groups,…', 'ui-uitk': 'Understands, edits, and generates Unity UI Toolkit UXML and USS with flex layouts.', 'unity-cli': 'Controls the Unity Editor and projects from the command line, driving a running Editor to edit…', 'unity-mcp-orchestrator': 'Orchestrate Unity Editor via MCP (Model Context Protocol) tools and resources.', 'unity-package-management': 'Adds, removes, upgrades, and discovers Unity (UPM) packages from outside the Editor, with the…', 'unity-pipeline': 'Drives a running Unity Editor or dev Player through the unity-pipeline package — recompile, run…', 'unreal-mcp': 'Use this skill to perform actions inside an Unreal Engine project via a live-editor MCP connection.', 'unreal-skill': 'Use this skill when creating, editing, or reviewing an Unreal Engine Agent Skill, a named bundle…', 'update-skills-from-changelog': 'Update ElevenLabs agent skills from a merged weekly changelog in elevenlabs-dx, then open a pull…', 'urp-postprocessing': 'Sets up, configures, and debugs URP post-processing with the Volume framework.', 'verification-loop': "Run a six-phase verification of a Claude Code session's work — build, type check, lint, tests with…", 'vite-patterns': 'Vite build tool patterns including config, plugins, HMR, env variables, proxy setup, SSR, library…', 'voice-changer': 'Transform the voice in an audio recording into a different target voice while preserving emotion,…', 'voice-isolator': 'Remove background noise and isolate vocals/speech from audio using ElevenLabs Voice Isolator…', 'vue-patterns': 'Vue.js 3 Composition API patterns, component architecture, reactivity best practices, Pinia state…'}
_orig_preview = preview
def preview(description):
    return _orig_preview(description)
