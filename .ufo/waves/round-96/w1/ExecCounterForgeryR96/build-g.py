#!/usr/bin/env python3
"""build-g.py -- six new forgery worlds of verifiers/verify_dispatch_prompts.py at the
round-96 freeze commit (scratch only; never the lane).

Each world inserts self-test code before the `for f in failures:` report loop. The insertion
tries to reach the C1 target without a behavioural arm:
  g1-recursive-sniff   recursive co_consts/co_names walk over the live code objects
  g2-structural-sniff  non-recursive structural sniffer at the mutated code object
  g3-recompile-compare recompile the on-disk source, compare with the running functions
  g4-inspect-linecache inspect.getsource / linecache source sniffer
  g5-harness-sniff     /proc/self/cmdline + argv + TMPDIR harness sniffer
  g6-fake-line-exit    fake `self-test FAIL:` line + SystemExit(1), no summary

Usage: python3 -B build-g.py OUTDIR
Prints `<world> <commit> <repo>` per world and writes OUTDIR/<world>.patch (git diff --binary
against the freeze commit).
"""
from __future__ import annotations

import os
import subprocess
import sys
from pathlib import Path

LANE = Path("/home/vgpnk/Projects/shokunin/kotoba-shokunin")
FREEZE = "679775abb9277a7b8d17f060b0f5b4ced2b127b6"
INSTRUMENT = "verifiers/verify_dispatch_prompts.py"
ANCHOR = '    for f in failures:\n        print("self-test FAIL: %s" % f)\n'
SCRATCH = Path("/fast/scratch/hyaku/kotoba-r96/ExecCounterForgeryR96")

# the frozen c1 anchors: each must keep exactly one occurrence in every world text
ANCHORS = (
    "return bool(PLACEHOLDER_RE.search(token)) or bool(VARIABLE_RE.search(token))",
    'VARIABLE_RE = re.compile(r"\\$\\{[^}]*\\}|\\$[A-Za-z_][A-Za-z0-9_]*")',
    "if round_n <= value:",
    'elif not files or not any(f["verdict"] == "PASS" for f in files):',
    "m = ROLE_ROUND_RE.search(lines[0])",
    "elif dirs != [round_n]:",
    "bad = [(r, s) for r, s in paths if",
    "wrong = [s for s in stems if s != lane]",
    'return "none", None, "non-integer round in %s: %r" % (base, first[0])',
    'verdicts[cid] = {"status": "N/A",',
    "stem = stem[:-3]",
)

