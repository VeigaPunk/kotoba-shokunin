# MutC1Counter — mutation test of `verifiers/check_r69_routed_repairs.py` (round 70, wave 1)

**Verdict: the self-test kills 20 of 50 single-point mutants and 30 survive.** The 17-assertion
`--self-test` guards one token per item list. It also pins the base-line anchors, blob pins,
receipt `measured-rev`, the receipt's per-block `exit=0` line and the gate status. It does **not**
guard the other tokens in each list (21 survivors), the K69-1 block boundaries, the LOG entry
boundary, K69-8's verdict and missing-`command:` checks, or K69-11's "id absent" path. It also
never exercises `Repo` or `main()`: the self-test swaps in `FakeRepo` and calls `check()` directly.
Every survivor below is a coverage finding, not a defect in the frozen predicate. The pristine
counter, run on committed bytes, gives the same readings the plan records:
base `0 of 10` exit 1, tip `9 of 10` exit 1, with only K69-11 open.

## Setup and detector

- Seat scratch: `mktemp -d /tmp/k70w1-MutC1Counter.XXXX` → `/tmp/k70w1-MutC1Counter.4a2A` (deleted before return).
- Pristine bytes: `git show HEAD:verifiers/check_r69_routed_repairs.py > $S/pristine.py` at HEAD
  `16b212a390c7ce68b6bce49b2c3766b154fbcbae` (last touched by `53de0ac`, the frozen-plan commit).
  `sha256sum`: lane file = scratch pristine = `bdabd71cdecbf8be31c719b1599a5ec29350f335c99e8c1b1f17e53a29437d98`.
- **Primary detector:** `python3 -B mutant.py --self-test`. A mutant counts as killed when the exit
  code is not 0. The pristine baseline is green:
  `self-test: 0 failure(s) over 17 assertions`, exit=0. That makes every reading conclusive, so no
  mutant is inconclusive.
- **Secondary readings (not part of the verdict):** each mutant was also run with
  `--repo <lane> --rev 7d51253f…` (base control) and `--rev 16b212a3…` (measured tip). Both read
  committed bytes only; K69-11 runs the gate inside the counter's own `git clone --shared` temp
  sandbox. Pristine readings: base `r69 routed defects closed 0 of 10` exit=1, tip
  `r69 routed defects closed 9 of 10` exit=1 (only `K69-11: governance.citation_resolves FAIL`).
- Driver: one exact-once string replacement per mutant. Each anchor was asserted to occur exactly
  once, and no anchor errors occurred. The driver ran self-test, base and tip for every mutant, then
  rewrote the pristine bytes and reran the self-test.

## Survivors table (self-test exit 0 with the mutation in place)

