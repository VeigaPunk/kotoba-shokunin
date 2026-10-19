#!/usr/bin/env python3
"""R3 late-pass critic — the union battery for round 40.

Re-runs, against whatever comparator/guard/corpus bytes are live at the moment
it runs, the union of every probe class named by the round-40 claims:

  * C1/F-2  value-channel laundering through `expected`/`expected_value`
  * C1/F-3  `_record_list` reads-first: a divergent value hidden in `rows`
  * C1/A7   the same class against `checks` (V1's arm A7)
  * C2/V3a  copy-variant `--script` override pointing at another row's target
  * C2/V3b  path confinement: an override/`--repo` reading outside the repo
  * C3/V4   a 4-space / tab pseudo-closer that cmark reads as content

Every arm is built from captured payloads (never the live instruments) and
mutates copies only. The live join is re-run at the end and must read 24/24
exit 0.

Usage:
    python3 union-battery.py --repo <repo> [--out <dir>] [--ind <ind.json>]
                             [--live <live.json>]
"""

import argparse
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent


def sha256(path):
    import hashlib
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def run(argv, cwd, timeout=180):
    proc = subprocess.run(argv, cwd=str(cwd), capture_output=True, text=True,
                          timeout=timeout)
    return proc.returncode, proc.stdout, proc.stderr


# --------------------------------------------------------------------------
# C1 arms: mutate the captured independent payload, run the comparator on it
# --------------------------------------------------------------------------
def _records(payload, key):
    v = payload.get(key)
    return v if isinstance(v, list) else None


def _unscoped(out):
    """The records the live join actually scores (scoped rows must stay out)."""
    return [r for r in out["results"] if r.get("status") != "SCOPED_OUT"]


def _harvested(live):
    return {r["check"]: r["observed"] for r in live["results"]}


def _scored_ids(out):
    """The ids the join scores: unscoped rows only.

    A scoped row's `checks` entry is legitimately `None` in the live payload,
    so mutating it would manufacture a divergence the arm is not about.
    """
    return {r["check"] for r in _unscoped(out)}


def arm_f2_expected_launder(ind, live):
    """R1's m2 / F-2: park the harvested value in `expected` in both record
    channels and in the plain `checks` map, while BOTH derived fields read
    NOT DERIVED.  Channel-consistent by construction (every channel selects to
    the same value), so the only thing under test is the value channel."""
    observed = _harvested(live)
    out = json.loads(json.dumps(ind))
    scored = _scored_ids(out)
    for rec in _unscoped(out):
        rec["expected"] = observed.get(rec["check"])
        rec["re_derived"] = "NOT DERIVED"
        rec["value"] = "NOT DERIVED"
    for rec in out["rows"]:
        if rec["check"] in scored:
            rec["expected"] = observed.get(rec["check"])
            rec["value"] = "NOT DERIVED"
    for cid in scored:
        if cid in out["checks"]:
            out["checks"][cid] = observed.get(cid)
    return out


def arm_f2b_expected_outranks(ind, live):
    """The discriminator: `expected` = harvested (agrees), `value` = 999.

    Exit 0 proves the driver consumed `expected` and never looked at the
    derived channel; exit 1 would mean it read the derived value.
    """
    observed = _harvested(live)
    out = json.loads(json.dumps(ind))
    scored = _scored_ids(out)
    for rec in _unscoped(out):
        rec["expected"] = observed.get(rec["check"])
        rec["re_derived"] = 999
        rec["value"] = 999
    for rec in out["rows"]:
        if rec["check"] in scored:
            rec["expected"] = observed.get(rec["check"])
            rec["value"] = 999
    for cid in scored:
        if cid in out["checks"]:
            out["checks"][cid] = observed.get(cid)
    return out


def arm_f2c_consistent_divergence(ind, live):
    """The control that keeps the F-2 arms from reading as 'everything fails':
    a CONSISTENT divergence in every channel must still be caught as a genuine
    disagreement (exit 1), not swept into the divergence error (exit 2).

    The key mutated is the one the driver actually selects -- the first of
    ``IND_VALUE_KEYS`` present -- so ``re_derived`` must move, not just
    ``value`` (an arm that moved only ``value`` manufactured a channel split
    instead, which is what my first revision measured).
    """
    out = json.loads(json.dumps(ind))
    scored = _scored_ids(out)
    for rec in _unscoped(out):
        rec["value"] = 999
        if "re_derived" in rec:
            rec["re_derived"] = 999
    for rec in out["rows"]:
        if rec["check"] in scored:
            rec["value"] = 999
    for cid in scored:
        if cid in out["checks"]:
            out["checks"][cid] = 999
    return out


