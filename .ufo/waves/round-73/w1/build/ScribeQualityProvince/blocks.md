# Round 73 — append-only blocks (ScribeQualityProvince)

Draft only. The L1 lands these; this file never edits the lane. Anchors are given by the text they
follow, with the line number observed at `ac8fc59` (wave-1 spec v3) in parentheses — re-anchor by text
after any landing ahead of it.

Placeholder convention (per the seat ticket): every count the claim has not yet measured is `<<N>>`,
every registry id is `<<S-ids>>`, every mistake id the round's lesson assigns is `<<M-id>>`.
Nothing here asserts a value that wave 1 has not produced.

---

## Block 1 — `PROVINCE.md` § Core bullet

**Anchor:** append as the last line of `## Core`, i.e. after the round-72 bullet
(`- Author-facing rules, host substrate and tip battery (round 72): …`, line 30) and immediately
before `## Frontier` (line 31). One bullet, one line, no blank line inserted.

```markdown
- Chinese-vendor skill surfaces, own description and the tip battery (round 73): four Chinese vendors' documented skill surfaces — TRAE (ByteDance), CodeBuddy IDE and CLI (Tencent), Kimi Code CLI (Moonshot) and Zhipu managed agents — with each vendor's discovery roots, body placement and frontmatter vocabulary, renumbered by document from the read-only staged package (S<<S-ids>>) — `corpus/knowledge/chinese-vendor-skill-surfaces-round73.md`, counted by `verifiers/check_cn_vendor_surfaces.py --rev <rev>` (`vendor skill surfaces backed <<N>> of 4`; `held at base: 0`); this file's own frontmatter `description` read against the lane's own trigger rule (`corpus/knowledge/frontmatter-trigger-surface.md:116-120`, `:68`) — first sentence 40–99 characters with a quoted trigger inside the first 99 — counted by `verifiers/check_own_description.py --rev <rev>` (`own-description rules held <<N>> of 3`; `<<N>> of 3` at base `072048f`; plan addendum 1, considerthese item 5); and the six-gate tip battery counted by `verifiers/check_tip_battery.py --rev <rev>` (`tip battery exit 0: <<N>> of 6`; `2 of 6` at base), its sandbox environment reconciled with the hand run (M127, `corpus/lessons/round-72.md:85-87`). The Chinese-vendor rows are documentary: no client was run.
```

Notes for the L1:

- The round-72 bullet already names `check_tip_battery.py`; this bullet names the same counter for a
  different claim (the `2 of 6` reading is the C3 surface). Do not delete the round-72 clause.
- `verifiers/check_province_core.py` compares only `## Frontier` and `## Adjacent` against its base, so
  appending this bullet cannot move that gate; do **not** touch either section in the same edit.
- The `<<S-ids>>` must be the lane's renumbered ids, never the staged ids: staged `S214`, `S216`–`S219`,
  `S221` collide with the lane's r72 rows `S214`–`S216` (plan § Before-values, id-collision row).
- If the pre-data Q45 census lowers C1's target below 4, the bullet's `<<N>>` is the measured count and
  the claim's target becomes the lowered number as the committed addendum states; the printed line stays
  `backed N of 4` (the population is four vendors — only the target moves). This is the last moment the
  plan allows that lowering.
- `verifiers/check_province_core.py` does **not** score this bullet: its `AREAS` tuple is frozen to
  rounds 67 and 68 (`verifiers/check_province_core.py:45-50`). It cannot be cited as evidence that the
  round-73 bullet is present; what it does constrain is the byte-identity of `## Frontier` and
  `## Adjacent`.

## Block 2a — `corpus/README.md` Coverage-map row

**Anchor:** append as the last row of the Coverage-map table, after the `Round-72 lessons` row
(line 140), before the blank line 141.

```markdown
| Chinese-vendor skill surfaces (round 73) | `knowledge/chinese-vendor-skill-surfaces-round73.md` | four Chinese vendors' documented skill surfaces — TRAE (ByteDance), CodeBuddy IDE and CLI (Tencent), Kimi Code CLI (Moonshot) and Zhipu managed agents — each with its discovery roots, where the skill body is placed and its frontmatter vocabulary, renumbered by document from the read-only staged entry (S<<S-ids>>); every cited page re-opened this round with a located quote and a snapshot pinned by `snapshots/MANIFEST.sha256`; counted by `verifiers/check_cn_vendor_surfaces.py --rev <rev>` (`vendor skill surfaces backed <<N>> of 4`, `0 of 4` at base `072048f`) |
```

