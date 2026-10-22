# D5Rows — routed defect D5 (rows): kama quote + citation, kengaku `README.md:192` premise

Seat: KotobaR51.D5Rows (scribe, round 51 build, 2026-10-22). Read-only on the lane; edits are in the
private clone `/fast/scratch/hyaku/kotoba-r51/build/D5Rows/lane` at base `43ca0bfb74372f2a67a48e0aeb2e35d0d98b1d10`.

**HOLDS-BOUNDED.** Both D5 sub-defects are real and are fixed in a patch. The kengaku row's class and the
counts do not move; the kama row's classification, commit and basis do not move. `PROVINCE.md` boundary text
is unchecked by the guard, so the fix is bounded to two `PROVINCE.md:44` spans plus one appended census section.

## Behaviour

**(1) `PROVINCE.md:44` — cut kama quote + deletion citation.** The row quoted kama's split as `"Kotoba
owns the instruction/agent surface and its model/fallback wording; kama owns independent verification"`
and closed the quotation there. The source at kama `corpus/knowledge/cross-lane-scope.md:29` (`c808ba07`,
quoted in Evidence) continues `of the target endpoint.` — the row cut a sentence with no ellipsis and
dropped the scope words the ruling rests on. The census already quotes the full sentence at
`sibling-overlap-census-round49.md:268-269`; the province row did not. Corrected quote (full sentence,
verbatim, `**` emphasis as in the source): "**Kotoba** owns the instruction/agent surface and its
model/fallback wording; **kama** owns independent verification of the target endpoint"

The deletion citation was the second defect. The row said "the agent files it names were deleted
2026-10-14 per kama `corpus/README.md:51-55`". That passage names **only** `janitor.md` of the two agent
files the split names (`janitor.md`, `distiller.md`), and says the pins were "deleted or emptied" **as of
the 2026-10-14 re-census** — a re-census date, not a deletion day. No line in kama's tree names the
deletion of both agent files in full, so the row now uses bounded wording over the three passages that
carry each half: kama `corpus/knowledge/consumer-registry.md:56-57` (the whole `~/.config/opencode/agents/`
directory, hence both agent files); kama `corpus/knowledge/cross-lane-scope.md:57,59` (round-10 corrections
A26/A27 record both files **absent by shape check only**); and kama `corpus/README.md:51-55` retained but
scoped — it names only `janitor.md`, dated to the re-census.

