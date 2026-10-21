verdict: the round-end census can fail. `validate` exits 1 on each required synthetic defect (E01, E10, E11) and frozen F2/F6/F7 print each one, but all seven frozen commands exit 0 even when they print findings, `census` never fails on content, and a mined row with a blank used-by cell passes with exit 0 (a mined row with `—` only warns).

# SrcCensusDryRun — round-47 round-end census dry run

## 0. Scope, identity, writes

- Lane: kotoba, BASE `c61a973b2e02e1ded169703ddcb06466f4edd8bd` (branch master, detached in scratch clone).
- Production `corpus/SOURCES.md`: blob `a048aef0997e68881c9740e878d2fe01402bb04b` (= BASE blob via `git hash-object`), sha256 `ef331658e398dd552f8df992aade49d25025eb7b0309e7f2d3c00a7fd92e16d3`. Checked with `git hash-object` in the production worktree and by sha256 of the bytes; `git status` was deliberately not run in production (index refresh).
- Fleet root is a separate repo (not kotoba BASE). `scripts/sources-census.sh`, `CORPUS.md`, `shokunin.conf` cited below are fleet files at fleet HEAD `879df5ee61e92e935346e98c7947ccf90a8cabcf`; their blobs equal the worktree: `scripts/sources-census.sh` `3f314620…` (last changed in `6a1dd8ce`, 2026-10-19T21:22:45-03:00), `CORPUS.md` `882d6ca8…`, `shokunin.conf` `0ce6db89…`.
- Run: 2026-10-21, 15:58–16:03 UTC. `--today` default = `date -u +%F` = 2026-10-21.
- Writes: scratch only (`/fast/scratch/kotoba-r47/SrcCensusDryRun/`) plus the three build artifacts listed in §7. No production file touched. No git mutation in production. No subagent dispatched.

## 1. Axes

- **freshness:** reproduces the before-value (`kotoba-shokunin/.ufo/waves/round-47/before/SUMMARY.md`, line 2: `census: kotoba ok exit=0`). The frozen § Census commands were extracted verbatim from `CORPUS.md:135–147` at run time, not retyped.
- **operability:** only `validate` carries an exit contract (`scripts/sources-census.sh:16–18` header; findings set `findings=1` at `:739–741` and exit 1 at `:805`). The frozen block prints text and never sets exit status.
- **calibration:** `validate` flags every real violation in the probe set except two contract violations (§5, CE-3 and CE-4). The frozen block misses the same two, and misses or miscounts six more (CE-5 to CE-7).

## 2. BASE facts (path:line at c61a973)

- `corpus/SOURCES.md:12–13` table header and separator; registry rows `:14–24` (S001–S011); `:26` `## Paths`; file is 87 lines (last line `:87`).
- Mined rows at BASE: S001 `:14`, S002 `:15`, S003 `:16`, S008 `:21`. All cite `SKILL.md` in `used-by`. `SKILL.md` is tracked (blob `5d9486f3…`), so the mined-row existence check passes at BASE.
- Only community row: S011 at tier C (`:24`, rejected). Counts at BASE: rows 11, tier A 10 / C 1, status mined 4 / queued 6 / rejected 1.
- Contract text (fleet `CORPUS.md`): `status` `mined` = "cited by ≥1 path in `used-by`" (`CORPUS.md:103–104`); `used-by` = repo-relative paths, comma-separated, or `—` (`:107–108`); `id` has no `|` and is `S` + 3 or more digits (`:89`).

## 3. Commands run and exit codes

```
C-PROD  bash /home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kotoba
        rc 0 | kotoba<TAB>ok<TAB>/home/vgpnk/Projects/shokunin/kotoba-shokunin/corpus/SOURCES.md
C-BASE  same command, --root /fast/scratch/kotoba-r47/SrcCensusDryRun/roots/base_BASE (BASE bytes, SKILL.md copy)
        rc 0 | kotoba<TAB>ok<TAB>…/roots/base_BASE/kotoba-shokunin/corpus/SOURCES.md
F1–F7   bash -c '<CORPUS.md line 135,137,…,147>' with cwd = <root>/kotoba-shokunin, env PATH=/usr/bin:/bin
        rc 0 for all seven commands in all 15 variants and production (frozen-rcs=[0] everywhere)
selftest bash scripts/sources-census.sh selftest  → rc 0, 96 "killed", 0 "SURVIVED", last line "selftest ok"
```

