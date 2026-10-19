# Independent corpus derivation — round 12

Round 12's axis move is **consistency**: the corpus verdicts stop being author-only.
`AXES.md`'s band 10 asks for *repeated non-author verification in the opposite
direction*; round 11 supplied one non-author act (a cold run of the author's script
plus its own spot-checks), and running someone else's instrument a second time is not
a second derivation. So this round the **verdict classes are re-derived from the files
alone by an instrument that did not author the first one**, the two are compared
check-for-check, and every disagreement is adjudicated here rather than explained away.

Two artifacts, one verdict:

| | author's instrument | independent derivation |
|---|---|---|
| file | `verifiers/verify_corpus_integrity.py` | `verifiers/verify_corpus_independent.py` |
| sha256 | `a32da4a4224e9810549016ec3000583f3068bf552d7a92b0666114c32476dd56` (final; `747b1226…` before the index-scope repair of §4b, `391a54f4…` as landed at `4dd7753`) | `430fe289feb07eff638e33326ac17554f19d7e0579363f9c90137e571671f0e5` |
| author | L1 / round-11 lanes | L2 lane `ExecIndependentVerifier` — did not author the other script, **did not read its source**, and was given the class spec only |
| self-test | `--self-test` → `0 failure(s) over 88 assertions` | `--self-test` → `52 assertions, 0 failures` |
| exits | 0 agree · 1 drift · 2 environment unreadable · 3 no baseline | 0 clean · 1 drift · 2 environment unreadable (no baseline by construction) |
| wording re-read off the files | `git ls-files`, `os.path.exists`, `git cat-file -e` | its own tokenizer and counting code; same sources of truth |

Evidence kept by the derivation lane: `/tmp/round12/ExecIndependentVerifier/{run-live.txt,run-live.json,run-w0.txt,run-w0.json,selftest.txt,compare.md,METHOD.md,hermetic-no-host-ufo.txt}`
(`compare.md` is reproduced in structure below; scratch is not evidence — every number
here is re-runnable from the repo plus a clone, see §7).

## 1. The claim this round lands

*Live tree* (`corpus/` at `7d15407` plus the round-12 edits): both instruments print the
same nine numbers and both exit 0.

*World W0* = `git clone --no-hardlinks` + `checkout --detach d49dfa5` (the pre-round-11
tree; both scripts copied in, since the verifier is untracked there): both instruments
exit 1 and both name the **same ten dead pointer sites** and the **same one non-hash
commit site**.

That pair — agreement in the red direction and in the green direction, on two
independently written instruments — is the move. The author's instrument is no longer
its own only witness.

## 2. Agreement, check for check

Live tree (author `PASS`/`DRIFT` vs independent `clean`/`violation`):

| class | author observed | independent observed | agree |
|---|---:|---:|---|
| `corpus.index.tracked_files` | 39 | 39 | yes |
| `corpus.index.unindexed` | 0 | 0 | yes |
| `corpus.index.stale_patterns` | 0 | 0 | yes |
| `corpus.index.missing_paths` | 0 | 0 | yes |
| `corpus.pointers.report_total` | 25 | 25 | yes |
| `corpus.pointers.report_dead` | 0 | 0 | yes |
| `corpus.pointers.commit_total` | 23 | 23 | yes |
| `corpus.pointers.commit_unresolvable` | 0 | 0 | yes |
| `corpus.pointers.commit_nonhash` | 0 | 0 | yes |
| **exit** | **0** | **0** | yes |

Raw populations agree too: pointer shapes `{absolute 24, tilde 1, relative 0, bare 0}`,
`report_pointers_excluded` 8 with **identical sites**, `commit_quoted_excluded` 1 with the
identical site (`corpus/lessons/round-6-aggregator-audit.md:45`), `index_patterns` 43
= the independent's `index_tokens` 37 with 0 tokens outside the coverage-map section.

