# ScoutSource — S213 opened live (round 85, w1)

Seat: `ScoutSource`. Round 85 attempt 1, lane kotoba, host linux, 2026-11-04.
Scope: open S213 live, locate five ≤25-word quotes with page line numbers, and rule on each
staged claim of the round-74-rejected `spec-description-trigger-discipline.md` after re-grounding
on the live bytes.

**Result: S213 is live, unmoved, and every quote this seat needs is present verbatim. 11 of 13
staged claims survive re-grounding; 2 are refused with reasons. One material finding for the
L1: the staged entry's `source:` ids (S231/S232) are from the shokuknow package's registry, not
this lane's — in this lane those two ids point at unrelated rows.**

## Files written (all inside the lane, all under this seat's own wave dir)

| path | what |
|---|---|
| `.ufo/waves/round-85/w1/ScoutSource/fetch-record.txt` | fetch record: exact command, HTTP status, bytes, sha256, wc, byte-identity check, registry check |
| `.ufo/waves/round-85/w1/ScoutSource/source-packet.md` | the source packet: url, access date, HTTP status, bytes, sha256, 5 primary quotes + 13 supplementary located quotes with page lines and word counts, the 13-row staged-claim verdict table, registry-id mapping |
| `.ufo/waves/round-85/w1/ScoutSource.md` | this report |

Nothing else was written. **No** SOURCES row minted (S213 already holds the URL — a new row would
be a W04 duplicate, the round-74 rejection reason). Nothing written inside shokuknow (read-only:
two files read, zero writes). No git/jj write. No sibling lane touched. No fleet-root file touched.

## Fetch evidence (commands + observed output)

```
$ curl -sL -o "$S/page.md" -w 'HTTP %{http_code} size %{size_download}\n' \
    https://agentskills.io/skill-creation/optimizing-descriptions.md
HTTP 200 size 13403

$ sha256sum "$S/page.md"
7cc54fbb6abbcf08c33e7b320fd01a1fb9696426270da3b588a398d243bfd837  …/page.md

$ wc -c "$S/page.md"
13403 …/page.md

$ wc -l "$S/page.md"
196 …/page.md

$ cmp "$S/page.md" /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-76/snapshots/optimizing-descriptions.md
(exit 0, no output — identical)
```

The live page is **byte-identical** to the lane's committed r76 snapshot and to the digest pinned
at round 77 (`.ufo/waves/round-77/w1/S01Reopen1.md`, "7cc54fbb… match"). **S213 has not moved**;
C1 is not blocked by source drift. The staged entry's own fetch record ("13 403 B on 2026-10-23")
is still exact.

Supporting fetch (best-practices.md, for the staged entry's second half): HTTP 200, 15 060 B,
sha256 `ab9f3b6091a0f24816b52cd7b90a3fdf53e621f47dba13b36694be272b87fb41` — identical to the
round-77 pin.

## The five required quotes (all verbatim, all ≤ 25 words)

| need | page line | quote | words |
|---|---|---|---|
| (a) description carries the burden of triggering | **17** | `This means the description carries the entire burden of triggering.` | 10 |
| (b) imperative "Use this skill when…" form | **25** | `**Use imperative phrasing.** Frame the description as an instruction to the agent: "Use this skill when..." rather than "This skill does..."` | 21 |
| (c) trigger-eval design | **41** | `Aim for about 20 queries: 8-10 that should trigger and 8-10 that shouldn't.` | 13 |
| (c2) near-miss negatives | **56** | `The most valuable negative test cases are **near-misses** — queries that share keywords or concepts with your skill but actually need something different.` | 23 |
| (d) the 1024-character limit | **28** | `The [specification](https://agentskills.io/specification.md#description-field) enforces a hard limit of 1024 characters.` | 9 |
| (e) caveat: skills consulted only for knowledge beyond the agent | **19** | `One important nuance: agents typically only consult skills for tasks that require knowledge or capabilities beyond what they can handle alone.` | 21 |

Verification: a script re-read the packet's own tables, extracted every quoted string, and checked
it as a substring of the stated page line of the live bytes, re-counting its words —
**18/18 quotes verbatim, word counts exact, all ≤ 25.** Page lines are `grep -n` line numbers of
the fetched file.

## Staged-claim verdicts

Against `/home/vgpnk/Projects/shokuknow/merge/kotoba/knowledge/corpus/knowledge/spec-description-trigger-discipline.md`
(read-only) and the rejection row `corpus/lessons/round-74-verifier-spotcheck.md:116`:

- **survives (11)** — the under/over-specified error model (line 9); "the description carries the
  entire burden of triggering" (17); the imperative form (25); user-intent-not-mechanics (26);
  pushy/push-contexts (27); the 1024 limit (28, reinforced 159/174); ~20 queries, 8–10/8–10 (41);
  the four should-trigger variation axes and the "connection isn't obvious" sentence (47–52); the
  near-miss negative rule and "tests nothing" (56, 60); the "only consult skills for tasks …
  beyond what they can handle alone" caveat with the "read this PDF" example (19); and the
  best-practices half (best-practices.md 96/129/147 — located, but see the refusal below).
- **refused (2)** —
  (i) the **trigger-miss telemetry misattribution** claim: the page contains no telemetry
  sentence (`grep -n "telemetry\|misattribut" page.md` → no match). It is a sound *inference* from
  quote (e) but is **not** carried by S213 and must be labelled as the lane's inference, never
  cited to the page.
  (ii) the **three-way tension about negative conditions** (TRAE / Chiba): cited by the staged
  entry to "wave-2 rows", not to S213 or S223; neither page says anything about negative
  *directives* in a body. Out of scope for this seat's re-grounding; must not be folded into the
  round-85 S213 entry.
- **located but stays refused material (1)** — the best-practices half. All three quotes are
  present verbatim, but that half is exactly what round 74 refused: it is already carried by the
  admitted lane entry behind **S223**. The round-85 entry must **not** restate it.

One paraphrase caveat carried in the table: the staged entry's clause "only measures breadth" is
**not** a page quote — page line 56 says the near-misses "test whether the description is precise,
not just broad". Consistent, but it must not be quoted as if from the page.

## Material finding for the L1 — registry-id mismatch

The staged entry cites its two pages as **S231** and **S232**. Those ids come from the
shokuknow package's `SOURCES.append.md` (where `S231` = optimizing-descriptions.md, `S232` =
best-practices.md). In **this lane's** `corpus/SOURCES.md`:

