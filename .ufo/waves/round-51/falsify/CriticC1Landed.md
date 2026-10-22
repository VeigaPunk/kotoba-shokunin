# CriticC1Landed — attack on the landed C1 statement (freshness), round 51 falsify

**Verdict: HOLDS-BOUNDED.** Every condition set by `CriticC1Sizing.md` holds at HEAD `59903b26`. The numbers reproduce: base `pass 5`, exit 1, and HEAD `pass 7`, exit 0. All four cheap paths that critique named are caught by `--self-test`. But four clauses of the re-sized statement (`plans/round-51.md:76-86`) are not turned on by any output (Q26). One premise of the binding rule is wrong on the live dump, although the result it gives is right.

## Conditions from CriticC1Sizing, checked at HEAD

| Condition | Result at HEAD | Evidence |
|---|---|---|
| Counter has no override flags, and `DEFAULT_BINARIES` is unchanged | holds | no-flag `--json`: exit 0, `pass 7`. `substrate.omp` = `source: binary`, path `/home/vgpnk/.local/bin/omp`, sha256 `85d9daf3…07ccfa4`. `substrate.opencode` = binary, sha256 `179ca421…`. The diff has 0 lines that mention `DEFAULT_BINARIES` |
| The omp allowlist grows by exactly `Kl\|Ho\|bq` | holds (by the diff only) | `OMP_CALL_RE` and `CALLEE_SHAPES["omp"]` each gain `\|Kl\|Ho\|bq`. `CALL_RE` and `CALLEE_SHAPES["opencode"]` are unchanged. The docstring change `jD[ef]` → `jDe\|jDf` is cosmetic |
| The binding rule reads only the dump | holds | `module_scopes`, `scope_of`, `scope_table`, `constant_table` and `extract_classes` take only `dump` (and `harness`). There is no baseline read and no per-name table |
| The 18.12.6 fixture carries the earlier `var S$ = "title"` | holds | fixture line 1 is `// packages/coding-agent/src/session/session-entries.ts` and line 2 is `var S$ = "title";`. It has `S$ = "claude-md"` at line 11 and a later synthetic `var S$ = "later";` at line 36 |
| `--self-test` exits 0 | holds | `0 failure(s) over 115 assertions`, exit 0 |
| Baseline check rows and inventory are byte-unchanged | holds (by `git diff` only) | `git diff --exit-code --stat 43ca0bfb 59903b26 -- verifiers/surfaces-baseline.json corpus/knowledge/instruction-surface-census-round13.md` → exit 0, empty |

Mutants were built in my scratch clone at HEAD. Each was run with `--self-test` and with the no-flag `--json` on the live binary:

| Mutant | `--self-test` | live `--json` | Caught by |
|---|---|---|---|
| m0: callee names only (`consts = global_table`) | exit 1, 7 of 115 fail | exit 1, `pass 5` | both |
| m2a: last binding wins across the whole dump | exit 1, 9 of 115 fail | exit 0, `pass 7` | self-test |
| m2b: hardcoded `S$ = "claude-md"` | exit 1, 9 of 115 fail (`fx-renamed-var`, `ambiguous-rebind`) | exit 0, `pass 7` | self-test |
| m1: any callee of 1–4 characters | exit 1, 2 of 115 fail (18.12.5 decoy) | exit 0, `pass 7` | self-test |
| m5: module table wins over the dump-wide table | exit 0, 0 of 115 fail | exit 0, `pass 7` | nothing (an equivalent rule; see F3) |
| m6b: allowlist + an unused fourth name `Zq` | exit 0, 0 of 115 fail | exit 0 | nothing (see F2) |

The claim "a callee-names-only fix fails the self-test" is turned on: m0 is red on both.

## Findings

**F1. The no-override clause is turned on only for the binary and dump flags, not for `--baseline`, `--inventory` or `--repo` (Q26; calibration).**
- I ran `--json --baseline <copy> --inventory <copy>`, with byte-identical copies placed in `/tmp`. Exit 0, and the output is `cmp`-identical to the no-flag JSON.
- The `substrate` block names only the binaries and dumps.
- The clause "the baseline's check rows and the surfaces inventory are byte-unchanged from `43ca0bfb`" has no output and no cited guard. It holds only by the `git diff --exit-code` above, and neither the plan nor the lesson names that command.
- Impact: none on the landed value (the files are unchanged). The clause is not counter-measured.

**F2. "Grows by exactly `Kl|Ho|bq`" is turned on by the diff only, and four copies of the list are kept by hand (duplicate authority).**
- An allowlist with one more unused name (`|Zq`) passes `--self-test` (0 of 115 fail) and the live `--json` (exit 0).
- A one-letter extra name (`q`) is caught only because the 18.12.5 fixture holds a decoy for it.
- `OMP_CALL_RE` is a literal. `CALLEE_SHAPES["omp"]` and the docstring are separate copies. Only the round-50 list is a tuple (`OMP_CALLEE_NAMES_ROUND50`), and no assertion ties the current regex to `ROUND50 + ("Kl","Ho","bq")`.

**F3. The rule's premise is wrong on the live dump, but the result is right. The fixture encodes the premise rather than the live structure (calibration).**
- The docstring says "a minified name bound in two modules is two DIFFERENT variables" and uses `// packages/….ts` comments as the scope boundary.
- On the live dump, the two `S$` bindings are both top-level `var` statements, and they sit in different `// @bun @bytecode` chunks. The nearest chunk header before line 843423 is at line 839351. The nearest before lines 895604 and 895607 is at line 886528. The dump has 3042 chunk headers in total.
- Inside a single chunk, 95 conflicting names span more than one source-path module. Examples are `s`, `t`, `n` and `r` at lines 652942, 658893 and 664149: function-local names, not separate module scopes. So a source-path comment is a proxy for scope, not a JavaScript scope.
- A rule that uses chunk scope gives the same 8 pairs on the live dump (`HEAD rule live == chunk rule live: True`).
- That rule leaves `<unresolved-var:S$>` on the fixture, because the fixture leaves out the `// @bun` headers. So the self-test would reject an arguably truer rule.
- m5 (the opposite precedence) is green everywhere, so the clause "the dump-wide table wins wherever it has an entry" is not turned on by any arm. It does no harm today.
- The ambiguity control is turned on: m2b fails `ambiguous-rebind: claude-md NOT resolved`.

