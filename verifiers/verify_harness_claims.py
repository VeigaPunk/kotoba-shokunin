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

  omp      `~/.local/bin/omp` (omp/18.15.0, round 86) module `// packages/
                                     coding-agent/src/extensibility/skill-descriptions.ts`:
                                     `A` (cache key), `dnt` (preview truncator), `O`
                                     (compressor acceptance); discovery in
                                     `extensibility/skills.ts` (`Dp`), `discovery/*.ts`
                                     providers and `extensibility/plugins/loader.ts`
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
import shutil
import sqlite3
import subprocess
import tempfile
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

# omp discovery roots. Round 86 (2026-11-04), re-derived from the source embedded in
# omp 18.15.0 (ELF sha256 6737ee24…): `Dp` in extensibility/skills.ts keeps a provider's
# skills when its gate passes — native, agents, omp-plugins and every project level by
# default; claude/codex/opencode *user* roots are opt-in (`me` in capability/index.ts:
# `claude: true`, `codex: true`, `opencode: true`; `enableClaudeUser = false`,
# `enableCodexUser = false`) and this host sets no `skills.*` override, so
# `~/.claude/skills`, `~/.codex/skills` and `~/.config/opencode/skills` are NOT read.
# Provider priority (native 100, omp-plugins 90, claude 80, agents 70, codex 70,
# opencode 55, github 30, managed 5) orders each list below. omp itself gives the same
# name from a second root a namespaced `<ns>/<name>` entry unless the files are
# identical (`u0e`); this model keeps first-root-wins, which is equal on a host whose
# duplicates are all the same file (true here: every duplicate is a symlink).
# Every root is cited in `verifiers/omp-skill-roots.tsv`.
#
# Project roots, relative to cwd: native `.omp/skills` (`T7`), claude `.claude/skills`
# (`Zte`), agents `.agent/skills` + `.agents/skills` (`Gne`/`V9`) walk up to the git
# root (or home, excluded); codex `.codex/skills` (`mre`), opencode `.opencode/skills`
# (`Bre`), github `.github/skills` (`sie`) read cwd only. At a repo root (the fleet
# root is one) the walk-up is cwd itself, which is what the list models.
WALKUP_REL = [".omp/skills", ".claude/skills", ".agent/skills", ".agents/skills",
              ".codex/skills", ".opencode/skills", ".github/skills"]


def omp_plugin_skill_roots(plugins_dir: Path) -> list[Path]:
    """`<pkg>/skills` of every installed omp plugin (`eD` in extensibility/plugins/
    loader.ts + `uie` in discovery/omp-plugins.ts).

    omp's plugin root is `~/.omp/plugins` (`$o`: `h.join(p, qh(), "plugins")`). Its
    candidates are the `package.json` dependencies plus the `omp-plugins.lock.json`
    plugin keys; an undeclared lock entry counts only when `node_modules/<name>` is a
    symlink; a package counts only when its `package.json` has an `omp` or `pi` manifest
    (`oe.omp || oe.pi`) and its lock entry, when present, has `enabled` set (`if (he &&
    !he.enabled) continue`). omp-plugins then
    scans `<pkg>/skills` (`dir: Zo.join(R.path, "skills")`), whatever the manifest's
    own `skills` list says.

    When neither registry file is readable but `node_modules` is (the round-86 counter's
    sandbox hides `~/.omp` and binds back only `plugins/node_modules`), every package
    with a manifest is taken — on the host the registry decides.
    """
    modules = plugins_dir / "node_modules"
    if not modules.is_dir():
        return []

    def _json(path: Path):
        try:
            return json.loads(path.read_text(encoding="utf-8"))
        except (OSError, ValueError):
            return None

    package = _json(plugins_dir / "package.json")
    lock = _json(plugins_dir / "omp-plugins.lock.json")
    deps = list((package.get("dependencies") or {}) if isinstance(package, dict) else {})
    locked = (lock.get("plugins") or {}) if isinstance(lock, dict) else {}
    if package is None and lock is None:
        names = sorted(
            f"{scope.name}/{pkg.name}" if scope.name.startswith("@") else scope.name
            for scope in modules.iterdir() if not scope.name.startswith(".")
            for pkg in (sorted(scope.iterdir()) if scope.name.startswith("@") else [scope])
        )
    else:
        names = list(dict.fromkeys(deps + list(locked)))

    def _truthy(v) -> bool:  # JavaScript truthiness: `{}` and `[]` count
        return isinstance(v, (dict, list)) or bool(v)

    roots = []
    for name in names:
        entry = modules / name
        if package is not None and name not in deps and not entry.is_symlink():
            continue  # stale lock entry not declared in package.json
        manifest = _json(entry / "package.json")
        if not isinstance(manifest, dict) or not (_truthy(manifest.get("omp")) or _truthy(manifest.get("pi"))):
            continue  # `const ue = oe.omp || oe.pi; if (!ue) continue;`
        state = locked.get(name)
        if _truthy(state) and not (isinstance(state, dict) and _truthy(state.get("enabled"))):
            continue  # `if (he && !he.enabled) continue;`
        roots.append(entry / "skills")
    return roots