- `S231` (line 172) = **Mistral Vibe README** — unrelated.
- `S232` (line 173) = **OpenAI Codex Skills** — unrelated.
- The optimizing-descriptions page is **S210** (line 151) and **S213** (line 153, "supersedes
  S210 for citation").
- best-practices.md is **S223** (line 164).

So a round-85 entry that copied the staged `source:` ids verbatim would cite the wrong rows. The
entry scribe (ScribeC1Entry) must cite **S213**. Flagged to the L1; no write made outside this
seat's wave dir.

## What this hands to C1

- **R3 `spec_max_1024`** → grounded, page line 28 (and the spec's own `specification.md`: "Must be
  1-1024 characters", HTTP 200, 7 685 B, sha256 `bf4137a7…`).
- **R4 `imperative_invocation`** → grounded, page line 25 (the literal `Use this skill when`).
- **R6 `eval_set_shape`** → grounded, page lines 41 (8–10/8–10), 52 (indirect positives), 56
  (near-miss negatives), 60 (why an irrelevant negative tests nothing).
- **R8 `sourced_entry`** → the re-grounded entry can name **S213**, `verified-at: 2026-11-04`, a
  `recheck:` value, and a located quote within the cap — quote (b) (21 words) or quote (a) (10
  words) both qualify.
- **R1 / R2 / R5 / R7** are not sourced to this page and are **not** claimed here (R5 is the
  sibling-census guard; R7 the packager rule).

## Risks

1. **Registry-id mismatch** (above) — the highest-value finding; a wrong `source:` id in the
   round-85 entry would silently mis-cite.
2. **Staged-claim over-reach**: the staged entry's telemetry sentence and its three-way-tension
   half are not S213 material. If the round-85 entry absorbs them unlabelled, the claim would
   cite the page for things the page does not say. Both are refused above with reasons.
3. **Word-count drift in a quoted row**: my first draft of the packet carried stale word counts
   on four rows and one backtick-stripped quote (line 60). Caught by the re-read script and
   corrected; the final packet is 18/18 clean. Any downstream scribe should re-run the same
   substring+word-count check rather than trusting the numbers as typed.
4. **Provenance of the *staged* entry** is unverified beyond its own header: it was fetched
   2026-10-23 with 13 403 B, and today's live fetch is the same 13 403 B and byte-identical to
   the lane's r76 snapshot, so the page side is sound — but the staged entry's *file* carries no
   sha256 of its own, so only its page-derived quotes are re-groundable, which is exactly the
   scope of this seat.
5. **S018 drift noticed in passing (not this seat's row)**: the specification page now serves
   7 685 B (sha256 `bf4137a7…`), while the lane's S018 row and `frontmatter-rule-authorities-round48.md`
   pin 7 608 B (`9a67de89…`). The 1024 rule is still present (specification.md lines 31 and 105),
   so C1's R3 is unaffected — but the S018 digest is stale and the registry row owner
   (ScribeSources) may want to re-pin it. This seat did not touch SOURCES.md.

## Environment

- **Tooling**: no install, no upgrade. `curl`, `sha256sum`, `wc`, `cmp`, `grep`, `python3` were
  already present; nothing in the operator tooling directive applied. (No pacman transaction.)
- **Scratch**: `/fast/scratch/hyaku/kotoba-r85/ScoutSource` — created with `mkdir -p`, used as the
  only write target for the fetches, removed with `trap 'rm -rf -- "$S"' EXIT` before yielding.
- **Reads**: two shokuknow files (read-only, zero writes), the lane's `corpus/SOURCES.md`,
  `corpus/lessons/round-74-verifier-spotcheck.md`, the r76/r77 wave receipts and snapshot.
- **Git**: read-only only (`status`, `rev-parse`); no mutation.