## Block 2b — `corpus/README.md` index row for the round's lesson

**Anchor:** immediately after Block 2a.

```markdown
| Round-73 lessons | `lessons/round-73.md` | `## Gate` the S<<S-ids>> rows with this round's located quotes and snapshots, the id-collision result (lane `<<N>>` ids, package `<<N>>`, `<<N>>` collisions renumbered by document), the pre-data vendor census (`<<N>>` of 4 reachable) and the refused staged claims with their flips; `## Mistakes` M<<M-ids>> (a report's pointers resolved at the revision it cites, an append placed inside a prose note, a counter that disagreed with the hand run); `## Falsify corrections` <<N>> items, wave 2 <<state>> |
```

Note for the L1: the closure spot-check row (`| Round-73 non-author spot-check (closure) | … |`) is the
closure's own row and is **not** drafted here — history shows it lands unindexed and is indexed by the
next round (rounds 66–71 all did), so do not pre-empt it.

## Block 2c — `corpus/README.md` § Frontier note

**Anchor:** append at the end of the Frontier section's append-only notes, after the Round-60 note
(line 219), before the blank line 220 and `## Known gaps` (line 221).

```markdown
**Round 73 (append-only note; new area *Chinese-vendor skill surfaces*):** the Chinese-vendor channel of
the round-1 question — whether clients outside the held set expose an Agent Skills surface — moves to Core
in part: four vendors' documented discovery roots, body placement and frontmatter vocabulary are held in
`knowledge/chinese-vendor-skill-surfaces-round73.md` (S<<S-ids>>, renumbered by document from the staged
package) and counted by `../verifiers/check_cn_vendor_surfaces.py --rev <rev>` (`vendor skill surfaces
backed <<N>> of 4`). This is documentary evidence: no client was run, no version string is pinned, and a
page's own precedence statement is recorded as the page states it. Still not held: any measured client
behaviour; client versions (no binary or release pin exists for any of the four); CodeBuddy surfaces
beyond the two pages read here (its plugin, command, agent-definition and hook folders); and a Japanese
*client* tier — the Japanese material this corpus holds is documentation and practice, and no Japanese
client is recorded as documenting a skill surface.
```

Note for the L1: the note answers the "what stays unheld" half of the plan's C1 frontier statement and
must not repeat the C1 counts as held ground; if the pre-data census lowers the target, `<<N>>` is the
measured count and the target clause cites the addendum that lowered it. The printed population stays
four (`backed N of 4`); only the exit target moves.

---

## Block 3 — `corpus/QUALITY.md` rows Q66–Q68

**Anchor:** append after Q65 (line 81, the file's last row). Row form follows Q58–Q65 (five columns,
single line per row, `supersedes` = `—` where the row extends rather than replaces).

Mistake ids: this draft assumes the round's lesson numbers them `M128`, `M129`, `M130` — the next free
ids after M127. **Substitute the ids `corpus/lessons/round-73.md` § Mistakes actually assigns before
landing**; a QUALITY row grounded in an id the lesson does not carry is the M3 class.

