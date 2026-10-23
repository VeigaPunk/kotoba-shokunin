Result: DONE — S065’s W04 is shared with S053; merging their scopes would violate the append-only protected-cell rule, so report it without changing SOURCES.md.

## Finding

The other row with the same census URL is **S053**: its source cell is `https://code.claude.com/docs/en/skills.md` and its scope is Claude Code’s skill-description listing limits (`corpus/SOURCES.md:66`). S065 cites that identical URL, but for direct user-typed invocation (`corpus/SOURCES.md:78`). These are distinct scopes, so the W04 is expected. S022 is not another match for this census key: its source URL ends `/skills` (without `.md`); the parser retains the path suffix (`corpus/SOURCES.md:35`; `scripts/sources-census.sh:600-605`).

## Evidence and gate interpretation

- Existing Round-56 receipt: `.ufo/waves/round-56/census-start.txt:1-11` records `kotoba\tW04\tS065 duplicate url code.claude.com/docs/en/skills.md across scopes`, `kotoba\tok`, `exit 0`, and `rows 71`.
- Recorded command/outcome (not rerun): `scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kotoba` → `kotoba ok`, exit 0, 7 × W04 including S065 (`corpus/lessons/round-55-verifier-spotcheck.md:34`). The census script calls W04 a warning that does not affect clean-lane status (`scripts/sources-census.sh:31-33`). Its `url_of` drops scheme/fragment/trailing slash, lowercases the host, and retains the path (`:600-605`); W04 is emitted when a URL is already seen under a different scope (`:643-645`), independently of row status.
- The canonical contract permits in-place edits only to `status`, `recheck`, and `used-by`; a correction is a new row whose `teaches` starts `supersedes S0NN —` (`/home/vgpnk/Projects/shokunin/CORPUS.md:116-118`). `check_sources_append_only.py` defines all other cells as protected and row removal as a breach (`verifiers/check_sources_append_only.py:5-18`); its comparator reports changes to non-permitted columns and deleted rows as breaches (`:67-80`). Thus `scope` is protected.
- **[INFERENCE]** A scope merge requires changing a protected `scope` cell or removing a row, neither allowed under the current contract. Appending a superseding row or changing an allowed cell does not erase the existing S053/S065 cross-scope pair; W04 is evaluated from URL and scope without a status or supersedes exception. Recommend **report-only** for defect 6; no legitimate append-only remedy clears this warning.
- No census or append-only checker was rerun for this report. No source or lesson row was changed.

## Draft report line

`6. Census W04 S065 is shared with S053: both source cells name https://code.claude.com/docs/en/skills.md, but the scopes differ (skill-listing limits vs direct invocation). A scope merge would alter a protected cell under CORPUS.md § SOURCES.md rule 2; reported without changing SOURCES.md.`

## Draft lesson § Gate “Rows touched” note

`Rows touched: none. S065 shares the .md URL with S053 across distinct scopes; the append-only rule protects scope, so this W04 is reported without a SOURCES.md edit.`

## Surfaces, scope, and provenance

- Finding sources read: `.ufo/waves/round-56/census-start.txt:1-11`; `corpus/SOURCES.md:35,66,78`; `scripts/sources-census.sh:31-33,600-605,643-649`; `/home/vgpnk/Projects/shokunin/CORPUS.md:110-118`; `verifiers/check_sources_append_only.py:3-19,64-80`.
- Touched surface: this report only, `.ufo/waves/round-56/build/ScribeS065.md`.
- Out of scope: modifying SOURCES.md, changing either scope/status, appending a supersedes row, or changing the census/checker/contract. No tools installed or updated.