def arm_f3_rows_shadow(ind, live):
    """F-3: `results` clean, `rows` carries a divergent value."""
    out = json.loads(json.dumps(ind))
    for rec in out["rows"]:
        if rec["check"] == "omp.offered.skills":
            rec["value"] = 999
    return out


def arm_a7_checks_shadow(ind, live):
    """A7: `checks` map diverges while `results` stays clean."""
    out = json.loads(json.dumps(ind))
    out["checks"]["omp.offered.skills"] = 999
    return out


def arm_f3_rows_missing(ind, live):
    """F-3 variant: `rows` drops a record the other channels carry."""
    out = json.loads(json.dumps(ind))
    out["rows"] = [r for r in out["rows"] if r["check"] != "omp.offered.skills"]
    return out


def arm_f3_rows_all_divergent(ind, live):
    """The strong F-3 shape: EVERY row of `rows` diverges from `results`."""
    out = json.loads(json.dumps(ind))
    for rec in out["rows"]:
        rec["value"] = 999
    return out


def arm_control_unmutated(ind, live):
    """Control: the captured payload untouched must still read exit 0."""
    return json.loads(json.dumps(ind))


C1_ARMS = [
    ("F-2-copy-satisfaction", arm_f2_expected_launder),
    ("F-2b-expected-outranks-value", arm_f2b_expected_outranks),
    ("F-2c-consistent-divergence", arm_f2c_consistent_divergence),
    ("F-3-rows-shadow", arm_f3_rows_shadow),
    ("F-3b-rows-missing", arm_f3_rows_missing),
    ("F-3c-rows-all-divergent", arm_f3_rows_all_divergent),
    ("A7-checks-shadow", arm_a7_checks_shadow),
    ("CONTROL-unmutated", arm_control_unmutated),
]


def run_c1(repo, ind_payload, live_json, workdir, driver):
    """Each arm: write the mutated payload, run the driver on it."""
    results = []
    live_path = workdir / "live.json"
    live_path.write_text(json.dumps(live_json))
    for name, fn in C1_ARMS:
        payload = fn(ind_payload, live_json)
        path = workdir / ("ind-%s.json" % name)
        path.write_text(json.dumps(payload, indent=1))
        rc, out, err = run(
            [sys.executable, str(driver), "--independent-json", str(path),
             "--live-json", str(live_path), "--cwd", str(repo), "--json"],
            cwd=repo,
        )
        reason = ""
        try:
            meta = json.loads(out)
            reason = meta.get("reason", "")
            headline = meta.get("headline", {})
        except ValueError:
            headline = {}
            reason = (err or out).strip().splitlines()[-1][:160] if (err or out).strip() else ""
        results.append({"arm": name, "exit": rc, "reason": reason[:200],
                        "headline": headline})
    return results


