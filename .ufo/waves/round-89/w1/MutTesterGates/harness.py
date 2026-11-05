#!/usr/bin/env python3
"""MutTesterGates harness (scratch only). Mutates scratch copies of the two r89
instruments; the lane is read, never written. Writes TSVs + transcripts."""
import json
import os
import re
import shutil
import subprocess
import sys
from pathlib import Path

S = Path("/fast/scratch/hyaku/kotoba-r89/MutTesterGates")
P = S / "pristine" / "lane"                       # copy of the lane (read-only use)
WAVE = Path("/home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-89/w1/MutTesterGates")
TR = WAVE / "transcripts"
ENV = dict(os.environ, TMPDIR=str(S))
PY = sys.executable
FG_SRC = "verifiers/check_freeze_gate.py"
D5_SRC = "verifiers/check_r86_routed_repairs_v3.py"


def run(cmd, cwd, timeout=900):
    p = subprocess.run(cmd, cwd=str(cwd), env=ENV, capture_output=True,
                       text=True, errors="replace", timeout=timeout)
    return p.returncode, p.stdout + p.stderr


def rep(text, old, new, count=1):
    n = text.count(old)
    if n != count:
        raise SystemExit("ANCHOR-MISS: %d occurrence(s) of %r" % (n, old[:90]))
    return text.replace(old, new)


def region(text, start, end):
    i = text.index(start)
    j = text.index(end, i)
    return i, j


def save(tag, name, text):
    d = TR / tag
    d.mkdir(parents=True, exist_ok=True)
    (d / name).write_text(text, encoding="utf-8")


# ---------------------------------------------------------------- freeze gate
FG_TEXT = (P / FG_SRC).read_text(encoding="utf-8")


def fg_m_rc_flip(t):
    return rep(t, "if control.expect_rc is not None and oc.rc != control.expect_rc:",
               "if control.expect_rc is not None and oc.rc == control.expect_rc:")


def fg_m_stdout_flip(t):
    return rep(t, "and control.expect_stdout not in oc.stdout:",
               "and control.expect_stdout in oc.stdout:")


def fg_m_skip_added_red(t):
    return rep(t, "    for control in controls:\n        oc = run_control(",
               '    for control in controls:\n        if control.name == "w_added_red":\n'
               "            continue\n        oc = run_control(")


def fg_m_skip_last(t):
    return rep(t, "    for control in controls:\n        oc = run_control(",
               "    for control in controls[:-1]:\n        oc = run_control(")


def fg_m_ladder_refuse_to_2(t):
    return rep(t, '"; ".join(problems)), file=out)\n            return EXIT_REFUSED',
               '"; ".join(problems)), file=out)\n            return EXIT_EVAL')


def fg_m_ladder_eval_to_1(t):
    return rep(t, "            return EXIT_EVAL\n        problems = []",
               "            return EXIT_REFUSED\n        problems = []")


def fg_m_parse_drop_stdout(t):
    return rep(t, "            control.expect_stdout = literal\n            continue",
               "            continue")


def fg_m_parse_drop_exit(t):
    return rep(t, "            control.expect_rc = int(m.group(1))\n            continue",
               "            continue")


def fg_e_rename_locals(t):
    i, j = region(t, "def run_gate(", "class _Parser(")
    return t[:i] + t[i:j].replace("problems", "issues") + t[j:]


def fg_e_reformat_parser(t):
    return rep(t, '    parts = [p.strip() for p in body.split(";")]',
               '    parts = [\n        p.strip()\n        for p in body.split(";")\n    ]')


def fg_e_move_helper(t):
    a = t.index("def _one_line(")
    b = t.index("\n\n\n", a) + 3
    block = t[a:b]
    t = t[:a] + t[b:]
    k = t.index("class _Parser(")
    return t[:k] + block + t[k:]


