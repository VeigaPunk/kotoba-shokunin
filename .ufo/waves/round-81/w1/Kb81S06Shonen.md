# Kb81S06Shonen — SHONEN box-state check (round 81, w1)

Seat: Kb81S06Shonen (leaf; no subagent dispatch, no background jobs beyond own tool calls). Item: re-derive each
of the four SHONEN promotion boxes at base `b284223105f4d106f7e8f56ed4fd296c643cda0e` with live commands,
publish per-box `[~]`/`[ ]` state with a resolvable pointer at `{{TIP}}`, and name any drift between box text and
observed state.

## Behavior

Read `/home/vgpnk/Projects/shokunin/kotoba-shokunin/SHONEN.md` (sha256
`c42f6bff13563f39bcec3d255b78cb23fbded6bf0446e082179768725838dee8`), then re-ran, from the lane root, each
`Report:`/evidence command the boxes name plus the gates they rely on:

- box 1: SKILL.md identity (sha256 `ec92e5d9…`, 596 lines), § Sources recount (18), decision-table rows
  (`corpus/knowledge/anatomy-and-compression.md:102-108`, 5 data rows) and the pointer sweep
  (`grep -n 'Decision-table shape' SKILL.md` → `195:`), anatomy rows (`:130-136`, 7), checklist count per section
  (45 = 19/9/9/8), `verify_skill_checklist.py` (exit 0, 12 PASS), `check_gate_registry.py --rev` at base and at
  the box's cited rev `80bb8921`.
- box 2: `LOG.md:287,294,342` at base and at `078eec4`, cold-run record presence and author marker,
  `verify_corpus_integrity.py` at base, and the report-pointer sites it names (round-76/round-77).
- box 3: each line pin in `corpus/lessons/round-8-aggregator-box3-coldrun.md` (`:36`, `:37`, `:78`, `:100`), the
  quotation host line (`:102`), and the `corpus/knowledge/` cold-run filename sweep.
- box 4: `PROVINCE.md` § Adjacent heading/sentence re-grep, the box's round-49 census guard **with and without**
  `--skill SKILL.md`, the round-74 census guard, and `check_sibling_reread.py --rev b2842231…`.

All verdicts are the command's own exit status (`cmd > f 2>&1; rc=$?`), per M80-1; no verdict comes from a
pipeline. No lane file was edited; no scratch clone or fixture was needed, so no scratch dir was created and
none has to be removed.

## Box states (base `b2842231`)

