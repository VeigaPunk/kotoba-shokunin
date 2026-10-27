# A30RevengerR3 — R3 note reconciliation, machine-checked (report only)

Seat: revenger, round 76 w1. Assignment: verify that the R3 registry note
(`.ufo/waves/round-76/build/w2-registry-note.md`, draft of the landing path
`.ufo/waves/round-76/w2-registry-note.md`) reconciles machine-checkably:
(i) the jq excerpt of `.ufo/waves/round-75/w2-results.json`'s `R75Attack28` entry is the real byte
content; (ii) the `63 of 64` report-file count recomputes. No edits, no integration, no counter runs
against data (counters do not exist at this tip — recorded below).

Lane HEAD at measurement: `7eed80e9f4488c26cb8e10ef72662e7f6ef880c1`
(`round-76: pre-data addendum fixes digest home and folded-render convention`); note's own pin
`4de12b61f75c73e3675ef0e422cc2be0f7da8960` is an ancestor (`git merge-base --is-ancestor` → exit 0).

## 1. Reconstructed contract of repair R3

Source of the routed defect, verbatim from `corpus/lessons/round-75-verifier-spotcheck.md:79`:

> **R3 (wave hygiene):** `w2-results.json` seat `R75Attack28` names `w2/R75Attack28.md`, which does not
> exist (63/64 report files). Recover the report bytes or append a registry note recording the phantom,
> so the results file reconciles with the wave dir.

Frozen form in `plans/round-76.md` § C2 (R3 conjunct):

> note `.ufo/waves/round-76/w2-registry-note.md` reconciles `.ufo/waves/round-75/w2-results.json` seat
> `R75Attack28` (named report absent; 63 of 64 report files) with a machine-checkable excerpt of the
> results entry; LOG § Round 75 cites the note path.

So R3 is satisfied only by the conjunction: (A) the named report is genuinely absent and provably
never committed; (B) the results entry is quoted in a re-runnable, byte-faithful way; (C) the 63/64
count recomputes from bytes; (D) the note lands at the frozen path and LOG cites it. (D) is an
integration duty, not a note-content duty.

## 2. Evidence chain (all run at HEAD `7eed80e`, lane clean)

### 2.1 Subject identity and provenance

```
$ sha256sum .ufo/waves/round-75/w2-results.json
e4ce0f6d3be78fa6db5da230ca6ec5e388c08e5f0196ebe66600e39da17bcf5c   # == note's pin
$ git log --oneline -1 d118a3b
d118a3b round-75: clarify sourced trigger threshold boundary            # == note's "tracked at"
$ git show d118a3b:.ufo/waves/round-75/w2-results.json | sha256sum
e4ce0f6d3be78fa6db5da230ca6ec5e388c08e5f0196ebe66600e39da17bcf5c
$ git show HEAD:.ufo/waves/round-75/w2-results.json | sha256sum
e4ce0f6d3be78fa6db5da230ca6ec5e388c08e5f0196ebe66600e39da17bcf5c      # no drift d118a3b→HEAD
$ git diff --stat d118a3b..HEAD -- .ufo/waves/round-75/w2-results.json .ufo/waves/round-75/w2/
(empty)
```

Provenance cells in the note (commit, sha256) are correct and still correct at tip.

### 2.2 Excerpt fidelity — regenerated known-good vs note block, byte compare

The note's first fenced block was reconstructed from the results file (JSON projection built from the
entry's own keys, verdict and all four evidence lines taken from `output|fromjson`) and compared to the
note's block after stripping the trailing newline. Command run (python3, read-only):

```
BLOCK_BYTE_EQUAL_KNOWN_GOOD_RERUN: True
```

Independently, each recorded output line executes today with the recorded result:

```
$ jq -c '.results[] | select(.name=="R75Attack28") | {name, agent, has_report_field: has("report"), report_field: (.report // null), note}' .ufo/waves/round-75/w2-results.json
{"name":"R75Attack28","agent":"reviewer","has_report_field":false,"report_field":null,"note":null}

$ jq -r '.results[] | select(.name=="R75Attack28") | .output | fromjson | .verdict' .ufo/waves/round-75/w2-results.json
R75Facet28 survived with a material qualification: facts and boundary test are supported, but its preventative advice is misleading if read as odd runs OR deduplication; both are required to preclude equality at the default 0.5, or state the comparator. Written report: kotoba-shokunin/.ufo/waves/round-75/w2/R75Attack28.md

$ jq -r '.results[] | select(.name=="R75Attack28") | .output | fromjson | .evidence[]' .ufo/waves/round-75/w2-results.json
Verified measured revision 65a5c7a663249e0522cc49e4a148424200d9ddfe.
Entry lines 58–72; S211-run_eval.py.txt lines 213–234 and 260–268 establish strict-vs-inclusive threshold and duplicate pooling.
Read-only arithmetic check confirmed equality at 0.5 for two duplicate 3-run entries and for one unique 2-run entry.
Reopened S210 cited snapshot; no live fetch or production execution.
```

