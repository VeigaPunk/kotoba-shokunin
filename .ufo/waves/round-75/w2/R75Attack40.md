# R75Attack40 — Facet 40

Axes: consistency (claim matches evidence), operability (proposed control is implementable/non-vacuous).

## Verdict
Finding materially survives, with one calibration: the *central explicit* claim is well-scoped and should not be treated as an assertion that no client can execute the format. The source-row criticism is true, but the proposed remediation (“make the S065 source row's claim/anchor explicitly cover the plugin passage”) is not the smallest safe correction: no source bytes for that plugin passage are stored at this revision, so merely expanding the S065 row would assert evidence not represented by its captured hash/anchor. A separately captured committed source note, or citation to one, is needed.

## Evidence
Measured lane tip is `65a5c7a663249e0522cc49e4a148424200d9ddfe`. Reopened `corpus/knowledge/skill-eval-artefacts-round70.md:76-82`: it expressly says no claim that a client runs evals.json natively, distinguishes an opt-in user-installed/invoked plugin, and points to ScoutClientRuns. Thus the report correctly rejects any universal-absence inference. However `corpus/SOURCES.md:78` describes S065 as supporting a user-typed skill invocation, with quote/anchor at `skills.md:547` and disable flag `:577`; it does not preserve plugin details at `:968/:981`.

The cited committed note `.../round-70/w1/ScoutClientRuns.md:23-26` does document the exact plugin statements and user invocation, and at line 115 explicitly says new SOURCES rows are needed for those docs. This is enough to show the knowledge paragraph has a concrete cited evidentiary path, but the report is right that S065's registry metadata alone is not provenance for the plugin assertion. The note is a reviewer artifact, not the source snapshot; the `.ufo/waves/round-70/snapshots/` directory contains S209-S211 only (no captured Claude docs snapshot). This bears on the proposed reusable source/provenance fix, not the paragraph's bounded current statement.

I re-opened the target lines and note independently. The suggested check (read note + committed S065 bytes/statement then source-census/provenance checks) is only partially operable as phrased: there are no S065 source bytes in that snapshots directory to inspect, and no exact mechanical check or command named. Correct cheap check is compare registry row to its anchor/quote and ensure a captured artifact supports the plugin-specific text; the referenced note suffices to establish the mismatch, not primary-source byte integrity.

## Smallest safe correction
Keep the explicit native-vs-plugin qualification and narrow no-client claim. For a durable source claim, add a distinct source row/captured snapshot (or otherwise commit the fetched source bytes with hash and anchor) for the plugin passage; do not broaden S065's existing invocation claim without that evidence. No lane edits made; no live fetch or checks run.

Report trailer: Facet 40; measured tip 65a5c7a663249e0522cc49e4a148424200d9ddfe; evidence committed bytes at cited paths/lines; no live fetch or source edit performed.