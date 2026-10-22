# C1RegressionArm — the configured-root regression arm (plan Q05)

Seat: `KotobaR48.C1RegressionArm` (leaf; no delegation). Scope: add a self-test arm to the C1
consumer `verifiers/verify_harness_independent.py` `self_test()`, show it FAILS on the base
consumer and PASSES on the candidate, and answer the floor question.
Base consumer: `75f671b109d8eddd0d64c1429bd6379fe577175a` (pre-repair).
Candidate: `26035dcec54d8e42f3a8b47ae8ca551c18aec295` (consumer sha256 `2d824c0b…`).

## Findings

**F1 — Q05 was unmet; the arm is now written.** The candidate patch touches `derive()` only, so it
ships no regression arm (`C1AltImplementation.md` finding 4). My arm adds **11 assertions**
(104 → 115) to `self_test()`, in four fixture shapes, all built from a new helper
`build_configured_root_fixture()`:
- `skill/<solo-s>/SKILL.md` + `skills/<solo-p>/SKILL.md` (one skill in each configured root),
- the same-name pair `skill/<twin>/SKILL.md` + `skills/<twin>/SKILL.md` (two directories, one name),
- `skills/<not-a-skill>/` (a directory with no `SKILL.md`) and `skills/README.md` (a plain file),
- the nested skill `skill/group/zeta/SKILL.md` + `skills/group/eta/SKILL.md` (one level below a
  root's direct child — the L1's added requirement).
The fixture's opencode log names **no** source root, so every name beyond the shared agents root
can only have come from the configured roots. Asserted value of `oc.roots.names_plus_builtin`:
**5** (agents root `alpha`,`beta` + `solo-s`,`solo-p`,`twin`).

**F2 — the arm is a real discriminator (red-before).** Base consumer + arm: **exit 1, 7 failures
over 115 assertions**, every failure naming a configured-root arm (details in E2). The same arm on
the candidate: **exit 0, 0 failures over 115 assertions** (E3). The floors guard agrees: on the
base tree it prints `FAIL harness_independent observed=115 floor=104 self_test_failures=7`, exit 1
(E6); on the candidate tree, all nine instruments PASS (E5).

**F3 — the arm kills the L1's routed recursive mutant (F1 of `C1RulerTargetMutants.md`).** The
committed oracle has no nested case, so `path.rglob("SKILL.md")` + `parent.name` passes the ruler
clean. Against my arm the same mutant is red: **exit 1, 6 failures**, including the dedicated
direct-child-scope assertion `a nested skill is not a name (direct children only): got 2 want 0`
(E4). The arm therefore closes the coverage gap on the consumer side, without touching the frozen
oracle or its pinned sha256.

**F4 — the floor: no bump is required for green; a bump is required by the ratchet convention.**
`check_assertion_floors.py` compares `observed >= floor`, so the arm alone leaves the guard green
(`PASS harness_independent observed=115 floor=104`, exit 0). The registry's own BUMP-IN-STEP RULE
and its docstring history (`93->104` at round 39) ratchet the floor to the settled count, i.e.
**104 → 115**, which needs the same change in **four** places: `verifiers/floors-registry.json`,
the `EXPECTED_INSTRUMENTS` table, the `INSTRUMENTS` table and the guard docstring. I did **not**
put that in `arm.patch` (it is a different file set and the L1 may land the alternative consumer);
I ship it separately as `floors-bump.patch`, verified: guard exit 0 with
`PASS harness_independent observed=115 floor=115`, and the guard's own `--self-test` still
`0 failure(s) over 150 assertions`, exit 0 (E7).

**F5 — the arm is wording-robust.** The detail-text assertion checks that the row's evidence names
both configured roots (`"skill"`, `"skills"`), not one fixed sentence, so it survives the
alternative consumer's re-worded detail text (`C1AltImplementation.md` row "Detail text"). The
value assertions depend only on the enumeration contract, not on prose.

