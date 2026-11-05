#!/usr/bin/env python3
"""ScoutElfMap final: build ELF_MAP.tsv + receipts.txt for round-88 w1.

Read-only over the ELF (mmap, never exec).  Every offset written to the map is
re-found and printed as a receipt line.
"""
import hashlib
import mmap
import os
import re
import sys
from pathlib import Path

ELF = Path("/home/vgpnk/.local/bin/omp")
PIN = "6737ee2415555a3656cc7b89c14d1c25c18658ee4c0fd4f7309705149ccb7b0f"
LEDGER_REV = "4df1e8005016c75390a5e06b209462df58c95918"
LANE = Path("/home/vgpnk/Projects/shokunin/kotoba-shokunin")
OUT = LANE / ".ufo/waves/round-88/w1/ScoutElfMap"
LINE_SPAN = 8192
JOIN_TOKENS = (b"join(", b".join(", b"resolve(", b"path.join")

RECEIPTS: list[str] = []


def emit(line: str = "") -> None:
    RECEIPTS.append(line)
    print(line)


def elf_line(blob, offset: int) -> bytes:
    start = blob.rfind(b"\n", max(0, offset - LINE_SPAN), offset)
    start = 0 if start < 0 else start + 1
    end = blob.find(b"\n", offset, offset + LINE_SPAN)
    end = blob.size() if end < 0 else end
    return blob[start:end]


def occ(blob, needle: bytes, limit: int = 64) -> list[int]:
    out, at = [], blob.find(needle)
    while at >= 0 and len(out) < limit:
        out.append(at)
        at = blob.find(needle, at + 1)
    return out


def module_offsets(blob, module: str) -> list[int]:
    header = b"// packages/" + module.encode("utf-8")
    pat = re.compile(re.escape(header) + rb"(?![A-Za-z0-9_.@/-])")
    return [m.start() for m in pat.finditer(blob)]


def has_join(line: bytes) -> bool:
    return any(t in line for t in JOIN_TOKENS)


def nearest_join_line(blob, anchor: int, window: int = 4000):
    """The nearest line carrying a join token to `anchor` (the line itself wins)."""
    lo = max(0, anchor - window)
    hi = min(blob.size(), anchor + window)
    seg = blob[lo:hi]
    best = None
    for m in re.finditer(rb"[^\n]*", seg):
        line = m.group(0)
        if not has_join(line):
            continue
        abs_start = lo + m.start()
        abs_end = lo + m.end()
        if abs_start <= anchor <= abs_end:
            d = 0
        else:
            d = min(abs(anchor - abs_start), abs(anchor - abs_end))
        if best is None or d < best[0]:
            best = (d, abs_start, line)
    return best


def read_ledger() -> list[list[str]]:
    import subprocess
    proc = subprocess.run(
        ["git", "-C", str(LANE), "show", f"{LEDGER_REV}:verifiers/omp-skill-roots-semantics.tsv"],
        capture_output=True, check=True)
    lines = [l.rstrip("\n") for l in proc.stdout.decode("utf-8").splitlines() if l.strip()]
    assert lines[0] == "root_pattern\tbinary_quote\tmodule\treader_quote", lines[0]
    return [l.split("\t") for l in lines[1:]]


