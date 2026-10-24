# ReviewS122Fit — S122 source-fit review (calibration, round 66)

Seat: leaf reviewer (read-only). No plan, claim, counter, threshold, row, receipt or
baseline was changed; the only write is this report.

## Revisions (pinned base vs measured tip)

- Pinned round-66 base: `11385e04e368c1e94ab1a5a89d7439033eb1f855` (plan, controls).
- Observed lane tip at review: `2a8eba56b3f9321b70c569fa2816d42237ca49a2`
  (`round-66 verifier spot-check (integrator, hyaku): non-author admit/reject`);
  lane tree had 8 uncommitted paths, which are the in-flight w1 seat reports.
- C2 receipts measured at `fc1b71e56fda86fefe672f2cae90a62318d34449`; I did not
  re-run the gates (main-agent verification), and cite the committed receipts.

## Method

- Re-opened the cited primary source live on 2026-10-24:
  `https://force11.org/info/software-citation-principles-published-2016/`
  (§6.7 "Unique identification"), and compared it with the committed row,
  snapshot, lesson Gate and knowledge entry.
- Read the assigned entry `corpus/knowledge/fleet-commit-resolution-round66.md`
  against the resolver it describes (`verifiers/verify_corpus_integrity.py`) and
  the counter it cites (`verifiers/check_r66_routed_repairs.py`).
- Ran one throwaway `/tmp` fixture (no lane bytes touched) that imports
  `check_d2` and scores a synthetic tree; read the independently run
  `MutC2NoFleetHop` report in this wave as corroborating data.
- No `lsp` device is exposed in this seat's tool inventory, so caller/definition
  facts were read directly from the verifier sources rather than through a
  language server. No text-grep substitution was used as semantic proof.

## Verdict

S122's identity is fit for admission: URL, authors, PeerJ identity, DOI, §6.7
anchor, verbatim 17-word quote, snapshot and used-by paths all check out, and
the entry contains **no affirmative permanence claim** — every durability
mention is a disclaimer. The defects are calibration defects in the words
around the source and in one evidence sentence:

- the source's recommendation is paraphrased with an inserted "durable" that
  narrows it to durability and drops its DOI-first rule and explicit fallback;
- the entry calls the local lookup an application of the paper's "version-context
  distinction", which the paper does not draw;
- the entry credits the routed counter with a mutation kill that the round's own
  mutation seat measured as **survived** (the behavioural kill is in the
  integrity self-test and gate, not D2).

The C2 frozen predicate (`2 of 2`) is not falsified by any of this; the remedy
is an erratum to the entry and the SOURCES `teaches` cell, routed to the
canonical planning/closure seat — never a score change from this reviewer.

## Findings by severity

### High

**H1 — `corpus/knowledge/fleet-commit-resolution-round66.md:11`: the counter
kill asserted for D2 is measured as a survivor.**

The entry says: "the r66 routed-repairs counter's no-fleet-hop mutant fails D2."

- `verifiers/check_r66_routed_repairs.py:78-97` (`check_d2`) is a committed-byte
  SUBSTRING predicate: `HOP_MARKER` (line 40), `def commit_resolves(`,
  `inside_code_span`, `commit_resolves(hex_id`. It never executes the resolver.
- The counter's self-test arm `kill/D2-no-fleet-hop` (line 235) is fed a whole
  replacement file (`def commit_resolves(hex_id): pass`, written at line 233),
  so it kills by removing the marker text, not by removing the fleet hop.
- My synthetic-tree check: a resolver with only the behavioural fallback removed
  and the marker/docstring kept scores `check_d2 == True`; the counter's
  whole-file fixture scores `False`.
- The wave's mutation seat measured the same result on committed mutant bytes:
  `.ufo/waves/round-66/w1/MutC2NoFleetHop.md` § Verdict records
  "r66 routed counter D2: SURVIVED" — `check_r66_routed_repairs.py --rev
  3089e87…` prints `2 of 2`, exit 0, while the behavioural detectors kill it
  (`commit-hop/fleet-fallback` FAIL, gate 9/9 → 8/9, `commit_unresolvable=2`).

Criterion fit: Q25/Q26 (a counter must fail on the content of the claimed
thing; a clause the counter does not turn on is not evidence) and Q31 (prose
describing a counter names only what its code reads). The sentence should
attribute the kill to `verify_corpus_integrity.py --self-test`
(`commit-hop/fleet-fallback`) and the gate's `commit_unresolvable`, and describe
D2 honestly as a committed-byte pin that a behaviour-only mutant survives. The
frozen C2 predicate is met either way: it requires the "integrity-source hop"
pin, which is what D2 is.

