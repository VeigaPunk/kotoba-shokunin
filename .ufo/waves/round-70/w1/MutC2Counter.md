# MutC2Counter — mutation test of `verifiers/check_skill_evals.py` (round 70, wave 1)

## Verdict

**The self-test is weak: 23 of 34 single-point mutants survive it (11 killed).** Every survivor except
M09 and M27 would let a real defect in the repo be counted as backed, or would change an exit code;
each one has a reproduced witness world (a commit in a `git clone --shared` sandbox). **Two survivors
change the verdict at `--rev 16b212a390c7ce68b6bce49b2c3766b154fbcbae`.** M11 (sha check inverted)
turns `8 of 8 exit=0` into `environment error: snapshot_tampered … exit=2`. M31 (exit rule `!=`)
turns it into `8 of 8 exit=1`. No other survivor moves the tip reading: the tip is an honest 8-of-8
world, so every loosening mutant still reads `8 of 8 exit=0` there. Their effect shows only on the
defect worlds below. The pristine counter rejects all 16 defect worlds, so C2's tip reading is not
in doubt from this probe. The finding is about coverage: the 13-assertion self-test does not pin the
contract's own clauses.

Named probes from the tasking:

| tasking item | mutant | self-test |
|---|---|---|
| drop a key term | M01 F1 `by hand`, M02 F2 `produced`, M04 F7 `0.5`, M05 F8 `>=` survive; M03 F6 (sole term) killed | 4 of 5 survive |
| invert the 5–25 bound | M06 killed; but M07 (25→250) and M08 (5→1) survive | each bound side unpinned |
| skip the snapshot sha check | M10 | **survives** |
| skip the quote-in-snapshot check | M13 | killed |
| skip the mined check | M14 | killed |
| skip the used-by check | M15 | killed |
| skip the source:-line check | M19 | killed |
| skip the SKILL.md check | M21, M34 | killed |
| change `== TOTAL` | M30 `>= TOTAL-1`, M31 `!=`, M32 always 0 survive; M29 `TOTAL = 7` killed | main() never exercised |

## Method (commands run, all in `/tmp/k70w1-MutC2Counter.y7GC`, deleted on return)

- `cp verifiers/check_skill_evals.py $D/pristine.py`: sha256 `fc768197e10b152c444985a8fe41cf1c62f6d1c0605251d198d921dc35b68db2`
  for both the lane copy and the scratch copy.
- `git clone -q --shared <lane> $D/sb && git -C $D/sb checkout -q --detach 16b212a…`: sandbox for the witness
  worlds. Each world is one commit off the tip (`worlds.py`, table below).
- `mutate.py`: for each mutant, asserts `old` occurs exactly once in the pristine bytes, writes
  `mutants/Mxx.py`, then runs:
  `python3 -B Mxx.py --self-test`;
  `--repo <lane> --rev 16b212a…` (tip);
  `--repo <lane> --rev 7d51253f…` (base);
  `--repo <lane> --rev deadbeefdeadbeef` (unknown rev);
  and `--repo $D/sb --rev <world>` for all 18 worlds.
  "Killed" means self-test exit ≠ 0. The lane reads use `git show <rev>:path` only, i.e. committed bytes.
- Tools: python 3.14.8, git 2.56.0 (pre-installed). **No installs or upgrades.**

### Pristine baseline (the detector passes before mutation; nothing is inconclusive)

```
$ python3 -B verifiers/check_skill_evals.py --self-test      -> self-test: 0 failure(s) over 13 assertions, exit=0
$ ... --rev 16b212a390c7ce68b6bce49b2c3766b154fbcbae          -> skill eval facts backed 8 of 8, exit=0
$ ... --rev 7d51253f99906b8551b6a0a108761eedac00de74          -> skill eval facts backed 0 of 8 (entry absent), exit=1
$ ... --rev deadbeefdeadbeef                                  -> environment error: unknown revision deadbeefdeadbeef, exit=2
```

### Witness worlds (sandbox commits off the tip) and the pristine reading of each

