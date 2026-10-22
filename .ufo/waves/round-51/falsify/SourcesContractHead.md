# SourcesContractHead — round-51 falsify, SOURCES.md contract slice

Verdict: HOLDS-BOUNDED. The registry mechanics hold at HEAD 59903b26: the five used-by edits are append-only, S030 and S031 are well formed, the warning set matches round start, and both new sources re-open byte-identical today. One row clause (S031 teaches) names a settings key its cited page does not contain (F1), one entry paragraph cites a page with no row (F2), and the Search log has no round-51 note (F3).

Scope: seat KotobaR51.SourcesContractHead, leaf, no dispatch. Lane `/home/vgpnk/Projects/shokunin/kotoba-shokunin`. BASE `43ca0bfb74372f2a67a48e0aeb2e35d0d98b1d10`; HEAD `59903b2637689739a5b9901956301da72d0effe1` (committed 2026-10-22T12:12:02-03:00). BASE and HEAD runs used a private clone at `/fast/scratch/hyaku/kotoba-r51/falsify/SourcesContractHead/lane`. Lane writes: this report file only.

## Checks asked for (all pass)

1. Diff scope (E2, E7). One hunk, 7 insertions and 5 deletions. Rows 29 → 31; added S030 and S031; removed none. The five changed rows (S021, S022, S024, S025, S029) differ in cell index 10 (used-by) only, and each new value is the old value plus an appended path. Rule 2 holds.
2. New rows (E7, E9). S030 and S031 each have 11 cells with no extra pipe; census E01 count 0. Both have opened 2026-10-22, recheck 90d (valid, E09 count 0), kind docs, tier A, status mined. Every used-by path exists at HEAD.
3. Validity (E1, E5). Validate at HEAD exit 0, no E-code. Overdue exit 0; S030 and S031 reported as cadence, nothing overdue.
4. Warning set (E1, E3, E4). Round start (BASE) and HEAD print the same three lines: `W04 S018`, `W04 S019`, `W04 S021` (duplicate URLs across scopes), then `ok`. No new W-code.
5. Frozen census in CORPUS.md at HEAD (E9): rows 31; malformed 0; tier A=30 C=1; status mined=22 queued=8 rejected=1; duplicate ids none; enum violations none; mined used-by missing none. Every command exit 0.

## Findings

F1 — LOW-MODERATE, calibration. S031 `teaches` says Copilot CLI documents "a `disabledSkills` settings key". Its cited page, cli-command-reference.md (E12, E13), has no `disabledSkills` text: exact and case-insensitive searches find none, and no line pairs "disabled" with a skill term. `disabledSkills` appears on the Copilot SDK page (S030 lines 187, 288, 697), not this one. The S031 Gate quote (line 1300) is the `ignoredSkillsLocations` sentence, and the entry table row 21 uses that quote, so the C2 counted lever is not affected by this clause. Fix: a superseding row per contract rule 2, or an in-round amendment if the L1 allows one.

F2 — LOW, entry text. `corpus/knowledge/skill-overlap-levers-round51.md` lines 29–31 (the uncounted "Other levers" paragraph) place Copilot CLI's `disabledSkills` "in the config directory reference" (E14). That page has no S-row and no Gate quote, and the S031 page contains no "config directory" text (count 0). Not shown false, but unsourced. Fix: cite a row for that page or drop the clause.

