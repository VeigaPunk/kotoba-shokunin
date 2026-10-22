# ReviewSkillTriggerCraft — C1 pre-landing review (round 50 build, 2026-10-22)

FAILS today on exactly one checklist box — trigger.05 (description names 5 of the 9 census-adjacent
lanes; chousa, kama, kotodama, tameshi missing) — which is precisely C1's gap; the other 14 boxes pass
(13 clean, trigger.13 carrying an adjacent staleness note), all 8 executed checks are green in the lane
(`exit_code: 0`), and the instrument/prose split plus the rewrite contract are below. One plan defect:
the stated content-guard command is not reproducible at the pin (`--skill` unrecognized, exit 2) —
that arm must be built, not merely run.

Reviewed: `SKILL.md` at `f30464660c675d1c1e2851a3bf0366a3aaffe5a8`. Lane HEAD equals the pin and
`git diff f304646… -- SKILL.md` is empty (0 bytes), so working-tree reads are pin reads. Frontmatter is
lines 1–16 (16 lines); description folds to 814 chars; the only sibling names present are kagi, kake,
kasegi, kengaku, kumitate.

## Box-by-box: trigger-fidelity checklist vs today's description

| box | binding | today | evidence |
|---|---|---|---|
| 01 frontmatter parses | executed | PASS | instrument: `name='kotoba-shokunin', description 814 chars`; 814 ≤ 1024 portability floor |
| 02 name==directory | executed | PASS (layout-bound) | green only where the dir is `kotoba-shokunin`; a clone dir named `lane` FAILs (observed) |
| 03 literal trigger | executed | PASS | literal `Triggers:` + 8 quoted spans; shape test only (instrument says so itself) |
| 04 anti-trigger | executed | PASS | `Anti-triggers` unquoted (the check strips quoted spans *before* matching, ANTI_TRIGGER_RE) |
| 05 sibling arbitration | **unexecuted (prose)** | **FAIL as adjacency** | names 5 of 9 census-adjacent lanes; rule present and concrete for the named five; baseline disposition: "semantic judgements … human-graded" |
| 06 role statement | prose | PASS | H1 + loader-contract line; no trigger restatement |
| 07 prerequisites fail-closed | prose | PASS (scope) | frontmatter carries no procedures/`metadata.requires`; partially covered by box 09's check |
| 08 decision-table action cell | prose | PASS (scope) | no table in frontmatter; body tables carry verdict/action cells or are documentation by the rule's own carve-out |
| 09 command binary resolves | executed | PASS | 13 subjects over 9 segments resolve; description carries no commands |
| 10 failure-claim signature | prose | PASS w/ note | "never reach the omp skills router" is a mechanism claim whose signatures live in body-cited knowledge files — deliberate compression |
| 11 citation resolves | executed | PASS | 46 tokens resolve; description's only backtick token `` `*-shokunin` `` is a glob, not repo-rooted, not evaluated |
| 12 derivation second witness | prose | PASS (n/a here) | frontmatter carries no instrument claims; census is the adjacency derivation |
| 13 stale-risk pinned | prose | PASS w/ note | "the **five** `*-shokunin` domain skills" is an unpinned fleet-count fact (fleet: 20 lanes, 9 adjacent); C1's rewrite replaces it — do not leave any bare count stale |
| 14 file ≤ 600 lines | executed | PASS | 537 ≤ 600, threshold read from the box at line 252 |
| 15 no placeholder | executed | PASS | 493 scanned lines, no markers |

## trigger.* checks: instrument vs lane-attested prose

