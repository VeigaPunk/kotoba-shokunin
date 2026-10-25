# Counting-claim census — round 12

Landed by L1 from the round-12 census lane's scratch (`/tmp/round12/ScoutClaimCensus/census.md`)
so the round's central measurement is re-runnable from the repo instead of from `/tmp`.
Author: lane `ScoutClaimCensus` (batch 1, round 12). Method: extract every sentence carrying a
number or a zero/absent claim about the corpus or the verifiers, write the exact command that
re-derives it, RUN it, and classify the result AGREES / STALE / UNEXPRESSIBLE / FALSE-at-HEAD /
PARTIAL / DISAGREES. Verdict distribution, quoted with its command rather than as a bare row count (a raw
`|`-split row total differs from this — some cells contain escaped pipes, so the number is
only as good as the parse): `awk -F'|' '/^\|/ && NF>=7 {v=$(NF-1); gsub(/[ *]/,"",v); if (v ~
/AGREES/) a++; …} END{…}'` over this file → **49 AGREES, 22 STALE, 6 UNEXPRESSIBLE,
3 FALSE-at-HEAD, 3 PARTIAL, 1 DISAGREES**, plus one `planned, unmet` row (the round's own
falsifier, measured before it landed). The round-12 reviewer counted 86 rows by a raw
`|`-split; both numbers are recorded rather than one being smoothed away. The repairs this land forced are listed in
`knowledge/independent-verification-round12.md` §5 and `lessons/round-12.md`; the rows below
keep the *pre-repair* values they measured, so several of them then read STALE — that is the
record, not an error. Per-round records keep their round's values by design (the claim-scope
rule adopted this round).

## Table

`A` = `corpus/knowledge/corpus-integrity-round11.md`, `B` = `corpus/knowledge/cold-run-round11.md`,
`C` = `SCORECARD.md`, `D` = `LOG.md`, `E` = `corpus/README.md`, `F` = `SHONEN.md`,
`G` = `corpus/lessons/round-11.md`, `H` = `SKILL.md`.
`$R` = repo root; `$W0` = `/tmp/round12/ScoutClaimCensus/w0` (d49dfa5).

