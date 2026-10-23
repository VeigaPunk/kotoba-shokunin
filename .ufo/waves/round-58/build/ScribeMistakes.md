Result: DONE — drafted M70–M74, including four routed defects and one newly mined mistake with an isolated failing demonstration; round-58 fix implementation is not independently verified here.

# Scope and provenance

This is the proposed `## Mistakes` section for `corpus/lessons/round-58.md`; no lesson or product file was edited. The four routed-defect fix pointers below are the routes frozen in `plans/round-58.md`, not claims that their implementation has landed. The round-57 evidence and plan references were read directly. The new mined item is M74, from `.ufo/waves/round-57/a3/falsify/A3CriticScorecardCalib.md` M03; a targeted search of `corpus/lessons/` for `38 Sources entries`, `current Sources entries = 33`, `Sources-entry count`, and `SHONEN.md:6.*Sources` returned no matches. The broader issue is not in an existing lesson entry.

The required counter-source reads were completed: `verifiers/check_command_files.py` (frozen C1 spec) and `verifiers/check_sweep_mutants.py` (frozen record-only C2 probe). Neither counter was run. No source fetch, build, test, lint, or formatting command was run; no tools were installed or updated.

# Proposed lesson text (verbatim)

```markdown
## Mistakes

- **M70 `withdrawn-counter-kept-as-gate`** · `verifiers/check_infoless_fences.py` remained registered as a `gate` although C2 was withdrawn after hollow controls met its frozen predicate (`corpus/lessons/round-57-verifier-spotcheck.md:92-104,203-205`) · captured-by: the round-57 non-author verifier spot-check, routed defect R1 · fix: round 58 relabels the `SKILL.md` gate-registry row as `probe` and records the withdrawal reason (`plans/round-58.md:13`) · shown able to fail: the round-57 controls `CtlC2GeneratorKeyed`, `CtlC2DoNothingJunk`, and `CtlC2CharShortcuts` each reached `120 of 120`, exit 0, and `MutC2Counter` also met the predicate; the spot-check therefore withdrew the claim while the registry still called its counter a gate (`corpus/lessons/round-57-verifier-spotcheck.md:98-104,203-205`).

- **M71 `self-test-no-successful-main-path`** · the frozen round-57 C1 v2 self-test called `main()` only with an invalid revision, which returns before the real measurement path; it tested `predicate()` directly but never the final CLI return (`.ufo/waves/round-57/a3/falsify/A3CriticScorecardCalib.md:62-70`; routed R4: `corpus/lessons/round-57-verifier-spotcheck.md:210`) · captured-by: `A3CriticScorecardCalib` M05 / the round-57 non-author spot-check R4 · fix: add a successful-main-path arm to `check_plugin_manifests.py` and give the new C1 counter one from birth (`plans/round-58.md:16`) · shown able to fail: the existing pristine `python3 -B verifiers/check_plugin_manifests.py --self-test` passed with `0 failure(s) over 235 assertions`, while the recorded AST probe found only `main(['--rev', 'not-a-hash'])`; no successful-path mutant was run, so the mutation consequence is not demonstrated here ([INFERENCE] from the unexercised path).

- **M72 `dead-lowercase-home-path`** · the round-57 `SKILL.md` Sources inventory used `/home/vgpnk/projects/`, which does not exist on the host; the capitalized `/home/vgpnk/Projects/` is the live path (`.ufo/waves/round-57/a3/falsify/A3ReviewR2R6.md:27-30`; routed R5: `corpus/lessons/round-57-verifier-spotcheck.md:211`) · captured-by: `A3ReviewR2R6` F3 · fix: correct the dead lowercase paths to the live path (`plans/round-58.md:17`; target `SKILL.md:514-515` in the plan) · shown able to fail: `ls -d /home/vgpnk/projects` produced `No such file or directory` (`A3ReviewR2R6.md:29`).

- **M73 `correction-sweep-arms-weak` (R3; C2 withdrawn)** · four new self-test arms and three registry rows still let 7 of 11 mutants survive; all three weakened declarations and all four dropped arms survived (`corpus/lessons/round-57.md:169-173`; `.ufo/waves/round-57/a3/falsify/A3MutCorrectionSweep.md:39-55`) · captured-by: the round-57 `A3MutCorrectionSweep` mutation probe, routed defect R3 / M68 · fix: add behavioral arms to `verifiers/check_correction_sweep.py` (`plans/round-58.md:75-95`); C2 is withdrawn, so `check_sweep_mutants.py` is a record only, not a claim (`plans/round-58.md:86-95`) · shown able to fail: in the round-57 probe, each weakened-declaration mutant and dropped-arm mutant still let `--self-test` exit 0; the latter also reduced the assertion count from 18 to 17 (`A3MutCorrectionSweep.md:27-29,46-53`).

- **M74 `stale-shonen-source-inventory`** (mined) · `SHONEN.md:6` calls the Sources inventory 38 entries, while the current `SKILL.md` Sources section has 33 (`.ufo/waves/round-57/a3/falsify/A3CriticScorecardCalib.md:44-50`) · captured-by: `A3CriticScorecardCalib` M03 · fix: change the current inventory to 33 or label the B2 figure as the round-46 historical count; neither correction is claimed landed here (`A3CriticScorecardCalib.md:48-52`) · shown able to fail: in sandbox `07c33d73ddce769d9cea2844a6313164401b5478` (`/fast/scratch/hyaku/kotoba-r58/ScribeMistakes`), `timeout 30 python3 -B -c 'from pathlib import Path; s=Path("SKILL.md").read_text().splitlines(); h=s.index("## Sources"); count=sum(x.startswith("- ") for x in s[h+1:]); line=Path("SHONEN.md").read_text().splitlines()[5]; print("SHONEN current Sources entries:", count); print("SHONEN.md:6:", line); raise SystemExit(1 if "38 Sources entries" in line and count != 38 else 0)'` printed `SHONEN current Sources entries: 33` and `SHONEN.md:6:   evidence: `.ufo/round-46/scouts/B2.md` (SKILL.md inventory: 7 anatomy rows, 5 decision rows, 41 checklist boxes 15/9/9/8, 38 Sources entries; lane-run)`; exit 1.
```