Executed by `verify_skill_checklist.py` (run 2026-10-22, lane root, `python3 -B … --json` →
`exit_code 0`, pass 11 / fail 0): `trigger.frontmatter_parses`, `trigger.name_directory`,
`trigger.literal_trigger_string`, `trigger.anti_trigger_clause`, `trigger.line_budget`,
`trigger.no_placeholder`, `trigger.command_binary_resolves`, `trigger.citation_resolves` — 8 box-bound
— plus `trigger.no_xml_tag` (executes over unparsed name/description text, bound to no box since
round 47). The 11th check is `governance.citation_resolves` (LOG.md/SCORECARD.md, not SKILL.md).
Lane-attested prose (baseline `unexecuted:`): trigger.05, .06, .07, .08, .10, .12, .13 — seven boxes,
including **the C1 box trigger.05**. Its only machine teeth would come from the census guard's
description arm, which does not exist at the pin (F1).

## Rewrite contract: adding chousa, kama, kotodama, tameshi with splits

Must keep (else an executed check or the prose bar breaks):
- The literal `Triggers:` and the quoted trigger spans (box 03); at least one exclusion marker word
  **outside quotes** — the check strips all quoted spans first, so an anti-trigger only inside quotes
  fails unearned (box 04). Keep the three semantic exclusions (general prompt engineering, runtime
  code, skill `reference/` content) — instrument cannot attest them, prose must.
- A concrete per-sibling arbitration rule (box 05's bar: bare names don't count). Published splits to
  draw on: chousa — kotoba cites, never re-derives, the research method; kama — kotoba owns
  instruction/agent-surface wording, kama owns independent verification; kotodama — it refuses
  prompt/skill craft by naming kotoba (name collision, kotodama MINT.md:20), kotoba must name it back
  (census finding 2: today non-reciprocal); tameshi — fixture method is tameshi's, the SKILL-checklist
  instrument is kotoba's. Splits must not contradict the D3 precedence ruling (kengaku, kama, tameshi
  contested elements are recorded, unruled at the pin).
- The omp-not-router-visible note (it is what keeps the router claims honest; census confirms no lane
  SKILL.md in any discovery root).
- YAML folded block scalar (`description: >`), two-space continuation, no blank line introduced.

Must not break (numbers):
- ≤1024 chars: 814 now; +4 names ≈ +33 → ~847; **~175 chars left** for four arbitration-grade splits —
  the published split sentences do not fit verbatim; compressed rules are required. Dropping the
  router note or anti-triggers to make room is a content decision that must be recorded, not silent.
- No `<`/`>` anywhere in name/description (`trigger.no_xml_tag`, incl. YAML `\x3c`-style escapes);
  the counter's `→` arrows are safe, ASCII `<`/`>` are not.
- No backticked repo-rooted path in the description — `trigger.citation_resolves` executes file-wide;
  a `corpus/knowledge/sibling-overlap-census-round49.md` pointer would add a resolution obligation and
  a round-indexed staleness trap. Keep the description citation-free.
- Whole-token matching: the counter greps `-oiwE` and the guard re-derives `token_in` per lane;
  "kama" is not a substring of "kotodama", so no accidental satisfaction — each of the 9 must appear
  as its own token.
- Line budget: file 537/600; the rewrite adds ~5–9 frontmatter lines — safe margin, but do not rewrap
  the body.
- Do not touch the checklist section: box text is hash-pinned in `checklist-baseline.json` (41 boxes);
  rewording any box FAILs by design. The frontmatter is not a box, so the description edit alone
  cannot trip the baseline.
- Only committed reader of kotoba's own description is `verify_skill_checklist.py` (swept
  `verifiers/` for `kotoba|description_of|SELF_LANE`): `check_sibling_census.py` reads sibling SKILL.mds
  and kotoba's PROVINCE.md, never kotoba's SKILL.md; the harness baseline has no kotoba coupling; the
  omp cache row is keyed per (name, description) but lane files are not router-visible, so editing the
  description has no host cache consequence.

## Findings

