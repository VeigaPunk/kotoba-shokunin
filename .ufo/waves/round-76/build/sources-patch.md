# S213 `used-by` patch — build draft (seat B14SourcesUpdate, round 76 w1)

Status: **draft only, not applied.** No lane file was written by this seat. The lane
`corpus/SOURCES.md` at lane HEAD `4de12b61f75c73e3675ef0e422cc2be0f7da8960` still carries the
old row; every receipt below was produced on copies under
`/fast/scratch/hyaku/kotoba-r76/B14SourcesUpdate/`.

Measured base: `4de12b61f75c73e3675ef0e422cc2be0f7da8960` (round-76 plan/dispatch commit). The
contract's C2 base `b7f13f4b39cbd43076a85568adca763a6f674e7a` carries the same S213 row (verified:
`git show b7f13f4:corpus/SOURCES.md | sed -n '153p'` is byte-identical to the HEAD line, diff empty).

## The change — one cell, one line

File: `corpus/SOURCES.md`, registry row `S213`, **line 153**, cell index 11 (`used-by`) only.
Rule 2 of `CORPUS.md` (fleet root, lines 116–118) permits exactly this cell in place: *"Only
`status`, `recheck` and `used-by` change in place, and each change is logged old→new in the round
lesson."*

Old `used-by` cell (verbatim, spaces included):

```
 corpus/knowledge/skill-eval-artefacts-round70.md 
```

New `used-by` cell (verbatim, spaces included):

```
 corpus/knowledge/skill-eval-artefacts-round70.md, corpus/knowledge/description-craft-round76.md 
```

Separator is **comma + space**. The census parser splits `used-by` on `,` only
(`scripts/sources-census.sh`, `usedby_findings()`: `IFS=',' read -r -a paths <<< "$usedby"`), so a
semicolon would leave one path string and fire `E11` on the whole cell.

Old line 153 (verbatim; 810 characters = 814 UTF-8 bytes, 815 with `wc -c` incl. newline):

```
| S213 | Agent Skills — Optimizing skill descriptions — https://agentskills.io/skill-creation/optimizing-descriptions.md | docs | A | the open specification's own trigger-eval protocol for a skill description; supersedes S210 for citation | the "Running multiple times" subsection of "Testing whether a description triggers"; upstream commit 69ef37e9424c0a7ea9dd2293b559e43ec8176379 `docs/skill-creation/optimizing-descriptions.mdx` (equal to main on 2026-10-25, git ls-remote); quote "A should-trigger query passes if its trigger rate is above a threshold (0.5 is a reasonable default)." (17 words) | trigger queries carry should_trigger, run about 3 times each, pass on trigger rate against 0.5, with a held-out validation split | mined | 2026-10-25 | 90d | corpus/knowledge/skill-eval-artefacts-round70.md |
```

New line 153 (verbatim; 857 characters = 861 UTF-8 bytes, 862 with `wc -c` incl. newline):

```
| S213 | Agent Skills — Optimizing skill descriptions — https://agentskills.io/skill-creation/optimizing-descriptions.md | docs | A | the open specification's own trigger-eval protocol for a skill description; supersedes S210 for citation | the "Running multiple times" subsection of "Testing whether a description triggers"; upstream commit 69ef37e9424c0a7ea9dd2293b559e43ec8176379 `docs/skill-creation/optimizing-descriptions.mdx` (equal to main on 2026-10-25, git ls-remote); quote "A should-trigger query passes if its trigger rate is above a threshold (0.5 is a reasonable default)." (17 words) | trigger queries carry should_trigger, run about 3 times each, pass on trigger rate against 0.5, with a held-out validation split | mined | 2026-10-25 | 90d | corpus/knowledge/skill-eval-artefacts-round70.md, corpus/knowledge/description-craft-round76.md |
```

Byte delta: `857 - 810 = +47` characters (= 861 − 814 bytes) = `len(", corpus/knowledge/description-craft-round76.md")` (45 + 2);
no other byte on the line moves (`diff` of the two lines reports exactly one changed line, and the
appended text is the only insertion).

## Application constraint (operability)