| Box | State | Evidence (resolvable at `{{TIP}}`) |
|---|---|---|
| 1 — SKILL.md: decision tables, error patterns, checklists, cited sources | `[~]` | `git show {{TIP}}:SKILL.md \| grep -n 'Decision-table shape'` (195 at base); Sources recount 18; 45 boxes (19/9/9/8); `python3 -B verifiers/check_gate_registry.py --rev {{TIP}}` must print `… conformant N of N …; phantom 0`, exit 0 (63 at base, 64 once C2's counter lands); `verify_skill_checklist.py` exit 0 |
| 2 — end-to-end domain task executed and logged in LOG.md | `[~]` | `git show {{TIP}}:LOG.md \| grep -n 'cold-run-round11'` (287/294/342; identical at `078eec4`); `git show {{TIP}}:corpus/knowledge/cold-run-round11.md \| sed -n '1,6p'` (NON-AUTHOR marker), `:172` (`**none found**`) |
| 3 — instructions executable without oral context | `[~]` | `git show {{TIP}}:corpus/lessons/round-8-aggregator-box3-coldrun.md \| sed -n '36p;37p;78p'`; quotation at `:102`; `git ls-tree -r --name-only {{TIP}} corpus/knowledge/ \| grep -ci cold-run` → 1 |
| 4 — no cross-domain bleed (PROVINCE.md accurate) | `[~]` | `python3 -B verifiers/check_sibling_census.py corpus/knowledge/sibling-overlap-census-round74.md --province PROVINCE.md --skill SKILL.md` → `province rows 20 matched 20`, `names 10 of 10 non-none lanes`, exit 0; `check_sibling_reread.py --rev {{TIP}}` → `20 of 20`, exit 0 |

**4 of 4 boxes read `[~]`; 0 `[x]`; 0 `[ ]`** (`grep -n '^- \[' SHONEN.md` → lines 5,7,9,11; `grep -c '\[x\]'`
→ 0). Promotion is not claimed and this seat changes no verdict.

## Gates run (exact commands, direct exit capture)

| Command | Exit | Observed tail |
|---|---|---|
| `awk '/^## Sources/{p=1;next} /^## /{p=0} p && /^- /' SKILL.md \| wc -l` | 0 | `18` |
| `python3 -B verifiers/check_gate_registry.py --rev b2842231…` | 0 | `gate registry rows conformant 63 of 63 lane verifiers; phantom 0` |
| `python3 -B verifiers/check_gate_registry.py --rev 80bb8921…` | 0 | `gate registry rows conformant 42 of 42 lane verifiers; phantom 0` (the box's figure reproduces) |
| `python3 -B verifiers/verify_skill_checklist.py` | 0 | 12 PASS / 0 FAIL; `evaluated 45 — 45 boxes mapped (8 executed, 4 delegated, 33 unexecuted)`; `evaluated 596 — 596 lines within budget 600`; `212 repo-rooted citation token(s) resolve` |
| `python3 -B verifiers/verify_corpus_integrity.py` | 1 | `4/9 checks pass`; DRIFTs `tracked_files 155≠154`, `unindexed 1`, `report_total 111≠109`, `report_dead 1`, `commit_unresolvable 2` |
| `python3 -B verifiers/check_sibling_census.py corpus/knowledge/sibling-overlap-census-round49.md --province PROVINCE.md` | 1 | `rows 20 verified 20` / `province rows 20 matched 4`; 16 FAILs |
| `… round49.md --province PROVINCE.md --skill SKILL.md` (seat form) | 1 | same `matched 4`; `skill description names 9 of 9 non-none lanes` |
| `python3 -B verifiers/check_sibling_census.py corpus/knowledge/sibling-overlap-census-round74.md --province PROVINCE.md --skill SKILL.md` | 0 | `province rows 20 matched 20`; `names 10 of 10`; `length 1021 of 1024` |
| `python3 -B verifiers/check_sibling_reread.py --rev b2842231…` | 0 | `sibling rows re-pinned, re-located and re-diffed at the frozen fleet heads 20 of 20`; freeze sha256 `6e6012fc…` |

`git cat-file -e 078eec4^{commit}` → 0; `git show 078eec4:LOG.md | sed -n '287p;294p;342p'` → the same three
cold-run citations. `test -e verifiers/check_sdk_allowed_tools.py` → 1 (C2's counter does not exist at base).

## Findings (drift between box text and observed state)

Numbered R81-S06-F1…F10, each with the command that produced it, in
`.ufo/waves/round-81/build/Kb81S06Shonen.md` § Drift register. Summary:

- **F1** decision-table pointer `SKILL.md:241` → **`:195`** (persists; was 192 at r80 base).
- **F2** box inventory 41 (15/9/9/8) → **45 (19/9/9/8)** (persists).
- **F3** the box's `42 of 42` reproduces at its own rev, but base is now **63 of 63, exit 0** — r80's “60 of 62,
  two missing rows” and the checklist red arm are both gone; post-C2 the figure is **64 of 64**.
- **F4 (new)** `SKILL.md` sits at **596/600** lines and the frontmatter description at **1021/1024** chars: C2's
  SDK-channel sentence + registry row leave 2 lines and 3 chars of headroom.
- **F5** box-2's verifier is red at base (`4/9`, five DRIFT classes); the DEFENSIBLE sentence is “on record and
  logged, verifier red at base, C1 is the repair.”
- **F6 (new)** `report_dead 1` moved to `corpus/lessons/round-77-verifier-spotcheck.md:15`: the lane lacks
  `HEAD:.ufo/reports/round-77/kotoba.md` (`cat-file -e` exit 128) while the fleet carries it (8547 B, fleet
  `cat-file -e` exit 0) — C1 R1's lane-then-fleet order has a real target.
- **F7** box-3 citation `:100` is the heading; the quotation is at **`:102`** (persists).
- **F8 (load-bearing)** box-4's guard pairs the round-49 census with the round-74-pinned `PROVINCE.md`: exit 1,
  `matched 4`, 16 FAILs; with `--skill` a second red arm (`9 of 9`) appears; round-74 census or the re-pin gate is
  green (exit 0).
- **F9** “9 adjacent lanes” → **10 of 10**, at 1021/1024 chars.
- **F10** `PROVINCE.md` pins `35:`/`37:` → **`:42`** / **`:44`**; § Frontier precedes § Adjacent, so the heading
  moves with any § Frontier append.

## Touched surfaces

Wrote only, inside the lane's round-81 wave dir:
`.ufo/waves/round-81/build/Kb81S06Shonen.md` (box-state document) and the eight receipts
`.ufo/waves/round-81/build/Kb81S06Shonen-receipt-{gateregistry-base,gateregistry-80bb8921,skillchk-lane,integrity-base,census49-province,census49-province-skill,census74-province-skill,siblingreread-base}.txt`.
No lane file (SHONEN.md, SKILL.md, PROVINCE.md, LOG.md, corpus/, verifiers/, plans/) was edited; no git/jj
mutation anywhere; no tool was installed or upgraded this seat.

## Out of scope / not measured

- No after-value for C1 or C2, and no scoring of any claim; the C2 counter is absent at base and the tip battery
  was not run (heavy ~105 s pass; `disk-guard.sh status` showed `/fast/scratch/hyaku` at 27 % used / 592.2 G free,
  so no pass was needed by this seat). The base tip-battery receipt belongs to the L1.
- The round-64 `STRICT_HITS 0` claim is reported as history, not re-derived: no live gate re-runs it; the
  artifacts are `.ufo/waves/round-64/w1/ScoutSiblingOverlap.md:77` and `.ufo/waves/round-64/w2/ScoutW2SiblingVerify.md:7`
  (the latter agrees on STRICT_HITS 0 and separately qualifies ConnSibling's literal `M95` control).
- The S230/S231 external-commit binding is the plan's C1 R1/R2 work; this seat only records that
  `commit_unresolvable 2` still sits at `corpus/SOURCES.md:171`, `:172`.

VERDICT: All four SHONEN boxes remain `[~]` at base b2842231 (0 `[x]`, 0 `[ ]`); box 1 and box 3 have no red live gate (gate registry 63 of 63, checklist exit 0), box 2's record stands but its verifier is red at base for the C1 repair set, and box 4 is substantively accurate (round-74 census + re-pin both exit 0) while its own evidence command is red by construction — 10 named box-text drifts, headline being `SKILL.md:241`→`:195`, `PROVINCE.md:35/37`→`:42/44`, 41→45 boxes, 9→10 adjacent lanes, and the new 596/600-line + 1021/1024-char headroom that C2 must not trip.
DELIVERABLES: /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-81/w1/Kb81S06Shonen.md, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-81/build/Kb81S06Shonen.md, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-81/build/Kb81S06Shonen-receipt-gateregistry-base.txt, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-81/build/Kb81S06Shonen-receipt-gateregistry-80bb8921.txt, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-81/build/Kb81S06Shonen-receipt-skillchk-lane.txt, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-81/build/Kb81S06Shonen-receipt-integrity-base.txt, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-81/build/Kb81S06Shonen-receipt-census49-province.txt, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-81/build/Kb81S06Shonen-receipt-census49-province-skill.txt, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-81/build/Kb81S06Shonen-receipt-census74-province-skill.txt, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-81/build/Kb81S06Shonen-receipt-siblingreread-base.txt
