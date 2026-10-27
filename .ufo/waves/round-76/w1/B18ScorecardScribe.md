# Round 76 — seat B18ScorecardScribe (scribe, report only)

Role: scribe. Task: draft the `SCORECARD.md` round-76 annotation text. Lane repo
`/home/vgpnk/Projects/shokunin/kotoba-shokunin`.
Base for every fact below: `b7f13f4b39cbd43076a85568adca763a6f674e7a` (plan commit `abd8e5c`; SCORECARD.md has
no commit between base and the wave-spec commit). Working-tree HEAD at authoring time:
`4de12b61f75c73e3675ef0e422cc2be0f7da8960`; re-checked after the L1 follow-up at HEAD
`eab64394dba08a47f6797a2e23719be14675b44b`, with `7eed80e9` (addendum 1) and `eab6439` (wave role mix)
committed on top.

## Deliverable

| Item | Value |
|---|---|
| Path | `.ufo/waves/round-76/build/scorecard-draft.md` |
| sha256 | `88833414d38cae5fd75ff33edec78d306ea5ab6ef4685e53390a5e117dedddf4` |
| Size | 13 lines; annotation body lines 8–13 (HTML comment header lines 1–6, blank 7) |
| Shape | append-only block for after `SCORECARD.md:468` (the round-75 annotation, the file's last line) |

Content, in the order the seat asked for:

1. Bold section header matching the r70–r75 convention, plus the wave shape (one v2 wave, 64 seats, two
   frozen claims on distinct owned axes).
2. **Depth row (C1, sourced, score held 9, delta 0; verdict pending the non-author closure)** — the plan's
   frozen predicate sentence verbatim (see fidelity check below), the measured `0 of 6` exit 1 →
   `6 of 6` exit 0 with `<tip>` placeholders, the six conjuncts summarized (snapshot chain, located quotes,
   act-on row, self-audit, registry `used-by` + lesson log, provenance header), the counter bound ("counts
   form, sources, tokens and pinned bytes; whether the page teaches these rules is assigned to named
   non-author attack seats and the closure"), controls C1-W1/W2/W3 and the self-test must-fail arms,
   and `<freeze-commit>`/`<counter sha256>` placeholders.
3. **Consistency row (C2, calibration sub-axis, score held 10, delta 0; verdict pending the non-author
   closure)** — the second frozen predicate verbatim, `0 of 4` exit 1 → `4 of 4` exit 0 with `<tip>`
   placeholders, R1–R4 with their durable paths (`receipts/r1-folded-render.txt`, `receipts/noharm-at-tip.txt`,
   `w2-registry-note.md`, LOG § Round 75 closing line), the content-not-presence bound with C2-W1, and the
   disclosure that D2–D4 land outside this counter's scope (D5 recorded, conditional).
4. **Lowest-axis note** — owned axes depth 9 and consistency 10; depth is the lower and C1 works it; the
   all-axes reading stays the lane's open L0 question; no advisory axis moves (coverage 8.5, operability 8.5,
   freshness 8, calibration 8.5, adjacency 8.0 held and unmoved).
5. **No-harm line** — the committed base battery numbers, then `<tip>` placeholders filled from
   `receipts/noharm-at-tip.txt`.

Placeholder inventory (filled at integration from measured bytes, deliberately not asserted now):
`<tip>` (tip revision, repeated), `<C1 tip receipt path>`, `<C2 tip receipt path>`, `<freeze-commit>`,
`<counter sha256>`, `<tip values, filled from the receipt>`.

## Evidence actually run (commands, observed, exit)

| # | Command (cwd = lane repo unless noted) | Observed | Exit |
|---|---|---|---|
| 1 | `python3 -c "…plan predicate lines vs draft substring…"` | both plan `> `-quoted predicate sentences are verbatim substrings of the draft: `VERBATIM` ×2 | 0 |
| 2 | same script, count of the four counter phrases | `description craft backed 0 of 6` ×2, `… 6 of 6` ×1, `r75 routed repairs closed 0 of 4` ×2, `… 4 of 4` ×2 | 0 |
| 3 | `cat .ufo/waves/round-76/base-battery/base-battery.txt` | corpus integrity exit 0; corpus independent exit 0; `gate registry rows conformant 60 of 60 lane verifiers; phantom 0` exit 0; `PASS alwayson observed=89 floor=89`, `PASS correction_sweep observed=25 floor=25`, `PASS scoped_rules_v32 observed=240 floor=240` exit 0; checklist `"pass": 11` exit 0; `check_spec_craft` backed best-practices/using-scripts/quickstart exit 0; `check_sibling_reread` `20 of 20` exit 0 (all at `b7f13f4b…`) | 0 |
| 4 | `git cat-file -e b7f13f4b…:{verifiers/check_desc_craft.py, verifiers/check_r75_routed_repairs.py, corpus/knowledge/description-craft-round76.md}` | all three `BASE-ABSENT` | 0 (test) / 1 (cat-file, expected) |
| 5 | `git show b7f13f4b…:SKILL.md \| wc -l` | `590` | 0 |
| 6 | `python3` + `yaml.safe_load` on `git show b7f13f4b…:SKILL.md` frontmatter | `desc_len` clip **1022**, stripped **1021** (`endswith_nl True`), first sentence **151**; `description:` key line **3**, folded block content lines **4–18** | 0 |
| 7 | `grep -n '^| depth\|^| consistency\|Round 75 axis annotation' SCORECARD.md` | depth row line 28 = 9; consistency row line 29 = 10; round-75 annotation line 468 = last line | 0 |
| 8 | `ls .ufo/waves/round-76/snapshots/` then `sha256sum -c MANIFEST.sha256` (in snapshots dir) | three pages present; `optimizing-descriptions.md: OK`, `evaluating-skills.md: OK`, `best-practices.md: OK` | 0 |
| 9 | `python3 -c "json.load(fetch-record.json)"` | 3 records, each `http_status: 200`; optimizing-descriptions `bytes 13403`, sha256 `7cc54fbb…d837` (equal to MANIFEST and to the digest B13/B04 cite) | 0 |
| 10 | `git status --porcelain` (run before the addendum commit) | only untracked wave/build/receipts/snapshots/w1 items plus then-untracked `plans/round-76-addendum-1.md`; no tracked file modified by this seat | 0 |
| 12 | `git cat-file -t 7eed80e9`; `git diff`-style `diff -u` of `git show 7eed80e9:plans/round-76-addendum-1.md` vs the working-tree copy; `git show --stat eab6439` | `7eed80e9` is a commit ("pre-data addendum fixes digest home and folded-render convention", one file, +39); the committed copy differs from the worktree only by the wave-role section that `eab6439` appended (+8 lines); HEAD = `eab6439` | 0 (diff exit 1, differences present and explained) |

Read-only source reads: `plans/round-76.md` (whole), `plans/round-76-addendum-1.md` (whole),
`corpus/lessons/round-75.md` tail, `corpus/lessons/round-75-verifier-spotcheck.md` head + §6 (R1–R4),
`SCORECARD.md` lines 1–60 and 440–468, `.ufo/waves/round-76/w1-spec.json` (seat entry),
peers' drafts `build/skill-patch.md` and `build/quotes-s213.md` (read-only cross-check).

## Cross-checks against sibling drafts (read-only, no edits)

- `build/skill-patch.md` (B13): the § Body craft row cites `S213` + the round-76 entry and carries three
  page-unique quote fragments, so the draft's conjunct (c) clause ("citing the entry and S213 with at least
  two quote fragments") is satisfiable by that row; the patch projects `SKILL.md` 590 → 595 of 600.
  The draft deliberately leaves the tip line count to the no-harm receipt instead of hard-coding 595,
  because the patch is still a draft (+/- on the freeze).
- `build/quotes-s213.md` (B04): 13 quotes, page first heading at line 5, ≤25 words, page-unique against
  `evaluating-skills.md` and `best-practices.md` — same method as the draft's conjunct (b) clause
  ("≥4 page-unique located quotes (≤25 words, after the page's first heading)").
- `plans/round-76-addendum-1.md` (read from the working tree after the first draft pass; committed as
  `7eed80e9`, with `eab6439` appending a wave-role section): withdraws conjunct
  (a)'s "digest equals the S213 row's anchor update" clause in favour of **four** digest pins, and fixes the
  render convention (clip-preserving 1022 / stripped 1021). The draft was **corrected to match**: the C1 row
  now names the four pins (MANIFEST, fetch-record, counter table, lesson `## Gate`) and says the `anchor`
  cell is not edited in place; the render clause names the clip convention and prints both variants; R1's
  receipt clause now requires both variants printed. Digest equality across MANIFEST / fetch-record / B13 /
  B04 / the actual page files verified by command 9 (+ `sha256sum -c` in command 8).

## Findings and open points for integration

- **F1 — base-red values are quoted contract text, not observed output.** Both counters are absent from
  `b7f13f4` (command 4) and from the worktree (command 11). The draft's `0 of 6` / `0 of 4` sentences are the
  frozen predicate text from `plans/round-76.md:24` and `:40`; nobody has run either counter at base yet.
  Whoever lands the counters must run `--rev b7f13f4b39cbd43076a85568adca763a6f674e7a`, receipt the red,
  and only then may the `<tip>` placeholders be filled. The draft claims no run.
- **F2 — addendum 1 now committed; draft already aligned.** The C1 row cites
  `plans/round-76-addendum-1.md` at commit `7eed80e9` ("pre-data addendum fixes digest home and
  folded-render convention"), which withdraws conjunct (a)'s "digest equals the S213 row's anchor update"
  clause in favour of **four** digest pins and fixes the render convention (clip-preserving 1022 /
  stripped 1021). `eab6439` ("record validated wave role mix") appended a wave-role section to the same
  file; `git show 7eed80e9:plans/round-76-addendum-1.md` differs from the working-tree copy only by that
  appended section, so the substantive text the draft was aligned to is byte-stable. The draft's C1 row
  names the four pins (MANIFEST, fetch-record, counter table, lesson `## Gate`), says the `anchor` cell is
  not edited in place, names the clip convention with both variants, and R1's receipt clause requires both
  variants printed. Nothing remains to unblock on this pointer.
- **F3 — "annotation + planned" in the touch list has no second half to draft.** No `Next: round 76` line
  exists, and no per-round planned row was added for rounds 73–75 (`grep -n 'Next: round'` stops at round 67;
  the `## planned` narrative rows are per-round "completed" text). Nothing was drafted for `## planned`.
  If the L1 expects a planned narrative line for round 76, that is a separate fragment.
- **F4 — axis-table `Last change` cells untouched.** This seat drafted the annotation only; depth (line 28)
  and consistency (line 29) still name rounds 60 and 54. A closure that wants the evidence cell updated edits
  it as its own append-consistent change.
- **F5 — round-75 annotation is stale by closure outcome, append-only.** `SCORECARD.md:468` still reads
  "closure verdict pending"; the r75 closure has since recorded admission. The draft does not rewrite it
  (append-only); if a correction is wanted it must be an appended erratum line, not an edit.
- **F6 — the 1,022/151 numbers are the reference render, not the w1 tip.** Both were recomputed here
  (command 6) on base bytes: clip 1022 / stripped 1021 / first sentence 151, block content lines 4–18. The
  draft labels them "r75-tip reference render … which C2-R1 pins" and defers the w1 value to conjunct (d)'s
  recomputation, so a description edit at integration cannot silently falsify the SCORECARD row.
- **F7 — snapshot chain partially in place.** The three page files, `MANIFEST.sha256` and
  `fetch-record.json` exist and verify (commands 8–9); the fourth pin (lesson `## Gate` access record) and
  the counter's in-file digest table do not exist yet. The draft states the four-pin requirement, not that it
  holds.
- **F8 — no-harm tip values unmeasured.** The post-state clause is a placeholder by construction; the base
  values it quotes are the committed base battery's own lines (command 3), including `SKILL.md` 590 of 600.

## Out of scope / not done

- Did not edit `SCORECARD.md`, `LOG.md`, any lesson, any counter, `corpus/`, or any product file. No
  execution of either frozen counter (they do not exist yet), no claim data written, no freeze declared.
- No git/jj mutation anywhere (read-only `log/show/status/cat-file/rev-parse` only). No `pacman`. No
  subagents, no background jobs, no installs — nothing to record under the install mandate.
- Scratch `/fast/scratch/hyaku/kotoba-r76/B18ScorecardScribe` used only for one `git show` dump of
  `SKILL.md`; removed before yield (`rm -rf`, exit 0; directory absent on re-check).

VERDICT: DRAFTED-PENDING-MEASUREMENT — `.ufo/waves/round-76/build/scorecard-draft.md` (sha256
`88833414d38cae5fd75ff33edec78d306ea5ab6ef4685e53390a5e117dedddf4`) carries both frozen predicate sentences
verbatim (2/2), the base→tip rows with `<tip>` placeholders, scores held at depth 9 and consistency 10
pending the non-author closure, the lowest-axis note, and the addendum-1 corrections (four digest pins, no
S213 anchor edit; clip 1022 / stripped 1021 convention) with the addendum cited at committed `7eed80e9`;
no tip value, counter run, or score move is asserted anywhere in it.
