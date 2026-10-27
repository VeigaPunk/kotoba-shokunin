# SKILL.md patch draft — round 76 (B13SkillPatch)

Status: **draft, not applied.** The L1 integrates after the freeze; this file carries the exact
insert text and its anchors, so the patch is a copy-paste, not a re-derivation.

- Repo: `/home/vgpnk/Projects/shokunin/kotoba-shokunin`, base `b7f13f4b39cbd43076a85568adca763a6f674e7a`, `SKILL.md` **590 lines** (budget box `trigger.line_budget`, threshold 600, § Trigger-fidelity checklist base line 285).
- Net delta: **+3 lines → 593** (1 rule row, 2 registry rows). Margin to the 600 box: **7 lines**.
- Revised at 14:0x after B15Simplifier's D1–D2: the preamble edit is **dropped** (the frozen touch list names the § Body craft *row* and the § Gate registry *rows*, and `SKILL.md` § Compression rules already requires one authoritative home per fact — C1 conjunct (c) forces the entry path into the row's source cell, so the preamble gains nothing a reader cannot get there and from the gate-registry row), and the rule row is shortened to house length. All three quote fragments are kept.
- Sources: plan `plans/round-76.md` C1 conjunct (c) and the Gate-registry row format; entry `corpus/knowledge/description-craft-round76.md` (B04/B12); snapshot `.ufo/waves/round-76/snapshots/optimizing-descriptions.md` (B03).
- Fragment source, confirmed: HTTP 200, 13,403 bytes, sha256 `7cc54fbb6abbcf08c33e7b320fd01a1fb9696426270da3b588a398d243bfd837` — the same digest as `snapshots/MANIFEST.sha256` and the `fetch-record.json` record; my own fetch of the URL is byte-identical. Baselines: `evaluating-skills.md` `a799805f…fb684`, `best-practices.md` `ab9f3b60…fb41`.
- Post-patch anchors (base + these two pins, `wc -l` = 593): rule row line **217**; registry rows lines **514–515**; `## Gate registry` stays line 448; the budget box moves from base 285 to patched **286** with its text unchanged.
- Budget: `build/budget.txt` (B02) was still absent, so the anchors are computed directly (`wc -l SKILL.md` = 590, `+3`).

## Pin 1 — § Body craft rule row (insert after base line 216, the `confirm discovery before trusting a path` row; before the blank line 217 that ends the table)

```text
| write the description as an imperative about the goal, not the mechanics, and err pushy | S213 optimizing-descriptions; `corpus/knowledge/description-craft-round76.md` | "Err on the side of being pushy": list the contexts the skill serves, including ones the user never names; "descriptions tend to grow during optimization", so re-check length after each edit; "Avoid adding specific keywords from failed queries" — name the category instead. |
```

Row shape: 3 cells (`|` x4), **447 characters / 65 words** (B15Simplifier's own replacement draft measured
443/65): the row keeps the six existing § Body craft rows' dense one-line form and adds no padding, while
carrying all three page rules and all three quote fragments.

Row checks (all three fragments verbatim in the optimizing-descriptions page, each absent from the
evaluating-skills and best-practices pages — `grep -c -F` gave `1 / 0 / 0` for each):

| fragment (words) | page line | page-unique |
|---|---|---|
| `Err on the side of being pushy` (7) | 27 | yes |
| `descriptions tend to grow during optimization` (6) | 159 | yes |
| `Avoid adding specific keywords from failed queries` (8) | 157 | yes |

Fragment 1 sits inside `**bold**` markers in the page (`**Err on the side of being pushy.**`) and
fragments 2–3 are mid-line after a bullet: they are located by a word-bounded **substring** match (as
`check_spec_craft.py` does); a whole-line equality match will not find them. The fragments are 6–8
words, so the row also clears a ≥5-word token rule, with one fragment spare over C1's ≥2.

The source cell carries both `S213` and `corpus/knowledge/description-craft-round76.md`, so C1
conjunct (c) is satisfied by the row alone; the preamble stays byte-identical to base.