Matches note lines exactly (same strings; `EVID_ALL_IN_NOTE_EXACT True`, `VERDICT_IN_NOTE_EXACT True`,
`PROJ_IN_NOTE_EXACT True`, `n_evidence 4`).

### 2.3 Absence of the named report — both path forms, all refs, working tree

```
$ (cd /home/vgpnk/Projects/shokunin) test -e kotoba-shokunin/.ufo/waves/round-75/w2/R75Attack28.md; echo $?
1
$ (cd .../kotoba-shokunin) test -e .ufo/waves/round-75/w2/R75Attack28.md; echo $?
1
$ git log --all --oneline --diff-filter=A -- '.ufo/waves/round-75/w2/R75Attack28.md'
(empty, exit 0)                     # no commit in any ref ever added the path
$ git status --porcelain --ignored -- .ufo/waves/round-75/w2
(empty)                             # no untracked/ignored leftover
```

The note's "phantoms, never written" characterisation is supported: no add-commit, no working-tree
copy, no ignored copy.

### 2.4 The 63/64 count recomputes

```
$ ls .ufo/waves/round-75/w2/*.md | wc -l               -> 63
$ ls -1 .ufo/waves/round-75/w2/ | wc -l                -> 64
$ ls -1 .ufo/waves/round-75/w2/ | grep -v '\.md$'      -> swarm-registry.json
$ for n in $(jq -r '.results[].name' ...w2-results.json); do [ -e ".ufo/waves/round-75/w2/$n.md" ] || echo "MISSING $n"; done
MISSING R75Attack28
$ jq -r '.seats, (.results|length), ([.results[]|select((.output//"")=="")]|length), ([.results[].name]|unique|length)' ...w2-results.json
64 / 64 / 0 / 64
```

Independent set algebra (not the note's loop): `comm` of `jq results[].name` vs the `.md` stems →
"in results but no md: R75Attack28" only; "md but not in results: (none)". Committed-bytes variant:
`git ls-tree -r --name-only <rev> -- .ufo/waves/round-75/w2 | grep -c '\.md$'` = **63** at `d118a3b`
and **63** at HEAD; total tracked entries = 64. Registry: `.members|length` = 64, member keys are
exactly the 64 seat names (`comm` empty), 0 members carry a report path — the note's parenthetical
claim about the registry holds.

Result: **63 of 64**, one gap, `R75Attack28`, 0 dead seats. The wave spec expectation that seats write
reports is explicit (`w2-spec.json` item prompt: "Write only .ufo/waves/round-75/w2/…"), so 63/64 is a
real deficit, correctly counted.

### 2.5 Verbatim quote of the routed defect

The note's quotation of `corpus/lessons/round-75-verifier-spotcheck.md` § 6 R3 is character-identical
to source line 79 (diffed by inspection of `grep -n "R75Attack28" -B4 -A6`; both strings equal).
Heading in source is `## 6. Routed defects …`, so the note's "§ 6" citation is right.

### 2.6 Whole-file phantom sweep (depth beyond the note)

Every report-path mention inside every one of the 64 `output` strings was resolved:

```
61 seats name a report path; 60 resolve to an existing .md; 1 does not (R75Attack28)
3 seats name no path at all: R75Attack34, R75Attack38, R75Attack62
```

So `R75Attack28` is the *only* ghost reference in the file — the note's singling-out is correct, and
the file's fleet-root-relative and lane-relative path forms are both used elsewhere without ghosts
(e.g. `R75Attack16`, `R75Attack29` write `kotoba-shokunin/.ufo/...` and resolve).

## 3. Divergences

**D1 — false clause: "unlike sibling seats `R75Attack08`, `R75Attack13`, `R75Attack51`, …, which do".**
The note asserts the `R75Attack28` entry lacks a top-level `report` field *unlike siblings that carry
one*. Measured: **0 of 64** entries carry a `report` field; the entry key set is uniform across the
whole file (`{agent,name,note,output}` for all 64). The three named siblings likewise have no `report`
field (`has_report` false for each). The clause is unsupported by the file the note itself quotes.

- Class: self-contradiction / inferred-from-prose. The true facts the clause was reaching for are
  available and stronger: (a) the file has a uniform schema with no `report` field anywhere; (b) the
  report path lives *only* in the verdict prose, and (c) exactly one of 61 such references is a ghost.
- Harm: the note's excerpt (`has_report_field:false`) contradicts its own prose one paragraph later; a
  closure reader or a future counter that encoded "siblings carry `report`" would mis-model the r75 w2
  schema and could mark the uniform field-absence as an R75Attack28-specific defect. The repair
  conclusion (phantom, counted, attributed) is unaffected — the entry-level claim and the count are
  true.
- Minimal correction (for the scribe/integrator, not applied here): replace
  "carries **no** top-level `report` field (unlike sibling seats `R75Attack08`, `R75Attack13`,
  `R75Attack51`, …, which do)" with
  "carries **no** top-level `report` field (all 64 entries share the key set
  `agent,name,note,output`; the report path appears only inside the embedded verdict prose — for
  `R75Attack28` it is the file's single ghost reference, 1 of 61)".