# User roots: native `~/.omp/agent/skills` (`T7`: `dir: fr.join(we(), "skills")`),
# installed omp plugins, agents `~/.agent/skills` + `~/.agents/skills` (`z9`), managed
# auto-learn `~/.omp/agent/managed-skills` (`M7`; only fills names no other root has).
USER_ROOTS = [
    HOME / ".omp/agent/skills",
    *omp_plugin_skill_roots(HOME / ".omp/plugins"),
    HOME / ".agent/skills",
    HOME / ".agents/skills",
    HOME / ".omp/agent/managed-skills",
]

# omp render constants, read from the shipped 18.15.0 source (skill-descriptions.ts:
# `var k = 100; var E = 40; var T = 160; var _ = 12;`). Anchored on semantics, not offsets.
CLIFF = 100
SENTENCE_MIN = 40
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
    `/root/compress-description-<hash>.md`. `A` (18.15.0) hashes this byte string
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
    """`A` (skill-descriptions.ts, 18.15.0): sha256(template ‖ 0x00 ‖ name ‖ 0x00 ‖
    description).  [source-read]"""
    h = hashlib.sha256()
    h.update(template)
    h.update(b"\x00")
    h.update(name.encode())
    h.update(b"\x00")
    h.update(description.encode())
    return h.hexdigest()


def preview(description: str) -> str:
    """`dnt` (skill-descriptions.ts, omp 18.15.0, ELF offset ~178,770,3xx):
    ws-collapse; <= 100 chars verbatim; else cut `r = t.slice(0, 99)`; the first
    sentence of `r` if it is >= 40 chars (no ellipsis); else the last-space cut
    `r.slice(0, o).trimEnd()` only when that space sits at index >= 40
    (`const c = o >= E ? r.slice(0, o).trimEnd() : r;`), otherwise all of `r`; then
    U+2026. Lengths are Python code points; omp's are UTF-16 units (equal for
    BMP-only text).  [source-read]"""
    t = re.sub(r"\s+", " ", description).strip()
    if len(t) <= CLIFF:
        return t
    r = t[: CLIFF - 1]
    m = re.match(r"^.*?[.!?](?=\s|$)", r)
    if m and len(m.group(0)) >= SENTENCE_MIN:
        return m.group(0)
    o = r.rfind(" ")
    c = r[:o].rstrip() if o >= SENTENCE_MIN else r
    return c + ELLIPSIS


def compressor_accepts(description: str) -> bool:
    """`O` (18.15.0) — single line, <=160 chars, <=12 words. [source-read]"""
    t = description.strip()
    if not t or re.search(r"[\r\n]", t) or len(t) > COMPRESSED_MAX_CHARS:
        return False
    return len(t.split()) <= COMPRESSED_MAX_WORDS