W0 `d49dfa5`: both instruments exit 1; both report `tracked_files` 33,
`report_total` 19, `report_dead` 10, `commit_total` 18 hex, `commit_nonhash` 1,
`unresolvable` 0, shapes `{relative 9, absolute 8, tilde 1, bare 1}`, and the identical
dead sites (`corpus/README.md:23,24,25,26,27,28,36,37,38` + `corpus/lessons/round-3.md:5`)
and non-hash site (`corpus/README.md:38: round-10`).

The comparison was re-run in **three live tree states** (as sibling lanes landed prose
edits; corpus manifests `632a6b0e…`, `bc66c2a6…`, `d4c9eaa6…`) — every number identical
in all three, so the agreement is not a lucky snapshot.

## 3. Adjudications — seven definitional differences, one shared property

None of these is a verdict disagreement; each is named because a comparison that hides
its own boundary conditions is the thing this round exists to prevent.

1. **`commit_total` semantics.** The author's key counts *hex-shaped* citations (22 live /
   18 W0) — the docstring says so. The independent publishes a wider `commit_total`
   (22 live / 19 W0, i.e. every in-scope citation after the quoted-context rule) plus
   `commit_hex_total` (22/18) and `commit_candidates` (23/20). **Adjudicated: same
   population, different key name.** The author's name is ambiguous enough to mislead, so
   the baseline note now states the exact scope (§4c); no code change — renaming a key
   that the baseline and three artifacts cite would cost more than it explains.
2. **Counting-mode gating.** The author's `equal` ids compare a baseline, so on W0 they
   read `DRIFT` for 33≠36, 19≠24, 18≠22 — baseline-relative drift, not corpus defects;
   the independent is baseline-free, so those three read `observe`. **Adjudicated:
   different gate sets, same corpus verdict** (both exit 1 for `report_dead`+`commit_nonhash`).
   The author's `7/9 checks pass` and the independent's `6 clean violation classes` are
   both true statements about different questions.
3. **Index scan scope.** The specification binds the census to the coverage-map table;
   the author's code read column 2 of *any* table row in `corpus/README.md` while its
   docstring claimed the coverage map. Measured difference today: **0** tokens. This is a
   claim/behaviour gap with a latent failure mode (a future README table about something
   else moving `stale_patterns`/`missing_paths`), so the code was scoped to the section —
   **§4b**.
4. **Glob-bearing pointer token.** `.ufo/reports/round-*/x.md` cannot match the author's
   regex at all (its round segment must be digits), so it is invisible rather than
   excluded-with-reason; the independent matches it and files it as `glob`. **Adjudicated:
   bookkeeping only** (0 live, 0 at W0); named so nobody reads the author's silence as a
   pass.
5. **Exclusion-reason annotations** (`[angle-bracket]`/`[glob]`/`[whitespace]`/`[dotdot-after-hops]`)
   and the `(quoted meta-finding)` suffix: same sites, richer text in the independent.
   Cosmetic.
6. **Quoted-context bookkeeping:** identical site and token; annotation text differs.
   Cosmetic.
7. **Raw-candidate counters** (`report_candidates` 32/20, `commit_candidates` 23/20) exist
   only in the independent; summing the author's published parts reproduces both
   (24+8+0 = 32; 19+1+0 = 20; 22+1 = 23; 18+1+1 = 20). Cosmetic.

**Shared property, measured on both (the strongest carried gap):** pointer resolution is
host-anchored, so a clone's green verdict is **not hermetic**. Hidden behind a private
tmpfs over the host `.ufo` (`unshare -rm`), the W1 clone goes from 0 dead to
**24/24 dead** and W0 from 10 to **19/19 dead** — *identically* in both instruments
(`hermetic-no-host-ufo.txt`). Two instruments moving together is a second agreement; it
also means "green on a clone" only means something on a host that carries the reports.
24 of the 25 checked pointers are host-absolute.

## 3b. Fault harness — class fidelity, one shared blind spot, one falsified equivalence

