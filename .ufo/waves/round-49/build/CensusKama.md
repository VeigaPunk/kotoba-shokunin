ROW | kama | master | c808ba07f09c4be55413d3d6516c542ab69b64f8 | SKILL.md | adjacent | no | no | SKILL.md:8 | "Local model serving & endpoint health. This lane answers exactly one question:"

# kama census — kotoba round 49, C1 adjacency

Scout: `KotobaR49.CensusKama`. Surface: `/home/vgpnk/Projects/shokunin/kama-shokunin`, read-only.
All reads are `git show <pinned commit>:<path>`; the sibling's working tree was never read as evidence.
Classification: **adjacent**. Description names kotoba: **no**. Frontmatter arbitration clause: **no**.

## Findings

1. **Pin.** `master` = `c808ba07f09c4be55413d3d6516c542ab69b64f8` (`rev-parse master`, exit 0). HEAD is
   detached at the same commit (`symbolic-ref -q HEAD` exit 1; `rev-parse HEAD` = same 40-hex), so the
   checkout is not on a branch, but `master` resolves and is the branch recorded here.
   The sibling's working tree is live/dirty: `status --porcelain` shows two untracked paths
   (`.ufo/waves/round-25/a2-build/`, `corpus/knowledge/context-capacity.md`). Pins, not the tree, are
   the census surface.
2. **Skill file.** Exactly one SKILL.md, at the repo root (`ls-tree -r --name-only | grep -E
   '^(skills?/[^/]+/)?SKILL\.md$'` returns only `SKILL.md`, exit 0). No `skills/<name>/` layout.
   Frontmatter `name: kama-shokunin`; `description:` verbatim (SKILL.md:3):
   "Domain specialist — local model serving & endpoint health — scopes local LLM endpoints, baseURL
   drift, model-id reconciliation. Rank: shonen." No trigger clause, no sibling named, no arbitration
   rule in the description.
3. **PROVINCE.md.** Sections are bold labels, not `##` headings. It has **no Adjacent section**
   (`grep -ci adjacent` = 0) and **names kotoba 0 times**. Its Refuses line names kengaku, kagi,
   kumitate, kake — not kotoba. Its Owns table row 2 makes `baseURL pins in surviving/loadable
   consumers` a kama surface, including a historical agent file (`agents/janitor.md:21`).
4. **Why adjacent, not contested.** kama reads agent-definition files as a *config* surface: SKILL.md:20-21
   declares the domain as "`baseURL` values declared by consumer configs that point at a loopback port
   (OpenCode provider blocks, agent frontmatter, shell scripts, systemd units)". The lane's own corpus
   states the split in kotoba's terms: `corpus/knowledge/cross-lane-scope.md:29` assigns "**Kotoba** owns
   the instruction/agent surface and its model/fallback wording; **kama** owns independent verification of
   the target endpoint", and the falsifiable rule at `:32` says "if changing only agent/instruction wording
   changes it, kotoba". `.ufo/waves/round-11/advice/SiblingOverlap.md:68-71` repeats it under a heading
   named for kotoba: kama owns "whether the runtime behind a configured baseURL serves the exact model
   name", kotoba owns "agent system prompts, prompt template engineering, and declared model selection in
   agent definitions". That is one artifact class (agent definitions) with disjoint ownership of what is
   true in it — the same shape as kotoba's existing kumitate entry (runtime versus wording).
   Not contested: kama never writes those files (hard write boundary, PROVINCE `**Write boundary (hard)**`:
   never `~/.config`, `~/.omp`, systemd; "detects and reports"), never judges skill trigger/anatomy/
   fidelity, and builds no instrument over SKILL.md/prompt/AGENTS.md quality. Its only cross-lane SKILL.md
   touch is a host-path fact check inside kengaku's skill (`MINT.md:24`), not a craft verdict.
   `[INFERENCE]` The half kama owns is exercised read-only; if the L1 reads "owns a half" as requiring a
   write/audit verdict, kama drops to `none`. The corpus arbitration clause above is the evidence I used
   for `adjacent`; kotoba's current one-liner ("kama (model serving) — no overlap observed",
   `kotoba PROVINCE.md` § Adjacent) is echoed by kama's own scan `overlap-scan.tsv:17`
   ("boundary confirmed"), so the census is changing an existing recorded read, not filling a blank.