# --------------------------------------------------------------------------
# C2 arms: the floors guard — copy-variant override + path confinement
# --------------------------------------------------------------------------
def run_c2(repo, workdir):
    """The guard's override arms, run in a stub world that stays inside the lane.

    The world carries the real guard bytes plus a stub registry, so the arms
    measure the override logic itself, not the live tree's floors. The
    `--script` copy/symlink arms are what V3 filed: an absolute-argv override
    that POINTS AT another pinned row's target.
    """
    guard = repo / "verifiers" / "check_assertion_floors.py"
    results = []
    world = workdir / "guard-world"
    (world / "verifiers").mkdir(parents=True, exist_ok=True)
    shutil.copyfile(str(guard), str(world / "verifiers" / "check_assertion_floors.py"))

    # two stub instruments the guard's tables can pin
    for name, floor in (("stub_a", 3), ("stub_b", 3)):
        (world / "verifiers" / ("%s.py" % name)).write_text(
            'import argparse\n'
            'ap = argparse.ArgumentParser()\n'
            'ap.add_argument("--self-test", action="store_true")\n'
            'ap.add_argument("--repo", default=None)\n'
            'ap.parse_args()\n'
            'print("self-test: 0 failure(s) over 3 assertions")\n')
    registry = {"instrument_total": 2, "instruments": {
        "stub_a": {"path": "verifiers/stub_a.py", "floor": 3},
        "stub_b": {"path": "verifiers/stub_b.py", "floor": 3}}}
    (world / "verifiers" / "floors-registry.json").write_text(json.dumps(registry))

    # rewrite the guard's two tables to the stub pair (count-checked swaps).
    # NB: `"INSTRUMENTS = {"` is a SUBSTRING of `"EXPECTED_INSTRUMENTS = {"`,
    # so both anchors are line-anchored ("\n" prefix) -- an unanchored search
    # clobbers the wrong table (caught by the world's own control arm).
    # The tables are parsed, never hardcoded: sibling seats bump the live
    # floors mid-round and a hardcoded anchor would break this battery.
    text = (world / "verifiers" / "check_assertion_floors.py").read_text()

    # EXPECTED_INSTRUMENTS = { "<name>": <floor>, ... }
    exp_start = text.index("\nEXPECTED_INSTRUMENTS = {") + 1
    exp_end = text.index("\n}\n", exp_start) + 3
    names = re.findall(r'"([^"]+)":\s*\d+,', text[exp_start:exp_end])
    assert len(names) >= 2, names
    text = text[:exp_start] + (
        "EXPECTED_INSTRUMENTS = {\n"
        '    "stub_a": 3,\n'
        '    "stub_b": 3,\n'
        "}\n") + text[exp_end:]

    # INSTRUMENTS = { "<name>": ("<path>", <floor>, r"...", a, b), ... }
    ins_start = text.index("\nINSTRUMENTS = {") + 1
    ins_end = text.index("\n}\n", ins_start) + 3
    text = text[:ins_start] + (
        "INSTRUMENTS = {\n"
        '    "stub_a": ("verifiers/stub_a.py", 3,\n'
        '               r"self-test:\\s*(\\d+) failure\\(s\\) over (\\d+) assertions", 2, 1),\n'
        '    "stub_b": ("verifiers/stub_b.py", 3,\n'
        '               r"self-test:\\s*(\\d+) failure\\(s\\) over (\\d+) assertions", 2, 1),\n'
        "}\n") + text[ins_end:]
    src = text
    (world / "verifiers" / "check_assertion_floors.py").write_text(src)
    world_guard = world / "verifiers" / "check_assertion_floors.py"

    def guard_run(extra):
        return run([sys.executable, str(world_guard), "--repo", str(world),
                    "--self-test-timeout", "30"] + extra, cwd=world, timeout=120)

    # an out-of-world stub (a real file with a plausible self-test line) used by
    # both confinement arms below
    outside = workdir / "outside-stub.py"
    outside.write_text('print("self-test: 0 failure(s) over 999 assertions")\n')

    rc, out, err = guard_run([])
    results.append({
        "arm": "CONTROL-stub-world", "exit": rc,
        "out": (out + err).strip()[:300],
        "verdict": "green control" if rc == 0 else "control itself red",
    })

    # V3a: a COPY of another row's target, under a different name, absolute argv
    copy = world / "verifiers" / "copy-of-stub-b.py"
    shutil.copyfile(str(world / "verifiers" / "stub_b.py"), str(copy))
    rc, out, err = guard_run(["--script", "stub_a=%s" % copy])
    results.append({
        "arm": "V3a-copy-variant-absolute-argv", "exit": rc,
        "out": (out + err).strip()[:400],
        "verdict": "silent-green (no named rejection)" if rc == 0 else "rejected",
    })

    # V3a-b: the same repoint as a symlink
    link = world / "verifiers" / "link-to-stub-b.py"
    if link.exists() or link.is_symlink():
        link.unlink()
    link.symlink_to(world / "verifiers" / "stub_b.py")
    rc, out, err = guard_run(["--script", "stub_a=%s" % link])
    results.append({
        "arm": "V3a-b-symlink-absolute-argv", "exit": rc,
        "out": (out + err).strip()[:400],
        "verdict": "silent-green (no named rejection)" if rc == 0 else "rejected",
    })

    # V3a-c: control -- the same repoint expressed by the canonical path string
    rc, out, err = guard_run(["--script", "stub_a=%s" % (world / "verifiers" / "stub_b.py")])
    results.append({
        "arm": "V3a-c-canonical-path-control", "exit": rc,
        "out": (out + err).strip()[:400],
        "verdict": "rejected (expected -- the documented arm)" if rc != 0 else "silent-green",
    })

    # V3b: an override outside the world entirely (out-of-repo read)
    rc, out, err = guard_run(["--script", "stub_a=%s" % outside])
    results.append({
        "arm": "V3b-outside-world-override", "exit": rc,
        "out": (out + err).strip()[:400],
        "verdict": "silent-green (no named rejection)" if rc == 0 else "rejected",
    })

    # V3b-b: a `../` traversal that lands outside the world but is a real file
    traversal = world / "verifiers" / ".." / ".." / "outside-stub.py"
    if traversal.resolve() == outside.resolve():
        rc, out, err = guard_run(["--script", "stub_a=%s" % traversal])
    else:
        rc, out, err = 1, "", "traversal resolved to %s, expected %s" % (
            traversal.resolve(), outside.resolve())
    results.append({
        "arm": "V3b-b-dotdot-traversal", "exit": rc,
        "out": (out + err).strip()[:400],
        "verdict": "silent-green (no named rejection)" if rc == 0 else
                   ("rejected" if rc == 2 else "other exit"),
    })

    # V3b-d: V3's own confinement shape -- the REGISTRY declares a path that
    # lives outside --repo. If the guard runs it green, out-of-repo reads are
    # unenforced through the anchor channel.
    outside_reg = {"instrument_total": 2, "instruments": {
        "stub_a": {"path": "verifiers/stub_a.py", "floor": 3},
        "stub_b": {"path": str(outside), "floor": 3}}}
    (world / "verifiers" / "floors-registry.json").write_text(json.dumps(outside_reg))
    rc, out, err = guard_run([])
    results.append({
        "arm": "V3b-d-registry-outside-path", "exit": rc,
        "out": (out + err).strip()[:400],
        "verdict": "silent-green (out-of-repo path runs unenforced)" if rc == 0 else "rejected",
    })
    # restore the in-world registry for later arms
    (world / "verifiers" / "floors-registry.json").write_text(json.dumps(registry))

    # V3b-e: V3's actual confinement shape -- the guard's OWN row path (and the
    # registry entry, so no drift check fires) points at a file outside --repo.
    # If this runs green, the "under --repo" claim is unenforced.
    src2 = (world / "verifiers" / "check_assertion_floors.py").read_text()
    src2 = src2.replace('"stub_b": ("verifiers/stub_b.py", 3,',
                        '"stub_b": ("%s", 3,' % outside)
    (world / "verifiers" / "check_assertion_floors.py").write_text(src2)
    (world / "verifiers" / "floors-registry.json").write_text(json.dumps(
        {"instrument_total": 2, "instruments": {
            "stub_a": {"path": "verifiers/stub_a.py", "floor": 3},
            "stub_b": {"path": str(outside), "floor": 3}}}))
    rc, out, err = guard_run([])
    results.append({
        "arm": "V3b-e-row-path-outside-repo", "exit": rc,
        "out": (out + err).strip()[:400],
        "verdict": ("silent-green (out-of-repo row path runs unenforced)"
                    if rc == 0 else "rejected"),
    })
    # restore the in-world guard + registry
    (world / "verifiers" / "check_assertion_floors.py").write_text(src)
    (world / "verifiers" / "floors-registry.json").write_text(json.dumps(registry))

    # V3b-c: `--repo` pointed at a directory with no anchor at all
    rc, out, err = run([sys.executable, str(world_guard), "--repo", str(workdir),
                        "--self-test-timeout", "30"], cwd=workdir, timeout=120)
    results.append({
        "arm": "V3b-c-repo-without-anchor", "exit": rc,
        "out": (out + err).strip()[:400],
        "verdict": "named rejection" if rc == 2 else
                   ("silent-green" if rc == 0 else "other exit"),
    })
    return results


