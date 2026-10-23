Result: PARTIAL — identified an 18-line prose move and drafted its unified diff, but the scribe role forbids applying product edits or running another runtime, so no patch or gate result is claimed.

## Findings

- The target is at the stated budget: the observed `SKILL.md` ends at line 598; its checklist caps the file at 600 (`SKILL.md:300-302`). The plan says the line-budget move must preserve all nine agent-definition box texts (`plans/round-56.md:73-76`).
- Candidate: the two paragraphs under `## Frontmatter craft — the trigger surface`, `SKILL.md:157-175`. This is 18 prose lines plus the separating blank line. Their detail is already held in `corpus/knowledge/render-mechanism-round7.md:75-94` and `corpus/knowledge/frontmatter-trigger-surface.md:54-84`; the latter is the authoritative twelve-rule treatment. The move avoids the excluded agent-definition checklist, r54/r55 tables, Gate registry, and frontmatter.
- Proposed budget effect: replace the 19 physical lines (18 prose + 1 blank) with one pointer, reducing SKILL.md by 18 lines; with the planned ~12-line C1 addition, the estimate is 592 lines. This is arithmetic from the stated/current count, not a measured post-patch result. [INFERENCE]
- The round-55 precedent records a verbatim move and equal before/after SHA-256 for the moved bytes (`corpus/lessons/round-55-verifier-spotcheck.md:95`; example detail in `corpus/knowledge/skill-overlap-levers-round51.md:146-150`).

## Proposed unified diff — not applied

```diff
--- a/SKILL.md
+++ b/SKILL.md
@@ -155,24 +155,6 @@
 ## Frontmatter craft — the trigger surface
 
-`description` is an index, not a summary. On **omp** the router ingests it
-through a **cache-or-truncate** render (mechanism proven from the omp binary,
-`corpus/knowledge/render-mechanism-round7.md`): a
-`sha256(prompt ‖ 0x00 ‖ name ‖ 0x00 ‖ loader-held description)` hit in
-`~/.omp/agent/skill-descriptions.db` renders that cache line; a miss keeps at
-most 99 chars. The cache key includes the description, so **editing a
-`description` invalidates its row and reverts the skill to the truncator** until
-the compressor rewrites it. On **opencode** the full description reaches the
-model untruncated; trigger strings and anti-triggers are mandatory on both
-because the offer gate and the model's own matching both read the description.
-
-Twelve rules with the measurements behind each — capability clause first, quote
-literal *and* implicit-need triggers, co-locate anti-triggers (body-only
-exclusions cannot prevent activation), name the overlapping sibling and its
-arbitration rule, the 99-char cliff and its 55–96 effective keep, the ≥40-char
-first-sentence branch that discards sentence 2+, the CJK `[.!?]`-only sentence
-regex, `metadata.requires` over prose, render-by-reproduction, invocation-shaped
-triggers for domain-term names, and the discovery roots:
-`corpus/knowledge/frontmatter-trigger-surface.md` § Craft rules.
+Render mechanism: `corpus/knowledge/render-mechanism-round7.md` § Moved from `SKILL.md` § Frontmatter craft (round 56); craft rules: `corpus/knowledge/frontmatter-trigger-surface.md` § Craft rules.
 
 Portability floor (spec + vendor + YAML, `corpus/SOURCES.md` S018, S002, S019, S008): `name` ≤64 lowercase letters, digits and single hyphens, equal to the directory (the spec's charset wording is ambiguous on Unicode); `description` ≤1024 chars, no XML tags (Anthropic rule), quoted when it holds `: ` or ` #` (illegal in a YAML plain scalar — lenient loaders hide it, strict ones reject). `verifiers/verify_skill_checklist.py` `trigger.no_xml_tag` approximates the XML-tag rule lexically on the unparsed `name`/`description` text; Anthropic's packager (S012) refuses any `<`/`>` in the parsed value, so the two disagree in both directions. Which authority imposes which rule, with run counterexamples: `corpus/knowledge/frontmatter-rule-authorities-round48.md`.
--- a/corpus/knowledge/render-mechanism-round7.md
+++ b/corpus/knowledge/render-mechanism-round7.md
@@ -92,3 +92,25 @@
 - **Verify by reproduction, not logs**: re-run H7s (recipe above) on a new
   description to see the actual router view; the sqlite cache table lists
   which skills escaped truncation.
+
+## Moved from `SKILL.md` § Frontmatter craft (round 56)
+
+`description` is an index, not a summary. On **omp** the router ingests it
+through a **cache-or-truncate** render (mechanism proven from the omp binary,
+`corpus/knowledge/render-mechanism-round7.md`): a
+`sha256(prompt ‖ 0x00 ‖ name ‖ 0x00 ‖ loader-held description)` hit in
+`~/.omp/agent/skill-descriptions.db` renders that cache line; a miss keeps at
+most 99 chars. The cache key includes the description, so **editing a
+`description` invalidates its row and reverts the skill to the truncator** until
+the compressor rewrites it. On **opencode** the full description reaches the
+model untruncated; trigger strings and anti-triggers are mandatory on both
+because the offer gate and the model's own matching both read the description.
+
+Twelve rules with the measurements behind each — capability clause first, quote
+literal *and* implicit-need triggers, co-locate anti-triggers (body-only
+exclusions cannot prevent activation), name the overlapping sibling and its
+arbitration rule, the 99-char cliff and its 55–96 effective keep, the ≥40-char
+first-sentence branch that discards sentence 2+, the CJK `[.!?]`-only sentence
+regex, `metadata.requires` over prose, render-by-reproduction, invocation-shaped
+triggers for domain-term names, and the discovery roots:
+`corpus/knowledge/frontmatter-trigger-surface.md` § Craft rules.
```

## Gates, evidence, and limits

- No shell command was run. In particular, neither the requested before/after `sed -n … | sha256sum` checks nor `python3 -B verifiers/verify_skill_checklist.py` ran. No equality hash or PASS result is claimed; the after-side bytes do not exist because this diff was not applied.
- No sandbox clone was created and no product file, verifier, counter, judge, or lane Git/jj state was edited. No tools were installed or updated.
- Touched surface: this report only, `.ufo/waves/round-56/build/ScribeSkillBudget.md`. The proposed diff changes `SKILL.md` and appends to `corpus/knowledge/render-mechanism-round7.md`, but is report text, not a working-tree change.
- Out of scope under the scribe role: applying the proposed patch, producing execution evidence, and measuring the combined C1 table plus move. These require an authorized executor in its sandbox. The current line count, predicted result, and exact byte hashes after movement remain unverified.
