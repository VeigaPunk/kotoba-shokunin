# Round 75 wave 2 — R75Attack20: falsify `w1/R75Facet20.md` (description-audit calibration)

## Target

`R75Facet20.md` on the kotoba lane. Its central factual claim (the "candidate claim" it proposes):
**at `ec2c1d3`, the parsed folded frontmatter description of `SKILL.md` is 1,021 characters (under its
1,024 cap) and names the ten lanes classified non-`none` in the corresponding adjacency census.** The
facet cites `SKILL.md:3-18`, `:23-46`, `corpus/knowledge/skill-eval-artefacts-round70.md:19-21,32-34,
47-72,74-80`, and `corpus/lessons/round-74-verifier-spotcheck.md:75-78`, and proposes the concrete
check: parse frontmatter at the stated commit, compare extracted lane names exactly against the
committed census classifications at the same revision.

## Attack performed (independent re-derivation, not re-read)

- Re-parsed folded frontmatter myself at `ec2c1d3`, `65a5c7a`, and the dirty worktree with two methods:
  `yaml.safe_load` of the `---`-delimited block, and a parser-free byte fold (strip the 2-space indent
  on lines 4-18, join with single spaces). Both give **exactly 1,021 characters**, byte-for-byte equal
  values, no internal/trailing newlines, no trailing whitespace on any line (an earlier shell-pipeline
  count of 1,025 was a quoting artifact, superseded by this reconciliation).
- Re-derived the census classification at `ec2c1d3` from the committed blob
  (`git ls-tree ec2c1d3` → `sibling-overlap-census-round74.md` present, blob `6c8d65b5`): table rows
  53-72 give 10 `adjacent` (chousa, kagi, kake, kama, kasegi, kengaku, kotodama, kumitate, tameshi,
  tsukuroi) and 10 `none` (audio, game-dev-2d, game-dev-3d, kaidoku, lore, mado, mori, revenger, souji,
  tabi). Word-boundary extraction over the parsed description yields **exactly** that adjacent set —
  all ten named, zero `none` lanes named.
- Cap grounding: 1,024 is not a bare assertion — spec row S018 (`corpus/SOURCES.md:14`, description
  1-1024), four vendor docs (`corpus/knowledge/skill-listing-thresholds-round54.md:42-46`), and the
  lane's own guard `verifiers/check_sibling_census.py:418` (`SKILL_DESCRIPTION_MAX = 1024`, G4).
- Revision staleness attack: `git diff ec2c1d3 65a5c7a -- SKILL.md` is **empty** and both blobs hash
  to `57f0ad70…`; the dirty worktree edits only a body line (~`SKILL.md:190`), leaving frontmatter
  identical. The facet's flagged risk ("historical at `ec2c1d3`, not evidence of the current r75 tip")
  is moot for this claim — it holds at tip.
- Citation fidelity: `SKILL.md:3-18` is exactly the folded `description` block (closing `---` at :19);
  `loader contract` at `:23`, `historical path` at `:40` inside cited `:32-46`; spotcheck description
  row at `:76` (facet cited `:75-78`, the row plus its two neighbours — accurate);
  `skill-eval-artefacts-round70.md:20` (`should_trigger`), `:33-34` (F7/F8 `>`/`>=` rows), `:47-72`
  (author guidance + the equality-disagreement section), `:74-80` (Scope and refusals, "No claim is
  made" at `:76`) — all verified at worktree; the dirty diff on that file is +3 tail lines (:86-88)
  only, so the citations are revision-stable.
- Provenance check: `round-74-verifier-spotcheck.md` is committed at `65a5c7a` (blob `9f3e7b33`) but
  **absent at `ec2c1d3`** — consistent with the facet's wording "records an observed … parse at
  revision `ec2c1d3`" (a later record about that revision, not an artifact of it).

## Novel counterevidence surfaced by this attack

`corpus/lessons/round-75.md` (untracked, in-flight) contains a Mistakes row asserting the
considerthese 1,021/1,024 figure is stale-premise because "current committed SKILL frontmatter (master
65a5c7a, lines 3–18) is substantially shorter." **This is false by direct measurement.** The lesson's
own quoted awk (`NR>=3&&NR<=8` → 14,76,78,73,79,72) is correct but covers 6 of the 15 folded lines —
~392 of 1,021 chars — and lines 9-18 continue at 67-77 chars each before the `---` at :19. The
committed frontmatter is byte-identical at `ec2c1d3` and `65a5c7a`; `considerthese/2026-10-26.md:17`'s
"still 1,021 of 1,024" is **correct at tip, not stale**. Consequence for the target: the facet's
numbers are current, and any future attack on the facet that leans on the round-75 lesson would be
built on a broken measurement.

## Verdict

**Survived.** The facet's central claim is exactly true — 1,021 parsed characters at `ec2c1d3` (and
unchanged through `65a5c7a`), under the grounded 1,024 cap, naming precisely the ten non-`none` lanes
of the same-revision census. Its line citations are accurate; its scope (structural description, no
routing-effectiveness claim) is honestly bounded; its proposed check is non-vacuous — I executed it and
it discriminates. Not a duplicate: no other evidence artifact performs the frontmatter-vs-census
cross-check the facet proposes. Attack result is strengthened, not weakened: new evidence (the empty
`ec2c1d3..65a5c7a` SKILL.md diff) retires the facet's own flagged staleness risk.

## Residual risk / verification gaps

- I did not execute `verifiers/check_sibling_census.py` (safe but unnecessary — its G4/G9 logic covers
  the same length/name ground I re-derived; the facet proposed a fresh parse, not the lane's counter).
- No live client or router experiment performed (the facet performed none and explicitly disclaims
  one); the "1 client observable" render claims remain unmeasured, correctly outside the claim.
- Census classes were re-derived from rendered table rows at `ec2c1d3`, corroborated by the census's
  own class-count line (`:26-27`, "10 adjacent, 10 none, 0 contested").
- The round-75 lesson's false stale-premise row is a lane-internal error outside this facet's scope;
  noted here only as attack product.

Report: `.ufo/waves/round-75/w2/R75Attack20.md` (relative to
`/home/vgpnk/Projects/shokunin/kotoba-shokunin`). No lane source edited, no commits, no scratch used,
no live fetch.
