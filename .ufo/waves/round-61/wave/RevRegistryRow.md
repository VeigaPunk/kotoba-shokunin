# RevRegistryRow — gate-registry row audit (kotoba round 61, wave seat)

Seat: `kotoba-r61-wave-RevRegistryRow` (reviewer, axis: operability).
Scope: audit the planned `## Gate registry` additions/updates — (1) new row for
`verifiers/check_routed_repairs.py`, (2) v3-annotated update for
`verifiers/check_scoped_rules.py` — against `verifiers/check_gate_registry.py`'s
pinned rules, plus `--self-test` and `--rev <tip>` measurements. ScribeSkillReg's
draft had not landed at audit time (only `swarm-registry.json` existed under
`.ufo/waves/round-61/wave/`), so rows are drafted from the pinned rules and
verified with the checker's own `judge_row`/`judge` (harness-verified, not
eyeballed). Lane read-only; no files were changed.

## Measured results (tip = `7827628a939b0333c89892dfcedc72e390ccfb60`)

`date -u`: Fri 23 Oct 2026 07:10:53 PM UTC

```
$ python3 -B verifiers/check_gate_registry.py --self-test
self-test: 0 failure(s) over 28 assertions
exit=0
```

```
$ python3 -B verifiers/check_gate_registry.py --rev 7827628a939b0333c89892dfcedc72e390ccfb60
verifiers/box_proof_case_deletion.py         OK
verifiers/check_agent_definitions.py         OK
verifiers/check_agentdef_boxes.py            OK
verifiers/check_alwayson_boxes.py            OK
verifiers/check_assertion_floors.py          OK
verifiers/check_callee_rename.py             OK
verifiers/check_command_files.py             OK
verifiers/check_correction_sweep.py          OK
verifiers/check_could_not_evaluate.py        OK
verifiers/check_description_thresholds.py    OK
verifiers/check_explicit_invocation.py       OK
verifiers/check_gate_finding_delta.py        OK
verifiers/check_gate_registry.py             OK
verifiers/check_hook_files.py                OK
verifiers/check_infoless_fences.py           OK
verifiers/check_mcp_instructions.py          OK
verifiers/check_opencode_repin.py            OK
verifiers/check_overlap_levers.py            OK
verifiers/check_plugin_manifests.py          OK
verifiers/check_routed_repairs.py            no registry rows naming it: 0 (need 1)
verifiers/check_scoped_rules.py              OK
verifiers/check_sibling_census.py            OK
verifiers/check_sources_append_only.py       OK
verifiers/check_substrate_pins.py            OK
verifiers/check_sweep_mutants.py             OK
verifiers/compare_harness_independent.py     OK
verifiers/fault_injection_corpus.sh          OK
verifiers/verify_alwayson.py                 OK
verifiers/verify_corpus_independent.py       OK
verifiers/verify_corpus_integrity.py         OK
verifiers/verify_dispatch_prompts.py         OK
verifiers/verify_harness_claims.py           OK
verifiers/verify_harness_independent.py      OK
verifiers/verify_skill_checklist.py          OK
verifiers/verify_surfaces.py                 OK
gate registry rows conformant 34 of 35 lane verifiers; phantom 0
exit=1
```

Interpretation: the lone nonconformance is the missing row for the committed
round-61 counter `verifiers/check_routed_repairs.py` (committed by freeze commit
`7827628`, universe grew 34→35 blobs vs base `f3246d14`; the registry row rides
the integration commits per plan § Commit order). The gate is therefore **red
between freeze and integration** — expected sequencing, not a defect, but any
claim phrased "registry clean at tip" before the row lands would be false.

## Pinned rules audited against (checker lines cited)

From `verifiers/check_gate_registry.py` docstring + code (sha `95ffed38` at tip):

- Universe `M` = blobs directly under `verifiers/` ending `.py`/`.sh`
  (`git ls-tree`, no recursion; `fixtures/` and `__pycache__` are trees). (L16-18,
  L118-129) — **35 at tip, 34 at base**.
- Exactly one row per verifier, name cell `verifiers/F` (compared lower-cased,
  backticks stripped). (L230-234, `clean()` L146-147)
- `kind` ∈ {gate, probe} (L181-182); a **gate** must declare `0=clean` and
  `1=failed`, may not have self-test `none` or pinned-values `none` (L191-192,
  L199-201, L210-212).
