#!/usr/bin/env python3
"""MutSiblingCensus mutation battery for verifiers/check_sibling_census.py.

Round-73 wave 1, seat MutSiblingCensus.  Read-only attacker: the lane file is
never written; every mutant is an independent scratch copy under
.ufo/waves/round-73/w1/build/MutSiblingCensus/mutants/.  Detector per mutant:
`python3 -B <copy> --self-test` (60 s cap).  Pristine / mutated / restored
(lane file re-read after the battery) bytes are hashed at every step.
"""
import hashlib
import importlib.util
import json
import subprocess
import sys
import tempfile
import time
from pathlib import Path

LANE = Path("/home/vgpnk/Projects/shokunin/kotoba-shokunin")
SRC = LANE / "verifiers" / "check_sibling_census.py"
OUT = LANE / ".ufo" / "waves" / "round-73" / "w1" / "build" / "MutSiblingCensus"
MUTDIR = OUT / "mutants"
CENSUS = LANE / "corpus" / "knowledge" / "sibling-overlap-census-round49.md"

PRISTINE_BYTES = SRC.read_bytes()
PRISTINE_SHA = hashlib.sha256(PRISTINE_BYTES).hexdigest()
PRISTINE_TEXT = PRISTINE_BYTES.decode("utf-8")

MUTANTS = [
    dict(
        name="M01-no-ownership-marker",
        point="marker_in: final `return False` -> `return True` (G1 clause binding neutered: every clause counts as carrying an ownership/routing marker)",
        old="""        if re.search(pattern, clause, flags):
            return True
    return False""",
        new="""        if re.search(pattern, clause, flags):
            return True
    return True""",
    ),
    dict(
        name="M02-cap-dropped",
        point="skill_description_failures: the 1024 ceiling is dropped from the G4 length check",
        old="    if length < SKILL_DESCRIPTION_MIN or length > SKILL_DESCRIPTION_MAX:",
        new="    if length < SKILL_DESCRIPTION_MIN:",
    ),
    dict(
        name="M03-cap-off-by-one",
        point="G4 cap boundary `>` -> `>=`: a description of exactly 1024 characters is now rejected",
        old="    if length < SKILL_DESCRIPTION_MIN or length > SKILL_DESCRIPTION_MAX:",
        new="    if length < SKILL_DESCRIPTION_MIN or length >= SKILL_DESCRIPTION_MAX:",
    ),
    dict(
        name="M04-column0-comment-swallowed",
        point="description_of: lookahead `(?=^\\S|\\Z)` -> `(?=^\\S*:|\\Z)`; the value no longer ends at a bare column-0 line (round-50 m8 regression: a column-0 comment is swallowed into the description)",
        old='    match = re.search(r"^description:(.*?)(?=^\\S|\\Z)", front, re.S | re.M)',
        new='    match = re.search(r"^description:(.*?)(?=^\\S*:|\\Z)", front, re.S | re.M)',
    ),
    dict(
        name="M05-clauses-from-whole-file",
        point="skill_description_failures: clause source `description` -> `text` (a lane named only in the frontmatter Triggers list, or anywhere else in the file, now binds)",
        old="    clauses = split_clauses(description)",
        new="    clauses = split_clauses(text)",
    ),
    dict(
        name="M06-unreadable-description-pass",
        point="skill_description_failures: one inserted early return -- an unreadable/empty description yields an all-pass verdict (no length check, no missing-lane failures)",
        old="""    description = description_of(text)
    length = len(description)""",
        new="""    description = description_of(text)
    if not description:
        return {"named": 0, "total": 0, "length": 0, "failures": []}
    length = len(description)""",
    ),
    dict(
        name="M07-empty-description-floor-dropped",
        point="G4 floor dropped (`length < SKILL_DESCRIPTION_MIN or` removed): an empty description no longer fails the length check (missing-lane checks still run)",
        old="    if length < SKILL_DESCRIPTION_MIN or length > SKILL_DESCRIPTION_MAX:",
        new="    if length > SKILL_DESCRIPTION_MAX:",
    ),
    dict(
        name="M08-missing-lane-ignored",
        point="skill_description_failures: the does-not-name failure is never appended (a missing adjacent lane is ignored)",
        old="""        if not in_clause:
            failures.append("skill description does not name the non-none "
                            "census lane %s" % lane)
            continue""",
        new="""        if not in_clause:
            continue""",
    ),
    dict(
        name="M09-token-substring-match",
        point="token_in: word-boundary guards `(?<![a-z0-9-])` / `(?![a-z0-9])` dropped -- `kake` matches inside `kakegawa`",
        old="""    return re.search(r"(?<![a-z0-9-])" + re.escape(name) + r"(?![a-z0-9])",
                     text, re.I) is not None""",
        new="""    return re.search(re.escape(name), text, re.I) is not None""",
    ),
    dict(
        name="M10-first-256-chars-only",
        point="skill_description_failures: the parsed description is truncated to its first 256 characters before every check",
        old="""    description = description_of(text)
    length = len(description)""",
        new="""    description = description_of(text)[:256]
    length = len(description)""",
    ),
    dict(
        name="M11-duplicate-lane-accepted",
        point="duplicate_lane_failures: the more-than-one-row test is disabled (a repeated census/province lane is accepted)",
        old="        if len(entries) > 1:",
        new="        if False and len(entries) > 1:",
    ),
    dict(
        name="M12-count-hardcoded-9",
        point="skill_description_failures return: `total` hard-coded to 9 (tuned to the live nine-lane census; any other census is misreported)",
        old="""    return {"named": named, "total": len(non_none), "length": length,
            "failures": failures}""",
        new="""    return {"named": named, "total": 9, "length": length,
            "failures": failures}""",
    ),
]


