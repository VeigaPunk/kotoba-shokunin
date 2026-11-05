#!/usr/bin/env python3
"""MutTesterBattery harness (scratch only). Mutates the battery file in the scratch clone D,
never the lane. Each mutant runs the battery self-test and the frozen run at REV2; a mutant
that changes no observation is then probed with the X controls (rev/dirty-tree setups).
Writes mutants.tsv, equivalents.tsv, summary.json and transcripts to the wave dir."""
import hashlib, json, os, re, shutil, subprocess, sys
from pathlib import Path

S = Path("/fast/scratch/hyaku/kotoba-r90/MutTesterBattery")
D = S / "repo"
W = Path("/home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-90/w1/MutTesterBattery")
T = W / "transcripts"
BAT = "verifiers/check_mutation_battery.py"
MAN = "verifiers/fixtures/mutation-battery/manifest.tsv"
SK = "SKILL.md"
ENV = dict(os.environ, TMPDIR=str(S))
REV1 = (S / "rev-pristine.txt").read_text().strip()
REV2 = "a93b51b3279f8591e3938f590ca589c7d33c627b"
PRISTINE_SHA = "0828fd9b6277c98826521109b7abac5930dea9c9e5bb26314d84b54218477e3b"
FG = "verifiers/check_freeze_gate.py"
D5 = "verifiers/check_r86_routed_repairs_v3.py"
TRANSCRIPTS = []


def sha(b):
    return hashlib.sha256(b).hexdigest()


def git(*args):
    p = subprocess.run(["git", "-C", str(D), *args], capture_output=True, env=ENV)
    if p.returncode != 0:
        raise SystemExit("git failed %s: %s" % (args, p.stderr.decode()))
    return p.stdout


def run(argv, tag=None):
    p = subprocess.run(argv, cwd=str(D), env=ENV, capture_output=True, timeout=900)
    out = (p.stdout + p.stderr).decode("utf-8", "replace").replace(str(S), "<S>")
    if tag:
        (T / (tag + ".txt")).write_text("exit=%d\n%s" % (p.returncode, out), encoding="utf-8")
    return p.returncode, out


def put(data):
    (D / BAT).write_bytes(data)


def frozen(rev, tag):
    w = S / "w" / tag
    if w.exists():
        shutil.rmtree(w)
    return run(["python3", "-B", BAT, "--rev", rev, "--work", str(w)], tag)


def selftest(tag):
    return run(["python3", "-B", BAT, "--self-test"], tag)


def first_diff(a, b):
    la, lb = a.splitlines(), b.splitlines()
    for x, y in zip(la, lb):
        if x != y:
            return "%r -> %r" % (x[:110], y[:110])
    return "line count %d -> %d" % (len(la), len(lb))


def fails(out):
    return [l[:150] for l in out.splitlines() if l.startswith("FAIL ")]


# ---- setup: pristine battery bytes and the X-revisions / dirty overlays
PRI = git("show", "%s:%s" % (REV1, BAT))
assert sha(PRI) == PRISTINE_SHA, sha(PRI)
git("checkout", "-q", "--detach", REV2)
put(PRI)
assert sha((D / BAT).read_bytes()) == PRISTINE_SHA


def build_rev(path, newbytes, msg):
    (D / path).write_bytes(newbytes)
    git("add", path)
    git("-c", "user.name=MutTesterBattery", "-c", "user.email=mtb@scratch.invalid",
        "commit", "-q", "-m", msg)
    rev = git("rev-parse", "HEAD").decode().strip()
    git("checkout", "-q", "--detach", REV2)
    return rev


fg_rev2 = git("show", "%s:%s" % (REV2, FG))
REV3 = build_rev(FG, b"raise SystemExit(1)\n" + fg_rev2, "scratch X2: freeze gate broken at baseline")
man_rev2 = git("show", "%s:%s" % (REV2, MAN)).decode("utf-8").splitlines(keepends=True)
out_lines = []
for ln in man_rev2:
    if ln.startswith("d5-m1b-d5iii-removed\t"):
        parts = ln.rstrip("\n").split("\t")
        parts[3] = json.dumps({"op": "replace", "edits": [{"anchor": "    return 0\n",
                                                          "with": "    return 0  # r\n"}]})
        ln = "\t".join(parts) + "\n"
    out_lines.append(ln)
