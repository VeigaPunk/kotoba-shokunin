# Round 66 W1 — S122 lesson-Gate review (read-only)

- **Seat:** `ScribeLessonGate-2`, leaf scribe; no subagent dispatch; no production edits.
- **Lane:** kotoba (`/home/vgpnk/Projects/shokunin/kotoba-shokunin`).
- **Pinned base:** `11385e04e368c1e94ab1a5a89d7439033eb1f855`.
- **Measured tip (HEAD when read):** `2a8eba56b3f9321b70c569fa2816d42237ca49a2` (`protocol-shokunin`, 2026-10-24 04:26:20 -0300).
- **Checked item:** `corpus/lessons/round-66.md` §Gate, S122 bullet (lines 12–14), against the live FORCE11 page, `corpus/SOURCES.md` row 133, and `.ufo/waves/round-66/snapshots/S122-excerpt.txt`.
- **Date of review:** 2026-10-24.

## Evidence commands (exact, read-only)

| Command | Result |
|---|---|
| `read https://force11.org/info/software-citation-principles-published-2016/` | Full paper text served at the row URL; §6.7 heading `6.7. **Unique identification.**`; §6.7 contains the quoted sentence |
| `curl -sS --max-time 25 "<URL>" \| grep -o "a commit reference together with a repository URL is not recommended for the purposes of software citation"` | 1 match, exit 0 (verbatim on the live page today) |
| `printf '%s' "a commit reference together with a repository URL is not recommended for the purposes of software citation" \| wc -w` | `17` |
| `sed -n '133p' corpus/SOURCES.md`; `awk -F'|' 'NR==133{print $12}'` | Row S122; used-by = `corpus/knowledge/fleet-commit-resolution-round66.md, corpus/lessons/round-66.md` |
| `git show 11385e04:corpus/SOURCES.md \| grep -c "S122"` | `0` — row absent at the pinned base; S122 is new this round |
| `git diff --stat 11385e04..HEAD -- corpus/SOURCES.md corpus/README.md corpus/lessons/round-66.md` | SOURCES +3 (row + two search notes), README +8, lesson +36; additions only |
| `git log --format='%h %an %s' -- corpus/lessons/round-66-verifier-spotcheck.md` | `2a8eba5 protocol-shokunin round-66 verifier spot-check (integrator, hyaku): non-author admit/reject` |
| `git show --stat 2a8eba5` | adds 83 lines to `corpus/lessons/round-66-verifier-spotcheck.md`, 2026-10-24 04:26:20 -0300 |
| `git merge-base --is-ancestor 2a8eba5 HEAD` | yes (spot-check is at HEAD) |
| `grep -n "round-66" corpus/README.md` | lines 118 (r62 spot-check row), 123 (r66 lessons row); **no row for `lessons/round-66-verifier-spotcheck.md`** |
| `sha256sum .ufo/waves/round-66/snapshots/S122-excerpt.txt` | `8c027206637c0fffaa0df64559eb6ea7404ff77566e4e0e96346e5a0171409c8` |

## Attribute check

| # | Attribute | Gate text / pointer | Observed | Verdict |
|---|---|---|---|---|
| 1 | URL | `https://force11.org/info/software-citation-principles-published-2016/` | Byte-identical to page `canonical`, SOURCES row 133, excerpt `URL:`; page served the full paper text today | **PASS** |
| 2 | Access date | "opened 2026-10-24" | Lesson line 12, row `opened 2026-10-24` + anchor "page opened 2026-10-24", excerpt `Accessed: 2026-10-24`; URL live on 2026-10-24. The date is self-reported by the L1; I did not observe that session | **PASS** (record consistent; date not independently attested) |
| 3 | Located quote ≤25 words | "The located quote from §6.7, “Unique identification,” is: “a commit reference together with a repository URL is not recommended for the purposes of software citation” (17 words)." | 17 words; exact substring of the §6.7 sentence "…there are a number of reasons that a commit reference together with a repository URL is not recommended for the purposes of software citation:"; section heading matches | **PASS** |
| 4 | Source identity | "Software Citation Principles (Smith, Katz, Niemeyer & FORCE11 Software Citation Working Group, 2016) … PeerJ Computer Science 2:e86, DOI 10.7717/peerj-cs.86" | Page citation block: "Smith AM, Katz DS, Niemeyer KE, FORCE11 Software Citation Working Group. (2016) Software Citation Principles. *PeerJ Computer Science* 2:e86. DOI: 10.7717/peerj-cs.86" | **PASS** |
| 5 | Status | "S122: new row written directly as `mined`"; append-only note "`status` remains `mined`; `recheck` remains `180d`" | Row: `mined`, `opened 2026-10-24`, `recheck 180d`. `mined` requires ≥1 used-by path — satisfied (2) | **PASS** |
| 6 | used-by | Append-only: old `corpus/knowledge/fleet-commit-resolution-round66.md` -> new `corpus/knowledge/fleet-commit-resolution-round66.md, corpus/lessons/round-66.md` | Row column 11 equals the new value; both files exist and cite S122 (knowledge line 1 `source: S122`; lesson line 12). Residual strict-reading conflict C-2 below | **PASS as declared** |
| 7 | Non-author spot-check disclosure | "**Spot-check:** this L1 seat has no independent non-author reviewer; no round-66 admit/reject spot-check is claimed. The r65 non-author verifier spot-check was read and its D1–D3 routes are carried here." | Disclosure present and seat-scoped, but superseded at HEAD by a committed round-66 non-author spot-check (D-1). D1–D3 carry is supported at round level by `.ufo/reports/round-66/kotoba.md` line 12 (D3 operator-owned), though the lesson and plan name only D1/D2 | **FAIL (freshness)** |

