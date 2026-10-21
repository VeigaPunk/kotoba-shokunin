verdict: round-47 search-log template drafted; BASE census re-measured green (11 rows, 0 malformed, validate exit 0), but three BASE search-log entries misstate the contract or their own counts (SOURCES.md:48, :52, :56-60, :65) — the template repairs the shape; the L1 fills real counts; no row was opened or admitted by this lane.

# SrcSearchLog — round-47 draft (leaf lane SrcSearchLog, read-only on production)

BASE: `c61a973b2e02e1ded169703ddcb06466f4edd8bd` (kotoba-shokunin, branch master). Verified: `git rev-parse HEAD` → `c61a973b2e02e1ded169703ddcb06466f4edd8bd` (rc 0); `git diff --quiet c61a973b… -- corpus/SOURCES.md` → rc 0 (no working-tree drift in the target).

Contract source of truth: `.ufo/waves/kaika/SOURCES-CONTRACT-v1.md` (fleet root; sha256 `6c674a2281fb75b2de11790ebfe34fdcf7ddde61a6734d2eca302f023966119`). Its census block is `:64-81`; rule 5 (search log) is `:59-61`; rule 4 (no row quota) is `:56-58`; rule 1 (Gate evidence) is `:45-48`. Mirror: `CORPUS.md:64` (section), census block `:131-148`.

## 1. Findings at BASE

### F1 — census re-measured green; the frozen commands discriminate planted defects (non-vacuous)
- Frozen census at BASE, cwd = kotoba lane root (all rc 0):
  - rows = `11`; malformed (NF≠13) = `0`; tier histogram `A=10 C=1` (no B); status histogram `mined=4 queued=6 rejected=1`; duplicate ids = none; enum/tier-inflation violations = none; mined rows with missing used-by = none.
- Maintained CLI (`scripts/sources-census.sh`, read-only per its header):
  - `validate --root /home/vgpnk/Projects/shokunin kotoba` → `kotoba ok …corpus/SOURCES.md`, rc 0.
  - `census --root … kotoba` → `rows 11`, `tier.A 10`, `tier.C 1`, `status.mined 4`, `status.queued 6`, `status.rejected 1`, `FLEET missing 0`, rc 0.
  - `selftest` → every mutant line `killed`, final `selftest ok`, rc 0.
- Synthetic planted-defect fixture (scratch only: `/fast/scratch/kotoba-r47/SrcSearchLog/synth/corpus/SOURCES.md`, 9 rows):
  - Frozen awk flags: malformed NF=12 row (1), duplicate `S001` (printed), tier `D`, status `watch`, community-at-A, kind `blog`, mined row with dangling used-by `corpus/knowledge/absent-synth.md`. All caught.
  - Maintained `validate --file` → rc 1 with E01, E03, E06, E07, E10, E05, E11 (each planted defect named).
  - **Counterexample (silent undercount, documented):** the planted 2-space-indented valid row `S009` is counted by the maintained `census` (`rows 9`) but not by frozen `grep -cE` (`rows(grep)=8`). Frozen checks assume column-zero input (`CORPUS.md:150-154`). Consequence: the frozen census cannot be the only gate. Use the maintained `validate`/`census` as the primary gate and the frozen commands as a cross-check.
  - Frozen checks also do not cover E04 (duplicate URL), E08 (future `opened`), E09 (bad recheck), E12 (row outside Registry) — only the maintained `validate` does.

### F2 — search-log entry 1 cites a contract requirement that does not exist
- `corpus/SOURCES.md:52`: "Stop rationale: the contract asks 8–14 honest rows". The string `8–14` appears nowhere in `SOURCES-CONTRACT-v1.md` (grep: 0 hits). The contract says the opposite: rule 4, `…SOURCES-CONTRACT-v1.md:58` "no row quota; a short registry of opened, honestly tiered rows beats a long one."
- Fix in the template: the stop rationale cites rule 4 by line, not an invented number.

### F3 — search-log entry 1 counts are approximations, and the leads count is wrong
- `corpus/SOURCES.md:48-51`: "Identified 30 rows + ~40 lead bullets … excluded ~21 rows". `~` makes these non-counts; rule 5 asks for counts.
- Arithmetic check: 30 identified − 9 included (8 external + S011) = 21 excluded holds only if the `~21` is exact. Not verified as exact by any log line.
- "~40 lead bullets": the Leads section `corpus/SOURCES.md:68-87` contains **18** `^- ` bullets (`awk 'NR>68 && /^- /{n++}'` → 18, rc 0). The `~40` is not reproducible from the file.
- Template requires exact counts and the invariant `identified − duplicates = screened = included + excluded`.

