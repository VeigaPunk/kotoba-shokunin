# Lessons — round 10

Round: 10. Axis: **depth** — turn the harness claim set from hand-run recipes
into a committed, executable verifier. Evidence: `LOG.md` round-10 entry, commit
`abef8aa` (this file's hash pin is the follow-up corpus commit, per the round-9 pattern),
report `/home/vgpnk/Projects/shokunin/.ufo/reports/round-10/kotoba.md`, artifacts
`verifiers/verify_harness_claims.py` + `verifiers/baseline.json`,
`corpus/knowledge/harness-verifier-round10.md`. 14 L2 lanes ran this round in
two batched `task` calls (MISSION.md floor: 8): scout ×2, executor ×2,
critic ×2, reviewer, connector, sentinel ×2, distiller, labrat, mutation-tester,
simplifier.

## Worked

- **The depth ceiling named at round 9 was real and got paid.** Round 9 recorded
  depth 8 "not 10: checklist execution is still lane-attested". The harness half
  is now machine-checked: `python3 verifiers/verify_harness_claims.py` →
  `27/27 checks pass`, exit 0 on the live host, exit 1 on a perturbed baseline
  (naming the perturbed checks), exit 2 with an unreadable environment, exit 3
  with no baseline; `--self-test` → `0 failure(s) over 10 assertions`. The fixed
  checks include the one that matters for craft: the newest captured `<skills>`
  block renders **17/17 lines from cache**, so no offered skill is currently on
  the truncator path.
- **Authority moved from disassembly to source.** omp ships as a Bun single-file
  executable with **readable embedded JS**: `A8n` (cache key), `H7s`
  (`previewSkillDescription`), `ldl` (compressor acceptance: one line, ≤160
  chars, ≤12 words), `nV.render` = `cache.get(key) ?? previewSkillDescription`.
  Round 7 cited ELF offsets and a `slice(0,99)` literal; both drift across
  builds. This round cites functions and anchors (`strings`/byte-anchor on the
  prompt), so a build change moves `omp.elf.template_sha256` loudly instead of
  silently invalidating prose.
- **A routed lane claim was falsified by three independent lanes.** Round 9
  quoted the keyed template as the routing-hint sentence. The hashed constant is
  the whole 273-byte bunfs file — the sentence **plus** `Skill: {{name}}` /
  `Description: {{description}}` (placeholders are hashed verbatim) — sha256
  `c1f03c8e248eb40e…`. Measured: the round-9 quote alone reproduces **0/17**
  keys; the full blob reproduces 17/17 under the style-aware salt. Confirmed
  independently by the critic (`PlanContract`), the executor's own
  implementation (`omp_verify.py` → 17/17, and 11/11 of this repo's `omp.*`
  baseline values) and the scout (`17/17`, template bytes + sha256 identical).
  Corrected in `corpus/knowledge/harness-router-models-round9.md`,
  `SKILL.md` § Sources and the new round-10 artifact.
- **The verifier found a false negative in itself.** The first run of the
  catalogue check reported 16/17 with `wwkd` missing. Cause: the block lives
  inside a session jsonl record, so `wwkd`'s render arrives as
  `\"plan this\"`; matching raw bytes invents a staleness finding. Decoding the
  record (`json.loads` → walk every string) gives 17/17. Same defect class as
  the round-9 description census (escape vs byte), caught because the mismatch
  was inspected rather than explained away.
- **The offer-gate root list was incomplete in round 9.** `~/.agents/skills` is
  the root carrying 15 of the 17 offered names (plus `~/.omp/agent/skills` for
  `kimi-webbridge`/`ufo`); without it only 12/17 keys are discoverable. Two
  entries there (`sekhmet`, `xbrd`) are dangling symlinks and are recorded as a
  baseline count, not ignored.
- **Independent audit adopted, not absorbed.** The aggregator lane wrote and
  committed `corpus/lessons/round-6-aggregator-audit.md` as `778310d` (a child of
  `8e22a41`, the round-9 close) while this round was running: audited HEAD
  `8e22a41`, verdict **not conformant**. Its content was taken as ground truth
  (not re-run to confirm), indexed, and every kotoba-owned defect closed inside
  this repo — ledger below. The one finding routed back out is the
  `AXES.md`↔`MISSION.md` axis-set mismatch (`consistency`, `novelty` are not
  among the six axes).

## Failed / weak

- **A first-run false negative shipped to the console before it was caught**
  (16/17, `wwkd`). The lesson is specific: when a per-item check disagrees with
  a lane's independent measurement, inspect the disagreeing item — do not
  re-explain the aggregate.
- **A lane's negative claim needs its sweep.** The fixture lane reported
  "unverifiable today: plain single-line, `>-`, quoted…" while `>-` and plain
  single-line are the *most common* styles on this host (9 and 2 of 17). The
  claim was about its synthetic fixtures, but as written it reads as a host
  statement. Fixture lanes must separate "no host instance of this style" from
  "no host instance that can verify my fixture".
- **The catalogue check is only as fresh as the last captured session.** It
  compares the newest block against the db *now*; a mid-session description edit
  legitimately reads as a miss. Printed timestamp, no threshold — named as a gap
  in the artifact rather than papered over.
- **Style coverage is thin on this host**: 2 plain, 9 `>-`, 5 `>`, 1 `|`; zero
  quoted, `|-`, `|+`, `>+`, multi-line plain. Five parser cells are implemented
  but unfalsifiable here, which is why unmodelled scalars are *excluded from the
  pass/fail set* instead of guessed.

## Aggregator audit r6 — closure ledger (9 defects, 9 closed)

| # | Defect (audit id) | Correction landed | Verification |
|---|---|---|---|
| 1 | Falsified counts committed and re-asserted: "22-row anti-pattern table", "13/9/12/8" | `SHONEN.md` regenerated with the measured counts and the counting rule; `SKILL.md` § Sources and `corpus/README.md` now say the dispatch checklist numbers 12 items in the artifact and renders as 9 merged boxes in `SKILL.md`; this file names both corrections | `awk '/^## Anti-patterns/,/^## Refusals/' SKILL.md \| grep -c '^\|'` → 22 lines = 20 data rows + header + separator; `awk '/^## /{h=$0} /^- \[ \]/{c[h]++} END{print c[h]}'` → 13/9/9/8 |
| 2 | 8 unresolvable `commit round-N` pointers (`lessons/round-{1,4,5,6,7}.md:3`, `README.md` rows 23–25) | Pointers replaced by the hashes each round actually shipped (round-1 `1d93182`, round-3 `229b687`, round-4 `397b29c`, round-5 `4002b9f`, round-6 `a614927`, round-7 `3b029b8`); README rows 24–25 likewise; `PROTOCOL.md`'s "commits are cited by hash" rule was the standard applied | `grep -rn 'commit \`round-[0-9]\`' corpus/ \| wc -l` → 0 |
| 3 | `SCORECARD.md` scores not re-derivable; `consistency` ∉ the six axes; unowned rows unlabelled | `SCORECARD.md` rewritten: every row carries `score — counting command @ tree`, an owned/advisory label, a shared fractional rubric, and an axis-name reconciliation declaring `consistency` a calibration sub-axis; the `AXES.md`↔`MISSION.md` mismatch is routed to the protocol lane | `grep -c '@ round-10 worktree' SCORECARD.md` → 8; each row's command re-run this round |
| 4 | Inherited falsified mechanism claim (`skill-activation-telemetry.md:29-30`, "compression is a model call") | Appended correction note under the clause pointing at `harness-router-models-round9.md`, `render-mechanism-round7.md`, the verifier, and the live warn count (10925, not 10191) | `grep -n 'Round-10 correction' corpus/knowledge/skill-activation-telemetry.md` |
| 5 | Lane-identity breaches (`3b029b8` operator identity, `8c300ad` `shokunin <shokunin@local>`) | Recorded append-only (round-9 LOG entry + repo-local identity already fixed); the `8c300ad` class routed to the aggregator as a fleet pattern (kumitate `7a4c9a0`, kagi `ea77bf0`); no history rewrite | `git show -s --pretty='%an <%ae>' 8c300ad` → `shokunin <shokunin@local>` (historical, immutable) |
| 6 | Stale index count: README CLAUDE.md row "16-file census" vs live 18 | Row re-based to 18 with the command inline (16 at round 7) | `find ~ -maxdepth 6 -iname 'claude.md' -not -path '*/node_modules/*' \| wc -l` → 18 |
| 7 | Un-commanded counts: "50 round prompts" (live 53), "163–818-char sources" (163–820) | README row corrected to 163–818 with the measuring command stated (the audit's 820 = same corpus, blank-line folding); the round-10 report states 53 with its command (the round-9 report is a closed artifact and is corrected here, not rewritten) | `ls /home/vgpnk/projects/shokunin/.ufo/prompts/*-round-*.md \| wc -l` → 53; per-skill `description_chars` 163–818 |
| 8 | Index coverage: `lessons/round-{1,3,4}.md` had no row (and the aggregator audits were unindexed) | Rows added for `lessons/round-1/3/4.md` and for the four aggregator audits (`round-{1,4,5,6}-aggregator-audit.md`), so the audit trail is reachable from the index | `comm -13 <(grep -oE '(knowledge\|lessons)/[A-Za-z0-9._-]+\.md' corpus/README.md \| sort -u) <(git ls-files corpus/ \| sed 's\|^corpus/\|\|' \| sort -u)` → `README.md` only (self-reference) |
| 9 | `SHONEN.md` lacked the seed's trailing newline | Regenerated with a trailing newline, corrected counts, and the round-10 verifier evidence | `tail -c1 SHONEN.md \| od -An -tx1` → `0a` |

Routed back out (not kotoba's to fix): the round-5 aggregator minor 4
withdrawal (source char counts reproduce exactly under ws-collapse) belongs to
the aggregator's own ledger; the `AXES.md` axis-set mismatch belongs to the
protocol lane.

## New evidence (opinion-flagged where not provable)

- **omp is a Bun single-file binary whose JS is readable.** `strings -n 6` and
  raw byte reads expose `packages/coding-agent/src/extensibility/
  skill-descriptions.ts` verbatim. Any future omp mechanism question costs a byte
  read, not a disassembly.
- **Catalogue census (sentinel):** 4116 real `<skills>` blocks across 5924
  session files; the raw literal count is 8194 and is contaminated by captured
  transcript/tool text. Newest block 2026-09-28T21:47:06.212Z = 17/17 cache.
  `session_init` today 4142 (round-9 range ~4032–4116); compression warns 10925;
  omp binary sha256 `55016ef5…`; db main file 12288 B, `-wal` 0 B, `-shm` 3 B
  (mtime remains a lower bound).
- **Root order is load-bearing.** The shadowed `~/.config/opencode/skills/ufo`
  description hashes to a key absent from the db (`c78fa9df…`), while the
  offered `~/.omp/agent/skills/ufo` copy (`892555ed…`) hits. A precedence flip
  would orphan the row silently — detected by the verifier, prevented by
  nothing.
- **Cross-axis routing (connector):** no sibling lane has a verifier of this
  class (kagi's `corpus/*.sh` gates host telemetry; kengaku's scripts are
  benchmark runners), so no artifact duplication and no handover owed.

## Debt / next

- **39 `SKILL.md` checklist boxes are still lane-attested** (13/9/9/8). Round 11
  is scoped to **calibration**: make the depth evidence non-author-verifiable —
  a reproducible run record from a lane that did not author the round — and, if
  that lands early, close `consistency` 8 → 9 by making index coverage a
  committed check instead of a hand-run `comm`.
- `/tmp/round10/` scratch (fixture reports, independent verifiers, mutation
  reports) is not evidence under `PROTOCOL.md`; the durable copies are
  `verifiers/`, `corpus/knowledge/harness-verifier-round10.md`, this file and the
  report.