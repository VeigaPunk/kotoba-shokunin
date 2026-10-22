# ReviewProvinceRows: round 50 falsify, PROVINCE.md f3046466..956ee16

Verdict: HOLDS-BOUNDED. Applies to the PROVINCE.md diff f30464660c675d1c1e2851a3bf0366a3aaffe5a8..956ee1676e4c18480bce8ac3993541462be76e11: Core line 17, Frontier line 23, and rows kake, kama, kasegi, kengaku, kotodama, tameshi. The guard passes, no line number in the changed lines is stale, and all nine adjacent classifications hold. Two rulings (kama, tameshi) give reasons their cited bytes do not support; the outcome holds on a different test that the row does not state. Five defects sit on changed lines (2 Medium, 3 Low), plus one pin note. No defect changes a classification or a count.

## Scope and method

- Diff: `git --no-pager diff f3046466..956ee16 -- PROVINCE.md`, exit 0, 8 insertions and 8 deletions. Changed lines in the new file: 17 (Core), 23 (Frontier), 43 kake, 44 kama, 45 kasegi, 46 kengaku, 47 kotodama, 55 tameshi.
- Judged bytes: private clone at `/fast/scratch/hyaku/kotoba-r50/falsify/ReviewProvinceRows/lane`, checked out at 956ee16 (`rev-parse HEAD` confirmed). Sibling bytes read with `git -C <repo> show <row commit>:<path>` (exit 0 for every path).
- The guard does not check boundary text (PROVINCE.md line 32 says so). Every wording finding below is a manual check.

## Guard (read-only, `python3 -B`)

- Scratch clone at 956ee16: `python3 -B verifiers/check_sibling_census.py corpus/knowledge/sibling-overlap-census-round49.md --province PROVINCE.md --skill SKILL.md` printed `rows 20 verified 20`, `province rows 20 matched 20`, `skill description names 9 of 9 non-none lanes`, `skill description length 1008 of 1024`. EXIT 0.
- Lane checkout (HEAD 956ee16): same output, EXIT 0. The working copy also has uncommitted ` M corpus/lessons/round-50.md` and untracked `.ufo/waves/round-50/falsify*` entries from other seats. Those are not judged.
- Not run: the guard at f3046466 (the "5 of 9" claim). That belongs to the C1 item.

## Findings

**M1 [Medium] kama row, line 44: "verifies endpoint values in instruction files and judges no wording" is false for the cited lines 91-92.**
- `corpus/knowledge/consumer-registry.md:91-92` at c808ba07 judges fallback behaviour in agent files. Row 2: "there is no fallback" and "the only consumer with *no* fallback". Row 3: "**cascade-protected**: the cloud tail survives the 8080 break; janitor (#2) does not" (distiller.md cascade).
- Lines 111-112 (kengaku endpoint verdicts) and 325-326 (grep results) do judge no wording. The claim holds for those two ranges only.
- The row still reads `adjacent` correctly. kama's own split (`cross-lane-scope.md:29`, quoted in the same row) assigns "model/fallback wording" to kotoba, so under the census precedence rule (census, section "Round 50: precedence", kama bullet) that split defeats any claim. The row never makes this argument.
- Fix: replace "judges no wording" with that split as the basis. The fact report RuleKama.md:15 states the same "no wording" conclusion; I disagree for rows 2 and 3.