### F4 — search-log entry 2 (own-work gate selection) identifies 2 of 10 instruments and records 0 exclusions
- `corpus/SOURCES.md:54-60`: "Identified 2 candidate instruments … screened 2; included 2; excluded 0." The `verifiers/` directory holds **10** `.py`/`.sh` instruments: `check_assertion_floors.py check_substrate_pins.py compare_harness_independent.py fault_injection_corpus.sh verify_corpus_independent.py verify_corpus_integrity.py verify_harness_claims.py verify_harness_independent.py verify_skill_checklist.py verify_surfaces.py` (`ls verifiers | grep -E '\.(py|sh)$' | wc -l` → 10, rc 0).
- Rule 5 requires "a negative claim carries its sweep". The 8 unlisted instruments are neither identified-and-excluded nor explained. "Stop rationale: those are the two instruments this round's claims … rest on" is a scope argument, not a sweep. Template requires the full candidate list with per-item disposition.

### F5 — search-log entry 3 attributes a minimum to the contract that is not in it
- `corpus/SOURCES.md:65`: "Stop rationale: contract requires at least one rejected row". Grep of `SOURCES-CONTRACT-v1.md` and `CORPUS.md` for `at least one` → 0 hits; the contract defines `rejected` only as a status (`:36-37`, "kept — a rejection is evidence of taste") with no minimum. The `≥1 rejected row` phrase appears in fleet text at `.ufo/waves/kaika/lane-addendum.md` (grep, rc 0), which is not the frozen contract.
- Fix: cite `lane-addendum.md` for the minimum, or drop it; do not cite the contract.

### F6 — provenance pointers that do not resolve on this host
- `corpus/SOURCES.md:87` ("Full unopened lead lists in `.tower` fleet-ledger `kaika-w1/kotoba-art.md`") and `:45` (`kotoba-art.md` §3, the 30-row draft): `/home/vgpnk/Projects/shokunin/.tower/worktrees/kaika/` does not exist (`ls` → rc 2, "No such file or directory"); `kotoba-art.md` is not present in the kotoba repo (`grep -rln kotoba-art .` → only `corpus/SOURCES.md`). Entry 1's "identified 30" and the leads list cannot be re-derived from this host.
- The sample `fetch-log.json` the contract points at IS reachable: `.ufo/round-46/evidence/w2/sources/fetch-log.json` (11 rows, S001–S011, UTC access dates, sha256 per row). Its own `cwd` field (`.tower/worktrees/kaika/kotoba-shokunin`) is stale. Rule 1 Gate: `corpus/lessons/round-46.md:47` (`## Gate` present). Gate-table row text at `corpus/lessons/round-46-verifier-spotcheck.md:12` calls S006 "admitted"; the registry row is `corpus/SOURCES.md:19` status `queued`. Vocabulary mismatch (admitted vs queued) — not a status change logged old→new (rule 2).

### F7 — census block drift between contract and mirror (cosmetic, measured)
- `diff <(sed -n '64,81p' SOURCES-CONTRACT-v1.md) <(sed -n '131,148p' CORPUS.md)` → only line 1 differs: `## Census` (contract) vs `### Census` (CORPUS.md:131). Command bytes identical; rc 1 from diff (differences found).

## 2. Commands run (all read-only; no git write; no install)