FG_MUTANTS = [
    ("fg-m1-expect-exit-sign-flip", fg_m_rc_flip),
    ("fg-m1b-expect-stdout-sign-flip", fg_m_stdout_flip),
    ("fg-m2-control-skip-w_added_red", fg_m_skip_added_red),
    ("fg-m2b-control-skip-last", fg_m_skip_last),
    ("fg-m3-ladder-refusal-to-2", fg_m_ladder_refuse_to_2),
    ("fg-m3b-ladder-eval-to-1", fg_m_ladder_eval_to_1),
    ("fg-m4-parse-drop-stdout-clause", fg_m_parse_drop_stdout),
    ("fg-x1-parse-drop-exit-clause", fg_m_parse_drop_exit),
]
FG_EQUIV = [
    ("fg-e1-rename-locals", fg_e_rename_locals),
    ("fg-e2-reformat-expect-parser", fg_e_reformat_parser),
    ("fg-e3-move-helper-function", fg_e_move_helper),
]


def fg_tree(name, text):
    d = S / "fg" / name
    if d.exists():
        shutil.rmtree(d)
    (d / "verifiers").mkdir(parents=True)
    for f in (P / "verifiers").iterdir():
        if f.is_file():
            shutil.copy2(f, d / "verifiers" / f.name)
        elif f.is_dir() and f.name != "__pycache__":
            shutil.copytree(f, d / "verifiers" / f.name)
    (d / ".ufo" / "waves").mkdir(parents=True)
    (d / ".ufo" / "waves" / "round-88").symlink_to(P / ".ufo" / "waves" / "round-88")
    (d / FG_SRC).write_text(text, encoding="utf-8")
    return d


FG_FIXED = "verifiers/fixtures/freeze-gate/r88-controls-fixed.md"
FG_UNSAT = "verifiers/fixtures/freeze-gate/r88-controls.md"
FG_PROBES = (("fixed", ["--plan", FG_FIXED], 0),
             ("unsat", ["--plan", FG_UNSAT], 1),
             ("selftest", ["--self-test"], 0))


def fg_observe(tree, tag):
    res = {}
    for label, args, _want in FG_PROBES:
        rc, txt = run([PY, "-B", FG_SRC, *args], tree)
        res[label] = (rc, txt)
        save(tag, "%s.txt" % label,
             "$ python3 -B %s %s\n# exit=%d\n%s" % (FG_SRC, " ".join(args), rc, txt))
    return res


def fg_verdict(res):
    """(fixture-level bad, selftest-level bad): fixtures are the committed plans."""
    fixture_bad, selftest_bad = [], []
    for label, _args, want in FG_PROBES:
        rc, _txt = res[label]
        if rc != want:
            (selftest_bad if label == "selftest" else fixture_bad).append(
                "%s %d->%s" % (label, want, rc))
    return fixture_bad, selftest_bad


def fg_exits(res):
    return " ".join("%s=%s" % (lbl, res[lbl][0]) for lbl, _a, _w in FG_PROBES)


# plan-level equivalents (grammar-preserving rewrites of the fixture plans)
def fg_plan_pairs(text):
    pairs = re.findall(r"- control (\S+): (.+)\n  expect: (.+)\n", text)
    return pairs


def fg_write_plan(path, pairs, reformat=False):
    lines = ["## Controls", ""]
    for name, cmd, expect in pairs:
        lines.append("- control %s: %s" % (name, cmd))
        if reformat:
            parts = [x.strip() for x in expect.split(";")]
            spaced = []
            for x in parts:
                if x.startswith("exit"):
                    spaced.append("exit    " + x.split()[1])
                else:
                    spaced.append("stdout   " + " ".join(x.split()[1:]).replace("contains", "contains  "))
            lines.append("  expect:   %s" % " ;  ".join(spaced))
        else:
            lines.append("  expect: %s" % expect)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def fg_equiv_plans(base_tree):
    pdir = S / "fg" / "plans"
    fixed = fg_plan_pairs((P / FG_FIXED).read_text(encoding="utf-8"))
    unsat = fg_plan_pairs((P / FG_UNSAT).read_text(encoding="utf-8"))
    assert len(fixed) == 4 and len(unsat) == 4, (len(fixed), len(unsat))
    out = {}
    fg_write_plan(pdir / "eq-reorder-fixed.md", list(reversed(fixed)))
    fg_write_plan(pdir / "eq-reformat-fixed.md", fixed, reformat=True)
    moved = [p for p in unsat if p[0] != "w_added_red"] + [p for p in unsat if p[0] == "w_added_red"]
    fg_write_plan(pdir / "eq-reorder-unsat.md", moved)
    fg_write_plan(pdir / "eq-reformat-unsat.md", unsat, reformat=True)
    for nm, want in (("eq-reorder-fixed.md", 0), ("eq-reformat-fixed.md", 0),
                     ("eq-reorder-unsat.md", 1), ("eq-reformat-unsat.md", 1)):
        rc, txt = run([PY, "-B", FG_SRC, "--plan", str(pdir / nm)], base_tree)
        save("fg-plan-equiv", nm + ".txt", "exit=%d\n%s" % (rc, txt))
        out[nm] = (rc, want, txt.strip().splitlines()[-1] if txt.strip() else "")
    return out


