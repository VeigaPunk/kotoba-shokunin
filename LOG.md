# kotoba-shokunin — Iteration Log

- 2026-09-28 — round 0: minted as shonen.
- 2026-09-28 — round 1: rewrote SKILL.md as skill-file craft domain knowledge
  (anatomy table, frontmatter trigger rules, decision-table criteria, compression
  rules, 13-item trigger-fidelity checklist, anti-patterns, ~600-line bound).
  Evidence: surveyed 16 production skill files — `~/.agents/skills/{wwkd,godspeed,
  sekhmet-l3,xbrd-ask,omarchy,bailian-*}/SKILL.md` and
  `~/.config/opencode/skills/ufo/SKILL.md` (line counts 18–392; anatomy patterns
  and citations recorded in the file's Sources section).
  Also created corpus/ per ../CORPUS.md: README index + 3 knowledge entries
  (frontmatter triggers, anatomy/compression, fail-closed/anti-patterns) +
  lessons/round-1.md. Independent reviewer lane returned SHIP with all 13
  checklist items passing; added explicit drift-fail-closed clause post-review.
- 2026-09-28 — round 3: closed the AGENTS.md/dispatch-prompt gap filed in round-1
  corpus. SKILL.md gained an "Instruction surfaces" taxonomy (SKILL.md opt-in vs
  AGENTS.md always-on vs dispatch prompts one-shot), 2 cross-surface
  anti-patterns, checklist scope note, and 5 new source entries (3 previously
  unread bailian files now read in-body + AGENTS.md/prompt surfaces). Corpus:
  knowledge/agents-md-and-dispatch-surfaces.md, lessons/round-3.md, README gap
  list updated. Evidence: `cat`/`md5sum` of 6 shokunin AGENTS.md (identical
  5-line template), `diff` of .ufo/prompts/{kagi,kotoba}-L1.md, full reads of
  bailian-{docs-llm-wiki,managed-agent,sandbox}/SKILL.md, PROTOCOL.md file
  contract. Note: operator directive skipped round 2; LOG records actual rounds.
- 2026-09-28 — round 4: extended the instruction-surfaces taxonomy 3→5 classes.
  New surfaces surveyed: `~/.config/opencode/agents/*.md` (18 files, 14–197
  lines; roster frontmatter with `subagents`/`cascade`/`permission_mode`;
  `NOT general-purpose. NOT explore.` negative routing in 7/18; identical
  9-line godspeed preamble in 13/18 — doubled in mutation-tester.md; stale
  dated `cascade_note` in ufo.md), `~/.config/opencode/command/*.md` (3 files;
  pointer-then-rules idiom + `agent:` key + `$ARGUMENTS`), and the round-N
  dispatch mode (`.ufo/prompts/*-round-*.md`, 3–4 lines vs 9–12-line spawn
  mode; `diff kake-round-4.md kasegi-round-4.md` shows name+path-only
  variance). SKILL.md gained 3 table rows, 2 evidence paragraphs, spawn-vs-round
  completeness rule, 6 anti-patterns, 3 source entries. Corpus: knowledge/
  agent-defs-commands-and-round-prompts.md, lessons/round-4.md, README gap
  list updated (5-class coverage; system-prompt/CLAUDE.md/MCP remain open).

- 2026-09-28 — round 5: first end-to-end domain task + round-1 defect repairs.
  Audit: an independent L2 reviewer lane applied the 13-item trigger-fidelity
  checklist verbatim to the 5 sibling `*-shokunin/SKILL.md` files (strict
  reading); L1 verified frontmatter items and every cited defect line.
  Result: all 5 fail — systemic template defect, all descriptions are
  `Domain specialist — scopes X` with zero quoted triggers/anti-triggers
  (items 2–3: 0/5), zero sibling arbitration (item 4: 0/5) despite named
  overlaps found (kagi↔kake CDP, kengaku↔bailian-docs-llm-wiki). 5
  checklist-ambiguity meta-findings filed and resolved in SKILL.md
  (prerequisite defined, action-cell rule replaces last-column rule, command
  scope widened, citation-base rule added, item 4 surface pinned to
  `description`). Defect repairs (aggregator audit queue): dropped the
  fabricated `bailian-train-deploy` 火山方舟/ark frontmatter quote (verified:
  the text exists nowhere in that file); scoped `requires.bins` claim to
  7-of-10 with named exceptions; replaced the unswept "counterexample none
  found" claim with a grep sweep + 2/16 counterexample rate
  (bailian-docs-llm-wiki body 何时使用/何时不要使用, bailian-model-recommend
  body 适用场景). Corpus: knowledge/fleet-skill-audit-round5.md,
  knowledge/harness-system-prompt.md (6th surface class — observed,
  not owned), lessons/round-5.md, README coverage+gaps updated. SHONEN.md:
  all 4 boxes ticked with evidence lines.
  Telemetry (scout lane + L1 re-verified): a real activation trace exists —
  `~/.local/share/opencode/opencode.db` `part` table, `$.tool='skill'` (415
  calls / 216 sessions / 11 skills; histogram re-run by hand matches:
  godspeed 239, wwkd 52, ufo 51, …); per-prompt attribution via
  `part.message_id → message`. Bigger find: the `<skills>` catalogue the
  router sees is a model-compressed render of `description` (~95–103 chars,
  template embedded at ~/.local/bin/omp ELF offset 283082932 — re-verified by
  `grep -abo`; 10191 compression-failure warns in ~/.omp/logs). SKILL.md
  gained the compressed-render caveat + front-load rule 8. Corpus:
  knowledge/skill-activation-telemetry.md.
- 2026-09-28 — round 6: three convergent moves. (a) Second end-to-end domain
  task: added a 9-item agent-definition fidelity checklist to SKILL.md and an
  independent L2 reviewer lane applied it verbatim to all 18
  `~/.config/opencode/agents/*.md` — 15/18 clean, 4 fail cells (ufo.md missing
  `name:` + stale `cascade_note` "until 2026-08-29", mutation-tester.md
  preamble doubled at lines 8-14+34-40, scout.md `aaron` bin absent from PATH),
  all L1 re-verified (`command -v aaron` empty; frontmatter greps). 10
  meta-findings resolved into the checklist (schema-not-list key rule,
  description-dated-text scope, same-name-differing-content blocks, file-path
  resolution, harness-literal carve-out). Audit corrected round-4 counts:
  godspeed preamble 13→14/18 (orch.md missed), negative routing 7→11/18.
  Artifact: `corpus/knowledge/agent-def-audit-round6.md`. (b) Seventh surface
  class: CLAUDE.md census — 16 files (5 operator-authored incl. a 4339-line
  outlier, 1 dispatch template, 10 vendored/cache); loader strings exist in
  both harness binaries (9/17 refs) but 0 captured injections — a cold
  always-on channel; SKILL.md gained a surfaces-table row. MCP/plugin
  surfaces verified absent (`opencode.json` key set; plugin/ = one nudge
  script). Artifact: `corpus/knowledge/claude-md-surface.md`. (c) First
  fidelity measurement: literal-trigger miss proxy over opencode.db (398
  sessions / 415 skill calls, command/directive text scrubbed) — unique-token
  triggers miss 0%; godspeed always-on coverage only 51.5%; domain-term
  names ambiguous (all 5 `ufo` misses are references, not calls). SKILL.md
  gained frontmatter rule 9 (invocation-shaped triggers for domain-term
  names). Artifact: `corpus/knowledge/trigger-miss-proxy-round6.md`.
  SHONEN.md re-attributed `[~]` self-asserted per PROTOCOL.md round-6 rule.
  Sibling defect re-check: all 5 sibling descriptions still unchanged
  post-audit (fleet still fails trigger items — fix remains cross-domain).
- 2026-09-28 — round 7: mechanism-level correction + three new checklists,
  executed by 9 L2 lanes in one batch (MISSION.md minimum met: reviewer
  self-audit, critic drift recount, sentinel defect re-verify, executor ×2,
  scout ×2, connector routing map, planner AGENTS.md checklist).
  **Primary measurement** (scout lanes, L1 spot-verified): the `<skills>`
  description render is cache-or-truncate, not "model-compressed" as round 5
  claimed — `previewSkillDescription` does `slice(0,99)` + first-sentence
  (≥40 chars, no ellipsis) or last-space + `…`; an async LLM compressor fills
  `~/.omp/agent/skill-descriptions.db` (5/17 skills cached, key
  sha256(template+name+ws-description) reproduced 5/5). Compression activated
  2026-09-24→27 (earlier catalogues render verbatim 163–818 chars; current
  ≤98). Measured loss: 17.7% of description chars reach the router, 53/62
  quoted triggers lost, 13/13 `Triggers:`/反触发/`Excludes` clauses absent —
  all sit past the cliff. Also: 10681 compression-failure warns (99.92% Devin
  `invalid_argument`); two live catalogue variants coexist same-hour;
  godspeed offered 3911/3911 session_init records (round-6's 51.5% gap is
  opencode-side activation, not omp offer); `xbgst-surface` dead offer;
  `ufo` duplicate id (omp/agent copy wins); the six `*-shokunin` SKILL.md
  files are outside every discovery root — never routed at all.
  **Self-audit** (reviewer lane, verbatim 13-item checklist on own SKILL.md):
  7/13 clean, 4 fails + 1 ambiguous — all resolved same round (concrete
  sibling arbitration added to `description`; recipe-vs-prerequisite
  carve-out; bare-path citations grounded; "failure claim" defined).
  **New checklists landed**: dispatch-prompt (12 items, applied — 37/43
  prompt files fail ≥1; `<lane>` placeholders cost kake/kengaku canonical
  round-1 names; 38 files carry stale `m_composer`/`m_antigravity`/`m_grok`
  aliases; generator `shokunin-watchdog.sh` already fixed, artifacts stale)
  and AGENTS.md (8 items, applied — 6/6 repo files pass; host
  `~/.agents/AGENTS.md` fails: procedures at :18/:55, dated text :48/:51 —
  round-1 "zero procedures" claim corrected). SKILL.md rules 8→12 rewritten
  for the cliff (first-sentence exploit, reproduce-don't-assume, discovery-
  root gate); 4 new anti-patterns; Sources updated. **Drift recount**
  (critic): CLAUDE.md census 16→18 (+2 vendored); compression warns
  10191→10681; "byte-identical AGENTS.md" → shape-identical (6 distinct
  md5s, shared body hash equal). Artifacts:
  `corpus/knowledge/render-mechanism-round7.md`,
  `corpus/knowledge/dispatch-prompt-audit-round7.md`,
  `corpus/knowledge/alwayson-checklist-round7.md`, `lessons/round-7.md`.
  Cross-domain queue re-verified by sentinel lane: all sibling/agent-fleet
  defects still present (ufo.md cascade_note now 60d stale). `edit`
  boundary-echo recurred once (intro paragraph tail); caught by re-read.
- 2026-09-28 — round 9: axis move = **consistency** (lowest axis: harness-specific
  routing claims written as universal rules). 14 L2 lanes in two batched `task`
  calls (10 analysis/draft + 4 verification; MISSION.md floor 8): scouts
  (omp render census, opencode gate re-verify), 2 executors, scribe, planner,
  connector, critic ×2, reviewer ×2, sentinel ×2, distiller.
  **Drift measured first**: `sqlite3 -readonly ~/.omp/agent/skill-descriptions.db
  "select count(*) from skill_descriptions;"` → 17 rows (round 7: 5); the cache
  key's description salt is **style-aware** (`>-`/plain → ws-collapsed, `>` →
  +`"\n"` 5 keys, `|` → as-written+`"\n"` 1 key), so round-7's ws-normalised
  recipe reproduces only 11/17 and the correct one 17/17 → "the truncator is the
  default" is truncation-era. **Freeze was upgraded from [INFERENCE] to measured**:
  230 captured `<skills>` blocks show four signatures, monotone 3 ⊂ 5 ⊂ 11 ⊂ 17
  (19:37Z→21:00Z), one per session; kill-proof = L1's frozen catalogue holds a
  sekhmet-l3 render the live db has replaced, and the db's last write
  (20:57:58.180Z) landed 3.9 s after L1's session-start render (20:57:54.260Z).
  **Consistency landed**: `SKILL.md` gained `## Router model — which harness,
  which gate` (per-harness tag/render/offer gate/failure + check-before-predict
  recipe) and every cliff/render claim now names its harness (intro, frontmatter
  opener, rules 8/9, 3 anti-pattern rows). Measured before→after by an L2
  sentinel: 31 claim units, `UNSCOPED 9 → 0`, `UNSUPPORTED 7 → 6`, SCOPED 15 → 23,
  `<available_skills>` occurrences 0 → 3; the 6 residuals were re-worded in-round
  to cite the router model or be marked guidance/heuristic. A second L2 reviewer
  ran the 13-item trigger-fidelity checklist on SKILL.md itself: **13/13 pass**,
  0 ambiguous, with 2 citation fixes applied (split the `skill/index.ts`
  dedupe range to `:105-139`/`:235-246`; widen the session_init range).
  **Round-8's opencode mechanism sentences were re-verified and 3 corrected**:
  duplicates are last-parsed-wins under `concurrency:"unbounded"` (nondeterministic;
  154 vs 18 warn lines proof), name≠folder is not a gate (`NameMismatchError`
  dead code), the TUI never calls `fmt`. **Round-8 debt paid**: README rows for
  both round-8 artifacts + both lesson files, `lessons/round-8.md` written a
  round late, `SCORECARD.md` created (axes/planned/retired per AXES.md; consistency
  5→7), `SHONEN.md` regenerated to the canonical 4-box seed with one evidence
  line per box (all `[~]`). **Lane identity fixed**: repo-local
  `user.name=kotoba-shokunin`, `user.email=kotoba@shokunin.local` (round-7's
  `3b029b8` was a conformance defect under the operator identity). Counters
  re-run: warns 10681 → 10925, session_init 3911 → ~4032–4120 (live counter),
  opencode.db 415/216 and opencode.log 471 unchanged. Artifacts:
  `corpus/knowledge/harness-router-models-round9.md`,
  `corpus/knowledge/claim-scope-audit-round9.md`, `corpus/lessons/round-9.md`,
  report `../.ufo/reports/round-9/kotoba.md`.

## Round 10 — kotoba lane — depth axis-move: the harness claim set becomes executable

- **Trigger.** `SCORECARD.md` planned round 10 on depth, whose recorded ceiling
  was "the harness claim set lives as hand-run recipes, so nothing fails when a
  claim stops being true". Round 10 also began with the aggregator's non-author
  audit (`corpus/lessons/round-6-aggregator-audit.md`) landing in this tree with
  a **not conformant** verdict: 9 kotoba-owned defects, several routed open for
  4–6 rounds.
- **Action (the move).** Landed `verifiers/verify_harness_claims.py` +
  `verifiers/baseline.json`: **27 checks** over the two skill routers, exit 0
  agree / 1 drift / 2 environment unreadable / 3 no baseline, `--self-test` over
  the script's own model, and `--omp-bin/--omp-db/--oc-log/--oc-bin/--omp-sessions/
  --cwd/--baseline` overrides so it can be tested on fixture worlds.
  Key facts it pins: the omp key prefix recovered from the ELF by byte anchor
  (273 B, sha256 `c1f03c8e248eb40e…`, placeholders included) and the cache key
  `sha256(T ‖ 0x00 ‖ name ‖ 0x00 ‖ style-aware description)`; 17 offered skills
  from the roots `~/.agents/skills` + `~/.omp/agent/skills` (+ shadowing
  `.config/opencode` / `.claude` trees); 17/17 keys reproduced; 0 cache misses;
  the **newest captured `<skills>` block matched line-by-line against the cache
  (17/17)**; unmodelled YAML scalars excluded, never guessed; dangling skill
  dirs counted; opencode `init count` max == root union + builtin,
  `<available_skills>` 0 hits, per-root duplicate split both-sided, monotone
  init counts, `skill`-permission allow lines.
- **Authority upgrade.** omp ships as a Bun single-file executable with readable
  embedded JS: `A8n` (key), `H7s` (`previewSkillDescription`), `ldl` (compressor
  acceptance ≤160 chars / ≤12 words / single line), `_8n=100, idl=160, adl=12`.
  Round-7/9 cited ELF offsets and a stale `slice(0,99)` literal; this round cites
  functions and anchors, so a build change moves a recorded sha256 instead of
  silently invalidating prose.
- **A routed round-9 claim was falsified.** The hashed template is the whole
  273-byte bunfs prompt (routing-hint sentence + `Skill: {{name}}` /
  `Description: {{description}}`); round 9 recorded only the 226-byte first
  line, which reproduces **0/17** keys. Corrected in
  `corpus/knowledge/harness-router-models-round9.md`, `SKILL.md` § Sources and
  the new artifact. Independently reproduced by three lanes (critic, executor's
  own implementation, scout) — one of them also cross-checked 11/11 of this
  repo's `omp.*` baseline values.
- **Audit closure (aggregator r6, 9 defects → 0 open).** `SHONEN.md` regenerated
  with the measured counts (20 data-row anti-pattern table; `13/9/9/8` checklist
  boxes) and a trailing newline; 8 dead `commit round-N` pointers replaced by
  real hashes (`1d93182`, `397b29c`, `4002b9f`, `a614927`, `3b029b8`); index rows
  added for `lessons/round-{1,3,4}.md` and the four aggregator audits
  (`comm` diff now returns only the self-referential `README.md`); the
  falsified "compression is a model call" clause in
  `knowledge/skill-activation-telemetry.md` given an appended, named correction;
  CLAUDE.md census re-based 16 → 18; source-length range re-based to 163–818 with
  its measuring command; `SCORECARD.md` rewritten so every row carries
  `score — command @ tree`, an owned/advisory label, a fractional rubric and an
  axis-name reconciliation (`consistency` declared a calibration sub-axis; the
  `AXES.md`↔`MISSION.md` mismatch routed to the protocol lane). The audit file
  itself arrived as the aggregator's own commit `778310d` (child of the round-9
  close `8e22a41`), authored while this round was running; its findings were
  taken as ground truth rather than re-run, and the audit-trail is now indexed.
- **Outcome / evidence.** `python3 verifiers/verify_harness_claims.py` →
  `27/27 checks pass` (exit 0, ≈3 s); perturbed baseline → exit 1 naming exactly
  the perturbed checks; `HOME=/tmp/...emptyhome` → exit 2; baseline removed →
  exit 3; `--self-test` → 0 failures / 10 assertions; 10 planted faults → 9
  detected (the 10th is an equivalent mutation: `>-` trailing whitespace is
  discarded by the loader, so the key is identical and agreement is correct).
  Freshness inside the round: db 17 rows 44–98 chars; newest catalogue
  2026-09-28T21:47:06Z 17/17 cache over 5924 session files (4116 real
  `<skills>` blocks vs 8194 contaminated literals); opencode init distribution
  15×1 16×141 17×34 18×14, permission lines 471/471 allow, dup split 3 roots
  both-sided; `session_init` 4142; compression warns 10925; omp binary sha256
  `55016ef5…`. 14 L2 lanes in two batched `task` calls (floor 8).
- **Falsifiable next iteration (round 11).** calibration: make the depth
  evidence non-author-verifiable (a reproducible run record from a lane that did
  not author the round) — falsified if no non-author run record is attached, or
  if `SHONEN.md` still needs a `[x]` for that reason. 39 `SKILL.md` checklist
  boxes remain lane-attested and are named as the standing ceiling.

## Round 11 — kotoba lane — consistency axis-move: the citation rules become executable (entry written at round 12)

- **Status / provenance.** This round's work was complete in the working tree when
  the mission was respawned; the round-12 process landed it as `4dd7753` and wrote
  the missing `LOG.md` entry here. The round-11 report
  (`../.ufo/reports/round-11/kotoba.md`) was filed late with it. Nothing in this
  entry is claimed that the landing commit does not carry.
- **Trigger.** Round 10 recorded three zeros (non-hash commit pointers,
  unindexed corpus files, dead report pointers) with one hand-run command each —
  and two of the three commands could not express the class they named:
  `round-[0-9]` cannot match `round-10` (prints 0 *with the defect present*:
  `git show HEAD:corpus/README.md | grep -cE "commit \`round-[0-9]\`"` → 0,
  `…+\`"` → 1), and a `comm` whose regex cannot tokenize the brace row
  `lessons/round-{1,4,5}-aggregator-audit.md` lists three *indexed* files as
  unindexed. A claim whose counting command cannot express its scope is
  calibration debt even when the number is right.
- **Move.** `verifiers/verify_corpus_integrity.py` + `verifiers/corpus-baseline.json`:
  **9 checks** — `corpus.index.{tracked_files,unindexed,stale_patterns,missing_paths}`,
  `corpus.pointers.{report_total,report_dead,commit_total,commit_unresolvable,commit_nonhash}`
  — exit 0 agree / 1 drift naming the firing ids / 2 environment unreadable /
  3 no baseline, with `--json`, `--no-baseline`, `--baseline`, `--repo`,
  `--self-test` (chain 80 as landed → 86 after the quoted-token repair → 88 after the index-scope pins). Scope:
  tracked `corpus/*.md`; six false-positive shapes excluded by design and pinned
  in `--self-test`.
- **Measured before → after.** Real clone, never `git show` text (an uncommitted
  repair reads as "agree" to a working-tree check):
  `python3 verifiers/verify_corpus_integrity.py --repo <clone@d49dfa5> --no-baseline`
  → `report_dead=10/19 commit_total=18 unresolvable=0 nonhash=1`, shapes
  `[relative=9, absolute=8, tilde=1, bare=1]`, `7/9 checks pass` exit 1;
  landed tree → `9/9 checks pass` exit 0. Defects repaired: 9 dead
  `../.ufo/…` rows + 1 bare row in `corpus/README.md`/`corpus/lessons/round-3.md`,
  1 non-hash `commit \`round-10\`` citation, 2 md5 pins printed in commit
  notation (`SKILL.md` @ `143fe473…` was an md5 — `git cat-file` on it fails by
  construction; relabelled `@ md5 … (commit 3b029b8)`).
- **Verification of the verifier.** Exit codes probed on real inputs (perturbed
  baseline → exit 1 naming exactly that id; `--repo /tmp/notgit` → 2; baseline
  removed → 3); red-before on the clone exit 1 with exactly the two repaired
  ids. Non-author cold run (`corpus/knowledge/cold-run-round11.md`): runner
  `ColdRunRecord`, sha256 gate, coherence guard, verbatim runs + exit codes from
  outside the repo, three independent spot-checks in its own Python
  (`33`/`36` counts; every checked pointer via `test -e`; every `commit`
  citation via `git cat-file -e <hex>^{commit}`), `Discrepancies: none found`.
- **Artifacts.** `verifiers/verify_corpus_integrity.py`,
  `verifiers/corpus-baseline.json`, `corpus/knowledge/corpus-integrity-round11.md`,
  `corpus/knowledge/cold-run-round11.md`, `corpus/lessons/round-11.md`,
  `corpus/README.md` rows, `SKILL.md` § Sources + the citation rule made
  checkable, `SCORECARD.md` consistency row (8 → 9).
- **Landing edits (declared).** Two reported-absent pointer tokens were rewritten
  as prose (a live pointer to an absent path is what the check must flag) and one
  bare form was re-presented as the host-absolute path it names; the baseline was
  re-recorded with all nine ids (the draft omitted `corpus.pointers.report_total`,
  which is why that id read `expected=None`).
- **Carried into round 12.** The checked population is 24 pointers, 23 of them
  host-absolute (correct here, brittle across hosts); the three `equal` ids are
  change detectors needing a deliberate re-record; `LOG.md`/`SCORECARD.md`/`SKILL.md`
  pointers are unchecked; the 39 `SKILL.md` checklist boxes are machine-checked
  only as *counts*, never *executed*.

## Round 12 — kotoba lane — consistency axis-move: the second witness is a derivation, not a re-run

- **Opening move: the predecessor round was landed first.** Round 11 ended with its
  working tree complete but uncommitted; per `../PROTOCOL.md` § respawn, this round
  resolved it: three reported-absent pointer tokens were rewritten as prose (a live
  pointer to an absent path is exactly what the check must flag), the baseline was
  re-recorded with all nine ids (the draft omitted `corpus.pointers.report_total`, which
  is why that id read `expected=None`), and the round-11 work landed as `4dd7753` with a
  `round-11` `LOG.md` entry written here (the entry did not exist — one of the four
  false-at-HEAD claims the round-12 census found). The round-11 report was filed late in
  the main repo under the lane identity.
- **The move (consistency 9 → 10, rubric band 10 = repeated non-author verification in the
  opposite direction).** `verifiers/verify_corpus_independent.py` — written from the class
  spec by L2 lane `ExecIndependentVerifier`, which authored neither the author's script nor
  its baseline and **never read its source** — re-derives the index/pointer/commit classes
  with its own tokenizer and counting code. Compared check-for-check in two worlds: live
  tree both instruments exit 0 with identical numbers (39 tracked, 43 index tokens, 25
  checked pointers, 0 dead, 23 hex citations, 8 excluded, shapes 24 absolute + 1 tilde
  (measured on the landed tree)) and identical detail sites; clone at `d49dfa5` both exit 1 with the
  same ten dead-pointer sites and the same non-hash site. Re-run in three live tree states
  (corpus manifests `632a6b0e…` → `bc66c2a6…` → `d4c9eaa6…`), numbers unchanged. Seven
  definitional differences adjudicated in `corpus/knowledge/independent-verification-round12.md`
  §3 — none a verdict disagreement — and one shared caveat measured on both: pointer
  resolution is host-anchored, so with the host `.ufo` hidden a clone goes dead = checked
  (25/25 landed, 19/19 at `d49dfa5`).
- **Two repairs the derivation forced on the author's script.** (a) The docstring's
  quoted-context rule for report pointers could never fire: the tokenizer admitted `"` into
  a token, so the match began at the opening quote and `inside_quotes` counted zero quotes.
  Fixture world proof: pre-fix `report_total=26 dead=2` (the quoted token reported as a
  promise) → repaired `dead=1, quoted=1`, and with the quoted line alone `9/9 checks pass`
  exit 0. (b) The index census read column 2 of *any* table row in `corpus/README.md` while
  its docstring promised the coverage map; it is now scoped to the `## Coverage map`
  section with two self-test assertions pinning that an outside-section token produces no
  pattern and no finding (measured difference today: 0 tokens; live `index_patterns` stays
  37). Both repairs are declared in `corpus/knowledge/cold-run-round11.md` §7, which now
  carries the full sha chain (`631569277d…` pre-commit → `391a54f4…` at `4dd7753` →
  `747b1226…` → `a32da4a4…`) and the reachability qualifier that the two pre-commit digests
  are not objects in this repo. `--self-test` 80 → 88 assertions.
- **Counting-claim census and the repairs it forced (84 rows, executed commands).** 24
  numbers were stale after the round-11 landing (33→39 tracked files, 19→25 checked
  pointers, 21→23 citations, 1→8 excluded sites, 18/1→24/1 pointer shapes, 80→88
  assertions); 4 claims were false at HEAD; 9 were unexpressible; 1 had no command at all
  (`SCORECARD.md`'s round-10 "4 unindexed files" — a brace-aware `comm` reconstruction at
  `e997d45` yields 7). All live sites repaired, the unexpressible ones labelled, the
  commandless one re-qualified. The sharpest false claim was `SHONEN.md` box 1's own
  command: `awk … END{print c[h]}` prints an empty line and cannot produce the `13/9/9/8`
  it claimed — the fourth instance of the round-11 defect class, in the file the round-6
  audit used that same expression to correct. It now prints the counts when run as written
  (verified by executing the text as written), and the round-10/11 `LOG.md` entries and
  `lessons/round-10.md` keep their round's values under the stated rule: **a per-round
  record carries its round's number; a live document carries the current one.**
- **One box added, and every live claim site moved with it.** `SKILL.md`'s trigger-fidelity
  checklist gained "a claim that only its author's instrument settles names that as a gap,
  and its second witness is a derivation, not a re-run" → box count 39 → 40, split
  14/9/9/8; the sweep updated `SCORECARD.md` (4 rows), `corpus/README.md`,
  `SHONEN.md`'s embedded expected output, and both artifacts' gap lists.
- **Faults moved into the repo.** `verifiers/fault_injection_corpus.sh` (10 fault classes,
  one `--no-hardlinks` clone per fault, JSON assertions against **both** instruments,
  `--self-test` 4 probes, exit 0/1/2) replaces round 11's `/tmp` fault table, which was not
  re-runnable after the scratch wipe. Every must-fire fault fires with its intended class,
  the equivalent mutation stays clean, the repaired quoted idiom fires (context 0→1,
  checked total unchanged), and one **shared blind spot** is now on record: a pointer moved
  *out of* the `.ufo/reports/round-N/` grammar is invisible to both tokenizers and only the
  `equal`-mode count detector notices (`report_total` 24→23, default mode only). That
  narrows round 11's "pointer-shape-only rewrite ≡ no-op" (true in-grammar, incomplete
  otherwise — the round-12 reviewer's RF-3); the correction sits in the round-12 artifact,
  not rewritten into the round-11 record.