### Medium

**M1 — inserted "durable" misstates the paper's recommendation in three
committed places.**

The source sentence is: "there are a number of reasons that a commit reference
together with a repository URL is **not recommended for the purposes of software
citation**". The paper first recommends "the use of DOIs as the unique
identifier", and later explicitly permits the fallback: "falling back on a
combination of the repository URL and version number/commit hash would be an
appropriate way to cite the software used" when no DOI/version exists.

Committed paraphrases:

- `corpus/knowledge/fleet-commit-resolution-round66.md:1` — "The original paper
  states that a commit reference together with a repository URL is not
  recommended **as durable software citation**".
- `corpus/knowledge/fleet-commit-resolution-round66.md:9` — "The S122 source
  explicitly cautions against presenting a commit reference with its repository
  URL **as a durable software citation**".
- `corpus/SOURCES.md:133` teaches cell — "A commit reference with its repository
  URL is still not a recommended **durable** software citation; preserve
  repository context when checking local version evidence".

The inserted qualifier is not in the source. It turns a citation-scope
recommendation (DOI-first, commit+URL only as fallback) into a durability-only
caveat, so a reader can infer commit+URL is fine for non-durable citation. The
three reasons the paper gives (permanence, URL resolvability, preferred cite
point) and the DOI recommendation drop out; the teaches cell also puts a lane
instruction ("preserve repository context when checking local version
evidence") in the column that must state what the source teaches. The 17-word
quoted span in the lesson is verbatim; this is a paraphrase-fidelity defect,
not a quote defect (Q23 applies to the teaches cell; Q56's byte/quote rule is
not violated).

**M2 — `fleet-commit-resolution-round66.md:1`: "applies its version-context
distinction" attributes to S122 a distinction the paper does not draw.**

S122's object is a citation compound a citing author would write (repository URL
+ version/commit), judged against the principles of unique identification,
persistence and specificity. The gate's object is a backticked token in a local
Markdown file, resolved by `git cat-file -e <hex>^{commit}` against the lane
repository then `FLEET_ROOT` (`verify_corpus_integrity.py:591-603`). It never
reads a repository URL, never tests resolvability over a network, never tests
persistence, and cannot tell a preferred cite point from any other commit. So
S122 can bound what the gate's output may be called; it cannot support the
gate's lookup rule, and the paper's principle is not a "version-context
distinction". The entry's line 9 final clause ("the gate's scope is local
evidence integrity, not research citation policy") already states the correct
relationship, so line 1 contradicts the entry's own calibration. This is the
same drift as the plan's frozen source binding (see L4).

### Low

**L1 — `corpus/lessons/round-66.md:12`: "The excerpt and context are preserved"
overstates the snapshot's context.**

`.ufo/waves/round-66/snapshots/S122-excerpt.txt` preserves the single lead
sentence ending at the colon (plus URL/access metadata). The three enumerated
reasons, the DOI-first recommendation, and the fallback paragraph — the bytes
that scope the quoted recommendation — are absent. The file honestly labels
itself an excerpt, but the lesson's word "context" should be "the quoted
sentence", or the excerpt should carry the reasons and fallback. This is the
mechanism by which M1's "durable" qualifier survived review: the saved context
does not include the clauses that would have contradicted it.

**L2 — `corpus/lessons/round-66.md:12`: the "(17 words)" count carries no
`wc -w` command on that line or the next two (Q54).**

The count is correct: I ran
`printf '%s' 'a commit reference together with a repository URL is not recommended for the purposes of software citation' | wc -w` → `17`.
The evidence command is missing, so the number is not evidence of its own count
under Q54. (The non-author spot-check recounts it but does not add the command.)

**L3 — `fleet-commit-resolution-round66.md:7,9`: "configured fleet root" and
"two declared repositories" overstate configurability; the unresolved claim is
scoped to live citations only.**

`verify_corpus_integrity.py:125` is `FLEET_ROOT = Path("/home/vgpnk/Projects/shokunin")`,
a hardcoded absolute-path module constant, not a configuration surface; a
missing or non-repository fleet root reads `False` by design. Separately, "A
token present in neither repository stays unresolved" holds only for live
citations: a token inside matching quotes or a complete code span is excluded
before resolution (`citation_findings`, lines 522-531), which is the behaviour
the entry's own evidence sentence describes. No permanence claim is implied in
either case; this is scope wording.

