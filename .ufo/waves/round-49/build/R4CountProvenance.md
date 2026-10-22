# R4CountProvenance — Q13 count provenance for the round-48 frontmatter entry

Seat `KotobaR49.R4CountProvenance`, leaf, 2026-10-22. Surface:
`corpus/knowledge/frontmatter-rule-authorities-round48.md` at lane HEAD `a5adc14`
(working tree = HEAD; sha256 `75d6403eea24ac0c19fbf4dc31333a0efb84d8fcb2344f2102dd633d0f52827e`,
`git -C <lane> status --porcelain` on the file → 0 lines). Nothing in the entry was edited;
the section below is a draft for the integrator. All observations 2026-10-22T09:41:18Z –
09:56:57Z; the re-run transcript is `/fast/scratch/hyaku/kotoba-r49/seats/R4CountProvenance/transcript.txt`
(sha256 `6b36f3758bc0…`).

## Findings

1. **23 numeric claims; 21 reproduce, 2 do not.**
   - **F1 (defect, LOW) — line 56's printed sweep cannot produce its 0.** The printed
     `grep -niE -e 'third person' -e 'reserved' -e 'max_lines' -e 'line_count' -e '500' validator.py parser.py models.py`
     returns **1 hit, exit 0** (`validator.py:12:MAX_COMPATIBILITY_LENGTH = 500`); the seat's recorded
     sweep (`max_lines|body length|500 line|line_count`, `C2EntryScaffoldScribe.md`) returns 0, exit 1,
     reproduced. The cell's claim ("body length not stated") holds — the hit is a compatibility cap —
     but the printed command does not produce the printed number. Repair: print the executed pattern.
   - **F2 (unprovenanced, LOW) — line 32's "24 probe fixtures" has no producing command or run list.**
     The seat scratch holds 36 `SKILL.md` fixtures in 36 `probes*` directories, 33 distinct fixture
     names, 29 distinct contents (`counts.py`). No reading yields 24; not contradicted, not reproducible.
2. **Zero counts missing only their date (Q13):** line 51's first Codex sweep (`→ 0 hits, exit 1`) and
   line 54's two packager sweeps (`→ 0`; `→ 0 rule lines`) print the command but no date. All three
   reproduce today (0 hits, exit 1 each).
3. **Sizes and the diff count are exact.** 7,608 B / `9a67de89…` and 42,169 B / `f0a5d61b…` re-fetched
   identically; 42,028 B / `727f3fa1…` matches the retained round-47 copy, which is also byte-identical
   to today's spec bytes. "62 in-place copy edits" reproduces as 62 `c`, 0 `d`, 79/79 lines (A02's
   "32 hunks" is the 3-line-context count — different, also true).
4. **6 / 7 / 3 re-derived from fresh runs**, not copied from `results.json`: ten lane CLI + ten `qv.py`
   runs give 6/10 (angle rule), 7/10 (file verdict), 3/10 (docs tag rule); arithmetic in `s_div.py`
   (`94b1fe8b…`). A07's qualifications stand: f02b and f04 are emulated; 3/10 rests on the shape reading.
5. **Every threshold observation reproduces** on fixtures built today: 65-char name → packager 1,
   skills-ref 1, lane frontmatter 0; 1025 desc → 1/1/0; padded 1024 → 0/0; 501 `compatibility` → 1/1;
   empty → 0/0; lane budget 505 → 0, 605 → 1 ("605 lines exceed budget 600"); allowed keys = 6.
