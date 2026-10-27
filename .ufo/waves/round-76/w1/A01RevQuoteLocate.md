# A01RevQuoteLocate — quote audit

## Result: blocked on missing draft

At inspection time, neither `.ufo/waves/round-76/build/` nor `corpus/knowledge/description-craft-round76.md` existed. Therefore there were no claimed quote strings to re-locate or word-count, and I cannot report a quote-level pass/fail verdict without inventing the entry's contents.

## Snapshot facts established

Pinned bytes inspected:
- `.ufo/waves/round-76/snapshots/optimizing-descriptions.md`
- `.ufo/waves/round-76/snapshots/evaluating-skills.md`
- `.ufo/waves/round-76/snapshots/best-practices.md`

In the optimizing-descriptions snapshot, lines 1–4 are Documentation Index/site chrome; the first page heading is `# Optimizing skill descriptions` at line 5. Thus any candidate quote must be located at line 5 or later (and must actually belong to the page content, not the heading/index chrome); the round plan specifically requires quotes after the first heading. No candidate strings were available for checks of verbatimness, shaping/Q53 dropped-byte disclosure, <=25-word count, or occurrence in the other two snapshots.

## Evidence / limitation

The round contract at `plans/round-76.md` §C1(b) requires at least four located quotes in the entry. The wave's `build/` directory was empty and the entry path was absent when checked. Re-run this audit against the draft/committed entry once the scribe artifact exists; this report makes no claim that the quote conjunct passes or fails.