**F6 — residual, routed, not mine.** The frozen oracle
`.ufo/round-48/oracle/config-root-cases.json` still has no nested-skill case (grep for
`nested|group|zeta|depth`: no hit), so the *ruler* remains blind to a recursive enumeration. My
arm is consumer-side only; the oracle amendment (and its pinned sha256) is the L1's decision.

## Evidence (commands, exit codes, paths, hashes)

Private trees (all under `/fast/scratch/hyaku/kotoba-r48-a2/seats/C1RegressionArm/`, clones of the
candidate clone; no write in the lane, the fleet repo or a sibling lane):

| tree | content | consumer sha256 |
|---|---|---|
| `work-cand/` | candidate `26035dc` + the arm | `d67b1b6e9ba0e614f643adda2686c9db8d57c31741de01780be3fcb06c4f7937` |
| `work-base/` | base `75f671b` + the arm | `0c8f28be606837c38809604b05c0f08f122b80e3d2b4cb3822dc59980bff7950` |
| `work-mutant/` | candidate + the arm + recursive enumeration | `b45c9f6f176bc6b356e9e850b00b591b41a4e05c8ce5d2e3a1c7b5b8fec33852` |

- **E1** `git -C work-cand diff -- verifiers/verify_harness_independent.py > arm.patch` →
  `arm.patch` sha256 `1b27627ca0121c7895edaf0601817c59c6a4a55c5c7ec7ecd68eb41770eddf28`, 180 lines;
  applies cleanly to the base tree (`git apply`: hunk 1 at 875 (offset −5), hunk 2 at 1339 (offset −5)).
  `python3 -m py_compile work-cand/verifiers/verify_harness_independent.py` → exit 0.
- **E2 base** `cd work-base && python3 -B verifiers/verify_harness_independent.py --self-test` →
  **exit 1**, `7 failure(s) over 115 assertions`:
  `the configured roots are enumerated: got 2 want 5`; `the value equals an independent
  enumeration: got (2, [...]) want (5, [...])`; `the nested skill is on disk but not counted: got
  (True, 2) want (True, 5)`; `without the same-name pair the count drops by one: got 0 want 1`;
  `a directory without SKILL.md and a plain file are not names: got 2 want 4`; `a root the log names
  is still enumerated: got 3 want 6`; `a root named by the log and by the configuration is one
  root: got 4 want 5`.
- **E3 candidate** `cd work-cand && python3 -B verifiers/verify_harness_independent.py --self-test` →
  **exit 0**, `0 failure(s) over 115 assertions`.
- **E4 recursive mutant** (one edit in `derive()`: `for entry in sorted(path.rglob("SKILL.md")):
  names.add(entry.parent.name)`) `cd work-mutant && python3 -B verifiers/verify_harness_independent.py
  --self-test` → **exit 1**, `6 failure(s) over 115 assertions`: `the configured roots are
  enumerated: got 7 want 5`; `the value equals an independent enumeration: got (7, [...]) want
  (5, [...])`; `a nested skill is not a name (direct children only): got 2 want 0`; `a directory
  without SKILL.md and a plain file are not names: got 6 want 4`; `a root the log names is still
  enumerated: got 8 want 6`; `a root named by the log and by the configuration is one root: got 7
  want 5`.
- **E5 guard, floor not bumped** `cd work-cand && python3 -B verifiers/check_assertion_floors.py` →
  **exit 0**, nine PASS lines, `PASS harness_independent observed=115 floor=104`.
- **E6 guard on the base tree** `cd work-base && python3 -B verifiers/check_assertion_floors.py` →
  **exit 1**, `FAIL harness_independent observed=115 floor=104 self_test_failures=7`; the other eight
  instruments PASS.
- **E7 guard, floor bumped in-step** `cd work-bump && python3 -B verifiers/check_assertion_floors.py` →
  **exit 0**, `PASS harness_independent observed=115 floor=115`; `python3 -B
  verifiers/check_assertion_floors.py --self-test` → **exit 0**, `0 failure(s) over 150 assertions`.

## Files delivered (outside the lane; the L1 integrates)