6. **Structural counts hold:** ten rule rows; `O1`–`O6` six classes; 5 of 6 S016–S021 rows carry
   `https:` (S020 own work); "256-character" hits `errors.md:5388` and `:5397` on a 541,573 B fetch
   (`37e9799a…`, the hash the entry's table already records).
7. **Already compliant, re-run:** the four rechecks (lines 125–128) → 1, 1, 2, 1, so line 122's
   "1 or 2" is exact; (c)'s `third person` and `reserved` sweeps → 0 and its `unknown|unrecognized`
   sweep → exactly `spec.md:161` (the `angle|xml|[<>]` sweep returns 97 markup lines and no rule
   sentence — qualitative, no count claimed); (e)'s two sweeps → 0, exit 1; RFC 2119 → 0, exit 1.

## Draft appended section (append-only; do not reword the entry above it)

```markdown
## Count provenance (round 49, routed defect R4)

Every count and size above is re-measured here with its command (2026-10-22, UTC). Table cells avoid
`|` so each command is copy-paste runnable: alternations use repeated `-e`, row-id counts build the
separator with `chr(124)` (the A15 literal-pipe hazard).

| line | stated value | command | observed today (UTC) | match |
|---|---|---|---|---|
| 16 | 7,608 B | `curl -sSL -o spec.md -w '%{size_download}\n' https://agentskills.io/specification.md` (then `sha256sum spec.md`) | 7,608 B, `9a67de89…`, 2026-10-22T09:48:10Z | yes |
| 22 | 21 fixtures | `python3 -c "import glob;print(len(glob.glob('/fast/scratch/hyaku/kotoba-r48-a2/seats/C2SkillsRefRun/fixtures/*/')))"` | 21, 09:48:11Z (seat F3: 21 skill directories plus the lane copy) | yes |
| 23 | 42,169 B | `curl -sSL -o bp.md -w '%{size_download}\n' https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices.md` | 42,169 B, `f0a5d61b…`, 09:48:10Z | yes |
| 24 | 42,028 B (round 47) | `wc -c` and `sha256sum` on `.ufo/waves/round-47/build/KnowDescriptionRule.s003-best-practices.md` | 42,028 B, `727f3fa1…`, 09:48:11Z (retained copy; the live URL has moved) | yes |
| 24 | 62 in-place copy edits | `grep -cE '^[0-9]+(,[0-9]+)?c' <(diff .ufo/waves/round-47/build/KnowDescriptionRule.s003-best-practices.md bp.md)` | 62 `c`, 0 `d`, 79/79 lines, 09:48:11Z | yes |
| 32 | 24 probe fixtures | no stored run list; `python3 -B /fast/scratch/hyaku/kotoba-r49/seats/R4CountProvenance/counts.py` (prints the fixture tree's counts) | 36 fixtures, 33 distinct names, 29 distinct contents, 09:48:11Z | **no — 24 not reproducible** |
| 33, 72 | 10 fixtures | `python3 -c "import glob;print(len(glob.glob('/fast/scratch/hyaku/kotoba-r48-a2/seats2/A07LaneDivergence/fixtures/*/')))"`, then ten lane CLI runs and ten `qv.py` runs | 10 (A07's set equals the build seat's, `diff -r` exit 0) | yes |
| 72 | 6 of 10 (packager description-angle rule) | `python3 -B /fast/scratch/hyaku/kotoba-r49/seats/R4CountProvenance/s_div.py` (re-runs the ten pairs) | 6, 09:48:41Z (f02b and f04 emulated) | yes |
| 73 | 7 of 10 (packager whole-file verdict) | same command | 7, 09:48:41Z | yes |
| 74 | 3 of 10 (docs tag rule) | same command (stdlib `HTMLParser` shape) | 3, 09:48:41Z | yes |
| 51 | 0 hits, exit 1 (Codex sweep) | `grep -niE -e 'reserved' -e 'third person' -e 'xml' -e 'angle' -e '500 lines' -e '1024' -e '1,024' -e '64 char' -e 'lowercase' -e 'hyphen' -e 'consecutive' build-skills.md` | 0 lines, exit 1, 09:48:11Z | yes (date was missing) |
| 51 | 5 hits (widened sweep) | `grep -niE -e 'director' -e 'unknown' -e 'unexpected' -e 'additional field' build-skills.md` | 5 hits at md:11, 39, 48, 138, 142, 09:48:11Z | yes |
| 54 | → 0; → 0 rule lines | `grep -nE -e 'dirname' -e 'basename' -e 'parent' qv.py`; `grep -niE -e 'third person' -e 'reserved' -e 'lines' qv.py` | 0 / exit 1; 0 / exit 1, 09:48:11Z | yes (dates were missing) |
| 56 | → 0 (skills-ref sweep) | the printed pattern gives `validator.py:12:MAX_COMPATIBILITY_LENGTH = 500`; the seat's recorded pattern `grep -niE -e 'max_lines' -e 'body length' -e '500 line' -e 'line_count' validator.py parser.py models.py` gives 0, exit 1 | 1 hit from the printed command, 0 from the executed one, 09:48:11Z | **no — printed command cannot produce 0** |
| 40 | 65 chars fails | `python3 -B qv.py fx/n65`; `agentskills validate fx/n65`; lane `--check trigger.frontmatter_parses` | exit 1 ("Name is too long (65 characters). Maximum is 64 characters."); exit 1; lane exit 0, 09:48:12Z | yes |
| 44 | 1025 fails; padded 1,024 passes | `python3 -B qv.py fx/d1025` and `fx/d1024pad`; `agentskills validate` on both | 1025: 1 / 1, lane 0; padded: 0 / 0, 09:48:12Z | yes |
| 48 | allowed set of six | `python3 -B qv.py fx/badkey` (message lists the allowed set) | six names: allowed-tools, compatibility, description, license, metadata, name; exit 1, 09:56:57Z | yes |
| 49 | 600 budget; 605 FAIL, 505 PASS | lane `--check trigger.line_budget` on 505-line and 605-line fixtures | 505 → exit 0; 605 → exit 1 ("605 lines exceed budget 600"), 09:48:12Z | yes |
| 90 | ten rules | `grep -cP '^\x7c [a-z]' <(sed -n '40,49p' corpus/knowledge/frontmatter-rule-authorities-round48.md)` | 10 (A07's set equals the build seat's, `diff -r` exit 0) | yes |
| 100 | six rule classes | `grep -c '^\*\*O[0-9]' .ufo/waves/round-48/falsify/A12OmittedRules.md` | 6 (O1–O6), 09:48:11Z | yes |
| 102 | 501 fails both; empty passes both | `python3 -B qv.py fx/compat501` and `fx/compat-empty`; `agentskills validate` on both | 1 / 1; 0 / 0, 09:48:12Z | yes |
| 122 | Five of the six sources | `python3 -c "c=chr(124);ids={'S016','S017','S018','S019','S020','S021'};print(sum(1 for l in open('corpus/SOURCES.md') if l[0]==c and l[2:6] in ids and 'https:' in l))"` | 5 of 6 rows (S020 own work), 09:48:11Z | yes |
| 133 | 256-character name refusal | `curl -sSL -o errors.md -w '%{size_download}\n' https://code.claude.com/docs/en/errors.md` then `grep -n 'over 256 characters' errors.md` | 541,573 B, `37e9799a…`, hits at :5388 and :5397, 09:48:11Z | yes |

Disposition: 21 of 23 reproduce. Line 56 needs its printed pattern replaced by the executed one
(`max_lines`, `body length`, `500 line`, `line_count`); line 32's 24 needs either the run list or the
measured fixture count (36 built, 29 distinct). The cells those counts support are unaffected.

Fixture-based rows (40, 44, 48, 49, 102) ran on fixtures built this round in
`/fast/scratch/hyaku/kotoba-r49/seats/R4CountProvenance/fx/`; the ten divergence fixtures are A07's
persisted set, and `s_div.py` re-runs both tools rather than reading `results.json`. Rows 24, 51, 54
and 56 ran in that same scratch directory, where the fetched sources (`spec.md`, `bp.md`, `qv.py`,
`validator.py`, `parser.py`, `models.py`, `build-skills.md`) sit; each is re-fetchable from the URL in
the `source:` line or the Limits rechecks.
```

## Draft erratum line for the round-49 lesson `## Gate` (admit line for the round-48 entry)

> **Round-48 knowledge entry — admit line (round-49 erratum, routed defect R4):** candidates **1**,
> admitted **1** (`corpus/knowledge/frontmatter-rule-authorities-round48.md`, sha256 `75d6403e…` at
> `a5adc14`), rejected **0**. Derived from `plans/round-48.md:42` (one entry declared) and
> `:51-52` (34 → 35), re-measured today as `ls corpus/knowledge/*.md | wc -l` → 35
> (2026-10-22T09:47:42Z). Sweep for a second candidate: `grep -rniE 'second (knowledge )?entry|another entry|new entry candidate' .ufo/waves/round-48/{build,falsify}/*.md` → 0 hits, exit 1; the 14 mentions of "knowledge entry" all describe this one entry. The round-48 Gate carries the source-row ledger (6 admitted, 5 rejected as rows) but no entry-level candidate/admitted/rejected line, which `CORPUS.md:19-20` names as part of the Gate's required content.

## Classified out of scope (not Q13 counts)

- **Quoted thresholds** carry an authority line cite instead of a command: `1-64` (spec.md:63),
  `1-1024` / `1,024` (spec.md:101, bp.md:160), `500` (spec.md:237, bp.md:257), `1-500`
  (spec.md:33, :134), `600` (the lane's own box, SKILL.md:246), `a-z`/`0-9`. These are citations of
  source text, located; the entry's own *observations* about them are tabled above.
- **Coordinates, not counts:** `spec.md:30,63,64,66,67,101,161,237`, `bp.md:153-156,160-162,206,257`,
  `validator.py:10,11,37,51-52,54,60-65,104-113`, `qv.py:42-49,65,67,70-71,77-84`, commit `75f671b`,
  tag `0.1.1`, and line ranges `257-259`, `1131-1150`.
- **Quoted lane output** "description 2 chars" (line 87) is the lane's detail string, not a measurement.

## Evidence (commands, exit codes, hashes, UTC)

- Transcript `bash run-provenance.sh > transcript.txt` exit 0, 09:48:10–09:48:12Z; sha256:
  transcript `6b36f3758bc0…`, run-provenance `1747561c91da…`, s_div.py `94b1fe8b3351…`,
  s_div.out `b57bb8deff9a…`, counts.py `29b26ed3c3ba…` (prints 5 / 10 / 36 / 29, exit 0).
- Fetches (all HTTP 200, size via `-w '%{size_download}'`): specification.md 7,608 B `9a67de891329`;
  best-practices.md 42,169 B `f0a5d61b6712`; overview.md 21,840 B `7913d4556c01`;
  validator.py@69ef37e9 5,154 B `b5ee3d8537c8`; parser.py 3,413 B `9a74c9a90eb2`; models.py 1,461 B
  `c6645fcfc04c`; quick_validate.py@dbd4588 3,972 B `67cf57034020`; build-skills.md 11,035 B
  `ed6e324f747d` (these six at 09:41:18Z); errors.md 541,573 B `37e9799a4467` (09:48:11Z).
- Rechecks re-run: `grep -c 'Must match the parent directory name' spec.md` → 1, exit 0;
  `grep -c 'MAX_DESCRIPTION_LENGTH = 1024' validator.py` → 1; `grep -c 'Description cannot contain
  angle brackets (< or >)' qv.py` → 1; `grep -c 'Cannot contain XML tags' bp.md` → 2;
  `grep -c 'must include \`name\` and \`description\`' build-skills.md` → 1. All exit 0.
- Sweep exits (direct, without a counting pipe): Codex first sweep exit 1; `dirname|basename|parent`
  on qv.py exit 1; `third person|reserved|lines` on qv.py exit 1; RFC 2119 sweep
  `grep -cwE 'MUST|MUST NOT|…' spec.md` → 0, exit 1; seat's body-length pattern exit 1; entry-literal
  pattern exit 0 (the one hit above).
- Behavior fixtures and exits: `qv.py`/`agentskills` on n65 1/1, d1025 1/1, d1024pad 0/0,
  compat501 1/1, compat-empty 0/0; lane `trigger.line_budget` 505 → 0, 605 → 1; lane
  `trigger.frontmatter_parses` n65 → 0, d1025 → 0.
- Lane reads only: `git -C <lane> rev-parse --short HEAD` → `a5adc14`; `git -C <lane> status
  --porcelain <entry>` → 0 lines; `git -C <lane> show HEAD:<entry>` | sha256sum → `75d6403e…`.
  No git/jj write command ran; the only lane file written is this report.
- Tools installed or upgraded: none.

## Remaining unknowns

1. **What "24 probe fixtures" counted.** The seat scratch holds 36 files / 33 distinct names / 29 distinct
   contents; no run list or manifest exists. A reading of 24 (e.g. the first five `probes*` batches)
   is plausible but unproven.
2. **The 6/7/3 re-derivation depends on A07's scratch fixture tree** (`/fast/scratch/hyaku/kotoba-r48-a2/seats2/A07LaneDivergence`).
   If that tree is pruned, only `results.json` and A07's per-fixture table remain, which are records,
   not a re-run.
3. **The entry's f02b/f04 emulation caveat (A07 D2) and the 3/10 reading caveat (A07 D3)** are not
   stated in the entry's point 4; the counts are correct under A07's stated readings. Recorded, not
   repaired (append-only).
4. Whether line 56's mismatch ever misled a reader: no downstream citation of that sweep's 0 was found
   (`grep -rn 'skills-ref' SKILL.md PROVINCE.md corpus/README.md` → 2 lines, `PROVINCE.md:16` and
   `corpus/README.md:66`, both index pointers carrying no count).