REV4 = build_rev(MAN, "".join(out_lines).encode("utf-8"), "scratch X5: anchor over-matches")
MAN_DIRTY = "".join(
    ("\t".join(p) + "\n") for p in
    [(ln.rstrip("\n").split("\t") if False else None) or [] for ln in []])  # placeholder, rebuilt below
man_text = git("show", "%s:%s" % (REV2, MAN)).decode("utf-8")
dirty_lines = []
for ln in man_text.splitlines(keepends=True):
    if ln.startswith("d5-m1a-d5iii-leg-only\t"):
        p = ln.rstrip("\n").split("\t")
        p[2] = "kill"
        ln = "\t".join(p) + "\n"
    dirty_lines.append(ln)
MAN_DIRTY_BYTES = "".join(dirty_lines).encode("utf-8")
SKILL_DIRTY_BYTES = git("show", "%s:%s" % (REV1, SK))
git("checkout", "-q", "--detach", REV2)
put(PRI)
print("REV3", REV3, "REV4", REV4, flush=True)


def with_overlay(path, data, fn):
    orig = (D / path).read_bytes()
    (D / path).write_bytes(data)
    try:
        return fn()
    finally:
        (D / path).write_bytes(orig)
        assert (D / path).read_bytes() == orig


# ---- the X probes: rev or dirty-tree setups that only a mutant reading the wrong bytes can see
def x_probe(xid, tag):
    if xid == "X1":
        return run(["python3", "-B", BAT, "--rev", "f" * 40, "--work", str(S / "w" / tag)], tag)
    if xid == "X2":
        return frozen(REV3, tag)
    if xid == "X5":
        return frozen(REV4, tag)
    if xid == "X3":
        return with_overlay(MAN, MAN_DIRTY_BYTES, lambda: frozen(REV2, tag))
    if xid == "X4":
        return with_overlay(SK, SKILL_DIRTY_BYTES, lambda: frozen(REV2, tag))
    raise SystemExit("no X " + xid)


XCTRL = {}
for xid in ("X1", "X2", "X5", "X3", "X4"):
    XCTRL[xid] = x_probe(xid, "pristine.%s" % xid)
    print("pristine", xid, XCTRL[xid][0], flush=True)
    assert (D / BAT).read_bytes() == PRI
    assert git("status", "--porcelain").decode().strip() == "", git("status", "--porcelain")

P_S = selftest("pristine.S")
P_F = frozen(REV2, "pristine.F")
put(PRI)
print("pristine S", P_S[0], "F", P_F[0], flush=True)
assert P_S[0] == 0 and P_F[0] == 1, (P_S[0], P_F[0])

