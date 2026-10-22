# FrMistakeScribe — round-48 frontier: one mined mistake with a fix shown able to fail

Seat `KotobaR48.FrMistakeScribe` (leaf, read-only on the lane; no subagent dispatch).
Lane tip read: `75f671b109d8eddd0d64c1429bd6379fe577175a`.
Scope: mine one mistake for `corpus/lessons/round-48.md` `## Mistakes` — class, evidence pointer,
`captured-by`, and a fix shown able to fail with the exact demonstration command.

## Recommendation: M27 — Rule mis-credited to an authority

**M27 Rule mis-credited to an authority (a registry cell claims a rule an authority's own bytes do not carry)**

Of the three candidates in the brief, this is the one whose fix can be shown to fail today, in
one command, against bytes that are pinned and re-fetchable. It is also the only candidate that is
*not* a duplicate of an existing class — see the duplicate check below.

| class | evidence pointer (command → output) | captured-by | fix |
|---|---|---|---|
| M27 Rule mis-credited to an authority (a registry cell claims a rule an authority's own bytes do not carry) | `git show 75f671b:corpus/SOURCES.md \| grep '^| S003 '` → the `teaches` cell ends "…body under 500 lines; an Anthropic-only rule the open spec lacks"; `curl -fsSL https://agentskills.io/specification.md` (200, 7 608 B, sha256 `9a67de89…`) → `grep -n 'under 500 lines'` → `237:Keep your main \`SKILL.md\` under 500 lines. Move detailed reference material to separate files.` The closing clause, read after the 500-line clause, denies the open spec a rule the open spec **does** carry. The same shape was already rejected once for S011 (community row): it "credits an angle-bracket ban to the agentskills.io spec which has none" — `grep -ciE 'angle bracket' spec.md` → 0 (`corpus/lessons/round-46.md:73`). | `none → Q23` — no instrument reads a SOURCES `teaches` cell against the authority's own bytes. `grep -rn "teaches" verifiers/*.py` → no output (exit 1); `verifiers/verify_corpus_integrity.py:629` `CHECKS` covers only index/pointer counts; `scripts/sources-census.sh` validate checks shape, enums, dates and `used-by` (E01–E12, W01–W04) and never the truth of an attribution. | Q23: every rule a registry cell attributes to an authority is re-checked against that authority's own bytes before the cell is trusted. An attribution claim is a falsifiable statement with a named polarity — *the authority carries the rule* / *the authority lacks it* — not free prose. Shown able to fail: the demonstration below exits **1** on the live S003 cell and **0** on the corrected superseding-cell wording. |

### Exact demonstration command

One paste, read-only, no lane mutation (from my seat scratch
`/fast/scratch/hyaku/kotoba-r48-a2/seats/FrMistakeScribe/demo-one-liner.sh`, sha256 recorded below):

```sh
LANE=/home/vgpnk/Projects/shokunin/kotoba-shokunin
W=$(mktemp -d)
curl -fsSL https://agentskills.io/specification.md -o "$W/spec.md"
git -C "$LANE" show 75f671b109d8eddd0d64c1429bd6379fe577175a:corpus/SOURCES.md \
  | grep '^| S003 ' | grep -o 'body under 500 lines; an Anthropic-only rule the open spec lacks'
grep -n 'under 500 lines' "$W/spec.md"
grep -ci 'XML tag' "$W/spec.md"; grep -ci 'third[- ]person' "$W/spec.md"
```

Measured output (exit **1**, the class is present):

```
spec sha256: 9a67de89132948b2300b8dc87b93817971d47f9be89b644444965881a8dfde16  (expect 9a67de89...)
claim under test (corpus/SOURCES.md:16 @ 75f671b): ...body under 500 lines; an Anthropic-only rule the open spec lacks
open spec, 500-line rule:
237:Keep your main `SKILL.md` under 500 lines. Move detailed reference material to separate files.
open spec, XML-tag rule:  0 occurrence(s)
open spec, third-person:   0 occurrence(s)
REFUTED: the open spec carries the 500-line rule the cell attributes to Anthropic alone
```

The same shape in the sibling's superseding row S019 (`corpus/SOURCES.md`, working tree) is **not**
refuted: "the 500-line body rule is not Anthropic-only: the open spec states it too (S018 §
Progressive disclosure); Anthropic-only are the no-XML-tags rule on both `name` and `description`, the
reserved words "anthropic" and "claude", and the third-person description rule". Every clause of that
wording was re-measured against the two authorities' bytes and holds (8/8, exit **0**).

### The instrument (so the fix is not a claim, it is a runnable check)

`attribution-check.py` (sha256 `9a5e6fa6bb4cbabe6f800a83d99e98b7af4535cc1db00721bfa0325d03aff699`)
takes a claim set, each claim being `(authority, marker, polarity)` plus an optional binding to the
lane's own pinned bytes (`lane_row`: path, rev, and the substring that must occur in that blob). It
verifies each authority's sha256 against a manifest, refuses to evaluate a claim whose binding
substring is absent from the pinned lane blob, then tests each claim against the authority's bytes.

| arm | command | exit | what it shows |
|---|---|---|---|
| 1 | `--cases cases-lane-today.json` (bound to `corpus/SOURCES.md` @ `75f671b`) | **1** | 9 claims, 1 refuted: `s003-lacks-500-line-rule` — the live S003 cell |
| 2 | `--cases cases-superseding-control.json` (corrected wording, unbound) | **0** | 8 claims, 0 refuted — the control passes |
| 3 | arm 2 with `ctl-s003-500-line-shared` flipped to `absent` | **1** | 8 claims, 1 refuted — a polarity flip is caught, the check is not vacuous |
| 4 | arm 2 with a tampered manifest sha | **2** | `ERROR: sha256 drift for agentskills-specification.md` — a moved authority is refused, not silently scored |
| 5 | `--cases cases-s019-supersede-control.json` (bound to the **working-tree** S019 row) | **0** | 8 claims, 0 refuted — the sibling's superseding wording survives the same check that refutes the live cell |

Arm 5 is the important one: red on the lane as it stands, green on the repair, from one instrument.

## Why the other two candidates were not chosen

- **Round-47's C3 no-harm declared on green local targets while the frozen-carrier join moved 21/24 → 20/24.**
  The move is *definitional*, not demonstrated harm: the producer sees a `customize-opencode` built-in
  marker while the independent instrument fixes built-ins to zero by declaration
  (`corpus/lessons/round-47-verifier-spotcheck.md`, "Per-claim and no-harm review" and "Outside
  discernment checks"). The spot-check rules the join difference "not, by itself, demonstrated
  real-world harm" and forbids re-pinning the independent definition after the fact. A mistake class
  for it therefore has no falsifiable predicate today, and the fix would be a redefinition, not a fix.
  It is also adjacent to M5 (fix that harms) and M20 (stale planned premise) — the no-harm verdict
  was already recorded as unprovable in `corpus/lessons/round-47.md` M23 and the spot-check, so mining it
  again would re-report a routed defect as a new class.
- **Round-48 attempt 1 failing at T0 as a stale-author process.** No `T0` gate exists in the lane or the
  fleet (`grep -rn "\bT0\b" /home/vgpnk/Projects/shokunin/*.md`, `scripts/hyaku/` → no match), and
  attempt 1's commits are present and internally consistent: `instrument.json`'s ruler sha256
  `01af33a6…` and oracle sha256 `1d09a38c…` equal the committed bytes (`sha256sum` of
  `.ufo/round-48/tools/config-root-ruler.py`, `.ufo/round-48/oracle/config-root-cases.json`), and the
  before-receipt sha256 `8bec447a…` equals `plans/round-48.md`'s stated value. There is no failing
  artifact to point at, so the class would be a story rather than a measurement. The genuine
  inherited-state questions here are carried by the `FrAttempt1Audit` seat.

## Duplicate check against the existing class ledger

M1–M23 are the whole ledger (`grep -rho "| M[0-9]\+" corpus/lessons/*.md | sort -u` → M1…M23, no
gaps). None is an attribution class:

- M16 (unprovenanced knowledge entries) and M4 (dead recheck/source command) are about *provenance
  fields* being present or resolvable — not about whether a cited authority carries a rule.
- M13 (structural frontmatter gate mistaken for semantic) is about a *checker's* strength, not a
  registry cell's attribution.
- M22 (a lesson's own evidence pointers stale at landing) is about *line-number* rot inside the lane.
- M23 (a landing record quotes a count measured on a different tree) is about counts, not attribution.
- The nearest prior art is `corpus/lessons/round-1-aggregator-audit.md` ("Fabricated-location quote
  (hard failure)", "a misattributed quote here is a domain defect") and the S011 rejection in
  `corpus/lessons/round-46.md:73`. Both are the same *shape* — an assertion attributed to a source
  that does not carry it — but neither is a numbered M-class in this lane's ledger, and neither was
  captured by an instrument. M27 names the class; S011 is its prior instance.

**Numbering.** M23 is the highest number in the lane, so M24 is the next free one. `FrQualityCriteria`
owns the three routed-defect classes and proposed M24/M25/M26; I have taken **M27** for the mined class
and told them so — no renumbering on either side. QUALITY rows: `FrQualityCriteria` writes Q20/Q21/Q22
for their three; **Q23** is this class's criterion.

## Sources opened this session (primary, unexecuted)

| source | URL | accessed (UTC) | bytes / sha256 | quote (≤25 words) | location |
|---|---|---|---|---|---|
| open spec | https://agentskills.io/specification.md | 2026-10-22T08:19:15Z | 7 608 B, `9a67de89132948b2300b8dc87b93817971d47f9be89b644444965881a8dfde16` | "Keep your main `SKILL.md` under 500 lines. Move detailed reference material to separate files." | § Progressive disclosure, md:237 |
| Anthropic best practices | https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices.md | 2026-10-22T08:19:15Z | 42 169 B, `f0a5d61b67123a31527e64aae7c5cfc05c4c7e27fff16f5b35ea14b135423960` | "Cannot contain XML tags" | § Skill structure, md:155 (`name`) and md:162 (`description`) |

No fetched code was executed. No tool was installed or upgraded (none needed; `curl`, `sha256sum`,
`git`, `python3`, `sh` were all present).

## Artifacts (all in my seat scratch; the lane was not mutated)

`/fast/scratch/hyaku/kotoba-r48-a2/seats/FrMistakeScribe/`

| file | sha256 |
|---|---|
| `attribution-check.py` | `9a5e6fa6bb4cbabe6f800a83d99e98b7af4535cc1db00721bfa0325d03aff699` |
| `attribution-demo.sh` (self-contained, no helper script) | `84345412212f65e7c8fded55e9ce23151e42c980d2c47964adb28fb08ec1b625` |
| `demo-one-liner.sh` (the command quoted above) | see `sha256sum demo-one-liner.sh` |
| `cases-lane-today.json` | `9537e81e847a64ec91beb5ebed19cb25b53f3cf5718dcda1db4c5d4c4ff9f542` |
| `cases-superseding-control.json` | `2ade7f0c298ef57c77d9a0d5ca54a7dccb70f0261abdc26be465093dcd21c30e` |
| `cases-s019-supersede-control.json` | (worktree-bound control) |
| `manifest.json` | `c1113421187b8c6273a83d1297aaa7ca19508db1f2da0b9cb2063a22ea77f835` |
| `agentskills-specification.md` | `9a67de89132948b2300b8dc87b93817971d47f9be89b644444965881a8dfde16` |
| `anthropic-best-practices.md` | `f0a5d61b67123a31527e64aae7c5cfc05c4c7e27fff16f5b35ea14b135423960` |

## Row text for `corpus/lessons/round-48.md` `## Mistakes` (paste verbatim)

```
| M27 Rule mis-credited to an authority (a registry cell claims a rule an authority's own bytes do not carry) | `git show 75f671b:corpus/SOURCES.md \| grep '^| S003 '` → the `teaches` cell ends "…body under 500 lines; an Anthropic-only rule the open spec lacks"; `curl -fsSL https://agentskills.io/specification.md` (200, 7 608 B, sha256 `9a67de89…`) → `grep -n 'under 500 lines'` → `237:Keep your main SKILL.md under 500 lines.` — the closing clause, read after the 500-line clause, denies the open spec a rule the open spec does carry; the same shape was already rejected for S011, which "credits an angle-bracket ban to the agentskills.io spec which has none" (`grep -ciE 'angle bracket'` → 0, `corpus/lessons/round-46.md:73`) | none → Q23 (no instrument reads a SOURCES `teaches` cell against the authority's own bytes; `grep -rn "teaches" verifiers/*.py` → no output, and `scripts/sources-census.sh` validate checks only shape, enums, dates and `used-by`) | Q23: every rule a registry cell attributes to an authority is re-checked against that authority's own bytes before the cell is trusted; an attribution claim is a falsifiable statement with a named polarity (the authority carries the rule / the authority lacks it), not free prose. Shown able to fail: the attribution checker exits 1 on the live S003 cell (9 claims, 1 refuted) and 0 on the corrected superseding-cell wording (8 claims, 0 refuted); a flipped polarity exits 1 and a moved authority sha exits 2. |
```

## Out of scope for this seat

- The lesson file `corpus/lessons/round-48.md` itself (L1 integration owns landing it; `FrSourcesRowsScribe`
  holds the `## Gate` rows and sweeps, `FrQualityCriteria` holds M24–M26, this report holds M27).
- The registry repair itself: `FrSourcesRowsScribe` has already drafted the superseding rows S018/S019
  and S020 in the working tree; this seat changed no lane file.
- The C1 configured-root repair and the C2 knowledge entry (other seats).
- `corpus/QUALITY.md` Q20–Q23 rows (`FrQualityCriteria` owns Q20–Q22; Q23 is this class's criterion).
