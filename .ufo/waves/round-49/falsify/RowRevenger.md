# RowRevenger — C1 census row `revenger` falsify seat (round 49)

**HOLDS** — for the census row `revenger` (`corpus/knowledge/sibling-overlap-census-round49.md`,
branch `main`, pin `876630dbb4d630e016d7d8c32a19ea04c646cbae`, skill file NONE, classification
`none`, both mechanical columns `no SKILL.md`, quote at `PROVINCE.md:3`) and for the matching
`PROVINCE.md` § Adjacent row (line 52). No attack flipped any cell. One LOW wording finding on the
boundary note; residual risks listed.

## Findings

### LOW-1 — § Adjacent revenger note says "(theirs to arbitrate)"; the fleet record says integrator/operator-owned

`PROVINCE.md:52` boundary cell ends "overlaps kaidoku (theirs to arbitrate)". The committed record
of both interested sides assigns the ruling upward, not to the two lanes:

- kaidoku at its own pin `08c7a729`: `corpus/lessons/round-17-verifier-spotcheck.md:127` "the
  revenger/kaidoku contest is unchanged (**integrator-owned**)"; `round-24-verifier-spotcheck.md:63`
  "an **operator**/revenger overlap question"; `SKILL.md:677` "remains an open **L0** question".
- kotoba's own census (the declared source of the section), finding 4: "Both belong to the
  integrator"; and the § Adjacent kaidoku row (line 42) says "reported to the integrator".