Frozen outputs at BASE (identical in scratch and production):

```
F1 rows                     11
F2 malformed (must 0)       0
F3 tier histogram           A=10 C=1
F4 status histogram         mined=4 queued=6 rejected=1
F5 duplicate ids            (empty)
F6 enum / tier inflation    (empty)
F7 mined used-by missing    (empty)
census kotoba (rc 0)        rows 11 · tier.A 10 · tier.C 1 · status.mined 4 · status.queued 6 · status.rejected 1
overdue (rc 0)              11 cadence lines, 0 overdue
shared (rc 0)               (empty)
```

Environment: `/usr/bin/awk` → gawk 5.4.1; `/usr/bin/grep` GNU grep 3.12-modified; `/usr/bin/sort`, `/usr/bin/uniq` GNU coreutils 9.12; bash 5.3.20; `TZ` and locale as inherited (`LANG=en_US.UTF-8`).

## 4. Synthetic rows and the probe matrix

Required (scratch copy, inserted directly after the S011 registry row, `corpus/SOURCES.md:24`):

- **REQ-A** S012, malformed: 12 cells (one trailing extra cell, so NF=14).
- **REQ-B** S013, `community` at tier `A`.
- **REQ-C** S014, `mined` with `used-by` = `corpus/knowledge/does-not-exist.md`.

Probes P1–P10 were added to test the classes the required rows do not exercise (counterexamples, §5). Each variant is a separate root; `reqABC` is the combined file.

| variant | F1 rows | F2 malformed | F5 dup ids | F6 enum/tier | F7 used-by | validate rc → output | census rc / rows |
|---|---|---|---|---|---|---|---|
| BASE (scratch and production) | 11 | 0 | ∅ | ∅ | ∅ | **0** `ok` | 0 / 11 |
| REQ-A malformed, 12 cells | 12 | **1** | ∅ | ∅ | ∅ | **1** `E01 S012 fields=12` | 0 / 12 |
| REQ-B community at A | 12 | 0 | ∅ | **`tier-inflation S013`** | ∅ | **1** `E10 S013 community-at-A` | 0 / 12 (tier.A 11) |
| REQ-C mined, used-by missing | 12 | 0 | ∅ | ∅ | **`missing: corpus/knowledge/does-not-exist.md`** | **1** `E11 S014 missing used-by corpus/knowledge/does-not-exist.md` | 0 / 12 (mined 5) |
| REQ-A+B+C combined | 14 | 1 | ∅ | S013 | S014 path | **1** E01 + E10 + E11 | 0 / 14 |
| P1 indented 2 spaces, 12 cells (S015) | 11 | **0 — miss** | ∅ | ∅ | ∅ | **1** `E01 S015 fields=12` | 0 / 12 |
| P2 row after `## Leads`, at EOF (S015) | 12 | 0 | ∅ | ∅ | ∅ | **1** `E12 S015 row outside Registry section` | 0 / 11 |
| P3 mined, blank used-by (S016) | 12 | 0 | ∅ | ∅ | **∅ — miss** | **0** `ok` — **miss** | 0 / 12 (mined 5) |
| P4 mined, used-by `—` (S017) | 12 | 0 | ∅ | ∅ | ∅ | **0** + `W03 S017 mined but unused` | 0 / 12 (mined 5) |
| P5 duplicate id S011 | 12 | 0 | **S011** | ∅ | ∅ | **1** `E03 S011 duplicate id` | 0 / 12 |
| P6 kind blog, tier D, status watch (S018) | 12 | 0 | ∅ | **`tier S018 D` · `status S018 watch` · `kind S018 blog`** | ∅ | **1** `E05`, `E06`, `E07` | 0 / 12 (tier.invalid 1, status.invalid 1) |
| P7 opened 2026-12-01 (S019) | 12 | 0 | ∅ | ∅ | ∅ | **1** `E08 S019 opened=2026-12-01` | 0 / 12 |
| P8 recheck `90 days` (S020) | 12 | 0 | ∅ | ∅ | ∅ | **1** `E09 S020 recheck=90 days` | 0 / 12 |
| P9 same URL and scope as S001 (S021) | 12 | 0 | ∅ | ∅ | ∅ | **1** `E04 S021 duplicate url … within scope …` | 0 / 12 |
| P10 two-digit id `S22` | **11 — row dropped** | **0 — miss** | ∅ | ∅ | ∅ | **1** `E02 S22` | 0 / 12 |
| production, literal command | 11 | 0 | ∅ | ∅ | ∅ | **0** `ok` | 0 / 11 |

