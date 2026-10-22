# RowLore — C1 census row `lore` (round-49 falsify)

VERDICT: **HOLDS-BOUNDED** — for census row `lore` (`corpus/knowledge/sibling-overlap-census-round49.md:75`)
and its `PROVINCE.md` § Adjacent row. Classification `none`, commit, branch, skill file, scope quote,
`names kotoba`, the guard, and every factual statement in the boundary note verify. One finding: the
`arbitration` mechanical cell is right only under an unstated self-token exclusion that the entry's
stated rule does not contain. No claim of the round is flipped by it.

## Findings

1. **MINOR — `arbitration` cell not derivable from the entry's stated mechanical rule (self-token
   omission).** The rule (`§ Classification rule`, census entry): "`names kotoba` and `arbitration`
   are mechanical: whether the frontmatter `description` at the pin contains the token `kotoba`, and
   which sibling lane names (case-insensitive, whole token) it contains." Re-derived from
   `git show 380ef3abc7c7af11d7f23e9f9c82bb1937e1f695:SKILL.md` (folded description, lines 3-12):
   whole-token hits are `chousa:1`, `game-dev-2d:1`, **`lore:4`** ("lore provenance" trigger :4,
   "Lore owns fictional-world entities" :7, "Lore consumes its evidence" :8, "adjudicated as lore"
   :11). `lore` is one of the 20 sibling lane names; the cell records `yes: chousa, game-dev-2d`.
   The omission matches the entry intro's framing ("what each sibling's skill description says about
   its **neighbours**") but the rule sentence states no self-exclusion, so the cell is not the stated
   mechanical function of the description. Corroboration that this is systematic rule wording, not a
   lore-seat data error: kengaku's cell (`:78`, `yes: chousa, kama, kotoba, kumitate, tameshi`) also
   omits a self-token (`kengaku:1` in its description at `1f3b0f1e`), and it is the only other lane
   whose description contains its own name; all 15 other SKILL.md lanes derive self=0 and their
   cells match the derivation exactly (chousa, game-dev-3d, kotodama, mori, souji, tameshi checked
   token-by-token). Impact: none on classification (`lore`'s self-mentions claim lore's own ground,
   not a kotoba split), none on the C1 observables (row count 20; guard), none on the guard's join.
