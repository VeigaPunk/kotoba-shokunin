DIFFERS FROM r49: tsukuroi (r49 `none` -> proposed `adjacent`, kotoba-side corpus split). tameshi unchanged (`adjacent`).

# ScoutSibTameshiTsukuroiR74 — C2 re-read of tameshi and tsukuroi

Verdict: tameshi `adjacent` (r49 stands, pin moves 3b20f073 -> a944eb55). tsukuroi `adjacent` (r49 `none`
at 22fd1642 -> 8bd001f5), decided by a split kotoba's own corpus states, not by any new tsukuroi byte.
Only committed blobs at the freeze heads were read (`git show/grep/diff` against `<head40>`); working trees untouched.
JSON saved at `.ufo/waves/round-74/w1/build/ScoutSibTameshiTsukuroiR74/{tameshi,tsukuroi}.json` (extra keys `decided_by`; `changed` is a string starting yes/no).
Head pins confirmed against the freeze file: `git -C <lane>-shokunin rev-parse <head>:SKILL.md <head>:PROVINCE.md` printed
tameshi 0b44815c… / 6154fe44… and tsukuroi 4ae3ccf4… / 9ca7994e…, equal to the TSV columns 4-5.
Unobserved: working trees, other branches, sibling wave reports (excluded by the rule), whether the checker accepts `decided_by` as an extra key.

## tameshi (head a944eb55d64a2e0a77e3561c44bf89faadf04bb9)

