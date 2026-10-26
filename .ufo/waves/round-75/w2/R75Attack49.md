# R75Attack49 — independent falsification of R75Facet49

**Verdict: survived in its central finding, with qualifications.** The report correctly identifies that the Gemini row's code-level statement is not checked by the frozen counter and that the committed repository lacks the cited TypeScript snapshot. Its broader scope/freshness implications and proposed controls are less conclusive than stated. No source or lane changes made; no live fetch performed.

## Reopened evidence and cheap check

Measured repository revision is `65a5c7a663249e0522cc49e4a148424200d9ddfe`, matching the report's pinned revision. `SKILL.md:174` indeed asserts that `frontmatter.description` passes as-is at `skillLoader.ts:211`, is interpolated at `snippets.ts:320`, and that no cut appears in those steps. The entry `corpus/knowledge/skill-listing-thresholds-round54.md:44` repeats that claim, while `:60-67` explicitly says no client was run and that the Gemini/opencode no-cut claims came from source reading.

Ran the bounded local detector exactly against the measured tree:

```text
python3 -B verifiers/check_description_thresholds.py --root /home/vgpnk/Projects/shokunin/kotoba-shokunin
Claude Code  BACKED
Codex        BACKED
VS Code      BACKED
Copilot CLI  BACKED
Gemini CLI   BACKED
Cursor       BACKED
opencode     BACKED
description thresholds backed 7 of 7 clients
```

This confirms the proposed control gap in practice: the counter returns `BACKED` for Gemini. Its implementation at `verifiers/check_description_thresholds.py:281-330` checks number tokens, action text, entry/source metadata and quote; `:491-500` fetches the registered source URL and tests the quote's presence. S057 in `corpus/SOURCES.md:70` is a served documentation URL. The counter's successful quote check therefore does not establish the two code behaviors. The previously recorded source readings (`.ufo/waves/round-55/build/ScribeC1Cells.md:67-70`) supply URLs, pinned commit, quoted lines, byte counts and hashes, but not committed source bytes. The report's key depth/control finding survives.

## Attack / qualification

- **No direct falsification of the code proposition:** the report candidly did not re-fetch, and the current checkout contains no TypeScript snapshot to inspect at the pinned upstream commit. The cited r55 record is credible evidence that source was fetched and inspected then, but is not independently reproducible from committed bytes today. Verdict is therefore about evidence/control, not proof the upstream code claim is false.
- **Replacement scope is overstated as a defect:** the entry says the docs site banner replaces Gemini CLI *for unpaid-tier and Google One users*. That does not establish that Gemini CLI is unavailable to all users or that its technical behavior ceased to matter. `SKILL.md:174` is framed as the client behavior, not a claim that every audience can use it. The dropped qualifier/cadence is a useful freshness caveat, but not by itself a demonstrated false product-level assertion.
- **Eight-hex pin criticism is partly weak:** the source URL itself contains the full commit hash (as recorded in r55 evidence); `SKILL.md` presents an 8-hex abbreviation for readability. `corpus/SOURCES.md:59,73` associates the full hash with the same upstream commit but for a different file. Abbreviation is not inherently ambiguous in the URL/source record, so treating its form alone as a material evidence failure overstates the case. The absence of the actual TS bytes remains the stronger finding.
- **C2 proposed detector is not sufficient as written:** exact-line checks plus a grep for a few slice spellings do not establish absence of all truncation/length logic in relevant call paths (e.g. helper calls, other guard forms, or transformations). Its byte hash verifies identity, not semantic completeness. A proper source-level control would need an auditable inspection/test boundary, not rely on that narrow grep as a conclusive negative.
- **C3 cadence is not self-enforcing:** adding `recheck: 30d — <command>` in prose does not cause an audit to execute or fail when overdue absent a counter that parses and enforces it. Also, re-fetching immutable bytes at the same commit is a provenance/reproducibility check, not detection of later upstream changes; current-upstream drift requires a separate latest-revision check while preserving the historical pin.

## Outcome

The central claim—7/7 counter output does not certify Gemini's code-level clause, and the committed repository lacks the cited TypeScript bytes—survives. The report is calibrated in distinguishing the scope of the two functions from runtime behavior. Its stronger claims that the replacement makes the row product-level stale and that the short hash is materially defective are not established by the cited evidence. Proposed C2/C3 improve traceability only if strengthened with semantic coverage and an enforced freshness mechanism.

Report path (relative to `kotoba-shokunin`): `.ufo/waves/round-75/w2/R75Attack49.md`