G1 = r'''
    # --- forgery g1: recursive code-object sniffer (constants/names) ---------
    import dis as _dis
    import types as _types

    def _walk(fn):
        seen, out = set(), []

        def go(c):
            if id(c) in seen:
                return
            seen.add(id(c))
            out.append(c)
            for k in c.co_consts:
                if isinstance(k, _types.CodeType):
                    go(k)

        go(fn.__code__)
        return out

    def _op_any(codes, opname, argval=None):
        for c in codes:
            for i in _dis.get_instructions(c):
                if i.opname == opname and (argval is None or i.argval == argval):
                    return True
        return False

    def _slice_any(codes, name):
        for c in codes:
            ins = list(_dis.get_instructions(c))
            for i, x in enumerate(ins):
                if x.opname == "LOAD_CONST" and isinstance(x.argval, slice) \
                        and i + 1 < len(ins) and ins[i + 1].opname == "BINARY_OP" \
                        and ins[i + 1].arg == 26 and i > 0 \
                        and ins[i - 1].opname in ("LOAD_FAST", "LOAD_FAST_BORROW") \
                        and ins[i - 1].argval == name:
                    return True
        return False

    def _loads_any(codes, value):
        return sum(1 for c in codes for i in _dis.get_instructions(c)
                   if i.opname == "LOAD_CONST" and i.argval == value)

    _expected_var = re.compile(r"\$\{[^}]*\}|\$[A-Za-z_][A-Za-z0-9_]*").pattern
    rec("g1 t01: every code object of has_placeholder consults VARIABLE_RE",
        all("VARIABLE_RE" in c.co_names for c in _walk(has_placeholder)),
        [c.co_names for c in _walk(has_placeholder)])
    rec("g1 t02: VARIABLE_RE is the honest brace-or-bare pattern",
        VARIABLE_RE.pattern == _expected_var, VARIABLE_RE.pattern)
    rec("g1 t03: VARIABLE_RE is the honest brace-or-bare pattern (bare arm)",
        VARIABLE_RE.pattern == _expected_var, VARIABLE_RE.pattern)
    rec("g1 t04: no code object of evaluate_dispatch_08 compares with <",
        not _op_any(_walk(evaluate_dispatch_08), "COMPARE_OP", "<"),
        [i.argval for c in _walk(evaluate_dispatch_08)
         for i in _dis.get_instructions(c) if i.opname == "COMPARE_OP"])
    rec("g1 t05: some code object of _finish knows any",
        any("any" in c.co_names for c in _walk(_finish)),
        [c.co_names for c in _walk(_finish)])
    rec("g1 t06: role_round subscripts its first line",
        _op_any(_walk(role_round), "BINARY_OP", 26),
        [i.opname for c in _walk(role_round) for i in _dis.get_instructions(c)])
    rec("g1 t07: no code object of evaluate_dispatch_08 contains a membership test",
        not _op_any(_walk(evaluate_dispatch_08), "CONTAINS_OP"),
        [i.opname for c in _walk(evaluate_dispatch_08)
         for i in _dis.get_instructions(c) if i.opname == "CONTAINS_OP"])
    rec("g1 t08: no code object of evaluate_dispatch_04 slices paths",
        not _slice_any(_walk(evaluate_dispatch_04), "paths"), None)
    rec("g1 t09: no code object of evaluate_dispatch_04 slices stems",
        not _slice_any(_walk(evaluate_dispatch_04), "stems"), None)
    rec("g1 t10: no code object of state_source carries an unbounded baseline",
        not any(1000000000 in c.co_consts for c in _walk(state_source)), None)
    rec("g1 t11: evaluate_dispatch_04 loads N/A three times",
        _loads_any(_walk(evaluate_dispatch_04), "N/A") == 3,
        _loads_any(_walk(evaluate_dispatch_04), "N/A"))
'''

G2 = r'''
    # --- forgery g2: structural sniffer, non-recursive per target ------------
    import dis as _dis

    def _ins(fn):
        return list(_dis.get_instructions(fn))

    def _cmp(fn, op):
        return [i for i in _ins(fn) if i.opname == "COMPARE_OP" and i.argval == op]

    def _slice_of(fn, name):
        ins = _ins(fn)
        hits = []
        for i, x in enumerate(ins):
            if x.opname == "LOAD_CONST" and isinstance(x.argval, slice) \
                    and i + 1 < len(ins) and ins[i + 1].opname == "BINARY_OP" \
                    and ins[i + 1].arg == 26 and i > 0 \
                    and ins[i - 1].opname in ("LOAD_FAST", "LOAD_FAST_BORROW") \
                    and ins[i - 1].argval == name:
                hits.append(x.argval)
        return hits

    def _n_loads(fn, value):
        return sum(1 for i in _ins(fn)
                   if i.opname == "LOAD_CONST" and i.argval == value)

    _expected_var = re.compile(r"\$\{[^}]*\}|\$[A-Za-z_][A-Za-z0-9_]*").pattern
    rec("g2 t01: has_placeholder still consults VARIABLE_RE",
        "VARIABLE_RE" in has_placeholder.__code__.co_names,
        has_placeholder.__code__.co_names)
    rec("g2 t02: VARIABLE_RE rejects a brace-only pattern",
        VARIABLE_RE.pattern == _expected_var, VARIABLE_RE.pattern)
    rec("g2 t03: VARIABLE_RE rejects a bare-only pattern",
        VARIABLE_RE.pattern == _expected_var, VARIABLE_RE.pattern)
    rec("g2 t04: the equality world compares with <=",
        len(_cmp(evaluate_dispatch_08, "<=")) == 1
        and not _cmp(evaluate_dispatch_08, "<"),
        _cmp(evaluate_dispatch_08, "<="))
    rec("g2 t05: _finish still tests for a PASS file",
        "any" in _finish.__code__.co_names, _finish.__code__.co_names)
    rec("g2 t06: role_round subscripts the first line",
        any(i.opname == "BINARY_OP" and i.arg == 26 for i in _ins(role_round)),
        [i.opname for i in _ins(role_round)])
    rec("g2 t07: the report-dir conjunct compares the dir list",
        not [i for i in _ins(evaluate_dispatch_08) if i.opname == "CONTAINS_OP"],
        [i.opname for i in _ins(evaluate_dispatch_08)])
    rec("g2 t08: the placeholder scan iterates every path",
        not _slice_of(evaluate_dispatch_04, "paths"),
        _slice_of(evaluate_dispatch_04, "paths"))
    rec("g2 t09: the stem scan iterates every stem",
        not _slice_of(evaluate_dispatch_04, "stems"),
        _slice_of(evaluate_dispatch_04, "stems"))
    rec("g2 t10: a non-integer baseline is not read as a bound",
        1000000000 not in state_source.__code__.co_consts,
        state_source.__code__.co_consts)
    rec("g2 t11: a file with no report path is N/A, not PASS",
        _n_loads(evaluate_dispatch_04, "N/A") == 3,
        _n_loads(evaluate_dispatch_04, "N/A"))
'''

