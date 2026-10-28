# Kb81R08SourcesAudit — SOURCES registry deep-audit (round 81 w1)

Scope: independently re-derive `corpus/SOURCES.md` registry state at base
`b284223105f4d106f7e8f56ed4fd296c643cda0e`, then rule on S230/S231's `mined`
status vs their used-by cells vs their factual anchor state.

Base-pinning: lane `git rev-parse HEAD` = `b284223105f4d106f7e8f56ed4fd296c643cda0e`;
`git status --porcelain` shows only untracked `.ufo/wapes`, `.ufo/waves/round-81/`,
`plans/round-81.md`; `git diff HEAD -- corpus/SOURCES.md` is empty — the working-tree
file IS the base file, so every command below ran on base bytes from the lane root.
No tools installed or upgraded (tooling directive: nothing needed; pacman untouched).

## 1. Frozen census re-derivation (CORPUS.md § SOURCES.md § Census, run from lane root)

| Check | Command (frozen text) | Result at base |
|---|---|---|
| row count | `grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md` | **174** (plan expected ~174 ✓) |
| malformed rows | awk NF!=13 | **0** |
| tier histogram | awk $5 | `A=135 B=22 C=17` |
| status histogram | awk $9 | `mined=149 queued=8 rejected=17` (174 total ✓) |
| duplicate ids | awk $2 \| sort \| uniq -d | **none** (empty output) |
| enum violations / tier-inflation | awk triple-enum arm | **none** (empty output) |
| mined rows whose used-by paths don't exist | awk $12 \| `[ -e ]` loop | **none** (empty output) |

Maintained script (outside frozen v1): `bash /home/vgpnk/Projects/shokunin/scripts/sources-census.sh
validate --root /home/vgpnk/Projects/shokunin kotoba` → **`kotoba ok`, exit 0**, with
**31 W04 warnings** (all `duplicate url … across scopes`; warning class, never failing).
`census` subcommand agrees: rows 174, A=135 B=22 C=17, mined=149 queued=8 rejected=17,
`FLEET missing 0`, exit 0.

W04 list (31): S018, S019, S021, S054, S055, S056, S065, S086, S103, S104, S106, S110,
S111, S114, S115, S118, S207, S208, S212, S213, S227, S229, S230, S231, S234, S235,
S238, S239, S240, S241, S243. For the two rows under review: **S230 pairs with S215**
(same pi-mono skills.md URL, different scope — allowed-tools field vs rung bounds) and
**S231 pairs with S202** (same mistral-vibe README, different scope — allowed-tools
form vs discovery/trust). Both are the accepted same-URL-distinct-scope pattern, not
the supersede mechanism's cost (r48 precedent: W04s from supersedes were ruled
non-failing noise; same class here). r79 spotcheck already recorded S227/S229/S230/S231
as "new duplicates-by-scope" when the count was 24; +7 since (S207/S208/S212/S213/
S234/S235/S238/S239/S240/S241/S243 are r79–r80 additions sharing URLs with earlier rows —
the count is 31 because some URLs appear in 3+ rows). No W04 is an error.

## 2. Beyond the frozen census — deeper findings

The frozen commands check syntax and path existence only. I ran a two-way semantic
sweep (for every `mined` row, does each used-by path actually contain the row id?),
plus shape checks. Findings:

- **F-A — S030 stale used-by path (pre-existing drift).** used-by =
  `corpus/knowledge/skill-overlap-levers-round51.md, corpus/lessons/round-51.md,
  corpus/knowledge/skill-selection-rules-round50.md`. The round50 file exists but has
  never contained `S030` (`git log -S 'S030' -- <file>` empty; its source: line lists
  S019/S022/S024–S029 only). Genuine citations: the round51 knowledge file, the r51
  lesson, `corpus/README.md`, `SKILL.md`. The round50 path was added at commit `34cfffb`
  (round-51), apparently swept in with the sibling rows' block. `mined` still holds
  (≥1 real citing path exists); the extra path is a precision defect invisible to the
  frozen existence check. Repair shape: used-by edit-in-place + old→new lesson log.
- **F-B — S112/S113/S114/S115 used-by claims `SKILL.md` — false.** Each row's used-by =
  `SKILL.md, corpus/lessons/round-61.md`. SKILL.md contains neither `S112`–`S115` id
  tokens nor their URLs (grep for `claude-directory`, `agent-customization/
  custom-instructions`, `add-custom-instructions`, `cursor.com/docs/rules` all 0 hits;
  `git log -S 'S112' -- SKILL.md` empty → never present). `corpus/lessons/round-61.md`
  does cite all four (gate record, lines 14–17). Same class as F-A: semantic used-by
  imprecision, path exists so frozen census passes. (SKILL.md does cite 88 other S-ids
  verbatim; these four are absent.)