`∅` = empty output. F3/F4 histograms are informational (no pass criterion) and changed as expected; they are in the JSON. `overdue` and `shared` exit 0 for every variant with no findings, since no recheck or cross-lane defect was injected.

**Catchers for the three required rows:** REQ-A is caught by F2 and by `validate`. REQ-B is caught by F6 and by `validate`. REQ-C is caught by F7 and by `validate`. `census`, `overdue`, `shared`, F1, F3, F4 and F5 catch none of the three. F1, F3 and F4 count the row and nothing more. F5 has no duplicate in these variants.

## 5. Counterexamples and calibration gaps

**CE-1. The frozen § Census block cannot fail.** Every frozen command exits 0 when it prints a finding (REQ-A F2 = 1 rc 0; REQ-B F6 rc 0; REQ-C F7 rc 0; P5 F5 rc 0; P6 F6 rc 0; all 15 variants). The "must print nothing" convention is in comments only (`CORPUS.md:136, 142, 144, 146`); the commands themselves have no exit logic (`CORPUS.md:135–147`). F7's pipeline ends in a `while` loop whose last command is `echo`, so it also exits 0.

**CE-2. `census` mode never fails on content.** rc 0 in all 15 variants, including P6 where `tier.invalid` and `status.invalid` are non-zero. `census` exits 1 only on a missing registry (`scripts/sources-census.sh:803`). Its outputs are counts only (`:690–694`, `:766–772`). Round-end gate must be `validate`.

**CE-3. A mined row with a blank `used-by` passes the gate (P3, rc 0, `ok`).** `validate` checks `used-by` only for mined rows (`scripts/sources-census.sh:559`) and silently drops blank cells (`:565`: `[ -n "$path" ] && [ "$path" != "—" ] || continue`). W03 fires only on the literal `—` (`:673`). Frozen F7 has the same skip (`CORPUS.md:147`: `if (p!="" && p!="—")`). Contract violated: `CORPUS.md:103–104` (mined = cited by ≥1 path).

**CE-4. A mined row with `used-by` = `—` is warning-only (P4, rc 0).** The gate emits `W03` (`scripts/sources-census.sh:673–674`). The header says W-codes never change status (`:31–33`; exit contract `:16–18`). The contract says mined requires ≥1 path (`CORPUS.md:103–104`), so the gate passes a contract violation. Frozen F7 also skips `—` (`CORPUS.md:147`).

**CE-5. Frozen F1 and F2 are column-zero only (P1).** The regexes anchor `^\|` (`CORPUS.md:135, 137`). The maintained parser accepts 0–3 leading spaces and records that "frozen manual examples assume column-zero input" (`scripts/sources-census.sh:40–42`; strip at `:616`). P1 (2-space indent, 12 cells): F2 = 0 (miss), F1 = 11, census = 12, `validate` = E01 rc 1.

**CE-6. "Rows" is not a single number.** F1 counts column-zero S-rows anywhere in the file (`CORPUS.md:135`), so P2 (row after `## Leads`) gives F1 = 12. The gate counts only rows inside `## Registry` (`scripts/sources-census.sh:618–624`; census emit `:690–691`), so census = 11 and `validate` flags E12 rc 1. P1 goes the other way: F1 = 11, census = 12. A round-end "rows" figure from the frozen block can disagree with the gate's own census in either direction.

**CE-7. Frozen commands are blind to the id shape and to the date, recheck and URL rules.** The frozen regexes require `S[0-9]{3,}` (`CORPUS.md:135–147`). P10 (`S22`) drops out of F1 (11) and F2 (0) entirely, while `validate` flags E02 rc 1 (`scripts/sources-census.sh:637, :640`). P7 (future `opened`), P8 (prose `recheck`) and P9 (duplicate URL within a scope) pass all seven frozen commands. `validate` catches them as E08 (`:660–662`), E09 (`:663–667`) and E04 (`:643–649`). E04 is exempt when `teaches` contains `supersedes S0NN` (`:648`).