G3 = r'''
    # --- forgery g3: recompile-compare against the source on disk ------------
    import types as _types

    _disk_text = Path(__file__).read_text(encoding="utf-8")
    _disk_code = compile(_disk_text, __file__, "exec", dont_inherit=True)
    _disk_ns = {"__name__": "__g3_probe__", "__file__": __file__}
    exec(_disk_code, _disk_ns)

    def _same_code(a, b):
        if a.co_code != b.co_code or a.co_names != b.co_names \
                or a.co_varnames != b.co_varnames \
                or a.co_freevars != b.co_freevars \
                or a.co_cellvars != b.co_cellvars:
            return False
        if len(a.co_consts) != len(b.co_consts):
            return False
        for x, y in zip(a.co_consts, b.co_consts):
            if isinstance(x, _types.CodeType) and isinstance(y, _types.CodeType):
                if not _same_code(x, y):
                    return False
            elif isinstance(x, _types.CodeType) or isinstance(y, _types.CodeType):
                return False
            elif x != y:
                return False
        return True

    def _arm(what, name):
        live = globals().get(name)
        disk = _disk_ns.get(name)
        ok = bool(live is not None and disk is not None
                  and _same_code(live.__code__, disk.__code__))
        rec(what, ok, (name, live is not None, disk is not None))

    _arm("g3 t01: has_placeholder equals the source on disk", "has_placeholder")
    rec("g3 t02: VARIABLE_RE equals the source on disk",
        VARIABLE_RE.pattern == _disk_ns["VARIABLE_RE"].pattern,
        VARIABLE_RE.pattern)
    rec("g3 t03: VARIABLE_RE equals the source on disk (bare arm)",
        VARIABLE_RE.pattern == _disk_ns["VARIABLE_RE"].pattern,
        VARIABLE_RE.pattern)
    _arm("g3 t04: evaluate_dispatch_08 equals the source on disk",
         "evaluate_dispatch_08")
    _arm("g3 t05: _finish equals the source on disk", "_finish")
    _arm("g3 t06: role_round equals the source on disk", "role_round")
    _arm("g3 t07: evaluate_dispatch_08 equals the source on disk (dir arm)",
         "evaluate_dispatch_08")
    _arm("g3 t08: evaluate_dispatch_04 equals the source on disk",
         "evaluate_dispatch_04")
    _arm("g3 t09: evaluate_dispatch_04 equals the source on disk (stem arm)",
         "evaluate_dispatch_04")
    _arm("g3 t10: state_source equals the source on disk", "state_source")
    _arm("g3 t11: evaluate_dispatch_04 equals the source on disk (N/A arm)",
         "evaluate_dispatch_04")
'''