- Verdict-map pairs must parse as `\d+\s*(=|->|→)\s*(clean|failed|could-not-evaluate)`,
  no code twice (PAIR_RE L74, L185-190).
- Self-test cell: `none` or ≥1 backticked `` `--flag` ``; each flag must be an
  **exact** `add_argument` string arg (Python AST) or sole case-arm pattern
  (`.sh`); comments/lookalikes don't count (FLAG_RE L75, L78-105, L198-208).
- Pinned values: `none` | `in-file` | backticked repo-relative paths existing at
  the measured revision; no absolute, no `..` (L209-219).
- Write scope: non-empty, not `-`/`–`/`—` (L220-221); owner `kotoba` (L222-223).
- Parser end rules: first table under `## Gate registry` only; a blank line after
  rows sets `done`, a heading of level ≤2 ends the section — a row appended after
  a blank line is silently unread; literal `|` inside cell text shifts columns
  and yields phantom/wrong-cell failures (L150-175).
- Phantom: any row naming `verifiers/...` outside the universe (L239-241).

## Audit of the two planned rows — every cell

### Row 1 (new): `verifiers/check_routed_repairs.py` — gate

Script facts (sha `5d277dc6` at tip): `add_argument("--rev")` at L117 (optional,
`default=None` → `master`), `add_argument("--self-test")` at L118; exits 0 (K==6),
1 (K<6), 2 on unreadable rev (L131-145, L151). Reads committed blobs only
(`git show`); self-test fixtures are pure in-memory dicts (L154-211). Written
nothing; no network. Verdict-map `0=clean, 1=failed, 2=could-not-evaluate` is
honest; pinned values are genuinely `in-file` (the six R-a..R-f patterns frozen
in `check_repairs`, L63-112); write scope `none` is honest (in-memory fixtures;
`git show` is read-only — mirrors `check_gate_registry.py`'s own `none` cell).

Draft (conformant — `judge_row` → `why: []`; verified):

```
| `verifiers/check_routed_repairs.py` | gate | `python3 -B verifiers/check_routed_repairs.py` | 0=clean, 1=failed, 2=could-not-evaluate | `--self-test` | in-file | none | kotoba |
```

Notes: entry command omits `--rev` per the optional-flag precedent
(`check_assertion_floors.py`, `check_substrate_pins.py`, `check_mcp_instructions.py`
rows all omit it); the `… --rev <rev>` variant also judges clean. Insert **inside**
the table — alphabetically immediately after the `check_plugin_manifests.py` row
(`check_routed_repairs` < `check_scoped_rules` sorts correctly there); no blank
line may intervene (parser `done` rule).

### Row 2 (update): `verifiers/check_scoped_rules.py` — gate, v3 annotation

v2 source at tip has exact handlers `--rev` (L2495), `--fetch` (L2496), `--json`
(L2497), `--self-test` (L2498). The wave-spec asks for an r58-style annotation.
Landed precedent (commits `46b4a70`, `6de8e2e`): annotate the **verdict-map cell
in place**, e.g. `… 2=could-not-evaluate — claim withdrawn r58 before data (plan
erratum 1); not a claim gate until redesigned and re-controlled`. v3 differs from
those precedents: the claim is *not withdrawn* — v2 was measured at r60 and v3 is
re-measured this round — so the withdrawn wording must not be copied verbatim.
Honest conformant wording:

Draft (conformant vs the v2 source at tip — `judge_row` → `why: []`):

```
| `verifiers/check_scoped_rules.py` | gate | `python3 -B verifiers/check_scoped_rules.py --rev <rev> --fetch` | 0=clean, 1=failed, 2=could-not-evaluate — counter redesign v3 landed r61 (provenance-authenticating arms A1-A4 per plans/round-61.md); v2 predicate measured at r60 | `--self-test` | in-file | self-test repos under `$TMPDIR` (removed); `--fetch` reads the network | kotoba |
```

This is an **in-place cell update of the existing row** — it must remain exactly
one row (duplicating it → "registry rows naming it: 2" failure).

Conformance invariants for the v3 landing (hold regardless of v3 internals —
flag now so the v3 author cannot silently break the gate):

1. The counter must keep the path `verifiers/check_scoped_rules.py` (rename →
   phantom + missing row; the frozen C1 predicate pins this path anyway).
2. Keep an **exact** `add_argument("--self-test")` (the frozen predicate requires
   the flag to *work*: `--self-test` prints `worlds reject 7 of 7; eligible rows
   pass 4 of 4`, exit 0). The row's self-test cell names only `` `--self-test` ``;
   if a draft adds e.g. `` `--fixtures` `` to the cell, v3 must implement that
   exact string or the cell lies. Safest: keep the cell as shown.
3. `--rev` and `--fetch` must also remain real handlers (frozen C1 predicate
   calls `--rev <tip> --fetch`); they need not appear in the self-test cell.
4. Verdict-map annotation must contain **no `N=class`/`N->class`/`N→class` token**
   beyond 0/1/2 (a digit followed by `=`/`→`/`-\>` + a class word creates a
   second pair → "code declared twice" if it repeats 0/1/2, or a stray extra
   code). No literal `|` anywhere in the row. The drafted em-dash annotation is
   clean of both.
5. Pinned values: `in-file` stays conformant. Optionally name the committed
   fixture dir (`verifiers/fixtures/…` paths `cat-file -e`-exist at the measured
   rev) for bookkeeping honesty — but only if committed in the **same** commit
   as/ before the row (paths are checked at the measured revision).
6. Write scope: keep `… $TMPDIR (removed); --fetch reads the network` **iff** v3
   retains temp-repo self-tests and network `--fetch`. If v3's self-test runs
   purely over committed fixture bytes, honest cell = `none; --fetch reads the
   network` (still conformant — write scope only needs to be non-empty). Re-check
   the landed v3 source before freezing the cell.
7. Committed C1 fixture files must land under `verifiers/fixtures/` (a tree —
   excluded from the universe) or outside `verifiers/`; a stray
   `verifiers/*.py`/`.sh` blob grows M and breaks the gate until rowed.

## Harness verification of the drafts (whole table)

Both drafted rows were spliced into the tip `SKILL.md` table in-memory and run
through the checker's own `judge(skill, universe, read, exists)` against rev
`7827628a` blobs:

```
conformant: 35 of 35 phantom: []
verifiers/check_routed_repairs.py  OK
verifiers/check_scoped_rules.py    OK
```

i.e., with these two rows the registry gate returns to 35 of 35, exit 0. The v3
row was judged against the **v2** source — conformant at tip too — so the row
may be committed before or together with the v3 rewrite.

## Other planned rows: none found

Universe delta base→tip is exactly `+check_routed_repairs.py`. C3 adds a
SOURCES.md row + corpus README row (not this checker's scope). No other
`verifiers/` addition is planned; the wave-spec prompts for ScribeSkillReg name
these same two rows.

## Findings

1. **Expected-red window (informational):** `--rev 7827628a` exits 1 today —
   `check_routed_repairs.py` committed in the freeze without its row (universe
   35, rows 34). Closes when ScribeSkillReg's row lands at integration. Any
   pre-integration "registry clean" claim would be fabricated.
2. **No defect found** in the planned cell values: ScribeSkillReg's spec
   (kind gate / 0,1,2 verdict map / `` `--self-test` `` / `in-file` / owner
   kotoba) matches the script's real `add_argument` strings and exit codes; my
   independently drafted rows pass `judge_row` and full-table `judge`.
3. **Wording risk flagged:** the wave-spec says "annotate per the round-58 R1
   precedent for withdrawn/redesigned rows" — the r58 precedents all say
   "claim withdrawn … not a claim gate until redesigned". Copying that verbatim
   would be dishonest (C1 v2 *was* measured at r60 and v3 is measured this
   round); the draft above uses accurate redesign wording instead.
4. **Two cells must be re-checked against landed v3 bytes** (unverifiable now —
   v3 not committed): write scope (temp repos vs `none`) and pinned values
   (`in-file` vs naming committed fixture paths). Named explicitly so the
   residual review verifies them post-integration.

## Installs

no installs

## Blockers

none

## One line

Audited the two planned Gate-registry rows cell-by-cell against
check_gate_registry.py's pinned rules, drafted both (self-test flag ``--self-test``
verified as a real `add_argument`, verdict maps honest, owner kotoba, write scope
accurate), harness-verified 35 of 35 conformant / 0 phantom post-splice, ran
`--self-test` (0 failures/28 assertions) and `--rev` at tip `7827628a` (34 of 35,
exit 1 — only the not-yet-landed routed-repairs row), and pinned the seven
invariants the v3 landing must keep.