**CE-8. Tooling confound, checked, no discrepancy.** The bash tool's shell resolves `grep`, `sort`, `uniq` to shell builtins that report themselves as `pi-uu-grep 0.2.0`, `sort 0.8.0`, `uniq 0.8.0`. The matrix ran with `PATH=/usr/bin:/bin` (GNU tools above). Re-running F1 and F5 in the harness shell gave identical results: BASE root gives `11` and empty; P5 root gives `12` and `S011`. mawk was not tested (awk here is gawk).

**CE-9. Code-read divergence, not probed.** Frozen F7 splits `used-by` on `[,;]` (`CORPUS.md:147`). The gate splits on `,` only (`scripts/sources-census.sh:562`), and the contract says comma-separated (`CORPUS.md:107–108`). A `;` list is therefore checked per path by F7 but as one string by `validate`.

**Advice for L1 (not applied; this lane edits nothing in production):**
1. Make `validate` the round-end gate and say so in `CORPUS.md` § Census, since the frozen block cannot fail (CE-1, CE-2).
2. Treat mined + blank `used-by` as an E-class finding, and mined + `—` as E per `CORPUS.md:103–104` (CE-3, CE-4).
3. If the frozen block stays, let F1 and F2 accept 0–3 leading spaces and any `S[0-9]+` id, and make it exit non-zero when it prints (CE-5, CE-6, CE-7). Otherwise drop it in favour of `validate`.

## 6. What I did NOT check

1. Fleet-wide census (`census` with no lane arguments, all 13 child lanes). Scope was `kotoba` only.
2. Validate codes not probed: E04 `supersedes` exemption beyond the code read; W01 (tier-C mined with a path), W02 (thin reject), W04 (same URL across scopes; the script's selftest covers it), and E05/E06/E07 separately from the P6 combination.
3. `overdue` with a truly overdue row (only the script's own selftest covers overdue exit 1). `shared` with two or more lanes (no positive case run).
4. `--today` other than the UTC default, and TZ dependence (`mktime` at `scripts/sources-census.sh:55, :587`).
5. awk implementations other than gawk 5.4.1 (mawk, busybox); locales other than the inherited `en_US.UTF-8`.
6. Non-mechanical contract rules: "opened this round" (`CORPUS.md:112–115`), reverse back-references from knowledge entries, referential integrity of `## Paths` / `## Search log` / `## Leads`, and the `teaches` length rule beyond the W02 code read.
7. Whitespace and encoding variants: 3-space indent, tabs, CRLF/BOM, lowercase ids (`s001`), escaped `\|`.
8. Contents of `scripts/fixtures/sources-census/`. I observed only the selftest summary (96 killed, 0 SURVIVED, rc 0).
9. Used-by target content (existence only, as E11 defines it). I did not diff production `SKILL.md` against BASE; E11 passing shows only that it exists.
10. Lane-wide gates (`verify_*.py`) and the C1–C3 claims. Out of this assignment.
11. Production worktree cleanliness beyond the `SOURCES.md` blob and the census outputs.

## 7. Artifacts and tooling

- `.ufo/waves/round-47/build/SrcCensusDryRun.md` (this report).
- `.ufo/waves/round-47/build/SrcCensusDryRun.matrix.json` (101,869 bytes): argv, cwd, rc, stdout and stderr for all 15 variants, production and the selftest; per-variant sha256; the seven frozen command strings with `CORPUS.md` line numbers; the probe rows and their cell counts (REQ-A 12, P1 12, others 11).
- `.ufo/waves/round-47/build/SrcCensusDryRun.patch` (2,533 bytes): probe-only `git diff` (a/ b/ prefixes) adding REQ-A/B/C after S011 in `corpus/SOURCES.md`. `git apply --check -R` passes against the scratch lane. This is a probe, not a fix. Do not apply.
- Scratch: `/fast/scratch/kotoba-r47/SrcCensusDryRun/lane` (clone at BASE; its `corpus/SOURCES.md` currently holds the REQ-A/B/C file) and `roots/<variant>/` (a `shokunin.conf` copy, `kotoba-shokunin/corpus/SOURCES.md` for that variant, and a `kotoba-shokunin/SKILL.md` copy from BASE).
- Installs/updates: none (no pacman, uv or npm). Environment observed only (§3).
- Subagents: none. Labrat: not used.