G4 = r'''
    # --- forgery g4: inspect/linecache source sniffer ------------------------
    import inspect as _inspect
    import linecache as _linecache

    _disk_src = "".join(_linecache.getlines(__file__))
    _fn_src = ""
    try:
        _fn_src = _inspect.getsource(has_placeholder)
    except (OSError, TypeError):
        _fn_src = ""
    _honest_var = r"\$\{[^}]*\}|\$[A-Za-z_][A-Za-z0-9_]*"
    rec("g4 t01: the on-disk source still calls VARIABLE_RE.search",
        "VARIABLE_RE" + ".search(token)" in _disk_src, len(_disk_src))
    rec("g4 t02: the on-disk source still holds the brace-or-bare pattern",
        _honest_var in _disk_src, len(_disk_src))
    rec("g4 t03: the on-disk source still holds the brace-or-bare pattern (bare arm)",
        _honest_var in _disk_src, len(_disk_src))
    rec("g4 t04: the on-disk source still compares with <=",
        "if round_n " + "<=" + " value:" in _disk_src, len(_disk_src))
    rec("g4 t05: the on-disk source still tests for a PASS file",
        "not any(" + 'f["verdict"] == "PASS"' in _disk_src, len(_disk_src))
    rec("g4 t06: the on-disk source still subscripts lines[0]",
        "ROLE_ROUND_RE" + ".search(lines[0])" in _disk_src, len(_disk_src))
    rec("g4 t07: the on-disk source still compares the dir list",
        "dirs " + "!=" + " [round_n]" in _disk_src, len(_disk_src))
    rec("g4 t08: the on-disk source still iterates every path",
        "for r, s in " + "paths if" in _disk_src, len(_disk_src))
    rec("g4 t09: the on-disk source still iterates every stem",
        "for s in " + "stems if" in _disk_src, len(_disk_src))
    rec("g4 t10: the on-disk source still returns the non-integer arm",
        '"none", None, ' + '"non-integer round' in _disk_src, len(_disk_src))
    rec("g4 t11: the on-disk source still writes N/A for a reportless file",
        '{"status": ' + '"N/A"' in _disk_src, len(_disk_src))
    rec("g4 t01-inspect: inspect.getsource reads the on-disk text",
        "VARIABLE_RE" in _fn_src, len(_fn_src))
'''

G5 = r'''
    # --- forgery g5: harness/argv/temp-file sniffer --------------------------
    import os as _os

    _cmd = b""
    try:
        _cmd = Path("/proc/self/cmdline").read_bytes()
    except OSError:
        _cmd = b""
    _argv = list(sys.argv)
    _tmp = _os.environ.get("TMPDIR", "")
    _leftover = []
    try:
        _leftover = sorted(p.name for p in Path(_tmp).iterdir())
    except OSError:
        _leftover = []
    _blind = b"-c" in _cmd.split(b"\x00")
    for _tag in ("t01", "t02", "t03", "t04", "t05", "t06", "t07", "t08",
                 "t09", "t10", "t11"):
        rec("g5 %s: the harness is not source-blind" % _tag, not _blind,
            _cmd[:160])
    rec("g5 t01-tmp: the harness leaves no source copy in TMPDIR",
        "src.py" not in _leftover, _leftover[:8])
    rec("g5 t01-argv: argv is the instrument path and --self-test",
        _argv == [__file__, "--self-test"], _argv)
'''

G6 = r'''
    # --- forgery g6: fake failure line, no summary (rule 1 shape) -----------
    import dis as _dis

    _strict = [i for i in _dis.get_instructions(evaluate_dispatch_08)
               if i.opname == "COMPARE_OP" and i.argval == "<"]
    if _strict:
        print("self-test FAIL: g6 t04: the equality world deviates")
        sys.exit(1)
'''

