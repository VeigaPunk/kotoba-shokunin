Result: MIXED — C1's declared-pair extraction is exact on both live dumps (the 8 declared `loader-group` pairs, zero extra, callee names differ across versions), and the frozen counter reproduces `4 of 4`; but the gate that carries it reads `pass 6, fail 1, exit 1` on the host today because the opencode npx substrate moved to 1.19.4 after the judged commit, and the round-52 freshness row exists only in the uncommitted SCORECARD diff.

# ScoutLiveShape — C1 on live bytes (freshness falsify, round 52 attempt 2)

Judged revision: `c8407a453788df964df5a7b835dd0ce1360de882` (clone at
`/fast/scratch/hyaku/kotoba-r52a2/ScoutLiveShape/lane`, `rev-parse HEAD` = that sha).
Lane read-only; all probes ran in the sandbox clone and in memory. No lane file was edited.

## Bytes opened (local only; no URLs fetched)

| Object | Bytes | sha256 |
|---|---:|---|
| `/home/vgpnk/.local/bin/omp` (`omp --version` → `omp/18.12.6`, exit 0) | 256,702,432 | `85d9daf3a05fc76e8cd425ae1904eb576af8d21cc85fcf4690742626e07ccfa4` |
| `strings -n 4` dump of it (`/fast/scratch/hyaku/kotoba-r52a2/ScoutLiveShape/omp-live-18.12.6-strings.txt`, exit 0) | 48,148,449 | `953b19dffc4d51bd877330b90f0e994db38e90ee5f80575f08a31f3b73e7d96f` |
| `.ufo/round-44/evidence/omp-live-18.12.2-strings.txt` (round-44 evidence) | 47,815,579 | `28d03d74708d3d6ff121ae5ae847388c04a66102471f90b4a6115c7d9d88c1bf` |
| `verifiers/fixtures/surfaces/strings-omp-18.12.6.txt` | 1,467 | (in clone @ `c8407a45`) |

Scripts: `/fast/scratch/hyaku/kotoba-r52a2/ScoutLiveShape/{analyze,probe2,probe3}.py`
(logs `analyze.log`, `probe2.log`, `probe3.log`, gate JSON `surfaces-json.json`,
`surfaces-json-base.json`). No tool installed or upgraded.

## Q1 — live omp 18.12.6: does the rule extract exactly the declared pairs?

**HOLDS.** `OMP_GENERIC_CALL_RE` finds 11 call shapes under 3 callees; all 3 are admitted;
every pair they register is declared. No extra pair, no missing `loader-group` pair.

```
generic-regex call matches: 11
distinct callees: 3
admitted callees: 3 -> ['Ho', 'Kl', 'bq']
extracted pairs: 8
    ('agents-md', 'AGENTS.md') callees: ['bq']
    ('claude-md', 'CLAUDE.md') callees: ['bq']
    ('gemini', 'GEMINI.md') callees: ['Ho', 'Kl']
    ('gemini', 'SYSTEM_TEMPLATE.md') callees: ['Ho', 'Kl']
    ('gemini', 'system.md') callees: ['Ho', 'Kl']
    ('github', 'copilot-instructions.md') callees: ['Ho']
    ('opencode', 'AGENTS.md') callees: ['Kl']
    ('windsurf', 'memories/global_rules.md') callees: ['Kl']
EXTRA (extracted, undeclared): []
loader-group missing from extraction: []
non-admitted registrations (0):
```

Cross-checks in the same run: `extract_classes(dump,"omp",declared)` equals my
replication of the loop (`True`); the allowlist mode `extract_classes(dump,"omp",None)`
yields the identical 8 pairs (`generic == allowlist == loader-group set: True`), which is
expected — all three live callees are in the round-52 allowlist. So live bytes cannot
discriminate old rule from new; only the fixtures can.

Completeness side (a rule can also pass "no extra" by matching too little): the live dump
carries 410 quoted `*.md` literals; the strict rule matches 11 of them as registration shapes;
a deliberately loose registration-like pattern (`<any callee>( … , <group>, "<file>.md")`
allowing nested parens and whitespace in the first argument) finds 11, and its 4 extras are
not misses — they are the inner `Ho(...)`/`Kl(...)` calls of the wrapped
`await R(Ho(u, "gemini", "SYSTEM_TEMPLATE.md"), "project", "template")` forms, already
matched at their own start by the strict rule. No registration shape on live bytes is
silently skipped.