MUTANTS = [
 ("mb-m1-verdict-sign-flip", "kill", "    return 0 if ok else 1\n", "    return 1 if ok else 0\n", None,
  "predicate verdict exit sign flipped"),
 ("mb-m2-g1-commit-check-skipped", "kill",
  '    if rc != 0 or out.decode().strip() != rev:\n        raise CouldNotEvaluate("G1: %s is not a commit',
  '    if False:\n        raise CouldNotEvaluate("G1: %s is not a commit', "X1",
  "G1 guard skip: non-commit full-hex --rev check"),
 ("mb-m3-g2-readback-off", "kill", "    if got != expect:\n", "    if False:\n", None,
  "G2 copy read-back check off"),
 ("mb-m4-g3-skipped", "kill", "    g3_ok = g3_rows >= 1\n", "    g3_ok = True\n", None,
  "G3 registry guard skip"),
 ("mb-m5-survivor-class-dropped", "kill", '    survs = [r for r in results if r["cls"] == "survivor"]\n',
  "    survs = []\n", None, "manifest class skip: survivor class dropped from the count"),
 ("mb-m6-line-drift", "kill", 'equivalents survived %d of %d; ', 'equivalents survive %d of %d; ', None,
  "printed predicate line drifts from the frozen sentence"),
 ("mb-m7-equiv-skipped-at-evaluation", "kill", "    for row in rows:\n        text = data[row.target]",
  '    for row in [r for r in rows if r.cls != "equivalent"]:\n        text = data[row.target]', None,
  "equivalent class skipped at evaluation"),
 ("mb-m8-rev-bytes-from-worktree", "kill", "        data[target] = git_show(lane, rev, target)\n",
  "        data[target] = (lane / target).read_bytes()\n", None,
  "G1 violation: target bytes read from the working tree"),
 ("mb-m9-eq-ws-into-strings", "kill", "        if i in multi or line.endswith", "        if line.endswith", None,
  "trailing-whitespace rewrite touches multi-line string bodies"),
 ("mb-m10-eq-comment-not-comment", "kill", "            out.append(COMMENT_MARK)",
  "            out.append(COMMENT_MARK[2:])", None,
  "comment-insert generator emits non-comment text (syntax-breaking)"),
 ("mb-m11-baseline-check-removed", "kill", "        check_baseline(target, base[target])\n",
  "        pass\n", "X2", "probe baseline guard (exit 2 on a broken baseline) removed"),
 ("mb-m12-observe-exit-constant", "kill", '    return (p.returncode, "\\n".join(kept))',
  '    return (0, "\\n".join(kept))', None, "probe exit code not observed (constant 0)"),
 ("mb-m13-anchor-overmatch-unguarded", "kill", "        if found != want:\n", "        if found < want:\n", "X5",
  "anchor count guard weakened: over-matching anchors pass"),
 ("mb-m14-cne-ladder-to-1", "kill", "        return 2\n    except OSError as exc:\n",
  "        return 1\n    except OSError as exc:\n", None,
  "exit ladder: could-not-evaluate mapped to 1"),
 ("mb-m15-clean-tree-guard-off", "kill", "    if rc != 0 or out.strip():\n", "    if False:\n", None,
  "G1 scratch clean-tree guard off"),
 ("mb-m16-restore-unverified", "kill",
  '        place(dest / row.target, data[row.target], rec_sha[row.target], "restore " + row.target)\n',
  "        pass\n", None, "revision-copy restore after each mutant not re-read"),
 ("mb-m17-manifest-from-worktree", "kill",
  '    rows = parse_manifest(git_show(lane, rev, MANIFEST).decode("utf-8"))\n',
  '    rows = parse_manifest((lane / MANIFEST).read_text(encoding="utf-8"))\n', "X3",
  "G1 violation: manifest read from the working tree"),
 ("mb-m18-skill-from-worktree", "kill",
  "    g3_rows = sum(1 for ln in git_show(lane, rev, SKILL).splitlines()\n",
  "    g3_rows = sum(1 for ln in (lane / SKILL).read_bytes().splitlines()\n", "X4",
  "G1 violation: SKILL.md read from the working tree"),
 ("mb-m19-g3-match-broken", "kill", "if BATTERY.encode() in ln)", 'if b"NO-SUCH-ROW" in ln)', None,
  "G3 row match never names the battery"),
]

EQUIV = [
 ("eq-s1-trailing-comment", "appended trailing comment line",
  lambda t: t + "\n# scratch equivalence: trailing comment\n"),
 ("eq-s2-docstring-comma", "comma inserted in the module docstring first line (argparse help text only)",
  lambda t: t.replace("Mutation battery over the round-89", "Mutation battery, over the round-89", 1)),
 ("eq-s3-rename-local-kept", "local variable kept renamed to keep_lines in observe()",
  lambda t: re.sub(r"\bkept\b", "keep_lines", t)),
 ("eq-s4-trailing-space-return", "two trailing spaces on the final return line of main's ok path",
  lambda t: t.replace("    return 0 if ok else 1\n", "    return 0 if ok else 1  \n", 1)),
 ("eq-s5-reflow-classes", "CLASSES tuple reflowed across lines",
  lambda t: t.replace('CLASSES = ("kill", "equivalent", "survivor")',
                      'CLASSES = (\n    "kill",\n    "equivalent",\n    "survivor",\n)', 1)),
]