# --------------------------------------------------------------------------
# C3 arms: the corpus gates — an indentation-legal-looking pseudo-closer
# --------------------------------------------------------------------------
INDENT_SHAPES = {
    "4-space-closer": "    ````",
    "tab-closer": "\t````",
    "3-space-closer": "   ````",
    "0-space-closer-control": "````",
}


def _c3_world(root, closer):
    """A throwaway git world whose ONLY coverage of b.md is a quoted row.

    Line layout (1-based) -- the quoted row is line 10:
      1 '# t'            5 header          8 '````'   (opener)
      2 ''               6 separator       9 <closer>
      3 '## Coverage map' 7 live row       10 quoted row
      4 ''                                 11 '````'
    """
    lines = ["# t", "", "## Coverage map", "",
             "| Area | File | Basis |", "|------|------|-------|",
             "| Live | `knowledge/a.md` | x |",
             "````", closer, "| Quoted | `knowledge/b.md` | x |", "````"]
    readme = os.path.join(root, "corpus", "README.md")
    os.makedirs(os.path.dirname(readme), exist_ok=True)
    with open(readme, "w") as fh:
        fh.write("\n".join(lines) + "\n")
    for rel in ("corpus/knowledge/a.md", "corpus/knowledge/b.md"):
        p = os.path.join(root, rel)
        os.makedirs(os.path.dirname(p), exist_ok=True)
        with open(p, "w") as fh:
            fh.write("# %s\n" % rel)
    # a baseline so the integrity gate ADJUDICATES instead of observing only
    # (without one it exits 3 "observations above only", which is not a verdict)
    os.makedirs(os.path.join(root, "verifiers"), exist_ok=True)
    with open(os.path.join(root, "verifiers", "corpus-baseline.json"), "w") as fh:
        json.dump({"checks": {
            "corpus.index.tracked_files": {"mode": "equal", "expect": 3},
            "corpus.pointers.report_total": {"mode": "equal", "expect": 0},
            "corpus.pointers.commit_total": {"mode": "equal", "expect": 0},
        }}, fh)
    for argv in (["init", "-q"], ["add", "-A"]):
        subprocess.run(["git", "-C", root] + argv, capture_output=True)