**(2) Census line 273 — kengaku `README.md:192`.** The ruling said kengaku's `corpus/README.md:192` "says
only 'frontmatter triggers'". It does not. At `1f3b0f1e` that line is one row of the `plans/` table and
reads: `plans/round25_census.sh` | Round-25 counting script (SOURCES census, new rows, mistakes rows,
SHONEN form, frontmatter triggers, both instruments' summaries) — **six** outputs; "frontmatter triggers"
is the fifth. The script's own header (`plans/round25_census.sh:11-27`) documents 14 keys, and a run at the
pin prints all 14 (exit 0): it counts a lane root's SOURCES registry, lesson rows, SHONEN evidence boxes
and two instrument summaries — not a lane's `SKILL.md` frontmatter alone. The sibling's "reads only the
`SKILL.md` of the lane it runs in" premise was already withdrawn by the round-50 falsify-wave correction;
this entry withdraws the misreading of the sibling's own description.

**Adjacency / calibration.** The D5 spot-check's kengaku pointer (`README.md:192`) does not resolve at the pin
(kengaku's top-level `README.md` is 14 lines there); the census's own `corpus/README.md:192` resolves, so the
defect is the "says only" characterization, not the path — the appended paragraph says so rather than
"correcting" a path that was right. `PROVINCE.md:44` and the census were the only surfaces carrying either
defect.

**No row moves.** kengaku stays `adjacent`, basis both: its "no claim" rests on the scope-surface rule (the
script's cross-lane runs are recorded only in kengaku's wave reports, which § Classification rule excludes).
Counts stay 9 adjacent, 11 none, 0 contested; the kama row keeps `adjacent` at `c808ba07…`.

## Gates (scratch clone, base `43ca0bfb`)

| check | base | after | exit |
|---|---|---|---|
| `check_sibling_census.py <census> --province PROVINCE.md` | rows 20 verified 20 / province rows 20 matched 20 | same | 0 |
| `check_sibling_census.py --self-test` | 0 failure(s) over 68 assertions | same | 0 |
| `verify_corpus_integrity.py --json` | 5/9 pass, DRIFT 4 | **JSON byte-identical to base** | 1 (pre-existing) |
| `git apply --check patch.diff` | — | applies cleanly to base | 0 |

The corpus-integrity DRIFT (`corpus.index.tracked_files` 70→69, `corpus.index.unindexed` 1,
`corpus.pointers.report_total` 45→44, `corpus.pointers.report_dead` 2) is **pre-existing at base** and
byte-identical before and after (the two `--json` outputs diff empty) — the unindexed file is
`corpus/lessons/round-50-verifier-spotcheck.md`, not mine. `check_sibling_census.py` is the only verifier
that reads `PROVINCE.md`; it checks lane set, classification and commit, not boundary text.

## Touched surfaces

- `PROVINCE.md:44` (kama row): quote restored to the full sentence; deletion citation replaced with the
  bounded wording and the two passages carrying each half. The cell stays 4 pipe-separated cells.
- `corpus/knowledge/sibling-overlap-census-round49.md`: one appended section `## Round 51: corrections to the
  round-50 rulings (append-only)` with two bullets (kengaku premise, kama quote). Append-only; no line above
  the append was edited; no pipe-leading line added, so the guard's parser still selects the same 9-column
  census table and 4-column province table.

Patch: `/fast/scratch/hyaku/kotoba-r51/build/D5Rows/patch.diff` (2 files, +45/-1, against `43ca0bfb`).
The lane checkout was not written to; the patch was verified with `git apply --check` in a throwaway clone.

**Integration order (collision with seat `D6Provisional`).** Both seats append a round-51 section at the
census file's end (`@@ -368,3 +368,NN @@` off the same base tail), so only one can land first: D6-then-D5
fails with `patch failed: corpus/knowledge/sibling-overlap-census-round49.md:368` (verified, exit 1). Land
D5 first, then D6 from its `patch-after-D5.diff`; verified end to end (guard exit 0, self-test exit 0,
corpus-integrity JSON identical to base). A single merged diff is also at
`patch-combined-D5-then-D6.diff` (2 files, +90/-1), verified to apply cleanly to base with guard exit 0;
it is the same tree as the two-step route. `PROVINCE.md` does not collide — my hunk is the kama row
(line 44), D6's is the § Adjacent intro pointer (line 35).

## Out of scope

- **D6** (precedence rule's provisional status) and the L0 question it routes — seat `D6Provisional`. I did
  not extend or rely on the rule; the appended text rests the kengaku outcome on the scope-surface rule.
- The `SKILL.md:12` clause "kama owns endpoint verification" — a paraphrase, not a quote; already recorded in
  round 50 (`ReviewDescTriggerChecklist.md:72`).
- Round-49 census line 183 "agent files kama deleted on 2026-10-14" — a round-49 record, outside this round's
  scope; the appended paragraph records the same date-vs-re-census distinction.

## Evidence (commands with output excerpts)

```
$ git -C .../kama-shokunin show c808ba07...:corpus/knowledge/cross-lane-scope.md | nl -ba | sed -n '57p;59p'
    57  *[correction (A26): ... => absent ~/.config/opencode/agents/janitor.md — shape-only, no body read) ...]
    59  *[correction (A27): ... => absent ~/.config/opencode/agents/distiller.md — shape-only, no body read) ...]
$ git -C .../kama-shokunin show c808ba07...:corpus/README.md | nl -ba | sed -n '51,55p'
    51  - **Operator-dependent (historical):** the stale pins in `~/.config/opencode/opencode.json:158`,
    52    `~/.config/opencode/agents/janitor.md:21`, and `~/.local/bin/the-janitor:19` were ...
    53    *detected and reported*, never rewritten by kama (operator-owned files). As of the 2026-10-14 re-census
    54    all three files are deleted or emptied — see `knowledge/consumer-registry.md` §Errata; the drift
    55    resolved by deletion, not repoint.
$ git -C .../kama-shokunin show c808ba07...:corpus/knowledge/consumer-registry.md | nl -ba | sed -n '56,57p'
    56  - **Most consumer files are gone.** Deleted since round 2:
    57    `~/.config/opencode/agents/`, `~/.config/opencode/opencode.json.*.bak*`, ...
$ git -C .../kengaku-shokunin show 1f3b0f1e...:corpus/README.md | nl -ba | sed -n '192p'
   192  | `plans/round25_census.sh` | Round-25 counting script (SOURCES census, new rows, mistakes rows, SHONEN form, frontmatter triggers, both instruments' summaries) |
$ git -C .../kengaku-shokunin show 1f3b0f1e...:README.md | wc -l
    14
$ git -C .../kengaku-shokunin show 1f3b0f1e...:README.md | sed -n '192p'
    (empty — no line 192 at the top level)
$ cd /fast/scratch/.../D5Rows/kengaku && sh plans/round25_census.sh    # checkout at 1f3b0f1e
head=1f3b0f1
sources_rows=76
sources_malformed=0
sources_tier_histogram=A=70 B=4 C=2
sources_status_histogram=mined=64 queued=8 rejected=4
sources_new_rows_r25=16
knowledge_files=37
lesson_mistake_rows_r25=8
shonen_evidence_lines_per_box=1,1,1,1
skill_frontmatter_triggers=6
calib_summary=TOTAL files=9 scored_files=5 ... PASS=7 FAIL=0 ... ; calib_exit=0
state_check_summary=assertions=329 match=318 mismatch=0 ... ; state_check_exit=0
=== exit 0 ===   (14 keys printed)
$ cd /fast/scratch/.../D5Rows/lane && python3 -B verifiers/check_sibling_census.py corpus/knowledge/sibling-overlap-census-round49.md --province PROVINCE.md
rows 20 verified 20
province rows 20 matched 20
=== exit 0 ===
$ python3 -B verifiers/check_sibling_census.py --self-test
self-test: 0 failure(s) over 68 assertions
=== exit 0 ===
$ diff <(cd basecheck && python3 -B verifiers/verify_corpus_integrity.py --json) <(cd lane && python3 -B verifiers/verify_corpus_integrity.py --json)
(no output — JSON identical to base; the 4 DRIFT lines are pre-existing)
=== exit 0 ===
$ git -C applytest apply --check /fast/scratch/.../D5Rows/patch.diff
PATCH APPLIES CLEANLY
=== exit 0 ===
```

Tools installed or upgraded: none (python3 and git present; no pacman transaction — all pacman transactions are
paused host-wide). Unrun: nothing in scope; sibling text was read at the pinned commits only.

Report: `.ufo/waves/round-51/build/D5Rows.md`
