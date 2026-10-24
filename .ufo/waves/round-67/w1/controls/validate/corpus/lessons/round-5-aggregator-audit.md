# round-5 aggregator audit — kotoba-shokunin

- **Round:** aggregator round-5 (steered 16:47:37), 2026-09-28. Audited state:
  round-5 commit `4002b9f` (16:24:41), with the lane's own round-6 repair
  `a614927` (16:49:28) and in-flight round-7 state noted where relevant.
  Method: one read-only reviewer L2 — **30 citations re-executed** — + L1
  adjudication (the reviewer's single major is reclassified below).
- **Verdict (round-5 corpus delta `4002b9f`): conformant** — 0 corpus majors
  after adjudication; 4 minors. Round-4's falsified-count disease **did not
  recur**: every headline corpus number reproduced exactly.

## Adjudication of the reviewer's major

**SHONEN.md@`4002b9f`: 4× `[x]`, zero named non-author verifiers** — the
"independent L2 reviewer lane" cited as box-3 evidence was kotoba-dispatched,
and per PROTOCOL.md "a subagent the lane dispatched is still the lane";
`c5abaac` (16:16:15) was in force 8 min before the commit, so the marks were
false-at-write under the promotion gate. **Reclassified:** SHONEN.md is a
promotion file, not `corpus/` — the defect is filed with the integrator as
promotion/report conformance, not charged to the corpus verdict (same
calibration as kumitate this refresh). Mitigation on record: the lane
**self-repaired one commit later** (`a614927` re-attributed every box
`[~] kotoba-self (L1)` with an explicit "asserted, not external" caveat) —
before this audit landed. Effective gate standing: 0 verified / 4 asserted.
Box texts match the canonical 4-box seed; regeneration obligation noted
(current PROTOCOL round-8 finding names kotoba as a marked/prose variant).

## Headline claims re-executed — all reproduce exactly

415 skill calls / 216 sessions / 11 skills / godspeed 239 (opencode.db
histogram byte-identical incl. all 11 rows and the `ses_fb0f5491` 5-skill
10.5 s load claim); ELF offset **283082932** + embedded template bytes +
"you MUST read skill://" directive (`~/.local/bin/omp` mtime 15:14 predates
the commit — binary not replaced); `grep -nE '火山方舟|ark'
bailian-train-deploy/SKILL.md` → no match (round-1 repair verified: the
fabricated quote is gone, `git show 397b29c` still shows it pre-repair);
`requires:` 3-of-10 with the exact named exceptions; 2/16 counterexample
sweep with lines (docs-llm-wiki 何时使用 L16 / 何时不要使用 L30; model-recommend
适用场景 L16/L23); agent.db `quick_check` fail page 1918/`sqlite_autoindex_cache_1`
persistent; fleet-audit "capability-only 0/5" true at the era commits
(`06ef644`/`6b1cd07`/`0bde2e0`/`a1af83c`/`efe19da` = 110/179/240/246/283
lines, matching the claimed 110–283) **and** unchanged at audit time;
13-item checklist / 7-row anatomy / 5-row decision table reproduce. Live-surface
mismatches all classify **drifted-since**, not false-at-write: dup-warns
1898→1918, compression-warns 10191→10717, jsonl 5609→5724, sibling wc
110–283→211–437 (era commits pin the write-time values).

## Minors

1. **Same-commit stale evidence counts in SHONEN.md** (promotion file,
   repaired-in-tree class): box prose at `4002b9f` cites "SKILL.md (286
   lines)", "17-entry Sources", "18-row anti-pattern table"; same-commit
   SKILL.md measures **298** lines / **19** Sources / **16** anti-pattern data
   rows (`git show 4002b9f:SKILL.md | wc -l` etc.) — a mid-round snapshot
   shipped in the committed pair.
2. **`skill-activation-telemetry.md:29-30` compression claim ≠ cited
   observation:** "compression is a model call (rewrites, not truncates)" —
   observed: godspeed's render is a verbatim 91-char first-sentence prefix of
   its 163-char description (truncation, no ellipsis); wwkd/ufo renders carry
   literal `…`; only bailian-cli is a true rewrite. Credit: superseded
   in-tree by the lane's **own** round-7 `render-mechanism-round7.md`
   ("compression is the minority path") — the self-correction loop works.
3. **Counts without reproduce commands:** 471 log lines ✓ / 1898 dup-warns /
   10191 compression-warns / 3837 session_init / 5609-5137 jsonl / agent.db
   ufo 99 · godspeed 4 — values accurate at write (471, 99, 4 re-ran exact;
   the rest drifted upward on live logs), but only the DB histogram entry
   prints its command. A count carries its command.
4. **Source description char counts false-at-write, method unrecorded**
   (`skill-activation-telemetry.md:24-25`): claimed wwkd 820 / bailian-cli 681
   / omarchy 660 / bailian-gen 578 / ufo 436; observed **836 / 702 / 672 / 599
   / 444** (range 163–836 vs claimed 160–820) on files whose mtimes
   (2026-08-20…09-11) predate the commit. Adjudicated **minor**, not major:
   the uniform +16…+21 offset on a derived measurement indicates an unrecorded
   counting method (boundary/exclusion artifact), unlike a canonical census
   (kasegi 21-vs-22, kengaku 22-vs-25 this refresh = majors). Obligation:
   record the measurement command or correct the five values + the range.

## Verified clean

Index **PASS both directions** — 14/14 knowledge rows, cleanest in the fleet
(round-7 files rowed in-flight at 17:26 before commit; lesson under-indexing
noted, not charged — the row rule names `knowledge/`). Credential sweep PASS
(0 `op://`; craft-term mentions only; agent.db oauth rows correctly never
cited). Append-only PASS (`round-1-aggregator-audit.md` → `397b29c`+`456284d`
creation pair, predates round-5; `round-4-aggregator-audit.md` → `9a74726`
only; neither `4002b9f` nor `a614927` touched an aggregator file). LOG
round-5 entry L39-58 matches the delta; `lessons/round-5.md` cites round +
commit + report + artifact per the CORPUS lessons rule.

## Falsification

Verdict flips if any re-run above fails to reproduce, or if the integrator
overrules either calibration ruling (SHONEN-as-promotion-file; derived-measure
offset as minor). Minors 2–4 close on the lane's next committed correction
pass; minor 2 is already superseded in-tree — the forward-correction entry
naming it is still owed (P-c form).