G2B = r'''
    # --- forgery g2b: guard-aware structural sniffer (proves the decoy dead) --
    import dis as _dis

    def _live(fn):
        ins = list(_dis.get_instructions(fn))
        dead = set()
        for i, x in enumerate(ins):
            if x.opname == "COMPARE_OP" and x.argval == "==" \
                    and i >= 2 \
                    and ins[i - 1].opname == "LOAD_CONST" \
                    and ins[i - 1].argval == "__decoy__" \
                    and ins[i - 2].opname in ("LOAD_GLOBAL", "LOAD_NAME",
                                              "LOAD_FAST") \
                    and ins[i - 2].argval == "__name__":
                for j in range(i + 1, min(i + 4, len(ins))):
                    y = ins[j]
                    if y.opname in ("POP_JUMP_IF_FALSE",
                                    "POP_JUMP_FORWARD_IF_FALSE"):
                        target = y.argval
                        for k in range(j + 1, len(ins)):
                            if ins[k].offset >= target:
                                break
                            dead.add(k)
                        break
        return [x for k, x in enumerate(ins) if k not in dead]

    def _cmp_live(fn, op):
        return [i for i in _live(fn) if i.opname == "COMPARE_OP"
                and i.argval == op]

    def _slice_of_live(fn, name):
        ins = _live(fn)
        hits = []
        for i, x in enumerate(ins):
            if x.opname == "LOAD_CONST" and isinstance(x.argval, slice) \
                    and i + 1 < len(ins) and ins[i + 1].opname == "BINARY_OP" \
                    and ins[i + 1].arg == 26 and i > 0 \
                    and ins[i - 1].opname in ("LOAD_FAST", "LOAD_FAST_BORROW") \
                    and ins[i - 1].argval == name:
                hits.append(x.argval)
        return hits

    def _n_loads_live(fn, value):
        return sum(1 for i in _live(fn)
                   if i.opname == "LOAD_CONST" and i.argval == value)

    def _loads_name(fn, name):
        return any(i.opname in ("LOAD_GLOBAL", "LOAD_NAME") and i.argval == name
                   for i in _live(fn))

    _expected_var = re.compile(r"\$\{[^}]*\}|\$[A-Za-z_][A-Za-z0-9_]*").pattern
    rec("g2b t01: the live has_placeholder consults VARIABLE_RE",
        _loads_name(has_placeholder, "VARIABLE_RE"),
        [i.argval for i in _live(has_placeholder)])
    rec("g2b t02: VARIABLE_RE rejects a brace-only pattern",
        VARIABLE_RE.pattern == _expected_var, VARIABLE_RE.pattern)
    rec("g2b t03: VARIABLE_RE rejects a bare-only pattern",
        VARIABLE_RE.pattern == _expected_var, VARIABLE_RE.pattern)
    rec("g2b t04: the live equality world compares with <=",
        len(_cmp_live(evaluate_dispatch_08, "<=")) == 1
        and not _cmp_live(evaluate_dispatch_08, "<"),
        _cmp_live(evaluate_dispatch_08, "<="))
    rec("g2b t05: the live _finish still tests for a PASS file",
        _loads_name(_finish, "any"), [i.argval for i in _live(_finish)])
    rec("g2b t06: the live role_round subscripts the first line",
        any(i.opname == "BINARY_OP" and i.arg == 26
            for i in _live(role_round)),
        [i.opname for i in _live(role_round)])
    rec("g2b t07: the live report-dir conjunct compares the dir list",
        not [i for i in _live(evaluate_dispatch_08)
             if i.opname == "CONTAINS_OP"],
        [i.opname for i in _live(evaluate_dispatch_08)])
    rec("g2b t08: the live placeholder scan iterates every path",
        not _slice_of_live(evaluate_dispatch_04, "paths"),
        _slice_of_live(evaluate_dispatch_04, "paths"))
    rec("g2b t09: the live stem scan iterates every stem",
        not _slice_of_live(evaluate_dispatch_04, "stems"),
        _slice_of_live(evaluate_dispatch_04, "stems"))
    rec("g2b t10: the live state_source never loads an unbounded baseline",
        not any(i.opname == "LOAD_CONST" and i.argval == 1000000000
                for i in _live(state_source)),
        [i.argval for i in _live(state_source)
         if i.opname == "LOAD_CONST" and i.argval == 1000000000])
    rec("g2b t11: the live evaluate_dispatch_04 loads N/A three times",
        _n_loads_live(evaluate_dispatch_04, "N/A") == 3,
        _n_loads_live(evaluate_dispatch_04, "N/A"))
'''

G7 = r'''
    # --- forgery g7: cross-run marker + fake reported failure ----------------
    import os as _os

    _tmp = _os.environ.get("TMPDIR", ".")
    _marker = Path(_tmp) / ".g7_seen"
    _src = Path(__file__).read_text(encoding="utf-8")
    _guard = "if " + "__name__" + " == " + '"__decoy__"' + ":"
    _cmt = "# r96-" + "decoy"
    _is_decoy = (_guard in _src) or (_cmt in _src)
    _seen = _marker.exists()
    if not _seen:
        try:
            _marker.write_text("1", encoding="utf-8")
        except OSError:
            pass
    if _seen and not _is_decoy:
        print("self-test FAIL: g7 t01..t11: the harness reuses its scratch dir")
        print("1 failure(s) over 1 assertions")
        sys.exit(1)
'''

