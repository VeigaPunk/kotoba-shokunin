# R03RevR1Text — R1 correction draft review

Reviewed `.ufo/waves/round-76/build/B08-r1-round-75-correction.diff` and `B08-notes.md` against the round-75 lesson, spot-check §6 R1, round-76 C2 R1 definition and addendum 1 render convention. No counter, receipt, or corpus data was changed.

## Verdict

The correction draft is substantively accurate and append-only; it explicitly identifies both superseded passages and withdraws the false classification. It meets the spot-check's request to name superseded text, correct the whole folded scalar measurement, cite the spot-check, and re-derive the plan assertion. No replacement text is needed.

Evidence:

- The diff adds one hunk after the existing lesson rows (`@@ -10,3 +10,25 @@`) and has no removed lines. Its four-space-indented M75-1 quotation preserves it as historical text rather than reintroducing it as a live Markdown table row.
- The opening identifies M75-1 at `corpus/lessons/round-75.md:11` and the Gate reject candidate at `:5`, quotes their material assertions, says the reject is withdrawn, and withdraws M75-1's `stale-premise` classification. This satisfies §6 R1's requirement to name the superseded text.
- The source M75-1 row's raw window lengths `14,76,78,73,79,72` and its `1,021/1,024` assertion are accurately quoted. The correction distinguishes raw line lengths from a YAML folded-scalar render and states the clip-preserving convention pinned by `plans/round-76-addendum-1.md`.
- Independent command: `cd /home/vgpnk/Projects/shokunin/kotoba-shokunin && git show ac9f29510d3914a6edb97c8dbdb3445cab9141de:SKILL.md | python3 -c 'import sys,yaml; d=yaml.safe_load(sys.stdin.read().split("---")[1])["description"]; print(len(d),len(d.strip()),len(d.strip().split(". ")[0]+"."))'` → `1022 1021 151` (exit 0). Thus its stated r75-tip measurement is correct.
- Spot-check §6 R1 also requires re-deriving any plan/claim that consumed the assertion. The draft points to `plans/round-75.md:15`, withdraws that base note, and explains that r75 C1 was the unrelated equality-threshold claim at `SKILL.md:193`; it does not silently leave the premise in force.
- The CORPUS contract file named `CORPUS.md` is absent at this lane path (directory listing shows `corpus/README.md`, not a root `CORPUS.md`). The draft does not rewrite prior rows: it adds a separately headed correction and quotes the prior row as indented historical material, consistent with the stated corrections-as-new-entries convention. B08 notes report clean dry-runs and append-only checks, but those are not independently relied on here.

Residual risk / verification gap: this is a review of the draft, not confirmation that it was applied or that the required R1 receipt recomputes the render at its measured revision. The report also does not independently verify the corpus convention's exact wording because the referenced `CORPUS.md` is not present in the lane tree.

VERDICT: Accept the R1 correction draft as accurate and append-only; no corrected replacement text needed.
DELIVERABLES: /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-77/w1/R03RevR1Text.md; /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-77/build/R03RevR1Text.md