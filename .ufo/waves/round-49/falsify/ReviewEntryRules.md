# Falsify review — sibling-overlap-census-round49.md vs QUALITY Q12/Q13/Q14/Q23 (seat ReviewEntryRules)

VERDICT: HOLDS-BOUNDED — for `corpus/knowledge/sibling-overlap-census-round49.md` at judged bytes
`c48793dbe5eb30cd661f42ecad7399ae94e3d7ad`: the Q12 header verifies and its recheck runs with the
claimed output; all five § Counts commands reproduce exactly as written; every located quote and every
negative sweep I re-ran reproduces at the pinned source bytes; all 20 rows verify independently at
their pins (quotes verbatim, mechanical columns recomputed). Bounded by one substantive defect: two
judged `none` rows contradict the entry's own classification rule (F1), which makes the § Counts line
"7 adjacent, 13 none" wrong as a rule-following measure (the lane's own post-judgment commit `bfd5a58`
concedes exactly this, "kake/kasegi adjacent 9/11").

Note on bytes: the lane working tree moved during review (master `2272019`, HEAD `bfd5a583`; the census
file itself changed mid-session). All judged-bytes results below come from a private clone checked out
at `c48793d` (`/fast/scratch/hyaku/kotoba-r49/falsify/ReviewEntryRules/judged`), per bounds. Earlier
working-tree observations were discarded, not reported.

## Findings

**F1 (major — C1 classification rule vs rows, judged bytes).** The rule says `adjacent` = "either
side's committed scope surfaces (SKILL.md, PROVINCE.md, corpus files) state a split of one artifact,
function or trigger area between the sibling and kotoba". kotoba's own committed SKILL.md description
(at `a5adc146`, unchanged at `c48793d`; drift guard) states that split for five lanes: "the five
`*-shokunin` domain skills (kagi, kake, kasegi, kengaku, kumitate) own their own SKILL.md content —
this skill audits and reports; fixes route to the owning lane". Under the rule as written, `kake` and
`kasegi` must be `adjacent`; the judged rows say `none` (both mechanical cells "no/no" are factually
correct — their pinned descriptions contain no `kotoba` token, verified). Only a sibling-side-only
reading rescues them, but that reading is not what the rule text says and it breaks other rows (F2).
`bfd5a58` (post-judgment) flips both rows to `adjacent` and re-titles the count 9/11 — the lane itself
has already conceded F1; it is recorded here because the judged bytes are what this wave attacks.
Consequence: judged § Counts "7 adjacent, 13 none, 0 contested" reproduces against the table but not
against the rule; PROVINCE.md § Adjacent kake/kasegi rows inherit the same defect at `c48793d`.

**F2 (minor — rule scope/circularity).** `tameshi`'s adjacent warrant (PROVINCE.md § Adjacent boundary
cell) cites `tameshi .ufo/waves/round-16/w1/Overlap1.md:136` — a wave report, outside the rule's
enumerated surface list (SKILL.md, PROVINCE.md, corpus files). tameshi's own PROVINCE.md at pin
`3b20f073` contains no kotoba split (grep `kotoba|prompt` → only incidental checklist mentions at
:32,:70-71), and kotoba's description does not name tameshi. tameshi qualifies only via kotoba's own
§ Adjacent row — which makes "either side's surfaces" circular wherever § Adjacent itself is the
stating surface. chousa is unaffected (kotoba `corpus/QUALITY.md` header names chousa as the research
method — a corpus file, in-list).

**F3 (minor — S022 provenance, Q14/Q23 hygiene).** Seat `SrcClaudeCodeSkills.md` records the HTML
receipt (HTTP 200, 1,233,129 B, sha256 `10219534…`) in its Evidence lines alongside measurements that
hold only on the markdown export: `wc -l → 1,234` is false for the HTML (2,297 lines) and exact for
the export. The SOURCES row S022 (judged bytes) resolves this correctly — its canonical fetch is the
`.md` export ("fetched as .../skills.md (200, 111557 B, sha256 `cdfcb0df…`)"), so the entry's anchors
and sweeps do verify (see evidence). But on the HTML bytes named in the same row ("serves the same
prose and did not redirect"), `grep -ciE 'overlap'` → 2 (not 0; one prose line about markup rules, one
JS payload) and `skills.md:389/196-198/1190-1195` resolve to CSS/JS. The HTML side was never swept.
The negative claim's substance survives (neither HTML hit is a tie-break rule; both quoted texts do
appear in the HTML, 2 hits each), so this is a representation-provenance gap, not a false absence.

**F4 (minor — Q13 format).** Each § Counts line carries `<number> — <command>` but the date appears
once in the section header ("§ Counts (each with its command, 2026-10-22)"), not per line. Q13's
format is `<number> — <command> <date>`. All commands do run and match, so this is format, not
fabrication.

**F5 (observation — none-row machinery at judged bytes).** The judged guard checked quotes/commits/
province join only; it did not re-derive the mechanical columns nor enforce the sibling-side `none`
condition (both added post-judgment in `bfd5a58`). My independent recomputation shows the judged
mechanical cells are nevertheless correct on all 20 rows, and the 13 `none` rows' sibling-side surfaces
(PROVINCE.md + SKILL.md at pins) contain zero `kotoba` tokens — except `tabi`: 2 hits, both the
`LANES="protocol aggregator kasegi kengaku kake kumitate kotoba kagi kama"` list (`SKILL.md:1313,
:1450`; PROVINCE.md 0). That mention is disclosed in the cited seat `ConnectSiblingOverlap.md` as
incidental ("not scope claims"); a bare list is not a "stated split" under the rule, so `none` stands,
but it is the one live token a stricter none-side guard would have to adjudicate.

