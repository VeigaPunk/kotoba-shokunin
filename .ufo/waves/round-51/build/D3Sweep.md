# D3 sweep — stale restatements of the withdrawn round-50 claims

Seat: KotobaR51.D3Sweep (attack seat, round 51 build, 2026-10-22). Read-only sweep; no lane file
touched except this report. Measured at lane `master` = `43ca0bfb74372f2a67a48e0aeb2e35d0d98b1d10`
(`git rev-parse HEAD`); `git status --porcelain` shows no local modification to any swept target
(only ` M verifiers/baseline.json` plus untracked round-51 work by other seats).

**HOLDS** — on the D3 bar (only the two routed sites state the withdrawn claims as current in the
tracked text): `corpus/README.md:72` and `SKILL.md:375-377`. No third stale site exists. One owning
entry carries the superseded finding 4 unmarked (`corpus/knowledge/skill-selection-rules-round50.md:42`);
per the round-51 plan C2 supersedes it, but its append-only correction is routed nowhere — advisory P2
below, with wording. If the L1 counts that unmarked owning-entry finding as a live statement, the
verdict flips to FAILS with that single extra site; on the assignment's own framing (the entry is the
withdrawn/superseded source, its finding 3 already corrected in-entry) it is not a stale restatement.

## Counting rule

A sentence counts as a hit if a reader of the tracked file would take it as the current documented
state: not withdrawn by a corrections section in the same tracked text, and not scoped by an explicit
bound in the same tracked text. LOG.md, `corpus/lessons/*` and `.ufo/**` are records — out of scope
(sightings noted at the end).

## Hit 1 — SKILL.md:375-377 (routed D3)

Sentence (lines 375-377, inside the § Anti-patterns error pattern):

> No client documents a rule between two differently named skills whose descriptions
> both match; the documented rules decide between copies of one name, component types or
> configuration sources, and the documented remedy is a more specific description.

Defects: (a) the negative has no eight-page bound and no "author-written" qualifier (the entry's
finding 1 is limited: "The negative in finding 1 covers these eight pages only", entry line 69);
(b) "the documented remedy is a more specific description" is the superseded finding 4 — no disable
or deny lever is named. The middle clause already matches corrected finding 3.

Minimal replacement (carries: eight pages; author-written; type/source-keyed clause kept; disable and
deny levers per client):

> On the eight pages `corpus/knowledge/skill-selection-rules-round50.md` mined, no client documents
> a rule between two differently named author-written skills whose descriptions both match; the
> documented rules decide between copies of one name, between component types or between
> configuration sources, and the documented remedies beyond description wording are per client
> (Claude Code `disable-model-invocation: true`, `when_to_use`, `paths`; Copilot SDK `disabledSkills`
> and directory reorganization; opencode `autoinvoke: "false"`).

The following "Fix: name the neighbour and the split in the description (`trigger.05`)…" sentence
stands unchanged.

## Hit 2 — corpus/README.md:72 (routed D3)

Index row (basis cell):

> eight client pages (S024–S029, S022, S019): no client documents a rule between two differently
> named skills whose descriptions both match; every documented rule is keyed on the name, except
> Claude Code's built-in catch-all agent (fit-based default); the documented remedy is a more
> specific description; recheck compares content hashes

Defects: "every documented rule is keyed on the name, except …" is the withdrawn finding 3 as
pre-correction (type-keyed and source-keyed rules also exist — Copilot CLI; SDK provider-skill
replacement; entry lines 75-80); "the documented remedy is a more specific description" is the
superseded finding 4. The negative clause, though prefixed by the page list, lacks "author-written".

Minimal replacement (basis cell only):

> eight client pages (S024–S029, S022, S019): no client documents a rule between two differently
> named author-written skills whose descriptions both match (finding 1, these eight pages only);
> documented rules decide between copies of one name, component types or configuration sources, plus
> one fit-based built-in catch-all (finding 3 as corrected); documented overlap remedies beyond
> description wording are per client — Claude Code `disable-model-invocation: true`, `when_to_use`,
> `paths`; Copilot SDK `disabledSkills` and directory reorganization; opencode
> `autoinvoke: "false"` (finding 4 superseded round 51 by `knowledge/skill-overlap-levers-round51.md`);
> recheck compares content hashes

## Advisory P2 — the owning entry's finding 4 is superseded but unmarked