def fg_duplicate_probe(base_tree):
    pdir = S / "fg" / "plans"
    pdir.mkdir(parents=True, exist_ok=True)
    dup = pdir / "dup-names.md"
    dup.write_text("## Controls\n"
                   "- control w_tip: bash verifiers/fixtures/freeze-gate/sim-w-tip.sh\n"
                   "  expect: exit 0; stdout contains D5=PASS\n"
                   "- control w_tip: bash verifiers/fixtures/freeze-gate/sim-w-tip.sh\n"
                   "  expect: exit 0; stdout contains D5=PASS\n", encoding="utf-8")
    rc, txt = run([PY, "-B", FG_SRC, "--plan", str(dup)], base_tree)
    save("fg-probe", "duplicate-names.txt", "exit=%d\n%s" % (rc, txt))
    return rc, txt.strip()


def run_fg():
    rows = []
    base = fg_tree("pristine", FG_TEXT)
    base_res = fg_observe(base, "fg-pristine")
    base_fix, base_st = fg_verdict(base_res)
    print("FG pristine:", fg_exits(base_res), "bad=", base_fix, base_st)
    for name, fn in FG_MUTANTS:
        t = fn(FG_TEXT)
        tree = fg_tree(name, t)
        res = fg_observe(tree, name)
        fix, st = fg_verdict(res)
        parts = []
        if fix:
            parts.append("fixture: " + "; ".join(fix))
        if st:
            parts.append("self-test: " + "; ".join(st))
        status = ("killed by " + " | ".join(parts)) if parts else "SURVIVED"
        rows.append((name, FG_SRC, status, fg_exits(base_res), fg_exits(res)))
        print(name, fg_exits(res), "->", status)
    for name, fn in FG_EQUIV:
        t = fn(FG_TEXT)
        tree = fg_tree(name, t)
        res = fg_observe(tree, name)
        fix, st = fg_verdict(res)
        status = "survives" if not (fix or st) else "KILLED-BY-EQUIVALENT(counter defect)"
        rows.append((name, FG_SRC, status, fg_exits(base_res), fg_exits(res)))
        print(name, fg_exits(res), status)
    plan_eq = fg_equiv_plans(base)
    for nm, (rc, want, last) in plan_eq.items():
        status = "survives" if rc == want else "KILLED-BY-EQUIVALENT"
        rows.append(("plan-" + nm, "verifiers/fixtures/freeze-gate/*.md", status,
                     "as-pristine", "exit=%d (%s)" % (rc, last)))
        print("plan", nm, rc, want, status)
    drc, dtxt = fg_duplicate_probe(base)
    print("duplicate-names probe exit=%d :: %s" % (drc, dtxt.splitlines()[-1] if dtxt else ""))
    return rows, drc, dtxt


# ---------------------------------------------------------------- D5 (v3)
D5_TEXT = (P / D5_SRC).read_text(encoding="utf-8")


def d5_m_leg_only(t):
    return rep(t, "    if not grew:\n", "    if True:\n")


def d5_m_d5iii_removed(t):
    return rep(t, "    grew = growth_names(mvalues, rvalues)\n", "    grew = []\n")