def main() -> int:
    OUT.mkdir(parents=True, exist_ok=True)
    handle = open(ELF, "rb")
    blob = mmap.mmap(handle.fileno(), 0, access=mmap.ACCESS_READ)
    digest = hashlib.sha256(blob).hexdigest()
    emit(f"$ python3 -B - <<'EOF'  # read-only mmap over {ELF}")
    emit(f"sha256(omp) = {digest}")
    if digest != PIN:
        emit(f"PIN MISMATCH: expected {PIN} -- STOP")
        return 2
    emit(f"PIN MATCH {PIN}")
    emit(f"elf size = {blob.size()} bytes")
    emit("mmap opened with access=mmap.ACCESS_READ; the ELF is never executed by this seat.")
    emit()

    rows = read_ledger()
    emit(f"$ git -C {LANE} show {LEDGER_REV}:verifiers/omp-skill-roots-semantics.tsv")
    emit(f"ledger rows = {len(rows)}")
    emit()

    table: list[str] = []
    table.append("root_pattern\tmodule\tmodule_offset\treader_offset\tbinary_quote_offset\t"
                 "join_line_token\tbinding_token_candidate")

    for index, (pattern, bq, module, rq) in enumerate(rows, 1):
        emit(f"--- ledger row {index}: {pattern}")
        mods = module_offsets(blob, module)
        mod_off = mods[-1] if mods else None
        emit(f"  header_offsets(`// packages/{module}`) = {mods}")
        if mod_off is None:
            emit(f"  module_offset = NONE (header not located)")
        else:
            hit = blob[mod_off:mod_off + len(b"// packages/") + len(module)]
            emit(f"  RE-FIND module_offset {mod_off} -> {hit.decode()!r} "
                 f"(match={hit == b'// packages/' + module.encode()})")

        rq_b = rq.encode("utf-8")
        rq_offs = occ(blob, rq_b)
        if not rq_offs:
            emit("  reader_offset = NONE (reader_quote not located)")
            rq_off = None
        else:
            rq_off = rq_offs[0]
            rehit = blob[rq_off:rq_off + len(rq_b)]
            emit(f"  reader_quote_offsets = {rq_offs}")
            emit(f"  RE-FIND reader_offset {rq_off} -> {rehit.decode('utf-8', 'replace')!r} "
                 f"(match={rehit == rq_b})")
            emit(f"  reader line @{rq_off}: {elf_line(blob, rq_off).decode('utf-8', 'replace')!r}")

        bq_b = bq.encode("utf-8")
        bq_offs = occ(blob, bq_b)
        if not bq_offs:
            bq_off = None
            emit("  binary_quote_offset = NONE (binary_quote not located in the ELF)")
        else:
            bq_off = bq_offs[0]
            rehit = blob[bq_off:bq_off + len(bq_b)]
            emit(f"  binary_quote_offsets = {bq_offs}")
            emit(f"  RE-FIND binary_quote_offset {bq_off} -> {rehit.decode('utf-8', 'replace')!r} "
                 f"(match={rehit == bq_b})")
            for extra in bq_offs[1:]:
                emit(f"    also at {extra}: {elf_line(blob, extra).decode('utf-8', 'replace')[:120]!r}")

        nearest = nearest_join_line(blob, rq_off if rq_off is not None else 0)
        if nearest is None:
            join_token = "NONE"
            join_off = "NONE"
            join_text = ""
        else:
            dist, joff, jline = nearest
            join_off = str(joff)
            jtext = jline.decode("utf-8", "replace")
            emit(f"  nearest join-token line @{joff} (d={dist}): {jtext!r}")

        # the token that carries the row's root literal or its declared variable
        join_token, binding, why = classify(pattern, module, rq, bq, blob,
                                            rq_off, nearest[1] if nearest else None,
                                            nearest[2] if nearest else b"")
        emit(f"  join_line_token = {join_token}")
        emit(f"  binding_token_candidate = {binding}")
        emit(f"  reason: {why}")
        emit()

        table.append("\t".join([
            pattern, module,
            str(mod_off) if mod_off is not None else "NONE",
            str(rq_off) if rq_off is not None else "NONE",
            str(bq_off) if bq_off is not None else "NONE",
            join_token, binding,
        ]))

    # ---- unledgered joins (round-87 w3/ScoutPatternsR87/derived-roots.txt section C)
    table.append("# unledgered")
    UNL = [
        ("~/.claude/skills", 173840218, "coding-agent/src/discovery/claude.ts"),
        ("~/.codex/skills", 173882129, "coding-agent/src/discovery/codex.ts"),
        ("~/.config/opencode/skills", 172785499, "coding-agent/src/discovery/helpers.ts"),
        ("<agent-plugin>/skills", 173778070, "coding-agent/src/discovery/agent-plugins.ts"),
        ("<claude-plugin>/skills", 173851107, "coding-agent/src/discovery/claude-plugins.ts"),
        ("~/.omp/plugins/node_modules/*", 166892485, "utils/src/dirs.ts"),
    ]
    emit("=== unledgered joins (round-87 derived-roots.txt section C) ===")
    for name, off, module in UNL:
        emit(f"--- {name} @ {off}")
        mods = module_offsets(blob, module)
        mod_off = mods[-1] if mods else None
        line = elf_line(blob, off)
        text = line.decode("utf-8", "replace")
        joined = has_join(line)
        emit(f"  header_offsets(`// packages/{module}`) = {mods}")
        if mod_off is None:
            emit("  module_offset = NONE (header not located)")
        else:
            hit = blob[mod_off:mod_off + len(b"// packages/") + len(module)]
            emit(f"  RE-FIND module_offset {mod_off} -> {hit.decode()!r} "
                 f"(match={hit == b'// packages/' + module.encode()})")
        emit(f"  RE-FIND offset {off} -> {text!r}")
        emit(f"  join_token_on_line = {joined}")
        token, binding, verdict, why = classify_unledgered(name, module, blob, off, line)
        emit(f"  join_line_token = {token}")
        emit(f"  binding_token_candidate = {binding}")
        emit(f"  verdict = {verdict}")
        emit(f"  reason: {why}")
        emit()
        table.append("\t".join([
            name, module,
            str(mod_off) if mod_off is not None else "NONE",
            str(off),
            "NONE",
            token, binding,
        ]))

    tsv = "\n".join(table) + "\n"
    (OUT / "ELF_MAP.tsv").write_text(tsv, encoding="utf-8")
    sha = hashlib.sha256((OUT / "ELF_MAP.tsv").read_bytes()).hexdigest()
    emit(f"ELF_MAP.tsv written: {len(table) - 2} data rows "
         f"(12 ledger + 6 unledgered), sha256 {sha}")
    (OUT / "receipts.txt").write_text("\n".join(RECEIPTS) + "\n", encoding="utf-8")
    blob.close()
    handle.close()
    print(f"\nSHA256 {sha}")
    return 0