`corpus/knowledge/skill-selection-rules-round50.md:42-45` still reads "**The documented remedy for
overlap is specificity in the description.** …" with no correction anywhere in the entry: its
§ Falsify-wave corrections (lines 73-90) correct finding 3 (too wide) and finding 1's evidence basis,
not finding 4. The entry's own § craft paragraph (lines 52-56) already bounds the lever claim for
Claude Code ("The description is not the author's only lever …") but names no SDK/opencode lever.
The round-51 plan routes the supersession to C2's new entry and the SKILL.md rewrite, not to the old
entry; the corpus convention (LOG.md:2405; the census corrections; this entry's own corrections
section) is to append a marked correction to the entry that made the finding. Recommended append to
the entry's § Falsify-wave corrections when C2 lands:

> - **Finding 4 is superseded (round 51, C2)** (`skill-overlap-levers-round51.md`): specificity in
>   the description is one documented remedy, not the documented one; the Copilot SDK page documents
>   "Use `disabledSkills` to exclude conflicting skills" / "Reorganize skill directories to avoid
>   overlaps" (`skills.md:805-810`), opencode documents `autoinvoke: "false"`, and Claude Code's
>   `when_to_use` / `disable-model-invocation` / `paths` levers are already noted above.

(The two SDK quotes above are as recorded in `corpus/lessons/round-50-verifier-spotcheck.md:189` from
its 2026-10-22 fetch; I performed no fetches.)

## Checked, not hits (equivalents, each bounded or corrected in tracked text)

- `PROVINCE.md:17` — "the primary-source finding that no documented tie-break exists between
  overlapping descriptions (S022, S023, S018)" — negative carries its three-page citation and points
  to the census entry, which records the finding standing (census line 157) and its round-50 widening
  (census line 195). Neither withdrawn claim.
- `corpus/README.md:69` — census row: "(no documented tie-break between overlapping descriptions)"
  with "sourced on S022, S023 and S018". Bounded. (Index nit, outside the two claims: the entry now
  spans nine pages; the row names the round-49 base sources.)
- `corpus/README.md:128-129` — "six more client pages document no tie-break between overlapping
  descriptions (census entry, round-50 section)" — carries its own page count. Not a hit.
