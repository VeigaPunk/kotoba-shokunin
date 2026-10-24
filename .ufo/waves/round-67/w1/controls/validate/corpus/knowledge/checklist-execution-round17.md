# Checklist execution, round 17 — governance paths and literal-tilde heredocs

**Lane:** kotoba-shokunin. **Round:** 17. **Axis move:** `calibration`
(8.0 → 8.5).

## Why this was the axis move

`SCORECARD.md` began the round with three rows tied at the floor: `freshness`,
`calibration`, and `adjacency`, all 8.0. The pre-registered round-16 plan already
contained a calibration-shaped defect: root governance files (`LOG.md` and
`SCORECARD.md`) carried path claims that no instrument checked. `adjacency` was
blocked on sibling-owned repairs, and `freshness` already had six green
instruments without a newly falsified class. The round therefore took planned
item 4, governance citation resolution, and recorded the tie rather than
pretending `operability` remained the floor.

A second calibration repair lands in the same parser because the round-16
planner refuted the recorded `M36` fixture: bash treats the `~` in `<<~EOF` as
part of the delimiter word. The old fixture closed with a delimiter that bash
would not accept, so it did not isolate the claimed over-catch.

## Scope fence

This move changes:

- `verifiers/verify_skill_checklist.py` — one repo-level governance check, the
  `<<~WORD` parser correction, explicit `--repo` normalization, and self-tests;
- three fixture pairs under `verifiers/fixtures/checklist/`;
- four historical/dead-example path mentions in `LOG.md`, marked with the
  existing same-line double-quote meta-finding idiom;
- one ambiguous sibling citation in `SCORECARD.md`, repaired by naming the
  sibling base; and
- this evidence file, its `corpus/README.md` index row, `SKILL.md`, `LOG.md`, and
  `SCORECARD.md`.

It does **not** widen `verifiers/verify_corpus_integrity.py`: that instrument's
round-11 contract deliberately reads tracked `corpus/*.md` only. It does not
validate path contents, ownership, historical truth, commit pins, or line
anchors. It does not modify sibling repositories. It does not implement `M23`
(executable heredoc bodies) or the remaining 33 unexecuted checklist boxes.

## Falsifiable claim

> At the landed round-17 tree, the checklist instrument exposes ten checks.
> `governance.citation_resolves` examines repo-root `LOG.md` and `SCORECARD.md`
> whenever the target is that repo's own `SKILL.md`: every non-schematic,
> non-meta, repo-rooted backticked path resolves at HEAD. Its final live
> population is 134 extracted occurrences: 125 checked and resolving, six
> same-line quoted meta-findings, and three schematics. A planted unquoted dead path fails and is
> named. Separately, `<<~EOF` opens a heredoc whose delimiter is `~EOF`; its body
> is opaque to command extraction, and scanning resumes only after `~EOF`.

Falsifiers are concrete:

1. add an unquoted `` `corpus/absent.md` `` to either governance file — the new
   check must fail and name the file and line;
2. move that token inside same-line double quotes — it must be counted as a
   meta-finding, not checked;
3. split those quotes across lines — the token must remain checked, preventing
   unrelated Markdown quote parity from suppressing subjects;
4. run the verifier with `--repo .` on a skill citing a valid parent path — the
   result must equal an absolute-root run;
5. put `nonexistent-binary-xyz` inside a `<<~EOF` body — it must not become a
   command subject; and
6. put a dead `cat corpus/absent.md` after the real `~EOF` terminator — it must
   fail, proving the parser did not swallow the tail.

## Pre-state at `d85982d`

### Governance paths: unmeasured by any live gate

The round-16 `trigger.citation_resolves` predicate was run directly against the
two governance files before adding the repo-level check:

```text
$ python3 verifiers/verify_skill_checklist.py --skill LOG.md \
    --check trigger.citation_resolves
FAIL trigger.citation_resolves: evaluated 74 — … (+2 more)
# six dead occurrences; exit 1

$ python3 verifiers/verify_skill_checklist.py --skill SCORECARD.md \
    --check trigger.citation_resolves
FAIL trigger.citation_resolves: evaluated 51 —
  line 34: 'corpus/instruments/resolve.py' does not resolve …;
  line 82: '.ufo/reports/round-N/kotoba.md' does not resolve …
# two dead occurrences; exit 1
```

Independent reviewer `R17Review` reimplemented the extractor without importing
the verifier and reproduced exactly **74 / 6** and **51 / 2**. Scout `R17Gov`
classified all eight occurrences:

| Class | Occurrences | Sites | Landed disposition |
|---|---:|---|---|
| schematic ellipsis | 1 | `LOG.md` old `../.ufo/…` class | syntactically excluded and counted |
| literal-`N` template | 2 | `round-N` in LOG/SCORECARD | syntactically excluded and counted |
| historical repair record | 3 | `.ufo/reports`, `.ufo/prompts/` ×2 | same-line quoted meta-finding |
| deliberate dead example | 1 | `cat corpus/nope.md` | same-line quoted meta-finding |
| foreign sibling pointer | 1 | kasegi `corpus/instruments/resolve.py` | base named explicitly; `anchorcheck.py` named too |

The explicit sibling forms
`../kasegi-shokunin/corpus/instruments/{resolve,anchorcheck}.py` both resolve
under the existing bounded-hop rule. Connector `R17Connector` also found no
sibling verifier or script that checks `LOG.md`/`SCORECARD.md`, so this did not
establish a second fleet convention.

### `M36`: body lines were false command subjects

The three new fixtures were run against the pre-patch verifier. The clean,
correctly terminated case failed solely on a body token:

```text
FAIL trigger.command_binary_resolves: evaluated 4 — 5 segments;
line 16: 'nonexistent-binary-xyz' … does not resolve
```

The dead-tail case reported both the phantom body token and the real tail:

```text
FAIL … evaluated 4 — 5 segments;
line 16: 'nonexistent-binary-xyz' …;
line 18: 'corpus/absent-round17.md' … does not resolve
```

The deliberately mis-terminated case (`<<~EOF`, bare `EOF`) reported the body,
the false terminator, and the remaining body as commands. Bash itself warns
that it reached end-of-file while looking for `~EOF`; therefore the correct
post-fix verdict is PASS with only the opener as a subject, not a failure on the
line after bare `EOF`. This corrects the round-16 plan's inherited wording.

### Relative `--repo` changed bounded-hop verdicts

A red-before probe used `--repo .`. The CLI retained `Path('.')` instead of
normalizing it; `Path('.').parent` is still `.`, so valid `../` citations were
resolved from the wrong base. The landed CLI calls `.resolve()` on an explicit
repo path. A hermetic self-test runs from a child directory with a valid
`../shared/live.md` and requires PASS.

## Landed rule

### Governance extraction and resolution

`governance.citation_resolves` reuses the round-16 extractor and bounded
resolver. It runs only when the target is `<repo>/SKILL.md`, then reads the
explicit pair `LOG.md`, `SCORECARD.md` from that repo root.

A subject is a whitespace-separated word inside backticks, after fragment and
punctuation/line-anchor dressing is removed, rooted in the closed set
`corpus/`, `verifiers/`, `opencode/`, `.ufo/`, or a leading `../` hop. Plain
subjects resolve from the repo root; leading hops are bounded to three and may
not contain a later `..` segment.

Two exclusions are explicit and counted:

- **quoted meta-finding:** the token is enclosed by double quotes that both
  open and close on that same line; and
- **schematic:** the token contains an ellipsis (`…` or `...`) or a literal
  `round-N` path segment.

The first implementation carried quote parity across the whole file. Its live
probe excluded **17** pre-existing path subjects, including ordinary live
artifacts on lines 266–329 of `LOG.md`; that proposal was falsified and removed
before landing. Same-line enclosure excludes the four repaired records plus the
two synthetic fixture-path findings quoted in this round's final LOG entry. The
self-test pins that a cross-line quote does not suppress a dead path.

The result after the round record itself enters the checked surface is:

| File | Checked | Quoted meta | Schematics | Dead checked |
|---|---:|---:|---:|---:|
| `LOG.md` | 74 | 6 | 2 | 0 |
| `SCORECARD.md` | 51 | 0 | 1 | 0 |
| **total** | **125** | **6** | **3** | **0** |

The raw final population is therefore 134. Before the final round record, the
scorecard repair added the fully based `anchorcheck.py` subject, making that
intermediate population 126 — one occurrence larger than the 125-subject
pre-state.

### Literal-tilde heredoc parsing

Bash probes by `R17Probe` establish:

- `cat <<~EOF` wants the exact terminator `~EOF`; bare `EOF` is body text;
- `<<-EOF` is a different operator that strips leading tabs only;
- `<<~'EOF'` also has delimiter `~EOF`, but it remains outside the minimal
  regex landed here; and
- the existing `stripped == heredoc_end` comparison works unchanged when the
  captured word includes `~`.

The minimal monotonic repair is:

```python
HEREDOC_RE = re.compile(r"<<-?\s*['\"]?(~?[A-Za-z_][A-Za-z0-9_]*)['\"]?")
```

A miss stays the old safe-direction over-catch; the patch does not introduce an
under-catch by stripping `~` from the captured delimiter. Three fixtures pin the
boundary:

| Fixture | Expected command verdict | Non-vacuity |
|---|---|---|
| `command-heredoc-tilde` | PASS, 3 subjects / 2 segments | live tail scanned; phantom body absent |
| `command-heredoc-tilde-dead` | FAIL, 3 subjects / 2 segments | dead tail named; phantom body absent |
| `command-heredoc-tilde-misterm` | PASS, 1 subject / 1 segment | bare `EOF` and remaining lines stay body |

## Landed changes

| Change | Evidence-bearing surface |
|---|---|
| Add tenth check `governance.citation_resolves` | `verifiers/verify_skill_checklist.py` |
| Normalize explicit `--repo` to an absolute path | same, hermetic parent-hop self-test |
| Add same-line quote + schematic extraction, counts, fail-closed zero-subject behavior | same, synthetic clean/dead/cross-line cases |
| Correct `HEREDOC_RE` without changing terminator comparison | same + three committed fixture pairs |
| Mark four dead-by-assertion records as same-line quoted meta-findings | `LOG.md` |
| Name kasegi's sibling base for both prior-art scripts | `SCORECARD.md` |
| Update ten-check description while keeping `SKILL.md` at 599/600 lines | `SKILL.md` |

The verifier sha256 moved from `c55a3f9f382ac02d9805697944f864d920ab4264063c90ef5f7253664337f63b`
at `d85982d` to
`02ccf1b310f7910502f7938d24eb1cfcabe2c521ec42b7ce6420f1869af8df27`
after the landed code changes.

## Landed verification

```text
$ python3 verifiers/verify_skill_checklist.py
PASS checklist.box_map_complete: evaluated 41 — 41 boxes mapped (8 executed, 0 delegated, 33 unexecuted)
PASS trigger.frontmatter_parses: evaluated 4
PASS trigger.name_directory: evaluated 1
PASS trigger.literal_trigger_string: evaluated 1
PASS trigger.anti_trigger_clause: evaluated 1
PASS trigger.line_budget: evaluated 599 — 599 lines within budget 600
PASS trigger.no_placeholder: evaluated 550
PASS trigger.command_binary_resolves: evaluated 19 — 15 segments
PASS trigger.citation_resolves: evaluated 42
PASS governance.citation_resolves: evaluated 125 — 125 resolve across 2 files; 6 quoted meta-findings, 3 schematics excluded
# exit 0

$ python3 verifiers/verify_skill_checklist.py --self-test
0 failure(s) over 1504 assertions
# exit 0

$ sha256sum verifiers/verify_skill_checklist.py
02ccf1b310f7910502f7938d24eb1cfcabe2c521ec42b7ce6420f1869af8df27  verifiers/verify_skill_checklist.py

$ wc -l SKILL.md
599 SKILL.md

$ find verifiers/fixtures/checklist -mindepth 1 -maxdepth 1 -type d | wc -l
71
```

## Integration drift found by the corpus gate

After the new knowledge file was staged, the required corpus observation found
an unrelated host-base drift rather than a baseline-only count move:

```text
tracked_files=47  report_total=32  report_dead=32
```

Every dead pointer used `/home/vgpnk/projects/shokunin/.ufo/reports/…`.
`/home/vgpnk/projects` is absent on this host; the observed report tree is
`/home/vgpnk/Projects/shokunin/.ufo/reports/`. The 32 checked pointer
occurrences across 16 corpus files were case-corrected without changing their
round or lane targets. This is an integration/freshness repair, not a second
scored axis move.

The baseline moves only the expected tracked-file count, 46 → 47; report and
commit populations remain 32 and 27:

```text
$ python3 verifiers/verify_corpus_integrity.py
corpus.index    tracked=47 unindexed=0 stale=0 missing=0
corpus.pointers report_dead=0/32 commit_total=27 unresolvable=0 nonhash=0
9/9 checks pass
# exit 0
```

## Adjudication — eleven L2 lanes