```json
{"lane":"tameshi","head40":"a944eb55d64a2e0a77e3561c44bf89faadf04bb9","r49_classification":"adjacent","r49_pin":"3b20f073c7305a582562cd323982991464c324f3",
 "proposed_classification":"adjacent",
 "decided_by":"rule clause 2 (stated split). Deciding sibling sentence (tameshi corpus/knowledge/fleet-kill-rate-ledger.md:127-128): \"kotoba `verifiers/*` — file existence is O, their gate-ness is U until a survey admits them\"; corroborated by PROVINCE.md:14-15 \"every lane's gate remains its own\" (names no lane) and kotoba's own description SKILL.md:14 \"tameshi owns the fixture and mutation method\". No contested claim.",
 "changed":"no — r49 pin is an ancestor of head; numstat SKILL.md +95/-43, PROVINCE.md +13/-0; PROVINCE.md:1-20 and the frontmatter description are byte-equal to the pin; new bytes are the round-26 nine-legs append (PROVINCE.md:106-118) and SKILL.md registry text, none states a kotoba split or claim.",
 "skill_file":"SKILL.md",
 "quote":"Verification-fixture craft for 'hermetic suites', 'mutation testing', and 'gate fixtures'.","quote_path_line":"SKILL.md:3",
 "kotoba_mentions":[],
 "boundary":"tameshi owns the reusable fixture and mutation method while each lane's gate stays its own (PROVINCE.md:14-15); kotoba's `verifiers/*` are unsurveyed sightings there (fleet-kill-rate-ledger.md:127) and kotoba's description cedes the method."}
```

Honest weakness: at the head, tameshi's `SKILL.md` and `PROVINCE.md` never name kotoba (below). The sibling-side basis is
one corpus-file ledger line plus a lane-agnostic refusal; the kotoba-naming half of the split is kotoba's own description
(`SKILL.md:14` at base `1e03d19`) and `PROVINCE.md:70`. That is the same footing as r50's "basis sibling" ruling, which cited
`PROVINCE.md:14-17` that also names no lane. A reviewer who requires the sibling's own bytes to name kotoba would call this `none`; I did not.

## tsukuroi (head 8bd001f58bfda29c92d90d2a7a413825c0ca9fcb)

```json
{"lane":"tsukuroi","head40":"8bd001f58bfda29c92d90d2a7a413825c0ca9fcb","r49_classification":"none","r49_pin":"22fd1642e7fa4dfbdfba4419a443f06ffbb0b6c0",
 "proposed_classification":"adjacent",
 "decided_by":"rule clause 2 (either side's scope surfaces incl. corpus files state a split). Deciding sentence is kotoba-side (kotoba corpus/knowledge/hook-files-round59.md:19-20 at 1e03d19): \"Host package and initramfs hooks are tsukuroi's\"; sibling side of the same artifact class (tsukuroi PROVINCE.md:22): \"Inspect effective mkinitcpio drop-ins, hooks and recovery stages; never rebuild or boot.\" r50 precedence: a split stated only by kotoba may make a no-claim row adjacent. No contested claim.",
 "changed":"yes — r49 none rested on tsukuroi's own surfaces at 22fd1642; kotoba's corpus entry hook-files-round59.md (round 59, after the r49 pin) states a hook-file split with tsukuroi. tsukuroi's head bytes add no kotoba mention (0 whole-word hits in SKILL.md/PROVINCE.md at pin and head). If kotoba-side-only corpus splits are excluded, none stands.",
 "skill_file":"SKILL.md",
 "quote":"Domain specialist — host operability & system repair.","quote_path_line":"SKILL.md:3",
 "kotoba_mentions":[],
 "boundary":"tsukuroi owns host package and initramfs hooks and OS state as read-only probes (PROVINCE.md:22); kotoba routes only client hook-config files and cedes host hooks (hook-files-round59.md:20), a split stated on kotoba's side alone."}
```

Flag for the L1: kotoba's own base `PROVINCE.md:71` says tsukuroi `none` "no split with kotoba on its scope surfaces", while kotoba's
`hook-files-round59.md:19-20` (a corpus file, hence a scope surface under the rule) states the split; `corpus/lessons/round-59-verifier-spotcheck.md:156`
records `ConnSiblingHooks.md` "FITS (tsukuroi host hooks kept apart)" and left adjacency "unchanged". The two kotoba surfaces disagree.

## Sweeps (commands and observed output)

Whole-word `kotoba` over the committed bytes at the heads:

- `git -C tameshi-shokunin grep -n -w -i kotoba a944eb55… -- SKILL.md PROVINCE.md` -> no output, exit 1. Per file: `show <head>:SKILL.md | grep -c -w -i kotoba` 0 (2136 lines); PROVINCE.md 0 (118 lines); corpus/README.md 0 (579 lines). Same three counts at the r49 pin: exit 1.
- `git -C tameshi-shokunin grep -n -w -i kotoba a944eb55… -- . ':!LOG.md' ':!.ufo'` -> 4 hits, all corpus: `corpus/knowledge/fleet-kill-rate-ledger.md:127` ("kotoba `verifiers/*` — file existence"), `:233` ("sightings (kake, kama, kotoba) have unresolved gate-ness"), `corpus/knowledge/fleet-suite-census.md:625` (same sentence as :127), `corpus/lessons/round-33.md:90` ("three sibling adjacency imports catalogued (mado/kotoba/kake waves)"). Kinds: citation, none a claim on kotoba ground.
- `git -C tsukuroi-shokunin grep -n -w -i kotoba 8bd001f5… -- SKILL.md PROVINCE.md` -> no output, exit 1 (SKILL.md 3112 lines 0; PROVINCE.md 197 lines 0; corpus/README.md 282 lines 0). At pin 22fd1642: exit 1.
- `git -C tsukuroi-shokunin grep -n -w -i kotoba 8bd001f5… -- . ':!LOG.md' ':!.ufo'` -> 3 hits, all corpus: `adjacency-anchors-r19.json:570` (`"sibling": "kotoba"`), `adjacency-anchors-r19.md:116` (IN-021, a kotoba wave report at `.ufo/round-22/scouts/A6.md:47` cited as an inbound pointer), `executor-test-sufficiency.md:187` ("kotoba tail notes"). Kinds: citation; the IN-021 report is a wave report, which the rule excludes.
- Substring (non-word) `grep -n -i kotoba <head> -- SKILL.md PROVINCE.md` printed nothing for both lanes, so no `kotobaXYZ` form hides a mention.

Claim sweeps over head SKILL.md/PROVINCE.md (`git grep -n -i -E "prompt[- ]?(craft|engineer|text)|skill craft|AGENTS\.md|description (craft|wording)|trigger[- ](fidelity|string)|frontmatter|other lanes' SKILL|sibling'?s? SKILL"`):

- tameshi: 1 hit, `SKILL.md:1738`, a rejected-edit note about its own frontmatter quoting (own file). Another sweep (`SKILL\.md checklist|checklist-run|…|prompt|AGENTS\.md|instruction file|trigger`) hit only `PROVINCE.md:32` and SKILL.md ledger rows for kagi's `corpus/checklist-run.sh` (already ruled in r50 as kagi's instrument, kill rate measured read-only). No new contested element.
- tsukuroi: 4 hits, `SKILL.md:169,182,183,449`, all citations of its own lane's `AGENTS.md`/`SHONEN.md`. `check-seat-bindings.py` has `LANE = '/home/vgpnk/Projects/shokunin/tsukuroi-shokunin'` (blob line ~14) and `corpus/README.md:206` says it judges "recorded request spellings against predispatch prompt declarations": own-lane seat prompts, not other lanes' prompts, so no contested element.

Diffs from the r49 pins (`merge-base --is-ancestor` printed `ancestor-yes` for both):

- `git -C tameshi-shokunin diff --numstat 3b20f073… a944eb55… -- SKILL.md PROVINCE.md` -> `13 0 PROVINCE.md`, `95 43 SKILL.md`; `--shortstat` -> `2 files changed, 108 insertions(+), 43 deletions(-)`. `diff <(show pin:PROVINCE.md | sed -n 1,20p) <(show head:PROVINCE.md | sed -n 1,20p)` -> `same-1-20`. Description line 3 at pin and head identical.
- `git -C tsukuroi-shokunin diff --numstat 22fd1642… 8bd001f5… -- SKILL.md PROVINCE.md` -> `45 0 PROVINCE.md`, `827 0 SKILL.md` (shortstat, from the first sweep: `2 files changed, 872 insertions(+)`). Added PROVINCE headings: round-26 storage-integrity frontier, `Adjacent — mori userspace OOM killers (round 27)`, `Adjacent — ADJ-04 handoff lines (round 32)`, `Adjacent — ADJ-04 per-class boundary note (round 33)`; all mori-side. Description line 3 identical at pin and head.

Kotoba side (base `1e03d1991bc02281b00a5b7a5e00c9d5d5d72908`):

- `git show 1e03d19:SKILL.md | sed -n 1,20p | grep -c -i tsukuroi` -> 0; same file lines 11-14 name tameshi ("tameshi owns the fixture and mutation method", `SKILL.md:14`).
- `git grep -l -i tsukuroi 1e03d19 -- corpus` -> `hook-files-round59.md`, `sibling-overlap-census-round49.md`, `lessons/round-49-verifier-spotcheck.md`, `lessons/round-50.md`, `lessons/round-59-verifier-spotcheck.md`. Only `hook-files-round59.md:20` states a split ("Host package and initramfs hooks are tsukuroi's", blob `63e8ab85…`).
- Mechanical cells (for the row, recomputed from head description): tameshi names kotoba `no`, arbitration `yes: kama` ("route those to the product lane or kama", `SKILL.md:3`); tsukuroi names kotoba `no`, arbitration `no`.

Quote checks: `git show <head>:SKILL.md | sed -n '3p'` printed, for tameshi, `description: "Verification-fixture craft for 'hermetic suites', 'mutation testing', and 'gate fixtures'. Anti-trigger: … Rank: shonen."` (quote is the first sentence, 10 words, rest dropped) and for tsukuroi `description: Domain specialist — host operability & system repair. Rank: shonen (probation).` (quote 8 words, `description: ` prefix and trailing `Rank…` dropped). Both JSON quotes were asserted as substrings of the whitespace-collapsed line by script; boundary sentences 29 and 32 words.
Tooling: none installed. Scratch: none left (script was in /tmp, deleted).