def load_module(path):
    spec = importlib.util.spec_from_file_location("m_" + hashlib.sha256(str(path).encode()).hexdigest()[:10], path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def run_selftest(path, cap=60):
    t0 = time.monotonic()
    proc = subprocess.run([sys.executable, "-B", str(path), "--self-test"],
                          cwd=str(LANE), stdout=subprocess.PIPE,
                          stderr=subprocess.PIPE, timeout=cap)
    dt = time.monotonic() - t0
    return proc.returncode, proc.stdout.decode("utf-8", "replace"), \
        proc.stderr.decode("utf-8", "replace"), dt


def main():
    MUTDIR.mkdir(parents=True, exist_ok=True)
    results = {"pristine_sha": PRISTINE_SHA, "mutants": [], "probes": {}}

    # -- pristine run of the detector --------------------------------------
    rc, out, err, dt = run_selftest(SRC)
    print("PRISTINE rc=%d %.2fs stdout=%r stderr=%r" % (rc, dt, out.strip(), err.strip()))
    results["pristine"] = {"rc": rc, "stdout": out.strip(), "seconds": round(dt, 2)}
    if rc != 0:
        print("BASELINE FAILURE: inconclusive battery, aborting")
        results["pristine"]["baseline_failure"] = True

    for spec in MUTANTS:
        text = PRISTINE_TEXT
        n = text.count(spec["old"])
        if n != 1:
            print("%s: ANCHOR NOT UNIQUE (%d hits) -- skipped" % (spec["name"], n))
            results["mutants"].append(dict(name=spec["name"], error="anchor %d hits" % n))
            continue
        mtext = text.replace(spec["old"], spec["new"], 1)
        mpath = MUTDIR / (spec["name"] + ".py")
        mpath.write_text(mtext, encoding="utf-8")
        try:
            rc, out, err, dt = run_selftest(mpath)
        except subprocess.TimeoutExpired:
            results["mutants"].append(dict(name=spec["name"], sha256=hashlib.sha256(mtext.encode()).hexdigest(),
                                           verdict="TIMEOUT", seconds=60))
            print("%-38s TIMEOUT" % spec["name"])
            continue
        fails = [l for l in err.splitlines() if l.startswith("FAIL")]
        verdict = "KILLED" if rc != 0 else "SURVIVED"
        results["mutants"].append(dict(
            name=spec["name"], point=spec["point"],
            sha256=hashlib.sha256(mpath.read_bytes()).hexdigest(),
            rc=rc, verdict=verdict, seconds=round(dt, 2),
            stdout=out.strip(), n_fail_lines=len(fails),
            fail_lines=fails[:6],
        ))
        print("%-38s rc=%d %5.2fs %s  (%d FAIL lines)" % (spec["name"], rc, dt, verdict, len(fails)))
        for line in fails[:4]:
            print("    %s" % line)

    # -- restored-bytes evidence: the lane file is re-read and re-run -------
    after = SRC.read_bytes()
    results["restored_sha"] = hashlib.sha256(after).hexdigest()
    rc2, out2, err2, dt2 = run_selftest(SRC)
    results["restored"] = {"rc": rc2, "stdout": out2.strip(), "seconds": round(dt2, 2)}
    print("RESTORED sha=%s rc=%d stdout=%r" % (results["restored_sha"], rc2, out2.strip()))

    # -- differential probes on the survivors ------------------------------
    pristine = load_module(SRC)

    def sf(mod, body):
        with tempfile.TemporaryDirectory() as td:
            p = Path(td) / "SKILL.md"
            p.write_text(body, encoding="utf-8")
            lanes = {lane: "adjacent" for lane in mod.SKILL_LANES}
            lanes["kotoba"] = "none"
            return mod.skill_description_failures(p, lanes)

    # M03: boundary lengths 1023 / 1024 / 1025
    base = pristine.SKILL_DESC_ALL
    rows = []
    for target in (1023, 1024, 1025):
        pad = target - len(base)
        desc = base + " " + "q" * (pad - 1) if pad >= 2 else base[:target]
        body = pristine._skill_md(desc)
        p = sf(pristine, body)
        m3 = load_module(MUTDIR / "M03-cap-off-by-one.py")
        q = sf(m3, body)
        rows.append(dict(target=target, len=len(desc),
                         pristine_failures=len(p["failures"]), pristine_named=p["named"],
                         mutant_failures=len(q["failures"]), mutant_named=q["named"],
                         mutant_first=q["failures"][0][:90] if q["failures"] else None))
        print("M03 boundary len=%d pristine: %d failure(s) named %d | mutant: %d failure(s) named %d %r"
              % (len(desc), len(p["failures"]), p["named"], len(q["failures"]), q["named"],
                 q["failures"][0][:90] if q["failures"] else None))
    results["probes"]["M03_boundary"] = rows

    # M05: lanes named only inside a frontmatter Triggers list
    five = pristine.SKILL_DESC_FIVE
    trig = ("---\nname: kotoba-shokunin\ndescription: >\n  " + five + "\n"
            "Triggers:\n"
            "  - chousa owns deep research\n"
            "  - kama owns local model serving\n"
            "  - kotodama owns worldbuilding and naming\n"
            "  - tameshi owns mutation testing\n"
            "---\n\n# kotoba\n")
    p = sf(pristine, trig)
    m5 = load_module(MUTDIR / "M05-clauses-from-whole-file.py")
    q = sf(m5, trig)
    results["probes"]["M05_triggers"] = {
        "parsed_description_head": pristine.description_of(trig)[:60],
        "pristine": {"named": p["named"], "failures": p["failures"]},
        "mutant": {"named": q["named"], "failures": q["failures"]},
    }
    print("M05 triggers: pristine named %d failures %d | mutant named %d failures %d"
          % (p["named"], len(p["failures"]), q["named"], len(q["failures"])))

    # M09: kake never named; only kakegawa
    kake = ("Prompt and skill craft. Sibling boundary: kakegawa owns its own "
            "SKILL.md content, and kagi, kama, kasegi, kengaku, kotodama, "
            "kumitate, tameshi and chousa own theirs; fixes route to the "
            "owning lane.")
    body = pristine._skill_md(kake)
    p = sf(pristine, body)
    m9 = load_module(MUTDIR / "M09-token-substring-match.py")
    q = sf(m9, body)
    results["probes"]["M09_kakegawa"] = {
        "pristine": {"named": p["named"], "failures": p["failures"]},
        "mutant": {"named": q["named"], "failures": q["failures"]},
    }
    print("M09 kakegawa: pristine named %d failures %d | mutant named %d failures %d"
          % (p["named"], len(p["failures"]), q["named"], len(q["failures"])))

    # fixture geometry for the report
    all_desc = pristine.SKILL_DESC_ALL
    pos = {lane: all_desc.find(lane) for lane in pristine.SKILL_LANES}
    results["probes"]["fixture_geometry"] = {"len_SKILL_DESC_ALL": len(all_desc),
                                             "first_index_per_lane": pos,
                                             "len_SKILL_DESC_FIVE": len(five)}
    print("geometry: len(ALL)=%d len(FIVE)=%d first-index %s" % (len(all_desc), len(five), pos))

    # -- live --skill differential for the survivors (read-only) -----------
    if CENSUS.is_file():
        live = {}
        for tag, path in [("pristine", SRC),
                          ("M03", MUTDIR / "M03-cap-off-by-one.py"),
                          ("M05", MUTDIR / "M05-clauses-from-whole-file.py"),
                          ("M09", MUTDIR / "M09-token-substring-match.py")]:
            t0 = time.monotonic()
            try:
                proc = subprocess.run(
                    [sys.executable, "-B", str(path), str(CENSUS),
                     "--province", str(LANE / "PROVINCE.md"),
                     "--skill", str(LANE / "SKILL.md")],
                    cwd=str(LANE), stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                    timeout=120)
                tail = [l for l in proc.stdout.decode("utf-8", "replace").splitlines()][-3:]
                live[tag] = {"rc": proc.returncode, "tail": tail,
                             "seconds": round(time.monotonic() - t0, 1)}
                print("LIVE %-9s rc=%d %s | %s" % (tag, proc.returncode,
                                                   round(time.monotonic() - t0, 1), " / ".join(tail)))
            except subprocess.TimeoutExpired:
                live[tag] = {"rc": "timeout"}
                print("LIVE %-9s timeout" % tag)
        results["probes"]["live_skill_mode"] = live

    (OUT / "results.json").write_text(json.dumps(results, indent=1), encoding="utf-8")
    print("WROTE %s" % (OUT / "results.json"))


if __name__ == "__main__":
    main()