| # | command (cwd) | exit | key output |
|---|---|---|---|
| 1 | `git log --oneline -1` (kotoba) | 0 | `c61a973 round-46 verifier spot-check …` |
| 2 | `git rev-parse HEAD` (kotoba) | 0 | `c61a973b2e02e1ded169703ddcb06466f4edd8bd` |
| 3 | `git diff --quiet c61a973b… -- corpus/SOURCES.md` | 0 | no drift |
| 4 | frozen census rows / malformed / tier / status / dup / enum / mined-missing (7 commands, kotoba root) | 0 each | `11`; `0`; `A=10 C=1`; `mined=4 queued=6 rejected=1`; none; none; none |
| 5 | `scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kotoba` | 0 | `kotoba ok …/corpus/SOURCES.md` |
| 6 | `scripts/sources-census.sh census --root … kotoba` | 0 | `rows 11`, `tier.A 10`, `tier.C 1`, `status.queued 6`, `status.mined 4`, `status.rejected 1`, `FLEET missing 0` |
| 7 | `scripts/sources-census.sh selftest` | 0 | all `killed`, last `selftest ok` |
| 8 | synthetic fixture: frozen commands + `validate --file` + `census --file` (scratch) | 0 / 1 / 0 | planted defects caught; frozen `grep` rows 8 vs maintained 9 |
| 9 | `awk 'NR>68 && /^- /{n++} END{print n+0}' corpus/SOURCES.md` | 0 | `18` |
| 10 | `ls verifiers \| grep -E '\.(py\|sh)$' \| wc -l` | 0 | `10` |
| 11 | `grep -n 'quota\|8–14' SOURCES-CONTRACT-v1.md` | 0 (only `quota` hit, `:58`) | `:58` "no row quota"; `8–14` absent |
| 12 | `grep -rn '8–14\|at least one\|≥1 rejected row\|rejected row' corpus/SOURCES.md CORPUS.md corpus/QUALITY.md` | 0 | only the lane's own `:48` ("1 rejected row"), `:52` (`8–14`), `:65` (`at least one`) |
| 13 | `grep -rl '≥1 rejected row' .ufo/waves/kaika prompts` | 0 | `.ufo/waves/kaika/lane-addendum.md` |
| 14 | `ls /home/vgpnk/Projects/shokunin/.tower/worktrees/kaika/` | 2 | No such file or directory |
| 15 | `git cat-file -t 78ee57e` | 0 | `commit` (the S009 anchor resolves) |
| 16 | `sha256sum corpus/SOURCES.md CORPUS.md SOURCES-CONTRACT-v1.md` | 0 | SOURCES `ef331658…`, CORPUS `88556402…`, contract `6c674a22…` |
| 17 | `diff <(sed -n 64,81p contract) <(sed -n 131,148p CORPUS.md)` | 1 | only line 1 (`##` vs `###`) |

## 3. Counterexamples (what the template must not allow)

- A census that passes while a planted row is malformed → refuted: frozen awk and maintained validate both flip on planted defects (F1).
- A `~` or unspecified count in a search entry → refuted by F3 (`~21`, `~40` vs 18 bullets).
- A negative claim ("only two instruments qualify") without the candidate list → refuted by F4 (10 present, 2 identified, 0 excluded).
- A stop rationale citing a contract line that does not say it → refuted by F2 and F5.

## 4. Draft entries — template for the L1 (fill real counts; do not copy BASE numbers into new entries)

Contract rule 5 fields in order. Invariant to satisfy per entry: `identified − duplicates = screened = included + excluded`; `Δrows = included_new` for the registry.

```
### 2026-10-21 — round-47 <question-id>: <question as asked>
- Question / query: <exact query string or question text>
- Where searched: <each venue with its path or URL; for repo-local sweeps, the glob or directory listed>
- Date(s) searched: <ISO dates; UTC if fetched>
- Identified: <n_raw> raw; <n_dup> duplicates removed; <n_identified> after dedup
- Screened: <n_screened> (= <n_identified>; title/scope screen recorded per item in <path>)
- Included: <n_included> — row ids <S0NN …>; each opened this round with URL, UTC access date, ≤25-word quote located in `corpus/lessons/round-47.md ## Gate` (rule 1)
- Excluded: <n_excluded> — by reason: <reason A> = <k>; <reason B> = <k>; …  (must sum to n_excluded)
- Negative-claim sweep (required if any claim says "none"/"only"): <full candidate list with per-item disposition, or the command and its complete output>
- Stop rationale: <why more searching would not change an admitted row; cite the rule by line, e.g. SOURCES-CONTRACT-v1.md:58 for "no row quota">
```

Round-47 entries to fill (one per bounded search; no combined entries):
1. Frontier sweep for round-47 candidate rows (the wave's real search): fill from the wave's scouts' reports; list every candidate.
2. Own-work gate selection: candidates = every instrument in `verifiers/` (10 at BASE: list them); each gets an include/exclude line with reason.
3. Rejected-row verification (if re-run): cite the lane-addendum for any minimum; quote ≤25 words.

Round-47 summary line (L1 fills): `registry rows <BASE 11> → <after>; tier A/B/C <before 10/0/1> → <after>; status mined/queued/rejected <before 4/6/1> → <after>; Σ included across entries = Δrows; Σ identified/screened/included/excluded across entries reconciled with the registry`.

## 5. Census commands (copied verbatim from `SOURCES-CONTRACT-v1.md:66-80`; mirror `CORPUS.md:133-146`)

Run from the kotoba lane root. Expected at BASE shown after `#`.