- **F-C — `source:` lines citing unregistered ids S262/S263/S264.** In
  `corpus/knowledge/resident-index-and-rungs-round72.md` — resolved: these are
  staged-package snapshot filename prefixes (`S262-factory-droid-skills.md`,
  `S263-pi-skills.md`, `S264-hermes-skills.md`), i.e. quarantined shokuknow ids used as
  file names; the row ids actually cited (S214–S216) exist and are mined. Cosmetic
  ambiguity only — but the id collision it shadows is exactly why merge adoption stays
  closed (r80 lesson § Assimilation).
- **F-D — registry table carries a second header block.** Lines 137–138 repeat
  `| id | source | … | used-by |` + separator mid-table, restarting the table for the
  S198+ continuation after the id gap 129→198. Harmless to every census command
  (none match S-rows); shape note.
- **F-E — `## Leads (unopened)` duplicated.** Real headings at lines 304 and 346;
  the bullet blocks under them are byte-identical (`diff` of 306–320 vs 348–362 →
  IDENTICAL). Additionally, quoted search-log prose at lines 248/251 begins with
  `## Leads (unopened)` at column 0 and renders as headings; search-log entries are
  interleaved inside the first leads block (lines 322–345 sit between the two Leads
  headings). Contract shape §Shape says "one" Leads list; a duplicated section + a
  tangled search log is a real shape defect that every census command is blind to.
  Same verdict class as F-A/F-B: visible only to a structural read.
- **F-F — recheck vocabulary drift.** In use: `90d`, `180d`, `365d`, `on-release`,
  `on-commit` (S009, S010, S017, S020), `—`, ISO dates. Contract text enumerates only
  `90d`, `180d`, `on-release` as cadence examples; `on-commit`/`365d` are house
  extensions accepted by validate (exit 0). Latent contract-vocabulary drift, not an
  error today.
- **F-G — id space.** Rows S001–S248; gaps at 91→93, 115→117, 124→129, 129→198
  (S116 documented unassigned in r61 lesson — "no row is invented" was the correct
  call). Contract: "the next unused; never reused". The r81 plan's S249 (new) and S250
  (S230 supersede) continue the sequential-max convention; backfilling the gaps would
  be contract-legal but has never been house practice.
- **F-H — S248 status/used-by coherence for the r81 plan.** S248 is `queued` with
  used-by `—` — consistent. When C2 lands, its used-by gains
  `corpus/knowledge/allowed-tools-sdk-round81.md`; per contract `mined` = "cited by ≥1
  path in used-by", so the status cell should also move `queued`→`mined` in the same
  row edit (both are in-place-editable cells; log old→new in the lesson). A `queued`
  row carrying a used-by path would be a self-inflicted inconsistency (my sweep would
  flag it). Flagging for the integrator since the plan text names only the used-by move.

## 3. S230/S231 — `mined` status vs used-by vs factual anchor

### used-by cells (measured)

Both rows: status `mined`, used-by `corpus/knowledge/allowed-tools-surfaces-round80.md,
corpus/lessons/round-80.md`. Both files exist (frozen check) AND cite the ids —
`allowed-tools-surfaces-round80.md` carries `source: S230`/`source: S231` provenance
lines plus ~15 further id mentions each; `round-80.md` cites them in its gate record.
**`mined` is factually correct for both rows**: cited by ≥1 path in used-by.

### Factual anchor state (re-derived)

- S230 anchor claims: `` `main` resolved to `badlogic/pi-mono` commit
  `7bb48f213ac677f943d5c791199ed3dddf302f00` ``. **Falsified three ways:**
  1. `git cat-file -e 7bb48f21…` → exit 1 in the lane AND in the fleet root —
     the object is absent from both repos (matches the base gate's
     `commit_unresolvable` 2 at `corpus/SOURCES.md:171-172`; the token appears
     nowhere else in corpus — grep confirms only lines 171 and 172).
  2. The row's own fetch receipt
     `.ufo/waves/round-79/snapshots/S230.fetch.json` records pi-mono's main head at
     fetch time as `bb65e3e49710fbd14f10c7792d0eaa6e2b2c5923` and the last
     path-touching commit as `25cc5c7bf4cbc76b2e134c729eb8d57d521ed749`, with blob
     sha `19d2bf28910ce49caaaf4dde86d1e96330ca7b31` — the row's anchor contradicts
     its own committed receipt.
  3. Live re-derivation this seat, 2026-10-27 (quotable binding evidence for R2):
     `git ls-remote https://github.com/mistralai/mistral-vibe HEAD refs/heads/main`
     → `7bb48f213ac677f943d5c791199ed3dddf302f00` for **both** — the hash is
     verifiably Mistral Vibe's main head, correct for S231.
     `git ls-remote https://github.com/badlogic/pi-mono HEAD refs/heads/main`
     → `a92283056d915c758799fcd904948ff0cb42628c` for both — pi-mono's head has moved
     past even the r79 receipt's `bb65e3e4…`; and `7bb48f21` occurs in **0** of
     pi-mono's advertised refs (`ls-remote | grep -c` → 0; also 0 for `bb65e3e4`,
     i.e. heads only advance, the old head left the ref namespace).
  Diagnosis: single-cell wrong-repository attribution — S230's revision clause was
  filled with S231's resolved hash (both rows authored in the same r79 commit
  `6ef6753`, 2026-10-27T19:20:38-03:00 — committed before the 21:41Z fetch receipts
  were finalized, so the anchor was written before its own receipt could correct it).
