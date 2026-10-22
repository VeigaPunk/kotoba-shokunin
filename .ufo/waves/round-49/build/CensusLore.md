ROW | lore | main | 380ef3abc7c7af11d7f23e9f9c82bb1937e1f695 | SKILL.md | none | no | yes | PROVINCE.md:3 | "Owns: fictional-world records — entities (characters, places, factions, items), relations, timeline events — with consistency verification and sourced inspiration."

# Findings

1. **Classification `none`.** `lore-shokunin` owns fictional-world records (entities, relations,
   timeline, sourced inspiration) and its six executable gates (`check_bible`, `support_check`,
   `map_obligations`, `dependency_freeze`, `boundary_doc_check`, `discriminate_check`) all audit lore
   fixtures. No file in the pinned tree has SKILL.md anatomy, frontmatter, agent-definition,
   always-on (AGENTS.md/CLAUDE.md) or dispatch-prompt craft as its *subject*: `git grep -l -iE
   'SKILL\.md anatomy|frontmatter|AGENTS\.md|dispatch prompt' <c> -- corpus/` → no match (exit 1);
   knowledge-file names matching `skill|prompt|agent|frontmatter|dispatch` → 0 of 26 (exit 1).
   It therefore does not claim any part of kotoba's core (not `contested`) and shares no split
   surface with it (not `adjacent`).
2. **Sweep (the `none` arm), pinned files `SKILL.md`, `PROVINCE.md`, `README.md`.** Pattern
   `SKILL\.md|prompt|AGENTS\.md|frontmatter|trigger|description|kotoba`, case-insensitive → **6
   matches**: SKILL.md 4 (`description` ×2 = the frontmatter key at :2 and the phrase "sourced
   description" at :27; `Trigger`/`trigger` ×2 = :3 "Triggers:" and :4 "Anti-trigger:"),
   PROVINCE.md 1
   (`SKILL.md` self-reference at :27), README.md 1 (`SKILL.md` self-reference at :12). Zero
   occurrences of `prompt`, `AGENTS.md`, `frontmatter`, `kotoba` in any of the three files. Every
   match is self-referential, none is a claim on kotoba's province.
3. **Frontmatter shape (census datum).** The frontmatter is description-only: `name:` is absent
   (`git show <c>:SKILL.md | sed -n '1,12p'` shows `---`, `description: >`, eight folded lines,
   `---`). So a sibling that does not even carry the `name` key cannot be competing for kotoba's
   frontmatter-craft core.
4. **Arbitration clause: yes, but not against kotoba.** SKILL.md:6-11 (folded description) carries
   "Sibling arbitration: Lore owns fictional-world entities, relations, timeline and integration
   (PROVINCE.md:3,9); Chousa owns research method (…); game-dev-2d owns mechanics (PROVINCE.md:9)."
   It arbitrates against **chousa** and **game-dev-2d** only. `PROVINCE.md` § Adjacent (:25-29) names
   **chousa, kotodama, game-dev-2d**; kotoba is absent from both files.
5. **Mutual non-overlap, from the sibling's own record.** Lore's round-87 adjacency census already
   rejected kotoba as owner for a lore-content cluster: `.ufo/waves/round-87/K1.md:21`
   "**kotoba-shokunin — rejected.** Observed: it owns “prompt & skill craft”
   (`kotoba-shokunin/PROVINCE.md:1-6`)." and `.ufo/waves/round-87/followup/K2-adjacency.md:69`
   "| 11 | kotoba-shokunin | prompt & skill craft (`PROVINCE.md:3-6`) | rejected | A symbolism
   clause-map is fictional-world content, not a skill playbook. |". This is the sibling pinning the
   same boundary from its side, at its own commit.
6. **Residual candidates I considered and rejected.**
   - `boundary_doc_check` (SKILL.md:52-61) is an instrument of the same genus as kotoba's (pinned
     digests, receipt replay, explicit anchor ranges, limited structure), but its frozen document is
     `corpus/knowledge/holder-assessment-boundary.md` and the lane's own checker — a lore surface,
     not a skill/prompt surface (`corpus/tools/README.md:51`).
   - Lore runs its own per-round adjacency censuses (`.ufo/waves/round-87|94/followup/*-adjacency.md`).
     That is the same *activity* kotoba's C1 performs, but a wave artifact, not a claimed province
     surface; it is how each lane audits its own admissions.
   - Lore's own round dispatch declarations (`.ufo/waves/round-93/deepseek/dispatch-declaration.json`,
     6 dispatch-named files total) are seal receipts for its seats. `.ufo/prompts/` does not exist in
     the lane (0 paths, exit 1), so there is no dispatch-prompt corpus to overlap with C2.
7. **Census action for kotoba `PROVINCE.md` § Adjacent** (lore is currently unlisted; kotoba's
   section names 10 lanes at `awk '/^## Adjacent/,0' PROVINCE.md`). Suggested line, matching the
   existing prose form:
   `- lore — fictional-world records (entities, relations, timeline) with consistency and source-support gates; no overlap observed at `380ef3a` (lore `PROVINCE.md:3`), and no arbitration clause in its description names kotoba.`
8. **Remaining unknowns.** (a) Lane SCORECARD scale axes were not audited — out of scope for the
   row. (b) I did not re-verify lore's claim that `game-dev-2d` owns mechanics; taken as the
   sibling's assertion. (c) No web source was used, so no SOURCES.md row is owed by this seat.
   (d) `name:` absence is reported as observed shape only; I did not judge whether the fleet schema
   requires it.

