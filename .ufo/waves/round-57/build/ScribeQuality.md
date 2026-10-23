Result: DONE — drafted Q41–Q44 for L1 integration; no lane corpus file was edited.

## Draft append-only rows

| id | criterion | applies to | grounded in | supersedes |
|---|---|---|---|---|
| Q41 | A hash cited in a report resolves in the lane repo; if it is a sandbox hash, the same line labels it `sandbox` and gives its clone path. | Round reports and report-cited hashes | M58 `sandbox-hash-unlabelled` (`corpus/lessons/round-57.md` § Mistakes; round-56 spot-check R1, `corpus/lessons/round-56-verifier-spotcheck.md:219-221`) | — |
| Q42 | Before a quote note lands, reopen it against the fetched bytes; when a quote needs shaping (folded lines, stripped markup, or a fence info string) and an unshaped quote exists on the same page, use that unshaped quote. | Source quote notes in knowledge entries and lesson records | M59 `shaped-quote-note-unverified` (`corpus/lessons/round-57.md` § Mistakes; round-56 spot-check R2, `corpus/lessons/round-56-verifier-spotcheck.md:107-122`) | — |
| Q43 | Held-ground counts match case-sensitively at path-segment boundaries; the self-test demonstrates that a case variant and a memory-file analog are not held. | Claim counters and gates that count held ground | M60 `case-folded-held-ground` (`corpus/lessons/round-57.md` § Mistakes; round-56 spot-check R4, `corpus/lessons/round-56-verifier-spotcheck.md:233-236`) | — |
| Q44 | Wave contexts state that processes are killed only by PIDs started by the seat (never by a shared-path pattern) and cap contention tests at 4 concurrent processes and 120 seconds; a context check must fail when either bound is absent. | Wave contexts and checks that validate their required safety bounds | M61 `pattern-kill-no-cap` (`corpus/lessons/round-57.md` § Mistakes; R7, repeat of M56 `seat-killed-sibling-processes` in `corpus/lessons/round-56.md:61-64`; round-56 spot-check R7, `corpus/lessons/round-56-verifier-spotcheck.md:241-246`) | — |

## Evidence and scope

- `corpus/QUALITY.md` was read in full to match its five-column table and append-only convention (lines 1–11, 51–55); Q40 is its current final row. Existing Q03, Q23, and Q32 remain distinct: the proposed rows address hash origin labels, byte-grounded quote notes, and held-ground/self-test semantics without superseding them.
- Assignment anchors and exact lesson IDs/classes are in `.ufo/waves/round-57/build-spec.json:162,170`. The lesson file `corpus/lessons/round-57.md` was not present when read (read tool returned “not found”), so M58–M61 are prospective anchors assigned to L1, not independently observed lesson rows. Their labels above follow the assignment; L1 should retain those IDs and ensure the final mistake rows support the draft criteria.
- Supporting routed evidence: `corpus/lessons/round-56-verifier-spotcheck.md:219-221` (R1), `:107-122` (R2), `:233-236` (R4), and `:241-246` (R7); M56’s incident and fix are `corpus/lessons/round-56.md:61-64`. The round-57 plan states the R7 context-check requirement at `plans/round-57.md:81-87`.
- The binding bounds require each seat to write only its own report (`.ufo/waves/round-57/bounds.md:2-3`); therefore `corpus/QUALITY.md` is intentionally unchanged for L1 to integrate the candidate rows.
- No shell commands, gates, tests, or builds were run; no tools were installed or updated. This deliverable drafts documentation criteria only and makes no execution or product-behavior claim.

## Touched surface and artifact

- Written: `.ufo/waves/round-57/build/ScribeQuality.md` (this report only).
- Read-only target: `corpus/QUALITY.md`.
- Not changed: lesson corpus, counters/verifiers, runtime code, or other lane files.
