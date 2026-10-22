Result: MIXED — the M36 fix `check_correction_sweep.py` is red at the base and green at the judged revision exactly as the lesson claims, and it kills three of the four single-place reverts, but it survives the README index-row revert (that repair is not in the registry, so the lesson's "caught by `check_correction_sweep.py`" is false) and it cannot see a new stale statement planted in `SKILL.md`, in a knowledge entry, in a paraphrase, or any claim kind other than the three registered ones — and a sibling's in-flight registry extension (3→6 rows) closes none of those gaps.

Seat: `KotobaR52a2.MutSweepCheck` (mutation tester). Sandbox: `/fast/scratch/hyaku/kotoba-r52a2/MutSweepCheck`, cloned from the lane and checked out at `c8407a453788df964df5a7b835dd0ce1360de882`. Never pushed; the lane was not modified (read-only `git diff`/`git show` only).

Target: `verifiers/check_correction_sweep.py` (the M36 fix), judged revision `c8407a4`, base `c8579a4c5b48789e56fb9060ddd48f33569e1215`.

---

## 1. Baseline (pristine bytes)

Both endpoints reproduce the M36 lesson row (`corpus/lessons/round-52.md:10`) exactly.

```
$ python3 -B verifiers/check_correction_sweep.py --rev c8407a453788df964df5a7b835dd0ce1360de882
correction sweep: 0 stale block(s)
exit=0

$ python3 -B verifiers/check_correction_sweep.py --rev c8579a4c5b48789e56fb9060ddd48f33569e1215
FAIL r51-c2-readme corpus/README.md:119 stale claim without the declared result
FAIL r51-c2-scorecard-lead SCORECARD.md:28 stale claim without the declared result leading
FAIL r51-c2-province PROVINCE.md:17 stale claim without the declared result
correction sweep: 3 stale block(s)
exit=1

$ python3 -B verifiers/check_correction_sweep.py --self-test
0 failure(s) over 5 assertions
exit=0
```

The three FAIL strings and the file:line references match the lesson's fix cell verbatim (`FAIL r51-c2-readme corpus/README.md:119`, `FAIL r51-c2-scorecard-lead SCORECARD.md:28`, `FAIL r51-c2-province PROVINCE.md:17`; "0 failures over 5 assertions"). **The lesson's "shown able to fail" claim HOLDS.**

Registry as read at `c8407a4` (`verifiers/check_correction_sweep.py:31-38`) — three rows only:

| id | file | stale pattern | declared pattern | lead |
|---|---|---|---|---|
| `r51-c2-readme` | `corpus/README.md` | `overlap levers backed 7 of 7 clients` | `4 of 7` | no |
| `r51-c2-scorecard-lead` | `SCORECARD.md` | `` `7 of 7`, exit 0 @ `34cfffbb` `` | `4 of 7` | yes |
| `r51-c2-province` | `PROVINCE.md` | `overlap levers backed 7 of 7 clients` | `4 of 7` | no |

---

## 2. The four single-place reverts (mutation probes)

Each revert restores the place to its `c8579a4c` text, is committed in the sandbox, and the check is run at that sandbox commit. After each probe the sandbox is reset with `git reset --hard c8407a4`.

### M1 — `corpus/README.md` Core note (`:147-157` round-51 note + `:158-167` round-52 correction) → KILLED

Revert = delete the appended round-52 correction paragraph, restoring the base's unqualified note.

```
$ python3 -B verifiers/check_correction_sweep.py --rev 141ccd2
FAIL r51-c2-readme corpus/README.md:133 stale claim without the declared result
correction sweep: 1 stale block(s)
exit=1
```

**KILLED.** Expected detector: `r51-c2-readme` FAIL, exit 1. Observed: exactly that. The `4 of 7` declared pattern lives in the same bullet block as the stale phrase, so removing the correction removes the declared result with it.

### M2 — `corpus/README.md` index row (`:75`) → SURVIVED

Revert = restore the base index row (dropping the appended "**Round 52 correction (routed defect 1):**" sentence, which is what carries `removed in a scope` and `4 of 7`).

```
$ python3 -B verifiers/check_correction_sweep.py --rev 2facfe2
correction sweep: 0 stale block(s)
exit=0
```

**SURVIVED — the detector did not fire.** Root cause, measured on the reverted row: the base index row contains neither the stale phrase nor the declared phrase of the registry row that covers `corpus/README.md`:

```
$ python3 -c "t=open('base_row75.txt').read(); print('stale  \"overlap levers backed 7 of 7 clients\":', 'overlap levers backed 7 of 7 clients' in t); print('declared \"4 of 7\":', '4 of 7' in t); print('\"7 of 7\":', '7 of 7' in t)"
stale  "overlap levers backed 7 of 7 clients": False
declared "4 of 7": False
"7 of 7": False
```

The base index row states the superseded claim in a different wording — "seven client pages", "removed everywhere, or automatic choice off" — and names no count at all. The registry's only `corpus/README.md` row is keyed to the literal phrase `overlap levers backed 7 of 7 clients`, which the index row never contains. So the index-row repair is **unregistered**: no registry row covers it, and reverting it is invisible.

This matters because the lesson claims otherwise. `corpus/lessons/round-52.md:103` (routed defect 1) reads:

> `corpus/README.md:133-141` — correction appended inside the same bullet (`:144-153`), and the index row (`:75`) carries a correction naming `removed in a scope`. Fixed; caught by `check_correction_sweep.py` (M36).

"the index row … **caught by `check_correction_sweep.py`**" is false as written. M2 shows the index-row revert is caught by nothing: the check exits 0 on the reverted file. (The `:133-141` half of that sentence *is* caught — M1.) Severity: **MEDIUM-HIGH** — a false provenance claim in the lesson about the round's own mistake fix, on the exact axis under attack (calibration).

### M3 — `SCORECARD.md` depth lead (`:28`) → KILLED

Revert = restore the base depth row (the lead that opened with the widened `7 of 7`, exit 0 @ `34cfffbb`).

```
$ python3 -B verifiers/check_correction_sweep.py --rev b70e3cf
FAIL r51-c2-scorecard-lead SCORECARD.md:28 stale claim without the declared result leading
correction sweep: 1 stale block(s)
exit=1
```

**KILLED.** The `lead: true` rule fires: in the base row the stale phrase sits at offset 218 and the first `4 of 7` at offset 1655, so the declared result is *after* the stale claim, not before it.

### M4 — `PROVINCE.md` stale line (`:17`) → KILLED

Revert = restore the base `PROVINCE.md` (dropping the round-52 correction continuation line at `:18`).

```
$ python3 -B verifiers/check_correction_sweep.py --rev e4c9150
FAIL r51-c2-province PROVINCE.md:17 stale claim without the declared result
correction sweep: 1 stale block(s)
exit=1
```

**KILLED.** The stale phrase at offset 981 and the declared `4 of 7` at offset 1372 are in the same `- ` bullet block at the target; reverting removes the declared result with it.

**Summary of the four reverts: 3 killed (M1, M3, M4), 1 survived (M2).** The one that survived is precisely the one whose stale claim is worded differently from the registry's pattern.

---

## 3. Plant probes — a NEW stale statement of the same kind

### P1 — `SKILL.md` → SURVIVED (not seen)

Planted a new paragraph in `SKILL.md` (`## Anti-patterns`, after the overlap-levers paragraph, `:409-410`):

```
Overlap lever coverage (round 51 result): `python3 -B verifiers/check_overlap_levers.py --rev <rev>`
→ `overlap levers backed 7 of 7 clients`.
```

```
$ python3 -B verifiers/check_correction_sweep.py --rev d528ead
correction sweep: 0 stale block(s)
exit=0
```

**Not seen.** The check reads only the three files named in its registry; `SKILL.md` is not one of them.

### P2 — `corpus/knowledge/skill-overlap-levers-round51.md` → SURVIVED (not seen)

Planted under `## Findings` (`:40-42`):

```
Round-51 counter result: `python3 -B verifiers/check_overlap_levers.py --rev <rev>` prints
`overlap levers backed 7 of 7 clients`.
```

```
$ python3 -B verifiers/check_correction_sweep.py --rev 29a64d5
correction sweep: 0 stale block(s)
exit=0
```

**Not seen.** Same reason: the knowledge entry is not in the registry.

### P3 — different claim kind, in a *registered* file (`corpus/README.md`) → SURVIVED

Planted under `## Known gaps` (`:107-108`):

```
Round-52 C2 coverage (as measured): `python3 -B ../verifiers/check_mcp_instructions.py --rev <rev>`
prints `mcp instructions backed 0 of 7 clients`.
```

```
$ python3 -B verifiers/check_correction_sweep.py --rev 4bb5a21
correction sweep: 0 stale block(s)
exit=0
```

**Not seen.** Being in a registered file is not enough; the registry is keyed to the literal stale phrase of one specific claim, not to a class of claim.

### P4 — the *registered* phrase in a *different block* of `corpus/README.md` → KILLED

Planted the registry's own phrase at `corpus/README.md:107-108` (a different block from the Core note).

```
$ python3 -B verifiers/check_correction_sweep.py --rev 587eeab
FAIL r51-c2-readme corpus/README.md:107 stale claim without the declared result
correction sweep: 1 stale block(s)
exit=1
```

**KILLED.** So the check *is* block-wide within a registered file for the registered phrase: the sweep scans every block of a registered file, not only the block the correction was made in.

### P5 — stale phrase plus an unrelated `4 of 7` in the same block → SURVIVED

Planted the registered phrase and, in the same block, a sentence that has nothing to do with the claim: "Separately, 4 of 7 fixtures in an unrelated list were re-opened this round."

```
$ python3 -B verifiers/check_correction_sweep.py --rev 1d8b56f
correction sweep: 0 stale block(s)
exit=0
```

**SURVIVED.** The `declared` pattern is the bare string `4 of 7`; any occurrence of it in the block satisfies the rule, so an unrelated number launders a stale claim. The rule is a co-occurrence test, not a claim-binding test. Severity: **MEDIUM**.

### P6 — the index-row claim class, in `corpus/README.md` → SURVIVED

Planted the wording that the base index row actually used: "each client removes the skill everywhere (removed everywhere, or automatic choice off)."

```
$ python3 -B verifiers/check_correction_sweep.py --rev 6d8a1c8
correction sweep: 0 stale block(s)
exit=0
```

**SURVIVED** — the same wording that M2 reverted to, now confirmed to be invisible on its own terms, not merely because the revert removed a count.

### P7 — the registered phrase in a *different* `SCORECARD.md` row → KILLED

Planted `` `7 of 7`, exit 0 @ `34cfffbb` `` into the round-51 freshness row (`:258`).

```
$ python3 -B verifiers/check_correction_sweep.py --rev d94b7a8
FAIL r51-c2-scorecard-lead SCORECARD.md:258 stale claim without the declared result leading
correction sweep: 1 stale block(s)
exit=1
```

**KILLED.** Note the `lead` rule also applies to the new location: the stale phrase is found and the row has no `4 of 7` before it.

### P8 — paraphrase of the registered scorecard stale claim → SURVIVED

Planted "the round-51 counter printed 7 of 7, exit 0 at 34cfffbb" — same facts, no backticks, "at" instead of "@".

```
$ python3 -B verifiers/check_correction_sweep.py --rev d94b7a8   # P7 commit reused in run
correction sweep: 0 stale block(s)
exit=0
```

**SURVIVED.** The stale pattern is a literal regex; a paraphrase of the same claim is invisible.

**Plant summary: 6 of 8 probes survived.** The check sees a registered phrase anywhere in a registered file (P4, P7) and nothing else.

---

## 4. Answers to the two questions asked

### Is the check's scope wider than the three known places?

**No — it is exactly the three known places, plus one registered phrase per file.** The scope is the registry's three `(file, stale-phrase)` pairs, and nothing more:

- It is *file-bounded*: `SKILL.md` and knowledge entries are never read (P1, P2 both green).
- It is *phrase-bounded*: a different claim in a registered file is invisible (P3), and a paraphrase of the registered claim is invisible (P8).
- It is *block-wide within a registered file for the registered phrase*: the same phrase in another block of `corpus/README.md` or another row of `SCORECARD.md` is caught (P4, P7).
- The `declared` side is a bare `4 of 7` co-occurrence test, not a binding to the claim (P5).

The two live defects (M2's index row, P6's `removed everywhere` wording) are therefore not detectable by this instrument as written.

### Does the lesson say so?

**Partly, and the one place it speaks directly is false.**

What the lesson and criterion *do* say, accurately:

- `corpus/lessons/round-52.md:10` (M36 fix cell): "`verifiers/check_correction_sweep.py` with a registry of superseded claims: each block holding a stale claim must also hold the declared result (and lead with it in a SCORECARD cell)." — the word "registry" is accurate: a registry is a fixed list, and the docstring at `verifiers/check_correction_sweep.py:13-14` says "This check sweeps the registry below" and "A new superseded claim is added as a new registry row; rows are not edited." So the instrument's own docstring discloses that coverage is *registry-scoped*, not a general sweep.
- The M36 row's "Shown able to fail" receipt — the base/target outputs and the self-test tally — is exactly correct (section 1 above). **HOLDS.**

What the lesson and criterion *do not* say, and where they overclaim:

1. `corpus/lessons/round-52.md:103` — "the index row (`:75`) carries a correction naming `removed in a scope`. Fixed; **caught by `check_correction_sweep.py` (M36)**." **FALSE** (M2, P6). The index row is not in the registry; reverting it is caught by nothing. Severity **MEDIUM-HIGH**.
2. `corpus/QUALITY.md:40` (Q29) scope cell — "corrections of falsified or superseded claims (README, SCORECARD, **SKILL.md**, PROVINCE.md, **knowledge entries**)". At the judged revision the registry has rows for three of those five surfaces (`corpus/README.md`, `SCORECARD.md`, `PROVINCE.md`); `SKILL.md` and knowledge entries have none, so two named surfaces are unmonitored. (The sibling's in-flight extension adds an `SKILL.md` row, but for the *round-52* claim only — see section 5 — so the round-51 stale phrase planted in `SKILL.md` is still unseen, P1.) Q29's text ("the superseded claim's stale phrase and its declared result go into the registry") is satisfiable by registering the row *after* the fact; it does not say a place with no registry row is covered. Severity **MEDIUM**.
3. M36's captured-by cell cites PROTOCOL § Evidence standard, "Corrections sweep every mention", whose rule reads (fleet root `PROTOCOL.md:363-365`): "grep **every file the lane touches** (`corpus/README.md`, `SKILL.md`, `knowledge/`) for the superseded claim — a corrected fact left standing in a sibling file is still a defect." The committed instrument covers one file out of the three named, and only one phrase in it. The rule it claims to mechanize is broader than what it mechanizes. Severity **MEDIUM**.
4. The `declared` pattern is the bare `4 of 7` (P5). The sibling seat `CriticQ29.md:146-147` independently reached the same conclusion ("the `declared` pattern should be specific to the claim …, not a bare `4 of 7`"); my P5 is independent confirmation from the mutation side, with the survivor output.

**No automated gate exists for this check.** `grep -rn "check_correction_sweep" --include="*.sh" --include="*.py" --include="*.json"` over the lane returns only the script's own docstring and usage line — no runner, no `verifiers/floors-registry.json` entry, no CI hook. The "the sweep must exit 0 before the round's report" clause of Q29 therefore has no enforcer; a green exit is currently a thing a human must remember to run. Severity **MEDIUM-HIGH** (this is the sibling critic's Attack-4 territory; my contribution is the independent confirmation that no wiring exists, verified by that grep).

---

## 5. In-flight sibling change: the registry extension does not close these gaps

A sibling seat has an **uncommitted** change to `verifiers/check_correction_sweep.py` in the lane working tree (observed 2026-10-22T15:00:54-03:00; `git diff -- verifiers/check_correction_sweep.py`). It extends the registry from 3 rows to 6, adding three round-52 rows (`r52-c2-skill-silent` on `SKILL.md`, `r52-c2-province-five` on `PROVINCE.md`, `r52-c2-readme-five` on `corpus/README.md`) and two self-test arms. I re-ran my probes against that extended script, because a probe is only meaningful against the code that will actually be shipped.

**The extension does not close any of my findings.** On a tree carrying the sibling's own corrections (the lane working tree, copied read-only to a scratch dir), the extended script is green — `correction sweep: 0 stale block(s)`, exit 0 — and stays green when I re-plant each survivor:

| probe re-run against the **extended** registry | result |
|---|---|
| M2 — README index row reverted to base | exit 0, **still survives** |
| P1 — stale claim planted in `SKILL.md` | exit 0, **still survives** |
| P5 — stale phrase + unrelated `4 of 7` in same block | exit 0, **still survives** |
| P6 — the `removed everywhere` wording | exit 0, **still survives** |
| P8 — paraphrase of the scorecard stale claim | exit 0, **still survives** |

The extended self-test is green (`0 failure(s) over 7 assertions`, exit 0). The reason P1 still survives is that the new `SKILL.md` row registers a *different* claim (`say nothing about server instructions` → `S041`); the registry grew by adding rows for new claims, which does not make the registry discover claims it was not told about. M2, P5, P6 and P8 are all about the *round-51* rows, which the extension leaves untouched.

**One caution about the extension, found while re-running it.** The extended script is **red at the judged revision** `c8407a4`:

```
$ python3 -B <extended script> --rev c8407a453788df964df5a7b835dd0ce1360de882
FAIL r52-c2-skill-silent SKILL.md:94 stale claim without the declared result
FAIL r52-c2-province-five PROVINCE.md:19 stale claim without the declared result
FAIL r52-c2-readme-five corpus/README.md:78 stale claim without the declared result
correction sweep: 3 stale block(s)
exit=1
```

This is not a defect in the extension — the sibling's corrections to those three places are still uncommitted in the lane, so the extended registry correctly demands them. But it means the extension must land in the **same commit** as the corrections it registers, or the judged revision will be red under the new registry. Q29 already requires that ("the superseded claim's stale phrase and its declared result go into the registry in the same commit as the correction"), so this is the criterion working as intended; I record it as a sequencing constraint for the L1, not as a defect.

**Baseline-failure caveat, stated for honesty.** Because the extended script is red at `c8407a4`, re-running my four revert probes under the extended script would be *inconclusive by the mutation-testing rule* (a baseline failure is not a kill). I therefore ran the extension test the only sound way: on a tree where the sibling's own corrections are present (green baseline), then re-planting each survivor. Every "still survives" above is a green-baseline result and is therefore sound.

## 6. Additional observation — the lane's uncommitted `SCORECARD.md`

The attempt-1 L1 left one uncommitted file in the lane (`git diff -- SCORECARD.md`). It is an attack target named in my brief, so I ran the check against the lane working tree read-only:

```
$ cd /home/vgpnk/Projects/shokunin/kotoba-shokunin && python3 -B verifiers/check_correction_sweep.py --root .
correction sweep: 0 stale block(s)
exit=0
```

The working tree is clean under this check, so the uncommitted `SCORECARD.md` does not reintroduce a registered stale claim. [INFERENCE] The uncommitted diff rewrites the coverage and freshness rows to the round-52 values (`5 of 7`, `4 of 4 fixtures`); the depth row at `:28` is unchanged from `c8407a4` and keeps the corrected lead, so the registered row stays satisfied. No defect found here from this instrument's point of view — recorded for completeness, not scored.

---

## 7. Calibration verdict on the M36 fix itself

| claim | verdict | evidence |
|---|---|---|
| M36 "Shown able to fail": base red with the three named FAILs, target green, self-test 0/5 | **HOLDS** | section 1, outputs verbatim |
| Registry covers the README Core note | **HOLDS** | M1 killed, exit 1 |
| Registry covers the `SCORECARD.md` depth lead (with the lead rule) | **HOLDS** | M3 killed, exit 1 |
| Registry covers the `PROVINCE.md` stale line | **HOLDS** | M4 killed, exit 1 |
| Registry covers the README **index row** | **BREAKS** | M2 survived, exit 0 — false "caught by" at `corpus/lessons/round-52.md:103` |
| Check is a sweep of every mention (PROTOCOL § Evidence standard) | **BREAKS** | P1, P2, P3, P8 all survived; one of three named files, one phrase each |
| `declared` pattern binds the declared result to the claim | **BREAKS** | P5 survived |
| "the sweep must exit 0 before the round's report" is enforceable | **BREAKS** | no runner, no floors entry, no CI hook (grep above) |
| The sibling's in-flight registry extension (3→6 rows) closes the gaps above | **BREAKS** | section 5: M2, P1, P5, P6, P8 all still survive against the extended script on a green baseline |

**Severity summary:** MEDIUM-HIGH ×2 (M2 / false "caught by" provenance; Q29's "must exit 0" with no enforcer); MEDIUM ×3 (index row unregistered; Q29 scope names SKILL.md and knowledge entries with no rows; PROTOCOL rule broader than the instrument; bare `4 of 7` declared pattern).

**Note on a surviving mutant as a contract change.** M2 and P5 are coverage findings, not permission to change the contract. The contract as documented in the script's own docstring ("This check sweeps the registry below"; "A new superseded claim is added as a new registry row; rows are not edited") is internally consistent with what I measured — a registry is by construction a fixed list. The defect is in the *claims made about it elsewhere* (the lesson's "caught by", Q29's scope list, the PROTOCOL rule it is said to mechanize), not in the registry's stated design. The L1 should decide whether to (a) add a registry row for the README index row with a pattern matching its actual wording, (b) tighten the `declared` patterns to claim-specific strings, or (c) narrow the claims to match the instrument. I do not presume which.

---

## 8. Evidence: restoration

Sandbox `/fast/scratch/hyaku/kotoba-r52a2/MutSweepCheck` was reset with `git reset --hard c8407a453788df964df5a7b835dd0ce1360de882` after every probe. Final state:

```
$ git status --porcelain
(empty)

$ git log --oneline -1
c8407a4 round-52: C2 coverage - MCP server instructions per client (entry, rows S032-S037, SKILL.md table, PROVINCE Core); S038 supersedes S031; routed defects 1-2 corrected (README, SCORECARD depth lead) plus PROVINCE:17; M36 fix check_correction_sweep.py and Q29; round-52 lesson

$ sha256sum corpus/README.md SCORECARD.md PROVINCE.md SKILL.md corpus/knowledge/skill-overlap-levers-round51.md
c912b1e43d8c88bd65c809a45de124ba45f0d7ec6419fdfbd79049a4c3d84813  corpus/README.md
faacfb8c52e8cd212652d71ccc6044cd33cd186e63253d88c6ca5d71483bc976  SCORECARD.md
9a84316abb101df5bac5a455ca2eb0f355be09632f4704ceacdd7840ed84b1ce  PROVINCE.md
57dae36fc15590d69b162e0e9558d4b941e475313e5a0cadfce1aefb499c9766  SKILL.md
756058796ab3eebeda61a285b978bd923c1d7f3817d94907459b1276e3554f01  corpus/knowledge/skill-overlap-levers-round51.md

$ python3 -B verifiers/check_correction_sweep.py --rev HEAD
correction sweep: 0 stale block(s)
exit=0
```

All five hashes are byte-identical to the pre-probe values captured before the first mutation; `git status` is empty; the checkout is at the judged revision. The lane at `/home/vgpnk/Projects/shokunin/kotoba-shokunin` was never written to by this seat — only read (`git diff`, `git show`, `grep`, and the `--root .` read of the working tree). No `jj` command was run against the lane; no fleet-root, sibling-lane, `MANIFEST.json`, `.ufo/state` or `.ufo/watchdog.log` write was made. This report file is the only artifact written.

**Tooling:** no installs, upgrades or downgrades were performed by this seat; the tools used (`python3` 3.14.8, `git` 2.56.0, `uv` 0.13.0 present but unused) were already on the host. No pacman transaction was attempted (host-wide pacman transactions are paused).