The append **must land in the same commit as** `corpus/knowledge/description-craft-round76.md`.
The census resolves each `used-by` path against the lane root and raises `E11` when the file is
absent, so the SOURCES edit alone turns `kotoba ok` into `kotoba E11` + exit 1. Two-arm receipt:

```
$ bash scripts/sources-census.sh validate --file <mirror>/corpus/SOURCES.md --today 2026-10-27
file	E11	S213 missing used-by corpus/knowledge/description-craft-round76.md
exit=1
# after `printf 'stub entry, E11 fixture only\n' > <mirror>/corpus/knowledge/description-craft-round76.md`
$ bash scripts/sources-census.sh validate --file <mirror>/corpus/SOURCES.md --today 2026-10-27
file	ok	<mirror>/corpus/SOURCES.md
exit=0     # only the 20 pre-existing W04 warnings precede the ok line, unchanged from base
```

The knock-on is measured, not predicted: `check_spec_craft.py` (green, 3 of 3, exit 0 at
`b7f13f4`) carries a census-conformance conjunct, so the SOURCES line committed **without** the
entry drops it to `0 of 3`, exit 1 —

```
$ python3 -B verifiers/check_spec_craft.py --rev bccb297      # patch commit only
spec craft pages backed 0 of 3
  best-practices: corpus/SOURCES.md is not census-conformant at bccb297 (conjunct (b))
  … (same line for using-scripts, quickstart)
exit=1
$ python3 -B verifiers/check_spec_craft.py --rev <+entry stub in the next commit>
spec craft pages backed 3 of 3
exit=0
```

Real-lane base control, same parser, same day: `kotoba ok …/corpus/SOURCES.md`, `exit=0`
(20 `W04` duplicate-url warnings, the r75 set).

## Columns — the 11-column check the seat names

```
$ awk -F'|' 'NR==153{print "NF="NF}' corpus/SOURCES.md          -> NF=13   (11 cells + 2 edge empties)
$ python3 -c "...split('|')..."                                  -> cells=11, used-by cells[11], trailing cells[12] empty
$ grep -cE '^\|[[:space:]]*S[0-9]{3,}' corpus/SOURCES.md          -> 151 before, 151 after
```

`NF=13` is the census contract itself: `scripts/sources-census.sh:3` — *"one registry table, 11
columns => NF=13"*; `E01 malformed row (NF!=13)`. The new line keeps `NF=13`, and the registry
row count is unchanged at 151 (no row added, none removed).

### Apply-check: this artifact alone is sufficient

Extracting the two fenced lines above and substituting the new one at line 153 of a fresh copy of
the lane tree (`cp -a corpus/` + `SKILL.md`, plus a stub entry file) reproduces the change with no
other input:

```
$ bash /home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --file <copy>/corpus/SOURCES.md --today 2026-10-27
file	ok	<copy>/corpus/SOURCES.md
exit=0        # 151 rows, 20 pre-existing W04 lines suppressed
```

and the substituted line equals the line this seat built independently in its lane mirror
(`applied line equals earlier scratch line: True`).

## Contract gates measured against the change

### 1. Append-only gate (`verifiers/check_sources_append_only.py`) — permitted cell, no new breach

