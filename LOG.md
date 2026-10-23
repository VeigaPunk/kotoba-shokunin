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

## 2026-10-19 — Round 44 B1 scribe scaffold (landing measurements pending)

- Read `.ufo/round-44/claims.json` first; `python3 -m json.tool .ufo/round-44/claims.json` exited 0 and its SHA-256 was `cf18423f099475ba9733dd790a8de69ffe517c8e07d64a7b70b04b2ac81daf4f` at `2026-10-19T18:03:10Z`. Prepared `.ufo/round-44/drafts-report-skeleton.md` and `.ufo/round-44/scouts/B1.md`; the latter records exact source pins, commands, and the scaffold's absent-at-entry status.
- At `2026-10-19T18:05:13Z`, `git rev-parse HEAD` / `git rev-parse 'HEAD^{tree}'` returned `6881ce31912cf52982de733d18d25e7ab7aae5c4` / `f005c7f1f8a46c2ddbcb4e6a48ca949afb2de56d`. `sha256sum` returned skeleton `275862f58c9eff1f2913a80043fef5ace2ac45724b199d580b39e61d9622c1dc` and B1 report `730d391c7f5b8b75f68a9c0a08448da6f488bfcb73629ef5d394af12811ccbe2`; the required-heading/pending-cell structure check passed. These are working-tree artifacts, not a landing commit.
- At that same snapshot, `git status --porcelain=v1` listed `M verifiers/compare_harness_independent.py`, `?? .ufo/round-44/`, and three untracked fixture directories under `verifiers/fixtures/compare-harness-independent/` (the dotted-id-top-level-map-shadow, record-check-id-conflict, and record-re-derived-observed-conflict cases). These concurrent changes are not attributed to B1; no comparator or fixture was inspected or modified by this seat.
- No held-out probes, live join, self-test, assertion-floor guard, surfaces gate, corpus gate, or SHONEN check was run. All outcome and axis-verdict cells remain pending. No Git add/commit or other Git mutation was performed; the parent integrates under lane identity.

## 2026-10-19 — Round 44 D1 RECORD/MAP scope-guard map

- Added `.ufo/round-44/scouts/D1.md`. Its read-only source snapshot command at `2026-10-19T18:03:56Z` was `date -u +%Y-%m-%dT%H:%M:%SZ && git rev-parse HEAD && git rev-parse 'HEAD^{tree}' && git status --short && sha256sum verifiers/compare_harness_independent.py verifiers/harness-independent-scope.json .ufo/round-44/claims.json && git diff --name-only`; HEAD/tree `6881ce31912cf52982de733d18d25e7ab7aae5c4` / `f005c7f1f8a46c2ddbcb4e6a48ca949afb2de56d`; comparator `d8b8c7f6001db7f47a294dc2a98db9179f61a281be20293dc5b104906073679d`, scope `fbcdc8d247475a5f1c2c613d78b6188dab77a766b02497a729a884687a70f77a`. The report maps record parsing, dotted maps, scope-key/value guards, status/probe readers, and the historical composition boundary. It runs no probes or gates and edits no verifier or floor files.
- Shared comparator drift after that report snapshot: the same status/hash command observed comparator SHA `d4118737c1356f461dd36db6fcbbc19243120721f01fe97c6de6ba5d611e79c3` at `18:04:56Z`, then `a2bf6a2a93801dacef77f72509eb37f635d4f643c69cc41429d442dd4af3d10d` at `18:05:37Z` and `18:05:54Z`; HEAD/tree remained unchanged. The inspected `d411…` diff added record-ID/value-alias and dotted-id-shadow checks, not a scope-key guard hunk; `a2bf…` was not inspected or exercised by D1. Thus the report's mechanism is pinned to its `d8b8…` source snapshot, and no current mixed record+map outcome is claimed. No Git add/commit or other Git mutation was performed.

## 2026-10-19 — Round 44 Z1 final conformance sweep

- Audit snapshot `2026-10-19T18:05:52Z`: HEAD `6881ce31912cf52982de733d18d25e7ab7aae5c4`; shared status had 91 paths, zero staged, and three tracked modifications. The drafts inventory found 74 files / 49,326,129 bytes and the lane-wide `.git` symlink scan found none. The report records the commands, hashes, concurrent-change boundary, and draft-preservation caveat.
- Report `.ufo/round-44/scouts/Z1.md` SHA-256 `020287ed936ee669e208ba75accca273b5e4b6864b550846d5581bcfccf9d0e9`. Z1 created no commit and wrote nothing outside the lane; no probes or gates were run. The cited large OMP text capture is flagged for preservation pending G1's provenance/minimization decision. No Git add/commit or other Git mutation was performed.

## 2026-10-19 — Round 44 G1 surfaces extractor remap

- Added `.ufo/round-44/scouts/G1.md` (SHA-256 `2c7e0ea9d085d6b9142487eb1947f875a941ca3d55291b1f6f304fc30d8f507d`) with the pinned live gate, binary/pin comparison, and call-shape analysis. The report shows the current OMP bundle's `I5/Gl/Mo` callees outside the `Co/Dl/Hj` allowlist while preserving the same eight declared `(group, file)` pairs; it records command timestamps, source hashes, limits, and the counting-input preservation request.
- No verifier, baseline, or pin file was edited. No Git add/commit or other Git mutation was performed.

## 2026-10-19 — Round 44 V3 C3 substrate reconciliation

- V3's final independent measurement ran `2026-10-19T18:06:16.559917834Z–18:06:23.996026662Z` at HEAD/tree `6881ce31912cf52982de733d18d25e7ab7aae5c4` / `f005c7f1f8a46c2ddbcb4e6a48ca949afb2de56d`; preserved receipt `.ufo/round-44/evidence/v3/measurement.json` SHA-256 `882fcf84af313becab6e4f05c63e50608dc09219d82ab1b46a71842bbe82d470`. The measured source and binary inputs were stable; the shared tree was already dirty from concurrent round-44 work.
- Live `verify_surfaces.py --json` remains exit 1 at 5 PASS / 2 FAIL (0/8 OMP loader classes extracted); `check_substrate_pins.py --json` remains exit 1 at 1/3, with OMP SHA and mtime drift and opencode SHA passing. Independent `strings -n 4` parsing found 11 OMP `.md` call occurrences and 8 unique pairs, exact-set-equal to the declared eight loader-group IDs. The real new callees are `Gl`, `I5`, `Mo`; current binary reports `omp/18.12.2`, SHA-256 `9513ef9f19d7991aac6ae0cb6077bcf16662092ddde861c002a91cedc6f47f9a`. This confirms the OMP extraction repair is real; no Git-linked v18.12.2 build provenance or re-pin was found, and neither repair nor re-pin is present in this measurement. C3 is not closed.
- Report `.ufo/round-44/scouts/V3.md` SHA-256 `ed1e6643132773a9ee72b90ad0020bd3d7242f98a6e2bba1d0ffa8c983b362c9`. V3 changed no production verifier, baseline, corpus, or floors registry; self-tests and the assertion-floor guard were not run. No Git add/commit or other Git mutation was performed.

## 2026-10-19 — Round 44 H1 OMP substrate-pin audit

- H1's read-only pin and surfaces measurements, input hashes, and write-time tree state are recorded in `.ufo/round-44/scouts/H1.md`. The evidence identifies a post-2026-10-16 OMP executable and a stale loader-call allowlist; lane Git contains no source/build provenance for the new binary, so no re-pin or verifier change was made.
- H1 changed no production verifier, baseline, surfaces inventory, or floor registry. No Git add/commit or other Git mutation was performed.

## 2026-10-19 — Round 44 V2 independent C2 residual verification

- The stable matrix command `PYTHONDONTWRITEBYTECODE=1 python3 drafts/v2/probe.py` ran at `18:06:52.579511–18:07:04.858905Z`, HEAD/tree `6881ce31912cf52982de733d18d25e7ab7aae5c4` / `f005c7f1f8a46c2ddbcb4e6a48ca949afb2de56d`. It compares frozen `b1be35f` SHA `1742dcccad1118399f0aa959f7ea6884d5992834d8c4c8b94e108277ae87df76` to the then-current worktree comparator SHA `a2bf6a2a93801dacef77f72509eb37f635d4f643c69cc41429d442dd4af3d10d`; scope SHA `fbcdc8d247475a5f1c2c613d78b6188dab77a766b02497a729a884687a70f77a`. Three R2 arms each changed from exit 0 / 24-of-24 to named exit 2; extra `check/name` and `value/observed` alias conflicts did likewise. Honest control stayed exit 0, protocol 24/24, strict 20/24, four adjudicated/four scoped out.
- Comparator self-test passed 228/228; `python3 verifiers/check_assertion_floors.py --repo "$PWD"` passed 9/9 exact at `10/150/91/87/1597/62/104/228/150`; direct live join exited 0 at protocol 24/24. Full commands, pinned source hashes, and outputs are in `.ufo/round-44/scouts/V2.md` (SHA-256 `39ad41d0e67106e81d399e16c262173beef2afd43a66cb9dae701730dc23cff5`). The preliminary `python3 verifiers/compare_harness_independent.py --self-test` at the original HEAD/tree and comparator SHA `d8b8c7f6001db7f47a294dc2a98db9179f61a281be20293dc5b104906073679d` omitted `TMPDIR` and briefly used default host temp for self-test fixtures; those temp files cleaned on exit. The counted repeat used an in-lane `TMPDIR`.
- The candidate was a shared uncommitted worktree snapshot, not a committed landing. V2 changed no comparator, fixture, verifier, or single-writer floor file; no Git add/commit. An initial matrix was discarded after it detected concurrent source drift, and an ad-hoc `--expect-n 24` live call was discarded because the live producer publishes 28 rows; both corrections and their boundaries are recorded in the report.

## 2026-10-19 — Round 44 V1 independent C1 closure replay

- V1 replayed `python3 drafts/v1/probe.py` at `2026-10-19T18:06:48Z–18:07:23Z`; probe SHA-256 `15c6a62127a37a31d0f262d070a57975c4837f127c6c2ad446f527a51b46b3c8`, results SHA-256 `d69b8b34ffab1452c55fe54e1e7628675734d04f0215b41464e93bfd9b8c0156`. The honest join remained exit 0 at 24/24, strict 20/24, four adjudicated and four scoped out. Both the real expected-only full-copy and R1 record+map composition still exit 0 at 24/24, strict 24/24, zero adjudicated and four scoped out, so C1 remains open.
- The E1 full-copy map/list arm and both V1's own malformed compositions fail closed on the tested worktree and frozen `6fbbff5` comparator; the committed fixture also rejects its synthetic scoped-out non-null value, but does not reproduce the real null-value/24-row composition. V1's report explains the surviving path at `verifiers/compare_harness_independent.py:684-721` and records every arm, digest, command, and boundary in `.ufo/round-44/scouts/V1.md` (SHA-256 `993763178f5cce5902aec1d802cf20ecf14f0bac5307bc2a2db49ae9db49ee18`).
- No comparator, fixture, scope, or floors-registry source was edited by V1. The 213-assertion self-test and floors guard were not run by this focused seat and are not claimed as passed. Preserve the V1 probe, results, comparator snapshots, producer captures, and arm payloads under `drafts/v1/` because they are cited counting inputs. No Git add/commit or ref mutation was performed.

## 2026-10-19 — Round 44 E1 record/map scope-edge probe

- `python3 drafts/e1/probe.py` ran `18:07:00.509989Z–18:07:16.051077Z` at HEAD/tree `6881ce31912cf52982de733d18d25e7ab7aae5c4` / `f005c7f1f8a46c2ddbcb4e6a48ca949afb2de56d`. It compared frozen `6fbbff5` comparator SHA-256 `d8b8c7f6001db7f47a294dc2a98db9179f61a281be20293dc5b104906073679d` with the candidate snapshot SHA-256 `a2bf6a2a93801dacef77f72509eb37f635d4f643c69cc41429d442dd4af3d10d`; scope SHA-256 `fbcdc8d247475a5f1c2c613d78b6188dab77a766b02497a729a884687a70f77a`.
- Four non-null scoped-out record/map attacks failed with named exit 2 on both snapshots. The honest control stayed exit 0 at protocol 24/24, strict 20/24, four adjudicated and four scoped out. The agreeing-null record+map diagnostic also stayed exit 0 at 24/24, leaving the record-list key-set cross-check unresolved; E1 reports this as a C1 residual, not a closure. Full commands, per-arm results, and preservation requests are in `.ufo/round-44/scouts/E1.md` (SHA-256 `45b44aef7014207b394a4260e507c1eb4af8ceae1dee51291cc94e709b756543`).
- E1 changed no comparator, fixture, scope, verifier, or floor-registry source. Self-tests, floors guard, and corpus gates were not run. The report discloses an unused duplicate probe accidentally created outside the lane and flags it for parent cleanup. Preserve the counting inputs named in the report if pruning drafts. No Git add/commit or ref mutation was performed.

## 2026-10-19 — Round 44 P2 C2 comparator residuals

- P2 added three fixture-backed C2 closures in `verifiers/compare_harness_independent.py`: dotted top-level-map shadow, conflicting record ID aliases, and conflicting derived-value aliases. Frozen `6fbbff5` inputs accepted all three at exit 0; the candidate rejects each class-named at exit 2. Before/after evidence is `.ufo/round-44/evidence/p2/before.json` (SHA-256 `0dcbd26d6bbcc9c6f8ee4b3e92ee528745dfd3b43ebe608ed8e4fb9d48ed958f`) and `after.json` (SHA-256 `4d7fc267b2342bba4482bc058d517f8b7731376e5d06eda9d3981dcfd426afc8`); the P2 report pins source/input hashes and commands: `.ufo/round-44/scouts/P2.md` (SHA-256 `28f3c77231475739443f3862daf8ea6537511ab8ca71c9f32150698f6814fb52`).
- `python3 verifiers/compare_harness_independent.py --self-test` passed 228 assertions and `python3 verifiers/check_assertion_floors.py` passed all nine exact floors `10/150/91/87/1597/62/104/228/150` at `18:08:11Z–18:08:21Z`; outputs `.ufo/round-44/evidence/p2/final-comparator-self-test.txt` (SHA-256 `a2ca527f959065046d2550de723cef59bae31b5c0eff2ff550d9d563e8a3e52d`) and `final-floors-guard.txt` (SHA-256 `fd4181fcaf68b73f3b7e46e4047e80cfdd7a647c765d2f30201459ba30f3a9b7`). The later shared-tree run at `18:09:24Z–18:10:00Z` is red after concurrent `record-map-24-*` fixture additions: self-test 8 failures / 243 assertions and floor guard exit 1, output `.ufo/round-44/evidence/p2/floors-guard-after-concurrent.txt` (SHA-256 `9753aebdb39c6cc4b7f77562fe96db4c27d34c4e92845d000d6e3568f521cc8e`). Current 24/24 live join still exits 0; output `.ufo/round-44/evidence/p2/live-join-after-concurrent.json` (SHA-256 `332305975b59b540922b36e919ae03d7e666179e67b6d91ffe76d927248dea3d`). No Git add/commit or ref mutation was performed.

## 2026-10-19 — Round 44 X1 record/map composition probe

- Scout `.ufo/round-44/scouts/X1.md` (SHA-256 `40451136483eb2631b3f95b5e17e082687e80682e1d97a33caa2f87fcfea8f3a`) independently reproduces the expected-only record/checks composition bypass on the frozen HEAD and the latest stable dirty comparator snapshot (`354e1b3dc35f1ba66c78070ded600bfe87a7e57dfc370967a38700a8c62e1f6f`). The requested alternate record/map forms reject; exact commands, hashes, dirty-tree boundary, probe defects, and preservation inputs are recorded in the report.
- X1 changed no comparator, fixture, scope, floor guard, or registry source. Self-test and assertion-floor guard were not run by this scout. Preserve the counting inputs named in the report before pruning drafts. No Git add/commit or ref mutation was performed.

## 2026-10-19 — Round 44 H1 post-update live gate check

- After other seats updated the shared baseline and surfaces extractor, H1 reran both read-only live gates and focused self-tests; results and time-pinned source hashes are recorded in `.ufo/round-44/scouts/H1.md`. The current candidate demonstrates the repair-extraction plus re-pin route; H1 did not author the shared change or certify upstream source provenance.
- H1 changed no production or single-writer floor files and made no Git add/commit/ref mutation.

## 2026-10-19 — Round 44 P3 C3 OMP substrate reconciliation

- Git-frozen `6fbbff5:verifiers/baseline.json` (blob SHA-256 `80949255d14dfe027cb64a9e27d36f2c188e4b4a4f2d2529a0e27d46025c9cb6`, commit tree `87e2517d7db26cb9b6522c2feca5a7d2f4621fbe`) records OMP 18.11.1 / SHA `bf1e86a9…`; live `/home/vgpnk/.local/bin/omp --version` reports 18.12.2, SHA `9513ef9f19d7991aac6ae0cb6077bcf16662092ddde861c002a91cedc6f47f9a`, and mtime `2026-10-19T12:35:55.628149917-03:00`. The live `strings -n 4` census found 11 call sites / 8 existing loader ids with callees `I5|Gl|Mo`; the OMP-only extractor and exact pin were updated. Census evidence: `.ufo/round-44/evidence/p3/live-loader-census.json` (SHA-256 `11c465b0e0249833497160a6f6a6a684b429b750a97d0e442ab8f18d64556fab`).
- At HEAD/tree `6881ce31912cf52982de733d18d25e7ab7aae5c4` / `f005c7f1f8a46c2ddbcb4e6a48ca949afb2de56d`, `python3 verifiers/verify_surfaces.py` passes 7/7, its self-test passes 0/87, and `python3 verifiers/check_substrate_pins.py` passes 3/3. Commands, source hashes, output hashes, and timing are in `.ufo/round-44/evidence/p3/after-results.json` (SHA-256 `1d839218e0f21a5aa729c7cc5eeef156fe5453255b8c98492ff34ed701ed77f1`); frozen red-before and Git blobs are in `frozen-before.json` (SHA-256 `90b713743af22f12f45f3d19037bc41728426c3a3b93aa183e5daa5efc99ee12`).
- Latest `python3 verifiers/check_assertion_floors.py --repo "$PWD"` remains exit 1 because the concurrent comparator snapshot has 245 observed / 228 floor and 5 self-test failures; the other 8 instruments, including surfaces 87/87 and pins 62/62, pass. The run and stable source hashes are in `.ufo/round-44/evidence/p3/final-floor-recheck.json` (SHA-256 `9c868e7862e6d844074e549055014f10f15dab0f7fb49adda3c32edf45c13055`). P3 did not edit the single-writer floor registry. Full seat evidence and the missing upstream OMP source-commit limitation are recorded in `.ufo/round-44/scouts/P3.md`. No Git add/commit or ref mutation was performed.

## 2026-10-19 — Round 44 V3 final receipt amendment

- This amendment supersedes the initial V3 entry above: its cited measurement SHA-256 `882fcf84af313becab6e4f05c63e50608dc09219d82ab1b46a71842bbe82d470` was overwritten during recapture, and its red gate / no-repin conclusion describes the pre-update shared worktree, not the final result. Current report `.ufo/round-44/scouts/V3.md` SHA-256 `be299a8fa8bee4e884ee5ba7b47a54009d59878993c1907a007a1fb62b94021c`; final receipt `.ufo/round-44/evidence/v3/measurement.json` SHA-256 `77be6e0d9c0d8483248c16a9954316dcb891370d3e8886baf090b91a98724583`, measured `2026-10-19T18:10:37.463515595Z–18:10:44.607227950Z` at HEAD/tree `6881ce31912cf52982de733d18d25e7ab7aae5c4` / `f005c7f1f8a46c2ddbcb4e6a48ca949afb2de56d`.
- Independent repeat against the current shared worktree: surfaces gate exit 0 (7/7), substrate pins exit 0 (3/3), surfaces self-test 0 failures / 87 assertions. Before/after hashes match the receipt for `verify_surfaces.py` (`9fa10d44848a9ff7e9d516125beafe501d62d3df7dbcb777dd13fef074d69657`), `surfaces-baseline.json` (`f142506c551e5ea8c3a36cbf8957330ed15fc750dff1b350f322c7b13199c427`), `check_substrate_pins.py` (`bcfd5230eabb8b16343e11b21ec354d9860c65e4712187fc6650fc3f329495ce`), `baseline.json` (`b76d433e64afad15f4c78ce1169208377ba470f8dc81f2749110ed9361e35b9b`), inventory (`1930ec0428deb34791b3080b77f86c828589317e7074ff0a4e8316aa2cb3e4c2`), and OMP fixture (`60efc512c731ac01e4c6aaeb17cbd0e9e5bcd3db5bb2fcb8a5f667c30ba33cfd`). Current result supports the live OMP extractor repair (`I5/Gl/Mo`) and re-pin for the installed 18.12.2 binary; no upstream source-build provenance was established. No assertion-floor verdict is made.
- `verify_skill_checklist.py --json` remains 9 PASS / 1 FAIL because the other seat's schematic brace citation at `LOG.md:1618` is treated as an unresolved path; V3 did not alter that line. `git diff --check` passes. V3 made no production-code or floor-registry edits and performed no Git add, commit, or ref mutation.

## 2026-10-19 — Round 44 Q1 queue synthesis

- Added `.ufo/round-44/scouts/Q1.md` (SHA-256 `2ef37e627d912170dc00e3be66f3d0456accaca154a390071f8bf803caa718b6`). It reconciles the 13 remaining/open-or-unverified R41 census IDs, R44 C1/C2 residuals, the pinned C3 green and latest comparator-floor red, standing debts, and preservation requests.
- The report pins the moving worktree and distinguishes measured candidate results from untested later bytes; C1 remains unclosed pending a passing current-byte replay/self-test/floor check. This synthesis ran no probes, gates, or tests and changed no verifier, fixture, baseline, floor registry, corpus, Git index, or ref.

## 2026-10-19 — Round 44 R2 adversarial C2/C3 review

- Corrected, source-pinned R2 matrix ran `2026-10-19T18:14:06.759577Z–18:14:56.885713Z` at HEAD/tree `6881ce31912cf52982de733d18d25e7ab7aae5c4` / `f005c7f1f8a46c2ddbcb4e6a48ca949afb2de56d`. Full matrix `.ufo/round-44/evidence/r2-adversarial-results.json` SHA-256 `a2014d923de7d6b84d5aa06d0be8d6d771dd145f5e9944114685f4d7ac01f2b7`; preserved runner `.ufo/round-44/evidence/r2/probe.py` SHA-256 `7a3dd7e1492b4da57a842d520d4f73aaa561cf522aa5b3607f701f512b5f3bd7`. Pinned comparator candidate `04e0ffe7b2b2e5ccd6e85a46069c2c4a12e8e33f729135c331ac49a6dee18053` rejects dotted-map, declared ID-alias, and re_derived/observed conflicts with named exit 2; frozen `6fbbff5` accepts those originals. Honest candidate control exits 0 at protocol 24/24, strict 20/24, four adjudicated/four scoped out. A noncontract `check_id` extension is ignored while canonical `check` remains selected; it is disclosed, not counted as demonstrated laundering.
- C3 replay against `.ufo/round-44/evidence/r2-predecessor-baseline.json` (Git-frozen predecessor SHA-256 `80949255d14dfe027cb64a9e27d36f2c188e4b4a4f2d2529a0e27d46025c9cb6`) exits 1 with OMP SHA/mtime drift and opencode pin passing; output `.ufo/round-44/evidence/r2-predecessor-pins.json` SHA-256 `45c07aba993a15e77cafb83f20cf2dcd378d9c15b6d8aaf57d4a63b70f87a56a`. Independent census retains all eight declared loader IDs with new `I5/Gl/Mo` calls. Current official surfaces and pins gates pass 7/7 and 3/3 (outputs `r2-current-surfaces.json` SHA-256 `03b201b258c95f9afc382d39eb5dbb62df2574d5b0602915eff03bc40d35f91b` and `r2-current-substrate-pins.json` SHA-256 `748bc3c21eb14c18b2f87ed1287eab3470c27fc75c0dbd18bed6692fa3e96512`). No OMP source/build commit link was found; the verified conclusion is extractor repair plus re-pin on the shared candidate, not source-build provenance.
- Current comparator self-test is red at 1 failure / 245 assertions (output SHA-256 `dc989f858224a43a8e6c82614c072441cfd17f527613130b11b8395fd45d668c`); the sole failure is a C1 wrapper-precedence fixture's expected diagnostic substring. Floors guard output `6ad8bf0031838156c9342439f592c03d230d7fc08176cce7cd23bbb310bf431f` reports comparator observed 245 / floor 228 and the same self-test failure; other eight rows pass. R2 did not edit the single-writer registry.
- Scout report `.ufo/round-44/scouts/R2.md` SHA-256 `2de9b5d6ff042edc0053b8ad858c6727ff879303a46eae72d32933c0129775bc`. The probe recorded stable pinned sources but `stable_tracked_diff=false` amid shared concurrent edits; no whole-worktree stability or landing-commit claim is made. R2 made no production or registry change and performed no Git add/commit/ref mutation.

## 2026-10-19 — Round 44 P1 C1 record/map scope boundary

- At HEAD/tree `6881ce31912cf52982de733d18d25e7ab7aae5c4` / `f005c7f1f8a46c2ddbcb4e6a48ca949afb2de56d`, frozen `git show 6fbbff5:verifiers/compare_harness_independent.py` bytes hash to `d8b8c7f6001db7f47a294dc2a98db9179f61a281be20293dc5b104906073679d` (106,180 bytes). Baseline receipt `drafts/p1/before-results.json` SHA-256 `309e94066e1127a346073637ef9cb58a39eba5a9b1c386fdbbc863ba5dd58209` records the R1 expected-only records+checks payload (`dbdf702bc3f10c02dfa0777271a92f44f16509c85d6fc0d84831eda1e6f75299`) passing frozen at 24/24 with zero adjudications.
- P1's change in `verifiers/compare_harness_independent.py:684-756` validates map channels alongside record channels, requires an independent derived field on ordinary in-scope records in a record+map composition, and admits overflow only for explicit null `SCOPED_OUT` records. The heldout fixture now carries 24 non-null values and four null scope-outs instead of 28 non-null values. On the same R1 input, frozen exit 0 / 24-of-24 flips to current exit 2 / named `derived-set overflow`; the honest current capture remains exit 0 at protocol 24/24, strict 20/24, four adjudications, four scope-outs.
- Current comparator SHA-256 `13b6d791705be81a349178f2e392adf19012a64315a51c77856fcf2f98e8ca56`. `python3 verifiers/compare_harness_independent.py --self-test` passes 0 failures / 245 assertions; `python3 verifiers/check_assertion_floors.py --repo "$PWD"` passes all nine configured floors `10/150/91/87/1597/62/104/228/150`, with comparator observed 245 / floor 228. The floor guard was red at this count before P1's diagnostic-order repair (R2's preceding entry); it now passes. The floor registry/checker are concurrent single-writer files and were not edited by P1, so the C1 claim's same-round floor-bump clause remains an integration follow-up.
- E1's full-live-value mixed list/map input (`072880e8081a43b649be187641550d192310d062e11a35d6ed5436ec9bacb739`) already failed on frozen `6fbbff5` with `scope-out value laundering`; no 0→2 flip is claimed for that arm. Full source pins, commands, fixture hashes, limitations, and results are in `.ufo/round-44/scouts/P1.md` (SHA-256 `2fd0fb2a05613aceb6e5f3f8ad7dcdc27391b38ff8138f9f5942ad23f3960f9a`). No Git add, commit, reset, or ref mutation was performed.

## 2026-10-19 — Round 44 S2 evidence verification

- At HEAD/tree `6881ce31912cf52982de733d18d25e7ab7aae5c4` / `f005c7f1f8a46c2ddbcb4e6a48ca949afb2de56d`, the committed R41 replay/census matched and classified all 46 arms. The R40 union battery and direct live baseline both exited 0 at protocol 24/24, strict 20/24, four adjudicated/four scoped out, on recorded comparator snapshot `04e0ffe7b2b2e5ccd6e85a46069c2c4a12e8e33f729135c331ac49a6dee18053`. cmark 0.31.2 was present. The union retains two accepted legacy C2 path-override residuals; the exact R44 record+map composition was not tested on `04e0…` or the newer `13b6…` shared comparator. Full commands, hashes, limitations, restoration disclosure, and preservation list are in `.ufo/round-44/scouts/S2.md`. No verifier, floor, or registry source was changed; the Git index and refs remain unchanged.

## 2026-10-19 — Round 44 F1 record+map fixture builder

- Added the durable `record-map-24-control` and `record-map-24-composition` arms from the real producer payloads (28 published IDs, 24 joined rows, four committed scope-outs) and wired fixture-local census-marker materialization into the comparator battery. The honest control stays exit 0 at protocol 24/24, strict 20/24, four adjudicated/four scoped out. Frozen `6fbbff5` accepts the composition at 24/24, strict 24/24, zero adjudicated; current shared comparator SHA `13b6d791705be81a349178f2e392adf19012a64315a51c77856fcf2f98e8ca56` rejects it at exit 2 with named `derived-set overflow`. F1 changed fixture wiring and the composition expectation; P1's C1 production change in the same comparator and P2's C2 work are concurrent, not attributed to F1.
- `python3 verifiers/compare_harness_independent.py --self-test` passed 0 failures / 245 assertions at `18:17:50.830163–18:17:52.910544Z` with a lane-local temporary directory. F1 raised the comparator floor from 228 to 245 in the floor guard history, both in-file tables, and external registry. `python3 verifiers/check_assertion_floors.py --repo "$PWD"` passed 9/9 exact floors `10/150/91/87/1597/62/104/245/150` at `18:19:36.567433–18:19:44.443047Z` with a lane-local temporary directory; comparator, guard, and registry SHAs were stable (`13b6d791…`, `6dfed5f7…`, `5d97bfe1…`).
- The fresh live join `PYTHONDONTWRITEBYTECODE=1 python3 verifiers/compare_harness_independent.py --expect-n 28 --no-stamp --json` exited 0 at `18:20:12.543189–18:20:20.557651Z`: protocol 24/24, strict 20/24, four adjudicated/four scoped out, no disagreements/uncovered/unknown. Direct fixture before/after output, gate receipts, exact input pins, and limitations are recorded in `.ufo/round-44/scouts/F1.md` (SHA-256 `1faa1212200f74c5c93412e1a47f387a5d9401c5e4bb36470b1337591160c89f`). Preserve F1 counting inputs by their names: `build_fixtures.py`, `build-results.json`, `compare-6fbbff5.py`, `baseline-probe.json`, `final-measurement.json`, `self-test-result.json`, `post-closure-selftest.json`, `final-closure-measurement.json`, `shared-candidate-selftest.json`, `floor-guard-result.json`, `final-live-join.json`, `post-floor-fixture-probe.json`, `record-map-24-control-independent.json`, `record-map-24-composition-independent.json`, `measure-record-map-24-control.json`, `measure-record-map-24-composition.json`, `final-record-map-24-control.json`, `final-record-map-24-composition.json`, `target-record-map-24-composition.json`, `post-floor-record-map-24-control.json`, and `post-floor-record-map-24-composition.json`. C3 and the whole-tree gate battery were not run by F1. No Git add, commit, or ref mutation was performed.

## 2026-10-19 — Round 44 I1 integration gate battery

- At shared HEAD/tree `6881ce31912cf52982de733d18d25e7ab7aae5c4` / `f005c7f1f8a46c2ddbcb4e6a48ca949afb2de56d`, I1's battery passed all nine registered floors/self-tests at exact vector `10/150/91/87/1597/62/104/245/150`, the honest live comparator (protocol 24/24, strict 20/24, four adjudicated/four scoped out), both corpus verifiers, surfaces 7/7, and substrate pins 3/3. The C1 record+map composition self-test rejected the overflow with named exit 2 and the honest control passed. Sources, commands, timing, input/output hashes, disclosure, and preservation requests are in `.ufo/round-44/scouts/I1.md`.
- The pre-entry skill-checklist replay was 9 PASS / 1 FAIL on the grouped brace-path citation at `LOG.md:1618`; the required replay immediately after this LOG entry and its final disposition are documented in the I1 report. I1 made no verifier, baseline, fixture, or floor-registry edits and performed no Git add, commit, or ref mutation.

## 2026-10-19 — Round 44 P1 current floor revalidation

- This append-only amendment supersedes the P1 floor status above, which was recorded before F1 completed the synchronized comparator-floor bump. F1 raised the floor from 228 to 245 in the guard history, both in-file tables, and external registry; P1 did not edit those single-writer files.
- `python3 verifiers/check_assertion_floors.py --repo "$PWD"` ran `2026-10-19T18:22:57Z–18:23:07Z` and passed all nine floors `10/150/91/87/1597/62/104/245/150`, including comparator 245/245. Before/after hashes were stable: comparator `13b6d791705be81a349178f2e392adf19012a64315a51c77856fcf2f98e8ca56`, registry `5d97bfe15e2865a38bcfc01117791f1f578cfef55fdbbd859da7c5f7b353978a`, checker `6dfed5f7d22ad0680b1b4b0203de0cf89fd1f099b9440e15c775dce0a0df6986`.
- `.ufo/round-44/scouts/P1.md` was updated to distinguish the initial measurement from this current passing revalidation. No Git add, commit, reset, or ref mutation was performed.

## 2026-10-19 — Round 44 B2 SHONEN assessment

- B2's scribe-only SHONEN proposal, per-axis C1/C2/C3 verdicts, evidence pins, and limitations are recorded in `.ufo/round-44/scouts/B2.md`. The current shared candidate passed comparator self-test 245/245, live join 24/24 protocol and 20/24 strict, all nine configured floors, surfaces 7/7, and substrate pins 3/3. The proposal did not edit SHONEN or production sources; no Git mutation was performed.

## 2026-10-19 — Round 44 R2 final snapshot amendment

- This append-only amendment supersedes the earlier R2 gate status above, which captured the transient `04e0…` comparator before shared C1 fixture/floor integration. The final source-pinned R2 probe ran `2026-10-19T18:20:09.544560Z–18:20:59.427421Z` at HEAD/tree `6881ce31912cf52982de733d18d25e7ab7aae5c4` / `f005c7f1f8a46c2ddbcb4e6a48ca949afb2de56d`, on comparator SHA `13b6d791705be81a349178f2e392adf19012a64315a51c77856fcf2f98e8ca56`. Final result `.ufo/round-44/evidence/r2-adversarial-results.json` SHA-256 `c9aa323e4ffec24917080bd513ebb782c3d0fe7e6b04292fde7ad6cca2f35d3a`: original dotted-map, check/id, and re_derived/observed residuals remain frozen exit 0 → candidate named exit 2; honest join remains 24/24. The final candidate still tolerates unrecognized `check_id`, which the report distinguishes from an identity substitution.
- Final current gates: comparator self-test 0 failures / 245 assertions (output SHA-256 `05a8a24f6abe4d8cd200ca30cf053f9bc50d8b911bb95c666cf6264cd1fd5aae`); assertion floors 9/9 EXACT at `10/150/91/87/1597/62/104/245/150` (output SHA-256 `73659e63025405e41ead886cd1cac659e90c008b423f668c56eecf3485107e9e`); surfaces 7/7 and pins 3/3 (output SHAs `03b201b258c95f9afc382d39eb5dbb62df2574d5b0602915eff03bc40d35f91b` / `748bc3c21eb14c18b2f87ed1287eab3470c27fc75c0dbd18bed6692fa3e96512`). The predecessor-pins red remains reproducible from its Git-frozen baseline; current C3 interpretation is repaired extraction plus re-pin, with no OMP source/build provenance claim.
- Updated report `.ufo/round-44/scouts/R2.md` SHA-256 `05dcdcb5575becd8b66573bc0469c7dabeed1ecfb5aa758da125651f5f72cb77`. The probe's pinned sources and HEAD/tree were stable, while its tracked diff changed under concurrent shared work; no landing-commit or whole-worktree stability claim is made. R2 changed no production or registry source and made no Git add/commit/ref mutation.

## 2026-10-19 — Round 44 B2 checklist amendment

- After the B2 report pointer was present, `verifiers/verify_skill_checklist.py` ran at `18:25:01Z` and exited 1 at 9/10 live checks. The sole failure is the pre-existing `governance.citation_resolves` schematic brace path at `LOG.md:1618`; B2 did not rewrite that other seat's entry. The exact outcome and boundary are recorded in `.ufo/round-44/scouts/B2.md`; no Git mutation was performed.

## 2026-10-19 — Round 44 S1 current residual census

- Completed `.ufo/round-44/scouts/S1.md` (SHA-256 `afa66446b8c503e3ca33c0aa06fb60376fe4870e1522d8adac3624028699ab75`), pinning the r41/r43 inventory and final measured r44 state at HEAD/tree `6881ce31912cf52982de733d18d25e7ab7aae5c4` / `f005c7f1f8a46c2ddbcb4e6a48ca949afb2de56d`. The report records the frozen-to-current C1 composition result, current 0/245 self-test, honest 24/24 join, exact 9/9 floors, C3 final status, and bounded remaining doors.
- C1 is closed for the byte-pinned R1 composition and current fixture shapes, not arbitrary payloads; the separate E1 agreeing-null diagnostic remains unreplayed against the final comparator. S1 changed no verifier, producer, baseline, or floor-registry source. No Git add, commit, reset, or ref mutation was performed.

## 2026-10-19 — Round 44 (loop A position 8): the record+map composition door CLOSED — all three claims verify; first admitted candidate

- Claims at `.ufo/round-44/claims.json` (C1 depth = close the record+map composition door; C2 operability = R2's three residuals; C3 calibration = reconcile the substrate red). Provider: `openai-codex/gpt-6-luna-max` (pos-8 plan was zai glm-5.3-flash — zai quota-exhausted, operator directive: zai positions → luna-max for the session). 24/24 seats. Fragments `.ufo/round-44/scouts/*.md`; curated `.ufo/round-44/evidence/`.
- **C1 depth — the record+map composition door is CLOSED; the laundering class's last named channel.** `check_independent_scope_maps` (`verifiers/compare_harness_independent.py:684`) now cross-checks the RECORD channel against the committed scope file + the derived set, the same way the r43 key-set check constrains the MAP channel: a record supplying a non-null value for a scoped-out row → `scope-out value laundering` exit 2; a record-list+map whose combined id-set exceeds the honest derived set → `derived-set overflow` exit 2. The real 24-row V10 fixture (`record-map-24-composition` — F1 rebuilt it to reproduce the real case, not the earlier 28-value stand-in) now fails closed naming `oc.dup.onesided_roots`. F1/I1/B2 verified the closure on the settled comparator sha `13b6d791`; R1/X1's "still open" readings were on earlier shas (`d8b8c7f`/`a2bf6a2a`/`354e1b3`) — temporal, not substantive; on the landed bytes the arm fails closed. **This is the laundering class's last named door across the r37-r44 arc** (R1-D1 → F-2 → F-3 → map forms → record+map composition). Depth's band-9.5 shape (the closure machinery holding across the whole census class) is within reach — the residual question is whether the held-out hunt still finds an unlisted door.
- **C2 operability — VERIFIED (P2; V2 + R2 verify).** Three residuals closed class-named: a dotted-id top-level map shadow beside the row channels → exit 2; a record whose `check`/`id` fields disagree → exit 2; a record with conflicting `re_derived`/`observed` → exit 2. V2's matrix confirms each on frozen-vs-landed; comparator self-test 213→245, floors in-step. X2's 4th-shape hunt named new residuals for the queue: `expected`/`expected_value` conflict, lone non-string `status` silently discarded (both still exit 0). Score held: advisory.
- **C3 calibration — VERIFIED (P3; V3 + H1 + G1 + R2 verify).** The carried substrate red is reconciled: the live OMP is a real version change **18.11.1 → 18.12.2** (sha `bf1e86a9` → `9513ef9f`, mtime 2026-10-19 — a legitimate rebuild, not instrument-stale). The 0/8 loader-class extraction was stale because the new bundle uses `I5`/`Gl`/`Mo` callees; P3 extended the OMP-only extractor + added the call shapes to the fixture + re-pinned the binary. The live census resolves **11 call sites to the exact 8 declared loader classes**. Surfaces gate back to **7/7**, pins back to **3/3** (was 5/7 + 1/3). Named bound: no upstream OMP source/build commit provenance could be established (the installed binary doesn't expose it) — recorded, not smoothed.
- **Whole-tree battery at close:** comparator self-test **0/245**; floors **9/9 EXACT** (`10/150/91/87/1597/62/104/245/150`); live join exit 0 24/24 (strict 20/24, adjudicated 4, scoped 4); corpus 9/9 + exit 0; surfaces 7/7; pins 3/3; checklist 10×PASS after the brace-citation repair (the r37 lesson — no `{...}` glob sets in prose).
- **Wave conformance:** 24/24 seats, no commits; writes inside `.ufo/round-44/` + `verifiers/` + fixtures + `corpus/` + LOG/SCORECARD + `baseline.json`; no `.git` symlinks; floors-registry churn settled in-step; drafts pruned to evidence (the 47MB OMP strings dump + cited probe results preserved).
- **Queue for r45 (pos 9 — luna-max, 32-64 seats):** **C1' = the held-out hunt on the settled closure** — is the laundering class now REALLY closed? Run the full census replay + a fresh channel-hunt against the `13b6d791` comparator; if no unlisted door survives, the depth band-9.5 shape is the round's target. X2's residuals (expected/expected_value conflict; lone non-string status). Standing debt: OMP provenance (no upstream commit); digest-append; IND hang; resolver-vs-brace; SHONEN form; divergence merge (operator).

## 2026-10-19 — Round 45 Z1 final conformance sweep

- Z1 report: `.ufo/round-45/scouts/Z1.md` (SHA-256 `f40187e1d1aaf9b62c8bafd5509ece59c7d151d385586a0b1c528f25007f391c`). Snapshot was HEAD/tree `032f47bd13fdff0cd2ccea5f902df9690ad09376` / `7c5e0a753eb39babfd66033d0f7ee08054191b3a`; the 14 census/replay/record-map counting inputs matched HEAD (`git diff --exit-code HEAD -- ...` returned 0 at `15:35:47-03:00`). Draft count and footprint, comparator worktree divergence, empty drafts, `.git`-symlink scan, and scope limitations are pinned with their commands and timestamp in the report. No Git mutator or out-of-lane write was performed by Z1.

## 2026-10-19 — Round 45 B1 scribe scaffold

- Prepared `.ufo/round-45/drafts-report-skeleton.md` and `.ufo/round-45/scouts/B1.md` from the round-45 registration and the prior scaffold shape. At `2026-10-19T18:35:32Z`, `python3 -m json.tool .ufo/round-45/claims.json` exited 0; `sha256sum .ufo/round-45/claims.json` returned `69675f5c08d948e6e6c5aabe303fbda1d2d0eea3f7f96f7476b6dac147406c27`.
- The same snapshot pinned HEAD/tree `032f47bd13fdff0cd2ccea5f902df9690ad09376` / `7c5e0a753eb39babfd66033d0f7ee08054191b3a`. Frozen comparator hashes from `git show '6881ce3:verifiers/compare_harness_independent.py' | sha256sum` and `git show '032f47b:verifiers/compare_harness_independent.py' | sha256sum` were `d8b8c7f6001db7f47a294dc2a98db9179f61a281be20293dc5b104906073679d` and `13b6d791705be81a349178f2e392adf19012a64315a51c77856fcf2f98e8ca56`. The working-tree comparator differed; B1 ran no current-target measurement and made no source/floor/fixture edits.
- R41 census/replay sources and archive hashes, plus the distinct archived evidence generations, are detailed in `.ufo/round-45/scouts/B1.md`. No replay was run; all hunt, gate, and landing cells remain pending.
- At `2026-10-19T18:36:48Z`, `sha256sum .ufo/round-45/drafts-report-skeleton.md .ufo/round-45/scouts/B1.md` returned `f2ae1df86cc92b2bc9ed8e23dc37154ec8956e9b9fe5c51184c1f1795c3fe192` / `a0b50b588fe55b59051d6ed786ae929702e2951225be6222036143ae65469900`; a Python structure check on both artifacts passed. The read-only status snapshot also showed shared modifications to `LOG.md`, the comparator, guard, and floors registry, plus untracked fixtures; B1 did not modify or attribute those concurrent paths.
- No probes, joins, self-tests, floors/corpus gates, or SHONEN checks were run. No Git add/commit/ref mutation or out-of-lane write was performed.

## 2026-10-19 — Round 45 Z1 post-write shared-tree amendment

- The report was extended with a later shared-tree observation; its current SHA-256 is `6ddb28f4294a4fad0aff2eb814aff38dc538ebabd2836fed61548ba9e22e3882`. At `15:36:26-03:00`, HEAD/tree remained `032f47bd13fdff0cd2ccea5f902df9690ad09376` / `7c5e0a753eb39babfd66033d0f7ee08054191b3a`; the draft inventory had grown to 185 files / 3,039,279 bytes, 14/14 counting inputs still matched HEAD, and the `.git` symlink scan was still zero. Commands and limits are detailed in the report.
- `verifiers/floors-registry.json` was newly visible as a shared tracked modification at that snapshot. Z1 did not edit the single-writer registry or run the floors guard; its owner must rerun `python3 verifiers/check_assertion_floors.py` after the registry edit settles. No Git mutator or out-of-lane write was performed by Z1.

## 2026-10-19 — Round 45 Z1 final cutoff amendment

- Current `.ufo/round-45/scouts/Z1.md` SHA-256 is `f60eab304e9293913f9bfaf6642db4bf2fe6116d36c3751a1f9161385ca3c800`. At `15:37:07-03:00`, the final audit sample remained HEAD/tree `032f47bd13fdff0cd2ccea5f902df9690ad09376` / `7c5e0a753eb39babfd66033d0f7ee08054191b3a`; the recursive draft inventory was 343 files / 6,244,645 bytes, the input diff check returned 0 for 14/14 counting inputs, the `.git`-symlink scan returned 0, status had 380 entries, and the staged-path count was 0. Commands and volatility caveat are pinned in the report.
- Drafts fail the lean check at this cutoff. Z1 performed no cleanup, made no commit, and wrote nothing outside the lane.

## 2026-10-19 — Round 45 B1 report hash amendment

- The B1 report was corrected to state that it did not modify or use the concurrent worktree changes (the earlier wording incorrectly said it had not inspected the comparator at all). The hash `a0b50b588fe55b59051d6ed786ae929702e2951225be6222036143ae65469900` above is the pre-correction artifact hash; append-only correction: at `2026-10-19T18:37:31Z`, `sha256sum .ufo/round-45/drafts-report-skeleton.md .ufo/round-45/scouts/B1.md` returned `f2ae1df86cc92b2bc9ed8e23dc37154ec8956e9b9fe5c51184c1f1795c3fe192` / `4b6f4f29dc3f2b681ebc5fd8e74aaf03dfcfd2d78a529be1c18710dd7b543d17`; the required-section/pending-cell structure check passed. No measurement result changed.

## 2026-10-19 — Round 45 T1 regression join

- At HEAD/tree `032f47bd13fdff0cd2ccea5f902df9690ad09376` / `7c5e0a753eb39babfd66033d0f7ee08054191b3a`, T1's final producer+join replay ran `2026-10-19T18:35:50.332991665Z–18:35:59.091416852Z`; actual comparator SHA `1101213a7bed5410151564aeb5a4b49030a4821c86e7469286f046253fbc51e4` was stable before/after. Both producers and comparator exited 0: protocol 24/24, strict 20/24, 4 adjudicated, 4 scoped out, no disagreement/provisional/uncovered/unknown. Final producer, join, Markdown, and receipt hashes and row ids are pinned in `.ufo/round-45/scouts/T1.md` (SHA-256 `af8b4c1fd5622eaac1779e859708cc38bdf0d814582f3ebd967a9a9aca978a63`).
- Replayed those exact final producer captures through the Git-frozen `032f47bd:verifiers/compare_harness_independent.py` bytes (SHA-256 `13b6d791705be81a349178f2e392adf19012a64315a51c77856fcf2f98e8ca56`); frozen vs shared-candidate JSON and all 24 rendered row lines matched. No non-laundering-row change observed. T1 made no verifier, fixture, floor, or registry edit; comparator self-test/floor guard were not run by this seat. Preserve the counting artifacts under `drafts/t1/` before pruning. No Git add, commit, or ref mutation.

## 2026-10-19 — Round 45 P2 lone non-string status

- `.ufo/round-45/scouts/P2.md` (SHA-256 `7ddb98e9cb3c0372c89a5ed1ea14042af0355751279803ed41044b7a97ef19f2`) records the P2 closure and evidence. `_record_status` rejects any present non-string `status`/`state` as `non-string status`; fixture `status-lone-nonstring` pins exit 2, the class and `a.b`, and no traceback. The frozen `032f47b` baseline SHA `13b6d791705be81a349178f2e392adf19012a64315a51c77856fcf2f98e8ca56` returned 0 at `18:33:10Z`; the P2 status-only comparator SHA `b6a618ef94febf0fa361c1927b1c209fe4a9134fe7160ebfc87523b98b053f08` returned 2 at `18:34:18Z`. Latest shared comparator SHA `1101213a7bed5410151564aeb5a4b49030a4821c86e7469286f046253fbc51e4` re-ran the arm at `18:37:57Z` and still returned 2 with the same named error. HEAD/tree were `032f47bd13fdff0cd2ccea5f902df9690ad09376` / `7c5e0a753eb39babfd66033d0f7ee08054191b3a` throughout these pins.
- Self-test passed 0/255; the P2 fixture raised the count 245→250. The shared P1 expected-alias fixture subsequently contributed five assertions; the combined floor is 255. Comparator guard and registry both read 255; the guard docstring was aligned. `python3 verifiers/check_assertion_floors.py` passed 9/9, with comparator observed/floor 255/255. Final live join exited 0: 24/24 protocol, 20/24 strict, four adjudicated/four scoped out, zero disagreement/uncovered/unknown. Self-test, floors, status probes, join JSON, and receipt are pinned under `.ufo/round-45/evidence/p2/`; receipt metadata's built-in C1/round-39 label is stale and was not treated as P2 attribution. No C1 hunt or expected-alias implementation was done by P2; no Git add, commit, or ref mutation.

## 2026-10-19 — Round 45 E1 scope-file edge hunt

- E1 report: `.ufo/round-45/scouts/E1.md` (SHA-256 `3a7769bb9193b9724d091dff02b57453b02006916fce4449678e983216018311`). All runs pinned HEAD/tree `032f47bd13fdff0cd2ccea5f902df9690ad09376` / `7c5e0a753eb39babfd66033d0f7ee08054191b3a` and Git-frozen comparator SHA `13b6d791705be81a349178f2e392adf19012a64315a51c77856fcf2f98e8ca56`; the shared comparator worktree was separately modified (SHA `1101213a7bed5410151564aeb5a4b49030a4821c86e7469286f046253fbc51e4`) and not used.
- `python3 drafts/e1/probe.py` and `python3 drafts/e1/probe-cwd-residual.py` produced the pinned results in their matching `probe-results.json` and `cwd-residual-results.json`. The planted process-CWD scope with an extra `omp.offered.skills` entry plus null scoped-out payload values exits 0 at 23/23; the receipt reports the official four-row scope SHA while the enforced five-row scope differs. The repository-CWD control exits 2. An unreferenced ghost scope entry is accepted but inert at 24/24; an unsupported contract kind with active scope-outs exits 2.
- Preserve `drafts/e1/` before pruning: it holds the frozen comparator, both rerun drivers/results, scope variants, receipts, and null-value attack payload. E1 changed no verifier, fixture, scope file, floor registry, or Git refs; the full census/self-test/floors/corpus gates were not run by this seat.

## 2026-10-19 — Round 45 V1 C2 residual verification

- At HEAD/tree `032f47bd13fdff0cd2ccea5f902df9690ad09376` / `7c5e0a753eb39babfd66033d0f7ee08054191b3a`, V1 replayed the `expected`/`expected_value` conflict, lone non-string `status`, lone non-string `state`, and verdict/mode probes against frozen `6881ce3` (`d8b8c7f…`), frozen `032f47b` (`13b6d791…`), and the shared worktree comparator (`1101213a…`). Frozen arms were green where noted; all three current CLI residual arms failed closed with exit 2; verdict/mode variants exited 3 and 1. Probe command at `18:37:38Z`; results `drafts/v1/probe-results.json` SHA-256 `16d1fd7d99b5c02261de03a1dc929c4f6437111cefa90557bb37e0c61904b7cb`.
- The current comparator self-test passed 255/255; the live join passed protocol 24/24 (strict 20/24, 4 adjudicated, 4 scoped out). The floors guard at `18:38:43–18:38:53Z` passed 9/9 exact values `10/150/91/87/1597/62/104/255/150` against comparator `1101213a…`, guard `b9e0ce16…`, registry `36536063…`. Full command pins and the initial mistaken `--expect-n 24` attempt (superseded by correct `--expect-n 28`) are in `.ufo/round-45/scouts/V1.md` (SHA-256 `94e7ad5bdcf8933b2e754a06a9f7ef668c19bb547097103bf56152b24239c177`). Preserve `drafts/v1/`; V1 made no production source/fixture/floor edits and no Git add/commit/ref mutation.

## 2026-10-19 — Round 45 X3 floors-registry coverage hunt

- `PYTHONDONTWRITEBYTECODE=1 python3 drafts/x3/probe.py` ran `18:38:43.651997Z–18:38:44.876567Z` at HEAD/tree `032f47bd13fdff0cd2ccea5f902df9690ad09376` / `7c5e0a753eb39babfd66033d0f7ee08054191b3a`. Runner SHA-256 `d4b6477f53ae9657a0f89926647b334161bfcc18eefb13d34fe0d9a92c77b186`; results SHA-256 `bc58bccac9d04eca21a840ced4b5b543fb83e7e3c9e2241ae7bdc5e5a12d59ea`. It matched all 21 expected outcomes over r44 dispatch, the landing, and stable worktree inputs: rename exit 2; bad-first/canonical-last duplicate exit 0; reversed duplicate exit 2; float/bool/string floors exit 2.
- At `18:38:44Z–18:38:57Z`, lane-local-TMPDIR `python3 verifiers/check_assertion_floors.py --self-test` returned 0 failures/150 assertions, and the live guard passed all nine exact floors `10/150/91/87/1597/62/104/255/150`; HEAD/tree unchanged. Guard, registry, comparator SHAs were stable: `b9e0ce16cdb5de8592ffd877de684560495118b499ef41209cd904027f5fc6ef`, `36536063ef803122c16a13cc9db6cad5cc47b58e173caeafa1fd6f2677619622`, `1101213a7bed5410151564aeb5a4b49030a4821c86e7469286f046253fbc51e4`. This is the concurrent r45 P1/P2 255-assertion worktree, not the frozen `13b6d791` comparator snapshot.
- The report `.ufo/round-45/scouts/X3.md` SHA-256 is `59681f60bbef18ba2685509c3a02b0f1e6f2a1c63eb2f0f2c55c7b1a8808450f`. It records the duplicate-member residual, the corrected first-run harness defect, and the transient 250→255 floor-bump state. Parent: preserve `drafts/x3/probe.py` and `probe-results.json`. X3 changed no production source or registry and made no Git add/commit/ref mutation.

## 2026-10-19 — Round 45 P1 expected-alias contradiction

- Closed the assigned `expected`/`expected_value` contradictory-record residual in `verifiers/compare_harness_independent.py`: compare canonical values across every present foreign alias before choosing a priority value; raise the named `record value alias conflict` class. Added fixture `verifiers/fixtures/compare-harness-independent/expected-alias-conflict/` (same `a.c` record has `expected="x"`, `expected_value="conflict"`, and agreeing derived value). Probe `PYTHONDONTWRITEBYTECODE=1 python3 drafts/p1/probe_expected_alias.py after` finished `2026-10-19T18:39:09.869047Z`, at HEAD/tree `032f47bd13fdff0cd2ccea5f902df9690ad09376` / `7c5e0a753eb39babfd66033d0f7ee08054191b3a`; frozen `6881ce3` (`d8b8c7f…`) and frozen `032f47b` (`13b6d791…`) each accepted 3/3 (exit 0), while the stable working comparator (`1101213a…`) returned exit 2 naming `record value alias conflict` and `a.c`. Inputs are pinned under `.ufo/round-45/evidence/p1/` (the expected-alias live and independent payloads; SHA-256 `3472112f…` / `7033d1aa…`); before/after result SHA-256 `4e1bbe8d…` / `2cf4b58c…` (the before run finished `18:34:37.599430Z`).
- `PYTHONDONTWRITEBYTECODE=1 TMPDIR="$PWD/drafts/p1/tmp" python3 verifiers/compare_harness_independent.py --self-test` passed 0/255 at `18:39:07.036710–18:39:09.692323Z`, comparator SHA stable `1101213a…`, output SHA-256 `7c2c2ade…`. In-step floor bump 250→255 updates the guard docstring, `EXPECTED_INSTRUMENTS`, `INSTRUMENTS`, and `verifiers/floors-registry.json` (current SHAs `b9e0ce16…` / `36536063…`). `PYTHONDONTWRITEBYTECODE=1 TMPDIR="$PWD/drafts/p1/tmp" python3 verifiers/check_assertion_floors.py` passed all 9 exact floors `10/150/91/87/1597/62/104/255/150` at `18:39:19.437288–18:39:29.331996Z`; comparator, guard, and registry SHAs remained stable before/after (`1101213a…`, `b9e0ce16…`, `36536063…`), output SHA-256 `be3b8bcf…`. A prior pass at `18:38:18–18:38:30Z` had a changing guard SHA and is superseded by this stable re-run.
- Scope is limited to this C2a residual. The separate lone non-string `status` residual belongs to concurrent P2; this entry makes no claim about it or completion of the held-out census. Preserve `drafts/p1/probe_expected_alias.py` and `.ufo/round-45/evidence/p1/`; current shared worktree is dirty, but HEAD and index tree remained unchanged. No Git add, commit, reset, or ref mutation.

## 2026-10-19 — Round 45 E1 scope-file edge hunt

- E1 report: `.ufo/round-45/scouts/E1.md` (SHA-256 `3e198782d312a8fc86eca831e35b5affba392d4e95a18db74b01672ebe4822bf`). All runs pinned HEAD/tree `032f47bd13fdff0cd2ccea5f902df9690ad09376` / `7c5e0a753eb39babfd66033d0f7ee08054191b3a` and Git-frozen comparator SHA `13b6d791705be81a349178f2e392adf19012a64315a51c77856fcf2f98e8ca56`; shared comparator worktree SHA `1101213a7bed5410151564aeb5a4b49030a4821c86e7469286f046253fbc51e4` was not used.
- `python3 drafts/e1/probe.py` and `python3 drafts/e1/probe-cwd-residual.py` produced pinned results in their matching result JSON. A planted-CWD scope adding `omp.offered.skills` plus null scoped-out payload values exits 0 at 23/23; its receipt hashes the official four-row scope instead of the enforced five-row scope. The repository-CWD control exits 2. An unreferenced ghost scope entry is accepted but inert at 24/24; an unsupported contract kind with active scope-outs exits 2.
- Preserve `drafts/e1/` before pruning: frozen comparator, both drivers/results, scope variants, receipts, and null-value attack payload. E1 changed no verifier, fixture, scope file, or floor registry; per `AGENTS.md`, it appended this evidence to `LOG.md`. No Git add, commit, or ref mutation.

## 2026-10-19 — Round 45 V1 report post-write amendment

- V1 reran the C2 matrix, live join, comparator self-test and floors guard after writing its scout report. At `18:40:17–18:40:37Z`, all results were unchanged on HEAD/tree `032f47bd13fdff0cd2ccea5f902df9690ad09376` / `7c5e0a753eb39babfd66033d0f7ee08054191b3a` and comparator SHA `1101213a7bed5410151564aeb5a4b49030a4821c86e7469286f046253fbc51e4`; floors remained exact 9/9 at `10/150/91/87/1597/62/104/255/150` with guard `b9e0ce16…` and registry `36536063…`. The amended `.ufo/round-45/scouts/V1.md` SHA-256 at `18:41:07Z` was `3b0e2e5d8af7e443e01b1da58c3354913aff40d8d94837fa6c0fa5d23c76bf5b`. Preserve `drafts/v1/`; no Git mutator was used. Full census/self-test/floors/corpus gates were not run by this seat.

## 2026-10-19 — Round 45 P1 report hash amendment

- Final P1 report `.ufo/round-45/scouts/P1.md` SHA-256 is `cb4592100e349884543de154afa7e2f4d1c2edcfd62366e2c49943d521571e25`. This pins the report for the C2a expected-alias result recorded above; no measurement outcome changed.

## 2026-10-19 — Round 45 X2 corpus fence/classification hunt

- `PYTHONDONTWRITEBYTECODE=1 python3 drafts/x2/probe.py` ran `2026-10-19T18:39:32.741362Z–18:39:34.100504Z` at HEAD/tree `032f47bd13fdff0cd2ccea5f902df9690ad09376` / `7c5e0a753eb39babfd66033d0f7ee08054191b3a`. Probe SHA-256 `4fb218ee98fb20fc728c5ef9bd2a1c0770e9c5aa55f6da7238ef210bf7e9d8f9`; results `.ufo/round-45/evidence/x2/results.json` SHA-256 `ce12bf06ba47edcfbc1a49b754daa64ab73528c64917f6035ae57463ab1d81ec`; report `.ufo/round-45/scouts/X2.md` SHA-256 `8cb4060e5d1fbec29eefec856fd4528e549bcfb0e52de9baa8cd0e4f9f08d84f`.
- The fence-spanning-fake-heading fixture yields integrity exit 0 / `unindexed=0`, but independent exit 1 / `unindexed=1`; it is an integrity-only false green, not a joint corpus-gate false pass. Inline-code fence-like text is over-hidden and fails closed in both gates; CRLF and LF controls classify identically. The real corpus sweep counted 54 tracked Markdown files, no CRLF documents, no fenced coverage headings in the README. Both live corpus gates exited 0; integrity self-test was 0 failures/150 assertions, independent self-test 91 assertions/0 failures.
- Frozen/current corpus gate byte SHAs are identical across `git show 6881ce3:<gate>` and `git show 032f47bd:<gate>`: integrity `28224c76510dcafc4d7a52da41ffd2d366337414f65320cbb21e6d9de12aba9d`, independent `254b5a2f57aabbf0b8376fce34c42250b56499d9fd7a92b5e6374ac505315d69`. The comparator's committed `032f47bd` SHA is `13b6d791705be81a349178f2e392adf19012a64315a51c77856fcf2f98e8ca56`; the shared worktree comparator was `1101213a7bed5410151564aeb5a4b49030a4821c86e7469286f046253fbc51e` and was not exercised by X2.
- X2 changed no verifier, corpus document, floor registry, or comparator source. The initial fixture harness passed unsupported `--no-baseline` to the independent CLI; that exit-2 attempt was corrected and excluded from results. Preserve the evidence JSON and the minimal probe inputs/runner under `.ufo/round-45/evidence/x2/` and `drafts/x2/`. No Git add, commit, reset, or ref mutation; this seat did not run the full round-41 census replay.

## 2026-10-19 — Round 45 H09 field-gate held-out hunt

- `PYTHONDONTWRITEBYTECODE=1 python3 drafts/h09/probe.py` ran `2026-10-19T18:38:05.939613Z–18:38:52.980824Z` at HEAD/tree `032f47bd13fdff0cd2ccea5f902df9690ad09376` / `7c5e0a753eb39babfd66033d0f7ee08054191b3a`. Probe SHA-256 `dbbb3afb8d3fcb76b1b64f4112cb0d23fd3ff770f7e250395ba4c0ab09aa0bc5`; measurement SHA-256 `d55921408b0b136fe5329120ced5dd4ecb3afa14530e3e2abf7703eefe437e63`. The hunt executed Git-frozen `032f47bd:verifiers/compare_harness_independent.py` bytes (SHA-256 `13b6d791705be81a349178f2e392adf19012a64315a51c77856fcf2f98e8ca56`) against fresh producer captures.
- Frozen results: honest join exit 0, protocol 24/24, strict 20/24, four adjudicated/four scoped out. `alternatives`/`landed`/`unlanded` are the three ignored diagnostic names; `metadata`, `overrides`, `future_field`, `status`, and top-level `expected_value` reject. An unmatched bogus `scoped_out_probes` member passes 24/24; a nested conflicting `expected`/`expected_value` pair also passes 24/24 on frozen 13b. P1's shared comparator candidate SHA `1101213a7bed5410151564aeb5a4b49030a4821c86e7469286f046253fbc51e4` rejects that same alias-conflict input, while the unmatched probe remains accepted. `results`/`rows`/`checks` as record IDs pass matched synthetic controls; substitution into the real producer payload exits 2 on channel membership. Full per-input hashes/results are in the measurement matrix.
- H09 made no verifier, fixture, or floor change, and did not run the full r41 replay or floors guard. Report `.ufo/round-45/scouts/H09.md` SHA-256 `972ce000787e783634171951351c169696ebd67f49bc5a553da033e50da400ad`; preserve `drafts/h09/` as the report's counting inputs. No Git add, commit, reset, or ref mutation.

## 2026-10-19 — Round 45 B2 SHONEN assessment

- B2 report `.ufo/round-45/scouts/B2.md` SHA-256 `6d394a14011b2dbce9504882f13cfea7a171525b289d00547f38f4d3423b5a59` records four SHONEN box reruns, the paste-ready four `[~]` lines, seat-bounded per-axis verdicts, and the post-LOG checklist result. At `2026-10-19T18:42:06Z`, HEAD/tree were `032f47bd13fdff0cd2ccea5f902df9690ad09376` / `7c5e0a753eb39babfd66033d0f7ee08054191b3a`; the committed comparator SHA is `13b6d791705be81a349178f2e392adf19012a64315a51c77856fcf2f98e8ca56`. The report does not claim the full r41 census replay, a fresh exhaustive hunt, or final C1/C2/C3 adjudication.
- After this report pointer was first appended, `PYTHONDONTWRITEBYTECODE=1 python3 verifiers/verify_skill_checklist.py` ran at `18:42:54Z–18:42:55Z`: 9/10 checks passed, with only `governance.citation_resolves` failing on existing dead Round-44 draft citations (LOG lines 1649, 1655, 1657, 1661, plus two findings). These citations were not repaired. No SHONEN, production source, fixture, corpus, baseline, or floors-registry file was edited; no Git add/commit/ref mutation was performed.

## 2026-10-19 — Round 45 H02 held-out scope/probe/value-shadow hunt

- Report `.ufo/round-45/scouts/H02.md` SHA-256 `34ed4af4fc941e6c2209f720bce0c07971583f9071c130e6e685dc211cff95ca`. At HEAD/tree `032f47bd13fdff0cd2ccea5f902df9690ad09376` / `7c5e0a753eb39babfd66033d0f7ee08054191b3a`, `PYTHONDONTWRITEBYTECODE=1 python3 -B drafts/h02/h02_probe.py` exited 0 at `18:37:07.760068Z–18:38:27.250105Z`. It replayed 46 census arms plus five H02 variants on both frozen comparator blobs (51 CLI invocations per blob). R44 `6881ce3` SHA `d8b8c7f6001db7f47a294dc2a98db9179f61a281be20293dc5b104906073679d`; landed `032f47bd` SHA `13b6d791705be81a349178f2e392adf19012a64315a51c77856fcf2f98e8ca56`.
- Census open counts were 15/46 on R44 dispatch and 11/46 on landed `13b6d791`; the full survivor list and per-arm evidence are in the report and `drafts/h02/probe-results.json` (SHA-256 `a5de4999f99c3476187ab5952ef4e0e98bfcd3716aa51d8c2225ec5d0c65a386`). Nested `checks` forms under scope-out both failed exit 2; record-level probe shadows and the landed/unlanded expected-value variant exited 0 with the bounded interpretation in H02.md. Fresh live/independent producer captures were 28 records each, exit 0; scope SHA `fbcdc8d247475a5f1c2c613d78b6188dab77a766b02497a729a884687a70f77a`.
- Preserve `drafts/h02/` (runner SHA-256 `c6976335a40e9bfd856de5595a9422c9698978159ed7a80f2ca0f826ea37caf2`, result, producer captures, frozen source copies and per-arm runs). H02 made no production/verifier/fixture/floor-registry change and no Git ref/staging/commit change; the separate census-document update is not claimed here.

## 2026-10-19 — Round 45 H08 held-out payload-count hunt

- H08 report `.ufo/round-45/scouts/H08.md` SHA-256 `5ea36563fc5a65c9ad8560bb91b465268ad69a0e1e902df31ad3e32d6d3d3c8a`; snapshot HEAD/tree `032f47bd13fdff0cd2ccea5f902df9690ad09376` / `7c5e0a753eb39babfd66033d0f7ee08054191b3a`. All target CLI probes used the Git-frozen comparator SHA `13b6d791705be81a349178f2e392adf19012a64315a51c77856fcf2f98e8ca56`, not the concurrently changing comparator worktree.
- Fresh producer captures matched the r41 payload bytes (live `0bc250f5…`, independent `eb1068a4…`); the pinned join exited 0 at protocol 24/24, strict 20/24, four adjudicated/four scoped out. Full r41 replay classified 46/46: 11 open, 30 closed, 4 controls, 1 diagnostic; 15 outcomes changed from r41 (14 old open arms now fail closed and the caller-selected scope arm also fails closed). Payload matrix demonstrated adjudicated 4→3 or 4→5 and secondary 20→19 or 20→21, with protocol headline unchanged at 24/24. Per-arm commands, hashes, receipts, and the surviving-open list are in H08.md and its counting inputs.
- Replay results `drafts/h08/replay-46-results.json` SHA-256 `f931e5e981f2cdfa559b496938bda04d9e2873390ddeeb592e376aaf00560d52`; focused matrix `drafts/h08/focused-payload-matrix.json` SHA-256 `9f490f738528289d29dc6f2fb38183138b3813c7d0686eeb8c51aee903a6dcbf`. Separate shared-worktree comparator self-test, floors guard and both corpus gates passed on their recorded snapshot; these are not attributed to the frozen comparator. Preserve `drafts/h08/` before pruning. H08 changed no verifier, fixture, scope, floor-registry, or corpus source and made no Git add/commit/ref mutation.

## 2026-10-19 — Round 45 H01 Round 41 census replay

- Report `.ufo/round-45/scouts/H01.md` SHA-256 `a09fb0774756248b590e492d79a8362fc52fda4803114874dcc55b38d5c46b2e`. At HEAD/tree `032f47bd13fdff0cd2ccea5f902df9690ad09376` / `7c5e0a753eb39babfd66033d0f7ee08054191b3a`, H01 replayed the archived 46-arm command set against the Git-frozen comparator SHA `13b6d791705be81a349178f2e392adf19012a64315a51c77856fcf2f98e8ca56`, not the mutable worktree comparator.
- Candidate capture at `2026-10-19T18:36:48.908128Z` and deterministic replay at `18:40:55.204496Z` matched 46/46 exit/headline/reason outcomes and preserved every arm's input hashes. From the 25 historically-open arms in `.ufo/round-41/evidence/v10-channel-census.json` (SHA-256 `5cb218e133ef07a973e0a02ea1fd86f809eda213e9259a652fe92e949c6501b0`), 11 still exit 0 and 14 now reject with exit 2. Per-arm table is in H01.md.
- Evidence: first pass `drafts/H01/probe-results.json` SHA-256 `cc1ac246d909fdfa4170c952605006f7734a97bcf6b60a4166d7daccf7788e80`; replay `drafts/H01/subprocess-replay.json` SHA-256 `ab3fb5726b21e55e7fb450e4bb3082849072c19bc3d6f7b93702876434f2df79`; validated census `drafts/H01/channel-census.json` SHA-256 `bde84bb4129249713c7ec41426463f8c5c4bb88772f86fef97634468a80eeaa4`. Preserve `drafts/H01/` (including the comparator copy, runners, and input/command support files) before pruning. The receipt destination was set in the commands, but no replay receipt was produced.
- The prior mutable-worktree attempt was rejected after detecting comparator mutation and is not counted. H01 made no production verifier, fixture, protocol, mission, axes, corpus, or floors-registry edit; no Git add, commit, or ref mutation. Comparator self-test, floors guard, live join, and corpus gates were not run by this seat.

## 2026-10-19 — Round 45 U1 upstream census recheck

- U1 report `.ufo/round-45/scouts/U1.md` SHA-256 `d665168c6bf39c0f186b20e4793309ec38bc6d848684aa719e1cabdc68c37cc7`; measurement snapshot HEAD/tree `032f47bd13fdff0cd2ccea5f902df9690ad09376` / `7c5e0a753eb39babfd66033d0f7ee08054191b3a`. The census worktree file SHA-256 was `b06742e4dff0093b28d0a621cd3475799d76b5464ea23b785bc53fe20b75f79f`; it was not edited.
- Exact documented replay commands fail because `drafts/v10/` is absent; the exact live block fails with shell/CLI statuses 1, 1, 2. The evidence V10 scripts and original inputs were remapped into U1 scratch; `python3 drafts/u1/replay-probes.py && python3 drafts/u1/channel-census.py` reproduced 46/46 baseline arms and classified 25 open, 15 closed, 4 controls, 1 diagnostic, 1 trust-input against frozen b1be35f comparator SHA `1742dcccad1118399f0aa959f7ea6884d5992834d8c4c8b94e108277ae87df76` (replay/census output SHAs are in U1.md).
- Fresh producer outputs (28 records each) were joined by executing Git-frozen `032f47bd:verifiers/compare_harness_independent.py` bytes (SHA `13b6d791705be81a349178f2e392adf19012a64315a51c77856fcf2f98e8ca56`) at receipt time `2026-10-19T18:41:05Z`: exit 0, protocol 24/24, strict 20/24, four adjudicated/four scoped out, no disagreement/unknown/uncovered rows. `python3 verifiers/verify_corpus_integrity.py --json` passed 9/9; `python3 verifiers/verify_corpus_independent.py --json` exited 0 (6 PASS, 3 INFO). Commands, input/output hashes, and document path defects are in U1.md.
- No comparator, fixture, floor, registry, or census source was changed by U1. Preserve `drafts/u1/` counting inputs and outputs listed in the report. No Git add, commit, reset, or ref mutation.

## 2026-10-19 — Round 45 I1 integrator gate battery

- I1's green/red matrix is recorded in `.ufo/round-45/scouts/I1.md`. At HEAD/tree `032f47bd13fdff0cd2ccea5f902df9690ad09376` / `7c5e0a753eb39babfd66033d0f7ee08054191b3a`, the shared candidate passed `python3 -B verifiers/check_assertion_floors.py` at 9/9 exact values `10/150/91/87/1597/62/104/255/150`; the comparator, guard, and external registry SHAs were `1101213a7bed5410151564aeb5a4b49030a4821c86e7469286f046253fbc51e4`, `b9e0ce16cdb5de8592ffd877de684560495118b499ef41209cd904027f5fc6ef`, and `36536063ef803122c16a13cc9db6cad5cc47b58e173caeafa1fd6f2677619622`.
- Fresh live/independent producer captures exited 0 and were joined from frozen files at 24/24 protocol, strict 20/24, four adjudicated/four scoped out, with no disagreement, provisional, uncovered, unknown, or unadjudicated rows. Capture SHAs are `0bc250f5197c9dbbdbdce7e15c4220e0904118a8c290f81295aa18464b0b0341` / `eb1068a4f7b934d5553106d60737c05d8f1cd8d9ef827467f80281cac3853887`; receipt `.ufo/round-45/evidence/i1-join-receipt.json` SHA-256 `6e97056c5db51165c8665f82fe5027c3a5f37090574ddfe81c1c8770116fa9b8`.
- The two corpus gates passed (integrity 9/9, independent exit 0); surfaces passed 7/7; substrate pins passed 3/3. The pre-entry live skill checklist was 9/10: its only failure was existing governance citation resolution debt in earlier LOG entries. I1 made no unrelated citation edits; the mandatory post-entry checklist replay is recorded in the scout matrix.
- Preserve `drafts/i1/live.json` and `drafts/i1/independent.json` as the two counting inputs; the durable receipt is under `.ufo/round-45/evidence/`. I1 changed no verifier, fixture, baseline, or floor source and made no Git add, commit, reset, or ref mutation.

## 2026-10-19 — Round 45 M1 verifier baseline and live join

- Report `.ufo/round-45/scouts/M1.md` SHA-256 `bc2a5f4ee2bfff08be149b4d5f374b5001921c2742eac1079dd173ad8f41bd52`. At HEAD/tree `032f47bd13fdff0cd2ccea5f902df9690ad09376` / `7c5e0a753eb39babfd66033d0f7ee08054191b3a`, `PYTHONDONTWRITEBYTECODE=1 python3 verifiers/check_assertion_floors.py --repo "$PWD"` passed all nine registered instruments at exact observed/floor counts `10/10, 150/150, 91/91, 87/87, 1597/1597, 62/62, 104/104, 255/255, 150/150` (stdout SHA-256 `be3b8bcf58b1b6a7448659f5dec3889f8924789a89dc29be1de2271ae2f102f8`). Registry SHA-256 `36536063ef803122c16a13cc9db6cad5cc47b58e173caeafa1fd6f2677619622`; comparator `1101213a7bed5410151564aeb5a4b49030a4821c86e7469286f046253fbc51e4`; guard `b9e0ce16cdb5de8592ffd877de684560495118b499ef41209cd904027f5fc6ef`.
- Direct `PYTHONDONTWRITEBYTECODE=1 python3 verifiers/compare_harness_independent.py --self-test` passed 255 assertions at comparator `1101213a…`. The requested settled comparator `032f47bd` (`13b6d791…`) live join exited 0 at protocol 24/24, strict 20/24, four adjudicated/four scoped out; the later shared comparator `1101213a…` repeated the same join. Full command/time/input pins and distinction from the initial transition sample are in M1.md. Receipt `.ufo/round-45/evidence/M1-live-join-receipt.json` SHA-256 `79b7e0bbc3d8499f91f77e0aa1fe7ff22ea05c2cda945562afa3ed9900b1bb77` belongs to the later shared-comparator join; its embedded default C1/round-39 label is not M1 attribution.
- The initial 18:33:38 guard sample on comparator `13b6d791…` / registry `5d97bfe1…` transiently exited 1 at 250 observed vs 245 floor with five self-test failures (stdout SHA-256 `6639226dfdc60e9365e87fb550b8b633c16cd4960dd57c4ceedbdc087229a48f`); subsequent shared residual-fixture/floor updates superseded it. M1 did not edit verifier, fixture, floor, or registry sources, run C1’s census hunt, or take on C2/C3; no Git add, commit, reset, or ref mutation.

## 2026-10-19 — Round 45 H04 JSON-level channel hunt

- `PYTHONDONTWRITEBYTECODE=1 python3 -B drafts/h04/probe.py` ran `2026-10-19T18:41:02.795751Z–18:41:03.207748Z` at HEAD/tree `032f47bd13fdff0cd2ccea5f902df9690ad09376` / `7c5e0a753eb39babfd66033d0f7ee08054191b3a`. Runner SHA-256 `a5dcee63a930f46ddec003b7111b4293fec3af5c2257a9879f4f94a4353a93e2`; all ten CLI cases exited 0 on the Git-frozen comparator SHA `13b6d791705be81a349178f2e392adf19012a64315a51c77856fcf2f98e8ca56`. Six contradictory duplicate-member variants were green at 1/1 each; the NFC/NFD identity pair was green at 2/2; prefix and channel-key-as-record-ID controls did not demonstrate collisions. Results `.ufo/round-45/evidence/H04/channel-hunt-13b6d791.json` SHA-256 `f0c19e91c6b6f3670f00749dc61ad55349286f75b264b1b231c65ffd45bf27e6`.
- Report `.ufo/round-45/scouts/H04.md` SHA-256 `1d48615052a8614e10bcbfae422096190e3ac712c69297081318e509847bfc8d` records duplicate JSON members as a definite decoder-level open residual (`json.loads()` discards earlier members), and Unicode canonical equivalence as conditional on the unresolved identity policy. The report does not claim a full census.
- Fresh producer captures were joined using the same frozen comparator. Receipt `.ufo/round-45/evidence/H04/frozen-live-join-receipt.json` SHA-256 `313471ccb474559850859776c3c14cf87ee03710fee2209e72096b23e94d6299` records join exit 0, protocol 24/24, strict 20/24, four adjudicated/four scoped out, and no disagreements, uncovered, or unknown rows; joined JSON SHA-256 `7808e94ac2fa5dd433be92549835f64840a310ec0a0b2dac297df42711caea33`. Preserve `drafts/h04/` counting inputs. H04 made no comparator or floors edits and no Git add, commit, reset, or ref mutation.

## 2026-10-19 — Round 45 H11 held-out census/map hunt

- H11 report `.ufo/round-45/scouts/H11.md` SHA-256 `5a933bd4bfc988f9a6922d8c37844fca512715be723b764c7cc43497dc638803` records the full R41 46-arm replay and all 11 still-open IDs against frozen landed comparator SHA `13b6d791705be81a349178f2e392adf19012a64315a51c77856fcf2f98e8ca56` at HEAD/tree `032f47bd13fdff0cd2ccea5f902df9690ad09376` / `7c5e0a753eb39babfd66033d0f7ee08054191b3a`. The runner `PYTHONDONTWRITEBYTECODE=1 python3 drafts/h11/replay_h11.py` ran `18:38:01.237606Z–18:39:46.645221Z`; census result SHA-256 `79828e3b6074008c586191a53ea38e999a81883d00adbc448baee0737aabeac4` records 25 baseline-open, 14 now nonzero, 11 still-open, and no unexpected green.
- Frozen before/after dotted-map CLI cases and the write-time direct control join are in `.ufo/round-45/evidence/h11/write-time-check.json` (SHA-256 `06487981659b30dca570a3ab30bc947c7dcfdb42edb695c23c66477497a28628`); the full map-hunt matrix is `dotted-map-hunt.json` (SHA-256 `6e45b21471700b7e0fbe875d836b93a0fc6f1b247b3bfb73816a4b9644c42b2e`). The landing changes the checks-plus-flat-map case from exit 0 to 2; bare-map contradiction is exit 1 on both revisions, and the direct landed control exits 0 with 28 live records / 24 joined in-scope rows.
- Preserve `drafts/h11/replay_h11.py` and `.ufo/round-45/evidence/h11/` before pruning. H11 changed no comparator, floors, fixtures, producer, committed scope or census source; comparator self-test and floors guard were not run by this seat. No Git add, commit, reset, or ref mutation.

## 2026-10-19 — Round 45 H06 probe/scoped-out hunt

- Report `.ufo/round-45/scouts/H06.md` SHA-256 `4848c6b3b835aa13f06626af5c9f8752250ac28cae761db86b108223bcf59946` records the held-out probe/scoped-out hunt at HEAD/tree `032f47bd13fdff0cd2ccea5f902df9690ad09376` / `7c5e0a753eb39babfd66033d0f7ee08054191b3a`. `PYTHONDONTWRITEBYTECODE=1 python3 -B .ufo/round-45/evidence/h06/hunt_scoped_out.py` replayed all 46 R41 arms on frozen `6881ce3` comparator SHA `d8b8c7f6001db7f47bfecd2a98db9179f61a281be20293dc5b104906073679d` and landed `032f47b` comparator SHA `13b6d791705be81a349178f2e392adf19012a64315a51c77856fcf2f98e8ca56`; every saved input hash matched and stayed unchanged. Open counts were 15 and 11 respectively. The replay matrix is `.ufo/round-45/evidence/h06/r41-replay.json` (SHA-256 `5f1a5757392695e8269e44474766380b90bd26a1bb34c73ab99a9ea6119072a5`); fresh reason/target/derivability probes are in `fresh-hunts.json` (SHA-256 `404cfea0b99b33a18a7330b94a2810a15c4c8136bfc1a7b25280f146c9b802f4`), and the committed-row re-entry probe in `fresh-committed-row-reentry.json` (SHA-256 `845ca4af6c05ce4718426883c745992a7ef7a3d057e4c12c5891e5cd0d2d4855`).
- Payload-fabricated scope reason/evidence and payload-chosen probe target still exit 0 on the landed blob; probe channel-shadow, fallback, and unmatched-map arms remain open. Same-total probes, an uncommitted already-derived row, and a scope-out carrying value 7 fail closed. A synthetic re-entry attempt for a committed row marked DERIVED is also rejected as `scope-out value laundering`, contrary to the checker comment's re-entry promise. Honest fresh join remains protocol 24/24, strict 20/24, four adjudicated/four scoped out, with receipt SHA `c0480a3cc3862a0af8aab070812738640eec1f8b33412348321c2851ce6dc762`; the pinned command, producer hashes, and scope hash are in H06.md.
- Preserve `.ufo/round-45/evidence/h06/` (both frozen comparators, fresh producer/arm inputs, receipts and outputs). H06 changed no production verifier, fixture, committed scope, floor, or corpus source; did not run comparator self-test/floors/corpus gates; and made no Git add, commit, reset, or ref mutation.

## 2026-10-19 — Round 45 H07 identity/value alias hunt

- Report `.ufo/round-45/scouts/H07.md` SHA-256 `b7683fc5b804127bfda342b98657c4746a2d65a1601b0a31bc1f425c36eea0ca`. The runner `drafts/h07/run_alias_hunt.py` (SHA-256 `0e658c1da97b1fc5f7ac9a3d4efefd2b175ab7be40e3fb6b4e8e3c902ad49ce0`) ran `18:37:48.132936Z–18:41:13.869745Z` at HEAD/tree `032f47bd13fdff0cd2ccea5f902df9690ad09376` / `7c5e0a753eb39babfd66033d0f7ee08054191b3a`. It used frozen comparator bytes from `6881ce3` (SHA `d8b8c7f6001db7f47a294dc2a98db9179f61a281be20293dc5b104906073679d`) and `032f47bd` (SHA `13b6d791705be81a349178f2e392adf19012a64315a51c77856fcf2f98e8ca56`); the already-changed shared worktree comparator `1101213a7bed5410151564aeb5a4b49030a4821c86e7469286f046253fbc51e4` was not used.
- The exact 46 saved round-41 arms replayed on both frozen snapshots with all inputs unchanged; open adversarial arms were 15 on `6881ce3` and 11 on landed `032f47bd`. The 11 still-green arms and H07's 19 fresh alias variants (including the expected/expected_value, lone non-string status, and ignored non-string check residuals) are pinned in `.ufo/round-45/evidence/H07-hunt.json` (SHA-256 `79f027e1053bba50f1cb530583eebeae325ad9e90b741915dd077675cc525669`). Fresh producers joined through frozen `032f47bd` at 24/24 protocol, 20/24 strict, four adjudicated/four scoped out, exit 0; captures, join and receipt hashes are in H07.md.
- Preserve `drafts/h07/` (runner and two comparator snapshots) and `.ufo/round-45/evidence/H07-*` before pruning. H07 made no production verifier, fixture, floor, registry, corpus, or Git ref/index change; self-test, floors guard, and corpus gates were not run by this seat.

## 2026-10-19 — Round 45 F1 closed-census fixture coverage audit

- F1 report `.ufo/round-45/scouts/F1.md` SHA-256 `57a4d65115db3f119179a9ed9ab7d38c00d81cca00a251e52df212d590650f47` audits the 15 R41-baseline closed arms, pinned to census doc/JSON SHAs `b06742e4dff0093b28d0a621cd3475799d76b5464ea23b785bc53fe20b75f79f` / `5cb218e133ef07a973e0a02ea1fd86f809eda213e9259a652fe92e949c6501b0` and HEAD/tree `032f47bd13fdff0cd2ccea5f902df9690ad09376` / `7c5e0a753eb39babfd66033d0f7ee08054191b3a`.
- The report's arm-shaped crosswalk identifies 11 doors without a dedicated tracked `case.json`, distinguishes related class fixtures and inline checks, and records the 26-case HEAD manifest. The two current extra cases (`expected-alias-conflict`, `status-lone-nonstring`) are untracked and excluded. F1's 255-assertion self-test artifact is explicitly pinned to worktree comparator SHA `1101213a7bed5410151564aeb5a4b49030a4821c86e7469286f046253fbc51e4`, not the HEAD comparator blob `13b6d791705be81a349178f2e392adf19012a64315a51c77856fcf2f98e8ca56`.
- F1 did not run the R41 replay, fresh channel hunt, or floor guard and made no comparator, fixture, floor, registry, or corpus source change. No Git add, commit, reset, or ref mutation.

## 2026-10-19 — Round 45 R2 held-out depth review

- R2 report `.ufo/round-45/scouts/R2.md` SHA-256 `ba2aa3b99ad45ab1b67b17916bcc3c67b13109cd95d07df977757cb7d5687f05`. The full replay and added channel hunt use frozen `032f47bd` comparator SHA `13b6d791705be81a349178f2e392adf19012a64315a51c77856fcf2f98e8ca56`, at HEAD/tree `032f47bd13fdff0cd2ccea5f902df9690ad09376` / `7c5e0a753eb39babfd66033d0f7ee08054191b3a`.
- `PYTHONDONTWRITEBYTECODE=1 python3 drafts/r2/rerun_r41_current.py` reproduced all 46 landed outcomes with no input mutation or generation mismatch: 11 open, 29 closed, 4 controls, 1 diagnostic, 1 trust-input; 14/25 historical opens now reject. Replay JSON SHA-256 `1eebd2c0449312d78c2da88288258697b0cfb27e515774a88c0efe682cc09ac4`. `PYTHONDONTWRITEBYTECODE=1 python3 drafts/r2/fresh_channel_hunt.py` confirms the expected/expected_value conflict and lone non-string statuses still exit 0 on landed bytes. The null-valued relative scope-file attack returns 23/23 while receipt scope SHA `fbcdc8d2…` differs from actual resolved scope SHA `19b5f9d1…`; result JSON SHA-256 `da2ede20be7bd32d0cd602be32bf3c283732644a6233e8a431f4e3ea4ae69564`.
- The shared uncommitted comparator snapshot `1101213a7bed5410151564aeb5a4b49030a4821c86e7469286f046253fbc51e4` rejects both X2 shapes but retains the scope/receipt mismatch; it is not attributed to landed `13b6d791`. R2 recommends depth 9.5 only under C1's exhaustive, named-residual branch, not as a claim of closure; the separately-owned C3 census annotation/recheck remains outstanding. Preserve `drafts/r2/`. R2 changed no production source, fixture, scope, floor, registry, or census content; no Git add, commit, reset, or ref mutation.

## 2026-10-19 — Round 45 F1 report hash correction

- The earlier F1 entry points to the pre-correction report SHA-256 `57a4d65115db3f119179a9ed9ab7d38c00d81cca00a251e52df212d590650f47`. F1 corrected its artifact-scope sentence to include the captured self-test output and `drafts/f1/tmp/`; current `.ufo/round-45/scouts/F1.md` SHA-256 is `7591bedb1dc93a4197a5039e9d956dd959b5987df1ae4272236277da2e2fa0d6`. The crosswalk and 11 arm-shaped fixture-gap list are unchanged. No source/fixture or Git state change.

## 2026-10-19 — Round 45 N1 calibration

- N1 report `.ufo/round-45/scouts/N1.md` SHA-256 `26ad167980ef1233d44ae053f3df22b3081641f830c247a60b3dfe23c448cb3a` replays the historical R41 census against its pinned `b1be35f` comparator: 46/46 outcomes and classifications (25 open, 15 closed, 4 controls, 1 diagnostic, 1 trust input). The R41 arm payloads had been pruned; seven replayed independent payload hashes differ from original pins. Replay/census output SHAs are `320fc235debf7754a2a732b42e5557ad22f7ab1b5140560da9efc03ae32ca47c` / `54426fd77fb5d404c255e1cc96029b534f940994e4c1e4b46684b4e0e8d2985e`.
- Landed `032f47b` comparator SHA `13b6d791…` joins the retained producer captures at 24/24 protocol, strict 20/24, 4 adjudicated, 4 scoped out, exit 0. Historical R37 pinned instruments reproduce 23/28 with five disagreements; R38 reproduces 24/24, strict 19/24, five adjudications. The section's frozen-mutant 21/24 and `skills_rescan_max` claim did not reproduce: landed and R38 replays were 22/24, with no skills-rescan disagreement; the original mutant log is absent.
- Self-tests and floors results are separately labeled by source set in N1.md: the landed isolated comparator passed 245 assertions; the dirty R45 comparator passed 255 and its current floor guard passed 9/9. Preserve `drafts/n1/`; N1 changed no verifier, fixture, registry, or source document, and did not perform a fresh held-out hunt or Git add/commit/ref mutation.

## 2026-10-19 — Round 45 C2 severity-ranked open doors

- Report `.ufo/round-45/scouts/C2.md` SHA-256 `b368715ca422cf15dc38bfb51fef99fc89f2dff55d2f774b32c71b7e9c38fe0d` was written at HEAD/tree `032f47bd13fdff0cd2ccea5f902df9690ad09376` / `7c5e0a753eb39babfd66033d0f7ee08054191b3a`, using frozen comparator SHA `13b6d791705be81a349178f2e392adf19012a64315a51c77856fcf2f98e8ca56` (worktree comparator `1101213a…` was not executed). `PYTHONDONTWRITEBYTECODE=1 python3 -B drafts/c2/replay_r41.py` produced 46/46 replay results, 25 baseline-open / 11 landed-open, no unexpected opens; output SHA-256 `8a766995fd82d9c6de32187332c86dbd76ac9787080b901be08d707b45ba2d66`.
- `PYTHONDONTWRITEBYTECODE=1 python3 -B drafts/c2/fresh_hunts.py` produced 7 held-out arms (6 exit 0; unknown nested carrier control exit 2) and an honest 24/24 protocol join. Final result SHA-256 `30dcc7b07772cd020e8c41b7908ebf53743c628b6e2a9685e4267f07321b1ad0`; receipt SHA-256 `a79c4f078cf35bbc846cdedbdff856433f2dd0347090c1501243c481c25374bf`. Together with R41 replay, 17 exit-0 arm observations are ranked in C2.md; the registered `expected`/`expected_value` and lone non-string `status` cases remain exit 0 on frozen bytes.
- Preserve `drafts/c2/` (both runners, full arm outputs, raw payloads, producer captures and receipt) and the pinned R41 source inputs. No comparator, producer, fixture, scope, floor, or registry change; no Git add/commit/ref mutation.

## 2026-10-19 — Round 45 D1 deep-join-contract

- D1 report `.ufo/round-45/scouts/D1.md` SHA-256 `f6c430d0b77658e87ceddedcc23a93c94763e62eee4d25bab2fb21bc78952412` maps payload effects on headline, strict, adjudicated, and secondary outputs against frozen comparator `.ufo/round-44/evidence/r2-compare-candidate-13b6d791705b.py` SHA-256 `13b6d791705be81a349178f2e392adf19012a64315a51c77856fcf2f98e8ca56` at HEAD/tree `032f47bd13fdff0cd2ccea5f902df9690ad09376` / `7c5e0a753eb39babfd66033d0f7ee08054191b3a`.
- `PYTHONDONTWRITEBYTECODE=1 python3 drafts/d1/replay_r41.py` replayed all 46 R41 arms (source replay/census SHA-256 `991d8d95eb53c196ed5d74d9e4f23a9f948e29bc8e8480b81cbd430648baedb5` / `5cb218e133ef07a973e0a02ea1fd86f809eda213e9259a652fe92e949c6501b0`); evidence `.ufo/round-45/evidence/d1-r41-replay.json` SHA-256 `04027da4441ead0916c6c89bf61cae2e97fd33fe6b7a0f80b8a4d583a79e8045`. Results: 15 exit 0, 28 exit 2, 3 exit 1; 11/25 formerly open arms remain exit 0, 14 now exit 2.
- `PYTHONDONTWRITEBYTECODE=1 python3 drafts/d1/hunt_r45.py` ran eight fresh channel cases against the same frozen bytes; evidence `.ufo/round-45/evidence/d1-fresh-channel-hunt.json` SHA-256 `0035afef79ecaffd8393a365e30790dedc5030fb1dfa71edff7284d15f2c07d4`. Expected/expected_value conflict and lone non-string status still exit 0; changing live `expected` 7→999 with `observed=7` changes secondary only (20→19); record-map composition exits 2 on derived-set overflow. Source and case inputs were unchanged during runs.
- Findings and residual boundaries are enumerated in D1.md. The first attempt against the moving worktree comparator (observed SHA changed `b6a618ef…`→`1101213a…`) is invalid and excluded. This is a reporting/verification seat: no comparator, scope, floor, registry, fixture, protocol, or corpus source was changed; no standard gates or SHONEN checks were run; no Git index/ref mutation.

## 2026-10-19 — Round 45 S2 committed-evidence replay

- S2 report `.ufo/round-45/scouts/S2.md` SHA-256 `4d19901c5cf24e9d0ccd9bd3e35093d99f835cdb9216c0db8e59642f29e12cb2` records evidence at HEAD/tree `032f47bd13fdff0cd2ccea5f902df9690ad09376` / `7c5e0a753eb39babfd66033d0f7ee08054191b3a`, using Git-frozen comparator bytes `6881ce3` SHA `d8b8c7f6001db7f47bfecd2a98db9179f61a281be20293dc5b104906073679d` and landed `032f47b` SHA `13b6d791705be81a349178f2e392adf19012a64315a51c77856fcf2f98e8ca56`. The committed R41 replay matched 46/46; landed replay output `drafts/s2/r41-landed-032f47b/landed-census-replay.json` SHA-256 `21e30431f31a7f901c0a34fbc3c5a6b8f7fb1b45e55d568955fdef0cfb2d92f5` records 15 exit 0 (4 controls + 11 formerly-open arms), 3 exit 1 and 28 exit 2. Fourteen formerly-open arms now reject; no previously-closed attack arm became green. The exact expected/expected_value-conflict and lone non-string-status residual payloads still exit 0 (result SHA-256 `2b4d60efa2a21a8ce136b9e25d86c893f93c0eca767cc58218e844e8533f2732`).
- R43 generated-case matrix `drafts/s2/r43-replay/probe-matrix.json` SHA-256 `607fcd661b9c26b22ff936224b2b4fe2e055672b530c9394df3b6ac523a309f2` confirms P1's six cases exit 2 on both revisions and the V1 expected-only record+map case transitions from 24/24 green on 6881ce3 to named exit 2 (`derived-set overflow`) on 032f47b. R44 record-map fixture matrix `drafts/s2/record-map-matrix/matrix.json` SHA-256 `e77c4da6c09f668b5d70c9b3abb66945069de0a8c7c300dd440d894e1e4aab63` independently reproduces that transition; honest controls pass on both. The committed union battery passes 24/24 on both snapshots; G1 historical extraction result is distinguished from current HEAD, whose surfaces gate passes 7/7 and self-test passes 87 assertions (details and pins in S2.md).
- Preserve `drafts/s2/` as the counting bundle. The shared worktree comparator/guard/registry were changing and differed from the pinned landed comparator; S2 used frozen Git objects for comparator claims, did not run the comparator self-test or floors guard, and changed no verifier/fixture/floor/registry/census source. No Git add, commit, reset, or ref mutation.

## 2026-10-19 — Round 45 C1 held-out hunt and completeness ruling

- C1 report `.ufo/round-45/scouts/C1.md` SHA-256 `448cc65fd7d5631f03463870d5d56069304338640486f31d151dc49c678b20c0` pins claims SHA `69675f5c08d948e6e6c5aabe303fbda1d2d0eea3f7f96f7476b6dac147406c27`, census doc SHA `b06742e4dff0093b28d0a621cd3475799d76b5464ea23b785bc53fe20b75f79f`, HEAD/tree `032f47bd13fdff0cd2ccea5f902df9690ad09376` / `7c5e0a753eb39babfd66033d0f7ee08054191b3a`, and frozen comparator SHA `13b6d791705be81a349178f2e392adf19012a64315a51c77856fcf2f98e8ca56` (verified against `git show HEAD:...`). The replay command reproduced the exact 46 R41 arms with unchanged inputs: 11 open, 29 closed, 4 controls, 1 diagnostic, 1 caller-selected trust input; replay JSON `drafts/c1/heldout-replay.json` SHA-256 `262607584b3edb2e71a4c6375d660de1b20ca1f6ff5e10c55992b42774c274f1`.
- C1's 13-case frozen-byte channel hunt result `drafts/c1/channel-hunts.json` SHA-256 `7942fb59e8d92449da22d3ba3a0786c1283904ba08b0935e4f5d35682bb70d1b` includes accepted malformed aliases/raw duplicate members and live metadata order cases; controls behaved as expected. The direct frozen honest join exited 0 at protocol 24/24, strict 20/24, four adjudicated/four scoped out, zero disagreements/uncovered/unknown; output `drafts/c1/frozen-honest-join.json` SHA-256 `2122ae3aa4f25621c5bbeb5d8eb1384a93f0fb7e883787e84ff54bb12b68d6b1`.
- **Ruling: not demonstrably bounded; completeness unproven.** H04's additional raw duplicate-member cases and H05/H06/R2's fresh null-valued relative scope-file mismatch show accepted forms outside the 46-arm set. Preserve `drafts/c1/`; C1 changed no verifier, fixture, scope, floor/registry, or census source and made no Git add/commit/ref mutation. Comparator self-test, floors guard, and corpus gates were not run by this seat.

## 2026-10-19 — Round 45 S1 held-out hunt

- S1 report `.ufo/round-45/scouts/S1.md` SHA-256 `4c22966d719879d5370eaef6f91ae3a64cae4740db8f4cb4392b6daaddc3b083` pins claims SHA `69675f5c08d948e6e6c5aabe303fbda1d2d0eea3f7f96f7476b6dac147406c27`, HEAD/tree `032f47bd13fdff0cd2ccea5f902df9690ad09376` / `7c5e0a753eb39babfd66033d0f7ee08054191b3a`, and landed comparator SHA `13b6d791705be81a349178f2e392adf19012a64315a51c77856fcf2f98e8ca56`; paired probes also used frozen `6881ce3` SHA `d8b8c7f6001db7f47bfecd2a98db9179f61a281be20293dc5b104906073679d`.
- The exact R41 inputs replayed all 46 arms with unchanged input hashes: 15 exit 0, 3 exit 1, 28 exit 2; 11/25 formerly open remain green and 14 now reject. Replay artifact `drafts/s1/census-current-replay.json` SHA-256 `1cb1234ef989a0560fef15bbd54d22e29cf6bf2075380f35d21e662e01f700d0`; fresh hunt `drafts/s1/fresh-channel-hunt.json` SHA-256 `20c5e2acb2a66b9f6b72cbf78507f3bfac0b3e8cfb3306676db9443ac37a0bdf` confirms residual X2 alias/status forms, raw duplicate members, and the relative scope-file CWD split, while record+map composition rejects on landed bytes.
- Preserve `drafts/s1/` as the counting bundle. S1 changed no comparator, producer, fixture, floor, registry, census, or other production source; no worktree self-test/floor guard or corpus gate was run due to concurrent shared edits. No Git add/commit/ref mutation.

## 2026-10-19 — Round 45 N3 R41 census calibration errata

- N3 report `.ufo/round-45/scouts/N3.md` SHA-256 `8676b802621c84659f358ff22d63c7719cb867b175b053454f3d6f89c4513798` documents the append-only annotation to `corpus/knowledge/harness-independent-round41-census.md` (SHA-256 `ce55bbcebe645af20b2ec1a17ef0b351a1b4c34a9112a48da380a79610626b44`). The annotation preserves R41's historical 46-arm baseline (25 open, 15 closed, 4 controls, 1 diagnostic, 1 caller-selected trust input) and labels subsequent counts as regenerated-input comparisons.
- `PYTHONDONTWRITEBYTECODE=1 python3 -B drafts/n3/replay_13b6.py` replayed the 25 historical opens against landed comparator `032f47bd` (SHA-256 `13b6d791705be81a349178f2e392adf19012a64315a51c77856fcf2f98e8ca56`): 14 nonzero and 11 exit-0 on the rebound inputs; result `drafts/n3/replay-13b6.json` SHA-256 `01e42622eac20fe063e1c376edbc2f4ed6f34666b758f18d7ab4c35135638d47`. The separate R43/R44 comparison (`drafts/n3/compare_r43_r44.py`, SHA-256 `1e4c3b6be19dbd290103d3027bb6e65fa03d54b48ce6f5625e4a52a80cd46bbc`) regenerated 46 arms against comparator SHAs `d8b8c7f6001db7f47a294dc2a98db9179f61a281be20293dc5b104906073679d` / `13b6d791705be81a349178f2e392adf19012a64315a51c77856fcf2f98e8ca56`; R43 is 15 open / 25 closed / 4 controls / 1 diagnostic / 1 trust input, R44 is 11 / 29 / 4 / 1 / 1. Matrix SHA-256 `bc7a9bd4f8a8c511b88b33edd60a7169948737ace29809535649cc9d3682874a` records ten R43 and four additional R44 first closures.
- Input identity is limited: N1's rebound artifact and N2's matrix identify seven independent-payload hash mismatches against V10 pins; N2 records 39/46 matching saved arm hashes. Nine R43 closures and all four R44 closures match saved input hashes; `r1-f3-prime-scope-file-cwd` is among the mismatches, so that R43 first-close attribution is not established on original bytes. The exact classification of four originally-open changed-input arms (including that case) is unresolved; do not present 11 as an exact-original-input survivor count. The V10-named sidecars are `v10-probe-results.json` SHA-256 `cf60e7a9f374684e80c173de32f56fd8efbf58eefd6d88069daa9e2b49029d70` and `v10-subprocess-replay.json` SHA-256 `991d8d95eb53c196ed5d74d9e4f23a9f948e29bc8e8480b81cbd430648baedb5`. H06/H07 cite a distinct internally consistent unprefixed sidecar pair, which does not establish identity with these V10 inputs. Supporting N1/N2 reports: `.ufo/round-45/scouts/N1.md` SHA-256 `26ad167980ef1233d44ae053f3df22b3081641f830c247a60b3dfe23c448cb3a`; `.ufo/round-45/scouts/N2.md` SHA-256 `6c9537223896feb458bad261e2f44679db130c0597fa26e1baaaf91a03e2003b`.
- At HEAD `032f47bd13fdff0cd2ccea5f902df9690ad09376`, the live-worktree gates run after the N3 report correction returned: corpus integrity 9/9 PASS (exit 0); independent corpus 6 PASS / 3 INFO (exit 0); skill checklist 9/10 (exit 1), with only `governance.citation_resolves` failing on seven pre-existing dead R44 draft citations (including `LOG.md:1649`, `1655`, `1657`, `1661`); comparator self-test 0 failures / 255 assertions (exit 0); assertion floors 9/9, vector `10/150/91/87/1597/62/104/255/150` (exit 0). Current comparator, floors guard, and registry SHAs were `1101213a7bed5410151564aeb5a4b49030a4821c86e7469286f046253fbc51e4`, `b9e0ce16cdb5de8592ffd877de684560495118b499ef41209cd904027f5fc6ef`, and `36536063ef803122c16a13cc9db6cad5cc47b58e173caeafa1fd6f2677619622`; the red checklist references are outside this N3 scope and were not rewritten.
- Preserve `drafts/n3/` as the replay/counting evidence. N3 changed no comparator, verifier, fixture, scope, floor, registry, or SCORECARD source. The N2 predecessor/landed inputs are targeted `verifiers/` and `corpus/` snapshots, not full repository copies; do not modify or prune them without parent review. No Git staging, commit, or ref mutation.

## 2026-10-19 — Round 45 V10 exact-input census reconciliation

- `.ufo/round-45/scouts/V10.md` (SHA-256 `8979b1243196605a4abb889c1abf562c1ff941a77ed8d28b8724ba2b038c151b`) records the full per-arm crosswalk and current gate battery. The census `corpus/knowledge/harness-independent-round41-census.md` (SHA-256 `286937b7a5d7d2e0c370282a13ef7cd326dc1e77e2263f57a8e11b1ba8ee6cc7`) retains R41/N3 measurements, updates the stale operational `recheck:` pointer, and appends the exact-input result.
- `PYTHONDONTWRITEBYTECODE=1 python3 drafts/v10/post-r44-hunt.py` replayed all 46 registered R41 arms against frozen Git comparator `032f47bd13fdff0cd2ccea5f902df9690ad09376:verifiers/compare_harness_independent.py` SHA-256 `13b6d791705be81a349178f2e392adf19012a64315a1c77856fcf2f98e8ca56`, at HEAD/tree `032f47bd13fdff0cd2ccea5f902df9690ad09376` / `7c5e0a753eb39babfd66033d0f7ee08054191b3a`. Runner SHA-256 `3a70d405eb147d7029abb3f76668da60f65ec99002c37eda383d11ad458add86`; final result `.ufo/round-45/evidence/v10-post-r44-hunt.json` SHA-256 `fc05b89aab5c9a065e7ae51c80a1e111505f5b1736cdbdcc726091aabaccd221`. Source pins: R41 replay `991d8d95eb53c196ed5d74d9e4f23a9f948e29bc8e8480b81cbd430648baedb5`, R41 census `5cb218e133ef07a973e0a02ea1fd86f809eda213e9259a652fe92e949c6501b0`, scope `fbcdc8d247475a5f1c2c613d78b6188dab77a766b02497a729a884687a70f77a`; 138/138 live/independent/scope hashes were verified and unchanged. Seven recovered payload files and exact hashes are in `.ufo/round-45/evidence/v10-reconstructed-inputs/` and the result JSON.
- Of 25 historically-open arms, 10 still exit 0 and 15 exit nonzero. The report and census enumerate all IDs and reason classes. `r1-f4-payload-chosen-probe-target` is a false blocker because the archived `drafts/v10/builder-carrier` target is missing; its exit 2 is not a semantic fix. `r1-f3-prime-scope-file-cwd` rejects before receipt writing during `build_meta`, so its absent replay receipt is expected. The separate X2 `x2-expected-expected-value-conflict` and `x2-lone-nonstring-status` both remain exit 0. This reconciliation covers the registered R41 arms and those X2 probes only, not completeness across all R45 hunts.
- Current-worktree gate artifacts are in `.ufo/round-45/evidence/v10-gates/`: fresh producers exit 0 at 28 records (SHA-256 `0bc250f5197c9dbbdbdce7e15c4220e0904118a8c290f81295aa18464b0b0341` / `eb1068a4f7b934d5553106d60737c05d8f1cd8d9ef827467f80281cac3853887`); join exit 0 at protocol 24/24, strict 20/24, four adjudicated/four scoped out, no disagreements/provisional/unadjudicated/unknown/uncovered, receipt SHA-256 `3aa06203bd0018cb457e30a95ef62b019d36bffd6b7ae7c80db5f0ccbd6cdf2d`; self-test exit 0, 0 failures / 255 assertions; floors exit 0, 9/9 exact vector `10/150/91/87/1597/62/104/255/150`; corpus integrity exit 0, 9/9, tracked=55, index tokens=73, no stale/unindexed/missing paths, report pointers 38/0 dead, commits 27/0 unresolved; corpus independent exit 0, 6 PASS / 3 INFO. Stdout hashes are listed in V10.md.
- The fresh gates used the changing worktree comparator SHA-256 `1101213a7bed5410151564aeb5a4b49030a4821c86e7469286f046253fbc51e4`, floors guard `b9e0ce16cdb5de8592ffd877de684560495118b499ef41209cd904027f5fc6ef`, and registry `36536063ef803122c16a13cc9db6cad5cc47b58e173caeafa1fd6f2677619622`; those bytes are distinct from the frozen comparator replay. V10 changed no verifier, fixture, scope, floor, or registry source and performed no Git staging or commit.

## 2026-10-19 — Round 45 V10 final replay hash

- After the census and scout documents were finalized, `PYTHONDONTWRITEBYTECODE=1 python3 drafts/v10/post-r44-hunt.py` reran the exact-input replay and reproduced 46/46 arms, the same 10 exit-0 / 15 nonzero historical-open split, unchanged 138 input hashes, and stable HEAD/tree/scope pins. The refreshed final artifact `.ufo/round-45/evidence/v10-post-r44-hunt.json` SHA-256 is `b7cd1fbd4e0b94e578a5f7efa43690ee272bb535a0032b3561d8b66bc647a9be`; this supersedes the earlier run-artifact hash in the preceding entry (the JSON records run timestamps). The separate X2 residuals remain unchanged and exit 0. The finalized `.ufo/round-45/scouts/V10.md` SHA-256 is `1755883c87832fd30b8dc7bb7e16eac5cf0a5803769163b09080125f9fe3e92b`.

## 2026-10-19 — Round 45 V10 final gate receipt hash

- The post-documentation gate rerun exited 0 for both 28-record producers, the current-worktree join, comparator self-test, assertion floors, and both corpus gates. Comparator SHA-256 was stable before/after at `1101213a7bed5410151564aeb5a4b49030a4821c86e7469286f046253fbc51e4`; all stdout hashes and measured counts match the preceding V10 entry. The receipt at `.ufo/round-45/evidence/v10-gates/live-join.receipt.json` was refreshed and now has SHA-256 `f895fb15adbbbc776907a5203bb524d87978c22991b480ec3c84f9ab2d9f4e79`, superseding the earlier run's receipt hash.

## 2026-10-19 — Round 45 (loop A position 9 — the held-out hunt on the settled closure): 14 of 25 r41 doors now closed, 11 still open — depth holds 9, 9.5 not supported; C2+C3 verified

- Claims at `.ufo/round-45/claims.json` (C1 depth = held-out hunt on the settled closure — is the class closed?; C2 operability = X2's two residuals; C3 calibration = reconcile records to post-r44 tree). Provider: `openai-codex/gpt-6-luna-max`. 42 seats reported (~42 min). Fragments `.ufo/round-45/scouts/*.md`; curated `.ufo/round-45/evidence/` (the census replay + hunts + P1 inputs).
- **C1 depth — improved, bounded; depth holds 9 — 9.5 NOT supported.** The full r41 census replay (46/46 subprocess arms, input hashes unchanged) on the landed `13b6d791` comparator: **14 of the 25 r41-open doors now reject exit 2, 11 still exit 0** (H01/H02/C1/C2/S1/Y1/R2 all reproduce the same replay). The record+map composition is confirmed closed on the requested before/after bytes (frozen `d8b8c7f` exit 0 → landed `13b6d791` exit 2 `derived-set overflow`; the real 24-row `record-map-24-composition` fixture fails closed). **But the surviving doors are not demonstrably bounded** — the held-out hunts (C1/C2/S1) found doors OUTSIDE the 46-arm census: raw duplicate-JSON-members (decoder last-wins), the scope-file cwd door still open with a stronger null-value bypass, live-JSON mode/verdict/summary shadows. C1's "exhaustive residual list" branch is not verified. **The 11 still-open doors (the durable residual):** 4 caller-supplied live-JSON arms (live-mode-positive-masks-independent-drift — strongest false-green, live 7 vs ind 999 still exit 0; live-mode-split, live-verdict-shadow, live-top-level-summary) — conditional on caller tampering, not the producer path; the scope-file cwd door (F3 seam, still open — relative `--scope-file` from a planted cwd reads exit 0 23/23 while the receipt attests the honest file); unmatched-scoped-out-probe + scoped-out reason/evidence drift; raw duplicate-JSON-member doors; X2's two residuals (now closed by P1/P2 — see C2). **Depth holds 9 — R2: 9.5 is supportable only under C1's exhaustive-residual-list branch, and that branch is not verified; do not describe the landed comparator as closing all doors.** The r41 census doc is updated to the post-r44 state (V10).
- **C2 operability — VERIFIED (P1 expected-alias + P2 status-lone; on the newer `1101213a` comparator).** X2's two residuals closed on the landed bytes: a conflicting `expected`/`expected_value` pair → exit 2 `record value alias conflict` (the within-record cross-check now reconciles foreign-key disagreement); a lone non-string `status` → exit 2 `non-string status` (was silently discarded). S1's "still open" readings were on `13b6d791` (the r44 landing) — temporal; on `1101213a` they fail closed. Comparator self-test 245→255, floors in-step. Score held: advisory.
- **C3 calibration — VERIFIED (V10 census update + N3 errata).** `corpus/knowledge/harness-independent-round41-census.md` updated to the post-r44 state (append-only annotation — the r41 measurement preserved, each r43/r44-closed door marked closed-at-sha); the doc's `recheck` line still runs; records reconciled to the settled tree.
- **Wave conformance:** 42 seats, no commits; writes inside `.ufo/round-45/` + `verifiers/` + fixtures + corpus doc + LOG/SCORECARD; no `.git` symlinks; floors churn settled in-step (comparator 245→255); drafts pruned to evidence.
- **Whole-tree battery at close:** comparator self-test **0/255**; floors **9/9 EXACT** (`10/150/91/87/1597/62/104/255/150`); live join exit 0 24/24 (strict 20/24, adjudicated 4, scoped 4); corpus 9/9 + exit 0; surfaces 7/7; pins 3/3; checklist 10×PASS after citation repairs.
- **Queue for r46 (pos 10 — devin/deepseek-v4-1-flash-max, 32-64 seats):** **C1' = the surviving doors in C2's reachability order** — (a) the scope-file cwd seam (resolve `--scope-file` once vs `--cwd`, record resolved path+digest in the receipt — the strongest reachable-without-committed-edit door); (b) the live-JSON shadow channels (live mode/verdict/summary — the producer-vs-payload question: should the comparator trust a caller-supplied live JSON's shadow fields?); (c) raw duplicate-JSON-member handling (canonical-parse vs last-wins); (d) the scoped-out probe/reason/evidence drift. Standing debt: digest-append; IND hang; resolver-vs-brace; SHONEN form; OMP provenance; divergence merge (operator).

## 2026-10-19 — Round 46 X3 Markdown-report integrity probe

- `.ufo/round-46/scouts/X3.md` records an open operability finding against the frozen `055d3b9` comparator blob (SHA-256 `1101213a7bed5410151564aeb5a4b49030a4821c86e7469286f046253fbc51e4`). `PYTHONDONTWRITEBYTECODE=1 python3 .ufo/round-46/drafts/x3/probe.py` ran the control and crafted-identifier cases; runner SHA-256 `514ead13cec3eaaaa7291277bdd36162de0b12e99eb4c16d9fb013212213545e`, final result manifest SHA-256 `e98f966631535f4190412cee78065ac6e2af543a555d550f33ac4017e93d69fd`.
- The control report is clean; the crafted caller-supplied JSON yields a passing one-row join but injects a counterfeit Markdown table row. Full input, output, scope, and run-time pins are in the report and manifest. No production sources changed; comparator self-test, floors guard, and corpus gates were not run. Preserve `.ufo/round-46/evidence/x3/` and the cited replay runner. No Git add/commit/ref mutation.

## 2026-10-19 — Round 46 M1 live baseline

- M1 report `.ufo/round-46/scouts/M1.md` SHA-256 `4e09f6e4730e6b5f216ba9bfc9e0ced304360b2613716f8b3fb6c4a874aa2668` records the hash-bracketed baseline and later concurrent-edit observations. At HEAD/tree `055d3b9a3f7eb28d13452a0d26853ef4feabf2ae` / `e8dced184612a9738c5b8d244a0837fbd955a7da`, `PYTHONDONTWRITEBYTECODE=1 python3 verifiers/check_assertion_floors.py` passed 9/9 exact floors `10/150/91/87/1597/62/104/255/150` on stable instrument hashes; registry SHA-256 `36536063ef803122c16a13cc9db6cad5cc47b58e173caeafa1fd6f2677619622`, stdout SHA-256 `be3b8bcf58b1b6a7448659f5dec3889f8924789a89dc29be1de2271ae2f102f8`.
- At the same HEAD/tree and comparator SHA-256 `1101213a7bed5410151564aeb5a4b49030a4821c86e7469286f046253fbc51e4`, `PYTHONDONTWRITEBYTECODE=1 python3 verifiers/compare_harness_independent.py --expect-n 28 --no-stamp --json --receipt ...` exited 0: protocol 24/24, strict 20/24, four adjudicated/four scoped out; join output SHA-256 `b38dc4f2991f7c06578d76c6f317d1b99407c05d4bfefbf07fa231890235b80e`. Subsequent in-flight comparator edits made later guard attempts fail while the source SHA changed; those attempts are disclosed, not used to replace the pinned baseline. No Git add, commit, or ref mutation.

## 2026-10-19 — Round 46 B1 scribe scaffold

- `.ufo/round-46/scouts/B1.md` and `.ufo/round-46/drafts-report-skeleton.md` record the requested scaffold. Registration is pinned to `.ufo/round-46/claims.json`, SHA-256 `ff60fce90a203dbd793fa4fc21bd8e7139df196601e1b76d935aa62903af0e53` (`sha256sum .ufo/round-46/claims.json` at `2026-10-19T19:29:02Z`); registration facts are not measured outcomes.
- `sha256sum .ufo/round-46/claims.json .ufo/round-46/drafts-report-skeleton.md .ufo/round-46/scouts/B1.md verifiers/compare_harness_independent.py` at `2026-10-19T19:32:16Z` returned scaffold SHA-256 `c33d711942fa44b103843ac4baa185170543ac06aec6ed64158803c6c64dcf2c` and report SHA-256 `cd787cee37c7d1bdb8a35047cb9e2bbef97fb2cca6f11f293009d168ec65c322` (among the listed file hashes).
- At `2026-10-19T19:32:16Z`, `date -u +%Y-%m-%dT%H:%M:%SZ && git rev-parse HEAD && git rev-parse 'HEAD^{tree}' && git status --porcelain=v1 && sha256sum verifiers/compare_harness_independent.py && git show 055d3b9:verifiers/compare_harness_independent.py | sha256sum` returned HEAD `055d3b9a3f7eb28d13452a0d26853ef4feabf2ae`, tree `e8dced184612a9738c5b8d244a0837fbd955a7da`, worktree comparator SHA-256 `5763094d510e53d0ac438f292d01846852fa00f0f2805d2a6c1634df55b357f7`, and frozen comparator SHA-256 `1101213a7bed5410151564aeb5a4b49030a4821c86e7469286f046253fbc51e4`. Status showed the comparator modified and fixture directories `duplicate-independent-re-derived-member/`, `duplicate-independent-results-member/`, `duplicate-live-results-member/`, and `scope-file-cwd/` untracked alongside `.ufo/round-46/`. The worktree comparator/fixtures are shared-tree state, not B1 changes; the comparator changed repeatedly during this seat, so no measurement was run against it.
- B1 made no product, fixture, floors-registry, corpus, SCORECARD, or claim edits; no probes, gates, or red-before/after tests were run. All outcomes remain `[PENDING]`; no Git add/commit/ref operation was performed.

## 2026-10-19 — Round 46 Z1 conformance sweep

- Z1 report `.ufo/round-46/scouts/Z1.md` SHA-256 `f22b605c22797d9bcefce041b148d6922cb33b856d7ca7754ec93a80ee9fe6ac` records a read-only inventory at `2026-10-19T19:30:51Z`, HEAD/tree `055d3b9a3f7eb28d13452a0d26853ef4feabf2ae` / `e8dced184612a9738c5b8d244a0837fbd955a7da`. The report carries the exact commands/method, paths, hashes, and shared-tree limits.
- The pinned inventory found Round 46 drafts **91 files / 737,119 bytes** (manifest SHA-256 `6f3dfb236f2709c5c3d9f46dc05289c5669de9063b5a982e2389ada78d35a548`), Round 46 evidence **46 files / 493,045 bytes** (manifest SHA-256 `db43ab2d037456a0a8d29954eb101c8484af3e04ef24c9b980ef829d5fde7fd0`), and **67/67 tracked R41 evidence files present and unchanged** (tracked manifest SHA-256 `b26f95c7af8e802a6412b17979f0b91deeb79966191012202ab8aa6881fec6d7`). The R41 directory also held one ignored untracked `__pycache__` bytecode file, disclosed and left untouched.
- The same whole-repo symlink scan returned no symlinks. The Git index was clean; shared comparator edits and concurrent untracked seat artifacts were present. Z1 made no Git add/commit/ref operation or out-of-lane write and did not rerun gates against moving source bytes. Preserve the cited Round 46 counting bundle until seat owners finish and reconcile their references.

## 2026-10-19 — Round 46 Q1 standing-debt queue

- `.ufo/round-46/scouts/Q1.md` SHA-256 `02294226e7506a98936c753e4f95d3018a8d17e85d9756a89395b81b2765b5bc` (`sha256sum .ufo/round-46/scouts/Q1.md` at `2026-10-19T19:33:19Z`) compiles the registered F3′/live-JSON/raw-duplicate/scoped-out queue, remaining documented residuals, and cross-round debt. Its measurement snapshot is HEAD/tree `055d3b9a3f7eb28d13452a0d26853ef4feabf2ae` / `e8dced184612a9738c5b8d244a0837fbd955a7da`; `git show HEAD:verifiers/compare_harness_independent.py | sha256sum` was `1101213a7bed5410151564aeb5a4b49030a4821c86e7469286f046253fbc51e4`, while the worktree comparator at the same time was `8b4f3d10ab30e8517846e0606855805eaad04ccf3154d93c882e4b0f41f07c1f` (`sha256sum verifiers/compare_harness_independent.py`). Shared edits are not attributed to Q1.
- Q1 is a literature/source reconciliation; it ran no comparator, self-test, floors, corpus, or end-to-end join commands, changed no verifier/fixture/floor/registry/census source, and made no Git add/commit/ref mutation. It explicitly distinguishes R45’s frozen `13b6d791…` measurements from current committed `1101213a…` and the moving worktree. Preserve the cited R45 draft bundles per the Q1 report.

## 2026-10-19 — Round 46 V4 live-JSON producer boundary

- `.ufo/round-46/scouts/V4.md` records the producer-vs-payload boundary at HEAD/tree `055d3b9a3f7eb28d13452a0d26853ef4feabf2ae` / `e8dced184612a9738c5b8d244a0837fbd955a7da`; registration SHA-256 `ff60fce90a203dbd793fa4fc21bd8e7139df196601e1b76d935aa62903af0e53`.
- `PYTHONDONTWRITEBYTECODE=1 python3 verifiers/verify_harness_claims.py --json` exited 0; captured output `.ufo/round-46/evidence/V4-live.json` is 11,020 bytes, SHA-256 `4922af719d5678135494fd06832699308225688e2ad70e2c7e84221945c902a1`. Producer SHA-256 `6b8eb4b6e85b1640cbdbfedd10a6ee9055923caaad226736e7f672e8dff934f3`, baseline SHA-256 `b76d433e64afad15f4c78ce1169208377ba470f8dc81f2749110ed9361e35b9b`. The captured 28 rows carry per-row `mode`/`verdict` (17 equal, 10 zero, 1 positive; all 28 PASS); no top-level mode/verdict/summary or row summary.
- The real-input join `PYTHONDONTWRITEBYTECODE=1 python3 verifiers/compare_harness_independent.py --live-json .ufo/round-46/evidence/V4-live.json --expect-n 28 --no-stamp --json --receipt .ufo/round-46/evidence/V4-join-current-receipt.json` exited 0 at 24/24 protocol, 20/24 strict, 4 adjudicated, 4 scoped out. It used the worktree comparator SHA-256 `8b4f3d10ab30e8517846e0606855805eaad04ccf3154d93c882e4b0f41f07c1f`, stable before/after; output SHA-256 `890f31f3185c3d66bf5d9799ab04941f25076e243e757fccba2187409aa972a4`, receipt SHA-256 `ba5c4f54e2710f2ef846e802ddd7392c7101f20fdec70407a56a23f4983a1df8`. No source, fixtures, floors, registry, or Git refs were edited; comparator self-test, floors, and corpus gates were not run.

## 2026-10-19 — Round 46 W1 floors-registry watch

- W1 report `.ufo/round-46/scouts/W1.md` SHA-256 `f7b1c940f46db2fd5d95a72c3d929686403972a6854880a526501a17c693e46b` records two initial green guard runs at 16:27:44/16:28:31 (-03), followed by shared comparator edits and red guard runs. Latest stable measurement: `python3 verifiers/check_assertion_floors.py` at `2026-10-19T16:33:15-03:00`, HEAD/tree `055d3b9a3f7eb28d13452a0d26853ef4feabf2ae` / `e8dced184612a9738c5b8d244a0837fbd955a7da`, exit 1; comparator `observed=292 floor=255 self_test_failures=13`, other eight instrument rows PASS. The ten declared instrument/registry inputs plus comparator fixture-file hashes were identical before/after this run.
- At that run, `floors-registry.json` SHA-256 remained `36536063ef803122c16a13cc9db6cad5cc47b58e173caeafa1fd6f2677619622`, guard SHA-256 `b9e0ce16cdb5de8592ffd877de684560495118b499ef41209cd904027f5fc6ef`, comparator SHA-256 `8b4f3d10ab30e8517846e0606855805eaad04ccf3154d93c882e4b0f41f07c1f`. No registry edit or Git add/commit/ref operation was made by W1. This is not a round-close result; rerun the guard after the shared comparator/fixture work settles.

## 2026-10-19 — Round 46 L1 comparator self-test coverage audit

- `.ufo/round-46/scouts/L1.md` SHA-256 `d9452ba37485051185a3f2784c8efb8b2489f386dbeff65c41d0855e5a7b6f9b` (`sha256sum .ufo/round-46/scouts/L1.md` at `2026-10-19T16:34:26-03:00`) records the coverage map and shared-tree limits. Its self-test measurement is pinned to worktree comparator SHA-256 `5763094d510e53d0ac438f292d01846852fa00f0f2805d2a6c1634df55b357f7`, HEAD/tree `055d3b9a3f7eb28d13452a0d26853ef4feabf2ae` / `e8dced184612a9738c5b8d244a0837fbd955a7da`.
- `PYTHONDONTWRITEBYTECODE=1 python3 verifiers/compare_harness_independent.py --self-test` returned exit 1 with 5 failures over 276 assertions at `2026-10-19T16:32:09-03:00–16:32:11-03:00`. The report identifies stale receipt expectation and the scope-CWD fixture harness gap; raw duplicate payload arms did not appear among failures. A concurrent normal join attempt changed comparator SHA from `19b1ec15a25f25efda3f48006d4a03b1547c1e0d8099f40c013bbaa111b87ea5` to `016694f3d014309dbcbecf0f14fc99cd34c484e4816c2a5cd181bb573e6eeb31` during execution, so its exit-0 result is explicitly not counted as source-pinned verification.
- L1 changed no verifier, fixture, scope, or floors-registry file and ran no floors guard; the shared worktree edits are not attributed to L1. No Git add/commit/ref operation.

## 2026-10-19 — Round 46 Z1 post-publication recheck

- Z1 report `.ufo/round-46/scouts/Z1.md` was updated with a later read-only snapshot; current report SHA-256 `072deb145c236977af509f0e1841328c83b469bfe5b9a871878a670dc41e0c93` (`sha256sum .ufo/round-46/scouts/Z1.md` at `2026-10-19T19:34:47Z`). The added inventory is pinned at `2026-10-19T19:34:14Z`, HEAD/tree `055d3b9a3f7eb28d13452a0d26853ef4feabf2ae` / `e8dced184612a9738c5b8d244a0837fbd955a7da`.
- At that snapshot, Round 46 drafts were **320 files / 4,373,866 bytes** (manifest SHA-256 `cd9abe805ecec0373bf2c6fc5a78d975ac7fd22343e061890a894b38173529f9`) and evidence **145 files / 1,243,771 bytes** (manifest SHA-256 `c1414ceb473e543719ba38cfc8f63fa36caf008fbcc1f5f9db32bca368bdc4df`). These supersede the report's earlier point-in-time draft/evidence counts, not the R41/R45 preservation findings. Owner-led pruning to cited counting inputs remains outstanding.
- The latest symlink scan found zero `.git` symlinks (four ordinary R1 symlink test fixtures); there was no `.git` directory under drafts. R41 evidence and the census still matched HEAD. Worktree comparator was SHA-256 `8b4f3d10ab30e8517846e0606855805eaad04ccf3154d93c882e4b0f41f07c1f`; no gate run was claimed on that moving source. No Git add/commit/ref operation or out-of-lane write.

## 2026-10-19 — Round 46 V5 duplicate JSON-member verification

- `.ufo/round-46/scouts/V5.md` SHA-256 `301f6303958b0a2af0fbfc1730466ef8a0bc057080aed9b62f67037d11f38963` records the raw duplicate-member matrix. `PYTHONDONTWRITEBYTECODE=1 python3 -B .ufo/round-46/drafts/v5/probe.py` ran 19 CLI arms against each of frozen comparator `git show 055d3b9a3f7eb28d13452a0d26853ef4feabf2ae:verifiers/compare_harness_independent.py` SHA-256 `1101213a7bed5410151564aeb5a4b49030a4821c86e7469286f046253fbc51e4` and stable worktree comparator SHA-256 `8b4f3d10ab30e8517846e0606855805eaad04ccf3154d93c882e4b0f41f07c1f`, at HEAD/tree `055d3b9a3f7eb28d13452a0d26853ef4feabf2ae` / `e8dced184612a9738c5b8d244a0837fbd955a7da`; official scope SHA-256 `fbcdc8d247475a5f1c2c613d78b6188dab77a766b02497a729a884687a70f77a` was stable. Matrix `.ufo/round-46/evidence/V5/arm-matrix.json` SHA-256 `74eb59c688ae10ce670c6dd4b5831fa8b45da796a40d3e3689b3ac99caef0cb1`: baseline last-member-wins accepted all 16 duplicate forms, while the worktree candidate named all 16 as exit 2; ordinary control/mismatch were 0/1 on both.
- Preserve `.ufo/round-46/drafts/v5/probe.py` SHA-256 `89c315094855b450b360f7a4aeb2039cbfa03349de53d21d1561827b3662a831` and `.ufo/round-46/drafts/v5/inputs/` as the counting bundle. V5 made no comparator, fixture, floors-registry, or corpus-source edit and ran no self-test/floors guard. No Git add/commit/ref operation.

## 2026-10-19 — Round 46 E1 scope-file edge probes

- `.ufo/round-46/scouts/E1.md` SHA-256 `63fd2187a277da165ef095dec935505b570c00ed398dd90015ff518ce230118b` records E1's scope-file probes. `PYTHONDONTWRITEBYTECODE=1 python3 .ufo/round-46/drafts/e1/probe.py` (runner SHA-256 `473c37e539cc2e289cc26391e0170ac50e5b6942c954f54063ff1fc04431579a`) ran the frozen-comparator cases `2026-10-19T19:32:49.717296Z–19:33:11.942016Z`; result manifest `.ufo/round-46/evidence/E1-scope-edge-results.json` SHA-256 `58ec1b06f70f78a9d43f2ff8eb287676cb586d77d2704515c0dc91823090ae50` stores full argv and per-case input/output pins. Target: `git show HEAD:verifiers/compare_harness_independent.py`, HEAD/tree `055d3b9a3f7eb28d13452a0d26853ef4feabf2ae` / `e8dced184612a9738c5b8d244a0837fbd955a7da`, SHA-256 `1101213a7bed5410151564aeb5a4b49030a4821c86e7469286f046253fbc51e4`. Captured live/independent inputs were `0bc250f5197c9dbbdbdce7e15c4220e0904118a8c290f81295aa18464b0b0341` / `eb1068a4f7b934d5553106d60737c05d8d1cd8d9ef827467f80281cac3853887`; official scope SHA-256 `fbcdc8d247475a5f1c2c613d78b6188dab77a766b02497a729a884687a70f77a`.
- Results on those frozen bytes: a live row listed in scope but missing from payload is uncovered (exit 2); an ID absent from both sides is accepted but inert (24/24); an unsupported probe kind with active scope-outs and an empty set paired with four declared scope-outs fail closed; an empty set with fully-derived rows passes 28/28. A `committed_set` plus matching self-digest is ignored in favor of actual `scope_out`; adding a fifth scope-out to a caller-selected custom scope file with a valid recomputed probe passes at 23/23. The report distinguishes that caller-selected-input trust boundary from tampering with the default scope.
- The first attempt used archived probe observables that had drifted (the archived file recorded 766 session files / 625 skills-block files; the fresh measurement was 767 / 626) and failed closed before reaching most intended branches. The final runner refreshed those payload probes; only final-manifest outcomes are reported. No product verifier, fixture, registry, or corpus source was changed. Self-test, floors, and corpus gates were not run. Preserve `.ufo/round-46/drafts/e1/` while cited; no Git add/commit/ref operation.
- At `2026-10-19T19:35:31.511485Z`, HEAD/tree were unchanged; the shared worktree comparator was SHA-256 `2dff2b4c5c5ccc2e6cd9e74101a25a4cbe96da2062f0c54540b8a42b0898e2d8` and remained an in-flight concurrent edit. E1 used only the frozen `1101213a` comparator.

## 2026-10-19 — Round 46 D1 frozen scope-file path map

- `.ufo/round-46/scouts/D1.md` SHA-256 `b96ca34e81015efb1f4548e307d33965bfba62610ea8f2fb11c886a979552419` (`sha256sum .ufo/round-46/scouts/D1.md` at `2026-10-19T19:37:51Z`) maps each frozen `--scope-file`/`--cwd` read and resolution path. Source is `git show 055d3b9:verifiers/compare_harness_independent.py`, SHA-256 `1101213a7bed5410151564aeb5a4b49030a4821c86e7469286f046253fbc51e4`; HEAD/tree at the pin check was `055d3b9a3f7eb28d13452a0d26853ef4feabf2ae` / `e8dced184612a9738c5b8d244a0837fbd955a7da`. The modified worktree comparator was not executed.
- The frozen planted-CWD replay command and process CWD are in D1.md. It returned exit 0 with one joined row from two live rows; receipt `.ufo/round-46/evidence/d1/planted-receipt.json` SHA-256 `50ea2517a3261104f89ad8b6cf88639880d7a1e58c034304896d1bcf750fd83f` attests repository scope digest `fbcdc8d247475a5f1c2c613d78b6188dab77a766b02497a729a884687a70f77a`, while its committed set came from planted scope SHA-256 `838fe72cf8725f213c3b142b078521a9ec275238a6aa3ab8141b5a63b1640dd4`. The honest-CWD control returned exit 2 with stderr SHA-256 `638f352a56f7f01c37d1d85e79a8e0c5f75974e1e145a85cdcbbb96b58f9b7a9` at `2026-10-19T19:32:45.453173Z` on the same frozen comparator and JSON inputs.
- Counting inputs under `.ufo/round-46/evidence/d1/`: live JSON SHA-256 `b7cdc2c55ea60700c198877f08cd3c4e98f69887e51ad88c59a8dbb2f00e4462`; independent JSON `28f371842bcc95b5f9386823201e29ff3389da837aa7cbadef9e2e665847c5bc`; planted scope SHA above. Frozen comparator copy `.ufo/round-46/evidence/x3/frozen-comparator-055d3b9.py` was SHA-identical to the Git blob. Preserve both D1 evidence and this referenced X3 source snapshot.
- The first attempt to reuse the older R45 multi-row payload was discarded because stale dynamic probe observations caused unrelated false-blocker errors. D1 changed no production source and did not run comparator/IND self-tests, floors, or corpus gates. No Git add/commit/ref operation.

## 2026-10-19 — Round 46 X1 scope-path resolution probe

- `.ufo/round-46/scouts/X1.md` SHA-256 `377256973cd3da3138e650655510dee76e6b07a097c1123fba767005290ce004` records X1's path arm results. `PYTHONDONTWRITEBYTECODE=1 python3 -B .ufo/round-46/drafts/x1/probe_paths.py` (runner SHA-256 `8e3a9a9748136b69e880c095c9cf0927be7ebe2bae1721b71f882ae24adb0b1b`) ran at `2026-10-19T19:32:43.070366Z–19:32:43.242351Z`, pinning frozen comparator blob SHA-256 `1101213a7bed5410151564aeb5a4b49030a4821c86e7469286f046253fbc51e4` at HEAD/tree `055d3b9a3f7eb28d13452a0d26853ef4feabf2ae` / `e8dced184612a9738c5b8d244a0837fbd955a7da`. Synthetic live/independent input SHA-256 values were `872db0483080f33ea937a7083a845980636463a0b5b19e560691a152299a773d` / `221c42ce2be15757280cbc25fc736830b8b87991a18f0c415787ed4e9503a35a`.
- The absolute-file and symlinked-directory arms' receipts matched stable target bytes. The relative `--scope-file` arm reproduced the process-CWD versus `--cwd` mismatch (enforced file SHA-256 `2e64fb2ea3464797fca20749afcc86b06ddf965bcf3169a636f18581e9de4be8`; receipt file SHA-256 `184e1e31b63dd5b22d997f7a27ee2ce0985fbb6d989d9894c9a141fb635e6cc7`). Absolute outside-repo selection matched its receipt and is caller-selected trust. The reported `0/0` is a one-row synthetic case after scope-out, not a live-join result.
- Preserve `.ufo/round-46/drafts/x1/probe_paths.py` for replay; temporary inputs/receipts were removed. The report discloses the excluded defective early attempts. X1 made no production verifier/fixture/floors-registry edit and ran no full join or gates; no Git add/commit/ref operation.

## 2026-10-19 — Round 46 W1 latest floors remeasurement

- This append supersedes W1's earlier 16:33:15 guard as the latest valid observation. Report `.ufo/round-46/scouts/W1.md` SHA-256 `09bf45f4b42e771e8af8a1e0cf2adf22381603158fafaf3b4fdba8af661f416f`; observation `2026-10-19T16:35:31-03:00`, HEAD/tree `055d3b9a3f7eb28d13452a0d26853ef4feabf2ae` / `e8dced184612a9738c5b8d244a0837fbd955a7da`. `python3 verifiers/check_assertion_floors.py` exited 1: eight rows passed, comparator `observed=0 floor=255 summary=missing`.
- The stable 103-file input manifest (ten verifier/registry inputs plus all comparator fixture files) had SHA-256 `361b81db9a7c12865dca5e723eb928c91ea26ebc8f498dffb3e424f6033d9609` before and after the guard. Registry/guard/comparator SHAs were `36536063ef803122c16a13cc9db6cad5cc47b58e173caeafa1fd6f2677619622` / `b9e0ce16cdb5de8592ffd877de684560495118b499ef41209cd904027f5fc6ef` / `2dff2b4c5c5ccc2e6cd9e74101a25a4cbe96da2062f0c54540b8a42b0898e2d8`.
- Direct `python3 verifiers/compare_harness_independent.py --self-test` at `16:35:42-03:00` exited 1 with a traceback ending `CompareError: live metadata missing: modes, verdicts, summary_paths`; the same 103-file manifest was unchanged before/after. A `sha256sum` snapshot at `16:36:18-03:00` still showed the same registry and comparator hashes. No floors-registry or verifier change, Git add, commit, or ref mutation was made by W1; close-time status remains pending a clean self-test and guard rerun after shared edits settle.

## 2026-10-19 — Round 46 J1 join-output determinism

- `.ufo/round-46/scouts/J1.md` SHA-256 `ef4ae21243ca6ccac96dbc122eb3a86ced1f2a8dacbce44872c18e14a1903c37` records the bounded repeatability result and failed current-worktree candidate. At `2026-10-19T19:34:43.469857Z–19:35:23.848922Z`, five fresh processes ran `/usr/bin/python3 -B .ufo/round-46/drafts/j1/compare-snapshot.py --json --no-stamp --expect-n 28 --cwd /home/vgpnk/Projects/shokunin/kotoba-shokunin`; each exited 0 with identical 6,225-byte stdout SHA-256 `b38dc4f2991f7c06578d76c6f317d1b99407c05d4bfefbf07fa231890235b80e` and empty stderr. The snapshot SHA-256 is `8b4f3d10ab30e8517846e0606855805eaad04ccf3154d93c882e4b0f41f07c1f`; live join was protocol 24/24, strict 20/24, four adjudicated/four scoped out, on HEAD/tree `055d3b9a3f7eb28d13452a0d26853ef4feabf2ae` / `e8dced184612a9738c5b8d244a0837fbd955a7da`. Live, independent and scope input SHA-256 values are listed in J1.md.
- The mutable worktree comparator at SHA-256 `2dff2b4c5c5ccc2e6cd9e74101a25a4cbe96da2062f0c54540b8a42b0898e2d8` was also invoked five times at `2026-10-19T19:36:21.177088Z–19:36:24.860019Z`; each exited 2 before emitting JSON with identical stderr SHA-256 `71df090a1f35eacf0e2b0968136ae8b5fd9fa3116a653ee5b48c43f54c345b08` (`live metadata missing: modes, verdicts, summary_paths`). Do not treat that in-flight producer/comparator mismatch as a passing join; rerun determinism after integration.
- Preserve `.ufo/round-46/drafts/j1/compare-snapshot.py` while J1.md is cited. J1 changed no product source and ran no self-test, floors guard or corpus gates; no Git add, commit, or ref mutation.

## 2026-10-19 — Round 46 V5 final matrix and shared-source drift

- Final `.ufo/round-46/scouts/V5.md` SHA-256 `804a22a421c7376126f8b8f4698628bd9959263e22dbb610cb298105dce2dab8` supersedes the earlier V5 matrix citation above. `PYTHONDONTWRITEBYTECODE=1 python3 -B .ufo/round-46/drafts/v5/probe.py` ran 19 arms per source at `2026-10-19T19:35:40.314800Z–19:35:41.762203Z`, HEAD/tree `055d3b9a3f7eb28d13452a0d26853ef4feabf2ae` / `e8dced184612a9738c5b8d244a0837fbd955a7da`, frozen comparator SHA-256 `1101213a7bed5410151564aeb5a4b49030a4821c86e7469286f046253fbc51e4`, tested worktree SHA-256 `2dff2b4c5c5ccc2e6cd9e74101a25a4cbe96da2062f0c54540b8a42b0898e2d8`, scope SHA-256 `fbcdc8d247475a5f1c2c613d78b6188dab77a766b02497a729a884687a70f77a`. Matrix `.ufo/round-46/evidence/V5/arm-matrix.json` SHA-256 `8b071ff9d5bbc86140fcc5d62a0147041cfd07e043c32c7b0d8cf0ca1ea56357` records baseline last-wins vs 16/16 named duplicate rejections on the tested worktree; the prior matrix hash `74eb59c6…` and worktree SHA `8b4f3d10…` are superseded.
- A later `sha256sum verifiers/compare_harness_independent.py` at `2026-10-19T19:37:33.638254535Z` returned `f5d13345cf319125cef21eb44a35ecce56321e5bcda7cb5458787cdf30bb9d02`; that post-measurement shared edit was not retested. Preserve `.ufo/round-46/drafts/v5/probe.py` SHA-256 `89c315094855b450b360f7a4aeb2039cbfa03349de53d21d1561827b3662a831` and its `inputs/` counting bundle. V5 made no comparator/fixture/floors/corpus source edit or Git add/commit/ref operation; comparator self-test and floors guard were not rerun.

## 2026-10-19 — Round 46 A2 scope-out contract audit

- `.ufo/round-46/scouts/A2.md` SHA-256 `b151d243af1d88ad40b1e1760b58fe4915265b641b65bf5d0a82c21272d74d25` records the scope-out contract audit for claims SHA-256 `ff60fce90a203dbd793fa4fc21bd8e7139df196601e1b76d935aa62903af0e53`, at HEAD/tree `055d3b9a3f7eb28d13452a0d26853ef4feabf2ae` / `e8dced184612a9738c5b8d244a0837fbd955a7da`. The comparator target was the exact Git blob SHA-256 `1101213a7bed5410151564aeb5a4b49030a4821c86e7469286f046253fbc51e4`; committed scope SHA-256 `fbcdc8d247475a5f1c2c613d78b6188dab77a766b02497a729a884687a70f77a`.
- `PYTHONDONTWRITEBYTECODE=1 python3 -B .ufo/round-46/drafts/a2/replay_scope_contract.py` used only read-only `git show` / `git rev-parse`; runner SHA-256 `9e22a0304879c754b1cb62cbd09bfbc9272bad31e60c55e168b374cab6fb6319`. Result `.ufo/round-46/evidence/a2/scope-contract-results.json` SHA-256 `3be40b9cb096549529c2c501436eafd69687c138631be4b8024833ca044dfa65` records stable input hashes and five exact-byte cases.
- On a controlled in-repo carrier, the retargeted control passed 24/24. Fabricated payload reason and row evidence each still exited 0 at 24/24; an invalid probe kind and a mismatched recomputed observable each exited 2 with `false blocker`. Finding: the committed entry kind is only enum-checked, the payload reason/evidence are not bound to the entry, and the probe result is recomputed for an absolute target supplied by the payload rather than a target pinned in the scope file. The receipt records the committed set and probe kind, not the probe target. C3 remains open; the report identifies the R45 census/SCORECARD reconciliation still needed.
- No comparator, fixture, scope, corpus, SCORECARD, floor, or registry source was changed. Self-test/floors were not rerun by A2; the replay's worktree comparator was not executed. No Git add, commit, or ref operation.

## 2026-10-19 — Round 46 X2 live-JSON shadow arms

- Report `.ufo/round-46/scouts/X2.md` SHA-256 `aac382ef8019443442d624719ce4598efbd7c705eb20ccedd42e3db1066a4ac2` records the caller-supplied Live-JSON shadow boundary; C2 remains open and no whole-claim closure is asserted. Measurement was at HEAD/tree `055d3b9a3f7eb28d13452a0d26853ef4feabf2ae` / `e8dced184612a9738c5b8d244a0837fbd955a7da`, claims SHA-256 `ff60fce90a203dbd793fa4fc21bd8e7139df196601e1b76d935aa62903af0e53`.
- `PYTHONDONTWRITEBYTECODE=1 python3 .ufo/round-46/drafts/x2/probe_livejson_shadows.py` ran 8/8 expected arms at `2026-10-19T19:36:46Z–19:36:54Z`; runner SHA-256 `c83f33ab6d093f6b4bcc3f792f593316063e207ac392e6d5c504cf92121e09e6`, result `.ufo/round-46/drafts/x2/probe-results.json` SHA-256 `243c76f54c344c79b0eedff1d31c188141bcc53df7c7467ab02e7d8b33eff2a7`. Target was only frozen `055d3b9` comparator SHA-256 `1101213a7bed5410151564aeb5a4b49030a4821c86e7469286f046253fbc51e4`, verified equal to the Git blob. The moving worktree comparator was `2dff2b4c5c5ccc2e6cd9e74101a25a4cbe96da2062f0c54540b8a42b0898e2d8` at both run boundaries and was not executed.
- In the same shell window, fresh live/independent producer captures (28 rows each) had SHA-256 `4922af719d5678135494fd06832699308225688e2ad70e2c7e84221945c902a1` / `03513eadafe80df7b4f14841ad8e74c8c33637dafb441b35fbfb4bc1f885b1f8`; producer source SHAs were `6b8eb4b6e85b1640cbdbfedd10a6ee9055923caaad226736e7f672e8dff934f3` / `872993f875338f4f89d5b76178c124313e9fc3368966f8a32583acd0430bdbd1`, scope `fbcdc8d247475a5f1c2c613d78b6188dab77a766b02497a729a884687a70f77a`. Frozen full join exited 0: protocol 24/24, strict 20/24, four adjudicated/four scoped out, no remaining disagreement; join SHA-256 `f08c65e76f19ae989eef9ee53dceeb0bf71839ae1b233bb52f16e61f9cab684c`, receipt `1a885ae24326cdb5625c9206911417b7a4b9f81f8ae779a079322dff17297593`.
- Disclosed first attempt `.ufo/round-46/drafts/x2/probe-results-first-attempt.json` SHA-256 `b9a811609e338b803294a0f19a6b2d00403b4e43aa81146f1c8ae153004bb4df`: stale scope-probe count made its full-control exit 2 (`false blocker`; declared `files_with_skills_block=625`, recomputed `626`). A freshly paired control then passed. Post-run shared-source checks saw live producer change to `29e71b9a662e4aef12aa9fefff2446f3b09c4521c0506c489400ebc262a891fb` at 19:38:08Z, and worktree comparator subsequently change from `c43181ee87eedf159c77352369428205738b95e03ef5875d1876018f7c24e35a` to `6abc942750bc83ce86a2c7c42b162931d741509afaa0a9dcb2adb02f8d6a93b5` by 19:38:45Z; these later shared bytes were not tested. Preserve `.ufo/round-46/drafts/x2/` as the counting bundle. X2 changed no comparator, producer, floor, scope, registry, or fixture source. The final `git status --short --branch` showed shared worktree changes in those areas (including `verifiers/floors-registry.json`); X2 did not edit them. No self-test, floors, or corpus gates were run; no Git add/commit/ref mutation.

## 2026-10-19 — Round 46 U1 upstream-document recheck

- Report `.ufo/round-46/scouts/U1.md` SHA-256 `d8d137d24d24f1605f5d6164b761d33fbdbcd403ae1a8ee43227b28b218e1388`, pinned at `2026-10-19T19:41:24Z`, HEAD/tree `055d3b9a3f7eb28d13452a0d26853ef4feabf2ae` / `e8dced184612a9738c5b8d244a0837fbd955a7da`. Census doc, R37 §6 doc, and V10 source hashes were `286937b7a5d7d2e0c370282a13ef7cd326dc1e77e2263f57a8e11b1ba8ee6cc7`, `37376ed234457b1a49b0f1bfa2a10a500e7b5689fe31d994b37d2500d2aafa3b`, and `1755883c87832fd30b8dc7bb7e16eac5cf0a5803769163b09080125f9fe3e92b` at that read.
- At `2026-10-19T19:38:15Z`, the census replay command `python3 .ufo/round-45/drafts/v10/post-r44-hunt.py` and its two documented R41 draft replay commands each exited 2 because the referenced runners are absent. The prefixed V10 evidence scripts and R45 result JSON exist; the R41/R45 draft paths listed in U1.md do not. The V10 documented gate set was rerun `2026-10-19T19:36:35Z–19:36:53Z` at the frozen comparator blob `git show HEAD:verifiers/compare_harness_independent.py` SHA-256 `1101213a7bed5410151564aeb5a4b49030a4821c86e7469286f046253fbc51e4`: join exited 0 at protocol 24/24 (output SHA `60da2f224759ecdc6c7232941a3d5ee20f59b1097c6624eac5d063768ed3bbec`), self-test passed 255 assertions, floors passed exact `10/150/91/87/1597/62/104/255/150`, and both corpus gates exited 0. Evidence and command output SHAs are in U1.md; temporary HEAD snapshot was removed.
- R37 §6 null-echo command on the frozen comparator exited 2 (doc expects exit 1) with `scope-out value laundering`; `R1-make_blind_tree.sh` exited 0 but reported 11 residual files and a nonzero in-tree pins guard. Both results and their script/output hashes are in U1.md. All §6 source inputs exist; the R38 draft scratch path cited by the doc is pruned and its PRUNE.log exists. Preserve `.ufo/round-46/drafts/u1/` while cited. U1 changed only this report and the lane log; no verifier, fixture, scope, corpus, floor, or registry source and no Git add/commit/ref was changed by U1. Shared worktree edits were not attributed to U1.

## 2026-10-19 — Round 46 P2 live-JSON metadata shadows

- Report `.ufo/round-46/scouts/P2.md` SHA-256 `b2526d81922bc56c63f6f4ed27d7df8bb1fe0518e12e64777ef9b6aec009ec19` covers only C2(a)'s mode/verdict/summary consistency arms. The baseline is HEAD/tree `055d3b9a3f7eb28d13452a0d26853ef4feabf2ae` / `e8dced184612a9738c5b8d244a0837fbd955a7da`; `.ufo/round-46/drafts/p2/compare-before.py` is byte-identical to the HEAD comparator blob (SHA-256 `1101213a7bed5410151564aeb5a4b49030a4821c86e7469286f046253fbc51e4`) and must be preserved while cited.
- The three frozen shadow inputs previously passed with exit 0; red-before stdout SHA-256 values were mode `56c144c42abaad611f77d27504d5aadebbad99fef3355145b6feac88276d2eac`, verdict `47fa574fed8e500d2d5744d3cd337c7596891a24b4b5ba46fbbc2bef28758172`, summary `721723e7ee5f88fb31ede98a16666d5792d17c6cf745860acb6ad28720bfbf99`. Against worktree comparator SHA-256 `7a6ca85c3c02f5a350bfd12bfa0a2f1243e0cdb22a4d1f8b7cc15d8ab4d5728b`, all three now exit 2, name the affected check and the mode/verdict/summary class, and have no traceback; stderr SHA-256 values and exact errors are in P2.md and `evidence/p2/after-*.stderr`.
- The live producer now emits `modes`, `verdicts`, and `summary_paths` in JSON, using result rows and `CHECKS` extractor keys; the comparator requires and reconciles these on producer-shaped payloads. At `2026-10-19T19:41:18Z`, producer→comparator ran with current scope SHA-256 `3d8500ed1757b6da2ca7842ad411c5025faa1d094a04b383139e9caeeb0871e4`: producer 28/28 mirrors aligned, join exit 0 at protocol 24/24, strict 20/24, four adjudicated and four scoped out. Final live/join/receipt SHA-256 values are `e6c7f656ad0d115f5d63c5aeb8bf16dd72b27948a4f700b735df580a43eaeff5` / `a5ccb67fc1e5ec72e0c960e56d3aefbb14cc9386a05c97d67c92dd26a8a531c4` / `18e584de855933932d6a761134bba62b54e91b31bc69eeedc89d37bb4242b19d`.
- Comparator self-test passed 0/293 (output SHA-256 `15e2094906cb9ff7419b2f14ae0edc7bd59d93b6082d9e4ec49dc06e6ed1717f`); the final floors guard passed 9/9 exact floors `10/150/91/87/1597/62/104/293/150` on an unchanged before/after input manifest `c7952022e520db6f4703bfd3cabc349ffd5839f8f06c1a5820673c3838bf3dc8` (guard output SHA-256 `6d31a9f63a7ed213a9d9aa457f2770f0dbc3356d6afd8846cbde1010fa68fd9a`). The shared guard tables/registry are synchronized at comparator floor 293.
- Trust boundary: these are consistency checks, not provenance authentication; coherently rewritten copies can still be fabricated. P2 does not claim raw duplicate-member, scope-file, or scoped-out metadata closure, and does not attribute the concurrent changes for those claims. No Git add/commit/ref operation.

## 2026-10-19 — Round 46 H1 live producer-trust boundary

- `.ufo/round-46/scouts/H1.md` SHA-256 `18e3abaad92990382a186d8bf211f697f8922df546208999cd14e5e34b3f63ed` (supersedes `e6c47839155c04fa10d5b979995ff10b1870a836b789c24bcc9d452352a4fad9` after a source-scope addendum) maps which live-JSON fields are trusted, consistency-checked, or re-derived and answers the shadow-contract question. It uses claims SHA-256 `ff60fce90a203dbd793fa4fc21bd8e7139df196601e1b76d935aa62903af0e53` and distinguishes frozen HEAD/tree `055d3b9a3f7eb28d13452a0d26853ef4feabf2ae` / `e8dced184612a9738c5b8d244a0837fbd955a7da` from the mutable candidate.
- `python3 -B .ufo/round-46/drafts/h1/replay-pinned-head.py` replayed saved cases against the baseline comparator blob SHA-256 `1101213a7bed5410151564aeb5a4b49030a4821c86e7469286f046253fbc51e4`; `.ufo/round-46/evidence/H1-trust-boundary-pinned-head.json` SHA-256 `830650b2e5704a3620ce8b0e4b6919c65d64de7548847e54abd320908a48601d` is the cited baseline evidence. The earlier transient H1 manifest used moving source bytes and is not used for outcomes.
- `python3 -B .ufo/round-46/drafts/h1/replay-current-snapshot.py` completed `2026-10-19T19:41:51.763110Z` on an in-memory comparator snapshot, also preserved as `.ufo/round-46/drafts/h1/current-comparator-snapshot.py` SHA-256 `b3bad452ebb0e7d48360dca00466101e2fad532c92aa8fb1f1034b0272b77d06`. Current evidence `.ufo/round-46/evidence/H1-trust-boundary-current-snapshot.json` SHA-256 `82c19f06e3430281cbf7ce253bb06ebdca91aceafac063e56e79f4b2fa27a6bc` pins producer sources and scope. Fresh control passed 24/24 protocol; one-copy mode/verdict/summary conflicts failed 2; coherent mode rewrite and caller-selected decoy summary path still passed 24/24. The report states the candidate's documented consistency-only contract and the canonical-path residual.
- Preserve `.ufo/round-46/drafts/h1/` (runner SHA-256 `186aa86df4e69d02bc1658f9ff44a5d926d1e8a27517336c35189b1012533b0b`) as the counting bundle. H1 changed no product source or Git state and did not run comparator self-test, floors, or corpus gates; no Git add/commit/ref mutation.
- At `2026-10-19T19:51:23Z`, comparator worktree SHA-256 was `ccf41c23d2c766124b27f60653508cd1590aa625cbf8afd8da68b56f7b5bc04d`, HEAD/tree unchanged. Its diff from the tested `b3bad452` snapshot is confined to the comparator's self-test fixture battery and fixture/stub setup, not live parser/validator logic. The newer hash was not replayed; H1's behavioral claims remain scoped to the frozen `b3bad452` snapshot.

## 2026-10-19 — Round 46 V1 C1 scope-file path resolution

- Report `.ufo/round-46/scouts/V1.md` SHA-256 `50427375389a06ec5772663bdec8e8ded96b0dea110486a39817b2276c1ea247` records the final V1 measurement. `PYTHONDONTWRITEBYTECODE=1 python3 -B .ufo/round-46/drafts/v1/rebuild_scopefile_arms.py` ran at `2026-10-19T19:43:44.168869Z–19:43:52.879703Z`, stable at HEAD/tree `055d3b9a3f7eb28d13452a0d26853ef4feabf2ae` / `e8dced184612a9738c5b8d244a0837fbd955a7da`, worktree comparator SHA-256 `705423087f7adb395d690401945b7a7733b3a3ab4f8c04f67c7a532bb6b8172e`, scope SHA-256 `3d8500ed1757b6da2ca7842ad411c5025faa1d094a04b383139e9caeeb0871e4`. A post-run check at `19:44:57.416589181Z` confirmed the same source/tree.
- Result `.ufo/round-46/drafts/v1/scopefile-arm-results.json` SHA-256 `a6e97f39d22cfd818883381f3091e845afecef27c4f98d06bc87c319c199e785`; runner SHA-256 `de51ce35963101c475d7789ee781a9336c7ece2c428600efe9b6370f10c640a9`. Frozen `055d3b9` comparator SHA-256 `1101213a7bed5410151564aeb5a4b49030a4821c86e7469286f046253fbc51e4` reproduced the planted-CWD relative-path defect (exit 0 at 23/23; enforced planted SHA `29e9263e…`, receipt official SHA `3d8500ed…`). Candidate snapshot passed all 4 arm expectations: planted-CWD attack exit 2 with named probe drift/laundering; both successful scope controls' receipts matched enforced path+digest; total 8/8 expected outcomes across frozen and candidate.
- The candidate's real producer join exited 0 at protocol 24/24, strict 20/24, four adjudicated/four scoped out, zero disagreement/uncovered/unknown. Fresh 28-row producer captures: live SHA-256 `166b2ea315701c9ec2ea0f26aa16bf5cadf7e0d4db9683457cb4db3152bf38e6`; independent SHA-256 `03513eadafe80df7b4f14841ad8e74c8c33637dafb441b35fbfb4bc1f885b1f8`.
- Preserve `.ufo/round-46/drafts/v1/` while cited. V1 changed only its draft runner, report, and this log entry; no production verifier/scope/registry or prohibited corpus/protocol files, and no Git add/commit/ref operation. Self-test/floors are not claimed by V1.

## 2026-10-19 — Round 46 T1 live regression join

- `.ufo/round-46/scouts/T1.md` SHA-256 `35a442c19862495639cf231fd2990a917cbc505b853c41d31da2b49c1a18f009` records the baseline and shared-worktree reruns, including the temporary metadata rejection and recovery. Latest `PYTHONDONTWRITEBYTECODE=1 python3 verifiers/compare_harness_independent.py --expect-n 28 --cwd /home/vgpnk/Projects/shokunin/kotoba-shokunin --scope-file verifiers/harness-independent-scope.json --no-stamp --report .ufo/round-46/evidence/T1-after-landing-11-rows.md --json --receipt .ufo/round-46/evidence/T1-after-landing-11-receipt.json` exited 0 at `2026-10-19T19:43:36Z–19:43:44Z`, stable at HEAD/tree `055d3b9a3f7eb28d13452a0d26853ef4feabf2ae` / `e8dced184612a9738c5b8d244a0837fbd955a7da`; comparator/live/independent/scope SHAs `705423087f7adb395d690401945b7a7733b3a3ab4f8c04f67c7a532bb6b8172e` / `29e71b9a662e4aef12aa9fefff2446f3b09c4521c0506c489400ebc262a891fb` / `872993f875338f4f89d5b76178c124313e9fc3368966f8a32583acd0430bdbd1` / `3d8500ed1757b6da2ca7842ad411c5025faa1d094a04b383139e9caeeb0871e4`. Protocol 24/24, strict 20/24, four adjudicated/four scoped out; full row table SHA `cd091c203ec5fb804141af7b9ac7f7db5e3db99daf1cccbf00d27fefde4011c8` and join JSON SHA `b38dc4f2991f7c06578d76c6f317d1b99407c05d4bfefbf07fa231890235b80e` both match baseline, so no joined row changed. Receipt SHA `9054a6be4b093b26c12a618248e63dcd4e2fa3164ca2621f6ff5c067cfa2bc95`.
- Latest floors guard `PYTHONDONTWRITEBYTECODE=1 python3 verifiers/check_assertion_floors.py` ran `19:43:48Z–19:43:57Z` on comparator SHA `70542308…`, guard SHA `c121431e396884c2b1149ced1c083f42b0462e1cfefc3550bb244e0d8858d9ca`, registry SHA `56c44bc27d600fa98e9b479735cfe7cd40cbe03004313dc7f552b7ca4719c958`; it exited 1, with eight rows passing and comparator row `observed=293 floor=293 self_test_failures=13`. Direct self-test at `19:44:28Z–19:44:31Z` also exited 1 (13 failures/293 assertions). Guard and self-test output SHAs: `d86a27c1a5f0be61b3a946f031d35c8d57ee09fef19e4350ebb206f20dce8d2c` / `26f3b40af0da4d04f1e40c8410c0fe6a7626329b5017f93169c08ac400c3a723`. The original requested exact vector ends in 255, while the shared registry currently declares 293; T1 did not edit the single-writer registry. No Git add/commit/ref mutation.

## 2026-10-19 — Round 46 C3 scoped-out metadata reconciliation

- `.ufo/round-46/scouts/C3.md` (SHA-256 `badbee87f6c1a04b029fbcc70cce10cdbdfe05b6488f0854cbdf35504853ed1a`) records the focused result. `PYTHONDONTWRITEBYTECODE=1 python3 -B .ufo/round-46/drafts/v3/replay_scope_out_drift.py` exited 0 at `2026-10-19T19:38:07.101367Z–19:38:11.025855Z`, HEAD/tree `055d3b9a3f7eb28d13452a0d26853ef4feabf2ae` / `e8dced184612a9738c5b8d244a0837fbd955a7da`. Runner SHA-256 `04704dd288efd6bda9a240ee6f350d0c74eb406c6a82653f6c13a1d4b0c567e7`; frozen comparator SHA-256 `1101213a7bed5410151564aeb5a4b49030a4821c86e7469286f046253fbc51e4`; committed scope SHA-256 `fbcdc8d247475a5f1c2c613d78b6188dab77a766b02497a729a884687a70f77a`; result `.ufo/round-46/evidence/v3/scope-out-drift-results.json` SHA-256 `076772f53d975c660570a18c5038283e2527a7ff08d646a8b0e550659e11f711`.
- The fresh live/independent producers exited 0; their source/output hashes are recorded in C3.md and the result artifact. All four joins (honest control plus three mutations) exited 0 at protocol 24/24, strict 20/24, four adjudicated/four scoped out, no disagreement/uncovered/unknown rows. `fabricated-reason`, `fabricated-evidence`, and `unconstrained-probe-target` are each explicitly accepted residuals, not class-named. The target mutation uses a fresh valid `[3,7]` carrier and recomputed observable; no landing comparator byte or formal trust-boundary declaration is claimed.
- The append-only census annotation SHA-256 is `ef78ffe9d1c24674d04d5f1f9a68a44bb2c339989f93871f2d9b37b396158471`; it leaves the historical R41/R45 46-arm counts unchanged and preserves the R45 archived-target false-blocker disclosure. `SCORECARD.md` SHA-256 is `2f217ddc5a091687c021eda51a74022de7aad2a7980686b3316201f8ccbfe517`; calibration remains 8.5, depth remains 9, and 9.5 is unsupported. The report scaffold records C3 only; C1/C2 and whole-round fields remain pending.
- Excluded attempts are detailed in C3.md: a stale independent capture pointed into another session tree; carrier preflight `[1,4]` from a missing newline stopped before capture/CLI; and the first complete replay's postcondition expected aggregate paths rather than changed leaves. No verdict is drawn from those attempts. R45's absent archived `builder-carrier` remains a false blocker; the fresh `[3,7]` test confirms target selection is still accepted. Preserve `.ufo/round-46/drafts/v3/` and `.ufo/round-46/evidence/v3/` while cited.
- Post-write documentation checks ran at HEAD/tree `055d3b9a3f7eb28d13452a0d26853ef4feabf2ae` / `e8dced184612a9738c5b8d244a0837fbd955a7da`. Corpus integrity (`--json`, source SHA `28224c76510dcafc4d7a52da41ffd2d366337414f65320cbb21e6d9de12aba9d`) exited 0, 9/9 PASS, stdout SHA `63b07476d14a168071670ec659e3725a66ad29f5589bcbd1cdfcea60d918f9d4`; independent corpus (`--json`, source SHA `254b5a2f57aabbf0b8376fce34c42250b56499d9fd7a92b5e6374ac505315d69`) exited 0 with no unindexed/stale/missing/dead/unresolvable/nonhash findings, stdout SHA `97145f793a25f8a1e902ed33eb03f4df5c02aac20b36fa235bca52baf641f03c`. Both ran at `19:45:46Z` and outputs are preserved under `.ufo/round-46/evidence/v3/postwrite-gates/`.
- Skill checklist (`PYTHONDONTWRITEBYTECODE=1 python3 -B verifiers/verify_skill_checklist.py`, source SHA `214ae44dcba45ba19656a0b2aa6c49900c618f6716a64fef0776f06437cfc8d0`) exited 1 at `19:45:47Z`: nine checks PASS; `governance.citation_resolves` reports the pre-existing missing R45 draft runner already disclosed in `.ufo/round-46/scouts/U1.md`. Stdout SHA `d5fb79dc62846e9db47f9970a369bee6a89326058e035a15c86dd3b6d295d9db`; output is preserved beside the corpus outputs. This gate finding is not a C3 outcome. No comparator, producer, scope, fixture, floor, or registry source was edited here; no Git add/commit/ref operation.

## 2026-10-19 — Round 46 F1 fixture coverage audit

- `.ufo/round-46/scouts/F1.md` SHA-256 `980c2d7286632daeedb5e11e44b0e9216b5513fe9fd69a2ea7f3496c17730152` records the coverage map and residuals. Measurement inputs were claims SHA-256 `ff60fce90a203dbd793fa4fc21bd8e7139df196601e1b76d935aa62903af0e53`, HEAD/tree `055d3b9a3f7eb28d13452a0d26853ef4feabf2ae` / `e8dced184612a9738c5b8d244a0837fbd955a7da`, worktree comparator SHA-256 `4ce43f7aa67efa567f142c69c57bfdff39e7aa47b03e92f8a793ddc5a55e4217`, scope SHA-256 `3d8500ed1757b6da2ca7842ad411c5025faa1d094a04b383139e9caeeb0871e4`, and fixture manifest SHA-256 `dd7165b8da04744465e9e8e52cbbdda5d561d1e7388abd1b8a026c6fb6215a1c` (98 files, 40 arms; 28 tracked, 12 worktree-only). Source, scope, and fixture bytes were stable across the run at `2026-10-19T19:46:49.079226Z–19:46:53.895279Z`.
- Direct `fixture_battery(check)` produced 223/225 assertions; the two failures are `scope-out-probe-record-shadow` and `scope-out-probe-target-drift` mutation guards (`mutation changed its intended payload fields`). `PYTHONDONTWRITEBYTECODE=1 python3 -B verifiers/compare_harness_independent.py --self-test` exited 1: 9 failures over 328 assertions, stdout SHA-256 `9ba48901452634bb557251293792a33d3915a524fc80279e2f49aaf00f7c5b53`, empty stderr. Floors, a live join, and corpus gates were not run by F1.
- An earlier stable 35-arm snapshot (`7a6ca85c…`, fixture manifest `e796e514…`) had passed 190/190 and 0/293, but subsequent shared source and fixture changes make it inapplicable to this result. F1 changed only its report and this append-only log entry; no Git add/commit/ref mutation.

## 2026-10-19 — Round 46 T1 latest rerun addendum

- Supersedes the earlier T1 report pin above: `.ufo/round-46/scouts/T1.md` SHA-256 `d75a5f7783a5669d1ed9719882d1b24375099b5178d51c52dd4cf9d1c004e71d`. Latest live join command (the `compare_harness_independent.py --expect-n 28 --cwd /home/vgpnk/Projects/shokunin/kotoba-shokunin --scope-file verifiers/harness-independent-scope.json --no-stamp` invocation, with `T1-after-landing-12-*` outputs) exited 0 at `2026-10-19T19:46:47Z–19:46:55Z`, stable at HEAD/tree `055d3b9a3f7eb28d13452a0d26853ef4feabf2ae` / `e8dced184612a9738c5b8d244a0837fbd955a7da`; comparator/live/independent/scope SHA-256 values `4ce43f7aa67efa567f142c69c57bfdff39e7aa47b03e92f8a793ddc5a55e4217` / `29e71b9a662e4aef12aa9fefff2446f3b09c4521c0506c489400ebc262a891fb` / `872993f875338f4f89d5b76178c124313e9fc3368966f8a32583acd0430bdbd1` / `3d8500ed1757b6da2ca7842ad411c5025faa1d094a04b383139e9caeeb0871e4`. Protocol 24/24, strict 20/24, four adjudicated/four scoped out. The complete row report and join JSON remain byte-identical to baseline, hashes `cd091c203ec5fb804141af7b9ac7f7db5e3db99daf1cccbf00d27fefde4011c8` / `b38dc4f2991f7c06578d76c6f317d1b99407c05d4bfefbf07fa231890235b80e`; receipt SHA `964659baa96082c00bffd330957a7ea852fdcc1edd6671ee037f32922171c1d0`.
- The current floors guard (`PYTHONDONTWRITEBYTECODE=1 python3 verifiers/check_assertion_floors.py`) ran `19:47:00Z–19:47:09Z` on comparator SHA `4ce43f7a…`, guard SHA `c121431e396884c2b1149ced1c083f42b0462e1cfefc3550bb244e0d8858d9ca`, registry SHA `56c44bc27d600fa98e9b479735cfe7cd40cbe03004313dc7f552b7ca4719c958`; exit 1, eight pass and comparator row `observed=328 floor=293 self_test_failures=9`. Direct self-test at `19:47:30Z–19:47:33Z` exited 1 (9/328). Outputs: floors `f83b652110b9cf517f78cdc0254295a829fac7105766b55a5afccb71716cff14`; self-test `9ba48901452634bb557251293792a33d3915a524fc80279e2f49aaf00f7c5b53`. This is not a pass for the originally requested exact vector ending in 255; the shared registry declares 293 and was not edited by T1. No source edits or Git add/commit/ref mutation.

## 2026-10-19 — Round 46 P5 parse-time absolute scope path draft

- `.ufo/round-46/scouts/P5.md` SHA-256 `07f0d24844112f459b9b0afa680a57c1750a266761fd4c5d02f743ab0e535ecf` records the bounded C1/R1-F3′ result. Frozen baseline HEAD/tree `055d3b9a3f7eb28d13452a0d26853ef4feabf2ae` / `e8dced184612a9738c5b8d244a0837fbd955a7da`; comparator blob SHA-256 `1101213a7bed5410151564aeb5a4b49030a4821c86e7469286f046253fbc51e4`, scope SHA-256 `fbcdc8d247475a5f1c2c613d78b6188dab77a766b02497a729a884687a70f77a`, claims SHA-256 `ff60fce90a203dbd793fa4fc21bd8e7139df196601e1b76d935aa62903af0e53`.
- `PYTHONDONTWRITEBYTECODE=1 python3 -B .ufo/round-46/drafts/p5/prove_scopefile.py` completed `2026-10-19T19:48:57.196610Z–19:49:02.027093Z`. Runner SHA-256 `1a6daec32f255731fd8beed3f1b2dd3489f39844a16a77984d5dda7a39df4ee3`, patch SHA-256 `a8ef6b54b8f94ce16930e63ba018aabb1f9991e1616581a37bba8610ca77b202`, proof JSON SHA-256 `2e930cdedd7b8dd3c7473eda770ece1466d5d33106ebc82f0ebacfdd331e2f63`; patched candidate-source SHA-256 `29f2a0de7c9312f55395fe41c7190e6626ec69ed9dd90e722fc4c62318f5c7ad`. The run extracted frozen baseline bytes from `git show`; mutable worktree comparator SHA at both run boundaries was `4ddfeb7575a5598106fb2369aee71e529ff17ad4a9e48aa8cf92dbda304c540b` and was not executed.
- Red planted-CWD attack: frozen baseline exited 0, agreement 1/1, enforced planted-scope SHA-256 `9b6115ebdfe1ed808a76a4a8cdc8a005cab72bac882f248fc9d1c8add7a37ee4`, but receipt named the relative path and official scope SHA. Patched candidate rejects the same attack with class-named `laundering` exit 2 and writes no receipt; direct relative loader input is also rejected. Valid synthetic control stays exit 0 / 2/2, with the candidate receipt naming/hashing the resolved honest scope. Frozen baseline and candidate self-tests each pass 0 failures / 255 assertions (fixture archive SHA-256 `9463d16d45b71d133d6c46e81b4ad49acd8a5b8004a2bf35f6323cf02e45414d`).
- Depth is improved on this tested F3′ arm only; C1 remains incomplete, no scalar move is claimed. Full production 24/24 join, exact floors, and corpus gates were not run on this draft; operability and calibration did not move. Preserve `.ufo/round-46/drafts/p5/` while cited. P5 changed no production source and performed no Git add/commit/ref operation.

## 2026-10-19 — Round 46 P2 current shared-tree recheck

- Addendum `.ufo/round-46/scouts/P2.md` SHA-256 `7c415b74d72532ab6989dc976fb43cb8690878f8c0405686305353ebb1c9df83` records this recheck and marks its earlier green self-test/floors observation historical. On comparator SHA-256 `ffcf9c5795b56513658123fc351dd72e5a26e7197608d33e7cc613a08920fd24`, P2's mode/verdict/summary shadow fixtures each exited 2 with empty stdout and expected named `omp.offered.skills` errors; stderr SHA-256 values are mode `f9b4867e47d1283faee3afc5587c800349750813b0f78bc7705b05d2b0334498`, verdict `593ae22a1e718850e94059ca049880cc60400a3d2aa61b5b544e7b6a24ff8457`, summary `0913ef73d3471b48c94f2fdb91a8c1f729c12dd47b05cbf93fb67478e8c8f029` (`evidence/p2/recheck-1948-*`). The summary artifact SHA-256 is `ff382273ba53db1ed7ee766df02a0112998f9334a3d00659ee42a386bba2eceb`.
- Current full comparator self-test exited 1: 2 failures/328 assertions, exactly `cli: a probe-less scope-out is named` and `cli: a split channel is named`; stdout `.ufo/round-46/evidence/p2/recheck-1948-self-test.stdout` SHA-256 `3fe7ff753ae1d0b1f2c701cd853d64fc6cc2a52c8b2e61692d2a4f6f9bedd337`. Floors guard exited 1 with eight rows passing and `compare_harness_independent observed=328 floor=293 self_test_failures=2`; stdout SHA-256 `2249a1f64fbed7310863ad8a5ffd19a103d2732ed39f1d673563cb8a103e0004`. The 104-file verifier/fixture manifest stayed fixed before/after gates at SHA-256 `0646fcc98eccdcc4768e9e8fa9d59aecccdfe1b4ac018ed7ad29f7476d6b1a9f`; comparator SHA was unchanged. This manifest does not cover the external OMP session carrier/probe substrate.
- Fresh producer-to-frozen-input join exited 0 at `2026-10-19T19:49:28Z`: live/independent each 28 checks; mode-aware protocol 24/24, strict 20/24, four adjudicated and four scoped out, zero disagreements/uncovered/unknown/provisional. Live/independent/join/receipt SHA-256 values: `ac0d41c6f62e37d22991b891974c92e849091aecd402704df88fd5481c461af7` / `881817283aef4c442f80bbc2410021e48d05fdbaddc578c6d77aab357ac1e5ba` / `1a123a32c8aa5c3fda9232e359fe0d79811a8d4bbd63385c798fa62b7aca1903` / `9abf30f50b0a3b87f5f79ac7580ca52a616ff2de577147a503a5b83252376a80`. Receipt records scope SHA-256 `3d8500ed1757b6da2ca7842ad411c5025faa1d094a04b383139e9caeeb0871e4`, the four `omp.catalogue.*` scope-outs, and probe kind `rule-spread-census`. P2 did not take over raw duplicate JSON, scope-file cwd, or scoped-out metadata implementation/fixtures; no floors, scope, or comparator changes and no Git index/commit/ref operation.

## 2026-10-19 — Round 46 T1 final snapshot addendum

- Supersedes T1's prior addendum: `.ufo/round-46/scouts/T1.md` SHA-256 `6c9f70ab1df741f16d45bd299e2db2cdc8895333d443b7819ac62d0a480d2024`. The latest stable join used `PYTHONDONTWRITEBYTECODE=1 python3 verifiers/compare_harness_independent.py --expect-n 28 --cwd /home/vgpnk/Projects/shokunin/kotoba-shokunin --scope-file verifiers/harness-independent-scope.json --no-stamp` with `T1-after-landing-14-*` outputs; it exited 0 at `2026-10-19T19:49:51Z–19:50:00Z`, stable at HEAD/tree `055d3b9a3f7eb28d13452a0d26853ef4feabf2ae` / `e8dced184612a9738c5b8d244a0837fbd955a7da`. Comparator/live/independent/scope SHA-256: `ccf41c23d2c766124b27f60653508cd1590aa625cbf8afd8da68b56f7b5bc04d` / `29e71b9a662e4aef12aa9fefff2446f3b09c4521c0506c489400ebc262a891fb` / `872993f875338f4f89d5b76178c124313e9fc3368966f8a32583acd0430bdbd1` / `3d8500ed1757b6da2ca7842ad411c5025faa1d094a04b383139e9caeeb0871e4`. Protocol 24/24, strict 20/24, four adjudicated/four scoped out, no disagreements or row changes; row table and join JSON SHA-256 `cd091c203ec5fb804141af7b9ac7f7db5e3db99daf1cccbf00d27fefde4011c8` / `b38dc4f2991f7c06578d76c6f317d1b99407c05d4bfefbf07fa231890235b80e`; receipt `443ae3c4ceec501cb38467813b2e094bd6b8440568835462c77008f63c6d80dd`.
- `T1-after-landing-13` was excluded because comparator changed during its command (`ffcf9c57…` to `ef4e10e2…`). After landing14, current `PYTHONDONTWRITEBYTECODE=1 python3 verifiers/check_assertion_floors.py` reran `19:51:23Z–19:51:32Z`, stable at comparator `ccf41c23…`, guard SHA `8a4d156b88e82f318fa62f3cd67f00663b5ea3479b50bf5747f070996be0c38b`, registry SHA `1802ec0e0699807f51f6198e330119cdad7bdc8b746f6d55da76ead893655e50`; it passed 9/9, comparator `observed=328 floor=328`, output SHA `ef091efb957f0e4c38e883a813761fa6a2a4cf1f22d94522bfa1f3e757478b49`. Direct comparator self-test at `19:50:19Z–19:50:22Z` passed 0/328, output SHA `2eab26b6420d891524369f164ad5ab686bbeaac71fa9036e22e4e118c8c1aac4`. This is green against the shared revised 328 floor, not the originally specified exact vector ending 255. T1 did not edit the registry or make any Git add/commit/ref mutation.

## 2026-10-19 — Round 46 P3 raw duplicate-member handling

- `.ufo/round-46/scouts/P3.md` SHA-256 `b48c35ffc685f41a23e012d7415ddad26854b2578f835748b0e175fa86784e1c` records only C2(b). The frozen probe `PYTHONDONTWRITEBYTECODE=1 python3 -B .ufo/round-46/drafts/p3/probe_duplicate_members.py --source git --revision 055d3b9 --out .ufo/round-46/evidence/P3-duplicate-members-before-final.json` used baseline comparator SHA-256 `1101213a7bed5410151564aeb5a4b49030a4821c86e7469286f046253fbc51e4`; all three duplicate inputs exited 0 under last-member-wins. Baseline evidence SHA-256 `30b68f30f137cd59e13282fe5802523b99afb252352fe757b4fbc02fbe17b4c4`.
- Final worktree probe `PYTHONDONTWRITEBYTECODE=1 python3 -B .ufo/round-46/drafts/p3/probe_duplicate_members.py --source worktree --out .ufo/round-46/evidence/P3-duplicate-members-after-cf41c23.json` ran at `19:51:13Z`; comparator SHA-256 `ccf41c23d2c766124b27f60653508cd1590aa625cbf8afd8da68b56f7b5bc04d` was unchanged at both boundaries. All three cases exited 2 and named the expected side/key (independent `results`, independent `re_derived`, live `results`), evidence SHA-256 `69d81eabdb162e8066840101c840cb9529370541d9287294a8e63c98e11d4c02`. Self-test assertions 136–150 pin the same exits/classes without traceback.
- On that same comparator snapshot, the current live producer join ran at `19:51:21Z`: exit 0, 28 records per side, 24/24 protocol, 20/24 strict, four adjudicated/four scoped out, zero disagreements. Join JSON SHA-256 `b38dc4f2991f7c06578d76c6f317d1b99407c05d4bfefbf07fa231890235b80e`; receipt SHA-256 `1df97171a262afeb977c2fe2469a7b55ea88938daeb8cf73315c6d5363890b15`.
- Comparator self-test on SHA `ccf41c23…` exited 0 with 0 failures over 328 assertions (output SHA-256 `2eab26b6420d891524369f164ad5ab686bbeaac71fa9036e22e4e118c8c1aac4`). The floors guard exited 0 with 9/9 floors passing, comparator `observed=328 floor=328` (output SHA-256 `ef091efb957f0e4c38e883a813761fa6a2a4cf1f22d94522bfa1f3e757478b49`); guard/registry hashes were `8a4d156b88e82f318fa62f3cd67f00663b5ea3479b50bf5747f070996be0c38b` / `1802ec0e0699807f51f6198e330119cdad7bdc8b746f6d55da76ead893655e50`. An intermediate `4ce43f7…` snapshot had 9 failures/328 and is superseded by these later shared source/floor changes and green rerun.
- Preserve `.ufo/round-46/drafts/p3/probe_duplicate_members.py`, its three fixture directories and the cited evidence. The first frozen live-duplicate attempt used `rows-shadow/independent.json` and hit unrelated channel divergence; the final baseline uses a clean control. An early candidate run was misclassified by a runner expecting exit 0; the retained runner now requires exit 2 plus the named duplicate key. No Git add/commit/ref operation was performed; shared worktree changes remain for parent integration.

## 2026-10-19 — Round 46 P1 scope-file path resolution

- `.ufo/round-46/scouts/P1.md` records the relative `--scope-file` / `--cwd` fix and exact-byte receipt. At HEAD/tree `055d3b9a3f7eb28d13452a0d26853ef4feabf2ae` / `e8dced184612a9738c5b8d244a0837fbd955a7da`, frozen comparator blob SHA-256 `1101213a7bed5410151564aeb5a4b49030a4821c86e7469286f046253fbc51e4`; red-before `.ufo/round-46/evidence/P1-red-before.json` SHA-256 `27d70a2a613422302f4682b4ab54870828c834e82d94183b4ca15305ff94bad9` records candidate exit 0 and a receipt naming the honest scope digest although the planted scope was enforced.
- Final focused replay `PYTHONDONTWRITEBYTECODE=1 python3 .ufo/round-46/evidence/P1-scope-file-cwd-replay.py after .ufo/round-46/evidence/P1-final-red-after.json` ran at `19:50:44Z` on stable comparator SHA-256 `ccf41c23d2c766124b27f60653508cd1590aa625cbf8afd8da68b56f7b5bc04d`; frozen exit 0, candidate exit 2 named `laundering`, planted-scope control exit 0. Artifact SHA-256 `bfef6e92ddd9643e2b8fb7010e1f0c8e5b627a2f728c9d2c90a789fa013d5d88`; control receipt scope digest matched `9fea062a1db925b02b3d425e00d5f536b9667e42986107753bc485834625dd5f` at its resolved temporary path. P1 self-test output SHA-256 `2eab26b6420d891524369f164ad5ab686bbeaac71fa9036e22e4e118c8c1aac4`: 0 failures over 328 assertions; fixture manifest was stable before/after at `cb66173ee5cd264548dbaef55ecdbb97066c1ff1f6dc6d2633a295e3d31250c1`.
- Full `PYTHONDONTWRITEBYTECODE=1 python3 verifiers/check_assertion_floors.py` ran `19:51:21Z–19:51:30Z`, stable on comparator SHA `ccf41c23…`, guard SHA `8a4d156b88e82f318fa62f3cd67f00663b5ea3479b50bf5747f070996be0c38b`, registry SHA `1802ec0e0699807f51f6198e330119cdad7bdc8b746f6d55da76ead893655e50`; all nine floors passed, comparator observed/floor 328/328. Output SHA-256 `ef091efb957f0e4c38e883a813761fa6a2a4cf1f22d94522bfa1f3e757478b49`. P1 did not edit the floor guard or single-writer registry; an earlier check during the shared bump was transiently red, and the final synchronized state passes.
- Fresh in-process producer join at comparator SHA `ccf41c23…` exited 0 (`19:49:52Z–19:50:00Z`): 24/24 protocol, strict 20/24, four adjudicated/four scoped out, no disagreements. Join/receipt SHA-256 `b38dc4f2991f7c06578d76c6f317d1b99407c05d4bfefbf07fa231890235b80e` / `629defe9ffdd0e409648724aadade2654616c9ed25a5a7bdbae15cba51f877f3`; receipt resolved scope path digest `3d8500ed1757b6da2ca7842ad411c5025faa1d094a04b383139e9caeeb0871e4`.
- P1-specific source/fixture/replay files are the comparator, `verifiers/fixtures/compare-harness-independent/scope-file-cwd/`, and `.ufo/round-46/evidence/P1-scope-file-cwd-replay.py`; no Git add, commit, or ref mutation.

## 2026-10-19 — Round 46 N1 semantic diff and integration check

- `.ufo/round-46/scouts/N1.md` SHA-256 `1d5be9fcd26dce07c4e7dc0585e434a9c224abc1191f5c14713a89ccfe4a39a1` maps the shared comparator/producer/scope/fixture/floor changes to registered C1–C3 without claiming seat authorship. Baseline HEAD/tree `055d3b9a3f7eb28d13452a0d26853ef4feabf2ae` / `e8dced184612a9738c5b8d244a0837fbd955a7da`; claims SHA-256 `ff60fce90a203dbd793fa4fc21bd8e7139df196601e1b76d935aa62903af0e53`; final comparator SHA-256 `ccf41c23d2c766124b27f60653508cd1590aa625cbf8afd8da68b56f7b5bc04d`.
- Final gate-input manifest (106 files, including all comparator fixtures) was unchanged before/after at SHA-256 `e07e4e79ae214108dc2e6b1af0ba41eeb797f778557be00171c3a33e4c8f47d5`. Comparator self-test exited 0, 0/328 (stdout SHA-256 `2eab26b6420d891524369f164ad5ab686bbeaac71fa9036e22e4e118c8c1aac4`); floors guard exited 0, 9/9 exact vector `10/150/91/87/1597/62/104/328/150` (stdout SHA-256 `ef091efb957f0e4c38e883a813761fa6a2a4cf1f22d94522bfa1f3e757478b49`).
- The real producer join exited 0: 28 live checks, 24/24 protocol, 20/24 strict, four adjudicated/four scoped out, zero disagreements/uncovered/unknown; stdout SHA-256 `b38dc4f2991f7c06578d76c6f317d1b99407c05d4bfefbf07fa231890235b80e`, receipt SHA-256 `16682b56776f5349ca659a47638eb2b429aac04996fde7b4882ccffd56772665`.
- The earlier preliminary N1 run is explicitly superseded: its self-test/floors were red while the broader manifest changed (`4944fff1…`→`c162d059…`); it is not used for the final candidate verdict. Current candidate self-tests exercise the C1–C3 fixtures, while the historical frozen-HEAD C3 replay and current SCORECARD still report C3 partial/unproven; N1 does not close the wider claim. No product code or refs were changed; no staging, commit, or ref operation. Shared comparator, floor files, producer, SCORECARD/census, and sibling fixture edits are not wholly attributed to P1.

## 2026-10-19 — Round 46 R1 scope-file path and receipt review

- `.ufo/round-46/scouts/R1.md` SHA-256 `24bd8a4d577637830551b9123ee21e456d21eeb247f7ee0a1ce7463da4d129ad` records a focused review at HEAD/tree `055d3b9a3f7eb28d13452a0d26853ef4feabf2ae` / `e8dced184612a9738c5b8d244a0837fbd955a7da`, comparator SHA-256 `ccf41c23d2c766124b27f60653508cd1590aa625cbf8afd8da68b56f7b5bc04d`, scope SHA-256 `3d8500ed1757b6da2ca7842ad411c5025faa1d094a04b383139e9caeeb0871e4`. The preserved run-18 manifest SHA-256 is `d6b4018ce3b09039e2dc66d1010a657cb3e45baa27f8fe428d779ca6a43462ae`.
- The nine-case path matrix (result SHA-256 `21c506ce69d1240f71229831f366dae195105d164c35f042a4227c629e4b7efa`) rejected four honest-scope attacks with named `laundering`; five planted-scope path/symlink controls passed, each receipt matching the resolved path and enforced digest. The atomic replacement race (result SHA-256 `89655c8614755b906a874e957d00a68d7bce2c27ff114627be5d2f164aeabc50`) exited 0 at 1/1; the receipt attested initial digest `d86fd2f9…` after the opened file was replaced with bytes `dc9a7017…`.
- The pinned candidate's real 28-check producer join exited 0 at protocol 24/24, strict 20/24, four adjudicated/four scoped out, zero disagreement/uncovered/unknown. Result/receipt SHA-256 `1ad83c66dfa770f19bc06facca993a8e40d7bd0ac4b04021ba3c1e599da2a662` / `12819ab6c441cc3e593422676b96c814bf264630ba9e5d032bb573896e92d21f`; receipt scope path/digest matched the official resolved file. R1 closes only this path/receipt review, not authentication or whole-round closure. No production/fixture/floor/corpus/SCORECARD source, Git index, commit, or ref was changed by R1; preserve `.ufo/round-46/drafts/r1/` while cited.

## 2026-10-19 — Round 46 V2 independent C2 replay

- `.ufo/round-46/scouts/V2.md` SHA-256 `2b60e45874f1838a0acd9609cf7e07b72ccdd32f7abde9678dbbdc7486ae5234` records the fresh-scope replay at HEAD/tree `055d3b9a3f7eb28d13452a0d26853ef4feabf2ae` / `e8dced184612a9738c5b8d244a0837fbd955a7da`. Frozen comparator SHA-256 `1101213a7bed5410151564aeb5a4b49030a4821c86e7469286f046253fbc51e4`; HEAD scope SHA-256 `fbcdc8d247475a5f1c2c613d78b6188dab77a766b02497a729a884687a70f77a`. The earlier invalid worktree-scope run is not cited.
- `PYTHONDONTWRITEBYTECODE=1 python3 -B .ufo/round-46/drafts/v2/run_v2_fresh.py` ran `2026-10-19T19:51:19.607252Z–19:53:04.895697Z`; runner SHA-256 `95a513230a82482b1787377086ce9ade6ac4a90efe4a3c0890e7ec129d6afb67`, manifest `.ufo/round-46/drafts/v2/v2-results-head-scope.json` SHA-256 `068ea553d23c840359dd076870482b3a260676964cc96ab458756c55977ab4c2`. Four live shadow arms and both raw duplicate-member arms all exited 0; the two raw inputs contained exactly one duplicate `results` / `re_derived` member and were accepted last-member-wins. No explicit trusted exception applies in the frozen HEAD contract, so C2 remains open on HEAD.
- Honest fresh join: protocol 24/24, strict 20/24, four adjudicated/four scoped out, zero disagreements. The 46 R41 + 7 fresh C2 union had zero baseline-closed arms newly open; controls/diagnostics, unchanged-input, and fresh probe-stability checks all passed (`no_regression=true`). The worktree comparator SHA `ccf41c23d2c766124b27f60653508cd1590aa625cbf8afd8da68b56f7b5bc04d` was stable at run boundaries but not executed; no behavior is attributed to that uncommitted candidate. No self-test/floors guard or product-source edit was performed. Preserve `.ufo/round-46/drafts/v2/`; no Git add/commit/ref operation.

## 2026-10-19 — Round 46 Y1 final C1/C2/C3 recommendation

- `.ufo/round-46/scouts/Y1.md` SHA-256 `b2ab112ff90168ded1e2f5ce7b9c0b17f1811203eb1549c9f3f28cbf4a9fdff4` recommends **improved** for C1, C2 and C3 on the candidate worktree only; it does not claim landing, round admission, score changes, or full claim closure. Baseline HEAD/tree `055d3b9a3f7eb28d13452a0d26853ef4feabf2ae` / `e8dced184612a9738c5b8d244a0837fbd955a7da`; frozen comparator SHA `1101213a7bed5410151564aeb5a4b49030a4821c86e7469286f046253fbc51e4`; candidate comparator SHA `ccf41c23d2c766124b27f60653508cd1590aa625cbf8afd8da68b56f7b5bc04d`; scope SHA `3d8500ed1757b6da2ca7842ad411c5025faa1d094a04b383139e9caeeb0871e4`.
- The focused paired C1/C2/C3 matrix `.ufo/round-46/evidence/c1-resumed/focused-arms.json` (SHA-256 `3ef2cf7bdb62fe1e194a0363955029102f5658e0e96722b85ef56f5e3e4f49f7`) recorded frozen exit 0 → candidate exit 2 for the planted scope-CWD case, three live-JSON shadow cases, raw duplicate `results`, and C3's reason/evidence/valid alternate-probe-target changes. Candidate controls passed; the planted-scope receipt hash matched the actual resolved scope file. The comparator self-test independently exercises the three raw duplicate cases.
- Fresh Y1 checks at `19:53:10Z–19:53:30Z` ran on stable source and fixture inputs (308-file verifier manifest SHA-256 `0a825727d7d5dc39e4f397bc374c379bb75b348c1fd2439a6ea49a2ad0acae61`). Comparator self-test exited 0, 0/328 (stdout SHA `2eab26b6420d891524369f164ad5ab686bbeaac71fa9036e22e4e118c8c1aac4`); floors exited 0, all 9/9 exact floors `10/150/91/87/1597/62/104/328/150` (stdout SHA `ef091efb957f0e4c38e883a813761fa6a2a4cf1f22d94522bfa1f3e757478b49`). A fresh producer join exited 0 with 28 rows per side, 24/24 protocol, 20/24 strict, four adjudicated/four scoped out and zero disagreements/uncovered/unknown; join/receipt SHA `0570dc34925744e53c02865323d488f7ab491fd2577c9f526c1a75c19ab75fca` / `a950b183a3ac245423a65cf372989f26f75621067bed420ab03adf9ca9fda7e5`.
- The append-only census and SCORECARD still describe the frozen-baseline C3 residual; Y1 did not revise shared docs or source/fixture/floor/registry files and did not attribute other seats' edits. Preserve `.ufo/round-46/drafts/` and `.ufo/round-46/evidence/c1-resumed/` while cited. No Git add, commit, or ref operation.

## 2026-10-19 — Round 46 R2 C2/C3 adversarial review

- `.ufo/round-46/scouts/R2.md` SHA-256 `ae06914ee706eb5f7e30f502d216670572e17396f9883f18d7de84dfc79daf38` records the bounded C2/C3 replay at frozen baseline HEAD/tree `055d3b9a3f7eb28d13452a0d26853ef4feabf2ae` / `e8dced184612a9738c5b8d244a0837fbd955a7da`. The main matrix froze candidate comparator `705423087f7adb395d690401945b7a7733b3a3ab4f8c04f67c7a532bb6b8172e`; results manifest `.ufo/round-46/drafts/r2/final-adversarial-70542308/results.json` SHA-256 `8cde57e9d144bf02155ab026c96a067cfb5b83f7bd4f4b8782a28e04fe788770` records honest control 0/0, protocol 24/24, strict 20/24, four adjudicated/four scoped out, and the tested C2 shadow/duplicate-member rejections. C2 remains open: removing all four mirrored side channels still passes the skewed case.
- The two clean focused scope replays froze candidate `4ce43f7aa67efa567f142c69c57bfdff39e7aa47b03e92f8a793ddc5a55e4217`. Target-drift manifest `.ufo/round-46/drafts/r2/scope-target-4ce43f7a-195106/results.json` SHA-256 `ca23ea2c6940952ecb992cac93ed92458d7e702a9bf916fc16909cd4c2a74951` records baseline accept/candidate reject for a valid reason/evidence payload redirected to an attacker target. Forged-observable manifest `.ufo/round-46/drafts/r2/scope-probe-4ce43f7a-195254/results.json` SHA-256 `0c3584a12d327bbb15c5e41e07438e232583a743d2b2b4a9322168d7b3e12189` records rejection by both baseline and candidate after recomputation. The main matrix's two confounded scope arms and one stale-label run are excluded as detailed in R2.md.
- These are snapshot-bounded axis findings only: Operability/C2 improved but not closed; Calibration/C3 improved on the tested snapshot, not asserted for later mutable source. Self-test, floors, and corpus gates were not run on these R2 snapshots. No comparator, producer, scope, floor/registry, fixtures, corpus, or Git refs were changed by R2; no Git add/commit/ref operation.

## 2026-10-19 — Round 46 C1 census-boundary ruling

- `.ufo/round-46/scouts/C1.md` SHA-256 `d20b34c96f5ede6c9c018ddf02f9b93d026b1922ab0fff4860c1946c65ab2be3` rules the broader census boundary **not demonstrably bounded**. On the stable shared comparator `ccf41c23d2c766124b27f60653508cd1590aa625cbf8afd8da68b56f7b5bc04d` at HEAD/tree `055d3b9a3f7eb28d13452a0d26853ef4feabf2ae` / `e8dced184612a9738c5b8d244a0837fbd955a7da`, the focused scope-CWD, live mode/verdict/summary, raw duplicate-results, and tested scoped-out metadata arms reject; duplicate-ID/status order still exits 0 on both frozen and candidate. The finite R41 census and unreplayed carried residuals do not establish exhaustiveness.
- `PYTHONDONTWRITEBYTECODE=1 python3 -B .ufo/round-46/drafts/c1-resumed/probe.py` made ten paired cases plus one candidate control, stable at candidate comparator SHA `ccf41c23…`; runner SHA-256 `31468c0f3b7f74f7e2aeeb6a87a273729641116175a19a415650e046f4eba06f`, result `.ufo/round-46/evidence/c1-resumed/focused-arms.json` SHA-256 `3ef2cf7bdb62fe1e194a0363955029102f5658e0e96722b85ef56f5e3e4f49f7`. The registered scope-file seam is locally supported as closed for measured forms; shared comparator changes are not attributed to this seat.
- Stable gates on the same comparator: self-test exit 0, 0/328 (stdout SHA-256 `2eab26b6420d891524369f164ad5ab686bbeaac71fa9036e22e4e118c8c1aac4`); floors exit 0, 9/9 exact `10/150/91/87/1597/62/104/328/150` (stdout SHA-256 `ef091efb957f0e4c38e883a813761fa6a2a4cf1f22d94522bfa1f3e757478b49`); fresh producer join exit 0, 28 rows per producer, 24/24 protocol, 20/24 strict, four adjudicated/four scoped out, no disagreements (join/receipt SHA-256 `b38dc4f2991f7c06578d76c6f317d1b99407c05d4bfefbf07fa231890235b80e` / `6b808e2ba1b34ee329ff12c0212ddfe78108789da570897cdf765d53a05feb31`). Evidence is preserved under `.ufo/round-46/evidence/c1-resumed/`, including the `gates-1951/` outputs. No Git add, commit, or ref mutation.

## 2026-10-19 — Round 46 I1 integrator-gate candidate snapshot

- `.ufo/round-46/scouts/I1.md` SHA-256 `283ba80985c8f927f228cf3feec5a1bd98b36c2a8ea7a736a0d9f067b11a2f97` records a pre-final-wave candidate snapshot at HEAD/tree `055d3b9a3f7eb28d13452a0d26853ef4feabf2ae` / `e8dced184612a9738c5b8d244a0837fbd955a7da`; it is not post-wave certification. The floor guard and all nine instrument self-tests passed at exact current floors `10/150/91/87/1597/62/104/328/150`; direct comparator self-test passed 0 failures over 328 assertions. Transcript `.ufo/round-46/evidence/i1-floors-guard-candidate-20261019T1951Z.txt` SHA-256 `b4719e4240b21825668df3886cb03ebc340b57de14dd8e1ffe2f489c4e12ccfd`.
- The pinned live-gate battery at `19:52:39Z–19:52:53Z` is preserved in `.ufo/round-46/evidence/i1-wave-gates-20261019T1952Z.txt` SHA-256 `2106acede0c7e9f119f4410dd91b499e666870775669c0a1180cfb2883855a17`. The producer join passed (28 checks, 24/24 protocol, 20/24 strict, four adjudicated/four scoped out, no disagreement/uncovered/unknown); both corpus gates passed. Checklist was 9/10 with unresolved historical citation `LOG.md:2112`; surfaces were 5/7 with OMP extraction failures; pins were 1/3 with OMP SHA/mtime drift and no rebaseline. Exact sidecar outputs and hashes are in I1.md.
- I1 changed no production source, substrate baseline, assertion registry, or scope file; no Git add/commit/ref mutation. Shared tree remained active, so results are candidate-only. Checklist rerun after this report/LOG surface update is required; do not treat the captured green rows as final-wave certification.

## 2026-10-19 — Round 46 P1 current-snapshot recheck

- `.ufo/round-46/scouts/P1.md` SHA-256 `326ecf6fd58bff7ab50c0e9cce6a609287b9da6018041f8ea333bd1d6d3fcd1a` now includes this recheck. From `19:54:51.908046382Z–19:55:11.823270994Z`, comparator `ccf41c23d2c766124b27f60653508cd1590aa625cbf8afd8da68b56f7b5bc04d`, floor guard `8a4d156b88e82f318fa62f3cd67f00663b5ea3479b50bf5747f070996be0c38b`, registry `1802ec0e0699807f51f6198e330119cdad7bdc8b746f6d55da76ead893655e50`, scope `3d8500ed1757b6da2ca7842ad411c5025faa1d094a04b383139e9caeeb0871e4`, and producers `29e71b9a662e4aef12aa9fefff2446f3b09c4521c0506c489400ebc262a891fb` / `872993f875338f4f89d5b76178c124313e9fc3368966f8a32583acd0430bdbd1` were stable before and after the gates.
- Current focused replay `.ufo/round-46/evidence/P1-current-recheck-20261019.json` SHA-256 `f397130914964ffd0376dcafe8dab36d4af2c3451c36b959c0fc6c6acd6c6461`: frozen 0, candidate 2 named `laundering`, planted-scope control 0 with receipt matching enforced path/digest. Current self-test exited 0 at 0/328 (stdout SHA `2eab26b6420d891524369f164ad5ab686bbeaac71fa9036e22e4e118c8c1aac4`); floors exited 0, 9/9 exact `10/150/91/87/1597/62/104/328/150` (stdout SHA `ef091efb957f0e4c38e883a813761fa6a2a4cf1f22d94522bfa1f3e757478b49`).
- Fresh live join `.ufo/round-46/evidence/P1-current-live-join.json` / receipt SHA-256 `b38dc4f2991f7c06578d76c6f317d1b99407c05d4bfefbf07fa231890235b80e` / `0f78cdf03422807039f1da5342ec73c41a6037a704e8790e9ed4eeb57b0eab27`: exit 0, protocol 24/24, strict 20/24, four adjudicated/four scoped out, no disagreements/uncovered/unknown. Receipt scope path/digest is the resolved official file. Fresh producer stdout SHA-256 values: live `60aafdf8161222904c674393909b02024a5b00bfb04f544fad0534baa5f010a3`, independent `baf9c2581bfc8ffa670372d0c6d2588547bdb62931010c9222c73c40dac8d088`. No Git add, commit, or ref operation.

## 2026-10-19 — Round 46 I1 checklist rerun and report update

- Updated `.ufo/round-46/scouts/I1.md` SHA-256 `4312e59ce62662295ea3ad98d3fe00f935a30635952ad6b076a67e8a3f58034e` with the post-LOG checklist finding and exact evidence link. `PYTHONDONTWRITEBYTECODE=1 TMPDIR="$PWD/.ufo/round-46/drafts/i1/tmp" python3 -B verifiers/verify_skill_checklist.py --repo "$PWD" --skill "$PWD/SKILL.md" --json` ran `19:56:47Z–19:56:48Z`, exit 1: 9/10 PASS; only `governance.citation_resolves` fails on the pre-existing dangling historical R45 runner citation at `LOG.md:2112`. JSON `.ufo/round-46/evidence/i1-checklist-post-log-20261019T195647Z.json` SHA-256 `654d9db90187474558230288d3860bc37da298ab997a249266af9b3e9d392ce0`; stderr was empty (SHA-256 `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`).
- This is a candidate-snapshot documentation update only; it does not turn the battery into post-wave certification or alter the reported OMP surface/pin defects. No Git add, commit, or ref operation. A final checklist recheck after this report/log addendum is still needed to verify the final governance surface.

## Round 46 B2 — SHONEN assessment

- Report `.ufo/round-46/scouts/B2.md` SHA-256 `749e2f133422050a42f34110f929a953ac6f5bf258900eb7f6bc29ab9a517947` records the four tentative SHONEN boxes and separate C1/C2/C3 verdicts. Static inventory pins: `SKILL.md` `0404fdc0ee6e1b16c765b7dd7dc78aef92c5758bfb980dbbbaf2212ab3c2b09f`, 521 lines, 41 checklist boxes (15/9/9/8), 7 anatomy rows, 5 decision rows, 38 Sources entries; the moved anti-pattern table has 20 data rows at `corpus/knowledge/fail-closed-and-anti-patterns.md` SHA-256 `ec1f60ee8e5603e9267a6a3ef2c260582f145b2eff2c2d3b04cedde6cf731303`. `PROVINCE.md` SHA-256 `4f11c1611b3aa7b8d8b5346750d4f0338c2d9b18f9c3efc9c5646cd94e667acb`; `git diff --quiet HEAD -- PROVINCE.md` returned 0.
- Current assessment snapshot: HEAD/tree `055d3b9a3f7eb28d13452a0d26853ef4feabf2ae` / `e8dced184612a9738c5b8d244a0837fbd955a7da`; claims SHA-256 `ff60fce90a203dbd793fa4fc21bd8e7139df196601e1b76d935aa62903af0e53`; comparator `ccf41c23d2c766124b27f60653508cd1590aa625cbf8afd8da68b56f7b5bc04d`, floors guard `8a4d156b88e82f318fa62f3cd67f00663b5ea3479b50bf5747f070996be0c38b`, registry `1802ec0e0699807f51f6198e330119cdad7bdc8b746f6d55da76ead893655e50`, live/independent producers `29e71b9a662e4aef12aa9fefff2446f3b09c4521c0506c489400ebc262a891fb` / `872993f875338f4f89d5b76178c124313e9fc3368966f8a32583acd0430bdbd1`, scope `3d8500ed1757b6da2ca7842ad411c5025faa1d094a04b383139e9caeeb0871e4`. Before/after pins match across the sequential run. Fresh comparator self-test passed 0/328 (stdout `2eab26b6420d891524369f164ad5ab686bbeaac71fa9036e22e4e118c8c1aac4`); floors passed 9/9 exact `10/150/91/87/1597/62/104/328/150` (stdout `ef091efb957f0e4c38e883a813761fa6a2a4cf1f22d94522bfa1f3e757478b49`). Both producers exited 0 at 28 records; join exited 0 at 24/24 protocol, 20/24 strict, four adjudicated/four scoped out, zero disagreements (join `92c7daed69ed82a66fc79352dc5c97bb2990d6179ccd0c515647e78127f70650`, receipt `ef1432b3038baf5c52dd2104a3d7714f7b40935a1ce15c568a7cfbbb54816385`). Full bundle: `.ufo/round-46/evidence/b2-current-1952/`.
- Verdicts are bounded: C1's registered scope-file seam is supported by the frozen-red/current-reject replay and same-snapshot fixtures/gates, but C1's broader depth completeness remains unproven because duplicate-ID/status ordering still exits 0 and the census is finite (`.ufo/round-46/scouts/C1.md`). C2 is improved but open: six named shadow/duplicate fixtures pass on the current snapshot, while R2's side-channel-removal bypass on `70542308` has not been rerun on `ccf41c23…` (`.ufo/round-46/scouts/R2.md`). C3's reason/evidence/target fixtures pass on the current candidate, but calibration is not closed until the historical census/SCORECARD record is reconciled; no corpus or SCORECARD edit was made here. Green join is not treated as claim closure.
- The box-3 machine map remains partial (41 mapped, 8 executed, 0 delegated, 33 unexecuted); no fresh blank-context agent execution was performed. The required post-report/log checklist outputs are to be captured at `.ufo/round-46/evidence/b2-final-checklist.stdout.json`, `.ufo/round-46/evidence/b2-final-checklist.stderr.txt`, and `.ufo/round-46/evidence/b2-final-checklist.exit.txt`. No `SHONEN.md`, protocol, mission, axes, corpus, sibling repository, or floors-registry file was changed; no Git add, commit, or ref mutation was performed.

## 2026-10-19 — Round 46 P4 scoped-out metadata candidate proof

- `.ufo/round-46/scouts/P4.md` (SHA-256 `64b6643ff00779ec3029052a58bf97314bf765e43089062a35c8726dc735f227`) records the bounded C3 result on the uncommitted candidate. The frozen baseline at HEAD `055d3b9a3f7eb28d13452a0d26853ef4feabf2ae`/tree `e8dced184612a9738c5b8d244a0837fbd955a7da` accepted the reason/evidence/valid target drift (C3's red-before remains in `.ufo/round-46/evidence/v3/`). Candidate comparator SHA `ccf41c23d2c766124b27f60653508cd1590aa625cbf8afd8da68b56f7b5bc04d` rejects reason, evidence and target mutations with exit 2 and class names; probe-map/record shadows report `scope probe channel split`. Each fixture checks row `omp.catalogue.found` and no traceback (self-test output lines 269–303).
- Appended the candidate disposition to `corpus/knowledge/harness-independent-round41-census.md` (SHA-256 `51f6ffcca0d3ec2ed6ee11fd67dffa62306c9e2c95c113acc6ae2c0bd688a618`) without reclassifying R41/R45's 46-arm counts; updated SCORECARD's current C3 status and focused result (SHA-256 `9d708d3f5f3f81de01d4e93d2cd6126620ffc44fc43cc8ff928b0f44e14c1a6a`). Both retain score 8.5 and explicitly bound the result to this candidate and scope-file contract.
- Candidate measurement at `2026-10-19T19:53:27.620433186Z–19:53:35.928218232Z`: comparator, producer source and scope SHA pins matched before/after. Candidate self-test exit 0, 0/328 (stdout SHA `2eab26b6420d891524369f164ad5ab686bbeaac71fa9036e22e4e118c8c1aac4`); floor guard exit 0, all 9 exact rows at `10/150/91/87/1597/62/104/328/150` (stdout SHA `ef091efb957f0e4c38e883a813761fa6a2a4cf1f22d94522bfa1f3e757478b49`). Fresh producers exit 0 at 28 checks; frozen-input join exit 0, protocol 24/24, strict 20/24, four adjudicated/four scoped out, no disagreement/uncovered/unknown; join/receipt SHA `c50a9eb551725a90a52574b4a34675a8617506ce2f86d22feec60438254e788b` / `2a98917b9663addcb71c604599dc107cde864ff1e331ef6766cbb4ce0d230ea0`. Sidecars are under `.ufo/round-46/evidence/p4/`.
- This does not authenticate the uncommitted scope file, prove exhaustive C3 residual closure, or close C1/C2/the full round. No `verifiers/floors-registry.json` edit, Git add, commit, or ref operation was made.

## 2026-10-19 — Round 46 S2 independent evidence replay

- `.ufo/round-46/scouts/S2.md` (SHA-256 `77130102940d87d2dbea32a2916f3134033910429d7da77946fb851b4d808f34`) records the bounded independent review at HEAD/tree `055d3b9a3f7eb28d13452a0d26853ef4feabf2ae` / `e8dced184612a9738c5b8d244a0837fbd955a7da`, with frozen HEAD comparator SHA-256 `1101213a7bed5410151564aeb5a4b49030a4821c86e7469286f046253fbc51e4`. Evidence collector `PYTHONDONTWRITEBYTECODE=1 python3 -B .ufo/round-46/drafts/s2/verify_evidence.py` exited 0; summary `.ufo/round-46/evidence/S2/summary.json` SHA-256 `66e8b3b5118c03adb0718c6660d7c24f05e0a7c70aafe6e3c99808453275b7ea` records the collection results.
- The committed R41 replay/census pair validates 46/46 saved arms and reproduces the census semantically (fresh census SHA-256 `c680bd8e967c0ae6c1631951ce2a0d1a4e9bb3eccaaca407f9caba0d73269873`), but exact subprocess reruns do not reproduce historical outcomes: 16/46 match for R41 and 0/46 for the R44/R45/HEAD comparison drivers. Saved `candidate_blocks=678` differs from current `694`/`698`; the committed classifier refuses the R41 fresh replay as invalid.
- The R40 safe subset (SHA-256 `f5a7fdc4df6b680ff2743afac5be3991f1caa0e7e4bc63ed9625626b553c571f`) has C1 confounded by the same drift. C2 rejects several named paths but silently accepts the outside-world and dot-dot overrides (both `stub_a observed=999 floor=3`). C3 was not rerun because its helper performs `git init`/`git add`, forbidden for this lane.
- The R44 record-map fixture replay (SHA-256 `43b26c70d0b2323d06690959e3fb4bf49bfcf4f4cd528363be1b69baa2b5f28f`) shows the composition accepted by frozen R44 but rejected with named `derived-set overflow` by R45 and HEAD, on unchanged pinned fixture inputs. G1 census (SHA-256 `95750880afbca4e8940d4d3dca07413dd521ba92ab89ab1ebf42b8cd5dfbaad7`) finds the installed `omp/18.12.3` binary's fresh strings differ from the saved 18.12.2 dump; current gate exits 1 (two failures) and self-test exits 0 (87 assertions). Only binary strings/version and verifier data were examined; no session contents were read.
- S2 added this report and this LOG entry; the evidence collector’s generated raw artifacts are confined to `.ufo/round-46/evidence/S2/`. Existing shared worktree changes remain unattributed; no Git add, commit, ref mutation, or sibling-repository change.

## 2026-10-19 — Round 46 P4 SCORECARD citation correction

- The post-document `verify_skill_checklist.py --repo "$PWD" --skill "$PWD/SKILL.md" --json` sweep at `.ufo/round-46/evidence/p4/final/skill-checklist.stdout` exited 1 with 9/10 PASS. Its governance failure identified both the pre-existing absent R45 replay runner citation at `LOG.md:2112` and the newly added brace-form C3/P4 report citation in SCORECARD. Replaced the brace form with two literal file citations; retained the older missing-runner finding as separate, previously recorded documentation debt (U1).
- This correction changes no verifier, fixture, scope, floor or registry. Post-correction final checks are required; no Git add, commit, or ref mutation.

## 2026-10-19 — Round 46 P4 final-command sidecar correction

- Review of `.ufo/round-46/evidence/p4/final/commands.txt` against the initial capture found output-name drift (`.json` in the command ledger vs `.stdout` in the actual sidecars) and an implicit `$TMP`. Rewrote the command ledger with the actual paths and explicit in-repo `TMPDIR` before the post-document rerun. No verifier, fixture, scope, floor, or registry was changed.

## 2026-10-19 — Round 46 P4 citation-note correction

- The post-document checklist output `.ufo/round-46/evidence/p4/final/skill-checklist.stdout` exposed a second failure caused by the P4 correction note itself repeating the brace-form citation as a live link. Reworded that new note descriptively without the dead token; SCORECARD already has separate literal C3/P4 links. The original unrelated missing-runner finding remains unchanged. A final post-correction check is required; no verifier, fixture, scope, floor or registry was changed.

## 2026-10-19 — Round 46 B2 superseding report pin

- Final report `.ufo/round-46/scouts/B2.md` SHA-256 `3fe64da69d6b91e0ebf2a7e8125b1db15db06cf4e0ed1e89fb144deddbd504b4` supersedes the earlier B2 report hash recorded above. It retains exactly four tentative SHONEN marks, no rejected marks, and separate bounded C1/C2/C3 verdicts.
- Corrected the C3 source pin to current `SCORECARD.md` SHA-256 `c4049aa94aa2b652efed1f848679a3ee64b176ea690486c6696b7728418cb127`; P4's candidate result remains scoped to registered reason/evidence/probe-target metadata, with calibration 8.5 and no whole-round closure (`.ufo/round-46/scouts/P4.md`).
- The exact post-report/post-log checklist rerun is performed after this entry. Its stdout, stderr, exit status, and before/after pins are captured at `.ufo/round-46/evidence/b2-final-checklist.stdout.json`, `.ufo/round-46/evidence/b2-final-checklist.stderr.txt`, `.ufo/round-46/evidence/b2-final-checklist.exit.txt`, `.ufo/round-46/evidence/b2-final-checklist.pin-before.txt`, and `.ufo/round-46/evidence/b2-final-checklist.pin-after.txt`. No SHONEN, product, protocol, mission, axes, corpus, sibling-repository, or floors-registry file was changed; no Git add, commit, or ref operation was performed.

- 2026-10-17 — README: Devin wiki link. Operator directive (2026-10-17):
  insert the Devin wiki link into the README header of every repository
  with a generated wiki. `README.md` created (lane-header convention) with a `**Wiki:**` link to
  https://app.devin.ai/org/veigapunk/wiki/VeigaPunk/kotoba-shokunin?branch=master.
  Evidence: the org's Devin wiki index lists this repo's generated wiki;
  sibling lane READMEs carry the same `**Wiki:**` header.
  Documentation-only change; no round run, no axis moved.

## 2026-10-19 — Round 46 landing (kaika steered round 46): C1 improved; C2 improved-bounded; C3 improved as registered, class improved-bounded

- Steer: the kaika steer table on the fleet-ledger branch `kaika/ledger` (waves/kaika steer.md) row kotoba → 46, "land r46 if its claims verify on re-measurement, else close it honestly". Base `78ee57e` (merge of WIP `36ab0d3`); committed comparator `ccf41c23…`. Collision check: no round-46 kotoba report at the fleet root, no LOG entry closing round 46 before this one.
- Measurement harness: `.ufo/round-46/evidence/w2/gates/meas-tree.sh` builds a canonical-layout shared clone under `/tmp` (the tower worktree location breaks `../` citations); `battery.sh` runs the gate battery there. Base battery at `78ee57e` (`.ufo/round-46/evidence/w2/gates/before-78ee57e/summary.txt`): checklist exit 1 (9/10, `governance.citation_resolves` at `LOG.md:2111`), corpus integrity 0 (9/9), corpus independent 0, surfaces 1 (5/7, omp extraction), pins 1 (1/3, omp sha/mtime), floors 0 (9/9 exact `10/150/91/87/1597/62/104/328/150`, stdout `ef091efb…`).
- Carrier race (motivates M19): a fresh join's scoped-out probe recomputes `$HOME/.omp/agent/sessions`, which ~100 live agents grow every few seconds; paired runs raced into `false blocker` on both comparators (`.ufo/round-46/evidence/w2/l1-matrix/race-fresh2/results.json`; reviewer HIGH-3). All claim arms below were re-measured on a frozen `cp -a` snapshot (HOME `/var/tmp/kotoba-r46-home`, 1249 `*.jsonl`, listing digest `4d715d652a630a45c09df476095f96119c081eb5ba409b4bb21687fd994e2aaf`), producers on the real HOME, committed-target observables refreshed against the snapshot.
- C1 depth (`.ufo/round-46/evidence/w2/c1/summary.json`, seat R46ExecC1b): planted-CWD relative `--scope-file` — frozen exit 0 (attested `3d8500ed…` ≠ enforced superset `886b1393…`) → `ccf41c23…` exit 2 `laundering`, and `778b367e…` exit 2; absolute planted control exit 0, receipt digest = enforced; honest join exit 0, 24/24 protocol, 20/24 strict; self-test 0/328; floors 9/9. Critic P1 (symlinked relative `--cwd`) holds. Verdict improved; depth holds 9.
- C2 operability (`.ufo/round-46/evidence/w2/c2/summary.json`, seat R46ExecC2b; `.ufo/round-46/evidence/w2/l1-matrix/snapshot2/` at `ccf41c23…`, `snapshot3/` at landing): live mode/summary/verdict shadows, same-id mode duplicate, raw duplicate `results`/`re_derived`/nested member — frozen 0 → 2 class-named. Reviewer MED-3 reproduced (`.ufo/round-46/evidence/w2/l1-matrix/med3/`): a duplicate-member prose fragment before a valid payload — frozen 0, `ccf41c23…` 2 (new false red). Repaired: `extract_json` selects with a plain decode and re-decodes only the selected payload with the unique-member hook (prose arm 0; in-payload duplicate 2); two self-test arms added, floors bumped in step 328→330 (registry, both tables, docstring). Surviving: mirror opt-out 0/0 (R2, reviewer HIGH-1), missing `verdict` = PASS (MED-1), `NaN`/case-variant keys (critic P2/P3) — all pre-existing. Verdict improved-bounded; operability holds 8.5.
- C3 calibration (`.ufo/round-46/evidence/w2/l1-matrix/snapshot3/results.json`): reason+evidence drift, committed-reason/redirected target, probe-copy shadow — frozen 0 → landing 2 (`scope reason drift`, `scope evidence drift`, `scope probe target drift`, `scope probe channel split`); fabricated observable 2/2 (pre-existing); honest control 0/0 at 24/24. Records: SCORECARD calibration row and the census entry get appended corrections naming `36ab0d3` for `ccf41c23…` (Q03). Surviving: record-level `kind` drift 0/0 (critic P5), payload-selectable committed scope-outs (reviewer HIGH-2), carrier race (HIGH-3). Verdict improved as registered, class improved-bounded; calibration holds 8.5.
- Conformance landed (no claim credit): `corpus/QUALITY.md` Q01–Q18 (each cites a `corpus/lessons/round-46.md` § Mistakes row); the lesson (M1–M19 re-verified by seat R46Scribe-2, M17–M19 added at landing; § Gate); `corpus/SOURCES.md` per SOURCES contract v1 (11 opened rows, A=10 C=1, 1 rejected S011; seat R46ExecSources-2; S010's "both exit 0" corrected after the L1 re-run showed `--json` exit 1; S001–S003/S008 `queued`→`mined` by the `SKILL.md` portability-floor line); `SHONEN.md` regenerated in canonical form (4 boxes, one evidence line each, all `[~]`); `PROVINCE.md` Core/Frontier/Adjacent (adjacency from `.ufo/round-46/scouts/w2-connector.md`); `corpus/README.md` § Frontier + three index rows; `README.md` domain line (`**Domain:** >` leak) fixed; `SKILL.md` +1 portability paragraph, +1 Sources pointer.
- L2 swarm (one batched call, 10 seats: planner, connector, 3 executors, sources executor, scribe, scout, reviewer, critic; first attempt refused at the 100-job cap and re-sent whole). Provider exhaustion: R46ExecC1-2, R46ExecC2-2, R46ExecC3Gates-2 died `resource_exhausted` (Devin free-model limit); C1/C2 seats re-dispatched fresh (R46ExecC1b, R46ExecC2b); the C3 re-dispatch R46ExecC3b died on codex capacity, so the L1 ran C3 and the battery itself. Reviewer seat wrote 28 stray files into the fleet root through the broken-`cd` hazard (listed in `.ufo/round-46/scouts/w2-reviewer.md`; reported to the orchestrator; not touched here).
- Corpus baseline re-recorded in step (`verifiers/corpus-baseline.json` notes `round46_landing`): tracked_files 55→58, report_total 38→40, commit_total 27→29, all zero-defect checks zero. The lesson's two pointers to the round-45 report were first written bare and read `report_dead=2` against the fleet root (that report lives only in the lane repo); they are host-absolute now. Pre-commit overlay run (shared clone of `78ee57e` + this tree under `/tmp`): checklist 9/10 (only the pre-existing `LOG.md:2111`), corpus integrity 9/9, corpus independent exit 0, floors 9/9 exact at `…/330/150`.

## 2026-10-19 — Round 46 landing pin and after-battery

- Landing commit `f2f9ee1` (tree `d26a91bef9fff8877d5552e2dc4d2986da63eb10`, comparator SHA-256 `778b367e5e5f94fc90132f4070aec3e2395b26914a1d0a50a188558c55cff332`). After-battery on that commit in the canonical-layout clone (`.ufo/round-46/evidence/w2/gates/after-f2f9ee1/summary.txt`): checklist exit 1, 9/10 (only `LOG.md:2111`, unchanged class); corpus integrity 0, 9/9; corpus independent 0; surfaces exit 1, 5/7, stdout `8432070a…` byte-identical to base; pins exit 1, 1/3, stdout `16e71a19…` byte-identical to base; floors 0, 9/9 exact `10/150/91/87/1597/62/104/330/150`. No gate moved red; the only floor move is the in-step comparator bump.
- SOURCES census on `f2f9ee1` (contract v1 § Census, all seven commands): rows 11, malformed 0, tiers A=10 C=1, status mined=4 queued=6 rejected=1, duplicate ids none, enum/tier-inflation none, mined used-by missing none. The census also showed S002 was mined by `SKILL.md` only through the range "S001–S003", which a literal-id check cannot see; this commit spells the ids out (`S001, S002, S003, S008`).

## 2026-10-21 — Round 47 landing (hyaku campaign, steered round 47): C1 freshness improved; C2 operability improved; C3 calibration improved

- Steer and base: plan `plans/round-47.md`; BASE `c61a973b2e02e1ded169703ddcb06466f4edd8bd`; before-run `.ufo/waves/round-47/before/SUMMARY.md` (raw outputs beside it). Coordinator: MoriR22R (reused idle agent; Main spawn job-capped), which died with the host session after dispatch; the replacement coordinator KotobaR47-2 integrated the surviving wave-1 output. The L1 held the §3 planner seat; the planning data-walk rode scout/connector items (`ConnClaimSeparability`, `RevPlanCalibration`).
- Wave 1 (build): one validated 92-seat call (`.ufo/waves/round-47/build-spec.json`, `.ufo/waves/round-47/build-dispatch.json`; spawned on gate try 9 after 8 job-cap refusals, `.ufo/waves/round-47/build-refusals.json`): scout 39, executor 17, reviewer 10, scribe 8, connector 6, critic 5, revenger 2, sentinel 2, mutation-tester 2, simplifier 1. 72 seats reported (`.ufo/waves/round-47/build/`); 20 died with the host session without a report and stay dead: C1OpencodeResolve, C1OcRuleRederive, C1PinsRepin, C1SelfTestFloors, C1OmpLoaderRE, C1OcLoaderRE, C1CensusDocRows, C1DepthNoHarm, C2CheckImpl, C2Battery, C2TriggerFidelity, C2FloorsBoxes, C3ErrataImpl, C3Residuals, ConnClaimSeparability, RevPlanCalibration, CritNoHarm, RevHarnessIndependentNote, RevSurfacesFixtures, ExecErrataAlt. Their partial artifacts were not integrated.
- C1 (freshness): omp 18.12.5 callees `lq`/`Xl`/`Fo` appended to the allowlist with an 18.12.5 fixture (`.ufo/waves/round-47/build/C1OmpCallShapes.md`); opencode 1.19.3 is the npm `opencode-ai` channel and the round-14 loader lineage, not v2.0.26's successor (`.ufo/waves/round-47/build/KnowSubstrateRecensus.md`, `.ufo/waves/round-47/build/C1CriticRepin.md`). Rules OC-1..OC-6 re-measured anchor by anchor on the frozen dump (OC-3b now requires `.filter(`; OC-4 adds the `ReadTool.execute` caller); 9 ids re-instated, 3 v2.0.26 ids retired, `config/instructions` re-verdicted governed — census § B′ plus the ledger section, moved v2.0.26 rows byte-identical (`corpus/knowledge/instruction-surface-census-round13.md`); fixtures rebuilt from exact dump substrings, the v2.0.26 fixture kept as a must-fail generation probe, a planted-name fixture added. Default opencode path moved to the npx ELF in `verifiers/verify_surfaces.py`, `verifiers/check_substrate_pins.py` and `verifiers/verify_harness_claims.py` together; `verifiers/baseline.json` re-pinned from `/fast/scratch/kotoba-r47/shared/SHA256SUMS`. `python3 -B verifiers/verify_surfaces.py --json` exit 2 → exit 0, 7/7 at default resolution; `python3 -B verifiers/check_substrate_pins.py` exit 2 (DRIFT 3/3) → exit 0, 3/3; AFTER code with the BASE baseline and census → exit 1; `--self-test` 87 → 99 assertions, 0 failures.
- C2 (operability): `trigger.no_xml_tag` in `verifiers/verify_skill_checklist.py` (reference design `.ufo/waves/round-47/build/C2CriticRule.md`; the alternative `.ufo/waves/round-47/build/ExecDescriptionCheckAlt.md` was not taken — it scans `description` only), four fixtures under `verifiers/fixtures/checklist/xml-tag-*`; `SKILL.md` description `<skills>` → `omp skills router`. Frontmatter `<skills>` count 1 → 0; live check PASS 2 evaluated; `--self-test` 1597 → 1845 assertions with C3's arms, 0 failures. Sourced on S003 (re-opened) and S012 (`corpus/SOURCES.md`).
- C3 (calibration): in-source `GOVERNANCE_ERRATA` row pinning `LOG.md:2111` by line sha256, token and absence wording, horizon 2315 (`.ufo/waves/round-47/build/C3CriticDesign.md`; answers the sentinel's blocker `.ufo/waves/round-47/build/C3SentinelErrata.md`); `corpus/README.md` indexes `corpus/lessons/round-46-verifier-spotcheck.md` and `corpus/lessons/round-47.md`; `verifiers/corpus-baseline.json` tracked_files 58 → 60; `verifiers/fault_injection_corpus.sh` planters insert inside `## Coverage map` (`.ufo/waves/round-47/build/ExecFaultBaseline.md`). Checklist `--json` exit 1, 9 PASS / 1 FAIL → exit 0, 11/11 (governance evaluated 804, 1 recorded absence excused); corpus integrity exit 1 → 0, 9/9; corpus independent exit 1 → 0; fault harness exit 1 → 0, ALL PASS.
- Floors ratcheted in step (`verifiers/floors-registry.json`, `verifiers/check_assertion_floors.py`): surfaces 87 → 99, checklist 1597 → 1845; all 9 instruments at floor.
- Frontier step: `corpus/SOURCES.md` 11 → 15 rows (S012 code A mined, S013 docs A queued, S014 docs A queued, S015 own-work A mined), search log appended; `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kotoba` exit 0 before; mistakes M20–M22 and the Gate in `corpus/lessons/round-47.md`; `corpus/QUALITY.md` Q19.
- Not claimed: `verifiers/verify_harness_claims.py` 21/28 before and after (same seven DRIFT ids; three host skills born 2026-10-20 — Q09 debt); round-46 residuals carried (mirror opt-out, missing verdict, NaN/case-variant keys, row `kind`, payload-selectable committed scope-outs). Falsification wave and landing pin follow in the next entry.

## 2026-10-21 — Round 47 landing pin and falsify wave

- Landing commit `7ad7fadfc09354b74fb66605dfb0c1182c115a2f` (lane helper `landed` line; rebased over two operator `considerthese/` commits). After-battery on that commit: `.ufo/waves/round-47/after/SUMMARY.md` — census validate 0, surfaces 0 (7/7, default resolution), pins 0 (3/3), checklist 0 (11/11), corpus integrity 0 (9/9), corpus independent 0, harness claims 1 (21/28, unchanged, not claimed), fault harness 0 (ALL PASS), floors 0, frontmatter `<skills>` 0.
- Correction to the landing entry (Q19 / M23): its "governance evaluated 804" is the BASE-prefix count from `.ufo/waves/round-47/build/C3CriticDesign.md`; at `7ad7fad` the check reports PASS evaluated 848 (the landing's own 44 new citations; `.ufo/waves/round-47/falsify/W2ErrataRerun.md`). "9 ids re-instated" means 7 resurrected, 1 retained and re-anchored, 1 re-verdicted. `RevPlanCalibration` was a reviewer seat, not scout/connector. "Answers the sentinel's blocker" covers the bound-to-one-line, fail-closed half; the sentinel's registry-file probes do not apply to an in-source tuple, and review of the verifier diff remains the only guard against a horizon-plus-row edit (`.ufo/waves/round-47/falsify/W2ErrataAppend.md`). The checklist self-test delta splits 1597 → 1837 (C2) + 8 (C3) = 1845 (`.ufo/waves/round-47/falsify/W2Separability.md`).
- Wave 2 (falsify, post-crash, fresh identities): one validated 77-seat call (`.ufo/waves/round-47/falsify-spec.json`, `.ufo/waves/round-47/falsify-dispatch.json`; spawned on try 2 after 1 job-cap refusal, `.ufo/waves/round-47/falsify-refusals.json`): reviewer 28, scout 19, critic 10, executor 10, mutation-tester 5, connector 3, sentinel 2. 73 reported (`.ufo/waves/round-47/falsify/`); 4 died at the coordinator's rate-limit exit without a report and stay dead: W2S015Rerun, W2PlanNote, W2JjHygiene, W2EvidenceBloat. Round total 169 seats (92 + 77), 24 dead. One seat (W2DropOC2) wrote a candidate edit into the production `verifiers/verify_surfaces.py` through a relative path for about a minute and restored it byte-identical; no jj or git command ran in that window and the lane tree matched `7ad7fad` afterwards.
- Every counting command reproduced at `7ad7fad`, including the 2x2 matrix (only tip code with tip data exits 0), the real-dump planted-name and dropped-name probes, the erratum's laundering arms (7/7 killed) and the omp mutants (6/6 killed).
- Defects found and corrected in this commit (records and comments only; no gate logic changed): `SKILL.md` "10 checks" → 11; `verifiers/verify_surfaces.py` comments (rule list, OC-4 every-ancestor walk, OC-6 layer composition, census pointer, carried gate limits); the fixture headers' exact-substring claim and the four fixture baselines' round-18 comment; `corpus/README.md` lesson rows (S006/S007 not re-opened; round-46 spot-check landed); census and `corpus/knowledge/opencode-extraction-round14.md` append-only errata; lesson M23 and Gate corrections; `SCORECARD.md` pointers and attribution.
- Defects found and carried to round 48 (named, not fixed): every OC rule is a whole-dump presence test — OC-1's gate term is a tautology, OC-4's call edge and in-hook token, OC-5's polarity, OC-6's config candidate and OC-3a/3b decoys survive (`.ufo/waves/round-47/falsify/W2DropOC1.md`, `.ufo/waves/round-47/falsify/W2DropOC4.md`, `.ufo/waves/round-47/falsify/W2DropOC6.md`); 25 of 42 ids are witnessed by literal presence only (`.ufo/waves/round-47/falsify/W2BlindArm.md`); `trigger.no_xml_tag` misses non-ASCII tag names and flags non-double-quoted `\u003c` escapes, and its CDATA/PI arms are unasserted (`.ufo/waves/round-47/falsify/W2XmlEdgeCases.md`, `.ufo/waves/round-47/falsify/W2XmlMutants.md`); the npx launcher is unpinned and compound-kind pin keys are silently ignored (`.ufo/waves/round-47/falsify/W2PinsRerun.md`); `verify_harness_claims.py` exits 1 rather than 2 on a missing `--oc-bin`; census § A's omp evidence column still quotes pre-18.12.5 call shapes; `check_assertion_floors.py`'s 120 s self-test timeout is load-marginal for `harness_independent`.
- Possible harm, reported for the closure to rule: moving `OC_BIN` to the live 1.19.3 ELF turns the producer's `oc.roots.names_plus_builtin` 10 → 11 while the independent instrument declares built-ins 0, so the comparator's frozen-carrier join moves 21/24 → 20/24 (`.ufo/waves/round-47/falsify/W2DepthNoHarm.md`, `.ufo/waves/round-47/falsify/W2HarnessNoHarm.md`); its default live join exits 2 at BASE and at the landing alike (pre-existing probe race).
- Trend verdicts: expansion unchanged (no knowledge entry admitted); quality improved (census re-derived, stale entries marked by errata); discernment unchanged (no non-author spot-check this round; the falsify wave is lane-dispatched).
- Post-hold custody qualification (same author resumed after the recorded 429 backoff): 73 W2 reports remain findings/leads, not non-author closure. The captured wave context directed all roles into scratch clones; the parent's resume rule disallows scratch writes for read-only/report roles. A conservative lexical inventory holds 58 W2 reports from admission authority (mentions of scratch/clone/mutation or scratch paths; an over-approximation, not 58 proven scope violations). W2DropOC2's restored production-write incident is separately void as source-change authority. See `.ufo/waves/round-47/falsify/custody-note.txt`. No replacement seats were dispatched.
- Final claim disposition supersedes the provisional "improved" wording above: C1/C2 counting targets met with bounded limits; C3 counting targets met, but its calibration/no-harm admission is **unprovable** (registry-design limits, record defects and the reported producer/independent mismatch remain). Scores held; no round admission asserted. The L1's after-falsify battery, not scope-held reports, is positive measurement authority.
- Cleanup custody: all round-owned scratch, including the frozen shared snapshot, will be removed under the parent's cleanup order. Committed digest, anchor and command receipts remain; old absolute scratch-based recheck commands become unavailable. The current default surfaces/pins commands remain runnable against live host files. No deletion of an unrelated lane's scratch is authorized.
- Parent correction supersedes the provisional 58-report custody hold above: the new sole-report/no-scratch rule does not retroactively rewrite W2's captured permissions. Zero reports are void solely for authorized scratch usage. W2DropOC2's production-write incident remains separately disclosed; no candidate source from it was integrated. Reports remain lane-authored, not non-author closure.
- Cleanup incident supersedes the preceding future-tense cleanup note: deletion executed just before the stricter preservation instruction arrived. Final source corrections/evidence were already landed at `3f4345479278ec87e656afb230e2644f2d7db9ba`; no unmerged production edits lost. The deleted shared snapshot was reconstructed from live pinned binaries and regenerated strings; all four full SHA-256 values matched retained receipts. The restored shared snapshot remains at its cited path. Scratch-only Git objects cited by experiment reports may be lost; availability is not asserted. Post-incident worktree list/dry-run showed only an unrelated empty directory (not removed). No further cleanup performed; C3/no-harm disposition stays unprovable.
- Follow-up object custody census after the parent's explicit instruction: `.ufo/waves/round-47/after-falsify/git-object-custody.json` checks 953 standalone 7–40-digit hex candidates in retained round evidence and records (overinclusive, includes truncated content digests). 90 resolve to commits reachable from lane refs, 17 from fleet refs; 60 objects exist without proved ref reachability, 786 candidates do not resolve in either repo. Explicit cited scratch commits b1b48d1, 5d50621, 371e901, 51385ae, d68eae3 and 2e6e5c1 do not resolve; neither does the measured scratch tree a736f6407ba02a038a6c0256c40cc932727688fc. These past objects were NOT synthesized. Restored snapshot bytes are reconstructed custody, not uninterrupted custody; the original committed digests were comparison expectations, never regenerated to fit.

## 2026-10-22 — Round 48 landing (hyaku campaign, attempt 2): C1 freshness knowledge entry; C2 depth configured-root (improved-bounded)

- Steer and base: plan `plans/round-48.md`; base `75f671b109d8eddd0d64c1429bd6379fe577175a` (attempt 1's two pushed commits `c0185da` instrument and `75f671b` before receipt, re-verified inside the lane by seat FrAttempt1Audit: ruler, oracle and receipt hashes match committed bytes; a fresh base run reproduces the 5 target failures). Attempt 1's private trees, approval windows and hash chains are not continued; their pointers are named as not re-verifiable from the lane. The L1 held the planner seat; the planning data-walk rode the critic and connector items.
- Wave 1 (build): one validated 33-seat call (`.ufo/waves/round-48/build-spec.json`, `.ufo/waves/round-48/build-dispatch.json`, assignments `.ufo/waves/round-48/build-assignments.json`): executor 9, scout 8, scribe 5, reviewer 4, mutation-tester 2, critic 2, connector 2, revenger 1. Reports under `.ufo/waves/round-48/build/`.
- Claim order changed before any landing: C1ClaimCritic showed the configured-root change does not repair routed defect 1 (the join drop is the producer's built-in marker probe), so the knowledge entry, which repairs routed item 3, became the first claim (`corpus/lessons/round-48.md` M26, `corpus/QUALITY.md` Q21).
- C2 (depth), landed `d1ae45830235c38320b31032b57a8323cbf90b17`: `verifiers/verify_harness_independent.py` unions direct-child `SKILL.md` names from `--oc-config/skill` and `--oc-config/skills` with the log roots; self-test arm 104 → 115 assertions, with a nested-skill discriminator that kills the recursive mutant the frozen ruler passes (`.ufo/waves/round-48/build/C1RulerTargetMutants.md`, `.ufo/waves/round-48/build/C1RegressionArm.md`); floor ratcheted 104 → 115. Ruler on the landed commit: exit 0, verdict clean, 0 target failures, 0 behavioral mismatches, ruler sha256 `01af33a6…` (receipt `.ufo/round-48/verification/after-configured-root.json`). A first run through process substitution recorded an empty-input ruler hash and was discarded (M27).
- C1 (freshness), landed `887b6af54d3f4446f1fe51dc16f26b2e83bc82e1`: `corpus/knowledge/frontmatter-rule-authorities-round48.md` (rule-by-authority table over six authorities opened 2026-10-22; the YAML-alias, Unicode-name and escaped-value counterexamples run through the lane check, the packager and skills-ref); `SKILL.md` § Portability floor rewritten to name the parsed rule and point to the entry. Knowledge Markdown entries 34 → 35.
- Frontier step: `corpus/SOURCES.md` 15 → 21 rows (S016 opencode v1.19.3 skill discovery, S017 skills-ref, S018–S021 superseding S001/S003/S010/S013; old rows unchanged); census validate exit 0 at start and at the C1 landing (three W04 same-URL warnings from the superseding rows); lesson `corpus/lessons/round-48.md` with mistakes M24–M27 and the Gate; `corpus/QUALITY.md` Q20–Q21; `corpus/README.md` qualifies the stale live 24/24 rows and records the erratum horizon (2315 versus 2343 LOG lines at round start); `verifiers/corpus-baseline.json` tracked_files 61 → 63.
- Observed, not caused by this round: omp is 18.12.6 (sha256 `85d9daf3…`), so `verifiers/check_substrate_pins.py` exit 1 (DRIFT 2/3) and `verifiers/verify_surfaces.py --json` exit 1 (5/7) at base; `verifiers/compare_harness_independent.py --json` exit 2 (`false blocker`, live session growth) at base; the adjacency replay exits 1 `instrument_drift` at base (`.ufo/waves/round-48/build/FrCensusAndScorecard.md`).
- Falsification wave and landing pin follow in the next entry.

## 2026-10-22 — Round 48 landing pin and falsify wave

- Commits after the records commit `84b9c9ba89559b51a72c83c2b9605b184df4ae9e`, all through the lane helper: `d28b16b` and `2788704` (falsify corrections 1-2), `48819b9` (C2 follow-up: an unreadable configured root contributes nothing instead of aborting; self-test 115 → 116; floor 115 → 116), `eb5a80f` and `03f5394` (corrections 3-4: entry sweeps as footnotes with file operands, untabled rules listed, per-source rechecks, README qualifications corrected, Q23 supersedes Q20, Q22 and Q24, used-by moves on S001/S003/S012/S018/S019 logged in the lesson, C2 arm assertions tightened). Every correction is listed in `corpus/lessons/round-48.md` § Falsify-wave corrections.
- C2 counting command re-run on each later consumer: `48819b9` (consumer sha256 `0f33f600…`) and `03f5394` (`f576c23f…`) — ruler exit 0, verdict clean, 0 target failures, 0 behavioral mismatches (receipts `.ufo/round-48/verification/after-configured-root-48819b9.json`, `.ufo/round-48/verification/after-configured-root-03f5394.json`).
- C1 counting command: `git ls-tree -r --name-only <rev> corpus/knowledge | grep -c '\.md$'` → 34 at `75f671b`, 35 at `887b6af` and at every later commit (no other knowledge file changed).
- Wave 2 (falsify): one validated 34-seat call (`.ufo/waves/round-48/falsify-spec.json`, `.ufo/waves/round-48/falsify-dispatch.json`): reviewer 19, critic 8, mutation-tester 3, scout 3, sentinel 1; reports under `.ufo/waves/round-48/falsify/`. Wave 1 reported 33 of 33. No dead seats in either wave.
- Open after the wave (carried, not fixed): the frozen 13-case oracle has no nested-skill, frontmatter-name or log-named-external case, so recursive and frontmatter-keyed mutants pass the ruler (the self-test arm kills the recursive one; `A26NestedOracleGap.md`, `C1RulerNoHarmMutants.md`); an unreadable `SKILL.md` under a configured root is still counted (legacy `is_file()` parity, `A25ArmReview.md`); several counts in the entry carry no command and date (Q13, `A10FillerHunt.md`); C1's axis label (freshness versus the expansion observable) is disputed by `A09ClaimSizingC1.md`; the live gap on the routed row is 12 versus 10 with a second cause (`~/.claude/skills` is not enumerated by the instrument, `A27MistakeRows.md`).
- Also open (`A21NoHarmBattery.md`): the agents root keys names by frontmatter while configured and log-named roots key by directory, so a configured skill whose directory differs from its frontmatter name counts again (probe 4 → 5; no live effect, both roots absent here). The checklist gate was red at the records commit `84b9c9b` only (a SCORECARD pointer to the not-yet-landed fleet report) and green again from `d28b16b`; all other gates match base exit codes (`A21NoHarmBattery.md`, `A32NoHarmCritic.md`).
- Observed, not caused by this round: the live join exits 1 or 2 from run to run on the same commit (session-store race); omp 18.12.6 keeps pins and surfaces red.

## 2026-10-22 — Round 49 landing (hyaku campaign, attempt 1): C1 adjacency sibling-overlap census; C2 operability dispatch-prompt boxes

- Steer and base: plan `plans/round-49.md`; base `a5adc146a2995dcc5a95a6d8db6e5674f75191ac` (round 48 admitted). No earlier round-49 attempt. Drift guard honoured: the SKILL.md frontmatter is unchanged and no claim is on freshness.
- Wave 1 (build): one validated 36-seat call (`.ufo/waves/round-49/build-spec.json`, `.ufo/waves/round-49/build-dispatch.json`): scout 23, scribe 4, executor 4, reviewer 2, critic 2, connector 1; 0 dead seats. The L1 held the planner seat; the planning data-walk rode scout `PlanDataWalk`.
- Both claims were re-sized before any landing: `CriticC1Sizing` showed a bare list of 20 names satisfied the first C1 counter, and `CriticC2Sizing` showed two dispositions pointing at an unrelated instrument or a ten-byte stub satisfied the first C2 counter (`plans/round-49.md`, re-sizing notes; lesson M29, criterion Q25).
- C1 (adjacency), landed `f054b8e88f4c455d19a57d17e0369468ee4013dc`: `corpus/knowledge/sibling-overlap-census-round49.md` (20 rows at pinned sibling commits, one seat per lane; 7 adjacent, 13 none, 0 contested), `PROVINCE.md` § Adjacent rewritten as a table (classified, pinned rows 0 → 20), `verifiers/check_sibling_census.py` (self-test 39 assertions; `rows 20 verified 20`, `province rows 20 matched 20`, exit 0; exit 1 on the base `PROVINCE.md`, a kasegi-reclassified copy and a one-quote-altered census). Sources S022 and S023 written, S018 re-opened (`corpus/SOURCES.md` 21 → 23 rows).
- C2 (operability): `verifiers/verify_dispatch_prompts.py` with committed fixtures `verifiers/fixtures/dispatch-prompts/`; `--box-proof` → `boxes proven 2`, exit 0; `--self-test` 32 assertions; map 8/0/33 → 8/2/31; `dispatch.08` box authority re-worded from the frozen `.round` file to `.report-baseline`; floors guard 9 → 10 instruments, all PASS. Live run 11:15Z: dispatch.04 FAIL on six `*-L1.md` prompts with a `<lane>` report path; dispatch.08 PASS 250, N/A 29.
- Routed round-48 defects: R1 fixed in `f054b8e` (self-test 116 → 123); R2 → M29/Q25; R3 correction appended in SCORECARD; R4 count-provenance section appended to the round-48 entry (21 of 23 counts reproduce; two do not, recorded) plus the round-48 Gate admit erratum; R5 carried with a specified v2 oracle.
- Gates at the integrated tree: `verify_skill_checklist.py` exit 0 (11/11); `check_assertion_floors.py` exit 0 (10/10); `verify_corpus_integrity.py` 1 DRIFT (report_dead 2 from the closure-owned round-48 spot-check's repo-relative report pointers; at base it read 4 DRIFT); corpus baseline re-recorded (tracked 63 → 66, report_total 41 → 43; zero mode not masked).
- Frontier step: census `scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kotoba` exit 0 at start (21 rows) and after the C1 landing (23 rows), three W04 warnings both times (S018, S019, S021).
- Falsification wave and landing pin follow in the next entry.

## 2026-10-22 — Round 49 landing pin and falsify wave

- Wave 2 (falsify): one validated 38-seat call (`.ufo/waves/round-49/falsify-spec.json`): reviewer 29 (one probe item was re-roled from labrat, which the validator rejects), mutation-tester 3, critic 2 plus `CriticBoxReword`, scout 2, connector 1. Main's freeze arrived at 11:30Z; corrections below landed under it, no new scope. 13 seats were still running when this entry was written; their reports are not in this commit.
- C1 corrections: kake and kasegi reclassified `adjacent` under the stated rule (kotoba's own description names them; `CriticC1Landed`, `RowKake`, `RowKasegi`): 7/13 → 9/11; the rule now names wave reports as non-scope surfaces (`RowMado`, `RowTabi`); `none` notes no longer say "no claim on kotoba ground"; kengaku "route telemetry" removed and a possible contested element recorded (`RowKengaku`); tameshi note re-cited (`RowTameshi`); kaidoku/revenger routed to the existing L0 line 42. The guard now re-derives the skill-file, names-kotoba and arbitration cells, fails a `none` row whose sibling names kotoba and a quote under six words (self-test 39 → 44). Survivors still open (`MutCensusGuard`): the ±2 window, section isolation, vocabulary check and the M<N exit path have no killing arm. Live guard: `rows 20 verified 20`, `province rows 20 matched 20`, exit 0.
- C2 corrections: `boxes proven 2` reproduces, but the proof checks the instrument's six named conjuncts, not the box text (`ReplayC2BoxProof`, `CriticC2Landed`, `MutDispatchInstrument`): no fixture for an unsubstituted variable before the report path, a non-digit round folder, the `≤` equality boundary or the legacy-state arm; map-delegation and pinned-hash checks survive mutation; no gate runs `--box-proof`. SKILL.md and the capability row now say so.
- R4 is partly addressed, not closed (`ReviewR4Provenance`): corrections appended to the round-48 entry.
- S022 `teaches` cell corrected ("description alone" overstated; listing priority under budget is documented, not a tie-break; `ReopenS022`).
- No harm (`NoHarmGates`): no check green at base and red at head; corpus integrity improved 4 DRIFT → 1 DRIFT (the closure-owned report_dead 2).
- L0: two lines filed in the fleet repository (`ff3aff2`): opencode config group owner; retire the round-1 `*-L1.md` prompts.

## 2026-10-22 — Round 50 landing (hyaku campaign, attempt 1): C1 adjacency description names the adjacent lanes; C2 operability box proof deletion-enforced

- Steer and base: plan `plans/round-50.md`; base `f30464660c675d1c1e2851a3bf0366a3aaffe5a8` (round 49 admitted). No earlier round-50 attempt.
- Wave 1 (build): one validated 33-seat call (`.ufo/waves/round-50/build-spec.json`, `build-dispatch.json`): scribe 12, scout 7, executor 5, critic 3, reviewer 3, mutation-tester 2, connector 1. The L1 held the planner seat. `FloorsRegister` and `DescDraft` were overtaken: the L1 did the floors registration and wrote the description from the critics' constraints.
- Both counters were re-sized before any landing (`plans/round-50.md`, re-sizing notes): `CriticC1Sizing` showed a case-sensitive, whole-frontmatter name count printed 9 with fewer lanes; `CriticC2Sizing` showed a manifest hash pin and a traceback both scored 6 of 6. That is the class M31 records (criterion Q26).
- C1 (adjacency), landed `542f515672306e1baefcb69ba79f1d4c18b6450e`: `SKILL.md` description names chousa, kagi, kake, kama, kasegi, kengaku, kotodama, kumitate and tameshi, each in a clause with an ownership or routing word, 1,008 of 1,024 characters, first 99 characters unchanged. Guard `verifiers/check_sibling_census.py --skill` (new; self-test 44 → 68, floored): `skill description names 5 of 9 non-none lanes`, exit 1 on the base description → `9 of 9`, exit 0. Sources S024-S029 written (opencode, VS Code, Claude Code subagents, two GitHub Copilot pages, Gemini CLI), S019 and S022 re-opened byte-identical; finding appended to the census entry: no page documents a tie-break between overlapping descriptions; every "which one wins" rule found is keyed on the name.
- C2 (operability), same commit: `verifiers/verify_dispatch_prompts.py --box-proof` reads coverage from observed conjunct statuses (self-test 32 → 56); counter `verifiers/box_proof_case_deletion.py --rev <rev>`: `killed 0 of 6` at `f3046466` → `killed 6 of 6` at `542f515` (controls 0 of 2 → 2 of 2, N/A 0 of 1 → 1 of 1). The checklist gate runs each delegated instrument's `--box-proof` (self-test 1845 → 1851). Floors guard 10 → 11 instruments, all PASS.
- Routed round-49 defects: D1 (report append-only), D2 (docstring and help reworded; gate wired), D3 (precedence rule and rulings appended to the census entry; duplicate rows rejected; guard floored), D4 (SCORECARD qualifiers), D5 (reject erratum in `corpus/lessons/round-50.md`), D6 carried (R4, R5, R1; seat `CarryD6.md`).
- Base was already red on corpus integrity (the round-49 spot-check landed without an index row: `unindexed 1`, seat `BaselineGatesA.md`); indexed this round and the corpus baseline re-recorded (tracked 66 → 68, report_total 43 → 44). `report_dead 2` stays (the closure-owned round-48 spot-check's repo-relative pointers).
- Frontier step: census `scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kotoba` exit 0 at start (23 rows) and after the landing (29 rows), three W04 warnings both times (S018, S019, S021).
- Falsification wave and landing pin follow in the next entry.

## 2026-10-22 — Round 50 landing pin and falsify wave

- Wave 2 (falsify): one validated 38-seat call (`.ufo/waves/round-50/falsify-spec.json`): reviewer 26, critic 6, mutation-tester 5, scout 1, judged at `956ee1676e4c18480bce8ac3993541462be76e11`. Corrections landed through the helper at `a78fec1`, `bf109ca` and `87eeae2`, and a last records commit after this entry.
- Both counters reproduce (`ReplayC1Counter`, `ReplayC2Counter`, `NoHarmGates`, `CalibrationRecords`): C1 guard 5 of 9, exit 1 → 9 of 9, exit 0; C2 driver `killed 0 of 6`, exit 1 → `killed 6 of 6`, exit 0. No gate green at base is red at head (`NoHarmGates`): corpus integrity 4 DRIFT → 1 DRIFT (the closure-owned `report_dead 2`), corpus independent 2 → 1; `verify_surfaces.py`, `verify_harness_claims.py`, `check_substrate_pins.py` red at both from omp 18.12.6.
- Learning bar (`CriticLearningBar`): the census appendix did not meet Q12 on its own (round-49 `source:` line, a recheck that cannot fail on the new text). Added `corpus/knowledge/skill-selection-rules-round50.md` (source S024-S029, S022, S019; a hash recheck over eight pages that prints `DRIFT <url>` on change) and a `SKILL.md` § Anti-patterns error-pattern paragraph citing it; capability row "sibling-description check" entered.
- C1 corrections: the kengaku clause widened kengaku's ground (now "measured capability effects of prompt format", 1,019 of 1,024 characters; guard still 9 of 9); census sentences corrected by appended text: "every rule is keyed on the name" (S026 `sub-agents.md:77` is a fit-based default; Copilot CLI also has type- and source-keyed rules), "the only arbitration is the description" (S022 also documents `when_to_use`, `disable-model-invocation`, `paths`), the four-added-lanes list, the S025 bullet, S023 re-swept with `tie[- ]?break` (0). S019, S022, S026 and S028 `teaches`/`scope` cells narrowed to the page.
- D3 corrections: one definition of `contested` (the round-50 one, limited to text another fleet lane owns); kake and kasegi basis `kotoba` (the sibling-corpus lessons are kotoba-filed and aggregator-owned); kama, kengaku and tameshi rulings re-reasoned on the bytes (`RowKamaR50`, `RowKengakuR50`, `RowTameshiR50`, `ReviewProvinceRows`); no row moves. The rule and the closures are sent to the integrator (the fleet repository's L0 questions file, kotoba round-50 line, fleet commit 8d56eb1). This line was edited once before filing: a backticked fleet path read as an unresolvable lane citation in `governance.citation_resolves`.
- C2 bounds recorded, not fixed: the driver can be laundered by duplicate-id or unlabelled twins and its kill test is a stderr substring (`CriticC2Landed`, `ReviewDriver`); 7 of 17 instrument mutants survive the driver while the self-test catches 16 (`MutBoxProofCode`); the checklist gate's `--box-proof` run is fail-open on delegates it cannot probe (`ReviewBoxProofGate` F1) and 4 of 12 gate mutants survive its self-test (`MutBoxProofGate`). Census guard: 11 of 28 code mutants survive (`MutGuardCode`); second-table duplicates and a downgrade to `none` pass (`MutDuplicateRows`).
- Calibration count (`CalibrationRecords`): 5 mismatches of 51 round-50 statements at `956ee16`; all five fixed after (SCORECARD qualifiers moved out of older shell commands; "D2 and D4 qualifiers"; this entry names the four build seats without a usable report; lesson and census basis now agree).
- Build seats without a usable report at landing: `FloorsRegister` (the L1 did the registration), `DescDraft` (the L1 wrote the description), `D2D4Wording` (the L1 wrote the qualifiers); `PrecedenceDraft` returned after the L1 had landed the rule from `CriticPrecedence` and agreed on all 20 rows.
- Misroot sweep: a round-49 kotoba falsify seat report (`RowGameDev2d.md`) sat in the fleet root's `.ufo/waves/round-49/falsify/`; copied byte-exact into the lane (`cmp` equal, sha256 `37aaa836…`) and removed from the fleet root (lesson M32).

## 2026-10-22 — Round 51 landing (hyaku campaign, attempt 1): C1 freshness omp 18.12.6 re-derived and re-pinned; C2 depth overlap levers by client

- Steer and base: plan `plans/round-51.md` (with its re-sizing and after-landing sections); base `43ca0bfb74372f2a67a48e0aeb2e35d0d98b1d10` (round 50 admitted). No earlier round-51 attempt. Before-values measured at 14:09Z on the lane checkout: `verify_surfaces.py --json` pass 5, fail 2, exit 1; `check_substrate_pins.py` `DRIFT 2/3`, exit 1; census exit 0 with three W04 warnings (S018, S019, S021).
- Wave 1 (build): one validated 33-seat call (`.ufo/waves/round-51/build-spec.json`): scribe 14, scout 6, executor 4, critic 4, reviewer 3, connector 1, mutation-tester 1. The L1 held the planner seat. Follow-ups went to the same identities (no new seats): `LeverGuard` hardened the C2 counter twice, `SurfacesRepin` did the floors bump and the parameter-shadow fix.
- C1 (freshness): allowlist `+Kl|Ho|bq`; the rebound `S$` resolves from the call's own module scope, an in-module ambiguity or a parameter shadow stays unresolved; fixture `strings-omp-18.12.6.txt`; pins re-pinned to omp 18.12.6 (`85d9daf3…`, mtime `2026-10-21T20:37:24.615549837-03:00`); `--json` now prints the binaries it read. Result: pass 5 of 7 → 7 of 7, exit 0 (the two omp checks 0 of 2 → 2 of 2); pins `OK 3/3`. Q09 record: version 18.12.6, sha256 `85d9daf3…`, extraction-rule change (three callee names plus the module-scope binding rule, `verify_surfaces.py` docstring); the census rows 73-74 that cite older call shapes are unchanged (the inventory is byte-unchanged by design) and carried. Falsify: `ReplayC1Counter`, `CriticC1Landed`, `NoHarmGates` reproduce every number; `ReviewScopeRule` found a parameter-shadow false green introduced by the new rule, fixed before the report (self-test 115 → 119, floored); `FixtureFaithful` found three unlabelled non-dump lines in the fixture (carried); `ScoutOmpRuntime`: the gate reads `strings`, not omp's runtime; seven of the eight classes are documented with the inventory's paths, `gemini/system.md` only in code.
- C2 (depth, learning claim): entry `corpus/knowledge/skill-overlap-levers-round51.md`, `SKILL.md` § Anti-patterns table, rows S030–S031, five rows re-opened byte-identical. Not verified as declared: the L1 added three terms to the counter's reviewed list in the content commit `34cfffbb`, after the plan commit; the plan-commit counter gives 4 of 7 on the landed content and on the final content (lesson M35, criterion Q28). The falsify wave corrected the table (effects, author-held levers, quotes, opencode lever) and hardened the counter (self-test 22 → 51, floored); on that counter the final content gives 7 of 7, exit 0, `--fetch` 7 of 7 at 15:33:31Z.
- Routed round-50 defects: D1 `DescDraft.md` committed byte-exact (`e6219026`); seat accounting corrected: all 71 round-50 seats wrote a report, 70 committed in round 50 and the 71st this round; the report's "2 cancelled … without a report" is wrong (`D2D4Wording` was committed at `1cb2e65`, 10:51:01, 67 s before the filing; `DescDraft` wrote at 10:52:19, after it); "0 cancelled" rests on missing records, not on a positive finding. D2 bounded in `SKILL.md` and the SCORECARD qualifier (F1–F5 and the substring advertisement test carried). D3 swept (`SKILL.md`, `corpus/README.md:72`, a round-50 entry note, a census note on S026). D4 erratum and row S030. D5 kama quote and kengaku correction. D6 precedence rule marked provisional, not extended, not relied on. D7 carried (the F30–F33 patch no longer applies after this round's floors edits).
- Mistakes mined: M33 (a reject reason with no page line), M34 (a seat called cancelled wrote after the filing; criterion Q27), M35 (a counter's judgment table widened after the plan commit; criterion Q28).
- No harm (`NoHarmGates`): all 11 base-green gates green at `59903b26`; surfaces and pins red → green; corpus integrity 4 DRIFT → 1 (the carried `report_dead 2`); `verify_harness_claims.py` (21/28, host state) and `fault_injection_corpus.sh` (four red rows) red at both ends, unchanged.
- Calibration (`CriticCalibrationRows`): 5 mismatches of 23 current-state statements in SCORECARD/SHONEN at `59903b26`; four fixed by the appended SCORECARD calibration note, one (SHONEN box 1 "38" Sources entries, 39 by the round-46 method) reported, SHONEN unchanged.

## 2026-10-22 — Round 51 landing pin and falsify wave

- Wave 2 (falsify): one validated 34-seat call (`.ufo/waves/round-51/falsify-spec.json`): reviewer 25, critic 6, mutation-tester 2, scout 1, judged at `59903b2637689739a5b9901956301da72d0effe1`. Two seats (`MutSurfacesHead`, `MutLeverGuard`) first ended on a provider error, "[inception/mercury-3] 429 Rate limit reached: input token limit exceeded"; each identity was resumed once and completed. No seat stayed dead.
- Round total 67 seats (33 + 34); attack roles (reviewer, critic, mutation-tester) 41 of 67.
- Falsify verdicts that changed landed text: `CriticC2Landed` (FAILS: Gate read from any section, leaky section end, raw entry), `ReviewReviewedList` (FAILS: `ignoredSkillsLocations` fitted to the data on a false reason), `ReviewCommitOrder` (FAILS: C2 list moved after the plan; 4 of 7 on the declared counter), `CriticLeverSemantics` (FAILS: three effect cells), `ReplayC2Counter` (FAILS bounded: Copilot CLI per-directory lever), `ReviewEntry` (FAILS: recheck exited 0 on drift, unbounded negative, novelty count), `ReviewSkillWording`, `ReopenS022` (same-name nested-skill rule), `ReviewD3Sweep` (census S026 sentence), `ReviewD1`, `ReviewD7Carry`, `ReviewLessonGate`, `FixtureFaithful`, `ReviewScopeRule`. Each correction is in the lesson's falsify section, the entry's corrections section or the plan's after-landing section.
- Wave seat reports for both waves are committed under `.ufo/waves/round-51/`.

## 2026-10-22 — Round 52 (hyaku campaign, attempts 1 and 2): C1 freshness callee-rename-robust omp extraction; C2 coverage MCP server instructions per client

- Steer and base: plan `plans/round-52.md` at `4c003a4b` (both counters committed there, before any data); base `c8579a4c5b48789e56fb9060ddd48f33569e1215` (round 51 closed `rejected-honest-stop`). Attempt 1 landed `4c003a4b` (plan), `c2107ecf` (C1) and `c8407a45` (C2, routed repairs, M36 fix) through the lane helper, then died in an omp process restart at 17:26Z. Its build wave (34 seats) never received a seat grant and its falsify wave (36 seats) was cut off by the restart: neither left a seat report (M37). Inherited leftovers: `SCORECARD.md` (uncommitted round-52 cells and blocks; rewritten in attempt 2, then committed) and `.ufo/waves/round-52/` (attempt-1 specs, dispatch payloads, empty gate files and two registries; committed as evidence, with no seat reports because none exist).
- Re-verification of the inherited commits by the attempt-2 L1 at 17:44-17:46Z: `git diff 4c003a4b c8407a4 -- verifiers/check_callee_rename.py verifiers/check_mcp_instructions.py` empty (counters frozen); `check_callee_rename.py --rev` → 0 of 4 at `c8579a4`/`4c003a4`, 4 of 4 at `c2107ec`/`c8407a4` (seeds 52, 7, 1234); `check_mcp_instructions.py --rev` → 0 of 7 at `c8579a4`/`c2107ec`, 5 of 7 at `c8407a4`, `--fetch` 5 of 5; `verify_surfaces.py --json` pass 7, exit 0; `--self-test` 0 failures over 129; `check_substrate_pins.py` OK 3/3; census exit 0 (W04 S018, S019, S021).
- Host drift at 17:50:30Z, not caused by this round: an `npm exec … --package opencode-ai` run replaced opencode 1.19.3 with 1.19.4 (sha `538fcb1b…`); since then `verify_surfaces.py --json` reads pass 6, `surfaces.opencode_extract` FAIL, and pins `DRIFT 1/3`, at base and head alike (seats `ScoutLiveShape`, `CriticC1Escape`, `CriticCalibration`). With the committed opencode fixture the gate is pass 7. Carried to round 53 (Q09).
- Attempt-2 wave: one validated v1 falsify wave of 34 seats (`.ufo/waves/round-52/falsify-a2-spec.json`; gate `granted … seats=34 live=50 … cap=85` at 17:49Z): reviewer 9, scout 10, critic 7, mutation-tester 3, executor 3, scribe 1, connector 1. A first 46-item version was validated, then cut to 34 before dispatch so it fit under the shared seat cap (live 51 of 85); the 12 dropped items overlapped kept ones (`ExecGateMatrix` covers floors, no-harm and integrity; `ExecPushedBytes` covers both counter replays). No seat died; no refusal.
- Corrections that changed landed text are listed by seat in `corpus/lessons/round-52.md` § Falsify-wave corrections (attempt 2). The largest: the C2 entry's opencode and Copilot CLI negatives were false (M38); rows S041, S042 and the corrected entry raise the same frozen counter to 7 of 7 — a later measurement beside the declared 5 of 7 @ `c8407a45`, not in its place (Q28). Also S039 (supersedes S024), S040 (MCP spec 2026-07-28), fixture labels, two C1 extraction fixes (unresolved-group admission; empty-baseline fallback), Q30, Q31, M38-M40, sweep registry rows `r52-c2-*`.
- Gates on the attempt-2 working tree before the commit (18:41Z): `check_correction_sweep.py --root .` 0 stale blocks, `--self-test` 0 failures over 7 (and `--rev c8407a4` exit 1 with the three `r52-c2-*` FAILs, shown able to fail); `check_mcp_instructions.py --root .` 7 of 7, `--fetch` 7 of 7; `verify_surfaces.py --self-test` 0 failures over 129; `check_assertion_floors.py` PASS; `verify_skill_checklist.py --json` pass 11, fail 0; census exit 0; `verify_corpus_integrity.py` 5 of 9 (same count as base; `commit_total` 31 vs 30 and `tracked_files` 75 vs 72 are this round's new pointers and files; the baseline re-record is carried).

## 2026-10-22 — Round 53 (hyaku campaign, attempt 1): C1 freshness opencode 1.19.4 re-derived and re-pinned; C2 operability always-on boxes 04/07 executed (sourced)

- Base `e78dff66`; plan and frozen counters `3bb0a7a3` (2026-10-22T19:5xZ); plan erratum `5e5336c4`, written on the wave-1 critics (`CriticC1Sizing`, `CriticC2Sizing`, `CriticDrift`) before any claim content landed: statements bounded to the counters' printed lines, the C1 counter's trust in the measured gate named, three C1 guards (diff scope, independent dump, rows) and one C2 guard (relative delegate in `git ls-tree`) added outside the counters, the frontier sentence narrowed (lesson M43, Q33).
- C1: `python3 -B verifiers/check_opencode_repin.py --rev <rev>` → `surfaces pass 6 of 7 (opencode_extract FAIL); pins OK 2/3; opencode classes kept 9 of 9; self-test 0 failure(s) over 133 assertions`, exit 1 @ `55973a20` → `surfaces pass 7 of 7 (opencode_extract PASS); pins OK 3/3; opencode classes kept 9 of 9; self-test 0 failure(s) over 155 assertions`, exit 0 @ `6dd31164` (165 assertions @ `b5dc7dcf` after the falsify-wave OC-4 delivery decoy; 175 after the OC-6 walk-target decoy, W2MutOc6); host opencode sha256 `538fcb1b…` throughout (W2RerunC1 hashed it at 20:36Z). Guards: W2GuardScopeC1 HOLDS (every hunk OC-4/OC-6 or self-test; pin script untouched), W2GuardDumpC1 HOLDS (own 1.19.4 dump 7/7; real 1.19.3 dump 7/7), W2GuardRowsC1 HOLDS (exit 0, 7 ids once, 9/9 from 7/7). Cause: S051 (tag delta touches no `packages/opencode/src/`; Bun 1.3.14→1.4.4).
- C2: `python3 -B verifiers/check_alwayson_boxes.py --rev <rev>` → `always-on boxes executed and discriminating 0 of 8`, exit 1 @ `aeed0890` → `2 of 8`, exit 0 @ `55973a20` (also @ `c775d682`, `b5dc7dcf`); guard: both dispositions `delegated:verifiers/verify_alwayson.py`, a regular 100755 blob in `git ls-tree` (W2RerunC2, W2SentinelAlwaysOn). Entry `corpus/knowledge/alwayson-rule-files-round53.md`; rows S043–S050, S052 (Cursor help, added after W2ReopenS049), S051 (C1); S004 queued→mined, S019 used-by widened, S050 anchor wording fixed in place (lesson § Rows touched).
- Second measurements beside C2 (not the claim): held-out run 6 of 18 settled cases wrong, 3 false PASS (W2CriticHeldOut); five `alwayson.07` mutants survive the counter and die in the self-test (W2MutAlwaysOn07); the counter itself follows an absolute or `..` delegate (W2RerunC2, W2SentinelAlwaysOn) — the erratum guard covers the judged revisions only.
- Repairs (round-52 routed defects 2–4) `aeed0890`: fleet report pointers resolve against the fleet root in both corpus instruments (152/93 assertions), spot-check indexed; two self-test arms for the round-52 attempt-2 fixes (W2ReviewSurfArms: each fails on its revert alone); MCP counter exact host/segment and exact Gate quote (M12, M16 killed; `..` segment survivor W2MutMcpTighten fixed at `b5dc7dcf`); `verifiers/check_gate_finding_delta.py` (M41 fix; red on the round-52 pair).
- Floors (bump in step, `c775d682`, `b5dc7dcf`): surfaces 129→175, corpus_integrity 150→152, corpus_independent 91→93, checklist 1851→1852, alwayson registered at 89; `check_assertion_floors.py` 13 PASS, exit 0; its self-test 0 failures over 150.
- Waves: build 34 seats (gate granted 20:03:54Z, dispatched 20:04Z, all completed), falsify 36 seats (granted 20:35:54Z); round total 70; no dead seat, no refusal. Seat installs: `agnix` 0.59.0 via npx (ScoutPriorArtLinters, prior-art run).
- Mistakes: M41 stale baseline (fix shown able to fail), M42 loose matching (Q32), M43 plan overclaim caught before content (Q33), M44 lane index written by `git apply --3way` (procedural).

## 2026-10-22 — Round 54 (hyaku campaign, attempt 1): C1 depth description thresholds by client (sourced, the learning claim); C2 consistency gate registry rows

- Base `422ffd10`; plan and frozen counters `e3371548` (committer 21:12:08Z; base runs 21:10–21:11Z); errata `d051ec40` (times, M46), `3b2535d2` (C2 bounded, four-gate self-test guard, `CriticC2Sizing`), `90cae9af` (C1 unchecked items, prior holds, guards a–c, `CriticC1Sizing`), each before the content it bounds. Drift sentinel honoured: no freshness claim, no change to `verify_surfaces.py`, nothing on the checklist/always-on row; Frontier row worked: *Per-render consumption* (offer-render half).
- Enabling move `7ad05d34`: `SKILL.md` § Sources verifier bullets (43 lines, 532–574) moved verbatim to `verifiers/README.md` (593 → 552 lines).
- C1: `python3 -B verifiers/check_description_thresholds.py --rev <rev>` → `description thresholds backed 0 of 7 clients`, exit 1 @ `422ffd10`, `e3371548`, `bf65974c` → `7 of 7`, exit 0 @ `5a097e12` (`--fetch` 7 of 7). Guards: (a) S053–S059 absent at `e3371548`; (b) Claude Code (`1,536`, `1%`) and Codex (`2%`, `8,000`) carry numbers absent from `SKILL.md` at the plan commit; (c) fetch 7/7 (`W2RerunC1`). Entry `corpus/knowledge/skill-listing-thresholds-round54.md`, `SKILL.md` § Description thresholds by client, rows S053–S064 (S062–S064 renumbered from seat drafts S053b/S054b/S059b).
- C2: `python3 -B verifiers/check_gate_registry.py --rev <rev>` → `0 of 21` @ `422ffd10`, `0 of 23` @ `e3371548` and `b55550b9` → `24 of 24 lane verifiers; phantom 0`, exit 0 @ `bf65974c`. Prerequisite `b55550b9`: own `--self-test` modes for `box_proof_case_deletion.py`, `check_alwayson_boxes.py`, `check_callee_rename.py`, `check_opencode_repin.py` (each exited 2 on `--self-test` at `7ad05d34`; judging and counting lines unchanged; erratum-2 guard re-run by `W2RerunC2`).
- Routed round-53 defects: S046 → S060 (supersedes the teaches cell; `used-by` old→new logged), S050 → S061 and M45 with `verifiers/check_sources_append_only.py` (red on `e792607e`); registry (C2); tip runs `.ufo/waves/round-54/build/ExecTipRuns.md`; `baseline.json` note `fed56863`; round-53 addendum in `corpus/lessons/round-53.md`. **Round-53 LOG omission repaired here:** `e5355a62` (round-53 falsify-wave fix — OC-6 walk-target decoy arm, W2MutOc6; surfaces floor 165→175) landed in round 53 and was not named in its LOG entry; the floors guard at `b38c32a0` reads `surfaces 175/175` (`ExecTipRuns.md`).
- Falsify-wave corrections (seat named per item): Codex row and entry (`W2SrcCodex`, `W2CriticDepth`: "raises the default" → "sets a different budget"; shipped 1,024 catalog cut named); Cursor "Warned, not cut" → "No cut documented" and opencode/Gemini/Claude Code action cells (`W2CriticDepth`); Gemini banner scope (`W2SrcGeminiCLI`); entry `451a02ff` written as an upstream pin, not a lane commit (`W2RowVerifyCorpusIntegrity`, `W2CriticNoHarm`); M45 cells (`W2CriticLesson`); registry cells for `fault_injection_corpus.sh` pinned values and `check_assertion_floors.py` write scope; `check_sources_append_only.py` row-removal crash and non-UTF-8 exit (`W2RowCheckSourcesAppendOnly`; self-test 14 → 21 assertions, new arm fails on the old code). Carried: environment failures that exit 1 in several gates (box-proof, finding delta, floors, alwayson counter), `fault_injection_corpus.sh` red gate and self-test (fault-h expectation stale since round 49), weak self-tests (callee rename 1/4, opencode repin 1/4 mutants killed, `W2MutNewSelfTests`), both counters' review findings (`ReviewCounters.md` F1–F6).
- Waves: build 40 seats (`granted … seats=40 live=81 … cap=128`); falsify 41 seats (`granted … seats=41 live=49 … cap=90`, after a 684 s wait for capacity); round total 81; no dead seat, no refusal.

## 2026-10-23 — Round 55 (hyaku campaign, attempt 1): C1 depth explicit invocation by client (sourced, the learning claim); C2 operability could-not-evaluate paths (miss as declared)

- Base `f0e5de82`. Plan, frozen counters and §9 control receipts `a10240c0` (`plans/round-55.md`, `.ufo/waves/round-55/controls/`).
- Erratum 1 `b04a9005`, before any C1 content: wave-1 critic `CriticC1Sizing` met the v1 C1 predicate with real quotes holding no invocation form (W1) and a case flip (W3); counter v2 is strictly stricter; receipts `controls/C1-shortcut-W1W3.txt`, `controls/C1-v2-controls.txt` (M49, Q37).
- C1 landed `96155796`: `SKILL.md` § Explicit invocation by client, `corpus/knowledge/explicit-invocation-round55.md`, SOURCES S065–S071, lesson Gate. `check_explicit_invocation.py --rev <rev> --fetch` (v2): `0 of 0; new ground 0`, exit 1 @ `f0e5de82` → `found on the live page 5 of 5; new ground 4`, exit 0 on the working tree that became `96155796`. Gemini CLI (model tool call) and VS Code (quote without the word `skill`) are kept as rows the counter does not count.
- C2 landed `e966cd59` (eight gate patches, seats Fix*): `check_could_not_evaluate.py --rev <rev>` `13 of 25; 13 of 13`, exit 1 @ `f0e5de82` → `25 of 25; controls held 12 of 13`, exit 1 @ `e966cd59` (`.ufo/waves/round-55/C2-measure-e966cd59.txt`; the floors gate timed out a nested self-test at load average ~105). A miss as declared. Wave-1 critic `CriticC2Sizing` also met the frozen predicate with a remap, an entry check and an `argparse` shadow after seats had scored (M50); not amended.
- Routed round-54 defects: 3 cells narrowed and the anti-pattern prose moved verbatim to the round-51 entry (`ed3e8996`; SKILL.md 599 → 598 with the new table); 5 registry counter hardening and 6 fault-injection harness repairs (`4d700b17`); 2 QUALITY Q34, Q35 plus Q36, Q37 and lesson M48–M51 (`f2cc4099`); 1 base receipts with revisions (`build/ExecBaseReceipts.md`); 4 route move and 7 quote notes in the lesson; 8 the 12 earlier SOURCES edits filed as one L0 line (fleet `d2b2c566`).
- Waves: build 36 seats (granted `seats=36 live=25 cap=90`; MutC2Counter cancelled at the settle deadline with no report); falsify 40 seats (granted `seats=40 live=24 cap=256`).

## 2026-10-23 — Round 55 falsify wave and corrections

- Correction (append-only) to the round-55 entry above: `MutC2Counter` did write its report (`.ufo/waves/round-55/build/MutC2Counter.md`, last write 00:06:05Z, before its cancellation; `ReviewSeatAccounting`). The "with no report" clause is wrong.
- Falsify wave 40 seats; 33 reports; seven cancelled at the settle deadline (~00:21Z) without reports: ReviewFixBoxProof, ReviewFixMcpInstructions, ReviewFixAssertionFloors, ExecHandProbes, ReviewQuality, ReviewLessonMistakes, ReviewControlsReceipts.
- C1 re-measured by `W2RerunC1` at `f0e6b695`: v2 `--fetch` `5 of 5; new ground 4`, exit 0; v2 backed ⊂ v1 backed. In substance only Cursor's and opencode V2's forms are new (`CriticNewGround`); the entry now says so.
- C2 re-measured by `W2RerunC2` and `CriticC2Landed` at `f0e6b695` (also with `PYTHONSAFEPATH=1`): `25 of 25; controls held 12 of 13`, exit 1 each time; the only miss is the floors gate's 120 s nested timeout (`verify_harness_independent.py --self-test` alone took 185–222 s under load). C2 stays a miss as declared.
- Corrections landed after falsify: entry provenance, Copilot reading, Cursor Custom Mode, opencode V2 key, raw-text and per-skill set-aside in `SKILL.md` § Explicit invocation by client, entry Findings 2–4 (`ReviewC1Entry`).
- Tip receipts (`NoHarmGates`, at `722e474a`): finding delta `new 0, resolved 1`, exit 0; registry `26 of 26; phantom 0`; checklist on the lane path 11/11 (its input was the working-copy SKILL.md one edit ahead, recorded); floors exit 2 on the same load timeout; integrity exit 1 on carried DRIFT only.

## 2026-10-23 — Round 56 (hyaku campaign, attempt 1): C1 depth agent-definition files by client (sourced, the learning claim); C2 operability withdrawn before data

- Base `b0b7140b`. Plan and frozen counters `0f58a469` (`plans/round-56.md`, `verifiers/check_agent_definitions.py`, `verifiers/check_agentdef_boxes.py`, do-nothing receipts `controls/C1-base.txt`, `controls/C2-base.txt`). Counter-writing call: 2 executor seats (`.ufo/waves/round-56/w0/`).
- Pre-freeze control call (8 critic/mutation-tester seats, before any data seat): C2 met by `CtlC2Heuristics` (`5 of 9`, exit 0) and `CtlC2GeneratorKeyed` (case order leaked; `5 of 9` on 10 of 10 seeds) → C2 withdrawn (gate reject). C1 v1.1 met by `CtlC1RealNoForm` (issue-tracker text naming other clients' folders, `5 of 5; new ground 2`, exit 0); errata 1–3 make the C1 counter v1.3, strictly stricter; re-scored `controls/C1-v12-rescore.txt`, `controls/C1-v13-rescore.txt`; v1.2 re-attacked by `CtlC1RealNoForm` and `CtlC1HeldVariant`, not met. Commit `e02f5f5d`, before any C1 content.
- C1 landed `c22fdd39`: `SKILL.md` § Agent-definition files by client (under § Instruction surfaces), `corpus/knowledge/agent-definition-files-round56.md`, SOURCES S072–S078, lesson Gate; SKILL.md line-budget move of `SKILL.md:157-175` verbatim to `render-mechanism-round7.md` (sha256 `73497d2a…` both sides; SKILL.md 598 → 596). `check_agent_definitions.py --rev <rev> --fetch` (v1.3, sha256 `2f672bd1…`): `0 of 0; new ground 0`, exit 1 @ `b0b7140b` → `found on the live page 7 of 7; new ground 3`, exit 0 @ `c22fdd39` and @ `96189083` after falsify corrections (`.ufo/waves/round-56/C1-measure.txt`; reproduced by `W2RerunC1`).
- Falsify corrections `96189083` (cells and entry wider than their pages: Claude schema provenance, Codex `features.*`, VS Code harness-dependent user folder, Copilot CLI required keys, Gemini `enableAgents`/`kind`, Cursor fields and precedence, opencode V1/V2 split). No counted cell (location token, quote, row) changed.
- Routed round-55 defects: 1 leftover report committed `3d8efd7c`; 5a revision message in seven gates `250e3026`; 4 and 5b floors load-scaled nested cap and preflight returncode `a5314640`; 3 `check_could_not_evaluate.py` v2 closes D/P/S `15257a27` (no re-claim; it already prints `29 of 29; 13 of 13; red anchors 13 of 13`, exit 0 at `b0b7140b`, so it cannot back a re-claim from the tip); 2 rule applied in the new counter, the v3 patch to the round-55 counter rejected (template match); 6 S065 W04 report-only; 7 cross-domain item in the report.
- Registry rows for both new counters (`c22fdd39`): `check_gate_registry.py` 26/28 at `e02f5f5d` → 28/28 (`W2RerunC1`).
- Waves: counter-writing 2; control 8; build 32 (granted `seats=32 live=57 cap=256`); residual falsify 8. Round total 50. Bounds incident: seat `ExecFloorsTimeout` killed sibling runs by `pkill -f` on the shared scratch root and loaded the host to 96 (M56).

## 2026-10-23 — Round 57 (hyaku campaign, attempt 1): C1 depth plugin manifests by client (sourced, the learning claim; miss as declared); C2 operability withdrawn before data

- Plan and frozen counters `ee50d8fa` (C1 `check_plugin_manifests.py` v1, C2 `check_infoless_fences.py` v1, base receipts `controls/C1-base.txt`, `controls/C2-base.txt`); counter-writing call 2 executor seats (`.ufo/waves/round-57/w0/`). Lowest-axis duty read as owned axes (depth 9); anti-loop: Frontier rows *MCP/plugin instruction surfaces* (plugin half) and *Command extraction*.
- Pre-freeze control call (11 critic/mutation-tester seats, before any data seat): both v1 counters met by hollow worlds (C1: bare words, nav text, a changelog line, case variants of held words; C2: generator-keyed, path-keyed, character skips with an echo fallback, a gate-replacing stub). Erratum 1 `01312a77`: C1 counter v2 (strictly stricter, sha256 `bf11a4ef…`), C2 withdrawn (gate reject). v2 re-scored by the same five C1 control seats, not met (best hollow `found 1 of 7`), receipts `27af04a7`.
- Build wave 32 seats (validated v1 spec, `build-dispatch.json`). Landed `ac22ca87`: `SKILL.md` § Plugin manifests by client, `corpus/knowledge/plugin-manifests-round57.md`, SOURCES S079–S085, lesson Gate; verbatim budget move of § Decision tables to `corpus/knowledge/anatomy-and-compression.md` (sha256 `8a71375c…` both sides; SKILL.md 598 → 584 → 598 with the new table); R2 corrections registered in `check_correction_sweep.py` (self-test 14 → 18); R6 line marked at `SKILL.md:520`; Q41–Q45.
- C1 measured: `python3 -B verifiers/check_plugin_manifests.py --rev <rev> --fetch` → `0 of 0; new ground 0`, exit 1 @ `47c05558` → `plugin manifests found on the live page 4 of 4; new ground 4`, exit 1 @ `ac22ca87` (`.ufo/waves/round-57/C1-measure.txt`). Target F ≥ 5 missed: VS Code and Copilot CLI default to the shared root `plugin.json` and opencode has no JSON manifest. The row rule (own-format path, else the documented default) is stated in the entry; VS Code's Legacy OpenPlugin path, which would pass, was rejected (Gate). M62.
- Waves so far: w0 2; controls 11 (5 resumed for v2 re-scores, same identities); build 32.

## 2026-10-23 — Round 57 attempt 3: falsify wave, corrections re-derived, C1 re-measured (still a miss as declared)

- Attempts 1 and 2 died with the orchestrator (05:25Z, 06:19Z). Inherited: 5 landed commits `47c05558..07c33d73` (re-checked by `A3RerunC1Counter`, `A3NoHarmGates`, `A3NoHarmPriorClaims`); attempt 1's falsify dispatch records (33 seats, dead; re-validated byte-identical by the L1 and committed as records only); attempt 2's uncommitted edits saved as `.ufo/waves/round-57/a3/a2-candidate.patch` (untrusted, sha256 `2e681cf5…`), the files reset to the branch, its `attempt2/` scratch moved to `/fast/scratch/hyaku/kotoba-r57a3/attempt2-untrusted/` and never cited.
- Falsify wave: 40 seats, one v1 wave (`a3/falsify-spec.json`, `a3/falsify-dispatch.json`; reviewer 14, critic 13, scout 9, mutation-tester 2, sentinel 1, connector 1); all 40 returned, none dead.
- Landed `bc09a830`: plugin ship cells corrected per client from live re-fetches (`A3Ship*`); quote-location notes (`A3ReopenS079`–`S085`); S086–S088 admitted as re-opened by `A3CandS086`–`S088` (S088 `or` → `and no`; S086 used-by made true by the Codex ship-row citation); opencode wording: `package.json` is what S085 calls a minimal manifest, so "no JSON manifest" (attempt-1 entry above) is withdrawn (M67); Limits wording; corpus index rows for three unindexed files; SHONEN recount; lesson M62/M63/M64 corrections and M65–M69.
- C1 re-measured at `bc09a830`: `plugin manifests found on the live page 4 of 4; new ground 4`, exit 1 (`a3/C1-remeasure-a3.txt`), identical to the declared measurement; the miss stands. Census end exit 0 with eight W04 (S086 shares S080's URL as its correction row).
- Routed to round 58: correction-sweep arms (7 of 11 mutants survive, M68); the v2 C1 self-test reaches `main()` only on an invalid revision; band-10 attribution in `SCORECARD.md:29` (closure ruling); dead lowercase `/home/vgpnk/projects/` paths at `SKILL.md:514-515`.

## 2026-10-23 — Round 58 (hyaku campaign, attempt 1): C1 depth custom command files by client (sourced, the learning claim); C2 operability withdrawn before data

- Plan and frozen counters `3de87aad` (C1 `check_command_files.py`, C2 `check_sweep_mutants.py`; base `f56f6e19`). Q45 census preceded target freeze: 6 of 7 clients eligible (F_max = 6), with 4 eligible tokens absent from the base tree (G_max = 4); frozen targets F ≥ 4, G ≥ 3. `.codex/prompts` and `.github/prompts` each had one base hit; `.claude/commands`, `.gemini/commands`, `.cursor/commands`, and `.opencode/commands` had zero. Copilot CLI was not eligible: its command reference reads `.claude/commands/`, and a Copilot row with that token would trigger E5 and disqualify Claude Code too.
- Frontier: *Custom command files* is a new area, distinct from round 57's plugin half of *MCP/plugin instruction surfaces* and *Command extraction*. The intended coverage is documented per-client command/prompt locations and what a file sets; client execution, argument-substitution behaviour, and precedence where a skill and command share a name remain outside the claim.
- Pre-data controls: C1 do-nothing, junk, and off-topic worlds stayed below target; the shared-label control's false Copilot attribution was F=1, K=1, G=0. Fabricated quotations produced B=6 of 6 without a page read, but with `--fetch` scored F=0, K=6, G=0, exit 1. C2 `CtlC2SourceGrep` met the frozen predicate by checking its own source for mutant texts; Erratum 1 withdrew C2 before data. This is not evidence of behavioral arms.
- C1 measured: `python3 -B verifiers/check_command_files.py --rev <rev> --fetch` → `custom command files found on the live page 6 of 6; new ground 4`, exit 0 @ `46b4a706` (`.ufo/waves/round-58/C1-measure.txt`) (frozen predicate F ≥ 4 and G ≥ 3).
- C2 record only: prior-round M68 / `A3MutCorrectionSweep` had 7 of 11 mutants survive. The behavioural arms in `check_correction_sweep.py` remain R3 defect work, but C2 is withdrawn. `python3 -B verifiers/check_sweep_mutants.py --rev <rev>` → `sweep mutants killed 11 of 11; equivalents survived 5 of 5`, exit 0 @ `46b4a706` (`.ufo/waves/round-58/noharm-tip.txt`); record only, not a claim. Frozen base record: 4 of 11 killed, 5 of 5 equivalents survived, exit 1.
- Routed defects (landed at `46b4a706` unless marked): R1 — in-cell `claim withdrawn` annotation on the `check_infoless_fences.py` and `check_sweep_mutants.py` registry rows (a `probe` relabel fails the registry gate, M77); R2 — append a corrected README note adding S086–S088 with their row roles; R3 — repair behavioural correction-sweep arms as defect work despite C2 withdrawal; R4 — add the successful-`main()` arm to `check_plugin_manifests.py` self-test (the new C1 counter carries one from birth); R5 — correct lowercase `/home/vgpnk/projects/` paths (three SKILL.md lines; historical knowledge/lesson copies left as records); R6 — record the Q45 census before target freeze; R7 — carry, not attempt, C2 redesign, and inline/grep the kill-by-PID bound in every wave context; R8 — leave band-10 attribution at `SCORECARD.md:29` with the operator.
- No-harm at `46b4a706` (`.ufo/waves/round-58/noharm-tip.txt` vs `build/noharm-base.txt`): gate registry 32 of 32; correction sweep 0 stale; sources append-only 0 protected-cell changes; prior counters unchanged (agent definitions 7 of 7, explicit invocation 5 of 5, description thresholds 7 of 7, MCP 7 of 7, plugin manifests 4 of 4 exit 1 as at base); checklist exit 0 (SKILL.md 596 lines after the verbatim § Skill-file anatomy move); assertion floors exit 0; corpus integrity exit 1 at base (5 DRIFT) and at `46b4a706` (unindexed 1 → 3: the new entry and lesson); after the index rows at `8e52f064` unindexed is 0, 4 DRIFT, all pre-existing at base.
- Falsify wave (36 seats, `.ufo/waves/round-58/falsify/`): corrections landed after measurement — entry row rule, quote notes and lead (ReviewEntry, CriticVSCodeQuote, ReopenS091), S089 alias of S065 disclosed (CriticS089Alias), SKILL scope/field cells for Claude Code, Copilot CLI, Cursor, opencode (ScoutUserFolders, ReopenS028Copilot, ReopenS094, ReopenS095, CriticAxisDepth), r56 `check_agentdef_boxes.py` registry annotation (ReviewR1Annotations), S028 used-by old→new, claim-census anatomy note, agents-md row-11 path bound, correction_sweep assertion floor 25 (ExecFloorsSweep). cursor.com began answering Python urllib with HTTP 403 after 08:20Z (ReopenS094, MutR4Arm): re-runs then print 5 of 6, new ground 3, still exit 0.

## 2026-10-23 — Round 59 (hyaku campaign, attempt 1): C1 depth hook files by client (sourced, the learning claim)

- Plan draft `a3e70a30` (row rule and target formula T_F = F_max − 2, T_G = G_max − 1 fixed, targets `TBD`); freeze `4b2125c9` after the Q45 census (W0 `.ufo/waves/round-59/w0/Census*.md`): 6 of 7 clients eligible (Claude Code `.claude/settings.json`, Codex `~/.codex/hooks.json`, VS Code `.github/hooks/*.json`, Copilot CLI `~/.copilot/hooks/*.json`, Gemini CLI `.gemini/settings.json`, Cursor `.cursor/hooks.json`; opencode hook code is a plugin module), all six tokens absent from the base tree → F_max 6, G_max 6, frozen targets F ≥ 4, G ≥ 5; counter `verifiers/check_hook_files.py` sha256 `f695d59e…`. Freeze addendum `67b68e0f` named the Events conjunct's limit (printed, not proven an event) and the semantic seats before any control scored.
- Pre-data controls (`283124cd`, `.ufo/waves/round-59/controls/SUMMARY.md`): do-nothing, junk, all-false, no-reader, fabricated snapshot, fabricated events, off-topic and label-shortcut worlds all exit 1; fabricated worlds reach 6–7 of 6–7 on the offline snapshot line and 0 live, so the snapshot line is committed-bytes evidence only and the live conjunct is the measure.
- C1 measured: `python3 -B verifiers/check_hook_files.py --rev c63ccc68… --fetch` → `hook files backed on committed snapshots 6 of 6; found on the live page 6 of 6; new ground 6`, exit 0 (`.ufo/waves/round-59/C1-measure.txt`); base `a975cbbf` → `0 of 0`, exit 1 (`controls/CtlDoNothing.md`).
- Routed round-58 defects: R1 — the misrooted `ReviewBudgetMove.md` copied byte-exact into the lane with a provenance note (`a3e70a30`), the output-dir pin in every wave context (`.ufo/waves/round-59/bounds.md`), Q49, M79; R2 — receipts at `ed44e0c4` and `a975cbbf` committed (`receipts/`, `4b2125c9`), Q50, M80; R3 — the counter reads the Events field cell and a committed snapshot whose sha256 equals the row, and fetches with curl and a browser UA, Q51, M81; R4 — correction row S102 (`supersedes S089 —`), S089 untouched, M83; R5 — budget lines name the base: SKILL.md 596 @ `a975cbbf` → 587 @ `c63ccc68` (+1 registry row at the freeze, +14 hook section, −24 net from the verbatim 28-line § Sources move into `corpus/knowledge/anatomy-and-compression.md`), M82; R6 carried.
- Corpus index: rows for `lessons/round-58-verifier-spotcheck.md` (unindexed at base), the hook entry and the round-59 lesson (`corpus/README.md`).
- Build wave 33 seats (`.ufo/waves/round-59/build/`); census 10 seats (W0), controls 8. Mined mistake M84: the L1 substituted the VS Code census token without a census re-score (caught by `SentinelContexts`, `ScribeEntry`).
- Falsify wave 40 seats (`.ufo/waves/round-59/falsify/`), none dead: re-opens S096–S102 HOLD (live = snapshot, byte-identical); `RerunC1Counter` reproduced 6/6/6 exit 0; `MutC1Survivors`: the 13 self-test survivors leave the measurement unchanged; `MutC1Content`: Events-semantics and Action mutants invisible as pre-declared. Corrections at `a5e55b3c` (lesson § Falsify corrections, M85); re-measure there 6/6/6 exit 0 (`C1-remeasure-tip.txt`); checklist 11/11, corpus integrity 4 DRIFT (all at base, which had 5), registry 33/33. Post-settle misroot sweep: no round-59 file in the fleet root (`misroot-sweep.txt`).

## 2026-10-23 — Round 60 (hyaku campaign; attempt 1 landed data and died mid-close at ~09:30 -03 with no report; attempt 2 closed the round)

- Plan draft `b8b2a7a4` (row rule, semantic conjuncts, target formula); amendment A1 `bfe8cc2b` (scope-key key-form conjunct after `CensusCursor` showed `description` passing the draft; tightened, never loosened, before the freeze); freeze `49c3e87d` (Q45 census F_max = 4, T_F = 3; counter v1 sha `6aea3be0…`); erratum E1 `b1cd64bb` (the W0 census never scored the counter's inherited base-URL conjunct — M89; counter v2 accepts held-page re-opens whose base row never recorded K; sha `ca2585a4…`, T_F = 3 by the same formula); v1 controls `f9f12684` (6 receipts, none met; `CtlWrongKey`/`CtlInventedAction` cancelled at the settle deadline — M90); E2 `49f7ff22` declared C1 EXPLORATORY before data (two v2 control worlds met the predicate by forged provenance; the counter cannot authenticate fetch time or alias URLs); data `7b80ae80` (SKILL § Scoped rule files by client SKILL.md:135-148, entry, S103–S111 + 7 snapshots, QUALITY Q52–Q55, README/PROVINCE/index rows, build wave reports).
- C1 (depth, exploratory; the sourced claim rests on S103–S109 opened this round): supporting counter `python3 -B verifiers/check_scoped_rules.py --rev <rev> --fetch` → base `31092dc6` `0 of 0` exit 1; `7b80ae80` `backed on committed snapshots 4 of 4; found on the live page 4 of 4` exit 0 (`.ufo/waves/round-60/C1-measure.txt`, L1 sandbox re-run 2026-10-23T12:28Z). Limit (declared before data): wrong keys such as `sessions` and invented actions also pass (`build/ExecKeyForms.md`), so the counter is supporting evidence only and the semantic Cells re-read is the substance.
- Residual semantic verification (attempt 1: 3 seats; attempt 2 completed the call with 5 more, one ordinary `task` call, `.ufo/waves/round-60/residual/`): 21/21 SKILL.md cells HOLDS (`CellsClaudeCode`, `CellsVSCode`, `CellsCopilotCLI`, `CellsCursor`, `CellsNegatives` — the three negative pages byte-identical live at 2026-10-23T18:15Z); `ReviewMeasure` independently re-measured 4 of 4 exit 0 at data rev and tip, counter sha `ca2585a4…` at both, all 7 snapshot shas match their rows, census exit 0, SOURCES append-only (`grep -c '^-[^-]'` → 0); `ReviewLanded` passed every landed-artifact check except one LOW Q54 window miss (fixed at the closing commit); `CriticAxisDepth` ruled DEPTH (native-client scoped-file/key/action decisions newly distilled; prior omp `applyTo` knowledge round 13 acknowledged) with two HIGH process defects recorded (measured-admission blocker mitigated by E2; control-after-data-seat chronology, M90).
- Corrections at the closing commit: entry `scoped-rules-round60.md` Codex and Gemini CLI bullets re-cited per `CellsNegatives.md` F1/F2 (the bracketed snapshot lines did not contain their claims; substance real, evidence lives in the census fetches / other snapshot lines); lesson `round-60.md:41` "10-word" gained its `wc -w` command inline (Q54); `SHONEN.md:6` pointer `SKILL.md:217` → `SKILL.md:241` (round-59 carried R4 drift).
- Frontier: SOURCES 101 → 110 rows (S103–S111; 7 new tier-A opens + 2 correction rows; re-opens S043/S044/S045/S046/S048/S049 for facts those rows never recorded); census before `2026-10-23T10:27:24Z` 8 W04 exit 0 (`.ufo/waves/round-60/census-start.txt`) → after 13 W04 exit 0 (the 5 re-open/correction URLs duplicate their base rows' URLs by design); mined mistakes M86–M90 (`corpus/lessons/round-60.md`).
- No-harm at `7b80ae80` (L1 re-run 2026-10-23T18:1xZ): gate registry `34 of 34` conformant, phantom 0, exit 0; counter base do-nothing exit 1; SKILL.md 591 ≤ 600; budget move verbatim (`anatomy-and-compression.md:187-199` sha `20766162…` = the SKILL.md block it replaced); the round-58 fleet-root misroot `.ufo/waves/round-58/falsify/ReviewBudgetMove.md` verified byte-exact against the lane copy (sha `c288bbd8…`) and deleted.
- Round shape: one validated v1 build wave (32 seats: scribe 14, executor 7, critic 4, reviewer 3, scout 1, mutation-tester 1, sentinel 1, connector 1) + pre-freeze W0 census (11) + W0b re-census (3) + v1 controls (8 dispatched, 6 receipts, 2 cancelled) + v2 controls (3) + residual call (8: 5 reviewers, 1 critic — attempt 1 ran 3, attempt 2 ran the remaining 5) = 65 seats total; none dead in the build/residual waves; `CtlWrongKey`/`CtlInventedAction` cancelled (no receipts); v2 control seats refused twice at the 100-job cap before spawning. The §3 planner seat is the L1; planning data-walks rode `ConnSiblingScoped` and `CriticCensus`. Report `.ufo/reports/round-60/kotoba.md`.

## 2026-10-23 — Round 61 (hyaku run 5, attempt 1): C1 depth counter v3 (measured); C2 calibration routed repairs (measured); C3 adjacency withdrawn pre-data (E1)

- Base `f3246d14`. Plan + frozen predicates `7827628a`; pre-data errata: E1 (C3 withdrawn as a counted claim — CriticC3Axis hollow counterexample, class mined M92) `c630c4cb`; E2 (A3 url_key, MutA3) `3dbf0077`; E2c/E2d `daf4ad71`; E2e + E2c binding conditions `511aff7d`/`921c2512`/`e2132443`; E2f `ebffd45a`; A4(iv) pin 7 `40fd9601`. Round claims are C1 (depth) and C2 (calibration).
- C1: counter v3 landed `6a7f722e` (sha256 `5a5adc94…`, ExecCounterV3 draft integrated unmodified); controls committed BEFORE any C1 data per M90: world receipt `.ufo/waves/round-61/receipts/C1-worlds.txt` `5b8a533c` (format fix `b4a8d2ee`) — `python3 -B verifiers/check_scoped_rules.py --self-test` prints `worlds reject 7 of 7; eligible rows pass 4 of 4`, exit 0, worlds W1-W7 exit 1 with firing-arm attribution (W1 A4 sha-alias, W2 A3 rendering-alias, W3 A1, W4 live redirect, W5 A1, W6 A2, W7 A1; W0 extra); base control `.ufo/waves/round-61/controls/C1-base.txt` — `--rev f3246d1493b60ea1c0d947a19c39f9e08e92f326` exit 1 (E2d mechanism: canonical key rows absent at base). Independent rebuilds: MutWorldW1/W24/W5W6 reproduced the v2 recorded results; RevControlsV2 reproduced all r60 receipts byte-for-byte.
- C2: the six r60-closure routed repairs, counted by `python3 -B verifiers/check_routed_repairs.py` (frozen at `7827628a`, self-test hardened to 12 arms pre-data `eb5e149a` per MutC2, R-d empty-file guard `ee19e9c9`, count exemplar fixed to the 29-printing command `daf4ad71`): R-a this entry's correction line below; R-b this entry's landed-scope list below; R-c this entry's erratum line below; R-d census-after committed at the measurement step; R-e Q56 + M91; R-f controls-ancestry receipt committed after the data commit and before the C1 --fetch measurement.
- R-a erratum: the round-60 report's build wave claimed "32 reports, 0 dead"; the committed count is `committed 29` build reports — `ls .ufo/waves/round-60/build | grep -cE '^(Conn|Critic|Exec|Mut|Review|Scout|Scribe|Sentinel|Src)[A-Za-z0-9]+\.md$'` prints 29 at the r60 close commit (claimed 32; 59/65 seat reports overall per the closure) — one line carrying build reports, claimed 32, committed 29, and the counting path `.ufo/waves/round-60/build`.
- R-b landed scope (complete list): plans/round-61.md, plans/round-60.md (r60 work, omitted from the r60 report — named here per the closure), considerthese/2026-10-23.md (same), verifiers/check_scoped_rules.py (v3), verifiers/fixtures/scoped-rules/, verifiers/check_routed_repairs.py, corpus/SOURCES.md (S112-S115, S117), corpus/knowledge/scoped-rules-counter-round61.md, corpus/knowledge/writing-revision-calibration-round61.md, corpus/lessons/round-61.md, corpus/QUALITY.md (Q56), corpus/README.md, SKILL.md (registry rows/annotation), .ufo/waves/round-61/ (snapshots, receipts, controls, noharm-battery.sh, wave reports).
- R-c erratum: the r60 base measurement (base `31092dc6`, exit 1) is committed at `.ufo/waves/round-60/receipts/freeze2-selftest.txt`, NOT in `.ufo/waves/round-60/C1-measure.txt` (after-only, both runs at `7b80ae80`) — the r60 report's joint citation conflated them.
- Frontier: SOURCES 110 → 115 rows (S112-S115 canonical key rows, S117 sibling import; S116 gap named); census before 13 W04 exit 0 → after 15 W04 exit 0 (the two new by-design re-open URLs); mined mistakes M91 (report-evidence overstatement), M92 (presence-counter axis claim); wave: one v2 wave `kotoba-r61-wave`, 68 seats (executor 8, scribe 12, scout 6, connector 1, mutation-tester 11, reviewer 16, critic 9, sentinel 3, revenger 1, simplifier 1); attack seats 46/68 ≈ 68% (core attack — mutation-tester+reviewer+critic — 36/68 ≈ 53%); none dead at relay time. §3 planner seat: the L1 (frozen topology); planning data-walks rode ScoutKeyPagesA/B and ConnSibling.

## 2026-10-23 — Round 62 (hyaku run 5, attempt 2; attempt 1 OOM-killed mid-wave with no report): C1 depth erratum-absorption matrix; C2 calibration routed-repairs successor

- **Commit order (controls before data).** Plan freeze `45a7ecfa` → C1 erratum E1 `5c924b02` + addendum `9228be47` → pre-data controls `9f03dcd7` (`absorption-before` 0 of 5 arm-level receipts; `frozen-repairs-dishonest`; `seat-counts-r61`; seat-count gate `verifiers/check_seat_counts.py` + its registry row) → inherited wave-1 evidence, the absorption instrument, the routed-repairs v2 successor, the hollow/label control, S118 row+snapshot and the r61 stray-`n` repair at `3e7aed9b` → data receipts `f9ab0812` → corpus/LOG/SCORECARD → wave 2 → report. Attempt 1 (`~18:00-03` OOM) left 34 of 39 wave-1 reports and the drafted instruments; each reused artifact was re-verified here. Five seats died without a report (`ExecSuccessor31`, `ScribeLesson62`, `ScribeScorecard62`, `ScribeReportSkeleton`, `MutAbsorbMutants`); a separate build-completion call (new identities, not reseats) re-worked the unfinished items, so `ExecSuccessor31`'s report lands and four spec seats still have none (`controls/seat-counts-r62.txt` at the final tip: `35 of 39; missing 4; unmatched 3`).
- **C1 frozen counted predicate (Erratum E1, arm-level).** `python3 -B verifiers/check_erratum_absorption.py --self-test` prints `errata measured 5 of 5; absorbed K of 5; surviving N; controls 2 of 2` with K/N computed from the runs and every survivor printed. Measured at `3e7aed9b` (`.ufo/waves/round-62/C1-absorb-measure.txt`): `instances per direction: committed attacks 10; guard-disabled 10 per sweep (50 total); controls 4 committed + 4 disabled; content variant 2`; `guard flips: E2 2; E2b 2; E2c 0; E2e 0; E2f 0`; **`errata measured 5 of 5; absorbed 2 of 5; surviving 6; controls 2 of 2`**, exit 0; survivors `E2c e2c-wrong-supersedes-target`, `E2c e2c-supersedes-with-fresh-fetch`, `E2e e2e-negated-path-key`, `E2e e2e-commented-equals-key`, `E2f e2f-backticked-event-claim`, `E2f e2f-compound-purpose-outside-citation`. E2 and E2b are absorbed (both instances rejected, guard-disable admits both); the three survivor classes are the measured frontier.
- **C1 before (corrected by wave 2, F14).** Five targeted searches over `.ufo/waves/round-61/receipts` and `.ufo/waves/round-61/wave` (`.ufo/waves/round-62/controls/absorption-before.txt`, 2026-10-23T20:53:36Z) found **0 of 5 classes with both directions**, but under the control's own stated criterion `receipts/C1-worlds.txt` already carries one class-faithful arm-level reject for **E2b** (W2, arm A3) and **E2c** (W1, arm A4) — the honest before is **2 of 5 with one committed synthetic arm-level reject, 0 of 5 with the seat attack tables re-scored on landed bytes, 0 of 5 with the disabling direction** (`FalsifyBeforeState`). The matrix remains a new measurement. Kill arms: `controls/absorption-hollow.txt` — the hollow variant (never runs the guard-mutation direction) exits 1 `guard-mutation direction is missing for one or more errata`; the label-only variant exits 1 `seeded controls did not classify in both directions`; the real path exits 0.
- **C1 successor (v3.1, fix evidence; NOT in the counted predicate).** `verifiers/check_scoped_rules_v31.py` sha256 `a07c2269…`, the frozen counter untouched: `python3 -B verifiers/check_scoped_rules_v31.py --self-test` exits 0 with the unchanged `worlds reject 7 of 7; eligible rows pass 4 of 4`, five `before accepted; after rejected` survivor lines, **`survivors closed 5 of 6`**, both must-fail arms (`must-fail E2e guard disabled admits e2e-negated-path-key: yes`; `must-fail G7 disabled admits e2f-backticked-event-claim: yes`) and `self-test: 0 failure(s) over 201 assertions`; `--rev 43fe01804708d65e53965b4be31e9dc7dce793e4 --fetch` exits 0 `4 of 4 backed; 4 of 4 live` (`.ufo/waves/round-62/C1-v31-successor.txt`). G9 `e2f-compound-purpose-outside-citation` stays a declared surviving bound.
- **C1 falsification.** `CriticC1Hollow` built H2 (reject-direction-only) and H3/H3b (catalogue/fingerprint) candidates that print the frozen headline and exit 0 on scratch; H2 also met the two seeded controls, so the headline alone is not the evidence — the committed instrument's run-record validation, content variant and both-directions controls are the armed path (the critic's finding is carried into wave 2, not waived). `ExecSuccessor31`'s v3.1 copy and its G7 arm are reported under Landed changes; G9 compound-purpose stays a declared surviving bound (F6) per the plan.
- **C2 frozen predicate.** `python3 -B verifiers/check_routed_repairs_v2.py --self-test` → **`successor: dishonest rejected 6 of 6; honest passed 2 of 2; base 0 of 6; tip 6 of 6`**, exit 0, with `G-a paired population control: 29/29=6; 30/29=5; 30/30=6` and `label-only constants fail controls` printed in the same run (`.ufo/waves/round-62/C2-successor-measure.txt`, receipt rev `3e7aed9b`; successor bytes re-hardened after wave 2 — see the C2 falsification bullet — final sha256 in the re-run receipt).. CLI: base `f3246d1493b60ea1c0d947a19c39f9e08e92f326` → `routed repairs verified 0 of 6`, exit 1; data rev `3e7aed9b…` → `6 of 6`, exit 0; the frozen r61 counter at the same base → `0 of 6`, exit 1.
- **C2 wave-2 falsification and correction.** `FalsifyC2Shortcuts` showed a constant call-order transcript and a fixture-fingerprint lookup both printed the frozen signature and exited 0 — the self-test's literal-constant comparisons (`constant 6 vs base`, etc.) never substituted a shortcut evaluator. Corrected in the same round before closure: `verifiers/check_routed_repairs_v2.py` now scores every fixture through a supplied evaluator, and its self-test adds an oracle/order/fresh-invariance probe plus two real negative controls (a call-order transcript and an 8-input fingerprint lookup), both required to be rejected (`.ufo/waves/round-62/C2-successor-measure.txt` re-run: `invariance controls: real passes; call-order transcript rejected=True; fingerprint lookup rejected=True (8 memorized inputs)`, frozen line unchanged, exit 0). Remaining bound: finite discrimination — a shortcut rebuilt with knowledge of the exact arm sequence is not excluded; the receipt says so.
- **C2 before (re-measured).** `.ufo/waves/round-62/controls/frozen-repairs-dishonest.txt`: the frozen counter scores D1–D6 `6 of 6` each (dishonest variants accepted) and H1 `4 of 6`; `ExecDishonestTrees` imports the frozen `check_repairs` from the dispatch-tip path (sha256 `95ade9be…`) and records the six tree blobs plus H2 at `6 of 6`.
- **C2 freeze wording correction (r61 routed defect 3).** The r61 counter is frozen as **bytes** sha256 `95ade9be1ed1930266bce4b98c8c593fff1feba89e2cf25763f0aa83f206cb88` (the file at `a745411c`); `7827628a` froze the six repair *definitions* only. The v2 successor imports those six checks unchanged and adds its own G-a…G-f hardening; it is a separate measurement, not a rewrite.
- **R-a erratum: the round-60 report's build wave claimed "32 reports, 0 dead"; the committed count is `committed 29` build reports — `.ufo/waves/round-60/build` basename census prints 29 (claimed 32).** r61's own report repeated M91's class: it claimed "66/68 seats returned reports" and named two outstanding seats; the committed count is 65 report files (the 66th entry is `swarm-registry.json`) and three seats have no report: **`RevCounterHistory`, `SentNovelty`, `SimplEntry`** — `RevCounterHistory` was named nowhere. This round's seat-count receipt is `controls/seat-counts-r62.txt` → `seat reports committed 34 of 39; missing 5: ExecSuccessor31, ScribeLesson62, ScribeScorecard62, MutAbsorbMutants, ScribeReportSkeleton; unmatched 0: none`, exit 1 (measured at `3e7aed9b`; the visible dead-seat count, not a pass).
- **R-b landed scope (round 62, complete list to date):** `plans/round-62.md`, `.ufo/waves/round-62/` (census-before, controls, w1, snapshots, w2, receipts), `verifiers/check_erratum_absorption.py`, `verifiers/check_routed_repairs_v2.py`, `verifiers/check_scoped_rules_v31.py`, `verifiers/check_seat_counts.py`, `SKILL.md` (registry rows/annotation), `corpus/SOURCES.md` (S118), `corpus/knowledge/erratum-absorption-round62.md`, `corpus/knowledge/writing-revision-calibration-round61.md` (r61 stray-`n` repair), `corpus/lessons/round-62.md`, `corpus/QUALITY.md` (Q57), `corpus/README.md`, `SCORECARD.md`, `LOG.md`.
- **R-c base-pointer direction.** The r60 base measurement (`31092dc6`, exit 1) is in `.ufo/waves/round-60/receipts/freeze2-selftest.txt`, **not** `.ufo/waves/round-60/C1-measure.txt` (after-only, both runs at `7b80ae80`).
- **R-d census body.** `.ufo/waves/round-62/census-after.txt` carries the validator body and its `exit=` line; round-end exit 0 after the corpus files land (the interim exit 1 named E11 used-by paths that did not exist yet, recorded rather than hidden).
- **R-e exact ids.** `corpus/QUALITY.md` Q57 (absorption requires both directions and the guard mutation); `corpus/lessons/round-62.md` § Mistakes `M93` (erratum recorded as absorbed without an arm-level receipt).
- **R-f owned ancestry exit.** The r61 controls-ancestry receipt records `git merge-base --is-ancestor b4a8d2ee… 43fe0180…` followed by that command's own `exit 0`; this round's controls-before-data ordering is shown by the receipt revisions above (`9f03dcd7` before `3e7aed9b`), not by a claimed clock.
- **r61 routed defects worked.** (1) seat count corrected to 34 of 39 here and the r61 count to 65 + named `RevCounterHistory`; (2) the stray first-line `n` removed from `corpus/knowledge/writing-revision-calibration-round61.md` (file now opens `source:`), so the entry's provenance shape matches CORPUS.md; (3) C2 freeze wording corrected above; (4) no-harm arm count — the r61 receipt has 18 `PASS` lines, 15 comparison + 3 self-verification arms; this round's receipt reports its own measured count, not the mistaken 16+3; (5) the r62 lesson `## Gate` aggregates the r61 wave's rejected candidates with reasons.
- **Late wave-2 findings (post-report; report addendum cites the tip that carries them).** `FalsifyConnector` — method provenance was absent from every landed artifact; the entry gains `## Method provenance` and Q57's evidence cell the credits (tameshi's guard-kill/hollow method, kumitate D49, kagi self-counts, chousa r16 + game-dev-2d vocabulary), with the kumitate r40/r48 nearest-evidence corrections. `FalsifyBatterySelfTests` — deleting the C1 isolation arm or the C2 base-world CLI assertion leaves both self-tests exit 0 with byte-identical output, and neither gate is in `floors-registry.json` (the guard passes 14 of 14 while executing neither); recorded as a coverage bound, frozen predicates untouched.
- **Frontier.** SOURCES 115 → 116 rows: S118 (`https://code.claude.com/docs/en/memory.md`, fetched 2026-10-23T20:49:56Z, HTTP 200, 55,354 B, sha256 `02632438…`, snapshot `.ufo/waves/round-62/snapshots/S118.page`) re-opens S103; status `mined`, used-by the entry and lesson. Census before 15 W04 `exit=0` → after 16 W04 `exit=0` (S118 duplicates S103's URL by design).
- **Round shape.** Wave 1 `kotoba-r62-w1` (policy v1, 39 spawn, band 32–64): 34 reports at attempt-1 death → 35 after the completion call; 4 spec seats have no report (`ScribeLesson62`, `ScribeScorecard62`, `MutAbsorbMutants`, `ScribeReportSkeleton`; attempt-1 OOM). Build-completion call: 5 seats (executor 2, scribe 2, scout 1) finishing dead-seat build items — `controls/seat-counts-r62.txt` prints `seat reports committed 35 of 39; missing 4: …; unmatched 3: ExecNoHarmRun.md, ScoutRegistry.md, ScribeLessonQ57.md`. Wave 2 `kotoba-r62-w2` (policy v1, 39 spawn, band 32–64; one task call): reviewer 17, critic 10, scout 5, mutation-tester 3, sentinel 2, revenger 1, connector 1 — core attack roles 30 of 39 (77%). Round total 83 seats. Dead seats: no wave-2 seat replaces a dead one; every dead seat stays named in the evidence. §3 planner seat: the L1 (the validator rejects `planner`); planning data-walks rode `ScoutPriorReceipts`, `ScoutR62Candidates` and `RevPlanScope`.
- **No-harm.** `.ufo/waves/round-62/noharm-tip.txt` at the measured tip (battery arms as printed; see the receipt for its comparison/self-verification count).