| world | defect introduced | pristine |
|---|---|---|
| W01 | `S209` snapshot bytes appended (`\nforged line\n`) | `snapshot_tampered: S209… exit=2` |
| W02 | `S210` snapshot deleted | `snapshot S210… not committed … exit=2` |
| W03 | F4 quote = the full on-snapshot line 170 (30 words after norm) | 7 of 8 (`F4: quote is 30 words`) |
| W04 | F8 quote `">= trigger_threshold"` (2 words, on snapshot) | 7 of 8 (`F8: quote is 2 words`) |
| W05 | F1 quote `"Store test cases in evals/evals.json inside your skill directory:"` (on snapshot, S209 l.19) | 7 of 8 (lacks `by hand`) |
| W06 | F8 quote `"did_pass = trigger_rate < trigger_threshold"`: the **inverted operator, verbatim on the S211 snapshot l.234** | 7 of 8 (lacks `>=`) |
| W07 | F7 quote without `(0.5 is a reasonable default)` | 7 of 8 (lacks `0.5`) |
| W08 | F1 quote cell carries a second quote `"invented second quote"` | 7 of 8 (2 quotes) |
| W09 | F1 row cites `S209 S999` | 7 of 8 (2 S###) |
| W10 | SOURCES `S209` row given a 12th cell | 2 of 8 (not 11-cell) |
| W11 | SOURCES `S210` used-by cell `—`, entry path moved into cell 7 | 7 of 8 |
| W12 | SOURCES `S211` status cell `queued`, `mined` moved into the date cell | 7 of 8 |
| W13 | SKILL.md cites `…skill-eval-artefacts-round71.md` | 0 of 8 |
| W14 | F1 row cites `S124` (no pinned snapshot) | 7 of 8 (`S124 has no pinned snapshot`) |
| W15 | entry line `source: S211 —` → `~source: S211 —` | 7 of 8 (source: line lacks S211) |
| W16 | F8 quote `"if should_trigger: did_pass = trigger_rate >= trigger_threshold"` (spans S211 l.231–232) | **8 of 8 exit=0** (honest variant; whitespace collapse is meant to accept it) |
| W17 | F4 quote lower-cased `pass or fail` (off-snapshot) | 7 of 8 |
| W18 | F2 quote `"The other JSON files (grading.json, timing.json, benchmark.json)"` (on snapshot, lacks `produced`) | 7 of 8 |

## Survivors table (self-test exit 0, `self-test: 0 failure(s) over 13 assertions` for every row)

"Tip" is `--rev 16b212a…` against the lane; pristine reads `8 of 8 exit=0`.

| mutant | single-point change (pristine line) | tip verdict | other readings that change (pristine → mutant) |
|---|---|---|---|
| M01 | `"F1": ("evals/evals.json", "by hand")` → `("evals/evals.json",)` (l.59) | unchanged | W05 7/8 exit=1 → **8/8 exit=0** |
| M02 | F2 drops `"produced"` (l.60) | unchanged | W18 7/8 exit=1 → **8/8 exit=0** |
| M04 | F7 drops `"0.5"` (l.65) | unchanged | W07 7/8 exit=1 → **8/8 exit=0** |
| M05 | F8 drops `">="` (l.66) | unchanged | W06 7/8 exit=1 → **8/8 exit=0**: an on-snapshot `<` quote backs the fact that says `>=` |
| M07 | `<= 25` → `<= 250` (l.150) | unchanged | W03 7/8 → **8/8 exit=0** |
| M08 | `5 <=` → `1 <=` (l.150) | unchanged | W04 7/8 → **8/8 exit=0** |
| M09 | key terms matched case-insensitively (l.153) | unchanged | none. **Equivalent on the pinned snapshots**: a brute-force over every 5–25-word window of the three normalised snapshots found 0 windows (without `"` or `\|`) that meet a fact's terms case-insensitively but not exactly (133 such windows exist, all containing `"`, which `QUOTE_RE` cannot capture) |
| M10 | sha256 check → `if False:` (l.95) | unchanged | W01 `snapshot_tampered exit=2` → **8/8 exit=0** |
| M11 | sha256 `!=` → `==` (l.95) | **8/8 exit=0 → `environment error: snapshot_tampered: S209-evaluating-skills.md` exit=2** | every world → exit 2 |
| M12 | missing snapshot `raise EnvError` → `return ""` (l.94) | unchanged | W02 exit=2 → 7/8 exit=1 (environment error laundered into a content verdict) |
| M16 | `row[7] != "mined"` → `"mined" not in row` (l.167) | unchanged | W12 7/8 → **8/8 exit=0** |
| M17 | `ENTRY not in row[10]` → `ENTRY not in " ".join(row)` (l.167) | unchanged | W11 7/8 → **8/8 exit=0** |
| M18 | `len(row) != 11` → `len(row) < 11` (l.164) | unchanged | W10 2/8 → **8/8 exit=0** |
| M20 | `l.startswith("source:")` → `"source:" in l` (l.131) | unchanged | W15 7/8 → **8/8 exit=0** |
| M22 | `ENTRY in skill` → `"skill-eval-artefacts" in skill` (l.135) | unchanged | W13 0/8 → **8/8 exit=0** |
| M24 | `len(sids) != 1` → `len(sids) < 1` (l.146) | unchanged | W09 7/8 → **8/8 exit=0** |
| M25 | `len(quotes) != 1` → `len(quotes) < 1` (l.146) | unchanged | W08 7/8 → **8/8 exit=0** |
| M26 | `if sid not in SNAPSHOTS:` → `if False:` (l.157) | unchanged | W14 7/8 exit=1 → `KeyError: 'S124'` traceback, exit=1 (crash, no verdict line) |
| M27 | `norm` stops collapsing whitespace (l.77) | unchanged | W16 8/8 exit=0 → 7/8 exit=1 (stricter mutant: false negative on an honest cross-line quote) |
| M30 | `return 0 if n == TOTAL` → `n >= TOTAL - 1` (l.349) | unchanged | W03–W09, W11, W12, W14, W15, W17, W18: 7/8 exit=1 → **7/8 exit=0** |
| M31 | `n == TOTAL` → `n != TOTAL` (l.349) | **8/8 exit=0 → 8/8 exit=1** | base 0/8 exit=1 → **exit=0**; every world flips |
| M32 | `return 0 if n == TOTAL else 1` → `return 0` (l.349) | unchanged | base 0/8 exit=1 → **exit=0**; every 7/8, 2/8, 0/8 world → exit=0 |
| M33 | rev-parse failure check → `if False:` (l.331) | unchanged | `--rev deadbeefdeadbeef` exit=2 → **`measured-rev: ` (empty) / 8 of 8 exit=0**: with `rev == ""`, `git show :path` reads the **Git index**. Confirmed with the sandbox index at W13: same command printed `0 of 8` |

### Killed (11)

| mutant | change | killing assertion (first FAIL line) |
|---|---|---|
| M03 | F6 terms → `()` | `junk control … -> backed 1` |
| M06 | drop `not` on the 5–25 bound | `honest world: backed 0 of 8` (tip → 0/8 exit=1) |
| M13 | skip quote-in-snapshot | `forged control … -> backed 8` |
| M14 | skip mined | `row not mined -> backed 8` |
| M15 | skip used-by | `used-by lacks the entry -> backed 8` |
| M19 | skip source:-line | `source: line omits S211 -> backed 8` |
| M21 | `skill_ok = True` | `SKILL.md does not cite the entry -> backed 8` |
| M23 | `len(got) < 1` (duplicate rows) | `duplicate F3 row -> backed 8` |
| M28 | `norm` stops stripping backticks | `honest world: backed 6 of 8` (tip → 6/8 exit=1) |
| M29 | `TOTAL = 7` | `honest world: backed 8 of 7` |
| M34 | `if skill_ok:` → `if True:` | `SKILL.md does not cite the entry -> backed 8` |

The first run's M28 was malformed by me (unbalanced parenthesis, `SyntaxError`). I corrected it and
reran the whole matrix against a single, consistent world set. The rows above all come from the rerun.

## Why they survive (pointers into the counter)

1. **`FakeRepo.snapshot` has no sha** (`check_skill_evals.py:231-235`). The only snapshot assertion
   sets a snapshot to `None` (l.304-311), so nothing in the self-test exercises `Repo.snapshot`
   (l.89-97). This lets M10, M11 and M12 survive. M11 breaks the tip outright.
2. **`main()` is never exercised by `--self-test`** (l.323-324 returns before the exit rule at l.349 and the rev
   check at l.329-333). Hence M30–M33. M31 flips the tip and the base; M33 lets an unknown rev
   score the index.
3. **Every broken world violates two clauses at once.** The "quote over 25 words" world pads F4 with `" x" * 30`
   (l.291), which also leaves the snapshot. The "F8 inverted operator" world (l.292) fails only
   because the fake S211 snapshot (l.208) omits the `<` branch. The **real** snapshot carries it at
   l.234, which is why M05 + W06 is live. The junk control (l.279-281) lacks *all* terms of the
   multi-term facts, so dropping any one term survives. Only the single-term F6 (M03) dies.
4. **Positional/shape/multiplicity clauses have no isolated world.** The column positions of mined and
   used-by (M16, M17), the 11-cell shape (M18), one S###/one quote (M24, M25), the pinned-snapshot
   membership (M26), the `source:` anchor (M20) and the exact SKILL.md path (M22) each lack one.

## Restoration evidence

- Lane `verifiers/check_skill_evals.py` sha256 before: `fc768197e10b152c444985a8fe41cf1c62f6d1c0605251d198d921dc35b68db2`.
  After all runs: the same value. `git -C <lane> diff --stat 16b212a… -- verifiers/check_skill_evals.py`
  → empty. `mutate.py` asserted the scratch pristine sha unchanged after writing all 34 mutants.
- The lane was never written except this report. `git status --porcelain` shows modified
  `corpus/QUALITY.md`, `corpus/README.md`, `corpus/knowledge/skill-eval-artefacts-round70.md`,
  `corpus/lessons/round-70.md` and `verifiers/verify_skill_checklist.py`. These are other seats'
  working-tree edits, not mine. All my lane reads were `git show 16b212a…:` / `7d51253f…:` committed bytes.
- The sandbox HEAD was restored to `16b212a390c7ce68b6bce49b2c3766b154fbcbae` and the scratch dir was deleted on return.
- Unobserved: `--fetch` (the live-URL second evidence) was not mutated or run. It is outside N.

## Mutant shas (sha256, first 16 hex)

M01 2c5bc6620df5dcdb · M02 2c415cd6d1116ebf · M03 a5f3ce61652714b5 · M04 74bea028992cbae4 · M05 db0b05effb3205db ·
M06 23f95eae791bef45 · M07 3d1ab068cc8da7e1 · M08 04a0014f16b8aa64 · M09 769dc2573c34cd81 · M10 82652f6eb7acdca3 ·
M11 2859540409770069 · M12 a107fe0f5aeccfd5 · M13 47a702ee696a8e01 · M14 5dfb983060a817c5 · M15 8c6c1cf1704ed098 ·
M16 d34dfdbf000bd00c · M17 c9700cee1bc47c5d · M18 f99e5fdca71a1d6b · M19 f1c42bc121066630 · M20 009680aa5a20d335 ·
M21 172400f8854b4d17 · M22 0c68546aa6cc01b9 · M23 a0e5669c1638d278 · M24 ee4915465c383038 · M25 d5fb605335b8a9c9 ·
M26 9e33dce3d0ecab62 · M27 3679668517156aa5 · M28 8766389f972de140 · M29 e6495a155973961a · M30 bf9c1d5e59b06c49 ·
M31 5da7250e67e81142 · M32 5dec0789a50dd7cf · M33 acebbd374489f59b · M34 fa33962a3cf97e8c