# Executed commands and outcomes

The seat sandbox path was initially absent:

```sh
timeout 5 test ! -e /fast/scratch/hyaku/kotoba-r58/ScribeMistakes
```

Exit 0; no output. Sandbox clone and checkout (both were bounded by `timeout 120`):

```sh
timeout 120 sh -c 'unset GIT_DIR GIT_WORK_TREE GIT_INDEX_FILE; git clone -q /home/vgpnk/Projects/shokunin/kotoba-shokunin /fast/scratch/hyaku/kotoba-r58/ScribeMistakes && git -C /fast/scratch/hyaku/kotoba-r58/ScribeMistakes checkout -q 07c33d73ddce769d9cea2844a6313164401b5478'
```

Exit 0; no output. The clone was used only for the read-only M74 comparison above; no sandbox commit was made.

I first tried the following read-only comparison with a mistaken leading-tab assumption in the census-row regex:

```sh
timeout 10 python3 -B -c 'from pathlib import Path; import re; report=Path("/home/vgpnk/Projects/shokunin/.ufo/reports/round-55/kotoba.md").read_text(); end=Path("/home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-55/census-end.txt").read_text(); line=next(x for x in report.splitlines() if x.startswith("Census, start and end:")); reported=set(re.findall(r"S\d{3}", line)); ending=set(re.findall(r"\tkotoba\tW04\t(S\d{3})", end)); missing=sorted(ending-reported); print("report census line:", line); print("end W04 IDs:", ", ".join(sorted(ending))); print("end W04 absent from report census line:", ", ".join(missing)); raise SystemExit(1 if missing else 0)'
```

It printed an empty `end W04 IDs` and `end W04 absent ...` and exited 0. This was a false negative caused by the regex; I discarded it and did not use it as evidence.

The corrected command matched the actual `kotoba\tW04` row prefix:

```sh
timeout 10 python3 -B -c 'from pathlib import Path; import re; report=Path("/home/vgpnk/Projects/shokunin/.ufo/reports/round-55/kotoba.md").read_text(); end=Path("/home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-55/census-end.txt").read_text(); line=next(x for x in report.splitlines() if x.startswith("Census, start and end:")); reported=set(re.findall(r"S\d{3}", line)); ending=set(re.findall(r"kotoba\tW04\t(S\d{3})", end)); missing=sorted(ending-reported); print("report census line:", line); print("end W04 IDs:", ", ".join(sorted(ending))); print("end W04 absent from report census line:", ", ".join(missing)); raise SystemExit(1 if missing else 0)'
```

Observed: end W04 IDs were `S018, S019, S021, S054, S055, S056, S065`; `S065` was absent from the report's census line; exit 1. This corroborates the underlying round-55 spot-check evidence (`corpus/lessons/round-55-verifier-spotcheck.md:34-38`) but is not the M74 demonstration.

The M74 diagnostic command/output/exit are pasted verbatim in the draft entry. No round-58 counter, gate, verifier, or test was executed by this seat.

# Behavior, gates, touched surfaces, limits

- **Behavior:** lesson prose only; no source, verifier, gate, counter, or rule changed.
- **Gates:** no builds/tests/linters/formatters run. The only success/failure demonstrations executed were static text comparisons; neither runs lane code. The two counter sources required by the round context were read before drafting.
- **Touched surfaces:** this report file only: `.ufo/waves/round-58/build/ScribeMistakes.md`. Read-only sandbox: `/fast/scratch/hyaku/kotoba-r58/ScribeMistakes` at `07c33d73ddce769d9cea2844a6313164401b5478`.
- **Out of scope:** editing `corpus/lessons/round-58.md`; implementing or validating R1/R4/R5/R3; changing the withdrawn C2 claim; verifying C1; any lane Git/jj write, commit, push, or publication.
- **Known limits:** M70–M73 fix pointers state the frozen round-58 plan, not verified landed fixes. M71's success-path mutation remains explicitly unshown. The census comparison's first parser was wrong and is disclosed above; only the corrected run is evidence. M74's fix is not part of the frozen plan.
- **Installs/updates:** none.

# Artifact

- `/home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-58/build/ScribeMistakes.md`