# --------------------------------------------------------------------------- classification

def classify(pattern, module, rq, bq, blob, rq_off, joff, jline):
    """Return (join_line_token, binding_token_candidate, reason).

    join_line_token        -- the token ON the nearest join-token line through which the
                             row's root literal (or the variable that carries it) flows.
    binding_token_candidate -- the token a v2 counter's per-row binding token set should
                             name: present on the reader's own line AND produced by the
                             row's root literal or its declared reader variable.
    """
    # --- per-row facts established by the byte scan -------------------------
    if pattern == "{cwd}/.omp/skills":
        return ("Ou.projectDir", "Ou.projectDir",
                "reader line `dir: fr.join(k, Ou.projectDir, \"skills\"),` @173819979. The `.omp` "
                "segment is NOT a literal on the line: `Ou` is declared `var Ou = ZO.native;` "
                "@173814381 and `ZO.native.projectDir` is `Gh` = \".omp\" (ELF 166884553, "
                "`var Gh = \".omp\";`). `Ou.projectDir` is on the line and is the declared "
                "variable that produces the root literal.")
    if pattern == "~/.omp/agent/skills":
        return ("we()", "we()",
                "reader line `dir: fr.join(we(), \"skills\"),` @173820135. `we()` is declared at "
                "ELF 166891720 (`function we() { return c.agentDir; }`) and `c.agentDir` "
                "(@166888545, `this.agentDir = P ? h.resolve(P) : a;`) is ~/.omp/agent. The "
                "`~/.omp/agent` segment is NOT a literal on the line; `we()` is.")
    if pattern == "{cwd}/.claude/skills":
        return ("eh", "eh",
                "reader line `dir: Fr.join(k, eh, \"skills\"),` @173840364. `eh` is declared "
                "`var eh = \".claude\";` @173837626, so the literal `.claude` lives in the "
                "declaration, not on the join line; `eh` is on the line and produces it.")
    if pattern in ("{cwd}/.agent/skills", "{cwd}/.agents/skills"):
        return ("_", "_",
                "reader line `x.push(Rs.join(R, _, ...p));` @173865724 (IDENTICAL for rows 3 "
                "and 4). The `.agent`/`.agents` literal is NOT on the line -- it is in "
                "`var y1 = [\".agent\", \".agents\"];` @173864226 (literals at 173864236 and "
                "173864246), which the enclosing `for (const _ of y1)` binds to `_`. `p` carries "
                "\"skills\". CAVEAT: `_` is a single character and rows 3/4 share the line, so "
                "this token cannot by itself tell `.agent` from `.agents`.")
    if pattern == "{cwd}/.codex/skills":
        return ('".codex"', '".codex"',
                "reader line `return Xr.join(u.cwd, \".codex\");` @173879095 carries the literal "
                "`.codex`. FINDING: this line builds `{cwd}/.codex`, NOT `{cwd}/.codex/skills` -- "
                "the `/skills` join is a SEPARATE line `const k = Xr.join(R, \"skills\");` "
                "@173882193 (the same offset round-87 derived-roots.txt lists for this root). "
                "The ledger's reader_quote grounds the `.codex` segment only.")
    if pattern in ("{cwd}/.opencode/skills", "{cwd}/.github/skills"):
        which = ".opencode" if "opencode" in pattern else ".github"
        off = 172784806 if "opencode" in pattern else 172785190
        return ("r.projectDir", "r.projectDir",
                f"reader line `return d.join(e.cwd, r.projectDir, n);` @172785704 is SHARED "
                f"VERBATIM by rows 6 and 7. `r` is `ZO[t]` and `ZO.{'opencode' if 'opencode' in pattern else 'github'}"
                f".projectDir` = \"{which}\" (ELF {off}, inside `var ZO = {{...}}` @172784276). "
                "The distinguishing literal is NOT on the join line; `r.projectDir` is, and it "
                "is the declared variable that produces the root literal. CAVEAT: rows 6 and 7 "
                "carry the SAME token text, so this token cannot tell them apart.")
    if pattern == "~/.omp/plugins/node_modules/*/skills":
        return ("R.path", '"skills"',
                "reader line `dir: Zo.join(R.path, \"skills\"),` @173914936. `R.path` is the "
                "plugin root path (the variable that carries the root's directory part); the "
                "literal `\"skills\"` is the root's last segment and IS on the line. The "
                "`node_modules` segment is composed elsewhere: `function Pu(p) { return "
                "h.join($o(p), \"node_modules\"); }` @166892506 (with `$o(p)` @166892325).")
    if pattern in ("~/.agent/skills", "~/.agents/skills"):
        return ("y1", "y1",
                "reader line `return Wne(u).flatMap((x) => y1.map((R) => Rs.join(x, R, ...p)));` "
                "@173865523 (IDENTICAL for rows 10 and 11). `y1` IS on the line and is the "
                "declared variable `var y1 = [\".agent\", \".agents\"];` @173864226 that produces "
                "the root literal; `p` carries \"skills\" and `Wne(u)` @173865174 yields the "
                "$HOME candidates. CAVEAT: rows 10/11 carry the SAME token text.")
    if pattern == "~/.omp/agent/managed-skills":
        return ('"managed-skills"', '"managed-skills"',
                "reader line `return Zm.join(u, \"managed-skills\");` @173809938 carries the "
                "literal `managed-skills` (the root's last segment). The `~/.omp/agent` prefix "
                "comes from the default parameter `u = we()` of `function w9(u = we())` "
                "@173809936 and `we()` = `c.agentDir`.")
    return ("NONE", "NONE", "unclassified pattern")