| Lane | Finding | Disposition |
|---|---|---|
| `R17Plan` | round-18 rank 1 is adjacency remeasurement: 225 sibling subjects and 14 current unresolved occurrences, up from the stale 10-count row; classify the four-token delta before scoring | adopted as next plan, not claimed as gain |
| `R17Gov` | reproduced 125 pre-state occurrences / 8 dead; weak prose-based exclusions could veto all 8 and make the check vacuous | only syntactic schemes excluded; other dead records repaired/marked explicitly |
| `R17Probe` | bash delimiter is literal `~EOF`; minimal `~?WORD` capture removes the phantom while retaining tail scanning | landed with three fixtures |
| `R17Critic` | raw HEAD existence conflates navigability with historical truth and corpus placement violates a deliberate scope fence | claim narrowed to navigability; corpus verifier unchanged |
| `R17Sentinel` | adversarial set includes quoted spans, deep hops, brace tokens, symlinks, and heredoc variants; also found whitespace-terminator overreach | core quote/hop/ellipsis cases pinned; remaining variants named below |
| `R17Revenger` | round 11 deliberately excluded non-corpus files; kasegi `resolve.py` strips anchors and `anchorcheck.py` handles pinned historical anchors | placement kept outside corpus verifier; prior art cited with explicit base |
| `R17Fixtures` | drafted three complete pairs; real bash refuted the requested FAIL for the bare-`EOF` case | fixtures landed with the corrected PASS reading |
| `R17Connector` | all siblings have LOG/SCORECARD but no sibling instrument checks them; explicit kasegi paths resolve | no cross-lane convention claimed; sibling base repaired |
| `R17Review` | independent extractor confirmed 74/6 + 51/2 and all eight contexts; refuted the assumption that `…` was already excluded | explicit ellipsis exclusion added and tested |
| `R17Mutate` | designed M42–M50; seven rows have planned witnesses, wrong-root and quoted-context rows required explicit fixtures/ceilings | relative-root and quoted-context witnesses landed; harness remains scratch, not claimed run |
| `R17YAGNI` | corpus grammar sees only 2+1 report pointers and 2+1 commits here (clean but vacuous); reusing the checklist predicate is the smallest non-duplicating option | option (b) landed; no third instrument |

Two L2 recommendations were deliberately not followed verbatim:

1. equal-mode pinning of the eight dead sites would preserve known broken
   navigation. The existing quoted-meta idiom plus explicit repairs gives a
   zero-dead checked population and retains excluded counts, while a synthetic
   dead subject proves the check can fail; and
2. file-level quote parity was proposed for wrapped prose, but the live probe
   suppressed 17 ordinary citations. Same-line enclosure is narrower and is
   already the corpus verifier's documented convention.

## Named ceilings

| Ceiling | Consequence |
|---|---|
| HEAD existence only | a live file may not support the sentence; a deleted historical file requires an explicit meta marker, not silent acceptance |
| closed root set | dead `docs/x.md` remains invisible; naming an external/sibling base is the mandated repair |
| same-line quotes only | a genuinely quoted meta-finding wrapped across lines remains checked; this is deliberate to avoid the 17-site over-exclusion |
| two schematic classes only | other prose templates need `<…>`, glob, `$VAR`, or a new reviewed class |
| symlinks | existence is checked; containment and referent type are not |
| anchors and pins | `file:NN[-MM]` dressing is stripped; line existence, symbols, and `@commit` are not proved |
| heredoc variants | `<<~'EOF'` and `<<\~EOF` still over-catch; a single trailing `~` no longer does (`<<EOF~` matches bash since round 30), multi-tilde delimiters were fixed at round 35 (`<<EOF~~` closes like bash; C1's 36-form battery 0 mismatches); misses stay the old safe direction |
| terminator whitespace | the scanner uses `strip()` while bash `<<-` strips tabs only and `<<~` strips nothing; space-indented terminators may close early in the model |
| executable heredocs | bodies passed to `bash`/`python` are opaque today; `M23` remains planned with a `cat` control |

## Band decision

**8.5 lands.** The previously manual governance surface is now checked on every
normal live run, all eight pre-state dead occurrences have an explicit
classification and disposition, the machine gate is non-vacuous in both
directions, and the M36 record now matches bash.

**9.0 is withheld.** The check proves navigability only; anchors, content, pins,
symlink containment, and historical validity remain named ceilings. All eleven
review lanes were dispatched by this lane, so they are author-side evidence
under the protocol rather than the independent non-author witness required for
the stronger reading.

## Next move

The round-17 planner ranks **adjacency remeasurement/routing** first for round
18: five sibling `SKILL.md` files, 225 extracted subjects, 14 currently
unresolved occurrences (2/1/5/1/5 by lane). The move earns nothing unless an
independent classification shows the four-occurrence delta over round 16 is not
placeholder/ellipsis noise and every real finding is routed without editing the
sibling-owned files.