- `/fast/scratch/hyaku/kotoba-r48-a2/seats/C1RegressionArm/arm.patch` — the unified diff against
  the candidate (consumer only). sha256 `1b27627ca0121c7895edaf0601817c59c6a4a55c5c7ec7ecd68eb41770eddf28`.
- `/fast/scratch/hyaku/kotoba-r48-a2/seats/C1RegressionArm/floors-bump.patch` — the optional
  four-place floor ratchet (104 → 115). sha256
  `3e4ff950d3b8b923396d2a2bdb9b501911562d0794e7e37a75b61f86fad06471`. Apply **after** the arm.
- Report: `.ufo/waves/round-48/build/C1RegressionArm.md` (this file; the only file written in the lane).
- Landing status: the L1 applied both patches to the lane working tree during this session (the
  lane consumer is byte-identical to `work-cand`, and the lane's floor row reads 115 in the
  registry and in both guard tables).

## Risks and notes

- The arm adds 11 assertions to a floored instrument; if the L1 lands the alternative consumer
  instead, its own arm assertions must be counted and the floor set to the settled total of
  whichever consumer lands.
- The arm's value expectations assume the contract "direct children of `--oc-config/skill` and
  `--oc-config/skills` holding a `SKILL.md`, plus the shared agents root, names as a set". If the
  L1 changes the contract's scope, this arm (and the oracle) must change with it.
- Tooling: no install or upgrade was needed or performed (`python3` and `git` were already
  present). No web source was opened this session, so no SOURCES row is owed by this seat.
- Lane custody: the only file I wrote in the lane is this report. No git/jj write was run in the
  lane, the fleet repo or any sibling lane; all my work is in the private clones under
  `seats/C1RegressionArm/`. Later in the session the L1 applied both of my patches to the lane
  working tree: the lane's `verifiers/verify_harness_independent.py` is now byte-identical to my
  `work-cand` copy (sha256 `d67b1b6e9ba0e614f643adda2686c9db8d57c31741de01780be3fcb06c4f7937`,
  candidate + arm) and the lane's floor row reads 115 in all three tables plus the registry,
  matching `floors-bump.patch` exactly. At the time of writing, the lane working tree also
  carries ` M SKILL.md` and ` M corpus/SOURCES.md` from other seats; HEAD is still `75f671b`.

## Appendix — the unified diff against the candidate (verbatim)

The prose above is within the 150-line bound; this appendix is the verbatim diff the assignment
asked to be delivered in the report (180 lines, also at `seats/C1RegressionArm/arm.patch`).

