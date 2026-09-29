# kotoba-shokunin — Promotion checklist

Promotion to shokunin requires all of:

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources
  note (round 13): the round-12 `[x]` rested on `ReviewSHONEN`, a subagent this lane
  dispatched — PROTOCOL.md:34-39 ("a subagent the lane dispatched is still the lane …
  only a non-author `<id>` may write `[x]`") makes that author attestation, so the
  mark reverts to `[~]`. The findings below are unchanged and were not re-derived
  this round.
  note: checked in round 12 by the non-author reviewer lane `ReviewSHONEN` (see
  `../.ufo/reports/round-12/kotoba.md` § SHONEN); it ran the printed `awk` as
  written on the HEAD pin and on the worktree, re-derived the per-section counts
  with its own sed range, and spot-checked 36 § Sources targets (36 OK / 0 MISS).
  evidence: SKILL.md — 7-row anatomy table, 5-row decision-table table, four fidelity checklists (14/9/9/8 boxes: `git show HEAD:SKILL.md | awk '/^## /{h=$0; if(!(h in s)){s[h]=1; o[++n]=h}} /^- \[ \]/{c[h]++} END{for(i=1;i<=n;i++) if(c[o[i]]) printf "%s: %d; ", o[i], c[o[i]]}'` → `## Trigger-fidelity checklist: 14; ## Agent-definition fidelity checklist: 9; ## Dispatch-prompt fidelity checklist: 9; ## Always-on constraint-file checklist (AGENTS.md-class): 8` — the Trigger checklist gained the round-12 second-witness box, so this line moved 13→14 and 39→40 boxes; recompute with the command as written before citing it (round 12 replaced the command printed here: the previous one ended `END{print c[h]}`, which prints one empty line and cannot produce the counts it claimed — the fourth instance of the round-11 defect class, in this repo; the same broken expression sits in `corpus/lessons/round-6-aggregator-audit.md:30`, aggregator-owned and routed, not edited); the dispatch audit artifact numbers the same set as 12 items), 20-data-row anti-pattern table (`… | awk '/^## Anti-patterns/,/^## Refusals/' | grep -c '^|'` → 22 lines incl. header+separator), cited Sources list. Round-10 corrected the two counts this line previously carried (22 rows, 13/9/12/8) — aggregator audit r6 defects 1/9.
- [~] At least one end-to-end domain task executed and logged in LOG.md
  note (round 13): same defect — the round-11 promotion rested on `ColdRunRecord`, a
  subagent this lane dispatched, so the `[x]` reverts to `[~]`; a fresh-lane cold run
  of the same scripts is what would restore it.
  evidence: LOG.md round-5 fleet SKILL.md audit (5 siblings, 13-item checklist); round-7 dispatch-prompt audit of 43 files; round-10 harness-claim verifier (`verifiers/verify_harness_claims.py`, 27 checks, exit 0 on the live host) — `corpus/knowledge/harness-verifier-round10.md`; round-11 corpus-integrity verifier (9 checks, red-before → green-after) plus its **non-author cold run**: reviewer `ColdRunRecord` (did not author the script or baseline), record `corpus/knowledge/cold-run-round11.md` — script sha256 gate, verbatim run + exit code, three independent spot-checks in its own code, `Discrepancies: none found`.
  note: promoted from `[~]` in round 11; the reviewer is named and the record path is in-repo, per the round-6 attribution rule.
- [~] Instructions executable by an agent without oral context
  note (round 13): the round-12 `[x]` rested on `ReviewSHONEN` (lane-dispatched) →
  `[~]`; and the first genuine non-author witness on record, the aggregator lane's
  round-8 box-3 cold run (`corpus/lessons/round-8-aggregator-box3-coldrun.md`), graded
  this box `[~]` for two recipe defects it named: B1 — the "newest `<skills>` block"
  recipe names no file-selection rule (the newest-mtime session file carries 0
  `<skills>` blocks); B2 — `verifiers/fault_injection_corpus.sh` sits among runnable
  verifiers with no mutating-gate warning (it clones and `rm -rf`s). Both are fixed in
  round 13; a fresh non-author run is what would restore `[x]`.
  note: checked in round 12 by `ReviewSHONEN`: three stated procedures run verbatim
  from a foreign cwd with the stated outcomes (sqlite3 count → 17; the init-count
  distribution → 1/141/34/14; the corpus verifier fires its contract), one
  cwd assumption found and now stated in `SKILL.md` (relative script paths).
  evidence: LOG.md round-7 — a blank-context L2 reviewer ran the 13-item trigger-fidelity checklist on SKILL.md with zero clarification requests (13 verdicts + meta-findings); round-10 made the harness half of the file executable rather than prose (same verifier).
- [~] No cross-domain bleed (PROVINCE.md still accurate)
  evidence: LOG.md round-7 — cross-domain defects in .ufo/prompts/, ~/.config/opencode/, scripts/shokunin-watchdog.sh audited and reported, not fixed; round-10 aggregator audit adopted as-is and its kotoba-owned defects closed inside this repo; PROVINCE.md unchanged.

Verifier note: every check in this file is lane-run — therefore `[~]`, and a
`[x]` box still requires a reviewer who did not author the round. Round 13 applied
PROTOCOL.md:34-39 literally: a subagent this lane dispatched is this lane, so the
round-11/12 `[x]` marks were author attestation and were reverted to `[~]`. The only
non-author evidence on record is the aggregator lane's round-8 cold run
(`corpus/lessons/round-8-aggregator-box3-coldrun.md`; verdict `[~]` on box 3, whose
B1/B2 defects round 13 fixes).
