verdict: HOLDS — P-E/P-F/second-array attacks on OC-1 derivation in verify_surfaces.py against the real frozen opencode-1.19.3 dump: every planted/dropped name produces the claimed exit code and the claimed class id; the regex CAN anchor on a planted same-line decoy but never flips a verdict.

## Scope

Target: `verifiers/verify_surfaces.py` OC-1 derivation at 7ad7fadfc09354b74fb66605dfb0c1182c115a2f, attacked on the real dump `/fast/scratch/kotoba-r47/shared/opencode-1.19.3.strings` (sha256 `f4d8f34ae02a2411eb5e30203421b6fcdfa81b83e96b768bbcf404504a297bc3`, 67,839,091 bytes, 750,050 lines), never on the in-repo fixtures alone.

Code under attack (path:line at 7ad7fad):
- `verifiers/verify_surfaces.py:370` — `OC_PRIORITY_RE = re.compile(r'\["AGENTS\.md".{0,400}?"CONTEXT\.md"[^\]]{0,200}\]')`
- `verifiers/verify_surfaces.py:371` — `OC_MD_NAME_RE` (derives every `"*.md"` literal in the matched span)
- `verifiers/verify_surfaces.py:372` — `OC_GATE = "disableClaudeCodePrompt"`
- `verifiers/verify_surfaces.py:447-455` — OC-1: `OC_PRIORITY_RE.search(dump)` (leftmost match), names derived from the span, fallback `owns` = the three default ids when no match; `rule()` adds `owns` to the extracted set only when matched (`verifiers/verify_surfaces.py:437-444`)
- `verifiers/verify_surfaces.py:727-760` — `check_opencode_extract` two-way parity (vacuity / missing / extra / unmatched)
- `verifiers/verify_surfaces.py:1035-1048, 1065-1070` — the in-repo fixture expectations my real-dump runs independently confirm

Pristine-dump facts (measured, not assumed):
- Exactly one `["AGENTS.md"` array in the whole dump satisfies OC_PRIORITY_RE: span bytes 10893162–10893235 on dump line 443993, text `["AGENTS.md",...!t.disableClaudeCodePrompt?["CLAUDE.md"]:[],"CONTEXT.md"]` — matching the comment at `verifiers/verify_surfaces.py:366` ("dump 443993").
- `"CONTEXT.md"` occurs exactly ONCE in the entire 67.8 MB dump (byte 10893222, inside that array).
- Two other `["AGENTS.md"` arrays exist (bytes 12866337, 18744038) and never match (no reachable `"CONTEXT.md"`).

## Baseline (before)

```
$ cd <clone at 7ad7fad> && python3 verifiers/verify_surfaces.py \
    --omp-strings /fast/scratch/kotoba-r47/shared/omp-18.12.5.strings \
    --opencode-strings /fast/scratch/kotoba-r47/shared/opencode-1.19.3.strings
PASS surfaces.literal_present: 42 loader-kind entries verified against the dumps
PASS surfaces.no_uncovered_class: all 8 extracted loader class(es) declared
PASS surfaces.opencode_extract: opencode extraction 9/9 declared class(es) from 7/7 rules (OC-1, OC-2, OC-3a, OC-3b, OC-4, OC-5, OC-6)
PASS surfaces.table_parity / literal_parity / kind_parity / excluded_reason
EXIT=0
```

## (a) P-E — plant `"GUIDE.md"` into the 1.19.3 priority array

Splice: `,"GUIDE.md"` inserted as second element of the real array (byte span 10893162–10893235 → 10893246). Mutated copy: `/fast/scratch/kotoba-r47/w2/W2PlantedName/dumps/strings-oc-pe-planted-GUIDE.txt` (sha256 `ff95d3ee…88ff`).

```
EXIT=1
FAIL surfaces.opencode_extract: extracted opencode class(es) undeclared in baseline: opencode:instructions/GUIDE.md
```