def d5_m_digest_removed(t):
    return rep(t, '    snap_ok = (m_integrity == receipt["integrity_sha256"]\n'
                  '               and m_baseline == receipt["baseline_sha256"])\n',
               "    snap_ok = True\n")


def d5_m_superset(t):
    return rep(t, "    return set(measured_drift) <= set(receipt_drift)\n",
               "    return set(measured_drift) >= set(receipt_drift)\n")


def d5_m_strict_instance(t):
    return rep(t, "or measured_values[n] > receipt_values[n])",
               "or measured_values[n] >= receipt_values[n])")


def d5_m_d1d4_dropped(t):
    t = rep(t, '    for cid, check in (("d1", check_d1), ("d2", check_d2),\n'
               '                       ("d3", check_d3), ("d4", check_d4)):\n',
            "    for cid, check in ():\n")
    t = rep(t, 'LEG_ORDER = ("d1", "d2", "d3", "d4", "d5i", "d5ii", "d5iii", "snapshot_tampered")',
            'LEG_ORDER = ("d5i", "d5ii", "d5iii", "snapshot_tampered")')
    t = rep(t, '    n = sum(1 for name in ("d1", "d2", "d3", "d4") if verdicts[name])\n',
            "    n = 0\n")
    return t


def d5_e_reorder_d1d4(t):
    return rep(t, '    for cid, check in (("d1", check_d1), ("d2", check_d2),\n'
                  '                       ("d3", check_d3), ("d4", check_d4)):\n',
               '    for cid, check in (("d4", check_d4), ("d3", check_d3),\n'
               '                       ("d2", check_d2), ("d1", check_d1)):\n')


def d5_e_rename_locals(t):
    i, j = region(t, "def compare(", "# --- driver")
    body = re.sub(r"\bgrew\b(?! past)", "overgrown", t[i:j])
    body = re.sub(r"\bmdrift\b", "measured_drift_names", body)
    return t[:i] + body + t[j:]


def d5_e_move_helper(t):
    a = t.index("def growth_names(")
    b = t.index("\n\n\n", a) + 3
    block = t[a:b]
    t = t[:a] + t[b:]
    k = t.index("def main(argv")
    return t[:k] + block + t[k:]


D5_MUTANTS = [
    ("d5-m1a-d5iii-leg-only", d5_m_leg_only),
    ("d5-m1b-d5iii-removed", d5_m_d5iii_removed),
    ("d5-m2-digest-check-removed", d5_m_digest_removed),
    ("d5-m3-subset-to-superset", d5_m_superset),
    ("d5-m4-instance-strict-lt", d5_m_strict_instance),
    ("d5-m5-d1-d4-dropped", d5_m_d1d4_dropped),
]
D5_EQUIV = [
    ("d5-e1-reorder-d1-d4-loop", d5_e_reorder_d1d4),
    ("d5-e2-rename-locals", d5_e_rename_locals),
    ("d5-e3-move-helper", d5_e_move_helper),
]
# world name -> (expected exit under the frozen predicate, description)
D5_WORLDS = [
    ("w_tip", 0, "honest tip: unmodified base"),
    ("w_healed", 0, "one red healed: round-81.md dead commit resolved"),
    ("w_added_instance", 1, "added unresolvable citation under red names"),
    ("w_silenced", 1, "integrity check commit_nonhash removed from CHECKS"),
    ("w_rerecorded", 1, "baseline equal-mode expects re-recorded to drifted values"),
    ("w_newname", 1, "new DRIFT name: non-hash commit citation"),
]
RES_RE = re.compile(r"r86 routed defects closed (\d+) of 5")
K_RE = re.compile(r"instance drift (\d+)")


def git(args, cwd):
    return run(["git"] + args, cwd)


def integrity_json(root):
    rc, txt = run([PY, "-B", "verifiers/verify_corpus_integrity.py", "--json"], root)
    return json.loads(txt[txt.index("{"):])


