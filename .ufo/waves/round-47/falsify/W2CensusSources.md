verdict: PARTIAL — the SOURCES.md census at 7ad7fad is clean on every shipped gate and all four new rows (S012–S015) re-open and hold, but S015's `used-by` pointer names a file that does not cite the row, and neither the frozen seven-command census nor the maintained `sources-census.sh` can see it (mutation M5 exits 0 "ok").

# Lane: kotoba-shokunin `corpus/SOURCES.md` census (round-47 falsify, wave 2)

Target commit: `7ad7fadfc09354b74fb66605dfb0c1182c115a2f` (BASE `c61a973b2e02e1ded169703ddcb06466f4edd8bd`).
Scratch clone (canonical layout, sibling symlinks): `/fast/scratch/kotoba-r47/w2/W2CensusSources/kotoba-shokunin` @ detached 7ad7fad.
Artifacts: `.ufo/waves/round-47/falsify/W2CensusSources.commands.txt`, `.ufo/waves/round-47/falsify/W2CensusSources.mutants.txt`.
No production file was modified; no repo git/jj command was run in the lane repo; no subagent dispatched.

## 1. What I ran (exit codes)

```
$ /home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /fast/scratch/kotoba-r47/w2/W2CensusSources kotoba
kotoba	ok	.../kotoba-shokunin/corpus/SOURCES.md          exit=0
$ … census --root … kotoba
kotoba rows 15 | tier.A 14 | tier.C 1 | status.mined 6 | status.queued 8 | status.rejected 1
FLEET rows 15 tier.A 14 tier.B 0 tier.C 1 tier.invalid 0 … missing 0      exit=0
$ … validate --root … --today 2026-10-21            # fleet-wide, default resolution
kotoba	ok	.../kotoba-shokunin/corpus/SOURCES.md          exit=0  (fleet exit=0; kotoba emits no W-code,
                                                                  15 sibling lanes emit W04/W01)
$ … overdue --root … --today 2026-10-21 kotoba       # 15 cadence lines, no overdue → exit=0
$ … shared  --root … kotoba                           # no shared URL → exit=0
```
The seven frozen census commands (verbatim, `/home/vgpnk/Projects/shokunin/CORPUS.md:131-148`), run from the lane root at 7ad7fad:

| # | command (frozen) | output | exit |
|---|---|---|---|
| C1 | `grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md` | `15` | 0 |
| C2 | `awk -F'|' … NF!=13 {n++} END{print n+0}` | `0` (no malformed row) | 0 |
| C3 | tier histogram | `A=14 C=1` (no tier B, no invalid) | 0 |
| C4 | status histogram | `mined=6 queued=8 rejected=1` | 0 |
| C5 | duplicate ids `… | sort | uniq -d` | *(empty)* | 0 |
| C6 | enum violations + tier inflation | *(empty)* | 0 |
| C7 | mined rows whose used-by paths do not exist | *(empty — all 6 exist)* | 0 |

Full transcript with every command line and exit code: `W2CensusSources.commands.txt`.

## 2. Rows 11→15 (corpus/SOURCES.md at 7ad7fad)

| row | line | kind | tier | status | opened | recheck | used-by | exists? | cites the row? |
|---|---|---|---|---|---|---|---|---|---|
| S011 Agentman tutorial | SOURCES.md:24 | community | C | rejected | 2026-10-19 | 180d | — | n/a | n/a |
| S012 anthropics/skills skill-creator | SOURCES.md:25 | code | A | mined | 2026-10-21 | 90d | `SKILL.md` | yes | **yes** (SKILL.md:151) |
| S013 OpenAI Build skills | SOURCES.md:26 | docs | A | queued | 2026-10-21 | 90d | — | n/a | n/a |
| S014 Anthropic Engineering | SOURCES.md:27 | docs | A | queued | 2026-10-21 | 90d | — | n/a | n/a |
| S015 kotoba own work (substrate sha) | SOURCES.md:28 | own-work | A | mined | 2026-10-21 | on-release | `corpus/knowledge/instruction-surface-census-round13.md` | yes | **NO — 0 occurrences** |

Mined rows overall (6): S001, S002, S003, S008, S012 → `SKILL.md` (all exist, all cite their row); S015 → the knowledge entry (exists, cites nothing). Zero mined rows are cited by a `corpus/knowledge/` entry: `grep -rnE '\bS0[0-9]{2}\b' corpus/knowledge/` → **0 files**.

## 3. Findings

### F1 (medium, calibration) — S015's `used-by` names a file that does not cite the row, and no gate can see it