**F4. The Q09 record does not carry "the extraction rule change", and the census evidence is still stale (freshness; documentation, not counter).**
- `verifiers/baseline.json` `omp_round51_note` (663 characters) records version, sha256 and mtime. It does not mention `Kl|Ho|bq` or the module-scope rule. The rule appears only in the code docstring and in the subject of commit `e032030`.
- `SurfacesRepin.md:18` says "L1: fold into the record". The lesson's only mention of C1 is the claim sentence at line 4.
- Census rows 73 and 74 still cite `jDe(e,Pqr,"AGENTS.md")` and `jDe(e,BWr,"CLAUDE.md")`, the 2026-09-28 shapes.
- The landed clause "inventory byte-unchanged" forbids updating those cells. That conflicts with CriticC1Sizing condition 5, which keeps cells 1–3 fixed but has cells 4–5 updated.

**F5. The rule is cited at a location that is not in HEAD's tree (provenance).**
- `plans/round-51.md:84` places the stated rule in `.ufo/waves/round-51/build/SurfacesRepin.md`.
- `git ls-tree --name-only 59903b26 .ufo/waves/round-51/build/` lists 0 entries, so the build reports, including `CriticC1Sizing.md`, are not committed at the judged HEAD. The rule text does exist in the `verify_surfaces.py` docstring.

**F6 (minor). The sha256 that `substrate` prints comes from a second read of the binary, taken after the checks (`binary_digest` in `substrate_identity`). It is not a hash of the bytes that `strings` dumped.** Pins showed `OK 3/3` in the same session, so this matters only if the binary changes during the run (Q10).

## Clauses no output turns on
1. "with no override flags (`--baseline`, `--inventory`, `--repo`)" — see F1.
2. "baseline check rows and surfaces inventory byte-unchanged" — only `git diff`, and the plan does not cite it (F1).
3. "allowlist grows by exactly `Kl|Ho|bq`" — diff only; the m6b mutant is green (F2).
4. "dump-wide table wins wherever it has an entry" (the rule's precedence) — the m5 mutant is green (F3).

The runtime-loading clause is already stated as not measured.

## Smallest safe correction (no change to the claimed value)
- **Bound the statement.** Cite `git diff --exit-code 43ca0bfb 59903b26 -- verifiers/surfaces-baseline.json corpus/knowledge/instruction-surface-census-round13.md` (exit 0) as the guard for the "byte-unchanged" clause. State that "no override" is shown by the output only for the binary flags (`substrate.*.source == "binary"`).
- **Reword the docstring premise.** Describe the source-path comment as a scope proxy, and note that on 18.12.6 the two `S$` bindings also sit in different `// @bun` chunks.
- **Add the rule change to the Q09 record**, and disclose census rows 73–74 as stale evidence text.
- **Optional, code.** Build `OMP_CALL_RE` from `OMP_CALLEE_NAMES_ROUND50 + ("Kl","Ho","bq")` through `call_re`, and add a self-test assertion on that tuple. This closes F2.

## Evidence
All commands ran in `/fast/scratch/hyaku/kotoba-r51/falsify/CriticC1Landed/`, in a private clone `lane` at `59903b2637689739a5b9901956301da72d0effe1` (`git rev-parse HEAD`, exit 0).
- `python3 -B verifiers/verify_surfaces.py --json` → exit 0, `{'pass': 7, 'fail': 0, 'exit_code': 0}`. Details include `42 loader-kind entries verified against the dumps` and `all 8 extracted loader class(es) declared`.
- Base script (`git show 43ca0bfb:verifiers/verify_surfaces.py`, run on the unchanged baseline and inventory) `--json` → exit 1, `pass 5`, `fail 2`. The FAILs are `surfaces.literal_present` and `surfaces.no_uncovered_class`.
- `python3 -B verifiers/verify_surfaces.py --self-test` → exit 0, `0 failure(s) over 115 assertions`.
- `python3 -B verifiers/check_substrate_pins.py` → exit 0, `OK 3/3 pins hold`.
- `sha256sum /home/vgpnk/.local/bin/omp` → `85d9daf3…07ccfa4`. `omp --version` → `omp/18.12.6`.
- `strings -n 4 /home/vgpnk/.local/bin/omp` → exit 0, 48148449 B, sha256 `953b19df…7d96f`. This matches CriticC1Sizing. The `S$` bindings are at lines 843423 (`"title"`) and 895604 (`"claude-md"`).
- `git diff 43ca0bfb… 59903b26… -- verifiers/verify_surfaces.py` → 396 lines. Hunks are as cited in the conditions table.
- Mutant and probe exit codes are as tabled. The mutants were scratch-only files under `lane/verifiers/_m*.py`, removed afterwards. `git -C lane status --porcelain | wc -l` → 0.
- `git ls-tree --name-only 59903b26 .ufo/waves/round-51/build/ | grep -c .` → 0.
- Read: `/home/vgpnk/.agents/skills/godspeed/SKILL.md` (the skill file was found there). No lane file was written except this report. No tools were installed or updated. Run window: 2026-10-22T15:14Z to 15:21Z.
