HOLDS — applies to the C1 census row `tsukuroi` (`corpus/knowledge/sibling-overlap-census-round49.md:82`) and its `PROVINCE.md` § Adjacent row (`PROVINCE.md:56`), both at judged commit `c48793dbe5eb30cd661f42ecad7399ae94e3d7ad`. All five attack checks pass; no finding overturns the row.

## Findings

None overturning. Per-check results (attack named, then what I re-derived):

1. **Commit exists, branch cell right.** `git -C ../tsukuroi-shokunin rev-parse 22fd1642…^{commit}` exit 0;
   `git branch -a --contains` lists `master` (exit 0); `merge-base --is-ancestor 22fd1642… master` → yes.
   Commit subject round-24, dated 2026-10-22 05:59:42 -0300. Working tree detached at the same commit —
   the row's `master` cell is still correct (ancestor of master).
2. **Scope quote verbatim at locus.** `git show 22fd1642…:PROVINCE.md | sed -n '3,4p'` gives the quote
   split across lines 3–4 ("**Domain:** host operability & system repair (繕, mending) — the OS" /
   "substrate itself: package state, systemd, drivers/firmware, boot health."). Joined, it matches the
   census quote cell byte-for-byte after whitespace collapse, which the entry declares ("quotes verbatim
   at the pinned commit, whitespace collapsed", entry line 60). Start locus `PROVINCE.md:3` is exact and
   inside the guard's LINE_TOLERANCE 2 (`verifiers/check_sibling_census.py:31`).
3. **Classification `none` survives attack.** Rule (entry lines 45–50): contested = sibling scope
   surfaces claim kotoba's core (writing/auditing OTHER lanes' SKILL.md, prompts, AGENTS.md-class files,
   or instruments over them); adjacent = either side's scope surfaces state a split of one
   artifact/function/trigger area BETWEEN the sibling and kotoba. Attacks run:
   - Word sweep without the name: whole-tree `git grep -inE '(own|scope[sd]?|claim|refus|ced(e|es|ed|ing)|split|arbitrat|hand(ed|s)?[- ]?(to|off))' 22fd1642… -- '*:!*LOG.md' '*:!*reports/*' '*:!*SCORECARD.md' | grep -iE 'prompt|SKILL\.md|AGENTS\.md|frontmatter|trigger|dispatch|checklist|anatomy|agent-def'` → 0 lines, exit 1. The seven top-level files' 81 craft-noun hits were re-covered by pattern (build seat read all 81 line-by-line; spot re-reads agree).
   - `SKILL.md` at pin (2285 lines): every "trigger" hit is systemd timer vocabulary (LastTrigger,
     activation latency, OOM trigger — lines 661-1105); every `AGENTS.md` hit cites tsukuroi's OWN
     AGENTS.md (169, 182, 449); "SKILL craft gate" (183) is its own SHONEN.md probation criterion. No
     frontmatter/anatomy/compression/fidelity/agent-definition vocabulary at all.
   - Nearest touches re-read at pin: `SKILL.md:207-209` consumes `kama-shokunin/SKILL.md` as a shape
     model (read, not write/audit); `tools/check-boundary-contract.py:25` "Prompt policy and post-hoc
     request classification only" and `SKILL.md:2165` "Full native enforcement belongs to
     kumitate/operator runtime authority" constrain tsukuroi's OWN dispatch prompts and cede enforcement
     to kumitate/operator — not a claim on kotoba's instruments, not a split with kotoba. ADJ-05
     (`PROVINCE.md:50`) splits dispatch semantics with kumitate, not with kotoba; outside the rule.
   - Tree-wide `git grep -il kotoba 22fd1642…` → exactly the 10 files the build seat lists; re-read the
     corpus one (`executor-test-sufficiency.md:187`, "kotoba tail notes" in a list of other lanes'
     historical logs) and the IN-021 rows (`adjacency-anchors-r19.md:116`, `.json:570`) — inbound
     historical pointers, no ownership statement.
   - `considerthese/2026-10-19.md:44` (not in the build seat's 10) read: it records that OTHER lanes pin
     tsukuroi's files — inbound, not a claim.
   - Deep `.ufo` candidates the skill-file cell could hide: `.ufo/waves/round-21/{candidate,snapshot}/SKILL.md`,
     `.ufo/waves/round-22/candidate/SKILL.md` exist at the pin; all three are historical copies of
     tsukuroi's own SKILL.md, 0 kotoba tokens (absent from the 10-file grep), 0 pattern-A hits.
   - Build seat finding 8's flip-to-adjacent falsifier requires counting own-seat dispatch-prompt policy
     as a shared prompt surface — a taxonomy change, not evidence; under the stated rule `none` stands.
4. **Mechanical columns re-derived.** `git show 22fd1642…:SKILL.md | sed -n '3p'` = `description: Domain
   specialist — host operability & system repair. Rank: shonen (probation).` (frontmatter at line 3).
   Whole-token case-insensitive: `kotoba` → 0; 20-lane token alternation (audio…tsukuroi) → 0 matches.
   Cells `no` / `no` correct (entry lines 51-52 define these as description-only and mechanical).
5. **PROVINCE.md boundary note facts.** Row `| tsukuroi | none | 22fd1642… | host operability and
   system repair; no claim on kotoba ground |`: domain wording matches sibling `PROVINCE.md:3-4` and
   `SKILL.md:3`; "no claim on kotoba ground" backed by the sweeps in 3; commit and classification match
   the census row; no cited line in the row, and section preamble citations all resolve (census entry
   path, seat report `CensusTsukuroi.md`, `verifiers/check_sibling_census.py`).

Content guard re-run from a scratch clone at the judged commit:
`python3 -B verifiers/check_sibling_census.py corpus/knowledge/sibling-overlap-census-round49.md --province PROVINCE.md`
→ `rows 20 verified 20` / `province rows 20 matched 20`, exit 0 — the tsukuroi row joins on lane,
branch-independent commit, classification, quote-at-locus and PROVINCE row.

## Residual risk and verification gaps

- Master advanced past the pin (`git rev-parse master` → `0cd9b28bee5fd5a50d991e6dee0c0d0f48b15935`);
  the entry's Limits disclose pin drift and bind every claim to the pinned bytes. No new claim about
  the pin was asserted, so no defect — but the round's "20 rows" statement is pin-scoped, not tip-scoped.
- The entry's own Limits concede: a sibling claim stated only in an unread wave report would be missed.
  For tsukuroi the tree-wide kotoba-token search (10 files) plus the ownership-verb/craft-noun sweep
  over the rest of the tree mitigate this; a claim phrased with none of those tokens and no lane name
  would still be invisible. Disclosed, not falsified.
- I did not use an LSP device (none attached; review is over prose tables and pinned bytes, verified by
  direct execution, not semantic tooling).
- No tool installed or upgraded (none needed). Scratch clone: `/fast/scratch/hyaku/kotoba-r49/falsify/RowTsukuroi/clone`
  at `c48793db`; lane checkout untouched except this file.

## Evidence (commands → exit codes)

- `git -C ../tsukuroi-shokunin rev-parse 22fd1642…^{commit}` → 0; `branch -a --contains` → master, 0;
  `merge-base --is-ancestor 22fd1642… master` → 0 (yes).
- `git show 22fd1642…:PROVINCE.md | sed -n '3,4p' | tr '\n' ' '` → quote byte-match after collapse; locus :3.
- `sed -n '3p'` on `git show 22fd1642…:SKILL.md` → description; `grep -ioE '\bkotoba\b'` → 0;
  20-token alternation grep → 0 matches.
- Tree sweeps as quoted in finding 3: ownership-verb/craft-noun join → 0 (grep exit 1);
  `git grep -il kotoba` → 10 files; corpus/considerthese/.ufo candidates re-read.
- Guard in scratch clone: `GUARD_EXIT=0`, `rows 20 verified 20`, `province rows 20 matched 20`.
- `git ls-tree -r --name-only 22fd1642… tools | wc -l` → 26; `git show …:SKILL.md | wc -lc` → 2285 / 261104
  (both match build seat `CensusTsukuroi.md`).