## Discrepancies

### D-1 — Confirmed: the Gate's round-66 spot-check disclosure is stale at HEAD

- Lesson text (line 14, committed at `9e75e73`, 2026-10-24 04:20:01 -0300):
  > **Spot-check:** this L1 seat has no independent non-author reviewer; no round-66 admit/reject spot-check is claimed. The r65 non-author verifier spot-check was read and its D1–D3 routes are carried here.
- Observed: `corpus/lessons/round-66-verifier-spotcheck.md` was committed six minutes later at HEAD (`2a8eba5`, 04:26:20 -0300) by `protocol-shokunin`; its frontmatter is `author: hyaku closure (non-author integrator, @m_swe)`, and its discernment table re-opened exactly this row and agreed:
  > S122 admit (FORCE11 Software Citation Principles, Smith et al. 2016) | admit, tier A, `mined` | live URL … + committed snapshot … | **agree** | re-opened page confirms §6.7 "Unique identification" carries the quoted sentence verbatim; PeerJ/DOI metadata on the page matches the row; ≤25-word quote (17 words) located; …
- The Gate is frozen (CORPUS.md rule 2: only `status`, `recheck`, `used-by` change in place), so the sentence was not false when written and is not editable now. It is stale: at HEAD the round does have a non-author admit/reject spot-check, and the lesson's only spot-check disclosure does not say so.
- Related, outside this seat's item (for the C2/index owner): `corpus/README.md` has no coverage-map row for `corpus/lessons/round-66-verifier-spotcheck.md` (my grep found none; r46–r65 spot-check rows are explicit paths). `.ufo/waves/round-66/w1/ScoutCorpusCount.md` line 25 records the integrity gate's `unindexed=1` naming this file; I did not execute that gate.

### C-1 — Conflict for the canonical judge: excerpt label vs teaches-cell wording

- Excerpt: `Located quotation for the SOURCES.md teaches cell (17 words):` followed by the 17-word fragment.
- Row 133 `teaches` cell actually reads:
  > A commit reference with its repository URL is still not a recommended durable software citation; preserve repository context when checking local version evidence
- The fragment is verbatim from the page and grounds the cell, but it does not appear in the cell; the cell adds the qualifier "durable", which the located quote does not contain (the page recommends against commit+URL "for the purposes of software citation" and offers it only as a fallback when no DOI exists).
- Counter-record: the non-author spot-check already ruled the cell "honestly scoped … explicitly does not claim durable citation". Reported verbatim; I make no ruling.

### C-2 — Conflict for the canonical judge: used-by strict reading

- CORPUS.md: "`used-by` — repo-relative paths of the knowledge entries or lessons citing the row, comma-separated, or `—`."
- Row 133 lists `corpus/knowledge/fleet-commit-resolution-round66.md, corpus/lessons/round-66.md` (matches the lesson's logged old→new). Both exist and cite S122.
- `corpus/lessons/round-66-verifier-spotcheck.md` — also a lesson, also in this repo — references S122 and row 133, but is not listed. Under the literal contract wording this is an unlisted referencing lesson; under the "uses the source as support" reading (the spot-check reviews the row rather than derives knowledge from it) the list is complete. Canonical ruling needed; no ledger change made.

## Out of scope / not done

- No scoring of C1 (G9 floor coupling) or C2 (r65 D1/D2) claims; no wave dispatch; no edits to claims, counters, thresholds, plan, receipts, corpus, SOURCES row, or README.
- I did not execute `verifiers/verify_corpus_integrity.py`, `check_r66_routed_repairs.py`, or any other lane gate; the spot-check was read as committed bytes. No r65 route was re-derived beyond reading the r65 spot-check and the round-66 report line that carries D3.
- No tools installed or upgraded; no `pacman`/`uv`/binary installs. Only file written is this report.

## Verdict

At HEAD `2a8eba5`, the S122 row and the lesson's Gate are accurate on URL, access-date record, quote (17 words, verbatim, §6.7), source identity, status, and declared used-by. The single confirmed defect is the Gate's non-author spot-check disclosure (D-1), which the later `2a8eba5` spot-check supersedes without the lesson recording it; C-1 and C-2 are verbatim conflicts left to the canonical judge. The live page re-confirms the quote today, so the source binding itself is fresh; the disclosure text is the stale surface.

Report: `.ufo/waves/round-66/w1/ScribeLessonGate.md`