ROW_LINE = 10  # the quoted `knowledge/b.md` row


def _cmark_block(root):
    """The cmark code-block span of corpus/README.md, or None."""
    text = Path(root, "corpus", "README.md").read_text()
    proc = subprocess.run(["cmark", "--sourcepos", "-t", "xml"], input=text,
                          capture_output=True, text=True)
    m = re.search(r'<code_block sourcepos="(\d+):\d+-(\d+):\d+"', proc.stdout)
    return (int(m.group(1)), int(m.group(2))) if m else None


def run_c3(repo, workdir):
    """Each shape's verdict is derived from cmark, never from my expectation.

    cmark's own code_block span tells us whether the quoted row is CONTENT
    (the block covers ROW_LINE) or LIVE (the block closed before it). The
    gate is correct exactly when its classification matches cmark's:
      * cmark says content  -> the gate must report unindexed>=1 / exit!=0
      * cmark says live     -> the gate must report unindexed=0 / exit 0
    """
    results = []
    integ = repo / "verifiers" / "verify_corpus_integrity.py"
    indep = repo / "verifiers" / "verify_corpus_independent.py"
    for name, closer in INDENT_SHAPES.items():
        root = tempfile.mkdtemp(prefix="r3-c3-", dir=str(workdir))
        _c3_world(root, closer)
        span = _cmark_block(root)
        row_is_content = bool(span and span[0] <= ROW_LINE <= span[1])
        for label, inst in (("integrity", integ), ("independent", indep)):
            rc, out, err = run(
                [sys.executable, str(inst), "--repo", root], cwd=repo)
            unindexed = None
            m = re.search(r"unindexed=(\d+)", out + err)
            if m:
                unindexed = int(m.group(1))
            gate_says_content = rc != 0 or (unindexed or 0) > 0
            agrees = (gate_says_content == row_is_content)
            results.append({
                "arm": "%s/%s" % (name, label), "exit": rc,
                "unindexed": unindexed, "cmark_block": span,
                "row_line": ROW_LINE,
                "cmark_says": "content" if row_is_content else "live",
                "gate_says": "content" if gate_says_content else "live",
                "verdict": ("AGREES" if agrees else
                            "SILENT-FALSE-PASS (cmark says content, gate says live)"
                            if row_is_content else
                            "FALSE-ALARM (cmark says live, gate says content)"),
            })
        shutil.rmtree(root, ignore_errors=True)
    return results