## What holds (all at judged bytes unless stated)

- Q12: header opens `source:` naming S018/S022/S023 with URLs + § anchors (rows exist in
  `corpus/SOURCES.md`, lines 31/35/36), `verified-at: 2026-10-22`, and the `recheck:` runs exactly:
  `python3 -B verifiers/check_sibling_census.py corpus/knowledge/sibling-overlap-census-round49.md
  --province PROVINCE.md` → `rows 20 verified 20`, `province rows 20 matched 20`, exit 0.
- Q13: all five § Counts commands, run verbatim (`F` = the census file, from the clone root): 20 (exit
  0); 7 adjacent / 13 none (adjacent set = chousa, kagi, kama, kengaku, kotodama, kumitate, tameshi ✓);
  17 SKILL.md / 3 NONE; 2; 8. The `-F' \\| '` form is the correct one on this host's gawk — the
  single-backslash variant is what breaks (warning "escape sequence `\|' treated as plain `|'",
  fields misalign), so the entry's commands are the right ones, not the reverse. Prose numbers
  recompute from the judged table: 17 directed pairs across 8 descriptions (kotoba excluded:
  2+2+4+2+2+3+1+1) ✓; same-five-lanes arbitration 1/5 (kengaku) ✓; only reciprocal description pair
  chousa↔kengaku ✓.
- Q14: every negative claim located in the entry carries its sweep, and each reproduces: S022 four
  patterns → 0/0/0/0 and `conflict` → 1 at :49 on the pinned `.md` bytes; S023 nine patterns → 0 each
  (byte-identical refetch, sha `7913d455…`); S018 combined grep → 0, exit 1, over 7,608 B,
  sha `9a67de89…` reproduced; "0 contested" carried by the cmd2 output; kasegi negatives reproduced
  (`git grep -qiE 'prompt[- ]injection' 1fafde8f` exit 1; `git log -S` prompt/injection on PROVINCE.md
  → 0 commits); kotoba description lacks kotodama (`sed -n 1,16p SKILL.md | grep -c kotodama` → 0 at
  `a5adc146` and `c48793d`); "no lane SKILL.md in ten discovery roots" sweep present in
  `CriticC1Sizing.md` (with honest [INFERENCE] marker); "no SKILL.md at pin" verified 3/3.
- Q23: located quotes resolve at the pinned source bytes: S023 `overview.md:59` (both quoted sentences,
  one line), S018 `specification.md:102`, S022 `skills.md:389`, `:196-198` (name-clash rule),
  `:1190-1195` (troubleshooting) — all verbatim on the row's pinned `.md` fetch, which I reproduced
  byte-identically (sha `cdfcb0df…`). Per-row scope quotes: 20/20 found verbatim (whitespace-collapsed)
  at the stated `path:line` ±2 by my own script against `git show <pin>:<path>` (9 rows are folded
  multi-line spans whose stated line is the span's first line). Adjacency warrants verified verbatim:
  kagi `corpus/README.md:97` ("kagi pins its bytes; kotoba owns the checklist/shape reading"), kama
  `cross-lane-scope.md:29` ("**Kotoba** owns the instruction/agent surface …; **kama** owns
  independent verification"), kengaku/kotodama descriptions name kotoba (token match), kumitate
  PROVINCE cession per `CriticC1Sizing` sweep.
- Rows: mechanical columns ("names kotoba", "arbitration") recomputed from pinned frontmatter with a
  whole-token predicate — 0 mismatches on 20 rows (script:
  `/fast/scratch/hyaku/kotoba-r49/falsify/ReviewEntryRules/verify_rows.py`, exit 0).

## Residual risk and verification gaps

- I did not re-run each of the 13 `none`-row seat sweeps (`.ufo/waves/round-49/build/Census<Lane>.md`,
  all 20 present); beyond the token sweep above, their classifications rest on the seats' reading.
- The round-7 supersession figures (`alwayson-checklist-round7.md:56-57`, "1/5") were checked for
  internal consistency only, not against the round-7 bytes.
- F3's HTML-side sweeps were run once today; the HTML is editorially unstable (round-48 fetch of the
  same route differed), so its counts are session-local.
- Bounds compliance: lane untouched except this report; sibling access read-only (`show`/`grep`/`log`);
  private clone used for all judged-bytes runs. No tools installed or upgraded (none needed). Fetch
  receipts: code.claude.com/docs/en/skills.md (111,557 B, sha256 `cdfcb0df…`),
  .../skills HTML (1,233,129 B, sha256 `10219534…`), platform.claude.com .../overview.md (21,840 B,
  sha256 `7913d455…`), agentskills.io/specification.md (7,608 B, sha256 `9a67de89…`); all HTTP 200,
  fetched 2026-10-22 (`.md` set at 11:34:53Z, HTML minutes later), no challenge encountered; fetched
  bytes only grepped, never executed.
