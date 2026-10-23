# ConnSibling — round-61 sibling-overlap scan + adjacency packet

Seat: `kotoba-r61-wave-ConnSibling` (UFO-FSD connector, leaf; adjacency lane). Read-only.
No lane/fleet/jj writes except this report. No dispatch, no installs.
Observed 2026-10-23T19:07Z–2026-10-23T19:22Z (`date -u` at measurement: `2026-10-23T19:15:12Z`).

## Scope and method

Assignment: sibling-overlap scan of round 61 — does any sibling lane own part of this
round's work? — across tameshi (verification fixtures: the C1 worlds/fixtures shape),
kama (the writing-file import), chousa (source method), kengaku (measured capability
effects of counters), kotodama (naming); deliver (a) a classification table
(round-61 item × owning lane × none/adjacent/contested) and (b) the one-paragraph
adjacency packet for the report's Sources & frontier section; plus one bounded
connector move (build+attack wave posture: attacked the frozen predicates, the r60
evidentiary ground, the routed repairs, and the C3 bleed boundary from the adjacency
slice only — counter mechanics are covered by the wave's mutation/executor seats).

Canonical contract note (load-bearing): the committed plan `plans/round-61.md` at the
freeze commit `7827628` carries **Erratum E1** — C3 is withdrawn as a counted claim
before data (CriticC3Axis's static counterexample), mined as M92, and the S117 curation
continues as frontier-step work reported under Sources & frontier. My assignment text
predates that erratum; where they differ, the plan governs. This scan therefore treats
C3 as frontier curation, not a live claim, and delivers the adjacency packet for the
Sources & frontier section where that curation is now reported.

## Classification table

Overlap classes: `none` = no sibling province covers the item; `adjacent` = a sibling
owns the method/genre/artifact next to the item and the boundary is declared and held
(report, don't absorb); `contested` = two provinces claim the same item (none found).

| # | round-61 item | owning lane | overlap | basis (read this seat, evidence below) |
|---|---|---|---|---|
| 1 | C1 counter v3 gate code (`verifiers/check_scoped_rules.py` v3) | kotoba | none | kotoba PROVINCE Core lists the lane's own gates; tameshi PROVINCE: "every lane's gate remains its own" — the gate is unambiguously kotoba's |
| 2 | C1 worlds/fixtures W1–W7 + `--self-test` fail-closed arms + before/after receipts | kotoba builds; the reusable genre is tameshi's | adjacent | tameshi PROVINCE Domain: "verification-fixture craft — hermetic suites, mutation testing, fail-closed arms, verdict-line discipline, no-permissiveness audits, before/after proof"; tameshi refuses editing sibling gates, and the reverse holds — kotoba authors its own worlds in that genre. No tameshi artifact imported: tameshi r33's sealed held-out fixture never landed (MANIFEST `rejected-honest-stop`; ScoutAdjacency measured) |
| 3 | C1 source rows S112–S115 (client-doc fetches grounding arm A1's canonical key set) | vendor pages; admission method is chousa's | adjacent (method) | chousa PROVINCE owns source hierarchy / claim-vs-source verification; kotoba's QUALITY contract admits sources under that method without re-deriving it (round-49 census row chousa=adjacent) |
| 4 | Counter measurements (worlds reject 7 of 7; eligible rows pass 4 of 4; base exit 1) | kotoba gate behavior | none | kengaku owns measured *capability effects of prompt format on models*; gate reject/pass rates are verification behavior, not model-capability data, and no counter→capability inference is declared anywhere in the r61 plan or wave shape. kengaku PROVINCE refuses prompt-craft rules and hands craft implications to kotoba — the split holds in both directions |
| 5 | Artifact naming (W1–W7, A1–A4, R-a..R-f, S112–S117, Q56, M91, M92) | kotoba | none | kotodama owns naming *systems for fictional worlds feeding the world bible* (PROVINCE Domain); r61 names are engineering labels with no worldbible coupling. The round-49 census records a name-collision clause (lane names, kotodama MINT.md:20), not a scope split |
| 6 | C2 routed repairs R-a..R-f (LOG.md corrections, QUALITY.md Q56, `census-after.txt`, `controls-ancestry.txt`) | kotoba | none | In-lane record-keeping calibration over kotoba's own LOG/QUALITY/wave files; no sibling province owns a lane's own report hygiene. tameshi's before/after-proof genre is the *style* of R-f's ancestry receipt, not its content |
| 7 | C3/S117 kama import (SOURCES row + `writing-revision-calibration-round61.md` + README row) | kama owns the artifact; kotoba owns the admission decision | adjacent (declared, bounded) | plan §C3 froze tier B, kind `own-work` (sibling repo path), scope "writing-revision calibration for prompt-craft self-assessment"; Erratum E1 retired the counted claim (M92) — the curation survives as frontier work. Boundary held per CriticC3Axis + this seat's checks below |
| 8 | S117 content genre (git-blame-at-writing calibration counter record) | kama (artifact); craft genre is tameshi-adjacent | adjacent | the file is kama's r29 C1 counter record — verification craft in tameshi's genre, but authored and owned in kama's corpus; kotoba cites the artifact and re-derives neither kama's endpoint domain nor tameshi's method |

**Contested rows: none.** Every adjacency above has a declared boundary in at least one
province file and a read-only posture on kotoba's side. Two contradictions surfaced
during the scan and are stated, not smoothed:

1. **tameshi r33 closure contradiction** (via ScoutAdjacency's measurements): the
   committed spot-check lesson `corpus/lessons/round-33-verifier-spotcheck.md` ends
   with the word "Admitted." while the fleet MANIFEST row for tameshi r33 says
   `admitted: false`, `verdict: rejected-honest-stop`. The MANIFEST row governs any
   adjacency citation; the lesson's last word must not be copied (ScoutAdjacency
   consequence 4).
2. **C3 predicate vs Erratum E1**: my seat text still names C3 as a round claim; the
   frozen plan withdrew it pre-data. The plan is canonical (frozen predicates live
   there); C3's predicate is retired unmeasured and this report services its surviving
   curation under Sources & frontier.

## Attack slice (adjacency): the C3 bleed boundary

The counting-counter attack succeeded pre-data (CriticC3Axis → Erratum E1 → M92).
What remains attackable is the *content* of the surviving frontier curation. Three
bleed risks, all measured against committed bytes:

**B1 — `own-work` kind has no sibling-path precedent (semantic, not guard-visible).**
CORPUS.md (fleet) defines the `source` cell as "a repo path or command for `own-work`"
and the kind enum admits `own-work`, so the corpus guard (`corpus/SOURCES.md:145`
awk) will not reject the planned row. But every existing `own-work` row in kotoba's
registry is titled "kotoba own work" and the registry's own prose
(`corpus/SOURCES.md:139-140`) describes the own-work rows as where the lane's own
comparator/checklist gate facts land. A sibling artifact is by definition not the
lane's own work; S117 as planned would be the first sibling-path `own-work` row and a
future closure could route this as mis-classification (same class as r60 routed
defect (c): imprecise naming of what a pointer names). Mitigations the L1 can pick:
keep the frozen kind but make the row title carry "sibling lane (kama) own work —
…" so the provenance is in the cell the census reads, or record a one-line
frontier note in the Sources section that the kind's semantics are extended this
round. (No kind in the enum fits better; `docs` would mis-describe a lane artifact.)

**B2 — the kama file's limits must survive into the entry.** The committed kama file
(`kama-shokunin/corpus/knowledge/self-assessment-at-writing.md`, 33 lines, blob
`0601bd03…` at kama tip `227dd1ee` per ScoutAdjacency's measurement) states: front
matter "no fresh counter run performed"; the bounded six-class extractor is "not a
semantic proofreader"; and the L1-added paragraph: a correction row means "the stated
evidence did not resolve at writing", **not** "the claim was false"; the baseline
`11 unresolved / met false` is a frozen-base value, while the committed tip receipt
(c1-6de225c2.out) prints `met True` — the entry must not teach either number as the
knowledge file's sentence, and must not treat the tip receipt as text inside the
knowledge file (ScoutAdjacency consequences 1–2, re-stated as bleed guards).

**B3 — tameshi r33 must not be cited as an admitted fixture source.** Round 61's C1
worlds are kotoba-authored; tameshi r33's sealed held-out set was never authored and
the round closed `rejected-honest-stop`. Citing tameshi's r33 lesson (whose last word
is "Admitted.") as support would import a false provenance claim into kotoba's
registry — exactly the A4-class defect C1 v3 arm A4 exists to reject. No second
adjacency source is needed this round; the curation stands on S117 alone.

Adjacency-flavored notes on the surviving counted predicates (not re-attacking
mechanics — the wave's attack seats own that):

- **C1**: arm A1's "canonical per-client key set" is grounded in S112–S115, which are
  *opened this round* and do not exist at base (`grep -nE '^\| *S11[2-7] *\|'
  corpus/SOURCES.md` → no matches at `7827628`; registry holds S001–S111, count 110).
  The cross-seat dependency is real: the counter freeze at integration must land the
  four rows with their fetch receipts, or A1's grounding sentence has no registry
  referent. The plan's commit order already sequences this; the risk is a partial
  integration, and it is named here so the L1 checks it.
- **C1 vocabulary**: A3's predicate word "byte-identical" (URL equality) is literal
  equality and survives the Q56 discipline R-e introduces; recommend the integration
  receipt keep "byte-identical" only where the check is literal byte equality, so
  round 62 cannot route the M91 class against round 61's own label.
- **C2**: zero sibling content; all six repairs are in-lane record-keeping. The only
  adjacency-shaped risk is R-a's phrasing drifting into claiming the *method* of
  counting reports as new ground — it is tameshi-genre bookkeeping, report as such.

## Adjacency packet (one paragraph — for the round report's Sources & frontier section)

> Round 61 touched four sibling-adjacent boundaries and held each as report-don't-absorb. (1) Verification-fixture craft (tameshi): the C1 counter-v3 self-test with its seven committed attack worlds W1–W7 and fail-closed arms is built in the fixture genre tameshi owns as reusable method — hermetic attack worlds, no-permissiveness audits, before/after proof — but the gate and worlds remain kotoba's own (tameshi PROVINCE: every lane's gate remains its own; read-only probes only), and no tameshi artifact was imported: tameshi r33's sealed held-out fixture never landed and that round closed `rejected-honest-stop` per the fleet MANIFEST, whose verdict contradicts the spot-check lesson's closing word "Admitted." (the MANIFEST row governs; the word was not cited). (2) Source method (chousa): C1's four new rows S112–S115 are documentary fetches handled under chousa's source hierarchy and claim-vs-source discipline — cited, never re-derived. (3) Kama artifact: `kama-shokunin/corpus/knowledge/self-assessment-at-writing.md` was curated as SOURCES S117 (tier B, sibling repo path, scope "writing-revision calibration for prompt-craft self-assessment") with knowledge entry and README row; per pre-data Erratum E1 this curation is frontier-step work, not a counted claim (M92: a presence counter cannot back an adjacency claim), the entry preserves the source's stated limits (no fresh counter run performed; an evidence-resolution failure at writing is not a false judgment; neither the frozen-base nor the tip-receipt number is taught as the file's sentence), and the row pins the kama blob rather than a moving tip. (4) Kengaku's boundary held: counter reject/pass rates are gate behavior, not model-capability measurements, and no capability inference was drawn. Kotodama's naming domain (fictional-world systems) is untouched by round-61 engineering labels. No contested scope was arbitrated this round.

## Connector move (one bounded proposal)

**Move: landed-scope provenance naming — put the adjacency packet's four clauses into
the round-61 report's Landed changes / Sources & frontier verbatim.** No code, no new
gate, no measurement change; report prose only.

- **Evidence.** AXES adjacency = "evidence belonging to another domain reported, not
  absorbed" — the packet is the report. The r60 closure routed defect (b) (two files
  changed but unnamed in the report's landed scope) and M91 (the overstatement/sloppiness
  class mined from it) show closure reviewers check landed-scope completeness; a round-61
  report that names only kotoba files while using tameshi-genre fixtures, chousa-method
  admissions, and a kama artifact invites an isomorphic routed defect in round 62. The
  packet's content already exists in this wave (ScoutAdjacency, CriticC3Axis, this seat);
  the move only carries it into the report.
- **Axes affected.** adjacency/consistency improve (scope disclosure complete; the
  packet names what was used and what was refused); no other axis is touched — depth
  (C1 predicate unchanged), expansion (no rows implied by prose), quality, discernment.
- **Second-order effects.** Contract: SOURCES/CORPUS guards unchanged (prose, not
  rows). Verification surface: a future closure has a named scope to diff against —
  that is the point. Runtime/substrate: none. Contradiction carried visibly: the
  tameshi "Admitted."/MANIFEST conflict is reported inside the packet, not smoothed.
- **Risks.** (a) Over-reading as sibling co-authorship — mitigated by naming provinces
  as genre/artifact owners, not contributors; (b) the packet asserts kama/tameshi tips
  as of ~19:11Z — if either lane moves before integration, re-pin the two hashes
  (ScoutAdjacency's re-measure advice); (c) if the L1 declines, the fallback is one
  Landed-changes line "sibling-adjacent method and artifact provenance: see
  `wave/ConnSibling.md`" — cheaper, still closes the routed-defect shape.
- **Verification.** Each packet clause cites its evidence inline; the classification
  table above is the checklist a reviewer can diff clause-by-clause.

## Measurement record (commands, output, date -u, exit codes)

Lane state and round-61 base:

```
$ cd /home/vgpnk/Projects/shokunin/kotoba-shokunin && git log --oneline -3
7827628 round-61: plan freeze (3 claims, frozen predicates), C2 routed-repairs counter + base control, census-before, v2 wave spec+dispatch (68 seats, 46 attack)
f3246d1 round-60 verifier spot-check (integrator, hyaku): non-author admit/reject
79cf263 round-60: close (attempt 2) ...
$ git status --porcelain | head -5
?? .ufo/waves/round-61/wave/CriticC3Axis.md   (etc. — wave reports untracked, lane clean otherwise)
exit 0
```

C3 base count and registry head (the frozen before-values for the retired C3 counter;
kept as evidence of the state Erratum E1 presumes):

```
$ grep -cE '^\| *S[0-9]{3} *\|' corpus/SOURCES.md
110
$ grep -nE '^\| *S11[2-7] *\|' corpus/SOURCES.md   # no output: S112-S117 absent at base
exit 1 (grep no-match)
$ test -f corpus/knowledge/writing-revision-calibration-round61.md || echo entry-absent
entry-absent
$ date -u +'%Y-%m-%dT%H:%M:%SZ' → 2026-10-23T19:15:12Z
```

kama artifact presence (identity details — blob, tip receipt, deltas — are
ScoutAdjacency's measurements, cited not re-run):

```
$ test -f /home/vgpnk/Projects/shokunin/kama-shokunin/corpus/knowledge/self-assessment-at-writing.md && echo kama-file-present
kama-file-present
$ wc -l /home/vgpnk/Projects/shokunin/kama-shokunin/corpus/knowledge/self-assessment-at-writing.md
33 ... (5831 bytes per ScoutAdjacency)
exit 0
```

`own-work` precedent scan (basis for B1):

```
$ grep -n 'own-work' corpus/SOURCES.md
S009, S010, S015, S020 rows — all titled "kotoba own work"; :139 prose: "The two own-work rows are where those facts land: the comparator ... and the checklist gate"
$ grep -n 'shokunin/' corpus/SOURCES.md            # sibling repo paths in source cells
(no output — no sibling-path source cell precedent in kotoba's registry)
exit 0
```

C2 base control (committed, read not re-executed): `.ufo/waves/round-61/controls/C2-base.txt`
prints `routed repairs verified 0 of 6`, `base-exit=1` — confirms C2 has no sibling
content (all six repairs are kotoba-file patterns).

Reads (no execution): `plans/round-61.md` (incl. Erratum E1 at `:108-116`),
`tameshi-shokunin/PROVINCE.md`, `kama-shokunin/PROVINCE.md`, `chousa-shokunin/PROVINCE.md`,
`kengaku-shokunin/PROVINCE.md`, `kotodama-shokunin/PROVINCE.md`, `kotoba-shokunin/PROVINCE.md`
(round-49 Adjacent census), `verifiers/check_routed_repairs.py` docstring,
`.ufo/waves/round-61/controls/C2-base.txt`, `corpus/lessons/round-60-verifier-spotcheck.md`
§7–§8, `.ufo/waves/round-60/controls/SUMMARY.md`, `controls-v2/SUMMARY.md`,
`build/ExecKeyForms.md`, kama `corpus/knowledge/self-assessment-at-writing.md`,
fleet `CORPUS.md:88-95` (kind/tier cells + guard), sibling reports
`wave/ScoutAdjacency.md` and `wave/CriticC3Axis.md`.

Not verified (honesty): I did not re-run ScoutAdjacency's hash/ancestry commands
(kama blob `0601bd03…`, tameshi MANIFEST row, tip receipts) — cited as that seat's
measurements; I did not execute either sibling counter; I did not re-execute the C2
checker (committed control read instead).

## Installs

no installs (no tool missing; pacman untouched per orchestrator ruling).

## Blockers

none.

## Attacked / produced

Attacked: the C3 bleed boundary (own-work kind semantics vs the frozen plan's
sibling-path use; kama-file limit preservation; tameshi r33 false-provenance trap),
the C1 predicate's cross-seat grounding dependency on S112–S115, and the C1/C2
predicates' adjacency surface (naming discipline). Produced: the classification table
(eight items, zero contested, two contradictions stated), the lift-ready adjacency
packet for the report's Sources & frontier section, and one bounded connector move
(landed-scope provenance naming).