So the revenger cell's parenthetical contradicts both its source entry and its sibling row two lines
up. Substance intact (the dispute is open and not kotoba's to rule on; domain overlap is real), so
LOW — a wording fix, not a reclassification.

### Examined and held (each named attack, with the result)

1. **Commit/branch cell.** Pin exists; `git log -1` decorations `(HEAD, origin/main, origin/HEAD,
   main)`; `rev-parse main` = pin. Row cell `main` is correct even though HEAD is detached (the
   build seat's own header "main(detached)" is the same fact, not a cell mismatch).
2. **Quote verbatim at `PROVINCE.md:3` (±2).** Collapsed lines 3-5 are "Owns: … runtime evidence —
   using the REA skill and its toolset,"; the row quote is an exact whitespace-collapsed substring
   ending at "runtime evidence" (python substring check: True). Guard re-read it at the pin: exit 0.
3. **Classification `none` under § Classification rule.** kotoba's core (PROVINCE.md § Core) is
   skill/agent-def/dispatch-prompt craft plus instruments over those surfaces. revenger's committed
   scope surfaces at the pin claim none of it:
   - No SKILL.md/AGENTS.md anywhere (`git show …:SKILL.md` exit 128; 864-entry tree, name grep
     `skill|agents` → 0). Its SKILL.md mentions are (a) the external REA skill
     (`PROVINCE.md:10`, `corpus/knowledge/seed.md`) and (b) its **own absent** SKILL.md/AGENTS.md as
     named debt (`SCORECARD.md:109,124`; `SHONEN.md:5-6`; `README.md:10`; `considerthese/2026-10-20.md:85`)
     — debt is not a claim of craft.
   - `PROVINCE.md:22` refuses "harness/evidence auditing (harness-integrity, gate-evidence,
     rlm-dispatch)". A refusal, in one list with refusals of game-dev-2d and lore; it names neither
     kotoba nor skill/prompt craft, and `PROVINCE.md:31-32` explicitly disclaims taking ownership of
     generic harness gates. Not a stated split between revenger and kotoba.
   - corpus/ sweep (rule's named surface, excluding fixtures/live): every hit RE-domain or
     self-referential; `round-62-commonjs-require-name-evidence.md:68` "declares no ownership and no
     ruling". corpus/verify_*.py are RE-fixture instruments, not instruments over skill surfaces.
   - considerthese/ (not in the build seat's five-doc grep): 0 hits for
     `kotoba|prompt craft|skill craft|dispatch prompt|arbitrat`.
   - corpus/fixtures + corpus/live craft-token sweep: 1 benign hit (`limit-sentinel.md:36` "Fail
     criteria (not triggered)" — the token `trigger`).
   - Tree-wide `kotoba`: 0 files (seat's count; my greps never matched it either).
   This closes the census's own stated `none` risk ("a claim stated only in an unread wave report")
   for every surface the rule names: SKILL.md (absent), PROVINCE.md, corpus/ (all), tools (none; no
   tools/ or verifiers/ directory).
4. **Mechanical columns re-derived.** `git show <pin>:SKILL.md` → exit 128 and zero tree entries
   matching `skill|agents` ⇒ no skill file at the pin ⇒ `names kotoba: no SKILL.md`,
   `arbitration: no SKILL.md` are the only correct cells.
5. **§ Adjacent revenger row facts.** "reverse engineering of shipped artifacts" = revenger
   `PROVINCE.md:3` verbatim; "no skill file at the pin" = verified; "overlaps kaidoku" = kaidoku's
   description at its pin says "Domain specialist — reverse engineering of shipped artifacts with
   REA on this Linux host" (kaidoku `SKILL.md:3` frontmatter, `08c7a729`), and kaidoku records the
   boundary open (`SKILL.md:677,722`; `PROVINCE.md:240,272,303`; `SCORECARD.md:2748`) — see LOW-1
   for the owner wording.
6. **"(seed-form lanes)" parenthetical** (census Counts, line 96): sourced — revenger's own
   `README.md:11` at the pin carries the fleet clause "(absent on lanes still in shonen seed form)".
   Not a defect.
7. **Round-49 LOG entry**: no revenger-specific factual claims; aggregates (7 adjacent / 13 none /
   0 contested; 20 pinned rows) consistent with the entry and my guard run.

## Guard (run, not assumed)

`python3 -B verifiers/check_sibling_census.py corpus/knowledge/sibling-overlap-census-round49.md
--province PROVINCE.md` (lane root) → stdout "rows 20 verified 20" / "province rows 20 matched 20",
**exit 0** — the revenger row joins its census row and its pinned quote.

## Evidence (all run 2026-10-22; sibling access read-only: show/ls-tree/rev-parse/log/grep/rev-list)

```
git -C revenger-shokunin rev-parse 876630dbb4d630e016d7d8c32a19ea04c646cbae^{commit}   exit 0
git -C revenger-shokunin log -1 --format='%H %d %s' <pin>
  → 876630d… (HEAD, origin/main, origin/HEAD, main) 2026-10-21 round-62 …               exit 0
git -C revenger-shokunin show <pin>:SKILL.md          → exit 128 (no such path)
git -C revenger-shokunin ls-tree -r --name-only <pin> | wc -l → 864                    exit 0
git -C revenger-shokunin ls-tree -r --name-only <pin> | grep -icE 'skill|agents' → 0   exit 1
git -C revenger-shokunin show <pin>:PROVINCE.md        (32 lines; Owns :3-5, Refuses :19-23,
   writes-only-this-repo :25-32)                        exit 0
quote substring check (python, collapsed lines 3-5)    → True                          exit 0
git -C revenger-shokunin grep -inE '<craft pattern>' <pin> -- corpus ':!corpus/fixtures'
  ':!corpus/live'  → all hits RE-domain/self-referential (enumerated in report)        exit 0
git -C revenger-shokunin grep -icE 'kotoba|prompt craft|skill craft|dispatch prompt|arbitrat'
  <pin> -- considerthese → 0                                                            exit 1
git -C revenger-shokunin grep -inE 'kotoba|frontmatter|AGENTS\.md|trigger|prompt craft|skill craft'
  <pin> -- corpus/fixtures corpus/live → 1 hit, limit-sentinel.md:36 (benign)          exit 0
git -C revenger-shokunin show <pin>:README.md | grep -n -i seed → 11: …shonen seed form… exit 0
git -C kaidoku-shokunin show 08c7a729…:SKILL.md | sed -n 1,6p  (description line confirms
  "reverse engineering of shipped artifacts with REA on this Linux host")              exit 0
git -C kaidoku-shokunin grep -in revenger 08c7a729… -- ':!.ufo' ':!corpus/live' → 30 hits:
  SKILL.md:677,722; PROVINCE.md:71,176,240,272,303; SCORECARD.md:2748; lessons round-17:127
  (integrator-owned), round-24:63 (operator/revenger) …                                exit 0
python3 -B verifiers/check_sibling_census.py corpus/knowledge/sibling-overlap-census-round49.md
  --province PROVINCE.md  → rows 20 verified 20 / province rows 20 matched 20          exit 0
```

No tools installed or updated (none needed). Only file written: this report. Lane checkout otherwise
untouched; no git/jj write commands anywhere; guard run is read-only (`python3 -B`).

## Residual risk / verification gaps

- `harness-integrity`, `gate-evidence`, `rlm-dispatch` (revenger `PROVINCE.md:22`) are not
  resolvable from revenger's repo (build seat's unknown 3). If some future record ties them to
  kotoba's instruments, the sentence stays a refusal, so the classification would still be `none` —
  but the LOW-1-style wording audit of the boundary note should be redone then.
- The census's Limits clause stands for `.ufo/` wave prose (not a rule-named scope surface); my
  tree-wide token sweeps found no craft claim there, but I did not read 864 files line by line.
- LOW-1 is wording-level; I did not edit anything (read-only seat). Fix belongs to the build/integration seat.