- **F1 (high, blocks C1's guard claim as written).** The plan's content-guard command
  `check_sibling_census.py <census> --province PROVINCE.md --skill SKILL.md` exits 2 at the pin:
  `error: unrecognized arguments: --skill SKILL.md` (argparse surface: `census`, `--fleet`, `--province`,
  `--self-test`). The guard's own doc and code confirm it re-derives sibling-side cells only; it never
  reads kotoba's SKILL.md. So "fails (exit 1) and names the lane … 4 lanes missing" is not observable
  with the pin's instrument. C1's landing must add the `--skill` arm (and, per D3, duplicate-row
  rejection + floors-registry entry), then show red on the base description and green on the rewrite
  with the landed instrument. Run as the census recheck states it (no `--skill`): `rows 20 verified 20 /
  province rows 20 matched 20`, exit 0 — the guard is green on sibling+province content today.
- **F2 (medium, honest-saturation).** The checklist instrument's green is layout-dependent: in my
  scratch clone (same bytes, dir `lane`, parent without `.ufo/`) it exits 1 on
  `trigger.name_directory` (name != dir 'lane'), `trigger.citation_resolves` and
  `governance.citation_resolves` (`../.ufo/reports/round-7/kotoba.md` resolves only against the fleet
  root). Content-clean; expected from scratch clones. Any "exit 0" verdict is only reproducible in the
  lane checkout — say so when citing it.
- **F3 (low).** `the five` count word (box 13 adjacent-scope): stale the moment C1 lands 9; rewrite
  must not carry any bare count that the census can contradict. Prefer naming the mechanism
  (census-classified adjacent lanes) over a number.
- **F4 (info).** On an omp cache miss this description renders as its first 99 chars, cutting mid-word
  ("…dispatch prompts / syste") — every trigger, anti-trigger and sibling clause is past the cliff.
  Moot for lane files (not router-visible), but the disclaimer saying so is itself past offset 99;
  audit-side only. C1's new SOURCES row (opencode docs, S024 candidate) should state whether opencode's
  full-byte render still holds for the routed surfaces.

## Evidence (commands, exit codes)

- `git -C <lane> rev-parse HEAD` → `f3046466…` (equals pin); `git diff f3046466… -- SKILL.md` → 0 bytes.
- `python3 -B verifiers/verify_skill_checklist.py --json` (lane root): `exit_code 0`, pass 11, fail 0;
  description 814 chars; 537 lines vs budget 600 (from box at line 252).
- Same script in scratch clone `/fast/scratch/hyaku/kotoba-r50/build/ReviewSkillTriggerCraft/lane`:
  exit 1 — fail 3 (`name_directory`, `citation_resolves`, `governance.citation_resolves`), details in F2.
- Plan's C1 counter at the pin → `5` (exit 0 of the pipeline), names kagi/kake/kasegi/kengaku/kumitate.
- `check_sibling_census.py … --skill SKILL.md` → argparse exit 2; without `--skill` → exit 0, `rows 20
  verified 20`; with `--fleet .` → exit 1 naming all 20 lanes as outside the fleet root (expected
  misuse, shows the red arm fires on layout, not description).
- Baseline map read: trigger.05 disposition `unexecuted:concreteness and arbitration adequacy are
  semantic judgements … human-graded`; 8 `executed:trigger.*`, 2 `delegated:verify_dispatch_prompts.py`,
  31 further `unexecuted:`.

## Residual risk and verification gaps

- No `lsp` device exists in this session's tool inventory, so caller/definition checks were done by
  CLI + text sweep of `verifiers/` (recorded as the fallback, per role rules); a language server might
  surface additional in-repo readers of the frontmatter that my grep missed.
- I reviewed constraints and instrument behavior, not a candidate rewritten description (none exists at
  the pin); the split-compression arithmetic (~175 chars) is the binding constraint to re-check on the
  actual text, plus a post-landing rerun of both instruments in the lane.
- D3 may move census rows between `none` and non-`none` (plan says re-declare before landing); my
  5-of-9 statement is at the pin's census and would move with such a ruling.
- C2 (box-proof), D1–D6 execution, and the frontier SOURCES rows are other seats; not reviewed here.