**L4 — `plans/round-66.md:27` (frozen; record only, do not edit): the source
binding attributes an interpretation-context clause to S122.**

The plan says S122 "will support C2's scoped note that a commit hash is
version-specific evidence only when interpreted with its repository context,
not a durable software citation by itself." The paper does not state that a
hash requires repository context to identify a version, and does not use
"durable"; it says the repo-URL+commit compound is not recommended for citation
and permits it as a fallback. The plan is frozen before landing, so the
calibration task for the report is negative: do not restate that clause as
S122's teaching. The entry's line 1 should likewise be corrected under M2.

## What holds (checked, no finding)

- Source identity: live page title "Software Citation Principles (Published
  2016)", authors Arfon M. Smith, Daniel S. Katz, Kyle E. Niemeyer, FORCE11
  Software Citation Working Group; PeerJ Computer Science 2:e86; DOI
  `10.7717/peerj-cs.86` — matches `corpus/SOURCES.md:133` and the lesson Gate.
- §6.7 heading "Unique identification" is present and carries the quoted
  sentence verbatim; the 17-word located quote matches the live page; the
  snapshot's sentence matches the page including the trailing colon.
- SOURCES row: 11 columns, `S122` next unused id, tier A appropriate for a
  peer-reviewed primary paper, `status mined`, `opened 2026-10-24`, `recheck
  180d`, both `used-by` paths exist and are the two files that actually cite it.
- No affirmative permanence claim: entry line 9 ("does not make a raw commit
  identifier a persistent or independently resolvable software citation"),
  lesson line 12 ("does not claim that a raw commit identifier is a durable
  citation"), and the SOURCES scope cell ("this local check does not claim
  durable citation") are all disclaimers. The resolver docstring's "a real
  object in the fleet repository" states existence at check time, not
  persistence.
- The entry's behavioural self-test description is accurate:
  `commit_resolves` exists, and the self-test carries lane-first,
  fleet-fallback, neither, non-repository and missing-fleet-root arms
  (`verify_corpus_integrity.py:1055-1063`). The defect in H1 is the separate
  counter sentence, not this one.

## Residual risk

- The FORCE11 page is the row's cited URL; I did not diff §6.7 against the PeerJ
  PDF or page to §6.7 in the PeerJ HTML. If the two renderings diverged, the
  row's quote would still match the URL it cites.
- D2's committed-byte pin is a deliberate design choice for the frozen claim;
  the residual risk is readers treating `2 of 2` as behavioural proof of the
  fleet hop. H1's erratum plus MutC2NoFleetHop's recorded survivor closes that
  reading gap, provided the mutant report is committed with the erratum.
- Temporal order matters here: the entry's committed bytes precede the w1
  mutant report (the report was untracked at my read). The entry's sentence was
  written against the counter's synthetic self-test fixture, which is exactly
  the fixture that hides the survivor. If the erratum is routed without the
  mutant receipt, the same sentence can recur.
- The round-66 non-author spot-check (`corpus/lessons/round-66-verifier-spotcheck.md:61`)
  admits S122 and calls the teaches cell "honestly scoped"; it re-read the
  scope cell's disclaimer but did not test the teaches-cell paraphrase (M1) or
  the D2 sentence (H1). Its agree verdict does not cover these findings.

## Verification gaps

- I did not execute the lane counters or the integrity gate on the lane tree
  (main-agent verification). Receipts `C2-integrity-after.txt`,
  `C2-routed-after.txt` and the controls were read, not re-run. My only
  execution was the throwaway `/tmp` `check_d2` fixture described above.
- I did not re-open the PeerJ PDF; only the FORCE11 page (the cited URL) was
  fetched.
- I did not read the fleet report draft or any fleet-root file (lane-only
  scope); the mutation seat's scratch revisions (`3089e87…`, `376597f6…`) are
  sandbox-only and were not reproduced by me.
- No language-server (`lsp`) surface exists in this seat's tool inventory;
  code-path claims above come from reading the verifier sources at the measured
  tip, not from a semantic-index query.

Report: `.ufo/waves/round-66/w1/ReviewS122Fit.md`
Confidence: high on the source text and code-predicate findings (live source
re-fetched, code read, sandbox and independent mutant agree); medium on the
wording remediation, which is the canonical seat's call.
