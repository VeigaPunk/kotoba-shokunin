Result: MIXED — the C2 statement is exactly the counter's printed line, but `M of M` can be reached by registries that misdescribe gates. An honest registry at this tree scores 19 of 23, and two ways of reaching 23 of 23 are not named anywhere in the plan.

Seat: KotobaR54.CriticC2Sizing (critic). Axes judged: consistency, calibration. Counter read and run at the plan commit
`e33715486a45a4a857b64c30e6b695f7995858b8` (blob `d3e82a2b…`, sha256 `86c00395…f6e0`, identical at the tip and in my
sandbox). No lane file was edited. Sandbox: `/fast/scratch/hyaku/kotoba-r54/CriticC2Sizing` (clone at `7ad05d34`). Nothing
was installed.

## Runs

| Command (cwd) | Exit | Last line |
|---|---|---|
| `python3 -B verifiers/check_gate_registry.py --rev e33715486a45…` (lane, 21:15:45Z) | 1 | `gate registry rows conformant 0 of 23 lane verifiers; phantom 0` |
| same, `--rev 7ad05d342d75…` and `--rev HEAD` (= `d051ec40`) | 1 | `… 0 of 23 …; phantom 0` |
| `python3 -B verifiers/check_gate_registry.py --self-test` | 0 | `self-test: 0 failure(s) over 22 assertions` |
| `python3 -B scratch/worlds.py` (sandbox, 21:18:21Z) — five SKILL.md worlds committed on `7ad05d34` | 0 | see the table below |

| World (sandbox commit) | Counter exit | Counter line | Rows marked `no` |
|---|---|---|---|
| W0 honest (`46545fd5`) | 1 | `conformant 19 of 23 …; phantom 0` | the four verifiers below: `gate with self-test none` |
| W1 probe dodge (`064ac427`): those four as `probe`, `0=clean`, `none`, `none` | 0 | `conformant 23 of 23 …; phantom 0` | none |
| W2 flag dodge (`ee6ca2c4`): those four as `gate`, self-test `--rev`, or the borrowed `--self-test` for opencode_repin | 0 | `conformant 23 of 23 …; phantom 0` | none |
| W3 misdescription battery (`db7f22a1`): W2 plus attacks 1–9 below, plus two ghost rows | 0 | `conformant 23 of 23 …; phantom 0` | none |
| W4 control (`b49abfdd`): W2 plus pinned `verifiers/gone.json` | 1 | `conformant 22 of 23 …; phantom 0` | check_substrate_pins: `pinned path verifiers/gone.json does not exist` |

W4 shows that the counter works in the sandbox. Every W3 row below was accepted, and the counter's `why` list was empty for each one.

## The load-bearing finding: the target is honestly unreachable at this tree

Four verifiers are gates under PROTOCOL.md § Gate standard. Each exits 1 on failure (`box_proof_case_deletion.py:343-344`,
`check_alwayson_boxes.py:166`, `check_callee_rename.py:203`, `check_opencode_repin.py:133`), so none is a "tool that cannot
fail". None of the four has a self-test option. Running `python3 -B verifiers/<f> --self-test` on each in the sandbox gives
exit 2 with argparse `the following arguments are required: --rev` (for callee_rename: `one of the arguments --rev --root is
required`). The counter rule `a gate may not say none` (docstring line 31) therefore leaves three ways to reach `23 of 23`:

1. Add real self-test modes to four scripts. Three of them call themselves frozen counters of earlier rounds:
   `check_alwayson_boxes.py:2` (round 53 C2), `check_callee_rename.py:2` (round 52 C1) and `check_opencode_repin.py:2` (round 53 C1).
   [INFERENCE] Editing those scripts changes blobs that earlier verdicts cite.
2. Relabel them `probe` (W1). The plan names gate-versus-probe as reviewer judgment, so this dodge is visible.
3. Cite a flag that occurs somewhere in the file but is not a self-test (W2). The plan does not name this, so the dodge is silent.

This is already happening. `.ufo/waves/round-54/build/RegCheckOpencodeRepin.md:3` drafts the row with self-test
`` `--self-test` `` for `check_opencode_repin.py`. Its own lines 11 and 18 say that the literal is the nested call into
`verify_surfaces.py` (`check_opencode_repin.py:112`) and that the script "offers no standalone `--self-test`". The counter
will count that row as conformant, even though the row records a self-test spelling the script rejects. By contrast,
`RegBoxProofCaseDeletion.md:1` and `RegCheckAlwaysonBoxes.md:1` record `none` and accept that their rows will be rejected.