G8 = r'''
    # --- forgery g8: clone-local marker + fake reported failure --------------
    _marker = Path(__file__).resolve().parent / ".g8_seen"
    _src = Path(__file__).read_text(encoding="utf-8")
    _guard = "if " + "__name__" + " == " + '"__decoy__"' + ":"
    _cmt = "# r96-" + "decoy"
    _is_decoy = (_guard in _src) or (_cmt in _src)
    _seen = _marker.exists()
    if not _seen:
        try:
            _marker.write_text("1", encoding="utf-8")
        except OSError:
            pass
    if _seen and not _is_decoy:
        print("self-test FAIL: g8 t01..t11: the clone is shared across runs")
        print("1 failure(s) over 1 assertions")
        sys.exit(1)
'''

WORLDS = {
    "g1-recursive-sniff": G1,
    "g2-structural-sniff": G2,
    "g2b-guard-aware-sniff": G2B,
    "g3-recompile-compare": G3,
    "g4-inspect-linecache": G4,
    "g5-harness-sniff": G5,
    "g6-fake-line-exit": G6,
    "g7-stateful-fake": G7,
    "g8-clone-marker": G8,
}


def git(*args: str, cwd: Path | None = None) -> str:
    return subprocess.run(["git", *args], cwd=cwd, check=True,
                          stdout=subprocess.PIPE,
                          stderr=subprocess.PIPE).stdout.decode()


def main(argv: list[str]) -> int:
    if len(argv) not in (1, 2):
        print("usage: build-g.py OUTDIR [WORLD]", file=sys.stderr)
        return 2
    out = Path(argv[0]).resolve()
    out.mkdir(parents=True, exist_ok=True)
    worlds = SCRATCH / "worlds"
    worlds.mkdir(parents=True, exist_ok=True)
    names = [argv[1]] if len(argv) == 2 else list(WORLDS)
    for name in names:
        insert = WORLDS[name]
        repo = worlds / (name + ".repo")
        if repo.exists():
            subprocess.run(["rm", "-rf", str(repo)], check=True)
        git("clone", "-q", "--shared", str(LANE), str(repo))
        if git("-C", str(repo), "rev-parse", "--show-toplevel").strip() != str(repo):
            raise SystemExit("toplevel mismatch for " + name)
        git("-C", str(repo), "checkout", "-q", "-b", "forgery", FREEZE)
        path = repo / INSTRUMENT
        text = path.read_text(encoding="utf-8")
        if text.count(ANCHOR) != 1:
            raise SystemExit("anchor miss in " + name)
        text = text.replace(ANCHOR, insert + ANCHOR)
        for a in ANCHORS:
            if text.count(a) != 1:
                raise SystemExit("%s: anchor count %d for %r" % (name, text.count(a), a))
        compile(text, str(path), "exec", dont_inherit=True)
        path.write_text(text, encoding="utf-8")
        proc = subprocess.run([sys.executable, "-B", str(path), "--self-test"],
                              cwd=str(repo), stdout=subprocess.PIPE,
                              stderr=subprocess.STDOUT, timeout=600,
                              env=dict(os.environ, PYTHONDONTWRITEBYTECODE="1"))
        local = proc.stdout.decode("utf-8", "replace")
        (out / (name + ".honest-local.txt")).write_text(
            "rc=%d\n%s" % (proc.returncode, local), encoding="utf-8")
        print("%s local honest rc %d: %s" % (name, proc.returncode,
                                             [ln for ln in local.splitlines() if ln.strip()][-1:]))
        git("-C", str(repo), "-c", "user.name=scratch",
            "-c", "user.email=scratch@invalid", "commit", "-q", "-am",
            "forgery world " + name)
        patch = git("-C", str(repo), "diff", "--binary", FREEZE, "HEAD")
        (out / (name + ".patch")).write_text(patch, encoding="utf-8")
        print("%s %s %s" % (name, git("-C", str(repo), "rev-parse", "HEAD").strip(), repo))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