- Path: `corpus/SOURCES.md:28` (row S015, `status=mined`, `used-by=corpus/knowledge/instruction-surface-census-round13.md`).
- Contract: `/home/vgpnk/Projects/shokunin/CORPUS.md:103` — `mined` = "cited by ≥1 path in `used-by`"; `CORPUS.md:107` — "`used-by` — repo-relative paths of the knowledge entries or lessons **citing the row**".
- Repro (from the lane root at 7ad7fad):
  ```
  $ grep -c 'S015' corpus/knowledge/instruction-surface-census-round13.md
  0
  $ grep -nE '\bS0[0-9]{2}\b' corpus/knowledge/instruction-surface-census-round13.md
  (no output at all — the entry carries no S### token of any kind)
  ```
  The entry cites the *evidence* of S015 (the pinned sha256 at `corpus/knowledge/instruction-surface-census-round13.md:214-215`) but never the row.
- The row **is** cited — by a lesson: `corpus/lessons/round-47.md:38` (Gate table row `S015 | own work — sha256sum -c SHA256SUMS …`) and `corpus/lessons/round-47.md:44` ("C1 rests on S015 (the pinned bytes are the snapshot bytes)"). So `mined` is substantively true; the *pointer* is false. Contract rule 2 (`CORPUS.md:116`) allows `used-by` to change in place with an old→new log in the round lesson, so this is a one-cell erratum, not a new row.
- Why every shipped gate misses it (counterexample, `W2CensusSources.mutants.txt` M5): the frozen C7 tests existence only (`[ -e "$p" ] || echo "missing: $p"`), and the maintained validator's E11 is literally `[ ! -e "$dir/$path" ]` (`scripts/sources-census.sh:566-568`). Mutating a mined row's used-by to an existing-but-not-citing file leaves **both** gates silent:
  ```
  frozen : rows=15 malformed=0 dupids=[] enums=[] usedby-missing=[]
  maint. : exit=0  "w2c_mut ok /tmp/w2c_mut/corpus/SOURCES.md"
  ```
  So this class of falsehood is structurally invisible to the census; it needs a citation check (`grep -c "\b$id\b" "$path"`) that neither gate has. Fix for the lane: point S015's used-by at `corpus/lessons/round-47.md` (which cites it), and log the old→new change in the next round's lesson `## Gate`.

### F2 (low, calibration) — the round-47 rewrite of the cited entry carries no provenance trio, so it had nowhere to cite S015 from

- Path: `corpus/knowledge/instruction-surface-census-round13.md` (+93 lines in `git diff c61a973..7ad7fad -- corpus/knowledge/instruction-surface-census-round13.md`).
- Fleet rule (`CORPUS.md`, kaika campaign): "A new knowledge entry opens with its provenance trio. `source:`, `verified-at:` and `recheck:` come first."
- Observed: `grep -nE '(source|verified-at|recheck):' corpus/knowledge/instruction-surface-census-round13.md` → **no match**; there is no `source:` line anywhere in the entry. The entry is not *new* (rule targets new entries) so this is pre-existing, but round 47 rewrote 93 lines of it and did not add one. Lane-wide: only 2 of 32 `corpus/knowledge/*.md` files have the trio (`harness-independent-round41-census.md`, `sibling-citation-routing-round16.md`) — a fleet-legacy gap, not a round-47 regression, but it is the structural reason F1 exists: the entry S015 points at has no `source:` line to hang an `S015` citation on.
- Also note the entry's own § B′ claim is *true* and independently verified: `corpus/knowledge/instruction-surface-census-round13.md:214` names `/home/vgpnk/.npm/_npx/e2094862b59aac7b/node_modules/opencode-ai/bin/opencode.exe` with sha256 `179ca421…`; that file is in fact an ELF (not a PE, despite the `.exe` name) and `sha256sum` of it = `179ca421d61eefeadfa0c50e084a6e79c1623734732f0f4593f81ccfd3ab7ee9` = the frozen `bin/opencode-1.19.3` pin. Path+hash pair: **holds**.

### F3 (low) — 5 of 6 mined rows point `used-by` at `SKILL.md`, which is neither a knowledge entry nor a lesson

- Paths: `corpus/SOURCES.md:14,15,16,21,25` (S001, S002, S003, S008, S012 → `SKILL.md`); contract wording `CORPUS.md:107`.
- Substance holds — `SKILL.md:151` cites `S001, S002, S003, S008` and `(S012)`, and `corpus/lessons/round-46.md` / `round-47.md` cite the same rows; only the *kind* of path is off-contract. Worth noting because rule 4's expansion metric ("admitted `knowledge/` entries whose `source:` cites a `mined` row", `CORPUS.md:123`) can never be non-zero for this lane while no entry cites a row: `grep -rnE '\bS0[0-9]{2}\b' corpus/knowledge/` → 0 files.