Fixture A, two-commit repo holding only this change (clean history, so the arm is not masked by
the lane's existing breaches):

```
$ python3 -B verifiers/check_sources_append_only.py --repo <fixture> --rev <base>..HEAD
log  52e5c5276 S213 used-by: …cts-round70.md -> …cts-round70.md, corpus/k…
sources append-only rows clean: 1 commits scanned, 0 protected-cell changes
exit=0
```

Fixture B, negative control, same repo with the S213 `teaches` cell altered:

```
breach 0eac83850 S210 teaches: …lidation split -> …lidation split TAMPER
sources append-only breach 1 change(s) in 1 of 2 commits
exit=1
```

Lane context (clone of the lane at `4de12b6` + one commit adding this patch):

```
base 4de12b61f: sources append-only breach 18 change(s) in 8 of 44 commits      exit=1
+ used-by:      sources append-only breach 18 change(s) in 8 of 45 commits      exit=1
                log  bccb2972e S213 used-by: …cts-round70.md -> …cts-round70.md, corpus/k…
```

Net: **0 new breaches, +1 permitted-cell log line.** The gate is already red at base with 18
in-place edits in 8 commits (pre-existing: `S028`, `S050`, `S120`, `S201`, `S207`, `S209`, `S210`
…), so no-green-to-red flip is available or caused here.

### 2. `verifiers/check_skill_evals_v2.py` — the append costs one finding (CONFLICT, see below)

```
$ python3 -B verifiers/check_skill_evals_v2.py --repo <clone> --rev b7f13f4
skill eval artefacts verified 2 of 10                                            exit=1
$ python3 -B verifiers/check_skill_evals_v2.py --repo <clone> --rev 4de12b6
skill eval artefacts verified 2 of 10                                            exit=1
$ # after committing only the used-by append
$ python3 -B verifiers/check_skill_evals_v2.py --repo <clone> --rev HEAD
skill eval artefacts verified 1 of 10                                            exit=1
  F7: S213 used-by != corpus/knowledge/skill-eval-artefacts-round70.md (exact match required)
```

Code cause: `verifiers/check_skill_evals_v2.py:289` — `if row[10].strip() != ENTRY:` — exact
string equality, documented at `:21` as *"``used-by`` cell to be EXACTLY the entry path (no
substring, no ``not <entry>``)"*. `F7` of `corpus/knowledge/skill-eval-artefacts-round70.md`
cites `S213`, so the row is in scope. This counter is **already red at base** (2 of 10, exit 1, and
one of its two findings is a pre-existing `SKILL.md` line finding), so the append moves 2→1, not
green→red; it is not named in the round-76 base battery or the no-harm battery list.

### 3. `verifiers/check_spec_craft.py` (green at base, 3/3) — unaffected

It asserts membership, not equality — `:691 if ENTRY not in listed` over `row[10].split(",")` — and
its `ENTRY`/`SID_OF` set is S223/S224/S225, which this patch does not touch. Membership is also
what C1 conjunct (e) asks for ("row S213's `used-by` **lists** …"), so this patch satisfies the
letter of (e).

## Conflicts with the frozen contract (reported, not resolved here)

**CF-1 — C1 conjunct (a) demands an anchor-cell edit that the touch list forbids and rule 2
forbids in place.** Plan text, verbatim (`plans/round-76.md:27`): *"… the optimizing-descriptions
digest equals the digest recorded in the S213 row's anchor update."* Plan touch list, verbatim:
*"`corpus/SOURCES.md` (S213 used-by cell only)"*.

The S213 anchor cell today carries **no sha256** — it names the subsection, `upstream commit
69ef37e9…`, `(equal to main on 2026-10-25, git ls-remote)` and the 17-word quote. Neither S212 nor
S213 carries a digest (`awk` over lines 152–153: `NO sha256` for both), although
`check_skill_evals_v2.py:36` claims the anchors carry *"fetched sha256 in the anchor cell"* — that
docstring overstates what the code enforces (`A9` only requires the token `upstream commit`).

So (a) cannot be reached through `used-by` alone. The digest both fetch seats agree on
(`B03SnapshotFetch`, `B26FetchRecheck`): **`7cc54fbb6abbcf08c33e7b320fd01a1fb9696426270da3b588a398d243bfd837`**,
13 403 B, HTTP 200, `.md` route only (the extensionless URL serves a 344 074 B HTML body,
sha256 `21f902dc…`, and must not be used). An anchor-cell append of that digest is an **in-place
edit of a protected cell**:

```
fixture: S213 anchor cell gets "; fetched sha256 7cc54fbb… (2026-10-27, 13 403 B)"
$ python3 -B verifiers/check_sources_append_only.py --repo <fixture> --rev HEAD
breach 9fe719c4b S213 anchor: …)." (17 words) -> …)." (17 words); fetched sha256 7cc54fbb6abbc…
sources append-only breach 1 change(s) in 1 of 1 commits
exit=1
```