Exactly the claimed behavior (C1's oc-planted-name expectation, here proven on the real dump, not the fixture). Regex still anchors at 10893162; derived names become {AGENTS, CLAUDE, CONTEXT, GUIDE}; the single extra id is named verbatim.

## (b) P-F — drop `"CONTEXT.md"` from the array

Splice: `,"CONTEXT.md"` (13 bytes) removed from the real array. Mutated copy: `…/dumps/strings-oc-pf-dropped-CONTEXT.txt` (sha256 `1a8e8cd6…674b`).

```
EXIT=1
FAIL surfaces.literal_present: 1 loader literal(s) not verifiable: opencode:instructions/CONTEXT.md (literal 'CONTEXT.md' absent from opencode dump)
FAIL surfaces.opencode_extract: declared opencode class(es) produced by no rule: opencode:instructions/AGENTS.md, opencode:instructions/CLAUDE.md, opencode:instructions/CONTEXT.md; rule(s) matched nothing: OC-1 (owns opencode:instructions/AGENTS.md, opencode:instructions/CLAUDE.md, opencode:instructions/CONTEXT.md; missing ["AGENTS.md" … "CONTEXT.md"] + disableClaudeCodePrompt)
```

`opencode:instructions/CONTEXT.md` is named — twice — and NOT misattributed: since `"CONTEXT.md"` occurs nowhere else in the dump, OC_PRIORITY_RE has 0 matches (verified: `n_matches: 0`), so there is no wrong-array match to steal the anchor; OC-1 reports itself unmatched with its true ownership list, and OC-2..OC-6 all still match (no other FAIL line). Precision note, not a misattribution: the OC-1 unmatched message co-names AGENTS.md/CLAUDE.md because OC-1 genuinely owns all three ids (`verifiers/verify_surfaces.py:451-453`); `literal_present` attributes CONTEXT.md alone.

## (c) second unrelated `["AGENTS.md","X.md"]` array elsewhere — does OC_PRIORITY_RE pick the wrong one?

Two placements, both decoys `["AGENTS.md","X.md"]`:

(c1) Same line as the real array, 62 bytes before it (byte 10893100, dump line 443993). Copy `…/dumps/strings-oc-pc-bridge-sameline.txt` (sha256 `5d5527f0…829c`):

```
EXIT=1
FAIL surfaces.opencode_extract: extracted opencode class(es) undeclared in baseline: opencode:instructions/X.md
```

YES — the regex picks the WRONG array: leftmost-match semantics anchor the span at the decoy (span 10893100–10893255 instead of 10893162+), because the decoy sits within the 400-char lazy bridge of the real array's `"CONTEXT.md"` and CONTEXT.md is last, so `[^\]]{0,200}\]` completes on the real array's closer. Derived names = {AGENTS, CLAUDE, CONTEXT, X}. But the verdict stays correct: exit 1 naming the planted `opencode:instructions/X.md` undeclared. A wrong anchor cannot launder a planted name, and cannot forge a failure for an untouched dump (any span end must consume a real `"CONTEXT.md"`+`]`, so names outside planted content are exactly the declared three on this dump).

(c2) Own line after dump line 100 (no `"CONTEXT.md"` reachable — `.` in the regex cannot cross `\n`). Copy `…/dumps/strings-oc-pc-far-ownline.txt` (sha256 `cd29b7e1…2c8a`):

```
EXIT=0
PASS surfaces.opencode_extract: opencode extraction 9/9 declared class(es) from 7/7 rules (OC-1, OC-2, OC-3a, OC-3b, OC-4, OC-5, OC-6)
```

The signature-gated decoy is ignored; no false positive. Known single-anchor limitation (a second genuine priority-list-shaped array would be invisible to OC-1) is pre-declared in the header (`verifiers/verify_surfaces.py:36-39`, loaders shaped as config arrays are covered "by declaration only" for non-OC-1 channels) and is not a C1 claim violation.

## Exit-code summary (all on the real frozen dump, clone at 7ad7fad)

| Scenario | Exit | Named id |
|---|---|---|
| pristine | 0 | — (9/9, 7/7 rules) |
| (a) plant GUIDE.md | 1 | `opencode:instructions/GUIDE.md` undeclared |
| (b) drop CONTEXT.md | 1 | `opencode:instructions/CONTEXT.md` (literal_present + OC-1 unmatched) |
| (c1) decoy same line | 1 | `opencode:instructions/X.md` undeclared |
| (c2) decoy own line | 0 | — |

## Repro

Scratch clone `/fast/scratch/kotoba-r47/w2/W2PlantedName/kotoba-shokunin` (detached at 7ad7fad). Mutated dumps (NOT copies into the lane) under `/fast/scratch/kotoba-r47/w2/W2PlantedName/dumps/`; splice spec + digests in `W2PlantedName.oc1-mutations.txt` beside this report. Re-run any scenario with:

```
python3 verifiers/verify_surfaces.py \
  --omp-strings /fast/scratch/kotoba-r47/shared/omp-18.12.5.strings \
  --opencode-strings /fast/scratch/kotoba-r47/w2/W2PlantedName/dumps/<scenario>.strings
```

## Not checked

- OC-2..OC-6 mutations on the real dump (sibling seats W2DropOC1/2/3a/6 cover the fixture side; my (b) run incidentally shows OC-2..OC-6 still match on the real dump).
- `literal_present`/`no_uncovered_class` for the omp dump; baseline/inventory re-derivation (C1 census content) — outside this seat.
- Regex catastrophic-backtracking risk of the bounded quantifiers (bounded by construction; not timed).
- Whether the omp 18.12.5 dump contains an analogous plantable priority array (omp has no OC-1 analogue; its extractor is CALL_RE-shaped, `verifiers/verify_surfaces.py:162`).

Tooling installs: none (no pacman/uv/npm installs performed; pacman host-wide pause respected).