**D2 — stale HEAD pin (calibration, harmless at this tip).** Note: "Measured at lane `HEAD`
`4de12b61…`". Actual HEAD is `7eed80e…` (one commit later, `plans/round-76-addendum-1.md`). Ancestor
check passes and `git diff --stat 4de12b6..HEAD -- .ufo/waves/round-75/` is empty, so every number in
the note still holds at tip; the pin should read the measurement commit or be qualified, otherwise the
note's "measured at HEAD" is false-by-drift in exactly the way the lane's M75-1 family punished.

**D3 — landing path not yet present (integration, not note content).**
`test -e .ufo/waves/round-76/w2-registry-note.md` → absent; only the build draft exists. `LOG.md` §
Round 75 contains no `w2-registry-note` citation (`grep -n "w2-registry-note" LOG.md` → empty), and
`LOG.md:2810` still ends "w2 falsify results pending" (that is R4, pending). R3's frozen conjunct is
therefore **not yet satisfiable** at this tip: content is right, placement/citation is outstanding.

**D4 — counters absent at tip (expected pre-integration, recorded for calibration).**
`verifiers/check_r75_routed_repairs.py` and `verifiers/check_desc_craft.py` do not exist at `7eed80e`
(`ls verifiers/ | grep -E 'r75_routed|desc_craft'` → only `check_sibling_census.py`). The frozen
predicates `r75 routed repairs closed 4 of 4` / `description craft backed 6 of 6` cannot be run yet;
nothing here claims they pass. My verification is of note content only.

## 4. Coverage / calibration

| Note claim | Status | Basis |
|---|---|---|
| sha256 `e4ce0f6d…` | verified | `sha256sum` (+ blob at `d118a3b` and HEAD) |
| tracked at `d118a3b` | verified | `git log -1 -- <file>` |
| no `report` field on the entry | verified | `jq keys` → `[agent,name,note,output]` |
| siblings *do* carry `report` | **falsified (D1)** | 0/64 entries carry it; 3 named siblings false |
| path appears only in verdict prose | verified | 1 occurrence of `R75Attack28.md`; key = `output` |
| absent in both path forms | verified | `test -e` → 1, 1 |
| never committed / no leftover | verified | `--diff-filter=A` empty; `status --ignored` empty |
| 63 `.md`, 64 entries, 1 gap | verified | `ls`, `comm`, `git ls-tree` at two revs |
| 64 seats / 64 results / 0 empty / 64 unique | verified | `jq` scalar dump |
| registry: 64 members, no report paths | verified | `.members|length` 64, keys == seat names, 0 report fields |
| "measured at HEAD `4de12b6`" | **stale (D2)** | HEAD `7eed80e`; ancestor; r75 bytes unchanged |
| note at frozen path / LOG cites it | **absent (D3)** | `test -e`, `grep LOG.md` |

Confidence: **high** on 2.1–2.5 (byte-level comparisons, two independent count methods, two revs);
**high** on D1 (exhaustive key-set census over all 64 entries, not a sample); D2/D3 are single-command
facts. Nothing in this report was inferred from names or prose alone.

Bottom line: the excerpt is byte-faithful and the 63/64 count recomputes independently — the repair's
substance is sound — but the note carries one falsified parenthetical about sibling schema (D1) that
must be corrected before it lands, plus a stale HEAD pin (D2) and the still-missing landing
path/LOG citation (D3, owner: integrator).

VERDICT: R3-NOTE-RECONCILES (excerpt byte-equal, 63/64 recomputes, phantom attributed) WITH ONE FALSE PARENTHETICAL (sibling `report` field; 0/64 carry it) AND STALE HEAD PIN; landing path absent at this tip.

## 5. Housekeeping

- No installs. No pacman, no network, no git/jj writes, no subagents, no background jobs.
- Scratch `/fast/scratch/hyaku/kotoba-r76/A30RevengerR3/` created for the byte-compare helper and
  removed before yield; two temp files under `/tmp` (`a30_dirs.txt`, `a30_res.txt`, `a30_mem.txt`,
  `a30_mk.txt`) used only as set-algebra inputs, not citable evidence.
- Files written: this report only.