### F4 (low, pre-existing) — the frozen seven-command battery has no section check; a row outside `## Registry` is counted as a row and flagged by nothing

- Contract block `CORPUS.md:131-148` vs the maintained CLI's `E12` (`scripts/sources-census.sh:621`).
- Counterexample (`W2CensusSources.mutants.txt` M6): appending a well-formed `| S017 | … |` row under `## Leads (unopened)` yields `rows=16` (the row is counted) while malformed/dupids/enums/used-by all stay empty; the maintained validator says `E12 S017 row outside Registry section`, exit 1. The frozen battery reports "15 rows" but cannot tell a registry row from a stray row elsewhere in the file. Not introduced by round 47 — it is a property of the frozen contract block — but the round-47 "rows 15" figure inherits it.

### F5 (medium, calibration) — the S001 anchor defect is disclosed but the round still leaves a knowingly-wrong anchor in place

- `corpus/SOURCES.md:14` (S001 anchor reads "§ Skill metadata table, § Progressive disclosure"); the lane records at `corpus/lessons/round-47.md:46-48` that "its anchor label '§ Skill metadata table' names no heading on the live page", and that "contract rule 2 forbids an in-place anchor edit, so the defect is recorded here and a superseding row waits for the next round that cites S001".
- This is honest disclosure and rule 2 is honoured (the diff changes no existing row cell), so it is **not** a violation. Flagging it because S001 is `mined` and its anchor names a section that does not exist on the page it cites: the defect is load-bearing for a row the round still counts as tier-A/mined. Counterexample the next round can run: fetch `https://agentskills.io/specification` and grep the headings for "Skill metadata table" (I did not run it — see §5).

## 4. Claims that survived my attack