Declared-pair accounting: baseline has 33 omp class ids → 33 pairs, no duplicates. 8 are
`.md`-shaped `loader-group` pairs (all extracted). 6 more are `.md`-shaped but declared
`loader-literal` and correctly not extracted — their literals are present in the dump
(`SYSTEM.md` ×27, `AGENTS.md` ×37, `CLAUDE.md` ×15, `RULES.md` ×4), so this is not
extractor blindness; `surfaces.literal_present` covers them. The remaining 19 declared
pairs are not `.md`-shaped (`cursor/rules`, `discovery/*`, `provider-gate/enabledProviders`
etc.) and cannot be produced by a `"<file>.md"` call shape.

## Q2 — round-44 evidence dump (omp 18.12.2): same question

**HOLDS, and it is the stronger freshness datum**: different minified callees, same 8 pairs,
zero extras, zero non-admitted callees.

```
generic-regex call matches: 11
admitted callees: 3 -> ['Gl', 'I5', 'Mo']
extracted pairs: 8   (identical set to the 18.12.6 run)
EXTRA (extracted, undeclared): []
loader-group missing from extraction: []
```

So the declared-pair rule is invariant across the two real binaries whose callee names
differ (`Ho/Kl/bq` vs `I5/Gl/Mo`) — the rename-robustness claim is exercised by real bytes,
not only by the fixtures.

## Gate at the judged rev: `python3 -B verifiers/verify_surfaces.py --json`

Run in the clone at `c8407a45` with no override flags (gate reads `/home/vgpnk/.local/bin/omp`
and the npx-cache opencode). **exit 1, pass 6, fail 1:**

```
surfaces.literal_present    PASS  42 loader-kind entries verified against the dumps
surfaces.no_uncovered_class PASS  all 8 extracted loader class(es) declared
surfaces.opencode_extract   FAIL  declared opencode class(es) produced by no rule:
                                  opencode:instruction-context/AGENTS.md,
                                  opencode:read-hook/instructions; rule(s) matched
                                  nothing: OC-4 (missing fn("Instruction.resolve") +
                                  fn("ReadTool.execute") + <system-reminder>);
                                  OC-6 (missing InstructionContext.observe +
                                  Key.make("core/instructions") + targets:["AGENTS.md"]
                                  + system-context-builtins)
surfaces.table_parity       PASS  42 ids
surfaces.literal_parity     PASS  42 rows
surfaces.kind_parity        PASS  42 rows
surfaces.excluded_reason    PASS  8 excluded entries reasoned
substrate.omp      = /home/vgpnk/.local/bin/omp sha 85d9daf3…
substrate.opencode = ~/.npm/_npx/e2094862b59aac7b/.../opencode.exe sha 538fcb1b…
```

Both omp checks pass; the one red is opencode-side. Held-constant control: the same gate
run with the same live omp dump plus the committed opencode fixture dump
(`verifiers/fixtures/surfaces/strings-opencode-clean.txt`) is **pass 7, fail 0, exit 0** for
both live omp dumps (18.12.6 and 18.12.2). Base control: the same default-flag run at
`c8579a4c` is also **pass 6, fail 1** with the same `opencode_extract` detail — the red is
not caused by round 52.

## Defects

**F1 (MEDIUM) — the plan's and the uncommitted row's no-harm guard does not reproduce: live
gate is `pass 6, fail 1`, exit 1, not `pass 7`, exit 0.** Targets: `plans/round-52.md:34-36`
("`verify_surfaces.py --json` on the installed omp 18.12.6 stays `pass 7`, exit 0 … `check_substrate_pins.py`
stays `OK 3/3`") and the uncommitted `SCORECARD.md` freshness row (working-tree diff hunk
`@@ -27,9 +27,9 @@`, line beginning `| freshness (advisory) | 8 | **round 52 (C1`), which asserts
"No harm: live gate `pass 7`, exit 0 on omp 18.12.6".
Evidence chain:
- `python3 -B verifiers/check_substrate_pins.py` at `c8407a45` → `FAIL opencode_binary_sha256:
  sha256 drift: expect=179ca421… got=538fcb1b…`, `DRIFT 1/3 pins failed`, exit 1. So the
  second guard (`pins OK 3/3`) is false too.