| id | mutation (single point) | self-test | base reading | tip reading | note |
|---|---|---|---|---|---|
| M02 | K69-1 `need` drops `R69_BASE` | 0 fail / 17, exit 0 | 0/10 x1 | 9/10 x1 | only the R69_TIP drop is tested |
| M03 | K69-1 `need` drops the 3 counter names | 0 / 17, exit 0 | 0/10 x1 | 9/10 x1 | |
| M04 | K69-1 block terminator → `(?=\Z)` (block runs to EOF) | 0 / 17, exit 0 | 0/10 x1 | 9/10 x1 | tokens after the block would count |
| M05 | K69-1 heading regex → `Round 69.*?` (any mention) | 0 / 17, exit 0 | 0/10 x1 | 9/10 x1 | "heading only" world still fails on tokens |
| M07 | K69-2 drops `orchestrator` | 0 / 17, exit 0 | 0/10 x1 | 9/10 x1 | |
| M09 | `R69_COMMITS` drops `a02ba7e` | 0 / 17, exit 0 | 0/10 x1 | 9/10 x1 | only `278b9dc` is tested |
| M10 | K69-3 drops `4844216b` | 0 / 17, exit 0 | 0/10 x1 | 9/10 x1 | only `probe` is tested |
| M11 | K69-3 drops `9d9f181e` | 0 / 17, exit 0 | 0/10 x1 | 9/10 x1 | |
| M13 | K69-3 drops `0a1199a0` | 0 / 17, exit 0 | 0/10 x1 | 9/10 x1 | |
| M20 | LOG entry not bounded by the next `## ` heading | 0 / 17, exit 0 | 0/10 x1 | 9/10 x1 | later sections' tokens would count |
| M21 | LOG heading `startswith("## Round 69")` → `"Round 69" in line` | 0 / 17, exit 0 | 0/10 x1 | 9/10 x1 | |
| M22 | `LABELS` drops `pointer` | 0 / 17, exit 0 | 0/10 x1 | 9/10 x1 | only `outcome` is tested |
| M23 | `LABELS` drops `trigger` | 0 / 17, exit 0 | 0/10 x1 | 9/10 x1 | |
| M25 | K69-7 drops `23 landed` | 0 / 17, exit 0 | 0/10 x1 | 9/10 x1 | only `10 receipts` is tested |
| M26 | K69-7 drops `1 dispositioned` | 0 / 17, exit 0 | 0/10 x1 | 9/10 x1 | |
| M32 | K69-8 verdict-line check disabled | 0 / 17, exit 0 | 0/10 x1 | 9/10 x1 | no world breaks a verdict line |
| M33 | K69-8 missing `command:` block skipped silently | 0 / 17, exit 0 | 0/10 x1 | 9/10 x1 | no world drops a command block |
| M34 | K69-8 verdict searched in whole receipt, not the block | 0 / 17, exit 0 | 0/10 x1 | 9/10 x1 | |
| M36 | K69-9 drops `S201` | 0 / 17, exit 0 | 0/10 x1 | 9/10 x1 | |
| M37 | K69-9 drops `(13 words)` | 0 / 17, exit 0 | 0/10 x1 | 9/10 x1 | |
| M39 | K69-10 drops `(18 assertions)` | 0 / 17, exit 0 | 0/10 x1 | 9/10 x1 | only "not appended" is tested |
| M40 | K69-10 drops `22 assertions` | 0 / 17, exit 0 | 0/10 x1 | 9/10 x1 | |
| M43 | K69-11 "check id absent" → counted closed | 0 / 17, exit 0 | 0/10 x1 | 9/10 x1 | no world omits the id |
| M45 | `main` returns 0 regardless of N (**accepts an exit=1 world**) | 0 / 17, exit 0 | **0/10 exit=0** | **9/10 exit=0** | `main` unexercised; only the base control (`controls/C1-base.txt` expects exit 1) catches it |
| M46 | `main` skips rev resolution (`rev = args.rev`, any measured-rev echoed) | 0 / 17, exit 0 | 0/10 x1 | 9/10 x1 | equivalent for full-SHA input; differs for short/symbolic revs |
| M47 | `main` unknown `--rev` no longer exit 2 | 0 / 17, exit 0 | 0/10 x1 | 9/10 x1 | unobserved on a bad rev |
| M48 | K69-11 sandbox checks out `HEAD`, not `--rev` | 0 / 17, exit 0 | 0/10 x1 | 9/10 x1 | `Repo.checklist` unexercised; masked here because base and tip both FAIL the gate |
| M49 | `Repo.show` ignores its `rev` arg (base bytes = measured bytes) | 0 / 17, exit 0 | 0/10 x1 | **4/10 x1** | `Repo` unexercised; the tip reading moves from 9 to 4 |
| M50 | `BASE` constant → r69 base `a5f7459f…` | 0 / 17, exit 0 | 0/10 x1 | 9/10 x1 | equivalent under self-test (`FakeRepo` keys on `BASE`); undetected by both real runs |

"x1" = exit 1. "0 / 17" = `self-test: 0 failure(s) over 17 assertions`.

## Killed mutants (self-test exit 1)

| id | mutation | failing self-test assertion (stderr) |
|---|---|---|
| M01 | K69-1 drops `R69_TIP` | `K69-1 block without the r69 tip -> closed 10` |
| M06 | K69-2 drops `fast-forward` | `K69-2 no fast-forward record -> closed 10` |
| M08 | K69-2 drops all four commits | `K69-2 a round commit missing -> closed 10` |
| M12 | K69-3 drops `probe` | `K69-3 attribution missing -> closed 10` |
| M14 | K69-5 ignores blob pins (`if False:`) | `K69-5 wrong blob -> closed 10` |
| M15 | K69-5 presence-only blob (`got is None`) | `K69-5 wrong blob -> closed 10` |
| M16 | K69-5 pins only the first path | `K69-5 wrong blob -> closed 10` |
| M17 | K69-5 drops lesson-names-paths | `K69-5 lesson omits a path -> closed 10` |
| M18 | **base-line slicing flipped** in the LOG scan (`range(0, …)`) | `K69-6 entry inside base (no appended heading) -> closed 10` |
| M19 | `_base_lines` returns 0 | `K69-6 entry inside base…` and `K69-10 erratum not appended…` (2 failures) |
| M24 | `LABELS` drops `outcome` | `K69-6 label missing -> closed 10` |
| M27 | K69-7 drops `10 receipts` | `K69-7 nine receipts -> closed 10` |
| M28 | K69-8 **accepts any measured-rev** (`[0-9a-f]{40}`) | `K69-8 receipt pinned elsewhere -> closed 10` |
| M29 | K69-8 measured-rev check removed | `K69-8 receipt pinned elsewhere -> closed 10` |
| M30 | K69-8 **accepts exit=1** (`^exit=\d`) | `K69-8 red exit -> closed 10` |
| M31 | K69-8 `exit=0` searched in whole receipt | `K69-8 red exit -> closed 10` |
| M35 | K69-9 drops `(14 words)` | `K69-9 no new count -> closed 10` |
| M38 | K69-10 **base-line slicing flipped** (whole file) | `K69-10 erratum not appended -> closed 10` |
| M41 | K69-11 accepts any status | `K69-11 gate red -> closed 10` (secondary readings: **tip 10/10 exit=0**, base 1/10) |
| M42 | K69-11 unreadable gate → closed | `K69-11 gate unreadable -> closed 10` |
| M44 | `check()` counts every item closed | 16 failures; secondary readings: base **10/10 exit=0**, tip 10/10 exit=0 |