# Evidence (commands, exit codes, hashes)

Pin (step 1):
- `git -C /home/vgpnk/Projects/shokunin/lore-shokunin rev-parse master` → exit **128**
  (`fatal: ambiguous argument 'master'`); branch fallback per assignment.
- `git -C … symbolic-ref -q HEAD` → exit 0, `refs/heads/main`.
- `git -C … rev-parse HEAD` → exit 0, `380ef3abc7c7af11d7f23e9f9c82bb1937e1f695`.
- `git -C … status --porcelain | wc -l` → 0; `git -C … diff --stat HEAD -- SKILL.md PROVINCE.md
  README.md | wc -l` → 0. So working tree == pinned commit for the three files read.

Skill files (step 2):
- `git -C … ls-tree --name-only 380ef3a` → `.gitignore .scratch .ufo LOG.md PROVINCE.md README.md
  SCORECARD.md SHONEN.md SKILL.md considerthese corpus l0-questions.md reports`.
- `git -C … ls-tree -r --name-only 380ef3a | grep -E '^(skills?/[^/]+/)?SKILL\.md$'` → `SKILL.md`
  (exit 0). Tree-wide `(AGENTS|CLAUDE|SKILL)\.md` → only `SKILL.md` (exit 0).

Frontmatter (step 3, `git show 380ef3a:SKILL.md`):
- :2 `description: >`; :3-11 folded trigger/anti-trigger/arbitration text (verbatim scope of the
  lane's use):
  "Triggers: "world bible", "fictional canon claim", … Anti-trigger: do not use for real-world
  source discovery, archive authentication, research-method design, rights or permission
  conclusions, or game-mechanics verification."
- No `name:` key. File is 107 lines / 20349 bytes; blob sha256
  `c1954fbfc5d980bc53f828a2a48c56ffcbd1f1d321ef271291b5e73132f3d0b9` (`git show <c>:SKILL.md |
  sha256sum`).
- Gate registry: `git show <c>:SKILL.md | grep -c '^### '` → **5**; `grep -c '^- \*\*owner:\*\*
  `lore-shokunin`'` → **5** (all bounded to lore fixtures).

PROVINCE.md (step 3, `git show 380ef3a:PROVINCE.md`, 35 lines / 4029 bytes, sha256
`c51cc6b29c52c737dbd19597557730a36e27660f6ff82f5b096bab147c62baab`):
- :1 `# lore province`; :3 the scope quote above; :9 "Refuses: claiming canon without an in-world
  citation; silently resolving contradictions; real-world rights claims (art-east-asian-design);
  game mechanics verification (game-dev-2d)."
- Headings: `## Province map (round 103…)` :13, `### Core` :15, `### Frontier` :21,
  `### Adjacent` :25, `### Corrections` :31. § Adjacent names chousa (:27), kotodama (:28),
  game-dev-2d (:29). No kotoba.

kotoba naming (step 5):
- `git show <c>:SKILL.md | grep -c kotoba` → **0**, exit **1**.
- `git show <c>:PROVINCE.md | grep -c kotoba` → **0**, exit **1**.
- `git show <c>:README.md | grep -c kotoba` → **0**, exit **1**.
- Tree-wide `git grep -I -i -c 'kotoba' <c> -- .` → **14 files, 17 matches**, all in `.ufo/waves/`
  wave artifacts plus `reports/round-1/r1-current-scribe.md:73`; none in a province, skill or
  knowledge entry. Three substantive ones: `.ufo/waves/round-87/K1.md:21`,
  `.ufo/waves/round-87/followup/K2-adjacency.md:69`, `.ufo/waves/round-87/S3.md:15` ("kotoba-shokunin
  — cannot absorb the cluster.").

Sweep (step 4, `none` arm):
- `for f in SKILL.md PROVINCE.md README.md; do git show <c>:$f | grep -oiE 'SKILL\.md|prompt|AGENTS\.md|frontmatter|trigger|description|kotoba' | sort | uniq -c; done`
  → SKILL.md: `2 description`, `1 trigger`, `1 Trigger`; PROVINCE.md: `1 SKILL.md`; README.md:
  `1 SKILL.md`. Total **6** (case-insensitive), **5** case-sensitive (`… | grep -oE … | wc -l`).
- `for f in …; do n=$(git show <c>:$f | grep -ciE '…'); done` → 4 / 1 / 1.
- `git -C … ls-tree -r --name-only <c> | grep -E '^\.ufo/prompts' | wc -l` → **0** (exit 1);
  `… | grep -cE 'dispatch'` → **6**.

README.md (step 2 fallback surfaced anyway; 24 lines / 1178 bytes, sha256
`ad4adb1e6cfbec41c83281aa7dfe1439d453ab5cb4290a9d8c25c1a1b06c2caf`):
- :6 "**Domain:** Fictional-world records — entities, relations, timeline — with mechanical
  consistency verification and sourced inspiration." :12-13 lists `SKILL.md` as "the distilled
  expertise: decision tables, error patterns, checklists" — the fleet house form, not a craft claim.

Tooling: no installs or upgrades this session (nothing needed; `git`, `grep`, `awk`, `sha256sum`
already present). No `pacman`, `uv`, `cargo` or `npm` transaction was run. No jj command was run.
Sibling repo accessed read-only via `git show` / `ls-tree` / `grep` / `rev-parse` / `status` only.