## Attacks

| # | Attack (the C2 claim says no more than its counter checks) | Verdict | Evidence | Named in the plan as reviewer judgment? |
|---|---|---|---|---|
| A0 | The statement `gate registry rows conformant <M> of <M> lane verifiers; phantom 0` is the printed line, and M is a sound universe | HOLDS | Printed line `check_gate_registry.py:305-306`. Outside `verifiers/*.{py,sh}`, the only `.py`/`.sh` file at `7ad05d34` is a fixture (`verifiers/fixtures/checklist/delegated-py-suffix`). The before-value of 21 at `422ffd10` plus the two new counters gives 23, which matches the run. | — |
| A1 | A self-test flag that occurs only in a comment or docstring still counts | BREAKS | W3: `box_proof_case_deletion.py` with self-test `` `--box-proof` ``, which occurs only in its docstring (line 8) and in a subprocess argument list for another script (line 183); it was accepted. The check is `f.encode() not in src` (`:165`). | Silent. The plan names only "a self-test flag that is not in the file". |
| A2 | A flag the script does not accept still counts (borrowed literal, or a non-self-test option) | BREAKS | W2: `--rev` for three scripts, and the borrowed `--self-test` for opencode_repin. W3: `check_gate_registry.py` with `` `--selftest` ``, which occurs only inside its own self-test string (`:238`). All accepted. Live case: RegCheckOpencodeRepin.md:3. | Silent |
| A3 | A fragment flag counts (Q32: identity matched by substring) | BREAKS | W3: `verify_surfaces.py` with `` `--s` `` was accepted. The self-test has no fragment must-fail arm. Its only flag arm, `--selftest` against `--self-test` (`:237-238`), tests an absent flag, not a fragment. | Silent. Q32 asks for exact match plus a fragment arm. |
| A4 | A pinned path that exists but is not what the gate reads still counts | BREAKS | W3: `check_substrate_pins.py` pinned `` `SKILL.md` ``, although the script reads `verifiers/baseline.json` (`check_substrate_pins.py:320-321`). `verify_harness_claims.py` pinned the directory `` `verifiers` `` (`git cat-file -e HEAD:verifiers` succeeds, and `:99` only strips a trailing `/`). Both accepted. `in-file` is accepted for any gate without reading the file (`:171`). | Silent |
| A5 | A verdict map that misclassifies or omits a produced code still counts | BREAKS (misclassify) / HOLDS-by-protocol (omit) | W3: `verify_corpus_integrity.py` with `0=clean, 1=failed, 2=could-not-evaluate, 3=clean` was accepted, although `:1341-1344` returns 3 for "no baseline". Omission: every exit 3 in the lane is a missing-baseline or unreadable-input path (`check_substrate_pins.py:21,329`; `verify_harness_claims.py:692-694`; `verify_skill_checklist.py:2558`). PROTOCOL reads an undeclared nonzero code as could-not-evaluate, so omitting 3 classifies it correctly by default. The counter checks neither direction. | Partly. The plan names "whether each declared exit code is really produced"; the class of a produced code is silent. |
| A6 | `probe` is used to dodge the gate rules | BREAKS (dodge works) / HOLDS (named) | W1: four scripts that exit 1 become `probe` with `0=clean`, `none`, `none`; result 23 of 23. W3: `fault_injection_corpus.sh` as `probe` with `0=clean, 1=failed` was accepted, although a row declaring `1=failed` contradicts PROTOCOL's "a tool that cannot fail is a probe". The counter could have caught that from the row alone. | Named: "whether gate-vs-probe is the right kind" (plan, docstring `:39-41`) |
| A7 | An entry command that does not run the file still counts | BREAKS | W3: `` `python3 -B verifiers/verify_alwayson.py.orig` `` was accepted (substring test, `:146`). | Silent |
| A8 | A write scope that says nothing, or something false, still counts | BREAKS | W3: write scope `x` for `verify_dispatch_prompts.py` was accepted. The only test is non-empty and not a dash (`:178`). | Silent |
| A9 | Ghost rows escape `phantom 0` | BREAKS | W3: a row `scripts/ghost.py` is not phantom, because the phantom rule needs a `verifiers/` prefix (`:198-199`). A second table under the same heading with `verifiers/ghost2.py` is never read: `done` is never reset (`:124-130`). Both worlds print `phantom 0`. | Silent. The docstring says "first table" (`:20`), but the plan's statement `phantom 0` does not. |
| A10 | Q31: does the plan's prose describe only what the counter reads? | BREAKS (minor, fixable in text) | The plan says "Each mismatch it counts is a disagreement between the lane's registry (its self-description) and the repository". It gives "a gate without `0=clean` and `1=failed`" as an example. Of the eight row checks in `judge_row` (`:141-182`), only the self-test literal and pinned-path existence read repository bytes. Row existence and phantoms read the tree listing. Kind, verdict-map shape, write scope and owner check only the row's own cells. | — |
| A11 | Duplicate authority | Note (not a counted breach) | `verifiers/README.md` (moved verbatim in `7ad05d34`) still states exit codes and self-tests per script (for example lines 13 and 19: `exit 0/1/2/3, --self-test`). A disagreement between the README and the new registry is counted by nothing. `SKILL.md:533` at `7ad05d34` already points to a "§ Gate registry" that does not exist yet. | Silent |