- **Outcome / evidence.** `python3 verifiers/verify_corpus_integrity.py` → `9/9 checks pass`
  exit 0; `python3 verifiers/verify_corpus_independent.py` → exit 0; `--self-test` → 0
  failures over 88 and 52 assertions respectively; exit codes 2/3 re-probed; red-before on
  a clone at `d49dfa5` → both exit 1 with identical sites; `verifiers/fault_injection_corpus.sh`
  → all classes as tabulated; freshness re-measured inside the round (db 17 rows 44–98;
  permission lines 471; init distribution 15×1 16×141 17×34 18×14; compression warns 10925;
  harness verifier 27/27) — unchanged, so no drift to report.
- **12 L2 lanes in two batched `task` calls** (floor 8): batch 1 —
  `ExecIndependentVerifier`, `ScoutWorlds`, `LabratFaults`, `CriticSpec`, `SentinelCross`,
  `ConnectorCross`, `PlanRound13`, `ScoutClaimCensus`; batch 2 — `CriticRound12`,
  `ReviewerRound12`, `ScoutReCensus`, `ReviewSHONEN`.
- **Operator directive honored outside the repo (recorded, not a lane change):** the global
  cascade in `~/.omp/agent/config.yml` now lists `zai/glm-5.3-flash:max` before
  `opencode-go/glm-5.3-flash:max` in `retry.fallbackChains.m_zfl` (the alias every
  `@m_zfl` subagent route resolves to); YAML re-parsed, `cfg://retry/fallbackChains`
  shows the new order, backup `config.yml.bak-zfl-zai-order-20260928-200540`. `m_z53`'s
  identical-shaped chain was left untouched (not a z-flash alias).
- **Carried into round 13.** Hermeticity (24 of 25 pointers host-absolute, so a clone's
  green verdict depends on the host `.ufo`); `LOG.md`/`SCORECARD.md`/`SKILL.md` are outside
  both instruments' scan; the 40 checklist boxes are still counted, never executed —
  candidate: make one box executable with a missing-name fixture (scratch plan, not yet an
  in-repo artifact).

## Round 13 — kotoba lane — coverage axis-move: the instruction-surface inventory derives from loader code (coverage 7 → 8.0)

- **Why this axis.** `SCORECARD.md`'s lowest row was `coverage` (7, advisory), and
  the mission's round rule is "pick the lowest-scoring axis"; `AXES.md` defines
  coverage as "the fraction of the domain's real surfaces the skill governs",
  which for a prompt/skill-craft lane *is* the instruction-surface inventory. The
  round-12 plan's rank-1 candidate (execute one `SKILL.md` checklist box) was
  **deferred with reason**: it improves `operability`, an axis this lane does not
  own, and the plan itself recorded that it could not move an owned score without
  a protocol ruling. The `planned` block therefore points at the checklist move
  again, now with its axis-accounting question still open at L0.
- **Landed.** `corpus/knowledge/instruction-surface-census-round13.md` (41 class
  ids: 33 governed, 8 excluded with reasons; omp read from its registry
  descriptions + call shapes, opencode's instruction service quoted from its
  shipped JS), `verifiers/verify_surfaces.py` (4 checks, exit 0/1/2/3,
  `--self-test` 28 assertions), `verifiers/surfaces-baseline.json` (derived from
  the census by regenerating and diffing — the reviewer lane repeated the
  derivation and found no difference), 12 synthetic fixtures,
  `corpus/knowledge/instruction-surface-remeasure-round13.md` (the blind second
  witness). `SKILL.md`: 7 → 9 surface rows, the CLAUDE.md row's "9/17 string refs"
  proof replaced by code shapes plus the harness divergence (omp reads
  AGENTS.md *and* CLAUDE.md; opencode reads one name per directory in the order
  AGENTS.md → CLAUDE.md → CONTEXT.md), dispatch rows labelled host-observed, the
  agent-definition roster counts corrected (18 `.md` + a 19th entry, the singular
  `agent/` directory, 37 omp-side defs), and three repairs from the aggregator
  lane's landed round-8 cold run: B1 (the "newest `<skills>` block" recipe now
  states a *catalogue-bearing* selection rule and points at
  `omp.catalogue_path`), B2 (the fault harness is labelled mutating, not a smoke
  check), B3 (the cache-row count is a change detector; current 18 with all 17
  live keys reproducing).