5. **Arbitration clause field.** The ROW field is scoped to the *frontmatter description* (seat step 5):
   no. The lane nonetheless carries a concrete, falsifiable sibling arbitration rule naming kotoba in
   corpus, not in SKILL.md/PROVINCE.md — worth a census column of its own so the finding is not lost.

## Evidence (commands, exit codes)

Repo `B=/home/vgpnk/Projects/shokunin/kama-shokunin`, `C=c808ba07f09c4be55413d3d6516c542ab69b64f8`.

- `git -C $B rev-parse master` → `c808ba07f09c4be55413d3d6516c542ab69b64f8`, exit 0.
- `git -C $B symbolic-ref -q HEAD` → no output, exit 1 (detached); `git -C $B rev-parse HEAD` → same commit, exit 0.
- `git -C $B ls-tree --name-only $C` → 16 top-level entries (`.gitignore .ufo AGENTS.md LOG.md MINT.md PROVINCE.md README.md SCORECARD.md SHONEN.md SKILL.md considerthese corpus plans registry tests tools`), exit 0.
- `git -C $B ls-tree -r --name-only $C | grep -E '^(skills?/[^/]+/)?SKILL\.md$'` → `SKILL.md` (1 line), exit 0.
- `git -C $B show $C:SKILL.md | grep -c kotoba` → **0**, exit 1.
- `git -C $B show $C:PROVINCE.md | grep -c kotoba` → **0**, exit 1.
- `git -C $B show $C:PROVINCE.md | grep -ci adjacent` → **0**, exit 1.
- `git -C $B show $C:corpus/knowledge/cross-lane-scope.md | grep -c kotoba` → **3**, exit 0 (lines 13, 14, 29; rule at 32).
- `git -C $B show $C:MINT.md | grep -c -i kotoba` → 2 (lines 20-21; janitor.md 8080 consumer span).
- `git -C $B show $C:AGENTS.md | grep -c -i kotoba` → 0, exit 1.
- Sweep, SKILL.md: `git -C $B show $C:SKILL.md | grep -cE 'SKILL\.md|prompt|AGENTS\.md|frontmatter|trigger|description|kotoba'` → **4**, exit 0
  (line 3 description, line 21 "agent frontmatter", line 187 `llamacpp:prompt_tokens_total` metric, line 623 "trigger-to-outcome" KQ23). Only line 21 touches an instruction surface.
- Sweep, PROVINCE.md: same regex → **0**, exit 1.
- `git -C $B status --porcelain` → 2 untracked lines, exit 0.
- Blob ids at the pin: SKILL.md `eff23eab463c49c706ac69f32f6edd4f34234cdd`; PROVINCE.md `4106c7f54560e62e28707222f1d1a05ceb7d24ae`;
  cross-lane-scope.md `87204d4789ec460e508f0c559129f15b2a3ed100`; round-11 SiblingOverlap.md `6422cb2321426eddc8c3573c223d875eea028212`;
  overlap-scan.tsv `b6cf0cbebeb3f08b4840ca0b071ee05dd025bd86`. Commands: `git -C $B rev-parse $C:<path>` each, exit 0.

Quotes at the pin:
- Scope (SKILL.md:8-9, line 9 bold in file): "Local model serving & endpoint health. This lane answers
  exactly one question: is the thing at this baseURL the model this config believes it is, right now."
- Overlap (cross-lane-scope.md:29): "Kotoba owns the instruction/agent surface and its model/fallback
  wording; kama owns independent verification of the target endpoint." (`**` emphasis in file.)

Tooling: none installed or upgraded this seat.

## Remaining unknowns

- Whether any earlier kama revision carried a sibling arbitration clause in the SKILL.md description was
  not traced (would need `git log -L3,+1:SKILL.md`; out of scope for the pin).
- Kotoba's side of the arbitration (`kotoba PROVINCE.md` § Adjacent) and kama's own scan agree on
  "no overlap observed"; the census override to `adjacent` is my call on the corpus text, flagged above.