```sh
# rows (spacing-tolerant)                                   # BASE: 11
grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md
# malformed rows — 11 columns means NF=13; must print 0      # BASE: 0
awk -F'|' '/^\|[[:space:]]*S[0-9][0-9][0-9]+[[:space:]]*\|/ && NF!=13 {n++} END{print n+0}' corpus/SOURCES.md
# tier histogram                                            # BASE: A=10 C=1
awk -F'|' '/^\|[[:space:]]*S[0-9][0-9][0-9]+[[:space:]]*\|/ {t=$5; gsub(/[[:space:]]/,"",t); n[t]++} END{for(k in n) printf "%s=%d ", k, n[k]; print ""}' corpus/SOURCES.md
# status histogram                                          # BASE: mined=4 queued=6 rejected=1
awk -F'|' '/^\|[[:space:]]*S[0-9][0-9][0-9]+[[:space:]]*\|/ {s=$9; gsub(/[[:space:]]/,"",s); n[s]++} END{for(k in n) printf "%s=%d ", k, n[k]; print ""}' corpus/SOURCES.md
# duplicate ids — must print nothing                        # BASE: (none)
awk -F'|' '/^\|[[:space:]]*S[0-9][0-9][0-9]+[[:space:]]*\|/ {i=$2; gsub(/[[:space:]]/,"",i); print i}' corpus/SOURCES.md | sort | uniq -d
# enum violations and tier inflation — must print nothing   # BASE: (none)
awk -F'|' '/^\|[[:space:]]*S[0-9][0-9][0-9]+[[:space:]]*\|/ && NF==13 {i=$2;k=$4;t=$5;s=$9; gsub(/[[:space:]]/,"",i); gsub(/[[:space:]]/,"",k); gsub(/[[:space:]]/,"",t); gsub(/[[:space:]]/,"",s); if (t !~ /^[ABC]$/) print "tier", i, t; if (s !~ /^(queued|mined|rejected)$/) print "status", i, s; if (k !~ /^(spec|docs|paper|code|tool|dataset|talk|book|community|own-work)$/) print "kind", i, k; if (t=="A" && k=="community") print "tier-inflation", i}' corpus/SOURCES.md
# mined rows whose used-by paths do not exist — must print nothing   # BASE: (none)
awk -F'|' '/^\|[[:space:]]*S[0-9][0-9][0-9]+[[:space:]]*\|/ && NF==13 {s=$9; gsub(/[[:space:]]/,"",s); if (s=="mined") {n=split($12, a, /[,;]/); for (j=1;j<=n;j++) {p=a[j]; gsub(/^[[:space:]]+|[[:space:]]+$/,"",p); if (p!="" && p!="—") print p}}}' corpus/SOURCES.md | while read -r p; do [ -e "$p" ] || echo "missing: $p"; done
```

Maintained gate (primary; read-only) — run from the workspace root:

```sh
scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kotoba   # BASE: kotoba ok …, rc 0
scripts/sources-census.sh census   --root /home/vgpnk/Projects/shokunin kotoba   # BASE: rows 11, FLEET missing 0, rc 0
scripts/sources-census.sh selftest                                                # BASE: selftest ok, rc 0
```

## 6. Tooling

No installs or upgrades. Tools used: `git` (read-only subcommands), `awk`/`grep`/`sed`/`sha256sum`/`diff`, the repo's `scripts/sources-census.sh`. No pacman transaction.

## 7. Not checked

- No source was re-opened or re-fetched; no URL, access date or sha256 in `fetch-log.json` was re-verified against the live pages (rule 1's non-author sample is not this lane's job).
- `kotoba-art.md` (the 30-row draft and the leads dossier) was not inspected: the `.tower` path is absent on this host (F6).
- `sources-census.sh overdue` and the `--json`/`shared` modes were not run.
- Lead bullets in `corpus/SOURCES.md:70-87` were counted, not opened.
- Whether the lane-addendum minimum (`.ufo/waves/kaika/lane-addendum.md`) is binding was not read; only the phrase's location was grepped.
- The round-47 wave's real search (scouts' candidate lists) was not in scope; the template leaves those counts to the L1.
- The synthetic fixture lives in scratch only; nothing was written to production files, and no patch was produced (this lane writes only this report).