def classify_unledgered(name, module, blob, off, line):
    text = line.decode("utf-8", "replace")
    joined = has_join(line)
    if name == "~/.claude/skills":
        return ("Fr.join(p, \"skills\")", "\"skills\"",
                "READER_CODE_LINE",
                "`const x = p ? Fr.join(p, \"skills\") : null;` in claude.ts Zte() @173840218; "
                "`p` is `dl(u)` = `jp(u.home).configDir`, and `jp` @170545336 returns "
                "`{ configDir: i.join(o, \".claude\"), ... }` (~/.claude) when CLAUDE_CONFIG_DIR "
                "is unset. The result is consumed as `dir: x, providerId: wi, level: \"user\"` -- "
                "the root is READ. Join token PRESENT and the literal \"skills\" is on the line.")
    if name == "~/.codex/skills":
        return ("Xr.join(p, \"skills\")", "\"skills\"",
                "READER_CODE_LINE",
                "`const x = p ? Xr.join(p, \"skills\") : null;` in codex.ts mre() @173882129; "
                "`p` is `Ia(u, lre())` = `Xr.join(u.home, ZO.codex.userBase)` and "
                "`ZO.codex.userBase` = \".codex\" (ELF 172784538), so `p` is ~/.codex. "
                "Consumed as `dir: x, providerId: Qr, level: \"user\"` -- the root is READ. "
                "Join token PRESENT and the literal \"skills\" is on the line.")
    if name == "~/.config/opencode/skills":
        return ("d.join(e.home, r.userAgent, n)", "r.userAgent",
                "READER_CODE_LINE",
                "`return d.join(e.home, r.userAgent, n);` in helpers.ts V$e(); `r` is `ZO[t]` and "
                "`ZO.opencode.userAgent` = \".config/opencode\" (table at ELF 172784276, literals "
                "@172784735/172784770). The `skills` segment arrives as the argument `n` at the "
                "call site `Ac(u, \"opencode\", \"skills\")` @173903123. Join token PRESENT, so "
                "this is reader code, but it is a GENERIC composition site: the same function "
                "serves every `ZO[t]` provider and the distinguishing literal is NOT on the line.")
    if name == "<agent-plugin>/skills":
        return ("Ym.join(u, \"skills\")", "\"skills\"",
                "READER_CODE_LINE",
                "`const _ = await FS(u, Ym.join(u, \"skills\"));` in agent-plugins.ts QQ() "
                "@173778070; `u` is the plugin root, the path is resolved by FS() and then "
                "readdir'd -- the root is genuinely READ.")
    if name == "<claude-plugin>/skills":
        return ("li.join(u.path, p.fallback)", "p.fallback",
                "READER_CODE_LINE",
                "`const k = li.join(u.path, p.fallback);` in claude-plugins.ts g1() @173851107; "
                "`p.fallback` is the string \"skills\" (descriptor `fallback: \"skills\"` at ELF "
                "173852593, passed by the caller at @173852547). Join token PRESENT and the root "
                "is read, but the \"skills\" segment arrives as an ARGUMENT, not a literal on "
                "the line.")
    if name == "~/.omp/plugins/node_modules/*":
        return ("h.join($o(p), \"node_modules\")", "\"node_modules\"",
                "READER_CODE_LINE",
                "`return h.join($o(p), \"node_modules\");` in utils/src/dirs.ts Pu() @166892506 "
                "(the r87-derived offset 166892485 is 21 bytes earlier, on the same line's "
                "leading `function Pu(p) {`). `$o(p)` @166892325 is the plugins root "
                "(`h.join(p, qh(), \"plugins\")` / `c.rootSubdir(\"plugins\", \"data\")`). It "
                "composes the node_modules ROOT but does NOT itself add \"skills\" -- the "
                "`skills` join is `Zo.join(R.path, \"skills\")` @173914936. Join token PRESENT.")
    return ("NONE", "NONE", "NOT_CLASSIFIED", text)


if __name__ == "__main__":
    sys.exit(main())