## Findings for the owner (coverage only; this seat changes nothing)

1. **Item token lists are guarded by one token each.** K69-1 (base pin, the three counter names), K69-2
   (`orchestrator`, `a02ba7e`), K69-3 (3 of 4 attribution tokens), K69-6 (`trigger`, `pointer`),
   K69-7 (`23 landed`, `1 dispositioned`), K69-9 (`S201`, `(13 words)`) and K69-10 (both tokens)
   all survive being dropped: M02, M03, M07, M09–M11, M13, M22, M23, M25, M26, M36, M37, M39, M40.
   The plan's per-item tokens (`plans/round-70.md:38-58`) are therefore enforced by the code text
   alone. The self-test would not notice if one were deleted.
2. **Scope boundaries are untested.** M04 (K69-1 block to EOF), M05 (any `Round 69` text) and
   M20/M21 (LOG entry unbounded / heading anywhere in a line) survive. The heading-only world
   (`check_r69_routed_repairs.py:340-341`) is killed by the missing tokens, not by the heading regex.
3. **K69-8 structure is half-guarded.** The pin and the exit line are killed (M28–M31). The verdict
   line (M32, M34) and the missing-`command:` path (M33) survive, because no broken world edits
   them (`:351-353` are the only K69-8 worlds).
4. **The `Repo` and `main` paths sit outside the self-test.** M45 makes the counter exit 0 at
   `0 of 10`, which fails the frozen predicate's exit rule. Only the base control catches it, through
   its recorded exit 1. M49 changes the real tip reading from 9 to 4 with the self-test still green.
   M48 (gate on `HEAD`) is masked in this round only because base and tip both FAIL K69-11.
5. **M50 (wrong `BASE` pin) survives every detector exercised here.** The `--self-test` misses it
   because `FakeRepo.show` keys on the same constant (`:276`). Both real runs still read 0/10 and 9/10.

No surviving mutant can raise the measured-tip reading to 10 of 10. Only the killed M41 and M44 did.
So no survivor would, by itself, flip C1's declared miss into a pass.

## Restoration evidence

- After the loop, the driver wrote the pristine bytes back to `mutant.py`:
  `sha256 = bdabd71cdecbf8be31c719b1599a5ec29350f335c99e8c1b1f17e53a29437d98`,
  `equal_pristine: True`, restored `--self-test` exit 0, `self-test: 0 failure(s) over 17 assertions`.
- Lane file after the run: `sha256sum verifiers/check_r69_routed_repairs.py` →
  `bdabd71c…37d98` (unchanged), HEAD still `16b212a390c7ce68b6bce49b2c3766b154fbcbae`.
- `git status --porcelain -- verifiers/ SKILL.md corpus/ plans/ LOG.md SCORECARD.md` lists
  `corpus/README.md`, `corpus/knowledge/skill-eval-artefacts-round70.md` and
  `verifiers/verify_skill_checklist.py` as modified. This seat never wrote any of them; they come
  from concurrent sibling seats. The target counter is not among them. The secondary runs read only
  committed bytes (`git show <rev>:…`, and a sandbox checkout of `<rev>`), so these dirty files did
  not affect any reading.
- Scratch dir `/tmp/k70w1-MutC1Counter.4a2A` removed before return.

## Notes

- Tooling: nothing installed or updated.
- `skill://godspeed` was not found under `~/.omp` (`find ~/.omp -maxdepth 5 -ipath '*godspeed*' -name '*.md'`
  → no output), so it was not read.