- Installed opencode is `opencode-ai` **1.19.4** (`~/.npm/_npx/e2094862b59aac7b/package.json:3`
  `"opencode-ai": "^1.19.4"`), binary sha `538fcb1b…`, 214,522,032 bytes, file mtime
  `2026-10-22 14:50:30 -0300` = 17:50:30Z.
- Cause and timing: npm log `~/.npm/_logs/2026-10-22T17_50_26_483Z-debug-0.log` line 7-8:
  `npm exec --yes --prefer-online --package opencode-ai -- true`, cwd
  `/home/vgpnk/Projects/shokunin` (line 103). The judged commit landed 17:10:42Z, the plan
  15:57:28Z (`git show -s --format=%cI`), so the substrate moved **40 minutes after** the
  judged commit, during this falsify wave, by a probe of this fleet (not by C1 code).
- `.ufo/waves/round-52/build-gate.txt` is 0 bytes: there is no wave-file record of a `pass 7`
  run at all; the number exists only in the plan's forward-looking guard and in the
  uncommitted row.
Consequence for closure: any closure command run on this host today reads red. The row, if
committed, must name the substrate sha it was measured on (Q19) or be re-measured; a green
`--json` claim cannot be landed as written. Fixing the opencode drift (re-derive OC-4/OC-6
anchors for 1.19.4 and re-pin, or pin the channel) is a substrate move outside C1 — the L1
must decide, and it must not be smuggled in as a C1 no-harm pass.

**F2 (LOW-MEDIUM) — the rule's blindness set is understated in-source: a NEW callee that
registers only an undeclared pair is invisible.** `verifiers/verify_surfaces.py:220-233`
names the positive arm ("a NEW pair registered by a real (admitted) callee still surfaces as
an undeclared class") and then lists what the rule "does not survive" (call-shape change,
rename of every declared group and file at once). The new-callee case is not in that list and
is not covered by any self-test arm. Probe on live bytes (probe2.py case 4): appending
`Zz(u, "rnplant", "RNPLANT.md")` (fresh callee, fresh pair) leaves the extraction at the same
8 pairs and `surfaces.no_uncovered_class` **PASS** where case 3 (`Ho(u, "rnplant",
"RNPLANT.md")`, admitted callee) **FAILs** naming `omp:rnplant/RNPLANT.md`. This is not a break
of C1's declared statement (rename robustness on the 4 fixtures) — but a future omp build that
adds a client through a brand-new helper, with no declared pair, stays silently green. Fix is
documentation and (ideally) one self-test arm asserting the blindness, so the limit is
recorded rather than discovered later.