| site | claim | command | re-derived value | verdict |
|---|---|---|---|---|
| A:13 | before-state is `d49dfa5` | `git -C $W0 rev-parse --short HEAD` | `d49dfa5` | AGREES |
| A:34 | `round-[0-9]` pattern prints **0 with the defect present** | `B='`'; git -C $W0 show HEAD:corpus/README.md \| grep -cE "commit ${B}round-[0-9]${B}"` | `0` | AGREES |
| A:35 | `round-[0-9]+` prints 1 (the defect site) | same with `+` | `1` | AGREES |
| A:36 | the token at `corpus/README.md:38` is `round-10`, not a hash | `git -C $W0 show HEAD:corpus/README.md \| sed -n '38p' \| cut -c30-80` | `…commit \`roun` (token `round-10`) | AGREES |
| A:49-50 | post-fix both scopes empty | `git ls-files '*.md' \| xargs grep -nE "commit ${B}round-[0-9]+${B}"` | no output (grep rc=1) | AGREES |
| A:62-64 | as-printed escaped-pipe `comm` → 33 | W0, verbatim | `33` | AGREES |
| A:70-74 | real-pipe `comm` → 4 entries | W0, verbatim | `README.md` + 3 lesson files | AGREES |
| A:85 | `git ls-files corpus/ \| wc -l` → 33 | `git ls-files corpus/ \| wc -l` | **36** | **STALE** |
| A:86-88 | `index_patterns unindexed stale missing` → `32 0 0 0` | W0: `python3 …/verify_corpus_integrity.py --repo $W0 --no-baseline --json` | `32 0 0 0` (W0) · `37 0 0 0` (HEAD) | AGREES at W0 / **STALE at HEAD** |
| A:104-106 | four shapes at HEAD: 9 `../.ufo` · 3 `.ufo/` · 8 abs · 1 `~` = 21 tokens | W0: `git grep -h -o -E '[^ `]*\.ufo/reports/round-[0-9]+/[^ `]*' HEAD -- 'corpus/*.md' \| sed 's\|\(.*\)\.ufo/reports/.*\|\1.ufo/reports/\|' \| sort \| uniq -c` | 21 tokens: `../`×9, bare×3, abs×8, `~`×1 | AGREES |
| A:109-112 | loose class 21; tighter checks 19; 1 dir token + 1 placeholder excluded | W0 `--no-baseline --json` | loose 21; `report_total 19`, `report_pointers_excluded 1` | AGREES |
| A:126-128 | the 9 host-absolute report pointers resolve | `cd corpus && for n in 1 3 4 5 6 7 8 9 10; do test -f /home/vgpnk/projects/shokunin/.ufo/reports/round-$n/kotoba.md; done` | `OK ×9` | AGREES |
| A:133 | `grep -c '\.\./\.ufo/reports/round-' corpus/README.md` → 9 before **and** 9 after | W0: `9`; HEAD: `0` | `9` / `0` | **STALE** (live = 0) |
| A:143 | `corpus.index.tracked_files` 33 (unchanged) | live `--json` | **36** | **STALE** |
| A:147 | `report_total` 19 → 19 | live `--json` | **24** | **STALE** |
| A:148 | `report_dead` 10 → 0 | W0 `/` HEAD | `10` / `0` | AGREES |
| A:149 | `commit_total` 18 → 21 | W0 `/` HEAD | `18` / **22** | **STALE** (after-half) |
| A:150 | `commit_unresolvable` 0 → 0 | W0 `/` HEAD | `0` / `0` | AGREES |
| A:151 | `commit_nonhash` 1 → 0 | W0 `/` HEAD | `1` / `0` | AGREES |
| A:154-157 | `--json` prints `{"observed","results"}`, exits 0/1/2/3 | live `--json`; three probes | keys `['observed','results']`; exits `0/1/2/3` | AGREES |
| A:162-167 | red-before block: `7/9 checks pass` exit 1, `report_dead=10/19 commit_total=18 unresolvable=0 nonhash=1`, shapes `[relative=9, absolute=8, tilde=1, bare=1]` | `python3 …/verify_corpus_integrity.py --repo $W0 --no-baseline` | byte-match, exit 1 | AGREES |
| A:168-172 | green-after block: `report_dead=0/19 commit_total=21 unresolvable=0 nonhash=0`, shapes `[0,18,1,0]`, `9/9 checks pass` exit 0 | live plain | `0/**24**`, `**22**`, `0`, `0`, shapes `[0,**23**,1,0]`, 9/9 exit 0 | **STALE** |
| A:175 | perturbed baseline (`commit_total` expect→18) → exit 1 naming exactly that id | `python3 …/verify_corpus_integrity.py --baseline <perturbed.json>` (22→18) | `DRIFT corpus.pointers.commit_total: observed=22 expected=18`, exit 1 | AGREES |
| A:176-177 | `--repo /tmp/notgit` → exit 2; baseline removed → exit 3 | `--repo notgit`; `--baseline nope.json` | `exit=2`; `exit=3` | AGREES |
| A:181 | synthetic `archive + init` tree → `commit_unresolvable=18` and a third spurious DRIFT | `git archive d49dfa5 \| tar -x`; `git init && add -A && commit`; run `--no-baseline` | `unresolvable=18`, `6/9 checks pass` exit 1 | AGREES |
| A:192-193 | 10 planted faults — 7 zero-check, 2 guards, 1 mode-masked | no in-repo artifact records the run | not run | **UNEXPRESSIBLE** |
| A:208 | placeholder pointer → `pointer-excluded=1` | live plain | **8** | **STALE** |
| A:223-224 | md5 of `SKILL.md` @ `3b029b8` = `143fe473368ec9e2bbadde9d0425b1c`, 487 lines | `git show 3b029b8:SKILL.md \| md5sum`; `… \| wc -l` | exact match | AGREES |
| A:237 | checked pointer population 19, 18 host-absolute | live `--json` | **24 / 23** | **STALE** |
| A:245 | `grep -c '^- \[ \]' SKILL.md` → 39; 13/9/9/8 by section | `grep -c`; `awk '/^## /{h=$0} /^- \[ \]/{c[h]++} END{for(k in c) print c[k],k}'` | `39`; 13/9/9/8 | AGREES |
| A:3 | "Every number below was printed by the command next to it" | rows A:85,143,147,149,168-172,208,237 above | 7 numbers no longer re-derive | **STALE** |
| B:15,18 | shipped script sha256 `631569277d…`; gate PASSED, "artifact did not move" | `sha256sum verifiers/verify_corpus_integrity.py` | `747b1226…` (worktree) / `391a54f4…` (4dd7753) | **FALSE at HEAD** |
| B:21 | baseline sha256 `bcbcfee1…` | `sha256sum verifiers/corpus-baseline.json` | `0ff2a16b…` | **STALE** |
| B:51-62 | §2a pinned instant: `tracked=33 … stale=2`, `report_dead=1/20 commit_total=21`, shapes `[0,19,1,0]`, `6/9` exit 1 | no commit contains that mid-landing tree | not run | **UNEXPRESSIBLE** |
| B:89-94 | §2c pre-edit capture `report_dead=0/19`, `8/9` exit 1 | idem (dirty tree at 19:24) | not run | **UNEXPRESSIBLE** |
| B:111-117 | FILE-column tokens 36 / tracked corpus files 33 | `awk -F'\|' '/^\|/ { if (NF>=4 && $3 !~ /^[-:[:space:]]*$/) print $3 }' corpus/README.md \| grep -oP '`[^`]*`' \| wc -l`; `git ls-files corpus/ \| wc -l` | `37` / `36` | **STALE** |
| B:129-130 | own spot-check `pointers: raw=21 checked=20 dead=1 excluded=1` | live independent count | `raw=32 checked=24 dead=0 excluded=8` | **STALE** |
| B:151-158 | own spot-check `commits: raw=22 quoted_excluded=1 checked=21 nonhash=0 unresolvable=0` | live independent count | `raw=23 quoted=1 checked=22 nonhash=0 unresolvable=0` | **STALE** (counts) |
| B:240,304 | `COLD RUN: 1 / 9 checks` | live plain | `9/9 checks pass` exit 0 | **STALE** (live) |
| B:315-316 | "the shipped script is byte-identical to the §6 re-gate sha256 (`2f07179c…`)" | `sha256sum`; `git show 4dd7753:… \| sha256sum` | `747b1226…` / `391a54f4…` | **FALSE at HEAD** |
| B:296 | "everything else byte-identical (33/36, stale=2, 21/0/0 commits, quoted=1, excluded=1)" | live plain/`--json` | `36/37`, `24`, `22/0/0`, quoted `1`, excluded `8` | **STALE** |
| B:42,33 | "GUARD: coherent" (one pinned instant) | — | not re-runnable (history) | **UNEXPRESSIBLE** |
| C:28 | harness `27/27 checks pass` exit 0; `--self-test` `0 failure(s) over 10 assertions`; catalogue `17/17` from cache; `grep -c '^- \[ \]' SKILL.md` → 39 | `python3 verifiers/verify_harness_claims.py`; `… --self-test`; `grep -c` | `27/27 checks pass` exit 0; `0 failure(s) over 10 assertions`; `17/17 lines from cache`; `39` | AGREES |
| C:29 | `python3 verifiers/verify_corpus_integrity.py` → `9/9 checks pass` (exit 0) | live plain | `9/9 checks pass`, exit 0 | AGREES |
| C:29 | red-before on a clone at `d49dfa5`: `report_dead=10/19 commit_total=18 unresolvable=0 nonhash=1`, shapes `relative=9 absolute=8 tilde=1 bare=1`, `7/9 checks pass` exit 1 | W0 `--no-baseline` | exact match | AGREES |
| C:29 | `--self-test` → `0 failure(s) over 80 assertions` | `git show 4dd7753:verifiers/verify_corpus_integrity.py > v11.py; python3 v11.py --repo $W0 --self-test` | `0 failure(s) over 80 assertions` at 4dd7753; **86** at HEAD | AGREES at landing / **STALE at HEAD** |
| C:29,63 | "19 of the 20 checked pointers are host-absolute" | live `--json` shapes | **23 of 24** | **STALE** |
| C:30 | coverage map "33 data rows" via the printed awk | `awk -F'\|' '/^\|/ && NF>=4 && $3 !~ /^[-:[:space:]]*$/ {n++} END{print n}' corpus/README.md` | **34** | **STALE** |
| C:31 | two committed verifiers, "4 exit codes proven each" | corpus: `0`(live)/`1`(perturbed)/`2`(notgit)/`3`(no baseline); harness: `0`/`1`(perturbed `omp.db.rows`)/`2`(empty HOME)/`3`(no baseline) | `0/1/2/3` both | AGREES |
| C:31 | `/tmp/round11/fault-injection.md`: 10/10 faults surfaced, 7 by the zero-check | file outside the repo and per the round-11 lesson `/tmp` was wiped | not run | **UNEXPRESSIBLE** |
| C:32 | db `17/44/98`; permission lines `471`; init `15×1 16×141 17×34 18×14` | `sqlite3 -readonly ~/.omp/agent/skill-descriptions.db "select count(*),min(length(description)),max(length(description)) from skill_descriptions;"`; `grep -c 'evaluated permission=skill' …`; `grep -o 'message=init count=[0-9]*' … \| sort \| uniq -c` | `17\|44\|98`; `471`; exact distribution | AGREES |
| C:34 | sibling `*-shokunin` descriptions "0/5" carry triggers/arbitration | `for f in /home/vgpnk/projects/shokunin/*-shokunin/SKILL.md; do awk '/^description:/,/^---/' $f \| grep -ci 'arbitr\|boundary'; done` | `0 0 0 0` for the five siblings (+`1` for kotoba itself, not counted) | AGREES |
| C:51 | planned falsifier `python3 verifiers/verify_corpus_independent.py --json` | `ls verifiers/verify_corpus_independent.py` | absent | planned, unmet |
| C:80 | round-10 row: "8 dead commit pointers, 4 unindexed files" | `git grep -h -o -E "commit \`round-[0-9]+\`" e997d45 -- 'corpus/*.md' \| wc -l`; `comm -13 <(git show e997d45:corpus/README.md \| grep -oE '(knowledge|lessons)/[A-Za-z0-9._-]+\.md' \| sort -u) <(git ls-tree -r --name-only e997d45 -- corpus/ \| sed 's\|^corpus/\|\|' \| sort -u)` | `8` ✓; **`7`** (README.md + 6 lesson files) | **DISAGREES** on "4" |
| C:81 | round-11 row: 10 dead pointers (9 `../.ufo` + 1 bare), 1 non-hash token, 2 md5 pins printed as commits | W0 instrument: shapes `relative=9 … bare=1`, `commit_nonhash=1`; `grep -rn '143fe473' $W0 --include='*.md'` | first three exact; md5-pin sites with `@`-notation found in-repo at W0 = **1** (`claim-scope-audit-round9.md:15`) | PARTIAL |
| C:67 | 39 checklist boxes remain lane-attested | `grep -c '^- \[ \]' SKILL.md` | `39` | AGREES |
| D:218 | "8 dead `commit round-N` pointers replaced by real hashes" | `git grep -h -o -E "commit \`round-[0-9]+\`" e997d45 -- 'corpus/*.md' \| wc -l` | `8` | AGREES |
| D:219-221 | index rows added for `lessons/round-{1,3,4}.md` (+4 audits); `comm` diff now only `README.md` | `git show e997d45:corpus/README.md \| grep -cE 'lessons/round-[134]\.md'`; same at `abef8aa` | `0` → `3` | AGREES |
| D:216-217 | "20 data-row anti-pattern table; `13/9/9/8` checklist boxes" | `awk '/^## Anti-patterns/,/^## Refusals/' SKILL.md \| grep -c '^\|'` (→22 lines = 20 rows); per-section box awk | `22` (=20 rows); `13/9/9/8` | AGREES |
| D:232-235 | harness `27/27`, exits 0/1/2/3, `--self-test` 10 assertions; 10 planted faults → 9 detected | verifier runs; fault run has no in-repo record | `27/27`, `0/1/2/3`, `0 failures / 10 assertions` ✓; faults not run | PARTIAL |
| D:185,216 | "9 kotoba-owned defects" / "9 defects → 0 open" | `grep -cE '^[0-9]+\. \*\*' corpus/lessons/round-6-aggregator-audit.md` | `9` | AGREES |
| D:247 | "39 `SKILL.md` checklist boxes remain lane-attested" | `grep -c '^- \[ \]' SKILL.md` | `39` | AGREES |
| D:244-248 | LOG carries the round-10 entry and **no** round-11 entry | `grep -nE '^## \|^- 2026' LOG.md` | rounds `0,1,3,4,5,6,7,9,10` — no round-11 section | see E:41 |
| E:35 | red-before on a clone at `d49dfa5` → `7/9 checks pass` exit 1 (`report_dead=10/19`, `commit_nonhash=1`) | W0 `--no-baseline` | exact match | AGREES |
| E:35 | worktree → `9/9 checks pass` exit 0 (`report_dead=0/19`, "all shapes checked", **1 placeholder excluded**) | live plain | `0/**24**`, `pointer-excluded=**8**` | **STALE** |
| E:35 | "9 checks … exit 0/1/2/3, `--self-test`" | live runs | `9 checks`, exits `0/1/2/3`, self-test OK | AGREES |
| E:41 | "LOG.md round-11 entry, commit `4dd7753`" | `grep -nE '[Rr]ound[- ]11' LOG.md` | only `LOG.md:244` ("Falsifiable next iteration (round 11)") — **no entry** | **FALSE at HEAD** |
| E:41 | commit `4dd7753` resolves | `git cat-file -e 4dd7753^{commit}` | OK | AGREES |
| E:16 | opencode.db "415 calls / 216 sessions"; opencode.log "471" | `sqlite3 -readonly ~/.local/share/opencode/opencode.db "select count(*),count(distinct session_id) from part where json_extract(data,'\$.tool')='skill';"`; `grep -c 'evaluated permission=skill' …` | `415\|216`; `471` | AGREES |
| E:18 | CLAUDE.md census "18 at the round-10 re-count" | `find ~ -maxdepth 6 -iname 'claude.md' -not -path '*/node_modules/*' \| wc -l` | `18` | AGREES |
| E:58-60 | godspeed "387/387 offered"; "activation 205/399 = 51.4%" | `sqlite3 … "select count(distinct session_id) from part;"` | `399` ✓; `387`/`205` not re-derived | PARTIAL |
| F:6 | four fidelity checklists "13/9/9/8 boxes" **via the printed awk** | `git show HEAD:SKILL.md \| awk '/^## /{h=$0} /^- \[ \]/{c[h]++} END{print c[h]}'` | prints an **empty line** (END prints only the last section's key, `## Sources`, which has 0 boxes) | **UNEXPRESSIBLE** |
| F:6 | 13/9/9/8 via a working command | `… END{for(k in c) print c[k],k}` | 13/9/9/8 | (true value; the printed command cannot produce it) |
| F:6 | "7-row anatomy table, 5-row decision-table table" | `awk '/^## Skill-file anatomy/,/^## Instruction surfaces/' SKILL.md \| grep -c '^\|'`; same for Decision tables | `9` and `7` pipe lines = 7 and 5 data rows | AGREES |
| F:6 | "20-data-row anti-pattern table (… → 22 lines incl. header+separator)" | `awk '/^## Anti-patterns/,/^## Refusals/' SKILL.md \| grep -c '^\|'` | `22` | AGREES |
| F:8 | round-10 verifier "27 checks, exit 0"; round-11 verifier "9 checks, red-before → green-after" | verifier runs | `27/27` exit 0; `9 checks`, red→green | AGREES |
| G:6 | landing hash `4dd7753` | `git cat-file -e 4dd7753^{commit}` | OK | AGREES |
| G:22 | landed class "covers 19 live pointers plus the 10 that were dead" | live `--json` | **24** live | **STALE** |
| G:30 | synthetic `archive + init` tree "reports 18 unresolvable commits" | synthetic-tree run | `commit_unresolvable=18` | AGREES |
| G:51 | "18 of the 19 checked pointers are host-absolute" | live `--json` shapes | **23 of 24** | **STALE** |
| G:53 | 39 checklist boxes lane-attested | `grep -c` | `39` | AGREES |
| G:12-16 | three counting recipes "could not express the class they named" | A:34/A:35, A:62-64, A:133 | all three reproduce | AGREES |
| H:336-343 | "`python3 verifiers/verify_corpus_integrity.py` exits non-zero on a dead pointer or a non-hash commit token" | W0 (defect present) `exit=1`; HEAD `exit=0` | consistent both ways | AGREES |
| H:578-580 | corpus verifier "9 checks over tracked `corpus/*.md` … exit 0/1/2/3, `--self-test`" | live runs | AGREES |
| H:8-13, 541-570 | cache `17 rows`, `all 17 keys reproduced`, 273-byte template | `python3 verifiers/verify_harness_claims.py` | `db_rows=17 offered=17 keys_reproduced=17 misses=0`, template sha match, `27/27` | AGREES |
| PROVINCE.md | — (no numeric or zero/absent claim) | `grep -cE '[0-9]' PROVINCE.md` | `0` | nothing to census |

Round 58 note (append-only): the row `F:6` anatomy recipe reads `0` from round 58 on because § Skill-file anatomy
moved verbatim to `anatomy-and-compression.md` (round 57 moved § Decision tables the same way); run the same `awk` over
that file to re-derive `9` and `7`. The verdicts above stay records of the round-12 tree.

Legend for verdicts: **AGREES** = executed command reproduces the stated value;
**STALE** = command runs and yields a *different* value at HEAD 7d15407 (the claim was
truthful for a named or unnamed older tree); **UNEXPRESSIBLE** = no command available can
express the class the claim names (the round-11 defect class), or the object of the claim
no longer exists; **FALSE at HEAD** = the claim contradicts the landed tree as a claim about
the landed tree.

---

## (a) Claims the round-12 landing must update

Live-vs-claimed deltas the landing must absorb (each moves a file that the landing already
touches):

| what moves | was | is (HEAD) | why |
|---|---|---|---|
| `corpus.index.tracked_files` | 33 (A:143) | **36** | round-11's three corpus files landed |
| `corpus.pointers.report_total` | 19 (A:147, G:22) | **24** | README round-11 row + cold-run record pointers |
| `corpus.pointers.commit_total` | 21 (A:149, C:29, B:151) | **22** | README row now cites `4dd7753` |
| `report_pointers_excluded` | 1 (A:208, E:35) | **8** | the round-11 artifacts quote the `<lane>`/`<repo>` placeholder forms |
| absolute/tilde pointer split | 18/1 of 19 (A:237, G:51, C:29/63) | **23/1 of 24** | same move |
| coverage-map data rows | 33 (C:30) | **34** | round-11 README row |
| FILE-column backticked tokens | 36 (B:111-117) | **37** | same |
| `--self-test` assertions | 80 (A table, C:29) | **86** | round-12 script edit (737b…/6e968431 lineage) |
| `--json` key set | — | adds `report_pointers_quoted` + detail | round-12 quoted-token regex fix |
| green-after block (A:168-172), E:35, B:240/296/304 | `0/19`, `21`, 1 excluded | `0/24`, `22`, 8 excluded | tree movement |

Landing must also create/fill the things it *claims* it will:

- `verifiers/verify_corpus_independent.py` (SCORECARD:51) — still **absent**; until it exists
  the `consistency 9 → 10` move has no second derivation and the planned row is unmet.
- `verifiers/corpus-baseline.json` re-record (tracked_files 36 → 38 if two new corpus files
  land, plus `report_total`/`commit_total` for the new rows).
- `SCORECARD.md`: move the round-12 row from `## planned` to `## Move log` and re-score
  `consistency` 9 → 10 (row C:29), plus C:30 coverage re-base.
- `LOG.md`: **add the round-12 entry — and the missing round-11 entry** (E:41 asserts one
  exists; it does not).
- `corpus/README.md`: new coverage rows for the round-12 artifacts; correct E:35's
  "1 placeholder excluded" and any restated 19/20/21 counts.
- `SHONEN.md`: box 2/3 evidence lines currently quote the round-11 cold run; the round-12
  independent derivation supersedes or supplements it.
- `SKILL.md` § Sources / the citation checklist box (H:336-343): unchanged in substance, but
  the "9 checks" line is safe while the round-12 script still exposes 9 check ids.

Stale-by-construction rows that need a re-qualification (tree tag) or a re-run, not
necessarily a number change: A:85, A:133, B:21, B:32/33/40/41, F:6 (printed awk), C:80's "4".

## (b) Claims no command can settle

- **A:192-193 / C:31 / D:236 — the planted-fault runs** (10 faults, 7 by zero-check, 2 by
  guards, 1 mode-masked). The fault log lived in `/tmp/round11/`, which the round-11 lesson
  says was wiped; nothing in-repo records the ten faults. Not re-derivable from the repo.
- **B:34-35, B:51-62, B:89-94 — the cold run's pinned mid-landing instants.** §2a/§2b/§2c
  describe a dirty worktree between 19:24 and 19:33 (verifier + baseline untracked). No
  commit contains that tree, so no command can reproduce those numbers; the capture guard
  (B:42) is a historical assertion.
- **B:11 (`B:255/258`) — the intermediate sha chain `631569277d… → 2f07179c…`.** Neither
  blob is reachable from the repo (`git cat-file -e` on both short shas: not objects), so
  "the changed line is visible as prose" and "comment-only" cannot be verified — only the
  landed `391a54f4…` is.
- **C:80's "4 unindexed files"** — the count has no stated command; the only command of that
  shape I can build (`comm` over `e997d45`) yields 7. Disagreement, not a stale number.
- **C:81's "2 md5 pins printed as commits"** — only one `@ <md5>` site is identifiable in-repo
  at the before-tree; the second was presumably a lane report outside the repo.
- **E:58-60's "387/387 offered" and "205/399"** — the offer-side halves need an
  opencode `session_init`/offer parse that no in-repo command encodes (I reproduced only
  the `399` denominator and `415/216`).
- **G:87 (lessons:44) "27 checks mapped to 38 claims, 14 uncovered"** — the
  `ReviewTraceability` mapping exists only as that sentence; no artifact in the repo states
  the 38/14 pair.
- **A:91-96 — the `comm: file 1 is not in sorted order` observation.** The author already
  marks it `[UNVERIFIED]`; a five-variant sweep reproduced exit 0 with empty stderr. A
  transient disk-pressure event is not a property any command can settle.

## (c) Claims already false at HEAD 7d15407

1. **E:41 "LOG.md round-11 entry"** — `LOG.md` has sections for rounds 0,1,3,4,5,6,7,9,10
   and no round-11 entry (only `LOG.md:244`, "Falsifiable next iteration (round 11)").
   The round-11 round was never logged; the index row asserts otherwise.
2. **B:315-316 "the shipped script is byte-identical to the §6 re-gate sha256
   (`2f07179c…`)"** — false twice over: the file content at the round-11 landing commit
   `4dd7753` hashes (sha256) to
   `391a54f4a64b16620bfe68f66e021cff3ee4be5dd122bfebc34c6eb4c186f29c`, and at HEAD to
   `747b1226feb05cfa49de8e300df62bd300aa03ed1886ef04d261e7ddd3d6c081`.
3. **B:15,18 (the sha256 gate `631569277d…`, "the artifact did not move, so the record
   stands")** — the stated digest matches no revision of the file (`git cat-file -e
   631569277d` → not an object; content sha256 at 4dd7753/HEAD as above); the record's
   identity gate does not hold for any shipped revision. (These are content sha256s, not git
   object ids; none of `631569277d`, `2f07179c`, `90a9f2f3`, `391a54f4`, `747b1226` exists as
   an object in this repo — the last two are `git show <commit>:<path> | sha256sum` values.)
4. **F:6's printed checklist command** — `git show HEAD:SKILL.md | awk '/^## /{h=$0}
   /^- \[ \]/{c[h]++} END{print c[h]}'` prints an empty line, so as written it cannot be the
   command that produced "→ 13/9/9/8". This is a *fourth* instance of the round-11 defect
   class (a counting command that cannot express the class it names), sitting in the file the
   round-10 audit explicitly used that same awk to *correct* `SHONEN.md:6` (see
   `corpus/lessons/round-6-aggregator-audit.md:30`, where the same expression is printed with
   the same defect and read as producing 13/9/9/8).

Everything else that no longer matches is tree-qualified (`@ round-11 commit`,
`@ round-11 worktree`, "@ e997d45"), hence **STALE** rather than false — but note that
`A:143` "33 (unchanged)" and `A:147` "19 → 19" are stated in the *present tense* with no
tree tag inside the verifier table, and the artifact's own thesis (A:3) is that a number is
only as good as its command.

---

## What I could not check

- The two unreachable blobs (`631569277d…`, `2f07179c…`): not git objects.
- The pre-round-10 tree for `C:80`'s "4 unindexed files": I measured `e997d45` (round-9
  close), which is the tree the round-10 audit quotes; a different intermediate worktree may
  have produced 4.
- `fault-injection.md`, `round11/spot_checks.py` re-execution: outside the repo, gone.
- Harness/host rows (`C:28/C:32/E:16/E:18`) are live host state, not repo state: they agree
  today but are not round-12-tree claims.
- `PROVINCE.md` carries no counting claim; `§ Known gaps` in `corpus/README.md` is
  qualitative ("unmeasured", "absent") with no counting command, so it contributes no rows
  except where it restates numbers already censused (E:58-60).

Scratch: `/tmp/round12/ScoutClaimCensus/{w0,w1,synth,live.json,w0.json,r1.json,r2.json,perturbed-baseline.json,harness-perturbed2.json,v11-landed.py}`.