rows_m, rows_e, summary = [], [], {"pristine": {"S": [P_S[0], P_S[1][-200:]], "F": [P_F[0]]}}
for mid, cls, old, new, xid, note in MUTANTS:
    text = PRI.decode("utf-8")
    n = text.count(old)
    assert n == 1, (mid, n)
    mut = text.replace(old, new, 1).encode("utf-8")
    assert mut != PRI
    try:
        compile(mut.decode("utf-8"), BAT, "exec")
        compiles = True
    except SyntaxError as exc:
        compiles = False
        note += " [does not compile: %s]" % exc.msg
    put(mut)
    try:
        s_obs = selftest(mid + ".S")
        f_obs = frozen(REV2, mid + ".F")
    finally:
        put(PRI)
    assert sha((D / BAT).read_bytes()) == PRISTINE_SHA
    killed_by, exits = None, ["selftest=%d" % s_obs[0], "frozen=%d" % f_obs[0]]
    if s_obs != P_S:
        killed_by = "self-test: " + ("; ".join(fails(s_obs[1])[:2]) or "exit %d->%d" % (P_S[0], s_obs[0]))
    elif f_obs != P_F:
        killed_by = ("frozen run: exit %d->%d" % (P_F[0], f_obs[0]) if f_obs[0] != P_F[0]
                     else "frozen run: output %s" % first_diff(P_F[1], f_obs[1]))
    xres = {}
    if killed_by is None and xid:
        put(mut)
        try:
            xo = x_probe(xid, mid + "." + xid)
        finally:
            put(PRI)
        assert sha((D / BAT).read_bytes()) == PRISTINE_SHA
        base = XCTRL[xid]
        exits.append("%s=%d(pristine %d)" % (xid, xo[0], base[0]))
        if xid == "X1":
            if xo[0] != base[0]:
                killed_by = "%s: exit %d->%d" % (xid, base[0], xo[0])
            else:
                xres["msg"] = "X1 exit unchanged %d; diagnostic text %s" % (xo[0], first_diff(base[1], xo[1]))
        elif xo != base:
            killed_by = "%s: %s" % (xid, ("exit %d->%d" % (base[0], xo[0])) if xo[0] != base[0]
                                    else "output %s" % first_diff(base[1], xo[1]))
    if killed_by is None:
        killed_by = "SURVIVED: " + note + ("; " + xres["msg"] if xres else "")
    if killed_by.startswith("SURVIVED") is False and cls == "kill":
        pass
    rows_m.append((mid, "verifiers/check_mutation_battery.py", killed_by,
                   "selftest=%d frozen=%d" % (P_S[0], P_F[0]), " ".join(exits)))
    print(mid, "|", killed_by[:200], "|", " ".join(exits), flush=True)

for eid, note, fn in EQUIV:
    new = fn(PRI.decode("utf-8")).encode("utf-8")
    assert new != PRI, eid
    compile(new.decode("utf-8"), BAT, "exec")
    put(new)
    try:
        s_obs = selftest(eid + ".S")
        f_obs = frozen(REV2, eid + ".F")
    finally:
        put(PRI)
    assert sha((D / BAT).read_bytes()) == PRISTINE_SHA
    if s_obs == P_S and f_obs == P_F:
        verdict = "survived (probes identical: self-test and frozen run)"
    else:
        verdict = "KILLED (equivalence broken): " + first_diff(P_F[1], f_obs[1])
    rows_e.append((eid, "verifiers/check_mutation_battery.py", verdict + " [" + note + "]",
                   "selftest=%d frozen=%d" % (P_S[0], P_F[0]),
                   "selftest=%d frozen=%d" % (s_obs[0], f_obs[0])))
    print(eid, "|", verdict[:160], flush=True)

assert (D / BAT).read_bytes() == PRI
with (W / "mutants.tsv").open("w", encoding="utf-8") as fh:
    fh.write("mutant\tfile\tkilled-by-fixture\tobserved exit before\tobserved exit after\n")
    for r in rows_m:
        fh.write("\t".join(r) + "\n")
with (W / "equivalents.tsv").open("w", encoding="utf-8") as fh:
    fh.write("equivalent\tfile\tsurvived\tobserved exit before\tobserved exit after\n")
    for r in rows_e:
        fh.write("\t".join(r) + "\n")
summary.update({"REV1": REV1, "REV2": REV2, "REV3_X2": REV3, "REV4_X5": REV4,
                "battery_sha256": PRISTINE_SHA, "mutants": len(rows_m),
                "mutants_killed": sum(1 for r in rows_m if not r[2].startswith("SURVIVED")),
                "equivalents": len(rows_e),
                "equivalents_survived": sum(1 for r in rows_e if r[2].startswith("survived")),
                "restored_sha256_ok": True})
(W / "summary.json").write_text(json.dumps(summary, indent=2) + "\n", encoding="utf-8")
print("DONE", json.dumps({k: summary[k] for k in ("mutants", "mutants_killed", "equivalents",
                                                   "equivalents_survived")}))