- Everything else in S230 is sound: URL serves the bytes (fetch receipt HTTP 200,
  4793 B); snapshot `.ufo/waves/round-79/snapshots/S230-pi.md` sha256 =
  `5b9805525b194474ef1fe5455a0917ef15ed7f710aa9bec2eee11879556469e5` (matches
  `S230.manifest` and re-hashed here); located quote sits verbatim at `S230-pi.md:78`
  (`| `allowed-tools` | Experimental pre-approved tool list |`). S231's anchor is
  fully correct (`served commit` wording — accurate, since the hash IS mistral-vibe's
  head; snapshot `S231-vibe.md` sha256 matches manifest; quote block verified at
  lines 724–728).
- Disclosure state: the misattribution is already honestly disclosed in-corpus —
  `allowed-tools-surfaces-round80.md:21` provenance note, r80 lesson (M80-3), r80
  closure spotcheck R80-D4 and its discernment ruling ("caught by the lane itself").

### What the contract permits

Rule 2 (append-only): only `status`, `recheck`, `used-by` change in place; the
`anchor` cell is not editable — **a correction is a new row whose teaches opens
`supersedes S230 —`**, never a rewrite. Status is a citation fact, not a truth
verdict: a row can be `mined` and wrong, and superseded rows keep `mined` —
precedent verified: S001, S003, S089, S096, S097 are all superseded and all remain
`mined` with their used-by intact. So: S230 `mined` stays as the audit trail; the
r81 plan's S250 supersede row is the contract-conformant repair; after S250 lands
S230's status remains `mined` (the r80 entry still cites it), and S250's own status
becomes `mined` iff a used-by path cites it (the lesson's gate record does not count
as a used-by path under house convention — used-by names corpus files).

### For R2 (`external-commits.json`) design

The token `7bb48f213ac677f943d5c791199ed3dddf302f00` at SOURCES.md:171 AND :172 both
bind to `mistralai/mistral-vibe` — the manifest must pin the hash→repo association
regardless of which row cell carries it (S230's repo-name is the wrong one; S231's is
right). Receipts: `.ufo/waves/round-79/snapshots/S230.fetch.json` + `S231.fetch.json`
(committed) plus the ls-remote lines above (re-derived live today). A manifest entry
keyed to pi-mono for this hash would be false; keyed to mistral-vibe it covers both
occurrences.

## 4. Bottom line for the r81 repairs

- Registry at base: structurally healthy — 174 rows, 0 malformed, 0 dup ids, 0 enum
  violations, 0 missing used-by paths; exit 0 on the maintained validate; 31 W04s all
  of the accepted distinct-scope class. Plan's `~174` expectation confirmed exactly.
- Defects the frozen census cannot see (all pre-existing, none blocking): F-A S030
  stale used-by path; F-B SKILL.md falsely listed as used-by for S112–S115; F-E
  duplicated `## Leads` section (byte-identical) with search-log content tangled
  inside; F-D duplicated mid-table header; F-F recheck vocabulary drift. F-C is
  cosmetic. All are used-by/shape precision issues — candidates for a future
  structural audit criterion; none is load-bearing for C1/C2 except F-H (S248
  status flip when C2 lands).
- S230: `mined` correct per contract, anchor wrong per three independent
  falsifications; repair = S250 `supersedes S230 —` (append-only), hash binds
  mistralai/mistral-vibe. S231: clean on every axis measured.

Commands re-runnable from the lane root; every count above carries its command in §1/§2.

VERDICT: registry healthy on all frozen axes (174 rows, exit 0, 31 accepted W04s); S230/S231 `mined` is contract-correct while S230's anchor is verifiably wrong (hash is mistral-vibe's head, not pi-mono's — supersede via S250 per rule 2, never rewrite); plus five pre-existing precision/shape defects the frozen census is structurally blind to.
DELIVERABLES: /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-81/w1/Kb81R08SourcesAudit.md
