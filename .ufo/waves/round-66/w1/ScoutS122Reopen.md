# ScoutS122Reopen — S122 live re-open (freshness axis, round 66)

Seat: leaf scout (read-only). No row, claim, control, or receipt changed.
Base: pinned round-66 base `11385e04e368c1e94ab1a5a89d7439033eb1f855` (claims evaluated as recorded at that state; source re-opened live).
Re-open performed: 2026-10-24, `read` fetch of `https://force11.org/info/software-citation-principles-published-2016/` — page live (HTTP 200, canonical URL self-confirms, title "Software Citation Principles (Published 2016) – FORCE11").

## Verdict

The S122 row, lesson quote, and excerpt are **fresh and verbatim-accurate**: the source directly supports the narrow repository-context point as scoped, and the row does not overclaim it. No discrepancy found; no change made.

## Observed facts (re-opened page vs. recorded claims)

| Claim | Live-page observation | Match |
|---|---|---|
| URL `force11.org/info/software-citation-principles-published-2016/` | Page live; canonical tag self-confirms the same URL | ✓ |
| Paper identity: Smith AM, Katz DS, Niemeyer KE & FORCE11 Software Citation Working Group, *PeerJ Computer Science* 2:e86 (2016), DOI `10.7717/peerj-cs.86` | Identical citation block rendered at top of page, DOI hyperlink to `doi.org/10.7717/peerj-cs.86` | ✓ |
| §6.7 anchor "Unique identification" | Heading `6.7. Unique identification` present, directly under §6 Discussion | ✓ |
| Located quote (lesson + `S122-excerpt.txt`): "a commit reference together with a repository URL is not recommended for the purposes of software citation" | Verbatim in §6.7 sentence: "…there are a number of reasons that a commit reference together with a repository URL is not recommended for the purposes of software citation:" | ✓ exact |
| Quote length "17 words" | 17 words counted | ✓ |
| Second anchor: §1 Principle 6 | Principle 6 "Specificity — Software citations should facilitate identification of, and access to, the specific version of software that was used" present | ✓ |
| `opened 2026-10-24` (SOURCES row + lesson) | Re-opened 2026-10-24; content consistent with excerpt | ✓ |

SOURCES row fields (`corpus/SOURCES.md:133`): kind `paper`, tier `A`, status `mined`, recheck `180d`, used-by `corpus/knowledge/fleet-commit-resolution-round66.md, corpus/lessons/round-66.md` — consistent with the append-only used-by correction at `corpus/lessons/round-66.md:36`.

## Source-fit assessment (supports vs. overclaims)

**Directly supported by the source text:**
- The paper's own sentence states commit-reference + repository-URL is "not recommended for the purposes of software citation," with three enumerated reasons: (1) version/commit references are not guaranteed permanent (migration, force-push clobbering), (2) repository address + version does not guarantee a resolvable URL (author removal), (3) a commit point may not be the authors' preferred citation point. This directly grounds the row's teaches cell — "A commit reference with its repository URL is still not a recommended durable software citation" — and the knowledge note's "does not make a raw commit identifier a persistent or independently resolvable software citation."
- The knowledge note's scope disclaimers ("local evidence integrity, not research citation policy"; "does not claim durable citation") are corroborated, not contradicted, by the source: §6.7's same paragraph adds that repository-URL + commit-hash "would be an appropriate way to cite the software used" as a fallback when no DOI/release exists — i.e., the paper itself treats a repository-scoped commit reference as meaningful version evidence while denying it durable-citation status. That is exactly the distinction the row records.

**Not literally in the source (bounded inference, properly hedged):**
- The precise mechanic of the lane's claim — "a hash identifies a version only with its repository context" (i.e., a bare SHA1 cannot be resolved without knowing which repository holds it, motivating the lane-first-then-fleet-root lookup) — is an inference from the paper always pairing "commit reference" with "repository URL" as a unit. The paper never discusses cross-repository disambiguation of a bare hash. This half-step is confined to the scope cell and is explicitly framed as the lane's application: the row's scope says "here"/"this local check," and the knowledge note says "this entry applies its version-context distinction to a local integrity check, not to citation permanence." A lane inference declared as lane inference is a scoped application, not an overclaim.

**No overclaim detected:** nothing in the row, lesson, excerpt, or knowledge note asserts that the gate's repository-context resolution confers persistence, citability, or DOI-equivalent status. The source is, if anything, stronger than the claim (it recommends DOIs outright); the lane used only the narrower direction.

## Unresolved gaps / non-issues

- Excerpt file (`S122-excerpt.txt`) is a quote record, not a full-page snapshot — recorded as such on its face ("excerpt, not a full-page snapshot"); the live re-open confirms the quoted lines verbatim, so the missing byte-snapshot is a completeness nicety, not a correctness risk.
- S122's `opened` date (2026-10-24) equals today's re-open, so freshness could only be same-day anyway; no staleness window exists yet. `recheck: 180d` stands unexercised.
- Residual [INFERENCE]: paper's silent treatment of commit+repository as a compound unit → lane's "repository context" phrasing; bounded and declared in the row itself, as noted above.

## Report trailer

Report: `.ufo/waves/round-66/w1/ScoutS122Reopen.md`
Confidence: high (live page re-fetched; every recorded field re-verified against it).