Precedent cuts both ways: `bf98d28` (r71) edited **S209 and S210 anchor cells in place** to add
`upstream commit 69ef37e…`, and the gate still reports those two commits as breaches today
(`breach bf98d2837 S209 anchor: …` / `S210 anchor: …`). `CORPUS.md:117-118` instead routes
corrections through a new row: *"A correction is a new row whose `teaches` opens `supersedes S0NN —`."*

Options, for the L1 to choose (each has a cost, none is free):
- (i) Widen the touch list to the anchor cell and accept +1 append-only breach (18→19) plus a
  lesson record of the in-place anchor edit — consistent with the r71 precedent, inconsistent with
  rule 2.
- (ii) Add a superseding row `S2xx` (`teaches` opening `supersedes S213 —`) carrying the digest, and
  leave S213's anchor untouched — rule-2 clean, but then C1(e) "row S213's used-by lists the entry"
  and C1(a) "the digest recorded in the S213 row's anchor" must be re-read as pointing at S2xx.
  Note `check_skill_evals_v2` would then also require the *new* row's `used-by` to equal its own
  ENTRY if the entry ever cites S2xx (it does not today).
- (iii) Have `verifiers/check_desc_craft.py` (not yet written at the time of this draft:
  `ls verifiers/check_desc_craft.py` → *No such file or directory*) read the digest from the
  snapshot manifest/pinned table only, and drop the anchor clause from (a). This keeps the touch
  list and rule 2 intact, at the price of softening the frozen sentence — a plan amendment, so it
  is an L1 act, not a seat act.

**CF-2 — two counters disagree about the same cell.** C1(e) requires S213 `used-by` to *list* the
new entry; `check_skill_evals_v2.py:289` requires it to *equal* the r70 entry exactly. Both cannot
hold. Options: relax `check_skill_evals_v2` to membership (touches a verifier outside the touch
list and forces its `SELF_SHA` re-pin), or accept the `F7` finding as a declared, pre-existing red
that the append deepens (2 of 10 → 1 of 10). My draft takes the second path, because it changes no
file the touch list does not name.

## Lesson line for the r76 `## Status changes` (conjunct (e) evidence)

Format follows `corpus/lessons/round-66.md:36`:

```
- S213 `used-by` old -> new: `corpus/knowledge/skill-eval-artefacts-round70.md` -> `corpus/knowledge/skill-eval-artefacts-round70.md, corpus/knowledge/description-craft-round76.md`. The entry `corpus/knowledge/description-craft-round76.md` is the new consumer (C1). `status` remains `mined`; `recheck` remains `90d`; every other cell is unchanged (append-only gate: `log S213 used-by`, 0 new breaches).
```

## Adjacent finding for the C2/R2 receipt owner (outside this patch)

`plans/round-76.md` § Base battery reports "corpus integrity exit 0; corpus independent exit 0" at
`b7f13f4`; neither reproduces today, in a clean clone at that rev or on the lane: integrity is
4 DRIFTs / exit 1 (and still `DRIFT corpus.index.unindexed 1` under `--no-baseline`), independent
is `DRIFT corpus.index.unindexed 1` / exit 1 — `lessons/round-75-verifier-spotcheck.md` landed
without an index row, the same recurring cause recorded at `corpus/README.md:138,141,144`. Measured
fix: one `corpus/README.md` row for that lesson (already in the touch list) makes
`verify_corpus_integrity.py --no-baseline --json` and `verify_corpus_independent.py --json` exit 0;
default-mode integrity still needs the baseline re-record (`tracked_files 145 != 144`,
`report_total 101 != 99`, `commit_total 44 != 43`). Detail and commands: `w1/B14SourcesUpdate.md § F6`.

## What this seat did not do
- Did not run `verifiers/check_desc_craft.py` — the file does not exist yet in the lane
  (`ls` → No such file). The `used-by` half of conjunct (e) is therefore verified against the
  parser that the counter must itself use (`sources-census.sh`) and against the observed
  membership convention of `check_spec_craft.py`, not against the counter's own bytes.
- Did not touch `verifiers/check_skill_evals_v2.py`, `check_spec_craft.py`, the anchor cell, or any
  lane file. Nothing installed; no git/jj writes outside `/fast/scratch/`.