`verifiers/fault_injection_corpus.sh` (sha256 `9bc80ae61cea…`, `--repo/--keep-worlds/--self-test`,
per-fault `--no-hardlinks` clones, JSON-only assertions, exit 0 all-pass / 1 failure / 2
environment) replaced round 11's `/tmp` fault table, which could not be re-run after the
scratch wipe. Ten fault classes, each asserted against **both** instruments
(`/tmp/round12/LabratFaults/faults.md`; the row pins the sha of the script copy executed):

| fault | must fire | fired class (both instruments) |
|---|---|---|
| (a) dead in-grammar pointer | yes | `report_dead` (baseline mode also `report_total`) |
| (b) non-hash commit token | yes | `commit_nonhash` |
| (c) 7-hex unresolvable citation | yes | `commit_unresolvable` |
| (d1) index row naming an absent file | yes | `stale_patterns` (+`missing_paths`) |
| (d2) index row naming an untracked file | yes | `stale_patterns` only |
| (e) new tracked file with no index row | yes | `unindexed` |
| (f) pointer moved out of the grammar | **no class fires** (see below) | none under `--no-baseline`; `report_total` 24→23 in baseline mode |
| (g) equivalent mutation (prose only) | no | none — no false positive in either instrument |
| (h) quoted absent-path pointer | no | `report_pointers_quoted` 0→1, `report_total` stays 24 |

Row (h) is the round's own repair exercised in a real world: the documented quoted-context
idiom now fires exactly as documented (it also answers the open question left in
`verifiers/corpus-baseline.json`).

**The shared blind spot (f), adjudicated.** A pointer moved out of the
`.ufo/reports/round-N/` grammar — e.g. into `.ufo/round-4/` — stops being a pointer: both
tokenizers drop it, so neither flags it as dead. It is *not* a resolution failure (fault (a)
proves `report_dead` fires on any in-grammar dead token, and `test -e` confirmed the old
path existed and the new one does not before planting); it is a class boundary. The
detector that does notice is the `equal`-mode count: `report_total` moves 24 → 23, and only
in default (baseline) mode — under `--no-baseline` both instruments exit 0. **Consequence
adopted here: default mode is the safe invocation for this class**, and the round's §7
reproduce block keeps the clone runs labelled by mode.

This **names a boundary round 11's sentence does not distinguish** — the round-12 reviewer
(RF-3) was right to narrow the claim: `corpus/knowledge/corpus-integrity-round11.md`'s
"planted faults and equivalent mutants" section lists *"a pointer-shape-only rewrite ≡
no-op"*, and for an **in-grammar** rewrite (relative → absolute, say) that reading is
correct — the token stays a promise, the checked population does not move, and no zero-class
can fire. Fault (f) is a different case: a rewrite that leaves the grammar. The round-11
sentence is therefore **incomplete, not false**: it should read "a pointer-shape-only
rewrite that stays inside the `.ufo/reports/round-N/` grammar is a no-op; one that leaves
the grammar removes the token from the checked population and is visible only through the
`equal`-mode count detector." The correction is recorded here rather than rewritten into the
round-11 file (per-round records keep their round's text; the same rule the box-count sweep
of §5 follows).

## 4. Repairs the derivation forced

### (a) The documented quoted-pointer rule could not fire

The author's docstring documents a quoted-context rule for report pointers, but the
tokenizer admitted `"` into a token: a span `"…/round-99/kotoba.md"` matched starting *at*
the quote, so `inside_quotes` counted zero quotes before the span and the rule was dead
code. The comparison lane's reading of the spec (a quoted token is context) is what made
the mismatch visible. Fixture worlds (clone of HEAD, two lines appended to a tracked
corpus file):

```bash
# pre-fix script, both fixture lines present
report_total 26   dead 2   # the QUOTED token is reported as a dead promise
# repaired script, both fixture lines present
report_total 25   dead 1   quoted 1
# repaired script, quoted line only
report_dead=0/25 … 9/9 checks pass   → exit=0
```

