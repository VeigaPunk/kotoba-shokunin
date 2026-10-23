Result: HOLDS — the three new Coverage-map rows and the Round-55 Frontier note in corpus/README.md at f0e6b695 say no more than the counter prints and the entry holds; the "Still not held" list is honest; no actionable defect in scope.

## Scope

`git diff f0e5de820a60ec44ff7e5b7c88ac8c8d463dde0c f0e6b695b746775823b65a8c45de7d50ea33e84f -- corpus/README.md` = 10 added lines, 0 removed: rows at README.md:86-88 under § Coverage map, and the note at README.md:129-134 under § Frontier. Read-only review; nothing executed in the lane.

## Findings by severity

### None (no defect found)

### Verified claims

**Row :86 — Round-54 non-author spot-check (closure).**
- "written by the hyaku closure, not the lane": file frontmatter `corpus/lessons/round-54-verifier-spotcheck.md:1-9` reads `author: hyaku closure (non-author integrator, @m_opus)`; landed by commit `f0e5de8` authored `protocol-shokunin <protocol@shokunin.local>`, subject "round-54 verifier spot-check (integrator, hyaku): non-author admit/reject" (`git log -1 --format='%an %ae %s'`). "never edited here" holds: `git log --oneline --follow -- corpus/lessons/round-54-verifier-spotcheck.md` returns exactly one commit, `f0e5de8`.
- "landed without an index row, indexed round 55": `git log --oneline -S 'round-54-verifier-spotcheck' -- corpus/README.md` returns only `9615579` (the round-55 C1 commit), so the file had no README row before round 55. Consistent with the sibling rows for rounds 48-50, which each record the same pattern.
- "round 54 admitted; eight routed defects": `round-54-verifier-spotcheck.md:255-257` — `Status ok; **admitted**` and `Routed defects 1–8 above are status-neutral`; § 7 lists exactly eight numbered defects.
- "round 55 works them in `lessons/round-55.md`": `corpus/lessons/round-55.md:50-59` § "Routed defects from the round-54 spot-check" disposes of all eight, in order (receipts-with-revisions/M48; Q34/Q35; over-wide C1 cells `ed3e8996`; reject-1 route move; registry counter `4d700b17`; `fault_injection_corpus.sh` repairs; minor quote notes + SKILL.md 599→598; carried items).

**Row :87 — Explicit invocation by client (round 55).**
- "seven clients' own docs (S065–S071)": `corpus/knowledge/explicit-invocation-round55.md:1` cites S065–S071; `corpus/SOURCES.md:78-84` has all seven rows, each tier `A`, kind `docs`, status `mined`, opened `2026-10-22`, `used-by` naming the entry.
- Sigil mapping `/` in Claude Code, VS Code, Copilot CLI and Cursor; `$` in Codex; `@` in opencode V2; Gemini CLI `activate_skill` "(not a user-typed form)": matches SKILL.md:199-205 table cells and entry :22-28 verbatim (`@skill-id`, `/skill-name`, `$setup-demo-app`, `/webapp-testing`, `/frontend-design`, `activate_skill` marked "model tool call" in SKILL.md:203 and "not a user-typed form" in entry :26). The "V2" qualifier matches S071's `skills.mdx` source and the entry's "opencode V2" phrasing.
- "`SKILL.md` § Explicit invocation by client" exists at SKILL.md:193-205; counter path `../verifiers/check_explicit_invocation.py --rev <rev> --fetch` matches usage line in the counter docstring and registry row SKILL.md:459.

**Row :88 — Round-55 lessons.** `corpus/lessons/round-55.md` has `## Gate` (:8-39) covering S065–S071 admitted plus a Rejected subsection (five rows) and Rows-touched; `## Mistakes` (:41-48) M48-M51; and the round-54 routed-defect section (:50-59). "the rejections" — five rejected rows recorded. Accurate.

**Frontier note :129-134.**
- Anchors on the correct row (:98 *Implicit-intent fidelity* — "the literal-trigger proxy covers only prompts that name a skill"). The note's premise — "the form each client documents for invoking a named skill by name, which an implicit-trigger measure must set aside first" — is the entry's stated purpose (entry :7-16, SKILL.md:195).
- Counter string in the note, `user-typed invocation forms found on the live page F of K; new ground G`, is byte-identical to the actual print at `verifiers/check_explicit_invocation.py:636` (`"user-typed invocation forms found on the live page %d of %d; new ground %d"`). Q31 clean: the note quotes only what the counter prints; it does not claim the counter verifies semantic "explicit invocation" (which the counter docstring :57 and entry Limits :60-66 assign to the reading/reviewer).
- "one prerequisite moves in part" is correctly hedged: the note does not claim the counter counted all seven clients — Gemini CLI (`activate_skill`, a model call) and VS Code (quote lacks the word `skill`) are admitted but not counted under counter v2, per entry Limits :64-66 and lesson :24-25, :34. The note claims only that the documented forms are held in the entry, which is true for all seven.
- "Still not held" is honest on all three items:
  1. "the intent-labeling pass itself" — Frontier row :98 and Known-gaps :152-154 still list it as the next probe; the note does not mark the row held.
  2. "any measured client behaviour" — entry :11 "These are documentation statements, not measured client behaviour"; :69 "No client behaviour was run or measured".
  3. "who typed the form (a user, an orchestrator or another skill)" — entry finding 4 (:47-49) states the form identifies *that* a skill was named, not who named it; SKILL.md:195 likewise bounds "it says nothing about who chose the skill unless the user typed it".

## Residual observations (not defects)

- The note's "the form **each client** documents" is looser than the round-54 note's "what **seven clients** document" (README.md:124). The counter bounds the set to seven pinned clients, and row :87 names them via S065-S071, so context bounds the clause; if a reader took "each client" as universal it would overclaim, but the same-sentence pointer to the entry confines it. Recorded as a phrasing nit, no change required.
- Row :87 calls all seven sources "own docs"; S066 is a vendor blog (`developers.openai.com/blog/`), disclosed inside its SOURCES cell and the entry as "vendor guidance, not a measurement". Same looseness as round-54's row for S053; acceptable under the row's own convention.

## Verification gaps

- I did not re-run the counter's `--fetch` against live pages (other seats re-run the counters; this item is README-vs-counter/entry consistency). Verified the printed label in code (:636) and docstring (:95-97) rather than a live exit code.
- The "indexed round 55" clause rests on `git log -S` over `corpus/README.md` only; a row could in principle live in another index file, but § Coverage map is the lane's only index and no other file lists a `round-54-verifier-spotcheck` row (grep over corpus/ finds only README.md:86 and the file itself).

## Tooling

No installs. Read-only git (`diff`, `log --follow`, `log -S`, `log --format`) in the lane; no writes to lane files other than this report.