## Pin 2 — § Gate registry rows (append after base line 512, the `check_sibling_reread.py` row; before the blank line 513 and `## Sources` at 514)

```text
| `verifiers/check_desc_craft.py` | gate | `python3 -B verifiers/check_desc_craft.py --rev <rev>` | 0=clean, 1=failed, 2=could-not-evaluate — round-76 C1 counter (depth): committed bytes only; the entry `corpus/knowledge/description-craft-round76.md` carries ≥4 located quotes (≤25 words) that occur verbatim in the sha256-pinned optimizing-descriptions snapshot after its first heading and are page-unique against the evaluating-skills and best-practices snapshots, every digest appears in `snapshots/MANIFEST.sha256`, in `snapshots/fetch-record.json` (HTTP 200) and in the in-file digest table, row S213's `used-by` lists the entry, `SKILL.md` § Body craft carries a row citing the entry and S213 with ≥2 quote fragments, the entry's audit table equals the counter's recomputation from the measured `SKILL.md`, and the entry opens with `source:`/`verified-at:`/`recheck:`; `description craft backed 6 of 6` at the measured rev and `0 of 6` at the pinned base | `--self-test` | in-file SELF_SHA and the three page digests; `.ufo/waves/round-76/snapshots/MANIFEST.sha256` | none (read-only); `--self-test` fixture repos under `$TMPDIR` (removed) | kotoba |
| `verifiers/check_r75_routed_repairs.py` | gate | `python3 -B verifiers/check_r75_routed_repairs.py --rev <rev>` | 0=clean, 1=failed, 2=could-not-evaluate — round-76 C2 counter (consistency): the four round-75 routed defects close on committed content — R1's appended correction in `corpus/lessons/round-75.md` plus `receipts/r1-folded-render.txt` printing 1022 recomputed from the measured `SKILL.md`; R2's tip-named `receipts/noharm-at-tip.txt` carrying green integrity/independent stdout and exit codes, cited from LOG § Round 75; R3's `w2-registry-note.md` reconciling the R75Attack28 phantom with a machine-checkable excerpt, cited from LOG § Round 75; R4's appended LOG § Round 75 closing line after the pending text; `r75 routed repairs closed 4 of 4` at the measured rev and `0 of 4` at the pinned base | `--self-test` | in-file | none (read-only); `--self-test` fixture repos under `$TMPDIR` (removed) | kotoba |
```

Both rows use the registry's eight columns in file order (`Name | Kind | Entry command | Verdict map |
Self-test | Pinned values | Write scope | Owner`), backticked verifier path first, em dash before the
round label, the frozen verdict line in the verdict cell, `kotoba` owner — the shape of every row from
`check_report_pointers.py` (round 73) through `check_sibling_reread.py` (round 74).

## Trigger-fidelity checklist — no box text changes

This patch touches only `§ Compression rules › ### Body craft` (one table row) and `§ Gate registry`
(two table rows). It adds **no checklist box, rewording or reordering**: all 19 boxes in
`## Trigger-fidelity checklist` keep their exact text, so `verifiers/checklist-baseline.json`'s box-text
hashes and `verify_skill_checklist.py`'s executed set are untouched. The line-budget box (`File ≤ 600
lines`) is satisfied at 593 and its text is unchanged.

## Scope notes for the integrator

- Out of this seat: the entry `corpus/knowledge/description-craft-round76.md` (B04/B12), the two
  counters (B06/B07), `verifiers/floors-registry.json` + `check_assertion_floors.py` in-file tables
  (+2 rows, another seat), `corpus/SOURCES.md` S213 `used-by` (B14), lesson/LOG/SCORECARD rows
  (B08/B17–B19). `check_assertion_floors.py` fails until its registry rows are added in step, as the
  plan's touch list states.
- Preamble deliberately untouched: a second naming of the entry path there would duplicate the row's
  source cell (one authoritative home per fact) and is outside the frozen touch list.