F3 — LOW, contract rule 5. The `## Search log` section has five entries (E15): 2026-10-19 ×3, 2026-10-21, and 2026-10-22 round-48. None covers rounds 49, 50 or 51. The round-51 lever search (seven clients, rejected candidates with reasons in the lesson's Gate) has no note; its sweeps sit in seat reports. Fix: add one prose note (question, where searched, date, counts, exclusions, stop rationale). That is an append, not a row edit.

F4 — INFO, used-by true in substance. S030's used-by path `corpus/knowledge/skill-selection-rules-round50.md` cites the Copilot SDK page by name and line (`SDK skills.md:685`, file line 77), not by id or URL (E10: `git grep` count 0 for S030). The lesson's statement that the file "already cites the page" holds. A machine check on row ids would miss it; no change required.

F5 — INFO, freshness and negative claim pass for the two new rows. Re-opened today (E12): both HTTP 200 and byte-identical to the Gate hashes; quotes verbatim at the stated lines. The S030 negative claim ("no rule for choosing between two skills whose descriptions both match") holds on a sweep of the SDK page (E16): overlap 1, conflict 3, multiple skills 1, precedence 0, tie-break 0, ambig 0, prioriti 0. Every hit is in the remedy list at lines 805–810 (remove or reorganize), not an arbitration rule.

F6 — INFO, scope boundary. At check time the lane working tree had uncommitted changes to `PROVINCE.md`, `SCORECARD.md`, `corpus/README.md`, plus untracked `.ufo/waves/round-51/` (E8). Those three files also changed at HEAD (BASE..HEAD stat), so working tree and HEAD differ for them. I did not compare their contents; the L1 should confirm which copy is landed for the D2, D3 and D5 items.

F7 — INFO, credential scan (E11). Seven added diff lines; two pattern hits, both false positives: `skills.max_context_tokens` (S021) and `SessionConfig` (S030). No credential material, session URL or `op://` reference.

F8 — INFO. The lesson logs S022, S024, S025 and S029 used-by changes as "the same plus `, corpus/knowledge/skill-overlap-levers-round51.md`" instead of full strings. The old and new values are both recoverable from the diff, so I read it as logged.

## Residual risk and gaps

- The C2 counter (`check_overlap_levers.py`) was not run here; that is another seat's slice. F1 does not change its key term.
- Live re-opens covered S030 and S031 only. S021, S022, S024, S025 and S029 were not re-fetched by this seat; the lesson records an L1 re-fetch at 15:08Z.
- The `disabledSkills` location in F2 was not fetched, so F2 is an unsourced claim, not a shown error.
- Warning codes never change exit status (script contract). "Clean" here means no E-code plus the same three W04 lines.
- The fleet-root validate (E1) used UTC today, 2026-10-22, because no `--today` was passed; the scratch runs (E3, E4) passed `--today 2026-10-22`.

## Evidence (commands and exit codes)

- E1 `scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kotoba` → `kotoba W04 S018 …`, `kotoba W04 S019 …`, `kotoba W04 S021 …`, `kotoba ok …/corpus/SOURCES.md`; EXIT=0.
- E2 `git diff 43ca0bfb74372f2a67a48e0aeb2e35d0d98b1d10 59903b2637689739a5b9901956301da72d0effe1 -- corpus/SOURCES.md` → 1 file, 7 insertions, 5 deletions; EXIT=0.
- E3 validate on the scratch clone checked out at BASE → same three W04 + `lane ok`; EXIT=0.
- E4 validate on the scratch clone checked out at HEAD → same; VALIDATE_EXIT=0.
- E5 `scripts/sources-census.sh overdue --root /home/vgpnk/Projects/shokunin kotoba` → cadence lines for all 31 rows, including `S030 recheck=90d opened=2026-10-22` and `S031 …`; EXIT=0.
- E6 `… shared --root /home/vgpnk/Projects/shokunin | grep -Ei 'copilot-sdk/features/skills|cli-command-reference'` → no output; grep exit 1.
- E7 Python cell parse of `git show <rev>:corpus/SOURCES.md` for BASE and HEAD: rows 29 → 31; changed cell index [10] only on S021, S022, S024, S025, S029; S030 and S031 have 11 cells, opened 2026-10-22, recheck 90d, status mined, kind docs, tier A.
- E8 lane `git log -1` → `59903b2637689739a5b9901956301da72d0effe1 2026-10-22T12:12:02-03:00`; `git status --porcelain` → `M PROVINCE.md`, `M SCORECARD.md`, `M corpus/README.md`, `?? .ufo/waves/round-51/` (4 lines; wc exit 0).
- E9 frozen CORPUS.md census commands in the scratch HEAD clone: rows 31; malformed NF!=13 → 0; tier A=30 C=1; status mined=22 queued=8 rejected=1; duplicate ids none; enum violations none; used-by missing none; each rc 0.
- E10 `git grep -c` at HEAD for each used-by path: each names its row id except S030 ↔ `skill-selection-rules-round50.md` (rc 1; cited by name, F4).
- E11 credential scan over the 7 added diff lines: 2 hits (`token` in `skills.max_context_tokens`; `Session` in `SessionConfig`); both false positives.
- E12 `curl -sS -L --max-time 120 -o <scratch>/S030.fetch -w …` and the same for S031: each exit 0, HTTP 200 (see Web sources).
- E13 quote search on fetched bytes: S030 "Use `disabledSkills` to exclude conflicting skills" at line 809; "Reorganize skill directories to avoid overlaps" at 810; S031 "Use the `ignoredSkillsLocations` setting…" at 1300; "first found wins for duplicate names" at 1282; `disable-model-invocation` at 1278; `copilot skill disable` at 1324; `disabledSkills` NOT FOUND (exact and case-insensitive).
- E14 `git show 59903b26:corpus/knowledge/skill-overlap-levers-round51.md` lines 20–31 read (row 21 counted quote; lines 29–31 uncounted paragraph).
- E15 `## Search log` section of SOURCES.md at HEAD: five entries; latest 2026-10-22 round-48.
- E16 sweep of the fetched SDK page for overlap, ambig, tie-break, precedence, prioriti, conflict, multiple skills, both match, which skill: counts as in F5.

## Web sources (plain fetch; no challenge encountered)

- S030 — https://docs.github.com/en/copilot/how-tos/copilot-sdk/features/skills.md — accessed 2026-10-22T15:22:41Z; HTTP 200; 35,455 B; sha256 `64856ff44e5481f3ccb16defbc80180874e463862ac12309ef23b18802d4b9f3` (matches Gate). Quotes: "Use `disabledSkills` to exclude conflicting skills" (line 809); "Reorganize skill directories to avoid overlaps" (line 810).
- S031 — https://docs.github.com/en/copilot/reference/copilot-cli-reference/cli-command-reference.md — accessed 2026-10-22T15:22:42Z; HTTP 200; 461,944 B; sha256 `c61997efd7c939324e1f1b846fcb9ed420e5bbfd5eb5319531c6e6210025b5c9` (matches Gate). Quotes: "Use the `ignoredSkillsLocations` setting to exclude specific directories (and their descendants) from discovery, regardless of which location above would otherwise surface them." (line 1300, 22 words); "Skills are loaded from these locations in priority order (first found wins for duplicate names)." (line 1282).

## Tools

None installed or updated. Used the existing git, awk, python3 (subprocess) and curl.