2. **Verified-clean, no defect found** — each attacked cell:
   - Commit/branch (check 1): `380ef3abc7c7af11d7f23e9f9c82bb1937e1f695` resolves (exit 0), is HEAD
     of `main`, and `branch --contains` returns `main`; branch cell `main` is right.
   - Scope quote (check 2): verbatim at `lore PROVINCE.md:3` (title :1, blank :2, scope :3);
     whitespace-collapsed census text matches byte-for-byte including both em-dashes.
   - Classification `none` (check 3): under the entry's rule (surfaces = SKILL.md, PROVINCE.md,
     corpus files) no committed scope surface claims kotoba's core or states a kotoba split.
     Tree-wide `kotoba` grep at the pin → 17 matches, all in `.ufo/` wave artifacts plus
     `reports/round-1/r1-current-scribe.md:73` (a placeholder-token note, not a scope claim). The
     wave artifacts actually pin kotoba's ownership from lore's side: `.ufo/waves/round-87/S3.md:15`
     ("Its province covers prompt/skill craft … lore owns those records"; kotoba "cannot absorb the
     cluster") and `followup/K2-adjacency.md:69` (kotoba "rejected" as owner). Corpus sweep
     (`kotoba|frontmatter|AGENTS\.md|dispatch|prompt|SKILL\.md`, case-insensitive): 25 files, all
     lore-own SKILL.md gate-registry/decision-row references, lore's own dispatch-seat accounting,
     "prompt" as an external writing prompt (`r94-cross-myth-design-comparison.md:25`), and splits
     with chousa (`corpus/SOURCES.md:3`, `r103-canon-status-and-supersession.md:96`) and kotodama
     (`corpus/README.md:73` CM-g) — none with kotoba. `LOG.md:1655/:1670` are r86 process narration
     (lore inspecting its own alias bindings; "Root SKILL.md / AGENTS.md / MINT.md … were absent in
     explicit sweeps"), not frontmatter/agent-def craft claims. The build seat's narrower sweep
     (`SKILL\.md anatomy|frontmatter|AGENTS\.md|dispatch prompt` over `corpus/` → 0) is subsumed.
   - Mechanical columns (check 4): `names kotoba` = `no` (0 occurrences in the description; the only
     `kotoba` tokens in the tree are the wave artifacts above). `arbitration` = `yes: chousa,
     game-dev-2d` — correct under the neighbour reading (finding 1); lore's PROVINCE § Adjacent at
     the pin names exactly chousa, kotodama, game-dev-2d, no kotoba.
   - Skill file: tree has exactly `SKILL.md`; no `AGENTS.md`, `CLAUDE.md`, `MINT.md`, no root
     `tools/` (`ls-tree -r` filter → `SKILL.md` only, exit 0).
   - Guard: `python3 -B verifiers/check_sibling_census.py corpus/knowledge/sibling-overlap-census-round49.md
     --province PROVINCE.md` → `rows 20 verified 20` / `province rows 20 matched 20`, exit **0**,
     reproduced on the integrated tree.
3. **Boundary note (check 5)** — `| lore | none | 380ef3a… | fictional-world records; no claim on
   kotoba ground |`: "fictional-world records" matches `lore PROVINCE.md:3` verbatim; "no claim on
   kotoba ground" is supported by the sweeps above; commit and classification match the census row;
   the row cites no file:line, so there is no citation to verify. No defect.

## Residual risk

- The `none` classification depends on the rule's surface enumeration. Lore's committed wave
  artifacts (`.ufo/waves/round-87/S3.md:15`, `followup/K2-adjacency.md:69`) do state a lore/kotoba
  split for one artifact class (symbolism clause-maps inside world bibles: lore owns, kotoba cannot
  absorb). Under a broader "any committed declaration" reading lore would be `adjacent`; the
  kotodama override is anchored on SKILL.md:3 (enumerated), so the entry applies its own rule
  consistently. A future rule rewording should decide this explicitly.
- The `arbitration` self-exclusion should be stated in the rule text (finding 1); until then the
  column is a judgment cell wearing a mechanical label.

## Verification gaps

- First self-token sweep used an extractor that skipped single-line `description:` values; the
  published numbers come from the corrected extractor (folded and single-line both handled).
  Lore's numbers were identical under both.
- I did not audit the no-SKILL.md rows' `skill file` cells (audio, game-dev-2d, revenger) — out of
  this row's scope; their own seats hold them.

## Evidence (commands, exit codes)

- `git -C /home/vgpnk/Projects/shokunin/lore-shokunin rev-parse 380ef3abc7c7af11d7f23e9f9c82bb1937e1f695^{commit}`
  → same sha, exit 0; `rev-parse HEAD` → same; `rev-parse --abbrev-ref HEAD` → `main`;
  `branch --contains <pin>` → `* main` (read-only query; one command beyond the enumerated five —
  recorded here; nothing was written).
- `git -C … show 380ef3a:PROVINCE.md | sed -n '1,10p'` → :3 verbatim scope line, exit 0.
- `git -C … show 380ef3a:SKILL.md | sed -n '1,20p'` → folded description :2-12, exit 0.
- Token derivation loop over the census rows at each pinned commit (whole-token, case-insensitive):
  `lore => chousa:1 game-dev-2d:1 lore:4`; `kengaku => … kengaku:1 kotoba:1 …`; `kotodama => chousa:1
  lore:1 kotoba:1`; all other SKILL.md rows self=0 and cell-matching.
- `git -C … grep -I -i -n kotoba 380ef3a` → 17 matches, `.ufo/*` + `reports/round-1/r1-current-scribe.md:73`.
- `git -C … grep -I -c -iE 'kotoba|frontmatter|AGENTS\.md|dispatch|prompt|SKILL\.md' 380ef3a -- corpus
  considerthese SHONEN.md SCORECARD.md l0-questions.md README.md` → exit 0 (25 files; all lines
  inspected, none claims kotoba ground).
- `git -C … ls-tree -r --name-only 380ef3a | grep -E '(^|/)(AGENTS|CLAUDE|SKILL)\.md$|^tools/'`
  → `SKILL.md`, exit 0.
- `cd /home/vgpnk/Projects/shokunin/kotoba-shokunin && python3 -B verifiers/check_sibling_census.py
  corpus/knowledge/sibling-overlap-census-round49.md --province PROVINCE.md; echo exit=$?`
  → `rows 20 verified 20`, `province rows 20 matched 20`, `exit=0`.

Tooling: no tool installed or upgraded this session (git/grep/awk/sed/python3 already present); no
pacman/uv/cargo/npm transaction; no jj command anywhere; sibling repo accessed read-only via
rev-parse/show/ls-tree/grep plus the one `branch --contains` query recorded above.