## Calibration: real measure or bookkeeping?

[INFERENCE from W0–W4] The counter measures existence. It confirms that the registry is complete against the verifier
listing, that named flag text is somewhere in the file, and that a named path exists. Before-value 0 means only that the
table is absent. Any table with the right schema scores close to M, and every gap between an honest table and M of M can be
closed by a silent dodge (A1–A4, A7–A9) or a named one (A6). W0 does find one real gap between the registry and the
repository: four gates have no self-test mode, which breaks PROTOCOL § Gate standard, Self-test. So the counter has
calibration value only if the delivered registry is honest. If C2 lands at `23 of 23` with those four rows unchanged, the
counter's one real discrimination has been dodged. A `19 of 23` result is the honest calibration reading.

## Smallest safe corrections (the counter stays frozen)

1. **Admission condition for C2 (judge or reviewer):** read `23 of 23` as earned only if the four rows for
   `box_proof_case_deletion.py`, `check_alwayson_boxes.py`, `check_callee_rename.py` and `check_opencode_repin.py` are
   `gate`, and each declared self-test flag is shown to run in a sandbox: `python3 -B verifiers/<f> <flag>` exits 0 with
   a tally line. Otherwise, report the honest `19 of 23` (exit 1) as a miss. A `probe` label on any of the four, or the
   borrowed `--self-test` in `RegCheckOpencodeRepin.md:3`, is a misdescribed registry and must be rejected, not counted.
2. **Plan erratum (append-only, the same pattern as `d051ec40`):** extend "What the counter does not measure" to cover the
   checks the counter does not run:
   - whether a self-test flag is an option the script accepts, and whether that self-test passes;
   - whether a pinned path is what the gate reads (a directory or `in-file` passes);
   - whether each declared code's class is right;
   - whether the entry command runs;
   - whether the write scope is true;
   - that flag and entry matching are substring tests (Q32);
   - that rows outside the first table, and names without the `verifiers/` prefix, are never phantoms.

   Also replace "Each mismatch it counts is a disagreement between the registry and the repository". Only row existence,
   phantoms, the self-test literal and pinned-path existence read the repository; the other four checks read the row alone.
3. **Falsify wave:** per row, run each declared self-test flag, check that each pinned path or its basename appears in
   the script, and compare each declared code with the script's docstring exit list. Report findings beside the counter
   line, never inside it.
4. **Later round (routed, not now):** give the counter exact flag matching against the script's argparse options or
   `case` labels, a fragment must-fail arm, and a must-fail arm for a probe that declares `1=failed`. This would be a
   second measurement under Q28.

## Impacted axes

- **Calibration:** the main impact. The headline can certify registries that disagree with the repository (A1–A9).
- **Consistency:** the target creates an incentive to relabel gates or cite borrowed flags. A6 and A2 are live in drafted rows.
- **Q-rows involved:** Q26 holds literally. Q31 is breached by the plan's mismatch sentence (A10). Q32 is breached
  by the substring flag and entry matching (A3, A7).