Landed: the pointer tokenizer's char classes exclude `"`; `citation_findings` returns
`report_pointers_quoted[_detail]`; the collector aggregates and prints them; `--self-test`
pins the idiom (span excludes the quote, quoted = context, the same token unquoted is still
checked and still dead). Live effect: none today (0 quoted tokens), which is why the
fixture carries the proof.

### (b) The index census read more of `README.md` than it claimed

Landed: the census now reads only the `## Coverage map` section (the next `## ` heading
ends it), which is what its docstring always said. Live effect: no live count moved
(`index_patterns` was 37 before the repair and the nine verdicts are unchanged) — the
fixture pins the difference instead: a column-2
token in a table *outside* the section now produces no pattern and no finding
(`index/outside-coverage-map-ignored`, `index/outside-coverage-map-no-finding`), and the
independent instrument's counter for exactly that quantity
(`index_tokens_outside_coverage_map`) is 0 in both worlds.

### (c) The baseline names its scope

`verifiers/corpus-baseline.json`'s note now states that `commit_total` counts hex-shaped
citations only and that a non-hash token is carried by `commit_nonhash` — the ambiguity
adjudication 1 rests on is now written where the number is compared.

## 5. The claim-census pass (why this is a consistency move, not a plumbing move)

The same round ran a census of **every counting claim** in this repo's artifacts about the
corpus and the verifiers (84 rows, `/tmp/round12/ScoutClaimCensus/census.md`; executed
commands, per-row verdicts). It found, and this round repaired:

- **24 stale numbers** — all of them count moves caused by the round-11 landing (33→36
  tracked files, 19→25 checked pointers, 21→23 citations, 1→8 excluded sites, 18/1→24/1
  absolute/tilde split, 80→86 self-test assertions). Repaired in the artifact's check
  table and its green-after block, `SCORECARD.md`, `corpus/README.md` and
  `corpus/lessons/round-11.md` — with the landed commands beside them.
- **4 claims already false at HEAD.** (i) `corpus/README.md`'s round-11 row claimed a
  `LOG.md` round-11 entry that did not exist (the round was cut before logging) → the entry
  is now written; (ii) the cold-run record claimed the shipped script was byte-identical to
  a pre-commit sha → replaced by the reachability qualifier and the real sha chain;
  (iii) and (iv) two counting commands that cannot express the class they name — the
  cold-run record's mid-landing capture (now labelled historical) and **`SHONEN.md`'s
  checklist `awk`, which printed an empty line while claiming to produce `13/9/9/8`** — the
  fourth instance of the round-11 defect class, in the file the round-6 audit used that
  same expression to correct. `SHONEN.md` now carries a command that reproduces the
  numbers (verified by executing the text as written).
- **9 unexpressible claims** — records whose object no longer exists (two pre-commit
  sha256s, the pinned mid-landing capture instants, the round-11 planted-fault log that
  lived in `/tmp/round11/` and was wiped). Each is now labelled rather than left looking
  reproducible, and the fault-log class is closed by committing a harness
  (`verifiers/fault_injection_corpus.sh`).
- **1 disagreement** — `SCORECARD.md`'s round-10 row claimed "4 unindexed files" with no
  recorded command; a brace-aware `comm` reconstruction at `e997d45` yields 7. The row now
  says which number has no command rather than presenting it as measured.

## 6. What is still not verified

**Residuals the round-12 critic named, kept as residuals (not waved away).**