```diff
diff --git i/verifiers/verify_harness_independent.py w/verifiers/verify_harness_independent.py
index cf25d25..134f756 100644
--- i/verifiers/verify_harness_independent.py
+++ w/verifiers/verify_harness_independent.py
@@ -880,6 +880,68 @@ def build_fixture(root: Path) -> Substrate:
     return Substrate(binary, agents, db, log, config)
 
 
+# ---------------------------------------------------------------------------
+# round 48 (C1): the configured-root fixture
+# ---------------------------------------------------------------------------
+def build_configured_root_fixture(root: Path, twin: bool = True,
+                                  nested: bool = False) -> Substrate:
+    """A substrate whose --oc-config holds the two configured skill roots.
+
+    Round 48 (C1).  The instrument used to enumerate only the roots the
+    opencode log names as sources, so a skill sitting in --oc-config/skill/
+    or --oc-config/skills/ was invisible to oc.roots.names_plus_builtin
+    unless the log happened to name that root.  The fixture puts, under the
+    config root:
+
+        skill/<solo-s>/SKILL.md     one skill in the singular root
+        skills/<solo-p>/SKILL.md    one skill in the plural root
+        skill/<twin>/SKILL.md       the same-name pair, one half ...
+        skills/<twin>/SKILL.md      ... and the other half
+        skills/<not-a-skill>/       a directory with no SKILL.md
+        skills/README.md            a plain file, not a skill directory
+
+    The opencode log names no root at all, so every name beyond the shared
+    agents root can only have come from the configured roots.  `twin=False`
+    drops the same-name pair, which makes the pair's set semantics
+    measurable: the count must fall by exactly one, not two.  The directory
+    without a SKILL.md and the plain file make the enumeration operator
+    measurable too: neither may contribute a name.
+
+    `nested=True` adds skills one level deeper than a root's direct child
+    (skill/group/zeta/SKILL.md, skills/group/eta/SKILL.md).  The frozen
+    contract enumerates a root's DIRECT children only, so a nested skill is
+    not a name; a recursive enumeration would report both.
+    """
+    fixture = build_fixture(root)
+    config = fixture.oc_config
+
+    def skill(root_name: str, folder: str, name: str) -> None:
+        (config / root_name / folder).mkdir(parents=True)
+        (config / root_name / folder / "SKILL.md").write_text(
+            "---\nname: %s\ndescription: Use %s briefly.\n---\n\n# %s\n"
+            % (name, name, name), encoding="utf-8")
+
+    skill("skill", "solo-s", "solo-s")
+    skill("skills", "solo-p", "solo-p")
+    if twin:
+        skill("skill", "twin", "twin")
+        skill("skills", "twin", "twin")
+    (config / "skills" / "not-a-skill").mkdir(parents=True)
+    (config / "skills" / "README.md").write_text("not a skill\n",
+                                                 encoding="utf-8")
+    if nested:
+        skill("skill", "group/zeta", "zeta")
+        skill("skills", "group/eta", "eta")
+    return fixture
+
+
+def _name_log_root(fixture: Substrate, directory: Path) -> None:
+    """Append a log line that names `directory` as a skill source root."""
+    with open(fixture.oc_log, "a", encoding="utf-8") as handle:
+        handle.write('run=eee message="skills rescanned" '
+                     'sources="[\\"directory:%s\\"]"\n' % directory)
+
+
 # ---------------------------------------------------------------------------
 # fixture battery: pinned mutant trees driven through this file's own CLI
 # ---------------------------------------------------------------------------
@@ -1282,6 +1344,106 @@ def self_test() -> int:
         expect("dup split: a path without the home prefix is its own key",
                root_key("/opt/elsewhere/SKILL.md"), "/opt/elsewhere/SKILL.md")
 
+        # ---- round 48 (C1): the configured roots -------------------------
+        # A skill in --oc-config/skill/ or --oc-config/skills/ must be
+        # enumerated even when the opencode log names neither root.  The
+        # fixture names no root at all, so every name beyond the shared
+        # agents root can only have come from the configured roots.  The
+        # fixture also carries a NESTED skill (skill/group/zeta/SKILL.md):
+        # the frozen contract enumerates a root's direct children only, so
+        # a nested skill is not a name.
+        cfg_root = Path(tmp) / "cfg"
+        cfg_root.mkdir()
+        cfg = build_configured_root_fixture(cfg_root, nested=True)
+        cfg_rows = {r["check"]: r for r in derive(cfg)}
+        cfg_value = cfg_rows["oc.roots.names_plus_builtin"]["value"]
+        expect("round 48: fixture premise -- the log names no source root",
+               ("sources=" in cfg.log_text(), "directory:" in cfg.log_text()),
+               (False, False))
+        expect("round 48: fixture premise -- both configured roots exist",
+               ((cfg.oc_config / "skill").is_dir(),
+                (cfg.oc_config / "skills").is_dir()),
+               (True, True))
+        # alpha, beta (the shared agents root) + solo-s, solo-p, twin (the two
+        # configured roots; the same-name pair is one name)
+        expect("round 48: the configured roots are enumerated",
+               cfg_value, 5)
+        # the same expectation, computed from the fixture tree rather than
+        # hard-coded: the agents root's own names plus the DIRECT children of
+        # the two configured roots that hold a SKILL.md.  Mirrored here, not
+        # imported, so the arm states the contract instead of restating a
+        # number.
+        expected_names = {"alpha", "beta"}
+        for root_name in ("skill", "skills"):
+            for entry in sorted((cfg.oc_config / root_name).iterdir()):
+                if (entry / "SKILL.md").is_file():
+                    expected_names.add(entry.name)
+        expect("round 48: the value equals an independent enumeration",
+               (cfg_value, sorted(expected_names)),
+               (5, ["alpha", "beta", "solo-p", "solo-s", "twin"]))
+        # the row's own detail text must name the configured roots (the base
+        # mislabelled the two families); checked on the root names rather
+        # than on one wording, so it survives a re-worded detail string.
+        evidence = cfg_rows["oc.roots.names_plus_builtin"]["evidence"]
+        expect("round 48: the row's evidence names the configured roots",
+               ("skill" in evidence, "skills" in evidence), (True, True))
+
+        # the direct-child scope: a skill nested deeper than a root's direct
+        # child is not a name, so adding it must move the count by nothing.
+        # A recursive enumeration of the same roots would report zeta and
+        # eta and move the count by two.
+        flat_root = Path(tmp) / "cfg-flat"
+        flat_root.mkdir()
+        flat = build_configured_root_fixture(flat_root)
+        flat_rows = {r["check"]: r for r in derive(flat)}
+        expect("round 48: a nested skill is not a name (direct children only)",
+               cfg_value - flat_rows["oc.roots.names_plus_builtin"]["value"], 0)
+        expect("round 48: the nested skill is on disk but not counted",
+               ((cfg.oc_config / "skill" / "group" / "zeta" / "SKILL.md").is_file(),
+                flat_rows["oc.roots.names_plus_builtin"]["value"]),
+               (True, 5))
+
+        # the same-name pair: two directories in two roots, one name.  The
+        # count must fall by exactly one when the pair is removed, and the
+        # directory without a SKILL.md and the plain file must contribute
+        # nothing (otherwise the count would be 6 and 5).
+        notwin_root = Path(tmp) / "cfg-notwin"
+        notwin_root.mkdir()
+        notwin = build_configured_root_fixture(notwin_root, twin=False,
+                                               nested=True)
+        notwin_rows = {r["check"]: r for r in derive(notwin)}
+        expect("round 48: without the same-name pair the count drops by one",
+               cfg_value - notwin_rows["oc.roots.names_plus_builtin"]["value"],
+               1)
+        expect("round 48: a directory without SKILL.md and a plain file are "
+               "not names",
+               notwin_rows["oc.roots.names_plus_builtin"]["value"], 4)
+
+        # no-harm: the union is not a replacement.  A root the log DOES name
+        # is still enumerated alongside the configured roots ...
+        logext_root = Path(tmp) / "cfg-logext"
+        logext_root.mkdir()
+        logext = build_configured_root_fixture(logext_root, nested=True)
+        named = Path(tmp) / "named-root"
+        (named / "logged").mkdir(parents=True)
+        (named / "logged" / "SKILL.md").write_text(
+            "---\nname: logged\ndescription: Use logged briefly.\n---\n\n"
+            "# logged\n", encoding="utf-8")
+        _name_log_root(logext, named)
+        logext_rows = {r["check"]: r for r in derive(logext)}
+        expect("round 48: a root the log names is still enumerated",
+               logext_rows["oc.roots.names_plus_builtin"]["value"], 6)
+        # ... and a root named twice (by the log AND by the configuration) is
+        # still one root, so the count does not move.
+        logsame_root = Path(tmp) / "cfg-logsame"
+        logsame_root.mkdir()
+        logsame = build_configured_root_fixture(logsame_root, nested=True)
+        _name_log_root(logsame, logsame.oc_config / "skills")
+        logsame_rows = {r["check"]: r for r in derive(logsame)}
+        expect("round 48: a root named by the log and by the configuration is "
+               "one root",
+               logsame_rows["oc.roots.names_plus_builtin"]["value"], 5)
+
     fixture_battery(expect)
 
     for failure in failures:
```