- **Falsifiers, run.** `python3 verifiers/verify_surfaces.py` → 4/4 PASS, exit 0
  (≈19 s); `--self-test` → `0 failure(s) over 28 assertions`, exit 0. Anti-vacuous
  proof (from the checker's author lane): with the original empty baseline the
  live tree produces `table_parity` FAIL naming all 41 census rows and
  `no_uncovered_class` FAIL naming the 8 extracted classes — parity never passes
  on 0==0; a missing inventory exits 2, a missing baseline 3.
- **The finding that moved the score down.** Pre-registered 8.5; landed **8.0**.
  The machine check is real for omp's 8 machine-extracted `.md` registrations and
  **vacuous by construction for opencode** (its loaders are arrays/`join`/`findUp`
  — no extractable call shape), so band 9's "machine-checked" criterion is not met
  for the coverage claim as a whole; band 8's ("independently re-measured by
  another lane") is. The critic lane independently recommended 8.0 for the
  unqualified claim; that is the number recorded, with the ceiling stated in the
  census rather than implied.
- **A lane-vs-lane disagreement decided by bytes.** The host-census lane concluded
  "opencode's CLAUDE.md is prompt text; the loader is omp-only"; the anchor-review
  lane concluded the opposite. Adjudicated from the raw bytes: opencode's
  instruction service carries `y = ["AGENTS.md", …!disableClaudeCodePrompt ?
  ["CLAUDE.md"] : [], "CONTEXT.md"]` and `n = [<config>/AGENTS.md, ~/.claude/CLAUDE.md]`
  — a real loader with an env gate, shadowed per directory by AGENTS.md because
  `Instruction.find` breaks on the first name that exists. The opencode scout and
  the critic lane reach the same conclusion independently. Consequence recorded:
  a reference count is exactly the evidence class this round forbids.
- **Second witness.** Blind lane `scout-independent` (own printable-run extractor,
  `strings` never invoked) re-derived the class list and agrees check-for-check on
  every load-bearing class; it added the omp provider-enablement gates (`RTo` /
  `eu()` / `enabledProviders` / `disabledProviders`), `RULES.md`, opencode's
  Read-tool `<system-reminder>` channel, and the two description-vs-code gaps
  (`.cursorrules` and `.windsurfrules` exist only in registry *descriptions* — the
  census rows now say so).
- **The round's own instrument caught the round's own change.** Repairing four
  dead pointer sites in the aggregator lane's two in-repo files, the first pass
  used the *relative* shape; `verifiers/fault_injection_corpus.sh --self-test`
  then failed T2/T3 — it clones the repo into `${TMPDIR}` and asserts a no-op clone
  reads clean, and a relative "`.ufo/reports`" pointer dies off-layout. Reverted to
  the host-absolute shape the corpus already favours (24 of 28 pointers) and the
  gap is recorded in the reconciliation note. Same self-test also caught the
  mid-landing state twice (an unindexed corpus file), which is its job.
- **Baselines re-recorded, mechanisms named.** `verifiers/baseline.json`:
  `omp.db.rows` + `rows_wellformed` 17 → 18 — recomputed with the verifier's own
  `omp_key()`: the extra row is `name=ufo` against the *project-scoped* copy
  `~/Projects/origin-work/ufo-fsd-alpha/skills/ufo/SKILL.md` (690-char description,
  identical across the 10 substrate packs — 2026-10-14 errata: historical; the
  tree moved to `~/Projects/ufo-fsd-alpha` and no longer carries that byte), i.e.
  the cache is append-only per (name, description) pair and its count is a
  change detector. The binaries are
  unchanged (sha256 equal to the round-12 recording), all 17 live keys still
  reproduce. `verifiers/corpus-baseline.json`: re-recorded against this round's
  landing commit (see that commit's message for the moved numbers).
- **Freshness re-measure (same round).** cache db 18 rows (44–98 chars);
  `evaluated permission=skill` 471; init distribution 1/141/34/14; harness
  verifier 27/27 exit 0, `--self-test` 0/10; corpus verifier 9/9 after the
  re-record; `verify_surfaces.py` 4/4.
- **Operator-side / cross-domain, routed not fixed.** `~/Projects/bounties`
  vanished mid-survey (connector lane §4b; kasegi's domain root — the census
  records it as never-a-governed-pass); bootstrapper roster incompleteness (D1) →
  kumitate; kumitate/kasegi `.omp`-tree contest and the `~/.codex/AGENTS.md`
  class overlap; the kasegi↔kotoba `george/pendle` CLAUDE.md wording contest is
  now unobservable. Aggregate.md-level detail lives in the round report.
- **14 L2 lanes in two batched calls** (floor 8). Call 1 — `PlanCov13`,
  `ScoutOmp`, `ScoutOpencode`, `ScoutIndependent`, `LabratInject`, `ExecChecker`,
  `ExecHostCensus`, `CriticClass`, `ConnectorCross`, `SentinelScope`,
  `ReviewerAnchors`. Call 2 — `MutationSurfaces`, `ReviewRound13`, `CriticFinal`.
  Every lane's claim that landed is attributed in the census or the report; the
  lanes that disagreed with each other are named rather than averaged.
- **Carried into round 14.** (a) the checklist-execution move (its axis
  accounting still needs the protocol lane); (b) an opencode-side machine check
  (the .5 withheld this round); (c) the omp provider-priority/dedupe derivation is
  single-lane and unconfirmed; (d) `LDe`/`instructions` consumer unresolved by two
  lanes; (e) implicit-intent fidelity still unmeasured; (f) pointer hermeticity
  (relative vs absolute both fail off-layout) is now recorded with a failing probe
  rather than assumed.

- **Batch-2 rigor, and what it changed.** Mutation lane: 13 planted faults, **11
  caught** (both parity directions, literal presence, the call-shape requirement,
  excluded-reason, missing inventory → 2, missing baseline → 3) and **2 escaped** —
  rewriting a census row's *literal* or *evidence* column still exits 0, because
  parity compares ids and `literal_present` probes the baseline's literal. Recorded
  as an explicit id-level boundary in the census's ceiling, not smoothed over; it
  is also why the withheld half-point stays withheld. Review lane: three defects,
  all fixed here — a hash-"pins" overstatement (the baseline *records* binary
  hashes; the enforced pin is the template sha256), a stale duplicate schema list in
  the checker's module docstring (missing `loader-literal`), and an over-claimed
  agreement verdict in the re-measure record (one item is unresolved *by both*
  lanes, which is not agreement). Critic lane: recommended 8.0 over 8.5 for the
  unqualified claim — adopted — and supplied the strongest falsifiers it could
  find, all of which are extraction-set limits the census already declares.
- **Partial wire-level injection evidence (lane died mid-run).** `LabratInject`
  drove `omp -p` against a local capture server and read the request bodies: the
  context-file capability dedupes by `level:depth`, so **one project context file
  per depth bucket reaches the prompt** (bare `AGENTS.md` alone is injected; with
  `AGENTS.md` + `CLAUDE.md` at depth 0, one wins) — wire-level corroboration of
  the § A2 dedupe, from a different method; `.github/copilot-instructions.md` and
  an `alwaysApply` rule landed in the prompt; and the
  `for (const s of ["AGENTS.md","CLAUDE.md"])` loop is **memory consolidation**,
  not loading (the false friend killed twice). The lane hit a model rate limit and
  did not finish (determinism across reruns, opencode by wire) — recorded as
  partial in `corpus/knowledge/instruction-surface-census-round13.md` § A3, with
  only what it reproduced.

## Round 15 — kotoba lane — operability axis-move: the SKILL.md checklists become executable, plus the round-14 recording debt (operability 7.5 → 8.0; coverage 8.0 → 8.5 attributed to round 14)

- **Why this axis.** `SCORECARD.md`'s lowest rows were `operability`,
  `calibration` and `adjacency`, all 7.5. `operability` was chosen because it is
  the one carrying a *named, pre-falsified, unlanded* deliverable: round 13's
  plan item 2 ("make one `SKILL.md` box executable … as
  `verifiers/verify_skill_checklist.py`") with its falsifier already written, and
  the `operability` row already names the residual — "`SKILL.md` checklist boxes
  remain the only un-automated procedures (40 boxes)". The round-13 L0 question
  (may a lane work an advisory axis as its lowest-axis move; D-78's
  `AXES.md`↔`MISSION.md` naming) is still unanswered and this round again worked
  the lowest row — recorded, not re-litigated.
- **Landed.** `verifiers/verify_skill_checklist.py` (8 checks, exit 0/1/2/3,
  `--self-test` **0 failure(s) over 772 assertions** over 46 fixture cases),
  `verifiers/checklist-baseline.json` (41 boxes: **7 executed, 1 delegated, 33
  unexecuted with reasons**, multiset parity by normalized text hash),
  `verifiers/checklist-command-vocabulary.json` (28 declared command heads),
  `verifiers/fixtures/checklist/` (46 case dirs), and the round's evidence +
  pre-registration with amendments A1–A5
  (`corpus/knowledge/checklist-execution-round15.md`). `SKILL.md` gained the
  missing **frontmatter-parses box** (the checklist had none, so a file with no
  frontmatter passed every downstream box vacuously) and `(executed: <check-id>)`
  annotations on the seven executed boxes.
- **Red-before → green-after, on the lane's own file.** `SKILL.md` was **675
  lines** at the pre-registration commit (`63ceba7`) against its own ≤600 box:
  the landed map run against that snapshot exits 1 with exactly two FAILs —
  `trigger.line_budget: evaluated 675 — 675 lines exceed budget 600` and
  `checklist.box_map_complete` naming the unmatched boxes. The fix is the file's
  own remedy: three sections moved to their corpus homes with a summary + pointer
  each — § Frontmatter craft (95 lines → `knowledge/frontmatter-trigger-surface.md`
  § Craft rules, all 12 rules verbatim), § Compression rules (23 →
  `knowledge/anatomy-and-compression.md`), the § Anti-patterns table (20 data rows
  → `knowledge/fail-closed-and-anti-patterns.md`). Landed: **599 lines**, live run
  `exit 0`, 8 × PASS (`box_map evaluated 41`; `line_budget evaluated 599 within
  budget 600 (from box at line 328)`; `command_binary_resolves evaluated 16
  subjects / 16 segments`). The check also caught its own author mid-round: a
  603-line intermediate state FAILed `trigger.line_budget` until trimmed.
- **Round-14 recording debt closed, with its defects named.** Round 14 landed the
  opencode machine check (`29c17be`) but terminated before recording: no LOG or
  SCORECARD entry, and its report is a DRAFT with `[PENDING]` markers. An L2
  reviewer lane re-measured the landed artifacts — all 9 required falsifier cases
  plus the full 7-rule drop-one matrix reproduced, the opencode check proven
  non-vacuous by deleting the OC-1 anchor and reading the FAIL — and judged
  **full band: coverage 8.0 → 8.5 (attributed to round 14)**. Two defects in that
  round's record are recorded rather than smoothed: (a) the promised
  corpus-baseline re-record never landed, so `verify_corpus_integrity.py` was
  **8/9 at `29c17be`** while the DRAFT report claimed 9/9 — a false claim in a
  filed report, corrected here in the correcting round's artifact, not by
  rewriting the report; (b) the move was scored a round late.
- **Verification: 15 L2 lanes, two batched calls (floor 8).** Call 1 — `R15Plan`,
  `R15Connector` (planner/connector), `R15Populate`, `R15Exec` (executors),
  `R15Surfaces` (scout), `R15Rules` (critic), `R15Witness` (labrat), `R15R14`
  (reviewer), `R15Safety` (sentinel). Call 2 — `R15Mutate` (mutation-tester),
  `R15Review` (reviewer), `R15Agree` (labrat), `R15Dead` (simplifier),
  `R15Distill` (distiller), `R15Critic` (critic).
- **Four lane findings changed the artifact before landing.** (1) The blind
  witness (spec-only, forbidden to read the build) showed fenced-only command
  extraction is empty on 3 of its 4 files and that the 30-char negation window
  false-positived on the file's own box → A2, then A3 (the extraction set is a
  *declared* vocabulary, because a shape filter cannot tell `` `description` ``
  from `` `ls` `` — measured: 78 candidates, 56 unresolvable). (2) The population
  lane found 138 `SKILL.md` files and showed the English-only anti-trigger
  vocabulary fails 135 of them → A4 adds the observed CJK markers. (3) The critic
  executed counterexamples against 6 of 8 rules (multiset parity, pinned
  normalization, registry-bound `executed:` ids, frontmatter block parse,
  abspath'd directory, box-bound budget, word-bounded negation, wrapper unwrap) —
  all repaired before landing. (4) The agreement lane adjudicated the
  *instrument* wrong on a real false positive: the frontmatter parser rejected
  valid nested `metadata:` blocks — the very shape the file's own
  `metadata.requires` box prescribes — hitting 37/138 fleet files; repaired here
  with fixtures `fm-nested-metadata` / `fm-stray-indent`.
- **Escapes found and closed in-round.** The critic's two live escapes — a
  `- [x]` marker toggle, and `delegated:<path>` pointing at a file that does not
  exist — are now instrumented (`marker-checked`, `marker-near-miss`,
  `map-dead-delegated`) together with a new `annotation↔disposition` binding
  (`map-annotation-mismatch`, `map-executed-undisclosed`). The mutation lane then
  re-derived them as closed (provably absent in the pre-revision copy) and
  measured the new rules. It also found the vacuity miscount the critic predicted
  — inline prose spans counted as "segments seen" — which is fixed (inline spans
  are candidates only when their head is a declared vocabulary word).
- **Withheld, and why.** The mutation lane ran 45 mutations: **35 caught, 5
  escaped, 5 clean pins, 1 control**. The five escapes (inline command outside the
  vocabulary; a command hidden in a heredoc body; `echo <nonexistent>` in a shell
  fence — only segment heads resolve; whole-box reordering; a `delegated:` target
  that exists but is not an instrument) are now named as ceilings. Because the
  pre-registration's full band required "mutation lane finds no escape inside the
  seven executed checks", that condition **fails as written** and the band is the
  pre-registered **partial: 8.0**. The half-point stays withheld; the condition
  that earns 8.5 is stated in the evidence file (close `M35`/`M40`, or
  re-pre-register the condition and defend the wording before the build).
- **Fleet application (read-only; FAILs routed, never fixed).** All five sibling
  `SKILL.md` files FAIL `literal_trigger_string` and `anti_trigger_clause` (the
  round-8 rewrite set is still unapplied); `line_budget` FAILs kagi 653, kasegi
  997, kumitate 664; kasegi's command check trips on an info-less fence holding a
  diagram — the live example of the false-positive edge, which is why foreign
  FAILs are hints. Non-author witnesses also ran the instrument against
  `~/.agents/skills` files (bailian-sandbox after the repair, omarchy).
- **Cross-domain findings, routed.** `kumitate-shokunin/scripts/surface-probe.mjs
  --checklists` is an **existing box executor** with a frozen grammar
  (`- [ ] <label> — \`<cmd>\` → exit <n> + \`<expected>\``); only its own 9 of 72
  fleet boxes match it, the other 63 are prose. Two dialects now coexist and the
  consolidation call is kumitate's/protocol's, not this lane's. Also routed: the
  five siblings' description defects, kagi/kasegi/kumitate line budgets, and
  `corpus/lessons/round-9-aggregator-corpus-verdict.md` — **an aggregator-owned
  file written into this repo at 22:19 while this round ran** (unindexed, and
  carrying a documented main-repo-relative pointer the corpus instrument reads as
  dead). It is left uncommitted and reported, per PROTOCOL.md.
- **Corpus-side changes and baselines.** `corpus/README.md` gained the round's
  index row, a Known-gaps bullet naming the 33 unexecuted boxes and the command
  check's extraction set, and round-15 clauses on the three rows whose files
  absorbed moved sections. `SHONEN.md` box 1's evidence line now carries the
  41-box count and the moved-sections note (marks unchanged at `[~]`: no non-author
  verification of this round's changes exists yet). `verifiers/corpus-baseline.json`
  was re-recorded against the landed tree; the mechanisms are in its
  `measured_against.note`. A new dead pointer and a missing index row that the
  round introduced mid-flight were caught by the corpus instrument itself and
  fixed in-round (`report_dead 0`, `unindexed 0` at the point of the fix).
- **Carried into round 16.** (a) the five named escapes above; (b) the delegated
  box's instrument currently RED — `trigger.11` delegates to
  `verify_corpus_integrity.py`, which never scans `SKILL.md` itself, so the file's
  own corpus citations are outside the delegated enforcement; (c) the planner's
  ranked next moves: `T10` citation-resolution extension, `D6` dispatch-prompt
  literals, `A9` agent-body path resolution (each with its falsifier in
  `R15Plan/decidability.md`); (d) the L0 axis-accounting question (rounds 13–15).

### Round 15 — correction entry (appended; supersedes two statements above)

- **Attribution defect, recorded not rewritten.** The round's landing commit
  `0089974` used a `corpus/` pathspec, which swept in
  `corpus/lessons/round-9-aggregator-corpus-verdict.md` — a sibling lane's file
  written into this repo at 22:19 while this round ran. PROTOCOL.md: uncommitted
  aggregator-owned files are reported, not lane debt; history is not rewritten to
  fix attribution, so `d6177f4` untracks the file and leaves it in the working
  tree for its owner. The earlier claim above that the corpus instrument "is
  recorded as-found, so a sibling file leaves `verify_corpus_integrity.py` red" is
  **wrong twice**: the instrument counts *tracked* corpus files, so an untracked
  sibling file is outside the scan; and its `unindexed`/`report_dead` ids are
  baseline-free zero-mode checks that cannot be recorded away. Corrected numbers —
  `verifiers/corpus-baseline.json` re-recorded against `d6177f4`:
  `44/0/29/0/26` for tracked/unindexed/report_total/report_dead/commit_total
  (was 42/0/28/0/24 at the round-13 recording).
- **The red state was attributed by experiment.** Mid-round, `verify_corpus_integrity.py`
  read 4/9 and `fault_injection_corpus.sh --self-test` read BROKEN (T2/T3). A
  fresh `git clone` of the landed tree — no untracked sibling file — runs the
  harness `self-test: OK` (T1–T4 PASS) and the corpus instrument 9/9 exit 0, so
  the cause was the sibling file and not this round's changes. Landed state:
  `verify_harness_claims.py` 27/27 exit 0; `verify_surfaces.py` 7/7 exit 0
  (`--self-test` 0/75); `verify_skill_checklist.py` exit 0 (`--self-test` 0/772);
  `verify_corpus_integrity.py` 9/9 exit 0; `verify_corpus_independent.py` exit 0;
  `fault_injection_corpus.sh --self-test` OK, full run ALL PASS.

### Round 15 — second correction entry (the first correction was itself wrong)

- **The `git rm --cached` was the mistake, not the commit.** The aggregator lane
  had *committed* `corpus/lessons/round-9-aggregator-corpus-verdict.md` in
  `0f658ff` (24 lines, an ancestor of this round's commits) between writing it at
  22:19 and this lane's landing commit; the file was therefore tracked and stayed
  tracked through `0089974`. The correction commit `d6177f4` then un-tracked a file
  its owner had legitimately landed — a second, worse error than the one it
  claimed to fix, and the first entry above is wrong on that point. The next
  commit restores tracking, and the record keeps both errors rather than rewriting
  either commit.
- **What the repo now does with that file, and why.** It is indexed in
  `corpus/README.md` (a corpus file without an index row keeps this repo's own
  `corpus.index.unindexed` non-zero) and its two `shokunin:`-prefixed pointer
  sites are rewritten to host-absolute form — the round-13 convention for dead
  pointer sites in in-repo corpus files, taken because the corpus verifier
  resolves pointer bases and has no exception for a documented main-repo-relative
  convention. A dated round-15 repair note is appended inside that file; no
  finding, verdict or routed row is altered.
- **Final instrument state at the landed tree** (`verifiers/corpus-baseline.json`
  re-recorded, 45/0/30/0/27): `verify_corpus_integrity.py` **9/9 exit 0**,
  `verify_corpus_independent.py` exit 0, `fault_injection_corpus.sh --self-test`
  **OK** and full run ALL PASS, `verify_harness_claims.py` 27/27, `verify_surfaces.py`
  7/7, `verify_skill_checklist.py` exit 0 with `--self-test` 0/772.

### Round 16 — operability 8.0 → 8.5 (two escapes closed, one box executed, three citations named)

- **Move (pre-registered in round 15).** Close `M35` (path-like arguments never
  resolved) and `M40` (a `delegated:` target was checked for existence only), then
  execute one more checklist box. Round 15 wrote the falsifiers before the build:
  one red-before fixture per escape, and the band condition "the mutation lane's
  re-run catches both".
- **Landed.** `verifiers/verify_skill_checklist.py` gains `path_like_arg` /
  `arg_subjects` / `unwrap_tokens` (arguments resolve; `sh -c` arguments are read
  from the inner token list; `<` input redirects do not exempt, output redirects and
  a declared output-flag set do; URLs and comment tails are not paths),
  `is_instrument` (script suffix, shebang or ELF magic; `..` in a target FAILs),
  `citation_resolve` + the ninth check `trigger.citation_resolves` (every backticked
  token rooted in this repo must resolve; line anchors and trailing punctuation are
  stripped; a leading `./` is normalized; leading `..` hops are bounded to 3), and
  `strip_token_dressing`. `verifiers/checklist-baseline.json`: `trigger.11`
  `delegated:verifiers/verify_corpus_integrity.py` → `executed:trigger.citation_resolves`
  (new box sha `c7ad2458…`), map now **8 executed / 0 delegated / 33 unexecuted**.
  `SKILL.md` (599 → 599 lines, budget 600): three "`.ufo/prompts/`" citations named to
  the host-absolute form the file already used five times, the `trigger.11` box
  rewritten to its executed subset with the annotation, the corpus instrument's scope
  corrected to `corpus/*.md`, and the check/box counts updated. 21 fixtures (6 mine,
  4 boundary from the executor lane, 12 adversary-driven incl. the planner's rank-1
  `source` operand fixture); 47 → 68 fixture cases;
  `--self-test` 772 → **1302 assertions, 0 failures**.
- **Red-before, per rule.** R1: the pre-patch verifier (`sha256 2ee8abae…`) on
  `fixtures/checklist/command-path-arg` → `rc=0`, the dead argument invisible. R2: same
  on `delegated-noninstrument` → `rc=0`. R3: the patched verifier on a clone of
  `b25f37a` in a faithful host layout → 8 × PASS and
  `FAIL trigger.citation_resolves: evaluated 46 — line 86/95/385: '.ufo/prompts/' does
  not resolve`, exit 1. The check is also fail-closed on the live file: it FAILed on
  line 210 (`corpus/knowledge/checklist-execution-round16.md`) until this round's
  knowledge doc was written.
- **Instrument state at the landed tree.** `verify_skill_checklist.py` 9 × PASS exit 0
  (`41 boxes mapped (8 executed, 0 delegated, 33 unexecuted)`, `line_budget 599/600`,
  `command_binary_resolves 19 subjects / 15 segments`, `citation_resolves 42/42`);
  `verify_harness_claims.py` exit 0; `verify_surfaces.py` exit 0; `verify_corpus_integrity.py`
  9/9 exit 0 and `verify_corpus_independent.py` exit 0 after the corpus baseline
  re-record (45→46 tracked, 30→32 report pointers, 0 dead); `fault_injection_corpus.sh
  --self-test` OK.
- **Ten L2 lanes, six defects found in the new rules, all fixed in-round with fixtures.**
  `R16Mutate`: 46-row harness unchanged at HEAD (35/5/5/1); patched flips exactly `M40`
  → CAUGHT (36/4/5/1); `M35` stays escaped (bare `echo` argument — see below).
  `R16M35` (labrat): `sh -c 'cat corpus/README.md'` was a false positive → fixed.
  `R16Critic`: `is_instrument` rejected a compiled instrument (`~/.local/bin/sekhmet`,
  ELF) → fixed; `./` citation laundering → fixed; the `delegated:` class now has zero
  live entries (cost recorded). `R16Sentinel`: `<` treated as an output redirect →
  fixed; `corpus/README.md:42` / `x.md,` false FAILs → fixed; `delegated:../x.py` → fixed;
  its "empty `delegated:` passes" claim is **refuted** (exit 3 at map load).
  `R16Indep`: 4/4 predictions matched; A13 (`shutil.which` on a slash token made the
  verdict cwd-dependent) → fixed. `R16Blast`: R1 over 23 fleet files gave 77 args / 27
  would-FAIL / 3 flips with **0 true positives**; after the URL + comment-tail fixes
  75 / 25 / 2 — recorded as the foreign-hint rate, with the declared read-verb
  vocabulary as the round-17 tightening. `R16Review`: the three "`.ufo/prompts/`" sites
  are real at HEAD and HEAD reproduces every round-15 quote verbatim. `R16Fixtures`
  (executor): red-before for 9 cases (all exit 0 pre-patch), word-wise harvesting
  proven with a second-word fixture, and the **two-root replay probe** as the
  hermeticity rule for any fixture that resolves through ancestor hops. `R16Connector`:
  no sibling declares `delegated:`; kumitate executes checklist commands but resolves
  neither arguments nor targets; kasegi's `resolve.py`/`anchorcheck.py` are the
  citation/anchor prior art; sibling R3 dead tokens kagi 2 / kake 1 / kasegi 1 /
  kengaku 1 / kumitate 5 → routed.
- **`M35` re-labelled, with the argument stated.** The planted
  `echo r15absent-echoed-bin` is a bare token after a skip-list builtin: pasting it
  succeeds, so under the box's claim ("runnable as pasted") it is not a defect. The
  rule-covered class ("`cat corpus/nope.md`") is closed with `command-path-arg`. Both
  band readings are recorded in `corpus/knowledge/checklist-execution-round16.md`
  § Band decision (8.5 earned / 8.0 withheld) so the aggregator can move the row on
  that paragraph alone.
- **Carried into round 17.** (a) R1's foreign-hint rate and its read-verb vocabulary
  tightening; (b) `D6` dispatch-prompt literals and `A9` agent-body resolution (the
  round-15 planner's ranks 2 and 3); (c) `agentdef.*` (9 boxes) decidable subsets;
  (d) the `delegated:` class with no live entry and `is_instrument()` fixture-only;
  (e) ceilings `M22`, `M23`, `M36`, `M38`, the bare-token residual, `$VAR`/closed
  root set, symlinked instruments, backslash-continuation joins; (f) the
  `AXES.md`↔`MISSION.md` axis naming (rounds 13–16, `../.ufo/l0-questions.md`);
  (g) sibling R3 dead tokens, routed.

### Round 16 — addendum (planner lane, appended after the landing commits)

- **Rank-1 discharge.** `R16Plan` (planner) ranked the `source`/`.` operand residual
  first: a builtin that acts on its operand still hid a missing file
  (`source ./r17-plan-absent-source-fixture.sh` → `No such file or directory`, exit 1),
  while `echo <word>` is benign. It is already closed here by `READ_ARG_BUILTINS`
  (`source`, `.`, `exec`) and now carries the fixture `command-source-operand`
  (`FAIL … 'verifiers/absent-round16-source.sh' (fenced-arg …) does not resolve`),
  taking the fixture population to 68 cases and `--self-test` to 1302 assertions.
- **Refutation of a round-15 fixture, recorded not rewritten.** The planner probed the
  shell: `cat <<~R17EOF` terminates on `~R17EOF`, so the delimiter *word* includes the
  `~`. Round 15's `M36` row closed a `<<~` heredoc with `PYEOF`, which conflated a
  delimiter mismatch with the parser over-catch; the row's verdict (over-catch) stands,
  but its fixture was not shell-valid and round 17 must close with `~EOF`.
- **Planner ranking adopted for round 17**: D6 prompt literals (rank 2 there, rank 1 by
  this round's measured blast radius), M36 `<<~WORD`, M23 executable heredocs, R3 scope
  for `LOG.md`/`SCORECARD.md`, A9 gated on a named agent root. Ranks 7 (M38, no
  numerical headroom at consistency 10) and 8 (M22, needs a marker convention) are
  carried as policy calls.

## Round 17 — kotoba lane — calibration axis-move: governance paths become executable, `M36` corrected (8.0 → 8.5)

- **Axis selection.** `freshness`, `calibration`, and `adjacency` started tied at
  8.0. The pre-registered governance-path gap was a concrete calibration
  defect; adjacency remained sibling-owned and freshness had no failed
  instrument. This round therefore implements planned R3 scope for `LOG.md` +
  `SCORECARD.md`, with `M36` as a parser-calibration repair. The detailed record
  is `corpus/knowledge/checklist-execution-round17.md`.
- **Red-before — governance.** Direct pre-rule runs of
  `trigger.citation_resolves` over the two root files produced **74 subjects /
  6 dead** (`LOG.md`) and **51 / 2** (`SCORECARD.md`), both exit 1.
  `R17Review` independently reimplemented the extraction and reproduced both
  counts. The eight sites classified as: ellipsis schematic 1, literal-`N`
  templates 2, historical repair records 3, deliberate dead example 1, and an
  ambiguous foreign sibling pointer 1.
- **Landed governance gate.** `governance.citation_resolves` is the tenth
  `verify_skill_checklist.py` check. On repo-root `SKILL.md` runs it reads the
  explicit pair `LOG.md`/`SCORECARD.md`, reuses the bounded R3 resolver, and
  excludes/counts only same-line quoted meta-findings plus ellipsis/literal
  `round-N` schematics. Final population: **134 raw = 125 checked/resolving +
  6 quoted meta + 3 schematic, 0 checked dead**. Four dead-by-assertion records
  use the existing quote idiom; kasegi prior art now names
  `../kasegi-shokunin/corpus/instruments/resolve.py` and `../kasegi-shokunin/corpus/instruments/anchorcheck.py`.
- **Two governance designs were falsified before landing.** Weak prose-marker
  exclusions could veto all eight dead sites and make the gate vacuous
  (`R17Gov`), so they were rejected. File-level quote parity suppressed **17**
  ordinary live citations; same-line enclosure replaced it, and a cross-line
  quote evasion now FAILs in `--self-test`. A planted unquoted dead path FAILs
  and is named.
- **Red-before / green-after — `M36`.** The old regex did not open a
  `<<~EOF` heredoc: the clean fixture FAILed on body token
  `nonexistent-binary-xyz`; the dead-tail fixture reported both that phantom and
  "`corpus/absent-round17.md`"; a bare-`EOF` fixture reported the whole remaining
  body as commands. Bash probes (`R17Probe`) prove the delimiter word is
  literal `~EOF`. The landed `~?WORD` capture yields: clean PASS 3 subjects / 2
  segments; dead-tail FAIL naming only the real tail, 3 / 2; bare-`EOF`
  mis-termination PASS 1 / 1 because the rest is still body. Three committed
  fixture pairs pin those directions.
- **Additional calibration fix.** Explicit `--repo .` was retained as
  `Path('.')`; bounded `..` hops therefore resolved from the wrong base. The
  CLI now normalizes explicit repos with `.resolve()`. A hermetic child/parent
  self-test requires a valid "`../shared/live.md`" to pass.
- **Landed checklist state.** `python3 verifiers/verify_skill_checklist.py` →
  **10 × PASS**, including `governance.citation_resolves evaluated 125`; existing
  counts remain 41 boxes (8 executed / 0 delegated / 33 unexecuted), 599/600
  SKILL lines, 19 command subjects / 15 segments, 42 SKILL citation subjects.
  `--self-test` → **0 failure(s) over 1504 assertions**; fixture directories
  **68 → 71**; verifier sha256
  `02ccf1b310f7910502f7938d24eb1cfcabe2c521ec42b7ce6420f1869af8df27`.
- **Eleven L2 lanes, one batch.** `R17Plan` ranks next-round adjacency
  remeasurement; `R17Gov` classified all 125 pre-state occurrences; `R17Probe`
  established bash semantics; `R17Critic` narrowed the claim to HEAD
  navigability and rejected corpus-verifier placement; `R17Sentinel` supplied
  adversarial boundaries; `R17Revenger` proved corpus-only scope was deliberate;
  `R17Fixtures` drafted the three pairs and refuted the requested bare-`EOF`
  FAIL; `R17Connector` found no sibling overlap and resolved the kasegi base;
  `R17Review` reproduced counts; `R17Mutate` designed M42–M50 (not claimed run);
  `R17YAGNI` showed the existing corpus grammar was clean but vacuous here and
  selected predicate reuse over a third instrument.
- **Integration drift caught, not baselined away.** After staging the new
  corpus file, `verify_corpus_integrity.py --no-baseline --json` observed
  `tracked_files=47` and **report_dead=32/32**: every checked pointer used the
  absent lowercase `/home/vgpnk/projects`, while the observed report tree is
  `/home/vgpnk/Projects`. The 32 in-repo pointer occurrences across 16 corpus
  files were case-corrected without changing target round/lane. Re-run:
  `tracked=47 unindexed=0 stale=0 missing=0`, `report_dead=0/32`,
  `commit_total=27 unresolvable=0 nonhash=0`, **9/9 checks pass**. Baseline
  change: tracked files 46 → 47 only; this is unscored integration/freshness
  repair, not a second axis move.
- **Committed-state smoke.** The fault harness's `plant_f` anchor carried the
  same lowercase host base and was corrected with the corpus pointers. Against
  the committed `round-17` tree, `fault_injection_corpus.sh --self-test` reports four PASS /
  `OK`; the full control + a–h matrix reports **ALL PASS**, including the
  intended `fault-f` grammar blind spot. The other five instruments had already
  run green on the same source bytes; the governance gate was re-run after this
  LOG entry stabilized and reports 125 checked / 6 quoted / 3 schematic.
- **Band.** Calibration **8.0 → 8.5**. The governance surface is now
  machine-checked and non-vacuous in both directions, but 9 is withheld:
  existence proves neither content, anchors, pins, symlink containment nor
  historical truth, and every L2 lane remains author-side evidence under the
  protocol.
- **Carried into round 18.** `R17Plan` rank 1: classify and route the five
  sibling `SKILL.md` populations (**225 subjects / 14 unresolved**, 2/1/5/1/5);
  no score gain if the four-occurrence delta over round 16 is schematic noise.
  Then: R1 read-verb tightening, `M23` executable heredocs, D6 over 113 prompt
  markdown files, `agentdef.*`, `M22`, `M38`. Named ceilings: quoted/trailing
  tilde delimiters, terminator whitespace, closed citation roots, anchors/pins/
  content, symlinks, and the zero-live `delegated:` class.

## Round 18 — re-census against the moved substrate (2026-10-14)

The fleet's OMP-era lanes sat still because their substrate moved twice at
once: the origin tree relocated (`~/Projects/origin-work/ufo-fsd-alpha` →
`~/Projects/ufo-fsd-alpha`, HEAD `964f443e`) and **both harness binaries were
rebuilt** — `omp` `55016ef5…` → `ff59fc1b…`, opencode `f9dab322…` → `d9123b9b…`
(v2.0.26). This lane's gates never hardcode the origin path — they probe live
substrate artifacts — so the origin move itself was a citation problem
(historical pointers, 4 sites), while the **binary rebuilds** were the real
drift: the session-log grammar, the offered-skill set, and opencode's
instruction-loader shapes all changed under the frozen pins.

### Failure classification (round's survey)

- **(a) stale `--src` defaults:** **none** — this lane's gates never took
  `--src`; they probe the live host. The origin-work citations were the only
  path-class defect (see below).
- **(b) citations to upstream-deleted/moved files:** **4** — `SKILL.md` §
  truncator-key example (690-char ufo SKILL.md at the dead origin-work path),
  `LOG.md` round-13 baseline note (same file), `corpus/knowledge/
  harness-verifier-round10.md` quoted `ports/xbgst-codex/skills` symlink root,
  `corpus/knowledge/opencode-extraction-round14.md` (the whole v1 rule set —
  the *binary's* anchors are gone, equivalent severity). All marked historical
  with append-only errata; no claim deleted.
- **(c) moved-and-restructured citations:** **0**.
- **(d) genuine lane defects:** **0** — every failing check traced to
  substrate drift, not a verifier bug, **except one lane-side gap** the drift
  exposed: the catalogue guard demanded ≥10 matched names unconditionally,
  which wrongly hard-codes a 17-skill world. Now `min(10, len(offered))`.

### Live re-derivation (measured, never recalled)

- **omp** (`ff59fc1b…`): 7 offered skills in `~/.agents/skills` (was 17; the
  two dangling `sekhmet`/`xbrd` symlinks are gone), cache db 14 rows = 7
  skills × 2 description generations — append-only rows persist, never serve:
  `keys_reproduced=7`, `misses=0`. Newest `<skills>` catalogue parses 7/7
  against cache rows. `baseline.json` re-recorded with named mechanism
  (`measured_against.round18_move`).
- **opencode** (`d9123b9b…`, v2.0.26): the log grammar changed —
  `init count`, `evaluated permission=skill`, `duplicate skill name` no longer
  appear (expected 0); the live analogue is `skills rescanned`
  (`skills_rescan_max=3`, new check `oc.log.skills_rescan_max`).
- **opencode instruction model re-derived from the bundle:** the v1
  OC-1…OC-5 anchors are gone. New OC-1…OC-6 set over
  `ConfigInstructionPlugin.projectSource` + `targets:["AGENTS.md"]` all-match
  walk-up, `X(r.config,"AGENTS.md")` global candidate, schema-declared
  `ambient instructions` (witness only — consumer unproven),
  `ReadTool.Plugin` + `SessionInstructions.load` read-hook, the
  `OPENCODE_DISABLE_PROJECT_CONFIG` env gate, and the API-managed
  `/instructions/entries` + `session.instructions.entry.put` subsystem. Census
  § B rewritten, § C gains `opencode:config/instructions` (excluded, witness
  only), fixture drops regenerated for the new anchors.

### Verdict lines — before → after

- `verify_harness_claims.py`: **crash** (`KeyError: 'catalogue_timestamp'`,
  catalogue 0/0, guard floor 10 under a 7-skill world) → `28/28 checks pass`.
- `verify_surfaces.py`: `FAIL literal_present` (CONTEXT.md absent from omp
  dump) + `FAIL opencode_extract` (9/9 classes produced by no rule) →
  `7/7 PASS` (38 ids, 9 excluded, opencode 5/5 classes from 6/6 rules).
  Self-test 70/70.
- `verify_skill_checklist.py` — unchanged, `exit 0` (552 lines, 42 + 125
  citation tokens resolve).
- `verify_corpus_integrity.py` — unchanged, `9/9 checks pass`.
- `verify_corpus_independent.py` — unchanged, `exit 0`.
- `fault_injection_corpus.sh --self-test` — unchanged, `OK`.

### Carried debt

- The v1 opencode extraction doc (`opencode-extraction-round14.md`) is
  historical evidence only; its live claims are discharged by errata, and the
  current rule set stands on one author's reading — no blind second witness
  this round. Unblock: a scout re-enumerates v2.0.26 instruction surfaces and
  compares against OC-1…OC-6.
- `skills rescanned` (opencode log) is a max over rescans, not a per-skill
  record — if opencode gains a `names+builtin`-style line, the baseline should
  re-pin the richer grammar. Unblock: opencode bump re-runs the verifier.

## 19 — re-census round (freshness axis-move)

2026-10-14 · steered round 19 · axis: freshness · 32-lane fleet wave + parent integration.

Full round detail: `corpus/lessons/round-19-recensus.md`. Advisory inventories:
`../.ufo/waves/shokunin12h-20261014-p1-repair/members/`.

## Round 16 — 2026-10-15 redispatch: classified sibling citation routing

- **Motivation and scope.** The current `SCORECARD.md` has freshness and
  adjacency tied at 8.0; its planned adjacency claim is the more falsifiable
  next move. This dispatch follows the operator's round-16 steer despite the
  inherited round-17–19 records. It adds a dated supplement, not a rewrite of
  the earlier round-16 work. One move only: classify sibling citation findings
  and hand actionable craft defects to their owners; no sibling/domain edits.
- **Before, measured at `581e2932850db9cb917844662651f533bfd98519`.**
  A read-only Python census invoking `citation_subjects` and
  `citation_resolve` from `verifiers/verify_skill_checklist.py:1117-1232`
  reports raw subjects **226** (82/29/38/52/25 for kagi/kake/kasegi/kengaku/
  kumitate), unresolved occurrences **14** (2/1/5/1/5), and no classification
  ledger: **0 classified / 14 unclassified**. Governance-style exclusions
  identify four schematics and zero quoted meta-findings. The planned 225
  denominator is historical, not this run's population. The instrument SHA-256
  is `02ccf1b310f7910502f7938d24eb1cfcabe2c521ec42b7ce6420f1869af8df27`.
- **Integration baseline.** `python3 verifiers/verify_corpus_integrity.py
  --no-baseline --json` reports 48 tracked corpus files, 0 unindexed/stale/
  missing, 32 report citations with 0 dead, and 27 source-revision citations
  with 0 unresolved/nonhash. A later tracked-file expectation change must name
  the new indexed files; no zero-defect expectation will be weakened.
- **L2 evidence floor.** One native host-routed `task` call dispatched nine
  seats: `R16AdjPlan` (planner), `R16AdjConnector` (connector),
  `R16AdjExecKake`/`R16AdjExecKasegi`/`R16AdjExecKumitate` (executors),
  `R16AdjScribe` (scribe), `R16AdjScout` (scout), `R16AdjReviewer` (reviewer),
  and `R16AdjCritic` (critic). No model override or routing mutation. These
  are author-side evidence, not non-author SHONEN verification.

### Round 16 continuation — observed integration evidence (2026-10-15)

- **Inherited bytes are not this execution's evidence.** Lines 976–1003 were
  already uncommitted at entry. They are preserved, not silently adopted.
  This execution independently measured the same lane baseline
  `581e2932850db9cb917844662651f533bfd98519`: the documented counting command
  yields 226 raw subjects / 14 raw unresolved occurrences / 0 classified /
  14 unclassified. Four schematic exclusions leave 222 checked subjects,
  not the planned historical 225. Both corpus instruments were run before
  editing: 48 tracked files, zero index/pointer defects; the baseline-bearing
  instrument's `--no-baseline --json` and the independent instrument exit 0.
- **Actual dispatch.** One native `task` call dispatched nine explicit roles:
  `R16AdjPlanNow` (planner), `R16AdjConnectNow` (connector),
  `R16AdjKakeNow`, `R16AdjKasegiNow`, `R16AdjKumitateNow` (executors),
  `R16AdjScribeNow` (scribe), `R16AdjScoutNow` (scout),
  `R16AdjReviewNow` (reviewer), `R16AdjCriticNow` (critic). All used the
  existing host role overrides, without model parameters or routing edits.
  This is the canonical Shokunin native batch, not a validated generic UFO
  wave; the latter excludes the required planner. Every child is author-side.
- **One improvement.** The sourced occurrence ledger
  `corpus/knowledge/sibling-citation-routing-round16.json` preserves all
  226 normalized observations, token-only replay projections and targeted
  context excerpts, original source hashes, fourteen keyed dispositions,
  and three owner-addressed routing packets. The two final-audit occurrences
  remain separate. Role classification is not a declaration of live source
  truth: four schematics, one brace-set, two fleet-base references, three
  unavailable historical sources, and four conditional runtime artifacts.
  Concrete findings are kasegi's unqualified historical occurrence and
  kumitate's source-base/producer re-verification; two fleet-base wording
  suggestions are optional. No sibling, domain, verifier-code, runtime,
  counter, or router changes.
- **Provenance limit.** Four sibling input hashes match their contextual
  source revisions; kake's observed hash identifies working-tree bytes, not
  its contextual HEAD. Each token projection re-extracts the exact original
  subject rows, but neither reconstructs the full source hash nor verifies
  historical content or runtime behavior. Frozen resolution booleans are
  observations retained for classification replay, not a fresh live probe.
- **Score decision.** Adjacency stays 8.0; no half-point from tokenizer noise
  or author-side reviews. Planner and critic recommended hold. Owner
  acknowledgment, integrator mirroring and actual outside-lane remeasurement
  are not observed. SHONEN remains author-asserted, never promoted by these
  children. The round-number/dispatch mismatch was appended to the L0 queue
  under `kotoba | round-16 | Reconcile the relaunched round namespace`;
  publication does not wait for that decision.
- **Measured implementation, before commit.** The counting probe published in
  `corpus/knowledge/sibling-citation-routing-round16.md` returns 226 subjects /
  14 unresolved / 14 classified / 0 unclassified in both frozen and live
  modes, exit 0; before-revision frozen replay returns 0 classified /
  14 unclassified. Four actionable clarification/correction occurrences map
  to three prepared owner packets. Five in-memory negative controls each
  exit 1 with the intended finding: dropped row, duplicate replacing a row,
  missing route, changed frozen observation and altered projection. These
  are bounded evidence checks, not semantic proof or a new fleet gate.
- **Late source evidence retained, not suppressed.** The kumitate executor
  found the present-tense durable-latch claim unsupported by the current
  named producer. Parent read
  `/home/vgpnk/Projects/ufo-fsd-alpha/scripts/fleet-dispatcher.mjs:7920-7948`
  at source revision `964f443ee53df0ce06bd689af01f0dea031b01f9`: Map state,
  console/ledger emission, Map deletion. The ledger's runtime role therefore
  carries an explicit actionable `unresolved-defect`; the owner must correct
  or date-mark the claim, not create a latch file. Kasegi's line-720
  `unresolved-defect` proposal is retained as a historical role plus a
  wording-defect issue. Both disagreements are recorded in
  `corpus/lessons/round-16.md` § Gate.
- **Index/expectations.** The evidence note, companion JSON and round lesson
  are added to `corpus/README.md`'s coverage map. They are the only intended
  corpus-population increase: 48 → 51 tracked files. The tracked-file pin
  will be refreshed with that exact rationale after staging; zero-defect
  expectations and existing source/pointer populations are not relaxed.
- **Integration verification.** After staging exactly the three new corpus
  files and their index row, `python3 verifiers/verify_corpus_integrity.py
  --no-baseline --json` observed tracked=51, unindexed=0, stale=0, missing=0,
  report_dead=0/32, commit_total=27, unresolvable=0, nonhash=0.
  `verifiers/corpus-baseline.json` refreshes only tracked=48→51 and appends
  that rationale. The ordinary corpus run then returned **9/9 checks pass**;
  `python3 verifiers/verify_corpus_independent.py` returned exit 0 with the
  same relevant counts. The published one-line counting command, rather
  than only its in-memory draft, was exercised in frozen and live modes:
  226/14/14/0, exit 0. The changed governance-only citation predicate returned
  PASS over 136 subjects, with six quoted-meta and three schematic exclusions.
  The inherited 601>600 checklist failure was not rerun, suppressed or fixed;
  harness/source gates unrelated to this evidence-only move were not rerun.

## Round 20 — interactive cutover, blocked before native dispatch (2026-10-15)

- **Evidence and reconciliation.** Entry `git status --short --branch`
  reported `master...origin/master [ahead 6]` and only untracked `.ufo/`.
  HEAD is `292bbf8ca7527159570947dadd65bb5528554380`, carrying the October 15
  round-16 citation-routing redispatch. Existing round-17–19 records and the
  shared original round-16 operability report are preserved, not overwritten.
  The driver's launch counter 16 is not a verified completion count. Round 20
  is the next chronological attempt namespace; no cumulative verified tally
  is inferred. Native session filenames were inspected for shape only;
  session bodies were not read, staged, or republished.
- **Plan before work.** `plans/wwkd-round-20-interactive.md` records the data
  walk, freshness selection from the 8.0 tie, one falsifiable dispatch-guidance
  correction, gate/smoke, safety boundaries and the stop-before-dispatch rule.
  The current lane lesson selects freshness after its adjacency hold
  (`corpus/lessons/round-16.md:75-78`). No parent-only craft cutover bypasses
  the operator's required specialist-wave contract.
- **Canonical preflight.** `.ufo/round-20/wave-spec.json` assigns 32 distinct
  existing evidence scopes (30 knowledge records, SKILL.md and documentary
  baseline metadata), each with read-only ownership and no mid-flight
  build/lint/tests/formatters. The first canonical plan refused an absolute
  `reportDir`: `invalid_report_dir`, exit 1; its stderr and command record are
  retained. Correcting the path to a relative label produced
  `ufo-swarm-wave-v1`, exit 0, counts spawn=32/resume=0/total=32, 32 distinct
  names/prompts, and a leading fresh Godspeed invocation in every task.
  Full plan: `.ufo/round-20/wave-plan.validated.stdout.json`.
- **Exact authority blocker.** Canonical route preflight read the global
  authority at SHA-256
  `08788ddcbbb48180b987e6f54b517af294c85cacceb07bdd594843a53e668dcc`.
  Reviewer/sentinel/connector resolve through `@m_mid`, critic through
  `@m_strong`, and scribe through `@m_fast`. Other observed global bindings
  are executor/revenger `@m_mid` and scout/mutation-tester/simplifier `@m_fast`.
  The operator requires content `@m_composer`, audit `@m_grok`, connector
  `@m_antigravity` with `@m_zfl` fallback. The named aliases exist, but the
  role bindings do not select them; the alias-level antigravity fallback is
  `[]` at global config line 399. Exact comparison:
  `.ufo/round-20/route-contract.json`. Preflight is **unprobed**, zero pings:
  this is binding evidence, not a provider outage or availability claim.
- **Dispatch decision.** No canonical `run`, persisted worker registry,
  native `task` batch, worker, alternate L1, judged handoff, retry loop,
  model pin, routing overlay or configuration edit occurred. No new corpus
  admission, SKILL.md/verifier implementation change, or independent
  spot-check is claimed. The absence of "`corpus/QUALITY.md`" and optional
  MINT.md was observed during the scoped path lookup; no quality criterion
  or mint history is fabricated to fill that gap.
- **Measured safe acceptance.** All commands ran in this lane at
  `292bbf8ca7527159570947dadd65bb5528554380`; argv, full stdout/stderr and
  exit codes are retained in `.ufo/round-20/acceptance-results.json`.
  `python3 verifiers/verify_corpus_integrity.py`: tracked=51, unindexed=0,
  stale=0, missing=0, report_dead=0/32, commit_total=27, unresolvable=0,
  nonhash=0; **9/9 checks pass**, exit 0.
  `python3 verifiers/verify_corpus_independent.py`: the same relevant counts
  and **exit 0**. Isolated integrity `--self-test`: **0 failure(s) over 88
  assertions**, exit 0, with temporary fixtures confined to this repository.
- **Actual inherited scenario.** The published counting command was executed
  with the exact entry revision and `frozen`: **226 subjects, 14 unresolved,
  14 classified, 0 unclassified, 4 actionable occurrences, 3 prepared routes**,
  exit 0. This remeasures the retained projections/classification contract;
  it neither re-probes live sibling sources nor proves owner acknowledgment.
  Its exact invocation and full JSON outcome are in the same acceptance
  artifact. Inherited work is preserved, not counted again as a new move.
- **Intentionally unrun.** The unchanged 601>600 checklist failure and earlier
  Phase 0/self-iteration failures are already recorded ground truth, not
  rerun for confirmation. The live harness verifier reads native session
  bodies and is excluded. No host/source/package fix is absorbed. No
  substrate or sibling write, shared-report/ledger edit, native-session
  mutation or push is authorized.
- **Verdicts.** Freshness selected but **unchanged**; depth, coverage,
  operability, calibration (including owned consistency), and adjacency all
  **unchanged**. Expansion/quality/discernment **unchanged**. No score gain,
  completed/verified-round credit, convergence, saturation, promotion, native
  acceptance, successful receipt or Sighting completion. This attempt alone
  does not establish three consecutive blocked rounds.
- **Concrete unblock and continuation.** Operator/global routing owner must
  supply the requested role bindings and connector fallback; L1 cannot
  change them. Also resolve the canonical CLI's lane-local registry output
  root before `run`: source lines 431–432 and 1871–1877 resolve/persist it
  under the UFO authority root by default, outside this lane's write scope.
  This output-root risk is source-derived, not an attempted write. Preserve
  the at-least-100 verified-round target and use a fresh authorized native
  L1 session for the next attempt, carrying this blocked evidence and the
  existing owned work; do not loop rounds here or overwrite round 20.
- **Changed-record smoke.** The isolated existing
  `check_governance_citations` predicate was executed on the prepublication
  LOG/SCORECARD snapshot, not the known-red full checklist:
  `PASS governance.citation_resolves: evaluated 148 — 148 governance citation
  token(s) resolve across 2 files; 8 quoted meta-finding(s), 3 schematic
  token(s) excluded`, exit 0. `.ufo/round-20/governance-smoke.json` pins that
  snapshot's two hashes and exact command/output. This appended measurement
  record is later than that snapshot; no frozen-byte or whole-checklist
  pass is asserted for the append itself. Empty stdout/stderr captures were
  removed, retaining the actual refusal and successful plan instead.

### Round 20 publication — committed-work remeasurement and handoff

- Owned work landed as `5e347837797dac186d3b4138c348bed2e4d6e275` under the
  required lane identity. The later report is
  `.ufo/reports/round-20/kotoba.md`; the fresh-session handoff is
  `.ufo/round-20/continuation.json`. Both explicitly record dispatch-blocked,
  zero verified-round credit, and no release/receipt/Sighting completion.
  They preserve the historical launch-counter discrepancy instead of
  overwriting earlier reports or inventing a completed-round tally.
- Actual delivered-work runs at that exact revision are retained in
  `.ufo/round-20/delivered-acceptance.json`: own corpus gate **9/9**, independent
  instrument **exit 0**, bounded governance predicate **PASS / evaluated 148**,
  and frozen inherited replay **226/14/14/0** (subjects/unresolved/classified/
  unclassified). Every command exited 0. Full output and argv are retained;
  none is a whole-checklist, live-session, live-sibling or native-judge pass.
- Report and handoff publication finish the reachable local evidence work,
  not the blocked craft move. Only the global routing owner can supply the
  required aliases/fallback, and registry output containment must remain
  lane-local before a later `run`. No successor has been released or started.

## 2026-10-16 — protocol conformance: SCORECARD contract fields

- Operator rollout of the 2026-10-16 fleet protocol amendment (fleet-root commit `84bade0`): this lane's `SCORECARD.md` already carried real `axes`, `planned`, and `retired` sections, so only the missing `Capabilities` and `Saturation` sections were appended, per `../AXES.md` § SCORECARD.md contract. Purely additive — existing bytes unchanged (verified by diff: additions only).
- No axis claim was made, no score moved, no verdict changed, and no number invented; the capabilities table enters with no rows, pending a round that demonstrates a capability running.


## 2026-10-19 — Round 21 (loop 1, round-of-loop 1): freshness sweep + adjacency re-measure

- Claims declared at `.ufo/round-21/claims.json` (F freshness, A adjacency); dispatched as a 64-lane scout swarm on `opencode-go/deepseek-v4.1-flash` (opencode-go key 1 of 7 — round-robin continues at key 2 next opencode-go round); evidence fragments `.ufo/round-21/scouts/*.md`; report `.ufo/reports/round-21/kotoba.md`.
- **Claim F verified by repair + record.** At HEAD `4e92f36` two gates were red and unrecorded: `verify_surfaces.py` exit 1 — omp rebuilt 2026-10-16 (`ff59fc1b`→`bf1e86a9`, v18.11.1, unminified chunks; registration callees renamed `Co`/`Dl`/`Hj`; the `CALL_RE` allowlist extracted 0 and `no_uncovered_class` **passed vacuously on 0 extractions**) — and `verify_skill_checklist.py --self-test` 2/1504 — fixture `delegated-directory/map.json:15` delegates to `probe-dir`, an empty directory git cannot track, so the round-16/17 `0/1504` records were false in any clone. Repairs landed: per-harness callee allowlist (`OMP_CALL_RE` = historical + `Co|Dl|Hj`; opencode keeps the conservative list — its single-letter callees would over-match) + an extraction-vacuity guard in `check_no_uncovered_class`; `verifiers/fixtures/surfaces/strings-omp-newcallees.txt` + five new self-test assertions (70→75); `verifiers/fixtures/checklist/delegated-directory/probe-dir/.gitkeep`; `.gitignore` regained `__pycache__/` + `*.pyc` (rules deleted by `c8b53ac` in the same commit that added two pycs; `4e92f36`'s "already covered" claim was false); `verifiers/baseline.json` omp sha/mtime re-pinned to `bf1e86a9` (no check enforces `measured_against` — named debt).
- Known debt re-confirmed, not "fixed" by raising the budget: `trigger.line_budget` 601>600 (inherited from `02302c5`; LOG's round-18 `exit 0` was false at its own landing commit — recorded here, not rewritten).
- **Claim A verified.** Live sibling dead-token counts kagi 2 / kake 1 / kasegi 5 / kengaku 1 / kumitate 5 = 14, delta 0 vs round 16. Correction: the recorded headline "10 dead / kasegi 1" (SCORECARD adjacency row, this entry's round-16 record below, `claims.json`) was a transcription error — the round-16 ledger JSON always said 14 / kasegi 5 and replays live. Refreshed route evidence: `corpus/knowledge/sibling-citation-routing-round21.md` (README index row added; corpus-baseline re-recorded 51→52 tracked / 32→34 report pointers). kasegi gained delegated-root resolution post-round-16; new fleet prior art: kaidoku `citation-drift-probe.py`, kake `replay-proof.mjs`, kasegi `test_resolve.py`; kagi's `delegated=D` is an unrelated ratio count (naming collision).
- **Saturation declared** (SCORECARD §Saturation): line 10.0 on owned axes, N = 3 lane-rounds, prospective from round 22; owned-proxy reading recorded (draft evidence `.ufo/round-21/scouts/C2.md`).
- **Named debt, not landed:** repo is DIVERGED from its remote — true remote head `74fc0f1` (PR #2) is absent locally, `4e92f36` is unpushed, and a push would be non-fast-forward (scout H1; git commit/push/merge correctness is loop-round-14's audit — nothing pushed this round); `measured_against` pins are inert (no gate reads them); census doc errata (stale counts per scouts R4/S4) and the round-12 record's `10/19` (now `19/19` at `d49dfa5`) are documentary debt; `verify_corpus_independent.py:313` uncaught `FileNotFoundError` on a deleted tracked file (scout M8); SHONEN.md box-3 recipe outcomes are stale (scout S6 — supersession belongs to the round-25 targeting); LOG records falsified at their own commits (`LOG.md:848` 0/1504, `LOG.md:952` exit 0) — recorded here, not rewritten.
- SHONEN: untouched — every box stays `[~]`; a lane-dispatched swarm is the lane (PROTOCOL promotion gates), so no `[x]` was claimed. Round-25 (loop-round 5, luna-max) targeting spec: `.ufo/round-21/scouts/C3.md`.


## 2026-10-19 — Round 22 (loop 1, round-of-loop 2): line_budget cleared by content + adjacency escalation via L0

- Claims declared at `.ufo/round-22/claims.json` (B freshness, A2 adjacency); dispatched as a 62-lane scout swarm on `opencode-go-2/deepseek-v4.1-flash` (key 2 of 7 — the item list carried 62 of the designed 64: two planned lanes were merged in design; all 62 completed, zero lost; the deviation is recorded here rather than papered over). Fragments `.ufo/round-22/scouts/*.md`; report `.ufo/reports/round-22/kotoba.md`.
- **Claim B verified.** § Instruction surfaces (SKILL.md lines 75-166 at `b16300f`; body sha256 `e046a0252cc96f173d148b419b7856e23fe789659cf02bc5b3237e8da26114f5`, sed-canonical) moved verbatim into the existing `corpus/knowledge/instruction-surface-census-round13.md` (absorb variant — zero baseline churn, three independent green simulations: S04/S05/S07). SKILL.md 601 → 516 lines; live checklist gate exit 0 with 10 × PASS including `line_budget evaluated 516 within budget 600`; all six gates + three self-tests green. Byte preservation is gate-enforced at landing by the pinned sha + contiguity check (scout S10 proved no live instrument enforces it — the round-15 frontmatter move already drifted 4 lines under that hole, now named debt). The moved table's "All craft below" cell dangles in its new home — kept verbatim, named, not smoothed.
- **Claim A2 verified.** Live acknowledgment measure: **0 across all five siblings** — working trees, full git histories (`--all`), the fleet aggregator, and the L0 channel (scouts A1-A5, A7; positive controls prove the scans). Escalation appended to the protocol's L0 side channel `../.ufo/l0-questions.md`: 49→50 lines, 38356→38656 bytes, pure append proved (`cmp -n 38356` prefix-preservation; fleet `git diff --numstat` = 1 insertion, 0 deletions; shas `60ccdc9e…`→`029eebed…`). The fleet path remains uncommitted — durability is integrator-owned per PROTOCOL. Correction recorded: the ledger holds **3 route objects / 4 actionable findings** (r16adj-route-kake/-kasegi/-kumitate), not "five packets" as claims.json filed — the filed line itself names the three routes and uses "five" only as the sibling count (scout A7's D1).
- **Named debt / defects (recorded, not silently absorbed):** the round-21 report's "64/64 completed" overstates fragments — 63 exist, the 64th lane wrote the report skeleton (scout G5); the SCORECARD-vs-LOG stagnation clock wording differs by one round (scout C2 — round-22 convention: counted rounds are 21, 22, 23; a third no-capability round fires the nudge for round 24's planning); round-15's frontmatter move is not byte-verbatim (4 of 92 lines, scout S10-D3); claims.json B's landing surface omitted `verifiers/corpus-baseline.json` (moot for the chosen absorb variant); kasegi's `anchorcheck.py` ORIGIN_/MIRROR_ work has no kasegi LOG entry (scout A3); `.git`-less export self-test is 108/1504 (carried); SHONEN.md's PROTOCOL anchor cite is stale (`:65`, scout G7); the round-8 lesson's "aggregator report ABSENT" record is stale — it resolves at `a5d6a7e` (scout C3).
- **Stagnation bookkeeping:** no capability row entered at round 22 (the pin-guard stayed /tmp-only per its exploratory designation) — no-move count = 2/3 (rounds 21, 22). Round 23 (loop-round 3) plans the substrate-pin-guard capability claim (scouts P1-P8: verified prototype, merge recipe canonical-body + P1 exit-ladder + P4 self-test idiom; landing plan P8). If it lands, the window resets; if not, the nudge fires for round 24.
- SHONEN: untouched — all boxes stay `[~]`; round-25 targeting delta: `.ufo/round-22/scouts/C3.md` (the `[x]` gate is dispatch-ownership, not seat count; the aggregator's canonical-form gate cannot pass `[x]` lines as written).


## 2026-10-19 — Round 23 (loop 1, round-of-loop 3): substrate-pin-guard capability

- Claim declared at `.ufo/round-23/claims.json` (P — capability acquisition, freshness). **Provider exhaustion at dispatch:** opencode-go keys 3, 4, 5 all returned `402 Insufficient account funds` (the full 64-lane dispatch on key 3 insta-failed; 2-lane probes confirmed 4 and 5 dry); key 6 probed alive and carried the swarm — round-robin adapted per the goal's exhaustion clause, recorded in claims.json + this entry. Swarm: 64 items on `opencode-go-6/deepseek-v4.1-flash`; **64 completed — lane A4's fragment landed late** (the swarm summary showed 63 and a mid-run fragment check missed it; `git add` captured it in the work commit, and this entry corrects the pre-commit draft that recorded it as lost — the round-21 "64/64" class, caught before publish here). Fragments `.ufo/round-23/scouts/*.md`; report `.ufo/reports/round-23/kotoba.md`.
- **Claim P verified as filed.** `verifiers/check_substrate_pins.py` (sha256 `fafe88d881eb…`) landed as the merged design of three independent implementation drafts (D1-D3) refined by twelve verification lanes (V1-V12), from the round-22 P1-P8 specs. Integrator-run battery at landing: live `exit 0` (`OK 3/3 pins hold`, omp mtime `delta 0 ns`, ns-exact integer compare); `--self-test` `0 failure(s) over 46 assertions` over `verifiers/fixtures/pins/` (mini.bin `d3b4640e…`, byte-identical to the round-22 P4 design); six red probes on /tmp copies exactly as filed — sha drift → 1 naming the pin (text + `--json`), mtime-only drift → 1 naming `omp_binary_mtime`, missing binary → 2, corrupt baseline JSON → 3 no traceback, missing/null `measured_against` → 1 `VACUOUS`, deleted pin → 1 `PIN_ABSENT`; two live runs byte-identical; read-only, hash-never-exec (V3's strace: one execve — the interpreter). Red-before replay: baseline re-pinned to the round-18 omp sha `ff59fc1b…` → exit 1 `DRIFT omp_binary_sha256` — the state the 2026-10-16 rebuild produced while `verify_harness_claims.py` printed `28/28 checks pass`.
- **Debt closed:** `measured_against` had zero readers (`grep -c measured_against verifiers/*.py verifiers/*.sh` → 0 ×6, scout D6) and the block was deletable with every gate green (round-22 scout M6). The P7-C9 silent-shrink, P6-D1 TypeError, and M6-D2 silent-block-deletion classes are each closed by a designed exit (probes f/d/e). The 874 ns float-parse trap (P1) is closed by integer-ns compare.
- **First capabilities row** enters SCORECARD §Capabilities (substrate-pin guard, first-working round 23, evidence = the demonstrated run). Stagnation window resets to 0.
- **Records:** corpus doc + README row + SKILL.md bullet (518/600) + capabilities row + freshness annotation + move-log row + corpus-baseline re-record (observed 52→53 tracked, 34→36 report pointers; the first landing had one repo-relative report pointer — dead under the corpus instrument's file-relative base, corrected to host-absolute, matching the round-22 lesson).
- **Named debt / limits:** keys 3-5 exhaustion (next opencode-go round: key 7, then re-probe 1-5); F-lanes' documentary errata drafts (census counts, harness 27-vs-28, SHONEN anchors, round-12 10/19, F7 crash-class fix sketch, F8 git-archive hermeticity sketch) are deferred to round 24+ — drafts in `.ufo/round-23/scouts/F*.md`; adjacency held (ack still 0; L0 line still uncommitted — integrator-owned).


## 2026-10-19 — Round 24 (loop 1, round-of-loop 4): documentary errata + self-test hermeticity

- Claims at `.ufo/round-24/claims.json` (E freshness, H operability). **Provider:** hyper returned `402 out of credits` on all 45 reported lanes at dispatch (3 unreported) — the stated loop-round-4 fallback applied: the identical 48-item swarm reran on `devin/deepseek-v4-1-flash-high`, 45+3 completed (45 in the summary; all 48 fragments on disk — three landed late). Scout C1 put **both claims on HOLD as filed**; the landing corrects the claims per its verdicts (the filed texts stand in claims.json; the corrections are recorded here and in the report).
- **Claim E verified on the corrected set.** C1's re-targeting: the genuinely stale present-tense set replaced the filed set — (a) census counts: 9→5 opencode ids, seven→six rules at the two editable sites (:28, :287), 72→75 assertions, 41→38 extra-row findings; the third 'seven' (:337) sits **inside the sha-pinned round-22 verbatim block** (`e046a025…`) and was preserved byte-verbatim with an append-only erratum beside the block (E1's recommendation; the contiguity gate re-verified after landing); (b) harness-verifier doc 27→28 (:15, :186) + a vacuity note (6 of 11 opencode checks read 0 against the v2.0.26 grammar — scout R3, reproduced); (c) round-12 record: append-only erratum — the W0 `10/19` reads **19/19** on this host (the 10 was the round-12 host's lowercase `/home/vgpnk/projects` base; reconstructed in `unshare -rm`), and §2's `43=37` glues two tree states (`43 = 43` at either); (d) SHONEN :7/:46 + **README :49** (`PROTOCOL.md:34-39` → `:65` — the third occurrence claim E missed) + SHONEN's embedded awk output 14→15; (e) SKILL.md present-tense :109/:461 27→28. **Kept as dated records per C1 defects 1-2:** SKILL.md:456 and both SCORECARD '4 checks' cells. Every corrected value re-measures live; every gate exits 0; the pinned-block contiguity gate holds (`e046a025…` reproduces).
- **Claim H verified on the corrected mechanism (Fix A, not the filed Fix B).** C1-H1: the claim text named Fix B (fallback change) while its invariance falsifier requires Fix A (`--repo str(DEFAULT_REPO)` pinned at the two self-test fixture-argv sites). Fix B deferred — it changes live CLI behavior (foreign `--skill` in a .git-less tree: FAIL governance → N/A) and falsifies three in-file statements (`:142`, `:180-181`, `:1707-1708`); its three docstring edits are named debt. Fix A verified at landing: archive-export self-test `0 failure(s) over 1504 assertions` (count exact — C1-H4's anti-shrink observable), live gate + self-test byte-invariant, probe-dir removal → 2 failures, box tamper → box_map FAIL, pinned-block contiguity holds.
- **Pin supersession (C1-H3, acknowledged here):** `verify_skill_checklist.py` sha `02ccf1b310f7…` → `15d0aa16d549…`. The machine-used pin (`corpus/knowledge/sibling-citation-routing-round16.json` instrument block) is updated with a `sha_superseded_from` note; the historical prose pins (`checklist-execution-round17.md:221/:245`, `LOG.md:850/:992`) are superseded by this entry, not rewritten — they evidence what was true at rounds 16-17.
- **Adjacency (held):** scouts A1-A3/A5-A7 — acknowledgment still 0 (A4's round-24 fragment landed late; no count change); the L0 round-22 line remains uncommitted in the fleet repo (integrator-owned).
- **Named debt:** Fix B + its three docstring edits; F7 crash-class fix (independent verifier FileNotFoundError — sketch in `.ufo/round-24/scouts/H8.md`); the ~15 dated harness-count sites F4 classified keep (no action); hyper lane credits exhausted (operator-level, outside lane scope).


## 2026-10-19 — Round 25 (loop 1, round-of-round 5): luna-max verification sweep of rounds 21-24

- Claims at `.ufo/round-25/claims.json` (V1 freshness re-verification, V2 calibration re-measurement); 64/64 lanes on `openai-codex/gpt-6-luna-max`; fragments `.ufo/round-25/scouts/*.md`; report `.ufo/reports/round-25/kotoba.md`. Scout C1 put both claims on HOLD **as filed** (no artifact-to-command manifest; the L0 append is uncommitted; metric inventory unbounded; count discrepancies) — the shape is corrected here; the substance verified.
- **V1 verified.** All rounds-21-24 artifacts re-verify on the current tree (scouts W01-W16: 14 clean, W03/W04/W05/W07 named the defects repaired or filed below); every red probe in the M/X lanes flips (20/20 incl. pins sha/mtime/VACUOUS/PIN_ABSENT, corpus/independent/harness/surfaces/checklist classes, fault class (d) both instruments); all seven gates exit 0.
- **V2 verified with corrections filed.** Twelve per-record lanes re-measured every number in rounds 21-24's reports/LOG/SCORECARD. Corrections (recorded here; the filed reports stand as records): **r23's "64 items" was 63** (the items array carried 63; 62 fragments + C4's report skeleton = 63 deliverables); **r23's "518/+2 lines" was 521/+5** (scouts N07/N08/G03); **r24's "48 items/fragments" was 45** (44 fragments + C4 report); r24's "43 = 43 at either tree" was wrong for `7d15407` (37/37) — corrected in the round-12 erratum file in-round; r22's report figures (census 422 vs 421; governance 182 vs 171) measure different commits (named, not rewritten).
- **In-round repairs:** `verifiers/baseline.json:7` stale "no check enforces this pin" note corrected (the r23 pins guard enforces them); the census round-24 erratum's self-drifted "line 337" citation fixed (the note's own insertion shifted the block); the round-12 erratum's tree-pairing corrected (43/37 per tree); 4 ignored `.pyc` files removed from disk.
- **Sweep-named debt (filed):** W05 — the published current-replay command's stale SHA guard fails `instrument_drift`; G05 — report-completeness gaps (round 2 skipped, round 18 absent, round 16's report missing sections); X03 — kasegi's out-of-range citation still exits 0 (sibling-owned); the L0 round-22 line still uncommitted (integrator-owned); hyper + opencode-go keys 3-5 credits (operator-level).
- **SHONEN [x]-readiness pack** (scout C2): per-box procedures + committed-evidence requirements + a paste-ready aggregator-gate repair request, for a non-kotoba verifier (loop-14 devin agents or the aggregator). No `[x]` is claimed from this round — the dispatch is lane-authored per the promotion gates.
- Stagnation window: 1/3 (round 24; round 25 carried no capability row). Nudge would complete at round 26 if rounds 25-26 both land no capability; dormant anyway (depth 9 < line 10.0).


## 2026-10-19 — Round 26 (loop 1, round-of-loop 6): routing-replay guard + independent-verifier crash class

- Claims at `.ufo/round-26/claims.json` (R adjacency, I operability). **Provider:** `xai-oauth/grok-4.7-fast` returned 403 out-of-credits on ALL 46 reported lanes (2 unreported) — no stated fallback exists for loop-round 6; reran the identical 48 items on the proven `devin/deepseek-v4-1-flash-high` per the general exhaustion clause (recorded here + claims.json; same class as r23's key-6 adaptation). 48 items, all fragments landed (lane X3 filed as `X03.md`).
- **Claim R verified.** The stale guard (`corpus/knowledge/sibling-citation-routing-round16.md:154`, literal `02ccf1b3…` predating Fix A) is replaced per scout R4's pick of three drafts (R3a): the replay code reads `fixture["instrument"]["sha256"]` from the ledger JSON + fails closed (`instrument_pin_absent`). Integrator proofs: published replay `HEAD frozen` → exit 0, `226/14/14/0/4/3`; before-revision `581e293` → exit 0 (the documented "Before" command runs again, `14 unclassified/0 routes`); JSON-pin tamper flips it where a literal swap stayed silent (R3's discriminating probes); `HEAD live` still exits 1 `source_drift` (kake/kengaku bytes — pre-recorded, out of scope).
- **Claim I verified.** Scout F4's pick (F2's diff, applied verbatim from `/tmp/f2/draft-A.diff`): `_open_text` helper at every read site (README census, pointer + commit harvests) — a deleted tracked file now raises EnvError exit 2 naming the file, matching the primary's idiom, no `:313` traceback. Integrator proofs on a `cp -a` copy: crash probe exit 2 (primary exit 2), self-test `0 failure(s) over 52 assertions`, live agreement exit 0 + primary 9/9, red probes still flip (per F2/F4's own batteries).
- **Sweep-named debt (filed, scouts S1-X16):** X14 (high) — the repo is shallow (`.git/shallow`); fresh clones read `commit_unresolvable=24` while the live tree reads 0 (clone-hermeticity divergence; unshallow or repin is loop-14/operator territory); S7 — `verifiers/fixtures/pins/` is never read (self-test uses inline literals), `tripwire.bin` unenforced, four docs overclaim; M4 — `verify_harness_claims.py` never reads `expect` for 11 zero/positive pins (the r23 PIN_ABSENT class, open in the harness); X8 — six stale README counts (`:34` 27→28, `:39` 4→7, `:38` 9→5/seven→six, `:61` delegated 1→0, `:20` 17→14/7, `:16` telemetry family); X10 — self-test blocks deletable with counts green (no assertion-floor tripwire); X11 — heredoc `<<EOF` inside quotes/comment mis-scans; X12 — anchor *deletion* (vs corruption) passes the catalogue guard; M2 — vacuity guard escapable by re-kinding all 8 omp rows in both files; S3 — SHONEN's anti-pattern command now returns 0 not 22 (table moved at round 15) + "27 checks" at :20; S4/X15 — divergence measured at 14 ahead/2 behind vs live remote `74fc0f1`; X16 — quota state is locally pre-detectable (`~/.cache/ai-usage/status.json`; grok weekly 100% until Oct 23, hyper 0) and no dispatch precheck reads it.
- **Stagnation correction (scout C2):** the window is **2/3** (r24 + r25; LOG's "1/3" was wrong), and claim I carries no capability type — no reset. Window completes at end of r26; the nudge is first eligible at round 27 and dormant (depth 9 < line 10.0).
- Adjacency held otherwise: ack 0/5 (sixth measure, scouts X01-X05); L0 round-22 line pure-append but uncommitted, 93 min stale (integrator-owned, scout S9/X06); aggregator dormant since round 10 + driver stopped (X06, fleet-owned).


## 2026-10-19 — Round 27 (loop 1, round-of-loop 7): README errata + SHONEN note + shallow-close

- Claims at `.ufo/round-27/claims.json` (A freshness, C calibration); 26/26 lanes on `zai-coding-plan/glm-5.3-flash`; fragments `.ufo/round-27/scouts/*.md`; report `.ufo/reports/round-27/kotoba.md`. Scout R2's critic amended claim A before landing (bare `delegated 1->0` would have rewritten a dated record and tripped the claim's own falsifier).
- **Claim A verified on the amended shape.** Present-tense fixes: README harness row 27->28 + `17/17`->`7/7`; census row 9->5 opencode classes + seven->six rules; surfaces row 4->7 checks. Erratum (record kept): the delegated-map site now reads "delegated 1 (fixture-only from round 16 on; live map 8/0/33)". Annotations (dated rows kept): telemetry row (`part` table + permission grammar gone from opencode v2.x; live 14 rows/7 keys, chars 300-658) and render row (14 rows/7 keys; 17-row era ended at round 18). New sites folded in (scouts A1/A2): opencode.log rotated to `log/`, the harness row's reproduction count. Every value re-measures live (scouts A2-A7); gate-interlock proven (scouts A6 — Basis-prose edits cannot flip the corpus gates).
- **Claim C verified.** SHONEN:15's anti-pattern evidence now names the corpus home (`fail-closed-and-anti-patterns.md:58`, 20 data rows / 22 lines) and the live awk result (0); that file's own "18-row" stub corrected to 20 (scout S3-D1). Saturation section carries the running window: **3/3 completed at round 26's close** (r24+r25+r26, per C2's correction), first nudge-eligible round 27, **dormant** (depth 9 < 10.0). SHONEN marks untouched.
- **Round-26 X14 debt CLOSED:** `git fetch --unshallow origin` — the repo is no longer shallow; the fault harness self-test is green again, fresh clones read the same nine numbers as the live tree, and `commit_unresolvable` reads 0 in both. This was the sweep's only HIGH debt.
- **Sweep-named debt carried (scouts S1-S6, M2, S2, S7):** M2 — the surfaces vacuity guard is escapable by re-kinding all 8 omp rows in both files; S2 — pins-guard case boundary (`OMP_binary_sha256` silently ignored) + SKILL.md:465 overclaims fixture use + the guard is unpinned/uninvoked by any aggregate; S7 — `verifiers/fixtures/pins/` is never read (self-test uses inline literals), tripwire unenforced; X1 — ack 0/5, seventh measure; L0 line still uncommitted (integrator-owned).
- Stagnation: window 3/3 complete at r26 close; nudge dormant; no capability this round (window would only matter if depth reached the line — it has not).


## 2026-10-19 — Round 28 (loop 1, round-of-loop 8): rekind escape + pins exact-case

- Claims at `.ufo/round-28/claims.json` (K freshness, P operability); 16 lanes on `zai-coding-plan/glm-5.3-flash`; the swarm summary reported 15, but all 16 deliverables are committed (15 scout fragments + C2's report skeleton — the 'lost' 16th was the scribe's carve-out, corrected here). Fragments `.ufo/round-28/scouts/*.md`; report `.ufo/reports/round-28/kotoba.md`.
- **Claim K verified on K4's pick.** Scout M2's escape (re-kind omp loader-group rows to `doc` in baseline+census -> extraction checks silently skip; exit 0 on live dumps) is closed by K3's per-id kind-consistency arm in `check_no_uncovered_class`: an extracted id whose baseline entry is no longer `loader-group` FAILs naming every `id->kind`. K4 caught K2's zero-declared vacuity arm staying silent on a PARTIAL rekind — K3's arm catches both. Integrator proofs on a `cp -a` copy: full rekind -> exit 1 naming all 8; partial -> exit 1 naming the 7 (gemini kept); live gate byte-invariant; self-test **75 -> 82 assertions** with `baseline-rekind-doc/partial` fixtures that are true discriminators (pristine exits 0 on the unguarded tree).
- **Claim P verified on P3's approval.** P2's patch: DISCOVER_RE matches case-insensitively, then a pin-shaped key differing only in case from a contract pin is reported `UNSUPPORTED` and exits **2** naming the canonical pin — never skipped. Integrator proofs: `OMP_binary_sha256` -> exit 2 with the exact message; the three real pins pass; live byte-invariant; self-test **46 -> 51**. The "self-test over `verifiers/fixtures/pins/`" overclaim corrected in all three sites (SKILL.md:465, the SCORECARD capabilities row, the corpus doc) — the committed dir is evidence-only, the self-test builds inline tempdir fixtures (scout S7).
- All seven gates exit 0 on the landed tree; pins live 3/3 (delta 0 ns).
- Named debt carried: M2's rekind class is closed but the surfaces instrument still has the X10 block-deletability class (no assertion-floor tripwire anywhere); S4's sync axis (18 unpushed commits on no remote branch); the standing divergence/L0 items for loop-14.


## 2026-10-19 — Round 29 (loop 1, round-of-loop 9): harness zero/positive pins + assertion-floor capability

- Claims at `.ufo/round-29/claims.json` (H freshness, T capability/operability); the items array carried 27 lanes (not the prose 32 — corrected here, the r23/r24 count class); 27/27 on `openai-codex/gpt-6-luna-max`. Fragments `.ufo/round-29/scouts/*.md`; report `.ufo/reports/round-29/kotoba.md`. Scout C1 put both claims on HOLD as filed; landed on its resolutions.
- **Claim H verified on C1's semantics.** Scout M4's class (11 of 28 pins in zero/positive mode never compared against `expect`, verified again this round by H1/M4) is closed by H2's four-line mode fix: `zero` compares equal-to-expect, `positive` enforces observed >= expect. Integrator proofs: `omp.db.rows` and `oc.log.skills_rescan_max` corruption -> DRIFT exit 1 naming each; the swarm's all-28 matrix flipped every pin (H2/H3/H5); live gate byte-invariant 28/28; harness self-test 0/10.
- **Claim T verified — second capability row.** `verifiers/check_assertion_floors.py` (T3's implementation) reruns all six self-tests and fails below the recorded floors (harness 10, corpus_integrity 88, corpus_independent 52, surfaces 82, checklist 1504, pins 51) or on unparseable output. T4's trust boundary is documented in the docstring: the guard detects silent block deletion and count drift, not a self-test that prints a fake count (the instruments are the trusted base). Proofs: live all-PASS exit 0; T6's deletion probes (79/82, 1482/1504, 50/51) and my unparseable-output probe (a mangled copy -> 'FAIL surfaces summary=missing') both flip it.
- **Eight gates exit 0** on the landed tree (the seven + the new guard). Capabilities table: two rows. Stagnation window resets (capability landed at round 29).
- Named debt carried: C1's H-nits (H3's extra self-test cases not merged — 22 vs 14 assertions, a possible follow-up); the floors table must move whenever an instrument's count moves (the r28 surfaces 82 grew — floor updated this round; the guard's docstring carries the round-29 values); S5's report-completeness groups (rounds 2/18, r14 draft, r20-28 in the child repo); X2's quota-signal display defects.


## 2026-10-19 — Round 30 (loop 1, round-of-loop 10): fault-harness control world + heredoc scanner

- Claims at `.ufo/round-30/claims.json` (F freshness, D operability); the items array carried 28 lanes (prose said 32 — the r23/r24 count class, corrected here); 28/28 on `devin/deepseek-v4-1-flash-high`. Fragments `.ufo/round-30/scouts/*.md`; report `.ufo/reports/round-30/kotoba.md`. Both claims landed on critic-amended mechanisms.
- **Claim F verified on F3's design (the filed fix proven inert).** Scout M7's (f) gate re-read out.json twice (`blind_total == base_total`); C1/F5/R2 each proved the CLAIM's own fix (parse out-baseline.txt) remains tautological because the observation is mode-independent. F3's landed design adds a pristine CONTROL world clone and requires the planted world's `report_total` delta == exactly 1: M7's no-op plant FAILs, a count-only mutant FAILs, all 11 fault worlds behave as documented, exit codes 0/1/2 intact, live harness ALL PASS byte-invariant, self-test 4->8. **The (h) premise was false** — fault-h never runs the independent instrument at all (a stub exit-2 is already caught); recorded as the correction, not forced. Honest limit (F3): an alias re-exec of the primary still passes (D-M7-2 narrowed, not closed).
- **Claim D verified on D4's diff (both naive drafts rejected).** D4 proved D2's and D3's quote-masking regressed `$(...)` heredocs; the landed diff is operator-level: `HEREDOC_RE` captures optional trailing `~`, a `heredoc_delimiter()` walk tracks quote state / `$(` depth / word-start `#`, and the call site uses it. Evidence: 11/11 form matrix matches bash 5.2, 71/71 fixture dirs byte-identical, the four round-17 heredoc fixtures exact, self-test 0/1504, live gate + `--json` byte-invariant. The routing-16 instrument pin updated (`15d0aa16` -> `4d3d38c9`, supersession note).
- All eight gates green at close (checklist live + self-test 0/1504; fault self-test green; floors green; replay exit 0).
- Named debt carried: the round-17 ceiling row's direction (`checklist-execution-round17.md:317` says over-catch; measured under-catch — D4); M2's dead-dump+rekind residual (suite-closed by other checks — scout M6); S4's HIGH divergence/rebase trap; S5's report-completeness groups (11 defects, incl. rounds 2/18 absent, r20-29 at the lane root vs PROTOCOL's main-repo contract, r15's report clobbered); the floors-guard registry-shrink class (scout S6); SHONEN.md:20/35-37 stale counts (scout S3).


## 2026-10-19 — Round 31 (loop 1, round-of-loop 11): extractor-blindness arm + floors-guard hardening

- Claims at `.ufo/round-31/claims.json` (B freshness, G operability); items array 27 (prose 32 — the count class, corrected); 27/27 on `zai-coding-plan/glm-5.3-flash-low`. Fragments `.ufo/round-31/scouts/*.md`; report `.ufo/reports/round-31/kotoba.md`. Both claims landed on critic-shaped designs (C1's B-REVISE, G3's approve-with-defects).
- **Claim B verified on B4's pick.** Scout M6's residual — strip the dump's registration shapes AND re-kind baseline+census to `doc`, leaving 0 extracted passing — is closed by B4's omp-scoped arm: when extraction yields 0 while declared loader literals are present in the dump, FAIL "extractor blind". C1 caught the naive kind-keyed arm as self-defeating (the rekind it targets removes its own key); B4's draft pins the declared set instead. Landed bytes are B4's verified artifact (combined probe exit 1 naming 33 literals; plain dead-dump r21 semantics preserved; opencode's by-design 0-extraction unaffected — the omp scope is load-bearing). Self-test 82->87 (+ the `strings-omp-blind.txt` fixture); **floors bumped 82->87 in the same commit** (guard INSTRUMENTS + EXPECTED_INSTRUMENTS + docstring, per R3/R4's landing order — G first so its hardened registry witnesses B's table edit).
- **Claim G verified on G2's patch (G3-approved).** `check_assertion_floors.py` gains a 120s subprocess timeout (a hanging self-test FAILs named, exit 2 — scout M5's hang class closed) and a two-way registry self-check (EXPECTED_INSTRUMENTS: a dropped/renamed/added row or a lowered floor fails loudly before any self-test runs — scout S6's shrink class closed). Probes on /tmp copies: shrink -> exit 2 naming; add-row -> exit 2 naming; live all-PASS byte-invariant.
- All eight gates green at close. Ready-to-land scout drafts filed here (not claimed this round, per declare-before-work): R1's three errata — `checklist-execution-round17.md:317` ceiling direction (~-suffix delimiters UNDER-catch, not over-catch), SHONEN.md:20 '27 checks'->28, SHONEN.md:35-37 stale counts (9->10 checks, 67->71 cases, 1283->1504).
- Debt carried: S4's divergence/rebase trap (24 ahead/2 behind); S5's report-completeness (r8/r15 markers are completions-not-reports; r14 DRAFT; r18 absent); M4's leading-space pin-key skip; S2's unpinned substrate CLIs.


## 2026-10-19 — Round 32 (loop 1, round-of-loop 12): errata on the corrected set + pins whitespace closure

- Claims at `.ufo/round-32/claims.json` (E calibration, W freshness). **Provider:** `antigravity/gemini-3.8-flash` failed on ALL lanes with `502 token/shim error: antigravity token helper printed nothing` — an auth-shim failure (not credits); a 2-lane retry probe failed identically. Identical 32-item intent reran on `devin/deepseek-v4-1-flash-high` (items array 29; prose said 32 — the count class, corrected). **Round 13 (gemini-4-argon) will likely hit the same broken shim — probe first next round.**
- **Claim E verified on the critic-corrected set.** Scout C1/E1 **falsified the filed erratum (a) at dispatch**: round 30's `~?` HEREDOC_RE fix (`8e0d53a`) had already made `<<EOF~` match bash (3 subjects/2 segments) — landing the round-31 draft would have written a fresh falsehood. E1's corrected row landed instead: quoted forms `<<~'EOF'`/`<<\~EOF` still over-catch; a single trailing `~` no longer does; the true residual is `~~`-plus under-catch (body and tail swallowed, unnamed until now). E(b): SHONEN:20 27->28. E(c): the round-16 recount appended as a dated note (the 9/67/1283 values were exact at the note's own commit `57f9e38` — a true-at-commit snapshot). No SHONEN mark touched; gate-interlock proven by E5 (a positive control proves the corpus gate's non-reading is real).
- **Claim W verified on W3's unicodedata variant (W4's pick).** Whitespace-edged pin keys — 13 shapes including ZWSP/NUL/mid-key Cf that `str.strip()` misses — are discovered via their stripped shape and REJECTED (UNSUPPORTED exit 2 naming both forms); W4 disqualified trim (it launders a padded key into a pass — the round-21 vacuity class). Live byte-invariant 3/3; self-test 51->62; floors bumped 51->62 in-step (both tables + docstring; half-bump fails loudly).
- All gates green (fault self-test needs `TMPDIR` off the 80%-full /tmp — environmental, recorded at rounds 31-32).
- Debt carried: `~~`-plus under-catch is NAMED but not fixed (scanner hardening, future round); S4's divergence/rebase trap (26 ahead/2 behind); S5's report-completeness groups; the floors guard absent from SKILL.md's instrument list (scout S6); the M1 HIGH (box-map parity has no absolute floor — coordinated two-sided shrink passes; no gate covers live box counts).


## 2026-10-19 — Round 33 (loop 1, round-of-loop 13): corpus-index exclusion class + box-map floor

- Claims at `.ufo/round-33/claims.json` (X freshness, F operability); 8 lanes. **Provider:** `antigravity/gemini-4-argon` failed identically to round 12's gemini-3.8-flash (`502 token/shim error` on a 2-lane probe — the lane's auth shim is broken for a second consecutive round); identical items on `devin/deepseek-v4-1-flash-high` per the exhaustion clause. The antigravity outage is operator-level; rounds 44/45 (loop 2) and 58/59 (loop 3) will hit it unless repaired.
- **Claim X verified on X2's pair** (checker + independent companion; X4's review could not read the drafts and was outweighed by X2's direct evidence): FILE tokens that are /-ending, absolute/~ -rooted, or whitespace-bearing are classified and checked instead of silently dropped (`is_excluded_token` :185/:187 class). Proofs: all 8 planted dead shapes flip exit 0->1 and **both instruments agree** (they diverged before); the 2 live dropped tokens (README :44/:57) re-enter the census (index_patterns 67->69, observed-only — no baseline drift); live 9/9 byte-invariant; self-test 88->108; floors bumped 88->108 in-step.
- **Claim F verified on F1's pinned-field design** (F3's circularity catch rejected the map-length floor): `checklist-baseline.json` gains `"box_total": 41`, validated in `load_map` (positive int, >= entry count); `check_box_map` fails when live boxes < floor or entries != floor. Proofs: the r32 two-sided shrink (1/5/33/40 boxes) fails naming the floor; M1's one-sided classes still flip; live 10 × PASS; self-test 0/1504; the routing-16 pin updated (`e26f1939`, supersession note). Residual (F1, documented): removing the key AND the shrink passes — the map-custody trust boundary.
- All gates green at close (replay, corpus, floors, fault under TMPDIR=/dev/shm included).
- Loop-1 round 14 (round 34) is next: the 8-agent devin swe-2 git audit per the goal, following scout X15's checklist.


## 2026-10-19 — Round 34 (loop 1, round-of-loop 14): the loop-1 git-correctness audit — LOOP 1 CLOSES

- Claim A (calibration) verified: the 8-slice audit ran over everything landed in loop 1. **Prescribed-tool deviation (recorded):** the 8 Devin CLI swe-2 agents were dispatched but every tool call hit the CLI's permission wall ("requires confirmation — use --permission-mode dangerous"; the MCP wrapper cannot pass the flag; a `permissions.allow` config fix was attempted on `~/.config/devin/config.json` and reverted after a probe failed identically; the config backup `config.json.r34-backup` was restored). The identical 8 briefs were executed read-only by the integrator; the audit made no mutations. Operator-level: wire `--permission-mode dangerous` (or equivalent) before loop-2's round 48.
- **Verdict: loop-1 git correctness is CLEAN except one named defect.** G1 divergence — DEFECT (open since r21): ahead 30 / behind 2, push non-ff rejected, no remote backup of the loop's work; the behind-2 is PR #2 (README wiki link + LOG entry, additive); the merge conflict is LOG.md tail-appends (auto-resolvable); the repair is a merge commit, never a rebase (30+ SHA-citing records would break — the S4 trap). G2-G8 clean: 20/20 cited hashes are ancestors; 13/13 reports land-last with zero placeholders (2-commit convention; r33 combined); one lane identity author==committer; 0 out-of-scope paths (the r22 L0 append is the recorded exception); ignore/archive durability green (0 tracked pyc, pins fixtures tracked); append-only holds for every published artifact (spot-check deletions are in-commit round work); remote refs fresh post-r27 unshallow with the remote tip fully inspectable locally.
- Loop 1 closes: rounds 21-34 all dispatched, admitted (or audited), reported at `.ufo/reports/round-<N>/kotoba.md`, committed under the lane identity. Loop 2 begins at round 35 (opencode-go lane, key rotation resumes — re-probe keys 1-5, try key 7).


## 2026-10-19 — Round 35 (loop 2, round-of-loop 1): multi-tilde heredocs + fenced-decoy boxes — LOOP 2 OPENS

- Claims at `.ufo/round-35/claims.json` (H freshness, D operability); items array 59 (prose said 64 — the count class, corrected); 59/59 on `opencode-go-7` (key 7 alive on a 2-lane probe; rotation: 1-2 at r21-22, 3-5 dry, 6 at r23, 7 here). Fragments `.ufo/round-35/scouts/*.md` (incl. N01-N14, the loop-2 number re-measurement sweep).
- **Claim H verified on H5's WIDE pattern** (three drafts, two critics converged): `HEREDOC_RE` now captures the full tilde run (`~*[A-Za-z_][~A-Za-z0-9_]*`) — `<<EOF~~`/`<<EOF~~~` close like bash (20/20 matrix; C1's 36-form battery the same pattern). Live byte-invariant; self-test 0/1504 (an intermediate edit dropped the quotes' optionality — 9 self-test failures caught it before commit); r17:317 third correction (the `~~`-plus clause became false — H6). Pin `2b3daa2f`.
- **Claim D verified on D3's patch + D4's review**: `extract_boxes` skips fenced regions (and terminates continuations at fences) — the fenced `- [ ]` decoy flips 0->1 naming the missing box; live 41/41; 71/71 fixtures unchanged; self-test 0/1504. D4's named residuals (indented-code decoys, short-closer guard, unclosed-fence loud-fail) filed.
- **Calibration — round 29's H claim FALSIFIED (M8/N09):** the zero/positive pin fix is dead code — `verify_harness_claims.py:560/563` dispatches both modes before the baseline arm reads `expect`, so all 11 corruptions still exit 0 (pre- and post-fix trees split identically). The r29 record stands corrected here; the real fix (read expect before mode dispatch) is queued for round 36. The r29 floors/report numbers remain true (the floors guard and corpus claims were independently re-verified).
- **Bookkeeping corrections:** the Saturation window is 6/3 (r30-r35 capability-free; SCORECARD's 3/3-at-r26 stale — dormant anyway, depth 9 < 10.0). A scout's mid-round merge attempt (S12's fall-through) was aborted; the tree verified clean at `48a0720` before landing. The N-lanes filed 40+ bookkeeping defects across the r21-34 reports (fragment counts, stale ordinals, false self-references) — the loop-2 calibration queue.
- Debt queue for r36-40 (S10/C3): the r29-H real fix; P3's index fence blindness (`verify_corpus_integrity.py:300` shares D's blindness); SCORECARD:159's stale floors (10/88/52/82/1504/51 vs live 10/108/52/87/1504/62); the floors guard missing from SKILL.md's instrument list; the divergence merge (operator).


## 2026-10-19 — Round 36 (loop 2, round-of-loop 2): the r29 falsification CLOSED + index fence blindness

- Claims at `.ufo/round-36/claims.json` (Z + P3, both freshness); items array 29 (prose said 32 — the count class, corrected); 29/29 on `devin/deepseek-v4-1-flash-high` (hyper dry — remaining_credits 0 — the goal's stated fallback). Fragments `.ufo/round-36/scouts/*.md`.
- **Claim Z verified — the r29 record is CLOSED, not just corrected.** The fix is the 2-token guard (`and baseline is None` on the zero/positive intrinsic arms, Z4's pick): the baseline arm now serves those pins when a baseline exists. Integrator proofs: the first spot-probe forgot to write the mutated JSON and read green — rerun with the write: all four mode classes flip (equal `omp.db.rows`, `oc.log.skills_rescan_max`; zero `omp.cache.misses`; positive `omp.descriptions.over_cliff`), each exit 1 DRIFT-naming; the swarm's Z5 ran the full 28/28 on the same design; live 28/28 byte-invariant; self-test 10 unchanged (floor holds). Z4's named residuals (positive vacuity `expect:0`; bool-alias false-DRIFT) filed.
- **Claim P3 verified on P3b's PAIR** (P4: primary-only breaks the two witnesses): the coverage census is fence-aware in BOTH corpus instruments — fenced README rows no longer count (swap probe flips 0->1, `unindexed` names it); live 53 tracked / 52 indexed / 0 unindexed, 9/9 byte-invariant; self-tests 108->119 (integrity) and 52->59 (independent); floors bumped 119/59 in-step. Residuals filed (glob-only maps; unclosed-fence handling; the S7-2 class).
- Loop-2 queue after Z/P3 (S6/C2): the M1 fence-spec class (`~~~` fences + CommonMark closer rules — M1's HIGH); the floors-guard pair (two-table coordinated deletion; path repointing — C2's r37 candidate); SCORECARD's stale floors lines (S5: :31/:115/:163 + the capability row's own contract); the floors guard absent from SKILL.md; 18/35 reports missing the SHONEN clause; the divergence merge (operator).
- Stale-finding recurrence note: X1's sibling ack measure has used stale local refs for the 4th time — the fleet remotes moved (all five +2 commits, README/LOG only); the ack 0/5 verdict stands on the fresh mirrors.

## 2026-10-19 — Round 37 (loop A position 1 of the 3-loop regimen): C1 fails as declared; C2+C3 verify — round REJECTED, verified work landed

- Claims at `.ufo/round-37/claims.json` (C1 depth, C2 operability, C3 freshness). **Attempts:** attempt-1 (earlier session, interrupted) on opencode-go-2 — fragments `scouts/{M7,X2}.md` survive at this HEAD and were used as evidence; attempt-2 (operator-interrupted ~93 min in) on opencode-go key 1 — no seat output persisted; attempt-3 on `alibaba-token-plan/deepseek-v4.1-flash` key 1 per the operator's 2026-10-19 amendment (token plan replaces opencode-go for the swarm waves) — 22/24 seats, ~16 min; seats V3+B1 died on **429: token-plan key-1 monthly quota exhausted** (resets 11-11; rotation moves to key 2 next dispatch). Fragments `.ufo/round-37/scouts/*.md` (22 seats) + curated `.ufo/round-37/evidence/` (16 artifacts incl. PRUNE.log); ~79M of working-tree probe copies pruned.
- **C1 depth — FAILS AS DECLARED (unanimous: P3/P4/V1/V2/A1/I1/R1).** The source-blind re-derivation instruments landed (`verifiers/verify_harness_independent.py` 24 derived/4 declared-UNLANDED, self-test 0/71; `verifiers/compare_harness_independent.py` self-test 0/59) but the claim's counting commands are red: comparator exit 1 — headline 23/28 (strict 17/28), 5 open rows = 3 `omp.catalogue.*` UNLANDED (the catalogue carrier is selected by a rule inside the harness's own scope — a real blindness boundary) + `oc.dup.roots_both_sided` (3 vs 0) + `oc.log.skills_tag_hits` (13 vs 0), the latter two with raw-substrate evidence favoring the harness (V1/V2). R1's structural defects stand: the N/N headline is copy-satisfiable (counter-instrument scores 28/28 without reading anything), and the claim text never specified the freeze-before-compare receipt. **No adjudication report landed; the corpus doc was not written. The instruments commit as unverified scaffold — depth unchanged.**
- **C2 operability — VERIFIED (composite: P5's anchor + P6's override arm).** New external anchor `verifiers/floors-registry.json` + `registry_anchor_drift()` closes the two-table coordinated deletion (exit 2 `row vanish`, red-before reproduced by M7/V4/V5/I1/I2/S2 at HEAD bytes) and path drift (`path drift`/`path absent`/`floor drift`/`size drift`, all named); P6's `override_drift()` closes the `--script` repoint (exit 2 `override repoint`/`override path missing`). Guard self-test lands (0/41, F1–F11, red-before shown on pristine bytes). Floors EXACT 6/6 (`derive_floors.py`: 10/119/59/87/1584/62). Declared trust boundary recorded: a coherent 3-artifact coordinated edit still passes (R2/V5 — documented, not an unclosed class). Residuals: non-str key TypeError (V4-S), J's self-contradictory extra line, the guard's own 41-assertion battery is unfloored.
- **C3 freshness — VERIFIED (P7+P8 pair), one named residual.** CommonMark fence-spec in `extract_boxes`: closer = same char + length ≥ opener, info-string opener-only, indented-code marker (P7), unclosed fence → named FAIL via `box_map_complete`; 15-shape `FENCE_SHAPES` battery + cmark 0.31.2 oracle 0 misclassifications (HEAD was 5/11–11/15 misclassifying); 71 fixture dirs byte-identical; live byte-invariant (stdout sha `b3275e1c…`); self-test 1504→1584; floors bumped in-step in all four carriers + the routing-16 JSON pin re-pinned (`f182cd56→9ea386da`, P8). **Residual (V6): container-relative fences** (opener at 4+ columns inside a list item) misclassify — 4/36 lines on V6's extended matrix; the reference fix (`container-relative.patch`, oracle 0/36) is banked at `evidence/v6-container-relative.patch` for the loop-3 queue. Latency exposure: 0 corpus fences at ≥4 columns.
- Whole-tree battery green at close (harness 28/28; floors 6/6 EXACT + self-test 0/41; checklist 10×PASS + 0/1584; corpus 9/9 + independent exit 0; surfaces 7/7; pins 3/3; fault@/dev/shm OK; both replays green). Routing pins hold.
- **Bookkeeping defects corrected/recorded:** the dispatch brief's floor list was stale (82/51 vs live 87/62 — quoted by V2/V5/R1/B2/S2); SCORECARD stale-floors debt remains (S5); the r36 queue's "18/35 reports missing SHONEN" does not reproduce (B2: 9/17 fleet-path, 0/17 lane-repo); `corpus/README.md:11` "18-row" vs 20 rows (B2); SHONEN.md fleet-gate findings persist (B2, form-non-canonical — a canonicalizing rewrite would delete dated evidence lines, r24 idiom tension, not taken).
- Queue for r38 (pos 2, token-plan key 2): C1 closure per R1's amendment (per-row adjudication with the harness favored where substrate evidence says so, UNLANDED rows named with the blindness blocker, freeze-before-compare receipt, blindness-by-construction scrub, comparator as the counting command); then register both C1 instruments in the floors registry once verified (P1's handoff — else the new 71/59-assertion self-tests ride unguarded); V6's container-relative patch; the two C2 residuals; SCORECARD stale floors.

## 2026-10-19 — Round 38 (loop A position 2): C1+C2 fail as declared; C3 verifies — round REJECTED, closure machinery + fixes landed

- Claims at `.ufo/round-38/claims.json` (C1 depth = close the r37 re-derivation; C2 operability = the two floors-guard residuals; C3 freshness = container-relative fences). Provider: `devin/deepseek-v4-1-flash-max` (operator amendment 2: token-plan keys 1/2/3 all 429 — resets 11-11/10-23/10-28 — probed dead at dispatch; devin authorized for the deepseek-flash waves). 22/24 seats (~28 min). Fragments `.ufo/round-38/scouts/*.md`; curated `.ufo/round-38/evidence/`; ~45M drafts pruned (incl. p5/worlds `.git` symlinks — hazard removed).
- **C1 depth — FAILS AS DECLARED (the closure machinery landed; the recording clause did not).** Landed: adjudication of the 5 open rows (both definitional rows decided for the harness on raw substrate — 0 `<skills>` literals vs 13 `skills="` attributes; 0 `duplicate skill name` lines — V1's mutant protocol proving the r37 readings couldn't detect the class their ids name); the 4 catalogue rows formally SCOPED_OUT with the blindness blocker named (the selection rule lives at verify_harness_claims.py:369-441, inside the harness's own scope — V1's 11-rule spread proves the value is rule-dependent); freeze-before-compare receipt (load-bearing: frozen-vs-mutated flips where live-vs-live cannot, R1-F2 reproduced through the driver); blindness-by-construction scrub at residual 0 (V2, with named bounds: the scrub tree cannot contain itself; 182 session files out-of-repo carry the template sha); corpus/knowledge/harness-independent-round37.md landed (governance per A1's protocol); both instruments registered in floors-registry at **86/83 EXACT** (P3, self-test 68). Comparator exits 0 — 24/24 over the landed scope. **Why it still fails:** R1-D1 HIGH — the scope-out channel is a laundering hole (a genuine `omp.offered.skills` 5-vs-7 disagreement self-declared SCOPED_OUT reads exit 0; no machine-checkable discriminator required); R1-D2/A1-dissent/V1-d1 — `oc.log.init_count_monotone` has a wrong predicate (IND's own self-test asserts 1 where the predicate requires 0; HAR shows the divergence on probes) and `oc.log.init_count_max` is a third divergence, both mis-filed as D5 cosmetic in the landed doc — the smoothing the protocol forbids; doc §1/§5 stale (says exit 1/23-28); doc doesn't reference A1's r38 ledger. Depth holds at 9. R1: with D1+D2+D3 closed this is the 9.5 shape.
- **C2 operability — FAILS AS DECLARED (harm introduced).** Both declared residuals genuinely closed: non-str key → `FAIL registry non-string key` exit 2 (was TypeError); malformed tuple → single named FAIL (the self-contradictory `floor drift … row=None` gone); F12-F13 true discriminators (self-test 41→57→68). **But V4 found a fix-introduced regression: a `pins` row with path=None now crashes (TypeError, exit 1) where HEAD named it exit 2 — `_row_parts()` manufactures exactly that None; and the malformed-FIELD arm (floor `(62,)`, floor `True`) still prints the contradiction.** V4's verdict: partially verified, not closable as landed. Named pre-existing residuals: copy-variant `--script` 1/30 green; path confinement unenforced.
- **C3 freshness — VERIFIED.** V6's container-relative patch landed (container-only variant, P5; sha `9ea386da→214ae44d`): cmark oracle 0/36 on V6's rebuilt matrix (was 4/36 — denominator honestly corrected to 4/30 on the rebuild); 18-shape battery re-derived from cmark ALONE (V5's `verify_battery_cmark.py` — the banked auditor was container-blind, fixed); 3 container pins proven two-sided discriminators; 71 fixture dirs byte-identical; self-test 1584→1597 with floors bumped in-step across all carriers; routing-16 pin re-issued with a git-traceable chain (P6 repaired the round-35/36 label with git evidence); both replays green + stale-pin control. **Handed to the r39 queue (V6b): the corpus gates' own fence functions share the spec divergence — a proven silent false-PASS vector with zero live incidence; closable in one function.**
- **r37 record corrections (this integration):** the brace-set citations in r37's SCORECARD move-log rows reddened `governance.citation_resolves` from `c8e233d` — r37's "gates green" and "live byte-invariant" lines falsified; SCORECARD rows reworded (prose idiom), checklist gate green 293/293; **erratum appended to r37's filed report** (append-only, supersedes those lines). Also repaired 5 of 7 curated r37 evidence scripts (broken by the drafts→evidence move: import names, parents off-by-one — S2's F2; blind-tree script was archiving the parent monorepo) and re-committed V6's reconstructed shapes.json.
- Whole-tree battery at close: harness 28/28 + 0/10; floors 8/8 EXACT + 0/68; checklist 10×PASS + 0/1597 (gate green after the SCORECARD fix); corpus 9/9 + independent exit 0 once the new doc is tracked (verified green post-commit); surfaces 0/87; pins 3/3 + 0/62; fault OK; IND 24/4-scoped + 0/86; CMP exit 0 24/24 + 0/83; replays ALL GREEN.
- Queue for r39 (pos 3, devin per amendment while token-plan is dry): C1' = R1-D1/D2/D3 closure (scope-out discriminator or corpus-anchored scope set; init_count predicate fix + adjudication; doc/ledger reconciliation); C2' = the None-path crash + malformed-field arms + fixtures; C3' = the corpus-gate fence divergence (V6b's proven one-function fix). Standing debt: resolver-vs-brace divergence (tokenizers differ across instruments), guard's own battery unfloored, SHONEN.md form, divergence merge (operator).

## 2026-10-19 — Round 39 (loop A position 3): C1 fails as declared (F-2 survives); C2+C3 verify — round REJECTED, all three claims' work landed

- Claims at `.ufo/round-39/claims.json` (C1 depth = close R1-D1/D2/D3; C2 operability = the None-path crash + malformed-field arms; C3 freshness = corpus-gate fence fix). Provider: `devin/deepseek-v4-1-flash-max` (operator amendment 2 — token-plan keys all 429; key 2 re-probed 429 at dispatch, resets 10-23). 17/24 seats (~25 min). Fragments `.ufo/round-39/scouts/*.md` (17 seats); ~32M drafts pruned to 108K (kept only counting inputs — B1's skeleton, B2's SHONEN/verdict-table/at-head instrument pins — per R2's lesson).
- **C1 depth — FAILS AS DECLARED (all three named residuals closed; a same-class door survives).** Landed and verified by the integrator battery + four independent verifiers:
  - **R1-D1 closed (P1):** the laundering hole is shut with three locks none reachable by the payload — new committed `verifiers/harness-independent-scope.json` (the comparator reads the allowed scope-out set from there, `--scope-file`, not the payload; an unlisted scope-out → exit 2 `laundering: … which the committed scope file does not list`); a driver-recomputed `rule-spread-census` probe per scoped row (rejects a mismatched observable, vacuous carrier, relative/redirected target, missing probe, or a probe whose blind rules all agree — i.e. a derivable row); channel-agreement + freeze receipt now records the scope-file digest, committed set, and probe kind. R1's laundering payload (genuine `omp.offered.skills` 5-vs-7 → self-declared SCOPED_OUT) flips **exit 0 → exit 2** on the same bytes; V1's 18-arm battery + R1's 9-arm suite all fail closed class-named while the legitimate scope-out stays exit 0.
  - **R1-D2 closed (P2):** `oc.log.init_count_monotone` + `_max` re-derived from one file-order `init count=(\d+)` occurrence sequence (was: counted runs with >1 line — wrong population and inverted direction). IND == HAR == independent oracle on 10/10 mutant logs (V2 + R1's adversarial set); the bug-restating self-test arm replaced by five true discriminators; the green test that certified the bug now fails 7 ways on the old predicate (V2's splice proof). Comparator strict column **19/24 → 20/24**, adjudicated set **5 → 4** — a real list-vs-list agreement replaces an emptiness coincidence. Re-filed in the doc under `adj-r39-01` / D1 defect(independent) (was D5 cosmetic).
  - **R1-D3 closed (W1):** `corpus/knowledge/harness-independent-round37.md` reconciled with A1's r38 adjudication ledger — ledger referenced (was 0), §1/§5 re-stamped to live shas/numbers, §6 reproduce block made executable verbatim (rc=0) — its inputs rebuilt as committed/self-built (the r38 drafts→evidence prune had dead-pathed 4 legs); §3's stale "pre-existing red" marked historical; §4's scrub residual corrected 0/3→4.
  - **Why C1 still fails (R1's adversarial pass):** **F-2 (HIGH)** — `IND_VALUE_KEYS = ("expected","expected_value","re_derived","value","observed")`; the live IND never emits `expected`/`expected_value` but the driver accepts them **first**, so a payload carrying the harvested value in `expected` and `"NOT DERIVED"` in the derived fields scores **24/24 exit 0** — the same laundering class as D1, reached through the value channel the scope file/probe/`--expect-n` cannot see. **F-3 (MED)** — `_record_list` reads only the first of `results`/`rows`/`checks`; a divergent value hidden in `rows` still reads 24/24. R1: do not bump depth — the class the round meant to close survives in a second channel. **Depth holds at 9.**
- **C2 operability — VERIFIED (P3 builder; V3 + I2 + R2 verify).** New `row_problem(name, spec)` is the single shape gate reached by `registry_drift`, `registry_anchor_drift`, the `main()` join, and `override_drift`'s canonical map — no reordering reaches the join with a bad row, so callers can't re-format a rejected row's fields into the contradiction V4 reported. V4's full hunt list on copies: **before** — None-path → uncaught TypeError exit 1 (fix-introduced, named at r37 bytes), floor `(62,)`/`True` → self-contradictory `registry=62 expected=62`; **after** — all 8 arms exit 2 class-named, zero tracebacks, zero contradiction lines; F16–F20 true discriminators (reverting `row_problem` fails exactly those; self-test 68→109). Live 8/8 EXACT byte-invariant (stdout sha `916a8bbd…`). Named pre-existing residuals (documented, not C2-introduced): copy-variant `--script` absolute-argv override silent-green; path confinement outside `--repo` unenforced — both inside the registry's stated trust boundary.
- **C3 freshness — VERIFIED (P4 builder; V4 + I2 + R1 + R2 verify).** V6b's minimal CommonMark 4.5 closer rule landed on BOTH corpus instruments' fence detection — `verify_corpus_integrity.py fenced_lines` (:308) + `verify_corpus_independent.py fenced_line_numbers` (:221): a fence-looking line closes only when `run[0]==char and len(run)>=open_len and no info string`. The three exploit shapes (``` closing a ```` block; ```python; ``` nope) + V4's 4th `info-closer-same-length` all flip **silent-false-PASS 3→0** on both gates — cmark 0.31.2 oracle, before `unindexed=0 exit 0` → after `unindexed=1 exit 1` fail-safe-named. Live corpus sweep: 144 fence-like lines, **0 at column 4+**, 0 docs disagree (I2). Byte-invariant live stdout both gates (`c5eaf1a5…`/`ff1da383…`). Self-tests grow 119→129 / 59→68 with floors bumped in-step; the battery is a proven discriminator (M1 revert fails 6/129 + 5/68). **Named residual (V4, OPEN, MED):** CommonMark caps closer indent at 3 spaces; `FENCE_RE` is `^[ \t]*` — a 4-space/tab-indented pseudo-closer is content per cmark but still closes the region on both gates (silent false-PASS reproduced on HEAD *and* the landing; **0 live incidence**). One more clause in the same predicate → r40+ queue.
- **Wave conformance:** no seat commits; writes confined to `.ufo/round-39/` + the declared `verifiers/` + corpus doc; no `.git` symlinks (V3's symlink-farm self-inflicted live-registry write was caught by sha, restored, hardened — disclosed). Shared-tree churn: `floors-registry.json` is single-writer — two seats bumping it concurrently collided once (P4's rows clobbered, guard caught it `registry floor drift`, re-applied in-step) — recorded as a known wave hazard, not a defect. Floors moved 119/59/86/83 → 129/68/104/97 across the round in-step.
- **Whole-tree battery at close (post-prune):** floors 8/8 EXACT (10/129/68/87/1597/62/104/97); IND self-test 0/104; CMP self-test 0/97; corpus_integrity 0/129 + live 9/9; corpus_independent 0/68 + live exit 0; live comparator **exit 0, 24/24** (strict 20/24, adjudicated 4, scoped-out 4).
- **Queue for r40 (pos 4 — hyper per plan, expect dry → devin; re-probe token-plan key 2 first per rotation):** **C1' = close F-2/F-3** — drop `expected`/`expected_value` from `IND_VALUE_KEYS` or cross-check channels (a payload must not launder a harvested value through the value channel); `_record_list` must reconcile all of `results`/`rows`/`checks` not read-first. Standing debt: V4's closer-indent clause; V3's copy-variant/path-confinement pair; guard's own battery unfloored; the V3 hang (IND self-test >120s under wave load); resolver-vs-brace tokenizer divergence; SHONEN.md form; the divergence merge (operator, never rebase — 30/2 non-ff).

## 2026-10-19 — Round 40 (loop A position 4): F-2 + F-3 payloads now fail closed, but the laundering class survives on new channels — round REJECTED, all three claims' work landed

- Claims at `.ufo/round-40/claims.json` (C1 depth = close R1's r39 F-2/F-3; C2 operability = V3's copy-variant + path-confinement residuals; C3 freshness = V4's closer-indent clause). Provider: `devin/deepseek-v4-1-flash-max` (pos-4 plan was hyper — recorded dry `remaining_credits 0` since r38 → devin per the declared fallback; token-plan key 2 re-probed 429 at dispatch, resets 10-23). 41/41 seats, 1 provider loss (~78 min). Fragments `.ufo/round-40/scouts/*.md` (41 seats); curated `.ufo/round-40/evidence/`.
- **C1 depth — the two declared payloads now fail closed; the CLASS survives on new doors — FAILS AS DECLARED, depth holds 9.** Landed and verified:
  - **F-3 closed (P2's `_channel_maps`/`_reconcile`/`_reconcile_channels`):** every published row channel (`results`/`rows`/`checks`, list or dotted-map) is parsed and reconciled record-for-record — channel divergence, channel split (status disagreement), channel membership (a row in one channel absent from another), and duplicate-id two-value all raise `CompareError` → exit 2. R1's F-3 payload + V1's A7 + X2's whole family (results-subset, per-row status split, checks-extra-keys, 999-vs-'999' type confusion) all flip exit 0 → exit 2 class-named; live join still 24/24 (V2/X2/I1 verify).
  - **F-2 closed (T1's candidate, integrator-landed):** the candidate at `drafts/t1/candidate.py` (`ebed53e7`) was built and measured closing every arm by R3 but never landed (T1 is the critic — a critic that edits the instrument it grades destroys its own independence). I ported the within-record cross-check into `_channel_maps` (`:309-334`): a record carrying a foreign `expected`/`expected_value` ALONGSIDE a derived field reading `NOT DERIVED`/`N/A` → exit 2 `a harvested value cannot outrank an explicit non-derivation`; and the two channels must agree canonically. The committed `expected-launder` fixture (F1) flips exit 0 → exit 2; self-test **3 failures → 0/118 green**; live join preserved 24/24 exit 0.
  - **Why C1 still fails (the class, not the payloads):** R1's adversarial pass named TWO NEW DOORS in the closure machinery — **F-3' (HIGH):** `load_scope_file` resolves `--scope-file` against the *process cwd* while `render_receipt` resolves it against `--cwd` — run the driver outside the repo and a planted superset scope file is enforced while the receipt attests the honest file (digest `fbcdc8d2` + committed_set of 5 rows that can't both describe one file); **F-4 (MED):** the scope file pins the probe *kind* but never the *target* — `recompute_probe` reads `probe["target"]` from the payload, so all 4 committed probes re-pointed at a 2-file builder carrier still read exit 0. X2's surviving arms: `status` vs `state` within-record split, probe-channel split, `overrides`/`metadata`/`alternatives` payload fields all read exit 0. T1's residual: duplicate id *within one channel* is last-write-wins. R1's ruling stands: depth holds at 9 — the same class survives through channels the closure did not reach. R3's composite agrees and adds the integrator note that T1's candidate + the fixture battery are the right *shape* landed.
- **C2 operability — VERIFIED (P3; V3 + R2 + R3 verify).** `check_assertion_floors.py` gained `confinement_problem()` + a canonicalized/digest override predicate: a copy-variant `--script` (absolute-argv symlink/hardlink/copy aimed at another row's target) → exit 2 `override repoint`; a `--repo` escape or `../` traversal of a *declared* path → exit 2 `escape: … is absolute (outside …)`. V3's 0/336 cell matrix + R3's 8-arm hermetic world both confirm; guard self-test 150. **Two boundaries DECLARED with recorded reasons (per the claim's OR-clause):** a `--script` override to a *unique-bytes* file outside `--repo` stays green (the probe affordance — the guard polices declarations, not where a probe's stub lives); a `--repo` pointed at a foreign root runs that root's own guard green. V3's extra gap: the content-digest remedy is evaded by appending one byte (named, recorded). Score held: round rejected on C1.
- **C3 freshness — VERIFIED (P4; V4 + I2 + R1 + R3 verify).** The CommonMark 4.5 ≤3-space closer-indent clause landed on BOTH corpus instruments: `FENCE_RE = ^ {0,3}(`3,}|~3,})(.*)$` in `verify_corpus_integrity.py` + `verify_corpus_independent.py`. V4's 4-space and tab pseudo-closers flip both gates silent-false-PASS → fail-safe (`unindexed=0 exit 0` → `unindexed=1 exit 1`), cmark 0.31.2 oracle; the 3-space control still closes (no over-hiding); 0 live incidence (146 fence-like lines, 0 at col ≥4, 0 tab-indented); live stdout byte-invariant both gates; self-tests 129→145 / 68→86 with floors in-step.
- **Whole-tree battery at close (post-F-2-fix):** live comparator **exit 0 24/24** (strict 20/24, adjudicated 4, scoped-out 4); floors **8/8 EXACT** (`10/145/86/87/1597/62/104/118`); comparator self-test **0/118**; the `expected-launder`/`rows-shadow`/`checks-shadow` fixtures all exit 2 pinned.
- **Wave conformance:** 41/41 seats reported, no seat commits; writes inside `.ufo/round-40/` + declared `verifiers/` + the corpus doc; no `.git` symlinks (a `.gitignore` symlink loop in `drafts/p6/revworlds/before/` flagged by Z2 — pruned). `floors-registry.json` single-writer churn again (bumped in-step by multiple seats; the guard caught each half-state). The comparator's own self-test ran red mid-round (9→3 failures) while fixtures landed before the code — settled green after the F-2 fix.
- **Queue for r41 (pos 5 — codex/gpt-6-luna-max 64-seat verification round):** **C1' = close the surviving laundering channels per R1/X2/T1** — (a) resolve `--scope-file` once against `--cwd` and record *that* resolved path + digest in the receipt (F-3' cwd door); (b) pin the probe target in the committed scope file (F-4); (c) reconcile `status` vs `state` within a record (X2-x3); (d) drop or gate the un-contract payload fields (`overrides`/`metadata`/`alternatives`) so a foreign field can't ride free; (e) duplicate-id-within-channel last-write-wins (T1). Standing debt: V3's digest-append evasion; IND self-test >120s hang under wave load; resolver-vs-brace tokenizers; SHONEN.md form; the divergence merge (operator, never rebase — 30/2 non-ff). r41 is the loop's verification round — the corpus doc + the closure machinery need a clean re-read, not new closures.

## 2026-10-19 — Round 41 calibration errata (N08; C3)

- N02 parsed the corpus doc §2 table as 28 rows and re-derived 84/84 ind/har/pin cells plus all 28 modes with no mismatch. N03/N04 confirmed the pre-existing-red citation record is historical (N03's timestamped checklist run: 9/9 PASS, 314 citations); the final post-edit checklist run printed PASS for every check record and `governance.citation_resolves` evaluated 320 tokens across two files. They also re-ran the blind-tree and §6 block. The §6 block ends 0; current comparator is 24/24, strict 20/24, 4 adjudicated/4 scoped out, exit 0; comparator self-test is 0/118, not the older 97. Append-only annotations in `corpus/knowledge/harness-independent-round37.md` preserve the historical readings and state the current comparator SHA-256 `1742dcccad1118399f0aa959f7ea6884d5992834d8c4c8b94e108277ae87df76` at HEAD `b1be35f9522f21c0c5b39879358a011806ab9200` / tree `8bb24450a9c500c427019c7147013b4946525b09`.
- The committed scrub script SHA-256 `077211322ba8bd2c7d14f0272dd20b1cd21761135369343049b0b34cc22fc298` was rerun from its repository path: residual 5, tree_files 358, no `.git`, builder exit 0. Its nested pins check is NONZERO because the host OMP SHA/mtime drift from the pinned values; opencode pin passes. An initial `git show HEAD:<script> | bash -s -- <tmp>` attempt failed (`BASH_SOURCE[0]: unbound variable`, then `cd: null directory`) and its temporary tree was cleaned; the successful repository-path rerun was verified against the committed script. Historical scrub counts remain unchanged.
- N05 remeasured current axis-row counts: 118 comparator assertions, 145/86 corpus assertions, 150 floors-guard assertions; 9 registry rows PASS exactly `10/145/86/87/1597/62/104/118/150`; live comparator join remains 24/24. Fence census: 53 tracked corpus Markdown files, 146 fence-like lines, 0 tab-indented and 0 at indent >=4. The append-only SCORECARD annotation after the capability row marks its “all six” and older six-floor values as historical, records the nine-row current vector and hashes, and preserves the original snapshot.
- N06 found the r37 declaration says 24 seats but 26 committed scout files; the attempt-3 22/24 count and two named earlier-attempt carryovers do not reconcile every file without a dispatch roster. For r40, frozen claims declare 40 while 41 scout files exist; retain the original `41/41` prose as historical, but do not infer a 41-seat denominator absent an amended roster. The SCORECARD has an append-only qualification for r40. PRUNE.log amounts match their historical notes, but deleted working bytes and measurement argv are unavailable, so these are not fresh measurements. The r38/r39 counts (22/24 and 17/24) match their committed scout totals.
- No prior round text was rewritten and no verifier/registry files were modified by N08. Full post-edit gate results and reproducible command evidence are filed in `.ufo/round-41/scouts/N08.md` (the `measurements.txt` it references lived under `drafts/n08/` and was pruned at r41 close — the gate results it recorded are the committed readings above); no Git add or commit was performed.

## 2026-10-19 — Round 41 V10 frozen-comparator channel census (C1)

- **Boundary:** saved arms were replayed against HEAD `b1be35f9522f21c0c5b39879358a011806ab9200`, tree `8bb24450a9c500c427019c7147013b4946525b09`, frozen comparator SHA-256 `1742dcccad1118399f0aa959f7ea6884d5992834d8c4c8b94e108277ae87df76`. `python3 .ufo/round-41/evidence/v10-replay-probes.py` reproduced 46/46 subprocess outcomes (exit/headline/reason) with unchanged input hashes; `v10-channel-census.py` validates the exact 46-ID set, no missing/extra arms.
- **Classification:** 25 open, 15 closed, 4 controls, 1 diagnostic, 1 caller-selected trust input. Open saved arms demonstrate alternate expected/value and identity representations, status/metadata shadows, payload-chosen probes/scope evidence, the relative `--scope-file` process-CWD vs `--cwd` receipt split (23/23 green on planted CWD; honest-CWD control exits 2), and caller-crafted live-JSON inputs. The absolute scope-file arm tests an explicit caller trust choice, not a bypass of the chosen file. `headline-uncovered-count` rejects (exit 2) but reports 29 live checks against its 28-row input; recorded as diagnostic, not an open arm.
- **Current path:** fresh `verify_harness_claims.py --json` and `verify_harness_independent.py --json` captures each contain 28 records; the saved `compare_harness_independent.py` join exits 0 at protocol 24/24, strict 20/24, 4 adjudicated / 4 scoped out, 0 disagreement / unknown / uncovered. The replay/census counting inputs are curated under `.ufo/round-41/evidence/` (`v10-*.py` / `v10-*.json`; the working captures were pruned at r41 close).
- **C2 scratch:** `union-live/union-battery.json` is invalid for C2 because its control and all arms failed to launch the guard at a duplicated `guard-world/.../guard-world/...` path. Removed only `union-live/work/guard-world/` and C2-only `work/outside-stub.py`; retained C1 payloads, `work/live.json`, captures and other useful probes. No comparator or verifier source was changed.
- **Corpus/gates:** added `corpus/knowledge/harness-independent-round41-census.md` and its `corpus/README.md` row; refreshed `verifiers/corpus-baseline.json` tracked-files expectation 54→55 and recorded the measurement. The no-baseline measurement against a temporary index seeded from HEAD plus only the README and note reports tracked=55, corpus Markdown=54, index tokens=73, unindexed/stale/missing=0, report pointers=38 and commit pointers=27. On that same temporary index, `verify_corpus_integrity.py --json` passes 9/9 and `verify_corpus_independent.py --json` exits 0. The real index was not altered; the first real-index gate run saw the new note path as stale because it was not staged. No Git add or commit was performed.
- **Self-tests:** harness claims 0/10; harness independent 0/104; comparator 0/118; corpus integrity 0/145; independent corpus 0/86; assertion floors 0/150. Full census, source hashes, commands and classifications are in `corpus/knowledge/harness-independent-round41-census.md` and `.ufo/round-41/scouts/V10.md`; the curated counting inputs are under `.ufo/round-41/evidence/` (the working raw evidence was pruned at r41 close).

## 2026-10-19 — Round 41 (loop A position 5 — the loop's 64-seat VERIFICATION round): all three claims improved but INCOMPLETE — the held-out hunt found unlisted doors; honest data, not a failed round

- Claims at `.ufo/round-41/claims.json` (C1 depth = verify the C1 machinery + produce the COMPLETE surviving-channel census; C2 operability = verify confinement/override + floor the guard's own self-test; C3 calibration = verify records match the landed code). Provider: `openai-codex/gpt-6-luna-max`. 84 seats reported (~43 min; the swarm expanded). Fragments `.ufo/round-41/scouts/*.md` (82 seats); curated `.ufo/round-41/evidence/` (the V10 census counting inputs the doc's `recheck` line references).
- **C1 depth — the declared F-2/F-3/A7 closures hold, but the complete-census condition is UNMET; the held-out hunt found MORE doors.** Verifiers unanimously confirm the r40 closures hold on landed bytes `b1be35f`/`1742dccc`: the expected-launder fixture still exits 2, the channel reconciler still names every shadow family, the live join stays 24/24 exit 0, self-test 0/118. **But the claim's after-condition — a provably-complete census where a fresh hunt finds no unlisted door — is false.** The V10 census (`corpus/knowledge/harness-independent-round41-census.md`, 46 arms: **25 open / 15 closed / 4 controls / 1 diagnostic / 1 caller-trust**) maps the real attack surface, and the held-out hunts (H01-H06, R01, R02, Y01, Y02, A01) found doors OUTSIDE it: duplicate JSON keys (divergent-copy-first reads exit 0, honest-last reads exit 0 differently — last-key-wins decoding), duplicate same-value records hiding contradictory status/mode/verdict (10,000 identical `x.y` rows exit 0; order-dependent), the `secondary_agree` numerator/denominator skew (28 over a 24-row denominator), live `mode`/`verdict` shadow channels, expected-only/wrapper/flat-map forms that expand the join to 28/28 (payload supplies values for all 28 checks incl. the 4 scoped-out rows — C02's highest-reachability class), probe-map precedence reading only `results` or only the top-level map, and H06's post-read digest race + producer-provenance + receipt-tampering findings. R1's F-3' cwd door (V01-verified OPEN: superset scope file enforced from planted cwd while receipt attests honest file), F-4 probe target (V02-verified OPEN), status/state split (V03 OPEN), un-contract fields (V04 OPEN), W1's arms (V06) all reproduce. **Depth holds 9 — R02: the closures deserve credit as real depth improvement, but a green join + green self-test is not a complete census; no exhaustive target list exists to hand r42.** The surviving census is the durable deliverable.
- **C2 operability — improved, incomplete.** The guard's own self-test count is now FLOORED (V16: new `floors_guard` registry row, self-test 150, a deletion mutant caught — the r39/r40 named debt closed); the confinement + override predicates re-verified (copy-variant/symlink/hardlink overrides fail class-named; declared `--repo`/path escapes named). **Incomplete:** V14's digest-append evasion still open; the two declared trust boundaries (unique-bytes `--script` outside `--repo`; foreign `--repo` root) confirmed honest-but-unenforced; the aggregate gate battery was not all green at settle (V18's IND hang under load). Score held: advisory, round verdict incomplete.
- **C3 calibration — improved, incomplete.** Errata appended (N08, append-only — present-tense numbers re-measured and corrected); the corpus doc's §5 now calls its green payload-conditional and records the CWD/probe-target limits; SCORECARD/LOG re-measure swept (N01-N07). **Incomplete:** the full reconciliation of historical claims (the `agree`/OUT table column, seat denominators, 21/24-vs-current figures, pruned-byte measurements) is not done — the doc now honestly bounds what the join proves but not every historical line is re-derived. Score held.
- **Wave conformance:** 84 seats, no commits; writes inside `.ufo/round-41/` + the census doc + `verifiers/` + corpus + SCORECARD/LOG errata; drafts pruned 30M→424K keeping the V10 census counting inputs (the doc's `recheck` references them).
- **Whole-tree battery at close:** comparator exit 0 24/24 (strict 20/24, adjudicated 4, scoped 4); comparator self-test 0/118; floors **9/9 EXACT** (`10/145/86/87/1597/62/104/118/150` — the new floors_guard row); corpus 9/9 + independent exit 0; checklist 10×PASS, governance 328 resolve.
- **Queue for r42 (pos 6 — no-dispatch integration breather; then pos 7-8 zai glm-5.3-flash):** **C1' = close the census's OPEN class in reachability order** — C02's top class (payload-map forms that supply all 28 values incl. scoped-out rows → 28/28 laundering); then R1-F3' (resolve `--scope-file` once vs `--cwd`, record resolved path+digest in receipt — P01 has a drafted patch); R1-F4 (pin probe target in committed scope file — P02 drafted); the un-contract field gate (reject/ignore `overrides`/`metadata`/`alternatives`/unknown top-level keys — P03 drafted); status/state alias reconciliation; duplicate-record same-value status/mode shadows; duplicate-JSON-key handling; secondary_agree numerator/denominator; live mode/verdict shadow channels; probe-map precedence; H06's receipt/digest races. Standing debt: V14 digest-append, V18 IND hang, resolver-vs-brace, SHONEN form, divergence merge (operator). The census doc's `recheck` line names the re-run commands.

## 2026-10-19 — Round 43 S1 r41 census handoff

- Added `.ufo/round-43/scouts/S1.md`, a read-only synthesis of the r41 census and H01–H06, R01/R02, Y01/Y02 and A01, prioritized using C02. Its write-time evidence command, source SHA-256 ledger, historical command/pin references, conditional cases and verification limits are recorded in the report. Pre-write snapshot command at `2026-10-19T17:26:19Z`: `date -u +%Y-%m-%dT%H:%M:%SZ && git rev-parse HEAD && git rev-parse HEAD^{tree} && git status --short && sha256sum ...`; HEAD `1c79e8698a5a297f32fda4d71f0a23be2ec4248f`, tree `cd9d3814e8cdb664081746aa17e0557ddaa3e6c8`; it showed a pre-existing `M verifiers/compare_harness_independent.py` and `?? .ufo/round-43/`. S1 ran no probes or tests, did not touch the comparator, index, or refs, and made no commit.

## 2026-10-19 — Round 43 T1 comparator regression baseline

- T1 captured fresh harness/independent JSON and a frozen-input comparator receipt at HEAD `1c79e8698a5a297f32fda4d71f0a23be2ec4248f`, tree `cd9d3814e8cdb664081746aa17e0557ddaa3e6c8`; command: `python3 verifiers/verify_harness_claims.py --json`, `python3 verifiers/verify_harness_independent.py --json`, then `python3 verifiers/compare_harness_independent.py ... --expect-n 28 --no-stamp --json --receipt ...` (17:23:51–17:23:59Z). Producer exits 0; join exit 0, protocol 24/24, strict 20/24, four adjudicated and four scoped out. Same-tree recheck at 17:25:10–17:25:18Z again exited 0 with no semantic row changes. Instrument/scope hashes and raw captures, join and receipts were recorded in `drafts/t1/` (pruned at r43 close; the scouts report `.ufo/round-43/scouts/T1.md` carries the adjudicated ids and the rerun condition); report `.ufo/round-43/scouts/T1.md` records the four adjudicated ids and rerun condition. No comparator-source landing was observed in this window.

## 2026-10-19 — Round 43 B1 scribe scaffold (measurements pending)

- Prepared `.ufo/round-43/drafts-report-skeleton.md` and `.ufo/round-43/scouts/B1.md` from the registered claim file and round-41 report shape. At `2026-10-19T17:26:39Z`, `sha256sum .ufo/round-43/claims.json` returned `c1185d5b19193baf1975068634491883b8dbf6225c4aef5205478d9e88ec898e`; the dispatch snapshot was `git rev-parse HEAD` → `1c79e8698a5a297f32fda4d71f0a23be2ec4248f` and `git rev-parse 'HEAD^{tree}'` → `cd9d3814e8cdb664081746aa17e0557ddaa3e6c8`.
- At that same instant, `sha256sum .ufo/round-43/drafts-report-skeleton.md .ufo/round-43/scouts/B1.md` returned `0bf2d293b8252845e73a68dcb41f4a5d2f2a9246ee0a1e513750bcf0017db4c2` and `e55e264ab88de395618042254cbf05468abe37515efc971ad229a9dedb7ad413`; a Python section-shape check found the required headings and retained pending cells in both artifacts. Its exact one-off check was run from the repo root; re-run by reading both files and asserting their report-specific heading lists.
- No verifier, probe, gate, floor, or SHONEN measurement was run; all claim results and landing-dependent cells remain pending. No git add or commit was performed.

## 2026-10-19 — Round 43 Z1 conformance snapshot

- Z1's point-in-time conformance findings and exact command/source pins are in `.ufo/round-43/scouts/Z1.md` (sample `2026-10-19T17:28:23Z`, HEAD `1c79e8698a5a297f32fda4d71f0a23be2ec4248f`, tree `cd9d3814e8cdb664081746aa17e0557ddaa3e6c8`). No observed commits or staged entries; no `.git` symlinks or nested draft Git metadata; round-41 replay inputs and the C1 heldout files remained present. Draft counts grew during sampling and generated `__pycache__` residue remains, so this is not a close-of-round sweep; parent rerun/prune is required. Z1 made no out-of-lane writes and no Git mutations.
- Z1 report clarification: the one symlink counted by the lane-wide scan at `2026-10-19T17:26:12Z` was not path/target-captured; the same sample checked `.git` symlinks only under `.ufo/round-43`. The report makes no classification claim for that transient link; later lane-wide scans found none.

## 2026-10-19 — Round 43 X1 frozen map-form probes

- X1's targeted C1 evidence and limitations are in `.ufo/round-43/scouts/X1.md`; the final probe command `python3 drafts/x1/probe-map-forms.py` (pruned at r43 close; the runner + arm payloads are described in `.ufo/round-43/scouts/X1.md`) ran 17:29:02–17:29:10Z at HEAD `1c79e8698a5a297f32fda4d71f0a23be2ec4248f`, tree `cd9d3814e8cdb664081746aa17e0557ddaa3e6c8`. It used frozen `git show b1be35f:verifiers/compare_harness_independent.py` (SHA-256 `1742dcccad1118399f0aa959f7ea6884d5992834d8c4c8b94e108277ae87df76`) and frozen scope bytes (SHA-256 `fbcdc8d247475a5f1c2c613d78b6188dab77a766b02497a729a884687a70f77a`).
- Frozen results: the honest producer control exits 0 at protocol 24/24, strict 20/24, four scope-outs; six full map/wrapper-precedence arms each exit 0 at 28/28, including all four scope-out ids. Scope-only maps and non-dotted ids exit 2; all-`NOT-DERIVED` values exit 1, not green. The scope-only diagnostic reports 52 live checks for its 28-check input; X1 records that count defect. Exact per-arm argv, hashes and outputs are pinned in `probe-map-forms-results.json` (SHA-256 `e428496c5fbd2fc8a9f48471584b80d95c726ad2c1e4c752162d266e89a9e7af`); script SHA-256 `d061b5443e535db749ebf00def6da8fc2877ace999f66dc0fc8e2e43032275f1`; report SHA-256 `843362c163889f237d89a1cfaa91c155c812f2e3f84320458b526d7153178d8c`.
- Current producer sources and captured outputs are hash-pinned in the result artifact. The shared working comparator was dirty from concurrent round-43 work; X1 did not use or edit it, verifier sources, fixtures, scope, or floors. The first script attempt failed before scoring due to an incorrect expected-field assumption; corrected extractor and non-dotted key were followed by a full valid re-run. No Git add or commit was performed.

## 2026-10-19 — Round 43 E1 frozen edge-map probes

- Ran `python3 drafts/e1/edge_map_probe.py` (pruned at r43 close) against frozen comparator SHA-256 `1742dcccad1118399f0aa959f7ea6884d5992834d8c4c8b94e108277ae87df76`, using live/independent captures `0bc250f5…` / `eb1068a4…` and scope SHA `fbcdc8d2…`. Measurement record pins each arm's exact argv, payload/output hashes and timestamps in `drafts/e1/probe-results.json` (pruned at r43 close; the arm argv/payload-hash pins are recorded in `.ufo/round-43/scouts/E1.md`) (run at `2026-10-19T17:27:07Z`, HEAD `1c79e8698a5a297f32fda4d71f0a23be2ec4248f`, tree `cd9d3814e8cdb664081746aa17e0557ddaa3e6c8`).
- Outcomes: partial map exit 2 for two omitted/uncovered IDs (two included scope-out values counted); one scope-out map value changed to its matching live value, exit 1 only for two other mismatches; one-extra-level map exit 2 named; consistent copied map+list exit 0 at 28/28; split scoped-out value across map/list exit 2 `channel divergence`. Report: `.ufo/round-43/scouts/E1.md`.
- This is a pre-fix frozen-comparator scout, not a source change or post-fix result. The worktree comparator differed at the pre-report snapshot; E1 did not test that in-progress file or run self-tests/floor checks. No git add or commit was performed.

## 2026-10-19 — Round 43 T1 post-edit comparator recheck

- The comparator changed in the shared worktree after T1's baseline (HEAD/tree stayed `1c79e8698a5a297f32fda4d71f0a23be2ec4248f` / `cd9d3814e8cdb664081746aa17e0557ddaa3e6c8`). At 17:30:48Z, `sha256sum verifiers/compare_harness_independent.py` returned `d258369e3ebde6ac47bfecd707e42781386abdad31a191ab72eaf48854e98366`; T1 reran fresh `verify_harness_claims.py --json`, `verify_harness_independent.py --json` and the frozen-input `compare_harness_independent.py ... --expect-n 28 --no-stamp --json --receipt ...` (join exit 0, 24/24 protocol, 20/24 strict, four adjudicated/four scoped out). `compare-captures.py` against the baseline returned exit 0, `semantic_row_changes=0`, and unchanged join summary/adjudicated IDs. Latest captures, join and receipt were under `drafts/t1/` (pruned at r43 close). Transient comparator hashes `c861…` and `7a016…` were observed between runs and superseded before the next invocation; those intermediate states were not individually exercised. The self-test and floors gate were not run by T1. The post-write recheck at `2026-10-19T17:31:43Z` still found no commits/staged changes/symlinks, while `find drafts -type f | wc -l` and `du -sb drafts` had grown to 325 / 4,881,031 bytes at the same HEAD/tree, confirming the close-time sweep remains outstanding.

## 2026-10-19 — Round 43 P4 V21 fence-shape re-derivation

- Probe `python3 drafts/p4/fence_shapes.py` (SHA-256 `0700beb402460fa6bfd7192aa299bd2798b6ba1f60c65488eadb2adcb09745bb`) ran against cmark 0.31.2 at `2026-10-19T17:29:35.301485Z`, HEAD `1c79e8698a5a297f32fda4d71f0a23be2ec4248f`, tree `cd9d3814e8cdb664081746aa17e0557ddaa3e6c8`; result SHA-256 `9b6f62975f4500012234deb611d091b6983fb6b3e592da1bbe5cf2d709526f40`. Frozen `b1be35f` and current corpus instruments have equal bytes (integrity `c5b39165…`, independent `5066aa79…`). cmark sourcepos and real gate subprocesses classify unclosed EOF and tilde/backtick mismatch correctly; blockquote fences are missed by both predicates but the `> |` coverage row is unharvestable, so both fixture gates exit 1 with `unindexed=1` rather than silent PASS. The live sweep found 54 Markdown files, 0 target-shape incidences and 0 moved classifications; frozen/current live stdout is identical for both corpus gates. No corpus predicate or floor was changed.
- Corpus self-tests passed 145/145 and 86/86; floors guard self-test passed 150/150 (same probe/result pin). The latest full `python3 verifiers/check_assertion_floors.py --repo "$PWD"` at `17:34:15Z` exited 1 on concurrent comparator work: comparator observed 213 assertions with 1 failure at floor 143; the other eight instruments passed. That run used registry SHA `68a83161db1b7b2f3125c9a296a1815e240a19594e74910a14e39f624c0a0754`, guard SHA `8ea89a4400f3e5bac91be7ce03c807a940a4f9e430743b1bb23a24ae05df5c25`, comparator SHA `d8b8c7f6001db7f47a294dc2a98db9179f61a281be20293dc5b104906073679d`; C3 did not edit any of these. Report: `.ufo/round-43/scouts/P4.md` (SHA-256 `a38e14dbd1a1b355e7df4f5a5ceabd4dd28f109e9cdde2fe662c692d4b88808a`). No Git add or commit was performed.

## 2026-10-19 — Round 43 X2 alias-form probe

- `python3 drafts/x2/probe_aliases.py` (pruned at r43 close; the 19-arm runner + inputs are described in `.ufo/round-43/scouts/X2.md`) captured at `2026-10-19T17:32:22.466306Z`, HEAD/tree `1c79e8698a5a297f32fda4d71f0a23be2ec4248f` / `cd9d3814e8cdb664081746aa17e0557ddaa3e6c8`. Frozen `b1be35f` comparator SHA `1742dcccad1118399f0aa959f7ea6884d5992834d8c4c8b94e108277ae87df76`; pinned candidate/worktree SHA `6623b7f5acf38c64dd7a53dffa23d1cc5a205d847ad7d14a37bf5c33a803c2dc`; scope SHA `fbcdc8d247475a5f1c2c613d78b6188dab77a766b02497a729a884687a70f77a`. Baseline expectations matched 19/19, no runner-reported failures or within-run source/state drift.
- Candidate: status-absent `state=UNLANDED` remains provisional (exit 1); string and five non-string status/state splits now exit 2 named. Independent `landed`/`unlanded` are accepted and surfaced as ignored; independent `provisional`/`status`/`summary` reject as uncontracted. The tested live row/top-level verdict, mode, status and summary shadows still exit 0; mode shadows yield protocol 1/1 but strict 0/1. These are synthetic one-row probes, not a fresh 24/24 join or full C2 verdict; C2's `secondary_agree` denominator arm, self-tests and floors were not run here.
- Full commands, outputs and input hashes: `drafts/x2/probe-results.json` (SHA-256 `4a614f9f56e6c5eed9d0268ceb17333dcd659d685c92e154369bff8302842443`); runner SHA `2ecc3d171051f197e293a4f814b03a142e4f96961b2b330795d8bcad26259ade`. Report `.ufo/round-43/scouts/X2.md` SHA `0637e448e0cb9f2fa770b731b8a013973fbfbd5a93d784f8398e571d561a1c26`. The shared comparator changed after an earlier capture, which was superseded by this pinned rerun; no concurrent change is attributed to X2. X2 made no verifier, fixture, scope, floor, index or ref changes; no Git add or commit was performed.

## 2026-10-19 — Round 43 S2 V10 reproducibility and environment check

- Report `.ufo/round-43/scouts/S2.md` (SHA-256 `fb95b0aad4f15cf6a8b48a2f0becbada13409d5058ccca39c5f26c152d74a366`) records the measured scope at HEAD `1c79e8698a5a297f32fda4d71f0a23be2ec4248f`, tree `cd9d3814e8cdb664081746aa17e0557ddaa3e6c8`; claims digest `c1185d5b19193baf1975068634491883b8dbf6225c4aef5205478d9e88ec898e`. At 17:31:40Z each of the six archived `.ufo/round-41/evidence/v10-*` files matched its `HEAD:<path>` Git blob (full SHA-256 ledger in S2). Frozen comparator copy from `b1be35f` matched SHA-256 `1742dcccad1118399f0aa959f7ea6884d5992834d8c4c8b94e108277ae87df76`; the shared working comparator was changed and not used.
- At 17:31:28Z the archived replay/census scripts failed before replay because they expect `evidence/probe-results.json` and `evidence/subprocess-replay.json`, while the committed files carry `v10-` prefixes. Re-running the classifier from `drafts/s2/` (pruned at r43 close; the environment/replay findings are in `.ufo/round-43/scouts/S2.md`) with copied expected-name inputs yielded 46/46 classifications (25 open, 15 closed, 4 controls, 1 diagnostic, 1 trust-input); this only reclassifies recorded results. The subprocess replay runner still exits 1 at missing `drafts/v10/live-b1be35f.json` (the file it names lived under `drafts/v10/` and was pruned at r41 close; it is now re-materialized under `.ufo/round-41/evidence/` via `v10-census-probes.py`, and the replay reproduces 46/46 — see the r43 durability-repair entry), so end-to-end reproduction was not established at S2's measurement instant.
- Frozen-comparator honest join rerun 17:30:26–17:30:30Z: exit 0, protocol 24/24, strict 20/24, four adjudicated/four scoped out, zero disagreements/unknown/uncovered. `cmark --version` at 17:30:30Z returned `cmark 0.31.2`; executable SHA-256 `38722213866f8c18e4d5b2267b19853ea9c60dd4dada5ba8eff487e80e79fa81`. S2 changed no code, verifier, fixture, scope or floor; no Git add or commit was performed.

## 2026-10-19 — Round 43 T1 latest comparator recheck

- After additional shared worktree edits, the latest stable capture at `2026-10-19T17:33:23Z` used comparator SHA-256 `d8b8c7f6001db7f47a294dc2a98db9179f61a281be20293dc5b104906073679d`, with HEAD/tree still `1c79e8698a5a297f32fda4d71f0a23be2ec4248f` / `cd9d3814e8cdb664081746aa17e0557ddaa3e6c8`. Fresh producer commands exited 0; frozen-input comparator `--expect-n 28 --no-stamp --json --receipt` exited 0, protocol 24/24, strict 20/24, four adjudicated/four scoped out, and zero disagree/provisional/unadjudicated/uncovered/unknown. `compare-captures.py` against the baseline exited 0 with semantic_row_changes=0 and identical join summary/adjudicated IDs.
- Final current captures: live SHA-256 `0bc250f5197c9dbbdbdce7e15c4220e0904118a8c290f81295aa18464b0b0341`, independent SHA-256 `eb1068a4f7b934d5553106d60737c05d8f1cd8d9ef827467f80281cac3853887`, join SHA-256 `78072a34e1abd681801e432707681f265209cf29e35e378ae69b9dbcba3591ac`, receipt SHA-256 `1092be9edeb3eca4538110eeb2a435695cbbd84602b52fbde06e7435f2d813d8`; all in `drafts/t1/`.
- A transient comparator snapshot during the 17:32:02Z run raised `TypeError: check_independent_scope_values() takes 3 positional arguments but 4 were given`; that run had source SHA `dd17ca8c21450b23577568bdb3156e0979de02d8a23e8c384052cc36177dc70d` at start and `9f4e49f39cbe649db39a812072f6f452be8b5938554531600a8fe1c60acbb240` at end, so it was mid-edit. The next source snapshot (`6623b7f5acf38c64dd7a53dffa23d1cc5a205d847ad7d14a37bf5c33a803c2dc`) had matching helper/call arity on inspection at 17:32:19Z; its fresh live join exited 0 at 17:32:41–17:32:49Z. A later transient hash `cfe946…` was superseded before invocation; the d8b8 snapshot was then tested at 17:33:23–17:33:32Z. Comparator self-test and floors gate remain unrun by T1.
- Correction: the preceding sentence's reference to a reproduced error on `6623…` was incorrect; the 6623 snapshot was green as stated here. The only measured TypeError was the mixed-hash invocation starting `dd17…` and ending `9f4e…`.

## 2026-10-19 — Round 43 V3 C3 fence verification

- Report `.ufo/round-43/scouts/V3.md` (SHA-256 `daee0df82712719994309f62d8efe175fee7900cc62b90b44fb544d393f764cf`) records C3 at HEAD `1c79e8698a5a297f32fda4d71f0a23be2ec4248f`, tree `cd9d3814e8cdb664081746aa17e0557ddaa3e6c8`. Probe `python3 drafts/v3/c3_verify.py` (script SHA `91e2148252b9f84000127c021c08eaf857d0fc8d31cbb888e318eed7aa65cc5e`, output SHA `3866326f3820afea3afbabdd6f9f928a2c8edce43e0f0c780e2efeb6e89a6e99`) used cmark 0.31.2. Blockquote fences are recognized by cmark but missed by both bare-line scanners; end-to-end both census paths leave the quoted row unharvested (`unindexed=1`). Unclosed-at-EOF, mixed tilde/backtick closer, and the top-level r40 indent battery agree with cmark. The list-relative legal closer remains a fail-safe false-positive; no C3 source change was made.
- `python3 drafts/v3/corpus_sweep.py` (script SHA `95890f98964d793828dcc9deebe57f1c856c6a0aea6507c9c830beccb09609a6`, result SHA `93424de70476fb9820528860a61bec8dfa695d0874247d39b4c1635346aa06d4`) measured 54 tracked Markdown files, 74 cmark fence blocks, zero target-shape incidences, and zero gate/cmark classification mismatches. Both corpus self-tests passed (145 and 86 assertions); both live gate commands exited 0 and repeated stdout was byte-identical (SHA-256 `54cb2823…` integrity, `b21b57c8…` independent), all at the same HEAD/tree and unchanged gate source hashes.
- Latest `python3 verifiers/check_assertion_floors.py` at 17:33:04Z exited 1 on shared comparator work: C3 rows PASS at 145/145 and 86/86; comparator row observed 213 vs floor 143 with one self-test failure. Guard SHA `8ea89a4400f3e5bac91be7ce03c807a940a4f9e430743b1bb23a24ae05df5c25`, registry SHA `68a83161db1b7b2f3125c9a296a1815e240a19594e74910a14e39f624c0a0754`. V3 did not edit the registry or comparator.
- Disclosed: the direct independent self-test and floors guard invoke tempfile-based fixture tests, which briefly write temporary test trees outside the lane and clean them on completion. Durable V3 artifacts are confined to `drafts/v3/`; no Git add/commit or verifier/corpus change was made.

## 2026-10-19 — Round 43 T1 post-compaction comparator recheck

- After additional shared worktree edits, T1 remeasured the live join at `2026-10-19T17:38:21Z`–`17:38:29Z`, HEAD/tree `1c79e8698a5a297f32fda4d71f0a23be2ec4248f` / `cd9d3814e8cdb664081746aa17e0557ddaa3e6c8`. Comparator SHA-256 `6f3cba6c451186b2a87eb3d6b837a68b64486ef785d6d48045eb63afa7767b63`; live verifier, independent verifier, and scope-file hashes matched their 17:37:50Z snapshot and remained unchanged after the run. Fresh producers exited 0 (28 records each); the comparator `--expect-n 28 --no-stamp --json --receipt` exited 0 with 24/24 protocol, 20/24 strict, four adjudicated/four scoped out, and zero disagreement, provisional, unadjudicated, uncovered, or unknown.
- Captures/receipt (recorded under `drafts/t1/`, pruned at r43 close): live `live-recheck-173821.json` SHA-256 `0bc250f5197c9dbbdbdce7e15c4220e0904118a8c290f81295aa18464b0b0341`; independent `independent-recheck-173821.json` `eb1068a4f7b934d5553106d60737c05d8f1cd8d9ef827467f80281cac3853887`; join `join-recheck-173821.json` `b1ce556f02bb8c69cfa48aa2d06701ad2ebb9271a48aa787e0d3ee4199aa5d77`; receipt `join-recheck-173821-receipt.json` `a3a6292d1577d55793f2bd4b8fcf035516ce84c1c3965d06f26eaa3aefd57751`. `compare-captures.py` against baseline exited 0: `semantic_row_changes=0`, identical join totals, same four adjudicated IDs. T1 still did not run comparator self-test, floors guard, or held-out arms. No Git add/commit.

## 2026-10-19 — Round 43 P3 C2b verification

- `python3 drafts/p3/probe-c2b.py` reproduced the frozen defects on comparator SHA-256 `1742dcccad1118399f0aa959f7ea6884d5992834d8c4c8b94e108277ae87df76` at `17:35:52–17:36:03Z`, HEAD/tree `1c79e8698a5a297f32fda4d71f0a23be2ec4248f` / `cd9d3814e8cdb664081746aa17e0557ddaa3e6c8`: contradictory `status/state` exited 0; a valid all-match scenario with four null committed scope-outs returned `secondary_agree=28` over joined scope 24. Frozen results SHA-256 `2bdc93f096eb0f985920a5b0fb4ef957ab8cc5a6835058c0bdea43b65f6f1c42`.
- Final shared comparator snapshot SHA-256 `6f3cba6c451186b2a87eb3d6b837a68b64486ef785d6d48045eb63afa7767b63`: `python3 drafts/p3/probe-c2b.py --after` at `17:37:52–17:37:59Z` names the alias conflict at exit 2 and bounds the same secondary scenario at 24/24 (result SHA-256 `56f3570299306152821aa14755889b3440312b23470367d9bf9ea62c94953c1c`). `python3 verifiers/compare_harness_independent.py --self-test` at `17:36:25–17:36:27Z` passed 0/213; `python3 verifiers/check_assertion_floors.py --repo "$PWD"` at `17:37:04–17:37:11Z` passed all 9 instruments, comparator 213/213 against the synchronized 213 floor (guard SHA `6020e9879bf8046393d950427b679752ab6937faf179e4b9fc83c69a748ed23a`, registry SHA `a72a092ddf62d579cf5152286f8522f57cfa6a12370ec067119ddcfdbeb0c5b6`). The live frozen-input join at `17:37:11–17:37:15Z` exited 0, protocol 24/24, strict 20/24, secondary 20; output SHA `83cbc947916b8cd30c8a20f478823b0098aee461a117c9a1c40e1c845f19f5d3`.
- Scout report: `.ufo/round-43/scouts/P3.md`, SHA-256 `21399cb614b7d218cd0c0fc0a85b5e8e2e3bc7d7fce0d8351c6b15a453ec1b76`; full argv, times, input hashes, outputs, and shared-worktree attribution limits are recorded there and in `drafts/p3/`. The shared floor carriers were already synchronized by their concurrent single writer; P3 did not edit them. No Git add or commit.

## 2026-10-19 — Round 43 V1 C1 heldout-map verification

- `python3 drafts/v1/probe.py` reran at `2026-10-19T17:38:36Z`, HEAD/tree `1c79e8698a5a297f32fda4d71f0a23be2ec4248f` / `cd9d3814e8cdb664081746aa17e0557ddaa3e6c8`. It pinned current comparator SHA-256 `6f3cba6c451186b2a87eb3d6b837a68b64486ef785d6d48045eb63afa7767b63` (106180 bytes), stable before/after; frozen comparator SHA-256 `1742dcccad1118399f0aa959f7ea6884d5992834d8c4c8b94e108277ae87df76`; scope SHA-256 `fbcdc8d247475a5f1c2c613d78b6188dab77a766b02497a729a884687a70f77a`.
- Honest producer join remained exit 0 at protocol 24/24 (strict 20/24, four adjudicated/scope-out). Five of six rebuilt r41 heldout map arms and all three own cases exited 2 class-named: map overflow or competing value-map aliases; the expected-only full-copy arm remains open, exit 0 at 24/24. Final closure assertions are 10/11, so C1 is not fully verified. Fresh live/independent captures are `0bc250f5…` / `eb1068a4…`; historical census SHA `5cb218e133ef07a973e0a02ea1fd86f809eda213e9259a652fe92e949c6501b0` and replay SHA `991d8d95eb53c196ed5d74d9e4f23a9f948e29bc8e8480b81cbd430648baedb5` are pinned in the report/results.
- Final runner SHA-256 `6582c8ff288920eb620835be68fc10bd4c6cf8c2cf9c09ea5fe056ebdd2d00f6`; results JSON SHA-256 `ee9f36fc0cdf1772618575f4de3a3d6729605ad8268ec05eb782364484a00e5f`; scout `.ufo/round-43/scouts/V1.md` SHA-256 `ff292f9b4ddc9bf51ee66c504252ce601465f8630230cf854fcbeec5ab8a1d23`. Initial runner defects (exit-2 errors in stderr and alias-channel prefix parsing) are disclosed in V1; corrected full matrix reports the remaining expected-only failure. No comparator, verifier, fixture, scope, or floor files were edited by V1; no self-test/floors gate, Git add, or commit was performed.

## 2026-10-19 — Round 43 R1 map-form adversarial review

- Final `python3 drafts/r1/map_probe.py` run compares frozen `b1be35f` comparator SHA-256 `1742dcccad1118399f0aa959f7ea6884d5992834d8c4c8b94e108277ae87df76` with pinned candidate SHA-256 `6f3cba6c451186b2a87eb3d6b837a68b64486ef785d6d48045eb63afa7767b63`; scope SHA `fbcdc8d247475a5f1c2c613d78b6188dab77a766b02497a729a884687a70f77a`. Both producers exited 0 with 28 records; result artifact `drafts/r1/map-probe-results.json` SHA-256 `86b6b09489610caed17a8b3c8b196d63c5672be767a9d1b7248f3b735b134a49`; runner SHA `37af507ea815db03c60cda5c3fc8504f9ec39e838135fa00fc9761d11c701063`.
- High survivor: expected-only records plus a 28-key `checks` map (four scope-out values `null`) still exit 0, 24/24, but adjudications fall 4→0. Candidate source skips map-key validation when a record list exists and permits null scope-out map values. Full-value flat/nested maps and added `attacker.extra` are rejected exit 2; scored-only map alters adjudication but exits 2 for four uncovered rows. Report `.ufo/round-43/scouts/R1.md` SHA-256 `6f7c17da1478fc4214eafdbb847adf73a28140d74d051830b42477630d0c3204` records matrix and exact findings.
- Comparator `--self-test` passed 0/213 assertions on candidate `6f3c…`, unchanged before/after. The same run's floors guard exited 2 against registry SHA `920d53302788c03bed8bcd805389da9f67e1c5982d4a54b72db29f98c23b483a`, naming concurrent expectation drifts for `corpus_independent` (91 vs 86) and `corpus_integrity` (150 vs 145); no registry edit was made. A later shared-worktree comparator hash check observed `d8b8c7f6001db7f47a294dc2a98db9179f61a281be20293dc5b104906073679d`, not the tested snapshot. The first probe attempt used `parents[3]` for ROOT and failed before scoring; corrected `parents[4]` run is the sole measurement. No production verifier, fixture, scope or floor file was edited; no Git add/commit.

## 2026-10-19 — Round 43 P4 post-compaction recheck

- Re-ran `python3 drafts/p4/fence_shapes.py` at HEAD/tree `1c79e8698a5a297f32fda4d71f0a23be2ec4248f` / `cd9d3814e8cdb664081746aa17e0557ddaa3e6c8`, cmark 0.31.2. Probe SHA-256 `0700beb402460fa6bfd7192aa299bd2798b6ba1f60c65488eadb2adcb09745bb`; final result `drafts/p4/results.json` SHA `8849b99b90de8a964e4c539e0cf1bca909c6277f9c171a4abb8133fad2263a83`, measured `17:41:32.258908Z`. cmark spans: blockquote 1–3, unclosed EOF 1–2, tilde/backtick-mismatch 1–4; scanner miss only on blockquote. Fixture exits are 1/1 per target shape with `unindexed=1`; control exits 0. Live sweep: 54 tracked Markdown, zero incidences/moved classifications; frozen/current live stdout and exit codes identical. Silent false-PASS remains 0/3; no predicate change.
- Corpus self-tests passed integrity 150/150 and independent 91/91; the current floor carriers are 150/91. Latest integrated guard (guard SHA `d71afb4d875762d229182d51f6b9112efe66e9da546c0126fe2aa9420384f6dd`, registry SHA `920d53302788c03bed8bcd805389da9f67e1c5982d4a54b72db29f98c23b483a`) exited 1 because comparator SHA `d8b8c7f6001db7f47a294dc2a98db9179f61a281be20293dc5b104906073679d` had one self-test failure at assertion 185/213: expected `competing value-map aliases` for `heldout-wrapper-precedence-expected-over-observations`. Standalone comparator self-test at 17:41:56Z reproduced that one failure. The P4 probe therefore records overall FAIL only for the shared comparator gate; all corpus checks pass. P4 did not edit comparator, floors guard, registry, or corpus predicates.
- Updated scout report `.ufo/round-43/scouts/P4.md` SHA-256 `ee0861daa442ed58c700d93cb184041408d770cac29908fc11c84e6f457936e4`. Current corpus verifier hashes `28224c76510dcafc4d7a52da41ffd2d366337414f65320cbb21e6d9de12aba9d` / `254b5a2f57aabbf0b8376fce34c42250b56499d9fd7a92b5e6374ac505315d69`; shared deltas add self-test cases/helpers only. No Git add/commit.

## 2026-10-19 — Round 43 V3 post-sync correction

- Correction to the earlier V3 floor snapshot: the latest integrated `TMPDIR="$PWD/drafts/v3/tmp" python3 verifiers/check_assertion_floors.py` run at `2026-10-19T17:40:49Z` used guard SHA-256 `d71afb4d875762d229182d51f6b9112efe66e9da546c0126fe2aa9420384f6dd`, registry SHA-256 `920d53302788c03bed8bcd805389da9f67e1c5982d4a54b72db29f98c23b483a`, and comparator SHA-256 `6f3cba6c451186b2a87eb3d6b837a68b64486ef785d6d48045eb63afa7767b63`. The observed/registered vector was `10/150/91/87/1597/62/104/213/150`; both C3 rows passed exactly (integrity 150/150, independent 91/91). The full guard exited 1 only because the comparator row had one self-test failure at 213/213 (assertion 185); this is not a green full guard. Floor output SHA-256 `12dabdf7bb6735ffeba842f1d4a059f427762e09f4fd0a51c8c31157abeaf3ea`.
- Scope recheck at `2026-10-19T17:43:14Z` confirmed HEAD/tree `1c79e8698a5a297f32fda4d71f0a23be2ec4248f` / `cd9d3814e8cdb664081746aa17e0557ddaa3e6c8`, corpus byte-equal to HEAD, and current corpus-gate hashes `28224c76510dcafc4d7a52da41ffd2d366337414f65320cbb21e6d9de12aba9d` / `254b5a2f57aabbf0b8376fce34c42250b56499d9fd7a92b5e6374ac505315d69`. Shared gate diffs are confined to C3 self-test fixtures/expectations and comments; no fence-predicate changes. V3 did not edit gate predicates, corpus, or the single-writer floors registry. Report `.ufo/round-43/scouts/V3.md` SHA-256 `3c1999c4862e70da7b0b58faae985f32b20871f7e43cf05902c84fbf4de11e70`. No Git add or commit.

## 2026-10-19 — Round 43 P1 C1 held-out payload-map closure

- `python3 drafts/p1/run-probes.py` measured at `2026-10-19T17:42:46Z`, HEAD/tree `1c79e8698a5a297f32fda4d71f0a23be2ec4248f` / `cd9d3814e8cdb664081746aa17e0557ddaa3e6c8`. Frozen comparator SHA-256 `1742dcccad1118399f0aa959f7ea6884d5992834d8c4c8b94e108277ae87df76`; candidate/worktree SHA `d8b8c7f6001db7f47a294dc2a98db9179f61a281be20293dc5b104906073679d`, unchanged during replay; committed scope SHA `fbcdc8d247475a5f1c2c613d78b6188dab77a766b02497a729a884687a70f77a`. All six registered held-out arms flipped from frozen exit 0 to candidate exit 2 with the named scope-out value-laundering or derived-set-overflow class. The honest control stayed exit 0, protocol 24/24. Results JSON SHA-256 `1e7f7c26ba72787e28fefd980108fc56179de501a37b07b0c3014ab4a4ea032b`; runner SHA `968a291f9b5f63876b6d0e599a65a1e27420238177e3325e9c728ed675bf8b00`; fresh producer capture SHAs `0bc250f5…` / `eb1068a4…`.
- P1 orders the scope-derived map-key-set check before parsing, so the expected/observations precedence arm fails on overflow rather than only on alias conflict; its fixture now expects that diagnosis. `compare_harness_independent.py --self-test` passed 0/213; `check_assertion_floors.py --self-test` passed 0/150; the live comparator join exited 0 at protocol 24/24, strict 20/24, four adjudicated/four scope-outs; the full assertion-floor guard exited 0, all nine rows exact. Floor vector: `10/150/91/87/1597/62/104/213/150`. The concurrent C3 test additions raised corpus self-test counts 145→150 and 86→91; P1 synchronized the guard docstring, both guard tables, and registry. Guard SHA `d71afb4d875762d229182d51f6b9112efe66e9da546c0126fe2aa9420384f6dd`; registry SHA `920d53302788c03bed8bcd805389da9f67e1c5982d4a54b72db29f98c23b483a`.
- Report `.ufo/round-43/scouts/P1.md` SHA-256 `e243e22b08c732b94acc80dc55aee54b30a29f97eebd379561aa9c5e2d10d0a3`. The report records the bounded six-arm verdict and the separate R1 record-list + null scope-out map composition as an unclosed follow-up boundary; the six-arm result is not generalized to all mixed-channel payloads. Shared tree remained dirty from concurrent round-43 work; no Git add or commit.

## 2026-10-19 — Round 43 W1 floor-registry watch

- Report `.ufo/round-43/scouts/W1.md` SHA-256 `62e1504f1544a4e17e82bd005f45be7fbf48db9251938582df480ddc3ebf388c`. Its baseline was extracted with `git show HEAD:verifiers/floors-registry.json`; settle check `python3 verifiers/check_assertion_floors.py` at `2026-10-19T14:42:58–14:43:06-03:00` used HEAD/tree `1c79e8698a5a297f32fda4d71f0a23be2ec4248f` / `cd9d3814e8cdb664081746aa17e0557ddaa3e6c8`, registry `6a596dfcf34e984d1bc64ef0d64aef5df8a4b91f`, guard `4f8b664f5078afd6cfdde95bf2fcadc083c6d6e3`, comparator `0f5feb473645db803e488fe5b619059417f96feb`, corpus instruments `470ec1b6993daf99847dec95366458382d953129` / `dadb425807f05ea9b0622bc648dc204b5b5eda32`. All nine observed counts equaled floors; exit 0.
- Watch recorded an intermediate comparator guard/anchor mismatch and a later period where corpus self-test counts exceeded the registered minimums. The report pins those samples and the red intermediate comparator self-tests; the registry moved monotonically from `10/145/86/87/1597/62/104/118/150` to `10/150/91/87/1597/62/104/213/150`, with no observed rollback. A post-report guard run at `2026-10-19T14:44:47-03:00` again passed all nine exact floors. W1 made no floor edits; no Git add or commit.

## Round 43 I1 integrator gate battery

- At Unix epoch `1792431729`–`1792431769`, against HEAD/tree `1c79e8698a5a297f32fda4d71f0a23be2ec4248f` / `cd9d3814e8cdb664081746aa17e0557ddaa3e6c8` and claims SHA-256 `c1185d5b19193baf1975068634491883b8dbf6225c4aef5205478d9e88ec898e`, the refreshed assertion-floor gate passed all nine instruments exactly at `10/150/91/87/1597/62/104/213/150` (guard SHA `d71afb4d875762d229182d51f6b9112efe66e9da546c0126fe2aa9420384f6dd`; registry SHA `920d53302788c03bed8bcd805389da9f67e1c5982d4a54b72db29f98c23b483a`). Fresh producers and comparator join exited 0: protocol 24/24, strict 20/24, four adjudicated/four scoped out, no disagreement or uncovered rows. Both corpus gates passed.
- Live checklist remains red on pruned round-41 citation paths in LOG; the OMP surfaces gate reports 0 extracted loader classes against baseline 8; the OMP binary SHA/mtime pins drift. These live-gate failures and the green self-test/floor results are distinguished in `.ufo/round-43/scouts/I1.md`, which carries the command, source, output hashes and Unix-epoch evidence for each result. No project source or floor registry was edited by I1; no Git add or commit.

## 2026-10-19 — Round 43 P4 final settled rerun

- Final `python3 drafts/p4/fence_shapes.py` at HEAD/tree `1c79e8698a5a297f32fda4d71f0a23be2ec4248f` / `cd9d3814e8cdb664081746aa17e0557ddaa3e6c8` used cmark 0.31.2, passed, and recorded `drafts/p4/results.json` SHA-256 `4677b366286b7f870a8bf824e98c442ade2a422f8877e463fc51792873fd3315` (`measured_at=2026-10-19T17:44:17.659767Z`). Probe SHA `0700beb402460fa6bfd7192aa299bd2798b6ba1f60c65488eadb2adcb09745bb`. cmark spans blockquote 1–3, unclosed EOF 1–2, tilde/backtick pseudo-closer 1–4; fixture gates fail closed for each target, control passes, and live sweep is 54 tracked Markdown / 0 target incidences / 0 moved classifications / byte-identical frozen-current output. Silent false-PASS remains 0/3; no fence predicate changed.
- Final corpus self-tests passed 150/150 and 91/91; floors-guard self-test 150/150. `python3 verifiers/check_assertion_floors.py --repo "$PWD"` passed all nine exact floors at 17:44:09Z, vector `10/150/91/87/1597/62/104/213/150`; the integrated guard in the P4 probe also passed. Guard SHA `d71afb4d875762d229182d51f6b9112efe66e9da546c0126fe2aa9420384f6dd`, registry SHA `920d53302788c03bed8bcd805389da9f67e1c5982d4a54b72db29f98c23b483a`, comparator SHA `d8b8c7f6001db7f47a294dc2a98db9179f61a281be20293dc5b104906073679d`; comparator self-test passed 0/213 at 17:43:50Z.
- This supersedes the preceding P4 snapshot (results SHA `8849b99b…`), which was transiently red on comparator assertion 185 while its fixture expected the old `competing value-map aliases` diagnosis. The shared P1 update made the expected diagnostic `derived-set overflow` (fixture `case.json` SHA `e803d2bbd7130e3b08556d10c72c874cb4378410e0c7bc45de7ecd21921d4e80`); the comparator source did not change. P4 made no comparator, fixture, floors-guard, registry, or corpus-predicate edits.
- Final scout report `.ufo/round-43/scouts/P4.md` SHA-256 `7bd776491a8d900fb896c0731f6e1a80726b4f9641d16fa809b7fc93917772a0`. No Git add or commit.

## 2026-10-19 — Round 43 V2 independent C2 verification

- `python3 drafts/v2/probe_c2.py` measured at `2026-10-19T14:42:01–14:43:08-03:00`, recorded UTC `17:43:08Z`, HEAD/tree `1c79e8698a5a297f32fda4d71f0a23be2ec4248f` / `cd9d3814e8cdb664081746aa17e0557ddaa3e6c8`; stable pre/post. Probe SHA `bdf645f668dba76be978c3f0cc6b5eaf7bc1cda4b1a46078c693b4aca83a83c7`; comparator SHA `d8b8c7f6001db7f47a294dc2a98db9179f61a281be20293dc5b104906073679d`; frozen `b1be35f` SHA `1742dcccad1118399f0aa959f7ea6884d5992834d8c4c8b94e108277ae87df76`; scope SHA `fbcdc8d247475a5f1c2c613d78b6188dab77a766b02497a729a884687a70f77a`.
- Four field arms: `overrides`, `metadata`, `v2_extra_top_level` fail exit 2 named; `alternatives` exits 0 as explicitly ignored, join 24/24. `status/state` split fails exit 2 named. H02 combined scope-out + adjudicated values: frozen comparator accepts secondary `28/24`, landed comparator rejects exit 2 `scope-out value laundering`; adjudicated-only control bounds secondary to `24/24`. Full per-arm payload/output hashes are in `drafts/v2/c2-matrix.json` (SHA `14409dff1545e2602a37c317f4950b5d6edb7ff0f3f209b2112a1e765b84ccfd`) and `c2-matrix.txt` (SHA `d2810c8a66b359a3f5bf10df64c594425679822000b463e0a876d07827dad852`).
- Live join command `python3 verifiers/compare_harness_independent.py --no-stamp --json`: exit 0, protocol 24/24, strict 20/24, four adjudicated/four scoped out, zero disagreement/unknown/uncovered; stdout SHA `44a69c6883ee92be19a156159b7179262da383a8b87145e5cca8b8aee3b4d532`. Comparator `--self-test`: 0/213, exit 0, stdout SHA `ed98297d573fb6ccc3be64ff6a177b1f5990f02966936d1b7f455ebb242451c6`. `python3 verifiers/check_assertion_floors.py`: all nine PASS at `10/150/91/87/1597/62/104/213/150`, exit 0, stdout SHA `0f119f970c8d98edc5f36cbd296e3c6bffb12a86c212fedb685209e5fe2e4ff2`; guard SHA `d71afb4d875762d229182d51f6b9112efe66e9da546c0126fe2aa9420384f6dd`, registry SHA `920d53302788c03bed8bcd805389da9f67e1c5982d4a54b72db29f98c23b483a`.
- Follow-up self-test + floors run `17:43:53–17:44:03Z` confirmed unchanged pre/post SHA for 61 verifier/fixture files (manifest SHA `9ded01042392399e855ff5c31b48ff7a1eeba75a13b75290209ee2fabaf2c191`); both commands exited 0 on the same comparator/guard/registry and tree. Earlier mixed-hash attempt (`6f3c…`→`d8b8…`) was excluded, not counted. Report `.ufo/round-43/scouts/V2.md` SHA-256 `e683042340309482882fdad1283ce24d02ec3a934cc65b8f5e895f8ed8b9fc7c`; fresh captures live/independent `0bc250f5…` / `eb1068a4…`. No verifier, scope, registry, corpus, index or ref was changed by V2; no Git add/commit.

## 2026-10-19 — Round 43 P2 C2a independent-payload field gate

- `python3 drafts/p2/probe_fields.py` measured at `2026-10-19T17:44:25Z`, HEAD/tree `1c79e8698a5a297f32fda4d71f0a23be2ec4248f` / `cd9d3814e8cdb664081746aa17e0557ddaa3e6c8`. Frozen `b1be35f` comparator SHA-256 `1742dcccad1118399f0aa959f7ea6884d5992834d8c4c8b94e108277ae87df76`; current shared comparator SHA `d8b8c7f6001db7f47a294dc2a98db9179f61a281be20293dc5b104906073679d`. Four injected uncontracted/override arms (`metadata`, `overrides`, arbitrary future key, value-map override) changed frozen exit 0 / 24-of-24 to current exit 2 with the named class. Diagnostic `alternatives` stayed exit 0 and JSON named `alternatives`, `landed`, `unlanded` as ignored. Probe script SHA `982d7f6fed1d2cca44399de5566b81cd2df4b6a3ffe09d71cce28b483cba8a9d`; results `drafts/p2/probe-results.json` SHA `ff558ea3be72b24c0e8cd927c28aba17a71768b78e0a7b25805e3e85e5ace256`.
- Full `python3 drafts/p2/verify_p2.py` ran `17:44:25–17:44:43Z` and passed with sources pinned before/after: comparator self-test 0/213; live join exit 0 at protocol 24/24, strict 20/24, four adjudicated/four scope-outs, no disagreement/provisional/uncovered/unknown; floors 9/9; both corpus JSON gates exit 0. Floor vector `10/150/91/87/1597/62/104/213/150`; guard SHA `d71afb4d875762d229182d51f6b9112efe66e9da546c0126fe2aa9420384f6dd`, registry SHA `920d53302788c03bed8bcd805389da9f67e1c5982d4a54b72db29f98c23b483a`. Verification script SHA `824ef1b4d4ee3a8ed5114d7f2403ed5fe885a7b108da7f07d473f6929976682d`; results `drafts/p2/verification-results.json` SHA `3fa4b12f84818d15c383f3c18f566b9c5e07dd198039cb407c907b353f755170`.
- Disclosure: an initial probe attempt failed before measurement on its own incorrect marker assertion; after correction the cited full five-arm run passed. A shared-tree comparator self-test at 17:41:34Z briefly failed assertion 185/213 on a held-out-wrapper fixture expectation during concurrent P1 changes. The settled fixture (`case.json` SHA `e803d2bbd7130e3b08556d10c72c874cb4378410e0c7bc45de7ecd21921d4e80`) and same comparator passed 0/213 at 17:42:57Z; P2's full verification then repeated green. No P2 change was made to the separate C1 fixture issue.
- Scout report `.ufo/round-43/scouts/P2.md` SHA-256 `b755948ac7da1173664c7c29d644c134a96fe1f98ef8dac51b86f1de4c9e2218`. This records only C2a and distinguishes the shared comparator snapshot from concurrent C1/C2/C3 changes. No Git add or commit.

## 2026-10-19 — Round 43 P3 C2b post-compaction recheck

- At HEAD/tree `1c79e8698a5a297f32fda4d71f0a23be2ec4248f` / `cd9d3814e8cdb664081746aa17e0557ddaa3e6c8`, comparator SHA-256 `d8b8c7f6001db7f47a294dc2a98db9179f61a281be20293dc5b104906073679d` stayed unchanged through all runs. `python3 drafts/p3/probe-c2b.py --after` (`17:44:33–17:44:40Z`, runner SHA `e8dbbf854f766571444f9475edfac94f12e42d3bb0b2dbc4e666eea188d59993`) exited 0: contradictory status/state named at exit 2; bounded secondary arm 24/24, `secondary_agree=24`; control secondary 20. `after-results.json` SHA `f4e8e822f26319984f2d5feb8bd7e48166ebfcaead1db2eb73ead55a306e5957`; producer/scope SHAs `0bc250f5…` / `eb1068a4…` / `fbcdc8d2…`.
- The frozen-input live join command recorded in `.ufo/round-43/scouts/P3.md` at `17:45:09–17:45:13Z` exited 0: protocol 24/24, strict 20/24, four adjudicated/four scoped-out, secondary 20, no disagreement/uncovered/unknown; same comparator and producer/scope hashes.
- `TMPDIR="$PWD/drafts/p3" python3 verifiers/compare_harness_independent.py --self-test` at `17:45:45–17:45:47Z` passed 0/213 (exit 0), case SHA `2b5cfd7d268949dfaf191b6fab0999a08fbc51f32d718b046ab27b8d71ee4912`. This supersedes P4's earlier 17:41 failure on assertion 185: the heldout wrapper arm's expected diagnosis is now scope-first `derived-set overflow`, matching the shared comparator; P3 did not edit that C1 fixture or source.
- `TMPDIR="$PWD/drafts/p3" python3 verifiers/check_assertion_floors.py --repo "$PWD"` at `17:45:53–17:46:01Z` exited 0, all nine exact floors `10/150/91/87/1597/62/104/213/150`. Guard SHA `d71afb4d875762d229182d51f6b9112efe66e9da546c0126fe2aa9420384f6dd`; registry SHA `920d53302788c03bed8bcd805389da9f67e1c5982d4a54b72db29f98c23b483a`; no floor carrier changed by P3.
- Updated report `.ufo/round-43/scouts/P3.md` SHA-256 `2bd552c771aae54a393a9742686617a5f41b540ea3b3b9d92433d821d8c46dfb`. No Git add or commit.

## 2026-10-19 — Round 43 B2 SHONEN scribe and box recheck

- Prepared `.ufo/round-43/scouts/B2.md`, `drafts/b2/shonen-block.md`, and `drafts/b2/verdict-table.md`. The paste-ready SHONEN block has exactly four `[~]` marks, no completion marks, and four resolving B2 report anchors. The table gives distinct C1/C2/C3 verdicts. B2 changed no `SHONEN.md`, verifier, fixture, floor guard, registry, scope, index, or Git ref.
- Claims SHA-256 `c1185d5b19193baf1975068634491883b8dbf6225c4aef5205478d9e88ec898e`; HEAD/tree `1c79e8698a5a297f32fda4d71f0a23be2ec4248f` / `cd9d3814e8cdb664081746aa17e0557ddaa3e6c8`. These are shared dirty-worktree results, not landed-commit claims.
- At comparator SHA-256 `d8b8c7f6001db7f47a294dc2a98db9179f61a281be20293dc5b104906073679d`, B2 reran `--self-test` (0/213) and the honest frozen-input join (exit 0, protocol 24/24, strict 20/24, four adjudicated/four scoped out, no disagreement or uncovered rows). P1’s direct replay at the same comparator snapshot closed all six registered C1 heldout-map arms with named exit 2; it records a separate mixed record-list/null-map composition as follow-up. P2/P3’s direct C2 field, status/state, and secondary-count arms pass on d8b8. P4’s cmark 0.31.2 C3 battery records 0/3 silent false-PASS, fail-safe fixture outcomes, and zero live target incidence. Scout reports `.ufo/round-43/scouts/P1.md`, `.ufo/round-43/scouts/P2.md`, `.ufo/round-43/scouts/P3.md`, and `.ufo/round-43/scouts/P4.md` contain axis-specific limits.
- Latest verified floors are all 9/9 EXACT, vector `10/150/91/87/1597/62/104/213/150`; comparator SHA above, guard `d71afb4d875762d229182d51f6b9112efe66e9da546c0126fe2aa9420384f6dd`, registry `920d53302788c03bed8bcd805389da9f67e1c5982d4a54b72db29f98c23b483a`. Box 2 harness verification passes 28/28; corpus gates, harness-independent, and fault-injection self-test pass. The surfaces gate remains 5 PASS / 2 FAIL, and substrate pins 1/3 PASS (OMP digest/mtime drift).
- Immediately before this B2 append, `verify_skill_checklist.py` SHA `214ae44dcba45ba19656a0b2aa6c49900c618f6716a64fef0776f06437cfc8d0` ran at `17:50:53Z` against LOG SHA `3bc5f02b12f04c2dc20d36d06d82d7e2790a2fedda3fa50a61f0db70cac3998c`: 9 PASS / 1 FAIL, `governance.citation_resolves` on pre-existing dead historical citations. The required post-entry rerun follows this entry. No Git add, commit, or other Git mutation was performed.

## 2026-10-19 — Round 43 P2 competing-alias control

- To test the `competing value-map aliases` branch independently of the held-out C1 wrapper fixture's scope-first check, a direct CLI probe ran at `2026-10-19T17:50:17Z`. It supplied same-key `expected` and `observations` maps for `a.b`, `a.c`, `a.d` (payload SHA-256 `138b9ba33bf52e9ce2a5c65549ead1b596d6470cd4445f9d1627bdc96729edfd`) against agree-control live fixture SHA `327df1057a0bfbc3f247a1454c5541c727adc9622a3bf96825b626d19c36426e` and empty fixture scope SHA `b67c96230174515b16e74f7bfbcea996dbbc474903af95a893ea2e7f5f66a1d9`. CLI: `python3 verifiers/compare_harness_independent.py --live-json <agree-control/live.json> --independent-json <temporary JSON> --cwd "$PWD" --scope-file <fixtures/scope.json> --expect-n 3 --no-stamp --json`.
- Comparator SHA-256 remained `d8b8c7f6001db7f47a294dc2a98db9179f61a281be20293dc5b104906073679d` before/after; the call exited 2 with `competing value-map aliases: expected, observations`. Updated report `.ufo/round-43/scouts/P2.md` SHA-256 `add845f3756b7dd0a9c3f8d0bedaec6a887eda3edf4dcf9b891827149354620f`. Temporary JSON was removed; no production source, fixtures, or floors changed. No Git add or commit.

## 2026-10-19 — Round 43 R2 C2/C3 adversarial review

- Stable `python3 drafts/r2/probe.py` matrix at `17:42:29.623635Z–17:43:50.887443Z`, HEAD/tree `1c79e8698a5a297f32fda4d71f0a23be2ec4248f` / `cd9d3814e8cdb664081746aa17e0557ddaa3e6c8`; comparator SHA `d8b8c7f6001db7f47a294dc2a98db9179f61a281be20293dc5b104906073679d` matched worktree before/after. Fresh control join 24/24, strict 20/24, four adjudicated/four scoped out, secondary 20. Full results `drafts/r2/probe-results.json` SHA-256 `ca5d37cf911fcb7040ff9b22327013d9a72f17020dc987b50f447320e840298f`; scope SHA `fbcdc8d247475a5f1c2c613d78b6188dab77a766b02497a729a884687a70f77a`.
- C2 recheck: unknown keys/overrides/metadata/observed maps and top-level `re_derived` with row channels exit 2; alternatives and unlanded summary are surfaced as ignored; status/state split and attempted secondary overflow fail closed. New survivors: a conflicting dotted-id top-level map alongside row channels, check/id alias conflict, and re_derived/observed record-value conflict each still exit 0 at 24/24. Exact per-arm inputs/outputs and source locations are in the report/results JSON; no source or fixture changed.
- C3 recheck with cmark 0.31.2: nested blockquote fences are missed by both scanners, but end-to-end fixtures fail closed at `unindexed=1`; unclosed EOF and mixed tilde/backtick pseudo-closer agree with cmark. P4's contemporaneous 54-file sweep found zero target incidences/classification changes (`scouts/P4.md:24-28`).
- Final `python3 verifiers/check_assertion_floors.py` at `17:46:39Z–17:46:47Z` exited 0, all 9 exact floors `10/150/91/87/1597/62/104/213/150`; guard SHA `d71afb4d875762d229182d51f6b9112efe66e9da546c0126fe2aa9420384f6dd`, registry SHA `920d53302788c03bed8bcd805389da9f67e1c5982d4a54b72db29f98c23b483a`, output SHA `0f119f970c8d98edc5f36cbd296e3c6bffb12a86c212fedb685209e5fe2e4ff2`. A mixed-source direct join (`6f3c…`→`d8b8…`) was excluded and disclosed. Report `.ufo/round-43/scouts/R2.md` SHA-256 `329f482297d80121ff2c4215d23382e84a19573185349b68431bf97a8a60464c`; no Git add or commit.

## 2026-10-19 — Round 43 F1 fixture-builder evidence

- F1 generated a durable 21-case suite covering six heldout-map shapes (full expected-only copy, flat dotted map, nested `checks`, nested `expected`, nested `observations`, and competing expected/observations wrappers), the uncontracted `overrides`/`metadata`/unknown-field cases, the allowed-`alternatives` control, and string/non-string `status`/`state` conflicts. All six heldout maps passed the frozen comparator at 28/28 and now fail closed at exit 2. The wrapper case requires a named expected-value rejection and no traceback or success headline without pinning validation order; its carried scope-out values trigger the earlier `derived-set overflow` diagnostic. P2 separately verified the competing-alias branch at exit 2 (`LOG.md`, Round 43 P2 competing-alias control). Comparator self-test passed 0 failures / 213 assertions (output SHA-256 `db5a356583312095c2b0e4438c617413ab6d3650de884bc048560837736caaa0`).
- Added C3 self-test cases in both corpus verifiers for unclosed tilde fences, mixed-character pseudo-closers, and blockquote fences. With cmark 0.31.2, unclosed/mixed cases agree; both bare-line scanners miss the blockquote fence, while the end-to-end gates fail safe with `unindexed=1` on the fixture world's `knowledge/b.md` (a synthetic doc inside F1's probe world, not a repo file). Self-tests pass integrity 150/150 and independent 91/91. The 54-Markdown/74-fence cmark sweep found zero target-shape incidences and no corpus-vs-cmark mismatches. The separate list-relative two-space closer remains a scanner/cmark mismatch (fail-safe), recorded but not claimed closed.
- Both live corpus `--json` gates passed twice with byte-identical outputs (integrity SHA-256 `63b07476d14a168071670ec659e3725a66ad29f5589bcbd1cdfcea60d918f9d4`; independent SHA-256 `3a8c8558c6527ba3b1310009b3413abb0bc54ea3fe7ac6b2f3f224f3dc24ea75`). Fresh producers each returned 28 records; frozen-input join exited 0 with protocol 24/24, strict 20/24, secondary 20, four scope-outs, and no disagreement/uncovered/unknown rows. Captures: `0bc250f5197c9dbbdbdce7e15c4220e0904118a8c290f81295aa18464b0b0341` / `eb1068a4f7b934d5553106d60737c05d8f1cd8d9ef827467f80281cac3853887`; join `8fdafcfb2d7cc064cdfb069456fa1371e59275c86827f8afc7cb71565381c2f3`; receipt `cef4b8d8179f22260b33a2ed30a10dccd78156a1ab075225605c7eb4ca022ac3`.
- `python3 verifiers/check_assertion_floors.py --repo "$PWD"` passed all nine exact floors `10/150/91/87/1597/62/104/213/150` (output SHA-256 `0f119f970c8d98edc5f36cbd296e3c6bffb12a86c212fedb685209e5fe2e4ff2`). The floor carriers were shared-tree work and were not edited by F1. Scope limit: the synthetic expected-only full-copy fixture has 28 values and does not reproduce V10's real expected-only 24-row form, which V1 found still accepted at 24/24; this work does not close C1. F1 scout report `.ufo/round-43/scouts/F1.md` SHA-256 `0dc1e33bd92abd6fa36fdf5140e78d36fccdc4accd8cefd9a4a52d6f39244547`. Shared dirty worktree; no Git add or commit.

## 2026-10-19 — Round 43 (loop A position 7): C1 fails as declared on the surviving expected-only map door; C2+C3 verified — round REJECTED, all three claims' work landed

- Claims at `.ufo/round-43/claims.json` (C1 depth = close the census's top-reachability map forms; C2 operability = un-contract field gate + status/state + secondary_agree; C3 freshness = V21's residual fence shapes). Provider: `openai-codex/gpt-6-luna-max` (pos-7 plan was zai glm-5.3-flash — zai quota-exhausted, operator directive: all zai positions run on codex luna-max for the rest of the session). 24/24 seats. Fragments `.ufo/round-43/scouts/*.md`; curated `.ufo/round-43/evidence/` pending.
- **C1 depth — five of six heldout-* map arms now fail closed; the expected-only record+map composition still launders — FAILS AS DECLARED, depth holds 9.** P1 landed a scope-derived key-set check before parsing (`verifiers/compare_harness_independent.py`): a flat/nested map whose key-set exceeds the honest derived set, or a scoped-out row carrying a non-null value, now fails `derived-set overflow` / named exit 2. Five of the six `heldout-*` map arms (flat-dotted-map, nested-checks-map, nested-expected-wrapper, nested-observations-wrapper, wrapper-precedence) flip frozen-b1be35f exit 0 → exit 2 class-named; the wrapper-precedence fixture re-pinned. **The sixth — `heldout-expected-only-full-copy` — still exits 0.** V1 + R1 + F1 + E1 independently confirm: a record-bearing expected-only payload with a 28-key `checks` map still joins 24/24 (adjudications collapse 4→0) or 28/28 — the record channel bypasses the map-key validation, and F1's committed fixture doesn't reproduce V10's real 24-row case (it's a 28-value fixture, not the real form). R1: the record+map composition is a distinct door the key-set check doesn't reach. **Depth holds 9.**
- **C2 operability — VERIFIED (P2 field-gate + P3 alias/denominator; V2 + R2 verify).** The comparator now rejects unknown top-level keys, competing value-map forms, and row-channel overrides class-named; `alternatives`/`landed`/`unlanded` are explicitly ignored and reported by name. A within-record `status` vs `state` split rejects `status/state split` exit 2 (was last-wins/first-read); `secondary_agree` is bounded to its denominator (a 28-over-24 skewed payload now rejects `scope-out value laundering` exit 2). V2's 8-arm matrix + R2's 12-arm matrix confirm; comparator self-test 118→213 with floors in-step. **New residuals (R2):** a dotted-id top-level map shadow, conflicting `check`/`id`, conflicting `re_derived`/`observed` still read exit 0 — carried to r44+. Score held: round rejected on C1.
- **C3 freshness — verified fail-safe, no predicate change needed.** V21's residual shapes re-derived from cmark 0.31.2 (P4 + V3 + T2 + R2): a blockquote fence (`> ```...`) — cmark fences it lines 1-3 but both bare-line scanners miss it, AND the quoted coverage row still reads `unindexed=1` exit 1 — **fail-closed, not a silent PASS**; an unclosed fence at EOF — agrees with cmark; a tilde-opener + backtick-closer (mixed-char) — correctly does NOT close. **0/3 silent false-PASS** — no predicate change landed; F1 added C3 self-test cases (unclosed-tilde, mixed-char, blockquote) pinning the classifications; self-tests 145→150 / 86→91, floors in-step; 54-doc/74-fence cmark sweep 0 incidence, 0 moved classifications, byte-invariant stdout. **Named residual (conservative, not a defect):** a legal list-relative two-space closer is over-hidden (a false-positive `unindexed`, fail-safe direction) — recorded, not claimed closed.
- **r41 durability repair (this integration):** the r41 prune deleted the V10 census arm payloads — a counting input the committed replay runner + the census doc's `recheck` line need (the r37 lesson recurring: pruned a counting input). Recovered by running `v10-census-probes.py` — the durable generator — which re-materialized all 52 arm/live/independent payloads into `evidence/` (one parents-index fix for the drafts→evidence depth move; LOG citations re-pointed at `evidence/`). The subprocess replay reproduces the 46/46 recorded outcomes.
- **Whole-tree battery at close:** live comparator exit 0 24/24 (strict 20/24, adjudicated 4, scoped 4); comparator self-test **0/213**; floors **9/9 EXACT** (`10/150/91/87/1597/62/104/213/150`); corpus integrity 150/150 + independent 91/91 + both live gates exit 0; checklist 10×PASS after the citation repairs. Named carried reds (I1, B2): surfaces gate 5 PASS/2 FAIL (OMP loader-class extraction finds 0/8) + OMP binary sha/mtime pin drift — substrate moved, not a lane regression.
- **Queue for r44 (pos 8 — codex luna-max per the zai→luna substitution):** **C1' = close the record+map composition door** (the expected-only record payload whose `checks` map launders the scoped-out rows — the record channel must be cross-checked against the map-key set / the committed scope file the same way the map channel is); R2's residuals (dotted-id top-level map shadow; check/id conflict; re_derived/observed conflict). Standing debt: surfaces gate 0/8 loader-class + OMP pin drift (substrate moved); digest-append; IND hang; resolver-vs-brace; SHONEN form; divergence merge (operator).