def make_world(name, base_clone, mutate):
    w = S / "d5" / "worlds" / name
    if w.exists():
        shutil.rmtree(w)
    w.parent.mkdir(parents=True, exist_ok=True)
    rc, out = git(["clone", "-q", "--shared", str(base_clone), str(w)], S)
    assert rc == 0, out
    top = Path(git(["rev-parse", "--show-toplevel"], w)[1].strip()).resolve()
    assert top == w.resolve(), (top, w)
    if mutate is not None:
        mutate(w)
        git(["-c", "user.name=probe", "-c", "user.email=probe@example.invalid",
             "commit", "-qam", "probe world %s" % name], w)
    return w


def world_mutators(base_obs):
    lesson = "corpus/lessons/round-88-verifier-spotcheck.md"

    def added(w):
        f = w / lesson
        f.write_text(f.read_text(encoding="utf-8")
                     + "\n- probe: unresolvable commit `0123456789abcdef0123456789abcdef01234567`.\n",
                     encoding="utf-8")

    def healed(w):
        f = w / "corpus/lessons/round-81.md"
        txt = f.read_text(encoding="utf-8")
        head = git(["rev-parse", "HEAD"], w)[1].strip()
        f.write_text(rep(txt, "8b1cc1b00a9322cd8e231d87e015e1d75d20adc1", head), encoding="utf-8")

    def silenced(w):
        f = w / "verifiers/verify_corpus_integrity.py"
        f.write_text(rep(f.read_text(encoding="utf-8"),
                         '    "corpus.pointers.commit_nonhash": ("zero", "commit_nonhash"),\n', ""),
                     encoding="utf-8")

    def rerecorded(w):
        f = w / "verifiers/corpus-baseline.json"
        doc = json.loads(f.read_text(encoding="utf-8"))
        for cid in ("corpus.index.tracked_files", "corpus.pointers.report_total",
                    "corpus.pointers.commit_total"):
            doc["checks"][cid]["expect"] = base_obs[cid]
        f.write_text(json.dumps(doc, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    def newname(w):
        f = w / lesson
        f.write_text(f.read_text(encoding="utf-8")
                     + "\n- probe: non-hash citation commit `not-a-hash-token`.\n", encoding="utf-8")

    return {"w_tip": None, "w_healed": healed, "w_added_instance": added,
            "w_silenced": silenced, "w_rerecorded": rerecorded, "w_newname": newname}


def d5_run_gate(gate_path, receipt, root, tag):
    rc, txt = run([PY, "-B", str(gate_path), "--base-receipt", str(receipt),
                   "--root", str(root)], S)
    save(tag, "%s.txt" % root.name, "$ gate --root %s\n# exit=%d\n%s" % (root, rc, txt))
    closed = RES_RE.search(txt)
    drift = K_RE.search(txt)
    return rc, (closed.group(1) if closed else "?"), (drift.group(1) if drift else "?"), txt


def run_d5():
    d5dir = S / "d5"
    d5dir.mkdir(parents=True, exist_ok=True)
    receipt = d5dir / "d5v3-base-receipt.json"
    rc, out = run([PY, "-B", str(P / D5_SRC), "--write-base-receipt", str(receipt)], P)
    print("base receipt:", rc, out.strip().splitlines()[-1])
    assert rc == 0, out
    base_clone = make_world("base", P, None)
    lane_obs = integrity_json(P)
    clone_obs = integrity_json(base_clone)
    eq = lane_obs == clone_obs
    print("Q79 equivalence lane vs base clone (integrity observation dict):", eq)
    base_obs = {row["check"]: row["observed"] for row in clone_obs["results"]}
    mutators = world_mutators(base_obs)
    worlds = {}
    for name, _want, _desc in D5_WORLDS:
        mut = mutators[name]
        worlds[name] = make_world(name, base_clone, mut)
        obs = integrity_json(worlds[name])
        drift = sorted(r["check"] for r in obs["results"] if r["verdict"] == "DRIFT")
        print("world %-18s DRIFT=%s" % (name, drift))
    # the lane itself is an honest tip too (Q79: must match the world result)
    gates = {"pristine": P / D5_SRC}
    d5dir_g = d5dir / "gates"
    d5dir_g.mkdir(exist_ok=True)
    for name, fn in D5_MUTANTS + D5_EQUIV:
        t = fn(D5_TEXT)
        (d5dir_g / (name + ".py")).write_text(t, encoding="utf-8")
        gates[name] = d5dir_g / (name + ".py")
    tables = {}
    for gname, gpath in gates.items():
        tables[gname] = {}
        for wname, want, _desc in D5_WORLDS:
            root = worlds[wname]
            rc2, closed, drift, _txt = d5_run_gate(gpath, receipt, root, "d5-" + gname)
            tables[gname][wname] = (rc2, closed, drift)
        print(gname, " ".join("%s=%d(%s/%s)" % (w, tables[gname][w][0], tables[gname][w][1],
                                                tables[gname][w][2]) for w, _x, _d in D5_WORLDS))
    lane_rc, lane_closed, lane_drift, _t = d5_run_gate(P / D5_SRC, receipt, P, "d5-lane-tip")
    print("lane tip (working tree):", lane_rc, lane_closed, lane_drift, "Q79 eq:", eq)
    return tables, eq, (lane_rc, lane_closed, lane_drift)


def d5_killed(table):
    bad = []
    for wname, want, _d in D5_WORLDS:
        rc, _c, _k = table[wname]
        if rc != want:
            bad.append("%s %d->%d" % (wname, want, rc))
    return bad


def d5_exits(table):
    return " ".join("%s=%d" % (w, table[w][0]) for w, _x, _d in D5_WORLDS)


def main():
    TR.mkdir(parents=True, exist_ok=True)
    which = sys.argv[1] if len(sys.argv) > 1 else "all"
    fg_rows, dup_rc, dup_txt = ([], None, "")
    d5_tables, eq, lane_tip = ({}, None, None)
    if which in ("all", "fg"):
        fg_rows, dup_rc, dup_txt = run_fg()
    if which in ("all", "d5"):
        d5_tables, eq, lane_tip = run_d5()
    rows_m, rows_e = [], []
    ptable = d5_tables.get("pristine", {})
    for name, _fn in FG_MUTANTS:
        r = [x for x in fg_rows if x[0] == name]
        if r:
            rows_m.append(r[0])
    for name, _fn in D5_MUTANTS:
        if name in d5_tables:
            bad = d5_killed(d5_tables[name])
            rows_m.append((name, "verifiers/check_r86_routed_repairs_v3.py",
                           ("killed: " + "; ".join(bad)) if bad else "SURVIVED",
                           d5_exits(ptable), d5_exits(d5_tables[name])))
    for name, _fn in FG_EQUIV:
        r = [x for x in fg_rows if x[0] == name]
        if r:
            rows_e.append(r[0])
    for r in fg_rows:
        if r[0].startswith("plan-"):
            rows_e.append(r)
    for name, _fn in D5_EQUIV:
        if name in d5_tables:
            bad = d5_killed(d5_tables[name])
            rows_e.append((name, "verifiers/check_r86_routed_repairs_v3.py",
                           "survives" if not bad else "KILLED-BY-EQUIVALENT: " + "; ".join(bad),
                           d5_exits(ptable), d5_exits(d5_tables[name])))
    WAVE.mkdir(parents=True, exist_ok=True)
    if rows_m:
        (WAVE / "mutants.tsv").write_text(
            "mutant\tfile\tkilled-by-fixture\tobserved exit before\tobserved exit after\n"
            + "".join("\t".join(map(str, r)) + "\n" for r in rows_m), encoding="utf-8")
    if rows_e:
        (WAVE / "equivalents.tsv").write_text(
            "equivalent\tfile\tsurvived\tobserved exit before\tobserved exit after\n"
            + "".join("\t".join(map(str, r)) + "\n" for r in rows_e), encoding="utf-8")
    summary = {
        "duplicate_probe_exit": dup_rc, "duplicate_probe_tail": dup_txt.splitlines()[-1:] if dup_txt else [],
        "q79_equivalence": eq, "lane_tip": lane_tip,
        "d5_pristine_exits": d5_exits(ptable) if ptable else None,
    }
    (WAVE / "summary.json").write_text(json.dumps(summary, indent=2), encoding="utf-8")
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
