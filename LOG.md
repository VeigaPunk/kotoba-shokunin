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
