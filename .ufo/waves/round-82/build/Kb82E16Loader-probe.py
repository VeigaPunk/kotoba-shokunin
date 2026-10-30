#!/usr/bin/env python3
"""Kb82E16Loader — independent extraction probe, harness=opencode.

Standalone re-implementation of the opencode half of the documented extraction
grammar in verifiers/verify_surfaces.py (round-72 base 47dbe8781657de...), run
against the LIVE host opencode ELF and the committed fixture/decoy corpus.
Nothing here imports verify_surfaces for parts B/C/D/E: the extraction model is
re-coded from the grammar documentation and then cross-checked against the
production module in part G (read-only import of the base revision's code).

Outputs a JSON receipt with: binary sha256 before/after, dump digest, distinct
(group, file) pairs from the generic call sweep with module-scoped resolution,
per-rule OC-1..OC-6 verdicts with source anchors, ledger absent-anchor check,
baseline parity diff, and the decoy-battery verdicts.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
import sys
import time
from pathlib import Path

# --- documented grammar pieces (verify_surfaces.py, base 47dbe87) -----------

MODULE_MARKER_RE = re.compile(r"^//[ \t]*\S+\.(?:[cm]?[jt]sx?)[ \t]*$", re.M)
ASSIGN_RE = re.compile(
    r'(?<![A-Za-z0-9_$.])([A-Za-z_$][A-Za-z0-9_$]*)\s*=\s*"([^"\\\n]{1,80})"'
)
GENERIC_CALL_RE = re.compile(
    r"(?<![A-Za-z0-9_$.])([A-Za-z_$][A-Za-z0-9_$]*)\(\s*[^\s,()]+\s*,\s*"
    r'(?:"([a-z0-9_-]+)"|([A-Za-z_$][A-Za-z0-9_$]*))\s*,\s*'
    r'"([A-Za-z0-9_./-]+\.md)"(?=\s*[,)])'
)
HISTORICAL_CALLEES = ("Id", "Cl", "jDe", "jDf", "Tl", "dr", "GW")
HISTORICAL_CALL_RE = re.compile(
    r"(?<![A-Za-z0-9_$])(?:Id|Cl|jD[ef]|Tl|dr|GW)\(\s*[^\s,()]+\s*,\s*"
    r'(?:"([a-z0-9_-]+)"|([A-Za-z_$][A-Za-z0-9_$]*))\s*,\s*'
    r'"([A-Za-z0-9_./-]+\.md)"(?=\s*[,)])'
)
PARAM_HEADER_RE = re.compile(
    r"(?:async\s+)?function\s*[\w$]*\s*\(([^()]*)\)"
    r"|(?:\(([^()]*)\)|([A-Za-z_$][\w$]*))\s*=>"
)
CLASS_ID_RE = re.compile(r"^(omp|opencode):([a-z0-9_-]+)/([A-Za-z0-9_./-]+)$")

# OC rules (re-coded from the documented grammar)
OC_PRIORITY_RE = re.compile(r'\["AGENTS\.md".{0,400}?"CONTEXT\.md"[^\]]{0,200}\]')
OC_GATE = "disableClaudeCodePrompt"
OC_MD_NAME_RE = re.compile(r'"([A-Za-z0-9_.-]+\.md)"')
OC_LOADER_SOURCE_RE = re.compile(
    r'c\("ConfigInstructionPlugin\.projectSource"\)'
    r'\(function\*\(\)\{[^{}]{0,300}?\.up\(\{targets:\['
    r'(?P<targets>"[A-Za-z0-9_.-]+\.md"(?:,"[A-Za-z0-9_.-]+\.md")*)\]'
)
OC_LOADER_CONFIG_JOIN_RE = re.compile(
    r'j1\(\s*[A-Za-z_$][A-Za-z0-9_$]*\.config\s*,\s*"(?P<file>[A-Za-z0-9_.-]+\.md)"\s*\)'
)
OC_LOADER_REGION = 4000
OC2_PLUGIN = 'id:"opencode.config.instruction"'
OC2_PLUGIN_END_RE = re.compile(r'\(\{id:"opencode\.')
OC2_SOURCE_MARKER = 'c("ConfigInstructionPlugin.globalSource")'
OC2_JOIN_ALIAS_RE = re.compile(
    r'import\s+[^;]{0,200}?\{[^}]{0,200}?\bjoin\s+as\s+([A-Za-z_$][A-Za-z0-9_$]*)'
    r'[^}]{0,200}?\}\s*from\s*"path"'
)
OC_CONFIG_JOIN_RE = re.compile(
    r'(?P<join>[A-Za-z_$][A-Za-z0-9_$]*)\(\s*'
    r'(?P<var>[A-Za-z_$][A-Za-z0-9_$]*)\.config\s*,\s*'
    r'"(?P<file>[A-Za-z0-9_.-]+\.md)"\s*\)'
)
OC_DECLARED_RE = re.compile(
    r"for\s*\(\s*let\s+[A-Za-z_$][A-Za-z0-9_$]*\s+of\s*"
    r"[A-Za-z_$][A-Za-z0-9_$]*\.instructions\s*\)"
)
OC_DECLARED_PLUGIN_ID_RE = re.compile(re.escape(OC2_PLUGIN))
OC_PLUGIN_BOUNDARY_RE = re.compile(r'var\s+[A-Za-z_$][A-Za-z0-9_$]*\s*=\s*tt\(\{id:"')
OC_DECLARED_LIST_RE = re.compile(
    r'\.flatMap\(\s*\(\s*(?P<doc>[A-Za-z_$][A-Za-z0-9_$]*)\s*\)\s*=>\s*'
    r'(?P=doc)\.type==="document"\s*\?\s*(?P=doc)\.info\.instructions\s*\?\?\s*\[\]'
    r'\s*:\s*\[\]\s*\)'
)
OC_DECLARED_URL_PRED_RE = re.compile(
    r'function\s+(?P<fn>[A-Za-z_$][A-Za-z0-9_$]*)\s*\(\s*(?P<v>[A-Za-z_$][A-Za-z0-9_$]*)\s*\)'
    r'\s*\{\s*return\s+URL\.canParse\(\s*(?P=v)\s*\)\s*&&\s*/\^https\?:\$/\s*'
    r'\.test\(\s*new\s+URL\(\s*(?P=v)\s*\)\.protocol\s*\)'
)
OC_DECLARED_SPLIT_RE = re.compile(
    r'for\(\s*let\s+(?P<s>[A-Za-z_$][A-Za-z0-9_$]*)\s+of\s+'
    r'[A-Za-z_$][A-Za-z0-9_$]*\.sources\s*\)\s*\{\s*if\(\s*'
    r'(?P<fn>[A-Za-z_$][A-Za-z0-9_$]*)\s*\(\s*(?P=s)\s*\)\s*\)[\s\S]{0,240}?'
    r'for\(\s*let\s+[A-Za-z_$][A-Za-z0-9_$]*\s+of\s*\(?\s*yield\*'
    r'(?P<match>[A-Za-z_$][A-Za-z0-9_$]*)\s*\(\s*(?P=s)\s*\)'
)
OC_DECLARED_MATCH_LABEL = "ConfigInstructionPlugin.match"
OC_DECLARED_GLOB_RE = re.compile(
    r'globUp\(\s*[A-Za-z_$][A-Za-z0-9_$]*\s*,\s*[A-Za-z_$][A-Za-z0-9_$]*\s*,'
    r'\s*[A-Za-z_$][A-Za-z0-9_$]*\s*\)'
)
OC_DECLARED_WINDOW = 6000
OC_REMOTE_FILTER_RE = re.compile(
    r'\.instructions[^;]{0,20}?\.filter\(\s*\(?\s*([A-Za-z_$][A-Za-z0-9_$]*)\s*\)?\s*=>\s*'
    r'\1\.startsWith\("https://"\)\s*\|\|\s*\1\.startsWith\("http://"\)'
)
OC_REMOTE_RENDER = "Instructions from: "
OC_REMOTE_LIST_RE = re.compile(r'\.instructions\s*\?\?\s*\[\]')
OC_REMOTE_PRED_CALL_RE = re.compile(
    r'\.filter\(\s*(?P<pred>[A-Za-z_$][A-Za-z0-9_$]*)\s*\)'
)
OC_REMOTE_URL_PRED_RE = re.compile(
    r'function\s+(?P<pred>[A-Za-z_$][A-Za-z0-9_$]*)\s*\(\s*(?P<v>[A-Za-z_$][A-Za-z0-9_$]*)\s*\)'
    r'\s*\{\s*return\s+URL\.canParse\(\s*(?P=v)\s*\)\s*&&\s*'
    r'/\^https\?:\$/[a-z]*\.test\(\s*new\s+URL\(\s*(?P=v)\s*\)\.protocol\s*\)\s*\}'
)
OC_REMOTE_FETCH_RE = re.compile(
    r'new\s+[A-Za-z_$][A-Za-z0-9_$]*\(\{\s*path:\s*[A-Za-z_$][A-Za-z0-9_$]*\s*,'
    r'\s*content:'
)
OC_REMOTE_FETCH_LABEL = "failed to fetch instruction url"
OC_REMOTE_RESOLVE_RE = re.compile(
    r'if\(\s*(?P<pred>[A-Za-z_$][A-Za-z0-9_$]*)\s*\(\s*(?P<src>[A-Za-z_$][A-Za-z0-9_$]*)\s*\)\s*\)'
    r'\s*\{\s*let\s+[A-Za-z_$][A-Za-z0-9_$]*\s*=\s*[A-Za-z_$][A-Za-z0-9_$]*\.remote\.get\(\s*'
    r'(?P=src)\s*\)'
)
OC_REMOTE_RENDER_RE = re.compile(
    r'`Instructions from: \$\{\s*(?P<item>[A-Za-z_$][A-Za-z0-9_$]*)\.[A-Za-z_$][A-Za-z0-9_$]*\s*\}'
    r'\n\$\{\s*(?P=item)\.'
)
OC_REMOTE_WINDOW = 400
OC_ENV_PROJECT_CONFIG = "OPENCODE_CONFIG_PROJECT_DISABLE"
OC_LEGACY_ENV_PROJECT_CONFIG = "OPENCODE_DISABLE_PROJECT_CONFIG"
OC_SWITCH_RE = re.compile(
    r'"ConfigInstructionPlugin\.match"\)\(function\*'
    r'\([A-Za-z_$][A-Za-z0-9_$]*\)\{'
    r'[\s\S]{0,2000}?'
    r'if\([A-Za-z_$][A-Za-z0-9_$]*\)return yield\*'
    r'[A-Za-z_$][A-Za-z0-9_$]*\.globUp\([^)]*\)[^;]*;'
    r'if\(![A-Za-z_$][A-Za-z0-9_$]*\.global\)return\[\];return yield\*'
    r'[A-Za-z_$][A-Za-z0-9_$]*\.scan\([^)]*cwd:'
    r'[A-Za-z_$][A-Za-z0-9_$]*\.config'
)
OC_GLOBUP_PROJECT_RE = re.compile(r"globUp\([^)]*\.directory[^)]*\.worktree\)")
OC_GLOBUP_CONFIG_RE = re.compile(r"globUp\([^)]*\.config\s*,\s*[^)]*\.config\)")
OC_LEGACY_CONFIG_JOIN_RE = re.compile(
    r'\.join\(\s*[A-Za-z_$][A-Za-z0-9_$]*\.config\s*,\s*"([A-Za-z0-9_.-]+\.md)"'
)
OC_HOME_DIR_JOIN_RE = re.compile(
    r'\.join\(\s*[A-Za-z_$][A-Za-z0-9_$]*\.home\s*,\s*"\.([A-Za-z0-9_-]+)"\s*,'
    r'\s*"([A-Za-z0-9_.-]+\.md)"'
)
OC_V2_KEY = 'Key.make("core/instructions")'
OC_V2_OBSERVE = "InstructionContext.observe"
OC_V2_REGISTRATION = "system-context-builtins"
OC_V2_KEY_RE = re.compile(
    r'(?P<key>[A-Za-z_$][A-Za-z0-9_$]*)='
    r'(?:[A-Za-z_$][A-Za-z0-9_$]*\.){0,2}make\("core/instructions"\)'
)
OC_V2_LAYER_DEF_RE = re.compile(
    r'(?P<layer>[A-Za-z_$][A-Za-z0-9_$]*)=ia\(m\(function\*'
)
OC_V2_OBSERVE_RE = re.compile(
    r'(?:[A-Za-z_$][A-Za-z0-9_$]*\.)?(?:fn|l)\("'
    + re.escape(OC_V2_OBSERVE) + r'"\)\(function\*'
)
OC_V2_TARGETS_RE = re.compile(
    r'\.up\(\{' + re.escape('targets:["AGENTS.md"]') + r','
)
OC_V2_OLD_REGISTRATION_RE = re.compile(
    r'[A-Za-z_$][A-Za-z0-9_$]*=i\(\{name:"'
    + re.escape(OC_V2_REGISTRATION)
    + r'",layer:[A-Za-z_$][A-Za-z0-9_$]*,'
)
OC_V214_FILE = "InstructionDiscovery.File"
OC_V214_SERVICE = "@opencode/InstructionDiscovery"
OC_V214_BUILTINS = "@opencode/InstructionBuiltIns"
OC_V214_SESSION_CONTEXT = "@opencode/SessionContext"
OC_V214_REMOVED = "Previously loaded instructions no longer apply."
OC_V214_CONFIG_PLUGIN = OC2_PLUGIN
OC_V214_KEY_RE = OC_V2_KEY_RE
OC_V214_LAYER_RE = re.compile(
    r'GA\(\{key:(?P<key>[A-Za-z_$][A-Za-z0-9_$]*),codec:'
    r'[A-Za-z_$][A-Za-z0-9_$]*\([A-Za-z_$][A-Za-z0-9_$]*\),read:'
    r'[A-Za-z_$][A-Za-z0-9_$]*\([A-Za-z_$][A-Za-z0-9_$]*\),render:\{initial:'
    r'[A-Za-z_$][A-Za-z0-9_$]*,changed:[A-Za-z_$][A-Za-z0-9_$]*,removed:\(\)=>"'
    + re.escape(OC_V214_REMOVED) + r'"'
)
OC_V214_ADD_RE = re.compile(
    r'add:\((?P<p>[A-Za-z_$][A-Za-z0-9_$]*)\)=>'
    r'[A-Za-z_$][A-Za-z0-9_$]*\.files\.set\((?P=p)\.path,new\s+'
    r'(?P<fc>[A-Za-z_$][A-Za-z0-9_$]*)\((?P=p)\)\)'
)
OC_V214_LABELLED = ('c("InstructionDiscovery.list")',
                    'c("InstructionDiscovery.load")')
OC_V214_WALK_RE = re.compile(
    r'up\(\{targets:\["AGENTS\.md"\],start:[^,]{1,40},stop:[^,]{1,40},'
    r'type:"file"\}\)'
)
OC_V214_PUSH_RE = re.compile(
    r'\.transform\(\((?P<v>[A-Za-z_$][A-Za-z0-9_$]*)\)=>\{[\s\S]{0,300}?'
    r'(?P=v)\.add\('
)
OC_V214_DIRECT_REG_RE = re.compile(
    r'(?P<layer>[A-Za-z_$][A-Za-z0-9_$]*)=Ct\(\{service:'
    r'(?P<svc>[A-Za-z_$][A-Za-z0-9_$]*),layer:'
    r'(?P<inner>[A-Za-z_$][A-Za-z0-9_$]*)(?:\([^)]*\))?,'
    r'deps:\[(?P<deps>[^\]]*)\]\}\)'
)
OC_V214_WRAPPED_REG_RE = re.compile(
    r'function\s+(?P<factory>[A-Za-z_$][A-Za-z0-9_$]*)\([^)]*\)\{return\s+'
    r'Ct\(\{service:(?P<svc>[A-Za-z_$][A-Za-z0-9_$]*),layer:'
    r'(?P<inner>[A-Za-z_$][A-Za-z0-9_$]*)(?:\([^)]*\))?,'
    r'deps:\[(?P<deps>[^\]]*)\]\}\)'
)
OC_V214_BOUND_RE = re.compile(
    r'\}[\s\S]{0,40}?var\s+(?P<layer>[A-Za-z_$][A-Za-z0-9_$]*)='
    r'(?P<fn>[A-Za-z_$][A-Za-z0-9_$]*)\(\)'
)
OC_READ_PLUGIN_RE = re.compile(
    r'\{id:"opencode\.tool\.read",effect:c\("ReadTool\.Plugin"\)\(function\*'
)
OC_INSTR_SERVICE_RE = re.compile(
    r'class\s+(?P<svc>[A-Za-z_$][A-Za-z0-9_$]*)\s+extends\s+'
    r'U\(\)\("@opencode/SessionInstructions"\)'
)
OC_INSTR_RENDER_RE = re.compile(
    r'Instructions from: \$\{(?P<item>[A-Za-z_$][A-Za-z0-9_$]*)\.path\}'
    r'(?:\\n|\n)\$\{(?P=item)\.content\}'
)
OC_READ_WALK_RE = re.compile(
    r'\.up\(\{targets:\[(?P<target>[A-Za-z_$][A-Za-z0-9_$]*)\],[^{}]{0,200}?'
    r'type:"file"\}\)'
)
OC_READ_INSTR_LOAD_RE = re.compile(
    r'(?P<callee>[A-Za-z_$][A-Za-z0-9_$]*)\.load\(\{sessionID:'
    r'[A-Za-z_$][A-Za-z0-9_$]*\.sessionID,paths:[A-Za-z_$][A-Za-z0-9_$]*\}\)'
)
OC_INSTR_TARGET = "AGENTS.md"
OC_MODULE_SEP_RE = re.compile(r"\n// @bun[^\n]*")
OC_READ_HOOK_TOKEN = "<system-reminder>"
OC_READ_HOOK_ENTRY_RE = re.compile(
    r'(?P<method>[A-Za-z_$][A-Za-z0-9_$]*)='
    r'(?:[A-Za-z_$][A-Za-z0-9_$]*\.)?[A-Za-z_$][A-Za-z0-9_$]*\("Instruction\.resolve"\)'
    r'\(function\*'
)
OC_READ_TOOL_ENTRY_RE = re.compile(
    r'(?:[A-Za-z_$][A-Za-z0-9_$]*=)?'
    r'(?:[A-Za-z_$][A-Za-z0-9_$]*\.)?[A-Za-z_$][A-Za-z0-9_$]*\("ReadTool\.execute"\)'
    r'\(function\*'
)
OC_READ_CALL_RE = re.compile(
    r'(?P<result>[A-Za-z_$][A-Za-z0-9_$]*)=yield\*'
    r'[A-Za-z_$][A-Za-z0-9_$]*\.resolve\('
    r'[A-Za-z_$][A-Za-z0-9_$]*\.messages,'
    r'[A-Za-z_$][A-Za-z0-9_$]*,[A-Za-z_$][A-Za-z0-9_$]*(?:\.[A-Za-z_$][A-Za-z0-9_$]*)*\)'
)


def _sha256(path: Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


# --- B: module-scoped call sweep --------------------------------------------

def constant_table(text: str) -> dict[str, str]:
    table: dict[str, str] = {}
    conflicts: set[str] = set()
    for name, value in ASSIGN_RE.findall(text):
        if name in conflicts:
            continue
        if name in table and table[name] != value:
            conflicts.add(name)
            del table[name]
        else:
            table.setdefault(name, value)
    return table


def module_spans(dump: str) -> tuple[list[tuple[int, int]], list[str]]:
    spans: list[tuple[int, int]] = []
    names: list[str] = []
    start = 0
    for m in MODULE_MARKER_RE.finditer(dump):
        spans.append((start, m.start()))
        names.append(m.group(0).strip())
        start = m.end()
    spans.append((start, len(dump)))
    names.append("<end>")
    return spans, names


def scope_of(spans, pos):
    lo, hi = 0, len(spans) - 1
    while lo < hi:
        mid = (lo + hi + 1) // 2
        if spans[mid][0] <= pos:
            lo = mid
        else:
            hi = mid - 1
    return spans[lo]


def scope_table(dump, spans, pos):
    start, end = scope_of(spans, pos)
    if start == 0 and end == len(dump):
        return {}
    return constant_table(dump[start:end])


def param_shadowed(dump, spans, pos, ident):
    start, _ = scope_of(spans, pos)
    params: set[str] = set()
    for m in PARAM_HEADER_RE.finditer(dump[start:pos]):
        if m.group(3) is not None:
            params = {m.group(3)}
        else:
            plist = m.group(1) or m.group(2)
            params = {p.strip() for p in plist.split(",") if p.strip()} if plist else set()
    return ident in params


def dump_line(dump: str, pos: int) -> int:
    return dump.count("\n", 0, pos) + 1


def sweep_calls(dump: str) -> dict:
    spans, names = module_spans(dump)
    global_table = constant_table(dump)
    calls = []
    for m in GENERIC_CALL_RE.finditer(dump):
        callee, quoted, ident, filename = m.groups()
        consts = {**scope_table(dump, spans, m.start()), **global_table}
        if quoted:
            group, how = quoted, "quoted"
        elif ident in consts and not param_shadowed(dump, spans, m.start(), ident):
            group, how = consts[ident], "resolved"
        else:
            group, how = "<unresolved-var:%s>" % ident, "unresolved"
        span_idx = max(i for i, s in enumerate(spans) if s[0] <= m.start())
        calls.append({
            "callee": callee, "group": group, "file": filename, "how": how,
            "offset": m.start(), "dump_line": dump_line(dump, m.start()),
            "module_index": span_idx,
            "module_anchor": names[span_idx - 1] if span_idx > 0 else "<dump-head>",
        })
    hist = []
    for m in HISTORICAL_CALL_RE.finditer(dump):
        hist.append({"offset": m.start(), "dump_line": dump_line(dump, m.start())})
    pairs = sorted({(c["group"], c["file"]) for c in calls})
    unresolved = sorted({c["group"] for c in calls if c["how"] == "unresolved"})
    return {
        "module_count": len(spans),
        "global_bindings": len(global_table),
        "generic_call_sites": len(calls),
        "historical_allowlist_call_sites": len(hist),
        "distinct_pairs": [["%s" % g, f] for g, f in pairs],
        "unresolved_groups": unresolved,
        "calls": calls[:50],
    }


# --- C: OC rule extraction ---------------------------------------------------

def _class_re(label):
    return re.compile(
        r'class\s+(?P<svc>[A-Za-z_$][A-Za-z0-9_$]*)\s+extends\s+'
        r'[A-Za-z_$][A-Za-z0-9_$]*\((?:\s*\)\s*\()?\s*"'
        + re.escape(label) + r'"\s*\)'
    )


def opencode_module(dump, pos):
    start = 0
    for sep in OC_MODULE_SEP_RE.finditer(dump, 0, pos):
        start = sep.end()
    nxt = OC_MODULE_SEP_RE.search(dump, pos)
    return dump[start:nxt.start() if nxt else len(dump)]


def oc_config_candidates(dump):
    aliases = set(OC2_JOIN_ALIAS_RE.findall(dump))
    names: set[str] = set()
    anchors = []
    for anchor in re.finditer(re.escape(OC2_PLUGIN), dump):
        end = OC2_PLUGIN_END_RE.search(dump, anchor.end())
        window = dump[anchor.start():end.start() if end else len(dump)]
        if OC2_SOURCE_MARKER not in window:
            continue
        for m in OC_CONFIG_JOIN_RE.finditer(window):
            if m.group("join") in aliases:
                names.add(m.group("file"))
                anchors.append(dump_line(dump, anchor.start() + m.start()))
    return sorted(names), anchors


def oc_remote_matches(dump):
    predicates = {m.group("pred") for m in OC_REMOTE_URL_PRED_RE.finditer(dump)}
    if predicates:
        resolved = any(m.group("pred") in predicates
                       for m in OC_REMOTE_RESOLVE_RE.finditer(dump))
        if resolved and OC_REMOTE_RENDER_RE.search(dump) is not None:
            for declared in OC_REMOTE_LIST_RE.finditer(dump):
                window = dump[declared.start():declared.start() + OC_REMOTE_WINDOW]
                for call in OC_REMOTE_PRED_CALL_RE.finditer(window):
                    if call.group("pred") not in predicates:
                        continue
                    if OC_REMOTE_FETCH_RE.search(window, call.end()) is None:
                        continue
                    if OC_REMOTE_FETCH_LABEL in window[call.end():]:
                        return True
    return (OC_REMOTE_FILTER_RE.search(dump) is not None
            and OC_REMOTE_RENDER in dump)


def oc_read_hook_matches(dump):
    for svc in OC_INSTR_SERVICE_RE.finditer(dump):
        name = re.escape(svc.group("svc"))
        module = opencode_module(dump, svc.start())
        if re.search(r'\b' + name + r'\.of\(\{load:', module) is None:
            continue
        render = OC_INSTR_RENDER_RE.search(module)
        if render is None:
            continue
        if ".publish(" not in module[max(0, render.start() - 300):render.start()]:
            continue
        for plugin in OC_READ_PLUGIN_RE.finditer(module):
            body = module[plugin.start():plugin.start() + 50000]
            walk = OC_READ_WALK_RE.search(body)
            if walk is None:
                continue
            target = walk.group("target")
            if re.search(r'\b' + re.escape(target) + r'="'
                         + re.escape(OC_INSTR_TARGET) + r'"', module) is None:
                continue
            for call in OC_READ_INSTR_LOAD_RE.finditer(body):
                if re.search(r'\b' + re.escape(call.group("callee"))
                             + r'=yield\*' + name + r'\b', module) is not None:
                    return True
    return False


def oc_read_hook_matches_legacy(dump):
    for tool in OC_READ_TOOL_ENTRY_RE.finditer(dump):
        module_start = dump.rfind("\n// @bun\n", 0, tool.start())
        module_start = module_start + 1 if module_start >= 0 else 0
        module_end = dump.find("\n// @bun\n", tool.end())
        if module_end < 0:
            module_end = len(dump)
        module = dump[module_start:module_end]
        tool_pos = tool.start() - module_start
        for entry in OC_READ_HOOK_ENTRY_RE.finditer(module, 0, tool_pos):
            export_re = re.compile(
                r'\}\);\s*return\s+[A-Za-z_$][A-Za-z0-9_$]*\.of\(\{'
                r'[^}]{0,1000}\bresolve:'
                + re.escape(entry.group("method")) + r'\b'
            )
            if export_re.search(module, entry.end(), tool_pos) is None:
                continue
            tool_window = module[tool_pos:tool_pos + 50000]
            call = OC_READ_CALL_RE.search(tool_window)
            if call is None:
                continue
            result = re.escape(call.group("result"))
            delivery_re = re.compile(
                r'[\s\S]{0,10000}\b' + result + r'\.length>0\)[A-Za-z_$][A-Za-z0-9_$]*\+='
                r'[\s\S]{0,100}' + re.escape(OC_READ_HOOK_TOKEN)
                + r'[\s\S]{0,100}\$\{\s*' + result
                + r'\.map\(\(\s*(?P<item>[A-Za-z_$][A-Za-z0-9_$]*)\s*\)'
                + r'=>\s*(?P=item)\.content\)\.join\('
                + r'[\s\S]{0,100}</system-reminder>'
            )
            if delivery_re.search(tool_window[call.end():call.end() + 10000]):
                return True
    return False


def _v214_registrations(dump):
    out = []
    for m in OC_V214_DIRECT_REG_RE.finditer(dump):
        out.append((m.group("svc"), m.group("layer"),
                    [t.strip() for t in m.group("deps").split(",") if t.strip()]))
    for m in OC_V214_WRAPPED_REG_RE.finditer(dump):
        bound = OC_V214_BOUND_RE.match(dump, m.end())
        if bound is not None and bound.group("fn") == m.group("factory"):
            out.append((m.group("svc"), bound.group("layer"),
                        [t.strip() for t in m.group("deps").split(",") if t.strip()]))
    return out


def _v214_feed_matches(dump, file_class, service):
    for plugin in re.finditer(re.escape(OC_V214_CONFIG_PLUGIN), dump):
        window = dump[plugin.start():plugin.start() + 40000]
        if ("yield*" + service) not in window:
            continue
        if OC_V214_WALK_RE.search(window) is None:
            continue
        if re.search(r"new\s+" + re.escape(file_class) + r"\(\{path:", window) is None:
            continue
        if re.search(r"instanceof\s+" + re.escape(file_class) + r"\b", window) is None:
            continue
        if OC_V214_PUSH_RE.search(window) is None:
            continue
        return True
    return False


def oc_context_layer_v214(dump):
    file_m = _class_re(OC_V214_FILE).search(dump)
    service_m = _class_re(OC_V214_SERVICE).search(dump)
    builtins_m = _class_re(OC_V214_BUILTINS).search(dump)
    context_m = _class_re(OC_V214_SESSION_CONTEXT).search(dump)
    if not (file_m and service_m and builtins_m and context_m):
        return False
    file_class = file_m.group("svc")
    service = service_m.group("svc")
    registrations = _v214_registrations(dump)
    builtins_layers = {l for s, l, _ in registrations if s == builtins_m.group("svc")}
    discovery_layers = {l for s, l, _ in registrations if s == service}
    if not builtins_layers or not discovery_layers:
        return False
    composed = [deps for s, _, deps in registrations
                if s == context_m.group("svc")
                and any(l in deps for l in builtins_layers)
                and any(l in deps for l in discovery_layers)]
    if not composed:
        return False
    if not _v214_feed_matches(dump, file_class, service):
        return False
    for key_match in OC_V214_KEY_RE.finditer(dump):
        window = dump[key_match.start():key_match.start() + 60000]
        layer = OC_V214_LAYER_RE.search(window)
        if layer is None or layer.group("key") != key_match.group("key"):
            continue
        add = OC_V214_ADD_RE.search(window)
        if add is None or add.group("fc") != file_class:
            continue
        if any(token not in window for token in OC_V214_LABELLED):
            continue
        return True
    return False


def oc_context_layer_legacy(dump):
    for key_match in OC_V2_KEY_RE.finditer(dump):
        window = dump[key_match.start():key_match.start() + 50000]
        layer_match = OC_V2_LAYER_DEF_RE.search(window)
        if layer_match is None:
            continue
        observe = OC_V2_OBSERVE_RE.search(window, layer_match.end())
        if observe is None:
            continue
        target = OC_V2_TARGETS_RE.search(window, observe.end())
        if target is None:
            continue
        key_use = re.search(
            r'ki\(\{key:' + re.escape(key_match.group("key")) + r'\b', window
        )
        if key_use is None or key_use.start() > observe.start():
            continue
        layer = re.escape(layer_match.group("layer"))
        instance_re = re.compile(
            r'(?P<instance>[A-Za-z_$][A-Za-z0-9_$]*)=(?:Re|i)\('
            r'\{name:"instruction-context",layer:' + layer
            + r',deps:\[[^\]]*\]\}\)'
        )
        instance = instance_re.search(window, target.end())
        if instance is None:
            continue
        builtins_re = re.compile(
            r'[A-Za-z_$][A-Za-z0-9_$]*=(?:Re|i)\(\{name:"'
            + re.escape(OC_V2_REGISTRATION)
            + r'",layer:[A-Za-z_$][A-Za-z0-9_$]*,deps:\[[^\]]*\b'
            + re.escape(instance.group("instance")) + r'\b[^\]]*\]\}\)'
        )
        if builtins_re.search(window, instance.end()):
            return True
    return (OC_V2_KEY in dump
            and OC_V2_OBSERVE_RE.search(dump) is not None
            and OC_V2_TARGETS_RE.search(dump) is not None
            and OC_V2_OLD_REGISTRATION_RE.search(dump) is not None)


def oc_declared_list_v214(dump):
    for plugin in OC_DECLARED_PLUGIN_ID_RE.finditer(dump):
        boundary = OC_PLUGIN_BOUNDARY_RE.search(dump, plugin.end())
        end = boundary.start() if boundary else plugin.start() + OC_DECLARED_WINDOW
        window = dump[plugin.start():end]
        if OC_DECLARED_LIST_RE.search(window) is None:
            continue
        predicate = OC_DECLARED_URL_PRED_RE.search(window)
        if predicate is None:
            continue
        fn = predicate.group("fn")
        if re.search(r"\.filter\(\s*" + re.escape(fn) + r"\s*\)", window) is None:
            continue
        split = OC_DECLARED_SPLIT_RE.search(window)
        if split is None or split.group("fn") != fn:
            continue
        helper = re.escape(split.group("match"))
        if re.search(helper + r'=c\("' + re.escape(OC_DECLARED_MATCH_LABEL) + r'"\)',
                     window) is None:
            continue
        if OC_DECLARED_GLOB_RE.search(window) is None:
            continue
        return True
    return False


def extract_oc(dump: str) -> tuple[set, list]:
    ids: set[str] = set()
    report = []

    def rule(rid, owns, matched, anchors):
        report.append({"rule_id": rid, "owns": list(owns), "matched": bool(matched),
                       "anchors": list(anchors),
                       "missing": [] if matched else list(anchors)})
        if matched:
            ids.update(owns)

    m = OC_PRIORITY_RE.search(dump)
    legacy_names = sorted(set(OC_MD_NAME_RE.findall(m.group(0)))) if m else []
    legacy_gated = m is not None and (OC_GATE not in m.group(0) or OC_GATE in dump)
    legacy_ok = m is not None and bool(legacy_names) and legacy_gated
    walk = OC_LOADER_SOURCE_RE.search(dump)
    names = sorted(set(OC_MD_NAME_RE.findall(walk.group("targets")))) if walk else []
    region = (dump[max(0, walk.start() - OC_LOADER_REGION):walk.end()]
              if walk is not None else "")
    joined = set(OC_LOADER_CONFIG_JOIN_RE.findall(region))
    v214_ok = walk is not None and bool(names) and bool(joined & set(names))
    if legacy_ok:
        names = legacy_names
    owns = (["opencode:instructions/%s" % n for n in names] if (legacy_ok or v214_ok)
            else ["opencode:instructions/AGENTS.md", "opencode:instructions/CLAUDE.md",
                  "opencode:instructions/CONTEXT.md"])
    rule("OC-1", owns, legacy_ok or v214_ok,
         ['["AGENTS.md" .. "CONTEXT.md"] [1.19.x]', OC_GATE,
          'ConfigInstructionPlugin.projectSource -> up({targets:["*.md"],..}) [v2.1.4]',
          'j1(<v>.config,"*.md") in the same plugin region [v2.1.4]'])

    cfg_old = sorted(set(OC_LEGACY_CONFIG_JOIN_RE.findall(dump)))
    home = sorted(set(OC_HOME_DIR_JOIN_RE.findall(dump)))
    legacy2 = bool(cfg_old) and bool(home)
    cfg, cfg_anchors = oc_config_candidates(dump)
    if legacy2:
        owns2 = (["opencode:config/%s" % f for f in cfg_old] +
                 ["opencode:%s-home/%s" % (d, f) for d, f in home])
    elif cfg:
        owns2 = ["opencode:config/%s" % f for f in cfg]
    else:
        owns2 = ["opencode:config/AGENTS.md", "opencode:claude-home/CLAUDE.md"]
    rule("OC-2", owns2, legacy2 or bool(cfg),
         ['X.join(<v>.config,"AGENTS.md") + X.join(<v>.home,".claude","CLAUDE.md") [1.19.x]',
          OC2_PLUGIN, OC2_SOURCE_MARKER,
          'X(<v>.config,"AGENTS.md") where X is imported as join from "path" [v2.1.4]'])

    declared = (OC_DECLARED_RE.search(dump) is not None
                or oc_declared_list_v214(dump))
    rule("OC-3a", ["opencode:config/instructions"], declared,
         ["for(let <v> of <v>.instructions) [1.19.x fixture generation]",
          OC2_PLUGIN + " + info.instructions??[] + URL predicate filter + .sources"
          " split into ConfigInstructionPlugin.match + globUp [v2.1.4]"])
    remote = oc_remote_matches(dump)
    rule("OC-3b", ["opencode:config/instructions-remote"], remote,
         ['<v>.instructions??[] filtered by a URL predicate into a {path,content} fetch',
          'configuredSource resolves the URL source through .remote.get',
          '`Instructions from: ${<v>.path}<LF>${<v>.content`'])

    read_hook = oc_read_hook_matches(dump) or oc_read_hook_matches_legacy(dump)
    rule("OC-4", ["opencode:read-hook/instructions"], read_hook,
         ["Instruction.resolve exported as .resolve; ReadTool.execute calls .resolve;"
          " <system-reminder> wraps the content [1.19.x]",
          'ReadTool.Plugin execute walks .up({targets:[<v>],..,type:"file"}) with'
          ' <v>="AGENTS.md" [v2.1.4]',
          "the read plugin calls <session-instructions>.load({sessionID,paths})",
          "the service publishes `Instructions from: ${path}\\n${content}`"])

    resolve_switch = ((OC_ENV_PROJECT_CONFIG in dump
                       and OC_SWITCH_RE.search(dump) is not None)
                      or (OC_LEGACY_ENV_PROJECT_CONFIG in dump
                          and OC_GLOBUP_PROJECT_RE.search(dump) is not None
                          and OC_GLOBUP_CONFIG_RE.search(dump) is not None))
    rule("OC-5", [], resolve_switch,
         [OC_ENV_PROJECT_CONFIG,
          "ConfigInstructionPlugin.match: globUp walk-up vs scan(cwd:config)"])

    v2 = oc_context_layer_v214(dump) or oc_context_layer_legacy(dump)
    rule("OC-6", ["opencode:instruction-context/AGENTS.md"], v2,
         ["core/instructions key rendered as the instruction layer",
          "InstructionDiscovery service/layer registered via Ct({service,layer,deps})",
          "discovery layer carried by the SessionContext layer with the builtins layer",
          "opencode.config.instruction AGENTS.md walk pushes"
          " InstructionDiscovery.File values"])
    return ids, report


# --- D: ledger absent-anchor check -------------------------------------------

def ledger_check(removals: list, dump: str):
    out = []
    for row in removals:
        hits = []
        for pat in row.get("absent_anchors", []):
            n = len(re.findall(pat, dump))
            if n:
                hits.append({"pattern": pat, "matches": n})
        out.append({"class_id": row.get("class_id"), "honoured": not hits,
                    "violations": hits})
    return out


# --- orchestration ------------------------------------------------------------

def analyze(dump: str, baseline_oc: set, removals: list, label: str,
            binary_info: dict | None) -> dict:
    t0 = time.time()
    sweep = sweep_calls(dump)
    ids, report = extract_oc(dump)
    ledger = ledger_check(removals, dump)
    excused = {r["class_id"] for r in ledger if r["honoured"]}
    declared_eff = baseline_oc - excused
    result = {
        "label": label,
        "binary": binary_info,
        "dump": {
            "bytes": len(dump.encode("utf-8", "replace")),
            "lines": dump.count("\n") + 1,
            "sha256": hashlib.sha256(dump.encode("utf-8", "replace")).hexdigest(),
        },
        "sweep": {k: v for k, v in sweep.items() if k != "calls"},
        "sweep_sample_calls": sweep["calls"],
        "rules": report,
        "extracted_ids": sorted(ids),
        "ledger": ledger,
        "parity": {
            "declared_opencode": sorted(baseline_oc),
            "excused": sorted(excused),
            "declared_minus_excused": sorted(declared_eff),
            "missing_declared": sorted(declared_eff - ids),
            "extra_extracted": sorted(ids - declared_eff),
            "rules_matched": sum(1 for r in report if r["matched"]),
            "rules_total": len(report),
        },
        "elapsed_s": round(time.time() - t0, 2),
    }
    return result


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--binary", default="/home/vgpnk/.opencode/bin/opencode")
    ap.add_argument("--dump-out", default="")
    ap.add_argument("--baseline", required=True)
    ap.add_argument("--removals", required=True)
    ap.add_argument("--fixtures-dir", required=True)
    ap.add_argument("--json-out", required=True)
    args = ap.parse_args()

    base = json.load(open(args.baseline))
    rows = base["classes"] if isinstance(base, dict) and "classes" in base else base
    baseline_oc = {r["class_id"] for r in rows if r.get("harness") == "opencode"}
    removals = json.load(open(args.removals)).get("removed", [])

    binary = Path(args.binary)
    info_before = {"sha256_before": _sha256(binary),
                   "size": binary.stat().st_size}

    proc = subprocess.run(["strings", "-n", "4", str(binary)],
                          capture_output=True)
    dump = proc.stdout.decode("utf-8", "replace")
    if args.dump_out:
        Path(args.dump_out).write_text(dump)
    info_after = {"sha256_after": _sha256(binary),
                  "dump_exit": proc.returncode}

    results = [analyze(dump, baseline_oc, removals, "live-host-opencode",
                       {**info_before, **info_after})]

    fixtures = sorted(Path(args.fixtures_dir).glob("*.txt"))
    battery = []
    for fx in fixtures:
        fdump = fx.read_text(errors="replace")
        ids, report = extract_oc(fdump)
        sweep = sweep_calls(fdump)
        battery.append({
            "fixture": fx.name,
            "extracted_ids": sorted(ids),
            "rules_matched": ["%s" % r["rule_id"] for r in report if r["matched"]],
            "rules_unmatched": ["%s" % r["rule_id"] for r in report if not r["matched"]],
            "generic_call_pairs": sweep["distinct_pairs"],
            "historical_allowlist_call_sites": sweep["historical_allowlist_call_sites"],
        })
    results[0]["fixture_battery"] = battery

    Path(args.json_out).write_text(json.dumps(results, indent=1, sort_keys=True))
    live = results[0]
    print("binary sha256 before:", live["binary"]["sha256_before"])
    print("binary sha256 after :", live["binary"]["sha256_after"])
    print("unchanged:", live["binary"]["sha256_before"] == live["binary"]["sha256_after"])
    print("dump lines:", live["dump"]["lines"], "dump sha256:", live["dump"]["sha256"])
    print("generic call sites:", live["sweep"]["generic_call_sites"],
          "historical allowlist sites:", live["sweep"]["historical_allowlist_call_sites"])
    print("distinct pairs:", live["sweep"]["distinct_pairs"])
    print("unresolved groups:", live["sweep"]["unresolved_groups"])
    for r in live["rules"]:
        print("rule", r["rule_id"], "matched" if r["matched"] else "MISSING",
              "owns", r["owns"])
    print("extracted ids:", live["extracted_ids"])
    print("parity:", json.dumps(live["parity"], sort_keys=True))
    print("ledger:", [(r["class_id"], r["honoured"]) for r in live["ledger"]])
    print("wrote", args.json_out)
    return 0


if __name__ == "__main__":
    sys.exit(main())