# --------------------------------------------------------------------------
# the live join
# --------------------------------------------------------------------------
def run_live_join(repo, driver):
    rc, out, err = run([sys.executable, str(driver), "--json", "--cwd", str(repo)],
                       cwd=repo, timeout=300)
    summary = {"exit": rc}
    try:
        meta = json.loads(out)
        summary.update({
            "headline": meta.get("headline"),
            "agreement": meta.get("agreement"),
            "reason": meta.get("reason"),
            "head": meta.get("head"),
        })
    except ValueError:
        summary["stdout_tail"] = out.strip()[-300:]
        summary["stderr_tail"] = err.strip()[-300:]
    return summary


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo", default=str(Path(__file__).resolve().parents[4]))
    ap.add_argument("--out", default=str(HERE / "union"))
    ap.add_argument("--ind", default=None, help="captured independent JSON (default: run it live)")
    ap.add_argument("--live", default=None, help="captured live JSON (default: run it live)")
    ap.add_argument("--driver", default=None,
                    help="comparator to test (default: the live one). Point this at a "
                         "frozen copy to run the SAME arm set against HEAD bytes.")
    args = ap.parse_args()
    repo = Path(args.repo).resolve()
    outdir = Path(args.out)
    outdir.mkdir(parents=True, exist_ok=True)
    work = outdir / "work"
    if work.exists():
        shutil.rmtree(work)
    work.mkdir(parents=True)

    driver = (Path(args.driver).resolve() if args.driver
              else repo / "verifiers" / "compare_harness_independent.py")

    # capture fresh payloads from the LIVE instruments unless a file was given:
    # a stale capture would measure the r39 bytes, not the landing
    if args.ind:
        ind_payload = json.loads(Path(args.ind).read_text())
    else:
        rc, out, err = run([sys.executable, str(repo / "verifiers" /
                          "verify_harness_independent.py"), "--json"], cwd=repo, timeout=300)
        assert rc == 0, ("independent instrument exit %d: %s" % (rc, err[:300]))
        ind_payload = json.loads(out)
        (outdir / "ind-live.json").write_text(json.dumps(ind_payload, indent=1))
    if args.live:
        live_payload = json.loads(Path(args.live).read_text())
    else:
        rc, out, err = run([sys.executable, str(repo / "verifiers" /
                          "verify_harness_claims.py"), "--json"], cwd=repo, timeout=300)
        assert rc == 0, ("live instrument exit %d: %s" % (rc, err[:300]))
        live_payload = json.loads(out)
        (outdir / "live-live.json").write_text(json.dumps(live_payload, indent=1))

    report = {
        "repo": str(repo),
        "when": subprocess.run(["date", "-u", "+%Y-%m-%dT%H:%M:%SZ"],
                               capture_output=True, text=True).stdout.strip(),
        "head": run(["git", "-C", str(repo), "rev-parse", "--short", "HEAD"],
                    cwd=repo)[1].strip(),
        "shas": {
            p.name: sha256(repo / "verifiers" / p.name)
            for p in [Path("compare_harness_independent.py"),
                      Path("verify_harness_independent.py"),
                      Path("check_assertion_floors.py"),
                      Path("floors-registry.json"),
                      Path("verify_corpus_integrity.py"),
                      Path("verify_corpus_independent.py"),
                      Path("harness-independent-scope.json")]
            if (repo / "verifiers" / p.name).is_file()
        },
    }

    report["C1"] = run_c1(repo, ind_payload, live_payload, work, driver)
    report["C2"] = run_c2(repo, work)
    report["C3"] = run_c3(repo, work)
    report["LIVE_JOIN"] = run_live_join(repo, driver)

    (outdir / "union-battery.json").write_text(
        json.dumps(report, indent=2, sort_keys=True) + "\n")

    # ---- human-readable summary -------------------------------------------
    print("== union battery ==")
    print("repo %s head %s" % (report["repo"], report["head"]))
    for k, v in report["shas"].items():
        print("  %s %s" % (v[:16], k))
    print()
    print("-- C1 (comparator payload arms) --")
    for r in report["C1"]:
        print("  %-24s exit=%s  %s" % (r["arm"], r["exit"], r["reason"]))
    print()
    print("-- C2 (floors guard arms) --")
    for r in report["C2"]:
        first = (r["out"].splitlines() or [""])[0]
        print("  %-32s exit=%s  %s" % (r["arm"], r["exit"], first))
    print()
    print("-- C3 (corpus gate arms) --")
    for r in report["C3"]:
        print("  %-32s exit=%s unindexed=%s cmark=%s cmark_says=%s gate_says=%s  %s" % (
            r["arm"], r["exit"], r["unindexed"], r["cmark_block"],
            r["cmark_says"], r["gate_says"], r["verdict"]))
    print()
    print("-- live join --")
    print("  exit=%s  %s" % (report["LIVE_JOIN"]["exit"],
                             report["LIVE_JOIN"].get("reason")))
    hl = report["LIVE_JOIN"].get("headline") or {}
    print("  headline=%s joined=%s" % (hl.get("column"), hl.get("joined_scope")))
    return 0


if __name__ == "__main__":
    sys.exit(main())