```markdown
| Q66 | A report's artifact pointers are resolved against the lane tree at the revision the report cites, not against the worktree it was written in: every backticked `receipts/…`, `.ufo/waves/…`, `corpus/…` and `verifiers/…` token names a path that exists at that revision, and the resolving gate is shown red on the previous round's report at the previous round's tip before it is run on the current report; a pointer repaired after filing is an appended line naming the committed file, never a rewrite of the filed report. A pointer that names a file existing in no revision is invisible to Q04 (it resolves source/recheck commands), Q49 (seat `Report:` paths) and Q60 (its `git cat-file -e <rev>:<path>` form needs a revision, which a report's bare relative name does not carry). | round reports and `SHONEN.md` pointer tokens | M128 `report-pointer-drift` (`corpus/lessons/round-73.md` § Mistakes; the r72 report cited `receipts/tip-check_tip_battery.txt` at `../.ufo/reports/round-72/kotoba.md:70` and `receipts/tip-check_substrate_repin_v2.txt` at `:103`, while the committed files are `tip-tip_battery.txt`, `tip-tip_battery-run2.txt` and `tip-substrate_repin_v2.txt`; routed at `corpus/lessons/round-72-verifier-spotcheck.md:31-34`); checked by `verifiers/check_report_pointers.py --rev <rev>` | — |
| Q67 | An append into a file that carries free prose lands at a section boundary — after the last line of the target section and before the next `## ` heading — and the gate that guards the file checks the section order and the anchor lines on both sides of the append, not only that the appended text is present; a file a previous append split mid-sentence is repaired by an appended correction entry, and the structure check is shown red on the split revision before it is claimed green on the repaired one. Placement is what neither the append-only gate (Q34: protected cells unchanged) nor `../scripts/sources-census.sh validate` (row grammar; exit 0 on the split file) reads. | `corpus/SOURCES.md` and any ledger carrying free-prose notes | M129 `append-inside-prose-note` (`corpus/lessons/round-73.md` § Mistakes; at `072048f` the r72 entry sits inside the round-64 placement correction — `corpus/SOURCES.md:207-215`: a line holding one backtick at 207, the r72 entry at 212, and a line led by `` ## Leads (unopened)` `` at 214 that splits the old note mid-sentence; routed at `corpus/lessons/round-72-verifier-spotcheck.md:35-43`; `../scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kotoba` → exit 0 on those bytes, 2026-10-25) | — |
| Q68 | When a counter's gate result disagrees with the same gate run by hand in an environment the counter claims to reproduce, the disagreement is explained at the identity of the code path that selects the environment (file:line) before the counter's number is used as claim evidence; the repair is shown red-before on the old invocation and green after on the same command, and while the disagreement is unexplained the counter's figure is reported as `cause unresolved`, never as the claim's measurement. Q63 fixes the environment of a counter item's first run but does not require the counter's built environment to be reconciled with a hand run, and Q50/Q36 stay satisfied while the two numbers disagree. | counters that build their own sandbox or environment | M127 `environment-variance` (`corpus/lessons/round-72.md:85-87`; explained at round 73 by `verifiers/check_tip_battery.py:610`, `fleet = Path(args.fleet) if args.fleet else repo.parent`, which resolves to the lane itself under the documented `--repo .`; receipt `.ufo/waves/round-73/receipts/m127-l1-repro.txt`) | — |
```

Landing conditions for Block 3:

- **Q66's check clause lands only with the gate it names.** `verifiers/check_report_pointers.py` does
  not exist at `ac8fc59` (`ls verifiers/check_report_pointers.py` → no such file). If the L1 lands the
  row without the gate, delete `; checked by …` — a row naming a nonexistent check is the Q04 class.
  The row's own red-before requirement: the gate exits 1 on `.ufo/reports/round-72/kotoba.md` at the
  r72 tip (`e8207c6`), naming the two `tip-check_*` tokens, before it exits 0 on the round-73 report.
- **Q67 cites the damaged bytes, not a rewrite of them.** `corpus/SOURCES.md:207-215` is the routed
  defect the round repairs by an appended correction entry; the row must not be read as licence to
  rewrite the filed note.
- **Q68 does not restate M127's evidence as a solved mystery.** The class is `environment-variance`;
  the explanation landed at round 73 and the row's grounding names the line, not the receipt alone.

## Landing order (one integration owner)

1. `corpus/knowledge/chinese-vendor-skill-surfaces-round73.md` + its snapshots and
   `snapshots/MANIFEST.sha256` must land **before** Block 2a: `verify_corpus_integrity.py` reports an
   unindexed file red, and a README row pointing at an absent file is a dead pointer.
2. `corpus/lessons/round-73.md` must land **before** Block 3 (ids) and Block 2b (Gate/Mistakes cells).
3. Block 1 last: it names the entry, the counter and (via `check_province_core.py`'s docstring conjunct) a
   tree whose `## Frontier` and `## Adjacent` are still byte-identical to that gate's base. Note that
   gate scores only rounds 67/68 — it is a no-harm guard here, not a witness for this bullet.

## What this draft does not claim

- No value: every count is `<<N>>`; wave 1 has measured none of C1/C2/C3's post-data numbers.
- No new ground: the four vendors' rows are documentary and the lane ran no client, pinned no version.
- No sibling claim: the Frontier note says nothing about which other lane owns Chinese-client craft.