- **Agreement falsifies implementations, never specs.** A third same-spec instrument would
  inherit the class spec's *scope choices* (no code-fence model, line-scoped quoting, the
  `LOG.md`/`SCORECARD.md`/`SKILL.md` exclusion, host-anchored resolution) and could still
  agree check-for-check. The minimal extra act — derive an adversarial fixture from each
  *promise* in the spec and run **both** instruments on it — is what §4(a)/(b) did for two
  idioms and what `verifiers/fault_injection_corpus.sh` does for the fault classes; a
  derivation-owned *expected census* (the baseline's job, still authorial) is the unfinished
  half of the reversal.
- **Authorship is attested, not verifiable.** "Did not author / did not read its source" is
  a lane claim; nothing in-repo proves a negative about source reading. `[INFERENCE]` only:
  the two tokenizers' independent bugs (parity counting vs span containment) are unlikely
  from one authoring hand.

- **Hermeticity** (§3, shared): a clone's green verdict depends on the host's `.ufo` tree.
  Repo-relative pointers would fix it; 24 of 25 pointers are host-absolute, and the
  corpus has not been normalised.
- **`LOG.md`/`SCORECARD.md`/`SKILL.md` are outside both instruments' scope** (they scan
  tracked `corpus/*.md`): their pointers and citations are unchecked. The census walked
  them by hand this round; nothing asserts them next round.
- **`SKILL.md`'s 40 checklist boxes** (14/9/9/8 by section: `grep -c '^- \[ \]' SKILL.md`) are still only counted, never executed; the
  round-12 candidates for that ceiling are planned in
  `/tmp/round12/PlanRound13/plan.md` (not an in-repo artifact — carried, not claimed).
- **Neither instrument models code fences or multi-line quoting**: a path printed inside a
  captured output block counts as a promise (both instruments, identical behaviour). Three
  prose mentions in `cold-run-round11.md` are promises under this reading and would drop
  out under a backticked-only reading (24 → 21 live; the red verdict at W0 is unaffected).
  Adjacent spec-scoped boundaries, measured on both: a quoted span that opens on one line
  and closes on the next is still checked (the rule is line-scoped), and single-quoted
  tokens are never context (the docstring promises double quotes only).
- **The independent instrument's own correctness rests on its self-test and this
  comparison** — a third party could falsify it; §7 is how.

## 7. Reproduce

```bash
cd <repo>                                   # kotoba-shokunin
python3 verifiers/verify_corpus_integrity.py            ; echo "author exit=$?"      # 9/9, exit 0
python3 verifiers/verify_corpus_independent.py          ; echo "independent exit=$?" # clean, exit 0
python3 verifiers/verify_corpus_integrity.py --self-test ; echo "author self-test=$?"      # 88 assertions, 0 failures
python3 verifiers/verify_corpus_independent.py --self-test ; echo "independent self-test=$?" # 52 assertions, 0 failures

W0=$(mktemp -d)/w0 && git clone -q --no-hardlinks . "$W0" && git -C "$W0" checkout -q --detach d49dfa5
cp verifiers/verify_corpus_integrity.py verifiers/corpus-baseline.json verifiers/verify_corpus_independent.py "$W0/verifiers/"
python3 "$W0/verifiers/verify_corpus_integrity.py"   --repo "$W0" --no-baseline ; echo "author@W0=$?"       # report_dead=10/19, nonhash=1, exit 1
python3 "$W0/verifiers/verify_corpus_independent.py" --repo "$W0"                ; echo "independent@W0=$?"  # same two classes, exit 1
```

The round-11 cold run (`corpus/knowledge/cold-run-round11.md`) is the *first* non-author
act; this file is the second, and the direction is reversed: there, a non-author checked
the author's numbers; here, a non-author derived the verdicts and the author's instrument
is the thing that had to agree.
## Round-24 erratum (append-only)

Two corrections, both host-conditional, from scouts R4/R5 (round 22) and E3 (round 24):

- The W0 block's `report_dead=10/19` at `d49dfa5` reads **19/19** on the current host — the
  recorded 10 was the round-12 host's lowercase `/home/vgpnk/projects` base resolving 9
  host-anchored tokens (reconstructed byte-exactly in `unshare -rm`; LOG records that base
  as now absent). Both instruments agree on the 19-site dead set and identical shapes.
- §2's `index_patterns 43 = index_tokens 37` glues two tree states: `43` is the `633859f`
  live tree, `37` is `7d15407`; the correct pairing at either tree is `43 = 43`.