**M2 [Medium] tameshi row, line 55: three statements the cited bytes do not support.**
- (a) "tameshi measures it read-only" (kagi `corpus/checklist-run.sh`). The ledger the row cites, `corpus/knowledge/fleet-kill-rate-ledger.md:121` at 3b20f073, lists `checklist-run | 34 | 7e5ec98b9e1d0afa | unmeasured by sweep; hermetic` under §3 "Surveyed, unmeasured". "Read-only probes" (PROVINCE.md:17) describes a method, not a measured result for that gate.
- (b) "so it is no claim on kotoba's Core". The census classification rule (census, "Classification rule", contested bullet) counts "the instruments over them" (over other lanes' SKILL.md) as part of kotoba's core. The census precedence section says the tameshi test "fires literally". The row reaches `adjacent` only through the second precedence test: tameshi's own split "every lane's gate remains its own" (PROVINCE.md:14-17), which assigns the gate to kagi. The row does not state that test. Fix the reason.
- (c) Pre-existing text on the same line: "kotoba owns the SKILL-checklist instrument (kotoba base PROVINCE.md § Adjacent; tameshi corpus fleet-kill-rate-ledger.md:125-128)". The census correction (section "Correction to § Classification rule") says kotoba's tameshi line in § Adjacent names only the sibling's ground. Ledger lines 125-128 list kotoba `verifiers/*` as "sightings and adjacent machinery, not queued", with gate-ness "U". Neither cited place states a split.

**L1 [Low] kama row, quote cut short (pre-existing text on a changed line).** The row quotes "Kotoba owns the instruction/agent surface and its model/fallback wording; kama owns independent verification" and closes the quote there. The source (`cross-lane-scope.md:29` at c808ba07) continues "of the target endpoint." The census precedence section quotes the full sentence. The cut removes the scope words that the ruling depends on. Fix: restore the full sentence.

**L2 [Low] kama row, deletion claim (pre-existing text on a changed line).** The row says "the agent files it names were deleted 2026-10-14 per kama `corpus/README.md:51-55`". That passage says three named files (`opencode.json:158`, `agents/janitor.md:21`, `the-janitor:19`) were "deleted or emptied" at the 2026-10-14 re-census. Only janitor.md is an agent file among them. distiller.md, the other agent file named in the quoted sentence, appears in neither the README nor consumer-registry.md with a deletion claim (grep for "distiller" with delet/removed/2026-10-14 at c808ba07: no matches). Fix: "deleted or emptied", name janitor.md, and drop distiller.md or cite its deletion.

**L3 [Low] basis labels are unpinned and partly stale.** The kama and tameshi rows say "basis sibling". The census gives those as the basis at f3046466 and says the round-50 description edit adds kotoba's side for chousa, kama, kotodama and tameshi (census, "Basis of each adjacent row at f3046466"). The kotodama row has no basis label. Fix: pin the labels to f3046466, or update them to the 956ee16 basis, and label kotodama.

**L4 [Low, note] line pins.** No stale line number found. Two pin styles:
- Kotoba-side lines are pinned inline: `SKILL.md:10-12` at `f3046466` (kake, kasegi rows). Base lines 10-12 name kagi, kake, kasegi, kengaku and kumitate. At 956ee16 the same clause sits at lines 10-11.
- Sibling-side lines (kama 91-92, 111-112, 325-326; kake and kasegi `:4-5`; kengaku `SKILL.md:3`; tameshi `PROVINCE.md:14-17`) carry no inline revision. They rest on the row's commit cell, and every one resolves at that commit. They pass the rule as written. Adding the revision inline would remove the doubt.

## Verified, no finding

- Core 17 and Frontier 23: the 956ee16 description (lines 10-17) names chousa, kagi, kake, kama, kasegi, kengaku, kotodama, kumitate and tameshi. Each name shares a clause with owns, own, route or NOT (verifier marker list and clause test, `verifiers/check_sibling_census.py` lines 420-460 and 502-557). The statement is lexical, as the census says. NOT is upper-case only and is a refusal marker, but every clause also carries owns or route, so the wording holds for the current bytes.
- kake row, line 43: `corpus/lessons/round-5-aggregator-mirror-pathless-cli-invocation.md:5` at e73d48bb reads "Aggregator-owned file; the owning lane corrects `SKILL.md`." The lesson is filed from kotoba's round-5 audit, so "basis both" holds.
- kasegi row, line 45: lesson line 5 at 1fafde8f has the same sentence. `git grep -ciE 'prompt[- ]injection' 1fafde8f...` exits 1, so the withdrawn clause has no source.
- kengaku row, line 46: `SKILL.md:3` at 1f3b0f1e contains "route telemetry ... absent since 2026-10-15" and "kotoba owns prompt and skill craft (kengaku keeps only measured capability effects)". `plans/round25_census.sh` has three SKILL.md references (lines 37-38, 112, 172), and all three point at the working directory's file; it also reads its own corpus files. So "reads only the SKILL.md of the lane it runs in" holds, and "no claim on kotoba's Core" follows. The round-49 provenance claim matches RuleKengaku.md:57-66.
- kotodama row, line 47: `SKILL.md:3` at 35f0d49f contains "NOT prompt/skill craft (kotoba-shokunin)". `MINT.md:20-21` contains "kotoba owns prompt/skill craft despite its name" (line break after "despite"). The 956ee16 description names kotodama at line 14.
- tameshi row, line 55: `PROVINCE.md:14-17` at 3b20f073 matches, and Core line 32 names kagi `corpus/checklist-run.sh`.
- Counts: PROVINCE rows give 9 adjacent and 11 none, matching the census.

## Verification gaps

- Not checked here: C1 at f3046466 (the "5 of 9" claim), C2 box-proof deletion, D1-D6, S024-S029, Q26 beyond the rows above, and the 1,024-character count (the guard reports 1008).
- The verifier's marker list was read from source, not run on mutants.
- The kengaku provenance claim relies on RuleKengaku.md; I did not reopen the round-49 build report.

## Tooling and commands

- Installed or updated: nothing. Used git and python3, both already present. No pacman, uv, npm or cargo use.
- Writes: scratch clone and output only under `/fast/scratch/hyaku/kotoba-r50/falsify/ReviewProvinceRows/`, plus this report. The lane was not edited.
- `git --no-pager diff f3046466..956ee16 -- PROVINCE.md` exit 0.
- `git clone -q ... lane && git checkout -q 956ee16` exit 0; `git rev-parse HEAD` prints 956ee16.
- `git -C <repo> cat-file -t <row commit>` for six sibling commits: exit 0 each.
- `git -C <repo> show <commit>:<path>` for 15 paths: exit 0 each.
- Guard in scratch clone: exit 0. Guard in lane checkout: exit 0.
- `git grep -ciE 'prompt[- ]injection' 1fafde8f...` (kasegi): exit 1.
- `git --no-optional-locks status --porcelain` (lane): exit 0; no entry names PROVINCE.md.