- **C1 substrate re-derivation (S015, own-work): holds.** `cd /fast/scratch/kotoba-r47/shared && sha256sum -c SHA256SUMS` → `bin/omp-18.12.5: OK`, `bin/opencode-1.19.3: OK`, `omp-18.12.5.strings: OK`, `opencode-1.19.3.strings: OK`, exit 0 (4/4). Live `~/.local/bin/omp` sha256 = `fdbc8136084c9a10439569157b2af62312e2b0d801cab54c73e89476da798e7e` = the pin; npx-cache ELF `~/.npm/_npx/e2094862b59aac7b/node_modules/opencode-linux-x64/bin/opencode` sha256 = `179ca421d61eefeadfa0c50e084a6e79c1623734732f0f4593f81ccfd3ab7ee9` = the pin; `opencode-ai/package.json` version = `1.19.3`. `~/.local/bin/opencode` is a 1460-byte bash wrapper — read, never executed.
- **S012 row (rule 1): holds exactly.** `curl https://raw.githubusercontent.com/anthropics/skills/dbd4588f9e1033efb41dad4bef2f7947c8993d44/skills/skill-creator/scripts/quick_validate.py` → HTTP 200, 3972 bytes, sha256 `67cf5703402013936c8fb75ad6a1afecd8841d45cc5e606b634eb05825fde365` — the same prefix the Gate records (`corpus/lessons/round-47.md:35`). The quote "Description cannot contain angle brackets (< or >)" sits at line **81**; the row's anchor `quick_validate.py:79-81` covers exactly the "# Check for angle brackets" block (79 comment, 80 test, 81 message). The `teaches` claim ("refuses any `<` or `>` … stricter than the S003 prose rule") is exactly what the code does.
- **S013 row: holds.** `https://learn.chatgpt.com/docs/build-skills` → HTTP 200; `https://developers.openai.com/codex/skills` → **HTTP 308** → `https://learn.chatgpt.com/docs/build-skills` (the row's "308 from developers.openai.com/codex/skills" is exact); `Last-Modified: Wed, 21 Oct 2026 15:05:00 GMT` = the row's "2026-10-21T15:05:00Z". Rendered prose: "In Codex, the initial list also includes each skill's file path. By default, this list uses at most 2% of the model's context window, or 8,000 characters when the context window is unknown. If many skills are installed, Codex shortens skill descriptions first." and "Implicit invocation: ChatGPT or Codex can choose a skill when your task matches the skill description." → the row's `teaches` ("caps its initial skill list at 2% of context (8,000 characters when unknown), shortens descriptions first, and gates implicit invocation on the description") is supported.
- **S014 row: holds.** HTTP 200, 216,618 bytes (matches the seat report's byte count in `.ufo/waves/round-47/build/SrcNewAnthropicEng.md:1`); `datePublished 2025-10-16`, `dateModified 2026-10-18T21:26:58Z` — the row's "published 2025-10-16, modified 2026-10-18"; the ground quote is present verbatim in the rendered text ("At startup, the agent pre-loads the `name` and `description` of every installed skill into its system prompt."); the three-level model is present ("first level"/"second level"/"third level" of progressive disclosure).
- **Contract rule 2 (append-only) holds for round 47.** `git diff c61a973..7ad7fad -- corpus/SOURCES.md` touches **no** existing row cell: 4 row insertions (S012–S015), one search-log bullet (`corpus/SOURCES.md:72`), and one intro-paragraph edit. Consistent with `corpus/lessons/round-47.md:29-31` ("All four rows are new; no existing row's `status`, `recheck` or `used-by` changed (old→new: none)") — independently confirmed by diff, not by the lesson's assertion.
- **Contract rule 1 (Gate evidence for every new row) holds.** `corpus/lessons/round-47.md:33-38` gives URL, access timestamp, a ≤25-word quote and its location for each of S012–S015 (quote lengths 7, 20, 19 words; S015 is a hash line, not prose).
- **Search log (rule 5) reconciles.** `corpus/SOURCES.md:72-81`: 7 identified = 4 included (S012–S015) + 3 excluded (anthropics/skills `spec/agent-skills-spec.md`, opencode skills docs, Anthropic platform skills guide); re-opened set "S001–S005 and S008" = 6 rows, matching `corpus/lessons/round-47.md:46-49` ("S006, S007 not re-opened").
- **C2's substance spot-check:** `SKILL.md` frontmatter `description` (folded `>` scalar) contains no XML tag — the `<skills>` token is gone; `re.findall(r'</?[A-Za-z][A-Za-z0-9_:.-]*(?:\s[^<>]*)?/?>', description)` → `[]`.
- **The census itself is live, not vacuous:** mutation matrix M1b/M2/M3/M4 each make the frozen battery and the maintained CLI fail with the expected code and exit 1 (see `W2CensusSources.mutants.txt`), so the "clean" result at 7ad7fad is a real measurement, not a gate that never fires.

## 5. What I did NOT check

- I did not re-open S001–S011's sources (agentskills.io spec, the Claude client guide, Claude best practices, CommonMark 0.31.2, RFC 8259, the Python json docs, the Agentman tutorial) to re-verify their quotes — the lane's own round-47 record claims they were re-opened, and peers own S003/S012 reopens. In particular I did **not** run the F5 counterexample (grep the live agentskills.io page for a "Skill metadata table" heading).
- I did not verify the three **excluded** candidates named in the search log (anthropics/skills `spec/agent-skills-spec.md` as "a 3-line pointer", the opencode skills docs as "tier B at best", the Anthropic platform skills guide as "states the rule S003 already carries") — I took the exclusion reasons as written.
- I did not run the lane's own verifiers (`verifiers/verify_surfaces.py`, `verifiers/check_substrate_pins.py`, `verifiers/verify_skill_checklist.py`, `verify_corpus_integrity.py`) — C1/C2/C3 gates belong to other lanes; I only independently re-verified the substrate bytes those gates pin (S015) and the census.
- I did not audit the `## Registry` of the 30 sibling lanes (the fleet-wide run was used only to confirm kotoba is clean in default resolution); W04/W01 findings in other lanes were not analysed.
- I did not re-derive § B′'s per-id class ledger or the § Superseded class rows inside `corpus/knowledge/instruction-surface-census-round13.md` — I verified only its substrate citation (path + sha256) and the absence of an `S###` citation.
- I did not check whether `verifiers/corpus-baseline.json` pins the *content* of `corpus/SOURCES.md` (the only mention of SOURCES.md in that file is prose inside the `round46_landing` note, so the tracked-file list is unaffected by row edits) — the 58→60 arithmetic belongs to the C3 lane.
- No tool was installed or upgraded for this lane: `curl`, `python3`, `gawk`, `bash` and `sha256sum` were already present and sufficient; nothing was fetched from the network except the four source pages re-opened above (all read-only GETs).

## 6. Net judgement

Freshness: holds — every new row's source re-opens today at the exact revision the row names, and the substrate bytes behind S015 re-verify byte-for-byte.
Operability: holds — the census CLI runs clean on kotoba in both lane-scoped and fleet-default resolution, and every mutation I could think of that the frozen battery claims to catch does make it fire.
Calibration: **partial** — the registry is internally clean, but one new row (S015) ships a `used-by` pointer that is false against its own contract sentence, and the corpus's citation-side check for `used-by` does not exist in any shipped gate, so the falsehood cannot be caught by re-running the census (F1). F2–F4 are lower-severity contract-shape gaps; F5 is disclosed-but-unfixed.