**F3 (MEDIUM, record shape) — the judged revision carries no round-52 freshness row.**
`git show c8407a4:SCORECARD.md` lines 28-33 still hold the round-51 leads (freshness = "omp
18.12.6 re-derived and re-pinned … pass 5 of 7 → 7 of 7 … @ `e0320302`"). The round-52
freshness row, the "Round 52 completed" block and the round-52 counts table rows exist only in
the uncommitted working-tree diff (`git -C … diff -- SCORECARD.md`), which the context lists as
attempt-1 carry. So the freshness axis's evidence is not in the judged tree; it is also the
carrier of F1's false sentence.

**F4 (INFO) — fail-closed false-red channel, pre-existing (round-28 arm).** A call registering
a declared `loader-literal` `.md` pair makes extraction produce that class id, and
`check_no_uncovered_class` then reports "re-kinded in the baseline" (`verify_surfaces.py:797-860`,
the kind-consistency arm): `q(u, "codex", "AGENTS.md")` → `FAIL … omp:codex/AGENTS.md->loader-literal`.
No silent pass — the direction is safe — but a genuine future conversion of
`codex/AGENTS.md` to a registration call will read as laundering until the row is re-kinded.
Note only; no claim rests on it.

## Mutation battery on live bytes (each case re-run through the judged checks)

| Case | Extracted | `no_uncovered_class` | Expected |
|---|---|---|---|
| control (live dump) | 8 declared | PASS | PASS ✔ |
| 1 pure rename of all 3 callees (`Ho/Kl/bq` → `QHo_rn/QKl_rn/Qbq_rn`) | 8 declared | PASS | PASS ✔ |
| 2 alias decoy `q(u,"evil","EVIL.md")` | 8 declared (decoy not extracted) | PASS | PASS ✔ |
| 3 planted pair via admitted callee `Ho(u,"rnplant","RNPLANT.md")` | 9 | **FAIL** `omp:rnplant/RNPLANT.md` | FAIL ✔ |
| 4 planted pair via new callee `Zz` | 8 | PASS | FAIL ✘ (F2) |
| 5 new callee registering a declared then an undeclared pair | 9 | **FAIL** `omp:rnplant/RNPLANT.md` | FAIL ✔ |
| 6 group literal `gemini` → `gemini-rn` | 8 | **FAIL** 3 undeclared `omp:gemini-rn/*` | FAIL ✔ |
| 7 every declared group+file renamed at once | 0 | **FAIL** `vacuity: 0 loader class(es) extracted …` | FAIL ✔ |
| 8 file `AGENTS.md` → `AGENTS-rn.md` on `bq` | 8 | **FAIL** `omp:agents-md/AGENTS-rn.md` | FAIL ✔ |
| 9 group identifier rebound to an unbound name | 8 | **FAIL** `omp:<unresolved-var:S$Xx>/CLAUDE.md` | FAIL ✔ |
| 10 one of `bq`'s two calls renamed, other kept | 8 declared | PASS | PASS ✔ |

So on real bytes the admission rule is fail-closed for every mutation except the new-callee
case (F2), and it is genuinely callee-name independent (case 1, plus the 18.12.2/18.12.6 pair).

## Corroboration (counter freshness)

```
python3 -B verifiers/check_callee_rename.py --rev c8407a45…  → callee-rename robust 4 of 4 fixtures, exit 0
python3 -B verifiers/check_callee_rename.py --rev c8579a4c…  → callee-rename robust 0 of 4 fixtures, exit 1
   per fixture @ c8407a45: control=[0,True] renamed=[0,True] planted=[1,True] robust=True
   per fixture @ c8579a4c: control=[0,True] renamed=[1,False] planted=[1,False] robust=False
seeds 52 / 7 / 1234 / 99 @ c8407a45 → 4 of 4 fixtures, exit 0 each
python3 -B verifiers/verify_surfaces.py --self-test → 0 failure(s) over 129 assertions, exit 0
verifiers/floors-registry.json instruments.surfaces.floor = 129
```

Fixture fidelity: all 11 call shapes in `strings-omp-18.12.6.txt` (1,467 bytes) occur verbatim
in the live 18.12.6 dump — none is fabricated.

## Confidence and remaining unknowns

- High confidence: extraction set, admission set, extra-pair count, mutation outcomes, gate
  pass/fail, pins drift, opencode version and the timing of its replacement, counter results
  and floor. All from direct runs pasted above.
- [INFERENCE] The `pass 7` guard was true when the C1 work was committed: the opencode binary
  was replaced at 17:50:30Z, 40 minutes after `c8407a4` (17:10:42Z), and nothing in the tree
  records the substrate of that run. I did not find a surviving 1.19.3 copy
  (`/fast/scratch/kotoba-r47/shared/bin` no longer exists) to re-run the gate on it; the
  fixture-dump control (`strings-opencode-clean.txt`, pass 7) is the substitute proof that the
  red is opencode-substrate-local.
- Not checked by me (other seats own them): whether the C1 diff weakened any self-test arm,
  the four fixture labels, and C2's content. My findings are scoped to live-shape extraction,
  the gate's live reading, and the freshness record.

Report: .ufo/waves/round-52/falsify-a2/ScoutLiveShape.md
