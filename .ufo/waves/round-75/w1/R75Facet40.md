# Facet 40 — source scope and calibration boundary

## Observation
`corpus/knowledge/skill-eval-artefacts-round70.md:76-82` explicitly limits itself to the two Agent Skills evaluation guides plus one implementation, disclaims native client execution, and distinguishes Claude Code's opt-in `skill-creator` plugin from client behavior. This boundary is appropriately falsifiable: lines 1-5 identify sources S209–S213 and S065, while `corpus/SOURCES.md:150-153` records S209/S210 and superseding upstream-pinned S212/S213; `corpus/SOURCES.md:78` identifies S065 but its row's stated claim is direct user invocation, not the plugin passage.

## Assessment
The no-native-client claim is calibrated to the evidence named in the paragraph (“none of the three sources says so” and “lane has not observed it”); it does not establish that no client supports native execution. The plugin claim's supporting row is weaker than its use: the cited paragraph says S065 was re-read for this near-miss (`...round70.md:4`), but S065's current registry claim at `SOURCES.md:78` is about user-typed invocation. This is not necessarily unsupported—the paragraph points to the separate reviewer note `.ufo/waves/round-70/w1/ScoutClientRuns.md`—but the registry row does not itself preserve the plugin-specific proposition. Confidence: high on scope/disclaimer from committed text; medium on plugin sourcing until the cited reviewer artifact is opened.

## Concrete check/control
At the committed revision, open `.ufo/waves/round-70/w1/ScoutClientRuns.md` and the committed S065 snapshot/bytes, locate the exact statements corresponding to lines 968 and 981, and verify the plugin is described as opt-in/user-installed rather than native client behavior. If retained as a reusable factual claim, make the S065 source row's claim/anchor explicitly cover the plugin passage (or cite a separate captured committed source note); then rerun the source-census and provenance checks. Do not generalize the observation into a universal absence claim.

## Evidence commands
- `read corpus/knowledge/skill-eval-artefacts-round70.md:1-5,76-84`
- `read corpus/SOURCES.md:78,150-153` (row 78 is S065; rows 150-153 are S209/S210/S212/S213)

Report trailer: `Facet 40; evidence committed bytes at the cited paths/lines; no live fetch or source edit performed.`
