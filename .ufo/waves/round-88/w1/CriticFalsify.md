# CriticFalsify — round 88 scoped findings (r88-w1)

Full constructions, commands and observed lines: `.ufo/waves/round-88/w1/CriticFalsify/attacks.md` (receipts in `CriticFalsify/receipts/`).
Measured at lane HEAD `89579c7` (freeze commit, verifiers unchanged since `4df1e80`) and tip `4df1e80`. The C1 v2 counter has not landed (`C1_READY` absent): C1 results are constructions against the frozen r87 counter and its helpers, not v2 verdicts.

## Admission-blocking survivors

- **C2-S2 — silencing passes D5 v2.** `report_dead` forced PASS in place (name kept): identity PASS, monotone PASS, `d5 PASS`. Integrity's own self-test then reads `2 failure(s) over 178 assertions`. Fix: D5 also requires integrity `--self-test` exit 0 at `<rev>`.
- **C2-S3 — re-recorded baseline passes D5 v2.** `verifiers/corpus-baseline.json` equal expects set to observed (170/125/59): three reds heal, `d5 PASS`. The file is outside the kill rule. Fix: pin its blob to the base blob, or add it to the kill rule.
- **C2-S1 — the frozen control cannot fail.** `w_added_red` (an unresolvable commit) leaves the DRIFT name set unchanged (`commit_unresolvable` already red at base): D5 PASS. v2's own self-test is `1 failure(s) over 16` on that arm, yet `C2_READY` was written. Fix before any candidate is scored: use the new-name shape (`commit \`zz-not-hex\`` → `commit_nonhash`), which v2 FAILs (`monotone FAIL … commit_nonhash`).
- **C1-S1 — one commit rewrites both ledgers.** `~/.agents/skills` → `/tmp/x/skills` in both `omp-skill-roots*.tsv`: r87 counter `grounded 12 of 12`, exit 0. S3 compares to the round-86 ledger at the same rev, so it is self-referential. Fix: anchor S3 to a frozen SHA.
- **C1-S2 — module mislabels pass.** Conjunct 3 is header order only: r87 counter reads `12 of 12`, exit 0 for `claude.ts → builtin.ts` (row 2) and `managed-skills.ts → helpers.ts` (row 12). Conjunct 3 accepts 47 of 84 (row, module) pairs. Fix: the nearest preceding header must equal the module; all 12 honest rows agree (checked), so the honest N is unchanged.
- **C1-S4 — `$HOME` escape by path string.** `/etc/skills`, `/tmp/x/skills`, `~root/skills` pass conjuncts 1 and 4 (no `..` needed). Fix: every candidate under `$HOME` (or the cwd ancestors for `{cwd}/`); refuse absolute and `~user` patterns.
- **C1-S3 — binding tokens are generic substrings.** `cwd` (from every `{cwd}` pattern, present on the forged `codex` line of w_cross_row7) and `skills` (from the managed-skills literal, present on the forged plugins line of w_misattr_row12) are legal under the frozen wording. Fix: binding tokens come from the root's own segment, are reviewed before scoring, and are keyed by pattern.

## Bounds to disclose (not blocking on their own)

- **C2-S4:** growth of instance count inside an already-DRIFT name is invisible (3 unresolvable commits: D5 PASS; v2 discloses this as F1).
- **C2-S5:** integrity reads the working tree and fleet root, not `<rev>`. At `89579c7` `report_dead` is green (fleet `kama.md` present); in a scratch clone at the same rev it is DRIFT. D5's monotone test holds in both, but the healed-red claim is location-specific.
- **C1-S5 (inference):** a lookup-table counter (hash-pinned honest ledger, rejects the rest) would pass N==12 and M==4. Fix: a fresh honest-variant control that the counter must score 12.
- **C1-S6:** conjunct 4's "visibly walks" set has no mechanical extractor (the walk is `function Wne` @173865174, off the reader line). Predicted inert, as in r87.

## Controls

- Removal control works: v2 identity FAIL on `removed_check` (8 names vs 9).
- Honest revisions: v2 D5 `closed 5 of 5` at `4df1e80` and at `89579c7`.
- Blanket refusal is caught by N==12 on the honest ledger. Blanket acceptance is caught by M==0 on the do-nothing run (r87 counter `12 of 12` on all four worlds). Neither control catches C1-S5.

## Not run

v2 C1 counter (absent); `w_healed` control; r87 C2 gate at tip (plan's `4 of 5` not re-measured).

## Frozen bytes and tooling

No frozen file edited. No lane write outside the seat directory and this report. No ELF execution (read-only mmap). Tools installed: none (stdlib and existing git only).