- `corpus/knowledge/sibling-overlap-census-round49.md:34` ("the only arbitration a skill author
  controls is the text of each description") and :210, :225-227 (same class, "keyed on the skill
  *name*") — both sentences are named and rewritten by the entry's appended § Round 50 falsify-wave
  corrections at :301-311 (author-written scope; S022 also documents `when_to_use`,
  `disable-model-invocation`, `paths`). Corrected-in-entry; not live. Census :32 already names
  `disable-model-invocation: true`; :212 is page-scoped ("Its remedy" = S026's page).
- Census :250 ("the six pages opened this round document only name-keyed rules") — same
  keyed-on-name claim bounded to six named pages; covered by the :301 class correction plus "The full
  account is `skill-selection-rules-round50.md`" (whose corrections carry the type/source-keyed
  detail). P3: the :301 correction names two sentences but not this one; extend it when touching the
  census.
- `corpus/knowledge/skill-selection-rules-round50.md:29` (finding 1) — bounded by entry intro lines
  8-9 ("widens that to eight more pages") and § Limits line 69 ("these eight pages only"). :40
  (finding 3) — corrected at :75-80. :52-53 — "the documented advice is to make each description
  specific" is bounded by the next sentence ("not the author's only lever") and § Limits; P3 wording
  nit: "one documented piece of advice".
- `SCORECARD.md` — :31's only match is "the content-digest remedy is evaded by appending one byte"
  (verifier note, unrelated); :34/:116/:118/:250-252/:262 are C1/C2 landing records. `AGENTS.md`,
  root `README.md`, `SHONEN.md` — zero matches on every claim pattern. `corpus/SOURCES.md` scope
  cells describe pages, not the claims.

Out-of-scope sightings (records, not swept, listed for completeness): `.ufo/waves/round-50/build/
SrcReopenS022.md:58` ("specificity is the documented remedy … the only arbitration surface") — a
round-50 seat report kept as evidence; `.ufo/round-23/scouts/F10.md:178`, `.ufo/round-40/scouts/
P6.md:326` — "documented remedy" in unrelated pin contexts; LOG.md:2393/2404/2405 and lessons
(census/round-50 corrections) — records.

## Evidence — commands (run at `43ca0bf`; outputs trimmed, elisions marked)

1. `git -C /home/vgpnk/Projects/shokunin/kotoba-shokunin grep -n -i -e "keyed on the name" -e "documented remedy" -e "only remedy" -e "no client documents"`
   exit 0. In-scope lines: `SKILL.md:375`, `SKILL.md:377`, `corpus/README.md:72`,
   `corpus/knowledge/skill-selection-rules-round50.md:40,42,86`,
   `corpus/knowledge/sibling-overlap-census-round49.md:301`; all other hits under `.ufo/`, `LOG.md`,
   `corpus/lessons/` (out of scope; elided).
2. `git -C … grep -n -i -e "more specific description" -e "specificity" -e "description wording" -e "sharpen the description" -e "eight pages"`
   exit 0. In-scope: `SKILL.md:377`, `corpus/README.md:72`,
   `skill-selection-rules-round50.md:42,69`, `sibling-overlap-census-round49.md:32`;
   `.ufo/`+`LOG.md`+lessons hits elided.
3. `git -C … grep -n -i -e "only lever" -e "only arbitration" -e "only remedy" -e "only mechanism" -e "only documented" -e "only way" -- SKILL.md PROVINCE.md corpus README.md SCORECARD.md AGENTS.md SHONEN.md`
   exit 0. In-scope: census :34, :210, :227, :304, :309; `skill-selection-rules-round50.md:54`
   ("not the author's only lever" — the bound); lessons elided. No SKILL/PROVINCE/SCORECARD/AGENTS/
   README/SHONEN hits.
4. `git -C … grep -n -i -e "no client" -e "no documented" -e "none documents" -e "no rule between" -e "no tie-break" -e "no tiebreak" -- SKILL.md PROVINCE.md corpus README.md SCORECARD.md AGENTS.md SHONEN.md`
   exit 0. In-scope: `PROVINCE.md:17`, `SKILL.md:375`, `corpus/README.md:69,72,128`,
   census :34, :157, :195, `skill-selection-rules-round50.md:8,29,36,52`. No AGENTS/README/SHONEN hits.
5. `git -C … grep -n -i -e "remedy" -e "keyed on" -- SKILL.md PROVINCE.md corpus README.md SCORECARD.md AGENTS.md SHONEN.md`
   exit 0. In-scope: `SKILL.md:377`, `corpus/README.md:72`, census :212, :225, :301, :305,
   round-50 entry :10, :16, :40, :42, :86, `SCORECARD.md:31` (unrelated content-digest remedy).
6. `git -C … grep -n -i -e "keyed" -e "choose between" -e "chooses between" -e "decides between" -e "picks between" -e "no rule" -e "documents no" -e "description only" -e "description-only" -- SKILL.md PROVINCE.md README.md AGENTS.md SCORECARD.md SHONEN.md corpus/README.md corpus/knowledge`
   exit 0. New in-scope: census :14, :217, :219, :250 (all page-scoped or corrected, see above);
   `frontmatter-rule-authorities-round48.md` "no rule" cells are per-rule table cells, unrelated.
7. Clean-file check with exit code:
   `git grep -n -i -e "remedy" -e "keyed on" -e "only lever" -e "only arbitration" -e "no client documents" -e "documented remedy" -e "more specific description" -- AGENTS.md README.md SHONEN.md PROVINCE.md SCORECARD.md; echo "exit=$?"`
   → only `SCORECARD.md:31` (content-digest remedy, unrelated), `exit=0`.
8. Full-sentence reads: `SKILL.md:365-390`, `corpus/README.md:59-138`, `SCORECARD.md:249-278`,
   census `:294-318`, round-50 entry `:7-12,40-47,52-57` (via `git show HEAD:… | sed -n …`).
   grep on tracked files reads the working tree; none of the seven targets is locally modified
   (`git status --porcelain`), so tree = HEAD for every quoted line.

## Residual risk and verification gaps

- The verdict depends on the counting rule above; the single judgment call is the unmarked finding 4
  at `skill-selection-rules-round50.md:42` (advisory P2). Everything else is bounded or corrected in
  tracked text and quoted here.
- The replacement wordings reference `knowledge/skill-overlap-levers-round51.md`, which does not
  exist at `43ca0bf` (untracked tree has no such file yet); the C2 executor must land it (or the L1
  adjust the pointer) for the replacements to resolve.
- `git grep` cannot see untracked files; if a round-51 seat has already written a new in-scope file
  (e.g. the C2 knowledge entry) it was outside this sweep. The only untracked in-scope-path file at
  sweep time was none (untracked: `plans/round-51.md`, `verifiers/check_overlap_levers.py`,
  `.ufo/waves/round-51/`, `DescDraft.md`).
- I ran no fetches and no gates; counts carry their commands. No installs or tool updates were
  needed (none performed).