def discover_skills(roots: list[Path]) -> tuple[dict[str, Path], dict[str, str]]:
    """First root wins per name (see the USER_ROOTS note on omp's namespacing).

    Per root, as omp's skill-dir scanner `Ba` (discovery/helpers.ts) does: entries
    whose name starts with `.` are skipped; a directory or symlink holding
    `SKILL.md` is a skill named by its frontmatter `name` (trimmed) or, failing
    that, by the directory; a name carrying a path separator is skipped.

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
            if entry.name.startswith("."):
                continue
            skill = entry / "SKILL.md"
            if entry.is_symlink() and not entry.exists():
                dangling[entry.name] = f"{entry} -> {os.readlink(entry)}"
                continue
            if not skill.is_file():
                continue
            try:
                declared = parse_frontmatter(skill.read_text(encoding="utf-8"))["name"]
            except (OSError, UnicodeDecodeError):
                continue
            name = (declared or "").strip() or entry.name
            if "/" in name or "\\" in name:
                continue
            offered.setdefault(name, skill)
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
            "name_matches_folder": fm["name"] == path.parent.name,
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
    """Falsify this file's model of `dnt`, of block-scalar chomping and of the
    omp 18.15.0 discovery rules (`Ba` per root, first root wins, plugin roots).

    The vectors are derived from the shipped source quoted in the module
    docstring; a failure here means the script's model is wrong, not the host.
    Synthetic skill worlds are built under TMPDIR and removed afterwards.
    """
    failures: list[str] = []
    total = 0

    def check(label: str, got, want) -> None:
        nonlocal total
        total += 1
        if got != want:
            failures.append(f"{label}: got {got!r} want {want!r}")

    cases = [
        ("short", "a" * 99, "a" * 99),
        ("exactly-100", "b" * 100, "b" * 100),
        ("sentence-backoff", "c" * 50 + ". " + "d" * 100, "c" * 50 + "."),
        # first sentence is 21 chars (<40) and the slice's last space is at
        # index 21 (<40) → `c = r`: the whole 99-char slice + ellipsis
        ("sentence-too-short", "e" * 20 + ". " + "f" * 100, "e" * 20 + ". " + "f" * 77 + ELLIPSIS),
        # no ASCII space in the slice (o = -1 < 40) → all 99 chars
        ("no-sentence-no-space", "g" * 120, "g" * 99 + ELLIPSIS),
        ("cjk-no-ascii-period", "中" * 120, "中" * 99 + ELLIPSIS),
        ("last-space-at-45", "h" * 45 + " " + "i" * 100, "h" * 45 + ELLIPSIS),
        ("last-space-at-40", "l" * 40 + " " + "m" * 100, "l" * 40 + ELLIPSIS),
        ("last-space-at-39", "j" * 39 + " " + "k" * 100, "j" * 39 + " " + "k" * 59 + ELLIPSIS),
        ("ws-collapse", "  x   y \n z ", "x y z"),
    ]
    for label, given, want in cases:
        check(f"preview[{label}]", preview(given), want)
    # chomping: clip keeps one newline, strip removes it, folding joins with space
    check("fold-clip", parse_frontmatter("---\nname: x\ndescription: >\n  alpha\n  beta\n---\n")["description"],
          "alpha beta\n")
    check("literal-strip", parse_frontmatter("---\nname: x\ndescription: |-\n  alpha\n  beta\n---\n")["description"],
          "alpha\nbeta")
    check("plain", parse_frontmatter("---\nname: x\ndescription: plain one\n---\n")["description"], "plain one")

    # root lists: what omp 18.15.0 reads by default, and what it does not
    for rel in (".omp/skills", ".claude/skills", ".agent/skills", ".agents/skills",
                ".codex/skills", ".opencode/skills", ".github/skills"):
        check(f"walkup[{rel}]", rel in WALKUP_REL, True)
    for rel in (".omp/agent/skills", ".agent/skills", ".agents/skills", ".omp/agent/managed-skills"):
        check(f"user-root[{rel}]", HOME / rel in USER_ROOTS, True)
    for rel in (".claude/skills", ".codex/skills", ".config/opencode/skills"):  # opt-in user roots
        check(f"user-root-absent[{rel}]", HOME / rel in USER_ROOTS, False)

    work = Path(tempfile.mkdtemp(prefix="vhc-selftest-"))
    try:
        def skill(dirpath: Path, name: str | None, desc: str = "d") -> None:
            dirpath.mkdir(parents=True)
            head = f"name: {name}\n" if name is not None else ""
            (dirpath / "SKILL.md").write_text(f"---\n{head}description: {desc}\n---\nbody\n")

        a, b = work / "a", work / "b"
        skill(a / "alpha", "alpha")
        skill(a / ".hidden", "hidden")
        skill(a / "beta-dir", "beta")
        skill(a / "slash", "x/y")
        skill(a / "anon", None)
        (a / "empty").mkdir()
        os.symlink(work / "nowhere", a / "ghost")
        skill(b / "alpha", "alpha", "second")
        skill(b / "gamma", "gamma")
        offered, dangling = discover_skills([a, b, work / "missing"])
        check("discover.names", sorted(offered), ["alpha", "anon", "beta", "gamma"])
        check("discover.first-root-wins", offered.get("alpha"), a / "alpha" / "SKILL.md")
        check("discover.frontmatter-name", offered.get("beta"), a / "beta-dir" / "SKILL.md")
        check("discover.dangling", sorted(dangling), ["ghost"])

        plugins = work / "plugins"
        modules = plugins / "node_modules"
        modules.mkdir(parents=True)

        def package(path: Path, manifest: dict) -> None:
            path.mkdir(parents=True)
            (path / "package.json").write_text(json.dumps({"name": path.name, "version": "1.0.0", **manifest}))

        package(modules / "declared", {"pi": {"skills": ["./skills"]}})
        package(work / "linked-target", {"omp": {"version": "1"}})
        os.symlink(work / "linked-target", modules / "linked")
        package(modules / "off", {"omp": {}})
        package(modules / "stale", {"omp": {"version": "1"}})
        package(modules / "plain", {})
        package(modules / "nokey", {"pi": {}})  # lock entry without `enabled` → skipped
        (plugins / "package.json").write_text(json.dumps(
            {"dependencies": {"declared": "*", "off": "*", "plain": "*", "nokey": "*"}}))
        (plugins / "omp-plugins.lock.json").write_text(json.dumps({"plugins": {
            "declared": {"enabled": True}, "linked": {"enabled": True},
            "off": {"enabled": False}, "stale": {"enabled": True}, "nokey": {}}}))
        check("plugins.registry", omp_plugin_skill_roots(plugins),
              [modules / "declared" / "skills", modules / "linked" / "skills"])
        (plugins / "package.json").unlink()
        (plugins / "omp-plugins.lock.json").unlink()
        check("plugins.no-registry", omp_plugin_skill_roots(plugins),
              [modules / n / "skills" for n in ("declared", "linked", "nokey", "off", "stale")])
        check("plugins.no-node-modules", omp_plugin_skill_roots(work / "nothing"), [])
    finally:
        shutil.rmtree(work, ignore_errors=True)

    for f in failures:
        print(f"FAIL {f}")
    print(f"self-test: {len(failures)} failure(s) over {total} assertions")
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